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
import hashlib
import html
import io
import json
import re
import statistics
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure as PF  # noqa: E402  (pied commun 11 px, versions téléphone ; phase B du volet 5, 11/10/2026)
import langue_generee as lg  # noqa: E402  -- comparaisons publiées à la précision affichée (organe commun)
import releve_jeu as rj  # noqa: E402  -- relevé daté par les seules données (organe commun, 17/10/2026)

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dette_baisse.json"
OUT_STATIC = ROOT / "static" / "dette_baisse.json"
OUT_CSV = ROOT / "static" / "dette_baisse.csv"
OUT_FIGURES = ROOT / "data" / "figures_baisse.json"
OUT_IMG = ROOT / "static" / "img"
DYN = ROOT / "data" / "dette_dynamique.json"
MONDE = ROOT / "data" / "dette_monde.json"
PAGES = [ROOT / "content" / "dette-publique-peut-elle-baisser" / "_index.md", ROOT / "content" / "dette-publique-peut-elle-baisser" / "_index.en.md"]
# Formules interdites dans les deux pages (contre-expertise OPTIMUM-24, Q4) : l'écart de la dernière année est un écart comptable
# constaté pour une année, jamais un montant d'économies ni un manque à combler.
INTERDITS = [r"il manque", r"économies? à (réaliser|faire|trouver)", r"manque à combler", r"savings? to be (made|found)",
             r"\bshortfall\b", r"\bmissing\b", r"charge d'intérêts cumulée"]
PAGE_URL = "stephane-lalut.com/dette-publique-peut-elle-baisser/"
PAGE_URL_EN = "stephane-lalut.com/en/can-public-debt-come-down/"

TOL = 0.11            # ratios publiés à une décimale ; le solde primaire additionne deux arrondis
SEUIL_DETTE = 90.0    # dette de départ des pays comparés à la France, % du PIB
SEUILS_SENSIBILITE = (80.0, 100.0)   # le même groupe à d'autres seuils : la page dit ce qui change
SEUIL_PIB = 35.0      # croissance nominale annuelle au-delà : hyperinflation ou rupture du PIB, fenêtre écartée
FORTE_BAISSE = 15.0   # points de PIB en dix ans
# Section « Dans la zone euro » (#zone-euro, 17/10/2026 ; arbitrage anthropie-site-20261017-005433, piste 2) : membres de la
# zone euro au 1er janvier 2026 (21 pays, Bulgarie comprise ; AMECO publie l'agrégat EA21). Comparaison des membres ACTUELS sur
# toute la fenêtre : la page le dit (Croatie entrée en 2023, Bulgarie en 2026).
ZONE_EURO = ("AT", "BE", "BG", "CY", "DE", "EE", "EL", "ES", "FI", "FR", "HR", "IE", "IT", "LT", "LU", "LV", "MT", "NL", "PT", "SI", "SK")
# Témoin indépendant : solde primaire structurel de la Commission (AMECO 1.0.319.0.UBLGBPS, % du PIB potentiel), autre producteur,
# corrigé du cycle, qui n'entre pas dans le calcul. Extrait archivé ; l'empreinte change avec l'édition (geste manuel, deux fois
# par an : registre data/sources_maj.json, id « ameco-structurel »).
AMECO = ROOT / "scripts" / "sources_dette" / "ameco_ublgbps_2026-06-02.csv"
AMECO_SHA = "8f48c054cff8786b9a018f29553fa82330848d5b4d1cfe3992b84a237d10fd92"
AMECO_EDITION = {"fr": "printemps 2026", "en": "spring 2026"}
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


REJETES: dict = {}   # années-pays écartées par le témoin, gardées pour la seule variante « avec les pays écartés »


def panel():
    D = eurostat("gov_10dd_edpt1", na_item="GD", sector="S13", unit="MIO_NAC")
    Y = eurostat("gov_10dd_edpt1", na_item="B1GQ", sector="S1", unit="MIO_NAC")
    I = eurostat("gov_10a_main", na_item="D41PAY", sector="S13", unit="MIO_NAC")
    B = eurostat("gov_10a_main", na_item="B9", sector="S13", unit="MIO_NAC")
    pub = {k: eurostat("gov_10dd_edpt1", na_item=k, sector="S13", unit="PC_GDP") for k in ("GD", "B9", "D41PAY")}
    # Volume (comptes nationaux annuels, volumes chaînés) : scission comptable de la croissance nominale en volume et prix
    # (OPTIMUM-24, Q2). Absente pour une année : None, jamais zéro.
    V = eurostat("nama_10_gdp", na_item="B1GQ", unit="CLV10_MNAC")
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
            ligne = dict(pays=p, annee=a, dette=d1, dette_prec=d0, variation=d1 - d0, interets=interets,
                         encours=D[k] / 1000, encours_prec=D[k0] / 1000,
                         croissance=croissance, taux_croissance=interets + croissance, solde_primaire=pb,
                         flux_stock=sfa, taux_implicite=i * 100, croissance_nominale=g * 100, pib=Y[k] / 1000,
                         croissance_volume=((V[k] / V[k0] - 1) * 100) if (k in V and k0 in V) else None)
            e_d, e_pb = d1 - pub["GD"][k], pb - (pub["B9"][k] + pub["D41PAY"][k])
            if abs(e_d) > TOL or abs(e_pb) > TOL:
                ecartes.append(dict(pays=p, annee=a, motif="écart au ratio publié", ecart_dette=round(e_d, 2), ecart_solde_primaire=round(e_pb, 2)))
                REJETES.setdefault(p, {})[a] = ligne   # variante de sensibilité seulement (section zone euro), jamais dans un chiffre publié
                continue
            R.setdefault(p, {})[a] = ligne
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
             encours_depart=L[0]["encours_prec"], encours_fin=L[-1]["encours"],
             taux_implicite_moyen=s("taux_implicite") / n, dette_moyenne=s("dette_prec") / n)
    vol = [x["croissance_volume"] for x in L]
    f["croissance_volume_moyenne"] = sum(vol) / n if None not in vol else None
    f["prix_moyen"] = (sum(((1 + x["croissance_nominale"] / 100) / (1 + x["croissance_volume"] / 100) - 1) * 100 for x in L) / n
                       if None not in vol else None)
    if abs(f["variation"] - (f["taux_croissance"] + f["deficits_primaires"] + f["flux_stock"])) > 1e-6:
        fail("%s %d : la somme des termes ne rend pas la variation" % (f["pays"], a0))
    return f


def ameco() -> dict:
    """Solde primaire structurel (AMECO), {pays: {année: valeur}} ; refuse une pièce dont l'empreinte a changé."""
    if not AMECO.is_file():
        fail("piece absente : %s" % AMECO)
    b = AMECO.read_bytes()
    if hashlib.sha256(b).hexdigest() != AMECO_SHA:
        fail("empreinte changee : %s ; relire la piece, puis mettre a jour AMECO_SHA et SHA256SUMS" % AMECO.name)
    S = {}
    for r in csv.DictReader(l for l in b.decode("utf-8").splitlines() if not l.startswith("#")):
        S.setdefault(r["pays"], {})[int(r["annee"])] = float(r["solde_primaire_structurel"])
    if set(ZONE_EURO) - set(S):
        fail("AMECO : pays de la zone euro absents de l'extrait : %s" % sorted(set(ZONE_EURO) - set(S)))
    return S


# Rang structurel selon deux autres estimateurs du PIB potentiel (17/10/2026, test RANG_STRUCTUREL_OCDE_FMI, accord de
# l'auteur le 18/10) : OCDE, solde primaire sous-jacent (hors cycle et mesures ponctuelles, 17 membres de la zone euro) ;
# FMI, solde primaire corrigé du cycle seulement (21 membres). Extraits archivés ; témoins, aucun calcul n'en dépend.
SOURCES_DETTE = ROOT / "scripts" / "sources_dette"
TEMOINS_STRUCT = {"ocde": "ocde_EO119_NLGXQU.csv", "fmi": "fmi_FM2026-10_GGCBP.json"}
TEMOINS_ED = {"fr": dict(ocde="Perspectives économiques n° 119", fmi="Moniteur des finances publiques d’octobre 2026"),
              "en": dict(ocde="Economic Outlook No. 119", fmi="Fiscal Monitor, October 2026")}
ISO3 = dict(AT="AUT", BE="BEL", BG="BGR", CY="CYP", DE="DEU", EE="EST", EL="GRC", ES="ESP", FI="FIN", FR="FRA", HR="HRV",
            IE="IRL", IT="ITA", LT="LTU", LU="LUX", LV="LVA", MT="MLT", NL="NLD", PT="PRT", SI="SVN", SK="SVK")


def temoins_structurels() -> dict:
    """{"ocde"|"fmi": {pays: {année: % du PIB potentiel}}} ; refuse une pièce dont l'empreinte n'est pas celle de SHA256SUMS."""
    sums = {l.split()[1].lstrip("*"): l.split()[0] for l in (SOURCES_DETTE / "SHA256SUMS").read_text(encoding="utf-8").splitlines() if l.strip()}
    T = {}
    for cle, nomf in TEMOINS_STRUCT.items():
        b = (SOURCES_DETTE / nomf).read_bytes()
        if sums.get(nomf) != hashlib.sha256(b).hexdigest():
            fail("piece %s : empreinte differente de SHA256SUMS ; relire la piece" % nomf)
        inv = {v: k for k, v in ISO3.items()}
        if cle == "ocde":
            S = {}
            for r in csv.DictReader(b.decode("utf-8-sig").splitlines()):
                if r["MEASURE"] == "NLGXQU" and r["OBS_VALUE"] and r["REF_AREA"] in inv:
                    S.setdefault(inv[r["REF_AREA"]], {})[int(r["TIME_PERIOD"])] = float(r["OBS_VALUE"])
        else:
            v = json.loads(b.decode("utf-8"))["values"]["GGCBP_G01_PGDP_PT"]
            S = {p: {int(a): float(x) for a, x in v[ISO3[p]].items()} for p in ZONE_EURO if ISO3[p] in v}
        if "FR" not in S:
            fail("temoin %s : France absente" % cle)
        T[cle] = S
    return T


def rang_temoin(S: dict, a0: int, a1: int, sauf: tuple = ()) -> tuple[int, list, int]:
    """Rang de la France (plus bas solde moyen) à la précision affichée, ses ex aequo, et le nombre de pays comparés."""
    ans = [a for a in range(a0, a1 + 1) if a not in sauf]
    f = {"pays": [{"pays": p, "s": sum(S[p][a] for a in ans) / len(ans)} for p in ZONE_EURO
                  if p in S and all(a in S[p] for a in ans)]}
    r, ex = rang_bas(f, "s")
    return r, ex, len(f["pays"])


