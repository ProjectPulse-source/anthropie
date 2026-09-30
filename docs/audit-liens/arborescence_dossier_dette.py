# Arborescence du dossier dette, lue dans le site construit : pages FR/EN, titres, langue, alternates,
# liens sortants vers le dossier, les prolongements, l'index des ressources et le livre.
import sys, os, re, html, json
B, AUDIT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
DOSSIER = [
    ("1. Pourquoi elle augmente", "/pourquoi-la-dette-publique-augmente/", "/en/why-does-public-debt-rise/"),
    ("2. Combien coûte", "/cout-de-la-dette-publique/", "/en/cost-of-french-public-debt/"),
    ("3. Qui paie", "/qui-paie-la-dette-publique/", "/en/who-really-pays-public-debt/"),
    ("4. Et ailleurs", "/dette-publique-comparaison-internationale/", "/en/public-debt-international-comparison/"),
]
PROLONG = ["/dette-publique-collectivites-locales/", "/dette-publique-generations-futures/"]
INDEX = ["/ressources/", "/en/resources/"]
LIVRE = "/livres/dette-publique-qui-paie-vraiment/"


def f(url):
    return os.path.join(B, url.lstrip("/"), "index.html")


def lire(url):
    p = f(url)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def meta(url):
    t = lire(url)
    if t is None:
        return dict(existe=False)
    g = lambda rx: (re.search(rx, t, re.S).group(1) if re.search(rx, t, re.S) else "")
    alt = dict(re.findall(r'<link rel="?alternate"? hreflang="?([a-z-]+)"? href="?([^"\s>]+)', t))
    return dict(existe=True, lang=g(r'<html[^>]*lang="?([a-z]+)'), titre=html.unescape(g(r"<title>(.*?)</title>")).split(" — ")[0],
                og=g(r'og:image"? content="?([^"\s>]+)').replace("https://stephane-lalut.com", ""),
                alt={k: v.replace("https://stephane-lalut.com", "") for k, v in alt.items()},
                canon=g(r'rel="?canonical"? href="?([^"\s>]+)').replace("https://stephane-lalut.com", ""))


def liens(url):
    t = lire(url) or ""
    out = []
    for m in re.finditer(r'<a\b[^>]*?href="?([^"\s>]+)"?([^>]*)>(.*?)</a>', t, re.S):
        h = m.group(1).replace("https://stephane-lalut.com", "")
        if h.startswith("/"):
            out.append((h.split("#")[0], "hreflang" in m.group(2) or "hreflang" in m.group(0), " ".join(html.unescape(re.sub("<[^>]+>", " ", m.group(3))).split())[:50]))
    return out


a = json.load(open(AUDIT, encoding="utf-8"))
L = []
w = L.append
w("# Arborescence et liens du dossier dette publique — FR / EN")
w("")
w("Généré le 30/09/2026 depuis le site **construit localement** (`hugo --minify`, commit de travail postérieur à "
  "`77898a7`), non depuis le site en ligne. Script et audit : voir « Méthode ».")
w("")
w("## 1. Les pages et leurs paires de langue")
w("")
w("| Volet | Page FR | Titre FR | Page EN | Titre EN | alternate FR→EN | alternate EN→FR | carte FR | carte EN |")
w("|---|---|---|---|---|---|---|---|---|")
for nom, fr, en in DOSSIER:
    mf, me = meta(fr), meta(en)
    w("| %s | `%s` | %s | `%s` | %s | %s | %s | `%s` | `%s` |" % (
        nom, fr, mf.get("titre", "ABSENTE"), en, me.get("titre", "ABSENTE"),
        "✅" if mf.get("alt", {}).get("en") == en else "❌ " + str(mf.get("alt", {}).get("en")),
        "✅" if me.get("alt", {}).get("fr") == fr else "❌ " + str(me.get("alt", {}).get("fr")),
        mf.get("og", "—"), me.get("og", "—")))
