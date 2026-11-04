# -*- coding: utf-8 -*-
"""generer_frise_durees.py -- frise des durées d'inscription, page /combien-de-temps-une-erreur-reste-inscrite/ (04/11/2026).

Ce que montre la figure : de six mois à quarante ans, les durées pendant lesquelles une trace reste inscrite, registre par
registre, sur une échelle logarithmique (seule échelle qui lise à la fois six mois et quarante ans). C'est la première
conclusion de la page, « la durée d'une trace ne dit pas la gravité de l'erreur ».

Source : le TABLEAU DE LA PAGE, établi d'après les textes qu'elle cite. Ce que le script vérifie, et rien de plus :
  1. chaque fragment de VERIF figure mot pour mot dans la cellule « Délai » de son registre ;
  2. chaque valeur dessinée se lit dans ces fragments : « 6 mois » pour 0,5 ; le nombre lui-même pour une durée en ans ;
     pour un point creux (récidive), la moitié de la valeur et le mot « doublés ».
Si l'un manque, arrêt sans rien écrire (témoins : --mutation=texte, --mutation=marque).

Marques : un POINT par durée distincte (jamais un trait, qui ferait lire une plage) ; plein pour le délai, creux pour le
délai doublé en récidive. Une seule couleur : le délai prend fin seul partout ; seul l'effacement anticipé passe par la
personne ou par un tiers, ce que la note dit.

Usage : python scripts/generer_frise_durees.py [--check] [--mutation=texte|marque]
Sorties : static/img/durees-inscription{,-m}.svg + .png ; contrôles : pied_figure.controler_page, pied_figure.parite.
"""
from __future__ import annotations

import html
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure as PF  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "content" / "combien-de-temps-une-erreur-reste-inscrite" / "_index.md"
OUT = ROOT / "static" / "img"
NOM = "durees-inscription"
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
ENCRE, GRIS, GRILLE, BLEU, FILET = "#1a1a1f", "#55524f", "#e6e3dc", "#184f95", "#c9c6bd"
DETAIL = "#45423e"   # détails des lignes : teinte propre, que le contrôle de parité lit (le pied reste en GRIS)
URL = "stephane-lalut.com/combien-de-temps-une-erreur-reste-inscrite/"
NB = " "

# (registre de la cellule « Registre », libellé, détail affiché, fragments exacts de la cellule « Délai », marques)
# marques : ("p", années) point plein, délai ; ("c", années) point creux, délai doublé en récidive
LIGNES = [
    ("Permis à points", "Permis : un point", "6 mois pour un point seul", ["6 mois pour un point seul"], [("p", 0.5)]),
    ("Permis à points", "Permis : tous les points",
     "2 ans sans infraction ; 3 ans après un délit ou une contravention de 4e ou 5e classe",
     ["2 ans sans infraction", "3 ans après un délit ou une contravention de 4e ou 5e classe"], [("p", 2), ("p", 3)]),
    ("Assurance auto, malus", "Malus d'assurance auto", "coefficient ramené à 1 au plus après 2 années sans sinistre",
     ["après 2 années sans sinistre"], [("p", 2)]),
    ("Fichier des incidents de crédit (FICP)", "Incident de crédit (FICP)", "5 ans", ["5 ans"], [("p", 5)]),
    ("Interdiction d'émettre des chèques", "Interdiction d'émettre des chèques", "5 ans", ["5 ans"], [("p", 5)]),
    ("Assurance d'un prêt, cancer ou hépatite C", "Prêt : cancer ou hépatite C", "5 ans après la fin du protocole thérapeutique",
     ["5 ans"], [("p", 5)]),
    ("FICP, surendettement", "Surendettement (FICP)",
     "la durée du plan, 7 ans au plus ; 5 ans si le plan est exécuté sans incident",
     ["7 ans au plus", "5 ans si le plan est exécuté sans incident"], [("p", 5), ("p", 7)]),
    ("Casier, bulletin n° 2", "Casier, bulletin n° 2 (réhabilitation)",
     "3, 5 ou 10 ans selon la peine ; doublés en récidive (points creux)",
     ["3, 5 ou 10 ans selon la peine, doublés en récidive"], [("p", 3), ("p", 5), ("p", 10), ("c", 6), ("c", 10), ("c", 20)]),
    ("Casier, bulletin n° 1", "Casier, bulletin n° 1", "40 ans sans nouvelle condamnation criminelle ou correctionnelle",
     ["40 ans sans nouvelle condamnation criminelle ou correctionnelle"], [("p", 40)]),
]
TICKS = [(0.5, "6 mois"), (1, "1 an"), (2, "2 ans"), (5, "5 ans"), (10, "10 ans"), (20, "20 ans"), (40, "40 ans")]
TICKS_M = [(0.5, "6 mois"), (2, "2 ans"), (5, "5 ans"), (10, "10 ans"), (40, "40 ans")]
TITRE = "Combien de temps une trace reste inscrite : de six mois à quarante ans"
SOURCE = ("Source : tableau de la page, établi d'après les textes qu'elle cite (code monétaire et financier, code de la "
          "consommation, code pénal et code de procédure pénale, code de la route, code des assurances, code de la santé "
          "publique, convention AERAS).")
