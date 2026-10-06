#!/usr/bin/env python3
"""Volet « Appliquer » du dossier Promesses : une loi votée, les mesures qu'elle appelle, et les taux publiés.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 3 (v2, gelée au commit
dfd0ec9 ; arbitrage PRO-20261005-164029). Test décisif du 06/10/2026 : test_decisif/appliquer/VERDICT.md (registre de
concordance loi par loi, 17 mutations) ; recalcul indépendant des comptes du baromètre par un second code, concordant.
  E1 — lois sans mesure réglementaire d'application, sessions 2017-2018 à 2024-2025, bornes [D/N ; (D+U)/N] ;
       « moins de la moitié » seulement si 2(D+U) < N dans CHAQUE session (sinon : valeurs par session).
  E2 — état des mesures au jour du relevé (repli : le baromètre ne publie que l'état courant).
  E3 — définitions avant taux : Sénat et Gouvernement, même session ; série longue du Sénat par segments.

Sources (scripts/sources_appliquer/, constituées par extraire_sources.py) : extraits bruts du baromètre de
l'application des lois (Assemblée nationale, LexImpact ; données DILA) ; texte des pages citées des rapports du Sénat,
avec l'empreinte de chaque document ; registre de concordance ; extrait du bilan SGG au 31/12/2025 ; code civil, art. 1
(Légifrance).

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  A1  code civil, art. 1 : en vigueur, phrase du report d'entrée en vigueur retrouvée mot pour mot ;
  A2  champ : lois de l'extrait = lois retenues + conventions écartées, par session ; registre = champ, loi par loi ;
  A3  « directe » du baromètre recalculée = registre ; effectifs du Sénat = effectifs annoncés par ses annexes (2017-2024)
      et par ses commissions (2024-2025, dont la somme = « 22 d'entre elles », p. 45) ;
  A4  phrase générale : écrite seulement si 2(D+U) < N partout ; la page dit qu'elle ne tient pas, donc il faut une
      session où 2(D+U) >= N, et le baromètre seul doit y dépasser la moitié (phrase de la page) ;
  A5  mesures : N = P + A + S + U par session ; cohérence avec le fichier des lois du même producteur (mesures à
      appliquer = appliquées + en attente ; appliquées = appliquées), loi par loi ;
  A6  cas témoin 2025-138 : « sans objet » au baromètre avec l'observation d'un arrêté, mesure « en attente » au SGG ;
  A7  citations des rapports du Sénat et du SGG retrouvées mot pour mot dans la page archivée ; chaque valeur publiée
      retrouvée dans sa citation ; Sénat et SGG publient des taux différents pour la même session (phrase de la page).
Autotest de mutation à chaque exécution : loi appliquée après décret reclassée « directe » -> A3 ; une convention
réintégrée au champ -> A2 ; une mesure « appliquée » passée « en attente » -> A5 ; citation du Sénat altérée -> A7 ;
2018-2019 ramenée sous la moitié -> A4.

Bilingue (06/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés, deux jeux de tableaux, des figures
-en au même dessin ; la Constitution se cite en anglais dans la traduction du Conseil constitutionnel (vérifiée, garde A1) ;
les autres textes français en français, suivis de notre traduction (clés *_tr), dont chaque nombre doit figurer dans
l'original (garde A7 bis).

Écrit : data/promesses_appliquer.json (+ static/), static/promesses_appliquer.csv, data/figures_appliquer.json,
static/img/appliquer-{mesures,lois,serie}.svg/.png. Rien n'est écrit à données identiques.
"""
from __future__ import annotations

import collections
import copy
import csv
import hashlib
import html
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "sources_promesses_en"))
import constitution_en as cen  # noqa: E402
SRC = ROOT / "scripts" / "sources_appliquer"
PAGE_URL = "stephane-lalut.com/une-loi-votee-s-applique-t-elle-tout-de-suite/"
PAGE_URL_EN = "stephane-lalut.com/en/does-a-law-apply-as-soon-as-it-is-passed/"
OUT_DATA = ROOT / "data" / "promesses_appliquer.json"
OUT_STATIC = ROOT / "static" / "promesses_appliquer.json"
OUT_CSV = ROOT / "static" / "promesses_appliquer.csv"
OUT_FIGURES = ROOT / "data" / "figures_appliquer.json"
OUT_IMG = ROOT / "static" / "img"
CCIV = "legifrance_cc0765ea833ba2ee7901764e2b924cd6bebc1122f1273afe63316f12a6604f33.json"
# Du vote à l'entrée en vigueur (contre-expertise PRO-20261006-142218, P8) : promulgation (art. 10), suspendue par la
# saisine du Conseil constitutionnel (art. 61).
CONST = {"art10": "legifrance_09785484a231a183e5290643bbb832eeab7a232b4102ab55206f6b4cfcb2a5bb.json",
         "art61": "legifrance_c14abed78a1e9932d2cf37f84e6366e03847a41174d17466b5f83b4a0a3d299c.json"}
CIT_CONST = {"art10": "Le Président de la République promulgue les lois dans les quinze jours qui suivent la transmission au Gouvernement de la loi définitivement adoptée.",
             "art61": "la saisine du Conseil constitutionnel suspend le délai de promulgation."}
