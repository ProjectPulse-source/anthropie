#!/usr/bin/env python3
"""update_parcoursup.py -- ressource « Parcoursup : quelles sont vraiment vos chances d'être admis ? » (bloc École, lycée
et université).

Découverte de la page (dépôt de pilotage de l'auteur, 06_PROMOTION/RECHERCHE_RESSOURCE_UNIVERSITE_2026-11-03, cinq
contre-expertises arbitrées les 10 et 11/11/2026, panel avant du 11/11) : d'une session à la suivante, le taux d'accès
d'une formation change peu le plus souvent, et parfois beaucoup ; au-dessus de 90 %, le conseil courant tient le plus
souvent ; certaines filières varient ensemble. La page décrit une dispersion PASSÉE, jamais une prévision.

Entrées : les exports archivés des jeux ouverts Parcoursup, une session par fichier
(scripts/sources_parcoursup/manifeste.json, empreintes dans SHA256SUMS). Ce que fait ce script, et rien de plus :
- il LIT ces exports ; le taux d'accès y est REPRIS tel que le ministère le publie, il n'est pas recalculé (il ne peut
  pas l'être à partir du fichier ouvert) ;
- il APPARIE les formations de deux sessions consécutives (même code, même intitulé) et compte les écartées par motif ;
- il CALCULE, par tranche de taux de départ, les déciles, la médiane et des parts ; les corrélations ; les variations
  par filière ; trois sensibilités ; le test de sélection de l'appariement ;
- il COMPARE ses résultats à un témoin écrit par un autre code sur d'autres fichiers (temoin.json : appariement de
  p04b.py, corrélations de p05.py, export 2023 d'origine) et s'arrête à 0,1 point d'écart ;
- il s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases (fonction
  garde_constats), ou si une fraction écrite en lettres sort de son intervalle.
Ce qu'il ne fait pas : aucune probabilité individuelle, aucun taux par type de bac (absent du fichier ouvert), aucune
prévision, aucune décomposition causale.

Sessions : celles du manifeste. Les jetons portent un RÔLE (p_ : transition précédente ; d_ : dernière transition), pas
une année : à la parution de la session suivante, on dépose son export, on relance le témoin, et la page se réécrit ou
une garde dit quelle phrase est à reprendre.
Mise à jour : à la main, hors module pour l'instant. Rendez-vous de rattrapage : 31 mars 2027 (jeu de la session 2026 ;
celui de 2025 a été publié le 09/03/2026). La ligne au registre data/sources_maj.json s'écrit avec la page.
Page en français seulement (exclusion déclarée : procédure française, comme les pages voisines du bloc).

Usage : python scripts/update_parcoursup.py [--check] [--mutation=<nom>] [--mutations]
  --mutations : rejoue toutes les mutations et exige que chacune fasse mordre SA garde.
Sorties : data/ et static/parcoursup.json, static/parcoursup.csv, data/figures_parcoursup.json,
static/img/parcoursup-tranches.svg et parcoursup-filieres.svg, leurs versions téléphone (-m.svg), et leurs PNG.
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
import statistics as st
import sys
from collections import Counter, defaultdict
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import langue_generee as lg  # nombres, signes et accord de « point » à la précision affichée
import pied_figure  # pied commun, coupure des lignes, version téléphone, parité
import releve_jeu  # releve_le ne bouge qu'avec une donnée

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_parcoursup"
OUT_DATA = ROOT / "data" / "parcoursup.json"
OUT_STATIC = ROOT / "static" / "parcoursup.json"
OUT_CSV = ROOT / "static" / "parcoursup.csv"
OUT_FIGURES = ROOT / "data" / "figures_parcoursup.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_MD = ROOT / "content" / "parcoursup-quelles-chances-d-etre-admis" / "_index.md"
PAGE_URL = "stephane-lalut.com/parcoursup-quelles-chances-d-etre-admis/"
LICENCE = ("CC BY 4.0 — calcul Stéphane Lalut ; source : ministère chargé de l'enseignement supérieur (SIES), jeux "
           "ouverts Parcoursup, Licence Ouverte 2.0")

COLONNES = ("session", "g_ea_lib_vx", "lib_for_voe_ins", "fili", "capa_fin", "nb_voe_pp", "nb_voe_pc", "nb_cla_pp",
            "prop_tot", "acc_tot", "taux_acces_ens", "part_acces_gen", "part_acces_tec", "part_acces_pro", "cod_aff_form")
# Tranches du taux de départ, fixées par le protocole avant tout calcul : [bas ; haut[, la dernière réduite à 100.
# Les CLÉS (« 60-75 ») nomment l'intervalle [60 ; 75[ du protocole ; les LIBELLÉS affichés donnent ses bornes entières
# incluses (« 60 à 74 % »), parce que les taux sont des entiers et qu'une formation à 75 % se chercherait sinon dans la
# mauvaise ligne (contrôleur de lecture, 11/11/2026).
TRANCHES = (("0-20", 0, 20, "moins de 20 %"), ("20-40", 20, 40, "20 à 39 %"), ("40-60", 40, 60, "40 à 59 %"),
            ("60-75", 60, 75, "60 à 74 %"), ("75-90", 75, 90, "75 à 89 %"), ("90-99", 90, 100, "90 à 99 %"),
            ("100", 100, 101, "100 %"))
COURT_TRANCHE = {"0-20": "moins de 20 %", "20-40": "20-39 %", "40-60": "40-59 %", "60-75": "60-74 %",
                 "75-90": "75-89 %", "90-99": "90-99 %", "100": "100 %"}
JETON_TRANCHE = {"0-20": "t0020", "20-40": "t2040", "40-60": "t4060", "60-75": "t6075", "75-90": "t7590",
                 "90-99": "t9099", "100": "t100"}
# Motifs d'écart, dans l'ordre de priorité du protocole (§ 2) : le premier qui s'applique l'emporte.
MOTIFS = ("nouvelle", "disparue", "intitulé changé", "taux absent", "aucun classé")
JETON_MOTIF = {"nouvelle": "nouv", "disparue": "disp", "intitulé changé": "intit", "taux absent": "tauxabs",
               "aucun classé": "nonclasse", "appariée": "app"}
JETON_FILIERE = {"CPGE": "cpge", "BTS": "bts", "BUT": "but", "Licence": "licence", "Licence_Las": "las", "PASS": "pass",
                 "IFSI": "ifsi", "EFTS": "efts", "Ecole d'Ingénieur": "ing", "Ecole de Commerce": "com",
                 "Autre formation": "autre"}
SEUIL_FILIERE = 100
# Seuils des constats : la prose les affiche par jetons (seuil_*), jamais en chiffres saisis à côté du calcul.
SEUIL_RESTE, SEUIL_BAISSE, SEUIL_SELECT, SEUIL_ATTEINT, SEUIL_CAND, SEUIL_CAPA = 90, 20, 20, 40, 50, 0.25      # une filière entre dans les tableaux à partir de cent formations appariées
RECLASSEE = "filière reclassée"   # formation appariée dont la filière (fili) diffère entre les deux sessions
TOLERANCE = 0.1          # garde 4 : écart admis avec le témoin, en points
TOLERANCE_CORR = 0.001   # corrélations : une tolérance de 0,1 n'y garderait rien
COMPTES = {"n", "entrees", "appariees", "n_reste_90", "n_baisse_20", "n_50cand", "atteint_40", "n_interieur"}
HORS_TEMOIN = {"de", "a", "cle", "petites_filieres"}   # clés d'une transition propres au générateur, sans valeur à comparer
# Garde 9 : une fraction écrite en lettres vaut dans un intervalle de parts (en %), jamais au-delà.
FRACTIONS = {"une sur dix": (8.5, 11.5), "une sur cinq": (18.0, 22.5), "un peu plus d'une sur deux": (51.0, 56.0),
             "deux sur trois": (64.5, 68.5), "près de quatre sur cinq": (76.0, 79.95), "huit sur dix": (78.0, 83.0),
             "une formation sur deux": (50.0, 57.0)}
# Garde 8 : formules retirées par les arbitrages des pièces 04, 05 et 06 et par le panel avant (jamais dans la page).
# Pièce 06 : « le plus souvent » rassure trop pour une part de 52 à 55 % (la page écrit la fraction et son nombre) ;
# « personne ne peut calculer » affirme plus que la page n'établit (elle montre ce que le taux publié ne donne pas).
INTERDITES = (r"fourchette,? pas un point", r"ne fluctuent pas au hasard", r"loterie réfutée",
              r"l'année compte autant que la formation", r"où lire sa propre chance",
              r"placer (ses|vos|tes|leurs) v(œ|oe)ux de sécurité", r"taux médian a baissé",
              r"le plus souvent", r"personne ne peut calculer",
              # Pièce 08 : les données mesurent la tenue d'un seuil par des formations, pas le réalisme d'un vœu pour un
              # candidat ; « le conseil tient » validait ce qui n'est pas testé. « Et elle seule » : absolu inutile.
              r"le conseil tient", r"et elle seule")


class Arret(SystemExit):
    """Arrêt d'une garde : SystemExit(1) qui garde son message, pour qu'une mutation sache QUELLE garde a mordu."""

    def __init__(self, msg: str):
        super().__init__(1)
        self.msg = msg


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


def fail(msg: str) -> None:
    log("ECHEC : " + msg)
    log("Aucun fichier ecrit.")
    raise Arret(msg)


def nombre(x: str, quoi: str):
    """Cellule vide : None (donnée absente, jamais zéro). Cellule illisible : arrêt."""
    if x is None or x.strip() == "":
        return None
    try:
        return float(x)
    except ValueError:
        fail("cellule illisible (%s) : %r" % (quoi, x))


# ------------------------------------------------------------------ lecture (gardes 2 et 7)
def lire(mut: str = "") -> dict:
    man = json.loads((SRC / "manifeste.json").read_text(encoding="utf-8"))
    sums = {}
    for ligne in (SRC / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if ligne.strip():
            h, nom = ligne.split(None, 1)
            sums[nom.strip().lstrip("*")] = h
    if mut == "empreinte":      # l'export de la dernière session ne rend plus l'empreinte inscrite
        sums[man["sessions"][-1]["fichier"]] = "0" * 64

    def octets(nom: str) -> bytes:
        b = (SRC / nom).read_bytes()
        h = hashlib.sha256(b).hexdigest()
        if sums.get(nom) != h:
            fail("garde 7 (empreintes) : %s ne rend pas l'empreinte de SHA256SUMS (%s) ; un export qui change sans "
                 "mise a jour declaree du jeu arrete la generation" % (nom, h))
        return b

    ans = [s["session"] for s in man["sessions"]]
    if len(ans) < 2 or any(b - a != 1 for a, b in zip(ans, ans[1:])):
        fail("manifeste : il faut au moins deux sessions consecutives, lu %s" % ans)
    S = {}
    for s in man["sessions"]:
        lignes = list(csv.DictReader(io.StringIO(octets(s["fichier"]).decode("utf-8-sig")), delimiter=";"))
        manque = [c for c in COLONNES if c not in (lignes[0] if lignes else {})]
        if manque:
            fail("%s : colonnes absentes %s" % (s["fichier"], manque))
        if len(lignes) != s["lignes"]:
            fail("%s : %d lignes lues, %d declarees au manifeste" % (s["fichier"], len(lignes), s["lignes"]))
        if mut == "bornes" and s is man["sessions"][-1]:      # un taux hors de 0-100 dans la dernière session
            lignes[0] = dict(lignes[0], taux_acces_ens="101")
        F = {}
        for r in lignes:
            if r["session"] != str(s["session"]):
                fail("%s : ligne de la session %r dans le fichier de %d" % (s["fichier"], r["session"], s["session"]))
            t = nombre(r["taux_acces_ens"], "taux d'acces")
            if t is not None and (t != int(t) or not 0 <= t <= 100):
                fail("garde 2 (bornes) : taux d'acces %r hors des entiers de 0 a 100 (%s, formation %s)"
                     % (r["taux_acces_ens"], s["fichier"], r["cod_aff_form"]))
            F[r["cod_aff_form"]] = {
                "lib": r["lib_for_voe_ins"], "etab": r["g_ea_lib_vx"], "fili": r["fili"],
                "taux": None if t is None else int(t), "capa": nombre(r["capa_fin"], "capacite"),
                "voe": nombre(r["nb_voe_pp"], "candidats en phase principale"),
                "voe_pc": nombre(r["nb_voe_pc"], "candidats en phase complementaire"),
                "cla": nombre(r["nb_cla_pp"], "classes"), "prop": nombre(r["prop_tot"], "propositions"),
                "acc": nombre(r["acc_tot"], "admis"), "gen": nombre(r["part_acces_gen"], "part bac general"),
                "tec": nombre(r["part_acces_tec"], "part bac technologique"),
                "pro": nombre(r["part_acces_pro"], "part bac professionnel")}
        if len(F) != len(lignes):       # entré == retenu : un code en double écraserait une formation en silence
            fail("%s : %d codes pour %d lignes (code de formation en double)" % (s["fichier"], len(F), len(lignes)))
        S[s["session"]] = F
    temoin = json.loads(octets("temoin.json").decode("utf-8"))
    return {"man": man, "ans": ans, "S": S, "temoin": temoin, "sums": sums}


# ------------------------------------------------------------------ calcul
def tranche_de(t: int) -> str:
    return next(cle for cle, bas, haut, _ in TRANCHES if bas <= t < haut)


def part(s, cond) -> float:
    if not s:
        fail("part sur un groupe vide : aucune valeur ne s'ecrit a la place")
    return 100.0 * sum(1 for p in s if cond(p)) / len(s)


def deciles(v) -> tuple:
    """1er décile, médiane, 9e décile : quantiles « inclusive » de Python (déclaré dans la note de méthode)."""
    q = st.quantiles(v, n=10, method="inclusive")
    return q[0], st.median(v), q[8]


def rangs(v) -> list:
    """Rangs moyens des ex aequo, pour la corrélation de Spearman."""
    compte, cumul, rang = Counter(v), 0, {}
    for x in sorted(compte):
        rang[x] = cumul + (compte[x] + 1) / 2
        cumul += compte[x]
    return [rang[x] for x in v]


def correlations(s) -> tuple:
    x, y = [p["t0"] for p in s], [p["t1"] for p in s]
    return st.correlation(x, y), st.correlation(rangs(x), rangs(y))


def apparier(a: dict, b: dict, classes: bool = True) -> tuple:
    """Protocole § 2. Rend les paires, le motif de chaque formation et le nombre de formations présentes l'une ou
    l'autre année. `classes=False` n'existe que pour la mutation de la garde 3."""
    paires, motifs = [], {}
    for k in sorted(set(a) | set(b)):
        if k not in a:
            motifs[k] = "nouvelle"
        elif k not in b:
            motifs[k] = "disparue"
        elif a[k]["lib"] != b[k]["lib"]:
            motifs[k] = "intitulé changé"
        elif a[k]["taux"] is None or b[k]["taux"] is None:
            motifs[k] = "taux absent"
        elif classes and (a[k]["cla"] == 0 or b[k]["cla"] == 0):
            motifs[k] = "aucun classé"
        else:
            motifs[k] = "appariée"
            paires.append({"k": k, "t0": a[k]["taux"], "t1": b[k]["taux"], "d": b[k]["taux"] - a[k]["taux"],
                           "c0": a[k]["capa"], "c1": b[k]["capa"], "v0": a[k]["voe"], "v1": b[k]["voe"],
                           "cla0": a[k]["cla"], "cla1": b[k]["cla"], "f0": a[k]["fili"], "f1": b[k]["fili"],
                           # Filière de la formation si le ministère la classe pareil les deux années ; sinon RECLASSEE.
                           # En 2024 seulement, 162 formations paramédicales (ergothérapeutes, orthophonistes, imagerie
                           # médicale…) sont rangées en IFSI ; avec la filière de l'année d'arrivée, la ligne IFSI mêlait
                           # deux populations (contrôleur indépendant, 11/11/2026).
                           "f": b[k]["fili"] if a[k]["fili"] == b[k]["fili"] else RECLASSEE})
    return paires, motifs, len(motifs)


def selection(a: dict, b: dict, motifs: dict) -> dict:
    """Test de sélection de l'appariement (protocole § 3, pièce 05) : chaque groupe à l'année de départ, les nouvelles
    à l'année d'arrivée."""
    out = {}
    for grp in ("appariée", "intitulé changé", "disparue", "aucun classé", "taux absent"):
        ks = [k for k, m in motifs.items() if m == grp]
        if not ks:
            continue
        taux = [a[k]["taux"] for k in ks if a[k]["taux"] is not None]
        capa = [a[k]["capa"] for k in ks if a[k]["capa"]]            # capacité nulle ou vide : hors de la médiane
        cand = [a[k]["voe"] for k in ks if a[k]["voe"] is not None]
        fil = Counter(a[k]["fili"] for k in ks)
        out[grp] = {"n": len(ks), "taux_med": st.median(taux) if taux else None,
                    "capa_med": st.median(capa) if capa else None, "cand_med": st.median(cand) if cand else None,
                    "part_cpge": 100.0 * fil["CPGE"] / len(ks), "part_bts": 100.0 * fil["BTS"] / len(ks),
                    "part_licence": 100.0 * fil["Licence"] / len(ks)}
    ks = [k for k, m in motifs.items() if m == "nouvelle"]
    if ks:
        taux = [b[k]["taux"] for k in ks if b[k]["taux"] is not None]
        fil = Counter(b[k]["fili"] for k in ks)
        out["nouvelle"] = {"n": len(ks), "taux_med": st.median(taux) if taux else None,
                           "part_cpge": 100.0 * fil["CPGE"] / len(ks), "part_bts": 100.0 * fil["BTS"] / len(ks),
                           "part_licence": 100.0 * fil["Licence"] / len(ks)}
    return out


def transition(X: dict, y0: int, y1: int, bornes_prec, classes: bool = True) -> dict:
    a, b = X["S"][y0], X["S"][y1]
    ps, motifs, total = apparier(a, b, classes)
    ecartees = Counter(m for m in motifs.values() if m != "appariée")
    med_fil = {f: st.median(p["d"] for p in ps if p["f"] == f) for f in {p["f"] for p in ps}}
    stable = [p for p in ps if p["c0"] and p["c1"] and abs(p["c1"] - p["c0"]) / p["c0"] <= SEUIL_CAPA]
    changee = [p for p in ps if p["c0"] and p["c1"] and abs(p["c1"] - p["c0"]) / p["c0"] > SEUIL_CAPA]

    tranches = {}
    for cle, _, _, _ in TRANCHES:
        s = [p for p in ps if tranche_de(p["t0"]) == cle]
        s50 = [p for p in s if p["v0"] is not None and p["v0"] >= SEUIL_CAND]
        sc = [p for p in stable if tranche_de(p["t0"]) == cle]
        d1, med, d9 = deciles([p["t1"] for p in s])
        c1, cm, c9 = deciles([p["t1"] for p in sc])
        t = {"n": len(s), "d1": d1, "mediane": med, "d9": d9,
             "reste_90": part(s, lambda p: p["t1"] >= SEUIL_RESTE), "n_reste_90": sum(1 for p in s if p["t1"] >= SEUIL_RESTE),
             "baisse_20": part(s, lambda p: p["d"] <= -SEUIL_BAISSE), "n_baisse_20": sum(1 for p in s if p["d"] <= -SEUIL_BAISSE),
             "perte_cinquieme": part(s, lambda p: p["t1"] <= 0.8 * p["t0"]),
             "dans_d1_d9": part(s, lambda p: d1 <= p["t1"] <= d9), "a_d1_ou_moins": part(s, lambda p: p["t1"] <= d1),
             "n_50cand": len(s50), "baisse_20_50cand": part(s50, lambda p: p["d"] <= -SEUIL_BAISSE),
             "baisse_20_corrigee": part(s, lambda p: p["d"] - med_fil[p["f"]] <= -SEUIL_BAISSE),
             "sans_capa": {"n": len(sc), "d1": c1, "mediane": cm, "d9": c9}}
        if bornes_prec is not None:
            bas, haut = bornes_prec[cle]
            t["couverture_bornes_precedentes"] = part(s, lambda p: bas <= p["t1"] <= haut)
        tranches[cle] = t

    filieres = {}
    par_fil = defaultdict(list)
    for p in ps:
        par_fil[p["f"]].append(p)
    recl = par_fil.pop(RECLASSEE, [])
    reclassees = {"n": len(recl), "variation_mediane": st.median(p["d"] for p in recl) if recl else None,
                  "detail": dict(sorted(Counter("%s → %s" % (p["f0"], p["f1"]) for p in recl).items()))}
    petites = {f: len(s) for f, s in par_fil.items() if len(s) < SEUIL_FILIERE}
    for f, s in par_fil.items():
        if len(s) < SEUIL_FILIERE:
            continue
        if any(p["v0"] is None or p["v1"] is None for p in s):
            fail("filiere %s : candidats absents pour une formation appariee (une mediane ne s'ecrit pas sur un trou)" % f)
        pe, sp = correlations(s)
        m = med_fil[f]
        filieres[f] = {"n": len(s), "pearson": pe, "spearman": sp, "variation_mediane": m,
                       # Trois résumés distincts d'une même baisse : médiane des variations, moyenne des variations, écart
                       # entre les taux médians (classes préparatoires 2024-2025 : −11, −14,9, 62 % → 43 %).
                       "variation_moyenne": st.mean(p["d"] for p in s),
                       "taux_med": [st.median(p["t0"] for p in s), st.median(p["t1"] for p in s)],
                       "part_mediane_ou_moins": part(s, lambda p: p["d"] <= m), "part_baisse": part(s, lambda p: p["d"] < 0),
                       "candidats_med": [st.median(p["v0"] for p in s), st.median(p["v1"] for p in s)],
                       "places_med": [st.median(p["c0"] for p in s if p["c0"]), st.median(p["c1"] for p in s if p["c1"])]}

    inter = [p for p in ps if 0 < p["t0"] < 100]
    pe, sp = correlations(ps)
    pi, si = correlations(inter)
    absmed = st.median(abs(p["d"]) for p in ps)
    lo20 = [p for p in ps if p["t0"] < SEUIL_SELECT]
    return {"de": y0, "a": y1, "cle": "%d-%d" % (y0, y1), "entrees": total, "appariees": len(ps),
            "ecartees": {m: ecartees.get(m, 0) for m in MOTIFS}, "tranches": tranches,
            "pearson": pe, "spearman": sp, "n_interieur": len(inter), "pearson_interieur": pi, "spearman_interieur": si,
            "variation_mediane": st.median(p["d"] for p in ps), "abs_mediane": absmed,
            "part_abs_mediane_ou_moins": part(ps, lambda p: abs(p["d"]) <= absmed),
            # Sens des variations de l'ensemble des appariées (pièce 06 : le recul d'ensemble se lit ici, pas dans une
            # lecture inversée des tranches) : parts en baisse, en hausse, inchangées, et variation moyenne.
            "part_baisse": part(ps, lambda p: p["d"] < 0), "part_hausse": part(ps, lambda p: p["d"] > 0),
            "part_inchangee": part(ps, lambda p: p["d"] == 0), "variation_moyenne": st.mean(p["d"] for p in ps),
            "capacite_changee_25": {"n": len(changee), "part": 100.0 * len(changee) / len(ps)},
            "contre_population": {"n": len(lo20), "atteint_40": sum(1 for p in lo20 if p["t1"] >= SEUIL_ATTEINT)},
            "filieres": filieres, "reclassees": reclassees, "petites_filieres": petites,
            "selection": selection(a, b, motifs), "_paires": ps}


def cohorte(T: list) -> dict:
    """Formations appariées aux DEUX dernières transitions : un ensemble strictement identique sur trois sessions, chacune
    portant ses deux variations successives (arbitrages des pièces 06 et 07). Répond à une seule question : le recul de
    la dernière transition subsiste-t-il quand on compare exactement les mêmes formations, avec et sans les classes
    préparatoires ? Il ne neutralise que le périmètre des formations comparées, pas la composition des candidats."""
    p, d = T[-2], T[-1]
    dp, dd = {x["k"]: x for x in p["_paires"]}, {x["k"]: x for x in d["_paires"]}
    ks = sorted(set(dp) & set(dd))

    def bloc(cles):
        a, b = [dp[k]["d"] for k in cles], [dd[k]["d"] for k in cles]
        return {"n": len(cles), "part_baisse": [part(a, lambda x: x < 0), part(b, lambda x: x < 0)],
                "part_hausse": [part(a, lambda x: x > 0), part(b, lambda x: x > 0)],
                "variation_moyenne": [st.mean(a), st.mean(b)], "variation_mediane": [st.median(a), st.median(b)]}

    def prepa(k):       # classe préparatoire à l'une au moins des trois sessions
        return "CPGE" in (dp[k]["f0"], dp[k]["f1"], dd[k]["f1"])

    return {"toutes": bloc(ks), "sans_cpge": bloc([k for k in ks if not prepa(k)])}


def calcul(X: dict, classes: bool = True) -> dict:
    T, bornes = [], None
    for y0, y1 in zip(X["ans"], X["ans"][1:]):
        t = transition(X, y0, y1, bornes, classes)
        bornes = {cle: (v["d1"], v["d9"]) for cle, v in t["tranches"].items()}
        T.append(t)
    der = X["ans"][-1]
    code = X["man"]["exemple"]["cod_aff_form"]
    e = X["S"][der].get(code)
    if e is None or any(e[k] is None for k in ("taux", "voe", "cla", "prop", "acc", "gen", "tec", "pro")):
        fail("exemple : formation %s absente ou incomplete dans la session %d" % (code, der))
    ex = dict(e, session=der, code=code, part_admis=100.0 * e["acc"] / e["voe"], part_propositions=100.0 * e["prop"] / e["voe"])
    return {"X": X, "T": T, "ex": ex, "cohorte": cohorte(T),
            "page": PAGE_MD.read_text(encoding="utf-8") if PAGE_MD.exists() else None}


# ------------------------------------------------------------------ gardes
def garde(G: list, cond: bool, phrase: str) -> None:
    G.append(phrase)
    if not cond:
        fail("garde : « %s » n'est plus soutenue par les donnees" % phrase)


def garde_1_conservation(c: dict) -> int:
    G = []
    for t in c["T"]:
        a, b = c["X"]["S"][t["de"]], c["X"]["S"][t["a"]]
        garde(G, t["entrees"] == len(set(a) | set(b)), "garde 1 (conservation) %s : entrees = formations presentes l'une ou l'autre annee" % t["cle"])
        garde(G, t["entrees"] == t["appariees"] + sum(t["ecartees"].values()),
              "garde 1 (conservation) %s : entrees = appariees + ecartees, motif par motif" % t["cle"])
        garde(G, t["appariees"] == len(t["_paires"]) == sum(v["n"] for v in t["tranches"].values()),
              "garde 1 (conservation) %s : chaque appariee est dans une tranche et une seule" % t["cle"])
        garde(G, set(t["ecartees"]) == set(MOTIFS) and all(v >= 0 for v in t["ecartees"].values()),
              "garde 1 (conservation) %s : chaque ecartee porte un motif nomme" % t["cle"])
    return len(G)


def garde_2_bornes(c: dict) -> int:
    G = []
    for an, F in c["X"]["S"].items():
        garde(G, all(r["taux"] is None or (isinstance(r["taux"], int) and 0 <= r["taux"] <= 100) for r in F.values()),
              "garde 2 (bornes) %d : tous les taux d'acces sont des entiers de 0 a 100" % an)
    return len(G)


def garde_3_aucun_classe(c: dict) -> int:
    G = []
    for t in c["T"]:
        garde(G, all(p["cla0"] != 0 and p["cla1"] != 0 for p in t["_paires"]),
              "garde 3 (aucun classe) %s : aucune formation sans candidat classe parmi les appariees" % t["cle"])
    return len(G)


def ecarts_temoin(mien, attendu, chemin: str = "") -> list:
    """Compare récursivement au témoin : comptes exacts, corrélations à 0,001, le reste à 0,1 point."""
    if isinstance(attendu, dict):
        if not isinstance(mien, dict):
            return ["%s : structure differente" % chemin]
        out = []
        for k, v in attendu.items():
            if k not in mien:
                out.append("%s/%s : absent du generateur" % (chemin, k))
            else:
                out += ecarts_temoin(mien[k], v, "%s/%s" % (chemin, k))
        return out
    if isinstance(attendu, list):
        if not isinstance(mien, list) or len(mien) != len(attendu):
            return ["%s : liste differente" % chemin]
        return [e for i, (m, a) in enumerate(zip(mien, attendu)) for e in ecarts_temoin(m, a, "%s[%d]" % (chemin, i))]
    if attendu is None or mien is None:
        return [] if attendu is mien else ["%s : %r contre %r au temoin" % (chemin, mien, attendu)]
    cle = chemin.rsplit("/", 1)[-1]
    tol = 0 if cle in COMPTES else TOLERANCE_CORR if ("pearson" in cle or "spearman" in cle) else TOLERANCE
    return [] if abs(mien - attendu) <= tol else ["%s : %s contre %s au temoin" % (chemin, mien, attendu)]


def temoin_de(c: dict, t: dict) -> dict:
    w = c["X"]["temoin"]["transitions"].get(t["cle"])
    if w is None:
        fail("garde 4 (temoin) : aucun temoin pour la transition %s ; relancer temoin_json.py du dossier de recherche, "
             "recopier temoin.json et son empreinte" % t["cle"])
    return w


def garde_5_reprise(c: dict) -> int:
    G = []
    for t in c["T"]:
        w = temoin_de(c, t)
        garde(G, (t["entrees"], t["appariees"]) == (w["entrees"], w["appariees"]),
              "garde 5 (reprise) %s : %d appariees sur %d, comme au temoin (%d sur %d)"
              % (t["cle"], t["appariees"], t["entrees"], w["appariees"], w["entrees"]))
    return len(G)


def garde_4_temoin(c: dict) -> int:
    G = []
    garde(G, len(c["X"]["temoin"]["transitions"]) == len(c["T"]), "garde 4 (temoin) : autant de transitions au temoin qu'au generateur")
    for t in c["T"]:
        w = temoin_de(c, t)
        mien = {k: v for k, v in t.items() if not k.startswith("_")}
        attendu = dict(w, ecartees={m: w["ecartees"].get(m, 0) for m in MOTIFS})
        inconnus = set(w["ecartees"]) - set(MOTIFS)
        ec = ecarts_temoin(mien, attendu) + ["motif inconnu au temoin : %s" % m for m in sorted(inconnus)]
        for nom in ("filieres", "selection"):
            en_trop = set(mien[nom]) - set(w[nom])
            ec += ["/%s/%s : absent du temoin" % (nom, k) for k in sorted(en_trop)]
        # Un indicateur ajouté au générateur sans l'être au témoin ne serait comparé à rien, en silence : il arrête.
        ec += ["/%s : absent du temoin" % k for k in sorted(set(mien) - set(w) - HORS_TEMOIN)]
        garde(G, not ec, "garde 4 (temoin) %s : deciles, parts et correlations egaux a ceux du temoin a %s point pres%s"
              % (t["cle"], TOLERANCE, " -- " + " ; ".join(ec[:4]) if ec else ""))
    w = c["X"]["temoin"].get("cohorte")
    ec = ["absente du temoin"] if w is None else ecarts_temoin(c["cohorte"], w) + [
        "/%s : absent du temoin" % k for k in sorted(set(c["cohorte"]) - set(w))]
    garde(G, not ec, "garde 4 (temoin) cohorte des trois sessions : effectifs, parts et moyennes egaux a ceux du temoin%s"
          % (" -- " + " ; ".join(ec[:4]) if ec else ""))
    return len(G)


def texte_nu(s: str) -> str:
    """Texte d'un fragment de page sans jetons, sans balises et sans entités : ce qui reste a été saisi."""
    s = re.sub(r"\{\{[<%].*?[%>]\}\}", " ", s, flags=re.S)       # shortcodes
    s = re.sub(r"\{[a-z_]+\.[a-z0-9_]+\}", " ", s)                # jetons du front matter
    s = re.sub(r"<[^>]+>", " ", s)                                # balises
    return re.sub(r"&[a-z]+;|&#\d+;", " ", s)                     # entités


