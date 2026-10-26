#!/usr/bin/env python3
"""update_menages_imprevu.py -- page « Qui peut faire face à une dépense imprévue ? » (26/10/2026).

Origine : contre-expertise PRO-20261026-033434 (graphe G1, page de faits distincte), comité de lecteurs du même jour
(témoin à une seule variable), fiche docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md.

Découverte : au-dessus du seuil de pauvreté, être le seul adulte d'un foyer avec enfants va de pair avec une part bien
plus forte de personnes incapables de faire face à une dépense imprévue ; à présence d'enfants constante, le passage de
deux adultes à un seul pèse deux à trois fois plus qu'en l'absence d'enfants. Association, non cause.

Entrée : Eurostat, enquête SILC, jeu ilc_mdes04 (« Incapacité à faire face à des dépenses financières imprévues »), en %
des personnes, par composition du ménage (hhcomp) et position par rapport au seuil de 60 % du revenu médian équivalent
(rskpovth), France et UE à 27, relevé par l'API de diffusion (JSON-stat 2.0). Rien n'est saisi à la main.
Chaque qualificatif de la prose est une garde (fonction gardes) ; si la donnée la dément, arrêt, rien n'est écrit.
Témoin : l'UE à 27 (même indicateur, autre population) et la variante « couple avec deux enfants » ; le calcul ne
partage avec eux que la définition de l'indicateur.

Usage : python scripts/update_menages_imprevu.py [--check] [--mutation=total|dessus|dessous|ratio|ecarts|chaque|serre|ue|deux|majorite|rupture|annee]
Sorties : data/ et static/menages_imprevu.json, static/menages_imprevu.csv, data/figures_imprevu.json,
          static/img/imprevu-menages{,-en}{,-m}.svg + .png
"""
from __future__ import annotations

import csv
import html
import io
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure  # noqa: E402  -- pied commun, version téléphone, parité
import langue_generee as lg  # noqa: E402  -- nombres et « points » à la précision affichée
import releve_jeu as rj  # noqa: E402  -- relevé daté par les seules données

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "menages_imprevu.json"
OUT_STATIC = ROOT / "static" / "menages_imprevu.json"
OUT_CSV = ROOT / "static" / "menages_imprevu.csv"
OUT_FIGURES = ROOT / "data" / "figures_imprevu.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_FR = "stephane-lalut.com/qui-peut-faire-face-a-une-depense-imprevue/"
PAGE_EN = "stephane-lalut.com/en/who-can-cope-with-an-unexpected-expense/"
JEU = "ilc_mdes04"
API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/" + JEU
GEOS = ("FR", "EU27_2020")
MENAGES = ("TOTAL", "A2", "A1", "A2_DCH1", "A2_DCH2", "A1_DCH")
SEUILS = ("TOTAL", "A_60", "B_60")
DEBUT = 2015          # fenêtre des écarts publiés (série France complète depuis 2004 ; UE à 27 depuis 2010)

