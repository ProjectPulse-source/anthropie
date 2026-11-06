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

Usage : python scripts/update_malaise_etudiant.py [--check] [--mutation=etudiants|calendrier|suicides|depense|composition|lyceens]
Sorties : data/ et static/malaise_etudiant.json, static/malaise_etudiant.csv
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import sys
from datetime import date
from pathlib import Path

import langue_generee as lg  # nombres, signes et accord de « point » à la précision affichée
import releve_jeu  # releve_le ne bouge qu'avec une donnée

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_malaise_etudiant"
OUT_DATA = ROOT / "data" / "malaise_etudiant.json"
OUT_STATIC = ROOT / "static" / "malaise_etudiant.json"
OUT_CSV = ROOT / "static" / "malaise_etudiant.csv"
PAGE_URL = "stephane-lalut.com/les-etudiants-vont-ils-plus-mal/"
LICENCE = ("CC BY 4.0 — calcul Stéphane Lalut ; sources Santé publique France (BEH, EnCLASS), DREES, Assurance maladie, "
           "Eurostat (CépiDc-Inserm), Insee (compte de l'éducation, Depp)")
MUTATIONS = ("etudiants", "calendrier", "suicides", "depense", "composition", "lyceens")


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
    return json.loads(p.read_text(encoding="utf-8"))


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
        c["n24"] = 140
    elif m == "depense":        # la dépense de 2024 dépasse le sommet de 2009 : « recule depuis 2009 » faux
        c["dep"] = dict(c["dep"], superieur_euros_constants_2024=dict(c["dep"]["superieur_euros_constants_2024"], **{"2024": 14600}))
    elif m == "composition":    # simulation à 1,2 point : « environ 0,6 point » faux
        c["comp"] = dict(c["comp"], simulation_pts=1.2)
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
    g(ad["tous sexes"]["2017"] < ad["tous sexes"]["2018"] < ad["tous sexes"]["2019"], "la hausse commence des 2018, avant le covid")
    # Section 1 -- ce qu'on fait (hospitalisations)
    g(c["f_var"] > 20, "hospitalisations des jeunes femmes en forte hausse depuis 2019")
    # Section 1 -- suicides
    g(c["sf_var"] > 25, "taux de suicide des femmes de 20-24 ans en nette hausse apres la rupture de 2018")
    g(abs(c["sm_var"]) < 10, "taux des hommes du meme age a peu pres stable")
    g(abs(c["n24"] - c["n23"]) < 2 * c["n_sd"], "2024 : le niveau eleve se maintient, sans nouvelle hausse etablie")
    g(c["X"]["beh2025"]["anxiete_stable_18_75"] is True, "pas de hausse significative des etats anxieux")
    # Section 2 -- qui
    g(c["f1824"]["2021"] - c["f1824"]["2017"] > c["h1824"]["2021"] - c["h1824"]["2017"], "hausse plus forte chez les femmes de 18-24 ans")
    g(c["f_var"] > 2 * max(c["m_var"], 0.1), "celle des jeunes hommes beaucoup moins")
    f = hf["f18_24"]
    g(f["2012"] > f["2013"] > f["2014"], "les hospitalisations des femmes de 18-24 ans baissent jusqu'en 2014")
    pal = [f[str(a)] for a in range(2014, 2018)]
    g((max(pal) - min(pal)) / min(pal) < 0.05, "plafonnent jusqu'en 2017")
    g(all(f[str(a)] > f["2017"] for a in range(2018, c["der"] + 1) if a != 2020) and f[str(c["der"])] > f["2018"],
      "puis montent")
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
    g(lg.depasse(en["risque_depression_lyceennes"]["2024"], 2 * en["risque_depression_lyceens_garcons"]["2024"]),
      "lyceennes : plus du double des lyceens")
    g(min(en["bien_etre_hausse_2022_2024_pts"].values()) > 0, "le bien-etre declare remonte par rapport a 2022")
    # Section 4 -- moyens
    d = c["dep"]["superieur_euros_constants_2024"]
    sommet = max((v, k) for k, v in d.items() if int(k) >= 1980)[1]
    g(sommet == "2009", "la depense par etudiant culmine en 2009")
    g(d["2024"] < d["2009"] and d["2024"] < d["2014"], "puis recule")
    p = c["dep"]["par_etudiant_2024"]
    g(p["universite"] < p["ensemble"] < p["cpge"], "universite sous la moyenne, classes preparatoires au-dessus")
    # Section 5 -- composition
    cp = c["comp"]
    g(cp["par_annee"]["2021"]["ecart_pts"] > cp["par_annee"]["2017"]["ecart_pts"] > 0,
      "part des femmes plus elevee chez les etudiants, ecart qui s'elargit")
    g(0.5 <= cp["simulation_pts"] < 0.75, "environ 0,6 point")
    g(cp["sensibilite_pts"]["min"] <= cp["simulation_pts"] <= cp["sensibilite_pts"]["max"], "simulation dans sa plage de sensibilite")
    return len(G)


