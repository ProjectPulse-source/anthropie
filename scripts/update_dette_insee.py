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
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_JSON = REPO / "data" / "dette_officielle.json"
OUT_ENDPOINT = REPO / "static" / "dette_officielle.json"
# CSV (avis « Combien coûte », 30/09) : même contenu que le JSON publié, en format LONG — une valeur par ligne, avec
# son unité, sa période et sa source —, UTF-8 avec BOM pour qu'Excel lise les accents. Dérivé du payload, jamais
# recalculé : il ne peut pas dire autre chose que le JSON.
OUT_CSV = REPO / "static" / "dette_officielle.csv"
OUT_SVG = REPO / "static" / "img" / "ciseau-dette-interets.svg"
OUT_SVG_TAUX = REPO / "static" / "img" / "taux-apparent-dette.svg"
OUT_SVG_EN = REPO / "static" / "img" / "ciseau-dette-interets-en.svg"
OUT_SVG_TAUX_EN = REPO / "static" / "img" / "taux-apparent-dette-en.svg"
OUT_SVG_LONGUE = REPO / "static" / "img" / "dette-longue.svg"
OUT_SVG_LONGUE_EN = REPO / "static" / "img" / "dette-longue-en.svg"
OUT_FIGURES = REPO / "data" / "figures_dette.json"
OUT_SVG_MARCHE = REPO / "static" / "img" / "taux-marche-apparent.svg"
OUT_SVG_MARCHE_EN = REPO / "static" / "img" / "taux-marche-apparent-en.svg"
OUT_SVG_MASSES = REPO / "static" / "img" / "masses-comparees.svg"
OUT_SVG_MASSES_EN = REPO / "static" / "img" / "masses-comparees-en.svg"
OUT_SVG_CHARGE = REPO / "static" / "img" / "charge-interets-mdeur.svg"
OUT_SVG_CHARGE_EN = REPO / "static" / "img" / "charge-interets-mdeur-en.svg"
TRAJECTOIRE = REPO / "data" / "trajectoire_plf2026.json"


def lire_trajectoire() -> dict:
    """Serie PREVISIONNELLE, saisie a la main apres lecture a la source.

    Absente ou illisible : la figure se dessine sans prolongement, elle ne
    s'arrete pas. Une prevision manquante ne doit pas suspendre une observation.
    """
    if not TRAJECTOIRE.is_file():
        return {}
    try:
        t = json.loads(TRAJECTOIRE.read_text(encoding="utf-8"))
        d = {int(a): float(v) for a, v in t["dette_pct_pib"].items()
             if not a.startswith("_")}
        return {"dette": d, "source": t["source"]["publication"]} if d else {}
    except Exception as exc:                       # noqa: BLE001
        print("trajectoire ignoree (%s)" % exc)
        return {}
# Segment 1978-1995 que le flux ne couvre pas : comptes nationaux clos,
# donc figes ici plutot que rapatries d'un .xlsx dont l'URL change a
# chaque millesime. L'annee 1995 y est en DOUBLE avec la serie
# trimestrielle : c'est le temoin qui rend le raccord verifiable.
HIST_JSON = REPO / "data" / "dette_historique_1978_1995.json"

INSEE_URL = ("https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/"
             "010777616+010777608?startPeriod=1995-Q1")
EURO = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
EURO_D41_MIO = EURO + ("gov_10a_main?format=JSON&geo=FR&na_item=D41PAY"
                       "&sector=S13&unit=MIO_EUR&lang=en")
EURO_D41_PIB = EURO + ("gov_10a_main?format=JSON&geo=FR&na_item=D41PAY"
                       "&sector=S13&unit=PC_GDP&lang=en")
# Les postes de NIVEAU II de la sante et de l'enseignement servent la
# decomposition affichee sous les etiquettes des masses comparees : le lecteur
# qui lit « Sante 261 » ne sait pas ce qu'il y a derriere, et « Enseignement 149 »
# ne signifie pas 149 Md EUR de professeurs. Ils sont DERIVES de la meme requete
# que les totaux -- jamais recopies a la main, sinon ils se figent au millesime
# du jour ou on les a lus (regle de surface du depot : toute valeur derivable se
# derive). Le reste de chaque fonction se calcule par soustraction, ce qui ferme
# la somme par construction.  (2026-09-29)
EURO_COFOG_MIO = EURO + ("gov_10a_exp?format=JSON&geo=FR&na_item=TE&sector=S13"
                         "&unit=MIO_EUR&cofog99=GF03&cofog99=GF0303"
                         "&cofog99=GF07&cofog99=GF09"
                         "&cofog99=GF0701&cofog99=GF0702&cofog99=GF0703"
                         "&cofog99=GF0901&cofog99=GF0902&cofog99=GF0904"
                         "&cofog99=GF0906&lang=en")

# Postes affiches, dans l'ordre de lecture, et leur part ADMISSIBLE du total de
# leur fonction. Bornes larges : elles ne pretendent pas predire la structure,
# elles arretent une inversion de code ou un poste qui deviendrait aberrant.
POSTES_COFOG = {
    "GF07": (("GF0703", 0.30, 0.55), ("GF0702", 0.25, 0.45), ("GF0701", 0.10, 0.30)),
    "GF09": (("GF0902", 0.30, 0.55), ("GF0901", 0.20, 0.40),
             ("GF0904", 0.05, 0.20), ("GF0906", 0.05, 0.25)),
}
EURO_COFOG_PIB = EURO + ("gov_10a_exp?format=JSON&geo=FR&na_item=TE&sector=S13"
                         "&unit=PC_GDP&cofog99=GF03&cofog99=GF0303"
                         "&cofog99=GF07&cofog99=GF09&lang=en")
# Taux a 10 ans de reference (critere de convergence de Maastricht), annuel.
# Serie ACCESSOIRE : si elle manque, la figure est conservee et la mise a jour
# des donnees passe quand meme -- jamais l'essentiel suspendu a l'accessoire.
EURO_LT = EURO + "irt_lt_mcby_a?format=JSON&geo=FR&lang=en"
EURO_TR = EURO + ("gov_10a_main?format=JSON&geo=FR&na_item=TR"
                  "&sector=S13&unit=MIO_EUR&lang=en")

RE_QUARTER = re.compile(r"^\d{4}-Q[1-4]$")
RE_YEAR = re.compile(r"^\d{4}$")

FAILURES: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)
    print("GARDE EN ECHEC: " + msg)


def fetch_once(url: str) -> bytes:
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


def fetch(url: str, essais: int = 3) -> bytes:
    """fetch_once, avec reprise espacee sur echec transitoire.

    Une indisponibilite de quelques secondes chez INSEE ou Eurostat n'est pas
    une donnee manquante : sans reprise elle reporterait la publication au
    passage suivant et ouvrirait une issue pour rien. Un defaut durable (404,
    serie retiree) epuise les essais et remonte tel quel -- la reprise ne
    transforme jamais une absence en silence."""
    for essai in range(1, essais + 1):
        try:
            return fetch_once(url)
        except Exception as e:
            if essai == essais:
                raise
            attente = essai * 5
            print("info: echec %d/%d (%s) -- nouvelle tentative dans %d s"
                  % (essai, essais, type(e).__name__, attente))
            time.sleep(attente)
    raise RuntimeError("fetch: sortie de boucle impossible")  # pragma: no cover


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


# -- locale anglaise -------------------------------------------------------
# Un seul endroit de CALCUL (plus bas), deux endroits de PRESENTATION. La page
# EN ne doit jamais afficher "3 536,1" ni "T1 2026" : ce serait FAUX, pas
# seulement inelegant. Hugo reste bete -- il choisit un bloc, il ne formate pas.
# NB : fr_quarter colle l'espace INSECABLE (U+00A0) entre le trimestre et
# l'annee ; l'anglais n'en a pas besoin, on met une espace ordinaire.
MOIS_EN = ("January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December")


def en(v: float, dec: int = 1) -> str:
    """3536.1 -> '3,536.1' : virgule de milliers, point decimal."""
    return ("{:,." + str(dec) + "f}").format(v)


def en_quarter(p: str) -> str:
    y, q = p.split("-Q")
    return "Q" + q + " " + y


def en_date(d: datetime) -> str:
    return "%d %s %d" % (d.day, MOIS_EN[d.month - 1], d.year)


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


# ------------------------------------------------------- serie longue 1978->
def charger_historique(dette_pib: dict[str, float]) -> dict:
    """Serie annuelle 1978 -> derniere annee pleine, et ce qu'on peut en dire.

    Le segment fige s'arrete en 1995, la serie vivante commence la : l'annee
    commune est comparee a chaque execution. Un ecart la-dessus signifierait
    que l'INSEE a revise l'ancien millesime ou que le fichier fige a derive --
    dans les deux cas, la courbe raconterait une marche fausse, et il vaut
    mieux ne rien publier."""
    try:
        brut = json.loads(HIST_JSON.read_text(encoding="utf-8"))
        fige = {int(a): float(v) for a, v in brut["pct_pib"].items()}
    except (OSError, ValueError, KeyError, TypeError) as e:
        fail("historique: %s illisible (%s)" % (HIST_JSON.name, type(e).__name__))
        return {}

    annuel = dict(fige)
    for p, v in dette_pib.items():
        if p.endswith("-Q4"):
            annuel[int(p[:4])] = v

    # -- temoin de raccord : 1995 existe des DEUX cotes -------------------
    commun = sorted(set(fige) & {int(p[:4]) for p in dette_pib if p.endswith("-Q4")})
    if not commun:
        fail("historique: aucune annee commune entre le segment fige et la "
             "serie trimestrielle -- raccord invérifiable")
    else:
        for a in commun:
            ecart = abs(fige[a] - dette_pib["%d-Q4" % a])
            if ecart > 0.5:
                fail("historique: raccord %d, fige %.1f vs T4 %.1f (ecart %.1f pt)"
                     % (a, fige[a], dette_pib["%d-Q4" % a], ecart))

    if len(annuel) < 45:
        fail("historique: %d annees seulement -- serie tronquee" % len(annuel))
    return annuel


def faits_historiques(annuel: dict, pct_courant: float) -> dict:
    """Ce que la serie autorise a ecrire, calcule et non recopie : une phrase
    du genre « jamais revenue a son niveau de dix ans plus tot » se verifie en
    dix secondes, et devient fausse toute seule si la serie bouge."""
    ans = sorted(annuel)
    baisses = [a for a in ans[1:] if annuel[a] < annuel[a - 1]]
    best = cur = 0
    for a in ans[1:]:
        cur = cur + 1 if annuel[a] < annuel[a - 1] else 0
        best = max(best, cur)
    seuils = {}
    for s in (30, 60, 80, 100):
        an = next((a for a in ans if annuel[a] >= s), None)
        if an is None:
            fail("historique: seuil %d %% jamais franchi -- serie suspecte" % s)
        seuils[s] = an
    retours = [a for a in ans if a - 10 in annuel and annuel[a] <= annuel[a - 10]]
    return {
        "annee_debut": ans[0],
        "pct_debut": annuel[ans[0]],
        "seuils": seuils,
        "annees_baisse": len(baisses),
        "annees_total": len(ans) - 1,
        "plus_longue_baisse": best,
        "multiple": pct_courant / annuel[ans[0]],
        "retour_10_ans": len(retours),
    }


