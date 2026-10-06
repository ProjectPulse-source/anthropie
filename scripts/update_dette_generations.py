#!/usr/bin/env python3
"""update_dette_generations.py -- prolongement « La dette publique est-elle un fardeau pour les générations futures ? »

Test décisif avant la page (protocole écrit avant le calcul, verdict, pièces) :
D:\\PRO\\06_PROMOTION\\RECHERCHE_GENERATIONS_FUTURES_2026-10-03\\test_decisif\\ (PROTOCOLE.md, VERDICT.md, 03/10/2026).
Les trois arguments qui allègent le fardeau, chacun confronté à la série qui peut le démentir :

  A1. « On transmet aussi des actifs » : à quoi a correspondu le besoin de financement des administrations publiques
      (Eurostat gov_10a_main, S13). Identité des comptes, par année :
          -B9 = -B8N + (P51G - P51C + P52_P53 + NP) + (D9PAY - D9REC)
          besoin de financement = désépargne nette + acquisitions nettes d'actifs non financiers + transferts en capital nets
      TÉMOIN 1 (bloquant pour la France) : les ratios qu'Eurostat PUBLIE en % du PIB (gov_10a_main, PC_GDP), que le
      calcul n'utilise pas ; tolérance TOL ; vu mordre au test (PIB de l'année précédente : 683 rejets sur 810).
      TÉMOIN 2 (autre cadre statistique) : le patrimoine net des APU dans les bilans (tous les actifs non financiers,
      produits N1N et non produits N2N, nama_10_nfa_bs ; valeur financière nette consolidée, nasa_10_f_bs) : sa baisse
      doit concorder avec la faible part en actifs, quelle que soit l'année de départ (garde de sensibilité).
      La décomposition dit la COMPOSITION COMPTABLE des déficits, non la charge transmise (Auerbach, Gokhale et
      Kotlikoff 1991 : le déficit dépend de l'étiquetage) ; la prose ne dit jamais « financé ».
  A2. « On se la doit à nous-mêmes » : dette des APU par secteur détenteur (BCE, statistiques de finances publiques,
      GFS), 1995-dernière année ; contrôle de cohérence contre Eurostat gov_10dd_ggd (même déclarant : cohérence, pas
      indépendance). TÉMOIN DE PÉRIMÈTRE État : Banque de France, Webstat, série DET (CSV de la page publique, l'API ne
      la sert pas aux scripts) ; dernière observation : relevé daté du graphique de l'AFT (source Banque de France),
      gardé contre une erreur de transcription et contre la péremption (garde de fraîcheur).
  A3. « Le vrai fardeau est le vieillissement » : indicateur S2 de la Commission (Debt Sustainability Monitor), position
      budgétaire initiale contre coût du vieillissement. COR : ordre de grandeur illustratif, présenté À PART, jamais
      comme une composante de S2 (arbitrage PRO-20261003-195656, B4). Pièces sans API, archivées dans
      scripts/sources_generations/ et vérifiées par leur empreinte (SHA256SUMS).

Une garde numérique protège contre une variation des données, jamais contre une interprétation : une phrase dont le
défaut est conceptuel se corrige dans la prose, pas par une garde (même arbitrage).

Chaque qualificatif de la page est une garde (fonction gardes) ; une donnée qui dément une phrase arrête tout, rien
n'est écrit. Page en français seulement (le prolongement n'a pas de miroir anglais : exclusion déclarée).

MISE À JOUR. Séries Eurostat et BCE : workflow dette-monde.yml (mêmes notifications d'avril et d'octobre).
Pièces : à la main, à chaque édition — Debt Sustainability Monitor (publication annuelle, début d'année), rapport
annuel du COR (juin), série Webstat DET et relevé de l'AFT (chaque trimestre ; le générateur s'arrête si Webstat
rattrape le relevé, qu'il faut alors remplacer ou retirer). Geste : déposer la nouvelle pièce dans scripts/sources_generations/, mettre à jour SOURCES
ci-dessous et SHA256SUMS, relancer ; si une garde refuse, réécrire la phrase, jamais desserrer la garde.

Usage : python scripts/update_dette_generations.py [--check] [--mutation-garde]
Sorties : data/ et static/dette_generations.json, static/dette_generations.csv, data/figures_generations.json,
          static/img/dette-generations-{actifs,detention,vieillissement}.svg + .png
"""
from __future__ import annotations

import csv
import hashlib
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
OUT_DATA = ROOT / "data" / "dette_generations.json"
OUT_STATIC = ROOT / "static" / "dette_generations.json"
OUT_CSV = ROOT / "static" / "dette_generations.csv"
OUT_FIGURES = ROOT / "data" / "figures_generations.json"
OUT_IMG = ROOT / "static" / "img"
PIECES = ROOT / "scripts" / "sources_generations"
PAGE_URL = "stephane-lalut.com/dette-publique-generations-futures/"

# Pièces sans API : fichier, libellé de l'édition (dit dans la page par jeton, jamais saisi dans la prose)
SOURCES = {
    "dsm": dict(fichier="dsm2025_country_fiches.xlsx", lib="Debt Sustainability Monitor 2025", publie="2026-02",
                producteur="Commission européenne, DG ECFIN, Institutional Paper 332, février 2026",
                url="https://economy-finance.ec.europa.eu/publications/debt-sustainability-monitor-2025_en"),
    "cor": dict(fichier="cor_ra2026_synthese.xlsx", lib="rapport annuel de juin 2026", publie="2026-06",
                producteur="Conseil d'orientation des retraites, données de la synthèse, scénario de référence",
                url="https://www.cor-retraites.fr/rapports-du-cor/rapport-annuel-cor-juin-2026-evolutions-perspectives-retraites-france"),
    # Témoin de périmètre État (règle constante de l'auteur, 03/10/2026 : anti-robot -> changer de canal, jamais abandonner
    # la donnée). L'API Webstat ne sert pas ces observations aux scripts ; le CSV est celui du bouton « Télécharger les
    # données » de la page publique de la série (format long), archivé tel quel. Mise à jour : trimestrielle, à la main.
    "det": dict(fichier="webstat_DET.Q.FR.1315.F33000.M.Z9.8.F.csv", lib="Banque de France, série DET.Q.FR.1315.F33000.M.Z9.8.F",
                producteur="Banque de France, Webstat : détention par les non-résidents de la dette négociable de l'État (en %), valeur de marché",
                url="https://webstat.banque-france.fr/fr/catalogue/det/DET.Q.FR.1315.F33000.M.Z9.8.F"),
    # Dernière observation (arbitrage PRO-20261003-195656, B3) : relevé daté du graphique de l'AFT, source Banque de
    # France ; l'image n'est pas servie aux scripts, ses deux étiquettes sont transcrites dans la pièce avec son empreinte.
    "aft": dict(fichier="aft_non_residents_releve_2026T1.json", lib="Agence France Trésor, d'après la Banque de France",
                producteur="Agence France Trésor, page « Principaux chiffres », graphique des non-résidents (source Banque de France)",
                url="https://www.aft.gouv.fr/fr/principaux-chiffres-dette"),
}

TOL = 0.11            # ratios publiés à une décimale
TOL_BOUCLAGE = 0.05   # identité des comptes, par année, en points de PIB
SEUIL_BESOIN = 30.0   # contre-population : besoin de financement cumulé minimal pour comparer la part en actifs
API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/%s?format=JSON&%s"
ECB = "https://data-api.ecb.europa.eu/service/data/GFS/%s?format=csvdata&detail=dataonly"

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCE = "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL

