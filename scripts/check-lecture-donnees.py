"""check-lecture-donnees.py -- les générateurs lisent et classent comme le lecteur lit.

    python scripts/check-lecture-donnees.py            contrôle (dans check-all --ci, BLOQUANT)
    python scripts/check-lecture-donnees.py --temoin   témoin positif : chaque motif injecté doit être vu

Né le 2026-10-16 de deux défauts de structure trouvés le même jour, corrigés à l'échelle des générateurs :
1. Une source change la FORME d'un tableur (Insee Première n° 2130 : années écrites en texte) et un filtre
   `if isinstance(r[0], (int, float))` écarte toutes les lignes en silence ; variante pire, `... else 0.0` fabrique un
   zéro pour une cellule illisible. Organe commun : scripts/lecture_tableur.py (annee, nombre, valeur, entetes, ligne).
2. Un rang, une position d'extremum ou un « dépasse » calculés sur la valeur BRUTE publient un ordre que le lecteur ne
   voit pas (Belgique 2,2285 % contre France 2,2278 %, toutes deux affichées 2,23 % : « huitième rang »). Organe
   commun : scripts/langue_generee.py (rang, depasse, positions, position_unique).

Ce contrôle refuse, dans les générateurs (scripts/update_*.py, generer_*.py, og_*.py, dette_*.py), les quatre motifs
qui reproduisent ces défauts. Exception possible, jamais muette : `# brut-ok: <motif>` sur la ligne (un diagnostic
écrit en clair dans un JSON, une étiquette posée sur une barre qui affiche sa propre valeur…) ; un `brut-ok` sans
motif est refusé.

Ce qu'il ne voit pas, dit ici : une comparaison stricte `a["x"] > b["x"]` d'une garde de prose (motif trop fréquent
hors prose pour être interdit mécaniquement : seuils, boucles, tests de cohérence). Elle passe par `lg.depasse` à
l'adoption ; la relecture du texte servi et la contre-expertise restent la défense.
Condition de mort : aucune -- permanent tant que des générateurs lisent des tableurs et publient des rangs (R2, revue
annuelle). Sortie console ASCII pur.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
MOTIFS_GLOB = ("update_*.py", "generer_*.py", "og_*.py", "dette_*.py")

MOTIFS = [
    # Deux formes : l'index d'une liste triée sur place, et `.index(x) + 1` sur une liste triée plus haut (témoin du
    # 16/10 sur le code d'avant : `[x["code"] for x in classement].index("FR") + 1` échappait à la première).
    ("rang sur valeur brute (lg.rang)", re.compile(r"sorted\(.*\)\s*\.index\(|\.index\(.*\)\s*\+\s*1")),
    ("position d'extremum sur valeur brute (lg.positions / lg.position_unique)", re.compile(r"\.index\(\s*(max|min)\(")),
    ("cellule illisible lue comme zero (lt.nombre, et arret si None)",
     re.compile(r"isinstance\([^)]*\(\s*int\s*,\s*float\s*\)\s*\)\s+else\s+0")),
    ("ligne de tableur filtree par le type de sa premiere cellule (lt.annee / lt.nombre)",
     re.compile(r"if\s+isinstance\(\s*r\[\d+\]\s*,\s*\(\s*int\s*,\s*float\s*\)\s*\)")),
]
EXCEPTION = re.compile(r"#\s*brut-ok\s*:\s*(\S.*)?$")


def examiner(nom: str, texte: str) -> list[str]:
    out = []
    for n, ligne in enumerate(texte.splitlines(), 1):
        if ligne.lstrip().startswith("#"):
            continue                                  # ligne de commentaire ; la ligne entière sinon (« #184f95 »)
        for quoi, rx in MOTIFS:
            if rx.search(ligne):
                m = EXCEPTION.search(ligne)
                if m and m.group(1):
                    continue
                out.append("%s:%d : %s%s" % (nom, n, quoi, " -- brut-ok SANS motif" if m else ""))
    return out


# Cinquième défaut, même famille (trouvé le 16/10 en écrivant ce contrôle) : une barre oblique inverse mangée par le
# canal d'écriture (heredoc, commande Bash) laisse un octet de contrôle à sa place. `r"\bmissing\b"` était devenu
# BS + missing + BS dans update_dette_baisse.py le 11/10 : la garde de mots interdits ne pouvait plus mordre, sans
# erreur. Balayage de TOUS les scripts/*.py, C0 et C1 (leçon « octets de contrôle par échappement : balayer »).
OCTETS = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")


def octets(nom: str, texte: str) -> list[str]:
    return ["%s:%d : octet de controle U+%04X (barre oblique inverse mangee a l'ecriture ?)" % (nom, n, ord(m.group()))
            for n, ligne in enumerate(texte.splitlines(), 1) for m in [OCTETS.search(ligne)] if m]


def fichiers() -> list[Path]:
    vus = set()
    for g in MOTIFS_GLOB:
        for p in sorted(SCRIPTS.glob(g)):
            if p not in vus:
                vus.add(p)
                yield p


def temoin() -> int:
    cas = [
        ("rang = sorted(rows, key=lambda x: -x['charge']).index(F) + 1", True),
        ("rang = [x['code'] for x in classement].index('FR') + 1", True),
        ("rang_prix_euro = euro_prix.index(F) + 1", True),
        ("an = annees[stabs.index(max(stabs))]", True),
        ("v = [abs(float(x)) if isinstance(x, (int, float)) else 0.0 for x in r]", True),
        ("serie = [r for r in f3 if isinstance(r[0], (int, float))]", True),
        ("imax = rat.index(max(rat))   # brut-ok: etiquette d'une barre qui affiche sa valeur", False),
        ("imax = rat.index(max(rat))   # brut-ok:", True),
        ("rang, eg = lg.rang(v, 'FR', 2)", False),
    ]
    rate = [c for c, attendu in cas if bool(examiner("temoin", c)) != attendu]
    # Mutation d'un VRAI générateur, en mémoire : l'ancienne ligne du rang (avant le 16/10) doit être vue.
    vrai = (SCRIPTS / "update_dette_monde.py").read_text(encoding="utf-8")
    ancre = '    rang_ipib, egaux_ipib = lg.rang(ipib, "FR", 2)'
    if ancre not in vrai:
        rate.append("ancre de mutation absente de update_dette_monde.py")
    elif not examiner("mutation", vrai.replace(ancre, '    rang_ipib = sorted(ipib, key=lambda c: -ipib[c]).index("FR") + 1', 1)):
        rate.append("mutation de update_dette_monde.py non vue")
    if not octets("mutation", 'INTERDITS = [r"' + chr(8) + 'missing' + chr(8) + '"]') or octets("sain", 'r"\\bmissing\\b"'):
        rate.append("balayage des octets de controle mal juge")
    if rate:
        for c in rate:
            print("  TEMOIN RATE : " + c.encode("ascii", "replace").decode())
        print("Temoin : %d cas sur %d mal juges. ECHEC" % (len(rate), len(cas)))
        return 1
    print("Temoin : %d cas, chacun juge comme attendu (4 motifs vus, exception motivee admise, exception muette refusee)." % len(cas))
    return 0


def main() -> int:
    if "--temoin" in sys.argv:
        return temoin()
    defauts, n = [], 0
    for p in fichiers():
        n += 1
        defauts += examiner(p.name, p.read_text(encoding="utf-8"))
    for p in sorted(SCRIPTS.glob("*.py")):
        defauts += octets(p.name, p.read_text(encoding="utf-8"))
    if defauts:
        for d in defauts:
            print("  " + d.encode("ascii", "replace").decode())
        print("Lecture et rangs des generateurs : %d defaut(s) dans %d fichier(s). ECHEC" % (len(defauts), n))
        return 1
    print("Lecture et rangs des generateurs : %d fichier(s), aucun motif interdit. OK" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
