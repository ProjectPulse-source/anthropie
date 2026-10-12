#!/usr/bin/env python3
"""Prolongement « Référendum » du dossier Promesses : le registre des référendums nationaux et le référendum
d'initiative partagée, arrêtés au 05/10/2026.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, « Prolongement R » (gelé au
commit 324c9cd du dépôt D:/PRO) ; tests décisifs R-E1 et R-E2 (commit 368a020), décision de l'auteur du 06/10/2026 sur
R-E2 (option a : la page dit les dépôts sans saisine, sans leur prêter de cause). Phase B de la refonte (12/10/2026) :
REFONTE_PILOTE/REFERENDUM/ARBITRAGE_CE_REFERENDUM_PHASE_A.md et la section « Référendum » de
ARBITRAGE_CE_RELECTURE_JURIDIQUE_PROMESSES_2026-10-12.md.

Entrées (script LOCAL : les archives ne sont pas dans le dépôt du site ; il s'arrête si elles manquent ; aucune lecture
en direct, aucune donnée nouvelle ne peut entrer en silence) :
  - stock CONSTIT de la DILA (décisions du Conseil constitutionnel), global du 13/07/2025 et incréments jusqu'au
    05/10/2026, extrait sous .../sondes/referendum/constit/ ;
  - articles de la Constitution, de l'ordonnance n° 58-1067, de la loi organique n° 2013-1114 et du code civil archivés
    par le serveur `sources` (API Légifrance, D:/PRO/02_FABRIQUE/sources/archive) ;
  - pièces hors Légifrance archivées le 12/10/2026 avec leur empreinte (REFONTE_PILOTE/REFERENDUM/sources_phase_b/,
    SHA256SUMS.txt) : textes adoptés par le Congrès le 4/02/2008 et le 21/07/2008 (site du Sénat ; la page JORF de
    Légifrance refuse les scripts, canal changé), dossier législatif du Sénat pjl20-449, déclaration publiée par
    l'Élysée le 29/06/2020, proposition de loi n° 459 (2017-2018) du Sénat.
Le témoin du Journal officiel (décrets de soumission, lois promulguées) et le témoin de l'Assemblée nationale (dépôts au
titre de l'art. 11) ont été exécutés hors de ce script (test_decisif/referendum/) ; leurs résultats sont repris ici,
identifiants compris, et le script vérifie qu'ils correspondent toujours au registre.

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  R1  registre : 9 proclamations ; oui + non = exprimés ; exprimés <= votants <= inscrits ; décret de soumission lu dans
      le visa de chaque proclamation ;
  R2  concordance avec le témoin JO, scrutin par scrutin : décret à la date du visa, loi promulguée si et seulement si
      le texte est adopté ;
  R3  RIP : chaque saisine a sa solution ; chaque non-conformité cite la condition de l'art. 45-2 non remplie ; la
      seule conformité porte la déclaration des soutiens (lus, pas recalculés) ;
  R4  citations : chaque passage entre guillemets de la page qui vient d'un texte archivé (Constitution, ordonnance,
      loi organique, code civil) y est retrouvé mot pour mot, sa version anglaise dans la traduction du Conseil
      constitutionnel ; chaque motif cité d'une décision RIP est retrouvé mot pour mot DANS LE CONSIDÉRANT dont la page
      donne le numéro (12/10 : un motif cité sous le mauvais numéro arrête) ;
  R5  phrases : comptes recalculés ; « aucune n'a réuni le soutien requis » ; rejets nommés 1969 et 2005 ; « aucun
      scrutin sur le fondement de l'art. 88-5 » (aucun scrutin du registre depuis son entrée dans la Constitution ne
      porte sur une adhésion) ;
  R6  dépôts sans saisine identiques au témoin Assemblée-Sénat ;
  R7  décision 62-20 DC et loi 62-1292 ;
  R8  (12/10) pièces hors Légifrance : empreinte de chaque fichier égale à SHA256SUMS.txt, et chaque passage que la
      page en cite ou en tire (clause du 1er juillet 2004, procédure du Congrès, déclaration du 29/06/2020, étapes du
      dossier pjl20-449) retrouvé mot pour mot ; la dernière étape datée du dossier du Sénat est celle que la page dit ;
  R9  (12/10) signataires des dépôts sans saisine : le nombre transcrit est relu dans le témoin de l'Assemblée (auteurs +
      cosignataires) et dans le texte déposé au Sénat (archivé, R8).
Autotest de mutation à chaque exécution : chaque garde nouvelle doit mordre sur SA mutation, sinon le script échoue.

Écrit : data/promesses_referendum.json (+ static/), static/promesses_referendum.csv (UTF-8 BOM, format long),
data/figures_referendum.json, static/img/referendum-registre(-en)(-m).svg/.png, referendum-rip(-en)(-m).svg/.png.
Rien n'est écrit à données identiques (fiches « Réutiliser » comprises). `--check` n'écrit rien. Sortie console ASCII.
Nombres et lettres : scripts/langue_generee.py ; pied des figures : scripts/pied_figure.py.
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
PIECES = PRO / "06_PROMOTION" / "RECHERCHE_LYCEES_LECTURE_2026-10-09" / "REFONTE_PILOTE" / "REFERENDUM" / "sources_phase_b"
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "sources_promesses_en"))
import constitution_en as cen  # noqa: E402
import langue_generee as lg  # noqa: E402  -- nombres et lettres (organe commun)
import pied_figure  # noqa: E402  -- pied commun des figures détaillées

ARRETE = "2026-10-05"
PAGE_URL = "stephane-lalut.com/un-president-peut-il-recourir-au-referendum/"
PAGE_URL_EN = "stephane-lalut.com/en/can-the-french-president-call-a-referendum/"
OUT_DATA = ROOT / "data" / "promesses_referendum.json"
OUT_STATIC = ROOT / "static" / "promesses_referendum.json"
OUT_CSV = ROOT / "static" / "promesses_referendum.csv"
OUT_FIGURES = ROOT / "data" / "figures_referendum.json"
OUT_IMG = ROOT / "static" / "img"
# texte -> (LEGIARTI, archive `sources`). Les clés sans préfixe sont des articles de la Constitution (traduction anglaise du
# Conseil vérifiée) ; « o » ordonnance n° 58-1067, « lo » loi organique n° 2013-1114, « cc » code civil (cités en français,
# suivis de notre traduction sur la page anglaise).
ARTICLES = {
    "3": ("LEGIARTI000019240995", "2026-10/2b5639c959fce37006de2d076ddd81a76e9d7599c4d9e9cab4ad35deb29ecc50.json"),
    "11": ("LEGIARTI000019241004", "2026-09/e4718a1b13a755204ea409d81c5025811a2bfb29fb5e6fae0bc10a87d19367d8.json"),
    "19": ("LEGIARTI000006527482", "2026-10/6f964a9686927f9c174efa86fc1dcba43b752b7a94c135ff58e9295e19c59efb.json"),
    "60": ("LEGIARTI000006527548", "2026-10/f656b0168a0ba65883300603e607fde04bfec939640a048a721567ab3c539064.json"),
    "61": ("LEGIARTI000019241074", "2026-10/c14abed78a1e9932d2cf37f84e6366e03847a41174d17466b5f83b4a0a3d299c.json"),
    "88-5": ("LEGIARTI000018077285", "2026-10/74232615eacf35866333fd388b977914dbfe65e66d839cd030c690f503f060cf.json"),
    "89": ("LEGIARTI000019240655", "2026-10/0caaf2457602bce55a86b6825cd567e7bca2a4a2d82794135566b840d7c58eee.json"),
    "o45-2": ("LEGIARTI000028280493", "2026-10/0739986eb516531ec30dce183a952ac0f835bd9ffdd52bbdc6a4c5bb06abf1fa.json"),
    "lo1": ("LEGIARTI000028280452", "2026-10/8e8440fa7f764b6386c82fb269a6abeed0418d20ed6a872a85675b6509fa8928.json"),
    "lo4": ("LEGIARTI000028280470", "2026-10/3f89ac87be83d8ddecdd572a49e8c9ab7f7405284e98c99a091603a995964fe0.json"),
    "lo9": ("LEGIARTI000028280466", "2026-10/a1bff9735e709fc8f5ee091343578411ee2559f309155edbb330f27f24f34178.json"),
    "cc1": ("LEGIARTI000006419280", "2026-10/cc0765ea833ba2ee7901764e2b924cd6bebc1122f1273afe63316f12a6604f33.json"),
}
# Citations de la page : clé -> (texte, citation française, citation anglaise de la traduction du Conseil constitutionnel ou
# notre traduction pour les textes hors Constitution). Une citation de la Constitution est vérifiée dans les deux langues ;
# une autre, en français seulement (sa traduction est la nôtre, dite comme telle sur la page anglaise).
CIT = {
    "art3": ("3", "La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum.",
             "National sovereignty shall vest in the people, who shall exercise it through their representatives and by means of referendum."),
    "art11_peut": ("11", "peut soumettre au référendum tout projet de loi", "submit to a referendum any Government Bill"),
    "art11_1": ("11", "sur proposition du Gouvernement pendant la durée des sessions ou sur proposition conjointe des deux assemblées, publiées au Journal officiel",
                "on a recommendation from the Government when Parliament is in session, or on a joint motion of the two Houses, published in the Journal Officiel"),
    "art11_objet": ("11", "portant sur l'organisation des pouvoirs publics, sur des réformes relatives à la politique économique, sociale ou environnementale de la nation et aux services publics qui y concourent, ou tendant à autoriser la ratification d'un traité qui, sans être contraire à la Constitution, aurait des incidences sur le fonctionnement des institutions",
                    "which deals with the organization of the public authorities, or with reforms relating to the economic, social or environmental policy of the Nation, and to the public services contributing thereto, or which provides for authorization to ratify a treaty which, although not contrary to the Constitution, would affect the functioning of the institutions"),
    "art11_decl": ("11", "celui-ci fait, devant chaque assemblée, une déclaration qui est suivie d'un débat",
                   "the latter shall make a statement before each House and the same shall be followed by a debate"),
    "art11_promulgue": ("11", "le Président de la République promulgue la loi dans les quinze jours qui suivent la proclamation des résultats de la consultation",
                        "the President of the Republic shall promulgate the resulting statute within fifteen days following the proclamation of the results of the vote"),
    "art11_rip": ("11", "à l'initiative d'un cinquième des membres du Parlement, soutenue par un dixième des électeurs inscrits sur les listes électorales",
                  "upon the initiative of one fifth of the members of Parliament, supported by one tenth of the voters enrolled on the electoral lists"),
    "art11_abrog": ("11", "ne peut avoir pour objet l'abrogation d'une disposition législative promulguée depuis moins d'un an",
                    "may not be applied to the repeal of a legislative provision promulgated for less than one year"),
    "art11_deux_ans": ("11", "aucune nouvelle proposition de référendum portant sur le même sujet ne peut être présentée avant l'expiration d'un délai de deux ans suivant la date du scrutin",
                       "no new referendum proposal on the same subject may be submitted before the end of a period of two years following the date of the vote"),
    "art11_soumet": ("11", "le Président de la République la soumet au référendum",
                     "the President of the Republic may submit it to a referendum"),
    "art19": ("19", "Les actes du Président de la République autres que ceux prévus aux articles 8 (1er alinéa), 11, 12, 16, 18, 54, 56 et 61 sont contresignés par le Premier ministre",
              "Instruments of the President of the Republic, other than those provided for under articles 8 (paragraph one), 11, 12, 16, 18, 54, 56 and 61, shall be countersigned by the Prime Minister"),
    "art60": ("60", "Le Conseil constitutionnel veille à la régularité des opérations de référendum prévues aux articles 11 et 89 et au titre XV. Il en proclame les résultats.",
              "The Constitutional Council shall ensure the proper conduct of referendum proceedings as provided for in articles 11 and 89 and in Title XV and shall proclaim the results of the referendum."),
    "art61": ("61", "les propositions de loi mentionnées à l'article 11 avant qu'elles ne soient soumises au référendum",
              "Private Members' Bills mentioned in article 11 before they are submitted to referendum"),
    "art88_5_1": ("88-5", "Tout projet de loi autorisant la ratification d'un traité relatif à l'adhésion d'un État à l'Union européenne est soumis au référendum par le Président de la République.",
                  "Any government bill authorizing the ratification of a treaty pertaining to the accession of a state to the European Union shall be submitted to referendum by the president of the republic."),
    "art88_5_2": ("88-5", "par le vote d'une motion adoptée en termes identiques par chaque assemblée à la majorité des trois cinquièmes, le Parlement peut autoriser l'adoption du projet de loi selon la procédure prévue au troisième alinéa de l'article 89",
                  "by passing a motion adopted in identical terms in each House by a three-fifths majority, Parliament may authorize the passing of the bill according to the procedure provided for in paragraph three of article 89"),
    "art88_5_2004": ("88-5", None,  # la clause n'est pas dans l'article : texte français lu dans la LC 2008-724 (R8)
                     "Article 88-5 is not applicable to accessions that result from an Intergovernmental Conference whose meeting was decided by the European Council before July 1, 2004."),
    "art89_init": ("89", "L'initiative de la révision de la Constitution appartient concurremment au Président de la République sur proposition du Premier ministre et aux membres du Parlement.",
                   "The President of the Republic, on the recommendation of the Prime Minister, and Members of Parliament alike shall have the right to initiate amendments to the Constitution."),
    "art89_identiques": ("89", "voté par les deux assemblées en termes identiques", "be passed by the two Houses in identical terms"),
    "art89_ref": ("89", "La révision est définitive après avoir été approuvée par référendum.",
                  "The amendment shall take effect after approval by referendum."),
    "art89_voies": ("89", "le projet de révision n'est pas présenté au référendum lorsque le Président de la République décide de le soumettre au Parlement convoqué en Congrès",
                    "a Government Bill to amend the Constitution shall not be submitted to referendum where the President of the Republic decides to submit it to Parliament convened in Congress"),
    "art89_limites": ("89", "Aucune procédure de révision ne peut être engagée ou poursuivie lorsqu'il est porté atteinte à l'intégrité du territoire. La forme républicaine du Gouvernement ne peut faire l'objet d'une révision.",
                      "No amendment procedure shall be commenced or continued where the integrity of national territory is placed in jeopardy. The republican form of government shall not be the object of any amendment."),
    "o45_2_delai": ("o45-2", "dans le délai d'un mois à compter de la transmission de la proposition de loi",
                    "within one month of the transmission of the bill"),
    "lo1": ("lo1", "La proposition de loi est transmise au Conseil constitutionnel par le président de l'assemblée saisie.",
            "The bill is forwarded to the Conseil constitutionnel by the president of the House in which it was tabled."),
    "lo4": ("lo4", "La durée de la période de recueil des soutiens est de neuf mois.",
            "The period for collecting signatures of support is nine months."),
    "lo9": ("lo9", "n'a pas été examinée au moins une fois par chacune des deux assemblées parlementaires dans un délai de six mois à compter de la publication au Journal officiel de la décision du Conseil constitutionnel déclarant qu'elle a obtenu le soutien d'au moins un dixième des électeurs inscrits sur les listes électorales",
            "has not been considered at least once by each of the two Houses of Parliament within six months of the publication in the Journal officiel of the decision of the Conseil constitutionnel declaring that it has obtained the support of at least one tenth of the voters registered on the electoral lists"),
    "lo9_susp": ("lo9", "Ce délai est suspendu entre deux sessions ordinaires.",
                 "This period is suspended between two ordinary sessions."),
    "cc1": ("cc1", "l'entrée en vigueur de celles de leurs dispositions dont l'exécution nécessite des mesures d'application est reportée à la date d'entrée en vigueur de ces mesures",
            "the entry into force of those of their provisions whose implementation requires implementing measures is postponed until the date on which those measures enter into force"),
}
CONSTITUTION = {"3", "11", "19", "60", "61", "88-5", "89"}
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
# Objet de chaque scrutin, en mots de la page (titres de la proclamation, du décret ou de la loi au JO) : TRANSCRIT.
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
# Art. 88-5 : première version en vigueur le 2/03/2005 (versions de LEGIARTI000018077285, API Légifrance, 12/10/2026).
DEBUT_88_5 = "2005-03-02"
# Témoin de l'Assemblée nationale (test_decisif/referendum/test_r_e2.py) : dépôts « en application de l'article 11 »
# sans décision du Conseil (décision de l'auteur, 06/10/2026 : dits au lecteur, sans cause).
# Témoin du Sénat ajouté le 07/10/2026 (Dosleg, type « refe » ; EVALUATION_UNICITE_PUBLICS.md, C1) : ppl17-459.
# Signataires transcrits ici, relus par R9 (12/10/2026) dans le témoin de l'Assemblée et dans le texte déposé au Sénat.
DEPOTS_SANS_SAISINE = [
    {"chambre": "Sénat", "numero": "459", "legislature": "2017-2018", "date": "2018-04-20", "auteurs": 2,
     "objet": "renforcer le contrôle de l'immigration en France",
     "objet_en": "strengthening immigration control in France"},
    {"chambre": "AN", "numero": "1749", "legislature": "XVe", "date": "2019-03-06", "auteurs": 2,
     "objet": "mesures d'exception contre les djihadistes français ayant combattu en Irak et en Syrie",
     "objet_en": "exceptional measures against French jihadists who fought in Iraq and Syria"},
    {"chambre": "AN", "numero": "5203", "legislature": "XVe", "date": "2022-04-05", "auteurs": 1,
     "objet": "lutter contre les mauvais traitements envers les animaux",
     "objet_en": "combating the mistreatment of animals"},
]
MOIS = {m: i + 1 for i, m in enumerate("janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split())}
MOIS_FR = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def fr(n: float, dec: int = 0) -> str:
    return lg.nombre(n, dec, "fr")


def en(n: float, dec: int = 0) -> str:
    return lg.nombre(n, dec, "en")


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
        raise Arret("texte %s : archive absente (%s)" % (n, rel))
    d = json.loads(p.read_text(encoding="utf-8"))
    a = d.get("article") or d.get("contenu") or d
    if a.get("id") != leg:
        raise Arret("texte %s : l'archive porte %s, attendu %s" % (n, a.get("id"), leg))
    return norm(a["texte"])


# ------------------------------------------------------------------ pièces hors Légifrance (R8)
def texte_html(b: bytes) -> str:
    s = b.decode("utf-8")
    s = re.sub(r"\s*<sup>\s*(.*?)\s*</sup>", r"\1", s, flags=re.S)       # « 1<sup>er</sup> » -> « 1er »
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    return norm(html.unescape(re.sub(r"<[^>]+>", " ", s)))


def sommes() -> dict[str, str]:
    f = PIECES / "SHA256SUMS.txt"
    if not f.is_file():
        raise Arret("R8 : %s absent" % f)
    out = {}
    for l in f.read_text(encoding="utf-8").splitlines():
        if l.strip():
            h, nom = l.split(None, 1)
            out[nom.lstrip("*").strip()] = h
    return out


# fichier -> passages cités ou tirés par la page (mot pour mot, après normalisation des espaces)
PIECES_CITEES = {
    "senat_tac07-002_congres_2008-07-21.html": [
        "CONGRÈS DU PARLEMENT 21 JUILLET 2008",
        "Le Parlement, réuni en Congrès, a approuvé dans les conditions prévues à l'article 89, alinéa 3, de la Constitution",
        "L'article 88-5 de la Constitution, dans sa rédaction résultant tant de l'article 44 de la présente loi constitutionnelle que du 2° du I du présent article, n'est pas applicable aux adhésions faisant suite à une conférence intergouvernementale dont la convocation a été décidée par le Conseil européen avant le 1er juillet 2004.",
    ],
    "senat_tac07-001_congres_2008-02-04.html": [
        "CONGRÈS DU PARLEMENT 4 février 2008",
        "Le Parlement, réuni en Congrès, a approuvé, dans les conditions prévues à l'article 89, alinéa 3, de la Constitution",
    ],
    "elysee_2020-06-29_convention_climat.html": [
        "Je suis favorable à cette proposition.",
        "je suis prêt à recourir au référendum si celui-ci était alors constitutionnellement possible après le vote des chambres dans le cadre strict de notre Constitution",
    ],
    "senat_dossier_pjl20-449.html": [
        "Projet de loi constitutionnelle complétant l'article 1er de la Constitution et relatif à la préservation de l'environnement",
        "Page mise à jour le 1er juillet 2024",
    ],
    "senat_ppl17-459.html": ["Enregistré à la Présidence du Sénat le 20 avril 2018"],
}
# Dossier pjl20-449 : étapes que la page date (ISO, passage du dossier du Sénat). La dernière doit être la dernière du dossier.
ETAPES_2021 = [
    ("depot", "2021-01-20", "déposé à l'Assemblée Nationale le 20 janvier 2021"),
    ("an1", "2021-03-16", "Texte n° 577 adopté par l'Assemblée nationale le 16 mars 2021"),
    ("se1", "2021-05-10", "Texte n° 105 (2020-2021) modifié par le Sénat le 10 mai 2021"),
    ("an2", "2021-06-22", "Texte n° 634 adopté avec modifications par l'Assemblée nationale le 22 juin 2021"),
    ("se2", "2021-07-05", "Texte n° 133 (2020-2021) modifié par le Sénat le 5 juillet 2021"),
]
DECLARATION_2020 = "2020-06-29"  # date de la page de l'Élysée (adresse /2020/06/29/, vérifiée par R8)
CIT_ELYSEE = PIECES_CITEES["elysee_2020-06-29_convention_climat.html"][1]
# Passages repris sur la page : extraits des passages vérifiés ci-dessus (un extrait d'un passage retrouvé l'est aussi).
CLAUSE_2004 = PIECES_CITEES["senat_tac07-002_congres_2008-07-21.html"][2]
CLAUSE_2004_PAGE = CLAUSE_2004[CLAUSE_2004.index("n'est pas applicable"):].rstrip(".")
CONGRES_2008_PAGE = "dans les conditions prévues à l'article 89, alinéa 3, de la Constitution"
if CONGRES_2008_PAGE not in PIECES_CITEES["senat_tac07-001_congres_2008-02-04.html"][1]:
    raise SystemExit("extrait du texte du Congrès du 4/02/2008 hors du passage vérifié")


def lire_pieces(altere: str | None = None) -> dict[str, str]:
    """altere : nom d'une pièce dont une copie EN MÉMOIRE reçoit un octet de plus (autotest)."""
    h = sommes()
    out = {}
    for nom in PIECES_CITEES:
        p = PIECES / nom
        if not p.is_file():
            raise Arret("R8 : pièce absente : %s" % nom)
        b = p.read_bytes() + (b" " if nom == altere else b"")
        if hashlib.sha256(b).hexdigest() != h.get(nom):
            raise Arret("R8 : %s : empreinte différente de SHA256SUMS.txt" % nom)
        out[nom] = texte_html(b)
    return out