PAYS = {"AT": ("Autriche", "l'Autriche"), "BE": ("Belgique", "la Belgique"), "BG": ("Bulgarie", "la Bulgarie"),
        "CY": ("Chypre", "Chypre"), "CZ": ("Tchéquie", "la Tchéquie"), "DE": ("Allemagne", "l'Allemagne"),
        "DK": ("Danemark", "le Danemark"), "EE": ("Estonie", "l'Estonie"), "EL": ("Grèce", "la Grèce"),
        "ES": ("Espagne", "l'Espagne"), "FI": ("Finlande", "la Finlande"), "FR": ("France", "la France"),
        "HR": ("Croatie", "la Croatie"), "HU": ("Hongrie", "la Hongrie"), "IE": ("Irlande", "l'Irlande"),
        "IT": ("Italie", "l'Italie"), "LT": ("Lituanie", "la Lituanie"), "LU": ("Luxembourg", "le Luxembourg"),
        "LV": ("Lettonie", "la Lettonie"), "MT": ("Malte", "Malte"), "NL": ("Pays-Bas", "les Pays-Bas"),
        "PL": ("Pologne", "la Pologne"), "PT": ("Portugal", "le Portugal"), "RO": ("Roumanie", "la Roumanie"),
        "SE": ("Suède", "la Suède"), "SI": ("Slovénie", "la Slovénie"), "SK": ("Slovaquie", "la Slovaquie")}
TRIM = ["premier trimestre", "deuxième trimestre", "troisième trimestre", "quatrième trimestre"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
LETTRES = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
           "treize", "quatorze", "quinze", "seize"]


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


def lettres(n: int) -> str:
    return LETTRES[n] if 0 <= n < len(LETTRES) else str(n)


def enumere(noms: list[str]) -> str:
    return noms[0] if len(noms) == 1 else ", ".join(noms[:-1]) + " et " + noms[-1]


def maj(s: str) -> str:
    return s[:1].upper() + s[1:]


# ------------------------------------------------------------------ données
def fetch(url: str, essais: int = 4) -> bytes:
    for k in range(essais):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com (stephane@stephane-lalut.com)"})
            with urllib.request.urlopen(req, timeout=240) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if k == essais - 1:
                fail("reseau : %s (%s)" % (url[:120], e))
            time.sleep(15 * (k + 1))   # le portail de la BCE répond parfois 504 : on attend, on ne contourne pas
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


def bce(cle: str) -> dict[tuple[str, str], dict[int, float]]:
    """GFS de la BCE : {(pays, secteur détenteur): {année: % du PIB}}."""
    raw = fetch(ECB % cle).decode("utf-8")
    if not raw.startswith("KEY"):
        fail("BCE %s : reponse qui n'est pas un CSV de donnees" % cle)
    out: dict = {}
    for x in csv.DictReader(io.StringIO(raw)):
        if x["OBS_VALUE"]:
            out.setdefault((x["REF_AREA"], x["COUNTERPART_SECTOR"]), {})[int(x["TIME_PERIOD"])] = float(x["OBS_VALUE"])
    return out


def piece(cle: str) -> Path:
    """Une pièce archivée n'est lue que si son empreinte est celle de SHA256SUMS."""
    f = PIECES / SOURCES[cle]["fichier"]
    sums = dict(reversed(l.split(None, 1)) for l in (PIECES / "SHA256SUMS").read_text(encoding="utf-8").split("\n") if l.strip())
    if not f.is_file():
        fail("piece absente : %s" % f)
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    if sums.get(f.name) != h:
        fail("piece %s : empreinte %s differente de SHA256SUMS" % (f.name, h[:16]))
    return f


# ------------------------------------------------------------------ A1 : à quoi ont correspondu les déficits
ITEMS = ("B9", "P51G", "P51C", "B8N", "D9PAY", "D9REC", "D92PAY", "NP", "P52_P53")
PUBLIES = ("B9", "P51G", "P51C", "B8N")


def emplois():
    M = {it: eurostat("gov_10a_main", na_item=it, sector="S13", unit="MIO_NAC") for it in ITEMS}
    pub = {it: eurostat("gov_10a_main", na_item=it, sector="S13", unit="PC_GDP") for it in PUBLIES}
    Y = eurostat("gov_10dd_edpt1", na_item="B1GQ", sector="S1", unit="MIO_NAC")
    R, ecartes, calculables = {}, [], 0
    for (p, a) in sorted(M["B9"]):
        if p not in PAYS or (p, a) not in Y or any((p, a) not in M[it] for it in ("P51G", "P51C", "B8N", "D9PAY", "D9REC")):
            continue
        calculables += 1
        y = Y[(p, a)]
        r = {it: M[it].get((p, a), 0.0) / y * 100 for it in ITEMS}
        if not all((p, a) in pub[it] for it in PUBLIES):
            ecartes.append(dict(pays=p, annee=a, motif="ratio publié absent"))
            continue
        e = {it: r[it] - pub[it][(p, a)] for it in PUBLIES}
        if any(abs(v) > TOL for v in e.values()):
            ecartes.append(dict(pays=p, annee=a, motif="écart au ratio publié", ecarts={k: round(v, 2) for k, v in e.items() if abs(v) > TOL}))
            continue
        B, E = -r["B9"], -r["B8N"]
        N = r["P51G"] - r["P51C"]
        K = N + r["NP"] + r["P52_P53"]          # acquisitions nettes d'actifs non financiers, usure déduite
        T = r["D9PAY"] - r["D9REC"]
        bou = B - (E + K + T)
        if abs(bou) > TOL_BOUCLAGE:
            ecartes.append(dict(pays=p, annee=a, motif="identité des comptes non bouclée", ecart=round(bou, 3)))
            continue
        R.setdefault(p, {})[a] = dict(besoin=B, desepargne=E, investissement_net=N, actifs=K, transferts=T,
                                      aides_investissement=r["D92PAY"], d92_publie=(p, a) in M["D92PAY"],
                                      besoin_meur=-M["B9"][(p, a)], actifs_meur=M["P51G"][(p, a)] - M["P51C"][(p, a)]
                                      + M["NP"].get((p, a), 0.0) + M["P52_P53"].get((p, a), 0.0))
    retenues = sum(len(v) for v in R.values())
    if calculables != retenues + len(ecartes):
        fail("conservation rompue : %d calculables, %d retenues, %d ecartees" % (calculables, retenues, len(ecartes)))
    return R, ecartes, calculables


def cumul(an: dict, a0: int, a1: int):
    if not all(a in an for a in range(a0, a1 + 1)):
        return None
    L = [an[a] for a in range(a0, a1 + 1)]
    s = {k: sum(x[k] for x in L) for k in ("besoin", "desepargne", "investissement_net", "actifs", "transferts", "aides_investissement",
                                            "besoin_meur", "actifs_meur")}
    s.update(debut=a0, fin=a1, annees=len(L))
    if s["besoin"] > 0:
        s.update(part_actifs=100 * s["actifs"] / s["besoin"], part_desepargne=100 * s["desepargne"] / s["besoin"],
                 part_transferts=100 * s["transferts"] / s["besoin"], part_actifs_euros=100 * s["actifs_meur"] / s["besoin_meur"],
                 part_investissement_net=100 * s["investissement_net"] / s["besoin"])
    return s


def patrimoine(fin: int):
    Y = eurostat("gov_10dd_edpt1", na_item="B1GQ", sector="S1", unit="MIO_NAC")
    # Tous les actifs non financiers (arbitrage PRO-20261003-195656, B2) : produits N1N (actifs fixes, stocks, objets de
    # valeur) et non produits N2N (terrains surtout) ; les terrains seuls (N211N) gardés pour la phrase sur leur valeur.
    prod = eurostat("nama_10_nfa_bs", sector="S13", unit="CP_MNAC", asset10="N1N")
    nonprod = eurostat("nama_10_nfa_bs", sector="S13", unit="CP_MNAC", asset10="N2N")
    terrains = eurostat("nama_10_nfa_bs", sector="S13", unit="CP_MNAC", asset10="N211N")
    bf = eurostat("nasa_10_f_bs", sector="S13", unit="MIO_NAC", na_item="BF90", co_nco="CO", finpos="LIAB")
    ans = [a for a in range(fin - 30, fin + 1) if all(("FR", a) in s for s in (Y, prod, nonprod, terrains, bf))]
    if not ans:
        fail("patrimoine : aucune annee complete pour la France")
    out = {a: dict(annee=a, actifs_produits=prod[("FR", a)] / Y[("FR", a)] * 100, actifs_non_produits=nonprod[("FR", a)] / Y[("FR", a)] * 100,
                   terrains=terrains[("FR", a)] / Y[("FR", a)] * 100, valeur_financiere_nette=bf[("FR", a)] / Y[("FR", a)] * 100,
                   patrimoine_net_meur=prod[("FR", a)] + nonprod[("FR", a)] + bf[("FR", a)]) for a in ans}
    for x in out.values():
        x["patrimoine_net"] = x["actifs_produits"] + x["actifs_non_produits"] + x["valeur_financiere_nette"]
        if x["terrains"] > x["actifs_non_produits"] + 1e-9:
            fail("patrimoine %d : terrains superieurs aux actifs non produits" % x["annee"])
    return [out[a] for a in ans]


