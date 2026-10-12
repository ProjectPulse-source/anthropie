#!/usr/bin/env python3
"""Volet « Appliquer » du dossier Promesses : une loi votée, les mesures qu'elle appelle, et les taux publiés.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 3 (v2, gelée au commit
dfd0ec9 ; arbitrage PRO-20261005-164029). Test décisif du 06/10/2026 : test_decisif/appliquer/VERDICT.md (registre de
concordance loi par loi, 17 mutations) ; recalcul indépendant des comptes du baromètre par un second code, concordant.
  E1 — lois sans mesure réglementaire d'application, sessions 2017-2018 à 2024-2025, bornes [D/N ; (D+U)/N] ;
       « moins de la moitié » seulement si 2(D+U) < N dans CHAQUE session (sinon : valeurs par session).
  E2 — état des mesures au jour du relevé (repli : le baromètre ne publie que l'état courant).
  E3 — définitions avant taux : Sénat et Gouvernement, même session ; série longue du Sénat par segments.
Phase B de la refonte (12/10/2026 ; arbitrages APPLIQUER/ARBITRAGE_CE_APPLIQUER_PHASE_A.md et
ARBITRAGE_CE_RELECTURE_JURIDIQUE_PROMESSES_2026-10-12.md, section « Appliquer ») : compte PAR LOI en quatre statuts ; filtre
des « sans objet » portant un acte restreint à une référence en tête, témoin des écartés à motif nommé ; tri des
observations « sans objet » par règles écrites, cas ambigus « indéterminés » ; chaîne juridique complète (Constitution
art. 10, 13, 21, 22, 61 ; code civil art. 1er, al. 1 à 3) ; décisions du Conseil d'État sur le délai raisonnable ; bilan du
SGG relu dans la page rendue archivée ; série du Sénat : « + 4 points » et les deux valeurs de 2019-2020 citées.

Sources (scripts/sources_appliquer/) : extraits bruts du baromètre de l'application des lois (Assemblée nationale,
LexImpact ; données DILA), constitués par extraire_sources.py ; texte des pages citées des rapports du Sénat, avec
l'empreinte de chaque document ; registre de concordance ; articles de la Constitution et du code civil (Légifrance, API
PISTE) ; relevé de la page rendue du bilan du SGG au 31/12/2025 (Légifrance refuse les scripts : page lue dans Chrome le
12/10/2026, lignes recopiées et vérifiées par l'empreinte que le navigateur a calculée sur le texte rendu) ; quatre
décisions du Conseil d'État (ArianeWeb, pages publiques, 12/10/2026). Le générateur ne lit rien en direct.

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  A1  Constitution (art. 10, 13, 21, 22, 61) et code civil, art. 1er : en vigueur, chaque citation retrouvée mot pour mot
      (FR Légifrance, EN traduction du Conseil constitutionnel) ; la paraphrase de l'art. 61, al. 1 (lois organiques) et
      celle de l'al. 1 du code civil adossées à leur texte ;
  A2  champ : lois de l'extrait = lois retenues + conventions écartées, par session ; registre = champ, loi par loi ;
  A3  « directe » du baromètre recalculée = registre ; effectifs du Sénat = effectifs annoncés par ses annexes (2017-2024)
      et par ses commissions (2024-2025, dont la somme = « 22 d'entre elles », p. 45) ;
  A4  « sous la moitié quelle que soit la source » : vrai dans toutes les sessions sauf une, où le baromètre seul dépasse ;
  A5  mesures : N = P + A + S + U par session ; cohérence avec le fichier des lois du même producteur, loi par loi ;
      A5 bis : « sans objet » commençant par un acte = référence d'acte retenue + écartés à MOTIF NOMMÉ (un écarté sans
      motif arrête) ; tri des observations : entré = classé + indéterminé, une observation qui relève de deux règles est
      indéterminée ;
  A6  cas témoin 2025-138 : « sans objet » au baromètre avec un arrêté, loi classée « sans mesure à prendre », mesure en
      attente au SGG ;
  A7  citations des rapports du Sénat, du bilan du SGG (empreinte du relevé = empreinte calculée par le navigateur) et
      valeurs de série retrouvées mot pour mot ; totaux du SGG : mesures = reçues + en attente, taux recalculé = publié ;
      A7 bis : tout nombre d'une traduction figure dans l'original ;
  A8  statut des lois : chaque loi du champ dans un et un seul des quatre statuts, définis séparément ; somme = champ ;
      témoin du Sénat 2024-2025 : même nombre de lois (56) dans les deux sources ;
  A9  « + 4 points » de 2024-2025 = 66 − 62 (taux 2023-2024 hors mesures différées), et 62 ≠ 59 ;
  A10 décisions du Conseil d'État : empreinte du fichier archivé, chaque citation retrouvée mot pour mot ; la formule du
      délai raisonnable présente dans les trois décisions où la page la dit ;
  Figures : version téléphone à parité avec la version détaillée (pied_figure.parite).
Autotest de mutation à chaque exécution (une mutation par garde, chacune doit arrêter sur SA garde).

Bilingue (06/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés, deux jeux de tableaux, des figures
-en au même dessin ; la Constitution se cite en anglais dans la traduction du Conseil constitutionnel (garde A1) ; les
autres textes français en français, suivis de notre traduction (clés *_tr), dont chaque nombre doit figurer dans
l'original (garde A7 bis). Nombres et lettres : scripts/langue_generee.py (adopté le 12/10/2026 ; écart de sortie : le
séparateur des milliers passe de l'espace fine insécable à l'espace insécable du module, « 5 398 »).

Écrit : data/promesses_appliquer.json (+ static/), static/promesses_appliquer.csv, data/figures_appliquer.json,
static/img/appliquer-{statut,mesures,lois,serie}[-en][-m].svg/.png. Rien n'est écrit à données identiques ; --check
calcule tout, figures comprises, et n'écrit rien.
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
import langue_generee as lg  # noqa: E402
import pied_figure as pf  # noqa: E402

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
# saisine du Conseil constitutionnel (art. 61). Qui prend les mesures (arbitrage du 12/10/2026) : art. 21, 13 et 22.
CONST = {"art10": "legifrance_09785484a231a183e5290643bbb832eeab7a232b4102ab55206f6b4cfcb2a5bb.json",
         "art61": "legifrance_c14abed78a1e9932d2cf37f84e6366e03847a41174d17466b5f83b4a0a3d299c.json",
         "art21_exec": "legifrance_ec04bca269f2bb1d8d41a22541853096f4a2eef7091b31f154e05f8158502a28.json",
         "art13": "legifrance_48d68737de9c34143c355de92838a0155262914c3a30096cd639a481a095f95a.json",
         "art22": "legifrance_5df36cc8f355cedc1593866297e49997e9361af8053855a4ecc4c3e0a13ff496.json"}
# Activité d'EMC (/enseignants/emc/, avis entrant du 07/10/2026) : le contrôle de l'art. 61 se distingue selon le texte,
# facultatif pour une loi votée (al. 2), obligatoire pour une proposition de l'art. 11 (al. 1). Même pièce archivée.
CONST["art61_saisine"] = CONST["art61_rip"] = CONST["art61"]
CONST["art10_al2"] = CONST["art10"]
CONST["art21_regl"] = CONST["art21_exec"]
CIT_CONST = {"art10": "Le Président de la République promulgue les lois dans les quinze jours qui suivent la transmission au Gouvernement de la loi définitivement adoptée.",
             "art10_al2": "Il peut, avant l'expiration de ce délai, demander au Parlement une nouvelle délibération de la loi ou de certains de ses articles. Cette nouvelle délibération ne peut être refusée.",
             "art61": "la saisine du Conseil constitutionnel suspend le délai de promulgation.",
             "art61_saisine": "les lois peuvent être déférées au Conseil constitutionnel, avant leur promulgation, par le Président de la République, le Premier ministre, le Président de l'Assemblée nationale, le Président du Sénat ou soixante députés ou soixante sénateurs.",
             "art61_rip": "les propositions de loi mentionnées à l'article 11 avant qu'elles ne soient soumises au référendum",
             "art21_exec": "Il assure l'exécution des lois.",
             "art21_regl": "il exerce le pouvoir réglementaire",
             "art13": "Le Président de la République signe les ordonnances et les décrets délibérés en Conseil des ministres.",
             "art22": "Les actes du Premier ministre sont contresignés, le cas échéant, par les ministres chargés de leur exécution."}
# Paraphrases de la page adossées au texte (A1) : la saisine obligatoire des lois organiques (art. 61, al. 1) ; « sous
# réserve de l'article 13 » (art. 21).
PARAPHRASES = {"art61": ["Les lois organiques, avant leur promulgation,", "doivent être soumis au Conseil constitutionnel",
                         "peuvent être déférées au Conseil constitutionnel, avant leur promulgation",
                         "suspend le délai de promulgation"],
               "art21_exec": ["Sous réserve des dispositions de l'article 13", "Il assure l'exécution des lois",
                              "il exerce le pouvoir réglementaire"],
               # passe B2 (12/10/2026) : au fil du texte, une phrase par article ; la lettre intégrale passe en repli
               "art10": ["promulgue les lois dans les quinze jours qui suivent la transmission au Gouvernement",
                         "demander au Parlement une nouvelle délibération"],
               "art13": ["signe les ordonnances et les décrets délibérés en Conseil des ministres"],
               "art22": ["contresignés, le cas échéant, par les ministres chargés de leur exécution"]}
SESSIONS = ["%d-%d" % (a, a + 1) for a in range(2017, 2025)]
RELEVE = "05/10/2026"
MOTS = {"un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
CONST_EN = {"art10": ("10", "The President of the Republic shall promulgate Acts of Parliament within fifteen days following the "
                             "final passage of an Act and its transmission to the Government."),
            "art10_al2": ("10", "He may, before the expiry of this time limit, ask Parliament to reopen debate on the Act or any "
                                "sections thereof. Such reopening of debate shall not be refused."),
            "art61": ("61", "referral to the Constitutional Council shall suspend the time allotted for promulgation."),
            "art61_saisine": ("61", "Acts of Parliament may be referred to the Constitutional Council, before their promulgation, by the "
                                    "President of the Republic, the Prime Minister, the President of the National Assembly, the "
                                    "President of the Senate, sixty Members of the National Assembly or sixty Senators."),
            "art61_rip": ("61", "Private Members' Bills mentioned in article 11 before they are submitted to referendum"),
            "art21_exec": ("21", "He shall ensure the implementation of legislation."),
            "art21_regl": ("21", "he shall have power to make regulations"),
            "art13": ("13", "The President of the Republic shall sign the Ordinances and Decrees deliberated upon in the Council of Ministers."),
            "art22": ("22", "Instruments of the Prime Minister shall be countersigned, where required, by the ministers responsible "
                            "for their implementation.")}
PARAPHRASES_EN = {"61": ["Institutional Acts, before their promulgation,", "be referred to the Constitutional Council",
                          "shall suspend the time allotted for promulgation"],
                  "10": ["shall promulgate Acts of Parliament within fifteen days following the final passage of an Act and its "
                         "transmission to the Government", "ask Parliament to reopen debate"],
                  "21": ["He shall ensure the implementation of legislation", "he shall have power to make regulations"],
                  "13": ["shall sign the Ordinances and Decrees deliberated upon in the Council of Ministers"],
                  "22": ["countersigned, where required, by the ministers responsible for their implementation"]}
# « hors conventions » (passe B2) : les lois que le baromètre marque « Loi autorisant la ratification d'accords
# internationaux » sont, d'après leur titre, celles qui autorisent la ratification ou l'approbation d'un accord
# international, ou l'adhésion à un tel accord ; garde A2 dans les deux sens.
CONV_TITRE = re.compile(r"autorisant (?:la ratification|l['’]approbation|l['’]adh[ée]sion)", re.I)

# Décisions du Conseil d'État (ArianeWeb, pages publiques, lues le 12/10/2026 ; curl sans en-tête imité, réponse 200).
CE = {"343188": ("ce_decision_2011-06-29_343188.html", "db9594c1b2025c48c76d0cc0c1d37277a39af68b7d097f33f5b93ef9c9d0a68d"),
      "429956": ("ce_decision_2021-01-21_429956.html", "07af6831a01ad03493fa0bba76695253f0e4758db1ff9f5dc0cffbccc32b3e0c"),
      "261694": ("ce_decision_2005-07-27_261694.html", "bb38e40ec0126fa4d1ed65887da3726f35f1eab6b3a89150917e6ec06593e498"),
      "441660": ("ce_decision_2021-05-27_441660.html", "621baccd9513b80a9a392983d95ad0c9fb4f046f2c32279be19ac0387bc711d5")}
PRINCIPE = ("L'exercice du pouvoir réglementaire comporte non seulement le droit mais aussi l'obligation de prendre dans un délai "
            "raisonnable les mesures qu'implique nécessairement l'application de la loi, hors le cas où le respect "
            "d'engagements internationaux de la France y ferait obstacle.")
CIT_CE = {  # clé -> (décision, citation exacte)
    "cit_ce_principe": ("441660", PRINCIPE),
    "cit_ce_arrete": ("429956", "Lorsqu'un décret pris pour l'application d'une loi renvoie lui-même à un arrêté la détermination de certaines mesures nécessaires à cette application, cet arrêté doit également intervenir dans un délai raisonnable."),
    "cit_ce_precision": ("441660", "ces dispositions ne sont pas suffisamment précises pour permettre leur entrée en vigueur en l'absence du décret d'application dont elles prévoient d'ailleurs l'intervention"),
    "cit_ce_injonction": ("441660", "d'enjoindre au Premier ministre de prendre ce décret dans un délai de six mois à compter de la notification de la présente décision"),
    "cit_ce_arrete_injonction": ("429956", "d'ordonner au garde des sceaux, ministre de la justice, de prendre l'arrêté prévu par l'article 9 du décret du 29 juin 2020 dans un délai de trois mois"),
    "cit_ce_reparation": ("261694", "les préjudices qui résultent du retard mis à prendre, au-delà d'un délai raisonnable, un décret nécessaire à l'application d'une loi ouvrent droit à réparation"),
    "cit_ce_nature": ("261694", "eu égard à la nature des mesures à prendre"),
    "cit_ce_exhaustif": ("343188", "l'article R. 1243-4 fixe de façon exhaustive et précise le contenu du dossier de demande d'autorisation"),
    "cit_ce_pas_tenu": ("343188", "le ministre chargé de la santé n'était pas tenu de prendre l'arrêté prévu par ce dernier article"),
}
PRINCIPE_DANS = ("343188", "429956", "441660")  # la page dit la formule reprise en 2011 et en 2021
# Noyau de la formule, commun aux trois décisions (2011 : « Considérant que l'exercice… ; », 2021 : « L'exercice… . »).
PRINCIPE_NOYAU = ("comporte non seulement le droit mais aussi l'obligation de prendre dans un délai raisonnable les mesures "
                  "qu'implique nécessairement l'application de la loi, hors le cas où le respect d'engagements internationaux "
                  "de la France y ferait obstacle")

# Bilan du SGG au 31/12/2025 : Légifrance refuse les scripts (403). Page rendue dans Chrome le 12/10/2026 ; douze lignes
# de document.body.innerText (21, 25, 27, 29, 33, 100, 102, 104, 106, 110, 116, 135) jointes par « \n » ; empreinte
# calculée DANS LE NAVIGATEUR sur ces lignes, puis comparée à celle du fichier recopié : identiques. Empreinte du texte
# rendu entier, pour mémoire : PAGE_SGG_SHA.
SGG_FICHIER = "sgg_bilan_31-12-2025_page_rendue.txt"
SGG_SHA = "3232dcae236eb2d06794a0d785aff4f80dacba93ba3bd19f60c03041a7a78cd7"
PAGE_SGG_SHA = "c5cda67497c80af9be853ab8d71a3a1c5bb238d2150278969b39a79a89d2c030"
SGG_URL = ("https://www.legifrance.gouv.fr/contenu/menu/autour-de-la-loi/legislatif-et-reglementaire/application-des-lois/"
           "bilan-semestriel-au-31-decembre-2025")

# Notre traduction des citations françaises hors Constitution ; chaque nombre doit figurer dans l'original (garde A7 bis).
TR = {
    "cit_cciv": "However, provisions whose implementation requires implementing measures do not enter into force until "
                "those measures themselves enter into force.",
    "cit_cciv_urg": "In case of urgency, laws whose promulgation decree so prescribes enter into force on their publication",
    "cit_sgg_1718": "On 31 March 2019, these 28 laws called for 461 implementing regulations and we adopted 393 of them, an "
                    "implementation rate of 85%",
    "cit_senat_1718": "It now stands at 78% - 86% if measures whose entry into force is deferred are excluded",
    "cit_senat_1819": "The overall implementation rate of laws calculated by the Senate is 72%",
    "cit_sgg_1819": "the departments of the General Secretariat of the Government arrive for their part at an overall rate of 82.4%",
    "cit_diverge": "The rate calculated by the Senate may differ from the one calculated by the Government for technical "
                   "reasons, of two kinds.",
    "cit_arretes": "the Senate carries out a comprehensive check of the implementing measures of laws, including the ministerial "
                   "orders (arrêtés) whose publication is provided for by the law. This is not the case of the General "
                   "Secretariat of the Government.",
    "cit_politique": "It may also differ for political reasons, in particular when the Senate considers that a decree adopted "
                     "does not reflect the legislature's intent, and therefore that the expected measure has not been taken.",
    "cit_differees": "the Senate includes in its rate the measures expected for articles whose entry into force is deferred, "
                     "unlike the Government.",
    "cit_1213": "for the laws promulgated during the 2012-2013 parliamentary year, the implementation rate of laws stands at 90% "
                "(counting by number of laws) or about 64% (counting by number of measures), percentages calculated from the "
                "Senate's statistical database and which match exactly those calculated by the Government's departments",
    "cit_802_arretes": "Since 1 January 2024, the SGG has checked the publication of ministerial orders provided that they were "
                       "expressly provided for by a legislative provision.",
    "cit_802_differees": "it was decided, for the 2024-2025 session, no longer to take into account measures deferred beyond "
                         "31 March 2026",
    "cit_802_appreciation": "Despite the convergence of methods, some divergences remain between the Senate and the SGG as to "
                            "the assessment of whether certain laws are effectively applied.",
    "cit_802_baisse": "since 2018 the Senate has witnessed an overall and steady decline in the average implementation rate of "
                      "the laws it adopts",
    "cit_802_36": "As at 31 March 2026, 36 laws (64%) adopted during the 2024-25 session out of 56 were fully applicable.",
    "cit_802_detail": "More precisely, 22 of them (39%) were directly applicable and 14 (25%) had received all the planned "
                      "implementing measures.",
    "cit_802_22": "More precisely, 22 of them (39%) were directly applicable",
    "cit_802_24": "the number of laws promulgated during the 2024-2025 session stands at 56, of which 24 directly applicable",
    "cit_802_66": "Overall implementation rate of laws 66% (+ 4 points)",
    "cit_802_note": "The data taken into account are those of the measures provided for by the legislative provisions, "
                    "excluding optional measures and measures deferred beyond 31 March 2026.",
    "cit_2324_62": "If measures whose deferred entry into force the legislature has authorised are excluded, this "
                   "implementation rate stands at 62%",
    "cit_2020_62": "The overall implementation rate of laws measured by the Senate this year is 62%",
    "cit_2021_60": "a lower rate than that of the previous year (60%)",
    "cit_2021_62": "Including implementing measures adopted but not planned, this rate is 63% (62% for the previous year)",
    "cit_six_mois": "this year, for the first time, in order to measure the number of regulations adopted only at the end of "
                    "the six-month period the Government sets itself, the period used includes three months fewer for the "
                    "laws promulgated and three months more for the regulations adopted.",
    "cit_sgg16_def": "shows the implementation rate at 31 December 2025 of the laws which, among those passed between 1 July 2022 "
                     "and 9 June 2024, call for implementing decrees.",
    "cit_sgg17_def": "shows the implementation rate at 31 December 2025 of the laws which, among those published between 18 July "
                     "2024 and 30 June 2025, call for implementing decrees or orders.",
    "cit_ce_principe": "The exercise of regulatory power entails not only the right but also the obligation to take, within a "
                       "reasonable time, the measures that the application of the law necessarily implies, except where "
                       "compliance with France's international commitments would prevent it.",
    "cit_ce_arrete": "Where a decree adopted for the application of a law itself refers to a ministerial order the "
                     "determination of certain measures necessary for that application, that order must also be issued "
                     "within a reasonable time.",
    "cit_ce_precision": "these provisions are not precise enough to allow their entry into force in the absence of the "
                        "implementing decree, whose adoption they moreover provide for",
    "cit_ce_injonction": "to order the Prime Minister to adopt this decree within six months of notification of this decision",
    "cit_ce_arrete_injonction": "to order the Keeper of the Seals, Minister of Justice, to adopt the order provided for by "
                                "article 9 of the decree of 29 June 2020 within three months",
    "cit_ce_reparation": "the losses resulting from the delay in adopting, beyond a reasonable time, a decree necessary for the "
                         "application of a law give rise to compensation",
    "cit_ce_nature": "having regard to the nature of the measures to be taken",
    "cit_ce_exhaustif": "article R. 1243-4 sets out exhaustively and precisely the content of the authorisation application file",
    "cit_ce_pas_tenu": "the minister responsible for health was not bound to adopt the order provided for by that article",
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


def fr(n, dec=0) -> str:
    return lg.nombre(n, dec, "fr")


def en(n, dec=0) -> str:
    return lg.nombre(n, dec, "en")


def nombres(s: str) -> set:
    return {x.replace(",", ".") for x in re.findall(r"\d+(?:[.,]\d+)?", s)}


def session(d: str) -> str:
    a = int(d[:4]) if int(d[5:7]) >= 10 else int(d[:4]) - 1
    return "%d-%d" % (a, a + 1)


def texte_html(b: bytes) -> str:
    t = b.decode("utf-8", "replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S | re.I)
    return norm(html.unescape(re.sub(r"<[^>]+>", " ", t)))


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
        const[k] = {"etat": a["etat"], "texte": norm(a["texte"]), "id": a["id"], "num": a.get("num")}
    sgg = (SRC / SGG_FICHIER).read_bytes().replace(b"\r\n", b"\n")
    ce = {}
    for num, (f, h) in CE.items():
        b = (SRC / f).read_bytes()
        ce[num] = {"sha": hashlib.sha256(b).hexdigest(), "texte": texte_html(b), "fichier": f}
    return {"cciv": {"etat": c["etat"], "texte": norm(c["texte"]), "id": c["id"]}, "const": const,
            "lois": L, "mesures": M, "tetes": [tl, tm], "registre": reg,
            "effectifs": json.loads((SRC / "senat_effectifs.json").read_text(encoding="utf-8")),
            "pages": json.loads((SRC / "senat_pages.json").read_text(encoding="utf-8")),
            "sgg_sha": hashlib.sha256(sgg).hexdigest(), "sgg": norm(sgg.decode("utf-8")), "ce": ce}


# ------------------------------------------------------------------ citations (A7)
CIT_CCIV = ("Toutefois, l'entrée en vigueur de celles de leurs dispositions dont l'exécution nécessite des mesures "
            "d'application est reportée à la date d'entrée en vigueur de ces mesures.")
CIT_CCIV_URG = "En cas d'urgence, entrent en vigueur dès leur publication les lois dont le décret de promulgation le prescrit"
PARAPHRASE_CCIV = "entrent en vigueur à la date qu'ils fixent ou, à défaut, le lendemain de leur publication"
CITATIONS = {  # clé -> (page archivée, citation exacte) ; affichées par jeton
    "cit_sgg_1718": ("r18-542|539", "Au 31 mars 2019, ces 28 lois appelaient 461 mesures réglementaires d'application et nous en avons pris 393, soit un taux d'application de 85 %"),
    "cit_senat_1718": ("r18-542|5", "Il atteint désormais 78 % - 86 % si on exclut les mesures dont l'entrée en vigueur est différée"),
    "cit_senat_1819": ("r19-523|7", "Le taux global d'application des lois calculé par le Sénat est de 72 %"),
    "cit_sgg_1819": ("r19-523|13", "les services du Secrétariat général du Gouvernement parviennent pour leur part à un taux global de 82,4 %"),
    "cit_diverge": ("r19-523|13", "Le taux calculé par le Sénat peut diverger de celui calculé par le Gouvernement pour des raisons techniques, qui sont de deux ordres."),
    "cit_arretes": ("r19-523|13", "le Sénat effectue un contrôle global des mesures d'application des lois, en incluant les arrêtés dont la publication est prévue par la loi. Ce n'est pas le cas du secrétariat général du Gouvernement."),
    "cit_politique": ("r19-523|13", "Il peut également diverger pour des raisons politiques, notamment lorsque le Sénat considère qu'un décret pris ne respecte pas la volonté du législateur, et donc que la mesure attendue n'est pas prise."),
    "cit_differees": ("r19-523|13", "le Sénat intègre dans son taux les mesures attendues pour des articles dont l'entrée en vigueur est différée, à la différence du Gouvernement."),
    "cit_1213": ("r13-623|15", "pour les lois promulguées durant l'année parlementaire 2012-2013, le taux d'application des lois s'élève à 90 % (si on compte en nombre de lois) ou à environ 64 % (si on compte en nombre de mesures), pourcentages calculés à partir de la base statistique du Sénat et qui recoupent parfaitement ceux calculés par les services du Gouvernement"),
    "cit_802_arretes": ("r25-802|20", "Depuis le 1er janvier 2024, le SGG contrôle la parution des arrêtés sous réserve qu'ils aient été expressément prévus par une disposition législative."),
    "cit_802_differees": ("r25-802|20", "il a été décidé, pour la session 2024-2025, de ne plus prendre en compte les mesures différées au-delà du 31 mars 2026"),
    "cit_802_appreciation": ("r25-802|21", "En dépit de la convergence des méthodes, certaines divergences demeurent quant à l'appréciation de l'effectivité de l'application de certaines lois entre le Sénat et le SGG."),
    "cit_802_baisse": ("r25-802|21", "le Sénat assiste depuis 2018 à une réduction globale et constante du taux d'application moyen des lois qu'il adopte"),
    "cit_802_36": ("r25-802|45", "Au 31 mars 2026, 36 lois (soit 64 %) adoptées au cours de la session 2024-25 sur 56 étaient entièrement applicables."),
    "cit_802_detail": ("r25-802|45", "Plus précisément, 22 d'entre elles (soit 39 %) étaient d'application directe et 14 (soit 25 %) avaient fait l'objet de l'intégralité des mesures d'application prévues."),
    "cit_802_22": ("r25-802|45", "Plus précisément, 22 d'entre elles (soit 39 %) étaient d'application directe"),
    "cit_802_24": ("r25-802|271", "le nombre de lois promulguées lors de la session 2024-2025 s'établit à 56, dont 24 d'application directe"),
    "cit_802_66": ("r25-802|7", "Taux d'application global des lois 66 % (+ 4 points)"),
    "cit_802_note": ("r25-802|7", "Les données prises en compte sont celles des mesures prévues, non éventuelles et non différées au-delà du 31 mars 2026, par les dispositions législatives."),
    "cit_2324_62": ("r24-710|3", "Si l'on exclut les mesures dont le législateur a autorisé une entrée en vigueur différée, ce taux d'application s'élève à 62 %"),
    "cit_2020_62": ("r20-645|16", "Le taux global d'application des lois mesuré par le Sénat cette année est de 62 %"),
    "cit_2021_60": ("r21-658|3", "soit un taux inférieur à celui de l'année précédente (60 %)"),
    "cit_2021_62": ("r21-658|3", "En incluant les mesures d'application prises mais non prévues, ce taux est de 63 % (62 % pour l'année précédente)"),
    "cit_six_mois": ("r11-323|11", "cette année, pour la première fois, afin de ne mesurer le nombre de mesures réglementaires prises qu'à l'expiration du délai de six mois que s'impose à lui-même le Gouvernement, la période retenue comprend trois mois de moins pour les lois promulguées retenues et trois mois de plus pour les mesures réglementaires prises."),
}
CIT_SGG = {  # lignes du relevé de la page rendue du bilan du SGG au 31/12/2025
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
# 2019-2020 : 62 % dans le rapport de 2020 ; le rapport suivant écrit « (60 %) » pour l'année précédente, et donne aussi
# « 62 % pour l'année précédente » en incluant les mesures prises mais non prévues. Révision ou autre variante : non établi
# (arbitrage du 12/10/2026, Q6) ; les deux valeurs sont gardées avec leurs documents.
REVISION = ("2019-2020", 60, "r21-658|3", "soit un taux inférieur à celui de l'année précédente (60 %)")
SEGMENTS = {
    1: "lois de l'année parlementaire, arrêt au 30 septembre de la même année",
    2: "période décalée de trois mois pour attendre le délai de six mois du Gouvernement, session ordinaire seule",
    3: "« nouvelles bornes » : lois du 14 juillet 2011 au 30 septembre 2012",
    4: "lois du 1er octobre au 30 septembre, arrêt au 31 mars suivant",
    5: "même calendrier, mesures différées comprises (un second taux les exclut)",
    6: "un seul taux, sans mesures éventuelles ni différées au-delà du 31 mars 2026",
}

# B2 (arbitrage du 12/10/2026) : une observation « sans objet » compte comme portant la référence d'un acte si elle
# COMMENCE par une référence (« Arrêté du », « Décret du », « Décret n° ») ; le filtre large (le mot en tête) en rend
# compte : retenu + écarté, chaque écarté avec un motif nommé.
REF_ACTE = re.compile(r"\s*(?:Arr[êe]t[ée] du |D[ée]cret du |D[ée]cret n\s?°)")
LARGE_ACTE = re.compile(r"\s*(?:Arr[êe]t[ée]|D[ée]cret)\b")
MOTIFS_ECARTES = {"décret non pris": re.compile(r"\s*D[ée]cret non pris\b")}
# Q5 : tri de l'observation du producteur, par règles écrites ; une observation qui relève de zéro ou de plusieurs
# règles est « indéterminée ». Échantillon relu le 12/10/2026 (rapport de phase B, § 5). Jamais un reclassement juridique.
_AP = "['\u2019]"
TRI = [
    ("acte_en_tete", REF_ACTE.pattern),
    ("deja_appliquee", r"d[ée]j[àa] appliqu"),
    ("base_legale_modifiee", r"abrog|r[ée][ée]cri|supprim|obsol|modifi\w* .*renvoi"),
    ("aucune_mesure_necessaire", r"(?:pas|n" + _AP + r"est|n" + _AP + r"était|plus) n[ée]cessaire|aucune mesure r[ée]glementaire|"
                                 r"n" + _AP + r"appelle (?:pas|aucune)|pas d" + _AP + r"une mesure d" + _AP + r"application|"
                                 r"non n[ée]cessaire|ne n[ée]cessit\w* pas"),
    ("mesure_eventuelle_non_utilisee", r"[ée]ventuelle.*(?:pas été|non) utilis|pas prévu de prendre de texte pour cette mesure [ée]ventuelle"),
    ("mesure_non_prise", r"non pris|n" + _AP + r"(?:a|ont) (?:pas )?été pris|pas été pris|ne sera pas pris|renonc|abandonn"),
]
_TRI = [(k, re.compile(r, re.I)) for k, r in TRI]


def trier(obs: str) -> str:
    k = [n for n, r in _TRI if (r.match(obs) if n == "acte_en_tete" else r.search(obs))]
    return k[0] if len(k) == 1 else "indetermine"


def verifier_citations(S: dict) -> dict:
    P = S["pages"]
    out = {}
    for k, (pg, c) in CITATIONS.items():
        if pg not in P or norm(c) not in P[pg]["texte"]:
            raise Arret("A7 : citation %s absente de la page %s : %r" % (k, pg, c[:60]))
        out[k] = norm(c)
    if S["sgg_sha"] != SGG_SHA:
        raise Arret("A7 : releve du bilan du SGG : empreinte %s, attendue %s (empreinte calculee par le navigateur)"
                    % (S["sgg_sha"][:12], SGG_SHA[:12]))
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


def totaux_sgg(S: dict) -> dict:
    """Totaux du bilan du SGG : mesures, reçues, en attente, taux ; mesures = reçues + attente, taux recalculé = publié."""
    out = {}
    for k in ("sgg16", "sgg17"):
        m = re.fullmatch(r"Total général (\d+) (\d+) (\d+) (\d+)%", norm(CIT_SGG[k + "_total"]))
        n, ok, att, t = map(int, m.groups())
        if n != ok + att or round(100 * ok / n) != t:
            raise Arret("A7 : SGG %s : %d != %d + %d ou taux %d != %d" % (k, n, ok, att, t, round(100 * ok / n)))
        out[k] = {"mesures": n, "recues": ok, "attente": att, "taux": t}
    return out


def verifier_ce(S: dict) -> dict:
    out = {}
    for num, (f, h) in CE.items():
        if S["ce"][num]["sha"] != h:
            raise Arret("A10 : decision %s : empreinte du fichier archive changee" % num)
    for k, (num, c) in CIT_CE.items():
        if norm(c) not in S["ce"][num]["texte"]:
            raise Arret("A10 : %s : citation absente de la decision %s : %r" % (k, num, c[:60]))
        out[k] = norm(c)
    for num in PRINCIPE_DANS:
        if norm(PRINCIPE_NOYAU) not in S["ce"][num]["texte"]:
            raise Arret("A10 : formule du delai raisonnable absente de la decision %s" % num)
    return out


# ------------------------------------------------------------------ calcul et gardes
def calculer(S: dict) -> tuple[dict, list[str]]:
    g = []
    cc = S["cciv"]["texte"]
    if S["cciv"]["etat"] != "VIGUEUR" or not all(norm(x) in cc for x in (CIT_CCIV, CIT_CCIV_URG, PARAPHRASE_CCIV)):
        raise Arret("A1 : code civil, art. 1 : texte non en vigueur, phrase du report, de l'urgence ou de l'al. 1 introuvable")
    for k, c in CIT_CONST.items():
        if S["const"][k]["etat"] != "VIGUEUR" or norm(c) not in S["const"][k]["texte"]:
            raise Arret("A1 : Constitution %s : texte non en vigueur ou citation introuvable" % k)
    for k, xs in PARAPHRASES.items():
        if not all(norm(x) in S["const"][k]["texte"] for x in xs):
            raise Arret("A1 : Constitution %s : paraphrase sans appui dans le texte" % k)
    try:
        tcen = cen.texte()
        cit_en = {"cit_" + k: cen.citer(a, c, tcen) for k, (a, c) in CONST_EN.items()}
        for a, xs in PARAPHRASES_EN.items():
            for x in xs:
                cen.citer(a, x, tcen)
    except ValueError as e:
        raise Arret("A1 : %s" % e)
    g.append("A1 : Constitution art. 10, 13, 21, 22 et 61 (FR Legifrance, EN Conseil constitutionnel), code civil art. 1 (al. 1 a 3)")
    cit = verifier_citations(S)
    sgg = totaux_sgg(S)
    cce = verifier_ce(S)
    g.append("A10 : %d decisions du Conseil d'Etat (empreintes), %d citations retrouvees mot pour mot ; formule du delai "
             "raisonnable dans %d decisions" % (len(CE), len(CIT_CE), len(PRINCIPE_DANS)))
    orig = dict(cit, **cce, cit_cciv=norm(CIT_CCIV), cit_cciv_urg=norm(CIT_CCIV_URG),
                cit_sgg16_def=norm(CIT_SGG["sgg16_def"]), cit_sgg17_def=norm(CIT_SGG["sgg17_def"]))
    for k, tr in TR.items():
        if k not in orig:
            raise Arret("A7 bis : traduction %s sans original" % k)
        if not nombres(tr) <= nombres(orig[k]):
            raise Arret("A7 bis : %s : nombres de la traduction absents de l'original : %s" % (k, nombres(tr) - nombres(orig[k])))
    g.append("A7 : %d citations du Senat, %d extraits du SGG (releve a l'empreinte du navigateur ; totaux recalcules), "
             "%d valeurs de serie retrouvees mot pour mot" % (len(CITATIONS), len(CIT_SGG), len(SERIE) + 1))

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
        champ[l[iJ]] = {"session": s, "directe": l[iDir] == "oui", "sans_ech": l[iSE] == "oui", "na": int(l[iNa]),
                        "napp": int(l[iNapp]), "titre": l[iT]}
    N = collections.Counter(v["session"] for v in champ.values())
    for s in SESSIONS:
        if entree[s] != N[s] + ecartees[s]:
            raise Arret("A2 : %s entre %d != retenu %d + ecarte %d" % (s, entree[s], N[s], ecartees[s]))
    reg = S["registre"]
    rj = {r["jorf"]: r for r in reg}
    if set(rj) != set(champ):
        raise Arret("A2 : registre et champ du barometre different (%d lois hors registre, %d hors champ)"
                    % (len(set(champ) - set(rj)), len(set(rj) - set(champ))))
    hors_def = [l[iT][:50] for l in L[1:] if l[iConv] == "oui" and not CONV_TITRE.search(l[iT])]
    dans_def = [v["titre"][:50] for v in champ.values() if CONV_TITRE.search(v["titre"])]
    if hors_def or dans_def:  # la page définit « hors conventions » par l'objet de la loi
        raise Arret("A2 : « hors conventions » != lois autorisant ratification, approbation ou adhesion : %d ecartee(s) hors "
                    "definition %s, %d loi(s) du champ dans la definition %s" % (len(hors_def), hors_def[:1], len(dans_def),
                                                                                dans_def[:1]))
    g.append("A2 : %d lois au champ, %d conventions ecartees (toutes, et elles seules, autorisent ratification, approbation "
             "ou adhesion), registre identique loi par loi" % (len(champ), sum(ecartees.values())))

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
    contraires = [x for x in lignes if 2 * (x["D"] + x["U"]) >= x["N"]]
    if not contraires:
        raise Arret("A4 : la phrase « moins de la moitie » tiendrait dans chaque session : la page dit le contraire, a reecrire")
    ct = contraires[0]
    if not 2 * ct["baro"] > ct["N"]:
        raise Arret("A4 : %s : le barometre seul ne depasse pas la moitie" % ct["session"])
    if any(2 * x["D"] > x["N"] for x in lignes):
        raise Arret("A4 : une majorite inverse serait a dire")
    # Phrase de la page : « Dans <nautres> sessions sur <nsessions>, les lois d'application directe restent sous la moitié,
    # quelle que soit la source ; en <ct>, le baromètre en compte plus de la moitié. »
    if len(contraires) != 1 or any(2 * max(x["baro"], x["senat_publie"], x["D"] + x["U"]) >= x["N"] for x in lignes if x is not ct):
        raise Arret("A4 : « dans les autres sessions, sous la moitie quelle que soit la source » faux")
    ndesacc = sum(1 for r in reg if r["directe_baro"] != r["directe_senat"])
    g.append("A4 : %s : barometre %d/%d, seule session au-dessus de la moitie ; %d lois classees differemment"
             % (ct["session"], ct["baro"], ct["N"], ndesacc))

    # --- E2 : mesures
    M = S["mesures"]
    hm = M[0]
    iLoi, iEtat, iActe, iObs, iObj, iDP = 1, hm.index("État"), hm.index("Identifiant décret"), \
        hm.index("Objectif initial de publication, observations"), hm.index("Objet"), hm.index("Date prévue")
    cl = collections.defaultdict(collections.Counter)
    par_loi = collections.defaultdict(collections.Counter)
    obs_acte = collections.Counter()
    obs_large = 0
    ecartes = []
    tri = collections.Counter()
    nS = 0
    differ_A = collections.Counter()
    differ_sans_date = 0
    A_sans_date = 0
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
        if c == "S":
            nS += 1
            tri[trier(m[iObs])] += 1
            if LARGE_ACTE.match(m[iObs]):
                obs_large += 1
                if REF_ACTE.match(m[iObs]):
                    obs_acte[s] += 1
                else:
                    motif = [k for k, r in MOTIFS_ECARTES.items() if r.match(m[iObs])]
                    if not motif:
                        raise Arret("A5 bis : observation « sans objet » commencant par un acte, sans reference ni motif nomme : %r"
                                    % m[iObs][:60])
                    ecartes.append({"session": s, "loi": champ[m[iLoi]]["titre"][:60], "observation": m[iObs].strip(),
                                    "motif": motif[0]})
        if c == "A":
            sans_date = not m[iDP].strip()
            A_sans_date += sans_date
            if re.search(r"\bdiff[ée]r[ée]e?s?\b", m[iObs] + " " + m[iObj], re.I):  # pas « différent », « différer »
                differ_A[s] += 1
                differ_sans_date += sans_date
        if champ[m[iLoi]]["titre"].startswith("LOI n° 2025-138 "):
            cas.append((e, m[iObs], m[iLoi]))
    for j, v in champ.items():
        pl = par_loi[j]
        if v["na"] != pl["appliqué"] + pl["en attente d'application"] or v["napp"] != pl["appliqué"]:
            raise Arret("A5 : %s : fichier des lois (%d/%d) != mesures (%d appliquees, %d en attente)"
                        % (rj[j]["num_loi"], v["napp"], v["na"], pl["appliqué"], pl["en attente d'application"]))
    nmes = len(M) - 1
    if nmes != sum(sum(c.values()) for c in cl.values()):
        raise Arret("A5 : bilan des mesures")
    if obs_large != sum(obs_acte.values()) + len(ecartes):
        raise Arret("A5 bis : filtre large %d != retenu %d + ecarte %d" % (obs_large, sum(obs_acte.values()), len(ecartes)))
    if sum(tri.values()) != nS or tri["acte_en_tete"] != sum(obs_acte.values()):
        raise Arret("A5 bis : tri des « sans objet » : entre %d, classe + indetermine %d ; acte en tete %d != filtre %d"
                    % (nS, sum(tri.values()), tri["acte_en_tete"], sum(obs_acte.values())))
    # Phrase de la page : l'observation dit « le plus souvent » déjà appliquée, base légale modifiée ou aucune mesure nécessaire.
    if not 2 * (tri["deja_appliquee"] + tri["base_legale_modifiee"] + tri["aucune_mesure_necessaire"]) > nS:
        raise Arret("A5 bis : « le plus souvent » (deja appliquee, base legale, aucune mesure) faux : a reecrire")
    g.append("A5 : %d mesures, N = P + A + S + U ; coherence loi par loi avec le fichier des lois du meme producteur" % nmes)
    g.append("A5 bis : « sans objet » commencant par un acte : %d = %d references + %d ecartes a motif nomme ; tri : %d = "
             "%d classes + %d indetermines" % (obs_large, sum(obs_acte.values()), len(ecartes), nS, nS - tri["indetermine"],
                                                tri["indetermine"]))

    # --- A8 : statut des lois, quatre prédicats définis séparément
    statut = collections.defaultdict(collections.Counter)
    statut_loi = {}
    for j, v in champ.items():
        att = par_loi[j]["en attente d'application"]
        pred = {"directe": v["directe"], "sans_echeancier": v["sans_ech"], "attente": att > 0,
                "toutes": not v["directe"] and not v["sans_ech"] and v["na"] > 0 and att == 0 and v["napp"] == v["na"]}
        vrais = [k for k, b in pred.items() if b]
        if len(vrais) != 1:
            raise Arret("A8 : %s : %d statut(s) %s" % (rj[j]["num_loi"], len(vrais), vrais))
        statut[v["session"]][vrais[0]] += 1
        statut_loi[j] = vrais[0]
    for s in SESSIONS:
        if sum(statut[s].values()) != N[s]:
            raise Arret("A8 : %s : statuts %d != champ %d" % (s, sum(statut[s].values()), N[s]))
    tse = sum(statut[s]["sans_echeancier"] for s in SESSIONS)
    if tse != 1:  # la page écrit « une n'avait pas d'échéancier »
        raise Arret("A8 : %d lois sans echeancier : la phrase « une n'avait pas d'echeancier » est a reecrire" % tse)
    m36 = re.search(r"sur (\d+) étaient", cit["cit_802_36"])
    if not m36 or int(m36.group(1)) != N["2024-2025"]:
        raise Arret("A8 : 2024-2025 : le Senat compte %s lois, le barometre %d : « sur les memes lois » faux"
                    % (m36.group(1) if m36 else "?", N["2024-2025"]))
    g.append("A8 : statut des lois : chaque loi dans un seul des quatre statuts, somme = champ par session ; 2024-2025 : %d lois "
             "dans les deux sources" % N["2024-2025"])
    # A8 bis (passe B2, panel « après » ; libellé requalifié en B3) : part des lois en attente parmi les lois que le baromètre
    # classe avec au moins une mesure à prendre, en attente ou prise (en attente + toutes reçues ; la loi sans échéancier hors
    # des deux). Rapport entre deux catégories du baromètre à la date du relevé, pas un besoin initial de mesures : une loi
    # classée « sans mesure à prendre » peut en avoir prévu une (2025-138, garde A6).
    # Phrase de la page : « soit <pct> : environ une sur deux ».
    l_att = sum(statut[s]["attente"] for s in SESSIONS)
    l_mes = l_att + sum(statut[s]["toutes"] for s in SESSIONS)
    if not 0.45 <= l_att / l_mes <= 0.55:
        raise Arret("A8 bis : %d lois en attente sur %d classees avec au moins une mesure a prendre (%.1f %%) : « environ une "
                    "sur deux » faux"
                    % (l_att, l_mes, 100 * l_att / l_mes))
    g.append("A8 bis : %d lois en attente sur %d classees avec au moins une mesure a prendre, en attente ou prise (%.1f %%), "
             "« environ une sur deux »"
             % (l_att, l_mes, 100 * l_att / l_mes))

    if not (cas and all(e == "sans objet" and re.match(r"\s*Arr[êe]t[ée] du", o) for e, o, _ in cas)
            and statut_loi[cas[0][2]] == "directe"):
        raise Arret("A6 : cas 2025-138 : le barometre ne la porte plus « sans objet » avec un arrete, ou la loi n'est plus "
                    "« sans mesure a prendre » : texte a revoir")
    g.append("A6 : 2025-138 : %d mesure(s) « sans objet » portant un arrete au barometre, loi sans mesure a prendre ; "
             "en attente au SGG (31/12/2025)" % len(cas))
    tot = collections.Counter()
    for s in SESSIONS:
        tot.update(cl[s])
    if not tot["A"] > 0 or not cl["2017-2018"]["A"] > 0:
        raise Arret("A5 : « des mesures attendent encore » faux")

    # --- A9 : « + 4 points » du Sénat en 2024-2025
    v66 = int(re.search(r"(\d+) % \(\+ (\d+) points\)", cit["cit_802_66"]).group(1))
    p4 = int(re.search(r"\(\+ (\d+) points\)", cit["cit_802_66"]).group(1))
    v62 = int(re.search(r"s'élève à (\d+) %", cit["cit_2324_62"]).group(1))
    v59 = [v for s, v, *_ in SERIE if s == "2023-2024"][0]
    if v66 - v62 != p4 or v62 == v59:
        raise Arret("A9 : « + %d points » : %d - %d ; taux 2023-2024 de la serie %g" % (p4, v66, v62, v59))
    g.append("A9 : « + %d points » = %d - %d (2023-2024 hors mesures differees), et non %d - %g" % (p4, v66, v62, v66, v59))

    r = {"lignes": lignes, "ct": ct, "ndesacc": ndesacc, "nregistre": len(reg), "conventions": sum(ecartees.values()),
         "cl": {s: dict(cl[s]) for s in SESSIONS}, "tot": dict(tot), "nmes": nmes, "obs_acte": dict(obs_acte),
         "obs_large": obs_large, "ecartes": ecartes, "tri": dict(tri), "nS": nS,
         "differ_A": dict(differ_A), "differ_sans_date": differ_sans_date, "A_sans_date": A_sans_date,
         "cas_2025_138": cas[0][1].strip(), "citations": cit, "cit_ce": cce, "cit_en": cit_en, "sgg": sgg,
         "statut": {s: dict(statut[s]) for s in SESSIONS}, "N": dict(N), "plus4": (v66, v62, p4, v59)}
    return r, g


def _cles_communes(r: dict, lang: str) -> dict:
    """Valeurs calculées, mêmes clés dans les deux langues (nombres par langue_generee)."""
    nb = fr if lang == "fr" else en
    lt = lambda n: lg.lettres(n, lang)  # noqa: E731
    pct = (lambda v: "%d %%" % v) if lang == "fr" else (lambda v: "%d%%" % v)
    t, ct, cl, st = r["tot"], r["ct"], r["cl"], r["statut"]
    l25 = r["lignes"][-1]
    tst = collections.Counter()
    for s in SESSIONS:
        tst.update(st[s])
    tri = collections.Counter(r["tri"])
    return {
        "nmes": nb(r["nmes"]), "P": nb(t.get("P", 0)), "A": nb(t.get("A", 0)), "S": nb(t.get("S", 0)), "U": nb(t.get("U", 0)),
        "A_pct": nb(100 * t.get("A", 0) / r["nmes"], 1),
        "A_1718": nb(cl["2017-2018"].get("A", 0)), "N_1718": nb(sum(cl["2017-2018"].values())),
        "A_2425": nb(cl["2024-2025"].get("A", 0)), "N_2425": nb(sum(cl["2024-2025"].values())),
        "differ_A": nb(sum(r["differ_A"].values())), "differ_1819": nb(r["differ_A"].get("2018-2019", 0)),
        "differ_1920": nb(r["differ_A"].get("2019-2020", 0)), "differ_sans_date": nb(r["differ_sans_date"]),
        "A_sans_date": nb(r["A_sans_date"]),
        "obs_acte": nb(sum(r["obs_acte"].values())), "obs_acte_2425": nb(r["obs_acte"].get("2024-2025", 0)),
        "obs_large": nb(r["obs_large"]), "obs_ecartes": lt(len(r["ecartes"])),
        "nS": nb(r["nS"]), "tri_deja": nb(tri["deja_appliquee"]), "tri_base": nb(tri["base_legale_modifiee"]),
        "tri_acte": nb(tri["acte_en_tete"]), "tri_aucune": nb(tri["aucune_mesure_necessaire"]),
        "tri_event": nb(tri["mesure_eventuelle_non_utilisee"]), "tri_nonprise": lt(tri["mesure_non_prise"]),
        "tri_indet": nb(tri["indetermine"]),
        "cas_2025_138": r["cas_2025_138"],
        "nlois": nb(r["nregistre"]), "conventions": nb(r["conventions"]), "ndesacc": nb(r["ndesacc"]),
        "ct_session": ct["session"], "ct_baro": nb(ct["baro"]), "ct_senat": nb(ct["senat"]), "ct_N": nb(ct["N"]),
        "s25_baro": nb(l25["baro"]), "s25_senat": nb(l25["senat"]), "s25_publie": nb(l25["senat_publie"]),
        "s25_N": nb(l25["N"]),
        "L_dir": nb(tst["directe"]), "L_att": nb(tst["attente"]), "L_tout": nb(tst["toutes"]), "L_se": lt(tst["sans_echeancier"]),
        "L_mes": nb(tst["attente"] + tst["toutes"]),
        "L_att_pct_mes": pct(round(100 * tst["attente"] / (tst["attente"] + tst["toutes"]))),
        "L_att_1718": nb(st["2017-2018"].get("attente", 0)), "L_N_1718": nb(r["N"]["2017-2018"]),
        "s25_dir": nb(st["2024-2025"].get("directe", 0)), "s25_tout": nb(st["2024-2025"].get("toutes", 0)),
        "s25_dirtout": nb(st["2024-2025"].get("directe", 0) + st["2024-2025"].get("toutes", 0)),
        "nsessions": lt(len(SESSIONS)), "nautres": lt(len(SESSIONS) - 1), "nsegments": lt(len(SEGMENTS)),
        "sgg16_taux": pct(r["sgg"]["sgg16"]["taux"]), "sgg17_taux": pct(r["sgg"]["sgg17"]["taux"]),
        "sgg16_n": nb(r["sgg"]["sgg16"]["mesures"]), "sgg17_n": nb(r["sgg"]["sgg17"]["mesures"]),
        "s1718_hd": pct(int(re.search(r"- (\d+) % si on exclut", r["citations"]["cit_senat_1718"]).group(1))),
        "sgg1718": pct(int(re.search(r"taux d'application de (\d+) %", r["citations"]["cit_sgg_1718"]).group(1))),
        "plus4": nb(r["plus4"][2]), "s2324_hd": pct(r["plus4"][1]), "s2324": pct(r["plus4"][3]), "s2425": pct(r["plus4"][0]),
    }


def affichage(r: dict) -> dict:
    A = _cles_communes(r, "fr")
    A.update({
        "releve": RELEVE,
        "releve_le": "05/10/2026 (baromètre de l'application des lois) ; rapports du Sénat lus le 06/10/2026 ; bilan du SGG au "
                     "31/12/2025, page relue le 12/10/2026 ; décisions du Conseil d'État lues le 12/10/2026",
    })
    for k, cle in (("senat_1819", "cit_senat_1819"), ("sgg_1819", "cit_sgg_1819")):
        m = re.search(r"(\d+(?:,\d+)?) %", r["citations"][cle])
        A[k] = m.group(1) + " %"
    A.update(r["citations"])
    A.update(r["cit_ce"])
    A["cit_cciv"] = norm(CIT_CCIV)
    A["cit_cciv_urg"] = norm(CIT_CCIV_URG)
    for k, c in CIT_CONST.items():
        A["cit_" + k] = norm(c)
    A["cit_sgg16_def"] = norm(CIT_SGG["sgg16_def"])
    A["cit_sgg17_def"] = norm(CIT_SGG["sgg17_def"])
    A.update({k + "_tr": v for k, v in TR.items()})
    return A


def affichage_en(r: dict, A_fr: dict) -> dict:
    A = _cles_communes(r, "en")
    A.update({
        "releve": "5 October 2026",
        "releve_le": "5 October 2026 (barometer of the application of laws); Senate reports read on 6 October 2026; General "
                     "Secretariat of the Government report at 31 December 2025, page reread on 12 October 2026; Conseil "
                     "d'État decisions read on 12 October 2026",
    })
    for k in ("senat_1819", "sgg_1819"):
        A[k] = A_fr[k].replace(" ", "").replace(",", ".")
    const = {"cit_" + k for k in CONST_EN}
    for k, v in A_fr.items():  # citations françaises : l'original, suivi de sa traduction (_tr)
        if k.startswith("cit_") and k not in const:
            A[k] = v
    A.update(r["cit_en"])
    A.update({k + "_tr": v for k, v in TR.items()})
    return A


STATUTS = ("attente", "toutes", "directe", "sans_echeancier")


def _tableaux(r: dict, lang: str) -> dict:
    nb = fr if lang == "fr" else en
    sur = "sur" if lang == "fr" else "out of"
    lois = []
    for x in r["lignes"]:
        b = "%d %s %d" % (x["D"], sur, x["N"]) if x["U"] == 0 else (
            ("de %d à %d sur %d" if lang == "fr" else "%d to %d out of %d") % (x["D"], x["D"] + x["U"], x["N"]))
        autre = " (%d dans une autre page du même rapport)" if lang == "fr" else " (%d on another page of the same report)"
        lois.append([x["session"], str(x["N"]), str(x["baro"]),
                     str(x["senat"]) + (autre % x["senat_publie"] if x["senat_publie"] != x["senat"] else ""), b])
    mes = [[s, nb(sum(r["cl"][s].values()))] + [nb(r["cl"][s].get(k, 0)) for k in "PASU"] for s in SESSIONS]
    mes.append(["Total", nb(r["nmes"])] + [nb(r["tot"].get(k, 0)) for k in "PASU"])
    st = [[s, nb(r["N"][s])] + [nb(r["statut"][s].get(k, 0)) for k in STATUTS] for s in SESSIONS]
    tt = collections.Counter()
    for s in SESSIONS:
        tt.update(r["statut"][s])
    st.append(["Total", nb(sum(r["N"][s] for s in SESSIONS))] + [nb(tt[k]) for k in STATUTS])
    g = r["sgg"]
    if lang == "fr":
        serie = [[s, ("%g" % v).replace(".", ",") + " %", SEGMENTS[seg], pg.split("|")[0]] for s, v, pg, _, seg in SERIE]
        serie.insert(17, [REVISION[0], "60 % (rapport suivant ; variante non établie)", SEGMENTS[5], REVISION[2].split("|")[0]])
        taux = [["Secrétariat général du Gouvernement, bilan semestriel, XVIe législature",
                 "lois votées du 1er juillet 2022 au 9 juin 2024 qui appellent des décrets d'application",
                 "décrets (%s mesures)" % nb(g["sgg16"]["mesures"]), "31 décembre 2025", "%d %%" % g["sgg16"]["taux"]],
                ["Secrétariat général du Gouvernement, bilan semestriel, XVIIe législature",
                 "lois publiées du 18 juillet 2024 au 30 juin 2025 qui appellent des décrets ou des arrêtés d'application",
                 "décrets ou arrêtés (%s mesures)" % nb(g["sgg17"]["mesures"]), "31 décembre 2025", "%d %%" % g["sgg17"]["taux"]],
                ["Sénat, rapport sur la session 2024-2025", "lois de la session 2024-2025 (1er octobre au 30 septembre)",
                 "mesures prévues, non éventuelles et non différées au-delà du 31 mars 2026", "31 mars 2026",
                 "%d %%" % r["plus4"][0]]]
        return {
            "statut": {"entetes": ["Session", "Lois promulguées (hors conventions)", "Au moins une mesure en attente",
                                   "Toutes mesures prises", "Sans mesure à prendre", "Sans échéancier"], "lignes": st},
            "lois": {"entetes": ["Session", "Lois promulguées (hors conventions)", "D'application directe selon le baromètre",
                                 "Selon le Sénat", "Bornes : directes pour les deux sources, puis en comptant les classements divergents"],
                     "lignes": lois},
            "mesures": {"entetes": ["Session de la loi", "Mesures", "Acte publié identifié", "En attente", "Indiquées sans objet",
                                    "Statut incomplet"], "lignes": mes},
            "serie": {"entetes": ["Session", "Taux publié par le Sénat", "Définition (segment)", "Document"], "lignes": serie},
            "taux": {"entetes": ["Producteur et document", "Lois couvertes", "Mesures comptées", "Données arrêtées au", "Taux publié"],
                     "lignes": taux},
        }
    serie = [[s, ("%g" % v) + "%", SEGMENTS_EN[seg], pg.split("|")[0]] for s, v, pg, _, seg in SERIE]
    serie.insert(17, [REVISION[0], "60% (following report; variant not established)", SEGMENTS_EN[5], REVISION[2].split("|")[0]])
    taux = [["General Secretariat of the Government, half-yearly report, 16th legislature",
             "laws passed from 1 July 2022 to 9 June 2024 that call for implementing decrees",
             "decrees (%s measures)" % nb(g["sgg16"]["mesures"]), "31 December 2025", "%d%%" % g["sgg16"]["taux"]],
            ["General Secretariat of the Government, half-yearly report, 17th legislature",
             "laws published from 18 July 2024 to 30 June 2025 that call for implementing decrees or orders",
             "decrees or orders (%s measures)" % nb(g["sgg17"]["mesures"]), "31 December 2025", "%d%%" % g["sgg17"]["taux"]],
            ["Senate, report on the 2024-2025 session", "laws of the 2024-2025 session (1 October to 30 September)",
             "planned measures, excluding optional measures and measures deferred beyond 31 March 2026", "31 March 2026",
             "%d%%" % r["plus4"][0]]]
    return {
        "statut": {"entetes": ["Session", "Laws promulgated (excluding treaties)", "At least one measure pending",
                               "All measures taken", "No measure to take", "No schedule"], "lignes": st},
        "lois": {"entetes": ["Session", "Laws promulgated (excluding treaties)", "Directly applicable according to the barometer",
                             "According to the Senate", "Bounds: directly applicable for both sources, then counting divergent classifications"],
                 "lignes": lois},
        "mesures": {"entetes": ["Session of the law", "Measures", "Identified published instrument", "Pending",
                                "Classified “not applicable” (sans objet)", "Incomplete status"], "lignes": mes},
        "serie": {"entetes": ["Session", "Rate published by the Senate", "Definition (segment)", "Document"], "lignes": serie},
        "taux": {"entetes": ["Producer and document", "Laws covered", "Measures counted", "Data as at", "Published rate"],
                 "lignes": taux},
    }


def tableaux(r: dict) -> dict:
    return _tableaux(r, "fr")


def tableaux_en(r: dict) -> dict:
    return _tableaux(r, "en")


# ------------------------------------------------------------------ figures
W = 720
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCES_M = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
              "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
LANG = "fr"
COUL_STATUT = {"attente": ORANGE, "toutes": BLEU, "directe": GRIS_CLAIR, "sans_echeancier": GRIS}


def nb(n) -> str:
    return en(n) if LANG == "en" else fr(n)


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def cadre(H, ident, titre, sous, desc) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def blocs_pied(src, note, mobile=False) -> list:
    return [(src, INK2, "pied-source"), (note, INK2, "pied-note"), ((LICENCES_M if mobile else LICENCES)[LANG], MUTED, "pied-licence")]


def legende(e, y, items) -> None:
    x = 0
    for col, lab in items:
        e.append('<rect x="%d" y="%d" width="11" height="11" fill="%s"/>' % (x, y - 9, col))
        e.append(txt(x + 16, y, lab, 10, INK2))
        x += 16 + 6.2 * len(lab) + 18


_SEG_FR, _SEG_EN = lg.lettres(len(SEGMENTS), "fr"), lg.lettres(len(SEGMENTS), "en")
T = {
    "fr": {"src0": "Baromètre de l'application des lois (Assemblée nationale, LexImpact ; données DILA), état au " + RELEVE,
           "note0": "Lois promulguées par session (1er oct.-30 sept.), hors conventions. Statuts tirés des étiquettes du baromètre : "
                    "« en attente » ne veut pas dire « en retard » ; « sans mesure à prendre » dépend de l'étiquette « sans objet » et "
                    "ne prouve pas que la loi ne prévoyait aucune mesure.",
           "t0": "Les lois promulguées depuis 2017 attendent-elles encore une mesure ?",
           "s0": "nombre de lois par session ; statuts administratifs à la date du relevé (%s)" % RELEVE,
           "l0": ["au moins une mesure en attente", "toutes mesures prises", "sans mesure à prendre", "sans échéancier"],
           "e0": "{a} en attente sur {n} lois",
           "d0": "Barres horizontales, une par session de 2017-2018 à 2024-2025, lois promulguées hors conventions, par statut au {r} : "
                 "{liste}. Les valeurs sont dans le tableau sous la figure.",
           "d0s": "{s} : {n} lois, dont {a} avec au moins une mesure en attente, {t} toutes mesures prises, {d} sans mesure à prendre{e}",
           "d0e": ", {x} sans échéancier",
           "src1": "Baromètre de l'application des lois (Assemblée nationale, LexImpact ; données DILA), état au " + RELEVE,
           "note1": "Mesures des lois promulguées par session (1er oct.-30 sept.), hors conventions. État à la date du relevé : ni un "
                    "taux historique, ni une efficacité.",
           "t1": "Les mesures d'application des lois, par session de la loi", "s1": "nombre de mesures recensées et leur état au %s" % RELEVE,
           "d1": "Barres horizontales, une par session de 2017-2018 à 2024-2025 : mesures avec un acte publié identifié, en attente, "
                 "indiquées sans objet, statut incomplet. Au total {nmes} mesures, dont {A} en attente. Par session : {liste}. "
                 "Les valeurs sont dans le tableau sous la figure.",
           "d1s": "{s} : {n} mesures, dont {a} en attente",
           "l1": ["acte publié identifié", "en attente", "indiquées sans objet", "statut incomplet"],
           "attente": "{} en attente", "e1": "{a} en attente sur {n} mesures",
           "src2": "Baromètre de l'application des lois (état au %s) ; rapports annuels du Sénat sur l'application des lois" % RELEVE,
           "note2": "Gris : lois que le baromètre et le Sénat classent différemment. 2024-2025 : le Sénat publie {senat} lois "
                    "d'application directe dans sa synthèse et {publie} ailleurs dans le même rapport ; les {ecart} de plus, sans liste "
                    "nominative, sont en gris. Trait noir : la moitié des lois.",
           "t2": "Les lois classées d'application directe, selon deux sources",
           "s2": "nombre de lois promulguées, hors conventions ; trait noir : la moitié des lois de la session",
           "d2": "Barres horizontales, une par session : lois d'application directe pour les deux sources, lois classées différemment "
                 "par le baromètre et par le Sénat, lois qu'aucune des deux ne classe d'application directe. Par session : {liste}. En {ct_session}, le baromètre "
                 "compte {ct_baro} lois d'application directe sur {ct_N}. Les valeurs sont dans le tableau sous la figure.",
           "d2s": "{s} : {n} lois, {d} directes pour les deux sources, {u} classées différemment",
           "l2": ["application directe (les deux sources)", "classement divergent", "non directes (les deux sources)"],
           "lois": "{} lois",
           "e2": "{d} directes, {u} divergentes, sur {n}",
           "src3": "Sénat, bilans annuels de l'application des lois, 2003-2026 (taux tels que publiés, page citée dans le tableau)",
           "note3": "%s définitions successives : ne pas relier les segments. Deux valeurs pour une session et une rupture de "
                    "définition sont deux faits distincts. 2009-2010 non représentée : date d'arrêté du taux non établie."
                    % _SEG_FR.capitalize(),
           "t3": "Le taux d'application des lois publié par le Sénat, 2002-2003 à 2024-2025",
           "s3": "en %% des mesures attendues ; %s définitions successives, fonds alternés : un segment ne se compare pas à un autre" % _SEG_FR,
           "d3": "Points par session, regroupés en %s segments séparés par des ruptures de définition : {liste}. Pour 2019-2020, le "
                 "rapport suivant écrit 60 %% (cercle vide). Les valeurs, leur document et leur définition sont dans le tableau sous "
                 "la figure." % _SEG_FR,
           "d3s": "{s} : {v} % (segment {g})",
           "pct": "{} %", "leg3": "1 à 6 : segments (définitions dans le tableau) ; cercle vide : 2019-2020 selon le rapport suivant",
           "leg3m": "1 à 6 : segments ; cercle vide : 2019-2020 selon le rapport suivant"},
    "en": {"src0": "Barometer of the application of laws (National Assembly, LexImpact; DILA data), status at 5 October 2026",
           "note0": "Laws promulgated per session (1 Oct.-30 Sept.), excluding treaties. Statuses from the barometer's labels: "
                    "'pending' does not mean 'late'; 'no measure to take' depends on the 'not applicable' label and does not prove "
                    "that the law provided for no measure.",
           "t0": "Are the laws promulgated in France since 2017 still waiting for a measure?",
           "s0": "number of laws per session; administrative statuses at the reading date (5 October 2026)",
           "l0": ["at least one measure pending", "all measures taken", "no measure to take", "no schedule"],
           "e0": "{a} pending out of {n} laws",
           "d0": "Horizontal bars, one per session from 2017-2018 to 2024-2025, laws promulgated excluding treaties, by status at {r}: "
                 "{liste}. The values are in the table below the figure.",
           "d0s": "{s}: {n} laws, {a} with at least one measure pending, {t} with all measures taken, {d} with no measure to take{e}",
           "d0e": ", {x} with no schedule",
           "src1": "Barometer of the application of laws (National Assembly, LexImpact; DILA data), status at 5 October 2026",
           "note1": "Measures of the laws promulgated per session (1 Oct.-30 Sept.), excluding treaties. Status at the reading date: "
                    "neither a historical rate nor efficiency.",
           "t1": "Implementing measures of French laws, by session of the law", "s1": "number of measures listed and their status at 5 October 2026",
           "d1": "Horizontal bars, one per session from 2017-2018 to 2024-2025: measures with an identified published instrument, "
                 "pending, classified as “not applicable”, incomplete status. In total {nmes} measures, {A} of them pending. By "
                 "session: {liste}. The values are in the table below the figure.",
           "d1s": "{s}: {n} measures, {a} pending",
           "l1": ["identified published instrument", "pending", "classified as “not applicable”", "incomplete status"],
           "attente": "{} pending", "e1": "{a} pending out of {n} measures",
           "src2": "Barometer of the application of laws (status at 5 October 2026); Senate annual reports on the application of laws",
           "note2": "Grey: laws that the barometer and the Senate classify differently. 2024-2025: the Senate publishes {senat} "
                    "directly applicable laws in its summary and {publie} elsewhere in the same report; the {ecart} extra laws, with no "
                    "list of names, are in grey. Black mark: half of the laws.",
           "t2": "Laws classified as directly applicable by two sources",
           "s2": "number of laws promulgated, excluding treaties; black mark: half of the session's laws",
           "d2": "Horizontal bars, one per session: laws directly applicable for both sources, laws classified differently by the "
                 "barometer and the Senate, laws that neither source classifies as directly applicable. By session: {liste}. In {ct_session}, the barometer counts "
                 "{ct_baro} directly applicable laws out of {ct_N}. The values are in the table below the figure.",
           "d2s": "{s}: {n} laws, {d} directly applicable for both sources, {u} classified differently",
           "l2": ["directly applicable (both sources)", "divergent classification", "not direct for either source"],
           "lois": "{} laws",
           "e2": "{d} direct, {u} divergent, out of {n}",
           "src3": "French Senate, annual reports on the application of laws, 2003-2026 (rates as published, page cited in the table)",
           "note3": "%s successive definitions: do not join the segments. Two values for one session and a change of definition are "
                    "two distinct facts. 2009-2010 not shown: cut-off date of the rate not established." % _SEG_EN.capitalize(),
           "t3": "The implementation rate of laws published by the French Senate, 2002-2003 to 2024-2025",
           "s3": "in %% of expected measures; %s successive definitions, alternating backgrounds: one segment does not compare with "
                 "another" % _SEG_EN,
           "d3": "Points by session, grouped in %s segments separated by changes of definition: {liste}. For 2019-2020, the following "
                 "report gives 60%% (open circle). The values, their document and their definition are in the table below the "
                 "figure." % _SEG_EN,
           "d3s": "{s}: {v}% (segment {g})",
           "pct": "{}%", "leg3": "1 to 6: segments (definitions in the table); open circle: 2019-2020 according to the following report",
           "leg3m": "1 to 6: segments; open circle: 2019-2020 according to the following report"},
}


def _desc_statut(r: dict, A: dict) -> str:
    L = T[LANG]
    parts = []
    for s in SESSIONS:
        st = r["statut"][s]
        e = L["d0e"].format(x=nb(st["sans_echeancier"])) if st.get("sans_echeancier") else ""
        parts.append(L["d0s"].format(s=s, n=nb(r["N"][s]), a=nb(st.get("attente", 0)), t=nb(st.get("toutes", 0)),
                                     d=nb(st.get("directe", 0)), e=e))
    return L["d0"].format(r=A["releve"], liste="; ".join(parts))


def _desc_mesures(r: dict, A: dict) -> str:
    L = T[LANG]
    liste = "; ".join(L["d1s"].format(s=s, n=nb(sum(r["cl"][s].values())), a=nb(r["cl"][s].get("A", 0))) for s in SESSIONS)
    return L["d1"].format(liste=liste, **A)


def _desc_lois(r: dict, A: dict) -> str:
    L = T[LANG]
    liste = "; ".join(L["d2s"].format(s=x["session"], n=x["N"], d=x["D"], u=x["U"]) for x in r["lignes"])
    return L["d2"].format(liste=liste, **A)


def _val_serie(v) -> str:
    return ("%g" % v) if LANG == "en" else ("%g" % v).replace(".", ",")


def _desc_serie() -> str:
    L = T[LANG]
    return L["d3"].format(liste="; ".join(L["d3s"].format(s=s, v=_val_serie(v), g=g) for s, v, _, _, g in SERIE))


def _barres(e, rows, x0, x1, y0, pas, vmax, graduations, moitie=False) -> None:
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    for v in graduations:
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * len(rows) + 2, GRID))
        e.append(txt(X(v), y0 + pas * len(rows) + 16, nb(v), 9, MUTED, "middle"))
    for i, (lab, segs, etiq, n) in enumerate(rows):
        y = y0 + i * pas
        e.append(txt(0, y + 15, lab, 10, INK))
        a = 0
        for v, col in segs:
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        if moitie:
            e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2"/>' % (X(n / 2), y - 3, X(n / 2), y + 23, INK))
        e.append(txt(X(a) + 4, y + 14, etiq, 9, INK2))


def _barres_m(ident, titre, desc, sous, leg, rows, vmax, src, note) -> str:
    """Version téléphone (300 de large, police jamais sous 13,5) : par session, le libellé, la barre, puis l'étiquette en gras."""
    e, y = pf.tete_mobile(ident, titre, desc, INK, FONT, 30)
    for l in pf.coupe(sous, 36):
        y += 18
        e.append('<text x="0" y="%d" font-size="13.5" fill="%s">%s</text>' % (y, INK2, esc(l)))
    y += 6
    for col, lab in leg:
        y += 19
        e.append('<rect x="0" y="%d" width="12" height="12" fill="%s"/>' % (y - 11, col))
        e.append('<text x="17" y="%d" font-size="13.5" fill="%s">%s</text>' % (y, INK2, esc(lab)))
    y += 10
    for lab, segs, etiq, n in rows:
        y += 18
        e.append('<text x="0" y="%d" font-size="13.5" fill="%s">%s</text>' % (y, INK, esc(lab)))
        y += 5
        a = 0
        for v, col in segs:
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="14" fill="%s"/>' % (300 * a / vmax, y, 300 * v / vmax, col))
            a += v
        y += 14 + 16
        e.append('<text x="0" y="%d" font-size="13.5" font-weight="600" fill="%s">%s</text>' % (y, INK2, esc(etiq)))
        y += 6
    return pf.pied_mobile(e, y + 8, blocs_pied(src, note, True), GRID)


