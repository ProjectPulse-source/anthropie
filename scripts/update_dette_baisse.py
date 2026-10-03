#!/usr/bin/env python3
"""update_dette_baisse.py -- volet « La dette publique peut-elle baisser ? » (dossier dette, volet 5).

Découverte de la page (test décisif et contre-expertise PRO-20261002-195300, arbitrage du 02/10/2026) : sur la dernière
décennie, l'effet taux-croissance a fait BAISSER le ratio de dette français, et les déficits primaires l'ont fait monter
davantage. Trois jeux, un seul calcul :

  1. France, trois décennies glissant avec la dernière année publiée : la décomposition du volet 1, cumulée ;
  2. France, année par année : le solde primaire observé et celui qui aurait stabilisé le ratio, (i - g)/(1 + g) x d(t-1) ;
  3. les pays de l'Union dont la dette dépassait SEUIL_DETTE % du PIB à la veille de la dernière décennie : même
     décomposition, même décennie ; et, en repli, toutes les fenêtres de dix ans des 27 pays, par dette de départ.

Identité (celle de update_dette_dynamique.py), par pays et par année, en monnaie nationale :
    d_t - d_{t-1} = i/(1+g) d_{t-1} - g/(1+g) d_{t-1} - pb_t + sfa_t        (sfa = résidu)

TÉMOIN, bloquant pour la France et pour les pays comparés, filtrant ailleurs : les ratios qu'Eurostat PUBLIE en % du PIB
(gov_10dd_edpt1, PC_GDP), que le calcul n'utilise pas ; tolérance TOL. Conservation : années-pays calculables ==
retenues + écartées, chaque écart avec son motif (bloc `conservation` du jeu).

Chaque phrase de la page est une garde (fonction gardes) : événement, dénominateur et période sont ceux de la phrase.
Bilingue (03/10/2026, miroir demandé par l'auteur) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés,
et des figures -en au même dessin ; les gardes ne lisent que des nombres, une passe vaut pour les deux langues.

Usage : python scripts/update_dette_baisse.py [--check]
Sorties : data/ et static/dette_baisse.json, static/dette_baisse.csv, data/figures_baisse.json,
          static/img/dette-baisse-{decennies,comparaison,stabilisant}{,-en}.svg + .png
"""
from __future__ import annotations

import csv
import html
import io
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dette_baisse.json"
OUT_STATIC = ROOT / "static" / "dette_baisse.json"
OUT_CSV = ROOT / "static" / "dette_baisse.csv"
OUT_FIGURES = ROOT / "data" / "figures_baisse.json"
OUT_IMG = ROOT / "static" / "img"
DYN = ROOT / "data" / "dette_dynamique.json"
PAGE_URL = "stephane-lalut.com/dette-publique-peut-elle-baisser/"
PAGE_URL_EN = "stephane-lalut.com/en/can-public-debt-come-down/"

TOL = 0.11            # ratios publiés à une décimale ; le solde primaire additionne deux arrondis
SEUIL_DETTE = 90.0    # dette de départ des pays comparés à la France, % du PIB
SEUILS_SENSIBILITE = (80.0, 100.0)   # le même groupe à d'autres seuils : la page dit ce qui change
SEUIL_PIB = 35.0      # croissance nominale annuelle au-delà : hyperinflation ou rupture du PIB, fenêtre écartée
FORTE_BAISSE = 15.0   # points de PIB en dix ans
API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/%s?format=JSON&%s"

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}

# nom, forme avec article (prose)
PAYS = {"AT": ("Autriche", "l'Autriche"), "BE": ("Belgique", "la Belgique"), "BG": ("Bulgarie", "la Bulgarie"),
        "CY": ("Chypre", "Chypre"), "CZ": ("Tchéquie", "la Tchéquie"), "DE": ("Allemagne", "l'Allemagne"),
        "DK": ("Danemark", "le Danemark"), "EE": ("Estonie", "l'Estonie"), "EL": ("Grèce", "la Grèce"),
        "ES": ("Espagne", "l'Espagne"), "FI": ("Finlande", "la Finlande"), "FR": ("France", "la France"),
        "HR": ("Croatie", "la Croatie"), "HU": ("Hongrie", "la Hongrie"), "IE": ("Irlande", "l'Irlande"),
        "IT": ("Italie", "l'Italie"), "LT": ("Lituanie", "la Lituanie"), "LU": ("Luxembourg", "le Luxembourg"),
        "LV": ("Lettonie", "la Lettonie"), "MT": ("Malte", "Malte"), "NL": ("Pays-Bas", "les Pays-Bas"),
        "PL": ("Pologne", "la Pologne"), "PT": ("Portugal", "le Portugal"), "RO": ("Roumanie", "la Roumanie"),
        "SE": ("Suède", "la Suède"), "SI": ("Slovénie", "la Slovénie"), "SK": ("Slovaquie", "la Slovaquie")}
LETTRES = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
           "treize", "quatorze", "quinze", "seize"]
LETTRES_EN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
              "thirteen", "fourteen", "fifteen", "sixteen"]
PAYS_EN = {"AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "CY": "Cyprus", "CZ": "Czechia", "DE": "Germany", "DK": "Denmark",
           "EE": "Estonia", "EL": "Greece", "ES": "Spain", "FI": "Finland", "FR": "France", "HR": "Croatia", "HU": "Hungary",
           "IE": "Ireland", "IT": "Italy", "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "MT": "Malta",
           "NL": "the Netherlands", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SE": "Sweden", "SI": "Slovenia",
           "SK": "Slovakia"}


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def fr(v: float, dec: int = 1) -> str:
    s = ("%." + str(dec) + "f") % v
    if float(s) == 0:
        s = s.replace("-", "")
    return s.replace("-", "−").replace(".", ",")


def signe(v: float, dec: int = 1) -> str:
    s = fr(v, dec)
    return s if s.startswith("−") else "+" + s


def milliers(v: float) -> str:
    """Entier avec séparateur de milliers insécable (règle typographique du site)."""
    return "{:,}".format(int(round(v))).replace(",", " ")


def lettres(n: int) -> str:
    return LETTRES[n] if 0 <= n < len(LETTRES) else str(n)


def enumere(noms: list[str]) -> str:
    return noms[0] if len(noms) == 1 else ", ".join(noms[:-1]) + " et " + noms[-1]


# ---- Deux langues, un seul calcul : use(lang) rebranche les formats ; les gardes, elles, ne lisent que des nombres.
FR_FMT = dict(fr=fr, signe=signe, milliers=milliers, lettres=lettres, enumere=enumere)


def _en_nb(v: float, dec: int = 1) -> str:
    s_ = ("%." + str(dec) + "f") % v
    if float(s_) == 0:
        s_ = s_.replace("-", "")
    return s_.replace("-", "−")


def _en_signe(v: float, dec: int = 1) -> str:
    s_ = _en_nb(v, dec)
    return s_ if s_.startswith("−") else "+" + s_


EN_FMT = dict(fr=_en_nb, signe=_en_signe, milliers=lambda v: "{:,}".format(int(round(v))),
              lettres=lambda n: LETTRES_EN[n] if 0 <= n < len(LETTRES_EN) else str(n),
              enumere=lambda noms: noms[0] if len(noms) == 1 else ", ".join(noms[:-1]) + " and " + noms[-1])
LANG = "fr"


def use(lang: str) -> None:
    global LANG
    LANG = lang
    globals().update(FR_FMT if lang == "fr" else EN_FMT)


def art(code: str) -> str:
    """Nom de pays dans la prose (avec article en français)."""
    return PAYS[code][1] if LANG == "fr" else PAYS_EN[code]


def nom(code: str) -> str:
    """Nom de pays seul (figures, tableaux)."""
    n = PAYS[code][0] if LANG == "fr" else PAYS_EN[code]
    return n[0].upper() + n[1:]


