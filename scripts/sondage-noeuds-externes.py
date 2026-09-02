#!/usr/bin/env python3
"""Sondage inverse des noeuds externes : ce qu'un noeud sait de l'auteur et que le registre ignore.

MOTIF (2026-09-02). Meme classe que check-wikidata-registre.py, sur les autres noeuds :
un noeud externe (Crossref, OpenLibrary) ou une surface du site connait une oeuvre
que data/works.yaml -- ou une liste manuelle -- ignore. Le premier sondage a trouve
le DOI Cairn de l'article Revue Projet (absent du registre et de la fiche) et 4 livres
sur 5 sans identifiant OpenLibrary au registre.

Ce script MESURE, il ne garde pas : lecture seule, aucune ecriture. On l'execute a la
cloture d'une navette ou d'un ajout d'oeuvre, et a la demande.

CONDITION DE MORT (R2, predicat verifiable) : deux executions consecutives a zero ecart,
espacees d'au moins un mois, et aucune nouvelle oeuvre entre les deux -> supprimer ce
fichier et sa ligne dans PROJECT_STATUS ; le controle Wikidata, lui, reste (il a un
declencheur permanent : chaque navette).

Hors perimetre, et dit : Zenodo (communaute -> registre) est couvert par
zenodo_audit_complet.py (jeton requis) ; ORCID et OpenAlex par audit_works.py ;
livres et AWP (registre -> fiche) par check-fiches-registre.py.

Sortie 0 = aucun ecart ; 1 = au moins un ecart ; 2 = un noeud injoignable (dit lequel).
"""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML requis : pip install pyyaml")
    sys.exit(2)

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:  # pragma: no cover
    SSL_CTX = ssl.create_default_context()

ROOT = Path(__file__).resolve().parent.parent
UA = "anthropie-site-navette/1.0 (https://stephane-lalut.com; sondage-noeuds-externes)"
AUTEUR_OL = "OL16378291A"


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40, context=SSL_CTX) as r:
        return json.load(r)


def front_matter(path: Path) -> dict:
    m = re.search(r"(?s)\A---\r?\n(.*?)\r?\n---", path.read_text(encoding="utf-8"))
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def main() -> int:
    reg = yaml.safe_load((ROOT / "data" / "works.yaml").read_text(encoding="utf-8"))
    works = reg["works"]
    ecarts: list[str] = []
    injoignables: list[str] = []

    # 1. Crossref, par auteur (prenom + nom : les homonymes « Lalut » sont ecartes, et dits)
    print("1. Crossref (auteur Stéphane Lalut) -> DOI d'articles au registre")
    reg_dois = {w["doi"].lower() for w in works if w.get("doi")}
    try:
        r = get("https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.author": "Stéphane Lalut", "rows": 50, "select": "DOI,title,container-title,author"}))
        homonymes = 0
        for it in r["message"]["items"]:
            auteurs = it.get("author", [])
            if not any((a.get("family") or "").lower() == "lalut" for a in auteurs):
                continue
            if not any((a.get("family") or "").lower() == "lalut" and (a.get("given") or "").startswith("St")
                       for a in auteurs):
                homonymes += 1
                continue
            doi = it["DOI"].lower()
            if doi.startswith("10.2139/ssrn.") or doi.startswith("10.31235/"):
                continue  # depots (SSRN, SocArXiv) : suivis dans works.yaml sous deposits, pas comme articles
            if doi not in reg_dois:
                ecarts.append(f"Crossref : {doi} « {(it.get('title') or [''])[0][:60]} » "
                              f"({(it.get('container-title') or ['?'])[0]}) ABSENT du registre")
        print(f"   {len(reg_dois)} DOI d'articles au registre ; {homonymes} homonyme(s) Crossref écarté(s) (autre prénom)")
    except Exception as exc:
        injoignables.append(f"Crossref ({exc.__class__.__name__})")

    # 2. OpenLibrary, par auteur -> bloc openlibrary.work des livres
    print("2. OpenLibrary (auteur OL16378291A) -> openlibrary.work des livres au registre")
    reg_ol = {w["openlibrary"]["work"] for w in works if isinstance(w.get("openlibrary"), dict) and w["openlibrary"].get("work")}
    try:
        r = get(f"https://openlibrary.org/authors/{AUTEUR_OL}/works.json?limit=50")
        entries = r.get("entries", [])
        ol_keys = {e["key"].split("/")[-1] for e in entries}
        for e in entries:
            key = e["key"].split("/")[-1]
            if key not in reg_ol:
                ecarts.append(f"OpenLibrary : {key} « {e.get('title', '')[:60]} » ABSENT du registre")
        for key in sorted(reg_ol - ol_keys):
            ecarts.append(f"OpenLibrary : {key} au registre mais ABSENT des œuvres de l'auteur (fusion ? redirection ?)")
        print(f"   {len(entries)} œuvre(s) OpenLibrary ; {len(reg_ol)} au registre")
    except Exception as exc:
        injoignables.append(f"OpenLibrary ({exc.__class__.__name__})")

    # 3. Site <-> registre (articles), deux sens
    print("3. content/publications <-> registre (articles publiés), deux sens")
    fiches = {}
    for p in sorted((ROOT / "content" / "publications").glob("*.md")):
        if p.name.startswith("_"):
            continue
        fiches[p.stem] = (front_matter(p).get("url_externe") or "").rstrip("/")
    reg_urls = {(w.get("url") or "").rstrip("/") for w in works if w.get("type") == "article" and w.get("url")}
    for slug, url in fiches.items():
        if url not in reg_urls:
            ecarts.append(f"Site : fiche {slug} sans entrée au registre ({url or 'url_externe vide'})")
    for w in works:
        if w.get("type") == "article" and w.get("status") == "published":
            u = (w.get("url") or "").rstrip("/")
            if u not in fiches.values():
                ecarts.append(f"Registre : article publié {w['id']} sans fiche ({u or 'url vide'})")
    print(f"   {len(fiches)} fiche(s)")

    # 4. Listes manuelles (presence ecrite a la main = absence silencieuse possible)
    print("4. Listes manuelles (intent_matrix, presse_objets FR/EN) <-> fiches")
    im = (ROOT / "data" / "intent_matrix.yaml").read_text(encoding="utf-8")
    inscrits = set(re.findall(r"^\s*- slug: (\S+)", im, re.M))
    for slug in fiches:
        if slug not in inscrits:
            ecarts.append(f"intent_matrix : inscription ABSENTE pour {slug}")
    for f in ("content/a-propos/_index.md", "content/a-propos/_index.en.md"):
        keys = set((front_matter(ROOT / f).get("presse_objets") or {}).keys())
        for slug in fiches:
            if slug not in keys:
                ecarts.append(f"{f} : presse_objets ABSENT pour {slug}")
        for k in sorted(keys - set(fiches)):
            ecarts.append(f"{f} : presse_objets ORPHELIN {k}")

    print()
    for e in ecarts:
        print(f"  ECART  {e}")
    for n in injoignables:
        print(f"  INJOIGNABLE  {n} — rien conclu pour ce nœud")
    if not ecarts and not injoignables:
        print("Aucun écart. OK")
        return 0
    if ecarts:
        print(f"\n{len(ecarts)} écart(s) : écrire en retour au registre (et en fiche), puis relancer.")
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
