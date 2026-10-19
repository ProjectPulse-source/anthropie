#!/usr/bin/env python3
"""update_dette_dynamique.py -- volet « Pourquoi la dette publique augmente-t-elle ? » (dossier dette, volet 1).

Arbitrage PRO-20260930-092814 (option E) : le volet n'existe que s'il porte une DÉCOMPOSITION robuste de la variation
du ratio dette/PIB. Identité (administrations publiques, France, Eurostat, monnaie nationale) :

    d_t - d_{t-1} = i_t/(1+g_t) * d_{t-1}      effet des intérêts            (i = intérêts_t / dette_{t-1}, taux implicite)
                  - g_t/(1+g_t) * d_{t-1}      effet de la croissance nominale (g = PIB_t / PIB_{t-1} - 1)
                  - pb_t                       solde primaire / PIB (excédent > 0 : il fait BAISSER le ratio)
                  + sfa_t                      ajustements flux-stock (résidu)

TÉMOIN, bloquant (02/10/2026) : les ratios qu'Eurostat PUBLIE en % du PIB (gov_10dd_edpt1, PC_GDP : dette, solde,
intérêts), que le calcul n'utilise pas. Un écart de plus de 0,11 point sur la dette ou le solde primaire d'une année :
rien n'est écrit. L'ancien « témoin » ((ΔDette_t + B9_t) / PIB_t) était ALGÉBRIQUEMENT égal au résidu flux-stock : il ne
pouvait rien rejeter. Le PIB est celui de la notification (gov_10dd_edpt1, B1GQ, monnaie nationale) : jusqu'au 02/10 le
calcul divisait par nama_10_gdp en CP_MEUR, donc par des écus avant 1999 — dette de 1995 à 57,5 % au lieu des 57,8 %
publiés. Trouvé en faisant mordre le nouveau témoin (test décisif de /dette-publique-peut-elle-baisser/).

Les phrases que la page affirme sont recalculées ici (gardes de prose) : si une nouvelle donnée les dément, arrêt.
SVG et PNG sont produits ensemble ou pas du tout (cairosvg) ; les fiches « Réutiliser » sont lues dans le SVG.

Bilingue (30/09/2026), sur le modèle de update_dette_insee.py : UN calcul, deux présentations. Le bloc `affichage_en`
porte les mêmes clés que `affichage`, au format anglais (point décimal, virgule des milliers) ; les figures `-en`
reprennent le même dessin, textes traduits dans l'image. Les gardes de prose ne regardent que les nombres : une seule
passe vaut pour les deux langues.

Usage : python scripts/update_dette_dynamique.py [--check]
Sorties : data/ et static/dette_dynamique.json (blocs affichage et affichage_en), static/dette_dynamique.csv,
          data/figures_dynamique.json (clés fr et en),
          static/img/dette-dynamique-{cascade,annuelle}{,-en}.svg + .png
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pied_figure  # pied commun, parité des figures téléphone, hauteurs déclarées (scripts/pied_figure.py)
import langue_generee as lg  # noqa: E402  -- extremums publiés à la précision affichée (organe commun)
import releve_jeu as rj  # noqa: E402  -- relevé daté par les seules données (organe commun, 17/10/2026)

ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dette_dynamique.json"
OUT_STATIC = ROOT / "static" / "dette_dynamique.json"
OUT_CSV = ROOT / "static" / "dette_dynamique.csv"
OUT_FIGURES = ROOT / "data" / "figures_dynamique.json"
OUT_IMG = ROOT / "static" / "img"
PAGE_URL = "stephane-lalut.com/pourquoi-la-dette-publique-augmente/"
# Adresse de la future page anglaise, imprimée dans le cartouche des figures -en : à aligner sur l'`url:` du
# front matter de la page .en.md le jour où elle est créée (même forme que /en/cost-of-french-public-debt/).
PAGE_URL_EN = "stephane-lalut.com/en/why-does-public-debt-rise/"
PERIODES = [(1996, 2007, "1996-2007"), (2008, 2019, "2008-2019"), (2020, None, "2020-%s")]
TOL_TEMOIN = 0.11   # ratios publiés à une décimale ; le solde primaire additionne deux arrondis

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


MILLESIMES: dict[str, str] = {}   # jeu Eurostat -> date de sa dernière mise à jour (champ « updated » de l'API)
MOIS_EN = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")


def millesime(ds: str, lang: str) -> str:
    a, m, j = MILLESIMES[ds][:10].split("-")
    return "%s/%s/%s" % (j, m, a) if lang == "fr" else "%d %s %s" % (int(j), MOIS_EN[int(m) - 1], a)


def eurostat(ds: str, **f) -> dict[int, float]:
    q = "&".join("%s=%s" % (k, v) for k, v in f.items())
    d = json.loads(fetch("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/%s?format=JSON&geo=FR&%s" % (ds, q)))
    if "dimension" not in d:
        fail("Eurostat %s : reponse sans dimensions" % ds)
    if not re.match(r"\d{4}-\d{2}-\d{2}", str(d.get("updated", ""))):
        fail("Eurostat %s : date de mise a jour absente (millesime affiche dans la page et les figures)" % ds)
    MILLESIMES[ds] = max(MILLESIMES.get(ds, ""), d["updated"])
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


def en(v: float, dec: int = 1) -> str:
    """Même contrat que update_dette_insee.en (3536.1 -> '3,536.1'), signe moins typographique conservé."""
    return ("{:," + "." + str(dec) + "f}").format(v).replace("-", "−")


def signe(v: float, dec: int = 1, nb=fr) -> str:
    return ("+" if v >= 0 else "") + nb(v, dec)


def signe_en(v: float, dec: int = 1) -> str:
    return signe(v, dec, en)


# ------------------------------------------------------------------ calcul
def decomposition():
    D = eurostat("gov_10dd_edpt1", na_item="GD", sector="S13", unit="MIO_NAC")
    Y = eurostat("gov_10dd_edpt1", na_item="B1GQ", sector="S1", unit="MIO_NAC")
    pub = {k: eurostat("gov_10dd_edpt1", na_item=k, sector="S13", unit="PC_GDP") for k in ("GD", "B9", "D41PAY")}
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
        if not all(a in pub[k] for k in pub):
            fail("%d : ratio publie absent (temoin)" % a)
        e_d, e_pb = d1 - pub["GD"][a], pb - (pub["B9"][a] + pub["D41PAY"][a])
        if abs(e_d) > TOL_TEMOIN or abs(e_pb) > TOL_TEMOIN:
            fail("%d : ecart aux ratios publies par Eurostat, dette %+.2f pt, solde primaire %+.2f pt" % (a, e_d, e_pb))
        rows.append(dict(annee=a, dette_pct_pib=d1, variation=d1 - d0, effet_interets=interets,
                         effet_croissance=croissance, effet_taux_croissance=interets + croissance,
                         contribution_solde_primaire=-pb, flux_stock=sfa, taux_implicite_pct=i * 100,
                         croissance_nominale_pct=g * 100, solde_primaire_pct_pib=pb))
    return ans[0] - 1, D[ans[0] - 1] / Y[ans[0] - 1] * 100, rows


def depenses_recettes():
    """Dépenses (TE), recettes (TR), intérêts (D41PAY) et solde (B9), en % du PIB, tels qu'Eurostat les PUBLIE.

    Troisième tour de la confrontation à la recherche (03/10/2026) : l'OFCE attribue le creusement du déficit depuis
    2017 à la baisse des prélèvements, la DG Trésor (Trésor-Éco n° 403) celui de 2019-2025 surtout à la dépense. Les
    séries publiées éprouvent les deux lectures sur leurs fenêtres. Témoin : TR − TE redonne B9 publié."""
    s = {k: eurostat("gov_10a_main", na_item=k, sector="S13", unit="PC_GDP") for k in ("TE", "TR", "D41PAY", "B9")}
    ans = sorted(a for a in s["TE"] if all(a in s[k] for k in s))
    for a in ans:
        if abs((s["TR"][a] - s["TE"][a]) - s["B9"][a]) > 0.15:
            fail("%d : recettes - depenses ne redonnent pas le solde publie (temoin TE/TR/B9)" % a)
    return {a: dict(depenses=s["TE"][a], recettes=s["TR"][a], interets=s["D41PAY"][a], solde=s["B9"][a],
                    depenses_hors_interets=s["TE"][a] - s["D41PAY"][a]) for a in ans}


# ------------------------------------------------------------------ conjoncture ou structure (19/10/2026)
# Test décisif (arbitrages ENTRANTE_2026-10-18_Dette-contexte-solution, -02, -03 ; décision de l'auteur du 19/10) : le
# déficit primaire d'après 2020 est-il conjoncturel ? Trois estimations du solde corrigé du cycle, chacune avec sa
# méthode : Commission (AMECO, structurel, sans cycle ni mesures ponctuelles, publié depuis 2010 ; et ses recettes et
# dépenses corrigées du cycle depuis 1978), FMI (corrigé du cycle seulement, mesures ponctuelles comprises), OCDE
# (sous-jacent). Pièces archivées et contrôlées par SHA256SUMS ; aucune moyenne entre producteurs n'est publiée.
# Témoins BLOQUANTS : (1) recettes corrigées − dépenses corrigées = solde primaire corrigé d'AMECO, au demi-centième ;
# (2) l'écart entre le solde primaire d'Eurostat (intérêts VERSÉS déduits) et celui du FMI (intérêts NETS déduits, selon
# la définition de l'indicateur) égale les intérêts reçus (Eurostat D41REC), à 0,1 point près chaque année.
SOURCES_DETTE = ROOT / "scripts" / "sources_dette"
PIECES_CS = {"ameco": "ameco_fr_corrige_2026-06-02.csv", "fmi_ca": "fmi_FM2026-10_GGCBP.json",
             "fmi_obs": "fmi_FM2026-10_GGXONLB.json", "ocde": "ocde_EO119_NLGXQU.csv"}
EDITIONS_CS = {"fr": dict(ameco="AMECO, printemps 2026", fmi="Moniteur des finances publiques d’octobre 2026",
                          ocde="Perspectives économiques n° 119"),
               "en": dict(ameco="AMECO, spring 2026", fmi="Fiscal Monitor, October 2026", ocde="Economic Outlook No. 119")}
FEN_CS = {"avant": (2015, 2019), "apres": (2022, None), "long": (1996, 2007), "crise": (2010, 2014)}


def piece_cs(nom: str) -> bytes:
    sums = {l.split()[1].lstrip("*"): l.split()[0] for l in (SOURCES_DETTE / "SHA256SUMS").read_text(encoding="utf-8").splitlines() if l.strip()}
    b = (SOURCES_DETTE / nom).read_bytes()
    if sums.get(nom) != hashlib.sha256(b).hexdigest():
        fail("piece %s : empreinte differente de SHA256SUMS ; relire la piece" % nom)
    return b


def conjoncture(rows):
    """{an: dict(obs, ce_rec, ce_dep, ce_ca, ce_st, fmi_ca, fmi_obs, ocde, int_recus)} de 1996 à la dernière année."""
    S = {"ce_rec": {}, "ce_dep": {}, "ce_ca": {}, "ce_st": {}}
    for r in csv.DictReader(l for l in piece_cs(PIECES_CS["ameco"]).decode("utf-8").splitlines() if not l.startswith("#")):
        a = int(r["annee"])
        S["ce_rec"][a], S["ce_dep"][a], S["ce_ca"][a] = (float(r["recettes_corrigees"]), float(r["depenses_hors_interets_corrigees"]),
                                                         float(r["solde_primaire_corrige"]))
        if r["solde_primaire_structurel"]:
            S["ce_st"][a] = float(r["solde_primaire_structurel"])
    for cle, nomf, ind in (("fmi_ca", PIECES_CS["fmi_ca"], "GGCBP_G01_PGDP_PT"), ("fmi_obs", PIECES_CS["fmi_obs"], "GGXONLB_G01_GDP_PT")):
        S[cle] = {int(a): float(v) for a, v in json.loads(piece_cs(nomf).decode("utf-8"))["values"][ind]["FRA"].items()}
    S["ocde"] = {int(r["TIME_PERIOD"]): float(r["OBS_VALUE"]) for r in csv.DictReader(piece_cs(PIECES_CS["ocde"]).decode("utf-8-sig").splitlines())
                 if r["REF_AREA"] == "FRA" and r["MEASURE"] == "NLGXQU" and r["OBS_VALUE"]}
    rec = eurostat("gov_10a_main", na_item="D41REC", sector="S13", unit="MIO_NAC")
    Y = eurostat("gov_10dd_edpt1", na_item="B1GQ", sector="S1", unit="MIO_NAC")
    fin = rows[-1]["annee"]
    out = {}
    for r in rows:
        a = r["annee"]
        if any(a not in S[k] for k in ("ce_rec", "ce_dep", "ce_ca", "fmi_ca", "fmi_obs")) or a not in rec:
            fail("conjoncture : %d absent d'une piece ou de D41REC" % a)
        if abs(S["ce_rec"][a] - S["ce_dep"][a] - S["ce_ca"][a]) > 0.005:
            fail("conjoncture : %d, recettes - depenses corrigees ne redonnent pas le solde corrige d'AMECO (temoin 1)" % a)
        ir = rec[a] / Y[a] * 100
        if abs((r["solde_primaire_pct_pib"] - S["fmi_obs"][a]) - ir) > 0.1:
            fail("conjoncture : %d, ecart Eurostat - FMI (%.2f) different des interets recus (%.2f) (temoin 2)"
                 % (a, r["solde_primaire_pct_pib"] - S["fmi_obs"][a], ir))
        out[a] = dict(obs=r["solde_primaire_pct_pib"], ce_rec=S["ce_rec"][a], ce_dep=S["ce_dep"][a], ce_ca=S["ce_ca"][a],
                      ce_st=S["ce_st"].get(a), fmi_ca=S["fmi_ca"][a], fmi_obs=S["fmi_obs"][a], ocde=S["ocde"].get(a), int_recus=ir)
    if any(out[a]["ce_st"] is None or out[a]["ocde"] is None for a in range(2010, fin + 1)):
        fail("conjoncture : structurel Commission ou OCDE absent d'une annee depuis 2010")
    if "--mutation=conjoncture" in sys.argv:   # témoin positif : la baisse des recettes corrigées disparaît après 2022
        for a in range(FEN_CS["apres"][0], fin + 1):
            out[a]["ce_rec"] += 1.6
            out[a]["ce_ca"] += 1.6
    return out


def moy_cs(cs, cle, fen, fin):
    a0, a1 = fen[0], fen[1] or fin
    return sum(cs[a][cle] for a in range(a0, a1 + 1)) / (a1 - a0 + 1)


# Fenêtres des deux lectures institutionnelles du creusement récent du déficit (None = dernière année publiée).
FENETRES_DEFICIT = {"ofce": (2017, 2024), "tresor": (2019, None)}
# Clés d'affichage dérivées (relecture de langue du 11/10/2026) : <clé>_abs, la valeur sans signe après un verbe de sens ;
# <clé>_pt, « point » ou « points » accordé à la valeur affichée.
VALEURS_SANS_SIGNE = ("tc_avant", "tc_apres", "rec_fin",
                      "p1_hausse", "p2_hausse", "p3_hausse", "p1_taux_croissance")   # « gagne », « ajoute » (motif de check-rendu, 11/10)
ACCORD_POINTS = ("effet_net", "ofce_rec", "ofce_dep", "tresor_dep_hi", "croise_dep_hi", "croise_dep", "rec_fin")


def agreger(rows, a0, a1):
    s = [r for r in rows if a0 <= r["annee"] <= a1]
    return {k: sum(r[k] for r in s) for k in ("variation", "effet_interets", "effet_croissance", "effet_taux_croissance",
                                               "contribution_solde_primaire", "flux_stock")}


# ------------------------------------------------------------------ figures
# Textes des figures, par langue. Le dessin est commun : seules les chaînes et le format des nombres changent.
# Les modèles français sont ceux d'origine, recopiés à l'identique (les sorties FR ne doivent pas bouger d'un octet).
TXT = {
    "fr": {
        "licence": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL,
        "pc": " %",
        "etapes": ("Dette fin %d", "Effet des intérêts", "Croissance du PIB nominal", "Déficits primaires",
                   "Ajustements flux-stock"),
        "titre_cascade": "Pourquoi la dette a doublé : de %s %% à %s %% du PIB, %d-%d",
        "desc_cascade": ("Cascade en points de PIB. La dette part de %s %% fin %d. Les intérêts l'auraient poussée de %s points, mais la "
                         "croissance du PIB nominal en a effacé %s : leur effet net est de %s point. Les déficits primaires, hors intérêts, "
                         "ajoutent %s points, les ajustements flux-stock %s. La dette atteint %s %% fin %d. Décomposition comptable, non causale."),
        "legende_cascade": "En points de PIB : bleu, le stock ; orange, ce qui le fait monter ; gris, ce qui le fait baisser.",
        "src_cascade": "Eurostat gov_10dd_edpt1 (dette), gov_10a_main (B9, D41PAY), PIB de la notification, France, %d-%d ; mises à jour Eurostat du %s et du %s",
        "note_cascade": ("Contributions cumulées au ratio, en points de PIB : ni des sommes versées, ni des causes. "
                         "Totaux calculés avant arrondi, d'où un dixième d'écart possible."),
        "titre_annuelle": "Année par année : ce qui a fait monter ou baisser le ratio dette/PIB, %d-%d",
        "desc_annuelle": ("Barres empilées par année, en points de PIB : en orange la contribution du solde primaire (déficit en plus, excédent en moins), en bleu l'effet "
                          "net des taux et de la croissance, en gris les ajustements flux-stock ; le point noir est la variation effective du "
                          "ratio. Les deux plus fortes hausses sont en 2009 (+%s points) et en 2020 (+%s). De 2021 à 2023, l'effet "
                          "taux-croissance retire %s points au ratio, quand la croissance du PIB nominal, hausse des prix comprise, s'accélère."),
        "legende_annuelle": ("contribution du solde primaire", "effet taux-croissance", "ajustements flux-stock", "variation du ratio"),
        "src_annuelle": "Eurostat gov_10dd_edpt1, gov_10a_main (B9, D41PAY), France, %d-%d ; mises à jour Eurostat du %s et du %s",
        "note_annuelle": ("Points de PIB par an ; solde primaire : un déficit compte en plus, un excédent en moins ; la somme "
                          "des trois barres égale la variation (point noir), au centième près."),
        "montre_cascade": ("Sur la période, les intérêts et la croissance nominale se sont presque annulés ; la hausse de la dette "
                           "tient pour l'essentiel aux déficits primaires, hors intérêts."),
        "montre_annuelle": ("Année par année, ce qui a poussé ou freiné le ratio ; en 2021-2023, la croissance nominale l'a fait baisser "
                            "malgré les déficits."),
        "titre_cascade_m": "Dette publique : de %s %% à %s %% du PIB, %d-%d",
        "titre_annuelle_m": "Chaque année, ce qui a poussé ou freiné le ratio dette/PIB",
        "faits_m": ("2009 : %s points", "2020 : %s points", "2021-2023 : effet taux-croissance −%s"),
        "points": "en points de PIB ; + fait monter, − fait baisser",
        "titre_cs": "Le déficit primaire corrigé du cycle, selon trois estimations, %d-%d",
        "desc_cs": ("Courbes en %% du PIB potentiel. Solde primaire corrigé du cycle selon le FMI, depuis %d ; solde primaire structurel "
                    "selon la Commission européenne et solde primaire sous-jacent selon l'OCDE, depuis 2010 ; en gris, le solde primaire "
                    "observé (Eurostat, %% du PIB). Moyennes %s puis %s : Commission %s puis %s, FMI %s puis %s, OCDE %s puis %s. "
                    "Au-dessous de zéro, un déficit."),
        "legende_cs": ("FMI, corrigé du cycle", "Commission, structurel", "OCDE, sous-jacent", "observé (Eurostat)"),
        "src_cs": "FMI, %s ; Commission européenne, %s ; OCDE, %s ; Eurostat gov_10a_main, mise à jour du %s",
        "note_cs": ("Trois méthodes : la Commission et l'OCDE retirent aussi les mesures ponctuelles, le FMI non. Estimations de la "
                    "production potentielle, non des mesures ; zones grises : %s et %s."),
        "montre_cs": ("Corrigé du cycle, le déficit primaire d'après 2022 reste plus creusé qu'en 2015-2019 dans les trois estimations : "
                      "la conjoncture ne l'explique pas."),
        "titre_cs_m": "Déficit primaire corrigé du cycle, trois estimations",
        "faits_cs_m": ("Commission : %s, puis %s", "FMI : %s, puis %s", "OCDE : %s, puis %s"),
        "unite_cs_m": "moyennes %s puis %s, en %% du PIB potentiel",
    },
    # Terminologie reprise de la page anglaise « Combien coûte » (implicit interest rate, general government, primary
    # deficits, stock-flow adjustments, nominal GDP growth, interest paid).
    "en": {
        "licence": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN,
        "pc": "%",
        "etapes": ("Debt, end %d", "Interest effect", "Nominal GDP growth", "Primary deficits", "Stock-flow adjustments"),
        "titre_cascade": "Why the debt doubled: from %s%% to %s%% of GDP, %d-%d",
        "desc_cascade": ("Waterfall chart in points of GDP. The debt starts at %s%% at the end of %d. Interest would have pushed it up by "
                         "%s points, but nominal GDP growth erased %s: their net effect is %s points. Primary deficits, excluding "
                         "interest, add %s points, stock-flow adjustments %s. The debt reaches %s%% at the end of %d. Accounting "
                         "decomposition, not a causal one."),
        "legende_cascade": "In points of GDP: blue, the stock; orange, what pushes it up; grey, what pushes it down.",
        "src_cascade": "Eurostat gov_10dd_edpt1 (debt), gov_10a_main (B9, D41PAY), notification GDP, France, %d-%d; Eurostat releases of %s and %s",
        "note_cascade": ("Cumulative contributions to the ratio, in points of GDP: neither amounts paid nor causes. "
                         "Totals computed before rounding, hence a possible gap of a tenth."),
        "titre_annuelle": "Year by year: what pushed the debt-to-GDP ratio up or down, %d-%d",
        "desc_annuelle": ("Stacked bars per year, in points of GDP: in orange the primary balance contribution (deficit as plus, surplus as minus), in blue the net "
                          "effect of interest rates and growth, in grey stock-flow adjustments; the black dot is the actual change in "
                          "the ratio. The two largest rises are in 2009 (+%s points) and 2020 (+%s). From 2021 to 2023, the "
                          "interest-growth effect takes %s points off the ratio, as nominal GDP growth, price rises included, accelerates."),
        "legende_annuelle": ("primary balance contribution", "interest-growth effect", "stock-flow adjustments", "change in the ratio"),
        "src_annuelle": "Eurostat gov_10dd_edpt1, gov_10a_main (B9, D41PAY), France, %d-%d; Eurostat releases of %s and %s",
        "note_annuelle": ("Points of GDP per year; primary balance: a deficit counts as plus, a surplus as minus; the three "
                          "bars add up to the change (black dot), to within a hundredth."),
        "montre_cascade": ("Over the period, interest and nominal growth almost cancelled out; the rise in the debt is mostly due to "
                           "primary deficits, excluding interest."),
        "montre_annuelle": ("Year by year, what pushed the ratio up or held it back; in 2021-2023, nominal growth brought it down "
                            "despite the deficits."),
        "titre_cascade_m": "Public debt: from %s%% to %s%% of GDP, %d-%d",
        "titre_annuelle_m": "Each year, what pushed the debt-to-GDP ratio up or held it back",
        "faits_m": ("2009: %s points", "2020: %s points", "2021-2023: interest-growth effect −%s"),
        "points": "in points of GDP; + pushes up, − pulls down",
        "titre_cs": "The cyclically adjusted primary deficit, according to three estimates, %d-%d",
        "desc_cs": ("Lines as %% of potential GDP. Cyclically adjusted primary balance according to the IMF, since %d; structural "
                    "primary balance according to the European Commission and underlying primary balance according to the OECD, "
                    "since 2010; in grey, the observed primary balance (Eurostat, %% of GDP). Averages %s then %s: Commission %s then "
                    "%s, IMF %s then %s, OECD %s then %s. Below zero, a deficit."),
        "legende_cs": ("IMF, cyclically adjusted", "Commission, structural", "OECD, underlying", "observed (Eurostat)"),
        "src_cs": "IMF, %s; European Commission, %s; OECD, %s; Eurostat gov_10a_main, release of %s",
        "note_cs": ("Three methods: the Commission and the OECD also remove one-off measures, the IMF does not. Estimates of "
                    "potential output, not measurements; grey bands: %s and %s."),
        "montre_cs": ("Cyclically adjusted, the primary deficit after 2022 remains deeper than in 2015-2019 in all three estimates: "
                      "the business cycle does not explain it."),
        "titre_cs_m": "Cyclically adjusted primary deficit, three estimates",
        "faits_cs_m": ("Commission: %s, then %s", "IMF: %s, then %s", "OECD: %s, then %s"),
        "unite_cs_m": "averages %s then %s, as %% of potential GDP",
    },
}
NB = {"fr": (fr, signe), "en": (en, signe_en)}   # même calcul, deux présentations
SUFFIXE = {"fr": "", "en": "-en"}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def entete(h, ident, titre, desc):
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h + 52, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + 52),
            '<text x="0" y="18" font-size="15" font-weight="600" fill="%s">%s</text>' % (INK, esc(titre))]


def pied(e, y0, source, note, lang="fr"):
    """Pied commun (11 px, retour à la ligne, hauteur suivie) : scripts/pied_figure.py, phase B du 11/10/2026."""
    return pied_figure.pied(e, y0, W, [(source, INK2, "pied-source"), (note, INK2, "pied-note"),
                                       (TXT[lang]["licence"], MUTED, "pied-licence")], GRID)


def fig_cascade(a0, d_depart, rows, total, lang="fr"):
    """Figure signature : de la dette de départ à la dette d'arrivée, en quatre marches."""
    T, (nb, sg) = TXT[lang], NB[lang]
    an_fin = rows[-1]["annee"]
    etapes = [(T["etapes"][0] % a0, d_depart, "stock"),
              (T["etapes"][1], total["effet_interets"], "delta"),
              (T["etapes"][2], total["effet_croissance"], "delta"),
              (T["etapes"][3], total["contribution_solde_primaire"], "delta"),
              (T["etapes"][4], total["flux_stock"], "delta"),
              (T["etapes"][0] % an_fin, rows[-1]["dette_pct_pib"], "stock")]
    H, X0, X1, TOP, BAS = 330, 40, W - 10, 70, 290
    haut = max(d_depart + max(0, total["effet_interets"]), rows[-1]["dette_pct_pib"]) * 1.08
    vmax = (int(haut / 20) + 1) * 20

    def Y(v):
        return BAS - (BAS - TOP) * v / vmax

    titre = T["titre_cascade"] % (nb(d_depart), nb(rows[-1]["dette_pct_pib"]), a0, an_fin)
    desc = (T["desc_cascade"]
            % (nb(d_depart), a0, nb(total["effet_interets"]), nb(-total["effet_croissance"]), sg(total["effet_taux_croissance"]),
               nb(total["contribution_solde_primaire"]), sg(total["flux_stock"]), nb(rows[-1]["dette_pct_pib"]), an_fin))
    e = entete(H, "dc", titre, desc)
    for g in range(0, vmax + 1, 20):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.2 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%d%s</text>' % (X0 - 6, Y(g) + 3, MUTED, g, T["pc"]))
    n = len(etapes)
    pas = (X1 - X0) / n
    bw = pas * 0.58
    niveau = 0.0
    for k, (lib, v, nature) in enumerate(etapes):
        cx = X0 + pas * (k + 0.5)
        if nature == "stock":
            bas_v, haut_v, col = 0.0, v, BLEU
            niveau = v
            etiq = nb(v) + T["pc"]
        else:
            bas_v, haut_v = (niveau, niveau + v) if v >= 0 else (niveau + v, niveau)
            col = ORANGE if v >= 0 else GRIS
            etiq = sg(v)
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
    e.append('<text x="%d" y="44" font-size="11" fill="%s">%s</text>' % (X0, INK2, esc(T["legende_cascade"])))
    return pied(e, H + 4, T["src_cascade"] % ((a0 + 1, an_fin) + (millesime("gov_10dd_edpt1", lang), millesime("gov_10a_main", lang))), T["note_cascade"], lang)


