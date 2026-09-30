# Audit des liens du site construit (hugo --minify -d BUILD, baseURL de production).
# Pour chaque page HTML : liens internes -> cible existante ? ancre existante ? langue de la cible ?
# Sortie JSON pour le rapport. Aucun reseau : seul le build local est lu.
import json, os, re, sys, html
from urllib.parse import urlparse, unquote

BUILD = sys.argv[1]
OUT = sys.argv[2]
BASE = "https://stephane-lalut.com"

pages = {}
for root, _d, files in os.walk(BUILD):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = "/" + os.path.relpath(p, BUILD).replace("\\", "/")
            url = rel[:-len("index.html")] if rel.endswith("/index.html") else rel
            pages[url] = p

def lire(p):
    return open(p, encoding="utf-8", errors="replace").read()

cache = {}
def infos(url):
    if url not in cache:
        t = lire(pages[url])
        m = re.search(r'<html[^>]*\blang="?([a-zA-Z-]+)', t)
        ids = set(re.findall(r'\bid="?([^"\s>]+)', t))
        titre = re.search(r"<title>(.*?)</title>", t, re.S)
        alt = re.findall(r'<link rel="?alternate"? hreflang="?([a-z-]+)"? href="?([^"\s>]+)', t)
        cache[url] = dict(lang=(m.group(1).lower()[:2] if m else "?"), ids=ids,
                          titre=html.unescape(titre.group(1).strip()) if titre else "", alt=alt)
    return cache[url]

def normaliser(href, src):
    href = html.unescape(href)
    if href.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    u = urlparse(href)
    if u.scheme and u.netloc and u.netloc not in ("stephane-lalut.com", "www.stephane-lalut.com"):
        return None
    path = unquote(u.path) if (u.path or u.netloc) else src
    if not path.startswith("/"):
        base = src if src.endswith("/") else src.rsplit("/", 1)[0] + "/"
        path = os.path.normpath(base + path).replace("\\", "/") + ("/" if path.endswith("/") else "")
    return path, u.fragment

res = {"pages": len(pages), "casses": [], "ancres": [], "langue": [], "alternates": []}
for src, p in sorted(pages.items()):
    t = lire(p)
    src_lang = infos(src)["lang"]
    for m in re.finditer(r'<a\b[^>]*?\bhref="?([^"\s>]+)"?([^>]*)>(.*?)</a>', t, re.S):
        href, reste, texte = m.group(1), m.group(0), html.unescape(re.sub("<[^>]+>", " ", m.group(3))).strip()
        n = normaliser(href, src)
        if not n:
            continue
        path, frag = n
        if re.search(r"\.(jpg|png|svg|pdf|json|csv|xml|txt|bib|ris|enw|webp|ico|js|css|mp3|zip)$", path, re.I):
            f = os.path.join(BUILD, path.lstrip("/"))
            if not os.path.exists(f):
                res["casses"].append(dict(src=src, href=href, texte=texte[:60], motif="fichier absent"))
            continue
        cible = path if path.endswith("/") or path in pages else path + "/"
        if cible not in pages:
            res["casses"].append(dict(src=src, href=href, texte=texte[:60], motif="page absente du build"))
            continue
        if frag and frag not in infos(cible)["ids"]:
            res["ancres"].append(dict(src=src, href=href, texte=texte[:60]))
        cl = infos(cible)["lang"]
        if src_lang != cl:
            marque = 'hreflang' in reste
            res["langue"].append(dict(src=src, src_lang=src_lang, cible=cible, cible_lang=cl, texte=texte[:70],
                                      hreflang_marque=marque))
    # réciprocité des alternates
    for lg, h in infos(src)["alt"]:
        if lg == "x-default":
            continue
        n = normaliser(h, src)
        if not n:
            continue
        c = n[0]
        if c not in pages:
            res["alternates"].append(dict(src=src, lang=lg, cible=c, motif="cible absente"))
        elif c != src and not any(normaliser(h2, c) and normaliser(h2, c)[0] == src for _l, h2 in infos(c)["alt"]):
            res["alternates"].append(dict(src=src, lang=lg, cible=c, motif="non réciproque"))

json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("pages", len(pages), "| casses", len(res["casses"]), "| ancres", len(res["ancres"]),
      "| changements de langue", len(res["langue"]), "| alternates", len(res["alternates"]))