w("")
w("## 2. Barre d'onglets et liens entre volets (chaque page → les trois autres)")
w("")
w("| Page | → volet 1 | → volet 2 | → volet 3 | → volet 4 | même langue ? |")
w("|---|---|---|---|---|---|")
for nom, fr, en in DOSSIER:
    for src, lang in ((fr, "fr"), (en, "en")):
        cibles = {h for h, _m, _t in liens(src)}
        cells, ok = [], True
        for nom2, fr2, en2 in DOSSIER:
            if (fr2, en2) == (fr, en):
                cells.append("(page)")
                continue
            attendu = en2 if lang == "en" else fr2
            autre = fr2 if lang == "en" else en2
            if attendu in cibles:
                cells.append("✅ " + attendu)
            elif autre in cibles:
                cells.append("❌ autre langue " + autre); ok = False
            else:
                cells.append("❌ absent"); ok = False
        w("| `%s` | %s | %s |" % (src, " | ".join(cells), "✅" if ok else "❌"))
w("")
w("## 3. Prolongements, livre, index des ressources")
w("")
w("| Page | Prolongements (collectivités, générations) | Livre | Index des ressources de la même langue |")
w("|---|---|---|---|")
for nom, fr, en in DOSSIER:
    for src, lang in ((fr, "fr"), (en, "en")):
        ls = liens(src)
        pro = [("%s%s" % (h, " (hreflang)" if mk else "")) for h, mk, _t in ls if h in PROLONG]
        liv = sorted({("hreflang" if mk else "sans hreflang") for h, mk, _t in ls if h == LIVRE})
        idx = INDEX[1] if lang == "en" else INDEX[0]
        w("| `%s` | %s | %s | %s |" % (src, ", ".join(sorted(set(pro))) or "—", ", ".join(liv) or "—",
                                      "✅" if idx in {h for h, _m, _t in ls} else "— (menu du site seulement)"))
w("")
w("### Index des ressources : entrées du dossier dette")
w("")
for idx in INDEX:
    ls = [(h, t) for h, _m, t in liens(idx) if any(h in (fr, en) for _n, fr, en in DOSSIER)]
    w("- `%s` :" % idx)
    for h, t in ls:
        lg = meta(h).get("lang", "?")
        attendu = "en" if idx.startswith("/en/") else "fr"
        w("  - %s `%s` — %s %s" % ("✅" if lg == attendu else "❌", h, t, "" if lg == attendu else "(page %s)" % lg))
w("")
w("## 4. Audit de tous les liens du site construit")
w("")
w("- Pages lues : **%d**." % a["pages"])
w("- Liens internes cassés (page ou fichier absent) : **%d**." % len(a["casses"]))
w("- Ancres absentes dans la page cible : **%d**." % len(a["ancres"]))
w("- Alternates de langue non réciproques ou vers une page absente : **%d**." % len(a["alternates"]))
en_fr = [x for x in a["langue"] if x["src_lang"] == "en" and x["cible_lang"] == "fr" and not x["hreflang_marque"]]
cat = {}
for x in en_fr:
    k = ("dossier dette" if x["src"] in {u for _n, fr, en in DOSSIER for u in (fr, en)}
         else "fiches des livres (français seulement)" if x["cible"].startswith("/livres/")
         else "sélecteurs « FR » des AWP anglais" if x["cible"].startswith("/awp/")
         else "autre")
    cat.setdefault(k, []).append(x)
w("- Liens d'une page anglaise vers une page française **sans `hreflang`** : **%d**, répartis ainsi :" % len(en_fr))
for k, v in sorted(cat.items()):
    w("  - %s : **%d**%s" % (k, len(v), "" if k != "dossier dette" else " — " + " ; ".join(
        "`%s` → `%s` (« %s »)" % (x["src"], x["cible"], x["texte"][:45]) for x in v)))
w("")
open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ecrit", OUT, len(L), "lignes")
