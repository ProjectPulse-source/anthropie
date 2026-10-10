#!/usr/bin/env python3
"""update_langue_eleves.py -- ressource « Les élèves maîtrisent-ils moins bien la langue française ? » (bloc École et lycée,
troisième onglet).

Découverte de la page (dépôt de pilotage de l'auteur, 06_PROMOTION/RECHERCHE_LYCEES_LECTURE_2026-10-09, protocole écrit
avant calcul, commit ddab2bc ; verdict du 09/10/2026) : la langue des élèves ne recule pas d'un bloc. Les reculs les plus
anciens (orthographe et lecture en fin d'école, temps de lecture pour le plaisir à 15 ans) précèdent la généralisation
du smartphone chez les adolescents ; à la même dictée, l'orthographe des mots bouge peu quand les autres erreurs, surtout
grammaticales (NI 08.38, tableau 4), doublent ; PISA ne baisse qu'après 2012, quand PIRLS et CEDRE ne reculent pas
significativement sur des périodes qui recouvrent en partie cette baisse ; le vocabulaire n'est suivi par aucune série
publique. Prose corrigée après la contre-expertise PRO-20261009-202511 (arbitrage dans D:\PRO\.claude\external-audits).

Entrée : l'extrait FIGÉ du calcul, scripts/sources_langue_eleves/extrait_langue.json (écrit par extrait_langue.py du dépôt
de recherche, qui lit chaque valeur par une ancre dans les pièces archivées), contrôlé contre SHA256SUMS. Ce générateur
ne recalcule que des écarts et des tests simples ; il met en forme et GARDE : chaque qualificatif de la prose est une
condition sur les nombres (fonction gardes) ; si l'extrait la dément, arrêt.
Mise à jour : hors module de mise à jour ; rendez-vous de rattrapage : CEDRE maîtrise de la langue (cycle suivant de la
DEPP), évaluations de sixième et test de seconde (chaque automne), PISA 2029. Relancer extrait_langue.py (et calc_t7.py
pour PISA) dans le dossier de recherche, recopier l'extrait et son empreinte, relancer ce script.
Page en français seulement (exclusion déclarée : langue, programmes et statistique français).

Section « textes » : extrait_textes.json (Gate 0 de l'étude sur la langue offerte aux enfants, 10/10/2026).

Usage : python scripts/update_langue_eleves.py [--check] [--mutation=<nom>]  (noms : les branches de mutation())
Sorties : data/ et static/langue_eleves.json, static/langue_eleves.csv, data/figures_langue.json,
          static/img/langue-{chronologie,dictee,plaisir}.svg + .png
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

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_langue_eleves"
OUT_DATA = ROOT / "data" / "langue_eleves.json"
OUT_STATIC = ROOT / "static" / "langue_eleves.json"
OUT_CSV = ROOT / "static" / "langue_eleves.csv"
OUT_FIGURES = ROOT / "data" / "figures_langue.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/les-eleves-maitrisent-ils-moins-bien-la-langue-francaise/"

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
LICENCE = "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_URL
Q5, Q6 = "ST326Q05JA", "ST326Q06JA"
NIVEAUX_2023 = ("Sixième", "Quatrième", "Seconde générale et technologique", "Seconde professionnelle", "CAP")
DOMAINES_6E = ("Compréhension de l'écrit", "Lexique", "Compréhension de l'oral", "Grammaire", "Orthographe")


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
    return ("−" if neg else "") + " ".join(groupes) + ("," + frac if frac else "")


def nbp(v: float) -> str:
    """Précision publiée : la DEPP écrit « 18 » et « 3 » erreurs (sans décimale), « 10,7 » et « 2,1 » (une décimale)."""
    return nb(v, 0) if float(v) == int(v) else nb(v, 1)


# ------------------------------------------------------------------ données
def lire():
    for ligne in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        h, nom_ = ligne.split()
        if hashlib.sha256((SRC / nom_.lstrip("*")).read_bytes()).hexdigest() != h:
            fail("empreinte de %s differente de SHA256SUMS : extrait modifie hors du depot de recherche" % nom_)
    X = json.loads((SRC / "extrait_langue.json").read_text(encoding="utf-8"))
    # Gate 0 de l'étude « langue offerte aux enfants » (06_PROMOTION/RECHERCHE_LANGUE_OFFERTE_2026-10-10/gate0,
    # extrait_textes.py) : recensement Emmanuelle et rappel du catalogue de la BnF, pour la section « textes »
    X["textes_offerts"] = json.loads((SRC / "extrait_textes.json").read_text(encoding="utf-8"))
    return X


def effectif(d: float) -> int:
    """Ouvrages par période pour détecter un écart de d écarts-types (bilatéral 5 %, puissance 80 %)."""
    from math import ceil
    from statistics import NormalDist
    z = NormalDist().inv_cdf(0.975) + NormalDist().inv_cdf(0.80)
    return ceil(2 * z * z / (d * d))


def calcul(X):
    sm = {int(a): v for a, v in X["smartphone_12_17"].items()}
    seuil = min(a for a, v in sm.items() if v > 50)
    P = X["pisa_lecture"]
    # PISA 2000 -> 2012 : test prudent (sans erreur de liaison, donc plus severe que le test de l'OCDE)
    d_00_12 = P["score"]["2012"] - P["score"]["2000"]
    se_00_12 = (P["et"]["2012"] ** 2 + P["et"]["2000"] ** 2) ** 0.5
    t7 = X["t7"]["questions"]
    return dict(X=X, sm=sm, seuil=seuil, P=P, d_00_12=d_00_12, se_00_12=se_00_12, q5=t7[Q5], q6=t7[Q6],
                dic=X["dictee"], lc=X["lecture_cm2"], ce=X["cedre_ecole"], cc=X["cedre_college"], six=X["sixieme"],
                pirls=X["pirls"], sec=X["seconde_francais"], oc=X["ocde_lecture_loisir"], cul=X["culture"],
                pr=X["pratiques_2023_ne_lit_pas_pour_plaisir"], releve=X["releve_le"],
                dty=X["dictee_types_1987_2007"], cct=X["cedre_college_textes"], tx=X["textes_offerts"])


def mutation(c):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if not m:
        return None
    c["X"] = X = json.loads(json.dumps(c["X"]))
    if m == "lexicales":  # les erreurs lexicales auraient augmente autant que les autres
        X["dictee"]["lexicales"]["2021"] = 9.0
    elif m == "temps_lecture":  # le temps de lecture n'aurait pas baisse de 2000 a 2009
        X["ocde_lecture_loisir"]["heures_semaine"]["d2009_2000"] = -0.1
    elif m == "pisa_2012":  # PISA aurait deja recule entre 2000 et 2012
        X["pisa_lecture"]["score"]["2012"] = 480.0
    elif m == "cedre":  # la hausse de CEDRE fin d'ecole ne serait pas significative
        X["cedre_ecole"]["significatif"]["2021"] = False
    elif m == "joyread":
        X["ocde_lecture_loisir"]["joyread"]["variation"] = -0.02
    elif m == "pratiques":  # la seconde professionnelle lirait autant que la sixieme
        X["pratiques_2023_ne_lit_pas_pour_plaisir"]["Seconde professionnelle"] = 12.0
    elif m == "ecrans":  # la part des eleves a plus de 3 h aurait augmente
        X["t7"]["questions"][Q5]["c"]["part_plus_de_3h"]["2025"][0] = 40.0
    elif m == "non_reponse":
        X["t7"]["questions"][Q5]["a"]["2025"]["non_reponse"][0] = 13.0
    elif m == "lexique_ips":  # l'ecart social serait plus faible en lexique qu'ailleurs
        X["sixieme"]["satisfaisant_par_domaine_2025"]["Groupe d'IPS 5"]["Lexique"] = 40.0
    elif m == "seconde":
        X["seconde_francais"]["GT"]["2025"] = 272.0
    elif m == "smartphone":
        X["smartphone_12_17"]["2013"] = 45.0
    elif m == "college":  # l'education prioritaire ne reculerait pas significativement en fin de college
        X["cedre_college"]["groupes_significatif"]["EP"]["2021"] = False
    elif m == "sixieme":
        X["sixieme"]["score_francais"]["2025"] = 249.0
    elif m == "pirls":
        X["pirls"]["2016"]["sup_2021"] = True
    elif m == "dictee_rythme":  # la hausse 2015-2021 serait aussi forte que 2007-2015
        X["dictee"]["total"]["2021"] = 21.3
    elif m == "citation":
        X["dictee"]["citations_depp"] = X["dictee"]["citations_depp"][:1]
    elif m == "tranches":  # la baisse se verrait aussi chez les eleves qui declarent peu d'ecran
        X["t7"]["questions"][Q5]["b"]["aucune_ou_1h"]["baisse_sig"] = True
    elif m == "grammaticales":  # la hausse 1987-2007 ne serait pas surtout grammaticale
        X["dictee_types_1987_2007"]["grammaticales"]["2007"] = 8.0  # meme total : la hausse passerait par la ponctuation
        X["dictee_types_1987_2007"]["ponctuation"]["2007"] = 3.7
    elif m == "emmanuelle":  # le francais aurait ete saisi dans la base Emmanuelle
        X["textes_offerts"]["emmanuelle"]["disciplines_saisies"].append("français")
    elif m == "rappel":  # le cadre par titre retrouverait Daniel et Valerie
        X["textes_offerts"]["temoins_bnf"]["daniel et valérie"]["r1"] = 5
    elif m == "ecart_ep":  # le calcul des tableaux ne retrouverait pas l'ecart ecrit par la DEPP
        X["cedre_college"]["groupes"]["Public hors EP"]["2021"] = 245.0
    else:
        fail("mutation inconnue : %s" % m)
    c.update(calcul(X))
    return m


# ------------------------------------------------------------------ gardes : chaque qualificatif de la prose
def gardes(c):
    n = [0]

    def g(cond, phrase):
        n[0] += 1
        if not cond:
            fail("garde : %s" % phrase)

    dic, lc, ce, cc, six, P, oc = c["dic"], c["lc"], c["ce"], c["cc"], c["six"], c["P"], c["oc"]
    tot, lx = dic["total"], dic["lexicales"]
    autres = {a: tot[a] - lx[a] for a in tot}
    # chronologie
    g(c["seuil"] == 2013 and c["sm"][2011] < 25, "« en 2013, plus de la moitié des 12-17 ans » ; « en 2011, moins d'un quart »")
    g(dic["hausse_significative_1987_2007"] and 2007 < c["seuil"], "dictée : hausse significative des erreurs de 1987 à 2007, « avant le smartphone »")
    g(lc["stable_1987_1997"] and lc["baisse_significative_1997_2007"] and lc["score"]["2007"] < lc["score"]["1997"] <= lc["score"]["1987"] + 0.05,
      "lecture CM2 : « stable de 1987 à 1997, en baisse significative de 1997 à 2007 »")
    hs = oc["heures_semaine"]
    g(hs["d2009_2000"] < 0 and abs(hs["d2009_2000"]) >= 1.96 * hs["d2009_2000_et"] and 2009 < c["seuil"],
      "temps de lecture pour le plaisir à 15 ans : baisse significative de 2000 à 2009, « avant le smartphone »")
    g(abs(hs["d2018_2009"]) < 1.96 * hs["d2018_2009_et"], "temps de lecture : « sans évolution significative de 2009 à 2018 »")
    g(abs(c["d_00_12"]) < 1.96 * c["se_00_12"], "PISA : « aucune baisse significative de 2000 à 2012 »")
    s = P["score"]
    g(s["2012"] > s["2015"] > s["2018"] > s["2022"] > s["2025"], "PISA : « recule à chaque enquête depuis 2012 »")
    v12 = P["variation_vers_2025"]["2012"], P["variation_vers_2025_et"]["2012"]
    g(v12[0] < 0 and abs(v12[0]) >= 1.96 * v12[1], "PISA : baisse significative de 2012 à 2025")
    g(not c["pirls"]["2016"]["sup_2021"] and c["pirls"]["2021"]["score"] >= c["pirls"]["2016"]["score"] - 5,
      "PIRLS : « sans recul significatif de 2016 à 2021 »")
    g(c["X"]["pirls_baisses_2016_significatives_a_5_10_15_ans"] and c["pirls"]["2016"]["score"] < c["pirls"]["2011"]["score"],
      "PIRLS : baisse significative de 2011 à 2016")
    g(ce["significatif"]["2021"] and ce["score"]["2021"] > ce["score"]["2015"] and ce["stable_2003_2015_declare"],
      "CEDRE fin d'école : « stable de 2003 à 2015, en hausse significative en 2021 »")
    g(not cc["significatif"]["2021"] and abs(cc["score"]["2021"] - cc["score"]["2015"]) < 5, "CEDRE fin de collège : « sans évolution significative »")
    sf = six["score_francais"]
    g(sf["2025"] > sf["2017"] and min(sf.values()) == sf["2017"] and max(sf.values()) == sf["2021"] == sf["2020"] and sf["2025"] < sf["2021"],
      "sixième : « au-dessus de 2017, après un sommet en 2020-2021 »")
    gt = c["sec"]["GT"]
    g(abs(gt["2025"] - gt["2019"]) < 1 and gt["2021"] == max(gt.values()), "seconde GT : « revient en 2025 au niveau de 2019, après un sommet en 2020-2021 »")
    L = lignes_chrono(c)
    g(len(L) == 11, "chronologie : « onze mesures »")
    g(sum(1 for _, _, seg in L for u, v, sg, bs in seg if v < c["seuil"] - 1 and sg and bs) == 3, "chronologie : « trois reculs sont acquis avant » le smartphone")
    g(s["2006"] < s["2000"] and s["2009"] > s["2006"] and s["2012"] >= s["2000"], "PISA : « un creux en 2006 sans tendance »")
    # vocabulaire et dictée
    cit = set(dic["citations_depp"])
    g({"mots_usuels_neuf_sur_dix", "accords_baisse_1987_2015_seulement", "hausse_2015_2021_deux_fois_moindre"} <= cit,
      "dictée : citations de la DEPP (« neuf élèves sur dix », baisse des accords « sur 1987-2015 », hausse « deux fois moins forte »)")
    g(1.7 <= (tot["2015"] - tot["2007"]) / (tot["2021"] - tot["2015"]) <= 2.6, "dictée : hausse de 2015 à 2021 « deux fois moins forte » que de 2007 à 2015")
    g(lx["2021"] - lx["1987"] < 0.25 * (tot["2021"] - tot["1987"]), "dictée : l'orthographe des mots « bouge peu » au regard du total")
    g(1.8 <= autres["2021"] / autres["1987"] < 2.2, "dictée : les autres erreurs « ont presque doublé, ou doublé »")
    dty = c["dty"]
    g(dty["citation_depp"] == "principalement_grammaticales" and dty["lexicales"]["1987"] == lx["1987"] and dty["lexicales"]["2007"] == lx["2007"]
      and all(abs(sum(dty[k][a] for k in ("lexicales", "grammaticales", "ponctuation", "autres")) - tot[a]) <= 0.15 for a in ("1987", "2007")),
      "dictée : la décomposition de la NI 08.38 retrouve les totaux et les erreurs lexicales de la NI 22.37")
    gr = dty["grammaticales"]
    g(gr["2007"] - gr["1987"] >= 0.8 * (tot["2007"] - tot["1987"]) and dty["ponctuation"]["2007"] <= dty["ponctuation"]["1987"],
      "dictée : de 1987 à 2007, la hausse est « surtout grammaticale » (au moins les quatre cinquièmes), la ponctuation ne monte pas")
    g(dic["vingt_cinq_ou_plus"]["2021"] > 3.5 * dic["vingt_cinq_ou_plus"]["1987"], "dictée : la part à 25 erreurs ou plus « a quadruplé »")
    sat = six["satisfaisant_par_domaine_2025"]
    ecarts = {d: sat["Groupe d'IPS 5"][d] - sat["Groupe d'IPS 1"][d] for d in DOMAINES_6E}
    g(max(ecarts, key=ecarts.get) == "Lexique", "sixième 2025 : l'écart social est « le plus grand en lexique »")
    g(sat["Groupe d'IPS 5"]["Lexique"] > 2 * sat["Groupe d'IPS 1"]["Lexique"], "sixième 2025 : en lexique, « plus du double » dans les collèges favorisés")
    # lecture pour le plaisir
    jr = oc["joyread"]
    g(jr["variation"] < 0 and abs(jr["variation"]) >= 1.96 * jr["variation_et"], "OCDE : le plaisir de lire baisse significativement de 2009 à 2018")
    ob = oc["lit_seulement_si_oblige"]
    g(ob["2009"] < 35 and ob["2018"] > 40, "OCDE : « je ne lis que si j'y suis obligé », « d'un tiers à plus de quatre sur dix »")
    pr = c["pr"]
    g(all(pr[a] < pr[b] for a, b in zip(NIVEAUX_2023[:3], NIVEAUX_2023[1:4])), "DEPP 2023 : la part qui ne lit pas pour le plaisir « croît de la sixième à la seconde professionnelle »")
    g(45 <= pr["Seconde professionnelle"] < 50 and 11 <= pr["Sixième"] < 14, "DEPP 2023 : « un élève de sixième sur huit », « près de la moitié » en seconde professionnelle")
    v20 = c["cul"]["vingt_livres_ou_plus"]["15_24"]
    g(v20["1988"] > v20["1997"] > v20["2008"], "Culture : les forts lecteurs de 15-24 ans reculent de 1988 à 2008")
    # écarts
    gs = cc["groupes_significatif"]
    g(gs["EP"]["2021"] and gs["Garçons"]["2021"] and cc["groupes"]["EP"]["2021"] < cc["groupes"]["EP"]["2015"]
      and cc["groupes"]["Garçons"]["2021"] < cc["groupes"]["Garçons"]["2015"], "CEDRE fin de collège : éducation prioritaire et garçons « en baisse significative »")
    ct, grp = c["cct"], cc["groupes"]
    ec = {a: grp["Public hors EP"][a] - grp["EP"][a] for a in ("2015", "2021")}
    g(all(round(ec[a]) == ct["ecart_hors_ep_ep_points"][a] for a in ec) and ec["2021"] > ec["2015"] and ct["ecart_ep_dit_augmenter"]
      and not gs["Public hors EP"]["2021"] and not ct["test_de_l_ecart_publie"]
      and ct["ecart_filles_garcons_dit_augmenter"] and grp["Filles"]["2021"] - grp["Garçons"]["2021"] > grp["Filles"]["2015"] - grp["Garçons"]["2015"],
      "CEDRE fin de collège : l'écart avec le public hors éducation prioritaire « passe de 17 à 22 points », celui entre filles et garçons « augmente aussi » (DEPP), sans test publié")
    g(not ce["secteurs_significatif"]["EP"]["2021"] and ce["secteurs_significatif"]["Public hors EP"]["2021"],
      "CEDRE fin d'école : « la hausse vient du public hors éducation prioritaire »")
    # textes offerts (Gate 0)
    em, tb = c["tx"]["emmanuelle"], c["tx"]["temoins_bnf"]
    g(len(em["disciplines_saisies"]) == 8 and "français" not in em["disciplines_saisies"] and em["francais_en_cours"]
      and not em["daniel_et_valerie_trouve"], "Emmanuelle : huit disciplines saisies, « pas le français », dont la saisie est annoncée en cours")
    g(all(tb[k]["periode"] == "1970s" and tb[k]["catalogue"] > 0 and tb[k]["r1"] == 0 for k in ("daniel et valérie", "rémi et colette")),
      "BnF : les méthodes des années 1970 sont au catalogue, « aucune n'est retrouvée » par le titre")
    g(0 < tb["taoki"]["r1"] < tb["taoki"]["catalogue"], "BnF : Taoki « retrouvé en partie »")
    g(effectif(0.5) > 3 * effectif(1.0), "précision : un écart deux fois plus petit demande « environ quatre fois plus » d'ouvrages")
    # écrans (PISA 2022-2025)
    for q in (c["q5"], c["q6"]):
        p = q["c"]["part_plus_de_3h"]
        g(p["2025"][0] < p["2022"][0], "PISA : la part des élèves à plus de 3 h de numérique de loisir « ne progresse pas, elle recule »")
        g(q["c_verdict"] == "indetermine", "PISA : verdict de substitution « indéterminé » (bornes de non-réponse)")
    a5 = c["q5"]["a"]
    r = a5["2025"]["non_reponse"][0] / a5["2022"]["non_reponse"][0]
    g(1.7 <= r < 2.0, "PISA : la non-réponse « a presque doublé »")
    g(20 <= a5["2025"]["non_reponse"][0] < 25, "PISA 2025 : « près d'un élève sur quatre » ne répond pas")
    g(all(a5[an]["lecture_repondants"][0] - a5[an]["lecture_non_repondants"][0] > 80 for an in ("2022", "2025")),
      "PISA : les non-répondants ont des scores « très inférieurs »")
    b = c["q5"]["b"]
    g(b["3_a_5h"]["baisse_sig"] and b["plus_de_5h"]["baisse_sig"] and not b["aucune_ou_1h"]["baisse_sig"] and not b["1_a_3h"]["baisse_sig"],
      "PISA : la baisse 2022-2025 est significative chez ceux qui déclarent le plus d'écran, pas chez les autres")
    return n[0]


# ------------------------------------------------------------------ affichage
def affichage(c):
    A = {}
    dic, lc, ce, cc, six, P, oc = c["dic"], c["lc"], c["ce"], c["cc"], c["six"], c["P"], c["oc"]
    tot, lx = dic["total"], dic["lexicales"]
    for a in ("1987", "2007", "2015", "2021"):
        A["tot" + a[2:]] = nbp(tot[a])
        A["lex" + a[2:]] = nbp(lx[a])
        A["aut" + a[2:]] = nbp(round(tot[a] - lx[a], 1))
    A["peu87"], A["peu21"] = nb(dic["deux_erreurs_ou_moins"]["1987"]), nb(dic["deux_erreurs_ou_moins"]["2021"])
    A["bcp87"], A["bcp21"] = nb(dic["vingt_cinq_ou_plus"]["1987"]), nb(dic["vingt_cinq_ou_plus"]["2021"])
    A["lcm2_07"] = nb(-lc["score"]["2007"], 2)
    A["smart_seuil"] = str(c["seuil"])
    A["smart11"], A["smart13"] = nb(c["sm"][2011], 0), nb(c["sm"][c["seuil"]], 0)
    s = P["score"]
    for a in ("2000", "2012", "2018", "2022", "2025"):
        A["pisa" + a[2:]] = nb(s[a], 0)
    A["pisa_v12"] = nb(-P["variation_vers_2025"]["2012"], 0)
    pi = c["pirls"]
    A["pirls01"], A["pirls11"], A["pirls16"], A["pirls21"] = (nb(pi[a]["score"], 0) for a in ("2001", "2011", "2016", "2021"))
    A["ce03"], A["ce15"], A["ce21"] = nb(ce["score"]["2003"], 0), nb(ce["score"]["2015"], 0), nb(ce["score"]["2021"], 0)
    A["cc15"], A["cc21"] = nb(cc["score"]["2015"], 0), nb(cc["score"]["2021"], 0)
    g_ = cc["groupes"]
    A["ccep15"], A["ccep21"] = nb(g_["EP"]["2015"], 0), nb(g_["EP"]["2021"], 0)
    A["ccg15"], A["ccg21"] = nb(g_["Garçons"]["2015"], 0), nb(g_["Garçons"]["2021"], 0)
    A["ccec15"], A["ccec21"] = (nb(c["cct"]["ecart_hors_ep_ep_points"][a], 0) for a in ("2015", "2021"))
    dty = c["dty"]
    A["gram87"], A["gram07"] = nbp(dty["grammaticales"]["1987"]), nbp(dty["grammaticales"]["2007"])
    sf = six["score_francais"]
    A["six17"], A["six21"], A["six25"] = nb(sf["2017"], 0), nb(sf["2021"], 0), nb(sf["2025"], 0)
    gt = c["sec"]["GT"]
    A["sec19"], A["sec21"], A["sec25"] = nb(gt["2019"], 0), nb(gt["2021"], 0), nb(gt["2025"], 0)
    sat = six["satisfaisant_par_domaine_2025"]
    A["lex_sat"] = nb(sat["Ensemble"]["Lexique"])
    A["lex_ips1"], A["lex_ips5"] = nb(sat["Groupe d'IPS 1"]["Lexique"]), nb(sat["Groupe d'IPS 5"]["Lexique"])
    hs = oc["heures_semaine"]
    A["h00"], A["h09"], A["h18"] = nb(hs["2000"]), nb(hs["2009"]), nb(hs["2018"])
    ob = oc["lit_seulement_si_oblige"]
    A["obl09"], A["obl18"] = nb(ob["2009"], 0), nb(ob["2018"], 0)
    pr = c["pr"]
    A["np6"], A["np4"], A["np2gt"], A["np2pro"], A["npcap"] = (nb(pr[k], 0) for k in NIVEAUX_2023)
    v20 = c["cul"]["vingt_livres_ou_plus"]["15_24"]
    A["cul88"], A["cul08"] = nb(v20["1988"], 0), nb(v20["2008"], 0)
    for q, k in ((c["q5"], "e"), (c["q6"], "w")):
        p = q["c"]["part_plus_de_3h"]
        A[k + "3h22"], A[k + "3h25"] = nb(p["2022"][0], 0), nb(p["2025"][0], 0)
    a5 = c["q5"]["a"]
    A["nr22"], A["nr25"] = nb(a5["2022"]["non_reponse"][0], 0), nb(a5["2025"]["non_reponse"][0], 0)
    A["nrs25"], A["reps25"] = nb(a5["2025"]["lecture_non_repondants"][0], 0), nb(a5["2025"]["lecture_repondants"][0], 0)
    b = c["q5"]["b"]
    A["d35"], A["d5p"] = nb(-b["3_a_5h"]["variation"], 0), nb(-b["plus_de_5h"]["variation"], 0)
    em, tb = c["tx"]["emmanuelle"], c["tx"]["temoins_bnf"]
    A["emma_ndisc"], A["emma_notices"] = nb(len(em["disciplines_saisies"]), 0), nb(em["notices_base"], 0)
    A["dv_cat"], A["dv_r1"] = nb(tb["daniel et valérie"]["catalogue"], 0), nb(tb["daniel et valérie"]["r1"], 0)
    A["rc_cat"], A["rc_r1"] = nb(tb["rémi et colette"]["catalogue"], 0), nb(tb["rémi et colette"]["r1"], 0)
    A["taoki_cat"], A["taoki_r1"] = nb(tb["taoki"]["catalogue"], 0), nb(tb["taoki"]["r1"], 0)
    A["n_d05"], A["n_d1"] = nb(effectif(0.5), 0), nb(effectif(1.0), 0)
    j, mo, an = c["tx"]["releve_le"].split("-")[2], c["tx"]["releve_le"].split("-")[1], c["tx"]["releve_le"].split("-")[0]
    A["tx_date"] = "%d %s %s" % (int(j), ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
                                          "novembre", "décembre")[int(mo) - 1], an)
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
    "chronologie": dict(
        titre="La langue des élèves : quand chaque mesure recule, tient ou progresse",
        source="DEPP (Notes d'Information) ; OCDE (PISA 2025 ; 21st-Century Readers) ; IEA (PIRLS) ; ministère de la Culture ; CREDOC",
        note="Chaque ligne a sa propre échelle ; seul le sens est montré. Plein : test publié (PISA 2000-2012 : test de l'auteur) ; tirets : sans test.",
        montre="Les reculs les plus anciens (dictée et lecture en CM2, temps de lecture pour le plaisir à 15 ans) précèdent 2013 ; PISA ne baisse significativement qu'après 2012, quand PIRLS et CEDRE ne reculent pas significativement sur des périodes qui recouvrent en partie cette baisse."),
    "dictee": dict(
        titre="La même dictée en CM2 : nombre moyen d'erreurs",
        source="DEPP, Note d'Information 22.37 (dictée de 67 mots, 1987, 2007, 2015, 2021 ; secteur public) ; NI 08.38 pour 1987-2007",
        note="Erreurs lexicales : orthographe des mots eux-mêmes. Autres erreurs : grammaire (accords, conjugaison), ponctuation, oublis (total moins lexicales).",
        montre="L'orthographe des mots eux-mêmes bouge peu ; ce sont les autres erreurs, surtout grammaticales, qui ont presque doublé, avant de se stabiliser après 2015."),
    "plaisir": dict(
        titre="Élèves qui déclarent ne pas lire pour leur plaisir, selon la classe (2023)",
        source="DEPP, Note d'Information 25.66, figure 1.1 web (questionnaires des évaluations nationales, septembre 2023)",
        note="Une seule enquête : l'écart entre classes compare des élèves différents la même année, ce n'est pas une évolution dans le temps.",
        montre="Une part croissante d'élèves ne lit pas pour son plaisir, de la sixième à la seconde ; près de la moitié en seconde professionnelle."),
}


def statut(sig, baisse):
    """(couleur, plein) : plein = significativité publiée ; couleur = sens (orange recul, bleu hausse, gris sans évolution)."""
    if sig is None:
        return (ORANGE if baisse else BLEU), False
    if sig:
        return (ORANGE if baisse else BLEU), True
    return GRIS, True


def lignes_chrono(c):
    dic, lc, ce, cc, six, P, oc = c["dic"], c["lc"], c["ce"], c["cc"], c["six"], c["P"], c["oc"]
    pi, sf, gt, hs = c["pirls"], six["score_francais"], c["sec"]["GT"], oc["heures_semaine"]
    v12 = P["variation_vers_2025"]["2012"], P["variation_vers_2025_et"]["2012"]
    jr = oc["joyread"]
    v20 = c["cul"]["vingt_livres_ou_plus"]["15_24"]
    L = [
        ("PIRLS, lecture", "CM1", [(2001, 2006, None, pi["2006"]["score"] < pi["2001"]["score"]),
                                   (2006, 2011, None, pi["2011"]["score"] < pi["2006"]["score"]),
                                   (2011, 2016, True, True), (2016, 2021, pi["2016"]["sup_2021"], pi["2021"]["score"] < pi["2016"]["score"])]),
        ("Dictée (erreurs en hausse = recul)", "CM2", [(1987, 2007, True, True), (2007, 2015, None, True), (2015, 2021, None, True)]),
        ("Lecture, épreuves de 1987", "CM2", [(1987, 1997, False, True), (1997, 2007, True, True)]),
        ("CEDRE, maîtrise de la langue", "CM2", [(2003, 2009, False, False), (2009, 2015, False, False),
                                                 (2015, 2021, ce["significatif"]["2021"], ce["score"]["2021"] < ce["score"]["2015"])]),
        ("Évaluation de début de sixième", "6e", [(2017, 2021, None, sf["2021"] < sf["2017"]), (2021, 2025, None, sf["2025"] < sf["2021"])]),
        ("CEDRE, langue et littératie", "3e", [(2015, 2021, cc["significatif"]["2021"], cc["score"]["2021"] < cc["score"]["2015"])]),
        ("PISA, compréhension de l'écrit", "15 ans", [(2000, 2012, abs(c["d_00_12"]) >= 1.96 * c["se_00_12"], c["d_00_12"] < 0),
                                                       (2012, 2025, abs(v12[0]) >= 1.96 * v12[1], v12[0] < 0)]),
        ("PISA, temps de lecture-plaisir", "15 ans", [(2000, 2009, abs(hs["d2009_2000"]) >= 1.96 * hs["d2009_2000_et"], hs["d2009_2000"] < 0),
                                                       (2009, 2018, abs(hs["d2018_2009"]) >= 1.96 * hs["d2018_2009_et"], hs["d2018_2009"] < 0)]),
        ("PISA, plaisir de lire (indice)", "15 ans", [(2009, 2018, abs(jr["variation"]) >= 1.96 * jr["variation_et"], jr["variation"] < 0)]),
        ("Test d'entrée, français (GT)", "seconde", [(2019, 2021, None, gt["2021"] < gt["2019"]), (2021, 2025, None, gt["2025"] < gt["2021"])]),
        ("20 livres ou plus dans l'année", "15-24 ans", [(1988, 1997, None, v20["1997"] < v20["1988"]), (1997, 2008, None, v20["2008"] < v20["1997"])]),
    ]
    return L


def fig_chronologie(c, A):
    t = FIG["chronologie"]
    L = lignes_chrono(c)
    a0, a1, x0, x1 = 1985, 2026, 262, 704
    sx = lambda a: x0 + (x1 - x0) * (a - a0) / (a1 - a0)
    top, pas = 74, 30
    h = top + pas * len(L) + 70
    mots = {(ORANGE, True): "recul significatif", (BLEU, True): "hausse significative", (GRIS, True): "sans évolution significative",
            (ORANGE, False): "recul, sans test publié", (BLEU, False): "hausse, sans test publié"}
    desc = "Frise 1985-2026, une ligne par mesure, sens de chaque intervalle ; repère : %s, plus de la moitié des 12-17 ans équipés d'un smartphone. " % A["smart_seuil"] + " ; ".join(
        "%s (%s) : %s" % (lib, pop, ", ".join("%d-%d %s" % (u, v, mots[statut(sg, bs)]) for u, v, sg, bs in seg)) for lib, pop, seg in L) + "."
    e = tete("lan-c", t["titre"], desc, h + 52)
    xs = sx(c["seuil"])
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#f1efec"/>' % (xs, top - 22, x1 - xs, pas * len(L) + 22))
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.2"/>' % (xs, top - 22, xs, top + pas * len(L), INK2))
    e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="end">%s : plus de la moitié des 12-17 ans ont un smartphone →</text>'
             % (xs - 4, top - 28, INK2, A["smart_seuil"]))
    for a in range(1990, 2026, 5):
        e.append('<text x="%.1f" y="%d" font-size="9.5" fill="%s" text-anchor="middle">%d</text>' % (sx(a), top + pas * len(L) + 14, MUTED, a))
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="0.5"/>' % (sx(a), top - 10, sx(a), top + pas * len(L), GRID))
    for i, (lib, pop, seg) in enumerate(L):
        y = top + pas * i + 8
        e.append('<text x="0" y="%d" font-size="11" fill="%s">%s</text>' % (y + 4, INK, esc(lib)))
        e.append('<text x="%d" y="%d" font-size="10" fill="%s" text-anchor="end">%s</text>' % (x0 - 10, y + 4, MUTED, esc(pop)))
        for u, v, sg, bs in seg:
            col, plein = statut(sg, bs)
            e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"%s/>'
                     % (sx(u), y, sx(v), y, col, "4" if plein else "3", "" if plein else ' stroke-dasharray="5 3"'))
        for a in sorted({u for u, *_ in seg} | {v for _, v, *_ in seg}):
            e.append('<circle cx="%.1f" cy="%d" r="3.2" fill="#ffffff" stroke="%s" stroke-width="1.4"/>' % (sx(a), y, INK2))
    yl = top + pas * len(L) + 34
    x = 0
    for (col, plein), lib in ((( ORANGE, True), "recul significatif"), ((GRIS, True), "sans évolution significative"),
                              ((BLEU, True), "hausse significative"), ((ORANGE, False), "tirets : sans test publié")):
        e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="4"%s/>' % (x, yl, x + 22, yl, col, "" if plein else ' stroke-dasharray="5 3"'))
        e.append('<text x="%d" y="%d" font-size="10" fill="%s">%s</text>' % (x + 28, yl + 4, INK2, esc(lib)))
        x += 34 + 7 * len(lib)
    return pied(e, h + 2, t["source"], t["note"])


def fig_dictee(c, A):
    t = FIG["dictee"]
    tot, lx = c["dic"]["total"], c["dic"]["lexicales"]
    ans = ("1987", "2007", "2015", "2021")
    vmax = 25.0
    x0, bw, gap, base, hmax = 110, 90, 60, 300, 220
    sy = lambda v: hmax * v / vmax
    desc = "Barres empilées, nombre moyen d'erreurs à la même dictée en CM2 : " + " ; ".join(
        "%s : %s erreurs lexicales et %s autres erreurs, %s au total" % (a, nbp(lx[a]), nbp(round(tot[a] - lx[a], 1)), nbp(tot[a])) for a in ans) + "."
    h = base + 60
    e = tete("lan-d", t["titre"], desc, h + 52)
    for v in (0, 5, 10, 15, 20, 25):
        y = base - sy(v)
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (x0 - 10, y, W - 40, y, GRID))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d</text>' % (x0 - 16, y + 3.5, MUTED, v))
    for i, a in enumerate(ans):
        x = x0 + i * (bw + gap)
        l, o = lx[a], tot[a] - lx[a]
        e.append('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s"/>' % (x, base - sy(l), bw, sy(l), BLEU))
        e.append('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s"/>' % (x, base - sy(l + o), bw, sy(o), ORANGE))
        e.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="600" fill="%s" text-anchor="middle">%s</text>' % (x + bw / 2, base - sy(l + o) - 6, INK, nbp(tot[a])))
        e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="#ffffff" text-anchor="middle">%s</text>' % (x + bw / 2, base - sy(l) / 2 + 4, nbp(l)))
        e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="#ffffff" text-anchor="middle">%s</text>' % (x + bw / 2, base - sy(l) - sy(o) / 2 + 4, nbp(round(o, 1))))
        e.append('<text x="%.1f" y="%d" font-size="11.5" fill="%s" text-anchor="middle">%s</text>' % (x + bw / 2, base + 16, INK2, a))
    yl = base + 40
    for k, (col, lib) in enumerate(((BLEU, "Erreurs lexicales (orthographe des mots)"), (ORANGE, "Autres erreurs (grammaire, ponctuation, oublis)"))):
        e.append('<rect x="%d" y="%d" width="12" height="12" fill="%s"/>' % (k * 300, yl - 10, col))
        e.append('<text x="%d" y="%d" font-size="10.5" fill="%s">%s</text>' % (k * 300 + 18, yl, INK2, esc(lib)))
    return pied(e, h + 2, t["source"], t["note"])


def fig_plaisir(c, A):
    t = FIG["plaisir"]
    pr = c["pr"]
    libs = {"Sixième": "Sixième", "Quatrième": "Quatrième", "Seconde générale et technologique": "Seconde générale et techno.",
            "Seconde professionnelle": "Seconde professionnelle", "CAP": "Première année de CAP"}
    x0, x1, top, pas = 200, 640, 44, 40
    sx = lambda v: (x1 - x0) * v / 60
    desc = "Barres, part des élèves qui déclarent ne pas lire pour leur plaisir en 2023 : " + " ; ".join(
        "%s %s %%" % (libs[k], nb(pr[k], 0)) for k in NIVEAUX_2023) + "."
    h = top + pas * len(NIVEAUX_2023) + 10
    e = tete("lan-p", t["titre"], desc, h + 52)
    for i, k in enumerate(NIVEAUX_2023):
        y = top + pas * i
        e.append('<text x="0" y="%d" font-size="11.5" fill="%s">%s</text>' % (y + 18, INK, esc(libs[k])))
        e.append('<rect x="%d" y="%d" width="%.1f" height="22" fill="%s"/>' % (x0, y + 4, sx(pr[k]), ORANGE))
        e.append('<text x="%.1f" y="%d" font-size="12" font-weight="600" fill="%s">%s %%</text>' % (x0 + sx(pr[k]) + 8, y + 20, INK, nb(pr[k], 0)))
    return pied(e, h + 2, t["source"], t["note"])


def fiches(figs):
    out = []
    for fid in ("chronologie", "dictee", "plaisir"):
        svg = figs["langue-%s.svg" % fid]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        out.append(dict(id=fid, fichier="langue-" + fid, titre=titre, montre=FIG[fid]["montre"], source=cart[0], precaution=cart[1]))
    return {"fr": out}


def csv_texte(c):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "variable", "cle", "valeur", "unite"])
    X = c["X"]
    for k in ("total", "lexicales", "deux_erreurs_ou_moins", "vingt_cinq_ou_plus"):
        for a, v in sorted(X["dictee"][k].items()):
            w.writerow(["depp_dictee_cm2", k, a, v, "erreurs (moyenne)" if k in ("total", "lexicales") else "% des eleves"])
    for k in ("lexicales", "grammaticales", "ponctuation", "autres"):
        for a, v in sorted(X["dictee_types_1987_2007"][k].items()):
            w.writerow(["depp_dictee_cm2_types_ni08_38", k, a, v, "erreurs (moyenne)"])
    for a, v in sorted(X["cedre_college_textes"]["ecart_hors_ep_ep_points"].items()):
        w.writerow(["depp_cedre_fin_college", "ecart public hors EP - EP (texte de la DEPP)", a, v, "points ; evolution sans test publie"])
    for a, v in sorted(X["lecture_cm2"]["score"].items()):
        w.writerow(["depp_lecture_cm2_epreuves_1987", "score", a, v, "ecart-type de 1987"])
    for a, v in sorted(X["cedre_ecole"]["score"].items()):
        w.writerow(["depp_cedre_fin_ecole", "score", a, v, "points (250 en 2003)" + (" ; evolution significative" if X["cedre_ecole"]["significatif"][a] else "")])
    for g_, s in X["cedre_college"]["groupes"].items():
        for a, v in sorted(s.items()):
            w.writerow(["depp_cedre_fin_college", g_, a, v, "points (250 en 2015)" + (" ; evolution significative" if X["cedre_college"]["groupes_significatif"][g_][a] else "")])
    for a, v in sorted(X["cedre_college"]["score"].items()):
        w.writerow(["depp_cedre_fin_college", "ensemble", a, v, "points (250 en 2015)"])
    for a, v in sorted(X["sixieme"]["score_francais"].items()):
        w.writerow(["depp_sixieme_francais", "score", a, v, "points (250 en 2017)"])
    for g_, s in X["sixieme"]["satisfaisant_par_domaine_2025"].items():
        for d, v in s.items():
            w.writerow(["depp_sixieme_2025_maitrise_satisfaisante", g_ + " / " + d, "2025", v, "% des eleves"])
    for voie, s in X["seconde_francais"].items():
        for a, v in sorted(s.items()):
            w.writerow(["depp_test_seconde_francais", voie, a, v, "points (250 en 2019)"])
    for a, v in sorted(X["pirls"].items()):
        w.writerow(["iea_pirls_france_cm1", "score", a, v["score"], "points PIRLS"])
    for a, v in sorted(X["pisa_lecture"]["score"].items()):
        w.writerow(["ocde_pisa_lecture_france", "score", a, round(v, 2), "points PISA (erreur type %s)" % round(X["pisa_lecture"]["et"][a], 2)])
    for k, v in X["ocde_lecture_loisir"]["heures_semaine"].items():
        w.writerow(["ocde_temps_lecture_plaisir_france", k, "", round(v, 3), "heures par semaine"])
    for k, v in X["ocde_lecture_loisir"]["joyread"].items():
        w.writerow(["ocde_indice_plaisir_de_lire_france", k, "", round(v, 4), "indice (OCDE = 0 en 2009)"])
    for k, v in X["ocde_lecture_loisir"]["lit_seulement_si_oblige"].items():
        w.writerow(["ocde_lit_seulement_si_oblige_france", k, "", round(v, 2), "% des eleves"])
    for k, s in X["culture"].items():
        if isinstance(s, dict):
            for pop, v in s.items():
                for a, x in sorted(v.items()):
                    w.writerow(["culture_pratiques_culturelles", k + " / " + pop, a, x, "% (enquetes 1973-2008)"])
    for a, v in sorted(X["smartphone_12_17"].items()):
        w.writerow(["credoc_smartphone_12_17_ans", "equipes", a, v, "%"])
    for k, v in X["pratiques_2023_ne_lit_pas_pour_plaisir"].items():
        w.writerow(["depp_2023_ne_lit_pas_pour_son_plaisir", k, "2023", round(v, 2), "% des eleves"])
    for q, lib in ((Q5, "jours_de_classe"), (Q6, "week_end")):
        r = X["t7"]["questions"][q]
        for an in ("2022", "2025"):
            a = r["a"][an]
            w.writerow(["pisa_numerique_loisir_" + lib, "non_reponse", an, round(a["non_reponse"][0], 2), "% des eleves (calcul)"])
            for t_, v in a["tranches"].items():
                w.writerow(["pisa_numerique_loisir_" + lib, t_ + " / part", an, round(v["part"][0], 2), "% des repondants (calcul)"])
                w.writerow(["pisa_numerique_loisir_" + lib, t_ + " / lecture", an, round(v["lecture"][0], 2), "points PISA (calcul)"])
    tx = X["textes_offerts"]
    w.writerow(["emmanuelle_manuels_recenses", "disciplines saisies", tx["releve_le"], len(tx["emmanuelle"]["disciplines_saisies"]),
                "disciplines (" + ", ".join(tx["emmanuelle"]["disciplines_saisies"]) + ") ; francais : saisie en cours"])
    w.writerow(["emmanuelle_manuels_recenses", "notices de la base", tx["releve_le"], tx["emmanuelle"]["notices_base"], "notices"])
    for k, v in tx["temoins_bnf"].items():
        w.writerow(["bnf_rappel_cadre_par_titre", k + " / notices au catalogue (" + v["periode"] + ")", tx["releve_le"], v["catalogue"], "notices"])
        w.writerow(["bnf_rappel_cadre_par_titre", k + " / retrouvees par titre lecture + niveau (" + v["periode"] + ")", tx["releve_le"], v["r1"], "notices"])
    for d in (0.5, 1.0):
        w.writerow(["precision_comparaison_de_periodes", "ouvrages par periode pour un ecart de %s ecart-type" % nb(d), "", effectif(d),
                    "ouvrages (bilateral 5 %, puissance 80 %)"])
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
    log("Dictee CM2 : %s -> %s erreurs (lexicales %s -> %s) ; PISA lecture 2012-2025 : -%s ; seuil smartphone %s"
        % (A["tot87"], A["tot21"], A["lex87"], A["lex21"], A["pisa_v12"], A["smart_seuil"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(A)))
        return 0
    import cairosvg
    figs = {"langue-chronologie.svg": fig_chronologie(c, A), "langue-dictee.svg": fig_dictee(c, A), "langue-plaisir.svg": fig_plaisir(c, A)}
    X = c["X"]
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "champ": "France ; élèves de CM1, CM2, sixième, troisième, seconde ; jeunes de 15 ans (PISA) ; 15-24 ans (enquêtes Pratiques culturelles)",
                        "source_calcul": "calcul de l'auteur (protocole écrit avant calcul) ; extrait figé scripts/sources_langue_eleves/ (SHA256SUMS)"},
               **{k: v for k, v in X.items() if k not in ("releve_le",)},
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
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; sources DEPP, OCDE (PISA), IEA (PIRLS), ministère de la Culture, CREDOC", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/langue_eleves.json, static/langue_eleves.csv, data/figures_langue.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
