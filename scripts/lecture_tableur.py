"""lecture_tableur.py -- lire une cellule de tableur d'une source publique sans dépendre de sa mise en forme.

Organe commun, né le 2026-10-16. L'Insee Première n° 2130 (empreinte carbone, données 2025) a changé la FORME de son
fichier sans en changer le fond : « Année » au singulier, colonnes vides en queue d'en-tête, années écrites en texte
(« 1990 ») au lieu de nombres. Le générateur filtrait les lignes par `isinstance(r[0], (int, float))` : toutes les
années du tableau complémentaire 2 sont sorties EN SILENCE, et seul un témoin de concordance l'a vu. Le même idiome,
et sa variante « sinon 0.0 », vivaient dans six générateurs. Ce module les remplace :

- ligne(row)    : textes normalisés, positions inchangées (pour un lecteur qui indexe ses colonnes) ;
- entetes(row)  : libellés normalisés (espaces insécables, blancs multiples), colonnes vides en queue retirées ;
- annee(v)      : une année, qu'elle soit écrite en nombre (1990, 1990.0) ou en texte (« 1990 ») ; None sinon ;
- valeur(v)     : comme nombre(), mais un nombre garde son type (sortie publiée identique) ;
- nombre(v)     : un nombre, écrit en nombre ou en texte au format français (« 1 234,5 », « 12,3 % ») ; None si
                  la cellule est vide ou porte un code d'absence (« /// », « nd », « s ») -- JAMAIS 0 pour une
                  donnée absente : manquant n'est pas zéro (doctrine R5).

Ce qui reste au générateur, et ne se tolère pas : l'ORDRE et l'INTITULÉ des colonnes, que chaque générateur compare
après normalisation, et ses témoins de concordance. On tolère la forme, jamais le sens.

Contrôle : scripts/check-lecture-donnees.py (dans check-all --ci) refuse l'idiome `if isinstance(..., (int, float))`
sur une ligne de tableur et le repli `else 0` d'un lecteur ; tests : scripts/test_lecture_tableur.py.
Condition de mort : aucune -- organe permanent tant qu'un générateur lit un tableur (R2, revue annuelle).
"""
from __future__ import annotations

import re

NBSP = (" ", " ", " ")
ABSENCE = {"", "///", "//", "-", "–", "—", "nd", "n.d.", "ns", "s", "nc", "..", "...", "x"}


def _texte(v) -> str:
    s = str(v)
    for c in NBSP:
        s = s.replace(c, " ")
    return " ".join(s.split())


def ligne(row) -> list:
    """Ligne de données : textes normalisés (insécables, blancs multiples), longueur et positions inchangées."""
    return [(_texte(c) if isinstance(c, str) else c) for c in row]


def entetes(row) -> list:
    """Libellés d'une ligne d'en-tête : texte normalisé, None conservé à sa place, None de queue retirés."""
    out = [(_texte(c) if isinstance(c, str) else c) for c in row]
    while out and (out[-1] is None or out[-1] == ""):
        out.pop()
    return out


def annee(v) -> int | None:
    """Année écrite en nombre ou en texte ; None pour tout le reste (libellé, note, cellule vide)."""
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v if 1000 <= v <= 2999 else None
    if isinstance(v, float):
        return int(v) if v.is_integer() and 1000 <= v <= 2999 else None
    if isinstance(v, str):
        s = _texte(v)
        m = re.fullmatch(r"(\d{4})(?:\s*\((?:p|sd|r|e|prov\.?)\))?(?:\s*[pre*])?", s)
        return int(m.group(1)) if m else None
    return None


def nombre(v) -> float | None:
    """Nombre écrit en nombre ou en texte (format français ou anglais simple) ; None si absent ou illisible."""
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if not isinstance(v, str):
        return None
    s = _texte(v).replace("−", "-").rstrip("%").strip()
    if s.lower() in ABSENCE:
        return None
    s = s.replace(" ", "")
    if re.fullmatch(r"-?\d+(,\d+)?", s):
        return float(s.replace(",", "."))
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        return float(s)
    return None


def valeur(v) -> int | float | None:
    """Comme nombre(), mais un nombre garde son type (entier ou décimal) : pour une sortie publiée qui écrit les
    entiers de la source tels quels (« -6400 », pas « -6400.0 »). Un texte lu devient un décimal."""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return v
    return nombre(v)
