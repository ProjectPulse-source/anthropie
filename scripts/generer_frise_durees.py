# -*- coding: utf-8 -*-
"""generer_frise_durees.py -- frise des durées d'inscription, page /combien-de-temps-une-erreur-reste-inscrite/ (04/11/2026).

Ce que montre la figure : de six mois à quarante ans, les durées pendant lesquelles une trace reste inscrite, registre par
registre, sur une échelle logarithmique (seule échelle qui lise à la fois six mois et quarante ans). C'est la première
conclusion de la page, « la durée d'une trace ne dit pas la gravité de l'erreur ».

Source : le TABLEAU DE LA PAGE, établi d'après les textes qu'elle cite. Ce que le script vérifie, et rien de plus :
  1. chaque fragment de VERIF figure mot pour mot dans la cellule « Délai » de son registre ;
  2. chaque valeur dessinée se lit dans ces fragments : « 6 mois » pour 0,5 ; le nombre lui-même pour une durée en ans ;
     pour un point creux (récidive), la moitié de la valeur et le mot « doublés ».
  3. les points pleins sont exactement les durées des fragments (aucune omise, aucune ajoutée) ; les points creux,
     exactement leur double quand le tableau dit « doublés » ;
  4. chaque nombre d'un détail affiché se lit dans la ligne du tableau ;
  5. toute durée de la cellule « Délai » est dessinée, ou déclarée « non figurée » dans la note (NON_FIGURES) ;
  6. chaque couple « A au lieu de B » d'un détail vérifie A = 2 B, B point plein et A point creux de sa ligne.
Si l'un manque, arrêt sans rien écrire (témoins : --mutation=texte, marque, omission, detail, ordinal, nonfigure, couple). Le texte alternatif de
l'image, dans la page, n'est pas contrôlé par ce script (relu à la main).

Marques : un POINT par durée distincte (jamais un trait, qui ferait lire une plage) ; plein pour le délai, creux pour le
délai doublé en récidive. Une seule couleur : le délai prend fin seul partout ; seul l'effacement anticipé passe par la
personne ou par un tiers, ce que la note dit.

Usage : python scripts/generer_frise_durees.py [--check] [--mutation=texte|marque|omission|detail|ordinal|nonfigure|couple]
Sorties : static/img/durees-inscription{,-m}.svg + .png ; contrôles : pied_figure.controler_page, pied_figure.parite.
"""
from __future__ import annotations

import html
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure as PF  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "content" / "combien-de-temps-une-erreur-reste-inscrite" / "_index.md"
OUT = ROOT / "static" / "img"
NOM = "durees-inscription"
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
ENCRE, GRIS, GRILLE, BLEU, FILET = "#1a1a1f", "#55524f", "#e6e3dc", "#184f95", "#c9c6bd"
DETAIL = "#45423e"   # détails des lignes : teinte propre, que le contrôle de parité lit (le pied reste en GRIS)
URL = "stephane-lalut.com/combien-de-temps-une-erreur-reste-inscrite/"
NB = " "

