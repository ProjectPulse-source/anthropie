#!/usr/bin/env python3
"""Contrôle du site CONSTRUIT : chaque ressource dit la même date dans ses trois canaux.

MOTIF (2026-10-16, arbitrage PRO-20261016-174136, phase P1). Avant, une même page portait jusqu'à trois dates
différentes (sitemap au 11/10, Dataset au 07/10, texte « relevées le 7 octobre ») sans qu'aucune règle dise laquelle
valait pour la page. Les trois canaux lisent désormais une source unique (partials/page-date.html) ; ce contrôle relit
le HTML et le sitemap SERVIS, sans passer par cette source, pour qu'une date recopiée en dur un jour se voie.

Pour chaque page qui porte le balisage de page (`"@id": "<url>#page"`) :
    sitemap <lastmod>  ==  dateModified du balisage de page  ==  <time datetime> de la ligne « Page … le »
    (la ligne dit « publiée » quand la page n'a pas changé : on compare alors datePublished, égal à dateModified).
Entré == conformes + en défaut ; une page à balisage sans ligne visible ou absente du sitemap est un défaut nommé.

Second volet (P1-F) : un BLOC citable d'une page de données (chapô, « résultat en une phrase », réponse de FAQ) qui
porte un chiffre doit porter aussi une période (année, trimestre, mois, session). Un moteur cite un passage, pas une
page : un pourcentage sans son année y devient faux dès la mise à jour suivante. Mesuré le 16/10/2026 : 7 blocs sur
117 en défaut, tous réels ; au grain de la phrase, 45 signalements dont la plupart prolongeaient une phrase datée,
d'où le grain du bloc.

Usage : python scripts/check-dates-build.py [public]   ·   --temoin : mute une date dans une copie et exige l'échec.
"""
import html
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

HOTE = "https://stephane-lalut.com"


def sitemap(build: Path) -> dict:
    out = {}
    for f in [build / "sitemap.xml", build / "fr" / "sitemap.xml", build / "en" / "sitemap.xml"]:
        if f.exists():
            for loc, lm in re.findall(r"<loc>(.*?)</loc>\s*(?:<lastmod>(.*?)</lastmod>)?", f.read_text(encoding="utf-8")):
                out[loc] = (lm or "")[:10] or None
    return out


def noeud_page(html: str):
    for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = json.loads(bloc)
        except ValueError:
            continue
        if isinstance(d, dict) and str(d.get("@id", "")).endswith("#page"):
            return d
    return None


def verifier(build: Path, muter=None) -> tuple:
    sm = sitemap(build)
    vues, fautes = 0, []
    for f in sorted(build.rglob("index.html")):
        html = f.read_text(encoding="utf-8")
        if muter:
            html = muter(f, html)
        n = noeud_page(html)
        if not n:
            continue
        vues += 1
        url, mod, pub = n.get("url"), n.get("dateModified"), n.get("datePublished")
        m = re.search(r'<p class="page-header__date">(Page [^<]*?)<time datetime="(\d{4}-\d{2}-\d{2})"', html)
        if not m:
            fautes.append((url, "balisage de page sans ligne de date visible"))
            continue
        libelle, visible = m.group(1), m.group(2)
        publiee = "publiée" in libelle or "published" in libelle
        attendu_visible = pub if publiee else mod
        lm = sm.get(url)
        ecarts = []
        if lm is None:
            ecarts.append("absente du sitemap ou sans lastmod")
        elif lm != mod:
            ecarts.append(f"sitemap {lm} != dateModified {mod}")
        if visible != attendu_visible:
            ecarts.append(f"ligne visible {visible} != {'datePublished' if publiee else 'dateModified'} {attendu_visible}")
        if pub and mod and pub > mod:
            ecarts.append(f"datePublished {pub} postérieure à dateModified {mod}")
        if publiee and pub != mod:
            ecarts.append(f"« publiée » alors que dateModified {mod} != datePublished {pub}")
        if ecarts:
            fautes.append((url, " ; ".join(ecarts)))
    return vues, fautes


