#!/usr/bin/env python3
"""Volet « Délais » du dossier Promesses : la durée d'une formation de médecin, qui décide du nombre d'étudiants admis,
les admissions à leur année, et ce qui agit avant la fin du cursus.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 4 (v2, gelée au commit
dfd0ec9 ; arbitrage PRO-20261005-164029). Refonte (phase B, 12/10/2026) : arbitrage
06_PROMOTION/RECHERCHE_LYCEES_LECTURE_2026-10-09/REFONTE_PILOTE/DELAIS/ARBITRAGE_CE_DELAIS_PHASE_A.md.
  E1 — à règles constantes, durée du cursus standard de médecine générale depuis la première année : SOMME DE DURÉES
       LUES DANS LES TEXTES (aucune durée saisie), comparée à la durée du mandat lue dans l'art. 6 de la Constitution.
  E2 — étudiants admis en deuxième année du premier cycle (en troisième pour certaines passerelles), à leur année
       (DREES 1972-2020, ONDPS 2021-2025) ; aucun décalage, aucune projection ; ruptures de champ marquées.
  E3 — ce qui agit avant la fin du cursus : internat et autonomie supervisée (textes) ; médecins actifs à diplôme
       étranger (stock).
  Témoin daté (phase B) : loi du 23/12/2022 -> première phase de consolidation PRÉVUE le 2/11/2026 (instruction du
       21/05/2026) -> premiers diplômés du régime à quatre ans au plus tôt à l'automne 2027.

Sources (toutes dans scripts/sources_delais/) : réponses Légifrance archivées (nom = empreinte du fichier, garde G0) —
arrêté du 8 avril 2013 art. 1 ; C. éduc. L632-2 ; C. éduc. L631-1 en vigueur et ses versions de 2004, 2010, 2020 et
2023 ; CSP R6153-1-2 et L1434-4 ; Constitution art. 6 ; XML JORF de l'art. 37 de la loi n° 2022-1616 (stock DILA) ;
instruction DGOS/RH2/DGESIP/2026/44 du 21 mai 2026 (PDF du Bulletin officiel) ; DREES, Dossier n° 76, graphique 8 ;
ONDPS, bilan 2021-2025 (PDF) et transcription de sa page 7 ; extrait DREES RPPS 2012-2026 (lieu du diplôme).

Gardes (toutes ARRÊTENT, rien n'est écrit). Valeur :
  G0  chaque réponse Légifrance archivée a l'empreinte de son nom, l'état attendu (VIGUEUR / MODIFIE) et, pour une
      version ancienne, sa date de début attendue ; les lois modificatrices sont lues dans la réponse ;
  D1  durée du cursus = somme des durées LUES : « six semestres » (1er cycle) + « six semestres » (2e cycle) +
      « quatre années » (3e cycle de médecine générale) ; l'année de la rentrée d'application est LUE dans l'art. 37 ;
  D2  mandat : « cinq ans » (art. 6, français et traduction du Conseil constitutionnel) ;
  D3  « N fois la durée d'un mandat » n'est écrit que si durée du cursus / mandat est entier ;
  D4  série DREES contiguë 1972-2020 ; « divisées par plus de deux » exige 1972 / minimum > 2 ;
  D5  TÉMOIN DE PRODUCTEUR : sommes quinquennales de la série DREES contre les totaux imprimés par l'ONDPS (figure 2) ;
      écart nul exigé sur 2001-2005, 2006-2010, 2011-2015 ; l'écart 2016-2020 est calculé et PUBLIÉ, jamais corrigé ;
  D6  transcription ONDPS 2021-2025 : somme des admis == total imprimé ; total, admis 2025, capacités 2025 et ONP
      2021-2025 retrouvés dans le TEXTE du PDF ; empreinte du PDF égale à celle de la transcription ;
  D6 bis total 2016-2020 (lu sur l'image, relu le 12/10) : il doit redonner, aux arrondis imprimés, la hausse de « 27 % »
      et la moyenne annuelle de « 8 700 places » que le TEXTE du PDF imprime (portée : un intervalle, 43 250-43 540) ;
  D7  diplômés à l'étranger : part croissante 2012 -> 2026 ; c'est un stock, jamais présenté comme un flux.
Qualification (prose, toutes surfaces : pages FR et EN avec leur front matter — titre, chapô, description, FAQ et
JSON-LD —, libellés des figures, fiches « Réutiliser », carte de partage) :
  Q1  aucune formule qui fait des admis des entrants en études (« commencent / entrent en études de médecine »,
      « admissions en études de médecine », « start / enter medical studies »…) ;
  Q2  un nombre d'admis ne paraît que dans un paragraphe qui dit le niveau (deuxième année) ; des capacités, que dans
      une phrase qui dit « capacités » ; des places de 1972-2020, que dans une phrase qui dit « pourvues » ; le total
      2016-2020, que dans une phrase qui dit « numerus clausus » ; l'ONP, que dans une phrase qui dit « objectif ».
Temporalité :
  T1  cohorte : la première quatrième année (2 novembre 2026, LUE dans l'instruction) tombe l'année de la rentrée
      d'application + (durée de l'internat − 1) ;
  T2  toute phrase qui porte la durée du cursus dit « depuis la première année » et l'année de la rentrée d'application ;
  T3  le 2 novembre 2026 ne s'écrit que par jeton, dans une phrase qui le dit PRÉVU ; la date passée, le générateur
      s'arrête (condition de mort de T3 : la page réécrite au passé, une fois le début constaté) ;
  T4  « moins de quatre ans » (loi -> première année d'autonomie supervisée) et « près de cinq ans » (loi -> premiers
      diplômés au plus tôt) : inégalités STRICTES, sans quoi la phrase n'est pas écrite.
D1 bis : citations retrouvées mot pour mot ; D1 ter : chaque nombre d'une traduction figure dans l'original.
Autotest de mutation à chaque exécution, chaque mutation devant s'arrêter sur SA garde (liste dans autotest()).

Bilingue (06/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés, des figures -en au même dessin ;
l'art. 6 de la Constitution se cite en anglais dans la traduction du Conseil constitutionnel (vérifiée, garde D2) ; les
autres textes en français, suivis de notre traduction (clés *_tr). Nombres écrits par scripts/langue_generee.py.

Écrit : data/promesses_delais.json (+ static/), static/promesses_delais.csv, data/figures_delais.json,
static/img/delais-{cursus,admissions}{,-en}{,-m}.svg/.png. Rien n'est écrit à données identiques ; --check n'écrit rien.
"""
from __future__ import annotations

import copy
import csv
import datetime as dt
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

SRC = ROOT / "scripts" / "sources_delais"
PAGE_URL = "stephane-lalut.com/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/"
PAGE_URL_EN = "stephane-lalut.com/en/can-a-campaign-promise-produce-results-within-five-years/"
PAGE_FR = ROOT / "content" / "une-promesse-peut-elle-produire-ses-effets-en-cinq-ans" / "_index.md"
PAGE_EN = ROOT / "content" / "une-promesse-peut-elle-produire-ses-effets-en-cinq-ans" / "_index.en.md"
OG = ROOT / "scripts" / "og_promesses_delais.py"
OUT_DATA = ROOT / "data" / "promesses_delais.json"
OUT_STATIC = ROOT / "static" / "promesses_delais.json"
OUT_CSV = ROOT / "static" / "promesses_delais.csv"
OUT_FIGURES = ROOT / "data" / "figures_delais.json"
OUT_IMG = ROOT / "static" / "img"
# nom -> (empreinte du fichier archivé, état attendu, date de début attendue pour une version ancienne)
LEGI = {"arrete_2013": ("f89e9d3991814a43b91e67bcf31ffbd98b57ac38ce05d32ae5e5f74011ee913d", "VIGUEUR", None),
        "L632-2": ("804e64dca7a58af716c9d862f5a06d70b5603c7ab2690167ba5da4958e21df54", "VIGUEUR", None),
        "R6153-1-2": ("ef0a7e80801badd6e432f9b51c5e64ec546441fa8c14d102343930acf2a29dd1", "VIGUEUR", None),
        "art6": ("496783ff67a6d9cefb20a451d4d559d20101f0a63a39dad41c42448fe8c461ad", "VIGUEUR", None),
        "L1434-4": ("c6d2027182bb60c14c83a422983f721c608d63822e025fcc3f607dddfcc4b765", "VIGUEUR", None),
        "L631-1": ("3aa70ec21e91a1a8ebb315a554fbdfa60a0ac9fe9eb81d0f16e77ff6fda2e837", "VIGUEUR", "2025-06-29"),
        "L631-1_2023": ("38779f47d480726fb49e0b59b64a58fd1d84367cdcb0536e7b9f745c79bf9e7a", "MODIFIE", "2023-12-29"),
        "L631-1_2020": ("b177154e4cdb751b617db56d72a9c8bac67fa2fbee060e7ebf2e9392672ef866", "MODIFIE", "2020-09-01"),
        "L631-1_2010": ("0b531da0411f2111bc790d093cf6c71e0cc03326def043ca895e8e743fc557f3", "MODIFIE", "2010-10-01"),
        "L631-1_2004": ("f7de55f8c8fbd3da77e397a475edeaad6e713305ff8aff95c4ec115b700711e9", "MODIFIE", "2004-07-17")}
