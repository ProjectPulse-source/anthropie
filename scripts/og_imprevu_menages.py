#!/usr/bin/env python3
"""Carte de partage et vignette d'index de la page « Qui peut faire face à une dépense imprévue ? » (26/10/2026).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les parts sont LUES dans data/menages_imprevu.json
(scripts/update_menages_imprevu.py, Eurostat ilc_mdes04) ; le contraste annoncé (parent seul plus de deux fois le couple
avec un enfant, au-dessus du seuil de pauvreté) est recontrôlé ici : s'il n'est plus vrai, la carte n'est pas dessinée.
Écrit : static/images/{og,vig}-imprevu-menages{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402
import pied_figure  # noqa: E402

GRIS_CLAIR = (201, 197, 192)


def barres(d, j: dict, lang: str = "fr") -> None:
    a = j["affichage_en" if lang == "en" else "affichage"]
    s = j["serie"]["FR"]["A_60"]
    an = str(j["meta"]["derniere_annee"])
    x0, x1 = 660, 1060
    X = lambda v: x0 + (x1 - x0) * v / 60  # noqa: E731  -- échelle 0-60 %, assez pour la plus forte valeur dessinée
    fl, fv = og.font("inter", 18, 500), og.font("inter", 22, 600)
    d.text((x0, 112), "Above the poverty threshold, France " + an if lang == "en" else "Au-dessus du seuil de pauvreté, France " + an,
           font=og.font("inter", 17, 400), fill=og.GREY)
    # unité statistique (Audit-20/21, 07/11/2026) : des personnes, classées par le type de foyer où elles vivent
    d.text((x0, 134), "% of people, by type of household" if lang == "en" else "En % des personnes, selon le type de foyer",
           font=og.font("inter", 17, 400), fill=og.GREY)
    pct = "%" if lang == "en" else " %"
    for i, (cle, lib_fr, lib_en, col) in enumerate((("A2", "Deux adultes sans enfant", "Two adults, no children", GRIS_CLAIR),
                                                     ("A2_DCH1", "Deux adultes, un enfant", "Two adults, one child", og.SEC),
                                                     ("A1_DCH", "Un adulte avec enfants", "One adult with children", og.C2))):
        y = 160 + 92 * i
        v = s[cle][an]
        if not 0 <= v <= 60:   # échelle de 0 à 60 % : la série a atteint 61,3 % en 2005 (contrôleur de géométrie, 12/11/2026)
            og.fail("carte : %s vaut %.1f %%, hors de l'échelle de 0 à 60 %%" % (cle, v))
        d.text((x0, y), lib_en if lang == "en" else lib_fr, font=fl, fill=og.INK)
        d.rectangle([x0, y + 30, X(v), y + 62], fill=col)
        k = {"A2": "c0_dessus", "A2_DCH1": "c1_dessus", "A1_DCH": "ps_dessus"}[cle]
        # texte de la série orange en orange foncé (charte du 11/11/2026 ; l'orange vif ne passait pas 4,5:1 sur le crème)
        d.text((X(v) + 10, y + 32), a[k] + pct, font=fv, fill=pied_figure.ORANGE_TEXTE if cle == "A1_DCH" else og.INK)


def main() -> int:
    f = og.ROOT / "data" / "menages_imprevu.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_menages_imprevu.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    an = str(j["meta"]["derniere_annee"])
    s = j["serie"]["FR"]["A_60"]
    if not s["A1_DCH"][an] > 2 * s["A2_DCH1"][an]:
        og.fail("carte : « plus de deux fois » n'est plus vrai dans les donnees (%s contre %s)" % (s["A1_DCH"][an], s["A2_DCH1"][an]))
    A, E = j["affichage"], j["affichage_en"]
    og.carte("og-imprevu-menages-en.jpg",
             ["Unexpected expense: being above", "the poverty threshold is not enough"],
             "Above the threshold: %s%% of people in one-adult households with children could not pay an unexpected bill."
             % E["ps_dessus"],
             "Eurostat, EU-SILC (ilc_mdes04), France %s; association, not cause, not at equal income · CC BY 4.0" % an,
             "stephane-lalut.com/en/who-can-cope-with-an-unexpected-expense/",
             lambda d: barres(d, j, "en"),
             [(og.C2, "One adult with children: %s%% of people" % E["ps_dessus"]),
              (og.SEC, "Two adults, one child: %s%% of people" % E["c1_dessus"])])
    og.carte("og-imprevu-menages.jpg",
             ["Dépense imprévue : être au-dessus", "du seuil de pauvreté ne suffit pas"],
             "Au-dessus du seuil : %s %% des personnes en foyer d’un adulte avec enfants ne pourraient pas payer un imprévu."
             % A["ps_dessus"],
             "Eurostat, EU-SILC (ilc_mdes04), France %s ; association, non cause, pas à revenu égal · CC BY 4.0" % an,
             "stephane-lalut.com/qui-peut-faire-face-a-une-depense-imprevue/",
             lambda d: barres(d, j),
             [(og.C2, "Un adulte avec enfants : %s %% des personnes" % A["ps_dessus"]),
              (og.SEC, "Deux adultes, un enfant : %s %% des personnes" % A["c1_dessus"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
