#!/usr/bin/env python3
"""Prolongement « Europe » du dossier Promesses : ce que la France peut décider dans l'Union européenne.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, « Prolongement U » (gelé au
commit 324c9cd ; champ de U-E2 fixé avant calcul au commit a650e9c). Tests décisifs : test_decisif/europe/ (U-E1, U-E2,
U-E3, U-E4 ; commits 1ec0c07, aa11c84).

Entrées (script LOCAL ; il s'arrête si elles manquent) :
  U-E1, U-E2  le TFUE consolidé (JO C 202 du 07/06/2016, XHTML de Cellar, empreintes vérifiées), lu et qualifié par
              les fonctions des tests décisifs (test_u_e1.py, test_u_e2.py), importées ici et non recopiées ;
  U-E3        le relevé de la recherche des votes du Conseil de l'UE fait dans le navigateur le 06/10/2026 (le site refuse
              les scripts ; méthode : test_u_e3_conseil.js), TRANSCRIT ci-dessous, et le jeu SWP / GESIS (DOI
              10.7802/2560) que le script relit pour contrôler la transcription pays par pays ;
  U-E4        le tableau d'affichage du marché unique (Commission), transcrit d'une capture (test_u_e4.py, qui le contrôle) ;
  phase B     (12/10/2026) les articles du TUE et du TFUE cités par la page et le protocole n° 36, FR et EN (Cellar,
              archivés dans sondes/europe/tfue/, empreintes) ; pour les cinq actes où la France n'a pas voté pour, la
              note « Voting result » du Conseil (PDF, sondes/europe/conseil_votes/) et l'acte publié (EUR-Lex, FR et EN,
              sondes/europe/eurlex_actes/) ; les pages FR et EN (garde de prose U9).

Gardes (toutes ARRÊTENT ; le texte servi n'est relu que par U9) :
  U1  typologie complète et citée (contrôles de test_u_e1) ;
  U2  bases qualifiées sans unité non classée, concordance exacte avec le témoin du Conseil (test_u_e2) ;
  U3  TÉMOIN : sur la période commune (22/12/2009 - 28/03/2023), les comptes « contre » et « abstention » de chaque État,
      recalculés du jeu SWP, égalent la transcription du relevé du Conseil, aux seuls écarts expliqués près (acte du
      28/03/2023 absent de SWP ; deux fiches SWP sans titre du 17/05/2021 démenties par le registre des documents) ;
      tout autre écart arrête ; les règles de vote du relevé totalisent ses entrées (1 622 + 132 + 1) ; passe B2 : les deux
      fiches du 17/05/2021 cherchées au Conseil (récapitulatif des actes de mai 2021 relu : aucune séance ce jour, une seule
      procédure écrite, PESC ; dans SWP, rien d'autre qu'elles entre les votes du 10 et du 26/05 que rend la recherche du
      Conseil) ;
  U4  la liste des actes de la France est cohérente avec ses comptes ; le total des votes est écrit en borne ;
  U5  transposition : contrôles de test_u_e4 (moyennes dans le texte de la Commission, cohérence 11 / 1 022) ;
  U6  chaque citation des traités ajoutée en phase B retrouvée mot pour mot, FR et EN, dans le texte archivé ; passe B3 :
      les phrases que la page résume sans les citer (TFUE 238, § 3, FR et EN ; TFUE 168, § 4, FR, traité complet archivé)
      et la citation anglaise du TUE, art. 16, § 4, relues dans le texte archivé ;
  U7  citations SWP 2021 et 2024 et inventaire Polidori 2014 relus dans les PDF archivés ;
  U8  les cinq actes : décompte qui totalise les États membres du moment et contient la position de la France ; note du
      Conseil (procédure, date du vote) et acte publié (numéro, date, « décision du Conseil du <date du vote> ») relus ;
      décompte recalculé depuis le jeu SWP pour les votes qu'il couvre (les deux votes postérieurs n'ont pas de second
      jeu : passe B3, leur COMPOSITION État par État, transcrite, est relue dans l'annexe en image de la note, pictogramme
      par pictogramme ; un vote déplacé à total constant arrête) ;
  U9  GARDE DE PROSE (pages FR et EN, jetons résolus) : « amender … unanimité » jamais sans « sauf » / « except » dans la
      phrase (art. 293, § 1 : exceptions) ; aucune formule de classement verbal (« moins / plus souvent que ») ; « pour
      dans tous les autres cas » seulement si la France n'a aucune non-participation. Justification R2 : remplace la
      promesse « U4 interdit le classement » de l'en-tête antérieur, qui ne lisait aucune phrase ; une fonction, quatre
      mutations. Condition de mort : la page ne cite plus l'art. 293 ni de comparaison entre États.
Autotest (chaque mutation doit arrêter SA garde) : vote de la France et compte d'un État altérés (U3), domaine retiré
(U1), écart SWP modifié (U7), séance du 17/05/2021 injectée et fiche SWP retirée (U3, passe B2), citations FR et EN altérées (U6), décomptes 2014 et 2026 et date d'un acte altérés (U8),
deux phrases résumées altérées (U6, passe B3), composition de 2025 et de 2026 altérée à total constant (U8, passe B3),
quatre phrases fautives injectées (U9). Figures téléphone : parité avec la version détaillée (pied_figure.parite).

Écrit : data/promesses_europe.json (+ static/), static/promesses_europe.csv, data/figures_europe.json,
static/img/europe-votes(-en)(-m).svg/.png. Rien n'est écrit à données identiques ; --check n'écrit rien. Sortie ASCII.
"""
from __future__ import annotations

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
PRO = ROOT.parents[1]
RECH = PRO / "06_PROMOTION" / "RECHERCHE_DOSSIER_PROMESSES_2026-10-05"
TESTS = RECH / "test_decisif" / "europe"
SWP = RECH / "sondes" / "europe" / "swp" / "2023-04-12_ceu_vote_full_voting.csv"
sys.path.insert(0, str(TESTS))
import test_u_e1 as ue1  # noqa: E402
import test_u_e2 as ue2  # noqa: E402
import test_u_e4 as ue4  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure as pf  # noqa: E402
import langue_generee as lg  # noqa: E402

PAGE_URL = "stephane-lalut.com/ce-que-la-france-peut-decider-dans-l-union-europeenne/"
PAGE_URL_EN = "stephane-lalut.com/en/what-can-france-decide-in-the-european-union/"
OUT_DATA = ROOT / "data" / "promesses_europe.json"
OUT_STATIC = ROOT / "static" / "promesses_europe.json"
OUT_CSV = ROOT / "static" / "promesses_europe.csv"
OUT_FIGURES = ROOT / "data" / "figures_europe.json"
OUT_IMG = ROOT / "static" / "img"

# --- U-E3 : relevé du Conseil, 06/10/2026 (recherche publique des votes, 1 755 entrées, 22/12/2009 - 01/10/2026).
RELEVE = {"date": "2026-10-06", "entrees": 1755, "doublons": 8, "debut": "2009-12-22", "fin": "2026-10-01",
          "regles": {"Majorité qualifiée": 1622, "Unanimité": 132, "Majorité qualifiée sans proposition de la Commission": 1}}
# État -> (contre, abstention, ne participe pas) sur tout le relevé ; puis (contre, abstention) sur la période commune.
TOUT = dict(x.split(":") for x in (
    "AT:36/67/0 BE:7/47/0 BG:19/48/1 CY:13/1/1 CZ:19/54/3 DE:32/48/0 DK:29/12/159 EE:7/26/3 EL:7/7/1 ES:17/14/2 "
    "FI:19/11/1 FR:2/3/0 HR:4/12/1 HU:79/47/4 IE:5/12/106 IT:18/12/2 LT:6/7/3 LU:15/18/0 LV:7/20/3 MT:15/17/0 "
    "NL:41/24/1 PL:57/40/4 PT:8/19/0 RO:9/11/3 SE:41/13/2 SI:6/15/0 SK:23/35/4 UK:56/118/72").split())
TOUT = {k: tuple(int(n) for n in v.split("/")) for k, v in TOUT.items()}
FENETRE = dict(x.split(":") for x in (
    "AT:30/40 BE:7/25 BG:15/24 CY:13/1 CZ:17/29 DE:27/33 DK:26/8 EE:6/15 EL:6/4 ES:11/10 FI:10/6 FR:1/2 HR:2/10 "
    "HU:37/34 IE:5/11 IT:10/7 LT:6/5 LU:11/16 LV:5/12 MT:14/8 NL:38/19 PL:31/30 PT:6/14 RO:7/10 SE:31/9 SI:4/12 "
    "SK:13/16 UK:56/118").split())
FENETRE = {k: tuple(int(n) for n in v.split("/")) for k, v in FENETRE.items()}
FIN_TEMOIN = "2023-03-28"
# Écarts expliqués entre le relevé et le témoin (VERDICT_U_E3.md) : (État, champ) -> écart Conseil - SWP.
ECARTS_EXPLIQUES = {("PL", 0): +1, ("BG", 1): +1, ("IT", 1): +1, ("RO", 1): +1,  # acte du 28/03/2023, absent de SWP
                    ("FR", 0): -2}  # deux fiches SWP sans titre du 17/05/2021, démenties par le registre des documents
# --- Passe B2 (12/10/2026, question du panel « après ») : ces deux fiches SWP cherchées dans les publications du Conseil.
# (1) Récapitulatif mensuel des actes du Conseil de mai 2021 (ST 8962/21 INIT, 28/06/2021, PDF archivé dans conseil_votes/) :
# séances des 6, 10, 20, 26 et 27-28 mai, aucune le 17 ; le 17 mai, un seul acte, par procédure écrite, une décision PESC
# (mesures restrictives, cyberattaques) ; aucune procédure écrite législative dans le mois. (2) Recherche des votes du
# Conseil, lue dans le navigateur le 12/10/2026 (France, toutes positions) : du 01/05 au 15/06/2021, votes le 10/05 puis le
# 26/05, aucun entre les deux ; fenêtre du 14 au 21/05 : « 0 result(s) found ». (2) est TRANSCRIT ; la garde (U3) relit (1)
# et vérifie dans le jeu SWP qu'entre ces deux dates il n'y a que les fiches écartées.
MAI21 = {"pdf": "ST-8962-2021-INIT_en.pdf", "sha": "3a4db0c32db356110482068afd3c685a27582bba857c310a957150f3cda63790",
         "date": "2021-05-17", "avant": "2021-05-10", "apres": "2021-05-26"}


def texte_mai21() -> str:
    import fitz
    p = CONSEIL_DIR / MAI21["pdf"]
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != MAI21["sha"]:
        raise Arret("U3 : récapitulatif des actes de mai 2021 absent ou modifié (%s)" % p.name)
    return re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in fitz.open(p)))


def verifier_17mai(texte: str, rows: list) -> str:
    """Les deux fiches SWP écartées : aucune séance du Conseil ni acte législatif le 17/05/2021 dans le récapitulatif du
    Conseil, et, dans SWP, rien d'autre qu'elles entre les deux votes qui encadrent ce jour dans la recherche du Conseil."""
    if "MONTHLY SUMMARY OF COUNCIL ACTS - MAY 2021" not in texte:
        raise Arret("U3 : le récapitulatif archivé n'est pas celui de mai 2021")
    seances = re.findall(r"meeting of the Council of the European Union \([^)]*\) held in \w+ on ([0-9-]+) May 2021", texte)
    jour = int(MAI21["date"][-2:])
    if not seances or any(int(s.split("-")[0]) <= jour <= int(s.split("-")[-1]) for s in seances):
        raise Arret("U3 : le récapitulatif de mai 2021 porte une séance du Conseil le %s (%s)" % (MAI21["date"], seances))
    ecrites = re.findall(r"Written procedure completed on %d May 2021 CM \S+ (.{0,300})" % jour, texte)
    if len(ecrites) != 1 or "(CFSP)" not in ecrites[0]:
        raise Arret("U3 : le %s, le récapitulatif ne porte plus une seule procédure écrite PESC (%d)" % (MAI21["date"], len(ecrites)))
    i = texte.find("Written procedures NON LEGISLATIVE ACTS")
    if i < 0 or re.search(r"(?<!NON )LEGISLATIVE ACTS", texte[i:]):
        raise Arret("U3 : le récapitulatif de mai 2021 porte une procédure écrite législative")
    entre = [r for r in rows if MAI21["avant"] < r["decisionDate"] < MAI21["apres"]]
    if (len(entre) != -ECARTS_EXPLIQUES[("FR", 0)] or any(r["decisionDate"] != MAI21["date"] or r["countryCodeAgainstGrouped"] != "FR"
                                                         or r["docTitle"] != "NA" for r in entre)):
        raise Arret("U3 : entre le %s et le %s, SWP ne porte pas exactement les fiches écartées (%d fiches)" % (MAI21["avant"], MAI21["apres"], len(entre)))
    return ("U3 : fiches SWP du %s cherchées au Conseil : aucune séance ce jour (séances %s mai), une procédure écrite PESC, "
            "aucune procédure écrite législative ; SWP n'a que ces %d fiches entre le %s et le %s"
            % (MAI21["date"], ", ".join(seances), len(entre), MAI21["avant"], MAI21["apres"]))