# (registre de la cellule « Registre », libellé, détail affiché, fragments exacts de la cellule « Délai », marques)
# marques : ("p", années) point plein, délai ; ("c", années) point creux, délai doublé en récidive
LIGNES = [
    ("Permis à points", "Permis : infraction à un seul point", "6 mois quand une infraction n'a retiré qu'un point, sans nouvelle infraction entraînant un retrait de points", ["6 mois quand une infraction n'a retiré qu'un point, sans nouvelle infraction entraînant un retrait de points"], [("p", 0.5)]),
    ("Permis à points", "Permis : tous les points rendus",
     "2 ans sans infraction entraînant un retrait de points ; 3 ans si l'une des infractions est un délit ou une contravention de 4e ou 5e classe ; hors permis probatoire",
     ["2 ans sans infraction entraînant un retrait de points", "3 ans si l'une des infractions est un délit ou une contravention de 4e ou 5e classe"], [("p", 2), ("p", 3)]),
    ("Assurance auto, malus", "Malus d'assurance auto", "2 années consécutives sans sinistre : coefficient ramené à 1 au plus, sans rétablir le bonus antérieur",
     ["après 2 années consécutives sans sinistre"], [("p", 2)]),
    ("Fichier des incidents de crédit (FICP)", "Incident de crédit (FICP)", "5 ans au plus ; radiation dès le paiement intégral déclaré", ["5 ans"], [("p", 5)]),
    ("Interdiction d'émettre des chèques", "Interdiction d'émettre des chèques", "5 ans, moins si la personne régularise", ["5 ans"], [("p", 5)]),
    ("Assurance d'un prêt, cancer ou hépatite C", "Assurance de prêt : cancer ou hépatite C",
     "antécédent à ne plus déclarer 5 ans après la fin du protocole thérapeutique, sans rechute ; prêts couverts par la "
     "convention AERAS, assurance prenant fin avant le 71e anniversaire", ["5 ans"], [("p", 5)]),
    ("FICP, surendettement", "Surendettement (FICP)",
     "la durée du plan ou des mesures, 7 ans au plus ; 5 ans si le plan ou les mesures sont exécutés sans incident ; 5 ans après un rétablissement personnel ou, en Alsace-Moselle, la liquidation judiciaire d'un particulier",
     ["la durée du plan ou des mesures, 7 ans au plus", "5 ans si le plan ou les mesures sont exécutés sans incident",
      "5 ans après un rétablissement personnel ou, en Alsace-Moselle, la liquidation judiciaire d'un particulier"], [("p", 5), ("p", 7)]),
    ("Casier, bulletin n° 2", "Casier, bulletin n° 2 (réhabilitation)",
     "points creux : en récidive légale, délais doublés (6 ans au lieu de 3, 10 au lieu de 5, 20 au lieu de 10) ; réhabilitation légale, sans nouvelle condamnation criminelle ou correctionnelle, dans trois cas seulement : 3 ans (amende ou jours-amende), 5 ans (condamnation unique à un emprisonnement d'un an au plus ou à une peine autre que la réclusion criminelle, la détention criminelle, l'emprisonnement, l'amende ou le jour-amende), 10 ans (condamnation unique à un emprisonnement de 10 ans au plus, ou plusieurs totalisant 5 ans au plus) ; pas de réhabilitation légale au-delà de ces trois cas ; n'y figurent pas les contraventions, ni un sursis devenu non avenu, sauf mesure qui l'y maintient, ni, au bout de 3 ou 5 ans, certaines peines prononcées sans sursis",
     ["3 ans (amende ou jours-amende), 5 ans (condamnation unique à un emprisonnement d'un an au plus ou à une peine autre que la réclusion criminelle, la détention criminelle, l'emprisonnement, l'amende ou le jour-amende), 10 ans (condamnation unique à un emprisonnement de 10 ans au plus, ou plusieurs totalisant 5 ans au plus), sans nouvelle condamnation criminelle ou correctionnelle, doublés en récidive légale", "pas de réhabilitation légale au-delà de ces trois cas"], [("p", 3), ("p", 5), ("p", 10), ("c", 6), ("c", 10), ("c", 20)]),
    ("Casier, bulletin n° 1", "Casier, bulletin n° 1 (aucun employeur)",
     "40 ans sans nouvelle condamnation criminelle ou correctionnelle, hors faits imprescriptibles et condamnations "
     "étrangères ; 3 ans pour une contravention, une dispense de peine et, sous conditions, une amende forfaitaire délictuelle ou une composition pénale ; 4 ans pour une contravention dont la récidive constitue un délit",
     ["40 ans sans nouvelle condamnation criminelle ou correctionnelle", "3 ans pour une contravention, une dispense de peine, une amende forfaitaire délictuelle ou une composition pénale", "4 ans pour une contravention dont la récidive constitue un délit"],
     [("p", 3), ("p", 4), ("p", 40)]),
]
TICKS = [(0.5, "6 mois"), (1, "1 an"), (2, "2 ans"), (5, "5 ans"), (10, "10 ans"), (20, "20 ans"), (40, "40 ans")]
TICKS_M = [(0.5, "6 mois"), (2, "2 ans"), (5, "5 ans"), (10, "10 ans"), (40, "40 ans")]
TITRE = "Combien de temps dure chaque délai : de six\u00a0mois à\u00a0quarante\u00a0ans"
SOURCE = ("Source : tableau et texte de la page (droit en vigueur au 1er novembre 2026), établis d'après les textes qu'elle cite (code monétaire et financier, code de la "
          "consommation, code de commerce, arrêté du 26 octobre 2010 relatif au FICP, code pénal et code de procédure pénale, "
          "code de la route, code des assurances, code de la santé publique, convention AERAS).")
