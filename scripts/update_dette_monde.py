#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update_dette_monde.py -- comparaison internationale de la charge de la dette publique.

Ecrit la source unique data/dette_monde.json, sa copie endpoint static/dette_monde.json et
les figures static/img/dette-monde-*.svg de la page « Dette publique : pourquoi 100 % du PIB
ne pese pas partout de la meme facon ».

Cahier des charges : 06_PROMOTION/DOSSIER_PAGE_DETTE_INTERNATIONALE.md (depot D:/PRO), arrete
apres trois avis externes (29/09/2026). Quatre mots, quatre definitions :
  STOCK        = dette brute / PIB
  PRIX         = taux IMPLICITE = interets de l'annee t / dette de fin t-1 (convention de la BCE). Ce n'est PAS
                 l'« apparent cost » d'Eurostat (interets / dette MOYENNE de l'annee) : les deux sont proches,
                 non identiques -- d'ou le nom, fixe par la contre-expertise PRO-20260930-061613.
  CHARGE       = interets / recettes publiques
  TRANSMISSION = part de la dette a moins d'un an, ecart taux a 10 ans - prix
Identite EXACTE, verifiee pays par pays (assertion) :
  I_t/R_t = (D_{t-1}/Y_t) x (I_t/D_{t-1}) / (R_t/Y_t)

Trois niveaux de comparabilite, jamais melanges dans un meme calcul statistique :
  1. EUROPE (27 pays UE) -- Eurostat, administrations publiques S.13, SEC 2010, dette de
     Maastricht, montants en MONNAIE NATIONALE (une conversion en euros a deux dates fausse
     le prix des pays hors euro : defaut mesure le 29/09). Badge « strictement comparable ».
  2. AVANCES HORS UE (Etats-Unis, Japon, Royaume-Uni, Canada, Suisse, Norvege) -- OCDE,
     Economic Outlook : interets BRUTS (GGINTP), recettes (YRGT), PIB, passifs financiers
     bruts SCN (GGFLQ, pas la dette de Maastricht). Badge « comparable avec reserve ». La
     France est calculee aussi sur cette base, pour montrer l'ecart entre les deux sources.
  3. GRANDS EMERGENTS (Chine, Inde, Bresil, Afrique du Sud) -- FMI WEO (dette brute des
     administrations publiques) et Banque mondiale WDI (interets en % des recettes de
     l'administration CENTRALE). Badge « indicatif » ; aucun prix calcule.

Invariants (repris de update_dette_insee.py) :
  - toute garde en echec => exit 1, AUCUNE ecriture ;
  - les nombres affiches derivent de ce JSON (bloc « affichage », chaines precalculees ; « affichage_en »
    aux memes cles pour la page anglaise, figures anglaises suffixees -en, champs texte anglais « _en ») ;
  - sorties CONSOLE en ASCII pur (console Windows cp1252) ; les fichiers sont en UTF-8 accentue ;
  - statistiques descriptives (moindres carres simples) : jamais presentees comme causales.

Usage :
  python scripts/update_dette_monde.py            # ecrit tout
  python scripts/update_dette_monde.py --check    # fetch + gardes, rien ecrit
  python scripts/update_dette_monde.py --png      # + rendu PNG de controle (cairosvg)

Mise a jour : Eurostat (avril et octobre, notifications EDP), OCDE (Economic Outlook,
juin et decembre), FMI WEO (avril et octobre). Condition de mort du niveau 3 : s'il n'existe
toujours pas de source d'interets des administrations publiques pour les emergents au WEO
d'avril 2027, retirer ce niveau plutot que de le garder « indicatif » indefiniment.
"""
from __future__ import annotations

import json
import math
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dette_monde.json"
OUT_STATIC = ROOT / "static" / "dette_monde.json"
# CSV : demandé par l'avis du 30/09 (« plus exploitable qu'un JSON par un journaliste ou un enseignant »).
# Une ligne par pays et par niveau de comparabilité, les mêmes valeurs que la page, point décimal.
OUT_CSV = ROOT / "static" / "dette_monde.csv"
# Fiches « Réutiliser » (30/09, demande de l'auteur : figures réutilisables sous licence, comme les volets 1 et 2).
# Titre, source et précaution sont LUS DANS LE SVG produit : la fiche dit ce que l'image imprime, jamais autre chose.
OUT_FIGURES = ROOT / "data" / "figures_monde.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/dette-publique-comparaison-internationale/"

UE = "BE BG CZ DK DE EE IE EL ES FR HR IT CY LV LT LU HU MT NL AT PL PT RO SI SK FI SE".split()
# Membres de la zone euro L'ANNEE DES DONNEES (la Bulgarie n'y entre qu'en 2026).
EURO_PAR_AN = {
    "2024": set("BE DE EE IE EL ES FR HR IT CY LV LT LU MT NL AT PT SI SK FI".split()),
    "2025": set("BE DE EE IE EL ES FR HR IT CY LV LT LU MT NL AT PT SI SK FI".split()),
    "2026": set("BE BG DE EE IE EL ES FR HR IT CY LV LT LU MT NL AT PT SI SK FI".split()),
}
NOMS = {
    "BE": "Belgique", "BG": "Bulgarie", "CZ": "Tchéquie", "DK": "Danemark", "DE": "Allemagne",
    "EE": "Estonie", "IE": "Irlande", "EL": "Grèce", "ES": "Espagne", "FR": "France",
    "HR": "Croatie", "IT": "Italie", "CY": "Chypre", "LV": "Lettonie", "LT": "Lituanie",
    "LU": "Luxembourg", "HU": "Hongrie", "MT": "Malte", "NL": "Pays-Bas", "AT": "Autriche",
    "PL": "Pologne", "PT": "Portugal", "RO": "Roumanie", "SI": "Slovénie", "SK": "Slovaquie",
    "FI": "Finlande", "SE": "Suède",
    "USA": "États-Unis", "JPN": "Japon", "GBR": "Royaume-Uni", "CAN": "Canada", "CHE": "Suisse",
    "NOR": "Norvège", "FRA": "France (base OCDE)", "CHN": "Chine", "IND": "Inde", "BRA": "Brésil",
    "ZAF": "Afrique du Sud",
}
# Nom AVEC son article, pour la prose : la paire de faux jumeaux sort d'une règle, pas d'un choix ; si elle change,
# « la {pays} » écrit en dur donnerait « la Portugal ». Le générateur fournit donc le groupe nominal complet.
ARTICLE = {
    "BE": "la Belgique", "BG": "la Bulgarie", "CZ": "la Tchéquie", "DK": "le Danemark", "DE": "l'Allemagne",
    "EE": "l'Estonie", "IE": "l'Irlande", "EL": "la Grèce", "ES": "l'Espagne", "FR": "la France", "HR": "la Croatie",
    "IT": "l'Italie", "CY": "Chypre", "LV": "la Lettonie", "LT": "la Lituanie", "LU": "le Luxembourg",
    "HU": "la Hongrie", "MT": "Malte", "NL": "les Pays-Bas", "AT": "l'Autriche", "PL": "la Pologne",
    "PT": "le Portugal", "RO": "la Roumanie", "SI": "la Slovénie", "SK": "la Slovaquie", "FI": "la Finlande",
    "SE": "la Suède",
}
# -- locale anglaise (30/09/2026, page anglaise à venir) ------------------------------------------------------------
# Même architecture que update_dette_insee.py : UN calcul, DEUX présentations. Structure des champs texte du JSON :
#   - bloc « affichage_en » à côté de « affichage », AUX MÊMES CLÉS (vérifié : sinon échec, rien écrit) ;
#   - dans chaque ligne de pays (europe, avances, emergents, ecarts_allemagne.pays), le champ anglais se pose À CÔTÉ
#     du champ français, suffixé « _en » : nom -> nom_en, note -> note_en, badge -> badge_en ; idem
#     ecarts_allemagne.source -> source_en, meta.definitions -> definitions_en, meta.niveaux -> niveaux_en.
# Un gabarit choisit la clé selon .Page.Lang ; il ne traduit rien, il ne formate pas de chiffre au-delà du point décimal.
# En anglais, le nom de pays porte lui-même son article quand il en faut un (« the Netherlands ») : ARTICLE_EN
# joue le rôle d'ARTICLE, sans article pour les autres.
NOMS_EN = {
    "BE": "Belgium", "BG": "Bulgaria", "CZ": "Czechia", "DK": "Denmark", "DE": "Germany",
    "EE": "Estonia", "IE": "Ireland", "EL": "Greece", "ES": "Spain", "FR": "France",
    "HR": "Croatia", "IT": "Italy", "CY": "Cyprus", "LV": "Latvia", "LT": "Lithuania",
    "LU": "Luxembourg", "HU": "Hungary", "MT": "Malta", "NL": "Netherlands", "AT": "Austria",
    "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SI": "Slovenia", "SK": "Slovakia",
    "FI": "Finland", "SE": "Sweden",
    "USA": "United States", "JPN": "Japan", "GBR": "United Kingdom", "CAN": "Canada", "CHE": "Switzerland",
    "NOR": "Norway", "FRA": "France (OECD basis)", "CHN": "China", "IND": "India", "BRA": "Brazil",
    "ZAF": "South Africa",
}
ARTICLE_EN = {c: ("the " + n if c == "NL" else n) for c, n in NOMS_EN.items() if c in ARTICLE}
ORD_FR = {1: "première", 2: "deuxième", 3: "troisième", 4: "quatrième", 5: "cinquième", 6: "sixième"}
ORD_EN = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth"}
PAGE_URL_EN = "stephane-lalut.com/en/public-debt-international-comparison/"
AVANCES = ["USA", "JPN", "GBR", "CAN", "CHE", "NOR", "FRA"]
EMERGENTS = ["CHN", "IND", "BRA", "ZAF"]


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def fetch(url: str, essais: int = 3) -> bytes:
    for k in range(essais):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com (stephane@stephane-lalut.com)"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if k == essais - 1:
                fail("reseau : %s (%s)" % (url[:120], e))
            time.sleep(3 * (k + 1))
    return b""


# ------------------------------------------------------------------ Eurostat
def eurostat(dataset: str, annees: list[str], **filtres) -> dict[tuple[str, str], float]:
    """(geo, annee) -> valeur. Re-parse en float, rien de brut ne sort de la fonction."""
    q = [("format", "JSON")] + [(k, v) for k, v in filtres.items()] + [("geo", g) for g in UE] + [("time", a) for a in annees]
    url = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/%s?" % dataset) + urllib.parse.urlencode(q)
    d = json.loads(fetch(url))
    if "dimension" not in d:
        fail("Eurostat %s : reponse sans dimensions" % dataset)
    ids, size = d["id"], d["size"]
    gi = d["dimension"]["geo"]["category"]["index"]
    ti = d["dimension"]["time"]["category"]["index"]
    out = {}
    for g, a in gi.items():
        for t, b in ti.items():
            pos, mult = 0, 1
            for dim, sz in reversed(list(zip(ids, size))):
                k = a if dim == "geo" else (b if dim == "time" else 0)
                pos += k * mult
                mult *= sz
            v = d["value"].get(str(pos))
            if v is not None:
                out[(g, t)] = float(v)
    return out


# ------------------------------------------------------------------ OCDE
def ocde(cle: str) -> dict[tuple[str, str, str], float]:
    """(pays, mesure, annee) -> valeur, Economic Outlook (derniere edition publiee)."""
    url = ("https://sdmx.oecd.org/public/rest/data/OECD.ECO.MAD,DSD_EO@DF_EO,1.3/%s"
           "?format=csvfilewithlabels&startPeriod=2022" % cle)
    raw = fetch(url).decode("utf-8-sig")
    import csv
    import io
    rows = list(csv.DictReader(io.StringIO(raw)))
    if not rows:
        fail("OCDE : reponse vide pour %s" % cle)
    out = {}
    for r in rows:
        try:
            out[(r["REF_AREA"], r["MEASURE"], r["TIME_PERIOD"])] = float(r["OBS_VALUE"])
        except (KeyError, ValueError):
            continue
    return out


def fmi(ind: str, pays: list[str]) -> dict[str, dict[str, float]]:
    d = json.loads(fetch("https://www.imf.org/external/datamapper/api/v1/%s/%s" % (ind, "/".join(pays))))
    return {p: {k: float(v) for k, v in d["values"][ind].get(p, {}).items()} for p in pays}


def banque_mondiale(ind: str, pays: list[str]) -> dict[str, tuple[str, float]]:
    url = "https://api.worldbank.org/v2/country/%s/indicator/%s?format=json&per_page=500&mrv=5" % (";".join(pays), ind)
    d = json.loads(fetch(url))
    out = {}
    for r in d[1] or []:
        if r["value"] is not None:
            p = r["countryiso3code"]
            if p not in out or r["date"] > out[p][0]:
                out[p] = (r["date"], float(r["value"]))
    return out


# ------------------------------------------------------------------ statistiques
def ols(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((a - mx) ** 2 for a in xs)
    sxy = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    syy = sum((b - my) ** 2 for b in ys)
    return my - sxy / sxx * mx, sxy / sxx, (sxy * sxy / (sxx * syy) if syy else 0.0)


def rangs(v: list[float]) -> list[float]:
    o = sorted(range(len(v)), key=lambda k: v[k])
    r = [0.0] * len(v)
    for pos, k in enumerate(o):
        r[k] = pos + 1.0
    return r


def ols2(x1: list[float], x2: list[float], y: list[float]) -> tuple[list[float], float]:
    X = [[1.0, a, b] for a, b in zip(x1, x2)]
    n, m = len(y), 3
    A = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(m)] for a in range(m)]
    v = [sum(X[i][a] * y[i] for i in range(n)) for a in range(m)]
    for c in range(m):
        p = max(range(c, m), key=lambda r: abs(A[r][c]))
        A[c], A[p], v[c], v[p] = A[p], A[c], v[p], v[c]
        for r in range(m):
            if r != c:
                f = A[r][c] / A[c][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
                v[r] -= f * v[c]
    b = [v[i] / A[i][i] for i in range(m)]
    my = sum(y) / n
    yh = [sum(bb * xx for bb, xx in zip(b, X[i])) for i in range(n)]
    return b, 1 - sum((y[i] - yh[i]) ** 2 for i in range(n)) / sum((yy - my) ** 2 for yy in y)


# ------------------------------------------------------------------ formatage
def fr(v: float, dec: int = 1) -> str:
    s = ("%." + str(dec) + "f") % v
    return s.replace("-", "\u2212").replace(".", ",")


def pct(v: float, dec: int = 1) -> str:
    return fr(v, dec) + "\u00a0%"


def en(v: float, dec: int = 1) -> str:
    """3536.1 -> '3,536.1' : virgule de milliers, point d\u00e9cimal (m\u00eame fonction que update_dette_insee.py), et le
    m\u00eame signe moins typographique que la version fran\u00e7aise."""
    return ("{:,." + str(dec) + "f}").format(v).replace("-", "\u2212")


def pct_en(v: float, dec: int = 1) -> str:
    return en(v, dec) + "%"


def liste_en(noms: list[str]) -> str:
    """['Belgium', 'Spain', 'Italy'] -> 'Belgium, Spain and Italy'."""
    return noms[0] if len(noms) == 1 else ", ".join(noms[:-1]) + " and " + noms[-1]


def ordinal_en(n: int) -> str:
    if n in ORD_EN:
        return ORD_EN[n]
    return "%d%s" % (n, "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))


# Les deux pr\u00e9sentations, d\u00e9crites une fois : affichage() et les figures lisent l'une ou l'autre, jamais un litt\u00e9ral.
LOC = {
    "fr": dict(nb=fr, pct=pct, nom="nom", article=ARTICLE, ordinal=lambda n: ORD_FR.get(n, "%de" % n),
               liste=lambda noms: " et ".join(noms), point=lambda v: fr(v, 2) + "\u00a0point"),
    "en": dict(nb=en, pct=pct_en, nom="nom_en", article=ARTICLE_EN, ordinal=ordinal_en, liste=liste_en,
               point=lambda v: en(v, 2) + (" percentage point" if abs(round(v, 2)) == 1 else " percentage points")),
}


# ------------------------------------------------------------------ niveau 1 : Europe
def niveau_europe() -> tuple[str, list[dict]]:
    # Annee la plus recente ou les interets sont publies pour >= 25 pays.
    an = None
    for cand in (str(datetime.now().year), str(datetime.now().year - 1), str(datetime.now().year - 2)):
        test = eurostat("gov_10a_main", [cand], na_item="D41PAY", sector="S13", unit="MIO_NAC")
        if len(test) >= 25:
            an = cand
            break
    if not an:
        fail("aucune annee Eurostat avec interets pour 25 pays")
    an_1 = str(int(an) - 1)
    euro = EURO_PAR_AN.get(an)
    if euro is None:
        fail("zone euro non declaree pour %s : completer EURO_PAR_AN" % an)
    I = eurostat("gov_10a_main", [an], na_item="D41PAY", sector="S13", unit="MIO_NAC")
    R = eurostat("gov_10a_main", [an], na_item="TR", sector="S13", unit="MIO_NAC")
    Y = eurostat("nama_10_gdp", [an], na_item="B1GQ", unit="CP_MNAC")
    D = eurostat("gov_10dd_edpt1", [an_1, an], na_item="GD", sector="S13", unit="MIO_NAC")
    DP = eurostat("gov_10dd_edpt1", [an], na_item="GD", sector="S13", unit="PC_GDP")
    ans_inf = [str(int(an) - k) for k in (3, 2, 1)]
    # Cinq ans d'inflation : la fenêtre de 3 ans est celle de la page, 2, 4 et 5 ans servent au test de
    # robustesse demandé par la contre-expertise PRO-20260930-061613 (recalculé et gardé à chaque passage).
    H = eurostat("prc_hicp_aind", [str(int(an) - k) for k in (5, 4, 3, 2, 1)], coicop="CP00", unit="RCH_A_AVG")
    T10 = eurostat("irt_lt_mcby_a", [an], int_rt="MCBY")
    M1 = eurostat("gov_10dd_ggd", [an], na_item="GD", sector="S13", sector2="S1_S2", maturity="Y_LE1", unit="MIO_NAC")
    MT = eurostat("gov_10dd_ggd", [an], na_item="GD", sector="S13", sector2="S1_S2", maturity="TOTAL", unit="MIO_NAC")
    rows = []
    manquants = []
    for g in UE:
        try:
            i, r, y, d1, dp = I[(g, an)], R[(g, an)], Y[(g, an)], D[(g, an_1)], DP[(g, an)]
        except KeyError:
            manquants.append(g)
            continue
        stock, prix, rec, charge = 100 * d1 / y, 100 * i / d1, 100 * r / y, 100 * i / r
        if abs(charge - stock * prix / rec) > 1e-9:
            fail("identite non verifiee pour %s" % g)
        infl = [H[(g, a)] for a in ans_inf if (g, a) in H]
        fen = {}
        for k in (2, 3, 4, 5):
            v = [H.get((g, str(int(an) - j))) for j in range(1, k + 1)]
            fen[str(k)] = sum(v) / k if None not in v else None
        part1 = (100 * M1[(g, an)] / MT[(g, an)]) if (g, an) in M1 and MT.get((g, an)) else None
        rows.append(dict(code=g, nom=NOMS[g], nom_en=NOMS_EN[g], euro=g in euro, stock_fin=dp, stock=stock, prix=prix, recettes=rec,
                         charge=charge, inflation=(sum(infl) / len(infl)) if len(infl) == 3 else None,
                         inflation_fenetres=fen, taux10=T10.get((g, an)), part_1an=part1))
    if manquants:
        log("Europe : pays sans donnees completes pour %s : %s" % (an, ", ".join(manquants)))
    if len(rows) < 25:
        fail("Europe : %d pays seulement (25 attendus au minimum)" % len(rows))
    for x in rows:  # gardes de vraisemblance
        for k, lo, hi in (("stock", 3, 250), ("prix", 0.2, 12), ("recettes", 15, 70), ("charge", 0, 30)):
            if not lo <= x[k] <= hi:
                fail("Europe : %s %s = %.2f hors bande [%s, %s]" % (x["code"], k, x[k], lo, hi))
    fr_ = next(x for x in rows if x["code"] == "FR")
    if not 1.0 <= fr_["prix"] <= 4.0 or not 90 <= fr_["stock"] <= 140:
        fail("France hors bande de vraisemblance (prix %.2f, stock %.1f)" % (fr_["prix"], fr_["stock"]))
    return an, rows


# ------------------------------------------------------------------ niveau 2 : avances hors UE
def niveau_avances(an: str) -> list[dict]:
    an_1 = str(int(an) - 1)
    o = ocde("%s.GGINTP+YRGT+GDP+GGFLQ+GNFLQ.A" % "+".join(AVANCES))
    out = []
    for p in AVANCES:
        try:
            i, r, y = o[(p, "GGINTP", an)], o[(p, "YRGT", an)], o[(p, "GDP", an)]
        except KeyError:
            log("OCDE : %s incomplet pour %s" % (p, an))
            continue
        d1_pct = o.get((p, "GGFLQ", an_1))
        y1 = o.get((p, "GDP", an_1))
        if d1_pct is None or y1 is None:
            dern = max((int(k[2]) for k in o if k[0] == p and k[1] == "GGFLQ"), default=None)
            out.append(dict(code=p, nom=NOMS[p], nom_en=NOMS_EN[p], niveau="avance", badge="avec réserve",
                            badge_en="with reservations", stock=None, prix=None,
                            recettes=100 * r / y, charge=100 * i / r,
                            note="passifs financiers bruts publiés jusqu'en %s seulement : prix non calculé" % dern,
                            note_en="gross financial liabilities published up to %s only: price not computed" % dern,
                            dette_nette=o.get((p, "GNFLQ", an))))
            continue
        d1 = d1_pct / 100 * y1
        stock, prix, rec, charge = 100 * d1 / y, 100 * i / d1, 100 * r / y, 100 * i / r
        if abs(charge - stock * prix / rec) > 1e-9:
            fail("identite non verifiee (OCDE) pour %s" % p)
        out.append(dict(code=p, nom=NOMS[p], nom_en=NOMS_EN[p], niveau="avance", badge="avec réserve",
                        badge_en="with reservations", stock=stock, prix=prix,
                        recettes=rec, charge=charge, note="", note_en="", dette_nette=o.get((p, "GNFLQ", an))))
    if len(out) < 5:
        fail("OCDE : %d pays avances seulement" % len(out))
    return out


# ------------------------------------------------------------------ niveau 3 : emergents
def niveau_emergents() -> tuple[str, list[dict]]:
    dette = fmi("GGXWDG_NGDP", EMERGENTS)
    wb = banque_mondiale("GC.XPN.INTP.RV.ZS", EMERGENTS)
    an_fmi = str(datetime.now().year - 1)
    out = []
    for p in EMERGENTS:
        ch = wb.get(p)
        # Contre-expertise PRO-20260930-061613 (P1) : dette et charge de la MÊME année. La charge Banque
        # mondiale est datée (2021 pour la Chine…) : on lit la dette FMI de cette année-là, jamais celle de l'an dernier.
        an_ligne = ch[0] if ch else None
        st = dette[p].get(an_ligne) if an_ligne else None
        if ch and st is None:
            fail("FMI : dette de %s absente pour %s, année de la charge Banque mondiale" % (p, an_ligne))
        out.append(dict(code=p, nom=NOMS[p], nom_en=NOMS_EN[p], niveau="emergent", badge="indicatif", badge_en="indicative",
                        stock=st, prix=None, recettes=None,
                        charge=ch[1] if ch else None, charge_annee=an_ligne, annee=an_ligne,
                        note_en="IMF debt and World Bank interest for the same year; interest of central government only",
                        note="dette FMI et intérêts Banque mondiale de la même année ; intérêts de la seule administration centrale"))
    return an_fmi, out


# ------------------------------------------------------------------ statistiques de la page
def statistiques(rows: list[dict]) -> dict:
    euro = [x for x in rows if x["euro"]]
    hors = [x for x in rows if not x["euro"]]
    s = {}
    a, b, r2 = ols([x["stock"] for x in rows], [x["charge"] for x in rows])
    s["charge_stock"] = dict(n=len(rows), pente=b, ordonnee=a, r2=r2)
    rx, ry = rangs([x["stock"] for x in rows]), rangs([x["charge"] for x in rows])
    rho2 = ols(rx, ry)[2]
    s["spearman_rho"] = math.sqrt(rho2) * (1 if ols(rx, ry)[1] > 0 else -1)
    for nom, g in (("euro", euro), ("hors", hors)):
        a, b, r2 = ols([x["stock"] for x in g], [x["charge"] for x in g])
        s["charge_stock_" + nom] = dict(n=len(g), pente=b, ordonnee=a, r2=r2,
                                        stock_min=min(x["stock"] for x in g), stock_max=max(x["stock"] for x in g))
        s["prix_moyen_" + nom] = sum(x["prix"] for x in g) / len(g)
        s["prix_stock_r2_" + nom] = ols([x["stock"] for x in g], [x["prix"] for x in g])[2]
        gi = [x for x in g if x["inflation"] is not None]
        a, b, r2 = ols([x["inflation"] for x in gi], [x["prix"] for x in gi])
        s["prix_inflation_" + nom] = dict(n=len(gi), pente=b, ordonnee=a, r2=r2)
    s["prix_stock_r2"] = ols([x["stock"] for x in rows], [x["prix"] for x in rows])[2]
    gi = [x for x in rows if x["inflation"] is not None]
    coef, r2 = ols2([1.0 if x["euro"] else 0.0 for x in gi], [x["inflation"] for x in gi], [x["prix"] for x in gi])
    s["prix_euro_inflation"] = dict(n=len(gi), effet_euro=coef[1], effet_inflation=coef[2], r2=r2)
    loo = []
    for k in hors:
        g = [x for x in hors if x is not k]
        loo.append(ols([x["stock"] for x in g], [x["charge"] for x in g])[1])
    s["pente_hors_loo"] = dict(min=min(loo), max=max(loo))
    # Robustesse de la fenêtre d'inflation (2 à 5 ans) : si le signe ou l'ordre de grandeur changent, les
    # coefficients sortent de la page (garde de prose « coefficients robustes »).
    rob = []
    for k in ("2", "3", "4", "5"):
        g = [x for x in rows if x["inflation_fenetres"].get(k) is not None]
        c, r2 = ols2([1.0 if x["euro"] else 0.0 for x in g], [x["inflation_fenetres"][k] for x in g], [x["prix"] for x in g])
        he = [x for x in g if not x["euro"]]
        rob.append(dict(fenetre=int(k), n=len(g), r2=r2, effet_euro=c[1], effet_inflation=c[2],
                        r2_hors=ols([x["inflation_fenetres"][k] for x in he], [x["prix"] for x in he])[2]))
    s["robustesse_inflation"] = rob
    return s


# ------------------------------------------------------------------ trente ans d'écarts avec l'Allemagne
# Question de l'auteur (30/09/2026) : « l'euro fait-il baisser le coût de la dette ? », à trancher par les chiffres et
# non par le récit courant. Test : les pays restés HORS de l'euro (Suède, Danemark ; Pologne et Hongrie depuis 2001)
# ont-ils suivi la même trajectoire que les membres ? Rendements de convergence à 10 ans, Eurostat.
ECARTS_PAYS = [("FR", 1999), ("IT", 1999), ("ES", 1999), ("PT", 1999), ("IE", 1999), ("EL", 2001),
               ("SE", None), ("DK", None), ("PL", None), ("HU", None)]


def ecarts_allemagne(an: str) -> dict:
    ans = ["1995", "1998", "2007", "2012", an]
    T = eurostat("irt_lt_mcby_a", ans, int_rt="MCBY")
    if any(("DE", a) not in T for a in ans):
        fail("Eurostat irt_lt_mcby_a : taux allemand absent pour une des annees %s" % ans)
    pays = []
    for g, entree in ECARTS_PAYS:
        e = {a: (T[(g, a)] - T[("DE", a)]) if (g, a) in T else None for a in ans}
        pays.append(dict(code=g, nom=NOMS[g], nom_en=NOMS_EN[g], euro_depuis=entree, ecarts=e))
    return dict(annees=ans, allemagne={a: T[("DE", a)] for a in ans}, pays=pays,
                source_en="Eurostat irt_lt_mcby_a (10-year convergence yields on government bonds)",
                source="Eurostat irt_lt_mcby_a (rendements de convergence à 10 ans des emprunts d'État)")


def faux_jumeaux(rows: list[dict], seuil: float = 10.0, n: int = 3) -> list[dict]:
    """Regle PUBLIEE, fixee avant calcul : pour chaque pays, son plus proche voisin en stock ;
    couples a ecart de stock < seuil points ; classes par ecart de charge ; les n premiers."""
    couples = set()
    for x in rows:
        v = min((y for y in rows if y is not x), key=lambda y: abs(y["stock"] - x["stock"]))
        if abs(v["stock"] - x["stock"]) < seuil:
            couples.add(tuple(sorted((x["code"], v["code"]))))
    by = {x["code"]: x for x in rows}
    cl = sorted(couples, key=lambda c: -abs(by[c[0]]["charge"] - by[c[1]]["charge"]))[:n]
    out = []
    for a, b in cl:
        u, v = sorted((by[a], by[b]), key=lambda z: z["charge"])
        out.append(dict(bas=u["code"], haut=v["code"], ecart_stock=abs(u["stock"] - v["stock"]),
                        rapport_charge=v["charge"] / u["charge"]))
    return out


# ------------------------------------------------------------------ SVG
W = 720
COL_EURO, COL_HORS = "#184f95", "#eb6834"
INK, INK2, MUTED, GRID, AXIS = "#0A0A0E", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
TY_TITRE, TY_AXE, TY_ANNOT = 13, 11, 11
CARTOUCHE_H = 48


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def entete(h: int, ident: str, titre: str, desc: str) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" '
            'font-variant-numeric="tabular-nums" aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h + CARTOUCHE_H, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + CARTOUCHE_H)]


# Libellés imprimés DANS les images, par langue. Les titres, descriptions, sources et précautions propres à chaque
# figure vivent dans figures() ; ici, ce que toutes partagent.
LIB_FIG = {
    "fr": dict(licence="Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, euro="zone euro", hors="hors zone euro",
               pc=" %", pt=" pt"),
    "en": dict(licence="Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN, euro="euro area",
               hors="outside euro area", pc="%", pt=" pp"),
}


def cartouche(y0: float, source: str, note: str, lang: str = "fr") -> list[str]:
    lignes = [(source, INK2)] + ([(note, INK2)] if note else []) + [(LIB_FIG[lang]["licence"], MUTED)]
    out = ['<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID)]
    for k, (t, c) in enumerate(lignes):
        out.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, c, esc(t)))
    return out


def legende(x: float, y: float, lang: str = "fr") -> list[str]:
    L = LIB_FIG[lang]
    return ['<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (x, y - 4, COL_EURO),
            '<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s</text>' % (x + 9, y, TY_ANNOT, INK2, L["euro"]),
            '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (x + 90, y - 4, COL_HORS),
            '<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s</text>' % (x + 99, y, TY_ANNOT, INK2, L["hors"])]


def axe_x(x0, x1, y, vmin, vmax, pas, fmt, libelle):
    e = ['<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (x0, y, x1, y, AXIS)]
    v = vmin
    while v <= vmax + 1e-9:
        x = x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="middle">%s</text>' % (x, y + 15, TY_AXE, MUTED, fmt(v)))
        v += pas
    e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="middle">%s</text>' % ((x0 + x1) / 2, y + 32, TY_AXE, INK2, esc(libelle)))
    return e


def grille_y(x0, x1, y0, y1, vmin, vmax, pas, fmt, libelle):
    e = []
    v = vmin
    while v <= vmax + 1e-9:
        y = y1 - (v - vmin) / (vmax - vmin) * (y1 - y0)
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (x0, y, x1, y, GRID))
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="end">%s</text>' % (x0 - 6, y + 4, TY_AXE, MUTED, fmt(v)))
        v += pas
    e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s</text>' % (x0, y0 - 10, TY_AXE, INK2, esc(libelle)))
    return e


def nuage(rows, fx, fy, xmax, ymax, pasx, pasy, lx, ly, ident, titre, desc, source, note, etiquettes, droites=None,
          jumeaux=(), ymin=0.0, fmt_y=None, lang="fr"):
    H = 440
    nb, pc, cle_nom = LOC[lang]["nb"], LIB_FIG[lang]["pc"], LOC[lang]["nom"]
    X0, X1, Y0, Y1 = 58, W - 20, 64, H - 52
    sx = lambda v: X0 + v / xmax * (X1 - X0)  # noqa: E731
    sy = lambda v: Y1 - (v - ymin) / (ymax - ymin) * (Y1 - Y0)  # noqa: E731
    e = entete(H, ident, titre, desc)
    e.append('<text x="0" y="18" font-size="%d" font-weight="600" fill="%s">%s</text>' % (TY_TITRE, INK, esc(titre)))
    e += legende(W - 250, 18, lang)
    e += grille_y(X0, X1, Y0, Y1, ymin, ymax, pasy, fmt_y or (lambda v: nb(v, 0) + pc), ly)
    e += axe_x(X0, X1, Y1, 0, xmax, pasx, lambda v: nb(v, 0) + pc, lx)
    by = {x["code"]: x for x in rows}
    for j in jumeaux:
        a, b = by[j["bas"]], by[j["haut"]]
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.5" stroke-dasharray="3 3"/>'
                 % (sx(fx(a)), sy(fy(a)), sx(fx(b)), sy(fy(b)), MUTED))
    for (a, b, xa, xb, col) in (droites or []):
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" opacity="0.7"/>'
                 % (sx(xa), sy(a + b * xa), sx(xb), sy(a + b * xb), col))
    for x in rows:
        e.append('<circle cx="%.1f" cy="%.1f" r="5.5" fill="%s" stroke="#fff" stroke-width="1"/>'
                 % (sx(fx(x)), sy(fy(x)), COL_EURO if x["euro"] else COL_HORS))
    # Placement : au-dessus par défaut (étiquette centrée sur son point, charte du site) ; « b » dessous,
    # « g » à gauche, « d » à droite, pour les points serrés. Les membres des faux jumeaux sont toujours nommés.
    noms = dict(etiquettes) if isinstance(etiquettes, dict) else {c: "h" for c in etiquettes}
    for j in jumeaux:
        noms.setdefault(j["bas"], "h")
        noms.setdefault(j["haut"], "h")
    for x in rows:
        pos = noms.get(x["code"])
        if not pos:
            continue
        px, py = sx(fx(x)), sy(fy(x))
        dx, dy, anc = {"h": (0, -9, "middle"), "b": (0, 18, "middle"), "g": (-9, 4, "end"), "d": (9, 4, "start")}[pos]
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>'
                 % (px + dx, py + dy, TY_ANNOT, INK, anc, ' font-weight="600"' if x["code"] == "FR" else "", esc(x[cle_nom])))
    e += cartouche(H + 2, source, note, lang)
    e.append("</svg>")
    return "\n".join(e)


def barres_stock(rows, an, source, lang="fr"):
    rows = sorted(rows, key=lambda x: -x["stock_fin"])
    hb = 15
    H = 70 + hb * len(rows) + 20
    X0, X1 = 110, W - 60
    vmax = math.ceil(max(x["stock_fin"] for x in rows) / 20) * 20
    T = {"fr": ("Le stock : dette publique en %% du PIB, fin %s",
                "Dette brute de Maastricht des administrations publiques, 27 pays de l'Union européenne, fin %s.",
                "Stock brut, sans les actifs publics ni les engagements hors dette (retraites)."),
         "en": ("The stock: public debt as a %% of GDP, end-%s",
                "Maastricht gross debt of general government, 27 European Union countries, end-%s.",
                "Gross stock, excluding public assets and liabilities outside debt (pensions).")}[lang]
    titre = T[0] % an
    e = entete(H, "ms", titre, T[1] % an)
    e.append('<text x="0" y="18" font-size="%d" font-weight="600" fill="%s">%s</text>' % (TY_TITRE, INK, esc(titre)))
    e += legende(W - 250, 18, lang)
    for k, x in enumerate(rows):
        y = 50 + k * hb
        w = x["stock_fin"] / vmax * (X1 - X0)
        e.append('<text x="%d" y="%.1f" font-size="%d" fill="%s" text-anchor="end"%s>%s</text>'
                 % (X0 - 8, y + 10, TY_ANNOT, INK, ' font-weight="600"' if x["code"] == "FR" else "", esc(x[LOC[lang]["nom"]])))
        e.append('<rect x="%d" y="%.1f" width="%.1f" height="%d" fill="%s"/>' % (X0, y + 1, w, hb - 4, COL_EURO if x["euro"] else COL_HORS))
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s</text>' % (X0 + w + 5, y + 10, TY_ANNOT, INK2, LOC[lang]["pct"](x["stock_fin"])))
    e += cartouche(H + 2, source, T[2], lang)
    e.append("</svg>")
    return "\n".join(e)


def transmission(rows, an, source, lang="fr"):
    g = [x for x in rows if x["part_1an"] is not None and x["taux10"] is not None]
    fx = lambda x: x["part_1an"]  # noqa: E731
    fy = lambda x: x["taux10"] - x["prix"]  # noqa: E731
    xmax = math.ceil(max(fx(x) for x in g) / 5) * 5
    ymax = math.ceil(max(fy(x) for x in g) * 2) / 2
    ymin = min(0.0, math.floor(min(fy(x) for x in g) * 2) / 2)
    etiq = {"FR": "h", "IT": "d", "DE": "d", "EL": "h", "HU": "g", "SE": "h", "PT": "h", "DK": "d"}
    # Contre-expertise PRO-20260930-061613 (P1) : repère conditionnel, jamais une prévision -- le <desc> lu par
    # les lecteurs d'écran ne doit pas affirmer plus que le texte visible.
    T = {"fr": ("Pression de refinancement : échéances et écart de taux, %s",
                "part de la dette à échéance résiduelle de moins d'un an",
                "écart rendement à 10 ans − taux implicite du stock, en points",
                "Chaque point est un pays : à droite, une plus grande part de la dette arrive à échéance dans l'année ; en haut, "
                "le rendement harmonisé à 10 ans dépasse davantage le taux implicite du stock. Si les conditions de financement "
                "restaient supérieures au coût de la dette remplacée, les refinancements pousseraient le coût moyen à la hausse. "
                "Sous zéro, l'indicateur est orienté dans l'autre sens. Repère, non prévision.",
                "Rendement de convergence à 10 ans, non le coût de toutes les émissions nouvelles. Repère, non prévision."),
         "en": ("Refinancing pressure: maturities and rate gap, %s",
                "share of debt with a residual maturity of less than one year",
                "10-year yield − implicit interest rate on the stock, in percentage points",
                "Each dot is a country: further right, a larger share of the debt falls due within the year; higher up, "
                "the harmonised 10-year yield exceeds the implicit interest rate on the stock by more. If financing conditions "
                "stayed above the cost of the debt being replaced, refinancing would push the average cost up. "
                "Below zero, the indicator points the other way. A marker, not a forecast.",
                "10-year convergence yield, not the cost of all new issuance. A marker, not a forecast.")}[lang]
    nb, pt = LOC[lang]["nb"], LIB_FIG[lang]["pt"]
    return nuage(g, fx, fy, xmax, ymax, 5, 0.5, T[1], T[2], "mt", T[0] % an, T[3], source, T[4],
                 etiq, ymin=ymin, fmt_y=lambda v: nb(v, 1) + pt, lang=lang)


# ------------------------------------------------------------------ affichage
def affichage(an, rows, stats, jum, avances, an_fmi, emergents, ecarts) -> tuple[dict, dict]:
    """Rend (affichage, affichage_en) : UN calcul, deux présentations, aux mêmes clés (même règle que
    bloc_affichage de update_dette_insee.py). Les gardes de prose, plus bas, ne dépendent pas de la langue."""
    by = {x["code"]: x for x in rows}
    F = by["FR"]
    s = stats
    j0 = jum[0]
    lo, hi = by[j0["bas"]], by[j0["haut"]]
    moins_chers_que_fr = sorted((x for x in rows if x["charge"] > F["charge"] and x["stock"] < F["stock"]), key=lambda x: x["stock"])
    se = by.get("SE")
    de = by.get("DE")
    rob = stats["robustesse_inflation"]
    classement = sorted(rows, key=lambda x: -x["stock_fin"])
    rang = [x["code"] for x in classement].index("FR") + 1
    av = {x["code"]: x for x in avances}
    E = {x["code"]: x["ecarts"] for x in ecarts["pays"]}

    def bloc(L: dict) -> dict:
        nb, pc, nom, article = L["nb"], L["pct"], L["nom"], L["article"]
        A = {"annee": an, "annee_1": str(int(an) - 1), "n_pays": str(len(rows)),
             "n_euro": str(sum(x["euro"] for x in rows)), "n_hors": str(sum(not x["euro"] for x in rows))}
        for k in ("stock_fin", "stock", "recettes", "charge"):
            A["fr_" + k] = pc(F[k])
        A["fr_prix"] = pc(F["prix"], 2)
        A["r2_charge_stock"] = nb(s["charge_stock"]["r2"], 2)
        A["spearman"] = nb(s["spearman_rho"], 2)
        A["r2_euro"] = nb(s["charge_stock_euro"]["r2"], 2)
        A["r2_hors"] = nb(s["charge_stock_hors"]["r2"], 2)
        A["r2_prix_stock"] = nb(s["prix_stock_r2"], 2)
        A["prix_moyen_euro"] = pc(s["prix_moyen_euro"], 1)
        A["prix_moyen_hors"] = pc(s["prix_moyen_hors"], 1)
        A["r2_prix_inflation_euro"] = nb(s["prix_inflation_euro"]["r2"], 2)
        A["r2_prix_inflation_hors"] = nb(s["prix_inflation_hors"]["r2"], 2)
        A["r2_prix_euro_inflation"] = nb(s["prix_euro_inflation"]["r2"], 2)
        A["effet_euro"] = nb(-s["prix_euro_inflation"]["effet_euro"], 1)
        A["effet_inflation"] = nb(s["prix_euro_inflation"]["effet_inflation"], 2)
        A["pente_hors_loo_min"] = nb(s["pente_hors_loo"]["min"], 3)
        A["pente_hors_loo_max"] = nb(s["pente_hors_loo"]["max"], 3)
        A["j_bas"], A["j_haut"] = lo[nom], hi[nom]
        for k, x in (("j_bas", lo), ("j_haut", hi)):
            A[k + "_le"] = article[x["code"]]
            A[k + "_le_maj"] = article[x["code"]][0].upper() + article[x["code"]][1:]
        A["j_bas_stock"], A["j_haut_stock"] = pc(lo["stock"], 0), pc(hi["stock"], 0)
        A["j_bas_charge"], A["j_haut_charge"] = pc(lo["charge"]), pc(hi["charge"])
        A["j_bas_prix"], A["j_haut_prix"] = pc(lo["prix"], 2), pc(hi["prix"], 2)
        A["j_bas_rec"], A["j_haut_rec"] = pc(lo["recettes"], 0), pc(hi["recettes"], 0)
        A["j_rapport"] = nb(j0["rapport_charge"], 1)
        # Énumération sans conjonction, dans les deux langues : la prose la cite entre parenthèses.
        A["plus_charges_moins_endettes"] = ", ".join(x[nom] for x in moins_chers_que_fr)
        A["n_plus_charges_moins_endettes"] = str(len(moins_chers_que_fr))
        if se and de:
            A["se_prix"], A["de_prix"] = pc(se["prix"], 2), pc(de["prix"], 2)
        for c in ("FR", "SE", "PT", "DK", "IT", "DE"):
            x = by.get(c)
            if x and x["part_1an"] is not None and x["taux10"] is not None:
                A["%s_part_1an" % c.lower()] = pc(x["part_1an"], 1)
                A["%s_ecart_taux" % c.lower()] = L["point"](x["taux10"] - x["prix"])
                A["%s_taux10" % c.lower()] = pc(x["taux10"], 2)
        A["an_fmi"] = an_fmi
        A["rob_euro_min"] = nb(-max(r["effet_euro"] for r in rob), 1)
        A["rob_euro_max"] = nb(-min(r["effet_euro"] for r in rob), 1)
        A["rob_infl_min"] = nb(min(r["effet_inflation"] for r in rob), 2)
        A["rob_infl_max"] = nb(max(r["effet_inflation"] for r in rob), 2)
        A["rob_r2_min"] = nb(min(r["r2"] for r in rob), 2)
        A["rob_r2_max"] = nb(max(r["r2"] for r in rob), 2)
        A["fr_rang_stock"] = L["ordinal"](rang)
        A["devant_fr"] = L["liste"]([x[nom] for x in classement[:rang - 1]]) if rang > 1 else ""
        # Hors UE : une clé par grandeur disponible, jamais de chiffre saisi dans la prose.
        for x in avances:
            c = x["code"].lower()
            for k, dec in (("stock", 0), ("prix", 2), ("charge", 1), ("dette_nette", 0)):
                if x.get(k) is not None:
                    A["%s_%s" % (c, k)] = pc(x[k], dec)
        for x in emergents:
            c = x["code"].lower()
            if x.get("stock") is not None:
                A[c + "_stock"] = pc(x["stock"], 0)
            if x.get("charge") is not None:
                A[c + "_charge"] = pc(x["charge"], 0)
                A[c + "_charge_annee"] = x["charge_annee"]
        for c, a in (("IT", "1995"), ("IT", "1998"), ("ES", "1995"), ("ES", "1998"), ("SE", "1995"), ("SE", "1998"),
                     ("EL", "2012"), ("PT", "2012"), ("IE", "2012"), ("ES", "2012"), ("IT", "2012"), ("SE", "2012"),
                     ("DK", "2012"), ("HU", "2012"), ("SE", an), ("DK", an), ("FR", an), ("IT", an), ("PL", an), ("HU", an)):
            A["ec_%s_%s" % (c.lower(), "an" if a == an else a)] = nb(abs(E[c][a]), 1 if abs(E[c][a]) >= 10 else 2)
        A["usa_fra_rapport"] = nb(av["USA"]["charge"] / av["FRA"]["charge"], 1)
        return A

    A = bloc(LOC["fr"])
    A_en = bloc(LOC["en"])
    if list(A) != list(A_en):
        fail("affichage_en : cles differentes du bloc francais (%s)" % sorted(set(A) ^ set(A_en)))
    # GARDES DE PROSE : la page affirme ces faits en toutes lettres. Si une nouvelle donnée les
    # dément, on s'arrête au lieu de publier une phrase devenue fausse (« état déclaré ≠ état réel »).
    se, de, dk = by["SE"], by["DE"], by["DK"]
    affirmations = [
        ("la Suède paie comme l'Allemagne", abs(se["prix"] - de["prix"]) < 0.15),
        ("FAQ « pas systématiquement » : l'Allemagne paie moins que la France", de["prix"] < F["prix"]),
        ("FAQ « pas systématiquement » : d'autres pays de la zone euro paient davantage",
         any(x["euro"] and x["prix"] > F["prix"] for x in rows)),
        ("le prix ne suit pas le stock (R2 < 0,1)", stats["prix_stock_r2"] < 0.1),
        ("hors euro, le prix suit l'inflation plus que dans l'euro",
         stats["prix_inflation_hors"]["r2"] > stats["prix_inflation_euro"]["r2"] + 0.2),
        ("indicateur français orienté à la hausse (rendement 10 ans > taux implicite)", F["taux10"] > F["prix"]),
        ("indicateur danois orienté dans l'autre sens (rendement 10 ans < taux implicite)", dk["taux10"] < dk["prix"]),
        ("coefficients robustes à la fenêtre d'inflation (signes stables, facteur < 2)",
         all(r["effet_euro"] < 0 and r["effet_inflation"] > 0 for r in stats["robustesse_inflation"])
         and max(r["effet_euro"] for r in stats["robustesse_inflation"]) / min(r["effet_euro"] for r in stats["robustesse_inflation"]) > 0.5
         and min(r["effet_inflation"] for r in stats["robustesse_inflation"]) / max(r["effet_inflation"] for r in stats["robustesse_inflation"]) > 0.5),
        ("le Japon consacre moins que la France (base OCDE)", av["JPN"]["charge"] < av["FRA"]["charge"]),
        # Cartes hors Europe (30/09) : les qualificatifs de la prose, recalculés.
        ("le Japon doit « près du double » de la France (rapport 1,7 à 2,2)", 1.7 < av["JPN"]["stock"] / av["FRA"]["stock"] < 2.2),
        ("le Japon paie moins cher que la France sur ses passifs", av["JPN"]["prix"] < av["FRA"]["prix"]),
        ("la Suisse « paie peu sur une dette faible » (< 60 % du PIB, rapport sous la France)",
         av["CHE"]["stock"] < 60 and av["CHE"]["prix"] < av["FRA"]["prix"]),
        ("les États-Unis ont des passifs « proches » de la France (écart < 15 points)", abs(av["USA"]["stock"] - av["FRA"]["stock"]) < 15),
        ("la dette nette suisse est négative", (av["CHE"].get("dette_nette") or 0) < 0),
        # Section « trente ans d'écarts » : chaque constat de la prose, recalculé.
        ("avant 1999, les écarts italien et espagnol fondent (> 2 points en 1995, < 0,5 en 1998)",
         all(E[c]["1995"] > 2 and E[c]["1998"] < 0.5 for c in ("IT", "ES"))),
        ("la Suède, hors euro, converge aussi avant 1999 (> 2 points en 1995, < 0,6 en 1998)",
         E["SE"]["1995"] > 2 and E["SE"]["1998"] < 0.6),
        ("en 2012, Grèce, Portugal, Irlande, Espagne, Italie > 3 points ; Suède et Danemark < 0,5",
         all(E[c]["2012"] > 3 for c in ("EL", "PT", "IE", "ES", "IT")) and all(abs(E[c]["2012"]) < 0.5 for c in ("SE", "DK"))),
        ("écarts de 2012 : la Suède au-dessus, le Danemark au-dessous de l'Allemagne", E["SE"]["2012"] > 0 > E["DK"]["2012"]),
        ("en 2012, la Hongrie, hors euro, au-dessus de 3 points", E["HU"]["2012"] > 3),
        ("en 2012, aucun pays hors euro du tableau n'atteint la Grèce ni le Portugal",
         max(x["ecarts"]["2012"] for x in ecarts["pays"] if not x["euro_depuis"] and x["ecarts"]["2012"] is not None)
         < min(E["EL"]["2012"], E["PT"]["2012"])),
        ("aujourd'hui, la Suède et le Danemark empruntent sous l'Allemagne", E["SE"][an] < 0 and E["DK"][an] < 0),
        ("aujourd'hui, la France au-dessus de l'Allemagne, l'Italie au-dessus de la France",
         0 < E["FR"][an] < E["IT"][an]),
        ("aujourd'hui, la Pologne et la Hongrie, hors euro, paient plus que l'Italie",
         E["PL"][an] > E["IT"][an] and E["HU"][an] > E["IT"][an]),
        ("le prix français est dans la moyenne de la zone euro", abs(F["prix"] - stats["prix_moyen_euro"]) < 0.4),
        ("des pays moins endettés que la France ont une charge plus lourde", len(moins_chers_que_fr) >= 2),
        ("les faux jumeaux : le plus chargé paie plus cher", hi["prix"] > lo["prix"]),
        ("la France est troisième, derrière la Grèce et l'Italie",
         rang == 3 and {x["code"] for x in classement[:2]} == {"EL", "IT"}),
        ("figure du stock : de la Grèce à l'Estonie", classement[0]["code"] == "EL" and classement[-1]["code"] == "EE"),
        ("euro et inflation rendent compte d'une large part du prix (R2 >= 0,5)", stats["prix_euro_inflation"]["r2"] >= 0.5),
        ("les États-Unis consacrent plus que la France", av["USA"]["charge"] > av["FRA"]["charge"]),
    ]
    faux = [t for t, ok in affirmations if not ok]
    if faux:
        fail("la page affirme ce que les données ne soutiennent plus : " + " ; ".join(faux))
    return A, A_en


def fiches_figures(figs: dict, A: dict, A_en: dict) -> dict:
    """Cartes du bloc « Réutiliser cette page », dans l'ordre de lecture de la page. « montre » est la seule phrase
    écrite ici ; ses qualificatifs sont couverts par les gardes de prose (rapport des faux jumeaux, Suède, inflation).
    Clé "en" : même structure, fichiers suffixés -en, titre, source et précaution lus dans le SVG anglais."""
    import html as _html
    import re as _re
    MONTRE = {
        "fr": [
            ("charge", "dette-monde-charge",
             "À dette voisine, la part des recettes consacrée aux intérêts peut varier de 1 à %s ; hors de la zone euro, "
             "elle croît plus vite avec la dette." % A["j_rapport"]),
            ("prix", "dette-monde-prix",
             "Hors de la zone euro, le taux implicite est étroitement associé à l'inflation récente ; dans la zone euro, "
             "beaucoup moins. La Suède, hors euro, paie comme l'Allemagne."),
            ("transmission", "dette-monde-transmission",
             "La part de la dette qui arrive à échéance et l'écart entre taux de marché et taux implicite : un repère de "
             "pression sur le coût moyen, non une prévision."),
            ("stock", "dette-monde-stock",
             "Le classement le plus cité : il ne dit ni le prix payé sur la dette, ni la part des recettes qu'elle absorbe."),
        ],
        "en": [
            ("charge", "dette-monde-charge-en",
             "With similar debt, the share of revenue spent on interest can differ by a factor of %s; outside the euro area, "
             "it rises faster with debt." % A_en["j_rapport"]),
            ("prix", "dette-monde-prix-en",
             "Outside the euro area, the implicit interest rate is closely associated with recent inflation; within the euro "
             "area, much less so. Sweden, outside the euro, pays about the same as Germany."),
            ("transmission", "dette-monde-transmission-en",
             "The share of debt falling due and the gap between market yields and the implicit interest rate: a marker of "
             "pressure on the average cost, not a forecast."),
            ("stock", "dette-monde-stock-en",
             "The most quoted ranking: it shows neither the price paid on the debt nor the share of revenue it absorbs."),
        ],
    }
    res = {}
    for lang in ("fr", "en"):
        out = []
        for ident, fichier, montre in MONTRE[lang]:
            svg = figs[fichier + ".svg"]
            titre = _html.unescape(_re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [_html.unescape(t) for t in _re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
            if len(cart) < 2 or cart[-1] != LIB_FIG[lang]["licence"]:
                fail("fiche %s : cartouche illisible dans le SVG" % fichier)
            out.append(dict(id=ident, fichier=fichier, titre=titre, montre=montre, source=cart[0],
                            precaution=cart[1] if len(cart) == 3 else ""))
        res[lang] = out
    return res


def csv_texte(an: str, rows: list[dict], avances: list[dict], emergents: list[dict]) -> str:
    import csv, io as _io
    def v(x, d):
        return "" if x is None else ("%." + str(d) + "f") % x
    buf = _io.StringIO()
    w = csv.writer(buf, lineterminator="\n")  # guillemets posés par le module : un libellé peut contenir une virgule
    w.writerow(["niveau", "comparabilite", "pays", "code", "annee", "zone_euro", "stock_depart_pct_pib",
                "stock_cloture_pct_pib", "prix_taux_implicite_pct", "recettes_pct_pib", "charge_interets_pct_recettes",
                "part_dette_moins_1an_pct", "taux_10ans_pct"])
    for x in sorted(rows, key=lambda r: -r["stock"]):
        w.writerow(["europe", "strictement comparable (Eurostat S.13)", x["nom"], x["code"], an, "oui" if x["euro"] else "non",
                    v(x["stock"], 2), v(x["stock_fin"], 1), v(x["prix"], 3), v(x["recettes"], 2), v(x["charge"], 2),
                    v(x["part_1an"], 2), v(x["taux10"], 2)])
    for x in avances:
        w.writerow(["avances_hors_ue", "avec réserve (OCDE, passifs financiers bruts)", x["nom"], x["code"], an, "",
                    v(x.get("stock"), 2), "", v(x.get("prix"), 3), v(x.get("recettes"), 2), v(x.get("charge"), 2), "", ""])
    for x in emergents:
        w.writerow(["emergents", "indicatif (dette FMI, intérêts Banque mondiale de l'administration centrale)", x["nom"],
                    x["code"], str(x.get("annee") or ""), "", v(x.get("stock"), 2), "", "", "", v(x.get("charge"), 2), "", ""])
    return buf.getvalue()


def figures(lang: str, an: str, rows: list[dict], stats: dict, jum: list[dict]) -> dict[str, str]:
    """Les quatre figures d'une langue : même dessin, mêmes données, seuls les textes changent. Fichiers anglais
    suffixés -en (dette-monde-charge-en.svg), comme ceux de update_dette_insee.py."""
    an_1, an_3 = str(int(an) - 1), str(int(an) - 3)
    suf = "" if lang == "fr" else "-en"
    T = {
        "fr": dict(
            src_stock="Eurostat gov_10dd_edpt1, dette de Maastricht, fin %s" % an,
            src_eu=("Eurostat gov_10a_main (D41PAY, TR), gov_10dd_edpt1 (GD), nama_10_gdp (B1GQ), %s ; "
                    "administrations publiques S.13, monnaie nationale" % an),
            c_lx="stock : dette fin %s rapportée au PIB %s" % (an_1, an),
            c_ly="charge : intérêts en % des recettes publiques",
            c_titre="Même dette, charge différente : les 27 pays de l'UE en %s" % an,
            c_desc="Chaque point est un pays. Les pointillés relient les faux jumeaux désignés par la règle publiée : dette voisine, "
                   "charge très différente. Deux droites de moindres carrés, une par groupe, sur leur plage observée.",
            c_note="Pointillés : faux jumeaux (plus proche voisin en stock, écart < 10 points, trois plus grands écarts de charge).",
            p_lx="inflation moyenne %s-%s (IPCH)" % (an_3, an_1),
            p_ly="taux implicite : intérêts %s / dette fin %s" % (an, an_1),
            p_titre="Prix de la dette et inflation récente : l'Europe en %s" % an,
            p_desc="Hors de la zone euro, le taux implicite est étroitement associé à l'inflation récente ; dans la zone euro, beaucoup "
                   "moins : les pays baltes ont connu une forte inflation sans taux élevé. La Suède, hors euro, a le même taux implicite "
                   "que l'Allemagne. Association observée sur une année, non causalité.",
            p_src="Eurostat prc_hicp_aind (IPCH), gov_10a_main, gov_10dd_edpt1, %s" % an,
            p_note="Relation descriptive sur une année, non causale.",
            src_tr="Eurostat gov_10dd_ggd (dette par échéance résiduelle), irt_lt_mcby_a (taux à 10 ans), %s" % an),
        "en": dict(
            src_stock="Eurostat gov_10dd_edpt1, Maastricht debt, end-%s" % an,
            src_eu=("Eurostat gov_10a_main (D41PAY, TR), gov_10dd_edpt1 (GD), nama_10_gdp (B1GQ), %s; "
                    "general government S.13, national currency" % an),
            c_lx="stock: debt at end-%s relative to %s GDP" % (an_1, an),
            c_ly="burden: interest as a % of public revenue",
            c_titre="Same debt, different burden: the 27 EU countries in %s" % an,
            c_desc="Each dot is a country. Dotted lines link the false twins picked out by the published rule: similar debt, "
                   "very different burden. Two least-squares lines, one per group, over their observed range.",
            c_note="Dotted lines: false twins (nearest neighbour by debt stock, gap under 10 percentage points, "
                   "three largest gaps in burden).",
            p_lx="average inflation %s-%s (HICP)" % (an_3, an_1),
            p_ly="implicit interest rate: interest %s / debt at end-%s" % (an, an_1),
            p_titre="Price of debt and recent inflation: Europe in %s" % an,
            p_desc="Outside the euro area, the implicit interest rate is closely associated with recent inflation; within the "
                   "euro area, much less so: the Baltic states saw high inflation without a high rate. Sweden, outside the euro, "
                   "has the same implicit interest rate as Germany. Association observed over one year, not causation.",
            p_src="Eurostat prc_hicp_aind (HICP), gov_10a_main, gov_10dd_edpt1, %s" % an,
            p_note="Descriptive relationship over one year, not causal.",
            src_tr="Eurostat gov_10dd_ggd (debt by residual maturity), irt_lt_mcby_a (10-year yields), %s" % an),
    }[lang]
    return {
        "dette-monde-stock%s.svg" % suf: barres_stock(rows, an, T["src_stock"], lang),
        "dette-monde-charge%s.svg" % suf: nuage(
            rows, lambda x: x["stock"], lambda x: x["charge"], 160, 10, 20, 2,
            T["c_lx"], T["c_ly"], "mc", T["c_titre"], T["c_desc"], T["src_eu"], T["c_note"],
            {"FR": "h", "IT": "h", "EL": "h", "DE": "b", "HU": "h", "RO": "h", "PL": "g", "SE": "b", "ES": "h",
             "BE": "h", "PT": "h", "AT": "h", "SI": "d", "HR": "g"},
            droites=[(stats["charge_stock_euro"]["ordonnee"], stats["charge_stock_euro"]["pente"],
                      stats["charge_stock_euro"]["stock_min"], stats["charge_stock_euro"]["stock_max"], COL_EURO),
                     (stats["charge_stock_hors"]["ordonnee"], stats["charge_stock_hors"]["pente"],
                      stats["charge_stock_hors"]["stock_min"], stats["charge_stock_hors"]["stock_max"], COL_HORS)],
            jumeaux=jum, lang=lang),
        "dette-monde-prix%s.svg" % suf: nuage(
            [x for x in rows if x["inflation"] is not None], lambda x: x["inflation"], lambda x: x["prix"], 14, 6, 2, 1,
            T["p_lx"], T["p_ly"], "mp", T["p_titre"], T["p_desc"], T["p_src"], T["p_note"],
            {"FR": "h", "IT": "h", "DE": "d", "HU": "h", "RO": "h", "PL": "h", "SE": "b", "EE": "h", "LT": "h",
             "CZ": "h", "DK": "g", "BG": "d"}, lang=lang),
        "dette-monde-transmission%s.svg" % suf: transmission(rows, an, T["src_tr"], lang),
    }


# ------------------------------------------------------------------ main
def main() -> int:
    args = sys.argv[1:]
    check = "--check" in args
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    an, rows = niveau_europe()
    log("Europe : %d pays, annee %s" % (len(rows), an))
    stats = statistiques(rows)
    jum = faux_jumeaux(rows)
    avances = niveau_avances(an)
    ecarts = ecarts_allemagne(an)
    an_fmi, emergents = niveau_emergents()
    log("Avances hors UE : %d ; emergents : %d (FMI %s)" % (len(avances), len(emergents), an_fmi))
    log("R2 charge~stock %.2f | euro %.2f | hors %.2f | prix~stock %.2f | prix~euro+inflation %.2f"
        % (stats["charge_stock"]["r2"], stats["charge_stock_euro"]["r2"], stats["charge_stock_hors"]["r2"],
           stats["prix_stock_r2"], stats["prix_euro_inflation"]["r2"]))
    for j in jum:
        log("  faux jumeaux : %s / %s (rapport de charge %.1f)" % (j["bas"], j["haut"], j["rapport_charge"]))
    # Les gardes de prose vivent dans affichage() : on le calcule AVANT --check, sinon --check annoncerait
    # « gardes passees » sans en avoir execute aucune (defaut trouve le 30/09/2026).
    aff, aff_en = affichage(an, rows, stats, jum, avances, an_fmi, emergents, ecarts)
    if check:
        log("--check : gardes passees (%d cles d'affichage), rien ecrit." % len(aff))
        return 0
    figs = {}
    for lang in ("fr", "en"):
        figs.update(figures(lang, an, rows, stats, jum))
    payload = {
        "meta": {"annee": an, "releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                 "page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                 "definitions": {"stock": "dette brute / PIB (dette de fin d'année précédente pour la décomposition)",
                                 "prix": "taux implicite : intérêts de l'année / dette de fin d'année précédente "
                                         "(convention de la BCE ; différent du « coût apparent » d'Eurostat, fondé sur la dette moyenne)",
                                 "charge": "intérêts / recettes publiques",
                                 "transmission": "part de la dette à moins d'un an ; écart taux à 10 ans − prix"},
                 # Pendants anglais (convention « _en » à côté du champ français, voir NOMS_EN).
                 "definitions_en": {"stock": "gross debt / GDP (debt at the end of the previous year for the decomposition)",
                                    "prix": "implicit interest rate: interest for the year / debt at the end of the previous year "
                                            "(ECB convention; differs from Eurostat's \"apparent cost\", based on average debt)",
                                    "charge": "interest / public revenue",
                                    "transmission": "share of debt due within one year; 10-year yield minus price"},
                 "niveaux_en": {"europe": "strictly comparable (Eurostat S.13, ESA 2010)",
                                "avances": "with reservations (OECD Economic Outlook, SNA gross financial liabilities, gross interest)",
                                "emergents": "indicative (IMF WEO and World Bank, central government)"},
                 "identite": "I_t/R_t = (D_{t-1}/Y_t) x (I_t/D_{t-1}) / (R_t/Y_t)",
                 "niveaux": {"europe": "strictement comparable (Eurostat S.13, SEC 2010)",
                             "avances": "avec réserve (OCDE Economic Outlook, passifs financiers bruts SCN, intérêts bruts)",
                             "emergents": "indicatif (FMI WEO et Banque mondiale, administration centrale)"}},
        "europe": rows, "statistiques": stats, "faux_jumeaux": jum, "avances": avances,
        "emergents": emergents, "annee_fmi": an_fmi, "ecarts_allemagne": ecarts,
        "affichage": aff,
        "affichage_en": aff_en,
    }
    # releve_le à la RACINE : le sitemap le lit pour toute page déclarant `donnees: [dette_monde]`.
    # À données identiques, on garde l'ancienne date et on n'écrit rien (même règle que
    # update_dette_insee.py : pas de faux « nouveau » dans le sitemap ni de diff vide dans le dépôt).
    releve = payload["meta"]["releve_le"]
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev); p2.pop("releve_le", None); p2["meta"] = dict(p2["meta"], releve_le=None)
            n2 = dict(payload); n2["meta"] = dict(n2["meta"], releve_le=None)
            p2.pop("_licence", None)
            if prev.get("releve_le") \
                    and json.dumps(p2, sort_keys=True, ensure_ascii=False) == json.dumps(n2, sort_keys=True, ensure_ascii=False) \
                    and all((OUT_IMG / nom).exists() and (OUT_IMG / nom).read_text(encoding="utf-8") == svg for nom, svg in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(an, rows, avances, emergents) \
                    and all((OUT_IMG / nom.replace(".svg", ".png")).exists() for nom in figs) \
                    and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches_figures(figs, aff, aff_en):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev.get("releve_le"))
                return 0
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Eurostat, OCDE, FMI, Banque mondiale", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(an, rows, avances, emergents), encoding="utf-8-sig", newline="\n")  # BOM : Excel lit les accents
    import cairosvg
    for nom, svg in figs.items():
        (OUT_IMG / nom).write_text(svg, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / nom), write_to=str(OUT_IMG / nom.replace(".svg", ".png")),
                         output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches_figures(figs, aff, aff_en), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/dette_monde.json, static/dette_monde.json, static/dette_monde.csv, data/figures_monde.json, "
        "%d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