def aucune() -> str:
    return "aucune" if LANG == "fr" else "none"


# ------------------------------------------------------------------ données
def fetch(url: str, essais: int = 3) -> bytes:
    for k in range(essais):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com (stephane@stephane-lalut.com)"})
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if k == essais - 1:
                fail("reseau : %s (%s)" % (url[:120], e))
            time.sleep(3 * (k + 1))
    return b""


def eurostat(ds: str, **f) -> dict[tuple[str, int], float]:
    """Tous les pays d'un jeu, une seule valeur par (pays, année) : toute autre dimension doit être fixée."""
    d = json.loads(fetch(API % (ds, "&".join("%s=%s" % kv for kv in f.items()))))
    if "dimension" not in d:
        fail("Eurostat %s : reponse sans dimensions" % ds)
    ids, size = d["id"], d["size"]
    for dim, n in zip(ids, size):
        if dim not in ("geo", "time") and n != 1:
            fail("Eurostat %s : dimension %s non fixee (%d valeurs)" % (ds, dim, n))
    if ids[-2:] != ["geo", "time"]:
        fail("Eurostat %s : ordre des dimensions inattendu (%s)" % (ds, ids))
    nt = size[-1]
    out = {}
    for g, ig in d["dimension"]["geo"]["category"]["index"].items():
        for t, it in d["dimension"]["time"]["category"]["index"].items():
            v = d["value"].get(str(ig * nt + it))
            if v is not None:
                out[(g, int(t))] = float(v)
    return out


def panel():
    D = eurostat("gov_10dd_edpt1", na_item="GD", sector="S13", unit="MIO_NAC")
    Y = eurostat("gov_10dd_edpt1", na_item="B1GQ", sector="S1", unit="MIO_NAC")
    I = eurostat("gov_10a_main", na_item="D41PAY", sector="S13", unit="MIO_NAC")
    B = eurostat("gov_10a_main", na_item="B9", sector="S13", unit="MIO_NAC")
    pub = {k: eurostat("gov_10dd_edpt1", na_item=k, sector="S13", unit="PC_GDP") for k in ("GD", "B9", "D41PAY")}
    if "--mutation-pib" in sys.argv:   # témoin positif : PIB en euros, le contrôle doit rejeter les pays hors zone euro
        Y = eurostat("nama_10_gdp", na_item="B1GQ", unit="CP_MEUR")
    R, ecartes, calculables = {}, [], 0
    for p in sorted(PAYS):
        for a in sorted(a for (g, a) in D if g == p):
            k, k0 = (p, a), (p, a - 1)
            if not (k0 in D and k in Y and k0 in Y and k in I and k in B):
                continue
            calculables += 1
            d0, d1 = D[k0] / Y[k0] * 100, D[k] / Y[k] * 100
            i, g = I[k] / D[k0], Y[k] / Y[k0] - 1
            interets, croissance = i / (1 + g) * d0, -g / (1 + g) * d0
            pb = (B[k] + I[k]) / Y[k] * 100
            sfa = (d1 - d0) - (interets + croissance) + pb
            if not all(k in pub[x] for x in pub):
                ecartes.append(dict(pays=p, annee=a, motif="ratio publié absent"))
                continue
            e_d, e_pb = d1 - pub["GD"][k], pb - (pub["B9"][k] + pub["D41PAY"][k])
            if abs(e_d) > TOL or abs(e_pb) > TOL:
                ecartes.append(dict(pays=p, annee=a, motif="écart au ratio publié", ecart_dette=round(e_d, 2), ecart_solde_primaire=round(e_pb, 2)))
                continue
            R.setdefault(p, {})[a] = dict(pays=p, annee=a, dette=d1, dette_prec=d0, variation=d1 - d0, interets=interets,
                                          encours=D[k] / 1000, encours_prec=D[k0] / 1000,
                                          croissance=croissance, taux_croissance=interets + croissance, solde_primaire=pb,
                                          flux_stock=sfa, taux_implicite=i * 100, croissance_nominale=g * 100)
    if calculables != sum(len(v) for v in R.values()) + len(ecartes):
        fail("conservation rompue : %d calculables, %d retenues, %d ecartees" % (calculables, sum(len(v) for v in R.values()), len(ecartes)))
    return R, ecartes, calculables


def fenetre(an: dict, a0: int, n: int = 10):
    """Dix flux annuels a0..a0+9 = variation entre le stock de fin (a0-1) et le stock de fin (a0+9)."""
    if not all(a in an for a in range(a0, a0 + n)):
        return None
    L = [an[a] for a in range(a0, a0 + n)]
    s = lambda k: sum(x[k] for x in L)
    f = dict(pays=L[0]["pays"], debut=a0, fin=a0 + n - 1, dette_depart=L[0]["dette_prec"], dette_fin=L[-1]["dette"],
             variation=L[-1]["dette"] - L[0]["dette_prec"], interets=s("interets"), croissance=s("croissance"),
             taux_croissance=s("taux_croissance"), deficits_primaires=-s("solde_primaire"), flux_stock=s("flux_stock"),
             solde_primaire_moyen=s("solde_primaire") / n, annees_excedent=sum(1 for x in L if x["solde_primaire"] > 0),
             croissance_max=max(abs(x["croissance_nominale"]) for x in L), croissance_nominale_moyenne=s("croissance_nominale") / n,
             encours_depart=L[0]["encours_prec"], encours_fin=L[-1]["encours"])
    if abs(f["variation"] - (f["taux_croissance"] + f["deficits_primaires"] + f["flux_stock"])) > 1e-6:
        fail("%s %d : la somme des termes ne rend pas la variation" % (f["pays"], a0))
    return f


