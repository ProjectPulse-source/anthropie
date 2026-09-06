#!/usr/bin/env python3
"""
goatcounter_zenodo_outbound.py — clics sortants vers Zenodo, par jour (READ-ONLY).

Exporte les événements `ext-zenodo-<pdf|record|doi>-<page>` (émis par
static/js/zenodo-outbound.js) pour la fenêtre de mesure du régime mixte du
collector (écart explicable entre compteurs Zenodo et parcours réels des
lecteurs, 06/09/2026). Réutilise l'accès API de goatcounter_baseline.py.

Usage :
  set GOATCOUNTER_API_TOKEN=<token>     (PowerShell : $env:GOATCOUNTER_API_TOKEN="...")
  python scripts/goatcounter_zenodo_outbound.py [--days 30]
Sortie : reports/geo_audit/zenodo_outbound/<date>.json
         {"start","end","days": {"AAAA-MM-JJ": {"ext-zenodo-pdf-/awp/awp-04/": n, ...}},
          "totals": {...}}
Consommé par : anthropie-collector/scripts/mesure_regime.py --clics <ce fichier>
Ne modifie rien côté GoatCounter (GET uniquement). Le jeton n'est jamais écrit.
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from goatcounter_baseline import fetch_hits  # noqa: E402

# Encodage console : le message d'absence de jeton ci-dessous contient
# « → », que cp1252 ne sait pas encoder. Sans cette reconfiguration le
# script meurt sur son propre message d'erreur sous PowerShell 5.1 --
# l'echec imiterait un jeton illisible au lieu d'un jeton absent.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports",
                       "geo_audit", "zenodo_outbound")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    args = ap.parse_args()
    token = os.environ.get("GOATCOUNTER_API_TOKEN")
    if not token:
        print("ERREUR : variable GOATCOUNTER_API_TOKEN absente "
              "(Settings → API → New token, lecture seule).")
        return 1
    end = dt.date.today()
    start = end - dt.timedelta(days=args.days)
    hits = fetch_hits(token, start.isoformat(), end.isoformat())
    days, totals = {}, {}
    for h in hits:
        path = h.get("path", "")
        if not path.startswith("ext-zenodo-"):
            continue
        totals[path] = int(h.get("count", 0))
        for st in h.get("stats", []) or []:
            day = st.get("day")
            n = int(st.get("daily", 0) or 0)
            if day and n:
                days.setdefault(day, {})[path] = days.get(day, {}).get(path, 0) + n
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, end.isoformat() + ".json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"start": start.isoformat(), "end": end.isoformat(),
                   "days": days, "totals": totals}, f,
                  ensure_ascii=False, indent=2, sort_keys=True)
    print("OK : %d evenement(s) ext-zenodo, %d jour(s) -> %s" % (len(totals), len(days), out))
    if totals and not days:
        print("NOTE : l'API n'a pas renvoye de detail journalier (champ stats) ; "
              "seuls les totaux sont exploitables.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
