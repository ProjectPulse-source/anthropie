import json, os, urllib.request, urllib.parse, datetime

q = urllib.parse.quote('Lalut AND (anthropie OR anthropy OR AWP)')
url = f"https://zenodo.org/api/records?q={q}&size=50&sort=mostrecent&all_versions=true"
headers = {"Accept": "application/json"}
token = os.environ.get("ZENODO_TOKEN")
if token:
    headers["Authorization"] = f"Bearer {token}"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as r:
    data = json.load(r)

today = datetime.date.today()
hits = data.get("hits", {}).get("hits", [])

# Mapping titre → label AWP
def awp_label(title):
    t = title.lower()
    for n, kw in [("AWP-01", ["principes d'une hypothèse", "principles of a hypothesis"]),
                  ("AWP-02", ["3,3 millions", "3.3 million"]),
                  ("AWP-03", ["dette publique", "public debt"]),
                  ("AWP-04", ["transition", "energy transition"]),
                  ("AWP-05", ["hors les murs", "beyond the walls"])]:
        if any(k in t for k in kw):
            return n
    return "?"

rows = []
for h in hits:
    md = h.get("metadata", {})
    s = h.get("stats", {})
    created = h.get("created", "")[:10]
    try:
        days = max((today - datetime.date.fromisoformat(created)).days, 1)
    except Exception:
        days = None
    rows.append({
        "awp": awp_label(md.get("title", "")),
        "lang": md.get("language", "—"),
        "created": created,
        "days": days,
        "uv": s.get("unique_views", 0),
        "ud": s.get("unique_downloads", 0),
        "v": s.get("views", 0),
        "d": s.get("downloads", 0),
    })

# Tri : par AWP puis FR avant EN
rows.sort(key=lambda r: (r["awp"], 0 if r["lang"] == "fra" else 1))

print(f"# Stats Zenodo consolidées — snapshot {today.isoformat()}\n")
print(f"_Source : `created` Zenodo (date réelle de dépôt), pas `publication_date` déclarative._\n")
print("| AWP | Lang | Déposé | Jours | Vues uniq. | DL uniq. | V/jour | DL/jour |")
print("|-----|------|--------|------:|-----------:|---------:|-------:|--------:|")
for r in rows:
    j = r["days"] if r["days"] else "—"
    vpd = f"{r['uv']/r['days']:.2f}" if r["days"] else "—"
    dpd = f"{r['ud']/r['days']:.2f}" if r["days"] else "—"
    print(f"| {r['awp']} | {r['lang']} | {r['created']} | {j} | {r['uv']} | {r['ud']} | {vpd} | {dpd} |")

# Synthèses
print("\n## Synthèses\n")
fr = [r for r in rows if r["lang"] == "fra"]
en = [r for r in rows if r["lang"] == "eng"]
for label, group in [("FR", fr), ("EN", en)]:
    if not group:
        continue
    tot_uv = sum(r["uv"] for r in group)
    tot_ud = sum(r["ud"] for r in group)
    print(f"- **{label}** ({len(group)} records) : {tot_uv} vues uniq. cumulées, {tot_ud} DL uniq. cumulés.")