# ---------------------------------------------------------------------- SVG
SVG_W, SVG_H = 720, 480
MARG_L, MARG_R = 46, 14
# Bleu PROFOND (pas 600 de la rampe) : direction « minimal newsroom » retenue par
# l'auteur le 28/09 sur maquettes. Le bleu marine du site echoue au controle de
# palette (chroma trop faible, il lit gris en donnee) ; ce pas-ci passe tous les
# controles, seul et avec l'orange et l'aqua.
COL_DETTE = "#184f95"   # palette dataviz, rampe bleue, pas 600 (validee)
COL_INTER = "#eb6834"   # slot 2
INK, INK2, MUTED, GRID, AXIS = "#0A0A0E", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
# Troisieme valeur de contexte des masses comparees. « Ordre et securite » etait
# trace en AXIS, c'est-a-dire dans la couleur de l'axe des abscisses : une SERIE
# partageait la teinte d'un element de structure, et la comparaison la plus
# frappante de la figure -- les interets repassent au-dessus d'elle -- se lisait
# comme du quadrillage. Un gris de plus, entre MUTED et AXIS, separe la donnee de
# la grille SANS introduire de seconde couleur de donnees : la hierarchie continue
# de tenir en noir et blanc, ce que la docstring de la figure protege.  (2026-09-29)
CTX3 = "#a5a39a"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
# Chiffres tabulaires : memes largeurs, donc les valeurs et les axes s'alignent
# d'une figure a l'autre (28/09).
TABNUM = 'font-variant-numeric="tabular-nums"' 
# Echelle typographique COMMUNE aux quatre figures (arbitrage du 28/09) : une
# seule definition, pour que les figures forment une famille et non une
# collection. Les tailles restent celles deja en place -- ce qui change, c'est
# qu'elles sont nommees en un seul endroit.
TY_TITRE, TY_AXE, TY_ANNOT, TY_VALEUR, TY_MINEUR = 13, 11, 12, 15, 11


def _x(t: float, t0: float, t1: float) -> float:
    return MARG_L + (t - t0) / (t1 - t0) * (SVG_W - MARG_L - MARG_R)


def _line_path(pts: list[tuple[float, float]]) -> str:
    return "M" + " L".join("%.1f,%.1f" % (x, y) for x, y in pts)


# ------------------------------------------------------------- CARTOUCHE
# Une figure REPRISE voyage sans sa page : le lecteur qui la colle dans un
# diaporama emporte la courbe et laisse sur place la source, le millesime, la
# licence et la precaution. Le cartouche les attache a l'image elle-meme --
# c'est le seul endroit qu'une reprise ne peut pas oublier.
# HAUTEUR : CARTOUCHE_H s'ajoute a la hauteur utile de chaque figure. Les
# attributs `height` des <img> qui les servent doivent suivre, sinon le ratio
# annonce au navigateur ment et la page saute au chargement.
CARTOUCHE_H = 48

LABELS_CARTOUCHE = {
    "fr": {
        "licence": "Compilation Stéphane Lalut, CC BY 4.0 · "
                   "stephane-lalut.com/cout-de-la-dette-publique/",
        "taux": "Taux implicite = intérêts de l'année / encours au "
                "31 décembre précédent, non le taux d'emprunt du jour.",
        "ciseau": "Deux échelles distinctes, une même unité : "
                  "le % du PIB.",
        "longue": "Dette au sens de Maastricht, toutes administrations publiques. « > 80 % » : "
                  "première fin d'année au-delà du seuil ; en trimestriel, il peut être franchi plus tôt.",
        # Lignes Â« source Â» et textes des cartes de la page : un seul modele
        # par figure, lu par le cartouche de l'image ET par la carte HTML.
        "src_ciseau": "INSEE, dette de Maastricht (%s)  ·  "
                      "Eurostat gov_10a_main, intérêts D41PAY (%s)",
        "src_taux": "Calcul sur séries Eurostat (gov_10a_main) et INSEE, %s-%s",
        "src_longue": "INSEE, dette de Maastricht, %s-%s",
        "titre_ciseau": "Le ciseau : encours et charge d'intérêts, 1995-%s",
        "titre_taux": "Le taux implicite, %s-%s",
        "titre_longue": "La dette depuis %s, en %% du PIB",
        "montre_ciseau": ("L'encours double en part de PIB pendant que la charge "
                          "d'intérêts baisse, jusqu'au retournement de 2022."),
        "montre_taux": ("Le coût moyen du stock : il baisse pendant vingt-cinq "
                        "ans, puis remonte depuis 2021."),
        "montre_longue": ("La dette monte par paliers, chacun installé par une "
                          "crise ; dans la série observée, le ratio n\'est jamais revenu à son niveau de dix ans auparavant."),
        "charge": ("Milliards d'euros courants, non corrigés de l'inflation : "
                   "la facture, non son poids dans la richesse produite."),
        "titre_charge": "La charge d'intérêts en milliards d'euros, %s-%s",
        "montre_charge": ("Ce que la dette coûte en euros, et non en part de PIB : "
                          "le creux, puis la remontée."),
        "masses": ("Les intérêts sont une nature de dépense, les trois autres des "
                   "fonctions : ce n'est pas le même découpage, et aucun transfert "
                   "n'est établi de l'un vers l'autre."),
        "titre_masses": "La charge d'intérêts face aux grands budgets, %s-%s",
        "montre_masses": ("La charge d'intérêts est longtemps restée sous le poste "
                          "« ordre et sécurité » ; elle est repassée au-dessus."),
        "marche": ("Le taux à 10 ans, repère du coût des emprunts nouveaux ; le "
                   "taux implicite, coût de tout le stock, ne le suit qu'au fil des "
                   "refinancements."),
        "src_marche": ("Eurostat irt_lt_mcby_a (taux à 10 ans)  ·  taux implicite : "
                       "Eurostat gov_10a_main et INSEE, %s-%s"),
        "titre_marche": "Taux de marché et coût moyen du stock, %s-%s",
        "montre_marche": ("Le coût moyen du stock suit le taux à 10 ans avec des "
                          "années de retard : il descend moins bas, et remonte moins vite."),
    },
    "en": {
        "licence": "Compiled by Stéphane Lalut, CC BY 4.0 · "
                   "stephane-lalut.com/en/cost-of-french-public-debt/",
        "taux": "Implicit rate = a year's interest / debt outstanding at the "
                "end of the previous year, not today's borrowing rate.",
        "ciseau": "Two separate scales, one shared unit: % of GDP.",
        "longue": ("Maastricht debt, general government. \"> 80%\": first year-end above the "
                   "threshold; in quarterly data it may be crossed earlier."),
        "src_ciseau": "INSEE, Maastricht debt (%s)  ·  "
                      "Eurostat gov_10a_main, interest D41PAY (%s)",
        "src_taux": "Computed on Eurostat (gov_10a_main) and INSEE series, %s-%s",
        "src_longue": "INSEE, Maastricht debt, %s-%s",
        "titre_ciseau": "The scissor: debt stock and interest burden, 1995-%s",
        "titre_taux": "The implicit interest rate, %s-%s",
        "titre_longue": "Debt since %s, as a %% of GDP",
        "montre_ciseau": ("The stock doubles as a share of GDP while the interest "
                          "burden falls, until the 2022 turn."),
        "montre_taux": ("The average cost of the stock: falling for twenty-five "
                        "years, rising again since 2021."),
        "montre_longue": ("Debt climbs in steps, each set by a crisis; in the observed series, the ratio has "
                          "never returned to its level of ten years earlier."),
        "charge": ("Billion euros at current prices, not adjusted for inflation: "
                   "the bill itself, not its weight in national income."),
        "titre_charge": "Interest paid in billion euros, %s-%s",
        "montre_charge": ("What the debt costs in euros rather than as a share of GDP: "
                          "the trough, then the climb."),
        "masses": ("Interest is a type of spending, the other three are functions: not "
                   "the same breakdown, and no transfer from one to the other is "
                   "established."),
        "titre_masses": "Interest paid against the main public budgets, %s-%s",
        "montre_masses": ("Interest paid long stayed below the public order and safety "
                          "function; it has moved back above it."),
        "marche": ("The 10-year yield benchmarks the cost of new borrowing; the implicit "
                   "rate, the cost of the whole stock, follows it only as old debt is "
                   "refinanced."),
        "src_marche": ("Eurostat irt_lt_mcby_a (10-year yield)  ·  implicit rate: "
                       "Eurostat gov_10a_main and INSEE, %s-%s"),
        "titre_marche": "Market rate and average cost of the stock, %s-%s",
        "montre_marche": ("The average cost of the stock follows the 10-year rate "
                          "years behind: it falls less far, and climbs back more slowly."),
    },
}


def _esc(s: str) -> str:
    """Le cartouche porte des URL et des libelles : `&` casserait le XML."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def cartouche(w: int, y0: float, source: str, note_cle: str,
              lang: str) -> list:
    """Deux lignes de pied : sources + millesime, puis licence + precaution.

    Rendu en 9 px sur 720 px de large. La longueur n'est pas ESTIMEE, elle est
    verifiee au rendu (`--png`) : un depassement ne casse rien et ne se voit
    pas dans le fichier -- le texte sort simplement du cadre, en silence.
    """
    T = LABELS_CARTOUCHE[lang]
    # TROIS lignes, et non deux : mesure du 21/09, la ligne unique
    # "licence + precaution" sortait du cadre a 720 px -- sans rien casser et
    # sans se voir dans le fichier. Une ligne par role, chacune sous 110
    # caracteres, ce que le rendu confirme.
    lignes = [(source, INK2)]
    note = T.get(note_cle, "")
    if note:
        lignes.append((note, INK2))
    lignes.append((T["licence"], MUTED))
    out = ['<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
           'stroke-width="1"/>' % (y0, w, y0, GRID)]
    for i, (txt, col) in enumerate(lignes):
        out.append('<text x="0" y="%.1f" font-family="%s" font-size="9" '
                   'fill="%s">%s</text>'
                   % (y0 + 13 + i * 12, FONT, col, _esc(txt)))
    return out


# ---------------------------------------------------------------- style B
# Bandes de crise, trait epais, valeur en pastille (choix de l'auteur, 28/09,
# sur maquettes). Le fond situe les ruptures sans que le lecteur les cherche
# dans le texte ; la pastille fait voyager la valeur cle avec l'image.
# (debut, fin, libelle fr, libelle en, PERIODE AFFICHEE) : la periode ne se
# deduit pas des bornes de la bande -- la bande de 1993 deborde sur 1994 pour
# rester visible, mais la recession, elle, est de 1993.
CRISES = ((1979.0, 1982.0, "post-choc pétrolier", "post-oil-shock", "1979-1982"),
          (1993.0, 1994.0, "récession", "recession", "1993"),
          (2008.0, 2010.0, "crise financière", "financial crisis", "2008-2009"),
          (2020.0, 2021.0, "crise sanitaire", "pandemic", "2020-2021"))
BANDE = "#eb6834"
# Orange ATTENUE des seuils anciens : l'orange sature est reserve au point
# contemporain et a la serie des interets (28/09). Sinon l'oeil rebondit sur cinq
# accents au lieu d'aller a la derniere valeur.
ORANGE_DOUX = "#b8703f"
PASTILLE = "#1B2A4E"


def bandes_crise(X, y_haut, y_bas, lang, x_min=None, x_max=None, libelles=True,
                 bas=False):
    """Bandes derriere la courbe : a emettre AVANT la serie, c'est un fond."""
    out = []
    for a1, a2, lib_fr, lib_en, _per in CRISES:
        if x_min is not None and a2 < x_min:
            continue
        if x_max is not None and a1 > x_max:
            continue
        xa, xb = X(a1), X(a2)
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                   'opacity="0.05"/>' % (xa, y_haut, max(xb - xa, 2.0), y_bas - y_haut, BANDE))
        # Le libelle ne s'imprime que la ou il ne heurte rien : dans la figure
        # longue, les jalons de seuil occupent deja le haut du cadre (vu au rendu).
        if libelles:
            # `bas` : 10 px au-dessus de la ligne de base du panneau, la ou aucune
            # courbe ne passe -- l'evenement est du contexte, il se lit apres.
            y = (y_bas - 10) if bas else (y_haut + 12)
            out.append('<text x="%.1f" y="%.1f" font-size="10" fill="%s" text-anchor="middle" '
                       'opacity="0.85">%s</text>'
                       % ((xa + xb) / 2, y, BANDE, _esc(lib_fr if lang == "fr" else lib_en)))
    return out