# --- Les cinq actes où la France n'a pas voté pour, LUS À LA SOURCE le 12/10/2026 (phase B, arbitrage de la
# contre-expertise de phase A) : résultat de vote publié par le Conseil (note « Voting result » du registre public, PDF
# archivé ; décompte lu dans son annexe, une image, et recoupé sur la page de recherche des votes du Conseil, lue dans le
# navigateur) et acte publié au Journal officiel (EUR-Lex, XHTML de Cellar archivé, FR et EN). Le décompte est
# TRANSCRIT ; la garde U8 relit dans les fichiers archivés ce qui s'y lit en texte (procédure, date du vote, numéro et
# date de l'acte, « décision du Conseil du … ») et, pour les trois actes antérieurs à mars 2023, recalcule le décompte
# depuis le jeu SWP. Les deux actes postérieurs n'ont pas de second jeu : ils sont « documentés à la source ».
# (vote, position, titre FR, titre EN, (pour, contre, abstention, ne participe pas), note du Conseil, CELEX,
#  acte FR, acte EN, date de l'acte, procédure)
ACTES = [
    ("2014-02-17", "contre", "Règlement sur les vins aromatisés", "Regulation on aromatised wine products",
     (27, 1, 0, 0), "ST-6595-2014-INIT", "32014R0251", "règlement (UE) n° 251/2014", "Regulation (EU) No 251/2014", "2014-02-26", "2011/0231 (COD)"),
    ("2014-05-08", "abstention", "Directive modifiant la directive 2001/110/CE relative au miel", "Directive amending Council Directive 2001/110/EC relating to honey",
     (24, 2, 2, 0), "ST-9727-2014-INIT", "32014L0063", "directive 2014/63/UE", "Directive 2014/63/EU", "2014-05-15", "2012/0260 (COD)"),
    ("2015-10-01", "abstention", "Règlement sur le commerce des produits dérivés du phoque", "Regulation on trade in seal products",
     (23, 1, 4, 0), "ST-12596-2015-INIT", "32015R1775", "règlement (UE) 2015/1775", "Regulation (EU) 2015/1775", "2015-10-06", "2015/0028 (COD)"),
    ("2025-07-08", "abstention", "Décision sur l'accord d'interprétation du traité sur la Charte de l'énergie", "Decision on the agreement on the interpretation of the Energy Charter Treaty",
     (22, 1, 4, 0), "ST-11350-2025-INIT", "32025D1904", "décision (UE) 2025/1904", "Decision (EU) 2025/1904", "2025-09-10", "2024/0148 (COD)"),
    ("2026-02-23", "contre", "Règlement sur la notion de « pays tiers sûr »", "Regulation on the 'safe third country' concept",
     (23, 3, 0, 1), "ST-6628-2026-INIT", "32026R0463", "règlement (UE) 2026/463", "Regulation (EU) 2026/463", "2026-02-24", "2025/0132 (COD)"),
]
FR_ACTES = [(a[0], a[1], a[2], a[3]) for a in ACTES]
CONSEIL_DIR = RECH / "sondes" / "europe" / "conseil_votes"
ACTES_DIR = RECH / "sondes" / "europe" / "eurlex_actes"
CONSEIL_SHA = {"ST-6595-2014-INIT": "98f7cae82c4db176cf580f9d6c38ec6aa4f3f7fda99eb27f0f420c99dafa6c75",
               "ST-9727-2014-INIT": "c575a52481b6c473885b1fa3f86c40aaa9a88a469c15ca7d9743b555ec093bea",
               "ST-12596-2015-INIT": "68f95e58fcf4c778018bc29a0d0891e9526a9405c6934dcbc3f2143f18253f65",
               "ST-11350-2025-INIT": "7f6749b61a6fa6a384e5cee1d1d8cbe99c9a9bde197efd923e6f63735ac10241",
               "ST-6628-2026-INIT": "7b6d26f36b0beda9b65ce7bf1466e03cb6bca73e43408de487d77a4b0fe85b39"}
ACTES_SHA = {"32014R0251": ("d400b28a552c1951d599fd3e1eb983cbfb78c3eff20712c90f422f68e83ec497", "eb80ce751563ef2351c1e4b33d2aed8220cac85c6c53e9a0fba6f4355246c7cb"),
             "32014L0063": ("c2d48bae93704ca7186238104b85658b6ec32c1943213f86c68245bc30889090", "b7cfdff91624e7d7f599935867deb81f4554c6ab93f0ba17ba502fe8618237a9"),
             "32015R1775": ("cfac2f56a38e522d9b745629d6042e90b1547ceca952a42da83d7de33f784dbb", "b742cb28fe80c86f9156008032433a6683e9976e531e8ff370e5c011239b3a04"),
             "32025D1904": ("180661aebda2ed8b8f50c24e9b05c3c79a4ed3f436e045d4c0c4956056923f69", "fbd13cd91a3977629d4c8d7e9acc2809d909d2133aa0275613046a2916f39520"),
             "32026R0463": ("7de35b3eb7af3e6c89d86095996537be342b73ae19d632bfd10c8729b3b2c9e0", "4ea6a673354c4be49071badc37273d6706e826bfb5af94ca939c9f2bb9f40ef2")}
DEBUT_DOUBLE_MAJORITE = "2014-11-01"  # TUE art. 16, § 4 et protocole n° 36, art. 3 (relus par la garde U6)
# --- Passe B3 (12/10/2026, arbitrage de la contre-expertise du rendu, U8 renforcée) : pour les deux votes sans second jeu
# (2025, 2026), la COMPOSITION État par État, transcrite de l'annexe de la note du Conseil (une image, page 2 du PDF
# archivé, lue à l'œil le 12/10/2026) ; la garde U8 relit les pictogrammes de vote de cette image, pixel par pixel
# (vert pour, rouge contre, jaune abstention, aucun pictogramme coloré = ne participe pas), dans l'ordre protocolaire
# du Conseil (deux colonnes), et s'arrête au moindre écart avec la transcription. Un total juste ne suffit plus : un vote
# déplacé entre deux catégories à total constant arrête (mutation de l'autotest). L'extraction n'est pas fiable sur les
# annexes de 2014-2015 (mise en page différente) : ces trois votes restent contrôlés par le jeu SWP.
# R2 : une fonction de lecture, aucune dépendance nouvelle (fitz déjà importé) ; condition de mort : la page ne publie
# plus le décompte des votes de 2025 et 2026, ou un second jeu indépendant les couvre État par État.
ORDRE_CONSEIL = (("BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR", "IT", "CY", "LV"),
                 ("LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT", "RO", "SI", "SK", "FI", "SE"))
COMPOSITION = {"ST-11350-2025-INIT": {"contre": ("HU",), "abstention": ("CZ", "FR", "MT", "AT"), "np": ()},
               "ST-6628-2026-INIT": {"contre": ("ES", "FR", "PT"), "abstention": (), "np": ("DK",)}}


