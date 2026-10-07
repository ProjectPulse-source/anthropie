#!/usr/bin/env python3
"""Volet « Délais » du dossier Promesses : la durée d'une formation de médecin, les admissions à leur date, et ce
qui agit avant la fin du cursus.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 4 (v2, gelée au commit
dfd0ec9 ; arbitrage PRO-20261005-164029).
  E1 — à règles constantes, durée du cursus standard de médecine générale depuis la première année : SOMME DE DURÉES
       LUES DANS LES TEXTES (aucune durée saisie), comparée à la durée du mandat lue dans l'art. 6 de la Constitution.
  E2 — admissions en études de médecine à leur année (DREES 1972-2020, ONDPS 2021-2025) ; aucun décalage, aucune
       projection, aucune densité ; ruptures de champ marquées.
  E3 — capacités avant la fin du cursus : autonomie supervisée (textes) ; médecins actifs à diplôme étranger (stock).

Sources (toutes dans scripts/sources_delais/, empreintes au JSON) : réponses Légifrance archivées (arrêté du 8 avril
2013 art. 1 ; C. éduc. L632-2 ; CSP R6153-1-2 ; Constitution art. 6) ; XML JORF de l'art. 37 de la loi n° 2022-1616
(stock DILA) ; DREES, Dossier n° 76, graphique 8 ; ONDPS, bilan 2021-2025 (PDF) et transcription de sa page 7 ;
extrait DREES RPPS 2012-2026 (lieu du diplôme).

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  D1  durée du cursus = somme des durées LUES : « six semestres » (1er cycle) + « six semestres » (2e cycle) +
      « quatre années » (3e cycle de médecine générale), applicable aux entrants en 3e cycle « à la rentrée de l'année
      universitaire 2023 » (citations retrouvées mot pour mot) ;
  D2  mandat : « cinq ans » et « Nul ne peut exercer plus de deux mandats consécutifs » (art. 6) ;
  D3  la phrase « soit deux fois la durée d'un mandat » n'est écrite que si durée du cursus / mandat est entier ;
  D4  série DREES contiguë 1972-2020 ; « divisées par plus de deux » exige 1972 / minimum > 2 ;
  D5  TÉMOIN DE PRODUCTEUR : sommes quinquennales de la série DREES contre les totaux imprimés par l'ONDPS (figure 2) ;
      écart nul exigé sur 2001-2005, 2006-2010, 2011-2015 ; l'écart 2016-2020 est calculé et PUBLIÉ, jamais corrigé ;
  D6  transcription ONDPS 2021-2025 : somme des admis == total imprimé ; total et admis 2025 retrouvés dans le TEXTE du
      PDF (pas seulement dans l'image) ; empreinte du PDF égale à celle de la transcription ;
  D7  diplômés à l'étranger : part croissante 2012 -> 2026 ; c'est un stock, jamais présenté comme un flux.
Autotest de mutation à chaque exécution : « quatre années » altéré -> D1 ; admis 2023 altéré -> D6 ; valeur DREES 2003
altérée -> D5.

Bilingue (06/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés, des figures -en au même dessin ;
l'art. 6 de la Constitution se cite en anglais dans la traduction du Conseil constitutionnel (vérifiée, garde D2) ; les
autres textes en français, suivis de notre traduction (clés *_tr), dont chaque nombre doit figurer dans l'original (D1 ter).

Écrit : data/promesses_delais.json (+ static/), static/promesses_delais.csv, data/figures_delais.json,
static/img/delais-{cursus,admissions}{,-en}.svg/.png. Rien n'est écrit à données identiques.
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
sys.path.insert(0, str(ROOT / "scripts" / "sources_promesses_en"))
import constitution_en as cen  # noqa: E402
SRC = ROOT / "scripts" / "sources_delais"
PAGE_URL = "stephane-lalut.com/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/"
PAGE_URL_EN = "stephane-lalut.com/en/can-a-campaign-promise-produce-results-within-five-years/"
OUT_DATA = ROOT / "data" / "promesses_delais.json"
OUT_STATIC = ROOT / "static" / "promesses_delais.json"
OUT_CSV = ROOT / "static" / "promesses_delais.csv"
OUT_FIGURES = ROOT / "data" / "figures_delais.json"
OUT_IMG = ROOT / "static" / "img"
LEGI = {"arrete_2013": "f89e9d3991814a43b91e67bcf31ffbd98b57ac38ce05d32ae5e5f74011ee913d",
        "L632-2": "804e64dca7a58af716c9d862f5a06d70b5603c7ab2690167ba5da4958e21df54",
        "R6153-1-2": "ef0a7e80801badd6e432f9b51c5e64ec546441fa8c14d102343930acf2a29dd1",
        "art6": "496783ff67a6d9cefb20a451d4d559d20101f0a63a39dad41c42448fe8c461ad"}
ART37 = "loi_2022-1616_art37_JORFARTI000046791824.xml"
MOTS = {"un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
LETTRES = {v: k for k, v in MOTS.items()}
LETTRES_EN = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
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
    "cit_dj1": "The acts performed under this regime are performed by the docteur junior alone.",
    "cit_dj2": "The docteur junior exercises his functions by delegation and under the responsibility of the practitioner he "
               "reports to.",
    "cit_dd76": "it therefore takes five to ten years (respectively for midwives and doctors) for a policy based on this "
                "lever to begin to produce its effects",
}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'")
    s = re.sub(r"\s+", " ", s)
    return re.sub(r" ([,.;:])", r"\1", s).strip()


def en(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n)


def nombres(s: str) -> set:
    return {x.replace(",", ".") for x in re.findall(r"\d+(?:[.,]\d+)?", s)}


def fr(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n).replace(",", "\u202f").replace(".", ",")


# ------------------------------------------------------------------ lecture
def lire() -> dict:
    t = {}
    for k, h in LEGI.items():
        j = json.loads((SRC / ("legifrance_%s.json" % h)).read_text(encoding="utf-8"))
        a = j["article"]
        if a.get("etat") != "VIGUEUR":
            raise Arret("source %s : article non en vigueur" % k)
        t[k] = {"id": a["id"], "texte": norm(a["texte"]), "sha": h}
    x = (SRC / ART37).read_text(encoding="utf-8")
    t["art37"] = {"id": "JORFARTI000046791824", "texte": norm(html.unescape(re.sub("<[^>]+>", " ", x))),
                  "sha": hashlib.sha256((SRC / ART37).read_bytes()).hexdigest()}
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
    import fitz
    pdf = SRC / ondps["fichier"]
    texte_pdf = norm(" ".join(p.get_text() for p in fitz.open(pdf)))
    # C6 (07/10/2026) : synthèse du Dossier n° 76 de la DREES, citée comme accord (le PDF est archivé dans sondes\delais).
    ext = (SRC / "drees_DD76_2021_page5_extrait.txt").read_text(encoding="utf-8")
    t["dd76_pdf"] = {"id": "drees_DD76_2021.pdf, page 5 (extrait archivé)", "texte": norm(re.sub(r"\s+", " ", ext)),
                     "sha": re.search(r"SHA-256 du PDF d'origine : ([0-9a-f]{64})", ext).group(1)}
    rpps = list(csv.reader(l for l in (SRC / "drees_rpps_lieu_diplome_extrait.csv").read_text(encoding="utf-8").splitlines()
                           if not l.startswith("#")))
    return {"textes": t, "dd76": serie, "ondps": ondps, "pdf_sha": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "texte_pdf": texte_pdf, "rpps": rpps}


# ------------------------------------------------------------------ calcul et gardes
def mot_avant(texte: str, unite: str, apres: str) -> int:
    m = re.search(r"\b(%s) %s" % ("|".join(MOTS), unite), texte[texte.find(apres):] if apres in texte else "")
    if not m:
        raise Arret("D1 : « %s » introuvable après « %s »" % (unite, apres[:40]))
    return MOTS[m.group(1)]


def calculer(S: dict) -> tuple[dict, list[str]]:
    g, T = [], S["textes"]
    a13 = T["arrete_2013"]["texte"]
    s1 = mot_avant(a13, "semestres", "sanctionne le premier cycle")
    s2 = mot_avant(a13, "semestres", "sanctionne le deuxième cycle")
    mg = mot_avant(T["L632-2"]["texte"], "années", "pour la spécialité de médecine générale")
    if "s'applique aux étudiants qui commencent ce troisième cycle à la rentrée de l'année universitaire 2023" not in T["art37"]["texte"]:
        raise Arret("D1 : application aux entrants de la rentrée 2023 introuvable dans l'art. 37")
    duree = s1 / 2 + s2 / 2 + mg
    g.append("D1 : cursus MG = %d + %d semestres + %d annees = %g ans (entrants en 3e cycle depuis la rentree 2023)" % (s1, s2, mg, duree))
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
    # La référence aux « deux mandats consécutifs » autorisés est retirée : elle chargeait la comparaison d'un sous-entendu.
    rapport = duree / mandat
    if rapport != int(rapport) or int(rapport) not in LETTRES:
        raise Arret("D3 : cursus %g ans / mandat %d ans = %g : la phrase « N fois la durée d'un mandat » serait fausse" % (duree, mandat, rapport))
    nmax = int(rapport)
    g.append("D3 : cursus = %d fois la duree d'un mandat (comparaison d'echelle)" % nmax)
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
    for v in (o["total_admis_2021_2025"], o["admis_medecine"]["2025"], o["capacites_2025"]):
        if fr(v).replace("\u202f", " ") not in S["texte_pdf"]:
            raise Arret("D6 : %d absent du texte du PDF" % v)
    g.append("D6 : admis 2021-2025 (%d) controles par la somme et par le texte du PDF" % o["total_admis_2021_2025"])
    h = S["rpps"][0]
    rows = {(r[1], r[2]): r for r in S["rpps"][1:]}
    i12, i26 = h.index("effectif_2012"), h.index("effectif_2026")
    tot, etr = rows[("00-Ensemble", "0-Ensemble")], rows[("99-Etranger", "0-Ensemble")]
    p12, p26 = 100 * int(etr[i12]) / int(tot[i12]), 100 * int(etr[i26]) / int(tot[i26])
    if not p26 > p12:
        raise Arret("D7 : part des diplomes a l'etranger non croissante")
    g.append("D7 : diplome a l'etranger %.1f %% (2012) -> %.1f %% (2026), stock" % (p12, p26))
    r = {"s1": s1, "s2": s2, "mg": mg, "duree": duree, "mandat": mandat, "nmax": nmax, "dd76": d, "amin": amin,
         "ecarts": ecarts, "ondps": o, "etr12": int(etr[i12]), "tot12": int(tot[i12]), "etr26": int(etr[i26]),
         "tot26": int(tot[i26]), "p12": p12, "p26": p26}
    return r, g


CITATIONS = {  # clé -> (texte source, citation exacte). Vérifiées mot pour mot (garde D1 bis) ; la page les affiche par jeton.
    "cit_cycle1": ("arrete_2013", "Le diplôme de formation générale en sciences médicales sanctionne le premier cycle ; il comprend six semestres de formation"),
    "cit_cycle2": ("arrete_2013", "Le diplôme de formation approfondie en sciences médicales, défini au présent arrêté, sanctionne le deuxième cycle ; il comprend six semestres de formation"),
    "cit_mg": ("L632-2", "qui, pour la spécialité de médecine générale, est d'une durée de quatre années"),
    "cit_37": ("art37", "La durée du troisième cycle des études de médecine pour la spécialité de médecine générale mentionnée au 2° du I s'applique aux étudiants qui commencent ce troisième cycle à la rentrée de l'année universitaire 2023."),
    "cit_art6a": ("art6", "Le Président de la République est élu pour cinq ans au suffrage universel direct."),
    "cit_supervision": ("L632-2", "La dernière année du diplôme d'études spécialisées de médecine générale est effectuée en stage, sous un régime d'autonomie supervisée"),
    "cit_dj1": ("R6153-1-2", "Les actes réalisés sous ce régime le sont par le docteur junior seul."),
    "cit_dj2": ("R6153-1-2", "Le docteur junior exerce ses fonctions par délégation et sous la responsabilité du praticien dont il relève."),
    "cit_dd76": ("dd76_pdf", "il faut ainsi compter de cinq à dix ans (respectivement pour le cas des sages-femmes et des médecins) pour qu’une politique axée sur ce levier ne commence à produire ses effets"),
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


def affichage(r: dict) -> dict:
    o = r["ondps"]
    q = o["quinquennaux_figure2"]
    return {
        "duree": LETTRES[int(r["duree"])], "duree_chiffre": "%d" % r["duree"], "mandat": LETTRES[r["mandat"]],
        "nmax": LETTRES[r["nmax"]], "nfois": LETTRES[r["nmax"]] + " fois", "ecart_pct": fr(100 * abs(r["ecarts"]["2016-2020"]) / r["ondps"]["quinquennaux_figure2"]["2016-2020"], 1), "cycle1": LETTRES[r["s1"]], "cycle2": LETTRES[r["s2"]], "mg": LETTRES[r["mg"]],
        "an_min": str(r["amin"]), "places_min": fr(r["dd76"][r["amin"]]), "places_1972": fr(r["dd76"][1972]),
        "places_2020": fr(r["dd76"][2020]), "rapport_baisse": fr(r["dd76"][1972] / r["dd76"][r["amin"]], 1),
        "admis_2025": fr(o["admis_medecine"]["2025"]), "capacites_2025": fr(o["capacites_2025"]),
        "admis_2021_2025": fr(o["total_admis_2021_2025"]), "onp": fr(o["onp_2021_2025"]),
        "admis_2016_2020": fr(q["2016-2020"]),
        "hausse_quinquennale": fr(100 * (o["total_admis_2021_2025"] / q["2016-2020"] - 1), 0),
        "ecart_2016_2020": fr(abs(r["ecarts"]["2016-2020"])),
        "etr_p12": fr(r["p12"], 1), "etr_p26": fr(r["p26"], 1), "etr_26": fr(r["etr26"]), "tot_26": fr(r["tot26"]),
        "releve_le": "06/10/2026 (textes lus sur Légifrance les 05 et 06/10/2026 ; DREES, 2 juillet 2026 ; ONDPS, 19 décembre 2025)",
    }


def affichage_en(r: dict) -> dict:
    o = r["ondps"]
    q = o["quinquennaux_figure2"]
    return {
        "duree": LETTRES_EN[int(r["duree"])], "duree_chiffre": "%d" % r["duree"], "mandat": LETTRES_EN[r["mandat"]],
        "nmax": LETTRES_EN[r["nmax"]],
        "nfois": {1: "once", 2: "twice", 3: "three times"}.get(r["nmax"], LETTRES_EN[r["nmax"]] + " times"), "ecart_pct": en(100 * abs(r["ecarts"]["2016-2020"]) / q["2016-2020"], 1),
        "cycle1": LETTRES_EN[r["s1"]], "cycle2": LETTRES_EN[r["s2"]], "mg": LETTRES_EN[r["mg"]],
        "an_min": str(r["amin"]), "places_min": en(r["dd76"][r["amin"]]), "places_1972": en(r["dd76"][1972]),
        "places_2020": en(r["dd76"][2020]), "rapport_baisse": en(r["dd76"][1972] / r["dd76"][r["amin"]], 1),
        "admis_2025": en(o["admis_medecine"]["2025"]), "capacites_2025": en(o["capacites_2025"]),
        "admis_2021_2025": en(o["total_admis_2021_2025"]), "onp": en(o["onp_2021_2025"]),
        "admis_2016_2020": en(q["2016-2020"]),
        "hausse_quinquennale": en(100 * (o["total_admis_2021_2025"] / q["2016-2020"] - 1), 0),
        "ecart_2016_2020": en(abs(r["ecarts"]["2016-2020"])),
        "etr_p12": en(r["p12"], 1), "etr_p26": en(r["p26"], 1), "etr_26": en(r["etr26"]), "tot_26": en(r["tot26"]),
        "releve_le": "6 October 2026 (texts read on Légifrance on 5 and 6 October 2026; DREES, 2 July 2026; ONDPS, 19 December 2025)",
    }


# ------------------------------------------------------------------ figures
W = 720
BLEU, BLEU_CLAIR, GRIS, GRIS_CLAIR = "#184f95", "#7fa3cf", "#8a8f98", "#c9cdd3"
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


T = {
    "fr": {"src1": "Arrêté du 8 avril 2013, art. 1 ; code de l'éducation, art. L632-2 ; loi n° 2022-1616, art. 37 ; Constitution, art. 6 (Légifrance)",
           "note1": "Comparaison d'échelle seulement : ni l'effet d'une politique, ni la date de ses premiers effets. Durées minimales ; soins avant la fin du cursus.",
           "src2": "DREES, Dossier n° 76 (2021), graphique 8, source ONDPS (1972-2020) ; ONDPS, bilan 2021-2025 (admis)",
           "note2": "Places pourvues ; champ élargi aux passerelles et droits au remords à partir de 2010-2011 ; numerus apertus depuis 2021.",
           "t1": "Former un médecin généraliste, et la durée d'un mandat présidentiel",
           "s1": "en années, durées minimales écrites dans les textes en vigueur",
           "d1": "Deux barres de même échelle. En haut, le cursus de médecine générale : {a} ans de premier cycle, {b} ans de "
                 "deuxième cycle, {c} ans de troisième cycle, soit {d} ans. En bas, un mandat présidentiel de {e} ans. Comparaison "
                 "d'échelle seulement.",
           "mg": "Médecine générale", "cycles": ["1er cycle", "2e cycle", "3e cycle", "4e année"],
           "auto": "dernière année : autonomie supervisée", "mandat": "Mandat présidentiel", "ans": "{} ans",
           "t2": "Admissions en études de médecine, 1972-2025, à leur année",
           "s2": "places pourvues jusqu'en 2020 (DREES, ONDPS), admis depuis 2021 (ONDPS)",
           "d2": "Barres annuelles : {places_1972} places en 1972, minimum de {places_min} en {an_min}, {places_2020} en 2020 ; puis de "
                 "{min_admis} à {admis_2025} admis par an de 2021 à 2025.",
           "r1": "2010-2011 : passerelles incluses", "r2": "2021 : numerus apertus", "annot": "%s : %s"},
    "en": {"src1": "Order of 8 April 2013, art. 1; Education Code, art. L632-2; Law no. 2022-1616, art. 37; Constitution, art. 6",
           "note1": "Comparison of scale only: neither the effect of a policy nor the date of its first effects. Minimum durations; care before the end.",
           "src2": "DREES, Dossier no. 76 (2021), chart 8, source ONDPS (1972-2020); ONDPS, 2021-2025 report (admissions)",
           "note2": "Places filled; scope widened to alternative-entry routes (passerelles) and reorientation entries (droit au remords) from 2010-2011; numerus apertus since 2021.",
           "t1": "Training a general practitioner in France, and the length of a presidential term",
           "s1": "in years, minimum durations written in the texts in force",
           "d1": "Two bars on the same scale. Above, the general practice curriculum: {a} years of first cycle, {b} years of second "
                 "cycle, {c} years of third cycle, {d} years in all. Below, a presidential term of {e} years. Comparison of scale only.",
           "mg": "General practice", "cycles": ["1st cycle", "2nd cycle", "3rd cycle", "4th year"],
           "auto": "last year: supervised autonomy", "mandat": "Presidential term", "ans": "{} years",
           "t2": "Admissions to medical studies in France, 1972-2025, by year",
           "s2": "places filled until 2020 (DREES, ONDPS), admissions since 2021 (ONDPS)",
           "d2": "Annual bars: {places_1972} places in 1972, a minimum of {places_min} in {an_min}, {places_2020} in 2020; then from "
                 "{min_admis} to {admis_2025} admissions a year from 2021 to 2025.",
           "r1": "2010-2011: passerelles included", "r2": "2021: numerus apertus", "annot": "%s: %s"},
}


def fig_cursus(r: dict, A: dict) -> str:
    H = 200
    x0, x1 = 120, W - 10
    an = x1 - x0
    X = lambda a: x0 + a / r["duree"] * an  # noqa: E731
    L = T[LANG]
    e = cadre(H, "dc", L["t1"], L["s1"], L["d1"].format(a="%g" % (r["s1"] / 2), b="%g" % (r["s2"] / 2), c=r["mg"],
                                                          d=A["duree_chiffre"], e=r["mandat"]))
    y = 70
    segs = [(0, r["s1"] / 2, L["cycles"][0], GRIS_CLAIR), (r["s1"] / 2, r["s2"] / 2, L["cycles"][1], GRIS_CLAIR),
            (r["s1"] / 2 + r["s2"] / 2, r["mg"] - 1, L["cycles"][2], BLEU_CLAIR), (r["duree"] - 1, 1, L["cycles"][3], BLEU)]
    e.append(txt(0, y + 21, L["mg"], 11, INK, weight="600"))
    for a0, l, lab, col in segs:
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="32" fill="%s" stroke="#ffffff" stroke-width="2"/>' % (X(a0), y, X(a0 + l) - X(a0), col))
        e.append(txt((X(a0) + X(a0 + l)) / 2, y + 20, lab, 10, "#ffffff" if col == BLEU else INK, "middle"))
    e.append(txt(X(r["duree"]), y + 46, L["auto"], 9, BLEU, "end"))
    y2 = 132
    e.append(txt(0, y2 + 21, L["mandat"], 11, INK, weight="600"))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="32" fill="%s"/>' % (X(0), y2, X(r["mandat"]) - X(0), GRIS))
    e.append(txt(X(r["mandat"] / 2), y2 + 20, L["ans"].format(r["mandat"]), 10, "#ffffff", "middle"))
    e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(0), y2 + 33, X(r["duree"]), y2 + 33, GRID))
    for a in range(0, int(r["duree"]) + 1):
        e.append(txt(X(a), y2 + 50, str(a), 9, MUTED, "middle"))
    e += cartouche(H, L["src1"], L["note1"])
    e.append("</svg>")
    return "\n".join(e)


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
    for a, lab in ((2010, L["r1"]), (2021, L["r2"])):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (X(a), y0 - 4, X(a), y1, INK2))
        e.append(txt(X(a) - 4, y0 - 8, lab, 9, INK2, "end"))
    voisins = max(d[a] for a in range(r["amin"] - 2, r["amin"] + 3))
    ya = Y(voisins) - 22
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (X(r["amin"]) + bw / 2, ya + 4, X(r["amin"]) + bw / 2, Y(d[r["amin"]]) - 2, INK2))
    e.append(txt(X(r["amin"]) + bw / 2, ya, (L["annot"] % (r["amin"], A["places_min"])), 10, INK, "middle", "600"))
    e += cartouche(H, L["src2"], L["note2"])
    e.append("</svg>")
    return "\n".join(e)


MONTRE_EN = {
    "cursus": "Under the rules in force for students who entered the third cycle from the start of the 2023 academic year, the "
              "standard general practice curriculum in France takes at least {duree} years from the first year, {nfois} the "
              "length of a presidential term. Comparison of scale only.",
    "admissions": "Places in French medical studies were divided by {rapport_baisse} between 1972 and {an_min} ({places_min} "
                  "places), then rose again; {admis_2021_2025} students were admitted from 2021 to 2025.",
}


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    montre = {
        "cursus": ("delais-cursus", "Aux règles en vigueur pour les étudiants entrés en troisième cycle depuis la rentrée 2023, le "
                   "cursus standard de médecine générale dure au moins %s ans depuis la première année, soit %s fois la durée "
                   "d'un mandat présidentiel. Comparaison d'échelle seulement." % (A["duree"], A["nmax"])),
        "admissions": ("delais-admissions", "Les places en études de médecine ont été divisées par %s entre 1972 et %s (%s places), "
                       "puis sont remontées ; %s étudiants ont été admis de 2021 à 2025." % (A["rapport_baisse"], A["an_min"],
                                                                                          A["places_min"], A["admis_2021_2025"])),
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


def autotest(S: dict) -> list[str]:
    out = []
    for nom, mut, pref in (
            ("quatre annees altere", lambda m: m["textes"]["L632-2"].__setitem__(
                "texte", m["textes"]["L632-2"]["texte"].replace("d'une durée de quatre années", "d'une durée de trois années")), "D3"),
            ("admis 2023 altere", lambda m: m["ondps"]["admis_medecine"].__setitem__("2023", 10982), "D6"),
            ("DREES 2003 altere", lambda m: m["dd76"].__setitem__(2003, 5200), "D5")):
        m = copy.deepcopy(S)
        mut(m)
        try:
            calculer(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
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
    S = lire()
    r, g = calculer(S)
    for m in autotest(S):
        log("autotest : la mutation a mordu : " + m)
    cit = citations(S["textes"])
    A = dict(affichage(r), **cit)
    A.update({k + "_tr": v for k, v in TR.items()})
    A["cit_art6a_en"] = CIT_ART6_EN
    A_en = dict(affichage_en(r), **cit)
    A_en.update({k + "_tr": v for k, v in TR.items()})
    A_en["cit_art6a_en"] = CIT_ART6_EN
    if set(A) != set(A_en):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    g.append("D1 bis : %d citations des textes retrouvees mot pour mot ; D1 ter : %d traductions, nombres controles"
             % (len(CITATIONS), len(TR)))
    if "--check" in sys.argv[1:]:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        figs["delais-cursus%s.svg" % suf] = fig_cursus(r, AA)
        figs["delais-admissions%s.svg" % suf] = fig_admissions(r, AA)
    LANG = "fr"
    fi = fiches(figs, A, A_en)
    csvt = csv_texte(r)
    T = S["textes"]
    payload = {
        "releve_le": "2026-10-06",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Légifrance (DILA), DREES, ONDPS",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Délais, E1 à E3",
                 "textes": {k: {"id": v["id"], "sha256": v["sha"]} for k, v in T.items()},
                 "definitions": {
                     "duree_cursus": "somme des durées minimales écrites (sans redoublement, interruption ni passerelle), "
                                     "pour les étudiants qui commencent le troisième cycle à partir de la rentrée 2023",
                     "places_pourvues": "jusqu'en 2009, numerus clausus principal ; à partir de 2011 (2010 partiellement), "
                                        "numerus clausus principal et complémentaire, passerelles et droits au remords "
                                        "(DREES, note du graphique 8)",
                     "diplome_etranger": "médecins actifs au 1er janvier dont le diplôme a été obtenu à l'étranger : un "
                                         "stock, pas un flux d'arrivées ; le lieu du diplôme ne dit pas la nationalité"},
                 "ecart_documente": {"2016-2020": "la somme des valeurs DREES dépasse de %d le total imprimé par l'ONDPS ; "
                                                  "non expliqué (la valeur 2020 de la DREES porte un astérisque sans légende "
                                                  "trouvée) ; publié, non corrigé" % r["ecarts"]["2016-2020"]}},
        "gardes": g,
        "calcul": {k: v for k, v in r.items() if k not in ("dd76", "ondps")},
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
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")), output_width=1440,
                         background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_delais.json, static/promesses_delais.{json,csv}, data/figures_delais.json, 4 figures SVG + PNG (FR, EN)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