def _rows_statut(r):
    L = T[LANG]
    return [(s, [(r["statut"][s].get(k, 0), COUL_STATUT[k]) for k in STATUTS],
             L["e0"].format(a=nb(r["statut"][s].get("attente", 0)), n=nb(r["N"][s])), r["N"][s]) for s in SESSIONS]


def fig_statut(r: dict, A: dict) -> str:
    L = T[LANG]
    e = cadre(330, "at", L["t0"], L["s0"], _desc_statut(r, A))
    legende(e, 58, list(zip([COUL_STATUT[k] for k in STATUTS], L["l0"])))
    _barres(e, _rows_statut(r), 78, W - 150, 74, 28, 70, range(0, 71, 10))
    return pf.pied(e, 330 + 2, W, blocs_pied(L["src0"], L["note0"]), GRID)


def fig_statut_m(r: dict, A: dict) -> str:
    L = T[LANG]
    return _barres_m("atm", L["t0"], _desc_statut(r, A), L["s0"], list(zip([COUL_STATUT[k] for k in STATUTS], L["l0"])),
                     _rows_statut(r), 70, L["src0"], L["note0"])


def _rows_mesures(r, mobile):
    L = T[LANG]
    out = []
    for s in SESSIONS:
        c = r["cl"][s]
        n = sum(c.values())
        et = L["e1"].format(a=nb(c.get("A", 0)), n=nb(n)) if mobile else L["attente"].format(nb(c.get("A", 0)))
        out.append((s, [(c.get(k, 0), col) for k, col in (("P", BLEU), ("A", ORANGE), ("S", GRIS_CLAIR), ("U", GRIS))], et, n))
    return out