def verifier_pieces(t: dict[str, str], citees=None, etapes=None) -> str:
    citees = PIECES_CITEES if citees is None else citees
    etapes = ETAPES_2021 if etapes is None else etapes
    n = 0
    for nom, passages in citees.items():
        for c in passages:
            if norm(c) not in t[nom]:
                raise Arret("R8 : %s : passage introuvable : %s" % (nom, c[:60]))
            n += 1
    d = t["senat_dossier_pjl20-449.html"]
    for _, iso, c in etapes:
        if norm(c) not in d or jour(c) != iso:
            raise Arret("R8 : pjl20-449 : étape introuvable ou mal datée : %s" % c[:60])
    dates = [jour(m.group(1)) for m in re.finditer(r"(?:adopté|modifié)[^.;]{0,40}? le (\d{1,2}(?:er)? \w+ \d{4})", d)]
    if not dates or max(dates) != etapes[-1][1]:
        raise Arret("R8 : pjl20-449 : dernière étape du dossier %s, la page dit %s" % (max(dates) if dates else None, etapes[-1][1]))
    if "/2020/06/29/" not in (PIECES / "elysee_2020-06-29_convention_climat.html").read_text(encoding="utf-8"):
        raise Arret("R8 : page de l'Élysée : date du 29/06/2020 absente de l'adresse canonique")
    return "R8 : %d pièces hors Légifrance à leur empreinte, %d passages et %d étapes retrouvés, dernière étape %s" % (
        len(citees), n, len(etapes), etapes[-1][1])


