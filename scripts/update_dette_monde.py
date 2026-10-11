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
sys.path.insert(0, str(ROOT / "scripts"))
import pied_figure as PF  # noqa: E402  (organe commun des pieds et des figures téléphone)
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
ORD_FR = {1: "première", 2: "deuxième", 3: "troisième", 4: "quatrième", 5: "cinquième", 6: "sixième", 7: "septième",
          8: "huitième", 9: "neuvième", 10: "dixième"}
ORD_EN = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth",
          10: "tenth"}
# Entrées dans la zone euro APRÈS l'année des données (décision du Conseil de l'UE du 8 juillet 2025 pour la Bulgarie) : la
# page classe le pays selon l'année des données et le dit (défaut M11 de la phase A du volet 4).
ENTREES_EURO = {"BG": ("1er janvier 2026", "1 January 2026")}
TOL_RATIO = 0.11  # témoin de la variation du ratio : deux ratios publiés à une décimale (même tolérance que le volet 5)
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
    # Fin d'année précédente rapportée à SON PIB (contre-expertise OPTIMUM-22) : pour dire la variation du ratio
    # et empêcher de lire l'écart entre stock de départ et stock de clôture comme une hausse annuelle du ratio.
    DP = eurostat("gov_10dd_edpt1", [an_1, an], na_item="GD", sector="S13", unit="PC_GDP")
    # Variation du ratio calculée sur les montants (dette et PIB de la notification), non par différence de deux ratios
    # publiés déjà arrondis (phase A du volet 5, B3 : 3,0 ici contre 2,9 au volet 5 pour la même année). Les ratios publiés
    # restent le témoin (TOL_RATIO).
    YN = eurostat("gov_10dd_edpt1", [an_1, an], na_item="B1GQ", sector="S1", unit="MIO_NAC")
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
        var_ratio = None
        if (g, an) in D and (g, an_1) in YN and (g, an) in YN:
            var_ratio = 100 * D[(g, an)] / YN[(g, an)] - 100 * d1 / YN[(g, an_1)]
            if (g, an_1) in DP and abs(var_ratio - (dp - DP[(g, an_1)])) > TOL_RATIO:
                fail("%s : variation du ratio %.3f, ratios publies %.1f -> %.1f (temoin)" % (g, var_ratio, DP[(g, an_1)], dp))
        rows.append(dict(code=g, nom=NOMS[g], nom_en=NOMS_EN[g], euro=g in euro, stock_fin=dp,
                         stock_fin_prec=DP.get((g, an_1)), var_ratio=var_ratio, stock=stock, prix=prix, recettes=rec,
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
                            note_en="gross financial liabilities published up to %s only: implicit interest rate not computed" % dern,
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
                        note_en="IMF debt and World Bank interest for the same year; central-government interest payments only",
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


SERIE_ECARTS = ["EL", "IT", "PT", "FR", "SE", "HU"]
# Un style par pays (épaisseur, tirets), le même dans les deux versions : la couleur dit le groupe (zone euro ou non), le
# trait dit le pays — trois lignes bleues identiques ne se distinguaient qu'à leur extrémité (rendu du 11/10).
STYLE_ECARTS = {"FR": (2.8, ""), "IT": (1.8, ""), "EL": (1.1, ""), "PT": (1.5, "2 3"), "SE": (2.6, "7 3"), "HU": (1.4, "7 3")}


def ecarts_allemagne(an: str) -> dict:
    ans = ["1995", "1998", "2007", "2012", an]
    T = eurostat("irt_lt_mcby_a", ans, int_rt="MCBY")
    if any(("DE", a) not in T for a in ans):
        fail("Eurostat irt_lt_mcby_a : taux allemand absent pour une des annees %s" % ans)
    pays = []
    for g, entree in ECARTS_PAYS:
        e = {a: (T[(g, a)] - T[("DE", a)]) if (g, a) in T else None for a in ans}
        pays.append(dict(code=g, nom=NOMS[g], nom_en=NOMS_EN[g], euro_depuis=entree, ecarts=e))
    # Séries annuelles complètes (cinquième figure, contre-expertise OPTIMUM-22) : peu de pays, ceux que la prose cite.
    ans_s = [str(a) for a in range(1995, int(an) + 1)]
    TS = eurostat("irt_lt_mcby_a", ans_s, int_rt="MCBY")
    if any(("DE", a) not in TS for a in ans_s):
        fail("Eurostat irt_lt_mcby_a : taux allemand absent pour une des annees 1995-%s" % an)
    series = {g: {a: round(TS[(g, a)] - TS[("DE", a)], 2) for a in ans_s if (g, a) in TS} for g in SERIE_ECARTS}
    if any(len(v) < 10 for v in series.values()):
        fail("series d'ecarts trop courtes : %s" % {g: len(v) for g, v in series.items()})
    return dict(annees=ans, allemagne={a: T[("DE", a)] for a in ans}, pays=pays, series=series,
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


def blocs_pied(source: str, note: str, lang: str, licence: str = "") -> list:
    return ([(source, INK2, "pied-source")] + ([(note, INK2, "pied-note")] if note else [])
            + [(licence or LIB_FIG[lang]["licence"], MUTED, "pied-licence")])


def pied_monde(e: list[str], y0: float, source: str, note: str, lang: str) -> str:
    """Pied commun (pied_figure, 11 px, renvoi à la ligne) à la place du cartouche en 9 px (défaut M3 de la phase A du
    volet 4) ; la hauteur du SVG suit. Les fiches « Réutiliser » relisent le pied par classe."""
    return PF.pied(e, y0, W, blocs_pied(source, note, lang), GRID)


def marque(x: float, y: float, euro: bool, r: float = 5.5, liseré: bool = True) -> str:
    """Rond pour la zone euro, carré pour les pays hors zone euro (OPTIMUM-22, M4 : la couleur porte le groupe, et la
    forme le double pour qui ne distingue pas les couleurs)."""
    bord = ' stroke="#fff" stroke-width="1"' if liseré else ""
    if euro:
        return '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"%s/>' % (x, y, r, COL_EURO, bord)
    c = r * 0.9
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"%s/>' % (x - c, y - c, 2 * c, 2 * c, COL_HORS, bord)


def legende(x: float, y: float, lang: str = "fr") -> list[str]:
    L = LIB_FIG[lang]
    return [marque(x, y - 4, True, 5, False),
            '<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s</text>' % (x + 9, y, TY_ANNOT, INK2, L["euro"]),
            marque(x + 90, y - 4, False, 5, False),
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


def largeur_texte(s: str, taille: float) -> float:
    """Largeur approchée d'un libellé, en px : chasses d'Arial par classe de lettre (en millièmes d'em). Table
    fixe plutôt qu'une police mesurée : le générateur tourne aussi en CI, où les polices du poste n'existent pas."""
    def chasse(c: str) -> int:
        if c in "ijlI.,;:'’!| ":
            return 250 if c != " " else 278
        if c in "frt-":
            return 333
        if c in "mwMW":
            return 833
        if c.isupper():
            return 667
        return 556
    return sum(chasse(c) for c in s) * taille / 1000


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
    traits = []  # segments dessinés (pointillés, droites), que l'anti-chevauchement des étiquettes doit éviter
    for j in jumeaux:
        a, b = by[j["bas"]], by[j["haut"]]
        traits.append((sx(fx(a)), sy(fy(a)), sx(fx(b)), sy(fy(b))))
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.5" stroke-dasharray="3 3"/>'
                 % (sx(fx(a)), sy(fy(a)), sx(fx(b)), sy(fy(b)), MUTED))
    for (a, b, xa, xb, col) in (droites or []):
        traits.append((sx(xa), sy(a + b * xa), sx(xb), sy(a + b * xb)))
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" opacity="0.7"/>'
                 % (sx(xa), sy(a + b * xa), sx(xb), sy(a + b * xb), col))
    for x in rows:
        e.append(marque(sx(fx(x)), sy(fy(x)), x["euro"]))
    # Placement CALCULÉ (charte du 28/09 : « toute règle graphique doit être calculable, anti-chevauchement
    # compris ») : les points bougent à chaque millésime, et une étiquette posée à la main finit par recouvrir
    # un point, une autre étiquette ou un trait sans que rien ne le dise (« Allemagne » sur les Pays-Bas, nuage
    # des prix ; « Pologne » barrée par la droite hors zone euro -- vus le 04/10). La table d'appel dit QUI est
    # nommé et la position PRÉFÉRÉE ; si elle est prise, on essaie les suivantes, dans l'ordre de POSITIONS
    # (centrée d'abord, charte du site). Recouvrir un point, une étiquette ou sortir du cadre est BLOQUANT ;
    # croiser un trait est seulement évité : à défaut de mieux, le liseré blanc de l'étiquette interrompt le
    # trait sous le texte (Danemark, posé sur le croisement des deux droites). Aucune position sans conflit
    # bloquant : arrêt, avec la liste complète des conflits.
    # Les membres des faux jumeaux sont toujours nommés. Boîte approchée : largeur_texte(), hauteur de capitale.
    POSITIONS = {"h": (0, -9, "middle"), "b": (0, 18, "middle"), "d": (9, 4, "start"), "g": (-9, 4, "end"),
                 "hd": (6, -7, "start"), "hg": (-6, -7, "end"), "bd": (9, 16, "start"), "bg": (-9, 16, "end"),
                 "h2": (0, -13, "middle"), "b2": (0, 22, "middle")}
    noms = dict(etiquettes) if isinstance(etiquettes, dict) else {c: "h" for c in etiquettes}
    for j in jumeaux:
        noms.setdefault(j["bas"], "h")
        noms.setdefault(j["haut"], "h")
    points = [(x["code"], sx(fx(x)), sy(fy(x))) for x in rows]
    boites, echecs = [], []

    def conflits(code, lib, b, px, py):
        """(bloquants, évitables)."""
        out = []
        if b[0] < X0 + 2 or b[2] > W - 2 or b[1] < Y0 - 6 or b[3] > Y1 - 2:
            out.append("« %s » sort du cadre" % lib)
        for c, cx, cy in points:
            if c != code and math.hypot(cx - min(max(cx, b[0]), b[2]), cy - min(max(cy, b[1]), b[3])) < 5.5 + 1.5:
                out.append("« %s » recouvre le point %s" % (lib, c))
        for c, o in boites:
            if b[0] < o[2] and o[0] < b[2] and b[1] < o[3] and o[1] < b[3]:
                out.append("« %s » chevauche l'étiquette de %s" % (lib, c))
        for (x1, y1, x2, y2) in traits:
            n = int(math.hypot(x2 - x1, y2 - y1)) + 1
            # Au ras de son propre point (12 px), un trait qui passe par ce point ne prête à aucune confusion :
            # sans cette exemption, un pays posé sur le croisement des deux droites (Danemark) n'aurait aucune place.
            if any(b[0] - 1 < x1 + (x2 - x1) * k / n < b[2] + 1 and b[1] - 1 < y1 + (y2 - y1) * k / n < b[3] + 1
                   and math.hypot(x1 + (x2 - x1) * k / n - px, y1 + (y2 - y1) * k / n - py) > 12
                   for k in range(n + 1)):
                return out, True
        return out, False

    for x in rows:
        pref = noms.get(x["code"])
        if not pref:
            continue
        px, py = sx(fx(x)), sy(fy(x))
        lib = x[cle_nom]
        larg = largeur_texte(lib, TY_ANNOT) * (1.07 if x["code"] == "FR" else 1.0)
        essais = []
        for pos in [pref] + [q for q in POSITIONS if q != pref]:
            dx, dy, anc = POSITIONS[pos]
            gx = {"middle": px + dx - larg / 2, "end": px + dx - larg, "start": px + dx}[anc]
            b = (gx, py + dy - TY_ANNOT * 0.75, gx + larg, py + dy + 1)
            dur, trait = conflits(x["code"], lib, b, px, py)
            essais.append((dur, trait, dx, dy, anc, b))
            if not dur and not trait:
                break
        libres = [t for t in essais if not t[0]]
        if not libres:
            echecs += essais[0][0]
            continue
        _, _, dx, dy, anc, b = libres[-1] if not libres[-1][1] else libres[0]
        boites.append((x["code"], b))
        gras = ' font-weight="600"' if x["code"] == "FR" else ""
        # Liseré : le même texte, contour blanc, dessous ; masqué aux lecteurs d'écran (sinon lu deux fois).
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="#fff" stroke="#fff" stroke-width="3" '
                 'stroke-linejoin="round" text-anchor="%s"%s aria-hidden="true">%s</text>'
                 % (px + dx, py + dy, TY_ANNOT, anc, gras, esc(lib)))
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>'
                 % (px + dx, py + dy, TY_ANNOT, INK, anc, gras, esc(lib)))
    if echecs:
        fail("%s (%s) : aucune position libre -- %s" % (ident, lang, " ; ".join(echecs)))
    return pied_monde(e, H + 2, source, note, lang)


