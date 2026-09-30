#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""og_dossier_dette.py -- cartes de partage propres aux deux volets du dossier dette.

    python scripts/og_dossier_dette.py

POURQUOI. Les deux pages du dossier servaient la carte générique du site. Quand un
journaliste colle le lien dans LinkedIn, Bluesky, WhatsApp ou un CMS, l'aperçu ne
dit donc rien de la ressource -- au moment précis où elle a besoin d'une identité.
La carte est ce que le lecteur voit AVANT d'ouvrir le lien.

LA FIGURE EST REDESSINÉE, JAMAIS RECADRÉE. Un recadrage du SVG publié se casserait
au premier changement de cadre, de marge ou de cartouche -- et en silence, puisque
personne ne regarde une image de partage. Elle est donc redessinée ici, à l'échelle
de la carte, À PARTIR DU JEU PUBLIÉ (`data/*.json`) : aucun chiffre en dur, et une
donnée qui bouge déplace la carte comme elle déplace la page.

PALETTE ET TYPOGRAPHIE. Mêmes constantes que les figures (charte du 2026-09-28 :
bleu profond #184f95, orange #eb6834, gris pour la série secondaire) et même fond
que les autres cartes du site (dégradé crème, Newsreader, filet bleu, URL en Inter).
Une carte qui ne ressemblerait pas aux figures ferait deux identités.

SORTIES : static/images/og-qui-paie-dette.jpg (exposition, depuis le 30/09), og-cout-dette.jpg, og-dette-monde.jpg (1200x630),
déclarées par `og_image` dans le front matter des deux pages.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "static" / "fonts"
OUT_DIR = ROOT / "static" / "images"
W, H = 1200, 630

C1, C2, SEC = (24, 79, 149), (235, 104, 52), (137, 135, 129)
NAVY = (31, 43, 77)
INK = (38, 38, 48)
GREY = (85, 82, 80)
RULE = (86, 110, 146)
URL_GREY = (150, 146, 143)
GRID = (214, 210, 205)

# Legende sous la figure du ciseau, posee par carte() selon la langue.
LEGENDE_CISEAU = ("", "")


def fail(msg: str) -> None:
    print("ECHEC : " + msg)
    sys.exit(1)


def font(name: str, size: int, weight: int = 400, italic: bool = False):
    """Reprise exacte du sélecteur d'axes de og_ressources_livre_base.py."""
    fam = "newsreader" if name == "newsreader" else "inter"
    base = "Newsreader" if fam == "newsreader" else "Inter"
    path = FONTS / fam / f"{base}-{'Italic-' if italic else ''}Variable.woff2"
    f = ImageFont.truetype(str(path), size)
    vals = []
    for ax in f.get_variation_axes():
        n = ax["name"] if isinstance(ax["name"], str) else ax["name"].decode()
        if n.lower().startswith("weight"):
            vals.append(weight)
        elif n.lower().startswith("optical"):
            vals.append(min(max(size, ax["minimum"]), ax["maximum"]))
        else:
            vals.append(ax["default"])
    f.set_variation_by_axes(vals)
    return f


def background() -> Image.Image:
    a, b = (249, 245, 242), (237, 233, 230)
    im = Image.new("RGB", (W, H))
    px = im.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            px[x, y] = tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))
    return im


def habillage(d: ImageDraw.ImageDraw, titre: list[str], accroche: str,
              source: str, url: str, cle: list[tuple]) -> None:
    y = 74
    ft = font("newsreader", 58, 600)
    for ligne in titre:
        d.text((70, y), ligne, font=ft, fill=NAVY)
        y += 68
    d.text((70, y + 10), accroche, font=font("newsreader", 25, 400, italic=True), fill=GREY)
    # CLÉ DE COULEUR. Sans elle la figure est muette : à cette taille aucune
    # étiquette ne tient sur les barres, et un aperçu de partage se lit en une
    # seconde. Elle occupe la colonne de gauche, restée vide sous l'accroche.
    yc = 322
    fc = font("inter", 19, 500)
    for couleur, libelle in cle:
        d.rectangle([70, yc, 88, yc + 18], fill=couleur)
        d.text((100, yc - 1), libelle, font=fc, fill=INK)
        yc += 36
    d.line([(70, H - 96), (W - 70, H - 96)], fill=RULE, width=2)
    d.text((70, H - 80), source, font=font("inter", 21, 500), fill=INK)
    d.text((70, H - 48), url, font=font("inter", 19, 400), fill=URL_GREY)