# ------------------------------------------------------------------ signataires (R9)
def signataires_senat(t: str) -> int:
    i, j = t.find("PRÉSENTÉE"), t.find("EXPOSÉ DES MOTIFS")
    if i < 0 or j < i:
        raise Arret("R9 : texte du Sénat n° 459 : bloc des signataires introuvable")
    return len(re.findall(r"\b(?:M\.|Mme|MM\.)\s", t[i:j]))


def verifier_signataires(t_pieces: dict, depots=None) -> str:
    depots = DEPOTS_SANS_SAISINE if depots is None else depots
    if not TEMOIN_RIP.exists():
        raise Arret("R9 : sortie du témoin absente (%s)" % TEMOIN_RIP)
    an = {re.sub(r"\D", "", d["uid"][-5:]).lstrip("0"): d["auteurs"] + d["cosignataires"]
          for d in json.loads(TEMOIN_RIP.read_text(encoding="utf-8")).get("depots_sans_saisine", [])}
    for d in depots:
        lu = signataires_senat(t_pieces["senat_ppl17-459.html"]) if (d["chambre"], d["numero"]) == ("Sénat", "459") else an.get(d["numero"])
        if lu is None:
            raise Arret("R9 : %s n° %s : aucune source de signataires" % (d["chambre"], d["numero"]))
        if lu != d["auteurs"]:
            raise Arret("R9 : %s n° %s : %d signataire(s) transcrit(s), %d lu(s)" % (d["chambre"], d["numero"], d["auteurs"], lu))
    return "R9 : signataires des %d dépôts relus (Assemblée : témoin ; Sénat : texte déposé)" % len(depots)


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
        if s["solution"] != "Conformité" and n not in MOTIFS:
            raise Arret("R3 : %s non conforme sans motif cité" % n)
    g.append("R3 : %d saisines, solutions et conditions lues, un motif cité par non-conformité" % len(S))
    return g