# Lois modificatrices attendues dans la réponse de chaque version de L631-1 (lues, jamais saisies dans la prose).
LOIS_631 = {"L631-1": "2025-580", "L631-1_2023": "2023-1268", "L631-1_2020": "2019-774"}
ART37 = "loi_2022-1616_art37_JORFARTI000046791824.xml"
INSTR = "instruction_DGOS_DGESIP_2026-44_SFHH2607068J.pdf"
INSTR_SHA = "8abb0ce9982b814bcf9aba6d3d72d3d3eac13205d01430250b2a292bbef7ad7b"
INSTR_URL = "https://bulletins-officiels.social.gouv.fr/sites/textes-officiels/files/2026-05/SFHH2607068J.pdf"
MOTS = {"un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
CIT_ART6_EN = "The President of the Republic shall be elected for a term of five years by direct universal suffrage."
# Notre traduction des textes français cités ; chaque nombre doit figurer dans l'original (garde D1 ter).
TR = {
    "cit_cycle1": "The general training diploma in medical sciences concludes the first cycle; it comprises six semesters of training",
    "cit_cycle2": "The advanced training diploma in medical sciences, defined in this order, concludes the second cycle; it "
                  "comprises six semesters of training",
    "cit_mg": "which, for the specialty of general practice, lasts four years",
    "cit_37": "The duration of the third cycle of medical studies for the specialty of general practice mentioned in 2° of I applies "
              "to students who begin this third cycle at the start of the 2023 academic year.",
    "cit_supervision": "The last year of the diploma of specialised studies in general practice is carried out as an internship, "
                       "under a regime of supervised autonomy",
    "cit_ambu": "in approved places of ambulatory practice where one or more general practitioners work, and as a priority in the "
                "areas mentioned in 1° of article L. 1434-4 of the Public Health Code",
    "cit_derog": "Exceptionally and by derogation from the first paragraph of this II, an internship may be carried out in a "
                 "hospital or non-hospital setting during the last year of the diploma of specialised studies in general practice.",
    "cit_zones": "The areas characterised by an insufficient supply of care or by difficulties in access to care",
    "cit_dj1": "The acts performed under this regime are performed by the docteur junior alone.",
    "cit_dj3": "Supervision is provided by a practitioner whom the docteur junior can call on at any time in the course of his "
               "practice, in accordance with the duty rosters.",
    "cit_dj2": "The docteur junior exercises his functions by delegation and under the responsibility of the practitioner he "
               "reports to.",
    "cit_dd76_objet": "this lever can only affect the demographic situation with a delay equivalent to the length of the "
                      "studies concerned",
    "cit_dd76": "it therefore takes five to ten years (respectively for midwives and doctors) for a policy based on this "
                "lever to begin to produce its effects",
    "cit_631_cap": "The intake capacities of the courses in the second and third years of the first cycle are determined "
                   "annually by the universities.",
    "cit_631_obj": "These multi-year objectives, which take into account the health needs of the territory as a priority, then "
                   "training capacities, are set by the university on the binding opinion of the territorial health councils "
                   "concerned and of the regional health agency or agencies concerned.",
    "cit_631_onp": "The multi-year objectives for admission to the first year of the second cycle are defined in the light of "
                   "national multi-year objectives on the number of professionals to be trained set by the State",
    "cit_631_hausse": "the latter may be called upon to implement measures to increase its intake capacities",
    "cit_631_2020": "These multi-year objectives, which take into account training capacities and the health needs of the "
                    "territory, are set by the university on the binding opinion of the regional health agency or agencies "
                    "concerned.",
    "cit_631_2023": "which take into account the health needs of the territory as a priority, then training capacities",
    "cit_631_2010": "The ministers responsible for higher education and health determine by regulation",
    "cit_631_2010b": "The number of students admitted to each course at the end of the first year of health studies",
    "cit_631_2004": "The number of students admitted, and the terms of their admission, at the end of the first year of the "
                    "first cycle, to continue medical, dental, midwifery or pharmaceutical studies are set each year",
    "cit_ondps_sat": "Intake capacities were almost saturated over the period.",
    "cit_ondps_2026": "For the 2026 academic year, the medical schools do not anticipate any increase in intake capacities "
                      "(0% increase).",
    "cit_ondps_9_11": "professionals in practice 9 to 11 years later depending on the length of the training",
    "cit_ondps_nc": "This is the sum over 5 years (2016-2020) of the numbers of the total numerus clausus, which includes the "
                    "alternative-entry routes.",
    "cit_ondps_2630": "preparatory work for the national conference that is to propose the national multi-year objectives",
    "cit_instr_interne": "The third-cycle student, working with the status of intern, carries out internships in hospital and in "
                         "ambulatory settings, in order to discover the overall care of the patient and to begin to develop "
                         "progressive autonomy, always under close supervision.",
    "cit_instr_amb": "mainly in ambulatory medicine",
    "cit_instr_diplome": "At the end of this fourth year, the training is validated by obtaining the DES in general practice.",
    "cit_instr_sup": "always under close supervision",
    "cit_631_moyens": "in particular as regards the financial and human resources made available, notably by the State",
    "cit_631_pass": "may be admitted to the second or third year of the first cycle",
    "cit_ondps_cae1": "from the 2nd or 3rd year of the 1st cycle",
    "cit_ondps_onp_pass": "the ONP includes those admitted through alternative-entry routes",
}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'")
    s = re.sub(r"\s+", " ", s)
    return re.sub(r" ([,.;:])", r"\1", s).strip()


def fr(n, dec=0) -> str:
    return lg.nombre(n, dec, "fr")


def en(n, dec=0) -> str:
    return lg.nombre(n, dec, "en")


def nombres(s: str) -> set:
    return {x.replace(",", ".") for x in re.findall(r"\d+(?:[.,]\d+)?", s)}


def jour(ms: int) -> dt.date:
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).date()


def date_fr(d: dt.date) -> str:
    return "%s %s %d" % ("1er" if d.day == 1 else str(d.day), MOIS[d.month - 1], d.year)


def date_en(d: dt.date) -> str:
    return "%d %s %d" % (d.day, MONTHS[d.month - 1], d.year)


def saison(d: dt.date, lang: str) -> str:
    md = (d.month, d.day)
    if (9, 23) <= md <= (12, 20):
        return ("l'automne %d" if lang == "fr" else "autumn %d") % d.year
    raise Arret("T4 : saison de la fin au plus tot non prevue (%s)" % d)


# ------------------------------------------------------------------ lecture
def lire() -> dict:
    t = {}
    for k, (h, etat, debut) in LEGI.items():
        f = SRC / ("legifrance_%s.json" % h)
        b = f.read_bytes()
        if hashlib.sha256(b).hexdigest() != h:
            raise Arret("G0 : %s : empreinte du fichier differente de son nom" % k)
        a = json.loads(b.decode("utf-8"))["article"]
        lois = [re.sub(r"\s+", " ", l.get("textTitle") or "") for l in (a.get("lienModifications") or [])]
        t[k] = {"id": a["id"], "texte": norm(a["texte"]), "sha": h, "etat": a.get("etat"),
                "debut": jour(a["dateDebut"]), "fin": jour(a["dateFin"]), "lois": lois}
        t[k]["etat_attendu"], t[k]["debut_attendu"] = etat, debut
    x = (SRC / ART37).read_text(encoding="utf-8")
    titre37 = norm(html.unescape(re.search(r"<TITRE_TXT[^>]*>([^<]*)<", x).group(1)))
    t["art37"] = {"id": "JORFARTI000046791824", "texte": norm(html.unescape(re.sub("<[^>]+>", " ", x))),
                  "sha": hashlib.sha256((SRC / ART37).read_bytes()).hexdigest(), "titre": titre37}
    import fitz
    ip = SRC / INSTR
    t["instr"] = {"id": "instruction n° DGOS/RH2/DGESIP/2026/44 du 21 mai 2026 (NOR SFHH2607068J), " + INSTR_URL,
                  "texte": norm(" ".join(p.get_text() for p in fitz.open(ip))),
                  "sha": hashlib.sha256(ip.read_bytes()).hexdigest()}
    import openpyxl
    wb = openpyxl.load_workbook(SRC / "drees_DD76_donnees_2021.xlsx", data_only=True)
    serie, an = {}, 1972
    for r in wb["Graphique 8"].iter_rows(values_only=True):
        v = [c for c in r if c is not None]
        if not v or not isinstance(v[-1], (int, float)):
            continue
        if len(v) == 2:
            an = int(str(v[0]).rstrip("*"))
        serie[an] = int(v[-1])
        an += 1
    ondps = json.loads((SRC / "ondps_admis_transcription.json").read_text(encoding="utf-8"))
    pdf = SRC / ondps["fichier"]
    texte_pdf = norm(" ".join(p.get_text() for p in fitz.open(pdf)))
    t["ondps"] = {"id": "ONDPS, note de bilan des ONP 2021-2025, 19/12/2025 (" + ondps["fichier"] + ")", "texte": texte_pdf,
                  "sha": hashlib.sha256(pdf.read_bytes()).hexdigest()}
    # C6 (07/10/2026) : synthèse du Dossier n° 76 de la DREES, citée comme accord (le PDF est archivé dans sondes\delais).
    ext = (SRC / "drees_DD76_2021_page5_extrait.txt").read_text(encoding="utf-8")
    t["dd76_pdf"] = {"id": "drees_DD76_2021.pdf, page 5 (extrait archivé)", "texte": norm(re.sub(r"\s+", " ", ext)),
                     "sha": re.search(r"SHA-256 du PDF d'origine : ([0-9a-f]{64})", ext).group(1)}
    rpps = list(csv.reader(l for l in (SRC / "drees_rpps_lieu_diplome_extrait.csv").read_text(encoding="utf-8").splitlines()
                           if not l.startswith("#")))
    pages = {"fr": PAGE_FR.read_text(encoding="utf-8"), "en": PAGE_EN.read_text(encoding="utf-8"),
             "og": OG.read_text(encoding="utf-8")}
    return {"textes": t, "dd76": serie, "ondps": ondps, "pdf_sha": t["ondps"]["sha"], "texte_pdf": texte_pdf,
            "rpps": rpps, "pages": pages, "aujourdhui": dt.date.today(), "libelles": copy.deepcopy(T)}