def calcul():
    R, ecartes, calculables = panel()
    if "FR" not in R or any(e["pays"] == "FR" for e in ecartes):
        fail("France : annee ecartee par le temoin (%s)" % [e for e in ecartes if e["pays"] == "FR"])
    FR = R["FR"]
    fin = max(FR)
    if fin - 29 not in FR:
        fail("France : moins de trente annees (%d-%d)" % (min(FR), fin))
    # Cohérence avec le volet 1 : mêmes séries, mêmes valeurs. Un écart = deux pages du dossier qui se contredisent.
    if not DYN.is_file():
        fail("data/dette_dynamique.json absent : lancer scripts/update_dette_dynamique.py d'abord")
    dyn = {r["annee"]: r for r in json.loads(DYN.read_text(encoding="utf-8"))["annees"]}
    for a in range(fin - 29, fin + 1):
        if a not in dyn or abs(dyn[a]["dette_pct_pib"] - FR[a]["dette"]) > 0.005 or abs(dyn[a]["solde_primaire_pct_pib"] - FR[a]["solde_primaire"]) > 0.005:
            fail("France %d : ecart avec le volet 1 (data/dette_dynamique.json) ; relancer update_dette_dynamique.py" % a)
    depart_dyn = json.loads(DYN.read_text(encoding="utf-8"))["depart"]   # contre-expertise PRO-20261003-064640 : 1995 aussi
    if depart_dyn["annee"] != fin - 30 or abs(depart_dyn["dette_pct_pib"] - FR[fin - 29]["dette_prec"]) > 0.005:
        fail("France %d : dette de depart differente de celle du volet 1" % (fin - 30))
    dec = [fenetre(FR, fin - 29), fenetre(FR, fin - 19), fenetre(FR, fin - 9)]
    annees = [dict(annee=a, solde_primaire=FR[a]["solde_primaire"], solde_stabilisant=FR[a]["taux_croissance"],
                   ecart=FR[a]["solde_primaire"] - FR[a]["taux_croissance"], dette=FR[a]["dette"],
                   variation=FR[a]["variation"], flux_stock=FR[a]["flux_stock"],
                   taux_implicite=FR[a]["taux_implicite"], croissance_nominale=FR[a]["croissance_nominale"])
              for a in range(fin - 29, fin + 1)]
    # Pays comparés : dette >= SEUIL_DETTE à la veille de la dernière décennie ; décennie complète exigée.
    a0 = fin - 9
    candidats = [p for p in R if (a0 in R[p] and R[p][a0]["dette_prec"] >= SEUIL_DETTE)]
    cmp_, incomplets = [], []
    for p in candidats:
        f = fenetre(R[p], a0)
        (cmp_.append(f) if f and f["croissance_max"] <= SEUIL_PIB else incomplets.append(p))
    if incomplets:
        fail("pays compares : decennie incomplete ou ecartee par le temoin pour %s" % incomplets)
    cmp_.sort(key=lambda f: f["variation"])
    for f in cmp_:
        f["nom"] = PAYS[f["pays"]][0]
    # Sensibilité du groupe au seuil (contre-expertise PRO-20261003-064640, B3) : mêmes calculs à 80 et à 100 %.
    sensibilite = {}
    for s in SEUILS_SENSIBILITE:
        g = [fenetre(R[p], a0) for p in R if a0 in R[p] and R[p][a0]["dette_prec"] >= s]
        sensibilite[str(int(s))] = sorted((dict(pays=f["pays"], nom=PAYS[f["pays"]][0], dette_depart=f["dette_depart"], variation=f["variation"],
                                               solde_primaire_moyen=f["solde_primaire_moyen"]) for f in g if f), key=lambda f: f["variation"])
    # Repli : toutes les fenêtres de dix ans, par dette de départ.
    F, hyper = [], 0
    for p in R:
        for d0 in range(min(R[p]), max(R[p]) - 8):
            f = fenetre(R[p], d0)
            if f is None:
                continue
            if f["croissance_max"] > SEUIL_PIB:
                hyper += 1
                continue
            F.append(f)
    hautes = [f for f in F if f["dette_depart"] >= SEUIL_DETTE]
    defi, exc = [f for f in hautes if f["solde_primaire_moyen"] < 0], [f for f in hautes if f["solde_primaire_moyen"] >= 2]
    mid = [f for f in hautes if 0 <= f["solde_primaire_moyen"] < 2]
    europe = dict(fenetres=len(F), fenetres_ecartees_pib=hyper, pays=len({f["pays"] for f in F}), premiere=min(f["debut"] for f in F),
                  haute_dette=dict(seuil=SEUIL_DETTE, fenetres=len(hautes),
                                   deficit=dict(n=len(defi), fortes_baisses=sum(1 for f in defi if f["variation"] <= -FORTE_BAISSE),
                                                baisses=sum(1 for f in defi if f["variation"] < 0), pays=sorted({f["pays"] for f in defi})),
                                   excedent_2=dict(n=len(exc), fortes_baisses=sum(1 for f in exc if f["variation"] <= -FORTE_BAISSE),
                                                   baisses=sum(1 for f in exc if f["variation"] < 0), pays=sorted({f["pays"] for f in exc}),
                                                   debut_avant_2003=sum(1 for f in exc if f["debut"] < 2003)),
                                   excedent_0_2=dict(n=len(mid), fortes_baisses=sum(1 for f in mid if f["variation"] <= -FORTE_BAISSE),
                                                     baisses=sum(1 for f in mid if f["variation"] < 0), pays=sorted({f["pays"] for f in mid}))))
    if len(defi) + len(mid) + len(exc) != len(hautes):
        fail("repli europeen : les trois classes ne couvrent pas toutes les fenetres")
    cons = dict(annees_pays_calculables=calculables, retenues=sum(len(v) for v in R.values()), ecartees=len(ecartes), detail_ecartees=ecartes)
    europe["sensibilite_seuil"] = sensibilite
    return fin, dec, annees, cmp_, europe, cons, R