def figure_exposition(d: ImageDraw.ImageDraw, ex: dict) -> None:
    """Volet 2 : un même effort de 10 Md€ réparti selon trois décisions, en % du revenu de chaque dixième.
    Le point D1 de la décision fiscale est écarté dans le jeu publié (motif dans le JSON) : il est absent ici aussi."""
    x0, x1, top, bas = 648, 1126, 100, 424
    series = [(ex["taux"]["enseignement"], C2), (ex["taux"]["fiscal"], C1), (ex["taux"]["pensions"], SEC)]
    vmax = max(v for s, _c in series for v in s if v is not None)
    vmax = (int(vmax * 2) + 1) / 2.0

    def X(i):
        return x0 + (x1 - x0) * i / 9

    def Y(v):
        return bas - (bas - top) * v / vmax

    g = 0.0
    while g <= vmax + 1e-9:
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=2 if g == 0 else 1)
        g += 0.5
    for serie, c in series:
        pts = [(X(i), Y(v)) for i, v in enumerate(serie) if v is not None]
        d.line(pts, fill=c, width=5, joint="curve")
        for x, y in pts:
            d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=c)
    fa = font("inter", 18, 500)
    d.text((x0, bas + 14), "D1", font=fa, fill=URL_GREY)
    d.text((x1 - 34, bas + 14), "D10", font=fa, fill=URL_GREY)
    d.text((x0, bas + 40), "Un effort de %g Md€, en %% du revenu de chaque" % ex["effort_mdeur"],
           font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "dixième de niveau de vie, %s" % ex["millesime"], font=font("inter", 17, 400), fill=URL_GREY)

def figure_ciseau(d: ImageDraw.ImageDraw, annees: list[int],
                  dette: list[float], interets: list[float]) -> None:
    """Le ciseau du volet 1 : l'encours qui monte, la charge qui baisse puis
    remonte. Deux échelles distinctes, une même unité — comme dans la page."""
    x0, x1, top, bas = 648, 1126, 110, 424
    n = len(annees)

    def X(i):
        return x0 + (x1 - x0) * i / (n - 1)

    def mk(serie):
        lo, hi = min(serie), max(serie)
        marge = (hi - lo) * 0.12 or 1.0
        return lambda v: bas - (v - lo + marge) / (hi - lo + 2 * marge) * (bas - top)

    Yd, Yi = mk(dette), mk(interets)
    for f in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = top + (bas - top) * f
        d.line([(x0, y), (x1, y)], fill=GRID, width=1)
    d.line([(X(i), Yd(v)) for i, v in enumerate(dette)], fill=C1, width=5, joint="curve")
    d.line([(X(i), Yi(v)) for i, v in enumerate(interets)], fill=C2, width=5, joint="curve")
    fa = font("inter", 18, 500)
    d.text((x0, bas + 14), str(annees[0]), font=fa, fill=URL_GREY)
    d.text((x1 - 44, bas + 14), str(annees[-1]), font=fa, fill=URL_GREY)
    l1, l2 = LEGENDE_CISEAU
    d.text((x0, bas + 40), l1, font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), l2, font=font("inter", 17, 400), fill=URL_GREY)