NOTE = ("Échelle logarithmique. Point plein : délai ou durée maximale ; point creux : délai du bulletin n° 2 doublé en récidive ; non figuré : le retour, au plus tard 10 ans après, des points de permis retirés pour des contraventions des quatre premières classes, même après une nouvelle infraction. Chaque délai "
        "s'écoule sans démarche, vaut dans les conditions du tableau et ne court pas du même point de départ. Certains s'abrègent : démarche de la "
        "personne (stage de récupération de points, une\u00a0fois\u00a0par\u00a0an ; régularisation d'un chèque ; justification du règlement de toutes les dettes d'un plan ou d'un jugement de surendettement ; requête en exclusion du "
        "bulletin n° 2, sauf exceptions), déclaration d'un "
        "tiers (paiement déclaré par l'établissement), délais plus courts que la convention AERAS peut fixer pour certaines "
        "pathologies. Les effets de la réhabilitation sont reportés en cas d'interdiction, d'incapacité ou de déchéance prononcée à titre définitif comme peine complémentaire, de suivi socio-judiciaire ou d'interdiction d'activité au contact de mineurs.")
NON_FIGURES = {("Permis à points", 10): "le retour, au plus tard 10 ans après, des points de permis retirés pour des contraventions des quatre premières classes"}   # durée du tableau non dessinée, déclarée par la note (A8)
LICENCE = "Figure Stéphane Lalut, CC BY 4.0" + NB + "· " + URL
LICENCE_M = "Figure Stéphane Lalut, CC" + NB + "BY" + NB + "4.0, stephane-lalut.com"   # sans séparateur : jamais « · » seul en bord de ligne


def fail(msg: str) -> None:
    print("ECHEC : " + msg)
    print("Aucun fichier ecrit.")
    sys.exit(1)