def lire_annexe(pdf: Path) -> dict:
    """Pictogrammes de vote de l'annexe (page 2, image unique) : {État: "pour" | "contre" | "abstention" | "np"}.
    Colonnes de vote = bandes verticales les plus colorées de chaque moitié ; pictogrammes = segments verticaux d'une même
    couleur ; rang = écart au premier pictogramme divisé par le pas médian. Toute ambiguïté arrête (jamais de valeur par
    défaut silencieuse : un rang en double ou hors grille est une erreur)."""
    import fitz
    import statistics
    d = fitz.open(pdf)
    imgs = d[1].get_images(full=True)
    if len(imgs) != 1:
        raise Arret("U8 : %s : %d images en page 2 (1 attendue)" % (pdf.name, len(imgs)))
    pix = fitz.Pixmap(d, imgs[0][0])
    if pix.alpha or pix.n != 3:
        pix = fitz.Pixmap(fitz.csRGB, pix, 0)
    W, H, n, s = pix.width, pix.height, pix.n, pix.samples

    def cls(i, j):
        o = (j * W + i) * n
        r, g, b = s[o], s[o + 1], s[o + 2]
        if g > 120 and r < 150 and b < 100 and g - r > 40:
            return "pour"
        if r > 180 and g < 90 and b < 90:
            return "contre"
        if r > 200 and g > 170 and b < 80:
            return "abstention"
        return None
    y0, y1 = int(H * 0.40), int(H * 0.85)
    cnt = [sum(1 for j in range(y0, y1) if cls(i, j)) for i in range(W)]
    colonnes = []
    for a, b in ((0, W // 2), (W // 2, W)):
        m = max(range(a, b), key=lambda i: cnt[i])
        lo = hi = m
        while lo > a and cnt[lo - 1] >= 0.5 * cnt[m]:
            lo -= 1
        while hi < b - 1 and cnt[hi + 1] >= 0.5 * cnt[m]:
            hi += 1
        runs, cur = [], None
        for j in range(y0, y1):
            c = [cls(i, j) for i in range(lo, hi + 1)]
            k = max(("pour", "contre", "abstention"), key=c.count)
            k = k if c.count(k) >= 0.4 * len(c) else None
            if cur and cur[0] == k:
                cur[2] = j
            else:
                if cur and cur[0] and cur[2] - cur[1] >= 7:
                    runs.append(cur)
                cur = [k, j, j]
        if cur and cur[0] and cur[2] - cur[1] >= 7:
            runs.append(cur)
        colonnes.append([(r[0], (r[1] + r[2]) / 2) for r in runs])
    ys = [y for col in colonnes for _, y in col]
    pas = statistics.median([b - a for col in colonnes for (_, a), (_, b) in zip(col, col[1:])])
    haut = min(ys)
    lu = {}
    for col, etats in zip(colonnes, ORDRE_CONSEIL):
        for k, y in col:
            rang = (y - haut) / pas
            if abs(rang - round(rang)) > 0.25 or not 0 <= round(rang) < len(etats) or etats[round(rang)] in lu:
                raise Arret("U8 : %s : pictogramme hors grille (y = %.0f, pas %.1f)" % (pdf.name, y, pas))
            lu[etats[round(rang)]] = k
    return {e: lu.get(e, "np") for col in ORDRE_CONSEIL for e in col}

# --- Citations des traités ajoutées en phase B (12/10/2026) : textes de Cellar archivés (JO C 202 du 07/06/2016, FR et EN,
# empreintes vérifiées), chaque phrase retrouvée mot pour mot (garde U6). clé : (fichier FR, sha FR, phrase FR,
# fichier EN, sha EN, phrase EN). Répertoire tfue/ (FR) et tfue/en/ (EN) de la sonde.
TFUE_DIR = RECH / "sondes" / "europe" / "tfue"
_F = {"tue4": ("tue_art4.xhtml", "4019e93305fc002c4ce5ea5a65ec38457268500ec2f5c0635e6094c5a3019d25", "arttue4.xhtml", "5e6bbe07535d607a94a3c0dc10e0fd809d2e1fff30f021f9c1bf745c5eb90598"),
      "tue5": ("tue_art5.xhtml", "371423cfa765c569bbb6980157ce5c9945036272d8e7662f7a3e531a90645840", "arttue5.xhtml", "9e7aa733135dca312cc36463c60c7ebb92f5c41e484da9d70abd5f90b4c07afe"),
      "tue16": ("tue_art16.xhtml", "9a2b31eca99ed0cbd3948a331d2351cfa3022576eb88df85281c04a7fdf842c0", "arttue16.xhtml", "4fc20ceebf6057fd31bcda4d8df15c1564ff6a6b0c79ccc485ab7a77b719691a"),
      "tue17": ("tue_art17.xhtml", "231d8d634374156305785afdee695ad752c9511176ba8a32adca919b32f77ab7", "arttue17.xhtml", "63c761bbefbe368ac5b7b1580f97eb3d7b67031cadabb781b3ddf524a1900ae3"),
      "2": ("art2.xhtml", "ebca98d73eaaa34ed97dca66b944c959d32b2673302c9b85d6ebb0e4ac273095", "art2.xhtml", "b53b68d7e26334a6a9f57cfee091334d8982acf30acd312371a62c1e872d4900"),
      "18": ("art18.xhtml", "81ab9448c1054a782c1926aca2aaa7092e6a61c9ea0b4fa4f398103ff68bea30", "art18.xhtml", "521e7f96d80e6f4c303b1e9d3dbbd7f7f2773046ec39aa55550bde491e96cfee"),
      "76": ("art76.xhtml", "db75f76bef826e105693969a0c143c476e4cc6c83dff4a086d322f81fb98452c", "art76.xhtml", "0677c31ea628a8f5f9b3193d0678b11e1c6426390a5886cc8525fd7fdf836a39"),
      "238": ("art238.xhtml", "d18f3cd348e29df43b1da824d62da8b864a67d0f20cd67a1dbe4b3c68744f745", "art238.xhtml", "cf62de7ef4b9dd33f9b2680c83af3169010c92c43a2cc89616ffefb7860cde1b"),
      "241": ("art241.xhtml", "0ed6d4fc6337a47e6f1b67125291946c335c6a33f15858b3680db2be283af08f", "art241.xhtml", "1c6f09b862030de0e7b974d18826262f849378a5d8f9f45a176664931efd0f2a"),
      "293": ("art293.xhtml", "66ff550ab458457690c3a6d6f4bc5703ba633bc91adcc86def55c84abf57852a", "art293.xhtml", "02abc65c92b2fca7695c21b29b34f887b4caf49ea5a4befd81ed9789aff7902a"),
      "294": ("art294.xhtml", "008fd767d317c9cd77b7d1e8a994dd0e005a68e28af3aee8bc46ace5d100bab3", "art294.xhtml", "f28e77b2eb8a2d684aa8ef5d561da0d02bc6fb27187c3b24684c8f8e4cf68d3e"),
      "tue15": ("tue_art15.xhtml", "fc407122bc62cbb556b24078ab925299abc9b002fefc4ef97e3a36d1978ca36e", "arttue15.xhtml", "fe12a3e23407f7ad895b55cb9265e482975e127d94fa493f23fd19e646de56a6"),
      "288": ("art288.xhtml", "2b8a537515a628443be5144133bc98ab1fd0cf8f6130e853405efa078c655838", "art288.xhtml", "ef4f449b6aca9f1a85211972a6a24dc2bd70c65ea097d7a97b18a46717d160ec"),
      "p36": ("protocole36.xhtml", "a8acc5216ac00e3fd81433d03677284686ee3d8492d6b606546671b876a39ba4", "protocol36.xhtml", "51608d1fd040ea38f7e85f80075c5083e98ebfd9c3c7511030c514c9bccc1265")}
CITS = {
    "cit_tue4_1": ("tue4", "toute compétence non attribuée à l'Union dans les traités appartient aux États membres",
                   "competences not conferred upon the Union in the Treaties remain with the Member States"),
    "cit_tue5_2": ("tue5", "l'Union n'agit que dans les limites des compétences que les États membres lui ont attribuées dans les traités pour atteindre les objectifs que ces traités établissent",
                   "the Union shall act only within the limits of the competences conferred upon it by the Member States in the Treaties to attain the objectives set out therein"),
    "cit_tue4_2": ("tue4", "la sécurité nationale reste de la seule responsabilité de chaque État membre",
                   "national security remains the sole responsibility of each Member State"),
    "cit_tue4_3": ("tue4", "Les États membres prennent toute mesure générale ou particulière propre à assurer l'exécution des obligations découlant des traités ou résultant des actes des institutions de l'Union",
                   "The Member States shall take any appropriate measure, general or particular, to ensure fulfilment of the obligations arising out of the Treaties or resulting from the acts of the institutions of the Union"),
    "cit_18": ("18", "Dans le domaine d'application des traités, et sans préjudice des dispositions particulières qu'ils prévoient, est interdite toute discrimination exercée en raison de la nationalité",
               "Within the scope of application of the Treaties, and without prejudice to any special provisions contained therein, any discrimination on grounds of nationality shall be prohibited"),
    "cit_2_5b": ("2", "ne peuvent pas comporter d'harmonisation des dispositions législatives et réglementaires des États membres",
                 "shall not entail harmonisation of Member States' laws or regulations"),
    "cit_17_2": ("tue17", "Un acte législatif de l'Union ne peut être adopté que sur proposition de la Commission, sauf dans les cas où les traités en disposent autrement",
                 "Union legislative acts may only be adopted on the basis of a Commission proposal, except where the Treaties provide otherwise"),
    "cit_294_2": ("294", "La Commission présente une proposition au Parlement européen et au Conseil",
                  "The Commission shall submit a proposal to the European Parliament and the Council"),
    "cit_241": ("241", "Si la Commission ne soumet pas de proposition, elle en communique les raisons au Conseil",
                "If the Commission does not submit a proposal, it shall inform the Council of the reasons"),
    "cit_76": ("76", "sur initiative d'un quart des États membres", "on the initiative of a quarter of the Member States"),
    "cit_293_1": ("293", "le Conseil ne peut amender la proposition que statuant à l'unanimité, sauf dans les cas visés à l'article 294, paragraphes 10 et 13, aux articles 310, 312, 314 et à l'article 315, deuxième alinéa",
                  "it may amend that proposal only by acting unanimously, except in the cases referred to in paragraphs 10 and 13 of Article 294, in Articles 310, 312 and 314 and in the second paragraph of Article 315"),
    "cit_293_2": ("293", "Tant que le Conseil n'a pas statué, la Commission peut modifier sa proposition tout au long des procédures conduisant à l'adoption d'un acte de l'Union",
                  "As long as the Council has not acted, the Commission may alter its proposal at any time during the procedures leading to the adoption of a Union act"),
    "cit_238_4": ("238", "Les abstentions des membres présents ou représentés ne font pas obstacle à l'adoption des délibérations du Conseil qui requièrent l'unanimité",
                  "Abstentions by Members present in person or represented shall not prevent the adoption by the Council of acts which require unanimity"),
    "cit_16_4": ("tue16", "au moins 55 % des membres du Conseil, comprenant au moins quinze d'entre eux et représentant des États membres réunissant au moins 65 % de la population de l'Union",
                 "at least 55 % of the members of the Council, comprising at least fifteen of them and representing Member States comprising at least 65 % of the population of the Union"),
    "cit_tue15": ("tue15", "Il n'exerce pas de fonction législative", "It shall not exercise legislative functions"),
    "cit_16_7": ("tue16", "Un comité des représentants permanents des gouvernements des États membres est responsable de la préparation des travaux du Conseil",
                 "A Committee of Permanent Representatives of the Governments of the Member States shall be responsible for preparing the work of the Council"),
    "cit_288": ("288", "La directive lie tout État membre destinataire quant au résultat à atteindre, tout en laissant aux instances nationales la compétence quant à la forme et aux moyens",
                "A directive shall be binding, as to the result to be achieved, upon each Member State to which it is addressed, but shall leave to the national authorities the choice of form and methods"),
    "cit_238_2": ("238", "au moins 72 % des membres du Conseil, représentant des États membres réunissant au moins 65 % de la population de l'Union",
                  "at least 72 % of the members of the Council, representing Member States comprising at least 65 % of the population of the Union"),
}
# Protocole n° 36 : phrases non citées mais relues (la page les résume ; elles doivent rester dans le texte archivé).
P36_LU = {"fr": ["Jusqu'au 31 octobre 2014, les dispositions suivantes sont en vigueur", "les voix des membres sont affectées de la pondération suivante",
                 "Entre le 1 er novembre 2014 et le 31 mars 2017, lorsqu'une délibération doit être prise à la majorité qualifiée, un membre du Conseil peut demander"],
          "en": ["Until 31 October 2014, the following provisions shall remain in force", "members' votes shall be weighted as follows",
                 "Between 1 November 2014 and 31 March 2017, when an act is to be adopted by qualified majority, a member of the Council may request"]}
# Passe B3 (12/10/2026) : phrases que la page résume sans les citer (TFUE 238, § 3 ; TFUE 168, § 4, français seulement :
# le traité complet archivé est l'expression française du JO C 202, l'anglais de l'art. 168 n'est pas archivé) et la
# citation anglaise du TUE, art. 16, § 4 (TUE16_EN, jusqu'ici servie sans relecture). Chacune doit rester dans le texte
# archivé, sinon U6 arrête. Condition de mort : la page ne mentionne plus la règle des États participants ni l'art. 168.
JO_COMPLET = (TFUE_DIR / "jo_c202_2016_complet.xhtml", "4db565fae7fc3d23be314fd341e0d11917bf7aae4716d7107f48fc5f777bf8fe")
B3_LU = {("238", "fr"): ["dans les cas où, en application des traités, tous les membres du Conseil ne prennent pas part au vote",
                         "au moins 55 % des membres du Conseil représentant les États membres participants",
                         "plus de 35 % de la population des États membres participants, plus un membre"],
         ("238", "en"): ["in cases where, under the Treaties, not all the members of the Council participate in voting",
                         "at least 55 % of the members of the Council representing the participating Member States",
                         "more than 35 % of the population of the participating Member States, plus one member"],
         ("tue16", "en"): ["A blocking minority must include at least four Council members"],
         ("jo", "fr"): ["Par dérogation à l'article 2, paragraphe 5, et à l'article 6, point a), et conformément à l'article 4, paragraphe 2, point k)",
                        "des mesures fixant des normes élevées de qualité et de sécurité des organes et substances d'origine humaine, du sang et des dérivés du sang",
                        "des mesures fixant des normes élevées de qualité et de sécurité des médicaments et des dispositifs à usage médical"]}
# --- C2 (07/10/2026, contre-expertise PRO-20261007-102607) : publications de la SWP qui chiffraient déjà les votes de la
# France. Citées mot pour mot (garde U7 sur le texte des PDF archivés), nos décomptes posés à côté sur la même fenêtre.
PUB_SWP = RECH / "sondes" / "europe" / "publications_swp"
SWP_PUBS = {
    "swp21": ("SWP_WP5_2021-12_Mintel_vonOndarza_Consensus_per_video.pdf",
              "c3310458f4fff66f5d8c62c3edd39596b9d7ceb5495d4361487d5d4fb83fe234",
              "France has only been outvoted once and abstained twice in all public votes since 2010", "2010-01-01", "2021-12-31"),
    "swp24": ("SWP_Comment_2024-16_vonOndarza_Stuerzer.pdf",
              "b8efc2ea800f45c8d18f48e9e5979694b591ad6dc0bca07a8637331174e0bd9d",
              "France, which was only outvoted five times in the entire observation period", "2010-01-01", "2023-09-30"),
}
POLIDORI = ("Polidori_2014_Unanimity_Lisbon_Eurostudium3w.pdf",
            "ad05d58bb183f9b5fd23b151df5cf189d0fd9838dad577cda087dc444eea5e16",
            "are 68 (13 as to TEU; 55 as to TFEU)")  # C4 : autre périmètre (Conseil européen compris), pas un témoin
SWP24_ANNONCE = 5  # « five times », lu dans la citation ci-dessus (la garde vérifie le mot)


def verifier_swp() -> tuple[str, dict]:
    import fitz
    vals = {}
    for k, (f, sha, cit, deb, fin) in SWP_PUBS.items():
        p = PUB_SWP / f
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != sha:
            raise Arret("U7 : publication SWP absente ou modifiée (%s)" % f)
        t = re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in fitz.open(p))).replace("- ", "")
        if cit not in t:
            raise Arret("U7 : citation introuvable dans %s : %s" % (f, cit))
        sel = [a for a in FR_ACTES if deb <= a[0] <= fin]
        vals[k] = {"contre": sum(a[1] == "contre" for a in sel), "abst": sum(a[1] == "abstention" for a in sel)}
    if (vals["swp21"]["contre"], vals["swp21"]["abst"]) != (1, 2) or "once and abstained twice" not in SWP_PUBS["swp21"][2]:
        raise Arret("U7 : la phrase de 2021 (« once », « twice ») ne correspond plus au relevé 2010-2021 : %s" % vals["swp21"])
    if "five times" not in SWP_PUBS["swp24"][2]:
        raise Arret("U7 : le nombre annoncé par la SWP en 2024 ne se lit plus dans la citation")
    ecart = SWP24_ANNONCE - (vals["swp24"]["contre"] + vals["swp24"]["abst"])
    if ecart != -ECARTS_EXPLIQUES[("FR", 0)]:
        raise Arret("U7 : écart SWP 2024 (%d) différent des deux entrées SWP écartées (%d)" % (ecart, -ECARTS_EXPLIQUES[("FR", 0)]))
    p = PUB_SWP / POLIDORI[0]
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != POLIDORI[1]:
        raise Arret("U7 : inventaire de 2014 absent ou modifié")
    if POLIDORI[2] not in re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in fitz.open(p))):
        raise Arret("U7 : le compte de l'inventaire de 2014 ne se lit plus dans le PDF")
    vals["polidori_tfue"] = re.search(r"(\d+) as to TFEU", POLIDORI[2]).group(1)
    return "U7 : citations SWP 2021 et 2024 retrouvées ; écart 2024 égal aux entrées écartées (%d)" % ecart, vals


