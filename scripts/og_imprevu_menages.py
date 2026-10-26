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
    pct = "%" if lang == "en" else " %"
    for i, (cle, lib_fr, lib_en, col) in enumerate((("A2", "Couple sans enfant", "Couple, no children", GRIS_CLAIR),
                                                     ("A2_DCH1", "Couple avec un enfant", "Couple, one child", og.SEC),
                                                     ("A1_DCH", "Parent seul", "Single parent", og.C2))):
        y = 160 + 92 * i
        v = s[cle][an]
        d.text((x0, y), lib_en if lang == "en" else lib_fr, font=fl, fill=og.INK)
        d.rectangle([x0, y + 30, X(v), y + 62], fill=col)
        k = {"A2": "c0_dessus", "A2_DCH1": "c1_dessus", "A1_DCH": "ps_dessus"}[cle]
        d.text((X(v) + 10, y + 32), a[k] + pct, font=fv, fill=og.C2 if cle == "A1_DCH" else og.INK)


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
             ["Income is not", "the whole story"],
             "Above the poverty line, %s%% of single parents could not face an unexpected expense." % E["ps_dessus"],
             "Eurostat, EU-SILC (ilc_mdes04), France %s · CC BY 4.0" % an,
             "stephane-lalut.com/en/who-can-cope-with-an-unexpected-expense/",
             lambda d: barres(d, j, "en"),
             [(og.C2, "Single parent: %s%%" % E["ps_dessus"]), (og.SEC, "Couple, one child: %s%%" % E["c1_dessus"])])
    og.carte("og-imprevu-menages.jpg",
             ["Le revenu", "ne dit pas tout"],
             "Au-dessus du seuil de pauvreté, %s %% des parents seuls ne pourraient pas faire face à une dépense imprévue." % A["ps_dessus"],
             "Eurostat, EU-SILC (ilc_mdes04), France %s · CC BY 4.0" % an,
             "stephane-lalut.com/qui-peut-faire-face-a-une-depense-imprevue/",
             lambda d: barres(d, j),
             [(og.C2, "Parent seul : %s %%" % A["ps_dessus"]), (og.SEC, "Couple avec un enfant : %s %%" % A["c1_dessus"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
