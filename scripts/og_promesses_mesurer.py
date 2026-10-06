#!/usr/bin/env python3
"""Carte de partage et vignette d'index du volet « Mesurer » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Tous les chiffres sont LUS dans
data/promesses_mesurer.json, écrit par scripts/update_promesses_mesurer.py ; la barre dessinée est la figure 2 de
l'Insee restituée (trois ensembles). Écrit : static/images/og-mesurer-promesse.jpg et vig-mesurer-promesse.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

GRIS_CLAIR = (201, 205, 211)


def barre(d, c: dict) -> None:
    x0, x1, y, h = 660, 1126, 220, 70
    tot = c["bit_seul"] + c["commun"] + c["a_seul"]
    a = x0 + (x1 - x0) * c["bit_seul"] / tot
    b = x0 + (x1 - x0) * (c["bit_seul"] + c["commun"]) / tot
    d.rectangle([x0, y, a, y + h], fill=GRIS_CLAIR)
    d.rectangle([a, y, b, y + h], fill=og.C1)
    d.rectangle([b, y, x1, y + h], fill=GRIS_CLAIR)
    f = og.font("inter", 22, 600)
    for (u, v, n, col) in ((x0, a, c["bit_seul"], og.INK), (a, b, c["commun"], (255, 255, 255)), (b, x1, c["a_seul"], og.INK)):
        s = "{:,}".format(n).replace(",", " ")
        w = d.textlength(s, font=f)
        d.text(((u + v) / 2 - w / 2, y + 22), s, font=f, fill=col)
    fl = og.font("inter", 17, 400)
    d.line([(x0, y - 14), (b, y - 14)], fill=og.GREY, width=2)
    d.text((x0, y - 44), "Chômeurs au sens du BIT", font=fl, fill=og.GREY)
    d.line([(a, y + h + 14), (x1, y + h + 14)], fill=og.GREY, width=2)
    d.text((a, y + h + 22), "Inscrits en catégorie A", font=fl, fill=og.GREY)
    d.text((x0, y + h + 70), "En milliers, moyenne 2024, 15-64 ans", font=fl, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_mesurer.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_mesurer.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    c = j["calcul"]
    if not (c["commun"] > 2 and c["bit_seul"] > 2 and c["a_seul"] > 2):
        og.fail("carte : « se recoupent en partie » n'est plus vrai dans les données")
    og.carte("og-mesurer-promesse.jpg",
             ["Deux mesures,", "deux populations"],
             "Chômage BIT et catégorie A : un recoupement partiel.",
             "Estimation Insee 2024 · Dares · CC BY 4.0",
             "stephane-lalut.com/comment-savoir-si-une-promesse-est-tenue/",
             lambda d: barre(d, c),
             [(og.C1, "Dans les deux à la fois"),
              (GRIS_CLAIR, "Dans une seule des deux mesures")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