# ------------------------------------------------------------------ A2 : qui détient la dette
def detention():
    tot = bce("A.N..W0.S13.S1.C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T")
    nr = bce("A.N..W1.S13.S1.C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T")
    res = bce("A.N..W2.S13..C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T")
    fr_ = []
    for a in sorted(tot.get(("FR", "S1"), {})):
        t, n, r, b = tot[("FR", "S1")][a], nr.get(("FR", "S1"), {}).get(a), res.get(("FR", "S1"), {}).get(a), res.get(("FR", "S121"), {}).get(a)
        if None in (n, r, b):
            fail("BCE : detention francaise incomplete en %d" % a)
        if abs(n + r - t) > 0.15:
            fail("BCE : non-residents + residents != total en %d (%.2f)" % (a, n + r - t))
        fr_.append(dict(annee=a, dette=t, non_residents=n, residents=r, banque_centrale=b, autres_residents=r - b,
                        part_non_residents=100 * n / t, part_banque_centrale=100 * b / t, part_autres_residents=100 * (r - b) / t))
    # Cohérence avec Eurostat (même déclarant : un écart signale une clé ou un millésime cassé, pas une contre-preuve)
    ggd = {s: eurostat("gov_10dd_ggd", na_item="GD", sector="S13", unit="PC_GDP", maturity="TOTAL", sector2=s) for s in ("S2", "S121")}
    vus = 0
    for x in fr_:
        a = x["annee"]
        if ("FR", a) in ggd["S2"]:
            vus += 1
            if abs(ggd["S2"][("FR", a)] - x["non_residents"]) > 0.15 or abs(ggd["S121"][("FR", a)] - x["banque_centrale"]) > 0.15:
                fail("BCE et Eurostat divergent sur la detention francaise en %d" % a)
    if vus < 3:
        fail("controle BCE/Eurostat : moins de trois annees communes")
    pays = {}
    for p in PAYS:
        t, n = tot.get((p, "S1"), {}), nr.get((p, "S1"), {})
        if t and n:
            a = max(set(t) & set(n))
            pays[p] = dict(annee=a, part_non_residents=100 * n[a] / t[a])
    return fr_, pays, vus


def etat_negociable():
    """Témoin de périmètre : part des titres négociables de l'État détenue par des non-résidents (Banque de France,
    valeur de marché), fin de chaque année ; autre champ (État, titres négociables, valeur de marché) que la série BCE
    (administrations publiques, toute la dette, valeur nominale)."""
    rows = list(csv.DictReader(io.StringIO(piece("det").read_text(encoding="utf-8-sig")), delimiter=";"))
    if not rows or rows[0].get("series_key") != "DET.Q.FR.1315.F33000.M.Z9.8.F" or rows[0].get("UNIT") != "PC":
        fail("piece Webstat DET : serie ou unite inattendue (le fichier n'est pas celui attendu)")
    obs = {x["time_period"]: float(x["obs_value"].replace(",", ".")) for x in rows if x["obs_value"]}
    dernier = max(obs)
    fins = [dict(annee=int(k[:4]), part=v) for k, v in sorted(obs.items()) if k.endswith("Q4")]
    if not 0 < fins[-1]["part"] < 100 or len(fins) < 20:
        fail("piece Webstat DET : moins de vingt fins d'annee ou valeur hors bornes")
    rel = json.loads(piece("aft").read_text(encoding="utf-8"))
    robs = {k: float(v) for k, v in rel["observations"].items()}
    rder = max(robs)
    # Garde de transcription : la période commune doit égaler Webstat à 0,1 point près.
    communs = [k for k in robs if k in obs]
    if not communs or any(abs(robs[k] - obs[k]) > 0.1 for k in communs):
        fail("releve AFT : la periode commune ne concorde pas avec Webstat (%s)" % {k: (robs[k], obs.get(k)) for k in robs})
    # Garde de fraîcheur : le relevé n'a de raison d'être que s'il est plus récent que Webstat.
    if rder <= dernier:
        fail("releve AFT perime : Webstat publie %s, le releve s'arrete a %s ; remplacer ou retirer le releve" % (dernier, rder))
    return dict(fins=fins, dernier=dernier, valeur_dernier=obs[dernier], maj=rows[0].get("updated_at", "")[:10],
                releve=dict(periode=rder, valeur=robs[rder], lu_le=rel["lu_le"], image_sha256=rel["image_sha256"]))


# ------------------------------------------------------------------ A3 : vieillissement ou position présente
JEUX = ("base", "productivite", "risque", "base_precedente")


def s2():
    import openpyxl
    wb = openpyxl.load_workbook(piece("dsm"), read_only=True, data_only=True)
    out = {}
    for g in wb.sheetnames:
        lab = {}
        for r in wb[g].iter_rows(min_row=180, max_row=200, values_only=True):
            txt = [v for v in r if isinstance(v, str)]
            num = [v for v in r if isinstance(v, (int, float))]
            if len(num) >= 4 and txt and txt[-1].strip() not in lab:
                lab[txt[-1].strip()] = num[:4]
        try:
            out[g] = {k: dict(zip(JEUX, lab[lib])) for k, lib in (
                ("S2", "Overall value  (% of GDP)"), ("IBP", "Initial budgetary position"), ("CoA", "Ageing costs"),
                ("pensions", "Pensions"), ("sante", "Health care"), ("dependance", "Long-term care"), ("education", "Education"))}
        except KeyError as e:
            fail("DSM, feuille %s : libelle introuvable %s (la mise en page de la piece a change)" % (g, e))
    if set(out) != set(PAYS):
        fail("DSM : feuilles pays inattendues (%s)" % sorted(set(out) ^ set(PAYS)))
    x = out["FR"]
    for j in JEUX:
        if abs(x["S2"][j] - x["IBP"][j] - x["CoA"][j]) > 0.02 or \
                abs(x["CoA"][j] - x["pensions"][j] - x["sante"][j] - x["dependance"][j] - x["education"][j]) > 0.02:
            fail("DSM France, jeu %s : S2 != position initiale + vieillissement, ou vieillissement != somme des postes" % j)
    return out


def cor():
    import openpyxl
    wb = openpyxl.load_workbook(piece("cor"), read_only=True, data_only=True)
    lignes = {}
    for nom_f, lib in (("Dépenses en %", "Sc. Ref"), ("Solde dépenses ressources", "Ressources"), ("Solde dépenses ressources", "Solde")):
        rows = list(wb[nom_f].iter_rows(values_only=True))
        hdr = next((r for r in rows if 2025 in r and 2070 in r), None)
        ref = next((r for r in rows if r and any(isinstance(v, str) and v.strip() == lib for v in r)), None)
        if not hdr or not ref:
            fail("COR, feuille %s : ligne %s introuvable (la mise en page de la piece a change)" % (nom_f, lib))
        d = {hdr[i]: ref[i] for i in range(len(hdr)) if isinstance(hdr[i], int) and isinstance(ref[i], (int, float))}
        lignes[lib] = {a: v * (100 if abs(d[2025]) < 1 and lib != "Solde" else 1) for a, v in d.items()}
    # Les ratios du COR sont en fraction (0,1412) : ramenés en % ; le solde aussi, s'il est en fraction.
    if abs(lignes["Solde"][2025]) < 0.05:
        lignes["Solde"] = {a: v * 100 for a, v in lignes["Solde"].items()}
    dep, ress, solde = lignes["Sc. Ref"], lignes["Ressources"], lignes["Solde"]
    if not 10 < dep[2025] < 20 or not 10 < ress[2025] < 20:
        fail("COR : ordre de grandeur inattendu (depenses %.2f, ressources %.2f)" % (dep[2025], ress[2025]))
    a1 = max(a for a in dep if a in ress and a in solde)
    if abs(ress[a1] - dep[a1] - solde[a1]) > 0.02:
        fail("COR : ressources - depenses != solde en %d" % a1)
    return dict(a0=2025, a1=a1, depenses0=dep[2025], depenses1=dep[a1], ressources0=ress[2025], ressources1=ress[a1],
                solde0=solde[2025], solde1=solde[a1])