def aff(s: str) -> str:
    """Texte affiché : ordinaux en exposant (4ᵉ, comme la page écrit 4<sup>e</sup>), « 5ᵉ classe » soudé, insécables."""
    s = re.sub(r"(?<![0-9])([0-9]+)e" + "\\b", "\\1ᵉ", s)
    s = s.replace("d'un an au plus", "d'un" + NB + "an" + NB + "au" + NB + "plus").replace("pas de réhabilitation", "pas" + NB + "de" + NB + "réhabilitation").replace("n'y figurent pas", "n'y" + NB + "figurent" + NB + "pas").replace("non avenu", "non" + NB + "avenu").replace("sans incident", "sans" + NB + "incident")   # contrôleur, 12/11/2026
    s = s.replace("ᵉ classe", "ᵉ\u00a0classe").replace("ans au plus", "ans\u00a0au\u00a0plus").replace("au plus", "au\u00a0plus").replace("un délit", "un\u00a0délit").replace("hors permis", "hors\u00a0permis").replace("permis probatoire", "permis\u00a0probatoire").replace("de points", "de\u00a0points").replace("d'un particulier", "d'un\u00a0particulier").replace("à 1 au plus", "à 1 au plus").replace("le 71ᵉ anniversaire", "le 71ᵉ anniversaire").replace("4ᵉ ou 5ᵉ", "4ᵉ\u00a0ou\u00a05ᵉ")
    s = insec(s)
    s = re.sub(r"\b(sans|non|hors|sous|sauf|avant) ", "\\1" + NB, s)   # B4 : négation ou restriction jamais seule en fin de ligne
    s = re.sub("(\\d) ou (\\d+)" + NB + "ans", "\\1" + NB + "ou" + NB + "\\2" + NB + "ans", s)   # B4 : « 3 ou 5 ans »
    s = re.sub("(\\d" + NB + "ans) (après|pour)", "\\1" + NB + "\\2", s)   # B4 : « 5 ans après », « 4 ans pour » (valeur et condition)
    s = s.replace("exécutés sans", "exécutés" + NB + "sans").replace("prononcées sans", "prononcées" + NB + "sans")   # B4 : la condition « sans … » reste avec son verbe
    s = s.replace("(amende ou jours-amende)", "(amende" + NB + "ou" + NB + "jours-amende)")   # B4 : parenthèse courte entière
    s = s.replace("sans" + NB + "nouvelle infraction", "sans" + NB + "nouvelle" + NB + "infraction").replace("un retrait", "un" + NB + "retrait").replace("de la peine", "de la" + NB + "peine").replace("le bonus antérieur", "le" + NB + "bonus" + NB + "antérieur").replace("après un rétablissement", "après" + NB + "un" + NB + "rétablissement")   # C1c du contrôleur B5 ; « après un rétablissement » : A5 (12/11/2026)
    s = s.replace(" ni ", " ni" + NB)   # contrôleur A6 : « ni » jamais seul en fin de ligne
    s = s.replace("ni, au bout de 3", "ni," + NB + "au" + NB + "bout" + NB + "de" + NB + "3")   # contrôleur A6
    s = s.replace("dès le paiement", "dès" + NB + "le" + NB + "paiement")   # contrôleur A6
    s = s.replace("paiement intégral déclaré", "paiement" + NB + "intégral" + NB + "déclaré")   # contrôleur B6, 12/11/2026 : condition du tiers
    s = s.replace("amende forfaitaire délictuelle", "amende" + NB + "forfaitaire" + NB + "délictuelle")   # contrôleur B6, 12/11/2026 : terme juridique
    s = s.replace("réhabilitation légale au-delà", "réhabilitation" + NB + "légale" + NB + "au-delà")   # contrôleur B6, 12/11/2026 : négation et sa borne
    s = s.replace("de la" + NB + "peine", "de" + NB + "la" + NB + "peine")   # contrôleur B6, 12/11/2026
    s = s.replace("en Alsace-Moselle", "en" + NB + "Alsace-Moselle")   # contrôleur B6, 12/11/2026
    s = s.replace("au bout de 3", "au" + NB + "bout" + NB + "de" + NB + "3")   # contrôleur B6, 12/11/2026
    s = s.replace("prêts couverts", "prêts" + NB + "couverts")   # contrôleur B6, 12/11/2026
    s = re.sub("trois[  ]cas[  ]seulement", "trois" + NB + "cas" + NB + "seulement", s)   # contrôleur B7, 12/11/2026 : restriction avec ce qu'elle restreint
    s = re.sub("2[  ]années[  ]consécutives[  ]sans[  ]sinistre", "2" + NB + "années" + NB + "consécutives" + NB + "sans" + NB + "sinistre", s)   # contrôleur B7, 12/11/2026 : valeur et condition
    s = s.replace("n'a retiré qu'un point", "n'a" + NB + "retiré" + NB + "qu'un" + NB + "point").replace("le jour-amende", "le" + NB + "jour-amende").replace("ou le" + NB + "jour-amende", "ou" + NB + "le" + NB + "jour-amende").replace("que la réclusion criminelle", "que" + NB + "la" + NB + "réclusion" + NB + "criminelle").replace("la détention criminelle", "la" + NB + "détention" + NB + "criminelle").replace("contravention de 4ᵉ", "contravention de" + NB + "4ᵉ").replace("ou correctionnelle", "ou" + NB + "correctionnelle")   # contrôleur de lecture, 13/11/2026 : le nombre avec ce qu'il compte, l'article avec son nom
    s = s.replace("constitue un" + NB + "délit", "constitue" + NB + "un" + NB + "délit")   # contrôleur A7, 12/11/2026 : « un délit » ne reste pas seul en fin de ligne
    s = s.replace(" au lieu de ", NB + "au" + NB + "lieu" + NB + "de" + NB)   # contrôleur B7, G4 : chaque couple « 6 ans au lieu de 3 » d'un tenant
    s = s.replace("délais doublés", "délais" + NB + "doublés")   # contrôleur A8, C3
    s = s.replace("dans trois" + NB + "cas", "dans" + NB + "trois" + NB + "cas")   # contrôleur A8, C3
    s = s.replace("sans" + NB + "rétablir le", "sans" + NB + "rétablir" + NB + "le")   # contrôleur A8, C4
    s = s.replace("sans" + NB + "nouvelle condamnation", "sans" + NB + "nouvelle" + NB + "condamnation").replace("autre que" + NB + "la", "autre" + NB + "que" + NB + "la").replace("totalisant 5" + NB + "ans", "totalisant" + NB + "5" + NB + "ans")   # troisième passage des contrôleurs, 13/11/2026
    return re.sub("([0-9]" + NB + "ans) [(]", lambda m: m.group(1) + NB + "(", s)   # « 3 ans (amende…) » sur une même ligne