NOTE = ("Échelle logarithmique. Point plein : délai ; point creux : délai doublé en récidive. Les délais ne courent pas du "
        "même point de départ (voir le tableau). Certains s'abrègent avant terme, par une démarche de la personne "
        "(régularisation d'un chèque, requête en exclusion devant le tribunal) ou par la déclaration d'un tiers (paiement "
        "déclaré par l'établissement).")
LICENCE = "Figure Stéphane Lalut, CC BY 4.0" + NB + "· " + URL
LICENCE_M = "Figure Stéphane Lalut, CC BY 4.0" + NB + "· stephane-lalut.com"


def fail(msg: str) -> None:
    print("ECHEC : " + msg)
    print("Aucun fichier ecrit.")
    sys.exit(1)


def insec(s: str) -> str:
    """Nombre et unité insécables (règle du site, « quel que soit le support ») : pied_figure.coupe ne soude pas « mois »
    ni « années »."""
    return re.sub(r"(\d) (ans|an|mois|années|classe)\b", "\\1" + NB + "\\2", s)


def cellules_delai(md: str) -> dict:
    """Cellule « Délai » de chaque registre du tableau de la page (texte brut, insécables en espaces)."""
    out = {}
    for tr in re.findall(r"<tr>(.*?)</tr>", md, re.S):
        c = [html.unescape(re.sub(r"<[^>]+>", "", x)).replace(NB, " ") for x in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if len(c) >= 3:
            out[c[0]] = c[2]
    return out


def nombres(texte: str) -> set:
    # entiers seuls : un décimal (« 2,5 ») n'est pas lu comme 2 ni 5 ; « 3, 5 ou 10 » donne bien 3, 5 et 10
    return {int(x) for x in re.findall(r"(?<!\d,)(?<!\d)(\d+)(?!\d)(?!,\d)", texte)}


def verifier(md: str, lignes) -> None:
    cel = cellules_delai(md)
    if "--mutation=texte" in sys.argv[1:]:   # témoin : une cellule reformulée doit arrêter le script
        cel["Casier, bulletin n° 1"] = cel.get("Casier, bulletin n° 1", "").replace("40 ans", "30 ans")
    for reg, lab, _, verifs, marques in lignes:
        if reg not in cel:
            fail("registre absent du tableau de la page : %s" % reg)
        for v in verifs:
            if v not in cel[reg]:
                fail("« %s » introuvable dans la cellule Délai de « %s » : relire la page avant toute écriture" % (v, reg))
        frag = " ".join(verifs)
        nb = nombres(frag)
        for sorte, an in marques:
            if not (TICKS[0][0] <= an <= TICKS[-1][0]):
                fail("valeur hors de l'axe : %s (%s)" % (an, lab))
            if sorte == "p":
                ok = ("6 mois" in frag) if an == 0.5 else (an == int(an) and int(an) in nb)
            else:
                ok = "doublés" in frag and an % 2 == 0 and int(an // 2) in nb
            if not ok:
                fail("marque %s %s de « %s » : valeur absente des fragments du tableau (%s)" % (sorte, an, lab, frag))


def desc() -> str:
    parts = ["%s : %s" % (lab, det) for _, lab, det, _, _ in LIGNES]
    return ("Frise des durées d'inscription sur une échelle logarithmique de six mois à quarante ans. " + " ; ".join(parts) + ".")


def x_de(an: float, x0: float, x1: float) -> float:
    a, b = math.log(TICKS[0][0]), math.log(TICKS[-1][0])
    return x0 + (math.log(an) - a) / (b - a) * (x1 - x0)


DY_RECIDIVE = 14   # les points creux (récidive) sur une seconde ligne, juste dessous : 5 et 6 ans ne se touchent pas (rendu du 04/11)


def marques_svg(e: list, marques, y: float, x0: float, x1: float, r: float = 5.5) -> None:
    for sorte, an in marques:
        x = x_de(an, x0, x1)
        if sorte == "p":
            e.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x, y, r, BLEU))
        else:
            e.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffffff" stroke="%s" stroke-width="1.6"/>'
                     % (x, y + DY_RECIDIVE, r - 0.5, BLEU))


