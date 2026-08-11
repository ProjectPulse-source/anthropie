import json, os, re, sys, urllib.request
from pathlib import Path

# Console Windows = cp1252 : n'encode ni « ↔ » ni « ✓ » ni « ✗ ». Sans cette
# reconfiguration le script sort 1 en imprimant son propre rapport, ce qui est
# indiscernable d'un vrai echec. Voir scripts/check-console-encoding.py.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

EN_RECORDS = {
    "19431208": "awp-01",
    "19433086": "awp-02",
    "19434094": "awp-03",
    "19439921": "awp-04",
    "19440866": "awp-05",
}
DATE_FIELDS = ["date", "publishDate", "publish_date",
               "publication_date", "pub_date", "date_en"]

def find_en_md(slug):
    candidates = [
        Path(f"content/en/awp/{slug}.md"),
        Path(f"content/awp/en/{slug}.md"),
        Path(f"content/awp/{slug}.en.md"),
        Path(f"content/en/awp/{slug}/index.md"),
    ]
    for c in candidates:
        if c.exists():
            return c
    for p in Path("content").rglob(f"{slug}*.md"):
        parts = [x.lower() for x in p.parts]
        if "en" in parts or p.name.endswith(".en.md"):
            return p
    return None

def parse_front_matter_dates(md_path):
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = m.group(1)
    found = {}
    for line in fm.split("\n"):
        for field in DATE_FIELDS:
            m2 = re.match(rf"^\s*{field}\s*:\s*['\"]?([^'\"\n#]+?)['\"]?\s*(?:#|$)", line)
            if m2:
                val = m2.group(1).strip().split("T")[0]
                found[field] = val
                break
    return found

def get_zenodo_pub_date(rid):
    headers = {"Accept": "application/json"}
    token = os.environ.get("ZENODO_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(
        f"https://zenodo.org/api/records/{rid}", headers=headers)
    with urllib.request.urlopen(req) as r:
        return json.load(r).get("metadata", {}).get("publication_date", "")

print("# Cohérence Hugo (front matter EN) ↔ Zenodo (publication_date)\n")
print("| AWP | Fichier MD | Dates front matter | Zenodo pub_date | Statut |")
print("|-----|------------|--------------------|-----------------|--------|")
divergences = []
for rid, slug in EN_RECORDS.items():
    md = find_en_md(slug)
    z_date = get_zenodo_pub_date(rid)
    if not md:
        print(f"| {slug.upper()} | (introuvable) | — | {z_date} | ⚠ MD non trouvé |")
        continue
    fm_dates = parse_front_matter_dates(md)
    fm_str = ", ".join(f"{k}={v}" for k, v in fm_dates.items()) or "(aucune)"
    if not fm_dates:
        status = "⚠ aucune date"
    elif z_date in fm_dates.values():
        status = "✓ aligné"
    else:
        status = "✗ divergence"
        divergences.append((slug, fm_dates, z_date))
    print(f"| {slug.upper()} | {md} | {fm_str} | {z_date} | {status} |")

if divergences:
    print("\n## Divergences à examiner\n")
    for slug, fm, z in divergences:
        print(f"- **{slug.upper()}** : front matter = {fm}, Zenodo = {z}")
else:
    print("\n_Aucune divergence détectée._")