def zone_euro(R: dict, fin: int, S: dict, sauf: tuple = ()) -> dict:
    """Moyennes par pays de la zone euro sur cinq fenêtres : solde primaire, solde stabilisant, écart, taux implicite, croissance
    nominale (Eurostat, panel témoin) et solde primaire structurel (AMECO, témoin). Un pays dont une année manque (absente ou
    écartée par le témoin) sort de la fenêtre avec ses années : conservation contrôlée.

    Identité à ne pas oublier en écrivant la page : sur une fenêtre, l'écart moyen = (somme des autres ajustements - variation du
    ratio) / n. Il ne s'ajoute donc pas à la variation de la dette comme un second constat ; ce qui ne s'en déduit pas, c'est la
    séparation entre solde primaire et repère (taux et croissance).

    sauf : années retirées de chaque fenêtre (variante de sensibilité « sans 2020 »)."""
    fen = (("an", fin, fin), ("cinq", fin - 4, fin), ("dix", fin - 9, fin), ("av20", 2015, 2019), ("d2010", 2010, 2019))
    out = {}
    for cle, a0, a1 in fen:
        L, ecartes = [], []
        for p in ZONE_EURO:
            ans = [a for a in range(a0, a1 + 1) if a not in sauf]
            manq = [a for a in ans if a not in R.get(p, {})]
            if manq:
                ecartes.append(dict(pays=p, annees=manq))
                continue
            n = len(ans)
            xs = [R[p][a] for a in ans]
            m = lambda k: sum(x[k] for x in xs) / n  # noqa: E731
            sps = [S[p].get(a) for a in ans]
            L.append(dict(pays=p, solde_primaire=m("solde_primaire"), solde_stabilisant=m("taux_croissance"),
                          ecart=m("solde_primaire") - m("taux_croissance"), taux_implicite=m("taux_implicite"),
                          croissance_nominale=m("croissance_nominale"), solde_structurel=(sum(sps) / n if None not in sps else None)))
        if len(L) + len(ecartes) != len(ZONE_EURO):
            fail("zone euro %d-%d : conservation rompue" % (a0, a1))
        if not any(d["pays"] == "FR" for d in L):
            fail("zone euro %d-%d : France absente" % (a0, a1))
        med = {k: statistics.median(d[k] for d in L) for k in ("solde_primaire", "solde_stabilisant", "ecart", "taux_implicite", "croissance_nominale")}
        sl = [d for d in L if d["solde_structurel"] is not None]
        med["solde_structurel"] = statistics.median(d["solde_structurel"] for d in sl) if sl else None
        out[cle] = dict(debut=a0, fin=a1, n=len(L), n_structurel=len(sl), pays=sorted(L, key=lambda d: d["solde_primaire"]),
                        ecartes=ecartes, medianes=med)
    return out


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
                   taux_implicite=FR[a]["taux_implicite"], croissance_nominale=FR[a]["croissance_nominale"],
                   croissance_volume=FR[a]["croissance_volume"], pib=FR[a]["pib"])
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
    A["stab_min"] = signe(min(stabs)); A["stab_min_annee"] = str(annees[lg.position_unique(stabs, 1, maxi=False, quoi="solde stabilisant minimal")]["annee"])
    A["stab_max"] = signe(max(stabs)); A["stab_max_annee"] = str(annees[lg.position_unique(stabs, 1, quoi="solde stabilisant maximal")]["annee"])
    # Section « La dette française est-elle soutenable ? » (#soutenable, 03/10/2026 ; arbitrage ENTRANTE_2026-10-03_Test_5_Questions, point 4)
    creux_ti = lg.extremum(annees, lambda r: r["taux_implicite"], 1, maxi=False)
    A["ti_creux"] = fr(creux_ti["taux_implicite"]); A["ti_creux_annee"] = str(creux_ti["annee"])
    A["var_derniere"] = fr(abs(last["variation"]))
    # Quatrième tour (document de travail de l'OFCE, E9) : écart au solde stabilisant de l'avant-dernière année.
    prec = annees[-2]
    A["annee_prec"] = str(prec["annee"]); A["ecart_prec"] = fr(abs(prec["ecart"]))
    rg_pos = sum(1 for r in annees if lg.depasse(r["taux_implicite"], r["croissance_nominale"], 1))
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
        # Phase B (OPTIMUM-24, B2) : taux et croissance séparés, en taux (les contributions en points dépendent aussi du
        # niveau de la dette), et la croissance nominale scindée en volume et prix.
        A[c + "int"] = signe(f["interets"]); A[c + "cr"] = signe(f["croissance"])
        A[c + "ti"] = fr(f["taux_implicite_moyen"], 2); A[c + "g"] = fr(f["croissance_nominale_moyenne"])
        A[c + "dm"] = fr(f["dette_moyenne"], 0)
        A[c + "rg"] = signe(f["taux_implicite_moyen"] - f["croissance_nominale_moyenne"])
        A[c + "gv"] = fr(f["croissance_volume_moyenne"]) if f["croissance_volume_moyenne"] is not None else "—"
        A[c + "gp"] = fr(f["prix_moyen"]) if f["prix_moyen"] is not None else "—"
    # Les trois baisses (OPTIMUM-24, B1) : hiérarchie mesurée des contributions, contrôle arithmétique.
    rap = [-f["taux_croissance"] / -f["deficits_primaires"] for f in haut]
    A["cmp_exc_rapport_min"] = fr(min(rap)); A["cmp_exc_rapport_max"] = fr(max(rap))
    A["cmp_exc_tc_min"] = fr(min(-f["taux_croissance"] for f in haut)); A["cmp_exc_tc_max"] = fr(max(-f["taux_croissance"] for f in haut))
    A["cmp_exc_sp_min"] = fr(min(-f["deficits_primaires"] for f in haut)); A["cmp_exc_sp_max"] = fr(max(-f["deficits_primaires"] for f in haut))
    tcs = [-(f["taux_croissance"] + f["flux_stock"]) for f in haut]
    A["cmp_exc_tcsfa_min"] = fr(min(tcs)); A["cmp_exc_tcsfa_max"] = fr(max(tcs))
    A["cmp_exc_ti_min"] = fr(min(f["taux_implicite_moyen"] for f in haut), 2); A["cmp_exc_ti_max"] = fr(max(f["taux_implicite_moyen"] for f in haut), 2)
    A["cmp_exc_g_min"] = fr(min(f["croissance_nominale_moyenne"] for f in haut)); A["cmp_exc_g_max"] = fr(max(f["croissance_nominale_moyenne"] for f in haut))
    gv = [f["croissance_volume_moyenne"] for f in haut if f["croissance_volume_moyenne"] is not None]
    gp = [f["prix_moyen"] for f in haut if f["prix_moyen"] is not None]
    if len(gv) != len(haut) or len(gp) != len(haut):
        fail("pays en baisse : volume du PIB absent (scission volume et prix impossible)")
    A["cmp_exc_gv_min"] = fr(min(gv)); A["cmp_exc_gv_max"] = fr(max(gv)); A["cmp_exc_gp_min"] = fr(min(gp)); A["cmp_exc_gp_max"] = fr(max(gp))
    dmax = lg.extremum(cmp_, lambda f: f["dette_moyenne"], 0)
    A["cmp_dm_max_pays"] = art(dmax["pays"]); A["cmp_dm_max"] = fr(dmax["dette_moyenne"], 0)
    # Dernière décennie : où se concentre l'allègement (contre-expertise PRO-20261003-064640, B2)
    d3 = dec[2]
    an3 = [r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]]
    trios = [an3[k:k + 3] for k in range(len(an3) - 2)]
    creux = lg.extremum(trios, lambda t: sum(r["solde_stabilisant"] for r in t), 1, maxi=False)
    tc_creux = sum(r["solde_stabilisant"] for r in creux)
    A["d3_creux_lib"] = "%d-%d" % (creux[0]["annee"], creux[-1]["annee"]); A["d3_creux_abs"] = fr(abs(tc_creux))
    A["d3_reste"] = signe(d3["taux_croissance"] - tc_creux); A["d3_reste_n"] = lettres(len(an3) - 3)
    A["d3_creux_g"] = fr(sum(r["croissance_nominale"] for r in creux) / 3)
    A["d3_creux_gv"] = fr(sum(r["croissance_volume"] for r in creux) / 3)
    A["d3_creux_rebond"] = str(creux[0]["annee"]); A["d3_creux_rebond_gv"] = fr(creux[0]["croissance_volume"])
    # Écart de la dernière année en milliards d'euros (OPTIMUM-24, Q4) : écart comptable × PIB de l'année, jamais saisi.
    A["ecart_md"] = milliers(abs(last["ecart"]) / 100 * last["pib"]); A["pib_dernier_md"] = milliers(last["pib"])
    A["point_md"] = milliers(last["pib"] / 100)   # un point de PIB de la dernière année, en milliards (panel « après », repère d'échelle)
    pic = lg.extremum(an3, lambda r: r["solde_stabilisant"], 1)
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
        ("dernière décennie : les déficits primaires font plus que toute la hausse", lg.depasse(d3["deficits_primaires"], d3["variation"], 1)),
        # --- les deux décennies précédentes
        ("première décennie : l'effet taux-croissance pousse la dette, le solde primaire pèse peu (moins de 5 points)",
         d1["taux_croissance"] > 5 and abs(d1["deficits_primaires"]) < 5),
        ("première décennie : la dette monte", d1["variation"] > 0),
        ("deuxième décennie : taux-croissance et déficits poussent ensemble, les déficits dominent (plus du double)",
         d2["taux_croissance"] > 0 and d2["deficits_primaires"] > 2 * d2["taux_croissance"]),
        ("deuxième décennie : la plus forte hausse des trois", lg.depasse(d2["variation"], max(d1["variation"], d3["variation"]))),
        ("les déficits primaires cumulés croissent d'une décennie à l'autre", lg.depasse(d2["deficits_primaires"], d1["deficits_primaires"]) and lg.depasse(d3["deficits_primaires"], d2["deficits_primaires"])),
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
         lg.extremum(annees, lambda r: r["solde_stabilisant"], 1)["croissance_nominale"] < 0),
        ("le solde stabilisant le plus bas est une année de forte croissance nominale (plus de 5 %)",
         lg.extremum(annees, lambda r: r["solde_stabilisant"], 1, maxi=False)["croissance_nominale"] > 5),
        ("moins d'une année sur deux au-dessus du solde stabilisant", sum(1 for r in annees if r["ecart"] >= 0) * 2 < len(annees)),
        # --- section #soutenable et « Ce qu'il faut retenir » (03/10/2026)
        ("dernière année : le ratio n'est pas stabilisé, il monte", last["variation"] > 0),
        ("le taux implicite « remonte » : son creux date de 2019 ou après et la dernière année le dépasse d'au moins 0,5 point",
         lg.extremum(annees, lambda r: r["taux_implicite"], 1, maxi=False)["annee"] >= 2019
         and last["taux_implicite"] > min(r["taux_implicite"] for r in annees) + 0.5),
        ("la croissance nominale « retombe » : la dernière année est sous la moyenne de 2021-2023 d'au moins 3 points",
         sum(r["croissance_nominale"] for r in annees if 2021 <= r["annee"] <= 2023) / 3 - last["croissance_nominale"] > 3),
        ("bloc de confrontation (OFCE, document de travail) : en 2024, solde sous le repère, « comme » les 2,1 points de l'OFCE (à 0,5 près)",
         annees[-2]["annee"] == 2024 and annees[-2]["ecart"] < 0 and abs(-annees[-2]["ecart"] - 2.1) < 0.5),
        ("bloc de confrontation (Trésor-Éco n° 403) : l'écart de la dernière année est « comme » les 3 points du Trésor (à 0,5 près)",
         abs(-last["ecart"] - 3.0) < 0.5),
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
        ("pays comparés : tous les autres pays partaient d'une dette plus élevée que la France", all(lg.depasse(f["dette_depart"], fr_c["dette_depart"]) for f in cmp_ if f["pays"] != "FR")),
        ("pays comparés : Grèce, Chypre et Portugal sont dans le groupe en excédent (le texte nomme leurs programmes d'assistance)",
         {"EL", "CY", "PT"} == {f["pays"] for f in haut}),
        ("pays comparés : la croissance nominale moyenne des pays en excédent dépasse celle de la France",
         all(lg.depasse(f["croissance_nominale_moyenne"], fr_c["croissance_nominale_moyenne"]) for f in haut)),
        # --- contre-expertise PRO-20261003-064640
        ("B1 : dans les pays en excédent, le montant de la dette n'a pas diminué alors que le ratio baissait",
         all(f["encours_fin"] >= f["encours_depart"] for f in haut)),
        ("B1 : au Portugal, l'encours augmente de plus de 10 % pendant que le ratio baisse",
         any(f["pays"] == "PT" and f["encours_fin"] > 1.1 * f["encours_depart"] and f["variation"] < 0 for f in haut)),
        ("B2 : l'allègement taux-croissance de la décennie tient à trois années consécutives, les autres l'alourdissent",
         sum(r["solde_stabilisant"] for r in lg.extremum([[r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]][k:k + 3] for k in range(8)],
                                                   lambda t: sum(r["solde_stabilisant"] for r in t), 1, maxi=False)) < d3["taux_croissance"]),
        ("B2 : l'année où l'effet taux-croissance pousse le plus la dette est 2020 et il y est positif",
         lg.extremum((r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]), lambda r: r["solde_stabilisant"], 1)["annee"] == 2020
         and next(r for r in annees if r["annee"] == 2020)["solde_stabilisant"] > 0),
        ("B3 : à 80 %, un seul pays ajouté connaît une baisse de 15 points avec un déficit primaire moyen (la Slovénie)",
         [f["pays"] for f in europe["sensibilite_seuil"]["80"] if f["pays"] not in {c["pays"] for c in cmp_}
          and f["variation"] <= -FORTE_BAISSE and f["solde_primaire_moyen"] < 0] == ["SI"]),
        ("B2 : les trois années les plus favorables de la décennie sont 2021-2023 (le texte parle du rebond et de l'inflation)",
         [r["annee"] for r in lg.extremum([[r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]][k:k + 3] for k in range(8)],
                                  lambda t: sum(r["solde_stabilisant"] for r in t), 1, maxi=False)] == [2021, 2022, 2023]),
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
        # --- phase B (OPTIMUM-24) : hiérarchie des ressorts, taux et croissance séparés
        ("B1 : dans chaque pays en baisse, l'effet des taux et de la croissance dépasse la contribution de l'excédent primaire",
         all(-f["taux_croissance"] > -f["deficits_primaires"] > 0 for f in haut)),
        ("B1 : « environ deux fois » : le rapport entre les deux contributions est compris entre 1,7 et 2,4 dans chaque pays en baisse",
         all(1.7 <= f["taux_croissance"] / f["deficits_primaires"] <= 2.4 for f in haut)),
        ("B1 : contrôle arithmétique : effet des taux et de la croissance plus autres ajustements reste négatif dans chaque pays en baisse",
         all(f["taux_croissance"] + f["flux_stock"] < 0 for f in haut)),
        ("B2 : la France a le taux implicite moyen le plus bas du groupe (« leur taux implicite n'était pas plus bas »)",
         fr_c["taux_implicite_moyen"] == min(f["taux_implicite_moyen"] for f in cmp_)),
        ("B2 : la croissance en volume moyenne de chaque pays en baisse dépasse celle de la France",
         all(f["croissance_volume_moyenne"] is not None and fr_c["croissance_volume_moyenne"] is not None
             and lg.depasse(f["croissance_volume_moyenne"], fr_c["croissance_volume_moyenne"]) for f in haut)),
        ("B2 : la Grèce a la dette moyenne la plus élevée du groupe (le texte : « une dette si élevée »)",
         lg.extremum(cmp_, lambda f: f["dette_moyenne"], 0)["pays"] == "EL"),
        ("B2 : écart taux-croissance de la Grèce « à peine plus favorable » que celui de la France (moins d'un point d'écart), et le moins favorable des trois pays en baisse",
         any(f["pays"] == "EL" for f in haut)
         and 0 < (fr_c["taux_implicite_moyen"] - fr_c["croissance_nominale_moyenne"]) - next(f["taux_implicite_moyen"] - f["croissance_nominale_moyenne"] for f in haut if f["pays"] == "EL") < 1
         and next(f["taux_implicite_moyen"] - f["croissance_nominale_moyenne"] for f in haut if f["pays"] == "EL") == max(f["taux_implicite_moyen"] - f["croissance_nominale_moyenne"] for f in haut)),
        ("B2 : 2021-2023 : la première année est un rebond en volume (plus de 5 %), les deux suivantes doivent davantage aux prix qu'au volume",
         (lambda tr: tr[0]["croissance_volume"] > 5 and all((1 + r["croissance_nominale"] / 100) / (1 + r["croissance_volume"] / 100) - 1 > r["croissance_volume"] / 100 for r in tr[1:]))(
             lg.extremum([[r for r in annees if d3["debut"] <= r["annee"] <= d3["fin"]][k:k + 3] for k in range(8)], lambda t: sum(r["solde_stabilisant"] for r in t), 1, maxi=False))),
        ("B2 : la Grèce paie « à peu près le même taux » que la France (moins de 0,1 point d'écart de taux implicite moyen) et sa croissance nominale « dépasse à peine » la française (moins d'un point)",
         any(f["pays"] == "EL" and abs(f["taux_implicite_moyen"] - fr_c["taux_implicite_moyen"]) < 0.1
             and 0 < f["croissance_nominale_moyenne"] - fr_c["croissance_nominale_moyenne"] < 1 for f in cmp_)),
        ("solde stabilisant : il aurait fallu un excédent l'année du recul du PIB, un déficit l'aurait laissé stable l'année du rebond",
         max(r["solde_stabilisant"] for r in annees) > 0 > min(r["solde_stabilisant"] for r in annees)),
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
        log("Valeurs nouvelles : France %d-%d variation %+.2f, taux-croissance %+.2f, deficits primaires %+.2f, flux-stock %+.2f ; "
            "derniere annee %d : solde primaire %+.2f, solde stabilisant %+.2f ; pays : %s"
            % (d3["debut"], d3["fin"], d3["variation"], d3["taux_croissance"], d3["deficits_primaires"], d3["flux_stock"], last["annee"],
               last["solde_primaire"], last["solde_stabilisant"],
               ", ".join("%s %+.1f (tc %+.1f, sp %+.1f)" % (f["pays"], f["variation"], f["taux_croissance"], f["deficits_primaires"]) for f in cmp_)))
        fail("la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    return len(G)


def rang_bas(f: dict, cle: str, dec: int = 1) -> tuple[int, list]:
    """Rang de la France du plus bas au plus haut, à la précision affichée, et ses ex aequo."""
    return lg.rang({d["pays"]: d[cle] for d in f["pays"] if d[cle] is not None}, "FR", dec, decroissant=False)


def ze_fr(f: dict) -> dict:
    return next(d for d in f["pays"] if d["pays"] == "FR")


def sz(v: float, dec: int = 1) -> str:
    """Signe, sauf pour une valeur qui s'affiche nulle (« 0,0 » et non « +0,0 » ou « −0,0 »)."""
    return fr(0.0, dec) if round(v, dec) == 0 else signe(v, dec)


def rang_txt(f: dict, cle: str, dec: int = 1) -> str:
    """Rang du plus bas à la précision affichée (tableau du repli). Des pays affichés à égalité occupent ensemble une plage de
    places : on écrit la plage (« 1 à 3 »), jamais la seule meilleure place, qui laisserait croire au premier rang un pays
    troisième sur les valeurs non arrondies (contre-expertise anthropie-site-20261017-030435, point 8)."""
    r, ex = rang_bas(f, cle, dec)
    return str(r) if not ex else ("%d à %d" if LANG == "fr" else "%d to %d") % (r, r + len(ex))


def sous_fr(f: dict, cle: str, pays: list) -> list:
    """Parmi `pays`, ceux dont la moyenne `cle` est plus basse que celle de la France, à la précision affichée."""
    x = ze_fr(f)[cle]
    return [d for d in f["pays"] if d["pays"] in pays and lg.depasse(x, d[cle], 2 if cle == "taux_implicite" else 1)]


def affichage_ze(ze: dict, V: dict, T: dict) -> dict:
    """Jetons de la section #zone-euro (mêmes clés en français et en anglais). V : variantes de sensibilité (« complet » avec
    les années écartées par le témoin, « sans2020 ») ; T : témoins structurels OCDE et FMI."""
    A = {}
    d = ze["dix"]
    A["ze_fmi_egaux"] = enumere([art(p) for p in rang_temoin(T["fmi"], d["debut"], d["fin"])[1]])
    A["ze_ocde_ed"], A["ze_fmi_ed"] = TEMOINS_ED[LANG]["ocde"], TEMOINS_ED[LANG]["fmi"]
    for w, f in ze.items():
        p, x = "ze_%s_" % w, ze_fr(f)
        A[p + "lib"] = str(f["debut"]) if f["debut"] == f["fin"] else "%d-%d" % (f["debut"], f["fin"])
        A[p + "n"] = str(f["n"]); A[p + "n_sps"] = str(f["n_structurel"])
        A[p + "pb"] = sz(x["solde_primaire"]); A[p + "pb_rang"] = rang_txt(f, "solde_primaire")
        A[p + "stab"] = sz(x["solde_stabilisant"]); A[p + "ecart"] = sz(x["ecart"])
        A[p + "ecart_rang"] = rang_txt(f, "ecart")
        A[p + "sps"] = sz(x["solde_structurel"]) if x["solde_structurel"] is not None else "—"
        A[p + "sps_rang"] = rang_txt(f, "solde_structurel") if x["solde_structurel"] is not None else "—"
    f = ze["dix"]; x = ze_fr(f); m = f["medianes"]
    A["ze_lib"] = A["ze_dix_lib"]; A["ze_n"] = lettres(f["n"]); A["ze_total"] = lettres(len(ZONE_EURO))
    A["ze_fr_ti"] = fr(x["taux_implicite"], 2); A["ze_med_ti"] = fr(m["taux_implicite"], 2)
    A["ze_ti_moins_n"] = lettres(rang_bas(f, "taux_implicite", 2)[0] - 1)
    A["ze_fr_g"] = fr(x["croissance_nominale"]); A["ze_med_g"] = fr(m["croissance_nominale"])
    A["ze_fr_stab"] = sz(x["solde_stabilisant"]); A["ze_med_stab"] = sz(m["solde_stabilisant"])
    A["ze_fr_pb"] = signe(x["solde_primaire"]); A["ze_med_pb"] = signe(m["solde_primaire"])
    A["ze_fr_sps"] = signe(x["solde_structurel"]); A["ze_med_sps"] = signe(m["solde_structurel"])
    A["ze_ecartes"] = enumere([art(e["pays"]) for e in f["ecartes"]]); A["ze_ecartes_n"] = lettres(len(f["ecartes"]))
    A["ze_edition"] = AMECO_EDITION[LANG]
    A["ze_cinq_pire_n"] = lettres(rang_bas(ze["cinq"], "ecart")[0] - 1)
    A["ze_g_avec"] = enumere([art(p) for p in rang_bas(f, "croissance_nominale")[1]])
    exc = [e["pays"] for e in f["ecartes"]]
    ti_s, g_s = sous_fr(V["complet"]["dix"], "taux_implicite", exc), sous_fr(V["complet"]["dix"], "croissance_nominale", exc)
    A["ze_ti_ecartes_sous"] = enumere([art(d["pays"]) for d in ti_s])
    A["ze_g_ecartes_sous"] = enumere([art(d["pays"]) for d in g_s])
    A["ze_g_ecartes_val"] = fr(g_s[0]["croissance_nominale"]) if g_s else "—"
    return A


def gardes_ze(ze: dict, V: dict, T: dict) -> int:
    d, c, a, d10 = ze["dix"], ze["cinq"], ze["av20"], ze["d2010"]
    if "--mutation-struct" in sys.argv:   # témoin positif : solde sous-jacent OCDE de la France relevé de 3 points
        T = dict(T, ocde=dict(T["ocde"], FR={a: v + 3 for a, v in T["ocde"]["FR"].items()}))
    ro, rf = rang_temoin(T["ocde"], d["debut"], d["fin"]), rang_temoin(T["fmi"], d["debut"], d["fin"])
    vd, vs = V["complet"]["dix"], V["sans2020"]["dix"]
    exc = [e["pays"] for e in d["ecartes"]]
    stab_av = {x["pays"]: x["solde_stabilisant"] for x in a["pays"]}
    xd, xc = ze_fr(d), ze_fr(c)
    rb = lambda f, k, dec=1: rang_bas(f, k, dec)  # noqa: E731
    G = [
        ("zone euro, dix ans : au moins dix-huit pays comparés, deux au plus écartés", d["n"] >= 18 and len(d["ecartes"]) <= 2),
        ("zone euro, dix ans : la France a le solde primaire moyen le plus bas, sans ex aequo", rb(d, "solde_primaire") == (1, [])),
        ("zone euro, dix ans : la France a la croissance nominale moyenne la plus faible, à égalité à l'affichage avec un seul pays (nommé par le jeton ze_g_avec)",
         rb(d, "croissance_nominale")[0] == 1 and len(rb(d, "croissance_nominale")[1]) == 1),
        ("zone euro, dix ans : « l'un des plus bas » : au plus cinq pays ont un taux implicite moyen plus bas que la France",
         2 <= rb(d, "taux_implicite", 2)[0] - 1 <= 5),   # « seuls N pays ont payé moins » : pluriel, N de deux à cinq
        ("zone euro, dix ans : taux implicite français sous la médiane", not lg.depasse(xd["taux_implicite"], d["medianes"]["taux_implicite"], 2)
         and xd["taux_implicite"] < d["medianes"]["taux_implicite"]),
        ("zone euro, dix ans : repère « proche du pays médian » (moins d'un point d'écart)", abs(xd["solde_stabilisant"] - d["medianes"]["solde_stabilisant"]) < 1),
        ("zone euro, dix ans : solde primaire français inférieur d'au moins un point à la médiane", xd["solde_primaire"] < d["medianes"]["solde_primaire"] - 1),
        ("témoin AMECO, dix ans : solde primaire structurel le plus bas, sans ex aequo", xd["solde_structurel"] is not None and rb(d, "solde_structurel") == (1, [])),
        ("témoin AMECO, dix ans : tous les pays comparés ont leur solde structurel", d["n_structurel"] == d["n"]),
        ("cinq ans : solde primaire toujours le plus bas, sans ex aequo", rb(c, "solde_primaire") == (1, [])),
        ("cinq ans : « la France n'est plus en moyenne sous son repère » (écart affiché positif ou nul) et au moins deux pays ont un écart plus défavorable",
         rb(c, "ecart")[0] >= 3 and 0 <= lg.affichee(xc["ecart"]) < 2),   # < 2 : « point » au singulier dans la page
        ("cinq ans : témoin AMECO, solde structurel parmi les deux plus bas", xc["solde_structurel"] is not None and rb(c, "solde_structurel")[0] <= 2),
        ("avant 2020 : la France est le seul pays sous le repère en moyenne", [x["pays"] for x in a["pays"] if lg.affichee(x["ecart"]) < 0] == ["FR"]),
        ("2010-2019 : solde structurel le plus bas (témoin)", rb(d10, "solde_structurel") == (1, [])),
        ("pays écartés : chacun l'est pour une année absente du panel témoin (motif repris dans la page)", all(e["annees"] for e in d["ecartes"])),
        # Contre-expertise anthropie-site-20261017-030435 : chaque phrase qui dit « des pays comparés » est éprouvée contre la zone
        # entière (années écartées réintégrées), et la décennie contre l'année 2020.
        ("avec les pays écartés réintégrés : tous les membres comparés sur dix ans", vd["n"] == len(ZONE_EURO)),
        ("avec les pays écartés réintégrés : solde primaire français toujours le plus bas, sans ex aequo (dix ans et cinq ans)",
         rb(vd, "solde_primaire") == (1, []) and rb(V["complet"]["cinq"], "solde_primaire") == (1, [])),
        ("avec les pays écartés réintégrés : solde structurel français toujours le plus bas, sans ex aequo", rb(vd, "solde_structurel") == (1, [])),
        ("« seul <pays écarté> a eu une croissance plus faible » : un seul pays, et c'est un pays écarté",
         len(sous_fr(vd, "croissance_nominale", exc)) == 1 and len(sous_fr(vd, "croissance_nominale", [x["pays"] for x in vd["pays"]])) == 1),
        ("« comme <pays écarté>, hors du calcul » : au moins un pays écarté a un taux implicite plus bas", len(sous_fr(vd, "taux_implicite", exc)) >= 1),
        ("sans 2020 : solde primaire et solde structurel les plus bas, croissance nominale la plus faible, sans ex aequo",
         vs["n"] >= 18 and rb(vs, "solde_primaire") == (1, []) and rb(vs, "solde_structurel") == (1, []) and rb(vs, "croissance_nominale") == (1, [])),
        ("cinq ans : « la forte croissance nominale a abaissé le repère de tous les pays » par rapport aux cinq années d'avant 2020",
         all(x["pays"] in stab_av and x["solde_stabilisant"] < stab_av[x["pays"]] for x in c["pays"])),
        # Rang structurel selon l'OCDE et le FMI (accord de l'auteur, 18/10/2026) : la page dit « le plus bas des pays qu'elle
        # couvre » pour l'OCDE et « à égalité avec <ex aequo> » pour le FMI.
        ("témoin OCDE, dix ans : au moins quinze pays couverts, solde structurel français le plus bas, sans ex aequo", ro[2] >= 15 and ro[:2] == (1, [])),
        ("témoin FMI, dix ans : au moins dix-huit pays, la France en tête d'un groupe d'ex aequo à l'affichage (« à égalité avec »)",
         rf[2] >= 18 and rf[0] == 1 and len(rf[1]) >= 1),
    ]
    if "--mutation-ze" in sys.argv:   # témoin positif : la France perd son rang (solde primaire relevé de 3 points)
        xd["solde_primaire"] += 3
        G[1] = (G[1][0], rb(d, "solde_primaire") == (1, []))
    faux = [nom_ for nom_, ok in G if not ok]
    if faux:
        log("Zone euro, %s : France solde primaire %+.2f (mediane %+.2f), taux %.2f (mediane %.2f), croissance %.2f (mediane %.2f), structurel %s"
            % (A_lib(d), xd["solde_primaire"], d["medianes"]["solde_primaire"], xd["taux_implicite"], d["medianes"]["taux_implicite"],
               xd["croissance_nominale"], d["medianes"]["croissance_nominale"], xd["solde_structurel"]))
        fail("section zone euro : la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    return len(G)


def A_lib(f: dict) -> str:
    return "%d-%d" % (f["debut"], f["fin"])


# ------------------------------------------------------------------ figures

TXT = {
 "fr": dict(
  monte="fait monter le ratio", baisse="le fait baisser", var_leg="variation du ratio (somme des trois)",
  cols=["Taux et croissance", "Solde primaire", "Autres ajustements", "Variation du ratio"],
  unite="En points de PIB cumulés sur dix ans",
  points=" points", sous="%s → %s %% du PIB",
  dec_titre="France : ce qui a fait monter ou baisser le poids de la dette, décennie par décennie",
  dec_desc=("Pour chaque décennie, en points de PIB cumulés sur dix ans : effet des taux et de la croissance, contribution du solde "
            "primaire, autres ajustements, et leur somme, la variation du ratio de dette. %s : %s, %s, %s ; variation %s. %s : %s, %s, %s ; "
            "variation %s. %s : %s, %s, %s ; variation %s. Sur la dernière décennie, l'effet des taux et de la croissance fait baisser le "
            "ratio et les déficits primaires le font monter davantage."),
  dec_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), France, %s-%s",
  dec_note=("Décomposition comptable, non causale : les trois termes ne sont pas indépendants. Variation calculée sur les valeurs non "
            "arrondies ; la somme des contributions affichées peut différer de 0,1 point."),
  cmp_titre="%s pays à plus de %s %% de dette fin %s : ce qui a fait bouger leur ratio en dix ans",
  cmp_desc=("Pays dont la dette dépassait %s %% du PIB fin %s. Pour chaque pays, en points de PIB cumulés de %s : effet des taux et de la croissance, contribution du solde primaire "
            "(un excédent fait baisser le ratio, un déficit le fait monter), autres ajustements, et la variation du ratio, leur somme. "),
  cmp_desc_pays="%s : taux et croissance %s, solde primaire %s, autres ajustements %s, variation %s.",
  cmp_desc_fin=(" L'effet des taux et de la croissance fait baisser le ratio partout ; dans les trois pays où le ratio a nettement baissé, "
                "il pèse environ deux fois plus que leurs excédents primaires."),
  cmp_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), %s ; pays triés par variation du ratio",
  cmp_note=("Grèce, Chypre et Portugal ont reçu des financements officiels (2010-2018). Comparaison comptable : elle n'attribue "
            "la baisse à aucune politique. Variation calculée sur les valeurs non arrondies ; la somme des contributions affichées peut "
            "différer de 0,1 point."),
  stab_titre="France : le solde primaire observé et celui qui aurait stabilisé la dette",
  stab_desc=("Deux courbes annuelles de %s à %s, en %% du PIB : le solde primaire observé, positif %s fois (%s à %s), et le solde primaire qui "
             "aurait stabilisé le ratio de dette, qui va de %s en %s à %s en %s. En %s, le solde observé est de %s et le solde stabilisant de %s : "
             "un écart de %s points de PIB."),
  pc=" %", recul="recul du PIB", rebond="rebond du PIB",
  leg_obs="solde primaire observé", leg_stab="solde qui aurait stabilisé le ratio cette année-là, hors autres ajustements", leg_stab_x=210,
  ecart_lab="En %s, l'écart entre les deux courbes (pointillé) : %s points de PIB.",
  m_2020="%s, recul du PIB : repère %s %%", m_2021="%s, rebond du PIB : repère %s %%",
  m_fin="%s : observé %s %%, repère %s %%, écart %s points",
  stab_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), France, %s-%s",
  stab_note=("En % du PIB ; solde stabilisant = (taux implicite − croissance nominale) / (1 + croissance) × ratio dette/PIB de fin d'année précédente, "
             "hors autres ajustements (flux-stock). Un repère comptable de l'année, non un objectif."),
  licence_m="Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
  montre=[("decennies", "De décennie en décennie, le terme qui fait monter la dette française change ; sur la dernière, taux et "
                        "croissance l'ont fait baisser et les déficits primaires l'ont fait monter davantage."),
          ("comparaison", "Parmi les pays partis d'une dette au moins aussi élevée, l'effet des taux et de la croissance a fait baisser "
                          "le ratio partout ; là où le ratio a nettement baissé, il a pesé environ deux fois plus que les excédents primaires."),
          ("stabilisant", "Le solde primaire qui stabilise la dette change chaque année avec les taux et la croissance ; "
                          "le solde observé est resté le plus souvent en dessous.")]),
 "en": dict(
  monte="pushes the ratio up", baisse="pulls it down", var_leg="change in the ratio (sum of the three)",
  cols=["Interest and growth", "Primary balance", "Other adjustments", "Change in the ratio"],
  unite="In points of GDP cumulated over ten years",
  points=" points", sous="%s → %s%% of GDP",
  dec_titre="France: what pushed the weight of debt up or down, decade by decade",
  dec_desc=("For each decade, in points of GDP cumulated over ten years: effect of interest rates and growth, contribution of the primary "
            "balance, other adjustments, and their sum, the change in the debt ratio. %s: %s, %s, %s; change %s. %s: %s, %s, %s; "
            "change %s. %s: %s, %s, %s; change %s. Over the last decade, the interest-growth effect pulled the ratio down and primary "
            "deficits pushed it up by more."),
  dec_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), France, %s-%s",
  dec_note=("An accounting decomposition, not a causal one: the three terms are not independent. Change computed on unrounded "
            "values; the sum of the contributions shown may differ by 0.1 points."),
  cmp_titre="%s countries with debt above %s%% of GDP at end-%s: what moved their ratio in ten years",
  cmp_desc=("Countries with debt above %s%% of GDP at end-%s. For each country, in points of GDP cumulated over %s: the interest-growth effect, the contribution of the primary balance "
            "(a surplus pulls the ratio down, a deficit pushes it up), other adjustments, and the change in the ratio, their sum. "),
  cmp_desc_pays="%s: interest and growth %s, primary balance %s, other adjustments %s, change %s.",
  cmp_desc_fin=(" The interest-growth effect pulls the ratio down everywhere; in the three countries where the ratio fell markedly, "
                "it weighs about twice as much as their primary surpluses."),
  cmp_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), %s; countries sorted by change in the debt ratio",
  cmp_note=("Greece, Cyprus and Portugal received official financing (2010-2018). An accounting comparison: it attributes "
            "the fall to no policy. Change computed on unrounded values; the sum of the contributions shown may differ by 0.1 points."),
  stab_titre="France: the observed primary balance and the one that would have stabilised the debt",
  stab_desc=("Two annual lines from %s to %s, in %% of GDP: the observed primary balance, positive %s times (%s to %s), and the primary balance "
             "that would have stabilised the debt ratio, ranging from %s in %s to %s in %s. In %s, the observed balance was %s and the "
             "stabilising balance %s: a gap of %s points of GDP."),
  pc="%", recul="GDP fell", rebond="GDP rebound",
  leg_obs="observed primary balance", leg_stab="balance that would have stabilised the ratio that year, excluding other adjustments", leg_stab_x=215,
  ecart_lab="In %s, the gap between the two lines (dotted): %s points of GDP.",
  m_2020="%s, GDP fell: marker %s%%", m_2021="%s, GDP rebound: marker %s%%",
  m_fin="%s: observed %s%%, marker %s%%, gap %s points",
  stab_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), France, %s-%s",
  stab_note=("In % of GDP; stabilising balance = (implicit interest rate − nominal growth) / (1 + growth) × debt-to-GDP ratio at the end of the previous year, "
             "excluding other adjustments (stock-flow). An accounting marker for the year, not a target."),
  licence_m="Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
  montre=[("decennies", "From one decade to the next, the term pushing French debt up changes; over the last one, interest and growth "
                        "pulled it down and primary deficits pushed it up by more."),
          ("comparaison", "Among countries that started from debt at least as high, the interest-growth effect pulled the ratio down "
                          "everywhere; where the ratio fell markedly, it weighed about twice as much as primary surpluses."),
          ("stabilisant", "The primary balance that stabilises the debt changes every year with interest rates and growth; the observed "
                          "balance mostly stayed below it.")]),
}
TXT["fr"].update(
  ze_titre="Zone euro, %s : taux, croissance et solde primaire de la France",
  ze_desc=("Moyennes annuelles %s, %s pays de la zone euro, un point par pays, la France en orange. Taux implicite de la dette : "
           "France %s %%, médiane %s %%. Croissance du PIB nominal : France %s %%, médiane %s %%. Solde primaire : France %s %% "
           "du PIB, médiane %s %%. La France a le solde primaire le plus bas, l'une des deux croissances nominales les plus faibles et l'un des taux implicites les plus bas."),
  ze_lignes=[("taux_implicite", "Taux implicite de la dette", "intérêts / dette, en %", 2),
             ("croissance_nominale", "Croissance du PIB nominal", "par an, en %", 1),
             ("solde_primaire", "Solde primaire", "en % du PIB", 1)],
  ze_leg=("France", "autres pays de la zone euro", "médiane"), ze_unite="Moyennes annuelles %s",
  ze_fr="France %s", ze_med="médiane %s", ze_fr_m="France : %s", ze_med_m="Médiane : %s",
  ze_src="Eurostat gov_10dd_edpt1 (dette, PIB), gov_10a_main (B9, D41PAY), %s ; membres de la zone euro au 1er janvier 2026, hors %s (années rejetées par le contrôle)",
  ze_note=("Comparaison comptable : elle ne dit ni si l'écart vient des dépenses ou des recettes, ni quel ajustement serait souhaitable. "
           "Taux implicite = intérêts payés / dette de fin d'année précédente."))
