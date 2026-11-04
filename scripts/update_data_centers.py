#!/usr/bin/env python3
"""update_data_centers.py -- page « Data centers : les gigawatts réservés annoncent-ils la consommation ? » (27/10/2026).

Origine : contre-expertise PRO-20261026-033434 (graphe G4, accepté avec modification : deux panneaux, puissances
réservées et consommation effective et projetée, jamais un taux d'utilisation calculé entre GW et TWh ; chiffres lus dans
une publication de RTE, datés), fiche docs/conception/data-centers-puissance-reservee.md.

Découverte : en dix-huit mois, la puissance de raccordement réservée par les data centers auprès de RTE a plus que triplé ;
plus de la moitié des gigawatts réservés en novembre 2025 visent une mise en service à partir de 2030, et près d'un
gigawatt de réservations a été abandonné depuis 2023 ; la consommation mesurée des centres raccordés au réseau de
transport reste de l'ordre du térawattheure. RTE lui-même ne convertit pas les réservations en consommation.

Entrées (aucune série statistique ouverte n'existe ; trois publications de RTE, téléchargées à chaque passage, empreintes
SHA-256 consignées dans le jeu) :
  - Bilan prévisionnel 2025-2035, volet consommation (PDF, décembre 2025) ;
  - Bilan électrique 2025, principaux résultats (PDF, février 2026) ;
  - page « Les data centers en chiffres clés » (HTML, date de mise à jour lue dans la page).
Deux catégories de valeurs, déclarées comme telles dans le jeu :
  - LUES DANS LE TEXTE : chaque valeur est capturée par une expression régulière dans la phrase de la publication qui la
    porte (table TEXTES) ; phrase absente = arrêt, rien n'est écrit ;
  - MESURÉES SUR UNE FIGURE : répartition par statut des réservations (figure 2.3 du Bilan prévisionnel) et trajectoires
    de 2030 (figure 2.10), lues sur la géométrie vectorielle du PDF. Témoins : les sommes par couleur de la figure 2.3
    retrouvent les trois totaux que le Bilan électrique écrit en toutes lettres (centres de données, hydrogène,
    industrie), ce qui valide l'échelle ET l'attribution des couleurs ; les tracés de la figure 2.10 retrouvent les
    valeurs de 2035 écrites dans le texte, et leurs valeurs de 2030 les étiquettes de la figure.
Chaque qualificatif de la prose est une garde ; si la donnée le dément, arrêt, rien n'est écrit.

Usage : python scripts/update_data_centers.py [--check]
        [--mutation=triple|devant|moitie|abandon|totaux|trace2035|trace2030|conso|ordre|ecart|raccorde|texte|doublon]
Sorties : data/ et static/data_centers.json, static/data_centers.csv, data/figures_data_centers.json,
          static/img/data-centers-reserve-consomme{,-en}{,-m}.svg + .png
"""
from __future__ import annotations

import csv
import gzip
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
OUT_DATA = ROOT / "data" / "data_centers.json"
OUT_STATIC = ROOT / "static" / "data_centers.json"
OUT_CSV = ROOT / "static" / "data_centers.csv"
OUT_FIGURES = ROOT / "data" / "figures_data_centers.json"
OUT_IMG = ROOT / "static" / "img"
FIG = "data-centers-reserve-consomme"
PAGE_FR = "stephane-lalut.com/data-centers-puissance-reservee/"
PAGE_EN = "stephane-lalut.com/en/data-centres-reserved-capacity/"

SOURCES = {
    "bp": ("https://assets.rte-france.com/prod/public/2025-12/2025-12-23-bilan-previsionnel-2025-consommation.pdf",
           "RTE, Bilan prévisionnel 2025-2035, La consommation d'électricité (décembre 2025)"),
    "be": ("https://assets.rte-france.com/prod/public/2026-02/Bilan-electrique-2025-principaux-resultats.pdf",
           "RTE, Bilan électrique 2025, principaux résultats (février 2026)"),
    "web": ("https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france",
            "RTE, « Les data centers en chiffres clés » (page web)"),
    # contrôle indépendant de RTE (contre-expertise du 04/11/2026) : recensement du service statistique du ministère
    "sdes": ("https://www.statistiques.developpement-durable.gouv.fr/la-consommation-delectricite-des-data-centers-en-2024",
             "SDES, « La consommation d'électricité des data centers en 2024 »"),
}
N = r"(\d+(?:,\d+)?)"   # nombre français
# Valeurs LUES DANS LE TEXTE : (clé, source, expression sur le texte normalisé ; chaque groupe nommé est une valeur).
TEXTES = [
    ("reserve_2026", "web", r"En mai 2026, RTE avait réservé près de (?P<res_mai2026>\d+) GW de capacité, pour environ (?P<projets_2026>\d+) projets"),
    ("reserve_2024", "web", r"Fin 2024, il y avait une quarantaine de projets totalisant environ (?P<res_fin2024>\d+) GW"),
    ("raccordes", "web", r"(?P<sites_rte_l>Huit) d'entre eux sont directement raccordés au réseau à haute et très haute tension de RTE, "
                         r"avec une puissance cumulée de (?P<mw_rte>\d+) MW"),
    ("utilisation", "web", r"depuis deux à trois ans ne consomment pour l'instant, en moyenne, que (?P<util_obs>\d+) ?% de la puissance qu'ils ont demandée"),
    ("montee", "web", r"il faudra (?P<montee>dix à quinze ans) pour atteindre environ (?P<montee_pct>\d+) ?%"),
    ("web_conso", "web", r"La consommation de ces centres de données est estimée à environ (?P<web_conso>\d+) TWh"),
    ("web_traj", "web", r"entre (?P<w30_bas>\d+) et (?P<w30_haut>\d+) TWh en 2030 \(environ \d+ ?% de la consommation électrique française\), "
                        r"puis entre (?P<w35_bas>\d+) et (?P<w35_haut>\d+) TWh en 2035"),
    ("droits", "be", r"atteignaient fin novembre 2025 environ (?P<tot_nov2025>\d+) GW, dont (?P<res_nov2025>%s) GW pour des centres de données, "
                     r"(?P<tot_h2>%s) GW pour des unités de production d'hydrogène et (?P<tot_ind>%s) GW pour des projets d'électrification" % (N, N, N)),
    ("conso_rpt", "be", r"Elle a atteint près de (?P<rpt_2025>%s) TWh en 2025 contre (?P<rpt_2024>%s) TWh en 2024 \((?P<enedis_2024>%s) TWh sur le réseau "
                        r"public de distribution d'Enedis en 2024\)" % (N, N, N)),
    ("conso_2024", "bp", r"de l'ordre de (?P<sd_bas>\d+) à (?P<sd_haut>\d+) TWh pour l'en-? ?semble des centres de données sur sites dédiés "
                         r"\(et entre (?P<int_bas>\d+) et (?P<int_haut>\d+) TWh en incluant les centres de données internes\)"),
    ("traj_2035", "bp", r"près de (?P<r2035>\d+) TWh en 2035 dans la trajectoire de décarbonation rapide contre (?P<l2035>\d+) TWh dans la trajectoire de décarbona"),
    ("concret_rapide", "bp", r"taux de concrétisation d'environ (?P<concret_r>\d+) ?%% \((?P<concret_r_gw>%s) GW\)" % N),
    ("concret_lente", "bp", r"taux de concrétisation d'environ (?P<concret_l>\d+) ?% pour les projets ayant demandé un raccordement au réseau de transport, avec"),
    ("util_2030", "bp", r"hypothèse de taux moyen d'utilisation de la puissance de raccordement de (?P<util_2030>\d+) ?%\d* à cet horizon"),
    ("theorique", "bp", r"ron (?P<theo_twh>\d+) TWh, soit un niveau sans commune mesure"),
    ("date_figure", "bp", r"\(situation au (?P<date_fig23>1er novembre 2025)\)"),
    ("sdes_recense", "sdes", r"En 2024, (?P<sdes_n>\d+) centres de données \(data centers\) consommant plus de 1 GWh par an ont été identifiés "
                             r"en France métropolitaine\. Ils consomment au total près de (?P<sdes_twh>%s) TWh" % N),
    ("sdes_total", "sdes", r"la consommation totale d'électricité des centres de données de France métropolitaine est estimée entre "
                           r"(?P<sdes_bas>%s) et (?P<sdes_haut>%s) TWh, soit (?P<sdes_pct_bas>%s) à (?P<sdes_pct_haut>%s) ?%% de l'électricité "
                           r"consommée en France" % (N, N, N, N)),
]
STATUTS = ("raccorde_depuis_2023", "travaux", "signe_2025_2029", "signe_2030", "suspendu", "abandonne_depuis_2023")
ACTIFS = ("travaux", "signe_2025_2029", "signe_2030", "suspendu")   # périmètre des « ~30 GW » (note 3 du Bilan prévisionnel)
TOL_TOTAL = 0.4   # GW : écart admis entre une somme mesurée sur la figure 2.3 et le total écrit (précision du tracé)

