#!/usr/bin/env python3
"""Volet « Adopter » du dossier Promesses : qui est à l'origine des lois votées, et l'engagement de responsabilité
(art. 49, al. 3).

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 2 (v2, gelée au commit
dfd0ec9). Test décisif du 06/10/2026 : test_decisif/adopter/VERDICT.md (19 mutations).
  E2 — origine formelle, au dépôt initial, des lois ordinaires promulguées, par législature de promulgation ; traités
       exclus et dénombrés ; autres natures à part. Concordance AN / Dosleg loi par loi, aucun désaccord.
  E3 — engagements de responsabilité (art. 49, al. 3), un par texte et par étape ; motions liées.
  E1 — parcours des propositions de loi déposées à l'Assemblée jusqu'à la séance, état à la fin de la législature.
       ÉCART AU PROTOCOLE DÉCLARÉ (décision de l'auteur, 06/10/2026, option 2) : le témoin des bulletins de l'AN n'est
       pas réconcilié par identifiant (test_decisif/adopter/reconciliation_e1/) ; la phrase n'est publiée que sur la
       borne du PIRE CAS, l'excès de dépôts sur les bulletins retiré et supposé sans examen.

Sources (scripts/sources_adopter/, constituées par extraire_sources.py) : registre loi par loi e2_lois.csv (JO, AN,
Dosleg, DOLE) ; e3_engagements.csv ; bulletins statistiques de l'AN (bulletins_493.csv) ; fiche n° 64 de l'AN et
rapport n° 802 du Sénat, p. 44 (pages_temoins.json) ; Constitution, art. 24, 39, 48, 49 (Légifrance).

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  B1  articles de la Constitution en vigueur, citations retrouvées mot pour mot ;
  B2  E2 : aucun désaccord d'origine AN / Dosleg ; bornes [P - source unique ; P] ; phrases de la page : moins de la
      moitié sous la XIVe (borne haute), plus de la moitié sous les XVe et XVIe (borne basse) ;
  B3  TÉMOINS : par session 2017-2018 à 2024-2025, nombre de lois hors traités = champ du baromètre d'Appliquer
      (autre producteur) ; 2024-2025 : 45 lois parlementaires sur 56, comme le publie le Sénat ; 2023-2024 compatible
      avec « 58 % » ;
  B4  E3 : engagements par législature = fiche n° 64 de l'AN ; = bulletins, session par session ; catégories de
      l'art. 49, al. 3 (contre-expertise PRO-20261006-144558, P4) : PLF ou PLFSS / autre projet ou proposition ; XVIe :
      les autres textes sont tous la loi de programmation des finances publiques ; aucune motion adoptée de la XIVe à la
      XVIe (bulletins) ; une en 2024-2025.
  B5  E1 : excès de dépôts sur les bulletins = extraction - bulletin, par législature ; phrase « plus de la moitié des
      propositions de loi ordinaires […] sans examen en séance observé » seulement si 2 (Z - e) > N - e partout ;
      part affichée (jeton Zpct, corrigé de l'activité d'EMC, avis entrant du 07/10/2026) seulement si l'arrondi de
      Z / N est celui du pire cas (Z - e) / (N - e).
Autotest de mutation à chaque exécution : origine d'une loi changée dans une source -> B2 ; une loi de 2024-2025
retirée -> B3 ; un engagement de la XVIe retiré -> B4 ; citation de l'art. 49 altérée -> B1 ; XIVe rendue majoritaire
-> B2.

Bilingue (06/10/2026, version anglaise demandée par l'auteur) : un calcul, deux blocs (affichage, affichage_en) aux
mêmes clés, deux jeux de tableaux, des figures -en au même dessin ; la Constitution se cite en anglais dans la traduction
publiée par le Conseil constitutionnel (scripts/sources_promesses_en/, vérifiée mot pour mot, garde B1) ; les autres
textes français se citent en français, suivis de notre traduction (clés *_tr).

Écrit : data/promesses_adopter.json (+ static/), static/promesses_adopter.csv, data/figures_adopter.json,
static/img/adopter-{origine,493}{,-en}.svg/.png. Rien n'est écrit à données identiques.
"""
from __future__ import annotations

import collections
import copy
import csv
import html
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "sources_promesses_en"))
import constitution_en as cen  # noqa: E402
SRC = ROOT / "scripts" / "sources_adopter"
REG_APPLIQUER = ROOT / "scripts" / "sources_appliquer" / "registre_concordance.csv"
PAGE_URL = "stephane-lalut.com/qui-peut-faire-adopter-une-loi/"
PAGE_URL_EN = "stephane-lalut.com/en/who-can-get-a-law-passed-in-france/"
OUT_DATA = ROOT / "data" / "promesses_adopter.json"
OUT_STATIC = ROOT / "static" / "promesses_adopter.json"
OUT_CSV = ROOT / "static" / "promesses_adopter.csv"
OUT_FIGURES = ROOT / "data" / "figures_adopter.json"
OUT_IMG = ROOT / "static" / "img"
RELEVE = "06/10/2026"
LEGS = ["14", "15", "16"]
ROMAIN = {"14": "XIVe", "15": "XVe", "16": "XVIe", "17": "XVIIe"}
PERIODE = {"14": "2012-2017", "15": "2017-2022", "16": "2022-2024", "17": "depuis 2024"}
ROMAIN_EN = {"14": "14th", "15": "15th", "16": "16th", "17": "17th"}
PERIODE_EN = {"14": "2012-2017", "15": "2017-2022", "16": "2022-2024", "17": "since 2024"}
# Citations anglaises de la Constitution : traduction publiée par le Conseil constitutionnel, vérifiée par cen.citer().
CONST_EN = {
    "24": ("24", "Parliament shall pass statutes."),
    "39": ("39", "Both the Prime Minister and Members of Parliament shall have the right to initiate legislation."),
    "48": ("48", "During two weeks of sittings out of four, priority shall be given, in the order determined by the Government, "
                 "to the consideration of texts and to debates which it requests to be included on the agenda."),
    "49a": ("49", "The Prime Minister may, after deliberation by the Council of Ministers, make the passing of a Finance Bill or "
                  "Social Security Financing Bill an issue of a vote of confidence before the National Assembly. In that event, "
                  "the Bill shall be considered passed unless a resolution of no-confidence, tabled within the subsequent "
                  "twenty-four hours, is carried as provided for in the foregoing paragraph."),
    "45a": ("45", "Every Government or Private Member's Bill shall be considered successively in the two Houses of Parliament "
                  "with a view to the passing of an identical text."),
    "45b": ("45", "may convene a joint committee, composed of an equal number of members from each House, to propose a text on "
                  "the provisions still under debate."),
    "45c": ("45", "the Government may, after a further reading by the National Assembly and by the Senate, ask the National "
                  "Assembly to reach a final decision."),
    "49b": ("49", "In addition, the Prime Minister may use the said procedure for one other Government or Private Members' Bill "
                  "per session."),
}
# Notre traduction des citations de témoins (fiche de l'AN, rapport du Sénat), affichée après l'original français.
TEMOINS_TR = {
    "cit_fiche64": "This instrument was nevertheless used six times, on two different bills, during the 14th legislature, once "
                   "during the 15th legislature, and 23 times during the 16th legislature.",
    "cit_censure": "The first motion tabled was carried by the required qualified majority",
    "cit_senat_origine": "Over the session, 80% of the laws adopted (45 out of 56) originated as private members' bills, against 58% in "
                         "2023-2024",
}
MOIS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
           "December"]