TXT["en"].update(
  ze_titre="Euro area, %s: France's interest rate, growth and primary balance",
  ze_desc=("Annual averages %s, %s euro-area countries, one dot per country, France in orange. Implicit interest rate on debt: "
           "France %s%%, median %s%%. Nominal GDP growth: France %s%%, median %s%%. Primary balance: France %s%% "
           "of GDP, median %s%%. France has the lowest primary balance, one of the two weakest nominal growth rates and one of the lowest implicit interest rates."),
  ze_lignes=[("taux_implicite", "Implicit interest rate", "interest / debt, in %", 2),
             ("croissance_nominale", "Nominal GDP growth", "per year, in %", 1),
             ("solde_primaire", "Primary balance", "in % of GDP", 1)],
  ze_leg=("France", "other euro-area countries", "median"), ze_unite="Annual averages %s",
  ze_fr="France %s", ze_med="median %s", ze_fr_m="France: %s", ze_med_m="Median: %s",
  ze_src="Eurostat gov_10dd_edpt1 (debt, GDP), gov_10a_main (B9, D41PAY), %s; euro-area members at 1 January 2026, excluding %s (years rejected by the check)",
  ze_note=("An accounting comparison: it says neither whether the gap comes from spending or revenue, nor which adjustment would be "
           "desirable. Implicit rate = interest paid / debt at the end of the previous year."))
