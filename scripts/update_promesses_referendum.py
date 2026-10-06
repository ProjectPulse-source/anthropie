#!/usr/bin/env python3
"""Prolongement « Référendum » du dossier Promesses : le registre des référendums nationaux et le référendum
d'initiative partagée, arrêtés au 05/10/2026.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, « Prolongement R » (gelé au
commit 324c9cd du dépôt D:/PRO) ; tests décisifs R-E1 et R-E2 (commit 368a020), décision de l'auteur du 06/10/2026 sur
R-E2 (option a : la page dit les deux dépôts sans saisine, sans leur prêter de cause).

Entrées (script LOCAL : les archives ne sont pas dans le dépôt du site ; il s'arrête si elles manquent) :
  - stock CONSTIT de la DILA (décisions du Conseil constitutionnel), global du 13/07/2025 et incréments jusqu'au
    05/10/2026, extrait sous .../sondes/referendum/constit/ ;
  - articles de la Constitution archivés par le serveur `sources` (Légifrance, D:/PRO/02_FABRIQUE/sources/archive).
Le témoin du Journal officiel (décrets de soumission, lois promulguées) et le témoin de l'Assemblée nationale (dépôts au
titre de l'art. 11) ont été exécutés hors de ce script (test_decisif/referendum/) ; leurs résultats sont repris ici,
identifiants compris, et le script vérifie qu'ils correspondent toujours au registre.

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  R1  registre : 9 proclamations ; oui + non = exprimés ; exprimés <= votants <= inscrits ; décret de soumission lu dans
      le visa de chaque proclamation ;
  R2  concordance avec le témoin JO, scrutin par scrutin : décret à la date du visa, loi promulguée si et seulement si
      le texte est adopté ;
  R3  RIP : chaque saisine a sa solution ; chaque non-conformité cite la condition de l'art. 45-2 non remplie ; la
      seule conformité porte la déclaration des soutiens (lus, pas recalculés) ; soutiens < seuil ;
  R4  citations : chaque passage entre guillemets de la page qui vient de la Constitution est retrouvé mot pour mot dans
      l'article archivé ; chaque motif cité d'une décision, dans le texte de la décision ;
  R5  phrases : « le dernier date du » exige le maximum du registre ; « aucune n'a été soumise » exige zéro ; la date
      d'arrêté figure dans toute phrase qui compte.
Autotest de mutation à chaque exécution : proclamation retirée (R2), oui/non permutés (R2), voix ajoutée (R1),
citation altérée (R4), soutiens au seuil (R5).

Écrit : data/promesses_referendum.json (+ static/), static/promesses_referendum.csv (UTF-8 BOM, format long),
data/figures_referendum.json, static/img/referendum-registre(-en).svg/.png, static/img/referendum-rip(-en).svg/.png.
Rien n'est écrit à données identiques. Sortie console ASCII.
"""
from __future__ import annotations

import copy
import csv
import glob
import hashlib
import html
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRO = ROOT.parents[1]
CONSTIT = PRO / "06_PROMOTION" / "RECHERCHE_DOSSIER_PROMESSES_2026-10-05" / "sondes" / "referendum" / "constit"
ARCHIVE = PRO / "02_FABRIQUE" / "sources" / "archive"
sys.path.insert(0, str(ROOT / "scripts" / "sources_promesses_en"))
import constitution_en as cen  # noqa: E402

