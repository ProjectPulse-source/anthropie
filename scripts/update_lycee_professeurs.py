#!/usr/bin/env python3
"""update_lycee_professeurs.py -- ressource « Manque-t-il des professeurs au lycée ? » (bloc École et lycée).

Découverte de la page (dépôt de pilotage de l'auteur, 06_PROMOTION/RECHERCHE_LYCEES_MOYENS_2026-10-07, test décisif du
07/10/2026, protocole écrit avant calcul, deux contre-expertises arbitrées) : « le manque de professeurs » recouvre
quatre mesures qui ne disent pas la même chose. Au lycée général et technologique, une heure de cours sur dix n'a pas
lieu, et en 2024-2025 plus de la moitié de ces heures tient aux fermetures, aux examens et commissions et à la
formation plutôt qu'aux absences individuelles ; les CAPES de mathématiques et de physique-chimie sont restés sous quatre
postes pourvus sur cinq de 2023 à 2025, puis au-delà de neuf sur dix à la session double de 2026, quand le CAPLP de
mathématiques-physique-chimie en pourvoit moins de deux sur trois ; les classes dépassent 30 élèves depuis 2020, mais la
part des divisions de 35 et plus est plus faible qu'en 2015.
Compléments du 07/10 (contre-expertise PRO-20261007-160259) : concours 2026 détaillés (ministère), dépense 2025
provisoire et comparaison OCDE de la DEPP (NI 26-42), dispersion entre établissements (NI 26-14).

Entrée : l'extrait FIGÉ du test décisif, scripts/sources_lycee_professeurs/extrait.json (écrit par extrait.py du dépôt
de recherche, qui retrouve ses valeurs phares dans la sortie du test), contrôlé contre SHA256SUMS. Ce générateur ne
recalcule que des rapports simples ; il met en forme et GARDE : chaque qualificatif de la prose est une condition sur les
nombres (fonction gardes) ; si l'extrait la dément, arrêt.
Mise à jour : DÉTECTÉE par le module de mise à jour (data/sources_maj.json, sources « lycee-* » en mode veille : RERS,
notes de la DEPP sur le temps d'enseignement non assuré, les élèves par structure, le compte de l'éducation et les
projections d'effectifs, concours de la session, OCDE), qui ouvre un ticket par édition nouvelle ; INTÉGRÉE à la main,
parce que l'extrait se calcule hors dépôt : relancer test_decisif.py puis extrait.py dans le dossier de recherche,
recopier l'extrait et son empreinte, relancer ce script, porter l'édition lue (« lu ») au registre.
Encadré #regions-lycees (bâti des lycées, 07/10/2026) : second extrait figé, extrait_bati.json, écrit par bati/extrait_bati.py
du même dépôt de recherche (protocoles 1 à 4 du bâti) ; balances DGFiP annuelles, hors module de mise à jour : rendez-vous de
rattrapage en juillet 2027 (exercice 2026) — relancer les tests du bâti puis extrait_bati.py, recopier l'extrait et son empreinte.
Page en français seulement (exclusion déclarée : débat, programme et statistique français).

Usage : python scripts/update_lycee_professeurs.py [--check] [--mutation=organisation|classes|concours|concours26|eleves|ocde|bati]
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
    s = ("−" if neg else "") + " ".join(groupes) + ("," + frac if frac else "")  # signe moins typographique
    return s


def pts(v: float) -> str:
    """« 1,9 point », « 3,3 points » : le pluriel français commence à 2."""
    return nb(v) + " " + ("point" if abs(v) < 2 else "points")


def disc(s: str) -> str:
    """Libellé de discipline de la DEPP en milieu de phrase : capitale non accentuée rétablie, minuscule initiale."""
    s = s.replace("Education", "Éducation")
    return s[0].lower() + s[1:]


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
    c26 = X["concours_2026"]
    taux = lambda d: 100 * sum(s["admis"] for s in d.values()) / sum(s["postes"] for s in d.values())
    postes = lambda d: sum(s["postes"] for s in d.values())
    k26 = {"maths": c26["capes"]["Mathématiques"], "pc": c26["capes"]["Physique - chimie"],
           "lp": c26["caplp"]["Mathématiques - physique chimie"]}
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
        nat=nat, contr=contr, e7=e7,
        t26={k: taux(d) for k, d in k26.items()}, p26={k: postes(d) for k, d in k26.items()},
        c1_2025=X["c1_2025"], ocde_depp=X["ocde_depp"], dec=X["d4"]["deciles"],
        c1=c1, c1_max_an=max(c1, key=c1.get), c3=c3,
        acad=acad, metro=metro, disc=disc_ok, grp=grp,
        es_toutes=next(d["es"] for d in X["v4"]["es_disciplines"] if d["discipline"] == "Toutes disciplines"),
        e4=e4, e4_nom=e4_nom, e4_prix=e4_prix, e4_reel=e4_reel, e4_el=e4_el, e4_par_el=e4_par_el, p_dern=p_dern,
        e5=e5, e5_f=e5["rcd_2024"] / e5["rcd_2022"], e9=e9,
        sd=X["d4"]["second_degre"], releve=X["releve_le"],
        e1=X["enonces"]["e1"],
        detail={"2024": X["d2"]["detail_2024"], "2025": X["d2"]["detail_2025"]},
        # Phase B de la refonte (10/10/2026) : candidats et postes des concours externes, motifs de fermeture du lycée.
        flux={int(a): v for a, v in X["d2"]["externes_flux"].items()}, ferm=X["d4"]["fermeture_gt"],
        # Contre-expertise de la page refondue (10/10/2026) : enseignants par niveau de formation (RERS 9.09).
        ens={int(a): v for a, v in X["d2"]["enseignants_niveau"]["gt_public_prive"].items()},
        ens_pub=X["d2"]["enseignants_niveau"]["public_2025"],
    )


# ------------------------------------------------------------------ bâti des lycées (encadré #regions-lycees)
# Extrait figé extrait_bati.json, écrit par bati/extrait_bati.py du dépôt de recherche (protocoles 1 à 4 du bâti, écrits
# avant calcul, trois contre-expertises arbitrées). Ici : rangs de Spearman, médianes, rapports, pente log-log.
LIEU = {"11": "en Île-de-France", "24": "en Centre-Val de Loire", "27": "en Bourgogne-Franche-Comté",
        "28": "en Normandie", "32": "dans les Hauts-de-France", "44": "dans le Grand Est",
        "52": "dans les Pays de la Loire", "53": "en Bretagne", "75": "en Nouvelle-Aquitaine", "76": "en Occitanie",
        "84": "en Auvergne-Rhône-Alpes", "93": "en Provence-Alpes-Côte d'Azur", "94": "en Corse"}
LETTRES = {3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"}


def rangs(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i])
    r, i = [0.0] * len(xs), 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[o[j + 1]] == xs[o[i]]:
            j += 1
        for k in range(i, j + 1):
            r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a, b):
    """Même calcul que test_bati.spearman (rangs moyens en cas d'égalité) ; série constante : None, jamais 0."""
    if len(set(a)) == 1 or len(set(b)) == 1:
        return None
    ra, rb = rangs(a), rangs(b)
    ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    return num / (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5


def mediane(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def cv(xs):
    m = sum(xs) / len(xs)
    return (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5 / m


BATI_UNITES = {
    "inv_total_3ans": "EUR, investissement rubrique 222 cumule sur la fenetre",
    "lyceens_moyens": "eleves (lycees publics, moyenne ponderee par annee budgetaire)",
    "inv_par_lyceen_3ans": "EUR par lyceen, cumul sur trois exercices",
    "inv_hors_204_par_lyceen_3ans": "EUR par lyceen, hors subventions d'equipement (compte 204)",
    "fonct_hors_personnel_par_lyceen": "EUR par lyceen et par an, hors chapitre 64",
    "fonct_hors_personnel_par_lycee": "EUR par lycee et par an, hors chapitre 64",
    "fonct_hors_personnel_par_lyceen_2019": "EUR par lyceen, exercice 2019, hors chapitre 64",
    "fonct_par_lycee_2019": "EUR par lycee, exercice 2019, hors chapitre 64",
    "lyceens_2019": "eleves (lycees publics, rentree)", "lyceens_2025": "eleves (lycees publics, rentree)",
    "part_prive": "part des lyceens scolarises dans le prive (rentrees 2024-2025)",
    "taille_lycees": "eleves par lycee public (rentrees 2023-2024)",
}


def calcul_bati(B):
    import math
    R = B["regions"]
    cs = sorted(R)
    v = lambda k: {c: R[c][k] for c in cs}
    rho = lambda X, Y, cc=cs: spearman([X[c] for c in cc], [Y[c] for c in cc])
    rap = lambda X: max(X.values()) / min(X.values())
    inv, inv204, fon = v("inv_par_lyceen_3ans"), v("inv_hors_204_par_lyceen_3ans"), v("fonct_hors_personnel_par_lyceen")
    fon_lyc, fon19, P, T = v("fonct_hors_personnel_par_lycee"), v("fonct_hors_personnel_par_lyceen_2019"), v("part_prive"), v("taille_lycees")
    dL = {c: R[c]["lyceens_2025"] / R[c]["lyceens_2019"] - 1 for c in cs}
    x = {c: math.log(1 + dL[c]) for c in cs}
    dFN = {c: math.log(R[c]["fonct_hors_personnel_par_lycee"] / R[c]["fonct_par_lycee_2019"]) for c in cs}
    lx = [math.log(R[c]["lyceens_moyens"]) for c in cs]
    ly = [math.log(R[c]["inv_total_3ans"]) for c in cs]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    elast = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    bas = [fon[c] for c in cs if dL[c] < 0]
    haut = [fon[c] for c in cs if dL[c] > 0]
    ordre_inv = sorted(cs, key=inv.get)
    sans_corse = {c: inv204[c] for c in cs if c != "94"}
    return dict(
        R=R, cs=cs, inv=inv, fon=fon, dL=dL, P=P, elast=elast, rap_inv=rap(inv), cv_inv=cv(list(inv.values())),
        cv_fon=cv(list(fon.values())), inv_min1=ordre_inv[0], inv_min2=ordre_inv[1], inv_max=ordre_inv[-1],
        rap204=rap(inv204), rap204_sc=rap(sans_corse), min204=min(inv204, key=inv204.get),
        rho_pt=rho(P, T), rho_pf=rho(P, fon), prive_top=sorted(cs, key=P.get)[-2:], inv_top=ordre_inv[-2:],
        rho_lf=rho(dL, fon), rho_ll=rho(dL, fon_lyc), med_bas=mediane(bas), med_haut=mediane(haut),
        n_bas=len(bas), n_haut=len(haut), meca=rap({c: 1 / (1 + dL[c]) for c in cs}),
        rho_19=rho(x, fon19), rho_creuse=rho(x, dFN), an=B["annees"], fen=B["fenetre_investissement"],
    )


def gardes_bati(b, g):
    """Chaque qualificatif de l'encadré #regions-lycees est une condition sur les nombres."""
    g(0.9 <= b["elast"] <= 1.1, "bâti : « à proportion de leurs lycéens, en moyenne » (élasticité %.2f)" % b["elast"])
    g(2 < b["rap_inv"] < 3, "bâti : « du simple à plus du double » (rapport %.2f)" % b["rap_inv"])
    g(b["cv_fon"] < 0.75 * b["cv_inv"], "bâti : « dépenses courantes bien plus régulières » (CV %.3f contre %.3f)" % (b["cv_fon"], b["cv_inv"]))
    g(b["rap204"] >= 2 and b["rap204_sc"] >= 2, "bâti : « l'écart ne disparaît pas hors subventions » (%.2f ; %.2f)" % (b["rap204"], b["rap204_sc"]))
    g(b["min204"] == "94", "bâti : « sans la Corse » suppose la Corse au plus bas hors subventions")
    g(abs(b["rho_pt"]) < 0.6 and abs(b["rho_pf"]) < 0.6, "bâti : « aucune relation lisible avec la part du privé » (%.2f ; %.2f)" % (b["rho_pt"], b["rho_pf"]))
    g(set(b["prive_top"]) == {"52", "53"} and all(0.35 <= b["P"][c] <= 0.45 for c in ("52", "53")),
      "bâti : « Bretagne et Pays de la Loire, environ quatre lycéens sur dix dans le privé »")
    g(set(b["inv_top"]) == {"52", "53"}, "bâti : « elles se distinguent par leur investissement » (deux plus forts)")
    g(b["rho_lf"] is not None and b["rho_lf"] <= -0.6, "bâti : « plus le recul, plus la dépense » (rho %.2f)" % (b["rho_lf"] or 0))
    g(b["med_bas"] > b["med_haut"], "bâti : médiane des régions en recul au-dessus")
    g(b["meca"] - 1 < (b["med_bas"] / b["med_haut"] - 1) and b["meca"] < 1.2,
      "bâti : « la seule baisse des effectifs ne suffit pas » (effet maximal %.3f)" % b["meca"])
    g(b["rho_ll"] is not None and -0.6 < b["rho_ll"] <= -0.3 and abs(b["rho_ll"]) < abs(b["rho_lf"]),
      "bâti : « la dépense rapportée aux lycées va dans le même sens, moins nettement » (rho %.2f)" % (b["rho_ll"] or 0))
    g(b["rho_19"] is not None and b["rho_19"] <= -0.6, "bâti : « relation déjà visible en %d »" % b["an"]["avant"])
    g(b["rho_creuse"] is None or b["rho_creuse"] > -0.6, "bâti : « que l'écart se soit creusé, les comptes ne permettent pas de l'établir »")
    g(b["n_bas"] in LETTRES and b["n_haut"] in LETTRES, "bâti : effectifs des groupes en toutes lettres")


def affichage_bati(b):
    R = b["R"]
    return {
        "bt_a0": str(b["fen"][0]), "bt_a1": str(b["fen"][1]),
        "bt_inv_min1": nb(b["inv"][b["inv_min1"]], 0), "bt_inv_min1_lieu": LIEU[b["inv_min1"]],
        "bt_inv_min2": nb(b["inv"][b["inv_min2"]], 0), "bt_inv_min2_lieu": LIEU[b["inv_min2"]],
        "bt_inv_max": nb(b["inv"][b["inv_max"]], 0), "bt_inv_max_lieu": LIEU[b["inv_max"]],
        "bt_rap": nb(b["rap_inv"], 2), "bt_rap204": nb(b["rap204"], 2), "bt_rap204_sc": nb(b["rap204_sc"], 2),
        "bt_l0": str(b["an"]["lyceens"][0]), "bt_l1": str(b["an"]["lyceens"][1]),
        "bt_f": "%d-%d" % tuple(b["an"]["fonctionnement"]), "bt_avant": str(b["an"]["avant"]),
        "bt_med_bas": nb(b["med_bas"], 0), "bt_med_haut": nb(b["med_haut"], 0),
        "bt_n_bas": LETTRES[b["n_bas"]], "bt_n_haut": LETTRES[b["n_haut"]],
        "bt_n_regions": {13: "treize"}[len(R)],
    }


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
    elif m == "eleves":       # les élèves seraient plus nombreux en 2027 qu'en 2017
        c["e4_el"] = 0.02
    elif m == "ocde":         # une année, la France serait sous l'agrégat de l'OCDE
        c["c3"] = {a: (dict(v, FRA=v["OECD"] * 0.95) if a == min(c["c3"]) else v) for a, v in c["c3"].items()}
    elif m == "concours26":   # le CAPES de mathématiques 2026 n'aurait pourvu que 85 % de ses postes
        c["t26"] = dict(c["t26"], maths=85.0)
    elif m == "bati":         # la dépense par lycéen de 2019 serait la même partout (rien de « déjà visible »)
        c["bati"] = dict(c["bati"], rho_19=None)
    elif m == "fermeture":    # les examens ne feraient plus que la moitié des fermetures du lycée
        c["ferm"] = dict(c["ferm"], part_examens=c["ferm"]["part_total"] / 2)
    elif m == "candidats":    # les candidats présents n'auraient baissé que de moitié depuis 2005
        fx = dict(c["flux"])
        fx[max(fx)] = dict(fx[max(fx)], presents=fx[min(fx)]["presents"] // 2)
        c["flux"] = fx
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
    g(c["org4"] - 3 * 0.05 > h4gt["individuelles"] + 0.05, "« fermetures, examens, formation pèsent plus que les absences individuelles » (2024-2025)")
    d = c["dec"]
    g(17 <= d["plus"]["total"] <= 20, "« près d'une heure sur cinq dans les plus touchés » : %s" % d["plus"]["total"])
    g(round(d["plus"]["total"] / d["moins"]["total"]) == 6,"« six fois plus » (déciles, DEPP) : %s / %s" % (d["plus"]["total"], d["moins"]["total"]))
    org4 = c["h4"][GT]["fermeture"] + c["h4"][GT]["systeme"] + c["h4"][GT]["formation"]
    g(org4 / h4gt["total"] > 0.5, "« plus de la moitié des heures perdues » : %.2f" % (org4 / h4gt["total"]))
    g(c["org3"] > c["h3"][GT]["individuelles"], "« même sens en 2023-2024 » (chiffres à l'unité)")
    g(abs(c["org4_col"] - c["h4"][COL]["individuelles"]) <= 0.5, "« au collège, les deux s'équilibrent » : %.1f / %.1f" % (c["org4_col"], c["h4"][COL]["individuelles"]))
    g(h4gt["fermeture"] > c["h4"][COL]["fermeture"] and h4gt["fermeture"] > c["h4"][LP]["fermeture"], "« le lycée GT ferme davantage »")
    g(abs(h4gt["total"] - 10) <= 0.5, "énoncé « 10 % des heures dans les lycées » : exact à 0,5 point")
    f = c["ferm"]
    g(f["part_examens"] / f["part_total"] >= 0.85 and f["jours_examens"] / f["jours_total"] >= 0.85,
      "« la fermeture du lycée tient presque toute aux examens » : %.2f du temps, %.1f jours sur %.1f" % (f["part_examens"] / f["part_total"], f["jours_examens"], f["jours_total"]))
    g(abs(f["part_total"] - h4gt["fermeture"]) <= 0.05, "motifs de fermeture : même total que la figure 2 de la DEPP")
    g(h4gt["individuelles"] > max(h4gt[k] for k in ("fermeture", "systeme", "formation")),
      "« aucun des trois autres motifs ne pèse, seul, autant que les absences individuelles » (panel après, 10/10 : lu à l'envers)")
    ecarts = {k: h4gt[k] - c["h4"][COL][k] for k in ("fermeture", "systeme", "formation", "individuelles")}
    g(ecarts["fermeture"] > sum(v for k, v in ecarts.items() if k != "fermeture" and v > 0),
      "« entre lycée GT et collège, la différence se fait surtout sur la fermeture » : %s" % {k: round(v, 1) for k, v in ecarts.items()})
    g(max(v["presents"] for a, v in c["flux"].items() if a > min(c["flux"])) < 0.6 * c["flux"][min(c["flux"])]["presents"],
      "« les candidats n'ont jamais approché leur niveau de %d »" % min(c["flux"]))
    g(round(h4gt["individuelles"] + c["org4"], 1) != round(h4gt["total"], 1),
      "« les parts arrondies totalisent %s pour %s publiés » : l'écart d'arrondi a disparu, la phrase est à retirer"
      % (nb(h4gt["individuelles"] + c["org4"]), nb(h4gt["total"])))
    # Concours : candidats et postes (RERS 9.27)
    fx = c["flux"]
    f0, f1 = fx[min(fx)], fx[max(fx)]
    r_pres = f0["presents"] / f1["presents"]
    g(2.5 <= r_pres < 3, "« près de trois fois moins de candidats présents » : %.2f" % r_pres)
    g(f1["postes"] / f0["postes"] > f1["presents"] / f0["presents"], "« les postes offerts ont moins baissé que les candidats »")
    cpp = lambda r: r["presents"] / r["postes"]
    g(1.8 <= cpp(f0) / cpp(f1) <= 2.2, "« deux fois moins de candidats par poste » : %.2f" % (cpp(f0) / cpp(f1)))
    suites = {a: fx[a]["presents"] / fx[a - 1]["presents"] - 1 for a in fx if a - 1 in fx}
    g(min(suites, key=suites.get) == 2022 and suites[2022] < -0.25,
      "« la plus forte baisse d'une session à la suivante est celle de 2022 » : %s" % {a: round(v, 3) for a, v in suites.items()})
    # Enseignants des formations GT (RERS 9.09, public + privé) : hausse jusqu'en 2017, recul depuis
    en, v1 = c["ens"], c["v1"]
    a_max = max(en, key=en.get)
    g(a_max == 2017 and en[max(en)] < en[a_max] and en[min(en)] < en[a_max],
      "« les enseignants des formations GT ont augmenté jusqu'en 2017, puis reculé » : %s" % en)
    g(v1[2025]["eleves"] / v1[2015]["eleves"] - 1 > en[2025] / en[2015] - 1 + 0.02,
      "« de 2015 à 2025, les élèves ont augmenté nettement plus que les enseignants »")
    pc_ = {k: 100 * v["contractuels"] / v["ensemble"] for k, v in c["ens_pub"].items()}
    g(pc_["gt"] < pc_["total"] < pc_["pro"], "« contractuels : moins en formations GT, plus en formations professionnelles » : %s" % pc_)
    # Trajectoires par discipline (R2 : jamais « longtemps déficitaire » pour les deux)
    m_, p_ = {int(a): v for a, v in c["maths"].items()}, {int(a): v for a, v in c["pc"].items()}
    g(all(m_[a] >= 98 for a in (2008, 2009, 2010)), "« le CAPES de mathématiques pourvoyait presque tous ses postes jusqu'en 2010 »")
    g(max(v for a, v in m_.items() if a >= 2011) < 93, "« depuis 2011, jamais plus de neuf postes sur dix ou presque » (mathématiques)")
    g(all(p_[a] >= 99.5 for a in range(2008, 2022) if a != 2019) and p_[2019] < 80,
      "« physique-chimie : presque tous ses postes de 2008 à 2021, sauf en 2019 »")
    g(all(p_[a] < 75 for a in p_ if a >= 2022), "« physique-chimie : sous trois postes sur quatre depuis 2022 »")
    # E6 : base publiée à l'unité (R9) -- l'écart réel tient entre deux bornes
    g(c["sd"]["total"]["2022-2023"] + 0.5 - c["sd"]["total"]["2024-2025"] < 3, "E6 : « même la borne haute de la baisse reste sous 3 points »")
    # Classes
    g(min(c["ed_depuis20"]) > c["ed_max_avant"], "« depuis 2020, au-dessus de tout niveau de 1994-2015 »")
    g(min(c["ed_depuis20"]) >= 30, "« plus de 30 élèves depuis 2020 »")
    g(max(c["ed_depuis20"]) - min(c["ed_depuis20"]) <= 0.4, "« stable depuis 2020 »")
    g(c["tr"]["2025"]["div_35"] < c["tr"]["2015"]["div_35"], "« les divisions de 35 et plus sont moins fréquentes qu'en 2015 »")
    g(c["tr"]["2025"]["div_30"] > c["tr"]["2015"]["div_30"] + 3, "« les divisions de 30 et plus sont plus fréquentes qu'en 2015 »")
    g(62 <= c["tr"]["2025"]["div_30"] <= 71, "« deux divisions sur trois » : %.1f" % c["tr"]["2025"]["div_30"])
    d3034 = c["tr"]["2025"]["div_30"] - c["tr"]["2025"]["div_35"]
    g(40 <= d3034 <= 55, "« près d'une classe sur deux de 30 à 34 élèves » : %.1f" % d3034)
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
    g(c["ocde_depp"]["france"] > c["ocde_depp"]["moyenne_ocde"], "« la DEPP trouve aussi la France au-dessus de la moyenne de l'OCDE »")
    # Concours
    for nom, s in (("mathématiques", c["maths"]), ("physique-chimie", c["pc"])):
        g(all(s[a] < 80 for a in ("2023", "2024", "2025")), "« moins de quatre postes sur cinq, trois sessions » : CAPES %s" % nom)
    for cle in ("Capet / sciences industrielles de l’ingénieur", "CAPLP / mathématiques-physique chimie"):
        g(all(c["detail"][an_][cle]["couverture"] < 85 for an_ in ("2024", "2025")), "« d'autres concours sous 85 %% en 2024 et 2025 » : %s" % cle)
    g(c["agreg_maths"]["2023"] >= 85, "« l'agrégation de mathématiques ne remplit pas le critère des trois sessions »")
    g(c["t26"]["maths"] > 90 and c["t26"]["pc"] > 90, "« 2026 : plus de neuf postes sur dix en mathématiques et en physique-chimie »")
    g(c["t26"]["lp"] < 200 / 3, "« CAPLP mathématiques-physique-chimie 2026 : moins de deux postes sur trois » : %.1f" % c["t26"]["lp"])
    g(c["p26"]["maths"] > 1.1 * c["detail"]["2025"]["Capes / mathématiques"]["postes"],
      "« plus de postes offerts en mathématiques en 2026 qu'en 2025 »")
    g(c["contr"][max(c["contr"])] - c["contr"][min(c["contr"])] >= 2, "« la part des contractuels monte »")
    # Académies
    g(max(c["metro"].values()) - min(c["metro"].values()) >= 2, "« les académies ne sont pas à égalité »")
    # Énoncés
    g(c["e4_reel"] > 0 and c["e4_par_el"] > c["e4_reel"], "E4 : majorants positifs, par élève plus fort")
    g(c["e4_el"] < 0, "« les élèves seront moins nombreux en 2027 qu'en 2017 » : %.3f" % c["e4_el"])
    g(2.5 <= c["e5_f"] < 2.95, "E5 « multiplié par environ 2,6, pas tout à fait triplé » : %.2f" % c["e5_f"])
    var = c["sd"]["total"]["2024-2025"] - c["sd"]["total"]["2022-2023"]
    g(-2.5 < var < 0, "E6 « baisse de 1 point environ sur la mesure DEPP, non de 3 » : %.1f" % var)
    gardes_bati(c["bati"], g)
    return n


# ------------------------------------------------------------------ affichage
def affichage(c):
    h4gt, h4col, h4lp = c["h4"][GT], c["h4"][COL], c["h4"][LP]
    rap = {a: v["FRA"] / v["OECD"] for a, v in c["c3"].items()}
    a_rmin, a_rmax = min(rap), max(rap)
    nat = c["nat"]
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
        "h_indiv": nb(h4gt["individuelles"]), "h_indiv_pt": pts(h4gt["individuelles"]),
        "h_ferm_pt": pts(h4gt["fermeture"]), "h_sys_pt": pts(h4gt["systeme"]), "h_form_pt": pts(h4gt["formation"]), "h_nr": nb(h4gt["non_remplacement"]),
        "h_org": nb(c["org4"]), "h_org_pt": pts(c["org4"]),"h_org_part": str(round(100 * c["org4"] / h4gt["total"])),
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
        "es_min": nb(dmin["es"]), "es_min_disc": disc(dmin["discipline"]), "es_max": nb(dmax["es"]), "es_max_disc": disc(dmax["discipline"]),
        "es_maths": nb(disc_txt["Mathématiques"]), "es_hg": nb(disc_txt["Histoire-Géographie"]), "es_philo": nb(disc_txt["Philosophie"]),
        "es_ses": nb(disc_txt["Sciences économiques et sociales"]), "es_svt": nb(disc_txt["Sciences de la Vie et de la Terre"]),
        "grp_1g_18": nb(c["grp"]["Première générale"]["2018"]), "grp_1g_19": nb(c["grp"]["Première générale"]["2019"]),
        "grp_1g": nb(c["grp"]["Première générale"][an_grp]), "grp_tg": nb(c["grp"]["Terminale générale"][an_grp]),
        "grp_2nde": nb(c["grp"]["Seconde GT"][an_grp]), "grp_an": an_grp,
        # moyens
        "a0": str(c["a0"]), "a1": str(c["a1"]), "el_var": nb(100 * c["el_var"]), "div_var": nb(100 * c["div_var"]), "div_baisse": nb(-100 * c["div_var"]),
        "he_var": nb(100 * c["he_var"], 0), "he_baisse": nb(-100 * c["he_var"], 0), "he_a0": nb(c["v1"][c["a0"]]["he"], 2), "he_a1": nb(c["v1"][c["a1"]]["he"], 2),
        "he_2010": nb(c["he_2010"], 2), "he_2015": nb(c["he_2015"], 2),
        "c1_max": nb(c["c1"][2010], 0), "c1_dern": nb(c["c1"][max(c["c1"])], 0), "c1_an": str(max(c["c1"])),
        "c1_var": nb(100 * (c["c1"][max(c["c1"])] / c["c1"][2010] - 1), 0),
        "c1_baisse": nb(100 * (1 - c["c1"][max(c["c1"])] / c["c1"][2010]), 0),
        "c3_an": str(max(c["c3"])), "c3_fra": nb(c["c3"][max(c["c3"])]["FRA"], 0), "c3_oecd": nb(c["c3"][max(c["c3"])]["OECD"], 0),
        "c3_pct": nb(100 * (rap[max(rap)] - 1), 0), "c3_debut": str(a_rmin),
        "ocde_depp_pct": nb(100 * (c["ocde_depp"]["france"] / c["ocde_depp"]["moyenne_ocde"] - 1)), "ocde_depp_an": str(c["ocde_depp"]["annee"]),
        "c1_25": nb(c["c1_2025"]["gt"], 0), "c1_25_an": str(c["c1_2025"]["annee"]),
        "dec_moins": nb(c["dec"]["moins"]["total"], 0), "dec_plus": nb(c["dec"]["plus"]["total"], 0),
        "dec_plus_indiv": nb(c["dec"]["plus"]["individuelles"], 0), "dec_plus_ferm": nb(c["dec"]["plus"]["fermeture"], 0),
        "div30_34": nb(c["tr"]["2025"]["div_30"] - c["tr"]["2025"]["div_35"]),
        "m26": nb(c["t26"]["maths"]), "pc26": nb(c["t26"]["pc"]), "lp26": nb(c["t26"]["lp"]),
        "m26_postes": nb(c["p26"]["maths"], 0), "m25_postes": nb(c["detail"]["2025"]["Capes / mathématiques"]["postes"], 0), "pc26_postes": nb(c["p26"]["pc"], 0), "lp26_postes": nb(c["p26"]["lp"], 0),
        "e4_17": nb(c["e4"]["credits_2017"]), "e4_27": nb(c["e4"]["credits_2027"], 0), "e4_nom": nb(100 * c["e4_nom"], 0),
        "e4_prix": nb(100 * c["e4_prix"], 0), "e4_prix_an": str(c["p_dern"]), "e4_reel": nb(100 * c["e4_reel"], 0),
        "e4_el": nb(100 * c["e4_el"], 0), "e4_el_baisse": nb(-100 * c["e4_el"], 0), "e4_par_el": nb(100 * c["e4_par_el"], 0),
        # concours
        "m23": nb(c["maths"]["2023"]), "m24": nb(c["maths"]["2024"]), "m25": nb(c["maths"]["2025"]),
        "pc23": nb(c["pc"]["2023"]), "pc24": nb(c["pc"]["2024"]), "pc25": nb(c["pc"]["2025"]),
        "agm23": nb(c["agreg_maths"]["2023"]),
        "nat15": nb(nat[2015]), "nat22": nb(nat[2022]), "nat25": nb(nat[max(nat)]),
        "e7": nb(c["e7"]["enonce_2026"]), "e7_25": nb(c["e7"]["enonce_2025"]),
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
        **affichage_bati(c["bati"]),
        **affichage_phase_b(c),
    }


def affichage_phase_b(c):
    """Jetons ajoutés par la refonte (phase B, 10/10/2026)."""
    h4gt, f, fx = c["h4"][GT], c["ferm"], c["flux"]
    a0, a1 = min(fx), max(fx)
    cpp = lambda r: r["presents"] / r["postes"]
    m_, p_ = {int(a): v for a, v in c["maths"].items()}, {int(a): v for a, v in c["pc"].items()}
    t22, t24 = c["sd"]["total"]["2022-2023"], c["sd"]["total"]["2024-2025"]
    return {
        "h_somme": nb(h4gt["individuelles"] + c["org4"]), "col_ferm": nb(c["h4"][COL]["fermeture"]),
        "ferm_j": nb(f["jours_total"]), "ferm_j_exam": nb(f["jours_examens"]),
        "ferm_pt_exam": pts(f["part_examens"]),
        "fx_a0": str(a0), "fx_a1": str(a1),
        "fx_pres0": nb(fx[a0]["presents"], 0), "fx_pres1": nb(fx[a1]["presents"], 0),
        "fx_postes0": nb(fx[a0]["postes"], 0), "fx_postes1": nb(fx[a1]["postes"], 0),
        "fx_pres_baisse": nb(100 * (1 - fx[a1]["presents"] / fx[a0]["presents"]), 0),
        "fx_postes_baisse": nb(100 * (1 - fx[a1]["postes"] / fx[a0]["postes"]), 0),
        "fx_cpp0": nb(cpp(fx[a0])), "fx_cpp1": nb(cpp(fx[a1])),
        "fx_pres21": nb(fx[2021]["presents"], 0), "fx_pres22": nb(fx[2022]["presents"], 0),
        "fx_chute22": nb(100 * (1 - fx[2022]["presents"] / fx[2021]["presents"]), 0),
        "fx_postes10": nb(fx[2010]["postes"], 0), "fx_postes15": nb(fx[2015]["postes"], 0),
        "m_max_11": nb(max(v for a, v in m_.items() if a >= 2011)),
        "pc19": nb(p_[2019]), "pc22": nb(p_[2022]), "m22": nb(m_[2022]), "m11": nb(m_[2011]),
        "sd_var_lo": nb(t22 - 0.5 - t24), "sd_var_hi": nb(t22 + 0.5 - t24),
        "en_a0": str(min(c["ens"])), "en_a1": str(max(c["ens"])), "en0": nb(c["ens"][min(c["ens"])], 0),
        "en1": nb(c["ens"][max(c["ens"])], 0), "en_max": nb(max(c["ens"].values()), 0),
        "en_max_an": str(max(c["ens"], key=c["ens"].get)),
        "en_recul": nb(100 * (1 - c["ens"][max(c["ens"])] / max(c["ens"].values()))),
        "en_var15": nb(100 * (c["ens"][2025] / c["ens"][2015] - 1)),
        "el_var15": nb(100 * (c["v1"][2025]["eleves"] / c["v1"][2015]["eleves"] - 1)),
        "epe15": nb(c["v1"][2015]["eleves"] / c["ens"][2015]), "epe25": nb(c["v1"][2025]["eleves"] / c["ens"][2025]),
        "en_pub": nb(c["ens_pub"]["gt"]["ensemble"], 0), "en_pub_contr": nb(c["ens_pub"]["gt"]["contractuels"], 0),
        "en_pub_contr_pct": nb(100 * c["ens_pub"]["gt"]["contractuels"] / c["ens_pub"]["gt"]["ensemble"]),
        "en_pro_contr_pct": nb(100 * c["ens_pub"]["pro"]["contractuels"] / c["ens_pub"]["pro"]["ensemble"], 0),
        "en_tot_contr_pct": nb(100 * c["ens_pub"]["total"]["contractuels"] / c["ens_pub"]["total"]["ensemble"]),
        "sd_nr_sys": nb(c["h4"]["Ensemble"]["systeme"]), "sd_nr_form": nb(c["h4"]["Ensemble"]["formation"]),
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
        note="En % des heures prévues. Examens, formation : enseignants absents eux aussi. Individuelles : maladie, congés, grèves. Enquête par échantillon, une année.",
        montre="Au lycée général et technologique public, en 2024-2025, les absences individuelles d'enseignants non remplacées pèsent moins que les trois autres motifs réunis : fermetures (presque toutes pour les examens), enseignants mobilisés par les examens ou les commissions, formation ; au collège, les deux parts s'équilibrent. Une seule année publiée au dixième."),
    "classes": dict(
        titre="Élèves par classe au lycée général et technologique, 1994-{ed_an}",
        source="DEPP, Repères et références statistiques 2026, fiches 2.05 et 2.06 (public et privé sous contrat)",
        note="Nombre moyen d'élèves par division (classe entière). Devant un professeur, les élèves sont moins nombreux : une partie des heures se fait en groupe.",
        montre="Depuis 2020, les classes de lycée GT comptent plus de 30 élèves en moyenne, un niveau jamais atteint de 1994 à 2015 ; la moyenne est stable depuis."),
    "concours": dict(
        titre="Part des postes pourvus aux concours externes d'enseignants, 2008-2025 et 2026",
        source="DEPP, RERS 2026, fiches 9.27 et 9.28 (concours externes, public) ; 2026 : ministère, résultats par concours",
        note="Admis rapportés aux postes offerts ; ne mesure pas le besoin. 2026 : deux concours (bac+3, bac+5), hors série.",
        montre="De 2023 à 2025, les CAPES de mathématiques et de physique-chimie sont restés sous quatre postes pourvus sur cinq. En 2026, deux concours (bac+3 et bac+5) et davantage de postes : plus de neuf sur dix pourvus, un résultat qui ne prolonge pas la série et ne mesure pas le besoin."),
}


def fig_heures(c, A):
    t = FIG["heures"]
    lignes = [("Lycée général et technologique", c["h4"][GT]), ("Lycée professionnel", c["h4"][LP]), ("Collège", c["h4"][COL])]
    desc = ("Barres empilées, 2024-2025, en %% des heures prévues. Lycée GT : %s au total, dont absences individuelles %s, "
            "examens et commissions %s, fermeture %s, formation %s. Lycée professionnel : %s. Collège : %s, dont absences individuelles %s. "
            "%s"
            % (A["h_total"], A["h_indiv"], A["h_sys"], A["h_ferm"], A["h_form"], A["lp_total"], A["col_total"], A["col_indiv"], arrondi_txt(A)))
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
    e.append('<text x="0" y="%d" font-size="10.5" fill="%s">%s</text>' % (h - 14, INK2, esc(arrondi_txt(A))))
    return pied(e, h + 2, t["source"], t["note"])


def arrondi_txt(A):
    """Contre-expertise de la page refondue (10/10/2026) : l'écart d'arrondi doit se lire dans l'image autonome."""
    return "Lycée GT : les quatre motifs arrondis totalisent %s ; total publié par la DEPP : %s (écart d'arrondi)." % (A["h_somme"], A["h_total"])


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
            "CAPES de physique-chimie : %s, %s, %s. Ensemble des concours externes (années publiées) : %s %% en 2015, %s en 2025. "
            "Session 2026, hors série (deux concours, bac+3 et bac+5, ministère) : CAPES de mathématiques %s %%, de physique-chimie %s %%."
            % (a1, A["m23"], A["m24"], A["m25"], A["pc23"], A["pc24"], A["pc25"], A["nat15"], A["nat25"], A["m26"], A["pc26"]))
    h = 290
    e = tete("lyc-k", t["titre"], desc, h + 52)
    X0, X1, TOP, BAS = 44, 420, 44, 260
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
    # 2026 : autre régime (deux concours, autre source) -- colonne séparée par une rupture, points creux, jamais reliés
    XR, X26 = 624, 660
    e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (XR, TOP - 4, XR, BAS, INK2))
    e.append('<text x="%d" y="%d" font-size="10" fill="%s" text-anchor="middle">2026</text>' % (X26 + 14, BAS + 14, MUTED))
    e.append('<text x="%d" y="%d" font-size="10" fill="%s" text-anchor="middle">deux concours</text>' % (X26 + 14, TOP - 8, INK2))
    for v, col in ((c["t26"]["maths"], BLEU), (c["t26"]["pc"], ORANGE)):
        e.append('<circle cx="%d" cy="%.1f" r="4" fill="#ffffff" stroke="%s" stroke-width="2"/>' % (X26, Y(min(v, 100)), col))
        e.append('<text x="%d" y="%.1f" font-size="10.5" fill="%s">%s</text>' % (X26 + 8, Y(min(v, 100)) + 4, col, nb(v)))
    return pied(e, h + 2, t["source"], t["note"])


# ------------------------------------------------------------------ figures mobiles (phase B de la refonte, 10/10/2026)
# Composées pour 300 px de large, jamais rétrécies : police minimale FS_MIN ; chaque valeur dessinée doit figurer dans la
# description de la version détaillée (parite_mobile). Patron : scripts/update_niveau_eleves.py.
WM, FS_MIN = 300, 13.5
LICENCE_M = "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"
SEGS = [("individuelles", "Absences individuelles", ORANGE, 1.0), ("systeme", "Examens, commissions", BLEU, 1.0),
        ("fermeture", "Fermeture (examens surtout)", BLEU, 0.62), ("formation", "Formation", BLEU, 0.35)]


def coupe(s, n):
    out, cur = [], ""
    for mot in s.split():
        if cur and len(cur) + 1 + len(mot) > n:
            out.append(cur)
            cur = mot
        else:
            cur = (cur + " " + mot).strip()
    return out + ([cur] if cur else [])


def tete_m(fid, titre, desc):
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (WM, fid, fid, FONT),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (fid, esc(titre), fid, esc(desc)),
         '<rect width="%d" height="0" fill="#ffffff"/>' % WM]
    lignes = coupe(titre, 30)
    for k, ligne in enumerate(lignes):
        e.append('<text x="0" y="%d" font-size="17" font-weight="600" fill="%s">%s</text>' % (20 + 22 * k, INK, esc(ligne)))
    return e, 20 + 22 * len(lignes)


