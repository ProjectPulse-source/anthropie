#!/usr/bin/env python3
"""Audit read-only des 10 records Zenodo AWP. Pas de modification."""
import os, sys, json, urllib.request, urllib.error

TOKEN = os.environ.get('ZENODO_TOKEN')
if not TOKEN:
    sys.exit("ERREUR : variable ZENODO_TOKEN absente")

# Tableau des 10 records attendus (id Zenodo | label lisible)
RECORDS = [
    ("19266862", "AWP-01 FR"),
    ("19268037", "AWP-02 FR"),
    ("19268769", "AWP-03 FR"),
    ("19269244", "AWP-04 FR"),
    ("19269486", "AWP-05 FR (concept DOI)"),
    ("19431208", "AWP-01 EN"),
    ("19433086", "AWP-02 EN"),
    ("19434094", "AWP-03 EN"),
    ("19439921", "AWP-04 EN"),
    ("19440866", "AWP-05 EN"),
]

def fetch(record_id):
    url = f"https://zenodo.org/api/records/{record_id}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}"}
    except Exception as e:
        return {"_error": str(e)}

print("# Audit Zenodo — 10 records AWP\n")
print("| Record ID | Label | Status | Concept | Version ID | Title |")
print("|---|---|---|---|---|---|")

all_data = []
for rid, label in RECORDS:
    d = fetch(rid)
    if "_error" in d:
        print(f"| {rid} | {label} | ERR {d['_error']} | — | — | — |")
        continue
    concept = d.get("conceptrecid", "?")
    version_id = d.get("id", "?")
    state = d.get("metadata", {}).get("resource_type", {}).get("type", "?")
    title = d.get("metadata", {}).get("title", "")[:50]
    status = "published" if not d.get("is_draft") else "DRAFT"
    divergent = " ⚠" if str(concept) != str(version_id) else ""
    print(f"| {rid} | {label} | {status} | {concept}{divergent} | {version_id} | {title} |")
    all_data.append((rid, label, d))

print("\n## Inventaire des Related Identifiers actuels par record\n")
for rid, label, d in all_data:
    rels = d.get("metadata", {}).get("related_identifiers", [])
    print(f"### {label} (record {rid})")
    if not rels:
        print("  (aucun related_identifier)")
    else:
        for r in rels:
            ident = r.get("identifier", "?")
            scheme = r.get("scheme", "?")
            rel = r.get("relation", "?")
            print(f"  - [{rel}] {scheme}: {ident}")
    print()

print("\n## Sommaire")
total_rels = sum(len(d.get("metadata", {}).get("related_identifiers", [])) for _,_,d in all_data)
print(f"- Records interroges avec succes : {len(all_data)}/10")
print(f"- Total related_identifiers existants : {total_rels}")
