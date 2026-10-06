#!/usr/bin/env python3
"""Carte de partage et vignette d'index du volet « Appliquer » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les nombres sont LUS dans
data/promesses_appliquer.json (scripts/update_promesses_appliquer.py), eux-mêmes tirés du baromètre de l'application
des lois. Année, champ, unité et source figurent sur la carte (arbitrage PRO-20261005-153428, angle 12).
Écrit : static/images/{og,vig}-appliquer-promesse{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

BLEU = (24, 79, 149)
ORANGE = (235, 104, 52)
GRIS_CLAIR = (201, 197, 192)


def barres(d, m: dict, lang: str = "fr") -> None:
    x0, x1, y = 780, 1126, 96
    vmax = 1000
    X = lambda v: x0 + (x1 - x0) * v / vmax  # noqa: E731
    fa = og.font("inter", 15, 400)
    for s, c in m.items():
        d.text((x0 - 96, y + 6), s, font=fa, fill=og.URL_GREY)
        a = 0
        for k, col in (("P", BLEU), ("A", ORANGE), ("S", GRIS_CLAIR)):
            v = c.get(k, 0)
            if v:
                d.rectangle([X(a), y, X(a + v) - 1, y + 28], fill=col)
            a += v
        y += 40
    d.text((x0 - 96, y + 6), "measures by session of the law; status at 5 October 2026" if lang == "en"
           else "mesures par session de la loi ; état au 05/10/2026", font=fa, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_appliquer.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_appliquer.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, m = j["affichage"], j["calcul"]["mesures"]
    if not int(A["A"].replace(" ", "")) > 0:
        og.fail("carte : plus aucune mesure en attente, le titre serait faux")
    E = j["affichage_en"]
    og.carte("og-appliquer-promesse-en.jpg",
             ["%s measures" % E["A"], "still pending"],
             "French laws passed from October 2017 to September 2025.",
             "Barometer of the application of laws (National Assembly, LexImpact, DILA) · CC BY 4.0",
             "stephane-lalut.com/en/does-a-law-apply-as-soon-as-it-is-passed/",
             lambda d: barres(d, m, "en"),
             [(BLEU, "Published: %s" % E["P"]), (ORANGE, "Pending: %s" % E["A"]), (GRIS_CLAIR, "Not applicable: %s" % E["S"])])
    og.carte("og-appliquer-promesse.jpg",
             ["%s mesures" % A["A"], "encore attendues"],
             "Lois votées d'octobre 2017 à septembre 2025.",
             "Baromètre de l'application des lois (AN, LexImpact, DILA) · CC BY 4.0",
             "stephane-lalut.com/une-loi-votee-s-applique-t-elle-tout-de-suite/",
             lambda d: barres(d, m),
             [(BLEU, "Acte publié : %s" % A["P"]), (ORANGE, "En attente : %s" % A["A"]),
              (GRIS_CLAIR, "Sans objet : %s" % A["S"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
