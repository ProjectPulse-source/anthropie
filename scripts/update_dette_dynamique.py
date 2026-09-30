#!/usr/bin/env python3
"""update_dette_dynamique.py -- volet « Pourquoi la dette publique augmente-t-elle ? » (dossier dette, volet 1).

Arbitrage PRO-20260930-092814 (option E) : le volet n'existe que s'il porte une DÉCOMPOSITION robuste de la variation
du ratio dette/PIB. Identité (administrations publiques, France, Eurostat, monnaie nationale) :

    d_t - d_{t-1} = i_t/(1+g_t) * d_{t-1}      effet des intérêts            (i = intérêts_t / dette_{t-1}, taux implicite)
                  - g_t/(1+g_t) * d_{t-1}      effet de la croissance nominale (g = PIB_t / PIB_{t-1} - 1)
                  - pb_t                       solde primaire / PIB (excédent > 0 : il fait BAISSER le ratio)
                  + sfa_t                      ajustements flux-stock (résidu)

TÉMOIN INDÉPENDANT, bloquant : le résidu doit égaler (ΔDette_t + B9_t) / PIB_t, la dette qui bouge sans passer par le
déficit, calculée par une autre voie. Un écart signale une série incohérente : rien n'est écrit.

Les phrases que la page affirme sont recalculées ici (gardes de prose) : si une nouvelle donnée les dément, arrêt.
SVG et PNG sont produits ensemble ou pas du tout (cairosvg) ; les fiches « Réutiliser » sont lues dans le SVG.

Usage : python scripts/update_dette_dynamique.py [--check]
Sorties : data/ et static/dette_dynamique.json, static/dette_dynamique.csv, data/figures_dynamique.json,
          static/img/dette-dynamique-{cascade,annuelle}.svg + .png
"""
from __future__ import annotations

import csv
import html
import io
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dette_dynamique.json"
OUT_STATIC = ROOT / "static" / "dette_dynamique.json"
OUT_CSV = ROOT / "static" / "dette_dynamique.csv"
OUT_FIGURES = ROOT / "data" / "figures_dynamique.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/pourquoi-la-dette-publique-augmente/"
PERIODES = [(1996, 2007, "1996-2007"), (2008, 2019, "2008-2019"), (2020, None, "2020-%s")]

W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#26262f", "#55524f", "#96928f", "#dcd8d3"


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    sys.exit(1)


def fetch(url: str, essais: int = 3) -> bytes:
    for k in range(essais):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com (stephane@stephane-lalut.com)"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if k == essais - 1:
                fail("reseau : %s (%s)" % (url[:120], e))
            time.sleep(3 * (k + 1))
    return b""


def eurostat(ds: str, **f) -> dict[int, float]:
    q = "&".join("%s=%s" % (k, v) for k, v in f.items())
    d = json.loads(fetch("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/%s?format=JSON&geo=FR&%s" % (ds, q)))
    if "dimension" not in d:
        fail("Eurostat %s : reponse sans dimensions" % ds)
    tm = d["dimension"]["time"]["category"]["index"]
    strides, s = {}, 1
    for dim, n in zip(reversed(d["id"]), reversed(d["size"])):
        strides[dim] = s
        s *= n
    out = {}
    for t, i in tm.items():
        v = d["value"].get(str(i * strides["time"]))
        if v is not None:
            out[int(t)] = float(v)
    return out


def fr(v: float, dec: int = 1) -> str:
    s = ("%." + str(dec) + "f") % v
    return s.replace("-", "−").replace(".", ",")


def signe(v: float, dec: int = 1) -> str:
    return ("+" if v >= 0 else "") + fr(v, dec)