def pastille(x, y, valeur, sous, largeur=176.0, hauteur=44.0):
    """Valeur cle en pastille pleine, coin superieur gauche en (x, y)."""
    return ['<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>'
            % (x, y, largeur, hauteur, hauteur / 2, PASTILLE),
            '<text x="%.1f" y="%.1f" font-size="16" font-weight="700" fill="#ffffff" '
            'text-anchor="middle">%s</text>' % (x + largeur / 2, y + 20, _esc(valeur)),
            '<text x="%.1f" y="%.1f" font-size="10" fill="#b9c6de" text-anchor="middle">%s</text>'
            % (x + largeur / 2, y + 34, _esc(sous))]


NBSP = " "  # U+00A0 pose par code, jamais tape

# Libelles des figures, par locale. MEME regle que le bloc "affichage" : un seul
# calcul, deux presentations. Une figure aux axes francais sur une page anglaise
# est un DEFAUT, pas une inelegance -- c'est exactement ce que l'edition
# ANTHROPY a deja paye une fois (du francais imprime dans le livre anglais).
LABELS_MASSES = {
    "fr": {
        "titre": "La charge d'intérêts face aux grands budgets publics, %s-%s",
        # Autosuffisant hors de la page : la figure est proposee en ressource
        # reutilisable, « France » et « administrations publiques » doivent donc
        # etre dans l'IMAGE, pas seulement deductibles du texte qui l'entoure.
        "panneau": "France · administrations publiques · milliards d'euros courants — "
                   "la charge d'intérêts comparée à quelques grandes fonctions de dépense",
        "series": {"interets": "Charge d'intérêts", "GF07": "Santé",
                   "GF09": "Enseignement", "GF03": "Ordre et sécurité"},
        "postes": {"GF0703": "hôpital", "GF0702": "ambulatoire",
                   "GF0701": "produits médicaux", "GF0902": "secondaire",
                   "GF0901": "primaire", "GF0904": "supérieur",
                   "GF0906": "annexes", "reste": "autres"},
        "desc": "Quatre courbes en milliards d'euros courants, de %s à %s. La santé et "
                "l'enseignement progressent régulièrement et restent les plus élevés. La charge "
                "d'intérêts baisse jusqu'au début des années 2020, puis remonte et repasse "
                "au-dessus du poste « ordre et sécurité ».",
        "src": "Eurostat : intérêts versés (gov_10a_main, D41PAY) et dépenses des "
               "administrations par fonction (gov_10a_exp, COFOG), %s-%s",
        # Pas de cle « note » ici : la note affichee sous la figure est la precaution
        # C["masses"], et elle porte deja en TETE la phrase qui empeche la figure
        # d'etre trompeuse -- les interets sont une nature de depense, les trois
        # autres des fonctions. Une seconde formulation au meme endroit divergerait.
        # (Le champ « note » qui vivait ici n'etait lu par aucun appelant : retire
        # le 2026-09-29, verifie par grep.)
    },
    "en": {
        "titre": "Interest paid against the main public budgets, %s-%s",
        "panneau": "France · general government · billion euros, current prices — "
                   "interest paid compared with a few large functions of spending",
        "series": {"interets": "Interest paid", "GF07": "Health",
                   "GF09": "Education", "GF03": "Public order and safety"},
        "postes": {"GF0703": "hospital", "GF0702": "outpatient",
                   "GF0701": "medical products", "GF0902": "secondary",
                   "GF0901": "primary", "GF0904": "tertiary",
                   "GF0906": "ancillary", "reste": "other"},
        "desc": "Four curves in billion euros, from %s to %s. Health and education rise "
                "steadily and stay the highest. Interest paid falls until the early 2020s, then "
                "climbs back above the public order and safety function.",
        "src": "Eurostat: interest paid (gov_10a_main, D41PAY) and general government "
               "expenditure by function (gov_10a_exp, COFOG), %s-%s",
        # Voir le commentaire du bloc francais : la note vient de C["masses"].
    },
}

LABELS_CISEAU = {
    "fr": {
        "titre": "Le ciseau de la dette publique française : encours et "
                 "charge d'intérêts, 1995-2026",
        "desc": "Deux courbes en pourcentage du PIB. En haut, la dette publique "
                "passe de %s %% du PIB en %s à %s %% au %s. En bas, les intérêts "
                "versés par les administrations publiques passent de %s %% du "
                "PIB en %s à un creux de %s %% en %s, puis remontent à %s %% "
                "en %s.",
        "panneau_a": "Dette publique des administrations, en % du PIB "
                     "(INSEE, trimestriel)",
        "panneau_b": "Intérêts versés par les administrations, en % du PIB "
                     "(Eurostat, annuel)",
        "retournement": "2022 : le retournement",
        "en_annee": NBSP + "% en ",
        # le francais met une insecable avant %, l'anglais colle : c'est une
        # DONNEE DE LOCALE, pas une constante de mise en forme.
        "pct": NBSP + "%",
    },
    "en": {
        "titre": "The scissor of French public debt: outstanding stock and "
                 "interest burden, 1995-2026",
        "desc": "Two curves as a percentage of GDP. Above, public debt rises "
                "from %s%% of GDP in %s to %s%% in %s. Below, interest paid by "
                "general government falls from %s%% of GDP in %s to a trough of "
                "%s%% in %s, then climbs back to %s%% in %s.",
        "panneau_a": "General government debt, % of GDP (INSEE, quarterly)",
        "panneau_b": "Interest paid by general government, % of GDP "
                     "(Eurostat, annual)",
        "retournement": "2022: the turning point",
        "en_annee": "% in ",
        "pct": "%",
    },
}


def build_svg(dette_pib: dict[str, float], d41_pib: dict[str, float],
              lang: str = "fr") -> str:
    L = LABELS_CISEAU[lang]
    quarter = fr_quarter if lang == "fr" else en_quarter
    # decimale brute de la serie (1,3 vs 1.3) -- pas de separateur de milliers
    # ici : aucune de ces valeurs n'atteint 1000.
    dec = ((lambda v: str(v).replace(".", ",")) if lang == "fr"
           else (lambda v: str(v)))
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
             'role="img" font-variant-numeric="tabular-nums" aria-labelledby="cz-t cz-d" font-family="%s">'
             % (SVG_W, SVG_H + CARTOUCHE_H, FONT))
    e.append('<title id="cz-t">%s</title>' % L["titre"])
    e.append('<desc id="cz-d">%s</desc>'
             % (L["desc"] % (dec(dette_pib[first_q]), quarter(first_q),
                             dec(dette_pib[last_q]), quarter(last_q),
                             dec(d41_pib[first_y]), first_y,
                             dec(d41_pib[trough_y]), trough_y,
                             dec(d41_pib[last_y]), last_y)))

    # titres de panneaux (encre secondaire, jamais la couleur de serie)
    e.append('<text x="%d" y="22" font-size="13" fill="%s">%s</text>'
             % (MARG_L, INK2, L["panneau_a"]))
    e.append('<text x="%d" y="288" font-size="13" fill="%s">%s</text>'
             % (MARG_L, INK2, L["panneau_b"]))

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
    # le meme repere dans le panneau du haut : la simultanee se voit au lieu de
    # se lire (arbitrage PRO-20260928-DESIGN-GRAPHES, point 5)
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="1" stroke-dasharray="3 4"/>' % (x2022, ay1, x2022, ay0, AXIS))
    e.append('<text x="%.1f" y="243" font-size="11" fill="%s" '
             'text-anchor="middle">%s</text>' % (x2022, INK2, L["retournement"]))

    # bandes de crise en FOND des deux panneaux, avant les series (style B)
    # Les bandes traversent les deux panneaux, le LIBELLE ne s'ecrit qu'une fois,
    # dans celui du bas (choix de l'auteur, 28/09) : deux panneaux alignes sur le
    # meme axe temporel n'ont pas besoin de repeter le meme mot, et en haut la
    # courbe le frolait. Pose au-dessus de la ligne de base du panneau.
    # BORNES : depuis que la liste porte aussi 1979-1982 et 1993, une bande
    # anterieure au debut du ciseau se dessinerait hors du cadre, a gauche.
    e += bandes_crise(lambda a: _x(a, t0, t1), ay1, ay0, lang, libelles=False,
                      x_min=t0, x_max=t1)
    e += bandes_crise(lambda a: _x(a, t0, t1), by1, by0, lang, bas=True,
                      x_min=t0, x_max=t1)

    # series (2,6 px, bouts ronds)
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" '
             'stroke-linecap="round" stroke-linejoin="round"/>'
             % (_line_path(qpts), COL_DETTE))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" '
             'stroke-linecap="round" stroke-linejoin="round"/>'
             % (_line_path(ypts), COL_INTER))

    # etiquettes directes selectives : points d'arrivee + creux
    def dot_label(x, y, color, txt, anchor="start", dx=7, dy=4, fort=False):
        """`fort` : la valeur d'arrivee, ancrage de la figure (arbitrage du 28/09,
        point 4). Elle se lit avant tout le reste ; les autres etiquettes restent
        secondaires."""
        e.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                 % (x, y, 4.5 if fort else 3.5, color))
        e.append('<text x="%.1f" y="%.1f" font-size="%d" font-weight="%d" fill="%s" '
                 'text-anchor="%s">%s</text>'
                 % (x + dx, y + dy, 15 if fort else 12, 700 if fort else 400,
                    INK if fort else INK2, anchor, txt))

    lx, ly = qpts[-1]
    dot_label(lx, ly, COL_DETTE,
              dec(dette_pib[last_q]) + L["pct"],
              anchor="end", dx=-9, dy=-10, fort=True)
    fx, fy = qpts[0]
    dot_label(fx, fy, COL_DETTE,
              dec(dette_pib[first_q]) + L["pct"], dy=-8)
    ix, iy = ypts[-1]
    dot_label(ix, iy, COL_INTER,
              dec(d41_pib[last_y]) + L["pct"],
              anchor="end", dx=-9, dy=-11, fort=True)
    jx, jy = ypts[0]
    dot_label(jx, jy, COL_INTER,
              dec(d41_pib[first_y]) + L["pct"], dy=-8)
    tx = _x(int(trough_y) + 0.5, t0, t1)
    ty = by(d41_pib[trough_y])
    dot_label(tx, ty, COL_INTER,
              dec(d41_pib[trough_y]) + L["en_annee"] + trough_y, anchor="middle", dx=0, dy=18)

    src = LABELS_CARTOUCHE[lang]["src_ciseau"]
    e += cartouche(SVG_W, SVG_H + 4,
                   src % (quarter(max(dette_pib)), max(d41_pib)),
                   "ciseau", lang)
    e.append("</svg>")
    return "\n".join(e) + "\n"