# ------------------------------------------------------------------ U6 : citations des traités ajoutées en phase B
def texte_archive(p: Path, sha: str, garde: str) -> str:
    """Texte d'un fichier archivé (XHTML ou HTML), empreinte vérifiée ; balises retirées, espaces normalisés
    (l'espace insécable du JO devient une espace : « 55 % »)."""
    if not p.is_file():
        raise Arret("%s : fichier archivé absent (%s)" % (garde, p))
    b = p.read_bytes()
    if hashlib.sha256(b).hexdigest() != sha:
        raise Arret("%s : empreinte changée (%s)" % (garde, p.name))
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b.decode("utf-8"))))


def textes_traite() -> dict:
    out = {}
    for k, (ffr, sfr, fen, sen) in _F.items():
        out[(k, "fr")] = texte_archive(TFUE_DIR / ffr, sfr, "U6")
        out[(k, "en")] = texte_archive(TFUE_DIR / "en" / fen, sen, "U6")
    out[("jo", "fr")] = texte_archive(JO_COMPLET[0], JO_COMPLET[1], "U6")
    return out


def citations_traite(tx: dict, cits: dict = None, lu: dict = None) -> tuple[dict, dict]:
    """Chaque phrase citée par la page, retrouvée mot pour mot dans le texte archivé, FR et EN ; sinon arrêt."""
    cits = CITS if cits is None else cits
    A, E = {}, {}
    for cle, (f, pfr, pen) in cits.items():
        for lang, p, d in (("fr", pfr, A), ("en", pen, E)):
            if p not in tx[(f, lang)]:
                raise Arret("U6 : citation %s (%s) introuvable dans le texte archivé : %s" % (cle, lang, p[:60]))
            d[cle] = p.replace(" %", " %") if lang == "fr" else p.replace(" %", "%")
    for lang in ("fr", "en"):
        for p in P36_LU[lang]:
            if p not in tx[("p36", lang)]:
                raise Arret("U6 : protocole n° 36 (%s), phrase introuvable : %s" % (lang, p[:60]))
    if "1 er novembre 2014" not in tx[("tue16", "fr")] or "31 mars 2017" not in tx[("tue16", "fr")]:
        raise Arret("U6 : TUE, art. 16 : dates de la transition introuvables")
    for (f, lang), phrases in (B3_LU if lu is None else lu).items():
        for p in phrases:
            if p not in tx[(f, lang)]:
                raise Arret("U6 : %s (%s), phrase résumée par la page introuvable : %s" % (f, lang, p[:60]))
    return A, E


# ------------------------------------------------------------------ U8 : les cinq actes, relus dans les pièces archivées
def membres(d: str) -> int:
    """États membres à la date d'un vote : 28 du 1er juillet 2013 au 31 janvier 2020, 27 sinon dans le relevé."""
    return 28 if "2013-07-01" <= d <= "2020-01-31" else 27


def controler_composition(st: str, cpt: tuple, pos: str, compo: dict) -> dict:
    """U8, passe B3 : composition transcrite = comptes transcrits, France à sa place, et = pictogrammes lus dans l'annexe."""
    etats = [e for col in ORDRE_CONSEIL for e in col]
    autres = set(compo["contre"]) | set(compo["abstention"]) | set(compo["np"])
    if len(autres) != len(compo["contre"]) + len(compo["abstention"]) + len(compo["np"]) or not autres <= set(etats):
        raise Arret("U8 : %s : composition transcrite incohérente (doublon ou État inconnu)" % st)
    trans = {e: ("contre" if e in compo["contre"] else "abstention" if e in compo["abstention"] else "np" if e in compo["np"] else "pour")
             for e in etats}
    comptes = tuple(sum(v == k for v in trans.values()) for k in ("pour", "contre", "abstention", "np"))
    if comptes != cpt:
        raise Arret("U8 : %s : composition transcrite %s, décompte transcrit %s" % (st, comptes, cpt))
    if trans["FR"] != pos:
        raise Arret("U8 : %s : la France est « %s » dans la composition, « %s » dans l'acte" % (st, trans["FR"], pos))
    lu = lire_annexe(CONSEIL_DIR / (st + ".pdf"))
    ecarts = ["%s transcrit %s, lu %s" % (e, trans[e], lu[e]) for e in etats if trans[e] != lu[e]]
    if ecarts:
        raise Arret("U8 : %s : composition État par État contredite par l'annexe : %s" % (st, "; ".join(ecarts)))
    return trans


def controler_actes(actes: list, sw_rows: list, composition: dict = None) -> list[dict]:
    import fitz
    composition = COMPOSITION if composition is None else composition
    res = []
    for (vote, pos, tfr, ten, cpt, st, celex, afr, aen, dacte, proc) in actes:
        if sum(cpt) != membres(vote):
            raise Arret("U8 : %s : décompte %s ne totalise pas %d États" % (vote, cpt, membres(vote)))
        if cpt[{"contre": 1, "abstention": 2}[pos]] < 1:
            raise Arret("U8 : %s : la position de la France (%s) est absente du décompte" % (vote, pos))
        p = CONSEIL_DIR / (st + ".pdf")
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != CONSEIL_SHA[st]:
            raise Arret("U8 : note du Conseil %s absente ou modifiée" % st)
        t = re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in fitz.open(p)))
        a, m, j = vote.split("-")
        if "Voting result" not in t or proc not in t or ("%d %s %s" % (int(j), MOIS_EN[int(m)], a)) not in t:
            raise Arret("U8 : note %s : « Voting result », procédure %s ou date du vote introuvable" % (st, proc))
        sfr, sen = ACTES_SHA[celex]
        xfr = texte_archive(ACTES_DIR / (celex + "_fra.html"), sfr, "U8").replace("1 er ", "1er ")
        xen = texte_archive(ACTES_DIR / (celex + "_eng.html"), sen, "U8")
        num = re.findall(r"\d{4}/\d+|\d+/\d{4}", aen)[-1]
        if num not in xfr or num not in xen:
            raise Arret("U8 : %s : numéro de l'acte %s introuvable" % (celex, num))
        if ("du %s" % date_fr(dacte)) not in xfr or ("of %s" % date_en(dacte)) not in xen:
            raise Arret("U8 : %s : date de l'acte %s introuvable" % (celex, dacte))
        if ("décision du Conseil du %s" % date_fr(vote)) not in xfr or ("decision of the Council of %s" % date_en(vote)) not in xen:
            raise Arret("U8 : %s : « décision du Conseil du %s » introuvable dans l'acte publié" % (celex, date_fr(vote)))
        temoin = None
        if vote <= FIN_TEMOIN:
            cand = [r for r in sw_rows if r["decisionDate"] == vote and "FR" in (
                (r["countryCodeAgainstGrouped"] or "") + "|" + (r["countryCodeAbstainedGrouped"] or "")).split("|")]
            if len(cand) != 1:
                raise Arret("U8 : %s : %d entrées SWP pour la France ce jour-là (1 attendue)" % (vote, len(cand)))
            r = cand[0]
            n = lambda k: len([c for c in (r[k] or "").split("|") if c and c != "NA"])  # noqa: E731
            temoin = (n("countryCodeInFavourGrouped"), n("countryCodeAgainstGrouped"), n("countryCodeAbstainedGrouped"),
                      n("countryCodeNotParticipatingGrouped"))
            if temoin != cpt:
                raise Arret("U8 : %s : décompte transcrit %s, jeu SWP %s" % (vote, cpt, temoin))
        elif st not in composition:
            raise Arret("U8 : %s : vote sans second jeu et sans composition État par État transcrite" % vote)
        if st in composition:
            controler_composition(st, cpt, pos, composition[st])
        res.append({"vote": vote, "temoin": temoin is not None, "pondere": vote < DEBUT_DOUBLE_MAJORITE,
                    "composition": st in composition})
    return res


# ------------------------------------------------------------------ U9 : garde de prose (pages FR et EN, jetons résolus)
PAGE_FR = ROOT / "content" / "ce-que-la-france-peut-decider-dans-l-union-europeenne" / "_index.md"
PAGE_EN = PAGE_FR.with_name("_index.en.md")


def resoudre(src: str, d: dict) -> str:
    """Texte de la page avec ses jetons remplacés par leurs valeurs (corps et front matter) ; balises et entités ôtées."""
    s = re.sub(r'\{\{<\s*ue-val\s+"([a-z_0-9]+)"\s*>\}\}', lambda m: str(d.get(m.group(1), "")), src)
    s = re.sub(r"\{ue\.([a-z_0-9]+)\}", lambda m: str(d.get(m.group(1), "")), s)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)).replace(" ", " ")
    return re.sub(r"[ \t]+", " ", s)


INTERDITS = {"fr": [(r"(?:moins|plus) souvent que", "classement verbal")],
             "en": [(r"(?:less|more) often than", "verbal ranking")]}


def garde_prose(textes: dict, fr_np: int) -> list[str]:
    """textes : {"fr": texte résolu, "en": texte résolu}. Rend la liste des fautes ; vide = conforme.
    1. « amender … unanimité » jamais sans « sauf » (« except ») dans la même phrase (art. 293, § 1 : exceptions) ;
    2. aucune formule de classement verbal entre États (fiche U, clause « sans classement verbal ») ;
    3. « pour dans tous les autres cas » suppose que la France n'a jamais été non participante (fr_np = 0)."""
    fautes = []
    for lang, t in textes.items():
        for ph in re.split(r"(?<=[.;!?])\s+|\n+", t):
            if lang == "fr" and re.search(r"amend\w*[^.;]*unanimit", ph, re.I) and "sauf" not in ph:
                fautes.append("fr : « amender … unanimité » sans « sauf » : %s" % ph.strip()[:90])
            if lang == "en" and re.search(r"amend\w*[^.;]*unanim", ph, re.I) and "except" not in ph:
                fautes.append("en : 'amend … unanimously' without 'except': %s" % ph.strip()[:90])
        for rx, motif in INTERDITS[lang]:
            if re.search(rx, t, re.I):
                fautes.append("%s : %s (%s)" % (lang, motif, re.search(rx, t, re.I).group(0)))
        tous = {"fr": "pour dans tous les autres cas", "en": "in favour in every other case"}[lang]
        if tous in t and fr_np != 0:
            fautes.append("%s : « %s » alors que la France a %d non-participation(s)" % (lang, tous, fr_np))
    return fautes


NOMS = {"AT": ("Autriche", "Austria"), "BE": ("Belgique", "Belgium"), "BG": ("Bulgarie", "Bulgaria"), "CY": ("Chypre", "Cyprus"),
        "CZ": ("Tchéquie", "Czechia"), "DE": ("Allemagne", "Germany"), "DK": ("Danemark", "Denmark"), "EE": ("Estonie", "Estonia"),
        "EL": ("Grèce", "Greece"), "ES": ("Espagne", "Spain"), "FI": ("Finlande", "Finland"), "FR": ("France", "France"),
        "HR": ("Croatie", "Croatia"), "HU": ("Hongrie", "Hungary"), "IE": ("Irlande", "Ireland"), "IT": ("Italie", "Italy"),
        "LT": ("Lituanie", "Lithuania"), "LU": ("Luxembourg", "Luxembourg"), "LV": ("Lettonie", "Latvia"), "MT": ("Malte", "Malta"),
        "NL": ("Pays-Bas", "Netherlands"), "PL": ("Pologne", "Poland"), "PT": ("Portugal", "Portugal"), "RO": ("Roumanie", "Romania"),
        "SE": ("Suède", "Sweden"), "SI": ("Slovénie", "Slovenia"), "SK": ("Slovaquie", "Slovakia"), "UK": ("Royaume-Uni", "United Kingdom")}
