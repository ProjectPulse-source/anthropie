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

Complétés après contre-expertise (anthropie-site-20261016-154235) : grammaire stricte et ambiguïté refusée, valeurs non
finies refusées, entier() pour les effectifs, colonnes() / cellules() / serie() pour lire par POSITION IDENTIFIÉE (jamais
après compactage), annees_continues() pour qu'une année manquante arrête au lieu de disparaître.

Ce qui reste au générateur, et ne se tolère pas : l'ORDRE et l'INTITULÉ des colonnes, que chaque générateur compare
après normalisation, et ses témoins de concordance. On tolère la forme, jamais le sens.

Contrôle : scripts/check-lecture-donnees.py (dans check-all --ci) refuse l'idiome `if isinstance(..., (int, float))`
sur une ligne de tableur et le repli `else 0` d'un lecteur ; tests : scripts/test_lecture_tableur.py.
Condition de mort : aucune -- organe permanent tant qu'un générateur lit un tableur (R2, revue annuelle).
"""
from __future__ import annotations

import math
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


# Grammaire d'un nombre écrit en texte (contre-expertise anthropie-site-20261016-154235, point 1) : on accepte la
# souplesse qui ne laisse aucun doute, on refuse l'ambiguïté. Milliers par espace en groupes de trois exactement ;
# décimales par virgule ; point décimal seulement s'il ne peut pas être un séparateur de milliers (« 10.1 », « 0.354 »).
# « 1.234 » et « 1,234 » (trois chiffres après un séparateur, partie entière non nulle) sont AMBIGUS : None, sauf si
# l'appelant déclare la convention de sa source (decimal="," ou ".").
_FR = re.compile(r"-?(\d{1,3}(?: \d{3})+|\d+)(,\d+)?")
_POINT = re.compile(r"-?\d+\.\d+")
_AMBIGU = re.compile(r"-?[1-9]\d{0,2}[.,]\d{3}")


def _fini(x: float) -> float | None:
    return x if math.isfinite(x) else None


def nombre(v, decimal: str | None = None) -> float | None:
    """Nombre écrit en nombre ou en texte ; None si absent, illisible, ambigu ou non fini (NaN, infini).

    decimal : convention de la source quand elle est connue (« , » ou « . ») ; seule elle lève l'ambiguïté de
    « 1.234 » / « 1,234 »."""
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return _fini(float(v))
    if not isinstance(v, str):
        return None
    s = _texte(v).replace("−", "-")
    if s.endswith("%"):
        s = s[:-1].rstrip()                       # un seul signe %, pas « 12%% »
    if s.lower() in ABSENCE or not s:
        return None
    if _AMBIGU.fullmatch(s) and decimal is None:
        return None
    if decimal == ".":
        s2 = s.replace(",", "").replace(" ", "")
        return _fini(float(s2)) if re.fullmatch(r"-?\d+(\.\d+)?", s2) else None
    if decimal == "," and re.fullmatch(r"-?\d{1,3}(\.\d{3})+(,\d+)?", s):
        s = s.replace(".", " ")                   # milliers par point, convention déclarée
    if _FR.fullmatch(s):
        return _fini(float(s.replace(" ", "").replace(",", ".")))
    if _POINT.fullmatch(s) and decimal != ",":
        return _fini(float(s))
    return None


def valeur(v, decimal: str | None = None) -> int | float | None:
    """Comme nombre(), mais un nombre garde son type (entier ou décimal) : pour une sortie publiée qui écrit les
    entiers de la source tels quels (« -6400 », pas « -6400.0 »). Un texte lu devient un décimal."""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return v if math.isfinite(v) else None
    return nombre(v, decimal)


def entier(v) -> int | None:
    """Effectif : un entier mathématique (12, 12.0, « 1 234 ») ; None pour 12,5 -- jamais un int() qui tronque."""
    x = nombre(v)
    return int(x) if x is not None and x.is_integer() else None


def colonnes(row, attendus) -> list[int]:
    """Positions des colonnes `attendus` dans une ligne d'en-tête, repérées par leur libellé normalisé ou, pour une
    année, par annee(). ValueError si l'une manque ou figure deux fois : on lit par position IDENTIFIÉE, jamais
    après avoir compacté la ligne (contre-expertise du 16/10 : un None retiré fait glisser 2021 dans 2024)."""
    lib = ligne(row)
    out = []
    for a in attendus:
        if isinstance(a, int):
            pos = [i for i, c in enumerate(lib) if annee(c) == a]
        else:
            pos = [i for i, c in enumerate(lib) if isinstance(c, str) and c == _texte(a)]
        if len(pos) != 1:
            raise ValueError("colonne %r : %d occurrence(s) dans l'en-tete %r" % (a, len(pos), lib))
        out.append(pos[0])
    return out


def cellules(row, positions, quoi: str = "ligne", decimal: str | None = None) -> list:
    """Valeurs aux positions données (type gardé) ; ValueError si l'une est absente ou illisible."""
    out = []
    for i in positions:
        v = valeur(row[i], decimal) if i < len(row) else None
        if v is None:
            raise ValueError("%s, colonne %d : valeur absente ou illisible (%r)" % (quoi, i, row[i] if i < len(row) else None))
        out.append(v)
    return out


def serie(row, debut: int = 1, quoi: str = "ligne") -> list:
    """Valeurs d'une ligne à partir de `debut`, colonnes vides de QUEUE retirées ; une cellule vide ou illisible au
    milieu lève ValueError (elle décalerait les suivantes)."""
    vals = entetes(row)[debut:]
    return cellules(vals, range(len(vals)), quoi)


def annees_continues(annees, premiere: int | None = None, derniere: int | None = None, quoi: str = "serie") -> list[int]:
    """Contrôle d'une série annuelle : années uniques, sans trou, bornes attendues. ValueError sinon -- une année
    illisible écartée au milieu ne doit pas passer sous un témoin qui ne regarde que les années gardées."""
    a = list(annees)
    if len(set(a)) != len(a):
        raise ValueError("%s : annee(s) en double %s" % (quoi, sorted({x for x in a if a.count(x) > 1})))
    s = sorted(a)
    if not s:
        raise ValueError("%s : aucune annee" % quoi)
    trous = [y for y in range(s[0], s[-1] + 1) if y not in set(s)]
    if trous:
        raise ValueError("%s : annee(s) manquante(s) %s" % (quoi, trous))
    if premiere is not None and s[0] != premiere:
        raise ValueError("%s : commence en %d, attendu %d" % (quoi, s[0], premiere))
    if derniere is not None and s[-1] != derniere:
        raise ValueError("%s : finit en %d, attendu %d" % (quoi, s[-1], derniere))
    return s