def finir_m(e, y0, source, note):
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, WM, y0, GRID))
    y = y0 + 4
    for tx, col in ((source, INK2), (note, INK2), (LICENCE_M, MUTED)):
        for ligne in coupe(tx, 38):
            y += 17
            e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, col, esc(ligne)))
        y += 4
    e.append("</svg>")
    h = y + 6
    s = "\n".join(e)
    return s.replace('viewBox="0 0 %d 0"' % WM, 'viewBox="0 0 %d %d"' % (WM, h), 1).replace(
        '<rect width="%d" height="0"' % WM, '<rect width="%d" height="%d"' % (WM, h), 1)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg).group(1))


def fig_heures_m(c, A, svg_d):
    t = FIG["heures"]
    e, y = tete_m("lyc-hm", "Heures de cours non assurées, 2024-2025 : pourquoi ?", desc_de(svg_d))
    gt = c["h4"][GT]
    y += 4
    e.append('<text x="0" y="%d" font-size="%s" fill="%s">Au lycée général et technologique :</text>' % (y + 14, FS_MIN, INK2))
    y += 14
    for cle, lib, col, op in SEGS:   # légende chiffrée : les quatre motifs au lycée GT
        y += 24
        e.append('<rect x="0" y="%d" width="14" height="14" fill="%s" opacity="%s"/>' % (y - 12, col, op))
        e.append('<text x="22" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK, esc(lib)))
        e.append('<text x="%d" y="%d" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (WM, y, INK, nb(gt[cle])))
    sx = lambda v: (WM - 64) * v / 11.0
    for lib, v in (("Lycée général et technologique", gt), ("Lycée professionnel", c["h4"][LP]), ("Collège", c["h4"][COL])):
        y += 36
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(lib)))
        y += 8
        x = 0.0
        for cle, _, col, op in SEGS:
            w = sx(v[cle])
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s" opacity="%s" stroke="#ffffff" stroke-width="1"/>' % (x, y, w, col, op))
            x += w
        e.append('<text x="%.1f" y="%d" font-size="15" font-weight="600" fill="%s">%s %%</text>' % (x + 6, y + 16, INK, nb(v["total"])))
        y += 22
    y += 14
    for ligne in coupe(arrondi_txt(A), 38):
        y += 18
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(ligne)))
    return finir_m(e, y + 16, t["source"], t["note"])