# ------------------------------------------------------------------ calcul
def calcul():
    R, ecartes, calculables = emplois()
    if "FR" not in R or any(e["pays"] == "FR" for e in ecartes):
        fail("France : annee ecartee par le temoin ou par l'identite (%s)" % [e for e in ecartes if e["pays"] == "FR"])
    FR = R["FR"]
    fin = max(FR)
    a0 = fin - 29
    if not all(a in FR for a in range(a0, fin + 1)):
        fail("France : moins de trente annees (%d-%d)" % (min(FR), fin))
    if not all(FR[a]["d92_publie"] for a in range(a0, fin + 1)):
        fail("France : aides a l'investissement versees (D92PAY) absentes certaines annees")
    total = cumul(FR, a0, fin)
    dec = [cumul(FR, a0 + 10 * k, a0 + 10 * k + 9) for k in range(3)]
    annees = [dict(annee=a, **{k: FR[a][k] for k in ("besoin", "desepargne", "investissement_net", "actifs", "transferts", "aides_investissement")})
              for a in range(a0, fin + 1)]
    # Contre-population : même fenêtre de vingt-cinq ans pour tous les pays, complète
    c0 = fin - 24
    cp = []
    for p in sorted(PAYS):
        s = cumul(R.get(p, {}), c0, fin)
        if s:
            cp.append(dict(pays=p, nom=PAYS[p][0], **s))
    pat = patrimoine(fin)
    det, det_pays, det_controle = detention()
    S2 = s2()
    C = cor()
    cons = dict(annees_pays_calculables=calculables, retenues=sum(len(v) for v in R.values()), ecartees=len(ecartes), detail_ecartees=ecartes)
    return fin, total, dec, annees, cp, pat, det, det_pays, det_controle, S2, C, cons, etat_negociable()


# ------------------------------------------------------------------ affichage et gardes
def affichage(fin, total, dec, annees, cp, pat, det, det_pays, S2, C, cons, etat):
    A = {"fin": str(fin), "a0": str(total["debut"]), "tolerance": fr(TOL, 2),
         "dsm_lib": SOURCES["dsm"]["lib"], "cor_lib": SOURCES["cor"]["lib"],
         "proj_an": max(SOURCES[k]["publie"] for k in ("dsm", "cor"))[:4]}   # année de publication des projections
    t = total
    A.update(b=fr(t["besoin"]), k=fr(t["actifs"]), e=fr(t["desepargne"]), t=fr(t["transferts"]), d92=fr(t["aides_investissement"]),
             part_k=fr(t["part_actifs"], 0), part_e=fr(t["part_desepargne"], 0), part_t=fr(t["part_transferts"], 0),
             part_k_eur=fr(t["part_actifs_euros"], 0), part_n=fr(t["part_investissement_net"], 0),
             part_max=fr(100 * (t["actifs"] + t["aides_investissement"]) / t["besoin"], 0))
    for k, d in enumerate(dec, 1):
        p = "d%d_" % k
        A[p + "lib"] = "%d-%d" % (d["debut"], d["fin"])
        A[p + "b"] = fr(d["besoin"]); A[p + "k"] = fr(d["actifs"]); A[p + "e"] = fr(d["desepargne"]); A[p + "t"] = fr(d["transferts"])
        A[p + "part"] = fr(d["part_actifs"], 0); A[p + "k_moy"] = fr(d["actifs"] / d["annees"])
    pos = [r["annee"] for r in annees if r["desepargne"] < 0]
    A["ep_pos_n"] = lettres(len(pos)); A["ep_pos_lib"] = enumere([str(a) for a in pos]) if pos else ""
    # patrimoine
    p0, p1 = pat[0], pat[-1]
    A.update(s0=str(p0["annee"]), s1=str(p1["annee"]), pn0=fr(p0["patrimoine_net"]), pn1=fr(p1["patrimoine_net"]),
             pn_var=fr(abs(p1["patrimoine_net"] - p0["patrimoine_net"])),
             prod_var=signe(p1["actifs_produits"] - p0["actifs_produits"]), terr_var=signe(p1["terrains"] - p0["terrains"]),
             bf_var_abs=fr(abs(p1["valeur_financiere_nette"] - p0["valeur_financiere_nette"])),
             pn_hors_terr=fr(abs((p1["patrimoine_net"] - p1["terrains"]) - (p0["patrimoine_net"] - p0["terrains"]))))
    # contre-population
    A["cp_a0"] = str(cp[0]["debut"]); A["cp_n"] = str(len(cp))
    frc = next(x for x in cp if x["pays"] == "FR")
    # Arbitrage PRO-20261003-195656 : le ratio n'a de sens que si le besoin cumulé est substantiel.
    groupe = [x for x in cp if x["besoin"] >= SEUIL_BESOIN]
    sup = [x for x in groupe if x["part_actifs"] >= 50]
    inf = [x for x in groupe if x["part_actifs"] < frc["part_actifs"]]
    exc = [x for x in cp if x["besoin"] < SEUIL_BESOIN]
    A["cp_fr_part"] = fr(frc["part_actifs"], 0)
    A["cp_sup_n"] = lettres(len(sup)); A["cp_sup_pays"] = enumere([PAYS[x["pays"]][1] for x in sorted(sup, key=lambda x: -x["part_actifs"])])
    A["cp_inf_n"] = lettres(len(inf)); A["cp_inf_pays"] = enumere([PAYS[x["pays"]][1] for x in sorted(inf, key=lambda x: -x["part_actifs"])])
    A["cp_exc_pays"] = enumere([PAYS[x["pays"]][1] for x in exc]) if exc else ""
    A["cp_seuil"] = fr(SEUIL_BESOIN, 0); A["cp_groupe_n"] = str(len(groupe))
    A["cp_exc_pays_maj"] = maj(A["cp_exc_pays"])
    # détention
    d0, d1 = det[0], det[-1]
    nr_max = max(det, key=lambda x: x["part_non_residents"])
    bc_max = max(det, key=lambda x: x["part_banque_centrale"])
    maj1 = next(x["annee"] for x in det if x["part_non_residents"] > 50)
    apres = [x for x in det if x["annee"] >= maj1]
    A.update(h0=str(d0["annee"]), h_fin=str(d1["annee"]), nr0=fr(d0["part_non_residents"]), nr_fin=fr(d1["part_non_residents"]),
             res_fin=fr(100 - d1["part_non_residents"]),
             nr_max=fr(nr_max["part_non_residents"]), nr_max_annee=str(nr_max["annee"]), nr_maj_premiere=str(maj1),
             nr_maj_n=str(sum(1 for x in apres if x["part_non_residents"] > 50)), nr_maj_tot=str(len(apres)),
             bc0=fr(d0["part_banque_centrale"]), bc_max=fr(bc_max["part_banque_centrale"]), bc_max_annee=str(bc_max["annee"]),
             bc_fin=fr(d1["part_banque_centrale"]), bc_var=fr(bc_max["part_banque_centrale"] - d1["part_banque_centrale"]),
             nr_var_bc=fr(d1["part_non_residents"] - bc_max["part_non_residents"]), nr_bcmax=fr(bc_max["part_non_residents"]),
             dette_h_fin=fr(d1["dette"]))
    # La part « nationale » tenue par la banque centrale : première année au-dessus du dixième, autres résidents avant/après
    bc10 = [x for x in det if x["part_banque_centrale"] > 10]
    avant = max((x for x in det if x["annee"] < bc_max["annee"] and x["part_banque_centrale"] < 3), key=lambda x: x["annee"])
    A.update(bc10_premiere=str(bc10[0]["annee"]), an_avant=str(avant["annee"]), ar_avant=fr(avant["part_autres_residents"]),
             ar_fin=fr(d1["part_autres_residents"]))
    # Témoin de périmètre État (Banque de France) : mêmes dates de fin d'année que la série BCE
    ef = {x["annee"]: x["part"] for x in etat["fins"]}
    emax = max(etat["fins"], key=lambda x: x["part"])
    emin_apres = min((x for x in etat["fins"] if x["annee"] > emax["annee"]), key=lambda x: x["part"])
    A.update(etat_a0=str(etat["fins"][0]["annee"]), etat_0=fr(etat["fins"][0]["part"]), etat_fin=fr(ef[d1["annee"]]),
             etat_max=fr(emax["part"]), etat_max_annee=str(emax["annee"]), etat_min=fr(emin_apres["part"]),
             etat_min_annee=str(emin_apres["annee"]), etat_maj=etat["maj"][8:10].lstrip("0") + " " + MOIS[int(etat["maj"][5:7]) - 1] + " " + etat["maj"][:4],
             etat_lib=SOURCES["det"]["lib"])
    rp = etat["releve"]["periode"]
    A.update(etat_der=fr(etat["releve"]["valeur"]), etat_der_trim=TRIM[int(rp[-1]) - 1] + " " + rp[:4],
             etat_der_lu=etat["releve"]["lu_le"][8:10].lstrip("0") + " " + MOIS[int(etat["releve"]["lu_le"][5:7]) - 1] + " " + etat["releve"]["lu_le"][:4])
    for p, x in det_pays.items():
        A["h_" + p.lower()] = fr(x["part_non_residents"], 0)
    # S2
    x = S2["FR"]
    A.update(s2=fr(x["S2"]["base"]), ibp=fr(x["IBP"]["base"]), coa=fr(x["CoA"]["base"]), pen=fr(x["pensions"]["base"]),
             hc_ltc=signe(x["sante"]["base"] + x["dependance"]["base"]), edu=fr(x["education"]["base"]),
             ibp_prod=fr(x["IBP"]["productivite"]), coa_prod=fr(x["CoA"]["productivite"]),
             ibp_risque=fr(x["IBP"]["risque"]), coa_risque=fr(x["CoA"]["risque"]),
             ibp_prec=fr(x["IBP"]["base_precedente"]), coa_prec=fr(x["CoA"]["base_precedente"]))
    A["ibp_pdf"] = fr(x["S2"]["base"] - x["CoA"]["base"])   # convention du tableau 3.2 du rapport : S2 - vieillissement
    cor_var = C["depenses1"] - C["depenses0"]
    A.update(cor_a0=str(C["a0"]), cor_a1=str(C["a1"]), cor_dep0=fr(C["depenses0"]), cor_dep1=fr(C["depenses1"]), cor_var=signe(cor_var),
             cor_res0=fr(C["ressources0"]), cor_res1=fr(C["ressources1"]), cor_solde1=fr(C["solde1"]),
             coa_cor=fr(x["CoA"]["base"] - x["pensions"]["base"] + cor_var),
             coa_cor_risque=fr(x["CoA"]["risque"] - x["pensions"]["risque"] + cor_var))
    vieux = sorted(g for g, y in S2.items() if y["CoA"]["base"] > y["IBP"]["base"])
    A["pays_coa_n"] = lettres(len(vieux)) if len(vieux) < len(LETTRES) else str(len(vieux)); A["pays_n"] = str(len(S2))
    # contrôles et conservation
    A["cons_calculables"] = str(cons["annees_pays_calculables"]); A["cons_ecartees"] = str(cons["ecartees"])
    return A, dict(sup=sup, inf=inf, exc=exc, frc=frc, vieux=vieux, cor_var=cor_var, nr_max=nr_max, bc_max=bc_max, maj1=maj1,
                   etat=etat, emax=emax, emin_apres=emin_apres)