def fig_annuelle(rows, lang="fr"):
    """Chaque année : ce qui a poussé ou freiné le ratio, et la variation effective (point)."""
    T, (nb, sg) = TXT[lang], NB[lang]
    a0, a1 = rows[0]["annee"], rows[-1]["annee"]
    H, X0, X1, TOP, BAS = 300, 40, W - 10, 70, 270
    hauts = [max(0, r["effet_taux_croissance"]) + max(0, r["contribution_solde_primaire"]) + max(0, r["flux_stock"]) for r in rows]
    bas_ = [min(0, r["effet_taux_croissance"]) + min(0, r["contribution_solde_primaire"]) + min(0, r["flux_stock"]) for r in rows]
    vmax, vmin = (int(max(hauts) / 4) + 1) * 4, -(int(-min(bas_) / 4) + 1) * 4

    def Y(v):
        return BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)

    titre = T["titre_annuelle"] % (a0, a1)
    by = {r["annee"]: r for r in rows}
    desc = T["desc_annuelle"] % (nb(by[2009]["variation"]), nb(by[2020]["variation"]),
                                 nb(-sum(r["effet_taux_croissance"] for r in rows if 2021 <= r["annee"] <= 2023)))
    e = entete(H, "da", titre, desc)
    for g in range(vmin, vmax + 1, 4):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(g) + 3, MUTED, sg(g, 0)))
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
    leg = list(zip((ORANGE, BLEU, GRIS_CLAIR), T["legende_annuelle"][:3]))
    x = X0
    for col, lib in leg:
        e.append('<rect x="%d" y="36" width="10" height="10" fill="%s"/>' % (x, col))
        e.append('<text x="%d" y="45" font-size="11" fill="%s">%s</text>' % (x + 14, INK2, esc(lib)))
        x += 14 + int(5.6 * len(lib)) + 18   # 7 px par caractère sortaient la 4e entrée du cadre (contre-expertise du 11/10/2026)
    e.append('<circle cx="%d" cy="41" r="3.2" fill="%s"/>' % (x + 4, INK))
    e.append('<text x="%d" y="45" font-size="11" fill="%s">%s</text>' % (x + 12, INK2, esc(T["legende_annuelle"][3])))
    return pied(e, H + 4, T["src_annuelle"] % ((a0, a1) + (millesime("gov_10dd_edpt1", lang), millesime("gov_10a_main", lang))), T["note_annuelle"], lang)


