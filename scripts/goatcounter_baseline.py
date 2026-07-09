#!/usr/bin/env python3
"""
goatcounter_baseline.py — baseline des clics sortants Amazon (READ-ONLY).

Fige, avant le lancement d'AI Overviews France (~23/09/2026) puis à chaque
lecture, l'état des événements `ext-amazon-<format>-<page>` (émis par
static/js/amazon-outbound.js) et des pageviews des pages d'origine — seul
proxy de vente disponible avant Amazon Attribution (sept. 2026).

Usage :
  set GOATCOUNTER_API_TOKEN=<token>       (PowerShell : $env:GOATCOUNTER_API_TOKEN="...")
  python scripts/goatcounter_baseline.py [--days 60] [--label T0]

Token : https://lalut.goatcounter.com → Settings → API → New token
        (permission « Read statistics » suffit — ne JAMAIS committer le token).

Sortie : reports/geo_audit/baseline_amazon_outbound/<date>_<label>.md + .json
(reports/ est gitignoré : les instantanés restent locaux, comme les audits).

Ne modifie rien côté GoatCounter (GET uniquement).
"""

import argparse
import datetime as dt
import json
import os
import ssl
import sys
import urllib.request
import urllib.parse

# Le magasin de certificats du Python Windows local rejette la chaîne
# Let's Encrypt de goatcounter.com (« certificate has expired ») ; certifi
# la valide. Fallback sur le contexte par défaut si certifi absent.
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:  # pragma: no cover
    SSL_CTX = ssl.create_default_context()

SITE = "https://lalut.goatcounter.com"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports",
                       "geo_audit", "baseline_amazon_outbound")
# Pages d'origine dont on veut le dénominateur (pageviews) pour un ratio
# clics-Amazon / visites par fiche.
DENOMINATOR_PREFIXES = (
    "/livres/",
    "/offrir-un-livre-kindle/",
    "/offrir-un-livre-de-culture-generale/",
    "/ressources-offertes/",
)


def api_get(path, token, **params):
    url = SITE + "/api/v0/" + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_hits(token, start, end):
    """Récupère toutes les pages/événements de la période (pagination after)."""
    hits, after = [], None
    while True:
        params = {"start": start, "end": end, "limit": 100}
        if after is not None:
            params["after"] = after
        data = api_get("stats/hits", token, **params)
        batch = data.get("hits", [])
        hits.extend(batch)
        if not data.get("more"):
            break
        after = batch[-1].get("path_id") or batch[-1].get("id")
        if after is None:  # structure inattendue : on garde ce qu'on a
            break
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--label", default="baseline")
    args = ap.parse_args()

    token = os.environ.get("GOATCOUNTER_API_TOKEN")
    if not token:
        print("ERREUR : variable GOATCOUNTER_API_TOKEN absente.")
        print('PowerShell : $env:GOATCOUNTER_API_TOKEN="<token>"')
        return 1

    end = dt.date.today()
    start = end - dt.timedelta(days=args.days)
    hits = fetch_hits(token, start.isoformat(), end.isoformat())

    events, denominators = {}, {}
    for h in hits:
        path = h.get("path", "")
        count = h.get("count", 0)
        if path.startswith("ext-amazon-"):
            events[path] = count
        elif path.startswith(DENOMINATOR_PREFIXES):
            denominators[path] = count

    os.makedirs(OUT_DIR, exist_ok=True)
    stamp = end.isoformat()
    base = os.path.join(OUT_DIR, "%s_%s" % (stamp, args.label))

    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump({
            "site": SITE, "start": start.isoformat(), "end": end.isoformat(),
            "days": args.days, "label": args.label,
            "events_ext_amazon": events, "pageviews_origines": denominators,
            "raw_hits_count": len(hits),
        }, f, ensure_ascii=False, indent=2, sort_keys=True)

    lines = [
        "# Baseline clics Amazon sortants — %s (%s)" % (args.label, stamp),
        "",
        "Période : %s → %s (%d jours). Source : GoatCounter, événements" % (
            start.isoformat(), end.isoformat(), args.days),
        "`ext-amazon-<format>-<page>` (amazon-outbound.js). Proxy de vente",
        "avant Amazon Attribution. Fichier brut : même nom en `.json`.",
        "",
        "## Clics sortants Amazon (par format et page d'origine)",
        "",
        "| Événement | Clics |",
        "|---|---|",
    ]
    for path in sorted(events, key=events.get, reverse=True):
        lines.append("| `%s` | %d |" % (path, events[path]))
    if not events:
        lines.append("| _(aucun événement sur la période)_ | 0 |")
    lines += [
        "",
        "## Pageviews des pages d'origine (dénominateur)",
        "",
        "| Page | Vues |",
        "|---|---|",
    ]
    for path in sorted(denominators, key=denominators.get, reverse=True):
        lines.append("| `%s` | %d |" % (path, denominators[path]))
    if not denominators:
        lines.append("| _(aucune vue relevée)_ | 0 |")
    lines += [
        "",
        "## Rappels de lecture",
        "",
        "- Comparer T0 (avant le 23/09) puis T+30j après le lancement",
        "  d'AI Overviews France, jamais en lecture hebdomadaire",
        "  (GEO_PROTOCOLE_MESURE : seuil >=50 evenements/cellule).",
        "- Le ratio clics/vues par fiche est le signal ; les volumes bruts",
        "  faibles ne se comparent pas cellule par cellule.",
    ]
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("OK : %d evenements ext-amazon, %d pages denominateur" % (
        len(events), len(denominators)))
    print("Ecrit : %s.md / .json" % base)
    return 0


if __name__ == "__main__":
    sys.exit(main())
