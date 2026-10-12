#!/usr/bin/env python3
"""Volet « Adopter » du dossier Promesses : qui dépose les lois promulguées, ce que deviennent les propositions de loi
déposées, qui fixe l'ordre du jour, qui a le dernier mot, et l'engagement de responsabilité (art. 49, al. 3).

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 2 (v2, gelée au commit
dfd0ec9). Test décisif du 06/10/2026 : test_decisif/adopter/VERDICT.md (19 mutations). Refonte du 12/10/2026 (phase B,
D:/PRO/06_PROMOTION/RECHERCHE_LYCEES_LECTURE_2026-10-09/REFONTE_PILOTE/ADOPTER/ARBITRAGE_CE_ADOPTER_PHASE_A.md, § 3).
  E2 — origine formelle, au dépôt initial, des lois promulguées, par législature de promulgation. Champ : lois
       ordinaires ; les natures exclues (traités, lois financières, organiques, constitutionnelles) sont nommées par la
       liste EXCLUES et données à part ; origine « toutes natures hors traités » calculée (la majorité parlementaire de la
       XVe dépend du champ, celle des XVIe et XVIIe non). Concordance AN / Dosleg loi par loi, aucun désaccord.
  E3 — engagements de responsabilité (art. 49, al. 3), chacun compté une fois (un même projet peut en recevoir
       plusieurs, y compris au cours d'une même lecture) ; motions liées ; lois financières
       promulguées ayant fait l'objet d'au moins un engagement (jointure par l'identifiant de dossier de l'Assemblée).
  E1 — parcours des propositions de loi déposées à l'Assemblée jusqu'à la séance, état à la fin de la législature.
       ÉCART AU PROTOCOLE DÉCLARÉ (décision de l'auteur, 06/10/2026, option 2) : le témoin des bulletins de l'AN n'est
       pas réconcilié par identifiant (test_decisif/adopter/reconciliation_e1/) ; la phrase n'est publiée que sur la
       borne du PIRE CAS, l'excès de dépôts sur les bulletins retiré et supposé sans examen.

Sources (scripts/sources_adopter/, constituées par extraire_sources.py) : registre loi par loi e2_lois.csv (JO, AN,
Dosleg, DOLE) ; e3_engagements.csv ; bulletins statistiques de l'AN (bulletins_493.csv : texte extrait ;
bulletins_depots.csv : transcrit à la main depuis l'image des pages, témoin du pire cas) ; fiche n° 64 de l'AN et
rapport n° 802 du Sénat, p. 44 (pages_temoins.json) ; fiche n° 52 de l'AN sur la recevabilité financière (septembre
2023 ; PDF archivé et son texte, an_fiche52_<sha256>.{pdf,json}, passe B3 du 12/10/2026) ; Constitution, art. 11, 24, 39, 40, 44, 45, 46, 47, 47-1, 48, 49,
50 (réponses Légifrance archivées, legifrance_<sha256>.json).

Gardes (toutes ARRÊTENT, rien n'est écrit) — elles vérifient des conditions sur les données dont dépendent les
principales phrases ; elles ne relisent pas le texte servi :
  B1  articles de la Constitution en vigueur, citations retrouvées mot pour mot (FR Légifrance, EN Conseil
      constitutionnel) ; citations des témoins ; empreinte du PDF archivé de la fiche n° 52 ;
  B2  E2 : aucun désaccord d'origine AN / Dosleg ; bornes [P - source unique ; P] ; champ : moins de la moitié sous la
      XIVe, plus de la moitié sous les XVe à XVIIe sur la borne basse, « de peu » pour la XVe ; toutes natures hors
      traités : la XVe sous la moitié (« dépend du champ »), XVIe et XVIIe au-dessus sur la borne basse ; lois
      financières et lois autorisant un traité toutes issues d'un projet ; lois « entre deux législatures » toutes
      d'origine parlementaire et du même mois ;
  B3  TÉMOINS : par session 2017-2018 à 2024-2025, nombre de lois hors traités = champ du baromètre d'Appliquer
      (autre producteur) ; 2024-2025 : 45 lois parlementaires sur 56, comme le publie le Sénat ; 2023-2024 : 58 % à
      l'unité inférieure, 59 % à l'arrondi (phrase qui explique l'écart) ;
  B8  (passe B3, 12/10/2026) unité de E3 : le compte est celui des actes (une ligne par engagement, aucun acte
      deux fois) ; au moins un couple (texte, étape) porte plusieurs engagements (PLF 2023, première lecture : 19/10 et
      02/11/2022) — sinon le libellé « un même projet peut en recevoir plusieurs, y compris au cours d'une même lecture »
      serait faux ;
  B4  E3 : engagements par législature = fiche n° 64 de l'AN ; = bulletins, session par session ; catégories de
      l'art. 49, al. 3 (contre-expertise PRO-20261006-144558, P4) ; motions adoptées ;
  B5  E1 : excès de dépôts sur les bulletins ; « plus de la moitié » sur le pire cas ; jeton Zpct seulement si son
      arrondi est celui du pire cas ; jeton « neuf sur dix » (Zdix, 12/10/2026) seulement si le dixième arrondi est le
      même pour les trois législatures closes, pire cas compris ;
  B6  (12/10/2026) toute nature et tout rattachement de e2_lois.csv est soit dans le champ, soit dans la liste des
      exclusions affichée (jeton `champ`) ; entrées == champ + exclues + entre deux législatures ;
  B7  (12/10/2026) jointure engagements / lois par dossier : un engagement classé « PLF ou PLFSS » (titre) porte sur une
      loi de nature financière (registre), un engagement « autre projet » jamais.
  Figures : parité des versions téléphone (chaque valeur dessinée figure dans la description de la version détaillée).
Autotest de mutation à chaque exécution (y compris --check) : chaque mutation doit être arrêtée par SA garde.

Bilingue (06/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés ; la Constitution se cite en
anglais dans la traduction publiée par le Conseil constitutionnel (scripts/sources_promesses_en/, garde B1) ; les autres
textes français se citent en français, suivis de notre traduction (clés *_tr). Nombres et lettres : scripts/langue_generee.py
(adopté le 12/10/2026 ; séparateur de milliers : espace insécable de l'organe commun au lieu de l'espace fine).

Écrit : data/promesses_adopter.json (+ static/), static/promesses_adopter.csv, data/figures_adopter.json,
static/img/adopter-{origine,493}{,-en}{,-m}.svg/.png. Rien n'est écrit à données identiques (fiches comprises).
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
sys.path.insert(0, str(ROOT / "scripts"))
import constitution_en as cen  # noqa: E402
import langue_generee as lg  # noqa: E402  -- nombres et lettres (organe commun)
import pied_figure  # noqa: E402  -- pied commun des figures détaillées

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
LEGS = ["14", "15", "16"]          # législatures closes
LEGS4 = LEGS + ["17"]              # XVIIe en cours au relevé
HORS = "hors législature"          # lois promulguées entre la dissolution du 9/06/2024 et la XVIIe
ROMAIN = {"14": "XIVe", "15": "XVe", "16": "XVIe", "17": "XVIIe"}
PERIODE = {"14": "2012-2017", "15": "2017-2022", "16": "2022-2024", "17": "depuis 2024"}
ROMAIN_EN = {"14": "14th", "15": "15th", "16": "16th", "17": "17th"}
PERIODE_EN = {"14": "2012-2017", "15": "2017-2022", "16": "2022-2024", "17": "since 2024"}
# Natures exclues du champ, dans l'ordre du libellé affiché (jeton `champ`) ; B6 refuse toute autre nature.
# Troisième et quatrième éléments (passe B2, 12/10/2026) : définition en quelques mots, FR et EN, pour le jeton
# `champ_def` (premier usage visible des catégories) ; une nature sans définition fait échouer le jeton.
EXCLUES = {"traite": ("lois autorisant un traité", "laws authorising a treaty",
                      "qui autorisent la France à ratifier ou approuver un accord international",
                      "which allow France to ratify or approve an international agreement"),
           "finances_fss": ("lois de finances et de financement de la sécurité sociale",
                            "finance and social security financing acts",
                            "les budgets de l'État et de la sécurité sociale",
                            "the State and social security budgets"),
           "organique": ("lois organiques", "institutional acts",
                         "prévues par la Constitution pour en préciser certaines règles",
                         "provided for by the Constitution to specify some of its rules"),
           "constitutionnelle": ("lois constitutionnelles", "constitutional acts",
                                 "qui modifient la Constitution", "which amend the Constitution")}
F11 = "legifrance_e4718a1b13a755204ea409d81c5025811a2bfb29fb5e6fae0bc10a87d19367d8.json"
F24 = "legifrance_f1e5f5212fef6ab730c4ed48b20035974af48b59ee63d13a3331e0b76eeae4fa.json"
F39 = "legifrance_751fa83fbb33037dfca31b34cb249316880035dc384b20d05a1b3e138b8df786.json"
F40 = "legifrance_f9291b41835cc8352403e4275a0e8dd814c7b9323d0378c16d32be09378a9bb1.json"
F44 = "legifrance_5ee859a43d6b1be91900d234fd312cf127cd05c7329a5f2344e19a08e8a85239.json"
F45 = "legifrance_9767001efce4060f18bf83ee36faa2520135b46643c9df910a43c3c796ee09a8.json"
F46 = "legifrance_1f70232b4cf7e1974df029784880c1046f354f517814bb2b158513c2485f5de0.json"
F47 = "legifrance_e2fae015864cb4994e10a7f7ad9779c982c55d53b650f4d4b2daab722737ef32.json"
F471 = "legifrance_74afd091f62437967e0ac556cbc0b4753a8b19d4a449da0d160ddeee232005c8.json"
F48 = "legifrance_376cbf6be973f815b0e9c33efecf371b16a12234c1193d3601a1df641c7b12bb.json"
F49 = "legifrance_8a30c40da44752bff91c17c1b15577bd338063c08a795785629c90d08ea40ccd.json"
F50 = "legifrance_eb4347955dda9a39f95486ad1c5b7491fc627b86317e679bd4716f1afa8857d1.json"
# Fiche de synthèse n° 52 de l'AN (recevabilité financière, septembre 2023), téléchargée le 12/10/2026 : PDF archivé tel
# quel et son texte (PyMuPDF, même normalisation que extraire_sources.py) ; l'empreinte du PDF est vérifiée (B1).
F52 = "an_fiche52_c81ff4441e4556c1676ef01ee1a0664afe5ad1fdda8bde1f54e6887543374c68"
CONST = {  # clé -> (fichier, citation exacte)
    "11a": (F11, "Lorsque le référendum a conclu à l'adoption du projet ou de la proposition de loi, le Président de la "
                 "République promulgue la loi dans les quinze jours qui suivent la proclamation des résultats de la "
                 "consultation."),
    "11b": (F11, "Lorsque le référendum est organisé sur proposition du Gouvernement, celui-ci fait, devant chaque "
                 "assemblée, une déclaration qui est suivie d'un débat."),
    "24": (F24, "Le Parlement vote la loi."),
    "39": (F39, "L'initiative des lois appartient concurremment au Premier ministre et aux membres du Parlement."),
    "40": (F40, "Les propositions et amendements formulés par les membres du Parlement ne sont pas recevables lorsque "
                "leur adoption aurait pour conséquence soit une diminution des ressources publiques, soit la création ou "
                "l'aggravation d'une charge publique."),
    "44c": (F44, "Si le Gouvernement le demande, l'Assemblée saisie se prononce par un seul vote sur tout ou partie du "
                 "texte en discussion en ne retenant que les amendements proposés ou acceptés par le Gouvernement."),
    "45a": (F45, "Tout projet ou proposition de loi est examiné successivement dans les deux Assemblées du Parlement en "
                 "vue de l'adoption d'un texte identique."),
    "45b": (F45, "ont la faculté de provoquer la réunion d'une commission mixte paritaire chargée de proposer un texte sur "
                 "les dispositions restant en discussion."),
    "45c": (F45, "le Gouvernement peut, après une nouvelle lecture par l'Assemblée nationale et par le Sénat, demander à "
                 "l'Assemblée nationale de statuer définitivement."),
    "45d": (F45, "Lorsque, par suite d'un désaccord entre les deux Assemblées, un projet ou une proposition de loi n'a pu "
                 "être adopté après deux lectures par chaque Assemblée ou, si le Gouvernement a décidé d'engager la "
                 "procédure accélérée sans que les Conférences des présidents s'y soient conjointement opposées, après "
                 "une seule lecture par chacune d'entre elles, le Premier ministre ou, pour une proposition de loi, les "
                 "présidents des deux assemblées agissant conjointement, ont la faculté de provoquer la réunion d'une "
                 "commission mixte paritaire chargée de proposer un texte sur les dispositions restant en discussion."),
    "45e": (F45, "Le texte élaboré par la commission mixte peut être soumis par le Gouvernement pour approbation aux deux "
                 "Assemblées. Aucun amendement n'est recevable sauf accord du Gouvernement."),
    "45f": (F45, "Si la commission mixte ne parvient pas à l'adoption d'un texte commun ou si ce texte n'est pas adopté "
                 "dans les conditions prévues à l'alinéa précédent, le Gouvernement peut, après une nouvelle lecture par "
                 "l'Assemblée nationale et par le Sénat, demander à l'Assemblée nationale de statuer définitivement."),
    "46c": (F46, "faute d'accord entre les deux assemblées, le texte ne peut être adopté par l'Assemblée nationale en "
                 "dernière lecture qu'à la majorité absolue de ses membres."),
    "46d": (F46, "Les lois organiques relatives au Sénat doivent être votées dans les mêmes termes par les deux assemblées."),
    "47c": (F47, "Si le Parlement ne s'est pas prononcé dans un délai de soixante-dix jours, les dispositions du projet "
                 "peuvent être mises en vigueur par ordonnance."),
    "471c": (F471, "Si le Parlement ne s'est pas prononcé dans un délai de cinquante jours, les dispositions du projet "
                   "peuvent être mises en oeuvre par ordonnance."),
    "48": (F48, "Deux semaines de séance sur quatre sont réservées par priorité, et dans l'ordre que le Gouvernement a "
                "fixé, à l'examen des textes et aux débats dont il demande l'inscription à l'ordre du jour."),
    "48a": (F48, "l'ordre du jour est fixé par chaque assemblée."),
    "48c": (F48, "En outre, l'examen des projets de loi de finances, des projets de loi de financement de la sécurité "
                 "sociale et, sous réserve des dispositions de l'alinéa suivant, des textes transmis par l'autre assemblée "
                 "depuis six semaines au moins, des projets relatifs aux états de crise et des demandes d'autorisation "
                 "visées à l'article 35 est, à la demande du Gouvernement, inscrit à l'ordre du jour par priorité."),
    "48e": (F48, "Un jour de séance par mois est réservé à un ordre du jour arrêté par chaque assemblée à l'initiative des "
                 "groupes d'opposition de l'assemblée intéressée ainsi qu'à celle des groupes minoritaires."),
    "49a": (F49, "Le Premier ministre peut, après délibération du Conseil des ministres, engager la responsabilité du "
                 "Gouvernement devant l'Assemblée nationale sur le vote d'un projet de loi de finances ou de financement "
                 "de la sécurité sociale. Dans ce cas, ce projet est considéré comme adopté, sauf si une motion de "
                 "censure, déposée dans les vingt-quatre heures qui suivent, est votée dans les conditions prévues à "
                 "l'alinéa précédent."),
    "49b": (F49, "Le Premier ministre peut, en outre, recourir à cette procédure pour un autre projet ou une proposition "
                 "de loi par session."),
    "49c": (F49, "Seuls sont recensés les votes favorables à la motion de censure qui ne peut être adoptée qu'à la "
                 "majorité des membres composant l'Assemblée."),
    "50": (F50, "Lorsque l'Assemblée nationale adopte une motion de censure ou lorsqu'elle désapprouve le programme ou une "
                "déclaration de politique générale du Gouvernement, le Premier ministre doit remettre au Président de la "
                "République la démission du Gouvernement."),
}
# Citations anglaises de la Constitution : traduction publiée par le Conseil constitutionnel, vérifiée par cen.citer().
CONST_EN = {
    "11a": ("11", "Where the outcome of the referendum is favourable to the Government Bill or to the Private Members' "
                  "Bill, the President of the Republic shall promulgate the resulting statute within fifteen days following "
                  "the proclamation of the results of the vote."),
    "11b": ("11", "Where the referendum is held on the recommendation of the Government, the latter shall make a statement "
                  "before each House and the same shall be followed by a debate."),
    "24": ("24", "Parliament shall pass statutes."),
    "39": ("39", "Both the Prime Minister and Members of Parliament shall have the right to initiate legislation."),
    "40": ("40", "Private Members' Bills and amendments introduced by Members of Parliament shall not be admissible where "
                 "their enactment would result in either a diminution of public revenue or the creation or increase of any "
                 "public expenditure."),
    "44c": ("44", "If the Government so requests, the House before which the Bill is tabled shall proceed to a single vote "
                  "on all or part of the text under debate, on the sole basis of the amendments proposed or accepted by the "
                  "Government."),
    "45a": ("45", "Every Government or Private Member's Bill shall be considered successively in the two Houses of Parliament "
                  "with a view to the passing of an identical text."),
    "45b": ("45", "may convene a joint committee, composed of an equal number of members from each House, to propose a text on "
                  "the provisions still under debate."),
    "45c": ("45", "the Government may, after a further reading by the National Assembly and by the Senate, ask the National "
                  "Assembly to reach a final decision."),
    "45d": ("45", "If, as a result of a failure to agree by the two Houses, it has proved impossible to pass a Government or "
                  "Private Member's Bill after two readings by each House or, if the Government has decided to apply the "
                  "accelerated procedure without the two Conferences of Presidents being jointly opposed, after a single "
                  "reading of such Bill by each House, the Prime Minister, or in the case of a Private Members' Bill, the "
                  "Presidents of the two Houses acting jointly, may convene a joint committee, composed of an equal number of "
                  "members from each House, to propose a text on the provisions still under debate."),
    "45e": ("45", "The text drafted by the joint committee may be submitted by the Government to both Houses for approval. No "
                  "amendment shall be admissible without the consent of the Government."),
    "45f": ("45", "If the joint committee fails to agree on a common text, or if the text is not passed as provided in the "
                  "foregoing paragraph, the Government may, after a further reading by the National Assembly and by the "
                  "Senate, ask the National Assembly to reach a final decision."),
    "46c": ("46", "failing agreement between the two Houses, the text may be passed by the National Assembly on a final "
                  "reading only by an absolute majority of the Members thereof."),
    "46d": ("46", "Institutional Acts relating to the Senate must be passed in identical terms by the two Houses."),
    "47c": ("47", "Should Parliament fail to reach a decision within seventy days, the provisions of the Bill may be brought "
                  "into force by Ordinance."),
    "471c": ("47-1", "Should Parliament fail to reach a decision within fifty days, the provisions of the Bill may be "
                     "implemented by Ordinance."),
    "48": ("48", "During two weeks of sittings out of four, priority shall be given, in the order determined by the Government, "
                 "to the consideration of texts and to debates which it requests to be included on the agenda."),
    "48a": ("48", "the agenda shall be determined by each House."),
    "48c": ("48", "In addition, the consideration of Finance Bills, Social Security Financing Bills and, subject to the "
                  "provisions of the following paragraph, texts transmitted by the other House at least six weeks previously, "
                  "as well as bills concerning a state of emergency and requests for authorization referred to in article "
                  "35, shall, upon Government request, be included on the agenda with priority."),
    "48e": ("48", "One day of sitting per month shall be given to an agenda determined by each House upon the initiative of "
                  "the opposition groups in the relevant House, as well as upon that of the minority groups."),
    "49a": ("49", "The Prime Minister may, after deliberation by the Council of Ministers, make the passing of a Finance Bill or "
                  "Social Security Financing Bill an issue of a vote of confidence before the National Assembly. In that event, "
                  "the Bill shall be considered passed unless a resolution of no-confidence, tabled within the subsequent "
                  "twenty-four hours, is carried as provided for in the foregoing paragraph."),
    "49b": ("49", "In addition, the Prime Minister may use the said procedure for one other Government or Private Members' Bill "
                  "per session."),
    "49c": ("49", "Solely votes cast in favour of the no-confidence resolution shall be counted and the latter shall not be "
                  "passed unless it secures a majority of the Members of the House."),
    "50": ("50", "When the National Assembly passes a resolution of no-confidence, or when it fails to endorse the Government "
                 "programme or general policy statement, the Prime Minister shall tender the resignation of the Government to "
                 "the President of the Republic."),
}
# Notre traduction des citations de témoins (fiche de l'AN, rapport du Sénat), affichée après l'original français.
TEMOINS_TR = {
    "cit_fiche64": "This instrument was nevertheless used six times, on two different bills, during the 14th legislature, once "
                   "during the 15th legislature, and 23 times during the 16th legislature.",
    "cit_censure": "The first motion tabled was carried by the required qualified majority",
    "cit_senat_origine": "Over the session, 80% of the laws adopted (45 out of 56) originated as private members' bills, against 58% in "
                         "2023-2024",
    "cit_fiche52": "The use of the plural has the effect of allowing a loss of revenue to be offset by an increase in another revenue.",
    "cit_fiche52b": "the creation or increase of a charge cannot be offset",
}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
           "December"]
SESSIONS = ["%d-%d" % (a, a + 1) for a in range(2017, 2025)]
MOTS = {"une": 1, "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
TEMOINS = {
    "cit_fiche64": ("fiche64", "Cet instrument a néanmoins été utilisé à six reprises, sur deux projets de loi différents, "
                    "sous la XIVe législature, à une reprise sous la XVe législature, et à 23 reprises sous la XVIe législature."),
    "cit_censure": ("fiche64", "La première motion déposée a été adoptée selon la majorité qualifiée requise"),
    "cit_senat_origine": ("r25-802|44", "Sur la session, 80 % des lois adoptées (45 sur 56) sont d'origine parlementaire, "
                          "contre 58 % en 2023-2024"),
    "cit_fiche52": ("fiche52", "L'emploi du pluriel a pour effet d'autoriser la compensation d'une perte de recettes par "
                    "l'augmentation d'une autre recette."),
    "cit_fiche52b": ("fiche52", "la création ou l'aggravation d'une charge ne peut être gagée"),
}
# Catégorie de l'art. 49, al. 3 : projet de loi de finances ou de financement de la sécurité sociale (rectificatives
# comprises) ; la loi de programmation des finances publiques relève de « un autre projet » (PRO-20261006-144558, P4).
FINANCIER = re.compile(r"loi de finances|financement (rectificative )?de la sécurité sociale", re.I)
LPFP = re.compile(r"programmation des finances publiques", re.I)
# Titre d'un projet de loi financier, en anglais (date de la censure) ; un titre non reconnu ARRÊTE (B4).
TITRE_EN = [(re.compile(r"^Projet de loi de financement de la sécurité sociale pour (\d{4})$"), "Social Security Financing Bill for %s"),
            (re.compile(r"^Projet de loi de finances pour (\d{4})$"), "Finance Bill for %s")]
ETAPE = {"texte de la CMP": ("texte de la commission mixte paritaire", "joint committee text"),
         "première lecture": ("première lecture", "first reading"), "nouvelle lecture": ("nouvelle lecture", "further reading"),
         "lecture définitive": ("lecture définitive", "final reading")}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def fr(n, dec=0) -> str:
    return lg.nombre(n, dec, "fr")


def en(n, dec=0) -> str:
    return lg.nombre(n, dec, "en")


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
    pages = json.loads((SRC / "pages_temoins.json").read_text(encoding="utf-8"))
    pages.update(json.loads((SRC / (F52 + ".json")).read_text(encoding="utf-8")))
    pages["fiche52"]["sha256_lu"] = hashlib.sha256((SRC / (F52 + ".pdf")).read_bytes()).hexdigest()
    return {"const": const, "lois": lire_csv(SRC / "e2_lois.csv"), "eng": lire_csv(SRC / "e3_engagements.csv"),
            "bull": lire_csv(SRC / "bulletins_493.csv"), "reg": lire_csv(REG_APPLIQUER, ";"),
            "e1": lire_csv(SRC / "e1_initiatives_extrait.csv"), "dep": lire_csv(SRC / "bulletins_depots.csv"),
            "pages": pages}


def parl(r: dict) -> bool:
    return r["origine"].startswith("parlementaire")


# ------------------------------------------------------------------ calcul et gardes
def calculer(S: dict) -> tuple[dict, list[str]]:
    g, cit = [], {}
    for k, (_, c) in CONST.items():
        if S["const"][k]["etat"] != "VIGUEUR" or norm(c) not in S["const"][k]["texte"]:
            raise Arret("B1 : Constitution art. %s : texte non en vigueur ou citation introuvable" % k)
        cit["cit_art" + k] = norm(c)
    f52 = S["pages"]["fiche52"]
    if f52["sha256_lu"] != f52["sha256_document"] or not F52.endswith(f52["sha256_document"]):
        raise Arret("B1 : fiche52 : empreinte du PDF archive %s != texte extrait %s"
                    % (f52["sha256_lu"][:12], f52["sha256_document"][:12]))
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
    if set(CONST) != set(CONST_EN):
        raise Arret("B1 : citations FR et EN : cles differentes %s" % sorted(set(CONST) ^ set(CONST_EN)))
    g.append("B1 : %d citations de la Constitution (FR Legifrance, EN Conseil constitutionnel), %d des temoins, retrouvees mot pour mot"
             % (len(CONST), len(TEMOINS)))

    # --- B6 : chaque loi est dans le champ, dans une exclusion nommée, ou entre deux législatures (12/10/2026)
    L = S["lois"]
    natures = collections.Counter(r["nature"] for r in L)
    inconnues = set(natures) - {"ordinaire"} - set(EXCLUES)
    if inconnues:
        raise Arret("B6 : nature(s) ni dans le champ ni dans les exclusions affichees : %s" % sorted(inconnues))
    ratt = collections.Counter(r["legislature"] for r in L)
    if set(ratt) - set(LEGS4) - {HORS}:
        raise Arret("B6 : rattachement(s) inconnu(s) : %s" % sorted(set(ratt) - set(LEGS4) - {HORS}))
    hors = [r for r in L if r["legislature"] == HORS]
    if any(r["nature"] != "ordinaire" for r in hors):
        raise Arret("B6 : loi entre deux legislatures hors du champ : la ligne du tableau ne la compterait pas")
    n_champ = sum(1 for r in L if r["legislature"] in LEGS4 and r["nature"] == "ordinaire")
    n_excl = sum(1 for r in L if r["legislature"] in LEGS4 and r["nature"] in EXCLUES)
    if n_champ + n_excl + len(hors) != len(L):
        raise Arret("B6 : conservation : %d entrees != %d champ + %d exclues + %d entre deux legislatures"
                    % (len(L), n_champ, n_excl, len(hors)))
    g.append("B6 : %d lois = %d du champ + %d exclues (%s) + %d entre deux legislatures"
             % (len(L), n_champ, n_excl, ", ".join("%s %d" % (k, natures[k]) for k in EXCLUES), len(hors)))

    # --- E2 (B2)
    for r in L:
        if r["origine_AN"] and r["origine_Dosleg"] and r["origine_AN"] != r["origine_Dosleg"]:
            raise Arret("B2 : %s : origine AN (%s) != Dosleg (%s)" % (r["numero"], r["origine_AN"], r["origine_Dosleg"]))
    leg = {}
    for l in LEGS4:
        o = [r for r in L if r["legislature"] == l and r["nature"] == "ordinaire"]
        c = collections.Counter(r["origine"] for r in o)
        P = c["parlementaire AN"] + c["parlementaire Sénat"]
        uniq = sum(1 for r in o if parl(r) and r["origine_source"].startswith("source unique"))
        t = [r for r in L if r["legislature"] == l and r["nature"] != "traite"]
        Pt = sum(1 for r in t if parl(r))
        Pt_u = sum(1 for r in t if parl(r) and r["origine_source"].startswith("source unique"))
        org = [r for r in L if r["legislature"] == l and r["nature"] == "organique"]
        leg[l] = {"N": len(o), "P": P, "Pmin": P - uniq, "gouv": c["gouvernement"], "AN": c["parlementaire AN"],
                  "SEN": c["parlementaire Sénat"], "traites": sum(1 for r in L if r["legislature"] == l and r["nature"] == "traite"),
                  "autres": sum(1 for r in L if r["legislature"] == l and r["nature"] not in ("ordinaire", "traite")),
                  "Ntot": len(t), "Ptot": Pt, "Ptotmin": Pt - Pt_u,
                  "Norg": len(org), "Porg": sum(1 for r in org if parl(r)),
                  "Nfin": sum(1 for r in L if r["legislature"] == l and r["nature"] == "finances_fss"),
                  "Ncst": sum(1 for r in L if r["legislature"] == l and r["nature"] == "constitutionnelle")}
        if leg[l]["N"] != leg[l]["P"] + leg[l]["gouv"]:
            raise Arret("B2 : %s : origine indeterminee ou inconnue" % l)
    fin_parl = [r["numero"] for r in L if r["nature"] == "finances_fss" and r["origine"] != "gouvernement"]
    if fin_parl:  # phrase : « les lois de finances et de financement de la sécurité sociale viennent toutes d'un projet »
        raise Arret("B2 : lois financieres d'origine parlementaire : %s" % fin_parl)
    tr_parl = [r["numero"] for r in L if r["nature"] == "traite" and r["origine"] != "gouvernement"]
    if tr_parl:  # phrase : « les lois autorisant un traité, toutes issues d'un projet »
        raise Arret("B2 : lois autorisant un traite d'origine parlementaire : %s" % tr_parl)
    x14, x15 = leg["14"], leg["15"]
    if not (2 * x14["P"] < x14["N"] and all(2 * leg[l]["Pmin"] > leg[l]["N"] for l in ("15", "16", "17"))):
        raise Arret("B2 : « moins de la moitie sous la XIVe, plus de la moitie depuis la XVe (borne basse) » faux")
    if not (2 * x15["Pmin"] - x15["N"]) <= 0.1 * x15["N"]:  # « de peu » : au plus 5 points au-dessus de la moitié
        raise Arret("B2 : XVe : « de peu » faux (%d sur %d)" % (x15["Pmin"], x15["N"]))
    if not (2 * x14["Ptot"] < x14["Ntot"] and 2 * x15["Ptot"] < x15["Ntot"]
            and all(2 * leg[l]["Ptotmin"] > leg[l]["Ntot"] for l in ("16", "17"))):
        raise Arret("B2 : toutes natures hors traites : « la majorite de la XVe depend du champ, celle des XVIe et XVIIe "
                    "non » faux (XV %d/%d, XVI %d/%d, XVII %d/%d)" % (x15["Ptot"], x15["Ntot"], leg["16"]["Ptotmin"],
                                                                   leg["16"]["Ntot"], leg["17"]["Ptotmin"], leg["17"]["Ntot"]))
    if not all(parl(r) for r in hors) or len({r["date_promulgation"][:7] for r in hors}) != 1:
        raise Arret("B2 : lois entre deux legislatures : « toutes d'origine parlementaire, promulguees le meme mois » faux")
    hl = {"N": len(hors), "P": sum(1 for r in hors if parl(r)), "AN": sum(1 for r in hors if r["origine"] == "parlementaire AN"),
          "SEN": sum(1 for r in hors if r["origine"] == "parlementaire Sénat"), "gouv": 0,
          "mois": hors[0]["date_promulgation"][:7], "numeros": sorted(r["numero"] for r in hors)}
    g.append("B2 : origine concordante AN/Dosleg ; champ XIV %d/%d, XV %d-%d/%d, XVI %d/%d, XVII %d/%d ; toutes natures hors "
             "traites XIV %d/%d, XV %d/%d, XVI %d/%d, XVII %d/%d ; %d lois entre deux legislatures"
             % (x14["P"], x14["N"], x15["Pmin"], x15["P"], x15["N"], leg["16"]["P"], leg["16"]["N"], leg["17"]["P"],
                leg["17"]["N"], x14["Ptot"], x14["Ntot"], x15["Ptot"], x15["Ntot"], leg["16"]["Ptot"], leg["16"]["Ntot"],
                leg["17"]["Ptot"], leg["17"]["Ntot"], len(hors)))

    # --- témoins par session (autre producteur pour le champ ; publication du Sénat pour l'origine)
    regN = collections.Counter(r["session"] for r in S["reg"])
    ses = {}
    for s in SESSIONS:
        o = [r for r in L if r["nature"] != "traite" and r["legislature"] != "" and session(r["date_promulgation"]) == s]
        ses[s] = {"N": len(o), "P": sum(1 for r in o if parl(r))}
        if ses[s]["N"] != regN[s]:
            raise Arret("B3 : session %s : %d lois hors traites ici, %d au barometre (Appliquer)" % (s, ses[s]["N"], regN[s]))
    if (ses["2024-2025"]["P"], ses["2024-2025"]["N"]) != (45, 56) or "(45 sur 56)" not in cit["cit_senat_origine"]:
        raise Arret("B3 : 2024-2025 : %d/%d contre 45 sur 56 publies par le Senat" % (ses["2024-2025"]["P"], ses["2024-2025"]["N"]))
    p2324 = 100 * ses["2023-2024"]["P"] / ses["2023-2024"]["N"]
    if not (int(p2324) == 58 and round(p2324) != 58):  # phrase : « le Sénat écrit 58 % ; arrondi, le tableau donne 59 % »
        raise Arret("B3 : 2023-2024 : %.1f %% : « 58 % a l'unite inferieure, autre valeur a l'arrondi » faux" % p2324)
    g.append("B3 : champ par session = barometre (8 sessions) ; 2024-2025 45/56 = Senat ; 2023-2024 %d/%d = %.1f %%"
             % (ses["2023-2024"]["P"], ses["2023-2024"]["N"], p2324))

    # --- B8 (passe B3, 12/10/2026) : unité de E3. Le compte est celui des actes ; un même projet peut recevoir plusieurs
    # engagements au cours d'une même lecture (libellé des figures, des fiches et des définitions).
    E = S["eng"]
    actes = collections.Counter((r["dossier_texte"], r["etape"], r["date"]) for r in E)
    doubles = sorted(k for k, v in actes.items() if v > 1)
    if doubles:
        raise Arret("B8 : acte(s) compte(s) deux fois : %s" % doubles[:3])
    if sum(1 for r in E if r["legislature"] in LEGS4) != len(E):
        raise Arret("B8 : engagement(s) hors des legislatures comptees")
    couples = collections.Counter((r["dossier_texte"], r["etape"]) for r in E)
    plusieurs = sorted(k for k, v in couples.items() if v > 1)
    if not plusieurs:
        raise Arret("B8 : aucun couple (texte, etape) a plusieurs engagements : « un meme projet peut en recevoir plusieurs, "
                    "y compris au cours d'une meme lecture » faux")
    plf23 = sorted(r["date"] for r in E if r["titre"] == "Projet de loi de finances pour 2023" and r["etape"] == "première lecture")
    g.append("B8 : %d engagements = %d actes distincts ; %d couples (texte, etape) a plusieurs engagements, dont PLF 2023 en "
             "premiere lecture (%s)" % (len(E), len(actes), len(plusieurs), ", ".join(plf23)))

    # --- E3 (B4)
    eng = {}
    for l in LEGS4:
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
    for l in LEGS4:  # sur la période couverte par les bulletins (XVIIe : jusqu'au 30/09/2025)
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
    adoptees_bull = {l: sum(int(r["motions_493_adoptees"] or 0) for r in B if r["legislature"] == l) for l in LEGS4}
    if any(adoptees_bull[l] for l in LEGS) or adoptees_bull["17"] != 1:
        raise Arret("B4 : motions adoptees aux bulletins : %s" % adoptees_bull)
    cens = [r for r in E if int(r["motions_adoptees"] or 0) > 0]
    if len(cens) != 1 or cens[0]["legislature"] != "17":
        raise Arret("B4 : engagements suivis d'une motion adoptee : %d" % len(cens))
    an, mo, jo = map(int, cens[0]["date"].split("-"))
    cit["censure_date"] = "%d%s %s %d" % (jo, "er" if jo == 1 else "", MOIS[mo - 1], an)
    cit["en_censure_date"] = "%d %s %d" % (jo, MOIS_EN[mo - 1], an)
    titre_en = None
    for rx, mod in TITRE_EN:
        mm = rx.match(cens[0]["titre"])
        if mm:
            titre_en = mod % mm.group(1)
    if not titre_en or cens[0]["etape"] not in ETAPE:
        raise Arret("B4 : texte ou etape de l'engagement censure non reconnu : %s / %s" % (cens[0]["titre"], cens[0]["etape"]))
    cit["censure_texte"] = cens[0]["titre"][0].lower() + cens[0]["titre"][1:]
    cit["en_censure_texte"] = "the " + titre_en
    cit["censure_etape"], cit["en_censure_etape"] = ETAPE[cens[0]["etape"]]
    g.append("B4 : engagements XIV %d, XV %d, XVI %d (= fiche 64 et bulletins) ; XVI %d PLF/PLFSS + %d LPFP ; 0 motion adoptee XIV-XVI"
             % (eng["14"]["n"], eng["15"]["n"], eng["16"]["n"], eng["16"]["fin"], eng["16"]["lpfp"]))

    # --- B7 : lois financières promulguées ayant fait l'objet d'au moins un engagement (jointure par dossier AN)
    dossier_loi = {}
    for r in L:
        for d in filter(None, r["dossiers_AN"].split("|")):
            dossier_loi.setdefault(d, []).append(r)
    for r in E:
        lois = dossier_loi.get(r["dossier_texte"], [])
        if FINANCIER.search(r["titre"]) and any(x["nature"] != "finances_fss" for x in lois):
            raise Arret("B7 : engagement du %s classe PLF/PLFSS sur une loi d'une autre nature (%s)"
                        % (r["date"], [x["numero"] for x in lois]))
        if not FINANCIER.search(r["titre"]) and any(x["nature"] == "finances_fss" for x in lois):
            raise Arret("B7 : engagement du %s classe « autre projet » sur une loi financiere (%s)"
                        % (r["date"], [x["numero"] for x in lois]))
    engages = {r["dossier_texte"] for r in E}
    for l in LEGS4:
        fl = [r for r in L if r["legislature"] == l and r["nature"] == "finances_fss"]
        avec = sorted(r["numero"] for r in fl if set(filter(None, r["dossiers_AN"].split("|"))) & engages)
        eng[l].update({"lois_fin": len(fl), "lois_fin_engagees": len(avec), "lois_fin_engagees_numeros": avec})
    if any(eng[l]["lois_fin_engagees"] for l in ("14", "15")):  # phrase : aucune loi financière concernée sous XIVe et XVe
        raise Arret("B7 : loi financiere avec engagement sous la XIVe ou la XVe")
    g.append("B7 : lois financieres avec au moins un engagement (jointure par dossier) : XVI %d/%d, XVII %d/%d ; classements "
             "titre/nature concordants" % (eng["16"]["lois_fin_engagees"], eng["16"]["lois_fin"], eng["17"]["lois_fin_engagees"],
                                         eng["17"]["lois_fin"]))

    # --- E1 (B5 ; écart au protocole déclaré : borne du pire cas)
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
    dix = {round(10 * x[k1] / x[k2]) for x in e1.values() for k1, k2 in (("Z", "N"), ("Zw", "Nw"))}
    if len(dix) != 1:  # jeton « neuf sur dix » : un seul dixième arrondi, trois législatures, pire cas compris
        raise Arret("B5 : dixieme arrondi non unique (%s) : « environ N sur dix » faux pour une legislature ou son pire cas"
                    % sorted(dix))
    for l, x in e1.items():
        if round(100 * x["Z"] / x["N"]) != round(100 * x["Zw"] / x["Nw"]):
            raise Arret("B5 : %s : part sans examen %d/%d et pire cas %d/%d : arrondis differents" % (l, x["Z"], x["N"], x["Zw"], x["Nw"]))
    for l, x in e1.items():  # phrase : « plus de cinq fois plus de propositions que de projets » (bulletins, 12/10/2026)
        x["pjl_bul"] = sum(int(r["pjl_an_premiere_lecture"]) for r in S["dep"] if r["legislature"] == l)
        if not x["bul"] > 5 * x["pjl_bul"]:
            raise Arret("B5 : %s : %d propositions et %d projets aux bulletins : « plus de cinq fois plus » faux" % (l, x["bul"], x["pjl_bul"]))
    if not 2 * e1["16"]["mediane_jours"] < e1["14"]["mediane_jours"]:  # « plus de deux fois plus court »
        raise Arret("B5 : duree mediane XVIe pas deux fois plus courte que XIVe")
    g.append("B5 : E1 pire cas XIV %d/%d, XV %d/%d, XVI %d/%d (exces sur bulletins %d, %d, %d) ; dixieme unique %d"
             % (tuple(v for l in LEGS for v in (e1[l]["Zw"], e1[l]["Nw"])) + tuple(e1[l]["exces"] for l in LEGS) + (dix.pop(),)))
    dixieme = round(10 * e1["14"]["Z"] / e1["14"]["N"])
    return {"leg": leg, "hl": hl, "ses": ses, "eng": eng, "e1": e1, "cit": cit, "dix": dixieme}, g


def pct(a, b) -> float:
    return 100 * a / b


def affichage(r: dict, lang: str) -> dict:
    N = (lambda v, d=0: lg.nombre(v, d, lang))
    A = {"releve": RELEVE if lang == "fr" else "6 October 2026"}
    for l, x in r["leg"].items():
        A.update({"N%s" % l: N(x["N"]), "P%s" % l: N(x["P"]), "Pmin%s" % l: N(x["Pmin"]), "G%s" % l: N(x["gouv"]),
                  "AN%s" % l: N(x["AN"]), "SEN%s" % l: N(x["SEN"]), "T%s" % l: N(x["traites"]),
                  "Ppct%s" % l: N(pct(x["P"], x["N"])), "Pminpct%s" % l: N(pct(x["Pmin"], x["N"])),
                  "Ntot%s" % l: N(x["Ntot"]), "Ptot%s" % l: N(x["Ptot"]), "Ptotpct%s" % l: N(pct(x["Ptot"], x["Ntot"])),
                  "Norg%s" % l: N(x["Norg"]), "Porg%s" % l: N(x["Porg"]), "Nfin%s" % l: N(x["Nfin"])})
    for l, x in r["eng"].items():
        A.update({"E%s" % l: N(x["n"]), "Efin%s" % l: N(x["fin"]), "Etextes%s" % l: N(x["textes"]),
                  "Eautre%s" % l: N(x["n"] - x["fin"]), "Lfin%s" % l: N(x["lois_fin"]), "Lfineng%s" % l: N(x["lois_fin_engagees"]),
                  "Efois%s" % l: (N(x["n"]) + " fois") if lang == "fr" else {1: "once", 2: "twice"}.get(x["n"], N(x["n"]) + " times")})
    for l, x in r["e1"].items():
        A.update({"Z%s" % l: N(x["Z"]), "NZ%s" % l: N(x["N"]), "Zpct%s" % l: N(pct(x["Z"], x["N"])), "Zw%s" % l: N(x["Zw"]),
                  "Nw%s" % l: N(x["Nw"]), "exces%s" % l: N(x["exces"]), "bul%s" % l: N(x["bul"]), "ext%s" % l: N(x["ext"]),
                  "med%s" % l: N(x["mediane_jours"]), "pjl%s" % l: N(x["pjl_bul"])})
    A["Zdix"] = lg.lettres(r["dix"], lang)  # « environ neuf propositions sur dix » / "about nine in ten"
    hl = r["hl"]
    an, mo = map(int, hl["mois"].split("-"))
    A.update({"HLn": lg.lettres(hl["N"], lang), "HLmois": ("%s %d" % (MOIS[mo - 1], an)) if lang == "fr" else "%s %d" % (MOIS_EN[mo - 1], an),
              "champ": ("hors " if lang == "fr" else "excluding ") + lg.enumere([v[0 if lang == "fr" else 1] for v in EXCLUES.values()], lang),
              "champ_def": lg.enumere(["%s (%s)" % ((v[0], v[2]) if lang == "fr" else (v[1], v[3])) for v in EXCLUES.values()], lang)})
    s1, s2, s3 = r["ses"]["2017-2018"], r["ses"]["2024-2025"], r["ses"]["2023-2024"]
    A.update({"s1718_P": N(s1["P"]), "s1718_N": N(s1["N"]), "s2425_P": N(s2["P"]), "s2425_N": N(s2["N"]),
              "s2324_P": N(s3["P"]), "s2324_N": N(s3["N"]), "s2324_pct": N(pct(s3["P"], s3["N"]), 1),
              "s2324_arr": N(pct(s3["P"], s3["N"]))})
    if lang == "fr":
        A["releve_le"] = ("06/10/2026 (données de l'Assemblée nationale et base Dosleg du Sénat du 06/10/2026, Journal "
                          "officiel ; bulletins statistiques de l'Assemblée nationale)")
        A.update({k: v for k, v in r["cit"].items() if not k.startswith("en_")})
    else:
        A["releve_le"] = ("6 October 2026 (National Assembly open data and the Senate's Dosleg database of 6 October 2026, "
                          "Journal officiel; National Assembly statistical bulletins)")
        for k, v in r["cit"].items():
            if k.startswith("en_"):
                continue
            if k.startswith("cit_art") or k.startswith("censure_"):
                A[k] = r["cit"]["en_" + k]
            else:
                A[k] = v  # citation de témoin : l'original français, suivi de sa traduction (_tr)
    A.update({k + "_tr": v for k, v in TEMOINS_TR.items()})
    return A


def tableaux(r: dict, lang: str) -> dict:
    N = (lambda v, d=0: lg.nombre(v, d, lang))
    fr_ = lang == "fr"
    R, PER = (ROMAIN, PERIODE) if fr_ else (ROMAIN_EN, PERIODE_EN)
    pc = (lambda v: N(v) + ("\u00a0%" if fr_ else "%"))

    def nomleg(l):
        if fr_:
            return R[l] + " (" + PER[l] + (", en cours au " + RELEVE if l == "17" else "") + ")"
        return R[l] + " legislature (" + PER[l] + (", ongoing on 6 October 2026" if l == "17" else "") + ")"

    def part(P, Pmin, n):
        s = pc(pct(P, n))
        return s if Pmin == P else s + (" (au moins %s)" % pc(pct(Pmin, n)) if fr_ else " (at least %s)" % pc(pct(Pmin, n)))

    lois = [[nomleg(l), N(x["N"]), N(x["gouv"]), N(x["AN"]), N(x["SEN"]),
             N(x["P"]) + ("" if x["Pmin"] == x["P"] else (" (au moins %s)" if fr_ else " (at least %s)") % N(x["Pmin"])),
             part(x["P"], x["Pmin"], x["N"])] for l, x in r["leg"].items()]
    hl = r["hl"]
    an, mo = map(int, hl["mois"].split("-"))
    lois.append([("Entre deux législatures (%s %d)" % (MOIS[mo - 1], an)) if fr_ else "Between two legislatures (%s %d)" % (MOIS_EN[mo - 1], an),
                 N(hl["N"]), N(hl["gouv"]), N(hl["AN"]), N(hl["SEN"]), N(hl["P"]), pc(pct(hl["P"], hl["N"]))])
    nat = [[R[l] + ((" (en cours)" if fr_ else " (ongoing)") if l == "17" else ""), N(x["Ntot"]),
            N(x["Ptot"]) + ("" if x["Ptotmin"] == x["Ptot"] else (" (au moins %s)" if fr_ else " (at least %s)") % N(x["Ptotmin"])),
            pc(pct(x["Ptot"], x["Ntot"])), N(x["Nfin"]), "%s / %s" % (N(x["Norg"]), N(x["Porg"])), N(x["Ncst"]), N(x["traites"])]
           for l, x in r["leg"].items()]
    ses = [[s, N(x["N"]), N(x["P"]), pc(pct(x["P"], x["N"]))] for s, x in r["ses"].items()]
    sur = " sur " if fr_ else " out of "
    eng = [[R[l] + ((" (en cours)" if fr_ else " (ongoing)") if l == "17" else ""), N(x["n"]), N(x["textes"]), N(x["fin"]),
            N(x["n"] - x["fin"]), N(x["adoptees"]), N(x["lois_fin_engagees"]) + sur + N(x["lois_fin"])]
           for l, x in r["eng"].items()]
    e1 = [[R[l] + " (" + PER[l] + ")", N(x["N"]), N(x["Z"]), N(x["Zw"]) + sur + N(x["Nw"]),
           "%s / %s" % (N(x["ext"]), N(x["bul"])), N(x["mediane_jours"])] for l, x in r["e1"].items()]
    if fr_:
        return {
            "lois": {"entetes": ["Législature de promulgation", "Lois du champ", "Projet du Gouvernement",
                                 "Proposition déposée à l'Assemblée", "Proposition déposée au Sénat", "Origine parlementaire",
                                 "Part d'origine parlementaire"], "lignes": lois},
            "natures": {"entetes": ["Législature", "Lois promulguées, toutes natures hors traités", "D'origine parlementaire",
                                    "Part", "dont lois de finances et de financement de la sécurité sociale (toutes d'un projet)",
                                    "dont lois organiques : total / d'origine parlementaire", "dont loi constitutionnelle",
                                    "Lois autorisant un traité (hors de tout calcul)"], "lignes": nat},
            "sessions": {"entetes": ["Session", "Lois promulguées hors traités", "D'origine parlementaire", "Part"], "lignes": ses},
            "engagements": {"entetes": ["Législature", "Engagements (art. 49, al. 3)", "Textes distincts",
                                        "Sur un projet de loi de finances ou de financement de la sécurité sociale",
                                        "Sur un autre projet ou une proposition", "Motions de censure adoptées",
                                        "Lois de finances et de financement de la sécurité sociale promulguées avec au moins un engagement"],
                            "lignes": eng},
            "e1": {"entetes": ["Législature de dépôt", "Propositions de loi ordinaires déposées à l'Assemblée",
                               "Sans examen en séance retrouvé dans les données de l'Assemblée avant la fin de la législature",
                               "Pire cas : excès sur les bulletins retiré", "Dépôts de propositions : données / bulletins",
                               "Durée médiane entre dépôt et fin de législature (jours)"], "lignes": e1},
        }
    return {
        "lois": {"entetes": ["Legislature of promulgation", "Laws in the scope", "Government bill",
                             "Private member's bill tabled in the Assembly", "Private member's bill tabled in the Senate",
                             "Parliamentary origin", "Share of parliamentary origin"], "lignes": lois},
        "natures": {"entetes": ["Legislature", "Laws promulgated, all kinds except treaties", "Of parliamentary origin", "Share",
                                "of which finance and social security financing acts (all from a government bill)",
                                "of which institutional acts: total / of parliamentary origin", "of which constitutional act",
                                "Laws authorising a treaty (outside every count)"], "lignes": nat},
        "sessions": {"entetes": ["Session", "Laws promulgated, excluding treaties", "Of parliamentary origin", "Share"], "lignes": ses},
        "engagements": {"entetes": ["Legislature", "Uses of art. 49, para. 3", "Distinct bills",
                                    "On a Finance Bill or Social Security Financing Bill", "On another bill",
                                    "Motions of no confidence carried",
                                    "Finance and social security financing acts promulgated with at least one use"], "lignes": eng},
        "e1": {"entetes": ["Legislature of tabling", "Ordinary private members' bills tabled first in the Assembly",
                           "No plenary debate found in the Assembly's data before the end of the legislature",
                           "Worst case: excess over the bulletins removed", "Bills tabled: data / bulletins",
                           "Median time from tabling to end of legislature (days)"], "lignes": e1},
    }


# ------------------------------------------------------------------ figures
W = 720
WM, FS_MIN = 300, 13.5
BLEU, BLEU_CLAIR, GRIS, GRIS_CLAIR = "#184f95", "#7fa3cf", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCES_M = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
              "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
LANG = "fr"


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None, cls=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    c = ' class="%s"' % cls if cls else ""
    return '<text%s x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>' % (c, x, y, size, fill, anchor, w, esc(s))


def cadre(H, ident, titre, sous, desc) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H + 48, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def pied(e, y0, source, note) -> str:
    return pied_figure.pied(e, y0, W, [(source, INK2, "pied-source"), (note, INK2, "pied-note"),
                                       (LICENCES[LANG], MUTED, "pied-licence")], GRID)


def triangle(x, y, s=6) -> str:
    return '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (x, y, x - s, y + s * 1.4, x + s, y + s * 1.4, INK)


T = {
    "fr": {"src1": "Assemblée nationale (données ouvertes, dossiers législatifs) et Sénat (base Dosleg), 06/10/2026 ; Journal officiel",
           "note1": "Champ : lois promulguées, {champ}. Origine au dépôt initial, non l'influence. Toutes natures : même compte, "
                    "lois organiques, financières et constitutionnelles réintégrées, traités toujours exclus.",
           "src2": "Assemblée nationale : dossiers législatifs, bulletins statistiques, fiche n° 64 (engagements de responsabilité)",
           "note2": "Catégories de l'art. 49, al. 3 : la loi de programmation des finances publiques est un « autre projet ». "
                    "Chaque engagement est compté une fois ; un même projet peut en recevoir plusieurs, y compris au cours "
                    "d'une même lecture. XVIIe en cours au " + RELEVE + ".",
           "t1": "Qui est à l'origine des lois promulguées ?",
           "s1": "part des lois du champ étudié, par législature de promulgation ; pointillés : la moitié",
           "l1": ["proposition déposée à l'Assemblée", "proposition déposée au Sénat", "projet du Gouvernement"],
           "bb": "borne basse : origine établie par les deux sources",
           "au_moins": "(au moins {})", "toutes": "toutes natures : {}", "moitie": "moitié",
           "encours": "* en cours au " + RELEVE, "pc": "{}\u00a0%",
           "t2": "Engagements de responsabilité sur un texte (art. 49, al. 3)",
           "s2": "nombre d'engagements, par législature ; chaque engagement est compté une fois",
           "l2": ["projet de loi de finances ou de financement de la sécurité sociale", "autre projet ou proposition"],
           "eng": ("engagement", "engagements"), "texte": ("texte", "textes"), "sur": "sur",
           "dont": "dont {} sur un projet de loi de finances ou de financement de la sécurité sociale",
           "tous": "tous sur un projet de loi de finances ou de financement de la sécurité sociale",
           "aucun": "aucun sur un projet de loi de finances ou de financement de la sécurité sociale",
           "motion": ("motion de censure adoptée", "motions de censure adoptées")},
    "en": {"src1": "National Assembly (open data, legislative files) and Senate (Dosleg database), 6 October 2026; Journal officiel",
           "note1": "Scope: laws promulgated, {champ}. Origin at the initial tabling, not influence. All kinds: same count with "
                    "institutional, finance and constitutional acts put back in, treaties still excluded.",
           "src2": "National Assembly: legislative files, statistical bulletins, summary sheet no. 64 (Government responsibility)",
           "note2": "Categories of art. 49, para. 3: the public finance programming act is 'one other bill'. Each use of "
                    "Article 49(3) is counted once; the same bill may be subject to several uses, including during the same "
                    "reading. 17th ongoing on 6 October 2026.",
           "t1": "Who initiated the laws promulgated in France?",
           "s1": "share of the laws in the scope studied, by legislature of promulgation; dotted line: half",
           "l1": ["private member's bill, National Assembly", "private member's bill, Senate", "Government bill"],
           "bb": "lower bound: origin established by both sources",
           "au_moins": "(at least {})", "toutes": "all kinds: {}", "moitie": "half",
           "encours": "* ongoing on 6 October 2026", "pc": "{}%",
           "t2": "Uses of Article 49(3) on bills",
           "s2": "number of uses, by legislature; each use is counted once",
           "l2": ["Finance Bill or Social Security Financing Bill", "other bill"],
           "eng": ("use", "uses"), "texte": ("bill", "bills"), "sur": "on",
           "dont": "{} of them on a Finance Bill or Social Security Financing Bill",
           "tous": "all on a Finance Bill or Social Security Financing Bill",
           "aucun": "none on a Finance Bill or Social Security Financing Bill",
           "motion": ("motion of no confidence carried", "motions of no confidence carried")},
}


def lib_leg(l: str) -> str:
    R, P = (ROMAIN_EN, PERIODE_EN) if LANG == "en" else (ROMAIN, PERIODE)
    return R[l] + " (" + P[l] + ")" + (" *" if l == "17" else "")


def nb(n, d=0) -> str:
    return lg.nombre(n, d, LANG)


def pc(v) -> str:
    return T[LANG]["pc"].format(nb(v))


def nombre_mot(n, mots) -> str:
    """« 1 engagement », « 23 engagements » (chiffres : ce sont des valeurs de figure)."""
    sing = n in (0, 1) if LANG == "fr" else n == 1
    return nb(n) + " " + (mots[0] if sing else mots[1])


def lignes_origine(l, x) -> list[str]:
    """Valeurs d'une législature, en clair (description de la figure détaillée ET lignes de la version téléphone)."""
    if LANG == "fr":
        out = ["%s d'origine parlementaire (%s lois sur %s)" % (pc(pct(x["P"], x["N"])), nb(x["P"]), nb(x["N"]))]
        if x["Pmin"] != x["P"]:
            out.append("au moins %s (%s lois)" % (pc(pct(x["Pmin"], x["N"])), nb(x["Pmin"])))
        out.append("toutes natures : %s (%s sur %s)" % (pc(pct(x["Ptot"], x["Ntot"])), nb(x["Ptot"]), nb(x["Ntot"])))
    else:
        out = ["%s of parliamentary origin (%s laws out of %s)" % (pc(pct(x["P"], x["N"])), nb(x["P"]), nb(x["N"]))]
        if x["Pmin"] != x["P"]:
            out.append("at least %s (%s laws)" % (pc(pct(x["Pmin"], x["N"])), nb(x["Pmin"])))
        out.append("all kinds: %s (%s out of %s)" % (pc(pct(x["Ptot"], x["Ntot"])), nb(x["Ptot"]), nb(x["Ntot"])))
    return out