# ------------------------------------------------------------------ calcul et gardes de valeur et de temps
def mot_avant(texte: str, unite: str, apres: str) -> int:
    m = re.search(r"\b(%s) %s" % ("|".join(MOTS), unite), texte[texte.find(apres):] if apres in texte else "")
    if not m:
        raise Arret("D1 : « %s » introuvable après « %s »" % (unite, apres[:40]))
    return MOTS[m.group(1)]


def date_lue(texte: str, motif: str, quoi: str) -> dt.date:
    m = re.search(motif, texte)
    if not m or m.group(2) not in MOIS:
        raise Arret("%s introuvable" % quoi)
    return dt.date(int(m.group(3)), MOIS.index(m.group(2)) + 1, int(m.group(1)))


def calculer(S: dict) -> tuple[dict, list[str]]:
    g, T = [], S["textes"]
    for k, (h, etat, debut) in LEGI.items():
        if T[k]["etat"] != etat:
            raise Arret("G0 : %s : etat %s, attendu %s" % (k, T[k]["etat"], etat))
        if debut and str(T[k]["debut"]) != debut:
            raise Arret("G0 : %s : version du %s, attendue du %s" % (k, T[k]["debut"], debut))
    lois = {}
    for k, num in LOIS_631.items():
        m = [re.search(r"LOI n° ?(%s) du (\d+) (\w+) (\d{4})" % re.escape(num), l.replace("n°", "n° ")) for l in T[k]["lois"]]
        m = [x for x in m if x]
        if not m:
            raise Arret("G0 : %s : loi modificatrice n° %s absente de la reponse" % (k, num))
        lois[k] = (num, dt.date(int(m[0].group(4)), MOIS.index(m[0].group(3)) + 1, int(m[0].group(2))))
    g.append("G0 : %d reponses Legifrance (empreinte, etat, version) ; lois modificatrices de L631-1 lues : %s"
             % (len(LEGI), ", ".join(v[0] for v in lois.values())))
    a13 = T["arrete_2013"]["texte"]
    s1 = mot_avant(a13, "semestres", "sanctionne le premier cycle")
    s2 = mot_avant(a13, "semestres", "sanctionne le deuxième cycle")
    mg = mot_avant(T["L632-2"]["texte"], "années", "pour la spécialité de médecine générale")
    m37 = re.search(r"s'applique aux étudiants qui commencent ce troisième cycle à la rentrée de l'année universitaire (\d{4})\.",
                    T["art37"]["texte"])
    if not m37:
        raise Arret("D1 : application aux entrants d'une rentree introuvable dans l'art. 37")
    an_reforme = int(m37.group(1))
    duree = s1 / 2 + s2 / 2 + mg
    duree_adm = (s1 - 2) / 2 + s2 / 2 + mg   # admission en deuxième année : une année (deux semestres) déjà faite
    if "deuxième et troisième années de premier cycle" not in T["L631-1"]["texte"]:
        raise Arret("D1 : niveau des capacites d'accueil (deuxieme annee) introuvable dans L631-1")
    g.append("D1 : cursus MG = %d + %d semestres + %d annees = %g ans depuis la 1re annee, %g depuis l'admission en 2e annee "
             "(entrants en 3e cycle a partir de la rentree %d)" % (s1, s2, mg, duree, duree_adm, an_reforme))
    if "supervisée" not in T["L632-2"]["texte"] or "autonomie supervisée" not in T["R6153-1-2"]["texte"]:
        raise Arret("D1 : autonomie supervisee introuvable")
    a6 = T["art6"]["texte"]
    m6 = re.search(r"élu pour (\w+) ans", a6)
    if not m6:
        raise Arret("D2 : duree du mandat introuvable dans l'art. 6")
    mandat = MOTS[m6.group(1)]
    try:
        cen.citer("6", CIT_ART6_EN)
    except ValueError as e:
        raise Arret("D2 : %s" % e)
    if "five years" not in CIT_ART6_EN or mandat != 5:
        raise Arret("D2 : duree du mandat differente entre le texte francais et la traduction")
    g.append("D2 : mandat %d ans (FR Legifrance, EN Conseil constitutionnel)" % mandat)
    # Comparaison d'ÉCHELLE seulement (contre-expertise PRO-20261006-130420, P1) : « soit N fois la durée d'un mandat ».
    rapport = duree / mandat
    if rapport != int(rapport) or int(rapport) > 16:
        raise Arret("D3 : cursus %g ans / mandat %d ans = %g : la phrase « N fois la durée d'un mandat » serait fausse" % (duree, mandat, rapport))
    nmax = int(rapport)
    if duree_adm != int(duree_adm):
        raise Arret("D3 : duree depuis l'admission non entiere (%g)" % duree_adm)
    g.append("D3 : cursus = %d fois la duree d'un mandat (comparaison d'echelle)" % nmax)
    # ---- témoin daté (T1, T3, T4)
    loi = date_lue(T["art37"]["titre"], r"LOI n° 2022-1616 du (\d+) (\w+) (\d{4}) de financement de la sécurité sociale pour 2023",
                   "T1 : date et nature de la loi n° 2022-1616")
    debut = date_lue(T["instr"]["texte"], r"concernera dès le (\d+) (\w+) (\d{4}) pour la première fois les étudiants inscrits "
                     r"dans le diplôme d'études spécialisées \(DES\) de médecine générale d'une durée de quatre ans",
                     "T1 : date de la premiere phase de consolidation dans l'instruction")
    if T["instr"]["sha"] != INSTR_SHA:
        raise Arret("T1 : l'instruction n'est pas celle qui a ete lue (empreinte)")
    if an_reforme + (mg - 1) != debut.year:
        raise Arret("T1 : la premiere quatrieme annee (%d) ne tombe pas %d + %d ans apres la rentree d'application"
                    % (debut.year, an_reforme, mg - 1))
    if S["aujourdhui"] >= debut:
        raise Arret("T3 : le %s est passe : la date ecoulee ne prouve rien ; la mise a jour exige une preuve du demarrage "
                    "effectif de la phase de consolidation (source officielle qui le constate), puis la page reecrite au "
                    "passe (jeton debut_conso) et T3 retire" % debut)
    fin = debut.replace(year=debut.year + 1) - dt.timedelta(days=1)
    quatre = loi.replace(year=loi.year + 4)
    limite = loi.replace(year=loi.year + mandat)
    if not debut < quatre:
        raise Arret("T4 : « moins de quatre ans » faux : loi %s, premiere phase de consolidation %s" % (loi, debut))
    if not (loi.replace(year=loi.year + 4) < fin < limite):
        raise Arret("T4 : « près de cinq ans » faux (inegalite stricte) : loi %s, fin au plus tot %s, limite %s" % (loi, fin, limite))
    g.append("T1-T4 : loi %s -> premiere phase de consolidation prevue %s (rentree %d + %d) -> fin au plus tot %s, < %s"
             % (loi, debut, an_reforme, mg - 1, fin, limite))
    d = S["dd76"]
    if sorted(d) != list(range(1972, 2021)):
        raise Arret("D4 : serie DREES non contigue 1972-2020")
    amin = min(d, key=d.get)
    if not d[1972] / d[amin] > 2:
        raise Arret("D4 : « divisees par plus de deux » faux")
    g.append("D4 : minimum %d (%d places), 1972 / minimum = %.2f" % (amin, d[amin], d[1972] / d[amin]))
    q = S["ondps"]["quinquennaux_figure2"]
    ecarts = {}
    for per, v in q.items():
        a0, a1 = map(int, per.split("-"))
        ecarts[per] = sum(d[a] for a in range(a0, a1 + 1)) - v
    for per in ("2001-2005", "2006-2010", "2011-2015"):
        if ecarts[per] != 0:
            raise Arret("D5 : somme DREES %s != total ONDPS (ecart %d)" % (per, ecarts[per]))
    g.append("D5 : DREES = ONDPS sur 2001-2015 ; ecart publie 2016-2020 : %+d" % ecarts["2016-2020"])
    o = S["ondps"]
    if S["pdf_sha"] != o["sha256_pdf"]:
        raise Arret("D6 : le PDF n'est pas celui de la transcription")
    if sum(o["admis_medecine"].values()) != o["total_admis_2021_2025"]:
        raise Arret("D6 : somme des admis transcrits != total imprime")
    tp = S["texte_pdf"]
    for v in (o["total_admis_2021_2025"], o["admis_medecine"]["2025"], o["capacites_2025"], o["onp_2021_2025"]):
        if fr(v).replace("\u00a0", " ") not in tp:
            raise Arret("D6 : %d absent du texte du PDF" % v)
    hausse = round(100 * (o["total_admis_2021_2025"] / q["2016-2020"] - 1))
    m27 = re.search(r"soit (\d+) % par rapport à la période quinquennale précédente", tp)
    m87 = re.search(r"(\d+ \d{3}) places sur la période 2016-2020", tp)
    if not m27 or not m87:
        raise Arret("D6 bis : hausse quinquennale ou moyenne 2016-2020 introuvable dans le texte du PDF")
    if hausse != int(m27.group(1)) or round(q["2016-2020"] / 5, -2) != int(m87.group(1).replace(" ", "")):
        raise Arret("D6 bis : total 2016-2020 transcrit (%d) incompatible avec le texte du PDF (%s %%, %s places par an)"
                    % (q["2016-2020"], m27.group(1), m87.group(1)))
    somme_drees = q["2016-2020"] + ecarts["2016-2020"]
    if round(100 * (o["total_admis_2021_2025"] / somme_drees - 1)) == hausse:
        raise Arret("D6 bis : la somme DREES 2016-2020 redonne aussi %d %% : « seul le total ONDPS redonne » serait faux" % hausse)
    g.append("D6 : admis 2021-2025 (%d), capacites 2025, ONP (%d) controles par la somme et par le texte du PDF ; D6 bis : "
             "total 2016-2020 (%d) compatible avec « %s %% » et « %s places »" % (o["total_admis_2021_2025"], o["onp_2021_2025"],
                                                                                q["2016-2020"], m27.group(1), m87.group(1)))
    h = S["rpps"][0]
    rows = {(r[1], r[2]): r for r in S["rpps"][1:]}
    i12, i26 = h.index("effectif_2012"), h.index("effectif_2026")
    tot, etr = rows[("00-Ensemble", "0-Ensemble")], rows[("99-Etranger", "0-Ensemble")]
    p12, p26 = 100 * int(etr[i12]) / int(tot[i12]), 100 * int(etr[i26]) / int(tot[i26])
    if not p26 > p12:
        raise Arret("D7 : part des diplomes a l'etranger non croissante")
    g.append("D7 : diplome a l'etranger %.1f %% (2012) -> %.1f %% (2026), stock" % (p12, p26))
    r = {"s1": s1, "s2": s2, "mg": mg, "duree": duree, "duree_adm": duree_adm, "mandat": mandat, "nmax": nmax, "dd76": d,
         "amin": amin, "ecarts": ecarts, "ondps": o, "etr12": int(etr[i12]), "tot12": int(tot[i12]), "etr26": int(etr[i26]),
         "tot26": int(tot[i26]), "p12": p12, "p26": p26, "an_reforme": an_reforme, "loi": loi, "debut": debut, "fin": fin,
         "lois631": lois, "versions631": {k: (T[k]["debut"], T[k]["fin"]) for k in LEGI if k.startswith("L631-1")}}
    return r, g


