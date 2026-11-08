#!/usr/bin/env python3
"""update_malaise_etudiant.py -- ressource « Les étudiants vont-ils plus mal que les autres jeunes ? » (bloc École, lycée
et université).

Découverte de la page (dépôt de pilotage de l'auteur, 06_PROMOTION/RECHERCHE_MALAISE_ETUDIANT_2026-10-23, six
contre-expertises arbitrées du 23 au 24/10/2026) : la dépression déclarée a augmenté plus vite chez les étudiants que dans
toute autre situation publiée de 2017 à 2021, et les soins, les hospitalisations et les suicides confirment une
dégradation réelle chez les jeunes ; mais elle touche d'abord les jeunes femmes, commence au milieu des années 2010 et se
voit avant l'université. La comparaison qui trancherait (étudiants et non-étudiants au même âge et du même sexe) n'est pas
publiée ; la page publie la simulation de ce que la seule composition par sexe produirait (environ 0,6 point).

Entrée : l'extrait FIGÉ scripts/sources_malaise_etudiant/extrait.json, écrit par outils/extrait.py du dossier de
recherche, contrôlé contre SHA256SUMS. Chaque valeur y porte sa catégorie : « lue » (calculée sur une réponse brute
archivée), « transcrite_verifiee » (la phrase qui la porte est exigée telle quelle dans le document archivé), « citee »
(étude citée, sans document archivé). Ce générateur ne recalcule que des écarts et des moyennes ; il met en forme et
GARDE : chaque qualificatif de la prose est une condition sur les nombres (fonction gardes) ; si l'extrait la dément,
arrêt.
Mise à jour : à la main, hors module (les sources sont des bulletins, une enquête et des API lues dans le dossier de
recherche). Rendez-vous de rattrapage : juin 2027 (série DREES 2026, cartographie de l'Assurance maladie 2025, décès 2025)
— relancer les extractions puis outils/extrait.py, recopier l'extrait et son empreinte, relancer ce script.
Page en français seulement (exclusion déclarée : statistique et débat français, comme les pages voisines du bloc).

Usage : python scripts/update_malaise_etudiant.py [--check] [--mutation=etudiants|calendrier|suicides|depense|composition|lyceens|adolescentes|arrondi|niveau2012|trajectoires|covid|traitements|filles|hommes2017|plat|formule|filles1019|premierehausse|plafond|soinsplat|vagues]
Sorties : data/ et static/malaise_etudiant.json, static/malaise_etudiant.csv, data/figures_etudiants.json,
static/img/etudiants-hospit.svg et -m.svg (version téléphone), avec leurs PNG
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import math
import re
import sys
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import langue_generee as lg  # nombres, signes et accord de « point » à la précision affichée
import pied_figure  # pied commun, coupure des lignes, version téléphone, parité
import releve_jeu  # releve_le ne bouge qu'avec une donnée

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_malaise_etudiant"
OUT_DATA = ROOT / "data" / "malaise_etudiant.json"
OUT_STATIC = ROOT / "static" / "malaise_etudiant.json"
OUT_CSV = ROOT / "static" / "malaise_etudiant.csv"
OUT_FIGURES = ROOT / "data" / "figures_etudiants.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_MD = ROOT / "content" / "les-etudiants-vont-ils-plus-mal" / "_index.md"
PAGE_URL = "stephane-lalut.com/les-etudiants-vont-ils-plus-mal/"
LICENCE = ("CC BY 4.0 — calcul Stéphane Lalut ; sources Santé publique France (BEH, EnCLASS), DREES, Assurance maladie, "
           "Eurostat (CépiDc-Inserm), Insee (compte de l'éducation, Depp)")
MUTATIONS = ("etudiants", "calendrier", "suicides", "depense", "composition", "lyceens", "adolescentes", "arrondi", "niveau2012",
             "trajectoires", "covid", "traitements", "filles", "hommes2017", "plat", "formule", "filles1019", "premierehausse", "plafond", "soinsplat", "vagues")


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def lire() -> dict:
    sums = dict(l.split()[::-1] for l in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines() if l.strip())
    p = SRC / "extrait.json"
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if sums.get("extrait.json", "").lstrip("*") != h and sums.get("*extrait.json") != h:
        fail("extrait.json ne correspond pas a SHA256SUMS (%s)" % h)
    X = json.loads(p.read_text(encoding="utf-8"))
    X["drees_hospit"] = drees_exact(X["drees_hospit"], sums)
    return X


# Séries de la DREES recalculées ici depuis l'archive (07/11/2026) : l'extrait les stockait arrondies au dixième, et
# l'arrondi de l'affichage arrondissait une seconde fois (234,46 stocké 234,5, affiché 235 ; 149,48 affiché 150). Taux
# gardés exacts, arrondis une seule fois à l'affichage (un stockage au centième aurait encore fait basculer 122,499 en
# 123) ; l'extrait devient le témoin du calcul.
DREES_SERIES = {"f18_24": ("F", 18, 24), "h18_24": ("M", 18, 24), "f15_17": ("F", 15, 17), "t15_17": ("FM", 15, 17),
                "f25_44": ("F", 25, 44), "f10_19": ("F", 10, 19), "f10_29": ("F", 10, 29)}


def drees_exact(ext: dict, sums: dict) -> dict:
    p = SRC / ext["fichier"]
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != ext["sha256"] or sums.get(p.name, "").lstrip("*") != h and sums.get("*" + p.name) != h:
        fail("%s ne correspond ni a l'extrait ni a SHA256SUMS (%s)" % (p.name, h))
    d = [x for x in json.loads(p.read_text(encoding="utf-8"))
         if x["champ"] == "mco" and x["unite"] == "patient" and x["age"].isdigit()]
    out = dict(ext)
    for nom, (sexes, a0, a1) in DREES_SERIES.items():
        serie = {}
        for an in ext[nom]:
            r = [x for x in d if x["annee"] == an and x["sexe"] in sexes and a0 <= int(x["age"]) <= a1]
            if len(r) != len(sexes) * (a1 - a0 + 1):
                fail("DREES %s %s : %d ages sur %d" % (nom, an, len(r), len(sexes) * (a1 - a0 + 1)))
            serie[an] = 1e5 * sum(x["nombre"] for x in r) / sum(x["population"] for x in r)   # jamais arrondi ici
            if abs(serie[an] - ext[nom][an]) > 0.051:
                fail("DREES %s %s : %.2f recalcule, %.1f dans l'extrait" % (nom, an, serie[an], ext[nom][an]))
        out[nom] = serie
    # Témoin : la publication de la DREES du 11/05/2026 (482 filles de 10-19 ans en 2025 ; 222 et 369 femmes de
    # 10-29 ans en 2012 et 2025), retrouvée à l'unité.
    if (arrondi(out["f10_19"]["2025"], 0), arrondi(out["f10_29"]["2012"], 0), arrondi(out["f10_29"]["2025"], 0)) != (482, 222, 369):
        fail("temoin DREES du 11/05/2026 non retrouve : %s %s" % (out["f10_19"], out["f10_29"]))
    return out


def moy(d: dict, ans) -> float:
    return sum(d[str(a)] for a in ans) / len(ans)


def calcul(X: dict) -> dict:
    b, h, a, s = X["beh2023"], X["drees_hospit"], X["antidepresseurs"]["par_sexe"], X["suicides"]
    c = {"X": X}
    c["etu"] = b["etudiants"]
    c["hausse"] = b["hausse_2017_2021"]
    c["f1824"], c["h1824"] = b["f18_24"], b["h18_24"]
    c["hosp"] = h
    c["antidep"] = a
    tf, tm = s["taux_20_24"]["F"], s["taux_20_24"]["M"]
    c["sf_avant"], c["sf_apres"] = moy(tf, (2018, 2019)), moy(tf, (2021, 2022, 2023))
    c["sm_avant"], c["sm_apres"] = moy(tm, (2018, 2019)), moy(tm, (2021, 2022, 2023))
    c["sf_var"] = 100 * (c["sf_apres"] / c["sf_avant"] - 1)
    c["sm_var"] = 100 * (c["sm_apres"] / c["sm_avant"] - 1)
    n = s["deces_f20_24_survenus_en_france"]
    c["n23"], c["n24"] = n["2023"], n["2024"]
    c["n_sd"] = math.sqrt(c["n23"] + c["n24"])  # écart type d'une différence de deux comptages de Poisson
    c["enc"] = X["enclass2024"]
    c["dep"] = X["depense"]
    c["comp"] = X["composition"]
    # Hospitalisations des femmes de 18-24 ans et des hommes : variation relative de 2019 à la dernière année.
    c["der"] = max(int(k) for k in h["f18_24"])
    c["f_var"] = 100 * (h["f18_24"][str(c["der"])] / h["f18_24"]["2019"] - 1)
    c["m_var"] = 100 * (h["h18_24"][str(c["der"])] / h["h18_24"]["2019"] - 1)
    return c


def mutation(c: dict) -> str:
    m = next((x.split("=", 1)[1] for x in sys.argv[1:] if x.startswith("--mutation=")), "")
    if not m:
        return ""
    if m not in MUTATIONS:
        fail("mutation inconnue %s (connues : %s)" % (m, ", ".join(MUTATIONS)))
    if m == "etudiants":        # les chômeurs dépassent les étudiants : « la plus forte hausse » devient fausse
        c["hausse"] = dict(c["hausse"], chomeurs=7.5)
    elif m == "calendrier":     # les hospitalisations des jeunes femmes remontent dès 2013 : « baissent jusqu'en 2014 » faux
        c["hosp"] = dict(c["hosp"], f18_24=dict(c["hosp"]["f18_24"], **{"2013": 240.0}))
    elif m == "suicides":       # 2024 très au-dessus de 2023 : « sans nouvelle hausse établie » faux
        c["n23"], c["n24"] = 85, 118   # dans « une centaine », mais écart de 33 > 2 écarts types (28,5)
        c["n_sd"] = math.sqrt(85 + 118)
    elif m == "depense":        # la dépense de 2024 dépasse le sommet de 2009 : « recule depuis 2009 » faux
        c["dep"] = dict(c["dep"], superieur_euros_constants_2024=dict(c["dep"]["superieur_euros_constants_2024"], **{"2024": 14600}))
    elif m == "composition":    # simulation à 1,2 point : « environ 0,6 point » faux
        c["comp"] = dict(c["comp"], simulation_pts=1.2)
    elif m == "adolescentes":   # filles de 15-17 ans en baisse de 2015 à 2016 : « montent dès le milieu des années 2010 » faux
        c["hosp"] = dict(c["hosp"], f15_17=dict(c["hosp"]["f15_17"], **{"2016": 380.0}))
    elif m in ("arrondi", "niveau2012"):
        # arrondi : 234,44 -> 359,86 font +53,498 % (imprimé 53) ; affichés 234,4 et 359,9, ils donnent +54 % au lecteur.
        # niveau2012 : 2019 au-dessus de 2012 ; « ne dépasse son niveau de 2012 qu'à partir de 2021 » faux.
        f, h = dict(c["hosp"]["f18_24"]), dict(c["hosp"]["h18_24"])
        if m == "arrondi":
            f["2019"], f[str(c["der"])] = 234.44, 359.86
        else:
            f["2019"] = 240.0
        c["hosp"] = dict(c["hosp"], f18_24=f, h18_24=h)
        c["f_var"] = 100 * (f[str(c["der"])] / f["2019"] - 1)
        c["m_var"] = 100 * (h[str(c["der"])] / h["2019"] - 1)
    elif m == "trajectoires":   # femmes de 25-44 ans en plus forte hausse que les jeunes femmes : « la plus marquée » faux
        f2544 = dict(c["hosp"]["f25_44"])
        f2544[str(c["der"])] = 2.0 * f2544["2019"]
        c["hosp"] = dict(c["hosp"], f25_44=f2544)
    elif m == "covid":          # pente après 2019 sous celle de 2017-2019 : « accélération après 2020 » faux
        f = dict(c["hosp"]["f18_24"])
        f[str(c["der"])] = f["2019"] + (c["der"] - 2019) * (f["2019"] - f["2017"]) / 2 - 1
        c["hosp"] = dict(c["hosp"], f18_24=f)
        c["f_var"] = 100 * (f[str(c["der"])] / f["2019"] - 1)
    elif m == "traitements":    # antidépresseurs des hommes en hausse comparable : « même contraste » faux
        c["antidep"] = dict(c["antidep"], hommes=dict(c["antidep"]["hommes"], **{"2024": 1.4}))
    elif m == "filles":         # lycéens en hausse plus forte que les lycéennes : « plus forte chez les filles » faux
        c["enc"] = dict(c["enc"], risque_depression_lyceens_garcons=dict(c["enc"]["risque_depression_lyceens_garcons"], **{"2018": 3.0}))
    elif m == "hommes2017":     # jeunes hommes très bas en 2017 : « remontent après 2017, mais beaucoup moins » faux
        c["hosp"] = dict(c["hosp"], h18_24=dict(c["hosp"]["h18_24"], **{"2017": 70.0}))
    elif m == "plat":           # antidépresseurs déjà en hausse de 2015 à 2017 : « la hausse commence dès 2018 » faux
        c["antidep"] = dict(c["antidep"], **{"tous sexes": dict(c["antidep"]["tous sexes"], **{"2015": 0.80})})
    elif m == "formule":        # chiffre de la simulation que la formule publiée ne redonne pas
        c["comp"] = dict(c["comp"], simulation_pts=0.70)
    elif m == "soinsplat":      # femmes déjà en hausse en 2016 : « à peu près plate de 2015 à 2017 » faux (figure soins)
        c["antidep"] = dict(c["antidep"], femmes=dict(c["antidep"]["femmes"], **{"2016": 1.32}))
    elif m == "vagues":         # lycéennes en baisse en 2022 : « augmente à chaque enquête » faux (figure lycée)
        r = c["enc"]["risque_depression_lyceennes"]
        c["enc"] = dict(c["enc"], risque_depression_lyceennes=dict(r, **{"2022": r["2018"] - 1.0}))
    elif m == "plafond":        # jeunes femmes en hausse des 2016 : « ne remonte qu'a partir de 2018 » faux
        c["hosp"] = dict(c["hosp"], f18_24=dict(c["hosp"]["f18_24"], **{"2016": 216.0}))
    elif m == "filles1019":     # filles de 10-19 ans sous les jeunes femmes de 18-24 ans en 2025 : « davantage » faux
        c["hosp"] = dict(c["hosp"], f10_19=dict(c["hosp"]["f10_19"], **{"2025": 300.0}))
    elif m == "premierehausse": # lycéens : quatre points de 2018 à 2022, « environ deux points » faux
        r = c["enc"]["risque_depression_lyceens"]
        c["enc"] = dict(c["enc"], risque_depression_lyceens=dict(r, **{"2018": r["2022"] - 4.0}))
    elif m == "lyceens":        # risque de 2024 sous 2022 : « continue de croître » faux
        c["enc"] = dict(c["enc"], risque_depression_lyceens=dict(c["enc"]["risque_depression_lyceens"], **{"2024": 15.0}))
    return m


def gardes(c: dict) -> int:
    """Chaque qualificatif de la prose, une condition. Retourne le nombre de gardes passées ; arrêt à la première fausse."""
    G = []

    def g(cond: bool, phrase: str) -> None:
        G.append(phrase)
        if not cond:
            fail("garde : « %s » n'est plus soutenue par les donnees" % phrase)

    e, hz, hf = c["etu"], c["hausse"], c["hosp"]
    # Section 1 -- le déclaré
    g(abs((e["2021"] - e["2017"]) - hz["etudiants"]) < 0.05, "etudiants : niveaux 2017 et 2021 coherents avec la hausse publiee")
    g(all(lg.depasse(hz["etudiants"], v) for k, v in hz.items() if k != "etudiants"),
      "la plus forte hausse de toutes les situations publiees")
    g(e["2010"] < e["2017"] < e["2021"], "la hausse precede le covid, qui l'accelere")
    g(e["2021"] - e["2017"] > e["2017"] - e["2010"], "accelere apres 2017")
    # Section 1 -- ce qu'on soigne
    ad = c["antidep"]
    g(ad["femmes"]["2017"] < ad["femmes"]["2021"] < ad["femmes"]["2024"], "antidepresseurs des jeunes femmes en hausse continue 2017-2021-2024")
    adf = ad["femmes"]
    plat = [adf[str(a)] for a in range(2015, 2018)]
    g((max(plat) - min(plat)) / min(plat) < 0.05 and all(adf[str(a)] > adf["2017"] for a in range(2018, 2025)),
      "figure soins : courbe des femmes a peu pres stable de 2015 a 2017 (moins de 5 %), au-dessus de 2017 chaque annee depuis 2018")
    ts = ad["tous sexes"]
    g(ts["2017"] < ts["2018"] < ts["2019"] and (max(ts[str(a)] for a in range(2015, 2018)) - min(ts[str(a)] for a in range(2015, 2018)))
      / min(ts[str(a)] for a in range(2015, 2018)) < 0.05, "la hausse commence des 2018, avant le covid (plat de 2015 a 2017)")
    # Section 1 -- ce qu'on fait (hospitalisations)
    g(c["f_var"] > 20, "hospitalisations des jeunes femmes en forte hausse depuis 2019")
    # Section 1 -- suicides
    g(c["sf_var"] > 25, "taux de suicide des femmes de 20-24 ans en nette hausse apres la rupture de 2018")
    g(abs(c["sm_var"]) < 10, "taux des hommes du meme age a peu pres stable")
    g(all(80 <= v <= 120 for v in (c["n23"], c["n24"])), "suicides de jeunes femmes de 20-24 ans : une centaine par an")
    g(abs(c["n24"] - c["n23"]) < 2 * c["n_sd"], "2024 : le niveau eleve se maintient, sans nouvelle hausse etablie")
    g(c["X"]["beh2025"]["anxiete_stable_18_75"] is True, "pas de hausse significative des etats anxieux")
    # Section 2 -- qui
    g(c["f1824"]["2021"] - c["f1824"]["2017"] > c["h1824"]["2021"] - c["h1824"]["2017"], "hausse plus forte chez les femmes de 18-24 ans")
    g(c["f_var"] > 2 * max(c["m_var"], 0.1), "celle des jeunes hommes beaucoup moins")
    f17, h17 = hf["f18_24"], hf["h18_24"]
    g(f17[str(c["der"])] / f17["2017"] - 1 > 2 * (h17[str(c["der"])] / h17["2017"] - 1),
      "jeunes hommes : remontent aussi apres 2017, mais beaucoup moins")
    # 08/11/2026 : garde « l'ecart femmes-hommes, bien plus que l'ecart etudiants-autres » retiree avec sa phrase
    # (contre-expertise de la page, P0.4 : l'ecart etudiants-autres comparait des situations d'ages differents).
    var = lambda s_: hf[s_][str(c["der"])] / hf[s_]["2019"] - 1  # noqa: E731
    g(min(var("f15_17"), var("f18_24")) > max(var("h18_24"), var("f25_44")),
      "la trajectoire la plus marquee est celle des adolescentes et des jeunes femmes (depuis 2019)")
    fh = hf["f18_24"]
    g((fh[str(c["der"])] - fh["2019"]) / (c["der"] - 2019) > (fh["2019"] - fh["2017"]) / 2,
      "covid : acceleration apres 2020 (pente 2019-der au-dessus de 2017-2019)")
    adf, adh = c["antidep"]["femmes"], c["antidep"]["hommes"]
    g(adf["2024"] / adf["2017"] - 1 > 2 * (adh["2024"] / adh["2017"] - 1), "meme contraste sur les traitements")
    f = hf["f18_24"]
    g(f["2012"] > f["2013"] > f["2014"] and min(f[str(a)] for a in range(2012, 2018)) == f["2014"],
      "les hospitalisations des femmes de 18-24 ans baissent jusqu'en 2014")
    g(all(f[str(a)] < f["2012"] for a in range(2013, 2021)) and all(f[str(a)] > f["2012"] for a in range(2021, c["der"] + 1)),
      "la hausse ne porte le taux au-dela de son niveau de 2012 qu'a partir de 2021")
    pal = [f[str(a)] for a in range(2014, 2018)]
    g((max(pal) - min(pal)) / min(pal) < 0.05, "plafonnent jusqu'en 2017 (ne remonte qu'a partir de 2018, page : calendrier des moyens)")
    g(all(f[str(a)] > f["2017"] for a in range(2018, c["der"] + 1) if a != 2020) and f[str(c["der"])] > f["2018"],
      "puis montent")
    f1517 = hf["f15_17"]
    g(f1517["2015"] < f1517["2016"] < f1517["2017"] < f1517["2018"] and f1517["2018"] > f1517["2014"],
      "filles de 15-17 ans : montent elles aussi des le milieu des annees 2010")
    g(f1517["2020"] < f1517["2019"] and lg.depasse(f1517["2021"], 1.2 * f1517["2019"], 0),
      "filles de 15-17 ans : bondissent en 2021, apres le creux de 2020")
    h1824 = hf["h18_24"]
    g(f["2020"] < f["2019"] and h1824["2020"] < h1824["2019"], "figure : 2020, moins d'hospitalisations (note du pied)")
    g(all(h1824[str(a)] > h1824["2017"] for a in range(2018, c["der"] + 1) if a != 2020),
      "jeunes hommes : remontent aussi apres 2017")
    f2544 = hf["f25_44"]
    creux = lg.extremum(sorted(f2544.items()), lambda kv: kv[1], dec=0, maxi=False, quoi="creux des femmes de 25-44 ans")[0]
    g(creux == "2022" and all(f2544[str(a)] > f2544["2022"] for a in range(2023, c["der"] + 1)),
      "femmes de 25-44 ans : baisse jusqu'en 2022, remontee seulement ensuite")
    t1517 = hf["t15_17"]
    g(t1517[str(c["der"])] > t1517["2019"], "15-17 ans : hausse depuis 2019")
    # Section 3 -- avant l'université
    en = c["enc"]
    r = en["risque_depression_lyceens"]
    g(r["2018"] < r["2022"] < r["2024"], "le risque de depression des lyceens continue de croitre")
    g(1.5 <= r["2022"] - r["2018"] < 2.5, "lyceens : premiere hausse d'environ deux points entre 2018 et 2022")
    g(hf["f10_19"]["2025"] > hf["f18_24"]["2025"],
      "filles de 10-19 ans en 2025 : davantage que les jeunes femmes de 18-24 ans la meme annee")
    g(lg.depasse(en["risque_depression_lyceennes"]["2024"], 2 * en["risque_depression_lyceens_garcons"]["2024"]),
      "lyceennes : plus du double des lyceens")
    lf, lgc = en["risque_depression_lyceennes"], en["risque_depression_lyceens_garcons"]
    g(lf["2024"] - lf["2018"] > lgc["2024"] - lgc["2018"], "smartphone : degradation plus forte chez les filles")
    g(lf["2018"] < lf["2022"] < lf["2024"], "figure lycee : chez les filles, la part augmente a chaque enquete depuis 2018")
    g(min(en["bien_etre_hausse_2022_2024_pts"].values()) > 0, "le bien-etre declare remonte par rapport a 2022")
    # Section 4 -- moyens
    d = c["dep"]["superieur_euros_constants_2024"]
    sommet = max((v, k) for k, v in d.items() if int(k) >= 1980)[1]
    g(sommet == "2009", "la depense par etudiant culmine en 2009")
    p = c["dep"]["par_etudiant_2024"]
    g(p["universite"] < p["ensemble"] < p["cpge"], "universite sous la moyenne, classes preparatoires au-dessus")
    # Section 5 -- composition
    cp = c["comp"]
    g(cp["par_annee"]["2021"]["ecart_pts"] > cp["par_annee"]["2017"]["ecart_pts"] > 0,
      "part des femmes plus elevee chez les etudiants, ecart qui s'elargit")
    g(0.5 <= cp["simulation_pts"] < 0.75, "environ 0,6 point")
    g(cp["sensibilite_pts"]["min"] <= cp["simulation_pts"] <= cp["sensibilite_pts"]["max"], "simulation dans sa plage de sensibilite")
    pa = cp["par_annee"]
    D = {a: pa[a]["ecart_pts"] / 100 * (c["f1824"][a] - c["h1824"][a]) for a in ("2017", "2021")}
    g(all(abs(D[a] - pa[a]["D_pts"]) < 0.01 for a in D) and abs(D["2021"] - D["2017"] - cp["simulation_pts"]) < 0.01,
      "formule de la simulation (methode) : D2021 - D2017 redonne le chiffre publie")
    return len(G)


def arrondi(v: float, dec: int) -> float:
    """Arrondi commercial (0,5 vers le haut) avant lg.nombre, qui arrondit au pair (2,5 -> 2). Valable sur une valeur
    exacte ou publiée, jamais sur une valeur déjà arrondie (double arrondi : voir drees_exact). Même geste que
    update_dette_inflation.py. Condition de mort : langue_generee.nombre arrondit lui-même 0,5 vers le haut."""
    return float(Decimal(repr(v)).quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP))


def affichage(c: dict) -> dict:
    n = lambda v, dec=1: lg.nombre(arrondi(v, dec), dec)  # noqa: E731
    e, hz, hf, ad, en, cp = c["etu"], c["hausse"], c["hosp"], c["antidep"], c["enc"], c["comp"]
    der = str(c["der"])
    d = c["dep"]["superieur_euros_constants_2024"]
    p = c["dep"]["par_etudiant_2024"]
    A = {
        "etu_2010": n(e["2010"]), "etu_2017": n(e["2017"]), "etu_2021": n(e["2021"]),
        "h_etu": lg.points(hz["etudiants"], signe_=True), "h_chom": lg.points(hz["chomeurs"], signe_=True),
        "h_actifs": lg.points(hz["actifs_occupes"], signe_=True),
        "f1824_2017": n(c["f1824"]["2017"]), "f1824_2021": n(c["f1824"]["2021"]),
        "h1824_2017": n(c["h1824"]["2017"]), "h1824_2021": n(c["h1824"]["2021"]),
        "f1824_hausse": lg.points(c["f1824"]["2021"] - c["f1824"]["2017"], signe_=True),
        "h1824_hausse": lg.points(c["h1824"]["2021"] - c["h1824"]["2017"], signe_=True),
        "ad_f_2017": n(ad["femmes"]["2017"], 2), "ad_f_2021": n(ad["femmes"]["2021"], 2), "ad_f_2024": n(ad["femmes"]["2024"], 2),
        "ad_h_2017": n(ad["hommes"]["2017"], 2), "ad_h_2024": n(ad["hommes"]["2024"], 2),
        "ad_f_2015": n(ad["femmes"]["2015"], 2), "ad_h_2015": n(ad["hommes"]["2015"], 2),
        "ad_h_2021": n(ad["hommes"]["2021"], 2),
        "hosp_der": der,
        # Taux des 18-24 ans au dixième : à l'unité, 360 / 234 donnait +54 % au lecteur pour +53,4 % (garde ci-dessous).
        "hosp_f_2012": n(hf["f18_24"]["2012"]), "hosp_f_2017": n(hf["f18_24"]["2017"]),
        "hosp_h_2012": n(hf["h18_24"]["2012"]), "hosp_h_2017": n(hf["h18_24"]["2017"]),
        "hosp_f_2014": n(hf["f18_24"]["2014"]), "hosp_f_2019": n(hf["f18_24"]["2019"]), "hosp_f_der": n(hf["f18_24"][der]),
        "hosp_h_2019": n(hf["h18_24"]["2019"]), "hosp_h_der": n(hf["h18_24"][der]),
        "hosp_f_var": n(c["f_var"], 0), "hosp_h_var": n(c["m_var"], 0),
        "hosp_t1517_2019": n(hf["t15_17"]["2019"], 0), "hosp_t1517_der": n(hf["t15_17"][der], 0),
        "hosp_f1019_2025": n(hf["f10_19"]["2025"], 0),
        "sf_avant": n(c["sf_avant"], 2), "sf_apres": n(c["sf_apres"], 2), "sf_var": n(c["sf_var"], 0), "sm_var": lg.signe(arrondi(c["sm_var"], 0), 0),
        "s_n23": n(c["n23"], 0), "s_n24": n(c["n24"], 0),
        "anx_etu_2021": n(c["X"]["beh2025"]["anxiete_etudiants_2021"]),
        "lyc_2022": n(en["risque_depression_lyceens"]["2022"]),
        "lyc_2024": n(en["risque_depression_lyceens"]["2024"]),
        "lyc_f_2018": n(en["risque_depression_lyceennes"]["2018"]), "lyc_f_2024": n(en["risque_depression_lyceennes"]["2024"]),
        "lyc_g_2024": n(en["risque_depression_lyceens_garcons"]["2024"]),
        "lyc_f_2022": n(en["risque_depression_lyceennes"]["2022"]),
        "lyc_g_2018": n(en["risque_depression_lyceens_garcons"]["2018"]),
        "lyc_g_2022": n(en["risque_depression_lyceens_garcons"]["2022"]),
        "be_college": lg.points(en["bien_etre_hausse_2022_2024_pts"]["college"], 0, signe_=True),
        "be_lycee": lg.points(en["bien_etre_hausse_2022_2024_pts"]["lycee"], 0, signe_=True),
        "dep_2009": n(d["2009"], 0), "dep_2024": n(d["2024"], 0),
        "dep_univ": n(p["universite"], 0), "dep_cpge": n(p["cpge"], 0), "dep_sts": n(p["sts"], 0), "dep_ens": n(p["ensemble"], 0),
        "comp_ecart_2017": lg.points(cp["par_annee"]["2017"]["ecart_pts"]),
        "comp_ecart_2021": lg.points(cp["par_annee"]["2021"]["ecart_pts"]),
        "comp_sim": lg.points(cp["simulation_pts"]),
        "comp_min": n(cp["sensibilite_pts"]["min"], 2), "comp_max": n(cp["sensibilite_pts"]["max"], 2),
        "confins_or": n(c["X"]["confins"]["rapport_de_cotes_etudiants"], 2),
    }
    # Le lecteur refait la variation à partir des deux taux affichés : il doit retrouver celle qui est imprimée.
    for s_, cle in (("f18_24", "hosp_f"), ("h18_24", "hosp_h")):
        lu = 100 * (arrondi(hf[s_][der], 1) / arrondi(hf[s_]["2019"], 1) - 1)
        if n(lu, 0) != A[cle + "_var"]:
            fail("%s : %s / %s donne %s %%, la page imprime %s %%" % (s_, A[cle + "_der"], A[cle + "_2019"], n(lu, 0), A[cle + "_var"]))
    return A



# ------------------------------------------------------------------ figures
# Charte de l'auteur (mémoire feedback_langage_graphique_figures) : orange = la série que la page interroge (les jeunes
# femmes), bleu = son témoin (les jeunes hommes du même âge) ; grille horizontale seule ; étiquetage direct ; valeur
# terminale en ancrage. Contrôle : skill controle-figures, verrou scripts/check-figures.py.
W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE = "#184f95", "#eb6834"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
FS_MIN = pied_figure.POLICE_M
LIC_FIG = "Calcul Stéphane Lalut, licence CC BY 4.0 · stephane-lalut.com/les-etudiants-vont-ils-plus-mal/"
LIC_FIG_M = "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"
FIG = {
    "hospit": dict(
        titre="Jeunes hospitalisés pour un geste auto-infligé, 2012-{der}",
        sous_titre="Patients hospitalisés dans l'année, pour 100 000 habitants de 18 à 24 ans du même sexe",
        source="DREES, patients hospitalisés pour geste auto-infligé depuis 2012 (PMSI, médecine, chirurgie, obstétrique) ; "
               "taux recalculés à partir des effectifs par âge détaillé",
        note="Geste auto-infligé : tentative de suicide ou automutilation. Ces séries ne distinguent pas les étudiants des "
             "autres jeunes. 2020 : moins de patients hospitalisés pendant l'épidémie de covid.",
        montre="De 2019 à {der}, le taux de jeunes femmes de 18 à 24 ans hospitalisées pour un geste auto-infligé a augmenté "
               "de {hosp_f_var} %, celui des jeunes hommes du même âge de {hosp_h_var} %. La courbe des femmes, à peu près "
               "plate de 2014 à 2017, monte dès 2018, avant l'épidémie de covid, et ne dépasse son niveau de 2012 qu'à partir "
               "de 2021."),
    "soins": dict(
        titre="Jeunes traités par antidépresseurs ou régulateurs de l'humeur, 2015-2024",
        sous_titre="Part des 20-24 ans du même sexe traités, hors pathologie psychiatrique repérée, en %",
        source="Assurance maladie, cartographie des pathologies et des dépenses : traitements antidépresseurs et "
               "régulateurs de l'humeur « hors pathologies »",
        note="C'est-à-dire sans diagnostic psychiatrique repéré par une hospitalisation ou une "
             "affection de longue durée récente. Ces séries ne distinguent pas les étudiants des autres jeunes.",
        montre="De 2017 à 2024, la part des femmes de 20 à 24 ans traitées par antidépresseurs ou régulateurs de "
               "l'humeur est passée de {ad_f_2017} % à {ad_f_2024} %, celle des hommes du même âge de {ad_h_2017} % à "
               "{ad_h_2024} %. La courbe des femmes, à peu près stable de 2015 à 2017, est en hausse chaque année depuis "
               "2018, avant l'épidémie de covid."),
    "lycee": dict(
        titre="Lycéens présentant un risque important de dépression, 2018-2024",
        sous_titre="Part des lycéens de chaque sexe, en %",
        source="Santé publique France, enquête EnCLASS 2024 (Le point sur, 2 juin 2026), lycéens",
        note="Risque important : au moins 7 symptômes sur les 10 de l'ADRS, échelle de repérage de la dépression "
             "de l'adolescent. Trois enquêtes (2018, 2022, 2024), reliées en tirets, auprès d'élèves différents "
             "à chaque fois.",
        montre="En 2024, {lyc_f_2024} % des lycéennes présentent un risque important de dépression, plus du double "
               "des lycéens ({lyc_g_2024} %) ; chez les filles, la part augmente à chaque enquête depuis 2018 "
               "({lyc_f_2018} %)."),
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def valeur(x: float, y: float, taille, col: str, txt: str, ancre: str = "middle", gras: bool = False) -> str:
    """Étiquette de valeur posée sur un liseré blanc (copie aria-hidden dessous) : une ligne de grille qui passe sous
    les chiffres ne les coupe pas (« 130 » sur la grille de 100, « 360 » sous celle de 400 : contrôleur, 07/11/2026)."""
    att = 'x="%.1f" y="%.1f" font-size="%s"%s text-anchor="%s"' % (x, y, taille, ' font-weight="600"' if gras else "", ancre)
    return ('<text aria-hidden="true" %s fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">%s</text>'
            '<text %s fill="%s">%s</text>' % (att, esc(txt), att, col, esc(txt)))


def textes_fig(A: dict) -> dict:
    return {k: v.format(der=A["hosp_der"], **A) for k, v in FIG["hospit"].items()}


def desc_hospit(A: dict) -> str:
    return ("Deux courbes, de 2012 à %s, du nombre de patients hospitalisés pour un geste auto-infligé pour 100 000 habitants. "
            "Femmes de 18 à 24 ans : %s en 2012, %s en 2014, %s en 2017, %s en 2019, %s en %s, soit +%s %% depuis 2019. "
            "Hommes de 18 à 24 ans : %s en 2012, %s en 2017, %s en 2019, %s en %s, soit +%s %% depuis 2019."
            % (A["hosp_der"], A["hosp_f_2012"], A["hosp_f_2014"], A["hosp_f_2017"], A["hosp_f_2019"], A["hosp_f_der"],
               A["hosp_der"], A["hosp_f_var"], A["hosp_h_2012"], A["hosp_h_2017"], A["hosp_h_2019"], A["hosp_h_der"],
               A["hosp_der"], A["hosp_h_var"]))


def fig_hospit(c: dict, A: dict) -> str:
    t = textes_fig(A)
    f, h = c["hosp"]["f18_24"], c["hosp"]["h18_24"]
    ans = sorted(int(a) for a in f)
    a0, a1 = ans[0], ans[-1]
    X0, X1, TOP, BAS, VMAX = 44, 540, 64, 280, 400
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * v / VMAX
    if max(max(f.values()), max(h.values())) > VMAX * 0.95:
        fail("figure : une valeur depasse l'echelle (%d)" % VMAX)
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="etu-h-t etu-h-d" font-family="%s">' % (W, esc(FONT)),
         '<title id="etu-h-t">%s</title><desc id="etu-h-d">%s</desc>' % (esc(t["titre"]), esc(desc_hospit(A))),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W,
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"])),
         '<text x="0" y="37" font-size="11" fill="%s">%s</text>' % (INK2, esc(t["sous_titre"]))]
    for gv in range(0, VMAX + 1, 100):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>'
                 % (X0, Y(gv), X1, Y(gv), GRID, 1 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d</text>' % (X0 - 6, Y(gv) + 3.5, MUTED, gv))
    for a in ans:
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 15, MUTED, a))
    for serie, col in ((h, BLEU), (f, ORANGE)):
        d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(serie[str(a)])) for k, a in enumerate(ans))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>' % (d, col))
        for a in ans:
            e.append('<circle cx="%.1f" cy="%.1f" r="2.8" fill="%s"/>' % (X(a), Y(serie[str(a)]), col))
    # 2019, année de référence des variations : valeur au-dessus du point, pour les deux séries comme sur téléphone (sous
    # le point, celle des hommes tombait sur la grille de 100 ; au-dessus, plus de 50 px la séparent des femmes).
    e.append(valeur(X(2019), Y(f["2019"]) - 9, 11, ORANGE, A["hosp_f_2019"]))
    e.append(valeur(X(2019), Y(h["2019"]) - 9, 11, BLEU, A["hosp_h_2019"]))
    # Valeur terminale en ancrage, à droite du dernier point : valeur, nom de la série, variation depuis 2019.
    for serie, col, nom, cle, var in ((f, ORANGE, "femmes de 18 à 24 ans", "hosp_f_der", A["hosp_f_var"]),
                                      (h, BLEU, "hommes de 18 à 24 ans", "hosp_h_der", A["hosp_h_var"])):
        y = Y(serie[str(a1)])
        e.append('<text x="%d" y="%.1f" font-size="16" font-weight="600" fill="%s">%s</text>' % (X1 + 12, y + 5, col, A[cle]))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s">%s</text>' % (X1 + 12, y + 21, col, nom))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s">+%s %% depuis 2019</text>' % (X1 + 12, y + 35, INK2, var))
    return pied_figure.pied(e, BAS + 30, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                             (LIC_FIG, MUTED, "pied-licence")], GRID)


def fig_hospit_m(c: dict, A: dict, svg_d: str) -> str:
    t = textes_fig(A)
    f, h = c["hosp"]["f18_24"], c["hosp"]["h18_24"]
    ans = sorted(int(a) for a in f)
    a0, a1 = ans[0], ans[-1]
    e, y = pied_figure.tete_mobile("etu-hm", t["titre"], html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d).group(1)),
                                   INK, FONT)
    for k, l in enumerate(pied_figure.coupe("Patients hospitalisés dans l'année, pour 100 000 habitants de 18 à 24 ans "
                                            "du même sexe", 38)):
        y += 18 if k else 0  # tete_mobile rend déjà la ligne de base suivante
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    X0, X1, VMAX = 34, 292, 400
    TOP = y + 30
    BAS = TOP + 200
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * v / VMAX
    for gv in range(0, VMAX + 1, 100):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>'
                 % (X0, Y(gv), X1, Y(gv), GRID, 1 if gv == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(gv) + 4.5, FS_MIN, MUTED, gv))
    for a in (a0, 2019, a1):  # 2019 : année de référence des variations, repérable sur l'axe
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                 % (X(a), BAS + 18, FS_MIN, MUTED, "start" if a == a0 else "end" if a == a1 else "middle", a))
    for serie, col in ((h, BLEU), (f, ORANGE)):
        d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(serie[str(a)])) for k, a in enumerate(ans))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>' % (d, col))
        for a in (2019, a1):
            e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s"/>' % (X(a), Y(serie[str(a)]), col))
    # Valeurs de 2019 et de la dernière année au-dessus de leur point : sous le point, celle des hommes se posait sur la
    # grille de 100 ; au-dessus, elle reste à plus de 40 px de la courbe des femmes.
    for serie, col, cle in ((f, ORANGE, "hosp_f_2019"), (h, BLEU, "hosp_h_2019")):
        e.append(valeur(X(2019), Y(serie["2019"]) - 9, FS_MIN, col, A[cle]))
    e.append(valeur(X(a1), Y(f[str(a1)]) - 10, 16, ORANGE, A["hosp_f_der"], "end", True))
    e.append(valeur(X(a1), Y(h[str(a1)]) - 10, 16, BLEU, A["hosp_h_der"], "end", True))
    y = BAS + 30
    for col, nom, v19, vder, var in ((ORANGE, "Femmes de 18 à 24 ans", A["hosp_f_2019"], A["hosp_f_der"], A["hosp_f_var"]),
                                     (BLEU, "Hommes de 18 à 24 ans", A["hosp_h_2019"], A["hosp_h_der"], A["hosp_h_var"])):
        y += 26
        e.append('<rect x="0" y="%d" width="14" height="4" fill="%s"/>' % (y - 6, col))
        e.append('<text x="22" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, nom))
        y += 21
        e.append('<text x="22" y="%d" font-size="%s" fill="%s">2019 : %s · %s : %s (+%s %%)</text>'
                 % (y, FS_MIN, col, v19, a1, vder, var))
    return pied_figure.pied_mobile(e, y + 16, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LIC_FIG_M, MUTED, "pied-licence")], GRID)


def textes(cle: str, A: dict) -> dict:
    return {k: v.format(der=A["hosp_der"], **A) for k, v in FIG[cle].items()}


def desc_soins(A: dict) -> str:
    return ("Deux courbes, de 2015 à 2024, de la part des 20-24 ans traités par antidépresseurs ou régulateurs de l'humeur, "
            "hors pathologie psychiatrique repérée, en %%. Femmes : %s en 2015, %s en 2017, %s en 2021, %s en 2024. "
            "Hommes : %s en 2015, %s en 2017, %s en 2021, %s en 2024."
            % (A["ad_f_2015"], A["ad_f_2017"], A["ad_f_2021"], A["ad_f_2024"],
               A["ad_h_2015"], A["ad_h_2017"], A["ad_h_2021"], A["ad_h_2024"]))


def desc_lycee(A: dict) -> str:
    return ("Deux séries, enquêtes de 2018, 2022 et 2024, de la part des lycéens présentant un risque important de "
            "dépression, en %%. Lycéennes : %s en 2018, %s en 2022, %s en 2024. Lycéens (garçons) : %s en 2018, %s en "
            "2022, %s en 2024."
            % (A["lyc_f_2018"], A["lyc_f_2022"], A["lyc_f_2024"], A["lyc_g_2018"], A["lyc_g_2022"], A["lyc_g_2024"]))


def courbes(ident: str, t: dict, desc: str, series, vmax: float, pas: float, etiquettes, terminaux,
            tirets: bool = False) -> str:
    """Figure détaillée (720) à deux courbes, sur le modèle de fig_hospit. series : [(valeurs par année, couleur)] ;
    etiquettes : [(année, valeur, couleur, texte)] posées au-dessus du point ; terminaux : [(valeur, couleur, gros, nom)]
    à droite du dernier point."""
    ans = sorted({int(a) for s, _ in series for a in s})
    a0, a1 = ans[0], ans[-1]
    X0, X1, TOP, BAS = 44, 540, 64, 280
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * v / vmax
    if max(max(s.values()) for s, _ in series) > vmax * 0.95:
        fail("figure %s : une valeur depasse l'echelle (%s)" % (ident, vmax))
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, ident, ident, esc(FONT)),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(t["titre"]), ident, esc(desc)),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W,
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"])),
         '<text x="0" y="37" font-size="11" fill="%s">%s</text>' % (INK2, esc(t["sous_titre"]))]
    n = int(round(vmax / pas))
    for k in range(n + 1):
        gv = k * pas
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>'
                 % (X0, Y(gv), X1, Y(gv), GRID, 1 if k == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>'
                 % (X0 - 6, Y(gv) + 3.5, MUTED, lg.nombre(gv, 0)))
    for a in ans:
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 15, MUTED, a))
    trait = ' stroke-dasharray="6 4"' if tirets else ""
    for serie, col in series:
        pts = sorted(int(a) for a in serie)
        d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(serie[str(a)])) for k, a in enumerate(pts))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"%s/>' % (d, col, trait))
        for a in pts:
            e.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (X(a), Y(serie[str(a)]), 3.6 if tirets else 2.8, col))
    for a, v, col, txt, *pos in etiquettes:
        # « dessous » : valeur sous le point (première année, au bord de l'axe : au-dessus, elle mordait sur les
        # graduations « 10 » et « 20 », check-figures du 08/11/2026).
        e.append(valeur(X(a), Y(v) + 18 if pos and pos[0] == "dessous" else Y(v) - 9, 11, col, txt))
    for v, col, gros, nom in terminaux:
        y = Y(v)
        if gros:
            e.append('<text x="%d" y="%.1f" font-size="16" font-weight="600" fill="%s">%s</text>' % (X1 + 12, y + 5, col, esc(gros)))
            e.append('<text x="%d" y="%.1f" font-size="11" fill="%s">%s</text>' % (X1 + 12, y + 21, col, esc(nom)))
        else:
            e.append('<text x="%d" y="%.1f" font-size="12" font-weight="600" fill="%s">%s</text>' % (X1 + 12, y + 4, col, esc(nom)))
    return pied_figure.pied(e, BAS + 30, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                             (LIC_FIG, MUTED, "pied-licence")], GRID)


def courbes_m(ident: str, t: dict, svg_d: str, series, vmax: float, pas: float, ans_axe, etiquettes, legende,
              tirets: bool = False) -> str:
    """Version téléphone (300) de courbes(). etiquettes : [(année, valeur, couleur, texte, taille, gras, ancre)] ;
    legende : [(couleur, nom, ligne de valeurs)]."""
    ans = sorted({int(a) for s, _ in series for a in s})
    a0, a1 = ans[0], ans[-1]
    e, y = pied_figure.tete_mobile(ident, t["titre"], html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d).group(1)),
                                   INK, FONT)
    for k, l in enumerate(pied_figure.coupe(t["sous_titre"], 38)):
        y += 18 if k else 0
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    X0, X1 = 34, 292
    TOP = y + 30
    BAS = TOP + 200
    X = lambda a: X0 + (X1 - X0) * (a - a0) / (a1 - a0)
    Y = lambda v: BAS - (BAS - TOP) * v / vmax
    n = int(round(vmax / pas))
    for k in range(n + 1):
        gv = k * pas
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>'
                 % (X0, Y(gv), X1, Y(gv), GRID, 1 if k == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%s</text>'
                 % (X0 - 4, Y(gv) + 4.5, FS_MIN, MUTED, lg.nombre(gv, 0)))
    for a in ans_axe:
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                 % (X(a), BAS + 18, FS_MIN, MUTED, "start" if a == a0 else "end" if a == a1 else "middle", a))
    trait = ' stroke-dasharray="6 4"' if tirets else ""
    for serie, col in series:
        pts = sorted(int(a) for a in serie)
        d = " ".join(("M" if k == 0 else "L") + "%.1f,%.1f" % (X(a), Y(serie[str(a)])) for k, a in enumerate(pts))
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"%s/>' % (d, col, trait))
    for a, v, col, txt, taille, gras, ancre, *pos in etiquettes:
        e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s"/>' % (X(a), Y(v), col))
        # « dessous » : au-dessus du premier point, la valeur se collait à la graduation (« 20 18,0 » lu « 2018,0 »,
        # rendu regardé le 08/11/2026 ; check-figures ne le voyait pas, les deux textes ne se chevauchant pas).
        e.append(valeur(X(a), Y(v) + 22 if pos and pos[0] == "dessous" else Y(v) - 10, taille, col, txt, ancre, gras))
    y = BAS + 30
    for col, nom, ligne in legende:
        y += 26
        e.append('<rect x="0" y="%d" width="14" height="4" fill="%s"/>' % (y - 6, col))
        e.append('<text x="22" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(nom)))
        y += 21
        e.append('<text x="22" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, col, esc(ligne)))
    return pied_figure.pied_mobile(e, y + 16, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LIC_FIG_M, MUTED, "pied-licence")], GRID)


def fig_soins(c: dict, A: dict) -> tuple:
    t = textes("soins", A)
    f = {a: v for a, v in c["antidep"]["femmes"].items()}
    h = {a: v for a, v in c["antidep"]["hommes"].items()}
    series = [(h, BLEU), (f, ORANGE)]
    d = courbes("etu-s", t, desc_soins(A), series, 3.0, 1.0,
                [(2017, f["2017"], ORANGE, A["ad_f_2017"]), (2017, h["2017"], BLEU, A["ad_h_2017"])],
                [(f["2024"], ORANGE, A["ad_f_2024"], "femmes de 20 à 24 ans"),
                 (h["2024"], BLEU, A["ad_h_2024"], "hommes de 20 à 24 ans")])
    m = courbes_m("etu-sm", t, d, series, 3.0, 1.0, (2015, 2017, 2024),
                  [(2017, f["2017"], ORANGE, A["ad_f_2017"], FS_MIN, False, "middle"),
                   (2017, h["2017"], BLEU, A["ad_h_2017"], FS_MIN, False, "middle"),
                   (2024, f["2024"], ORANGE, A["ad_f_2024"], 16, True, "end"),
                   (2024, h["2024"], BLEU, A["ad_h_2024"], 16, True, "end")],
                  [(ORANGE, "Femmes de 20 à 24 ans", "2017 : %s · 2024 : %s" % (A["ad_f_2017"], A["ad_f_2024"])),
                   (BLEU, "Hommes de 20 à 24 ans", "2017 : %s · 2024 : %s" % (A["ad_h_2017"], A["ad_h_2024"]))])
    return d, m


def fig_lycee(c: dict, A: dict) -> tuple:
    t = textes("lycee", A)
    en = c["enc"]
    f, g_ = en["risque_depression_lyceennes"], en["risque_depression_lyceens_garcons"]
    series = [(g_, BLEU), (f, ORANGE)]
    cles = (("2018", "lyc_f_2018", "lyc_g_2018"), ("2022", "lyc_f_2022", "lyc_g_2022"), ("2024", "lyc_f_2024", "lyc_g_2024"))
    etq = []
    for a, kf, kg in cles:
        etq += [(int(a), f[a], ORANGE, A[kf]), (int(a), g_[a], BLEU, A[kg])]
    etq_d = [(a, v, col, txt, "dessous") if a == 2018 else (a, v, col, txt) for a, v, col, txt in etq]
    d = courbes("etu-l", t, desc_lycee(A), series, 30.0, 10.0, etq_d,
                [(f["2024"], ORANGE, None, "lycéennes"), (g_["2024"], BLEU, None, "lycéens (garçons)")], tirets=True)
    etq_m = [(a, v, col, txt, FS_MIN, False, "start", "dessous") if a == 2018
             else (a, v, col, txt, FS_MIN, False, "end" if a == 2024 else "middle") for a, v, col, txt in etq]
    m = courbes_m("etu-lm", t, d, series, 30.0, 10.0, (2018, 2022, 2024), etq_m,
                  [(ORANGE, "Lycéennes", "2018 : %s · 2022 : %s · 2024 : %s" % (A["lyc_f_2018"], A["lyc_f_2022"], A["lyc_f_2024"])),
                   (BLEU, "Lycéens (garçons)", "2018 : %s · 2022 : %s · 2024 : %s" % (A["lyc_g_2018"], A["lyc_g_2022"], A["lyc_g_2024"]))],
                  tirets=True)
    return d, m



def figures(c: dict, A: dict) -> dict:
    d = fig_hospit(c, A)
    figs = {"etudiants-hospit.svg": d, "etudiants-hospit-m.svg": fig_hospit_m(c, A, d)}
    figs["etudiants-soins.svg"], figs["etudiants-soins-m.svg"] = fig_soins(c, A)
    figs["etudiants-lycee.svg"], figs["etudiants-lycee-m.svg"] = fig_lycee(c, A)
    for nom in ("hospit", "soins", "lycee"):
        ecarts = pied_figure.parite(figs["etudiants-%s.svg" % nom], figs["etudiants-%s-m.svg" % nom], FS_MIN, (BLEU, ORANGE))
        if ecarts:
            fail("parite mobile (%s) : " % nom + " ; ".join(ecarts))
    return figs


def fiches(figs: dict, A: dict) -> dict:
    out = []
    for nom in ("hospit", "soins", "lycee"):
        svg = figs["etudiants-%s.svg" % nom]
        out.append(dict(id=nom, fichier="etudiants-%s" % nom,
                        titre=html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1)),
                        montre=textes(nom, A)["montre"],
                        source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note")))
    return {"fr": out}


def csv_texte(c: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "serie", "annee", "valeur", "unite", "categorie", "source"])
    X = c["X"]
    b = X["beh2023"]
    for k, v in sorted(b["etudiants"].items()):
        w.writerow(["episode_depressif_declare", "etudiants_18_75", k, v, "%", b["categorie"], b["source"]])
    for nom in ("f18_24", "h18_24"):
        for k, v in sorted(b[nom].items()):
            w.writerow(["episode_depressif_declare", nom, k, v, "%", b["categorie"], b["source"]])
    for k, v in b["hausse_2017_2021"].items():
        w.writerow(["episode_depressif_hausse_2017_2021", k, "2017-2021", v, "points", b["categorie"], b["source"]])
    h = X["drees_hospit"]
    for nom in ("f18_24", "h18_24", "f15_17", "t15_17", "f25_44", "f10_19", "f10_29"):
        for k, v in sorted(h[nom].items()):
            w.writerow(["hospitalises_geste_auto_inflige", nom, k, v, "patients pour 100 000", h["categorie"], h["source"]])
    a = X["antidepresseurs"]
    for sexe, s in a["par_sexe"].items():
        for k, v in sorted(s.items()):
            w.writerow(["antidepresseurs_20_24", sexe, k, v, "%", a["categorie"], a["source"]])
    s = X["suicides"]
    for sexe, d in s["taux_20_24"].items():
        for k, v in sorted(d.items()):
            w.writerow(["suicides_taux_20_24_residents", sexe, k, v, "pour 100 000", s["categorie"], s["source"]])
    for k, v in sorted(s["deces_f20_24_survenus_en_france"].items()):
        w.writerow(["suicides_deces_femmes_20_24_survenus_en_france", "F", k, v, "deces", s["categorie"], s["source"]])
    e = X["enclass2024"]
    for nom in ("risque_depression_lyceens", "risque_depression_lyceennes", "risque_depression_lyceens_garcons"):
        for k, v in sorted(e[nom].items()):
            w.writerow(["lyceens_risque_important_de_depression", nom, k, v, "%", e["categorie"], e["source"]])
    dp = X["depense"]
    for k, v in sorted(dp["superieur_euros_constants_2024"].items()):
        w.writerow(["depense_par_etudiant_superieur", "euros_constants_2024", k, v, "euros", dp["categorie"], dp["source"]])
    for k, v in dp["par_etudiant_2024"].items():
        w.writerow(["depense_par_etudiant_2024_par_filiere", k, "2024", v, "euros", dp["categorie"], dp["source"]])
    cp = X["composition"]
    for an, r in sorted(cp["par_annee"].items()):
        for k in ("part_f_etudiants", "part_f_non_etudiants", "ecart_pts"):
            w.writerow(["composition_18_24", k, an, r[k], "%" if k != "ecart_pts" else "points", cp["categorie"], cp["source"]])
    w.writerow(["composition_18_24", "simulation_ecart_de_hausse", "2017-2021", cp["simulation_pts"], "points", cp["categorie"],
                "simulation sous hypothese nulle : meme prevalence a sexe et annee egaux chez etudiants et non-etudiants"])
    return buf.getvalue()


def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    X = lire()
    c = calcul(X)
    m = mutation(c)
    if m:
        try:
            gardes(c)
            affichage(c)   # la garde de lecture des variations vit dans l'affichage
        except SystemExit:
            log("mutation %s : une garde a mordu (attendu)." % m)
            return 0
        fail("mutation %s : aucune garde n'a mordu" % m)
    n = gardes(c)
    A = affichage(c)
    log("Etudiants %s -> %s %% (%s) ; hospit F18-24 2019->%s : %s -> %s ; composition %s"
        % (A["etu_2017"], A["etu_2021"], A["h_etu"], A["hosp_der"], A["hosp_f_2019"], A["hosp_f_der"], A["comp_sim"]))
    figs = figures(c, A)   # parité téléphone contrôlée dans figures(), aussi sous --check
    log("Figures : " + ", ".join("%s %sx%s" % ((f,) + re.search(r'viewBox="0 0 (\d+) (\d+)"', s).groups())
                                 for f, s in figs.items()))
    ecarts = pied_figure.controler_page(PAGE_MD.read_text(encoding="utf-8"), figs) if PAGE_MD.exists() \
        else ["page absente : %s" % PAGE_MD]
    if ecarts:
        fail("page : " + " ; ".join(ecarts))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), parite de la figure telephone controlee, rien ecrit."
            % (n, len(A)))
        return 0
    fic = json.dumps(fiches(figs, A), ensure_ascii=False, indent=1) + "\n"
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                        "champ": "France ; jeunes de 18 à 24 ans sauf mention ; aucune série non déclarative ne connaît le statut d'étudiant",
                        "source_calcul": "extrait figé scripts/sources_malaise_etudiant/ (SHA256SUMS), écrit par outils/extrait.py du dossier de recherche",
                        "categories": "lue : calculée sur une réponse brute archivée ; transcrite_verifiee : phrase exigée telle quelle dans le document archivé ; citee : étude citée"},
               "extrait": X, "affichage": A}
    try:
        prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
        releve_jeu.sans_licence(prev, LICENCE)
        prev.pop("releve_le", None)
        if prev == json.loads(json.dumps(payload, ensure_ascii=False)) and OUT_CSV.exists() \
                and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c) and OUT_STATIC.exists() \
                and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                and OUT_FIGURES.exists() and OUT_FIGURES.read_text(encoding="utf-8") == fic:
            # Figures et fiches « Réutiliser » comparées aussi (leçon 11 du pilote) : une légende corrigée est réécrite.
            log("Donnees, figures et fiches identiques : rien ecrit.")
            return 0
    except (OSError, ValueError):
        pass
    rel = releve_jeu.releve(OUT_DATA, payload, date.today().isoformat())
    payload = {"releve_le": rel, "_licence": LICENCE, **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    import cairosvg
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")),
                         output_width=900 if f.endswith("-m.svg") else 1440, background_color="white")
    OUT_FIGURES.write_text(fic, encoding="utf-8")
    log("Ecrit : data/ et static/malaise_etudiant.json, static/malaise_etudiant.csv, data/figures_etudiants.json, "
        "%d figures SVG + PNG (releve_le %s)" % (len(figs), rel))
    return 0


if __name__ == "__main__":
    sys.exit(main())