def considerant(texte: str, k: int) -> str:
    m = re.search(r"(?:^|\s)%d\. (.*?)(?=\s%d\. |\sLE CONSEIL CONSTITUTIONNEL DÉCIDE)" % (k, k + 1), texte)
    return m.group(1) if m else ""


def verifier_citations(textes: dict, motifs: dict, S: dict, cit=None) -> list[str]:
    cit = CIT if cit is None else cit
    for k, (n, f, e) in cit.items():
        if f is not None and norm(f) not in textes[n]:
            raise Arret("R4 : citation %s introuvable dans le texte %s" % (k, n))
        if n in CONSTITUTION and e:
            try:
                cen.citer(n, e)
            except ValueError as exc:
                raise Arret("R4 : citation anglaise %s : %s" % (k, exc))
    nm = 0
    for num, lignes in motifs.items():
        for cle, k, f, _ in lignes:
            if norm(f) not in considerant(S[num]["texte"], k):
                raise Arret("R4 : motif %s : introuvable au considérant %d de la décision %s" % (cle, k, num))
            nm += 1
    return ["R4 : %d citations des textes archivés (dont %d de la Constitution, vérifiées en anglais) et %d motifs retrouvés "
            "mot pour mot dans leur considérant" % (len(cit), sum(1 for v in cit.values() if v[0] in CONSTITUTION), nm)]


# Décision n° 2007-560 DC (traité de Lisbonne), citée par la page : (citation, numéro).
CIT_2007_560 = ("ne peut intervenir qu'après révision de la Constitution", "2007-560")
TITRE_LISBONNE = "Traité de Lisbonne modifiant le traité sur l'Union européenne et le traité instituant la Communauté européenne"
DEC_62_20 = ("62-20", "1962-11-06", "Incompétence pour statuer", "Président du Sénat", "n'a pas compétence")


def verifier_62_20(par_id: dict, dec=DEC_62_20) -> str:
    num, date, sol, saisi, dispositif = dec
    s = next((s for s in par_id.values() if champ(s, "NUMERO") == num and champ(s, "NATURE") == "DC"), None)
    if not s or champ(s, "DATE_DEC") != date or champ(s, "SOLUTION") != sol:
        raise Arret("R7 : décision %s DC absente du stock, ou date / solution différentes" % num)
    t = norm(contenu(s))
    if norm(saisi) not in t or norm(dispositif) not in t:
        raise Arret("R7 : décision %s DC : saisine ou dispositif cités introuvables" % num)
    if TEMOIN_JO["1962-10-28"][2] != "62-1292":
        raise Arret("R7 : loi référendaire du 28 octobre 1962 : témoin du JO différent de 62-1292")
    return "R7 : décision %s DC (%s, %s), saisine du président du Sénat ; loi 62-1292 au témoin du JO" % (num, date, sol)


def verifier_2007_560(par_id: dict) -> str:
    s = next((s for s in par_id.values() if champ(s, "NUMERO") == CIT_2007_560[1] and champ(s, "NATURE") == "DC"), None)
    if not s or CIT_2007_560[0] not in norm(contenu(s)) or norm(TITRE_LISBONNE) not in norm(s):
        raise Arret("R4 : citation de la décision %s DC introuvable" % CIT_2007_560[1])
    return "R4 : décision %s DC (%s) citée mot pour mot" % (CIT_2007_560[1], champ(s, "DATE_DEC"))


# Motifs cités, mot pour mot, avec le numéro du considérant (R-E2 : jamais une catégorie maison ; arbitrage du 12/10 :
# la situation juridique, le raisonnement et la conclusion, dans l'ordre de la décision). Traduction : la nôtre.
# num -> [(clé de jeton, considérant, citation, notre traduction)]
MOTIFS = {
    "2021-2": [("m21_10", 10, "Ces dispositions, qui subordonnent à l'avis conforme de la Conférence nationale de santé l'exercice du pouvoir réglementaire du Premier ministre, sont contraires à la Constitution",
                "These provisions, which make the exercise of the Prime Minister's regulatory power subject to the binding opinion of the National Health Conference, are contrary to the Constitution")],
    "2022-3": [("m22_5a", 5, "Elle a ainsi pour seul effet d'abonder le budget de l'État par l'instauration jusqu'au 31 décembre 2025 d'une mesure qui se borne à augmenter le niveau de l'imposition existante des bénéfices de certaines sociétés",
                "Its sole effect is thus to increase the State budget by introducing, until 31 December 2025, a measure that merely raises the existing level of taxation of certain companies' profits"),
               ("m22_5b", 5, "Elle ne porte donc pas, au sens de l'article 11 de la Constitution, sur une réforme relative à la politique économique de la nation",
                "It therefore does not relate, within the meaning of Article 11 of the Constitution, to a reform concerning the economic policy of the nation")],
    "2023-4": [("m23_7", 7, "l'article L. 161-17-2 du code de la sécurité sociale prévoit que l'âge d'ouverture du droit à une pension de retraite mentionné à ces mêmes dispositions est fixé à soixante-deux ans",
                "article L. 161-17-2 of the Social Security Code provides that the age at which the right to a retirement pension under these same provisions opens is set at sixty-two"),
               ("m23_8", 8, "n'emporte pas de changement de l'état du droit", "does not change the state of the law"),
               ("m23_9", 9, "le législateur peut toujours modifier, compléter ou abroger des dispositions législatives antérieures, qu'elles résultent d'une loi votée par le Parlement ou d'une loi adoptée par voie de référendum",
                "the legislature may always amend, supplement or repeal earlier legislative provisions, whether they result from an act passed by Parliament or from an act adopted by referendum"),
               ("m23_10", 10, "elle ne porte pas, au sens de l'article 11 de la Constitution, sur une « réforme » relative à la politique sociale",
                "it does not relate, within the meaning of Article 11 of the Constitution, to a \"reform\" concerning social policy")],
    "2023-5": [("m235_8", 8, "l'interdiction de fixer l'âge légal de départ à la retraite au-delà de soixante-deux ans n'emporte donc pas de changement de l'état du droit",
                "the prohibition on setting the legal retirement age above sixty-two therefore does not change the state of the law"),
               ("m235_10", 10, "Elle a ainsi pour seul effet d'abonder le budget d'une branche de la sécurité sociale",
                "Its sole effect is thus to increase the budget of one branch of social security"),
               ("m235_11", 11, "la proposition de loi ne porte pas, au sens de l'article 11 de la Constitution, sur une réforme relative à la politique sociale",
                "the bill does not relate, within the meaning of Article 11 of the Constitution, to a reform concerning social policy")],
    "2024-6": [("m24_7", 7, "elle porte, au sens de l'article 11 de la Constitution, sur une réforme relative à la politique sociale de la nation",
                "it relates, within the meaning of Article 11 of the Constitution, to a reform concerning the social policy of the nation"),
               ("m24_13", 13, "les dispositions de l'article 1er portent une atteinte disproportionnée à ces exigences. Elles sont donc contraires à la Constitution",
                "the provisions of Article 1 disproportionately infringe these requirements. They are therefore contrary to the Constitution")],
    "2026-7": [("m26_7", 7, "le constituant a entendu exclure les questions de société des objets mentionnés au premier alinéa de l'article 11 de la Constitution",
                "the framers of the constitutional amendment intended to exclude questions of society from the subjects listed in the first paragraph of Article 11 of the Constitution"),
               ("m26_9", 9, "elle ne porte ni sur la politique sociale de la nation et les services publics qui y concourent, ni sur aucun des autres objets mentionnés au premier alinéa de l'article 11 de la Constitution",
                "it relates neither to the social policy of the nation and the public services contributing to it, nor to any of the other subjects listed in the first paragraph of Article 11 of the Constitution"),
               ("m26_11", 11, "n'emporte pas de changement de l'état du droit", "does not change the state of the law"),
               ("m26_13", 13, "la proposition de loi ne porte pas non plus sur une « réforme » au sens de l'article 11 de la Constitution",
                "nor does the bill relate to a \"reform\" within the meaning of Article 11 of the Constitution")],
}
CONDITION = {"2": ("2° de l'art. 45-2, objet de l'article 11", "art. 45-2, 2°: subject of article 11"),
             "3": ("3° de l'art. 45-2, disposition contraire à la Constitution", "art. 45-2, 3°: provision contrary to the Constitution")}