LABELS_TAUX = {
    "fr": {
        "titre": "Le taux implicite de la dette publique française, %s-%s",
        "desc": "Une courbe, en pourcentage par an. Le taux implicite de la "
                "dette descend de %s %% en %s à %s %% en %s, son minimum sur la "
                "série, puis remonte à %s %% en %s. La baisse court sur près de "
                "vingt-cinq ans ; la remontée sur les dernières années.",
        "panneau": "Taux implicite de la dette publique, en % par an — "
                   "indicateur du coût moyen du stock",
        "en_annee": NBSP + "% en ",
    },
    "en": {
        "titre": "The implicit interest rate on French public debt, %s-%s",
        "desc": "A single curve, in percent per year. The implicit rate on the "
                "debt stock falls from %s%% in %s to %s%% in %s, its lowest "
                "point in the series, then climbs back to %s%% in %s. The "
                "decline runs for nearly twenty-five years; the rebound only "
                "for the last few.",
        "panneau": "Implicit interest rate on public debt, % per year — "
                   "a proxy for the average cost of the stock",
        "en_annee": "% in ",
    },
}


def build_svg_taux(taux: dict[str, float], lang: str = "fr") -> str:
    """Courbe du TAUX IMPLICITE -- le chainon causal que la page raconte sans le
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

    T = LABELS_TAUX[lang]
    num = (lambda v: fr(v, 1)) if lang == "fr" else (lambda v: en(v, 1))

    e = []
    e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
             'role="img" font-variant-numeric="tabular-nums" aria-labelledby="ta-t ta-d" font-family="%s">'
             % (W, H + CARTOUCHE_H, FONT))
    e.append('<title id="ta-t">%s</title>' % (T["titre"] % (first, last)))
    e.append('<desc id="ta-d">%s</desc>'
             % (T["desc"] % (num(taux[first]), first, num(taux[trough]), trough,
                             num(taux[last]), last)))
    e.append('<text x="%d" y="22" font-size="13" fill="%s">%s</text>'
             % (ml, INK2, T["panneau"]))

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
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.6" '
             'stroke-linecap="round" stroke-linejoin="round"/>'
             % (_line_path(pts), COL_INTER))

    # etiquetage direct SELECTIF : jamais un nombre sur chaque point
    def dot(px, py, txt, anchor, dx, dy):
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>'
                 % (px, py, COL_INTER))
        e.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s" '
                 'text-anchor="%s">%s</text>'
                 % (px + dx, py + dy, INK2, anchor, txt))

    dot(pts[0][0], pts[0][1], num(taux[first]) + T["en_annee"] + first,
        "start", 9, 4)
    dot(pts[-1][0], pts[-1][1], num(taux[last]) + T["en_annee"] + last,
        "end", -9, -10)
    dot(xt, y(taux[trough]), num(taux[trough]) + T["en_annee"] + trough,
        "middle", 0, 22)

    src = LABELS_CARTOUCHE[lang]["src_taux"]
    pc = " %" if lang == "fr" else "%"
    e += cartouche(W, H + 4, src % (first, last), "taux", lang)
    e.append("</svg>")
    return "\n".join(e) + "\n"


LABELS_LONGUE = {
    "fr": {
        "titre": "Dette publique française en %% du PIB, de %d à %s",
        "desc": ("Elle part de %s %% du PIB en %d, franchit 30 %% en %s, "
                 "60 %% en %s, 80 %% en %s, 100 %% en %s, et atteint %s %% "
                 "au %s."),
        "unite": " %",
    },
    "en": {
        "titre": "French public debt as a %% of GDP, from %d to %s",
        "desc": ("It starts at %s%% of GDP in %d, crosses 30%% in %s, "
                 "60%% in %s, 80%% in %s, 100%% in %s, and reaches %s%% "
                 "in %s."),
        "unite": "%",
    },
}


LABELS_MARCHE = {
    "fr": {"titre": "Taux \u00e0 10 ans et taux implicite de la dette publique, %s-%s",
           "desc": ("Deux courbes en pourcentage par an. Le taux \u00e0 10 ans passe de %s %% en %s "
                    "\u00e0 %s %% en %s, puis remonte \u00e0 %s %% en %s. Le taux implicite, co\u00fbt moyen "
                    "du stock, passe de %s %% \u00e0 %s %%, puis ne remonte qu'\u00e0 %s %% en %s."),
           "panneau": "Taux de march\u00e9 \u00e0 10 ans et co\u00fbt moyen du stock, en % par an",
           "marche": "Taux \u00e0 10 ans", "apparent": "Taux implicite", "pct": " %"},
    "en": {"titre": "10-year rate and implicit interest rate on French public debt, %s-%s",
           "desc": ("Two curves in percent per year. The 10-year rate goes from %s%% in %s to %s%% "
                    "in %s, then climbs back to %s%% in %s. The implicit rate, the average cost "
                    "of the stock, goes from %s%% to %s%%, then rises only to %s%% in %s."),
           "panneau": "10-year market yield and average cost of the stock, % per year",
           "marche": "10-year rate", "apparent": "Implicit rate", "pct": "%"},
}


def build_svg_marche(apparent: dict, marche: dict, lang: str = "fr") -> str:
    """Taux de marche a 10 ans (repere du cout des emprunts NOUVEAUX) et taux implicite (cout du
    STOCK) sur la MEME echelle : meme unite, et c'est l'ecart qui fait la
    demonstration -- le stock ne suit le marche qu'au fil des refinancements.
    Le taux implicite garde la couleur de l'entite « cout de la dette » ; le
    marche, repere, est en encre sombre et plus fin. Libelles directs aux
    extremites, places au-dessus pour la plus haute des deux : pas de legende."""
    W, H = 720, 360
    ml, mr = 46, 160  # 160 : « Taux implicite 2,0 % » en gras tenait mal dans 120 (etiquette coupee, contre-expertise du 28/09)
    ay0, ay1, vmin, vmax = 300.0, 46.0, -1.0, 7.0
    years = sorted(int(y) for y in apparent if y in marche)
    t0, t1 = years[0] - 0.6, years[-1] + 0.6

    def x(v): return ml + (v - t0) / (t1 - t0) * (W - ml - mr)
    def y(v): return ay0 - (v - vmin) / (vmax - vmin) * (ay0 - ay1)

    L = LABELS_MARCHE[lang]
    num = (lambda v: fr(v, 1)) if lang == "fr" else (lambda v: en(v, 1))
    first, last = str(years[0]), str(years[-1])
    creux = min((str(a) for a in years), key=lambda k: marche[k])
    pa = [(x(a), y(apparent[str(a)])) for a in years]
    pm = [(x(a), y(marche[str(a)])) for a in years]

    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
         'role="img" font-variant-numeric="tabular-nums" aria-labelledby="tm-t tm-d" font-family="%s">'
         % (W, H + CARTOUCHE_H, FONT)]
    e.append('<title id="tm-t">%s</title>' % (L["titre"] % (first, last)))
    e.append('<desc id="tm-d">%s</desc>' % (L["desc"] % (
        num(marche[first]), first, num(marche[creux]), creux, num(marche[last]), last,
        num(apparent[first]), num(min(apparent[str(a)] for a in years)),
        num(apparent[last]), last)))
    e.append('<text x="%d" y="22" font-size="13" fill="%s">%s</text>'
             % (ml, INK2, _esc(L["panneau"])))
    for v in (0, 2, 4, 6):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                 'stroke-width="1"/>' % (ml, y(v), W - mr, y(v), AXIS if v == 0 else GRID))
        e.append('<text x="%d" y="%.1f" font-size="11" fill="%s" '
                 'text-anchor="end">%d</text>' % (ml - 6, y(v) + 4, MUTED, v))
    for a in range(years[0] + 4, years[-1] + 1, 5):
        e.append('<text x="%.1f" y="%.1f" font-size="11" fill="%s" '
                 'text-anchor="middle">%d</text>' % (x(a), ay0 + 22, MUTED, a))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.6" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % (_line_path(pm), INK2))
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % (_line_path(pa), COL_INTER))

    # Libelles de fin : la courbe la plus haute prend le sien au-dessus. Ecart
    # MINIMUM garanti entre les deux : quand les deux series finissent proches,
    # « au-dessus » et « en dessous » ne suffisent plus a les separer.
    ECART_MIN = 26.0
    haut_m = marche[last] >= apparent[last]
    for serie, pts, col, cle, en_haut in (
            (marche, pm, INK2, "marche", haut_m),
            (apparent, pa, COL_INTER, "apparent", not haut_m)):
        px, py = pts[-1]
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (px, py, col))
        ecart = abs(pm[-1][1] - pa[-1][1])
        marge = max(0.0, (ECART_MIN - ecart) / 2.0)
        dy = (-9 - marge) if en_haut else (17 + marge)
        e.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s">'
                 '<tspan font-weight="600">%s</tspan> %s%s</text>'
                 % (px + 8, py + dy, col, _esc(L[cle]), num(serie[last]), L["pct"]))
    cx, cy = pm[years.index(int(creux))]
    e.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (cx, cy, INK2))
    e.append('<text x="%.1f" y="%.1f" font-size="11" fill="%s" text-anchor="middle">'
             '%s%s en %s</text>' % (cx, cy + 18, INK2, num(marche[creux]), L["pct"], creux))

    src = LABELS_CARTOUCHE[lang]["src_marche"]
    pc = " %" if lang == "fr" else "%"
    e += cartouche(W, H + 4, src % (first, last), "marche", lang)
    e.append("</svg>")
    return "\n".join(e) + "\n"


def build_svg_charge(interets_md: dict, lang: str = "fr") -> str:
    """La charge d'interets en MILLIARDS : la grandeur que le lecteur a en tete.

    Le % du PIB dit la soutenabilite, le milliard dit la facture. Les deux
    existent donc, et chacune porte son unite dans son intitule.
    """
    num = fr if lang == "fr" else en
    T = ({"panneau": "Charge d'intérêts des administrations publiques, en milliards d'euros courants",
          "creux": "creux de", "titre": "La charge d'intérêts en milliards d'euros, %s-%s",
          "src": "Eurostat, intérêts versés par les administrations publiques "
                 "(gov_10a_main, D41PAY), %s-%s",
          "desc": "Une courbe en milliards d'euros courants, de %s à %s. La charge d'intérêts "
                  "descend jusqu'au creux de %s, puis remonte fortement pour atteindre %s "
                  "milliards en %s."}
         if lang == "fr" else
         {"panneau": "Interest paid by general government, billion euros, current prices",
          "creux": "trough of", "titre": "Interest paid in billion euros, %s-%s",
          "src": "Eurostat, interest paid by general government (gov_10a_main, D41PAY), %s-%s",
          "desc": "One curve in billion euros, from %s to %s. Interest paid falls to its trough "
                  "in %s, then climbs steeply to %s billion in %s."})
    ans = sorted(int(a) for a in interets_md)
    a0, a1 = ans[0], ans[-1]
    creux = min(ans, key=lambda a: interets_md[a])
    W, H = 720, 340
    ml, mr, mt, mb = 52, 96, 46, 34
    vmax = max(interets_md.values()) * 1.12

    def X(a):
        return ml + (a - a0) / (a1 - a0) * (W - ml - mr)

    def Y(v):
        return H - mb - v / vmax * (H - mt - mb)

    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" '
         'aria-labelledby="ch-t ch-d" font-family="%s">' % (W, H + CARTOUCHE_H, FONT),
         '<title id="ch-t">%s</title>' % _esc(T["titre"] % (a0, a1)),
         '<desc id="ch-d">%s</desc>' % _esc(T["desc"] % (a0, a1, creux,
                                                         num(interets_md[a1], 1), a1)),
         '<text x="0" y="22" font-size="%d" fill="%s">%s</text>'
         % (TY_TITRE, INK2, _esc(T["panneau"]))]
    g = 0
    while g <= vmax:
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, Y(g), W - mr, Y(g), AXIS if g == 0 else GRID))
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="end">%d</text>'
                 % (ml - 7, Y(g) + 4, TY_AXE, MUTED, g))
        g += 20
    for a in range(a0, a1 + 1):
        if a % 10 == 0 or a == a1:
            e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="middle">%d</text>'
                     % (X(a), H - mb + 18, TY_AXE, MUTED, a))
    e += bandes_crise(X, mt, H - mb, lang, x_min=a0, x_max=a1)
    pts = [(X(a), Y(interets_md[a])) for a in ans]
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.8" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % (_line_path(pts), COL_INTER))
    # creux, en retrait ; derniere valeur, en ancrage
    cx, cy = X(creux), Y(interets_md[creux])
    e.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (cx, cy, COL_INTER))
    e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="middle">%s %s (%d)</text>'
             % (cx, cy + 20, TY_MINEUR, MUTED, _esc(T["creux"]), num(interets_md[creux], 1), creux))
    lx, ly = pts[-1]
    e.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (lx, ly, COL_INTER))
    e.append('<text x="%.1f" y="%.1f" font-size="%d" font-weight="700" fill="%s">%s</text>'
             % (lx + 10, ly + 2, TY_VALEUR, INK, num(interets_md[a1], 1)))
    e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s %d</text>'
             % (lx + 10, ly + 17, TY_MINEUR, MUTED, "Md€" if lang == "fr" else "bn", a1))
    e += cartouche(W, H + 4, T["src"] % (a0, a1), "charge", lang)
    e.append("</svg>")
    return "\n".join(e) + "\n"


def build_svg_masses(interets: dict, cofog: dict, lang: str = "fr") -> str:
    """Charge d'interets et grands budgets, en Md€ courants, millesime commun.

    Serie heroine en orange et epaisse, budgets en gris de valeurs differentes :
    la hierarchie tient sans la couleur (test du noir et blanc), et la regle des
    trois couleurs fonctionnelles est respectee.
    """
    L = LABELS_MASSES[lang]
    num = fr if lang == "fr" else en
    W, H = 720, 380
    # mr : place des etiquettes directes -- elargie le 29/09 pour les deux lignes
    # de decomposition (« hopital 109 · ambulatoire 92 » fait ~150 px a ce corps).
    ml, mr, mt, mb = 52, 196, 46, 34
    fonctions = ("GF07", "GF09", "GF03")
    ans = sorted(set(interets) & set.intersection(*[set(cofog[c]) for c in fonctions]))
    if len(ans) < 10:
        fail("masses comparees : millesimes communs insuffisants (%d)" % len(ans))
    a0, a1 = int(ans[0]), int(ans[-1])
    vmax = max(max(cofog[c][a] for a in ans) for c in fonctions) * 1.08

    def X(a):
        return ml + (int(a) - a0) / (a1 - a0) * (W - ml - mr)

    def Y(v):
        return H - mb - v / vmax * (H - mt - mb)

    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" '
         'aria-labelledby="ma-t ma-d" font-family="%s">' % (W, H + CARTOUCHE_H, FONT),
         '<title id="ma-t">%s</title>' % _esc(L["titre"] % (a0, a1)),
         '<desc id="ma-d">%s</desc>' % _esc(L["desc"] % (a0, a1)),
         '<text x="0" y="22" font-size="%d" fill="%s">%s</text>'
         % (TY_TITRE, INK2, _esc(L["panneau"]))]
    pas = 50 if vmax < 320 else 100
    g = 0
    while g <= vmax:
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, Y(g), W - mr, Y(g), AXIS if g == 0 else GRID))
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="end">%d</text>'
                 % (ml - 7, Y(g) + 4, TY_AXE, MUTED, g))
        g += pas
    for a in range(a0, a1 + 1):
        if a % 10 == 0 or a == a1:
            e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="middle">%d</text>'
                     % (X(a), H - mb + 18, TY_AXE, MUTED, a))
    # Annee de reference des croissances : le CREUX de la charge d'interets. Il se
    # calcule, il ne se choisit pas -- sinon la comparaison deviendrait un cadrage.
    ref = min(ans, key=lambda a: interets[a])
    # contexte d'abord, serie heroine ensuite : l'ordre de dessin est la hierarchie
    gris = {"GF07": INK2, "GF09": MUTED, "GF03": CTX3}
    bouts = []
    for c in fonctions:
        pts = [(X(a), Y(cofog[c][a])) for a in ans]
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.6" '
                 'stroke-linejoin="round"/>' % (_line_path(pts), gris[c]))
        bouts.append((pts[-1][1], gris[c], L["series"][c], cofog[c][ans[-1]], False,
                      (cofog[c][ans[-1]] / cofog[c][ref] - 1) * 100, c))
    pts = [(X(a), Y(interets[a])) for a in ans]
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.8" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % (_line_path(pts), COL_INTER))
    e.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s"/>' % (pts[-1][0], pts[-1][1], COL_INTER))
    # Le CREUX, marque sur la courbe : « +102 % depuis 2020 » est une assertion que
    # le lecteur doit pouvoir verifier de l'oeil -- 30 puis 60. L'annee et la valeur
    # sont celles du calcul de `ref`, jamais ecrites a la main.
    xr, yr = X(ref), Y(interets[ref])
    e.append('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s"/>' % (xr, yr, COL_INTER))
    e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="middle">'
             '%s — %d</text>' % (xr, yr + 17, TY_MINEUR, COL_INTER,
                                 num(interets[ref], 1), ref))
    bouts.append((pts[-1][1], COL_INTER, L["series"]["interets"], interets[ans[-1]], True,
                  (interets[ans[-1]] / interets[ref] - 1) * 100, "interets"))
    # Etiquetage DIRECT a droite, sans legende ; ecart minimum garanti, sinon
    # deux budgets proches se superposent (« ordre et securite » et les interets
    # se croisent justement a la fin de la serie).
    # Decomposition des deux grosses masses, en deux lignes sous leur etiquette :
    # « Sante 261 » ne dit pas ce qu'il y a derriere, et « Enseignement 149 » se lit
    # a tort comme 149 Md EUR de professeurs. Les postes sont derives (POSTES_COFOG),
    # le reste calcule par soustraction, donc la somme se ferme toujours. Aucune
    # qualification normative -- pas de « reellement consacres aux soins » : la
    # decomposition factuelle fait comprendre la distinction toute seule.
    detail = {}
    for fonction, postes in POSTES_COFOG.items():
        dispo = [(code, cofog[code][ans[-1]]) for code, _, _ in postes
                 if code in cofog and ans[-1] in cofog[code]]
        if len(dispo) < len(postes):
            continue                      # poste manquant : on n'affiche rien plutot qu'un faux
        reste = cofog[fonction][ans[-1]] - sum(v for _, v in dispo)
        if reste < 0:
            continue
        mots = ["%s %s" % (L["postes"][code], num(v, 0)) for code, v in dispo]
        mots.append("%s %s" % (L["postes"]["reste"], num(reste, 0)))
        # Couper la ou les deux lignes sont le plus egales EN LONGUEUR, non en
        # nombre de postes : « secondaire 64 · primaire 42 · superieur 12 » et
        # « annexes 20 · autres 10 » comptent 3 et 2 postes mais debordent la
        # marge d'un cote et la laissent vide de l'autre.
        milieu = min(range(1, len(mots)),
                     key=lambda k: abs(len(" · ".join(mots[:k]))
                                       - len(" · ".join(mots[k:]))))
        detail[fonction] = [" · ".join(mots[:milieu]), " · ".join(mots[milieu:])]

    bouts.sort()
    PAS = 13.0                            # interligne des lignes secondaires
    for i in range(1, len(bouts)):
        # L'ecart minimum n'est pas constant : un bloc decompose occupe deux lignes
        # de plus. Le mesurer sur le bloc PRECEDENT, sinon les deux plus proches --
        # « ordre et securite » et les interets, qui se croisent en fin de serie --
        # se superposent au detail de leur voisin du dessus.
        lignes_prec = 2 + len(detail.get(bouts[i - 1][6], []))
        besoin = lignes_prec * PAS + 6.0
        if bouts[i][0] - bouts[i - 1][0] < besoin:
            bouts[i] = (bouts[i - 1][0] + besoin,) + bouts[i][1:]
    for y, col, nom, val, fort, croiss, code in bouts:
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s">'
                 '<tspan font-weight="%d">%s</tspan> %s</text>'
                 % (W - mr + 12, y + 1, TY_ANNOT if fort else TY_MINEUR, col,
                    700 if fort else 600, _esc(nom), num(val, 0)))
        dy = y + 1
        for ligne in detail.get(code, []):
            dy += PAS
            e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%s</text>'
                     % (W - mr + 12, dy, TY_MINEUR - 1, MUTED, _esc(ligne)))
        # La croissance DEPUIS LE CREUX repond a la lecture spontanee de la
        # figure (« tout monte plus vite que les interets ») : vraie sur trente
        # ans, fausse depuis le creux. Calculee, jamais ecrite a la main.
        e.append('<text x="%.1f" y="%.1f" font-size="%d" fill="%s">%+d %% %s %d</text>'
                 % (W - mr + 12, dy + PAS, TY_MINEUR - 1, MUTED, round(croiss),
                    "depuis" if lang == "fr" else "since", ref))
    e += cartouche(W, H + 4, L["src"] % (a0, a1), "masses", lang)
    e.append("</svg>")
    return "\n".join(e) + "\n"


def build_svg_longue(annuel: dict, pct_courant: float, label_courant: str,
                     seuils: dict, lang: str = "fr", traj: dict | None = None) -> str:
    """Dette en % du PIB, de la premiere annee du segment fige a aujourd'hui.

    Meme couleur que la courbe de dette du ciseau : c'est la meme grandeur, et
    deux couleurs pour une seule serie feraient croire a deux mesures."""
    ans = sorted(annuel)
    L = LABELS_LONGUE[lang]
    nb = fr if lang == "fr" else en          # meme calcul, deux presentations
    U = L["unite"]
    pts = [(float(a), annuel[a]) for a in ans] + [(float(ans[-1]) + 0.25, pct_courant)]
    w, h = 720, 320
    # PROLONGEMENT PREVISIONNEL : il etend l'axe ET demande sa propre place a
    # droite, donc il se decide avant les marges.
    prev = sorted((a, v) for a, v in (traj or {}).items() if a > int(ans[-1]))
    ml, mr, mt, mb = 44, (128 if prev else 28), 34, 26  # place de l'etiquette de trajectoire
    x0, x1 = pts[0][0], pts[-1][0]
    if prev:
        x1 = float(prev[-1][0])
    ymax = 130.0

    def X(v):
        return ml + (v - x0) / (x1 - x0) * (w - ml - mr)

    def Y(v):
        return h - mb - v / ymax * (h - mt - mb)

    bandes = bandes_crise(X, mt, h - mb, lang, x_min=x0, x_max=x1, libelles=False)
    ligne = "M " + " L ".join("%.1f %.1f" % (X(a), Y(v)) for a, v in pts)
    aire = ("M %.1f %.1f L " % (X(x0), h - mb)
            + " L ".join("%.1f %.1f" % (X(a), Y(v)) for a, v in pts)
            + " L %.1f %.1f Z" % (X(pts[-1][0]), h - mb))   # ferme sur l'OBSERVE

    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
         'width="%d" height="%d" role="img" font-variant-numeric="tabular-nums" aria-labelledby="dl-t dl-d">'
         % (w, h + CARTOUCHE_H, w, h + CARTOUCHE_H)]
    e.append('<title id="dl-t">' + L["titre"] % (ans[0], label_courant) + '</title>')
    e.append('<desc id="dl-d">' + L["desc"]
             % (nb(annuel[ans[0]]), ans[0], seuils[30], seuils[60], seuils[80],
                seuils[100], nb(pct_courant), label_courant)
             + (("" if not prev else
                 (" Un prolongement en pointillés montre la trajectoire du projet de loi de "
                  "finances pour 2026, qui atteint %s%s en %d : une prévision, non une "
                  "observation." % (nb(prev[-1][1]), U, prev[-1][0]))) if lang == "fr" else
                ("" if not prev else
                 (" A dotted extension shows the path of the 2026 budget bill, reaching %s%s "
                  "in %d: a forecast, not an observation."
                  % (nb(prev[-1][1]), U, prev[-1][0]))))
             + '</desc>')
    e.append('<rect width="%d" height="%d" fill="#fff"/>' % (w, h))
    for g in (0, 25, 50, 75, 100, 125):
        e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="1"/>' % (ml, Y(g), w - mr, Y(g), GRID))
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="11" fill="%s" '
                 'text-anchor="end">%d%s</text>' % (ml - 7, Y(g) + 4, FONT, MUTED, g, U))
    # Seuil de traite : un fait, donc une ligne, pas une annotation flottante.
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="1" stroke-dasharray="5 4"/>' % (ml, Y(60), w - mr, Y(60), AXIS))
    e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="10" fill="%s">%s</text>'
             % (ml + 6, Y(60) - 5, FONT, MUTED,
                _esc("référence Maastricht, 60 %" if lang == "fr"
                     else "Maastricht reference, 60%")))
    # Les bandes passent APRES l'aplat : dessous, elles viraient au gris (vu au
    # rendu le 28/09). Elles restent derriere la courbe, qui domine.
    # Plus d'aplat sous la courbe : la ligne seule dans du blanc (direction
    # « minimal newsroom », 28/09). L'aire reste calculee mais n'est plus dessinee.
    if prev:
        # le prolongement part du dernier point OBSERVE : aucun saut, aucune
        # valeur intercalee entre les deux regimes.
        ppts = [(X(pts[-1][0]), Y(pct_courant))] + [(X(float(a)), Y(v)) for a, v in prev]
        e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" '
                 'stroke-dasharray="6 5" stroke-linejoin="round" opacity="0.75"/>'
                 % (_line_path(ppts), COL_DETTE))
        px, py = ppts[-1]
        e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="%s" '
                 'stroke-width="2"/>' % (px, py, COL_DETTE))
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" '
                 'font-weight="600" fill="%s">%s%s</text>'
                 % (px + 9, py + 1, FONT, TY_ANNOT, COL_DETTE, nb(prev[-1][1]), U))
        # SOUS la valeur d'arrivee, a droite du cercle : centree sur le pointille
        # elle heurtait « T1 2026 », au-dessus comme en dessous (deux rendus).
        # Ici elle nomme le trait sans disputer aucun aplomb.
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" '
                 'fill="%s">%s</text>'
                 % (px + 9, py + 16, FONT, TY_MINEUR, MUTED,
                    _esc("trajectoire PLF 2026" if lang == "fr"
                         else "2026 budget bill path")))
    e += bandes
    e.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.8" '
             'stroke-linejoin="round"/>' % (ligne, COL_DETTE))
    # valeur courante en pastille, dans l'angle haut-gauche : la courbe y est
    # au plus bas (premieres annees de la serie).

    # Un repere = un seuil franchi, donc un fait date, jamais une annee choisie
    # pour la jolie courbe. Disposition voulue par l'auteur le 20/09 : la DATE
    # en gras au-dessus de la courbe, le POURCENTAGE en couleur chaude dans
    # l'aire. Elle resout aussi le chevauchement : les etiquettes composees
    # (« 30 % en 1984 ») se touchaient des que deux reperes etaient proches,
    # parce que leur largeur ne dependait pas de leur ecart.
    # HIERARCHIE (arbitrage du 28/09) : six jalons de meme poids font une frise,
    # pas une lecture. Dominent : le depart, le seuil de Maastricht, le seuil de
    # 100 % (l'annee sanitaire) et le dernier point. Les deux autres restent
    # lisibles, en retrait. Le critere est le SEUIL, pas l'annee : il tient donc
    # quand la serie s'allonge.
    MAJEURS = (60, 100)
    reperes = [(float(ans[0]), annuel[ans[0]], str(ans[0]),
                nb(annuel[ans[0]]) + U, "start", True)]
    for s in (30, 60, 80, 100):
        an = seuils[s]
        reperes.append((float(an), annuel[int(an)], str(an), "> %d%s" % (s, U), "middle", s in MAJEURS))  # « > » : seuil franchi, pas valeur du point (relecture 28/09)
    reperes.append((pts[-1][0], pct_courant, label_courant,
                    nb(pct_courant) + U, "end", True))

    # Anti-collision : deux reperes proches voient leurs etiquettes se toucher,
    # et le cas se produit par construction a la fin de la serie -- le dernier
    # seuil franchi precede forcement le point courant. Plutot que d'ecarter le
    # cas a la main (il se deplacerait au prochain seuil), on replie a gauche
    # l'etiquette de tout repere dont le suivant est a moins de 95 px. Le
    # premier garde son ancrage : le replier le sortirait du cadre.
    # Toutes les etiquettes sont CENTREES sur leur point (auteur, 28/09) : une
    # date qui flotte a gauche de son marqueur ne le designe plus. Les ecarts
    # entre jalons le permettent ; le controle est fait ci-dessous, au rendu.
    reperes = [(xv, yv, date, pct, "middle", majeur)
               for xv, yv, date, pct, anchor, majeur in reperes]

    for xv, yv, date, pct, anchor, majeur in reperes:
        px, py = X(xv), Y(yv)
        dernier = xv == reperes[-1][0]
        # Meme diametre pour tous les points bleus : chaque jalon est un point de
        # bascule, et c'est la BANDE qui dit lequel. Seul le point contemporain,
        # en orange, se detache -- il n'est pas de la meme nature.
        e.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>'
                 % (px, py, "5" if dernier else "3.8",
                    COL_INTER if dernier else COL_DETTE))
        dx = 5 if anchor == "start" else (-5 if anchor == "end" else 0)
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" '
                 'font-weight="%d" fill="%s" text-anchor="%s">%s</text>'
                 % (px + dx, py - 13, FONT, TY_ANNOT, 700, INK2, anchor, date))
        # Le pourcentage doit etre SOUS la courbe, pas a une distance fixe du
        # point : la ou la pente est forte -- 2009, 2020 -- la ligne replonge
        # dans le texte quelques pixels plus loin. On prend donc le point le
        # plus bas de la courbe sur la LARGEUR REELLE de l'etiquette, et on se
        # pose en dessous. Mesure a l'ecran le 20/09 : « 80 % » etait traverse
        # par la courbe.
        corps = TY_ANNOT
        larg = 0.58 * corps * len(pct)
        tx = px + dx
        gx0 = tx if anchor == "start" else (tx - larg if anchor == "end"
                                            else tx - larg / 2)
        bas = py
        pas = max(1.0, (gx1 := gx0 + larg) - gx0) / 12.0
        xi = gx0
        while xi <= gx1:
            # inverse de X() : retrouver l'annee sous ce pixel, puis son y
            an_x = x0 + (xi - ml) / (w - ml - mr) * (x1 - x0)
            an_x = min(max(an_x, x0), x1)
            prec = [p for p in pts if p[0] <= an_x] or [pts[0]]
            suiv = [p for p in pts if p[0] >= an_x] or [pts[-1]]
            a, b = prec[-1], suiv[0]
            v = a[1] if b[0] == a[0] else a[1] + (b[1] - a[1]) * (an_x - a[0]) / (b[0] - a[0])
            bas = max(bas, Y(v))
            xi += pas
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" '
                 'font-weight="600" fill="%s" text-anchor="%s">%s</text>'
                 % (tx, bas + 17, FONT, corps,
                    COL_INTER if dernier else ORANGE_DOUX, anchor, pct))
    # Pas de libelles d'axe horizontal : les deux bornes de la periode sont
    # deja portees, en gras, par le premier et le dernier repere. Les repeter
    # sous l'axe ferait lire deux fois la meme date.

    # LEGENDE des bandes, sous l'axe : une figure reprise seule doit dire ce que
    # ses zones grisees signifient. Ordre chronologique, gris, une seule ligne.
    # Chaque libelle sous SA bande, sur deux lignes : periode au-dessus, intitule
    # en dessous (auteur, 28/09). Une ligne unique en pied ne disait pas quelle
    # bande portait quel mot ; ici le libelle est centre sur la bande qu'il nomme.
    for a1b, a2b, lf, le, per in CRISES:
        if a2b < x0 or a1b > x1:
            continue
        cx = (X(max(a1b, x0)) + X(min(a2b, x1))) / 2
        lib = lf if lang == "fr" else le
        # bornage : un libelle centre sur une bande de bord sortirait du cadre
        demi = 0.29 * (TY_MINEUR - 1) * max(len(lib), len(per))
        cx = min(max(cx, ml + demi), w - mr - demi)
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (cx, h - 18, FONT, TY_MINEUR - 1, MUTED, _esc(per)))
        e.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (cx, h - 6, FONT, TY_MINEUR - 1, MUTED, _esc(lib)))

    src = LABELS_CARTOUCHE[lang]["src_longue"]
    e += cartouche(w, h + 4, src % (ans[0], label_courant), "longue", lang)
    e.append("</svg>")
    return "\n".join(e) + "\n"


# ------------------------------------------------------------------- sortie
# Blocs d'affichage portant un "releve_le", en plus de la racine.
# Deux organes manipulent ce champ : l'empreinte qui DECIDE s'il faut publier, et
# la restauration qui APPLIQUE la decision. Chacun lisait sa propre liste. Le
# 16/08 la garde couvrait racine + "affichage" ; le 17/08 "affichage_en" est entre
# dans l'empreinte et PAS dans la restauration. Consequence mesuree le 06/09 : a
# donnees strictement identiques le script rendait quand meme une ligne de diff,
# la PR mensuelle vide etait de retour, et la page EN aurait publie un releve du
# 6 septembre que la page FR contredisait au 17 aout -- sur des chiffres CC BY
# repris dans le JSON-LD Dataset. Une seule liste, deux lecteurs.
BLOCS_RELEVE = ("affichage", "affichage_en")


def _blocs_dates(payload: dict):
    """Rend (cle, bloc) pour chaque dict portant un "releve_le", racine comprise.
    La cle vaut None pour la racine. Cle-a-cle, jamais par position : un paquet
    ancien peut ne pas avoir tous les blocs."""
    yield None, payload
    for cle in BLOCS_RELEVE:
        bloc = payload.get(cle)
        if isinstance(bloc, dict):
            yield cle, bloc


def _hors_dates(payload: dict) -> str:
    """Empreinte du paquet PRIVEE de ses horodatages, pour repondre a la
    seule question qui decide d'une publication : un chiffre a-t-il bouge ?"""
    c = json.loads(json.dumps(payload))
    for _, bloc in _blocs_dates(c):
        bloc.pop("releve_le", None)
    return json.dumps(c, ensure_ascii=False, sort_keys=True)