def figure_jumeaux(d: ImageDraw.ImageDraw, rows: list[dict], bas_code: str, haut_code: str) -> None:
    """Volet 3 : le nuage « Même dette, charge différente » réduit à l'essentiel — les 27 pays en gris,
    la paire de faux jumeaux désignée par la règle de la page, reliée, en bleu (bas) et orange (haut)."""
    x0, x1, top, bas = 660, 1126, 100, 424
    xmax = 160.0
    ymax = max(10.0, max(r["charge"] for r in rows) * 1.08)

    def X(v):
        return x0 + (x1 - x0) * min(v, xmax) / xmax

    def Y(v):
        return bas - (bas - top) * v / ymax

    for g in range(0, int(ymax) + 1, 2):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=2 if g == 0 else 1)
    for r in rows:
        if r["code"] not in (bas_code, haut_code):
            cx, cy = X(r["stock"]), Y(r["charge"])
            d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(196, 192, 188))
    by = {r["code"]: r for r in rows}
    pb, ph = by[bas_code], by[haut_code]
    d.line([(X(pb["stock"]), Y(pb["charge"])), (X(ph["stock"]), Y(ph["charge"]))], fill=GREY, width=3)
    for r, c in ((pb, C1), (ph, C2)):
        cx, cy = X(r["stock"]), Y(r["charge"])
        d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=c)
    fa = font("inter", 18, 500)
    d.text((x0, bas + 14), "0", font=fa, fill=URL_GREY)
    d.text((x1 - 70, bas + 14), "160 %", font=fa, fill=URL_GREY)
    d.text((x0, bas + 40), "Les 27 pays de l'UE : dette en % du PIB (horizontal)",
           font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "et intérêts en % des recettes publiques (vertical)",
           font=font("inter", 17, 400), fill=URL_GREY)


def carte(nom: str, titre: list[str], accroche: str, source: str, url: str,
          dessin, cle: list[tuple], legende: tuple = None) -> None:
    global LEGENDE_CISEAU
    if legende:
        LEGENDE_CISEAU = legende
    im = background()
    d = ImageDraw.Draw(im)
    dessin(d)
    habillage(d, titre, accroche, source, url, cle)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    p = OUT_DIR / nom
    im.save(p, "JPEG", quality=92, optimize=True)
    print("OK  %s (%dx%d, %d ko)" % (nom, W, H, p.stat().st_size // 1024))


def figure_cascade_mini(d: ImageDraw.ImageDraw, dyn: dict) -> None:
    """Volet « Pourquoi elle augmente » : la cascade de la page, réduite — stock de départ, intérêts, croissance,
    déficits primaires, flux-stock, stock d'arrivée. Valeurs lues dans data/dette_dynamique.json."""
    t, dep, fin = dyn["total"], dyn["depart"]["dette_pct_pib"], dyn["annees"][-1]["dette_pct_pib"]
    etapes = [(dep, "s"), (t["effet_interets"], "d"), (t["effet_croissance"], "d"),
              (t["contribution_solde_primaire"], "d"), (t["flux_stock"], "d"), (fin, "s")]
    x0, x1, top, bas = 660, 1126, 100, 424
    vmax = (int(max(dep + t["effet_interets"], fin) * 1.08 / 20) + 1) * 20

    def Y(v):
        return bas - (bas - top) * v / vmax

    for g in range(0, vmax + 1, 40):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=2 if g == 0 else 1)
    pas = (x1 - x0) / len(etapes)
    bw = pas * 0.6
    niveau = 0.0
    for k, (v, nat) in enumerate(etapes):
        cx = x0 + pas * (k + 0.5)
        if nat == "s":
            b, h, col, niveau = 0.0, v, C1, v
        else:
            b, h = (niveau, niveau + v) if v >= 0 else (niveau + v, niveau)
            col = C2 if v >= 0 else SEC
            niveau += v
        d.rectangle([cx - bw / 2, Y(h), cx + bw / 2, Y(b)], fill=col)
    fa = font("inter", 18, 500)
    d.text((x0, bas + 14), str(dyn["depart"]["annee"]), font=fa, fill=URL_GREY)
    d.text((x1 - 44, bas + 14), str(dyn["annees"][-1]["annee"]), font=fa, fill=URL_GREY)
    d.text((x0, bas + 40), "Dette publique française, en points de PIB :", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "départ, intérêts, croissance, déficits, flux-stock", font=font("inter", 17, 400), fill=URL_GREY)


def carte_dynamique() -> None:
    """Volet 1 (30/09) : « Pourquoi la dette a doublé ». Chiffres lus dans le jeu publié ; le contraste annoncé
    (intérêts et croissance presque annulés, déficits primaires dominants) est contrôlé ici."""
    f = ROOT / "data" / "dette_dynamique.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_dette_dynamique.py d'abord" % f)
    dyn = json.loads(f.read_text(encoding="utf-8"))
    A, t = dyn["affichage"], dyn["total"]
    if not (abs(t["effet_taux_croissance"]) < 5 and t["contribution_solde_primaire"] > 0.75 * t["variation"]):
        fail("carte dynamique : le contraste annoncé n'est plus vrai dans les données")
    carte("og-dette-dynamique.jpg",
          ["Pourquoi la dette", "a doublé"],
          "Intérêts et croissance se sont presque annulés.",
          "Eurostat, France %s-%s · CC BY 4.0" % (A["annee_depart"], A["annee_fin"]),
          "stephane-lalut.com/pourquoi-la-dette-publique-augmente/",
          lambda d: figure_cascade_mini(d, dyn),
          [(C2, "Intérêts : +%s pts" % A["effet_interets"]), (SEC, "Croissance : −%s pts" % A["effet_croissance"]),
           (C2, "Déficits primaires : +%s pts" % A["deficits_primaires"]), (C1, "Dette : %s → %s %%" % (A["dette_depart"], A["dette_fin"]))])


