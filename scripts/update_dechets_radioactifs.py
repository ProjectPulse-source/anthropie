#!/usr/bin/env python3
"""update_dechets_radioactifs.py -- page « Déchets radioactifs : le volume dit-il le problème ? » (26/10/2026).

Origine : contre-expertise PRO-20261026-033434 (graphe G3 reconçu : volume, activité et gestion, sans indice composite),
fiche docs/conception/dechets-radioactifs-volume-ou-radioactivite.md.

Découverte : les déchets de haute activité (HA) font quelques millièmes du volume des déchets radioactifs et plus de 95 %
de leur radioactivité ; avec la moyenne activité à vie longue (MA-VL), plus de 99 %. Elles font partie des trois
catégories à vie longue (avec FA-VL) qui n'ont pas encore de stockage définitif : elles attendent sur leurs sites de
production ; ce qui sépare les catégories avec et sans stockage est la durée de vie, non la radioactivité. Le volume, qui
remplit le débat, est porté par des catégories déjà stockées pour l'essentiel (FMA-VC, TFA).

Entrée : Andra, Inventaire national des matières et déchets radioactifs, fichiers « déchets déclarés à fin AAAA »
(data.gouv.fr, jeu « inventaire-national-des-matieres-et-dechets-radioactifs »), découverts par l'API de data.gouv et lus
par script : volumes en équivalent conditionné (m³) par catégorie, activité déclarée (Bq) les années où elle l'est (les
éditions de l'inventaire : l'activité n'est déclarée que tous les cinq ans pour une partie des sites), localisation dans
les centres de stockage de l'Andra (nom du site). Valeurs TRANSCRITES, déclarées comme telles : l'état de la filière de
chaque catégorie (Andra, Les Essentiels 2026, p. 11, et page « Classification des déchets radioactifs et filières de
gestion » de l'inventaire), table FILIERES ci-dessous.
Témoin (vérifié le 26/10/2026, consigné dans la fiche) : volumes par catégorie à fin 2024 et volumes stockés dans les
centres de l'Andra, publiés par l'Andra dans Les Essentiels 2026, retrouvés à l'arrondi près par ce calcul.
Chaque qualificatif de la prose est une garde ; si la donnée la dément, arrêt, rien n'est écrit.

Usage : python scripts/update_dechets_radioactifs.py [--check] [--force]
        [--mutation=vol|act|editions|ajuste|ha_mavl|ha_mavl_ed|masse|masse_a|faible|stocke|hors|periode]
Sorties : data/ et static/dechets_radioactifs.json, static/dechets_radioactifs.csv, data/figures_dechets.json,
          static/img/dechets-volume-activite{,-en}{,-m}.svg + .png
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pied_figure  # noqa: E402
import langue_generee as lg  # noqa: E402
import releve_jeu as rj  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dechets_radioactifs.json"
OUT_STATIC = ROOT / "static" / "dechets_radioactifs.json"
OUT_CSV = ROOT / "static" / "dechets_radioactifs.csv"
OUT_FIGURES = ROOT / "data" / "figures_dechets.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_FR = "stephane-lalut.com/dechets-radioactifs-volume-ou-radioactivite/"
PAGE_EN = "stephane-lalut.com/en/radioactive-waste-volume-or-radioactivity/"
API = "https://www.data.gouv.fr/api/1/datasets/inventaire-national-des-matieres-et-dechets-radioactifs/"
CATS = ("HA", "MA-VL", "FA-VL", "FMA-VC", "TFA")           # catégories des bilans de l'Andra (DSF : quelques centaines de m³)
HORS_BILAN = ("AUTRES", "SANS CATEGORIE")                   # gestion particulière (RTCU, stockages historiques)
CENTRES = ("CSA", "CSM", "CIRES")                           # centres de stockage de l'Andra, repérés dans le nom du site
STOCKABLES = ("FMA-VC", "TFA")                              # catégories qui ont un stockage en service
COUVERTURE_ACT = 0.9                                         # édition retenue si l'activité HA est déclarée sur 90 % du volume HA

# Valeurs transcrites (Andra, Les Essentiels 2026, p. 11 ; inventaire.andra.fr, classification et filières de gestion,
# lus le 26/10/2026). Revoir à chaque édition des Essentiels.
FILIERES = {
    "fr": {"HA": "stockage géologique profond en projet (Cigéo)", "MA-VL": "stockage géologique profond en projet (Cigéo)",
           "FA-VL": "stockage à l'étude", "FMA-VC": "stockage en surface en service (Aube, depuis 1992)",
           "TFA": "stockage en service (Cires, depuis 2003)"},
    "en": {"HA": "deep geological disposal planned (Cigéo)", "MA-VL": "deep geological disposal planned (Cigéo)",
           "FA-VL": "disposal under study", "FMA-VC": "near-surface disposal in operation (Aube, since 1992)",
           "TFA": "disposal in operation (Cires, since 2003)"},
}
# Valeur transcrite (Andra, Les Essentiels 2026, p. 11, lue le 26/10/2026) : résidus de traitement de conversion de l'uranium
# entreposés à Malvési, hors bilans (installation ECRIN 309 000 m³, bassins d'évaporation 372 000, bassins de décantation 9 590).
# La famille « RTCU » du fichier ouvert ne s'y rapproche pas (0,89 million de m³ à fin 2024) : la page cite les deux et
# n'interprète pas le total du fichier (contre-expertise PRO-20261026-045248, P8).
MALVESI_ESSENTIELS_M3 = 309000 + 372000 + 9590

NOMS = {"fr": {"HA": "Haute activité (HA)", "MA-VL": "Moyenne activité, vie longue (MA-VL)", "FA-VL": "Faible activité, vie longue (FA-VL)",
               "FMA-VC": "Faible et moyenne activité, vie courte (FMA-VC)", "TFA": "Très faible activité (TFA)"},
        "en": {"HA": "High-level (HA)", "MA-VL": "Intermediate-level, long-lived (MA-VL)", "FA-VL": "Low-level, long-lived (FA-VL)",
               "FMA-VC": "Low- and intermediate-level, short-lived (FMA-VC)", "TFA": "Very-low-level (TFA)"}}

W = 720
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, ORANGE, GRIS, GRIS_CLAIR = "#184f95", "#eb6834", "#8a8781", "#c9c5c0"
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


def num(s):
    s = (s or "").strip().replace(" ", "").replace(" ", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None   # « - », vide ou phrase réglementaire : activité NON déclarée, jamais un zéro


# ------------------------------------------------------------------ relevé
def catalogue() -> dict:
    try:
        with urllib.request.urlopen(API, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as exc:
        fail("catalogue data.gouv inaccessible : %s" % exc)


def lire_annee(url: str):
    try:
        with urllib.request.urlopen(url, timeout=120) as r:
            raw = r.read()
    except Exception as exc:
        fail("fichier %s inaccessible : %s" % (url, exc))
    for enc in ("utf-8-sig", "cp1252"):
        try:
            txt = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    sep = ";" if txt[:3000].count(";") > txt[:3000].count(",") else ","
    rows = list(csv.DictReader(io.StringIO(txt), delimiter=sep))
    k = list(rows[0])
    cle = lambda motif: next(x for x in k if motif in x.upper())  # noqa: E731
    kc, kv, ka, ks, kf = cle("CATEG"), cle("VOLUME"), cle("ACTIV"), cle("NOM DU SITE"), cle("FAMILLE")
    return rows, (kc, kv, ka, ks, kf), hashlib.sha256(raw).hexdigest()


def agreger(rows, cles) -> dict:
    kc, kv, ka, ks, kf = cles
    a = {"vol": {}, "act": {}, "vol_declare": {}, "stocke": {}, "hb_famille": {}, "lignes": len(rows)}
    for r in rows:
        c = (r[kc] or "").strip()
        c = "HORS_BILAN" if c in HORS_BILAN else c
        v = num(r[kv]) or 0.0
        act = num(r[ka])
        a["vol"][c] = a["vol"].get(c, 0.0) + v
        if c == "HORS_BILAN":
            f = (r[kf] or "").strip()
            a["hb_famille"][f] = a["hb_famille"].get(f, 0.0) + v
        if act is not None:
            a["act"][c] = a["act"].get(c, 0.0) + act
            a["vol_declare"][c] = a["vol_declare"].get(c, 0.0) + v
        site = (r[ks] or "").upper()
        if c in STOCKABLES and "ANDRA" in site and "STOCKAGE" in site and any(re.search(r"\b%s\b" % x, site) for x in CENTRES):
            a["stocke"][c] = a["stocke"].get(c, 0.0) + v
    return a


def relever(ds: dict) -> tuple[dict, dict]:
    ans, sources = {}, {}
    for res in ds["resources"]:
        m = re.search(r"(20\d\d)", res["title"])
        if not m or res.get("format", "").lower() != "csv":
            continue
        y = int(m.group(1))
        rows, cles, sha = lire_annee(res["url"])
        ans[y] = agreger(rows, cles)
        sources[y] = {"url": res["url"], "sha256": sha, "titre": res["title"]}
    if not ans:
        fail("aucun fichier annuel lu dans le catalogue")
    return ans, sources


# ------------------------------------------------------------------ calcul
def calcul(ans: dict) -> dict:
    yv = max(ans)
    for c in CATS:
        if ans[yv]["vol"].get(c, 0) <= 0:
            fail("%d : categorie %s absente ou nulle" % (yv, c))
    eds = sorted(y for y, a in ans.items()
                 if a["vol"].get("HA") and a["vol_declare"].get("HA", 0) / a["vol"]["HA"] >= COUVERTURE_ACT)
    if not eds:
        fail("aucune edition avec activite declaree")
    ya = max(eds)
    tot5 = lambda y: sum(ans[y]["vol"][c] for c in CATS)  # noqa: E731
    pv = {c: 100 * ans[yv]["vol"][c] / tot5(yv) for c in CATS}
    # comparaison SYNCHRONE (contre-expertise PRO-20261026-045248, P6) : volume et activité au même millésime
    pv_a = {c: 100 * ans[ya]["vol"][c] / tot5(ya) for c in CATS}
    def pa(y):
        t = sum(ans[y]["act"].values())
        return {c: 100 * ans[y]["act"].get(c, 0.0) / t for c in CATS}
    # variante : volumes sans activité déclarée crédités de l'activité moyenne de leur catégorie (même année)
    aj = {c: (ans[ya]["act"][c] * ans[ya]["vol"][c] / ans[ya]["vol_declare"][c]) for c in ans[ya]["act"] if ans[ya]["vol_declare"].get(c)}
    taj = sum(aj.values())
    hb = {y: a["vol"].get("HORS_BILAN", 0.0) for y, a in ans.items()}
    an_hb = min((y for y, v in hb.items() if v > 1e6), default=None)
    return {"yv": yv, "ya": ya, "editions": eds, "pv": pv, "pv_a": pv_a, "tot5_a": tot5(ya), "pa": pa(ya),
            "rtcu": ans[yv]["hb_famille"].get("RTCU", 0.0), "pa_ed": {y: pa(y) for y in eds},
            "pa_aj": {c: 100 * aj.get(c, 0.0) / taj for c in CATS},
            "vol": {c: ans[yv]["vol"][c] for c in CATS}, "tot5": tot5(yv), "tot5_0": tot5(min(ans)), "y0": min(ans),
            "stocke": {c: 100 * ans[yv]["stocke"].get(c, 0.0) / ans[yv]["vol"][c] for c in STOCKABLES},
            "hb": hb[yv], "an_hb": an_hb, "hb_avant": max((v for y, v in hb.items() if an_hb and y < an_hb), default=0.0),
            "ans": ans}


def mutation(c: dict):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    if m == "vol":
        c["pv"]["HA"] = 0.8
    elif m == "act":
        c["pa"]["HA"] = 90.0
    elif m == "editions":
        c["pa_ed"][min(c["pa_ed"])]["HA"] = 75.0
    elif m == "ajuste":
        c["pa_aj"]["HA"] = 93.0
    elif m == "ha_mavl":
        c["pa"]["MA-VL"] = 1.0
    elif m == "ha_mavl_ed":
        c["pa_ed"][min(c["pa_ed"])]["MA-VL"] = 5.0
    elif m == "masse":
        c["pv"]["FMA-VC"] = 40.0
    elif m == "masse_a":    # comparaison synchrone : FMA-VC et TFA sous les neuf dixièmes du volume au millésime de l'activité
        c["pv_a"]["FMA-VC"] = 40.0
    elif m == "faible":
        c["pa"]["FMA-VC"] = 2.0
    elif m == "stocke":
        c["stocke"]["FMA-VC"] = 60.0
    elif m == "hors":
        c["hb"] = 4e5
    elif m == "periode":
        c["hb_avant"] = 9e5
    elif m is not None:
        fail("mutation inconnue : %s" % m)
    return m


# ------------------------------------------------------------------ gardes
def gardes(c: dict) -> int:
    n = 0

    def g(cond, msg):
        nonlocal n
        n += 1
        if not cond:
            fail("garde : " + msg)

    pv, pa = c["pv"], c["pa"]
    g(pv["HA"] < 0.5 and c["pv_a"]["HA"] < 0.5, "« quelques millièmes du volume » (HA, fin %d et fin %d) : %.2f / %.2f %%"
      % (c["yv"], c["ya"], pv["HA"], c["pv_a"]["HA"]))
    g(c["pv_a"]["FMA-VC"] + c["pv_a"]["TFA"] > 90, "« FMA-VC et TFA : plus de neuf dixièmes du volume » (fin %d) : %.1f"
      % (c["ya"], c["pv_a"]["FMA-VC"] + c["pv_a"]["TFA"]))
    g(pa["HA"] > 95, "« plus de 95 %% de la radioactivité » (HA, édition %d) : %.2f" % (c["ya"], pa["HA"]))
    g(len(c["editions"]) >= 3 and all(v["HA"] > 80 for v in c["pa_ed"].values()),
      "« à chaque édition qui déclare l'activité, plus des quatre cinquièmes » : %s" % {y: round(v["HA"], 1) for y, v in c["pa_ed"].items()})
    g(c["pa_aj"]["HA"] > 95, "« même en créditant les volumes non déclarés, plus de 95 %% » : %.2f" % c["pa_aj"]["HA"])
    g(pa["HA"] + pa["MA-VL"] > 99, "« HA et MA-VL : plus de 99 %% de la radioactivité » : %.2f" % (pa["HA"] + pa["MA-VL"]))
    g(all(v["HA"] + v["MA-VL"] > 99 for v in c["pa_ed"].values()),
      "« à chaque édition, HA et MA-VL réunis plus de 99 %% » : %s" % {y: round(v["HA"] + v["MA-VL"], 2) for y, v in c["pa_ed"].items()})
    g(pv["FMA-VC"] + pv["TFA"] > 90, "« FMA-VC et TFA : plus de neuf dixièmes du volume » : %.1f" % (pv["FMA-VC"] + pv["TFA"]))
    g(pa["FMA-VC"] + pa["TFA"] < 1, "« FMA-VC et TFA : moins de 1 %% de la radioactivité » : %.2f" % (pa["FMA-VC"] + pa["TFA"]))
    g(c["stocke"]["FMA-VC"] > 85 and c["stocke"]["TFA"] > 60,
      "« l'essentiel des FMA-VC et deux tiers des TFA sont déjà dans un centre de stockage » : %s" % {k: round(v, 1) for k, v in c["stocke"].items()})
    g(c["hb"] > 1e6, "« plus d'un million de m³ hors des bilans » : %.0f" % c["hb"])
    g(c["an_hb"] is not None and c["hb_avant"] < 2e5,
      "« ces volumes apparaissent dans le fichier ouvert à partir de fin %s » : avant, %.0f m³" % (c["an_hb"], c["hb_avant"]))
    return n


# ------------------------------------------------------------------ affichage
def affichage(c: dict, lang: str) -> dict:
    f = lambda v, d=1: lg.nombre(v, d, lang)  # noqa: E731
    pct = "%" if lang == "en" else " %"
    A = {"an_vol": str(c["yv"]), "an_act": str(c["ya"]), "an_hors": str(c["an_hb"]), "ed_premiere": str(min(c["editions"])),
         "editions": lg.enumere([str(y) for y in c["editions"]], lang), "nb_editions": lg.lettres(len(c["editions"]), lang),
         "tot5": f(c["tot5"] / 1e6, 2), "hors": f(c["hb"] / 1e6, 2),
         "ha_vol": f(c["pv"]["HA"], 2), "ha_act": f(c["pa"]["HA"], 1), "ha_act_aj": f(c["pa_aj"]["HA"], 1),
         "ha_mavl_act": f(c["pa"]["HA"] + c["pa"]["MA-VL"], 1),
         "ha_ed_bas": f(min(v["HA"] for v in c["pa_ed"].values()), 1), "ha_ed_haut": f(max(v["HA"] for v in c["pa_ed"].values()), 1),
         "ha_mavl_ed_bas": f(min(v["HA"] + v["MA-VL"] for v in c["pa_ed"].values()), 1),
         "masse_vol": f(c["pv"]["FMA-VC"] + c["pv"]["TFA"], 1), "masse_act": f(c["pa"]["FMA-VC"] + c["pa"]["TFA"], 2),
         "stocke_fmavc": f(c["stocke"]["FMA-VC"], 0), "stocke_tfa": f(c["stocke"]["TFA"], 0),
         "ha_m3": f(c["vol"]["HA"], 0),
         "ha_vol_a": f(c["pv_a"]["HA"], 2), "masse_vol_a": f(c["pv_a"]["FMA-VC"] + c["pv_a"]["TFA"], 1),
         "tot5_a": f(c["tot5_a"] / 1e6, 2), "rtcu": f(c["rtcu"] / 1e6, 2),
         "malvesi": f(round(MALVESI_ESSENTIELS_M3, -4), 0)}
    for cat in CATS:
        k = cat.lower().replace("-", "")
        # parts de volume de la FIGURE au millésime de l'activité (comparaison synchrone, P6)
        A["vol_" + k] = f(c["pv_a"][cat], 2 if c["pv_a"][cat] < 1 else 1)
        # sous 0,005 %, « 0,00 » se lirait comme une radioactivité nulle : on écrit « < 0,01 »
        A["act_" + k] = ("< " + f(0.01, 2)) if c["pa"][cat] < 0.005 else f(c["pa"][cat], 2 if c["pa"][cat] < 1 else 1)
    A["pct"] = pct
    return A


# ------------------------------------------------------------------ figure
TXT = {
    "fr": dict(titre="Déchets radioactifs : le volume ne dit pas où est la radioactivité",
               titre_m="Déchets radioactifs : le volume ne dit pas où est la radioactivité",
               desc="Pour chaque catégorie, part du volume des déchets radioactifs et part de leur radioactivité déclarée, fin {an_act} "
                    "(dernière édition qui déclare l'activité), et filière de stockage. HA : {vol_ha} % du volume, {act_ha} % de la radioactivité. MA-VL : {vol_mavl} %, "
                    "{act_mavl} %. FA-VL : {vol_favl} %, {act_favl} %. FMA-VC : {vol_fmavc} %, {act_fmavc} %. TFA : {vol_tfa} %, {act_tfa} %.",
               volume="Part du volume (fin {an_act})", activite="Part de la radioactivité (fin {an_act})", filiere="Stockage",
               source="Andra, Inventaire national (données ouvertes, data.gouv.fr) ; filières : Andra, Les Essentiels 2026",
               note="Volume en équivalent conditionné et radioactivité déclarée, cinq catégories des bilans de l'Andra, même année. "
                    "La radioactivité ne mesure à elle seule ni le risque sanitaire ni le coût de gestion.",
               montre="Fin {an_act}, les déchets de haute activité faisaient {ha_vol_a} % du volume et {ha_act} % de la radioactivité "
                      "déclarée ; leur stockage définitif est en projet."),
    "en": dict(titre="Radioactive waste: volume does not show where the radioactivity is",
               titre_m="Radioactive waste: volume does not show where the radioactivity is",
               desc="For each category, share of the volume of radioactive waste and share of its declared radioactivity, end-{an_act} "
                    "(latest edition declaring activity), and disposal route. HA: {vol_ha}% of volume, {act_ha}% of radioactivity. MA-VL: {vol_mavl}%, {act_mavl}%. "
                    "FA-VL: {vol_favl}%, {act_favl}%. FMA-VC: {vol_fmavc}%, {act_fmavc}%. TFA: {vol_tfa}%, {act_tfa}%.",
               volume="Share of volume (end-{an_act})", activite="Share of radioactivity (end-{an_act})", filiere="Disposal",
               source="Andra, National Inventory (open data, data.gouv.fr); disposal routes: Andra, Les Essentiels 2026",
               note="Volume in conditioned equivalent and declared radioactivity, five categories of Andra's balances, same year. "
                    "Radioactivity alone measures neither health risk nor management cost.",
               montre="At end-{an_act}, high-level waste made up {ha_vol_a}% of the volume and {ha_act}% of the declared radioactivity; "
                      "its final disposal is planned."),
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def t_(lang, Aff):
    return {k: v.format(**Aff) for k, v in TXT[lang].items()}


def fig(c, Aff, lang):
    t = t_(lang, Aff)
    pct = Aff["pct"]
    h = 330
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="dr-t dr-d" font-family="%s">' % (W, h + 52, FONT),
         '<title id="dr-t">%s</title><desc id="dr-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"]))]
    xv0, xa0, xf, larg = 200, 370, 540, 140
    top = 56
    for x, lib in ((xv0, t["volume"]), (xa0, t["activite"]), (xf, t["filiere"])):
        for k, l in enumerate(pied_figure.coupe(lib, 24)):
            e.append('<text x="%d" y="%d" font-size="11" font-weight="600" fill="%s">%s</text>' % (x, top + 13 * k, INK2, esc(l)))
    y0 = top + 36
    for i, cat in enumerate(CATS):
        y = y0 + 50 * i
        k = cat.lower().replace("-", "")
        for j, l in enumerate(pied_figure.coupe(NOMS[lang][cat], 30)):
            e.append('<text x="0" y="%d" font-size="11" fill="%s">%s</text>' % (y + 12 + 13 * j, INK, esc(l)))
        for x0, v, col, cle in ((xv0, c["pv_a"][cat], GRIS, "vol_" + k), (xa0, c["pa"][cat], ORANGE, "act_" + k)):
            wv = max(larg * v / 100, 1.5)
            e.append('<rect x="%d" y="%d" width="%.1f" height="16" fill="%s"/>' % (x0, y + 2, wv, col))
            poids = ' font-weight="600"' if cat == "HA" else ""
            dedans = wv >= larg - 34          # barre presque pleine : l'étiquette passe dans la barre, en blanc
            xt, ancre = (x0 + wv - 4, "end") if dedans else (x0 + wv + 4, "start")
            coul = "#ffffff" if dedans else (ORANGE if col == ORANGE else INK)
            e.append('<text x="%.1f" y="%d" font-size="11"%s fill="%s" text-anchor="%s">%s%s</text>'
                     % (xt, y + 14, poids, coul, ancre, esc(Aff[cle]), pct))
        for j, l in enumerate(pied_figure.coupe(FILIERES[lang][cat], 30)):
            e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>'
                     % (xf, y + 12 + 13 * j, BLEU if cat in STOCKABLES else INK2, esc(l)))
    return pied_figure.pied(e, h + 2, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_m(c, Aff, lang, svg_d):
    t = t_(lang, Aff)
    pct = Aff["pct"]
    e, y = pied_figure.tete_mobile("drm", t["titre_m"], desc_de(svg_d), INK, FONT)
    y += 10
    lab = {"fr": ("volume", "radioactivité"), "en": ("volume", "radioactivity")}[lang]
    for cat in CATS:
        k = cat.lower().replace("-", "")
        y += 24
        for j, l in enumerate(pied_figure.coupe(NOMS[lang][cat], 32)):
            e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y + 19 * j, INK, esc(l)))
        y += 19 * (len(pied_figure.coupe(NOMS[lang][cat], 32)) - 1)
        for lib, v, col, cle in ((lab[0], c["pv_a"][cat], GRIS, "vol_" + k), (lab[1], c["pa"][cat], ORANGE, "act_" + k)):
            y += 20
            e.append('<rect x="0" y="%d" width="%.1f" height="12" fill="%s"/>' % (y - 10, max(150 * v / 100, 1.5), col))
            e.append('<text x="%.1f" y="%d" font-size="%s" font-weight="600" fill="%s">%s%s %s</text>'
                     % (max(150 * v / 100, 1.5) + 6, y, FS_MIN, ORANGE if col == ORANGE else INK, esc(Aff[cle]), pct, lib))
        for l in pied_figure.coupe(FILIERES[lang][cat], 36):
            y += 18
            e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, BLEU if cat in STOCKABLES else INK2, esc(l)))
        y += 6
    return pied_figure.pied_mobile(e, y + 16, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fiches(figs, Aff):
    out = {}
    for lang in ("fr", "en"):
        f = "dechets-volume-activite" + SUFFIXE[lang]
        svg = figs[f + ".svg"]
        out[lang] = [dict(id="volume-activite", fichier=f, titre=html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1)),
                          montre=TXT[lang]["montre"].format(**Aff[lang]),
                          source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note"))]
    return out


def csv_texte(c) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["annee_fin", "categorie", "volume_m3_equivalent_conditionne", "activite_declaree_bq", "volume_avec_activite_declaree_m3",
                "volume_dans_un_centre_de_stockage_andra_m3"])
    for y, a in sorted(c["ans"].items()):
        for cat in CATS + ("VTC", "DSF", "HORS_BILAN"):
            if cat in a["vol"]:
                w.writerow([y, cat, "%.1f" % a["vol"][cat], "%.4e" % a["act"][cat] if cat in a["act"] else "",
                            "%.1f" % a["vol_declare"].get(cat, 0.0), "%.1f" % a["stocke"][cat] if cat in a["stocke"] else ""])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    ds = catalogue()
    if OUT_DATA.exists() and not check and "--force" not in sys.argv[1:]:
        prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
        if prev.get("meta", {}).get("catalogue_modifie") == ds.get("last_modified"):
            log("Catalogue Andra inchange (%s) : rien telecharge, rien ecrit." % ds.get("last_modified"))
            return 0
    ans, sources = relever(ds)
    c = calcul(ans)
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, lang) for lang in ("fr", "en")}
    log("Fin %d : HA %.2f %% du volume ; activite fin %d : HA %.2f %% (ajustee %.2f) ; editions %s ; hors bilan %.0f m3"
        % (c["yv"], c["pv"]["HA"], c["ya"], c["pa"]["HA"], c["pa_aj"]["HA"], c["editions"], c["hb"]))
    figs = {}
    for lang in ("fr", "en"):
        sf = SUFFIXE[lang]
        figs["dechets-volume-activite%s.svg" % sf] = fig(c, Aff[lang], lang)
        figs["dechets-volume-activite%s-m.svg" % sf] = fig_m(c, Aff[lang], lang, figs["dechets-volume-activite%s.svg" % sf])
        ec = pied_figure.parite(figs["dechets-volume-activite%s.svg" % sf], figs["dechets-volume-activite%s-m.svg" % sf], FS_MIN, (ORANGE,))
        if ec:
            fail("parite mobile %s : %s" % (lang, " ; ".join(ec)))
    pages = ROOT / "content" / "dechets-radioactifs-volume-ou-radioactivite"
    for page, sf in (("_index.md", ""), ("_index.en.md", "-en")):
        if (pages / page).exists():
            ec = pied_figure.controler_page((pages / page).read_text(encoding="utf-8"),
                                            {f: v for f, v in figs.items() if re.fullmatch(r"dechets-volume-activite%s(-m)?\.svg" % sf, f)})
            if ec:
                fail("page %s : %s" % (page, " ; ".join(ec)))
    if check:
        log("--check : %d gardes passees (%d cles), parite controlee, rien ecrit." % (n, len(Aff["fr"])))
        for f_, v in figs.items():
            log("  %s : viewBox %s" % (f_, re.search(r'viewBox="([^"]+)"', v).group(1)))
        return 0
    import cairosvg
    payload = {"meta": {"page": "https://" + PAGE_FR, "licence": "CC BY 4.0",
                        "source": "Andra, Inventaire national des matières et déchets radioactifs, fichiers « déchets déclarés à fin AAAA » (data.gouv.fr)",
                        "catalogue_modifie": ds.get("last_modified"), "fichiers": {str(y): s for y, s in sorted(sources.items())},
                        "unite_volume": "m³ en équivalent conditionné", "unite_activite": "Bq déclarés",
                        "categories_bilan": list(CATS), "hors_bilan": "catégories AUTRES / SANS CATEGORIE du fichier (gestion particulière)",
                        "filieres_transcrites": FILIERES["fr"], "filieres_source": "Andra, Les Essentiels 2026, p. 11 ; inventaire.andra.fr (classification et filières), lus le 26/10/2026",
                        "annee_volume": c["yv"], "annee_activite": c["ya"], "editions_activite": c["editions"]},
               "parts": {"volume": c["pv"], "activite": c["pa"], "activite_ajustee": c["pa_aj"],
                         "activite_par_edition": {str(y): v for y, v in c["pa_ed"].items()}, "stocke_andra": c["stocke"]},
               "affichage": Aff["fr"], "affichage_en": Aff["en"]}
    releve = None
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            if rj.releve(OUT_DATA, payload, "") == prev["releve_le"]:
                releve = prev["releve_le"]
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
               "_licence": "CC BY 4.0 — calcul Stéphane Lalut ; source Andra (Licence ouverte)", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    # Tous les PNG rendus EN MÉMOIRE avant toute écriture : un rendu qui échoue ne laisse pas un JSON neuf à côté de
    # figures anciennes (défaut constaté le 26/10/2026 : « < » non échappé, JSON écrit puis arrêt au rendu).
    pngs = {f: cairosvg.svg2png(bytestring=v.encode("utf-8"), output_width=1440, background_color="white") for f, v in figs.items()}
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(c), encoding="utf-8-sig", newline="\n")
    for f, v in figs.items():
        (OUT_IMG / f).write_text(v, encoding="utf-8")
        (OUT_IMG / f.replace(".svg", ".png")).write_bytes(pngs[f])
    OUT_FIGURES.write_text(json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dechets_radioactifs.json, static/dechets_radioactifs.csv, data/figures_dechets.json, %d figures" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