W = 720
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, BLEU_CLAIR, ORANGE, ORANGE_CLAIR, GRIS = "#184f95", "#9db7da", "#eb6834", "#f5b89c", "#8a8781"
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


def num(s: str) -> float:
    return float(s.replace(",", "."))


def normalise(t: str) -> str:
    """Texte comparable d'une publication : apostrophes droites, espaces insécables et fines en espaces, césures
    conditionnelles retirées, blancs fusionnés (une phrase du PDF court sur plusieurs lignes)."""
    t = t.replace("’", "'").replace("­", "")
    t = re.sub(r"[    ]", " ", t)
    return re.sub(r"\s+", " ", t)


# ------------------------------------------------------------------ relevé
def telecharger(url: str) -> bytes:
    try:
        with urllib.request.urlopen(url, timeout=120) as r:
            raw = r.read()
        # le serveur du SDES envoie sa page compressée même sans en-tête Accept-Encoding (04/11/2026)
        return gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    except Exception as exc:
        fail("source inaccessible %s : %s" % (url, exc))


def texte_html(raw: bytes) -> str:
    t = raw.decode("utf-8", errors="strict")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def relever() -> tuple[dict, dict, dict]:
    import fitz  # PyMuPDF : texte et géométrie des PDF
    raws, textes, docs = {}, {}, {}
    for k, (url, _) in SOURCES.items():
        raws[k] = telecharger(url)
        if k in ("web", "sdes"):
            textes[k] = normalise(texte_html(raws[k]))
        else:
            docs[k] = fitz.open(stream=raws[k], filetype="pdf")
            textes[k] = normalise(" ".join(p.get_text() for p in docs[k]))
    # empreinte des seuls PDF : le HTML d'une page web peut changer d'un chargement à l'autre sans donnée nouvelle, il
    # ferait avancer la date de relevé ; la page web est identifiée par sa date de mise à jour, lue ci-dessous
    meta = {k: {"url": SOURCES[k][0], "titre": SOURCES[k][1]} for k in SOURCES}
    for k in ("bp", "be"):
        meta[k]["sha256"] = hashlib.sha256(raws[k]).hexdigest()
    m = re.search(r"(\d\d)/(\d\d)/(20\d\d) [^0-9]{0,40}Publication ?: ?(\d\d)/(\d\d)/(20\d\d)", textes["web"])
    if not m:
        fail("page web de RTE : dates de mise a jour et de publication introuvables")
    meta["web"]["mise_a_jour"] = "%s-%s-%s" % (m.group(3), m.group(2), m.group(1))
    meta["web"]["publication"] = "%s-%s-%s" % (m.group(6), m.group(5), m.group(4))
    m = re.search(r"Publié le (\d\d)/(\d\d)/(20\d\d)", textes["sdes"])
    if not m:
        fail("page du SDES : date de publication introuvable")
    meta["sdes"]["publication"] = "%s-%s-%s" % (m.group(3), m.group(2), m.group(1))
    return textes, docs, meta


def lire_textes(textes: dict) -> dict:
    v = {}
    for cle, src, motif in TEXTES:
        trouves = list(re.finditer(motif, textes[src]))
        if not trouves:
            fail("phrase introuvable dans %s (%s) : la publication a change, relire la source avant toute ecriture" % (src, cle))
        # une seule occurrence : deux phrases semblables (un autre secteur, 27/10/2026 : « taux moyen d'utilisation » de
        # l'industrie lu à la place de celui des centres de données) feraient lire la mauvaise valeur sans erreur
        if len(trouves) > 1:
            fail("%d phrases repondent a %s dans %s : expression a preciser" % (len(trouves), cle, src))
        m = trouves[0]
        for g, s in m.groupdict().items():
            v[g] = s if g in ("sites_rte_l", "montee", "date_fig23") else num(s)
    return v


def _graduations(page, xmax: float) -> tuple[float, float]:
    """Échelle verticale d'un graphique : régression des positions des graduations (nombres seuls à gauche de xmax)."""
    pts = [(float(w[4]), (w[1] + w[3]) / 2) for w in page.get_text("words") if w[0] < xmax and re.fullmatch(r"\d{1,2}", w[4])]
    if len(pts) < 5:
        fail("graduations illisibles (%d)" % len(pts))
    n = len(pts)
    mv, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    a = sum((p[0] - mv) * (p[1] - my) for p in pts) / sum((p[0] - mv) ** 2 for p in pts)
    return my - a * mv, a     # y = b + a·v


