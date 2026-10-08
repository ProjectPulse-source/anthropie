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

Usage : python scripts/update_dette_inflation.py [--check] [--mutation=demi|indexes|consolidation|encadre]
Sorties : data/ et static/dette_inflation.json, static/dette_inflation.csv, data/figures_inflation.json,
          static/img/dette-inflation-calendrier{,-en}.svg + .png
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

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_inflation_dette"
OUT_DATA = ROOT / "data" / "dette_inflation.json"
OUT_STATIC = ROOT / "static" / "dette_inflation.json"
OUT_CSV = ROOT / "static" / "dette_inflation.csv"
OUT_FIGURES = ROOT / "data" / "figures_inflation.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/inflation-et-dette-publique/"
PAGE_URL_EN = "stephane-lalut.com/en/inflation-and-french-public-debt/"

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCES = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Computed by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
SUFFIXE = {"fr": "", "en": "-en"}


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
    g(0 < 100 - sum(c["parts"].values()) < 5 and c["parts"]["non_residents"] == max(c["parts"].values()),
      "annexe : parts de détention incohérentes, ou les non-résidents ne sont plus le premier groupe : %s" % c["parts"])
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
    }


# ------------------------------------------------------------------ figure signature
TXT = {
    "fr": dict(titre="Dette de l'État à taux fixe de fin 2020 : l'érosion due à la surprise d'inflation, au fil des paiements",
               desc="Courbe cumulée de l'érosion réelle des paiements promis, de 2021 à {fin}, en milliards d'euros de 2020 : {cum23} fin 2023, "
                    "{cum27} fin {demi}, {t_exact} au total ; plage des prévisions publiées début 2021 : {a_bas} à {a_haut}.",
               source="AFT (encours au 31/12/2020), Eurostat (IPCH mensuel, France), BCE (SPF, janvier 2021) ; calcul de l'auteur",
               note="Md€ de 2020 aux prix à la consommation, non actualisés ; contrefactuel : inflation anticipée début 2021. Ni gain budgétaire net, ni perte finale.",
               axe="Md€ de 2020, cumul", total="total : {t_exact}", demi="moitié atteinte en {demi}", plage="prévisions publiées : {a_bas} à {a_haut}",
               montre="L'érosion est acquise fin 2023 dans ce contrefactuel, mais elle se matérialise au rythme des paiements : environ la moitié d'ici {demi}."),
    "en": dict(titre="End-2020 fixed-rate government debt: erosion from the inflation surprise, as payments fall due",
               desc="Cumulative real-value erosion of promised payments, 2021 to {fin}, in billions of 2020 euros: {cum23} by end-2023, "
                    "{cum27} by end-{demi}, {t_exact} in total; range of forecasts published in early 2021: {a_bas} to {a_haut}.",
               source="AFT (outstanding debt, 31/12/2020), Eurostat (monthly HICP, France), ECB (SPF, January 2021); author's calculation",
               note="€bn in 2020 euros at French consumer prices, undiscounted; counterfactual: inflation expected in early 2021. Neither a net fiscal gain nor a final loss.",
               axe="€bn in 2020 euros, cumulative", total="total: {t_exact}", demi="half reached in {demi}", plage="published forecasts: {a_bas} to {a_haut}",
               montre="In this counterfactual the erosion is locked in by end-2023, but it materialises as payments fall due: about half by {demi}."),
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
    # bande : plage des prévisions publiées début 2021 (famille A, sans actualisation)
    lo, hi = c["A_r0"]
    e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity="0.35"/>' % (X(2052), Y(hi), X1 - X(2052), Y(lo) - Y(hi), GRIS_CLAIR))
    e.append('<text x="%.1f" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X1, Y(hi) - 5, INK2, esc(t["plage"])))
    for a in range(2025, a1 + 1, 5):
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 14, MUTED, a))
    pts = [(a0, 0.0)] + sorted(c["cum"].items())
    d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(v)) for k, (a, v) in enumerate(pts))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>' % (d, BLEU))
    # jalons : fin 2023, demi-réalisation, total
    for a, lib in ((2023, ("fin 2023 : %s" if lang == "fr" else "end-2023: %s") % Aff["cum23"]), (c["demi"], t["demi"])):
        v = c["cum"][a]
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (X(a), Y(v), BLEU))
        e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s">%s</text>' % (X(a) + 7, Y(v) + 12, INK, esc(lib)))
    e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (X(a1), Y(c["T"]), BLEU))
    e.append('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (X(a1) - 6, Y(c["T"]) + 16, BLEU, esc(t["total"])))
    y0 = h + 2
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID))
    for k, (tx, col) in enumerate([(t["source"], INK2), (t["note"], INK2), (LICENCES[lang], MUTED)]):
        e.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, col, esc(tx)))
    e.append("</svg>")
    return "\n".join(e)


def fiches(figs, Aff):
    out = {}
    for lang in ("fr", "en"):
        f = "dette-inflation-calendrier%s" % SUFFIXE[lang]
        svg = figs[f + ".svg"]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        out[lang] = [dict(id="calendrier", fichier=f, titre=titre, montre=TXT[lang]["montre"].format(**Aff[lang]), source=cart[0], precaution=cart[1])]
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
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    v3, sens, ci = lire()
    c = calcul(v3, sens, ci)
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, lang) for lang in ("fr", "en")}
    if set(Aff["fr"]) != set(Aff["en"]):
        fail("blocs affichage et affichage_en : cles differentes")
    log("Erosion %.1f Md EUR 2020 (annuel %.1f) ; famille A %s ; demi %s ; indexes %.1f ; consolide %.1f -> %.1f"
        % (c["T"], c["T_annuel"], c["A_r0"], c["demi"], c["idx_j"], c["cons23"], c["cons25"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(Aff["fr"])))
        return 0
    import cairosvg
    figs = {"dette-inflation-calendrier%s.svg" % SUFFIXE[lang]: fig_calendrier(c, Aff[lang], lang) for lang in ("fr", "en")}
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "perimetre": "dette négociable de l'État à taux fixe au 31/12/2020 (OAT à taux fixe et BTF), flux promis (coupons et principal)",
                        "numeraire": "euros de 2020 aux prix à la consommation français (IPCH, moyenne annuelle 2020)",
                        "contrefactuel": "inflation anticipée début 2021 ; choc fermé : après décembre 2023, l'écart de niveau des prix persiste",
                        "source_calcul": "dépôt de recherche de l'auteur, scripts/v3.py ; extrait figé scripts/sources_inflation_dette/ (SHA256SUMS)"},
               "calendrier": {str(a): v for a, v in sorted(c["cum"].items())},
               "famille_A": c["A"], "famille_B": c["B"],
               "resultats": {"central": c["T"], "moyennes_annuelles": c["T_annuel"], "deflateur": [c["defl_spf"], c["defl_ce"]],
                             "indexes_paires_jumelles": c["idx_j"], "consolide_2023": c["cons23"], "consolide_2025": c["cons25"]},
               "affichage": Aff["fr"], "affichage_en": Aff["en"]}
    releve = None
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            same = {k: v for k, v in prev.items() if k not in ("releve_le", "_licence")} == json.loads(json.dumps(payload, ensure_ascii=False))
            if same and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
            if same:  # donnees identiques, seul le texte d'une figure change : la date de releve reste celle des donnees
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