CITATIONS = {  # clé -> (texte source, citation exacte). Vérifiées mot pour mot (garde D1 bis) ; la page les affiche par jeton.
    "cit_cycle1": ("arrete_2013", "Le diplôme de formation générale en sciences médicales sanctionne le premier cycle ; il comprend six semestres de formation"),
    "cit_cycle2": ("arrete_2013", "Le diplôme de formation approfondie en sciences médicales, défini au présent arrêté, sanctionne le deuxième cycle ; il comprend six semestres de formation"),
    "cit_mg": ("L632-2", "qui, pour la spécialité de médecine générale, est d'une durée de quatre années"),
    "cit_37": ("art37", "La durée du troisième cycle des études de médecine pour la spécialité de médecine générale mentionnée au 2° du I s'applique aux étudiants qui commencent ce troisième cycle à la rentrée de l'année universitaire 2023."),
    "cit_art6a": ("art6", "Le Président de la République est élu pour cinq ans au suffrage universel direct."),
    "cit_supervision": ("L632-2", "La dernière année du diplôme d'études spécialisées de médecine générale est effectuée en stage, sous un régime d'autonomie supervisée"),
    "cit_ambu": ("L632-2", "dans des lieux agréés en pratique ambulatoire dans lesquels exercent un ou plusieurs médecins généralistes et en priorité dans les zones mentionnées au 1° de l'article L. 1434-4 du code de la santé publique"),
    "cit_derog": ("L632-2", "A titre exceptionnel et par dérogation au premier alinéa du présent II, un stage peut être réalisé en milieu hospitalier ou extrahospitalier au cours de la dernière année du diplôme d'études spécialisées de médecine générale."),
    "cit_zones": ("L1434-4", "Les zones caractérisées par une offre de soins insuffisante ou par des difficultés dans l'accès aux soins"),
    "cit_dj1": ("R6153-1-2", "Les actes réalisés sous ce régime le sont par le docteur junior seul."),
    "cit_dj3": ("R6153-1-2", "La supervision est assurée par un praticien auquel le docteur junior peut avoir recours à tout moment de son exercice, conformément aux tableaux de service."),
    "cit_dj2": ("R6153-1-2", "Le docteur junior exerce ses fonctions par délégation et sous la responsabilité du praticien dont il relève."),
    "cit_dd76_objet": ("dd76_pdf", "ce levier ne peut affecter la situation démographique qu’avec un délai équivalent à la durée des études concernées"),
    "cit_dd76": ("dd76_pdf", "il faut ainsi compter de cinq à dix ans (respectivement pour le cas des sages-femmes et des médecins) pour qu’une politique axée sur ce levier ne commence à produire ses effets"),
    "cit_631_cap": ("L631-1", "Les capacités d'accueil des formations en deuxième et troisième années de premier cycle sont déterminées annuellement par les universités."),
    "cit_631_obj": ("L631-1", "Ces objectifs pluriannuels, qui tiennent compte des besoins de santé du territoire en priorité, puis des capacités de formation, sont arrêtés par l'université sur avis conforme des conseils territoriaux de santé concernés et de l'agence régionale de santé ou des agences régionales de santé concernées."),
    "cit_631_onp": ("L631-1", "Les objectifs pluriannuels d'admission en première année du deuxième cycle sont définis au regard d'objectifs nationaux pluriannuels relatifs au nombre de professionnels à former établis par l'Etat"),
    "cit_631_hausse": ("L631-1", "cette dernière peut être appelée à mettre en œuvre des mesures visant à accroître ses capacités d'accueil"),
    "cit_631_2020": ("L631-1_2020", "Ces objectifs pluriannuels, qui tiennent compte des capacités de formation et des besoins de santé du territoire, sont arrêtés par l'université sur avis conforme de l'agence régionale de santé ou des agences régionales de santé concernées."),
    "cit_631_2023": ("L631-1_2023", "qui tiennent compte des besoins de santé du territoire en priorité, puis des capacités de formation"),
    "cit_631_2010": ("L631-1_2010", "Les ministres chargés de l'enseignement supérieur et de la santé déterminent par voie réglementaire"),
    "cit_631_2010b": ("L631-1_2010", "Le nombre des étudiants admis dans chacune des filières à l'issue de la première année des études de santé"),
    "cit_631_2004": ("L631-1_2004", "Le nombre des étudiants admis ainsi que les modalités de leur admission, à la fin de la première année du premier cycle, à poursuivre des études médicales, odontologiques, de sage-femme ou pharmaceutiques sont fixés, chaque année"),
    "cit_ondps_sat": ("ondps", "Les capacités d'accueil ont été quasiment saturées sur la période."),
    "cit_ondps_2026": ("ondps", "Pour la rentrée 2026, les UFR n'anticipent pas d'augmentation de capacités d'accueil (0 % d'augmentation)."),
    "cit_ondps_9_11": ("ondps", "des professionnels en exercice 9 à 11 ans plus tard selon la durée de la formation"),
    "cit_ondps_nc": ("ondps", "Il s'agit de la somme sur 5 ans (2016-2020) des effectifs du numerus clausus total, qui comprend les passerelles."),
    "cit_ondps_2630": ("ondps", "travaux préparatoires à la conférence nationale qui devra proposer les objectifs nationaux pluriannuels"),
    "cit_instr_interne": ("instr", "L'étudiant de troisième cycle, exerçant sous le statut d'interne, effectue des stages qui se déroulent en milieu hospitalier et en milieu ambulatoire, afin de découvrir la prise en charge globale du patient et de commencer à développer une autonomie progressive, toujours sous supervision étroite."),
    "cit_instr_amb": ("instr", "principalement en médecine ambulatoire"),
    "cit_instr_diplome": ("instr", "À l'issue de cette quatrième année, la formation est validée par l'obtention du DES de médecine générale."),
    # passe B2 (12/10/2026) : réponses aux questions du panel « après » et niveau d'admission des admis de l'ONDPS
    "cit_instr_sup": ("instr", "toujours sous supervision étroite"),
    "cit_631_moyens": ("L631-1", "en particulier en matière de moyens financiers et humains dégagés notamment par l'Etat"),
    "cit_631_pass": ("L631-1", "peuvent être admis en deuxième ou en troisième année du premier cycle"),
    "cit_ondps_cae1": ("ondps", "à partir de la 2ème ou 3ème année du 1er cycle"),
    "cit_ondps_onp_pass": ("ondps", "l'ONP comprend les admis de passerelles"),
}


def citations(T: dict) -> dict:
    out = {}
    for k, (src, c) in CITATIONS.items():
        if norm(c) not in T[src]["texte"]:
            raise Arret("D1 bis : citation %s absente du texte %s : %r" % (k, src, c[:60]))
        out[k] = c
    for k, tr in TR.items():
        if k not in out:
            raise Arret("D1 ter : traduction %s sans original" % k)
        if not nombres(tr) <= nombres(out[k]):
            raise Arret("D1 ter : %s : nombres de la traduction absents de l'original : %s" % (k, nombres(tr) - nombres(out[k])))
    return out


