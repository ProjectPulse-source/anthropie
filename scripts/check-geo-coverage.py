#!/usr/bin/env python3
"""check-geo-coverage.py — rapport de couverture de la nasse GEO (doctrine §6b).

Rend EXÉCUTABLE la checklist d'assurance de couverture :
  1. chaque AWP FR a-t-il une porte de découverte (lien entrant hors section /awp/) ?
  2. chaque livre a-t-il une porte hors catalogue (lien entrant hors /livres/) ?
  3. chaque maille (section racine avec FAQ) est-elle fraîche (lastmod), maillée
     vers un hub (lien sortant /awp/ ou /livres/) et dotée d'une FAQ ?
  4. chaque publication est-elle rattachée (champ related non vide) ?
  5. miroir EN : mêmes contrôles 1-3 sur le graphe /en/ EXISTANT (.en.md).
     Mesure ce qui existe, n'exige jamais de page EN nouvelle — l'asymétrie
     FR/EN est un choix éditorial (« adapter, pas traduire », intent_matrix).

Rapport informatif : exit 0 toujours — les absences ACTÉES vivent dans
NASSE_GEO_ETENDUE.md (hors dépôt), l'arbitrage reste humain.
Usage : python scripts/check-geo-coverage.py   (racine du repo ou scripts/)
"""

from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"

# Sections utilitaires : ni mailles ni cibles de couverture
UTILITY = {"contact", "glossaire", "serie-awp", "a-propos", "ressources-offertes",
           "offrir-un-livre-kindle", "offrir-un-livre-de-culture-generale"}

FRESHNESS_DAYS = 120  # au-delà : signal de fraîcheur (lastmod à revisiter)

LINK_RE = re.compile(r'\]\((/[^)\s#]+)|href="(/[^"#]+)')
FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.S)


def front_matter(text: str) -> str:
    m = FM_RE.match(text)
    return m.group(1) if m else ""


def fm_value(fm: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*\"?([^\"\n#]+)\"?\s*(#.*)?$", fm, re.M)
    return m.group(1).strip() if m else None


def parse_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def norm(url: str) -> str:
    return url.rstrip("/") + "/"


def main() -> int:
    pages = {}  # url -> {file, fm, body, faq, lastmod}
    # Sections racines FR
    for f in sorted(CONTENT.glob("*/_index.md")):
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        url = norm(fm_value(fm, "url") or f"/{f.parent.name}/")
        pages[url] = dict(file=f, fm=fm, body=text,
                          faq=bool(re.search(r"^faq:", fm, re.M)),
                          lastmod=parse_date(fm_value(fm, "lastmod") or fm_value(fm, "date")),
                          section=f.parent.name)
    # AWP FR + livres FR + publications
    awp, livres, pubs = {}, {}, {}
    for f in sorted((CONTENT / "awp").glob("awp-*.md")):
        if f.name.endswith(".en.md"):
            continue
        awp[norm(f"/awp/{f.stem}/")] = f
        pages[norm(f"/awp/{f.stem}/")] = dict(file=f, body=f.read_text(encoding="utf-8"))
    for f in sorted((CONTENT / "livres").glob("*.md")):
        if f.name.startswith("_") or f.name.endswith(".en.md"):
            continue
        livres[norm(f"/livres/{f.stem}/")] = f
        pages[norm(f"/livres/{f.stem}/")] = dict(file=f, body=f.read_text(encoding="utf-8"))
    for f in sorted((CONTENT / "publications").glob("*.md")):
        if f.name.startswith("_"):
            continue
        pubs[f.stem] = front_matter(f.read_text(encoding="utf-8"))

    # Graphe de liens entrants (depuis toutes les pages FR connues)
    inbound: dict[str, set[str]] = {}
    for src_url, page in pages.items():
        for m in LINK_RE.finditer(page["body"]):
            tgt = norm(m.group(1) or m.group(2))
            inbound.setdefault(tgt, set()).add(src_url)

    warn = 0
    print(f"Couverture GEO — {date.today().isoformat()} (doctrine nasse §6b)\n")

    print("[1] AWP -> porte de découverte (lien entrant hors /awp/)")
    for url in sorted(awp):
        srcs = {s for s in inbound.get(url, set()) if not s.startswith("/awp/")}
        if not srcs:
            warn += 1
            print(f"  WARN {url} : aucune porte hors section AWP")
        else:
            print(f"  ok   {url} <- {len(srcs)} porte(s)")

    print("\n[2] Livres -> porte hors catalogue (lien entrant hors /livres/)")
    for url in sorted(livres):
        srcs = {s for s in inbound.get(url, set()) if not s.startswith("/livres/")}
        if not srcs:
            warn += 1
            print(f"  WARN {url} : aucune porte hors /livres/")
        else:
            print(f"  ok   {url} <- {len(srcs)} porte(s)")

    print("\n[3] Mailles (sections racines à FAQ) : fraîcheur + maillage sortant")
    today = date.today()
    for url, p in sorted(pages.items()):
        if "section" not in p or p["section"] in UTILITY or p["section"] in ("awp", "livres", "publications"):
            continue
        if not p.get("faq"):
            continue
        age = (today - p["lastmod"]).days if p.get("lastmod") else None
        out_hub = bool(re.search(r"\((/awp/|/livres/)", p["body"]))
        flags = []
        if age is None or age > FRESHNESS_DAYS:
            flags.append(f"lastmod {age if age is not None else '?'} j")
        if not out_hub:
            flags.append("aucun lien sortant vers /awp/ ou /livres/")
        if flags:
            warn += 1
            print(f"  WARN {url} : " + " ; ".join(flags))
        else:
            print(f"  ok   {url} (lastmod {age} j)")

    print("\n[4] Publications : rattachement (champ related)")
    unattached = [slug for slug, fm in sorted(pubs.items())
                  if not re.search(r"^related:\s*\[.+\]|^related:\s*\n\s+-", fm, re.M)]
    if unattached:
        for slug in unattached:
            print(f"  INFO {slug} : related vide (matière non versée a un cluster ?)")
    else:
        print("  ok   toutes rattachées")

    warn += check_en_coverage(today)

    print(f"\nBilan : {warn} signal(aux). Les absences ACTÉES (avec leur raison) vivent dans NASSE_GEO_ETENDUE.md — comparer avant d'agir.")
    return 0


