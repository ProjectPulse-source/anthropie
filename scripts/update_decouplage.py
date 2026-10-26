#!/usr/bin/env python3
"""update_decouplage.py -- page « L'économie mondiale se découple-t-elle de l'énergie ? » (26/10/2026).

Origine : contre-expertise PRO-20261026-033434 (graphe G2 « transformé » : page sur le découplage et ses limites, non sur
le rebond), fiche docs/conception/decouplage-energie-croissance.md.

Découverte : l'intensité énergétique mondiale baisse, la consommation d'énergie monte ; décomposée, la hausse tient plus au
PIB par habitant qu'à la population, et la baisse de l'intensité n'en compense qu'une partie. Dans l'Union européenne,
même producteur, même définition, la consommation baisse pendant que le PIB monte. Décomposition COMPTABLE : elle dit
combien chaque terme a pesé, jamais pourquoi (règle 15 du site) ; aucun effet rebond ne s'en déduit.

Entrée : EIA (U.S. Energy Information Administration), fichier groupé international INTL.zip (sans clé) : consommation
totale d'énergie (TJ), PIB en parité de pouvoir d'achat (milliards de dollars, prix constants), population, monde et UE.
Convention de l'EIA MESURÉE dans le fichier (garde) : électricité hydraulique et éolienne comptée à son contenu électrique
(3 412 Btu/kWh), solaire à un rapport voisin la dernière année (série qui comprend le solaire thermique), nucléaire à la
chaleur du réacteur. Prix constants du PIB vérifiés contre la Banque mondiale.
Témoin (autre producteur, même convention de contenu physique depuis 2025) : offre totale d'énergie de l'Energy Institute,
nouveau jeu d'Our World in Data (catalog.ourworldindata.org/energy/owid_energy ; le site de l'Energy Institute refuse les
scripts), contrôlée contre le total mondial publié par l'EI (valeur TRANSCRITE, EI_PUBLIE) ; PIB et population de la
Banque mondiale. Variante de conversion : PIB aux taux de change de marché (Banque mondiale NY.GDP.MKTP.KD), énergie et
population de l'EIA. UE : baisse de la consommation primaire depuis 2005 chez trois producteurs (EIA, EI, Eurostat).
L'ancien témoin (owid/energy-data, série en substitution mêlant EI et EIA) est retiré : contre-expertise du 26/10/2026,
arbitrage D:/PRO/.claude/external-audits/ARBITRATIONS/G2-DECOUPLAGE-20261026_arbitrage.md.
Rien n'est saisi à la main. Chaque qualificatif de la prose est une garde ; si la donnée la dément, arrêt, rien n'est écrit.

Décomposition : indice de Divisia logarithmique moyen (LMDI-I additif), E = P x (Y/P) x (E/Y) ; somme exacte, contrôlée.

Usage : python scripts/update_decouplage.py [--check] [--mutation=hausse|double|apres2019|fenetres|ue|somme|constant|convention|eolien|solaire|temoin|bande|provenance|marche|marche_ordre|eurostat]
Sorties : data/ et static/decouplage.json, static/decouplage.csv, data/figures_decouplage.json,
          static/img/decouplage-decomposition{,-en}{,-m}.svg + .png
"""
from __future__ import annotations

import csv
import html
import io
import json
import math
import re
import sys
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure  # noqa: E402
import langue_generee as lg  # noqa: E402
import releve_jeu as rj  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "decouplage.json"
OUT_STATIC = ROOT / "static" / "decouplage.json"
OUT_CSV = ROOT / "static" / "decouplage.csv"
OUT_FIGURES = ROOT / "data" / "figures_decouplage.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_FR = "stephane-lalut.com/decouplage-energie-croissance/"
PAGE_EN = "stephane-lalut.com/en/decoupling-energy-growth/"
EIA_BULK = "https://api.eia.gov/bulk/INTL.zip"
OWID = "https://catalog.ourworldindata.org/energy/owid_energy/owid_energy.csv"
OWID_CODEBOOK = "https://catalog.ourworldindata.org/energy/owid_energy/owid_energy.codebook.csv"
OWID_COL = "total_energy_twh"
# Total mondial publié par l'Energy Institute (Statistical Review of World Energy 2025, « Total energy supply », Total World,
# 2024 : 592,22 EJ ; méthode du contenu physique adoptée en 2025, p. 69). Valeur TRANSCRITE (le site de l'EI refuse les
# scripts ; PDF lu le 26/10/2026) : elle qualifie la provenance du témoin et n'entre dans aucun calcul publié.
EI_PUBLIE = (2024, 592.22)
EUROSTAT = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_ind_eff"
            "?geo=EU27_2020&nrg_bal=PEC_EED&unit=MTOE&format=JSON&lang=fr")