def fig_mesures(r: dict, A: dict) -> str:
    L = T[LANG]
    e = cadre(330, "am", L["t1"], L["s1"], _desc_mesures(r, A))
    legende(e, 58, list(zip((BLEU, ORANGE, GRIS_CLAIR, GRIS), L["l1"])))
    _barres(e, _rows_mesures(r, False), 78, W - 46, 74, 28, 1000, range(0, 1001, 250))
    return pf.pied(e, 330 + 2, W, blocs_pied(L["src1"], L["note1"]), GRID)


def fig_mesures_m(r: dict, A: dict) -> str:
    L = T[LANG]
    return _barres_m("amm", L["t1"], _desc_mesures(r, A), L["s1"], list(zip((BLEU, ORANGE, GRIS_CLAIR, GRIS), L["l1"])),
                     _rows_mesures(r, True), 1000, L["src1"], L["note1"])


def _rows_lois(r, mobile):
    L = T[LANG]
    out = []
    for x in r["lignes"]:
        et = L["e2"].format(d=x["D"], u=x["U"], n=x["N"]) if mobile else L["lois"].format(x["N"])
        out.append((x["session"], [(x["D"], BLEU), (x["U"], GRIS), (x["N"] - x["D"] - x["U"], GRIS_CLAIR)], et, x["N"]))
    return out


