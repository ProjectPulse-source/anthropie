# -*- coding: utf-8 -*-
"""audit-liens-build.py -- liens, paires de langue et indexabilité du site CONSTRUIT (avant déploiement).

    python scripts/audit-liens-build.py [public] [--json sortie.json]

Lit toutes les pages HTML d'un build Hugo (par défaut ./public). BLOQUANT (sortie 1) sur les défauts CRITIQUES :
  - lien interne vers une page ou un fichier absent du build ; ancre absente de la page cible ;
  - page traduite dont les <link rel=alternate hreflang> ne sont pas absolus, ne s'auto-référencent pas, ou ne
    sont pas réciproques ;
  - canonical absent, relatif, ou pointant vers une autre page (une page EN ne se canonicalise jamais vers la FR) ;
  - og:url différent du canonical ; page noindex alors qu'elle est dans le sitemap ;
  - page traduite absente du sitemap.
SIGNALÉ sans bloquer (UX) : lien de contenu d'une page anglaise vers une page française sans mention visible
« French » dans le texte du lien ni juste après. NON COMPTÉ : l'attribut hreflang des liens <a>, simple
métadonnée consultative (arbitrage ENTRANTE_2026-09-30_Architecture_Dette-02, D : déclassé).

POURQUOI (même arbitrage, E : promouvoir, pas supprimer). Le 30/09/2026, les versions anglaises du dossier dette
étaient justes dans le build et absentes en production ; ce contrôle garde la topologie du build, son pendant
scripts/smoke-production.py vérifie la même topologie sur le site servi. Contrôle PERMANENT : il se justifie à
chaque revue annuelle par ce qu'il a arrêté (présomption inversée, R2).
"""
import html
import json
import os
import re
import sys
from urllib.parse import urlparse, unquote

BASE = "https://stephane-lalut.com"
args = [a for a in sys.argv[1:] if not a.startswith("--")]
BUILD = args[0] if args else "public"
OUT = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
FICHIER = re.compile(r"\.(jpg|jpeg|png|svg|pdf|json|csv|xml|txt|bib|ris|enw|webp|ico|js|css|mp3|zip|woff2?)$", re.I)
MENTION_FR = re.compile(r"\b(in French|French only|French edition|en français)\b", re.I)

if not os.path.isdir(BUILD):
    print("ECHEC : build introuvable (%s)" % BUILD)
    sys.exit(1)

pages = {}
for root, _d, files in os.walk(BUILD):
    for f in files:
        if f.endswith(".html"):
            rel = "/" + os.path.relpath(os.path.join(root, f), BUILD).replace("\\", "/")
            pages[rel[:-len("index.html")] if rel.endswith("/index.html") else rel] = os.path.join(root, f)

_c = {}


def lire(u):
    return open(pages[u], encoding="utf-8", errors="replace").read()


def infos(u):
    if u not in _c:
        t = lire(u)
        g = lambda rx: (re.search(rx, t, re.S).group(1) if re.search(rx, t, re.S) else "")
        _c[u] = dict(lang=g(r'<html[^>]*\blang="?([a-zA-Z-]+)').lower()[:2],
                     ids=set(re.findall(r'\bid="?([^"\s>]+)', t)),
                     alt=re.findall(r'<link rel="?alternate"? hreflang="?([a-zA-Z-]+)"? href="?([^"\s>]+)', t),
                     canon=g(r'<link rel="?canonical"? href="?([^"\s>]+)'),
                     ogurl=g(r'property="?og:url"? content="?([^"\s>]+)'),
                     noindex=bool(re.search(r'<meta name="?robots"? content="?[^">]*noindex', t)),
                     redirect=bool(re.search(r'http-equiv="?refresh', t, re.I)))
    return _c[u]


def chemin(href, src):
    u = urlparse(html.unescape(href))
    if u.scheme and u.netloc and u.netloc not in ("stephane-lalut.com", "www.stephane-lalut.com"):
        return None
    if href.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    p = unquote(u.path) if (u.path or u.netloc) else src
    if not p.startswith("/"):
        base = src if src.endswith("/") else src.rsplit("/", 1)[0] + "/"
        p = os.path.normpath(base + p).replace("\\", "/") + ("/" if p.endswith("/") else "")
    return p, u.fragment


def abs_vers_chemin(url):
    return url[len(BASE):] if url.startswith(BASE) else None


sitemap = set()
for sm in ("sitemap.xml", "en/sitemap.xml", "fr/sitemap.xml"):
    f = os.path.join(BUILD, sm)
    if os.path.exists(f):
        sitemap |= {abs_vers_chemin(u) for u in re.findall(r"<loc>([^<]+)</loc>", open(f, encoding="utf-8").read())}

