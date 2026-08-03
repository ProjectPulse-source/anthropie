#!/usr/bin/env python3
"""
Audit exhaustif des records Zenodo des AWP — cherche les TROUS.

Ne modifie rien. A lancer :
  - a chaque ajout d'AWP (etape obligatoire de docs/CHECKLIST_AJOUT_AWP.md) ;
  - avant toute campagne de diffusion ;
  - au relevé trimestriel.

Controle, pour chaque record de chaque AWP, dans toutes les langues declarees :
  1. verbatim canonique de la definition present (ouverture OU incise)
  2. ORCID de l'auteur renseigne
  3. licence CC-BY-4.0
  4. langue declaree, NORMALISEE (es=spa, en=eng, fr=fra/fre) et coherente
  5. mots-cles presents
  6. communaute Zenodo `anthropie-working-papers`
  7. SITE_RELATION : PASS / N-A justifie / FAIL — voir ci-dessous
  8. liaison de traduction (isDerivedFrom / isSourceOf) vers la version source
  9. type de ressource = publication/preprint (ou workingpaper)
 10. version declaree
 11. fichier PDF present

Controle 7 — pourquoi il n'est plus universellement bloquant :
  `related_identifiers` est un champ FACULTATIF de Zenodo. L'absence d'un
  isDescribedBy n'est donc pas une incompletude du depot. Ce qui serait fautif,
  c'est de DECLARER une relation vers une page qui ne decrit pas cette version —
  par exemple faire pointer un depot espagnol vers la page francaise. D'ou :
    PASS  la locale a une page, et le record la declare correctement ;
    N-A   la locale n'a pas de page sur le site (site_policy: optional) ;
    FAIL  une relation est declaree mais pointe vers une autre langue,
          une autre version, ou est en http.

Usage : python scripts/zenodo_audit_complet.py [--json]
"""
import os, sys, json, re, html, urllib.request

TOKEN = os.environ.get('ZENODO_TOKEN')
if not TOKEN:
    sys.exit("ERREUR : variable ZENODO_TOKEN absente")
AS_JSON = "--json" in sys.argv

# Un AWP = une langue SOURCE + N traductions. `records` : langue -> id Zenodo.
# Une langue absente du dict n'est pas deposee ; elle n'est pas auditee et ce
# n'est pas un trou. Tenir a jour a chaque nouveau depot.
#
# CONVENTION MIXTE, et c'est deliberé (2026-08-03) :
#   - une oeuvre AVEC plusieurs versions est suivie par son recid de CONCEPT,
#     qui resout toujours vers la derniere version publiee. L'auditeur suit
#     alors l'oeuvre et non un etat fige : personne n'a a le remettre a jour
#     quand une v2 parait. C'est le cas de l'espagnol (concept 21766183).
#   - une oeuvre a version unique reste sur son recid de VERSION.
#
# Pourquoi ne pas tout passer au concept : essaye le meme jour, verifie sur les
# 16 records, et REVERTE. Le controle 8 (liaison de traduction) compare les
# relations telles que les records les DECLARENT — et elles pointent vers des
# DOI de version. Basculer le registre au concept faisait passer 16 records sur
# 17 en bloquant, sans qu'aucun depot n'ait change. Le registre doit parler la
# meme langue que les donnees qu'il controle.
#
# Corollaire de comparaison : la liste des membres d'une communaute Zenodo porte
# des recids de VERSION. Le controle 6 compare donc le record REELLEMENT RESOLU
# (d["id"]), pas l'identifiant demande — sans quoi une entree au concept est
# declaree hors communaute alors qu'elle en est membre (constate le 03/08).
#
# N'inscrire un id qu'une fois le record PUBLIE : un brouillon n'est pas
# interrogeable par /records, et l'auditeur le compterait en echec alors que le
# depot est simplement en cours.
AWPS = [
    {"label": "AWP-01", "source": "fr",
     "records": {"fr": "19266862", "en": "19431208", "es": "21766183"}},
    {"label": "AWP-02", "source": "fr", "records": {"fr": "19268037", "en": "19433086"}},
    {"label": "AWP-03", "source": "fr", "records": {"fr": "19268769", "en": "19434094"}},
    {"label": "AWP-04", "source": "fr", "records": {"fr": "19269244", "en": "19439921"}},
    {"label": "AWP-05", "source": "fr", "records": {"fr": "19269487", "en": "19440866"}},
    {"label": "AWP-06", "source": "fr", "records": {"fr": "20025421", "en": "20077993"}},
    {"label": "AWP-07", "source": "fr", "records": {"fr": "21200286", "en": "21200288"}},
    {"label": "AWP-08", "source": "fr", "records": {"fr": "21506320", "en": "21507249"}},
    # AWP-01 espagnol : v1 publiee le 2026-08-03 (21766184), v2 le meme jour
    # (21775366, correction de deux renvois de note). Le concept 21766183 suit.
]

