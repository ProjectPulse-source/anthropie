#!/usr/bin/env python3
"""Carte de partage et vignette d'index de la page « L'économie mondiale se découple-t-elle de l'énergie ? » (26/10/2026).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les valeurs sont LUES dans data/decouplage.json
(scripts/update_decouplage.py, EIA) ; le contraste annoncé (intensité mondiale en baisse, consommation mondiale en hausse)
est recontrôlé ici : s'il n'est plus vrai, la carte n'est pas dessinée.
Écrit : static/images/{og,vig}-decouplage{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402


def barres(d, j: dict, lang: str = "fr") -> None:
    a = j["affichage_en" if lang == "en" else "affichage"]
    w = j["decomposition"]["monde"]
    x0, x1 = 660, 1000
    vmin, vmax = -60.0, 75.0
    X = lambda v: x0 + (x1 - x0) * (v - vmin) / (vmax - vmin)  # noqa: E731
    fl, fv = og.font("inter", 18, 500), og.font("inter", 20, 600)
    pct = "%" if lang == "en" else " %"
    libs = {"fr": ("Effet de la population", "Effet du PIB par habitant", "Effet de l'intensité énergétique", "Variation de la consommation"),
            "en": ("Population effect", "GDP-per-head effect", "Energy-intensity effect", "Change in consumption")}[lang]
    for i, k in enumerate(("pop", "rev", "int", "tot")):
        y = 110 + 78 * i
        v = w[k + "_pct"]
        col = og.C2 if k in ("pop", "rev") else (og.SEC if k == "int" else og.INK)
        d.text((x0, y), libs[i], font=fl, fill=og.INK)
        xa, xb = sorted((X(0), X(v)))
        d.rectangle([xa, y + 28, max(xb, xa + 3), y + 56], fill=col)
        t = a["w_%s_pct" % k] + pct
        if v >= 0:
            d.text((xb + 10, y + 28), t, font=fv, fill=og.INK)
        else:
            d.text((xa - 10 - d.textlength(t, font=fv), y + 28), t, font=fv, fill=og.INK)
    d.line([X(0), 130, X(0), 110 + 78 * 3 + 60], fill=og.INK, width=2)


def main() -> int:
    f = og.ROOT / "data" / "decouplage.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_decouplage.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    w = j["decomposition"]["monde"]
    if not (w["tot"] > 0 and w["dI_pct"] < 0):
        og.fail("carte : le contraste annonce n'est plus vrai (consommation %s, intensite %s)" % (w["tot"], w["dI_pct"]))
    A, E = j["affichage"], j["affichage_en"]
    og.carte("og-decouplage-en.jpg",
             ["Energy intensity falls,", "world consumption rises"],
             "World energy use, %s-%s: up %s%%. Effects as %% of %s consumption."
             % (E["an0"], E["an1"], E["de_pct"], E["an0"]),
             "EIA, international data · CC BY 4.0",
             "stephane-lalut.com/en/decoupling-energy-growth/",
             lambda d: barres(d, j, "en"),
             [(og.C2, "Pushed consumption up"), (og.SEC, "Held it back (intensity)")])
    og.carte("og-decouplage.jpg",
             ["L'intensité baisse,", "la consommation monte"],
             "Monde, %s-%s : consommation d'énergie +%s %%. Effets en %% de la consommation de %s."
             % (A["an0"], A["an1"], A["de_pct"], A["an0"]),
             "EIA, données internationales · CC BY 4.0",
             "stephane-lalut.com/decouplage-energie-croissance/",
             lambda d: barres(d, j),
             [(og.C2, "Ont poussé la consommation"), (og.SEC, "L'a freinée (intensité)")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
