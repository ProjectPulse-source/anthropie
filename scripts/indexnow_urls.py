#!/usr/bin/env python3
"""Choisit les URL a notifier a IndexNow : celles dont le `lastmod` du sitemap a change.

MOTIF (2026-10-16, arbitrage PRO-20261016-174136). Le workflow soumettait TOUTES les URL du sitemap a chaque
push touchant le contenu, puis chaque lundi. La FAQ d'IndexNow range exactement cela parmi les erreurs :
« Submit only when content has changed. Do not resubmit unchanged URLs. » Le `lastmod` du sitemap ne bouge
que sur une modification reelle (texte revise, ou `releve_le` d'un jeu de donnees reecrit parce qu'un chiffre
a change) : c'est donc lui, et lui seul, qui dit ce qui a change.

REGLE
    retenue  : `lastmod` (au jour pres) >= --depuis
    ecartee  : motif « lastmod anterieur » ou « sans lastmod » (pages sans date : glossaire, index, contact)
    --tout   : toutes les URL (refonte du site entier, seul cas ou IndexNow l'admet)
    entre == retenues + ecartees, verifie avant d'ecrire.

`--depuis` est la date de la derniere execution reussie du workflow MOINS UN JOUR (calcule par le workflow).
Le jour de marge couvre le cas ou le sitemap lu par l'execution precedente n'etait pas encore deploye ; le
prix est qu'une URL modifiee peut etre notifiee deux fois en deux jours, ce qui reste une modification reelle.

Usage : python scripts/indexnow_urls.py (--depuis AAAA-MM-JJ | --tout) [--sitemap URL|fichier] [--sortie urls.json]
Sortie 0 meme si rien n'est retenu (le workflow n'envoie alors rien) ; 1 si le sitemap est illisible ou anormal.
"""
import argparse
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

HOTE = "stephane-lalut.com"
URL_RE = re.compile(r"<url>(.*?)</url>", re.S)
LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")
LASTMOD_RE = re.compile(r"<lastmod>\s*(\d{4}-\d{2}-\d{2})")


def lire(source: str) -> str:
    if source.startswith("http"):
        req = urllib.request.Request(source, headers={"User-Agent": "indexnow-workflow"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8")
    return Path(source).read_text(encoding="utf-8")


def entrees(source: str) -> dict:
    """{url: lastmod ou None}. Suit un <sitemapindex> (IndexNow n'expanse pas les sitemaps)."""
    xml = lire(source)
    if "<sitemapindex" in xml:
        out = {}
        for sous in LOC_RE.findall(xml):
            out.update(entrees(sous))
        return out
    out = {}
    for bloc in URL_RE.findall(xml):
        loc = LOC_RE.search(bloc)
        if not loc:
            continue
        u = loc.group(1)
        if HOTE not in u or u.endswith(".xml"):
            continue
        lm = LASTMOD_RE.search(bloc)
        d = lm.group(1) if lm else None
        # une URL peut figurer dans deux sitemaps de langue : on garde la date la plus recente
        if u not in out or (d and (out[u] is None or d > out[u])):
            out[u] = d
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--depuis", type=date.fromisoformat)
    g.add_argument("--tout", action="store_true")
    ap.add_argument("--sitemap", default=f"https://{HOTE}/sitemap.xml")
    ap.add_argument("--sortie", default="urls.json")
    a = ap.parse_args()

    tout = entrees(a.sitemap)
    # Garde anti-echec silencieux : le site compte plusieurs dizaines de pages.
    if len(tout) < 10:
        print(f"::error::Seulement {len(tout)} URL lues dans le sitemap : regression probable de l'extraction")
        return 1

    retenues, ecartees = [], []
    for u, d in sorted(tout.items()):
        if a.tout:
            retenues.append(u)
        elif d is None:
            ecartees.append((u, "sans lastmod"))
        elif date.fromisoformat(d) >= a.depuis:
            retenues.append(u)
        else:
            ecartees.append((u, "lastmod anterieur"))

    if len(tout) != len(retenues) + len(ecartees):
        print("::error::Compte faux : entre != retenues + ecartees")
        return 1

    motifs = {}
    for _, m in ecartees:
        motifs[m] = motifs.get(m, 0) + 1
    print(f"Sitemap : {len(tout)} URL ; retenues : {len(retenues)} ; ecartees : {len(ecartees)} {motifs}")
    print(f"Critere : {'toutes (--tout)' if a.tout else 'lastmod >= ' + a.depuis.isoformat()}")
    for u in retenues:
        print(f"  + {u} ({tout[u]})")
    for u, m in ecartees:
        if m == "sans lastmod":
            print(f"  . {u} (sans lastmod)")

    Path(a.sortie).write_text(json.dumps(retenues, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