def gardes(fin, total, dec, annees, cp, pat, det, det_pays, S2, C, aux):
    d1, d2, d3 = dec
    p0, p1 = pat[0], pat[-1]
    x = S2["FR"]
    dl = det[-1]
    cor_var = aux["cor_var"]
    G = [
        # --- A1 : à quoi ont correspondu les déficits
        ("chapo : « seulement » — moins d'un quart du besoin de financement en acquisitions nettes d'actifs", total["part_actifs"] < 25),
        ("verdict du test conservé : investissement net seul sous 25 % du besoin", total["part_investissement_net"] < 25),
        ("la mesure en euros donne le même ordre (à 3 points près)", abs(total["part_actifs_euros"] - total["part_actifs"]) < 3),
        ("« près des deux tiers » en dépenses courantes non couvertes (60 à 70 %)", 60 <= total["part_desepargne"] < 70),
        ("la désépargne est le premier emploi du besoin de financement", total["desepargne"] > max(total["actifs"], total["transferts"])),
        ("« la part investie a baissé de décennie en décennie »", d1["part_actifs"] > d2["part_actifs"] > d3["part_actifs"]),
        ("dernière décennie : « que » — moins d'un demi-point de PIB par an d'acquisitions nettes d'actifs", d3["actifs"] / d3["annees"] < 0.5),
        ("recettes courantes supérieures aux dépenses courantes au plus trois années sur trente", sum(1 for r in annees if r["desepargne"] < 0) <= 3),
        ("« aucune année l'investissement n'a égalé le besoin de financement »", all(r["actifs"] < r["besoin"] for r in annees)),
        ("en comptant toutes les aides à l'investissement versées : « toujours moins de la moitié »",
         (total["actifs"] + total["aides_investissement"]) / total["besoin"] < 0.5),
        # --- témoin 2 : patrimoine
        ("patrimoine net en baisse (concorde avec la faible part investie)", p1["patrimoine_net"] < p0["patrimoine_net"]),
        ("actifs produits : « à peine bougé » (moins de 5 points)", abs(p1["actifs_produits"] - p0["actifs_produits"]) < 5),
        ("valeur financière nette en recul", p1["valeur_financiere_nette"] < p0["valeur_financiere_nette"]),
        ("terrains en hausse : « seule » la hausse de leur valeur a limité la baisse",
         p1["terrains"] > p0["terrains"] and p1["actifs_produits"] - p0["actifs_produits"] < p1["terrains"] - p0["terrains"]),
        ("B2 : la baisse du patrimoine net ne dépend pas de l'année de départ (toute année des seize premières)",
         all(p1["patrimoine_net"] < x["patrimoine_net"] for x in pat[:16])),
        ("sans les terrains, la baisse aurait été plus forte", (p1["patrimoine_net"] - p1["terrains"]) - (p0["patrimoine_net"] - p0["terrains"]) < p1["patrimoine_net"] - p0["patrimoine_net"]),
        ("patrimoine : la série couvre au moins vingt-cinq ans", p1["annee"] - p0["annee"] >= 25),
        # --- contre-population
        ("« la France n'est pas un cas extrême » : au moins trois pays plus bas qu'elle", len(aux["inf"]) >= 3),
        ("au moins trois pays au-dessus de la moitié", len(aux["sup"]) >= 3),
        ("« dont l'Allemagne et l'Italie » sont plus bas que la France", {"DE", "IT"} <= {y["pays"] for y in aux["inf"]}),
        ("contre-population : au moins vingt pays de l'Union comparés sur la même fenêtre", len(cp) >= 20),
        # --- A2 : détention
        ("« un peu plus de la moitié » détenue par des non-résidents la dernière année (50 à 60 %)", 50 < dl["part_non_residents"] < 60),
        ("la part non résidente a monté depuis la première année d'au moins 10 points", dl["part_non_residents"] - det[0]["part_non_residents"] >= 10),
        ("la part non résidente est majoritaire la plupart des années depuis qu'elle a dépassé la moitié",
         sum(1 for y in det if y["annee"] >= aux["maj1"] and y["part_non_residents"] > 50) * 2 > sum(1 for y in det if y["annee"] >= aux["maj1"])),
        ("Banque de France : « détenteur majeur » — plus de 15 % de la dette à son maximum", aux["bc_max"]["part_banque_centrale"] > 15),
        ("Banque de France : moins de 3 % de la dette la première année", det[0]["part_banque_centrale"] < 3),
        ("Banque de France : « ses avoirs refluent » depuis le maximum", dl["part_banque_centrale"] < aux["bc_max"]["part_banque_centrale"] - 2),
        ("« la part des non-résidents est remontée » depuis le maximum de la Banque de France",
         dl["part_non_residents"] > aux["bc_max"]["part_non_residents"] + 2),
        ("la hausse de la Banque de France commence avec les achats de titres publics (2015-2016) : moins de 3 % en 2014, plus de 5 % en 2015",
         next(y for y in det if y["annee"] == 2014)["part_banque_centrale"] < 3 and next(y for y in det if y["annee"] == 2015)["part_banque_centrale"] > 5),
        ("Italie et Suède : prémisse « mieux vérifiée » (au moins 10 points de moins que la France)",
         all(det_pays[p]["part_non_residents"] < dl["part_non_residents"] - 10 for p in ("IT", "SE"))),
        ("Autriche et Belgique : « moins » vérifiée (plus que la France)", all(det_pays[p]["part_non_residents"] > dl["part_non_residents"] for p in ("AT", "BE"))),
        ("contre-population de détention : même dernière année que la France", all(det_pays[p]["annee"] == dl["annee"] for p in ("IT", "SE", "AT", "BE"))),
        # --- témoin de périmètre État (Banque de France, Webstat) : il doit dire la même chose que la série BCE
        ("État : la série Banque de France couvre la dernière année de la série BCE", dl["annee"] in {x["annee"] for x in aux["etat"]["fins"]}),
        ("État : « majorité non résidente aujourd'hui » (plus de 50 % la dernière année)",
         next(x["part"] for x in aux["etat"]["fins"] if x["annee"] == dl["annee"]) > 50),
        ("État : la part a monté depuis la première fin d'année publiée", aux["etat"]["fins"][-1]["part"] > aux["etat"]["fins"][0]["part"] + 10),
        ("État : « creux au moment des achats de la banque centrale » (à un an près du maximum de la Banque de France)",
         abs(aux["emin_apres"]["annee"] - aux["bc_max"]["annee"]) <= 1),
        ("État : « remonte depuis » (au moins 3 points au-dessus du creux)", aux["etat"]["fins"][-1]["part"] > aux["emin_apres"]["part"] + 3),
        ("État : la dernière observation (relevé AFT) prolonge la remontée", aux["etat"]["releve"]["valeur"] >= aux["etat"]["fins"][-1]["part"]),
        ("les deux séries vont dans le même sens depuis le creux de l'État",
         dl["part_non_residents"] > next(y for y in det if y["annee"] == aux["emin_apres"]["annee"])["part_non_residents"]),
        ("« depuis » la première année au-dessus du dixième, la Banque de France y reste chaque année",
         all(y["part_banque_centrale"] > 10 for y in det if y["annee"] >= next(z["annee"] for z in det if z["part_banque_centrale"] > 10))),
        ("« n'a tenu que par elle » : les autres résidents perdent au moins 8 points de part depuis la veille des achats",
         next(y for y in det if y["annee"] == max(z["annee"] for z in det if z["annee"] < aux["bc_max"]["annee"] and z["part_banque_centrale"] < 3))["part_autres_residents"]
         - dl["part_autres_residents"] >= 8),
        ("la part résidente totale ne baisse pas plus que la part des autres résidents (la banque centrale compense)",
         dl["part_banque_centrale"] > det[0]["part_banque_centrale"] + 8),
        # --- A3 : vieillissement
        ("« d'abord » / « bien plus » : position présente supérieure au double du vieillissement (scénario de base)", x["IBP"]["base"] > 2 * x["CoA"]["base"]),
        ("la position présente reste le premier terme dans les deux scénarios de risque et dans l'édition précédente",
         all(x["IBP"][j] > x["CoA"][j] for j in JEUX)),
        ("composante pensions négative (« dépense de pensions en baisse »)", x["pensions"]["base"] < 0),
        ("santé et dépendance poussent ensemble à la hausse", x["sante"]["base"] > 0 and x["dependance"]["base"] > 0),
        ("l'indicateur sait montrer l'inverse : au moins trois pays où le vieillissement l'emporte", len(aux["vieux"]) >= 3),
        ("« dont la Belgique, l'Espagne et le Luxembourg »", {"BE", "ES", "LU"} <= set(aux["vieux"])),
        ("COR : dépense de retraite en hausse en fin de projection", cor_var > 0),
        ("avec la trajectoire du COR, la position présente reste supérieure (scénario de base)",
         x["IBP"]["base"] > x["CoA"]["base"] - x["pensions"]["base"] + cor_var),
        ("« l'ordre ne s'inverse qu'en cumulant » : il s'inverse bien dans le scénario de risque avec le COR",
         x["IBP"]["risque"] <= x["CoA"]["risque"] - x["pensions"]["risque"] + cor_var),
        ("COR : le solde de fin de projection est un déficit", C["solde1"] < 0),
        ("méthode : le tableau 3.2 du rapport imprime une position initiale différente de la composante (sinon la phrase « au lieu de » tombe)",
         fr(x["S2"]["base"] - x["CoA"]["base"]) != fr(x["IBP"]["base"])),
        ("COR : baisse des ressources « autant » que hausse des dépenses (rapport 0,75 à 1,33)",
         0.75 < (C["ressources0"] - C["ressources1"]) / cor_var < 1.33),
        # Paragraphe « Deux projections, deux jeux d'hypothèses » (remarque du secrétariat du COR, 06/10/2026) : il décrit
        # les hypothèses de ces deux éditions (Insee nouvelle, Agirc-Arrco 2038 ; rapport de 2024 sur le vieillissement).
        ("hypothèses du COR et de la Commission décrites pour ces éditions : une autre édition impose de relire le paragraphe",
         SOURCES["cor"]["lib"] == "rapport annuel de juin 2026" and SOURCES["dsm"]["lib"] == "Debt Sustainability Monitor 2025"),
    ]
    if "--mutation-garde" in sys.argv:   # témoin positif : part investie de la première décennie mise sous la dernière
        G[5] = (G[5][0], d3["part_actifs"] - 1 > d2["part_actifs"] > d3["part_actifs"])
    faux = [n for n, ok in G if not ok]
    if faux:
        fail("la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    return len(G)


# ------------------------------------------------------------------ figures
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
    for k, (t, c) in enumerate([(source, INK2), (note, INK2), (LICENCE, MUTED)]):
        out.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, c, esc(t)))
    return out