def coupe_det(det: str, n: int) -> list:
    """Détail affiché, coupé à n caractères. La liste des trois cas de réhabilitation légale ouvre une ligne à chaque cas
    (« 3 ans (…) », « 5 ans (…) », « 10 ans (…) »), sur les deux supports : coupe() remplit au nombre de caractères, et
    au téléphone « 10 ans » finissait une ligne une fois la peine du 2° corrigée (contrôleur de lecture, 13/11/2026)."""
    s = aff(det)
    if len(re.findall("(?<![0-9])[0-9]+" + NB + "ans" + NB + "[(]", s)) < 2:   # pas d'énumération de cas
        return PF.coupe(s, n)
    lignes = []
    for morceau in re.split("(?<![0-9])(?=[0-9]+" + NB + "ans" + NB + "[(])", s):
        lignes += PF.coupe(morceau.rstrip(), n)
    return lignes


def insec(s: str) -> str:
    """Nombre et unité insécables (règle du site, « quel que soit le support ») : pied_figure.coupe ne soude pas « mois »
    ni « années »."""
    return re.sub(r"(\d) (ans|an|mois|années|classe)\b", "\\1" + NB + "\\2", s)


def cellules_delai(md: str) -> dict:
    """Cellule « Délai » de chaque registre du tableau de la page (texte brut, insécables en espaces)."""
    out = {}
    for tr in re.findall(r"<tr>(.*?)</tr>", md, re.S):
        c = [html.unescape(re.sub(r"<[^>]+>", "", x)).replace(NB, " ") for x in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if len(c) >= 3:
            out[c[0]] = c[2]
    return out


def nombres(texte: str) -> set:
    # entiers seuls : un décimal (« 2,5 ») n'est pas lu comme 2 ni 5 ; « 3, 5 ou 10 » donne bien 3, 5 et 10
    return {int(x) for x in re.findall(r"(?<!\d,)(?<!\d)(?<!n° )(\d+)(?!\d)(?!,\d)(?![a-zA-Zé])", texte)}


def entiers(texte: str) -> set:
    """Règle 4 : tout entier écrit, ordinaux compris (« 71e », « 4e ») ; nombres() les écarte, à raison, pour les durées
    (contrôleur A4, 12/11/2026 : « 71e » changé en « 81e » passait le contrôle)."""
    return {int(x) for x in re.findall(r"(?<![0-9,])(?<!n° )([0-9]+)(?![0-9,])", texte)}


def lignes_tableau(md: str) -> dict:
    """Texte de toutes les cellules de chaque ligne du tableau (registre en clé), pour confronter les détails affichés."""
    out = {}
    for tr in re.findall(r"<tr>(.*?)</tr>", md, re.S):
        c = [html.unescape(re.sub(r"<[^>]+>", "", x)).replace(NB, " ") for x in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if c:
            out[c[0]] = " ".join(c)
    return out


def verifier(md: str, lignes, note: str = NOTE) -> None:
    cel = cellules_delai(md)
    rangs = lignes_tableau(md)
    if "--mutation=texte" in sys.argv[1:]:   # témoin : une cellule reformulée doit arrêter le script
        cel["Casier, bulletin n° 1"] = cel.get("Casier, bulletin n° 1", "").replace("40 ans", "30 ans")
    for reg, lab, det, verifs, marques in lignes:
        if reg not in cel:
            fail("registre absent du tableau de la page : %s" % reg)
        for v in verifs:
            if v not in cel[reg]:
                fail("« %s » introuvable dans la cellule Délai de « %s » : relire la page avant toute écriture" % (v, reg))
        frag = " ".join(verifs)
        nb = nombres(frag)
        attendus = (nb - {6}) | {0.5} if "6 mois" in frag else nb
        pleins = {an for sorte, an in marques if sorte == "p"}
        creux = sorted(an for sorte, an in marques if sorte == "c")
        for an in pleins | set(creux):
            if not (TICKS[0][0] <= an <= TICKS[-1][0]):
                fail("valeur hors de l'axe : %s (%s)" % (an, lab))
        if pleins != attendus:
            fail("« %s » : points %s, durées du tableau %s (%s)" % (lab, sorted(pleins), sorted(attendus), frag))
        if creux != (sorted(2 * a for a in pleins) if "doublés" in frag else []):
            fail("« %s » : points creux %s, doubles attendus %s" % (lab, creux, sorted(2 * a for a in pleins) if "doublés" in frag else []))
        ligne = rangs.get(reg, "")
        hors = nombres(det) - nombres(ligne) - ({6} if "6 mois" in det else set()) - set(creux)
        hors |= entiers(det) - entiers(ligne) - ({6} if "6 mois" in det else set()) - set(creux)   # ordinaux compris (A4)
        if hors:
            fail("« %s » : nombres du détail absents de la ligne du tableau : %s" % (lab, sorted(hors)))
    # Règle 5 (contrôleur A8, 12/11/2026) : toute durée de la cellule « Délai » d'un registre est dessinée dans l'une de
    # ses lignes, ou déclarée « non figurée » dans la note (NON_FIGURES). Durées seulement, nombre suivi d'une unité de
    # temps : nombres() lirait le « 1 » du coefficient du malus.
    dessines = {}
    for reg, _, _, _, marques in lignes:
        dessines.setdefault(reg, set()).update(an for sorte, an in marques if sorte == "p")
    for reg, vus in dessines.items():
        durees = {int(n) / 12 if u == "mois" else int(n) for n, u in re.findall(
            "(?<![0-9,])([0-9]+)[ " + NB + "](ans|an|années|mois)(?![a-zA-Zé])", cel[reg])}
        for an in sorted(durees - vus):
            phrase = NON_FIGURES.get((reg, an))
            if phrase is None or phrase.replace(NB, " ") not in note.replace(NB, " "):   # clause entière, nombre compris (A9 G3)
                fail("« %s » : %s an(s) dans la cellule Délai, ni dessiné ni déclaré dans la note" % (reg, an))
    # Règle 6 (contrôleur A8, 12/11/2026) : chaque couple « A au lieu de B » d'un détail, A = 2 B (délais doublés,
    # art. 133-13 du code pénal), B point plein et A point creux de la même ligne.
    for _, lab, det, _, marques in lignes:
        pleins = {an for sorte, an in marques if sorte == "p"}
        creux = {an for sorte, an in marques if sorte == "c"}
        for a, b in re.findall("([0-9]+)(?: ans)? au lieu de ([0-9]+)", det.replace(NB, " ")):   # insécables comprises (A9 C11)
            if int(a) != 2 * int(b) or int(b) not in pleins or int(a) not in creux:
                fail("« %s » : couple « %s au lieu de %s » faux" % (lab, a, b))


def desc() -> str:
    parts = ["%s, %s" % (lab, aff(det).replace("ᵉ", "e")) for _, lab, det, _, _ in LIGNES]   # ordinaux en clair pour la synthèse vocale (A5)
    return ("Frise des délais fixés par les textes, sur une échelle logarithmique de six mois à quarante ans. " + " ; ".join(parts) + ". " + NOTE)


def x_de(an: float, x0: float, x1: float) -> float:
    a, b = math.log(TICKS[0][0]), math.log(TICKS[-1][0])
    return x0 + (math.log(an) - a) / (b - a) * (x1 - x0)


COCHE = "#8f8b84"   # repères de graduation de chaque ligne du téléphone : 3,39:1 sur blanc (contrôleur, 12/11/2026)
DY_RECIDIVE = 14   # les points creux (récidive) sur une seconde ligne, juste dessous : 5 et 6 ans ne se touchent pas (rendu du 04/11)


def marques_svg(e: list, marques, y: float, x0: float, x1: float, r: float = 5.5) -> None:
    for sorte, an in marques:
        x = x_de(an, x0, x1)
        if sorte == "p":
            e.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x, y, r, BLEU))
        else:
            e.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffffff" stroke="%s" stroke-width="1.6"/>'
                     % (x, y + DY_RECIDIVE, r - 0.5, BLEU))