TXT["fr"]["montre"].append(("zone-euro", "Dans la zone euro, la France paie un taux implicite parmi les plus bas ; ce qui la distingue est une "
                                         "croissance nominale parmi les plus faibles et le solde primaire le plus bas."))
TXT["en"]["montre"].append(("zone-euro", "In the euro area, France pays one of the lowest implicit interest rates; what sets it apart is among the weakest "
                                         "nominal growth and the lowest primary balance."))
SUFFIXE = {"fr": "", "en": "-en"}
WM, FSM = PF.LARGEUR_M, PF.POLICE_M
AXE = "#8f8a84"


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def entete(h, ident, titre, desc):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h + 52, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
            '<text x="0" y="18" font-size="15" font-weight="600" fill="%s">%s</text>' % (INK, esc(titre))]


def blocs_pied(source, note, licence=None):
    return [(source, INK2, "pied-source"), (note, INK2, "pied-note"), (licence or LICENCES[LANG], MUTED, "pied-licence")]


def legende(e, items, y=36):
    x = 0
    for col, lib in items:
        e.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/>' % (x, y, col))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (x + 14, y + 9, INK2, esc(lib)))
        x += 14 + 6.0 * len(lib) + 18


def largeur(s: str, fs: float) -> float:
    return 0.56 * fs * len(s)


