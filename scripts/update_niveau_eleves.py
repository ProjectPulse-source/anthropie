#!/usr/bin/env python3
"""update_niveau_eleves.py -- ressource « Le niveau des élèves baisse-t-il ? » (bloc École et lycée, deuxième onglet).

Découverte de la page (dépôt de pilotage de l'auteur, 06_PROMOTION/RECHERCHE_LYCEES_NIVEAU_2026-10-07, protocole écrit
avant calcul, commit 2986dfc ; verdict du 08/10/2026) : de 2015 à 2025, les jeunes de 15 ans ont reculé à PISA dans les
trois domaines ; en lecture et en sciences comme les autres pays de l'OCDE, en mathématiques plus que les trois quarts
d'entre eux ; la France perd aussi ses meilleurs élèves, et l'écart lié au milieu social s'est réduit par le haut ; sur
la même génération, le test de positionnement de seconde ne baisse pas en mathématiques quand PISA baisse (rapprochement
fait par la DEPP elle-même). Question distincte, jamais reliée à la précédente : le recrutement des professeurs.

Entrée : l'extrait FIGÉ du calcul, scripts/sources_niveau_eleves/extrait_niveau.json (écrit par extrait_niveau.py du dépôt
de recherche, qui retrouve ses valeurs phares dans les sorties du calcul), contrôlé contre SHA256SUMS. Ce générateur ne
recalcule que des rapports simples ; il met en forme et GARDE : chaque qualificatif de la prose est une condition sur les
nombres (fonction gardes) ; si l'extrait la dément, arrêt.
Mise à jour : hors module de mise à jour pour l'instant ; rendez-vous de rattrapage : printemps 2027 (test de positionnement
de seconde 2026, note de la DEPP), puis PISA 2029 (publication prévue fin 2030). Relancer calc_niveau.py, calc_profs.py
et extrait_niveau.py dans le dossier de recherche, recopier l'extrait et son empreinte, relancer ce script.
Page en français seulement (exclusion déclarée : débat, programme et statistique français).

Usage : python scripts/update_niveau_eleves.py [--check] [--mutation=maths|lecture|sommet|social|seconde|lycee|recrutement|haut_ocde|thermometres|composition|effort|amortisseur|timss_pisa]
Sorties : data/ et static/niveau_eleves.json, static/niveau_eleves.csv, data/figures_niveau.json,
          static/img/niveau-{baisse,sommet,seconde}.svg + .png
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_niveau_eleves"
OUT_DATA = ROOT / "data" / "niveau_eleves.json"
OUT_STATIC = ROOT / "static" / "niveau_eleves.json"
OUT_CSV = ROOT / "static" / "niveau_eleves.csv"
OUT_FIGURES = ROOT / "data" / "figures_niveau.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/le-niveau-des-eleves-baisse-t-il/"

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCE = "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_URL
DOM = ("lecture", "mathematiques", "sciences")
LIB = {"lecture": "Compréhension de l'écrit", "mathematiques": "Culture mathématique", "sciences": "Culture scientifique"}
COURT = {"lecture": "lect", "mathematiques": "math", "sciences": "sci"}
OC = "OECD average-35"


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
    s = ("−" if neg else "") + " ".join(groupes) + ("," + frac if frac else "")  # signe moins typographique
    return s


# noms français des pays du protocole 3 (TIMSS 4e / PISA), avec leur article ; un pays absent arrête le générateur
PAYS_FR = {"Sweden": "la Suède", "Romania": "la Roumanie", "Hong Kong (China)": "Hong Kong", "France": "la France",
           "Finland": "la Finlande", "Japan": "le Japon", "Ireland": "l'Irlande", "Italy": "l'Italie", "Hungary": "la Hongrie",
           "Qatar": "le Qatar", "Australia": "l'Australie", "Singapore": "Singapour", "Morocco": "le Maroc",
           "New Zealand": "la Nouvelle-Zélande", "Cyprus": "Chypre", "Saudi Arabia": "l'Arabie saoudite", "Israel": "Israël",
           "Lithuania": "la Lituanie", "Korea": "la Corée du Sud", "Chinese Taipei": "Taïwan", "Portugal": "le Portugal",
           "United Arab Emirates": "les Émirats arabes unis", "Chile": "le Chili", "Kazakhstan": "le Kazakhstan",
           "United States": "les États-Unis", "Georgia": "la Géorgie", "Malaysia": "la Malaisie", "Jordan": "la Jordanie"}


def liste_fr(noms):
    return noms[0] if len(noms) == 1 else ", ".join(noms[:-1]) + " et " + noms[-1]


LETTRES = {2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"}


# ------------------------------------------------------------------ données
def lire():
    for ligne in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        h, nom_ = ligne.split()
        if hashlib.sha256((SRC / nom_.lstrip("*")).read_bytes()).hexdigest() != h:
            fail("empreinte de %s differente de SHA256SUMS : extrait modifie hors du depot de recherche" % nom_)
    return json.loads((SRC / "extrait_niveau.json").read_text(encoding="utf-8"))


def calcul(X):
    P = X["pisa"]
    cl = X["echantillon_classes"]
    tot = sum(e["effectif"] for e in cl)
    part = lambda *noms: 100 * sum(e["effectif"] for e in cl if e["classe"] in noms) / tot
    p1 = {}
    for d, v in X["p1"].items():
        m0 = sum(v["avant"].values()) / len(v["avant"])
        m1 = sum(v["apres"].values()) / len(v["apres"])
        p1[d] = {"m0": m0, "m1": m1, "var": m1 / m0 - 1, "n0": len(v["avant"])}
    gen = {(g["evaluation"], g["domaine"]): g for g in X["depp_generations"]}
    return dict(
        P=P, X=X,
        lycee=part("CAP 1 an", "Seconde pro", "Seconde GT", "Première GT"),
        seconde_gt=part("Seconde GT"), seconde_pro=part("Seconde pro"),
        sec=X["seconde"], timss=X["timss_adv"], gen=gen, p1=p1, p2={int(a): v for a, v in X["p2"].items()},
        p3=X["p3"], p4=X["p4"], releve=X["releve_le"],
        t3=X["p3_timss_pisa_maths"],
        comp=X["p2_composition_sciences"], pct=X["p2_percentiles"], eff=X["p2_effort"], ae=X["p2_autres_evaluations"],
    )


def mutation(c):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m == "maths":          # la baisse française en mathématiques serait dans la moyenne des pays
        c["P"] = json.loads(json.dumps(c["P"]))
        c["P"]["mathematiques"]["n2"]["france"] = c["P"]["mathematiques"]["n2"]["mediane"]
    elif m == "lecture":      # la lecture ne serait plus « à la limite » du premier quartile
        c["P"] = json.loads(json.dumps(c["P"]))
        c["P"]["lecture"]["n2"]["france"] = c["P"]["lecture"]["n2"]["mediane"]
    elif m == "sommet":       # la France perdrait au sommet comme la moyenne de l'OCDE
        c["P"] = json.loads(json.dumps(c["P"]))
        n = c["P"]["lecture"]["niveaux"]
        n["France"]["haut25"] = n["France"]["haut15"] + n[OC]["haut25"] - n[OC]["haut15"]
    elif m == "social":       # le quart le plus favorisé aurait moins baissé que le quart le moins favorisé
        c["P"] = json.loads(json.dumps(c["P"]))
        s = c["P"]["lecture"]["social"]["France"]
        s["haut"]["2025"] = s["haut"]["2015"] - 5
    elif m == "seconde":      # le test de seconde baisserait aussi en mathématiques
        c["sec"] = json.loads(json.dumps(c["sec"]))
        c["sec"]["GT maths"]["2024"] = c["sec"]["GT maths"]["2021"] - 3
    elif m == "lycee":        # moins de sept élèves sur dix de l'échantillon PISA au lycée
        c["lycee"] = 65.0
    elif m == "recrutement":  # la sélectivité aurait monté en anglais
        c["p1"] = json.loads(json.dumps(c["p1"]))
        c["p1"]["anglais"]["var"] = 0.05
    elif m == "haut_ocde":    # le quart favorisé de l'OCDE aurait reculé autant que celui de la France
        c["P"] = json.loads(json.dumps(c["P"]))
        o = c["P"]["lecture"]["social"][OC]
        f_ = c["P"]["lecture"]["social"]["France"]
        o["haut"]["2025"] = o["haut"]["2015"] - (f_["haut"]["2015"] - f_["haut"]["2025"])
    elif m == "thermometres": # TIMSS 4e aurait baissé significativement de 2019 à 2023
        c["ae"] = json.loads(json.dumps(c["ae"]))
        c["ae"]["timss"]["TIMSS 4e maths"]["2019"]["sym"] = "p"
    elif m == "composition":  # la composition aurait contribué à la baisse au lieu de la masquer
        c["comp"] = dict(c["comp"], recompose_2025=c["comp"]["moyenne_2025"] + 5)
    elif m == "timss_pisa":   # la France serait au milieu des écarts TIMSS 4e / PISA
        c["t3"] = json.loads(json.dumps(c["t3"]))
        c["t3"]["rang"] = c["t3"]["n"] // 2
    elif m == "amortisseur":  # en France, le haut reculerait moins que le bas en mathématiques
        c["pct"] = json.loads(json.dumps(c["pct"]))
        c["pct"]["mathematiques"]["France"][4] = c["pct"]["mathematiques"]["France"][0] / 2
    elif m == "effort":       # la France ne serait que troisième pour la baisse de l'effort déclaré
        c["eff"] = dict(c["eff"], rang=3)
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

    P = c["P"]
    # protocole 2, N11 : « les évaluations par classe ne montrent pas la baisse récente » ; « sur trente ans, elles baissent aussi »
    ae = c["ae"]
    for lib in ("TIMSS CM1 maths", "TIMSS 4e maths", "TIMSS CM1 sciences", "TIMSS 4e sciences"):
        s_ = ae["timss"][lib]
        g(s_[sorted(s_)[-2]]["sym"] == "", "%s : « stable » sur la dernière période (aucun symbole de l'IEA)" % lib)
    g(not ae["pirls"]["2016"]["sup_2021"], "PIRLS : « stable » de 2016 à 2021")
    g(ae["timss"]["TIMSS 4e maths"]["1995"]["sym"] == "p", "TIMSS 4e maths : 1995 significativement au-dessus de 2023")
    g(ae["pirls"]["2001"]["sup_2021"] and ae["pirls"]["2006"]["sup_2021"], "PIRLS : 2001 et 2006 significativement au-dessus de 2021")
    # protocole 3, N12 : « l'un des quatre pays où l'écart TIMSS 4e / PISA est le plus défavorable » ; « ailleurs, souvent l'autre sens »
    p3 = c["t3"]
    g(p3["verdict"] == "TIENT" and all(v == "TIENT" for v in p3["variantes"].values()), "TIMSS / PISA : verdict robuste")
    g(p3["rang"] <= p3["n"] // 4 and p3["rang"] in LETTRES, "TIMSS / PISA : France dans le quart le plus défavorable")
    g(all(k in PAYS_FR for k in p3["pays"]), "TIMSS / PISA : nom français manquant")
    fr3 = p3["pays"]["France"]
    g(fr3["dT"] < 0 and fr3["dP"] < 0, "TIMSS / PISA : la France recule dans les deux")
    brut = sorted(v["dP"] - v["dT"] for v in p3["pays"].values())
    q1_brut = float(np.percentile(brut, 25))
    ecart_q1 = q1_brut - (fr3["dP"] - fr3["dT"])
    g(0 < ecart_q1 < 1.5 * P["mathematiques"]["dif"]["2022"]["se"], "TIMSS / PISA : écart au premier quartile « du même ordre » que la marge d'erreur")
    autre = sum(1 for v in p3["pays"].values() if v["dP"] > v["dT"])
    g(autre >= p3["n"] / 3 and p3["rho"] < 0.5, "TIMSS / PISA : « ailleurs, souvent dans l'autre sens », pas d'effet général")
    # protocole 2, N8 : la composition masque la baisse (sciences)
    cp = c["comp"]
    D_ = cp["moyenne_2025"] - cp["moyenne_2015"]
    g(cp["recompose_2025"] < cp["moyenne_2025"] and cp["recompose_2025"] - cp["moyenne_2015"] < D_,
      "composition : « à composition de 2015, la baisse serait plus forte »")
    g(1.6 <= (cp["recompose_2025"] - cp["moyenne_2015"]) / D_ < 2.0, "composition : « près de deux fois plus forte »")
    g(all(cp["scores_2025"][k] - cp["scores_2015"][k] < D_ for k in cp["scores_2015"]), "composition : « chaque classe recule davantage que la moyenne »")
    g(20 <= cp["parts_2015"]["a_troisieme_et_moins"] < 25 and cp["parts_2025"]["a_troisieme_et_moins"] < 10,
      "composition : « de près d'un quart à moins d'un dixième »")
    g(1.7 <= cp["parts_2025"]["c_seconde_pro_cap"] / cp["parts_2015"]["c_seconde_pro_cap"] < 2.0, "composition : voie professionnelle « presque doublée »")
    g(cp["moyenne_2025"] - cp["recompose_2025"] > 0, "composition : l'effet de répartition « relève » la moyenne")
    # protocole 2, N9 : dans l'OCDE, la baisse surtout en bas ; en France, tout le spectre (maths, sciences), le haut en lecture
    pct = c["pct"]
    for d in DOM:
        g(pct[d]["OCDE"][4] - pct[d]["OCDE"][0] > 10, "%s : OCDE « surtout en bas » (P90 recule bien moins que P10)" % d)
    for d in ("mathematiques", "sciences"):
        g(abs(pct[d]["France"][4] - pct[d]["France"][0]) <= 5, "%s : France « tout le spectre »" % d)
    g(pct["lecture"]["France"][4] - pct["lecture"]["France"][0] < -5, "lecture : France, « le haut davantage »")
    g(pct["mathematiques"]["France"][4] < 2 * pct["mathematiques"]["OCDE"][4], "maths : P90 France recule plus de deux fois plus que l'OCDE")
    for d in DOM:   # « dans la moyenne de l'OCDE, la baisse s'atténue quand on remonte la distribution »
        o_ = pct[d]["OCDE"]
        g(o_[0] < o_[2] < o_[4], "%s : OCDE, recul P10 > P50 > P90" % d)
    for d in ("lecture", "mathematiques"):   # « en France, le milieu et le haut reculent au moins autant que le bas »
        f_ = pct[d]["France"]
        g(f_[2] <= f_[0] and f_[4] <= f_[0], "%s : France, P50 et P90 reculent au moins autant que P10" % d)
    f_ = pct["lecture"]["France"]
    g(f_[2] <= 1.4 * f_[0] and f_[4] <= 1.4 * f_[0], "lecture : France, milieu et haut « bien davantage » que le bas")
    g(all(v < cp["s"] for v in cp["sensibilites"].values()), "composition : variantes « même sens, effet un peu plus fort »")
    f_ = pct["sciences"]["France"]
    g(f_[2] <= 0.65 * f_[0] and f_[4] <= 0.65 * f_[0], "sciences : France, « presque autant »")
    # protocole 2, N10 (descriptif) : « la plus forte baisse de l'effort déclaré des pays de l'OCDE », « deux fois la moyenne »
    ef = c["eff"]
    g(ef["rang"] == 1 and ef["france_sig"], "effort : « la plus forte baisse », significative")
    g(1.8 <= ef["france_d"] / ef["ocde_d"] < 2.2, "effort : « deux fois la moyenne de l'OCDE »")
    for d in DOM:
        x = P[d]["dif"]["2015"]
        g(x["v"] < 0 and x["sig"], "%s : « baisse depuis 2015 » exige une baisse significative" % d)
        g(P[d]["dif"]["2022"]["v"] < 0, "%s : la baisse 2022-2025 doit être une baisse" % d)
    # « sur la série longue » : lecture et mathématiques significatives, sciences non
    g(P["lecture"]["dif"][str(P["lecture"]["premier_cycle"])]["sig"] and P["lecture"]["dif"][str(P["lecture"]["premier_cycle"])]["v"] < 0,
      "lecture : baisse significative depuis le premier cycle")
    g(P["mathematiques"]["dif"][str(P["mathematiques"]["premier_cycle"])]["sig"], "mathématiques : baisse significative depuis le premier cycle")
    g(not P["sciences"]["dif"][str(P["sciences"]["premier_cycle"])]["sig"], "sciences : « pas significatif depuis 2006 »")
    g(P["sciences"]["dif"]["2022"]["sig"] is False, "sciences : « stable depuis 2022 » (non significatif)")
    g(P["lecture"]["dif"]["2022"]["sig"] and P["mathematiques"]["dif"]["2022"]["sig"], "lecture et maths : baisse significative depuis 2022")
    # N2 : mathématiques plus forte sous les trois variantes ; lecture à la limite ; sciences dans la moyenne
    m = P["mathematiques"]["n2"]
    g(m["france"] < m["q1"] and all(m["france"] < v["q1"] for v in m["variantes"].values()),
      "maths : « plus que les trois quarts des pays, quel que soit le groupe »")
    lec = P["lecture"]["n2"]
    g(lec["q1"] <= lec["france"] <= lec["q3"] and lec["france"] - lec["q1"] < 1.0, "lecture : « comme les autres, à la limite »")
    s = P["sciences"]["n2"]
    g(s["q1"] <= s["france"] <= s["q3"], "sciences : « comme les autres »")
    g(m["rang"] <= m["n"] // 4, "maths : rang dans le premier quart")
    # « l'écart au premier quartile est du même ordre que la marge d'erreur de la variation française » (maths)
    eq = m["q1"] - m["france"]
    g(0.5 <= eq / P["mathematiques"]["dif"]["2015"]["se"] <= 2.0, "maths : écart au premier quartile « du même ordre » que l'erreur type")
    # écart social : le quart favorisé recule « presque deux fois plus » que dans l'OCDE ; le quart défavorisé « comme dans l'OCDE »
    for d in ("lecture", "mathematiques"):
        fr_, oc_ = P[d]["social"]["France"], P[d]["social"][OC]
        dh = lambda s_: s_["haut"]["2015"] - s_["haut"]["2025"]
        db = lambda s_: s_["bas"]["2015"] - s_["bas"]["2025"]
        g(1.7 <= dh(fr_) / dh(oc_) < 2.0, "%s : quart favorisé « presque deux fois plus » que l'OCDE" % d)
        g(abs(db(fr_) / db(oc_) - 1) < 0.2, "%s : quart défavorisé « comme dans l'OCDE »" % d)
    # « en lecture, le même resserrement par le haut existe dans l'OCDE ; en mathématiques, les deux quarts reculent autant »
    ol, om = P["lecture"]["social"][OC], P["mathematiques"]["social"][OC]
    g(ol["haut"]["2015"] - ol["haut"]["2025"] > 1.2 * (ol["bas"]["2015"] - ol["bas"]["2025"]), "OCDE lecture : resserrement par le haut")
    g(abs((om["haut"]["2015"] - om["haut"]["2025"]) / (om["bas"]["2015"] - om["bas"]["2025"]) - 1) < 0.1, "OCDE maths : « les deux quarts reculent autant »")
    # « l'essentiel s'est produit depuis 2018 » : la baisse 2018-2025 dépasse celle de 2015-2018, dans chaque domaine
    for d in DOM:
        f_ = P[d]["france"]
        g(f_["2015"] - f_["2018"] < f_["2018"] - f_["2025"], "%s : « l'essentiel depuis 2018 »" % d)
    # « sans les N pays dont l'échantillon ne respecte pas toutes les normes » (nombre écrit en lettres)
    g(m["n"] - m["variantes"]["sans_asterisque"]["n"] in LETTRES, "nombre de pays à astérisque écrit en lettres")
    # « il ressemble à celui de l'OCDE » (hausse du bas, France moins de 1,5 fois l'OCDE) ; « plus que divisée par deux » en maths
    for d in ("lecture", "mathematiques"):
        f_, o_ = P[d]["niveaux"]["France"], P[d]["niveaux"][OC]
        g(0 < f_["bas25"] - f_["bas15"] < 1.5 * (o_["bas25"] - o_["bas15"]), "%s : hausse du bas « comme l'OCDE »" % d)
    fm = P["mathematiques"]["niveaux"]["France"]
    g(2.0 <= fm["haut15"] / fm["haut25"] < 2.5, "maths : « plus que divisée par deux »")
    # « en lecture et en mathématiques, le haut descend plus vite que le bas » (et le bas descend aussi)
    for d in ("lecture", "mathematiques"):
        so_ = P[d]["social"]["France"]
        g(so_["bas"]["2025"] < so_["bas"]["2015"], "%s : le quart bas baisse aussi" % d)
    # seconde : « retour au niveau de 2019 » en français (GT) ; « environ deux candidats par admis » dans au moins trois disciplines
    g(c["sec"]["GT francais"]["2025"] == c["sec"]["GT francais"]["2019"], "seconde : « retour au niveau de 2019 »")
    # N3 : le bas gonfle plus que le haut ne fond ; perte au sommet bien plus forte que l'OCDE en lecture et maths
    for d in DOM:
        f = P[d]["niveaux"]["France"]
        g(f["bas25"] - f["bas15"] > abs(f["haut25"] - f["haut15"]), "%s : « le bas gonfle plus que le haut ne fond »" % d)
    for d in ("lecture", "mathematiques"):
        f, o = P[d]["niveaux"]["France"], P[d]["niveaux"][OC]
        g(f["haut15"] - f["haut25"] > 2 * (o["haut15"] - o["haut25"]), "%s : « bien plus que l'OCDE » au sommet (plus du double)" % d)
    fl = P["lecture"]["niveaux"]["France"]
    g(2.5 <= fl["haut15"] / fl["haut25"] < 3.0, "lecture : « presque divisée par trois »")
    # N7 : écart social réduit significativement, et par le haut
    for d in DOM:
        so = P[d]["social"]["France"]
        g(so["var"] < 0 and so["var_sig"], "%s : « l'écart social s'est réduit » (significatif)" % d)
        g(so["haut"]["2025"] - so["haut"]["2015"] < so["bas"]["2025"] - so["bas"]["2015"], "%s : « par le haut »" % d)
    so = P["lecture"]["social"]["France"]
    g(so["haut"]["2015"] - so["haut"]["2025"] > 2 * (so["bas"]["2015"] - so["bas"]["2025"]), "lecture : « plus de deux fois plus »")
    # échantillon : « près de huit sur dix au lycée »
    g(75 <= c["lycee"] < 82, "« près de huit élèves sur dix au lycée »")
    g(c["seconde_gt"] > 50, "« plus de la moitié en seconde générale et technologique »")
    # N4 : sens contraire en mathématiques, même sens en français ; DEPP : idem en standardisé
    sec = c["sec"]
    g(sec["GT maths"]["2024"] > sec["GT maths"]["2021"] and P["mathematiques"]["dif"]["2022"]["v"] < 0,
      "seconde : « en mathématiques, le test de seconde monte quand PISA baisse »")
    g(sec["GT francais"]["2024"] < sec["GT francais"]["2021"], "seconde : « en français, les deux baissent »")
    gen = c["gen"]
    tm = next(v for k, v in gen.items() if k[0].startswith("Tests") and k[1].startswith("Math"))
    tf = next(v for k, v in gen.items() if k[0].startswith("Tests") and k[1].startswith("Fran"))
    pm = next(v for k, v in gen.items() if k[0] == "PISA" and k[1].startswith("Culture"))
    pl = next(v for k, v in gen.items() if k[0] == "PISA" and k[1].startswith("Compr"))
    g(tm["d100"] > 0 > pm["d100"] and tf["d100"] < 0 and pl["d100"] < 0, "figure DEPP : signes des écarts standardisés")
    g(abs(tf["d100"]) < abs(pl["d100"]), "figure DEPP : « en français, la seconde baisse moins que PISA »")
    # TIMSS Advanced
    g(c["timss"]["maths"]["dif"] < 0 and c["timss"]["physique"]["dif"] < 0, "TIMSS Advanced : baisse")
    # P1 : sélectivité en baisse dans les cinq disciplines, seuil d'un tiers atteint en anglais seulement
    p1 = c["p1"]
    g(all(v["var"] < 0 for v in p1.values()), "P1 : « moins de candidats par admis dans les cinq disciplines »")
    g(min(-v["var"] for v in p1.values()) > 0.2, "P1 : « d'un quart à un tiers » (au moins un cinquième partout)")
    # P2/P3 : « de moitié » ; au secondaire plus que l'OCDE, l'inverse avec le primaire
    p2 = c["p2"]
    g(1.4 <= p2[max(p2)] / p2[min(p2)] <= 1.6, "P2 : « a augmenté de moitié »")
    return n


# ------------------------------------------------------------------ affichage
def affichage(c):
    P = c["P"]
    A = {}
    for d in DOM:
        k = COURT[d]
        f = P[d]["france"]
        A[k + "_15"] = nb(f["2015"], 0)
        A[k + "_25"] = nb(f["2025"], 0)
        A[k + "_v15"] = nb(-P[d]["dif"]["2015"]["v"], 0)
        A[k + "_v22"] = nb(-P[d]["dif"]["2022"]["v"], 0)
        a0 = str(P[d]["premier_cycle"])
        A[k + "_an0"] = a0
        A[k + "_0"] = nb(f[a0], 0)
        A[k + "_vlong"] = nb(-P[d]["dif"][a0]["v"], 0)
        A[k + "_ocde_v15"] = nb(-P[d]["ocde35_dif2015"], 0)
        n2 = P[d]["n2"]
        A[k + "_rang"] = str(n2["rang"])
        A[k + "_mieux"] = str(n2["n"] - n2["rang"])
        A[k + "_q1"] = nb(-n2["q1"], 0)
        A[k + "_med"] = nb(-n2["mediane"], 0)
        nv, no = P[d]["niveaux"]["France"], P[d]["niveaux"][OC]
        for kk in ("bas15", "bas25", "haut15", "haut25"):
            A[k + "_" + kk] = nb(nv[kk])
            A[k + "_o" + kk] = nb(no[kk])
        A[k + "_dbas"] = nb(nv["bas25"] - nv["bas15"], 0)
        so, soo = P[d]["social"]["France"], P[d]["social"][OC]
        A[k + "_ec15"] = nb(so["ecart"]["2015"], 0)
        A[k + "_ec25"] = nb(so["ecart"]["2025"], 0)
        A[k + "_oec25"] = nb(soo["ecart"]["2025"], 0)
        A[k + "_qh"] = nb(so["haut"]["2015"] - so["haut"]["2025"], 0)
        A[k + "_qb"] = nb(so["bas"]["2015"] - so["bas"]["2025"], 0)
        A[k + "_oqh"] = nb(soo["haut"]["2015"] - soo["haut"]["2025"], 0)
        A[k + "_oqb"] = nb(soo["bas"]["2015"] - soo["bas"]["2025"], 0)
    A["math_ecart_q1"] = nb(P["mathematiques"]["n2"]["q1"] - P["mathematiques"]["n2"]["france"], 0)
    A["math_se"] = nb(P["mathematiques"]["dif"]["2015"]["se"], 0)
    A["n_ocde"] = str(P["mathematiques"]["n2"]["n"])
    A["n_etoile"] = LETTRES[P["mathematiques"]["n2"]["n"] - P["mathematiques"]["n2"]["variantes"]["sans_asterisque"]["n"]]
    A["n_autres"] = str(P["mathematiques"]["n2"]["n"] - 1)
    A["lycee"] = nb(c["lycee"], 0)
    A["seconde_gt"] = nb(c["seconde_gt"], 0)
    A["seconde_pro"] = nb(c["seconde_pro"], 0)
    sec = c["sec"]
    for cle, k in (("GT francais", "sf"), ("GT maths", "sm"), ("Pro francais", "pf"), ("Pro maths", "pm")):
        for a in ("2019", "2021", "2024", "2025"):
            A["%s_%s" % (k, a[2:])] = nb(sec[cle][a], 0)
    A["sm_v"] = nb(sec["GT maths"]["2024"] - sec["GT maths"]["2021"], 0)
    A["sf_v"] = nb(sec["GT francais"]["2021"] - sec["GT francais"]["2024"], 0)
    for (ev, dom), v in c["gen"].items():
        k = ("t" if ev.startswith("Tests") else "p") + ("m" if dom.startswith(("Math", "Culture")) else "f")
        A["g_" + k] = nb(abs(v["d100"]), 0)
    for d, t in c["timss"].items():
        A["timss_%s_95" % d[:4]] = str(t["1995"])
        A["timss_%s_15" % d[:4]] = str(t["2015"])
        A["timss_%s_v" % d[:4]] = str(-t["dif"])
    p1 = c["p1"]
    A["p1_min"] = nb(-100 * max(v["var"] for v in p1.values()), 0)
    A["p1_max"] = nb(-100 * min(v["var"] for v in p1.values()), 0)
    p2 = c["p2"]
    A["contr_a0"], A["contr_a1"] = str(min(p2)), str(max(p2))
    A["contr_0"], A["contr_1"] = nb(p2[min(p2)]), nb(p2[max(p2)])
    A["nq_fr"] = nb(c["p3"]["France"]["secondaire"])
    A["nq_ocde"] = nb(c["p3"]["OECD average"]["secondaire"])
    # protocole 3
    p3 = c["t3"]
    tri = [k for k, _ in sorted(p3["pays"].items(), key=lambda kv: kv[1]["G"])]
    i = tri.index("France")
    A["t3_n"] = str(p3["n"])
    A["t3_rang_l"] = LETTRES[p3["rang"]]
    A["t3_avant"] = liste_fr([PAYS_FR[k] for k in tri[:i]])
    A["t3_apres"] = liste_fr([PAYS_FR[k] for k in tri[i + 1:i + 4]])
    A["t3_fr_dt"] = nb(-p3["pays"]["France"]["dT"], 0)
    A["t3_fr_dp"] = nb(-p3["pays"]["France"]["dP"], 0)
    A["t3_autre"] = str(sum(1 for v in p3["pays"].values() if v["dP"] > v["dT"]))
    # protocole 2
    ae = c["ae"]
    for lib, k in (("TIMSS CM1 maths", "tcm1"), ("TIMSS 4e maths", "t4e"), ("TIMSS CM1 sciences", "tcm1s"), ("TIMSS 4e sciences", "t4es")):
        for a, v in ae["timss"][lib].items():
            A["%s_%s" % (k, a[2:])] = str(v["score"])
    for a, v in ae["pirls"].items():
        A["pirls_" + a[2:]] = nb(v["score"], 0)
    cp = c["comp"]
    A["comp_retard15"] = nb(cp["parts_2015"]["a_troisieme_et_moins"], 0)
    A["comp_retard25"] = nb(cp["parts_2025"]["a_troisieme_et_moins"], 0)
    A["comp_pro15"] = nb(cp["parts_2015"]["c_seconde_pro_cap"], 0)
    A["comp_pro25"] = nb(cp["parts_2025"]["c_seconde_pro_cap"], 0)
    A["comp_baisse_obs"] = nb(cp["moyenne_2015"] - cp["moyenne_2025"], 0)
    A["comp_baisse_rec"] = nb(cp["moyenne_2015"] - cp["recompose_2025"], 0)
    dcl = [cp["scores_2015"][k] - cp["scores_2025"][k] for k in cp["scores_2015"]]
    A["comp_cl_min"], A["comp_cl_max"] = nb(min(dcl), 0), nb(max(dcl), 0)
    A["comp_effet"] = nb(cp["moyenne_2025"] - cp["recompose_2025"], 0)
    A["comp_gt"] = nb(cp["scores_2015"]["b_seconde_gt"] - cp["scores_2025"]["b_seconde_gt"], 0)
    pct = c["pct"]
    for d in DOM:
        k = COURT[d]
        A[k + "_p50"], A[k + "_op50"] = nb(-pct[d]["France"][2], 0), nb(-pct[d]["OCDE"][2], 0)
        A[k + "_p10"], A[k + "_p90"] = nb(-pct[d]["France"][0], 0), nb(-pct[d]["France"][4], 0)
        A[k + "_op10"], A[k + "_op90"] = nb(-pct[d]["OCDE"][0], 0), nb(-pct[d]["OCDE"][4], 0)
    ef = c["eff"]
    A["eff_22"], A["eff_25"] = nb(ef["france"]["2022"], 2), nb(ef["france"]["2025"], 2)
    A["eff_d"], A["eff_od"] = nb(-ef["france_d"], 2), nb(-ef["ocde_d"], 2)
    A["eff_n"] = str(ef["n_pays"])
    return A


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
    "baisse": dict(
        titre="PISA, 2015-2025 : la France parmi les {n_ocde} pays de l'OCDE",
        source="OCDE, PISA 2025, volume I, tableaux I.B1.2a.36 à 38 (variation du score moyen entre 2015 et 2025)",
        note="Chaque point est un pays membre de l'OCDE. Bande bleue : la moitié centrale des pays (du premier au troisième quartile).",
        montre="En lecture et en sciences, la baisse française est dans la moitié centrale des pays de l'OCDE, la lecture pratiquement à sa frontière ; en mathématiques, elle compte, sur les estimations ponctuelles, parmi le quart des plus fortes."),
    "composition": dict(
        titre="PISA, culture scientifique : la répartition entre classes masque une partie de la baisse",
        source="DEPP, Notes d'Information 16-37 (PISA 2015, figure 3) et 26-39 (PISA 2025, figure 10 web) ; calcul de l'auteur",
        note="Moyenne des classes pondérée par leur part. Ne neutralise pas les changements de population à l'intérieur de chaque classe.",
        montre="Avec la répartition entre classes de 2015, le score de 2025 serait plus bas : la baisse serait près de deux fois plus forte, parce qu'à 15 ans moins d'élèves sont encore au collège."),
    "thermometres": dict(
        titre="Quatre évaluations, leur dernière variation en France",
        source="IEA (TIMSS 2023, rapport international) ; DEPP (PIRLS 2021, NI 23-21 ; test de positionnement de seconde, NI 26-22) ; OCDE (PISA 2025)",
        note="Chaque évaluation a son échelle : les points ne se comparent pas d'une ligne à l'autre. Point plein : significativité publiée ; point creux : test de seconde, sans test publié.",
        montre="Sur leur dernière période, PIRLS en CM1 et TIMSS en CM1 et en quatrième sont stables ; le test d'entrée en seconde monte en mathématiques ; PISA, à 15 ans, baisse nettement."),
    "sommet": dict(
        titre="Les élèves en difficulté et les meilleurs élèves, 2015 et 2025",
        source="OCDE, PISA 2025, volume I, tableaux I.B1.2a.34 et 35 ; moyenne de l'OCDE sur 35 pays comparables",
        note="En % des élèves de 15 ans. En difficulté : sous le niveau 2. Meilleurs élèves : niveaux 5 et 6.",
        montre="La part des élèves en difficulté augmente en France à peu près comme dans l'OCDE ; la part des meilleurs élèves y baisse bien davantage, surtout en lecture."),
    "seconde": dict(
        titre="Une même génération, deux évaluations : écart entre 2021-2022 et 2024-2025",
        source="DEPP, Note d'Information 26-40, figure 11 web (tests de positionnement de seconde 2021 et 2024 ; PISA 2022 et 2025)",
        note="Écart entre deux générations d'élèves, en centièmes d'écart-type (d de Cohen), calculé par la DEPP. Seconde : deux voies.",
        montre="En français, le test de seconde et PISA baissent tous les deux ; en mathématiques, le test de seconde monte quand PISA baisse."),
}


def fig_thermometres(c, A):
    t = FIG["thermometres"]
    ae, P, sec = c["ae"], c["P"], c["sec"]
    lignes = []
    for lib, pop, k in (("PIRLS, compréhension de l'écrit", "CM1", None), ("TIMSS, mathématiques", "CM1", "TIMSS CM1 maths"),
                        ("TIMSS, mathématiques", "quatrième", "TIMSS 4e maths")):
        if k is None:
            a0, a1 = "2016", "2021"
            d = ae["pirls"][a1]["score"] - ae["pirls"][a0]["score"]
            st = "baisse significative" if ae["pirls"][a0]["sup_2021"] else "stable"
        else:
            s_ = ae["timss"][k]
            a0, a1 = sorted(s_)[-2], "2023"
            d = s_[a1]["score"] - s_[a0]["score"]
            st = "baisse significative" if s_[a0]["sym"] == "p" else ("hausse significative" if s_[a0]["sym"] == "q" else "stable")
        lignes.append((lib, pop, "%s-%s" % (a0, a1), d, st))
    lignes.append(("Test de positionnement, mathématiques", "entrée en seconde GT", "2021-2024",
                   sec["GT maths"]["2024"] - sec["GT maths"]["2021"], "hausse, descriptif (sans test)"))
    lignes.append(("Test de positionnement, français", "entrée en seconde GT", "2021-2024",
                   sec["GT francais"]["2024"] - sec["GT francais"]["2021"], "baisse, descriptif (sans test)"))
    for d_, lib in (("mathematiques", "PISA, culture mathématique"), ("lecture", "PISA, compréhension de l'écrit")):
        x = P[d_]["dif"]["2022"]
        lignes.append((lib, "15 ans", "2022-2025", x["v"], "baisse significative" if x["sig"] and x["v"] < 0 else "stable"))
    desc = "Tableau, dernière variation de chaque évaluation en France, dans sa propre échelle : " + " ; ".join(
        "%s (%s, %s) %s%s points, %s" % (l, p, per, "+" if v > 0 else "", nb(v, 0), st) for l, p, per, v, st in lignes) + "."
    h = 60 + 34 * len(lignes) + 10
    e = tete("niv-t", t["titre"], desc, h + 52)
    cols = (0, 240, 395, 480, 545)
    for x, lib in zip(cols, ("Évaluation", "Élèves", "Période", "Variation", "Statut")):
        e.append('<text x="%d" y="48" font-size="10.5" fill="%s" font-weight="600">%s</text>' % (x, MUTED, esc(lib)))
    for i, (lib, pop, per, v, st) in enumerate(lignes):
        y = 60 + 34 * i
        if i % 2 == 0:
            e.append('<rect x="0" y="%d" width="%d" height="34" fill="#f6f4f1"/>' % (y, W))
        col = ORANGE if st.startswith("baisse") else (BLEU if st.startswith("hausse") else GRIS)
        creux = "descriptif" in st
        e.append('<text x="%d" y="%d" font-size="11.5" fill="%s">%s</text>' % (cols[0] + 6, y + 21, INK, esc(lib)))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (cols[1], y + 21, INK2, esc(pop)))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (cols[2], y + 21, INK2, per))
        e.append('<text x="%d" y="%d" font-size="11.5" fill="%s" font-weight="600">%s%s</text>' % (cols[3], y + 21, col, "+" if v > 0 else "", nb(v, 0)))
        e.append('<rect x="%d" y="%d" width="10" height="10" rx="5" fill="%s" stroke="%s" stroke-width="1.6"/>'
                 % (cols[4], y + 12, "#ffffff" if creux else col, col))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (cols[4] + 16, y + 21, INK, esc(st)))
    return pied(e, h + 2, t["source"], t["note"])


def fig_composition(c, A):
    t = FIG["composition"]
    cp = c["comp"]
    pts_ = [("2015, observé", cp["moyenne_2015"], GRIS), ("2025, à la répartition entre classes de 2015", cp["recompose_2025"], ORANGE),
            ("2025, observé", cp["moyenne_2025"], BLEU)]
    desc = ("Score moyen PISA en culture scientifique, moyenne des classes : 2015 observé %s ; 2025 recalculé avec la répartition "
            "entre classes de 2015 %s ; 2025 observé %s. Baisse observée %s points ; à répartition de 2015, %s ; effet de la "
            "répartition entre classes +%s." % (nb(cp["moyenne_2015"], 0), nb(cp["recompose_2025"], 0), nb(cp["moyenne_2025"], 0),
                                              A["comp_baisse_obs"], A["comp_baisse_rec"], A["comp_effet"]))
    h = 230
    e = tete("niv-c", t["titre"], desc, h + 52)
    X0, X1, vmin, vmax = 300, 690, 465, 500
    sx = lambda v: X0 + (X1 - X0) * (v - vmin) / (vmax - vmin)
    for gv in range(vmin, vmax + 1, 5):
        e.append('<line x1="%.1f" y1="44" x2="%.1f" y2="%d" stroke="%s" stroke-width="0.6"/>' % (sx(gv), sx(gv), 44 + 150, GRID))
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (sx(gv), 44 + 164, MUTED, gv))
    for i, (lib, v, col) in enumerate(pts_):
        y = 70 + i * 50
        e.append('<text x="0" y="%d" font-size="11.5" fill="%s">%s</text>' % (y + 4, INK, esc(lib)))
        e.append('<circle cx="%.1f" cy="%d" r="7" fill="%s"/>' % (sx(v), y, col))
        e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="middle" font-weight="600">%s</text>' % (sx(v), y - 12, col, nb(v, 0)))
    return pied(e, h + 2, t["source"], t["note"])


def fig_baisse(c, A):
    t = {k: v.format(**A) for k, v in FIG["baisse"].items()}
    P = c["P"]
    desc = ("Pour chaque domaine, variation du score moyen PISA de 2015 à 2025 des %s pays de l'OCDE, France en orange. "
            "Lecture : France −%s points, médiane −%s. Mathématiques : France −%s, médiane −%s, %se plus forte baisse. "
            "Sciences : France −%s, médiane −%s." % (A["n_ocde"], A["lect_v15"], A["lect_med"], A["math_v15"], A["math_med"],
                                                    A["math_rang"], A["sci_v15"], A["sci_med"]))
    h = 292
    e = tete("niv-b", t["titre"], desc, h + 52)
    X0, X1 = 170, 700
    vmin, vmax = -70, 20
    sx = lambda v: X0 + (X1 - X0) * (v - vmin) / (vmax - vmin)
    TOP = 50
    for gv in range(vmin, vmax + 1, 10):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"/>'
                 % (sx(gv), TOP, sx(gv), TOP + 210, INK2 if gv == 0 else GRID, 1 if gv == 0 else 0.6))
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%s</text>'
                 % (sx(gv), TOP + 224, MUTED, ("+" if gv > 0 else "") + nb(gv, 0)))
    e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">points de score, 2025 moins 2015</text>'
             % ((X0 + X1) / 2, TOP + 238, MUTED))
    for i, d in enumerate(DOM):
        y = TOP + 34 + i * 70
        n2 = P[d]["n2"]
        e.append('<text x="0" y="%d" font-size="11.5" fill="%s" font-weight="600">%s</text>' % (y + 4, INK, esc(LIB[d])))
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s" opacity="0.14"/>'
                 % (sx(n2["q1"]), y - 11, sx(n2["q3"]) - sx(n2["q1"]), BLEU))
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.6"/>'
                 % (sx(n2["mediane"]), y - 11, sx(n2["mediane"]), y + 11, BLEU))
        vus = {}
        for p_, v in sorted(n2["pays"].items(), key=lambda kv: kv[1]):
            if p_ == "France":
                continue
            b = round(v / 1.6)
            k = vus.get(b, 0)
            vus[b] = k + 1
            dy = (k % 3 - 1) * 5
            e.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s" opacity="0.75"/>' % (sx(v), y + dy, GRIS))
        fr = n2["france"]
        e.append('<circle cx="%.1f" cy="%d" r="6" fill="%s" stroke="#ffffff" stroke-width="1.5"/>' % (sx(fr), y, ORANGE))
        e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle" font-weight="600">France %s</text>'
                 % (sx(fr), y - 16, ORANGE, nb(fr, 0)))
        e.append('<text x="0" y="%d" font-size="10" fill="%s">%sᵉ baisse sur %s</text>' % (y + 20, INK2, n2["rang"], n2["n"]))
    return pied(e, h + 2, t["source"], t["note"])


def fig_sommet(c, A):
    t = FIG["sommet"]
    P = c["P"]
    desc = ("Barres, en %% des élèves, 2015 puis 2025. Lecture, sous le niveau 2 : France %s puis %s, OCDE %s puis %s ; "
            "niveaux 5-6 : France %s puis %s, OCDE %s puis %s. Mathématiques, sous le niveau 2 : France %s puis %s ; niveaux 5-6 : France %s puis %s."
            % (A["lect_bas15"], A["lect_bas25"], A["lect_obas15"], A["lect_obas25"], A["lect_haut15"], A["lect_haut25"],
               A["lect_ohaut15"], A["lect_ohaut25"], A["math_bas15"], A["math_bas25"], A["math_haut15"], A["math_haut25"]))
    h = 300
    e = tete("niv-s", t["titre"], desc, h + 52)
    # légende
    for k, (lib, col, op) in enumerate((("France 2015", BLEU, 0.4), ("France 2025", BLEU, 1.0), ("OCDE 2015", GRIS, 0.4), ("OCDE 2025", GRIS, 1.0))):
        e.append('<rect x="%d" y="32" width="11" height="11" fill="%s" opacity="%s"/>' % (k * 120, col, op))
        e.append('<text x="%d" y="42" font-size="10.5" fill="%s">%s</text>' % (k * 120 + 15, INK2, lib))
    panneaux = [("lecture", "bas", ("Lecture", "en difficulté")), ("lecture", "haut", ("Lecture", "meilleurs élèves")),
                ("mathematiques", "bas", ("Mathématiques", "en difficulté")), ("mathematiques", "haut", ("Mathématiques", "meilleurs élèves"))]
    BAS, HMAX, vmax = 268, 170, 40.0
    for i, (d, cote, lib) in enumerate(panneaux):
        x0 = 8 + i * 178
        e.append('<text x="%d" y="70" font-size="11" fill="%s" font-weight="600">%s</text>' % (x0, INK, esc(lib[0])))
        e.append('<text x="%d" y="84" font-size="11" fill="%s">%s</text>' % (x0, INK2, esc(lib[1])))
        f, o = P[d]["niveaux"]["France"], P[d]["niveaux"][OC]
        barres = [(f[cote + "15"], BLEU, 0.4), (f[cote + "25"], BLEU, 1.0), (o[cote + "15"], GRIS, 0.4), (o[cote + "25"], GRIS, 1.0)]
        for j, (v, col, op) in enumerate(barres):
            x = x0 + j * 36 + (8 if j >= 2 else 0)
            hh = HMAX * v / vmax
            e.append('<rect x="%d" y="%.1f" width="30" height="%.1f" fill="%s" opacity="%s"/>' % (x, BAS - hh, hh, col, op))
            e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="middle">%s</text>' % (x + 15, BAS - hh - 4, INK, nb(v)))
        e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (x0, BAS, x0 + 160, BAS, GRID))
    return pied(e, h + 2, t["source"], t["note"])


def fig_seconde(c, A):
    t = FIG["seconde"]
    desc = ("Barres horizontales, écart standardisé entre la génération de 2021-2022 et celle de 2024-2025. Français : test de seconde −%s, "
            "PISA lecture −%s. Mathématiques : test de seconde +%s, PISA −%s." % (A["g_tf"], A["g_pf"], A["g_tm"], A["g_pm"]))
    h = 250
    e = tete("niv-g", t["titre"], desc, h + 52)
    X0, X1 = 330, 690
    vmin, vmax = -25, 15
    sx = lambda v: X0 + (X1 - X0) * (v - vmin) / (vmax - vmin)
    TOP = 52
    for gv in range(vmin, vmax + 1, 5):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"/>'
                 % (sx(gv), TOP, sx(gv), TOP + 160, INK2 if gv == 0 else GRID, 1 if gv == 0 else 0.6))
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%s</text>'
                 % (sx(gv), TOP + 174, MUTED, ("+" if gv > 0 else "") + nb(gv, 0)))
    gen = c["gen"]
    lignes = []
    for ev, dom, lib in (("Tests de positionnement de seconde", "Français", "Test de seconde, français"),
                         ("PISA", "Compréhension de l'écrit", "PISA, compréhension de l'écrit"),
                         ("Tests de positionnement de seconde", "Mathématiques", "Test de seconde, mathématiques"),
                         ("PISA", "Culture mathématique", "PISA, culture mathématique")):
        v = next(x for k, x in gen.items() if k[0] == ev and k[1] == dom)
        lignes.append((lib, v["d100"], ev == "PISA"))
    for i, (lib, v, pisa) in enumerate(lignes):
        y = TOP + 8 + i * 38 + (12 if i >= 2 else 0)
        e.append('<text x="0" y="%d" font-size="11.5" fill="%s">%s</text>' % (y + 15, INK, esc(lib)))
        x = min(sx(0), sx(v))
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s"/>' % (x, y, abs(sx(v) - sx(0)), ORANGE if pisa else BLEU))
        e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="%s">%s%s</text>'
                 % (sx(v) + (6 if v > 0 else -6), y + 15, INK, "start" if v > 0 else "end", "+" if v > 0 else "", nb(v, 0)))
    return pied(e, h + 2, t["source"], t["note"])


def fiches(figs):
    out = []
    for fid in ("thermometres", "baisse", "composition", "seconde", "sommet"):
        svg = figs["niveau-%s.svg" % fid]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        out.append(dict(id=fid, fichier="niveau-" + fid, titre=titre, montre=FIG[fid]["montre"], source=cart[0], precaution=cart[1]))
    return {"fr": out}


def csv_texte(c):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "variable", "cle", "valeur", "unite"])
    P = c["P"]
    for d in DOM:
        for a, v in sorted(P[d]["france"].items()):
            w.writerow(["pisa_score_moyen_france", d, a, round(v, 2), "points PISA"])
        for a, v in sorted(P[d]["ocde35"].items()):
            w.writerow(["pisa_score_moyen_ocde35", d, a, round(v, 2), "points PISA"])
        for p_, v in sorted(P[d]["n2"]["pays"].items()):
            w.writerow(["pisa_variation_2015_2025_pays_ocde", d, p_, round(v, 2), "points PISA"])
        for zone in ("France", OC):
            for k in ("bas15", "bas25", "haut15", "haut25"):
                w.writerow(["pisa_niveaux_" + ("france" if zone == "France" else "ocde35"), d, k, round(P[d]["niveaux"][zone][k], 2),
                            "% des eleves (bas : sous le niveau 2 ; haut : niveaux 5-6)"])
            so = P[d]["social"][zone]
            for a in sorted(so["ecart"]):
                w.writerow(["pisa_ecart_social_" + ("france" if zone == "France" else "ocde35"), d, a, round(so["ecart"][a], 2),
                            "points (quart haut moins quart bas du statut economique, social et culturel)"])
    for e_ in c["X"]["echantillon_classes"]:
        w.writerow(["pisa_2025_echantillon_france_classe", e_["classe"], "effectif", e_["effectif"], "eleves"])
    for cle, s in c["sec"].items():
        for a, v in sorted(s.items()):
            w.writerow(["test_positionnement_seconde_score_moyen", cle, a, v, "points (echelle 250/50 en 2019)"])
    for (ev, dom), v in c["gen"].items():
        w.writerow(["depp_ecart_generations_2021_2024", ev + " / " + dom, "100 x d de Cohen", v["d100"], "centiemes d'ecart-type"])
    for d, t in c["timss"].items():
        for a in ("1995", "2015"):
            w.writerow(["timss_advanced_terminale_s_france", d, a, t[a], "points TIMSS"])
    for d, v in c["X"]["p1"].items():
        for s, (po, pr, ad) in sorted(v["brut"].items()):
            w.writerow(["capes_externe_postes_presents_admis", d, s, "%d/%d/%d" % (po, pr, ad), "postes/presents/admis"])
    for a, v in sorted(c["p2"].items()):
        w.writerow(["contractuels_second_degre_public", "part", a, v, "% des personnels a mission d'enseignement"])
    for z, v in c["p3"].items():
        for k, x in v.items():
            w.writerow(["ocde_non_pleinement_qualifies", z, k, round(x, 2), "% des enseignants (ETP, public)"])
    for z in ("france", "ocde"):
        for a, v in sorted(c["p4"][z].items()):
            w.writerow(["pisa_manque_enseignants_declare", z, a, round(v, 2), "% des eleves (chef d'etablissement : enseignement entrave)"])
    for k, v in sorted(c["t3"]["pays"].items()):
        w.writerow(["timss4e_2019_2023_pisa_2022_2025_maths", k, "dT", round(v["dT"], 2), "points TIMSS"])
        w.writerow(["timss4e_2019_2023_pisa_2022_2025_maths", k, "dP", round(v["dP"], 2), "points PISA"])
        w.writerow(["timss4e_2019_2023_pisa_2022_2025_maths", k, "G", round(v["G"], 4), "ecart standardise (z(dP) - z(dT))"])
    cp = c["comp"]
    for an in ("2015", "2025"):
        for k, v in cp["parts_" + an].items():
            w.writerow(["pisa_sciences_composition_par_classe", k, an, round(v, 2), "% de l'echantillon"])
            w.writerow(["pisa_sciences_score_par_classe", k, an, round(cp["scores_" + an][k], 2), "points PISA"])
    w.writerow(["pisa_sciences_composition_par_classe", "score_2025_aux_parts_2015", "2025", round(cp["recompose_2025"], 2), "points PISA (calcul)"])
    for d, v in c["pct"].items():
        for z in ("France", "OCDE"):
            for p_, x in zip((10, 25, 50, 75, 90), v[z]):
                w.writerow(["pisa_variation_percentiles_2015_2025_" + z.lower(), d, "P%d" % p_, round(x, 2), "points PISA"])
    for a, v in c["eff"]["france"].items():
        w.writerow(["pisa_indice_effort_declare_france", "indice (1 a 10)", a, v, "DEPP, NI 26-40"])
    for lib, s_ in c["ae"]["timss"].items():
        for a, v in sorted(s_.items()):
            w.writerow(["timss_france", lib, a, v["score"], "points TIMSS (p : significativement au-dessus de 2023)" + (" p" if v["sym"] == "p" else "")])
    for a, v in sorted(c["ae"]["pirls"].items()):
        w.writerow(["pirls_france_cm1", "lecture", a, v["score"], "points PIRLS" + (" (significativement au-dessus de 2021)" if v["sup_2021"] else "")])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    c = calcul(lire())
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    A = affichage(c)
    log("PISA 2015-2025 : lecture -%s, maths -%s (%se/%s), sciences -%s ; lycee %s %% de l'echantillon"
        % (A["lect_v15"], A["math_v15"], A["math_rang"], A["n_ocde"], A["sci_v15"], A["lycee"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(A)))
        return 0
    import cairosvg
    figs = {"niveau-thermometres.svg": fig_thermometres(c, A), "niveau-baisse.svg": fig_baisse(c, A), "niveau-composition.svg": fig_composition(c, A), "niveau-sommet.svg": fig_sommet(c, A), "niveau-seconde.svg": fig_seconde(c, A)}
    P = c["P"]
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "champ": "France ; jeunes de 15 ans (PISA), élèves entrant en seconde (DEPP), terminale S (TIMSS Advanced), concours externes du second degré public",
                        "source_calcul": "calcul de l'auteur (protocole écrit avant calcul) ; extrait figé scripts/sources_niveau_eleves/ (SHA256SUMS)"},
               "pisa": {d: {"france": P[d]["france"], "ocde35": P[d]["ocde35"], "variation_2015_2025": P[d]["dif"]["2015"],
                            "variation_2022_2025": P[d]["dif"]["2022"], "pays_ocde_2015_2025": P[d]["n2"]["pays"],
                            "niveaux": P[d]["niveaux"], "ecart_social": P[d]["social"]} for d in DOM},
               "test_positionnement_seconde": c["sec"],
               "depp_ecart_generations": c["X"]["depp_generations"],
               "timss_advanced": c["timss"],
               "protocole_3_timss_pisa_maths": c["t3"],
               "protocole_2": {"composition_sciences": c["comp"], "percentiles": c["pct"], "effort_declare": c["eff"],
                               "autres_evaluations": c["ae"]},
               "recrutement": {"capes_externe": c["X"]["p1"], "contractuels": c["X"]["p2"], "non_pleinement_qualifies_ocde": c["p3"],
                               "manque_enseignants_declare_pisa": c["p4"]},
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
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; sources OCDE (PISA, Regards sur l'éducation), DEPP, IEA", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/niveau_eleves.json, static/niveau_eleves.csv, data/figures_niveau.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