def desc_origine(r) -> str:
    L = T[LANG]
    tete = ("Barres à 100 % par législature de promulgation, champ étudié : part des lois issues d'une proposition déposée "
            "à l'Assemblée, d'une proposition déposée au Sénat, d'un projet du Gouvernement ; des pointillés marquent la "
            "moitié, un triangle la borne basse. " if LANG == "fr" else
            "100% bars by legislature of promulgation, scope studied: share of the laws arising from a private member's bill "
            "tabled in the National Assembly, from one tabled in the Senate, from a Government bill; a dotted line marks half, "
            "a triangle the lower bound. ")
    sep, j = (" : ", " ; ") if LANG == "fr" else (": ", "; ")
    parts = [lib_leg(l).replace(" *", ", en cours" if LANG == "fr" else ", ongoing") + sep + j.join(lignes_origine(l, x))
             for l, x in r["leg"].items()]
    _ = L
    return tete + (". " if LANG == "fr" else ". ").join(parts) + "."


def lignes_493(l, x) -> list[str]:
    L = T[LANG]
    out = ["%s %s %s" % (nombre_mot(x["n"], L["eng"]), L["sur"], nombre_mot(x["textes"], L["texte"]))]
    if x["fin"] == 0:
        out.append(L["aucun"])
    elif x["fin"] == x["n"]:
        out.append(L["tous"])
    else:
        out.append(L["dont"].format(nb(x["fin"])))
    if x["adoptees"]:
        out.append(nombre_mot(x["adoptees"], L["motion"]))
    return out


