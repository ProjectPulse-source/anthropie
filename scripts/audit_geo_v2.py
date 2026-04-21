#!/usr/bin/env python3
"""audit_geo_v2.py — parsing HTML/JSON-LD rigoureux + génération rapport markdown."""

import os, re, json, sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import socket

socket.setdefaulttimeout(10)

# Emoji constants (Python 3.11 can't use \u escapes inside f-string expressions)
OK = "✅"
FAIL = "❌"
OPP = "\💡"
WARN = "⚠️"
DASH = "—"

BASE = os.environ["AUDIT_BASE"]
REPORT = os.environ["AUDIT_REPORT"]

def fetch(url, head=False):
    try:
        req = Request(url, method="HEAD" if head else "GET",
                      headers={"User-Agent": "audit-geo-v2/1.0"})
        with urlopen(req, timeout=10) as r:
            return r.status, (r.read().decode("utf-8", errors="replace") if not head else ""), dict(r.headers)
    except HTTPError as e:
        return e.code, "", {}
    except (URLError, socket.timeout, Exception):
        return 0, "", {}

def extract_jsonld(html):
    """Extrait tous les blocs JSON-LD et les parse. Gère @graph."""
    blocks = []
    pattern = re.compile(
        r'<script[^>]*type=["\']?application/ld\+json["\']?[^>]*>(.*?)</script>',
        re.DOTALL | re.IGNORECASE)
    for m in pattern.finditer(html):
        raw = m.group(1).strip()
        try:
            data = json.loads(raw)
            if isinstance(data, dict) and "@graph" in data:
                for item in data["@graph"]:
                    if isinstance(item, dict):
                        blocks.append(item)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        blocks.append(item)
            elif isinstance(data, dict):
                blocks.append(data)
        except json.JSONDecodeError:
            pass
    return blocks

def find_by_type(blocks, type_name):
    """Retourne les blocs JSON-LD d'un @type donné."""
    out = []
    for b in blocks:
        t = b.get("@type")
        if isinstance(t, str) and t == type_name:
            out.append(b)
        elif isinstance(t, list) and type_name in t:
            out.append(b)
    return out

def get_sameAs(block):
    """Retourne la liste de sameAs, que ce soit string ou array."""
    sa = block.get("sameAs")
    if isinstance(sa, str):
        return [sa]
    if isinstance(sa, list):
        return [x for x in sa if isinstance(x, str)]
    return []

def extract_meta(html, name):
    """Extrait <meta name=X content=Y> robuste (guillemets ou pas)."""
    pattern = re.compile(
        rf'<meta\s[^>]*name=["\']?{re.escape(name)}(?:["\']|\s|/|>)[^>]*?content=(["\'])([^"\']*)\1',
        re.IGNORECASE)
    m = pattern.search(html)
    if m: return m.group(2)
    # Variante : content avant name
    pattern2 = re.compile(
        rf'<meta\s[^>]*content=(["\'])([^"\']*)\1[^>]*name=["\']?{re.escape(name)}',
        re.IGNORECASE)
    m = pattern2.search(html)
    return m.group(2) if m else None

def extract_links_from_page(html, patterns):
    """Retourne les href qui matchent un pattern donné (ex: /citation\\.bib$)."""
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
    out = {}
    for label, pat in patterns.items():
        for h in hrefs:
            if re.search(pat, h):
                out[label] = h
                break
    return out

def flag(status, label="", impact=None):
    """status: 'ok', 'missing_contract', 'opportunity', 'warn'
       retourne une cellule markdown."""
    symbols = {
        "ok": "✅",
        "missing_contract": "❌",
        "opportunity": "\💡",
        "warn": "⚠️"
    }
    sym = symbols.get(status, "·")
    if impact and status == "opportunity":
        return f"{sym} opportunité — impact {impact}"
    if label:
        return f"{sym} {label}"
    return sym

# ═══════════════════════════════════════════════════════════════
# COLLECTE DONNÉES
# ═══════════════════════════════════════════════════════════════

def safe_env(k): return os.environ.get(k, "").strip()