SESSIONS = ["%d-%d" % (a, a + 1) for a in range(2017, 2025)]
MOTS = {"une": 1, "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
CONST = {  # article -> (fichier, citation exacte)
    "24": ("legifrance_f1e5f5212fef6ab730c4ed48b20035974af48b59ee63d13a3331e0b76eeae4fa.json", "Le Parlement vote la loi."),
    "39": ("legifrance_751fa83fbb33037dfca31b34cb249316880035dc384b20d05a1b3e138b8df786.json",
           "L'initiative des lois appartient concurremment au Premier ministre et aux membres du Parlement."),
    "48": ("legifrance_376cbf6be973f815b0e9c33efecf371b16a12234c1193d3601a1df641c7b12bb.json",
           "Deux semaines de séance sur quatre sont réservées par priorité, et dans l'ordre que le Gouvernement a fixé, à "
           "l'examen des textes et aux débats dont il demande l'inscription à l'ordre du jour."),
    "49a": ("legifrance_8a30c40da44752bff91c17c1b15577bd338063c08a795785629c90d08ea40ccd.json",
            "Le Premier ministre peut, après délibération du Conseil des ministres, engager la responsabilité du "
            "Gouvernement devant l'Assemblée nationale sur le vote d'un projet de loi de finances ou de financement de la "
            "sécurité sociale. Dans ce cas, ce projet est considéré comme adopté, sauf si une motion de censure, déposée "
            "dans les vingt-quatre heures qui suivent, est votée dans les conditions prévues à l'alinéa précédent."),
    "45a": ("legifrance_9767001efce4060f18bf83ee36faa2520135b46643c9df910a43c3c796ee09a8.json",
            "Tout projet ou proposition de loi est examiné successivement dans les deux Assemblées du Parlement en vue de "
            "l'adoption d'un texte identique."),
    "45b": ("legifrance_9767001efce4060f18bf83ee36faa2520135b46643c9df910a43c3c796ee09a8.json",
            "ont la faculté de provoquer la réunion d'une commission mixte paritaire chargée de proposer un texte sur les "
            "dispositions restant en discussion."),
    "45c": ("legifrance_9767001efce4060f18bf83ee36faa2520135b46643c9df910a43c3c796ee09a8.json",
            "le Gouvernement peut, après une nouvelle lecture par l'Assemblée nationale et par le Sénat, demander à "
            "l'Assemblée nationale de statuer définitivement."),
    "49b": ("legifrance_8a30c40da44752bff91c17c1b15577bd338063c08a795785629c90d08ea40ccd.json",
            "Le Premier ministre peut, en outre, recourir à cette procédure pour un autre projet ou une proposition de loi "
            "par session."),
}
TEMOINS = {
    "cit_fiche64": ("fiche64", "Cet instrument a néanmoins été utilisé à six reprises, sur deux projets de loi différents, "
                    "sous la XIVe législature, à une reprise sous la XVe législature, et à 23 reprises sous la XVIe législature."),
    "cit_censure": ("fiche64", "La première motion déposée a été adoptée selon la majorité qualifiée requise"),
    "cit_senat_origine": ("r25-802|44", "Sur la session, 80 % des lois adoptées (45 sur 56) sont d'origine parlementaire, "
                          "contre 58 % en 2023-2024"),
}
# Catégorie de l'art. 49, al. 3 : projet de loi de finances ou de financement de la sécurité sociale (rectificatives
# comprises) ; la loi de programmation des finances publiques relève de « un autre projet » (PRO-20261006-144558, P4).
FINANCIER = re.compile(r"loi de finances|financement (rectificative )?de la sécurité sociale", re.I)
LPFP = re.compile(r"programmation des finances publiques", re.I)


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def fr(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n).replace(",", "\u202f").replace(".", ",")


def en(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n)


def session(d: str) -> str:
    a = int(d[:4]) if int(d[5:7]) >= 10 else int(d[:4]) - 1
    return "%d-%d" % (a, a + 1)


def lire_csv(p: Path, sep=",") -> list[dict]:
    return list(csv.DictReader(io.StringIO(p.read_text(encoding="utf-8")), delimiter=sep))


def lire() -> dict:
    const = {}
    for k, (f, _) in CONST.items():
        a = json.loads((SRC / f).read_text(encoding="utf-8"))
        a = a.get("contenu") or a.get("article")
        const[k] = {"etat": a["etat"], "texte": norm(a["texte"]), "id": a["id"]}
    return {"const": const, "lois": lire_csv(SRC / "e2_lois.csv"), "eng": lire_csv(SRC / "e3_engagements.csv"),
            "bull": lire_csv(SRC / "bulletins_493.csv"), "reg": lire_csv(REG_APPLIQUER, ";"),
            "e1": lire_csv(SRC / "e1_initiatives_extrait.csv"), "dep": lire_csv(SRC / "bulletins_depots.csv"),
            "pages": json.loads((SRC / "pages_temoins.json").read_text(encoding="utf-8"))}


# ------------------------------------------------------------------ calcul et gardes
def calculer(S: dict) -> tuple[dict, list[str]]:
    g, cit = [], {}
    for k, (_, c) in CONST.items():
        if S["const"][k]["etat"] != "VIGUEUR" or norm(c) not in S["const"][k]["texte"]:
            raise Arret("B1 : Constitution art. %s : texte non en vigueur ou citation introuvable" % k)
        cit["cit_art" + k] = norm(c)
    for k, (pg, c) in TEMOINS.items():
        if norm(c) not in S["pages"][pg]["texte"]:
            raise Arret("B1 : citation %s absente de %s" % (k, pg))
        cit[k] = norm(c)
    try:
        tcen = cen.texte()
        for k, (art, c) in CONST_EN.items():
            cit["en_cit_art" + k] = cen.citer(art, c, tcen)
    except ValueError as e:
        raise Arret("B1 : %s" % e)
    g.append("B1 : %d citations de la Constitution (FR Legifrance, EN Conseil constitutionnel), %d des temoins, retrouvees mot pour mot"
             % (len(CONST), len(TEMOINS)))

    # --- E2
    L = S["lois"]
    for r in L:
        if r["origine_AN"] and r["origine_Dosleg"] and r["origine_AN"] != r["origine_Dosleg"]:
            raise Arret("B2 : %s : origine AN (%s) != Dosleg (%s)" % (r["numero"], r["origine_AN"], r["origine_Dosleg"]))
    leg = {}
    for l in LEGS + ["17"]:
        o = [r for r in L if r["legislature"] == l and r["nature"] == "ordinaire"]
        c = collections.Counter(r["origine"] for r in o)
        P = c["parlementaire AN"] + c["parlementaire Sénat"]
        uniq = sum(1 for r in o if r["origine"].startswith("parlementaire") and r["origine_source"].startswith("source unique"))
        leg[l] = {"N": len(o), "P": P, "Pmin": P - uniq, "gouv": c["gouvernement"], "AN": c["parlementaire AN"],
                  "SEN": c["parlementaire Sénat"], "traites": sum(1 for r in L if r["legislature"] == l and r["nature"] == "traite"),
                  "autres": sum(1 for r in L if r["legislature"] == l and r["nature"] not in ("ordinaire", "traite"))}
        if leg[l]["N"] != leg[l]["P"] + leg[l]["gouv"]:
            raise Arret("B2 : %s : origine indeterminee ou inconnue" % l)
    fin_parl = [r["numero"] for r in L if r["legislature"] in LEGS and r["nature"] == "finances_fss" and r["origine"] != "gouvernement"]
    if fin_parl:  # phrase : « les lois de finances et de financement de la sécurité sociale viennent toutes d'un projet »
        raise Arret("B2 : lois financieres d'origine parlementaire : %s" % fin_parl)
    x14, x15, x16 = leg["14"], leg["15"], leg["16"]
    if not (2 * x14["P"] < x14["N"] and 2 * x15["Pmin"] > x15["N"] and 2 * x16["Pmin"] > x16["N"]):
        raise Arret("B2 : « moins de la moitie sous la XIVe, plus de la moitie sous les XVe et XVIe » faux")
    g.append("B2 : origine concordante AN/Dosleg ; parlementaires XIV %d/%d, XV %d-%d/%d, XVI %d/%d"
             % (x14["P"], x14["N"], x15["Pmin"], x15["P"], x15["N"], x16["P"], x16["N"]))

    # --- témoins par session (autre producteur pour le champ ; publication du Sénat pour l'origine)
    regN = collections.Counter(r["session"] for r in S["reg"])
    ses = {}
    for s in SESSIONS:
        o = [r for r in L if r["nature"] != "traite" and r["legislature"] != "" and session(r["date_promulgation"]) == s]
        ses[s] = {"N": len(o), "P": sum(1 for r in o if r["origine"].startswith("parlementaire"))}
        if ses[s]["N"] != regN[s]:
            raise Arret("B3 : session %s : %d lois hors traites ici, %d au barometre (Appliquer)" % (s, ses[s]["N"], regN[s]))
    if (ses["2024-2025"]["P"], ses["2024-2025"]["N"]) != (45, 56) or "(45 sur 56)" not in cit["cit_senat_origine"]:
        raise Arret("B3 : 2024-2025 : %d/%d contre 45 sur 56 publies par le Senat" % (ses["2024-2025"]["P"], ses["2024-2025"]["N"]))
    if not abs(100 * ses["2023-2024"]["P"] / ses["2023-2024"]["N"] - 58) < 1:
        raise Arret("B3 : 2023-2024 incompatible avec « 58 % »")
    g.append("B3 : champ par session = barometre (8 sessions) ; 2024-2025 45/56 = Senat ; 2023-2024 %d/%d ~ 58 %%"
             % (ses["2023-2024"]["P"], ses["2023-2024"]["N"]))

    # --- E3
    E = S["eng"]
    eng = {}
    for l in LEGS + ["17"]:
        e = [r for r in E if r["legislature"] == l]
        eng[l] = {"n": len(e), "fin": sum(1 for r in e if FINANCIER.search(r["titre"])),
                  "textes": len({r["dossier_texte"] for r in e}),
                  "lpfp": sum(1 for r in e if LPFP.search(r["titre"])),
                  "adoptees": sum(int(r["motions_adoptees"] or 0) for r in e)}
    m = re.search(r"à (\w+) reprises, sur (\w+) projets de loi différents, sous la XIVe législature, à (\w+) reprise sous "
                  r"la XVe législature, et à (\w+) reprises sous la XVIe", cit["cit_fiche64"])
    nb = [int(v) if v.isdigit() else MOTS[v] for v in m.groups()]
    if [eng["14"]["n"], eng["14"]["textes"], eng["15"]["n"], eng["16"]["n"]] != nb:
        raise Arret("B4 : engagements %s != fiche n° 64 %s" % ([eng[l]["n"] for l in LEGS], nb))
    B = S["bull"]
    for l in LEGS + ["17"]:  # sur la période couverte par les bulletins (XVIIe : jusqu'au 30/09/2025)
        bl = [r for r in B if r["legislature"] == l]
        b = sum(int(r["engagements_493"]) for r in bl)
        fin = max(r["fin"] for r in bl)
        n = sum(1 for r in E if r["legislature"] == l and r["date"] <= fin)
        if b != n:
            raise Arret("B4 : legislature %s : %d engagements aux bulletins, %d extraits jusqu'au %s" % (l, b, n, fin))
    if eng["14"]["fin"] != 0:  # phrase : « sur N projets de loi qui n'étaient pas des textes financiers »
        raise Arret("B4 : XIVe : engagement sur un texte financier")
    if eng["15"]["fin"] != 0:
        raise Arret("B4 : XVe : engagement sur un PLF ou un PLFSS")
    if eng["16"]["n"] - eng["16"]["fin"] != eng["16"]["lpfp"] or eng["16"]["lpfp"] == 0:
        raise Arret("B4 : XVIe : autres textes que PLF/PLFSS et LPFP")
    if eng["17"]["fin"] != eng["17"]["n"]:
        raise Arret("B4 : XVIIe : engagement hors PLF/PLFSS")
    adoptees_bull = {l: sum(int(r["motions_493_adoptees"] or 0) for r in B if r["legislature"] == l) for l in LEGS + ["17"]}
    if any(adoptees_bull[l] for l in LEGS) or adoptees_bull["17"] != 1:
        raise Arret("B4 : motions adoptees aux bulletins : %s" % adoptees_bull)
    cens = [r for r in E if int(r["motions_adoptees"] or 0) > 0]
    if len(cens) != 1 or cens[0]["legislature"] != "17":
        raise Arret("B4 : engagements suivis d'une motion adoptee : %d" % len(cens))
    MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    an, mo, jo = map(int, cens[0]["date"].split("-"))
    cit["censure_date"] = "%d%s %s %d" % (jo, "er" if jo == 1 else "", MOIS[mo - 1], an)
    cit["en_censure_date"] = "%d %s %d" % (jo, MOIS_EN[mo - 1], an)
    g.append("B4 : engagements XIV %d, XV %d, XVI %d (= fiche 64 et bulletins) ; XVI %d PLF/PLFSS + %d LPFP ; 0 motion adoptee XIV-XVI"
             % (eng["14"]["n"], eng["15"]["n"], eng["16"]["n"], eng["16"]["fin"], eng["16"]["lpfp"]))

    # --- E1 (écart au protocole déclaré : borne du pire cas)
    I = S["e1"]
    e1 = {}
    for l in LEGS:
        o = [r for r in I if r["legislature"] == l and r["origine"] == "parlementaire" and r["nature"] == "ordinaire"]
        ext = sum(1 for r in I if r["legislature"] == l and r["origine"] == "parlementaire")
        bul = sum(int(r["ppl_an_premiere_lecture"]) for r in S["dep"] if r["legislature"] == l)
        c = collections.Counter(r["etat"] for r in o)
        N, Z, U = len(o), c["1"], c["5"]
        e = ext - bul
        if e < 0:
            raise Arret("B5 : %s : extraction sous le bulletin, le pire cas change de sens" % l)
        dur = sorted(int(r["duree_jours"]) for r in I if r["legislature"] == l and r["origine"] == "parlementaire")
        e1[l] = {"N": N, "Z": Z, "U": U, "ext": ext, "bul": bul, "exces": e, "Nw": N - e, "Zw": Z - e,
                 "mediane_jours": dur[(len(dur) - 1) // 2]}
        if not 2 * (Z - e) > N - e:
            raise Arret("B5 : %s : pire cas %d/%d : « plus de la moitie » faux" % (l, Z - e, N - e))
        if round(100 * Z / N) != round(100 * (Z - e) / (N - e)):
            raise Arret("B5 : %s : part sans examen %d/%d et pire cas %d/%d : arrondis differents" % (l, Z, N, Z - e, N - e))
    if not 2 * e1["16"]["mediane_jours"] < e1["14"]["mediane_jours"]:  # « plus de deux fois plus court »
        raise Arret("B5 : duree mediane XVIe pas deux fois plus courte que XIVe")
    g.append("B5 : E1 pire cas XIV %d/%d, XV %d/%d, XVI %d/%d (exces sur bulletins %d, %d, %d)"
             % (tuple(v for l in LEGS for v in (e1[l]["Zw"], e1[l]["Nw"])) + tuple(e1[l]["exces"] for l in LEGS)))
    return {"leg": leg, "ses": ses, "eng": eng, "e1": e1, "cit": cit}, g


def affichage(r: dict) -> dict:
    A = {"releve": RELEVE}
    for l, x in r["leg"].items():
        A.update({"N%s" % l: fr(x["N"]), "P%s" % l: fr(x["P"]), "Pmin%s" % l: fr(x["Pmin"]), "G%s" % l: fr(x["gouv"]),
                  "AN%s" % l: fr(x["AN"]), "SEN%s" % l: fr(x["SEN"]), "T%s" % l: fr(x["traites"]),
                  "Ppct%s" % l: fr(100 * x["P"] / x["N"])})
    for l, x in r["eng"].items():
        A.update({"E%s" % l: fr(x["n"]), "Efin%s" % l: fr(x["fin"]), "Etextes%s" % l: fr(x["textes"]),
                  "Eautre%s" % l: fr(x["n"] - x["fin"]), "Efois%s" % l: fr(x["n"]) + " fois"})
    for l, x in r["e1"].items():
        A.update({"Z%s" % l: fr(x["Z"]), "NZ%s" % l: fr(x["N"]), "Zpct%s" % l: fr(100 * x["Z"] / x["N"]), "Zw%s" % l: fr(x["Zw"]), "Nw%s" % l: fr(x["Nw"]),
                  "exces%s" % l: fr(x["exces"]), "bul%s" % l: fr(x["bul"]), "ext%s" % l: fr(x["ext"]),
                  "med%s" % l: fr(x["mediane_jours"])})
    s1, s2 = r["ses"]["2017-2018"], r["ses"]["2024-2025"]
    A.update({"s1718_P": fr(s1["P"]), "s1718_N": fr(s1["N"]), "s2425_P": fr(s2["P"]), "s2425_N": fr(s2["N"]),
              "releve_le": "06/10/2026 (données de l'Assemblée nationale et base Dosleg du Sénat du 06/10/2026, Journal "
                           "officiel ; bulletins statistiques de l'Assemblée nationale)"})
    A.update({k: v for k, v in r["cit"].items() if not k.startswith("en_")})
    A.update({k + "_tr": v for k, v in TEMOINS_TR.items()})
    return A


def affichage_en(r: dict) -> dict:
    A = {"releve": "6 October 2026"}
    for l, x in r["leg"].items():
        A.update({"N%s" % l: en(x["N"]), "P%s" % l: en(x["P"]), "Pmin%s" % l: en(x["Pmin"]), "G%s" % l: en(x["gouv"]),
                  "AN%s" % l: en(x["AN"]), "SEN%s" % l: en(x["SEN"]), "T%s" % l: en(x["traites"]),
                  "Ppct%s" % l: en(100 * x["P"] / x["N"])})
    for l, x in r["eng"].items():
        A.update({"E%s" % l: en(x["n"]), "Efin%s" % l: en(x["fin"]), "Etextes%s" % l: en(x["textes"]),
                  "Eautre%s" % l: en(x["n"] - x["fin"]),
                  "Efois%s" % l: {1: "once", 2: "twice"}.get(x["n"], en(x["n"]) + " times")})
    for l, x in r["e1"].items():
        A.update({"Z%s" % l: en(x["Z"]), "NZ%s" % l: en(x["N"]), "Zpct%s" % l: en(100 * x["Z"] / x["N"]), "Zw%s" % l: en(x["Zw"]), "Nw%s" % l: en(x["Nw"]),
                  "exces%s" % l: en(x["exces"]), "bul%s" % l: en(x["bul"]), "ext%s" % l: en(x["ext"]),
                  "med%s" % l: en(x["mediane_jours"])})
    s1, s2 = r["ses"]["2017-2018"], r["ses"]["2024-2025"]
    A.update({"s1718_P": en(s1["P"]), "s1718_N": en(s1["N"]), "s2425_P": en(s2["P"]), "s2425_N": en(s2["N"]),
              "releve_le": "6 October 2026 (National Assembly open data and the Senate's Dosleg database of 6 October 2026, "
                           "Journal officiel; National Assembly statistical bulletins)"})
    for k, v in r["cit"].items():
        if k.startswith("cit_art"):
            A[k] = r["cit"]["en_" + k]
        elif not k.startswith("en_") and k != "censure_date":
            A[k] = v  # citation de témoin : l'original français, suivi de sa traduction (_tr)
    A["censure_date"] = r["cit"]["en_censure_date"]
    A.update({k + "_tr": v for k, v in TEMOINS_TR.items()})
    return A


def tableaux_en(r: dict) -> dict:
    lois = [[ROMAIN_EN[l] + " legislature (" + PERIODE_EN[l] + (", ongoing on 6 October 2026" if l == "17" else "") + ")",
             en(x["N"]), en(x["gouv"]), en(x["AN"]), en(x["SEN"]),
             en(x["P"]) + ("" if x["Pmin"] == x["P"] else " (at least %s)" % en(x["Pmin"])), en(x["traites"])]
            for l, x in r["leg"].items()]
    ses = [[s, en(x["N"]), en(x["P"]), en(100 * x["P"] / x["N"]) + "%"] for s, x in r["ses"].items()]
    eng = [[ROMAIN_EN[l] + (" (ongoing)" if l == "17" else ""), en(x["n"]), en(x["fin"]), en(x["n"] - x["fin"]), en(x["adoptees"])]
           for l, x in r["eng"].items()]
    e1 = [[ROMAIN_EN[l] + " (" + PERIODE_EN[l] + ")", en(x["N"]), en(x["Z"]), "%s out of %s" % (en(x["Zw"]), en(x["Nw"])),
           "%s / %s" % (en(x["ext"]), en(x["bul"])), en(x["mediane_jours"])] for l, x in r["e1"].items()]
    return {
        "lois": {"entetes": ["Legislature of promulgation", "Laws", "Government bill", "Private member's bill tabled in the Assembly",
                             "Private member's bill tabled in the Senate", "Parliamentary origin", "Laws authorising a treaty (excluded)"],
                 "lignes": lois},
        "sessions": {"entetes": ["Session", "Laws promulgated, excluding treaties", "Of parliamentary origin", "Share"], "lignes": ses},
        "engagements": {"entetes": ["Legislature", "Uses of art. 49, para. 3", "On a Finance Bill or Social Security Financing Bill",
                                    "On another bill", "Motions of no confidence carried"], "lignes": eng},
        "e1": {"entetes": ["Legislature of tabling", "Ordinary private members' bills tabled first in the Assembly",
                           "Not observed debated in the chamber before the end of the legislature",
                           "Worst case: excess over the bulletins removed", "Bills tabled: data / bulletins",
                           "Median time from tabling to end of legislature (days)"], "lignes": e1},
    }


def tableaux(r: dict) -> dict:
    lois = [[ROMAIN[l] + " (" + PERIODE[l] + (", en cours au " + RELEVE if l == "17" else "") + ")", fr(x["N"]), fr(x["gouv"]),
             fr(x["AN"]), fr(x["SEN"]), fr(x["P"]) + ("" if x["Pmin"] == x["P"] else " (au moins %s)" % fr(x["Pmin"])),
             fr(x["traites"])] for l, x in r["leg"].items()]
    ses = [[s, fr(x["N"]), fr(x["P"]), fr(100 * x["P"] / x["N"]) + " %"] for s, x in r["ses"].items()]
    eng = [[ROMAIN[l] + (" (en cours)" if l == "17" else ""), fr(x["n"]), fr(x["fin"]), fr(x["n"] - x["fin"]), fr(x["adoptees"])]
           for l, x in r["eng"].items()]
    e1 = [[ROMAIN[l] + " (" + PERIODE[l] + ")", fr(x["N"]), fr(x["Z"]), "%s sur %s" % (fr(x["Zw"]), fr(x["Nw"])),
           "%s / %s" % (fr(x["ext"]), fr(x["bul"])), fr(x["mediane_jours"])] for l, x in r["e1"].items()]
    return {
        "lois": {"entetes": ["Législature de promulgation", "Lois ordinaires", "Projet du Gouvernement",
                             "Proposition déposée à l'Assemblée", "Proposition déposée au Sénat", "Origine parlementaire",
                             "Lois autorisant un traité (exclues)"], "lignes": lois},
        "sessions": {"entetes": ["Session", "Lois promulguées hors traités", "D'origine parlementaire", "Part"], "lignes": ses},
        "engagements": {"entetes": ["Législature", "Engagements (art. 49, al. 3)", "Sur un projet de loi de finances ou de financement de la sécurité sociale",
                                    "Sur un autre projet ou une proposition", "Motions de censure adoptées"], "lignes": eng},
        "e1": {"entetes": ["Législature de dépôt", "Propositions de loi ordinaires déposées à l'Assemblée",
                           "Sans examen en séance observé avant la fin de la législature",
                           "Pire cas : excès sur les bulletins retiré", "Dépôts de propositions : données / bulletins",
                           "Durée médiane entre dépôt et fin de législature (jours)"], "lignes": e1},
    }


# ------------------------------------------------------------------ figures
W = 720
BLEU, BLEU_CLAIR, GRIS, GRIS_CLAIR = "#184f95", "#7fa3cf", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LANG = "fr"


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def cadre(H, ident, titre, sous, desc) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H + 48, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def cartouche(H, src, note) -> list[str]:
    out = ['<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (H + 2, W, H + 2, GRID)]
    for k, (t, c) in enumerate(((src, INK2), (note, INK2), (LICENCES[LANG], MUTED))):
        out.append('<text x="0" y="%d" font-size="9" fill="%s">%s</text>' % (H + 15 + 12 * k, c, esc(t)))
    return out


def legende(e, y, items) -> None:
    x = 0
    for col, lab in items:
        e.append('<rect x="%d" y="%d" width="11" height="11" fill="%s"/>' % (x, y - 9, col))
        e.append(txt(x + 16, y, lab, 10, INK2))
        x += 16 + 6.2 * len(lab) + 18


T = {
    "fr": {"src1": "Assemblée nationale (données ouvertes, dossiers législatifs) et Sénat (base Dosleg), 06/10/2026 ; Journal officiel",
           "note1": "Hors traités, lois de finances, de financement de la sécurité sociale et organiques. Origine au dépôt, non l'influence.",
           "src2": "Assemblée nationale : dossiers législatifs, bulletins statistiques, fiche n° 64 (engagements de responsabilité)",
           "note2": "Catégories de l'art. 49, al. 3 : la loi de programmation des finances publiques est un « autre projet ». XVIIe en cours au " + RELEVE + ".",
           "t1": "Qui est à l'origine des lois ordinaires promulguées ?",
           "s1": "nombre de lois, par législature de promulgation ; trait noir : la moitié des lois",
           "d1": "Barres horizontales par législature : lois issues d'un projet du Gouvernement, d'une proposition déposée à "
                 "l'Assemblée, d'une proposition déposée au Sénat. XIVe : {P14} d'origine parlementaire sur {N14} ; XVe : {P15} sur "
                 "{N15} ; XVIe : {P16} sur {N16} ; XVIIe en cours.",
           "l1": ["projet du Gouvernement", "proposition déposée à l'Assemblée", "proposition déposée au Sénat"],
           "lois": "{} lois", "encours": "* en cours au " + RELEVE,
           "t2": "Engagements de responsabilité sur un texte (art. 49, al. 3)",
           "s2": "nombre d'engagements, par législature ; un engagement par texte et par étape de lecture",
           "d2": "Barres horizontales par législature : engagements sur un projet de loi de finances ou de financement de la "
                 "sécurité sociale, et sur un autre projet ou une proposition. XIVe : {E14}, sur d'autres projets ; XVe : {E15} ; "
                 "XVIe : {E16}, dont {Eautre16} sur la loi de programmation des finances publiques ; XVIIe en cours.",
           "l2": ["projet de loi de finances ou de financement de la sécurité sociale", "autre projet ou proposition"]},
    "en": {"src1": "National Assembly (open data, legislative files) and Senate (Dosleg database), 6 October 2026; Journal officiel",
           "note1": "Excluding treaties, finance, social security financing and institutional acts. Origin at tabling, not influence.",
           "src2": "National Assembly: legislative files, statistical bulletins, summary sheet no. 64 (Government responsibility)",
           "note2": "Categories of art. 49, para. 3: the public finance programming act is 'one other bill'. 17th ongoing on 6 October 2026.",
           "t1": "Who initiated the laws promulgated in France?",
           "s1": "number of laws, by legislature of promulgation; black mark: half of the laws",
           "d1": "Horizontal bars by legislature: laws arising from a Government bill, from a private member's bill tabled in the "
                 "National Assembly, from one tabled in the Senate. 14th: {P14} of parliamentary origin out of {N14}; 15th: {P15} "
                 "out of {N15}; 16th: {P16} out of {N16}; 17th ongoing.",
           "l1": ["Government bill", "private member's bill, National Assembly", "private member's bill, Senate"],
           "lois": "{} laws", "encours": "* ongoing on 6 October 2026",
           "t2": "Bills made an issue of a vote of confidence (art. 49, para. 3)",
           "s2": "number of uses, by legislature; one per bill and per reading stage",
           "d2": "Horizontal bars by legislature: uses on a Finance Bill or Social Security Financing Bill, and on another "
                 "bill. 14th: {E14}, on other bills; 15th: {E15}; 16th: {E16}, including {Eautre16} on the public finance "
                 "programming act; 17th ongoing.",
           "l2": ["Finance Bill or Social Security Financing Bill", "other bill"]},
}


def lib_leg(l: str) -> str:
    if LANG == "en":
        return ROMAIN_EN[l] + " (" + PERIODE_EN[l] + ")" + (" *" if l == "17" else "")
    return ROMAIN[l] + " (" + PERIODE[l] + ")" + (" *" if l == "17" else "")


def nb(n) -> str:
    return en(n) if LANG == "en" else fr(n)


def fig_origine(r: dict, A: dict) -> str:
    H = 250
    x0, x1, y0, pas = 150, W - 70, 74, 34
    vmax = 250
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    L = T[LANG]
    e = cadre(H, "ao", L["t1"], L["s1"], L["d1"].format(**A))
    legende(e, 58, list(zip((GRIS_CLAIR, BLEU, BLEU_CLAIR), L["l1"])))
    for v in range(0, vmax + 1, 50):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 4 - 6, GRID))
        e.append(txt(X(v), y0 + pas * 4 + 8, str(v), 9, MUTED, "middle"))
    for i, (l, x) in enumerate(r["leg"].items()):
        y = y0 + i * pas
        e.append(txt(0, y + 14, lib_leg(l), 10, INK))
        a = 0
        for v, col in ((x["gouv"], GRIS_CLAIR), (x["AN"], BLEU), (x["SEN"], BLEU_CLAIR)):
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2"/>' % (X(x["N"] / 2), y - 3, X(x["N"] / 2), y + 23, INK))
        e.append(txt(X(a) + 4, y + 14, L["lois"].format(nb(x["N"])), 9, INK2))
    e.append(txt(0, y0 + pas * 4 + 22, L["encours"], 9, INK2))
    e += cartouche(H, L["src1"], L["note1"])
    e.append("</svg>")
    return "\n".join(e)


def fig_493(r: dict, A: dict) -> str:
    H = 250
    x0, x1, y0, pas = 150, W - 90, 74, 34
    vmax = 25
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    L = T[LANG]
    e = cadre(H, "a4", L["t2"], L["s2"], L["d2"].format(**A))
    legende(e, 58, list(zip((BLEU, GRIS_CLAIR), L["l2"])))
    for v in range(0, vmax + 1, 5):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 4 - 6, GRID))
        e.append(txt(X(v), y0 + pas * 4 + 8, str(v), 9, MUTED, "middle"))
    for i, (l, x) in enumerate(r["eng"].items()):
        y = y0 + i * pas
        e.append(txt(0, y + 14, lib_leg(l), 10, INK))
        a = 0
        for v, col in ((x["fin"], BLEU), (x["n"] - x["fin"], GRIS_CLAIR)):
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append(txt(X(a) + 4, y + 14, nb(x["n"]), 10, INK, weight="600"))
    e.append(txt(0, y0 + pas * 4 + 22, L["encours"], 9, INK2))
    e += cartouche(H, L["src2"], L["note2"])
    e.append("</svg>")
    return "\n".join(e)


