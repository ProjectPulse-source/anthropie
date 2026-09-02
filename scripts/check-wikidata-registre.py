#!/usr/bin/env python3
"""Parite Wikidata <-> registre canonique (data/works.yaml), dans les DEUX sens.

MOTIF (2026-09-02). La verification de l'item auteur Q138909233 a montre 19 items
Wikidata portant P50 -> auteur quand le registre n'en connaissait que 9 : les 8 AWP
(crees en mai et juillet), la serie, et l'item d'une recension (cree le 15/08) n'ont
jamais ete ecrits en retour. Le README de Wikidata/ le disait : « le premier maillon
-- Wikidata -> registre -- n'est couvert par aucun controle ». Un diff des QID cites
dans les fichiers du dossier avait ete ecarte (61 faux positifs sur 70). Ce script
prend l'autre chemin, celui qui a trouve les 10 trous sans un seul faux positif :
interroger Wikidata depuis le NOEUD AUTEUR (« quelles oeuvres pointent vers lui ? »)
et comparer a l'ensemble des QID declares au registre. Il relit la source sans
filtre (le registre n'entre jamais dans la requete), et rend compte des deux sens :

  · sur Wikidata, absent du registre  -> ecriture en retour a faire ;
  · au registre, mais sur Wikidata : inexistant, redirige (fusion) ou sans P50 vers
    l'auteur                          -> le registre a tort, ou l'item a bouge.

Perimetre des QID du registre : toute valeur `wikidata*` d'une entree de `works`
(y compris `english_edition.wikidata`, `wikidata_review`) et `author.wikidata_series`.
Exclus, et dits : `author.wikidata_person` (c'est le noeud interroge) et
`author.wikidata_concept` (un concept n'a pas d'auteur au sens de P50).

Quand le lancer : a chaque cloture d'un dossier Wikidata/Import_* (le bloc ✅ cite sa
sortie), dans les checklists d'ajout (AWP, publication, livre), et a la demande.

Sortie 0 = parite ; 1 = au moins un ecart ; 2 = Wikidata injoignable (rien conclu).
Options : --registre <chemin> (defaut data/works.yaml) -- sert au temoin par mutation.
"""
from __future__ import annotations

import argparse
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

ROOT = Path(__file__).resolve().parent.parent
API = "https://www.wikidata.org/w/api.php"
UA = "anthropie-site-navette/1.0 (https://stephane-lalut.com; check-wikidata-registre)"
QID = re.compile(r"^Q\d+$")

# Python 3.11 sous Windows ne lit pas le magasin systeme : sans certifi, wikidata.org
# echoue en CERTIFICATE_VERIFY_FAILED (constate le 2026-09-02) alors que curl passe.
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:  # pragma: no cover
    SSL_CTX = ssl.create_default_context()


def api(params: dict) -> dict:
    params = dict(params, format="json")
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
        return json.load(r)


def items_pointant_vers(auteur: str) -> set[str]:
    """Tous les items dont P50 = auteur (recherche paginee, sans filtre)."""
    found: set[str] = set()
    offset = 0
    while True:
        r = api({"action": "query", "list": "search", "srsearch": f"haswbstatement:P50={auteur}",
                 "srlimit": 50, "sroffset": offset})
        found |= {x["title"] for x in r["query"]["search"]}
        if "continue" not in r:
            return found
        offset = r["continue"]["sroffset"]


def qids_du_registre(reg: dict) -> dict[str, str]:
    """QID -> etiquette (id d'oeuvre + cle), pour toute cle wikidata* des oeuvres et la serie."""
    out: dict[str, str] = {}

    def walk(node, etiquette: str) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(k, str) and k.startswith("wikidata") and isinstance(v, str) and QID.match(v):
                    out[v] = f"{etiquette}.{k}"
                else:
                    walk(v, etiquette)
        elif isinstance(node, list):
            for v in node:
                walk(v, etiquette)

    for w in reg.get("works", []):
        walk(w, w.get("id", "?"))
    serie = (reg.get("author") or {}).get("wikidata_series")
    if isinstance(serie, str) and QID.match(serie):
        out[serie] = "author.wikidata_series"
    return out


def etat_des_qids(qids: list[str], auteur: str) -> dict[str, str]:
    """Pour chaque QID : 'ok' | 'inexistant' | 'redirige -> Qx' | 'sans P50 vers auteur'."""
    etat: dict[str, str] = {}
    for i in range(0, len(qids), 50):
        lot = qids[i:i + 50]
        r = api({"action": "wbgetentities", "ids": "|".join(lot), "props": "claims|info", "redirects": "yes"})
        for q in lot:
            e = r["entities"].get(q)
            if e is None or "missing" in e:
                etat[q] = "inexistant"
                continue
            if e.get("id") != q:
                etat[q] = f"redirige -> {e.get('id')} (fusion : mettre le registre a jour)"
                continue
            auteurs = {c["mainsnak"].get("datavalue", {}).get("value", {}).get("id")
                       for c in e.get("claims", {}).get("P50", [])}
            etat[q] = "ok" if auteur in auteurs else "sans P50 vers l'auteur"
    return etat


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--registre", default=str(ROOT / "data" / "works.yaml"))
    args = ap.parse_args()

    reg = yaml.safe_load(Path(args.registre).read_text(encoding="utf-8"))
    auteur = (reg.get("author") or {}).get("wikidata_person")
    if not auteur:
        print("author.wikidata_person absent du registre : rien a interroger")
        return 2
    declares = qids_du_registre(reg)

    try:
        sur_wikidata = items_pointant_vers(auteur)
        etat = etat_des_qids(sorted(declares), auteur)
    except Exception as exc:  # reseau, API : on ne conclut RIEN
        print(f"Wikidata injoignable ({exc.__class__.__name__}: {exc}) -- aucune conclusion")
        return 2

    manquants = sorted(sur_wikidata - set(declares))
    defaillants = {q: s for q, s in etat.items() if s != "ok"}
    print(f"Wikidata : {len(sur_wikidata)} item(s) avec P50 -> {auteur} | registre : {len(declares)} QID declare(s)")
    print("Exclus, et dits : author.wikidata_person (le noeud interroge), author.wikidata_concept (pas de P50).")
    if not manquants and not defaillants:
        print("\nParite Wikidata <-> registre. OK")
        return 0
    print()
    for q in manquants:
        print(f"  ECART  {q} : P50 -> auteur sur Wikidata, ABSENT du registre (ecriture en retour a faire)")
    for q, s in sorted(defaillants.items()):
        print(f"  ECART  {q} ({declares[q]}) : {s}")
    print(f"\n{len(manquants) + len(defaillants)} ecart(s). Corriger le registre (ou la fiche via check-fiches-registre).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