def _note2(r: dict) -> str:
    """Pied de la figure des lois : les deux effectifs du Sénat pour 2024-2025 (synthèse et autre page du même rapport)."""
    l25 = r["lignes"][-1]
    return T[LANG]["note2"].format(senat=nb(l25["senat"]), publie=nb(l25["senat_publie"]),
                                   ecart=nb(l25["senat_publie"] - l25["senat"]))


def fig_lois(r: dict, A: dict) -> str:
    L = T[LANG]
    e = cadre(330, "al", L["t2"], L["s2"], _desc_lois(r, A))
    legende(e, 58, list(zip((BLEU, GRIS, GRIS_CLAIR), L["l2"])))
    _barres(e, _rows_lois(r, False), 78, W - 60, 74, 28, 70, range(0, 71, 10), moitie=True)
    return pf.pied(e, 330 + 2, W, blocs_pied(L["src2"], _note2(r)), GRID)


def fig_lois_m(r: dict, A: dict) -> str:
    L = T[LANG]
    return _barres_m("alm", L["t2"], _desc_lois(r, A), L["s2"], list(zip((BLEU, GRIS, GRIS_CLAIR), L["l2"])),
                     _rows_lois(r, True), 70, L["src2"], _note2(r))


def fig_serie(r: dict, A: dict) -> str:
    sess = ["%d-%d" % (a, a + 1) for a in range(2002, 2025)]
    x0, x1, y0, y1 = 40, W - 10, 74, 272
    bw = (x1 - x0) / len(sess)
    X = lambda s: x0 + (sess.index(s) + 0.5) * bw  # noqa: E731
    Y = lambda v: y1 - v / 100 * (y1 - y0)  # noqa: E731
    L = T[LANG]
    e = cadre(330, "as", L["t3"], L["s3"], _desc_serie())
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
    return pf.pied(e, 330 + 2, W, blocs_pied(L["src3"], L["note3"]), GRID)