def desc_493(r) -> str:
    tete = ("Barres horizontales par législature : engagements sur un projet de loi de finances ou de financement de la "
            "sécurité sociale, et sur un autre projet ou une proposition. " if LANG == "fr" else
            "Horizontal bars by legislature: uses on a Finance Bill or Social Security Financing Bill, and on another bill. ")
    sep = " : " if LANG == "fr" else ": "
    parts = [lib_leg(l).replace(" *", ", en cours" if LANG == "fr" else ", ongoing") + sep + ", ".join(lignes_493(l, x))
             for l, x in r["eng"].items()]
    return tete + (" ; " if LANG == "fr" else "; ").join(parts) + "."


def fig_origine(r: dict, A: dict) -> str:
    L = T[LANG]
    x0, x1, y0, pas = 150, W - 178, 84, 50
    H = y0 + 4 * pas + 40
    X = lambda v: x0 + v * (x1 - x0)  # noqa: E731
    e = cadre(H, "ao", L["t1"], L["s1"], desc_origine(r))
    x = 0
    for col, lab in zip((BLEU, BLEU_CLAIR, GRIS_CLAIR), L["l1"]):
        e.append('<rect x="%d" y="%d" width="11" height="11" fill="%s"/>' % (x, 49, col))
        e.append(txt(x + 16, 58, lab, 10, INK2))
        x += 16 + 5.6 * len(lab) + 16
    for i, (l, xx) in enumerate(r["leg"].items()):
        y = y0 + i * pas
        e.append(txt(0, y + 15, lib_leg(l), 10, INK))
        a = 0
        for v, col in ((xx["AN"], BLEU), (xx["SEN"], BLEU_CLAIR), (xx["gouv"], GRIS_CLAIR)):
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s"/>' % (X(a / xx["N"]), y, X((a + v) / xx["N"]) - X(a / xx["N"]), col))
            a += v
        if xx["Pmin"] != xx["P"]:
            e.append(triangle(X(xx["Pmin"] / xx["N"]), y + 23))
        e.append(txt(x1 + 8, y + 10, pc(pct(xx["P"], xx["N"])) + ("" if xx["Pmin"] == xx["P"] else " " + L["au_moins"].format(pc(pct(xx["Pmin"], xx["N"])))),
                     10.5, INK, weight="600"))
        e.append(txt(x1 + 8, y + 24, L["toutes"].format(pc(pct(xx["Ptot"], xx["Ntot"]))), 10, INK2))
    ybas = y0 + 4 * pas - 18
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>'
             % (X(0.5), y0 - 8, X(0.5), ybas, INK))
    for v in (0, 0.5, 1):
        e.append(txt(X(v), ybas + 12, pc(100 * v), 9, MUTED, "middle"))
    e.append(triangle(6, ybas + 22, 5))
    e.append(txt(16, ybas + 31, L["bb"], 9.5, INK2))
    e.append(txt(x1 + 8, ybas + 31, L["encours"], 9.5, INK2))
    return pied(e, H + 2, L["src1"], L["note1"].format(champ=A["champ"]))