def fig_classes_m(c, A, svg_d):
    t = {k: v.format(**A) for k, v in FIG["classes"].items()}
    ed = c["ed"]
    a0, a1 = min(ed), max(ed)
    e, y = tete_m("lyc-cm", t["titre"], desc_de(svg_d))
    X0, X1, TOP = 26, WM - 6, y + 34
    BAS = TOP + 170
    vmin, vmax = 26, 31
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)
    for gv in range(vmin + 1, vmax + 1, 2):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (X0, Y(gv), X1, Y(gv), GRID))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(gv) + 4, FS_MIN, MUTED, gv))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity="0.25"/>' % (X(2020) - 3, TOP, X(a1) - X(2020) + 6, BAS - TOP, GRIS_CLAIR))
    e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="end">depuis 2020 : plus de 30</text>' % (X1, TOP - 10, FS_MIN, INK2))
    for a in (1995, 2005, 2015, a1):   # la dernière année s'aligne à droite : centrée, elle sortait du cadre
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%d</text>' % (X(a), BAS + 18, FS_MIN, MUTED, "end" if a == a1 else "middle", a))
    d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(v)) for k, (a, v) in enumerate(sorted(ed.items())))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>' % (d, BLEU))
    for a, anc in ((a0, "start"), (c["ed_an_max_avant"], "middle"), (a1, "end")):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.6" fill="%s"/>' % (X(a), Y(ed[a]), BLEU))
        e.append('<text x="%.1f" y="%.1f" font-size="15" font-weight="600" fill="%s" text-anchor="%s">%s</text>' % (X(a), Y(ed[a]) + 22, INK, anc, nb(ed[a])))
    return finir_m(e, BAS + 36, t["source"], t["note"])


