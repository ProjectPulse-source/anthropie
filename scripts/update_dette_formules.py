#!/usr/bin/env python3
"""update_dette_formules.py -- prolongement « Que valent les formules du débat sur la dette ? » (dossier dette).

Objet de la page : onze formules chiffrées prononcées le 8 septembre 2025 à l'Assemblée nationale (vote de confiance au
gouvernement Bayrou), confrontées aux séries officielles, chacune sur la question qu'elle pose, puis sur la question
voisine qui change le verdict. Recherche : dossier de l'auteur D:\\PRO\\06_PROMOTION\\PLAN_SUJETS_LIVRES_2026-11\\FORMULES_DETTE\\
(inventaire de 387 énoncés codés deux fois et arbitrés par un tiers ; fiches de test ; grille de tolérances ; trois
contre-expertises arbitrées, dont ENTRANTE_2026-11-02_Formules_dette_phaseB_arbitrage.md).

Entrées :
- jeux du site, relus et jamais recalculés à la source : data/dette_officielle.json (dette trimestrielle de Maastricht,
  intérêts et dépense d'enseignement des administrations publiques), data/dette_dynamique.json (dépenses, recettes, solde
  en points de PIB ; ratio de dette de la notification) ;
- extrait FIGÉ, contrôlé contre scripts/sources_dette_formules/SHA256SUMS : rendements à dix ans mensuels d'Eurostat
  (irt_lt_mcby_m, France, Grèce, Allemagne) ; capacité ou besoin de financement des administrations publiques depuis 1949
  (Insee, comptes nationaux base 2020) ; comptes de l'inventaire de la séance (inventaire_extrait.json) ; valeurs
  TRANSCRITES de documents publiés (documentaires.json : Cour des comptes, rapport des plafonds de juillet 2025, Sénat,
  Banque de France, Banque de Grèce), chacune avec sa page, son extrait et l'empreinte de la pièce archivée hors dépôt.

Règle : chaque qualificatif de la prose est une condition sur les nombres (fonction gardes) ; si une donnée la dément,
arrêt sans rien écrire. Mise à jour à la main : la page porte sur une séance close ; seules les révisions des jeux du
site peuvent changer un chiffre, et les gardes disent alors quelle phrase relire.

Usage : python scripts/update_dette_formules.py [--check] [--mutation=f1|f2|f3|f4|f5|f6|f8|f12|f13|f16|inv|hh]
Sorties : data/ et static/dette_formules.json, static/dette_formules.csv, data/figures_dette_formules.json,
          static/img/dette-formules-{grille,grece}{,-en}{,-m}.svg + .png
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure  # noqa: E402  -- pied commun, version téléphone, parité
import releve_jeu as rj  # noqa: E402  -- relevé daté par les seules données
import langue_generee as lg  # noqa: E402  -- signe, accord de « point » sur la valeur affichée

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_dette_formules"
OUT_DATA = ROOT / "data" / "dette_formules.json"
OUT_STATIC = ROOT / "static" / "dette_formules.json"
OUT_CSV = ROOT / "static" / "dette_formules.csv"
OUT_FIGURES = ROOT / "data" / "figures_dette_formules.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_DIR = ROOT / "content" / "formules-du-debat-sur-la-dette"
PAGE_URL = "stephane-lalut.com/formules-du-debat-sur-la-dette/"
PAGE_URL_EN = "stephane-lalut.com/en/public-debt-debate-claims/"
LICENCE = "CC BY 4.0 — calcul Stéphane Lalut ; sources Assemblée nationale, Insee, Eurostat, Cour des comptes, Gouvernement, Sénat, Banque de France, Banque de Grèce"

W = 720
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
FOND_NIVEAU = "#f3f1ee"
LICENCES = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Computed by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCES_M = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com", "en": "Computed by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
SUFFIXE = {"fr": "", "en": "-en"}
MOIS = {"fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
        "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]}



def per_trim(per: str, lang: str) -> str:
    """'2025-Q4' -> 'fin 2025' / 'at the end of 2025' ; autre trimestre -> 'au 2e trimestre 2026' / 'in Q2 2026'."""
    an, q = per.split("-Q")
    if q == "4":
        return ("fin " if lang == "fr" else "at the end of ") + an
    return ("au %se trimestre %s" % (q, an)) if lang == "fr" else ("in Q%s %s" % (q, an))

def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def nb(v: float, dec: int, lang: str) -> str:
    """Nombre à la précision affichée ; milliers séparés par une espace insécable (fr) ou une virgule (en)."""
    s = ("{:,.%df}" % dec).format(v)
    if lang == "fr":
        s = s.replace(",", "\u202f").replace(".", ",")
    return s


def esc(s: str) -> str:
    return html.escape(s, quote=False)


# ------------------------------------------------------------------ lecture
def lire():
    sums = {}
    for ligne in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if ligne.strip() and not ligne.startswith("#"):
            h, nom = ligne.split(None, 1)
            sums[nom.lstrip("*").strip()] = h
    for nom in ("eurostat_irt_lt_mcby_m.json", "insee_econ-fin-pub-deficit-secteur.xlsx", "insee_ip2054_donnees_2025-05-28.xlsx",
                "inventaire_extrait.json", "documentaires.json", "hors_hemicycle.json", "eurostat_gov_10a_main_TR_FR.json"):
        if nom not in sums:
            fail("empreinte absente de SHA256SUMS : " + nom)
        if hashlib.sha256((SRC / nom).read_bytes()).hexdigest() != sums[nom]:
            fail("empreinte differente pour " + nom + " : extrait modifie sans mise a jour de SHA256SUMS")
    off = json.loads((ROOT / "data" / "dette_officielle.json").read_text(encoding="utf-8"))
    dyn = json.loads((ROOT / "data" / "dette_dynamique.json").read_text(encoding="utf-8"))
    eu = json.loads((SRC / "eurostat_irt_lt_mcby_m.json").read_text(encoding="utf-8"))
    inv = json.loads((SRC / "inventaire_extrait.json").read_text(encoding="utf-8"))
    doc = json.loads((SRC / "documentaires.json").read_text(encoding="utf-8"))
    import openpyxl
    wb = openpyxl.load_workbook(SRC / "insee_econ-fin-pub-deficit-secteur.xlsx", data_only=True)
    solde = {}
    for feuille, cle in (("Figure 1", "mdeur"), ("Figure 2", "pct_pib")):
        rows = [[x for x in r if x is not None] for r in wb[feuille].iter_rows(values_only=True)]
        ans = next(r for r in rows if r and r[0] == "Administrations publiques")[1:]
        ens = next(r for r in rows if r and r[0] == "Ensemble")[1:]
        if len(ans) != len(ens):
            fail("Insee : annees et valeurs de longueurs differentes (%s)" % feuille)
        solde[cle] = {int(a): float(v) for a, v in zip(ans, ens)}
    # millésime de la séance : dépenses, recettes, solde en points de PIB publiés le 28 mai 2025 (Insee Première n° 2054, figure 2)
    wb = openpyxl.load_workbook(SRC / "insee_ip2054_donnees_2025-05-28.xlsx", data_only=True)
    rows = [r for r in wb["Figure 2"].iter_rows(values_only=True)]
    entete = next(i for i, r in enumerate(rows) if r[0] and str(r[0]).strip() == "Année")
    if [str(x) for x in rows[entete][1:4]] != ["Capacité (+) ou besoin (-) de financement des administrations publiques", "Dépenses publiques", "Recettes publiques"]:
        fail("Insee Première 2054 : colonnes de la figure 2 inattendues")
    dr25 = {int(r[0]): {"solde": float(r[1]), "depenses": float(r[2]), "recettes": float(r[3])} for r in rows[entete + 1:] if isinstance(r[0], int)}
    solde["dr25"] = dr25
    # même publication, figure 5 : dette de fin 2024 telle que publiée en mai 2025 (révisée depuis)
    rows5 = [[x for x in r if x is not None] for r in wb["Figure 5"].iter_rows(values_only=True)]
    if ["Administration publique", "Au 31 décembre 2023", "Au 31 décembre 2024"] not in rows5 or \
            ["Dette publique1 (brute)", "Dette publique nette2", "Dette publique1 (brute)", "Dette publique nette2"] not in rows5:
        fail("Insee Premiere 2054 : en-tetes de la figure 5 inattendus")
    ens5 = next(r for r in rows5 if r[0] == "Ensemble des administrations publiques")
    pct5 = next(r for r in rows5 if str(r[0]).strip() == "En % du PIB")
    solde["dette_fin2024_mai2025"] = {"mdeur": float(ens5[3]), "pct_pib": float(pct5[3])}
    ix = eu["dimension"]["time"]["category"]["index"]
    geo = eu["dimension"]["geo"]["category"]["index"]
    nt = len(ix)
    inv_t = {v: k for k, v in ix.items()}
    taux = {g: {inv_t[t]: eu["value"][str(gi * nt + t)] for t in range(nt) if str(gi * nt + t) in eu["value"]} for g, gi in geo.items()}
    # recettes en % du PIB, édition d'octobre 2026 d'Eurostat (le jeu dette_dynamique du site en est resté au printemps)
    tr = json.loads((SRC / "eurostat_gov_10a_main_TR_FR.json").read_text(encoding="utf-8"))
    ti = {v: k for k, v in tr["dimension"]["time"]["category"]["index"].items()}
    solde["rec_rev"] = {ti[int(k)]: float(v) for k, v in tr["value"].items()}
    solde["rec_rev_maj"] = tr["updated"][:10]
    hh = json.loads((SRC / "hors_hemicycle.json").read_text(encoding="utf-8"))
    gen = json.loads((ROOT / "data" / "dette_generations.json").read_text(encoding="utf-8"))
    return off, dyn, taux, solde, inv, doc, eu.get("updated", ""), hh, gen


# ------------------------------------------------------------------ calcul
def calcul(off, dyn, taux, solde, inv, doc):
    c = {}
    T = off["dette_trimestrielle"]["series"]
    Tm, Tp = T["mdeur"], T["pct_pib"]
    DR = dyn["depenses_recettes_pc_pib"]
    INT = off["interets_annuels"]["series"]["mdeur"]
    ED = off["depenses_fonction_annuelles"]["series"]["GF09"]["mdeur"]
    ratio = {dyn["depart"]["annee"]: dyn["depart"]["dette_pct_pib"], **{x["annee"]: x["dette_pct_pib"] for x in dyn["annees"]}}
    pib = {y: Tm["%d-Q4" % y] / ratio[y] * 100 for y in ratio if "%d-Q4" % y in Tm}
    c["millesime"] = {"dette_trimestrielle": off["dette_trimestrielle"]["derniere_periode"], "officielle": off["releve_le"], "dynamique": dyn["releve_le"]}

    # F1 : solde des administrations publiques depuis 1949 (Insee)
    sm, sp = solde["mdeur"], solde["pct_pib"]
    exc = [a for a in sorted(sm) if sm[a] > 0]
    c["F1"] = {"dernier_excedent": exc[-1], "excedent_mdeur": sm[exc[-1]], "excedent_pct": sp[exc[-1]],
               "derniere_annee": max(sm), "annees_deficit_depuis": max(sm) - exc[-1],
               "annees_excedent_depuis_1949": exc, "solde_mdeur": sm, "solde_pct": sp,
               "primaire_positif": [int(a) for a in sorted(DR) if DR[a]["solde"] + DR[a]["interets"] > 0]}

    # F2 : déficit et variation de la dette en euros, année par année
    f2 = []
    for y in range(1996, 2026):
        if y in pib and str(y) in DR and "%d-Q4" % (y - 1) in Tm:
            deficit = -DR[str(y)]["solde"] / 100 * pib[y]
            dd = Tm["%d-Q4" % y] - Tm["%d-Q4" % (y - 1)]
            f2.append({"annee": y, "deficit": round(deficit, 1), "var_dette": round(dd, 1), "ecart": round(dd - deficit, 1),
                       "ecart_pct": round((dd - deficit) / deficit * 100, 1)})
    c["F2"] = {"annees": f2, "n": len(f2), "somme_def": round(sum(x["deficit"] for x in f2), 1),
               "somme_var": round(sum(x["var_dette"] for x in f2), 1),
               "n_sup20": sum(abs(x["ecart_pct"]) > 20 for x in f2), "an0": f2[0]["annee"], "an1": f2[-1]["annee"]}

    # F16 : déficit de 3 % et dette
    d25 = ratio[2025]
    g25 = (pib[2025] / pib[2024] - 1) * 100
    stab = lambda d, g: d * g / (100 + g)
    d24 = ratio[2024]
    g24 = (pib[2024] / pib[2023] - 1) * 100
    c["F16"] = {"dette_pct": d25, "g25": g25, "stab_g25": stab(d25, g25), "stab_g25b": stab(d25, 2.5), "stab_g3": stab(d25, 3.0),
                "g_seuil": 300 / (d25 - 3), "euros_3pct": 0.03 * pib[2024],  # PIB de 2024, dernier connu le 08/09/2025 (C7, 06/11/2026)
                "dette_pct24": d24, "g24": g24, "g_seuil24": 300 / (d24 - 3), "stab_g24": stab(d24, g24)}

    # F8 : rendements à dix ans, mensuels (Eurostat) et au jour (Banque de France, Banque de Grèce)
    mois = sorted(set(taux["FR"]) & set(taux["EL"]) & set(taux["DE"]))
    ecart = {m: round(taux["FR"][m] - taux["EL"][m], 3) for m in mois}
    moy = lambda g, an: sum(taux[g][m] for m in mois if m.startswith(an)) / sum(m.startswith(an) for m in mois)
    jour = doc["taux_jour"]
    c["F8"] = {"mois": mois, "fr": {m: taux["FR"][m] for m in mois}, "el": {m: taux["EL"][m] for m in mois}, "de": {m: taux["DE"][m] for m in mois},
               "ecart": ecart, "m_aout": "2025-08", "m_sept": "2025-09",
               "fr_de_2025": moy("FR", "2025") - moy("DE", "2025"), "el_de_2025": moy("EL", "2025") - moy("DE", "2025"),
               "n_mois_2025": sum(m.startswith("2025") for m in mois),
               "bog": jour["banque_de_grece"]["dix_ans_pct"], "tec10": jour["banque_de_france"]["tec10_pct"],
               "hdat": jour["hdat"]["dix_ans_pct"],
               "dernier": mois[-1],
               "premier_dessus": next(m for m in mois if ecart[m] > 0),
               "dessous_2026": [m for m in mois if m >= "2026-01" and ecart[m] < 0]}

    # F6 : fenêtres, points de PIB
    fen = lambda a, b: {k: round(DR[str(b)][k] - DR[str(a)][k], 1) for k in ("depenses", "depenses_hors_interets", "recettes", "solde")}
    c["F6"] = {"%d-%d" % (a, b): fen(a, b) for a in (2017, 2019) for b in (2024, 2025)}
    D25 = solde["dr25"]
    fen25 = lambda a, b: {k: round(D25[b][k] - D25[a][k], 1) for k in ("depenses", "recettes", "solde")}
    c["F6d"] = {"2017-2024": fen25(2017, 2024), "2019-2024": fen25(2019, 2024)}

    # F12 et F13 : hausse de l'encours (dernier trimestre publié le 8/09/2025 : T1 2025)
    q = lambda k: Tm[k]
    c["F12"] = {"t2_2017": q("2017-Q2"), "t4_2016": q("2016-Q4"), "t1_2025": q("2025-Q1"), "t2_2025": q("2025-Q2"), "t2_2012": q("2012-Q2"),
                "h_election": q("2025-Q1") - q("2017-Q2"), "h_janvier": q("2025-Q1") - q("2016-Q4"), "h_t2": q("2025-Q2") - q("2017-Q2"),
                "h_hollande": q("2017-Q2") - q("2012-Q2"),
                "pts_macron_an": (Tp["2025-Q1"] - Tp["2017-Q2"]) / 7.75, "pts_hollande_an": (Tp["2017-Q2"] - Tp["2012-Q2"]) / 5,
                "eur_macron_an": (q("2025-Q1") - q("2017-Q2")) / 7.75, "eur_hollande_an": (q("2017-Q2") - q("2012-Q2")) / 5}

    mil = doc["millesime_2025"]["dette_mdeur"]
    c["F12d"] = {"h_election": mil["2025-Q1"] - mil["2017-Q2"], "h_janvier": mil["2025-Q1"] - mil["2016-Q4"], "h_hollande": mil["2017-Q2"] - mil["2012-Q2"]}
    for k in ("2012-Q2", "2016-Q4", "2017-Q2"):
        if abs(mil[k] - Tm[k]) > 0.05:
            log("note : %s revise depuis la seance (%.1f contre %.1f)" % (k, mil[k], Tm[k]))
    # F5 : millions d'euros par heure
    h = 365 * 24
    c["F5"] = {"hausse_h": (q("2025-Q1") - q("2024-Q1")) * 1000 / h, "deficit24_h": -DR["2024"]["solde"] / 100 * pib[2024] * 1000 / h,
               "prevu_h": 0.054 * pib[2025] * 1000 / h}

    # F4 : intérêts et enseignement, trois périmètres
    cour, pl, se = doc["cour_fevrier_2025"], doc["plafonds_juillet_2025"], doc["senat_plf_2026"]
    ens_pensions_25 = se["enseignement_scolaire_plf_2026_avec_pensions_mdeur"] - se["enseignement_scolaire_hausse_avec_pensions_mdeur"]
    an_ed = max(int(a) for a in ED if a in INT)
    c["F4"] = {"an": an_ed, "int_apu": INT[str(an_ed)], "ens_apu": ED[str(an_ed)], "r_apu": INT[str(an_ed)] / ED[str(an_ed)] * 100,
               "cour_2029": cour["interets_apu_mdeur"]["2029"],
               "etat_dette_25": se["charge_dette_etat_lfi_2025_budgetaire_mdeur"], "etat_ens_25": se["enseignement_scolaire_lfi_2025_hors_pensions_mdeur"],
               "r_etat_25": se["charge_dette_etat_lfi_2025_budgetaire_mdeur"] / se["enseignement_scolaire_lfi_2025_hors_pensions_mdeur"] * 100,
               "ef_26": pl["missions_mdeur"]["engagements_financiers"]["2026"], "es_26": pl["missions_mdeur"]["enseignement_scolaire"]["2026"],
               "r_plaf_26": pl["missions_mdeur"]["engagements_financiers"]["2026"] / pl["missions_mdeur"]["enseignement_scolaire"]["2026"] * 100,
               "ens_pensions_25": ens_pensions_25, "r_pensions_25": se["charge_dette_etat_lfi_2025_budgetaire_mdeur"] / ens_pensions_25 * 100,
               "gouv_apu_25": pl["charge_apu_2025_mdeur_plus_de"], "etat_2027": se["charge_dette_etat_2027_plus_de_mdeur"],
               "etat_2029": se["charge_dette_etat_2029_plus_de_mdeur"]}

    # F3 : intérêts prévus par la Cour et surcroît de production
    pib29 = cour["interets_apu_mdeur"]["2029"] / (cour["interets_apu_pts_pib"]["2029"] / 100)
    c["F3"] = {"cour": cour["interets_apu_mdeur"], "cour_pts": cour["interets_apu_pts_pib"], "cour_2024": cour["interets_apu_2024_mdeur"],
               "surcroit_25": pib[2025] - pib[2024], "pib29": pib29, "surcroit29_g2": pib29 * 0.02 / 1.02, "surcroit29_g3": pib29 * 0.03 / 1.03,
               "orateur_creation": 50, "orateur_verse": 107,
               "r_bas": cour["interets_apu_mdeur"]["2029"] / (pib29 * 0.03 / 1.03), "r_haut": cour["interets_apu_mdeur"]["2029"] / (pib29 * 0.02 / 1.02)}

    # F14 bis : deux prévisions pour 2026
    c["F14"] = {"bayrou": 75, "ciotti": 66, "int_2017": INT["2017"], "hausse_vs_2017": (66 / INT["2017"] - 1) * 100,
                "gouv_2025": pl["charge_apu_2025_mdeur_plus_de"], "cour_2025": cour["interets_apu_mdeur"]["2025"], "cour_2029": cour["interets_apu_mdeur"]["2029"],
                "ef_26": pl["missions_mdeur"]["engagements_financiers"]["2026"]}

    # Inventaire de la séance : bornes sur les trois codages (A, B, arbitre)
    cods = inv["codages"].values()
    rng = lambda f: (min(f(x) for x in cods), max(f(x) for x in cods))
    c["INV"] = {"n": inv["corpus"]["enonces"], "n_hors_rapporte": inv["corpus"]["hors_rapporte"], "n_noyau": inv["corpus"]["noyau"],
                "tech_gouv": rng(lambda x: x["nec_technique"].get("gouvernement_soutien", 0)),
                "tech_opp": rng(lambda x: x["nec_technique"].get("opposition", 0)),
                "tech_bayrou": rng(lambda x: x["nec_technique_bayrou"]),
                "neg_opp": rng(lambda x: x["negation_contrainte"].get("opposition", 0)),
                "neg_ailleurs": rng(lambda x: x["negation_contrainte"].get("gouvernement_soutien", 0) + x["negation_contrainte"].get("autre", 0)),
                "cond_gouv": rng(lambda x: x["nec_conditionnelle"].get("gouvernement_soutien", 0)),
                "cond_opp": rng(lambda x: x["nec_conditionnelle"].get("opposition", 0))}
    c["seance"] = doc["seance"]["enonces"]
    # Note d'autocritique du livre : témoin agrégé de la phrase des maternités (intérêts et santé, en points de PIB)
    IP = off["interets_annuels"]["series"]["pct_pib"]
    SA = off["depenses_fonction_annuelles"]["series"]["GF07"]["pct_pib"]
    an_sa = max(int(a) for a in SA)
    c["LIVRE"] = {"an0": 2011, "int0": IP["2011"], "int1": IP[max(IP)], "an_int1": int(max(IP)), "sante0": SA["2011"], "sante1": SA[str(an_sa)], "an_sante1": an_sa}
    return c


def trimestre_connu(T, date: str) -> str:
    """Dernier trimestre de dette publié à une date « AAAA-MM[-JJ] » : l'Insee le publie vers la fin du troisième mois qui
    suit (premier trimestre fin juin) ; il est compté connu à partir du mois suivant (juillet)."""
    k = int(date[:4]) * 12 + int(date[5:7])
    return max(q for q in T if k >= int(q[:4]) * 12 + 3 * int(q[-1]) + 4)


def calcul_hh(off, dyn, solde, doc, hh, gen):
    """Hors de l'hémicycle : textes de campagne des candidats de 2027 (corpus et codage hors dépôt, extrait figé
    hors_hemicycle.json). Chaque énoncé est jugé à la date de son document, sur les données publiées à cette date."""
    T = off["dette_trimestrielle"]["series"]
    Tm, Tp = T["mdeur"], T["pct_pib"]
    DR = dyn["depenses_recettes_pc_pib"]
    INT = off["interets_annuels"]["series"]["mdeur"]
    ratio = {dyn["depart"]["annee"]: dyn["depart"]["dette_pct_pib"], **{x["annee"]: x["dette_pct_pib"] for x in dyn["annees"]}}
    pib = {y: Tm["%d-Q4" % y] / ratio[y] * 100 for y in ratio if "%d-Q4" % y in Tm}
    E = {e["id"]: e for e in hh["enonces_testes"]}
    q = {k: trimestre_connu(Tm, e["date_reference"]) for k, e in E.items()}
    an_c = max(int(a) for a in DR)
    RV = solde["rec_rev"]
    ecarts = [a for a in RV if a in DR and int(a) < an_c and abs(RV[a] - DR[a]["recettes"]) > 0.05]
    if ecarts or str(an_c) not in RV:
        fail("recettes Eurostat d'octobre 2026 : ecart au jeu du site avant %d (%s) ou annee %d absente" % (an_c, ecarts, an_c))
    # manque de recettes cumulé depuis 2017 (recettes restées à leur part du PIB de 2017), édition d'octobre 2026
    manque = sum((RV["2017"] - RV[str(y)]) / 100 * pib[y] for y in range(2018, an_c + 1))
    pl, se = doc["plafonds_juillet_2025"]["missions_mdeur"], doc["senat_plf_2026"]
    p26 = doc["plafonds_juillet_2026"]
    det = {x["annee"]: x for x in gen["france"]["detention"]}
    a_det = max(det)
    cor = gen["cor"]
    q3417 = [k for k in Tm if round(Tm[k]) == E["H04"]["annonce"]["niveau"]]
    return {
        "corpus": hh["corpus"], "accord": hh["accord"], "unites_arbitrees": hh["unites_arbitrees"], "temoin": hh["temoin"],
        "registres": hh["registres"], "enonces": E, "q": q, "date_corpus": hh["date_reference_corpus"], "testables": hh["testables"],
        "tot": {r: sum(v[r] for v in hh["registres"].values()) for r in next(iter(hh["registres"].values()))},
        "dette": {k: Tm[k] for k in ("2016-Q2", "2016-Q4", "2017-Q2", "2017-Q4", "2024-Q4", "2025-Q2", "2026-Q1", "2026-Q2") if k in Tm},
        "dette_pct": {k: Tp[k] for k in ("2017-Q4", "2024-Q4", "2025-Q2", "2026-Q1", "2026-Q2") if k in Tp},
        "max_pct": max(Tp.values()), "q3417": q3417,
        "fin24_mai25": solde["dette_fin2024_mai2025"],
        "h_elec": {k: Tm[v] - Tm["2017-Q2"] for k, v in q.items()}, "h_jan": {k: Tm[v] - Tm["2016-Q4"] for k, v in q.items()},
        "pts_17": {k: Tp[v] - Tp["2017-Q4"] for k, v in q.items()},
        "an_c": an_c, "int_c": INT[str(an_c)], "int_max": max(INT.values()),
        # rec_c : millésime du printemps 2026, figé (le jeu du site est passé à l'édition d'octobre le 02/11/2026)
        "rec17": DR["2017"]["recettes"], "rec_c": doc["recettes_printemps_2026"]["recettes_pct_pib"][str(an_c)], "solde_c": DR[str(an_c)]["solde"],
        "rec_rev_c": RV[str(an_c)], "rec_rev_maj": solde["rec_rev_maj"],
        "solde17": DR["2017"]["solde"], "solde24": DR["2024"]["solde"],
        "manque": manque, "manque_pts": manque / pib[an_c] * 100, "dette_sans_pct": (Tm["%d-Q4" % an_c] - manque) / pib[an_c] * 100,
        "es25": pl["enseignement_scolaire"]["2025"], "ef25": pl["engagements_financiers"]["2025"], "def25": pl["defense"]["2025"],
        "es26": p26["missions_mdeur"]["enseignement_scolaire"]["2026"], "ef26": p26["missions_mdeur"]["engagements_financiers"]["2026"],
        "def26": p26["missions_mdeur"]["defense"]["2026"], "autres26": p26["autres_missions_max_mdeur"]["2026"],
        "es27": p26["missions_mdeur"]["enseignement_scolaire"]["2027"], "ef27": p26["missions_mdeur"]["engagements_financiers"]["2027"],
        "def27": p26["missions_mdeur"]["defense"]["2027"], "autres27": p26["autres_missions_max_mdeur"]["2027"],
        "p26_date": p26["date_publication"], "apuc26": p26["interets_apuc_mdeur"]["2026"], "apuc27": p26["interets_apuc_mdeur"]["2027"],
        "etat25": se["charge_dette_etat_lfi_2025_budgetaire_mdeur"],
        "nr_etat": gen["etat_negociable"]["valeur_dernier"], "nr_etat_per": gen["etat_negociable"]["dernier"],
        "nr_apu": det[a_det]["part_non_residents"], "a_det": a_det,
        "cor_pct": -cor["solde0"], "cor_an": cor["a0"], "cor_mdeur": -cor["solde0"] / 100 * pib[cor["a0"]],
    }


def arrondi_rang(v: float, annonce: int) -> bool:
    """Grille de tolérances : un nombre rond annoncé est exact si la valeur s'arrondit, au rang de son dernier chiffre non
    nul, au nombre annoncé (400 -> [350 ; 450[ ; 1 200 -> [1 150 ; 1 250[)."""
    rang = 1
    while annonce % (rang * 10) == 0:
        rang *= 10
    return annonce - rang / 2 <= v < annonce + rang / 2


# ------------------------------------------------------------------ mutations (témoin positif des gardes)
def mutation(c):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m is None:
        return None
    if m == "f1":
        c["F1"]["annees_excedent_depuis_1949"].append(2000); c["F1"]["dernier_excedent"] = 2000
    elif m == "f2":
        for x in c["F2"]["annees"]:
            x["ecart_pct"] = 1.0
        c["F2"]["n_sup20"] = 0
    elif m == "f3":
        c["F3"]["r_haut"] = 2.1
    elif m == "f4":
        c["F4"]["cour_2029"] = 160.0
    elif m == "f5":
        c["F5"]["hausse_h"] = 18.1
    elif m == "f6":
        c["F6d"]["2017-2024"]["depenses"] = 1.4
    elif m == "f8":
        c["F8"]["hdat"]["2025-09-08"] = 3.47
    elif m == "f12":
        c["F12"]["h_election"] = 990.0
    elif m == "f13":
        c["F12d"]["h_hollande"] = 330.0
    elif m == "f16":
        c["F16"]["g24"] = 2.1
    elif m == "inv":
        c["INV"]["tech_opp"] = (0, 2)
    elif m == "hh":
        c["HH"]["cor_mdeur"] = 45.0
    else:
        fail("mutation inconnue : " + m)
    return m


# ------------------------------------------------------------------ gardes : chaque qualificatif de la prose
def gardes(c):
    n = [0]
    mut = any(a.startswith("--mutation") for a in sys.argv[1:])

    def g(cond, msg):
        n[0] += 1
        if not cond:
            if mut:
                log("garde mordue (attendu sous mutation) : " + msg)
                sys.exit(0)
            fail("garde : " + msg)

    f1 = c["F1"]
    g(f1["dernier_excedent"] == 1974 and f1["derniere_annee"] - 1974 >= 50,
      "F1 « pas de budget en équilibre depuis cinquante et un ans » : dernier excédent en 1974, déficit chaque année depuis")
    g(f1["excedent_mdeur"] > 0 and round(f1["excedent_mdeur"], 1) == 0.2, "F1 « un excédent de 0,2 milliard en 1974 »")
    g(2025 - f1["dernier_excedent"] == 51, "F1 : 2025 - 1974 = cinquante et un ans")
    g(len(f1["primaire_positif"]) >= 1, "F1 variante : le solde hors intérêts a été positif certaines années")
    f2 = c["F2"]
    g(f2["n_sup20"] / f2["n"] > 0.4, "F2 « l'écart dépasse 20 % du déficit plus de quatre années sur dix »")
    g(abs(f2["somme_var"] / f2["somme_def"] - 1) < 0.06, "F2 « sur trente ans, les cumuls sont proches (moins de 6 %) »")
    f16 = c["F16"]
    g(f16["g25"] < f16["g_seuil"], "F16 « la croissance nominale de 2025 est restée sous le seuil qui stabilise le ratio à 3 % »")
    g(f16["g24"] > f16["g_seuil24"], "F16 à la date « en 2024, dernière année connue, la croissance dépassait le seuil »")
    g(f16["stab_g25"] < 3 < f16["stab_g3"], "F16 : à 2025, le déficit stabilisant est sous 3 % ; à 3 % de croissance, au-dessus")
    g(80 < f16["euros_3pct"] < 100, "F16 « un besoin de financement d'environ 90 milliards par an »")
    f8 = c["F8"]
    g(f8["ecart"][f8["m_aout"]] > 0 and f8["ecart"][f8["m_sept"]] > 0, "F8 « France au-dessus de la Grèce en août et en septembre 2025 »")
    for d in f8["bog"]:
        g(f8["bog"][d]["FR"] > f8["bog"][d]["GR"], "F8 « France au-dessus de la Grèce le %s (Banque de Grèce) »" % d)
    g(f8["bog"]["2025-09-04"]["FR"] - f8["bog"]["2025-09-04"]["GR"] < 0.10, "F8 « d'un cheveu : moins d'un dixième de point le 4 septembre »")
    g(abs(f8["fr_de_2025"] - f8["el_de_2025"]) < 0.1, "F8 « en moyenne sur 2025, écarts à l'Allemagne quasi égaux »")
    g(f8["premier_dessus"] >= "2025-07" and len(f8["dessous_2026"]) >= 1,
      "F8 « la France passe au-dessus à l'été 2025, et la Grèce repasse au-dessus en 2026 »")
    g(f8["tec10"]["2025-09-08"] < f8["tec10"]["2025-09-04"], "F8 « le taux français baisse entre le 4 et le 8 septembre »")
    j8 = f8["tec10"]["2025-09-08"] - f8["hdat"]["2025-09-08"]
    meth = max(abs(f8["tec10"]["2025-09-04"] - f8["bog"]["2025-09-04"]["FR"]), abs(f8["hdat"]["2025-09-04"] - f8["bog"]["2025-09-04"]["GR"]))
    g(j8 > 0.1 and j8 > 3 * meth, "F8 « le jour même, France au-dessus d'environ 0,15 point, bien au-delà de l'écart entre méthodes »")
    f6 = c["F6"]
    w = f6["2017-2024"]
    g(abs(w["depenses"]) <= 1 and w["recettes"] < -2 and w["depenses"] > w["recettes"],
      "F6 « 2017-2024 : dépenses stables à un point près, recettes en net recul »")
    g(f6["2019-2024"]["depenses"] > 1 and f6["2019-2025"]["depenses"] > 1, "F6 « depuis 2019, les dépenses montent de plus d'un point »")
    g(-f6["2019-2024"]["recettes"] > f6["2019-2024"]["depenses"] and f6["2019-2025"]["depenses"] > -f6["2019-2025"]["recettes"],
      "F6 « depuis 2019 : recettes de justesse en 2024, dépenses en 2025 »")
    f6d = c["F6d"]
    g(abs(f6d["2017-2024"]["depenses"]) <= 1 and f6d["2017-2024"]["recettes"] < -2, "F6 à la date « dépenses stables à un point près, recettes en net recul »")
    g(f6d["2019-2024"]["depenses"] > 1, "F6 à la date « depuis 2019, les dépenses montent de plus d'un point »")
    g((f6d["2019-2024"]["depenses"] > -f6d["2019-2024"]["recettes"]) != (f6["2019-2024"]["depenses"] > -f6["2019-2024"]["recettes"]),
      "F6 « sur 2019-2024, la prédominance change entre les comptes de mai 2025 et les comptes révisés »")
    f12d = c["F12d"]
    g(arrondi_rang(f12d["h_hollande"], 400) and arrondi_rang(f12d["h_janvier"], 1200) and not arrondi_rang(f12d["h_election"], 1200)
      and f12d["h_election"] > 1000, "F12-F13 à la date : 1 000 dépassé, 1 200 depuis janvier seulement, 400 à la centaine")
    f12 = c["F12"]
    g(min(f12["h_election"], f12["h_janvier"], f12["h_t2"]) > 1000, "F12 « plus de 1 000 milliards sous toutes les variantes »")
    g(arrondi_rang(f12["h_hollande"], 400), "F13 « 400 milliards sous F. Hollande : exact à la centaine »")
    g(arrondi_rang(f12["h_janvier"], 1200) and not arrondi_rang(f12["h_election"], 1200),
      "F13 « 1 200 : exact depuis janvier 2017, pas depuis l'élection »")
    g(abs(f12["pts_macron_an"] - f12["pts_hollande_an"]) < 0.3 and f12["eur_macron_an"] > 1.5 * f12["eur_hollande_an"],
      "F13 « en points de PIB par an, comparable ; en euros, près du double »")
    f5 = c["F5"]
    g(round(f5["hausse_h"]) > 18 and not (17.5 <= f5["hausse_h"] < 18.5), "F5 « la hausse de la dette dépasse 18 millions par heure »")
    g(abs(f5["prevu_h"] - 18) < 1, "F5 « le déficit prévu pour 2025 donne un chiffre proche de 18 millions par heure »")
    f4 = c["F4"]
    g(f4["r_apu"] < 50 and f4["cour_2029"] < f4["ens_apu"], "F4 « administrations : intérêts sous la moitié, pas de dépassement d'ici 2029 »")
    g(75 < f4["r_etat_25"] < 100 and f4["r_plaf_26"] > f4["r_etat_25"] and f4["r_plaf_26"] < 100, "F4 « État : rapprochement, sans dépassement en 2025-2026 »")
    g(f4["r_pensions_25"] < 75, "F4 « État avec pensions : loin du dépassement »")
    g(f4["gouv_apu_25"] > f4["etat_ens_25"], "F4 « la phrase du gouvernement compare deux périmètres : 66 > 64,3 »")
    f3 = c["F3"]
    r = f3["orateur_verse"] / f3["orateur_creation"]
    g(1.75 <= r < 2.25, "F3 « 107 contre 50 : le double, arithmétiquement »")
    g(f3["r_haut"] < 1.75 and f3["r_bas"] > 1, "F3 « à dates alignées, ce n'est plus le double : 1,1 à 1,6 fois »")
    g(f3["cour"]["2029"] == 107 and f3["cour"]["2025"] == 67, "F3 « les montants sont ceux de la Cour »")
    f14 = c["F14"]
    g(f14["cour_2025"] < f14["bayrou"] < f14["cour_2029"], "F14 « 75 dans la trajectoire de la Cour »")
    g(f14["ciotti"] == f14["gouv_2025"] and f14["ciotti"] < f14["cour_2025"] and f14["ciotti"] != f14["ef_26"],
      "F14 « 66 = chiffre officiel de 2025, aucune prévision 2026 lue »")
    g(arrondi_rang(f14["hausse_vs_2017"], 60), "F14 « 60 % de plus qu'en 2017 : exact à la dizaine »")
    lv = c["LIVRE"]
    g(lv["int1"] < lv["int0"] and lv["sante1"] > lv["sante0"], "livre « depuis 2011, intérêts en recul et santé en hausse, en points de PIB »")
    inv = c["INV"]
    g(inv["tech_opp"] == (0, 0) and inv["tech_gouv"][0] >= 10, "inventaire « nécessité technique : gouvernement et soutien seulement »")
    g(inv["tech_bayrou"][0] * 2 > inv["tech_gouv"][1], "inventaire « surtout F. Bayrou : plus de la moitié »")
    g(inv["neg_opp"][0] >= 10 and inv["neg_ailleurs"][1] <= 1, "inventaire « contrainte niée : opposition, au plus un énoncé ailleurs »")
    g(inv["cond_opp"] == (0, 0), "inventaire « conséquence conditionnelle : jamais dans l'opposition »")
    # hors de l'hémicycle : candidats de 2027, chaque énoncé jugé à la date de son document
    hh = c["HH"]
    E, q, D, P, R, K = hh["enonces"], hh["q"], hh["dette"], hh["dette_pct"], hh["registres"], hh["corpus"]
    an = lambda k, x: E[k]["annonce"][x]
    g(K["candidats_avec_texte"] + len(K["sans_texte"]) == K["declares"], "hors hémicycle : candidats avec texte + sans texte = déclarés")
    g("asselineau" in K["sans_texte"] and "le-pen" in K["candidats_sans_enonce"], "« F. Asselineau sans texte retrouvé ; aucun énoncé retenu chez M. Le Pen »")
    g(R["attal"]["necessite"] == max(v["necessite"] for v in R.values()), "« la nécessité : d'abord G. Attal »")
    regs = ("necessite", "contrainte_reconnue_politique_contestee", "alarme_contestee", "contrainte_niee", "dette_illegitime")
    g(all(R[x]["contrainte_reconnue_politique_contestee"] == max(R[x][r] for r in regs) for x in ("melenchon", "ruffin", "tondelier", "philippot")),
      "« contrainte reconnue, politique contestée : le plus fréquent des registres chez J.-L. Mélenchon, F. Ruffin, M. Tondelier et F. Philippot »")
    g(R["ruffin"]["necessite"] >= 5 and R["philippot"]["contrainte_reconnue_politique_contestee"] >= 5, "« les deux registres chez F. Ruffin ; F. Philippot dans le même registre argumentatif »")
    g(hh["tot"]["aucun"] * 2 > K["enonces"], "« la majorité des énoncés ne prennent position sur aucun registre »")
    g(R["melenchon"]["dette_illegitime"] * 2 > hh["tot"]["dette_illegitime"], "« annuler une part de la dette : surtout J.-L. Mélenchon »")
    g(hh["tot"]["contrainte_niee"] == 1, "« un seul énoncé nie explicitement la contrainte »")
    g("labib" in K["candidats_sans_enonce"] and "arthaud" in R, "« l'extrême gauche : Lutte ouvrière testée ; le texte du NPA-Révolutionnaires sans énoncé »")
    g(q["H00"] == "2026-Q1" and round(P["2026-Q1"], 1) == an("H00", "pct") and arrondi_rang(P["2026-Q1"] - P["2017-Q4"], 19),
      "H00 « 117,5 % au premier trimestre 2026, dix-neuf points de plus qu'en 2017 » : exact")
    g(q["H02"] == "2026-Q2" and arrondi_rang(D["2026-Q2"], an("H02", "niveau")), "H02 « 3 600 milliards » : exact au dernier trimestre publié")
    g(hh["q3417"] == ["2025-Q2"] and arrondi_rang(P["2025-Q2"], an("H04", "pct")) and P["2025-Q2"] < an("H04", "pct") - 3
      and hh["max_pct"] < an("H04", "pct") and D[q["H04"]] > an("H04", "niveau") + 100,
      "H04 « 3 417 milliards, 120 % » : montant de mi-2025, ratio exact à la dizaine seulement, dépassé à la date")
    g(hh["fin24_mai25"]["mdeur"] > an("H05", "niveau") and hh["fin24_mai25"]["pct_pib"] > an("H05", "pct") and P["2024-Q4"] < an("H05", "pct")
      and q["H05"] == "2026-Q1" and D["2026-Q1"] > an("H05", "niveau") and P["2026-Q1"] > an("H05", "pct"),
      "H05 « dépasse 3 305 milliards, plus de 113 % » : seuils dépassés à la date ; chiffres de fin 2024 publiés en mai 2025")
    g(arrondi_rang(D["2026-Q1"], an("H06", "niveau")) and q["H06"] == "2026-Q2" and not arrondi_rang(D["2026-Q2"], an("H06", "niveau"))
      and not arrondi_rang(D[q["H07"]], an("H07", "niveau")), "H06-H07 « 3 500 » exact au premier trimestre, dépassé au deuxième ; « 3 000 » inexact")
    g(q["H01"] == "2026-Q1" and not arrondi_rang(hh["h_elec"]["H01"], 1400) and not arrondi_rang(hh["h_jan"]["H01"], 1400),
      "H01 « 1 400 milliards depuis 2017 » (juillet 2026) : inexact depuis l'élection comme depuis janvier")
    g(not arrondi_rang(hh["h_elec"]["H02"], an("H02", "hausse")) and arrondi_rang(hh["h_jan"]["H02"], an("H02", "hausse")),
      "H02 « + 1 400 sous les quinquennats » : exact depuis janvier 2017 seulement")
    g(arrondi_rang(hh["h_elec"]["H03"], an("H03", "hausse")) and not arrondi_rang(hh["h_jan"]["H03"], an("H03", "hausse")),
      "H03 « 1 300 milliards » : exact depuis l'élection")
    g(hh["es25"] > hh["ef25"] > hh["def25"], "H09 « pour 2025, la mission de la charge de la dette est la deuxième, derrière l'enseignement scolaire »")
    g(hh["es26"] > hh["ef26"] > hh["def26"] > hh["autres26"], "H08-H10 « loi de finances 2026 : deuxième, derrière l'enseignement scolaire, devant la Défense »")
    g(hh["ef27"] > hh["es27"] > hh["def27"] > hh["autres27"] and hh["p26_date"] == E["H08"]["date_reference"] and E["H10"]["date_reference"] < hh["p26_date"],
      "H08-H10 « plafonds 2027, publiés le jour de la lettre de B. Cazeneuve et après le texte de N. Arthaud : en tête »")
    from datetime import date
    g((date.fromisoformat(hh["p26_date"]) - date.fromisoformat(E["H10"]["date_reference"])).days == 9,
      "H10 « les plafonds de 2027, publiés neuf jours plus tard »")
    g(hh["manque"] < an("H13", "moins"), "H13 « au moins 400 » : le calcul à part de recettes constante reste en deçà, sans pouvoir réfuter")
    g(hh["int_c"] > hh["es26"] > hh["ef26"], "H10 « devant l'Éducation nationale » : en 2026, seulement en comparant toutes les administrations à une mission de l'État")
    g(not arrondi_rang(hh["int_c"], an("H11", "interets")) and hh["int_max"] < an("H11", "interets") - 5 and hh["apuc27"] < an("H11", "interets"),
      "H11 « 80 milliards d'intérêts par an » : aucune année réalisée, ni la prévision des administrations centrales pour 2027")
    g(hh["an_c"] == 2025 and round(-hh["solde_c"] - (hh["rec17"] - hh["rec_c"]), 1) == an("H12", "solde_sans")
      and round(-hh["solde_c"] - (hh["rec17"] - hh["rec_rev_c"]), 1) != an("H12", "solde_sans"),
      "H12 « 2,9 % au lieu de 5,1 % » : exact au millésime du printemps, pas avec l'édition d'octobre 2026")
    g(abs(hh["dette_sans_pct"] - an("H13", "pct")) <= 10, "H13 « proche de 100 % » : compatible")
    g(arrondi_rang(hh["pts_17"]["H14"], an("H14", "points")) and hh["manque_pts"] < hh["pts_17"]["H14"],
      "H14 « + 20 points » : hausse exacte ; le calcul à part de recettes constante ne suffit pas à reconstituer l'attribution")
    g(hh["nr_etat"] >= an("H15", "pct") > hh["nr_apu"], "H15 « plus de 55 % détenus par l'étranger » : exact pour l'État, pas pour l'ensemble")
    g(hh["cor_mdeur"] < an("H16", "manque") / 4, "H16 « au moins 40 milliards par an » : loin du solde du Conseil d'orientation des retraites")
    g(-hh["solde_c"] > an("H17", "seuil") and all(-c["F1"]["solde_pct"][a] > 3 for a in c["F1"]["solde_pct"] if a >= 2020),
      "H17 « le seuil de 3 % n'est pas tenu » : déficit au-dessus de 3 % chaque année depuis 2020")
    g(round(-hh["solde17"], 1) == an("H18", "de") and round(-hh["solde24"], 1) == an("H18", "a"), "H18 « de 3,4 % à 5,8 % » sur 2017-2024 : exact")
    return n[0]


# ------------------------------------------------------------------ affichage (mêmes clés, deux langues)
def mois_txt(m: str, lang: str) -> str:
    a, mm = m.split("-")
    return ("%s %s" % (MOIS[lang][int(mm) - 1], a))


def affichage(c, lang):
    n1 = lambda v: nb(v, 1, lang)
    n0 = lambda v: nb(v, 0, lang)
    n2 = lambda v: nb(v, 2, lang)
    f1, f2, f16, f8, f6, f12, f5, f4, f3, f14, inv = (c[k] for k in ("F1", "F2", "F16", "F8", "F6", "F12", "F5", "F4", "F3", "F14", "INV"))
    rng = lambda t: ("%d à %d" if lang == "fr" else "%d to %d") % t if t[0] != t[1] else "%d" % t[0]
    sg = lambda v: ("+" if v > 0 else "−") + nb(abs(v), 1, lang)
    prim = f1["primaire_positif"]
    a = {
        "f1_an": str(f1["dernier_excedent"]), "f1_exc": n1(f1["excedent_mdeur"]), "f1_dern": str(f1["derniere_annee"]),
        "f1_n": str(f1["derniere_annee"] - f1["dernier_excedent"]), "f1_an1": str(f1["dernier_excedent"] + 1),
        "f1_prim": ("%d à %d" if lang == "fr" else "%d to %d") % (prim[0], prim[-1]) if prim == list(range(prim[0], prim[-1] + 1)) else ", ".join(map(str, prim)),
        "f1_prim_n": str(len(prim)), "f1_prim_l": lg.lettres(len(prim), lang),
        "f2_n": str(f2["n"]), "f2_sup": str(f2["n_sup20"]), "f2_def": n0(f2["somme_def"]), "f2_var": n0(f2["somme_var"]),
        "f2_an0": str(f2["an0"]), "f2_an1": str(f2["an1"]), "f2_ecart_cumul": n0(abs(f2["somme_var"] / f2["somme_def"] - 1) * 100),
        "f2_2020": n0(next(x["ecart"] for x in f2["annees"] if x["annee"] == 2020)),
        "f16_dette": n1(f16["dette_pct"]), "f16_g25": n2(f16["g25"]), "f16_stab": n2(f16["stab_g25"]), "f16_stab3": n2(f16["stab_g3"]),
        "f16_seuil": n2(f16["g_seuil"]), "f16_eur": n0(round(f16["euros_3pct"], -1)),  # ordre de grandeur arrondi : le PIB de l'année ne fait pas le verdict (audit du 05/11/2026)
        "f16_dette24": n1(f16["dette_pct24"]), "f16_g24": n2(f16["g24"]), "f16_seuil24": n2(f16["g_seuil24"]),
        "f8_aout_fr": n2(f8["fr"]["2025-08"]), "f8_aout_el": n2(f8["el"]["2025-08"]),
        "f8_sept_fr": n2(f8["fr"]["2025-09"]), "f8_sept_el": n2(f8["el"]["2025-09"]),
        "f8_j4_fr": n2(f8["bog"]["2025-09-04"]["FR"]), "f8_j4_gr": n2(f8["bog"]["2025-09-04"]["GR"]),
        "f8_j18_fr": n2(f8["bog"]["2025-09-18"]["FR"]), "f8_j18_gr": n2(f8["bog"]["2025-09-18"]["GR"]),
        "f8_j4_ecart": n2(f8["bog"]["2025-09-04"]["FR"] - f8["bog"]["2025-09-04"]["GR"]),
        "f8_j18_ecart": n2(f8["bog"]["2025-09-18"]["FR"] - f8["bog"]["2025-09-18"]["GR"]),
        "f8_tec4": n2(f8["tec10"]["2025-09-04"]), "f8_tec8": n2(f8["tec10"]["2025-09-08"]),
        "f8_hdat8": n2(f8["hdat"]["2025-09-08"]), "f8_hdat4": n2(f8["hdat"]["2025-09-04"]),
        "f8_j8_ecart": n2(f8["tec10"]["2025-09-08"] - f8["hdat"]["2025-09-08"]),
        "f8_frde": n2(f8["fr_de_2025"]), "f8_elde": n2(f8["el_de_2025"]),
        "f8_premier": mois_txt(f8["premier_dessus"], lang), "f8_dernier": mois_txt(f8["dernier"], lang),
        "f8_dessous": (("de %s à %s" if lang == "fr" else "%s to %s") % (MOIS[lang][int(f8["dessous_2026"][0][5:]) - 1], mois_txt(f8["dessous_2026"][-1], lang))
                       if len(f8["dessous_2026"]) > 1 else mois_txt(f8["dessous_2026"][0], lang)),
        "f8_ecart_dernier": n2(f8["ecart"][f8["dernier"]]),
        "f6_dep": sg(f6["2017-2024"]["depenses"]), "f6_rec": sg(f6["2017-2024"]["recettes"]),
        "f6_dep19": sg(f6["2019-2024"]["depenses"]), "f6_rec19": sg(f6["2019-2024"]["recettes"]),
        "f6_dep1925": sg(f6["2019-2025"]["depenses"]), "f6_rec1925": sg(f6["2019-2025"]["recettes"]),
        "f6_dep1725": sg(f6["2017-2025"]["depenses"]), "f6_rec1725": sg(f6["2017-2025"]["recettes"]),
        "f6d_dep": sg(c["F6d"]["2017-2024"]["depenses"]), "f6d_rec": sg(c["F6d"]["2017-2024"]["recettes"]),
        "f6d_dep19": sg(c["F6d"]["2019-2024"]["depenses"]), "f6d_rec19": sg(c["F6d"]["2019-2024"]["recettes"]),
        "f6d_dep_pt": lg.points(c["F6d"]["2017-2024"]["depenses"], 1, lang, True), "f6d_rec_pt": lg.points(c["F6d"]["2017-2024"]["recettes"], 1, lang, True),
        "f6d_dep19_hausse": lg.points(c["F6d"]["2019-2024"]["depenses"], 1, lang),
        "f8_frde_pt": lg.points(f8["fr_de_2025"], 2, lang), "f13_pts_mac_pt": lg.points(f12["pts_macron_an"], 1, lang),
        "f12d_elec": n0(c["F12d"]["h_election"]), "f12d_jan": n0(c["F12d"]["h_janvier"]), "f12d_hol": n0(c["F12d"]["h_hollande"]),
        "f12_elec": n0(f12["h_election"]), "f12_jan": n0(f12["h_janvier"]), "f12_t2": n0(f12["h_t2"]), "f12_hol": n0(f12["h_hollande"]),
        "f13_pts_mac": n1(f12["pts_macron_an"]), "f13_pts_hol": n1(f12["pts_hollande_an"]),
        "f13_eur_mac": n0(f12["eur_macron_an"]), "f13_eur_hol": n0(f12["eur_hollande_an"]),
        "f5_hausse": n1(f5["hausse_h"]), "f5_prevu": n1(f5["prevu_h"]), "f5_def24": n1(f5["deficit24_h"]),
        "f4_an": str(f4["an"]), "f4_int": n1(f4["int_apu"]), "f4_ens": n1(f4["ens_apu"]), "f4_r": n0(f4["r_apu"]),
        "f4_cour29": n0(f4["cour_2029"]), "f4_etat_dette": n1(f4["etat_dette_25"]), "f4_etat_ens": n1(f4["etat_ens_25"]),
        "f4_r_etat": n0(f4["r_etat_25"]), "f4_ef26": n1(f4["ef_26"]), "f4_es26": n1(f4["es_26"]), "f4_r26": n0(f4["r_plaf_26"]),
        "f4_ens_pens": n1(f4["ens_pensions_25"]), "f4_r_pens": n0(f4["r_pensions_25"]), "f4_gouv": n0(f4["gouv_apu_25"]),
        "f4_etat27": n0(f4["etat_2027"]), "f4_etat29": n0(f4["etat_2029"]),
        "f3_25": n0(f3["cour"]["2025"]), "f3_29": n0(f3["cour"]["2029"]), "f3_31": n0(f3["cour"]["2031"]), "f3_24": n0(f3["cour_2024"]),
        "f3_surcroit25": n1(f3["surcroit_25"]), "f3_s29_bas": n0(f3["surcroit29_g2"]), "f3_s29_haut": n0(f3["surcroit29_g3"]),
        "f3_pib29": n0(f3["pib29"]), "f3_r_bas": n1(f3["r_bas"]), "f3_r_haut": n1(f3["r_haut"]),
        "f14_int17": n1(f14["int_2017"]), "f14_hausse": n0(f14["hausse_vs_2017"]), "f14_ef26": n1(f14["ef_26"]),
        "lv_int0": n1(c["LIVRE"]["int0"]), "lv_int1": n1(c["LIVRE"]["int1"]), "lv_an_int1": str(c["LIVRE"]["an_int1"]),
        "lv_sante0": n1(c["LIVRE"]["sante0"]), "lv_sante1": n1(c["LIVRE"]["sante1"]), "lv_an_sante1": str(c["LIVRE"]["an_sante1"]),
        "inv_n": str(inv["n"]), "inv_noyau": str(inv["n_noyau"]),
        "inv_tech": rng(inv["tech_gouv"]), "inv_bayrou": rng(inv["tech_bayrou"]), "inv_neg": rng(inv["neg_opp"]),
        "inv_cond": rng(inv["cond_gouv"]),
    }
    a.update(affichage_hh(c["HH"], lang))
    return a


def affichage_hh(hh, lang):
    n0 = lambda v: nb(v, 0, lang)
    n1 = lambda v: nb(v, 1, lang)
    n2 = lambda v: nb(v, 2, lang)
    K, R, T = hh["corpus"], hh["registres"], hh["tot"]
    D, P = hh["dette"], hh["dette_pct"]
    reg = {"nec": "necessite", "crpc": "contrainte_reconnue_politique_contestee", "ala": "alarme_contestee", "cn": "contrainte_niee",
           "dil": "dette_illegitime", "auc": "aucun"}
    a = {"hh_declares": str(K["declares"]), "hh_avec": str(K["candidats_avec_texte"]), "hh_docs": str(K["documents"]),
         "hh_sans_l": lg.lettres(len(K["sans_texte"]), lang), "hh_enonces": str(K["enonces"]), "hh_cand": str(K["candidats_enonces"]),
         "hh_test": str(K["testables"]), "hh_vides": str(len(K["candidats_sans_enonce"])),
         "hh_k_ret": n2(hh["accord"]["retenu"]["kappa"]), "hh_k_reg": n2(hh["accord"]["registre"]["kappa"]), "hh_arb": str(hh["unites_arbitrees"]),
         "hh_tem_docs": str(hh["temoin"]["documents"]), "hh_tem_manq": str(hh["temoin"]["documents_manques"]),
         "hh_tem_pct": n0(100 * hh["temoin"]["documents_manques"] / hh["temoin"]["documents"]), "hh_tem_seuil": str(hh["temoin"]["seuil_pct"]),
         "hh_t1": n1(D["2026-Q1"]), "hh_t1p": n1(P["2026-Q1"]), "hh_t2": n1(D["2026-Q2"]), "hh_t2p": n1(P["2026-Q2"]),
         "hh_t225": n1(D["2025-Q2"]), "hh_t225p": n1(P["2025-Q2"]), "hh_maxp": n1(hh["max_pct"]),
         "hh_f24m": n1(hh["fin24_mai25"]["mdeur"]), "hh_f24mp": n1(hh["fin24_mai25"]["pct_pib"]), "hh_f24p": n1(P["2024-Q4"]),
         "hh_fin17p": n1(P["2017-Q4"]), "hh_pts_t1": lg.points(hh["pts_17"]["H00"], 1, lang),
         "hh_elec1": n0(hh["h_elec"]["H01"]), "hh_jan1": n0(hh["h_jan"]["H01"]), "hh_elec2": n0(hh["h_elec"]["H02"]), "hh_jan2": n0(hh["h_jan"]["H02"]),
         "hh_an_c": str(hh["an_c"]), "hh_int_c": n1(hh["int_c"]), "hh_es26": n1(hh["es26"]), "hh_ef26": n1(hh["ef26"]), "hh_def26": n1(hh["def26"]),
         "hh_rec17": n1(hh["rec17"]), "hh_rec_c": n1(hh["rec_c"]), "hh_rec_pt": lg.points(hh["rec17"] - hh["rec_c"], 1, lang),
         "hh_solde_c": n1(-hh["solde_c"]), "hh_sans": n1(-hh["solde_c"] - (hh["rec17"] - hh["rec_c"])),
         "hh_manque": n0(hh["manque"]), "hh_sans_pct": n0(hh["dette_sans_pct"]), "hh_manque_pts": lg.points(hh["manque_pts"], 0, lang),
         "hh_nr_etat": n1(hh["nr_etat"]), "hh_nr_etat_per": per_trim(hh["nr_etat_per"], lang), "hh_nr_apu": n1(hh["nr_apu"]), "hh_a_det": str(hh["a_det"]),
         "hh_cor_pct": lg.points(hh["cor_pct"], 2, lang), "hh_cor_md": n0(hh["cor_mdeur"]), "hh_cor_an": str(hh["cor_an"])}
    a["hh_pts_h14"] = lg.points(hh["pts_17"]["H14"], 1, lang)
    a["hh_n_page"] = str(len(hh["enonces"]))
    for k in ("es25", "ef25", "def25", "es27", "ef27", "def27", "apuc27", "rec_rev_c"):
        a["hh_" + k] = n1(hh[k])
    a["hh_sans_rev"] = n1(-hh["solde_c"] - (hh["rec17"] - hh["rec_rev_c"]))
    a["hh_solde17"], a["hh_solde24"] = n1(-hh["solde17"]), n1(-hh["solde24"])
    dm = hh["rec_rev_maj"]
    a["hh_rec_rev_maj"] = "%d %s %s" % (int(dm[8:]), MOIS[lang][int(dm[5:7]) - 1], dm[:4])
    dp = hh["p26_date"]
    a["hh_p26_date"] = "%d %s %s" % (int(dp[8:]), MOIS[lang][int(dp[5:7]) - 1], dp[:4])
    for k, e in hh["enonces"].items():
        a["hh_n_" + k] = e["nom"]
        a["hh_c_" + k] = e["citation"] if lang == "fr" else e["citation_en"]
        if e["rang"] in ("date_inconnue", "A_maj"):     # pièce sans date lisible : date de capture
            dc = hh["date_corpus"]
            jour = "%d %s %s" % (int(dc[8:]), MOIS[lang][int(dc[5:7]) - 1], dc[:4])
            a["hh_d_" + k] = ("page relevée le " if lang == "fr" else "page captured on ") + jour
        else:
            a["hh_d_" + k] = mois_txt(e["date_reference"][:7], lang)
    for k, t in VERDICTS_HH.items():
        a["hh_v_" + k] = t[lang].format(**a)
    for k, r in reg.items():
        a["hh_" + k] = str(T[r])
    for cand in R:
        for k, r in reg.items():
            if k != "auc" and R[cand][r]:
                a["hh_%s_%s" % (k, cand.replace("-", "_"))] = str(R[cand][r])
    return a


# ------------------------------------------------------------------ hors de l'hémicycle : verdicts (une source, page et données)
# Chaque verdict est une garde de gardes() ; les nombres entre guillemets sont ceux des candidats.
VERDICTS_HH = {
    "H00": {"fr": "Exact : {hh_t1p} % au premier trimestre 2026, {hh_pts_t1} de plus que fin 2017",
            "en": "Accurate: {hh_t1p}% in the first quarter of 2026, {hh_pts_t1} more than at the end of 2017"},
    "H01": {"fr": "Inexact à la centaine près : {hh_elec1} milliards depuis l'élection, {hh_jan1} depuis janvier 2017 (premier trimestre 2026)",
            "en": "Inaccurate to the nearest hundred: €{hh_elec1}bn since the election, €{hh_jan1}bn since January 2017 (first quarter of 2026)"},
    "H02": {"fr": "« 3 600 » : exact ({hh_t2} au deuxième trimestre 2026 ; la page, datée de 2022, a été mise à jour). « + 1 400 » : exact depuis janvier 2017 ({hh_jan2}), pas depuis l'élection ({hh_elec2})",
            "en": "“3,600”: accurate (€{hh_t2}bn in the second quarter of 2026; the page, dated 2022, has been updated). “+1,400”: accurate from January 2017 (€{hh_jan2}bn), not from the election (€{hh_elec2}bn)"},
    "H03": {"fr": "Exact : {hh_elec2} milliards depuis l'élection de 2017 (deuxième trimestre 2026)",
            "en": "Accurate: €{hh_elec2}bn since the 2017 election (second quarter of 2026)"},
    "H04": {"fr": "Montant exact pour le deuxième trimestre 2025 ({hh_t225}), dépassé à la date ({hh_t2}) ; « 120 % » exact à la dizaine près seulement : {hh_t225p} % pour ce montant, {hh_maxp} % au plus haut",
            "en": "The amount is accurate for the second quarter of 2025 (€{hh_t225}bn), overtaken by the date (€{hh_t2}bn); “120%” is accurate only to the nearest ten: {hh_t225p}% for that amount, {hh_maxp}% at the highest"},
    "H05": {"fr": "Exact comme seuils : {hh_t1} milliards et {hh_t1p} % au premier trimestre 2026. Les nombres cités sont ceux de fin 2024 publiés en mai 2025 ({hh_f24m} milliards, {hh_f24mp} %), {hh_f24p} % depuis la révision",
            "en": "Accurate as thresholds: €{hh_t1}bn and {hh_t1p}% in the first quarter of 2026. The figures cited are the end-2024 ones published in May 2025 (€{hh_f24m}bn, {hh_f24mp}%), {hh_f24p}% since the revision"},
    "H06": {"fr": "Exact au premier trimestre 2026 ({hh_t1}), dépassé au deuxième ({hh_t2})",
            "en": "Accurate for the first quarter of 2026 (€{hh_t1}bn), overtaken in the second (€{hh_t2}bn)"},
    "H07": {"fr": "Inexact ({hh_t2} au deuxième trimestre 2026) ; le même texte écrit aussi « 3500 milliards »",
            "en": "Inaccurate (€{hh_t2}bn in the second quarter of 2026); the same text also writes “3,500 billion”"},
    "H08": {"fr": "Selon le document : inexact pour la loi de finances de 2026, où la mission qui porte la charge de la dette ({hh_ef26} milliards) reste derrière l'enseignement scolaire ({hh_es26}) ; exact pour les plafonds de 2027 publiés le jour de la lettre ({hh_ef27}, devant {hh_es27} et la Défense, {hh_def27}). Rang d'une mission, qui contient d'autres dépenses que les intérêts",
            "en": "Depends on the document: inaccurate for the 2026 Finance Act, where the programme carrying the debt charge (€{hh_ef26}bn) stays behind school education (€{hh_es26}bn); accurate for the 2027 ceilings published on the day of the letter (€{hh_ef27}bn, ahead of €{hh_es27}bn and Defence, €{hh_def27}bn). The rank of a programme that contains spending other than interest"},
    "H09": {"fr": "Exact pour 2025, l'année que vise le texte : {hh_ef25} milliards en loi de finances, derrière l'enseignement scolaire ({hh_es25}), devant la Défense ({hh_def25}). Rang d'une mission, hors pensions et hors remboursements d'impôts",
            "en": "Accurate for 2025, the year the text refers to: €{hh_ef25}bn in the Finance Act, behind school education (€{hh_es25}bn), ahead of Defence (€{hh_def25}bn). The rank of a programme, excluding pensions and tax refunds"},
    "H10": {"fr": "Inexact au même périmètre à la date du texte : en loi de finances 2026, {hh_ef26} contre {hh_es26} milliards ; vrai seulement si l'on compare les intérêts de toutes les administrations ({hh_int_c} milliards en {hh_an_c}) au budget d'un seul ministère. Les plafonds de 2027, publiés neuf jours plus tard, inversent l'ordre des missions",
            "en": "Inaccurate within one scope at the date of the text: in the 2026 Finance Act, €{hh_ef26}bn against €{hh_es26}bn; true only when the interest of all general government (€{hh_int_c}bn in {hh_an_c}) is compared with a single ministry's budget. The 2027 ceilings, published nine days later, reverse the order of the programmes"},
    "H11": {"fr": "Non établi : le texte ne dit ni l'année ni le périmètre. Aucune année réalisée n'en approche ({hh_int_c} milliards en {hh_an_c} pour toutes les administrations) ; le gouvernement prévoit {hh_apuc27} milliards en 2027 pour les seules administrations centrales",
            "en": "Not established: the text gives neither the year nor the scope. No actual year comes close (€{hh_int_c}bn in {hh_an_c} for general government as a whole); the government forecasts €{hh_apuc27}bn in 2027 for central government alone"},
    "H12": {"fr": "Exact avec les comptes du printemps 2026 (recettes de {hh_rec17} % du PIB en 2017, {hh_rec_c} % en {hh_an_c}) ; {hh_sans_rev} % avec l'édition d'octobre 2026 ({hh_rec_rev_c} %). Un calcul à dépenses inchangées, pas une cause démontrée",
            "en": "Accurate with the spring 2026 accounts (revenue of {hh_rec17}% of GDP in 2017, {hh_rec_c}% in {hh_an_c}); {hh_sans_rev}% with the October 2026 edition ({hh_rec_rev_c}%). A calculation at unchanged spending, not a proven cause"},
    "H13": {"fr": "« Au moins 400 » : non établi. Le calcul à part de recettes constante donne {hh_manque} milliards avant intérêts et effets sur l'activité, et ne suffit ni à établir ni à réfuter la borne ; « proche des 100 % » : compatible ({hh_sans_pct} %)",
            "en": "“At least 400”: not established. The calculation at a constant revenue share gives €{hh_manque}bn before interest and effects on activity, and can neither establish nor refute the bound; “close to 100%”: consistent ({hh_sans_pct}%)"},
    "H14": {"fr": "Hausse exacte ({hh_pts_h14} de fin 2017 au premier trimestre 2026) ; attribution non établie : le calcul à part de recettes constante donne environ {hh_manque_pts}, et il n'isole pas l'effet des mesures fiscales",
            "en": "The rise is accurate ({hh_pts_h14} from the end of 2017 to the first quarter of 2026); the attribution is not established: the calculation at a constant revenue share gives about {hh_manque_pts}, and does not isolate the effect of tax measures"},
    "H15": {"fr": "Exact pour la dette négociable de l'État ({hh_nr_etat} % {hh_nr_etat_per}), inexact pour celle de toutes les administrations ({hh_nr_apu} %)",
            "en": "Accurate for the State's negotiable debt ({hh_nr_etat}% {hh_nr_etat_per}), inaccurate for general government debt as a whole ({hh_nr_apu}%)"},
    "H16": {"fr": "Incompatible avec la mesure du Conseil d'orientation des retraites (besoin de financement de {hh_cor_pct} de PIB en {hh_cor_an}, environ {hh_cor_md} milliards) ; d'autres présentations comptent les contributions d'équilibre de l'État employeur, et le texte ne dit pas laquelle il retient : verdict suspendu à cette définition",
            "en": "Incompatible with the measure of the Conseil d'orientation des retraites, the official pensions advisory council (a financing need of {hh_cor_pct} of GDP in {hh_cor_an}, about €{hh_cor_md}bn); other presentations count the State's balancing contributions as employer, and the text does not say which it uses: the verdict depends on that definition"},
    "H17": {"fr": "Exact : déficit de {hh_solde_c} % en {hh_an_c}, au-dessus de 3 % chaque année depuis 2020",
            "en": "Accurate: a deficit of {hh_solde_c}% in {hh_an_c}, above 3% every year since 2020"},
    "H18": {"fr": "Exact : {hh_solde17} % en 2017, {hh_solde24} % en 2024",
            "en": "Accurate: {hh_solde17}% in 2017, {hh_solde24}% in 2024"},
}


def hh_publie(hh, Aff=None):
    """Bloc « hors_hemicycle » du JSON et du CSV : comptes du codage, et pour chaque énoncé testé, la date, le trimestre
    publié à cette date, les données qui le jugent et (avec Aff) le verdict."""
    D, P = hh["dette"], hh["dette_pct"]
    extra = {"H04": {"dette_mdeur_2025_t2": D["2025-Q2"], "dette_pct_2025_t2": P["2025-Q2"], "dette_pct_max": hh["max_pct"]},
             "H05": {"dette_mdeur_fin2024_mai2025": hh["fin24_mai25"]["mdeur"], "dette_pct_fin2024_mai2025": hh["fin24_mai25"]["pct_pib"],
                     "dette_pct_fin2024_revisee": P["2024-Q4"]},
             "H08": {"mission_enseignement_scolaire_2026": hh["es26"], "mission_engagements_financiers_2026": hh["ef26"], "mission_defense_2026": hh["def26"],
                     "mission_enseignement_scolaire_2027": hh["es27"], "mission_engagements_financiers_2027": hh["ef27"], "mission_defense_2027": hh["def27"]},
             "H09": {"mission_enseignement_scolaire_2025": hh["es25"], "mission_engagements_financiers_2025": hh["ef25"], "mission_defense_2025": hh["def25"]},
             "H10": {"interets_apu_mdeur": hh["int_c"], "mission_enseignement_scolaire_2026": hh["es26"]},
             "H11": {"interets_apu_mdeur": hh["int_c"], "interets_apuc_2027_prevision": hh["apuc27"]},
             "H12": {"recettes_pct_2017": hh["rec17"], "recettes_pct_derniere_printemps": hh["rec_c"], "recettes_pct_derniere_octobre": hh["rec_rev_c"],
                     "solde_pct_derniere": hh["solde_c"]},
             "H13": {"manque_recettes_cumule_mdeur": hh["manque"], "dette_pct_sans_manque": hh["dette_sans_pct"]},
             "H14": {"manque_recettes_points_pib": hh["manque_pts"]},
             "H15": {"non_residents_etat_negociable_pct": hh["nr_etat"], "non_residents_apu_pct": hh["nr_apu"]},
             "H16": {"cor_besoin_pct_pib": hh["cor_pct"], "cor_besoin_mdeur": hh["cor_mdeur"]}}
    extra["H10"].update({"mission_engagements_financiers_2026": hh["ef26"]})
    out = []
    for k, e in hh["enonces"].items():
        d = {"dette_mdeur": D.get(hh["q"][k]), "hausse_depuis_election_2017": hh["h_elec"][k], "hausse_depuis_janvier_2017": hh["h_jan"][k],
             "points_pib_depuis_fin_2017": hh["pts_17"][k], **extra.get(k, {})}
        x = {kk: e[kk] for kk in ("id", "nom", "document", "url", "sha256_piece", "date_reference", "citation", "citation_en", "annonce")}
        x["trimestre_publie_a_la_date"] = hh["q"][k]
        x["donnees_a_la_date"] = {kk: round(v, 2) for kk, v in d.items() if v is not None}
        if Aff:
            x["verdict"], x["verdict_en"] = Aff["fr"]["hh_v_" + k], Aff["en"]["hh_v_" + k]
        out.append(x)
    return {"corpus": hh["corpus"], "accord": hh["accord"], "unites_arbitrees": hh["unites_arbitrees"], "temoin": hh["temoin"],
            "registres": hh["registres"], "enonces_testes": out, "testables": hh["testables"]}


# ------------------------------------------------------------------ la grille (figure signature)
# Une ligne par formule : la question que la formule pose, le verdict sur cette question, la question voisine qui change
# le verdict, et ce que vaut la conclusion qu'on en tire. Aucune case « vrai » ou « faux ».
NIVEAUX = {"fr": {"mesurer": "MESURER", "expliquer": "EXPLIQUER", "conclure": "CONCLURE"},
           "en": {"mesurer": "MEASURING", "expliquer": "EXPLAINING", "conclure": "CONCLUDING"}}

LIGNES = [
    ("mesurer", "F1", {
        "fr": ("« Pas de budget en équilibre depuis cinquante et un ans »", "F. Bayrou",
               "Exact pour les administrations publiques : dernier excédent en {f1_an} ({f1_exc} Md€), déficit chaque année depuis {f1_an1}",
               "Hors intérêts, le solde a été positif {f1_prim_l} ans ({f1_prim})", "Constat, pas d'inférence"),
        "en": ("“No balanced budget for fifty-one years”", "F. Bayrou",
               "Accurate for general government: last surplus in {f1_an} (€{f1_exc}bn), a deficit every year since {f1_an1}",
               "Excluding interest, the balance was positive for {f1_prim_l} years ({f1_prim})", "A finding, no inference")}),
    ("mesurer", "F2", {
        "fr": ("« Un euro de déficit, c'est un euro de dette »", "F. Bayrou",
               "Inexact année par année : écart de plus de 20 % du déficit {f2_sup} années sur {f2_n} (ajustements entre flux et stock)",
               "Cumul {f2_an0}-{f2_an1} : {f2_def} contre {f2_var} Md€, proche", "Constat, pas d'inférence"),
        "en": ("“A euro of deficit is a euro of extra debt”", "F. Bayrou",
               "Not year by year: the gap exceeds 20% of the deficit in {f2_sup} years out of {f2_n} (stock-flow adjustments)",
               "Cumulated {f2_an0}–{f2_an1}: €{f2_def}bn against €{f2_var}bn, close", "A finding, no inference")}),
    ("mesurer", "F16", {
        "fr": ("« 3 % de déficit, seuil à partir duquel la dette n'augmente plus »", "F. Bayrou",
               "En euros, inexact : un déficit de 3 % emprunte environ {f16_eur} Md€ par an",
               "En % du PIB, exact si la croissance nominale dépasse environ {f16_seuil24} % : {f16_g24} % en 2024, {f16_g25} % en 2025 (connu après)", "Condition décisive non dite"),
        "en": ("“A 3% deficit, the threshold at which debt stops rising”", "F. Bayrou",
               "In euros, inaccurate: a 3% deficit borrows about €{f16_eur}bn a year",
               "As a share of GDP, accurate if nominal growth exceeds about {f16_seuil24}%: {f16_g24}% in 2024, {f16_g25}% in 2025 (known later)", "Decisive condition left unsaid")}),
    ("mesurer", "F8", {
        "fr": ("« La France s'endette à des taux supérieurs à ceux de la Grèce »", "L. Wauquiez",
               "Exact le jour même : {f8_tec8} % contre {f8_hdat8} % le 8 septembre 2025 (sources des deux banques centrales)",
               "Moyenne 2025 : écarts à l'Allemagne quasi égaux ; Grèce au-dessus {f8_dessous}", "Jugement de risque, non établi"),
        "en": ("“France borrows at higher rates than Greece”", "L. Wauquiez",
               "Accurate on the day: {f8_tec8}% against {f8_hdat8}% on 8 September 2025 (both central banks' sources)",
               "2025 average: near-equal spreads over Germany; Greece above from {f8_dessous}", "Risk judgement, not established")}),
    ("mesurer", "F6", {
        "fr": ("« Dépenses restées stables depuis 2017 ; c'est la baisse des recettes »", "C. Chatelain",
               "Exact sur 2017-2024 : dépenses {f6d_dep} pt de PIB, recettes {f6d_rec} pts (comptes de mai 2025)",
               "Depuis 2019 : dépenses {f6d_dep19} pt", "Comptable : étayé ; causal : non établi"),
        "en": ("“Spending stable since 2017; it is falling revenue”", "C. Chatelain",
               "Accurate for 2017–2024: spending {f6d_dep} pt of GDP, revenue {f6d_rec} pts (May 2025 accounts)",
               "Since 2019: spending {f6d_dep19} pt", "Accounting: supported; causal: not established")}),
    ("mesurer", "F14b", {
        "fr": ("« 66 milliards en 2026 » contre « 75 milliards en 2026 »", "É. Ciotti, F. Bayrou",
               "75 : compatible avec la trajectoire de la Cour ; 66 : aucune prévision 2026 retrouvée",
               "66 égale le chiffre officiel de 2025 : un écho, pas une filiation prouvée", "Pas d'inférence"),
        "en": ("“€66bn in 2026” against “€75bn in 2026”", "É. Ciotti, F. Bayrou",
               "75: consistent with the Court of Audit path; 66: no 2026 forecast found",
               "66 equals the official 2025 figure: an echo, not a proven borrowing", "No inference")}),
    ("expliquer", "F3", {
        "fr": ("« 50 milliards créés, plus de 100 versés aux créanciers, le double »", "F. Bayrou",
               "Intérêts exacts : prévus par la Cour, {f3_25} Md€ en 2025, {f3_29} en 2029",
               "Années alignées : surcroît de 2029 de {f3_s29_bas} à {f3_s29_haut} Md€ ; ce n'est plus le double, mais {f3_r_bas} à {f3_r_haut} fois", "« Entièrement reversé » : non établi"),
        "en": ("“€50bn created, over €100bn paid to creditors, double”", "F. Bayrou",
               "Interest accurate: projected by the Court, €{f3_25}bn in 2025, €{f3_29}bn in 2029",
               "Same year: extra output in 2029 of €{f3_s29_bas}–{f3_s29_haut}bn; no longer double, but {f3_r_bas} to {f3_r_haut} times", "“Entirely handed over”: not established")}),
    ("expliquer", "F12", {
        "fr": ("« Plus de 1 000 milliards de dette en plus » depuis 2017", "B. Vallaud, M. Panot",
               "Exact sous toutes les variantes testées : de {f12d_elec} à {f12d_jan} Md€",
               "« Nous ont coûté » : mesurer n'est pas attribuer", "Attribution : non établie"),
        "en": ("“Over €1,000bn of extra debt” since 2017", "B. Vallaud, M. Panot",
               "Accurate under every variant tested: €{f12d_elec}bn to €{f12d_jan}bn",
               "“Cost us”: measuring is not attributing", "Attribution: not established")}),
    ("expliquer", "F13", {
        "fr": ("« 1 200 milliards depuis 2017, après 400 sous François Hollande »", "É. Ciotti",
               "400 : exact ({f12d_hol}) ; 1 200 : de justesse depuis janvier 2017 ({f12d_jan}), pas depuis l'élection ({f12d_elec})",
               "Par an en points de PIB : {f13_pts_mac} contre {f13_pts_hol}", "Imputation à un mandat : non établie"),
        "en": ("“€1,200bn since 2017, after 400 under François Hollande”", "É. Ciotti",
               "400: accurate ({f12d_hol}); 1,200: only just, from January 2017 ({f12d_jan}), not from the election ({f12d_elec})",
               "Per year in GDP points: {f13_pts_mac} against {f13_pts_hol}", "Attribution to a term: not established")}),
    ("conclure", "F4", {
        "fr": ("« Bientôt plus pour les intérêts que pour former nos enfants »", "L. Wauquiez",
               "Administrations : {f4_r} % en {f4_an}, pas avant 2029 ; État : {f4_r_etat} % en 2025",
               "Plafonds de l'État pour 2026 : {f4_r26} % (mission qui inclut d'autres dépenses)", "Pour l'État, étayé, non décisif"),
        "en": ("“Soon more on interest than on educating our children”", "L. Wauquiez",
               "General government: {f4_r}% in {f4_an}, not before 2029; State: {f4_r_etat}% in 2025",
               "State ceilings for 2026: {f4_r26}% (programme including other spending)", "For the State, supported, not decisive")}),
    ("conclure", "F5", {
        "fr": ("« La charge laissée à nos enfants augmente de 18 millions par heure »", "P. Christophe",
               "Sous-estimé pour la dette : {f5_hausse} millions par heure",
               "Proche du déficit prévu pour 2025 : environ {f5_prevu}", "Question distributive : non établi"),
        "en": ("“The burden left to our children grows by €18m an hour”", "P. Christophe",
               "Understated for debt: €{f5_hausse}m an hour",
               "Close to the 2025 planned deficit: about {f5_prevu}", "A distributional question: not established")}),
]

TXT_G = {
    "fr": dict(titre="Onze formules du 8 septembre 2025 : ce que les chiffres tranchent, et ce qu'ils ne tranchent pas",
               titre_m="Onze formules du 8 septembre 2025 : ce que les chiffres tranchent",
               col=("La formule (orateur)", "Sur la question qu'elle pose", "Si l'on pose une autre question", "La conclusion qu'on en tire"),
               source="Assemblée nationale (compte rendu du 8 septembre 2025) ; Insee ; Eurostat ; Cour des comptes ; Gouvernement ; Sénat ; Banque de France ; Banque de Grèce ; calcul de l'auteur",
               note="Données disponibles au 8 septembre 2025 : comptes publics tels que publiés à cette date pour les dépenses, les recettes et la dette, version révisée ailleurs ; prévisions publiées après la séance exclues des verdicts. Nombres ronds jugés à la précision annoncée (grille de tolérances). Une étude de cas d'une séance, pas un échantillon du débat.",
               montre="Pour la plupart des formules, le verdict dépend de la question posée : la date, l'unité, le périmètre ou l'année choisis. Aucune des conclusions tirées n'est démontrée par le chiffre."),
    "en": dict(titre="Eleven claims from 8 September 2025: what the figures settle, and what they do not",
               titre_m="Eleven claims from 8 September 2025: what the figures settle",
               col=("The claim (speaker)", "On the question it asks", "If another question is asked", "The conclusion drawn from it"),
               source="French National Assembly (record of 8 September 2025); Insee; Eurostat; Court of Audit; Government; Senate; Banque de France; Bank of Greece; author's calculation",
               note="Data available on 8 September 2025: public accounts as published at that date for spending, revenue and debt, revised version elsewhere; forecasts published after the debate are excluded from the verdicts. Round numbers judged at the stated precision (tolerance grid). A case study of one debate, not a sample of the debate.",
               montre="For most claims, the verdict depends on the question asked: the date, unit, scope or year chosen. None of the conclusions drawn is demonstrated by the figure."),
}


def lignes_txt(Aff, lang):
    return [(niv, fid, tuple(x.format(**Aff) for x in t[lang])) for niv, fid, t in LIGNES]


def desc_grille(Aff, lang):
    parts = []
    for niv, fid, (f, o, v, a, cc) in lignes_txt(Aff, lang):
        parts.append("%s (%s) : %s. %s. %s." % (f, o, v, a, cc) if lang == "fr" else "%s (%s): %s. %s. %s." % (f, o, v, a, cc))
    intro = ("Séance de l'Assemblée nationale du 8 septembre 2025, onze formules, groupées en trois niveaux (mesurer, expliquer, conclure)."
             if lang == "fr" else "French National Assembly, debate of 8 September 2025, eleven claims in three groups (measuring, explaining, concluding).")
    return intro + " " + " ".join(parts)


def fig_grille(Aff, lang):
    t = TXT_G[lang]
    L = lignes_txt(Aff, lang)
    xs = (0, 186, 372, 560)
    larg = (178, 178, 180, 160)
    car = lambda w: int(w / 5.3)
    e = []
    y = 40
    corps = []
    corps.append('<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"])))
    for k, col in enumerate(t["col"]):
        corps.append('<text x="%d" y="%d" font-size="10.5" font-weight="600" fill="%s">%s</text>' % (xs[k], y, INK2, esc(col)))
    y += 8
    niv_prec = None
    for niv, fid, cells in L:
        if niv != niv_prec:
            y += 10
            corps.append('<rect x="0" y="%d" width="%d" height="18" fill="%s"/>' % (y, W, FOND_NIVEAU))
            corps.append('<text x="6" y="%d" font-size="10" font-weight="600" letter-spacing="0.6" fill="%s">%s</text>' % (y + 13, BLEU, NIVEAUX[lang][niv]))
            y += 24
            niv_prec = niv
        f, o, v, a, cc = cells
        blocs = [pied_figure.coupe(f, car(larg[0])) + [o], pied_figure.coupe(v, car(larg[1])), pied_figure.coupe(a, car(larg[2])), pied_figure.coupe(cc, car(larg[3]))]
        hl = max(len(b) for b in blocs)
        for k, b in enumerate(blocs):
            for i, l in enumerate(b):
                poids, coul = "", INK
                if k == 0 and i == len(b) - 1:
                    coul = INK2
                elif k == 0:
                    poids = ' font-weight="600"'
                elif k == 2:
                    coul = INK2
                elif k == 3:
                    coul = ORANGE
                corps.append('<text x="%d" y="%d" font-size="10.5"%s fill="%s">%s</text>' % (xs[k], y + 12 + 13 * i, poids, coul, esc(l)))
        y += 13 * hl + 8
        corps.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.6"/>' % (y, W, y, GRID))
    h = y + 6
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="form-t form-d" font-family="%s">' % (W, h, FONT),
         '<title id="form-t">%s</title><desc id="form-d">%s</desc>' % (esc(t["titre"]), esc(desc_grille(Aff, lang))),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h)] + corps
    return pied_figure.pied(e, h, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                     (LICENCES[lang], MUTED, "pied-licence")], GRID)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_grille_m(Aff, lang, svg_d):
    t = TXT_G[lang]
    e, y = pied_figure.tete_mobile("formm", t["titre_m"], desc_de(svg_d), INK, FONT)
    niv_prec = None
    lab = {"fr": ("Question posée : ", "Autre question : ", "Conclusion : "), "en": ("Question asked: ", "Other question: ", "Conclusion: ")}[lang]
    for niv, fid, (f, o, v, a, cc) in lignes_txt(Aff, lang):
        if niv != niv_prec:
            y += 18
            e.append('<rect x="0" y="%d" width="%d" height="22" fill="%s"/>' % (y, WM, FOND_NIVEAU))
            e.append('<text x="6" y="%d" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y + 16, FS_MIN, BLEU, NIVEAUX[lang][niv]))
            y += 26
            niv_prec = niv
        y += 8
        for l in pied_figure.coupe(f, 34):
            y += 18
            e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(l)))
        y += 17
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(o)))
        for pre, txt, coul in ((lab[0], v, INK), (lab[1], a, INK2), (lab[2], cc, ORANGE)):
            for i, l in enumerate(pied_figure.coupe(pre + txt, 38)):
                y += 17
                e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, coul, esc(l)))
        y += 6
        e.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.6"/>' % (y, WM, y, GRID))
    return pied_figure.pied_mobile(e, y + 10, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


# ------------------------------------------------------------------ figure F8 : écart France - Grèce, mensuel
TXT_E = {
    "fr": dict(titre="Taux à dix ans : la France au-dessus ou au-dessous de la Grèce, mois par mois",
               titre_m="Taux à dix ans : la France moins la Grèce, mois par mois",
               axe="écart France − Grèce, en point de pourcentage", axe_m="France − Grèce, en point",
               desc="Barres mensuelles de janvier 2024 à {f8_dernier} de l'écart entre le rendement à dix ans de la France et celui de la Grèce : "
                    "négatif jusqu'au printemps 2025, positif à partir de {f8_premier} ; août 2025 {f8_aout_fr} contre {f8_aout_el} %, "
                    "septembre 2025 {f8_sept_fr} contre {f8_sept_el} % ; Grèce de nouveau au-dessus {f8_dessous} ; {f8_dernier} : +{f8_ecart_dernier} point.",
               seance="séance du 8 septembre 2025", dessus="France au-dessus", dessous="Grèce au-dessus",
               source="Eurostat, rendements des emprunts d'État à long terme, moyennes mensuelles (irt_lt_mcby_m) ; calcul de l'auteur",
               note="Moyennes mensuelles. Le 8 septembre 2025, la France empruntait à dix ans à {f8_tec8} % (Banque de France) et la Grèce à {f8_hdat8} % (Banque de Grèce) ; le 4, la même mesure pour les deux pays donnait {f8_j4_fr} % contre {f8_j4_gr} %. Un prix de marché dit le coût d'emprunt du moment, pas la solidité relative de deux pays.",
               montre="La France emprunte plus cher que la Grèce à partir de l'été 2025 : la formule est exacte au mois de la séance, et elle n'aurait pas été exacte six mois plus tôt."),
    "en": dict(titre="Ten-year yields: France above or below Greece, month by month",
               titre_m="Ten-year yields: France minus Greece, month by month",
               axe="France − Greece spread, percentage points", axe_m="France − Greece, points",
               desc="Monthly bars from January 2024 to {f8_dernier} of the gap between the ten-year yield of France and that of Greece: "
                    "negative until spring 2025, positive from {f8_premier}; August 2025 {f8_aout_fr} against {f8_aout_el}%, "
                    "September 2025 {f8_sept_fr} against {f8_sept_el}%; Greece above again from {f8_dessous}; {f8_dernier}: +{f8_ecart_dernier} point.",
               seance="debate of 8 September 2025", dessus="France above", dessous="Greece above",
               source="Eurostat, long-term government bond yields, monthly averages (irt_lt_mcby_m); author's calculation",
               note="Monthly averages. On 8 September 2025, France borrowed at ten years at {f8_tec8}% (Banque de France) and Greece at {f8_hdat8}% (Bank of Greece); on the 4th, a like-for-like measure gave {f8_j4_fr}% against {f8_j4_gr}%. A market price gives the current cost of borrowing, not the relative soundness of two countries.",
               montre="France borrows at higher rates than Greece from summer 2025: the claim is accurate for the month of the debate, and would not have been six months earlier."),
}


def fig_grece(c, Aff, lang):
    t = {k: v.format(**Aff) for k, v in TXT_E[lang].items()}
    f8 = c["F8"]
    mois = f8["mois"]
    h = 300
    X0, X1, TOP, BAS = 46, 708, 52, 262
    vmin, vmax = -0.7, 0.3
    n = len(mois)
    bw = (X1 - X0) / n
    X = lambda i: X0 + bw * i
    Y = lambda v: TOP + (BAS - TOP) * (vmax - v) / (vmax - vmin)
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="grec-t grec-d" font-family="%s">' % (W, h + 40, FONT),
         '<title id="grec-t">%s</title><desc id="grec-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 40),
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"])),
         '<text x="%d" y="%d" font-size="10" fill="%s">%s</text>' % (X0, TOP - 14, MUTED, esc(t["axe"]))]
    for gv in (-0.6, -0.4, -0.2, 0, 0.2):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(gv), X1, Y(gv), INK2 if gv == 0 else GRID, 1.2 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(gv) + 3, MUTED, nb(gv, 1, lang).replace("-", "−")))
    i_s = mois.index("2025-09")
    for i, m in enumerate(mois):
        v = f8["ecart"][m]
        y0, y1 = sorted((Y(0), Y(v)))
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (X(i) + 1.5, y0, bw - 3, max(y1 - y0, 0.8), ORANGE if v > 0 else GRIS_CLAIR))
        if m.endswith("-01"):
            e.append('<text x="%.1f" y="%d" font-size="10" fill="%s">%s</text>' % (X(i) + 1.5, BAS + 16, MUTED, m[:4]))
    xs = X(i_s) + bw / 2
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % (xs, TOP - 4, xs, BAS, INK))
    e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (xs, TOP - 6 + 0, INK, esc(t["seance"])))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (xs - 8, Y(0.2), ORANGE, esc(t["dessus"])))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s">%s</text>' % (X(mois.index("2025-01")), Y(-0.45), INK2, esc(t["dessous"])))
    return pied_figure.pied(e, h + 2, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


def fig_grece_m(c, Aff, lang, svg_d):
    t = {k: v.format(**Aff) for k, v in TXT_E[lang].items()}
    f8 = c["F8"]
    mois = f8["mois"]
    e, y = pied_figure.tete_mobile("grecm", t["titre_m"], desc_de(svg_d), INK, FONT)
    X0, X1, TOP = 34, WM - 2, y + 34
    BAS = TOP + 190
    vmin, vmax = -0.7, 0.3
    bw = (X1 - X0) / len(mois)
    X = lambda i: X0 + bw * i
    Y = lambda v: TOP + (BAS - TOP) * (vmax - v) / (vmax - vmin)
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (TOP - 14, FS_MIN, MUTED, esc(t["axe_m"])))
    for gv in (-0.6, -0.3, 0, 0.3):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(gv), X1, Y(gv), INK2 if gv == 0 else GRID, 1.2 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%s</text>' % (X0 - 4, Y(gv) + 4, FS_MIN, MUTED, nb(gv, 1, lang).replace("-", "−")))
    for i, m in enumerate(mois):
        v = f8["ecart"][m]
        y0, y1 = sorted((Y(0), Y(v)))
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (X(i) + 0.8, y0, bw - 1.6, max(y1 - y0, 0.8), ORANGE if v > 0 else GRIS_CLAIR))
    for a in ("2024", "2025", "2026"):
        i = mois.index(a + "-01")
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s">%s</text>' % (X(i), BAS + 18, FS_MIN, MUTED, a))
    i_s = mois.index("2025-09")
    xs = X(i_s) + bw / 2
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % (xs, TOP - 2, xs, BAS, INK))
    y = BAS + 30
    sep = " : " if lang == "fr" else ": "
    lignes = [((("Août 2025" if lang == "fr" else "August 2025") + sep + "%s / %s %%") % (Aff["f8_aout_fr"], Aff["f8_aout_el"]), ORANGE),
              ((("Septembre 2025" if lang == "fr" else "September 2025") + sep + "%s / %s %%") % (Aff["f8_sept_fr"], Aff["f8_sept_el"]), ORANGE)]
    for lib, col in lignes:
        y += 20
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, col, esc(lib)))
    for l in pied_figure.coupe(("France / Grèce, moyenne du mois ; ligne pointillée : la séance" if lang == "fr"
                                else "France / Greece, monthly average; dotted line: the debate"), 38):
        y += 18
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    return pied_figure.pied_mobile(e, y + 14, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fiches(figs, Aff):
    out = {}
    for lang in ("fr", "en"):
        out[lang] = []
        for id_, base, txt in (("grille", "dette-formules-grille", TXT_G), ("grece", "dette-formules-grece", TXT_E)):
            f = base + SUFFIXE[lang]
            svg = figs[f + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            out[lang].append(dict(id=id_, fichier=f, titre=titre, montre=txt[lang]["montre"].format(**Aff[lang]),
                                  source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note")))
    return out


def csv_texte(c):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "variable", "cle", "valeur", "unite"])
    for a in sorted(c["F1"]["solde_mdeur"]):
        w.writerow(["F1_solde_apu", "capacite_besoin_financement", a, "%.3f" % c["F1"]["solde_mdeur"][a], "Md EUR courants"])
        w.writerow(["F1_solde_apu", "capacite_besoin_financement", a, "%.1f" % c["F1"]["solde_pct"][a], "% du PIB"])
    for x in c["F2"]["annees"]:
        for k in ("deficit", "var_dette", "ecart"):
            w.writerow(["F2_deficit_et_dette", k, x["annee"], "%.1f" % x[k], "Md EUR courants"])
    for k, v in c["F16"].items():
        w.writerow(["F16_seuil_3pct", k, "", "%.3f" % v, "% ou Md EUR"])
    for m in c["F8"]["mois"]:
        for g, k in (("FR", "fr"), ("EL", "el"), ("DE", "de")):
            w.writerow(["F8_taux_10_ans_mensuels", g, m, "%.3f" % c["F8"][k][m], "%"])
    for d, v in sorted(c["F8"]["bog"].items()):
        for g, r in v.items():
            w.writerow(["F8_taux_10_ans_jour_banque_de_grece", g, d, "%.2f" % r, "%"])
    for d, r in sorted(c["F8"]["tec10"].items()):
        w.writerow(["F8_tec10_banque_de_france", "FR", d, "%.2f" % r, "%"])
    for fen, v in c["F6"].items():
        for k, x in v.items():
            w.writerow(["F6_fenetres", k, fen, "%.1f" % x, "points de PIB"])
    for fen, v in c["F6d"].items():
        for k, x in v.items():
            w.writerow(["F6_fenetres_comptes_mai_2025", k, fen, "%.1f" % x, "points de PIB"])
    for k, v in c["F12d"].items():
        w.writerow(["F12_F13_hausse_dette_au_8_septembre_2025", k, "", "%.1f" % v, "Md EUR"])
    for k, v in c["F12"].items():
        w.writerow(["F12_F13_hausse_dette", k, "", "%.1f" % v, "Md EUR ou points de PIB"])
    for k, v in c["F5"].items():
        w.writerow(["F5_par_heure", k, "", "%.1f" % v, "M EUR par heure"])
    for k, v in c["F4"].items():
        w.writerow(["F4_interets_enseignement", k, "", "%.1f" % v, "Md EUR ou %"])
    for k, v in c["F3"].items():
        if isinstance(v, dict):
            for a, x in v.items():
                w.writerow(["F3_cour_des_comptes", k, a, "%.1f" % x, "Md EUR ou points de PIB"])
        else:
            w.writerow(["F3_cour_des_comptes", k, "", "%.1f" % v, "Md EUR"])
    for k, v in c["F14"].items():
        w.writerow(["F14_previsions_2026", k, "", "%.1f" % v, "Md EUR ou %"])
    for k, v in c["INV"].items():
        w.writerow(["inventaire_seance", k, "", "%s-%s" % v if isinstance(v, tuple) else v, "enonces"])
    hp = hh_publie(c["HH"])
    for cand, regs in sorted(hp["registres"].items()):
        for r, n in regs.items():
            w.writerow(["hors_hemicycle_registres", r, cand, n, "enonces"])
    for e in hp["enonces_testes"]:
        for k, v in e["donnees_a_la_date"].items():
            w.writerow(["hors_hemicycle_tests", k, e["id"], "%.2f" % v, "Md EUR, % du PIB ou points"])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    off, dyn, taux, solde, inv, doc, eu_maj, hh, gen = lire()
    c = calcul(off, dyn, taux, solde, inv, doc)
    c["HH"] = calcul_hh(off, dyn, solde, doc, hh, gen)
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, lang) for lang in ("fr", "en")}
    if set(Aff["fr"]) != set(Aff["en"]):
        fail("blocs affichage et affichage_en : cles differentes")
    figs = {}
    for lang in ("fr", "en"):
        sf = SUFFIXE[lang]
        figs["dette-formules-grille%s.svg" % sf] = fig_grille(Aff[lang], lang)
        figs["dette-formules-grece%s.svg" % sf] = fig_grece(c, Aff[lang], lang)
        figs["dette-formules-grille%s-m.svg" % sf] = fig_grille_m(Aff[lang], lang, figs["dette-formules-grille%s.svg" % sf])
        figs["dette-formules-grece%s-m.svg" % sf] = fig_grece_m(c, Aff[lang], lang, figs["dette-formules-grece%s.svg" % sf])
        for fid, coul in (("grille", (ORANGE,)), ("grece", (ORANGE,))):
            ec = pied_figure.parite(figs["dette-formules-%s%s.svg" % (fid, sf)], figs["dette-formules-%s%s-m.svg" % (fid, sf)], FS_MIN, coul)
            if ec:
                fail("parite mobile %s %s : %s" % (fid, lang, " ; ".join(ec)))
    pages = [(p, sf) for p, sf in (("_index.md", ""), ("_index.en.md", "-en")) if (PAGE_DIR / p).exists()]
    for page, sf in pages:
        ec = pied_figure.controler_page((PAGE_DIR / page).read_text(encoding="utf-8"),
                                        {f: v for f, v in figs.items() if re.fullmatch(r"dette-formules-[a-z]+%s(-m)?\.svg" % sf, f)})
        if ec:
            fail("page %s : %s" % (page, " ; ".join(ec)))
    log("F1 %s ; F8 4/9 %s/%s ; F12 %.0f-%.0f ; F16 g=%.2f seuil %.2f ; inventaire tech %s neg %s"
        % (c["F1"]["dernier_excedent"], Aff["fr"]["f8_j4_fr"], Aff["fr"]["f8_j4_gr"], c["F12"]["h_election"], c["F12"]["h_janvier"],
           c["F16"]["g25"], c["F16"]["g_seuil"], Aff["fr"]["inv_tech"], Aff["fr"]["inv_neg"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), parite des 4 figures telephone et hauteurs de %d page(s) controlees, rien ecrit."
            % (n, len(Aff["fr"]), len(pages)))
        return 0
    import cairosvg
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "objet": "onze formules chiffrées de la séance de l'Assemblée nationale du 8 septembre 2025, confrontées aux séries officielles",
                        "millesime": c["millesime"], "eurostat_maj": eu_maj,
                        "transcrit": "valeurs documentaires transcrites de documents publiés, avec page, extrait et empreinte de la pièce archivée (scripts/sources_dette_formules/documentaires.json)"},
               "formules": [{"id": fid, "niveau": niv, "texte": t["fr"][0], "orateur": t["fr"][1], "question_posee": t["fr"][2].format(**Aff["fr"]),
                             "autre_question": t["fr"][3].format(**Aff["fr"]), "conclusion": t["fr"][4]} for niv, fid, t in LIGNES],
               "enonces_seance": c["seance"],
               "F1": {"dernier_excedent": c["F1"]["dernier_excedent"], "excedent_mdeur": c["F1"]["excedent_mdeur"], "primaire_positif": c["F1"]["primaire_positif"]},
               "F2": {k: v for k, v in c["F2"].items()},
               "F16": {k: round(v, 3) for k, v in c["F16"].items()},
               "F8": {"ecart_france_grece_mensuel": c["F8"]["ecart"], "jour_banque_de_grece": c["F8"]["bog"], "tec10_banque_de_france": c["F8"]["tec10"],
                      "fr_moins_de_2025": round(c["F8"]["fr_de_2025"], 3), "el_moins_de_2025": round(c["F8"]["el_de_2025"], 3)},
               "F6": c["F6"], "F6_comptes_mai_2025": c["F6d"], "F12_F13_au_8_septembre_2025": {k: round(v, 1) for k, v in c["F12d"].items()}, "F12_F13": {k: round(v, 1) for k, v in c["F12"].items()}, "F5": {k: round(v, 1) for k, v in c["F5"].items()},
               "F4": {k: round(v, 1) if isinstance(v, float) else v for k, v in c["F4"].items()},
               "F3": {k: (round(v, 1) if isinstance(v, float) else v) for k, v in c["F3"].items()},
               "F14": {k: round(v, 1) if isinstance(v, float) else v for k, v in c["F14"].items()},
               "inventaire": {k: list(v) if isinstance(v, tuple) else v for k, v in c["INV"].items()},
               "hors_hemicycle": hh_publie(c["HH"], Aff),
               "affichage": Aff["fr"], "affichage_en": Aff["en"]}
    payload = json.loads(json.dumps(payload, ensure_ascii=False))
    releve = None
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            rj.sans_licence(prev, LICENCE)
            same = {k: v for k, v in prev.items() if k != "releve_le"} == payload
            if same and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c) \
                    and OUT_FIGURES.exists() \
                    and OUT_FIGURES.read_text(encoding="utf-8") == json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n":
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
            if same or rj.releve(OUT_DATA, payload, "") == prev["releve_le"]:
                releve = prev["releve_le"]
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve or datetime.now(timezone.utc).strftime("%Y-%m-%d"), "_licence": LICENCE, **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dette_formules.json, static/dette_formules.csv, data/figures_dette_formules.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