def fig_493(r: dict, A: dict) -> str:
    L = T[LANG]
    x0, x1, y0, pas = 150, W - 40, 74, 58
    H = y0 + 4 * pas + 24
    vmax = 25
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    e = cadre(H, "a4", L["t2"], L["s2"], desc_493(r))
    x = 0
    for col, lab in zip((BLEU, GRIS_CLAIR), L["l2"]):
        e.append('<rect x="%d" y="%d" width="11" height="11" fill="%s"/>' % (x, 49, col))
        e.append(txt(x + 16, 58, lab, 10, INK2))
        x += 16 + 5.6 * len(lab) + 16
    for v in range(0, vmax + 1, 5):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 4 - 10, GRID))
        e.append(txt(X(v), y0 + pas * 4 + 2, str(v), 9, MUTED, "middle"))
    for i, (l, x) in enumerate(r["eng"].items()):
        y = y0 + i * pas
        e.append(txt(0, y + 13, lib_leg(l), 10, INK))
        a = 0
        for v, col in ((x["fin"], BLEU), (x["n"] - x["fin"], GRIS_CLAIR)):
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="18" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append(txt(X(a) + 4, y + 13, nb(x["n"]), 10, INK, weight="600"))
        for k, ligne in enumerate(coupe(" · ".join(lignes_493(l, x)), 104)):
            e.append(txt(x0, y + 31 + 12 * k, ligne, 9.5, INK2))
    e.append(txt(0, y0 + pas * 4 + 16, L["encours"], 9, INK2))
    return pied(e, H + 2, L["src2"], L["note2"])