def place_valeur(v, xz, xe, gauche, droite, fs, txt):
    """Valeur au bout de la barre si elle tient dans la colonne, sinon de l'autre côté du zéro (côté vide de la ligne)."""
    w = largeur(txt, fs)
    if v >= 0:
        return (xe + 4, "start") if xe + 4 + w <= droite else (xz - 4, "end")
    return (xe - 4, "end") if xe - 4 - w >= gauche else (xz + 4, "start")


def bornes(vals, pas):
    vmax = max(0.0, max(vals)); vmin = min(0.0, min(vals))
    return -(int(-vmin / pas) + 1) * pas if vmin < 0 else 0, (int(vmax / pas) + 1) * pas if vmax > 0 else 0


def multiples(ident, titre, desc, lignes, source, note, pas=10):
    """Petits multiples (phase B, OPTIMUM-24 : « remplacer T, S et A par des expressions compréhensibles ») : une ligne par
    décennie ou par pays, quatre colonnes intitulées en mots, même échelle partout ; la dernière, en bleu (stock), est la
    variation du ratio, somme exacte des trois autres : l'addition se vérifie à l'œil.
    lignes : [(libellé, sous-libellé, [taux-croissance, solde primaire, autres ajustements, variation])]"""
    T = TXT[LANG]
    e = entete(0, ident, titre, desc)
    legende(e, [(ORANGE, T["monte"]), (GRIS, T["baisse"]), (BLEU, T["var_leg"])])
    e.append('<text x="0" y="64" font-size="11" fill="%s">%s</text>' % (MUTED, esc(T["unite"])))
    LAB, pad, RH, Y0 = 150, 10, 40, 100
    CW = (W - LAB) / 4
    vmin, vmax = bornes([v for _, _, vs in lignes for v in vs], pas)
    for j, col in enumerate(T["cols"]):
        x0c = LAB + j * CW
        e.append('<text x="%.1f" y="88" font-size="12" font-weight="600" fill="%s" text-anchor="middle">%s</text>' % (x0c + CW / 2, INK, esc(col)))
    yb = Y0 + RH * len(lignes)
    for j in range(4):
        x0c = LAB + j * CW
        X = lambda v, x0c=x0c: x0c + pad + (v - vmin) / (vmax - vmin) * (CW - 2 * pad)  # noqa: E731
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.2"/>' % (X(0), Y0 - 4, X(0), yb - 4, AXE))
    for k, (lib, sous, vs) in enumerate(lignes):
        y = Y0 + RH * k
        if k:
            e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (y - 4, W, y - 4, GRID))
        e.append('<text x="0" y="%d" font-size="12.5" font-weight="600" fill="%s">%s</text>' % (y + 13, INK, esc(lib)))
        e.append('<text x="0" y="%d" font-size="11" fill="%s">%s</text>' % (y + 28, BLEU, esc(sous)))
        for j, v in enumerate(vs):
            x0c = LAB + j * CW
            X = lambda v, x0c=x0c: x0c + pad + (v - vmin) / (vmax - vmin) * (CW - 2 * pad)  # noqa: E731
            col = BLEU if j == 3 else (ORANGE if v >= 0 else GRIS)
            xa, xb = sorted((X(0), X(v)))
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="16" fill="%s"/>' % (xa, y + 6, max(xb - xa, 0.8), col))
            s = signe(v)
            tx, anc = place_valeur(v, X(0), X(v), x0c + 2, x0c + CW - 2, 11, s)
            e.append('<text x="%.1f" y="%d" font-size="11" font-weight="600" fill="%s" text-anchor="%s">%s</text>' % (tx, y + 18, INK, anc, s))
    return PF.pied(e, yb + 6, W, blocs_pied(source, note), GRID)