MOIS_FR = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
CH_FR = {0: "aucune fois", 1: "une fois", 2: "deux fois", 3: "trois fois", 4: "quatre fois", 5: "cinq fois"}
CH_EN = {0: "never", 1: "once", 2: "twice", 3: "three times", 4: "four times", 5: "five times"}


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


# ------------------------------------------------------------------ U-E1, U-E2 (fonctions des tests décisifs)
def typologie() -> dict:
    s = ue1.lire()
    err = ue1.verifier(s)
    if err:
        raise Arret("U1 : %s" % err[0])
    return s


def bases() -> dict:
    _, rel = ue2.lire()
    q, nc = ue2.qualifier(rel)
    if nc:
        raise Arret("U2 : unités non classées %s" % nc)
    plo = {x["unite"] for x in q if x["plo"] == "base"} | {u for u, v in ue2.RENVOI_PLO.items() if v[0] == "base"}
    cond = set(ue2.CONDITIONNEL_PLO) | {u for u, v in ue2.RENVOI_PLO.items() if v[0] == "conditionnel"}
    una = {x["unite"] for x in q if x["una_q"] == "base"}
    seul_nous, seul_tem = ue2.comparer(plo | cond, ue2.temoin())
    if seul_nous or seul_tem:
        raise Arret("U2 : écart au témoin du Conseil (%s / %s)" % (seul_nous, seul_tem))
    art = lambda S: len({u.split(",")[0].split("(")[0] for u in S})  # noqa: E731
    return {"plo": sorted(plo), "cond": sorted(cond), "una": sorted(una), "plo_art": art(plo), "una_art": art(una),
            "mixtes": sorted(plo & una), "ecartes_plo": len(ue2.ECARTS_PLO), "ecartes_una": len(ue2.ECARTS_UNA),
            "temoin": len(ue2.temoin()), "q": {x["unite"]: (x["plo"], x["una_q"]) for x in q}}


# ------------------------------------------------------------------ U-E3
def swp_fenetre() -> dict:
    if not SWP.is_file():
        raise Arret("U3 : jeu SWP absent (%s)" % SWP)
    out = {k: [0, 0] for k in NOMS}
    for r in csv.DictReader(open(SWP, encoding="utf-8")):
        for i, k in enumerate(("countryCodeAgainstGrouped", "countryCodeAbstainedGrouped")):
            for c in (r[k] or "").split("|"):
                if c and c != "NA":
                    out[c][i] += 1
    return {k: tuple(v) for k, v in out.items()}


def temoin_votes(fen: dict, sw: dict) -> list[str]:
    ecarts = []
    for c in NOMS:
        for i in (0, 1):
            d = fen.get(c, (0, 0))[i] - sw.get(c, (0, 0))[i]
            if d != ECARTS_EXPLIQUES.get((c, i), 0):
                ecarts.append("%s %s : relevé %d, SWP %d" % (c, ("contre", "abstention")[i], fen.get(c, (0, 0))[i], sw.get(c, (0, 0))[i]))
    return ecarts


def votes(tout: dict, fen: dict, sw: dict) -> dict:
    e = temoin_votes(fen, sw)
    if e:
        raise Arret("U3 : écart non expliqué au témoin SWP : %s" % "; ".join(e[:3]))
    fr_c, fr_a, fr_n = tout["FR"]
    if (fr_c, fr_a) != (sum(1 for a in FR_ACTES if a[1] == "contre"), sum(1 for a in FR_ACTES if a[1] == "abstention")):
        raise Arret("U4 : la liste des actes de la France ne correspond pas aux comptes")
    ident = sum(1 for c in NOMS if fen.get(c) == sw.get(c))
    return {"etats_identiques": ident, "fr_contre": fr_c, "fr_abst": fr_a, "fr_np": fr_n,
            "fr_pour": RELEVE["entrees"] - fr_c - fr_a - fr_n}


# ------------------------------------------------------------------ figures
W = 720
BLEU, GRIS, GRIS_CLAIR = "#184f95", "#8a8f98", "#c9cdd3"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LANG = "fr"
T = {
    "fr": {"t": "Nombre brut de votes contre et d'abstentions — durées et champs de participation différents",
           "s": "par État membre, votes publics du Conseil de l'UE sur des actes législatifs, du {debut} au {fin}",
           "d": "Barres horizontales par État membre, triées par total : votes contre (foncé) et abstentions (clair). {liste}. Sur {entrees} votes publiés.",
           "src": "Conseil de l'UE, recherche des résultats de vote (relevé du {releve}) ; contrôle : SWP / GESIS, doi 10.7802/2560, du {debut} au {fin_temoin}",
           "note": "Comptes bruts, pas un classement d'influence : Royaume-Uni jusqu'à son retrait (2020), Croatie depuis son adhésion (2013) ; le Danemark et l'Irlande ne participent pas à certains actes.",
           "contre": "contre", "abst": "abstention", "etat": "{nom} : {c} contre, {a} abstention{s}"},
    "en": {"t": "Raw number of votes against and abstentions — different lengths of membership and fields of participation",
           "s": "by Member State, public votes of the Council of the EU on legislative acts, {debut} to {fin}",
           "d": "Horizontal bars by Member State, sorted by total: votes against (dark) and abstentions (light). {liste}. Out of {entrees} published votes.",
           "src": "Council of the EU, voting results search (retrieved {releve}); check: SWP / GESIS, doi 10.7802/2560, {debut} to {fin_temoin}",
           "note": "Raw counts, not a ranking of influence: United Kingdom until its withdrawal (2020), Croatia since its accession (2013); Denmark and Ireland do not take part in some acts.",
           "contre": "against", "abst": "abstention", "etat": "{nom}: {c} against, {a} abstention{s}"},
}


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def _ordre(tout: dict) -> list[str]:
    return sorted(NOMS, key=lambda c: (-(tout[c][0] + tout[c][1]), NOMS[c][0]))


def _desc(tout: dict, A: dict) -> str:
    L = T[LANG]
    liste = "; ".join(L["etat"].format(nom=NOMS[c][0 if LANG == "fr" else 1], c=tout[c][0], a=tout[c][1],
                                       s="" if tout[c][1] < 2 else "s") for c in _ordre(tout))
    return L["d"].format(liste=liste, **A)


def _pied_blocs(A: dict) -> list:
    L = T[LANG]
    return [(L["src"].format(**A), INK2, "pied-source"), (L["note"], INK2, "pied-note"), (LICENCES[LANG], MUTED, "pied-licence")]


def fig_votes(tout: dict, A: dict) -> str:
    L = T[LANG]
    ordre = _ordre(tout)
    hb, gap = 15, 4
    titre = pf.coupe(L["t"], 92)
    y_s = 18 + 18 * len(titre)
    y_leg = y_s + 12
    y0 = y_leg + 24
    H = y0 + len(ordre) * (hb + gap) + 6
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="ev-t ev-d" font-family="%s">' % (W, H, FONT),
         '<title id="ev-t">%s</title><desc id="ev-d">%s</desc>' % (esc(L["t"]), esc(_desc(tout, A))),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)]
    for k, l in enumerate(titre):
        e.append(txt(0, 18 + 18 * k, l, 14, INK, weight="600"))
    e.append(txt(0, y_s, L["s"].format(**A), 12, INK2))
    x0, wmax = 130, 520
    vmax = max(tout[c][0] + tout[c][1] for c in ordre)
    e.append('<rect x="%d" y="%d" width="12" height="10" fill="%s"/>' % (x0, y_leg, INK2))
    e.append(txt(x0 + 16, y_leg + 9, L["contre"], 11, INK2))
    e.append('<rect x="%d" y="%d" width="12" height="10" fill="%s"/>' % (x0 + 90, y_leg, GRIS_CLAIR))
    e.append(txt(x0 + 106, y_leg + 9, L["abst"], 11, INK2))
    for k, c in enumerate(ordre):
        y = y0 + k * (hb + gap)
        contre, abst, _ = tout[c]
        estfr = c == "FR"
        col = BLEU if estfr else INK2
        nom = NOMS[c][0 if LANG == "fr" else 1]
        e.append(txt(x0 - 8, y + 11, nom, 11, INK if estfr else INK2, "end", "600" if estfr else None))
        wc, wa = wmax * contre / vmax, wmax * abst / vmax
        e.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0, y, wc, hb, col))
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0 + wc, y, wa, hb, "#9db5d8" if estfr else GRIS_CLAIR))
        e.append(txt(x0 + wc + wa + 6, y + 11, "%d · %d" % (contre, abst), 10, INK if estfr else MUTED, "start", "600" if estfr else None))
    return pf.pied(e, H + 2, W, _pied_blocs(A), GRID)


def fig_votes_m(tout: dict, A: dict) -> str:
    """Version téléphone (300 de large, police jamais sous 13,5) : une ligne par État, nom, barre et nombres."""
    L = T[LANG]
    e, y = pf.tete_mobile("evm", L["t"], _desc(tout, A), INK, FONT, 30)
    for l in pf.coupe(L["s"].format(**A), 36):
        y += 18
        e.append('<text x="0" y="%d" font-size="13.5" fill="%s">%s</text>' % (y, INK2, esc(l)))
    y += 12
    e.append('<rect x="0" y="%d" width="12" height="12" fill="%s"/>' % (y, INK2))
    e.append('<text x="17" y="%d" font-size="13.5" fill="%s">%s</text>' % (y + 11, INK2, esc(L["contre"])))
    e.append('<rect x="110" y="%d" width="12" height="12" fill="%s"/>' % (y, GRIS_CLAIR))
    e.append('<text x="127" y="%d" font-size="13.5" fill="%s">%s</text>' % (y + 11, INK2, esc(L["abst"])))
    y += 22
    ordre = _ordre(tout)
    vmax = max(tout[c][0] + tout[c][1] for c in ordre)
    x0, wmax = 112, 118
    for c in ordre:
        contre, abst, _ = tout[c]
        estfr = c == "FR"
        nom = NOMS[c][0 if LANG == "fr" else 1]
        e.append('<text x="%d" y="%d" font-size="13.5" fill="%s" text-anchor="end"%s>%s</text>'
                 % (x0 - 6, y + 13, INK if estfr else INK2, ' font-weight="600"' if estfr else "", esc(nom)))
        wc, wa = wmax * contre / vmax, wmax * abst / vmax
        e.append('<rect x="%d" y="%d" width="%.1f" height="14" fill="%s"/>' % (x0, y + 2, wc, BLEU if estfr else INK2))
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="14" fill="%s"/>' % (x0 + wc, y + 2, wa, "#9db5d8" if estfr else GRIS_CLAIR))
        e.append('<text x="%.1f" y="%d" font-size="13.5" fill="%s"%s>%s</text>'
                 % (x0 + wc + wa + 5, y + 13, INK if estfr else MUTED, ' font-weight="600"' if estfr else "", esc("%d · %d" % (contre, abst))))
        y += 21
    blocs = _pied_blocs(A)
    blocs[-1] = (LICENCES[LANG].split(" · ")[0] + " · stephane-lalut.com", MUTED, "pied-licence")  # l'URL longue ne se coupe pas a 300
    return pf.pied_mobile(e, y + 6, blocs, GRID)


# ------------------------------------------------------------------ affichage
TUE16 = (RECH / "sondes" / "europe" / "tfue" / "tue_art16.xhtml", "9a2b31eca99ed0cbd3948a331d2351cfa3022576eb88df85281c04a7fdf842c0",
         "Une minorité de blocage doit inclure au moins quatre membres du Conseil")