AN_ES = 2005                                  # première année de l'indicateur d'Eurostat
WB = "https://api.worldbank.org/v2/country/%s/indicator/%s?format=json&per_page=200&date=1980:2030"
GEOS = {"WORL": ("WLD", "World"), "EU27": ("EUU", "European Union (27)")}   # EIA -> (Banque mondiale, Our World in Data)
SERIES = {"E": "INTL.44-2-%s-TJ.A", "Y": "INTL.4701-34-%s-BDOLPPP.A", "P": "INTL.4702-33-%s-THP.A"}
CONVENTION = {"hydro_q": "INTL.33-12-WORL-QBTU.A", "hydro_kwh": "INTL.33-12-WORL-BKWH.A",
              "eol_q": "INTL.37-12-WORL-QBTU.A", "eol_kwh": "INTL.37-12-WORL-BKWH.A",
              "sol_q": "INTL.116-12-WORL-QBTU.A", "sol_kwh": "INTL.116-12-WORL-BKWH.A",
              "nuc_q": "INTL.4417-2-WORL-QBTU.A", "nuc_kwh": "INTL.27-12-WORL-BKWH.A"}
DEBUT = 2000                                  # fenêtre principale (début du siècle) ; variantes ci-dessous
FENETRES = (1990, 2000, 2010, 2015, 2019)     # « dans toutes les fenêtres testées »
TERMES = ("pop", "rev", "int")

W = 720
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS = "#184f95", "#eb6834", "#8a8781"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
SUFFIXE = {"fr": "", "en": "-en"}
LICENCES = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_FR, "en": "Computed by Stéphane Lalut, CC BY 4.0 · " + PAGE_EN}
LICENCES_M = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com", "en": "Computed by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def lire_url(url: str, quoi: str) -> bytes:
    try:
        with urllib.request.urlopen(url, timeout=180) as r:
            return r.read()
    except Exception as exc:  # réseau, HTTP : jamais une série vide prise pour une donnée
        fail("lecture %s impossible : %s" % (quoi, exc))


# ------------------------------------------------------------------ relevé
def relever_eia() -> tuple[dict, dict, str]:
    """{geo: {E|Y|P: {annee: valeur}}}, ratios de convention, date de mise à jour la plus récente."""
    voulu = {SERIES[k] % g: (g, k) for g in GEOS for k in SERIES}
    voulu.update({v: ("conv", k) for k, v in CONVENTION.items()})
    s, maj = {}, []
    with zipfile.ZipFile(io.BytesIO(lire_url(EIA_BULK, "EIA INTL.zip"))) as z:
        with z.open("INTL.txt") as f:
            for line in f:
                d = json.loads(line)
                cle = voulu.get(d.get("series_id"))
                if not cle:
                    continue
                vals = {}
                for a, v in d.get("data", []):
                    if isinstance(v, (int, float)):
                        vals[int(a)] = float(v)          # « -- », « NA » : absents, jamais des zéros
                s.setdefault(cle[0], {})[cle[1]] = vals
                maj.append(d.get("last_updated", ""))
    manque = [k for k, (g, n) in voulu.items() if n not in s.get(g, {})]
    if manque:
        fail("series EIA absentes du fichier : %s" % manque)
    conv = s.pop("conv")
    return s, conv, max(maj)


def relever_temoin() -> dict:
    """Témoin : offre totale d'énergie de l'Energy Institute (via Our World in Data) ; PIB PPA constant, PIB aux taux de
    marché et population (Banque mondiale) ; consommation primaire de l'UE (Eurostat)."""
    t = {g: {} for g in GEOS}
    rows = csv.DictReader(io.StringIO(lire_url(OWID, "Our World in Data owid_energy").decode("utf-8")))
    noms = {v[1]: g for g, v in GEOS.items()}
    for r in rows:
        g = noms.get(r["country"])
        if g and r.get(OWID_COL):
            t[g].setdefault("E", {})[int(r["year"])] = float(r[OWID_COL]) * 3600   # TWh -> TJ
    for g, (wb, _) in GEOS.items():
        for k, ind in (("Y", "NY.GDP.MKTP.PP.KD"), ("P", "SP.POP.TOTL"), ("Ycour", "NY.GDP.MKTP.PP.CD"), ("Ymer", "NY.GDP.MKTP.KD")):
            d = json.loads(lire_url(WB % (wb, ind), "Banque mondiale %s %s" % (wb, ind)).decode("utf-8"))
            if len(d) < 2 or not d[1]:
                fail("Banque mondiale %s %s : reponse vide" % (wb, ind))
            t[g][k] = {int(x["date"]): float(x["value"]) for x in d[1] if x["value"] is not None}
    for g in GEOS:
        if "E" not in t[g]:
            fail("temoin Energy Institute absent pour %s" % g)
    cb = {r["column"]: r for r in csv.DictReader(io.StringIO(lire_url(OWID_CODEBOOK, "Our World in Data codebook").decode("utf-8")))}
    col = cb.get(OWID_COL) or {}
    m = re.search(r"Energy Institute . Statistical Review of World Energy \((20\d\d)\)", col.get("source", ""))
    if not m:
        fail("edition de l'Energy Institute introuvable pour %s dans le codebook d'Our World in Data" % OWID_COL)
    if "energy content of their gross electrical output" not in col.get("description_from_producer", ""):
        fail("codebook : la colonne %s n'est plus decrite en contenu physique" % OWID_COL)
    t["edition_ei"] = int(m.group(1))
    j = json.loads(lire_url(EUROSTAT, "Eurostat nrg_ind_eff").decode("utf-8"))
    idx = j["dimension"]["time"]["category"]["index"]          # une seule série demandée : l'indice est celui de l'année
    t["es"] = {int(a): float(j["value"][str(i)]) for a, i in idx.items() if str(i) in j["value"]}
    if AN_ES not in t["es"]:
        fail("Eurostat nrg_ind_eff : annee %d absente" % AN_ES)
    return t