def csv_dette(payload: dict) -> str:
    import csv
    import io as _io
    buf = _io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "periode", "variable", "valeur", "unite", "source"])
    blocs = [("dette_trimestrielle", "dette_trimestrielle"), ("dette_annuelle_longue", "dette_annuelle_longue"),
             ("interets_annuels", "interets_annuels"), ("recettes_annuelles", "recettes_annuelles"),
             ("depenses_fonction_annuelles", "depenses_fonction_annuelles"), ("taux_long_terme_annuels", "taux_long_terme_annuels")]
    for cle, nom in blocs:
        b = payload.get(cle)
        if not isinstance(b, dict) or "series" not in b:
            continue
        unites = b.get("unite") if isinstance(b.get("unite"), dict) else {}
        src = b.get("source") if isinstance(b.get("source"), str) else json.dumps(b.get("source"), ensure_ascii=False)
        for var, serie in b["series"].items():
            if not isinstance(serie, dict):
                continue
            unite = unites.get(var, "") if unites else (b.get("unite") if isinstance(b.get("unite"), str) else "")
            if var == "taux_apparent_pct":
                unite = unite or "% par an (taux implicite)"
            for periode in sorted(serie):
                w.writerow([nom, periode, var, serie[periode], unite, src])
    return "\ufeff" + buf.getvalue()


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def meta_figures(lastq: str, last_y: str, taux: dict, annuel: dict,
                 masses: tuple[int, int], charge: tuple[int, int]) -> dict:
    """Donnees des cartes « Reutiliser » : meme texte que les cartouches.

    Source UNIQUE de la precaution de lecture : elle est ecrite une fois, dans
    LABELS_CARTOUCHE, et lue ici comme par l'image. Deux copies de la phrase
    qui sert a eviter un contresens finiraient par se contredire.
    """
    t0, t1 = min(taux), max(taux)
    a0 = min(annuel)
    m0, m1 = masses
    c0, c1 = charge
    out = {}
    for lang, quarter in (("fr", fr_quarter), ("en", en_quarter)):
        C = LABELS_CARTOUCHE[lang]
        q = quarter(lastq)
        suf = "" if lang == "fr" else "-en"
        out[lang] = [
            {"id": "ciseau", "fichier": "ciseau-dette-interets" + suf,
             "titre": C["titre_ciseau"] % q, "montre": C["montre_ciseau"],
             "source": C["src_ciseau"] % (q, last_y),
             "precaution": C["ciseau"]},
            {"id": "taux", "fichier": "taux-apparent-dette" + suf,
             "titre": C["titre_taux"] % (t0, t1), "montre": C["montre_taux"],
             "source": C["src_taux"] % (t0, t1), "precaution": C["taux"]},
            {"id": "longue", "fichier": "dette-longue" + suf,
             "titre": C["titre_longue"] % a0, "montre": C["montre_longue"],
             "source": C["src_longue"] % (a0, q), "precaution": C["longue"]},
            {"id": "marche", "fichier": "taux-marche-apparent" + suf,
             "titre": C["titre_marche"] % (t0, t1), "montre": C["montre_marche"],
             "source": C["src_marche"] % (t0, t1), "precaution": C["marche"]},
            {"id": "charge", "fichier": "charge-interets-mdeur" + suf,
             "titre": C["titre_charge"] % (c0, c1), "montre": C["montre_charge"],
             "source": (("Eurostat, intérêts versés par les administrations publiques "
                         "(gov_10a_main, D41PAY), %s-%s") if lang == "fr" else
                        ("Eurostat, interest paid by general government "
                         "(gov_10a_main, D41PAY), %s-%s")) % (c0, c1),
             "precaution": C["charge"]},
            {"id": "masses", "fichier": "masses-comparees" + suf,
             "titre": C["titre_masses"] % (m0, m1), "montre": C["montre_masses"],
             "source": LABELS_MASSES[lang]["src"] % (m0, m1), "precaution": C["masses"]},
        ]
    out["licence"] = {"fr": LABELS_CARTOUCHE["fr"]["licence"],
                      "en": LABELS_CARTOUCHE["en"]["licence"]}
    return out