URL_AWP_FR = safe_env("AUDIT_URL_AWP_FR")
URL_AWP_EN = safe_env("AUDIT_URL_AWP_EN")
URL_SERIE = safe_env("AUDIT_URL_SERIE")
URL_ABOUT = safe_env("AUDIT_URL_ABOUT")
URL_DEFINITION = safe_env("AUDIT_URL_DEFINITION")
URL_HOME_FR = safe_env("AUDIT_URL_HOME_FR")
URL_HOME_EN = safe_env("AUDIT_URL_HOME_EN")
URLS_LIVRES = [u for u in safe_env("AUDIT_URLS_LIVRES").splitlines() if u.strip()]
ALL_URLS = [u for u in safe_env("AUDIT_URLS").splitlines() if u.strip()]

# ═══════════════════════════════════════════════════════════════
# GÉNÉRATION RAPPORT
# ═══════════════════════════════════════════════════════════════

import datetime
out = []
def w(s=""): out.append(s)

w("# Audit GEO v2 — stephane-lalut.com")
w()
w(f"Généré : {datetime.datetime.now():%Y-%m-%d %H:%M}")
w(f"Base : `{BASE}`")
w()
w("## Légende")
w()
w("| Symbole | Sens |")
w("|---|---|")
w("| ✅ | Présent et conforme |")
w("| ❌ | Manquant — élément du contrat initial |")
w("| \💡 | Opportunité GEO 2026 — enrichissement recommandé |")
w("| ⚠️ | Anomalie à investiguer |")
w()
w("L'échelle sépare **ce qui devait être présent** (❌ = vrai manque) de **ce qui pourrait l'être** (\💡 = opportunité, décision ouverte).")
w()
w("Le rapport est en deux parties : **A — Audit on-site** (reproductible, verdict opérationnel) et **B — Annexe écosystème** (indicative, variable dans le temps).")
w()
w("---")
w()
w("# Partie A — Audit on-site (reproductible)")
w()

# ──────────────────────────────────────────────
# A.1 — Fondations crawlabilité
# ──────────────────────────────────────────────
w("## A.1 Crawlabilité (robots.txt, sitemap, llms.txt)")
w()

_, robots, _ = fetch(f"{BASE}/robots.txt")
_, llms_body, _ = fetch(f"{BASE}/llms.txt")
llms_code, _, _ = fetch(f"{BASE}/llms.txt", head=True)

ai_crawlers = [
    ("GPTBot", "OpenAI"),
    ("ClaudeBot", "Anthropic (Claude)"),
    ("anthropic-ai", "Anthropic (legacy)"),
    ("PerplexityBot", "Perplexity"),
    ("Google-Extended", "Google AI / Gemini"),
    ("CCBot", "Common Crawl (corpus d'entraînement LLM)"),
    ("Googlebot-Scholar", "Google Scholar"),
    ("Bingbot", "Bing / Copilot")
]

w("| Crawler | Présent dans robots.txt | Rôle |")
w("|---|---|---|")
for name, role in ai_crawlers:
    present = bool(re.search(rf'b{re.escape(name)}\b', robots, re.IGNORECASE))
    w(f"| `{name}` | {'✅' if present else '💡 impact **fort**'} | {role} |")
w()
w(f"- `llms.txt` : {'✅ HTTP 200' if llms_code == 200 else '💡 absent — impact **moyen** (norme émergente, utile pour auto-description du site aux LLMs)'}")

# Sitemaps
n_root = len(re.findall(r'<loc>', fetch(f"{BASE}/sitemap.xml")[1]))
n_fr = len(re.findall(r'<loc>', fetch(f"{BASE}/fr/sitemap.xml")[1]))
n_en = len(re.findall(r'<loc>', fetch(f"{BASE}/en/sitemap.xml")[1]))
w(f"- Sitemaps : racine={n_root} entrée(s), FR={n_fr}, EN={n_en}")
w()

# ──────────────────────────────────────────────
# A.2 — Inventaire JSON-LD par page-clé
# ──────────────────────────────────────────────
w("## A.2 Inventaire JSON-LD par page")
w()

pages_to_check = [
    ("Accueil FR", URL_HOME_FR),
    ("Accueil EN", URL_HOME_EN),
    ("À propos", URL_ABOUT),
    ("Définition anthropie", URL_DEFINITION),
    ("Série AWP", URL_SERIE),
    ("AWP échantillon (FR)", URL_AWP_FR),
    ("AWP échantillon (EN)", URL_AWP_EN)
] + [(f"Livre — {u.rsplit('/', 2)[-2]}", u) for u in URLS_LIVRES[:3]]