def multiples_m(ident, titre, svg_d, lignes, source, note, pas=10):
    """Version téléphone : une décennie ou un pays à la fois, trois barres nommées en mots, la variation dans l'intitulé."""
    T = TXT[LANG]
    desc = html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d, re.S).group(1))
    e, y = PF.tete_mobile(ident, titre, desc, INK, FONT)
    for col, lib in ((ORANGE, T["monte"]), (GRIS, T["baisse"])):
        y += 20
        e.append('<rect x="0" y="%.1f" width="11" height="11" fill="%s"/>' % (y - 10, col))
        e.append('<text x="17" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, INK2, esc(lib)))
    for l in PF.coupe(T["unite"], 38):
        y += 19
        e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, MUTED, esc(l)))
    BX0, BX1 = 140, WM - 4
    vmin, vmax = bornes([v for _, _, vs in lignes for v in vs[:3]], pas)
    X = lambda v: BX0 + (v - vmin) / (vmax - vmin) * (BX1 - BX0)  # noqa: E731
    for lib, sous, vs in lignes:
        y += 16
        e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (y - 4, WM, y - 4, GRID))
        y += 18
        e.append('<text x="0" y="%.1f" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc("%s : %s%s" % (lib, signe(vs[3]), T["points"])
                                                                                                          if LANG == "fr" else "%s: %s%s" % (lib, signe(vs[3]), T["points"]))))
        y += 18
        e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, BLEU, esc(sous)))
        y0 = y + 8
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2"/>' % (X(0), y0, X(0), y0 + 3 * 21 - 3, AXE))
        for j in range(3):
            v = vs[j]
            yy = y0 + 21 * j
            e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (yy + 13, FSM, INK2, esc(T["cols"][j])))
            xa, xb = sorted((X(0), X(v)))
            e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="14" fill="%s"/>' % (xa, yy + 2, max(xb - xa, 0.8), ORANGE if v >= 0 else GRIS))
            s = signe(v)
            tx, anc = place_valeur(v, X(0), X(v), BX0 - 2, WM, FSM, s)
            e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%s</text>' % (tx, yy + 13, FSM, INK, anc, s))
        y = y0 + 3 * 21
    return PF.pied_mobile(e, y + 10, blocs_pied(source, note, T["licence_m"]), GRID)


def lignes_dec(dec, A):
    T = TXT[LANG]
    return [(A["d%d_lib" % k], T["sous"] % (A["d%d_dette_deb" % k], A["d%d_dette_fin" % k]),
             [f["taux_croissance"], f["deficits_primaires"], f["flux_stock"], f["variation"]]) for k, f in enumerate(dec, 1)]


def lignes_cmp(cmp_, A):
    T = TXT[LANG]
    return [(nom(f["pays"]), T["sous"] % (fr(f["dette_depart"]), fr(f["dette_fin"])),
             [f["taux_croissance"], f["deficits_primaires"], f["flux_stock"], f["variation"]]) for f in cmp_]


def textes_dec(A):
    T = TXT[LANG]
    desc = (T["dec_desc"]
            % tuple(x for k in (1, 2, 3) for x in (A["d%d_lib" % k], A["d%d_tc" % k], A["d%d_def" % k], A["d%d_sfa" % k], A["d%d_var" % k])))
    return T["dec_titre"], desc, T["dec_src"] % (A["annee_debut"], A["annee_fin"]), T["dec_note"]


def textes_cmp(cmp_, A):
    T = TXT[LANG]
    titre = T["cmp_titre"] % (A["cmp_n_maj"], A["seuil_dette"], A["cmp_veille"])
    desc = (T["cmp_desc"] % (A["seuil_dette"], A["cmp_veille"], A["cmp_lib"])
            + " ".join(T["cmp_desc_pays"] % (nom(f["pays"]), signe(f["taux_croissance"]), signe(f["deficits_primaires"]), signe(f["flux_stock"]), signe(f["variation"])) for f in cmp_)
            + T["cmp_desc_fin"])
    return titre, desc, T["cmp_src"] % A["cmp_lib"], T["cmp_note"]


def fig_decennies(dec, A):
    titre, desc, src, note = textes_dec(A)
    return multiples("bd", titre, desc, lignes_dec(dec, A), src, note)


def fig_comparaison(cmp_, A):
    titre, desc, src, note = textes_cmp(cmp_, A)
    return multiples("bc", titre, desc, lignes_cmp(cmp_, A), src, note, 20)


def stab_desc(A):
    T = TXT[LANG]
    return (T["stab_desc"]
            % (A["annee_debut"], A["annee_fin"], A["exc_n"], A["exc_premiere"], A["exc_derniere"], A["stab_min"], A["stab_min_annee"],
               A["stab_max"], A["stab_max_annee"], A["annee_fin"], A["pb_dernier"], A["stab_dernier"], A["ecart_dernier"]))