ARRETE = "2026-10-05"
PAGE_URL = "stephane-lalut.com/un-president-peut-il-recourir-au-referendum/"
PAGE_URL_EN = "stephane-lalut.com/en/can-the-french-president-call-a-referendum/"
OUT_DATA = ROOT / "data" / "promesses_referendum.json"
OUT_STATIC = ROOT / "static" / "promesses_referendum.json"
OUT_CSV = ROOT / "static" / "promesses_referendum.csv"
OUT_FIGURES = ROOT / "data" / "figures_referendum.json"
OUT_IMG = ROOT / "static" / "img"
ARTICLES = {  # numéro -> (LEGIARTI, archive `sources`)
    "3": ("LEGIARTI000019240995", "2026-10/2b5639c959fce37006de2d076ddd81a76e9d7599c4d9e9cab4ad35deb29ecc50.json"),
    "11": ("LEGIARTI000019241004", "2026-09/e4718a1b13a755204ea409d81c5025811a2bfb29fb5e6fae0bc10a87d19367d8.json"),
    "60": ("LEGIARTI000006527548", "2026-10/71b380ebc25814f0688b85855d579f19d6f05d7193d05b00ad8bc7d3881f0c9e.json"),
    "89": ("LEGIARTI000019240655", "2026-10/0caaf2457602bce55a86b6825cd567e7bca2a4a2d82794135566b840d7c58eee.json"),
}
# Citations de la page (clé -> article, texte français, texte anglais de la traduction du Conseil constitutionnel).
CIT = {
    "art3": ("3", "La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum.",
             "National sovereignty shall vest in the people, who shall exercise it through their representatives and by means of referendum."),
    "art11_1": ("11", "sur proposition du Gouvernement pendant la durée des sessions ou sur proposition conjointe des deux assemblées",
                "on a recommendation from the Government when Parliament is in session, or on a joint motion of the two Houses"),
    "art11_objet": ("11", "portant sur l'organisation des pouvoirs publics, sur des réformes relatives à la politique économique, sociale ou environnementale de la nation et aux services publics qui y concourent, ou tendant à autoriser la ratification d'un traité qui, sans être contraire à la Constitution, aurait des incidences sur le fonctionnement des institutions",
                    "which deals with the organization of the public authorities, or with reforms relating to the economic, social or environmental policy of the Nation, and to the public services contributing thereto, or which provides for authorization to ratify a treaty which, although not contrary to the Constitution, would affect the functioning of the institutions"),
    "art11_rip": ("11", "à l'initiative d'un cinquième des membres du Parlement, soutenue par un dixième des électeurs inscrits sur les listes électorales",
                  "upon the initiative of one fifth of the members of Parliament, supported by one tenth of the voters enrolled on the electoral lists"),
    "art11_soumet": ("11", "le Président de la République la soumet au référendum",
                     "the President of the Republic may submit it to a referendum"),
    "art89_voies": ("89", "le projet de révision n'est pas présenté au référendum lorsque le Président de la République décide de le soumettre au Parlement convoqué en Congrès",
                    "a Government Bill to amend the Constitution shall not be submitted to referendum where the President of the Republic decides to submit it to Parliament convened in Congress"),
    "art60": ("60", "Il en proclame les résultats.", "shall proclaim the results of the referendum"),
}
# Témoin du JO (test_decisif/referendum/temoin_jo.py, 06/10/2026) : date du scrutin -> décret (date, JORFTEXT), loi.
TEMOIN_JO = {
    "1961-01-08": ("1960-12-08", "JORFTEXT000000852818", "61-44", "JORFTEXT000000314906"),
    "1962-04-08": ("1962-03-20", "JORFTEXT000000496969", "62-421", "JORFTEXT000000509045"),
    "1962-10-28": (None, None, "62-1292", "JORFTEXT000000684037"),
    "1969-04-27": ("1969-04-02", "JORFTEXT000000499637", None, None),
    "1972-04-23": ("1972-04-05", "JORFTEXT000000513770", "72-339", "JORFTEXT000000684055"),
    "1988-11-06": ("1988-10-05", "JORFTEXT000000872797", "88-1028", "JORFTEXT000000687687"),
    "1992-09-20": ("1992-07-01", "JORFTEXT000000504610", "92-1017", "JORFTEXT000000726005"),
    "2000-09-24": ("2000-07-12", "JORFTEXT000000766148", "2000-964", "JORFTEXT000000219201"),
    "2005-05-29": ("2005-03-09", "JORFTEXT000000627571", None, None),
}
# Objet de chaque scrutin, en mots de la page (titres de la proclamation, du décret ou de la loi au JO).
OBJET = {
    "1961-01-08": ("Autodétermination des populations algériennes", "Self-determination of the Algerian populations"),
    "1962-04-08": ("Accords d'Évian sur l'Algérie", "Évian agreements on Algeria"),
    "1962-10-28": ("Élection du président de la République au suffrage universel", "Election of the President by universal suffrage"),
    "1969-04-27": ("Création de régions et rénovation du Sénat", "Creation of regions and reform of the Senate"),
    "1972-04-23": ("Élargissement de la Communauté européenne", "Enlargement of the European Community"),
    "1988-11-06": ("Statut de la Nouvelle-Calédonie et autodétermination en 1998", "Status of New Caledonia and self-determination in 1998"),
    "1992-09-20": ("Ratification du traité sur l'Union européenne (Maastricht)", "Ratification of the Treaty on European Union (Maastricht)"),
    "2000-09-24": ("Durée du mandat du président de la République (quinquennat)", "Length of the presidential term (five years)"),
    "2005-05-29": ("Ratification du traité établissant une Constitution pour l'Europe", "Ratification of the Treaty establishing a Constitution for Europe"),
}
# Témoin de l'Assemblée nationale (test_decisif/referendum/test_r_e2.py) : dépôts « en application de l'article 11 »
# sans décision du Conseil (décision de l'auteur, 06/10/2026 : dits au lecteur, sans cause).
DEPOTS_SANS_SAISINE = [
    {"numero": "1749", "legislature": "XVe", "date": "2019-03-06",
     "objet": "mesures d'exception contre les djihadistes français ayant combattu en Irak et en Syrie",
     "objet_en": "exceptional measures against French jihadists who fought in Iraq and Syria"},
    {"numero": "5203", "legislature": "XVe", "date": "2022-04-05",
     "objet": "lutter contre les mauvais traitements envers les animaux",
     "objet_en": "combating the mistreatment of animals"},
]
MOIS = {m: i + 1 for i, m in enumerate("janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split())}
MOIS_FR = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
CHIFFRES_FR = {0: "aucun", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"}
CHIFFRES_EN = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def fr(n: float, dec: int = 0) -> str:
    return ("{:,.%df}" % dec).format(n).replace(",", "\u202f").replace(".", ",")


def date_fr(iso: str) -> str:
    a, m, j = iso.split("-")
    return "%s %s %s" % ("1er" if j == "01" else str(int(j)), MOIS_FR[int(m)], a)


def date_en(iso: str) -> str:
    a, m, j = iso.split("-")
    return "%d %s %s" % (int(j), MOIS_EN[int(m)], a)


def champ(s: str, b: str) -> str:
    m = re.search(rf"<{b}>(.*?)</{b}>", s, re.S)
    return m.group(1) if m else ""


def contenu(s: str) -> str:
    c = re.sub(r"<br\s*/?>", "\n", champ(s, "CONTENU"))
    return re.sub(r"<[^>]+>", "", c).replace("&amp;nbsp;", " ").replace("&nbsp;", " ")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'")).strip()


# ------------------------------------------------------------------ lecture
def charger_constit() -> dict[str, str]:
    if not CONSTIT.is_dir():
        raise Arret("stock CONSTIT absent : %s" % CONSTIT)
    par_id = {}
    for f in sorted(glob.glob(str(CONSTIT / "**" / "*.xml"), recursive=True),
                    key=lambda p: (not Path(p).relative_to(CONSTIT).parts[0].startswith("constit"), p)):
        s = open(f, encoding="utf-8").read()
        par_id[champ(s, "ID")] = s
    return par_id


def jour(txt: str) -> str:
    m = re.search(r"(\d{1,2})(?:er)?\s+(" + "|".join(MOIS) + r")\s+(\d{4})", txt)
    if not m:
        raise Arret("date illisible : %s" % txt[:80])
    return "%s-%02d-%02d" % (m.group(3), MOIS[m.group(2)], int(m.group(1)))


def nombre(lib: str, t: str):
    m = re.search(lib + r"\s*:\s*([\d .\u00a0\u202f]+\d)", t, re.I)
    return int(re.sub(r"\D", "", m.group(1))) if m else None


def registre(par_id: dict) -> list[dict]:
    out = []
    for s in par_id.values():
        if champ(s, "NATURE") != "REF" or not champ(s, "TITRE").startswith("Proclamation des résultats"):
            continue
        c = contenu(s)
        visa = re.search(r"Vu le décret[^;\n]*?décidant de soumettre[^;\n]*", re.sub(r"[ \t]*\n[ \t]*(?=[a-zé])", " ", c))
        v = visa.group(0) if visa else ""
        p = c[c.find("Proclame"):] if "Proclame" in c else c
        out.append({"id": champ(s, "ID"), "numero": champ(s, "NUMERO"), "ecli": champ(s, "ECLI"),
                    "date_decision": champ(s, "DATE_DEC"), "date_scrutin": jour(champ(s, "TITRE")),
                    "decret_date": jour(v) if v else None,
                    "nature": "révision de la Constitution" if "révision de la Constitution" in v else ("projet de loi" if "projet de loi" in v else None),
                    "inscrits": nombre(r"(?:É|E)lecteurs inscrits", p), "votants": nombre("Votants", p),
                    "exprimes": nombre(r"Suffrages exprim(?:é|e)s?", p), "oui": nombre(r"\bOUI\b", p), "non": nombre(r"\bNON\b", p)})
    return sorted(out, key=lambda l: l["date_scrutin"])


def rip(par_id: dict) -> dict:
    rip = [s for s in par_id.values() if champ(s, "NATURE") == "RIP" and champ(s, "DATE_DEC") <= ARRETE]
    sa = {}
    for s in rip:
        num = champ(s, "NUMERO")
        if re.fullmatch(r"\d{4}-\d+", num):
            c = norm(contenu(s))
            cond = sorted(set(re.findall(r"(?:le|au) ([23])° de l.article\s*45-2", c)))
            sa[num] = {"numero": num, "id": champ(s, "ID"), "date": champ(s, "DATE_DEC"), "titre": norm(champ(s, "TITRE")),
                       "solution": champ(s, "SOLUTION"), "condition": cond, "soutiens": None, "seuil": None, "texte": c}
    for s in rip:
        m = re.fullmatch(r"(\d{4}-\d+)-\d+", champ(s, "NUMERO"))
        if m:
            c = norm(contenu(s))
            ns = re.search(r"a recueilli le soutien de ([\d ]+) électeurs", c)
            nm = re.search(r"à recueillir était de ([\d ]+)", c)
            if ns and nm:
                sa[m.group(1)]["soutiens"] = int(ns.group(1).replace(" ", ""))
                sa[m.group(1)]["seuil"] = int(nm.group(1).replace(" ", ""))
                sa[m.group(1)]["declaration"] = champ(s, "NUMERO")
    return dict(sorted(sa.items(), key=lambda kv: kv[1]["date"]))


def article_fr(n: str) -> str:
    leg, rel = ARTICLES[n]
    p = ARCHIVE / rel
    if not p.is_file():
        raise Arret("article %s : archive absente (%s)" % (n, rel))
    d = json.loads(p.read_text(encoding="utf-8"))
    a = d.get("article") or d.get("contenu") or d
    if a.get("id") != leg:
        raise Arret("article %s : l'archive porte %s, attendu %s" % (n, a.get("id"), leg))
    return norm(a["texte"])


# ------------------------------------------------------------------ gardes
def gardes(R: list[dict], S: dict) -> list[str]:
    g = []
    if len(R) != 9:
        raise Arret("R1 : %d proclamations, 9 attendues (le registre a changé : relire la fiche)" % len(R))
    for l in R:
        if None in (l["inscrits"], l["votants"], l["exprimes"], l["oui"], l["non"], l["decret_date"], l["nature"]):
            raise Arret("R1 : %s, donnée illisible" % l["date_scrutin"])
        if l["oui"] + l["non"] != l["exprimes"] or not (l["exprimes"] <= l["votants"] <= l["inscrits"]):
            raise Arret("R1 : %s, incohérence des nombres de voix" % l["date_scrutin"])
    g.append("R1 : 9 proclamations, nombres cohérents, décret lu dans chaque visa")
    if set(TEMOIN_JO) != {l["date_scrutin"] for l in R}:
        raise Arret("R2 : le registre et le témoin JO ne portent pas les mêmes scrutins")
    for l in R:
        dd, _, loi, _ = TEMOIN_JO[l["date_scrutin"]]
        if dd and dd != l["decret_date"]:
            raise Arret("R2 : %s, décret du %s au JO, du %s dans le visa" % (l["date_scrutin"], dd, l["decret_date"]))
        if (l["oui"] > l["non"]) != (loi is not None):
            raise Arret("R2 : %s, issue contredite par le JO" % l["date_scrutin"])
    g.append("R2 : témoin JO concordant (décret indéterminé au témoin : 1962-10-28)")
    for n, s in S.items():
        if s["solution"] == "Conformité":
            if s["soutiens"] is None:
                raise Arret("R3 : %s conforme sans déclaration des soutiens" % n)
        elif not s["condition"]:
            raise Arret("R3 : %s non conforme sans condition de l'art. 45-2 citée" % n)
    g.append("R3 : %d saisines, solutions et conditions lues" % len(S))
    return g


def verifier_citations(textes: dict, motifs: dict, S: dict) -> list[str]:
    for k, (n, f, e) in CIT.items():
        if norm(f) not in textes[n]:
            raise Arret("R4 : citation %s introuvable dans l'art. %s" % (k, n))
        if e:
            try:
                cen.citer(n, e)
            except ValueError as exc:
                raise Arret("R4 : citation anglaise %s : %s" % (k, exc))
    for num, m in motifs.items():
        if norm(m) not in S[num]["texte"]:
            raise Arret("R4 : motif cité de la décision %s introuvable" % num)
    return ["R4 : %d citations de la Constitution et %d motifs retrouvés mot pour mot" % (len(CIT), len(motifs))]


# Décision n° 2007-560 DC (traité de Lisbonne), citée par la page : (citation, numéro).
CIT_2007_560 = ("ne peut intervenir qu'après révision de la Constitution", "2007-560")


def verifier_2007_560(par_id: dict) -> str:
    s = next((s for s in par_id.values() if champ(s, "NUMERO") == CIT_2007_560[1] and champ(s, "NATURE") == "DC"), None)
    if not s or CIT_2007_560[0] not in norm(contenu(s)):
        raise Arret("R4 : citation de la décision %s DC introuvable" % CIT_2007_560[1])
    return "R4 : décision %s DC (%s) citée mot pour mot" % (CIT_2007_560[1], champ(s, "DATE_DEC"))


# Motifs cités, mot pour mot, de chaque non-conformité (R-E2 : jamais une catégorie maison).
MOTIFS = {
    "2021-2": "sont contraires à la Constitution",
    "2022-3": "ne porte sur aucun des autres objets mentionnés au premier alinéa de l'article 11 de la Constitution",
    "2023-4": "elle ne porte pas, au sens de l'article 11 de la Constitution, sur une « réforme » relative à la politique sociale",
    "2023-5": "la proposition de loi ne porte pas, au sens de l'article 11 de la Constitution, sur une réforme relative à la politique sociale",
    "2024-6": "portent une atteinte disproportionnée à ces exigences",
    "2026-7": "la proposition de loi ne porte pas non plus sur une « réforme » au sens de l'article 11 de la Constitution",
}
MOTIFS_COURTS = {  # en mots de la page, une ligne par décision ; la citation exacte est dans MOTIFS
    "2021-2": ("une disposition contraire à la Constitution (3° de l'art. 45-2)", "a provision contrary to the Constitution (art. 45-2, 3°)"),
    "2022-3": ("pas d'objet visé par l'article 11 (2°)", "no subject covered by article 11 (2°)"),
    "2023-4": ("pas une « réforme » au sens de l'article 11 (2°)", "not a 'reform' within the meaning of article 11 (2°)"),
    "2023-5": ("pas une « réforme » au sens de l'article 11 (2°)", "not a 'reform' within the meaning of article 11 (2°)"),
    "2024-6": ("une disposition contraire à la Constitution (3°)", "a provision contrary to the Constitution (3°)"),
    "2026-7": ("pas une « réforme » au sens de l'article 11 (2°)", "not a 'reform' within the meaning of article 11 (2°)"),
}
OBJET_RIP = {
    "2019-1": ("Aérodromes de Paris, service public national", "Paris airports as a national public service"),
    "2021-2": ("Service public hospitalier (loi de programmation)", "Public hospital service (programming act)"),
    "2022-3": ("Contribution sur les bénéfices exceptionnels des grandes entreprises", "Contribution on large companies' windfall profits"),
    "2023-4": ("Âge légal de départ à la retraite : pas au-delà de 62 ans", "Legal retirement age: not above 62"),
    "2023-5": ("Âge légal de départ à la retraite : pas au-delà de 62 ans (seconde proposition)", "Legal retirement age: not above 62 (second bill)"),
    "2024-6": ("Accès des étrangers aux prestations sociales", "Foreigners' access to social benefits"),
    "2026-7": ("Exclure de la notion de soin la provocation active de la mort", "Excluding the active causing of death from the notion of care"),
}


def resultat(R: list[dict], S: dict, arrete: str = ARRETE) -> dict:
    vals = [l for l in R if "1958-10-04" <= l["date_scrutin"] <= arrete]
    ad = [l for l in vals if l["oui"] > l["non"]]
    conf = [s for s in S.values() if s["solution"] == "Conformité"]
    return {"N": len(vals), "A": len(ad), "R": len(vals) - len(ad), "dernier": max(l["date_scrutin"] for l in vals),
            "art89": sum(1 for l in vals if l["nature"] == "révision de la Constitution"),
            "S": len(S), "C": len(conf), "reunis": sum(1 for s in conf if s["soutiens"] >= s["seuil"]),
            "cond2": sum(1 for s in S.values() if s["condition"] == ["2"]),
            "cond3": sum(1 for s in S.values() if s["condition"] == ["3"]),
            "rejetes": sorted(l["date_scrutin"] for l in vals if l["oui"] <= l["non"])}


def phrases(r: dict) -> None:
    """R5 : les phrases de la page, recalculées ; une donnée qui les dément arrête."""
    if r["reunis"] != 0:
        raise Arret("R5 : « aucune n'a réuni le soutien requis » démenti")
    if r["C"] != 1:
        raise Arret("R5 : « une a été jugée conforme » démenti (%d)" % r["C"])
    if r["A"] + r["R"] != r["N"] or r["R"] < 1:
        raise Arret("R5 : comptes adoptés / rejetés incohérents")
    if r.get("rejetes") != ["1969-04-27", "2005-05-29"]:
        raise Arret("R5 : la page nomme les rejets de 1969 et 2005 ; le registre dit %s" % r.get("rejetes"))


# ------------------------------------------------------------------ affichage
def affichage(R, S, r) -> tuple[dict, dict]:
    conf = next(s for s in S.values() if s["solution"] == "Conformité")
    d = {l["date_scrutin"]: l for l in R}
    part = lambda l: 100 * l["votants"] / l["inscrits"]  # noqa: E731
    A = {"N": CHIFFRES_FR[r["N"]], "N_chiffre": str(r["N"]), "A": CHIFFRES_FR[r["A"]], "R": CHIFFRES_FR[r["R"]],
         "dernier": date_fr(r["dernier"]), "arrete": date_fr(ARRETE), "annees_depuis": str(int(ARRETE[:4]) - int(r["dernier"][:4])),
         "S": "une" if r["S"] == 1 else CHIFFRES_FR[r["S"]],
         "C": "une" if r["C"] == 1 else CHIFFRES_FR[r["C"]], "cond2": CHIFFRES_FR[r["cond2"]], "cond3": CHIFFRES_FR[r["cond3"]],
         "soutiens": fr(conf["soutiens"]), "seuil": fr(conf["seuil"]), "part_seuil": fr(100 * conf["soutiens"] / conf["seuil"], 0),
         "rip_conf_date": date_fr(conf["date"]), "rip_depuis": "2015",
         "part_2005": fr(part(d["2005-05-29"]), 1), "non_2005": fr(100 * d["2005-05-29"]["non"] / d["2005-05-29"]["exprimes"], 2),
         "part_2000": fr(part(d["2000-09-24"]), 1), "part_1988": fr(part(d["1988-11-06"]), 1),
         "part_max": fr(max(part(l) for l in R), 1), "part_min": fr(min(part(l) for l in R), 1),
         "oui_1992": fr(100 * d["1992-09-20"]["oui"] / d["1992-09-20"]["exprimes"], 2),
         "non_1969": fr(100 * d["1969-04-27"]["non"] / d["1969-04-27"]["exprimes"], 2),
         "depots_sans_saisine": "deux" if len(DEPOTS_SANS_SAISINE) == 2 else str(len(DEPOTS_SANS_SAISINE)),
         "n_loi": CHIFFRES_FR[r["N"] - r["art89"]].capitalize(), "n_rev": "un seul" if r["art89"] == 1 else CHIFFRES_FR[r["art89"]],
         "part_min_an": min(R, key=part)["date_scrutin"][:4], "part_max_an": max(R, key=part)["date_scrutin"][:4],
         "non_conformes": CHIFFRES_FR[r["S"] - r["C"]], "cond2_maj": CHIFFRES_FR[r["cond2"]].capitalize(),
         "cond3_maj": CHIFFRES_FR[r["cond3"]].capitalize(),
         "cit_motif_2023_4": MOTIFS["2023-4"].replace("elle ne porte", "ne porte"), "cit_2007_560": CIT_2007_560[0]}
    E = {"N": CHIFFRES_EN[r["N"]], "N_chiffre": str(r["N"]), "A": CHIFFRES_EN[r["A"]], "R": CHIFFRES_EN[r["R"]],
         "dernier": date_en(r["dernier"]), "arrete": date_en(ARRETE), "annees_depuis": str(int(ARRETE[:4]) - int(r["dernier"][:4])),
         "S": CHIFFRES_EN[r["S"]], "C": CHIFFRES_EN[r["C"]], "cond2": CHIFFRES_EN[r["cond2"]], "cond3": CHIFFRES_EN[r["cond3"]],
         "soutiens": "{:,}".format(conf["soutiens"]), "seuil": "{:,}".format(conf["seuil"]),
         "part_seuil": "%.0f" % (100 * conf["soutiens"] / conf["seuil"]),
         "rip_conf_date": date_en(conf["date"]), "rip_depuis": "2015",
         "part_2005": "%.1f" % part(d["2005-05-29"]), "non_2005": "%.2f" % (100 * d["2005-05-29"]["non"] / d["2005-05-29"]["exprimes"]),
         "part_2000": "%.1f" % part(d["2000-09-24"]), "part_1988": "%.1f" % part(d["1988-11-06"]),
         "part_max": "%.1f" % max(part(l) for l in R), "part_min": "%.1f" % min(part(l) for l in R),
         "oui_1992": "%.2f" % (100 * d["1992-09-20"]["oui"] / d["1992-09-20"]["exprimes"]),
         "non_1969": "%.2f" % (100 * d["1969-04-27"]["non"] / d["1969-04-27"]["exprimes"]),
         "depots_sans_saisine": "two" if len(DEPOTS_SANS_SAISINE) == 2 else str(len(DEPOTS_SANS_SAISINE)),
         "n_loi": CHIFFRES_EN[r["N"] - r["art89"]].capitalize(), "n_rev": "only one" if r["art89"] == 1 else CHIFFRES_EN[r["art89"]],
         "part_min_an": min(R, key=part)["date_scrutin"][:4], "part_max_an": max(R, key=part)["date_scrutin"][:4],
         "non_conformes": CHIFFRES_EN[r["S"] - r["C"]], "cond2_maj": CHIFFRES_EN[r["cond2"]].capitalize(),
         "cond3_maj": CHIFFRES_EN[r["cond3"]].capitalize(),
         # décisions françaises : citées en français sur la page anglaise, suivies de « our translation »
         "cit_motif_2023_4": MOTIFS["2023-4"].replace("elle ne porte", "ne porte"), "cit_2007_560": CIT_2007_560[0]}
    for k, (n, f, e) in CIT.items():  # sans traduction vérifiée, la clé anglaise reste vide : la page anglaise ne cite pas
        A["cit_" + k] = f
        E["cit_" + k] = e or ""
    return A, E


def tableaux(R, S) -> tuple[dict, dict]:
    t, te = {}, {}
    lignes, lignes_en = [], []
    for l in R:
        _, _, loi, _ = TEMOIN_JO[l["date_scrutin"]]
        o, oe = OBJET[l["date_scrutin"]]
        part = 100 * l["votants"] / l["inscrits"]
        oui = 100 * l["oui"] / l["exprimes"]
        art = "89" if l["nature"] == "révision de la Constitution" else "11"
        lignes.append([date_fr(l["date_scrutin"]), o, art, fr(l["inscrits"]), fr(part, 1) + " %", fr(oui, 2) + " %",
                       ("Adopté (loi n° %s)" % loi) if l["oui"] > l["non"] else "Rejeté"])
        lignes_en.append([date_en(l["date_scrutin"]), oe, art, "{:,}".format(l["inscrits"]), "%.1f%%" % part, "%.2f%%" % oui,
                          ("Adopted (Act No. %s)" % loi) if l["oui"] > l["non"] else "Rejected"])
    t["registre"] = {"entetes": ["Scrutin", "Objet", "Article", "Inscrits", "Participation", "Oui (exprimés)", "Issue"], "lignes": lignes}
    te["registre"] = {"entetes": ["Vote", "Subject", "Article", "Registered voters", "Turnout", "Yes (valid votes)", "Outcome"], "lignes": lignes_en}
    lr, lre = [], []
    for n, s in S.items():
        o, oe = OBJET_RIP[n]
        if s["solution"] == "Conformité":
            issue = "Conforme ; %s soutiens pour %s requis" % (fr(s["soutiens"]), fr(s["seuil"]))
            issue_en = "Valid; %s signatures of support for %s required" % ("{:,}".format(s["soutiens"]), "{:,}".format(s["seuil"]))
        else:
            issue, issue_en = ("Non conforme : " + MOTIFS_COURTS[n][0]), ("Not valid: " + MOTIFS_COURTS[n][1])
        lr.append([date_fr(s["date"]), "%s RIP" % n, o, issue])
        lre.append([date_en(s["date"]), "%s RIP" % n, oe, issue_en])
    t["rip"] = {"entetes": ["Décision", "Numéro", "Proposition de loi", "Solution"], "lignes": lr}
    te["rip"] = {"entetes": ["Decision", "Number", "Private Members' Bill", "Outcome"], "lignes": lre}
    return t, te


# ------------------------------------------------------------------ figures
W = 720
BLEU, GRIS, GRIS_CLAIR = "#184f95", "#8a8f98", "#c9cdd3"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LANG = "fr"


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def cadre(H, ident, titre, sous, desc):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H + 48, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def cartouche(H, src, note):
    out = ['<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (H + 2, W, H + 2, GRID)]
    for k, (t, c) in enumerate(((src, INK2), (note, INK2), (LICENCES[LANG], MUTED))):
        out.append('<text x="0" y="%d" font-size="9" fill="%s">%s</text>' % (H + 15 + 12 * k, c, esc(t)))
    return out


T = {
    "fr": {"t1": "Les référendums nationaux depuis 1958", "s1": "date du scrutin et part des « oui » parmi les suffrages exprimés, arrêté au {arrete}",
           "d1": "Frise de 1958 à 2026 portant {N} référendums nationaux : {A} adoptés et {R} rejetés (1969 et 2005) ; aucun scrutin depuis le {dernier}.",
           "src1": "Conseil constitutionnel, proclamations des résultats (stock CONSTIT de la DILA, arrêté au 05/10/2026) ; Journal officiel",
           "note1": "Référendums nationaux des art. 11 et 89 seulement ; hors scrutin du 28/09/1958 et consultations locales.",
           "adopte": "adopté", "rejete": "rejeté", "aucun": "aucun référendum depuis {annees_depuis} ans",
           "moitie": "50 % des exprimés",
           "t2": "Le référendum d'initiative partagée, de 2015 au {arrete}", "s2": "propositions de loi soumises au Conseil constitutionnel, et ce qu'elles sont devenues",
           "d2": "{S} saisines du Conseil constitutionnel ; {C} conforme ; {soutiens} soutiens recueillis pour {seuil} requis ; aucun référendum.",
           "src2": "Conseil constitutionnel, décisions « RIP » (stock CONSTIT, arrêté au 05/10/2026) ; Constitution, art. 11",
           "note2": "Deux autres propositions déposées à l'Assemblée « en application de l'article 11 » n'ont fait l'objet d'aucune décision.",
           "e1": "Saisines du Conseil", "e2": "Jugées conformes", "e3": "Soutien d'un dixième des inscrits réuni", "e4": "Soumises au référendum",
           "sout": "Soutiens recueillis : {soutiens}", "seuil": "Seuil : {seuil} (un dixième des inscrits)"},
    "en": {"t1": "National referendums in France since 1958", "s1": "date of the vote and share of 'yes' among valid votes, as at {arrete}",
           "d1": "Timeline from 1958 to 2026 with {N} national referendums: {A} adopted and {R} rejected (1969 and 2005); no vote since {dernier}.",
           "src1": "Conseil constitutionnel, proclamations of results (DILA CONSTIT database, as at 5 Oct. 2026); Journal officiel",
           "note1": "National referendums under articles 11 and 89 only; excludes the vote of 28 Sept. 1958 and local consultations.",
           "adopte": "adopted", "rejete": "rejected", "aucun": "no referendum for {annees_depuis} years",
           "moitie": "50% of valid votes",
           "t2": "The shared-initiative referendum, 2015 to {arrete}", "s2": "Private Members' Bills referred to the Conseil constitutionnel, and what became of them",
           "d2": "{S} referrals to the Conseil constitutionnel; {C} valid; {soutiens} signatures of support for {seuil} required; no referendum.",
           "src2": "Conseil constitutionnel, 'RIP' decisions (DILA CONSTIT database, as at 5 Oct. 2026); Constitution, art. 11",
           "note2": "Two other bills tabled in the National Assembly 'under article 11' gave rise to no decision.",
           "e1": "Referrals", "e2": "Found valid", "e3": "One tenth of voters' support reached", "e4": "Put to a referendum",
           "sout": "Signatures collected: {soutiens}", "seuil": "Threshold: {seuil} (one tenth of registered voters)"},
}


def fig_registre(R, A):
    H = 262
    L = T[LANG]
    e = cadre(H, "rr", L["t1"], L["s1"].format(**A), L["d1"].format(**A))
    x0, x1 = 20, W - 20
    a0, a1 = 1958, int(ARRETE[:4]) + 1
    X = lambda y: x0 + (y - a0) / (a1 - a0) * (x1 - x0)  # noqa: E731
    yb, hmax = 230, 150  # base et hauteur pour 100 % de oui
    Y = lambda p: yb - p / 100 * hmax  # noqa: E731
    e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (x0, yb, x1, yb, INK2))
    e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-dasharray="3 3"/>' % (x0, Y(50), x1, Y(50), GRIS))
    e.append(txt(X(1976), Y(50) - 4, L["moitie"], 9, MUTED, "start"))  # zone sans scrutin (1973-1987)
    for an in range(1960, a1, 10):
        e.append(txt(X(an), yb + 16, str(an), 10, MUTED, "middle"))
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(an), yb, X(an), yb + 4, INK2))
    dernier = max(l["date_scrutin"] for l in R)
    xd = X(int(dernier[:4]) + (int(dernier[5:7]) - 0.5) / 12)
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity="0.35"/>' % (xd + 6, yb - hmax, x1 - xd - 6, hmax, GRID))
    e.append(txt((xd + x1) / 2, yb - hmax + 22, L["aucun"].format(**A), 11, INK2, "middle", "600"))
    prec = None
    for l in R:
        an = int(l["date_scrutin"][:4]) + (int(l["date_scrutin"][5:7]) - 0.5) / 12
        p = 100 * l["oui"] / l["exprimes"]
        x = X(an)
        ad = l["oui"] > l["non"]
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="5"/>' % (x, yb, x, Y(p), BLEU if ad else GRIS))
        e.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, Y(p), BLEU if ad else "#ffffff", BLEU if ad else INK2))
        lab = (fr(p, 0) + " %") if LANG == "fr" else "%.0f%%" % p
        # deux scrutins à moins d'un an (1962) : l'étiquette du second passe à droite de sa tige
        proche = prec is not None and an - prec < 1
        e.append(txt(x + (12 if proche else 0), Y(p) + (4 if proche else -10), lab, 9, INK if ad else INK2,
                     "start" if proche else "middle", "600"))
        prec = an
    e.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x0 + 4, 58, BLEU))
    e.append(txt(x0 + 14, 62, L["adopte"], 10, INK2))
    e.append('<circle cx="%d" cy="%d" r="5" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (x0 + 84, 58, INK2))
    e.append(txt(x0 + 94, 62, L["rejete"], 10, INK2))
    e += cartouche(H, L["src1"], L["note1"])
    e.append("</svg>")
    return "\n".join(e)


def fig_rip(S, r, A):
    H = 286
    L = T[LANG]
    e = cadre(H, "rp", L["t2"].format(**A), L["s2"], L["d2"].format(**A))
    etapes = [(L["e1"], r["S"]), (L["e2"], r["C"]), (L["e3"], r["reunis"]), (L["e4"], 0)]
    x0, wmax, y, h = 260, 300, 66, 26
    for k, (nom, v) in enumerate(etapes):
        yy = y + k * (h + 12)
        e.append(txt(x0 - 10, yy + 18, nom, 11, INK2, "end"))
        w = wmax * v / max(1, r["S"])
        if v:
            e.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0, yy, w, h, BLEU))
        else:
            e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (x0, yy, x0, yy + h, INK2))
        e.append(txt(x0 + w + 8, yy + 18, str(v), 13, INK, "start", "600"))
    conf = next(s for s in S.values() if s["solution"] == "Conformité")
    yy = y + 4 * (h + 12) + 8
    ws = wmax * conf["soutiens"] / conf["seuil"]
    e.append('<rect x="%d" y="%d" width="%d" height="12" fill="none" stroke="%s"/>' % (x0, yy, wmax, INK2))
    e.append('<rect x="%d" y="%d" width="%.1f" height="12" fill="%s"/>' % (x0, yy, ws, GRIS))
    e.append(txt(x0 - 10, yy + 10, "2019-1 RIP", 10, INK2, "end"))
    e.append(txt(x0, yy + 28, L["sout"].format(**A), 10, INK, "start", "600"))
    e.append(txt(x0, yy + 42, L["seuil"].format(**A), 10, INK2))
    e += cartouche(H, L["src2"], L["note2"])
    e.append("</svg>")
    return "\n".join(e)