W = 720
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
ORANGE, GRIS, GRIS_CLAIR = "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"
SUFFIXE = {"fr": "", "en": "-en"}
LICENCES = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · " + PAGE_FR, "en": "Computed by Stéphane Lalut, CC BY 4.0 · " + PAGE_EN}
LICENCES_M = {"fr": "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com", "en": "Computed by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


# ------------------------------------------------------------------ relevé
def relever() -> tuple[dict, dict]:
    """Série {geo: {seuil: {menage: {annee: valeur}}}} et statuts {(geo, seuil, menage, annee): drapeau}."""
    q = "&".join(["format=JSON", "lang=fr", "unit=PC"] + ["geo=" + g for g in GEOS] + ["hhcomp=" + h for h in MENAGES]
                 + ["rskpovth=" + r for r in SEUILS])
    try:
        with urllib.request.urlopen(API + "?" + q, timeout=60) as r:
            d = json.loads(r.read().decode("utf-8"))
    except Exception as exc:  # réseau, HTTP, JSON : jamais une série vide prise pour une donnée
        fail("releve Eurostat %s impossible : %s" % (JEU, exc))
    ids, size = d["id"], d["size"]
    dims = {k: sorted(d["dimension"][k]["category"]["index"], key=d["dimension"][k]["category"]["index"].get) for k in ids}
    for k, attendu in (("geo", GEOS), ("hhcomp", MENAGES), ("rskpovth", SEUILS)):
        if set(dims[k]) != set(attendu):
            fail("dimension %s : %s au lieu de %s" % (k, dims[k], attendu))
    val, st = d.get("value", {}), d.get("status", {})
    serie, statuts = {}, {}
    for g in GEOS:
        for r_ in SEUILS:
            for h in MENAGES:
                for t in dims["time"]:
                    kw = dict(freq="A", unit="PC", geo=g, hhcomp=h, rskpovth=r_, time=t)
                    pos = 0
                    for k, s in zip(ids, size):
                        pos = pos * s + dims[k].index(kw[k])
                    v = val.get(str(pos))
                    if v is None:
                        continue      # absent : jamais un zéro
                    serie.setdefault(g, {}).setdefault(r_, {}).setdefault(h, {})[int(t)] = float(v)
                    if str(pos) in st:
                        statuts[(g, r_, h, int(t))] = st[str(pos)]
    return serie, statuts


def plausibilite(s: dict) -> int:
    """Bandes : pourcentages entre 0 et 100 ; dernière année commune récente ; série France complète sur la fenêtre."""
    for g in GEOS:
        for r_ in SEUILS:
            for h in MENAGES:
                for a, v in s.get(g, {}).get(r_, {}).get(h, {}).items():
                    if not 0 <= v <= 100:
                        fail("valeur hors bande : %s %s %s %d = %s" % (g, r_, h, a, v))
    y = min(max(s[g][r_][h]) for g in GEOS for r_ in SEUILS for h in MENAGES)
    if y < 2024:
        fail("derniere annee commune %d : serie trop ancienne ou incomplete" % y)
    for g in GEOS:
        for a in range(DEBUT, y + 1):
            for r_ in ("A_60", "B_60"):
                for h in MENAGES:
                    if a not in s[g][r_][h]:
                        fail("%s %s %s : annee %d manquante dans la fenetre" % (g, r_, h, a))
    return y


# ------------------------------------------------------------------ calcul
def calcul(s: dict, y: int) -> dict:
    def v(g, r_, h, a=y):
        return s[g][r_][h][a]
    ans = range(DEBUT, y + 1)
    c = {"y": y, "s": s}
    for g, p in (("FR", ""), ("EU27_2020", "ue_")):
        c[p + "total"] = v(g, "TOTAL", "TOTAL")
        c[p + "dessus"] = v(g, "A_60", "TOTAL")
        c[p + "dessous"] = v(g, "B_60", "TOTAL")
        for r_, cote in (("A_60", "dessus"), ("B_60", "dessous")):
            for h, nom in (("A1_DCH", "ps"), ("A2_DCH1", "c1"), ("A2_DCH2", "c2"), ("A1", "seul"), ("A2", "c0")):
                c["%s%s_%s" % (p, nom, cote)] = v(g, r_, h)
        # écarts à une seule variable (un adulte de moins), chaque année de la fenêtre
        c[p + "g_enf"] = {a: v(g, "A_60", "A1_DCH", a) - v(g, "A_60", "A2_DCH1", a) for a in ans}
        c[p + "g_sans"] = {a: v(g, "A_60", "A1", a) - v(g, "A_60", "A2", a) for a in ans}
        c[p + "g_enf2"] = {a: v(g, "A_60", "A1_DCH", a) - v(g, "A_60", "A2_DCH2", a) for a in ans}
        c[p + "g_enf_dessous"] = {a: v(g, "B_60", "A1_DCH", a) - v(g, "B_60", "A2_DCH1", a) for a in ans}
    return c


def mutation(c: dict):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m == "total":        # « près de trois personnes sur dix » deviendrait faux
        c["total"] = 34.0
    elif m == "dessus":     # « environ une sur cinq » au-dessus du seuil
        c["dessus"] = 30.0
    elif m == "dessous":    # « environ deux tiers » sous le seuil
        c["dessous"] = 50.0
    elif m == "ratio":      # « plus de deux fois » (parent seul contre couple avec un enfant)
        c["ps_dessus"] = 1.8 * c["c1_dessus"]
    elif m == "ecarts":     # « deux à trois fois l'écart observé sans enfants »
        c["g_sans"][c["y"]] = c["g_enf"][c["y"]] / 1.2
    elif m == "chaque":     # « chaque année depuis 2015 »
        c["g_sans"][DEBUT] = c["g_enf"][DEBUT] + 1
    elif m == "serre":      # « sous le seuil, l'écart se resserre »
        c["g_enf_dessous"][c["y"]] = c["g_enf"][c["y"]] + 1
    elif m == "ue":         # « même constat dans l'Union européenne »
        c["ue_g_sans"][DEBUT + 3] = c["ue_g_enf"][DEBUT + 3]
    elif m == "deux":       # « avec deux enfants aussi »
        c["g_enf2"][c["y"]] = 4.0
    elif m == "majorite":   # « en grande majorité exposés » sous le seuil
        c["c1_dessous"] = 55.0
    elif m == "rupture":    # plus aucune rupture : la phrase des limites deviendrait fausse
        c["ruptures_fr"] = []
    elif m == "annee":      # traitée avant le calcul (main) : la série relevée est tronquée après 2019
        pass
    elif m is not None:
        fail("mutation inconnue : %s" % m)
    return m


# ------------------------------------------------------------------ gardes : chaque qualificatif de la prose
def gardes(c: dict) -> int:
    n = 0

    def g(cond, msg):
        nonlocal n
        n += 1
        if not cond:
            fail("garde : " + msg)

    y, ans = c["y"], range(DEBUT, c["y"] + 1)
    g(26 <= c["total"] < 30, "« près de trois personnes sur dix » : %.1f" % c["total"])
    g(19 <= c["dessus"] < 24, "« environ une sur cinq au-dessus du seuil » : %.1f" % c["dessus"])
    g(62 <= c["dessous"] <= 71, "« environ deux tiers sous le seuil » : %.1f" % c["dessous"])
    g(c["ps_dessus"] > 2 * c["c1_dessus"], "« plus de deux fois » (parent seul / couple avec un enfant, au-dessus) : %.1f / %.1f"
      % (c["ps_dessus"], c["c1_dessus"]))
    r_ = c["g_enf"][y] / c["g_sans"][y]
    g(2 <= r_ <= 3.5, "« deux à trois fois l'écart observé sans enfants » : %.2f" % r_)
    g(all(c["g_enf"][a] > c["g_sans"][a] + 5 for a in ans),
      "« chaque année depuis %d, l'écart avec enfants dépasse nettement celui sans enfants » : %s"
      % (DEBUT, {a: round(c["g_enf"][a] - c["g_sans"][a], 1) for a in ans}))
    g(all(c["g_enf_dessous"][a] < c["g_enf"][a] for a in ans),
      "« sous le seuil, l'écart se resserre » : %s" % {a: (round(c["g_enf_dessous"][a], 1), round(c["g_enf"][a], 1)) for a in ans})
    g(all(c["ue_g_enf"][a] >= 1.5 * c["ue_g_sans"][a] for a in ans),
      "« même constat dans l'Union européenne » : %s" % {a: (round(c["ue_g_enf"][a], 1), round(c["ue_g_sans"][a], 1)) for a in ans})
    g(all(c["g_enf2"][a] > 15 for a in ans), "« avec deux enfants aussi » (écart > 15 points chaque année) : %s"
      % {a: round(c["g_enf2"][a], 1) for a in ans})
    g(c["ps_dessous"] > 66 and c["c1_dessous"] > 66,
      "« sous le seuil, parents seuls comme couples avec un enfant y sont en grande majorité exposés » : %.1f / %.1f" % (c["ps_dessous"], c["c1_dessous"]))
    g(len(c["ruptures_fr"]) >= 1, "la page cite des ruptures de série en France dans la fenêtre : aucune lue (%s)" % c["ruptures_fr"])
    g(c["ue_ps_dessus"] > 2 * c["ue_c1_dessus"] - 5,
      "UE : parent seul au-dessus du seuil « environ deux fois » le couple avec un enfant : %.1f / %.1f" % (c["ue_ps_dessus"], c["ue_c1_dessus"]))
    return n


# ------------------------------------------------------------------ affichage (mêmes clés, deux langues)
def affichage(c: dict, lang: str) -> dict:
    f = lambda v, d=1: lg.nombre(v, d, lang)  # noqa: E731
    pts = lambda v, d=1: lg.points(v, d, lang)  # noqa: E731
    y, ans = c["y"], range(DEBUT, c["y"] + 1)
    A = {"annee": str(y), "debut": str(DEBUT),
         "total": f(c["total"]), "dessus": f(c["dessus"]), "dessous": f(c["dessous"]),
         "ratio": f(c["ps_dessus"] / c["c1_dessus"]),
         "ecart_enf": pts(c["g_enf"][y]), "ecart_sans": pts(c["g_sans"][y]), "ecart_enf2": pts(c["g_enf2"][y]),
         "ecart_enf_dessous": pts(c["g_enf_dessous"][y]),
         "plage_enf_bas": f(min(c["g_enf"][a] for a in ans), 0), "plage_enf_haut": f(max(c["g_enf"][a] for a in ans), 0),
         "plage_sans_bas": f(min(c["g_sans"][a] for a in ans), 0), "plage_sans_haut": f(max(c["g_sans"][a] for a in ans), 0),
         "plage_dessous_bas": f(min(c["g_enf_dessous"][a] for a in ans), 0), "plage_dessous_haut": f(max(c["g_enf_dessous"][a] for a in ans), 0),
         "ue_total": f(c["ue_total"]), "ue_ecart_enf": pts(c["ue_g_enf"][y]), "ue_ecart_sans": pts(c["ue_g_sans"][y]),
         "ue_plage_enf_bas": f(min(c["ue_g_enf"][a] for a in ans), 0), "ue_plage_enf_haut": f(max(c["ue_g_enf"][a] for a in ans), 0),
         "ruptures_fr": lg.enumere([str(a) for a in c["ruptures_fr"]], lang),
         "ue_plage_sans_bas": f(min(c["ue_g_sans"][a] for a in ans), 0), "ue_plage_sans_haut": f(max(c["ue_g_sans"][a] for a in ans), 0)}
    for p in ("", "ue_"):
        for nom in ("ps", "c1", "c2", "seul", "c0"):
            for cote in ("dessus", "dessous"):
                A["%s%s_%s" % (p, nom, cote)] = f(c["%s%s_%s" % (p, nom, cote)])
    return A


# ------------------------------------------------------------------ figure signature
TXT = {
    "fr": dict(
        titre="Ne pas pouvoir faire face à une dépense imprévue : le revenu ne dit pas tout (France, {annee})",
        titre_m="Faire face à une dépense imprévue : le revenu ne dit pas tout (France, {annee})",
        desc="Part des personnes qui ne pourraient pas faire face à une dépense imprévue, France, {annee}. Au-dessus du seuil de "
             "pauvreté : couple sans enfant {c0_dessus} %, adulte seul {seul_dessus} %, couple avec un enfant {c1_dessus} %, parent seul "
             "{ps_dessus} %. En dessous du seuil : couple sans enfant {c0_dessous} %, adulte seul {seul_dessous} %, couple avec un enfant "
             "{c1_dessous} %, parent seul {ps_dessous} %.",
        dessus="Au-dessus du seuil de pauvreté", dessous="En dessous du seuil de pauvreté",
        menages=("Couple sans enfant", "Adulte seul", "Couple avec un enfant", "Parent seul"),
        ecart="+{ecart_enf}",
        source="Eurostat, enquête SILC (ilc_mdes04), en % des personnes",
        note="Déclaratif ; seuil de pauvreté : 60 % du revenu médian par unité de consommation ; montant de la dépense fixé par "
             "l'enquête. Association, non cause : la position dans la tranche de revenu n'est pas contrôlée.",
        montre="Au-dessus du seuil de pauvreté, {ps_dessus} % des parents seuls ne pourraient pas faire face à une dépense imprévue, "
               "contre {c1_dessus} % des couples avec un enfant : le revenu relatif ne dit pas tout de la capacité d'encaisser un choc."),
    "en": dict(
        titre="Unable to face an unexpected expense: income is not the whole story (France, {annee})",
        titre_m="Facing an unexpected expense: income is not the whole story (France, {annee})",
        desc="Share of people who could not face an unexpected expense, France, {annee}. Above the poverty threshold: couple without "
             "children {c0_dessus}%, single adult {seul_dessus}%, couple with one child {c1_dessus}%, single parent {ps_dessus}%. Below "
             "the threshold: couple without children {c0_dessous}%, single adult {seul_dessous}%, couple with one child {c1_dessous}%, "
             "single parent {ps_dessous}%.",
        dessus="Above the poverty threshold", dessous="Below the poverty threshold",
        menages=("Couple, no children", "Single adult", "Couple, one child", "Single parent"),
        ecart="+{ecart_enf}",
        source="Eurostat, EU-SILC (ilc_mdes04), % of people",
        note="Self-reported; poverty threshold: 60% of median equivalised income; expense amount set by the survey. "
             "Association, not cause: position within the income band is not controlled.",
        montre="Above the poverty threshold, {ps_dessus}% of single parents could not face an unexpected expense, against "
               "{c1_dessus}% of couples with one child: relative income does not tell the whole story about coping with a shock."),
}
CLES = ("c0", "seul", "c1", "ps")
COUL = {"c0": GRIS_CLAIR, "seul": GRIS_CLAIR, "c1": GRIS, "ps": ORANGE}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def txt(lang: str, Aff: dict) -> dict:
    return {k: (v.format(**Aff) if isinstance(v, str) else v) for k, v in TXT[lang].items()}


def fig(c: dict, Aff: dict, lang: str) -> str:
    t = txt(lang, Aff)
    pct = "%" if lang == "en" else " %"
    h = 268
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="imp-t imp-d" font-family="%s">' % (W, h + 52, FONT),
         '<title id="imp-t">%s</title><desc id="imp-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52)]
    for k, l in enumerate(pied_figure.coupe(t["titre"], 96)):
        e.append('<text x="0" y="%d" font-size="14" font-weight="600" fill="%s">%s</text>' % (18 + 18 * k, INK, esc(l)))
    top = 70
    for p, (cote, x0) in enumerate((("dessus", 0), ("dessous", 372))):
        e.append('<text x="%d" y="%d" font-size="12" font-weight="600" fill="%s">%s</text>' % (x0, top, INK2, esc(t[cote])))
        lab, b0, b1 = x0, x0 + 132, x0 + 312
        X = lambda v: b0 + (b1 - b0) * v / 100  # noqa: E731
        for i, cle in enumerate(CLES):
            yy = top + 22 + 40 * i
            val = c["%s_%s" % (cle, cote)]
            e.append('<text x="%d" y="%d" font-size="11.5" fill="%s">%s</text>' % (lab, yy + 13, INK, esc(t["menages"][i])))
            e.append('<rect x="%d" y="%d" width="%.1f" height="18" fill="%s"/>' % (b0, yy, X(val) - b0, COUL[cle]))
            poids = ' font-weight="600"' if cle in ("ps", "c1") else ""
            e.append('<text x="%.1f" y="%d" font-size="11.5"%s fill="%s">%s%s</text>'
                     % (X(val) + 5, yy + 13, poids, ORANGE if cle == "ps" else INK, Aff["%s_%s" % (cle, cote)], pct))
        e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>' % (b0, top + 14, b0, top + 22 + 40 * 4 - 4, GRID))
        if cote == "dessus":   # accolade de l'écart à une seule variable : couple avec un enfant -> parent seul
            ya, yb = top + 22 + 40 * 2 + 9, top + 22 + 40 * 3 + 9
            xa = X(max(c["ps_dessus"], c["c1_dessus"])) + 46
            e.append('<path d="M%.1f,%d h6 v%d h-6" fill="none" stroke="%s" stroke-width="1.4"/>' % (xa, ya, yb - ya, ORANGE))
            e.append('<text x="%.1f" y="%d" font-size="11.5" font-weight="600" fill="%s">%s</text>'
                     % (xa + 10, (ya + yb) // 2 + 4, ORANGE, esc(t["ecart"])))
    return pied_figure.pied(e, h + 2, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


def desc_de(svg: str) -> str:
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_m(c: dict, Aff: dict, lang: str, svg_d: str) -> str:
    t = txt(lang, Aff)
    pct = "%" if lang == "en" else " %"
    e, y = pied_figure.tete_mobile("impm", t["titre_m"], desc_de(svg_d), INK, FONT)
    y += 16
    for cote in ("dessus", "dessous"):
        y += 8
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK2, esc(t[cote])))
        b0, b1 = 0, 228
        X = lambda v: b0 + (b1 - b0) * v / 100  # noqa: E731
        for i, cle in enumerate(CLES):
            y += 22
            val = c["%s_%s" % (cle, cote)]
            e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK, esc(t["menages"][i])))
            y += 6
            e.append('<rect x="0" y="%d" width="%.1f" height="14" fill="%s"/>' % (y, X(val), COUL[cle]))
            e.append('<text x="%.1f" y="%d" font-size="%s" font-weight="600" fill="%s">%s%s</text>'
                     % (X(val) + 5, y + 12, FS_MIN, ORANGE if cle == "ps" else INK, Aff["%s_%s" % (cle, cote)], pct))
            y += 14
        y += 30
    return pied_figure.pied_mobile(e, y + 4, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                              (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fiches(figs: dict, Aff: dict) -> dict:
    out = {}
    for lang in ("fr", "en"):
        f = "imprevu-menages" + SUFFIXE[lang]
        svg = figs[f + ".svg"]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        out[lang] = [dict(id="menages", fichier=f, titre=titre, montre=TXT[lang]["montre"].format(**Aff[lang]),
                          source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note"))]
    return out


def csv_texte(s: dict, statuts: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["geo", "annee", "seuil_pauvrete", "menage", "valeur_pct_personnes", "statut_eurostat"])
    for g in GEOS:
        for r_ in SEUILS:
            for h in MENAGES:
                for a, v in sorted(s[g][r_][h].items()):
                    w.writerow([g, a, r_, h, "%.1f" % v, statuts.get((g, r_, h, a), "")])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    s, statuts = relever()
    if "--mutation=annee" in sys.argv[1:]:   # témoin de la bande de plausibilité : une série arrêtée en 2019
        for g in s.values():
            for r_ in g.values():
                for h in r_.values():
                    for a in [a for a in h if a > 2019]:
                        del h[a]
    y = plausibilite(s)
    c = calcul(s, y)
    # ruptures de série (drapeau « b ») en France dans la fenêtre : la page les cite, lues ici, jamais saisies
    c["ruptures_fr"] = sorted({a for (g, _r, _h, a), f in statuts.items() if g == "FR" and "b" in f and DEBUT <= a <= y})
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, lang) for lang in ("fr", "en")}
    if set(Aff["fr"]) != set(Aff["en"]):
        fail("blocs affichage et affichage_en : cles differentes")
    log("France %d : %.1f %% ; au-dessus %.1f, en dessous %.1f ; parent seul %.1f contre couple 1 enfant %.1f (au-dessus)"
        % (y, c["total"], c["dessus"], c["dessous"], c["ps_dessus"], c["c1_dessus"]))
    figs = {}
    for lang in ("fr", "en"):
        sf = SUFFIXE[lang]
        figs["imprevu-menages%s.svg" % sf] = fig(c, Aff[lang], lang)
        figs["imprevu-menages%s-m.svg" % sf] = fig_m(c, Aff[lang], lang, figs["imprevu-menages%s.svg" % sf])
        ec = pied_figure.parite(figs["imprevu-menages%s.svg" % sf], figs["imprevu-menages%s-m.svg" % sf], FS_MIN, (ORANGE,))
        if ec:
            fail("parite mobile %s : %s" % (lang, " ; ".join(ec)))
    pages = ROOT / "content" / "qui-peut-faire-face-a-une-depense-imprevue"
    for page, sf in (("_index.md", ""), ("_index.en.md", "-en")):
        if (pages / page).exists():
            ec = pied_figure.controler_page((pages / page).read_text(encoding="utf-8"),
                                            {f: v for f, v in figs.items() if re.fullmatch(r"imprevu-menages%s(-m)?\.svg" % sf, f)})
            if ec:
                fail("page %s : %s" % (page, " ; ".join(ec)))
    if check:
        log("--check : %d gardes passees (%d cles d'affichage), parite des figures telephone controlee, rien ecrit." % (n, len(Aff["fr"])))
        for f_, v in figs.items():
            log("  %s : viewBox %s" % (f_, re.search(r'viewBox="([^"]+)"', v).group(1)))
        return 0
    import cairosvg
    payload = {"meta": {"page": "https://" + PAGE_FR, "licence": "CC BY 4.0",
                        "source": "Eurostat, enquête EU-SILC, jeu %s (incapacité à faire face à des dépenses financières imprévues)" % JEU,
                        "unite": "% des personnes", "url_source": "https://ec.europa.eu/eurostat/databrowser/view/%s/default/table" % JEU,
                        "seuil": "A_60 : au-dessus de 60 % du revenu médian équivalent ; B_60 : en dessous",
                        "menages": {"TOTAL": "ensemble", "A2": "deux adultes sans enfant dépendant", "A1": "un adulte sans enfant dépendant",
                                    "A2_DCH1": "deux adultes avec un enfant dépendant", "A2_DCH2": "deux adultes avec deux enfants dépendants",
                                    "A1_DCH": "un adulte avec enfants dépendants"},
                        "derniere_annee": y},
               "serie": {g: {r_: {h: {str(a): v for a, v in sorted(s[g][r_][h].items())} for h in MENAGES} for r_ in SEUILS} for g in GEOS},
               "affichage": Aff["fr"], "affichage_en": Aff["en"]}
    releve = None
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            same = {k: v for k, v in prev.items() if k not in ("releve_le", "_licence")} == json.loads(json.dumps(payload, ensure_ascii=False))
            if same and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == v for f, v in figs.items()) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(s, statuts) \
                    and OUT_FIGURES.exists() \
                    and OUT_FIGURES.read_text(encoding="utf-8") == json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n":
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
            if same or rj.releve(OUT_DATA, payload, "") == prev["releve_le"]:
                releve = prev["releve_le"]
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; source Eurostat (EU-SILC)", **payload}
    txt_ = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt_, encoding="utf-8")
    OUT_STATIC.write_text(txt_, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(s, statuts), encoding="utf-8-sig", newline="\n")
    for f, v in figs.items():
        (OUT_IMG / f).write_text(v, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/menages_imprevu.json, static/menages_imprevu.csv, data/figures_imprevu.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
