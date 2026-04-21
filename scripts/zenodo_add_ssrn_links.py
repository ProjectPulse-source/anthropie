#!/usr/bin/env python3
"""
Ajout idempotent des relations isIdenticalTo vers SSRN sur les 4 AWP EN en attente.

Mapping : chaque AWP EN Zenodo -> son DOI SSRN previsible.
Le script n'ecrit que si le DOI SSRN resout deja publiquement (HTTP 200 ou 302).

Justification du relationType 'IsIdenticalTo' :
SSRN stocke les PDFs deposes sans ajouter de page de garde. Le fichier SSRN et
le fichier Zenodo sont la meme ressource bit-a-bit. Verifie manuellement sur
AWP-01 EN (21/04/2026).

Mode par defaut : dry-run. Pour appliquer : --apply

Relance-le autant de fois que voulu. A chaque execution, les DOIs resolus
sont traites, les autres skippes avec un warning.
"""
import os, sys, json, urllib.request, urllib.error

TOKEN = os.environ.get('ZENODO_TOKEN')
if not TOKEN:
    sys.exit("ERREUR : variable ZENODO_TOKEN absente")

APPLY = "--apply" in sys.argv
VERBOSE = "--verbose" in sys.argv

# Mapping : record Zenodo EN -> (label, DOI SSRN previsible)
# Les DOIs SSRN suivent le pattern strict 10.2139/ssrn.{abstract_id}
MAPPING = [
    ("19431208", "AWP-01 EN", "10.2139/ssrn.6543618"),  # deja DISTRIBUTED, skip si deja pose
    ("19433086", "AWP-02 EN", "10.2139/ssrn.6615059"),
    ("19434094", "AWP-03 EN", "10.2139/ssrn.6615278"),
    ("19439921", "AWP-04 EN", "10.2139/ssrn.6615305"),
    ("19440866", "AWP-05 EN", "10.2139/ssrn.6615438"),
]

def doi_resolves(doi):
    """Test de resolution DOI via doi.org. Retourne True si HTTP 200 ou 302."""
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, method="HEAD")
    # Ne pas suivre les redirections pour distinguer 302 (DOI resolu) d'une erreur
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None
    opener = urllib.request.build_opener(NoRedirect)
    try:
        opener.open(req, timeout=15)
        return True  # 200 explicite
    except urllib.error.HTTPError as e:
        return e.code in (301, 302, 303, 307, 308)  # redirection = DOI resolu
    except Exception:
        return False

def api_get(path):
    req = urllib.request.Request(f"https://zenodo.org/api{path}")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def api_post(path):
    req = urllib.request.Request(f"https://zenodo.org/api{path}", method="POST")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def api_put(path, data):
    req = urllib.request.Request(f"https://zenodo.org/api{path}", method="PUT")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    body = json.dumps(data).encode("utf-8")
    with urllib.request.urlopen(req, data=body, timeout=20) as r:
        return json.loads(r.read())

def already_has_ssrn_link(rels, ssrn_doi):
    for r in rels:
        if r.get("relation") == "isIdenticalTo" and r.get("identifier") == ssrn_doi:
            return True
    return False

print("=" * 70)
print(f"Script zenodo_add_ssrn_links — mode : {'APPLY' if APPLY else 'DRY-RUN'}")
print("=" * 70)
print()

summary = {"done": [], "skipped_no_doi": [], "skipped_already": [], "error": []}

for record_id, label, ssrn_doi in MAPPING:
    print(f"--- {label} (Zenodo {record_id} -> SSRN {ssrn_doi}) ---")

    # Etape 1 : test de resolution DOI SSRN
    if not doi_resolves(ssrn_doi):
        print(f"  [SKIP] DOI SSRN non resolvable (paper probablement encore PRELIMINARY_UPLOAD)")
        summary["skipped_no_doi"].append(label)
        print()
        continue
    print(f"  [OK] DOI SSRN resolvable")

    # Etape 2 : lecture du deposit Zenodo (format plat, endpoint deposit)
    try:
        dep = api_get(f"/deposit/depositions/{record_id}")
    except Exception as e:
        print(f"  [ERR] Lecture deposit impossible : {e}")
        summary["error"].append(label)
        print()
        continue

    metadata = dep.get("metadata", {})
    current_rels = metadata.get("related_identifiers", [])

    # Etape 3 : verification idempotence
    if already_has_ssrn_link(current_rels, ssrn_doi):
        print(f"  [SKIP] isIdenticalTo {ssrn_doi} deja present sur ce record")
        summary["skipped_already"].append(label)
        print()
        continue
    print(f"  [ADD] Relation a ajouter : isIdenticalTo -> {ssrn_doi}")
    print(f"        Related_identifiers actuels : {len(current_rels)} -> {len(current_rels) + 1}")

    if not APPLY:
        print(f"  [DRY-RUN] aucune modification effectuee")
        summary["done"].append(f"{label} (dry-run)")
        print()
        continue

    # Etape 4 (APPLY uniquement) : ouvrir edition, modifier, publier
    try:
        # Ouvrir edition
        api_post(f"/deposit/depositions/{record_id}/actions/edit")
        if VERBOSE:
            print(f"  [EDIT] brouillon ouvert")

        # Ajouter la relation a la liste existante
        new_rels = list(current_rels) + [{
            "relation": "isIdenticalTo",
            "identifier": ssrn_doi,
            "scheme": "doi"
        }]
        new_metadata = dict(metadata)
        new_metadata["related_identifiers"] = new_rels

        # PUT metadata
        api_put(f"/deposit/depositions/{record_id}", {"metadata": new_metadata})
        if VERBOSE:
            print(f"  [PUT] metadata mises a jour")

        # Publier
        api_post(f"/deposit/depositions/{record_id}/actions/publish")
        print(f"  [PUBLISH] record republie avec la nouvelle relation")
        summary["done"].append(label)

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  [ERR] HTTP {e.code} : {body[:200]}")
        summary["error"].append(label)
    except Exception as e:
        print(f"  [ERR] {type(e).__name__} : {e}")
        summary["error"].append(label)

    print()

# Rapport final
print("=" * 70)
print("RAPPORT FINAL")
print("=" * 70)
print(f"Relations ajoutees             : {len(summary['done'])}")
for x in summary["done"]:
    print(f"  - {x}")
print(f"Skippes (DOI SSRN non resolu)  : {len(summary['skipped_no_doi'])}")
for x in summary["skipped_no_doi"]:
    print(f"  - {x}")
print(f"Skippes (relation deja posee)  : {len(summary['skipped_already'])}")
for x in summary["skipped_already"]:
    print(f"  - {x}")
print(f"Erreurs                        : {len(summary['error'])}")
for x in summary["error"]:
    print(f"  - {x}")

if not APPLY and summary["done"]:
    print()
    print("DRY-RUN termine. Pour appliquer : python zenodo_add_ssrn_links.py --apply")