def fragments_gardes(page: str) -> list:
    """Garde 6 : le résultat en une phrase, les textes alternatifs des figures et les réponses de la FAQ. Les
    QUESTIONS de la FAQ sont exemptées : une année de calendrier y est un mot de la question, pas une donnée."""
    out = [("resultat en une phrase", m) for m in re.findall(r'<div class="resultat-phrase">(.*?)</div>', page, flags=re.S)]
    out += [("texte alternatif d'une figure", m) for m in re.findall(r'<img\b[^>]*\balt="([^"]*)"', page, flags=re.S)]
    out += [("reponse de la FAQ", m) for m in re.findall(r'^\s+answer:\s*"(.*)"\s*$', page, flags=re.M)]
    return out


def garde_6_jetons(c: dict) -> int:
    G = []
    if c["page"] is None:
        return 0        # page non écrite : la garde s'applique dès qu'elle existe ; vue mordre par la mutation « jeton »
    fr = fragments_gardes(c["page"])
    garde(G, any(nom == "resultat en une phrase" for nom, _ in fr), "garde 6 (jetons) : la page porte un bloc « resultat en une phrase »")
    for nom, f in fr:
        saisi = re.findall(r"\d[\d   ,.]*", texte_nu(f))
        garde(G, not saisi, "garde 6 (jetons) : aucun nombre saisi dans %s%s" % (nom, " -- lu : " + ", ".join(saisi[:3]) if saisi else ""))
    return len(G)