ORCID = "0009-0002-1794-4895"
COMMUNITY = "anthropie-working-papers"

# Profil par langue. UNE table, pas deux paralleles : deux tables indexees par la
# meme cle sont deux sources qui finissent par diverger.
#   aliases     : codes acceptes par Zenodo/DataCite pour cette langue (ISO 639-1 et -2)
#   mark        : verbatim canonique de la definition, forme normalisee (voir norm())
#   site_policy : "required" si le site publie cette langue, "optional" sinon
#   site_url    : prefixe de la page qui decrit cette version ; None si aucune
LANG_PROFILES = {
    "fr": {
        "aliases": {"fr", "fra", "fre", "fr-fr"},
        "mark": "deplacent le desordre plutot qu",
        "site_policy": "required",
        "site_url": "https://stephane-lalut.com/awp/",
    },
    "en": {
        "aliases": {"en", "eng", "en-us", "en-gb"},
        "mark": "displace disorder rather than resolve it",
        "site_policy": "required",
        "site_url": "https://stephane-lalut.com/en/awp/",
    },
    "es": {
        "aliases": {"es", "spa", "es-es"},
        # Verbatim canonique espagnol, arrete au cadrage du 2026-08-02 et employe
        # a l'identique dans le corps du texte et dans la description du depot.
        "mark": "desplazan el desorden en lugar de resolverlo",
        # Le site ne declare que fr et en (config/_default/hugo.toml). Tant qu'il
        # n'existe pas de /es/awp/, aucune page ne peut decrire cette version :
        # le controle 7 rendra N-A, et surtout PAS un isDescribedBy vers la page
        # francaise, qui serait une relation fausse.
        "site_policy": "optional",
        "site_url": None,
    },
}


def profil(lang):
    """FAIL-CLOSED : une langue inconnue arrete l'audit au lieu d'etre ignoree."""
    p = LANG_PROFILES.get(lang)
    if p is None:
        sys.exit(f"ERREUR : langue {lang!r} absente de LANG_PROFILES. "
                 f"Connues : {', '.join(sorted(LANG_PROFILES))}. "
                 f"Ajouter son profil plutot que de contourner le controle.")
    return p


def langue_conforme(declaree, attendue):
    """Normalise avant comparaison : es == spa, en == eng, fr == fra/fre."""
    return str(declaree or "").strip().lower().replace("_", "-") in profil(attendue)["aliases"]


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


_MEMBRES = None


