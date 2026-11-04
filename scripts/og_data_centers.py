#!/usr/bin/env python3
"""Carte de partage et vignette d'index de la page « Data centers : les gigawatts réservés annoncent-ils la consommation ? »
(27/10/2026).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les valeurs sont LUES dans data/data_centers.json
(scripts/update_data_centers.py, publications de RTE) ; le contraste annoncé (plus de la moitié des gigawatts réservés en
novembre 2025 visent 2030 ou après ; consommation mesurée sous 2 TWh) est recontrôlé ici : s'il n'est plus vrai, la carte
n'est pas dessinée. Deux grandeurs, deux échelles : aucune barre ne se compare à l'autre.
Écrit : static/images/{og,vig}-data-centers{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

CLAIR = (157, 183, 218)


def barres(d, j: dict, lang: str = "fr") -> None:
    a = j["affichage_en" if lang == "en" else "affichage"]
    st, v = j["repartition_novembre_2025_gw"], j["valeurs"]
    x0, x1 = 660, 1120
    fl, fv = og.font("inter", 18, 500), og.font("inter", 20, 600)
    en = lang == "en"
    # panneau du haut : gigawatts réservés en novembre 2025, découpés par calendrier
    X = lambda g: x0 + (x1 - x0 - 120) * g / 20  # noqa: E731
    d.text((x0, 104), "Reserved, November 2025" if en else "Réservé, novembre 2025", font=fl, fill=og.INK)
    avant = st["travaux"] + st["signe_2025_2029"]
    d.rectangle([x0, 136, X(avant), 172], fill=og.C1)
    d.rectangle([X(avant), 136, X(avant + st["signe_2030"]), 172], fill=CLAIR)
    d.text((X(avant + st["signe_2030"]) + 10, 140), "%s GW" % a["res_nov2025"], font=fv, fill=og.C1)
    d.text((x0, 182), ("from 2030: %s GW" if en else "à partir de 2030 : %s GW") % a["st_2030"], font=fl, fill=og.GREY)
    # panneau du bas : térawattheures consommés, mesurés sur le réseau de RTE
    Y = lambda t: x0 + (x1 - x0 - 160) * t / 35  # noqa: E731
    d.text((x0, 252), "Consumed, RTE's grid, 2025" if en else "Consommé, réseau de RTE, 2025", font=fl, fill=og.INK)
    d.rectangle([x0, 284, max(Y(v["rpt_2025"]), x0 + 6), 320], fill=og.C2)
    d.text((max(Y(v["rpt_2025"]), x0 + 6) + 10, 288), ("nearly %s TWh" if en else "près de %s TWh") % a["rpt_2025"], font=fv, fill=og.C2)
    d.text((x0, 334), ("RTE pathways 2030: %s to %s TWh" if en else "Trajectoires RTE 2030 : %s à %s TWh") % (a["l2030"], a["r2030"]),
           font=fl, fill=og.GREY)


def main() -> int:
    f = og.ROOT / "data" / "data_centers.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_data_centers.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    st, v = j["repartition_novembre_2025_gw"], j["valeurs"]
    actif = st["travaux"] + st["signe_2025_2029"] + st["signe_2030"] + st["suspendu"]
    if not (st["signe_2030"] / actif > 0.5 and v["rpt_2025"] < 2):
        og.fail("carte : le contraste annonce n'est plus vrai (%s / %s ; %s TWh)" % (st["signe_2030"], actif, v["rpt_2025"]))
    A, E = j["affichage"], j["affichage_en"]
    og.carte("og-data-centers-en.jpg",
             ["Reserved is", "not consumed"],
             "Data centres: %s GW reserved with RTE in November 2025, %s GW of it for 2030 or later." % (E["res_nov2025"], E["st_2030"]),
             "RTE, Bilan prévisionnel 2025-2035 and Bilan électrique 2025 · CC BY 4.0",
             "stephane-lalut.com/en/data-centres-reserved-capacity/",
             lambda d: barres(d, j, "en"),
             [(og.C1, "Reserved capacity (GW)"), (og.C2, "Electricity consumed (TWh)")])
    og.carte("og-data-centers.jpg",
             ["Réservé n'est pas", "consommé"],
             "Data centers : %s GW réservés auprès de RTE en novembre 2025, dont %s GW pour 2030 ou après." % (A["res_nov2025"], A["st_2030"]),
             "RTE, Bilan prévisionnel 2025-2035 et Bilan électrique 2025 · CC BY 4.0",
             "stephane-lalut.com/data-centers-puissance-reservee/",
             lambda d: barres(d, j),
             [(og.C1, "Puissance réservée (GW)"), (og.C2, "Électricité consommée (TWh)")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