def motifs_groupes(n: str, lang: str) -> str:
    """Motifs d'une décision, regroupés par considérant, dans l'ordre de la décision (cellule du tableau)."""
    par = {}
    for _, k, f, tr in MOTIFS[n]:
        par.setdefault(k, []).append((f, tr))
    if lang == "fr":
        return " ".join("Consid. %d : %s." % (k, " ; ".join("« %s »" % f for f, _ in v)) for k, v in par.items())
    return " ".join("Para. %d: %s." % (k, "; ".join("« %s » (our translation: \"%s\")" % (f, tr) for f, tr in v))
                    for k, v in par.items())
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
            "art88_5": sum(1 for l in vals if l["date_scrutin"] >= DEBUT_88_5 and "adhésion" in OBJET[l["date_scrutin"]][0].lower()),
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
    if r["art88_5"] != 0:
        raise Arret("R5 : « aucun scrutin sur le fondement de l'art. 88-5 » démenti")
    if r["cond2"] + r["cond3"] != r["S"] - r["C"]:
        raise Arret("R5 : chaque non-conformité relève du 2° ou du 3°, la somme ne tombe pas juste")


# ------------------------------------------------------------------ affichage
def affichage(R, S, r) -> tuple[dict, dict]:
    conf = next(s for s in S.values() if s["solution"] == "Conformité")
    d = {l["date_scrutin"]: l for l in R}
    part = lambda l: 100 * l["votants"] / l["inscrits"]  # noqa: E731
    pct = lambda l, k: 100 * l[k] / l["exprimes"]  # noqa: E731
    out = {}
    for lang, nb, dt in (("fr", fr, date_fr), ("en", en, date_en)):
        L = lambda n: lg.lettres(n, lang)  # noqa: E731
        A = {"N": L(r["N"]), "N_chiffre": str(r["N"]), "A": L(r["A"]), "R": L(r["R"]),
             "dernier": dt(r["dernier"]), "arrete": dt(ARRETE), "annees_depuis": str(int(ARRETE[:4]) - int(r["dernier"][:4])),
             "S": L(r["S"]), "C": ("une" if r["C"] == 1 else L(r["C"])) if lang == "fr" else L(r["C"]),
             "cond2": L(r["cond2"]), "cond3": L(r["cond3"]),
             "soutiens": nb(conf["soutiens"]), "seuil": nb(conf["seuil"]),
             "part_seuil": nb(100 * conf["soutiens"] / conf["seuil"], 1),
             "rip_conf_date": dt(conf["date"]), "rip_depuis": "2015",
             "part_2005": nb(part(d["2005-05-29"]), 1), "non_2005": nb(pct(d["2005-05-29"], "non"), 2),
             "part_2000": nb(part(d["2000-09-24"]), 1), "part_1988": nb(part(d["1988-11-06"]), 1),
             "oui_2000": nb(pct(d["2000-09-24"], "oui"), 2),
             "part_max": nb(max(part(l) for l in R), 1), "part_min": nb(min(part(l) for l in R), 1),
             "oui_1992": nb(pct(d["1992-09-20"], "oui"), 2), "non_1969": nb(pct(d["1969-04-27"], "non"), 2),
             "depots_sans_saisine": L(len(DEPOTS_SANS_SAISINE)),
             "depots_sans_saisine_maj": L(len(DEPOTS_SANS_SAISINE)).capitalize(),
             "depots_auteurs": lg.enumere([L(x["auteurs"]) for x in DEPOTS_SANS_SAISINE], lang),
             "n_loi": L(r["N"] - r["art89"]).capitalize(),
             "n_rev": ("un seul" if lang == "fr" else "only one") if r["art89"] == 1 else L(r["art89"]),
             "part_min_an": min(R, key=part)["date_scrutin"][:4], "part_max_an": max(R, key=part)["date_scrutin"][:4],
             "non_conformes": L(r["S"] - r["C"]), "cond2_maj": L(r["cond2"]).capitalize(), "cond3_maj": L(r["cond3"]).capitalize(),
             "cit_2007_560": CIT_2007_560[0], "cit_elysee": CIT_ELYSEE, "cit_clause_2004": CLAUSE_2004_PAGE,
             "cit_congres_2008": CONGRES_2008_PAGE,
             "declaration_2020": dt(DECLARATION_2020)}
        for cle, iso, _ in ETAPES_2021:
            A["e2021_" + cle] = dt(iso)
        for k, (n, f, e) in CIT.items():
            # page française : texte français ; page anglaise : traduction du Conseil (Constitution) ou texte français
            # suivi de notre traduction (clé _tr)
            if n in CONSTITUTION:
                A["cit_" + k] = (f or "") if lang == "fr" else e
            else:
                A["cit_" + k] = f
                A["cit_" + k + "_tr"] = e
        A["cit_art88_5_2004"] = CLAUSE_2004 if lang == "fr" else CIT["art88_5_2004"][2]
        for num, lignes in MOTIFS.items():
            for cle, k, f, t in lignes:
                A[cle] = f
                A[cle + "_tr"] = t
                A[cle + "_n"] = str(k)
        out[lang] = A
    return out["fr"], out["en"]


def tableaux(R, S) -> tuple[dict, dict]:
    t, te = {}, {}
    lignes, lignes_en = [], []
    for l in R:
        _, _, loi, _ = TEMOIN_JO[l["date_scrutin"]]
        o, oe = OBJET[l["date_scrutin"]]
        part = 100 * l["votants"] / l["inscrits"]
        oui = 100 * l["oui"] / l["exprimes"]
        art = "89" if l["nature"] == "révision de la Constitution" else "11"
        lignes.append([date_fr(l["date_scrutin"]), o, art, fr(l["inscrits"]), fr(part, 1) + "\u00a0%", fr(oui, 2) + "\u00a0%",
                       ("Adopté (loi n°\u00a0%s)" % loi) if l["oui"] > l["non"] else "Rejeté"])
        lignes_en.append([date_en(l["date_scrutin"]), oe, art, en(l["inscrits"]), en(part, 1) + "%", en(oui, 2) + "%",
                          ("Adopted (Act No. %s)" % loi) if l["oui"] > l["non"] else "Rejected"])
    t["registre"] = {"entetes": ["Scrutin", "Objet", "Article", "Inscrits", "Participation", "Oui (exprimés)", "Issue"], "lignes": lignes}
    te["registre"] = {"entetes": ["Vote", "Subject", "Article", "Registered voters", "Turnout", "Yes (valid votes)", "Outcome"], "lignes": lignes_en}
    lr, lre = [], []
    for n, s in S.items():
        o, oe = OBJET_RIP[n]
        if s["solution"] == "Conformité":
            issue = "Conforme ; %s soutiens pour %s requis" % (fr(s["soutiens"]), fr(s["seuil"]))
            issue_en = "Met the statutory conditions; %s signatures of support for %s required" % (en(s["soutiens"]), en(s["seuil"]))
            motif = motif_en = "—"
        else:
            issue = "Non conforme : " + " ; ".join(CONDITION[c][0] for c in s["condition"])
            issue_en = "Did not meet the statutory conditions: " + "; ".join(CONDITION[c][1] for c in s["condition"])
            motif, motif_en = motifs_groupes(n, "fr"), motifs_groupes(n, "en")
        lr.append([date_fr(s["date"]), "%s RIP" % n, o, issue, motif])
        lre.append([date_en(s["date"]), "%s RIP" % n, oe, issue_en, motif_en])
    t["rip"] = {"entetes": ["Décision", "Numéro", "Proposition de loi", "Solution", "Motifs cités (considérants)"], "lignes": lr}
    te["rip"] = {"entetes": ["Decision", "Number", "Private Members' Bill", "Outcome", "Grounds quoted (paragraphs)"], "lignes": lre}
    return t, te


# ------------------------------------------------------------------ figures
W = 720
BLEU, GRIS, GRIS_CLAIR = "#184f95", "#8a8f98", "#c9cdd3"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCES_M = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
              "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
WM, FS_MIN = 300, 13.5
LANG = "fr"


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None, cls=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    c = ' class="%s"' % cls if cls else ""
    return '<text%s x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>' % (c, x, y, size, fill, anchor, w, esc(s))


def cadre(H, ident, titre, sous, desc):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H + 48, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def pied(e, y0, source, note) -> str:
    return pied_figure.pied(e, y0, W, [(source, INK2, "pied-source"), (note, INK2, "pied-note"),
                                       (LICENCES[LANG], MUTED, "pied-licence")], GRID)


def pct_oui(l) -> float:
    return 100 * l["oui"] / l["exprimes"]


def etiquette_scrutin(l, lang) -> str:
    a = l["date_scrutin"][:4]
    if a == "1962":
        m = int(l["date_scrutin"][5:7])
        return "%s (%s)" % (a, (MOIS_FR if lang == "fr" else MOIS_EN)[m][:3].lower() + ".")
    return a