def fig_stabilisant(annees, A):
    H, X0, X1, TOP, BAS = 320, 40, W - 10, 84, 290
    T = TXT[LANG]
    e = entete(H, "bs", T["stab_titre"], stab_desc(A))
    vals = [r[k] for r in annees for k in ("solde_primaire", "solde_stabilisant")]
    # Une graduation de marge sous le minimum : l'étiquette du rebond se pose SOUS son point, sans croiser les courbes.
    vmax, vmin = (int(max(vals) / 2) + 1) * 2, -(int(-min(vals) / 2) + 2) * 2

    def Y(v):
        return BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)

    n = len(annees)
    X = lambda k: X0 + (X1 - X0) * (k + 0.5) / n  # noqa: E731
    for g in range(vmin, vmax + 1, 2):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(g) + 4, MUTED, (signe(g, 0) if g else "0") + T["pc"]))
    for cle, col, larg in (("solde_stabilisant", GRIS, 2.2), ("solde_primaire", ORANGE, 2.6)):
        pts = " ".join("%.1f,%.1f" % (X(k), Y(r[cle])) for k, r in enumerate(annees))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (pts, col, larg))
    for k, r in enumerate(annees):
        if r["annee"] % 5 == 0 or k == n - 1:
            e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="middle">%d</text>' % (X(k), BAS + 16, INK2, r["annee"]))
    # Les deux ruptures (année du repère le plus haut, recul du PIB ; le plus bas, rebond ; gardées), étiquetées À GAUCHE du point :
    # posée à droite, l'étiquette du rebond sortait du cadre (défaut B4 de la phase A).
    for r_, lib, dy in ((lg.extremum(annees, lambda r: r["solde_stabilisant"], 1), T["recul"], 4), (lg.extremum(annees, lambda r: r["solde_stabilisant"], 1, maxi=False), T["rebond"], 20)):
        k = annees.index(r_)
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (X(k), Y(r_["solde_stabilisant"]), GRIS))
        e.append('<text x="%.1f" y="%.1f" font-size="11" fill="%s" text-anchor="end">%d%s%s</text>'
                 % (X(k) - 7 + (12 if dy > 4 else 0), Y(r_["solde_stabilisant"]) + dy, INK2, r_["annee"], " : " if LANG == "fr" else ": ", esc(lib)))
    last = annees[-1]
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4" stroke-dasharray="3 3"/>'
             % (X(n - 1) + 6, Y(last["solde_stabilisant"]), X(n - 1) + 6, Y(last["solde_primaire"]), INK2))
    for cle, col in (("solde_stabilisant", GRIS), ("solde_primaire", ORANGE)):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (X(n - 1), Y(last[cle]), col))
    e.append('<line x1="0" y1="41" x2="18" y2="41" stroke="%s" stroke-width="2.6"/>' % ORANGE)
    e.append('<text x="23" y="45" font-size="11" fill="%s">%s</text>' % (INK2, esc(T["leg_obs"])))
    x2 = T["leg_stab_x"] - 40
    e.append('<line x1="%d" y1="41" x2="%d" y2="41" stroke="%s" stroke-width="2.2"/>' % (x2, x2 + 18, GRIS))
    e.append('<text x="%d" y="45" font-size="11" fill="%s">%s</text>' % (x2 + 23, INK2, esc(T["leg_stab"])))
    e.append('<text x="0" y="66" font-size="11" fill="%s">%s</text>' % (INK, esc(T["ecart_lab"] % (A["annee_fin"], A["ecart_dernier"]))))
    return PF.pied(e, H + 2, W, blocs_pied(T["stab_src"] % (A["annee_debut"], A["annee_fin"]), T["stab_note"]), GRID)