def citation_tue16() -> str:
    """TUE, art. 16, § 4 (XHTML de Cellar, empreinte vérifiée) : la phrase citée par la page, mot pour mot."""
    import hashlib
    b = TUE16[0].read_bytes()
    if hashlib.sha256(b).hexdigest() != TUE16[1]:
        raise Arret("U2 : empreinte du TUE, art. 16, changée")
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b.decode("utf-8"))))
    if TUE16[2] not in t:
        raise Arret("U2 : citation du TUE, art. 16, § 4, introuvable")
    return TUE16[2]


# Texte anglais officiel du TFUE et du TUE (même JO C 202, expression anglaise de Cellar, téléchargée le 06/10/2026).
EN_DIR = RECH / "sondes" / "europe" / "tfue" / "en"
EN_SHA = {"2": "b53b68d7e26334a6a9f57cfee091334d8982acf30acd312371a62c1e872d4900",
          "3": "2a579b28498f2f4520f374c3aba5dc8a8aee4b04bc1c34451f358bf2ff9d5faf",
          "4": "56392afb9746318b086731d8bb1ec51ce88939b2dbdf6f41839b72a2e9fba440",
          "5": "1a52a53bbe83d2f2075f46cf4729e4582d569d58ba67d14c74728bc0d361a576",
          "6": "c26a6161fd8c60d02b12cc190643ac5da233f453591569f2ecf60f34338cade3",
          "tue16": "4fc20ceebf6057fd31bcda4d8df15c1564ff6a6b0c79ccc485ab7a77b719691a"}
TUE16_EN = "A blocking minority must include at least four Council members"


def paragraphes_en(art: str) -> list[str]:
    import hashlib
    b = (EN_DIR / ("art%s.xhtml" % art)).read_bytes()
    if hashlib.sha256(b).hexdigest() != EN_SHA[art]:
        raise Arret("U1 : empreinte du texte anglais, art. %s, changée" % art)
    x = b.decode("utf-8")
    return [ue1.normal(html.unescape(re.sub(r"<[^>]+>", "", p))) for p in re.findall(r'<p class="normal">(.*?)</p>', x, re.S)]


def typologie_en(typ: dict) -> dict:
    """Mêmes listes, même nombre de domaines, mêmes lettres que le texte français ; sinon arrêt."""
    out = {"listes": [], "paragraphes": {}}
    for l in typ["listes"]:
        ps = paragraphes_en(l["article"])
        debut = 0 if l["paragraphe"] is None else next(i for i, p in enumerate(ps) if p.startswith(l["paragraphe"] + ". "))
        items, i = [], debut + 1
        while i + 1 < len(ps) and re.fullmatch(r"\(?[a-z]\)", ps[i]):  # « (a) » en anglais, « a) » en français
            items.append(ps[i + 1])
            i += 2
        if len(items) != len(l["domaines"]):
            raise Arret("U1 : art. %s, %d domaines en anglais pour %d en français" % (l["article"], len(items), len(l["domaines"])))
        out["listes"].append(items)
    for k in typ["paragraphes"]:
        art, par = k.split(".")
        p = next((p for p in paragraphes_en(art) if p.startswith(par + ". ")), None)
        if not p:
            raise Arret("U1 : paragraphe %s absent du texte anglais" % k)
        out["paragraphes"][k] = p[len(par) + 2:].strip()
    t16 = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", (EN_DIR / "arttue16.xhtml").read_bytes().decode("utf-8"))))
    if TUE16_EN not in t16:
        raise Arret("U2 : citation anglaise du TUE, art. 16, introuvable")
    return out


def double_deficit() -> int:
    """Nombre d'États que la Commission range à double déficit élevé, lu dans son texte (la France doit y figurer)."""
    m = re.search(r"(\d+) Member States \(([^)]*)\) combine both a high transposition deficit", ue4.texte_page())
    if not m or "France" not in m.group(2):
        raise Arret("U5 : liste des États à double déficit illisible ou sans la France")
    return int(m.group(1))


def affichage(typ, B, V, tr) -> tuple[dict, dict]:
    ex, pa, ap = (typ["listes"][0], typ["listes"][1], typ["listes"][2])
    joindre = lambda L, et: ", ".join(L[:-1]) + " " + et + " " + L[-1]  # noqa: E731
    dom = lambda l: [d["domaine"].rstrip(";.") for d in l["domaines"]]  # noqa: E731
    deb, fin = RELEVE["debut"], RELEVE["fin"]
    A = {"exclusives": joindre(dom(ex), "et"), "n_exclusives": str(len(ex["domaines"])),
         "partagees": joindre(dom(pa), "et"), "n_partagees": str(len(pa["domaines"])),
         "appui": joindre(dom(ap), "et"), "n_appui": str(len(ap["domaines"])),
         "cit_2_1": typ["paragraphes"]["2.1"], "cit_2_2": typ["paragraphes"]["2.2"], "cit_2_5": typ["paragraphes"]["2.5"],
         "cit_4_3": typ["paragraphes"]["4.3"], "cit_3_2": typ["paragraphes"]["3.2"],
         "n_plo": str(len(B["plo"])), "n_plo_art": str(B["plo_art"]), "n_una": str(len(B["una"])), "n_una_art": str(B["una_art"]),
         "n_cond": str(len(B["cond"])), "n_temoin": str(B["temoin"]),
         "debut": date_fr(deb), "fin": date_fr(fin), "entrees": fr(RELEVE["entrees"]), "entrees_min": fr(RELEVE["entrees"] - RELEVE["doublons"]),
         "doublons": str(RELEVE["doublons"]), "fr_contre": CH_FR[V["fr_contre"]], "fr_abst": CH_FR[V["fr_abst"]],
         "fr_c": str(V["fr_contre"]), "fr_a": str(V["fr_abst"]), "fr_pour": fr(V["fr_pour"]),
         "de_c": str(TOUT["DE"][0]), "de_a": str(TOUT["DE"][1]), "nl_c": str(TOUT["NL"][0]), "pl_c": str(TOUT["PL"][0]),
         "hu_c": str(TOUT["HU"][0]), "it_c": str(TOUT["IT"][0]), "es_c": str(TOUT["ES"][0]), "uk_c": str(TOUT["UK"][0]),
         "qmv": fr(RELEVE["regles"]["Majorité qualifiée"]), "una": fr(RELEVE["regles"]["Unanimité"]),
         "releve": date_fr(RELEVE["date"]),
         "tr_date": date_fr(tr["date_arrete"]), "tr_def": fr(tr["deficit_transposition"][0], 1), "tr_def_ue": fr(tr["deficit_transposition"][1], 1),
         "tr_retard": str(tr["directives_en_retard"][0]), "tr_dues": fr(tr["directives_dues"]),
         "tr_conf": fr(tr["deficit_conformite"][0], 1), "tr_conf_ue": fr(tr["deficit_conformite"][1], 1),
         "tr_mois": fr(tr["retard_moyen_mois"][0], 1), "tr_mois_ue": fr(tr["retard_moyen_mois"][1], 1),
         "tr_inf": fr(tr["duree_infractions_mois"][0], 1), "tr_inf_ue": fr(tr["duree_infractions_mois"][1], 1),
         "tr_double": {9: "neuf", 8: "huit", 10: "dix", 7: "sept"}.get(double_deficit(), str(double_deficit())),
         "cit_tue16": citation_tue16(), "etats_identiques": str(V["etats_identiques"]), "etats_total": str(len(NOMS))}
    te_ = typologie_en(typ)
    dom_en = lambda L: [d.rstrip(";.") for d in L]  # noqa: E731
    jen = lambda L: ", ".join(L[:-1]) + " and " + L[-1]  # noqa: E731
    E = {"exclusives": jen(dom_en(te_["listes"][0])), "partagees": jen(dom_en(te_["listes"][1])), "appui": jen(dom_en(te_["listes"][2])),
         "cit_2_1": te_["paragraphes"]["2.1"], "cit_2_2": te_["paragraphes"]["2.2"], "cit_2_5": te_["paragraphes"]["2.5"],
         "cit_4_3": te_["paragraphes"]["4.3"], "cit_3_2": te_["paragraphes"]["3.2"],
         "n_exclusives": A["n_exclusives"], "n_partagees": A["n_partagees"], "n_appui": A["n_appui"],
         "n_plo": A["n_plo"], "n_plo_art": A["n_plo_art"], "n_una": A["n_una"], "n_una_art": A["n_una_art"], "n_cond": A["n_cond"],
         "n_temoin": A["n_temoin"], "debut": date_en(deb), "fin": date_en(fin), "entrees": "{:,}".format(RELEVE["entrees"]),
         "entrees_min": "{:,}".format(RELEVE["entrees"] - RELEVE["doublons"]), "doublons": A["doublons"],
         "fr_contre": CH_EN[V["fr_contre"]], "fr_abst": CH_EN[V["fr_abst"]], "fr_c": A["fr_c"], "fr_a": A["fr_a"],
         "fr_pour": "{:,}".format(V["fr_pour"]), "de_c": A["de_c"], "de_a": A["de_a"], "nl_c": A["nl_c"], "pl_c": A["pl_c"],
         "hu_c": A["hu_c"], "it_c": A["it_c"], "es_c": A["es_c"], "uk_c": A["uk_c"],
         "qmv": "{:,}".format(RELEVE["regles"]["Majorité qualifiée"]), "una": "{:,}".format(RELEVE["regles"]["Unanimité"]),
         "releve": date_en(RELEVE["date"]), "tr_date": date_en(tr["date_arrete"]),
         "tr_def": "%.1f" % tr["deficit_transposition"][0], "tr_def_ue": "%.1f" % tr["deficit_transposition"][1],
         "tr_retard": A["tr_retard"], "tr_dues": "{:,}".format(tr["directives_dues"]),
         "tr_conf": "%.1f" % tr["deficit_conformite"][0], "tr_conf_ue": "%.1f" % tr["deficit_conformite"][1],
         "tr_mois": "%.1f" % tr["retard_moyen_mois"][0], "tr_mois_ue": "%.1f" % tr["retard_moyen_mois"][1],
         "tr_inf": "%.1f" % tr["duree_infractions_mois"][0], "tr_inf_ue": "%.1f" % tr["duree_infractions_mois"][1],
         "tr_double": {9: "nine", 8: "eight", 10: "ten", 7: "seven"}.get(double_deficit(), str(double_deficit())),
         "cit_tue16": TUE16_EN, "etats_identiques": str(V["etats_identiques"]), "etats_total": str(len(NOMS))}
    return A, E


# Instruments que nomment le livre et les programmes : (unités du TFUE, libellé FR, libellé EN).
INSTRUMENTS = [
    (["114(1)"], "Marché intérieur (rapprochement des législations)", "Internal market (approximation of laws)"),
    (["113, al. 1"], "Fiscalité indirecte (TVA, accises)", "Indirect taxation (VAT, excise duties)"),
    (["207(2)"], "Politique commerciale : cadre de mise en œuvre", "Commercial policy: implementing framework"),
    (["207(4)"], "Politique commerciale : certains accords", "Commercial policy: certain agreements"),
    (["192(1)"], "Environnement", "Environment"),
    (["192(2)"], "Environnement : dispositions fiscales, aménagement du territoire, énergie", "Environment: fiscal provisions, land use, energy mix"),
    (["43(2)"], "Agriculture et pêche : organisation commune des marchés", "Agriculture and fisheries: common market organisation"),
    (["78(2)"], "Asile", "Asylum"),
    (["79(2)"], "Immigration", "Immigration"),
    (["153(2)"], "Politique sociale", "Social policy"),
    (["311, al. 3"], "Ressources propres de l'Union", "The Union's own resources"),
    (["312(2)"], "Cadre financier pluriannuel", "Multiannual financial framework"),
]