def garde_8_prose(c: dict) -> int:
    G = []
    textes = list(c.get("A", {}).values()) + ([c["page"]] if c["page"] is not None else [])
    tout = " ".join(textes).replace(" ", " ").replace(" ", " ").replace("’", "'").lower()
    for motif in INTERDITES:
        garde(G, not re.search(motif, tout), "garde 8 (prose) : la formule retiree « %s » n'apparait pas" % motif)
    # La diversification ne s'écrit que comme recommandation de la plateforme (arbitrage de la pièce 05).
    fautives = [p.strip()[:80] for p in re.split(r"(?<=[.!?])\s+", texte_nu(tout)) if "diversifi" in p
                and not (("parcoursup" in p or "plateforme" in p) and "recommand" in p)]
    garde(G, not fautives, "garde 8 (prose) : la diversification n'est citee que comme recommandation de la plateforme%s"
          % (" -- " + fautives[0] if fautives else ""))
    return len(G)


def fractions_attendues(c: dict) -> list:
    """(jeton, part en %, fraction écrite) : les fractions du plan d'après le panel avant. Rôles p et d, jamais une année."""
    p, d = c["T"][-2], c["T"][-1]
    return [("p_t9099_reste_frac", p["tranches"]["90-99"]["reste_90"], "deux sur trois"),
            ("d_t9099_reste_frac", d["tranches"]["90-99"]["reste_90"], "un peu plus d'une sur deux"),
            ("p_t9099_b20_frac", p["tranches"]["90-99"]["baisse_20"], "une sur dix"),
            ("d_t9099_b20_frac", d["tranches"]["90-99"]["baisse_20"], "une sur cinq"),
            ("d_t6075_dans_frac", d["tranches"]["60-75"]["dans_d1_d9"], "huit sur dix"),
            ("p_t6075_dans_frac", p["tranches"]["60-75"]["dans_d1_d9"], "huit sur dix"),
            ("d_t6075_bas_frac", d["tranches"]["60-75"]["a_d1_ou_moins"], "une sur dix"),
            ("p_absmed_frac", p["part_abs_mediane_ou_moins"], "une formation sur deux"),
            ("d_absmed_frac", d["part_abs_mediane_ou_moins"], "une formation sur deux"),
            ("d_f_cpge_baisse_frac", d["filieres"]["CPGE"]["part_baisse"], "près de quatre sur cinq")]


def garde_9_fractions(c: dict) -> int:
    G = []
    for jeton, v, frac in fractions_attendues(c):
        bas, haut = FRACTIONS[frac]
        garde(G, bas <= v <= haut, "garde 9 (fractions) %s : « %s » vaut entre %s et %s %%, la part est de %.1f %%"
              % (jeton, frac, bas, haut, v))
    return len(G)


def garde_constats(c: dict) -> int:
    """Chaque qualificatif des constats de la fiche de conception, une condition. Comparaisons à la précision affichée."""
    G = []
    T, p, d = c["T"], c["T"][-2], c["T"][-1]
    for t in T:
        tr, cle = t["tranches"], t["cle"]
        garde(G, t["pearson"] >= 0.85 and t["spearman"] >= 0.85 and t["pearson_interieur"] >= 0.80,
              "%s : forte stabilite relative (correlation d'au moins 0,85, en valeurs comme en rangs ; 0,80 sans les taux de 0 et 100 %%)" % cle)
        garde(G, tr["90-99"]["reste_90"] > 50 and tr["100"]["reste_90"] > 50,
              "%s : au-dessus de 90 %%, plus d'une formation sur deux reste a 90 %% ou plus" % cle)
        garde(G, lg.depasse(tr["90-99"]["baisse_20"], tr["100"]["baisse_20"]) and lg.depasse(tr["100"]["reste_90"], tr["90-99"]["reste_90"]),
              "%s : les formations a 100 %% bougent moins que celles a 90-99 %%" % cle)
        cp = t["contre_population"]
        garde(G, 100.0 * cp["atteint_40"] / cp["n"] < 5, "%s : les formations tres selectives le restent (moins de 5 %% atteignent 40 %%)" % cle)
        pertes = {k: v["perte_cinquieme"] for k, v in tr.items()}
        autres = [v for k, v in pertes.items() if k not in ("90-99", "100")]
        garde(G, all(lg.depasse(v, pertes["90-99"]) and lg.depasse(v, pertes["100"]) for v in autres),
              "%s : en perte relative (un cinquieme du niveau), les tranches 90-99 %% et 100 %% sont les plus stables" % cle)
        garde(G, lg.depasse(tr["75-90"]["baisse_20"], tr["90-99"]["baisse_20"]),
              "%s : en points, la tranche 90-99 %% decroche moins que la tranche 75-90 %%" % cle)
        garde(G, all(abs(v["baisse_20_50cand"] - v["baisse_20"]) < 1 for k, v in tr.items() if k != "100"),
              "%s : sans les formations de moins de 50 candidats, les parts bougent de moins d'un point, sauf a 100 %%" % cle)
        garde(G, all(abs(v[q] - v["sans_capa"][q]) <= 1 for v in tr.values() for q in ("d1", "mediane", "d9")),
              "%s : sans les formations dont la capacite change de plus de 25 %%, les deciles bougent d'au plus un point" % cle)
        sel = t["selection"]
        garde(G, all(sel[g]["taux_med"] > sel["appariée"]["taux_med"] and sel[g]["capa_med"] < sel["appariée"]["capa_med"]
                     and sel[g]["cand_med"] < sel["appariée"]["cand_med"] for g in ("disparue", "intitulé changé")),
              "%s : les formations disparues ou renommees sont plus petites et plus accessibles que les formations suivies" % cle)
    for t in T:
        dans = {k: v["dans_d1_d9"] for k, v in t["tranches"].items()}
        garde(G, all(80 <= v <= 84.5 for k, v in dans.items() if k not in ("90-99", "100"))
              and all(88 <= dans[k] <= 92 for k in ("90-99", "100")),
              "%s, cle et note de la figure 1 : du 1er au 9e decile, au moins huit formations sur dix dans chaque tranche, "
              "neuf sur dix au-dessus de 90 %%" % t["cle"])
        garde(G, sum(v["n"] for v in t["filieres"].values()) + t["reclassees"]["n"] + sum(t["petites_filieres"].values()) == t["appariees"],
              "%s, filieres : appariees = filieres + reclassees + petites filieres" % t["cle"])
        garde(G, not t["petites_filieres"],
              "%s, figure 2 : aucune filiere de moins de cent formations n'est ecartee de la figure" % t["cle"])
        garde(G, t["reclassees"]["n"] < 0.02 * t["appariees"],
              "%s : les formations dont la filiere est reclassee restent marginales (moins de 2 %% des appariees)" % t["cle"])
    garde(G, p["abs_mediane"] == d["abs_mediane"], "la variation absolue mediane est la meme dans les deux transitions")
    garde(G, d["part_baisse"] > 50 and lg.depasse(d["part_baisse"], p["part_baisse"]) and lg.depasse(p["part_hausse"], d["part_hausse"])
          and d["variation_moyenne"] < p["variation_moyenne"] < 0.5 and d["variation_mediane"] < 0 == p["variation_mediane"],
          "recul d'ensemble dans la derniere transition : plus d'une formation sur deux en baisse, davantage que dans la "
          "precedente, ou la variation mediane etait nulle")
    for t in T:
        garde(G, abs(t["part_baisse"] + t["part_hausse"] + t["part_inchangee"] - 100) < 1e-9,
              "%s : en baisse + en hausse + inchangees = toutes les appariees" % t["cle"])
    coh = c["cohorte"]
    garde(G, all(v["part_baisse"][1] > 50 and lg.depasse(v["part_baisse"][1], v["part_baisse"][0])
                 and v["variation_moyenne"][1] < v["variation_moyenne"][0] for v in coh.values()),
          "cohorte des trois sessions : le recul subsiste sur les memes formations, avec et sans les classes preparatoires")
    garde(G, coh["sans_cpge"]["n"] < coh["toutes"]["n"] <= min(p["appariees"], d["appariees"]) and coh["toutes"]["n"] > 0.8 * p["appariees"],
          "cohorte des trois sessions : plus de huit appariees sur dix de la transition precedente s'y retrouvent")
    for k in ("40-60", "60-75", "75-90", "90-99"):
        garde(G, lg.depasse(d["tranches"][k]["baisse_20"], p["tranches"][k]["baisse_20"]),
              "tranche %s : les baisses de 20 points ou plus sont plus frequentes dans la derniere transition" % k)
    for k in ("60-75", "75-90", "90-99"):
        garde(G, lg.depasse(d["tranches"][k]["baisse_20_corrigee"], p["tranches"][k]["baisse_20_corrigee"]),
              "tranche %s : elles le restent apres correction par filiere (au-dessus de 60 %%)" % k)
    couv = [v["couverture_bornes_precedentes"] for v in d["tranches"].values()]
    garde(G, all(70 <= v <= 90 for v in couv), "validation hors echantillon : les bornes de la transition precedente couvrent de 70 a 90 %% des formations")
    fil = d["filieres"]
    garde(G, "CPGE" in fil and "Licence" in fil and "BTS" in fil and "BUT" in fil, "les quatre filieres nommees dans la page ont au moins cent formations")
    try:
        plus_forte = lg.extremum(sorted(fil), lambda f: fil[f]["variation_mediane"], 0, maxi=False, quoi="plus forte baisse mediane")
    except ValueError as e:
        fail("garde : « %s »" % e)
    garde(G, plus_forte == "CPGE" and fil["CPGE"]["variation_mediane"] < 0,
          "derniere transition : les classes preparatoires ont la plus forte baisse mediane")
    garde(G, fil["Licence"]["variation_mediane"] == 0, "derniere transition : la variation mediane des licences est nulle")
    garde(G, max(abs(v["variation_mediane"]) for v in p["filieres"].values()) <= 3,
          "transition precedente : aucune variation mediane par filiere ne depasse 3 points")
    garde(G, p["filieres"]["CPGE"]["pearson"] - fil["CPGE"]["pearson"] > 0.1 and min(p["filieres"]["Licence"]["pearson"], fil["Licence"]["pearson"]) >= 0.9,
          "classes preparatoires : le classement des formations se recompose (correlation en baisse de plus de 0,1), pas celui des licences")
    garde(G, fil["CPGE"]["candidats_med"][1] < fil["CPGE"]["candidats_med"][0] and fil["CPGE"]["places_med"][0] == fil["CPGE"]["places_med"][1],
          "classes preparatoires : la baisse se produit avec moins de candidats et autant de places (medianes)")
    return len(G)