# ------------------------------------------------------------------ affichage et gardes
def affichage(fin, dec, annees, cmp_, europe, cons):
    A = {"annee_fin": str(fin), "annee_debut": str(fin - 29), "seuil_dette": fr(SEUIL_DETTE, 0), "forte_baisse": fr(FORTE_BAISSE, 0),
         "tolerance": fr(TOL, 2)}
    for k, f in enumerate(dec, 1):
        p = "d%d_" % k
        A[p + "lib"] = "%d-%d" % (f["debut"], f["fin"]); A[p + "debut"] = str(f["debut"]); A[p + "fin"] = str(f["fin"])
        A[p + "var"] = signe(f["variation"]); A[p + "var_abs"] = fr(abs(f["variation"]))
        A[p + "tc"] = signe(f["taux_croissance"]); A[p + "tc_abs"] = fr(abs(f["taux_croissance"]))
        A[p + "def"] = signe(f["deficits_primaires"]); A[p + "def_abs"] = fr(abs(f["deficits_primaires"]))
        A[p + "sfa"] = signe(f["flux_stock"]); A[p + "sfa_abs"] = fr(abs(f["flux_stock"]))
        A[p + "dette_deb"] = fr(f["dette_depart"]); A[p + "dette_fin"] = fr(f["dette_fin"])
        A[p + "pb_moyen"] = signe(f["solde_primaire_moyen"], 2)
        A[p + "exc"] = lettres(f["annees_excedent"])
        A[p + "interets"] = fr(f["interets"]); A[p + "croissance"] = fr(-f["croissance"])
    exc_ans = [r["annee"] for r in annees if r["solde_primaire"] > 0]
    A["exc_n"] = lettres(len(exc_ans)); A["exc_n_maj"] = A["exc_n"][:1].upper() + A["exc_n"][1:];A["exc_premiere"] = str(exc_ans[0]); A["exc_derniere"] = str(exc_ans[-1])
    A["exc_max"] = fr(max(r["solde_primaire"] for r in annees), 2)
    A["annees_total"] = lettres(len(annees)) if len(annees) < len(LETTRES) else str(len(annees))
    last = annees[-1]
    A["stab_dernier"] = signe(last["solde_stabilisant"]); A["pb_dernier"] = signe(last["solde_primaire"])
    A["ecart_dernier"] = fr(abs(last["ecart"])); A["dette_derniere"] = fr(last["dette"])
    A["taux_implicite_dernier"] = fr(last["taux_implicite"]); A["croissance_derniere"] = fr(last["croissance_nominale"])
    suff = [r["annee"] for r in annees if r["ecart"] >= 0]
    A["suffisant_n"] = lettres(len(suff)) if len(suff) < len(LETTRES) else str(len(suff))
    stabs = [r["solde_stabilisant"] for r in annees]
    A["stab_min"] = signe(min(stabs)); A["stab_min_annee"] = str(annees[stabs.index(min(stabs))]["annee"])
    A["stab_max"] = signe(max(stabs)); A["stab_max_annee"] = str(annees[stabs.index(max(stabs))]["annee"])
    # Section « La dette française est-elle soutenable ? » (#soutenable, 03/10/2026 ; arbitrage ENTRANTE_2026-10-03_Test_5_Questions, point 4)
    creux_ti = min(annees, key=lambda r: r["taux_implicite"])
    A["ti_creux"] = fr(creux_ti["taux_implicite"]); A["ti_creux_annee"] = str(creux_ti["annee"])
    A["var_derniere"] = fr(abs(last["variation"]))
    rg_pos = sum(1 for r in annees if r["taux_implicite"] > r["croissance_nominale"])
    A["rg_pos_n"] = str(rg_pos)   # en chiffres : la prose le met en regard de annees_total, en chiffres au-delà de seize
    # Un point d'écart taux-croissance durable déplace le solde stabilisant de d(t-1)/(1+g) point : dette et croissance de la dernière année.
    A["sens_pt"] = fr(last["dette"] / 100 / (1 + last["croissance_nominale"] / 100))
    # pays comparés
    a0 = fin - 9
    A["cmp_lib"] = "%d-%d" % (a0, fin); A["cmp_veille"] = str(a0 - 1); A["cmp_n"] = lettres(len(cmp_))
    A["cmp_n_maj"] = A["cmp_n"][:1].upper() + A["cmp_n"][1:]; A["cmp_autres_n"] = lettres(len(cmp_) - 1)
    haut = [f for f in cmp_ if f["solde_primaire_moyen"] > 0]
    bas = [f for f in cmp_ if f["solde_primaire_moyen"] <= 0]
    A["cmp_exc_n"] = lettres(len(haut)); A["cmp_def_n"] = lettres(len(bas))
    A["cmp_exc_pays"] = enumere([art(f["pays"]) for f in sorted(haut, key=lambda f: f["variation"])])
    A["cmp_def_autres"] = enumere([art(f["pays"]) for f in sorted(bas, key=lambda f: f["variation"]) if f["pays"] != "FR"])
    A["cmp_exc_baisse_min"] = fr(min(-f["variation"] for f in haut), 0); A["cmp_exc_baisse_max"] = fr(max(-f["variation"] for f in haut), 0)
    A["cmp_exc_pb_min"] = fr(min(f["solde_primaire_moyen"] for f in haut)); A["cmp_exc_pb_max"] = fr(max(f["solde_primaire_moyen"] for f in haut))
    autres = [f for f in bas if f["pays"] != "FR"]
    A["cmp_def_var_min"] = signe(min(f["variation"] for f in autres)); A["cmp_def_var_max"] = signe(max(f["variation"] for f in autres))
    A["cmp_tc_min"] = fr(min(-f["taux_croissance"] for f in cmp_), 0); A["cmp_tc_max"] = fr(max(-f["taux_croissance"] for f in cmp_), 0)
    for f in cmp_:
        c = "cmp_%s_" % f["pays"].lower()
        A[c + "nom"] = nom(f["pays"])
        A[c + "var"] = signe(f["variation"]); A[c + "tc"] = signe(f["taux_croissance"]); A[c + "def"] = signe(f["deficits_primaires"])
        A[c + "sfa"] = signe(f["flux_stock"]); A[c + "sfa_abs"] = fr(abs(f["flux_stock"])); A[c + "pb"] = signe(f["solde_primaire_moyen"])
        A[c + "d0"] = fr(f["dette_depart"]); A[c + "d1"] = fr(f["dette_fin"])
        A[c + "enc0"] = milliers(f["encours_depart"]); A[c + "enc1"] = milliers(f["encours_fin"])
        A[c + "tcdef"] = signe(f["taux_croissance"] + f["deficits_primaires"])
    # Dernière décennie : où se concentre l'allègement (contre-expertise PRO-20261003-064640, B2)
    d3 = dec[2]
    an3 = [r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]]
    trios = [an3[k:k + 3] for k in range(len(an3) - 2)]
    creux = min(trios, key=lambda t: sum(r["solde_stabilisant"] for r in t))
    tc_creux = sum(r["solde_stabilisant"] for r in creux)
    A["d3_creux_lib"] = "%d-%d" % (creux[0]["annee"], creux[-1]["annee"]); A["d3_creux_abs"] = fr(abs(tc_creux))
    A["d3_reste"] = signe(d3["taux_croissance"] - tc_creux); A["d3_reste_n"] = lettres(len(an3) - 3)
    pic = max(an3, key=lambda r: r["solde_stabilisant"])
    A["d3_pic_annee"] = str(pic["annee"]); A["d3_pic_tc"] = signe(pic["solde_stabilisant"])
    # Années où le solde atteint le repère sans que le ratio baisse (B4)
    sh = [r["annee"] for r in annees if r["ecart"] >= 0 and r["variation"] > 0]
    A["suff_hausse"] = enumere([str(a) for a in sh]) if sh else ""
    A["suff_baisse_n"] = lettres(sum(1 for r in annees if r["ecart"] >= 0 and r["variation"] < 0))  # ENTRANTE 03/10, point 4
    # Sensibilité du groupe au seuil (B3)
    s80, s100 = europe["sensibilite_seuil"]["80"], europe["sensibilite_seuil"]["100"]
    codes90 = {f["pays"] for f in cmp_}
    ajouts = [f for f in s80 if f["pays"] not in codes90]
    A["s80_n"] = lettres(len(s80)); A["s80_ajouts"] = enumere([art(f["pays"]) for f in sorted(ajouts, key=lambda f: f["pays"])])
    exc80 = [f for f in ajouts if f["variation"] <= -FORTE_BAISSE and f["solde_primaire_moyen"] < 0]
    if exc80:
        e = exc80[0]
        A["s80_exc_pays"] = art(e["pays"]); A["s80_exc_nom"] = nom(e["pays"]); A["s80_exc_d0"] = fr(e["dette_depart"])
        A["s80_exc_var"] = fr(abs(e["variation"])); A["s80_exc_pb"] = signe(e["solde_primaire_moyen"])
    A["s100_n"] = lettres(len(s100))
    # Europe, repli
    h = europe["haute_dette"]
    A["eu_pays"] = str(europe["pays"]); A["eu_fenetres"] = str(europe["fenetres"]); A["eu_premiere"] = str(europe["premiere"])
    A["eu_def_n"] = str(h["deficit"]["n"]); A["eu_def_fb"] = lettres(h["deficit"]["fortes_baisses"]) if h["deficit"]["fortes_baisses"] else aucune()
    A["eu_def_baisses"] = lettres(h["deficit"]["baisses"]); A["eu_def_pays_n"] = lettres(len(h["deficit"]["pays"]))
    A["eu_def_pays"] = enumere([art(p) for p in h["deficit"]["pays"]])
    A["eu_exc_n"] = lettres(h["excedent_2"]["n"]); A["eu_exc_baisses"] = lettres(h["excedent_2"]["baisses"])
    A["eu_exc_fb"] = lettres(h["excedent_2"]["fortes_baisses"]); A["eu_exc_pays_n"] = lettres(len(h["excedent_2"]["pays"]))
    A["eu_exc_pays"] = enumere([art(p) for p in h["excedent_2"]["pays"]])
    m = h["excedent_0_2"]
    A["eu_mid_n"] = str(m["n"]); A["eu_mid_baisses"] = lettres(m["baisses"]) if m["baisses"] < len(LETTRES) else str(m["baisses"])
    A["eu_mid_fb"] = lettres(m["fortes_baisses"]) if m["fortes_baisses"] < len(LETTRES) else str(m["fortes_baisses"])
    A["eu_mid_pays_n"] = lettres(len(m["pays"])); A["eu_hautes_n"] = str(h["fenetres"])
    A["cons_calculables"] = str(cons["annees_pays_calculables"]); A["cons_ecartees"] = lettres(cons["ecartees"]) if cons["ecartees"] < len(LETTRES) else str(cons["ecartees"])
    A["cons_retenues"] = str(cons["retenues"]); A["cons_ecartees_maj"] = A["cons_ecartees"][:1].upper() + A["cons_ecartees"][1:]
    return A, haut, bas, exc_ans