def fig_concours_m(c, A, svg_d):
    t = FIG["concours"]
    m = {int(a): v for a, v in c["maths"].items()}
    p = {int(a): v for a, v in c["pc"].items()}
    e, y = tete_m("lyc-km", "Part des postes pourvus aux CAPES, 2008-2025 et 2026", desc_de(svg_d))
    a0, a1 = 2008, max(m)
    X0, X1, TOP = 40, 222, y + 34
    BAS = TOP + 170
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * (v - 40) / 60
    for gv in range(40, 101, 20):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (X0, Y(gv), X1, Y(gv), GRID))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(gv) + 4, FS_MIN, MUTED, gv))
    for a in (2010, 2020):
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 18, FS_MIN, MUTED, a))
    for serie, col in ((m, BLEU), (p, ORANGE)):
        d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(min(v, 100))) for k, (a, v) in enumerate(sorted(serie.items())))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>' % (d, col))
    XR, X26 = 246, 276
    e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (XR, TOP - 6, XR, BAS, INK2))
    e.append('<text x="%d" y="%d" font-size="%s" fill="%s" text-anchor="middle">2026</text>' % (X26, BAS + 18, FS_MIN, MUTED))
    for v, col in ((c["t26"]["maths"], BLEU), (c["t26"]["pc"], ORANGE)):
        e.append('<circle cx="%d" cy="%.1f" r="5" fill="#ffffff" stroke="%s" stroke-width="2.2"/>' % (X26, Y(min(v, 100)), col))
    y = BAS + 30
    for lib, col, v25, v26 in (("CAPES de mathématiques", BLEU, A["m25"], A["m26"]), ("CAPES de physique-chimie", ORANGE, A["pc25"], A["pc26"])):
        y += 26
        e.append('<rect x="0" y="%d" width="14" height="4" fill="%s"/>' % (y - 6, col))
        e.append('<text x="22" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, lib))
        y += 22
        e.append('<text x="22" y="%d" font-size="%s" fill="%s">2025 : %s %% · 2026 : %s %%</text>' % (y, FS_MIN, col, v25, v26))
    y += 26
    for ligne in coupe("Point creux, 2026 : deux concours (bac+3 et bac+5), plus de postes, hors série. Deux CAPES seulement : "
                       "l'ensemble des concours figure dans la version détaillée.", 38):
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(ligne)))
        y += 18
    return finir_m(e, y + 6, t["source"], t["note"])