GARDES = (("1", garde_1_conservation), ("2", garde_2_bornes), ("3", garde_3_aucun_classe), ("5", garde_5_reprise),
          ("4", garde_4_temoin), ("6", garde_6_jetons), ("9", garde_9_fractions), ("constats", garde_constats),
          ("8", garde_8_prose))


def gardes(c: dict, seule: str = "") -> int:
    return sum(f(c) for nom, f in GARDES if not seule or nom == seule)


# ------------------------------------------------------------------ mutations (chaque garde vue mordre)
PAGE_TEMOIN = ('---\ntitle: "page temoin"\nfaq:\n  - question: "Le taux de 2026 vaudra-t-il pour 2027 ?"\n'
               '    answer: "Rien ne le garantit : {psup.d_t6075_d1} a {psup.d_t6075_d9}."\n---\n'
               '<div class="resultat-phrase">\n\n**Le résultat en une phrase.** Parmi les formations à '
               '{{< psup-val "d_t6075_lib" >}}, {{< psup-val "d_t6075_dans_frac" >}} se situaient entre '
               '{{< psup-val "d_t6075_d1" >}} et {{< psup-val "d_t6075_d9" >}}&nbsp;%.\n\n</div>\n'
               "Parcoursup recommande de diversifier ses vœux.\n")
# nom : (garde visée, fragment attendu dans le message de la garde, commentaire)
MUTATIONS = {
    "empreinte": ("7", "garde 7 (empreintes)", "un export ne rend plus son empreinte"),
    "bornes": ("2", "garde 2 (bornes)", "un taux de 101 dans la dernière session"),
    "conservation": ("1", "garde 1 (conservation)", "une écartée de trop : entrées ≠ appariées + écartées"),
    "aucunclasse": ("3", "garde 3 (aucun classe)", "le motif « aucun classé » désactivé : formations à 0 % sans classé appariées"),
    "temoin": ("4", "garde 4 (temoin)", "un 9e décile décalé d'un point"),
    "reprise": ("5", "garde 5 (reprise)", "le témoin attend 200 appariées de plus"),
    "jeton": ("6", "garde 6 (jetons)", "un nombre saisi dans le résultat en une phrase"),
    "jetonfaq": ("6", "garde 6 (jetons)", "un nombre saisi dans une réponse de la FAQ"),
    "prose": ("8", "garde 8 (prose)", "la formule « ne fluctuent pas au hasard » dans la page"),
    "diversification": ("8", "diversification", "un conseil de diversification en nom propre"),
    "fraction": ("9", "garde 9 (fractions)", "45 % écrit « un peu plus d'une sur deux »"),
    "stabilite": ("constats", "forte stabilite relative", "corrélation de la dernière transition à 0,70"),
    "conseil": ("constats", "plus d'une formation sur deux reste", "45 % seulement des 90-99 % restent à 90 % ou plus"),
    "recul": ("constats", "recul d'ensemble", "autant de formations en baisse dans la dernière transition que dans la précédente"),
    "cohorte": ("constats", "le recul subsiste sur les memes formations", "sans les classes préparatoires, autant de baisses qu'avant"),
    "temoincohorte": ("4", "cohorte des trois sessions", "une formation de moins dans la cohorte que dans le témoin"),
    "huitsurdix": ("constats", "au moins huit formations sur dix", "79 % seulement des formations entre les deux déciles (60-74 %)"),
    "plussouvent": ("8", "le plus souvent", "la formule « le plus souvent » dans la page"),
    "cent": ("constats", "bougent moins", "les formations à 100 % décrochent plus que les 90-99 %"),
    "selectives": ("constats", "tres selectives", "300 formations très sélectives passent 40 %"),
    "relatif": ("constats", "en perte relative", "la tranche 40-60 % devient la plus stable en perte relative"),
    "decroche": ("constats", "decroche moins", "la tranche 90-99 % décroche plus que la tranche 75-90 %"),
    "petites": ("constats", "moins de 50 candidats", "sans les petites formations, une part bouge de trois points"),
    "capacite": ("constats", "capacite change", "sans les capacités changées, un décile bouge de cinq points"),
    "selection": ("constats", "plus petites et plus accessibles", "les formations disparues deviennent moins accessibles"),
    "absmed": ("constats", "variation absolue mediane", "8 points dans la dernière transition"),
    "frequentes": ("constats", "plus frequentes", "moins de baisses dans la dernière transition (40-60 %)"),
    "corrigee": ("constats", "correction par filiere", "après correction, la tranche 75-90 % ne décroche plus davantage"),
    "validation": ("constats", "validation hors echantillon", "couverture de 50 % dans une tranche"),
    "filiere": ("constats", "plus forte baisse mediane", "les BTS baissent plus que les classes préparatoires"),
    "licence": ("constats", "licences est nulle", "variation médiane des licences à −2"),
    "troispoints": ("constats", "ne depasse 3 points", "une filière à −5 dans la transition précédente"),
    "recompose": ("constats", "se recompose", "corrélation des classes préparatoires inchangée"),
    "candidats": ("constats", "moins de candidats", "candidats médians des classes préparatoires en hausse"),
    "deciles": ("constats", "note de la figure 1", "70 % seulement des formations entre les deux déciles (40-60 %)"),
    "echelle": ("figures", "hors de l'echelle", "une variation médiane de −14 points, hors de l'échelle de la figure 2"),
    "parite": ("figures", "valeurs dessinées absentes", "la version téléphone affiche une valeur absente de la version détaillée"),
}


def muter(c: dict, m: str) -> None:
    """Altère le calcul pour qu'UNE condition devienne fausse. Rien n'est écrit en mode mutation."""
    p, d = c["T"][-2], c["T"][-1]
    tr = d["tranches"]

    def tranche(k, **v):
        tr[k] = dict(tr[k], **v)

    if m == "conservation":
        d["ecartees"] = dict(d["ecartees"], nouvelle=d["ecartees"]["nouvelle"] + 1)
    elif m == "temoin":
        tranche("60-75", d9=tr["60-75"]["d9"] + 1)
    elif m == "reprise":
        w = c["X"]["temoin"]["transitions"]
        w[d["cle"]] = dict(w[d["cle"]], appariees=w[d["cle"]]["appariees"] + 200)
    elif m == "jeton":
        c["page"] = PAGE_TEMOIN.replace('{{< psup-val "d_t6075_d1" >}} et', "43 et")
    elif m == "jetonfaq":
        c["page"] = PAGE_TEMOIN.replace("{psup.d_t6075_d1}", "43")
    elif m == "prose":
        c["page"] = PAGE_TEMOIN + "Les taux d'accès ne fluctuent pas au hasard d'une année à l'autre.\n"
    elif m == "diversification":
        c["page"] = PAGE_TEMOIN + "Il faut diversifier ses vœux entre filières.\n"
    elif m == "fraction":
        tranche("90-99", reste_90=45.0)
    elif m == "stabilite":
        d["pearson"] = 0.70
    elif m == "conseil":
        tranche("90-99", reste_90=45.0)
    elif m == "cent":
        tranche("100", baisse_20=tr["90-99"]["baisse_20"] + 5)
    elif m == "selectives":
        d["contre_population"] = dict(d["contre_population"], atteint_40=300)
    elif m == "relatif":
        tranche("40-60", perte_cinquieme=1.0)
    elif m == "decroche":
        tranche("90-99", baisse_20=tr["75-90"]["baisse_20"] + 5)
    elif m == "petites":
        tranche("60-75", baisse_20_50cand=tr["60-75"]["baisse_20"] + 3)
    elif m == "capacite":
        tranche("60-75", sans_capa=dict(tr["60-75"]["sans_capa"], d1=tr["60-75"]["d1"] + 5))
    elif m == "selection":
        d["selection"] = dict(d["selection"], disparue=dict(d["selection"]["disparue"], taux_med=40.0))
    elif m == "absmed":
        d["abs_mediane"] = 8.0
    elif m == "frequentes":     # les deux parts ensemble : sinon la sensibilité aux petites formations mordrait d'abord
        x = p["tranches"]["40-60"]["baisse_20"] - 1
        tranche("40-60", baisse_20=x, baisse_20_50cand=x)
    elif m == "corrigee":
        tranche("75-90", baisse_20_corrigee=p["tranches"]["75-90"]["baisse_20_corrigee"] - 1)
    elif m == "validation":
        tranche("75-90", couverture_bornes_precedentes=50.0)
    elif m in ("filiere", "licence", "recompose", "candidats"):
        f = dict(d["filieres"])
        if m == "filiere":
            f["BTS"] = dict(f["BTS"], variation_mediane=f["CPGE"]["variation_mediane"] - 4)
        elif m == "licence":
            f["Licence"] = dict(f["Licence"], variation_mediane=-2.0)
        elif m == "recompose":
            f["CPGE"] = dict(f["CPGE"], pearson=p["filieres"]["CPGE"]["pearson"])
        else:
            f["CPGE"] = dict(f["CPGE"], candidats_med=[f["CPGE"]["candidats_med"][0], f["CPGE"]["candidats_med"][0] + 50])
        d["filieres"] = f
    elif m == "deciles":
        tranche("40-60", dans_d1_d9=70.0)
    elif m == "huitsurdix":
        tranche("60-75", dans_d1_d9=79.0)
    elif m == "recul":
        d["part_baisse"] = p["part_baisse"]
    elif m == "cohorte":
        v = c["cohorte"]["sans_cpge"]
        c["cohorte"] = dict(c["cohorte"], sans_cpge=dict(v, part_baisse=[v["part_baisse"][0], v["part_baisse"][0]]))
    elif m == "temoincohorte":
        v = c["cohorte"]["toutes"]
        c["cohorte"] = dict(c["cohorte"], toutes=dict(v, n=v["n"] - 1))
    elif m == "plussouvent":
        c["page"] = PAGE_TEMOIN + "Au-dessus de 90 %, le taux tient le plus souvent.\n"
    elif m == "echelle":
        f = dict(d["filieres"])
        f["CPGE"] = dict(f["CPGE"], variation_mediane=-14.0)
        d["filieres"] = f
    elif m == "troispoints":
        f = dict(p["filieres"])
        f["BUT"] = dict(f["BUT"], variation_mediane=-5.0)
        p["filieres"] = f


def jouer_mutation(m: str) -> bool:
    """Vrai si la garde VISÉE a mordu (et pas une autre)."""
    if m not in MUTATIONS:
        fail("mutation inconnue %s (connues : %s)" % (m, ", ".join(MUTATIONS)))
    cible, attendu, quoi = MUTATIONS[m]
    try:
        X = lire(m)
        c = calcul(X, classes=(m != "aucunclasse"))
        if cible in ("6", "8") and c["page"] is None:
            c["page"] = PAGE_TEMOIN
        muter(c, m)
        if cible in ("8", "9"):
            c["A"] = affichage(c) if cible == "8" else {}
        if cible == "figures":
            figures(c, affichage(c), fausse=(m == "parite"))
        else:
            gardes(c, cible)
    except Arret as e:
        if attendu in e.msg:
            log("mutation %s (%s) : la garde %s a mordu (attendu)." % (m, quoi, cible))
            return True
        log("mutation %s : une AUTRE garde a mordu : %s" % (m, e.msg))
        return False
    log("mutation %s (%s) : AUCUNE garde n'a mordu." % (m, quoi))
    return False


# ------------------------------------------------------------------ affichage (jetons)
def arrondi(v: float, dec: int) -> float:
    """Arrondi commercial (0,5 vers le haut) avant lg.nombre, qui arrondit au pair. Même geste que
    update_malaise_etudiant.py. Condition de mort : langue_generee.nombre arrondit lui-même 0,5 vers le haut."""
    return float(Decimal(repr(float(v))).quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP))


def n0(v) -> str:
    return lg.nombre(arrondi(v, 0), 0)


def n1(v) -> str:
    return lg.nombre(arrondi(v, 1), 1)


def n2(v) -> str:
    return lg.nombre(arrondi(v, 2), 2)


def nmed(v) -> str:
    """Médiane d'effectifs ou de taux : entière le plus souvent, parfois à la demie (« 993,5 ») ; jamais « 418,0 »."""
    return n0(v) if float(v) == int(v) else n1(v)


def jeton_filiere(f: str) -> str:
    return JETON_FILIERE.get(f) or re.sub(r"[^a-z0-9]", "", f.lower())