def gardes(fin, dec, annees, cmp_, europe, haut, bas, exc_ans):
    d1, d2, d3 = dec
    last = annees[-1]
    fr_c = next(f for f in cmp_ if f["pays"] == "FR")
    h = europe["haute_dette"]
    G = [
        # --- découverte : dernière décennie
        ("dernière décennie : l'effet taux-croissance fait BAISSER le ratio (de plus de 10 points)", d3["taux_croissance"] < -10),
        ("dernière décennie : les déficits primaires ajoutent plus que l'effet taux-croissance ne retire", d3["deficits_primaires"] > -d3["taux_croissance"]),
        ("dernière décennie : la dette monte", d3["variation"] > 0),
        ("dernière décennie : aucune année d'excédent primaire", d3["annees_excedent"] == 0),
        ("dernière décennie : les déficits primaires font plus que toute la hausse", d3["deficits_primaires"] > d3["variation"]),
        # --- les deux décennies précédentes
        ("première décennie : l'effet taux-croissance pousse la dette, le solde primaire pèse peu (moins de 5 points)",
         d1["taux_croissance"] > 5 and abs(d1["deficits_primaires"]) < 5),
        ("première décennie : la dette monte", d1["variation"] > 0),
        ("deuxième décennie : taux-croissance et déficits poussent ensemble, les déficits dominent (plus du double)",
         d2["taux_croissance"] > 0 and d2["deficits_primaires"] > 2 * d2["taux_croissance"]),
        ("deuxième décennie : la plus forte hausse des trois", d2["variation"] > max(d1["variation"], d3["variation"])),
        ("les déficits primaires cumulés croissent d'une décennie à l'autre", d1["deficits_primaires"] < d2["deficits_primaires"] < d3["deficits_primaires"]),
        ("la dette monte dans les trois décennies", all(f["variation"] > 0 for f in dec)),
        ("première décennie : le solde primaire cumulé est un excédent", d1["deficits_primaires"] < 0),
        ("deuxième décennie : contient 2008 et 2009 ; dernière décennie : contient 2020 à 2023",
         d2["debut"] <= 2008 and d2["fin"] >= 2009 and d3["debut"] <= 2020 and d3["fin"] >= 2023),
        # --- excédents
        ("après la dernière année d'excédent, le solde primaire est déficitaire chaque année", all(r["solde_primaire"] < 0 for r in annees if r["annee"] > exc_ans[-1])),
        ("les années d'excédent primaire sont consécutives et dans la première décennie",
         exc_ans == list(range(exc_ans[0], exc_ans[-1] + 1)) and d1["debut"] <= exc_ans[0] and exc_ans[-1] <= d1["fin"]),
        ("excédent primaire maximal inférieur à 2 % du PIB", max(r["solde_primaire"] for r in annees) < 2),
        # --- solde stabilisant
        ("dernière année : solde observé inférieur de plus de 2 points au solde stabilisant", last["ecart"] < -2),
        ("dernière année : solde stabilisant proche de zéro (entre -0,5 et +0,5)", abs(last["solde_stabilisant"]) < 0.5),
        ("le solde stabilisant varie de plus de 10 points d'une année à l'autre de la série", max(r["solde_stabilisant"] for r in annees) - min(r["solde_stabilisant"] for r in annees) > 10),
        ("le solde stabilisant le plus haut est une année de recul du PIB nominal",
         max(annees, key=lambda r: r["solde_stabilisant"])["croissance_nominale"] < 0),
        ("le solde stabilisant le plus bas est une année de forte croissance nominale (plus de 5 %)",
         min(annees, key=lambda r: r["solde_stabilisant"])["croissance_nominale"] > 5),
        ("moins d'une année sur deux au-dessus du solde stabilisant", sum(1 for r in annees if r["ecart"] >= 0) * 2 < len(annees)),
        # --- section #soutenable et « Ce qu'il faut retenir » (03/10/2026)
        ("dernière année : le ratio n'est pas stabilisé, il monte", last["variation"] > 0),
        ("le taux implicite « remonte » : son creux date de 2019 ou après et la dernière année le dépasse d'au moins 0,5 point",
         min(annees, key=lambda r: r["taux_implicite"])["annee"] >= 2019
         and last["taux_implicite"] > min(r["taux_implicite"] for r in annees) + 0.5),
        ("la croissance nominale « retombe » : la dernière année est sous la moyenne de 2021-2023 d'au moins 3 points",
         sum(r["croissance_nominale"] for r in annees if 2021 <= r["annee"] <= 2023) / 3 - last["croissance_nominale"] > 3),
        ("un point d'écart taux-croissance vaut « un peu plus d'un point » de solde stabilisant (entre 1 et 1,3)",
         1 < last["dette"] / 100 / (1 + last["croissance_nominale"] / 100) < 1.3),
        # --- pays comparés
        ("pays comparés : au moins cinq, dont la France", len(cmp_) >= 5 and any(f["pays"] == "FR" for f in cmp_)),
        ("pays comparés : l'effet taux-croissance fait baisser le ratio chez tous", all(f["taux_croissance"] < 0 for f in cmp_)),
        ("pays comparés : avec un excédent primaire moyen, la dette baisse d'au moins 15 points chez tous", bool(haut) and all(f["variation"] <= -FORTE_BAISSE for f in haut)),
        ("pays comparés : avec un déficit primaire moyen, aucune baisse de 5 points", bool(bas) and all(f["variation"] > -5 for f in bas)),
        ("pays comparés : la France a la plus forte hausse", fr_c["variation"] == max(f["variation"] for f in cmp_)),
        ("pays comparés : la France a le déficit primaire moyen le plus élevé", fr_c["solde_primaire_moyen"] == min(f["solde_primaire_moyen"] for f in cmp_)),
        ("pays comparés : la France est le seul pays en hausse de plus de 10 points", sum(1 for f in cmp_ if f["variation"] > 10) == 1 and fr_c["variation"] > 10),
        ("pays comparés : l'effet taux-croissance français n'est pas le plus faible du groupe", fr_c["taux_croissance"] < max(f["taux_croissance"] for f in cmp_)),
        ("pays comparés : hors France, les pays en déficit primaire moyen restent à moins de 5 points de leur niveau de départ",
         all(abs(f["variation"]) < 5 for f in bas if f["pays"] != "FR")),
        ("pays comparés : tous les autres pays partaient d'une dette plus élevée que la France", all(f["dette_depart"] > fr_c["dette_depart"] for f in cmp_ if f["pays"] != "FR")),
        ("pays comparés : Grèce, Chypre et Portugal sont dans le groupe en excédent (le texte nomme leurs programmes d'assistance)",
         {"EL", "CY", "PT"} == {f["pays"] for f in haut}),
        ("pays comparés : la croissance nominale moyenne des pays en excédent dépasse celle de la France",
         all(f["croissance_nominale_moyenne"] > fr_c["croissance_nominale_moyenne"] for f in haut)),
        # --- contre-expertise PRO-20261003-064640
        ("B1 : dans les pays en excédent, le montant de la dette n'a pas diminué alors que le ratio baissait",
         all(f["encours_fin"] >= f["encours_depart"] for f in haut)),
        ("B1 : au Portugal, l'encours augmente de plus de 10 % pendant que le ratio baisse",
         any(f["pays"] == "PT" and f["encours_fin"] > 1.1 * f["encours_depart"] and f["variation"] < 0 for f in haut)),
        ("B2 : l'allègement taux-croissance de la décennie tient à trois années consécutives, les autres l'alourdissent",
         sum(r["solde_stabilisant"] for r in min([[r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]][k:k + 3] for k in range(8)],
                                                   key=lambda t: sum(r["solde_stabilisant"] for r in t))) < d3["taux_croissance"]),
        ("B2 : l'année où l'effet taux-croissance pousse le plus la dette est 2020 et il y est positif",
         max((r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]), key=lambda r: r["solde_stabilisant"])["annee"] == 2020
         and next(r for r in annees if r["annee"] == 2020)["solde_stabilisant"] > 0),
        ("B3 : à 80 %, un seul pays ajouté connaît une baisse de 15 points avec un déficit primaire moyen (la Slovénie)",
         [f["pays"] for f in europe["sensibilite_seuil"]["80"] if f["pays"] not in {c["pays"] for c in cmp_}
          and f["variation"] <= -FORTE_BAISSE and f["solde_primaire_moyen"] < 0] == ["SI"]),
        ("B2 : les trois années les plus favorables de la décennie sont 2021-2023 (le texte parle du rebond et de l'inflation)",
         [r["annee"] for r in min([[r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]][k:k + 3] for k in range(8)],
                                  key=lambda t: sum(r["solde_stabilisant"] for r in t))] == [2021, 2022, 2023]),
        ("F3 : l'Espagne est dans le groupe (le texte cite son aide bancaire de 2012-2014)", any(f["pays"] == "ES" for f in cmp_)),
        ("B3 : à 100 %, la France sort du groupe", "FR" not in {f["pays"] for f in europe["sensibilite_seuil"]["100"]}),
        ("ENTRANTE 03/10 : parmi les années au-dessus du repère, la plupart ont vu le ratio baisser",
         sum(1 for r in annees if r["ecart"] >= 0 and r["variation"] < 0) * 2 > sum(1 for r in annees if r["ecart"] >= 0)),
        ("ENTRANTE 03/10 : le bilan de la dernière décennie est l'addition affichée (déficits + taux-croissance + ajustements)",
         abs(d3["deficits_primaires"] + d3["taux_croissance"] + d3["flux_stock"] - d3["variation"]) < 1e-6 and d3["flux_stock"] > 0),
        ("B4 : au moins une année où le solde atteint le repère hors ajustements et où le ratio monte",
         any(r["ecart"] >= 0 and r["variation"] > 0 for r in annees)),
        ("B5 : en Belgique, taux-croissance et solde primaire font baisser le ratio mais les autres ajustements le font monter",
         any(f["pays"] == "BE" and f["taux_croissance"] + f["deficits_primaires"] < 0 < f["variation"] and f["flux_stock"] > 0 for f in cmp_)),
        ("B5 : les pays en excédent ont des autres ajustements positifs (ils freinent leur baisse)", all(f["flux_stock"] > 0 for f in haut)),
        # --- Europe, repli
        ("dette de départ élevée, excédent d'au moins 2 % : la plupart des fenêtres commencent avant 2003", europe["haute_dette"]["excedent_2"]["debut_avant_2003"] * 2 > h["excedent_2"]["n"]),
        ("dette de départ élevée, déficit primaire moyen : aucune forte baisse", h["deficit"]["fortes_baisses"] == 0 and h["deficit"]["n"] >= 20),
        ("dette de départ élevée, excédent moyen d'au moins 2 % : la dette baisse dans toutes les fenêtres", h["excedent_2"]["baisses"] == h["excedent_2"]["n"] and h["excedent_2"]["n"] >= 5),
        ("dette de départ élevée, excédent d'au moins 2 % : quatre pays au plus (le texte dit « quelques pays »)", len(h["excedent_2"]["pays"]) <= 4),
    ]
    if "--mutation-garde" in sys.argv:   # témoin positif : inverser le signe de l'effet taux-croissance de la dernière décennie
        G[0] = (G[0][0], -d3["taux_croissance"] < -10)
    faux = [nom for nom, ok in G if not ok]
    if faux:
        fail("la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    return len(G)


# ------------------------------------------------------------------ figures

TXT = {
 "fr": dict(
  monte="fait monter le ratio", baisse="le fait baisser",
  tsa="T : taux et croissance · S : déficits (+) ou excédents (−) primaires · A : autres ajustements",
  dec_titre="France : ce qui a fait monter ou baisser la dette, décennie par décennie",
  dec_desc=("Trois groupes de trois barres, en points de PIB cumulés sur dix ans : effet des taux et de la croissance, déficits primaires, "
            "autres ajustements (flux-stock). %s : %s, %s, %s ; dette %s. %s : %s, %s, %s ; dette %s. %s : %s, %s, %s ; dette %s. "
            "Sur la dernière décennie, l'effet des taux et de la croissance fait baisser le ratio et les déficits primaires le font monter davantage."),
  dec_sous="dette : %s points (%s → %s %% du PIB)",
  dec_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), France, %s-%s",
  dec_note="Points de PIB cumulés sur dix ans ; décomposition comptable, non causale : les trois termes ne sont pas indépendants.",
  cmp_titre="%s pays à plus de %s %% de dette fin %s : dix ans après",
  cmp_desc=("Pour chaque pays, trois barres en points de PIB cumulés de %s : l'effet des taux et de la croissance, la contribution du solde "
            "primaire (un excédent fait baisser la dette, un déficit la fait monter) et les autres ajustements. "),
  cmp_desc_pays="%s : taux-croissance %s, solde primaire %s, autres ajustements %s, dette %s.",
  cmp_desc_fin=(" L'effet des taux et de la croissance est favorable partout, mais d'ampleur très différente ; le ratio a baissé de plus de 15 points "
                "là où le solde primaire a été excédentaire en moyenne."),
  cmp_sous="ratio : %s",
  cmp_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), %s ; pays triés par variation de la dette",
  cmp_note="Points de PIB cumulés ; Grèce, Chypre et Portugal ont reçu des financements officiels (2010-2018). Comparaison comptable, non causale.",
  stab_titre="France : le solde primaire observé et celui qui aurait stabilisé la dette",
  stab_desc=("Deux courbes annuelles de %s à %s, en %% du PIB : le solde primaire observé, positif %s fois (%s à %s), et le solde primaire qui "
             "aurait stabilisé le ratio de dette, qui va de %s en %s à %s en %s. En %s, le solde observé est de %s et le solde stabilisant de %s."),
  pc=" %", recul="recul du PIB", rebond="rebond du PIB",
  leg_obs="solde primaire observé", leg_stab="solde qui aurait stabilisé le ratio cette année-là, hors autres ajustements", leg_stab_x=210,
  stab_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), France, %s-%s",
  stab_note="En % du PIB ; solde stabilisant = (taux implicite − croissance nominale) / (1 + croissance) × dette de l'année précédente, hors autres ajustements (flux-stock).",
  montre=[("decennies", "De décennie en décennie, le terme qui fait monter la dette française change ; sur la dernière, taux et "
                        "croissance l'ont fait baisser et les déficits primaires l'ont fait monter davantage."),
          ("comparaison", "Parmi les pays partis d'une dette au moins aussi élevée, l'effet des taux et de la croissance a été favorable "
                          "partout ; la dette a baissé là où le solde primaire était excédentaire en moyenne."),
          ("stabilisant", "Le solde primaire qui stabilise la dette change chaque année avec les taux et la croissance ; "
                          "le solde observé est resté le plus souvent en dessous.")]),
 "en": dict(
  monte="pushes the ratio up", baisse="pulls it down",
  tsa="T: interest and growth · S: primary deficits (+) or surpluses (−) · A: other adjustments",
  dec_titre="France: what pushed the debt up or down, decade by decade",
  dec_desc=("Three groups of three bars, in points of GDP cumulated over ten years: effect of interest rates and growth, primary deficits, "
            "other adjustments (stock-flow). %s: %s, %s, %s; debt %s. %s: %s, %s, %s; debt %s. %s: %s, %s, %s; debt %s. "
            "Over the last decade, the interest-growth effect pulled the ratio down and primary deficits pushed it up by more."),
  dec_sous="debt: %s points (%s → %s%% of GDP)",
  dec_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), France, %s-%s",
  dec_note="Points of GDP cumulated over ten years; an accounting decomposition, not a causal one: the three terms are not independent.",
  cmp_titre="%s countries with debt above %s%% of GDP at end-%s: ten years on",
  cmp_desc=("For each country, three bars in points of GDP cumulated over %s: the interest-growth effect, the contribution of the primary "
            "balance (a surplus pulls the debt down, a deficit pushes it up) and other adjustments. "),
  cmp_desc_pays="%s: interest-growth %s, primary balance %s, other adjustments %s, debt %s.",
  cmp_desc_fin=(" The interest-growth effect is favourable everywhere, but of very different size; the ratio fell by more than 15 points "
                "where the primary balance was in surplus on average."),
  cmp_sous="ratio: %s",
  cmp_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), %s; countries sorted by change in the debt ratio",
  cmp_note="Points of GDP, cumulated; Greece, Cyprus and Portugal received official financing (2010-2018). An accounting comparison, not a causal one.",
  stab_titre="France: the observed primary balance and the one that would have stabilised the debt",
  stab_desc=("Two annual lines from %s to %s, in %% of GDP: the observed primary balance, positive %s times (%s to %s), and the primary balance "
             "that would have stabilised the debt ratio, ranging from %s in %s to %s in %s. In %s, the observed balance was %s and the stabilising balance %s."),
  pc="%", recul="GDP fell", rebond="GDP rebound",
  leg_obs="observed primary balance", leg_stab="balance that would have stabilised the ratio that year, excluding other adjustments", leg_stab_x=215,
  stab_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), France, %s-%s",
  stab_note="In % of GDP; stabilising balance = (implicit interest rate − nominal growth) / (1 + growth) × previous year's debt, excluding other adjustments (stock-flow).",
  montre=[("decennies", "From one decade to the next, the term pushing French debt up changes; over the last one, interest and growth "
                        "pulled it down and primary deficits pushed it up by more."),
          ("comparaison", "Among countries that started from debt at least as high, the interest-growth effect was favourable everywhere; "
                          "debt fell where the primary balance was in surplus on average."),
          ("stabilisant", "The primary balance that stabilises the debt changes every year with interest rates and growth; the observed "
                          "balance mostly stayed below it.")]),
}
SUFFIXE = {"fr": "", "en": "-en"}