def barres_stock(rows, an, source, lang="fr"):
    rows = sorted(rows, key=lambda x: -x["stock_fin"])
    hb = 15
    H = 70 + hb * len(rows) + 20
    X0, X1 = 110, W - 60
    vmax = math.ceil(max(x["stock_fin"] for x in rows) / 20) * 20
    T = {"fr": ("Le stock : dette publique en %% du PIB, fin %s",
                "Dette brute de Maastricht des administrations publiques, 27 pays de l'Union européenne, fin %s ; France : "
                + pct(next(x["stock_fin"] for x in rows if x["code"] == "FR")).replace("%", "%%") + ".",
                "Stock brut, sans les actifs publics ni les engagements hors dette (retraites)."),
         "en": ("The stock: public debt as a %% of GDP, end-%s",
                "Maastricht gross debt of general government, 27 European Union countries, end-%s; France: "
                + pct_en(next(x["stock_fin"] for x in rows if x["code"] == "FR")).replace("%", "%%") + ".",
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
    return pied_monde(e, H + 2, source, T[2], lang)


def transmission(rows, an, source, lang="fr"):
    g = [x for x in rows if x["part_1an"] is not None and x["taux10"] is not None]
    by = {x["code"]: x for x in rows}
    fx = lambda x: x["part_1an"]  # noqa: E731
    fy = lambda x: x["taux10"] - x["prix"]  # noqa: E731
    xmax = math.ceil(max(fx(x) for x in g) / 5) * 5
    ymax = math.ceil(max(fy(x) for x in g) * 2) / 2
    ymin = min(0.0, math.floor(min(fy(x) for x in g) * 2) / 2)
    # Extrêmes nommés (auteur, 04/10) : les deux écarts les plus hauts (LU, IE), le plus bas hors Danemark (BG) ;
    # RO nommé pour qu'on ne lui attribue pas l'étiquette de la Hongrie, sa voisine.
    etiq = {"FR": "h", "IT": "d", "DE": "d", "EL": "g", "HU": "g", "SE": "h", "PT": "h", "DK": "d",
            "LU": "d", "IE": "h", "RO": "bd", "BG": "d"}
    # Contre-expertise PRO-20260930-061613 (P1) : repère conditionnel, jamais une prévision -- le <desc> lu par
    # les lecteurs d'écran ne doit pas affirmer plus que le texte visible.
    T = {"fr": ("Pression de refinancement : échéances et écart de taux, %s",
                "part de la dette à échéance résiduelle de moins d'un an",
                "écart rendement à 10 ans − taux implicite du stock, en points",
                "Chaque point est un pays : à droite, une plus grande part de la dette arrive à échéance dans l'année ; en haut, "
                "le rendement harmonisé à 10 ans dépasse davantage le taux implicite du stock. Si les conditions de financement "
                "restaient supérieures au coût de la dette remplacée, les refinancements pousseraient le coût moyen à la hausse. "
                "Sous zéro, l'indicateur est orienté dans l'autre sens. Repère, non prévision. France : %s de la dette à moins "
                "d'un an, écart de %s." % (pct(by["FR"]["part_1an"]), LOC["fr"]["point"](by["FR"]["taux10"] - by["FR"]["prix"])),
                "Rendement de convergence à 10 ans, non le coût de toutes les émissions nouvelles. Repère, non prévision."),
         "en": ("Refinancing pressure: maturities and rate gap, %s",
                "share of debt with a residual maturity of less than one year",
                "10-year yield − implicit interest rate on the stock, in percentage points",
                "Each dot is a country: further right, a larger share of the debt falls due within the year; higher up, "
                "the harmonised 10-year yield exceeds the implicit interest rate on the stock by more. If financing conditions "
                "stayed above the cost of the debt being replaced, refinancing would push the average cost up. "
                "Below zero, the indicator points the other way. A marker, not a forecast. France: %s of debt due within a "
                "year, gap of %s." % (pct_en(by["FR"]["part_1an"]), LOC["en"]["point"](by["FR"]["taux10"] - by["FR"]["prix"])),
                "10-year convergence yield, not the cost of all new issuance. A marker, not a forecast.")}[lang]
    nb, pt = LOC[lang]["nb"], LIB_FIG[lang]["pt"]
    return nuage(g, fx, fy, xmax, ymax, 5, 0.5, T[1], T[2], "mt", T[0] % an, T[3], source, T[4],
                 etiq, ymin=ymin, fmt_y=lambda v: nb(v, 1) + pt, lang=lang)


# ------------------------------------------------------------------ écarts avec l'Allemagne, 1995-an
def ecarts_figure(ecarts: dict, an: str, lang: str = "fr") -> str:
    """Cinquième figure (contre-expertise OPTIMUM-22) : trente ans d'écarts de taux à 10 ans avec l'Allemagne, peu de pays
    (ceux que la prose cite), pays restés hors de l'euro en témoins. Échelle bornée à 10 points pour que les écarts
    ordinaires restent lisibles : la Grèce, qui sort du cadre en 2010-2013, porte sa valeur de 2012 en toutes lettres."""
    S, nb = ecarts["series"], LOC[lang]["nb"]
    L = LIB_FIG[lang]
    ans = sorted({a for v in S.values() for a in v}, key=int)
    a0, a1 = int(ans[0]), int(ans[-1])
    H, X0, X1, Y0, Y1 = 400, 46, W - 92, 70, 340
    vmin, vmax = -1.0, 10.0
    sx = lambda a: X0 + (int(a) - a0) / (a1 - a0) * (X1 - X0)  # noqa: E731
    sy = lambda v: Y1 - (min(max(v, vmin), vmax) - vmin) / (vmax - vmin) * (Y1 - Y0)  # noqa: E731
    T = {"fr": ("Trente ans d'écarts de taux avec l'Allemagne, %s-%s" % (a0, a1),
                "écart de rendement à 10 ans avec l'Allemagne, en points",
                "avant l'euro", "2012", "Grèce : %s points en 2012 ; ▲ hors échelle",
                "Rendement de convergence à 10 ans moins celui de l'Allemagne, en points. Cercles : membres de la zone euro "
                "aujourd'hui ; carrés : pays restés hors de l'euro.",
                "Taux de marché à 10 ans, non le taux implicite du stock. Comparateurs, non groupe de contrôle."),
         "en": ("Thirty years of yield spreads over Germany, %s-%s" % (a0, a1),
                "10-year yield spread over Germany, in percentage points",
                "before the euro", "2012", "Greece: %s points in 2012; ▲ off the scale",
                "10-year convergence yield minus Germany's, in percentage points. Circles: current euro-area members; "
                "squares: countries that stayed outside the euro.",
                "10-year market yields, not the implicit interest rate on the stock. Comparators, not a control group.")}[lang]
    eur = {"EL", "IT", "PT", "FR", "ES", "IE"}
    v = lambda g, a: S[g].get(str(a))  # noqa: E731
    desc = (T[5] + " " + {"fr": "Italie : %s en 1995, %s en 1998 ; Suède : %s en 1995, %s en 1998 ; Grèce : %s en 2012, "
                                "Portugal : %s ; en %s, Hongrie : %s, Italie : %s, Grèce : %s, France : %s, Portugal : %s, Suède : %s.",
                          "en": "Italy: %s in 1995, %s in 1998; Sweden: %s in 1995, %s in 1998; Greece: %s in 2012, "
                                "Portugal: %s; in %s, Hungary: %s, Italy: %s, Greece: %s, France: %s, Portugal: %s, Sweden: %s."}[lang]
            % (nb(v("IT", 1995), 2), nb(v("IT", 1998), 2), nb(v("SE", 1995), 2), nb(v("SE", 1998), 2),
               nb(v("EL", 2012), 1), nb(v("PT", 2012), 2), an, nb(v("HU", an), 2), nb(v("IT", an), 2), nb(v("EL", an), 2),
               nb(v("FR", an), 2), nb(v("PT", an), 2), nb(v("SE", an), 2)))
    e = entete(H, "me", T[0], desc)
    e.append('<text x="0" y="18" font-size="%d" font-weight="600" fill="%s">%s</text>' % (TY_TITRE, INK, esc(T[0])))
    e += legende(W - 250, 18, lang)
    # Bande « avant l'euro » (1995-1998), libellée sous elle ; repère 2012.
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#f0efe9"/>' % (sx(1995), Y0, sx(1998) - sx(1995), Y1 - Y0))
    e.append('<text x="%.1f" y="%d" font-size="%d" fill="%s" text-anchor="middle">%s</text>'
             % ((sx(1995) + sx(1998)) / 2, Y1 + 30, TY_AXE, INK2, esc(T[2])))
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (sx(2012), Y0, sx(2012), Y1, MUTED))
    for g in range(-1, 11):
        if g % 2 and g != -1:
            continue
        yy = sy(g)
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, yy, X1, yy, AXIS if g == 0 else GRID))
        e.append('<text x="%d" y="%.1f" font-size="%d" fill="%s" text-anchor="end">%s</text>'
                 % (X0 - 6, yy + 4, TY_AXE, MUTED, nb(g, 0)))
    e.append('<text x="%d" y="%d" font-size="%d" fill="%s">%s</text>' % (X0, Y0 - 10, TY_AXE, INK2, esc(T[1])))
    for a in range(a0, a1 + 1, 5):
        e.append('<text x="%.1f" y="%d" font-size="%d" fill="%s" text-anchor="%s">%d</text>'
                 % (sx(a), Y1 + 15, TY_AXE, MUTED, "end" if a == a1 else ("start" if a == a0 else "middle"), a))
    e.append('<defs><clipPath id="me-clip"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath></defs>' % (X0, Y0 - 2, X1 - X0, Y1 - Y0 + 2))
    fins = []
    for g in SERIE_ECARTS:
        pts = sorted(S[g].items(), key=lambda p: int(p[0]))
        col = COL_EURO if g in eur else COL_HORS
        w, dd = STYLE_ECARTS[g]
        dash = ' stroke-dasharray="%s"' % dd if dd else ""
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%.1f"%s clip-path="url(#me-clip)"/>'
                 % (" ".join("%.1f,%.1f" % (sx(a), Y1 - (vv - vmin) / (vmax - vmin) * (Y1 - Y0)) for a, vv in pts), col, w, dash))
        fins.append((sy(pts[-1][1]), g, col, pts[-1][1]))
    # Étiquettes directes en fin de ligne, écart minimal garanti (même règle que les autres figures du dossier).
    fins.sort()
    pos = []
    for yy, g, col, val in fins:
        y_ = max(yy, pos[-1] + 13) if pos else yy
        pos.append(y_)
    debord = pos[-1] - (Y1 - 2)
    if debord > 0:
        pos = [p - debord for p in pos]
    for (yy, g, col, val), y_ in zip(fins, pos):
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s"%s>%s</text>'
                 % (X1 + 6, y_ + 4, TY_ANNOT, col, ' font-weight="600"' if g == "FR" else "",
                    esc("%s %s" % (NOMS[g] if lang == "fr" else NOMS_EN[g], nb(val, 2)))))
    # Valeurs hors échelle marquées (OPTIMUM-23) : un triangle au bord supérieur pour chaque année où un pays dépasse 10 points.
    for g in SERIE_ECARTS:
        for a, vv in S[g].items():
            if vv > vmax:
                x = sx(a)
                e.append('<polygon points="%.1f,%d %.1f,%d %.1f,%d" fill="%s"/>' % (x - 4, Y0 + 1, x + 4, Y0 + 1, x, Y0 - 6, COL_EURO if g in eur else COL_HORS))
    for trait in ('fill="#fff" stroke="#fff" stroke-width="4" stroke-linejoin="round" aria-hidden="true"',
                  'fill="%s"' % COL_EURO):
        e.append('<text x="%.1f" y="%d" font-size="%d" %s>%s</text>'
                 % (sx(2012) + 8, Y0 + 12, TY_ANNOT, trait, esc(T[4] % nb(v("EL", 2012), 1))))
    return pied_monde(e, H + 2, ecarts["source"] if lang == "fr" else ecarts["source_en"], T[6], lang)


