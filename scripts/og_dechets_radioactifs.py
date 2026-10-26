#!/usr/bin/env python3
"""Carte de partage et vignette d'index de la page « Déchets radioactifs : le volume dit-il le problème ? » (26/10/2026).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les parts sont LUES dans data/dechets_radioactifs.json
(scripts/update_dechets_radioactifs.py, Inventaire national de l'Andra) ; le contraste annoncé (HA : moins de 0,5 % du volume,
plus de 95 % de la radioactivité) est recontrôlé ici : s'il n'est plus vrai, la carte n'est pas dessinée.
Écrit : static/images/{og,vig}-dechets-radioactifs{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402


def barres(d, j: dict, lang: str = "fr") -> None:
    a = j["affichage_en" if lang == "en" else "affichage"]
    p = j["parts"]
    x0, x1 = 660, 1000
    X = lambda v: x0 + (x1 - x0) * v / 100  # noqa: E731
    fl, fv = og.font("inter", 18, 500), og.font("inter", 20, 600)
    pct = "%" if lang == "en" else " %"
    groupes = (("HA", "High-level waste" if lang == "en" else "Haute activité", "ha"),
               (None, "Short-lived (FMA-VC) and very-low-level (TFA)" if lang == "en" else "Vie courte (FMA-VC) et très faible activité (TFA)", "masse"))
    for i, (cat, lib, k) in enumerate(groupes):
        y = 120 + 170 * i
        d.text((x0, y), lib, font=fl, fill=og.INK)
        vol = p["volume"]["HA"] if cat else p["volume"]["FMA-VC"] + p["volume"]["TFA"]
        act = p["activite"]["HA"] if cat else p["activite"]["FMA-VC"] + p["activite"]["TFA"]
        tv = a["ha_vol"] if cat else a["masse_vol"]
        ta = a["ha_act"] if cat else a["masse_act"]
        for jdx, (v, t, col, nom) in enumerate(((vol, tv, og.SEC, "volume"), (act, ta, og.C2, "radioactivity" if lang == "en" else "radioactivité"))):
            yy = y + 34 + 46 * jdx
            d.rectangle([x0, yy, max(X(v), x0 + 3), yy + 30], fill=col)
            d.text((max(X(v), x0 + 3) + 10, yy + 2), "%s%s %s" % (t, pct, nom), font=fv, fill=og.C2 if col == og.C2 else og.INK)


def main() -> int:
    f = og.ROOT / "data" / "dechets_radioactifs.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_dechets_radioactifs.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    p = j["parts"]
    if not (p["volume"]["HA"] < 0.5 and p["activite"]["HA"] > 95):
        og.fail("carte : le contraste annonce n'est plus vrai (%s / %s)" % (p["volume"]["HA"], p["activite"]["HA"]))
    A, E = j["affichage"], j["affichage_en"]
    og.carte("og-dechets-radioactifs-en.jpg",
             ["Volume does not show", "where the radioactivity is"],
             "High-level waste: %s%% of the volume, %s%% of the radioactivity, no final disposal yet." % (E["ha_vol"], E["ha_act"]),
             "Andra, National Inventory (open data) · CC BY 4.0",
             "stephane-lalut.com/en/radioactive-waste-volume-or-radioactivity/",
             lambda d: barres(d, j, "en"),
             [(og.SEC, "Share of volume (end-%s)" % E["an_vol"]), (og.C2, "Share of radioactivity (end-%s)" % E["an_act"])])
    og.carte("og-dechets-radioactifs.jpg",
             ["Le volume ne dit pas", "où est la radioactivité"],
             "Haute activité : %s %% du volume, %s %% de la radioactivité, pas encore de stockage définitif." % (A["ha_vol"], A["ha_act"]),
             "Andra, Inventaire national (données ouvertes) · CC BY 4.0",
             "stephane-lalut.com/dechets-radioactifs-volume-ou-radioactivite/",
             lambda d: barres(d, j),
             [(og.SEC, "Part du volume (fin %s)" % A["an_vol"]), (og.C2, "Part de la radioactivité (fin %s)" % A["an_act"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