# ------------------------------------------------------------------ calcul
def decomposition():
    D = eurostat("gov_10dd_edpt1", na_item="GD", sector="S13", unit="MIO_NAC")
    Y = eurostat("nama_10_gdp", na_item="B1GQ", unit="CP_MEUR")
    I = eurostat("gov_10a_main", na_item="D41PAY", sector="S13", unit="MIO_NAC")
    B9 = eurostat("gov_10a_main", na_item="B9", sector="S13", unit="MIO_NAC")
    ans = sorted(a for a in D if a - 1 in D and a in Y and a - 1 in Y and a in I and a in B9)
    if len(ans) < 25:
        fail("series trop courtes (%d annees)" % len(ans))
    rows = []
    for a in ans:
        d0, d1 = D[a - 1] / Y[a - 1] * 100, D[a] / Y[a] * 100
        i, g = I[a] / D[a - 1], Y[a] / Y[a - 1] - 1
        interets, croissance = i / (1 + g) * d0, -g / (1 + g) * d0
        pb = (B9[a] + I[a]) / Y[a] * 100
        sfa = (d1 - d0) - (interets + croissance) + pb
        temoin = ((D[a] - D[a - 1]) + B9[a]) / Y[a] * 100
        if abs(sfa - temoin) > 1e-6:
            fail("%d : residu flux-stock %.4f != temoin comptable %.4f" % (a, sfa, temoin))
        rows.append(dict(annee=a, dette_pct_pib=d1, variation=d1 - d0, effet_interets=interets,
                         effet_croissance=croissance, effet_taux_croissance=interets + croissance,
                         contribution_solde_primaire=-pb, flux_stock=sfa, taux_implicite_pct=i * 100,
                         croissance_nominale_pct=g * 100, solde_primaire_pct_pib=pb))
    return ans[0] - 1, D[ans[0] - 1] / Y[ans[0] - 1] * 100, rows


def agreger(rows, a0, a1):
    s = [r for r in rows if a0 <= r["annee"] <= a1]
    return {k: sum(r[k] for r in s) for k in ("variation", "effet_interets", "effet_croissance", "effet_taux_croissance",
                                               "contribution_solde_primaire", "flux_stock")}


# ------------------------------------------------------------------ figures
def esc(s: str) -> str:
    return html.escape(s, quote=False)


def entete(h, ident, titre, desc):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h + 52, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
            '<text x="0" y="18" font-size="15" font-weight="600" fill="%s">%s</text>' % (INK, esc(titre))]