def tableaux(typ, B, tr) -> tuple[dict, dict]:
    t, te = {}, {}
    lignes, le = [], []
    for l, (cfr, cen) in zip(typ["listes"], (("Exclusive (art. 3, § 1)", "Exclusive (art. 3(1))"), ("Partagée (art. 4, § 2)", "Shared (art. 4(2))"),
                                             ("Appui, coordination, complément (art. 6)", "Competence to support, coordinate or supplement (art. 6)"))):
        for d in l["domaines"]:
            lignes.append([cfr, d["domaine"].rstrip(";.")])
    t["competences"] = {"entetes": ["Catégorie", "Domaine (texte du traité)"], "lignes": lignes}
    te_ = typologie_en(typ)
    te["competences"] = {"entetes": ["Category", "Area (text of the Treaty)"],
                         "lignes": [[c, d.rstrip(";.")] for c, L in zip(("Exclusive (art. 3(1))", "Shared (art. 4(2))", "Competence to support, coordinate or supplement (art. 6)"), te_["listes"]) for d in L]}
    li, lie = [], []
    for unites, lfr, len_ in INSTRUMENTS:
        u = unites[0]
        plo, una = B["q"].get(u, (None, None))
        if u not in B["q"]:
            raise Arret("U2 : instrument %s absent du relevé" % u)
        r_fr = "unanimité au Conseil" if una == "base" and plo != "base" else ("procédure législative ordinaire (majorité qualifiée)" if plo == "base" and una != "base" else "les deux, selon les mesures")
        r_en = "unanimity in the Council" if una == "base" and plo != "base" else ("ordinary legislative procedure (qualified majority)" if plo == "base" and una != "base" else "both, depending on the measure")
        art = "art. " + u.replace(", al. ", ", al. ")
        li.append([lfr, art, r_fr])
        lie.append([len_, art, r_en])
    t["instruments"] = {"entetes": ["Matière", "Base (TFUE)", "Règle au Conseil"], "lignes": li}
    te["instruments"] = {"entetes": ["Area", "Legal basis (TFEU)", "Rule in the Council"], "lignes": lie}
    t["france"] = {"entetes": ["Date", "Vote de la France", "Acte"], "lignes": [[date_fr(d), v, a] for d, v, a, _ in FR_ACTES]}
    te["france"] = {"entetes": ["Date", "France's vote", "Act"], "lignes": [[date_en(d), {"contre": "against", "abstention": "abstention"}[v], b] for d, v, _, b in FR_ACTES]}
    t["etats"] = {"entetes": ["État membre", "Contre", "Abstention", "Ne participe pas"],
                  "lignes": [[NOMS[c][0], str(TOUT[c][0]), str(TOUT[c][1]), str(TOUT[c][2])] for c in sorted(NOMS, key=lambda c: NOMS[c][0])]}
    te["etats"] = {"entetes": ["Member State", "Against", "Abstention", "Not taking part"],
                   "lignes": [[NOMS[c][1], str(TOUT[c][0]), str(TOUT[c][1]), str(TOUT[c][2])] for c in sorted(NOMS, key=lambda c: NOMS[c][1])]}
    rows = [("Déficit de transposition (directives non transposées)", "Transposition deficit (directives not transposed)", "%s %%", tr["deficit_transposition"]),
            ("Directives en retard", "Overdue directives", "%s", tr["directives_en_retard"]),
            ("En retard de plus de deux ans", "Overdue by more than two years", "%s", tr["en_retard_2_ans"]),
            ("Retard moyen (mois)", "Average delay (months)", "%s", tr["retard_moyen_mois"]),
            ("Déficit de conformité (procédures pour transposition incorrecte)", "Conformity deficit (proceedings for incorrect transposition)", "%s %%", tr["deficit_conformite"]),
            ("Durée des procédures d'infraction pour retard (mois)", "Duration of infringement proceedings for late transposition (months)", "%s", tr["duree_infractions_mois"])]
    f1 = lambda v: fr(v, 1) if isinstance(v, float) else str(v)  # noqa: E731
    t["transposition"] = {"entetes": ["Indicateur, au %s" % date_fr(tr["date_arrete"]), "France", "Moyenne de l'UE"],
                          "lignes": [[a, m % f1(v[0]), m % f1(v[1])] for a, _, m, v in rows]}
    te["transposition"] = {"entetes": ["Indicator, as at %s" % date_en(tr["date_arrete"]), "France", "EU average"],
                           "lignes": [[b, (m.replace(" %%", "%%") % v[0]), (m.replace(" %%", "%%") % v[1])] for _, b, m, v in rows]}
    return t, te


MONTRE = {"fr": "Sur les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {debut} au {fin}, la France a voté contre {fr_contre} et s'est abstenue {fr_abst} ; elle a voté pour dans tous les autres cas.",
          "en": "In the public votes of the Council of the European Union on legislative acts, from {debut} to {fin}, France voted against {fr_contre} and abstained {fr_abst}; it voted in favour in every other case."}


def fiches(figs, A, E):
    """Fiches « Réutiliser » : titre, source et précaution LUS dans le SVG servi (classes du pied commun)."""
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", E)):
        svg = figs["europe-votes%s.svg" % suf]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        src, note, lic = pf.lire(svg, "pied-source"), pf.lire(svg, "pied-note"), pf.lire(svg, "pied-licence")
        if not src or not note or lic.replace("\u00a0", " ") != LICENCES[lang]:
            raise Arret("fiche europe-votes%s : pied illisible" % suf)
        res[lang] = [dict(id="votes", fichier="europe-votes" + suf, titre=titre, montre=MONTRE[lang].format(**AA), source=src, precaution=note)]
    return res


def csv_texte(B) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "cle", "variable", "valeur", "source"])
    for c in sorted(NOMS):
        for i, v in enumerate(("contre", "abstention", "ne_participe_pas")):
            w.writerow(["votes_conseil_2009_2026", c, v, TOUT[c][i], "Conseil de l'UE, recherche des résultats de vote, relevé du %s" % RELEVE["date"]])
    for (vote, pos, tfr, ten, cpt, st, celex, afr, aen, dacte, proc) in ACTES:
        w.writerow(["votes_france_hors_pour", vote, pos, tfr, "Conseil de l'UE, note %s ; acte %s (CELEX %s) du %s ; procédure %s" % (st, afr, celex, dacte, proc)])
        for i, v in enumerate(("pour", "contre", "abstention", "ne_participe_pas")):
            w.writerow(["decompte_conseil_actes_france", vote, v, cpt[i], "Conseil de l'UE, note %s" % st])
    for u in B["plo"]:
        w.writerow(["bases_tfue", u, "procedure_legislative_ordinaire", "base", "TFUE consolidé, JO C 202 du 07/06/2016"])
    for u in B["cond"]:
        w.writerow(["bases_tfue", u, "procedure_legislative_ordinaire", "conditionnelle", "TFUE"])
    for u in B["una"]:
        w.writerow(["bases_tfue", u, "unanimite_au_conseil", "base", "TFUE"])
    tr = ue4.FR
    for k in ("deficit_transposition", "directives_en_retard", "en_retard_2_ans", "retard_moyen_mois", "deficit_conformite", "duree_infractions_mois"):
        w.writerow(["transposition_%s" % tr["date_arrete"], k, "France", tr[k][0], "Commission, tableau d'affichage du marché unique"])
        w.writerow(["transposition_%s" % tr["date_arrete"], k, "moyenne_UE", tr[k][1], "Commission, tableau d'affichage du marché unique"])
    return buf.getvalue()