def _cs_series(cs):
    ans = sorted(cs)
    return ans, [("fmi_ca", BLEU, None, ans), ("ce_st", INK, None, [a for a in ans if a >= 2010]),
                 ("ocde", INK2, "5 3", [a for a in ans if a >= 2010]), ("obs", GRIS_CLAIR, None, ans)]


def _cs_moyennes(cs, nb):
    fin = max(cs)
    vals = []
    for cle in ("ce_st", "fmi_ca", "ocde"):
        vals += [sg_cs(moy_cs(cs, cle, FEN_CS["avant"], fin), nb), sg_cs(moy_cs(cs, cle, FEN_CS["apres"], fin), nb)]
    return vals


def sg_cs(v, nb):
    return nb(v, 1)


def _lib_fen(cle, fin):
    a0, a1 = FEN_CS[cle][0], FEN_CS[cle][1] or fin
    return "%d-%d" % (a0, a1)


def fig_cs(cs, lang="fr"):
    """Trois estimations du solde primaire corrigé du cycle, et le solde observé ; deux fenêtres grisées."""
    T, (nb, sg) = TXT[lang], NB[lang]
    ans, series = _cs_series(cs)
    fin = ans[-1]
    H, X0, X1, TOP, BAS = 290, 40, W - 10, 78, 262
    vals = [cs[a][c] for c, _, _, aa in series for a in aa]
    vmax, vmin = 2, -(int(-min(vals) / 2) + 1) * 2
    X = lambda a: X0 + (X1 - X0) * (a - ans[0]) / (fin - ans[0])
    Y = lambda v: BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)
    av, ap = _lib_fen("avant", fin), _lib_fen("apres", fin)
    m = _cs_moyennes(cs, nb)
    desc = T["desc_cs"] % ((ans[0], av, ap) + tuple(m[0:2] + m[2:4] + m[4:6]))
    e = entete(H, "dcs", T["titre_cs"] % (ans[0], fin), desc)
    for k in ("avant", "apres"):
        a0, a1 = FEN_CS[k][0], FEN_CS[k][1] or fin
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#f1efec"/>' % (X(a0 - 0.5), TOP, min(X(a1 + 0.5), X1) - X(a0 - 0.5), BAS - TOP))
    for g in range(vmin, vmax + 1, 2):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%s</text>' % (X0 - 6, Y(g) + 3, MUTED, sg(g, 0) if g else "0"))
    for a in ans:
        if a % 5 == 0 or a == fin:
            e.append('<text x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="%s">%d</text>' % (X(a), BAS + 14, INK2, "end" if a == fin else "middle", a))
    for cle, col, dash, aa in reversed(series):
        pts = " ".join("%.1f,%.1f" % (X(a), Y(cs[a][cle])) for a in aa)
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
                 % (pts, col, 2.2 if cle != "obs" else 1.6, ' stroke-dasharray="%s"' % dash if dash else ""))
    x = X0
    for (cle, col, dash, _), lib in zip(series, T["legende_cs"]):
        e.append('<line x1="%d" y1="41" x2="%d" y2="41" stroke="%s" stroke-width="2.4"%s/>' % (x, x + 16, col, ' stroke-dasharray="%s"' % dash if dash else ""))
        e.append('<text x="%d" y="45" font-size="11" fill="%s">%s</text>' % (x + 20, INK2, esc(lib)))
        x += 20 + int(5.6 * len(lib)) + 16
    E = EDITIONS_CS[lang]
    return pied(e, H + 4, T["src_cs"] % (E["fmi"], E["ameco"], E["ocde"], millesime("gov_10a_main", lang)), T["note_cs"] % (av, ap), lang)


