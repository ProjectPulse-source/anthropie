#!/usr/bin/env python3
"""Carte de partage et vignette d'index du volet « Adopter » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les nombres sont LUS dans
data/promesses_adopter.json (scripts/update_promesses_adopter.py). Période, champ et source figurent sur la carte.
Titre « lois promulguées » (12/10/2026, refonte : « votées » contredisait l'adoption sans vote sur le texte, art. 49 al. 3).
XVIIe ajoutée et datée (passe B3, 12/10/2026 : la page la compte, la carte s'arrêtait à la XVIe).
Écrit : static/images/{og,vig}-adopter-promesse{,-en}.jpg.
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
ROMAIN = {"14": "XIVe", "15": "XVe", "16": "XVIe", "17": "XVIIe*"}
ROMAIN_EN = {"14": "14th", "15": "15th", "16": "16th", "17": "17th*"}


def barres(d, leg: dict, lang: str = "fr") -> None:
    x0, x1, y = 780, 1126, 110
    vmax = 220
    X = lambda v: x0 + (x1 - x0) * v / vmax  # noqa: E731
    fa = og.font("inter", 16, 400)
    for l in ("14", "15", "16", "17"):
        x = leg[l]
        d.text((x0 - 70, y + 10), (ROMAIN_EN if lang == "en" else ROMAIN)[l], font=fa, fill=og.URL_GREY)
        a = 0
        for v, col in ((x["gouv"], GRIS_CLAIR), (x["AN"], BLEU), (x["SEN"], BLEU_CLAIR)):
            d.rectangle([X(a), y, X(a + v) - 1, y + 34], fill=col)
            a += v
        y += 52
    d.text((x0 - 70, y + 6), "laws promulgated, by legislature" if lang == "en" else "lois ordinaires promulguées, par législature", font=fa, fill=og.URL_GREY)
    d.text((x0 - 70, y + 30), "* ongoing on 6 October 2026" if lang == "en" else "* en cours au 06/10/2026", font=fa, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_adopter.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_adopter.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    leg = j["calcul"]["legislatures"]
    if not 2 * leg["16"]["Pmin"] > leg["16"]["N"]:
        og.fail("carte : la XVIe n'est plus majoritairement d'origine parlementaire, le titre serait faux")
    og.carte("og-adopter-promesse-en.jpg",
             ["Who initiated the laws", "promulgated in France?"],
             "Ordinary laws, 14th to 17th legislatures (2012-2026).",
             "National Assembly · Senate (Dosleg) · Journal officiel · CC BY 4.0",
             "stephane-lalut.com/en/who-can-get-a-law-passed-in-france/",
             lambda d: barres(d, leg, "en"),
             [(GRIS_CLAIR, "Government bill"), (BLEU, "Private member's bill, Assembly"), (BLEU_CLAIR, "Private member's bill, Senate")])
    og.carte("og-adopter-promesse.jpg",
             ["Qui est à l'origine", "des lois promulguées ?"],
             "Lois ordinaires, XIVe à XVIIe législatures (2012-2026).",
             "Assemblée nationale · Sénat (Dosleg) · Journal officiel · CC BY 4.0",
             "stephane-lalut.com/qui-peut-faire-adopter-une-loi/",
             lambda d: barres(d, leg),
             [(GRIS_CLAIR, "Projet du Gouvernement"), (BLEU, "Proposition, Assemblée"), (BLEU_CLAIR, "Proposition, Sénat")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
