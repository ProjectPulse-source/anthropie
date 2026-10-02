#!/usr/bin/env python3
"""generer_acces_superieur.py -- activité de SES « Après le bac, les mêmes voies pour tous ? » (/enseignants/ecole-et-parcours/).

Jeu : filière d'inscription des nouveaux bacheliers dans l'enseignement supérieur, selon l'origine sociale.
Source : MESRE-SIES, « L'état de l'Enseignement supérieur, de la Recherche et de l'Innovation en France », fiche 13,
tableau 13.03 ; témoin de composition : fiche 09, tableaux 09.03 et 09.04. Les fiches sont ARCHIVÉES dans
scripts/sources_enseignants/ (pages officielles, empreintes dans SHA256SUMS) : aucun appel réseau ici.

MILLÉSIME (arbitrage ENTRANTE_2026-10-02_Ecole_Parcours_Graphe_supplementaire, tour 2) : la figure porte sur les
bacheliers de l'année ANNEE, la même que la cohorte de l'activité « licence » de la page ; l'édition suivante sert de
témoin de stabilité. Les deux activités ne suivent pas les mêmes élèves, et la page le dit.

METTRE À JOUR : `python scripts/maj_sources.py integrer` archive les fiches 13 et 09 des éditions nécessaires et les
inscrit au registre data/sources_maj.json ; l'année de la figure suit d'elle-même la dernière cohorte de l'activité
« licence ». Les gardes disent si les constats tiennent.

TÉMOINS, bloquants : six catégories d'origine exactement, libellés de la source ; quatre destinations qui somment à
100 à l'arrondi près sur chaque ligne ; « dont IUT » inférieur à « université » ; mêmes contrôles sur le millésime témoin.
Chaque qualificatif de la fiche et du corrigé est une garde. SVG et PNG ensemble ou pas du tout.

Mêmes fonctions de service, mêmes couleurs que generer_parcours_licence.py, importé tel quel : les deux figures de la
page forment une famille.

Usage : python scripts/generer_acces_superieur.py [--check]
Sorties : data/ et static/acces_superieur.json (bloc affichage), static/acces_superieur.csv,
          static/img/acces-superieur-origine.svg + .png
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generer_parcours_licence as gl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_enseignants"
OUT_DATA = ROOT / "data" / "acces_superieur.json"
OUT_STATIC = ROOT / "static" / "acces_superieur.json"
OUT_CSV = ROOT / "static" / "acces_superieur.csv"
OUT_IMG = ROOT / "static" / "img"
FIGURE = "acces-superieur-origine"
PAGE_URL = "stephane-lalut.com/enseignants/ecole-et-parcours/"

# Tout vient du registre data/sources_maj.json. RÈGLE : l'année de la figure est celle de la dernière cohorte de
# l'activité « licence » ; l'autre année archivée la plus proche sert de témoin (la suivante si elle existe).
_SRC = gl.source("eesr-acces")
FICHES = {int(k): tuple(v) for k, v in _SRC["fiches_acces"].items()}
ANNEE = max(gl.COHORTES)
if ANNEE not in FICHES or str(ANNEE) not in _SRC["fiches_bac"]:
    print("ECHEC : aucune fiche archivee pour les bacheliers %d (fiches 13 et 09) -- lancer scripts/maj_sources.py integrer" % ANNEE)
    sys.exit(1)
_AUTRES = sorted((a for a in FICHES if a != ANNEE), key=lambda a: (abs(a - ANNEE), -a))
if not _AUTRES:
    print("ECHEC : aucun millesime temoin archive pour la fiche 13")
    sys.exit(1)
TEMOIN = _AUTRES[0]
FICHE_BAC = _SRC["fiches_bac"][str(ANNEE)]
ORIGINES = [("ind", "Agriculteurs, artisans, commerçants, chefs d'entreprise", ("Agriculteurs, artisans,", "commerçants, chefs d'entreprise")),
            ("cad", "Cadres, professions intellectuelles supérieures", ("Cadres, professions", "intellectuelles supérieures")),
            ("pi", "Professions intermédiaires", ("Professions intermédiaires",)),
            ("emp", "Employés", ("Employés",)),
            ("ouv", "Ouvriers", ("Ouvriers",)),
            ("ret", "Retraités, inactifs", ("Retraités, inactifs",))]
DEST = [("univ", "Université"), ("cpge", "CPGE"), ("sts", "STS"), ("autres", "Autres")]
COULEUR = {"univ": (gl.BLEU, "#ffffff"), "cpge": (gl.ORANGE, gl.INK), "sts": (gl.GRIS_CLAIR, gl.INK), "autres": (gl.GRIS, "#ffffff")}
LIBELLE = {"univ": ("Université", "(dont IUT)"), "cpge": ("Classes", "prépa."), "sts": ("Sections de", "technicien sup."),
           "autres": ("Autres", "formations")}
fail, log, fr, esc = gl.fail, gl.log, gl.fr, gl.esc


def nombre(s: str) -> float:
    return float(s.replace(" ", "").replace(" ", "").replace(",", "."))


def tables(fichier: str, sums: dict[str, str]) -> list[list[list[str]]]:
    p = SRC / fichier
    if not p.is_file():
        fail("fiche absente : %s" % fichier)
    if sums.get(fichier) != hashlib.sha256(p.read_bytes()).hexdigest():
        fail("%s : empreinte differente de SHA256SUMS (piece remplacee ?)" % fichier)
    t = p.read_text(encoding="utf-8", errors="replace")
    out = []
    for tb in re.findall(r"<table.*?</table>", t, flags=re.S):
        rows = []
        for r in re.findall(r"<tr.*?</tr>", tb, flags=re.S):
            rows.append([re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", c))).strip()
                         for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, flags=re.S)])
        out.append(rows)
    return out, t


def lire_acces(annee: int, sums: dict[str, str]) -> dict:
    fichier, edition = FICHES[annee]
    tabs, brut = tables(fichier, sums)
    if "Nouveaux bacheliers %d inscrits dans les différentes filières" % annee not in re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", brut))):
        fail("%s : le tableau 13.03 des bacheliers %d n'est pas dans cette fiche" % (fichier, annee))
    cible = [tb for tb in tabs if any(r and r[0] == "Ouvriers" for r in tb) and any("CPGE" in r for r in tb)]
    if len(cible) != 1:
        fail("%s : %d tableau(x) candidat(s) pour 13.03, attendu 1" % (fichier, len(cible)))
    tb = cible[0]
    if tb[0] != ["", "Université", "dont IUT", "CPGE", "STS", "Autres", "Ensemble"]:
        fail("%s : en-tetes du tableau 13.03 changes : %s" % (fichier, tb[0]))
    lignes = {r[0]: r for r in tb[1:]}
    rens = [k for k in lignes if k.startswith("Origine sociale renseignée")]
    if len(rens) != 1:
        fail("%s : ligne « Origine sociale renseignée » introuvable" % fichier)
    m = re.search(r"\(([\d,]+)\s*%\)", rens[0])
    if not m:
        fail("%s : part d'origine renseignee illisible" % fichier)
    presentes = [k for k in lignes if k not in ("Hommes", "Femmes") and not k.startswith("Origine sociale renseignée")]
    if sorted(presentes) != sorted(lib for _, lib, _ in ORIGINES):
        fail("%s : categories d'origine inattendues : %s" % (fichier, " | ".join(presentes)))

    def ligne(r, nom):
        d = dict(univ=nombre(r[1]), iut=nombre(r[2]), cpge=nombre(r[3]), sts=nombre(r[4]), autres=nombre(r[5]))
        if nombre(r[6]) != 100.0 or abs(d["univ"] + d["cpge"] + d["sts"] + d["autres"] - 100) > 0.21:
            fail("%d, %s : les quatre destinations ne somment pas a 100 (%.1f)" % (annee, nom, d["univ"] + d["cpge"] + d["sts"] + d["autres"]))
        if d["iut"] > d["univ"]:
            fail("%d, %s : « dont IUT » superieur a « universite »" % (annee, nom))
        return d

    return {"annee": annee, "edition": edition, "fichier": fichier, "origine_renseignee_pct": nombre(m.group(1)),
            "origines": {cle: ligne(lignes[lib], lib) for cle, lib, _ in ORIGINES}, "ensemble_renseigne": ligne(lignes[rens[0]], "ensemble")}


def lire_bac(sums: dict[str, str]) -> dict:
    """Témoin de composition : série du baccalauréat par filière (09.03) et origine sociale par série (09.04), 2023."""
    tabs, _ = tables(FICHE_BAC, sums)
    t3 = [tb for tb in tabs if tb and tb[0][:5] == ["", "Université", "dont IUT", "CPGE", "STS"]]
    t4 = [tb for tb in tabs if tb and tb[0] == ["", "Bacheliers", "Poursuivants"]]
    if len(t3) != 1 or len(t4) != 1:
        fail("%s : tableaux 09.03 ou 09.04 introuvables (%d, %d)" % (FICHE_BAC, len(t3), len(t4)))
    t3, t4 = t3[0], t4[0]
    if [c.split()[0] for c in t3[1]] != ["2013", str(ANNEE)] * 7:
        fail("%s : annees du tableau 09.03 inattendues : %s" % (FICHE_BAC, t3[1]))
    if t4[1] != ["général", "technologique", "professionnel", "Ensemble"] * 2:
        fail("%s : en-tetes du tableau 09.04 inattendus : %s" % (FICHE_BAC, t4[1]))
    l3 = {r[0]: r for r in t3[2:]}
    l4 = {r[0]: r for r in t4[2:]}
    # 09.03 : colonnes par paires (2013, année) : université 1-2, IUT 3-4, CPGE 5-6, STS 7-8
    out = {"cpge_bac_general": nombre(l3["Bac général"][6]), "sts_bac_general": nombre(l3["Bac général"][8]),
           "sts_bac_technologique": nombre(l3["Bac technologique"][8]), "sts_bac_professionnel": nombre(l3["Bac professionnel"][8]),
           # 09.04, bloc « Bacheliers » : colonnes 1 général, 2 technologique, 3 professionnel
           "bac_general_cadres": nombre(l4["Cadres, professions intellectuelles supérieures"][1]),
           "bac_general_ouvriers": nombre(l4["Ouvriers"][1]),
           "bac_professionnel_cadres": nombre(l4["Cadres, professions intellectuelles supérieures"][3]),
           "bac_professionnel_ouvriers": nombre(l4["Ouvriers"][3])}
    s = out["sts_bac_general"] + out["sts_bac_technologique"] + out["sts_bac_professionnel"]
    if abs(s - 100) > 0.21:
        fail("09.03 : les trois series ne somment pas a 100 en STS (%.1f)" % s)
    return out


def affichage(a: dict, t: dict, bac: dict) -> tuple[dict, list[str]]:
    o = a["origines"]
    A = {"annee": str(a["annee"]), "annee_temoin": str(t["annee"]), "edition": a["edition"], "edition_temoin": t["edition"],
         "origine_renseignee": fr(a["origine_renseignee_pct"]), "origine_non_renseignee": fr(100 - a["origine_renseignee_pct"])}
    for cle, d in list(o.items()) + [("ens", a["ensemble_renseigne"])]:
        for k in ("univ", "iut", "cpge", "sts", "autres"):
            A["%s_%s" % (cle, k)] = fr(d[k])
    ecart, rapport = {}, {}
    for k, _ in DEST:
        v = [d[k] for d in o.values()]
        ecart[k], rapport[k] = max(v) - min(v), max(v) / min(v)
        A["ecart_" + k], A["rapport_" + k] = fr(ecart[k]), fr(rapport[k])
    A["sts_ouv_sur_cad"] = fr(o["ouv"]["sts"] / o["cad"]["sts"])
    A["cpge_cad_sur_ouv"] = fr(o["cad"]["cpge"] / o["ouv"]["cpge"])
    for cle in ("cad", "ouv"):
        for k in ("cpge", "sts"):
            A["temoin_%s_%s" % (cle, k)] = fr(t["origines"][cle][k])
    # Les deux millésimes dans l'ordre du temps : la page écrit « x % en N, y % en N+1 », quel que soit celui de la figure.
    c1, c2 = sorted((a, t), key=lambda x: x["annee"])
    A["chrono1_annee"], A["chrono2_annee"] = str(c1["annee"]), str(c2["annee"])
    for n, c in (("chrono1", c1), ("chrono2", c2)):
        A[n + "_ouv_sts"], A[n + "_cad_cpge"] = fr(c["origines"]["ouv"]["sts"]), fr(c["origines"]["cad"]["cpge"])
    A["telecharge_le"] = gl.date_fr(_SRC["telecharge_le"])
    for k, v in bac.items():
        A[k] = fr(v)
    derive = max(abs(o[c][k] - t["origines"][c][k]) for c in o for k, _ in DEST)
    A["derive_max"] = fr(derive)
    gardes = [
        ("« six catégories » d'origine", len(o) == 6),
        ("les enfants d'ouvriers sont la catégorie la plus souvent inscrite en STS, les enfants de cadres la moins souvent",
         o["ouv"]["sts"] == max(d["sts"] for d in o.values()) and o["cad"]["sts"] == min(d["sts"] for d in o.values())),
        ("les enfants de cadres sont la catégorie la plus souvent inscrite en CPGE", o["cad"]["cpge"] == max(d["cpge"] for d in o.values())),
        ("STS : « plus de quatre fois » plus fréquent pour les enfants d'ouvriers que de cadres", o["ouv"]["sts"] / o["cad"]["sts"] > 4),
        ("CPGE : « plus de trois fois » plus fréquent pour les enfants de cadres que d'ouvriers", o["cad"]["cpge"] / o["ouv"]["cpge"] > 3),
        ("en points, les CPGE montrent le plus petit écart ; en rapport, l'université (les deux mesures ne classent pas pareil)",
         ecart["cpge"] == min(ecart.values()) and rapport["univ"] == min(rapport.values()) and rapport["cpge"] > 2.5),
        ("en points, les STS montrent le plus grand écart", ecart["sts"] == max(ecart.values())),
        ("l'université est la première destination de cinq catégories sur six ; pour les enfants d'ouvriers, ce sont les STS",
         sum(1 for d in o.values() if d["univ"] == max(d[k] for k, _ in DEST)) == 5 and o["ouv"]["sts"] > o["ouv"]["univ"]),
        ("enfants de retraités et d'inactifs : université et STS « proches » (moins de cinq points)", abs(o["ret"]["univ"] - o["ret"]["sts"]) < 5),
        ("« d'une année à l'autre, aucune valeur ne bouge de plus d'un point et demi »", derive < 1.5),
        ("les CPGE recrutent « plus de neuf fois sur dix » des bacheliers généraux ; en STS, les bacheliers professionnels sont plus nombreux que les généraux",
         bac["cpge_bac_general"] > 90 and bac["sts_bac_professionnel"] > bac["sts_bac_general"]),
        ("parmi les bacheliers généraux, les enfants de cadres sont plus de trois fois plus nombreux que les enfants d'ouvriers ; "
         "parmi les bacheliers professionnels, les enfants d'ouvriers plus de deux fois plus nombreux que ceux de cadres",
         bac["bac_general_cadres"] > 3 * bac["bac_general_ouvriers"] and bac["bac_professionnel_ouvriers"] > 2 * bac["bac_professionnel_cadres"]),
    ]
    return A, [nom for nom, ok in gardes if not ok]


def figure(a: dict, A: dict) -> str:
    """Sept barres empilées à 100 % : six origines (ordre de la source), puis l'ensemble des origines renseignées."""
    lignes = [(lib2, a["origines"][cle]) for cle, _, lib2 in ORIGINES] + [(("Ensemble", "(origine renseignée)"), a["ensemble_renseigne"])]
    W = gl.W
    X0, X1, TOP, HB, PAS = 196, W - 8, 96, 28, 40
    NB_CART = 6
    H = TOP + PAS * (len(lignes) - 1) + HB + 14 + 12 * (NB_CART - 3)
    titre = "Après le bac : où s'inscrivent les nouveaux bacheliers, selon l'origine sociale"
    o = a["origines"]
    desc = ("Barres empilées à 100 %%, une par catégorie socioprofessionnelle du parent. Nouveaux bacheliers %s inscrits dans "
            "l'enseignement supérieur : %s %% des enfants de cadres sont à l'université, %s %% en classes préparatoires, %s %% "
            "en sections de technicien supérieur, %s %% dans d'autres formations ; pour les enfants d'ouvriers, %s %%, %s %%, "
            "%s %% et %s %%. Toutes les valeurs sont dans le tableau qui suit la figure."
            % (A["annee"], A["cad_univ"], A["cad_cpge"], A["cad_sts"], A["cad_autres"], A["ouv_univ"], A["ouv_cpge"], A["ouv_sts"], A["ouv_autres"]))
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="as-t as-d" font-family="%s">' % (W, H + 52, gl.FONT),
         '<title id="as-t">%s</title><desc id="as-d">%s</desc>' % (esc(titre), esc(desc)),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 52),
         '<text x="0" y="18" font-size="15" font-weight="600" fill="%s">%s</text>' % (gl.INK, esc(titre)),
         '<text x="0" y="38" font-size="11" fill="%s">%s</text>'
         % (gl.INK2, esc("Nouveaux bacheliers %s inscrits dans l'enseignement supérieur, par filière, en %% de chaque catégorie." % A["annee"]))]
    larg = X1 - X0
    for n, (lib, d) in enumerate(lignes):
        y = TOP + PAS * n
        total = sum(d[k] for k, _ in DEST)
        ens = lib[0] == "Ensemble"
        if ens:
            e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="0.6"/>' % (y - 6, W, y - 6, gl.GRID))
        y0l = y + HB / 2 + 4 - (6 if len(lib) == 2 else 0)
        for j, mot in enumerate(lib):
            e.append('<text x="%d" y="%.1f" font-size="10.5" fill="%s" text-anchor="end"%s>%s</text>'
                     % (X0 - 10, y0l + 12 * j, gl.INK, ' font-weight="600"' if ens and j == 0 else "", esc(mot)))
        x = float(X0)
        for k, _ in DEST:
            w = larg * d[k] / total
            fond, encre = COULEUR[k]
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" stroke="#ffffff" stroke-width="1.5"/>' % (x, y, w, HB, fond))
            e.append('<text x="%.1f" y="%.1f" font-size="%s" font-weight="600" fill="%s" text-anchor="middle">%s</text>'
                     % (x + w / 2, y + HB / 2 + 4, "12" if w >= 30 else "10", encre, esc(fr(d[k]))))
            if n == 0:
                for j, mot in enumerate(LIBELLE[k]):
                    e.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="%s" text-anchor="middle">%s</text>'
                             % (x + w / 2, y - 19 + 12 * j, gl.INK2, esc(mot)))
            x += w
    y0 = H + 4 - 12 * (NB_CART - 3)
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, gl.GRID))
    cart = [("MESRE-SIES, État de l'enseignement supérieur, de la recherche et de l'innovation en France %s, tableau 13.03 ; France "
             "métropolitaine et DROM" % a["edition"], gl.INK2),
            ("Champ : bacheliers %s inscrits dans le supérieur à la rentrée suivante ; ceux qui ne poursuivent pas n'y figurent pas. "
             "STS : apprentissage compris." % A["annee"], gl.INK2),
            ("Origine : catégorie socioprofessionnelle du parent, renseignée pour %s %% des inscrits ; les autres ne sont pas répartis "
             "par la source." % A["origine_renseignee"], gl.INK2),
            ("Une inscription observée n'est pas un choix : elle dépend aussi de la série du baccalauréat, des candidatures et des "
             "admissions, que ce tableau ne croise pas.", gl.INK2),
            ("Taux arrondis : leur somme peut différer de 100 %. Catégories dans l'ordre de la source, sans hiérarchie.", gl.INK2),
            ("Figure Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, gl.MUTED)]
    assert len(cart) == NB_CART
    for k, (txt, col) in enumerate(cart):
        e.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, col, esc(txt)))
    e.append("</svg>")
    return "\n".join(e)