# ------------------------------------------------------------------ calcul
def L(a: float, b: float) -> float:
    return a if a == b else (b - a) / math.log(b / a)


def decomp(s: dict, y0: int, y1: int) -> dict:
    E, Y, P = s["E"], s["Y"], s["P"]
    w = L(E[y0], E[y1])
    d = {"pop": w * math.log(P[y1] / P[y0]),
         "rev": w * math.log((Y[y1] / P[y1]) / (Y[y0] / P[y0])),
         "int": w * math.log((E[y1] / Y[y1]) / (E[y0] / Y[y0])),
         "tot": E[y1] - E[y0], "E0": E[y0], "E1": E[y1],
         "dE_pct": 100 * (E[y1] / E[y0] - 1), "dY_pct": 100 * (Y[y1] / Y[y0] - 1),
         "dI_pct": 100 * ((E[y1] / Y[y1]) / (E[y0] / Y[y0]) - 1), "dP_pct": 100 * (P[y1] / P[y0] - 1)}
    d["somme"] = d["pop"] + d["rev"] + d["int"]
    for k in TERMES + ("tot",):
        d[k + "_pct"] = 100 * d[k] / E[y0]          # contribution en % de la consommation de départ
    d["part_compensee"] = -d["int"] / (d["pop"] + d["rev"])
    return d


def calcul(s: dict, t: dict, conv: dict) -> dict:
    y1 = min(max(s[g][k]) for g in GEOS for k in SERIES)      # dernière année commune (énergie, PIB, population)
    yt = min(max(t[g][k]) for g in GEOS for k in ("E", "Y", "P"))
    c_ed, es = t.pop("edition_ei"), t.pop("es")
    c = {"y1": y1, "y0": DEBUT, "yt": min(y1, yt), "s": s, "edition_ei": c_ed}
    for g in GEOS:
        for a in range(min(FENETRES), y1 + 1):
            for k in SERIES:
                if a not in s[g][k]:
                    fail("EIA %s %s : annee %d manquante" % (g, k, a))
    c["W"] = decomp(s["WORL"], DEBUT, y1)
    c["U"] = decomp(s["EU27"], DEBUT, y1)
    c["fen"] = {y0: decomp(s["WORL"], y0, y1) for y0 in FENETRES}
    c["fen_ue"] = {y0: decomp(s["EU27"], y0, y1) for y0 in FENETRES}
    # « elle culmine en {an_pic_ue} » : une seule année au dixième d'exajoule, sinon la phrase est à réécrire
    try:
        c["pic_ue"] = lg.extremum(sorted(s["EU27"]["E"]), lambda a: s["EU27"]["E"][a] / 1e6, 1, True, "pic de la consommation de l'UE")
    except ValueError as exc:
        fail(str(exc))
    c["T"] = decomp(t["WORL"], DEBUT, c["yt"])
    c["TU"] = decomp(t["EU27"], DEBUT, c["yt"])
    # prix constants : la croissance du PIB de l'EIA doit suivre celle du PIB de la Banque mondiale à prix constants
    c["g_eia"] = s["WORL"]["Y"][y1] / s["WORL"]["Y"][DEBUT]
    c["g_wb"] = t["WORL"]["Y"][y1] / t["WORL"]["Y"][DEBUT]
    c["g_wb_cour"] = t["WORL"]["Ycour"][y1] / t["WORL"]["Ycour"][DEBUT]
    # provenance du témoin : son total mondial doit être celui que publie l'Energy Institute (contenu physique)
    c["ei_owid"] = t["WORL"]["E"].get(EI_PUBLIE[0], float("nan")) / 1e6
    # variante de conversion : PIB aux taux de change de marché, seule variable changée (énergie et population de l'EIA)
    mer = {"E": s["WORL"]["E"], "P": s["WORL"]["P"], "Y": t["WORL"]["Ymer"]}
    if any(a not in mer["Y"] for a in FENETRES + (y1,)):
        fail("Banque mondiale NY.GDP.MKTP.KD : annees manquantes")
    c["M"] = {y0: decomp(mer, y0, y1) for y0 in FENETRES}
    # UE : la baisse depuis AN_ES chez trois producteurs (Eurostat ne publie pas cet indicateur avant)
    if y1 not in es:
        fail("Eurostat nrg_ind_eff : annee %d absente" % y1)
    c["ue_es"] = {"EIA": 100 * (s["EU27"]["E"][y1] / s["EU27"]["E"][AN_ES] - 1),
                  "EI": 100 * (t["EU27"]["E"][y1] / t["EU27"]["E"][AN_ES] - 1),
                  "Eurostat": 100 * (es[y1] / es[AN_ES] - 1)}
    c["es_ej"] = es[y1] * 0.041868                            # Mtep -> EJ
    # convention : rapport énergie / électricité, chaque année de la fenêtre la plus longue (une rupture de convention
    # en cours de série fabriquerait de la baisse d'intensité ; question du test de lecture du 26/10/2026)
    ans_c = [a for a in range(min(FENETRES), y1 + 1) if all(a in conv[k] for k in CONVENTION)]
    if len(ans_c) != y1 + 1 - min(FENETRES):
        fail("convention EIA : annees manquantes (%d sur %d)" % (len(ans_c), y1 + 1 - min(FENETRES)))
    ratio = lambda q, a: conv[q + "_q"][a] * 1e15 / (conv[q + "_kwh"][a] * 1e9)  # noqa: E731
    hy = [ratio(q, a) for a in ans_c for q in ("hydro", "eol")]    # hydraulique et éolien, chaque année
    nu = [ratio("nuc", a) for a in ans_c]
    c["btu_hydro_min"], c["btu_hydro_max"], c["btu_nuc_min"], c["btu_nuc_max"] = min(hy), max(hy), min(nu), max(nu)
    c["btu_hydro"], c["btu_nuc"], c["btu_sol"] = ratio("hydro", ans_c[-1]), nu[-1], ratio("sol", ans_c[-1])
    c["an_conv0"], c["an_conv"] = ans_c[0], ans_c[-1]
    c["U19"] = decomp(s["EU27"], DEBUT, 2019)                 # UE arrêtée avant la pandémie et la flambée des prix de 2022
    return c