def legende(e, items, y=36, x=0):
    for col, lib in items:
        e.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/>' % (x, y, col))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (x + 14, y + 9, INK2, esc(lib)))
        x += 14 + 6.0 * len(lib) + 18


def fig_actifs(total, dec, A):
    """Signature : 100 % du besoin de financement de chaque période, partagé entre ses trois emplois."""
    H, X0, X1 = 300, 132, W - 64
    titre = "France : à quoi ont correspondu les déficits publics"
    rang = [(A["d%d_lib" % k], d) for k, d in enumerate(dec, 1)] + [("%s-%s" % (A["a0"], A["fin"]), total)]
    desc = ("Pour chaque période, le besoin de financement des administrations publiques, ramené à 100, partagé entre trois emplois : "
            "acquisitions nettes d'actifs (investissement moins usure du capital, terrains, stocks), transferts en capital nets vers "
            "d'autres secteurs, dépenses courantes non couvertes par les recettes courantes. "
            + " ".join("%s : %s points de PIB de besoin de financement, dont %s %% en actifs, %s %% en transferts, %s %% en dépenses courantes."
                       % (lib, fr(d["besoin"]), fr(d["part_actifs"], 0), fr(d["part_transferts"], 0), fr(d["part_desepargne"], 0)) for lib, d in rang))
    e = entete(H, "ga", titre, desc)
    legende(e, [(BLEU, "actifs (investissement net, terrains)"), (GRIS_CLAIR, "transferts en capital"), (ORANGE, "dépenses courantes non couvertes")])
    e.append('<text x="%d" y="72" font-size="10" fill="%s" text-anchor="end">besoin de financement,</text>' % (W, MUTED))
    e.append('<text x="%d" y="84" font-size="10" fill="%s" text-anchor="end">points de PIB</text>' % (W, MUTED))
    top, hb, pas = 96, 34, 50
    for k, (lib, d) in enumerate(rang):
        y = top + pas * k + (14 if k == 3 else 0)
        if k == 3:
            e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y - 12, W, y - 12, GRID))
        e.append('<text x="0" y="%.1f" font-size="12" font-weight="600" fill="%s">%s</text>' % (y + hb / 2 + 4, INK, esc(lib)))
        x = X0
        for cle, col, txt in (("part_actifs", BLEU, "#ffffff"), ("part_transferts", GRIS_CLAIR, INK), ("part_desepargne", ORANGE, "#ffffff")):
            w = (X1 - X0) * max(d[cle], 0) / 100
            e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s"/>' % (x, y, max(w, 0.6), hb, col))
            if w >= 30:
                e.append('<text x="%.1f" y="%.1f" font-size="11" font-weight="600" fill="%s" text-anchor="middle">%s %%</text>'
                         % (x + w / 2, y + hb / 2 + 4, txt, fr(d[cle], 0)))
            x += w
        e.append('<text x="%d" y="%.1f" font-size="11" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (W, y + hb / 2 + 4, INK2, fr(d["besoin"])))
    e += cartouche(H + 4, "Eurostat gov_10a_main (B9, B8N, P51G, P51C, NP, P52_P53, D9), gov_10dd_edpt1 (PIB), administrations publiques, France, %s-%s"
                   % (A["a0"], A["fin"]),
                   "Identité comptable : elle dit à quoi les déficits ont correspondu, non ce qu'ils ont produit ; l'éducation n'y est pas un actif.")
    e.append("</svg>")
    return "\n".join(e)


def fig_detention(det, A):
    H, X0, X1, TOP, BAS = 300, 40, W - 128, 60, 276
    titre = "Qui détient la dette publique française"
    desc = ("Parts de la dette des administrations publiques détenues par les non-résidents, par la Banque de France et par les autres "
            "résidents, de %s à %s. Non-résidents : %s %% en %s, %s %% au plus haut en %s, %s %% en %s. Banque de France : %s %% en %s, "
            "%s %% en %s, %s %% en %s." % (A["h0"], A["h_fin"], A["nr0"], A["h0"], A["nr_max"], A["nr_max_annee"], A["nr_fin"], A["h_fin"],
                                         A["bc0"], A["h0"], A["bc_max"], A["bc_max_annee"], A["bc_fin"], A["h_fin"]))
    e = entete(H, "gd", titre, desc)
    n = len(det)
    X = lambda k: X0 + (X1 - X0) * k / (n - 1)
    Y = lambda v: BAS - (BAS - TOP) * v / 100
    bandes = (("part_banque_centrale", BLEU), ("part_autres_residents", GRIS_CLAIR), ("part_non_residents", ORANGE))
    bas_cumul = [0.0] * n
    milieux = {}
    for cle, col in bandes:
        haut = [bas_cumul[k] + det[k][cle] for k in range(n)]
        pts = ["%.1f,%.1f" % (X(k), Y(haut[k])) for k in range(n)] + ["%.1f,%.1f" % (X(k), Y(bas_cumul[k])) for k in reversed(range(n))]
        e.append('<polygon points="%s" fill="%s"/>' % (" ".join(pts), col))
        milieux[cle] = (bas_cumul[-1] + haut[-1]) / 2
        bas_cumul = haut
    for g in range(0, 101, 25):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6" stroke-opacity="0.8"/>' % (X0, Y(g), X1, Y(g), "#ffffff"))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d %%</text>' % (X0 - 6, Y(g) + 3, MUTED, g))
    e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>' % (X0, Y(50), X1, Y(50), INK))
    for k, r in enumerate(det):
        if r["annee"] % 5 == 0 or k == n - 1:
            e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(k), BAS + 14, INK2, r["annee"]))
    last = det[-1]
    for cle, lib in (("part_non_residents", "non-résidents"), ("part_autres_residents", "autres résidents"), ("part_banque_centrale", "Banque de France")):
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s">%s</text>' % (X1 + 8, Y(milieux[cle]) - 2, INK2, esc(lib)))
        e.append('<text x="%d" y="%.1f" font-size="11" font-weight="600" fill="%s">%s %%</text>' % (X1 + 8, Y(milieux[cle]) + 11, INK, fr(last[cle], 0)))
    e.append('<text x="%d" y="%.1f" font-size="10" fill="%s">moitié de la dette</text>' % (X0 + 4, Y(50) - 4, INK))
    e += cartouche(H + 4, "BCE, statistiques de finances publiques (GFS) : dette de Maastricht des administrations publiques par secteur détenteur, France, %s-%s"
                   % (A["h0"], A["h_fin"]),
                   "Résidence du détenteur enregistré (fonds, dépositaire), non de l'épargnant final ; valeur nominale. Banque de France : titres comptés comme résidents.")
    e.append("</svg>")
    return "\n".join(e)