MONTRE_EN = {
    "origine": "Among the laws promulgated in the scope studied (excluding treaties, finance, social security financing and "
               "institutional acts), {P14} out of {N14} originated as private members' bills during the 14th legislature, {P15} out of {N15} "
               "during the 15th and {P16} out of {N16} during the 16th; formal origin at the initial tabling.",
    "493": "The Government made the passing of a bill an issue of a vote of confidence (art. 49, para. 3) {E14} times during the 14th legislature, "
           "{Efois15} during the 15th and {E16} times during the 16th, including {Efin16} on a Finance Bill or Social Security "
           "Financing Bill.",
}


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    montre = {
        "origine": ("adopter-origine", "Parmi les lois promulguées du champ étudié (hors traités, lois de finances, de financement "
                    "de la sécurité sociale et organiques), %s sur %s sont d'origine parlementaire sous la "
                    "XIVe législature, %s sur %s sous la XVe et %s sur %s sous la XVIe ; origine formelle au dépôt initial."
                    % (A["P14"], A["N14"], A["P15"], A["N15"], A["P16"], A["N16"])),
        "493": ("adopter-493", "Le Gouvernement a engagé sa responsabilité sur un texte (art. 49, al. 3) %s fois sous la XIVe "
                "législature, %s fois sous la XVe et %s fois sous la XVIe, dont %s sur un projet de loi de finances ou de "
                "financement de la sécurité sociale." % (A["E14"], A["E15"], A["E16"], A["Efin16"])),
    }
    res = {}
    for lang, suf in (("fr", ""), ("en", "-en")):
        out = []
        for ident, (fichier, m) in montre.items():
            svg = figs[fichier + suf + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
            cart = [c for c in cart if not c.startswith("* ")]
            if len(cart) != 3 or cart[-1] != LICENCES[lang]:
                raise Arret("fiche %s%s : cartouche illisible" % (fichier, suf))
            out.append(dict(id=ident, fichier=fichier + suf, titre=titre,
                            montre=m if lang == "fr" else MONTRE_EN[ident].format(**A_en), source=cart[0], precaution=cart[1]))
        res[lang] = out
    return res


def csv_texte(r: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "periode", "categorie", "valeur", "unite", "source"])
    for l, x in r["leg"].items():
        for k in ("N", "gouv", "AN", "SEN", "P", "Pmin", "traites", "autres"):
            w.writerow(["lois_ordinaires_promulguees", "legislature_" + l, k, x[k], "lois", "AN, Dosleg, JO"])
    for s, x in r["ses"].items():
        w.writerow(["lois_hors_traites", s, "N", x["N"], "lois", "AN, Dosleg, JO"])
        w.writerow(["lois_hors_traites", s, "origine_parlementaire", x["P"], "lois", "AN, Dosleg, JO"])
    for l, x in r["e1"].items():
        for k in ("N", "Z", "U", "exces", "Nw", "Zw", "ext", "bul", "mediane_jours"):
            w.writerow(["propositions_deposees_AN", "legislature_" + l, k, x[k], "textes", "AN, bulletins statistiques"])
    for l, x in r["eng"].items():
        for k in ("n", "fin", "lpfp", "adoptees"):
            w.writerow(["engagements_49_3", "legislature_" + l, k, x[k], "engagements", "AN"])
    return buf.getvalue()