def figure() -> str:
    W, X0, X1 = 720, 300, 690
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, NOM, NOM, esc(FONT)),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (NOM, esc(TITRE), NOM, esc(desc())),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W,
         '<text x="0" y="22" font-size="17" font-weight="600" fill="%s">%s</text>' % (ENCRE, esc(TITRE))]
    # Hauteur de ligne : 54 pour un détail de deux lignes, 13 de plus par ligne au-delà. Jamais de troncature : le
    # 04/11/2026, un [:2] coupait en silence deux détails au milieu d'une phrase (contrôleur indépendant).
    y0, pas = 74, 54   # 74 : place de l'échelle en tête (contrôleur indépendant, 12/11/2026)
    dets = [coupe_det(det, 48) for _, _, det, _, _ in LIGNES]   # 48 : « délit » ne reste pas seul (04/11)
    ys, y = [], y0
    for d in dets:
        ys.append(y)
        y += pas + 13 * (len(d) - 2)   # contrôleur, 12/11/2026
    yb = y - 14
    e.append('<text x="0" y="%d" font-size="11" fill="%s">%s</text>' % (y0 - 22, GRIS, esc("Échelle logarithmique :")))
    for an, lab in TICKS:
        x = x_de(an, X0, X1)
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (x, y0 - 14, x, yb, GRILLE))
        e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="middle">%s</text>' % (x, y0 - 22, GRIS, esc(insec(lab))))   # échelle en tête
        e.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="middle">%s</text>' % (x, yb + 15, GRIS, esc(insec(lab))))
    for k, (_, lab, det, _, marques) in enumerate(LIGNES):
        y = ys[k]
        e.append('<text x="0" y="%.1f" font-size="13" font-weight="600" fill="%s">%s</text>' % (y - 2, ENCRE, esc(lab)))
        for j, l in enumerate(dets[k]):
            e.append('<text x="0" y="%.1f" font-size="11" fill="%s">%s</text>' % (y + 12 + 13 * j, DETAIL, esc(l)))
        marques_svg(e, marques, y + 2, X0, X1)
    return PF.pied(e, yb + 26, W, [(SOURCE, GRIS, "pied-source"), (NOTE, GRIS, "pied-note"), (LICENCE, GRIS, "pied-licence")], FILET)