def affichage(c: dict) -> dict:
    X, T, ex = c["X"], c["T"], c["ex"]
    ans = X["ans"]
    A = {"sessions": lg.enumere([str(a) for a in ans]), "n_sessions": lg.lettres(len(ans)),
         "s_premiere": str(ans[0]), "s_derniere": str(ans[-1]),
         "seuil_reste": n0(SEUIL_RESTE), "seuil_baisse_pts": lg.points(SEUIL_BAISSE, 0), "seuil_select": n0(SEUIL_SELECT),
         "seuil_atteint": n0(SEUIL_ATTEINT), "seuil_cand": n0(SEUIL_CAND), "seuil_capa": n0(100 * SEUIL_CAPA)}
    for role, t in (("p", T[-2]), ("d", T[-1])):
        r = role + "_"
        A.update({r + "de": str(t["de"]), r + "a": str(t["a"]), r + "n": n0(t["appariees"]), r + "entrees": n0(t["entrees"]),
                  r + "ecartees": n0(sum(t["ecartees"].values())), r + "part_app": n1(100.0 * t["appariees"] / t["entrees"]),
                  r + "pearson": n2(t["pearson"]), r + "spearman": n2(t["spearman"]),
                  r + "pearson_int": n2(t["pearson_interieur"]), r + "spearman_int": n2(t["spearman_interieur"]),
                  r + "absmed": n0(t["abs_mediane"]), r + "absmed_pts": lg.points(arrondi(t["abs_mediane"], 0), 0),
                  r + "part_absmed": n1(t["part_abs_mediane_ou_moins"]),
                  r + "varmed": lg.signe(arrondi(t["variation_mediane"], 0), 0),
                  r + "varmoy": lg.signe(arrondi(t["variation_moyenne"], 1), 1),
                  r + "baisse": n1(t["part_baisse"]), r + "hausse": n1(t["part_hausse"]), r + "egal": n1(t["part_inchangee"]),
                  r + "capa_n": n0(t["capacite_changee_25"]["n"]), r + "capa_part": n1(t["capacite_changee_25"]["part"]),
                  r + "cp_n": n0(t["contre_population"]["atteint_40"]), r + "cp_tot": n0(t["contre_population"]["n"])})
        A[r + "recl_n"] = n0(t["reclassees"]["n"])
        if t["reclassees"]["variation_mediane"] is not None:
            A[r + "recl_med_pts"] = lg.points(arrondi(t["reclassees"]["variation_mediane"], 0), 0, signe_=True)
        for m in MOTIFS:
            A[r + "m_" + JETON_MOTIF[m]] = n0(t["ecartees"][m])
        for cle, _, _, lib in TRANCHES:
            v, j = t["tranches"][cle], r + JETON_TRANCHE[cle] + "_"
            A.update({j + "lib": lib.replace(" %", lg.NBSP + "%"), j + "court": COURT_TRANCHE[cle].replace(" %", lg.NBSP + "%"),
                      j + "n": n0(v["n"]), j + "d1": n0(v["d1"]), j + "med": n0(v["mediane"]),
                      j + "d9": n0(v["d9"]), j + "reste": n1(v["reste_90"]), j + "reste_n": n0(v["n_reste_90"]),
                      j + "b20": n1(v["baisse_20"]), j + "b20_n": n0(v["n_baisse_20"]), j + "cinq": n1(v["perte_cinquieme"]),
                      j + "dans": n1(v["dans_d1_d9"]), j + "bas": n1(v["a_d1_ou_moins"]),
                      j + "n50": n0(v["n_50cand"]), j + "b20_50": n1(v["baisse_20_50cand"]), j + "b20_cor": n1(v["baisse_20_corrigee"])})
            if "couverture_bornes_precedentes" in v:
                A[j + "val"] = n1(v["couverture_bornes_precedentes"])
            # Le lecteur refait la part à partir des deux effectifs imprimés : il doit retrouver celle qui est imprimée.
            for num, part_, quoi in ((v["n_reste_90"], v["reste_90"], "reste a 90 % ou plus"), (v["n_baisse_20"], v["baisse_20"], "baisse de 20 points")):
                if n1(100.0 * num / v["n"]) != n1(part_):
                    fail("%s %s (%s) : %d sur %d ne redonne pas %s %%" % (t["cle"], cle, quoi, num, v["n"], n1(part_)))
        meds = {f: v["variation_mediane"] for f, v in t["filieres"].items()}
        A.update({r + "f_min": lg.signe(arrondi(min(meds.values()), 0), 0), r + "f_max": lg.signe(arrondi(max(meds.values()), 0), 0),
                  r + "f_absmax": n0(max(abs(x) for x in meds.values())),
                  r + "f_absmax_pts": lg.points(arrondi(max(abs(x) for x in meds.values()), 0), 0),
                  r + "f_nb": lg.lettres(len(meds))})
        for f, v in t["filieres"].items():
            j = r + "f_" + jeton_filiere(f) + "_"
            A.update({j + "n": n0(v["n"]), j + "med": lg.signe(arrondi(v["variation_mediane"], 0), 0),
                      j + "med_pts": lg.points(arrondi(v["variation_mediane"], 0), 0, signe_=True),
                      j + "exemple": "par exemple, de 45" + lg.NBSP + "% à " + n0(45 + v["variation_mediane"]) + lg.NBSP + "%",
                      j + "perte_pts": lg.points(arrondi(abs(v["variation_mediane"]), 0), 0), j + "baisse": n1(v["part_baisse"]),
                      j + "moy": lg.signe(arrondi(v["variation_moyenne"], 1), 1), j + "taux0": nmed(v["taux_med"][0]),
                      j + "taux1": nmed(v["taux_med"][1]),
                      j + "pearson": n2(v["pearson"]), j + "spearman": n2(v["spearman"]),
                      j + "cand0": nmed(v["candidats_med"][0]), j + "cand1": nmed(v["candidats_med"][1]),
                      j + "places0": n0(v["places_med"][0]), j + "places1": n0(v["places_med"][1])})
        for g, v in t["selection"].items():
            j = r + "sel_" + JETON_MOTIF[g] + "_"
            A.update({j + "n": n0(v["n"]), j + "bts": n0(v["part_bts"]), j + "cpge": n1(v["part_cpge"]), j + "licence": n0(v["part_licence"])})
            for k, cle_ in (("taux_med", "taux"), ("capa_med", "capa"), ("cand_med", "cand")):
                if v.get(k) is not None:
                    A[j + cle_] = nmed(v[k])
    p, d = T[-2], T[-1]
    couv = [v["couverture_bornes_precedentes"] for v in d["tranches"].values()]
    dans = [v["dans_d1_d9"] for v in p["tranches"].values()]
    rapports = [d["tranches"][k]["baisse_20"] / p["tranches"][k]["baisse_20"] for k in ("40-60", "60-75", "75-90", "90-99")]
    groupes = [t["selection"][g] for t in (p, d) for g in ("disparue", "intitulé changé")]
    A.update({"val_min": n0(min(couv)), "val_max": n0(max(couv)), "val_ref_min": n0(min(dans)), "val_ref_max": n0(max(dans)),
              "b20_rapport_min": n1(min(rapports)), "b20_rapport_max": n1(max(rapports)),
              "sel_taux_min": n0(min(g["taux_med"] for g in groupes)), "sel_taux_max": n0(max(g["taux_med"] for g in groupes)),
              "sel_capa_min": n0(min(g["capa_med"] for g in groupes)), "sel_capa_max": n0(max(g["capa_med"] for g in groupes)),
              "sel_cand_min": n0(min(g["cand_med"] for g in groupes)), "sel_cand_max": n0(max(g["cand_med"] for g in groupes)),
              "ex_session": str(ex["session"]), "ex_etab": ex["etab"], "ex_formation": ex["lib"], "ex_taux": n0(ex["taux"]),
              "ex_cand": n0(ex["voe"]), "ex_cla": n0(ex["cla"]), "ex_prop": n0(ex["prop"]), "ex_adm": n0(ex["acc"]),
              "ex_capa": n0(ex["capa"]), "ex_adm_part": n1(ex["part_admis"]), "ex_prop_part": n1(ex["part_propositions"]),
              "ex_gen": n0(ex["gen"]), "ex_tec": n0(ex["tec"]), "ex_pro": n0(ex["pro"])})
    if n1(100.0 * arrondi(ex["acc"], 0) / arrondi(ex["voe"], 0)) != A["ex_adm_part"]:
        fail("exemple : %s sur %s ne redonne pas %s %%" % (A["ex_adm"], A["ex_cand"], A["ex_adm_part"]))
    for nom, v in (("coh_", c["cohorte"]["toutes"]), ("coh_sc_", c["cohorte"]["sans_cpge"])):
        A.update({nom + "n": n0(v["n"]), nom + "p_baisse": n1(v["part_baisse"][0]), nom + "d_baisse": n1(v["part_baisse"][1]),
                  nom + "p_varmoy": lg.signe(arrondi(v["variation_moyenne"][0], 1), 1),
                  nom + "d_varmoy": lg.signe(arrondi(v["variation_moyenne"][1], 1), 1)})
    for jeton, _, frac in fractions_attendues(c):
        A[jeton] = frac
    return A


# ------------------------------------------------------------------ figures
# Charte de l'auteur (mémoire feedback_langage_graphique_figures) : bleu profond = la série principale, ici la DERNIÈRE
# transition ; gris = le contexte, ici la transition précédente ; une seule couleur de données. Étiquetage direct, valeurs
# de la série principale seulement dans la figure 1 (celles de la précédente se lisent sur l'échelle, dans la description
# et dans le CSV). Les deux figures sont des barres ou des points HORIZONTAUX : la grille suit l'axe des valeurs, donc
# verticale (écart déclaré à « grille horizontale seule », écrite pour des séries en ordonnée). Figures statiques.
# Contrôle : skill controle-figures, verrou scripts/check-figures.py. Corrections du 11/11/2026 après deux contrôleurs
# indépendants : note de la figure 1 réécrite en exemple de lecture (elle se lisait « huit formations sur dix ont un taux
# sous 90 % »), libellés de tranche à bornes entières, en-têtes vrais pour les deux séries, unité de la figure 2.
# Corrections du même jour après la contre-expertise externe (pièce 06) : clé de la figure 1 (« au moins huit formations
# sur dix », vrai des sept tranches, gardé ; la bande n'est plus dite « taux inchangé ») ; gris des séries secondaires
# ramené au gris des autres figures du site (#8a8781 : 3,6 pour 1 sur blanc, contre 2,9 pour #9a968f, sous le seuil de
# 3 pour 1 d'une marque graphique) ; barre grise détourée de blanc là où elle passe sur la bande (2,7 pour 1 sans cela).
W = 720
FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
BLEU, GRIS = "#184f95", "#8a8781"
INK, INK2, MUTED, GRID, BANDE, LIEN = "#26262f", "#55524f", "#96928f", "#dcd8d3", "#e4dfd7", "#cfcac3"
FS_MIN = pied_figure.POLICE_M
LIC_FIG = "Calcul Stéphane Lalut, licence CC BY 4.0 · " + PAGE_URL
LIC_FIG_M = "Calcul Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"
TRANCHE_RESULTAT = "60-75"      # la tranche de la phrase de résultat : ses valeurs sont en ancrage dans la figure 1
NOM_FILIERE = {"CPGE": "Classes préparatoires", "BTS": "BTS", "BUT": "BUT", "Licence": "Licences (hors accès santé)",
               "Licence_Las": "Licences accès santé (L.AS)", "PASS": "Parcours accès santé (PASS)",
               "IFSI": "Soins infirmiers (IFSI)", "EFTS": "Travail social (EFTS)", "Ecole d'Ingénieur": "Écoles d'ingénieurs",
               "Ecole de Commerce": "Écoles de commerce", "Autre formation": "Autres formations"}
ECHELLE_FILIERES = (-15, 3)     # points ; une médiane hors de l'échelle arrête la génération
SOURCE_FIG = ("Ministère chargé de l'enseignement supérieur, données ouvertes Parcoursup, sessions {sessions} ; formations "
              "présentes deux années de suite sous le même code et le même intitulé, avec un taux d'accès publié et des "
              "candidats classés. Taux d'accès : part des candidats de la phase principale dont le rang de classement ne "
              "dépasse pas celui du dernier appelé de leur groupe.")
FIG = {
    "tranches": dict(
        titre="Comment les taux d'accès évoluent-ils d'une année sur l'autre ?",
        sous_titre="Taux d'accès l'année suivante, selon le taux de l'année de départ, toutes filières confondues",
        source=SOURCE_FIG,
        note="Lecture de la ligne « {d_t6075_lib} » : parmi les {d_t6075_n} formations à ce taux d'accès en {d_de}, "
             "{d_t6075_dans_frac} avaient en {d_a} un taux compris entre {d_t6075_d1}~et~{d_t6075_d9} % ; "
             "{d_t6075_bas_frac} était à {d_t6075_d1} % ou moins, une sur deux à {d_t6075_med} % ou moins (la médiane). "
             "Dans les deux tranches du haut, la barre touche 100 %, le maximum, et contient neuf formations sur dix. Ces "
             "barres décrivent ce qui est arrivé aux formations d'une tranche, prises ensemble : elles ne donnent ni le "
             "taux futur d'une formation, ni les chances d'un candidat.",
        source_m="Ministère chargé de l'enseignement supérieur, données ouvertes Parcoursup, sessions {s_premiere} à {s_derniere}",
        note_m="Lecture de la ligne « {d_t6075_lib} » : parmi les formations à ce taux en {d_de}, {d_t6075_dans_frac} "
               "avaient en {d_a} un taux compris entre {d_t6075_d1}~et~{d_t6075_d9} % ; {d_t6075_bas_frac} était à "
               "{d_t6075_d1} % ou moins, une sur deux à {d_t6075_med} % ou moins (la médiane). Dans les deux tranches du "
               "haut, la barre touche 100 %, le maximum, et contient neuf formations sur dix. Ces barres décrivent le "
               "passé, pas le taux futur d'une formation ni les chances d'un candidat.",
        montre="Un taux d'accès n'est pas une promesse pour l'année suivante : parmi les formations à {d_t6075_court} en "
               "{d_de}, {d_t6075_dans_frac} se situaient entre {d_t6075_d1} et {d_t6075_d9} % en {d_a} (médiane : "
               "{d_t6075_med} %)."),
    "filieres": dict(
        titre="Variation médiane du taux d'accès selon la filière",
        sous_titre="D'une année à la suivante, en points de pourcentage",
        source=SOURCE_FIG,
        note="Lecture : une médiane de {d_f_cpge_med_pts} signifie que la moitié des classes préparatoires ont perdu "
             "{d_f_cpge_perte_pts} de taux d'accès ou plus ; un taux qui perd {d_f_cpge_perte_pts} passe, {d_f_cpge_exemple}. "
             "Une médiane nulle ne veut pas dire que chaque formation est restée stable. Les deux points d'une filière ne "
             "portent pas tout à fait sur les mêmes formations ; les {d_recl_n} formations que le ministère a classées "
             "dans une autre filière d'une session à l'autre ne sont pas dessinées. Ces données ne disent ni la cause "
             "d'une baisse, ni si elle se reproduira, ni les chances d'un candidat.",
        source_m="Ministère chargé de l'enseignement supérieur, données ouvertes Parcoursup, sessions {s_premiere} à {s_derniere}",
        note_m="Lecture : {d_f_cpge_med_pts} signifie que la moitié des classes préparatoires ont perdu "
               "{d_f_cpge_perte_pts} de taux d'accès ou plus ({d_f_cpge_exemple}). Une médiane nulle ne veut pas dire que "
               "chaque formation est restée stable. Les deux points d'une filière ne portent pas tout à fait sur les "
               "mêmes formations ; les {d_recl_n} que le ministère a classées dans une autre filière ne sont pas "
               "dessinées. Ces données ne disent ni la cause d'une baisse, ni si elle se reproduira, ni les chances d'un "
               "candidat.",
        montre="De {d_de} à {d_a}, la moitié des classes préparatoires ont perdu {d_f_cpge_perte_pts} de taux d'accès ou "
               "plus ; la variation médiane est de {d_f_bts_med_pts} en BTS, de {d_f_but_med_pts} en BUT, et nulle en licence. "
               "De {p_de} à {p_a}, elle ne dépassait {p_f_absmax_pts} dans aucune filière."),
}