def liste_oui(R, lang) -> str:
    nb = fr if lang == "fr" else en
    sep, u = ("\u00a0%", " ; ") if lang == "fr" else ("%", "; ")
    return u.join("%s : %s%s" % (etiquette_scrutin(l, lang), nb(pct_oui(l), 0), sep) if lang == "fr"
                  else "%s: %s%s" % (etiquette_scrutin(l, lang), nb(pct_oui(l), 0), sep) for l in R)


T = {
    "fr": {"t1": "Les référendums nationaux depuis 1958", "s1": "date du scrutin et part des « oui » parmi les suffrages exprimés, arrêté au {arrete}",
           "d1": "Frise de 1958 à 2026 portant {N} référendums nationaux : {A} adoptés et {R} rejetés (1969 et 2005) ; aucun scrutin depuis le {dernier}. Part des oui parmi les exprimés : {liste}.",
           "src1": "Conseil constitutionnel, proclamations des résultats (stock CONSTIT de la DILA, arrêté au 05/10/2026) ; Journal officiel",
           "note1": "Référendums nationaux des art. 11 et 89 seulement (aucun n'a eu lieu au titre de l'art. 88-5) ; hors scrutin du 28/09/1958 et consultations locales.",
           "adopte": "adopté", "rejete": "rejeté", "aucun": "aucun référendum depuis {annees_depuis} ans",
           "moitie": "50 % des exprimés",
           "t2": "Le référendum d'initiative partagée, de 2015 au {arrete}", "s2": "propositions de loi soumises au Conseil constitutionnel, et ce qu'elles sont devenues",
           "d2": "Saisines du Conseil constitutionnel : {S_chiffre} ; jugées conformes : {C_chiffre} ; soutien d'un dixième des inscrits réuni : 0 ; soumises au référendum : 0. La proposition conforme a recueilli {soutiens} soutiens pour {seuil} requis, soit {part_seuil} % du seuil.",
           "src2": "Conseil constitutionnel, décisions « RIP » (stock CONSTIT, arrêté au 05/10/2026) ; Constitution, art. 11",
           "note2": "{depots_maj} autres propositions déposées « en application de l'article 11 » (Sénat, Assemblée) n'ont fait l'objet d'aucune décision.",
           "e1": "Saisines du Conseil", "e2": "Jugées conformes", "e3": "Soutien d'un dixième des inscrits réuni", "e4": "Soumises au référendum",
           "sout": "Soutiens recueillis : {soutiens}", "seuil": "Seuil : {seuil} (un dixième des inscrits)",
           "part": "{part_seuil} % du seuil",
           "t1m": "Les référendums nationaux depuis 1958", "s1m": "part des « oui » parmi les exprimés",
           "t2m": "Le référendum d'initiative partagée, 2015-{an_arrete}", "dernier_m": "Aucun scrutin depuis le {dernier}"},
    "en": {"t1": "National referendums in France since 1958", "s1": "date of the vote and share of 'yes' among valid votes, as at {arrete}",
           "d1": "Timeline from 1958 to 2026 with {N} national referendums: {A} adopted and {R} rejected (1969 and 2005); no vote since {dernier}. Share of yes among valid votes: {liste}.",
           "src1": "Conseil constitutionnel, proclamations of results (DILA CONSTIT database, as at 5 Oct. 2026); Journal officiel",
           "note1": "National referendums under articles 11 and 89 only (none was held under article 88-5); excludes the vote of 28 Sept. 1958 and local consultations.",
           "adopte": "adopted", "rejete": "rejected", "aucun": "no referendum for {annees_depuis} years",
           "moitie": "50% of valid votes",
           "t2": "The shared-initiative referendum, 2015 to {arrete}", "s2": "Private Members' Bills referred to the Conseil constitutionnel, and what became of them",
           "d2": "Referrals to the Conseil constitutionnel: {S_chiffre}; meeting the statutory conditions: {C_chiffre}; support of one tenth of registered voters reached: 0; put to a referendum: 0. The bill that met the conditions collected {soutiens} signatures of support for {seuil} required, {part_seuil}% of the threshold.",
           "src2": "Conseil constitutionnel, 'RIP' decisions (DILA CONSTIT database, as at 5 Oct. 2026); Constitution, art. 11",
           "note2": "{depots_maj} other bills tabled 'under article 11' (Senate, National Assembly) gave rise to no decision.",
           "e1": "Referrals", "e2": "Met the statutory conditions", "e3": "One tenth of voters' support reached", "e4": "Put to a referendum",
           "sout": "Signatures collected: {soutiens}", "seuil": "Threshold: {seuil} (one tenth of registered voters)",
           "part": "{part_seuil}% of the threshold",
           "t1m": "National referendums in France since 1958", "s1m": "share of 'yes' among valid votes",
           "t2m": "The shared-initiative referendum, 2015-{an_arrete}", "dernier_m": "No vote since {dernier}"},
}


def vals_fig(A, R, r):
    return dict(A, liste=liste_oui(R, LANG), S_chiffre=str(r["S"]), C_chiffre=str(r["C"]), depots_maj=A["depots_sans_saisine_maj"],
                an_arrete=ARRETE[:4])


def fig_registre(R, r, A):
    H = 262
    L = T[LANG]
    V = vals_fig(A, R, r)
    e = cadre(H, "rr", L["t1"], L["s1"].format(**V), L["d1"].format(**V))
    x0, x1 = 20, W - 20
    a0, a1 = 1958, int(ARRETE[:4]) + 1
    X = lambda y: x0 + (y - a0) / (a1 - a0) * (x1 - x0)  # noqa: E731
    yb, hmax = 230, 150  # base et hauteur pour 100 % de oui
    Y = lambda p: yb - p / 100 * hmax  # noqa: E731
    e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (x0, yb, x1, yb, INK2))
    e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-dasharray="3 3"/>' % (x0, Y(50), x1, Y(50), GRIS))
    e.append(txt(X(1976), Y(50) - 4, L["moitie"], 10, MUTED, "start"))  # zone sans scrutin (1973-1987)
    for an in range(1960, a1, 10):
        e.append(txt(X(an), yb + 16, str(an), 10, MUTED, "middle"))
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(an), yb, X(an), yb + 4, INK2))
    dernier = max(l["date_scrutin"] for l in R)
    xd = X(int(dernier[:4]) + (int(dernier[5:7]) - 0.5) / 12)
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity="0.35"/>' % (xd + 6, yb - hmax, x1 - xd - 6, hmax, GRID))
    e.append(txt((xd + x1) / 2, yb - hmax + 22, L["aucun"].format(**V), 11, INK2, "middle", "600"))
    prec = None
    for l in R:
        an = int(l["date_scrutin"][:4]) + (int(l["date_scrutin"][5:7]) - 0.5) / 12
        p = pct_oui(l)
        x = X(an)
        ad = l["oui"] > l["non"]
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="5"/>' % (x, yb, x, Y(p), BLEU if ad else GRIS))
        e.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, Y(p), BLEU if ad else "#ffffff", BLEU if ad else INK2))
        lab = (fr(p, 0) + "\u00a0%") if LANG == "fr" else en(p, 0) + "%"
        # deux scrutins à moins d'un an (1962) : l'étiquette du second passe à droite de sa tige
        proche = prec is not None and an - prec < 1
        e.append(txt(x + (12 if proche else 0), Y(p) + (4 if proche else -10), lab, 10, INK if ad else INK2,
                     "start" if proche else "middle", "600"))
        prec = an
    e.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x0 + 4, 58, BLEU))
    e.append(txt(x0 + 14, 62, L["adopte"], 10, INK2))
    e.append('<circle cx="%d" cy="%d" r="5" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (x0 + 84, 58, INK2))
    e.append(txt(x0 + 94, 62, L["rejete"], 10, INK2))
    return pied(e, H + 2, L["src1"], L["note1"].format(**V))


def fig_rip(S, r, A, R):
    H = 286
    L = T[LANG]
    V = vals_fig(A, R, r)
    e = cadre(H, "rp", L["t2"].format(**V), L["s2"], L["d2"].format(**V))
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
    e.append(txt(x0 + ws + 6, yy + 10, L["part"].format(**V), 10, INK2))
    e.append(txt(x0, yy + 28, L["sout"].format(**V), 10, INK, "start", "600"))
    e.append(txt(x0, yy + 42, L["seuil"].format(**V), 10, INK2))
    return pied(e, H + 2, L["src2"], L["note2"].format(**V))


# ------------------------------------------------------------------ figures téléphone (phase B, 12/10/2026)
# Composées pour 300 px de large, jamais rétrécies : police >= FS_MIN ; chaque valeur dessinée (classe « val ») doit
# figurer dans la description de la version détaillée (parite_mobile). Patron : scripts/update_promesses_delais.py.
def tete_m(fid, titre, desc):
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (WM, fid, fid, FONT),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (fid, esc(titre), fid, esc(desc)),
         '<rect width="%d" height="0" fill="#ffffff"/>' % WM]
    lignes = pied_figure.coupe(titre, 30)
    for k, ligne in enumerate(lignes):
        e.append(txt(0, 20 + 22 * k, ligne, 17, INK, weight="600"))
    return e, 20 + 22 * len(lignes)


