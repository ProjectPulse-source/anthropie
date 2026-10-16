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

Après contre-expertise (anthropie-site-20261016-154235) : six motifs (s'ajoutent l'extremum par clé et la ligne
compactée), balayage des octets sur le texte entier.

COUVERTURE EXACTE -- ce qu'il ne voit pas, dit ici :
- une comparaison stricte `a["x"] > b["x"]` d'une garde de prose (motif trop fréquent hors prose pour être interdit
  mécaniquement : seuils, boucles, tests de cohérence) ; elle passe par `lg.depasse` à l'adoption ;
- toute expression répartie sur plusieurs lignes, `np.argmax`, un tri suivi d'un `enumerate` ou d'un `[0]` publié
  comme « le premier », un compactage écrit autrement que `[c for c in r if c is not None]` ;
- la PERTINENCE d'un `brut-ok` : il exige un motif, il ne le juge pas. `--exceptions` les liste pour la revue.
La relecture du texte servi et la contre-expertise restent la défense de ce qui échappe aux motifs.
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
    # Ajout après contre-expertise (point 6) : l'élément extrême choisi par une clé -- une année de pic, un pays -- se
    # choisit au chiffre affiché (lg.extremum ; lg.sommets pour dire un plateau). 70 occurrences au 16/10.
    ("extremum par cle sur valeur brute (lg.extremum / lg.sommets)", re.compile(r"\b(max|min)\([^#]*\bkey\s*=")),
    ("ligne compactee avant lecture par position (lt.colonnes / lt.cellules / lt.serie)",
     re.compile(r"\[\s*c\s+for\s+c\s+in\s+r\s+if\s+c\s+is\s+not\s+None\s*\]")),
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
    # Sur le texte ENTIER (contre-expertise anthropie-site-20261016-154235) : splitlines() traite \x0b \x0c \x1c-\x1e et
    # U+0085 comme des fins de ligne et les faisait disparaître avant l'examen. Ligne = nombre de \n avant l'octet.
    return ["%s:%d : octet de controle U+%04X (barre oblique inverse mangee a l'ecriture ?)"
            % (nom, texte.count("\n", 0, m.start()) + 1, ord(m.group())) for m in OCTETS.finditer(texte)]


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
        # Cas de la contre-expertise du 16/10, devenus permanents :
        ("pmax = max(pat, key=lambda x: x['patrimoine_net'])", True),
        ("ypic = max(serie, key=serie.get)", True),
        ("ypic = lg.extremum(serie, serie.get, 1)", False),
        ("f8 = [[c for c in r if c is not None] for r in wb['Figure 8'].iter_rows(values_only=True)]", True),
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
    # Octets que splitlines() avalait (contre-expertise) : chacun doit être vu, à la bonne ligne.
    for o in (0x0B, 0x0C, 0x1C, 0x1D, 0x1E, 0x85):
        vu = octets("t", "a = 1\nb = 'x" + chr(o) + "y'\n")
        if len(vu) != 1 or not vu[0].startswith("t:2 "):
            rate.append("octet U+%04X mal vu : %r" % (o, vu))
    if rate:
        for c in rate:
            print("  TEMOIN RATE : " + c.encode("ascii", "replace").decode())
        print("Temoin : %d cas sur %d mal juges. ECHEC" % (len(rate), len(cas)))
        return 1
    print("Temoin : %d cas, chacun juge comme attendu (%d motifs vus, exception motivee admise, exception muette refusee, "
          "6 octets que splitlines avalait)." % (len(cas), len(MOTIFS)))
    return 0


def exceptions() -> int:
    """Revue des `brut-ok` : un motif est exigé, sa pertinence se juge ici, à la revue (contre-expertise, point 6)."""
    n = 0
    for p in fichiers():
        for k, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            m = EXCEPTION.search(ligne)
            if m and any(rx.search(ligne) for _, rx in MOTIFS):
                n += 1
                print("  %s:%d : %s" % (p.name, k, (m.group(1) or "").encode("ascii", "replace").decode()))
    print("Exceptions motivees : %d" % n)
    return 0


def main() -> int:
    if "--temoin" in sys.argv:
        return temoin()
    if "--exceptions" in sys.argv:
        return exceptions()
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
