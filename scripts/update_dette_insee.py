#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update_dette_insee.py -- rapatrie les series officielles de dette publique,
ecrit la source unique data/dette_officielle.json, sa copie endpoint
static/dette_officielle.json, la courbe static/img/ciseau-dette-interets.svg,
et (option) l'export legacy du site compagnon.

Sources, attribution PAR BLOC (jamais melangee) :
  - INSEE BDM SDMX (anonyme) : dette de Maastricht trimestrielle
      010777616 = encours Md EUR ; 010777608 = % du PIB
  - Eurostat (API dissemination, anonyme) :
      gov_10a_main D41PAY S13 FR = interets verses par les APU (annuel)
      gov_10a_exp  TE   S13 FR   = depenses par fonction COFOG (annuel)

Invariants (arbitrage panel 2026-08-15) :
  - AUCUNE mise a jour silencieuse non testee : toute garde en echec => exit 1,
    AUCUNE ecriture, le fichier precedent reste en place ;
  - ancres exactes UNIQUEMENT sur valeurs anciennes consolidees (en bandes --
    les bases INSEE/Eurostat sont revisees) ; le recent est garde par un DELTA
    borne contre les valeurs deja committees (anti fatigue d'alarme) ;
  - tous les nombres affiches par le site derivent de ce JSON (bloc
    "affichage", chaines francaises precalculees) -- Hugo reste bete ;
  - les ratios d'equivalence sont calcules ICI, sur UN MEME millesime ;
  - aucune chaine brute des API dans les sorties : nombres re-parses en float,
    periodes revalidees par regex, libelles ecrits en dur dans ce script ;
  - sorties CONSOLE ASCII pur (console Windows cp1252). La contrainte porte
    sur print(), PAS sur le contenu des fichiers : tout libelle destine a un
    lecteur -- JSON public, titre et desc du SVG (texte lu par les lecteurs
    d'ecran) -- est en francais accentue, ecrit en UTF-8. Ne pas "corriger"
    ces accents en ASCII : ils partent dans le JSON-LD Dataset et dans la
    page (defaut trouve et corrige le 2026-08-16) ;
  - une reecriture ne se declenche QUE si un chiffre a bouge : a donnees
    identiques les deux "releve_le" sont conserves, donc le depot ne bouge pas
    et le workflow n'ouvre pas de PR vide (mesure du 2026-08-16).

Usage :
  python scripts/update_dette_insee.py             # ecrit tout
  python scripts/update_dette_insee.py --check     # fetch + gardes, rien ecrit
  python scripts/update_dette_insee.py --legacy P  # + export compagnon vers P

Decroissance : si le flux automatise (workflow dette-insee.yml) echoue plus de
2 fois par an pour une cause non-donnee, repli = execution locale trimestrielle
de ce script + commit humain (l'alternative a toujours ete viable).
"""
from __future__ import annotations

import json
import os
import re
import ssl
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_JSON = REPO / "data" / "dette_officielle.json"
OUT_ENDPOINT = REPO / "static" / "dette_officielle.json"
OUT_SVG = REPO / "static" / "img" / "ciseau-dette-interets.svg"
OUT_SVG_TAUX = REPO / "static" / "img" / "taux-apparent-dette.svg"

INSEE_URL = ("https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/"
             "010777616+010777608?startPeriod=1995-Q1")
EURO = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
EURO_D41_MIO = EURO + ("gov_10a_main?format=JSON&geo=FR&na_item=D41PAY"
                       "&sector=S13&unit=MIO_EUR&lang=en")
EURO_D41_PIB = EURO + ("gov_10a_main?format=JSON&geo=FR&na_item=D41PAY"
                       "&sector=S13&unit=PC_GDP&lang=en")
EURO_COFOG_MIO = EURO + ("gov_10a_exp?format=JSON&geo=FR&na_item=TE&sector=S13"
                         "&unit=MIO_EUR&cofog99=GF03&cofog99=GF0303"
                         "&cofog99=GF07&cofog99=GF09&lang=en")
EURO_COFOG_PIB = EURO + ("gov_10a_exp?format=JSON&geo=FR&na_item=TE&sector=S13"
                         "&unit=PC_GDP&cofog99=GF03&cofog99=GF0303"
                         "&cofog99=GF07&cofog99=GF09&lang=en")
EURO_TR = EURO + ("gov_10a_main?format=JSON&geo=FR&na_item=TR"
                  "&sector=S13&unit=MIO_EUR&lang=en")

RE_QUARTER = re.compile(r"^\d{4}-Q[1-4]$")
RE_YEAR = re.compile(r"^\d{4}$")

FAILURES: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)
    print("GARDE EN ECHEC: " + msg)


def fetch(url: str) -> bytes:
    """urllib d'abord ; repli curl si le magasin de certificats local est
    perime (vu sous Windows). Jamais de verification desactivee."""
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return r.read()
    except (urllib.error.URLError, ssl.SSLError) as e:
        print("info: urllib KO (" + type(e).__name__ + "), repli curl")
        p = subprocess.run(["curl", "-sS", "--fail", "--max-time", "60", url],
                           capture_output=True)
        if p.returncode != 0:
            raise RuntimeError("curl a echoue: "
                               + p.stderr.decode("ascii", "replace")[:200])
        return p.stdout


def parse_insee(xml_bytes: bytes) -> dict[str, dict[str, float]]:
    root = ET.fromstring(xml_bytes)
    out: dict[str, dict[str, float]] = {}
    for series in root.iter():
        if not series.tag.endswith("Series"):
            continue
        idbank = series.get("IDBANK")
        if not idbank:
            continue
        obs = {}
        for o in series:
            if o.tag.endswith("Obs"):
                per, val = o.get("TIME_PERIOD"), o.get("OBS_VALUE")
                if per and val and RE_QUARTER.match(per):
                    obs[per] = float(val)
        if obs:
            out[idbank] = obs
    return out


def parse_eurostat(raw: bytes, split_dim: str) -> dict[str, dict[str, float]]:
    d = json.loads(raw.decode("utf-8"))
    if "error" in d:
        raise RuntimeError("Eurostat: " + str(d["error"])[:200])
    dims, sizes = d["id"], d["size"]
    cats = {dim: {v: k for k, v in
                  d["dimension"][dim]["category"]["index"].items()}
            for dim in dims}
    series: dict[str, dict[str, float]] = {}
    for flat, val in d["value"].items():
        rem, coord = int(flat), {}
        for dim, size in zip(reversed(dims), reversed(sizes)):
            coord[dim] = rem % size
            rem //= size
        year = cats["time"][coord["time"]]
        if not RE_YEAR.match(year):
            continue
        key = cats[split_dim][coord[split_dim]] if split_dim in coord else "all"
        series.setdefault(key, {})[year] = float(val)
    return series


# ---------------------------------------------------------------- formatage
def fr(v: float, dec: int = 1) -> str:
    """3536.1 -> '3 536,1' (espace insecable U+00A0 pour les milliers)."""
    s = ("{:,." + str(dec) + "f}").format(v)
    return s.replace(",", " ").replace(".", ",")


def fr_quarter(p: str) -> str:
    y, q = p.split("-Q")
    return "T" + q + " " + y


# ------------------------------------------------------------------- gardes
def in_band(name: str, value: float, lo: float, hi: float) -> None:
    if not (lo <= value <= hi):
        fail("%s = %s hors bande [%s, %s]" % (name, value, lo, hi))


def check_quarterly(name: str, obs: dict[str, float], lo: float, hi: float,
                    max_step_pct: float = 12.0) -> None:
    if len(obs) < 100:
        fail("%s: %d observations (< 100 attendues)" % (name, len(obs)))
        return
    prev = None
    for p in sorted(obs):
        in_band("%s[%s]" % (name, p), obs[p], lo, hi)
        if prev is not None and prev > 0:
            step = abs(obs[p] - prev) / prev * 100.0
            if step > max_step_pct:
                fail("%s: saut %s de %.1f%% (> %.0f%%)"
                     % (name, p, step, max_step_pct))
        prev = obs[p]


def check_annual(name: str, obs: dict[str, float], lo: float, hi: float,
                 min_obs: int = 25) -> None:
    if len(obs) < min_obs:
        fail("%s: %d observations (< %d attendues)" % (name, len(obs), min_obs))
        return
    for y in sorted(obs):
        in_band("%s[%s]" % (name, y), obs[y], lo, hi)


def check_consolidated_anchors(dette_mdeur, dette_pib, d41_mio) -> None:
    """Ancres UNIQUEMENT sur des valeurs anciennes consolidees, en bandes."""
    anchors = [
        ("dette_mdeur[1995-Q4]", dette_mdeur.get("1995-Q4"), 600, 800),
        ("dette_pib[1995-Q4]", dette_pib.get("1995-Q4"), 50, 65),
        ("dette_mdeur[2020-Q4]", dette_mdeur.get("2020-Q4"), 2500, 2800),
        ("dette_pib[2020-Q4]", dette_pib.get("2020-Q4"), 108, 122),
        ("interets_mio[2010]", d41_mio.get("2010"), 38000, 58000),
    ]
    for name, v, lo, hi in anchors:
        if v is None:
            fail(name + ": ancre absente de la serie")
        else:
            in_band("ancre " + name, v, lo, hi)


def check_delta_vs_committed(payload_prev: dict | None, dette_mdeur, dette_pib,
                             d41_mdeur: dict[str, float]) -> None:
    """Le recent est garde par continuite avec ce qui est deja publie :
    sur la derniere periode DEJA committee, la nouvelle valeur ne peut
    s'ecarter que d'une revision plausible."""
    if not payload_prev:
        print("info: pas de fichier precedent -- delta vs committe saute")
        return
    try:
        t = payload_prev["dette_trimestrielle"]
        old_p = t["derniere_periode"]
        old_mdeur = float(t["series"]["mdeur"][old_p])
        old_pib = float(t["series"]["pct_pib"][old_p])
        i = payload_prev["interets_annuels"]
        old_y = i["derniere_periode"]
        old_int = float(i["series"]["mdeur"][old_y])
    except (KeyError, TypeError, ValueError):
        print("info: fichier precedent sans les cles attendues -- delta saute")
        return
    if old_p in dette_mdeur:
        if old_mdeur > 0 and abs(dette_mdeur[old_p] - old_mdeur) / old_mdeur > 0.05:
            fail("delta committe: dette[%s] %s -> %s (> 5%%)"
                 % (old_p, old_mdeur, dette_mdeur[old_p]))
    else:
        fail("delta committe: periode %s disparue de la serie INSEE" % old_p)
    if old_p in dette_pib and abs(dette_pib[old_p] - old_pib) > 3.0:
        fail("delta committe: ratio[%s] %s -> %s (> 3 points)"
             % (old_p, old_pib, dette_pib[old_p]))
    if old_y in d41_mdeur:
        if old_int > 0 and abs(d41_mdeur[old_y] - old_int) / old_int > 0.15:
            fail("delta committe: interets[%s] %s -> %s (> 15%%)"
                 % (old_y, old_int, d41_mdeur[old_y]))
    else:
        fail("delta committe: annee %s disparue de la serie Eurostat" % old_y)
    new_last = max(dette_mdeur) if dette_mdeur else ""
    if str(new_last) < str(old_p):
        fail("regression de periode: %s < %s" % (new_last, old_p))


# ---------------------------------------------------------------------- SVG
SVG_W, SVG_H = 720, 480
MARG_L, MARG_R = 46, 14
COL_DETTE = "#2a78d6"   # palette dataviz slot 1 (validee)
COL_INTER = "#eb6834"   # slot 2
INK2, MUTED, GRID, AXIS = "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"


def _x(t: float, t0: float, t1: float) -> float:
    return MARG_L + (t - t0) / (t1 - t0) * (SVG_W - MARG_L - MARG_R)


def _line_path(pts: list[tuple[float, float]]) -> str:
    return "M" + " L".join("%.1f,%.1f" % (x, y) for x, y in pts)


def build_svg(dette_pib: dict[str, float], d41_pib: dict[str, float]) -> str:
    t0, t1 = 1994.8, 2026.9
    # panneau A (dette, % PIB) : y 34..208 pour 0..125
    ay0, ay1, amax = 208.0, 34.0, 125.0
    # panneau B (interets, % PIB) : y 300..452 pour 0..4
    by0, by1, bmax = 452.0, 300.0, 4.0

    def ay(v): return ay0 - v / amax * (ay0 - ay1)
    def by(v): return by0 - v / bmax * (by0 - by1)

    qpts = []
    for p in sorted(dette_pib):
        y, q = int(p[:4]), int(p[-1])
        qpts.append((_x(y + (q - 1) * 0.25 + 0.125, t0, t1), ay(dette_pib[p])))
    ypts = []
    for yr in sorted(d41_pib):
        ypts.append((_x(int(yr) + 0.5, t0, t1), by(d41_pib[yr])))

    first_q, last_q = min(dette_pib), max(dette_pib)
    first_y, last_y = min(d41_pib), max(d41_pib)
    trough_y = min(d41_pib, key=lambda k: d41_pib[k])
    x2022 = _x(2022.0, t0, t1)

    e = []
    e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
             'role="img" aria-labelledby="cz-t cz-d" font-family="%s">'
             % (SVG_W, SVG_H, FONT))
    e.append('<title id="cz-t">Le ciseau de la dette publique française : '
             'encours et charge d\'intérêts, 1995-2026</title>')
    e.append('<desc id="cz-d">Deux courbes en pourcentage du PIB. En haut, la '
             'dette publique passe de %s %% du PIB en %s à %s %% au %s. En bas, '
             'les intérêts versés par les administrations publiques passent de '
             '%s %% du PIB en %s à un creux de %s %% en %s, puis remontent à '
             '%s %% en %s.</desc>'
             % (str(dette_pib[first_q]).replace(".", ","), fr_quarter(first_q),
                str(dette_pib[last_q]).replace(".", ","), fr_quarter(last_q),
                str(d41_pib[first_y]).replace(".", ","), first_y,
                str(d41_pib[trough_y]).replace(".", ","), trough_y,
                str(d41_pib[last_y]).replace(".", ","), last_y))

    # titres de panneaux (encre secondaire, jamais la couleur de serie)
    e.append('<text x="%d" y="22" font-size="13" fill="%s">Dette publique des '
             'administrations, en %% du PIB (INSEE, trimestriel)</text>'
             % (MARG_L, INK2))
    e.append('<text x="%d" y="288" font-size="13" fill="%s">Intérêts versés par '
             'les administrations, en %% du PIB (Eurostat, annuel)</text>'
             % (MARG_L, INK2))

    # grilles + libelles d'axe Y
    for v in (0, 40, 80, 120):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                 'stroke-width="1"/>' % (MARG_L, ay(v), SVG_W - MARG_R, ay(v),
                                         GRID if v else AXIS))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s" '
                 'text-anchor="end">%d</text>'
                 % (MARG_L - 6, ay(v) + 4, MUTED, v))
    for v in (0, 1, 2, 3, 4):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                 'stroke-width="1"/>' % (MARG_L, by(v), SVG_W - MARG_R, by(v),
                                         GRID if v else AXIS))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s" '
                 'text-anchor="end">%d</text>'
                 % (MARG_L - 6, by(v) + 4, MUTED, v))

    # annees sur l'axe partage (sous le panneau B)
    for yr in range(1995, 2027, 5):
        e.append('<text x="%.1f" y="472" font-size="11" fill="%s" '
                 'text-anchor="middle">%d</text>'
                 % (_x(yr + 0.5, t0, t1), MUTED, yr))

    # repere du retournement 2022, traversant les deux panneaux
    e.append('<line x1="%.1f" y1="30" x2="%.1f" y2="455" stroke="%s" '
             'stroke-width="1" stroke-dasharray="3 4"/>' % (x2022, x2022, AXIS))
    e.append('<text x="%.1f" y="243" font-size="11" fill="%s" '
             'text-anchor="middle">2022 : le retournement</text>'
             % (x2022, INK2))

    # series (2 px, bouts ronds)
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round"/>'
             % (_line_path(qpts), COL_DETTE))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round"/>'
             % (_line_path(ypts), COL_INTER))

    # etiquettes directes selectives : points d'arrivee + creux
    def dot_label(x, y, color, txt, anchor="start", dx=7, dy=4):
        e.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>'
                 % (x, y, color))
        e.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s" '
                 'text-anchor="%s">%s</text>'
                 % (x + dx, y + dy, INK2, anchor, txt))

    lx, ly = qpts[-1]
    dot_label(lx, ly, COL_DETTE,
              str(dette_pib[last_q]).replace(".", ",") + " %",
              anchor="end", dx=-8, dy=-8)
    fx, fy = qpts[0]
    dot_label(fx, fy, COL_DETTE,
              str(dette_pib[first_q]).replace(".", ",") + " %", dy=-8)
    ix, iy = ypts[-1]
    dot_label(ix, iy, COL_INTER,
              str(d41_pib[last_y]).replace(".", ",") + " %",
              anchor="end", dx=-8, dy=-9)
    jx, jy = ypts[0]
    dot_label(jx, jy, COL_INTER,
              str(d41_pib[first_y]).replace(".", ",") + " %", dy=-8)
    tx = _x(int(trough_y) + 0.5, t0, t1)
    ty = by(d41_pib[trough_y])
    dot_label(tx, ty, COL_INTER,
              str(d41_pib[trough_y]).replace(".", ",") + " %% en "
              .replace("%%", "%") + trough_y, anchor="middle", dx=0, dy=18)

    e.append("</svg>")
    return "\n".join(e) + "\n"


def build_svg_taux(taux: dict[str, float]) -> str:
    """Courbe du TAUX APPARENT -- le chainon causal que la page raconte sans le
    montrer. Serie UNIQUE : donc pas de legende (le titre nomme la serie), et
    etiquetage direct des trois seuls points que la prose cite : depart, creux,
    arrivee. Le repere vertical est pose sur le creux MESURE, jamais sur une
    annee en dur -- une revision qui deplace le creux deplace le repere.
    Couleur = slot 2 de la palette, celle des interets dans l'autre figure :
    la couleur suit l'ENTITE (le cout de la dette), pas le rang de la serie.
    Pas de survol : l'actif est servi en <img> et vaut comme image citable ;
    exclusion declaree, les valeurs vivent dans la prose et dans le JSON public.
    """
    W, H = 720, 340
    ml, mr = 46, 14
    ay0, ay1, amax = 280.0, 46.0, 7.0
    years = sorted(int(y) for y in taux)
    t0, t1 = years[0] - 0.6, years[-1] + 0.6

    def x(v): return ml + (v - t0) / (t1 - t0) * (W - ml - mr)
    def y(v): return ay0 - v / amax * (ay0 - ay1)

    pts = [(x(yr), y(taux[str(yr)])) for yr in years]
    first, last = str(years[0]), str(years[-1])
    trough = min(taux, key=lambda k: taux[k])

    def num(v): return fr(v, 1)

    e = []
    e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
             'role="img" aria-labelledby="ta-t ta-d" font-family="%s">'
             % (W, H, FONT))
    e.append('<title id="ta-t">Le taux apparent de la dette publique '
             'française, %s-%s</title>' % (first, last))
    e.append('<desc id="ta-d">Une courbe, en pourcentage par an. Le coût moyen '
             'du stock de dette descend de %s %% en %s à %s %% en %s, son '
             'minimum sur la série, puis remonte à %s %% en %s. La baisse court '
             'sur près de vingt-cinq ans ; la remontée sur les dernières '
             'années.</desc>'
             % (num(taux[first]), first, num(taux[trough]), trough,
                num(taux[last]), last))
    e.append('<text x="%d" y="22" font-size="13" fill="%s">Taux apparent de la '
             'dette publique, en %% par an — le coût moyen du stock</text>'
             % (ml, INK2))

    for v in (0, 2, 4, 6):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                 'stroke-width="1"/>'
                 % (ml, y(v), W - mr, y(v), GRID if v else AXIS))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s" '
                 'text-anchor="end">%d</text>' % (ml - 6, y(v) + 4, MUTED, v))
    for yr in range(years[0] + 4, years[-1] + 1, 5):
        e.append('<text x="%.1f" y="305" font-size="11" fill="%s" '
                 'text-anchor="middle">%d</text>' % (x(yr), MUTED, yr))

    # Pas de verticale au creux : non etiquetee, elle serait indiscernable
    # d'une grille en pointilles (anti-pattern) et n'ajouterait rien -- le creux
    # est deja porte par son point et son libelle direct.
    xt = x(int(trough))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round"/>'
             % (_line_path(pts), COL_INTER))

    # etiquetage direct SELECTIF : jamais un nombre sur chaque point
    def dot(px, py, txt, anchor, dx, dy):
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>'
                 % (px, py, COL_INTER))
        e.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s" '
                 'text-anchor="%s">%s</text>'
                 % (px + dx, py + dy, INK2, anchor, txt))

    dot(pts[0][0], pts[0][1], num(taux[first]) + " % en " + first, "start", 9, 4)
    dot(pts[-1][0], pts[-1][1], num(taux[last]) + " % en " + last, "end", -9, -10)
    dot(xt, y(taux[trough]), num(taux[trough]) + " % en " + trough,
        "middle", 0, 22)
    e.append("</svg>")
    return "\n".join(e) + "\n"


# ------------------------------------------------------------------- sortie
def _hors_dates(payload: dict) -> str:
    """Empreinte du paquet PRIVEE de ses deux horodatages, pour repondre a la
    seule question qui decide d'une publication : un chiffre a-t-il bouge ?"""
    c = json.loads(json.dumps(payload))
    c.pop("releve_le", None)
    if isinstance(c.get("affichage"), dict):
        c["affichage"].pop("releve_le", None)
    return json.dumps(c, ensure_ascii=False, sort_keys=True)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def main() -> int:
    args = sys.argv[1:]
    check_only = "--check" in args
    legacy_path = None
    if "--legacy" in args:
        legacy_path = Path(args[args.index("--legacy") + 1])

    print("fetch INSEE SDMX ...")
    insee = parse_insee(fetch(INSEE_URL))
    print("fetch Eurostat (5 requetes) ...")
    d41_mio = parse_eurostat(fetch(EURO_D41_MIO), "sector").get("S13", {})
    d41_pib = parse_eurostat(fetch(EURO_D41_PIB), "sector").get("S13", {})
    cofog_mio = parse_eurostat(fetch(EURO_COFOG_MIO), "cofog99")
    cofog_pib = parse_eurostat(fetch(EURO_COFOG_PIB), "cofog99")
    tr_mdeur = {y: round(v / 1000.0, 1) for y, v in
                parse_eurostat(fetch(EURO_TR), "sector").get("S13", {}).items()}

    dette_mdeur = insee.get("010777616", {})
    dette_pib = insee.get("010777608", {})
    d41_mdeur = {y: round(v / 1000.0, 1) for y, v in d41_mio.items()}

    payload_prev = None
    if OUT_JSON.exists():
        try:
            payload_prev = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            print("info: fichier precedent illisible")

    # -- gardes ------------------------------------------------------------
    check_quarterly("dette_mdeur", dette_mdeur, 600, 10000)
    check_quarterly("dette_pib", dette_pib, 40, 200)
    check_annual("interets_mdeur", d41_mdeur, 15, 200)
    check_annual("interets_pib", d41_pib, 0.5, 6.0)
    bands_pib = {"GF03": (1.0, 3.0), "GF0303": (0.1, 0.8),
                 "GF07": (5.0, 13.0), "GF09": (3.5, 8.0)}
    for code, (lo, hi) in bands_pib.items():
        check_annual("cofog_pib." + code, cofog_pib.get(code, {}), lo, hi)
    check_annual("recettes_mdeur", tr_mdeur, 300, 3000)
    check_consolidated_anchors(dette_mdeur, dette_pib, d41_mio)
    check_delta_vs_committed(payload_prev, dette_mdeur, dette_pib, d41_mdeur)

    lastq = max(dette_mdeur) if dette_mdeur else None
    if lastq and lastq not in dette_pib:
        fail("periodes INSEE desalignees: %s absent du ratio" % lastq)
    if lastq and lastq in dette_pib and dette_pib[lastq] > 0:
        in_band("PIB implicite " + lastq,
                dette_mdeur[lastq] / (dette_pib[lastq] / 100.0), 1000, 5000)

    if FAILURES:
        print("ECHEC: %d garde(s) -- AUCUNE ecriture, fichiers precedents "
              "conserves." % len(FAILURES))
        return 1

    # -- derives (un seul endroit de calcul) --------------------------------
    last_y = max(d41_mdeur)
    trough_y = min(d41_pib, key=lambda k: d41_pib[k])
    peak_q = max(dette_pib, key=lambda k: dette_pib[k])
    equiv_y = str(min(int(last_y), int(max(cofog_mio.get("GF0303", {"0": 0})))))
    cof24 = {c: round(cofog_mio[c][equiv_y] / 1000.0, 1)
             for c in ("GF0303", "GF03", "GF07", "GF09") if equiv_y in cofog_mio.get(c, {})}
    int_equiv = d41_mdeur.get(equiv_y)
    if not (int_equiv and len(cof24) == 4):
        print("ECHEC: millesime commun %s incomplet -- rien n'est ecrit."
              % equiv_y)
        return 1
    hausse_pct = round((d41_mdeur[last_y] - d41_mdeur[trough_y])
                       / d41_mdeur[trough_y] * 100.0)
    # controle pre-Covid : 2019 est une reference historique FIXE (derniere
    # annee avant la rupture sanitaire), pas un point mobile
    hausse_2019_pct = None
    if "2019" in d41_mdeur and d41_mdeur["2019"] > 0:
        hausse_2019_pct = round((d41_mdeur[last_y] - d41_mdeur["2019"])
                                / d41_mdeur["2019"] * 100.0)
    if hausse_2019_pct is None:
        print("ECHEC: reference 2019 absente de la serie D41 -- rien n'est ecrit.")
        return 1

    # taux apparent = interets de l'annee N / encours au T4 de N-1
    # (cout moyen du stock, PAS le taux d'emission courant)
    taux_apparent = {}
    for y in sorted(d41_mdeur):
        prev_q4 = "%d-Q4" % (int(y) - 1)
        if prev_q4 in dette_mdeur and dette_mdeur[prev_q4] > 0:
            taux_apparent[y] = round(d41_mdeur[y] / dette_mdeur[prev_q4] * 100.0, 2)
    if len(taux_apparent) < 20:
        print("ECHEC: serie taux apparent incomplete (%d obs) -- rien n'est ecrit."
              % len(taux_apparent))
        return 1
    ta_first = min(taux_apparent)
    ta_trough = min(taux_apparent, key=lambda k: taux_apparent[k])
    ta_last = max(taux_apparent)
    for y, v in taux_apparent.items():
        in_band("taux_apparent[%s]" % y, v, 0.5, 12.0)

    # interets / recettes publiques (capacite d'absorption budgetaire)
    tr_last = max(set(tr_mdeur) & set(d41_mdeur)) if tr_mdeur else None
    if not tr_last or tr_mdeur[tr_last] <= 0:
        print("ECHEC: recettes publiques indisponibles -- rien n'est ecrit.")
        return 1
    int_sur_recettes = round(d41_mdeur[tr_last] / tr_mdeur[tr_last] * 100.0, 1)
    in_band("interets/recettes " + tr_last, int_sur_recettes, 1.0, 15.0)
    if FAILURES:
        print("ECHEC: %d garde(s) sur les derives -- AUCUNE ecriture." % len(FAILURES))
        return 1

    # parametres du compteur anime de la page (extrapolation depuis l'ancre
    # officielle -- le JS de la page ne contient AUCUN nombre en dur)
    q_sorted = sorted(dette_mdeur)
    if len(q_sorted) < 5:
        print("ECHEC: moins de 5 trimestres, croissance annuelle incalculable.")
        return 1
    prev_year_q = q_sorted[-5]
    croissance = round((dette_mdeur[lastq] / dette_mdeur[prev_year_q] - 1) * 100.0, 1)
    in_band("croissance annuelle du stock", croissance, 0.0, 15.0)
    ly, lq = int(lastq[:4]), int(lastq[-1])
    fin_mois = lq * 3
    fin_jour = {3: 31, 6: 30, 9: 30, 12: 31}[fin_mois]
    fin_periode_iso = "%d-%02d-%02d" % (ly, fin_mois, fin_jour)
    if FAILURES:
        print("ECHEC: %d garde(s) sur le bloc live -- AUCUNE ecriture." % len(FAILURES))
        return 1

    now_fr = datetime.now(timezone.utc).strftime("%d/%m/%Y")
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    affichage = {
        "dette_periode": fr_quarter(lastq),
        "dette_mdeur": fr(dette_mdeur[lastq]),
        "dette_pct_pib": fr(dette_pib[lastq]),
        "dette_pic_periode": fr_quarter(peak_q),
        "dette_pic_pct_pib": fr(dette_pib[peak_q]),
        "dette_1995_pct_pib": fr(dette_pib[min(dette_pib)]),
        "interets_annee": last_y,
        "interets_mdeur": fr(d41_mdeur[last_y]),
        "interets_pct_pib": fr(d41_pib[last_y]),
        "interets_1995_pct_pib": fr(d41_pib[min(d41_pib)]),
        "interets_creux_annee": trough_y,
        "interets_creux_mdeur": fr(d41_mdeur[trough_y]),
        "interets_creux_pct_pib": fr(d41_pib[trough_y]),
        "interets_hausse_pct": str(hausse_pct),
        "interets_2019_mdeur": fr(d41_mdeur["2019"]),
        "interets_hausse_2019_pct": str(hausse_2019_pct),
        "taux_apparent_premier_annee": ta_first,
        "taux_apparent_premier": fr(taux_apparent[ta_first]),
        "taux_apparent_creux_annee": ta_trough,
        "taux_apparent_creux": fr(taux_apparent[ta_trough]),
        "taux_apparent_dernier_annee": ta_last,
        "taux_apparent_dernier": fr(taux_apparent[ta_last]),
        "recettes_annee": tr_last,
        "recettes_mdeur": fr(tr_mdeur[tr_last]),
        "interets_sur_recettes_pct": fr(int_sur_recettes),
        "equiv_annee": equiv_y,
        "interets_equiv_mdeur": fr(int_equiv),
        "justice_mdeur": fr(cof24["GF0303"]),
        "ordre_mdeur": fr(cof24["GF03"]),
        "sante_mdeur": fr(cof24["GF07"]),
        "education_mdeur": fr(cof24["GF09"]),
        "ratio_interets_justice": fr(round(int_equiv / cof24["GF0303"], 1)),
        "pct_interets_education": str(round(int_equiv / cof24["GF09"] * 100)),
        "pct_interets_sante": str(round(int_equiv / cof24["GF07"] * 100)),
        "croissance_annuelle_pct": fr(croissance),
        "releve_le": now_fr,
    }

    live = {
        "_usage": ("Paramètres du compteur animé (extrapolation mécanique) — "
                   "consommés par le partial dette-chiffres via data-attributes."),
        "mdeur": dette_mdeur[lastq],
        "periode": fr_quarter(lastq),
        "fin_periode_iso": fin_periode_iso,
        "croissance_annuelle_pct": croissance,
    }

    payload = {
        "_avertissement": ("Fichier GÉNÉRÉ par scripts/update_dette_insee.py "
                           "— ne pas éditer à la main."),
        # Le fichier voyage seul : qui le telecharge n'a pas la page sous les
        # yeux. La licence doit donc etre DANS le paquet, pas seulement dans
        # le JSON-LD et la prose (meme surface, trois portes d'entree).
        "_licence": ("Compilation sous licence CC BY 4.0 "
                     "(https://creativecommons.org/licenses/by/4.0/) : "
                     "réutilisation libre, y compris commerciale, à condition "
                     "de citer Stéphane Lalut, "
                     "https://stephane-lalut.com/cout-de-la-dette-publique/. "
                     "La licence porte sur la COMPILATION (assemblage des "
                     "séries, grandeurs dérivées, mise en cohérence) ; les "
                     "séries brutes restent celles de l'INSEE et d'Eurostat, "
                     "sous leurs propres conditions."),
        "releve_le": now_iso,
        "affichage": affichage,
        "live": live,
        "dette_trimestrielle": {
            "source": "INSEE, dette de Maastricht des administrations publiques",
            "idbanks": {"mdeur": "010777616", "pct_pib": "010777608"},
            "unite": {"mdeur": "milliards d'euros courants",
                      "pct_pib": "% du PIB"},
            "derniere_periode": lastq,
            "series": {
                "mdeur": {p: dette_mdeur[p] for p in sorted(dette_mdeur)},
                "pct_pib": {p: dette_pib[p] for p in sorted(dette_pib)},
            },
        },
        "interets_annuels": {
            "source": ("Eurostat, gov_10a_main — intérêts versés (D41PAY) "
                       "par les administrations publiques (S13), France"),
            "dataset": "gov_10a_main",
            "unite": {"mdeur": "milliards d'euros courants",
                      "pct_pib": "% du PIB"},
            "derniere_periode": last_y,
            "series": {
                "mdeur": {y: d41_mdeur[y] for y in sorted(d41_mdeur)},
                "pct_pib": {y: d41_pib[y] for y in sorted(d41_pib)},
                "taux_apparent_pct": dict(sorted(taux_apparent.items())),
            },
            "taux_apparent_definition": ("intérêts versés l'année N / encours de "
                                         "dette au T4 de l'année N-1 — coût moyen "
                                         "du stock, pas le taux d'émission courant"),
        },
        "recettes_annuelles": {
            "source": ("Eurostat, gov_10a_main — recettes totales (TR) des "
                       "administrations publiques (S13), France"),
            "dataset": "gov_10a_main",
            "unite": {"mdeur": "milliards d'euros courants"},
            "derniere_periode": tr_last,
            "series": {"mdeur": {y: tr_mdeur[y] for y in sorted(tr_mdeur)}},
        },
        "depenses_fonction_annuelles": {
            "source": ("Eurostat, gov_10a_exp — dépenses totales (TE) des "
                       "administrations publiques (S13) par fonction COFOG, "
                       "France"),
            "dataset": "gov_10a_exp",
            "fonctions": {"GF0303": "justice (tribunaux)",
                          "GF03": "ordre et sécurité publics (ensemble)",
                          "GF07": "santé", "GF09": "enseignement"},
            "unite": {"mdeur": "milliards d'euros courants",
                      "pct_pib": "% du PIB"},
            "derniere_periode": equiv_y,
            "series": {
                code: {
                    "mdeur": {y: round(v / 1000.0, 1)
                              for y, v in sorted(cofog_mio.get(code, {}).items())},
                    "pct_pib": dict(sorted(cofog_pib.get(code, {}).items())),
                } for code in ("GF0303", "GF03", "GF07", "GF09")
            },
        },
    }

    # -- pas de reecriture pour la seule date -------------------------------
    # Mesure du 2026-08-16 : a donnees identiques, le paquet differait quand
    # meme -- par les deux champs "releve_le". Donc `git diff --quiet` du
    # workflow etait TOUJOURS faux, et dette-insee.yml ouvrait une PR chaque
    # mois pour 4 lignes de date : 12 gestes/an la ou il en annonce ~4.
    # L'ecart n'aurait rien casse ; il aurait use le merge humain, qui est la
    # seule barriere de publication (clause de decroissance du workflow :
    # "PRs laissees sans merge plus d'un trimestre => reexamen").
    # Donc : quand rien n'a change hors dates, on conserve les dates publiees
    # et la page reste bit pour bit identique. "releve_le" designe des lors le
    # dernier releve AYANT MODIFIE un chiffre -- ce que la page dit en toutes
    # lettres. Aucun champ nouveau : un second horodatage "verifie_le" exigerait
    # un commit mensuel pour rester vrai, soit le defaut qu'on corrige.
    inchange = payload_prev is not None and _hors_dates(payload) == _hors_dates(payload_prev)
    if inchange:
        payload["releve_le"] = payload_prev.get("releve_le", payload["releve_le"])
        payload["affichage"]["releve_le"] = (
            payload_prev.get("affichage", {}).get("releve_le",
                                                 payload["affichage"]["releve_le"]))

    if check_only:
        print("OK (--check): gardes passees, rien n'est ecrit. Dette %s = %s "
              "Md EUR / %s %% PIB ; interets %s = %s Md EUR%s"
              % (lastq, dette_mdeur[lastq], dette_pib[lastq],
                 last_y, d41_mdeur[last_y],
                 " -- INCHANGE depuis le releve du " + str(payload["releve_le"])
                 if inchange else " -- DONNEES NOUVELLES"))
        return 0

    txt = json.dumps(payload, ensure_ascii=False, indent=1) + "\n"
    atomic_write(OUT_JSON, txt)
    atomic_write(OUT_ENDPOINT, txt)
    atomic_write(OUT_SVG, build_svg(dette_pib, d41_pib))
    atomic_write(OUT_SVG_TAUX, build_svg_taux(taux_apparent))
    print("OK: ecrits %s + endpoint + %s + %s%s"
          % (OUT_JSON.name, OUT_SVG.name, OUT_SVG_TAUX.name,
             " -- CONTENU INCHANGE (dates conservees, aucun diff attendu)"
             if inchange else " -- DONNEES NOUVELLES"))

    if legacy_path is not None:
        legacy = {
            "last_update": now_iso + "T00:00:00",
            "source": "INSEE, dette de Maastricht (idbanks 010777616/010777608)",
            "data": [{"period": p, "dette_pib": dette_pib.get(p),
                      "dette_montant": dette_mdeur[p]}
                     for p in sorted(dette_mdeur) if p in dette_pib],
        }
        atomic_write(legacy_path,
                     json.dumps(legacy, ensure_ascii=False, indent=1) + "\n")
        print("OK: export legacy compagnon -> " + str(legacy_path))

    print("Dette %s = %s Md EUR / %s %% PIB ; interets %s = %s Md EUR (%s %% "
          "PIB) ; equivalences %s"
          % (lastq, dette_mdeur[lastq], dette_pib[lastq], last_y,
             d41_mdeur[last_y], d41_pib[last_y], equiv_y))
    return 0


if __name__ == "__main__":
    sys.exit(main())
