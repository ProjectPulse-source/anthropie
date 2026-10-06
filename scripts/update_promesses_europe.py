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
  U-E4        le tableau d'affichage du marché unique (Commission), transcrit d'une capture (test_u_e4.py, qui le contrôle).

Gardes (toutes ARRÊTENT) :
  U1  typologie complète et citée (contrôles de test_u_e1) ;
  U2  bases qualifiées sans unité non classée, concordance exacte avec le témoin du Conseil (test_u_e2) ;
  U3  TÉMOIN : sur la période commune (22/12/2009 - 28/03/2023), les comptes « contre » et « abstention » de chaque État,
      recalculés du jeu SWP, égalent la transcription du relevé du Conseil, aux seuls écarts expliqués près (acte du
      28/03/2023 absent de SWP ; deux fiches SWP sans titre du 17/05/2021 démenties par le registre des documents) ;
      tout autre écart arrête ;
  U4  phrases : « contre deux fois et abstenue trois fois » recalculé ; « la France vote contre moins souvent que » est
      INTERDIT (aucune phrase de classement) ; le total des votes est écrit en borne (doublons du producteur) ;
  U5  transposition : contrôles de test_u_e4 (moyennes dans le texte de la Commission, cohérence 11 / 1 022).
Autotest : vote de la France transcrit altéré (U3), compte d'un État altéré (U3), domaine retiré (U1).