SESSIONS = ["%d-%d" % (a, a + 1) for a in range(2017, 2025)]
RELEVE = "05/10/2026"
MOTS = {"un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
LETTRES = {v: k for k, v in MOTS.items()}
LETTRES_EN = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
CONST_EN = {"art10": ("10", "The President of the Republic shall promulgate Acts of Parliament within fifteen days following the "
                             "final passage of an Act and its transmission to the Government."),
            "art61": ("61", "referral to the Constitutional Council shall suspend the time allotted for promulgation.")}
# Notre traduction des citations françaises hors Constitution ; chaque nombre doit figurer dans l'original (garde A7 bis).
TR = {
    "cit_cciv": "However, the entry into force of those of their provisions whose implementation requires implementing "
                "measures is postponed to the date on which those measures enter into force.",
    "cit_sgg_1718": "these 28 laws called for 461 implementing regulations and we adopted 393 of them, an application rate of 85%",
    "cit_senat_1718": "It now stands at 78% - 86% if measures whose entry into force is deferred are excluded",
    "cit_senat_1819": "The overall rate of application of laws calculated by the Senate is 72%",
    "cit_sgg_1819": "the departments of the General Secretariat of the Government arrive for their part at an overall rate of 82.4%",
    "cit_diverge": "The rate calculated by the Senate may differ from the one calculated by the Government for technical "
                   "reasons, of two kinds.",
    "cit_arretes": "the Senate carries out a comprehensive check of the implementing measures of laws, including the ministerial "
                   "orders (arrêtés) whose publication is provided for by the law. This is not the case of the General "
                   "Secretariat of the Government.",
    "cit_politique": "It may also differ for political reasons, in particular when the Senate considers that a decree adopted "
                     "does not respect the will of the legislator, and therefore that the expected measure has not been taken.",
    "cit_differees": "the Senate includes in its rate the measures expected for articles whose entry into force is deferred, "
                     "unlike the Government.",
    "cit_802_22": "More precisely, 22 of them (39%) were directly applicable",
    "cit_802_24": "the number of laws promulgated during the 2024-2025 session stands at 56, of which 24 directly applicable",
    "cit_802_66": "Overall rate of application of laws 66% (+ 4 points)",
    "cit_802_note": "The data taken into account are those of the measures provided for by the legislative provisions, "
                    "excluding optional measures and measures deferred beyond 31 March 2026.",
    "cit_six_mois": "this year, for the first time, in order to measure the number of regulations adopted only at the end of "
                    "the six-month period the Government sets itself, the period used includes three months fewer for the "
                    "laws promulgated and three months more for the regulations adopted.",
    "cit_sgg16_def": "shows the rate of application at 31 December 2025 of the laws which, among those passed between 1 July 2022 "
                     "and 9 June 2024, call for implementing decrees.",
    "cit_sgg17_def": "shows the rate of application at 31 December 2025 of the laws which, among those published between 18 July "
                     "2024 and 30 June 2025, call for implementing decrees or orders.",
}
SEGMENTS_EN = {
    1: "laws of the parliamentary year, cut-off on 30 September of the same year",
    2: "period shifted by three months to wait for the Government's six-month deadline, ordinary session only",
    3: "'new bounds': laws of 14 July 2011 to 30 September 2012",
    4: "laws of 1 October to 30 September, cut-off on the following 31 March",
    5: "same calendar, deferred measures included (a second rate excludes them)",
    6: "a single rate, excluding optional measures and measures deferred beyond 31 March 2026",
}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def en(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n)


def nombres(s: str) -> set:
    return {x.replace(",", ".") for x in re.findall(r"\d+(?:[.,]\d+)?", s)}


def fr(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n).replace(",", "\u202f").replace(".", ",")


def session(d: str) -> str:
    a = int(d[:4]) if int(d[5:7]) >= 10 else int(d[:4]) - 1
    return "%d-%d" % (a, a + 1)


# ------------------------------------------------------------------ lecture
def csv_extrait(nom: str) -> tuple[str, list[list[str]]]:
    t = (SRC / nom).read_text(encoding="utf-8")
    tete, corps = t.split("\n", 1)
    return tete, list(csv.reader(io.StringIO(corps), delimiter=";"))


def lire() -> dict:
    j = json.loads((SRC / CCIV).read_text(encoding="utf-8"))
    c = j.get("contenu") or j.get("article")
    tl, L = csv_extrait("barometre_lois_extrait.csv")
    tm, M = csv_extrait("barometre_mesures_extrait.csv")
    reg = list(csv.DictReader(io.StringIO((SRC / "registre_concordance.csv").read_text(encoding="utf-8")), delimiter=";"))
    const = {}
    for k, f in CONST.items():
        a = json.loads((SRC / f).read_text(encoding="utf-8"))
        a = a.get("contenu") or a.get("article")
        const[k] = {"etat": a["etat"], "texte": norm(a["texte"]), "id": a["id"]}
    return {"cciv": {"etat": c["etat"], "texte": norm(c["texte"]), "id": c["id"]}, "const": const,
            "lois": L, "mesures": M, "tetes": [tl, tm], "registre": reg,
            "effectifs": json.loads((SRC / "senat_effectifs.json").read_text(encoding="utf-8")),
            "pages": json.loads((SRC / "senat_pages.json").read_text(encoding="utf-8")),
            "sgg": norm((SRC / "sgg_bilan_31-12-2025_extrait.txt").read_text(encoding="utf-8"))}


# ------------------------------------------------------------------ citations (A7)
CIT_CCIV = ("Toutefois, l'entrée en vigueur de celles de leurs dispositions dont l'exécution nécessite des mesures "
            "d'application est reportée à la date d'entrée en vigueur de ces mesures.")
CITATIONS = {  # clé -> (page archivée, citation exacte) ; affichées par jeton
    "cit_sgg_1718": ("r18-542|539", "ces 28 lois appelaient 461 mesures réglementaires d'application et nous en avons pris 393, soit un taux d'application de 85 %"),
    "cit_senat_1718": ("r18-542|5", "Il atteint désormais 78 % - 86 % si on exclut les mesures dont l'entrée en vigueur est différée"),
    "cit_senat_1819": ("r19-523|7", "Le taux global d'application des lois calculé par le Sénat est de 72 %"),
    "cit_sgg_1819": ("r19-523|13", "les services du Secrétariat général du Gouvernement parviennent pour leur part à un taux global de 82,4 %"),
    "cit_diverge": ("r19-523|13", "Le taux calculé par le Sénat peut diverger de celui calculé par le Gouvernement pour des raisons techniques, qui sont de deux ordres."),
    "cit_arretes": ("r19-523|13", "le Sénat effectue un contrôle global des mesures d'application des lois, en incluant les arrêtés dont la publication est prévue par la loi. Ce n'est pas le cas du secrétariat général du Gouvernement."),
    "cit_politique": ("r19-523|13", "Il peut également diverger pour des raisons politiques, notamment lorsque le Sénat considère qu'un décret pris ne respecte pas la volonté du législateur, et donc que la mesure attendue n'est pas prise."),
    "cit_differees": ("r19-523|13", "le Sénat intègre dans son taux les mesures attendues pour des articles dont l'entrée en vigueur est différée, à la différence du Gouvernement."),
    "cit_802_22": ("r25-802|45", "Plus précisément, 22 d'entre elles (soit 39 %) étaient d'application directe"),
    "cit_802_24": ("r25-802|271", "le nombre de lois promulguées lors de la session 2024-2025 s'établit à 56, dont 24 d'application directe"),
    "cit_802_66": ("r25-802|7", "Taux d'application global des lois 66 % (+ 4 points)"),
    "cit_802_note": ("r25-802|7", "Les données prises en compte sont celles des mesures prévues, non éventuelles et non différées au-delà du 31 mars 2026, par les dispositions législatives."),
    "cit_six_mois": ("r11-323|11", "cette année, pour la première fois, afin de ne mesurer le nombre de mesures réglementaires prises qu'à l'expiration du délai de six mois que s'impose à lui-même le Gouvernement, la période retenue comprend trois mois de moins pour les lois promulguées retenues et trois mois de plus pour les mesures réglementaires prises."),
}
CIT_SGG = {  # extrait verbatim du bilan SGG au 31/12/2025, lu par navigateur
    "sgg16_def": "fait apparaître le taux d'application au 31 décembre 2025 des lois qui, parmi celles votées entre le 1er juillet 2022 et le 9 juin 2024, appellent des décrets d'application.",
    "sgg17_def": "fait apparaître le taux d'application au 31 décembre 2025 des lois qui, parmi celles publiées entre le 18 juillet 2024 et le 30 juin 2025, appellent des décrets ou des arrêtés d'application.",
    "sgg16_total": "Total général 1088 948 140 87%",
    "sgg17_total": "Total général 320 177 143 55%",
    "sgg_2025_138": "Loi n° 2025-138 du 17 février 2025 pour améliorer la prise en charge de la sclérose latérale amyotrophique et d'autres maladies évolutives graves 1 0 1 0%",
}

# Série longue du Sénat : (session, valeur, page archivée, citation, segment). Valeurs telles que publiées ; 2009-2010
# est écartée de la figure (date d'arrêté non précisée dans la phrase), la republication arrondie de 2013 aussi.
SERIE = [
    ("2002-2003", 9.7, "cp20051201.html|html", "en 2002-2003 ( 9,7 % )", 1),
    ("2003-2004", 14.4, "cp20051201.html|html", "qui passe de 14,4 % en 2003-2004 à 16,4 % en 2004-2005", 1),
    ("2004-2005", 16.4, "cp20051201.html|html", "qui passe de 14,4 % en 2003-2004 à 16,4 % en 2004-2005", 1),
    ("2005-2006", 30, "appleg_06-syn|2", "en 2005-2006, à 30 %", 1),
    ("2006-2007", 32.1, "apleg_08-syn|1", "32,1 % en 2006-2007 à 24,6 % en 2007-2008", 1),
    ("2007-2008", 24.6, "apleg_08-syn|1", "32,1 % en 2006-2007 à 24,6 % en 2007-2008", 1),
    ("2008-2009", 27, "apleg_09-syn|2", "a atteint 27 % en 2008-2009", 1),
    ("2010-2011", 64, "r11-323|11", "346 mesures réglementaires sur les 540 prévues avaient été publiées, soit 64 %", 2),
    ("2011-2012", 66, "r12-654|8", "atteint en effet un taux global de 66 %", 3),
    ("2012-2013", 64, "r13-623|15", "ou à environ 64 % (si on compte en nombre de mesures)", 4),
    ("2013-2014", 55, "r14-495|5", "ce taux s'élève à 55 %", 4),
    ("2014-2015", 62, "r15-650|11", "mise en œuvre des mesures législatives) 62 %", 4),
    ("2015-2016", 71, "r16-677|11", "mesures législatives) 71 % (+ 9%)", 4),
    ("2016-2017", 73, "r17-510|18", "session parlementaire 2016-2017 73% (+2 points)", 4),
    ("2017-2018", 78, "r18-542|5", "Il atteint désormais 78 % - 86 % si on exclut", 5),
    ("2018-2019", 72, "r19-523|7", "Le taux global d'application des lois calculé par le Sénat est de 72 %", 5),
    ("2019-2020", 62, "r20-645|16", "est de 62 % - en retrait de dix points", 5),
    ("2020-2021", 57, "r21-658|3", "Le taux global d'application des lois calculé par le Sénat est de 57 %", 5),
    ("2021-2022", 65, "r22-636|3", "Le taux global d'application des lois calculé par le Sénat est de 65 %", 5),
    ("2022-2023", 64, "r23-624|3", "Le taux global d'application des lois calculé par le Sénat est de 64 %", 5),
    ("2023-2024", 59, "r24-710|3", "et s'établit à 59 %", 5),
    ("2024-2025", 66, "r25-802|7", "Taux d'application global des lois 66 % (+ 4 points)", 6),
]
REVISION = ("2019-2020", 60, "r21-658|3", "soit un taux inférieur à celui de l'année précédente (60 %)")
SEGMENTS = {
    1: "lois de l'année parlementaire, arrêt au 30 septembre de la même année",
    2: "période décalée de trois mois pour attendre le délai de six mois du Gouvernement, session ordinaire seule",
    3: "« nouvelles bornes » : lois du 14 juillet 2011 au 30 septembre 2012",
    4: "lois du 1er octobre au 30 septembre, arrêt au 31 mars suivant",
    5: "même calendrier, mesures différées comprises (un second taux les exclut)",
    6: "un seul taux, sans mesures éventuelles ni différées au-delà du 31 mars 2026",
}


def verifier_citations(S: dict) -> dict:
    P = S["pages"]
    out = {}
    for k, (pg, c) in CITATIONS.items():
        if pg not in P or norm(c) not in P[pg]["texte"]:
            raise Arret("A7 : citation %s absente de la page %s : %r" % (k, pg, c[:60]))
        out[k] = norm(c)
    for k, c in CIT_SGG.items():
        if norm(c) not in S["sgg"]:
            raise Arret("A7 : extrait SGG %s introuvable" % k)
    for s, v, pg, c, _ in SERIE + [REVISION + (5,)]:
        if pg not in P or norm(c) not in P[pg]["texte"]:
            raise Arret("A7 : serie %s : citation absente de %s" % (s, pg))
        val = ("%g" % v).replace(".", ",")
        if not re.search(r"(?<![\d,])%s ?%%" % re.escape(val), norm(c)):
            raise Arret("A7 : serie %s : valeur %s absente de sa citation" % (s, val))
    return out


# ------------------------------------------------------------------ calcul et gardes
def calculer(S: dict) -> tuple[dict, list[str]]:
    g = []
    if S["cciv"]["etat"] != "VIGUEUR" or norm(CIT_CCIV) not in S["cciv"]["texte"]:
        raise Arret("A1 : code civil, art. 1 : texte non en vigueur ou phrase du report introuvable")
    for k, c in CIT_CONST.items():
        if S["const"][k]["etat"] != "VIGUEUR" or norm(c) not in S["const"][k]["texte"]:
            raise Arret("A1 : Constitution %s : texte non en vigueur ou citation introuvable" % k)
    try:
        tcen = cen.texte()
        cit_en = {"cit_" + k: cen.citer(a, c, tcen) for k, (a, c) in CONST_EN.items()}
    except ValueError as e:
        raise Arret("A1 : %s" % e)
    g.append("A1 : Constitution art. 10 et 61 (FR Legifrance, EN Conseil constitutionnel), code civil art. 1")
    cit = verifier_citations(S)
    orig = dict(cit, cit_cciv=norm(CIT_CCIV), cit_sgg16_def=norm(CIT_SGG["sgg16_def"]), cit_sgg17_def=norm(CIT_SGG["sgg17_def"]))
    for k, tr in TR.items():
        if k not in orig:
            raise Arret("A7 bis : traduction %s sans original" % k)
        if not nombres(tr) <= nombres(orig[k]):
            raise Arret("A7 bis : %s : nombres de la traduction absents de l'original : %s" % (k, nombres(tr) - nombres(orig[k])))
    g.append("A7 : %d citations du Senat, %d extraits du SGG, %d valeurs de serie retrouvees mot pour mot"
             % (len(CITATIONS), len(CIT_SGG), len(SERIE) + 1))

    # --- E1 : champ
    L = S["lois"]
    h = L[0]
    iD, iT, iJ, iConv, iDir, iSE = 0, 1, 2, h.index("Loi autorisant la ratification d'accords internationaux"), \
        h.index("Loi d'application directe"), h.index("Loi sans échéancier")
    iNa, iNapp = h.index("Nombre de mesures à appliquer"), h.index("Nombre de mesures appliquées")
    champ, ecartees = {}, collections.Counter()
    entree = collections.Counter()
    for l in L[1:]:
        s = session(l[iD])
        entree[s] += 1
        if l[iConv] == "oui":
            ecartees[s] += 1
            continue
        champ[l[iJ]] = {"session": s, "directe": l[iDir] == "oui", "na": int(l[iNa]), "napp": int(l[iNapp]), "titre": l[iT]}
    N = collections.Counter(v["session"] for v in champ.values())
    for s in SESSIONS:
        if entree[s] != N[s] + ecartees[s]:
            raise Arret("A2 : %s entre %d != retenu %d + ecarte %d" % (s, entree[s], N[s], ecartees[s]))
    reg = S["registre"]
    rj = {r["jorf"]: r for r in reg}
    if set(rj) != set(champ):
        raise Arret("A2 : registre et champ du barometre different (%d lois hors registre, %d hors champ)"
                    % (len(set(champ) - set(rj)), len(set(rj) - set(champ))))
    g.append("A2 : %d lois au champ, %d conventions ecartees, registre identique loi par loi" % (len(champ), sum(ecartees.values())))

    # --- E1 : classements
    for j, v in champ.items():
        if (rj[j]["directe_baro"] == "oui") != v["directe"]:
            raise Arret("A3 : %s : « directe » du registre != barometre" % rj[j]["num_loi"])
        if v["directe"] and v["na"] != 0:
            raise Arret("A3 : %s classee directe avec %d mesure(s) a appliquer" % (rj[j]["num_loi"], v["na"]))
    E = S["effectifs"]
    Dsen = collections.Counter(r["session"] for r in reg if r["directe_senat"] == "oui")
    for s in SESSIONS[:-1]:
        if Dsen[s] != E[s]["annonces"]["directe"]:
            raise Arret("A3 : %s : Senat %d lois directes au registre, %d annoncees" % (s, Dsen[s], E[s]["annonces"]["directe"]))
    somme = 0
    for k, t in E["2024-2025"]["annonces_commissions"].items():
        m = re.search(r"(\d+|%s) (?:étaient|était) d.application directe" % "|".join(MOTS), t)
        if not m:
            raise Arret("A3 : 2024-2025 : effectif de commission illisible (%s)" % k)
        somme += int(m.group(1)) if m.group(1).isdigit() else MOTS[m.group(1)]
    if not (somme == Dsen["2024-2025"] == 22 and "22 d'entre elles" in cit["cit_802_22"]):
        raise Arret("A3 : 2024-2025 : commissions %d, registre %d, synthese 22" % (somme, Dsen["2024-2025"]))
    g.append("A3 : directes du barometre recalculees = registre ; effectifs du Senat = annonces (2024-2025 : %d par commissions)" % somme)
    lignes = []
    for s in SESSIONS:
        rs = [r for r in reg if r["session"] == s]
        D = sum(1 for r in rs if r["directe_baro"] == "oui" and r["directe_senat"] == "oui")
        U = sum(1 for r in rs if r["directe_baro"] != r["directe_senat"])
        if s == "2024-2025":  # « dont 24 » (p. 271) sans liste nominative : 2 lois non identifiées, en U
            U += 24 - Dsen[s]
        Db = sum(1 for r in rs if r["directe_baro"] == "oui")
        lignes.append({"session": s, "N": N[s], "D": D, "U": U, "baro": Db, "senat": Dsen[s],
                       "senat_publie": 24 if s == "2024-2025" else Dsen[s], "conventions": ecartees[s]})
    tient = all(2 * (x["D"] + x["U"]) < x["N"] for x in lignes)
    contraires = [x for x in lignes if 2 * (x["D"] + x["U"]) >= x["N"]]
    if tient or not contraires:
        raise Arret("A4 : la phrase « moins de la moitie » tiendrait dans chaque session : la page dit le contraire, a reecrire")
    ct = contraires[0]
    if not 2 * ct["baro"] > ct["N"]:
        raise Arret("A4 : %s : le barometre seul ne depasse pas la moitie" % ct["session"])
    if any(2 * x["D"] > x["N"] for x in lignes):
        raise Arret("A4 : une majorite inverse serait a dire")
    # Phrase de la page : « En <ct>, le baromètre … plus de la moitié ; dans les autres sessions, les lois directes restent
    # sous la moitié, quelle que soit la source. »
    if len(contraires) != 1 or any(2 * max(x["baro"], x["senat_publie"], x["D"] + x["U"]) >= x["N"] for x in lignes if x is not ct):
        raise Arret("A4 : « dans les autres sessions, sous la moitie quelle que soit la source » faux")
    ndesacc = sum(1 for r in reg if r["directe_baro"] != r["directe_senat"])
    g.append("A4 : aucune phrase generale ; %s : barometre %d/%d ; %d lois classees differemment"
             % (ct["session"], ct["baro"], ct["N"], ndesacc))

    # --- E2 : mesures
    M = S["mesures"]
    hm = M[0]
    iLoi, iEtat, iActe, iObs, iObj = 1, hm.index("État"), hm.index("Identifiant décret"), \
        hm.index("Objectif initial de publication, observations"), hm.index("Objet")
    cl = collections.defaultdict(collections.Counter)
    par_loi = collections.defaultdict(collections.Counter)
    obs_acte = collections.Counter()
    differ_A = collections.Counter()
    cas = []
    for m in M[1:]:
        if m[iLoi] not in champ:
            if m[iLoi] in {l[iJ] for l in L[1:]}:
                raise Arret("A5 : mesure rattachee a une convention ecartee")
            raise Arret("A5 : mesure d'une loi hors extrait")
        s = champ[m[iLoi]]["session"]
        e = m[iEtat]
        if e == "appliqué":
            c = "P" if m[iActe].strip() else "U"
        elif e == "en attente d'application":
            c = "A"
        elif e == "sans objet":
            c = "S"
        else:
            c = "U"
        cl[s][c] += 1
        par_loi[m[iLoi]][e] += 1
        if c == "S" and re.match(r"\s*(Arr[êe]t[ée]|D[ée]cret)\b", m[iObs]):
            obs_acte[s] += 1
        if c == "A" and re.search(r"\bdiff[ée]r[ée]e?s?\b", m[iObs] + " " + m[iObj], re.I):  # pas « différent », « différer »
            differ_A[s] += 1
        if champ[m[iLoi]]["titre"].startswith("LOI n° 2025-138 "):
            cas.append((e, m[iObs]))
    for j, v in champ.items():
        pl = par_loi[j]
        if v["na"] != pl["appliqué"] + pl["en attente d'application"] or v["napp"] != pl["appliqué"]:
            raise Arret("A5 : %s : fichier des lois (%d/%d) != mesures (%d appliquees, %d en attente)"
                        % (rj[j]["num_loi"], v["napp"], v["na"], pl["appliqué"], pl["en attente d'application"]))
    nmes = len(M) - 1
    if nmes != sum(sum(c.values()) for c in cl.values()):
        raise Arret("A5 : bilan des mesures")
    g.append("A5 : %d mesures, N = P + A + S + U ; coherence loi par loi avec le fichier des lois du meme producteur" % nmes)
    if not (cas and all(e == "sans objet" and re.match(r"\s*Arr[êe]t[ée] du", o) for e, o in cas)):
        raise Arret("A6 : cas 2025-138 : le barometre ne la porte plus « sans objet » avec un arrete : texte a revoir")
    g.append("A6 : 2025-138 : %d mesure(s) « sans objet » portant un arrete au barometre, en attente au SGG (31/12/2025)" % len(cas))
    tot = collections.Counter()
    for s in SESSIONS:
        tot.update(cl[s])
    if not tot["A"] > 0 or not cl["2017-2018"]["A"] > 0:
        raise Arret("A5 : « des mesures attendent encore » faux")
    r = {"lignes": lignes, "ct": ct, "ndesacc": ndesacc, "nregistre": len(reg), "conventions": sum(ecartees.values()),
         "cl": {s: dict(cl[s]) for s in SESSIONS}, "tot": dict(tot), "nmes": nmes, "obs_acte": dict(obs_acte),
         "differ_A": dict(differ_A), "cas_2025_138": cas[0][1].strip(), "citations": cit, "cit_en": cit_en}
    return r, g


def pc(a, b, dec=0) -> str:
    return fr(100 * a / b, dec)


def affichage(r: dict) -> dict:
    t, ct, cl = r["tot"], r["ct"], r["cl"]
    l25 = r["lignes"][-1]
    A = {
        "releve": RELEVE, "nmes": fr(r["nmes"]), "P": fr(t.get("P", 0)), "A": fr(t.get("A", 0)), "S": fr(t.get("S", 0)),
        "U": fr(t.get("U", 0)), "A_pct": pc(t.get("A", 0), r["nmes"], 1),
        "A_1718": fr(cl["2017-2018"].get("A", 0)), "N_1718": fr(sum(cl["2017-2018"].values())),
        "A_2425": fr(cl["2024-2025"].get("A", 0)), "N_2425": fr(sum(cl["2024-2025"].values())),
        "differ_A": fr(sum(r["differ_A"].values())), "obs_acte": fr(sum(r["obs_acte"].values())),
        "obs_acte_2425": fr(r["obs_acte"].get("2024-2025", 0)), "cas_2025_138": r["cas_2025_138"],
        "nlois": fr(r["nregistre"]), "conventions": fr(r["conventions"]), "ndesacc": fr(r["ndesacc"]),
        "ct_session": ct["session"], "ct_baro": fr(ct["baro"]), "ct_senat": fr(ct["senat"]), "ct_N": fr(ct["N"]),
        "s25_baro": fr(l25["baro"]), "s25_senat": fr(l25["senat"]), "s25_publie": fr(l25["senat_publie"]),
        "s25_N": fr(l25["N"]),
        "nsessions": LETTRES[len(SESSIONS)],
        "releve_le": "05/10/2026 (baromètre de l'application des lois) ; rapports du Sénat lus le 06/10/2026 ; bilan du SGG au 31/12/2025, lu le 06/10/2026",
    }
    # « plus de N ans après leur promulgation » : du 30/09/2018 (dernière loi possible de la session) au relevé
    j, mo, an = map(int, RELEVE.split("/"))
    age = an - 2018 - (1 if (mo, j) < (9, 30) else 0)
    if age not in LETTRES:
        raise Arret("A5 : age des lois de 2017-2018 hors bornes")
    A["age_1718"] = LETTRES[age]
    for k, cle in (("senat_1819", "cit_senat_1819"), ("sgg_1819", "cit_sgg_1819")):
        m = re.search(r"(\d+(?:,\d+)?) %", r["citations"][cle])
        A[k] = m.group(1) + " %"
    A.update(r["citations"])
    A["cit_cciv"] = norm(CIT_CCIV)
    A["cit_art10"] = norm(CIT_CONST["art10"])
    A["cit_art61"] = norm(CIT_CONST["art61"])
    A["nautres"] = LETTRES[len(SESSIONS) - 1]
    A["nsegments"] = LETTRES[len(SEGMENTS)]
    A["cit_sgg16_def"] = norm(CIT_SGG["sgg16_def"])
    A["cit_sgg17_def"] = norm(CIT_SGG["sgg17_def"])
    A.update({k + "_tr": v for k, v in TR.items()})
    return A


def affichage_en(r: dict, A_fr: dict) -> dict:
    t, ct, cl = r["tot"], r["ct"], r["cl"]
    l25 = r["lignes"][-1]
    A = {
        "releve": "5 October 2026", "nmes": en(r["nmes"]), "P": en(t.get("P", 0)), "A": en(t.get("A", 0)), "S": en(t.get("S", 0)),
        "U": en(t.get("U", 0)), "A_pct": en(100 * t.get("A", 0) / r["nmes"], 1),
        "A_1718": en(cl["2017-2018"].get("A", 0)), "N_1718": en(sum(cl["2017-2018"].values())),
        "A_2425": en(cl["2024-2025"].get("A", 0)), "N_2425": en(sum(cl["2024-2025"].values())),
        "differ_A": en(sum(r["differ_A"].values())), "obs_acte": en(sum(r["obs_acte"].values())),
        "obs_acte_2425": en(r["obs_acte"].get("2024-2025", 0)), "cas_2025_138": r["cas_2025_138"],
        "nlois": en(r["nregistre"]), "conventions": en(r["conventions"]), "ndesacc": en(r["ndesacc"]),
        "ct_session": ct["session"], "ct_baro": en(ct["baro"]), "ct_senat": en(ct["senat"]), "ct_N": en(ct["N"]),
        "s25_baro": en(l25["baro"]), "s25_senat": en(l25["senat"]), "s25_publie": en(l25["senat_publie"]),
        "s25_N": en(l25["N"]),
        "nsessions": LETTRES_EN[len(SESSIONS)], "nautres": LETTRES_EN[len(SESSIONS) - 1],
        "nsegments": LETTRES_EN[len(SEGMENTS)],
        "age_1718": LETTRES_EN[MOTS[A_fr["age_1718"]]],
        "releve_le": "5 October 2026 (barometer of the application of laws); Senate reports read on 6 October 2026; "
                     "General Secretariat of the Government report at 31 December 2025, read on 6 October 2026",
    }
    for k in ("senat_1819", "sgg_1819"):
        A[k] = A_fr[k].replace("\u00a0", "").replace(",", ".")
    for k, v in A_fr.items():  # citations françaises : l'original, suivi de sa traduction (_tr)
        if k.startswith("cit_") and k not in ("cit_art10", "cit_art61"):
            A[k] = v
    A.update(r["cit_en"])
    A.update({k + "_tr": v for k, v in TR.items()})
    return A


def tableaux_en(r: dict) -> dict:
    lois = []
    for x in r["lignes"]:
        b = "%d out of %d" % (x["D"], x["N"]) if x["U"] == 0 else "%d to %d out of %d" % (x["D"], x["D"] + x["U"], x["N"])
        lois.append([x["session"], str(x["N"]), str(x["baro"]),
                     str(x["senat"]) + (" (%d on another page of the same report)" % x["senat_publie"] if x["senat_publie"] != x["senat"] else ""),
                     b])
    mes = [[s, en(sum(r["cl"][s].values()))] + [en(r["cl"][s].get(k, 0)) for k in "PASU"] for s in SESSIONS]
    mes.append(["Total", en(r["nmes"])] + [en(r["tot"].get(k, 0)) for k in "PASU"])
    serie = [[s, ("%g" % v) + "%", SEGMENTS_EN[seg], pg.split("|")[0]] for s, v, pg, _, seg in SERIE]
    serie.insert(17, [REVISION[0], "60% (figure revised the following year)", SEGMENTS_EN[5], REVISION[2].split("|")[0]])
    return {
        "lois": {"entetes": ["Session", "Laws promulgated (excluding treaties)", "Directly applicable according to the barometer",
                             "According to the Senate", "Bounds: directly applicable for both sources, then counting divergent classifications"],
                 "lignes": lois},
        "mesures": {"entetes": ["Session of the law", "Measures", "Identified published instrument", "Pending", "Listed as moot",
                                "Incomplete status"], "lignes": mes},
        "serie": {"entetes": ["Session", "Rate published by the Senate", "Definition (segment)", "Document"], "lignes": serie},
    }


def tableaux(r: dict) -> dict:
    lois = []
    for x in r["lignes"]:
        b = "%d sur %d" % (x["D"], x["N"]) if x["U"] == 0 else "de %d à %d sur %d" % (x["D"], x["D"] + x["U"], x["N"])
        lois.append([x["session"], str(x["N"]), str(x["baro"]),
                     str(x["senat"]) + (" (%d dans une autre page du même rapport)" % x["senat_publie"] if x["senat_publie"] != x["senat"] else ""),
                     b])
    mes = []
    for s in SESSIONS:
        c = r["cl"][s]
        mes.append([s, fr(sum(c.values())), fr(c.get("P", 0)), fr(c.get("A", 0)), fr(c.get("S", 0)), fr(c.get("U", 0))])
    t = r["tot"]
    mes.append(["Total", fr(r["nmes"]), fr(t.get("P", 0)), fr(t.get("A", 0)), fr(t.get("S", 0)), fr(t.get("U", 0))])
    serie = [[s, ("%g" % v).replace(".", ",") + " %", SEGMENTS[seg], pg.split("|")[0]] for s, v, pg, _, seg in SERIE]
    serie.insert(17, [REVISION[0], "60 % (valeur reprise l'année suivante)", SEGMENTS[5], REVISION[2].split("|")[0]])
    return {
        "lois": {"entetes": ["Session", "Lois promulguées (hors conventions)", "D'application directe selon le baromètre",
                             "Selon le Sénat", "Bornes : directes pour les deux sources, puis en comptant les classements divergents"],
                 "lignes": lois},
        "mesures": {"entetes": ["Session de la loi", "Mesures", "Acte publié identifié", "En attente", "Indiquées sans objet",
                                "Statut incomplet"], "lignes": mes},
        "serie": {"entetes": ["Session", "Taux publié par le Sénat", "Définition (segment)", "Document"], "lignes": serie},
    }


# ------------------------------------------------------------------ figures
W = 720
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LANG = "fr"


def nb(n) -> str:
    return en(n) if LANG == "en" else fr(n)


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
    "fr": {"src1": "Baromètre de l'application des lois (Assemblée nationale, LexImpact ; données DILA), état au " + RELEVE,
           "note1": "Lois promulguées par session (1er oct.-30 sept.), hors conventions. État à la date du relevé : ni un taux historique, ni une efficacité.",
           "src2": "Baromètre de l'application des lois (état au %s) ; rapports annuels du Sénat sur l'application des lois" % RELEVE,
           "note2": "Gris : lois que le baromètre et le Sénat classent différemment (2024-2025 : 2 lois sans liste nominative en plus).",
           "src3": "Sénat, bilans annuels de l'application des lois, 2003-2026 (taux tels que publiés, page citée dans le tableau)",
           "note3": LETTRES[len(SEGMENTS)].capitalize() + " définitions successives : ne pas relier les segments. Une révision de chiffre et une rupture de définition sont deux faits distincts.",
           "t1": "Les mesures d'application des lois, par session de la loi", "s1": "nombre de mesures recensées et leur état au %s" % RELEVE,
           "d1": "Barres horizontales, une par session de 2017-2018 à 2024-2025 : mesures avec un acte publié identifié, en attente, "
                 "indiquées sans objet. Au total {nmes} mesures, dont {A} en attente. Les valeurs sont dans le tableau sous la figure.",
           "l1": ["acte publié identifié", "en attente", "indiquées sans objet", "statut incomplet"], "attente": "{} en attente",
           "t2": "Les lois qui n'appellent aucune mesure d'application, par session",
           "s2": "nombre de lois promulguées, hors conventions ; trait noir : la moitié des lois de la session",
           "d2": "Barres horizontales, une par session : lois d'application directe pour les deux sources, lois classées différemment "
                 "par le baromètre et par le Sénat, lois qui appellent des mesures. En {ct_session}, le baromètre compte {ct_baro} lois "
                 "d'application directe sur {ct_N}. Les valeurs sont dans le tableau sous la figure.",
           "l2": ["application directe (les deux sources)", "classement divergent", "appellent des mesures"], "lois": "{} lois",
           "t3": "Le taux d'application des lois publié par le Sénat, 2002-2003 à 2024-2025",
           "s3": "en %% des mesures attendues ; %s définitions successives, fonds alternés : un segment ne se compare pas à un autre" % LETTRES[len(SEGMENTS)],
           "d3": "Points par session, regroupés en %s segments séparés par des ruptures de définition : de {a} %% à {b} %% dans le premier "
                 "segment ({c} à {d}), de {e} %% à {f} %% dans les suivants. Les valeurs, leur document et leur définition sont dans le "
                 "tableau sous la figure." % LETTRES[len(SEGMENTS)],
           "pct": "{} %", "leg3": "1 à 6 : segments (définitions dans le tableau) ; cercle vide : valeur 2019-2020 reprise l'année suivante"},
    "en": {"src1": "Barometer of the application of laws (National Assembly, LexImpact; DILA data), status at 5 October 2026",
           "note1": "Laws promulgated per session (1 Oct.-30 Sept.), excluding treaties. Status at the reading date: neither a past rate nor efficiency.",
           "src2": "Barometer of the application of laws (status at 5 October 2026); Senate annual reports on the application of laws",
           "note2": "Grey: laws that the barometer and the Senate classify differently (2024-2025: plus 2 laws with no list of names).",
           "src3": "French Senate, annual reports on the application of laws, 2003-2026 (rates as published, page cited in the table)",
           "note3": LETTRES_EN[len(SEGMENTS)].capitalize() + " successive definitions: do not join the segments. A revised figure and a change of definition are two distinct facts.",
           "t1": "Implementing measures of French laws, by session of the law", "s1": "number of measures listed and their status at 5 October 2026",
           "d1": "Horizontal bars, one per session from 2017-2018 to 2024-2025: measures with an identified published instrument, pending, "
                 "listed as moot. In total {nmes} measures, {A} of them pending. The values are in the table below the figure.",
           "l1": ["identified published instrument", "pending", "listed as moot", "incomplete status"], "attente": "{} pending",
           "t2": "French laws that call for no implementing measure, by session",
           "s2": "number of laws promulgated, excluding treaties; black mark: half of the session's laws",
           "d2": "Horizontal bars, one per session: laws directly applicable for both sources, laws classified differently by the "
                 "barometer and the Senate, laws that call for measures. In {ct_session}, the barometer counts {ct_baro} directly "
                 "applicable laws out of {ct_N}. The values are in the table below the figure.",
           "l2": ["directly applicable (both sources)", "divergent classification", "call for measures"], "lois": "{} laws",
           "t3": "The rate of application of laws published by the French Senate, 2002-2003 to 2024-2025",
           "s3": "in %% of expected measures; %s successive definitions, alternating backgrounds: one segment does not compare with another" % LETTRES_EN[len(SEGMENTS)],
           "d3": "Points by session, grouped in %s segments separated by changes of definition: from {a}%% to {b}%% in the first segment "
                 "({c} to {d}), from {e}%% to {f}%% in the following ones. The values, their document and their definition are in the "
                 "table below the figure." % LETTRES_EN[len(SEGMENTS)],
           "pct": "{}%", "leg3": "1 to 6: segments (definitions in the table); open circle: 2019-2020 figure revised the following year"},
}