# ------------------------------------------------------------------ figures téléphone (phase B, 11/10/2026)
# Composées pour 300 px, jamais rétrécies ; police minimale FS_MIN ; parité contrôlée contre la version détaillée
# (pied_figure.parite). Patron : scripts/update_lycee_professeurs.py.
WM, FS_MIN = 300, 13.5
LICENCE_M = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com", "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}


def tete_m(ident, titre, desc):
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (WM, ident, ident, FONT),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
         '<rect width="%d" height="0" fill="#ffffff"/>' % WM]
    lignes = pied_figure.coupe(titre, 30)
    for k, l in enumerate(lignes):
        e.append('<text x="0" y="%d" font-size="17" font-weight="600" fill="%s">%s</text>' % (20 + 22 * k, INK, esc(l)))
    return e, 20 + 22 * len(lignes)


def finir_m(e, y0, source, note, lang):
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, WM, y0, GRID))
    y = y0 + 4
    for tx, col in ((source, INK2), (note, INK2), (LICENCE_M[lang], MUTED)):
        for l in pied_figure.coupe(tx, 38):
            y += 17
            e.append('<text x="0" y="%.1f" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, col, esc(l)))
        y += 4
    e.append("</svg>")
    h = y + 6
    out = "\n".join(e)
    return out.replace('viewBox="0 0 %d 0"' % WM, 'viewBox="0 0 %d %d"' % (WM, h), 1).replace(
        '<rect width="%d" height="0"' % WM, '<rect width="%d" height="%d"' % (WM, h), 1)


def desc_de(svg):
    return html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S).group(1))