# ------------------------------------------------------------------ figures téléphone (phase B, 12/10/2026)
# Composées pour 300 px de large, jamais rétrécies : police >= FS_MIN ; chaque valeur dessinée (classe « val ») doit
# figurer dans la description de la version détaillée (parite_mobile). Patron : scripts/update_promesses_delais.py.
def coupe(s, n):
    """Coupe aux espaces ordinaires ; ponctuation haute, « n° » et nombre + unité soudés (règle typographique du site)."""
    s = re.sub(r" ([:;?!»%])", "\u00a0\\1", s).replace("« ", "«\u00a0").replace("n° ", "n°\u00a0")
    s = re.sub(r"\b(art\.|al\.|no\.|para\.) (\d)", "\\1\u00a0\\2", s)
    s = re.sub(r"(\d) (January|February|March|April|May|June|July|August|September|October|November|December)\b",
               "\\1\u00a0\\2", s)
    out, cur = [], ""
    for mot in s.split(" "):
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
        e.append(txt(0, 20 + 22 * k, ligne, 17, INK, weight="600"))
    return e, 20 + 22 * len(lignes)


def finir_m(e, y0, source, note):
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, WM, y0, GRID))
    y = y0 + 4
    for tx, col, cls in ((source, INK2, "pied-source"), (note, INK2, "pied-note"), (LICENCES_M[LANG], MUTED, "pied-licence")):
        for ligne in coupe(tx, 38):
            y += 17
            e.append(txt(0, y, ligne, FS_MIN, col, cls=cls))
        y += 4
    e.append("</svg>")
    h = y + 6
    s = "\n".join(e)
    return s.replace('viewBox="0 0 %d 0"' % WM, 'viewBox="0 0 %d %d"' % (WM, h), 1).replace(
        '<rect width="%d" height="0"' % WM, '<rect width="%d" height="%d"' % (WM, h), 1)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg).group(1))


