#!/usr/bin/env python3
"""update_dette_futurs.py -- volet « Quels futurs ? Peut-on changer les règles du jeu de la dette publique ? »

Fiche de conception : docs/conception/dette-publique-quels-futurs.md. Matière, tests et arbitrages :
D:\\PRO\\06_PROMOTION\\RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\\ ; arbitrages PRO-20261109-063209, ENTRANTE Dette-04,
PRO-20261109-075318 (.claude\\external-audits\\ARBITRATIONS\\).

LOGIQUE PROSPECTIVE PROBABILISTE (consigne de l'auteur, 09/11/2026). Trois objets, jamais confondus :
  1. la RÉFÉRENCE de la Commission (DSM 2025, fiche France) : trajectoire à politique inchangée, variantes
     déterministes, et DISTRIBUTION STOCHASTIQUE publiée (centiles 10 à 90 jusqu'en 2030, probabilité que la dette de 2030
     dépasse celle de 2025). Les probabilités sont celles de la Commission, conditionnelles à l'absence de mesures
     nouvelles et aux chocs historiques qu'elle retient ; aucune probabilité n'est attribuée ici à un choix politique ;
  2. les ENGAGEMENTS et PRÉVISIONS du Gouvernement : plan budgétaire et structurel à moyen terme (PSMT, 23/10/2024) et
     rapport sur la dette annexé au PLF 2027 ; positionnés DANS la distribution de la Commission (centile atteint), en
     niveau et en variation depuis 2025 (la variation neutralise l'écart de point de départ) ;
  3. les SENSIBILITÉS de la page : leviers de taux et de croissance calculés par le moteur (moteur_dette_futurs.py),
     affichés à partir de la deuxième année (témoin AFT, étape 2) ; leviers de solde en illustration COMPTABLE seulement
     (aucun témoin d'un choc de solde permanent, arbitrage PRO-20261109-075318, B3).

Valeurs : lues par le script dans la fiche du DSM (xlsx) et dans le rapport sur la dette (PDF, PyMuPDF) ; transcrites et
vérifiées contre l'extrait archivé du PSMT (sources_futurs/psmt_2025_2029_p67_p122.txt, empreinte du PDF entier inscrite).

TÉMOINS rejoués à chaque exécution (bloquants) :
  R1 « adverse r-g » et R2 « financial stress » de la Commission (tolérances du protocole du 09/11/2026) ;
  AFT (sensibilité à +100 pb, années 2 et 5, ≤ 25 %) ; cohérences internes de la distribution publiée (centiles
  croissants, référence entre les centiles 40 et 60, probabilité cohérente avec le centile 10).
  python update_dette_futurs.py            calcule, contrôle, écrit si les données changent
  python update_dette_futurs.py --check    calcule et contrôle, n'écrit rien
  python update_dette_futurs.py --temoin   rejoue les gardes sur des mutations : chacune doit être arrêtée

MATRICE INSTITUTIONNELLE : matrice_dette_futurs.py (source sources_futurs/matrice_institutionnelle.yaml) écrit le bloc
« matrice » du jeu et static/dette_futurs_matrice.csv (tableau complet, FR et EN) ; ses gardes sont dans le module.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moteur_dette_futurs as M  # noqa: E402
import releve_jeu as rj  # noqa: E402
import langue_generee as lg  # noqa: E402
import figures_dette_futurs as FIG  # noqa: E402
import pied_figure as pf  # noqa: E402
import matrice_dette_futurs as MX  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PIECES = ROOT / "scripts" / "sources_futurs"
OUT_DATA = ROOT / "data" / "dette_futurs.json"
OUT_STATIC = ROOT / "static" / "dette_futurs.json"
OUT_CSV = ROOT / "static" / "dette_futurs.csv"
OUT_MAT_CSV = ROOT / "static" / "dette_futurs_matrice.csv"
OUT_FIGURES = ROOT / "data" / "figures_futurs.json"   # fiches « Réutiliser », lues dans les SVG
MONTRE = {
    "fr": [("eventail", "dette-futurs-eventail", "a_titre", "Où mène la trajectoire actuelle selon la Commission européenne, à politique inchangée et sous des chocs historiques, et où se placent les trajectoires annoncées par le Gouvernement en 2024 et en 2026."),
           ("leviers", "dette-futurs-leviers", "b_titre", "Ce que changeraient en 2035, un à la fois, un solde primaire supérieur d'un point de PIB, quelques dixièmes de point de taux ou un demi-point de croissance, sur la référence de la Commission.")],
    "en": [("eventail", "dette-futurs-eventail-en", "a_titre", "Where the current path leads according to the European Commission, with unchanged policy and under historical shocks, and where the paths announced by the Government in 2024 and 2026 stand."),
           ("leviers", "dette-futurs-leviers-en", "b_titre", "What a primary balance one point of GDP higher, a few tenths of a point of interest rates or half a point of growth would each change in 2035, on the Commission's baseline.")],
}


def fiches(figs: dict) -> dict:
    out = {}
    for lang, liste in MONTRE.items():
        out[lang] = []
        for ident, fichier, cle, montre in liste:
            svg = figs[fichier + ".svg"]
            src, note = pf.lire(svg, "pied-source"), pf.lire(svg, "pied-note")
            if not src or not note:
                fail("fiche Reutiliser : pied illisible dans %s" % fichier)
            out[lang].append(dict(id=ident, fichier=fichier, titre=FIG.T[lang][cle], montre=montre, source=src, precaution=note))
    return out
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/dette-publique-quels-futurs/"
LICENCE = "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL
CENTILES = ("p10", "p20", "p40", "p60", "p80", "p90")
APUC_2027 = None   # part des administrations centrales, lue dans le rapport sur la dette


class Garde(Exception):
    pass


def fail(msg: str) -> None:
    raise Garde(msg)


def fr(v: float, dec: int = 1) -> str:
    s = ("%." + str(dec) + "f") % v
    return s.replace("-", "−").replace(".", ",")


def en(v: float, dec: int = 1) -> str:
    return (("%." + str(dec) + "f") % v).replace("-", "−")


def piece(nom: str) -> Path:
    f = PIECES / nom
    sums = {}
    for l in (PIECES / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if l.strip():
            h, n = l.split(None, 1)
            sums[n.strip().lstrip("*")] = h
    if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest() != sums.get(nom):
        fail("piece %s absente ou empreinte differente de SHA256SUMS" % nom)
    return f


def nombres(s: str) -> list[float]:
    return [float(x.replace(",", ".").replace("−", "-")) for x in re.findall(r"[−-]?\d+,\d", s)]


# ------------------------------------------------------------------ 1. référence de la Commission
def reference() -> dict:
    rows = M.rows
    base = {a: M.d0[i] for i, a in enumerate(M.AN)}
    variantes = {}
    for cle, nom in (("historical_spb", "2. Historical SPB scenario"), ("financial_stress", "3. Financial stress scenario"),
                     ("lower_spb", "4. Lower SPB scenario"), ("adverse_rg", "5. Adverse 'r-g' scenario")):
        variantes[cle] = M.bloc_variante(nom)["Gross public debt"]
    stoch, annees = {}, None
    for r in rows:
        if len(r) > 30 and r[23] in CENTILES:
            stoch[r[23]] = {2024 + j: float(r[24 + j]) for j in range(7)}
    if sorted(stoch) != sorted(CENTILES):
        fail("DSM : centiles stochastiques introuvables (%s)" % sorted(stoch))
    proba = next((float(r[15]) for r in rows if len(r) > 15 and r[4] == "Probability of debt ratio exceeding in 2030 its 2025 level"), None)
    ecart = next((float(r[15]) for r in rows if len(r) > 15 and r[4] == "Difference between 90th and 10th percentiles (% of GDP)"), None)
    if proba is None or ecart is None:
        fail("DSM : probabilite ou ecart p90-p10 introuvable")
    # cohérences internes (témoins de lecture)
    for a in range(2026, 2031):
        v = [stoch[c][a] for c in CENTILES]
        if v != sorted(v):
            fail("DSM %d : centiles non croissants %s" % (a, v))
        if not (stoch["p40"][a] <= base[a] <= stoch["p60"][a]):
            fail("DSM %d : reference %.2f hors de [p40, p60]" % (a, base[a]))
    if stoch["p10"][2030] > base[2025] and proba < 0.90:
        fail("DSM : p10 2030 au-dessus du niveau 2025 mais probabilite %.3f < 0,90" % proba)
    if abs((stoch["p90"][2030] - stoch["p10"][2030]) - ecart) > 0.05:
        fail("DSM : ecart p90-p10 publie %.2f != %.2f lu dans les centiles" % (ecart, stoch["p90"][2030] - stoch["p10"][2030]))
    return dict(base=base, variantes=variantes, stoch=stoch, proba=proba, ecart=ecart)


def centile(x: float, points: list[tuple[float, float]]) -> float | None:
    """Centile atteint par x, interpolé linéairement entre centiles publiés ; None hors de [p10, p90]."""
    for (c0, v0), (c1, v1) in zip(points, points[1:]):
        if v0 <= x <= v1:
            return c0 + (c1 - c0) * (x - v0) / (v1 - v0) if v1 > v0 else c0
    return None


def position(val: float, val_2025: float, an: int, ref: dict) -> dict:
    st, b25 = ref["stoch"], ref["base"][2025]
    niv = [(int(c[1:]), st[c][an]) for c in CENTILES]
    var = [(int(c[1:]), st[c][an] - b25) for c in CENTILES]
    cn, cv = centile(val, niv), centile(val - val_2025, var)
    return dict(valeur=val, variation=round(val - val_2025, 2), centile_niveau=cn, centile_variation=cv,
                sous_p10_niveau=val < niv[0][1], sous_p10_variation=(val - val_2025) < var[0][1])


# ------------------------------------------------------------------ 2. Gouvernement
def gouvernement() -> dict:
    global APUC_2027
    doc = fitz.open(str(piece("PLF2027_Rapport_dette_APU_2026-11-09.pdf")))
    t5 = " ".join(doc[4].get_text().split())
    m = re.search(r"Ratio d’endettement au sens de Maastricht \(1\) ((?:[−-]?\d+,\d ?){7})", t5)
    s = re.search(r"Solde effectif \(4\) ((?:[−-]?\d+,\d ?){7})", t5)
    if not m or not s:
        fail("rapport sur la dette p. 5 : tableau de trajectoire introuvable (mise en page changee)")
    dette = dict(zip(range(2024, 2031), nombres(m.group(1))))
    solde = dict(zip(range(2024, 2031), nombres(s.group(1))))
    t11 = " ".join(doc[10].get_text().split())
    a = re.search(r"Maastricht 112,6 3 306,1 115,7 3 460,5 119,3 3 639,7 121,7 3 813,9 dont contribution des administrations publiques centrales \(APUC\) [\d,]+ [\d ,]+ [\d,]+ [\d ,]+ [\d,]+ [\d ,]+ ([\d,]+) (\d) (\d{3}),(\d)", t11)
    if not a:
        fail("rapport sur la dette p. 11 : contribution des APUC 2027 introuvable")
    APUC_2027 = float(a.group(1).replace(",", ".")) / dette[2027]
    dette_md_2027 = 3813.9
    t46 = " ".join(doc[45].get_text().split())
    aft = re.search(r"\+1 % \(\+100 points de base\).*?de ([\d,]+) Md€ supplémentaires la première année, ([\d,]+) Md€ supplémentaires la deuxième année, d’environ ([\d,]+) Md€ la cinquième année", t46)
    if not aft:
        fail("rapport sur la dette p. 46 : sensibilite +100 pb introuvable")
    sens = dict(zip((1, 2, 5), [float(x.replace(",", ".")) for x in aft.groups()]))
    # PSMT : valeurs transcrites, vérifiées contre l'extrait archivé
    ext = piece("psmt_2025_2029_p67_p122.txt").read_text(encoding="utf-8")
    attendus = ["passerait de 109,9 % du PIB en 2023 à 116,5 % en 2027", "116,1 % dePIB en 2028 et 115,8 % du PIB en 2029",
                "Dette publique totale109,9112,9114,7"]
    for e in attendus:
        if e not in ext:
            fail("PSMT : passage transcrit absent de l'extrait archive : %r" % e)
    psmt = {2023: 109.9, 2024: 112.9, 2025: 114.7, 2027: 116.5, 2028: 116.1, 2029: 115.8}
    return dict(plf2027=dict(dette=dette, solde=solde), psmt=psmt, aft=sens, apuc_2027=APUC_2027, dette_md_2027=dette_md_2027)


# ------------------------------------------------------------------ 3. moteur, témoins, sensibilités
def pib_md(dette_md_2027: float, dette_2027: float) -> dict:
    k = {a: i for i, a in enumerate(M.AN)}
    p = {2027: dette_md_2027 / (dette_2027 / 100)}
    for a in range(2028, 2037):
        p[a] = p[a - 1] * (1 + M.g0[k[a]])
    for a in range(2026, 2023, -1):
        p[a] = p[a + 1] / (1 + M.g0[k[a + 1]])
    return p


def interets_md(sim: dict, pib: dict) -> dict:
    k = {a: i for i, a in enumerate(M.AN)}
    out, prev = {}, M.d0[0]
    for a in M.AN[1:]:
        d, it, _, _ = sim[a]
        out[a] = prev * (it / 100) / (1 + M.g0[k[a]]) / 100 * pib[a]
        prev = d
    return out


def temoins(gv: dict, mut: dict) -> dict:
    base = M.projeter(**mut)
    k = {a: i for i, a in enumerate(M.AN)}
    # R1
    T = M.bloc_variante("5. Adverse 'r-g' scenario")
    s = M.projeter(dmarche={a: 0.5 for a in range(2026, 2037)}, dg_perm={a: -0.5 for a in range(2026, 2037)}, **mut)
    for a in (2028, 2030, 2032, 2035):
        dt, pt = s[a][1] - base[a][1], T["Implicit interest rate (nominal)"][a] - M.i0[k[a]]
        dd, pd = s[a][0] - base[a][0], T["Gross public debt"][a] - M.d0[k[a]]
        if abs(dt - pt) > 0.10 or abs(dd - pd) > (1.5 if a == 2035 else 1.0):
            fail("temoin R1 %d : taux %.3f/%.3f, dette %.2f/%.2f hors tolerance" % (a, dt, pt, dd, pd))
    # R2
    T = M.bloc_variante("3. Financial stress scenario")
    prime = 0.06 * (M.d0[k[2025]] - 90)
    s = M.projeter(dmarche={2026: 1.0 + prime, 2027: 0.0}, **mut)
    for a in (2028, 2030, 2032, 2035):
        dt, pt = s[a][1] - base[a][1], T["Implicit interest rate (nominal)"][a] - M.i0[k[a]]
        dd, pd = s[a][0] - base[a][0], T["Gross public debt"][a] - M.d0[k[a]]
        if abs(dt - pt) > 0.10 or abs(dd - pd) > (1.5 if a == 2035 else 1.0):
            fail("temoin R2 %d : taux %.3f/%.3f, dette %.2f/%.2f hors tolerance" % (a, dt, pt, dd, pd))
    # AFT (années 2 et 5 ; l'année 1 n'est pas affichée : calendrier d'émission, étape 2)
    pib = pib_md(gv["dette_md_2027"], gv["plf2027"]["dette"][2027])
    s = M.projeter(dmarche={a: 1.0 for a in range(2027, 2037)}, **mut)
    ib, is_ = interets_md(base, pib), interets_md(s, pib)
    aft = {}
    for n, a in ((2, 2028), (5, 2031)):
        eng = (is_[a] - ib[a]) * gv["apuc_2027"]
        if abs(eng - gv["aft"][n]) / gv["aft"][n] > 0.25:
            fail("temoin AFT annee %d : moteur %.1f Md€ contre %.1f publie" % (n, eng, gv["aft"][n]))
        aft[n] = round(eng, 2)
    return dict(aft_moteur=aft, pib=pib, base=base)


def sensibilites(t: dict) -> dict:
    base, pib = t["base"], t["pib"]
    ib = interets_md(base, pib)
    out = {}
    for cle, kw in (("taux_moins_10pb", dict(dmarche={a: -0.10 for a in range(2027, 2037)})),
                    ("taux_moins_20pb", dict(dmarche={a: -0.20 for a in range(2027, 2037)})),
                    ("taux_plus_100pb", dict(dmarche={a: 1.0 for a in range(2027, 2037)})),
                    ("croissance_plus_05", dict(dg_perm={a: 0.5 for a in range(2027, 2037)})),
                    ("croissance_moins_05", dict(dg_perm={a: -0.5 for a in range(2027, 2037)}))):
        s = M.projeter(**kw)
        is_ = interets_md(s, pib)
        out[cle] = {"dette_2030": s[2030][0] - base[2030][0], "dette_2035": s[2035][0] - base[2035][0],
                    "interets_md_2028": is_[2028] - ib[2028], "interets_md_2035": is_[2035] - ib[2035]}
    # Calcul COMPTABLE (arbitrage ENTRANTE Dette-07, 09/11/2026) : un point de solde primaire de plus chaque année de 2028
    # à 2035, propagé par la seule identité de la dette, taux et croissance de la référence inchangés (multiplicateur et
    # effet conjoncturel nuls). Ce n'est pas une simulation du moteur (arbitrage PRO-20261109-075318, B3) ; la somme non
    # capitalisée (8 points) sous-estimait l'effet, la dette évitée cessant aussi de porter intérêts.
    s = M.projeter(dspb={a: 1.0 for a in range(2028, 2037)}, mult=0.0, eps=0.0)
    out["solde_plus_1_comptable"] = {"annees": 8, "dette_2030": s[2030][0] - base[2030][0],
                                     "dette_2035": s[2035][0] - base[2035][0]}
    # Règle d'or (matrice, cas 3) : un point de PIB d'investissement emprunté chaque année de 2028 à 2035, sans effet sur
    # la croissance ni sur les taux (même calcul comptable, de signe opposé). L'effet net dépend du rendement, non modélisé.
    s = M.projeter(dspb={a: -1.0 for a in range(2028, 2037)}, mult=0.0, eps=0.0)
    out["investissement_emprunte_1pt_comptable"] = {"annees": 8, "dette_2030": s[2030][0] - base[2030][0],
                                                    "dette_2035": s[2035][0] - base[2035][0]}
    # Valeurs BRUTES : on n'arrondit qu'à l'écriture (sens_ecrit). Un arrondi à 2 décimales ici, puis à 1 à l'affichage,
    # imprimait 6,0 pour 5,947 (contrôleur des figures, 09/11/2026).
    return out


def sens_ecrit(sens: dict) -> dict:
    """Sensibilités arrondies pour le JSON et le CSV : 3 décimales en points de PIB, 1 en Md€."""
    return {k: {m: (v if m == "annees" else round(v, 1 if m.startswith("interets") else 3)) for m, v in d.items()}
            for k, d in sens.items()}


# ------------------------------------------------------------------ calcul complet
def calculer(mut: dict | None = None) -> dict:
    mut = dict(mut or {})
    facteur_aft = mut.pop("_aft", 1.0)   # mutation de témoin : sensibilité AFT faussée
    ref = reference()
    gv = gouvernement()
    gv["aft"] = {n: v * facteur_aft for n, v in gv["aft"].items()}
    t = temoins(gv, mut)
    pos = {"plf2027_2030": position(gv["plf2027"]["dette"][2030], gv["plf2027"]["dette"][2025], 2030, ref),
           "psmt_2029": position(gv["psmt"][2029], gv["psmt"][2025], 2029, ref)}
    for cle, p in pos.items():
        cn, cv = p["centile_niveau"], p["centile_variation"]
        p["depend_du_point_de_depart"] = (cn is None) != (cv is None) or (cn is not None and cv is not None and abs(cn - cv) > 10)
    return dict(ref=ref, gv=gv, aft_moteur=t["aft_moteur"], pos=pos, sens=sensibilites(t))


def affichage(R: dict, lang: str) -> dict:
    f = fr if lang == "fr" else en
    ref, gv, pos, sens = R["ref"], R["gv"], R["pos"], R["sens"]
    p = pos["plf2027_2030"]
    q = pos["psmt_2029"]
    # Gardes de prose (la page les écrit en clair) :
    #  « la prévision du Gouvernement se situe dans la moitié basse de l'éventail » : centiles < 50, en niveau ET en variation ;
    #  « la promesse de 2024 pour 2029 tombe sous le 10e centile en niveau » ; « son rang dépend du point de départ » ;
    #  « la prévision de 2026 pour 2027 dépasse la promesse de 2024 » ; « probabilité de plus de neuf chances sur dix ».
    if p["centile_niveau"] is None or p["centile_variation"] is None or p["centile_niveau"] >= 50 or p["centile_variation"] >= 50:
        fail("prose : la prevision du PLF 2027 pour 2030 n'est plus dans la moitie basse de l'eventail (%s)" % p)
    if not q["sous_p10_niveau"] or not q["depend_du_point_de_depart"] or q["centile_variation"] is None:
        fail("prose : la promesse du PSMT pour 2029 n'est plus sous le 10e centile en niveau avec un rang qui depend du depart (%s)" % q)
    if gv["plf2027"]["dette"][2027] <= gv["psmt"][2027]:
        fail("prose : la prevision 2027 ne depasse plus la promesse de 2024")
    if ref["proba"] <= 0.9:
        fail("prose : « plus de neuf chances sur dix » n'est plus vrai (%.3f)" % ref["proba"])
    if not ref["base"][2035] > ref["base"][2030] > ref["base"][2025]:
        fail("prose : la reference ne monte plus continument de 2025 a 2035")
    pts = lambda v: lg.points(abs(v), 1, lang)
    md = lambda v: lg.nombre(abs(v), 1, lang)
    s = sens
    B = {
        "dsm_publie": "12 février 2026" if lang == "fr" else "12 February 2026",
        "ref_2036": f(ref["base"][2036]) if 2036 in ref["base"] else "",
        "plf_2025": f(gv["plf2027"]["dette"][2025]), "plf_2030_var": f(p["variation"]),
        "plf_2030_c_niv": f(p["centile_niveau"], 0), "plf_2030_c_var": f(p["centile_variation"], 0),
        "psmt_2025": f(gv["psmt"][2025]), "psmt_2029_var": f(q["variation"]), "psmt_2029_c_var": f(q["centile_variation"], 0),
        "taux10_2035_pts": pts(s["taux_moins_10pb"]["dette_2035"]), "taux20_2035_pts": pts(s["taux_moins_20pb"]["dette_2035"]),
        "taux20_int_2035": md(s["taux_moins_20pb"]["interets_md_2035"]),
        "taux100_2035_pts": pts(s["taux_plus_100pb"]["dette_2035"]), "taux100_int_2035": md(s["taux_plus_100pb"]["interets_md_2035"]),
        "croiss_plus_2035_pts": pts(s["croissance_plus_05"]["dette_2035"]), "croiss_moins_2035_pts": pts(s["croissance_moins_05"]["dette_2035"]),
        "solde_2030_pts": pts(s["solde_plus_1_comptable"]["dette_2030"]), "solde_2035_pts": pts(s["solde_plus_1_comptable"]["dette_2035"]),
        "invest_2035_pts": pts(s["investissement_emprunte_1pt_comptable"]["dette_2035"]),
        "aft_an1": f(gv["aft"][1], 1),
        "n_operations": lg.lettres(len(R["matrice"]["matrice"]["fr"]["operations"]), lang) if "matrice" in R else "",
        "n_operations_maj": lg.lettres(len(R["matrice"]["matrice"]["fr"]["operations"]), lang).capitalize() if "matrice" in R else "",
        "cac_part": lg.nombre(R["matrice"]["matrice"]["aft"]["cac_part"], 1, lang) if "matrice" in R else "",
    }
    for k in ("taux_moins_10pb", "taux_moins_20pb", "croissance_plus_05", "solde_plus_1_comptable"):
        if s[k]["dette_2035"] >= 0:
            fail("prose : %s ne fait plus baisser la dette en 2035" % k)
    for k in ("taux_plus_100pb", "croissance_moins_05", "investissement_emprunte_1pt_comptable"):
        if s[k]["dette_2035"] <= 0:
            fail("prose : %s ne fait plus monter la dette en 2035" % k)
    def ordinal(v):
        n = int(f(v, 0)) if lang == "en" else int(f(v, 0))
        return "%d%s" % (n, "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
    if lang == "en":
        B.update(plf_2030_c_niv_ord=ordinal(p["centile_niveau"]), plf_2030_c_var_ord=ordinal(p["centile_variation"]),
                 psmt_2029_c_var_ord=ordinal(q["centile_variation"]))
    A = {**B,
        "ref_2025": f(ref["base"][2025]), "ref_2030": f(ref["base"][2030]), "ref_2035": f(ref["base"][2035]),
        "proba_2030_pct": f(ref["proba"] * 100, 0), "p10_2030": f(ref["stoch"]["p10"][2030]), "p90_2030": f(ref["stoch"]["p90"][2030]),
        "ecart_p90_p10": f(ref["ecart"]),
        "plf_2027": f(gv["plf2027"]["dette"][2027]), "plf_2028": f(gv["plf2027"]["dette"][2028]), "plf_2030": f(gv["plf2027"]["dette"][2030]),
        "psmt_2027": f(gv["psmt"][2027]), "psmt_2029": f(gv["psmt"][2029]),
        "ecart_promesse_2027": f(gv["plf2027"]["dette"][2027] - gv["psmt"][2027]),
        "plf_2030_centile_variation": f(p["centile_variation"], 0) if p["centile_variation"] is not None else "",
        "aft_an5": f(gv["aft"][5], 1), "aft_an2": f(gv["aft"][2], 1),
        "eurobonds_20pb_2035": f(abs(sens["taux_moins_20pb"]["dette_2035"]), 1),
        "croissance_05_2035": f(abs(sens["croissance_plus_05"]["dette_2035"]), 0),
    }
    return A


def csv_texte(R: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["objet", "serie", "annee", "valeur", "unite", "source"])
    for a, v in R["ref"]["base"].items():
        w.writerow(["reference", "politique_inchangee", a, round(v, 2), "% du PIB", "Commission européenne, DSM 2025"])
    for k, s in R["ref"]["variantes"].items():
        for a, v in s.items():
            w.writerow(["reference", k, a, round(v, 2), "% du PIB", "Commission européenne, DSM 2025"])
    for c, s in R["ref"]["stoch"].items():
        for a, v in s.items():
            w.writerow(["distribution", c, a, round(v, 2), "% du PIB", "Commission européenne, DSM 2025 (projections stochastiques)"])
    for a, v in R["gv"]["plf2027"]["dette"].items():
        w.writerow(["gouvernement", "prevision_plf2027", a, v, "% du PIB", "Rapport sur la dette des APU, annexe au PLF 2027"])
    for a, v in R["gv"]["psmt"].items():
        w.writerow(["gouvernement", "engagement_psmt_2024", a, v, "% du PIB", "PSMT 2025-2029 (23/10/2024)"])
    for k, s in sens_ecrit(R["sens"]).items():
        for m, v in s.items():
            w.writerow(["sensibilite", k + ":" + m, "", v, "points de PIB ou Md€", "calcul de l'auteur, moteur calé sur la Commission"])
    return buf.getvalue()


def payload(R: dict) -> dict:
    ref, gv = R["ref"], R["gv"]
    return {
        "meta": {"releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "page": "https://" + PAGE_URL,
                 "licence": "CC BY 4.0", "sources": ["Commission européenne, Debt Sustainability Monitor 2025 (12/02/2026), fiche France",
                                                    "Rapport sur la dette des administrations publiques, annexe au PLF 2027",
                                                    "Plan budgétaire et structurel à moyen terme 2025-2029 (23/10/2024)"]},
        "reference": {"politique_inchangee": ref["base"], "variantes": ref["variantes"], "distribution": ref["stoch"],
                      "probabilite_2030_au_dessus_de_2025": ref["proba"], "ecart_p90_p10_2030": ref["ecart"]},
        "gouvernement": {"prevision_plf2027": gv["plf2027"], "engagement_psmt_2024": gv["psmt"],
                         "sensibilite_aft_100pb_md": gv["aft"], "part_apuc_2027": round(gv["apuc_2027"], 4)},
        "positionnement": R["pos"], "sensibilites": sens_ecrit(R["sens"]), "temoin_aft_moteur_md": R["aft_moteur"],
        "matrice": R["matrice"]["matrice"],
        "affichage": affichage(R, "fr"), "affichage_en": affichage(R, "en"),
    }


def main() -> int:
    if "--temoin" in sys.argv:
        stop = 0
        cas = (("passage immediat des taux", dict(passage=False)), ("sensibilite AFT doublee", dict(_aft=2.0)))
        for nom, mut in cas:
            try:
                calculer(mut)
                print("MUTATION NON ARRETEE : %s" % nom)
            except Garde as e:
                stop += 1
                print("arretee : %s -> %s" % (nom, e))
        R0 = calculer()
        cas_m = (("montant saisi dans la matrice", dict(ajout=" Soit 12,5 Md€.")),
                 ("ecart AFT non declare", dict(ecarts=set())),
                 ("jeton inconnu dans la matrice", dict(ajout=" {inconnu}")))
        for nom, mut in cas_m:
            try:
                MX.construire(R0, piece, mut)
                print("MUTATION NON ARRETEE : %s" % nom)
            except MX.Garde as e:
                stop += 1
                print("arretee : %s -> %s" % (nom, e))
        return 0 if stop == len(cas) + len(cas_m) else 1
    try:
        R = calculer()
        R["matrice"] = MX.construire(R, piece)
    except (Garde, MX.Garde) as e:
        print("ARRET : %s" % e)
        return 1
    P = payload(R)
    figs = FIG.produire(R)
    ecarts = []
    for nom, svg in figs.items():
        if nom.endswith("-m.svg"):
            ecarts += ["%s : %s" % (nom, x) for x in pf.parite(figs[nom.replace("-m.svg", ".svg")], svg, pf.POLICE_M,
                                                               (FIG.BLEU, FIG.ORANGE, FIG.ORANGE_A))]
    if ecarts:
        print("ARRET : parite telephone / bureau : %s" % ecarts)
        return 1
    if "--check" in sys.argv:
        print(json.dumps({k: P[k] for k in ("positionnement", "sensibilites", "temoin_aft_moteur_md", "affichage")}, ensure_ascii=False, indent=1, default=str))
        return 0
    P = rj.normalise(json.loads(json.dumps(P, ensure_ascii=False, default=str)))
    releve = P["meta"]["releve_le"]
    if OUT_DATA.exists():
        prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
        a = json.loads(json.dumps(prev)); a.pop("releve_le", None); a.pop("_licence", None)
        b = json.loads(json.dumps(P))
        for x in (a, b):
            x["meta"] = dict(x["meta"], releve_le=None)
            x.pop("affichage", None); x.pop("affichage_en", None)
        if a == b and prev.get("releve_le"):
            releve = prev["releve_le"]
    P["meta"]["releve_le"] = releve
    P = {"releve_le": releve, "_licence": LICENCE, **P}
    txt = json.dumps(P, ensure_ascii=False, indent=1) + "\n"
    ctxt = csv_texte(R)
    mtxt = R["matrice"]["csv"]
    try:
        fic = fiches(figs)
    except Garde as e:
        print("ARRET : %s" % e)
        return 1
    ftxt = json.dumps(fic, ensure_ascii=False, indent=1) + "\n"
    figs_identiques = all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s
                          and (OUT_IMG / n.replace(".svg", ".png")).exists() for n, s in figs.items())
    if OUT_DATA.exists() and OUT_STATIC.exists() and OUT_CSV.exists() and OUT_DATA.read_text(encoding="utf-8") == txt \
            and OUT_STATIC.read_text(encoding="utf-8") == txt and OUT_CSV.read_text(encoding="utf-8-sig") == ctxt \
            and OUT_MAT_CSV.exists() and OUT_MAT_CSV.read_text(encoding="utf-8-sig") == mtxt and figs_identiques \
            and OUT_FIGURES.exists() and OUT_FIGURES.read_text(encoding="utf-8") == ftxt:
        print("Donnees et figures identiques : rien ecrit (releve_le %s)." % releve)
        return 0
    try:
        import cairosvg
    except ImportError:
        print("ARRET : cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout")
        return 1
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(ctxt, encoding="utf-8-sig", newline="\n")
    OUT_MAT_CSV.write_text(mtxt, encoding="utf-8-sig", newline="\n")
    OUT_FIGURES.write_text(ftxt, encoding="utf-8")
    for nom, svg in figs.items():
        (OUT_IMG / nom).write_text(svg, encoding="utf-8")
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(OUT_IMG / nom.replace(".svg", ".png")),
                         output_width=1440 if not nom.endswith("-m.svg") else 900, background_color="white")
    print("ecrit : %s, %s, %s, %s (releve_le %s)" % (OUT_DATA.name, OUT_STATIC.name, OUT_CSV.name, OUT_MAT_CSV.name, releve))
    return 0


if __name__ == "__main__":
    sys.exit(main())
