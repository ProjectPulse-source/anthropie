#!/usr/bin/env python3
"""update_lycee_professeurs.py -- ressource « Manque-t-il des professeurs au lycée ? » (bloc École et lycée).

Découverte de la page (dépôt de pilotage de l'auteur, 06_PROMOTION/RECHERCHE_LYCEES_MOYENS_2026-10-07, test décisif du
07/10/2026, protocole écrit avant calcul, deux contre-expertises arbitrées) : « le manque de professeurs » recouvre
quatre mesures qui ne disent pas la même chose. Au lycée général et technologique, une heure de cours sur dix n'a pas
lieu, et en 2024-2025 plus de la moitié de ces heures tient à l'organisation (examens, fermetures, formation) plutôt
qu'aux absences individuelles ; les concours de mathématiques et de physique-chimie restent sous quatre postes pourvus
sur cinq quand la couverture nationale atteint son meilleur niveau depuis 2015 ; les classes dépassent 30 élèves depuis
2020, mais les divisions de 35 et plus sont moins fréquentes qu'en 2015.

Entrée : l'extrait FIGÉ du test décisif, scripts/sources_lycee_professeurs/extrait.json (écrit par extrait.py du dépôt
de recherche, qui retrouve ses valeurs phares dans la sortie du test), contrôlé contre SHA256SUMS. Ce générateur ne
recalcule que des rapports simples ; il met en forme et GARDE : chaque qualificatif de la prose est une condition sur les
nombres (fonction gardes) ; si l'extrait la dément, arrêt.
Mise à jour : à la main, à chaque nouvelle édition de la DEPP (RERS fin août, note sur le temps d'enseignement non assuré
au printemps, note sur les élèves par structure fin août) : relancer test_decisif.py puis extrait.py dans le dépôt de
recherche, recopier l'extrait et son empreinte, relancer ce script. Rendez-vous : septembre 2027 (RERS 2027).
Page en français seulement (exclusion déclarée : débat, programme et statistique français).

Usage : python scripts/update_lycee_professeurs.py [--check] [--mutation=organisation|classes|concours|ocde]
Sorties : data/ et static/lycee_professeurs.json, static/lycee_professeurs.csv, data/figures_lycee.json,
          static/img/lycee-{heures,classes,concours}.svg + .png
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
SRC = ROOT / "scripts" / "sources_lycee_professeurs"
OUT_DATA = ROOT / "data" / "lycee_professeurs.json"
OUT_STATIC = ROOT / "static" / "lycee_professeurs.json"
OUT_CSV = ROOT / "static" / "lycee_professeurs.csv"
OUT_FIGURES = ROOT / "data" / "figures_lycee.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/manque-t-il-des-professeurs/"

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCE = "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_URL
GT, LP, COL = "En lycée général", "En lycée professionnel", "En collège"


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def nb(v: float, dec: int = 1) -> str:
    s = ("%." + str(dec) + "f") % v
    s = s.replace(".", ",")
    ent, _, frac = s.partition(",")
    neg = ent.startswith("-")
    ent = ent.lstrip("-")
    groupes = []
    while len(ent) > 3:
        groupes.insert(0, ent[-3:])
        ent = ent[:-3]
    groupes.insert(0, ent)
    s = ("-" if neg else "") + " ".join(groupes) + ("," + frac if frac else "")
    return s


# ------------------------------------------------------------------ données
def lire():
    for ligne in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        h, nom_ = ligne.split()
        if hashlib.sha256((SRC / nom_.lstrip("*")).read_bytes()).hexdigest() != h:
            fail("empreinte de %s differente de SHA256SUMS : extrait modifie hors du depot de recherche" % nom_)
    return json.loads((SRC / "extrait.json").read_text(encoding="utf-8"))


def calcul(X):
    ed = {int(a): v for a, v in X["ed_gt"].items()}
    v1 = {r["annee"]: r for r in X["v1"]}
    a0, a1 = min(v1), max(v1)
    h4 = X["d4"]["2024-2025"]["par_etablissement"]
    h3 = X["d4"]["2023-2024"]["par_etablissement"]
    org = lambda h: h["fermeture"] + h["systeme"] + h["formation"]
    s5 = X["d2"]["serie_5"]
    maths, pc = s5["Capes de mathématiques"], s5["Capes de physique-chimie"]
    nat = {int(a): v for a, v in X["d2"]["externes_national"].items()}
    contr = {int(a): v for a, v in X["d2"]["contractuels"].items()}
    c1 = {int(a): v for a, v in X["c1"].items()}
    c3 = {int(a): v for a, v in X["c3"].items()}
    acad = X["d3"]["es_gt"]
    metro = {k: v for k, v in acad.items() if not k.startswith(tuple(X["d3"]["drom"]))}
    disc = sorted(X["v4"]["es_disciplines"], key=lambda d: d["es"])
    disc_ok = [d for d in disc if not d["discipline"].startswith(("Total", "Toutes", "Disciplines", "Enseignement"))]
    grp = X["v4"]["groupes"]
    e4, e5, e7, e9 = (X["enonces"][k] for k in ("e4", "e5", "e7", "e9"))
    prix = {int(a): v for a, v in e4["prix_pib"].items()}
    p_dern = max(prix)
    e4_nom = e4["credits_2027"] / e4["credits_2017"] - 1
    e4_prix = prix[p_dern] / prix[2017] - 1
    e4_reel = (1 + e4_nom) / (1 + e4_prix) - 1
    e4_el = e4["eleves_2027"] / e4["eleves_2017"] - 1
    e4_par_el = (1 + e4_reel) / (1 + e4_el) - 1
    ecart_base = e7["enonce_2025"] - nat[max(nat)]
    return dict(
        ed=ed, ed_max_avant=max(v for a, v in ed.items() if a <= 2015),
        ed_an_max_avant=max((a for a, v in ed.items() if a <= 2015), key=lambda a: ed[a]),
        ed_depuis20=[ed[a] for a in ed if a >= 2020], ed_dern=max(ed),
        v1=v1, a0=a0, a1=a1,
        el_var=v1[a1]["eleves"] / v1[a0]["eleves"] - 1, div_var=v1[a1]["divisions"] / v1[a0]["divisions"] - 1,
        he_var=v1[a1]["he"] / v1[a0]["he"] - 1, he_var20=v1[a1]["he"] / v1[2020]["he"] - 1,
        he_2010=v1[2010]["he"], he_2015=v1[2015]["he"],
        pub=X["v3"]["public"], prive=X["v3"]["prive"], tr=X["v3"]["tranches"],
        h4=h4, h3=h3, org4=org(h4[GT]), org3=org(h3[GT]), org4_col=org(h4[COL]), org4_lp=org(h4[LP]),
        maths=maths, pc=pc, agreg_maths=s5["Agrégation de mathématiques"],
        nat=nat, contr=contr, ecart_base=ecart_base, e7=e7, enonce_base_depp=e7["enonce_2026"] - ecart_base,
        c1=c1, c1_max_an=max(c1, key=c1.get), c3=c3,
        acad=acad, metro=metro, disc=disc_ok, grp=grp,
        es_toutes=next(d["es"] for d in X["v4"]["es_disciplines"] if d["discipline"] == "Toutes disciplines"),
        e4=e4, e4_nom=e4_nom, e4_prix=e4_prix, e4_reel=e4_reel, e4_el=e4_el, e4_par_el=e4_par_el, p_dern=p_dern,
        e5=e5, e5_f=e5["rcd_2024"] / e5["rcd_2022"], e9=e9,
        sd=X["d4"]["second_degre"], releve=X["releve_le"],
        e1=X["enonces"]["e1"],
        detail={"2024": X["d2"]["detail_2024"], "2025": X["d2"]["detail_2025"]},
    )


def mutation(c):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m == "organisation":   # les absences individuelles l'emporteraient au lycée en 2024-2025
        c["h4"] = json.loads(json.dumps(c["h4"]))
        c["h4"][GT]["individuelles"] = 7.0
    elif m == "classes":      # la part des divisions de 35+ serait remontée au-dessus de 2015
        c["tr"] = json.loads(json.dumps(c["tr"]))
        c["tr"]["2025"]["div_35"] = 25.0
    elif m == "concours":     # le CAPES de mathématiques serait pourvu à 85 % en 2024
        c["maths"] = dict(c["maths"], **{"2024": 85.0})
    elif m == "ocde":         # l'écart avec l'OCDE ne se resserrerait plus
        c["c3"] = {a: (dict(v, FRA=v["OECD"] * 1.6) if a == max(c["c3"]) else v) for a, v in c["c3"].items()}
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

    h4gt = c["h4"][GT]
    # Heures non assurées
    g(round(100 / h4gt["total"]) == 10, "« une heure sur dix » : %.1f %%" % h4gt["total"])
    g(c["org4"] - 3 * 0.05 > h4gt["individuelles"] + 0.05, "« plus de la moitié tient à l'organisation, devant les absences individuelles » (2024-2025)")
    org4 = c["h4"][GT]["fermeture"] + c["h4"][GT]["systeme"] + c["h4"][GT]["formation"]
    g(org4 / h4gt["total"] > 0.5, "« plus de la moitié des heures perdues » : %.2f" % (org4 / h4gt["total"]))
    g(c["org3"] > c["h3"][GT]["individuelles"], "« même sens en 2023-2024 » (chiffres à l'unité)")
    g(abs(c["org4_col"] - c["h4"][COL]["individuelles"]) <= 0.5, "« au collège, les deux s'équilibrent » : %.1f / %.1f" % (c["org4_col"], c["h4"][COL]["individuelles"]))
    g(h4gt["fermeture"] > c["h4"][COL]["fermeture"] and h4gt["fermeture"] > c["h4"][LP]["fermeture"], "« le lycée GT ferme davantage »")
    g(abs(h4gt["total"] - 10) <= 0.5, "énoncé « 10 % des heures dans les lycées » : exact à 0,5 point")
    # Classes
    g(min(c["ed_depuis20"]) > c["ed_max_avant"], "« depuis 2020, au-dessus de tout niveau de 1994-2015 »")
    g(min(c["ed_depuis20"]) >= 30, "« plus de 30 élèves depuis 2020 »")
    g(max(c["ed_depuis20"]) - min(c["ed_depuis20"]) <= 0.4, "« stable depuis 2020 »")
    g(c["tr"]["2025"]["div_35"] < c["tr"]["2015"]["div_35"], "« les divisions de 35 et plus sont moins fréquentes qu'en 2015 »")
    g(c["tr"]["2025"]["div_30"] > c["tr"]["2015"]["div_30"] + 3, "« les divisions de 30 et plus sont plus fréquentes qu'en 2015 »")
    g(62 <= c["tr"]["2025"]["div_30"] <= 71, "« deux divisions sur trois » : %.1f" % c["tr"]["2025"]["div_30"])
    g(22 <= c["pub"]["eleves_35"] < 25, "« près d'un lycéen du public sur quatre » : %.1f" % c["pub"]["eleves_35"])
    g(c["pub"]["vecue"] > c["pub"]["moyenne"] + 0.5, "« la classe vécue est plus grande que la moyenne »")
    for niv in ("Première générale", "Terminale générale"):
        g(65 <= c["grp"][niv][str(max(map(int, c["grp"][niv])))] < 75, "« sept heures sur dix en groupe » : %s" % niv)
    g(c["grp"]["Première générale"]["2019"] - c["grp"]["Première générale"]["2018"] > 10, "« saut de 2019 en première générale »")
    # Heures et dépense
    g(c["he_var"] <= -0.04, "« les heures par élève ont baissé depuis %d » : %.3f" % (c["a0"], c["he_var"]))
    g(abs(c["he_var20"]) <= 0.02, "« stables depuis 2020 » : %.3f" % c["he_var20"])
    g(c["he_2010"] - c["he_2015"] >= 0.05, "« la baisse s'est faite entre 2010 et 2015 »")
    g(c["el_var"] > 0.03 and c["div_var"] < 0, "« plus d'élèves, moins de divisions »")
    g(c["c1_max_an"] == 2010 and c["c1"][max(c["c1"])] < 0.95 * c["c1"][2010], "« dépense par lycéen sous son maximum de 2010 »")
    rap = {a: v["FRA"] / v["OECD"] for a, v in c["c3"].items()}
    g(all(r > 1.10 for r in rap.values()), "« au-dessus de l'OCDE chaque année »")
    g(rap[max(rap)] < rap[min(rap)] - 0.1, "« l'écart se resserre »")
    # Concours
    for nom, s in (("mathématiques", c["maths"]), ("physique-chimie", c["pc"])):
        g(all(s[a] < 80 for a in ("2023", "2024", "2025")), "« moins de quatre postes sur cinq, trois sessions » : CAPES %s" % nom)
    for cle in ("Capet / sciences industrielles de l’ingénieur", "CAPLP / mathématiques-physique chimie"):
        g(all(c["detail"][an_][cle]["couverture"] < 85 for an_ in ("2024", "2025")), "« d'autres concours sous 85 %% en 2024 et 2025 » : %s" % cle)
    g(c["agreg_maths"]["2023"] >= 85, "« l'agrégation de mathématiques ne remplit pas le critère des trois sessions »")
    g(c["enonce_base_depp"] > max(v for a, v in c["nat"].items() if 2015 <= a <= 2025), "« 96,1 % : au-dessus des années publiées depuis 2015 »")
    g(c["enonce_base_depp"] < min(c["nat"][2005], c["nat"][2010]), "« sous 2005 et 2010 »")
    g(c["contr"][max(c["contr"])] - c["contr"][min(c["contr"])] >= 2, "« la part des contractuels monte »")
    # Académies
    g(max(c["metro"].values()) - min(c["metro"].values()) >= 2, "« les académies ne sont pas à égalité »")
    # Énoncés
    g(c["e4_reel"] > 0 and c["e4_par_el"] > c["e4_reel"], "E4 : majorants positifs, par élève plus fort")
    g(2.5 <= c["e5_f"] < 2.95, "E5 « multiplié par environ 2,6, pas tout à fait triplé » : %.2f" % c["e5_f"])
    var = c["sd"]["total"]["2024-2025"] - c["sd"]["total"]["2022-2023"]
    g(-2.5 < var < 0, "E6 « baisse de 1 point environ sur la mesure DEPP, non de 3 » : %.1f" % var)
    return n


# ------------------------------------------------------------------ affichage
def affichage(c):
    h4gt, h4col, h4lp = c["h4"][GT], c["h4"][COL], c["h4"][LP]
    rap = {a: v["FRA"] / v["OECD"] for a, v in c["c3"].items()}
    a_rmin, a_rmax = min(rap), max(rap)
    nat = c["nat"]
    nat_max_an = max((a for a in nat if 2015 <= a <= 2025), key=nat.get)
    lo_m, hi_m = min(c["metro"], key=c["metro"].get), max(c["metro"], key=c["metro"].get)
    lo_a, hi_a = min(c["acad"], key=c["acad"].get), max(c["acad"], key=c["acad"].get)
    dmin, dmax = c["disc"][0], c["disc"][-1]
    disc_txt = {d["discipline"]: d["es"] for d in c["disc"]}
    an_grp = str(max(map(int, c["grp"]["Première générale"])))
    return {
        # heures
        "h_total": nb(h4gt["total"]), "h_un_sur": str(round(100 / h4gt["total"])),
        "h_un_sur_l": {8: "huit", 9: "neuf", 10: "dix", 11: "onze", 12: "douze"}[round(100 / h4gt["total"])],
        "h_ferm": nb(h4gt["fermeture"]), "h_sys": nb(h4gt["systeme"]), "h_form": nb(h4gt["formation"]),
        "h_indiv": nb(h4gt["individuelles"]), "h_nr": nb(h4gt["non_remplacement"]),
        "h_org": nb(c["org4"]), "h_org_part": str(round(100 * c["org4"] / h4gt["total"])),
        "h3_total": nb(c["h3"][GT]["total"], 0), "h3_org": nb(c["org3"], 0), "h3_indiv": nb(c["h3"][GT]["individuelles"], 0),
        "col_total": nb(h4col["total"]), "col_indiv": nb(h4col["individuelles"]), "col_org": nb(c["org4_col"]),
        "lp_total": nb(h4lp["total"]), "lp_indiv": nb(h4lp["individuelles"]), "lp_org": nb(c["org4_lp"]),
        "sd_total": nb(c["h4"]["Ensemble"]["total"]), "sd_nr": nb(c["h4"]["Ensemble"]["non_remplacement"]),
        "sd_total22": nb(c["sd"]["total"]["2022-2023"], 0), "sd_var": nb(c["sd"]["total"]["2024-2025"] - c["sd"]["total"]["2022-2023"]),
        "sd_indiv22": nb(c["sd"]["individuelles"]["2022-2023"]), "sd_indiv24": nb(c["sd"]["individuelles"]["2024-2025"]),
        # classes
        "ed": nb(c["ed"][c["ed_dern"]]), "ed_an": str(c["ed_dern"]), "ed_max_avant": nb(c["ed_max_avant"]),
        "ed_an_max_avant": str(c["ed_an_max_avant"]), "ed_2021": nb(c["ed"][2021]), "ed_1994": nb(c["ed"][1994]),
        "ed_pub": nb(c["pub"]["moyenne"]), "vecue_pub": nb(c["pub"]["vecue"]), "ed_prive": nb(c["prive"]["moyenne"]),
        "vecue_prive": nb(c["prive"]["vecue"]), "el35_pub": nb(c["pub"]["eleves_35"]), "el30_pub": nb(c["pub"]["eleves_30"], 0),
        "el35_prive": nb(c["prive"]["eleves_35"]), "max_pub": str(c["pub"]["max"]),
        "div30_15": nb(c["tr"]["2015"]["div_30"]), "div30_25": nb(c["tr"]["2025"]["div_30"]),
        "div35_15": nb(c["tr"]["2015"]["div_35"]), "div35_25": nb(c["tr"]["2025"]["div_35"]),
        "es_gt": nb(c["es_toutes"]),
        "es_min": nb(dmin["es"]), "es_min_disc": dmin["discipline"].lower(), "es_max": nb(dmax["es"]), "es_max_disc": dmax["discipline"],
        "es_maths": nb(disc_txt["Mathématiques"]), "es_hg": nb(disc_txt["Histoire-Géographie"]), "es_philo": nb(disc_txt["Philosophie"]),
        "es_ses": nb(disc_txt["Sciences économiques et sociales"]), "es_svt": nb(disc_txt["Sciences de la Vie et de la Terre"]),
        "grp_1g_18": nb(c["grp"]["Première générale"]["2018"]), "grp_1g_19": nb(c["grp"]["Première générale"]["2019"]),
        "grp_1g": nb(c["grp"]["Première générale"][an_grp]), "grp_tg": nb(c["grp"]["Terminale générale"][an_grp]),
        "grp_2nde": nb(c["grp"]["Seconde GT"][an_grp]), "grp_an": an_grp,
        # moyens
        "a0": str(c["a0"]), "a1": str(c["a1"]), "el_var": nb(100 * c["el_var"]), "div_var": nb(100 * c["div_var"]),
        "he_var": nb(100 * c["he_var"], 0), "he_a0": nb(c["v1"][c["a0"]]["he"], 2), "he_a1": nb(c["v1"][c["a1"]]["he"], 2),
        "he_2010": nb(c["he_2010"], 2), "he_2015": nb(c["he_2015"], 2),
        "c1_max": nb(c["c1"][2010], 0), "c1_dern": nb(c["c1"][max(c["c1"])], 0), "c1_an": str(max(c["c1"])),
        "c1_var": nb(100 * (c["c1"][max(c["c1"])] / c["c1"][2010] - 1), 0),
        "c3_an": str(max(c["c3"])), "c3_fra": nb(c["c3"][max(c["c3"])]["FRA"], 0), "c3_oecd": nb(c["c3"][max(c["c3"])]["OECD"], 0),
        "c3_pct": nb(100 * (rap[max(rap)] - 1), 0), "c3_pct_debut": nb(100 * (rap[a_rmin] - 1), 0), "c3_debut": str(a_rmin),
        "e4_17": nb(c["e4"]["credits_2017"]), "e4_27": nb(c["e4"]["credits_2027"], 0), "e4_nom": nb(100 * c["e4_nom"], 0),
        "e4_prix": nb(100 * c["e4_prix"], 0), "e4_prix_an": str(c["p_dern"]), "e4_reel": nb(100 * c["e4_reel"], 0),
        "e4_el": nb(100 * c["e4_el"], 0), "e4_par_el": nb(100 * c["e4_par_el"], 0),
        # concours
        "m23": nb(c["maths"]["2023"]), "m24": nb(c["maths"]["2024"]), "m25": nb(c["maths"]["2025"]),
        "pc23": nb(c["pc"]["2023"]), "pc24": nb(c["pc"]["2024"]), "pc25": nb(c["pc"]["2025"]),
        "agm23": nb(c["agreg_maths"]["2023"]),
        "nat15": nb(nat[2015]), "nat22": nb(nat[2022]), "nat25": nb(nat[max(nat)]), "nat_max": nb(nat[nat_max_an]),
        "nat_max_an": str(nat_max_an), "nat05": nb(nat[2005]), "nat10": nb(nat[2010]),
        "e7": nb(c["e7"]["enonce_2026"]), "e7_25": nb(c["e7"]["enonce_2025"]), "e7_base": nb(c["enonce_base_depp"]),
        "e7_ecart": nb(c["ecart_base"]),
        "contr_debut": nb(c["contr"][min(c["contr"])]), "contr_fin": nb(c["contr"][max(c["contr"])]),
        "contr_a0": str(min(c["contr"])), "contr_a1": str(max(c["contr"])),
        # académies
        "ac_lo": lo_m, "ac_lo_v": nb(c["metro"][lo_m]), "ac_hi": hi_m, "ac_hi_v": nb(c["metro"][hi_m]),
        "ac_ecart": nb(c["metro"][hi_m] - c["metro"][lo_m]), "ac_lo_all": lo_a, "ac_lo_all_v": nb(c["acad"][lo_a]),
        # énoncés
        "e5_22": nb(c["e5"]["rcd_2022"]), "e5_23": nb(c["e5"]["rcd_2023"]), "e5_24": nb(c["e5"]["rcd_2024"]),
        "e5_f": nb(c["e5_f"]), "e5_non": nb(100 - c["e5"]["rcd_2024"], 0),
        "e9_j": nb(c["e9"]["journees_2023"], 0), "e9_h": nb(c["e9"]["hausse_depuis_2018"]),
        "e10_2d": nb(abs(c["e4"]["eleves_2026_2d_variation"]), 0),
        "e1_snes": nb(c["e1"]["snes"], 0), "e1_snpden": nb(c["e1"]["snpden"], 0),
    }


# ------------------------------------------------------------------ figures
def esc(s: str) -> str:
    return html.escape(s, quote=False)


def tete(fid, titre, desc, h):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h, fid, fid, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (fid, esc(titre), fid, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h),
            '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(titre))]


def pied(e, y0, source, note):
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID))
    for k, (tx, col) in enumerate([(source, INK2), (note, INK2), (LICENCE, MUTED)]):
        e.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, col, esc(tx)))
    e.append("</svg>")
    return "\n".join(e)


FIG = {
    "heures": dict(
        titre="Une heure de cours sur dix n'a pas lieu au lycée : pourquoi ?",
        source="DEPP, enquête sur le temps d'enseignement non assuré (Note d'Information 26-14), établissements publics, 2024-2025",
        note="En % des heures d'enseignement prévues. Absences individuelles : maladie, congés, grèves, convenances. Enquête déclarative par échantillon.",
        montre="Au lycée général et technologique, plus de la moitié des heures perdues en 2024-2025 tient à l'organisation (fermetures pour examens, enseignants mobilisés par les examens ou les commissions, formation) ; au collège, les deux parts s'équilibrent."),
    "classes": dict(
        titre="Élèves par classe au lycée général et technologique, 1994-{ed_an}",
        source="DEPP, Repères et références statistiques 2026, fiches 2.05 et 2.06 (public et privé sous contrat)",
        note="Nombre moyen d'élèves par division (classe entière). Devant un professeur, les élèves sont moins nombreux : une partie des heures se fait en groupe.",
        montre="Depuis 2020, les classes de lycée GT comptent plus de 30 élèves en moyenne, un niveau jamais atteint de 1994 à 2015 ; la moyenne est stable depuis."),
    "concours": dict(
        titre="Part des postes pourvus aux concours externes d'enseignants, 2008-2025",
        source="DEPP, Repères et références statistiques 2026, fiches 9.27 et 9.28 (concours externes, enseignement public)",
        note="Admis rapportés aux postes offerts. Ensemble des concours externes d'enseignants du second degré : années publiées seulement.",
        montre="Les CAPES de mathématiques et de physique-chimie restent sous quatre postes pourvus sur cinq aux trois dernières sessions, quand l'ensemble des concours se redresse."),
}


def fig_heures(c, A):
    t = FIG["heures"]
    lignes = [("Lycée général et technologique", c["h4"][GT]), ("Lycée professionnel", c["h4"][LP]), ("Collège", c["h4"][COL])]
    desc = ("Barres empilées, 2024-2025, en %% des heures prévues. Lycée GT : %s au total, dont absences individuelles %s, "
            "examens et commissions %s, fermeture %s, formation %s. Lycée professionnel : %s. Collège : %s, dont absences individuelles %s."
            % (A["h_total"], A["h_indiv"], A["h_sys"], A["h_ferm"], A["h_form"], A["lp_total"], A["col_total"], A["col_indiv"]))
    h = 270
    e = tete("lyc-h", t["titre"], desc, h + 52)
    X0, X1 = 200, 690
    vmax = 12.0
    sx = lambda v: (X1 - X0) * v / vmax
    segs = [("individuelles", "Absences individuelles", ORANGE, 1.0), ("systeme", "Examens, commissions", BLEU, 1.0),
            ("fermeture", "Fermeture (examens surtout)", BLEU, 0.62), ("formation", "Formation", BLEU, 0.35)]
    # légende
    lx = 0
    for k, (_, lib, col, op) in enumerate(segs):
        e.append('<rect x="%d" y="34" width="11" height="11" fill="%s" opacity="%s"/>' % (lx, col, op))
        e.append('<text x="%d" y="44" font-size="10.5" fill="%s">%s</text>' % (lx + 15, INK2, esc(lib)))
        lx += 22 + int(6.1 * len(lib)) + 12
    for i, (lib, v) in enumerate(lignes):
        y = 78 + i * 58
        e.append('<text x="0" y="%d" font-size="11.5" fill="%s" font-weight="%s">%s</text>' % (y + 17, INK, 600 if i == 0 else 400, esc(lib)))
        x = X0
        for cle, _, col, op in segs:
            w = sx(v[cle])
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="26" fill="%s" opacity="%s" stroke="#ffffff" stroke-width="1"/>' % (x, y, w, col, op))
            if w > 26:
                fc = "#ffffff" if (col == ORANGE or op > 0.5) else INK
                e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (x + w / 2, y + 17, fc, nb(v[cle])))
            x += w
        e.append('<text x="%.1f" y="%d" font-size="11.5" font-weight="600" fill="%s">%s %%</text>' % (x + 6, y + 17, INK, nb(v["total"])))
    return pied(e, h + 2, t["source"], t["note"])


def fig_classes(c, A):
    t = {k: v.format(**A) for k, v in FIG["classes"].items()}
    ed = c["ed"]
    a0, a1 = min(ed), max(ed)
    desc = ("Courbe du nombre moyen d'élèves par classe au lycée GT, de %d à %d : %s en %d, %s en %s (maximum d'avant 2016), "
            "%s en 2021, %s en %d." % (a0, a1, A["ed_1994"], a0, A["ed_max_avant"], A["ed_an_max_avant"], A["ed_2021"], A["ed"], a1))
    h = 270
    e = tete("lyc-c", t["titre"], desc, h + 52)
    X0, X1, TOP, BAS = 44, 690, 44, 240
    vmin, vmax = 26, 31
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)
    for gv in range(vmin, vmax + 1):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (X0, Y(gv), X1, Y(gv), GRID))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d</text>' % (X0 - 6, Y(gv) + 3, MUTED, gv))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity="0.25"/>' % (X(2020) - 4, TOP, X(a1) - X(2020) + 8, BAS - TOP, GRIS_CLAIR))
    e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">depuis 2020 : plus de 30</text>' % ((X(2020) + X(a1)) / 2, TOP - 6, INK2))
    for a in range(1995, a1 + 1, 5):
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 14, MUTED, a))
    d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(v)) for k, (a, v) in enumerate(sorted(ed.items())))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>' % (d, BLEU))
    for a in (a0, c["ed_an_max_avant"], a1):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s"/>' % (X(a), Y(ed[a]), BLEU))
        e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (X(a), Y(ed[a]) + 16, INK, nb(ed[a])))
    return pied(e, h + 2, t["source"], t["note"])


def fig_concours(c, A):
    t = FIG["concours"]
    m = {int(a): v for a, v in c["maths"].items()}
    p = {int(a): v for a, v in c["pc"].items()}
    nat = c["nat"]
    a0, a1 = 2008, max(m)
    desc = ("Courbes 2008-%d de la part des postes pourvus. CAPES de mathématiques : %s %% en 2023, %s en 2024, %s en 2025. "
            "CAPES de physique-chimie : %s, %s, %s. Ensemble des concours externes (années publiées) : %s %% en 2015, %s en 2025."
            % (a1, A["m23"], A["m24"], A["m25"], A["pc23"], A["pc24"], A["pc25"], A["nat15"], A["nat25"]))
    h = 290
    e = tete("lyc-k", t["titre"], desc, h + 52)
    X0, X1, TOP, BAS = 44, 500, 44, 260
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * (v - 40) / 60
    for gv in range(40, 101, 20):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (X0, Y(gv), X1, Y(gv), GRID))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d %%</text>' % (X0 - 6, Y(gv) + 3, MUTED, gv))
    for a in range(2010, a1 + 1, 5):
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 14, MUTED, a))
    etiq = []
    for serie, col, lib, dash in ((nat, GRIS, "Ensemble des concours", "4 3"), (m, BLEU, "CAPES de mathématiques", ""), (p, ORANGE, "CAPES de physique-chimie", "")):
        pts = sorted((a, v) for a, v in serie.items() if a >= a0)
        d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(min(v, 100))) for k, (a, v) in enumerate(pts))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="%s" stroke-linejoin="round"/>' % (d, col, dash))
        for a, v in pts:
            if serie is nat:
                e.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>' % (X(a), Y(min(v, 100)), col))
        etiq.append([Y(pts[-1][1]) + 4, col if col != GRIS else INK2, "%s : %s %%" % (lib, nb(pts[-1][1]))])
    etiq.sort()
    for k in range(1, len(etiq)):   # étiquettes de fin : jamais à moins de 14 px l'une de l'autre
        etiq[k][0] = max(etiq[k][0], etiq[k - 1][0] + 14)
    for y, col, txt in etiq:
        e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s">%s</text>' % (X1 + 8, y, col, esc(txt)))
    return pied(e, h + 2, t["source"], t["note"])


def fiches(figs, Aff):
    out = []
    for fid in ("heures", "classes", "concours"):
        svg = figs["lycee-%s.svg" % fid]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        out.append(dict(id=fid, fichier="lycee-" + fid, titre=titre, montre=FIG[fid]["montre"], source=cart[0], precaution=cart[1]))
    return {"fr": out}


def csv_texte(c):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "variable", "cle", "valeur", "unite"])
    for a, v in sorted(c["ed"].items()):
        w.writerow(["classes", "eleves_par_division_lycee_gt", a, v, "eleves"])
    for a, r in sorted(c["v1"].items()):
        for k in ("eleves", "divisions", "he"):
            w.writerow(["eleves_divisions_heures", k, a, r[k], "eleves" if k == "eleves" else "divisions" if k == "divisions" else "heures par eleve et par semaine (public, GT et post-bac)"])
    for sect, d in (("public", c["pub"]), ("prive", c["prive"])):
        for k in ("moyenne", "vecue", "eleves_35", "eleves_30", "divisions_35"):
            w.writerow(["distribution_2025_" + sect, k, "", "%.2f" % d[k], "eleves" if k in ("moyenne", "vecue") else "%"])
    for an_, d in sorted(c["tr"].items()):
        for k, v in d.items():
            w.writerow(["tranches_divisions", k, an_, "%.1f" % v, "% des divisions"])
    for d in c["disc"]:
        w.writerow(["eleves_par_structure_discipline_2025", d["discipline"], "", d["es"], "eleves"])
    for niv, s in c["grp"].items():
        for a, v in sorted(s.items()):
            w.writerow(["heures_en_groupe", niv, a, v, "% des heures"])
    for an_, h in (("2023-2024", c["h3"]), ("2024-2025", c["h4"])):
        for etab, v in h.items():
            for k, x in v.items():
                w.writerow(["heures_non_assurees_" + an_, etab, k, x, "% des heures prevues"])
    for nom, s in (("capes_mathematiques", c["maths"]), ("capes_physique_chimie", c["pc"]), ("agregation_mathematiques", c["agreg_maths"])):
        for a, v in sorted(s.items()):
            w.writerow(["couverture_concours", nom, a, v, "%"])
    for a, v in sorted(c["nat"].items()):
        w.writerow(["couverture_concours", "externes_second_degre_ensemble", a, v, "%"])
    for a, v in sorted(c["contr"].items()):
        w.writerow(["contractuels", "part_enseignants_second_degre_public", a, v, "%"])
    for a, v in sorted(c["c1"].items()):
        w.writerow(["depense_par_lyceen_gt", "euros_2024", a, v, "EUR (prix 2024)"])
    for a, v in sorted(c["c3"].items()):
        w.writerow(["ocde_depense_publique_par_eleve_general", "France", a, v["FRA"], "USD PPA"])
        w.writerow(["ocde_depense_publique_par_eleve_general", "OCDE", a, v["OECD"], "USD PPA"])
    for k, v in sorted(c["acad"].items()):
        w.writerow(["eleves_par_structure_academie_2025", k, "", v, "eleves"])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    X = lire()
    c = calcul(X)
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    A = affichage(c)
    log("Lycee GT : heures non assurees %s %% (organisation %s, individuelles %s) ; E/D %s ; CAPES maths %s/%s/%s ; OCDE x%s"
        % (A["h_total"], A["h_org"], A["h_indiv"], A["ed"], A["m23"], A["m24"], A["m25"], A["c3_pct"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(A)))
        return 0
    import cairosvg
    figs = {"lycee-heures.svg": fig_heures(c, A), "lycee-classes.svg": fig_classes(c, A), "lycee-concours.svg": fig_concours(c, A)}
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "champ": "France ; lycée général et technologique sauf mention ; public et privé sous contrat sauf mention",
                        "source_calcul": "test décisif de l'auteur (protocole écrit avant calcul) ; extrait figé scripts/sources_lycee_professeurs/ (SHA256SUMS)"},
               "classes": {str(a): v for a, v in sorted(c["ed"].items())},
               "heures_non_assurees": {"2023-2024": c["h3"], "2024-2025": c["h4"]},
               "concours": {"capes_mathematiques": c["maths"], "capes_physique_chimie": c["pc"], "ensemble_externes": {str(a): v for a, v in c["nat"].items()}},
               "affichage": A}
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            same = {k: v for k, v in prev.items() if k not in ("releve_le", "_licence")} == json.loads(json.dumps(payload, ensure_ascii=False))
            if same and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": c["releve"],
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; sources DEPP, ministère de l'Éducation nationale, OCDE, Eurostat, Cour des comptes, Sénat", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs, A), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/lycee_professeurs.json, static/lycee_professeurs.csv, data/figures_lycee.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