MONTRE = {
    "fr": {"registre": "Du 4 octobre 1958 au {arrete}, {N} référendums nationaux ont été organisés ; {A} ont adopté le texte soumis, {R} l'ont rejeté ; le dernier date du {dernier}.",
           "rip": "De 2015 au {arrete}, le Conseil constitutionnel a été saisi de {S} propositions de loi au titre de l'article 11 ; {C} a été jugée conforme et n'a pas réuni le soutien d'un dixième des électeurs inscrits ; aucune n'a été soumise au référendum."},
    "en": {"registre": "From 4 October 1958 to {arrete}, {N} national referendums were held; {A} adopted the text put to the vote and {R} rejected it; the last one took place on {dernier}.",
           "rip": "From 2015 to {arrete}, the Conseil constitutionnel received {S} Private Members' Bills under article 11; {C} was found valid and did not gather the support of one tenth of registered voters; none was put to a referendum."},
}


def fiches(figs, A, E):
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", E)):
        out = []
        for ident, fichier in (("registre", "referendum-registre"), ("rip", "referendum-rip")):
            svg = figs[fichier + suf + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
            if len(cart) != 3 or cart[-1] != LICENCES[lang]:
                raise Arret("fiche %s%s : cartouche illisible" % (fichier, suf))
            out.append(dict(id=ident, fichier=fichier + suf, titre=titre, montre=MONTRE[lang][ident].format(**AA),
                            source=cart[0], precaution=cart[1]))
        res[lang] = out
    return res


def csv_texte(R, S) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "identifiant", "date", "objet", "article", "variable", "valeur", "source"])
    for l in R:
        for k in ("inscrits", "votants", "exprimes", "oui", "non"):
            w.writerow(["referendum_national", l["numero"], l["date_scrutin"], OBJET[l["date_scrutin"]][0],
                        "89" if l["nature"] == "révision de la Constitution" else "11", k, l[k],
                        "Conseil constitutionnel, proclamation %s (%s)" % (l["numero"], l["ecli"])])
    for n, s in S.items():
        w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "solution", s["solution"], "Conseil constitutionnel, décision %s RIP" % n])
        if s["soutiens"] is not None:
            w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "soutiens", s["soutiens"], "décision %s RIP" % s.get("declaration")])
            w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "seuil", s["seuil"], "décision %s RIP" % s.get("declaration")])
    for d in DEPOTS_SANS_SAISINE:
        w.writerow(["depot_art11_sans_saisine", "AN %s %s" % (d["legislature"], d["numero"]), d["date"], d["objet"], "11 al. 3",
                    "decision_du_conseil", "aucune", "Assemblée nationale, données ouvertes"])
    return buf.getvalue()