def fig_cascade_m(a0, d_depart, rows, total, lang, svg_d):
    """Cascade couchée : une ligne par marche (libellé, valeur), une barre sous chaque ligne, de son niveau de départ à son niveau d'arrivée."""
    T, (nb, sg) = TXT[lang], NB[lang]
    an_fin = rows[-1]["annee"]
    e, y = tete_m("dcm", T["titre_cascade_m"] % (nb(d_depart), nb(rows[-1]["dette_pct_pib"]), a0, an_fin), desc_de(svg_d))
    etapes = [(T["etapes"][0] % a0, d_depart, "stock"), (T["etapes"][1], total["effet_interets"], "delta"),
              (T["etapes"][2], total["effet_croissance"], "delta"), (T["etapes"][3], total["contribution_solde_primaire"], "delta"),
              (T["etapes"][4], total["flux_stock"], "delta"), (T["etapes"][0] % an_fin, rows[-1]["dette_pct_pib"], "stock")]
    haut = max(d_depart + max(0, total["effet_interets"]), rows[-1]["dette_pct_pib"]) * 1.04
    sx = lambda v: (WM - 4) * v / haut
    y += 4
    for l in pied_figure.coupe(T["points"], 38):   # la ligne dépassait le cadre de 300 px (contre-expertise du 11/10/2026)
        y += 18
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    niveau = 0.0
    for lib, v, nature in etapes:
        y += 30
        etiq = (nb(v) + T["pc"]) if nature == "stock" else sg(v)
        e.append('<text x="0" y="%d" font-size="15" fill="%s">%s</text>' % (y, INK, esc(lib)))
        e.append('<text x="%d" y="%d" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (WM, y, INK, esc(etiq)))
        y += 8
        if nature == "stock":
            a, b, col, niveau = 0.0, v, BLEU, v
        else:
            a, b = (niveau, niveau + v) if v >= 0 else (niveau + v, niveau)
            col = ORANGE if v >= 0 else GRIS
            niveau += v
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="14" fill="%s"/>' % (sx(a), y, max(1.5, sx(b) - sx(a)), col))
        y += 14
    return finir_m(e, y + 18, T["src_cascade"] % ((a0 + 1, an_fin) + (millesime("gov_10dd_edpt1", lang), millesime("gov_10a_main", lang))), T["note_cascade"], lang)


def fig_annuelle_m(rows, lang, svg_d):
    T, (nb, sg) = TXT[lang], NB[lang]
    e, y = tete_m("dam", T["titre_annuelle_m"], desc_de(svg_d))
    hauts = [max(0, r["effet_taux_croissance"]) + max(0, r["contribution_solde_primaire"]) + max(0, r["flux_stock"]) for r in rows]
    bas_ = [min(0, r["effet_taux_croissance"]) + min(0, r["contribution_solde_primaire"]) + min(0, r["flux_stock"]) for r in rows]
    vmax, vmin = (int(max(hauts) / 4) + 1) * 4, -(int(-min(bas_) / 4) + 1) * 4
    X0, X1, TOP = 30, WM - 2, y + 26
    BAS = TOP + 210
    Y = lambda v: BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)
    for g in range(vmin, vmax + 1, 8):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%s</text>' % (X0 - 4, Y(g) + 4, FS_MIN, MUTED, sg(g, 0)))
    pas = (X1 - X0) / len(rows)
    bw = pas * 0.72
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
        e.append('<circle cx="%.1f" cy="%.1f" r="2.4" fill="%s"/>' % (cx, Y(r["variation"]), INK))
        if r["annee"] in (2000, 2010, 2020):
            e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="middle">%d</text>' % (cx, BAS + 18, FS_MIN, INK2, r["annee"]))
    y = BAS + 30
    for col, lib in zip((ORANGE, BLEU, GRIS_CLAIR), T["legende_annuelle"][:3]):
        y += 22
        e.append('<rect x="0" y="%d" width="14" height="14" fill="%s"/>' % (y - 12, col))
        e.append('<text x="22" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(lib)))
    y += 22
    e.append('<circle cx="7" cy="%d" r="4" fill="%s"/>' % (y - 5, INK))
    e.append('<text x="22" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(T["legende_annuelle"][3])))
    by = {r["annee"]: r for r in rows}
    eff = -sum(r["effet_taux_croissance"] for r in rows if 2021 <= r["annee"] <= 2023)
    y += 12
    for f in (T["faits_m"][0] % sg(by[2009]["variation"]), T["faits_m"][1] % sg(by[2020]["variation"]), T["faits_m"][2] % nb(eff)):
        for k, l in enumerate(pied_figure.coupe(f, 30)):   # 15 px gras : au-delà de 30 caractères, la ligne touchait le bord
            y += 22 if k == 0 else 19
            e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(l)))
    return finir_m(e, y + 18, T["src_annuelle"] % ((rows[0]["annee"], rows[-1]["annee"]) + (millesime("gov_10dd_edpt1", lang), millesime("gov_10a_main", lang))), T["note_annuelle"], lang)


def fig_cs_m(cs, lang, svg_d):
    T, (nb, sg) = TXT[lang], NB[lang]
    ans, series = _cs_series(cs)
    fin = ans[-1]
    e, y = tete_m("dcsm", T["titre_cs_m"], desc_de(svg_d))
    av, ap = _lib_fen("avant", fin), _lib_fen("apres", fin)
    vals = [cs[a][c] for c, _, _, aa in series for a in aa]
    vmax, vmin = 2, -(int(-min(vals) / 2) + 1) * 2
    X0, X1, TOP = 30, WM - 2, y + 16
    BAS = TOP + 190
    X = lambda a: X0 + (X1 - X0) * (a - ans[0]) / (fin - ans[0])
    Y = lambda v: BAS - (BAS - TOP) * (v - vmin) / (vmax - vmin)
    for k in ("avant", "apres"):
        a0, a1 = FEN_CS[k][0], FEN_CS[k][1] or fin
        e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#f1efec"/>' % (X(a0 - 0.5), TOP, min(X(a1 + 0.5), X1) - X(a0 - 0.5), BAS - TOP))
    for g in range(vmin, vmax + 1, 4):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (X0, Y(g), X1, Y(g), GRID, 1.4 if g == 0 else 0.6))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%s</text>' % (X0 - 4, Y(g) + 4, FS_MIN, MUTED, sg(g, 0) if g else "0"))
    for a in (2000, 2010, 2020):
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="middle">%d</text>' % (X(a), BAS + 18, FS_MIN, INK2, a))
    for cle, col, dash, aa in reversed(series):
        pts = " ".join("%.1f,%.1f" % (X(a), Y(cs[a][cle])) for a in aa)
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
                 % (pts, col, 2.2 if cle != "obs" else 1.6, ' stroke-dasharray="%s"' % dash if dash else ""))
    y = BAS + 26
    for (cle, col, dash, _), lib in zip(series, T["legende_cs"]):
        y += 22
        e.append('<line x1="0" y1="%d" x2="16" y2="%d" stroke="%s" stroke-width="2.6"%s/>' % (y - 5, y - 5, col, ' stroke-dasharray="%s"' % dash if dash else ""))
        e.append('<text x="22" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(lib)))
    y += 14
    for l in pied_figure.coupe(T["unite_cs_m"] % (av, ap), 38):
        y += 18
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    m = _cs_moyennes(cs, nb)
    for f in (T["faits_cs_m"][0] % tuple(m[0:2]), T["faits_cs_m"][1] % tuple(m[2:4]), T["faits_cs_m"][2] % tuple(m[4:6])):
        for k, l in enumerate(pied_figure.coupe(f, 30)):
            y += 22 if k == 0 else 19
            e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(l)))
    E = EDITIONS_CS[lang]
    return finir_m(e, y + 18, T["src_cs"] % (E["fmi"], E["ameco"], E["ocde"], millesime("gov_10a_main", lang)), T["note_cs"] % (av, ap), lang)


def fiches(figs, A):
    out = {}
    for lang in ("fr", "en"):
        T, suf = TXT[lang], SUFFIXE[lang]
        MONTRE = [("cascade", "dette-dynamique-cascade" + suf, T["montre_cascade"]),
                  ("annuelle", "dette-dynamique-annuelle" + suf, T["montre_annuelle"]),
                  ("conjoncture", "dette-dynamique-conjoncture" + suf, T["montre_cs"])]
        out[lang] = []
        for ident, f, montre in MONTRE:
            svg = figs[f + ".svg"]
            titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [pied_figure.lire(svg, "pied-source"), pied_figure.lire(svg, "pied-note")]
            out[lang].append(dict(id=ident, fichier=f, titre=titre, montre=montre, source=cart[0], precaution=cart[1]))
    return out


def csv_texte(rows, cs):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    cles = ["annee", "dette_pct_pib", "variation", "effet_interets", "effet_croissance", "effet_taux_croissance",
            "contribution_solde_primaire", "flux_stock", "taux_implicite_pct", "croissance_nominale_pct", "solde_primaire_pct_pib"]
    # Conjoncture ou structure (19/10/2026) : mêmes lignes, colonnes des trois producteurs (vide = non publié cette année)
    cles_cs = [("ce_st", "commission_solde_primaire_structurel_pct_pib_potentiel"), ("ce_rec", "commission_recettes_corrigees_pct_pib_potentiel"),
               ("ce_dep", "commission_depenses_hors_interets_corrigees_pct_pib_potentiel"), ("fmi_ca", "fmi_solde_primaire_corrige_pct_pib_potentiel"),
               ("ocde", "ocde_solde_primaire_sous_jacent_pct_pib_potentiel")]
    w.writerow(cles + [n for _, n in cles_cs])
    for r in rows:
        c = cs[r["annee"]]
        w.writerow([r["annee"]] + ["%.3f" % r[k] for k in cles[1:]] + ["" if c[k] is None else "%.3f" % c[k] for k, _ in cles_cs])
    return buf.getvalue()


# ------------------------------------------------------------------ affichage et gardes
def dette_insee_fin(annee: int):
    """Dette de Maastricht au T4 de la derniere annee selon l'INSEE (data/dette_officielle.json, jeu du volet 2), pour
    dire l'ecart avec la notification d'Eurostat que la page utilise d'un bout a l'autre (OPTIMUM-15). Absente : None."""
    try:
        o = json.loads((ROOT / "data" / "dette_officielle.json").read_text(encoding="utf-8"))
        return float(o["dette_trimestrielle"]["series"]["pct_pib"]["%d-Q4" % annee])
    except (OSError, ValueError, KeyError):
        return None


