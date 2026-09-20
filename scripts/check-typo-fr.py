#!/usr/bin/env python3
"""Linter typographique français — espaces insécables manquantes dans le contenu.

MOTIF (2026-09-20, consigne de l'auteur : « règle pour tout le site »). Le
français impose une espace insécable devant la ponctuation haute (; : ! ?),
autour des guillemets et devant les unités (%, €). Sans elle, le navigateur
peut rejeter le signe seul en début de ligne : « 3 536,1 milliards d'euros » se
coupe après « d'euros » et le « € » atterrit à la ligne suivante. Sur une page
dont l'argument EST le chiffre, la coupure abîme précisément ce qu'on montre.

POURQUOI UN LINTER ET PAS UN FILTRE AU RENDU
    Le site possède déjà `layouts/partials/fr-typo.html`, appliqué aux TITRES.
    L'étendre au corps rendu exigerait de transformer du HTML déjà assemblé :
    il faudrait épargner les attributs, le code, les URL et le JavaScript inline
    de la page dette — où « a ? b : c » deviendrait une expression ponctuée
    d'insécables. Corriger la SOURCE est déterministe et se relit dans un diff.

CE QUE CE LINTER VÉRIFIE (et seulement cela)
    Une espace ORDINAIRE suivie de ; : ! ? », précédée de «, ou séparant un
    chiffre de % ou €. Les insécables déjà posées — &nbsp;, U+00A0, U+202F —
    ne sont pas des fautes et ne sont jamais retouchées.

CE QU'IL NE REGARDE PAS, ET POURQUOI
    Front matter, blocs et fragments de code, shortcodes, balises HTML brutes
    et URL : une espace avant « : » y est normale ou significative. Les
    signaler apprendrait à ignorer le linter.

USAGE
    python scripts/check-typo-fr.py             # signale tout, sort 1 si faute
    python scripts/check-typo-fr.py --corriger  # applique partout, sort 0
    python scripts/check-typo-fr.py --corriger content/x.md content/y.md
        # ne touche QUE ces fichiers. Utile quand une autre session edite le
        # depot en parallele : une correction de masse ecraserait son travail
        # en cours, et rien ne le signalerait.
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

# La console Windows sort en cp1252 : sans cette reconfiguration, imprimer un
# extrait accentué ferait échouer le linter sur un corpus sain — et l'échec
# technique serait indiscernable d'une détection.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
# Les pages anglaises sont hors champ : l'anglais ne met pas d'espace devant
# « : » et place le symbole AVANT le nombre (« €19 »). Appliquer la regle
# francaise y introduirait la faute qu'on pretend corriger. Verifie le 20/09 :
# les seules insecables presentes dans les .en.md tiennent a des TITRES
# francais cites en anglais, ou elles sont justes -- le hasard, pas la regle.
CIBLES = sorted(f for f in (RACINE / "content").rglob("*.md")
                if not f.name.endswith(".en.md"))

NBSP = "&nbsp;"

# Zones où une espace avant « : » est normale : on les met de côté avant
# d'analyser, on les remet ensuite, à l'identique.
PROTEGES = [
    # Front matter : `\r?\n` et non `\n`, sinon les fichiers en CRLF passent au
    # travers et le linter propose d'ecrire `&nbsp;` dans un `title:` — qui
    # ressort tel quel dans les balises meta. Defaut vu au premier essai.
    re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.S),
    re.compile(r"<!--.*?-->", re.S),               # commentaire HTML, souvent multiligne
    re.compile(r"```.*?```", re.S),                # bloc de code
    re.compile(r"`[^`\n]*`"),                      # code en ligne
    re.compile(r"\{\{[<%].*?[>%]\}\}", re.S),      # shortcodes Hugo
    re.compile(r"<[^>\n]+>"),                      # balise HTML brute
    re.compile(r"\]\([^)\n]*\)"),                  # cible d'un lien
    re.compile(r"https?://\S+"),                   # URL nue
]

REGLES = [
    ("ponctuation haute", re.compile(r"(?<=\S) (?=[;:!?»])")),
    ("ouvrante", re.compile(r"(?<=«) (?=\S)")),
    ("unite", re.compile(r"(?<=[0-9]) (?=[%€])")),
]


def masquer(txt: str):
    """Remplace les zones protégées par des jetons non ambigus."""
    coffre: list[str] = []

    def prendre(m):
        coffre.append(m.group(0))
        return "\x00%d\x00" % (len(coffre) - 1)

    for motif in PROTEGES:
        txt = motif.sub(prendre, txt)
    return txt, coffre


def demasquer(txt: str, coffre: list[str]) -> str:
    for i, brut in enumerate(coffre):
        txt = txt.replace("\x00%d\x00" % i, brut)
    return txt


def analyser(txt: str):
    """Rend (texte corrigé, liste des occurrences)."""
    masque, coffre = masquer(txt)
    trouve = []
    for nom, motif in REGLES:
        for m in motif.finditer(masque):
            ligne = masque.count("\n", 0, m.start()) + 1
            extrait = masque[max(0, m.start() - 40):m.start() + 30]
            trouve.append((ligne, nom, " ".join(extrait.split())))
        masque = motif.sub(NBSP, masque)
    return demasquer(masque, coffre), trouve


def main() -> int:
    args = sys.argv[1:]
    corriger = "--corriger" in args
    explicites = [a for a in args if not a.startswith("--")]
    cibles = CIBLES
    if explicites:
        cibles = [Path(a) if Path(a).is_absolute() else RACINE / a for a in explicites]
        manquants = [str(c) for c in cibles if not c.is_file()]
        if manquants:
            print("Fichier(s) introuvable(s) : %s" % ", ".join(manquants))
            return 2

    total = 0
    touches = 0
    for f in cibles:
        brut = io.open(f, encoding="utf-8", newline="").read()
        corrige, trouve = analyser(brut)
        if not trouve:
            continue
        touches += 1
        total += len(trouve)
        rel = f.relative_to(RACINE)
        print("%s : %d" % (rel, len(trouve)))
        for ligne, nom, extrait in trouve[:3]:
            print("    l.%-5d %-18s ...%s..." % (ligne, nom, extrait))
        if len(trouve) > 3:
            print("    (+%d autres)" % (len(trouve) - 3))
        if corriger:
            io.open(f, "w", encoding="utf-8", newline="").write(corrige)

    if not total:
        print("Typographie : aucune espace insecable manquante. OK")
        return 0
    if corriger:
        print("\n%d correction(s) appliquee(s) dans %d fichier(s)." % (total, touches))
        return 0
    print("\n%d espace(s) insecable(s) manquante(s) dans %d fichier(s)."
          % (total, touches))
    print("Corriger : python scripts/check-typo-fr.py --corriger")
    return 1


if __name__ == "__main__":
    sys.exit(main())