def mutation(c: dict):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m == "hausse":       # « la consommation mondiale a augmenté »
        c["W"]["tot"] = -1.0
    elif m == "double":     # « {ratio_rp} fois plus » (PIB par habitant / population)
        c["W"]["rev"] = c["W"]["pop"] * 1.1
    elif m == "apres2019":  # « plus de la moitié de la baisse européenne est intervenue après 2019 »
        c["U19"]["tot"] = c["U"]["tot"] * 0.8
    elif m == "fenetres":   # « dans toutes les fenêtres testées »
        c["fen"][2019]["rev"] = c["fen"][2019]["pop"] / 2
    elif m == "ue":         # « dans l'UE, la consommation a baissé pendant que le PIB augmentait »
        c["U"]["tot"] = 1.0
    elif m == "somme":      # somme exacte de la décomposition
        c["W"]["somme"] += 5e5
    elif m == "constant":   # PIB de l'EIA à prix constants
        c["g_eia"] = c["g_wb_cour"]
    elif m == "convention": # électricité renouvelable comptée à son contenu électrique, toute la série
        c["btu_hydro_max"] = 9500.0
    elif m == "eolien":     # éolien compté à son contenu électrique, toute la série
        c["btu_hydro_min"] = 2500.0
    elif m == "solaire":    # « le solaire à un rapport voisin » la dernière année
        c["btu_sol"] = 9000.0
    elif m == "provenance": # le témoin est bien l'offre totale publiée par l'Energy Institute
        c["ei_owid"] = 636.25                     # niveau de l'ancienne série en substitution
    elif m == "marche":     # aux taux de marché aussi, le PIB par habitant pèse plus que la population
        c["M"][1990]["rev"] = c["M"][1990]["pop"] * 0.9
    elif m == "marche_ordre":  # « aux taux de marché, l'intensité retire moins que la population n'ajoute »
        c["M"][DEBUT]["int"] = -c["M"][DEBUT]["pop"] * 1.2
    elif m == "eurostat":   # « trois producteurs, même baisse à quelques points près »
        c["ue_es"]["Eurostat"] = -5.0
    elif m == "temoin":     # même hiérarchie chez l'autre producteur
        c["T"]["rev"] = c["T"]["pop"] * 0.9
    elif m == "bande":      # bande de plausibilité de la consommation mondiale
        c["W"]["E1"] = 1e6
    elif m is not None:
        fail("mutation inconnue : %s" % m)
    return m