html_cache = {}
w("| Page | URL | @types détectés |")
w("|---|---|---|")
for label, url in pages_to_check:
    if not url:
        w(f"| {label} | *(non détecté au sitemap)* | — |")
        continue
    code, html, _ = fetch(url)
    html_cache[url] = html
    if code != 200:
        w(f"| {label} | `{url}` | ⚠️ HTTP {code} |")
        continue
    blocks = extract_jsonld(html)
    types = set()
    for b in blocks:
        t = b.get("@type")
        if isinstance(t, str): types.add(t)
        elif isinstance(t, list): types.update(t)
    types_str = ", ".join(sorted(types)) if types else "*(aucun)*"
    path = url.replace(BASE, "") or "/"
    w(f"| {label} | `{path}` | {types_str} |")
w()

# ──────────────────────────────────────────────
# A.3 — Page Person (/a-propos/)
# ──────────────────────────────────────────────
w("## A.3 Page Person — sameAs et champs")
w()

if URL_ABOUT and URL_ABOUT in html_cache:
    html = html_cache[URL_ABOUT]
    blocks = extract_jsonld(html)
    # Check both Person and ProfilePage (Person may be nested in mainEntity)
    persons = find_by_type(blocks, "Person")
    profiles = find_by_type(blocks, "ProfilePage")
    if not persons and profiles:
        for pp in profiles:
            me = pp.get("mainEntity")
            if isinstance(me, dict) and me.get("@type") == "Person":
                persons.append(me)
    if persons:
        p = persons[0]
        w("**JSON-LD Person détecté.**")
        w()
        w("### Champs présents")
        w()
        fields_contract = ["name", "jobTitle", "url"]
        fields_opp = {
            "description": "moyen",
            "image": "faible",
            "email": "faible",
            "affiliation": "moyen",
            "knowsAbout": "fort",
            "alumniOf": "faible",
            "birthDate": "faible",
            "nationality": "faible"
        }
        w("| Champ | État | Impact |")
        w("|---|---|---|")
        for f in fields_contract:
            state = "✅" if f in p else "❌"
            w(f"| `{f}` | {state} | contrat |")
        for f, imp in fields_opp.items():
            if f in p:
                w(f"| `{f}` | ✅ | — |")
            else:
                w(f"| `{f}` | \💡 | **{imp}** |")
        w()
        w("### sameAs — identifiants externes")
        w()
        sa = get_sameAs(p)
        if not sa:
            w("❌ Aucun `sameAs` — **impact fort** sur reconnaissance d'entité par les LLMs.")
        else:
            w(f"**{len(sa)} identifiant(s) présent(s) :**")
            for u in sa:
                w(f"- {u}")
        w()
        expected = {
            "ORCID": ("orcid.org", "contrat"),
            "Zenodo": ("zenodo.org", "contrat"),
            "OpenAlex": ("openalex.org", "fort"),
            "Wikidata": ("wikidata.org", "fort"),
            "Google Scholar": ("scholar.google", "moyen (quand profil créé)"),
            "ResearchGate": ("researchgate.net", "moyen"),
            "GitHub": ("github.com", "faible"),
            "LinkedIn": ("linkedin.com", "faible"),
            "Academia.edu": ("academia.edu", "moyen"),
            "RePEC/IDEAS": ("ideas.repec.org", "moyen"),
            "MPRA": ("mpra.ub", "moyen")
        }
        w("**Cartographie vs identifiants attendus :**")
        w()
        w("| Identifiant | Présent | Statut |")
        w("|---|---|---|")
        for name, (pat, imp) in expected.items():
            found = any(pat in u for u in sa)
            if found:
                w(f"| {name} | ✅ | — |")
            else:
                tag = "contrat ❌" if imp == "contrat" else f"\💡 opportunité — impact **{imp}**"
                w(f"| {name} | — | {tag} |")
    else:
        w("❌ Pas de JSON-LD Person sur la page À propos — **impact fort**.")
else:
    w("⚠️ Page À propos non détectée dans le sitemap.")
w()

