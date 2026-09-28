#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figure du test de sensibilite de la FICHE 02 (piece de contre-expertise).

    python scripts/figure_fiche_02_sensibilite.py [dossier_de_sortie]

Le solde de la redistribution avec et sans les services publics imputes. La
figure n'est PAS publiee sur le site : elle appartient a la fiche 02 du dossier
de contre-expertise, ou elle soutient le paragraphe sur la dependance du
resultat a la convention d'imputation.

POURQUOI CE SCRIPT EXISTE. La version precedente de cette figure etait produite
hors chaine, en Matplotlib par defaut : palette hors charte, legende a pastilles
la ou la charte veut l'etiquetage direct, et surtout CONVENTION DE SIGNE
INVERSEE par rapport a la source, au jeu publie et a la figure du site. Une
piece qui part se faire contredire ne peut pas contredire sa propre source sur
le signe.

ZERO DUPLICATION DE LA CHARTE. Couleurs, echelle typographique, helpers et
cartouche sont IMPORTES du generateur du site. Une charte recopiee derive ; une
charte importee suit.

TITRE. « Test de sensibilite » et non « test de robustesse » : la figure montre
qu'un resultat DEPEND d'une convention, ce qui est une sensibilite. Nommer cela
robustesse disait le contraire de ce qu'on mesure.

CONDITION DE MORT. Si cette figure entre un jour dans le corps de la page, elle
passe dans generer_figures_qui_paie.py avec les autres et ce script disparait :
il n'existe que parce que la figure vit hors du site.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
SORTIE_DEFAUT = Path(r"D:\CONTRE_EXPERTISE\2026-09-28_FICHES_RESSOURCES\F02_QUI_PAIE\figures")