def fig_mesures(r: dict, A: dict) -> str:
    H = 330
    x0, x1, y0 = 78, W - 46, 74
    vmax = 1000
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    pas = 28
    L = T[LANG]
    e = cadre(H, "am", L["t1"], L["s1"], L["d1"].format(**A))
    legende(e, 58, list(zip((BLEU, ORANGE, GRIS_CLAIR, GRIS), L["l1"])))
    for v in range(0, vmax + 1, 250):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 8 + 2, GRID))
        e.append(txt(X(v), y0 + pas * 8 + 16, nb(v), 9, MUTED, "middle"))
    for i, s in enumerate(SESSIONS):
        c = r["cl"][s]
        y = y0 + i * pas
        e.append(txt(0, y + 15, s, 10, INK))
        a = 0
        for k, col in (("P", BLEU), ("A", ORANGE), ("S", GRIS_CLAIR), ("U", GRIS)):
            v = c.get(k, 0)
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append(txt(X(a) + 4, y + 14, L["attente"].format(nb(c.get("A", 0))), 9, INK2))
    e += cartouche(H, L["src1"], L["note1"])
    e.append("</svg>")
    return "\n".join(e)


def fig_lois(r: dict, A: dict) -> str:
    H = 330
    x0, x1, y0 = 78, W - 60, 74
    vmax = 70
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    pas = 28
    L = T[LANG]
    e = cadre(H, "al", L["t2"], L["s2"], L["d2"].format(**A))
    legende(e, 58, list(zip((BLEU, GRIS, GRIS_CLAIR), L["l2"])))
    for v in range(0, vmax + 1, 10):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 8 + 2, GRID))
        e.append(txt(X(v), y0 + pas * 8 + 16, str(v), 9, MUTED, "middle"))
    for i, x in enumerate(r["lignes"]):
        y = y0 + i * pas
        e.append(txt(0, y + 15, x["session"], 10, INK))
        a = 0
        for v, col in ((x["D"], BLEU), (x["U"], GRIS), (x["N"] - x["D"] - x["U"], GRIS_CLAIR)):
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2"/>' % (X(x["N"] / 2), y - 3, X(x["N"] / 2), y + 23, INK))
        e.append(txt(X(x["N"]) + 4, y + 14, L["lois"].format(x["N"]), 9, INK2))
    e += cartouche(H, L["src2"], L["note2"])
    e.append("</svg>")
    return "\n".join(e)