def legende_m(e, y, items):
    for col, lab in items:
        lignes = coupe(lab, 32)
        e.append('<rect x="0" y="%d" width="13" height="13" fill="%s"/>' % (y + 3, col))
        for k, ligne in enumerate(lignes):
            e.append(txt(20, y + 15 + 18 * k, ligne, FS_MIN, INK2))
        y += 18 * len(lignes) + 4
    return y


def fig_origine_m(r, A, svg_d):
    L = T[LANG]
    e, y = tete_m("aom", L["t1"], desc_de(svg_d))
    for ligne in coupe(L["s1"], 38):
        y += 18
        e.append(txt(0, y, ligne, FS_MIN, INK2))
    y = legende_m(e, y + 10, list(zip((BLEU, BLEU_CLAIR, GRIS_CLAIR), L["l1"])))
    for l, x in r["leg"].items():
        y += 24
        e.append(txt(0, y, lib_leg(l), 15, INK, weight="600"))
        y += 8
        a = 0
        for v, col in ((x["AN"], BLEU), (x["SEN"], BLEU_CLAIR), (x["gouv"], GRIS_CLAIR)):
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="24" fill="%s"/>' % (a / x["N"] * WM, y, v / x["N"] * WM, col))
            a += v
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>'
                 % (WM / 2, y - 4, WM / 2, y + 28, INK))
        if x["Pmin"] != x["P"]:
            e.append(triangle(x["Pmin"] / x["N"] * WM, y + 25, 5))
        y += 32
        for ligne in lignes_origine(l, x):
            for morceau in coupe(ligne, 36):
                y += 19
                e.append(txt(0, y, morceau, FS_MIN, INK2, cls="val"))
    y += 26
    e.append('<line x1="0" y1="%d" x2="22" y2="%d" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>' % (y - 5, y - 5, INK))
    e.append(txt(30, y, L["moitie"], FS_MIN, INK2))
    y += 20
    e.append(triangle(11, y - 12, 5))
    for ligne in coupe(L["bb"], 34):
        e.append(txt(30, y, ligne, FS_MIN, INK2))
        y += 18
    for ligne in coupe(L["encours"], 38):
        e.append(txt(0, y, ligne, FS_MIN, INK2))
        y += 18
    return finir_m(e, y + 4, L["src1"], L["note1"].format(champ=A["champ"]))