def esc(s: str) -> str:
    """Échappe, après avoir soudé la ponctuation haute et le signe « % » à ce qui les précède (règle typographique du
    site, valable aussi dans une image)."""
    return html.escape(re.sub(" ([:;?!%»])", lg.NBSP + r"\1", s), quote=False)


def textes(cle: str, A: dict) -> dict:
    """« ~ » dans un texte de FIG = espace insécable écrite en clair (« entre 43 et 83 % » ne se coupe pas)."""
    return {k: v.replace("~", lg.NBSP).format(**A) for k, v in FIG[cle].items()}


def largeur(txt: str, taille, gras: bool = False) -> float:
    """Chasse approchée d'un texte (le verrou check-figures.py la mesure à la police réelle)."""
    return (0.60 if gras else 0.56) * float(taille) * len(txt)


def valeur(x: float, y: float, taille, col: str, txt: str, ancre: str = "middle", gras: bool = False) -> str:
    """Étiquette de valeur sur un liseré blanc (copie aria-hidden dessous) : une ligne de grille ou une bande qui passe
    sous les chiffres ne les coupe pas (même organe que update_malaise_etudiant.py)."""
    att = 'x="%.1f" y="%.1f" font-size="%s"%s text-anchor="%s"' % (x, y, taille, ' font-weight="600"' if gras else "", ancre)
    return ('<text aria-hidden="true" %s fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">%s</text>'
            '<text %s fill="%s">%s</text>' % (att, esc(txt), att, col, esc(txt)))


def ouvre(ident: str, titre: str, sous_titre: str, desc: str) -> list:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, ident, ident, esc(FONT)),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="0" fill="#ffffff"/>' % W,
            '<text x="0" y="18" font-size="14" font-weight="600" fill="%s">%s</text>' % (INK, esc(titre)),
            '<text x="0" y="37" font-size="11" fill="%s">%s</text>' % (INK2, esc(sous_titre))]


def bornes_bande(cle: str) -> tuple:
    """Étendue de la tranche de départ sur l'axe des taux, bornes entières incluses (les taux sont des entiers)."""
    bas, haut = next((b, h) for k, b, h, _ in TRANCHES if k == cle)
    return (bas, haut - 1)


def desc_tranches(c: dict, A: dict) -> str:
    out = ["Pour chaque tranche de taux d'accès une année, intervalle du 1er au 9e décile et médiane du taux d'accès des "
           "mêmes formations l'année suivante : de %s à %s, puis de %s à %s (autres formations, autres effectifs)."
           % (A["d_de"], A["d_a"], A["p_de"], A["p_a"])]
    for cle, _, _, lib in reversed(TRANCHES):
        j = JETON_TRANCHE[cle]
        out.append("%s en %s (%s formations) : en %s, de %s à %s %%, médiane %s %%. %s en %s (%s formations) : en %s, de %s à "
                   "%s %%, médiane %s %%."
                   % (lib.capitalize(), A["d_de"], A["d_%s_n" % j], A["d_a"], A["d_%s_d1" % j], A["d_%s_d9" % j], A["d_%s_med" % j],
                      lib.capitalize(), A["p_de"], A["p_%s_n" % j], A["p_a"], A["p_%s_d1" % j], A["p_%s_d9" % j], A["p_%s_med" % j]))
    return " ".join(out)


def cle_tranches(e: list, y: float, A: dict, taille, mobile: bool = False) -> float:
    """Clé des trois marques. Bureau : deux lignes (série principale, puis les deux repères). Téléphone : une entrée
    par ligne, coupée dans 300 de large. Rend l'ordonnée de la dernière ligne écrite."""
    # « Au moins huit formations sur dix » : vrai des sept tranches (neuf sur dix dans les deux du haut, que la note
    # explique), condition gardée. La bande situe la tranche de départ sur l'échelle : une formation peut y rester en
    # ayant changé de taux, elle ne se dit donc pas « taux inchangé » (pièce 06).
    # Bureau et téléphone disent la même chose : la barre CONTIENT au moins huit formations sur dix (le mot « décile »
    # passe en parenthèse ; « la barre va du … au … » se lisait comme un trajet). Sur téléphone, la parenthèse renvoie
    # à la phrase bleue de chaque ligne (troisième lecture, 11/11/2026).
    plage = "(« de … à … %% »)".replace(" ", lg.NBSP)      # renvoi à la phrase bleue de chaque ligne : ne se coupe pas
    items = (("d", ("de %s à %s : la barre " + plage + " contient au moins huit formations sur dix ; le point est la médiane" if mobile else
                    "de %s à %s : la barre contient au moins huit formations sur dix (du 1er au 9e" + lg.NBSP + "décile) ; le point est la médiane")
              % (A["d_de"], A["d_a"])),
             # Les effectifs imprimés sur chaque ligne sont ceux de la série bleue : la clé de la grise le dit.
             ("p", "de %s à %s : même mesure un an plus tôt (autres effectifs)" % (A["p_de"], A["p_a"])),
             ("b", "tranche de départ, placée sur le même axe"))
    x = 0.0
    for k, (genre, texte) in enumerate(items):
        if genre == "d":
            e.append('<rect x="%.1f" y="%.1f" width="20" height="10" fill="%s"/>' % (x, y - 9, BLEU))
            e.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#ffffff" stroke="%s" stroke-width="1.8"/>' % (x + 10, y - 4, BLEU))
        elif genre == "p":
            e.append('<rect x="%.1f" y="%.1f" width="20" height="4" fill="%s"/>' % (x, y - 6, GRIS))
            e.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s" stroke="#ffffff" stroke-width="1.2"/>' % (x + 10, y - 4, GRIS))
        else:
            e.append('<rect x="%.1f" y="%.1f" width="20" height="12" fill="%s"/>' % (x, y - 10, BANDE))
        lignes = pied_figure.coupe(texte, 32) if mobile else [texte]
        for n, l in enumerate(lignes):
            e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s">%s</text>' % (x + 26, y + 17 * n, taille, INK2, esc(l)))
        if mobile:
            y += 17 * (len(lignes) - 1) + (21 if k < len(items) - 1 else 0)
        elif k == 0:
            y += 18                                 # la série principale occupe la première ligne
        else:
            x += 26 + largeur(texte, taille) + 22
    return y


def marques_tranche(e: list, X, y: float, cle: str, p: dict, d: dict) -> None:
    """Une ligne de la figure 1 : bande de la tranche de départ (sous les étiquettes), intervalle de la transition
    précédente (fin, gris), intervalle de la dernière (épais, bleu), médianes. Aucun interstice : chaque rectangle va
    exactement de X(1er décile) à X(9e décile)."""
    bas, haut = bornes_bande(cle)
    if haut > bas:      # la tranche 100 % est un point, pas une étendue : pas de bande (elle débordait sous 100)
        # La bande dépasse au-dessus de la barre bleue et sous la grise : au ras de la bleue, ce qu'il en restait de
        # visible n'entourait que la grise et se lisait comme son halo (contrôleur de lecture, 11/11/2026).
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="28" fill="%s"/>' % (X(bas), y - 9, X(haut) - X(bas), BANDE))
    vp, vd = p["tranches"][cle], d["tranches"][cle]
    # Liseré blanc SOUS la barre grise (un rectangle à part, d'un pixel plus large de chaque côté) : sur la bande, le
    # gris seul ne se détache qu'à 2,7 pour 1. La barre elle-même garde ses bornes exactes.
    e.append('<rect aria-hidden="true" x="%.1f" y="%.1f" width="%.1f" height="6" fill="#ffffff"/>'
             % (X(vp["d1"]) - 1, y + 9, X(vp["d9"]) - X(vp["d1"]) + 2))
    e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="4" fill="%s"/>' % (X(vp["d1"]), y + 10, X(vp["d9"]) - X(vp["d1"]), GRIS))
    e.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s" stroke="#ffffff" stroke-width="1.2"/>' % (X(vp["mediane"]), y + 12, GRIS))
    e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="10" fill="%s"/>' % (X(vd["d1"]), y - 5, X(vd["d9"]) - X(vd["d1"]), BLEU))
    e.append('<circle cx="%.1f" cy="%.1f" r="4.6" fill="#ffffff" stroke="%s" stroke-width="2.2"/>' % (X(vd["mediane"]), y, BLEU))


def fig_tranches(c: dict, A: dict) -> str:
    t = textes("tranches", A)
    p, d = c["T"][-2], c["T"][-1]
    X0, X1, TOP, PAS = 150, 684, 114, 46
    X = lambda v: X0 + (X1 - X0) * v / 100.0  # noqa: E731
    ordre = [cle for cle, _, _, _ in reversed(TRANCHES)]      # 100 % en haut : la figure monte de gauche à droite
    BAS = TOP + PAS * len(ordre)
    e = ouvre("psup-t", t["titre"], t["sous_titre"], desc_tranches(c, A))
    cle_tranches(e, 60, A, 10.5)
    e.append('<text x="0" y="%d" font-size="10.5" fill="%s">Taux d\'accès l\'année de départ</text>' % (TOP - 6, INK2))
    for gv in range(0, 101, 20):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"/>'
                 % (X(gv), TOP - 2, X(gv), BAS, GRID, 1 if gv == 0 else 0.6))
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (X(gv), BAS + 15, MUTED, gv))
    e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">Taux d\'accès l\'année suivante, en %%</text>'
             % (X(50), BAS + 31, INK2))
    for i, cle in enumerate(ordre):
        y = TOP + PAS * i + 22
        j = "d_%s_" % JETON_TRANCHE[cle]
        ancre = cle == TRANCHE_RESULTAT
        e.append('<text x="0" y="%.1f" font-size="12" font-weight="600" fill="%s">%s</text>' % (y + 1, INK, esc(A[j + "lib"].capitalize())))
        e.append('<text x="0" y="%.1f" font-size="10" fill="%s">%s formations en %s</text>' % (y + 15, INK2, esc(A[j + "n"]), A["d_de"]))
        marques_tranche(e, X, y, cle, p, d)
        vd = d["tranches"][cle]
        fs = 13 if ancre else 11
        # Les trois valeurs AU-DESSUS de la barre bleue, chacune centrée sur ce qu'elle désigne : posées au bout de la
        # barre, cinq valeurs du 9e décile étaient plus proches de la barre grise que de la leur (contrôleur, 11/11/2026).
        e.append(valeur(X(vd["d1"]), y - 11, fs, BLEU, A[j + "d1"], "middle", ancre))
        if vd["d9"] != vd["mediane"]:               # à égalité (tranche 100 %), la médiane suffit : pas deux « 100 » côte à côte
            e.append(valeur(X(vd["d9"]), y - 11, fs, BLEU, A[j + "d9"], "middle", ancre))
        e.append(valeur(X(vd["mediane"]), y - 11, fs, BLEU, A[j + "med"], "middle", True))
    return pied_figure.pied(e, BAS + 44, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                             (LIC_FIG, MUTED, "pied-licence")], GRID)


def fig_tranches_m(c: dict, A: dict, svg_d: str) -> str:
    t = textes("tranches", A)
    p, d = c["T"][-2], c["T"][-1]
    e, y = pied_figure.tete_mobile("psup-tm", t["titre"], html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d).group(1)),
                                   INK, FONT)
    for k, l in enumerate(pied_figure.coupe(t["sous_titre"], 38)):
        y += 18 if k else 0
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    y = cle_tranches(e, y + 28, A, FS_MIN, mobile=True)
    X0, X1 = 6, 290
    X = lambda v: X0 + (X1 - X0) * v / 100.0  # noqa: E731
    for cle, _, _, _ in reversed(TRANCHES):
        j = "d_%s_" % JETON_TRANCHE[cle]
        ancre = cle == TRANCHE_RESULTAT
        y += 27
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s en %s</text>'
                 % (y, INK, esc(A[j + "lib"].capitalize()), A["d_de"]))
        e.append('<text x="298" y="%d" font-size="%s" fill="%s" text-anchor="end">%s formations</text>' % (y, FS_MIN, INK2, esc(A[j + "n"])))
        # La ligne de valeurs décrit la barre bleue : elle se pose entre le libellé et elle, jamais contre la barre grise.
        y += 19
        e.append('<text x="0" y="%d" font-size="%s"%s fill="%s">%s</text>'
                 % (y, 15 if ancre else FS_MIN, ' font-weight="600"' if ancre else "", BLEU,
                    esc("en %s : de %s à %s %%, médiane %s %%" % (A["d_a"], A[j + "d1"], A[j + "d9"], A[j + "med"]))))
        yb = y + 16
        e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8"/>' % (X0, yb, X1, yb, GRID))
        marques_tranche(e, X, yb, cle, p, d)
        y = yb + 16
    y += 12
    e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (X0, y, X1, y, GRID))
    for gv, ancre_ in ((0, "start"), (50, "middle"), (100, "end")):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(gv), y, X(gv), y + 5, MUTED))
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%s</text>' % (X(gv), y + 21, FS_MIN, MUTED, ancre_, esc("%d %%" % gv)))
    e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="middle">Taux d\'accès l\'année suivante</text>'
             % (X(50), y + 40, FS_MIN, INK2))
    return pied_figure.pied_mobile(e, y + 54, [(t["source_m"], INK2, "pied-source"), (t["note_m"], INK2, "pied-note"),
                                               (LIC_FIG_M, MUTED, "pied-licence")], GRID)