# ------------------------------------------------------------------ gardes : chaque qualificatif de la prose
def gardes(c: dict) -> int:
    n = 0

    def g(cond, msg):
        nonlocal n
        n += 1
        if not cond:
            fail("garde : " + msg)

    W_, U = c["W"], c["U"]
    g(4e8 < W_["E1"] < 9e8, "bande : consommation mondiale %.0f TJ hors de 400 a 900 EJ" % W_["E1"])
    g(W_["tot"] > 0 and W_["dI_pct"] < 0, "« l'intensite baisse, la consommation monte » : %.0f TJ, %.1f %%" % (W_["tot"], W_["dI_pct"]))
    r_ = W_["rev"] / W_["pop"]
    g(1.5 <= r_ <= 2.5, "« pese {ratio_rp} fois plus » (PIB par habitant / population) : %.2f, phrase a revoir" % r_)
    g(0.5 * U["tot"] < c["U19"]["tot"] < 0 and c["U19"]["dY_pct"] > 0,
      "UE : « en 2019 deja en baisse ; plus de la moitie de la baisse apres 2019 » : %.0f contre %.0f TJ" % (c["U19"]["tot"], U["tot"]))
    g(all(d["rev"] > d["pop"] and d["tot"] > 0 and d["int"] < 0 for d in c["fen"].values()),
      "« dans toutes les fenetres testees » : %s" % {y: (round(d["pop"] / 1e6), round(d["rev"] / 1e6), round(d["int"] / 1e6))
                                                     for y, d in c["fen"].items()})
    g(U["tot"] < 0 and U["dY_pct"] > 0, "UE : « la consommation a baisse pendant que le PIB augmentait » : %.0f TJ, %.1f %%" % (U["tot"], U["dY_pct"]))
    g(all(d["tot"] < 0 for y, d in c["fen_ue"].items() if y >= DEBUT), "UE : baisse dans les fenetres depuis %d" % DEBUT)
    g(all(abs(d["somme"] - d["tot"]) < 1e-6 * d["E0"] for d in (W_, U, c["T"], c["TU"])), "somme exacte de la decomposition")
    g(abs(c["g_eia"] / c["g_wb"] - 1) < 0.01, "PIB EIA a prix constants : croissance %.3f contre %.3f (Banque mondiale)" % (c["g_eia"], c["g_wb"]))
    g(3400 < c["btu_hydro_min"] and c["btu_hydro_max"] < 3425 and c["btu_nuc_min"] > 9000 and 3400 < c["btu_sol"] < 3600,
      "convention EIA de %d a %d (hydro et eolien %.0f-%.0f Btu/kWh, solaire %.0f la derniere annee, nucleaire des %.0f) : "
      "la phrase sur la frontiere deviendrait fausse"
      % (c["an_conv0"], c["an_conv"], c["btu_hydro_min"], c["btu_hydro_max"], c["btu_sol"], c["btu_nuc_min"]))
    g(abs(c["ei_owid"] / EI_PUBLIE[1] - 1) < 0.005,
      "provenance du temoin : %.2f EJ en %d contre %.2f publies par l'Energy Institute" % (c["ei_owid"], EI_PUBLIE[0], EI_PUBLIE[1]))
    T = c["T"]
    g(T["tot"] > 0 and T["int"] < 0 and T["rev"] > T["pop"],
      "temoin (Energy Institute, Banque mondiale) : meme sens et meme ordre : %s" % {k: round(T[k] / 1e6) for k in TERMES})
    g(c["TU"]["tot"] < 0, "temoin UE : baisse de la consommation (Energy Institute) : %.0f" % c["TU"]["tot"])
    M = c["M"]
    g(all(d["rev"] > d["pop"] and d["tot"] > 0 and d["int"] < 0 for d in M.values()),
      "taux de marche : « le PIB par habitant pese plus que la population, dans chaque fenetre » : %s"
      % {y: (round(d["pop"] / 1e6), round(d["rev"] / 1e6), round(d["int"] / 1e6)) for y, d in M.items()})
    g(-M[DEBUT]["int"] < M[DEBUT]["pop"] < -W_["int"],
      "« aux taux de marche, la baisse de l'intensite retire moins que la population n'ajoute ; en parite, plus » : %.0f, %.0f, %.0f"
      % (-M[DEBUT]["int"] / 1e6, M[DEBUT]["pop"] / 1e6, -W_["int"] / 1e6))
    v = list(c["ue_es"].values())
    g(max(v) < 0 and max(v) - min(v) < 5, "UE depuis %d : « trois producteurs, meme baisse a quelques points pres » : %s"
      % (AN_ES, {k: round(x, 1) for k, x in c["ue_es"].items()}))
    return n


# ------------------------------------------------------------------ affichage (mêmes clés, deux langues)
def affichage(c: dict, lang: str) -> dict:
    f = lambda v, d=0: lg.nombre(v, d, lang)  # noqa: E731
    ej = lambda tj: f(tj / 1e6, 0)  # noqa: E731
    W_, U, T = c["W"], c["U"], c["T"]
    A = {"an0": str(c["y0"]), "an1": str(c["y1"]), "an_t": str(c["yt"]), "an_pic_ue": str(c["pic_ue"]),
         "an_conv": str(c["an_conv"]), "fenetres": lg.enumere([str(y) for y in FENETRES], lang),
         "e0": ej(W_["E0"]), "e1": ej(W_["E1"]), "de_pct": f(W_["dE_pct"]), "dy_pct": f(W_["dY_pct"]),
         "di_pct": f(-W_["dI_pct"], 1), "dp_pct": f(W_["dP_pct"]),
         "pop_ej": ej(W_["pop"]), "rev_ej": ej(W_["rev"]), "int_ej": ej(-W_["int"]), "tot_ej": ej(W_["tot"]),

         "ue_e0": ej(U["E0"]), "ue_e1": ej(U["E1"]), "ue_de_pct": f(-U["dE_pct"]), "ue_dy_pct": f(U["dY_pct"]),
         "ue_di_pct": f(-U["dI_pct"], 1), "ue_pop_ej": ej(U["pop"]), "ue_rev_ej": ej(U["rev"]), "ue_int_ej": ej(-U["int"]),
         "ue_tot_ej": ej(-U["tot"]),
         "t_de_pct": f(T["dE_pct"]), "t_pop_ej": ej(T["pop"]), "t_rev_ej": ej(T["rev"]), "t_int_ej": ej(-T["int"]),
         "t_ue_de_pct": f(-c["TU"]["dE_pct"]), "t_poussee_ej": ej(T["pop"] + T["rev"]),
         "edition_ei": str(c["edition_ei"]), "t_e0": ej(T["E0"]), "t_e1": ej(T["E1"]),
         "ratio_rp": lg.nombre(W_["rev"] / W_["pop"], 1, lang),
         "m_rev_ej": ej(c["M"][DEBUT]["rev"]), "m_int_ej": ej(-c["M"][DEBUT]["int"]), "m_di_pct": f(-c["M"][DEBUT]["dI_pct"]),
         "m_dy_pct": f(c["M"][DEBUT]["dY_pct"]), "an_es": str(AN_ES),
         "es_eia_pct": f(-c["ue_es"]["EIA"]), "es_ei_pct": f(-c["ue_es"]["EI"]), "es_es_pct": f(-c["ue_es"]["Eurostat"]),
         "es_ej": ej(c["es_ej"] * 1e6), "btu_sol": f(c["btu_sol"], 0),
         "ei_publie": f(EI_PUBLIE[1], 2), "an_ei_publie": str(EI_PUBLIE[0]),
         "btu_hydro": f(c["btu_hydro"], 0), "btu_nuc": f(round(c["btu_nuc"], -2), 0), "an_conv0": str(c["an_conv0"]),
         "btu_nuc_min": f(round(c["btu_nuc_min"], -2), 0), "btu_nuc_max": f(round(c["btu_nuc_max"], -2), 0),
         "poussee_ej": ej(W_["pop"] + W_["rev"]), "lmoy_ej": ej(L(W_["E0"], W_["E1"])),
         "ln_i": lg.nombre(math.log(1 + W_["dI_pct"] / 100), 2, lang), "ratio_i": lg.nombre(1 + W_["dI_pct"] / 100, 3, lang), "int_pct_e0": f(-W_["int_pct"], 1),
         "ue19_de_pct": f(-c["U19"]["dE_pct"], 1), "ue19_dy_pct": f(c["U19"]["dY_pct"]),
         "pct": "%" if lang == "en" else " %"}
    for nom, d in (("w", W_), ("u", U)):
        for k in TERMES + ("tot",):
            A["%s_%s_pct" % (nom, k)] = lg.signe(d[k + "_pct"], 1, lang)
    for y0, d in c["fen"].items():                  # tableau des fenêtres (le test de lecture demandait les chiffres)
        for k in TERMES + ("tot",):
            A["f%d_%s" % (y0, k)] = lg.signe(d[k] / 1e6, 0, lang)
    return A