def fig_493_m(r, A, svg_d):
    L = T[LANG]
    e, y = tete_m("a4m", L["t2"], desc_de(svg_d))
    for ligne in coupe(L["s2"], 38):
        y += 18
        e.append(txt(0, y, ligne, FS_MIN, INK2))
    y = legende_m(e, y + 10, list(zip((BLEU, GRIS_CLAIR), L["l2"])))
    vmax = 25
    for l, x in r["eng"].items():
        y += 24
        e.append(txt(0, y, lib_leg(l), 15, INK, weight="600"))
        y += 8
        a = 0
        for v, col in ((x["fin"], BLEU), (x["n"] - x["fin"], GRIS_CLAIR)):
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s"/>' % (a / vmax * (WM - 40), y, v / vmax * (WM - 40), col))
            a += v
        e.append(txt(a / vmax * (WM - 40) + 5, y + 17, nb(x["n"]), 15, INK, weight="600", cls="val"))
        y += 22
        for ligne in lignes_493(l, x):
            for morceau in coupe(ligne, 36):
                y += 19
                e.append(txt(0, y, morceau, FS_MIN, INK2, cls="val"))
    y += 26
    for ligne in coupe(L["encours"], 38):
        e.append(txt(0, y, ligne, FS_MIN, INK2))
        y += 18
    return finir_m(e, y + 4, L["src2"], L["note2"])


NUM = re.compile(r"(?<!\d)\d+(?:[ \u00a0\u202f,]\d{3})*(?:[.,]\d+)?(?!\d|er\b|re\b|e\b|st\b|nd\b|rd\b|th\b)")  # ordinaux exclus


def _nums(s):
    return {re.sub(r"[ \u00a0\u202f,]", "", x).replace(".", ",") for x in NUM.findall(s)}


def parite_mobile(figs):
    """Chaque valeur dessinée (classe « val ») de la version téléphone figure dans la description de la version détaillée ;
    police >= FS_MIN. Rend le nombre de valeurs contrôlées."""
    n = 0
    for nom in [k for k in figs if k.endswith("-m.svg")]:
        d, m = figs[nom.replace("-m.svg", ".svg")], figs[nom]
        vals = re.findall(r'<text class="val"[^>]*>([^<]*)</text>', m)
        dessines = {x for tx in vals for x in _nums(html.unescape(tx)) if not re.fullmatch(r"(19|20)\d\d", x)}
        if not dessines:
            raise Arret("parite mobile : %s -- aucune valeur dessinee lue (controle aveugle)" % nom)
        manquants = dessines - _nums(desc_de(d))
        if manquants:
            raise Arret("parite mobile : %s -- valeurs dessinees absentes de la version detaillee : %s" % (nom, sorted(manquants)))
        tailles = [float(x) for x in re.findall(r'font-size="([0-9.]+)"', m)]
        if min(tailles) < FS_MIN:
            raise Arret("parite mobile : %s -- police %.1f sous le minimum %.1f" % (nom, min(tailles), FS_MIN))
        n += len(dessines)
    return n