def affichage(c: dict) -> dict:
    n = lg.nombre
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
        "hosp_der": der,
        "hosp_f_2014": n(hf["f18_24"]["2014"], 0), "hosp_f_2019": n(hf["f18_24"]["2019"], 0), "hosp_f_der": n(hf["f18_24"][der], 0),
        "hosp_h_2019": n(hf["h18_24"]["2019"], 0), "hosp_h_der": n(hf["h18_24"][der], 0),
        "hosp_f_var": n(c["f_var"], 0), "hosp_h_var": n(c["m_var"], 0),
        "hosp_t1517_2019": n(hf["t15_17"]["2019"], 0), "hosp_t1517_der": n(hf["t15_17"][der], 0),
        "hosp_f1019_2025": n(hf["f10_19"]["2025"], 0),
        "sf_avant": n(c["sf_avant"], 2), "sf_apres": n(c["sf_apres"], 2), "sf_var": n(c["sf_var"], 0), "sm_var": n(c["sm_var"], 0),
        "s_n23": n(c["n23"], 0), "s_n24": n(c["n24"], 0),
        "anx_etu_2021": n(c["X"]["beh2025"]["anxiete_etudiants_2021"]),
        "lyc_2018": n(en["risque_depression_lyceens"]["2018"]), "lyc_2022": n(en["risque_depression_lyceens"]["2022"]),
        "lyc_2024": n(en["risque_depression_lyceens"]["2024"]),
        "lyc_f_2018": n(en["risque_depression_lyceennes"]["2018"]), "lyc_f_2024": n(en["risque_depression_lyceennes"]["2024"]),
        "lyc_g_2024": n(en["risque_depression_lyceens_garcons"]["2024"]),
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
    return A


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
        except SystemExit:
            log("mutation %s : une garde a mordu (attendu)." % m)
            return 0
        fail("mutation %s : aucune garde n'a mordu" % m)
    n = gardes(c)
    A = affichage(c)
    log("Etudiants %s -> %s %% (%s) ; hospit F18-24 2019->%s : %s -> %s ; composition %s"
        % (A["etu_2017"], A["etu_2021"], A["h_etu"], A["hosp_der"], A["hosp_f_2019"], A["hosp_f_der"], A["comp_sim"]))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), rien ecrit." % (n, len(A)))
        return 0
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
                and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(c) and OUT_STATIC.exists():
            log("Donnees identiques : rien ecrit.")
            return 0
    except (OSError, ValueError):
        pass
    rel = releve_jeu.releve(OUT_DATA, payload, date.today().isoformat())
    payload = {"releve_le": rel, "_licence": LICENCE, **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    log("Ecrit : data/ et static/malaise_etudiant.json, static/malaise_etudiant.csv (releve_le %s)" % rel)
    return 0


if __name__ == "__main__":
    sys.exit(main())