def ordre_filieres(c: dict) -> list:
    """Filières de la dernière transition, de la plus forte baisse médiane à la plus forte hausse ; à égalité, par nom."""
    fil = c["T"][-1]["filieres"]
    inconnues = [f for f in fil if f not in NOM_FILIERE]
    if inconnues:
        fail("figure des filieres : filiere sans nom d'affichage %s (completer NOM_FILIERE)" % inconnues)
    bas, haut = ECHELLE_FILIERES
    hors = [f for t in c["T"][-2:] for f, v in t["filieres"].items() if not bas + 3 <= v["variation_mediane"] <= haut - 1]
    if hors:
        fail("figure des filieres : variation mediane hors de l'echelle %s a %s (%s)" % (bas, haut, hors))
    return sorted(fil, key=lambda f: (fil[f]["variation_mediane"], NOM_FILIERE[f]))


def desc_filieres(c: dict, A: dict) -> str:
    p = c["T"][-2]
    out = ["Variation médiane du taux d'accès par filière, en points de pourcentage, de %s à %s puis de %s à %s."
           % (A["p_de"], A["p_a"], A["d_de"], A["d_a"])]
    for f in ordre_filieres(c):
        j = "f_%s_" % jeton_filiere(f)
        avant = "%s de %s à %s (%s formations), " % (A["p_" + j + "med"], A["p_de"], A["p_a"], A["p_" + j + "n"]) if f in p["filieres"] else ""
        out.append("%s : %s%s de %s à %s (%s formations)." % (NOM_FILIERE[f], avant, A["d_" + j + "med"], A["d_de"], A["d_a"], A["d_" + j + "n"]))
    # Exclusion déclarée dans l'image elle-même (contrôleur de géométrie, 11/11/2026) : le groupe reclassé n'est ni
    # dessiné ni nommé dans la figure ; il est au jeu, au CSV et dans la description.
    out.append("Ne sont pas dessinées les formations que le ministère a changé de filière d'une session à l'autre : %s de %s à %s, "
               "%s de %s à %s." % (A["p_recl_n"], A["p_de"], A["p_a"], A["d_recl_n"], A["d_de"], A["d_a"]))
    return " ".join(out)


def marques_filiere(e: list, X, y: float, vp, vd) -> None:
    """Une ligne de la figure 2 : anneau gris fin (transition précédente), point bleu plein (dernière), lien pâle."""
    if vp is not None:
        if vp != vd:
            e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2"/>' % (X(vp), y, X(vd), y, LIEN))
        e.append('<circle cx="%.1f" cy="%.1f" r="5.2" fill="#ffffff" stroke="%s" stroke-width="1.3"/>' % (X(vp), y, GRIS))
    e.append('<circle cx="%.1f" cy="%.1f" r="4.6" fill="%s"/>' % (X(vd), y, BLEU))


def pose_valeur(X, y: float, v, autre, a_gauche: bool, txt: str, taille, col: str, gras: bool) -> str:
    """Valeur d'un point de la figure 2 : à côté du point, du côté opposé à l'autre marque de la ligne ; AU-DESSUS du
    point quand ce côté toucherait l'axe du zéro ou l'autre marque (« −1 » collé à l'axe se lisait « −1| »)."""
    w = largeur(txt, taille, gras)
    g, dr = (X(v) - 10 - w, X(v) - 10) if a_gauche else (X(v) + 10, X(v) + 10 + w)
    gene = [X(0)] if v != 0 else []
    if autre is not None and autre != v:
        gene.append(X(autre))
    if any(g - 5 < x < dr + 5 for x in gene):
        return valeur(X(v), y - 9, taille, col, txt, "middle", gras)
    return valeur(dr if a_gauche else g, y + (5 if float(taille) >= 14 else 4), taille, col, txt, "end" if a_gauche else "start", gras)


def fig_filieres(c: dict, A: dict) -> str:
    t = textes("filieres", A)
    p, d = c["T"][-2], c["T"][-1]
    fil = ordre_filieres(c)
    VMIN, VMAX = ECHELLE_FILIERES
    X0, X1, TOP, PAS = 250, 690, 92, 31
    X = lambda v: X0 + (X1 - X0) * (v - VMIN) / float(VMAX - VMIN)  # noqa: E731
    BAS = TOP + PAS * len(fil)
    e = ouvre("psup-f", t["titre"], t["sous_titre"], desc_filieres(c, A))
    # Clé dans l'ordre du temps, comme sur téléphone (« −2 puis −11 ») ; l'en-tête des effectifs est collé à sa colonne et
    # dit « de … à … » (« 2024-2025 » se lisait comme une année scolaire, et l'en-tête comme une suite de la clé).
    e.append('<circle cx="6" cy="60" r="5.2" fill="#ffffff" stroke="%s" stroke-width="1.3"/>' % GRIS)
    e.append('<text x="18" y="64" font-size="10.5" fill="%s">de %s à %s, puis</text>' % (INK2, A["p_de"], A["p_a"]))
    e.append('<circle cx="158" cy="60" r="4.6" fill="%s"/>' % BLEU)
    e.append('<text x="170" y="64" font-size="10.5" fill="%s">de %s à %s</text>' % (INK2, A["d_de"], A["d_a"]))
    e.append('<text x="236" y="%d" font-size="10" fill="%s" text-anchor="end">formations comparées de %s à %s</text>'
             % (TOP + 3, INK2, A["d_de"], A["d_a"]))
    for gv in (-10, -5, 0):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"/>'
                 % (X(gv), TOP - 2, X(gv), BAS, INK2 if gv == 0 else GRID, 0.9 if gv == 0 else 0.6))
        e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%s</text>' % (X(gv), BAS + 15, MUTED, lg.signe(gv, 0)))
    e.append('<text x="%.1f" y="%d" font-size="10.5" fill="%s" text-anchor="middle">Variation médiane du taux d\'accès, en points de pourcentage</text>'
             % ((X0 + X1) / 2.0, BAS + 31, INK2))
    extreme = fil[0]
    for i, f in enumerate(fil):
        y = TOP + PAS * i + 17
        j = "f_%s_" % jeton_filiere(f)
        vd = d["filieres"][f]["variation_mediane"]
        vp = p["filieres"][f]["variation_mediane"] if f in p["filieres"] else None
        bleu = A["d_" + j + ("med_pts" if f == extreme else "med")]      # la valeur en ancrage porte son unité
        a_gauche = vp is None or vd <= vp                                # la valeur bleue se pose du côté opposé à l'anneau
        # Le filet de ligne part de la marque la plus à gauche quand la valeur écrite à sa gauche déborderait sur lui.
        mini = vd if vp is None else min(vd, vp)
        txt_g = bleu if (a_gauche and mini == vd) else (A["p_" + j + "med"] if vp is not None and vp < vd else "")
        xg = X(mini) if txt_g and X(mini) - 10 - largeur(txt_g, 14, True) < X0 + 30 else X0
        e.append('<line x1="%.1f" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (xg, y, X1, y, GRID))
        e.append('<text x="0" y="%.1f" font-size="11.5"%s fill="%s">%s</text>'
                 % (y + 4, ' font-weight="600"' if f == extreme else "", INK, esc(NOM_FILIERE[f])))
        e.append('<text x="236" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (y + 4, INK2, esc(A["d_" + j + "n"])))
        marques_filiere(e, X, y, vp, vd)
        e.append(pose_valeur(X, y, vd, vp, a_gauche, bleu, 14 if f == extreme else 11, BLEU, True))
        if vp is not None:                                               # à égalité aussi : chaque ligne porte ses deux valeurs
            e.append(pose_valeur(X, y, vp, vd, not a_gauche, A["p_" + j + "med"], 10, INK2, False))
    return pied_figure.pied(e, BAS + 44, W, [(t["source"], INK2, "pied-source"), (t["note"], INK2, "pied-note"),
                                             (LIC_FIG, MUTED, "pied-licence")], GRID)


def fig_filieres_m(c: dict, A: dict, svg_d: str) -> str:
    t = textes("filieres", A)
    p, d = c["T"][-2], c["T"][-1]
    fil = ordre_filieres(c)
    VMIN, VMAX = ECHELLE_FILIERES
    e, y = pied_figure.tete_mobile("psup-fm", t["titre"], html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d).group(1)),
                                   INK, FONT)
    for k, l in enumerate(pied_figure.coupe(t["sous_titre"], 38)):
        y += 18 if k else 0
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    # Clé dans l'ordre de la ligne de valeurs (« −2 puis −11 ») : la transition précédente d'abord.
    y += 28
    e.append('<circle cx="6" cy="%d" r="5.2" fill="#ffffff" stroke="%s" stroke-width="1.3"/>' % (y - 5, GRIS))
    e.append('<text x="18" y="%d" font-size="%s" fill="%s">de %s à %s, puis</text>' % (y, FS_MIN, INK2, A["p_de"], A["p_a"]))
    y += 21
    e.append('<circle cx="6" cy="%d" r="4.6" fill="%s"/>' % (y - 5, BLEU))
    e.append('<text x="18" y="%d" font-size="%s" fill="%s">de %s à %s</text>' % (y, FS_MIN, INK2, A["d_de"], A["d_a"]))
    # Les effectifs se disent dans la clé : un en-tête de colonne coiffait « −2 puis −11 », pas le nombre de formations.
    # « comparées », pas « suivies » : pour un lycéen, suivre une formation, c'est y étudier (troisième lecture, 11/11).
    y += 5
    for l in pied_figure.coupe("À droite de chaque axe : nombre de formations comparées de %s à %s" % (A["d_de"], A["d_a"]), 38):
        y += 19
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    X0, X1 = 14, 246       # la droite de la ligne des points (au-delà de +1) reçoit la colonne des effectifs
    X = lambda v: X0 + (X1 - X0) * (v - VMIN) / float(VMAX - VMIN)  # noqa: E731
    extreme = fil[0]
    y += 2
    for f in fil:
        j = "f_%s_" % jeton_filiere(f)
        vd = d["filieres"][f]["variation_mediane"]
        vp = p["filieres"][f]["variation_mediane"] if f in p["filieres"] else None
        y += 31
        e.append('<text x="0" y="%d" font-size="14"%s fill="%s">%s</text>'
                 % (y, ' font-weight="600"' if f == extreme else "", INK, esc(NOM_FILIERE[f])))
        bleu, fs = A["d_" + j + "med"], (17 if f == extreme else 15)
        e.append('<text x="298" y="%d" font-size="%s" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (y, fs, BLEU, esc(bleu)))
        if vp is not None:
            e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="end">%s puis</text>'
                     % (298 - largeur(bleu, fs, True) - 7, y, FS_MIN, INK2, esc(A["p_" + j + "med"])))
        yb = y + 15
        e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8"/>' % (X0, yb, X1, yb, GRID))
        for gv in (-10, -5, 0):     # repères de l'échelle sur chaque ligne, sous le texte et jamais à travers
            h = 6 if gv == 0 else 3
            e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="%s"/>'
                     % (X(gv), yb - h, X(gv), yb + h, INK2 if gv == 0 else MUTED, 1 if gv == 0 else 0.8))
        marques_filiere(e, X, yb, vp, vd)
        e.append('<text x="298" y="%d" font-size="%s" fill="%s" text-anchor="end">%s</text>' % (yb + 5, FS_MIN, INK2, esc(A["d_" + j + "n"])))
        y = yb
    y += 14
    for gv in (-10, -5, 0):
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="middle">%s</text>' % (X(gv), y + 17, FS_MIN, MUTED, lg.signe(gv, 0)))
    e.append('<text x="150" y="%d" font-size="%s" fill="%s" text-anchor="middle">points de pourcentage</text>' % (y + 36, FS_MIN, INK2))
    return pied_figure.pied_mobile(e, y + 50, [(t["source_m"], INK2, "pied-source"), (t["note_m"], INK2, "pied-note"),
                                               (LIC_FIG_M, MUTED, "pied-licence")], GRID)


def figures(c: dict, A: dict, fausse: bool = False) -> dict:
    """`fausse` n'existe que pour la mutation « parite » : la version téléphone reçoit une valeur que la détaillée n'a pas."""
    figs = {}
    Am = dict(A, d_t6075_d9="84") if fausse else A
    for nom, bureau, mobile in (("tranches", fig_tranches, fig_tranches_m), ("filieres", fig_filieres, fig_filieres_m)):
        svg = bureau(c, A)
        figs["parcoursup-%s.svg" % nom], figs["parcoursup-%s-m.svg" % nom] = svg, mobile(c, Am, svg)
        ecarts = pied_figure.parite(svg, figs["parcoursup-%s-m.svg" % nom], FS_MIN, (BLEU,))
        ecarts += ["hors cadre (bureau) : " + x for x in pied_figure.hors_cadre(svg, W)]
        ecarts += ["hors cadre (telephone) : " + x for x in pied_figure.hors_cadre(figs["parcoursup-%s-m.svg" % nom], pied_figure.LARGEUR_M)]
        if ecarts:
            fail("figure %s : %s" % (nom, " ; ".join(ecarts)))
    return figs


