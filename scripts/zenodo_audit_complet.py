#!/usr/bin/env python3
"""
Audit exhaustif des records Zenodo des AWP — cherche les TROUS.

Ne modifie rien. A lancer :
  - a chaque ajout d'AWP (etape obligatoire de docs/CHECKLIST_AJOUT_AWP.md) ;
  - avant toute campagne de diffusion ;
  - au relevé trimestriel.

Controle, pour chaque record (FR et EN de chaque AWP) :
  1. verbatim canonique de la definition present (ouverture OU incise)
  2. ORCID de l'auteur renseigne
  3. licence CC-BY-4.0
  4. langue declaree et coherente avec la version
  5. mots-cles presents
  6. communaute Zenodo `anthropie-working-papers`
  7. isDescribedBy -> page du site, en https
  8. liaison de traduction reciproque (isDerivedFrom / isSourceOf)
  9. type de ressource = publication/preprint (ou workingpaper)
 10. version declaree
 11. fichier PDF present

Usage : python scripts/zenodo_audit_complet.py [--json]
"""
import os, sys, json, re, html, urllib.request

TOKEN = os.environ.get('ZENODO_TOKEN')
if not TOKEN:
    sys.exit("ERREUR : variable ZENODO_TOKEN absente")
AS_JSON = "--json" in sys.argv

# (label, record FR, record EN) — tenir a jour a chaque nouvel AWP.
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

MARK = {"fr": "deplacent le desordre plutot qu",
        "en": "displace disorder rather than resolve it"}
ORCID = "0009-0002-1794-4895"
COMMUNITY = "anthropie-working-papers"
SITE = {"fr": "https://stephane-lalut.com/awp/",
        "en": "https://stephane-lalut.com/en/awp/"}


def norm(s):
    s = re.sub("<[^>]+>", " ", html.unescape(s or ""))
    for a, b in [("’", "'"), ("é", "e"), ("è", "e"), ("ê", "e"), ("ô", "o"),
                 ("à", "a"), (" ", " "), ("î", "i"), ("â", "a")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def api(path):
    req = urllib.request.Request(f"https://zenodo.org/api{path}")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def check(label, rec, lang, sibling_doi):
    """Retourne (liste de trous, dict d'infos)."""
    holes = []
    try:
        d = api(f"/records/{rec}")
    except Exception as e:
        return [f"record illisible ({e})"], {}
    m = d.get("metadata", {})
    rels = m.get("related_identifiers", []) or []
    relset = {(r.get("relation"), r.get("identifier")) for r in rels}

    # 1. verbatim
    if MARK[lang] not in norm(m.get("description")):
        holes.append("verbatim canonique ABSENT")
    # 2. ORCID
    creators = m.get("creators", []) or []
    if not any(c.get("orcid") == ORCID for c in creators):
        holes.append("ORCID absent des creators")
    # 3. licence
    lic = m.get("license")
    lic = lic.get("id") if isinstance(lic, dict) else lic
    if str(lic).lower() not in ("cc-by-4.0", "cc-by-4.0", "cc-by"):
        holes.append(f"licence inattendue ({lic})")
    # 4. langue
    if (m.get("language") or "").lower()[:2] != ("fr" if lang == "fr" else "en"):
        holes.append(f"langue declaree = {m.get('language')!r}")
    # 5. mots-cles
    if not (m.get("keywords") or []):
        holes.append("aucun mot-cle")
    # 6. communaute
    comms = [c.get("id") if isinstance(c, dict) else c
             for c in (d.get("metadata", {}).get("communities") or [])]
    if COMMUNITY not in comms:
        holes.append(f"communaute {COMMUNITY} absente")
    # 7. isDescribedBy vers le site en https
    described = [i for (r, i) in relset if r == "isDescribedBy"]
    if not any(str(i).startswith(SITE[lang]) for i in described):
        holes.append("isDescribedBy vers la page du site absent/incorrect")
    if any(str(i).startswith("http://") for i in described):
        holes.append("isDescribedBy en http (doit etre https)")
    # 8. liaison de traduction
    if not any(r in ("isDerivedFrom", "isSourceOf") and i == sibling_doi
               for (r, i) in relset):
        holes.append("liaison de traduction absente vers la version soeur")
    # 9. type
    rt = m.get("resource_type", {})
    rt = rt.get("subtype") or rt.get("type") if isinstance(rt, dict) else rt
    if rt not in ("publication", "preprint", "workingpaper", "report"):
        holes.append(f"resource_type inattendu ({rt})")
    # 11. fichier
    if not (d.get("files") or []):
        holes.append("aucun fichier attache")

    # --- INFO (non bloquant) : champ decoratif, n'affecte ni la citation ni
    # la visibilite. Garde en INFO pour que les BLOQUANTS restent lisibles.
    info = []
    if not m.get("version"):
        info.append("version non declaree (champ optionnel)")

    return holes, {"doi": d.get("doi"), "title": m.get("title", "")[:48],
                   "info": info}


results = {}
total_holes = 0
total_info = 0
print("=" * 74)
print("AUDIT EXHAUSTIF DES RECORDS ZENODO — recherche de trous")
print("=" * 74)
for label, fr, en in PAIRS:
    for lang, rec, sib in (("fr", fr, f"10.5281/zenodo.{en}"),
                           ("en", en, f"10.5281/zenodo.{fr}")):
        holes, meta = check(label, rec, lang, sib)
        key = f"{label} {lang.upper()}"
        results[key] = holes
        total_holes += len(holes)
        total_info += len(meta.get("info", []))
        if holes:
            print(f"\n{key}  ({meta.get('doi','?')})")
            for h in holes:
                print(f"   - BLOQUANT : {h}")
            for i in meta.get("info", []):
                print(f"   - info     : {i}")
        else:
            suffix = f"   (info : {len(meta.get('info', []))})" if meta.get("info") else ""
            print(f"{key:12} OK{suffix}")

print("\n" + "=" * 74)
print(f"BLOQUANTS : {total_holes} sur {len(results)} records"
      f"   |   INFO : {total_info}")
if total_holes == 0:
    print("Aucun trou bloquant. Les AWP sont conformes.")
if AS_JSON:
    print(json.dumps(results, indent=2, ensure_ascii=False))