def autotest(sw):
    out = []
    for nom, mut in (("vote FR altéré", lambda f: dict(f, FR=(f["FR"][0] + 1, f["FR"][1]))),
                     ("compte d'un État altéré", lambda f: dict(f, DE=(f["DE"][0], f["DE"][1] - 1)))):
        if not temoin_votes(mut(dict(FENETRE)), sw):
            raise Arret("mutation %s : U3 n'a pas mordu, contrôle ABSENT" % nom)
        out.append(nom + " -> U3")
    s = ue1.lire()
    del s["listes"][0]["domaines"][1]
    if not ue1.verifier(s):
        raise Arret("mutation domaine retiré : U1 n'a pas mordu")
    out.append("domaine retiré -> U1")
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def table_actes(lang: str) -> dict:
    """Les cinq actes : date du vote, position, acte, décompte au Conseil, acte publié, second jeu, liens primaires."""
    fr = lang == "fr"
    dt = date_fr if fr else date_en
    lignes = []
    for (vote, pos, tfr, ten, cpt, st, celex, afr, aen, dacte, proc) in ACTES:
        p, c, a, n = cpt
        if fr:
            dec = "%d pour, %d contre, %d abstention%s" % (p, c, a, "s" if a > 1 else "") + (", %d ne participe pas" % n if n else "")
            pub = "%s du %s" % (afr, dt(dacte))
            tem = "SWP : même décompte" if vote <= FIN_TEMOIN else "aucun (vote postérieur au jeu SWP)"
            liens = [{"t": "résultat du Conseil", "u": "https://data.consilium.europa.eu/doc/document/%s/fr/pdf" % st},
                     {"t": "EUR-Lex", "u": "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:%s" % celex}]
            lignes.append([dt(vote), pos, tfr, dec, pub, tem, liens])
        else:
            dec = "%d in favour, %d against, %d abstention%s" % (p, c, a, "" if a == 1 else "s") + (", %d not taking part" % n if n else "")
            pub = "%s of %s" % (aen, dt(dacte))
            tem = "SWP: same count" if vote <= FIN_TEMOIN else "none (vote later than the SWP dataset)"
            liens = [{"t": "Council result", "u": "https://data.consilium.europa.eu/doc/document/%s/en/pdf" % st},
                     {"t": "EUR-Lex", "u": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:%s" % celex}]
            lignes.append([dt(vote), {"contre": "against", "abstention": "abstention"}[pos], ten, dec, pub, tem, liens])
    ent = (["Date du vote", "Vote de la France", "Acte", "Décompte au Conseil", "Acte publié", "Second jeu", "Documents"] if fr
           else ["Date of the vote", "France's vote", "Act", "Count in the Council", "Published act", "Second dataset", "Documents"])
    return {"entetes": ent, "lignes": lignes}


def tokens_phase_b(A: dict, E: dict, RA: list, B: dict) -> None:
    regles = RELEVE["regles"]
    if sum(regles.values()) != RELEVE["entrees"]:
        raise Arret("U3 : les règles de vote (%s) ne totalisent pas les %d entrées" % (regles, RELEVE["entrees"]))
    for d, lang, dt in ((A, "fr", date_fr), (E, "en", date_en)):
        d["fin_temoin"] = dt(FIN_TEMOIN)
        d["qmv_sp"] = lg.lettres(regles["Majorité qualifiée sans proposition de la Commission"], lang)
        d["n_cond_min"] = lg.lettres(len(B["cond"]), lang)
        d["n_cond"] = d["n_cond_min"].capitalize()
        d["n_ponderes"] = lg.lettres(sum(r["pondere"] for r in RA), lang)
        d["n_actes_temoin"] = lg.lettres(sum(r["temoin"] for r in RA), lang)
        d["n_actes_source"] = lg.lettres(len(RA) - sum(r["temoin"] for r in RA), lang)
        d["n_actes"] = lg.lettres(len(RA), lang)
        d["n_ponderes_maj"] = d["n_ponderes"].capitalize()
        d["fr_c_l"] = lg.lettres(sum(a[1] == "contre" for a in ACTES), lang)
        d["fr_a_l"] = lg.lettres(sum(a[1] == "abstention" for a in ACTES), lang)
        d["dm_debut"] = dt(DEBUT_DOUBLE_MAJORITE)
        d["dm_fin_ancien"] = dt("2014-10-31")
        d["dm_option_fin"] = dt("2017-03-31")
        d["tr_double"] = lg.lettres(double_deficit(), lang)


def autotest_b(tx: dict, sw_rows: list, A: dict, E: dict, textes: dict, fr_np: int, t_mai21: str) -> list[str]:
    """Mutations des gardes nouvelles de la phase B : chacune doit arrêter SA garde."""
    out = []

    def doit_arreter(nom, f, garde):
        try:
            f()
        except Arret as x:
            if not str(x).startswith(garde):
                raise Arret("mutation %s : arrêtée par une autre garde (%s)" % (nom, x))
            out.append("%s -> %s" % (nom, garde))
            return
        raise Arret("mutation %s : %s n'a pas mordu, contrôle ABSENT" % (nom, garde))

    c2 = dict(CITS)
    c2["cit_293_1"] = (c2["cit_293_1"][0], c2["cit_293_1"][1].replace("sauf dans", "y compris dans"), c2["cit_293_1"][2])
    doit_arreter("citation de l'art. 293 altérée", lambda: citations_traite(tx, c2), "U6")
    c3 = dict(CITS)
    c3["cit_tue4_1"] = (c3["cit_tue4_1"][0], c3["cit_tue4_1"][1], c3["cit_tue4_1"][2].replace("remain with", "belong to"))
    doit_arreter("citation anglaise du TUE, art. 4 altérée", lambda: citations_traite(tx, c3), "U6")
    l2 = copy.deepcopy(B3_LU)
    l2[("238", "fr")][0] = l2[("238", "fr")][0].replace("ne prennent pas part", "prennent part")
    doit_arreter("TFUE 238, § 3 : règle des États participants altérée", lambda: citations_traite(tx, None, l2), "U6")
    l3 = copy.deepcopy(B3_LU)
    l3[("jo", "fr")][2] = l3[("jo", "fr")][2].replace("médicaments", "denrées")
    doit_arreter("TFUE 168, § 4 : médicaments altérés", lambda: citations_traite(tx, None, l3), "U6")
    m = copy.deepcopy(ACTES)
    m[4] = m[4][:4] + ((22, 3, 0, 1),) + m[4][5:]
    doit_arreter("décompte de 2026 altéré (total faux)", lambda: controler_actes(m, sw_rows), "U8")
    m = copy.deepcopy(ACTES)
    m[0] = m[0][:4] + ((26, 1, 1, 0),) + m[0][5:]
    doit_arreter("décompte de 2014 altéré (total juste)", lambda: controler_actes(m, sw_rows), "U8")
    m = copy.deepcopy(ACTES)
    m[3] = m[3][:9] + ("2025-09-11",) + m[3][10:]
    doit_arreter("date de l'acte de 2025 altérée", lambda: controler_actes(m, sw_rows), "U8")
    # passe B3 : composition altérée À TOTAL CONSTANT (les comptes 22/1/4/0 et 23/3/0/1 restent justes)
    k = copy.deepcopy(COMPOSITION)
    k["ST-11350-2025-INIT"]["abstention"] = ("CZ", "FR", "MT", "BE")  # AT abstention -> pour, BE pour -> abstention
    doit_arreter("2025 : un vote de « pour » à « abstention », un autre d'« abstention » à « pour » (total constant)",
                 lambda: controler_actes(ACTES, sw_rows, k), "U8")
    k = copy.deepcopy(COMPOSITION)
    k["ST-6628-2026-INIT"]["contre"] = ("ES", "FR", "IT")  # PT contre -> pour, IT pour -> contre
    doit_arreter("2026 : un vote de « contre » à « pour », un autre de « pour » à « contre » (total constant)",
                 lambda: controler_actes(ACTES, sw_rows, k), "U8")

    seance = t_mai21.replace("Written procedures", "3794th meeting of the Council of the European Union (Education) held in Brussels on 17 May 2021 Written procedures", 1)
    doit_arreter("séance du Conseil le 17 mai 2021 ajoutée au récapitulatif", lambda: verifier_17mai(seance, sw_rows), "U3")
    sans = [r for r in sw_rows if r["voteProc"] != "http://data.consilium.europa.eu/id/votingprocedure/4782"]
    doit_arreter("une des deux fiches SWP du 17 mai 2021 retirée", lambda: verifier_17mai(t_mai21, sans), "U3")

    def prose(t, np_):
        f = garde_prose(t, np_)
        if f:
            raise Arret("U9 : " + f[0])
    doit_arreter("« le Conseil ne peut amender la proposition qu'à l'unanimité » (fr, sans sauf)",
                 lambda: prose(dict(textes, fr=textes["fr"] + "\nLe Conseil ne peut amender la proposition qu'à l'unanimité.\n"), fr_np), "U9")
    doit_arreter("'the Council may amend it only unanimously' (en, without except)",
                 lambda: prose(dict(textes, en=textes["en"] + "\nThe Council may amend the proposal only unanimously.\n"), fr_np), "U9")
    doit_arreter("classement verbal ajouté", lambda: prose(dict(textes, fr=textes["fr"] + "\nLa France vote contre moins souvent que l'Allemagne.\n"), fr_np), "U9")
    doit_arreter("non-participation de la France", lambda: prose(textes, 1), "U9")
    return out


def _main() -> int:
    check = "--check" in sys.argv[1:]
    g = []
    typ = typologie()
    g.append("U1 : typologie complète et citée (%s exclusives, %s partagées, %s d'appui)" % tuple(len(l["domaines"]) for l in typ["listes"]))
    B = bases()
    g.append("U2 : %d bases PLO (%d articles), %d conditionnelles, %d bases à l'unanimité ; témoin du Conseil : concordance exacte" % (len(B["plo"]), B["plo_art"], len(B["cond"]), len(B["una"])))
    sw = swp_fenetre()
    V = votes(TOUT, FENETRE, sw)
    g.append("U3 : relevé du Conseil concordant avec SWP pays par pays (écarts expliqués seulement) ; règles de vote %s = %d entrées"
             % (" + ".join(str(v) for v in RELEVE["regles"].values()), RELEVE["entrees"]))
    g.append("U4 : France %d contre, %d abstentions, %d pour (liste des actes cohérente)" % (V["fr_contre"], V["fr_abst"], V["fr_pour"]))
    err = ue4.controles(ue4.FR, ue4.texte_page())
    if err:
        raise Arret("U5 : %s" % err[0])
    g.append("U5 : transposition contrôlée par le texte de la Commission")
    tx = textes_traite()
    CA, CE = citations_traite(tx)
    g.append("U6 : %d citations des traités (TUE 4, 5, 15, 16, 17 ; TFUE 2, 18, 76, 238, 241, 288, 293, 294) retrouvées mot pour mot, FR et EN ; protocole n° 36 relu ; TFUE 238, § 3 et 168, § 4 relus (phrases résumées)" % len(CITS))
    sw_rows = list(csv.DictReader(open(SWP, encoding="utf-8")))
    RA = controler_actes(ACTES, sw_rows)
    g.append("U8 : %d actes relus (note du Conseil, acte publié FR et EN) ; %d décomptes recoupés par SWP, %d documentés à la source, composition État par État relue dans l'annexe (%d)"
             % (len(RA), sum(r["temoin"] for r in RA), len(RA) - sum(r["temoin"] for r in RA), sum(r["composition"] for r in RA)))
    t_mai21 = texte_mai21()
    g.append(verifier_17mai(t_mai21, sw_rows))
    for m in autotest(sw):
        log("autotest : la mutation a mordu : " + m)
    A, E = affichage(typ, B, V, ue4.FR)
    A.update(CA)
    E.update(CE)
    tokens_phase_b(A, E, RA, B)
    msg, sv = verifier_swp()
    g.append(msg)
    sauve = ECARTS_EXPLIQUES[("FR", 0)]
    try:  # mutation : un écart expliqué différent doit arrêter U7
        ECARTS_EXPLIQUES[("FR", 0)] = -1
        verifier_swp()
        raise RuntimeError("U7 : la mutation « écart modifié » n'a pas mordu")
    except Arret:
        log("autotest : la mutation a mordu : écart SWP modifié -> U7")
    finally:
        ECARTS_EXPLIQUES[("FR", 0)] = sauve
    for d, lang in ((A, "fr"), (E, "en")):
        d["swp21_cit"], d["swp24_cit"] = SWP_PUBS["swp21"][2], SWP_PUBS["swp24"][2]
        d["swp21_contre"] = lg.lettres(sv["swp21"]["contre"], lang)
        d["swp21_abst"] = lg.lettres(sv["swp21"]["abst"], lang)
        d["swp24_nonpour"] = lg.lettres(sv["swp24"]["contre"] + sv["swp24"]["abst"], lang)
        d["swp24_ecart"] = lg.lettres(-ECARTS_EXPLIQUES[("FR", 0)], lang)
        d["swp24_annonce"] = lg.lettres(SWP24_ANNONCE, lang)
        d["polidori_tfue"] = sv["polidori_tfue"]
    for d, dt in ((A, date_fr), (E, date_en)):
        if MAI21["avant"][:4] != MAI21["apres"][:4]:
            raise Arret("U3 : les deux votes qui encadrent le %s ne sont pas de la même année (« entre le … et le … »)" % MAI21["date"])
        # « entre le 10 mai et le 26 mai 2021 » : la première date sans l'année, la même que celle de la seconde
        d["ecart_date"], d["ecart_avant"], d["ecart_apres"] = dt(MAI21["date"]), dt(MAI21["avant"]).rsplit(" ", 1)[0], dt(MAI21["apres"])
    if set(A) != set(E):
        raise Arret("blocs affichage : clés différentes (%s)" % sorted(set(A) ^ set(E)))
    textes = {"fr": resoudre(PAGE_FR.read_text(encoding="utf-8"), A), "en": resoudre(PAGE_EN.read_text(encoding="utf-8"), E)}
    fautes = garde_prose(textes, V["fr_np"])
    if fautes:
        raise Arret("U9 : " + fautes[0])
    g.append("U9 : prose FR et EN relue, jetons résolus (amender sans « sauf », classement verbal, « pour dans tous les autres cas »)")
    for m in autotest_b(tx, sw_rows, A, E, textes, V["fr_np"], t_mai21):
        log("autotest : la mutation a mordu : " + m)
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", E)):
        figs["europe-votes%s.svg" % suf] = fig_votes(TOUT, AA)
        figs["europe-votes%s-m.svg" % suf] = fig_votes_m(TOUT, AA)
        corps_m = re.sub(r'<text class="pied-[a-z]+"[^>]*>[^<]*</text>', "", figs["europe-votes%s-m.svg" % suf])  # pied : texte, pas des valeurs
        ec = pf.parite(figs["europe-votes%s.svg" % suf], corps_m, pf.POLICE_M, (INK, MUTED))
        if ec:
            raise Arret("figure téléphone europe-votes%s : %s" % (suf, "; ".join(ec)))
    LANG = "fr"
    g.append("Figures : version téléphone à parité avec la version détaillée (FR et EN)")
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        for x in g:
            log("OK " + x)
        return 0
    import cairosvg
    fi = fiches(figs, A, E)
    t, te = tableaux(typ, B, ue4.FR)
    t["france"], te["france"] = table_actes("fr"), table_actes("en")
    csvt = csv_texte(B)
    payload = {
        "releve_le": RELEVE["date"],
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources : TFUE et TUE (EUR-Lex), Conseil de l'UE, SWP / GESIS (doi 10.7802/2560, CC BY 4.0), Commission européenne",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve, prolongement U (U-E1 à U-E4) ; phase B du 12/10/2026 (U6, U8, U9)",
                 "releve_conseil": RELEVE, "temoin_votes": "Public Voting Data of the Council of the EU, v2.0.0, SWP, doi 10.7802/2560",
                 "temoin_bases": "Secrétariat général du Conseil, Guide to the ordinary legislative procedure, annexe III, doi 10.2860/74684",
                 "ecarts_expliques": {"%s_%s" % (k[0], ("contre", "abstention")[k[1]]): v for k, v in ECARTS_EXPLIQUES.items()},
                 "actes_france": [{"vote": a[0], "position": a[1], "decompte_pour_contre_abstention_np": list(a[4]), "note_conseil": a[5],
                                   "celex": a[6], "acte": a[8], "date_acte": a[9], "procedure": a[10],
                                   "second_jeu": "SWP" if a[0] <= FIN_TEMOIN else "aucun",
                                   **({"composition": {k: list(v) for k, v in COMPOSITION[a[5]].items()},
                                       "verification_composition": {"piece": "ST %s/%s INIT" % (a[5].split("-")[1], a[5].split("-")[2][2:]),
                                                                    "page": 2, "objet": "annexe (image) : vote de chaque État membre",
                                                                    "sha256_pdf": CONSEIL_SHA[a[5]],
                                                                    "controle": "lue à l'œil le 12/10/2026, transcrite ; la garde U8 relit les pictogrammes de l'image État par État et s'arrête au moindre écart ; mutation à total constant vue mordre"}}
                                      if a[5] in COMPOSITION else {})} for a in ACTES]},
        "gardes": g, "calcul": {"votes": V, "bases": {k: v for k, v in B.items() if k != "q"}},
        "tableaux": t, "tableaux_en": te,
        "affichage": dict(A, releve_le="%s (votes du Conseil, relevé à cette date ; transposition au %s)" % (date_fr(RELEVE["date"]), date_fr(ue4.FR["date_arrete"]))),
        "affichage_en": dict(E, releve_le="%s (Council votes, retrieved on that date; transposition as at %s)" % (date_en(RELEVE["date"]), date_en(ue4.FR["date_arrete"]))),
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
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
    log("Ecrit : data/promesses_europe.json, static/promesses_europe.{json,csv}, data/figures_europe.json, 4 figures SVG + PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