MONTRE = {
    "fr": {"origine": "Dans le champ étudié ({champ}), la part des lois promulguées issues d'une proposition de parlementaire "
                      "est de {Ppct14} % sous la XIVe législature, {Ppct15} % sous la XVe (au moins {Pminpct15} %), "
                      "{Ppct16} % sous la XVIe et {Ppct17} % sous la XVIIe, en cours au {releve} ; toutes natures hors "
                      "traités, {Ptotpct14}, {Ptotpct15}, {Ptotpct16} et {Ptotpct17} %. Origine formelle au dépôt initial, "
                      "non l'influence.",
           "493": "Le Premier ministre a engagé la responsabilité du Gouvernement sur un texte (art. 49, al. 3) {E14} fois sous "
                  "la XIVe législature, {Efois15} sous la XVe, {E16} fois sous la XVIe, dont {Efin16} sur un projet de loi "
                  "de finances ou de financement de la sécurité sociale, et {E17} fois sous la XVIIe, en cours au {releve} ; "
                  "chaque engagement est compté une fois."},
    "en": {"origine": "In the scope studied ({champ}), the share of the laws promulgated in France that arose from a private "
                      "member's bill is {Ppct14}% during the 14th legislature, {Ppct15}% during the 15th (at least "
                      "{Pminpct15}%), {Ppct16}% during the 16th and {Ppct17}% during the 17th, ongoing on {releve}; all kinds "
                      "except treaties, {Ptotpct14}, {Ptotpct15}, {Ptotpct16} and {Ptotpct17}%. Formal origin at the initial "
                      "tabling, not influence.",
           "493": "The Prime Minister made the passing of a bill an issue of a vote of confidence (art. 49, para. 3) {E14} times "
                  "during the 14th legislature, {Efois15} during the 15th, {E16} times during the 16th, {Efin16} of them on a "
                  "Finance Bill or Social Security Financing Bill, and {E17} times during the 17th, ongoing on {releve}; each "
                  "use is counted once."},
}


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        out = []
        for ident in ("origine", "493"):
            fichier = "adopter-" + ident + suf
            svg = figs[fichier + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            src, note, lic = (pied_figure.lire(svg, c) for c in ("pied-source", "pied-note", "pied-licence"))
            if not src or not note or lic != LICENCES[lang]:
                raise Arret("fiche %s : pied illisible" % fichier)
            out.append(dict(id=ident, fichier=fichier, titre=titre, montre=MONTRE[lang][ident].format(**AA), source=src,
                            precaution=note))
        res[lang] = out
    return res


def csv_texte(r: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "periode", "categorie", "valeur", "unite", "source"])
    for l, x in r["leg"].items():
        for k in ("N", "gouv", "AN", "SEN", "P", "Pmin", "traites", "autres"):
            w.writerow(["lois_ordinaires_promulguees", "legislature_" + l, k, x[k], "lois", "AN, Dosleg, JO"])
        for k in ("Ntot", "Ptot", "Ptotmin", "Nfin", "Norg", "Porg", "Ncst"):
            w.writerow(["lois_toutes_natures_hors_traites", "legislature_" + l, k, x[k], "lois", "AN, Dosleg, JO"])
    for k in ("N", "gouv", "AN", "SEN", "P"):
        w.writerow(["lois_ordinaires_promulguees", "entre_deux_legislatures_" + r["hl"]["mois"], k, r["hl"][k], "lois", "AN, Dosleg, JO"])
    for s, x in r["ses"].items():
        w.writerow(["lois_hors_traites", s, "N", x["N"], "lois", "AN, Dosleg, JO"])
        w.writerow(["lois_hors_traites", s, "origine_parlementaire", x["P"], "lois", "AN, Dosleg, JO"])
    for l, x in r["e1"].items():
        for k in ("N", "Z", "U", "exces", "Nw", "Zw", "ext", "bul", "pjl_bul", "mediane_jours"):
            w.writerow(["propositions_deposees_AN", "legislature_" + l, k, x[k], "textes", "AN, bulletins statistiques"])
    for l, x in r["eng"].items():
        for k in ("n", "fin", "lpfp", "adoptees", "textes"):
            w.writerow(["engagements_49_3", "legislature_" + l, k, x[k], "engagements" if k != "textes" else "textes", "AN"])
        for k in ("lois_fin", "lois_fin_engagees"):
            w.writerow(["lois_financieres_promulguees", "legislature_" + l, k, x[k], "lois", "AN, Dosleg, JO"])
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

    def citation47(m):
        m["const"]["47c"]["texte"] = m["const"]["47c"]["texte"].replace("soixante-dix jours", "soixante jours")

    def majorite(m):
        n = 0
        for r in m["lois"]:
            if r["legislature"] == "14" and r["nature"] == "ordinaire" and r["origine"] == "gouvernement" and n < 12:
                for k in ("origine", "origine_AN", "origine_Dosleg"):
                    if r[k]:
                        r[k] = "parlementaire AN"
                n += 1

    def champ_xv(m):  # lois organiques de la XVe rendues parlementaires : la XVe passe la moitié toutes natures
        n = 0
        for r in m["lois"]:
            if r["legislature"] == "15" and r["nature"] == "organique" and r["origine"] == "gouvernement" and n < 12:
                for k in ("origine", "origine_AN", "origine_Dosleg"):
                    if r[k]:
                        r[k] = "parlementaire AN"
                n += 1

    def nature(m):  # une nature que la liste des exclusions affichée ne nomme pas
        r = dict(m["lois"][0])
        r["numero"], r["nature"] = "9999-1", "decret"
        m["lois"].append(r)

    def reclasse(m):  # une loi financière de la XVIe classée « ordinaire » au registre
        for r in m["lois"]:
            if r["numero"] == "2023-1322":
                r["nature"] = "ordinaire"

    def unite(m):  # un seul engagement gardé par couple (texte, étape) : l'ancien libellé, faux
        vus, garde = set(), []
        for r in m["eng"]:
            if (r["dossier_texte"], r["etape"]) not in vus:
                vus.add((r["dossier_texte"], r["etape"]))
                garde.append(r)
        m["eng"] = garde

    def double(m):  # un même acte compté deux fois
        m["eng"].append(dict(m["eng"][0]))

    def fiche52(m):
        m["pages"]["fiche52"]["texte"] = m["pages"]["fiche52"]["texte"].replace("perte de recettes", "perte de ressources")

    def pdf52(m):  # PDF archivé de la fiche n° 52 remplacé
        m["pages"]["fiche52"]["sha256_lu"] = "0" * 64

    def projets(m):  # projets de loi déposés à l'Assemblée sous la XIVe portés à 400 (bulletins)
        r0 = [r for r in m["dep"] if r["legislature"] == "14"]
        tot = sum(int(r["pjl_an_premiere_lecture"]) for r in r0)
        r0[0]["pjl_an_premiere_lecture"] = str(int(r0[0]["pjl_an_premiere_lecture"]) + 400 - tot)

    def bulletins(e_cible):
        def f(m):
            r0 = [r for r in m["dep"] if r["legislature"] == "14"]
            ext = sum(1 for r in m["e1"] if r["legislature"] == "14" and r["origine"] == "parlementaire")
            tot = sum(int(r["ppl_an_premiere_lecture"]) for r in r0)
            r0[0]["ppl_an_premiere_lecture"] = str(int(r0[0]["ppl_an_premiere_lecture"]) - (tot - (ext - e_cible)))
        return f

    for nom, mut, pref, motif in (
            ("origine changee dans une source", origine, "B2", "origine AN"),
            ("loi 2024-2025 retiree", retire, "B3", "session 2024-2025"),
            ("engagement XVIe retire", engagement, "B4", "fiche n"),
            ("art. 49 altere", citation, "B1", "49b"),
            ("art. 47 altere", citation47, "B1", "47c"),
            ("XIVe rendue majoritaire", majorite, "B2", "moins de la moitie"),
            ("XVe majoritaire toutes natures", champ_xv, "B2", "depend du champ"),
            ("nature non declaree", nature, "B6", "nature"),
            ("un engagement par texte et par etape", unite, "B8", "plusieurs engagements"),
            ("acte double", double, "B8", "deux fois"),
            ("fiche 52 alteree", fiche52, "B1", "cit_fiche52"),
            ("PDF fiche 52 remplace", pdf52, "B1", "empreinte"),
            ("loi financiere reclassee", reclasse, "B7", "classe PLF/PLFSS"),
            ("bulletins XIV abaisses (exces 1 311)", bulletins(1311), "B5", "plus de la moitie"),
            ("bulletins XIV abaisses (exces 600)", bulletins(600), "B5", "dixieme"),
            ("projets XIV aux bulletins multiplies", projets, "B5", "cinq fois")):
        m = copy.deepcopy(S)
        mut(m)
        try:
            calculer(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if str(e).startswith("mutation") or not str(e).startswith(pref) or motif not in str(e):
                raise Arret("mutation %s : arretee par une autre garde que %s (%s) : %s" % (nom, pref, motif, e))
            out.append("%s -> %s" % (nom, str(e)[:90]))
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def _main() -> int:
    global LANG
    S = lire()
    r, g = calculer(S)
    for m in autotest(S):
        log("autotest : la mutation a mordu : " + m)
    A, A_en = affichage(r, "fr"), affichage(r, "en")
    if set(A) != set(A_en):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        figs["adopter-origine%s.svg" % suf] = fig_origine(r, AA)
        figs["adopter-493%s.svg" % suf] = fig_493(r, AA)
        figs["adopter-origine%s-m.svg" % suf] = fig_origine_m(r, AA, figs["adopter-origine%s.svg" % suf])
        figs["adopter-493%s-m.svg" % suf] = fig_493_m(r, AA, figs["adopter-493%s.svg" % suf])
    LANG = "fr"
    nv = parite_mobile(figs)
    fi = fiches(figs, A, A_en)
    g.append("parite des %d figures telephone (%d valeurs dessinees)" % (len([k for k in figs if k.endswith("-m.svg")]), nv))
    if "--check" in sys.argv[1:]:
        for x in g:
            log("OK " + x)
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    csvt = csv_texte(r)
    payload = {
        "releve_le": "2026-10-06",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Assemblée nationale, Sénat (Dosleg), Journal officiel "
                    "(DILA), Légifrance",
        "meta": {"page": "https://" + PAGE_URL,
                 "protocole": "fiches de preuve v2, volet Adopter, E1 (pire cas, écart déclaré), E2 et E3 ; refonte du 12/10/2026",
                 "constitution": {k: v["id"] for k, v in S["const"].items()},
                 "temoins": {k: v["sha256_document"] for k, v in S["pages"].items()},
                 "definitions": {
                     "origine": "origine formelle au dépôt initial : projet du Gouvernement, proposition déposée à l'Assemblée "
                                "nationale, proposition déposée au Sénat ; rattachement à la législature de promulgation",
                     "champ": "lois ordinaires promulguées, " + A["champ"] + " ; les lois promulguées entre deux "
                              "législatures (juin 2024, après la dissolution) sont comptées sur une ligne à part",
                     "toutes_natures": "toutes les lois promulguées hors lois autorisant un traité : lois ordinaires, de "
                                       "finances et de financement de la sécurité sociale, organiques et constitutionnelles",
                     "Pmin": "origine parlementaire établie par les deux sources (AN et Dosleg) ; l'écart avec P vient de lois "
                             "dont le dossier manque aux fichiers de l'AN pour un motif établi (dépôt sous la législature "
                             "précédente)",
                     "engagement": "engagement de responsabilité (art. 49, al. 3) : chaque engagement est compté une fois ; un même "
                                   "projet peut en recevoir plusieurs, y compris au cours d'une même lecture",
                     "fin": "engagement sur un projet de loi de finances ou de financement de la sécurité sociale "
                            "(rectificatives comprises), catégorie de l'art. 49, al. 3 ; la loi de programmation des finances "
                            "publiques relève d'« un autre projet »",
                     "lois_fin_engagees": "lois de finances et de financement de la sécurité sociale promulguées dont un "
                                          "dossier de l'Assemblée porte au moins un engagement, à une étape quelconque "
                                          "(jointure par l'identifiant de dossier)",
                     "E1": "proposition de loi ordinaire déposée en premier lieu à l'Assemblée ; « sans examen en séance "
                           "retrouvé dans les données de l'Assemblée avant la fin de la législature » ; pire cas : excès "
                           "des dépôts extraits sur les bulletins statistiques de l'AN retiré du champ et des propositions "
                           "sans examen (écart au protocole déclaré)"},
                 "limites": "l'origine formelle n'observe ni l'influence du Gouvernement sur une proposition, ni les "
                            "amendements ; les dépôts extraits ne concordent pas texte par texte avec les bulletins de "
                            "l'Assemblée : E1 est publié sur la borne du pire cas ; les lois sont rattachées à la législature "
                            "de promulgation, les propositions à celle de leur dépôt"},
        "gardes": g,
        "calcul": {"legislatures": r["leg"], "entre_deux_legislatures": r["hl"], "sessions": r["ses"], "engagements": r["eng"]},
        "tableaux": tableaux(r, "fr"),
        "tableaux_en": tableaux(r, "en"),
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
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")),
                         output_width=900 if n.endswith("-m.svg") else 1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_adopter.json, static/promesses_adopter.{json,csv}, data/figures_adopter.json, %d figures SVG + PNG"
        % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