def loi_txt(num_date, lang):
    num, d = num_date
    return ("loi n° %s du %s" % (num, date_fr(d))) if lang == "fr" else ("Law no. %s of %s" % (num, date_en(d)))


def affichage(r: dict, lang: str = "fr") -> dict:
    o = r["ondps"]
    q = o["quinquennaux_figure2"]
    n = fr if lang == "fr" else en
    D = date_fr if lang == "fr" else date_en
    nfois = lg.lettres(r["nmax"], lang) + " fois" if lang == "fr" else \
        {1: "once", 2: "twice", 3: "three times"}.get(r["nmax"], lg.lettres(r["nmax"], "en") + " times")
    v = r["versions631"]
    return {
        "duree": lg.lettres(int(r["duree"]), lang), "duree_chiffre": "%d" % r["duree"],
        "duree_adm": lg.lettres(int(r["duree_adm"]), lang), "mandat": lg.lettres(r["mandat"], lang),
        "nmax": lg.lettres(r["nmax"], lang), "nfois": nfois,
        "ecart_pct": n(100 * abs(r["ecarts"]["2016-2020"]) / q["2016-2020"], 1),
        "cycle1": lg.lettres(r["s1"], lang), "cycle2": lg.lettres(r["s2"], lang), "mg": lg.lettres(r["mg"], lang),
        "an_reforme": str(r["an_reforme"]), "loi_date": D(r["loi"]), "debut_conso": D(r["debut"]),
        "fin_min": saison(r["fin"], lang),
        "moins_quatre": "moins de quatre ans" if lang == "fr" else "less than four years",
        "pres_cinq": "près de cinq ans" if lang == "fr" else "almost five years",
        "d631_2020": D(v["L631-1_2020"][0]), "d631_2023": D(v["L631-1_2023"][0]), "d631_2025": D(v["L631-1"][0]),
        "loi631_2020": loi_txt(r["lois631"]["L631-1_2020"], lang), "loi631_2023": loi_txt(r["lois631"]["L631-1_2023"], lang),
        "loi631_2025": loi_txt(r["lois631"]["L631-1"], lang),
        "an_min": str(r["amin"]), "places_min": n(r["dd76"][r["amin"]]), "places_1972": n(r["dd76"][1972]),
        "places_2020": n(r["dd76"][2020]), "rapport_baisse": n(r["dd76"][1972] / r["dd76"][r["amin"]], 1),
        "admis_2025": n(o["admis_medecine"]["2025"]), "capacites_2025": n(o["capacites_2025"]),
        "admis_2021_2025": n(o["total_admis_2021_2025"]), "onp": n(o["onp_2021_2025"]),
        "admis_2016_2020": n(q["2016-2020"]),
        "hausse_quinquennale": n(100 * (o["total_admis_2021_2025"] / q["2016-2020"] - 1), 0),
        "hausse_drees": n(100 * (o["total_admis_2021_2025"] / (q["2016-2020"] + r["ecarts"]["2016-2020"]) - 1), 0),
        "ecart_2016_2020": n(abs(r["ecarts"]["2016-2020"])),
        "etr_p12": n(r["p12"], 1), "etr_p26": n(r["p26"], 1), "etr_26": n(r["etr26"]), "tot_26": n(r["tot26"]),
        "releve_le": ("12/10/2026 (textes lus sur Légifrance les 05, 06, 11 et 12/10/2026 ; instruction du 21 mai 2026 ; DREES, "
                      "2 juillet 2026 ; ONDPS, 19 décembre 2025)") if lang == "fr" else
                     ("12 October 2026 (texts read on Légifrance on 5, 6, 11 and 12 October 2026; instruction of 21 May 2026; "
                      "DREES, 2 July 2026; ONDPS, 19 December 2025)"),
    }


# ------------------------------------------------------------------ gardes de prose (qualification Q, temporalité T)
JETON = re.compile(r"\{\{<\s*del-val\s+\"([a-z0-9_]+)\"\s*>\}\}|\{del\.([a-z0-9_]+)\}")
Q1 = [re.compile(x, re.I) for x in (
    r"\b(?:commenc|entr|début|début)\w*\s+(?:en|des|les|dans les)\s+études\s+de\s+médecine",
    r"\badmissions?\s+en\s+études\s+de\s+médecine", r"\badmis\s+en\s+études", r"\bentrées?\s+en\s+études\s+de\s+médecine",
    r"\bplaces\s+en\s+études\s+de\s+médecine", r"\badmis\s+en\s+première\s+année(?!\s+du\s+deuxième\s+cycle)",
    r"\b(?:start|enter|begin|began|entering|starting)\w*\s+(?:the\s+)?medical\s+(?:studies|school)",
    r"\badmissions?\s+to\s+medical\s+(?:studies|school)", r"\bplaces\s+in\s+(?:French\s+)?medical\s+studies",
    r"\badmitted\s+to\s+(?:the\s+)?first\s+year(?!\s+of\s+the\s+second\s+cycle)")]
Q2 = {  # jeton -> (portée, motif exigé)
    "admis_2025": ("paragraphe", r"deuxième année|second year"), "admis_2021_2025": ("paragraphe", r"deuxième année|second year"),
    "capacites_2025": ("phrase", r"capacit"), "onp": ("phrase", r"objectif|target"),
    "places_1972": ("phrase", r"pourvu|filled"), "places_min": ("phrase", r"pourvu|filled"),
    "rapport_baisse": ("phrase", r"pourvu|filled"), "admis_2016_2020": ("phrase", r"numerus clausus"),
}
T_PREVU = re.compile(r"\bprévu|\bdoit commencer|\bdevait commencer|\bscheduled|\bplanned|\bis (?:due|set) to", re.I)
DATE_CLAIRE = re.compile(r"\b2\s*(?:&nbsp;|\u00a0)?\s*(?:novembre|November)\s*(?:&nbsp;|\u00a0)?\s*2026")


def phrases(texte: str):
    """(paragraphe, phrase) : un paragraphe = une ligne (Markdown à une ligne par paragraphe, front matter YAML)."""
    for par in texte.splitlines():
        if not par.strip():
            continue
        for ph in re.split(r"(?<=[.!?])\s+(?=[^a-z0-9])", par):
            yield par, ph


def prose(textes: dict, an_reforme: int) -> int:
    n = 0
    for nom, texte in textes.items():
        for par, ph in phrases(texte):
            n += 1
            for rx in Q1:
                m = rx.search(ph)
                if m:
                    raise Arret("Q1 %s : niveau d'admission faux ou ambigu : « %s »" % (nom, m.group(0)))
            if DATE_CLAIRE.search(ph):
                raise Arret("T3 %s : date de la premiere phase de consolidation ecrite en clair (jeton debut_conso exige)" % nom)
            jetons = {a or b for a, b in JETON.findall(ph)}
            for j in jetons & set(Q2):
                portee, motif = Q2[j]
                # le motif se cherche HORS jetons : « capacites_2025 » contient « capacit » (témoin vu échouer le 12/10)
                if not re.search(motif, JETON.sub(" ", par if portee == "paragraphe" else ph), re.I):
                    raise Arret("Q2 %s : jeton %s sans « %s » dans la %s : %s" % (nom, j, motif, portee, ph[:90]))
            if "duree" in jetons and not ((str(an_reforme) in JETON.sub(" ", ph) or "an_reforme" in jetons)
                                          and re.search(r"première année|first year", JETON.sub(" ", ph), re.I)):
                raise Arret("T2 %s : duree du cursus sans « premiere annee » ou sans la rentree %d : %s" % (nom, an_reforme, ph[:90]))
            if "debut_conso" in jetons and not T_PREVU.search(ph):
                raise Arret("T3 %s : la date du jeton debut_conso n'est pas dite prevue : %s" % (nom, ph[:90]))
            if "fin_min" in jetons and not re.search(r"au plus tôt|pas avant|at the earliest|not before", ph, re.I):
                raise Arret("T4 %s : fin du premier internat a quatre ans sans « au plus tot » : %s" % (nom, ph[:90]))
    return n


def textes_prose(S: dict) -> dict:
    """Surfaces que les gardes de prose relisent : pages FR et EN (front matter compris), carte, libellés des figures."""
    t = {"page fr": S["pages"]["fr"], "page en": S["pages"]["en"], "carte": S["pages"]["og"]}
    for lang, L in S["libelles"].items():
        t["libelles figures %s" % lang] = "\n".join(v if isinstance(v, str) else " / ".join(v) for v in L.values())
    return t


def verifier(S: dict):
    r, g = calculer(S)
    n = prose(textes_prose(S), r["an_reforme"])
    # le nombre de phrases relues n'entre pas dans le jeu publié : une retouche de prose ne doit pas réécrire les données
    log("prose : %d phrases relues (pages FR et EN avec front matter, carte, libelles des figures)" % n)
    g.append("Q1-Q2, T2-T4 : pages FR et EN avec front matter, carte, libelles des figures")
    return r, g


# ------------------------------------------------------------------ figures
W = 720
BLEU, BLEU_CLAIR, GRIS, GRIS_CLAIR = "#184f95", "#7fa3cf", "#8a8f98", "#c9cdd3"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCES_M = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
              "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
LANG = "fr"
WM, FS_MIN = 300, 13.5


def nb(n) -> str:
    return en(n) if LANG == "en" else fr(n)


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