def fig_stabilisant_m(annees, A):
    T = TXT[LANG]
    e, y = PF.tete_mobile("bs-m", T["stab_titre"], stab_desc(A), INK, FONT)
    for col, larg, lib in ((ORANGE, 2.6, T["leg_obs"]), (GRIS, 2.2, T["leg_stab"])):
        for i, l in enumerate(PF.coupe(lib, 34)):
            y += 19
            if i == 0:
                e.append('<line x1="0" y1="%.1f" x2="16" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (y - 5, y - 5, col, larg))
            e.append('<text x="22" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, INK2, esc(l)))
    X0, X1, TOP = 46, WM - 6, y + 18
    BAS = TOP + 200
    vals = [r[k] for r in annees for k in ("solde_primaire", "solde_stabilisant")]
    vmax, vmin = (int(max(vals) / 4) + 1) * 4, -(int(-min(vals) / 4) + 1) * 4
    Y = lambda v: BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)  # noqa: E731
    n = len(annees)
    X = lambda k: X0 + (X1 - X0) * (k + 0.5) / n  # noqa: E731
    for g in range(vmin, vmax + 1, 4):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%s</text>' % (X0 - 5, Y(g) + 5, FSM, MUTED, (signe(g, 0) if g else "0") + T["pc"]))
    for cle, col, larg in (("solde_stabilisant", GRIS, 2.0), ("solde_primaire", ORANGE, 2.4)):
        pts = " ".join("%.1f,%.1f" % (X(k), Y(r[cle])) for k, r in enumerate(annees))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (pts, col, larg))
    marques = [annees[0], next(r for r in annees if r["annee"] == 2010), annees[-1]]
    for r in marques:
        k = annees.index(r)
        e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                 % (X(k), BAS + 19, FSM, INK2, "start" if k == 0 else ("end" if k == n - 1 else "middle"), r["annee"]))
    hi = lg.extremum(annees, lambda r: r["solde_stabilisant"], 1); lo = lg.extremum(annees, lambda r: r["solde_stabilisant"], 1, maxi=False)
    last = annees[-1]
    for r, cle, col in ((hi, "solde_stabilisant", GRIS), (lo, "solde_stabilisant", GRIS), (last, "solde_stabilisant", GRIS), (last, "solde_primaire", ORANGE)):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (X(annees.index(r)), Y(r[cle]), col))
    y = BAS + 26
    for texte in (T["m_2020"] % (hi["annee"], A["stab_max"]), T["m_2021"] % (lo["annee"], A["stab_min"]),
                  T["m_fin"] % (A["annee_fin"], A["pb_dernier"], A["stab_dernier"], A["ecart_dernier"])):
        for l in PF.coupe(texte, 36):
            y += 19
            e.append('<text x="0" y="%.1f" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y, FSM, INK, esc(l)))
    return PF.pied_mobile(e, y + 12, blocs_pied(T["stab_src"] % (A["annee_debut"], A["annee_fin"]), T["stab_note"], T["licence_m"]), GRID)


def ze_val(v, dec):
    return (fr(v, dec) if dec == 2 else signe(v, dec) if v < 0 else fr(v, dec)) + TXT[LANG]["pc"]


def textes_ze(ze, A):
    T, f = TXT[LANG], ze["dix"]
    m = f["medianes"]; x = ze_fr(f)
    desc = T["ze_desc"] % (A["ze_lib"], f["n"], fr(x["taux_implicite"], 2), fr(m["taux_implicite"], 2), fr(x["croissance_nominale"]),
                           fr(m["croissance_nominale"]), signe(x["solde_primaire"]), signe(m["solde_primaire"]))
    hors = enumere([nom(e["pays"]) for e in f["ecartes"]])
    src = T["ze_src"] % (A["ze_lib"], hors) if f["ecartes"] else T["ze_src"].split(" ; ")[0].split("; ")[0] % A["ze_lib"]
    return T["ze_titre"] % A["ze_lib"], desc, src, T["ze_note"]


def ze_echelle(vals, dec):
    pas = 0.5 if dec == 2 else 1.0
    lo, hi = min(vals), max(vals)
    return (int(lo / pas) - (1 if lo < 0 else 0)) * pas, (int(hi / pas) + (1 if hi > 0 else 0)) * pas


def fig_zone_euro(ze, A):
    T = TXT[LANG]
    titre, desc, src, note = textes_ze(ze, A)
    f = ze["dix"]; m = f["medianes"]
    e = entete(0, "bz", titre, desc)
    e.append('<circle cx="5" cy="41" r="5" fill="%s"/>' % ORANGE)
    e.append('<text x="15" y="45" font-size="11" fill="%s">%s</text>' % (INK2, esc(T["ze_leg"][0])))
    e.append('<circle cx="75" cy="41" r="4.5" fill="%s" fill-opacity="0.6"/>' % GRIS)
    e.append('<text x="85" y="45" font-size="11" fill="%s">%s</text>' % (INK2, esc(T["ze_leg"][1])))
    xl = 85 + 0.85 * largeur(T["ze_leg"][1], 11) + 16   # largeur() majore : sans ce facteur, un vide visible avant « pays médian »
    e.append('<line x1="%.1f" y1="34" x2="%.1f" y2="48" stroke="%s" stroke-width="2"/>' % (xl, xl, INK))
    e.append('<text x="%.1f" y="45" font-size="11" fill="%s">%s</text>' % (xl + 7, INK2, esc(T["ze_leg"][2])))
    e.append('<text x="0" y="66" font-size="11" fill="%s">%s</text>' % (MUTED, esc(T["ze_unite"] % A["ze_lib"])))
    LAB, X0, X1, Y0, RH = 200, 225, W - 20, 92, 78
    for k, (cle, lib, sous, dec) in enumerate(T["ze_lignes"]):
        y = Y0 + RH * k
        if k:
            e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (y - 6, W, y - 6, GRID))
        e.append('<text x="0" y="%d" font-size="12.5" font-weight="600" fill="%s">%s</text>' % (y + 30, INK, esc(lib)))
        e.append('<text x="0" y="%d" font-size="11" fill="%s">%s</text>' % (y + 45, MUTED, esc(sous)))
        vals = [d[cle] for d in f["pays"]]
        lo, hi = ze_echelle(vals, dec)
        X = lambda v, lo=lo, hi=hi: X0 + (v - lo) / (hi - lo) * (X1 - X0)  # noqa: E731
        ya = y + 36
        e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>' % (X0, ya, X1, ya, AXE))
        for v in (lo, hi):
            e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="%s">%s</text>'
                     % (X(v), ya + 30, MUTED, "start" if v == lo else "end", esc(ze_val(v, dec if dec == 2 else 0))))
        if lo < 0 < hi:   # zéro marqué ET étiqueté : sans étiquette, le trait se confondait avec la médiane
            e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.2"/>' % (X(0), ya - 9, X(0), ya + 9, AXE))
            e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="middle">0</text>' % (X(0), ya + 30, MUTED))
        for d in f["pays"]:
            if d["pays"] != "FR":
                e.append('<circle cx="%.1f" cy="%d" r="4.5" fill="%s" fill-opacity="0.6"/>' % (X(d[cle]), ya, GRIS))
        xm = X(m[cle])
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2"/>' % (xm, ya - 8, xm, ya + 8, INK))
        x = ze_fr(f)[cle]
        e.append('<circle cx="%.1f" cy="%d" r="6" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (X(x), ya, ORANGE))
        tf, tm = T["ze_fr"] % ze_val(x, dec), T["ze_med"] % ze_val(m[cle], dec)
        # Étiquettes centrées sur leur point, recentrées si elles sortent de la bande (France au-dessus, médiane en dessous).
        for txt, cx, yy, poids in ((tf, X(x), ya - 12, "600"), (tm, xm, ya + 21, "400")):
            w = largeur(txt, 11)
            cx = min(max(cx, X0 + w / 2), X1 - w / 2)
            e.append('<text x="%.1f" y="%d" font-size="11" font-weight="%s" fill="%s" text-anchor="middle">%s</text>' % (cx, yy, poids, INK, esc(txt)))
    return PF.pied(e, Y0 + RH * 3 - 2, W, blocs_pied(src, note), GRID)


def fig_zone_euro_m(ze, A, svg_d):
    T = TXT[LANG]
    titre, _, src, note = textes_ze(ze, A)
    desc = html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d, re.S).group(1))
    f = ze["dix"]; m = f["medianes"]
    e, y = PF.tete_mobile("bz-m", titre, desc, INK, FONT)
    for k, (forme, lib) in enumerate(zip(("fr", "autres", "med"), T["ze_leg"])):
        y += 20
        if forme == "fr":
            e.append('<circle cx="6" cy="%.1f" r="5.5" fill="%s"/>' % (y - 5, ORANGE))
        elif forme == "autres":
            e.append('<circle cx="6" cy="%.1f" r="5" fill="%s" fill-opacity="0.6"/>' % (y - 5, GRIS))
        else:
            e.append('<line x1="6" y1="%.1f" x2="6" y2="%.1f" stroke="%s" stroke-width="2"/>' % (y - 12, y + 2, INK))
        e.append('<text x="18" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, INK2, esc(lib)))
    y += 19
    e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, MUTED, esc(T["ze_unite"] % A["ze_lib"])))
    X0, X1 = 8, WM - 8
    for cle, lib, sous, dec in T["ze_lignes"]:
        y += 16
        e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (y - 4, WM, y - 4, GRID))
        y += 18
        e.append('<text x="0" y="%.1f" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(lib)))
        y += 18
        e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FSM, MUTED, esc(sous)))
        vals = [d[cle] for d in f["pays"]]
        lo, hi = ze_echelle(vals, dec)
        X = lambda v, lo=lo, hi=hi: X0 + (v - lo) / (hi - lo) * (X1 - X0)  # noqa: E731
        ya = y + 22
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>' % (X0, ya, X1, ya, AXE))
        for d in f["pays"]:
            if d["pays"] != "FR":
                e.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" fill-opacity="0.6"/>' % (X(d[cle]), ya, GRIS))
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (X(m[cle]), ya - 8, X(m[cle]), ya + 8, INK))
        e.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (X(ze_fr(f)[cle]), ya, ORANGE))
        for v in (lo, hi):
            e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%s</text>'
                     % (X(v), ya + 24, FSM, MUTED, "start" if v == lo else "end", esc(ze_val(v, dec if dec == 2 else 0))))
        y = ya + 24
        for txt in (T["ze_fr_m"] % ze_val(ze_fr(f)[cle], dec), T["ze_med_m"] % ze_val(m[cle], dec)):
            y += 20
            e.append('<text x="0" y="%.1f" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y, FSM, INK, esc(txt)))
    return PF.pied_mobile(e, y + 12, blocs_pied(src, note, T["licence_m"]), GRID)


def figures_m(dec, cmp_, annees, A, D):
    """Versions téléphone, contrôlées contre les versions détaillées (parité des valeurs en gras, police minimale)."""
    x = SUFFIXE[LANG]
    td, tc_ = textes_dec(A), textes_cmp(cmp_, A)
    sortie = {"dette-baisse-decennies%s-m.svg" % x: multiples_m("bd-m", td[0], D["dette-baisse-decennies%s.svg" % x], lignes_dec(dec, A), td[2], td[3]),
              "dette-baisse-comparaison%s-m.svg" % x: multiples_m("bc-m", tc_[0], D["dette-baisse-comparaison%s.svg" % x], lignes_cmp(cmp_, A), tc_[2], tc_[3], 20),
              "dette-baisse-stabilisant%s-m.svg" % x: fig_stabilisant_m(annees, A),
              "dette-baisse-zone-euro%s-m.svg" % x: fig_zone_euro_m(ZE_COURANT, A, D["dette-baisse-zone-euro%s.svg" % x])}
    for nom_, svg in sortie.items():
        ec = PF.parite(D[nom_.replace("-m.svg", ".svg")], svg, FSM)
        if ec:
            fail("%s : %s" % (nom_, " ; ".join(ec)))
        for h in PF.hors_cadre(svg, WM):
            log("  a verifier au rendu, %s : %s" % (nom_, h))
    for nom_, svg in D.items():
        if nom_.endswith(x + ".svg") and not nom_.endswith("-m.svg"):
            for h in PF.hors_cadre(svg, W):
                log("  a verifier au rendu, %s : %s" % (nom_, h))
    return sortie


def fiches(figs):
    out = {}
    for lang in ("fr", "en"):
        out[lang] = []
        for ident, montre in TXT[lang]["montre"]:
            f = "dette-baisse-%s%s" % (ident, SUFFIXE[lang])
            svg = figs[f + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            out[lang].append(dict(id=ident, fichier=f, titre=titre, montre=montre, source=PF.lire(svg, "pied-source"),
                                  precaution=PF.lire(svg, "pied-note")))
    return out


ZE_COURANT: dict = {}   # posé par main() : figures_m() garde sa signature


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
    for f in ZE_COURANT.values():
        for d in f["pays"]:
            for k in ("solde_primaire", "solde_stabilisant", "ecart", "taux_implicite", "croissance_nominale", "solde_structurel"):
                if d[k] is not None:
                    w.writerow(["zone_euro_moyennes", d["pays"], "%d-%d" % (f["debut"], f["fin"]), k, "%.3f" % d[k]])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    global ZE_COURANT
    fin, dec, annees, cmp_, europe, cons, R = calcul()
    S = ameco()
    ze = ZE_COURANT = zone_euro(R, fin, S)
    V = dict(complet=zone_euro({p: {**R.get(p, {}), **REJETES.get(p, {})} for p in set(R) | set(REJETES)}, fin, S),
             sans2020=zone_euro(R, fin, S, sauf=(2020,)))
    T = temoins_structurels()
    use("en")
    A_en = affichage(fin, dec, annees, cmp_, europe, cons)[0]
    A_en.update(affichage_ze(ze, V, T))
    use("fr")
    A, haut, bas, exc_ans = affichage(fin, dec, annees, cmp_, europe, cons)
    A.update(affichage_ze(ze, V, T))
    if set(A) != set(A_en):
        fail("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    n = gardes(fin, dec, annees, cmp_, europe, haut, bas, exc_ans) + gardes_ze(ze, V, T)
    # Une variation, deux pages (phase A du volet 5, B3) : la hausse du ratio de la dernière année doit être la même qu'au volet 4.
    if MONDE.is_file():
        m = json.loads(MONDE.read_text(encoding="utf-8"))
        frm = next((x for x in m["europe"] if x.get("code") == "FR"), None)
        if frm and m["affichage"].get("annee") == str(fin) and frm.get("var_ratio") is not None                 and abs(frm["var_ratio"] - annees[-1]["variation"]) > 0.005:
            fail("volet 4 et volet 5 : variation du ratio %d differente (%.3f contre %.3f)" % (fin, frm["var_ratio"], annees[-1]["variation"]))
    for pg in PAGES:
        src = pg.read_text(encoding="utf-8")
        trouves = [m_.group(0) for x in INTERDITS for m_ in re.finditer(x, src, re.I)]
        if trouves:
            fail("%s : formule interdite (ecart comptable lu comme un montant a trouver) : %s" % (pg.name, trouves))
    d3 = dec[2]
    log("France %s : dette %+.1f = taux-croissance %+.1f + deficits primaires %+.1f + flux-stock %+.1f ; %d pays compares ; %d annees-pays ecartees sur %d"
        % (A["d3_lib"], d3["variation"], d3["taux_croissance"], d3["deficits_primaires"], d3["flux_stock"], len(cmp_), cons["ecartees"], cons["annees_pays_calculables"]))
    figs = {}
    for lang, AA in (("fr", A), ("en", A_en)):
        use(lang)
        x = SUFFIXE[lang]
        figs["dette-baisse-decennies%s.svg" % x] = fig_decennies(dec, AA)
        figs["dette-baisse-comparaison%s.svg" % x] = fig_comparaison(cmp_, AA)
        figs["dette-baisse-stabilisant%s.svg" % x] = fig_stabilisant(annees, AA)
        figs["dette-baisse-zone-euro%s.svg" % x] = fig_zone_euro(ze, AA)
        figs.update(figures_m(dec, cmp_, annees, AA, figs))
    use("fr")
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), %d figures construites et controlees, rien ecrit." % (n, len(A), len(figs)))
        return 0
    payload = {"meta": {"releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "perimetre": "administrations publiques (S.13), SEC 2010, monnaie nationale, PIB de la notification de déficit et de dette",
                        "identite": "d_t - d_{t-1} = i/(1+g) d_{t-1} - g/(1+g) d_{t-1} - pb_t + sfa_t",
                        "definitions": {"taux_croissance": "effet cumulé des intérêts et de la croissance du PIB nominal sur le ratio, en points de PIB",
                                        "deficits_primaires": "déficits hors intérêts cumulés, en points de PIB (négatif : excédents)",
                                        "flux_stock": "variation de dette qui ne passe pas par le déficit ; résidu de l'identité",
                                        "solde_stabilisant": "solde primaire qui aurait laissé le ratio inchangé cette année-là, hors flux-stock : (i - g)/(1 + g) x d(t-1)",
                                        "zone_euro": "membres de la zone euro au 1er janvier 2026 ; moyennes annuelles par fenêtre ; solde_structurel = AMECO UBLGBPS (Commission européenne, édition %s, %% du PIB potentiel), témoin indépendant non utilisé dans le calcul" % AMECO_EDITION["fr"],
                                        "temoin": "ratios de dette et de solde primaire comparés à ceux publiés par Eurostat en %% du PIB ; tolérance %.2f point" % TOL}},
               "france": {"decennies": dec, "annees": annees}, "pays_dette_elevee": cmp_, "europe": europe, "zone_euro": ze, "conservation": cons, "affichage": A, "affichage_en": A_en}
    releve = payload["meta"]["releve_le"]
    # Bruit de calcul au 15e chiffre : le jeu se compare et s'écrit normalisé (organe commun releve_jeu.normalise, 19/10/2026).
    payload = rj.normalise(payload)
    licence = "CC BY 4.0 — compilation Stéphane Lalut ; sources Eurostat, Commission européenne (AMECO), OCDE, FMI"   # nomme les sources : un changement s'écrit (rj.sans_licence, 18/10/2026)
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev); p2.pop("releve_le", None); rj.sans_licence(p2, licence); p2["meta"] = dict(p2["meta"], releve_le=None)
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
    releve = rj.releve(OUT_DATA, payload, releve)   # le texte seul ne date pas les données
    payload["meta"]["releve_le"] = releve
    payload = {"releve_le": releve, "_licence": licence, **payload}
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