def fig_serie_m(r: dict, A: dict) -> str:
    """Version téléphone : une ligne par session, le point sur une échelle de 0 à 100 %, la valeur en gras ; segments en fonds
    alternés, numérotés à droite ; la valeur de 2019-2020 du rapport suivant en cercle vide, sur sa propre ligne."""
    L = T[LANG]
    e, y = pf.tete_mobile("asm", L["t3"], _desc_serie(), INK, FONT, 30)
    for l in pf.coupe(L["s3"], 36):
        y += 18
        e.append('<text x="0" y="%d" font-size="13.5" fill="%s">%s</text>' % (y, INK2, esc(l)))
    xa, xb = 84, 214
    X = lambda v: xa + v / 100 * (xb - xa)  # noqa: E731
    y += 24
    for v in (0, 50, 100):
        e.append('<text x="%.1f" y="%d" font-size="13.5" fill="%s" text-anchor="middle">%s</text>'
                 % (X(v), y, MUTED, esc(L["pct"].format(v))))
    y += 6
    pas = 19
    lignes = [(s, v, seg, False) for s, v, _, _, seg in SERIE]
    lignes.insert(17, (REVISION[0], REVISION[1], 5, True))
    for k, seg in enumerate(SEGMENTS):
        grp = [x for x in lignes if x[2] == seg]
        if k % 2 == 0:
            e.append('<rect x="0" y="%d" width="300" height="%d" fill="#f3f2ee"/>' % (y, pas * len(grp)))
        e.append('<text x="298" y="%d" font-size="13.5" fill="%s" text-anchor="end">%s</text>' % (y + 14, MUTED, seg))
        for s, v, _, rev in grp:
            if not rev:
                e.append('<text x="2" y="%d" font-size="13.5" fill="%s">%s</text>' % (y + 14, INK, esc(s)))
            e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (xa, y + 9.5, xb, y + 9.5, GRID))
            if rev:
                e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (X(v), y + 9.5, BLEU))
            else:
                e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (X(v), y + 9.5, BLEU))
            e.append('<text x="%d" y="%d" font-size="13.5" font-weight="600" fill="%s">%s</text>'
                     % (xb + 10, y + 14, INK2, esc(L["pct"].format(_val_serie(v)))))
            y += pas
    y += 6
    for l in pf.coupe(L["leg3m"], 38):
        y += 17
        e.append('<text x="0" y="%d" font-size="13.5" fill="%s">%s</text>' % (y, INK2, esc(l)))
    return pf.pied_mobile(e, y + 10, blocs_pied(L["src3"], L["note3"], True), GRID)