def finir_m(e, y0, source, note):
    return pied_figure.pied_mobile(e, y0, [(source, INK2, "pied-source"), (note, INK2, "pied-note"),
                                           (LICENCES_M[LANG], MUTED, "pied-licence")], GRID)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg).group(1))


def fig_registre_m(R, r, A, svg_d):
    L = T[LANG]
    V = vals_fig(A, R, r)
    e, y = tete_m("rrm", L["t1m"], desc_de(svg_d))
    e.append(txt(0, y + 6, L["s1m"], FS_MIN, INK2))
    y += 22
    X0, X1 = 92, WM - 50
    xm = X0 + (X1 - X0) / 2
    top = y + 8
    for l in R:
        y += 26
        p = pct_oui(l)
        ad = l["oui"] > l["non"]
        e.append(txt(0, y + 14, etiquette_scrutin(l, LANG), FS_MIN, INK2))
        w = (X1 - X0) * p / 100
        if ad:
            e.append('<rect x="%d" y="%d" width="%.1f" height="18" fill="%s"/>' % (X0, y, w, BLEU))
        else:
            e.append('<rect x="%d" y="%d" width="%.1f" height="18" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (X0, y + 1, w, INK2))
        lab = (fr(p, 0) + "\u00a0%") if LANG == "fr" else en(p, 0) + "%"
        e.append(txt(X0 + w + 6, y + 14, lab, FS_MIN, INK if ad else INK2, "start", "600", "val"))
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (xm, top, xm, y + 22, GRIS))
    y += 46
    e.append('<rect x="0" y="%d" width="14" height="14" fill="%s"/>' % (y - 12, BLEU))
    e.append(txt(20, y, L["adopte"], FS_MIN, INK2))
    e.append('<rect x="110" y="%d" width="14" height="14" fill="#ffffff" stroke="%s" stroke-width="1.5"/>' % (y - 12, INK2))
    e.append(txt(130, y, L["rejete"], FS_MIN, INK2))
    y += 22
    e.append(txt(0, y, L["moitie"] + " : - - -" if LANG == "fr" else L["moitie"] + ": - - -", FS_MIN, MUTED))
    y += 22
    e.append(txt(0, y, L["dernier_m"].format(**V), FS_MIN, INK, weight="600"))
    return finir_m(e, y + 14, L["src1"], L["note1"].format(**V))


def fig_rip_m(S, r, A, R, svg_d):
    L = T[LANG]
    V = vals_fig(A, R, r)
    e, y = tete_m("rpm", L["t2m"].format(**V), desc_de(svg_d))
    etapes = [(L["e1"], r["S"]), (L["e2"], r["C"]), (L["e3"], r["reunis"]), (L["e4"], 0)]
    for nom, v in etapes:
        for ligne in pied_figure.coupe(nom, 36):
            y += 18
            e.append(txt(0, y, ligne, FS_MIN, INK2))
        y += 6
        w = (WM - 40) * v / max(1, r["S"])
        if v:
            e.append('<rect x="0" y="%d" width="%.1f" height="20" fill="%s"/>' % (y, w, BLEU))
        else:
            e.append('<line x1="1" y1="%d" x2="1" y2="%d" stroke="%s" stroke-width="2"/>' % (y, y + 20, INK2))
        e.append(txt(w + 8, y + 15, str(v), 15, INK, "start", "600", "val"))
        y += 24
    conf = next(s for s in S.values() if s["solution"] == "Conformité")
    y += 18
    e.append(txt(0, y, "2019-1 RIP", FS_MIN, INK, weight="600"))
    y += 8
    e.append('<rect x="0" y="%d" width="%d" height="14" fill="none" stroke="%s"/>' % (y, WM - 2, INK2))
    e.append('<rect x="0" y="%d" width="%.1f" height="14" fill="%s"/>' % (y, (WM - 2) * conf["soutiens"] / conf["seuil"], GRIS))
    y += 14
    for ligne in (L["sout"].format(**V), L["seuil"].format(**V), L["part"].format(**V)):
        for morceau in pied_figure.coupe(ligne, 36):
            y += 19
            e.append(txt(0, y, morceau, FS_MIN, INK2, cls="val"))
    return finir_m(e, y + 14, L["src2"], L["note2"].format(**V))


NUM = re.compile(r"(?<!\d)\d+(?:[ \u00a0\u202f,]\d{3})*(?:[.,]\d+)?(?!\d|er\b|re\b|e\b|st\b|nd\b|rd\b|th\b)")


def _nums(s):
    return {re.sub(r"[ \u00a0\u202f,]", "", x).replace(".", ",") for x in NUM.findall(s)}


def parite_mobile(figs):
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
    "fr": {"registre": "Du 4 octobre 1958 au {arrete}, {N} référendums nationaux ont été organisés ; {A} ont adopté le texte soumis, {R} l'ont rejeté ; le dernier date du {dernier}.",
           "rip": "De 2015 au {arrete}, le Conseil constitutionnel a été saisi de {S} propositions de loi au titre de l'article 11 ; {C} a été jugée conforme et a recueilli {part_seuil} % des soutiens requis ; aucune n'a été soumise au référendum."},
    "en": {"registre": "From 4 October 1958 to {arrete}, {N} national referendums were held; the proposed text was approved in {A} and rejected in {R}; the last one took place on {dernier}.",
           "rip": "From 2015 to {arrete}, the Conseil constitutionnel received {S} Private Members' Bills under article 11; {C} was found to meet the statutory conditions and collected {part_seuil}% of the required signatures; none was put to a referendum."},
}


def fiches(figs, A, E):
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", E)):
        out = []
        for ident, fichier in (("registre", "referendum-registre"), ("rip", "referendum-rip")):
            svg = figs[fichier + suf + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            src, note, lic = (pied_figure.lire(svg, c) for c in ("pied-source", "pied-note", "pied-licence"))
            if not src or not note or lic != LICENCES[lang]:
                raise Arret("fiche %s%s : pied illisible" % (fichier, suf))
            out.append(dict(id=ident, fichier=fichier + suf, titre=titre, montre=MONTRE[lang][ident].format(**AA),
                            source=src, precaution=note))
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
        src = "Conseil constitutionnel, décision %s RIP" % n
        w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "solution", s["solution"], src])
        for c in s["condition"]:
            w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "condition_art_45_2", c + "°", src])
        for _, k, f, _ in MOTIFS.get(n, []):
            w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "motif_considerant_%d" % k, f, src])
        if s["soutiens"] is not None:
            w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "soutiens", s["soutiens"], "décision %s RIP" % s.get("declaration")])
            w.writerow(["rip", n, s["date"], OBJET_RIP[n][0], "11 al. 3", "seuil", s["seuil"], "décision %s RIP" % s.get("declaration")])
    for d in DEPOTS_SANS_SAISINE:
        src = "Sénat, base Dosleg" if d["chambre"] == "Sénat" else "Assemblée nationale, données ouvertes"
        w.writerow(["depot_art11_sans_saisine", "%s %s %s" % (d["chambre"], d["legislature"], d["numero"]), d["date"], d["objet"],
                    "11 al. 3", "decision_du_conseil", "aucune", src])
        w.writerow(["depot_art11_sans_saisine", "%s %s %s" % (d["chambre"], d["legislature"], d["numero"]), d["date"], d["objet"],
                    "11 al. 3", "auteurs", d["auteurs"], "texte déposé"])
    return buf.getvalue()