# ──────────────────────────────────────────────
# A.4 — ScholarlyArticle (pages AWP)
# ──────────────────────────────────────────────
w("## A.4 Pages AWP — ScholarlyArticle")
w()

for label, url in [("FR", URL_AWP_FR), ("EN", URL_AWP_EN)]:
    if not url or url not in html_cache:
        w(f"⚠️ AWP {label} non échantillonné.")
        continue
    html = html_cache[url]
    blocks = extract_jsonld(html)
    articles = find_by_type(blocks, "ScholarlyArticle") + find_by_type(blocks, "Article")
    w(f"### {label} — `{url.replace(BASE,'')}`")
    w()
    if not articles:
        w(f"❌ Aucun `ScholarlyArticle` détecté — **impact fort**.")
        w()
        continue
    a = articles[0]
    fields = {
        "headline": ("contrat", ""),
        "author": ("contrat", ""),
        "datePublished": ("contrat", ""),
        "inLanguage": ("contrat", ""),
        "identifier": ("contrat", "(DOI)"),
        "license": ("contrat", "(CC-BY)"),
        "publisher": ("fort", "série émettrice"),
        "isPartOf": ("fort", "rattache à la série AWP"),
        "citation": ("moyen", "références citées par l'article"),
        "about": ("fort", "concepts abordés — clé GEO"),
        "keywords": ("moyen", "mots-clés structurés"),
        "abstract": ("fort", "résumé exploitable par LLM"),
        "mainEntityOfPage": ("faible", "ancrage canonique"),
        "sameAs": ("moyen", "pont vers Zenodo/DOI")
    }
    w("| Champ | État | Impact GEO |")
    w("|---|---|---|")
    for f, (imp, note) in fields.items():
        if f in a and a[f]:
            w(f"| `{f}` | ✅ | — |")
        else:
            if imp == "contrat":
                w(f"| `{f}` | ❌ | **contrat** |")
            else:
                note_str = f" — {note}" if note else ""
                w(f"| `{f}` | \💡 | **{imp}**{note_str} |")
    w()

# ──────────────────────────────────────────────
# A.5 — Entité Série
# ──────────────────────────────────────────────
w("## A.5 Page Série AWP — type d'entité")
w()

if URL_SERIE and URL_SERIE in html_cache:
    html = html_cache[URL_SERIE]
    blocks = extract_jsonld(html)
    types_found = set()
    for b in blocks:
        t = b.get("@type")
        if isinstance(t, str): types_found.add(t)
        elif isinstance(t, list): types_found.update(t)

    candidates = {
        "ItemList": ("contrat", "liste plate — prévu initialement"),
        "CollectionPage": ("faible", "page de collection générique"),
        "Periodical": ("fort", "série périodique — identité éditoriale forte"),
        "PublicationIssue": ("moyen", "numéro de la série"),
        "CreativeWorkSeries": ("fort", "série d'œuvres — plus sémantique"),
        "BlogPosting": ("warn", "inadéquat pour AWP")
    }
    w("| Type | Détecté | Lecture |")
    w("|---|---|---|")
    for t, (imp, note) in candidates.items():
        present = t in types_found
        if present:
            w(f"| `{t}` | ✅ | {note} |")
        else:
            tag = "— présent " if imp == "contrat" else f"\💡 **{imp}**"
            w(f"| `{t}` | — | {note} ({tag}) |")
    w()
    w("**Note** : Dans le contrat initial, la série est un `ItemList` et le lien vers la série se fait via `isPartOf` à l'intérieur de chaque `ScholarlyArticle`. Une montée en `CreativeWorkSeries` ou `Periodical` **en complément** (pas en remplacement) durcirait l'identité éditoriale de la série auprès des LLMs.")
    w()
else:
    w("⚠️ Page série non détectée.")
w()