def fiches(figs: dict, A: dict) -> dict:
    out = []
    for nom in ("tranches", "filieres"):
        svg = figs["parcoursup-%s.svg" % nom]
        out.append(dict(id=nom, fichier="parcoursup-%s" % nom,
                        titre=html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1)),
                        montre=textes(nom, A)["montre"],
                        source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note")))
    return {"fr": out}


# ------------------------------------------------------------------ sorties
def csv_texte(c: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tableau", "transition", "modalite", "indicateur", "valeur", "unite"])
    lib = {cle: l for cle, _, _, l in TRANCHES}
    for t in c["T"]:
        tr = t["cle"]
        w.writerow(["appariement", tr, "présentes l'une ou l'autre année", "formations", t["entrees"], "formations"])
        w.writerow(["appariement", tr, "appariées (même code, même intitulé)", "formations", t["appariees"], "formations"])
        for m in MOTIFS:
            w.writerow(["appariement", tr, "écartées : " + m, "formations", t["ecartees"][m], "formations"])
        for cle, v in t["tranches"].items():
            for ind, val, unite in (("effectif", v["n"], "formations"), ("premier_decile", v["d1"], "%"), ("mediane", v["mediane"], "%"),
                                    ("neuvieme_decile", v["d9"], "%"), ("part_a_90_ou_plus", v["reste_90"], "% des formations"),
                                    ("part_perdant_20_points_ou_plus", v["baisse_20"], "% des formations"),
                                    ("part_perdant_un_cinquieme_du_niveau", v["perte_cinquieme"], "% des formations"),
                                    ("part_entre_les_deux_deciles", v["dans_d1_d9"], "% des formations"),
                                    ("part_couverte_par_les_bornes_de_la_transition_precedente",
                                     v.get("couverture_bornes_precedentes"), "% des formations"),
                                    ("sensibilite_50_candidats_effectif", v["n_50cand"], "formations"),
                                    ("sensibilite_50_candidats_part_perdant_20_points", v["baisse_20_50cand"], "% des formations"),
                                    ("sensibilite_filiere_part_perdant_20_points", v["baisse_20_corrigee"], "% des formations"),
                                    ("sensibilite_capacite_effectif", v["sans_capa"]["n"], "formations"),
                                    ("sensibilite_capacite_premier_decile", v["sans_capa"]["d1"], "%"),
                                    ("sensibilite_capacite_mediane", v["sans_capa"]["mediane"], "%"),
                                    ("sensibilite_capacite_neuvieme_decile", v["sans_capa"]["d9"], "%")):
                if val is not None:
                    w.writerow(["taux_de_l_annee_suivante_par_tranche", tr, lib[cle], ind, val, unite])
        for ind, val, unite in (("correlation_de_pearson", t["pearson"], ""), ("correlation_de_spearman", t["spearman"], ""),
                                ("correlation_de_pearson_hors_0_et_100", t["pearson_interieur"], ""),
                                ("correlation_de_spearman_hors_0_et_100", t["spearman_interieur"], ""),
                                ("variation_mediane", t["variation_mediane"], "points"),
                                ("variation_moyenne", t["variation_moyenne"], "points"),
                                ("part_en_baisse", t["part_baisse"], "% des formations"),
                                ("part_en_hausse", t["part_hausse"], "% des formations"),
                                ("part_inchangee", t["part_inchangee"], "% des formations"),
                                ("variation_absolue_mediane", t["abs_mediane"], "points"),
                                ("tres_selectives_moins_de_20_effectif", t["contre_population"]["n"], "formations"),
                                ("tres_selectives_atteignant_40_ou_plus", t["contre_population"]["atteint_40"], "formations"),
                                ("capacite_changee_de_plus_de_25_pour_cent", t["capacite_changee_25"]["n"], "formations")):
            w.writerow(["stabilite_d_ensemble", tr, "toutes les formations appariées", ind, val, unite])
        for f, v in sorted(t["filieres"].items()):
            for ind, val, unite in (("effectif", v["n"], "formations"), ("variation_mediane", v["variation_mediane"], "points"),
                                    ("variation_moyenne", v["variation_moyenne"], "points"),
                                    ("taux_median_depart", v["taux_med"][0], "%"), ("taux_median_arrivee", v["taux_med"][1], "%"),
                                    ("part_en_baisse", v["part_baisse"], "% des formations"), ("correlation_de_pearson", v["pearson"], ""),
                                    ("correlation_de_spearman", v["spearman"], ""),
                                    ("candidats_medians_depart", v["candidats_med"][0], "candidats"),
                                    ("candidats_medians_arrivee", v["candidats_med"][1], "candidats"),
                                    ("places_medianes_depart", v["places_med"][0], "places"), ("places_medianes_arrivee", v["places_med"][1], "places")):
                w.writerow(["filieres", tr, f, ind, val, unite])
        w.writerow(["filieres", tr, RECLASSEE + " par le ministère d'une session à l'autre", "effectif", t["reclassees"]["n"], "formations"])
        if t["reclassees"]["variation_mediane"] is not None:
            w.writerow(["filieres", tr, RECLASSEE + " par le ministère d'une session à l'autre", "variation_mediane",
                        t["reclassees"]["variation_mediane"], "points"])
        for g, v in t["selection"].items():
            for ind, cle_, unite in (("effectif", "n", "formations"), ("taux_d_acces_median", "taux_med", "%"),
                                     ("capacite_mediane", "capa_med", "places"), ("candidats_medians", "cand_med", "candidats"),
                                     ("part_de_cpge", "part_cpge", "%"), ("part_de_bts", "part_bts", "%"), ("part_de_licences", "part_licence", "%")):
                if v.get(cle_) is not None:
                    w.writerow(["selection_de_l_appariement", tr, g, ind, v[cle_], unite])
    tr2 = [t["cle"] for t in c["T"][-2:]]
    for nom, v in (("toutes les formations appariées aux deux transitions", c["cohorte"]["toutes"]),
                   ("idem, sans les classes préparatoires", c["cohorte"]["sans_cpge"])):
        for i, tr in enumerate(tr2):
            for ind, val, unite in (("effectif", v["n"], "formations"), ("part_en_baisse", v["part_baisse"][i], "% des formations"),
                                    ("part_en_hausse", v["part_hausse"][i], "% des formations"),
                                    ("variation_moyenne", v["variation_moyenne"][i], "points"),
                                    ("variation_mediane", v["variation_mediane"][i], "points")):
                w.writerow(["cohorte_des_trois_sessions", tr, nom, ind, val, unite])
    e = c["ex"]
    for ind, cle_, unite in (("taux_d_acces", "taux", "%"), ("candidats_phase_principale", "voe", "candidats"), ("candidats_classes", "cla", "candidats"),
                             ("propositions", "prop", "propositions"), ("admis", "acc", "candidats"), ("capacite", "capa", "places"),
                             ("part_bac_general_parmi_les_appelables", "gen", "%"), ("part_bac_technologique_parmi_les_appelables", "tec", "%"),
                             ("part_bac_professionnel_parmi_les_appelables", "pro", "%")):
        w.writerow(["exemple_fichier_ouvert", str(e["session"]), "%s — %s" % (e["etab"], e["lib"]), ind, e[cle_], unite])
    return buf.getvalue()


def payload_de(c: dict, A: dict) -> dict:
    X = c["X"]
    meta = {
        "page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
        "champ": "France ; formations de la plateforme Parcoursup hors apprentissage, sessions %s" % lg.enumere([str(a) for a in X["ans"]]),
        "sources": [dict(s, sha256=X["sums"][s["fichier"]]) for s in X["man"]["sessions"]],
        "licence_des_sources": X["man"]["licence"], "producteur": X["man"]["producteur"],
        "regles": {"appariement": "même code de formation (cod_aff_form) et même intitulé (lib_for_voe_ins) dans deux sessions consécutives",
                   "motifs_d_ecart_par_priorite": list(MOTIFS),
                   "tranches": [{"tranche": cle, "bas_inclus": bas, "haut_exclu": haut} for cle, bas, haut, _ in TRANCHES],
                   "quantiles": "statistics.quantiles(n=10, method='inclusive') de Python",
                   "seuil_filiere": SEUIL_FILIERE},
        "temoin": {"fichier": "scripts/sources_parcoursup/temoin.json", "sha256": X["sums"]["temoin.json"],
                   "scripts": X["temoin"]["scripts"], "tolerance_points": TOLERANCE, "tolerance_correlations": TOLERANCE_CORR},
        "definitions": {
            "taux_d_acces": "repris tel que publié (taux_acces_ens), entier de 0 à 100 ; jamais recalculé",
            "dans_d1_d9": "part des formations de la tranche dont le taux d'arrivée est compris entre le 1er et le 9e décile, bornes incluses ; elle dépasse 80 % quand des formations sont à égalité sur une borne (9e décile à 100 %)",
            "couverture_bornes_precedentes": "bornes 1er-9e décile de la transition précédente appliquées aux formations de la transition ; à comparer à dans_d1_d9 de la transition précédente, pas à 80 %",
            "baisse_20_corrigee": "variation diminuée de la variation médiane de la filière (ou du groupe des formations reclassées)",
            "filieres": "formations classées dans la même filière (fili) les deux sessions ; celles dont la filière diffère forment le groupe « reclassees », compté à part et jamais présenté comme une filière",
            "selection": "groupes décrits à l'année de départ ; les nouvelles formations à l'année d'arrivée",
            "exemple": "nombres du fichier ouvert (au 10 septembre, tous candidats) ; la fiche de la plateforme, arrêtée à la fin de la phase principale, en donne d'autres"}}
    T = [{k: v for k, v in t.items() if not k.startswith("_")} for t in c["T"]]
    ex = {k: c["ex"][k] for k in ("session", "code", "etab", "lib", "fili", "taux", "capa", "voe", "voe_pc", "cla", "prop", "acc", "gen", "tec", "pro",
                                  "part_admis", "part_propositions")}
    meta["definitions"]["cohorte"] = ("formations appariées aux deux dernières transitions (mêmes formations sur trois sessions) ; "
                                      "listes [transition précédente, dernière transition] ; sans_cpge : hors formations classées "
                                      "CPGE à l'une au moins des trois sessions")
    return releve_jeu.normalise({"meta": meta, "transitions": T, "cohorte": c["cohorte"], "exemple": ex, "affichage": A})


def main() -> int:
    args = sys.argv[1:]
    if "--mutations" in args:
        ok = [jouer_mutation(m) for m in MUTATIONS]
        log("%d mutations sur %d ont fait mordre leur garde." % (sum(ok), len(ok)))
        return 0 if all(ok) else 1
    m = next((a.split("=", 1)[1] for a in args if a.startswith("--mutation=")), "")
    if m:
        return 0 if jouer_mutation(m) else 1
    X = lire()
    c = calcul(X)
    n = gardes(c, "1") + gardes(c, "2") + gardes(c, "3") + gardes(c, "5") + gardes(c, "4") + gardes(c, "6") \
        + gardes(c, "9") + gardes(c, "constats")
    A = affichage(c)
    c["A"] = A
    n += gardes(c, "8")       # la prose interdite se cherche aussi dans les jetons
    p, d = c["T"][-2], c["T"][-1]
    log("Parcoursup %s : %s appariees sur %s puis %s sur %s ; 60-75 %% -> %s a %s (%s) ; 90-99 %% restent %s puis %s %%"
        % (A["sessions"], A["p_n"], A["p_entrees"], A["d_n"], A["d_entrees"], A["d_t6075_d1"], A["d_t6075_d9"],
           A["d_t6075_dans_frac"], A["p_t9099_reste"], A["d_t9099_reste"]))
    figs = figures(c, A)      # parité téléphone et cadre contrôlés dans figures(), aussi sous --check
    log("Figures : " + ", ".join("%s %sx%s" % ((f,) + re.search(r'viewBox="0 0 (\d+) (\d+)"', s).groups()) for f, s in figs.items()))
    if c["page"] is None:
        log("Page absente (%s) : gardes 6 et 8 appliquees aux jetons seulement, vues mordre par mutation ; hauteurs des "
            "figures non confrontees a la page." % PAGE_MD.relative_to(ROOT))
    else:
        ecarts = pied_figure.controler_page(c["page"], figs)
        if ecarts:
            fail("page : " + " ; ".join(ecarts))
    if "--check" in args:
        log("--check : %d conditions de garde passees (%d cles d'affichage), temoin egal a %s point pres, parite des "
            "figures telephone controlee, rien ecrit." % (n, len(A), TOLERANCE))
        return 0
    payload = payload_de(c, A)
    texte_csv = csv_texte(c)
    fic = json.dumps(fiches(figs, A), ensure_ascii=False, indent=1) + "\n"
    try:
        prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
        releve_jeu.sans_licence(prev, LICENCE)
        prev.pop("releve_le", None)
        if prev == json.loads(json.dumps(payload, ensure_ascii=False)) and OUT_STATIC.exists() and OUT_CSV.exists() \
                and OUT_STATIC.read_text(encoding="utf-8") == OUT_DATA.read_text(encoding="utf-8") \
                and OUT_CSV.read_text(encoding="utf-8-sig") == texte_csv \
                and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s
                        and (OUT_IMG / f.replace(".svg", ".png")).exists() for f, s in figs.items()) \
                and OUT_FIGURES.exists() and OUT_FIGURES.read_text(encoding="utf-8") == fic:
            # Figures et fiches « Réutiliser » comparées aussi : une légende corrigée se réécrit (leçon 11 du pilote).
            log("Donnees, figures et fiches identiques : rien ecrit.")
            return 0
    except (OSError, ValueError):
        pass
    import cairosvg      # SVG et PNG ensemble ou pas du tout : sans la bibliothèque de rendu, rien ne s'écrit
    rel = releve_jeu.releve(OUT_DATA, payload, date.today().isoformat())
    payload = {"releve_le": rel, "_licence": LICENCE, **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(texte_csv, encoding="utf-8-sig", newline="\n")
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8", newline="\n")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")),
                         output_width=900 if f.endswith("-m.svg") else 1440, background_color="white")
    OUT_FIGURES.write_text(fic, encoding="utf-8", newline="\n")
    log("Ecrit : data/ et static/parcoursup.json, static/parcoursup.csv, data/figures_parcoursup.json, %d figures SVG + PNG "
        "(releve_le %s ; %d conditions de garde, %d cles d'affichage)" % (len(figs), rel, n, len(A)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
