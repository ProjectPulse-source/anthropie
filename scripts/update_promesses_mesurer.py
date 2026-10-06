#!/usr/bin/env python3
"""Volet « Mesurer » du dossier Promesses : deux mesures du chômage, deux populations, et la règle qui change.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 5, E1 et E2 (v2,
gelée au commit dfd0ec9 ; arbitrage PRO-20261005-164029).

E1 — restitution de l'ESTIMATION Insee (Insee Références « Emploi, chômage, revenus du travail », éd. 2026, dossier 1,
figure 2, moyenne 2024) : trois ensembles disjoints tirés des EFFECTIFS, jamais de parts arrondies. Énoncé autorisé :
« deux définitions, des populations qui se recoupent partiellement ».
E2 — rupture administrative du 1er janvier 2025 (loi pour le plein emploi) : séries publiées par la Dares (catégorie
A et « A hors RSA et hors jeunes en parcours », France hors Mayotte, CVS-CJO), sans aucun écart calculé comme effet.

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  M1  champ et année imprimés dans le tableur = ceux du protocole (France hors Mayotte, 15-64 ans, logement ordinaire, 2024) ;
  M2  additivité des effectifs de la figure 2 (lignes et colonnes) à l'arrondi publié près (± 1 millier par cellule) ;
  M3  « se recoupent partiellement » : intersection et deux ensembles exclusifs strictement positifs au-delà de la
      précision de restitution (> 2 milliers, soit deux arrondis) ;
  M4  CONTRÔLE DE DÉFINITION : les trois ensembles restitués depuis la figure 2 égalent ceux que l'Insee imprime dans
      un autre tableau, la figure 8 (lignes (1), (2), (3)) ; écart nul exigé ;
  M5  cohérence algébrique (déclarée comme telle, jamais appelée témoin) : les parts publiées 49 % et 62 % se
      retrouvent depuis les effectifs, à l'arrondi ;
  M6  séries Dares : présence des deux séries, champ « France », CVS-CJO ; la série « hors RSA » commence en 2018-T1.
Le TÉMOIN d'extraction indépendant (lecture du PDF par une chaîne écrite séparément) est exécuté hors de ce script :
D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/test_decisif/mesurer_e1/.
Autotest de mutation à chaque exécution : effectif du commun altéré -> M4 ; parts permutées -> M5 ; champ altéré -> M1.

Écrit : data/promesses_mesurer.json (+ static/), static/promesses_mesurer.csv (UTF-8 BOM, format long),
data/figures_mesurer.json, static/img/mesurer-recoupement.svg/.png, static/img/mesurer-regle.svg/.png.
Sources brutes archivées dans scripts/sources_mesurer/ (empreintes). Rien n'est écrit à données identiques.
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
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRCDIR = ROOT / "scripts" / "sources_mesurer"
URL_XLSX = "https://www.insee.fr/fr/statistiques/fichier/8733119/ECRT2026-D1.xlsx"
URL_DARES = ("https://data.dares.travail-emploi.gouv.fr/api/explore/v2.1/catalog/datasets/"
             "dares_defm_stock_france_cvs_trim/exports/csv?use_labels=true")
URL_DARES_META = "https://data.dares.travail-emploi.gouv.fr/api/explore/v2.1/catalog/datasets/dares_defm_stock_france_cvs_trim"
PAGE_URL = "stephane-lalut.com/comment-savoir-si-une-promesse-est-tenue/"
PAGE_URL_EN = "stephane-lalut.com/en/how-to-tell-whether-a-promise-was-kept/"
# Bilingue (06/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux mêmes clés, des figures -en au même dessin.
OUT_DATA = ROOT / "data" / "promesses_mesurer.json"
OUT_STATIC = ROOT / "static" / "promesses_mesurer.json"
OUT_CSV = ROOT / "static" / "promesses_mesurer.csv"
OUT_FIGURES = ROOT / "data" / "figures_mesurer.json"
OUT_IMG = ROOT / "static" / "img"
CHAMP_ATTENDU = "France hors Mayotte, personnes âgées de 15 à 64 ans, vivant dans un logement ordinaire."
STATUTS = ["En emploi", "Chômeur", "Inactif dans le halo", "Inactif hors halo"]
CATS = ["Catégorie A", "Catégorie B", "Catégorie C", "Catégorie D", "Catégorie E", "Non inscrits"]


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def fr(n: float, dec: int = 0) -> str:
    s = ("{:,.%df}" % dec).format(n).replace(",", "\u202f").replace(".", ",")
    return s


def nb(s: str) -> str:
    return s.replace("\u00a0", " ").strip()


# ------------------------------------------------------------------ relevé (source, sinon archive locale, et on le dit)
def charger(url: str, nom: str) -> tuple[bytes, str]:
    SRCDIR.mkdir(parents=True, exist_ok=True)
    p = SRCDIR / nom
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com generateur (contact via site)"})
        with urllib.request.urlopen(req, timeout=90) as r:
            b = r.read()
        origine = "source"
        if not p.exists() or p.read_bytes() != b:
            p.write_bytes(b)
    except Exception as e:  # noqa: BLE001
        if not p.exists():
            raise Arret("source %s injoignable et aucune archive locale (%s)" % (url, e))
        b, origine = p.read_bytes(), "archive locale (source injoignable : %s)" % type(e).__name__
    return b, origine


def lire_insee(b: bytes) -> dict:
    import openpyxl
    wb = openpyxl.load_workbook(io.BytesIO(b), data_only=True)
    f2 = [list(r) for r in wb["Figure 2"].iter_rows(values_only=True) if any(c is not None for c in r)]
    titre = f2[0][0]
    entete = list(f2[1][1:8])
    if entete != CATS + ["Ensemble"]:
        raise Arret("figure 2 : en-tete inattendue %s" % entete)
    eff, i = {}, 3
    for k in range(5):
        r = f2[i + k]
        eff[r[0]] = dict(zip(CATS + ["Ensemble"], r[1:8]))
    textes = [r[0] for r in f2 if r and isinstance(r[0], str)]
    champ = next((nb(t[len("Champ :"):]) for t in textes if nb(t).startswith("Champ :")), "")
    source = next((nb(t) for t in textes if t.startswith("Source")), "")
    parts_cat = {}
    j = next(k for k, r in enumerate(f2) if r[0] and str(r[0]).startswith("Part dans la catégorie"))
    for k in range(1, 6):
        r = f2[j + k]
        parts_cat[r[0]] = dict(zip(CATS + ["Ensemble"], r[1:8]))
    jj = next(k for k, r in enumerate(f2) if r[0] and str(r[0]).startswith("Part dans le statut"))
    parts_stat = {}
    for k in range(1, 6):
        r = f2[jj + k]
        parts_stat[r[0]] = dict(zip(CATS + ["Ensemble"], r[1:8]))
    f8 = [[c for c in r if c is not None] for r in wb["Figure 8"].iter_rows(values_only=True)]
    f8d = {}
    for r in f8:
        if r and isinstance(r[0], str) and len(r) >= 3 and isinstance(r[1], (int, float)):
            f8d[nb(r[0])] = {"2024": r[1], "2021": r[2]}
    return {"titre": nb(titre), "eff": eff, "champ": champ, "source": source, "parts_cat": parts_cat,
            "parts_stat": parts_stat, "f8": f8d}


def lire_dares(b: bytes) -> dict:
    rows = list(csv.DictReader(io.StringIO(b.decode("utf-8-sig")), delimiter=";"))
    out = {}
    for cat, cle in (("A", "a"), ("A hors RSA et hors jeunes en parcours", "a_hors")):
        s = {r["Date"]: int(r["Nombre de demandeurs d'emploi"]) for r in rows
             if r["Champ"] == "France" and r["Catégorie"] == cat and r["Sexe"] == "Total" and r["Tranche d'âge"] == "Total"
             and r["Ancienneté"] == "Total" and r["Type de données"] == "cvs-cjo" and r["Nombre de demandeurs d'emploi"]}
        out[cle] = dict(sorted(s.items()))
    return out


# ------------------------------------------------------------------ calcul et gardes
def calculer(I: dict, D: dict) -> tuple[dict, list[str]]:
    g = []
    if "2024" not in I["titre"] or I["champ"] != CHAMP_ATTENDU:
        raise Arret("M1 : annee ou champ de la figure 2 differents du protocole (%r / %r)" % (I["titre"][-30:], I["champ"]))
    g.append("M1 : figure 2, moyenne 2024, champ « %s »" % I["champ"])
    E = I["eff"]
    for s in STATUTS + ["Ensemble"]:
        if abs(sum(E[s][c] for c in CATS) - E[s]["Ensemble"]) > len(CATS):
            raise Arret("M2 : ligne %s non additive" % s)
    for c in CATS + ["Ensemble"]:
        if abs(sum(E[s][c] for s in STATUTS) - E["Ensemble"][c]) > len(STATUTS):
            raise Arret("M2 : colonne %s non additive" % c)
    g.append("M2 : effectifs additifs a l'arrondi publie pres")
    commun = E["Chômeur"]["Catégorie A"]
    bit_seul = E["Chômeur"]["Ensemble"] - commun
    a_seul = E["Ensemble"]["Catégorie A"] - commun
    if not (commun > 2 and bit_seul > 2 and a_seul > 2):
        raise Arret("M3 : « se recoupent partiellement » faux (commun %s, BIT seul %s, A seul %s)" % (commun, bit_seul, a_seul))
    g.append("M3 : recoupement partiel (commun %d, BIT hors A %d, A hors BIT %d milliers)" % (commun, bit_seul, a_seul))
    f8 = I["f8"]
    k1 = next(k for k in f8 if k.startswith("Inscrits en catégorie A et non chômeurs"))
    k2 = next(k for k in f8 if k.startswith("Inscrits en catégorie A et chômeurs"))
    k3 = next(k for k in f8 if k.startswith("Chômeurs et non inscrits en catégorie A"))
    if (f8[k1]["2024"], f8[k2]["2024"], f8[k3]["2024"]) != (a_seul, commun, bit_seul):
        raise Arret("M4 : restitution figure 2 (%d, %d, %d) != figure 8 (%s, %s, %s)"
                    % (a_seul, commun, bit_seul, f8[k1]["2024"], f8[k2]["2024"], f8[k3]["2024"]))
    g.append("M4 : les trois ensembles restitues egalent la figure 8 imprimee")
    p_a = 100 * commun / E["Ensemble"]["Catégorie A"]
    p_b = 100 * commun / E["Chômeur"]["Ensemble"]
    if round(p_a) != I["parts_cat"]["Chômeur"]["Catégorie A"] or round(p_b) != I["parts_stat"]["Chômeur"]["Catégorie A"]:
        raise Arret("M5 : parts publiees non retrouvees (%.1f/%s ; %.1f/%s)"
                    % (p_a, I["parts_cat"]["Chômeur"]["Catégorie A"], p_b, I["parts_stat"]["Chômeur"]["Catégorie A"]))
    g.append("M5 (coherence algebrique, non temoin) : 49 et 62 % retrouves")
    if not D["a"] or not D["a_hors"] or min(D["a_hors"]) != "2018-T1":
        raise Arret("M6 : series Dares absentes ou debut inattendu (%s)" % (min(D["a_hors"]) if D["a_hors"] else None))
    g.append("M6 : series Dares A (%s-%s) et A hors RSA (%s-%s)" % (min(D["a"]), max(D["a"]), min(D["a_hors"]), max(D["a_hors"])))
    r = {"commun": commun, "bit_seul": bit_seul, "a_seul": a_seul, "bit_total": E["Chômeur"]["Ensemble"],
         "a_total": E["Ensemble"]["Catégorie A"], "p_a": p_a, "p_b": p_b,
         "bit_non_inscrits": E["Chômeur"]["Non inscrits"],
         "bit_bc": E["Chômeur"]["Catégorie B"] + E["Chômeur"]["Catégorie C"],
         "bit_de": E["Chômeur"]["Catégorie D"] + E["Chômeur"]["Catégorie E"],
         "a_halo": E["Inactif dans le halo"]["Catégorie A"], "a_hors_halo": E["Inactif hors halo"]["Catégorie A"],
         "a_emploi": E["En emploi"]["Catégorie A"],
         "f8_2021": {"commun": f8[k2]["2021"], "a_seul": f8[k1]["2021"], "bit_seul": f8[k3]["2021"]},
         "dares_a": D["a"], "dares_a_hors": D["a_hors"], "eff": E}
    return r, g


def affichage_en(r: dict) -> dict:
    def m(v):  # thousands -> "1.43 million" or "863,000"
        return ("%.2f million" % (v / 1000)) if v >= 1000 else "{:,.0f}".format(v * 1000)
    da, dh = r["dares_a"], r["dares_a_hors"]
    t_fin = max(da)
    e = lambda v, d=0: ("{:,.%df}" % d).format(v)  # noqa: E731
    return {
        "commun": m(r["commun"]), "bit_seul": m(r["bit_seul"]), "a_seul": m(r["a_seul"]),
        "commun_env": "about " + m(r["commun"]), "a_seul_env": "about " + m(r["a_seul"]),
        "bit_total": m(r["bit_total"]), "a_total": m(r["a_total"]),
        "p_a": e(r["p_a"]), "p_b": e(r["p_b"]),
        "bit_non_inscrits": m(r["bit_non_inscrits"]), "bit_bc": m(r["bit_bc"]), "bit_de": m(r["bit_de"]),
        "a_halo": m(r["a_halo"]), "a_hors_halo": m(r["a_hors_halo"]), "a_emploi": m(r["a_emploi"]),
        "commun_2021": m(r["f8_2021"]["commun"]), "a_seul_2021": m(r["f8_2021"]["a_seul"]),
        "bit_seul_2021": m(r["f8_2021"]["bit_seul"]),
        "dares_fin": "%s quarter of %s" % ({"1": "first", "2": "second", "3": "third", "4": "fourth"}[t_fin[-1]], t_fin[:4]),
        "dares_a_fin": m(da[t_fin] / 1000), "dares_a_hors_fin": m(dh[max(dh)] / 1000),
        "dares_a_2024t4": m(da["2024-T4"] / 1000), "dares_a_hors_2024t4": m(dh["2024-T4"] / 1000),
    }


def affichage(r: dict) -> dict:
    def m(v):  # milliers -> « 1,43 million » ou « 863 000 »
        return (fr(v / 1000, 2) + " million" + ("s" if v >= 2000 else "")) if v >= 1000 else fr(v * 1000, 0)
    da, dh = r["dares_a"], r["dares_a_hors"]
    t_fin = max(da)
    return {
        "commun": m(r["commun"]), "bit_seul": m(r["bit_seul"]), "a_seul": m(r["a_seul"]),
        "commun_env": "environ " + m(r["commun"]), "a_seul_env": "environ " + m(r["a_seul"]),
        "bit_total": m(r["bit_total"]), "a_total": m(r["a_total"]),
        "p_a": fr(r["p_a"], 0), "p_b": fr(r["p_b"], 0),
        "bit_non_inscrits": m(r["bit_non_inscrits"]), "bit_bc": m(r["bit_bc"]), "bit_de": m(r["bit_de"]),
        "a_halo": m(r["a_halo"]), "a_hors_halo": m(r["a_hors_halo"]), "a_emploi": m(r["a_emploi"]),
        "commun_2021": m(r["f8_2021"]["commun"]), "a_seul_2021": m(r["f8_2021"]["a_seul"]),
        "bit_seul_2021": m(r["f8_2021"]["bit_seul"]),
        "dares_fin": t_fin.replace("-T", "e trimestre ").split(" ")[1] + " " + t_fin[:4] if False else
        "%s trimestre %s" % ({"1": "1er", "2": "2e", "3": "3e", "4": "4e"}[t_fin[-1]], t_fin[:4]),
        "dares_a_fin": m(da[t_fin] / 1000), "dares_a_hors_fin": m(dh[max(dh)] / 1000),
        "dares_a_2024t4": m(da["2024-T4"] / 1000), "dares_a_hors_2024t4": m(dh["2024-T4"] / 1000),
    }


# ------------------------------------------------------------------ figures (charte des dossiers du site)
W = 720
BLEU, GRIS, GRIS_CLAIR = "#184f95", "#8a8f98", "#c9cdd3"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LANG = "fr"


def nbl(v) -> str:  # nombre selon la langue de la figure (nb() normalise du texte, plus haut)
    return "{:,.0f}".format(v) if LANG == "en" else fr(v)


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def cadre(H: int, ident: str, titre: str, sous: str, desc: str) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H + 48, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def cartouche(H: int, src: str, note: str) -> list[str]:
    out = ['<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (H + 2, W, H + 2, GRID)]
    for k, (t, c) in enumerate(((src, INK2), (note, INK2), (LICENCES[LANG], MUTED))):
        out.append('<text x="0" y="%d" font-size="9" fill="%s">%s</text>' % (H + 15 + 12 * k, c, esc(t)))
    return out


T = {
    "fr": {"src1": "Insee Références, Emploi, chômage, revenus du travail, éd. 2026, dossier 1, figures 2 et 8 (appariement Dares-Insee-France Travail)",
           "note1": "Estimation de l'Insee, moyenne 2024, France hors Mayotte, 15-64 ans, logement ordinaire ; deux définitions distinctes.",
           "src2": "Dares et France Travail, inscrits en fin de trimestre, France hors Mayotte, données CVS-CJO (série « hors RSA » depuis 2018)",
           "note2": "Champ et période différents de la figure du croisement 2024. Labellisation suspendue pour la période du 01/01/2025 au 20/05/2026.",
           "t1": "Chômeurs au sens du BIT et inscrits en catégorie A, 2024",
           "s1": "deux définitions, des populations qui se recoupent en partie (en milliers de personnes)",
           "d1": "Barre en trois segments : {bit_seul} chômeurs au sens du BIT non inscrits en catégorie A, {commun} personnes dans les deux "
                 "à la fois, {a_seul} inscrits en catégorie A non chômeurs au sens du BIT (estimation Insee, 2024).",
           "bit": "Chômeurs au sens du BIT : %s", "insc": "Inscrits en catégorie A à France Travail : %s",
           "dont1": "dont : non inscrits %s ; inscrits en B ou C %s ;", "dont2": "inscrits en D ou E %s",
           "dont3": "dont : halo autour du chômage %s ;", "dont4": "inactifs hors halo %s ; en emploi %s", "deux": "dans les deux",
           "t2": "Inscrits en catégorie A : série publiée et série hors bénéficiaires du RSA et jeunes en parcours",
           "s2": "France hors Mayotte, fin de trimestre, données CVS-CJO ; même échelle pour les deux panneaux",
           "d2": "Deux panneaux de 2018 à %s, sur la même échelle : à gauche la catégorie A publiée, à droite la série hors "
                 "bénéficiaires du RSA et hors jeunes en parcours ; dans chacun, une ligne marque le 1er janvier 2025, changement de règles.",
           "p1": "Catégorie A publiée", "p2": "Hors bénéficiaires du RSA et jeunes en parcours",
           "rupture": "01/01/2025 : changement de règles",
           "ecart": "Cet écart entre panneaux ne mesure pas l'effet de la réforme : ce sont deux populations distinctes.",
           "M": lambda v: fr(v / 1e6, 1) + " M"},
    "en": {"src1": "Insee Références, Emploi, chômage, revenus du travail, 2026 ed., file 1, figures 2 and 8 (Dares-Insee-France Travail matching)",
           "note1": "Insee estimate, 2024 average, France excluding Mayotte, aged 15-64, ordinary housing; two distinct definitions.",
           "src2": "Dares and France Travail, registrants at end of quarter, France excluding Mayotte, seasonally adjusted (series 'excluding RSA' since 2018)",
           "note2": "Scope and period differ from the 2024 cross-tabulation figure. Official label suspended for 1 Jan. 2025 to 20 May 2026.",
           "t1": "ILO-unemployed and category A registrants in France, 2024",
           "s1": "two definitions, populations that partly overlap (thousands of people)",
           "d1": "Bar in three segments: {bit_seul} ILO-unemployed not registered in category A, {commun} people in both at once, {a_seul} "
                 "category A registrants who are not ILO-unemployed (Insee estimate, 2024).",
           "bit": "Unemployed (ILO definition): %s", "insc": "Registered in category A at France Travail: %s",
           "dont1": "of whom: not registered %s; registered in B or C %s;", "dont2": "registered in D or E %s",
           "dont3": "of whom: halo around unemployment %s;", "dont4": "inactive outside the halo %s; in work %s", "deux": "in both",
           "t2": "Category A registrants: published series and series without RSA recipients or youth programmes",
           "s2": "France excluding Mayotte, end of quarter, seasonally and working-day adjusted; same scale for both panels",
           "d2": "Two panels from 2018 to %s, on the same scale: left, published category A; right, the series excluding RSA recipients "
                 "and young people in programmes; in each, a line marks 1 January 2025, change of rules.",
           "p1": "Published category A", "p2": "Excluding RSA recipients and young people in programmes",
           "rupture": "1 Jan. 2025: change of rules",
           "ecart": "This gap between panels does not measure the effect of the reform: they are two distinct populations.",
           "M": lambda v: "%.1fm" % (v / 1e6)},
}


def fig_recoupement(r: dict, A: dict) -> str:
    H = 270
    x0, x1 = 0, W
    tot = r["bit_seul"] + r["commun"] + r["a_seul"]
    X = lambda v: x0 + v / tot * (x1 - x0)  # noqa: E731
    y, h = 118, 46
    L = T[LANG]
    e = cadre(H, "mr", L["t1"], L["s1"], L["d1"].format(**A))
    a, b = X(r["bit_seul"]), X(r["bit_seul"] + r["commun"])
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (x0, y, a - x0, h, GRIS_CLAIR))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (a, y, b - a, h, BLEU))
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (b, y, x1 - b, h, GRIS_CLAIR))
    e.append(txt((x0 + a) / 2, y + 28, nbl(r["bit_seul"]), 15, INK, "middle", "600"))
    e.append(txt((a + b) / 2, y + 28, nbl(r["commun"]), 15, "#ffffff", "middle", "600"))
    e.append(txt((b + x1) / 2, y + 28, nbl(r["a_seul"]), 15, INK, "middle", "600"))
    # accolades : au-dessus, les chômeurs BIT ; au-dessous, les inscrits en A
    e.append('<path d="M%.1f %d v-8 H%.1f v8" fill="none" stroke="%s" stroke-width="1.5"/>' % (x0 + 1, y - 6, b, INK2))
    e.append(txt((x0 + b) / 2, y - 20, L["bit"] % nbl(r["bit_total"]), 12, INK, "middle", "600"))
    e.append('<path d="M%.1f %d v8 H%.1f v-8" fill="none" stroke="%s" stroke-width="1.5"/>' % (a, y + h + 6, x1 - 1, INK2))
    e.append(txt((a + x1) / 2, y + h + 30, L["insc"] % nbl(r["a_total"]), 12, INK, "middle", "600"))
    yy = y + h + 62
    e.append(txt(x0, yy, L["dont1"] % (nbl(r["bit_non_inscrits"]), nbl(r["bit_bc"])), 10, INK2))
    e.append(txt(x0, yy + 13, L["dont2"] % nbl(r["bit_de"]), 10, INK2))
    e.append(txt(x1, yy, L["dont3"] % nbl(r["a_halo"]), 10, INK2, "end"))
    e.append(txt(x1, yy + 13, L["dont4"] % (nbl(r["a_hors_halo"]), nbl(r["a_emploi"])), 10, INK2, "end"))
    e.append(txt((a + b) / 2, yy, L["deux"], 10, BLEU, "middle", "600"))
    e += cartouche(H, L["src1"], L["note1"])
    e.append("</svg>")
    return "\n".join(e)


def fig_regle(r: dict, A: dict) -> str:
    """Deux PANNEAUX sur la même échelle (contre-expertise PRO-20261005-183942, P6) : deux courbes superposées autour
    d'une date se lisent comme une quasi-expérience ; deux panneaux séparés disent deux populations."""
    H = 360
    da, dh = r["dares_a"], r["dares_a_hors"]
    cles = list(dh)  # 2018-T1 -> fin
    tout = [v for s in (da, dh) for k, v in s.items() if k in cles]
    vmin = int(min(tout) // 200_000) * 200_000  # échelle tirée des données, commune aux deux panneaux
    vmax = int(-(-max(tout) // 200_000)) * 200_000
    L = T[LANG]
    e = cadre(H, "mg", L["t2"], L["s2"], L["d2"] % max(dh)[:4])
    pw, gap, x0g = 300, 50, 56
    y0, y1 = 96, 300
    Y = lambda v: y1 - (v - vmin) / (vmax - vmin) * (y1 - y0)  # noqa: E731
    for k, (s, col, nom) in enumerate(((da, BLEU, L["p1"]), (dh, GRIS, L["p2"]))):
        x0 = x0g + k * (pw + gap)
        X = lambda i, x0=x0: x0 + i / (len(cles) - 1) * pw  # noqa: E731
        e.append(txt(x0, y0 - 26, nom, 11, col if col == BLEU else INK2, "start", "600"))
        for v in range(vmin, vmax + 1, 400_000):
            e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (x0, Y(v), x0 + pw, Y(v), GRID))
            if k == 0:
                e.append(txt(x0 - 6, Y(v) + 4, L["M"](v), 10, MUTED, "end"))
        for i, c in enumerate(cles):
            if c.endswith("T1") and int(c[:4]) % 2 == 0:
                e.append(txt(X(i), y1 + 15, c[:4], 10, MUTED, "middle"))
        i25 = cles.index("2025-T1") - 0.5
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (X(i25), y0 - 8, X(i25), y1, INK2))
        pts = " ".join("%.1f,%.1f" % (X(i), Y(s[c])) for i, c in enumerate(cles))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"%s/>'
                 % (pts, col, "" if col == BLEU else ' stroke-dasharray="5 3"'))
        e.append(txt(X(i25) - 4, y0 - 10, L["rupture"], 9, INK2, "end"))
    e.append(txt(0, y1 + 36, L["ecart"], 10, INK2))
    e += cartouche(H, L["src2"], L["note2"])
    e.append("</svg>")
    return "\n".join(e)