# ──────────────────────────────────────────────
# A.6 — Livres
# ──────────────────────────────────────────────
w("## A.6 Pages livres — Book")
w()
for url in URLS_LIVRES[:4]:
    if url not in html_cache:
        code, html, _ = fetch(url)
        html_cache[url] = html
    else:
        code, html = 200, html_cache[url]
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    w(f"### `{slug}`")
    w()
    if not html:
        w("⚠️ Page vide ou inaccessible.")
        w()
        continue
    books = find_by_type(extract_jsonld(html), "Book")
    if not books:
        w("❌ Pas de JSON-LD `Book` — **contrat**.")
        w()
        continue
    b = books[0]
    fields = {
        "name": "contrat", "author": "contrat", "isbn": "contrat",
        "datePublished": "contrat", "publisher": "contrat", "inLanguage": "contrat",
        "image": "contrat", "description": "moyen",
        "numberOfPages": "faible", "bookFormat": "faible",
        "about": "fort", "sameAs": "moyen (Amazon/Wikidata)"
    }
    w("| Champ | État | Impact |")
    w("|---|---|---|")
    for f, imp in fields.items():
        if f in b and b[f]:
            w(f"| `{f}` | ✅ | — |")
        else:
            tag = "**contrat**" if imp == "contrat" else f"\💡 **{imp}**"
            w(f"| `{f}` | — | {tag} |")
    w()

# ──────────────────────────────────────────────
# A.7 — Structure extractible (AWP)
# ──────────────────────────────────────────────
w("## A.7 Structure de page — extractibilité LLM")
w()
for label, url in [("FR", URL_AWP_FR), ("EN", URL_AWP_EN)]:
    if not url or url not in html_cache:
        continue
    html = html_cache[url]
    n_h1 = len(re.findall(r'<h1\b', html, re.IGNORECASE))
    n_h2 = len(re.findall(r'<h2\b', html, re.IGNORECASE))
    n_h3 = len(re.findall(r'<h3\b', html, re.IGNORECASE))
    n_ids = len(re.findall(r'sid=["\'][^"\']+["\']', html))
    n_article = len(re.findall(r'<article\b', html, re.IGNORECASE))
    n_time = len(re.findall(r'<time\b', html, re.IGNORECASE))
    faq_present = bool(re.search(r'"@type":\s*"(FAQPage|Question)"', html))
    w(f"### AWP {label}")
    w()
    w(f"- `<h1>` : {n_h1} — {'✅' if n_h1 == 1 else '⚠️ attendu 1'}")
    w(f"- `<h2>` : {n_h2} (sectionnement)")
    w(f"- `<h3>` : {n_h3}")
    w(f"- ancres `id=\"…\"` : {n_ids} — {'✅' if n_ids >= 3 else '💡 opportunité — impact **moyen** (permet citation LLM vers sous-section)'}")
    w(f"- `<article>` : {'✅' if n_article else '💡 impact **faible**'}")
    w(f"- `<time>` : {'✅' if n_time else '💡 impact **faible**'}")
    w(f"- FAQ Schema : {'✅' if faq_present else '💡 impact **moyen**'}")
    w()

# ──────────────────────────────────────────────
# A.8 — Versions alternatives (lu dans la page)
# ──────────────────────────────────────────────
w("## A.8 Versions alternatives — liens réellement exposés")
w()

if URL_AWP_FR and URL_AWP_FR in html_cache:
    html = html_cache[URL_AWP_FR]
    found = extract_links_from_page(html, {
        "BibTeX": r"\.bib($|\?)",
        "RIS": r"\.ris($|\?)",
        "PDF (Zenodo)": r"zenodo\.org/.+\.pdf",
        "Markdown raw": r"\.md($|\?)"
    })
    w(f"**Liens détectés dans `{URL_AWP_FR.replace(BASE,'')}` :**")
    w()
    w("| Format | Présent sur la page | URL | HTTP |")
    w("|---|---|---|---|")
    for fmt in ["BibTeX", "RIS", "PDF (Zenodo)", "Markdown raw"]:
        if fmt in found:
            url = found[fmt]
            if not url.startswith("http"):
                url = BASE + url
            code, _, _ = fetch(url, head=True)
            w(f"| {fmt} | ✅ | `{url[:70]}` | {code} |")
        else:
            imp = {"BibTeX": "contrat", "RIS": "contrat",
                   "PDF (Zenodo)": "contrat", "Markdown raw": "faible"}.get(fmt, "faible")
            tag = "❌ contrat" if imp == "contrat" else f"\💡 **{imp}**"
            w(f"| {fmt} | {tag} | — | — |")
    w()