def parite_mobile(figs):
    """Chaque valeur dessinée dans la version mobile figure dans la description de la version détaillée ; police >= FS_MIN."""
    for fid in ("heures", "classes", "concours"):
        d, m = figs["lycee-%s.svg" % fid], figs["lycee-%s-m.svg" % fid]
        nombres_d = set(re.findall(r"\d+(?:,\d+)?", desc_de(d)))
        textes_m = re.findall(r'<text [^>]*font-weight="600"[^>]*>([^<]*)</text>', m) + \
            re.findall(r'<text [^>]*fill="(?:%s|%s)"[^>]*>([^<]*)</text>' % (BLEU, ORANGE), m)
        dessines = set(n for tx in textes_m for n in re.findall(r"\d+(?:,\d+)?", html.unescape(tx)) if not re.fullmatch(r"(19|20)\d\d", n))
        if not dessines:
            fail("parite mobile : %s -- aucune valeur dessinee lue (controle aveugle)" % fid)
        manquants = dessines - nombres_d
        if manquants:
            fail("parite mobile : %s -- valeurs dessinees absentes de la version detaillee : %s" % (fid, sorted(manquants)))
        tailles = [float(x) for x in re.findall(r'font-size="([0-9.]+)"', m)]
        if min(tailles) < FS_MIN:
            fail("parite mobile : %s -- police %.1f sous le minimum %.1f" % (fid, min(tailles), FS_MIN))


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
    for k, nom in (("maths", "capes_mathematiques"), ("pc", "capes_physique_chimie"), ("lp", "caplp_mathematiques_physique_chimie")):
        w.writerow(["couverture_concours_2026_double_session", nom, "2026", "%.1f" % c["t26"][k], "% (admis / postes, bac+3 et bac+5, ministère)"])
    for k in ("moins", "plus"):
        w.writerow(["heures_non_assurees_deciles_2024_2025", "etablissements_" + k + "_concernes", "total", c["dec"][k]["total"], "% des heures prevues (second degre public)"])
    for k in ("part_examens", "part_total"):
        w.writerow(["fermeture_lycee_gt_2024_2025", k, "", c["ferm"][k], "% du temps d'enseignement (lycee GT public, y compris LPO)"])
    for k in ("jours_examens", "jours_total"):
        w.writerow(["fermeture_lycee_gt_2024_2025", k, "", c["ferm"][k], "jours de fermeture totale"])
    for a, f in sorted(c["flux"].items()):
        for k in ("postes", "presents", "admis"):
            w.writerow(["concours_externes_second_degre_public", k, a, f[k], "nombre (annees publiees)"])
    for a, v in sorted(c["ens"].items()):
        w.writerow(["enseignants_formations_gt_lycee", "public_prive", a, v, "enseignants face a eleves, au prorata (RERS 9.09)"])
    for k, v in c["ens_pub"].items():
        for kk, x in v.items():
            w.writerow(["enseignants_public_2025_par_formation", k, kk, x, "enseignants (RERS 9.09, tableau 2)"])
    for a, v in sorted(c["contr"].items()):
        w.writerow(["contractuels", "part_enseignants_second_degre_public", a, v, "%"])
    for a, v in sorted(c["c1"].items()):
        w.writerow(["depense_par_lyceen_gt", "euros_2024", a, v, "EUR (prix 2024)"])
    w.writerow(["depense_par_lyceen_gt", "euros_2025_provisoire", c["c1_2025"]["annee"], c["c1_2025"]["gt"], "EUR (prix 2025, NI 26-42)"])
    for a, v in sorted(c["c3"].items()):
        w.writerow(["ocde_depense_publique_par_eleve_general", "France", a, v["FRA"], "USD PPA"])
        w.writerow(["ocde_depense_publique_par_eleve_general", "OCDE", a, v["OECD"], "USD PPA"])
    for k, v in sorted(c["acad"].items()):
        w.writerow(["eleves_par_structure_academie_2025", k, "", v, "eleves"])
    for code, r in sorted(c["bati"]["R"].items()):
        for k, v in r.items():
            if k != "nom":
                w.writerow(["bati_regions_rubrique_222", r["nom"], k, v, BATI_UNITES[k]])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    X = lire()
    c = calcul(X)
    c["bati"] = calcul_bati(json.loads((SRC / "extrait_bati.json").read_text(encoding="utf-8")))
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    A = affichage(c)
    log("Lycee GT : heures non assurees %s %% (organisation %s, individuelles %s) ; E/D %s ; CAPES maths %s/%s/%s ; OCDE x%s"
        % (A["h_total"], A["h_org"], A["h_indiv"], A["ed"], A["m23"], A["m24"], A["m25"], A["c3_pct"]))
    figs = {"lycee-heures.svg": fig_heures(c, A), "lycee-classes.svg": fig_classes(c, A), "lycee-concours.svg": fig_concours(c, A)}
    for fid, fn in (("heures", fig_heures_m), ("classes", fig_classes_m), ("concours", fig_concours_m)):
        figs["lycee-%s-m.svg" % fid] = fn(c, A, figs["lycee-%s.svg" % fid])
    parite_mobile(figs)   # avant --check : la parité se contrôle aussi sans écrire
    # Les hauteurs des <source> de la page sont recopiées : une figure mobile qui change de hauteur doit les faire suivre.
    page = (ROOT / "content" / "manque-t-il-des-professeurs" / "_index.md").read_text(encoding="utf-8")
    for fid in ("heures", "classes", "concours"):
        h_svg = re.search(r'viewBox="0 0 %d (\d+)"' % WM, figs["lycee-%s-m.svg" % fid]).group(1)
        h_page = re.search(r'srcset="/img/lycee-%s-m\.svg" width="%d" height="(\d+)"' % (fid, WM), page)
        if not h_page or h_page.group(1) != h_svg:
            fail("page : hauteur de lycee-%s-m.svg a %s dans le <source>, %s dans le SVG" % (fid, h_page and h_page.group(1), h_svg))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), parite des %d figures mobiles controlee, rien ecrit." % (n, len(A), 3))
        return 0
    import cairosvg
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "champ": "France ; lycée général et technologique sauf mention ; public et privé sous contrat sauf mention",
                        "source_calcul": "test décisif de l'auteur (protocole écrit avant calcul) ; extrait figé scripts/sources_lycee_professeurs/ (SHA256SUMS)"},
               "classes": {str(a): v for a, v in sorted(c["ed"].items())},
               "heures_non_assurees": {"2023-2024": c["h3"], "2024-2025": c["h4"]},
               "concours": {"capes_mathematiques": c["maths"], "capes_physique_chimie": c["pc"], "ensemble_externes": {str(a): v for a, v in c["nat"].items()},
                            "session_2026_ministere": {k: {"postes": c["p26"][k], "taux": round(c["t26"][k], 1)} for k in c["t26"]}},
               "heures_non_assurees_deciles_2024_2025": c["dec"],
               "fermeture_lycee_gt_2024_2025": c["ferm"],
               "concours_externes_postes_presents_admis": {str(a): v for a, v in sorted(c["flux"].items())},
               "enseignants_formations_gt": {"public_prive": {str(a): v for a, v in sorted(c["ens"].items())}, "public_2025": c["ens_pub"]},
               "depense_2025_provisoire": c["c1_2025"], "ocde_depp": c["ocde_depp"],
               "bati_regions_rubrique_222": c["bati"]["R"],
               "affichage": A}
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            same = {k: v for k, v in prev.items() if k not in ("releve_le", "_licence")} == json.loads(json.dumps(payload, ensure_ascii=False))
            if same and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c) \
                    and OUT_FIGURES.exists() \
                    and OUT_FIGURES.read_text(encoding="utf-8") == json.dumps(fiches(figs, A), ensure_ascii=False, indent=1) + "\n":
                # (10/10/2026) fiches « Réutiliser » comparées aussi : sans elles, une légende corrigée n'était jamais réécrite.
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