def affichage(a0, d_depart, rows, total, per, dr, cs):
    """Rend (affichage, affichage_en) : deux présentations d'un seul corps de valeurs, puis les gardes (une passe,
    numérique, valable pour les deux langues)."""
    last = rows[-1]
    insee_fin = dette_insee_fin(last["annee"])
    infl = [r for r in rows if 2021 <= r["annee"] <= 2023]
    by = {r["annee"]: r for r in rows}

    # Deux présentations, UN SEUL corps (même règle que bloc_affichage de update_dette_insee.py) : les blocs ne
    # peuvent diverger que sur le format, jamais sur les valeurs ni sur les clés.
    def bloc(nb, sg):
        A = {"annee_depart": str(a0), "annee_premiere_variation": str(a0 + 1), "annee_fin": str(last["annee"]), "dette_depart": nb(d_depart), "dette_fin": nb(last["dette_pct_pib"]),
             "hausse": nb(total["variation"]), "effet_interets": nb(total["effet_interets"]),
             "effet_croissance": nb(-total["effet_croissance"]), "effet_net": sg(total["effet_taux_croissance"]),
             "deficits_primaires": nb(total["contribution_solde_primaire"]), "flux_stock": sg(total["flux_stock"]),
             "part_deficits": nb(100 * total["contribution_solde_primaire"] / total["variation"], 0)}
        for (a, b, lib), t in zip(PERIODES, per):
            k = "p%d" % (PERIODES.index((a, b, lib)) + 1)  # brut-ok: numero d'une periode dans une liste fixe
            A[k + "_lib"] = lib if b else lib % last["annee"]
            A[k + "_hausse"] = sg(t["variation"])
            A[k + "_taux_croissance"] = sg(t["effet_taux_croissance"])
            A[k + "_deficits"] = sg(t["contribution_solde_primaire"])
            A[k + "_flux"] = sg(t["flux_stock"])
        A["effet_2021_2023"] = nb(-sum(r["effet_taux_croissance"] for r in infl))
        A["deficits_2021_2023"] = nb(sum(r["contribution_solde_primaire"] for r in infl))
        # recul OBSERVÉ du ratio en 2021-2023, cité par la page « inflation » pour que -16,8 ne se lise pas comme la baisse
        # du ratio (contre-expertise OPTIMUM-27, 11/10/2026) ; sans signe : la prose dit « a reculé de »
        A["recul_2021_2023"] = nb(-sum(r["variation"] for r in infl))
        for a in (2009, 2020):
            A["hausse_%d" % a] = nb(by[a]["variation"])
            A["deficits_%d" % a] = nb(by[a]["contribution_solde_primaire"])
            A["taux_croissance_%d" % a] = nb(by[a]["effet_taux_croissance"])
        A["net_dernier"] = sg(last["effet_taux_croissance"])
        A["taux_implicite_dernier"] = nb(last["taux_implicite_pct"], 2)
        A["croissance_derniere"] = nb(last["croissance_nominale_pct"], 2)   # même précision que le taux implicite (OPTIMUM-10)
        A["annees_excedent"] = str(sum(1 for r in rows if r["solde_primaire_pct_pib"] > 0))
        A["annees_total"] = str(len(rows))
        # « Ce qu'il faut retenir » (03/10/2026) : la quasi-annulation sur la série est une compensation DANS LE TEMPS
        # (Trésor-Éco n° 334, E7-E8 ; Note du CAE n° 82, E4-E5). Bascule = première année à partir de laquelle l'effet
        # taux-croissance est négatif chaque année, hors années de recul du PIB nominal.
        A["tc_bascule"] = str(bascule)
        A["tc_avant"] = sg(sum(r["effet_taux_croissance"] for r in rows if r["annee"] < bascule))
        A["tc_apres"] = sg(sum(r["effet_taux_croissance"] for r in rows if r["annee"] >= bascule))
        # Troisième tour (Trésor-Éco n° 403) : « relative stabilité » 2001-2007 éprouvée ; fenêtres OFCE et DG Trésor.
        A["dette_2001"], A["dette_2007"] = nb(by[2001]["dette_pct_pib"]), nb(by[2007]["dette_pct_pib"])
        for k, (d0, d1) in fen.items():
            A[k + "_debut"], A[k + "_fin"] = str(d0), str(d1)
            for v, cle in (("solde", "_solde"), ("recettes", "_rec"), ("depenses_hors_interets", "_dep_hi"), ("depenses", "_dep")):
                A[k + cle] = sg(dr[d1][v] - dr[d0][v])
        # Contre-expertise PRO-20261003-172718 (T-7, T-9) : même convention (hors intérêts) et fenêtre croisée.
        A["entre_dep_hi"] = sg(dr[fen["tresor"][0]]["depenses_hors_interets"] - dr[fen["ofce"][0]]["depenses_hors_interets"])
        A["croise_rec"] = sg(dr[fen["ofce"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"])
        # Quatrième tour (document de travail de l'OFCE, E6) : sur la fenêtre commune, dépenses totales.
        A["croise_dep"] = sg(dr[fen["ofce"][1]]["depenses"] - dr[fen["tresor"][0]]["depenses"])
        # Phase B (contre-expertise du 11/10/2026, D15) : fenêtre commune, dépenses hors intérêts.
        A["croise_dep_hi"] = sg(dr[fen["ofce"][1]]["depenses_hors_interets"] - dr[fen["tresor"][0]]["depenses_hors_interets"])
        # Contre-expertise de la page construite (OPTIMUM-10) : le retournement entre les deux fenêtres de même départ.
        A["rec_fin"] = sg(dr[fen["tresor"][1]]["recettes"] - dr[fen["ofce"][1]]["recettes"])
        # OPTIMUM-15 : marge du retournement sur la fenetre du Tresor (hausse des depenses hors interets moins recul
        # des recettes, en points de PIB), et valeur de l'INSEE pour la derniere fin d'annee.
        A["tresor_marge"] = nb(abs((dr[fen["tresor"][1]]["depenses_hors_interets"] - dr[fen["tresor"][0]]["depenses_hors_interets"])
                                   + (dr[fen["tresor"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"])))
        A["dette_insee_fin"] = nb(insee_fin) if insee_fin is not None else ""
        A["ti_creux_an"] = str(lg.extremum(rows, lambda r: r["taux_implicite_pct"], 2, maxi=False)["annee"])
        A["ti_creux"] = nb(min(r["taux_implicite_pct"] for r in rows), 2)
        A["ti_2021"], A["ti_2022"] = nb(by[2021]["taux_implicite_pct"], 2), nb(by[2022]["taux_implicite_pct"], 2)
        # Conjoncture ou structure (19/10/2026) : valeurs des trois producteurs, jamais leur moyenne.
        fin_ = last["annee"]
        M = lambda cle, k: moy_cs(cs, cle, FEN_CS[k], fin_)
        for k in ("avant", "apres", "long", "crise"):
            A["cs_%s_lib" % k] = _lib_fen(k, fin_)
        A["cs_apres_debut"] = str(FEN_CS["apres"][0])
        for cle, nom in (("ce_st", "ce"), ("fmi_ca", "fmi"), ("ocde", "ocde")):
            A["cs_%s_avant" % nom], A["cs_%s_apres" % nom] = nb(M(cle, "avant")), nb(M(cle, "apres"))
            A["cs_%s_saut" % nom] = nb(abs(M(cle, "apres") - M(cle, "avant")))
        A["cs_fmi_long"], A["cs_fmi_crise"] = nb(M("fmi_ca", "long")), nb(M("fmi_ca", "crise"))
        A["cs_ce_conj"] = nb(abs(M("obs", "apres") - M("ce_st", "apres")), 2)
        A["cs_fmi_conj"] = nb(abs(M("fmi_obs", "apres") - M("fmi_ca", "apres")), 2)
        A["cs_rec"] = nb(abs(M("ce_rec", "apres") - M("ce_rec", "avant")), 2)
        A["cs_dep"] = sg(M("ce_dep", "apres") - M("ce_dep", "avant"), 2)
        A["cs_ca_saut"] = nb(abs(M("ce_ca", "apres") - M("ce_ca", "avant")), 2)
        A["cs_l_rec"], A["cs_l_dep"] = nb(M("ce_rec", "apres") - M("ce_rec", "long")), nb(M("ce_dep", "apres") - M("ce_dep", "long"))   # sans signe : « augmentent de » (gardes : positifs)
        A["cs_int_long"] = nb(M("int_recus", "long"), 2)
        A["cs_int_apres"] = nb(M("int_recus", "apres"), 2)
        for a in range(FEN_CS["avant"][0], fin_ + 1):
            A["cs_%d_ce" % a], A["cs_%d_fmi" % a] = nb(cs[a]["ce_st"]), nb(cs[a]["fmi_ca"])
            A["cs_%d_ocde" % a], A["cs_%d_obs" % a] = nb(cs[a]["ocde"]), nb(cs[a]["obs"])
        A["cs_tab_fin"] = str(fin_)
        return A

    fen = {k: (d0, d1 or last["annee"]) for k, (d0, d1) in FENETRES_DEFICIT.items()}
    if any(a not in dr for d0, d1 in fen.values() for a in (d0, d1)):
        fail("depenses et recettes publiees absentes pour une fenetre %s" % fen)

    bascule = next((r["annee"] for r in rows
                    if all(x["effet_taux_croissance"] < 0 or x["croissance_nominale_pct"] < 0 for x in rows if x["annee"] >= r["annee"])), None)
    if bascule is None or bascule == rows[-1]["annee"]:
        fail("« Ce qu'il faut retenir » : plus de periode finale ou l'effet taux-croissance est negatif chaque annee (bascule %s)" % bascule)

    A, A_en = bloc(*NB["fr"]), bloc(*NB["en"])
    for X_, lang in ((A, "fr"), (A_en, "en")):
        X_["millesime_dette"], X_["millesime_comptes"] = millesime("gov_10dd_edpt1", lang), millesime("gov_10a_main", lang)
        for k, v in EDITIONS_CS[lang].items():
            X_["cs_ed_" + k] = v
        # « point » accordé à la valeur affichée (même règle que ACCORD_POINTS)
        for k in ("cs_ce_saut", "cs_fmi_saut", "cs_ocde_saut", "cs_rec", "cs_ca_saut", "cs_ce_conj", "cs_fmi_conj"):
            v = abs(float(X_[k].replace(",", "." if lang == "fr" else "")))
            X_[k + "_pt"] = X_[k] + ("\u00a0" if lang == "fr" else " ") + (("point" if v < 2 else "points") if lang == "fr" else ("point" if v == 1 else "points"))
        # Relecture de langue du 11/10/2026. (1) Après un verbe qui porte déjà le sens (« a ajouté », « a retiré »), la
        # valeur s'écrit sans signe : « retiré −15,7 » se lisait comme un ajout. Les sens sont couverts par les gardes
        # « compensation dans le temps » (plus de 10 points avant la bascule, moins de −10 après) et OPTIMUM-10 (les
        # recettes « remontent » de plus d'un demi-point la dernière année).
        for k in VALEURS_SANS_SIGNE:
            X_[k + "_abs"] = X_[k].lstrip("+−")
        # (2) Accord de « point » : singulier sous 2 en français (« 1,2 point »), pluriel hors 1 en anglais. Calculé
        # sur la valeur AFFICHÉE (arrondie), puisque c'est elle que le lecteur accorde.
        for k in ACCORD_POINTS:
            v = abs(float(X_[k].lstrip("+−").replace(",", "." if lang == "fr" else "")))
            X_[k + "_pt"] = ("point" if v < 2 else "points") if lang == "fr" else ("point" if v == 1 else "points")
    p1, p2, p3 = per
    affirmations = [
        ("titre de la figure : « la dette a doublé » (rapport 1,85 à 2,2)", 1.85 < last["dette_pct_pib"] / d_depart < 2.2),
        ("page inflation : « le ratio a reculé en 2021-2023, beaucoup moins que l'effet taux-croissance »",
         sum(r["variation"] for r in infl) < 0 and -sum(r["effet_taux_croissance"] for r in infl) > -2 * sum(r["variation"] for r in infl)),
        ("chaque période : « le ratio gagne » (variation positive)", all(t["variation"] > 0 for t in per)),
        ("période 1 : l'effet taux-croissance « ajoute » (positif)", p1["effet_taux_croissance"] > 0),
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
        ("« Ce qu'il faut retenir » : compensation dans le temps — plus de 10 points avant la bascule, moins de -10 après",
         sum(r["effet_taux_croissance"] for r in rows if r["annee"] < bascule) > 10
         and sum(r["effet_taux_croissance"] for r in rows if r["annee"] >= bascule) < -10),
        ("« Ce qu'il faut retenir » : la bascule tombe entre 2014 et 2019 (le bloc de confrontation la rapproche de la note du Trésor, qui la date de 2016)",
         2014 <= bascule <= 2019),
        ("« Ce qu'il faut retenir » : avant la bascule, le taux implicite dépasse « le plus souvent » la croissance nominale",
         sum(1 for r in rows if r["annee"] < bascule and lg.depasse(r["taux_implicite_pct"], r["croissance_nominale_pct"], 2)) * 2
         > sum(1 for r in rows if r["annee"] < bascule)),
        ("« Ce qu'il faut retenir » : depuis la bascule, la seule année d'effet taux-croissance positif est 2020",
         [r["annee"] for r in rows if r["annee"] >= bascule and r["effet_taux_croissance"] >= 0] == [2020]),
        ("« Ce qu'il faut retenir » : le taux implicite « remonte » (creux en 2019 ou après, dernière année au moins 0,5 point au-dessus)",
         lg.extremum(rows, lambda r: r["taux_implicite_pct"], 2, maxi=False)["annee"] >= 2019
         and last["taux_implicite_pct"] > min(r["taux_implicite_pct"] for r in rows) + 0.5),
        # --- troisième tour (Trésor-Éco n° 403, 03/10/2026) : chaque constat du bloc de confrontation, recalculé
        ("2001-2007 : le ratio monte de plus de 4 points (le bloc l'oppose à la « relative stabilité » du Trésor)",
         by[2007]["dette_pct_pib"] - by[2001]["dette_pct_pib"] > 4),
        ("fenêtre OFCE : le solde se dégrade, la baisse des recettes dépasse la variation des dépenses hors intérêts",
         dr[fen["ofce"][1]]["solde"] < dr[fen["ofce"][0]]["solde"]
         and dr[fen["ofce"][1]]["recettes"] - dr[fen["ofce"][0]]["recettes"] < 0
         and abs(dr[fen["ofce"][1]]["recettes"] - dr[fen["ofce"][0]]["recettes"])
         > abs(dr[fen["ofce"][1]]["depenses_hors_interets"] - dr[fen["ofce"][0]]["depenses_hors_interets"])),
        ("fenêtre DG Trésor : le solde se dégrade, la hausse des dépenses hors intérêts dépasse la variation des recettes",
         dr[fen["tresor"][1]]["solde"] < dr[fen["tresor"][0]]["solde"]
         and dr[fen["tresor"][1]]["depenses_hors_interets"] - dr[fen["tresor"][0]]["depenses_hors_interets"] > 0
         and dr[fen["tresor"][1]]["depenses_hors_interets"] - dr[fen["tresor"][0]]["depenses_hors_interets"]
         > abs(dr[fen["tresor"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"])),
        ("entre les deux années de départ, les dépenses hors intérêts baissent de plus d'un point",
         dr[fen["tresor"][0]]["depenses_hors_interets"] - dr[fen["ofce"][0]]["depenses_hors_interets"] < -1),
        ("fenêtre commune : dépenses en hausse et recettes en baisse de plus d'un point chacune, d'ampleur voisine "
         "(le bloc dit que les chiffres de l'OFCE, +1,8 et −1,6, s'y retrouvent ; écart à 0,5 près)",
         dr[fen["ofce"][1]]["depenses"] - dr[fen["tresor"][0]]["depenses"] > 1
         and dr[fen["ofce"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"] < -1
         and abs((dr[fen["ofce"][1]]["depenses"] - dr[fen["tresor"][0]]["depenses"]) - 1.8) < 0.5
         and abs((dr[fen["ofce"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"]) + 1.6) < 0.5),
        ("l'année d'arrivée compte aussi : depuis le départ du Trésor, les recettes baissent davantage jusqu'à la fin OFCE (écart > 0,5)",
         (dr[fen["ofce"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"])
         < (dr[fen["tresor"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"]) - 0.5),
        ("« Ce qu'il faut retenir » : excédents primaires rares (six années au plus sur la série)",
         sum(1 for r in rows if r["solde_primaire_pct_pib"] > 0) <= 6),
        # --- phase B (contre-expertise du 11/10/2026)
        ("D15 : sur la fenêtre commune 2019-2024, le recul des recettes dépasse la hausse des dépenses hors intérêts "
         "(le diagnostic de 2019-2025 se retourne avec l'année d'arrivée)",
         dr[fen["ofce"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"] < 0
         and abs(dr[fen["ofce"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"])
         > dr[fen["ofce"][1]]["depenses_hors_interets"] - dr[fen["tresor"][0]]["depenses_hors_interets"] > 0),
        ("D1 : le taux implicite remonte par un saut en 2022 (plus de 0,3 point en un an, le plus fort depuis le creux), puis plus lentement",
         by[2022]["taux_implicite_pct"] - by[2021]["taux_implicite_pct"] > 0.3
         and all(by[a]["taux_implicite_pct"] - by[a - 1]["taux_implicite_pct"] < by[2022]["taux_implicite_pct"] - by[2021]["taux_implicite_pct"]
                 for a in by if a > 2022)
         # OPTIMUM-12 : la prose dit « point bas en 2020, légère hausse en 2021, saut en 2022 ».
         and lg.extremum(rows, lambda r: r["taux_implicite_pct"], 2, maxi=False)["annee"] == 2020
         and 0 < by[2021]["taux_implicite_pct"] - by[2020]["taux_implicite_pct"] < 0.3),
        ("OPTIMUM-10 : entre les deux fenêtres de même départ, les dépenses hors intérêts varient d'autant (à 0,1 près) et les "
         "recettes remontent de plus d'un demi-point la dernière année : c'est elles qui retournent la conclusion",
         abs((dr[fen["tresor"][1]]["depenses_hors_interets"] - dr[fen["ofce"][1]]["depenses_hors_interets"])) < 0.1
         and dr[fen["tresor"][1]]["recettes"] - dr[fen["ofce"][1]]["recettes"] > 0.5),
        ("OPTIMUM-15 : le retournement 2019-2025 tient a un ecart mince (moins d'un demi-point) entre hausse des depenses "
         "hors interets et recul des recettes",
         0 < (dr[fen["tresor"][1]]["depenses_hors_interets"] - dr[fen["tresor"][0]]["depenses_hors_interets"])
         + (dr[fen["tresor"][1]]["recettes"] - dr[fen["tresor"][0]]["recettes"]) < 0.5),
        ("OPTIMUM-15 : l'INSEE publie pour la derniere fin d'annee une valeur voisine mais differente de celle d'Eurostat",
         insee_fin is not None and 0 < abs(insee_fin - last["dette_pct_pib"]) <= 0.5),
        ("OPTIMUM-10 : « un déficit qui se réduit n'a pas disparu » — le solde primaire de la dernière année reste négatif",
         last["solde_primaire_pct_pib"] < 0),
        # --- Conjoncture ou structure (19/10/2026). Seuils écrits avant les phrases.
        ("« plus creusé dans les trois estimations » : chaque producteur, solde d'après 2022 inférieur de plus d'un point à 2015-2019",
         all(moy_cs(cs, c, FEN_CS["apres"], last["annee"]) < moy_cs(cs, c, FEN_CS["avant"], last["annee"]) - 1 for c in ("ce_st", "fmi_ca", "ocde"))),
        ("« la conjoncture ne l'explique pas » : part conjoncturelle (et ponctuelle) d'après 2022 sous 0,5 point chez la Commission et le FMI",
         abs(moy_cs(cs, "obs", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_st", FEN_CS["apres"], last["annee"])) < 0.5
         and abs(moy_cs(cs, "fmi_obs", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "fmi_ca", FEN_CS["apres"], last["annee"])) < 0.5),
        ("« par les recettes » : recettes corrigées en baisse de plus d'un point, plus de quatre fois la variation des dépenses corrigées, elle-même sous 0,5 point",
         moy_cs(cs, "ce_rec", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_rec", FEN_CS["avant"], last["annee"]) < -1
         and abs(moy_cs(cs, "ce_rec", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_rec", FEN_CS["avant"], last["annee"]))
         > 4 * abs(moy_cs(cs, "ce_dep", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_dep", FEN_CS["avant"], last["annee"]))
         and abs(moy_cs(cs, "ce_dep", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_dep", FEN_CS["avant"], last["annee"])) < 0.5),
        ("« sur la longue période, l'inverse » : depuis 1996-2007, dépenses corrigées en hausse de plus de deux points et plus de deux fois les recettes",
         moy_cs(cs, "ce_dep", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_dep", FEN_CS["long"], last["annee"]) > 2
         and moy_cs(cs, "ce_dep", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_dep", FEN_CS["long"], last["annee"])
         > 2 * (moy_cs(cs, "ce_rec", FEN_CS["apres"], last["annee"]) - moy_cs(cs, "ce_rec", FEN_CS["long"], last["annee"])) > 0),
        ("FMI : « proche de l'équilibre » en 1996-2007 (moins d'un demi-point), « tombe » en 2010-2014 (sous -1,5), « revient » "
         "en 2015-2019 (au-dessus de 2010-2014 d'un point) et « s'établit » plus bas d'après 2022 (sous 2015-2019)",
         abs(moy_cs(cs, "fmi_ca", FEN_CS["long"], last["annee"])) < 0.5 and moy_cs(cs, "fmi_ca", FEN_CS["crise"], last["annee"]) < -1.5
         and moy_cs(cs, "fmi_ca", FEN_CS["avant"], last["annee"]) > moy_cs(cs, "fmi_ca", FEN_CS["crise"], last["annee"]) + 1
         and moy_cs(cs, "fmi_ca", FEN_CS["apres"], last["annee"]) < moy_cs(cs, "fmi_ca", FEN_CS["avant"], last["annee"])),
        ("2009 et 2020 : les deux plus fortes hausses de la série",
         sorted(rows, key=lambda r: -r["variation"])[0]["annee"] in (2009, 2020) and sorted(rows, key=lambda r: -r["variation"])[1]["annee"] in (2009, 2020)),
    ]
    faux = [nom for nom, ok in affirmations if not ok]
    if faux:
        fail("la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    return A, A_en


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
    dr = depenses_recettes()
    cs = conjoncture(rows)
    aff, aff_en = affichage(a0, d_depart, rows, total, per, dr, cs)
    log("Decomposition %d-%d : hausse %.1f = interets %.1f + croissance %.1f + deficits primaires %.1f + flux-stock %.1f"
        % (rows[0]["annee"], rows[-1]["annee"], total["variation"], total["effet_interets"], total["effet_croissance"],
           total["contribution_solde_primaire"], total["flux_stock"]))
    figs = {}
    for lang in ("fr", "en"):
        suf = SUFFIXE[lang]
        figs["dette-dynamique-cascade%s.svg" % suf] = fig_cascade(a0, d_depart, rows, total, lang)
        figs["dette-dynamique-annuelle%s.svg" % suf] = fig_annuelle(rows, lang)
        figs["dette-dynamique-cascade%s-m.svg" % suf] = fig_cascade_m(a0, d_depart, rows, total, lang, figs["dette-dynamique-cascade%s.svg" % suf])
        figs["dette-dynamique-annuelle%s-m.svg" % suf] = fig_annuelle_m(rows, lang, figs["dette-dynamique-annuelle%s.svg" % suf])
        figs["dette-dynamique-conjoncture%s.svg" % suf] = fig_cs(cs, lang)
        figs["dette-dynamique-conjoncture%s-m.svg" % suf] = fig_cs_m(cs, lang, figs["dette-dynamique-conjoncture%s.svg" % suf])
        for fid in ("cascade", "annuelle", "conjoncture"):
            ec = pied_figure.parite(figs["dette-dynamique-%s%s.svg" % (fid, suf)], figs["dette-dynamique-%s%s-m.svg" % (fid, suf)], FS_MIN)
            if ec:
                fail("parite mobile %s %s : %s" % (fid, lang, " ; ".join(ec)))
    for page, suf in (("_index.md", ""), ("_index.en.md", "-en")):
        ecarts = pied_figure.controler_page((ROOT / "content" / "pourquoi-la-dette-publique-augmente" / page).read_text(encoding="utf-8"),
                                            {f: v for f, v in figs.items() if re.fullmatch(r"dette-dynamique-[a-z]+%s(-m)?\.svg" % suf, f)})
        if ecarts:
            fail("page %s : %s" % (page, " ; ".join(ecarts)))
    if check:
        log("--check : gardes passees (%d cles d'affichage), parite des 6 figures telephone et hauteurs des pages controlees, rien ecrit." % len(aff))
        return 0
    payload = {"meta": {"releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "page": "https://" + PAGE_URL,
                        "licence": "CC BY 4.0", "pays": "France", "perimetre": "administrations publiques (S.13), SEC 2010",
                        "identite": "d_t - d_{t-1} = i/(1+g) d_{t-1} - g/(1+g) d_{t-1} - pb_t + sfa_t",
                        "definitions": {"effet_interets": "intérêts de l'année rapportés au PIB, via le taux implicite appliqué à la dette de départ",
                                        "effet_croissance": "érosion du ratio par la hausse du PIB nominal (croissance réelle et inflation)",
                                        "contribution_solde_primaire": "déficit hors intérêts, en points de PIB (négatif en cas d'excédent)",
                                        "flux_stock": "variation de dette qui ne passe pas par le déficit (trésorerie, actifs, valorisation) ; résidu de l'identité ; les ratios de dette et de solde sont contrôlés contre ceux que publie Eurostat"}},
               "depart": {"annee": a0, "dette_pct_pib": d_depart}, "annees": rows, "total": total,
               "periodes": [dict(periode=(lib if b else lib % rows[-1]["annee"]), **t) for (a, b, lib), t in zip(PERIODES, per)],
               "depenses_recettes_pc_pib": {str(k): v for k, v in dr.items() if k >= a0},
               "conjoncture_structure": {"definitions": {
                   "obs": "solde primaire observé, Eurostat, % du PIB (intérêts versés déduits)",
                   "ce_st": "solde primaire structurel, Commission (AMECO UBLGBPS), % du PIB potentiel, depuis 2010",
                   "ce_ca": "solde primaire corrigé du cycle, Commission (AMECO UBLGBP) = ce_rec - ce_dep",
                   "ce_rec": "recettes corrigées du cycle, Commission (AMECO URTGAP)", "ce_dep": "dépenses hors intérêts corrigées du cycle, Commission (AMECO UUTGBP)",
                   "fmi_ca": "solde primaire corrigé du cycle, FMI (GGCBP_G01_PGDP_PT), intérêts nets déduits",
                   "fmi_obs": "solde primaire observé, FMI (GGXONLB_G01_GDP_PT), intérêts nets déduits",
                   "ocde": "solde primaire sous-jacent, OCDE (NLGXQU), depuis 2010", "int_recus": "intérêts reçus, Eurostat D41REC, % du PIB"},
                   "pieces": {k: dict(fichier=v, sha256=hashlib.sha256((SOURCES_DETTE / v).read_bytes()).hexdigest()) for k, v in PIECES_CS.items()},
                   "annees": {str(k): v for k, v in cs.items()}},
               "affichage": aff, "affichage_en": aff_en}
    releve = payload["meta"]["releve_le"]
    # « Rien écrit à données identiques » : l'empreinte compare le paquet ENTIER, donc affichage_en compris (aucun
    # releve_le n'est logé dans les blocs d'affichage ici, contrairement à BLOCS_RELEVE de update_dette_insee.py) ;
    # figs et fiches couvrent les figures et fiches anglaises. Un paquet ancien sans affichage_en diffère : il est réécrit.
    # Bruit de calcul au 15e chiffre : le jeu se compare et s'écrit normalisé (organe commun releve_jeu.normalise, 19/10/2026).
    payload = rj.normalise(payload)
    licence = "CC BY 4.0 — compilation Stéphane Lalut ; source Eurostat"   # nomme les sources : un changement s'écrit (rj.sans_licence, 18/10/2026)
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev); p2.pop("releve_le", None); rj.sans_licence(p2, licence); p2["meta"] = dict(p2["meta"], releve_le=None)
            n2 = dict(payload); n2["meta"] = dict(n2["meta"], releve_le=None)
            if prev.get("releve_le") and json.dumps(p2, sort_keys=True, ensure_ascii=False) == json.dumps(n2, sort_keys=True, ensure_ascii=False) \
                    and all((OUT_IMG / f).exists() and (OUT_IMG / f).read_text(encoding="utf-8") == s for f, s in figs.items()) \
                    and all((OUT_IMG / f.replace(".svg", ".png")).exists() for f in figs) \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte(rows, cs) \
                    and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches(figs, aff):
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
        except (ValueError, KeyError):
            pass
    releve = rj.releve(OUT_DATA, payload, releve)   # le texte seul ne date pas les données
    payload["meta"]["releve_le"] = releve
    payload = {"releve_le": releve, "_licence": licence, **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte(rows, cs), encoding="utf-8-sig", newline="\n")  # BOM : Excel lit les accents
    import cairosvg
    for f, s in figs.items():
        (OUT_IMG / f).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / f), write_to=str(OUT_IMG / f.replace(".svg", ".png")), output_width=1440, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches(figs, aff), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("Ecrit : data/ et static/dette_dynamique.json, static/dette_dynamique.csv, data/figures_dynamique.json, %d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