def mesurer_fig23(doc) -> dict:
    """Figure 2.3 (page 7) : cascade des réservations par statut, trois couleurs (secteurs). Rend {couleur: {statut: GW}}."""
    p = doc[6]
    if "Puissance de raccordement réservée auprès de RTE" not in normalise(p.get_text()):
        fail("figure 2.3 introuvable en page 7")
    b, a = _graduations(p, 95)
    barres = []
    for dr in p.get_drawings():
        r, f = dr["rect"], dr.get("fill")
        if dr["type"] != "f" or not f or not (20 < r.width < 40) or r.height < 0.2:
            continue
        if min(f) > 0.95 or b + a * 45 > r.y0 or r.y1 > b + 2:      # blanc (abandons voilés) ; hors du tracé
            continue
        barres.append((round(r.x0), tuple(round(c, 2) for c in f), (r.y1 - r.y0) / -a))
    cols = sorted({x for x, _, _ in barres})
    if len(cols) != len(STATUTS):
        fail("figure 2.3 : %d colonnes au lieu de %d" % (len(cols), len(STATUTS)))
    # chaque colonne porte le libellé de son statut, centré sous elle (vérifié le 27/10/2026 : l'ordre seul ne suffisait
    # pas, la légende compte sept libellés pour six colonnes, « Projets déjà mis en service » sous-titrant la première)
    premiers = ("Raccordé", "En", "Signé", "Signé", "Suspendu", "Abandonné")
    mots = [w for w in p.get_text("words") if b < (w[1] + w[3]) / 2 < b + 12]
    for x, attendu in zip(cols, premiers):
        if not any(w[4] == attendu and abs((w[0] + w[2]) / 2 - (x + 14)) < 16 for w in mots):
            fail("figure 2.3 : la colonne d'abscisse %d ne porte pas le libelle « %s »" % (x, attendu))
    out = {}
    for x, c, gw in barres:
        out.setdefault(c, {s: 0.0 for s in STATUTS})[STATUTS[cols.index(x)]] += gw
    if len(out) != 3:
        fail("figure 2.3 : %d couleurs de secteur au lieu de 3" % len(out))
    return out


def mesurer_fig210(doc) -> dict:
    """Figure 2.10 (page 28) : trajectoires de consommation des centres de données sur sites dédiés. Rend les deux tracés
    pleins (valeurs en 2030 et 2035) et les étiquettes de la figure."""
    p = doc[27]
    if "Consommation d'électricité des centres de données sur sites dédiés dans les trajectoires" not in normalise(p.get_text()):
        fail("figure 2.10 introuvable en page 28")
    mots = p.get_text("words")
    ans = {int(w[4]): (w[0] + w[2]) / 2 for w in mots if w[4] in ("2020", "2025", "2030", "2035") and 540 < w[1] < 570}
    if not {2030, 2035} <= set(ans):
        fail("figure 2.10 : axe des annees illisible")
    b, a = _graduations(p, 130)
    traces = {}
    for dr in p.get_drawings():
        c = dr.get("color")
        if dr["type"] != "s" or not c or dr.get("dashes") not in (None, "[] 0") or dr["rect"].x0 < 125:
            continue
        for it in dr["items"]:
            if it[0] == "l":
                traces.setdefault(tuple(round(x, 2) for x in c), []).append((it[1].x, it[1].y, it[2].x, it[2].y))
    def valeur(segs, x):
        for x0, y0, x1, y1 in segs:
            if min(x0, x1) - 0.5 <= x <= max(x0, x1) + 0.5 and x1 != x0:
                y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
                return (y - b) / a
        return None
    courbes = {}
    for c, segs in traces.items():
        v30, v35 = valeur(segs, ans[2030]), valeur(segs, ans[2035] - 1)
        if v30 is not None and v35 is not None and len(segs) >= 8 and abs(v35) < 60:
            courbes[c] = {"2030": v30, "2035": v35}
    if len(courbes) != 2:
        fail("figure 2.10 : %d traces pleins au lieu de 2" % len(courbes))
    unites = [u for u in mots if u[4] == "TWh"]
    etiq = [(w[0], float(w[4])) for w in mots if re.fullmatch(r"\d+", w[4]) and 350 < w[0] < 540 and 400 < w[1] < 530
            and any(abs(u[1] - w[1]) < 3 and 0 <= u[0] - w[2] < 8 for u in unites)]   # « 15 TWh » : nombre suivi de son unité
    e30 = sorted(v for x, v in etiq if abs(x - ans[2030]) < 25)
    if len(e30) != 2:
        fail("figure 2.10 : etiquettes de 2030 illisibles (%s)" % e30)
    hi, lo = sorted(courbes.values(), key=lambda d: d["2035"], reverse=True)
    return {"rapide": hi, "lente": lo, "etiquettes_2030": e30}


# ------------------------------------------------------------------ calcul
def calcul(v: dict, f23: dict, f210: dict) -> dict:
    # attribution des couleurs par les totaux écrits (Bilan électrique) : chaque couleur au total le plus proche
    totaux = {"centres_de_donnees": v["res_nov2025"], "hydrogene": v["tot_h2"], "industrie": v["tot_ind"]}
    actif = {c: sum(d[s] for s in ACTIFS) for c, d in f23.items()}
    att = {}
    for sect, t in totaux.items():
        att[sect] = min(actif, key=lambda c: abs(actif[c] - t))  # brut-ok: attribution d'une couleur au total le plus proche, aucun extremum affiché ; unicité contrôlée ci-dessous, écart gardé (témoin de la figure 2.3)
    if len(set(att.values())) != len(att):
        fail("figure 2.3 : deux secteurs attribues a la meme couleur (%s)" % att)
    dc = f23[att["centres_de_donnees"]]
    st = {s: round(dc[s], 1) for s in STATUTS}
    actif_dc = sum(dc[s] for s in ACTIFS)
    return {"v": v, "statuts": st, "actif_dc": actif_dc,
            "totaux_ecrits": totaux, "totaux_mesures": {s: actif[att[s]] for s in totaux}, "couleurs": att,
            "part_2030": 100 * dc["signe_2030"] / actif_dc,
            "avant_2030": dc["travaux"] + dc["signe_2025_2029"],
            "f210": f210, "traj": {"rapide": {"2030": None, "2035": v["r2035"]}, "lente": {"2030": None, "2035": v["l2035"]}}}