def fig_serie(r: dict, A: dict) -> str:
    H = 330
    sess = ["%d-%d" % (a, a + 1) for a in range(2002, 2025)]
    x0, x1, y0, y1 = 40, W - 10, 74, 272
    bw = (x1 - x0) / len(sess)
    X = lambda s: x0 + (sess.index(s) + 0.5) * bw  # noqa: E731
    Y = lambda v: y1 - v / 100 * (y1 - y0)  # noqa: E731
    L = T[LANG]
    nb1 = (lambda v: ("%g" % v)) if LANG == "en" else (lambda v: fr(v, 1).replace(",0", ""))
    e = cadre(H, "as", L["t3"], L["s3"], L["d3"].format(
        a=nb1(min(v for _, v, _, _, g in SERIE if g == 1)), b=nb1(max(v for _, v, _, _, g in SERIE if g == 1)),
        c=SERIE[0][0], d=[s for s, _, _, _, g in SERIE if g == 1][-1],
        e=nb(min(v for _, v, _, _, g in SERIE if g > 1)), f=nb(max(v for _, v, _, _, g in SERIE if g > 1))))
    for v in range(0, 101, 25):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (x0, Y(v), x1, Y(v), GRID))
        e.append(txt(x0 - 6, Y(v) + 4, L["pct"].format(v), 9, MUTED, "end"))
    segs = collections.OrderedDict()
    for s, v, _, _, seg in SERIE:
        segs.setdefault(seg, []).append((s, v))
    for k, (seg, pts) in enumerate(segs.items()):
        xa, xb = X(pts[0][0]) - bw / 2 + 1, X(pts[-1][0]) + bw / 2 - 1
        if k % 2 == 0:
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#f3f2ee"/>' % (xa, y0, xb - xa, y1 - y0))
        e.append(txt((xa + xb) / 2, y0 - 6, str(seg), 10, INK2, "middle", "600"))
        if len(pts) > 1:
            e.append('<polyline fill="none" stroke="%s" stroke-width="1.6" points="%s"/>'
                     % (BLEU, " ".join("%.1f,%.1f" % (X(s), Y(v)) for s, v in pts)))
        for s, v in pts:
            e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s"/>' % (X(s), Y(v), BLEU))
    e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#ffffff" stroke="%s" stroke-width="1.4"/>' % (X(REVISION[0]), Y(REVISION[1]), BLEU))
    for s in sess:
        a = int(s[:4])
        if a % 5 == 2 or s == "2024-2025":
            e.append(txt(X(s), y1 + 14, s, 9, MUTED, "middle"))
    e.append(txt(x1, y1 + 30, L["leg3"], 9, INK2, "end"))
    e += cartouche(H, L["src3"], L["note3"])
    e.append("</svg>")
    return "\n".join(e)