def cartouche(y0, source, note):
    out = ['<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID)]
    for k, (t, c) in enumerate([(source, INK2), (note, INK2), ("Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, MUTED)]):
        out.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, c, esc(t)))
    return out


def fig_cascade(a0, d_depart, rows, total):
    """Figure signature : de la dette de départ à la dette d'arrivée, en quatre marches."""
    an_fin = rows[-1]["annee"]
    etapes = [("Dette fin %d" % a0, d_depart, "stock"),
              ("Intérêts payés", total["effet_interets"], "delta"),
              ("Croissance du PIB nominal", total["effet_croissance"], "delta"),
              ("Déficits primaires", total["contribution_solde_primaire"], "delta"),
              ("Ajustements flux-stock", total["flux_stock"], "delta"),
              ("Dette fin %d" % an_fin, rows[-1]["dette_pct_pib"], "stock")]
    H, X0, X1, TOP, BAS = 330, 40, W - 10, 70, 290
    haut = max(d_depart + max(0, total["effet_interets"]), rows[-1]["dette_pct_pib"]) * 1.08
    vmax = (int(haut / 20) + 1) * 20

    def Y(v):
        return BAS - (BAS - TOP) * v / vmax

    titre = "Pourquoi la dette a doublé : de %s %% à %s %% du PIB, %d-%d" % (fr(d_depart), fr(rows[-1]["dette_pct_pib"]), a0, an_fin)
    desc = ("Cascade en points de PIB. La dette part de %s %% fin %d. Les intérêts l'auraient poussée de %s points, mais la "
            "croissance du PIB nominal en a effacé %s : leur effet net est de %s point. Les déficits primaires, hors intérêts, "
            "ajoutent %s points, les ajustements flux-stock %s. La dette atteint %s %% fin %d. Décomposition comptable, non causale."
            % (fr(d_depart), a0, fr(total["effet_interets"]), fr(-total["effet_croissance"]), signe(total["effet_taux_croissance"]),
               fr(total["contribution_solde_primaire"]), signe(total["flux_stock"]), fr(rows[-1]["dette_pct_pib"]), an_fin))
    e = entete(H, "dc", titre, desc)
    for g in range(0, vmax + 1, 20):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.2 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d %%</text>' % (X0 - 6, Y(g) + 3, MUTED, g))
    n = len(etapes)
    pas = (X1 - X0) / n
    bw = pas * 0.58
    niveau = 0.0
    for k, (lib, v, nature) in enumerate(etapes):
        cx = X0 + pas * (k + 0.5)
        if nature == "stock":
            bas_v, haut_v, col = 0.0, v, BLEU
            niveau = v
            etiq = "%s %%" % fr(v)
        else:
            bas_v, haut_v = (niveau, niveau + v) if v >= 0 else (niveau + v, niveau)
            col = ORANGE if v >= 0 else GRIS
            etiq = signe(v)
            e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="3 2"/>'
                     % (cx - pas + bw / 2, Y(niveau), cx - bw / 2, Y(niveau), MUTED))
            niveau += v
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (cx - bw / 2, Y(haut_v), bw, max(1.0, Y(bas_v) - Y(haut_v)), col))
        e.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="600" fill="%s" text-anchor="middle">%s</text>' % (cx, Y(haut_v) - 6, INK, esc(etiq)))
        mots = lib.split(" ")
        l1 = " ".join(mots[:2]) if len(mots) > 2 else lib
        l2 = " ".join(mots[2:]) if len(mots) > 2 else ""
        e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (cx, BAS + 16, INK2, esc(l1)))
        if l2:
            e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (cx, BAS + 29, INK2, esc(l2)))
    e.append('<text x="%d" y="44" font-size="11" fill="%s">En points de PIB : bleu, le stock ; orange, ce qui le fait monter ; gris, ce qui le fait baisser.</text>' % (X0, INK2))
    e += cartouche(H + 4, "Eurostat gov_10dd_edpt1 (dette), gov_10a_main (B9, D41PAY), nama_10_gdp (PIB), France, %d-%d" % (a0 + 1, an_fin),
                   "Décomposition comptable de la variation du ratio, non une attribution causale ; les termes se compensent en partie.")
    e.append("</svg>")
    return "\n".join(e)