def autotest(R, S, textes):
    out = []
    essais = [("proclamation retirée", lambda R, S, t: (R[1:], S, t), "R1"),
              ("oui/non permutés (1969)", lambda R, S, t: ([dict(l, oui=l["non"], non=l["oui"]) if l["date_scrutin"] == "1969-04-27" else l for l in R], S, t), "R2"),
              ("voix ajoutée", lambda R, S, t: ([dict(l, oui=l["oui"] + 1) if l["date_scrutin"] == "1961-01-08" else l for l in R], S, t), "R1"),
              ("citation altérée", lambda R, S, t: (R, S, dict(t, **{"11": t["11"].replace("un dixième", "un cinquième")})), "R4"),
              ("soutiens au seuil", lambda R, S, t: (R, {k: (dict(v, soutiens=v["seuil"]) if v["solution"] == "Conformité" else v) for k, v in S.items()}, t), "R5")]
    for nom, mut, pref in essais:
        R2, S2, t2 = mut(copy.deepcopy(R), copy.deepcopy(S), dict(textes))
        try:
            gardes(R2, S2)
            verifier_citations(t2, MOTIFS, S2)
            phrases(resultat(R2, S2))
            raise Arret("mutation %s : aucune garde n'a mordu, contrôle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith(pref):
                raise
            out.append("%s -> %s" % (nom, str(e)[:60]))
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def _main() -> int:
    check = "--check" in sys.argv[1:]
    par_id = charger_constit()
    R, S = registre(par_id), rip(par_id)
    textes = {n: article_fr(n) for n in ARTICLES}
    g = gardes(R, S)
    g += verifier_citations(textes, MOTIFS, S)
    g.append(verifier_2007_560(par_id))
    r = resultat(R, S)
    phrases(r)
    g.append("R5 : phrases recalculées (N=%d, A=%d, R=%d, S=%d, C=%d, soutiens réunis=%d)" % (r["N"], r["A"], r["R"], r["S"], r["C"], r["reunis"]))
    for m in autotest(R, S, textes):
        log("autotest : la mutation a mordu : " + m)
    A, E = affichage(R, S, r)
    if set(A) != set(E):
        raise Arret("blocs affichage et affichage_en : clés différentes (%s)" % sorted(set(A) ^ set(E)))
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    try:
        import cairosvg
    except ImportError:
        raise Arret("cairosvg absent : SVG et PNG ensemble ou pas du tout")
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", E)):
        figs["referendum-registre%s.svg" % suf] = fig_registre(R, AA)
        figs["referendum-rip%s.svg" % suf] = fig_rip(S, r, AA)
    LANG = "fr"
    fi = fiches(figs, A, E)
    t, te = tableaux(R, S)
    csvt = csv_texte(R, S)
    payload = {
        "releve_le": ARRETE,
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Conseil constitutionnel (DILA, CONSTIT), Journal officiel, Assemblée nationale",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve, prolongement R (R-E1, R-E2)",
                 "arrete": ARRETE, "constitution": {n: {"legiarti": v[0], "archive": v[1]} for n, v in ARTICLES.items()},
                 "temoin_jo": TEMOIN_JO, "depots_sans_saisine": DEPOTS_SANS_SAISINE,
                 "hors_champ": "référendum du 28/09/1958 (antérieur au Conseil constitutionnel) ; consultations locales (art. 72-1, 72-4, 73, 76, 77)"},
        "gardes": g, "calcul": r,
        "registre": [{k: v for k, v in l.items()} for l in R],
        "rip": {n: {k: v for k, v in s.items() if k != "texte"} for n, s in S.items()},
        "motifs_cites": MOTIFS,
        "tableaux": t, "tableaux_en": te,
        "affichage": dict(A, releve_le=date_fr(ARRETE) + " (registre du Conseil constitutionnel, stock DILA arrêté à cette date)"),
        "affichage_en": dict(E, releve_le=date_en(ARRETE) + " (Conseil constitutionnel register, DILA database as at that date)"),
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    same = (OUT_DATA.exists() and OUT_DATA.read_text(encoding="utf-8") == txt_json and OUT_CSV.exists()
            and OUT_CSV.read_text(encoding="utf-8-sig") == csvt
            and all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s for n, s in figs.items())
            and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fi)
    if same:
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
    log("Ecrit : data/promesses_referendum.json, static/promesses_referendum.{json,csv}, data/figures_referendum.json, 4 figures SVG + PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