MONTRE = {
    "fr": {"statut": "Au {releve}, selon le baromètre, {L_att} des {nlois} lois promulguées d'octobre 2017 à septembre 2025, hors "
                     "conventions, comportaient encore au moins une mesure classée « en attente » ; {L_tout} avaient reçu toutes leurs "
                     "mesures et {L_dir} étaient classées sans mesure à prendre.",
           "mesures": "Au {releve}, sur les {nmes} mesures d'application recensées par le baromètre pour les lois promulguées "
                      "d'octobre 2017 à septembre 2025, {P} ont un acte publié identifié, {A} sont en attente, {S} sont indiquées "
                      "sans objet et {U} ont un statut incomplet.",
           "lois": "Les lois d'application directe restent sous la moitié dans {nautres} sessions sur {nsessions}, quelle que soit "
                   "la source ; en {ct_session}, le baromètre en compte {ct_baro} sur {ct_N}. Les deux sources classent "
                   "différemment {ndesacc} des {nlois} lois.",
           "serie": "Le taux publié par le Sénat repose sur {nsegments} définitions successives depuis 2002-2003 : les segments ne "
                    "se lisent pas comme une seule série."},
    "en": {"statut": "On {releve}, according to the barometer, {L_att} of the {nlois} laws promulgated in France from October 2017 "
                     "to September 2025, excluding treaties, still had at least one measure classified as pending; {L_tout} had "
                     "received all their measures and {L_dir} were classified as having no measure to take.",
           "mesures": "On {releve}, of the {nmes} implementing measures listed by the barometer for the laws promulgated in France "
                      "from October 2017 to September 2025, {P} have an identified published instrument, {A} are pending, {S} are "
                      "classified as “not applicable” (sans objet) and {U} have an incomplete status.",
           "lois": "Directly applicable laws stay below half in {nautres} sessions out of {nsessions}, whatever the source; in "
                   "{ct_session}, the barometer counts {ct_baro} out of {ct_N}. The two sources classify {ndesacc} of the {nlois} "
                   "laws differently.",
           "serie": "The rate published by the French Senate rests on {nsegments} successive definitions since 2002-2003: the "
                    "segments do not read as a single series."},
}
FIGS = ("statut", "mesures", "lois", "serie")


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    """Fiches « Réutiliser » : titre, source et précaution LUS dans le SVG servi (classes du pied commun)."""
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        out = []
        for ident in FIGS:
            fichier = "appliquer-%s%s" % (ident, suf)
            svg = figs[fichier + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            src, note, lic = pf.lire(svg, "pied-source"), pf.lire(svg, "pied-note"), pf.lire(svg, "pied-licence")
            if not src or not note or lic.replace(" ", " ") != LICENCES[lang]:
                raise Arret("fiche %s : pied illisible" % fichier)
            out.append(dict(id=ident, fichier=fichier, titre=titre, montre=MONTRE[lang][ident].format(**AA), source=src,
                            precaution=note))
        res[lang] = out
    return res


def csv_texte(r: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "session", "categorie", "valeur", "unite", "source"])
    for s in SESSIONS:
        for k in STATUTS:
            w.writerow(["lois_statut", s, k, r["statut"][s].get(k, 0), "lois", "barometre, etat au %s" % RELEVE])
    for x in r["lignes"]:
        for k, lab in (("N", "lois_promulguees_hors_conventions"), ("baro", "lois_directes_barometre"),
                       ("senat", "lois_directes_senat_liste"), ("D", "lois_directes_deux_sources"),
                       ("U", "lois_classement_incertain")):
            w.writerow(["lois", x["session"], lab, x[k], "lois", "barometre %s ; rapports du Senat" % RELEVE])
    for s in SESSIONS:
        for k, lab in (("P", "acte_publie_identifie"), ("A", "en_attente"), ("S", "sans_objet"), ("U", "statut_incomplet")):
            w.writerow(["mesures", s, lab, r["cl"][s].get(k, 0), "mesures", "barometre, etat au %s" % RELEVE])
    for k in [k for k, _ in TRI] + ["indetermine"]:
        w.writerow(["sans_objet_tri_observation", "2017-2025", k, r["tri"].get(k, 0), "mesures",
                    "barometre, etat au %s ; tri par regles ecrites (generateur), pas un reclassement" % RELEVE])
    for s, v, pg, _, seg in SERIE:
        w.writerow(["taux_senat", s, "segment_%d" % seg, v, "%", "Senat, %s" % pg.replace("|", " p. ")])
    w.writerow(["taux_senat", REVISION[0], "segment_5_rapport_suivant", REVISION[1], "%", "Senat, %s" % REVISION[2].replace("|", " p. ")])
    for k, leg in (("sgg16", "XVIe legislature, decrets"), ("sgg17", "XVIIe legislature, decrets ou arretes")):
        w.writerow(["taux_sgg", leg, "taux_au_31-12-2025", r["sgg"][k]["taux"], "%", "SGG, bilan semestriel au 31/12/2025"])
    return buf.getvalue()