# ------------------------------------------------------------------ téléphone
# Versions téléphone (phase B du volet 4, OPTIMUM-22 : « véritable figure éditoriale, non simple réduction ») : 300 de large,
# police jamais sous 13,5, organe commun pied_figure ; servies d'office par le shortcode figure-svg. On ne nomme que les
# points qui fondent le propos ; le tableau de la page donne les autres. Chaque valeur dessinée en gras figure dans la
# description de la version détaillée (PF.parite).
WM, FSM = PF.LARGEUR_M, PF.POLICE_M


def tm(x, y, s, fill=INK2, anchor="start", weight=None, size=None):
    w = ' font-weight="%s"' % weight if weight else ""
    return ('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, size or FSM, fill, anchor, w, esc(s)))


def desc_de(svg: str) -> str:
    import html as _h
    import re as _r
    return _h.unescape(_r.search(r"<desc[^>]*>(.*?)</desc>", svg, _r.S).group(1))


def lignes_m(e: list[str], y: float, texte: str, fill=MUTED, weight=None) -> float:
    for l in PF.coupe(texte, 38):
        y += 18
        e.append(tm(0, y, l, fill, weight=weight))
    return y


def legende_m(e: list[str], y: float, lang: str) -> float:
    L = LIB_FIG[lang]
    y += 20
    e.append(marque(6, y - 5, True, 5, False))
    e.append(tm(16, y, L["euro"]))
    e.append(marque(150, y - 5, False, 5, False))
    e.append(tm(160, y, L["hors"]))
    return y


def pied_m(e: list[str], y: float, source: str, note: str, lang: str) -> str:
    lic = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
           "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}[lang]
    return PF.pied_mobile(e, y, blocs_pied(source, note, lang, lic), GRID)


def nuage_m(rows, fx, fy, xmax, ymin, ymax, pasx, pasy, fmt_x, fmt_y, lx, ly, ident, titre, svg_d, source, note, lang,
            noms, valeurs=None, jumeaux=(), droites=None, liste=None, x0=40):
    """liste : [(code, valeur)] dits SOUS la figure quand leurs points sont trop serrés pour être nommés dedans."""
    e, y = PF.tete_mobile(ident, titre, desc_de(svg_d), INK, FONT)
    y = legende_m(e, y + 4, lang)
    y = lignes_m(e, y + 4, ly)
    X0, X1, Y0 = x0, WM - 8, y + 14
    Y1 = Y0 + 230
    sx = lambda v: X0 + v / xmax * (X1 - X0)  # noqa: E731
    sy = lambda v: Y1 - (v - ymin) / (ymax - ymin) * (Y1 - Y0)  # noqa: E731
    v = ymin
    while v <= ymax + 1e-9:
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, sy(v), X1, sy(v), AXIS if v == 0 else GRID))
        e.append(tm(X0 - 5, sy(v) + 5, fmt_y(v), MUTED, "end"))
        v += pasy
    v = 0
    while v <= xmax + 1e-9:
        e.append(tm(sx(v), Y1 + 19, fmt_x(v), MUTED, "middle" if 0 < v < xmax else ("start" if v == 0 else "end")))
        v += pasx
    by = {x["code"]: x for x in rows}
    for j in jumeaux:
        a, b = by[j["bas"]], by[j["haut"]]
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.5" stroke-dasharray="3 3"/>'
                 % (sx(fx(a)), sy(fy(a)), sx(fx(b)), sy(fy(b)), MUTED))
    for (a, b, xa, xb, col) in (droites or []):
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" opacity="0.7"/>'
                 % (sx(xa), sy(a + b * xa), sx(xb), sy(a + b * xb), col))
    pts = [(x["code"], sx(fx(x)), sy(fy(x))) for x in rows]
    for x in rows:
        e.append(marque(sx(fx(x)), sy(fy(x)), x["euro"], 4.2))
    boites, echecs = [], []
    for code in noms:
        x = by.get(code)
        if not x:
            continue
        px, py = sx(fx(x)), sy(fy(x))
        lib = x[LOC[lang]["nom"]] + ((" " + valeurs[code]) if valeurs and code in valeurs else "")
        gras = valeurs and code in valeurs
        larg = largeur_texte(lib, FSM) * (1.08 if gras else 1.0)
        ok = None
        for dx, dy, anc in ((7, 5, "start"), (-7, 5, "end"), (0, -9, "middle"), (0, 19, "middle"), (6, -7, "start"),
                            (-6, -7, "end"), (6, 17, "start"), (-6, 17, "end")):
            gx = {"start": px + dx, "end": px + dx - larg, "middle": px + dx - larg / 2}[anc]
            b = (gx, py + dy - FSM * 0.75, gx + larg, py + dy + 2)
            if b[0] < 0 or b[2] > WM or b[1] < Y0 - 4 or b[3] > Y1 + 2:
                continue
            if any(c != code and b[0] - 4 < cx < b[2] + 4 and b[1] - 4 < cy < b[3] + 4 for c, cx, cy in pts):
                continue
            if any(b[0] < o[2] and o[0] < b[2] and b[1] < o[3] and o[1] < b[3] for o in boites):
                continue
            ok = (dx, dy, anc, b)
            break
        if not ok:
            echecs.append(lib)
            continue
        dx, dy, anc, b = ok
        boites.append(b)
        e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="#fff" stroke="#fff" stroke-width="3" stroke-linejoin="round" '
                 'text-anchor="%s"%s aria-hidden="true">%s</text>'
                 % (px + dx, py + dy, FSM, anc, ' font-weight="600"' if gras else "", esc(lib)))
        e.append(tm(px + dx, py + dy, lib, INK, anc, "600" if gras else None))
    if echecs:
        fail("%s (%s, téléphone) : aucune position libre pour %s" % (ident, lang, ", ".join(echecs)))
    y = lignes_m(e, Y1 + 26, lx)
    for code, val in (liste or []):
        x = by[code]
        y += 22
        e.append(marque(6, y - 5, x["euro"], 5, False))
        e.append(tm(18, y, x[LOC[lang]["nom"]], INK2))
        e.append(tm(WM, y, val, INK, "end", "600"))
    return pied_m(e, y + 14, source, note, lang)