def csv_texte(annees: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["bacheliers", "origine_sociale", "filiere", "part_pct"])
    for a in annees:
        for cle, lib, _ in ORIGINES:
            for k, nom in DEST + [("iut", "dont IUT")]:
                w.writerow([a["annee"], lib, nom, "%.1f" % a["origines"][cle][k]])
        for k, nom in DEST + [("iut", "dont IUT")]:
            w.writerow([a["annee"], "Ensemble (origine renseignée)", nom, "%.1f" % a["ensemble_renseigne"][k]])
    return buf.getvalue()


def main() -> int:
    check = "--check" in sys.argv[1:]
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    sums = gl.empreintes()
    a, t, bac = lire_acces(ANNEE, sums), lire_acces(TEMOIN, sums), lire_bac(sums)
    A, faux = affichage(a, t, bac)
    if faux:
        fail("la page affirme ce que les donnees ne soutiennent plus : " + " ; ".join(faux))
    log("Bacheliers %d : STS %s (ouvriers) / %s (cadres), CPGE %s / %s ; derive maximale vers %d : %s point"
        % (ANNEE, A["ouv_sts"], A["cad_sts"], A["ouv_cpge"], A["cad_cpge"], TEMOIN, A["derive_max"]))
    if check:
        log("--check : temoins et gardes passes (%d cles d'affichage), rien ecrit." % len(A))
        return 0
    svg = figure(a, A)
    payload = {"meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0 pour la compilation et la figure ; données MESRE-SIES",
                        "champ": "nouveaux bacheliers inscrits dans l'enseignement supérieur à la rentrée suivant le baccalauréat, France métropolitaine et DROM",
                        "source": "MESRE-DGESIP/DGRI-SIES, L'état de l'Enseignement supérieur, de la Recherche et de l'Innovation en France, fiche 13 (tableau 13.03) et fiche 09 (tableaux 09.03 et 09.04)",
                        "definitions": {
                            "universite": "université, IUT compris (« dont IUT » est un sous-ensemble, non une cinquième destination)",
                            "cpge": "classes préparatoires aux grandes écoles",
                            "sts": "sections de technicien supérieur, par voie scolaire et par apprentissage",
                            "autres": "autres formations (écoles de commerce et d'ingénieurs, formations paramédicales et sociales, autres établissements)",
                            "origine_sociale": "catégorie socioprofessionnelle du parent, six catégories de la source ; origine non renseignée : non répartie par la source",
                            "temoin_baccalaureat": "série du baccalauréat des nouveaux inscrits de chaque filière (09.03) et origine sociale des bacheliers de chaque série (09.04)"}},
               "bacheliers": [a, t], "temoin_baccalaureat": bac, "affichage": A}
    releve = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = dict(prev)
            ancien = p2.pop("releve_le", None)
            p2.pop("_licence", None)
            if ancien and json.dumps(p2, sort_keys=True, ensure_ascii=False) == json.dumps(payload, sort_keys=True, ensure_ascii=False) \
                    and (OUT_IMG / (FIGURE + ".svg")).exists() and (OUT_IMG / (FIGURE + ".svg")).read_text(encoding="utf-8") == svg \
                    and (OUT_IMG / (FIGURE + ".png")).exists() and OUT_STATIC.exists() \
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csv_texte([a, t]):
                log("Donnees et figure identiques : rien ecrit (releve_le conserve : %s)." % ancien)
                return 0
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; source MESRE-SIES", **payload}
    txt = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT_DATA.write_text(txt, encoding="utf-8")
    OUT_STATIC.write_text(txt, encoding="utf-8")
    OUT_CSV.write_text(csv_texte([a, t]), encoding="utf-8-sig", newline="\n")
    import cairosvg
    (OUT_IMG / (FIGURE + ".svg")).write_text(svg, encoding="utf-8", newline="\n")
    cairosvg.svg2png(url=str(OUT_IMG / (FIGURE + ".svg")), write_to=str(OUT_IMG / (FIGURE + ".png")), output_width=1440,
                     background_color="white")
    log("Ecrit : data/ et static/acces_superieur.json, static/acces_superieur.csv, static/img/%s.svg + .png" % FIGURE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