def check_en_coverage(today: date) -> int:
    """[5] Miroir EN des contrôles 1-3, restreint aux pages .en.md existantes."""
    pages = {}
    # Sections racines EN — URL = `url:` du front matter si présent, sinon /en/<section>/
    for f in sorted(CONTENT.glob("*/_index.en.md")):
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        url = norm(fm_value(fm, "url") or f"/en/{f.parent.name}/")
        pages[url] = dict(file=f, fm=fm, body=text,
                          faq=bool(re.search(r"^faq:", fm, re.M)),
                          lastmod=parse_date(fm_value(fm, "lastmod") or fm_value(fm, "date")),
                          section=f.parent.name)
    awp, livres = {}, {}
    for f in sorted((CONTENT / "awp").glob("awp-*.en.md")):
        slug = f.name[:-len(".en.md")]
        awp[norm(f"/en/awp/{slug}/")] = f
        pages[norm(f"/en/awp/{slug}/")] = dict(file=f, body=f.read_text(encoding="utf-8"))
    for f in sorted((CONTENT / "livres").glob("*.en.md")):
        if f.name.startswith("_"):
            continue
        slug = f.name[:-len(".en.md")]
        livres[norm(f"/en/livres/{slug}/")] = f
        pages[norm(f"/en/livres/{slug}/")] = dict(file=f, body=f.read_text(encoding="utf-8"))

    inbound: dict[str, set[str]] = {}
    for src_url, page in pages.items():
        for m in LINK_RE.finditer(page["body"]):
            tgt = norm(m.group(1) or m.group(2))
            inbound.setdefault(tgt, set()).add(src_url)

    warn = 0
    print("\n[5] Miroir EN (pages .en.md existantes — l'asymétrie FR/EN reste un choix acté)")
    for url in sorted(awp):
        srcs = {s for s in inbound.get(url, set()) if not s.startswith("/en/awp/")}
        if not srcs:
            warn += 1
            print(f"  WARN {url} : aucune porte EN hors section AWP")
        else:
            print(f"  ok   {url} <- {len(srcs)} porte(s)")
    for url in sorted(livres):
        srcs = {s for s in inbound.get(url, set()) if not s.startswith("/en/livres/")}
        if not srcs:
            warn += 1
            print(f"  WARN {url} : aucune porte EN hors /en/livres/")
        else:
            print(f"  ok   {url} <- {len(srcs)} porte(s)")
    for url, p in sorted(pages.items()):
        if "section" not in p or p["section"] in UTILITY or p["section"] in ("awp", "livres", "publications"):
            continue
        if not p.get("faq"):
            continue
        age = (today - p["lastmod"]).days if p.get("lastmod") else None
        out_hub = bool(re.search(r"\((/en/awp/|/en/livres/|/en/books/|/en/serie-awp/)", p["body"]))
        flags = []
        if age is None or age > FRESHNESS_DAYS:
            flags.append(f"lastmod {age if age is not None else '?'} j")
        if not out_hub:
            flags.append("aucun lien sortant vers un hub EN (/en/awp/, /en/livres/, /en/books/, /en/serie-awp/)")
        if flags:
            warn += 1
            print(f"  WARN {url} : " + " ; ".join(flags))
        else:
            print(f"  ok   {url} (lastmod {age} j)")
    return warn


if __name__ == "__main__":
    sys.exit(main())