def membres_communaute():
    """Identifiants des records REELLEMENT admis dans la communaute.

    Interroge la communaute, pas le record : un record peut declarer une
    communaute qu'il n'a jamais integree (demande d'inclusion en attente).
    Un seul appel par execution, memorise — le controle passe sur 17 records.
    """
    global _MEMBRES
    if _MEMBRES is None:
        # size est plafonne cote Zenodo (400 au-dela) : on pagine.
        _MEMBRES, page = set(), 1
        while True:
            d = api(f"/communities/{COMMUNITY}/records?size=50&page={page}")
            hits = d.get("hits", {}).get("hits", [])
            _MEMBRES |= {str(h["id"]) for h in hits}
            if len(_MEMBRES) >= d.get("hits", {}).get("total", 0) or not hits:
                break
            page += 1
    return _MEMBRES


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

    prof = profil(lang)
    # 1. verbatim
    if prof["mark"] not in norm(m.get("description")):
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
    # 4. langue — normalisee (le test sur les deux premieres lettres echouait
    #    sur les codes ISO 639-2 : « spa » ne commence pas par « es »)
    if not langue_conforme(m.get("language"), lang):
        holes.append(f"langue declaree = {m.get('language')!r}, attendu "
                     f"un alias de {lang} ({'/'.join(sorted(prof['aliases']))})")
    # 5. mots-cles
    if not (m.get("keywords") or []):
        holes.append("aucun mot-cle")
    # 6. communaute — APPARTENANCE REELLE, pas champ declare
    #
    # Ce controle lisait `metadata.communities` du record. Ce champ reflete la
    # DEMANDE d'inclusion, pas l'admission : sur Zenodo, publier avec un champ
    # `communities` ouvre une requete que la communaute doit ACCEPTER. Tant
    # qu'elle dort, le record n'est dans aucune communaute — mais il declare
    # la sienne, et l'audit passait au vert.
    #
    # Constate le 2026-08-03 : AWP-08 FR et EN etaient hors communaute depuis
    # leur depot (demandes en attente), et l'auditeur les donnait conformes.
    # On interroge donc la liste des membres de la communaute : la seule
    # source qui distingue « a demande » de « est dedans ».
    # On compare le record REELLEMENT RESOLU, pas l'identifiant demande : une
    # entree du registre peut etre un recid de CONCEPT (qui resout vers la
    # derniere version), tandis que la liste des membres de la communaute porte
    # des recids de VERSION. Comparer les deux directement accusait a tort
    # l'espagnol, membre reel, des que son entree est passee au concept.
    if str(d.get("id", rec)) not in membres_communaute():
        holes.append(f"communaute {COMMUNITY} : record absent "
                     f"(demande d'inclusion peut-etre en attente d'acceptation)")
    # 7. SITE_RELATION — trois etats, voir docstring
    described = [str(i) for (r, i) in relset if r == "isDescribedBy"]
    site_state = "PASS"
    if any(i.startswith("http://") for i in described):
        holes.append("isDescribedBy en http (doit etre https)")
        site_state = "FAIL"
    if prof["site_url"]:
        if not any(i.startswith(prof["site_url"]) for i in described):
            holes.append("isDescribedBy vers la page du site absent/incorrect")
            site_state = "FAIL"
    else:
        # Aucune page pour cette langue : l'absence est normale. Mais declarer
        # une relation vers la page d'une AUTRE langue serait une relation fausse.
        autres = [u for c, u in ((c, LANG_PROFILES[c]["site_url"]) for c in LANG_PROFILES)
                  if c != lang and u]
        if any(any(i.startswith(u) for u in autres) for i in described):
            holes.append("isDescribedBy pointe vers la page d'une AUTRE langue "
                         "(relation fausse : cette page ne decrit pas cette version)")
            site_state = "FAIL"
        elif site_state == "PASS":
            site_state = "N-A"
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
                   "site_relation": site_state, "info": info}


results = {}
total_holes = 0
total_info = 0
print("=" * 74)
print("AUDIT EXHAUSTIF DES RECORDS ZENODO — recherche de trous")
print("=" * 74)
for awp in AWPS:
    label, src_lang, recs = awp["label"], awp["source"], awp["records"]
    src_rec = recs.get(src_lang)
    for lang, rec in recs.items():
        # La source doit pointer vers ses traductions ; une traduction, vers la source.
        if lang == src_lang:
            autres = [r for l, r in recs.items() if l != src_lang]
            sib = f"10.5281/zenodo.{autres[0]}" if autres else None
        else:
            sib = f"10.5281/zenodo.{src_rec}" if src_rec else None
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
            bits = []
            if meta.get("site_relation") == "N-A":
                bits.append("site N-A justifie")
            if meta.get("info"):
                bits.append(f"info : {len(meta['info'])}")
            suffix = f"   ({' | '.join(bits)})" if bits else ""
            print(f"{key:12} OK{suffix}")

print("\n" + "=" * 74)
print(f"BLOQUANTS : {total_holes} sur {len(results)} records"
      f"   |   INFO : {total_info}")
if total_holes == 0:
    print("Aucun trou bloquant. Les AWP sont conformes.")
if AS_JSON:
    print(json.dumps(results, indent=2, ensure_ascii=False))