def graduations_m(e: list, y: float, X0: float, X1: float) -> None:
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    for an, lab in TICKS_M:
        x = x_de(an, X0 + 6, X1 - 6)
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (x, y - 6, x, y, GRIS))
        # extrêmes ancrés au bord (exception déclarée : centrés, « 6 mois » et « 40 ans » sortiraient du cadre de 300)
        ancre = "start" if an == TICKS_M[0][0] else ("end" if an == TICKS_M[-1][0] else "middle")
        xt = 0 if ancre == "start" else (PF.LARGEUR_M if ancre == "end" else x)
        if an == 10:   # « 10 ans » commence à son trait : centré, il touchait « 5 ans » (contrôleur A4, 12/11/2026)
            ancre, xt = "start", x
        e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%s</text>'
                 % (xt, y + 15, PF.POLICE_M, GRIS, ancre, esc(insec(lab))))


def figure_m() -> str:
    WM, X0, X1 = PF.LARGEUR_M, 4, PF.LARGEUR_M - 4
    esc = lambda s: html.escape(s, quote=False)  # noqa: E731
    e, y = PF.tete_mobile(NOM + "-m", TITRE, desc(), ENCRE, FONT)
    for l in PF.coupe("Même échelle logarithmique partout :", 38):
        y += 18
        e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, PF.POLICE_M, GRIS, esc(l)))
    y += 16
    graduations_m(e, y, X0, X1)   # échelle en tête : au téléphone, celle du bas est trop loin des premières lignes
    y += 22
    for k, (_, lab, det, _, marques) in enumerate(LIGNES):
        if k in (5, 7):   # échelle rappelée (avant le bulletin n° 2 aussi : option B, contrôleur B4) : les lignes du milieu étaient à plus d'un écran de toute graduation (contrôleur, 12/11/2026)
            y += 16
            graduations_m(e, y, X0, X1)
            y += 22
        for l in PF.coupe(lab, 41):   # 41 : un libellé qui tient sur une ligne n'est plus coupé (contrôleur, 12/11/2026)
            y += 18
            e.append('<text x="0" y="%.1f" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y, PF.POLICE_M, ENCRE, esc(l)))
        y += 14   # option B : l'échelle de la ligne et ses points juste sous le libellé
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, y, X1, y, GRILLE))
        for an, _ in TICKS_M:   # repères des graduations sur chaque ligne
            xt = x_de(an, X0 + 6, X1 - 6)
            e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (xt, y - 4, xt, y + 4, COCHE))
        marques_svg(e, marques, y, X0 + 6, X1 - 6, r=5)
        if any(m[0] == "c" for m in marques):   # G3 : la clé des points creux à leur hauteur (contrôleur, 12/11/2026)
            e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y + DY_RECIDIVE + 5, PF.POLICE_M, GRIS, esc("en récidive" + NB + ":")))
            y += DY_RECIDIVE + 8   # la clé « en récidive » reste avec ses points (contrôleur B6)
        y += 6
        for l in coupe_det(det, 40):   # 40 : C1c du contrôleur B5 (12/11/2026)
            y += 17
            e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, PF.POLICE_M, DETAIL, esc(l)))
        y += 14
    y += 8
    graduations_m(e, y, X0, X1)
    return PF.pied_mobile(e, y + 30, [(SOURCE, GRIS, "pied-source"), (NOTE, GRIS, "pied-note"), (LICENCE_M, GRIS, "pied-licence")], FILET)