T = {
    "fr": {"src1": "Arrêté du 8 avril 2013, art. 1 ; code de l'éducation, art. L632-2 ; loi n° 2022-1616, art. 37 ; Constitution, art. 6 (Légifrance)",
           "note1": "Durées minimales, sans redoublement, interruption ni passerelle, pour les étudiants entrés en internat à partir de la rentrée 2023. Comparaison d'échelle seulement : ni l'effet d'une politique, ni la date de ses premiers effets ; les internes soignent avant la fin du cursus.",
           "src2": "DREES, Dossier n° 76 (2021), graphique 8, source ONDPS (1972-2020) ; ONDPS, bilan 2021-2025 (admis)",
           "note2": "Admissions en deuxième année du premier cycle, ou directement en troisième pour certaines passerelles. Jusqu'en 2020, places pourvues du numerus clausus, élargi aux passerelles et aux droits au remords à partir de 2010-2011 ; depuis 2021, admis. Chaque barre à l'année publiée par la source, sans décalage.",
           "t1": "Former un médecin généraliste, et la durée d'un mandat présidentiel",
           "s1": "en années, durées minimales écrites dans les textes en vigueur",
           "d1": "Deux barres de même échelle. En haut, le cursus de médecine générale : {a} ans de premier cycle, {b} ans de "
                 "deuxième cycle, puis {c} ans d'internat de médecine générale dont la dernière en autonomie supervisée, soit {d} "
                 "ans depuis la première année et {f} depuis l'admission en deuxième année. En bas, un mandat présidentiel de {e} "
                 "ans. Comparaison d'échelle seulement.",
           "mg": "Médecine générale", "cycles": ["1er cycle", "2e cycle", "Internat de médecine générale"],
           "court": ["1er", "2e", "Internat"],
           "auto": "dernière année : autonomie supervisée", "mandat": "Mandat présidentiel", "ans": "{} ans",
           "depuis_adm": "{} ans depuis l'admission en 2e année", "internat": "Internat de médecine générale : {} ans",
           "cycle1_m": "1er cycle : {} ans", "cycle2_m": "2e cycle : {} ans", "internat_m": "Internat de médecine générale",
           "dont": "{} ans, dont la dernière en autonomie supervisée", "total": "Total : {} ans depuis la 1re année",
           "t2": "Étudiants admis dans le cursus de médecine, 1972-2025",
           "s2": "admissions en deuxième année du premier cycle, ou directement en troisième année par passerelle",
           "s2m": "admissions en deuxième année du premier cycle, ou directement en troisième année par passerelle",
           "d2": "Barres annuelles des étudiants admis en deuxième année du premier cycle : {places_1972} places pourvues en "
                 "1972, minimum de {places_min} en {an_min}, {places_2020} en 2020 ; puis de {min_admis} à {admis_2025} admis par "
                 "an de 2021 à 2025.",
           "r1": "2010-2011 : passerelles incluses", "r2": "2021 : fin du numerus clausus", "annot": "%s : %s"},
    "en": {"src1": "Order of 8 April 2013, art. 1; Education Code, art. L632-2; Law no. 2022-1616, art. 37; Constitution, art. 6",
           "note1": "Minimum durations, without repeating a year, interruption or alternative-entry route, for students who entered residency from the 2023 academic year. Comparison of scale only: neither the effect of a policy nor the date of its first effects; residents provide care before the end.",
           "src2": "DREES, Dossier no. 76 (2021), chart 8, source ONDPS (1972-2020); ONDPS, 2021-2025 report (admissions)",
           "note2": "Admissions to the second year of the first cycle, or directly to the third for some alternative-entry routes. Until 2020, places filled under the numerus clausus, widened to alternative-entry routes and reorientation entries from 2010-2011; since 2021, students admitted. Each bar at the year published by the source, no shift.",
           "t1": "Training a general practitioner in France, and the length of a presidential term",
           "s1": "in years, minimum durations written in the texts in force",
           "d1": "Two bars on the same scale. Above, the general practice curriculum: {a} years of first cycle, {b} years of second "
                 "cycle, then {c} years of general practice residency, the last under supervised autonomy: {d} years from the "
                 "first year and {f} from admission to the second year. Below, a presidential term of {e} years. Comparison of "
                 "scale only.",
           "mg": "General practice", "cycles": ["1st cycle", "2nd cycle", "General practice residency"],
           "court": ["1st", "2nd", "Residency"],
           "auto": "last year: supervised autonomy", "mandat": "Presidential term", "ans": "{} years",
           "depuis_adm": "{} years from admission to the 2nd year", "internat": "General practice residency: {} years",
           "cycle1_m": "1st cycle: {} years", "cycle2_m": "2nd cycle: {} years", "internat_m": "General practice residency",
           "dont": "{} years, the last under supervised autonomy", "total": "Total: {} years from the 1st year",
           "t2": "Students admitted into the medical curriculum in France, 1972-2025",
           "s2": "admissions to the second year of the first cycle, or directly to the third year through an alternative-entry route",
           "s2m": "admissions to the second year of the first cycle, or directly to the third year through an alternative-entry route",
           "d2": "Annual bars of students admitted to the second year of the first cycle: {places_1972} places filled in 1972, a "
                 "minimum of {places_min} in {an_min}, {places_2020} in 2020; then from {min_admis} to {admis_2025} admissions a "
                 "year from 2021 to 2025.",
           "r1": "2010-2011: alternative routes included", "r2": "2021: end of the numerus clausus", "annot": "%s: %s"},
}


def d1(r, A, L):
    return L["d1"].format(a="%g" % (r["s1"] / 2), b="%g" % (r["s2"] / 2), c=r["mg"], d=A["duree_chiffre"], e=r["mandat"],
                          f="%d" % r["duree_adm"])


def fig_cursus(r: dict, A: dict) -> str:
    H = 236
    x0, x1 = 120, W - 10
    an = x1 - x0
    X = lambda a: x0 + a / r["duree"] * an  # noqa: E731
    L = T[LANG]
    e = cadre(H, "dc", L["t1"], L["s1"], d1(r, A, L))
    y = 70
    deb_int = r["s1"] / 2 + r["s2"] / 2
    segs = [(0, r["s1"] / 2, L["cycles"][0], GRIS_CLAIR), (r["s1"] / 2, r["s2"] / 2, L["cycles"][1], GRIS_CLAIR),
            (deb_int, r["mg"] - 1, None, BLEU_CLAIR), (r["duree"] - 1, 1, None, BLEU)]
    e.append(txt(0, y + 21, L["mg"], 11, INK, weight="600"))
    for a0, l, lab, col in segs:
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="32" fill="%s" stroke="#ffffff" stroke-width="2"/>' % (X(a0), y, X(a0 + l) - X(a0), col))
        if lab:
            e.append(txt((X(a0) + X(a0 + l)) / 2, y + 20, lab, 10, INK, "middle"))
    # un seul bloc « Internat de médecine générale », de quatre ans, la dernière année plus soutenue (arbitrage, graphique 2)
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="32" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (X(deb_int) + 1, y, X(r["duree"]) - X(deb_int) - 2, BLEU))
    e.append(txt((X(deb_int) + X(r["duree"] - 1)) / 2, y + 20, L["cycles"][2], 10, INK, "middle"))
    e.append(txt((X(deb_int) + X(r["duree"])) / 2, y - 6, L["internat"].format(r["mg"]), 10, BLEU, "middle", "600"))
    e.append(txt(X(r["duree"]), y + 46, L["auto"], 9.5, BLEU, "end"))
    ya = y + 62
    e.append('<path d="M%.1f %d V%d H%.1f V%d" fill="none" stroke="%s"/>' % (X(1), ya - 5, ya, X(r["duree"]), ya - 5, INK2))
    e.append(txt(X(1) + 4, ya + 13, L["depuis_adm"].format("%d" % r["duree_adm"]), 10, INK2))
    y2 = 168
    e.append(txt(0, y2 + 21, L["mandat"], 11, INK, weight="600"))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="32" fill="%s"/>' % (X(0), y2, X(r["mandat"]) - X(0), GRIS))
    e.append(txt(X(r["mandat"] / 2), y2 + 20, L["ans"].format(r["mandat"]), 10, "#ffffff", "middle"))
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(0), y2 + 33, X(r["duree"]), y2 + 33, GRID))
    for a in range(0, int(r["duree"]) + 1):
        e.append(txt(X(a), y2 + 50, str(a), 9, MUTED, "middle"))
    return pied(e, H + 2, L["src1"], L["note1"])