def fig_annuelle(rows):
    """Chaque année : ce qui a poussé ou freiné le ratio, et la variation effective (point)."""
    a0, a1 = rows[0]["annee"], rows[-1]["annee"]
    H, X0, X1, TOP, BAS = 300, 40, W - 10, 70, 270
    hauts = [max(0, r["effet_taux_croissance"]) + max(0, r["contribution_solde_primaire"]) + max(0, r["flux_stock"]) for r in rows]
    bas_ = [min(0, r["effet_taux_croissance"]) + min(0, r["contribution_solde_primaire"]) + min(0, r["flux_stock"]) for r in rows]
    vmax, vmin = (int(max(hauts) / 4) + 1) * 4, -(int(-min(bas_) / 4) + 1) * 4

    def Y(v):
        return BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)

    titre = "Année par année : ce qui a fait monter ou baisser le ratio, %d-%d" % (a0, a1)
    desc = ("Barres empilées par année, en points de PIB : en orange la contribution des déficits primaires, en bleu l'effet "
            "net des taux et de la croissance, en gris les ajustements flux-stock ; le point noir est la variation effective du "
            "ratio. Les déficits primaires portent la hausse de 2008 à 2025 ; l'effet taux-croissance devient fortement "
            "négatif en 2021-2023, quand la croissance du PIB nominal, portée notamment par l'inflation, s'accélère.")
    e = entete(H, "da", titre, desc)
    for g in range(vmin, vmax + 1, 4):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(g) + 3, MUTED, signe(g, 0)))
    pas = (X1 - X0) / len(rows)
    bw = pas * 0.7
    for k, r in enumerate(rows):
        cx = X0 + pas * (k + 0.5)
        pos = neg = 0.0
        for cle, col in (("contribution_solde_primaire", ORANGE), ("effet_taux_croissance", BLEU), ("flux_stock", GRIS_CLAIR)):
            v = r[cle]
            if v >= 0:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (cx - bw / 2, Y(pos + v), bw, Y(pos) - Y(pos + v), col))
                pos += v
            else:
                e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (cx - bw / 2, Y(neg), bw, Y(neg + v) - Y(neg), col))
                neg += v
        e.append('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s" stroke="#ffffff" stroke-width="1"/>' % (cx, Y(r["variation"]), INK))
        if r["annee"] % 5 == 0 or k == len(rows) - 1:
            e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (cx, BAS + 14, INK2, r["annee"]))
    leg = [(ORANGE, "déficits primaires"), (BLEU, "effet taux-croissance"), (GRIS_CLAIR, "ajustements flux-stock")]
    x = X0
    for col, lib in leg:
        e.append('<rect x="%d" y="36" width="10" height="10" fill="%s"/>' % (x, col))
        e.append('<text x="%d" y="45" font-size="11" fill="%s">%s</text>' % (x + 14, INK2, esc(lib)))
        x += 14 + 7 * len(lib) + 18
    e.append('<circle cx="%d" cy="41" r="3.2" fill="%s"/>' % (x + 4, INK))
    e.append('<text x="%d" y="45" font-size="11" fill="%s">variation du ratio</text>' % (x + 12, INK2))
    e += cartouche(H + 4, "Eurostat gov_10dd_edpt1, gov_10a_main (B9, D41PAY), nama_10_gdp, France, %d-%d" % (a0, a1),
                   "Points de PIB par an ; la somme des trois barres égale la variation (point noir), au centième près.")
    e.append("</svg>")
    return "\n".join(e)


def fiches(figs, A):
    MONTRE = [("cascade", "dette-dynamique-cascade",
               "Sur la période, les intérêts et la croissance nominale se sont presque annulés ; la hausse de la dette "
               "tient pour l'essentiel aux déficits primaires, hors intérêts."),
              ("annuelle", "dette-dynamique-annuelle",
               "Année par année, ce qui a poussé ou freiné le ratio ; en 2021-2023, la croissance nominale l'a fait baisser "
               "malgré les déficits.")]
    out = []
    for ident, f, montre in MONTRE:
        svg = figs[f + ".svg"]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        out.append(dict(id=ident, fichier=f, titre=titre, montre=montre, source=cart[0], precaution=cart[1]))
    return {"fr": out}