def figure() -> str:
    W, X0, X1 = 720, 300, 690
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, NOM, NOM, esc(FONT)),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (NOM, esc(TITRE), NOM, esc(desc())),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W,
         '<text x="0" y="22" font-size="17" font-weight="600" fill="%s">%s</text>' % (ENCRE, esc(TITRE))]
    y0, pas = 58, 54   # 54 : un détail sur deux lignes ne touche pas le libellé suivant (rendu du 04/11)
    yb = y0 + pas * len(LIGNES) - 14
    for an, lab in TICKS:
        x = x_de(an, X0, X1)
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (x, y0 - 14, x, yb, GRILLE))
        e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="middle">%s</text>' % (x, yb + 15, GRIS, esc(insec(lab))))
    for k, (_, lab, det, _, marques) in enumerate(LIGNES):
        y = y0 + pas * k
        e.append('<text x="0" y="%.1f" font-size="13" font-weight="600" fill="%s">%s</text>' % (y - 2, ENCRE, esc(lab)))
        for j, l in enumerate(PF.coupe(insec(det), 46)[:2]):
            e.append('<text x="0" y="%.1f" font-size="11" fill="%s">%s</text>' % (y + 12 + 13 * j, DETAIL, esc(l)))
        marques_svg(e, marques, y + 2, X0, X1)
    return PF.pied(e, yb + 26, W, [(SOURCE, GRIS, "pied-source"), (NOTE, GRIS, "pied-note"), (LICENCE, GRIS, "pied-licence")], FILET)


def graduations_m(e: list, y: float, X0: float, X1: float) -> None:
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    for an, lab in TICKS_M:
        x = x_de(an, X0 + 6, X1 - 6)
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (x, y - 6, x, y, GRIS))
        # extrêmes ancrés au bord (exception déclarée : centrés, « 6 mois » et « 40 ans » sortiraient du cadre de 300)
        ancre = "start" if an == TICKS_M[0][0] else ("end" if an == TICKS_M[-1][0] else "middle")
        xt = 0 if ancre == "start" else (PF.LARGEUR_M if ancre == "end" else x)
        e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%s</text>'
                 % (xt, y + 15, PF.POLICE_M, GRIS, ancre, esc(insec(lab))))


def figure_m() -> str:
    WM, X0, X1 = PF.LARGEUR_M, 4, PF.LARGEUR_M - 4
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    e, y = PF.tete_mobile(NOM + "-m", TITRE, desc(), ENCRE, FONT)
    for l in PF.coupe("Même échelle logarithmique sur chaque ligne :", 38):
        y += 18
        e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, PF.POLICE_M, GRIS, esc(l)))
    y += 16
    graduations_m(e, y, X0, X1)   # échelle en tête : au téléphone, celle du bas est trop loin des premières lignes
    y += 22
    for _, lab, det, _, marques in LIGNES:
        for l in PF.coupe(lab, 32):
            y += 18
            e.append('<text x="0" y="%.1f" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y, PF.POLICE_M, ENCRE, esc(l)))
        for l in PF.coupe(insec(det), 38):
            y += 17
            e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, PF.POLICE_M, DETAIL, esc(l)))
        y += 16
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, y, X1, y, GRILLE))
        for an, _ in TICKS_M:   # repères des graduations sur chaque ligne
            xt = x_de(an, X0 + 6, X1 - 6)
            e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (xt, y - 4, xt, y + 4, FILET))
        marques_svg(e, marques, y, X0 + 6, X1 - 6, r=5)
        y += 14 + (DY_RECIDIVE if any(m[0] == "c" for m in marques) else 0)
    y += 8
    graduations_m(e, y, X0, X1)
    return PF.pied_mobile(e, y + 30, [(SOURCE, GRIS, "pied-source"), (NOTE, GRIS, "pied-note"), (LICENCE_M, GRIS, "pied-licence")], FILET)


def main() -> None:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    md = PAGE.read_text(encoding="utf-8")
    lignes = LIGNES
    if "--mutation=marque" in sys.argv[1:]:   # témoin : une marque déplacée (5 → 6 ans) doit arrêter le script
        lignes = [(r, l, d, v, [("p", 6)] if l == "Incident de crédit (FICP)" else m) for r, l, d, v, m in LIGNES]
    verifier(md, lignes)
    figs = {NOM + ".svg": figure(), NOM + "-m.svg": figure_m()}
    ecarts = PF.parite(figs[NOM + ".svg"], figs[NOM + "-m.svg"], PF.POLICE_M, couleurs=(DETAIL,))
    if ecarts:
        fail("parite telephone : %s" % ecarts)
    ecarts = PF.controler_page(md, figs)
    for f, s in figs.items():
        print("  %s : viewBox %s" % (f, re.search(r'viewBox="([^"]+)"', s).group(1)))
    if ecarts:
        if check:
            print("A REPORTER DANS LA PAGE : %s" % "; ".join(ecarts))
        else:
            fail("page : %s" % "; ".join(ecarts))
    if check:
        print("--check : %d lignes verifiees contre le tableau de la page (fragments et valeurs), rien ecrit." % len(LIGNES))
        return
    import cairosvg
    change = [f for f, s in figs.items() if not (OUT / f).exists() or (OUT / f).read_text(encoding="utf-8") != s]
    pngs = {f: cairosvg.svg2png(bytestring=figs[f].encode("utf-8"), output_width=1440, background_color="white") for f in change}
    for f in change:
        (OUT / f).write_text(figs[f], encoding="utf-8", newline="\n")
        (OUT / f.replace(".svg", ".png")).write_bytes(pngs[f])
    print("Ecrit : %d SVG, %d PNG" % (len(change), len(pngs)))


if __name__ == "__main__":
    main()