def autotest(S: dict) -> list[str]:
    out = []
    hl = S["lois"][0]
    hm = S["mesures"][0]
    iObs = hm.index("Objectif initial de publication, observations")

    def reclasse(m):  # 2017-1754 : appliquée après ses décrets -> « directe » au registre
        for r in m["registre"]:
            if r["num_loi"] == "2017-1754":
                r["directe_baro"] = "oui"

    def convention(m):
        i = hl.index("Loi autorisant la ratification d'accords internationaux")
        for l in m["lois"][1:]:
            if l[i] == "oui":
                l[i] = "non"
                return

    def attente(m):
        for l in m["mesures"][1:]:
            if l[hm.index("État")] == "appliqué":
                l[hm.index("État")] = "en attente d'application"
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
                        l[hl.index("Loi d'application directe")] = "non"

    def sans_echeancier(m):  # une loi qui attend une mesure, déclarée aussi « sans échéancier » : deux statuts (A8)
        att = {l[1] for l in m["mesures"][1:] if l[hm.index("État")] == "en attente d'application"}
        for l in m["lois"][1:]:
            if l[2] in att:
                l[hl.index("Loi sans échéancier")] = "oui"
                return

    def ecarte_sans_motif(m):  # un « sans objet » qui commence par « Décret » sans référence ni motif connu (A5 bis)
        for l in m["mesures"][1:]:
            if l[hm.index("État")] == "sans objet" and not LARGE_ACTE.match(l[iObs]):
                l[iObs] = "Décret simple, sans référence"
                return

    def sgg_altere(m):  # le relevé du SGG modifié après coup : l'empreinte du navigateur ne tient plus (A7)
        m["sgg_sha"] = hashlib.sha256(m["sgg"].replace("87%", "88%").encode("utf-8")).hexdigest()

    def plus4(m):  # le taux 2023-2024 hors différées à 63 % dans la page ET dans le script : A7 passe, A9 mord
        k = "r24-710|3"
        m["pages"][k] = dict(m["pages"][k], texte=m["pages"][k]["texte"].replace("s'élève à 62 %", "s'élève à 63 %"))
        CITATIONS["cit_2324_62"] = ("r24-710|3", CITATIONS["cit_2324_62"][1].replace("62 %", "63 %"))
        TR["cit_2324_62"] = TR["cit_2324_62"].replace("62%", "63%")

    def ce_principe(m):  # la formule du délai raisonnable retirée de la décision de 2011 (A10)
        m["ce"]["343188"] = dict(m["ce"]["343188"], texte=m["ce"]["343188"]["texte"].replace("délai raisonnable", "délai"))

    def titre_convention(m):  # une loi écartée dont le titre n'autorise ni ratification, ni approbation, ni adhésion (A2)
        i = hl.index("Loi autorisant la ratification d'accords internationaux")
        for l in m["lois"][1:]:
            if l[i] == "oui":
                l[1] = "LOI n° 2099-1 relative a un objet interne"
                return

    def moitie(m):  # 40 lois en attente (hors 2017-2018) reçoivent toutes leurs mesures, fichier des lois tenu à jour (A8 bis)
        iE, iNapp = hm.index("État"), hl.index("Nombre de mesures appliquées")
        lois = {l[2]: l for l in m["lois"][1:]}
        att = collections.defaultdict(list)
        for l in m["mesures"][1:]:
            if l[iE] == "en attente d'application" and session(lois[l[1]][0]) != "2017-2018":
                att[l[1]].append(l)
        for j in sorted(att)[:40]:
            for l in att[j]:
                l[iE] = "appliqué"
            lois[j][iNapp] = str(int(lois[j][iNapp]) + len(att[j]))

    def paraphrase(m):  # l'al. 1 de l'art. 61 ne mentionne plus les lois organiques : la paraphrase de la page tombe (A1)
        m["const"]["art61"] = dict(m["const"]["art61"], texte=m["const"]["art61"]["texte"].replace("Les lois organiques, ", ""))

    sauve_cit, sauve_tr = dict(CITATIONS), dict(TR)
    for nom, mut, pref in (("2017-1754 reclassee directe", reclasse, "A3"), ("convention reintegree", convention, "A2"),
                           ("mesure appliquee -> en attente", attente, "A5"), ("citation SGG alteree", citation, "A7"),
                           ("2018-2019 sous la moitie", sous_moitie, "A4"),
                           ("loi en attente et sans echeancier", sans_echeancier, "A8"),
                           ("sans objet « Decret » sans motif", ecarte_sans_motif, "A5 bis"),
                           ("releve SGG modifie", sgg_altere, "A7"), ("2023-2024 hors differees a 63 %", plus4, "A9"),
                           ("formule du delai raisonnable retiree", ce_principe, "A10"),
                           ("art. 61 al. 1 sans lois organiques", paraphrase, "A1"),
                           ("convention au titre hors definition", titre_convention, "A2"),
                           ("40 lois en attente completees", moitie, "A8 bis")):
        m = copy.deepcopy(S)
        try:
            mut(m)
            calculer(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith(pref + " ") or str(e).startswith("mutation"):
                raise Arret("mutation %s : attendu %s, obtenu : %s" % (nom, pref, str(e)[:90]))
            out.append("%s -> %s" % (nom, str(e)[:70]))
        finally:
            CITATIONS.clear()
            CITATIONS.update(sauve_cit)
            TR.clear()
            TR.update(sauve_tr)
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
    # Règle du tri : une observation qui relève de deux règles est indéterminée, jamais classée.
    if trier("Décret non pris, mesure déjà appliquée par un autre texte") != "indetermine":
        raise Arret("tri : une observation a deux regles a ete classee, controle ABSENT")
    out.append("tri : observation a deux regles -> indetermine")
    return out


def figures(r: dict, A: dict, A_en: dict) -> dict:
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        for ident, f, fm in (("statut", fig_statut, fig_statut_m), ("mesures", fig_mesures, fig_mesures_m),
                             ("lois", fig_lois, fig_lois_m), ("serie", fig_serie, fig_serie_m)):
            n = "appliquer-%s%s" % (ident, suf)
            figs[n + ".svg"] = f(r, AA)
            figs[n + "-m.svg"] = fm(r, AA)
    LANG = "fr"
    return figs


def parite(figs: dict) -> list[str]:
    ecarts = []
    for n in [x for x in figs if x.endswith("-m.svg")]:
        corps = re.sub(r'<text class="pied-[a-z]+"[^>]*>[^<]*</text>', "", figs[n])  # pied : texte, pas des valeurs
        ecarts += ["%s : %s" % (n, x) for x in pf.parite(figs[n.replace("-m.svg", ".svg")], corps, pf.POLICE_M)]
    return ecarts


# A11 (passe B3, contre-expertise du rendu, P0) : un statut courant du baromètre ne dit pas ce qu'une loi « appelait ». La
# loi 2025-138, classée « sans mesure à prendre », prévoyait un arrêté (A6). Formules interdites, FR et EN, dans la prose
# et dans les sorties ; les citations des producteurs (« appellent des décrets », SGG) et les règles du tri ne sont pas
# visées par ces motifs.
PAGE_FR = ROOT / "content" / "une-loi-votee-s-applique-t-elle-tout-de-suite" / "_index.md"
PAGE_EN = ROOT / "content" / "une-loi-votee-s-applique-t-elle-tout-de-suite" / "_index.en.md"
PORTEE_INTERDITES = [re.compile(x, re.I) for x in (
    r"n['’]appel\w*\s+(?:aucune|pas)\b", r"\bappel\w*\s+au\s+moins\s+une\b", r"\bqui\s+appel\w*\s+(?:une|des)\s+mesures?\b",
    r"avaient\s+une\s+mesure\s+à\s+attendre", r"\bcall(?:s|ed|ing)?\s+for\s+(?:none|no\b|at\s+least|a\s+measure|measures)",
    r"had\s+a\s+measure\s+to\s+wait\s+for")]


def garde_portee(textes: dict) -> None:
    trouve = ["%s : %r" % (nom, m.group(0)) for nom, t in textes.items() for r in PORTEE_INTERDITES for m in r.finditer(html.unescape(t))]
    if trouve:
        raise Arret("A11 : statut courant du barometre dit comme besoin initial : " + " ; ".join(trouve[:4]))


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
    figs = figures(r, A, A_en)
    ec = parite(figs)
    if ec:
        raise Arret("figures telephone : " + " ; ".join(ec[:4]))
    # Témoin de la parité : une valeur faussée dans une figure téléphone doit être vue.
    faux = re.sub(r'(font-weight="600" fill="[^"]+">)(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 900),
                  figs["appliquer-statut-m.svg"], count=1)
    if faux == figs["appliquer-statut-m.svg"] or not pf.parite(figs["appliquer-statut.svg"], faux, pf.POLICE_M):
        raise Arret("figures telephone : la parite n'a pas vu une valeur faussee, controle ABSENT")
    for n in [x for x in figs if x.endswith("-m.svg")]:
        for x in pf.hors_cadre(figs[n], pf.LARGEUR_M):
            log("estimation hors cadre (le rendu tranche) : %s : %s" % (n, x))
    g.append("Figures : %d versions telephone a parite avec la version detaillee (FR et EN) ; temoin : valeur faussee vue"
             % len([x for x in figs if x.endswith("-m.svg")]))
    fi = fiches(figs, A, A_en)
    csvt = csv_texte(r)
    payload = {
        "releve_le": "2026-10-12",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Assemblée nationale et LexImpact (données DILA), Sénat, "
                    "Secrétariat général du Gouvernement, Légifrance, Conseil d'État",
        "meta": {"page": "https://" + PAGE_URL,
                 "protocole": "fiches de preuve v2, volet Appliquer, E1 à E3 ; phase B de la refonte du 12/10/2026",
                 "dates": "baromètre : version du 05/10/2026 ; rapports du Sénat : pages lues le 06/10/2026 (deux pages ajoutées le "
                          "12/10/2026) ; bilan du SGG au 31/12/2025 : page rendue relue le 12/10/2026 ; décisions du Conseil d'État : "
                          "lues le 12/10/2026 ; releve_le = date de la dernière lecture d'une source",
                 "sources": {"barometre": S["tetes"], "code_civil_art1": S["cciv"]["id"],
                             "constitution": {k: S["const"][k]["id"] for k in ("art10", "art13", "art21_exec", "art22", "art61")},
                             "senat_pages": {k: v["sha256_document"] for k, v in S["pages"].items()},
                             "sgg_bilan_31_12_2025": {"url": SGG_URL, "releve": SGG_FICHIER, "sha256_releve": SGG_SHA,
                                                      "sha256_texte_rendu_entier": PAGE_SGG_SHA,
                                                      "canal": "page rendue dans Chrome le 12/10/2026 (Légifrance refuse les "
                                                               "scripts) ; empreinte des lignes relevées calculée dans le navigateur"},
                             "conseil_etat": {num: {"fichier": f, "sha256": h,
                                                    "url": "https://www.conseil-etat.fr/fr/arianeweb/CE/decision/%s/%s"
                                                           % (re.search(r"(\d{4}-\d\d-\d\d)", f).group(1), num)}
                                              for num, (f, h) in CE.items()}},
                 "definitions": {
                     "session": "lois publiées du 1er octobre au 30 septembre suivant",
                     "directe": "loi classée d'application directe : par le baromètre quand son échéancier ne comporte, à la "
                                "date du relevé, aucune mesure autre que « sans objet » (un statut courant, pas la preuve que la "
                                "loi ne prévoyait aucune mesure : voir 2025-138) ; par le Sénat dans ses annexes",
                     "statut_loi": "attente : au moins une mesure « en attente d'application » ; toutes : non directe, avec "
                                   "échéancier, toutes ses mesures à appliquer appliquées ; directe : « Loi d'application directe » ; "
                                   "sans_echeancier : « Loi sans échéancier » (baromètre)",
                     "U_lois": "lois classées différemment par les deux sources, même quand une règle explique l'écart",
                     "P": "mesure à l'état « appliqué » avec un identifiant d'acte", "A": "mesure « en attente d'application »",
                     "S": "mesure indiquée « sans objet »", "U_mesures": "mesure « appliquée » sans identifiant d'acte",
                     "sans_objet_avec_acte": "observation « sans objet » qui COMMENCE par la référence d'un acte (« Arrêté du », "
                                             "« Décret du », « Décret n° ») ; les écartés du filtre large sont listés avec leur motif",
                     "tri_observations": "tri de l'observation du producteur par règles écrites (regles_tri) ; zéro ou plusieurs "
                                         "règles = indéterminé ; jamais un reclassement juridique"},
                 "limites": "état courant seulement : aucun taux à six ou douze mois ne se calcule sans historique daté "
                            "des échéanciers ; les taux du Sénat et du Gouvernement ne se comparent pas entre eux ni d'un "
                            "segment de définition à l'autre"},
        "gardes": g,
        "calcul": {"lois": r["lignes"], "lois_statut": r["statut"], "mesures": r["cl"], "total_mesures": r["tot"],
                   "sans_objet_avec_acte": r["obs_acte"], "sans_objet_filtre_large": r["obs_large"],
                   "sans_objet_ecartes": r["ecartes"], "sans_objet_tri": r["tri"], "regles_tri": dict(TRI),
                   "attente_mention_differe": r["differ_A"], "attente_differe_sans_date_prevue": r["differ_sans_date"],
                   "attente_sans_date_prevue": r["A_sans_date"], "sgg_31_12_2025": r["sgg"],
                   "senat_2024_2025_plus4": {"taux": r["plus4"][0], "taux_2023_2024_hors_differees": r["plus4"][1],
                                             "points": r["plus4"][2], "taux_2023_2024_serie": r["plus4"][3]}},
        "serie_senat": [{"session": s, "valeur": v, "document": pg, "citation": norm(c), "segment": seg,
                         "definition": SEGMENTS[seg]} for s, v, pg, c, seg in SERIE],
        "serie_senat_2019_2020_rapport_suivant": {"valeur": REVISION[1], "document": REVISION[2], "citation": norm(REVISION[3]),
                                                  "statut": "révision ou autre variante : non établi"},
        "tableaux": tableaux(r),
        "tableaux_en": tableaux_en(r),
        "affichage": A,
        "affichage_en": A_en,
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    # A11 : portée des catégories, sur la prose des deux pages et sur toutes les sorties (jetons, JSON, CSV, figures, fiches).
    textes = {"page FR": PAGE_FR.read_text(encoding="utf-8"), "page EN": PAGE_EN.read_text(encoding="utf-8"),
              "JSON": txt_json, "CSV": csvt, "fiches": json.dumps(fi, ensure_ascii=False)}
    textes.update(figs)
    garde_portee(textes)
    for nom, cle, ajout in (("page FR « n'appelaient aucune »", "page FR", " 144 lois n'appelaient aucune mesure."),
                            ("figure EN « called for none »", "appliquer-statut-en.svg", "<desc>144 called for none</desc>"),
                            ("JSON « appelaient au moins une »", "JSON", "254 lois qui appelaient au moins une mesure"),
                            ("fiches EN « called for at least one »", "fiches", "254 laws that called for at least one")):
        try:
            garde_portee(dict(textes, **{cle: textes[cle] + ajout}))
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith("A11 "):
                raise
            log("autotest : la mutation a mordu : %s -> %s" % (nom, str(e)[:90]))
    g.append("A11 : portee des categories : aucune formule de besoin initial (FR et EN) dans les deux pages et les sorties ; "
             "%d textes lus" % len(textes))
    if "--check" in sys.argv[1:]:
        for x in g:
            log("OK " + x)
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    same = (OUT_DATA.exists() and OUT_DATA.read_text(encoding="utf-8") == txt_json and OUT_CSV.exists()
            and OUT_CSV.read_text(encoding="utf-8-sig") == csvt
            and all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s for n, s in figs.items())
            and all((OUT_IMG / n.replace(".svg", ".png")).exists() for n in figs)
            and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fi)
    if same:
        log("Donnees et figures identiques : rien ecrit.")
        return 0
    OUT_DATA.write_text(txt_json, encoding="utf-8")
    OUT_STATIC.write_text(txt_json, encoding="utf-8")
    OUT_CSV.write_text(csvt, encoding="utf-8-sig", newline="\n")
    for n, s in figs.items():
        (OUT_IMG / n).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")),
                         output_width=600 if n.endswith("-m.svg") else 1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_appliquer.json, static/promesses_appliquer.{json,csv}, data/figures_appliquer.json, "
        "%d figures SVG + PNG (FR, EN, detail et telephone)" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