def csv_texte(rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    cles = ["annee", "dette_pct_pib", "variation", "effet_interets", "effet_croissance", "effet_taux_croissance",
            "contribution_solde_primaire", "flux_stock", "taux_implicite_pct", "croissance_nominale_pct", "solde_primaire_pct_pib"]
    w.writerow(cles)
    for r in rows:
        w.writerow([r["annee"]] + ["%.3f" % r[k] for k in cles[1:]])
    return buf.getvalue()


# ------------------------------------------------------------------ affichage et gardes
def affichage(a0, d_depart, rows, total, per):
    last = rows[-1]
    A = {"annee_depart": str(a0), "annee_fin": str(last["annee"]), "dette_depart": fr(d_depart), "dette_fin": fr(last["dette_pct_pib"]),
         "hausse": fr(total["variation"]), "effet_interets": fr(total["effet_interets"]),
         "effet_croissance": fr(-total["effet_croissance"]), "effet_net": signe(total["effet_taux_croissance"]),
         "deficits_primaires": fr(total["contribution_solde_primaire"]), "flux_stock": signe(total["flux_stock"]),
         "part_deficits": fr(100 * total["contribution_solde_primaire"] / total["variation"], 0)}
    for (a, b, lib), t in zip(PERIODES, per):
        k = "p%d" % (PERIODES.index((a, b, lib)) + 1)
        A[k + "_lib"] = lib if b else lib % last["annee"]
        A[k + "_hausse"] = signe(t["variation"])
        A[k + "_taux_croissance"] = signe(t["effet_taux_croissance"])
        A[k + "_deficits"] = signe(t["contribution_solde_primaire"])
        A[k + "_flux"] = signe(t["flux_stock"])
    infl = [r for r in rows if 2021 <= r["annee"] <= 2023]
    A["effet_2021_2023"] = fr(-sum(r["effet_taux_croissance"] for r in infl))
    A["deficits_2021_2023"] = fr(sum(r["contribution_solde_primaire"] for r in infl))
    by = {r["annee"]: r for r in rows}
    for a in (2009, 2020):
        A["hausse_%d" % a] = fr(by[a]["variation"])
        A["deficits_%d" % a] = fr(by[a]["contribution_solde_primaire"])
        A["taux_croissance_%d" % a] = fr(by[a]["effet_taux_croissance"])
    A["net_dernier"] = signe(last["effet_taux_croissance"])
    A["taux_implicite_dernier"] = fr(last["taux_implicite_pct"], 2)
    A["croissance_derniere"] = fr(last["croissance_nominale_pct"])
    A["annees_excedent"] = str(sum(1 for r in rows if r["solde_primaire_pct_pib"] > 0))
    A["annees_total"] = str(len(rows))
    p1, p2, p3 = per
    affirmations = [
        ("titre de la figure : « la dette a doublé » (rapport 1,85 à 2,2)", 1.85 < last["dette_pct_pib"] / d_depart < 2.2),
        ("les déficits primaires portent plus des trois quarts de la hausse", total["contribution_solde_primaire"] > 0.75 * total["variation"]),
        ("intérêts et croissance se compensent presque (effet net < 5 points)", abs(total["effet_taux_croissance"]) < 5),
        ("l'effet des intérêts dépasse 50 points et celui de la croissance aussi", total["effet_interets"] > 50 and -total["effet_croissance"] > 50),
        ("1996-2007 : l'effet taux-croissance domine, le solde primaire ne pèse pas",
         p1["effet_taux_croissance"] > 0 and p1["effet_taux_croissance"] > abs(p1["contribution_solde_primaire"])),
        ("2008-2019 : les déficits primaires dominent", p2["contribution_solde_primaire"] > 2 * abs(p2["effet_taux_croissance"])),
        ("2020-fin : l'effet taux-croissance fait baisser le ratio, les déficits le font monter davantage",
         p3["effet_taux_croissance"] < -5 and p3["contribution_solde_primaire"] > -p3["effet_taux_croissance"]),
        ("2021-2023 : l'effet taux-croissance fait baisser le ratio de plus de 10 points", sum(r["effet_taux_croissance"] for r in infl) < -10),
        ("1996-2007 : solde primaire « proche de l'équilibre et parfois excédentaire »",
         abs(p1["contribution_solde_primaire"]) < 5 and any(r["solde_primaire_pct_pib"] > 0 for r in rows if 1996 <= r["annee"] <= 2007)),
        ("2009 et 2020 : le déficit primaire se creuse (> 2 points) et le PIB nominal recule",
         all(by[a]["contribution_solde_primaire"] > 2 and by[a]["croissance_nominale_pct"] < 0 for a in (2009, 2020))),
        ("2021-2023 : l'effet taux-croissance retire plus que les déficits n'ajoutent, et le ratio baisse chaque année",
         -sum(r["effet_taux_croissance"] for r in infl) > sum(r["contribution_solde_primaire"] for r in infl)
         and all(r["variation"] < 0 for r in infl)),
        ("depuis 2024, le ratio remonte (2024 et années suivantes en hausse)", all(r["variation"] > 0 for r in rows if r["annee"] >= 2024)),
        ("dernière année : taux implicite et croissance nominale presque égaux (effet net < 0,5 point)", abs(last["effet_taux_croissance"]) < 0.5),
        ("2009 et 2020 : les deux plus fortes hausses de la série",
         sorted(rows, key=lambda r: -r["variation"])[0]["annee"] in (2009, 2020) and sorted(rows, key=lambda r: -r["variation"])[1]["annee"] in (2009, 2020)),
    ]
    faux = [nom for nom, ok in affirmations if not ok]
    if faux:
        fail("la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    return A


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:]
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    a0, d_depart, rows = decomposition()
    total = agreger(rows, rows[0]["annee"], rows[-1]["annee"])
    per = [agreger(rows, a, b or rows[-1]["annee"]) for a, b, _ in PERIODES]
    aff = affichage(a0, d_depart, rows, total, per)
    log("Decomposition %d-%d : hausse %.1f = interets %.1f + croissance %.1f + deficits primaires %.1f + flux-stock %.1f"
        % (rows[0]["annee"], rows[-1]["annee"], total["variation"], total["effet_interets"], total["effet_croissance"],
           total["contribution_solde_primaire"], total["flux_stock"]))
    if check:
        log("--check : gardes passees (%d cles d'affichage), rien ecrit." % len(aff))
        return 0
    figs = {"dette-dynamique-cascade.svg": fig_cascade(a0, d_depart, rows, total),
            "dette-dynamique-annuelle.svg": fig_annuelle(rows)}
    payload = {"meta": {"releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "page": "https://" + PAGE_URL,
                        "licence": "CC BY 4.0", "pays": "France", "perimetre": "administrations publiques (S.13), SEC 2010",
                        "identite": "d_t - d_{t-1} = i/(1+g) d_{t-1} - g/(1+g) d_{t-1} - pb_t + sfa_t",
                        "definitions": {"effet_interets": "intérêts de l'année rapportés au PIB, via le taux implicite appliqué à la dette de départ",
                                        "effet_croissance": "érosion du ratio par la hausse du PIB nominal (croissance réelle et inflation)",
                                        "contribution_solde_primaire": "déficit hors intérêts, en points de PIB (négatif en cas d'excédent)",
                                        "flux_stock": "variation de dette qui ne passe pas par le déficit (trésorerie, actifs, valorisation) ; résidu, contrôlé par une seconde identité comptable (variation de dette moins déficit)"}},
               "depart": {"annee": a0, "dette_pct_pib": d_depart}, "annees": rows, "total": total,
               "periodes": [dict(periode=(lib if b else lib % rows[-1]["annee"]), **t) for (a, b, lib), t in zip(PERIODES, per)],
               "affichage": aff}
    releve = payload["meta"]["releve_le"]
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev); p2.pop("releve_le", None); p2.pop("_licence", None); p2["meta"] = dict(p2["meta"], releve_le=None)
            n2 = dict(payload); n2["meta"] = dict(n2["meta"], releve_le=None)
            if prev.get("releve_le") and json.dumps(p2, sort_keys=True, ensure_ascii=False) == json.dumps(n2, sort_keys=True, ensure_ascii=False) \
                    and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and all((OUT_IMG / f.replace(".svg", ".png")).exists() for f in figs) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(rows) \
                    and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches(figs, aff):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; source Eurostat", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(rows), encoding="utf-8-sig", newline="\n")  # BOM : Excel lit les accents
    import cairosvg
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs, aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dette_dynamique.json, static/dette_dynamique.csv, data/figures_dynamique.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