MONTRE_EN = {
    "mesures": "On {releve}, of the {nmes} implementing measures listed by the barometer for the laws promulgated in France from "
               "October 2017 to September 2025, {P} have an identified published instrument, {A} are pending and {S} are listed as moot.",
    "lois": "'Fewer than half in every session' does not hold: in {ct_session}, the barometer counts {ct_baro} directly applicable "
            "laws out of {ct_N}; in the {nautres} other sessions, even the upper bound stays below half. The two sources classify "
            "{ndesacc} of the {nlois} laws differently.",
    "serie": "The rate published by the French Senate rests on {nsegments} successive definitions since 2002-2003: the segments "
             "do not read as a single series.",
}


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    montre = {
        "mesures": ("appliquer-mesures", "Au %s, sur les %s mesures d'application recensées par le baromètre pour les lois "
                    "promulguées d'octobre 2017 à septembre 2025, %s ont un acte publié identifié, %s sont en attente et %s sont "
                    "indiquées sans objet." % (A["releve"], A["nmes"], A["P"], A["A"], A["S"])),
        "lois": ("appliquer-lois", "« Moins de la moitié dans chaque session » ne tient pas : en %s, le baromètre compte %s lois "
                 "d'application directe sur %s ; dans les %s autres sessions, même la borne haute reste sous la moitié. Les deux "
                 "sources classent différemment %s des %s lois."
                 % (A["ct_session"], A["ct_baro"], A["ct_N"], A["nautres"], A["ndesacc"], A["nlois"])),
        "serie": ("appliquer-serie", "Le taux publié par le Sénat repose sur %s définitions successives depuis 2002-2003 : les "
                  "segments ne se lisent pas comme une seule série." % LETTRES[len(SEGMENTS)]),
    }
    res = {}
    for lang, suf in (("fr", ""), ("en", "-en")):
        out = []
        for ident, (fichier, m) in montre.items():
            svg = figs[fichier + suf + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
            if len(cart) != 3 or cart[-1] != LICENCES[lang]:
                raise Arret("fiche %s%s : cartouche illisible" % (fichier, suf))
            out.append(dict(id=ident, fichier=fichier + suf, titre=titre,
                            montre=m if lang == "fr" else MONTRE_EN[ident].format(**A_en), source=cart[0], precaution=cart[1]))
        res[lang] = out
    return res


def csv_texte(r: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "session", "categorie", "valeur", "unite", "source"])
    for x in r["lignes"]:
        for k, lab in (("N", "lois_promulguees_hors_conventions"), ("baro", "lois_directes_barometre"),
                       ("senat", "lois_directes_senat_liste"), ("D", "lois_directes_deux_sources"),
                       ("U", "lois_classement_incertain")):
            w.writerow(["lois", x["session"], lab, x[k], "lois", "barometre %s ; rapports du Senat" % RELEVE])
    for s in SESSIONS:
        for k, lab in (("P", "acte_publie_identifie"), ("A", "en_attente"), ("S", "sans_objet"), ("U", "statut_incomplet")):
            w.writerow(["mesures", s, lab, r["cl"][s].get(k, 0), "mesures", "barometre, etat au %s" % RELEVE])
    for s, v, pg, _, seg in SERIE:
        w.writerow(["taux_senat", s, "segment_%d" % seg, v, "%", "Senat, %s" % pg.replace("|", " p. ")])
    w.writerow(["taux_senat", REVISION[0], "segment_5_revision", REVISION[1], "%", "Senat, %s" % REVISION[2].replace("|", " p. ")])
    return buf.getvalue()