def autotest(S: dict) -> list[str]:
    out = []

    def origine(m):
        for r in m["lois"]:
            if r["legislature"] == "15" and r["origine_AN"] == "parlementaire AN":
                r["origine_AN"] = "gouvernement"
                return

    def retire(m):
        for i, r in enumerate(m["lois"]):
            if r["nature"] == "ordinaire" and session(r["date_promulgation"]) == "2024-2025":
                del m["lois"][i]
                return

    def engagement(m):
        for i, r in enumerate(m["eng"]):
            if r["legislature"] == "16":
                del m["eng"][i]
                return

    def citation(m):
        m["const"]["49b"]["texte"] = m["const"]["49b"]["texte"].replace("par session", "par an")

    def majorite(m):
        n = 0
        for r in m["lois"]:
            if r["legislature"] == "14" and r["nature"] == "ordinaire" and r["origine"] == "gouvernement" and n < 12:
                for k in ("origine", "origine_AN", "origine_Dosleg"):
                    if r[k]:
                        r[k] = "parlementaire AN"
                n += 1

    def bulletins(m):  # bulletins de la XIVe ramenés à 400 dépôts (excès 1 311 ; il en faut 1 249) : le pire cas passe sous la moitié
        r0 = [r for r in m["dep"] if r["legislature"] == "14"]
        tot = sum(int(r["ppl_an_premiere_lecture"]) for r in r0)
        r0[0]["ppl_an_premiere_lecture"] = str(int(r0[0]["ppl_an_premiere_lecture"]) - (tot - 400))

    for nom, mut, pref in (("origine changee dans une source", origine, "B2"), ("loi 2024-2025 retiree", retire, "B3"),
                           ("engagement XVIe retire", engagement, "B4"), ("art. 49 altere", citation, "B1"),
                           ("XIVe rendue majoritaire", majorite, "B2"), ("bulletins XIV abaisses", bulletins, "B5")):
        m = copy.deepcopy(S)
        mut(m)
        try:
            calculer(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith(pref) or str(e).startswith("mutation"):
                raise
            out.append("%s -> %s" % (nom, str(e)[:70]))
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def _main() -> int:
    S = lire()
    r, g = calculer(S)
    for m in autotest(S):
        log("autotest : la mutation a mordu : " + m)
    A, A_en = affichage(r), affichage_en(r)
    if set(A) != set(A_en):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    if "--check" in sys.argv[1:]:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        figs["adopter-origine%s.svg" % suf] = fig_origine(r, AA)
        figs["adopter-493%s.svg" % suf] = fig_493(r, AA)
    LANG = "fr"
    fi = fiches(figs, A, A_en)
    csvt = csv_texte(r)
    payload = {
        "releve_le": "2026-10-06",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Assemblée nationale, Sénat (Dosleg), Journal officiel "
                    "(DILA), Légifrance",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Adopter, E1 (pire cas, écart déclaré), E2 et E3",
                 "constitution": {k: v["id"] for k, v in S["const"].items()},
                 "temoins": {k: v["sha256_document"] for k, v in S["pages"].items()},
                 "definitions": {
                     "origine": "origine formelle au dépôt initial : projet du Gouvernement, proposition déposée à l'Assemblée "
                                "nationale, proposition déposée au Sénat ; rattachement à la législature de promulgation",
                     "Pmin": "origine parlementaire établie par les deux sources (AN et Dosleg) ; l'écart avec P vient de lois "
                             "dont le dossier manque aux fichiers de l'AN pour un motif établi (dépôt sous la législature "
                             "précédente)",
                     "engagement": "un engagement de responsabilité (art. 49, al. 3) par texte et par étape de lecture",
                     "fin": "engagement sur un projet de loi de finances ou de financement de la sécurité sociale "
                            "(rectificatives comprises), catégorie de l'art. 49, al. 3 ; la loi de programmation des finances "
                            "publiques relève d'« un autre projet »",
                     "E1": "proposition de loi ordinaire déposée en premier lieu à l'Assemblée ; « sans examen en séance "
                           "observé avant la fin de la législature » ; pire cas : excès des dépôts extraits sur les bulletins "
                           "statistiques de l'AN retiré du champ et des propositions sans examen (écart au protocole déclaré)"},
                 "limites": "l'origine formelle n'observe ni l'influence du Gouvernement sur une proposition, ni les "
                            "amendements ; les dépôts extraits ne concordent pas texte par texte avec les bulletins de "
                            "l'Assemblée : E1 est publié sur la borne du pire cas"},
        "gardes": g,
        "calcul": {"legislatures": r["leg"], "sessions": r["ses"], "engagements": r["eng"]},
        "tableaux": tableaux(r),
        "tableaux_en": tableaux_en(r),
        "affichage": A,
        "affichage_en": A_en,
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    if (OUT_DATA.exists() and OUT_DATA.read_text(encoding="utf-8") == txt_json and OUT_CSV.exists()
            and OUT_CSV.read_text(encoding="utf-8-sig") == csvt
            and all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s for n, s in figs.items())
            and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fi):
        log("Donnees et figures identiques : rien ecrit.")
        return 0
    OUT_DATA.write_text(txt_json, encoding="utf-8")
    OUT_STATIC.write_text(txt_json, encoding="utf-8")
    OUT_CSV.write_text(csvt, encoding="utf-8-sig", newline="\n")
    for n, s in figs.items():
        (OUT_IMG / n).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")), output_width=1440,
                         background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_adopter.json, static/promesses_adopter.{json,csv}, data/figures_adopter.json, 4 figures SVG + PNG (FR, EN)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