def fig_admissions(r: dict, A: dict) -> str:
    H = 330
    d = dict(r["dd76"])
    o = {int(k): v for k, v in r["ondps"]["admis_medecine"].items()}
    ans = list(range(1972, 2026))
    x0, x1, y0, y1 = 50, W - 8, 60, 280
    vmax = 12000
    bw = (x1 - x0) / len(ans)
    X = lambda a: x0 + (a - 1972) * bw  # noqa: E731
    Y = lambda v: y1 - v / vmax * (y1 - y0)  # noqa: E731
    L = T[LANG]
    e = cadre(H, "da", L["t2"], L["s2"], L["d2"].format(min_admis=nb(min(o.values())), **A))
    for v in range(0, vmax + 1, 3000):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (x0, Y(v), x1, Y(v), GRID))
        e.append(txt(x0 - 6, Y(v) + 4, nb(v), 10, MUTED, "end"))
    for a in ans:
        v = d.get(a, o.get(a))
        col = BLEU if a <= 2020 else BLEU_CLAIR
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (X(a) + 0.6, Y(v), bw - 1.2, y1 - Y(v), col))
        if a % 10 == 0 or a == 1972:
            e.append(txt(X(a) + bw / 2, y1 + 14, str(a), 10, MUTED, "middle"))
    # deux rangs : en anglais, les deux étiquettes se touchaient sur un seul (contre-expertise du rendu, 12/10/2026) ;
    # celle de 2010-2011 descend dans la zone vide au-dessus des barres d'avant 2010 (toutes < 9 000)
    for a, lab, ylab in ((2010, L["r1"], y0 + 10), (2021, L["r2"], y0 - 8)):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (X(a), y0 - 4, X(a), y1, INK2))
        e.append(txt(X(a) - 4, ylab, lab, 9, INK2, "end"))
    voisins = max(d[a] for a in range(r["amin"] - 2, r["amin"] + 3))
    ya = Y(voisins) - 22
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (X(r["amin"]) + bw / 2, ya + 4, X(r["amin"]) + bw / 2, Y(d[r["amin"]]) - 2, INK2))
    e.append(txt(X(r["amin"]) + bw / 2, ya, (L["annot"] % (r["amin"], A["places_min"])), 10, INK, "middle", "600"))
    return pied(e, H + 2, L["src2"], L["note2"])


# ------------------------------------------------------------------ figures téléphone (phase B, 12/10/2026)
# Composées pour 300 px de large, jamais rétrécies : police >= FS_MIN ; chaque valeur dessinée (classe « val ») doit
# figurer dans la description de la version détaillée (parite_mobile). Patron : scripts/update_lycee_professeurs.py.
def coupe(s, n):
    """Coupe aux espaces ordinaires ; ponctuation haute, « n° » et nombre + unité soudés (règle typographique du site)."""
    s = re.sub(r" ([:;?!»%])", "\u00a0\\1", s).replace("« ", "«\u00a0").replace("n° ", "n°\u00a0")
    s = re.sub(r"(\d) (ans|years|places)\b", "\\1\u00a0\\2", s)
    s = re.sub(r"\b(art\.|no\.) (\d)", "\\1\u00a0\\2", s)
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


def fig_cursus_m(r, A, svg_d):
    L = T[LANG]
    e, y = tete_m("dcm", L["t1"], desc_de(svg_d))
    X = lambda a: a / r["duree"] * WM  # noqa: E731
    y += 14
    e.append(txt(0, y + 4, L["mg"], 15, INK, weight="600"))
    y += 14
    deb_int = r["s1"] / 2 + r["s2"] / 2
    for a0, l, lab, col, fc in ((0, r["s1"] / 2, L["court"][0], GRIS_CLAIR, INK), (r["s1"] / 2, r["s2"] / 2, L["court"][1], GRIS_CLAIR, INK),
                                (deb_int, r["mg"] - 1, L["court"][2], BLEU_CLAIR, INK), (r["duree"] - 1, 1, None, BLEU, None)):
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="30" fill="%s" stroke="#ffffff" stroke-width="2"/>' % (X(a0), y, X(a0 + l) - X(a0), col))
        if lab:
            e.append(txt((X(a0) + X(a0 + l)) / 2, y + 20, lab, FS_MIN, fc, "middle"))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="30" fill="none" stroke="%s" stroke-width="1.5"/>' % (X(deb_int) + 1, y, X(r["duree"]) - X(deb_int) - 2, BLEU))
    y += 30
    for ligne, col, w in ((L["cycle1_m"].format("%g" % (r["s1"] / 2)), INK2, None), (L["cycle2_m"].format("%g" % (r["s2"] / 2)), INK2, None),
                          (L["internat_m"], BLEU, "600"), (L["dont"].format(r["mg"]), BLEU, None),
                          (L["depuis_adm"].format("%d" % r["duree_adm"]), INK2, None),
                          (L["total"].format(A["duree_chiffre"]), INK, "600")):
        for morceau in coupe(ligne, 36):
            y += 19
            e.append(txt(0, y, morceau, FS_MIN, col, weight=w, cls="val"))
    y += 30
    e.append(txt(0, y, L["mandat"], 15, INK, weight="600"))
    y += 10
    e.append('<rect x="0" y="%d" width="%.1f" height="30" fill="%s"/>' % (y, X(r["mandat"]), GRIS))
    e.append(txt(X(r["mandat"]) / 2, y + 20, L["ans"].format(r["mandat"]), FS_MIN, "#ffffff", "middle", cls="val"))
    y += 30
    e.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (y + 1, WM, y + 1, GRID))
    for a, anc in ((0, "start"), (r["mandat"], "middle"), (int(r["duree"]), "end")):
        e.append(txt(X(a), y + 18, str(a), FS_MIN, MUTED, anc))
    return finir_m(e, y + 32, L["src1"], L["note1"])


def fig_admissions_m(r, A, svg_d):
    L = T[LANG]
    d = dict(r["dd76"])
    o = {int(k): v for k, v in r["ondps"]["admis_medecine"].items()}
    e, y = tete_m("dam", L["t2"], desc_de(svg_d))
    for ligne in coupe(L["s2m"], 38):
        y += 6
        e.append(txt(0, y + 12, ligne, FS_MIN, INK2))
        y += 12
    ans = list(range(1972, 2026))
    X0, X1, TOP = 44, WM - 2, y + 44
    BAS = TOP + 180
    bw = (X1 - X0) / len(ans)
    X = lambda a: X0 + (a - 1972) * bw  # noqa: E731
    Y = lambda v: BAS - v / 12000 * (BAS - TOP)  # noqa: E731
    for gv in (0, 6000, 12000):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (X0, Y(gv), X1, Y(gv), GRID))
        e.append(txt(X0 - 4, Y(gv) + 5, nb(gv), FS_MIN, MUTED, "end"))
    for a in ans:
        v = d.get(a, o.get(a))
        e.append('<rect x="%.1f" y="%.1f" width="%.2f" height="%.1f" fill="%s"/>' % (X(a) + 0.4, Y(v), bw - 0.8, BAS - Y(v), BLEU if a <= 2020 else BLEU_CLAIR))
    for a in (2010, 2021):   # pointillés sous la zone des étiquettes (sinon « 11 133 » les chevauche)
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (X(a), TOP + 34, X(a), BAS, INK2))
    for a, anc in ((1972, "start"), (2000, "middle"), (2025, "end")):
        e.append(txt(X(a) + (0 if anc == "start" else bw if anc == "end" else bw / 2), BAS + 18, str(a), FS_MIN, MUTED, anc))
    e.append(txt(X(1972), Y(d[1972]) - 8, nb(d[1972]), 15, INK, "start", "600", "val"))
    haut = max(d[a] for a in range(r["amin"] - 4, r["amin"] + 5))   # au-dessus des barres voisines
    e.append(txt(X(r["amin"]) + bw / 2, Y(haut) - 8, nb(d[r["amin"]]), 15, INK, "middle", "600", "val"))
    # « 2025 : 11 133 », relié à la dernière barre par un trait (sinon lu comme la valeur de la première barre claire)
    xb = X(2025) + bw / 2
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (xb, Y(o[2025]) - 12, xb, Y(o[2025]) - 1, INK2))
    lab25 = (L["annot"] % (2025, nb(o[2025]))).replace(" :", " :")
    e.append(txt(X(2025) + bw, Y(o[2025]) - 15, lab25, 15, INK, "end", "600", "val"))
    y = BAS + 26
    for ligne in coupe(L["annot"] % (r["amin"], A["places_min"]) + (" (minimum)" if LANG == "fr" else " (lowest)"), 38) + \
            ["- - " + L["r1"], "- - " + L["r2"]]:
        y += 19
        e.append(txt(0, y, ligne, FS_MIN, INK2, cls="val"))
    return finir_m(e, y + 14, L["src2"], L["note2"])


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
    "fr": {"cursus": "Aux règles en vigueur pour les étudiants entrés en internat à partir de la rentrée {an_reforme}, le cursus "
                     "standard de médecine générale dure au moins {duree} ans depuis la première année ({duree_adm} depuis "
                     "l'admission en deuxième année), soit {nfois} la durée d'un mandat présidentiel. Comparaison d'échelle seulement.",
           "admissions": "Les places pourvues en deuxième année du cursus de médecine ont été divisées par {rapport_baisse} entre "
                         "1972 et {an_min} ({places_min} places pourvues), puis sont remontées ; {admis_2021_2025} étudiants ont "
                         "été admis en deuxième année (ou en troisième par une passerelle) de 2021 à 2025."},
    "en": {"cursus": "Under the rules in force for students who entered residency from the {an_reforme} academic year, the "
                     "standard general practice curriculum in France takes at least {duree} years from the first year ({duree_adm} "
                     "from admission to the second year), {nfois} the length of a presidential term. Comparison of scale only.",
           "admissions": "Places filled in the second year of French medical studies were divided by {rapport_baisse} between "
                         "1972 and {an_min} ({places_min} places filled), then rose again; {admis_2021_2025} students were "
                         "admitted to the second year (or the third, through an alternative-entry route) from 2021 to 2025."},
}


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        out = []
        for ident in ("cursus", "admissions"):
            fichier = "delais-" + ident + suf
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
    w.writerow(["serie", "annee", "valeur", "unite", "source"])
    for a, v in sorted(r["dd76"].items()):
        w.writerow(["places_pourvues_medecine", a, v, "places", "DREES Dossier 76, graphique 8 (ONDPS)"])
    for a, v in sorted(r["ondps"]["admis_medecine"].items()):
        w.writerow(["admis_medecine", a, v, "étudiants", "ONDPS, bilan 2021-2025, figure 1"])
    w.writerow(["medecins_actifs_diplome_etranger", 2012, r["etr12"], "médecins", "DREES RPPS, 1er janvier"])
    w.writerow(["medecins_actifs_ensemble", 2012, r["tot12"], "médecins", "DREES RPPS, 1er janvier"])
    w.writerow(["medecins_actifs_diplome_etranger", 2026, r["etr26"], "médecins", "DREES RPPS, 1er janvier"])
    w.writerow(["medecins_actifs_ensemble", 2026, r["tot26"], "médecins", "DREES RPPS, 1er janvier"])
    for k, v in (("cursus_mg_premier_cycle_semestres", r["s1"]), ("cursus_mg_deuxieme_cycle_semestres", r["s2"]),
                 ("cursus_mg_troisieme_cycle_annees", r["mg"]), ("mandat_presidentiel_annees", r["mandat"]),
                 ("rapport_cursus_mandat", r["nmax"])):
        w.writerow([k, "", v, "", "texte en vigueur (Légifrance)"])
    return buf.getvalue()