def esc(s: str) -> str:
    return html.escape(s, quote=False)


def entete(h, ident, titre, desc):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h + 52, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
            '<text x="0" y="18" font-size="15" font-weight="600" fill="%s">%s</text>' % (INK, esc(titre))]


def cartouche(y0, source, note):
    out = ['<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID)]
    for k, (t, c) in enumerate([(source, INK2), (note, INK2), (LICENCES[LANG], MUTED)]):
        out.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, c, esc(t)))
    return out


def legende(e, items, y=36):
    x = 40
    for col, lib in items:
        e.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/>' % (x, y, col))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (x + 14, y + 9, INK2, esc(lib)))
        x += 14 + 6.2 * len(lib) + 20


def barres_groupees(e, groupes, X0, X1, TOP, BAS, pas_grille):
    """groupes : [(libellé, sous-libellé, [(valeur, étiquette courte)]...)]. Orange : fait monter ; gris : fait baisser."""
    vals = [v for _, _, bs in groupes for v, _ in bs]
    vmax = (int(max(max(vals), 0) / pas_grille) + 1) * pas_grille
    vmin = -(int(-min(min(vals), 0) / pas_grille) + 1) * pas_grille if min(vals) < 0 else 0

    def Y(v):
        return BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)

    for g in range(vmin, vmax + 1, pas_grille):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(g) + 3, MUTED, signe(g, 0) if g else "0"))
    pas = (X1 - X0) / len(groupes)
    for k, (lib, sous, bs) in enumerate(groupes):
        gx = X0 + pas * k
        bw = pas * 0.74 / len(bs)
        for j, (v, court) in enumerate(bs):
            x = gx + pas * 0.13 + bw * j
            e.append('<text x="%.1f" y="%d" font-size="9" font-weight="600" fill="%s" text-anchor="middle">%s</text>' % (x + bw / 2, BAS + 13, MUTED, esc(court)))
            col = ORANGE if v >= 0 else GRIS
            y0, y1 = (Y(v), Y(0)) if v >= 0 else (Y(0), Y(v))
            e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x + 1.5, y0, bw - 3, max(y1 - y0, 0.6), col))
            e.append('<text x="%.1f" y="%.1f" font-size="10" font-weight="600" fill="%s" text-anchor="middle">%s</text>'
                     % (x + bw / 2, (Y(v) - 4) if v >= 0 else (Y(v) + 12), INK, signe(v)))
        e.append('<text x="%.1f" y="%d" font-size="11.5" font-weight="600" fill="%s" text-anchor="middle">%s</text>' % (gx + pas / 2, BAS + 32, INK, esc(lib)))
        e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (gx + pas / 2, BAS + 46, BLEU, esc(sous)))
    return Y