def autotest(S: dict) -> list[str]:
    out = []

    def reclasse(m):  # 2017-1754 : appliquée après ses décrets -> « directe » au registre
        for r in m["registre"]:
            if r["num_loi"] == "2017-1754":
                r["directe_baro"] = "oui"

    def convention(m):
        for l in m["lois"][1:]:
            if l[m["lois"][0].index("Loi autorisant la ratification d'accords internationaux")] == "oui":
                l[m["lois"][0].index("Loi autorisant la ratification d'accords internationaux")] = "non"
                return

    def attente(m):
        for l in m["mesures"][1:]:
            if l[m["mesures"][0].index("État")] == "appliqué":
                l[m["mesures"][0].index("État")] = "en attente d'application"
                return

    def citation(m):
        k = "r19-523|13"
        m["pages"][k] = dict(m["pages"][k], texte=m["pages"][k]["texte"].replace("82,4 %", "84,2 %"))

    def sous_moitie(m):  # 2018-2019 : 4 lois « directes » au baromètre reclassées non directes, partout
        n = 0  # cohérente avec les effectifs annoncés, pour que seule A4 puisse la voir
        for r in m["registre"]:
            if r["session"] == "2018-2019" and r["directe_baro"] == "oui" and n < 4:
                if r["directe_senat"] == "oui":
                    m["effectifs"]["2018-2019"]["annonces"]["directe"] -= 1
                r["directe_baro"], r["directe_senat"] = "non", "non"
                n += 1
                for l in m["lois"][1:]:
                    if l[2] == r["jorf"]:
                        l[m["lois"][0].index("Loi d'application directe")] = "non"

    for nom, mut, pref in (("2017-1754 reclassee directe", reclasse, "A3"), ("convention reintegree", convention, "A2"),
                           ("mesure appliquee -> en attente", attente, "A5"), ("citation SGG alteree", citation, "A7"),
                           ("2018-2019 sous la moitie", sous_moitie, "A4")):
        m = copy.deepcopy(S)
        mut(m)
        try:
            calculer(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith(pref) or str(e).startswith("mutation"):
                raise
            out.append("%s -> %s" % (nom, str(e)[:70]))
    sauve = TR["cit_senat_1819"]  # traduction faussée : un nombre absent de l'original doit arrêter (A7 bis)
    TR["cit_senat_1819"] = sauve.replace("72%", "73%")
    try:
        calculer(S)
        raise Arret("mutation traduction faussee : aucune garde n'a mordu, controle ABSENT")
    except Arret as e:
        if not str(e).startswith("A7 bis"):
            raise
        out.append("traduction faussee -> %s" % str(e)[:70])
    finally:
        TR["cit_senat_1819"] = sauve
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
    A = affichage(r)
    A_en = affichage_en(r, A)
    if set(A) != set(A_en):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    if "--check" in sys.argv[1:]:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        figs["appliquer-mesures%s.svg" % suf] = fig_mesures(r, AA)
        figs["appliquer-lois%s.svg" % suf] = fig_lois(r, AA)
        figs["appliquer-serie%s.svg" % suf] = fig_serie(r, AA)
    LANG = "fr"
    fi = fiches(figs, A, A_en)
    csvt = csv_texte(r)
    payload = {
        "releve_le": "2026-10-06",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Assemblée nationale et LexImpact (données DILA), Sénat, "
                    "Secrétariat général du Gouvernement, Légifrance",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Appliquer, E1 à E3",
                 "sources": {"barometre": S["tetes"], "code_civil_art1": S["cciv"]["id"],
                             "senat_pages": {k: v["sha256_document"] for k, v in S["pages"].items()}},
                 "definitions": {
                     "session": "lois publiées du 1er octobre au 30 septembre suivant",
                     "directe": "loi qui n'appelle aucune mesure réglementaire d'application ; le baromètre la déduit de "
                                "son échéancier (aucune mesure autre que « sans objet »), le Sénat la classe dans ses annexes",
                     "U_lois": "lois classées différemment par les deux sources, même quand une règle explique l'écart",
                     "P": "mesure à l'état « appliqué » avec un identifiant d'acte", "A": "mesure « en attente d'application »",
                     "S": "mesure indiquée « sans objet »", "U_mesures": "mesure « appliquée » sans identifiant d'acte"},
                 "limites": "état courant seulement : aucun taux à six ou douze mois ne se calcule sans historique daté "
                            "des échéanciers ; les taux du Sénat et du Gouvernement ne se comparent pas entre eux ni d'un "
                            "segment de définition à l'autre"},
        "gardes": g,
        "calcul": {"lois": r["lignes"], "mesures": r["cl"], "total_mesures": r["tot"], "sans_objet_avec_acte": r["obs_acte"],
                   "attente_mention_differe": r["differ_A"]},
        "serie_senat": [{"session": s, "valeur": v, "document": pg, "citation": norm(c), "segment": seg,
                         "definition": SEGMENTS[seg]} for s, v, pg, c, seg in SERIE],
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
    log("Ecrit : data/promesses_appliquer.json, static/promesses_appliquer.{json,csv}, data/figures_appliquer.json, 6 figures SVG + PNG (FR, EN)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