R = dict(pages=len(pages), casses=[], ancres=[], alternates=[], canonical=[], indexabilite=[], langue=[], ux=[])
for src in sorted(pages):
    I = infos(src)
    if I["redirect"]:
        continue  # page d'alias (redirection) : pas de contenu propre
    t = lire(src)
    # -- liens
    for m in re.finditer(r'<a\b([^>]*?)\bhref="?([^"\s>]+)"?([^>]*)>(.*?)</a>(.{0,160})', t, re.S):
        href, attrs, texte = m.group(2), m.group(1) + m.group(3), m.group(4)
        apres = t[max(0, m.start() - 400):m.start()] + " " + m.group(5)  # étiquette avant ou après le lien
        n = chemin(href, src)
        if not n:
            continue
        p, frag = n
        if FICHIER.search(p):
            if not os.path.exists(os.path.join(BUILD, p.lstrip("/"))):
                R["casses"].append(dict(src=src, href=href, motif="fichier absent"))
            continue
        cible = p if (p.endswith("/") or p in pages) else p + "/"
        if cible not in pages:
            R["casses"].append(dict(src=src, href=href, motif="page absente du build"))
            continue
        if frag and frag not in infos(cible)["ids"]:
            R["ancres"].append(dict(src=src, href=href))
        cl = infos(cible)["lang"]
        txt = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", texte)).split())
        if I["lang"] != cl:
            R["langue"].append(dict(src=src, src_lang=I["lang"], cible=cible, cible_lang=cl, texte=txt[:70],
                                    hreflang_marque="hreflang" in attrs))
            est_selecteur = cible in [abs_vers_chemin(h) for _l, h in I["alt"]] or len(txt) <= 3 or re.search(r"version|this page|cette page|English|Français", txt, re.I)
            if I["lang"] == "en" and cl == "fr" and not est_selecteur:
                apres_txt = html.unescape(re.sub(r"<[^>]+>", " ", apres))
                if not (MENTION_FR.search(txt) or MENTION_FR.search(apres_txt)):
                    R["ux"].append(dict(src=src, cible=cible, texte=txt[:70]))
    # -- paires de langue
    if I["alt"]:
        chemins = {}
        for lg, h in I["alt"]:
            if not h.startswith(BASE + "/"):
                R["alternates"].append(dict(src=src, motif="alternate non absolu", href=h))
                continue
            chemins[lg.lower()] = abs_vers_chemin(h)
        if chemins.get(I["lang"]) != src:
            R["alternates"].append(dict(src=src, motif="pas d'auto-référence", lang=I["lang"]))
        for lg, c in chemins.items():
            if lg in ("x-default", I["lang"]):
                continue
            if c not in pages:
                R["alternates"].append(dict(src=src, motif="variante absente du build", cible=c))
            elif src not in [abs_vers_chemin(h) for _l, h in infos(c)["alt"]]:
                R["alternates"].append(dict(src=src, motif="non réciproque", cible=c))
            if src not in sitemap or c not in sitemap:
                R["indexabilite"].append(dict(src=src, motif="page traduite absente du sitemap", cible=c))
    # -- canonical, og:url, indexabilité
    if src.endswith("/") and src not in ("/404.html",):
        c = I["canon"]
        if not c:
            R["canonical"].append(dict(src=src, motif="canonical absent"))
        elif not c.startswith(BASE + "/"):
            R["canonical"].append(dict(src=src, motif="canonical non absolu", canon=c))
        elif abs_vers_chemin(c) != src:
            R["canonical"].append(dict(src=src, motif="canonical vers une autre page", canon=c))
        if I["ogurl"] and c and I["ogurl"] != c:
            R["canonical"].append(dict(src=src, motif="og:url différent du canonical", ogurl=I["ogurl"]))
        if I["noindex"] and src in sitemap:
            R["indexabilite"].append(dict(src=src, motif="noindex alors que la page est dans le sitemap"))

CRIT = ("casses", "ancres", "alternates", "canonical", "indexabilite")
n_crit = sum(len(R[k]) for k in CRIT)
if OUT:
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("audit-liens-build : %d pages ; critiques : %s ; UX (signale) : %d" % (
    len(pages), ", ".join("%s %d" % (k, len(R[k])) for k in CRIT), len(R["ux"])))
for k in CRIT:
    for x in R[k][:10]:
        print("  CRITIQUE [%s] %s" % (k, json.dumps(x, ensure_ascii=True)))
for x in R["ux"][:10]:
    print("  UX : %s -> %s (lien sans mention visible 'in French')" % (x["src"], x["cible"]))
sys.exit(1 if n_crit else 0)
