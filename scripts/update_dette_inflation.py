#!/usr/bin/env python3
"""update_dette_inflation.py -- prolongement « L'inflation a-t-elle vraiment allégé la dette française ? » (dossier dette).

Découverte de la page (dépôt de recherche de l'auteur, chantier inflation et dette, V3 du 07/10/2026, arbitrage
PRO-20261007-091811) : l'écart entre l'inflation réalisée en 2021-2023 et celle anticipée début 2021 réduit d'environ
150 Md€ de 2020 le pouvoir d'achat des flux promis sur la dette négociable de l'État à taux fixe de fin 2020 ; cette
érosion se mesure bien, mais elle ne se convertit pas en un gain budgétaire net identifiable.

Entrée : l'extrait FIGÉ de la recherche, scripts/sources_inflation_dette/ (v3_resultats.json, choc_ferme_sensibilites.csv,
cout_indexes.json), contrôlé contre ses empreintes SHA256SUMS. Le calcul vit dans le dépôt de recherche (scripts/v3.py) ;
ce générateur ne recalcule rien, il met en forme et GARDE : chaque qualificatif de la prose est une condition sur les
nombres (fonction gardes) ; si l'extrait la dément, arrêt. Mise à jour à la main, comme generer_figures_qui_paie.py :
les données sont celles d'un épisode clos (2021-2023), non une série vivante.
Témoins de la méthode, dans le script de recherche : IPCH mensuel Eurostat contre le relevé Insee (36 mois) ; même calcul
en moyennes annuelles (v2, 143,2) et sans correction saisonnière ; identité de consolidation contre l'arbitre 5. Ici, la
seule cohérence vérifiée est l'agrégation par année de paiement, qui partage la fonction de perte : elle n'est pas un témoin.

Section « achats de la banque centrale » (09/10/2026) : extrait FIGÉ du chantier « QE et maturité consolidée » (dépôt de
recherche, VERDICT.md, phrases P1 à P4, contre-expertise PRO-20261008-194156 arbitrée), scripts/sources_qe_maturite/,
contrôlé contre son SHA256SUMS. Mêmes règles : rien recalculé hors de sommes et de rapports, chaque qualificatif gardé.
Témoins publiés que le calcul n'utilise pas : figure 1.16 de l'OCDE (SBO 2023) mesurée au pixel ; « jusqu'à deux ans »
de la Bundesbank (avril 2024) ; comptes de la Banque de France (résultat ordinaire, versements à l'État).

Usage : python scripts/update_dette_inflation.py [--check]
        [--mutation=demi|indexes|consolidation|encadre|qe_cinq|qe_partage|qe_ocde|qe_bdf|fonds]
Sorties : data/ et static/dette_inflation.json, static/dette_inflation.csv, data/figures_inflation.json,
          static/img/dette-inflation-{calendrier,achats}{,-en}{,-m}.svg + .png (versions téléphone -m : refonte du 11/10/2026)
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

import pied_figure  # pied commun, version téléphone, parité (scripts/pied_figure.py)

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_inflation_dette"
SRC_QE = ROOT / "scripts" / "sources_qe_maturite"
OUT_DATA = ROOT / "data" / "dette_inflation.json"
OUT_STATIC = ROOT / "static" / "dette_inflation.json"
OUT_CSV = ROOT / "static" / "dette_inflation.csv"
OUT_FIGURES = ROOT / "data" / "figures_inflation.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/inflation-et-dette-publique/"
PAGE_URL_EN = "stephane-lalut.com/en/inflation-and-french-public-debt/"

W = 720
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCES = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Computed by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
SUFFIXE = {"fr": "", "en": "-en"}
LICENCES_M = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com", "en": "Computed by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def nb(v: float, dec: int, lang: str) -> str:
    s = ("%." + str(dec) + "f") % v
    return s.replace(".", ",") if lang == "fr" else s


def arr5(v: float) -> int:
    return int(5 * round(v / 5))


# ------------------------------------------------------------------ données
def lire():
    sums = {}
    for ligne in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        h, nom_ = ligne.split()
        sums[nom_.lstrip("*")] = h
    for nom_, h in sums.items():
        if hashlib.sha256((SRC / nom_).read_bytes()).hexdigest() != h:
            fail("empreinte de %s differente de SHA256SUMS : extrait modifie hors du depot de recherche" % nom_)
    v3 = json.loads((SRC / "v3_resultats.json").read_text(encoding="utf-8"))
    sens = {r["parametre"]: float(r["transfert_stock2020_mdeur"]) for r in csv.DictReader((SRC / "choc_ferme_sensibilites.csv").open(encoding="utf-8"))}
    ci = json.loads((SRC / "cout_indexes.json").read_text(encoding="utf-8"))
    ci["_parts_2020T4"] = json.loads((SRC / "t5_resultats.json").read_text(encoding="utf-8"))["T1_parts_2020T4_brut"]
    return v3, sens, ci


def calcul(v3, sens, ci):
    o1 = v3["op1_ipch_mensuel"]
    cum = {int(a): v for a, v in o1["cumul_realise_par_annee"].items()}
    A = v3["op2_famille_A"]
    pal = v3["op8_pallotti_residu"]["pallotti"]
    pont = dict(pal["pont_pct_pib_annuel"])
    residu = pont["Résidu jusqu'à la position de Pallotti (0,39 x 3 = 1,17 PIB)"] - pont["Date : ratio de 2017 au lieu de 2020"]
    return {
        "T": o1["transfert_central_spf_mdeur"], "T_annuel": o1["meme_calcul_moyennes_annuelles_v2_mdeur"],
        "T_sans_saison": o1["sans_correction_saisonniere_mdeur"],
        "pts_pib": o1["en_pts_pib2020"], "gap23": o1["ecart_niveau_prix_dec2023_pct"], "demi": o1["annee_demi_realisation"],
        "cum": cum,
        "A": A, "A_r0": v3["op2_plage_famille_A_r0_mdeur"], "A_tout": v3["op2_plage_publiee_famille_A_mdeur"],
        "B": v3["op2_famille_B_sensibilite"],
        "defl_spf": sens["indice de prix : déflateur du PIB (anticipation IPCH SPF)"],
        "defl_ce": sens["déflateur du PIB réalisé contre déflateur prévu (Commission, automne 2020)"],
        "idx_j": v3["op4_indexes"]["transfert_renonce_paires_jumelles_mdeur"],
        "idx_1": v3["op4_indexes"]["transfert_renonce_point_unique_1_162_mdeur"],
        "idx_tot": v3["op4_indexes"]["cout_total_paires_jumelles_mdeur"],
        "idx_ecart": v3["op4_indexes"]["ecart_indice_mdeur_repris_v2"],
        "idx_encours": ci["encours_indexe_mdeur"], "idx_n": ci["titres_indexes_fin_2020"],
        "charge_aft": {int(a): v for a, v in ci["charge_budgetaire_aft_mdeur_nominaux"].items()},
        "s_bdf": v3["op5_consolidation"]["part_BdF_fin_2020"],
        "cons23": v3["op5_consolidation"]["T_consolide_fin_2023_mdeur"],
        "cons25": v3["op5_consolidation"]["T_consolide_fin_2025_mdeur"],
        "pal_rapport": pal["rapport_eux_sur_nous_pib_annuel"], "pal_total": pont["Résidu jusqu'à la position de Pallotti (0,39 x 3 = 1,17 PIB)"],
        "pal_residu": residu,
        "parts": {k: v for k, v in ci["_parts_2020T4"].items() if k != "total_MdEUR"},
    }


def tsv(nom_):
    return list(csv.DictReader((SRC_QE / nom_).open(encoding="utf-8"), delimiter="\t"))


def lire_qe():
    for ligne in (SRC_QE / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        h, nom_ = ligne.split()
        if hashlib.sha256((SRC_QE / nom_.lstrip("*")).read_bytes()).hexdigest() != h:
            fail("empreinte de %s differente de SHA256SUMS : extrait QE modifie hors du depot de recherche" % nom_)
    return {k: tsv(k + ".tsv") for k in ("indicateurs_mensuels", "sensibilite_mensuelle", "rendement_cycle",
                                         "t4_pays_annuel", "releve_T1_T2", "mesure_figure_ocde")}


def calcul_qe(x):
    ind = {r["situation"]: r for r in x["indicateurs_mensuels"]}
    sen = {r["situation"]: r for r in x["sensibilite_mensuelle"]}
    F = lambda r, k: float(r[k])
    d0, d22 = "2015-03-31", "2022-12-31"
    fen = [r for d, r in ind.items() if d0 <= d <= d22]
    emis = {}
    for r in x["indicateurs_mensuels"]:
        if r["emission_maturite"]:
            a = int(r["situation"][:4])
            s, w = emis.get(a, (0.0, 0.0))
            emis[a] = (s + F(r, "emission_MLT_Md"), w + F(r, "emission_MLT_Md") * F(r, "emission_maturite"))
    emis = {a: w / s for a, (s, w) in emis.items()}
    e1 = max((r for r in ind.values() if r["ecart_E1"]), key=lambda r: F(r, "ecart_E1"))
    dern = max(sen)
    serie = [(d, F(r, "S_m_1_Md"), F(r, "S_c_1_Md")) for d, r in sorted(sen.items())]
    # T4, base homogène BCE : rapport consolidée / marché à un an = r1 / F1, par pays et par année
    t4 = {}
    for r in x["t4_pays_annuel"]:
        t4.setdefault(r["pays"], {})[int(r["annee"])] = F(r, "r1") / F(r, "F1")
    # bloc 3 : portage net C (M€), soldes de partage publiés ; champ vide = non publié (ligne des titres avant 2023, quand
    # le taux de référence était nul : la recherche le compte pour zéro, convention dite dans SENSIBILITE.md, § 5)
    rc = {int(r["annee"]): r for r in x["rendement_cycle"]}
    C = {a: float(r["C_Meur"]) for a, r in rc.items() if r["C_Meur"]}
    st = {a: float(r["solde_partage_total_Meur"]) for a, r in rc.items() if r["solde_partage_total_Meur"]}
    ns = {a: float(r["solde_partage_titres_Meur"]) for a, r in rc.items() if r["solde_partage_titres_Meur"]}
    som = lambda d, lo, hi: sum(d.get(a, 0.0) for a in range(lo, hi + 1)) / 1e3
    rdt = [float(rc[a]["rendement_comptable_A71"]) for a in C]
    tref = [float(r["taux_reference_moyen"]) for r in rc.values()]
    # comptes de la Banque de France (lecture de l'institution, confrontée à son périmètre)
    bdf = {}
    for r in x["releve_T1_T2"]:
        bdf.setdefault(r["poste"], {})[int(r["annee"])] = float(r["valeur_Meur"])
    # versements à l'État = impôt (relevé en charge, négatif) + dividende ; une année non relevée fait échouer (KeyError),
    # jamais un zéro : le dividende de l'exercice 2025 n'est pas relevé, la page ne cite donc que 2015-2022
    verse = lambda lo, hi: sum(-bdf["impot_benefices"][a] + bdf["dividende_etat"][a] for a in range(lo, hi + 1)) / 1e3
    ocde = {r["pays"]: r for r in x["mesure_figure_ocde"]}
    return {
        "atr15": F(ind[d0], "ATR_fixe"), "atr22": F(ind[d22], "ATR_fixe"),
        "aj_min": min(F(r, "ATR_fixe_aj") for r in fen), "aj_max": max(F(r, "ATR_fixe_aj") for r in fen),
        "em14": emis[2014], "em_min": min(emis[a] for a in range(2016, 2023)), "em_max": max(emis[a] for a in range(2016, 2023)),
        "e1_max": F(e1, "ecart_E1"), "e1_date": e1["situation"],
        "sm1": F(sen[d22], "S_m_1_Md"), "sc1": F(sen[d22], "S_c_1_Md"), "sc1_pib": F(sen[d22], "S_c_1_pPIB"),
        "sm5": F(sen[d22], "S_m_5_Md"), "sc5": F(sen[d22], "S_c_5_Md"),
        "dern": dern, "sm1_d": F(sen[dern], "S_m_1_Md"), "sc1_d": F(sen[dern], "S_c_1_Md"), "h_d": F(sen[dern], "h"),
        "h22": F(sen[d22], "h"), "serie": serie,
        "t4_2015": {p: v[2015] for p, v in t4.items()}, "t4_max": {p: max(v.values()) for p, v in t4.items()},
        "gain": som(C, 2016, 2022), "cout": som(C, 2023, 2025), "solde": som(C, 2016, 2025),
        "net_total": som(C, 2016, 2025) + som(st, 2016, 2025), "net_titres": som(C, 2016, 2025) + som(ns, 2016, 2025),
        "rdt_min": min(rdt), "rdt_max": max(rdt), "tref_min": min(tref), "tref_max": max(tref),
        "bdf_ro_avant": sum(bdf["resultat_ordinaire_avant_impot"][a] for a in range(2015, 2023)) / 1e3,
        "bdf_ro_apres": sum(bdf["resultat_ordinaire_avant_impot"][a] for a in range(2023, 2026)) / 1e3,
        "bdf_verse_avant": verse(2015, 2022),
        "ocde_effet": float(ocde["FRA"]["ATR"]) - float(ocde["FRA"]["ATR_ajuste"]), "ocde_aj": float(ocde["FRA"]["ATR_ajuste"]),
        "nous_effet": F(ind[d22], "ATR_ocde") - F(ind[d22], "ATR_ocde_aj"),
        "C": C, "st": st, "ns": ns, "t4": t4, "rc": rc,
        "atr": [(d, F(r, "ATR_fixe"), F(r, "ATR_fixe_aj")) for d, r in sorted(ind.items()) if r["ATR_fixe_aj"]],
    }


def mutation(c):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m == "demi":            # la moitié n'est plus atteinte en 2027
        c["cum"][2027] = 0.40 * c["T"]
    elif m == "indexes":       # le contrefactuel des indexés s'éloigne de « environ 20 »
        c["idx_j"] = 27.0
    elif m == "consolidation":  # la consolidation retirerait l'érosion pendant l'épisode
        c["cons23"] = 0.8 * c["T"]
    elif m == "encadre":       # le SPF sortirait de l'intervalle des trois prévisions françaises
        list(c["A"].values())[0]["r=0%"] = 999.0
    elif m == "qe_cinq":       # à cinq ans, l'écart resterait aussi grand qu'à un an : « avancé » serait faux
        c["qe"]["sc5"] = c["qe"]["sm5"] * c["qe"]["sc1"] / c["qe"]["sm1"]
    elif m == "qe_partage":    # la redistribution entre banques centrales déplacerait le solde de plus de quelques milliards
        c["qe"]["net_total"] = c["qe"]["solde"] / 3
    elif m == "qe_ocde":       # le témoin OCDE ne retrouverait plus l'effet des achats
        c["qe"]["ocde_effet"] += 0.6
    elif m == "qe_bdf":        # la Banque de France serait restée bénéficiaire après 2023 : « puis pertes » serait faux
        c["qe"]["bdf_ro_apres"] = 5.0
    elif m == "fonds":         # « fonds et autres » dépasserait la part des banques : l'ordre dit dans la page serait faux
        c["parts"]["assureurs"] -= 5
    elif m is not None:
        fail("mutation inconnue : %s" % m)
    return m


# ------------------------------------------------------------------ gardes : chaque qualificatif de la prose
def gardes(c):
    n = 0

    def g(cond, msg):
        nonlocal n
        n += 1
        if not cond:
            fail("garde : " + msg)

    T = c["T"]
    g(abs(T - arr5(T)) <= 2.5, "« environ %d » : %.1f" % (arr5(T), T))
    # cohérence (non indépendante : même fonction de perte) : l'agrégation par année redonne le total
    g(abs(c["cum"][max(c["cum"])] - T) <= 0.15, "le cumul par année de paiement ne redonne pas le total (%.1f contre %.1f)" % (c["cum"][max(c["cum"])], T))
    g(c["A_r0"][0] <= T <= c["A_r0"][1], "le central (SPF) doit être dans la plage de la famille A")
    fr = [v["r=0%"] for v in list(c["A"].values())[1:]]  # Banque de France, Commission automne, hiver : propres à la France
    g(min(fr) < list(c["A"].values())[0]["r=0%"] < max(fr), "« les trois prévisions propres à la France encadrent » le SPF : %s" % fr)
    g(min(c["B"].values()) > T, "« les points morts de marché donneraient davantage » : %s" % c["B"])
    g(c["T"] > c["T_annuel"], "« plus élevé que le calcul en moyennes annuelles »")
    g(abs(c["T_sans_saison"] - T) < 1.0, "« la correction saisonnière ne change presque rien »")
    part27 = c["cum"][2027] / T
    g(c["demi"] == 2027 and 0.45 <= part27 <= 0.62, "« environ la moitié d'ici 2027 » : %.0f %%, demi %s" % (100 * part27, c["demi"]))
    part23 = c["cum"][2023] / T
    g(0.17 <= part23 <= 0.23, "« un cinquième seulement payé fin 2023 » : %.0f %%" % (100 * part23))
    g(47 <= c["parts"]["non_residents"] <= 53, "FAQ : « la moitié détenue par des non-résidents » : %.1f" % c["parts"]["non_residents"])
    g(21 <= c["parts"]["BdF"] < 25, "FAQ : « près d'un quart par la Banque de France » : %.1f" % c["parts"]["BdF"])
    g(c["defl_spf"] < c["T_annuel"] and c["defl_ce"] < c["T_annuel"], "« plus faible en unités de production intérieure »")
    g(abs(c["idx_j"] - 20) <= 2.5 and abs(c["idx_1"] - c["idx_j"]) <= 1.0, "« environ 20 Md€, la même chose avec un seul point mort » : %.1f / %.1f" % (c["idx_j"], c["idx_1"]))
    g(c["cons23"] >= 0.95 * T, "« consolidée, l'érosion reste presque entière fin 2023 » : %.1f" % c["cons23"])
    g(c["cons25"] < c["cons23"] - 10, "« puis l'avantage consolidé se réduit en 2024-2025 »")
    g(0.10 <= c["pal_residu"] / c["pal_total"] <= 0.16, "« résidu d'environ 13 %% » : %.3f" % (c["pal_residu"] / c["pal_total"]))
    g(c["charge_aft"][2022] == max(c["charge_aft"].values()), "« la charge d'indexation a culminé en 2022 »")
    fa = 100 - sum(v for k, v in c["parts"].items() if k != "OPC")
    g(1 < fa < 5 and fa < c["parts"]["banques"], "« fonds et autres » : petite part, sous celle des banques : %.2f" % fa)
    g(1 < c["parts"]["OPC"] < 2 and 1 < 100 - sum(c["parts"].values()) < 2,
      "annexe : « les fonds et les autres détenteurs pèsent chacun un peu plus de 1 %% » : %.2f / %.2f" % (c["parts"]["OPC"], 100 - sum(c["parts"].values())))
    g(c["parts"]["assureurs"] > c["parts"]["banques"] and c["parts"]["BdF"] > c["parts"]["assureurs"],
      "ordre des détenteurs dit dans la page (non-résidents, Banque de France, assureurs, banques) : %s" % c["parts"])
    g(0 < 100 - sum(c["parts"].values()) < 5 and c["parts"]["non_residents"] == max(c["parts"].values()),
      "annexe : parts de détention incohérentes, ou les non-résidents ne sont plus le premier groupe : %s" % c["parts"])
    # --- section « achats de la banque centrale » (VERDICT P1 à P4)
    q = c["qe"]
    g(q["atr22"] > q["atr15"] + 1, "P1 : « la durée moyenne de refixation est passée de %.1f à %.1f ans »" % (q["atr15"], q["atr22"]))
    g(q["aj_max"] - q["aj_min"] < 1 and q["aj_max"] < q["atr22"] - 1,
      "P1 : « l'indicateur ajusté est resté entre %.1f et %.1f ans », sous l'indicateur brut" % (q["aj_min"], q["aj_max"]))
    g(q["em_min"] > q["em14"] + 1, "« l'AFT émettait plus long » : %.1f en 2014, %.1f à %.1f ensuite" % (q["em14"], q["em_min"], q["em_max"]))
    r1, r5 = q["sc1"] / q["sm1"], q["sc5"] / q["sm5"]
    g(r1 > 2, "P2 : « plus du double à un an » : %.2f" % r1)
    g(1 < r5 < 1.5 and r5 < r1 / 1.8, "P2 : « à cinq ans l'écart n'est plus que de 1,3 fois : les achats ont surtout avancé » : %.2f contre %.2f" % (r5, r1))
    g(q["sc1_d"] / q["sm1_d"] > 1.8 and q["sc1_d"] / q["sm1_d"] < r1,
      "figure : « l'écart s'est resserré sans disparaître » au dernier mois : %.2f" % (q["sc1_d"] / q["sm1_d"]))
    g(0.05 < q["h_d"] < q["h22"], "figure : « la Banque de France détient encore des titres, moins de titres qu'en 2022 » : h %.3f contre %.3f" % (q["h_d"], q["h22"]))
    g(all(1.05 <= v <= 1.4 for v in q["t4_2015"].values()), "P3 : « de 1,1 à 1,35 en 2015 » : %s" % q["t4_2015"])
    g(all(1.85 <= v <= 2.95 for v in q["t4_max"].values()), "P3 : « au plus de 1,9 à 2,9 » : %s" % q["t4_max"])
    g(q["t4_max"]["FR"] < r1, "P3 : « pour la France, la base homogène donne moins que la mesure sur la dette de l'État »")
    g(q["gain"] > 0 > q["cout"] and abs(q["cout"]) > 3 * q["gain"], "P4 : « gain de 2016 à 2022, coût plus lourd de 2023 à 2025 »")
    g(abs(q["gain"] + q["cout"] - q["solde"]) < 0.05, "P4 : le solde n'est pas la somme des deux phases")
    g(max(abs(q["net_total"] - q["solde"]), abs(q["net_titres"] - q["solde"])) <= 5 and q["net_total"] < 0 and q["net_titres"] < 0,
      "P4 : « la redistribution le déplace de quelques milliards » : %.1f / %.1f contre %.1f" % (q["net_titres"], q["net_total"], q["solde"]))
    g(q["tref_min"] == 0 and 3.5 <= q["tref_max"] < 4.5, "P4 : « le taux de référence est passé de 0 à environ 4 %% » : %.2f" % q["tref_max"])
    g(q["rdt_max"] < 1, "P4 : « les titres rapportaient moins de 1 %% » : %.2f" % q["rdt_max"])
    g(max(float(r["taux_reference_moyen"]) for a, r in q["rc"].items() if a <= 2021) < 0.1,
      "P4 : « le taux de référence, proche de zéro jusqu'en 2021 »")
    g(q["bdf_ro_avant"] > 0 > q["bdf_ro_apres"] and q["solde"] < 0,
      "comptes de la Banque de France : « bénéfices, puis pertes, sur tout le bilan ; sur les seuls titres publics, le portage ne s'équilibre pas »")
    g(abs(q["nous_effet"] - q["ocde_effet"]) <= 0.2, "témoin OCDE : « proche de celui que nous mesurons » : %.2f contre %.2f" % (q["nous_effet"], q["ocde_effet"]))
    g(1.8 <= q["e1_max"] <= 2.3, "témoin Bundesbank : « jusqu'à deux ans » : %.2f" % q["e1_max"])
    return n


# ------------------------------------------------------------------ affichage (mêmes clés, deux langues)
def affichage(c, lang):
    f = lambda v, d=0: nb(v, d, lang)
    A = c["A"]
    k_spf, k_bdf, k_ceA, k_ceH = list(A)
    return {
        "t": str(arr5(c["T"])), "t_exact": f(c["T"], 1), "t_annuel": f(c["T_annuel"], 1), "pts_pib": f(c["pts_pib"], 1),
        "gap23": f(c["gap23"], 1),
        "a_bas": str(arr5(c["A_r0"][0])), "a_haut": str(arr5(c["A_r0"][1])),
        "a_tout_bas": str(arr5(c["A_tout"][0])), "a_tout_haut": str(arr5(c["A_tout"][1])),
        "spf": f(A[k_spf]["r=0%"], 1), "bdf": f(A[k_bdf]["r=0%"], 1), "ce_aut": f(A[k_ceA]["r=0%"], 1), "ce_hiv": f(A[k_ceH]["r=0%"], 1),
        "b_fr": f(c["B"]["point mort France 10 ans au 31/12/2020 (0,861, plat)"], 1),
        "b_eu": f(c["B"]["point mort zone euro 10 ans au 31/12/2020 (1,162, plat)"], 1),
        "defl_bas": str(round(min(c["defl_spf"], c["defl_ce"]))), "defl_haut": str(round(max(c["defl_spf"], c["defl_ce"]))),
        "demi": str(c["demi"]), "cum23": f(c["cum"][2023], 0), "part23": str(round(100 * c["cum"][2023] / c["T"])),
        "cum27": f(c["cum"][2027], 0), "part27": str(round(100 * c["cum"][2027] / c["T"])),
        "cum35": f(c["cum"][2035], 0), "fin": str(max(c["cum"])),
        "idx": str(arr5(c["idx_j"])), "idx_j": f(c["idx_j"], 1), "idx_1": f(c["idx_1"], 1), "idx_tot": f(c["idx_tot"], 1),
        "idx_ecart": f(c["idx_ecart"], 1), "idx_encours": f(c["idx_encours"], 0), "idx_n": str(c["idx_n"]),
        "charge22": f(c["charge_aft"][2022], 0), "charge_cum": f(sum(c["charge_aft"].values()), 1),
        "s_bdf": f(100 * c["s_bdf"], 0), "cons23": f(c["cons23"], 0), "cons25": f(c["cons25"], 0),
        "pal_rapport": f(c["pal_rapport"], 2), "pal_residu": str(round(100 * c["pal_residu"] / c["pal_total"])),
        "pal_explique": str(100 - round(100 * c["pal_residu"] / c["pal_total"])),
        **{"part_" + k: f(v, 0) for k, v in c["parts"].items()},
        **{"alloc_" + k: f(c["T"] * v / 100, 0) for k, v in c["parts"].items()},
        "part_autres": f(100 - sum(c["parts"].values()), 0), "alloc_autres": f(c["T"] * (100 - sum(c["parts"].values())) / 100, 0),
        # « fonds et autres » arrondi sur les parts EXACTES (1,39 + 1,21 = 2,60 -> 3), jamais en additionnant deux arrondis
        # (1 + 1) : défaut relevé par la contre-expertise OPTIMUM-27 (11/10/2026)
        "part_fonds_autres": f(100 - sum(v for k, v in c["parts"].items() if k != "OPC"), 0),
        "alloc_fonds_autres": f(c["T"] * (100 - sum(v for k, v in c["parts"].items() if k != "OPC")) / 100, 0),
        **affichage_qe(c["qe"], lang),
    }


MOIS = {"fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(),
        "en": "January February March April May June July August September October November December".split()}


def affichage_qe(q, lang):
    # arrondi au plus proche, moitié vers le haut, sur la valeur décimale lue : l'extrait porte deux décimales, et 12,35 doit
    # s'afficher 12,4 comme dans le verdict de la recherche, non 12,3 par la représentation binaire du flottant
    from decimal import Decimal, ROUND_HALF_UP
    f = lambda v, d=1: nb(float(Decimal(repr(v)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)), d, lang)
    mois = lambda d: "%s %s" % (MOIS[lang][int(d[5:7]) - 1], d[:4])
    return {
        "qe_atr15": f(q["atr15"]), "qe_atr22": f(q["atr22"]), "qe_aj_min": f(q["aj_min"]), "qe_aj_max": f(q["aj_max"]),
        "qe_em14": f(q["em14"]), "qe_em_min": f(q["em_min"]), "qe_em_max": f(q["em_max"]),
        "qe_sc1": f(q["sc1"]), "qe_sm1": f(q["sm1"], 2), "qe_sc1_pib": f(q["sc1_pib"], 2), "qe_r1": f(q["sc1"] / q["sm1"]),
        "qe_sc5": f(q["sc5"]), "qe_sm5": f(q["sm5"]), "qe_r5": f(q["sc5"] / q["sm5"]),
        "qe_dern": mois(q["dern"]), "qe_sc1_d": f(q["sc1_d"]), "qe_sm1_d": f(q["sm1_d"]), "qe_r_d": f(q["sc1_d"] / q["sm1_d"]),
        "qe_h22": f(100 * q["h22"], 0), "qe_h_d": f(100 * q["h_d"], 0),
        "qe_t4_2015_bas": f(min(q["t4_2015"].values())), "qe_t4_2015_haut": f(max(q["t4_2015"].values()), 2),
        "qe_t4_bas": f(min(q["t4_max"].values())), "qe_t4_haut": f(max(q["t4_max"].values())), "qe_t4_fr": f(q["t4_max"]["FR"]),
        "qe_gain": f(q["gain"], 0), "qe_cout": f(abs(q["cout"]), 0), "qe_solde": f(abs(q["solde"]), 0),
        "qe_net_bas": f(abs(max(q["net_total"], q["net_titres"])), 0), "qe_net_haut": f(abs(min(q["net_total"], q["net_titres"])), 0),
        "qe_rdt_min": f(q["rdt_min"]), "qe_rdt_max": f(q["rdt_max"]), "qe_tref_max": f(q["tref_max"], 0),
        "qe_bdf_ro_avant": f(q["bdf_ro_avant"]), "qe_bdf_ro_apres": f(abs(q["bdf_ro_apres"])), "qe_bdf_verse": f(q["bdf_verse_avant"]),
        "qe_ocde_effet": f(q["ocde_effet"], 2), "qe_nous_effet": f(q["nous_effet"], 2), "qe_ocde_aj": f(q["ocde_aj"]),
        "qe_e1_max": f(q["e1_max"]), "qe_e1_date": mois(q["e1_date"]),
    }


# ------------------------------------------------------------------ figure signature
TXT = {
    "fr": dict(titre="Dette de l'État à taux fixe de fin 2020 : l'érosion due à la surprise d'inflation, au fil des paiements",
               desc="Courbe cumulée de l'érosion réelle des paiements promis, de 2021 à {fin}, en milliards d'euros de 2020 : {cum23} fin 2023, "
                    "{cum27} fin {demi}, soit environ {part27} %, {t_exact} au total ; plage des prévisions publiées début 2021 : {a_bas} à {a_haut}. "
                    "Après 2023, l'écart de prix est supposé persister.",
               source="AFT (encours au 31/12/2020), Eurostat (IPCH mensuel, France), BCE (SPF, janvier 2021) ; calcul de l'auteur",
               note="Somme non actualisée des écarts de valeur réelle des paiements promis, en Md€ de 2020 aux prix à la consommation : ni de la dette effacée, "
                    "ni un gain budgétaire net, ni une perte finale. Contrefactuel : inflation anticipée début 2021 ; après 2023, l'écart de prix est supposé persister.",
               axe="Md€ de 2020, cumul", total="total : {t_exact}", demi="environ {part27} % d'ici fin {demi}", plage="selon la prévision de départ : {a_bas} à {a_haut}",
               apres="après 2023 : écart de prix supposé persistant",
               titre_m="Dette à taux fixe de fin 2020 : l'érosion, au fil des paiements", axe_m="Md€ de 2020, cumul",
               montre="L'érosion est acquise fin 2023 dans ce contrefactuel, mais elle se matérialise au rythme des paiements : environ {part27} % d'ici fin {demi}."),
    "en": dict(titre="End-2020 fixed-rate government debt: erosion from the inflation surprise, as payments fall due",
               desc="Cumulative real-value erosion of promised payments, 2021 to {fin}, in billions of 2020 euros: {cum23} by end-2023, "
                    "{cum27} by end-{demi}, about {part27}%, {t_exact} in total; range of forecasts published in early 2021: {a_bas} to {a_haut}. "
                    "After 2023, the price gap is assumed to persist.",
               source="AFT (outstanding debt, 31/12/2020), Eurostat (monthly HICP, France), ECB (SPF, January 2021); author's calculation",
               note="Undiscounted sum of the real-value differences in promised payments, €bn in 2020 euros at French consumer prices: not debt written off, "
                    "not a net fiscal gain, not a final loss. Counterfactual: inflation expected in early 2021; after 2023, the price gap is assumed to persist.",
               axe="€bn in 2020 euros, cumulative", total="total: {t_exact}", demi="about {part27}% by end-{demi}", plage="depending on the starting forecast: {a_bas} to {a_haut}",
               apres="after 2023: price gap assumed to persist",
               titre_m="End-2020 fixed-rate debt: the erosion, as payments fall due", axe_m="€bn in 2020 euros, cumulative",
               montre="In this counterfactual the erosion is locked in by end-2023, but it materialises as payments fall due: about {part27}% by end-{demi}."),
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def fig_calendrier(c, Aff, lang):
    t = {k: v.format(**Aff) for k, v in TXT[lang].items()}
    h = 292
    X0, X1, TOP, BAS = 54, 690, 44, 262
    a0, a1 = 2020, max(c["cum"])
    vmax = 200

    def X(a):
        return X0 + (X1 - X0) * (a - a0) / (a1 - a0)

    def Y(v):
        return BAS - (BAS - TOP) * v / vmax

    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="infl-t infl-d" font-family="%s">' % (W, h + 52, FONT),
         '<title id="infl-t">%s</title><desc id="infl-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"]))]
    for gv in range(0, vmax + 1, 50):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(gv), X1, Y(gv), GRID, 1.2 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d</text>' % (X0 - 6, Y(gv) + 3, MUTED, gv))
    e.append('<text x="%d" y="%d" font-size="10" fill="%s">%s</text>' % (X0, TOP - 8, MUTED, esc(t["axe"])))
    # intervalle au POINT FINAL : la plage des prévisions de départ (famille A, sans actualisation) porte sur le total,
    # pas sur une période ; une bande 2052-2066 se lisait comme une incertitude datée (contre-expertise OPTIMUM-28, 11/10/2026)
    lo, hi = c["A_r0"]
    xi = X1 + 12
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>' % (xi, Y(hi), xi, Y(lo), INK2))
    for v in (lo, hi):
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>' % (xi - 4, Y(v), xi + 4, Y(v), INK2))
    e.append('<text x="%.1f" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (xi + 4, Y(hi) - 7, INK2, esc(t["plage"])))
    for a in range(2025, a1 + 1, 5):
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 14, MUTED, a))
    # trait plein jusqu'à fin 2023 (inflation réalisée), pointillé ensuite : au-delà, les paiements sont évalués sous
    # l'hypothèse du contrefactuel (l'écart de prix persiste), pas observés (contre-expertise OPTIMUM-27, 11/10/2026)
    pts = [(a0, 0.0)] + sorted(c["cum"].items())
    trace = lambda ps: " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(v)) for k, (a, v) in enumerate(ps))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>' % (trace([p for p in pts if p[0] <= 2023]), BLEU))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-dasharray="6 4" stroke-linejoin="round"/>'
             % (trace([p for p in pts if p[0] >= 2023]), BLEU))
    e.append('<text x="%.1f" y="%.1f" font-size="10" fill="%s">%s</text>' % (X(2034), Y(c["cum"][2034]) + 22, INK2, esc(t["apres"])))
    # jalons : fin 2023, demi-réalisation, total
    for a, lib in ((2023, ("fin 2023 : %s" if lang == "fr" else "end-2023: %s") % Aff["cum23"]), (c["demi"], t["demi"])):
        v = c["cum"][a]
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (X(a), Y(v), BLEU))
        e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s">%s</text>' % (X(a) + 7, Y(v) + 12, INK, esc(lib)))
    e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (X(a1), Y(c["T"]), BLEU))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (X(a1) - 6, Y(c["T"]) + 16, BLEU, esc(t["total"])))
    return pied_figure.pied(e, h + 2, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


TXT_QE = {
    "fr": dict(titre="Hausse durable d'un point des taux : combien d'intérêts supplémentaires dès la première année ?",
               titre_m="Un point de taux en plus : intérêts supplémentaires la première année",
               desc="Courbes mensuelles, de mars 2015 à {qe_dern}, en milliards d'euros : hausse de la charge d'intérêts la première année, en scénario, pour l'ensemble "
                    "État + Banque de France ({qe_sc1} fin 2022, {qe_sc1_d} en {qe_dern}) et pour la seule dette de marché de l'État "
                    "({qe_sm1} fin 2022, {qe_sm1_d} en {qe_dern}).",
               source="AFT (bulletins mensuels, ligne à ligne), Banque de France (Webstat), BCE ; décision (UE) 2016/2248 ; calcul de l'auteur",
               note="Scénario : +1 point sur toute la courbe, encours constant ; titres de la Banque de France au taux de référence de la BCE. "
                    "Ni une prévision, ni une série de dépenses constatées, ni le coût du QE.",
               axe="Md€ la première année", cons="État + Banque de France (périmètre d'analyse)", marche="dette de marché de l'État seule", jalon="fin 2022",
               cons_m="État + Banque de France", marche_m="dette de marché seule",
               montre="Fin 2022, si toute la courbe des taux avait augmenté d'un point, la charge de l'ensemble État + Banque de France aurait "
                      "augmenté la première année {qe_r1} fois plus que celle de la seule dette de marché ; l'écart se resserre depuis, sans disparaître."),
    "en": dict(titre="A lasting one-percentage-point rise in rates: how much extra interest in the first year?",
               titre_m="One more percentage point: extra interest in year one",
               desc="Monthly lines, March 2015 to {qe_dern}, in billions of euros: first-year rise in the interest bill, in a scenario, for the government and the "
                    "Banque de France taken together ({qe_sc1} at end-2022, {qe_sc1_d} in {qe_dern}) and for central-government marketable "
                    "debt alone ({qe_sm1} at end-2022, {qe_sm1_d} in {qe_dern}).",
               source="AFT (monthly bulletins, line by line), Banque de France (Webstat), ECB; Decision (EU) 2016/2248; author's calculation",
               note="Scenario: +1 point across the whole curve, constant stock; Banque de France holdings at the ECB reference rate. "
                    "Not a forecast, not a series of recorded spending, nor the cost of QE.",
               axe="€bn in the first year", cons="Government + Banque de France (analytical scope)", marche="central-government marketable debt alone", jalon="end-2022",
               cons_m="Government + Banque de France", marche_m="marketable debt alone",
               montre="At end-2022, had the whole yield curve risen by one point, the first-year interest bill of the government and the Banque de France "
                      "together would have risen {qe_r1} times as much as that of market debt alone; the gap has narrowed since, without closing."),
}


def fig_achats(q, Aff, lang):
    t = {k: v.format(**Aff) for k, v in TXT_QE[lang].items()}
    h = 292
    X0, X1, TOP, BAS = 54, 640, 44, 262
    serie = q["serie"]
    mois = lambda d: int(d[:4]) + (int(d[5:7]) - 0.5) / 12
    m0, m1 = mois(serie[0][0]), mois(serie[-1][0])
    vmax = 2 * (int(max(s for _, _, s in serie) / 2) + 1)

    def X(m):
        return X0 + (X1 - X0) * (m - m0) / (m1 - m0)

    def Y(v):
        return BAS - (BAS - TOP) * v / vmax

    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="achats-t achats-d" font-family="%s">' % (W, h + 52, FONT),
         '<title id="achats-t">%s</title><desc id="achats-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"]))]
    for gv in range(0, vmax + 1, 2):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(gv), X1, Y(gv), GRID, 1.2 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d</text>' % (X0 - 6, Y(gv) + 3, MUTED, gv))
    e.append('<text x="%d" y="%d" font-size="10" fill="%s">%s</text>' % (X0, TOP - 8, MUTED, esc(t["axe"])))
    for a in range(int(m0) + 1, int(m1) + 1, 2):
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 14, MUTED, a))
    for k, col, larg in ((1, GRIS, 2.0), (2, ORANGE, 2.4)):
        d = " ".join(("M" if i == 0 else "L") + "%.1f,%.1f" % (X(mois(r[0])), Y(r[k])) for i, r in enumerate(serie))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (d, col, larg))
    # noms posés sur les séries, au milieu de la période d'achats (2018) : la consolidée au-dessus, le marché en dessous
    r18 = min(serie, key=lambda r: abs(mois(r[0]) - 2018.5))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (X(mois(r18[0])), Y(r18[2]) - 9, ORANGE, esc(t["cons"])))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (X(mois(r18[0])), Y(r18[1]) + 16, INK2, esc(t["marche"])))
    # jalon fin 2022 : date au-dessus du point consolidé, valeur du marché sous son point
    r22 = next(r for r in serie if r[0] == "2022-12-31")
    x22 = X(mois(r22[0]))
    e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (x22, Y(r22[2]), ORANGE))
    e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (x22, Y(r22[1]), GRIS))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s" text-anchor="middle">%s%s%s</text>' % (x22, Y(r22[2]) - 9, INK, esc(t["jalon"]), " : " if lang == "fr" else ": ", Aff["qe_sc1"]))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (x22, Y(r22[1]) + 16, INK, Aff["qe_sm1"]))
    # valeurs terminales
    rd = serie[-1]
    for k, col, lib in ((2, ORANGE, Aff["qe_sc1_d"]), (1, GRIS, Aff["qe_sm1_d"])):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (X1, Y(rd[k]), col))
        e.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="600" fill="%s">%s</text>' % (X1 + 7, Y(rd[k]) + 4, ORANGE if k == 2 else INK2, lib))
    e.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="%s">%s</text>' % (X1 + 7, Y(rd[2]) - 10, MUTED, esc(Aff["qe_dern"])))
    return pied_figure.pied(e, h + 2, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


# ------------------------------------------------------------------ versions téléphone (300 de large, recomposées)
# Composées pour le téléphone, jamais réduites : titre court, résultats décisifs seulement, police >= FS_MIN, pied lisible.
# Chaque valeur dessinée en gras ou en couleur figure dans la description de la version détaillée (pied_figure.parite).
def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_calendrier_m(c, Aff, lang, svg_d):
    t = {k: v.format(**Aff) for k, v in TXT[lang].items()}
    e, y = pied_figure.tete_mobile("inflm", t["titre_m"], desc_de(svg_d), INK, FONT)
    X0, X1, TOP = 34, WM - 4, y + 34
    BAS = TOP + 200
    a0, a1, vmax = 2020, max(c["cum"]), 200
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * v / vmax
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (TOP - 14, FS_MIN, MUTED, esc(t["axe_m"])))
    for gv in range(0, vmax + 1, 50):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(gv), X1, Y(gv), GRID, 1.2 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(gv) + 4, FS_MIN, MUTED, gv))
    for a in (2021, 2045, a1):
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                 % (X(a), BAS + 18, FS_MIN, MUTED, "start" if a == 2021 else ("end" if a == a1 else "middle"), a))
    pts = [(a0, 0.0)] + sorted(c["cum"].items())
    trace = lambda ps: " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(v)) for k, (a, v) in enumerate(ps))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6"/>' % (trace([p for p in pts if p[0] <= 2023]), BLEU))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" stroke-dasharray="6 4"/>' % (trace([p for p in pts if p[0] >= 2023]), BLEU))
    for a in (2023, c["demi"], a1):
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(a), Y(c["cum"][a]), BLEU))
    lo, hi = c["A_r0"]
    xi = X1 - 1
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.8"/>' % (xi, Y(hi), xi, Y(lo), INK2))
    for v in (lo, hi):
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.8"/>' % (xi - 4, Y(v), xi + 3, Y(v), INK2))
    y = BAS + 30
    lignes = [(("fin 2023 : %s" if lang == "fr" else "end-2023: %s") % Aff["cum23"], INK),
              (t["demi"], INK), (t["total"], BLEU)]
    plage_m = (("prévision de départ : %s à %s" if lang == "fr" else "starting forecast: %s to %s") % (Aff["a_bas"], Aff["a_haut"]))
    for lib, col in lignes:
        y += 20
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, col, esc(lib)))
    y += 20
    e.append('<text x="0" y="%d" font-size="15" fill="%s">%s</text>' % (y, INK2, esc(plage_m)))
    for l in pied_figure.coupe(t["apres"], 38):
        y += 19
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    return pied_figure.pied_mobile(e, y + 14, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fig_achats_m(q, Aff, lang, svg_d):
    t = {k: v.format(**Aff) for k, v in TXT_QE[lang].items()}
    e, y = pied_figure.tete_mobile("achm", t["titre_m"], desc_de(svg_d), INK, FONT)
    serie = q["serie"]
    mois = lambda d: int(d[:4]) + (int(d[5:7]) - 0.5) / 12
    m0, m1 = mois(serie[0][0]), mois(serie[-1][0])
    vmax = 2 * (int(max(s for _, _, s in serie) / 2) + 1)
    X0, X1, TOP = 26, WM - 4, y + 34
    BAS = TOP + 190
    X = lambda m: X0 + (X1 - X0) * (m - m0) / (m1 - m0)
    Y = lambda v: BAS - (BAS - TOP) * v / vmax
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (TOP - 14, FS_MIN, MUTED, esc(t["axe"])))
    for gv in range(0, vmax + 1, 4):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(gv), X1, Y(gv), GRID, 1.2 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(gv) + 4, FS_MIN, MUTED, gv))
    for a in (2016, 2021, 2026):
        if m0 <= a <= m1 + 0.5:
            e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                     % (min(X(a), X1), BAS + 18, FS_MIN, MUTED, "end" if X(a) > X1 - 20 else "middle", a))
    for k, col, larg in ((1, GRIS, 2.2), (2, ORANGE, 2.6)):
        d = " ".join(("M" if i == 0 else "L") + "%.1f,%.1f" % (X(mois(r[0])), Y(r[k])) for i, r in enumerate(serie))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, col, larg))
    r22 = next(r for r in serie if r[0] == "2022-12-31")
    for k, col in ((2, ORANGE), (1, GRIS)):
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(mois(r22[0])), Y(r22[k]), col))
    y = BAS + 30
    sep = " : " if lang == "fr" else ": "
    # chaque valeur avec sa courbe, aux deux dates (OPTIMUM-28 : « 7,3 / 3,6 » ne disait pas laquelle était laquelle)
    lignes = []
    for jalon, vc, vm in ((t["jalon"], Aff["qe_sc1"], Aff["qe_sm1"]), (Aff["qe_dern"], Aff["qe_sc1_d"], Aff["qe_sm1_d"])):
        lignes += [((jalon + sep).capitalize(), INK2), ("%s%s%s" % (t["cons_m"], sep, vc), ORANGE), ("%s%s%s" % (t["marche_m"], sep, vm), INK2)]
    for lib, col in lignes:
        y += 20
        poids = ' font-weight="600"' if col == ORANGE else ""
        e.append('<text x="0" y="%d" font-size="15"%s fill="%s">%s</text>' % (y, poids, col, esc(lib)))
    return pied_figure.pied_mobile(e, y + 14, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fiches(figs, Aff):
    out = {}
    for lang in ("fr", "en"):
        out[lang] = []
        for id_, base, txt in (("calendrier", "dette-inflation-calendrier", TXT), ("achats", "dette-inflation-achats", TXT_QE)):
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
    for a, v in sorted(c["cum"].items()):
        w.writerow(["calendrier", "erosion_cumulee_realisee", a, "%.1f" % v, "Md EUR 2020"])
    for k, x in c["A"].items():
        for r, v in x.items():
            w.writerow(["famille_A_previsions", k, r, "%.1f" % v, "Md EUR 2020"])
    for k, v in c["B"].items():
        w.writerow(["famille_B_marche_sensibilite", k, "r=0%", "%.1f" % v, "Md EUR 2020"])
    for k, v in (("central_ipch_mensuel", c["T"]), ("meme_calcul_moyennes_annuelles", c["T_annuel"]),
                 ("deflateur_pib_anticipation_spf_annuel", c["defl_spf"]), ("deflateur_pib_contre_prevision_commission_annuel", c["defl_ce"]),
                 ("indexes_transfert_renonce_paires_jumelles", c["idx_j"]), ("indexes_point_unique_1_162", c["idx_1"]),
                 ("indexes_cout_total_avec_ecart_indice", c["idx_tot"]),
                 ("consolide_etat_bdf_fin_2023", c["cons23"]), ("consolide_etat_bdf_fin_2025", c["cons25"])):
        w.writerow(["resultats", k, "", "%.1f" % v, "Md EUR 2020"])
    for k, v in c["parts"].items():
        w.writerow(["annexe_allocation_mecanique", k, "part_detention_2020T4_pct", "%.2f" % v, "%"])
        w.writerow(["annexe_allocation_mecanique", k, "allocation", "%.1f" % (c["T"] * v / 100), "Md EUR 2020"])
    q = c["qe"]
    for d, sm, sc in q["serie"]:
        w.writerow(["achats_surcout_premiere_annee", "dette_de_marche_seule", d, "%.2f" % sm, "Md EUR courants"])
        w.writerow(["achats_surcout_premiere_annee", "etat_plus_banque_de_france", d, "%.2f" % sc, "Md EUR courants"])
    for d, a, aj in q["atr"]:
        w.writerow(["achats_duree_refixation", "dette_etat_taux_fixe", d, "%.3f" % a, "annees"])
        w.writerow(["achats_duree_refixation", "ajustee_titres_detenus_par_la_banque_de_france", d, "%.3f" % aj, "annees"])
    for a in sorted(q["C"]):
        w.writerow(["achats_portage_net", "rendement_moins_taux_de_reference", a, "%.0f" % q["C"][a], "M EUR courants"])
        if a in q["st"]:
            w.writerow(["achats_portage_net", "solde_partage_revenu_monetaire_total", a, "%.0f" % q["st"][a], "M EUR courants"])
        if a in q["ns"]:
            w.writerow(["achats_portage_net", "solde_partage_ligne_des_titres", a, "%.0f" % q["ns"][a], "M EUR courants"])
    for pays, v in sorted(q["t4"].items()):
        for a, r in sorted(v.items()):
            w.writerow(["achats_comparaison_pays", pays, a, "%.3f" % r, "rapport consolidee / marche a un an"])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    v3, sens, ci = lire()
    c = calcul(v3, sens, ci)
    c["qe"] = calcul_qe(lire_qe())
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, lang) for lang in ("fr", "en")}
    if set(Aff["fr"]) != set(Aff["en"]):
        fail("blocs affichage et affichage_en : cles differentes")
    log("Erosion %.1f Md EUR 2020 (annuel %.1f) ; famille A %s ; demi %s ; indexes %.1f ; consolide %.1f -> %.1f"
        % (c["T"], c["T_annuel"], c["A_r0"], c["demi"], c["idx_j"], c["cons23"], c["cons25"]))
    figs = {"dette-inflation-calendrier%s.svg" % SUFFIXE[lang]: fig_calendrier(c, Aff[lang], lang) for lang in ("fr", "en")}
    figs.update({"dette-inflation-achats%s.svg" % SUFFIXE[lang]: fig_achats(c["qe"], Aff[lang], lang) for lang in ("fr", "en")})
    for lang in ("fr", "en"):
        sf = SUFFIXE[lang]
        figs["dette-inflation-calendrier%s-m.svg" % sf] = fig_calendrier_m(c, Aff[lang], lang, figs["dette-inflation-calendrier%s.svg" % sf])
        figs["dette-inflation-achats%s-m.svg" % sf] = fig_achats_m(c["qe"], Aff[lang], lang, figs["dette-inflation-achats%s.svg" % sf])
        for fid in ("calendrier", "achats"):
            ec = pied_figure.parite(figs["dette-inflation-%s%s.svg" % (fid, sf)], figs["dette-inflation-%s%s-m.svg" % (fid, sf)], FS_MIN)
            if ec:
                fail("parite mobile %s %s : %s" % (fid, lang, " ; ".join(ec)))
    for page, sf in (("_index.md", ""), ("_index.en.md", "-en")):
        ec = pied_figure.controler_page((ROOT / "content" / "inflation-et-dette-publique" / page).read_text(encoding="utf-8"),
                                        {f: v for f, v in figs.items() if re.fullmatch(r"dette-inflation-[a-z]+%s(-m)?\.svg" % sf, f)})
        if ec:
            fail("page %s : %s" % (page, " ; ".join(ec)))
    if check:   # après les figures : parité téléphone et hauteurs déclarées se contrôlent aussi sans écrire
        log("--check : %d gardes passees (%d cles d'affichage), parite des 4 figures telephone et hauteurs des pages controlees, rien ecrit."
            % (n, len(Aff["fr"])))
        return 0
    import cairosvg
    q_ = c["qe"]
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "perimetre": "dette négociable de l'État à taux fixe au 31/12/2020 (OAT à taux fixe et BTF), flux promis (coupons et principal)",
                        "numeraire": "euros de 2020 aux prix à la consommation français (IPCH, moyenne annuelle 2020)",
                        "contrefactuel": "inflation anticipée début 2021 ; choc fermé : après décembre 2023, l'écart de niveau des prix persiste",
                        "source_calcul": "dépôt de recherche de l'auteur, scripts/v3.py ; extrait figé scripts/sources_inflation_dette/ (SHA256SUMS)"},
               "calendrier": {str(a): v for a, v in sorted(c["cum"].items())},
               "famille_A": c["A"], "famille_B": c["B"],
               "resultats": {"central": c["T"], "moyennes_annuelles": c["T_annuel"], "deflateur": [c["defl_spf"], c["defl_ce"]],
                             "indexes_paires_jumelles": c["idx_j"], "consolide_2023": c["cons23"], "consolide_2025": c["cons25"]},
               "achats_banque_centrale": {
                   "perimetre": "dette négociable de l'État à taux fixe (AFT, ligne à ligne, fin de mois) ; titres de l'État détenus par la Banque de France, tous portefeuilles (Webstat), au nominal",
                   "regle": "décision (UE) 2016/2248 : titres détenus réputés rapporter le taux de référence de la BCE dans le revenu mis en commun",
                   "source_calcul": "dépôt de recherche de l'auteur, chantier QE et maturité consolidée (VERDICT.md) ; extrait figé scripts/sources_qe_maturite/ (SHA256SUMS)",
                   "fin_2022": {"surcout_1an_marche": q_["sm1"], "surcout_1an_consolide": q_["sc1"], "surcout_5ans_marche": q_["sm5"], "surcout_5ans_consolide": q_["sc5"]},
                   "portage_net_mdeur": {"2016_2022": round(q_["gain"], 1), "2023_2025": round(q_["cout"], 1), "solde": round(q_["solde"], 1),
                                         "apres_partage_total": round(q_["net_total"], 1), "apres_partage_ligne_des_titres": round(q_["net_titres"], 1)},
                   "rapport_pays_max": {k: round(v, 3) for k, v in q_["t4_max"].items()}},
               "affichage": Aff["fr"], "affichage_en": Aff["en"]}
    releve = None
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            same = {k: v for k, v in prev.items() if k not in ("releve_le", "_licence")} == json.loads(json.dumps(payload, ensure_ascii=False))
            if same and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c) \
                    and OUT_FIGURES.exists() \
                    and OUT_FIGURES.read_text(encoding="utf-8") == json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n":
                # (10/10/2026) fiches « Réutiliser » comparées aussi : sans elles, une légende corrigée n'était jamais réécrite.
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
            # données identiques hors blocs d'affichage (texte d'une figure, clé d'affichage nouvelle) : la date de relevé
            # reste celle des DONNÉES, sinon la page afficherait « Calcul du » au jour d'une simple retouche (11/10/2026)
            hors_aff = lambda d: {k: v for k, v in d.items() if k not in ("releve_le", "_licence", "affichage", "affichage_en")}
            if same or hors_aff(prev) == hors_aff(json.loads(json.dumps(payload, ensure_ascii=False))):
                releve = prev["releve_le"]
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; sources AFT, Eurostat, BCE, Banque de France, Commission européenne", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dette_inflation.json, static/dette_inflation.csv, data/figures_inflation.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