def barres_stock_m(rows, an, svg_d, source, note, titre, lang):
    rows = sorted(rows, key=lambda x: -x["stock_fin"])
    e, y = PF.tete_mobile("ms-m", titre, desc_de(svg_d), INK, FONT)
    y = legende_m(e, y + 4, lang)
    X0, X1 = 96, WM - 56
    vmax = max(x["stock_fin"] for x in rows)
    y += 10
    for x in rows:
        fr_ = x["code"] == "FR"
        w = x["stock_fin"] / vmax * (X1 - X0)
        e.append(tm(X0 - 6, y + 12, x[LOC[lang]["nom"]], INK, "end", "600" if fr_ else None))
        e.append('<rect x="%d" y="%.1f" width="%.1f" height="13" fill="%s"/>' % (X0, y + 2, w, COL_EURO if x["euro"] else COL_HORS))
        e.append(tm(X0 + w + 4, y + 12, LOC[lang]["pct"](x["stock_fin"]), INK if fr_ else INK2, weight="600" if fr_ else None))
        y += 19
    return pied_m(e, y + 10, source, note, lang)


def ecarts_figure_m(ecarts, an, svg_d, lang):
    S, nb = ecarts["series"], LOC[lang]["nb"]
    ans = sorted({a for v in S.values() for a in v}, key=int)
    a0, a1 = int(ans[0]), int(ans[-1])
    T = {"fr": ("Trente ans d'écarts de taux avec l'Allemagne", "Écart à 10 ans avec l'Allemagne, en points · Grèce hors "
                "échelle en 2010-2013", "avant l'euro", "Grèce : %s points en 2012", "en %s :" % a1,
                "Taux de marché à 10 ans, non le taux implicite. Comparateurs, non groupe de contrôle."),
         "en": ("Thirty years of yield spreads over Germany", "10-year spread over Germany, in points · Greece off the "
                "scale in 2010-2013", "before the euro", "Greece: %s points in 2012", "in %s:" % a1,
                "10-year market yields, not the implicit rate. Comparators, not a control group.")}[lang]
    e, y = PF.tete_mobile("me-m", T[0], desc_de(svg_d), INK, FONT)
    SERIE_M = [g for g in SERIE_ECARTS if g != "PT"]  # cinq lignes au plus sur un téléphone ; le Portugal reste dans la détaillée
    y = legende_m(e, y + 4, lang)
    y = lignes_m(e, y + 4, T[1])
    X0, X1, Y0 = 26, WM - 6, y + 14
    Y1 = Y0 + 220
    vmin, vmax = -1.0, 10.0
    sx = lambda a: X0 + (int(a) - a0) / (a1 - a0) * (X1 - X0)  # noqa: E731
    sy = lambda v: Y1 - (min(max(v, vmin), vmax) - vmin) / (vmax - vmin) * (Y1 - Y0)  # noqa: E731
    e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#f0efe9"/>' % (sx(1995), Y0, sx(1998) - sx(1995), Y1 - Y0))
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="3 3"/>' % (sx(2012), Y0, sx(2012), Y1, MUTED))
    for g in (0, 2, 4, 6, 8, 10):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, sy(g), X1, sy(g), AXIS if g == 0 else GRID))
        e.append(tm(X0 - 4, sy(g) + 5, nb(g, 0), MUTED, "end"))
    for a, anc in ((a0, "start"), (2012, "middle"), (a1, "end")):
        e.append(tm(sx(a), Y1 + 19, str(a), MUTED, anc))
    e.append('<defs><clipPath id="mem-clip"><rect x="%d" y="%.1f" width="%d" height="%.1f"/></clipPath></defs>' % (X0, Y0 - 2, X1 - X0, Y1 - Y0 + 2))
    eur = {"EL", "IT", "PT", "FR", "ES", "IE"}
    for g in SERIE_M:
        pts = sorted(S[g].items(), key=lambda p: int(p[0]))
        col = COL_EURO if g in eur else COL_HORS
        w, dd = STYLE_ECARTS[g]
        dash = ' stroke-dasharray="%s"' % dd if dd else ""
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%.1f"%s clip-path="url(#mem-clip)"/>'
                 % (" ".join("%.1f,%.1f" % (sx(a), Y1 - (vv - vmin) / (vmax - vmin) * (Y1 - Y0)) for a, vv in pts), col, w, dash))
    for g in SERIE_M:
        for a, vv in S[g].items():
            if vv > vmax:
                x = sx(a)
                e.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (x - 4, Y0 + 1, x + 4, Y0 + 1, x, Y0 - 6, COL_EURO if g in eur else COL_HORS))
    e.append(tm(X0 + 4, Y0 + 14, T[3] % nb(S["EL"]["2012"], 1), COL_EURO))
    y = Y1 + 44
    e.append('<rect x="%d" y="%.1f" width="14" height="12" fill="#f0efe9" stroke="%s"/>' % (X0, y - 11, GRID))
    e.append(tm(X0 + 20, y, T[2], INK2))
    y += 22
    e.append(tm(0, y, T[4], INK2))
    for g in sorted(SERIE_M, key=lambda g: -S[g][str(a1)]):
        y += 21
        col = COL_EURO if g in eur else COL_HORS
        w, dd = STYLE_ECARTS[g]
        e.append('<line x1="0" y1="%.1f" x2="20" y2="%.1f" stroke="%s" stroke-width="%.1f"%s/>'
                 % (y - 5, y - 5, col, w, ' stroke-dasharray="%s"' % dd if dd else ""))
        e.append(tm(26, y, NOMS[g] if lang == "fr" else NOMS_EN[g], INK2))
        e.append(tm(WM, y, nb(S[g][str(a1)], 2) + LIB_FIG[lang]["pt"], INK, "end", "600"))
    return pied_m(e, y + 16, ecarts["source"] if lang == "fr" else ecarts["source_en"], T[5], lang)


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
        # --- Phase B (OPTIMUM-22) ---
        # M1 : les deux dénominateurs de la charge française, et ce que change le dénominateur.
        A["fr_ipib"] = pc(ipib["FR"], 2)
        A["fr_rang_ipib"] = L["ordinal"](rang_ipib)
        A["fr_rang_charge"] = L["ordinal"](rang_charge)
        A["n_plus_ipib"] = str(len(plus_ipib))
        A["plus_ipib"] = ", ".join(x[nom] for x in plus_ipib)
        A["fr_rang_recettes"] = L["ordinal"](rang_rec)
        # Décomposition des faux jumeaux (identité vérifiée : produit = rapport des charges).
        A["j_f_stock"], A["j_f_prix"], A["j_f_rec"] = nb(f_stock, 2), nb(f_prix, 2), nb(f_rec, 2)
        # Les deux droites : rapport des pentes.
        A["pente_rapport"] = nb(s["charge_stock_hors"]["pente"] / s["charge_stock_euro"]["pente"], 1)
        # Trois temporalités françaises : stock de départ, stock de clôture, ratio de fin d'année précédente.
        A["fr_stock_fin_prec"] = pc(F["stock_fin_prec"])
        A["fr_var_ratio"] = nb(F["var_ratio"], 1)
        A["fr_ecart_stocks"] = nb(F["stock_fin"] - F["stock"], 1)
        A["fr_rang_prix_euro"] = L["ordinal"](rang_prix_euro)
        A["bg_entree"] = ENTREES_EURO["BG"][0 if L is LOC["fr"] else 1]
        return A

    # Calculs de la phase B, communs aux deux langues.
    ipib = {x["code"]: x["charge"] * x["recettes"] / 100 for x in rows}
    rang_ipib = sorted(ipib, key=lambda c: -ipib[c]).index("FR") + 1
    rang_charge = sorted(rows, key=lambda x: -x["charge"]).index(F) + 1
    plus_ipib = sorted((x for x in rows if x["stock"] < F["stock"] and ipib[x["code"]] > ipib["FR"]), key=lambda x: x["stock"])
    rang_rec = sorted(rows, key=lambda x: -x["recettes"]).index(F) + 1
    f_stock, f_prix, f_rec = hi["stock"] / lo["stock"], hi["prix"] / lo["prix"], lo["recettes"] / hi["recettes"]
    euro_prix = sorted((x for x in rows if x["euro"]), key=lambda x: x["prix"])
    rang_prix_euro = euro_prix.index(F) + 1
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
        ("le prix français est un peu sous la moyenne simple de la zone euro (écart < 0,4 point)",
         F["prix"] < stats["prix_moyen_euro"] and stats["prix_moyen_euro"] - F["prix"] < 0.4),
        # Phase B (OPTIMUM-22), chaque phrase nouvelle :
        ("changer de dénominateur déplace la France : rapporté au PIB, moins de pays moins endettés la dépassent",
         0 < len(plus_ipib) < len(moins_chers_que_fr)),
        ("recettes françaises « parmi les plus élevées de l'Union » (trois premiers rangs)", rang_rec <= 3),
        ("décomposition des faux jumeaux : produit des trois facteurs = rapport des charges",
         abs(f_stock * f_prix * f_rec - hi["charge"] / lo["charge"]) < 1e-9),
        ("l'essentiel de l'écart des faux jumeaux vient du taux implicite", f_prix > f_stock and f_prix > f_rec),
        ("relation nettement plus pentue hors de l'euro (rapport des pentes > 2)",
         stats["charge_stock_hors"]["pente"] > 2 * stats["charge_stock_euro"]["pente"]),
        ("l'écart entre stock de départ et stock de clôture n'est pas la variation annuelle du ratio",
         F["stock_fin_prec"] is not None and (F["stock_fin"] - F["stock_fin_prec"]) < (F["stock_fin"] - F["stock"])),
        ("la Bulgarie, classée hors zone euro pour l'année des données, y entre après elle",
         not by["BG"]["euro"] and "BG" in ENTREES_EURO),
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
            ("ecarts", "dette-monde-ecarts",
             "Convergence avant l'euro, Suède comprise ; décrochage des membres fragiles en 2012, puis resserrement : "
             "trente ans d'écarts avec l'Allemagne, pays restés hors de l'euro en comparateurs."),
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
             "The most quoted ranking: it shows neither the average interest cost of the debt nor the share of revenue it absorbs."),
            ("ecarts", "dette-monde-ecarts-en",
             "Convergence before the euro, Sweden included; the fragile members' break in 2012, then narrowing: "
             "thirty years of spreads over Germany, with countries outside the euro as comparators."),
        ],
    }
    res = {}
    for lang in ("fr", "en"):
        out = []
        for ident, fichier, montre in MONTRE[lang]:
            svg = figs[fichier + ".svg"]
            titre = _html.unescape(_re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            # Pied relu PAR CLASSE (pied_figure.lire), non plus par la taille de police du cartouche.
            source, note, licence = (PF.lire(svg, k) for k in ("pied-source", "pied-note", "pied-licence"))
            if not source or licence != LIB_FIG[lang]["licence"]:
                fail("fiche %s : pied illisible dans le SVG" % fichier)
            out.append(dict(id=ident, fichier=fichier, titre=titre, montre=montre, source=source, precaution=note))
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


def figures(lang: str, an: str, rows: list[dict], stats: dict, jum: list[dict], ecarts: dict) -> dict[str, str]:
    """Les quatre figures d'une langue : même dessin, mêmes données, seuls les textes changent. Fichiers anglais
    suffixés -en (dette-monde-charge-en.svg), comme ceux de update_dette_insee.py."""
    an_1, an_3 = str(int(an) - 1), str(int(an) - 3)
    suf = "" if lang == "fr" else "-en"
    by = {x["code"]: x for x in rows}
    T = {
        "fr": dict(
            src_stock="Eurostat gov_10dd_edpt1, dette de Maastricht, fin %s" % an,
            src_eu=("Eurostat gov_10a_main (D41PAY, TR), gov_10dd_edpt1 (GD), nama_10_gdp (B1GQ), %s ; "
                    "administrations publiques S.13, monnaie nationale" % an),
            c_lx="stock : dette fin %s rapportée au PIB %s" % (an_1, an),
            c_ly="charge : intérêts en % des recettes publiques",
            c_titre="Même dette, charge différente : les 27 pays de l'UE en %s" % an,
            c_desc="Chaque point est un pays. Les pointillés relient les faux jumeaux désignés par la règle publiée : dette voisine, "
                   "charge très différente. Deux droites de moindres carrés, une par groupe, sur leur plage observée. "
                   "Charge : Hongrie %s, Slovénie %s, France %s, Italie %s." % tuple(
                       pct(by[c]["charge"]) for c in ("HU", "SI", "FR", "IT")),
            c_note="Pointillés : faux jumeaux (plus proche voisin en stock, écart < 10 points, trois plus grands écarts de charge).",
            p_lx="inflation moyenne %s-%s (IPCH)" % (an_3, an_1),
            p_ly="taux implicite : intérêts %s / dette fin %s" % (an, an_1),
            p_titre="Prix de la dette et inflation récente : l'Europe en %s" % an,
            p_desc="Hors de la zone euro, le taux implicite est étroitement associé à l'inflation récente ; dans la zone euro, beaucoup "
                   "moins : les pays baltes ont connu une forte inflation sans taux élevé. La Suède, hors euro, a le même taux implicite "
                   "que l'Allemagne. Association observée sur une année, non causalité. Taux implicite : Hongrie %s, Roumanie %s, "
                   "France %s, Allemagne %s, Suède %s." % tuple(pct(by[c]["prix"], 2) for c in ("HU", "RO", "FR", "DE", "SE")),
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
            c_desc="Each dot is a country. Dotted lines link the look-alike pairs picked out by the published rule: similar debt, "
                   "very different burden. Two least-squares lines, one per group, over their observed range. "
                   "Burden: Hungary %s, Slovenia %s, France %s, Italy %s." % tuple(
                       pct_en(by[c]["charge"]) for c in ("HU", "SI", "FR", "IT")),
            c_note="Dotted lines: look-alike pairs (nearest neighbour by debt stock, gap under 10 percentage points, "
                   "three largest gaps in burden).",
            p_lx="average inflation %s-%s (HICP)" % (an_3, an_1),
            p_ly="implicit interest rate: interest %s / debt at end-%s" % (an, an_1),
            p_titre="Average interest cost and recent inflation: Europe in %s" % an,
            p_desc="Outside the euro area, the implicit interest rate is closely associated with recent inflation; within the "
                   "euro area, much less so: the Baltic states saw high inflation without a high rate. Sweden, outside the euro, "
                   "has the same implicit interest rate as Germany. Association observed over one year, not causation. Implicit "
                   "rate: Hungary %s, Romania %s, France %s, Germany %s, Sweden %s." % tuple(
                       pct_en(by[c]["prix"], 2) for c in ("HU", "RO", "FR", "DE", "SE")),
            p_src="Eurostat prc_hicp_aind (HICP), gov_10a_main, gov_10dd_edpt1, %s" % an,
            p_note="Descriptive relationship over one year, not causal.",
            src_tr="Eurostat gov_10dd_ggd (debt by residual maturity), irt_lt_mcby_a (10-year yields), %s" % an),
    }[lang]
    D = {
        "dette-monde-stock%s.svg" % suf: barres_stock(rows, an, T["src_stock"], lang),
        "dette-monde-charge%s.svg" % suf: nuage(
            rows, lambda x: x["stock"], lambda x: x["charge"], 160, 10, 20, 2,
            T["c_lx"], T["c_ly"], "mc", T["c_titre"], T["c_desc"], T["src_eu"], T["c_note"],
            {"FR": "h", "IT": "h", "EL": "h", "DE": "b", "HU": "h", "RO": "h", "PL": "g", "SE": "b", "ES": "h",
             "BE": "h", "PT": "h", "AT": "h", "SI": "d", "HR": "b",
             # Les deux moins endettés de chaque groupe (auteur, 04/10) : sans eux, le bas de l'échelle restait anonyme.
             "BG": "g", "DK": "g", "EE": "g", "LU": "g"},
            droites=[(stats["charge_stock_euro"]["ordonnee"], stats["charge_stock_euro"]["pente"],
                      stats["charge_stock_euro"]["stock_min"], stats["charge_stock_euro"]["stock_max"], COL_EURO),
                     (stats["charge_stock_hors"]["ordonnee"], stats["charge_stock_hors"]["pente"],
                      stats["charge_stock_hors"]["stock_min"], stats["charge_stock_hors"]["stock_max"], COL_HORS)],
            jumeaux=jum, lang=lang),
        "dette-monde-prix%s.svg" % suf: nuage(
            [x for x in rows if x["inflation"] is not None], lambda x: x["inflation"], lambda x: x["prix"], 14, 6, 2, 1,
            T["p_lx"], T["p_ly"], "mp", T["p_titre"], T["p_desc"], T["p_src"], T["p_note"],
            {"FR": "h", "IT": "h", "DE": "b2", "HU": "h", "RO": "h", "PL": "h", "SE": "bg", "EE": "d", "LT": "d",
             "CZ": "h", "DK": "g", "BG": "d",
             # Les deux taux implicites les plus bas (auteur, 04/10 : nommer le bas de l'échelle).
             "LU": "g", "IE": "b"}, lang=lang),
        "dette-monde-transmission%s.svg" % suf: transmission(rows, an, T["src_tr"], lang),
        "dette-monde-ecarts%s.svg" % suf: ecarts_figure(ecarts, an, lang),
    }
    return dict(D, **figures_m(lang, an, rows, stats, jum, ecarts, D, T, suf))


def figures_m(lang, an, rows, stats, jum, ecarts, D, T, suf):
    """Versions téléphone, recomposées ; contrôlées contre les versions détaillées (parité, police)."""
    nb, pc, pt = LOC[lang]["nb"], LIB_FIG[lang]["pc"], LIB_FIG[lang]["pt"]
    by = {x["code"]: x for x in rows}
    P = LOC[lang]["pct"]
    an_1 = str(int(an) - 1)
    titres = {"fr": ("Même dette, charge différente : l'UE en %s" % an, "Prix de la dette et inflation récente, %s" % an,
                     "Pression de refinancement, %s" % an, "Dette publique en % du PIB, fin " + an),
              "en": ("Same debt, different burden: the EU in %s" % an, "Average interest cost and recent inflation, %s" % an,
                     "Refinancing pressure, %s" % an, "Public debt as a % of GDP, end-" + an)}[lang]
    lx = {"fr": ("Stock : dette fin %s / PIB %s" % (an_1, an), "Inflation moyenne des trois années précédentes (IPCH)",
                 "Part de la dette à moins d'un an"),
          "en": ("Stock: debt end-%s / %s GDP" % (an_1, an), "Average inflation over the three previous years (HICP)",
                 "Share of debt due within a year")}[lang]
    ly = {"fr": ("Charge : intérêts en % des recettes", "Taux implicite du stock", "Rendement à 10 ans − taux implicite"),
          "en": ("Burden: interest as a % of revenue", "Implicit interest rate on the stock", "10-year yield − implicit rate")}[lang]
    infl = [x for x in rows if x["inflation"] is not None]
    trans = [x for x in rows if x["part_1an"] is not None and x["taux10"] is not None]
    tr_y = [x["taux10"] - x["prix"] for x in trans]
    sortie = {
        "dette-monde-charge%s-m.svg" % suf: nuage_m(
            rows, lambda x: x["stock"], lambda x: x["charge"], 160, 0, 10, 80, 2, lambda v: nb(v, 0) + pc, lambda v: nb(v, 0) + pc,
            lx[0], ly[0], "mc-m", titres[0], D["dette-monde-charge%s.svg" % suf], T["src_eu"], T["c_note"], lang,
            ["HU", "SI", "FR", "IT", "EL", "RO"], {c: P(by[c]["charge"]) for c in ("HU", "SI", "FR")}, jumeaux=jum[:1],
            droites=[(stats["charge_stock_euro"]["ordonnee"], stats["charge_stock_euro"]["pente"],
                      stats["charge_stock_euro"]["stock_min"], stats["charge_stock_euro"]["stock_max"], COL_EURO),
                     (stats["charge_stock_hors"]["ordonnee"], stats["charge_stock_hors"]["pente"],
                      stats["charge_stock_hors"]["stock_min"], stats["charge_stock_hors"]["stock_max"], COL_HORS)]),
        "dette-monde-prix%s-m.svg" % suf: nuage_m(
            infl, lambda x: x["inflation"], lambda x: x["prix"], 14, 0, 6, 7, 1, lambda v: nb(v, 0) + pc, lambda v: nb(v, 0) + pc,
            lx[1], ly[1], "mp-m", titres[1], D["dette-monde-prix%s.svg" % suf], T["p_src"], T["p_note"], lang,
            ["HU", "RO", "PL", "EE"], None,
            liste=[(c, P(by[c]["prix"], 2)) for c in ("HU", "FR", "DE", "SE")]),
        "dette-monde-transmission%s-m.svg" % suf: nuage_m(
            trans, lambda x: x["part_1an"], lambda x: x["taux10"] - x["prix"],
            math.ceil(max(x["part_1an"] for x in trans) / 10) * 10, min(-1.0, math.floor(min(tr_y))), math.ceil(max(tr_y)),
            10, 0.5, lambda v: nb(v, 0) + pc, lambda v: nb(v, 1) + pt,
            lx[2], ly[2], "mt-m", titres[2], D["dette-monde-transmission%s.svg" % suf], T["src_tr"],
            {"fr": "Repère, non prévision.", "en": "A marker, not a forecast."}[lang], lang,
            ["FR", "DK", "SE", "PT"], {"FR": nb(by["FR"]["taux10"] - by["FR"]["prix"], 2) + pt}, x0=56),
        "dette-monde-stock%s-m.svg" % suf: barres_stock_m(
            rows, an, D["dette-monde-stock%s.svg" % suf], T["src_stock"],
            {"fr": "Stock brut, sans les actifs publics ni les engagements hors dette.",
             "en": "Gross stock, excluding public assets and liabilities outside debt."}[lang], titres[3], lang),
        "dette-monde-ecarts%s-m.svg" % suf: ecarts_figure_m(ecarts, an, D["dette-monde-ecarts%s.svg" % suf], lang),
    }
    for nom, svg in sortie.items():
        d = D[nom.replace("-m.svg", ".svg")]
        ecarts_ = PF.parite(d, svg, FSM)
        if ecarts_:
            fail("%s : %s" % (nom, " ; ".join(ecarts_)))
        for h in PF.hors_cadre(svg, WM):
            log("  a verifier au rendu, %s : %s" % (nom, h))
    return sortie


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
        figs.update(figures(lang, an, rows, stats, jum, ecarts))
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
                                    "transmission": "share of debt due within one year; 10-year yield minus implicit interest rate"},
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
