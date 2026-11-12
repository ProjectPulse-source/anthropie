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
    x0, x1 = 695, 1035   # décalé de 35 px (12/11/2026) : la valeur négative sortait dans la gouttière de l'accroche
    vmin, vmax = -60.0, 75.0
    X = lambda v: x0 + (x1 - x0) * (v - vmin) / (vmax - vmin)  # noqa: E731
    fl, fv = og.font("inter", 18, 500), og.font("inter", 20, 600)
    pct = "%" if lang == "en" else " %"
    # la barre grise dit la baisse propre de l'intensité : sans elle, « −42,6 % » se lisait comme cette baisse (12/11/2026)
    # chaque rangée avec la variation propre de son facteur (troisième passage, 12/11/2026), comme la figure
    libs = {"fr": ("Effet de la population (elle-même %s %%)" % a["w_var_pop"],
                   "Effet du PIB par habitant (lui-même %s %%)" % a["w_var_rev"],
                   "Effet de l'intensité (elle-même %s %%)" % a["w_var_int"],
                   "Variation de la consommation"),
            "en": ("Population effect (population: %s%%)" % a["w_var_pop"],
                   "GDP-per-head effect (GDP per head: %s%%)" % a["w_var_rev"],
                   "Intensity effect (intensity: %s%%)" % a["w_var_int"],
                   "Change in consumption")}[lang]
    for i, k in enumerate(("pop", "rev", "int", "tot")):
        y = 110 + 78 * i
        v = w[k + "_pct"]
        col = og.C2 if k in ("pop", "rev") else (og.SEC if k == "int" else og.C1)   # total au bleu de la charte, comme la figure
        if x0 + d.textlength(libs[i], font=fl) > og.W - 70:
            og.fail("carte : libelle trop long pour la carte : %r" % libs[i])
        d.text((x0, y), libs[i], font=fl, fill=og.INK)
        xa, xb = sorted((X(0), X(v)))
        d.rectangle([xa, y + 28, max(xb, xa + 3), y + 56], fill=col)
        t = a["w_%s_pct" % k] + pct
        if v >= 0:
            d.text((xb + 10, y + 28), t, font=fv, fill=og.INK)
        else:
            d.text((xa - 10 - d.textlength(t, font=fv), y + 28), t, font=fv, fill=og.INK)
    # axe tracé par tronçons, à la hauteur des barres : un trait continu traversait les libellés (12/11/2026)
    for i in range(4):
        # 3 unités au-dessus et au-dessous de la barre (quatrième passage, 12/11/2026 : à 6, la parenthèse d'un libellé
        # allongé touchait le trait sur la carte anglaise)
        d.line([X(0), 110 + 78 * i + 25, X(0), 110 + 78 * i + 59], fill=og.INK, width=2)


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
             "World energy use, %s-%s: up %s%%. Accounting decomposition, as %% of %s consumption."
             % (E["an0"], E["an1"], E["de_pct"], E["an0"]),
             "EIA, international data; GDP at purchasing power parity · CC BY 4.0",
             "stephane-lalut.com/en/decoupling-energy-growth/",
             lambda d: barres(d, j, "en"),
             [(og.C2, "Upward effects"), (og.SEC, "Energy-intensity effect")])
    og.carte("og-decouplage.jpg",
             ["L'intensité baisse,", "la consommation mondiale monte"],
             "Monde, %s-%s : consommation d'énergie +%s %%. Décomposition comptable, en %% de celle de %s."
             % (A["an0"], A["an1"], A["de_pct"], A["an0"]),
             "EIA, données internationales ; PIB en parité de pouvoir d'achat · CC BY 4.0",
             "stephane-lalut.com/decouplage-energie-croissance/",
             lambda d: barres(d, j),
             [(og.C2, "Effets à la hausse"), (og.SEC, "Effet de l'intensité énergétique")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