def fig_decennies(dec, A):
    H = 356
    T = TXT[LANG]
    titre = T["dec_titre"]
    d1, d2, d3 = dec
    desc = (T["dec_desc"]
            % tuple(x for k in (1, 2, 3) for x in (A["d%d_lib" % k], A["d%d_tc" % k], A["d%d_def" % k], A["d%d_sfa" % k], A["d%d_var" % k])))
    e = entete(H, "bd", titre, desc)
    legende(e, [(ORANGE, T["monte"]), (GRIS, T["baisse"])])
    e.append('<text x="40" y="64" font-size="11" fill="%s">%s</text>' % (INK2, esc(T["tsa"])))
    groupes = [(A["d%d_lib" % k], T["dec_sous"] % (A["d%d_var" % k], A["d%d_dette_deb" % k], A["d%d_dette_fin" % k]),
                [(f["taux_croissance"], "T"), (f["deficits_primaires"], "S"), (f["flux_stock"], "A")]) for k, f in enumerate(dec, 1)]
    barres_groupees(e, groupes, 40, W - 10, 78, 270, 10)
    e += cartouche(H + 4, T["dec_src"] % (A["annee_debut"], A["annee_fin"]), T["dec_note"])
    e.append("</svg>")
    return "\n".join(e)


def fig_comparaison(cmp_, A):
    H = 366
    T = TXT[LANG]
    titre = T["cmp_titre"] % (A["cmp_n_maj"], A["seuil_dette"], A["cmp_veille"])
    desc = (T["cmp_desc"] % A["cmp_lib"]
            + " ".join(T["cmp_desc_pays"] % (nom(f["pays"]), signe(f["taux_croissance"]), signe(f["deficits_primaires"]), signe(f["flux_stock"]), signe(f["variation"])) for f in cmp_)
            + T["cmp_desc_fin"])
    e = entete(H, "bc", titre, desc)
    legende(e, [(ORANGE, T["monte"]), (GRIS, T["baisse"])])
    e.append('<text x="40" y="64" font-size="11" fill="%s">%s</text>' % (INK2, esc(T["tsa"])))
    groupes = [(nom(f["pays"]), T["cmp_sous"] % signe(f["variation"]), [(f["taux_croissance"], "T"), (f["deficits_primaires"], "S"), (f["flux_stock"], "A")]) for f in cmp_]
    barres_groupees(e, groupes, 40, W - 10, 78, 280, 20)
    e += cartouche(H + 4, T["cmp_src"] % A["cmp_lib"], T["cmp_note"])
    e.append("</svg>")
    return "\n".join(e)