# ------------------------------------------------------------------ figure signature
TXT = {
    "fr": dict(titre="Consommation d'énergie, {an0}-{an1} : ce qui l'a fait monter, ce qui l'a freinée",
               titre_m="Énergie, {an0}-{an1} : ce qui a fait monter la consommation, ce qui l'a freinée",
               desc="Décomposition de la variation de la consommation d'énergie primaire de {an0} à {an1}, en % de la consommation de {an0}. "
                    "Monde : effet de la population {w_pop_pct} %, du PIB par habitant {w_rev_pct} %, de l'intensité énergétique {w_int_pct} %, "
                    "variation totale {w_tot_pct} % (l'intensité elle-même a baissé de {di_pct} %). Union européenne (27 pays) : effet de la population {u_pop_pct} %, "
                    "du PIB par habitant {u_rev_pct} %, de l'intensité énergétique {u_int_pct} %, variation totale {u_tot_pct} %.",
               panneaux=("Monde", "Union européenne (27 pays)"),
               termes=("Effet de la population", "Effet du PIB par habitant", "Effet de l'intensité énergétique (énergie par unité de PIB)", "Variation de la consommation"),
               echelle="effets et variation, en % de la consommation de {an0}",
               source="EIA, données internationales (énergie, PIB en parité de pouvoir d'achat à prix constants, population)",
               note="Énergie primaire consommée sur le territoire (énergie contenue dans les importations non comptée) ; électricité "
                    "hydraulique et éolienne comptée à son contenu électrique, nucléaire à la chaleur produite. Décomposition comptable "
                    "(indice de Divisia), PIB en parité de pouvoir d'achat : elle ne dit pas pourquoi l'intensité baisse. Valeurs "
                    "arrondies au dixième : leur somme peut différer d'un dixième du total.",
               montre="De {an0} à {an1}, la consommation mondiale d'énergie a augmenté de {de_pct} % : la décomposition attribue "
                      "{poussee_ej} exajoules à la population et au PIB par habitant, et en retire {int_ej} à la baisse de l'intensité "
                      "énergétique. Dans l'UE, elle a baissé de {ue_de_pct} %."),
    "en": dict(titre="Energy consumption, {an0}-{an1}: what pushed it up, what held it back",
               titre_m="Energy, {an0}-{an1}: what pushed consumption up, what held it back",
               desc="Decomposition of the change in primary energy consumption from {an0} to {an1}, as % of {an0} consumption. "
                    "World: population effect {w_pop_pct}%, GDP-per-head effect {w_rev_pct}%, energy-intensity effect {w_int_pct}%, total change "
                    "{w_tot_pct}% (intensity itself fell by {di_pct}%). European Union (27 countries): population effect {u_pop_pct}%, "
                    "GDP-per-head effect {u_rev_pct}%, energy-intensity effect {u_int_pct}%, total change {u_tot_pct}%.",
               panneaux=("World", "European Union (27 countries)"),
               termes=("Population effect", "GDP-per-head effect", "Energy-intensity effect (energy per unit of GDP)", "Change in consumption"),
               echelle="effects and change, as % of {an0} consumption",
               source="EIA, international data (energy, GDP at purchasing power parity in constant prices, population)",
               note="Primary energy consumed on the territory (energy embodied in imports not counted); hydro and wind electricity "
                    "counted at its electrical content, nuclear at the heat produced. Accounting decomposition (Divisia index), GDP at "
                    "purchasing power parity: it does not say why intensity falls. Values rounded to one decimal: their sum may "
                    "differ from the total by one tenth.",
               montre="From {an0} to {an1}, world energy consumption rose by {de_pct}%: the decomposition attributes {poussee_ej} "
                      "exajoules to population and GDP per head, and takes {int_ej} away for the fall in energy intensity. In the EU, "
                      "it fell by {ue_de_pct}%."),
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def t_(lang, Aff):
    out = {}
    for k, v in TXT[lang].items():
        out[k] = tuple(x.format(**Aff) for x in v) if isinstance(v, tuple) else v.format(**Aff)
    return out


def couleur(k: str) -> str:
    return BLEU if k == "tot" else (GRIS if k == "int" else ORANGE)


def fig(c, Aff, lang):
    t = t_(lang, Aff)
    pct = Aff["pct"]
    vmin, vmax = -60.0, 75.0
    x0, x1 = 250, 690
    X = lambda v: x0 + (x1 - x0) * (v - vmin) / (vmax - vmin)  # noqa: E731
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="dc-t dc-d" font-family="%s">' % (W, FONT),
         '<title id="dc-t">%s</title><desc id="dc-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W]
    for k, l in enumerate(pied_figure.coupe(t["titre"], 84)):
        e.append('<text x="0" y="%d" font-size="14" font-weight="600" fill="%s">%s</text>' % (18 + 18 * k, INK, esc(l)))
    y = 18 + 18 * len(pied_figure.coupe(t["titre"], 84)) + 10
    e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (x0, y, INK2, esc(t["echelle"])))
    y += 12
    for p, (nom, d) in enumerate(((t["panneaux"][0], "w"), (t["panneaux"][1], "u"))):
        y += 22
        e.append('<text x="0" y="%d" font-size="13" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(nom)))
        y0p = y + 8
        for i, k in enumerate(TERMES + ("tot",)):
            yy = y0p + 28 * i
            v = c["W" if d == "w" else "U"][k + "_pct"]
            for j, l in enumerate(pied_figure.coupe(t["termes"][i], 34)):
                e.append('<text x="0" y="%d" font-size="11"%s fill="%s">%s</text>'
                         % (yy + 14 + 12 * j - 6 * (len(pied_figure.coupe(t["termes"][i], 34)) - 1),
                            ' font-weight="600"' if k == "tot" else "", INK, esc(l)))
            xa, xb = sorted((X(0), X(v)))
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="16" fill="%s"/>' % (xa, yy + 2, max(xb - xa, 1.5), couleur(k)))
            lab = Aff["%s_%s_pct" % (d, k)] + pct
            if v >= 0:
                e.append('<text x="%.1f" y="%d" font-size="11" font-weight="600" fill="%s">%s</text>' % (xb + 4, yy + 14, couleur(k) if k != "int" else INK, esc(lab)))
            else:
                e.append('<text x="%.1f" y="%d" font-size="11" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (xa - 4, yy + 14, INK, esc(lab)))
        y = y0p + 28 * 4
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(0), y0p - 2, X(0), y - 6, INK2))
    return pied_figure.pied(e, y + 6, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_m(c, Aff, lang, svg_d):
    t = t_(lang, Aff)
    pct = Aff["pct"]
    vmin, vmax = -60.0, 75.0
    X = lambda v: 150 * (v - vmin) / (vmax - vmin)  # noqa: E731
    e, y = pied_figure.tete_mobile("dcm", t["titre_m"], desc_de(svg_d), INK, FONT)
    for l in pied_figure.coupe(t["echelle"], 38):
        y += 18
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    for nom, d in ((t["panneaux"][0], "w"), (t["panneaux"][1], "u")):
        y += 30
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(nom)))
        for i, k in enumerate(TERMES + ("tot",)):
            v = c["W" if d == "w" else "U"][k + "_pct"]
            for l in pied_figure.coupe(t["termes"][i], 36):
                y += 18
                e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK, esc(l)))
            y += 18
            xa, xb = sorted((X(0), X(v)))
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="12" fill="%s"/>' % (xa, y - 10, max(xb - xa, 1.5), couleur(k)))
            e.append('<text x="%.1f" y="%d" font-size="%s" font-weight="600" fill="%s">%s</text>'
                     % (max(xb, X(0)) + 6, y, FS_MIN, INK, esc(Aff["%s_%s_pct" % (d, k)] + pct)))
            y += 4
    return pied_figure.pied_mobile(e, y + 16, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fiches(figs, Aff):
    out = {}
    for lang in ("fr", "en"):
        f = "decouplage-decomposition" + SUFFIXE[lang]
        svg = figs[f + ".svg"]
        out[lang] = [dict(id="decomposition", fichier=f, titre=html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1)),
                          montre=TXT[lang]["montre"].format(**Aff[lang]),
                          source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note"))]
    return out


def csv_texte(c) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["zone", "annee", "energie_primaire_tj_eia", "pib_ppa_prix_constants_milliards_usd_eia", "population_milliers_eia"])
    for g, nom in (("WORL", "monde"), ("EU27", "union_europeenne_27")):
        s = c["s"][g]
        for a in sorted(s["E"]):
            if a in s["Y"] and a in s["P"]:
                w.writerow([nom, a, "%.0f" % s["E"][a], "%.1f" % s["Y"][a], "%.1f" % s["P"][a]])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    s, conv, maj = relever_eia()
    t = relever_temoin()
    c = calcul(s, t, conv)
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, lang) for lang in ("fr", "en")}
    if set(Aff["fr"]) != set(Aff["en"]):
        fail("blocs affichage et affichage_en : cles differentes")
    W_ = c["W"]
    log("Monde %d-%d : E %+.1f %% ; pop %+.0f, rev %+.0f, int %+.0f EJ ; compense %.0f %% ; UE E %+.1f %% ; temoin E %+.1f %%"
        % (c["y0"], c["y1"], W_["dE_pct"], W_["pop"] / 1e6, W_["rev"] / 1e6, W_["int"] / 1e6, 100 * W_["part_compensee"],
           c["U"]["dE_pct"], c["T"]["dE_pct"]))
    figs = {}
    for lang in ("fr", "en"):
        sf = SUFFIXE[lang]
        figs["decouplage-decomposition%s.svg" % sf] = fig(c, Aff[lang], lang)
        figs["decouplage-decomposition%s-m.svg" % sf] = fig_m(c, Aff[lang], lang, figs["decouplage-decomposition%s.svg" % sf])
        ec = pied_figure.parite(figs["decouplage-decomposition%s.svg" % sf], figs["decouplage-decomposition%s-m.svg" % sf], FS_MIN, ())
        if ec:
            fail("parite mobile %s : %s" % (lang, " ; ".join(ec)))
    pages = ROOT / "content" / "decouplage-energie-croissance"
    for page, sf in (("_index.md", ""), ("_index.en.md", "-en")):
        if (pages / page).exists():
            ec = pied_figure.controler_page((pages / page).read_text(encoding="utf-8"),
                                            {f: v for f, v in figs.items() if re.fullmatch(r"decouplage-decomposition%s(-m)?\.svg" % sf, f)})
            if ec:
                fail("page %s : %s" % (page, " ; ".join(ec)))
    if check:
        log("--check : %d gardes passees (%d cles), parite controlee, rien ecrit." % (n, len(Aff["fr"])))
        for f_, v in figs.items():
            log("  %s : viewBox %s" % (f_, re.search(r'viewBox="([^"]+)"', v).group(1)))
        return 0
    import cairosvg
    r = lambda d: {k: round(v, 6) for k, v in d.items()}  # noqa: E731
    payload = {"meta": {"page": "https://" + PAGE_FR, "licence": "CC BY 4.0",
                        "source": "EIA, International Energy Data, fichier groupé INTL.zip (api.eia.gov/bulk)", "eia_mis_a_jour": maj,
                        "temoin": "Energy Institute, Statistical Review of World Energy, édition %d, offre totale d'énergie "
                                  "(contenu physique), jeu owid_energy d'Our World in Data ; Banque mondiale NY.GDP.MKTP.PP.KD, "
                                  "NY.GDP.MKTP.KD (variante aux taux de marché) et SP.POP.TOTL ; Eurostat nrg_ind_eff (PEC_EED)"
                                  % c["edition_ei"],
                        "convention_mesuree": {"annee": c["an_conv"], "hydro_btu_par_kwh": round(c["btu_hydro"], 1),
                                               "eolien_et_hydro_min_max": [round(c["btu_hydro_min"], 1), round(c["btu_hydro_max"], 1)],
                                               "solaire_btu_par_kwh": round(c["btu_sol"], 1),
                                               "nucleaire_btu_par_kwh": round(c["btu_nuc"], 1)},
                        "methode": "LMDI-I additif : E = P x (Y/P) x (E/Y) ; contributions en TJ et en % de la consommation de départ",
                        "annee_debut": c["y0"], "annee_fin": c["y1"], "fenetres": list(FENETRES)},
               "decomposition": {"monde": r(c["W"]), "ue27": r(c["U"]),
                                 "monde_fenetres": {str(y): r(d) for y, d in c["fen"].items()},
                                 "ue27_fenetres": {str(y): r(d) for y, d in c["fen_ue"].items()},
                                 "temoin_monde": r(c["T"]), "temoin_ue27": r(c["TU"]),
                                 "monde_fenetres_pib_taux_de_marche": {str(y): r(d) for y, d in c["M"].items()},
                                 "ue27_baisse_depuis_%d_pct" % AN_ES: r(c["ue_es"])},
               "affichage": Aff["fr"], "affichage_en": Aff["en"]}
    releve = None
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            if rj.releve(OUT_DATA, payload, "") == prev["releve_le"]:
                releve = prev["releve_le"]
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; source EIA (domaine public)", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    # PNG rendus EN MÉMOIRE avant toute écriture (même règle que les générateurs du 26/10/2026)
    pngs = {f: cairosvg.svg2png(bytestring=v.encode("utf-8"), output_width=1440, background_color="white") for f, v in figs.items()}
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, v in figs.items():
        (OUT_IMG / f).write_text(v, encoding="utf-8")
        (OUT_IMG / f.replace(".svg", ".png")).write_bytes(pngs[f])
    OUT_FIGURES.write_text(json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/decouplage.json, static/decouplage.csv, data/figures_decouplage.json, %d figures" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