# ------------------------------------------------------------------ autotest
def _page(lang, quoi):
    def f(m):
        m["pages"][lang] = m["pages"][lang] + "\n" + quoi + "\n"
    return f


def _ondps(cle, v, sous=None):
    def f(m):
        (m["ondps"][sous] if sous else m["ondps"])[cle] = v
    return f


def _texte(src, avant, apres):
    def f(m):
        if avant not in m["textes"][src]["texte"]:
            raise Arret("autotest : ancre de mutation introuvable dans %s : %s" % (src, avant))
        m["textes"][src]["texte"] = m["textes"][src]["texte"].replace(avant, apres)
    return f


MUTATIONS = [  # (nom, mutation, garde qui DOIT arrêter)
    ("« quatre années » altere (rapport non entier)", _texte("L632-2", "d'une durée de quatre années", "d'une durée de trois années"), "D3"),
    ("admis 2023 altere", _ondps("2023", 10982, "admis_medecine"), "D6"),
    ("DREES 2003 altere", lambda m: m["dd76"].__setitem__(2003, 5200), "D5"),
    ("ONP altere", _ondps("onp_2021_2025", 51550), "D6"),
    ("total ONDPS 2016-2020 remplace par la somme DREES", _ondps("2016-2020", 43619, "quinquennaux_figure2"), "D6 bis"),
    ("reforme de 2023 appliquee a une cohorte anterieure", _texte("art37", "année universitaire 2023.", "année universitaire 2022."), "T1"),
    ("horloge demarree en deuxieme annee", _page("fr", "Former un généraliste prend au moins {del.duree} ans depuis l'admission, aux règles de 2023."), "T2"),
    ("inegalite stricte remplacee par une egalite (premiere phase de consolidation = loi + quatre ans jour pour jour)",
     _texte("instr", "dès le 2 novembre 2026", "dès le 23 décembre 2026"), "T4"),
    ("date de la premiere phase de consolidation passee", lambda m: m.__setitem__("aujourdhui", dt.date(2026, 11, 2)), "T3"),
    ("date en clair dans la page", _page("fr", "La quatrième année commence le 2&nbsp;novembre 2026."), "T3"),
    ("date non dite prevue", _page("en", "The fourth year begins on {del.debut_conso}."), "T3"),
    ("admis presentes comme entrants (FR)", _page("fr", "En 2025, {del.admis_2025} étudiants commencent des études de médecine."), "Q1"),
    ("admis presentes comme entrants (EN)", _page("en", "In 2025, {del.admis_2025} students started medical studies."), "Q1"),
    ("titre de figure ambigu", lambda m: m["libelles"]["fr"].__setitem__("t2", "Admissions en études de médecine, 1972-2025"), "Q1"),
    ("admis sans niveau", _page("fr", "En 2025, {del.admis_2025} étudiants ont été admis."), "Q2"),
    ("capacites appelees places", _page("fr", "Il y avait {del.capacites_2025} places en 2025."), "Q2"),
]


def autotest(S: dict) -> list[str]:
    out = []
    for nom, mut, pref in MUTATIONS:
        m = copy.deepcopy(S)
        mut(m)
        try:
            verifier(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not re.match(r"%s\b" % re.escape(pref) + (r"(?! bis)" if pref == "D6" else ""), str(e)):
                raise Arret("mutation %s : arretee par une autre garde que %s : %s" % (nom, pref, e))
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
    r, g = verifier(S)
    for m in autotest(S):
        log("autotest : la mutation a mordu : " + m)
    cit = citations(S["textes"])
    A = dict(affichage(r, "fr"), **cit)
    A.update({k + "_tr": v for k, v in TR.items()})
    A["cit_art6a_en"] = CIT_ART6_EN
    A_en = dict(affichage(r, "en"), **cit)
    A_en.update({k + "_tr": v for k, v in TR.items()})
    A_en["cit_art6a_en"] = CIT_ART6_EN
    if set(A) != set(A_en):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    g.append("D1 bis : %d citations des textes retrouvees mot pour mot ; D1 ter : %d traductions, nombres controles"
             % (len(CITATIONS), len(TR)))
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        figs["delais-cursus%s.svg" % suf] = fig_cursus(r, AA)
        figs["delais-admissions%s.svg" % suf] = fig_admissions(r, AA)
        figs["delais-cursus%s-m.svg" % suf] = fig_cursus_m(r, AA, figs["delais-cursus%s.svg" % suf])
        figs["delais-admissions%s-m.svg" % suf] = fig_admissions_m(r, AA, figs["delais-admissions%s.svg" % suf])
    LANG = "fr"
    nv = parite_mobile(figs)
    fi = fiches(figs, A, A_en)
    n = prose({"fiches " + l: "\n".join(f["titre"] + "\n" + f["montre"] for f in v) for l, v in fi.items()}, r["an_reforme"])
    g.append("parite des %d figures telephone (%d valeurs dessinees) ; Q1-Q2 sur les fiches Reutiliser"
             % (len([k for k in figs if k.endswith("-m.svg")]), nv))
    if "--check" in sys.argv[1:]:
        for x in g:
            log("OK " + x)
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    csvt = csv_texte(r)
    T_ = S["textes"]
    payload = {
        "releve_le": "2026-10-12",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Légifrance (DILA), DREES, ONDPS, Bulletin officiel santé",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Délais, E1 à E3 ; refonte du 12/10/2026",
                 "textes": {k: {"id": v["id"], "sha256": v["sha"]} for k, v in T_.items()},
                 "definitions": {
                     "duree_cursus": "somme des durées minimales écrites (sans redoublement, interruption ni passerelle), "
                                     "pour les étudiants qui commencent le troisième cycle (internat) à partir de la rentrée "
                                     "%d ; comptée depuis la première année d'études, ou depuis l'admission en deuxième "
                                     "année du premier cycle (une année de moins)" % r["an_reforme"],
                     "niveau_d_admission": "places pourvues et admis comptent des admissions en deuxième année du premier "
                                           "cycle, ou directement en troisième année pour certaines passerelles ; la "
                                           "première année n'est pas comptée",
                     "places_pourvues": "jusqu'en 2009, numerus clausus principal ; à partir de 2011 (2010 partiellement), "
                                        "numerus clausus principal et complémentaire, passerelles et droits au remords "
                                        "(DREES, note du graphique 8) ; places pourvues et non places ouvertes",
                     "admis_2021_2025": "étudiants admis en deuxième année du premier cycle (ou en troisième par une "
                                        "passerelle), relevés par l'ONDPS auprès des universités",
                     "capacites_accueil": "places en deuxième et troisième années du premier cycle votées chaque année par "
                                          "chaque université (code de l'éducation, art. L631-1) ; ce ne sont pas des admis",
                     "onp": "objectif national pluriannuel de professionnels à former, fixé par l'État pour 2021-2025 "
                            "(arrêté du 13 septembre 2021, selon l'ONDPS) ; un nombre à former, ni des admis ni des diplômés",
                     "total_2016_2020": "somme sur 5 ans du numerus clausus total, passerelles comprises (ONDPS, note 6) ; "
                                        "lu sur l'image de la figure 2, relu le 12/10/2026, contrôlé par la hausse de 27 % "
                                        "et la moyenne annuelle de 8 700 places imprimées dans le texte",
                     "diplome_etranger": "médecins actifs au 1er janvier dont le diplôme a été obtenu à l'étranger : un "
                                         "stock, pas un flux d'arrivées ; le lieu du diplôme ne dit pas la nationalité",
                     "debut_consolidation": "date PRÉVUE par l'instruction du 21 mai 2026 (document non opposable), non "
                                            "constatée au relevé"},
                 "ecart_documente": {"2016-2020": "la somme des valeurs DREES dépasse de %d le total imprimé par l'ONDPS ; "
                                                  "non expliqué (la valeur 2020 de la DREES porte un astérisque sans légende "
                                                  "trouvée) ; publié, non corrigé" % r["ecarts"]["2016-2020"]}},
        "gardes": g,
        "calcul": {k: v for k, v in r.items() if k not in ("dd76", "ondps", "lois631", "versions631")},
        "series": {"places_pourvues": r["dd76"], "admis_2021_2025": r["ondps"]["admis_medecine"]},
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
    log("Ecrit : data/promesses_delais.json, static/promesses_delais.{json,csv}, data/figures_delais.json, %d figures SVG + PNG"
        % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