def carte_monde() -> None:
    """Volet 3, comparaison internationale (avis du 30/09 : l'aperçu doit montrer la découverte de la page).
    Tout vient de data/dette_monde.json : la paire de faux jumeaux (règle publiée), et les chaînes
    françaises du bloc `affichage`, celles-là mêmes que la page imprime — la carte ne peut pas dire autre
    chose que la page. Lancée aussi par le workflow dette-monde.yml (option --monde), dans le même geste
    que les données."""
    dm = ROOT / "data" / "dette_monde.json"
    if not dm.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_dette_monde.py d'abord" % dm)
    j = json.loads(dm.read_text(encoding="utf-8"))
    A, rows, j0 = j["affichage"], j["europe"], j["faux_jumeaux"][0]
    if (A["j_bas"], A["j_haut"]) != (next(r["nom"] for r in rows if r["code"] == j0["bas"]),
                                     next(r["nom"] for r in rows if r["code"] == j0["haut"])):
        fail("carte monde : la paire affichée ne correspond plus au premier couple de faux jumeaux")
    nbsp = lambda s: s.replace(" ", " ")
    cle = [(C1, "%s : dette %s du PIB, intérêts %s des recettes"
            % (A["j_bas"], nbsp(A["j_bas_stock"]), nbsp(A["j_bas_charge"]))),
           (C2, "%s : dette %s du PIB, intérêts %s des recettes"
            % (A["j_haut"], nbsp(A["j_haut_stock"]), nbsp(A["j_haut_charge"])))]
    fc = font("inter", 19, 500)
    for _, t in cle:
        if 100 + fc.getlength(t) > 640:
            fail("carte monde : ligne de clé trop longue pour la colonne (%s)" % t)
    carte("og-dette-monde.jpg",
          ["Même dette,", "charge × %s" % A["j_rapport"]],
          "Le stock ne dit pas ce que la dette coûte.",
          "Eurostat %s · 27 pays de l'UE · CC BY 4.0" % j["meta"]["annee"],
          "stephane-lalut.com/dette-publique-comparaison-internationale/",
          lambda d: figure_jumeaux(d, rows, j0["bas"], j0["haut"]),
          cle)


