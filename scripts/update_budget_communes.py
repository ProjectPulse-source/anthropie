#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fiche par commune de /budget-2027-votre-commune/#fiche (option A de l'auteur, pièce 2024_Communes-04, 22/10/2026).

Lit à l'OFGL (data.ofgl.fr, base des communes, budget principal) six agrégats pour les deux derniers exercices publiés,
et écrit :
  static/budget2027-communes/index.json        [[insee, nom, département], ...] pour la recherche
  static/budget2027-communes/<dep>.json        une fiche par commune du département (valeurs mesurées, strate)
  static/budget_communes.csv                   le même contenu, une ligne par commune (UTF-8 avec BOM)
  static/budget_communes.json, data/budget_communes.json   méta : relevé, médianes par strate, sources, comptes

Règles de la fiche (conception : docs/conception/budget-2027-votre-commune.md, « Extension ») :
  - valeur absente = null (« non disponible » à l'écran), jamais zéro ; un zéro publié reste un zéro ;
  - commune seule : les budgets annexes et l'intercommunalité ne sont jamais additionnés à la commune ;
  - groupe de comparaison = strate de population de l'OFGL (tranche_population), bornes lues dans les données ;
  - aucun montant 2027 : les statuts des mesures viennent du registre des votes (data/dette_collectivites.json).

Seconde source, OFGL « dotations-communes » (données de la DGCL ; le site de la DGCL répondait 503 le 22/10/2026 et
les annexes des arrêtés sur Légifrance refusent un script : même donnée, autre canal) :
  - DILICO 2025 prélevé et reversement 2026 ; absente de la liste = non contributrice (0), absente du jeu = null ;
  - DGF notifiée 2026 et ses composantes ; dotation en faveur des communes nouvelles, montant distinct ;
  - rangs 2026 à la DSU et à la DSR cible, et exonération de l'article 37 du PLF 2027 qui s'en déduit (classement de
    l'année précédant la contribution, CGCT L. 2336-3, III), outre-mer compris ; seuil de 5 000 € quand le plafond
    arithmétique (3 % des recettes 2024) est déjà inférieur.

Gardes (arrêt sans rien écrire) :
  - conservation : communes lues == communes écrites + écartées (motif nommé) ;
  - témoin : dix communes tirées au sort relues par une SECONDE voie de l'API (records, sans filtre de budget), écart
    nul exigé sur la recette de fonctionnement du dernier exercice ;
  - plausibilité : au moins 30 000 communes au dernier exercice ; aucune recette de fonctionnement négative ;
  - dotations : DILICO 2025 des communes = 250 M€ (loi de finances pour 2025, art. 186) ; reversement 2026 = 30 % du
    prélèvement, commune par commune ; exactement 250, 30 et 2 500 communes sous les seuils de rang ; DGF 2026 = somme
    de ses composantes ; témoin de cinq communes relues par la voie « records ».

Usage : python scripts/update_budget_communes.py [--check] [--cache <dossier>]
  --cache : lit/écrit les exports OFGL dans ce dossier (relevé de session) au lieu de tout retélécharger.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import random
import re
import statistics
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import releve_jeu as rj  # noqa: E402  -- releve date par les seules donnees (organe commun, 17/10/2026)
OUT_DIR = ROOT / "static" / "budget2027-communes"
OUT_CSV = ROOT / "static" / "budget_communes.csv"
OUT_JSON = ROOT / "static" / "budget_communes.json"
OUT_DATA = ROOT / "data" / "budget_communes.json"
API = "https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-communes"
AGREGATS = {"rf": "Recettes de fonctionnement", "eb": "Epargne brute", "dette": "Encours de dette",
            "dgf": "Dotation globale de fonctionnement", "fctva": "FCTVA", "equip": "Dépenses d'équipement"}
MIN_COMMUNES = 30000
API_DOT = "https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes"
AN_DOT = 2026  # classement et DGF de l'annee precedant une contribution due en 2027 ; DILICO preleve en AN_DOT - 1
DOT = {"dil": (AN_DOT - 1, "Montant du prélèvement DILICO"), "rev": (AN_DOT, "Montant du reversement DILICO N-1"),
       "dgf": (AN_DOT, "Montant Dotation DGF"), "forf": (AN_DOT, "Montant Dotation forfaitaire"),
       "dsu": (AN_DOT, "Montant Dotation DSU"), "dsr": (AN_DOT, "Montant Dotation DSR"), "dnp": (AN_DOT, "Montant Dotation DNP"),
       "dacom": (AN_DOT, "Montant Dotation DACOM"), "dcn": (AN_DOT, "Montant Dotation Commune nouvelle"),
       "r_dsu10": (AN_DOT, "Rang de classement à la DSU des communes métropolitaines de plus de 10 000 hab."),
       "r_dsu5": (AN_DOT, "Rang de classement à la DSU des communes métropolitaines de 5 000 à 9 999 hab."),
       "r_dsrc": (AN_DOT, "Rang DSR Cible"), "i_dsrc": (AN_DOT, "Indice synthétique de la DSR cible")}
SEUILS = {"r_dsu10": 250, "r_dsu5": 30, "r_dsrc": 2500}  # CGCT L. 2336-3, III, repris par l'article 37 du PLF 2027
DILICO_COMMUNES_2025 = 250_000_000
# Qualification graduee (contre-expertise PRO-20261022-215525) : etablie par le texte et une donnee publiee ; possible
# quand l'annee du classement (DSR cible) ou l'assiette legale (seuil de 5 000 EUR) n'est pas demontree.
QUALIF = {"dom": "etablie_outre_mer", "r_dsu10": "etablie_dsu", "r_dsu5": "etablie_dsu", "r_dsrc": "possible_dsr_cible",
          "seuil": "possible_seuil_5000", None: "aucun_critere_etabli"}


def fail(m: str) -> None:
    print("ARRET : " + m)
    sys.exit(1)


def get(url: str, timeout: int = 300) -> bytes:
    for essai in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com"}),
                                          timeout=timeout).read()
        except Exception as e:  # reseau : reprise, puis arret
            print("  reprise (%s) %s" % (type(e).__name__, url[:90]))
            time.sleep(5 * (essai + 1))
    fail("OFGL injoignable : %s" % url[:120])


def derniers_exercices() -> list[int]:
    u = API + "/records?" + urllib.parse.urlencode({"select": "exer, count(*) as n", "group_by": "exer", "order_by": "exer desc", "limit": 3})
    ans = [int(r["exer"][:4]) for r in json.loads(get(u))["results"]]
    return sorted(ans[:2])  # brut-ok: annees d'exercice, entiers


def exporter(an: int, cle: str, cache: Path | None) -> list[dict]:
    f = cache / ("ofgl_%s_%d.csv" % (cle, an)) if cache else None
    if f and f.is_file() and f.stat().st_size > 1000:
        brut = f.read_bytes()
    else:
        w = 'year(exer)=%d and type_de_budget="Budget principal" and agregat="%s"' % (an, AGREGATS[cle])
        brut = get(API + "/exports/csv?" + urllib.parse.urlencode(
            {"where": w, "select": "insee,com_name,dep_code,epci_code,epci_name,tranche_population,ptot,montant", "delimiter": ";"}))
        if f:
            f.write_bytes(brut)
    return list(csv.DictReader(io.StringIO(brut.decode("utf-8-sig")), delimiter=";"))


def nombre(x: str):
    x = (x or "").strip()
    return None if x == "" else float(x)


def exporter_dot(cle: str, cache: Path | None) -> list[dict]:
    an, var = DOT[cle]
    f = cache / ("dot_%s_%d.csv" % (cle, an)) if cache else None
    if f and f.is_file() and f.stat().st_size > 100:
        brut = f.read_bytes()
    else:
        brut = get(API_DOT + "/exports/csv?" + urllib.parse.urlencode(
            {"where": 'year(exercice)=%d and variable="%s"' % (an, var), "select": "code_insee,met_om,valeur", "delimiter": ";"}))
        if f:
            f.write_bytes(brut)
    return list(csv.DictReader(io.StringIO(brut.decode("utf-8-sig")), delimiter=";"))


def dotations(cache: Path | None) -> dict[str, dict]:
    """Une entree par commune presente dans le jeu des dotations ; gardes en tete de fichier."""
    d: dict[str, dict] = {}
    for cle in DOT:
        for r in exporter_dot(cle, cache):
            e = d.setdefault(r["code_insee"], {"om": r["met_om"][:2]})
            e[cle] = nombre(r["valeur"])
    dil = {i: e["dil"] for i, e in d.items() if e.get("dil") is not None}
    if len(dil) < 1000 or abs(sum(dil.values()) - DILICO_COMMUNES_2025) > 1:
        fail("DILICO %d : %d communes, total %.2f (attendu %d)" % (AN_DOT - 1, len(dil), sum(dil.values()), DILICO_COMMUNES_2025))
    rev = {i: e["rev"] for i, e in d.items() if e.get("rev") is not None}
    if set(rev) != set(dil) or any(abs(rev[i] - 0.3 * dil[i]) > 1 for i in dil):
        fail("reversement DILICO %d different de 30 %% du prelevement %d" % (AN_DOT, AN_DOT - 1))
    for k, n in SEUILS.items():
        sous = [i for i, e in d.items() if e.get(k) is not None and e[k] <= n and (k != "r_dsrc" or e.get("i_dsrc") is not None)]
        if len(sous) != n:
            fail("%s : %d communes sous le rang %d (attendu %d)" % (k, len(sous), n, n))
    for i, e in d.items():
        comp = sum(e.get(k) or 0 for k in ("forf", "dsu", "dsr", "dnp", "dacom"))
        if e.get("dgf") is not None and abs(e["dgf"] - comp) > 1:
            fail("DGF %d de %s : %.0f, composantes %.0f" % (AN_DOT, i, e["dgf"], comp))
    # Temoin : seconde voie (records, une commune a la fois), cinq communes dont deux contributrices.
    rnd = random.Random(len(d))
    for i in rnd.sample(sorted(dil), 2) + rnd.sample(sorted(d), 3):  # brut-ok: tirage du temoin, ordre des codes Insee
        res = json.loads(get(API_DOT + "/records?" + urllib.parse.urlencode(
            {"where": 'code_insee="%s" and year(exercice)>=%d and variable in (%s)' % (i, AN_DOT - 1, ",".join('"%s"' % DOT[k][1] for k in ("dil", "rev", "dgf"))),
             "select": "exercice,variable,valeur", "limit": 100})))["results"]
        if len(res) >= 100:
            fail("temoin dotations : reponse tronquee pour %s" % i)
        lu = {(r["exercice"][:4], r["variable"]): r["valeur"] for r in res}
        for cle in ("dil", "rev", "dgf"):
            an, var = DOT[cle]
            a, b = lu.get((str(an), var)), d[i].get(cle)
            if (a is None) != (b is None) or (a is not None and abs(a - b) > 0.01):
                fail("temoin dotations : %s %s, seconde voie %s, export %s" % (i, cle, a, b))
    print("dotations : %d communes, DILICO %d : %d contributrices, %.0f EUR ; temoin 5 communes, 0 ecart"
          % (len(d), AN_DOT - 1, len(dil), sum(dil.values())))
    return d


ANNEXES = ROOT / "scripts" / "sources_budget_communes"
# Annexes officielles des arretes (Legifrance, documents administratifs), telechargees par le navigateur le 22/10/2026
# (le script recoit un 403) et archivees avec SHA256SUMS. Une annexe par (variable, annee) ; temoin independant de l'OFGL.
PDF_ANNEXES = {("dil", AN_DOT - 1): "legifrance_da_2025-06-06_n0011_dilico_prelevement_communes.pdf",
               ("rev", AN_DOT): "legifrance_da_2026-06-04_n0008_dilico_reversement.pdf",
               ("dgf", AN_DOT): "legifrance_da_2026-05-12_n0006_dgf_communes.pdf"}
# Documents officiels lus par le temoin, cites par la fiche avec leur lien (piece 0133_Communes-12 : preuves accessibles).
DOCUMENTS = {
    "arrete_dilico": {"titre_en": "order of 21 May 2025", "titre": "arrêté du 21 mai 2025", "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051695423"},
    "dil": {"titre_en": "administrative document no. 0011 of 6 June 2025", "titre": "document administratif n° 0011 du 6 juin 2025", "fichier": PDF_ANNEXES[("dil", AN_DOT - 1)],
            "url": "https://www.legifrance.gouv.fr/download/pdf?id=YzOx2OdCcw8z8XNaI5ZoWYstvrbVw7vibSIX3L_C8eE="},
    "rev": {"titre_en": "administrative document no. 0008 of 4 June 2026", "titre": "document administratif n° 0008 du 4 juin 2026", "fichier": PDF_ANNEXES[("rev", AN_DOT)],
            "url": "https://www.legifrance.gouv.fr/download/pdf?id=VoEIffkZdyyg3ErfrLMQZglgj8aUOv1MZCf1HPdWY3s="},
    "dgf": {"titre_en": "administrative document no. 0006 of 12 May 2026", "titre": "document administratif n° 0006 du 12 mai 2026", "fichier": PDF_ANNEXES[("dgf", AN_DOT)],
            "url": "https://www.legifrance.gouv.fr/download/pdf?id=briayEHf_x1Jh-oGjekY0Cu1fmt64dDetDQxhvJZNMc="},
    "lf2025_186": {"titre_en": "article 186 of the 2025 Finance Act", "titre": "article 186 de la loi de finances pour 2025", "url": "https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051169538"},
    "plf": {"titre_en": "draft budget bill for 2027, no. 3210", "titre": "projet de loi de finances pour 2027, n° 3210", "url": "https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf"},
    "ofgl": {"titre_en": "OFGL, municipal database", "titre": "OFGL, base des communes", "url": "https://data.ofgl.fr/explore/dataset/ofgl-base-communes/"},
    "ofgl_dot": {"titre_en": "OFGL, municipal grants", "titre": "OFGL, dotations des communes", "url": "https://data.ofgl.fr/explore/dataset/dotations-communes/"},
}
# Omissions constatees dans l'annexe DGF 2026 (page 286 -> 287 : la liste des Landes s'ouvre sur 40004), valeurs OFGL gardees.
OMISES_ANNEXE_DGF = {"40001", "40002", "40003"}


def temoin_annexes(dot: dict[str, dict]) -> None:
    """Chaque montant non nul de l'OFGL (DILICO preleve, reverse, cinq composantes de la DGF) relu dans l'annexe officielle,
    a l'euro pres (les annexes arrondissent a l'euro ou au centime). Arret au premier ecart, ou si une commune manque."""
    import shutil
    import subprocess
    sommes = {l.split()[1].lstrip("*"): l.split()[0] for l in (ANNEXES / "SHA256SUMS").read_text().splitlines() if l.strip()}
    for f, h in sommes.items():
        if hashlib.sha256((ANNEXES / f).read_bytes()).hexdigest() != h:
            fail("annexe %s : empreinte differente de SHA256SUMS" % f)
    if not shutil.which("pdftotext"):
        fail("pdftotext absent : le temoin des annexes officielles ne peut pas tourner")
    sep = "[ " + chr(0xA0) + chr(0x202F) + "]"
    n = r"\d{1,3}(?:" + sep + r"\d{3})*"

    def lignes(f):
        out = subprocess.run(["pdftotext", "-enc", "UTF-8", "-raw", str(ANNEXES / f), "-"], capture_output=True).stdout
        return out.decode("utf-8").replace(chr(13), "").split("\n")

    def nb(x):
        return float(re.sub(sep, "", x).replace(",", "."))

    lu: dict[str, dict] = {}
    # « code nom montant » (ordre brut : la mise en page decale code et montant d'une ligne sur certaines pages)
    r = re.compile(r"^(\d{5}|2[AB]\d{3}) .+? (" + n + r")$")
    lu["dil"] = {m.group(1): nb(m.group(2)) for m in map(r.match, lignes(PDF_ANNEXES[("dil", AN_DOT - 1)])) if m}
    # « direction nom code montant » ; code sans zero initial ; un nom long peut passer a la ligne
    r = re.compile(r"^(?:\S{2,3} .+? )?(\d{4,5}|2[AB]\d{3}) (" + n + r",\d{2})$")
    lu["rev"] = {m.group(1).zfill(5): nb(m.group(2)) for m in map(r.match, lignes(PDF_ANNEXES[("rev", AN_DOT)])) if m}
    # DGF : chiffres en police decalee (U+03EC..U+03F5), separateur de milliers dans le bloc U+0D80, Corse en controle
    dec = {chr(0x03EC + i): str(i) for i in range(10)}
    for k in ("forf", "dsu", "dsr", "dnp", "dacom"):
        lu[k] = {}
    for l in lignes(PDF_ANNEXES[("dgf", AN_DOT)]):
        l = re.sub("[" + chr(0x0D80) + "-" + chr(0x0DFF) + "]", "", "".join(dec.get(ch, ch) for ch in l))
        tok = l.split(" ")
        tok[0] = tok[0].replace(chr(4), "A").replace(chr(0x11), "B")
        if len(tok) < 7 or not re.fullmatch(r"\d{5}|2[AB]\d{3}", tok[0]) or not all(x.isdigit() for x in tok[-5:]):
            continue
        for k, v in zip(("forf", "dsu", "dsr", "dnp", "dacom"), tok[-5:]):
            lu[k][tok[0]] = float(v)
    compte = 0
    for k, vals in lu.items():
        for i, e in dot.items():
            v = e.get(k)
            if not v:
                continue
            if i not in vals:
                if k in ("forf", "dsu", "dsr", "dnp", "dacom") and i in OMISES_ANNEXE_DGF:
                    continue
                fail("temoin annexes : %s %s = %.2f a l'OFGL, absent de l'annexe officielle" % (i, k, v))
            if abs(vals[i] - v) > 1:
                fail("temoin annexes : %s %s, annexe %.2f, OFGL %.2f" % (i, k, vals[i], v))
            compte += 1
    if sum(lu["dil"].values()) != DILICO_COMMUNES_2025:
        fail("annexe DILICO : total %.2f" % sum(lu["dil"].values()))
    print("temoin annexes officielles : %d montants OFGL non nuls relus dans les arretes, 0 ecart a l'euro "
          "(omission de l'annexe DGF : %s)" % (compte, ", ".join(sorted(OMISES_ANNEXE_DGF))))
    return compte


def fiche_dot(e: dict | None, rf24) -> dict | None:
    """Ce que la fiche affiche des dotations ; null si la commune est absente du jeu."""
    if e is None:
        return None
    exo = "dom" if e["om"] == "02" else None
    rangs = {k: int(e[k]) for k in SEUILS if e.get(k) is not None and (k != "r_dsrc" or e.get("i_dsrc") is not None)}
    for k in SEUILS:  # rang de queue sans indice a la DSR cible : non classee, donc absent de rangs
        if exo is None and k in rangs and rangs[k] <= SEUILS[k]:
            exo = k
    rang = next(([k, rangs[k]] for k in ([exo] if exo in rangs else []) + list(SEUILS) if k in rangs), None)
    if exo is None and rf24 is not None and 0.03 * rf24 < 5000:
        exo = "seuil"
    # DGF et dotation en faveur des communes nouvelles : deux dispositifs, deux montants (arbitrage de l'auteur, piece
    # 2231_Communes-06 : l'OFGL range la seconde parmi les « autres dotations », hors du total « Montant Dotation DGF »).
    comp = {k: e[k] for k in ("forf", "dsu", "dsr", "dnp", "dacom") if e.get(k)}
    return {"om": e["om"], "dil": e.get("dil") or 0.0, "rev": e.get("rev") or 0.0, "dgf": e.get("dgf"), "comp": comp,
            "dcn": e.get("dcn") or None, "exo": exo, "rang": rang}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    check = "--check" in sys.argv
    cache = Path(sys.argv[sys.argv.index("--cache") + 1]) if "--cache" in sys.argv else None  # brut-ok: position d'un argument de ligne de commande, aucun rang
    ans = derniers_exercices()
    print("exercices : %s" % ans)
    communes: dict[str, dict] = {}
    lus = 0
    for an in ans:
        for cle in AGREGATS:
            for r in exporter(an, cle, cache):
                lus += 1
                c = communes.setdefault(r["insee"], {"insee": r["insee"], "nom": r["com_name"], "dep": r["dep_code"],
                                                     "epci": r["epci_code"] or None, "epci_nom": r["epci_name"] or None,
                                                     "v": {}})
                if an == ans[-1]:  # identite et strate : celles du dernier exercice
                    c.update(nom=r["com_name"], dep=r["dep_code"], epci=r["epci_code"] or None, epci_nom=r["epci_name"] or None,
                             strate=r["tranche_population"], pop=nombre(r["ptot"]))
                c["v"].setdefault(str(an), {})[cle] = nombre(r["montant"])
    # Conservation : toute commune lue est ecrite, sauf celles absentes du dernier exercice (motif nomme).
    ecartees = {i: "absente du dernier exercice publie (%d) : commune fusionnee ou compte non publie" % ans[-1]
                for i, c in communes.items() if str(ans[-1]) not in c["v"]}
    gardees = {i: c for i, c in communes.items() if i not in ecartees}
    assert len(communes) == len(gardees) + len(ecartees), "conservation rompue"
    if len(gardees) < MIN_COMMUNES:
        fail("%d communes au dernier exercice (< %d)" % (len(gardees), MIN_COMMUNES))
    neg = [i for i, c in gardees.items() if (c["v"][str(ans[-1])].get("rf") or 0) < 0]
    if neg:
        fail("recette de fonctionnement negative : %s" % neg[:5])
    # Temoin : seconde voie (records, sans filtre de budget), dix communes tirees au sort (graine fixe par releve).
    rnd = random.Random(len(gardees))
    for i in rnd.sample(sorted(gardees), 10):  # brut-ok: tirage du temoin, ordre des codes Insee
        w = 'insee="%s" and year(exer)=%d and agregat="%s"' % (i, ans[-1], AGREGATS["rf"])
        res = json.loads(get(API + "/records?" + urllib.parse.urlencode({"where": w, "select": "type_de_budget,montant", "limit": 50})))["results"]
        bp = [r["montant"] for r in res if r["type_de_budget"] == "Budget principal"]
        attendu = gardees[i]["v"][str(ans[-1])].get("rf")
        if len(bp) != 1 or attendu is None or abs(bp[0] - attendu) > 0.01:
            fail("temoin : commune %s, seconde voie %s, export %s" % (i, bp, attendu))
    print("temoin : 10 communes relues par une seconde voie, 0 ecart")
    dot = dotations(cache)
    montants_relus = temoin_annexes(dot)
    for i, c in gardees.items():
        c["d"] = fiche_dot(dot.get(i), c["v"].get("2024", {}).get("rf"))
    sans_dot = [i for i, c in gardees.items() if c["d"] is None]
    # Perimetres (piece 2231_Communes-06) : jeu des dotations 2026 = fiches + communes sans fiche, motif nomme.
    hors = [i for i in dot if i not in gardees]
    perimetres = {"dotations_%d" % AN_DOT: len(dot), "comptes_lus": len(communes), "fiches": len(gardees),
                  "comptes_absents_dernier_exercice": len(ecartees),
                  "dotations_sans_fiche": {"collectivites_outre_mer_art74": sum(1 for i in hors if dot[i]["om"] == "03"),
                                           "absentes_des_comptes_%d" % ans[-1]: sum(1 for i in hors if dot[i]["om"] != "03")}}
    assert len(dot) == len(gardees) - len(sans_dot) + len(hors), "perimetre dotations"
    print("perimetres :", perimetres)
    print("dotations rattachees : %d communes ; %d absentes du jeu des dotations (fiche : non disponible)"
          % (len(gardees) - len(sans_dot), len(sans_dot)))
    # Strates : bornes de population et medianes, lues dans les donnees (dernier exercice).
    an = str(ans[-1])
    strates: dict[str, dict] = {}
    for c in gardees.values():
        s = strates.setdefault(c.get("strate") or "?", {"pops": [], "taux_eb": [], "dette_hab": [], "dgf_hab": [], "equip_hab": [], "annees_dette": [], "part_dgf": []})
        v, p = c["v"][an], c.get("pop")
        if p:
            s["pops"].append(p)
        if v.get("rf") and v.get("eb") is not None:
            s["taux_eb"].append(v["eb"] / v["rf"])
        if p and v.get("dette") is not None:
            s["dette_hab"].append(v["dette"] / p)
        if p and v.get("dgf") is not None:
            s["dgf_hab"].append(v["dgf"] / p)
        if p and v.get("equip") is not None:
            s["equip_hab"].append(v["equip"] / p)
        if v.get("eb") and v["eb"] > 0 and v.get("dette") is not None:
            s["annees_dette"].append(v["dette"] / v["eb"])
        # Part de la DGF comptabilisee dans les recettes de fonctionnement (piece 0124_Communes-11 : la DGF par habitant
        # ne mesure pas une dependance) ; repere de la premiere reponse de la fiche (piece 0133_Communes-12).
        if v.get("rf") and v.get("dgf") is not None:
            s["part_dgf"].append(v["dgf"] / v["rf"])
    meds = {}
    for k, s in strates.items():
        meds[k] = {"n": len(s["pops"]), "pop_min": min(s["pops"]) if s["pops"] else None,  # brut-ok: populations entieres, affichees entieres
                   "pop_max": max(s["pops"]) if s["pops"] else None}  # brut-ok: populations entieres, affichees entieres
        for m in ("taux_eb", "dette_hab", "dgf_hab", "equip_hab", "annees_dette", "part_dgf"):
            meds[k][m] = statistics.median(s[m]) if s[m] else None
            meds[k][m + "_n"] = len(s[m])
    meta = {"releve_le": None, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; source OFGL (comptes des communes, DGFiP)",
            "exercices": ans, "communes": len(gardees), "ecartees": len(ecartees), "lignes_lues": lus,
            "perimetres": perimetres,
            "dotations": {"annee": AN_DOT, "source": "https://data.ofgl.fr/explore/dataset/dotations-communes/",
                          "sans_dotations": len(sans_dot), "dilico_contributrices": sum(1 for c in gardees.values() if c["d"] and c["d"]["dil"]),
                          "seuils_exoneration": SEUILS,
                          # Lus par la fiche (preuves repliees, piece 0133_Communes-12) : le compte est celui du temoin
                          # qui vient de tourner, jamais un nombre ecrit dans la page.
                          "temoin_annexes": {"montants_relus": montants_relus, "ecart_max_euro": 1},
                          "documents": DOCUMENTS},
            "strates": meds, "source": "https://data.ofgl.fr/explore/dataset/ofgl-base-communes/",
            "definitions": {"perimetre": "budget principal de la commune ; budgets annexes et intercommunalite exclus",
                            "valeurs": "euros courants ; null = non publie, jamais zero",
                            "strate": "tranche de population de l'OFGL (tranche_population) ; bornes et medianes calculees sur les communes de la tranche, dernier exercice"}}
    # Releve date par les donnees (organe commun releve_jeu, 17/10/2026) ; avec --cache, date des exports lus : relire un
    # cache ne releve rien de nouveau.
    jour = (date.fromtimestamp(min(f.stat().st_mtime for f in cache.glob("*.csv"))).isoformat() if cache
            else date.today().isoformat())
    meta["releve_le"] = rj.releve(OUT_DATA, meta, jour)
    if check:
        print("--check : %d communes, %d ecartees, %d strates ; rien ecrit." % (len(gardees), len(ecartees), len(meds)))
        return 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    par_dep: dict[str, dict] = {}
    for c in gardees.values():
        par_dep.setdefault(c["dep"], {})[c["insee"]] = {k: c.get(k) for k in ("nom", "dep", "epci", "epci_nom", "strate", "pop")} | {"v": c["v"], "d": c["d"]}
    for dep, d in par_dep.items():
        (OUT_DIR / ("%s.json" % dep)).write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    index = sorted([[c["insee"], c["nom"], c["dep"]] for c in gardees.values()], key=lambda x: x[1])  # brut-ok: tri alphabetique de l'index de recherche, aucun rang publie
    (OUT_DIR / "index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=";", lineterminator="\n")
    tete = ["insee", "commune", "departement", "epci", "epci_nom", "strate_ofgl", "population"]
    for a in ans:
        tete += ["%s_%d" % (k, a) for k in AGREGATS]
    tete += ["dilico_preleve_%d" % (AN_DOT - 1), "dilico_reverse_%d" % AN_DOT, "dgf_notifiee_%d" % AN_DOT,
             "dotation_communes_nouvelles_%d" % AN_DOT,
             "rang_%d" % AN_DOT, "classement_rang", "exoneration_art37_texte_depose"]
    w.writerow(tete)
    for c in sorted(gardees.values(), key=lambda x: x["insee"]):  # brut-ok: tri par code Insee du CSV, aucun rang publie
        ligne = [c["insee"], c["nom"], c["dep"], c.get("epci") or "", c.get("epci_nom") or "", c.get("strate") or "", c.get("pop") or ""]
        for a in ans:
            v = c["v"].get(str(a), {})
            ligne += ["" if v.get(k) is None else ("%.2f" % v[k]) for k in AGREGATS]
        d = c["d"] or {}
        ligne += ["" if d.get(k) is None else ("%.2f" % d[k]) for k in ("dil", "rev", "dgf", "dcn")]
        ligne += [d["rang"][1], d["rang"][0]] if d.get("rang") else ["", ""]
        ligne += [QUALIF.get(d.get("exo")) if d else "non_determinable"]
        w.writerow(ligne)
    OUT_CSV.write_text(buf.getvalue(), encoding="utf-8-sig", newline="\n")
    txt = json.dumps(meta, ensure_ascii=False, indent=1)
    OUT_JSON.write_text(txt, encoding="utf-8")
    OUT_DATA.write_text(txt, encoding="utf-8")
    print("Ecrit : %d fiches dans %d fichiers de departement, index, CSV, meta (%d communes ecartees, motif nomme)."
          % (len(gardees), len(par_dep), len(ecartees)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