def fig_stabilisant(annees, A):
    H, X0, X1, TOP, BAS = 320, 40, W - 10, 66, 280
    T = TXT[LANG]
    titre = T["stab_titre"]
    desc = (T["stab_desc"]
            % (A["annee_debut"], A["annee_fin"], A["exc_n"], A["exc_premiere"], A["exc_derniere"], A["stab_min"], A["stab_min_annee"],
               A["stab_max"], A["stab_max_annee"], A["annee_fin"], A["pb_dernier"], A["stab_dernier"]))
    e = entete(H, "bs", titre, desc)
    vals = [r[k] for r in annees for k in ("solde_primaire", "solde_stabilisant")]
    vmax, vmin = (int(max(vals) / 2) + 1) * 2, -(int(-min(vals) / 2) + 1) * 2

    def Y(v):
        return BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)

    n = len(annees)
    X = lambda k: X0 + (X1 - X0) * (k + 0.5) / n
    for g in range(vmin, vmax + 1, 2):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(g) + 3, MUTED, (signe(g, 0) if g else "0") + T["pc"]))
    for cle, col, larg in (("solde_stabilisant", GRIS, 2.2), ("solde_primaire", ORANGE, 2.6)):
        pts = " ".join("%.1f,%.1f" % (X(k), Y(r[cle])) for k, r in enumerate(annees))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (pts, col, larg))
    for k, r in enumerate(annees):
        if r["annee"] % 5 == 0 or k == n - 1:
            e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(k), BAS + 14, INK2, r["annee"]))
    # Annotations des deux ruptures (contre-expertise PRO-20261003-064640, S4) : année du solde stabilisant le plus haut
    # (recul du PIB nominal, gardé) et le plus bas (rebond, gardé), lues dans les données, jamais saisies.
    for r_, lib in ((max(annees, key=lambda r: r["solde_stabilisant"]), T["recul"]), (min(annees, key=lambda r: r["solde_stabilisant"]), T["rebond"])):
        k = annees.index(r_)
        haut = r_["solde_stabilisant"] > 0
        e.append('<text x="%.1f" y="%.1f" font-size="10" fill="%s" text-anchor="%s">%d%s%s</text>'
                 % (((X(k) - 6, Y(r_["solde_stabilisant"]) + 4, INK2, "end") if haut
                     else (X(k) + 7, Y(r_["solde_stabilisant"]) + 3, INK2, "start")) + (r_["annee"], " : " if LANG == "fr" else ": ", lib)))
    last = annees[-1]
    for cle, col in (("solde_stabilisant", GRIS), ("solde_primaire", ORANGE)):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (X(n - 1), Y(last[cle]), col))
    e.append('<line x1="40" y1="41" x2="58" y2="41" stroke="%s" stroke-width="2.6"/>' % ORANGE)
    e.append('<text x="63" y="45" font-size="11" fill="%s">%s</text>' % (INK2, esc(T["leg_obs"])))
    x2 = T["leg_stab_x"]
    e.append('<line x1="%d" y1="41" x2="%d" y2="41" stroke="%s" stroke-width="2.2"/>' % (x2, x2 + 18, GRIS))
    e.append('<text x="%d" y="45" font-size="11" fill="%s">%s</text>' % (x2 + 23, INK2, esc(T["leg_stab"])))
    e += cartouche(H + 4, T["stab_src"] % (A["annee_debut"], A["annee_fin"]), T["stab_note"])
    e.append("</svg>")
    return "\n".join(e)


def fiches(figs):
    out = {}
    for lang in ("fr", "en"):
        out[lang] = []
        for ident, montre in TXT[lang]["montre"]:
            f = "dette-baisse-%s%s" % (ident, SUFFIXE[lang])
            svg = figs[f + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
            out[lang].append(dict(id=ident, fichier=f, titre=titre, montre=montre, source=cart[0], precaution=cart[1]))
    return out


def csv_texte(dec, annees, cmp_, europe):
    """Format long : les trois tableaux n'ont pas les mêmes colonnes."""
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "pays", "periode", "variable", "valeur"])
    cles = ["dette_depart", "dette_fin", "variation", "interets", "croissance", "taux_croissance", "deficits_primaires", "flux_stock",
            "solde_primaire_moyen", "annees_excedent", "croissance_nominale_moyenne"]
    for nom, L in (("france_decennies", dec), ("pays_dette_elevee", cmp_)):
        for f in L:
            for k in cles:
                w.writerow([nom, f["pays"], "%d-%d" % (f["debut"], f["fin"]), k, "%.3f" % f[k]])
    for r in annees:
        for k in ("solde_primaire", "solde_stabilisant", "ecart", "dette", "taux_implicite", "croissance_nominale"):
            w.writerow(["france_annuel", "FR", r["annee"], k, "%.3f" % r[k]])
    h = europe["haute_dette"]
    for classe in ("deficit", "excedent_2"):
        for k in ("n", "fortes_baisses", "baisses"):
            w.writerow(["europe_fenetres_dette_elevee", "+".join(h[classe]["pays"]), "fenetres de dix ans", "%s_%s" % (classe, k), h[classe][k]])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    fin, dec, annees, cmp_, europe, cons, _ = calcul()
    use("en")
    A_en = affichage(fin, dec, annees, cmp_, europe, cons)[0]
    use("fr")
    A, haut, bas, exc_ans = affichage(fin, dec, annees, cmp_, europe, cons)
    if set(A) != set(A_en):
        fail("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    n = gardes(fin, dec, annees, cmp_, europe, haut, bas, exc_ans)
    d3 = dec[2]
    log("France %s : dette %+.1f = taux-croissance %+.1f + deficits primaires %+.1f + flux-stock %+.1f ; %d pays compares ; %d annees-pays ecartees sur %d"
        % (A["d3_lib"], d3["variation"], d3["taux_croissance"], d3["deficits_primaires"], d3["flux_stock"], len(cmp_), cons["ecartees"], cons["annees_pays_calculables"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(A)))
        return 0
    figs = {}
    for lang, AA in (("fr", A), ("en", A_en)):
        use(lang)
        x = SUFFIXE[lang]
        figs["dette-baisse-decennies%s.svg" % x] = fig_decennies(dec, AA)
        figs["dette-baisse-comparaison%s.svg" % x] = fig_comparaison(cmp_, AA)
        figs["dette-baisse-stabilisant%s.svg" % x] = fig_stabilisant(annees, AA)
    use("fr")
    payload = {"meta": {"releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "perimetre": "administrations publiques (S.13), SEC 2010, monnaie nationale, PIB de la notification de déficit et de dette",
                        "identite": "d_t - d_{t-1} = i/(1+g) d_{t-1} - g/(1+g) d_{t-1} - pb_t + sfa_t",
                        "definitions": {"taux_croissance": "effet cumulé des intérêts et de la croissance du PIB nominal sur le ratio, en points de PIB",
                                        "deficits_primaires": "déficits hors intérêts cumulés, en points de PIB (négatif : excédents)",
                                        "flux_stock": "variation de dette qui ne passe pas par le déficit ; résidu de l'identité",
                                        "solde_stabilisant": "solde primaire qui aurait laissé le ratio inchangé cette année-là, hors flux-stock : (i - g)/(1 + g) x d(t-1)",
                                        "temoin": "ratios de dette et de solde primaire comparés à ceux publiés par Eurostat en %% du PIB ; tolérance %.2f point" % TOL}},
               "france": {"decennies": dec, "annees": annees}, "pays_dette_elevee": cmp_, "europe": europe, "conservation": cons, "affichage": A, "affichage_en": A_en}
    releve = payload["meta"]["releve_le"]
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev); p2.pop("releve_le", None); p2.pop("_licence", None); p2["meta"] = dict(p2["meta"], releve_le=None)
            n2 = json.loads(json.dumps(dict(payload, meta=dict(payload["meta"], releve_le=None)), ensure_ascii=False))
            if prev.get("releve_le") and json.dumps(p2, sort_keys=True, ensure_ascii=False) == json.dumps(n2, sort_keys=True, ensure_ascii=False) \
                    and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and all((OUT_IMG / f.replace(".svg", ".png")).exists() for f in figs) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(dec, annees, cmp_, europe) \
                    and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches(figs):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; source Eurostat", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(dec, annees, cmp_, europe), encoding="utf-8-sig", newline="\n")
    import cairosvg
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dette_baisse.json, static/dette_baisse.csv, data/figures_baisse.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