spec = importlib.util.spec_from_file_location("gfqp", REPO / "scripts" / "generer_figures_qui_paie.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)


def main() -> int:
    sortie = Path(sys.argv[1]) if len(sys.argv) > 1 else SORTIE_DEFAUT
    if not sortie.is_dir():
        print("ECHEC : dossier de sortie absent : %s" % sortie)
        return 1
    try:
        import cairosvg
    except ImportError:
        G.fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout")

    d = json.loads((REPO / "data" / "qui_paie_donnees.json").read_text(encoding="utf-8"))
    r = d["redistribution"]
    prel, esp, nat = r["prelevements"][:10], r["prestations_especes"][:10], r["transferts_non_monetaires"][:10]
    publie = r["transferts_nets"][:10]

    # Convention INSEE, celle du jeu publie et de la figure du site :
    # POSITIF = le groupe verse plus qu'il ne recoit.
    tous = [-(esp[i] + nat[i] + prel[i]) for i in range(10)]
    especes = [-(esp[i] + prel[i]) for i in range(10)]

    # Temoin : la serie recomposee doit redonner le solde publie, aux arrondis de
    # l'Insee pres. Sans ce controle, une inversion de signe passerait inapercue --
    # c'est exactement le defaut que cette figure corrige.
    ecart = max(abs(tous[i] - publie[i]) for i in range(10))
    if ecart > 200:
        G.fail("le solde recompose s'ecarte de %d € par UC du solde publie : la convention "
               "de signe ou le perimetre ne correspondent pas" % ecart)
    if not (tous[0] < 0 and tous[9] > 0):
        G.fail("convention de signe : D1 devrait etre negatif (recoit net) et D10 positif")

    W, NBSP = G.W, G.NBSP
    C1, SEC, INK, INK2, MUTED, GRID, AXIS = G.C1, G.SEC, G.INK, G.INK2, G.MUTED, G.GRID, G.AXIS
    tous_k = [v / 1000 for v in tous]
    esp_k = [v / 1000 for v in especes]

    ml, mr = 52, 176
    pas = (W - ml - mr) / 10
    bw = 15
    vmax, vmin = 75, -30
    top, bas = 96, 356
    k = (bas - top) / (vmax - vmin)

    def Y(v):
        return top + (vmax - v) * k

    def X(i):
        return ml + pas * (i + 0.5)

    c = [G.txt(0, 22, "Test de sensibilité : ce que devient le solde quand on retire les services "
               "publics imputés", G.TY_TITRE, INK2),
         G.txt(0, 48, "Solde de la redistribution publique par dixième de niveau de vie, 2023, en "
               "milliers d'euros par UC", G.TY_ANNOT, INK, weight="600"),
         G.txt(0, 64, "Convention Insee, celle de la source et des autres figures du dossier",
               G.TY_AXE, MUTED),
         G.txt(0, 80, "au-dessus de zéro : verse plus qu'il ne reçoit", G.TY_AXE - 1, INK2),
         G.txt(W - mr, 80, "en dessous : reçoit plus qu'il ne verse", G.TY_AXE - 1, INK2, "end")]
    for g in (-25, 0, 25, 50, 75):
        yy = Y(g)
        c.append('<line x1="%d" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, yy, W - mr, yy, AXIS if g == 0 else GRID))
        c.append(G.txt(ml - 6, yy + 4, G.fr(g) if g >= 0 else "−" + G.fr(-g), G.TY_AXE, MUTED, "end"))
    y0 = Y(0)
    for i in range(10):
        fort = i == 9
        for dec, serie, col in ((-bw - 1, tous_k, C1), (1, esp_k, SEC)):
            v = serie[i]
            haut = abs(v) * k
            yy = y0 - haut if v > 0 else y0
            c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                     % (X(i) + dec, yy, bw, max(haut, 2.0), col))
            # Chaque valeur est posee au bout de SA barre, jamais au-dessus du couple :
            # une etiquette placee sur la plus haute des deux designerait l'autre serie.
            # La serie grise n'est chiffree qu'au dernier dixieme, ou elle ancre la lecture.
            if serie is tous_k or fort:
                tv = G.TY_ANNOT if fort else G.TY_AXE - 1
                cv = INK if fort else (col if col == SEC else INK2)
                # Barres appariees de 15 px : une etiquette centree deborde sur la barre
                # voisine et devient illisible. Au-dessus de zero, chacune fuit l'autre —
                # la bleue vers la gauche, la grise vers la droite ; sous zero, la grise
                # est minuscule et le centrage reste lisible.
                if v > 0:
                    anc = "end" if col == C1 else "start"
                    x = X(i) + dec + (bw if col == C1 else 0)
                else:
                    anc, x = "middle", X(i) + dec + bw / 2
                c.append(G.txt(x, (Y(v) - 6) if v > 0 else (Y(v) + 13),
                               ("+" if v > 0 else "−") + G.fr(abs(v), 1),
                               tv, cv, anc, weight="600" if fort else None))
        c.append(G.txt(X(i), bas + 16, "D%d" % (i + 1), G.TY_AXE,
                       INK if fort else MUTED, "middle", weight="600" if fort else None))
    c += G.etiquettes_directes(W - mr + 14, [
        (Y(tous_k[9] / 2) + 4, C1, "Tous transferts", "services publics imputés compris"),
        (Y(esp_k[9] / 2) + 4, SEC, "Espèces seulement", "sans services imputés"),
    ], top + 8, bas - 12)
    c.append(G.txt(ml, bas + 32, "← 10" + NBSP + "% les plus modestes", G.TY_AXE - 1, MUTED))
    c.append(G.txt(W - mr, bas + 32, "10" + NBSP + "% les plus aisés →", G.TY_AXE - 1, MUTED, "end"))

    # Le resultat que la figure sert : la bascule se deplace.
    bascule_tous = next(i for i, v in enumerate(tous) if v > 0) + 1
    bascule_esp = next(i for i, v in enumerate(especes) if v > 0) + 1
    y = bas + 52
    c.append(G.txt(0, y, "Sans les services publics imputés, la bascule entre bénéficiaires et "
                   "contributeurs nets passe du dixième D%d au dixième D%d."
                   % (bascule_tous, bascule_esp), G.TY_ANNOT, INK, weight="600"))
    y += 22
    lignes = [
        ("Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, figure 1c) · calcul de "
         "l'auteur : espèces − prélèvements, puis espèces + non monétaires − prélèvements", INK2),
        ("Les services publics sont valorisés par imputation de consommations moyennes, non par "
         "l'usage de chacun : ce test mesure la dépendance du solde à cette convention.", INK2),
        ("Solde d'une année, non d'une vie ; ne mesure pas l'effet propre de la dette.", INK2),
        ("Compilation Stéphane Lalut, CC BY 4.0 · " + G.URL_PAGE, MUTED)]
    h = int(y + 13 + 12 * len(lignes) + 8)
    desc = ("Barres appariées par dixième de niveau de vie, 2023, en milliers d'euros par unité de "
            "consommation, convention Insee (positif : verse plus qu'il ne reçoit). La première "
            "série comprend les services publics imputés, la seconde ne retient que les espèces. "
            "Sans les services imputés, la bascule entre bénéficiaires et contributeurs nets passe "
            "du dixième D%d au dixième D%d." % (bascule_tous, bascule_esp))
    e = G.entete(h, "qp-sens", "Test de sensibilité : le solde selon que l'on compte ou non les "
                 "services publics imputés", desc) + c
    e += G.cartouche(y, lignes)
    e.append("</svg>")
    svg = "\n".join(e) + "\n"

    p = sortie / "test-sensibilite-services-imputes.svg"
    p.write_text(svg, encoding="utf-8")
    cairosvg.svg2png(url=str(p), write_to=str(p.with_suffix(".png")), output_width=1440,
                     background_color="white")
    print("OK  %s (720 x %d) + PNG 1440 px" % (p.name, h))
    print("    bascule D%d -> D%d  ·  temoin solde recompose : ecart maximal %d € par UC"
          % (bascule_tous, bascule_esp, ecart))
    return 0


if __name__ == "__main__":
    sys.exit(main())