def main() -> int:
    if "--monde" in sys.argv[1:]:
        carte_monde()
        carte_dynamique()
        return 0
    carte_monde()
    carte_dynamique()
    qp = ROOT / "data" / "qui_paie_donnees.json"
    do = ROOT / "data" / "dette_officielle.json"
    for f in (qp, do):
        if not f.is_file():
            fail("jeu de données absent : %s — lancer son générateur d'abord" % f)
    ex = json.loads(qp.read_text(encoding="utf-8"))["exposition"]
    o = json.loads(do.read_text(encoding="utf-8"))

    # Volet 2 (avis du 30/09) : la carte montre le résultat PROPRE à la page — un même effort, des payeurs
    # différents selon la décision — et non plus la redistribution générale, commune à bien des sources.
    # Le contraste qu'elle annonce est CONTRÔLÉ ici : l'enseignement pèse plus en D2 qu'en D10, l'impôt l'inverse.
    t = ex["taux"]
    if not (t["enseignement"][1] > t["enseignement"][9] and t["fiscal"][9] > t["fiscal"][1]):
        fail("la carte annonce que l'enseignement pèse en bas et l'impôt en haut : ce n'est plus vrai dans les données")
    carte("og-qui-paie-dette.jpg",
          ["Même effort,", "d'autres payeurs"],
          "Qui paie la dette dépend de la décision prise pour l'ajuster.",
          "Insee, comptes nationaux distribués %s · CC BY 4.0" % ex["millesime"],
          "stephane-lalut.com/qui-paie-la-dette-publique/",
          lambda d: figure_exposition(d, ex),
          [(C2, "Baisse de l'enseignement"), (C1, "Hausse des impôts (revenus, patrimoine)"),
           (SEC, "Baisse des pensions")])

    # Volet 1 : la fenêtre COMMUNE aux deux séries, lue dans le jeu publié. Le
    # ciseau n'a de sens que si les deux grandeurs couvrent les mêmes années.
    dpib = o["dette_annuelle_longue"]["series"]["pct_pib"]
    ipib = o["interets_annuels"]["series"]["pct_pib"]
    ans = sorted(set(dpib) & set(ipib))
    if len(ans) < 10:
        fail("volet 1 : années communes insuffisantes (%d) dans data/dette_officielle.json"
             % len(ans))
    ciseau = lambda d: figure_ciseau(d, [int(a) for a in ans],
                                     [dpib[a] for a in ans], [ipib[a] for a in ans])
    carte("og-cout-dette.jpg",
          ["Combien coûte", "la dette publique ?"],
          "L'encours a doublé en part de PIB ; la facture, elle, a d'abord baissé.",
          "Données INSEE et Eurostat · CC BY 4.0",
          "stephane-lalut.com/cout-de-la-dette-publique/",
          ciseau,
          [(C1, "Encours de dette"), (C2, "Charge d'intérêts")],
          ("Encours de dette et charge d'intérêts, en % du PIB",
           "deux échelles distinctes, une même unité"))

    # La page anglaise est diffusee a des medias anglophones : sa carte ne peut
    # pas porter un titre francais. Une carte de partage est LUE avant le lien,
    # et dans la mauvaise langue elle dit au lecteur que la page n'est pas pour
    # lui. Meme figure, meme palette, meme cadre -- seuls les mots changent.
    carte("og-cout-dette-en.jpg",
          ["What does French", "public debt cost?"],
          "The stock doubled as a share of GDP; the bill, at first, fell.",
          "INSEE and Eurostat data · CC BY 4.0",
          "stephane-lalut.com/en/cost-of-french-public-debt/",
          ciseau,
          [(C1, "Debt stock"), (C2, "Interest burden")],
          ("Debt stock and interest burden, as a share of GDP",
           "two distinct scales, one shared unit"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
