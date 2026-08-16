import json, os, urllib.request, urllib.parse
q = urllib.parse.quote('Lalut AND (anthropie OR anthropy OR AWP)')
url = f"https://zenodo.org/api/records?q={q}&size=50&sort=mostrecent&all_versions=true"
headers = {"Accept": "application/json"}
token = os.environ.get("ZENODO_TOKEN")
if token:
    headers["Authorization"] = f"Bearer {token}"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as r:
    d = json.load(r)
hits = d.get("hits", {}).get("hits", [])
print(f"# Inventaire Zenodo — {len(hits)} record(s) trouvé(s)\n")
print("| ID | Lang | Created | Pub.date déclarée | Titre |")
print("|----|------|---------|-------------------|-------|")
for h in hits:
    rid = h.get("id", "")
    md = h.get("metadata", {})
    title = md.get("title", "")[:70].replace("|", "/")
    pub = md.get("publication_date", "")
    created = h.get("created", "")[:10]
    lang = md.get("language", "—")
    print(f"| {rid} | {lang} | {created} | {pub} | {title} |")