def autotest(R, S, textes, pieces):
    """Chaque mutation doit être arrêtée par SA garde (préfixe) ; une autre garde qui l'arrêterait la fait échouer."""
    out = []
    mut_motifs = copy.deepcopy(MOTIFS)
    mut_motifs["2026-7"][0] = ("m26_7", 9) + mut_motifs["2026-7"][0][2:]     # bon motif, mauvais considérant
    mut_cit = dict(CIT, art88_5_2=("88-5", CIT["art88_5_2"][1].replace("trois cinquièmes", "majorité absolue"), CIT["art88_5_2"][2]))
    mut_pieces = {k: list(v) for k, v in PIECES_CITEES.items()}
    mut_pieces["elysee_2020-06-29_convention_climat.html"][1] = CIT_ELYSEE.replace("après le vote des chambres", "sans le vote des chambres")
    mut_etapes = ETAPES_2021[:-1]                                                  # la page tairait l'étape du 5/07/2021
    mut_depots = [dict(d, auteurs=2) if d["numero"] == "5203" else d for d in DEPOTS_SANS_SAISINE]
    essais = [("proclamation retirée", lambda: (gardes(R[1:], S), "R1")),
              ("oui/non permutés (1969)", lambda: (gardes([dict(l, oui=l["non"], non=l["oui"]) if l["date_scrutin"] == "1969-04-27" else l for l in R], S), "R2")),
              ("voix ajoutée", lambda: (gardes([dict(l, oui=l["oui"] + 1) if l["date_scrutin"] == "1961-01-08" else l for l in R], S), "R1")),
              ("citation altérée", lambda: (verifier_citations(dict(textes, **{"11": textes["11"].replace("un dixième", "un cinquième")}), MOTIFS, S), "R4")),
              ("art. 88-5 : trois cinquièmes -> majorité absolue", lambda: (verifier_citations(textes, MOTIFS, S, mut_cit), "R4")),
              ("motif 2026-7 sous le mauvais considérant", lambda: (verifier_citations(textes, mut_motifs, S), "R4")),
              ("soutiens au seuil", lambda: (phrases(resultat(R, {k: (dict(v, soutiens=v["seuil"]) if v["solution"] == "Conformité" else v) for k, v in S.items()})), "R5")),
              ("scrutin d'adhésion après 2005", lambda: (phrases(dict(resultat(R, S), art88_5=1)), "R5")),
              ("déclaration de l'Élysée altérée", lambda: (verifier_pieces(pieces, mut_pieces), "R8")),
              ("dernière étape du dossier 2021 omise", lambda: (verifier_pieces(pieces, None, mut_etapes), "R8")),
              ("signataires du n° 5203 : 1 -> 2", lambda: (verifier_signataires(pieces, mut_depots), "R9"))]
    for nom, f in essais:
        try:
            f()
            raise Arret("mutation %s : aucune garde n'a mordu, contrôle ABSENT" % nom)
        except Arret as e:
            pref = {"proclamation retirée": "R1", "voix ajoutée": "R1", "oui/non permutés (1969)": "R2",
                    "soutiens au seuil": "R5", "scrutin d'adhésion après 2005": "R5",
                    "déclaration de l'Élysée altérée": "R8", "dernière étape du dossier 2021 omise": "R8",
                    "signataires du n° 5203 : 1 -> 2": "R9"}.get(nom, "R4")
            if not str(e).startswith(pref):
                raise Arret("mutation %s : arrêtée par une autre garde que %s (%s)" % (nom, pref, str(e)[:60]))
            out.append("%s -> %s" % (nom, str(e)[:90]))
    # témoin de pièce : un octet ajouté à une copie en mémoire doit faire refuser la lecture
    try:
        lire_pieces("senat_ppl17-459.html")
        raise Arret("mutation pièce altérée : empreinte acceptée, contrôle ABSENT")
    except Arret as e:
        if not str(e).startswith("R8"):
            raise
        out.append("pièce altérée d'un octet -> %s" % str(e)[:90])
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


TEMOIN_RIP = PRO / "06_PROMOTION" / "RECHERCHE_DOSSIER_PROMESSES_2026-10-05" / "test_decisif" / "referendum" / "registre_rip.json"


def verifier_depots(depots=None) -> str:
    """R6 (07/10/2026) : la liste des dépôts « article 11 » sans décision est celle qu'a trouvée le témoin
    (test_r_e2.py : Assemblée XIV à XVII, Dosleg type « refe »). Un écart dans un sens ou dans l'autre arrête."""
    depots = DEPOTS_SANS_SAISINE if depots is None else depots
    if not TEMOIN_RIP.exists():
        raise Arret("R6 : sortie du témoin absente (%s) : lancer test_r_e2.py" % TEMOIN_RIP)
    t = json.loads(TEMOIN_RIP.read_text(encoding="utf-8"))
    vus = {("AN", re.sub(r"\D", "", d["uid"][-5:]).lstrip("0")) for d in t.get("depots_sans_saisine", [])}
    vus |= {("Sénat", re.search(r"-(\d+)$", k).group(1)) for k in t.get("depots_senat_sans_decision", {})}
    liste = {(d["chambre"], d["numero"]) for d in depots}
    if liste != vus:
        raise Arret("R6 : dépôts sans saisine, liste %s contre témoin %s" % (sorted(liste), sorted(vus)))
    return "R6 : %d dépôts sans saisine, identiques au témoin (Assemblée et Sénat)" % len(liste)


def _main() -> int:
    check = "--check" in sys.argv[1:]
    par_id = charger_constit()
    R, S = registre(par_id), rip(par_id)
    textes = {n: article_fr(n) for n in ARTICLES}
    pieces = lire_pieces()
    g = gardes(R, S)
    g.append(verifier_depots())
    try:
        verifier_depots(DEPOTS_SANS_SAISINE[1:])
        raise RuntimeError("R6 : la mutation « dépôt retiré » n'a pas mordu")
    except Arret:
        log("autotest : la mutation a mordu : dépôt retiré -> R6")
    g += verifier_citations(textes, MOTIFS, S)
    g.append(verifier_2007_560(par_id))
    g.append(verifier_62_20(par_id))
    try:
        verifier_62_20(par_id, DEC_62_20[:2] + ("Conformité",) + DEC_62_20[3:])
        raise RuntimeError("R7 : la mutation « solution changée » n'a pas mordu")
    except Arret:
        log("autotest : la mutation a mordu : solution de 62-20 changée -> R7")
    g.append(verifier_pieces(pieces))
    g.append(verifier_signataires(pieces))
    r = resultat(R, S)
    phrases(r)
    g.append("R5 : phrases recalculées (N=%d, A=%d, R=%d, S=%d, C=%d, soutiens réunis=%d, art. 88-5=%d)"
             % (r["N"], r["A"], r["R"], r["S"], r["C"], r["reunis"], r["art88_5"]))
    for m in autotest(R, S, textes, pieces):
        log("autotest : la mutation a mordu : " + m)
    A, E = affichage(R, S, r)
    if set(A) != set(E):
        raise Arret("blocs affichage et affichage_en : clés différentes (%s)" % sorted(set(A) ^ set(E)))
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", E)):
        figs["referendum-registre%s.svg" % suf] = fig_registre(R, r, AA)
        figs["referendum-rip%s.svg" % suf] = fig_rip(S, r, AA, R)
        figs["referendum-registre%s-m.svg" % suf] = fig_registre_m(R, r, AA, figs["referendum-registre%s.svg" % suf])
        figs["referendum-rip%s-m.svg" % suf] = fig_rip_m(S, r, AA, R, figs["referendum-rip%s.svg" % suf])
    LANG = "fr"
    nv = parite_mobile(figs)
    g.append("parite des 4 figures telephone (%d valeurs dessinees retrouvees dans la version detaillee)" % nv)
    fi = fiches(figs, A, E)
    t, te = tableaux(R, S)
    csvt = csv_texte(R, S)
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    try:
        import cairosvg
    except ImportError:
        raise Arret("cairosvg absent : SVG et PNG ensemble ou pas du tout")
    payload = {
        "releve_le": ARRETE,
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Conseil constitutionnel (DILA, CONSTIT), Journal officiel, Assemblée nationale, Sénat",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve, prolongement R (R-E1, R-E2) ; refonte, phase B du 12/10/2026",
                 "arrete": ARRETE, "textes": {n: {"legiarti": v[0], "archive": v[1]} for n, v in ARTICLES.items()},
                 "pieces_hors_legifrance": {n: {"sha256": h, "passages": PIECES_CITEES.get(n, [])} for n, h in sommes().items()},
                 "dossier_pjl20_449": [{"etape": c, "date": iso, "passage": p} for c, iso, p in ETAPES_2021],
                 "temoin_jo": TEMOIN_JO, "depots_sans_saisine": DEPOTS_SANS_SAISINE,
                 "hors_champ": "référendum du 28/09/1958 (antérieur au Conseil constitutionnel) ; consultations locales (art. 72-1, 72-4, 73, 76, 77)"},
        "gardes": g, "calcul": r,
        "registre": [{k: v for k, v in l.items()} for l in R],
        "rip": {n: {k: v for k, v in s.items() if k != "texte"} for n, s in S.items()},
        "motifs_cites": {n: [{"considerant": k, "citation": f, "traduction_en": tr} for _, k, f, tr in l] for n, l in MOTIFS.items()},
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
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")),
                         output_width=1440 if not n.endswith("-m.svg") else 600, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_referendum.json, static/promesses_referendum.{json,csv}, data/figures_referendum.json, 8 figures SVG + PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