def mutation(c: dict):
    m = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
    v = c["v"]
    if m == "triple":
        v["res_mai2026"] = 14.0
    elif m == "devant":
        v["tot_h2"] = 15.0
    elif m == "moitie":
        c["part_2030"] = 45.0
    elif m == "abandon":
        c["statuts"]["abandonne_depuis_2023"] = 0.3
    elif m == "totaux":       # une couleur mal attribuée ou une échelle fausse : une somme mesurée s'écarte du total écrit
        c["totaux_mesures"]["hydrogene"] += 1.0
    elif m == "trace2035":
        c["f210"]["rapide"]["2035"] = 28.0
    elif m == "trace2030":
        c["f210"]["lente"]["2030"] = 12.0
    elif m == "conso":
        v["rpt_2025"] = 2.5
    elif m == "ordre":        # trajectoire lente au-dessus de la rapide, tracé compris (le témoin de la figure 2.10 passe)
        v["l2035"] = c["f210"]["lente"]["2035"] = 35.0
    elif m == "ecart":        # si la page web de RTE rejoint le PDF, la phrase sur l'écart doit tomber
        v["w30_bas"], v["w30_haut"] = sorted(c["f210"]["etiquettes_2030"])
        v["w35_bas"], v["w35_haut"] = v["l2035"], v["r2035"]
    elif m == "raccorde":
        v["mw_rte"] = 1500.0
    elif m == "sdes":         # le recensement du SDES ne recoupe plus l'estimation de RTE : « compatible » doit tomber
        v["sdes_bas"], v["sdes_haut"] = 9.0, 12.0
    elif m is not None and m not in ("texte", "doublon"):   # appliquées au relevé (main)
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

    v, st, f = c["v"], c["statuts"], c["f210"]
    for s, t in c["totaux_ecrits"].items():
        g(abs(c["totaux_mesures"][s] - t) <= TOL_TOTAL,
          "temoin de la figure 2.3 : %s mesure %.2f GW pour %.1f ecrits (couleurs ou echelle fausses)" % (s, c["totaux_mesures"][s], t))
    g(v["res_mai2026"] / v["res_fin2024"] > 3, "« a plus que triplé » : %.0f / %.0f GW" % (v["res_mai2026"], v["res_fin2024"]))
    g(v["res_fin2024"] < v["res_nov2025"] < v["res_mai2026"], "« a augmenté à chaque relevé » : %s" % [v["res_fin2024"], v["res_nov2025"], v["res_mai2026"]])
    g(v["res_nov2025"] > max(v["tot_h2"], v["tot_ind"]), "« les data centers, devant l'hydrogène et l'industrie » : %s / %s / %s GW"
      % (v["res_nov2025"], v["tot_h2"], v["tot_ind"]))
    g(c["part_2030"] > 50, "« plus de la moitié vise une mise en service à partir de 2030 » : %.1f %%" % c["part_2030"])
    g(st["abandonne_depuis_2023"] >= 0.5, "« près d'un gigawatt abandonné depuis 2023 » (au moins 0,5) : %.2f" % st["abandonne_depuis_2023"])
    g(abs(f["rapide"]["2035"] - v["r2035"]) <= 0.6 and abs(f["lente"]["2035"] - v["l2035"]) <= 0.6,
      "temoin de la figure 2.10 : traces 2035 %.1f / %.1f pour %.0f / %.0f ecrits" % (f["rapide"]["2035"], f["lente"]["2035"], v["r2035"], v["l2035"]))
    g(sorted(round(f[t]["2030"]) for t in ("lente", "rapide")) == [round(x) for x in f["etiquettes_2030"]],
      "trajectoires 2030 : traces %.1f / %.1f, etiquettes %s" % (f["lente"]["2030"], f["rapide"]["2030"], f["etiquettes_2030"]))
    g(v["rpt_2024"] < v["rpt_2025"] < 2, "« près de 1 TWh, contre 0,8 » (progression, ordre du térawattheure) : %s -> %s" % (v["rpt_2024"], v["rpt_2025"]))
    lo30, hi30 = sorted(f["etiquettes_2030"])
    g(lo30 < hi30 and v["l2035"] < v["r2035"] and hi30 < v["l2035"], "« 10 à 15 TWh en 2030, 21 à 32 en 2035 » (ordre) : %s %s %s %s" % (lo30, hi30, v["l2035"], v["r2035"]))
    g([v["w30_bas"], v["w30_haut"], v["w35_bas"], v["w35_haut"]] != [lo30, hi30, v["l2035"], v["r2035"]],
      "« la page web de RTE donne d'autres valeurs que le PDF » : %s-%s et %s-%s contre %s-%s et %s-%s"
      % (v["w30_bas"], v["w30_haut"], v["w35_bas"], v["w35_haut"], lo30, hi30, v["l2035"], v["r2035"]))
    g(v["mw_rte"] / 1000 < v["res_fin2024"] / 4, "« les centres déjà raccordés au réseau de RTE : une fraction des réservations » : %.1f GW" % (v["mw_rte"] / 1000))
    g(v["sdes_bas"] <= v["sd_haut"] and v["sdes_haut"] >= v["sd_bas"],
      "« compatible avec l'ordre de grandeur de RTE » : SDES %s-%s TWh, RTE %s-%s TWh" % (v["sdes_bas"], v["sdes_haut"], v["sd_bas"], v["sd_haut"]))
    return n