Écrit : data/promesses_europe.json (+ static/), static/promesses_europe.csv, data/figures_europe.json,
static/img/europe-votes(-en).svg/.png. Rien n'est écrit à données identiques. Sortie console ASCII.
"""
from __future__ import annotations

import copy
import csv
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
FR_ACTES = [
    ("2014-02-17", "contre", "Règlement sur les vins aromatisés (n° 251/2014)", "Regulation on aromatised wine products (No 251/2014)"),
    ("2014-05-08", "abstention", "Directive modifiant la directive 2001/110/CE relative au miel", "Directive amending Council Directive 2001/110/EC relating to honey"),
    ("2015-10-01", "abstention", "Règlement sur le commerce des produits dérivés du phoque", "Regulation on trade in seal products"),
    ("2025-07-08", "abstention", "Décision sur l'accord d'interprétation du traité sur la Charte de l'énergie", "Decision on the agreement on the interpretation of the Energy Charter Treaty"),
    ("2026-02-23", "contre", "Règlement sur la notion de « pays tiers sûr » (2025/0132 (COD))", "Regulation on the 'safe third country' concept (2025/0132 (COD))"),
]
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
    "fr": {"t": "Votes contre et abstentions au Conseil de l'UE, par État membre",
           "s": "votes publics sur des actes législatifs, du {debut} au {fin}",
           "d": "Barres horizontales par État membre, triées : votes contre (foncé) et abstentions (clair). La France compte {fr_c} votes contre et {fr_a} abstentions sur {entrees} votes publiés.",
           "src": "Conseil de l'UE, recherche des résultats de vote (relevé du 06/10/2026) ; contrôle : SWP / GESIS, doi 10.7802/2560 (2009-2023)",
           "note": "Royaume-Uni jusqu'à son retrait (2020), Croatie depuis 2013. Le Danemark et l'Irlande ne participent pas à certains actes.",
           "contre": "contre", "abst": "abstention"},
    "en": {"t": "Votes against and abstentions in the Council of the EU, by Member State",
           "s": "public votes on legislative acts, {debut} to {fin}",
           "d": "Horizontal bars by Member State, sorted: votes against (dark) and abstentions (light). France has {fr_c} votes against and {fr_a} abstentions out of {entrees} published votes.",
           "src": "Council of the EU, voting results search (retrieved 6 Oct. 2026); check: SWP / GESIS, doi 10.7802/2560 (2009-2023)",
           "note": "United Kingdom until its withdrawal (2020), Croatia since 2013. Denmark and Ireland do not take part in some acts.",
           "contre": "against", "abst": "abstention"},
}


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def fig_votes(tout: dict, A: dict) -> str:
    L = T[LANG]
    ordre = sorted(NOMS, key=lambda c: (-(tout[c][0] + tout[c][1]), NOMS[c][0]))
    hb, gap, y0 = 15, 4, 74
    H = y0 + len(ordre) * (hb + gap) + 6
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="ev-t ev-d" font-family="%s">' % (W, H + 48, FONT),
         '<title id="ev-t">%s</title><desc id="ev-d">%s</desc>' % (esc(L["t"]), esc(L["d"].format(**A))),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
         txt(0, 18, L["t"], 13, INK, weight="600"), txt(0, 36, L["s"].format(**A), 12, INK2)]
    x0, wmax = 130, 520
    vmax = max(tout[c][0] + tout[c][1] for c in ordre)
    e.append('<rect x="%d" y="48" width="12" height="10" fill="%s"/>' % (x0, INK2))
    e.append(txt(x0 + 16, 57, L["contre"], 10, INK2))
    e.append('<rect x="%d" y="48" width="12" height="10" fill="%s"/>' % (x0 + 90, GRIS_CLAIR))
    e.append(txt(x0 + 106, 57, L["abst"], 10, INK2))
    for k, c in enumerate(ordre):
        y = y0 + k * (hb + gap)
        contre, abst, _ = tout[c]
        estfr = c == "FR"
        col = BLEU if estfr else INK2
        nom = NOMS[c][0 if LANG == "fr" else 1]
        e.append(txt(x0 - 8, y + 11, nom, 10, INK if estfr else INK2, "end", "600" if estfr else None))
        wc, wa = wmax * contre / vmax, wmax * abst / vmax
        e.append('<rect x="%d" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0, y, wc, hb, col))
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0 + wc, y, wa, hb, "#9db5d8" if estfr else GRIS_CLAIR))
        e.append(txt(x0 + wc + wa + 6, y + 11, "%d · %d" % (contre, abst), 9, INK if estfr else MUTED, "start", "600" if estfr else None))
    e.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (H + 2, W, H + 2, GRID))
    for k, (t, c) in enumerate(((L["src"], INK2), (L["note"], INK2), (LICENCES[LANG], MUTED))):
        e.append('<text x="0" y="%d" font-size="9" fill="%s">%s</text>' % (H + 15 + 12 * k, c, esc(t)))
    e.append("</svg>")
    return "\n".join(e)


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
    E = {"exclusives": "", "partagees": "", "appui": "", "cit_2_1": "", "cit_2_2": "", "cit_2_5": "", "cit_4_3": "", "cit_3_2": "",
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
         "cit_tue16": "", "etats_identiques": str(V["etats_identiques"]), "etats_total": str(len(NOMS))}
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
                                             ("Appui, coordination, complément (art. 6)", "Support, coordination, supplement (art. 6)"))):
        for d in l["domaines"]:
            lignes.append([cfr, d["domaine"].rstrip(";.")])
    t["competences"] = {"entetes": ["Catégorie", "Domaine (texte du traité)"], "lignes": lignes}
    te["competences"] = {"entetes": ["Category", "Area (French text of the Treaty)"], "lignes": [[{"Exclusive (art. 3, § 1)": "Exclusive (art. 3(1))", "Partagée (art. 4, § 2)": "Shared (art. 4(2))"}.get(a, "Support, coordination, supplement (art. 6)"), b] for a, b in lignes]}
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
            ("Déficit de conformité (directives mal transposées)", "Conformity deficit (directives incorrectly transposed)", "%s %%", tr["deficit_conformite"]),
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
    res = {}
    for lang, suf, AA in (("fr", "", A), ("en", "-en", E)):
        svg = figs["europe-votes%s.svg" % suf]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        if len(cart) != 3 or cart[-1] != LICENCES[lang]:
            raise Arret("fiche europe-votes%s : cartouche illisible" % suf)
        res[lang] = [dict(id="votes", fichier="europe-votes" + suf, titre=titre, montre=MONTRE[lang].format(**AA), source=cart[0], precaution=cart[1])]
    return res


def csv_texte(B) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "cle", "variable", "valeur", "source"])
    for c in sorted(NOMS):
        for i, v in enumerate(("contre", "abstention", "ne_participe_pas")):
            w.writerow(["votes_conseil_2009_2026", c, v, TOUT[c][i], "Conseil de l'UE, recherche des résultats de vote, relevé du %s" % RELEVE["date"]])
    for d, v, a, _ in FR_ACTES:
        w.writerow(["votes_france_hors_pour", d, v, a, "Conseil de l'UE"])
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


def _main() -> int:
    check = "--check" in sys.argv[1:]
    g = []
    typ = typologie()
    g.append("U1 : typologie complète et citée (%s exclusives, %s partagées, %s d'appui)" % tuple(len(l["domaines"]) for l in typ["listes"]))
    B = bases()
    g.append("U2 : %d bases PLO (%d articles), %d conditionnelles, %d bases à l'unanimité ; témoin du Conseil : concordance exacte" % (len(B["plo"]), B["plo_art"], len(B["cond"]), len(B["una"])))
    sw = swp_fenetre()
    V = votes(TOUT, FENETRE, sw)
    g.append("U3 : relevé du Conseil concordant avec SWP pays par pays (écarts expliqués seulement)")
    g.append("U4 : France %d contre, %d abstentions, %d pour (liste des actes cohérente)" % (V["fr_contre"], V["fr_abst"], V["fr_pour"]))
    err = ue4.controles(ue4.FR, ue4.texte_page())
    if err:
        raise Arret("U5 : %s" % err[0])
    g.append("U5 : transposition contrôlée par le texte de la Commission")
    for m in autotest(sw):
        log("autotest : la mutation a mordu : " + m)
    A, E = affichage(typ, B, V, ue4.FR)
    if set(A) != set(E):
        raise Arret("blocs affichage : clés différentes (%s)" % sorted(set(A) ^ set(E)))
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", E)):
        figs["europe-votes%s.svg" % suf] = fig_votes(TOUT, AA)
    LANG = "fr"
    fi = fiches(figs, A, E)
    t, te = tableaux(typ, B, ue4.FR)
    csvt = csv_texte(B)
    payload = {
        "releve_le": RELEVE["date"],
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources : TFUE (EUR-Lex), Conseil de l'UE, SWP / GESIS (doi 10.7802/2560, CC BY 4.0), Commission européenne",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve, prolongement U (U-E1 à U-E4)",
                 "releve_conseil": RELEVE, "temoin_votes": "Public Voting Data of the Council of the EU, v2.0.0, SWP, doi 10.7802/2560",
                 "temoin_bases": "Secrétariat général du Conseil, Guide to the ordinary legislative procedure, annexe III, doi 10.2860/74684",
                 "ecarts_expliques": {"%s_%s" % (k[0], ("contre", "abstention")[k[1]]): v for k, v in ECARTS_EXPLIQUES.items()}},
        "gardes": g, "calcul": {"votes": V, "bases": {k: v for k, v in B.items() if k != "q"}},
        "tableaux": t, "tableaux_en": te,
        "affichage": dict(A, releve_le="%s (votes du Conseil, relevé à cette date ; transposition au %s)" % (date_fr(RELEVE["date"]), date_fr(ue4.FR["date_arrete"]))),
        "affichage_en": dict(E, releve_le="%s (Council votes, retrieved on that date; transposition as at %s)" % (date_en(RELEVE["date"]), date_en(ue4.FR["date_arrete"]))),
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
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_europe.json, static/promesses_europe.{json,csv}, data/figures_europe.json, 2 figures SVG + PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