def main() -> None:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    md = PAGE.read_text(encoding="utf-8")
    lignes = LIGNES
    if "--mutation=marque" in sys.argv[1:]:   # témoin : une marque déplacée (5 → 6 ans) doit arrêter le script
        lignes = [(r, l, d, v, [("p", 6)] if l == "Incident de crédit (FICP)" else m) for r, l, d, v, m in LIGNES]
    if "--mutation=omission" in sys.argv[1:]:  # témoin : une durée du tableau sans sa marque (7 ans) doit arrêter
        lignes = [(r, l, d, v, [("p", 5)] if l == "Surendettement (FICP)" else m) for r, l, d, v, m in LIGNES]
    if "--mutation=detail" in sys.argv[1:]:    # témoin : un nombre faux dans un détail affiché doit arrêter
        lignes = [(r, l, d.replace("5 ans", "8 ans") if l == "Assurance de prêt : cancer ou hépatite C" else d, v, m) for r, l, d, v, m in LIGNES]
    if "--mutation=ordinal" in sys.argv[1:]:   # témoin : un ordinal faux (71e -> 81e) doit arrêter le script (A4)
        lignes = [(r, l, d.replace("71e", "81e"), v, m) for r, l, d, v, m in lignes]
    if "--mutation=couple" in sys.argv[1:]:   # témoin (A8) : un couple de récidive faux doit arrêter le script
        lignes = [(r, l, d.replace("20 au lieu de 10", "20 au lieu de 5"), v, m) for r, l, d, v, m in lignes]
    note = NOTE
    if "--mutation=nonfigure" in sys.argv[1:]:   # témoin (A8, A9) : la note déclare une autre durée (12 ans)
        note = NOTE.replace(NB + "10" + NB + "ans", NB + "12" + NB + "ans")
    verifier(md, lignes, note)
    figs = {NOM + ".svg": figure(), NOM + "-m.svg": figure_m()}
    ecarts = PF.parite(figs[NOM + ".svg"], figs[NOM + "-m.svg"], PF.POLICE_M, couleurs=(DETAIL,))
    if ecarts:
        fail("parite telephone : %s" % ecarts)
    ecarts = PF.controler_page(md, figs)
    for f, s in figs.items():
        print("  %s : viewBox %s" % (f, re.search(r'viewBox="([^"]+)"', s).group(1)))
    if ecarts:
        if check:
            print("A REPORTER DANS LA PAGE : %s" % "; ".join(ecarts))
        else:
            fail("page : %s" % "; ".join(ecarts))
    if check:
        print("--check : %d lignes verifiees contre le tableau de la page (fragments et valeurs), rien ecrit." % len(LIGNES))
        return
    import cairosvg
    change = [f for f, s in figs.items() if not (OUT / f).exists() or (OUT / f).read_text(encoding="utf-8") != s]
    pngs = {f: cairosvg.svg2png(bytestring=figs[f].encode("utf-8"), output_width=1440, background_color="white") for f in change}
    for f in change:
        (OUT / f).write_text(figs[f], encoding="utf-8", newline="\n")
        (OUT / f.replace(".svg", ".png")).write_bytes(pngs[f])
    print("Ecrit : %d SVG, %d PNG" % (len(change), len(pngs)))


if __name__ == "__main__":
    main()