# Feed RSS
_, home, _ = fetch(URL_HOME_FR)
rss_links = re.findall(r'<link[^>]+rel=["\']alternate["\'][^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]+href=["\']([^"\']+)["\']', home, re.IGNORECASE)
w(f"**Feed RSS/Atom annoncé sur accueil :** {'✅ ' + rss_links[0] if rss_links else '💡 non annoncé — impact **moyen**'}")
code_rss, _, _ = fetch(f"{BASE}/index.xml", head=True)
w(f"**Feed `/index.xml` HTTP :** {code_rss}")
w()

# ──────────────────────────────────────────────
# Synthèse Partie A
# ──────────────────────────────────────────────
w("## A.9 Synthèse opérationnelle — Partie A")
w()
w("Les ❌ (manques au contrat) doivent être traités. Les \💡 (opportunités GEO) sont à arbitrer selon l'effort vs l'impact indiqué. Règle : ne pas appliquer toutes les opportunités — en sélectionner 2 ou 3 à impact **fort**.")
w()

w("---")
w()

# ══════════════════════════════════════════════════════════════
# PARTIE B — ANNEXE ÉCOSYSTÈME (indicative)
# ══════════════════════════════════════════════════════════════
w("# Partie B — Annexe écosystème (indicative, datée)")
w()
w(f"*Snapshot du {datetime.datetime.now():%Y-%m-%d %H:%M}. Ces données dépendent d'APIs externes et évoluent. À re-mesurer dans 4-6 semaines.*")
w()

# Wikidata
w("## B.1 Wikidata — items liés")
w()
qids = [
    ("Q138909233", "Stéphane Lalut (personne)"),
    ("Q138827949", "Anthropie (concept)"),
    ("Q138827344", "ANTHROPIE — Ordre ici, dette ailleurs (livre)"),
    ("Q138910896", "Dette publique (livre)")
]
w("| Q-ID | Attendu | Label FR | Label EN | Claims | Sitelinks |")
w("|---|---|---|---|---|---|")
for qid, expected in qids:
    code, body, _ = fetch(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")
    if code != 200 or not body:
        w(f"| {qid} | {expected} | ⚠️ API | — | — | — |")
        continue
    try:
        d = json.loads(body)
        entity = list(d["entities"].values())[0]
        lfr = entity.get("labels", {}).get("fr", {}).get("value", "—")
        len_ = entity.get("labels", {}).get("en", {}).get("value", "—")
        nclaims = len(entity.get("claims", {}))
        nsl = len(entity.get("sitelinks", {}))
        w(f"| {qid} | {expected} | {lfr} | {len_} | {nclaims} | {nsl} |")
    except Exception as e:
        w(f"| {qid} | {expected} | ⚠️ parse | — | — | — |")
w()
w("**Lecture** : un nombre de *claims* < 8 est faible pour une entité académique. Opportunité de densification via Laura. Impact **fort** sur reconnaissance par les LLMs qui consomment Wikidata en pré-entraînement.")
w()

# OpenAlex
w("## B.2 OpenAlex — indexation du corpus")
w()
code, body, _ = fetch("https://api.openalex.org/works?filter=authorships.author.id:A5130851063&per_page=50&select=title,doi,publication_year,cited_by_count,type")
if code == 200 and body:
    try:
        d = json.loads(body)
        total = d.get("meta", {}).get("count", "?")
        w(f"**Nombre total de works indexés pour A5130851063 : {total}**")
        w()
        w("| Année | Citations | DOI | Titre (tronqué) | Type |")
        w("|---|---|---|---|---|")
        for wrk in d.get("results", [])[:25]:
            title = (wrk.get("title") or "")[:60]
            doi = (wrk.get("doi") or "").replace("https://doi.org/", "")
            year = wrk.get("publication_year", "?")
            cits = wrk.get("cited_by_count", 0)
            typ = wrk.get("type", "—")
            w(f"| {year} | {cits} | `{doi}` | {title} | {typ} |")
    except Exception:
        w("⚠️ Parsing OpenAlex impossible.")
else:
    w(f"⚠️ API OpenAlex HTTP {code}.")
w()
w("**Lecture** : vérifier que chaque AWP apparaît bien dans au moins une version (FR ou EN). Les doublons concept/version DOI sont normaux et non problématiques.")
w()

w("---")
w("*Fin du rapport.*")

with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(out))