def fig_vieillissement(S2fr, C, A):
    H, X0, X1 = 270, 210, W - 40
    titre = "France : d'où vient l'effort qui stabiliserait la dette (indicateur S2)"
    groupes = [("Scénario de base", S2fr["IBP"]["base"], S2fr["CoA"]["base"]),
               ("Productivité plus faible", S2fr["IBP"]["productivite"], S2fr["CoA"]["productivite"]),
               ("Risque santé et dépendance", S2fr["IBP"]["risque"], S2fr["CoA"]["risque"]),
               ("Édition précédente (%d)" % (int(A["dsm_lib"][-4:]) - 1), S2fr["IBP"]["base_precedente"], S2fr["CoA"]["base_precedente"])]
    desc = ("Ajustement permanent du solde primaire structurel qui stabiliserait la dette, en points de PIB, partagé entre la position "
            "budgétaire présente et le coût du vieillissement, selon la Commission européenne (%s), dans trois scénarios et dans "
            "l'édition précédente. " % A["dsm_lib"]
            + " ".join("%s : position présente %s, vieillissement %s." % (g, fr(a), fr(b)) for g, a, b in groupes))
    e = entete(H, "gv", titre, desc)
    legende(e, [(ORANGE, "position budgétaire présente"), (GRIS, "coût du vieillissement")])
    vmax = (int(max(max(a, b) for _, a, b in groupes)) + 1)
    Xv = lambda v: X0 + (X1 - X0) * v / vmax
    top, pas, hb = 64, 44, 15
    for g in range(0, vmax + 1):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"/>' % (Xv(g), top - 6, Xv(g), top + pas * len(groupes) - 8, GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (Xv(g), top + pas * len(groupes) + 6, MUTED, g))
    for k, (lib, a, b) in enumerate(groupes):
        y = top + pas * k
        e.append('<text x="0" y="%d" font-size="11.5" font-weight="600" fill="%s">%s</text>' % (y + hb + 2, INK, esc(lib)))
        for j, (v, col) in enumerate(((a, ORANGE), (b, GRIS))):
            yy = y + j * (hb + 2)
            x0_, x1_ = sorted((Xv(0), Xv(v)))
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0_, yy, max(x1_ - x0_, 0.6), hb, col))
            e.append('<text x="%.1f" y="%d" font-size="10" font-weight="600" fill="%s">%s</text>' % (max(x1_, Xv(0)) + 4, yy + 11, INK, fr(v)))
    e.append('<text x="%d" y="%d" font-size="10" fill="%s" text-anchor="end">points de PIB</text>' % (X1, top + pas * len(groupes) + 21, MUTED))
    e += cartouche(H + 4, "Commission européenne, %s, tableaux par pays : indicateur S2 et ses deux composantes, France" % A["dsm_lib"],
                   "Projections conditionnelles aux hypothèses de la Commission (Ageing Report 2024, réforme des retraites de 2023 appliquée).")
    e.append("</svg>")
    return "\n".join(e)