# ------------------------------------------------------------------ affichage
MOIS = {"fr": ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"),
        "en": ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")}


def date_longue(iso: str, lang: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    return "%s %s %d" % ("1er" if d == 1 and lang == "fr" else str(d), MOIS[lang][m - 1], y)


def affichage(c: dict, meta: dict, lang: str) -> dict:
    f = lambda x, d=1: lg.nombre(x, d, lang)  # noqa: E731
    v, st, f210 = c["v"], c["statuts"], c["f210"]
    lo30, hi30 = sorted(f210["etiquettes_2030"])
    A = {"res_fin2024": f(v["res_fin2024"], 0), "res_nov2025": f(v["res_nov2025"], 0), "res_mai2026": f(v["res_mai2026"], 0),
         "projets_2026": f(v["projets_2026"], 0), "tot_nov2025": f(v["tot_nov2025"], 0),
         "tot_h2": f(v["tot_h2"], 1 if v["tot_h2"] % 1 else 0), "tot_ind": f(v["tot_ind"], 1 if v["tot_ind"] % 1 else 0),
         "rac_gw": f(v["mw_rte"] / 1000, 1), "rac_mw": f(v["mw_rte"], 0),
         "sites_rte": lg.lettres(8, lang) if v["sites_rte_l"] == "Huit" else fail("nombre de sites raccordes : %s" % v["sites_rte_l"]),
         "util_obs": f(v["util_obs"], 0), "util_2030": f(v["util_2030"], 0), "montee_pct": f(v["montee_pct"], 0),
         "rpt_2024": f(v["rpt_2024"], 1), "rpt_2025": f(v["rpt_2025"], 0), "enedis_2024": f(v["enedis_2024"], 0),
         "sd_bas": f(v["sd_bas"], 0), "sd_haut": f(v["sd_haut"], 0), "int_bas": f(v["int_bas"], 0), "int_haut": f(v["int_haut"], 0),
         "web_conso": f(v["web_conso"], 0),
         "l2030": f(lo30, 0), "r2030": f(hi30, 0), "l2035": f(v["l2035"], 0), "r2035": f(v["r2035"], 0),
         "w30_bas": f(v["w30_bas"], 0), "w30_haut": f(v["w30_haut"], 0), "w35_bas": f(v["w35_bas"], 0), "w35_haut": f(v["w35_haut"], 0),
         "concret_r": f(v["concret_r"], 0), "concret_l": f(v["concret_l"], 0), "concret_r_gw": f(v["concret_r_gw"], 1),
         "theo_twh": f(v["theo_twh"], 0),
         "sdes_n": f(v["sdes_n"], 0), "sdes_twh": f(v["sdes_twh"], 1), "sdes_bas": f(v["sdes_bas"], 1),
         "sdes_haut": f(v["sdes_haut"], 1 if v["sdes_haut"] % 1 else 0), "sdes_pct_bas": f(v["sdes_pct_bas"], 1 if v["sdes_pct_bas"] % 1 else 0),
         "sdes_pct_haut": f(v["sdes_pct_haut"], 1 if v["sdes_pct_haut"] % 1 else 0),
         "date_sdes": date_longue(meta["sdes"]["publication"], lang),
         "st_travaux": f(st["travaux"], 1), "st_2529": f(st["signe_2025_2029"], 1), "st_2030": f(st["signe_2030"], 1),
         "st_suspendu": f(st["suspendu"], 1), "st_abandon": f(st["abandonne_depuis_2023"], 1), "st_raccorde": f(st["raccorde_depuis_2023"], 1),
         "st_avant2030": f(c["avant_2030"], 1), "part_2030": f(c["part_2030"], 0), "actif_dc": f(c["actif_dc"], 1),
         "date_web": date_longue(meta["web"]["mise_a_jour"], lang),
         "date_fig23": "1 November 2025" if lang == "en" else "1er novembre 2025",
         "montee": v["montee"] if lang == "fr" else {"dix à quinze ans": "ten to fifteen years"}.get(v["montee"]) or fail("traduction : %s" % v["montee"])}
    A["pct"] = "%" if lang == "en" else " %"
    A["deux_points"] = ": " if lang == "en" else " : "
    return A


# ------------------------------------------------------------------ figure
TXT = {
    "fr": dict(titre="Data centers : puissance réservée sur le réseau et électricité consommée",
               titre_m="Data centers : puissance réservée et électricité consommée",
               pa="Puissance de raccordement réservée auprès de RTE, en gigawatts (GW)",
               pb="Consommation d'électricité des data centers sur sites dédiés, en térawattheures par an (TWh)",
               fin2024="Fin 2024", nov2025="Novembre 2025", mai2026="Mai 2026", rac="Déjà raccordés au réseau de RTE ({sites_rte} sites)",
               avant="mise en service prévue avant 2030", apres="à partir de 2030", abandon="Suspendu (gris) : {st_suspendu} GW · abandonné depuis 2023 : environ {st_abandon} GW",
               m24="2024, mesurée (réseau de RTE)", m25="2025, mesurée (réseau de RTE)", e24="2024, estimée par RTE (tous sites dédiés)",
               t30="2030, deux trajectoires de RTE", t35="2035, deux trajectoires de RTE",
               v_fin2024="environ {res_fin2024} GW", v_nov2025="{res_nov2025} GW", v_mai2026="près de {res_mai2026} GW", v_rac="{rac_gw} GW",
               v_m24="{rpt_2024} TWh", v_m25="près de {rpt_2025} TWh", v_e24="{sd_bas} à {sd_haut} TWh", v_t30="{l2030} à {r2030} TWh", v_t35="{l2035} à {r2035} TWh",
               desc="Deux panneaux, deux grandeurs. Puissance de raccordement réservée par les data centers auprès de RTE : environ {res_fin2024} GW "
                    "fin 2024, {res_nov2025} GW en novembre 2025 (dont {st_avant2030} GW pour une mise en service avant 2030, {st_2030} GW à partir "
                    "de 2030 et {st_suspendu} GW suspendus), près de {res_mai2026} GW en mai 2026 ; {rac_gw} GW déjà raccordés au réseau de RTE ({sites_rte} sites) ; environ "
                    "{st_abandon} GW abandonnés depuis 2023. Consommation des data centers sur sites dédiés : {rpt_2024} TWh en 2024 et près de "
                    "{rpt_2025} TWh en 2025 mesurés sur le réseau de RTE ; {sd_bas} à {sd_haut} TWh estimés pour l'ensemble en 2024 ; "
                    "{l2030} à {r2030} TWh en 2030 et {l2035} à {r2035} TWh en 2035 dans les deux trajectoires de RTE.",
               source="RTE : Bilan prévisionnel 2025-2035 (déc. 2025), Bilan électrique 2025 (févr. 2026), page « Les data centers en chiffres clés » "
                      "({date_web}) ; répartition de novembre 2025 mesurée sur la figure 2.3 du Bilan prévisionnel",
               note="Une puissance réservée n'est ni une puissance appelée ni une consommation : les deux panneaux ne se comparent pas, "
                    "aucun rapport n'est calculé entre eux. Trajectoires : hypothèses de RTE, non des mesures.",
               montre="En novembre 2025, les data centers avaient réservé {res_nov2025} GW auprès de RTE, dont {st_2030} GW pour une mise en "
                      "service à partir de 2030 ; ceux raccordés au réseau de RTE consommaient près de {rpt_2025} TWh en 2025."),
    "en": dict(titre="Data centres: capacity reserved on the grid and electricity consumed",
               titre_m="Data centres: reserved capacity and electricity consumed",
               pa="Grid connection capacity reserved with RTE, in gigawatts (GW)",
               pb="Electricity consumption of dedicated-site data centres, in terawatt-hours per year (TWh)",
               fin2024="End-2024", nov2025="November 2025", mai2026="May 2026", rac="Already connected to RTE's grid ({sites_rte} sites)",
               avant="commissioning planned before 2030", apres="from 2030", abandon="Suspended (grey): {st_suspendu} GW · abandoned since 2023: about {st_abandon} GW",
               m24="2024, metered (RTE's grid)", m25="2025, metered (RTE's grid)", e24="2024, estimated by RTE (all dedicated sites)",
               t30="2030, two RTE pathways", t35="2035, two RTE pathways",
               v_fin2024="about {res_fin2024} GW", v_nov2025="{res_nov2025} GW", v_mai2026="nearly {res_mai2026} GW", v_rac="{rac_gw} GW",
               v_m24="{rpt_2024} TWh", v_m25="nearly {rpt_2025} TWh", v_e24="{sd_bas} to {sd_haut} TWh", v_t30="{l2030} to {r2030} TWh", v_t35="{l2035} to {r2035} TWh",
               desc="Two panels, two quantities. Grid connection capacity reserved by data centres with RTE: about {res_fin2024} GW at end-2024, "
                    "{res_nov2025} GW in November 2025 (of which {st_avant2030} GW for commissioning before 2030, {st_2030} GW from 2030 and {st_suspendu} GW suspended), "
                    "nearly {res_mai2026} GW in May 2026; {rac_gw} GW already connected to RTE's grid ({sites_rte} sites); about {st_abandon} GW "
                    "abandoned since 2023. Consumption of dedicated-site data centres: {rpt_2024} TWh in 2024 and nearly {rpt_2025} TWh in 2025 "
                    "metered on RTE's grid; {sd_bas} to {sd_haut} TWh estimated for all of them in 2024; {l2030} to {r2030} TWh in 2030 and "
                    "{l2035} to {r2035} TWh in 2035 in RTE's two pathways.",
               source="RTE: Bilan prévisionnel 2025-2035 (Dec. 2025), Bilan électrique 2025 (Feb. 2026), web page “Les data centers en chiffres clés” "
                      "({date_web}); November 2025 breakdown measured on figure 2.3 of the Bilan prévisionnel",
               note="Reserved capacity is neither power drawn nor consumption: the two panels are not comparable, and no ratio is computed "
                    "between them. Pathways: RTE's assumptions, not measurements.",
               montre="In November 2025, data centres had reserved {res_nov2025} GW with RTE, {st_2030} GW of it for commissioning from 2030; "
                      "those connected to RTE's grid consumed nearly {rpt_2025} TWh in 2025."),
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def t_(lang, Aff):
    return {k: v.format(**Aff) for k, v in TXT[lang].items()}


def _barre(e, x0, y, larg, vmax, segments, h=18):
    """segments : [(valeur, couleur)] empilés depuis x0 ; rend l'abscisse de fin."""
    x = x0
    for val, col in segments:
        w = max(larg * val / vmax, 1.5)
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s"/>' % (x, y, w, h, col))
        x += w
    return x


def fig(c, Aff, lang):
    t = t_(lang, Aff)
    v, st = c["v"], c["statuts"]
    lo30, hi30 = sorted(c["f210"]["etiquettes_2030"])
    xl, x0, larg = 0, 250, 330
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="dtc-t dtc-d" font-family="%s">' % (W, FONT),
         '<title id="dtc-t">%s</title><desc id="dtc-d">%s</desc>' % (esc(t["titre"]), esc(t["desc"])),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W,
         '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(t["titre"]))]
    # panneau A : gigawatts réservés
    y = 50
    e.append('<text x="0" y="%d" font-size="12" font-weight="600" fill="%s">%s</text>' % (y, BLEU, esc(t["pa"])))
    vmax = 20.0
    lignes = [(t["fin2024"], [(v["res_fin2024"], BLEU)], t["v_fin2024"]),
              (t["nov2025"], [(c["avant_2030"], BLEU), (st["signe_2030"], BLEU_CLAIR), (st["suspendu"], GRIS)], t["v_nov2025"]),
              (t["mai2026"], [(v["res_mai2026"], BLEU)], t["v_mai2026"]),
              (t["rac"], [(v["mw_rte"] / 1000, GRIS)], t["v_rac"])]
    for i, (lib, segs, val) in enumerate(lignes):
        yy = y + 18 + 34 * i
        for j, l in enumerate(pied_figure.coupe(lib, 36)):
            e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (xl, yy + 13 + 12 * j, INK, esc(l)))
        xf = _barre(e, x0, yy, larg, vmax, segs)
        e.append('<text x="%.1f" y="%d" font-size="11" font-weight="600" fill="%s">%s</text>' % (xf + 6, yy + 13, BLEU if segs[0][1] == BLEU else INK2, esc(val)))
    yy = y + 18 + 34 * len(lignes)
    # légende du découpage de novembre 2025
    lx = x0
    for col, lib in ((BLEU, t["avant"] + Aff["deux_points"] + Aff["st_avant2030"] + " GW"), (BLEU_CLAIR, t["apres"] + Aff["deux_points"] + Aff["st_2030"] + " GW")):
        e.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/>' % (lx, yy, col))
        e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (lx + 14, yy + 9, INK2, esc(lib)))
        lx += 14 + int(5.6 * len(lib)) + 16
    e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (x0, yy + 26, INK2, esc(t["abandon"])))
    # panneau B : térawattheures consommés ou projetés
    y = yy + 64
    e.append('<text x="0" y="%d" font-size="12" font-weight="600" fill="%s">%s</text>' % (y, ORANGE, esc(t["pb"])))
    vmax = 35.0
    lignes = [(t["m24"], [(v["rpt_2024"], ORANGE)], t["v_m24"]),
              (t["m25"], [(v["rpt_2025"], ORANGE)], t["v_m25"]),
              (t["e24"], [(v["sd_bas"], ORANGE_CLAIR), (v["sd_haut"] - v["sd_bas"], ORANGE_CLAIR)], t["v_e24"]),
              (t["t30"], [(lo30, ORANGE_CLAIR), (hi30 - lo30, ORANGE_CLAIR)], t["v_t30"]),
              (t["t35"], [(v["l2035"], ORANGE_CLAIR), (v["r2035"] - v["l2035"], ORANGE_CLAIR)], t["v_t35"])]
    for i, (lib, segs, val) in enumerate(lignes):
        yy = y + 18 + 34 * i
        for j, l in enumerate(pied_figure.coupe(lib, 36)):
            e.append('<text x="%d" y="%d" font-size="11" fill="%s">%s</text>' % (xl, yy + 13 + 12 * j, INK, esc(l)))
        if len(segs) == 2:       # fourchette : la borne basse en plein clair, l'écart hachuré par un contour
            xa = _barre(e, x0, yy, larg, vmax, segs[:1])
            wb = max(larg * segs[1][0] / vmax, 1.5)
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="17" fill="#ffffff" stroke="%s" stroke-width="1"/>' % (xa, yy, wb, ORANGE))
            xf = xa + wb
        else:
            xf = _barre(e, x0, yy, larg, vmax, segs)
        e.append('<text x="%.1f" y="%d" font-size="11" font-weight="600" fill="%s">%s</text>' % (xf + 6, yy + 13, ORANGE, esc(val)))
    yy = y + 18 + 34 * len(lignes)
    return pied_figure.pied(e, yy + 4, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                          (LICENCES[lang], MUTED, "pied-licence")], GRID)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_m(c, Aff, lang, svg_d):
    t = t_(lang, Aff)
    v, st = c["v"], c["statuts"]
    lo30, hi30 = sorted(c["f210"]["etiquettes_2030"])
    e, y = pied_figure.tete_mobile("dtcm", t["titre_m"], desc_de(svg_d), INK, FONT)

    def panneau(y, titre, col, vmax, lignes):
        y += 14
        for l in pied_figure.coupe(titre, 34):
            y += 18
            e.append('<text x="0" y="%d" font-size="%s" font-weight="600" fill="%s">%s</text>' % (y, FS_MIN, col, esc(l)))
        for lib, segs, val, fourchette in lignes:
            coul = INK2 if segs[0][1] == GRIS else col
            y += 10
            for l in pied_figure.coupe(lib, 36):
                y += 18
                e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK, esc(l)))
            y += 6
            if fourchette:
                xa = _barre(e, 0, y, 190, vmax, segs[:1], 12)
                wb = max(190 * segs[1][0] / vmax, 1.5)
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="11" fill="#ffffff" stroke="%s" stroke-width="1"/>' % (xa, y, wb, ORANGE))
                xf = xa + wb
            else:
                xf = _barre(e, 0, y, 190, vmax, segs, 12)
            e.append('<text x="%.1f" y="%d" font-size="%s" font-weight="600" fill="%s">%s</text>' % (min(xf + 6, 196), y + 11, FS_MIN, coul, esc(val)))
            y += 12
        return y

    y = panneau(y, t["pa"], BLEU, 20.0, [
        (t["fin2024"], [(v["res_fin2024"], BLEU)], t["v_fin2024"], False),
        (t["nov2025"], [(c["avant_2030"], BLEU), (st["signe_2030"], BLEU_CLAIR), (st["suspendu"], GRIS)], t["v_nov2025"], False),
        (t["mai2026"], [(v["res_mai2026"], BLEU)], t["v_mai2026"], False),
        (t["rac"], [(v["mw_rte"] / 1000, GRIS)], t["v_rac"], False)])
    for col, lib in ((BLEU, t["avant"] + Aff["deux_points"] + Aff["st_avant2030"] + " GW"), (BLEU_CLAIR, t["apres"] + Aff["deux_points"] + Aff["st_2030"] + " GW"),
                     (None, t["abandon"])):
        lignes = pied_figure.coupe(lib, 32)
        y += 8
        for k, l in enumerate(lignes):
            y += 18
            if col and k == 0:
                e.append('<rect x="0" y="%d" width="11" height="11" fill="%s"/>' % (y - 10, col))
            e.append('<text x="%d" y="%d" font-size="%s" fill="%s">%s</text>' % (16 if col else 0, y, FS_MIN, INK2, esc(l)))
    y = panneau(y + 10, t["pb"], ORANGE, 35.0, [
        (t["m24"], [(v["rpt_2024"], ORANGE)], t["v_m24"], False),
        (t["m25"], [(v["rpt_2025"], ORANGE)], t["v_m25"], False),
        (t["e24"], [(v["sd_bas"], ORANGE_CLAIR), (v["sd_haut"] - v["sd_bas"], ORANGE_CLAIR)], t["v_e24"], True),
        (t["t30"], [(lo30, ORANGE_CLAIR), (hi30 - lo30, ORANGE_CLAIR)], t["v_t30"], True),
        (t["t35"], [(v["l2035"], ORANGE_CLAIR), (v["r2035"] - v["l2035"], ORANGE_CLAIR)], t["v_t35"], True)])
    return pied_figure.pied_mobile(e, y + 16, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                               (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def fiches(figs, Aff):
    out = {}
    for lang in ("fr", "en"):
        f = FIG + SUFFIXE[lang]
        svg = figs[f + ".svg"]
        out[lang] = [dict(id="reserve-consomme", fichier=f, titre=html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1)),
                          montre=TXT[lang]["montre"].format(**Aff[lang]),
                          source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note"))]
    return out


def lignes_csv(c, meta) -> list[list]:
    v, st = c["v"], c["statuts"]
    lo30, hi30 = sorted(c["f210"]["etiquettes_2030"])
    L, M = "lue dans le texte", "mesurée sur la figure"
    bp, be, web = SOURCES["bp"][1], SOURCES["be"][1], SOURCES["web"][1] + " (mise à jour du %s)" % meta["web"]["mise_a_jour"]
    r = [["puissance_reservee", "centres de données, réseau de transport", "2024-12", v["res_fin2024"], v["res_fin2024"], "GW", "environ", L, web],
         ["puissance_reservee", "centres de données, réseau de transport", "2025-11", v["res_nov2025"], v["res_nov2025"], "GW", "", L, be],
         ["puissance_reservee", "centres de données, réseau de transport", "2026-05", v["res_mai2026"], v["res_mai2026"], "GW", "près de", L, web],
         ["puissance_raccordee", "centres de données raccordés au réseau de RTE (8 sites)", "2026", v["mw_rte"] / 1000, v["mw_rte"] / 1000, "GW", "", L, web]]
    for s in STATUTS:
        r.append(["puissance_reservee_par_statut", "centres de données : " + s.replace("_", " "), "2025-11-01", st[s], st[s], "GW", "à 0,1 GW près", M, bp + ", figure 2.3"])
    r += [["consommation_mesuree", "sites dédiés raccordés au réseau de transport", "2024", v["rpt_2024"], v["rpt_2024"], "TWh", "", L, be],
          ["consommation_mesuree", "sites dédiés raccordés au réseau de transport", "2025", v["rpt_2025"], v["rpt_2025"], "TWh", "près de", L, be],
          ["consommation_mesuree", "réseau public de distribution (Enedis)", "2024", v["enedis_2024"], v["enedis_2024"], "TWh", "", L, be],
          ["consommation_estimee", "ensemble des sites dédiés", "2024", v["sd_bas"], v["sd_haut"], "TWh", "de l'ordre de", L, bp],
          ["consommation_estimee", "sites dédiés et centres internes", "2024", v["int_bas"], v["int_haut"], "TWh", "", L, bp],
          ["consommation_trajectoire", "sites dédiés, trajectoire de décarbonation lente / rapide", "2030", lo30, hi30, "TWh", "", M + " (étiquettes)", bp + ", figure 2.10"],
          ["consommation_trajectoire", "sites dédiés, trajectoire de décarbonation lente / rapide", "2035", v["l2035"], v["r2035"], "TWh", "près de (rapide)", L, bp],
          ["consommation_trajectoire_page_web", "« trajectoire de décarbonation rapide »", "2030", v["w30_bas"], v["w30_haut"], "TWh", "", L, web],
          ["consommation_trajectoire_page_web", "« trajectoire de décarbonation rapide »", "2035", v["w35_bas"], v["w35_haut"], "TWh", "", L, web]]
    return r


def csv_texte(c, meta) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["grandeur", "perimetre", "date", "valeur_basse", "valeur_haute", "unite", "qualificatif_de_la_source", "nature_de_la_valeur", "source"])
    for l in lignes_csv(c, meta):
        w.writerow(l[:3] + ["%g" % l[3], "%g" % l[4]] + l[5:])
    return buf.getvalue()


# ------------------------------------------------------------------ main
def main() -> int:
    check = "--check" in sys.argv[1:] or any(a.startswith("--mutation") for a in sys.argv[1:])
    textes, docs, meta = relever()
    if "--mutation=texte" in sys.argv[1:]:   # témoin du relevé : la phrase de la page web reformulée, la lecture doit s'arrêter
        textes["web"] = textes["web"].replace("RTE avait réservé près de", "RTE avait réservé environ")
    if "--mutation=doublon" in sys.argv[1:]:  # témoin de l'unicité : une phrase présente deux fois doit arrêter la lecture
        textes["bp"] += " " + textes["bp"]
    v = lire_textes(textes)
    c = calcul(v, mesurer_fig23(docs["bp"]), mesurer_fig210(docs["bp"]))
    m = mutation(c)
    n = gardes(c)
    if m:
        fail("mutation %s : aucune garde n'a mordu" % m)
    Aff = {lang: affichage(c, meta, lang) for lang in ("fr", "en")}
    log("Reserve : %s / %s / %s GW ; nov. 2025 par statut %s (a partir de 2030 : %.1f %%) ; totaux mesures %s ; traces 2030 %s"
        % (v["res_fin2024"], v["res_nov2025"], v["res_mai2026"], c["statuts"], c["part_2030"],
           {k: round(x, 2) for k, x in c["totaux_mesures"].items()},
           {k: round(c["f210"][k]["2030"], 2) for k in ("lente", "rapide")}))
    figs = {}
    for lang in ("fr", "en"):
        sf = SUFFIXE[lang]
        figs["%s%s.svg" % (FIG, sf)] = fig(c, Aff[lang], lang)
        figs["%s%s-m.svg" % (FIG, sf)] = fig_m(c, Aff[lang], lang, figs["%s%s.svg" % (FIG, sf)])
        ec = pied_figure.parite(figs["%s%s.svg" % (FIG, sf)], figs["%s%s-m.svg" % (FIG, sf)], FS_MIN, (ORANGE, BLEU))
        if ec:
            fail("parite mobile %s : %s" % (lang, " ; ".join(ec)))
    pages = ROOT / "content" / "data-centers-puissance-reservee"
    for page, sf in (("_index.md", ""), ("_index.en.md", "-en")):
        if (pages / page).exists():
            ec = pied_figure.controler_page((pages / page).read_text(encoding="utf-8"),
                                            {f: x for f, x in figs.items() if re.fullmatch(r"%s%s(-m)?\.svg" % (FIG, sf), f)})
            if ec:
                fail("page %s : %s" % (page, " ; ".join(ec)))
    if check:
        log("--check : %d gardes passees (%d cles), parite controlee, rien ecrit." % (n, len(Aff["fr"])))
        for f_, x in figs.items():
            log("  %s : viewBox %s" % (f_, re.search(r'viewBox="([^"]+)"', x).group(1)))
        return 0
    import cairosvg
    payload = {"meta": {"page": "https://" + PAGE_FR, "licence": "CC BY 4.0", "sources": meta,
                        "nature_des_valeurs": {"lue dans le texte": "capturée par le script dans la phrase de la publication qui la porte",
                                               "mesurée sur la figure": "lue par le script sur la géométrie vectorielle du PDF ; témoins : "
                                               "totaux écrits par RTE (figure 2.3), valeurs de 2035 écrites et étiquettes (figure 2.10)"},
                        "date_repartition_par_statut": "2025-11-01",
                        "avertissement": "Une puissance de raccordement réservée n'est ni une puissance appelée ni une consommation ; "
                                         "aucun rapport n'est calculé entre GW et TWh."},
               "valeurs": {k: x for k, x in v.items()},
               "repartition_novembre_2025_gw": c["statuts"],
               "temoin_figure_2_3": {"totaux_ecrits_gw": c["totaux_ecrits"], "totaux_mesures_gw": c["totaux_mesures"]},
               "trajectoires_twh": {"2030": sorted(c["f210"]["etiquettes_2030"]), "2035": [v["l2035"], v["r2035"]],
                                    "traces_mesures": {k: c["f210"][k] for k in ("lente", "rapide")}},
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
               "_licence": "CC BY 4.0 — calcul et mesures Stéphane Lalut ; source RTE", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    # Rien n'est réécrit à sortie identique (méthode des ressources, règle 11) : chaque sortie est comparée à son fichier.
    sorties = {OUT_DATA: txt, OUT_STATIC: txt, OUT_FIGURES: json.dumps(fiches(figs, Aff), ensure_ascii=False, indent=1) + "\n"}
    sorties.update({OUT_IMG / f: x for f, x in figs.items()})
    lire = lambda p_: p_.read_text(encoding="utf-8") if p_.exists() else None  # noqa: E731
    change = {p_: x for p_, x in sorties.items() if lire(p_) != x}
    csv_ = csv_texte(c, meta)
    csv_change = not OUT_CSV.exists() or OUT_CSV.read_text(encoding="utf-8-sig") != csv_
    if not change and not csv_change:
        log("Sorties identiques (releve %s) : rien ecrit." % payload["releve_le"])
        return 0
    # PNG des figures changées rendus EN MÉMOIRE avant toute écriture (même règle que update_dechets_radioactifs.py).
    pngs = {f: cairosvg.svg2png(bytestring=x.encode("utf-8"), output_width=1440, background_color="white")
            for f, x in figs.items() if (OUT_IMG / f) in change}
    for p_, x in change.items():
        p_.write_text(x, encoding="utf-8")
    for f, b_ in pngs.items():
        (OUT_IMG / f.replace(".svg", ".png")).write_bytes(b_)
    if csv_change:
        OUT_CSV.write_text(csv_, encoding="utf-8-sig", newline="\n")
    log("Ecrit : %d fichiers de texte, %d PNG%s" % (len(change), len(pngs), ", CSV" if csv_change else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
