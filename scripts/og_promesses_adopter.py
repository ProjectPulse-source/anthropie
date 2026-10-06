#!/usr/bin/env python3
"""Carte de partage et vignette d'index du volet « Adopter » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les nombres sont LUS dans
data/promesses_adopter.json (scripts/update_promesses_adopter.py). Période, champ et source figurent sur la carte.
Écrit : static/images/og-adopter-promesse.jpg et vig-adopter-promesse.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

BLEU = (24, 79, 149)
BLEU_CLAIR = (127, 163, 207)
GRIS_CLAIR = (201, 197, 192)
ROMAIN = {"14": "XIVe", "15": "XVe", "16": "XVIe"}


def barres(d, leg: dict) -> None:
    x0, x1, y = 780, 1126, 120
    vmax = 220
    X = lambda v: x0 + (x1 - x0) * v / vmax  # noqa: E731
    fa = og.font("inter", 16, 400)
    for l in ("14", "15", "16"):
        x = leg[l]
        d.text((x0 - 70, y + 10), ROMAIN[l], font=fa, fill=og.URL_GREY)
        a = 0
        for v, col in ((x["gouv"], GRIS_CLAIR), (x["AN"], BLEU), (x["SEN"], BLEU_CLAIR)):
            d.rectangle([X(a), y, X(a + v) - 1, y + 40], fill=col)
            a += v
        y += 64
    d.text((x0 - 70, y + 6), "lois ordinaires promulguées, par législature", font=fa, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_adopter.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_adopter.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    leg = j["calcul"]["legislatures"]
    if not 2 * leg["16"]["Pmin"] > leg["16"]["N"]:
        og.fail("carte : la XVIe n'est plus majoritairement d'origine parlementaire, le titre serait faux")
    og.carte("og-adopter-promesse.jpg",
             ["Qui est à l'origine", "des lois votées ?"],
             "XIVe, XVe et XVIe législatures (2012-2024).",
             "Assemblée nationale · Sénat (Dosleg) · Journal officiel · CC BY 4.0",
             "stephane-lalut.com/qui-peut-faire-adopter-une-loi/",
             lambda d: barres(d, leg),
             [(GRIS_CLAIR, "Projet du Gouvernement"), (BLEU, "Proposition, Assemblée"), (BLEU_CLAIR, "Proposition, Sénat")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