MONTRE = [("actifs", "Depuis trente ans, la part des déficits français qui a correspondu à un accroissement net des actifs publics "
                     "a baissé de décennie en décennie ; l'essentiel a couvert des dépenses courantes."),
          ("detention", "La part de la dette française détenue par des non-résidents dépasse la moitié la plupart des années depuis le "
                        "début des années 2000 ; les achats de la Banque de France l'ont fait reculer, son reflux la fait remonter."),
          ("vieillissement", "Selon l'indicateur de la Commission, l'effort qui stabiliserait la dette française tient à la position "
                             "budgétaire présente plus qu'au vieillissement, sauf à cumuler deux hypothèses défavorables.")]


def fiches(figs):
    out = []
    for ident, montre in MONTRE:
        f = "dette-generations-%s" % ident
        svg = figs[f + ".svg"]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        out.append(dict(id=ident, fichier=f, titre=titre, montre=montre, source=cart[0], precaution=cart[1]))
    return {"fr": out}


def csv_texte(total, dec, annees, cp, pat, det, det_pays, S2, C, etat):
    """Format long : les tableaux n'ont pas les mêmes colonnes."""
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "pays", "periode", "variable", "valeur", "unite"])
    cles = ("besoin", "actifs", "investissement_net", "transferts", "aides_investissement", "desepargne")
    for d in [total] + dec:
        for k in cles:
            w.writerow(["france_emplois_du_besoin_de_financement", "FR", "%d-%d" % (d["debut"], d["fin"]), k, "%.3f" % d[k], "points de PIB cumulés"])
    for r in annees:
        for k in cles:
            w.writerow(["france_annuel", "FR", r["annee"], k, "%.3f" % r[k], "% du PIB"])
    for d in cp:
        for k in ("besoin", "actifs", "transferts", "desepargne"):
            w.writerow(["ue_emplois_du_besoin_de_financement", d["pays"], "%d-%d" % (d["debut"], d["fin"]), k, "%.3f" % d[k], "points de PIB cumulés"])
    for r in pat:
        for k in ("actifs_produits", "actifs_non_produits", "terrains", "valeur_financiere_nette", "patrimoine_net"):
            w.writerow(["france_patrimoine_apu", "FR", r["annee"], k, "%.3f" % r[k], "% du PIB"])
    for r in det:
        for k in ("dette", "non_residents", "banque_centrale", "autres_residents"):
            w.writerow(["france_detention", "FR", r["annee"], k, "%.3f" % r[k], "% du PIB"])
    for x in etat["fins"]:
        w.writerow(["france_etat_negociable_non_residents", "FR", x["annee"], "part_non_residents_fin_annee", "%.1f" % x["part"], "% de la dette négociable de l'État"])
    for p, x in sorted(det_pays.items()):
        w.writerow(["ue_part_non_residents", p, x["annee"], "part_non_residents", "%.3f" % x["part_non_residents"], "% de la dette"])
    for g, x in sorted(S2.items()):
        for j in JEUX:
            for k in ("S2", "IBP", "CoA", "pensions", "sante", "dependance", "education"):
                w.writerow(["commission_s2", g, j, k, "%.3f" % x[k][j], "points de PIB"])
    for k in ("depenses0", "depenses1", "ressources0", "ressources1", "solde0", "solde1"):
        w.writerow(["cor_retraites", "FR", C["a0"] if k.endswith("0") else C["a1"], k[:-1], "%.3f" % C[k], "% du PIB"])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    fin, total, dec, annees, cp, pat, det, det_pays, det_controle, S2, C, cons, etat = calcul()
    A, aux = affichage(fin, total, dec, annees, cp, pat, det, det_pays, S2, C, cons, etat)
    n = gardes(fin, total, dec, annees, cp, pat, det, det_pays, S2, C, aux)
    log("France %s-%s : besoin %.1f pts = actifs %.1f (%.0f %%) + transferts %.1f + depenses courantes %.1f ; non-residents %.1f %% (%s) ; "
        "S2 %.2f = IBP %.2f + CoA %.2f ; %d annees-pays ecartees sur %d"
        % (A["a0"], A["fin"], total["besoin"], total["actifs"], total["part_actifs"], total["transferts"], total["desepargne"],
           det[-1]["part_non_residents"], A["h_fin"], S2["FR"]["S2"]["base"], S2["FR"]["IBP"]["base"], S2["FR"]["CoA"]["base"],
           cons["ecartees"], cons["annees_pays_calculables"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(A)))
        return 0
    figs = {"dette-generations-actifs.svg": fig_actifs(total, dec, A), "dette-generations-detention.svg": fig_detention(det, A),
            "dette-generations-vieillissement.svg": fig_vieillissement(S2["FR"], C, A)}
    tableau = [dict(pays=x["pays"], nom=x["nom"], besoin=fr(x["besoin"]), actifs=fr(x["actifs"]), transferts=fr(x["transferts"]),
                    desepargne=fr(x["desepargne"]), part=("au-delà du besoin" if x["part_actifs"] > 100 else fr(x["part_actifs"], 0) + "\u00a0%")
                    if x["besoin"] > 0 else "sans objet")
               for x in sorted(cp, key=lambda x: -(x["part_actifs"] if x["besoin"] > 0 else 1e9))]
    payload = {"meta": {"releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "perimetre": "administrations publiques (S.13), SEC 2010, monnaie nationale, PIB de la notification de déficit et de dette",
                        "identite": "-B9 = -B8N + (P51G - P51C + NP + P52_P53) + (D9PAY - D9REC)",
                        "pieces": {k: dict(v, sha256=hashlib.sha256((PIECES / v["fichier"]).read_bytes()).hexdigest()) for k, v in SOURCES.items()},
                        "definitions": {"besoin": "besoin de financement des administrations publiques (-B9), en % du PIB",
                                        "actifs": "acquisitions nettes d'actifs non financiers : investissement (P51G) moins consommation de capital fixe (P51C), plus terrains et autres actifs non produits (NP) et variation des stocks (P52_P53)",
                                        "investissement_net": "P51G - P51C seul (critère du test décisif)",
                                        "transferts": "transferts en capital versés moins reçus (D9PAY - D9REC) ; les recettes comprennent les impôts en capital (droits de succession)",
                                        "aides_investissement": "aides à l'investissement versées à d'autres secteurs (D92PAY), comprises dans les transferts versés",
                                        "desepargne": "épargne nette changée de signe (-B8N) : dépenses courantes, consommation de capital comprise, non couvertes par les recettes courantes",
                                        "temoin": "ratios comparés à ceux qu'Eurostat publie en %% du PIB ; tolérance %.2f point" % TOL,
                                        "detention": "BCE, GFS : dette de Maastricht par zone (W1 reste du monde, W2 résidents) et secteur détenteur (S121 banque centrale)",
                                        "S2": "ajustement permanent du solde primaire structurel en 2027 qui stabiliserait la dette à horizon infini ; IBP : position budgétaire initiale ; CoA : coût du vieillissement (Commission européenne)"}},
               "france": {"periodes": [total] + dec, "annees": annees, "patrimoine": pat, "detention": det},
               "ue": {"emplois": cp, "tableau": tableau, "part_non_residents": det_pays, "s2": S2},
               "cor": C, "etat_negociable": etat, "controles": {"detention_bce_eurostat_annees": det_controle}, "conservation": cons, "affichage": A}
    releve = payload["meta"]["releve_le"]
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev); p2.pop("releve_le", None); p2.pop("_licence", None); p2["meta"] = dict(p2["meta"], releve_le=None)
            n2 = json.loads(json.dumps(dict(payload, meta=dict(payload["meta"], releve_le=None)), ensure_ascii=False))
            if prev.get("releve_le") and json.dumps(p2, sort_keys=True, ensure_ascii=False) == json.dumps(n2, sort_keys=True, ensure_ascii=False) \
                    and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and all((OUT_IMG / f.replace(".svg", ".png")).exists() for f in figs) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(total, dec, annees, cp, pat, det, det_pays, S2, C, etat) \
                    and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches(figs):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Eurostat, BCE, Commission européenne, COR", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(total, dec, annees, cp, pat, det, det_pays, S2, C, etat), encoding="utf-8-sig", newline="\n")
    import cairosvg
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dette_generations.json, static/dette_generations.csv, data/figures_generations.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
