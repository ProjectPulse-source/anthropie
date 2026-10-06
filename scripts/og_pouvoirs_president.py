#!/usr/bin/env python3
"""Carte de partage et vignette d'index du volet « Décider » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte : carte crème + vignette sur fond blanc, dans le
même passage). Tout chiffre de la carte est LU dans data/pouvoirs_president_donnees.json, écrit par
scripts/update_pouvoirs_president.py ; la matrice dessinée est celle du jeu, case par case. Lancer le générateur
d'abord. Écrit : static/images/og-pouvoirs-president.jpg et static/images/vig-pouvoirs-president.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

ATTRIBUTS = ["condition", "autre_autorite", "partage", "limite"]
COLS = ["Condition", "Autre", "Partagé", "Cadre"]
COLS_EN = ["Condition", "Other", "Shared", "Limit"]


def matrice(d, inv: list[dict], lang: str = "fr") -> None:
    x0, top, colw, pas = 700, 128, 108, 33
    fh = og.font("inter", 16, 500)
    for k, lib in enumerate(COLS_EN if lang == "en" else COLS):
        cx = x0 + colw * k + colw / 2
        w = d.textlength(lib, font=fh)
        d.text((cx - w / 2, top - 34), lib, font=fh, fill=og.URL_GREY)
    for i, e in enumerate(inv):
        y = top + pas * i + pas / 2
        for k, a in enumerate(ATTRIBUTS):
            cx = x0 + colw * k + colw / 2
            if e.get(a):
                d.ellipse([cx - 10, y - 10, cx + 10, y + 10], fill=og.C1)
            else:
                d.ellipse([cx - 9, y - 9, cx + 9, y + 9], outline=og.GRID, width=3)
    fl = og.font("inter", 17, 400)
    bas = top + pas * len(inv) + 12
    l1, l2 = (("One row per act of article 19;", "filled: exact quotation of the article") if lang == "en"
              else ("Une ligne par acte de l'article 19 ;", "case pleine : citation exacte de l'article"))
    d.text((x0, bas), l1, font=fl, fill=og.URL_GREY)
    d.text((x0, bas + 22), l2, font=fl, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "pouvoirs_president_donnees.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_pouvoirs_president.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, inv, c = j["affichage"], j["inventaire"], j["comptes"]
    if len(inv) != c["n"] or len(c["sans_condition_ni_autre_autorite_ni_partage"]) * 2 >= c["n"]:
        og.fail("carte : « seulement » n'est plus vrai dans les données")
    E = j["affichage_en"]
    og.carte("og-pouvoirs-president-en.jpg",
             ["Deciding alone:", "what the text says"],
             "%s acts out of %s with no condition or third party in their text."
             % (E["n_seuls"].capitalize(), E["n_renvois"]),
             "French Constitution of 1958 (Légifrance, Conseil constitutionnel) · CC BY 4.0",
             "stephane-lalut.com/en/what-can-the-french-president-decide-alone/",
             lambda d: matrice(d, inv, "en"),
             [(og.C1, "Exact quotation in the article"),
              (og.GRID, "Nothing in that article")])
    og.carte("og-pouvoirs-president.jpg",
             ["Décider seul :", "ce que dit le texte"],
             "%s actes sur %s sans condition ni tiers dans leur texte."
             % (A["n_seuls"].capitalize(), A["n_renvois"]),
             "Constitution de 1958, lue sur Légifrance · CC BY 4.0",
             "stephane-lalut.com/pouvoirs-du-president-de-la-republique/",
             lambda d: matrice(d, inv),
             [(og.C1, "Citation exacte dans l'article"),
              (og.GRID, "Rien dans cet article")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