def rendre_png(svgs: list) -> None:
    """Derive un PNG par SVG et note l'empreinte de la source dans un manifeste.

    L'absence de cairosvg n'est pas une panne : c'est le cas NORMAL hors du
    poste local. Elle se DIT, elle ne se tait pas -- un silence ici laisserait
    croire que les PNG viennent d'etre refaits.
    """
    try:
        import cairosvg
    except ImportError:
        print("PNG non rendus : cairosvg absent (cas normal hors poste local).")
        return
    import hashlib
    manifeste = {
        "_avertissement": ("Empreinte du SVG source au moment du rendu du PNG."
                           " Controle : scripts/check-png-dette.py"),
        "sources": {},
    }
    for svg in svgs:
        png = svg.with_suffix(".png")
        cairosvg.svg2png(url=str(svg), write_to=str(png), output_width=1440,
                         background_color="white")
        # Fins de ligne normalisees en LF : le manifeste doit dire la meme chose
        # selon qu'il est ecrit en CI (LF) ou sur un poste Windows (CRLF apres
        # checkout). Sans cela, les deux cotes se contredisent sans qu'aucun
        # fichier n'ait bouge -- cf. la docstring de check-png-dette.py, ou le
        # faux positif a ete mesure le 2026-09-29.
        manifeste["sources"][png.name] = hashlib.sha256(
            svg.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    # Manifeste dans data/ : c'est un artefact INTERNE de controle, il n'a
    # rien a faire parmi les fichiers servis au public.
    cible = REPO / "data" / "png_dette_source.json"
    cible.write_text(json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n",
                     encoding="utf-8")
    print("OK: %d PNG rendus (1440 px) + manifeste d'empreintes."
          % len(manifeste["sources"]))


def main() -> int:
    args = sys.argv[1:]
    check_only = "--check" in args
    faire_png = "--png" in args
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
    # Serie accessoire : un echec l'annonce et n'arrete rien.
    try:
        taux_marche = parse_eurostat(fetch(EURO_LT), "int_rt").get("MCBY", {})
        if len(taux_marche) < 20 or not all(-3 < v < 25 for v in taux_marche.values()):
            raise ValueError("serie hors bornes ou trop courte")
    except Exception as exc:
        print("AVERTISSEMENT non bloquant : taux a 10 ans indisponible (%s) ; "
              "figure taux-marche-apparent conservee en l'etat." % exc)
        taux_marche = None
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
    # Postes de niveau II : la garde porte sur la COHERENCE INTERNE, pas sur une
    # bande absolue. Une part du total ne derive pas avec l'inflation, et c'est
    # elle qui trahirait une inversion de code ou un poste devenu aberrant. Le
    # reste doit rester positif, sinon la decomposition affirmerait plus que le
    # total. Verifie sur le dernier millesime commun -- le seul qui s'affiche.
    for fonction, postes in POSTES_COFOG.items():
        annees_f = set(cofog_mio.get(fonction, {}))
        for code, lo, hi in postes:
            annees_f &= set(cofog_mio.get(code, {}))
        if not annees_f:
            fail("cofog niveau II : aucun millesime commun pour %s" % fonction)
            continue
        an = max(annees_f)
        total = cofog_mio[fonction][an]
        cumul = 0.0
        for code, lo, hi in postes:
            part = cofog_mio[code][an] / total if total else 0.0
            cumul += part
            in_band("part %s dans %s (%s)" % (code, fonction, an), part, lo, hi)
        in_band("reste de %s (%s)" % (fonction, an), 1.0 - cumul, 0.0, 0.40)
    check_annual("recettes_mdeur", tr_mdeur, 300, 3000)
    check_consolidated_anchors(dette_mdeur, dette_pib, d41_mio)
    check_delta_vs_committed(payload_prev, dette_mdeur, dette_pib, d41_mdeur)

    lastq = max(dette_mdeur) if dette_mdeur else None
    if lastq and lastq not in dette_pib:
        fail("periodes INSEE desalignees: %s absent du ratio" % lastq)
    if lastq and lastq in dette_pib and dette_pib[lastq] > 0:
        in_band("PIB implicite " + lastq,
                dette_mdeur[lastq] / (dette_pib[lastq] / 100.0), 1000, 5000)

    annuel = charger_historique(dette_pib)

    if FAILURES:
        print("ECHEC: %d garde(s) -- AUCUNE ecriture, fichiers precedents "
              "conserves." % len(FAILURES))
        return 1

    # -- derives (un seul endroit de calcul) --------------------------------
    hist = faits_historiques(annuel, dette_pib[max(dette_pib)])
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

    # taux implicite = interets de l'annee N / encours au T4 de N-1
    # (cout moyen du stock, PAS le taux d'emission courant)
    taux_apparent = {}
    for y in sorted(d41_mdeur):
        prev_q4 = "%d-Q4" % (int(y) - 1)
        if prev_q4 in dette_mdeur and dette_mdeur[prev_q4] > 0:
            taux_apparent[y] = round(d41_mdeur[y] / dette_mdeur[prev_q4] * 100.0, 2)
    if len(taux_apparent) < 20:
        print("ECHEC: serie taux implicite incomplete (%d obs) -- rien n'est ecrit."
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
    # MEME MILLESIME pour tous les termes d'une comparaison (arbitrage du 28/09) : la
    # section des masses comparees porte equiv_y en titre ; son ratio aux recettes doit
    # donc etre calcule sur equiv_y, et non sur la derniere annee disponible. Les deux
    # ratios coexistent : le recent en tete de page, celui du millesime commun dans la
    # comparaison. Absence de recettes sur equiv_y = echec, pas de repli silencieux.
    if equiv_y not in tr_mdeur or equiv_y not in d41_mdeur:
        print("ECHEC: recettes ou interets manquants pour le millesime commun %s." % equiv_y)
        return 1
    int_sur_recettes_equiv = round(d41_mdeur[equiv_y] / tr_mdeur[equiv_y] * 100.0, 1)
    # Croissances depuis le CREUX de la charge d'interets : c'est la seule lecture
    # qui repond a « tout monte plus vite que les interets » -- vraie sur trente
    # ans, fausse depuis le creux. Le creux se calcule ; la prose s'arrete si le
    # rapport s'inverse un jour.
    an_c = [a for a in d41_mdeur if a in cofog_mio.get("GF07", {})]
    creux_ref = min(an_c, key=lambda a: d41_mdeur[a])
    fin_c = max(an_c)
    croiss_int = (d41_mdeur[fin_c] / d41_mdeur[creux_ref] - 1) * 100
    croiss_fonc_max = max((cofog_mio[c][fin_c] / cofog_mio[c][creux_ref] - 1) * 100
                          for c in ("GF03", "GF07", "GF09"))
    if croiss_int < 2 * croiss_fonc_max:
        print("ECHEC: la page dit que les interets ont progresse bien plus vite que les "
              "fonctions depuis le creux (%.0f %% contre %.0f %%)." % (croiss_int, croiss_fonc_max))
        return 1
    in_band("interets/recettes " + equiv_y, int_sur_recettes_equiv, 1.0, 15.0)
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
    now_en = en_date(datetime.now(timezone.utc))

    # Deux presentations, UN SEUL corps : les blocs ne peuvent pas diverger
    # sur les VALEURS, seulement sur le format. C'est la meme regle que
    # "un seul endroit de calcul", appliquee a la locale.
    def bloc_affichage(nb, quarter, date_affichee):
        return {
            "dette_periode": quarter(lastq),
            "dette_mdeur": nb(dette_mdeur[lastq]),
            "dette_pct_pib": nb(dette_pib[lastq]),
            "dette_pic_periode": quarter(peak_q),
            "dette_pic_pct_pib": nb(dette_pib[peak_q]),
            "dette_1995_pct_pib": nb(dette_pib[min(dette_pib)]),
            "interets_annee": last_y,
            "interets_mdeur": nb(d41_mdeur[last_y]),
            "interets_pct_pib": nb(d41_pib[last_y]),
            "interets_1995_pct_pib": nb(d41_pib[min(d41_pib)]),
            "interets_creux_annee": trough_y,
            "interets_creux_mdeur": nb(d41_mdeur[trough_y]),
            "interets_creux_pct_pib": nb(d41_pib[trough_y]),
            "interets_hausse_pct": str(hausse_pct),
            "interets_2019_mdeur": nb(d41_mdeur["2019"]),
            "interets_hausse_2019_pct": str(hausse_2019_pct),
            "taux_apparent_premier_annee": ta_first,
            "taux_apparent_premier": nb(taux_apparent[ta_first]),
            "taux_apparent_creux_annee": ta_trough,
            "taux_apparent_creux": nb(taux_apparent[ta_trough]),
            "taux_apparent_dernier_annee": ta_last,
            "taux_apparent_dernier": nb(taux_apparent[ta_last]),
            "recettes_annee": tr_last,
            "recettes_mdeur": nb(tr_mdeur[tr_last]),
            "interets_sur_recettes_pct": nb(int_sur_recettes),
            "equiv_annee": equiv_y,
            "interets_equiv_mdeur": nb(int_equiv),
            "recettes_equiv_mdeur": nb(tr_mdeur[equiv_y]),
            "creux_ref_annee": creux_ref,
            "croiss_interets_depuis_creux_pct": nb(croiss_int, 0),
            "croiss_fonctions_depuis_creux_pct": nb(croiss_fonc_max, 0),
            "interets_sur_recettes_equiv_pct": nb(int_sur_recettes_equiv),
            "justice_mdeur": nb(cof24["GF0303"]),
            "ordre_mdeur": nb(cof24["GF03"]),
            "sante_mdeur": nb(cof24["GF07"]),
            "education_mdeur": nb(cof24["GF09"]),
            "ratio_interets_justice": nb(round(int_equiv / cof24["GF0303"], 1)),
            "pct_interets_education": str(round(int_equiv / cof24["GF09"] * 100)),
            "pct_interets_sante": str(round(int_equiv / cof24["GF07"] * 100)),
            "croissance_annuelle_pct": nb(croissance),
            # Serie longue : la page raconte les paliers en toutes lettres,
            # donc ils se calculent ici et nulle part ailleurs.
            "hist_annee_debut": str(hist["annee_debut"]),
            "hist_pct_debut": nb(hist["pct_debut"]),
            "hist_seuil_30_annee": str(hist["seuils"][30]),
            "hist_seuil_60_annee": str(hist["seuils"][60]),
            "hist_seuil_80_annee": str(hist["seuils"][80]),
            "hist_seuil_100_annee": str(hist["seuils"][100]),
            "hist_annees_baisse": str(hist["annees_baisse"]),
            "hist_annees_total": str(hist["annees_total"]),
            "hist_plus_longue_baisse": str(hist["plus_longue_baisse"]),
            "hist_multiple": nb(round(hist["multiple"], 1)),
            # Vaut "0" tant que le ratio n'est jamais revenu a son niveau de
            # dix ans plus tot. La page en tire une affirmation ; elle est
            # rendue SOUS CONDITION de cette cle, pour qu'un reflux durable
            # la fasse disparaitre au lieu de la laisser mentir.
            "hist_retour_10_ans": str(hist["retour_10_ans"]),
            "releve_le": date_affichee,
        }

    affichage = bloc_affichage(fr, fr_quarter, now_fr)
    affichage_en = bloc_affichage(en, en_quarter, now_en)

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
        "affichage_en": affichage_en,
        "live": live,
        "dette_annuelle_longue": {
            "source": ("INSEE, dette de Maastricht des administrations "
                       "publiques au 31 décembre — segment 1978-1995 issu du "
                       "tableau 2830192 (comptes nationaux base 2020, clos), "
                       "prolongé par la série trimestrielle (T4 de chaque "
                       "année). Année de recouvrement contrôlée à chaque "
                       "exécution."),
            "unite": {"pct_pib": "% du PIB"},
            "premiere_annee": str(min(annuel)),
            "derniere_annee": str(max(annuel)),
            "seuils_franchis": {str(s): str(a) for s, a in hist["seuils"].items()},
            "series": {"pct_pib": {str(a): annuel[a] for a in sorted(annuel)}},
        },
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
    # Serie du taux a 10 ans, jointe au jeu public (relecture externe du 28/09 : la
    # figure « taux de marche » n'etait pas reproductible depuis le JSON). Serie
    # ACCESSOIRE : si son fetch echoue, on reprend le bloc deja publie plutot que de
    # le retirer en silence -- et l'empreinte ne bouge pas pour autant.
    if taux_marche:
        payload["taux_long_terme_annuels"] = {
            "source": ("Eurostat, irt_lt_mcby_a -- rendement des titres publics de "
                       "reference a 10 ans (critere de convergence de Maastricht), France"),
            "dataset": "irt_lt_mcby_a",
            "unite": {"pct": "% par an, moyenne annuelle"},
            "derniere_periode": max(taux_marche),
            "series": {"pct": {y: taux_marche[y] for y in sorted(taux_marche)}},
        }
    elif payload_prev and "taux_long_terme_annuels" in payload_prev:
        payload["taux_long_terme_annuels"] = payload_prev["taux_long_terme_annuels"]
    inchange = payload_prev is not None and _hors_dates(payload) == _hors_dates(payload_prev)
    if inchange:
        for cle, bloc in _blocs_dates(payload):
            prec = payload_prev if cle is None else payload_prev.get(cle)
            if isinstance(prec, dict) and "releve_le" in prec:
                bloc["releve_le"] = prec["releve_le"]

    if check_only:
        print("OK (--check): gardes passees, rien n'est ecrit. Dette %s = %s "
              "Md EUR / %s %% PIB ; interets %s = %s Md EUR%s"
              % (lastq, dette_mdeur[lastq], dette_pib[lastq],
                 last_y, d41_mdeur[last_y],
                 " -- INCHANGE depuis le releve du " + str(payload["releve_le"])
                 if inchange else " -- DONNEES NOUVELLES"))
        return 0

    txt = json.dumps(payload, ensure_ascii=False, indent=1) + "\n"
    # TOUT est construit avant la premiere ecriture. Mesure du 2026-09-20 :
    # une exception levee pendant la generation d'une figure laissait le JSON
    # deja ecrit et les figures anciennes -- et, au passage suivant, le script
    # comparait au paquet neuf, concluait "contenu inchange" et ne regenerait
    # rien. Le depot disait alors une chose et la figure une autre, sans
    # erreur ni trace. Construire d'abord, ecrire ensuite : un echec laisse
    # l'ensemble dans son etat precedent, coherent.
    # Millesime commun des masses comparees : les series par fonction s'arretent
    # avant les interets, et une comparaison ne melange pas deux annees.
    trajectoire = lire_trajectoire()
    _codes_md = ["GF0303", "GF03", "GF07", "GF09"]
    _codes_md += [code for postes in POSTES_COFOG.values() for code, _, _ in postes]
    cofog_md = {c: {int(a): v / 1000.0 for a, v in cofog_mio[c].items()}
                for c in _codes_md if c in cofog_mio}
    inter_md = {int(a): v for a, v in d41_mdeur.items()}
    ans_masses = sorted(set(inter_md) & set(cofog_md["GF07"]) & set(cofog_md["GF09"])
                        & set(cofog_md["GF03"]))
    sorties = [
        (OUT_FIGURES, json.dumps(meta_figures(
            lastq, last_y, taux_apparent, annuel,
            (ans_masses[0], ans_masses[-1]),
            (min(inter_md), max(inter_md))),
            ensure_ascii=False, indent=1) + "\n"),
        (OUT_JSON, txt),
        (OUT_ENDPOINT, txt),
        (OUT_CSV, csv_dette(payload)),
        (OUT_SVG, build_svg(dette_pib, d41_pib)),
        (OUT_SVG_TAUX, build_svg_taux(taux_apparent)),
        (OUT_SVG_EN, build_svg(dette_pib, d41_pib, lang="en")),
        (OUT_SVG_TAUX_EN, build_svg_taux(taux_apparent, lang="en")),
        (OUT_SVG_LONGUE, build_svg_longue(
            annuel, dette_pib[lastq], fr_quarter(lastq), hist["seuils"],
            traj=trajectoire.get("dette"))),
        (OUT_SVG_LONGUE_EN, build_svg_longue(
            annuel, dette_pib[lastq], en_quarter(lastq), hist["seuils"],
            lang="en", traj=trajectoire.get("dette"))),
        (OUT_SVG_CHARGE, build_svg_charge(inter_md)),
        (OUT_SVG_CHARGE_EN, build_svg_charge(inter_md, lang="en")),
        (OUT_SVG_MASSES, build_svg_masses(inter_md, cofog_md)),
        (OUT_SVG_MASSES_EN, build_svg_masses(inter_md, cofog_md, lang="en")),
    ]
    if taux_marche:
        sorties += [
            (OUT_SVG_MARCHE, build_svg_marche(taux_apparent, taux_marche)),
            (OUT_SVG_MARCHE_EN, build_svg_marche(taux_apparent, taux_marche,
                                                 lang="en")),
        ]
    # Le workflow enumere a la main les fichiers qu'il commite. Deux fois deja
    # -- le 16/08 (courbe du taux implicite) et le 20/09 (courbe longue EN) --
    # une sortie NOUVELLE a failli rester hors de cette liste : elle aurait ete
    # regeneree en CI puis jamais publiee, laissant une figure figee en ligne
    # sans erreur ni trace. Le script est le seul a connaitre ses sorties :
    # c'est donc ici que la comparaison se fait.
    wf = REPO / ".github" / "workflows" / "dette-insee.yml"
    if wf.is_file():
        texte = wf.read_text(encoding="utf-8")
        # Les PNG derives comptent AUSSI : depuis le 2026-09-21 la CI les rend
        # (etape non bloquante) et doit donc les committer. Un quatrieme
        # graphique ajoute demain aurait sinon un PNG regenere en CI et jamais
        # publie -- exactement le defaut que cette garde previent pour les SVG.
        attendus = [c.relative_to(REPO).as_posix() for c, _ in sorties]
        attendus += [c.with_suffix(".png").relative_to(REPO).as_posix()
                     for c, _ in sorties if c.suffix == ".svg"]
        attendus.append("data/png_dette_source.json")
        oubliees = [c for c in attendus if c not in texte]
        if oubliees:
            print("ECHEC: sortie(s) absente(s) du `git add` de %s : %s"
                  % (wf.name, ", ".join(oubliees)))
            print("       -- elles seraient regenerees en CI et jamais publiees.")
            return 1

    for chemin, contenu in sorties:
        atomic_write(chemin, contenu)

    # PNG : derives des SVG, JAMAIS dans la chaine automatique. Rendre une image
    # demande une dependance graphique ; l'exiger en CI ferait dependre la mise a
    # jour des DONNEES d'une bibliotheque d'images -- l'essentiel suspendu a
    # l'accessoire. Ils sont donc produits ici a la demande, et leur peremption
    # est guettee par scripts/check-png-dette.py, qui compare l'empreinte du SVG
    # source a celle du SVG courant.
    if faire_png:
        rendre_png([c for c, _ in sorties if c.suffix == ".svg"])
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
