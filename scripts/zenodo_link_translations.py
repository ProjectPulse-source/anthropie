#!/usr/bin/env python3
"""
Audite (et pose si manquant) la liaison reciproque des paires de traduction
des AWP sur Zenodo.

CONSTAT DU 2026-08-02 — a lire avant d'utiliser ce script :
  - Les 8 paires FR<->EN sont DEJA liees reciproquement :
        version EN : isDerivedFrom -> DOI FR
        version FR : isSourceOf    -> DOI EN
  - Zenodo REFUSE les relations DataCite 4.6 `isTranslationOf` /
    `hasTranslation` (HTTP 400 "Invalid value hastranslation", teste sur
    AWP-08 le 2026-08-02). Son vocabulaire de relations est ferme et plus
    ancien que le schema DataCite courant.
  => Le couple isDerivedFrom/isSourceOf EST la bonne pratique ici. Ne pas
     tenter de le "moderniser" tant que Zenodo n'a pas etendu sa liste.

Utilite reelle : verifier la completude des liaisons a chaque nouvelle
langue (ES a venir) et poser ce qui manque.

Usage :
    python scripts/zenodo_link_translations.py                    # audit
    python scripts/zenodo_link_translations.py --apply            # pose ce qui manque
    python scripts/zenodo_link_translations.py --apply --only=AWP-08
"""
import os, sys, json, time, urllib.request, urllib.error

TOKEN = os.environ.get('ZENODO_TOKEN')
if not TOKEN:
    sys.exit("ERREUR : variable ZENODO_TOKEN absente")

APPLY = "--apply" in sys.argv
ONLY = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--only=")), None)

# (label, record source/FR, record traduction) — DOI = 10.5281/zenodo.<record>
# Source : data/works.yaml. Ajouter ici les paires FR<->ES a leur creation.
PAIRS = [
    ("AWP-01", "19266862", "19431208"),
    ("AWP-02", "19268037", "19433086"),
    ("AWP-03", "19268769", "19434094"),
    ("AWP-04", "19269244", "19439921"),
    ("AWP-05", "19269487", "19440866"),
    ("AWP-06", "20025421", "20077993"),
    ("AWP-07", "21200286", "21200288"),
    ("AWP-08", "21506320", "21507249"),
]

# Vocabulaire accepte par Zenodo (verifie 2026-08-02)
REL_ON_TRANSLATION = "isDerivedFrom"   # pose sur la traduction, pointe la source
REL_ON_SOURCE = "isSourceOf"           # pose sur la source, pointe la traduction

DOI = lambda rec: f"10.5281/zenodo.{rec}"


def api(path, method="GET", data=None):
    req = urllib.request.Request(f"https://zenodo.org/api{path}", method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    body = None
    if data is not None:
        req.add_header("Content-Type", "application/json")
        body = json.dumps(data).encode("utf-8")
    with urllib.request.urlopen(req, data=body, timeout=30) as r:
        raw = r.read()
        return json.loads(raw) if raw else {}


def has_relation(rels, relation, identifier):
    return any(r.get("relation") == relation and r.get("identifier") == identifier
               for r in rels)


def ensure(record_id, relation, target_doi, label):
    try:
        dep = api(f"/deposit/depositions/{record_id}")
    except Exception as e:
        print(f"  [ERR] lecture {record_id} : {e}")
        return "error"
    metadata = dep.get("metadata", {})
    rels = metadata.get("related_identifiers", []) or []

    if has_relation(rels, relation, target_doi):
        print(f"  [OK]   {label} : {relation} -> {target_doi}")
        return "already"

    print(f"  [MANQUE] {label} : {relation} -> {target_doi}")
    if not APPLY:
        return "todo"

    try:
        api(f"/deposit/depositions/{record_id}/actions/edit", method="POST")
        new_meta = dict(metadata)
        new_meta["related_identifiers"] = list(rels) + [
            {"relation": relation, "identifier": target_doi, "scheme": "doi"}
        ]
        api(f"/deposit/depositions/{record_id}", method="PUT", data={"metadata": new_meta})
        api(f"/deposit/depositions/{record_id}/actions/publish", method="POST")
        print(f"  [POSE] republie")
        time.sleep(1)
        return "done"
    except urllib.error.HTTPError as e:
        print(f"  [ERR] HTTP {e.code} : {e.read().decode('utf-8', 'replace')[:200]}")
        try:
            api(f"/deposit/depositions/{record_id}/actions/discard", method="POST")
            print("  [ROLLBACK] brouillon annule")
        except Exception:
            pass
        return "error"


print("=" * 72)
print(f"Liaisons de traduction Zenodo — mode : {'APPLY' if APPLY else 'AUDIT'}")
print("=" * 72)

counts = {}
for label, src, trad in PAIRS:
    if ONLY and label != ONLY:
        continue
    print(f"\n--- {label} (source {src} <-> traduction {trad}) ---")
    for s in (ensure(trad, REL_ON_TRANSLATION, DOI(src), f"{label} traduction"),
              ensure(src, REL_ON_SOURCE, DOI(trad), f"{label} source")):
        counts[s] = counts.get(s, 0) + 1

print("\n" + "=" * 72)
for k, lib in (("already", "deja en place"), ("done", "posees"),
               ("todo", "manquantes (audit)"), ("error", "erreurs")):
    if k in counts:
        print(f"  {lib:22} : {counts[k]}")