MONTRE_EN = {
    "recoupement": "In 2024, according to the Insee estimate, about {commun} people are both unemployed in the ILO sense and "
                   "registered in category A; about {a_seul} category A registrants are not ILO-unemployed, and {bit_seul} "
                   "ILO-unemployed are not registered in category A.",
    "regle": "Since 1 January 2025, some groups are registered automatically with France Travail; the Dares also publishes a "
             "series that excludes RSA recipients and young people in programmes. The two panels describe two populations, and "
             "the gap between them does not measure the effect of the reform.",
}


def fiches(figs: dict, A: dict, A_en: dict) -> dict:
    montre = {
        "recoupement": ("mesurer-recoupement", "En 2024, selon l'estimation de l'Insee, environ %s de personnes sont à la fois chômeurs au sens "
                        "du BIT et inscrites en catégorie A ; environ %s inscrits en catégorie A ne sont pas chômeurs au sens du BIT, "
                        "et %s chômeurs au sens du BIT ne sont pas inscrits en catégorie A." % (A["commun"], A["a_seul"], A["bit_seul"])),
        "regle": ("mesurer-regle", "Depuis le 1er janvier 2025, des publics sont inscrits d'office à France Travail ; la Dares publie "
                  "aussi une série qui exclut les bénéficiaires du RSA et les jeunes en parcours. Les deux panneaux décrivent deux "
                  "populations, et leur écart ne mesure pas l'effet de la réforme."),
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
    w.writerow(["serie", "periode", "statut_bit", "categorie_inscription", "valeur", "unite", "champ", "source"])
    for s in STATUTS + ["Ensemble"]:
        for c in CATS + ["Ensemble"]:
            w.writerow(["croisement_bit_inscription", "2024", s, c, r["eff"][s][c], "milliers de personnes",
                        CHAMP_ATTENDU, "Insee Références ECRT 2026, dossier 1, figure 2 (estimation)"])
    for k, v in r["dares_a"].items():
        w.writerow(["inscrits_categorie_A", k, "", "A", v, "personnes", "France hors Mayotte, CVS-CJO", "Dares-France Travail"])
    for k, v in r["dares_a_hors"].items():
        w.writerow(["inscrits_categorie_A_hors_RSA_et_jeunes_en_parcours", k, "", "A hors RSA et jeunes en parcours", v,
                    "personnes", "France hors Mayotte, CVS-CJO", "Dares-France Travail"])
    return buf.getvalue()


def autotest(I: dict, D: dict) -> list[str]:
    out = []
    for nom, mut, pref in (
            ("commun altere", lambda m: m["eff"]["Chômeur"].__setitem__("Catégorie A", m["eff"]["Chômeur"]["Catégorie A"] + 10), "M"),
            ("parts permutees", lambda m: (m["parts_cat"]["Chômeur"].__setitem__("Catégorie A", 62),
                                           m["parts_stat"]["Chômeur"].__setitem__("Catégorie A", 49)), "M5"),
            ("champ altere", lambda m: m.__setitem__("champ", m["champ"].replace("15 à 64", "15 ans ou plus, 15 à 74")), "M1")):
        m = copy.deepcopy(I)
        mut(m)
        try:
            calculer(m, D)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith(pref):
                raise
            out.append("%s -> %s" % (nom, str(e)[:55]))
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
    bx, ox = charger(URL_XLSX, "ECRT2026-D1.xlsx")
    bd, od = charger(URL_DARES, "dares_defm_stock_france_cvs_trim.csv")
    bm, om = charger(URL_DARES_META, "dares_defm_stock_france_cvs_trim_meta.json")
    maj_dares = json.loads(bm.decode("utf-8"))["metas"]["default"]["modified"][:10]
    I, D = lire_insee(bx), lire_dares(bd)
    r, g = calculer(I, D)
    for m in autotest(I, D):
        log("autotest : la mutation a mordu : " + m)
    A, A_en = affichage(r), affichage_en(r)
    if set(A) != set(A_en):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A) ^ set(A_en)))
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    try:
        import cairosvg
    except ImportError:
        raise Arret("cairosvg absent : SVG et PNG ensemble ou pas du tout")
    global LANG
    figs = {}
    for LANG, suf, AA in (("fr", "", A), ("en", "-en", A_en)):
        figs["mesurer-recoupement%s.svg" % suf] = fig_recoupement(r, AA)
        figs["mesurer-regle%s.svg" % suf] = fig_regle(r, AA)
    LANG = "fr"
    fi = fiches(figs, A, A_en)
    csvt = csv_texte(r)
    sha = {"insee_xlsx": hashlib.sha256(bx).hexdigest(), "dares_csv": hashlib.sha256(bd).hexdigest()}
    # Date de relevé = mise à jour publiée par la Dares (métadonnées) : elle ne change que si la source change.
    releve = maj_dares
    payload = {
        "releve_le": releve,
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Insee (Insee Références 2026), Dares-France Travail",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Mesurer, E1 et E2",
                 "sources": {"insee": {"url": URL_XLSX, "sha256": sha["insee_xlsx"]},
                             "dares": {"url": URL_DARES, "sha256": sha["dares_csv"], "metadonnees": URL_DARES_META}},
                 "definitions": {
                     "chomeur_bit": "« une personne âgée de 15 ans ou plus sans emploi, disponible pour en occuper un dans les quinze "
                                    "jours et qui a activement cherché un emploi dans le mois précédent (ou en a trouvé un qui "
                                    "commence dans moins de trois mois) » (Insee, ECRT 2026, dossier 1)",
                     "categorie_a": "« les personnes sans activité au cours du mois et tenues de rechercher un emploi » (Insee, ibid.)",
                     "estimation": "appariement du Fichier historique statistique de France Travail et de l'enquête Emploi de l'Insee"}},
        "gardes": g,
        "calcul": {k: v for k, v in r.items() if k not in ("dares_a", "dares_a_hors")},
        "series": {"inscrits_A": r["dares_a"], "inscrits_A_hors_RSA_et_jeunes_en_parcours": r["dares_a_hors"]},
        "affichage": dict(A, releve_le="%s (séries Dares mises à jour à cette date, jusqu'au %s ; Insee, édition du 02/07/2026)"
                          % ("/".join(reversed(releve.split("-"))), A["dares_fin"])),
        "affichage_en": dict(A_en, releve_le="%s (Dares series updated on that date, up to the %s; Insee, edition of 2 July 2026)"
                             % (releve, A_en["dares_fin"])),
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
    log("Sources : Insee %s ; Dares %s" % (ox, od))
    log("Ecrit : data/promesses_mesurer.json, static/promesses_mesurer.{json,csv}, data/figures_mesurer.json, 4 figures SVG + PNG (FR, EN)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