MOIS = ("janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre|January|February|March|"
        "April|May|June|July|August|September|October|November|December")
PERIODE = re.compile(rf"\b(1[89]\d\d|20\d\d)\b|\bT[1-4]\b|\bQ[1-4]\b|({MOIS})|\bsession\b", re.I)
CHIFFRE = re.compile(r"\d[\d\u00a0\u202f,.]*\s?(%|€|euros?|milliards?|millions?|billion|points?|élèves|candidats|jours|"
                     r"pays|countries|fois|times)|\b\d+[,.]\d+\b", re.I)


def texte(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def blocs_sans_periode(build: Path, muter=None) -> tuple:
    vus, fautes = 0, []
    for f in sorted(build.rglob("index.html")):
        h = f.read_text(encoding="utf-8")
        if '#dataset"' not in h:
            continue
        if muter:
            h = muter(f, h)
        url = "/" + f.parent.relative_to(build).as_posix() + "/"
        blocs = []
        m = re.search(r'<p class="page-header__lede">(.*?)</p>', h, re.S)
        if m:
            blocs.append(("chapô", texte(m.group(1))))
        blocs += [("résultat", texte(x)) for x in re.findall(r'<div class="resultat-phrase"[^>]*>(.*?)</div>', h, re.S)]
        for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                d = json.loads(b)
            except ValueError:
                continue
            if isinstance(d, dict) and d.get("@type") == "FAQPage":
                blocs += [("FAQ", q["acceptedAnswer"]["text"]) for q in d.get("mainEntity", [])]
        for genre, t in blocs:
            if CHIFFRE.search(t):
                vus += 1
                if not PERIODE.search(t):
                    fautes.append((url, f"{genre} chiffré sans période : « {t[:120]}… »"))
    return vus, fautes


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build = Path(args[0] if args else "public")
    if "--temoin" in sys.argv:
        cible = {"fait": False}

        def muter(f, html):
            if not cible["fait"] and 'class="page-header__date"' in html:
                cible["fait"] = True
                return re.sub(r'(<p class="page-header__date">[^<]*<time datetime=")\d{4}', r"\g<1>1999", html, count=1)
            return html
        _, fautes = verifier(build, muter)
        ok1 = cible["fait"] and fautes
        print("TÉMOIN 1 " + ("OK : une date visible mutée est signalée." if ok1 else "EN ÉCHEC : la date mutée n'a pas été vue."))
        cible2 = {"fait": False}

        def muter2(f, html_):
            if not cible2["fait"] and 'class="page-header__lede"' in html_:
                cible2["fait"] = True
                return re.sub(r'<p class="page-header__lede">.*?</p>',
                              '<p class="page-header__lede">La charge atteint 8,9 % des recettes.</p>', html_, count=1, flags=re.S)
            return html_
        _, f2 = blocs_sans_periode(build, muter2)
        ok2 = cible2["fait"] and any("chapô" in m for _, m in f2)
        print("TÉMOIN 2 " + ("OK : un chapô chiffré sans période est signalé." if ok2 else "EN ÉCHEC : le chapô sans période n'a pas été vu."))
        return 0 if (ok1 and ok2) else 1

    vues, fautes = verifier(build)
    if vues < 20:
        print(f"ERREUR : {vues} page(s) à balisage de page seulement : build incomplet ou balisage disparu")
        return 1
    print(f"Dates des ressources : {vues} page(s) ; concordantes : {vues - len(fautes)} ; en défaut : {len(fautes)}")
    nb, fp = blocs_sans_periode(build)
    print(f"Période des blocs citables : {nb} bloc(s) chiffré(s) ; sans période : {len(fp)}")
    for url, motif in fautes + fp:
        print(f"  DÉFAUT {url} : {motif}")
    return 1 if (fautes or fp) else 0


if __name__ == "__main__":
    sys.exit(main())
