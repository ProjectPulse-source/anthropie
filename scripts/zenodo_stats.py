import json, urllib.request, datetime
RECORDS = {
    "AWP-01": "19266862",
    "AWP-02": "19268037",
    "AWP-03": "19268769",
    "AWP-04": "19269244",
    "AWP-05": "19269487",
}
today = datetime.date.today()
print(f"# Stats Zenodo — snapshot {today.isoformat()}\n")
print("| AWP | Publié le | Jours | Vues uniq. | DL uniq. | Vues/jour | DL/jour |")
print("|-----|-----------|------:|-----------:|---------:|----------:|--------:|")
for awp, rid in RECORDS.items():
    req = urllib.request.Request(
        f"https://zenodo.org/api/records/{rid}",
        headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as r:
        d = json.load(r)
    s = d.get("stats", {})
    pub = d.get("metadata", {}).get("publication_date", "")
    try:
        pub_d = datetime.date.fromisoformat(pub)
        days = max((today - pub_d).days, 1)
    except Exception:
        days = None
    uv = s.get("unique_views", 0)
    ud = s.get("unique_downloads", 0)
    vpd = f"{uv/days:.2f}" if days else "—"
    dpd = f"{ud/days:.2f}" if days else "—"
    j = days if days else "—"
    print(f"| {awp} | {pub} | {j} | {uv} | {ud} | {vpd} | {dpd} |")
