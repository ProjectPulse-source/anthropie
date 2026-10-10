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

SORTIES : static/images/og-qui-paie-dette.jpg (exposition, depuis le 30/09), og-cout-dette.jpg, og-dette-monde.jpg,
og-dette-dynamique.jpg, et leurs versions anglaises -en.jpg (depuis le 30/09) (1200x630),
déclarées par `og_image` dans le front matter des deux pages. Pour chacune, une vignette `vig-*.jpg` (720x378,
même dessin sur fond blanc), lue par l'index /ressources/ à la place de l'image de partage (depuis le 01/10).
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


def figure_exposition(d: ImageDraw.ImageDraw, ex: dict, lang: str = "fr") -> None:
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
    if lang == "en":
        l1 = "A %g bn euro adjustment, as %% of each standard-of-living" % ex["effort_mdeur"]
        l2 = "decile's income, %s" % ex["millesime"]
    else:
        l1 = "Un effort de %g Md€, en %% du revenu de chaque" % ex["effort_mdeur"]
        l2 = "dixième de niveau de vie, %s" % ex["millesime"]
    d.text((x0, bas + 40), l1, font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), l2, font=font("inter", 17, 400), fill=URL_GREY)

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


def figure_jumeaux(d: ImageDraw.ImageDraw, rows: list[dict], bas_code: str, haut_code: str, lang: str = "fr") -> None:
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
    en = lang == "en"
    d.text((x1 - 70, bas + 14), "160%" if en else "160 %", font=fa, fill=URL_GREY)
    d.text((x0, bas + 40), "The 27 EU countries: debt as % of GDP (across)" if en
           else "Les 27 pays de l'UE : dette en % du PIB (horizontal)", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "and interest as % of public revenue (up)" if en
           else "et intérêts en % des recettes publiques (vertical)", font=font("inter", 17, 400), fill=URL_GREY)


def carte(nom: str, titre: list[str], accroche: str, source: str, url: str,
          dessin, cle: list[tuple], legende: tuple = None) -> None:
    global LEGENDE_CISEAU
    if legende:
        LEGENDE_CISEAU = legende
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # VIGNETTE (01/10/2026) : même dessin sur fond BLANC, réduit, pour les cartes de l'index /ressources/.
    # Le fond crème de la carte de partage, posé dans une carte blanche, faisait un rectangle gris collé ; la
    # carte de partage garde le sien (identité commune des cartes du site). Dessinée dans le même geste,
    # jamais à part : une vignette tirée d'un autre passage montrerait d'autres chiffres que la page.
    for fond, sortie in ((background(), nom), (Image.new("RGB", (W, H), (255, 255, 255)), nom.replace("og-", "vig-", 1))):
        im = fond
        d = ImageDraw.Draw(im)
        dessin(d)
        habillage(d, titre, accroche, source, url, cle)
        p = OUT_DIR / sortie
        if sortie == nom:
            im.save(p, "JPEG", quality=92, optimize=True)
        else:
            im.resize((720, 378), Image.LANCZOS).save(p, "JPEG", quality=88, optimize=True)
        print("OK  %s (%dx%d, %d ko)" % (sortie, im.width if sortie == nom else 720,
                                         im.height if sortie == nom else 378, p.stat().st_size // 1024))


def figure_cascade_mini(d: ImageDraw.ImageDraw, dyn: dict, lang: str = "fr") -> None:
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
    en = lang == "en"
    d.text((x0, bas + 40), "French public debt, in points of GDP:" if en
           else "Dette publique française, en points de PIB :", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "start, interest, growth, deficits, stock-flow" if en
           else "départ, intérêts, croissance, déficits, flux-stock", font=font("inter", 17, 400), fill=URL_GREY)


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
    # Version anglaise (30/09/2026, demande de l'auteur : le dossier dans les deux langues). Même figure, même
    # contrôle ; chaînes du bloc affichage_en, celles que la page anglaise imprime.
    E = dyn.get("affichage_en")
    if not E:
        fail("carte dynamique EN : bloc affichage_en absent de data/dette_dynamique.json")
    carte("og-dette-dynamique-en.jpg",
          ["Why French debt", "doubled"],
          "Interest and growth almost cancelled out.",
          "Eurostat, France %s-%s · CC BY 4.0" % (E["annee_depart"], E["annee_fin"]),
          "stephane-lalut.com/en/why-does-public-debt-rise/",
          lambda d: figure_cascade_mini(d, dyn, "en"),
          [(C2, "Interest: +%s pts" % E["effet_interets"]), (SEC, "Growth: −%s pts" % E["effet_croissance"]),
           (C2, "Primary deficits: +%s pts" % E["deficits_primaires"]), (C1, "Debt: %s → %s%%" % (E["dette_depart"], E["dette_fin"]))])


def figure_decennies_mini(d: ImageDraw.ImageDraw, dec: list[dict], lang: str = "fr") -> None:
    """Volet « Peut-elle baisser » : la figure signature réduite — par décennie, effet taux-croissance, déficits
    primaires, flux-stock. Orange : fait monter le ratio ; gris : le fait baisser. Valeurs lues dans data/dette_baisse.json."""
    x0, x1, top, bas = 660, 1126, 100, 424
    vals = [f[k] for f in dec for k in ("taux_croissance", "deficits_primaires", "flux_stock")]
    vmax, vmin = (int(max(vals) / 10) + 1) * 10, -(int(-min(vals) / 10) + 1) * 10

    def Y(v):
        return bas - (bas - top) * (v - vmin) / (vmax - vmin)

    for g in range(vmin, vmax + 1, 10):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=3 if g == 0 else 1)
    pas = (x1 - x0) / len(dec)
    fa = font("inter", 18, 500)
    for k, f in enumerate(dec):
        gx = x0 + pas * k
        bw = pas * 0.76 / 3
        for j, cle in enumerate(("taux_croissance", "deficits_primaires", "flux_stock")):
            v = f[cle]
            x = gx + pas * 0.12 + bw * j
            y0, y1 = (Y(v), Y(0)) if v >= 0 else (Y(0), Y(v))
            d.rectangle([x + 3, y0, x + bw - 3, y1], fill=C2 if v >= 0 else SEC)
        lib = "%d-%d" % (f["debut"], f["fin"])
        d.text((gx + pas / 2 - fa.getlength(lib) / 2, bas + 14), lib, font=fa, fill=URL_GREY)
    en = lang == "en"
    d.text((x0, bas + 40), "French public debt, in points of GDP per decade:" if en
           else "Dette publique française, en points de PIB par décennie :", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "interest-growth, primary deficits, stock-flow" if en
           else "taux-croissance, déficits primaires, flux-stock", font=font("inter", 17, 400), fill=URL_GREY)


def carte_baisse() -> None:
    """Volet 5 (02/10/2026) : « La dette peut-elle baisser ? ». Chiffres lus dans le jeu publié ; le contraste annoncé
    (taux et croissance allègent, les déficits primaires poussent davantage, la dette monte) est contrôlé ici."""
    f = ROOT / "data" / "dette_baisse.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_dette_baisse.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, dec = j["affichage"], j["france"]["decennies"]
    d3 = dec[-1]
    if not (d3["taux_croissance"] < 0 and d3["deficits_primaires"] > -d3["taux_croissance"] and d3["variation"] > 0):
        fail("carte baisse : le contraste annoncé n'est plus vrai dans les données")
    carte("og-dette-baisse.jpg",
          ["Les déficits", "ont pesé plus lourd"],
          "%s : plus que l'allègement par les taux et la croissance." % A["d3_lib"],
          "Eurostat, France %s-%s · CC BY 4.0" % (A["annee_debut"], A["annee_fin"]),
          "stephane-lalut.com/dette-publique-peut-elle-baisser/",
          lambda d: figure_decennies_mini(d, dec),
          [(SEC, "Taux et croissance : −%s pts" % A["d3_tc_abs"]), (C2, "Déficits primaires : +%s pts" % A["d3_def_abs"]),
           (C1, "Dette : %s → %s %%" % (A["d3_dette_deb"], A["d3_dette_fin"]))])
    # Version anglaise (03/10/2026, miroir de la page) : même figure, même contrôle ; chaînes du bloc affichage_en.
    E = j.get("affichage_en")
    if not E:
        fail("carte baisse EN : bloc affichage_en absent de data/dette_baisse.json")
    carte("og-dette-baisse-en.jpg",
          ["Deficits", "weighed more"],
          "%s: more than the relief from rates and growth." % E["d3_lib"],
          "Eurostat, France %s-%s · CC BY 4.0" % (E["annee_debut"], E["annee_fin"]),
          "stephane-lalut.com/en/can-public-debt-come-down/",
          lambda d: figure_decennies_mini(d, dec, "en"),
          [(SEC, "Interest and growth: −%s pts" % E["d3_tc_abs"]), (C2, "Primary deficits: +%s pts" % E["d3_def_abs"]),
           (C1, "Debt: %s → %s%%" % (E["d3_dette_deb"], E["d3_dette_fin"]))])


def figure_generations_mini(d: ImageDraw.ImageDraw, periodes: list[dict], lang: str = "fr") -> None:
    """Prolongement « Générations futures » : la figure signature réduite — par décennie, part du besoin de financement
    en actifs (bleu), en transferts en capital (gris) et en dépenses courantes non couvertes (orange). Valeurs lues dans
    data/dette_generations.json."""
    x0, x1, top = 660, 1126, 112
    fa = font("inter", 18, 500)
    for k, p in enumerate(periodes):
        y = top + 100 * k
        d.text((x0, y - 28), "%d-%d" % (p["debut"], p["fin"]), font=fa, fill=URL_GREY)
        x = x0
        for cle, col in (("part_actifs", C1), ("part_transferts", SEC), ("part_desepargne", C2)):
            w = (x1 - x0) * max(p[cle], 0) / 100
            d.rectangle([x, y, x + w, y + 46], fill=col)
            x += w
    en = lang == "en"
    d.text((x0, top + 300), "Share of French public deficits, by decade:" if en
           else "Part des déficits publics français, par décennie :", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, top + 322), "assets, capital transfers, current spending" if en
           else "actifs, transferts en capital, dépenses courantes", font=font("inter", 17, 400), fill=URL_GREY)


def carte_generations() -> None:
    """Prolongement « Générations futures » (03/10/2026). Chiffres lus dans le jeu publié ; le contraste annoncé (la part
    en actifs baisse d'une décennie à l'autre, la dernière est faible, les dépenses courantes dominent) est contrôlé ici."""
    f = ROOT / "data" / "dette_generations.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_dette_generations.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, per = j["affichage"], j["france"]["periodes"][1:]
    if not (per[0]["part_actifs"] > per[1]["part_actifs"] > per[2]["part_actifs"] and per[2]["part_actifs"] < 15
            and per[2]["part_desepargne"] > 60):
        fail("carte générations : le contraste annoncé n'est plus vrai dans les données")
    carte("og-dette-generations.jpg",
          ["Des déficits", "pour le courant"],
          "%s : %s %% seulement en actifs comptabilisés." % (A["d3_lib"], A["d3_part"]),
          "Eurostat, France %s-%s · CC BY 4.0" % (A["a0"], A["fin"]),
          "stephane-lalut.com/dette-publique-generations-futures/",
          lambda d: figure_generations_mini(d, per),
          [(C1, "Actifs : %s %% → %s %%" % (A["d1_part"], A["d3_part"])),
           (SEC, "Transferts en capital"),
           (C2, "Dépenses courantes non couvertes")])
    # Version anglaise (07/10/2026, miroir de la page) : même figure, même contrôle ; chaînes du bloc affichage_en.
    E = j.get("affichage_en")
    if not E:
        fail("carte générations EN : bloc affichage_en absent de data/dette_generations.json")
    carte("og-dette-generations-en.jpg",
          ["Deficits for", "current spending"],
          "%s: only %s%% in recorded assets." % (E["d3_lib"], E["d3_part"]),
          "Eurostat, France %s-%s · CC BY 4.0" % (E["a0"], E["fin"]),
          "stephane-lalut.com/en/public-debt-future-generations/",
          lambda d: figure_generations_mini(d, per, "en"),
          [(C1, "Assets: %s%% → %s%%" % (E["d1_part"], E["d3_part"])),
           (SEC, "Capital transfers"),
           (C2, "Uncovered current spending")])


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
    # Version anglaise : mêmes contrôles de largeur ; chaînes du bloc affichage_en (noms de pays en anglais).
    E = j.get("affichage_en")
    if not E:
        fail("carte monde EN : bloc affichage_en absent de data/dette_monde.json")
    cle_en = [(C1, "%s: debt %s of GDP, interest %s of revenue" % (E["j_bas"], E["j_bas_stock"], E["j_bas_charge"])),
              (C2, "%s: debt %s of GDP, interest %s of revenue" % (E["j_haut"], E["j_haut_stock"], E["j_haut_charge"]))]
    for _, t in cle_en:
        if 100 + fc.getlength(t) > 640:
            fail("carte monde EN : ligne de clé trop longue pour la colonne (%s)" % t)
    carte("og-dette-monde-en.jpg",
          ["Same debt,", "burden × %s" % E["j_rapport"]],
          "The stock does not say what the debt costs.",
          "Eurostat %s · 27 EU countries · CC BY 4.0" % j["meta"]["annee"],
          "stephane-lalut.com/en/public-debt-international-comparison/",
          lambda d: figure_jumeaux(d, rows, j0["bas"], j0["haut"], "en"),
          cle_en)


def figure_collectivites(d: ImageDraw.ImageDraw, inv: dict, tr: dict, lang: str = "fr") -> None:
    """Prolongement « Collectivités » (01/10/2026) : la figure signature de la page, réduite — investissement local (bleu)
    et transferts reçus (gris, série comparable jusqu'en 2017), bande de la baisse des dotations 2014-2017."""
    x0, x1, top, bas = 660, 1126, 100, 424
    a0, a1 = min(inv), max(inv)
    vmin, vmax = 1.5, 5.0

    def X(a):
        return x0 + (x1 - x0) * (a - a0) / (a1 - a0)

    def Y(v):
        return bas - (bas - top) * (v - vmin) / (vmax - vmin)

    d.rectangle([X(2014), top, X(2017.999), bas], fill=(243, 239, 230))
    for g in (2, 3, 4, 5):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=1)
    d.line([(X(a), Y(v)) for a, v in sorted(tr.items())], fill=SEC, width=5, joint="curve")
    d.line([(X(a), Y(v)) for a, v in sorted(inv.items())], fill=C1, width=5, joint="curve")
    fa = font("inter", 18, 500)
    d.text((x0, bas + 14), str(a0), font=fa, fill=URL_GREY)
    d.text((x1 - 44, bas + 14), str(a1), font=fa, fill=URL_GREY)
    en = lang == "en"
    d.text((x0, bas + 40), "Local government, France, in % of GDP:" if en
           else "Collectivités, France, en % du PIB :", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "band: grant cuts 2014-2017" if en
           else "bande : baisse des dotations 2014-2017", font=font("inter", 17, 400), fill=URL_GREY)


def carte_collectivites() -> None:
    """Prolongement « Collectivités locales » : séries et chaînes lues dans data/dette_collectivites.json ; le contraste
    annoncé (transferts et investissement en baisse sur l'épisode, dette locale contenue) est CONTRÔLÉ ici."""
    f = ROOT / "data" / "dette_collectivites.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_dette_collectivites.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, c, se = j["affichage"], j["calcul"], j["series"]
    if not (c["ep_transf"] < 0 and c["ep_inv"] < 0 and c["part_hausse_loc"] < 10):
        fail("carte collectivités : le contraste annoncé n'est plus vrai dans les données")
    inv = {int(k): v for k, v in se["serie_inv_fr"].items()}
    tr = {int(k): v for k, v in se["serie_transf_fr"].items()}
    carte("og-collectivites.jpg",
          ["L'ajustement local,", "hors de la dette"],
          "La dette locale est restée contenue ; l'investissement a reculé.",
          "Eurostat %s · OFGL · CC BY 4.0" % A["an_fin"],
          "stephane-lalut.com/dette-publique-collectivites-locales/",
          lambda d: figure_collectivites(d, inv, tr),
          [(C1, "Investissement : −%s pt de PIB (%s-%s)" % (A["ep_inv"], A["ep_a0"], A["ep_a1"])),
           (SEC, "Transferts reçus : −%s pt de PIB" % A["ep_transf"]),
           (URL_GREY, "Dette locale : %s → %s %% du PIB (%s-%s)" % (A["dette_loc_deb"], A["dette_loc_fin"], A["an_dette_deb"], A["an_dette_fin"]))])
    # Version anglaise (07/10/2026, page /en/local-government-debt/) : même figure, même contrôle ; chaînes du bloc
    # affichage_en, celles que la page anglaise imprime.
    E = j.get("affichage_en")
    if not E:
        fail("carte collectivités EN : bloc affichage_en absent de data/dette_collectivites.json")
    carte("og-collectivites-en.jpg",
          ["Local adjustment,", "outside the debt"],
          "Local debt stayed contained; investment fell.",
          "Eurostat %s · OFGL · CC BY 4.0" % E["an_fin"],
          "stephane-lalut.com/en/local-government-debt/",
          lambda d: figure_collectivites(d, inv, tr, "en"),
          [(C1, "Investment: −%s pts of GDP (%s-%s)" % (E["ep_inv"], E["ep_a0"], E["ep_a1"])),
           (SEC, "Transfers received: −%s pts of GDP" % E["ep_transf"]),
           (URL_GREY, "Local debt: %s → %s%% of GDP (%s-%s)" % (E["dette_loc_deb"], E["dette_loc_fin"], E["an_dette_deb"], E["an_dette_fin"]))])


def figure_inflation_mini(d: ImageDraw.ImageDraw, cal: dict, lo: float, hi: float, lang: str = "fr") -> None:
    """Prolongement « Inflation et dette » : la figure signature réduite — érosion réelle cumulée des paiements promis
    sur la dette de l'État à taux fixe de fin 2020, au fil des paiements. Valeurs lues dans data/dette_inflation.json."""
    x0, x1, top, bas = 660, 1126, 110, 424
    ans = sorted(int(a) for a in cal)
    a0, a1, vmax = 2020, ans[-1], 200

    def X(a):
        return x0 + (x1 - x0) * (a - a0) / (a1 - a0)

    def Y(v):
        return bas - (bas - top) * v / vmax

    for g in range(0, vmax + 1, 50):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=3 if g == 0 else 1)
    d.rectangle([X(2052), Y(hi), x1, Y(lo)], fill=(226, 223, 219))
    pts = [(X(a0), Y(0))] + [(X(a), Y(cal[str(a)])) for a in ans]
    d.line(pts, fill=C1, width=6, joint="curve")
    fa = font("inter", 18, 500)
    for a in (2025, 2045, 2065):
        d.text((X(a) - fa.getlength(str(a)) / 2, bas + 14), str(a), font=fa, fill=URL_GREY)
    en = lang == "en"
    d.text((x0, bas + 40), "End-2020 fixed-rate government debt: real erosion" if en
           else "Dette de l'État à taux fixe de fin 2020 : érosion réelle", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "of promised payments, cumulative, €bn (2020 euros)" if en
           else "des paiements promis, cumulée, en Md€ de 2020", font=font("inter", 17, 400), fill=URL_GREY)


def carte_inflation() -> None:
    """Prolongement « L'inflation a-t-elle vraiment allégé la dette française ? » (07/10/2026). Chiffres lus dans le jeu
    publié ; le contraste annoncé (érosion acquise, réalisée lentement : moins d'un quart payé fin 2023) est contrôlé ici."""
    f = ROOT / "data" / "dette_inflation.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_dette_inflation.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, E, cal = j["affichage"], j.get("affichage_en"), j["calendrier"]
    T = j["resultats"]["central"]
    lo, hi = min(v["r=0%"] for v in j["famille_A"].values()), max(v["r=0%"] for v in j["famille_A"].values())
    if not (cal["2023"] < 0.25 * T and abs(cal[max(cal, key=int)] - T) < 0.2):
        fail("carte inflation : le contraste annoncé n'est plus vrai dans les données")
    if not E:
        fail("carte inflation EN : bloc affichage_en absent de data/dette_inflation.json")
    carte("og-dette-inflation.jpg",
          ["L'inflation a érodé", "la vieille dette"],
          "Environ %s Md€ de 2020 : mesurés, non encaissés." % A["t"],
          "AFT, Eurostat, BCE · calcul de l'auteur · CC BY 4.0",
          "stephane-lalut.com/inflation-et-dette-publique/",
          lambda d: figure_inflation_mini(d, cal, lo, hi),
          [(C1, "Érosion cumulée : %s Md€" % A["t"]), ((226, 223, 219), "Prévisions de début 2021 : %s à %s" % (A["a_bas"], A["a_haut"]))])
    carte("og-dette-inflation-en.jpg",
          ["Inflation eroded", "legacy debt"],
          "About €%sbn in 2020 euros: measured, not banked." % E["t"],
          "AFT, Eurostat, ECB · author's calculation · CC BY 4.0",
          "stephane-lalut.com/en/inflation-and-french-public-debt/",
          lambda d: figure_inflation_mini(d, cal, lo, hi, "en"),
          [(C1, "Cumulative erosion: €%sbn" % E["t"]), ((226, 223, 219), "Early-2021 forecasts: %s to %s" % (E["a_bas"], E["a_haut"]))])


def figure_lycee_mini(d: ImageDraw.ImageDraw, h: dict) -> None:
    """Ressource « Manque-t-il des professeurs au lycée ? » (07/10/2026) : la figure signature réduite — heures de cours
    non assurées au lycée GT, 2024-2025, absences individuelles (orange) contre fermetures, examens et formation (bleu)."""
    x0, x1, top = 660, 1126, 196
    vmax = 12.0
    sx = lambda v: (x1 - x0) * v / vmax
    org = h["fermeture"] + h["systeme"] + h["formation"]
    fa, fb = font("inter", 20, 500), font("inter", 26, 600)
    for k, (lib, v, col) in enumerate((("Absences individuelles", h["individuelles"], C2), ("Fermetures, examens et commissions, formation", org, C1))):
        y = top + k * 110
        d.text((x0, y), lib, font=fa, fill=URL_GREY)
        d.rectangle([x0, y + 34, x0 + sx(v), y + 84], fill=col)
        lab = ("%.1f" % v).replace(".", ",") + " %"
        d.text((x0 + sx(v) + 12, y + 44), lab, font=fb, fill=col)
    d.text((x0, top + 240), "Heures non assurées au lycée général et", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, top + 262), "technologique, 2024-2025, % des heures prévues", font=font("inter", 17, 400), fill=URL_GREY)


def carte_lycee() -> None:
    """Ressource « Manque-t-il des professeurs au lycée ? » (07/10/2026). Chiffres lus dans le jeu publié ; le contraste
    annoncé (fermetures, examens et formation pèsent plus que les absences individuelles) est contrôlé ici. Français seulement."""
    f = ROOT / "data" / "lycee_professeurs.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_lycee_professeurs.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A = j["affichage"]
    h = j["heures_non_assurees"]["2024-2025"]["En lycée général"]
    if not (h["fermeture"] + h["systeme"] + h["formation"] > h["individuelles"]):
        fail("carte lycée : le contraste annoncé n'est plus vrai dans les données")
    carte("og-lycee-professeurs.jpg",
          ["Manque-t-il des", "professeurs au lycée ?"],
          "Une heure de cours sur %s n'a pas lieu." % {"10": "dix"}[A["h_un_sur"]],
          "DEPP · calcul de l'auteur · CC BY 4.0",
          "stephane-lalut.com/manque-t-il-des-professeurs/",
          lambda d: figure_lycee_mini(d, h),
          [(C2, "Absences individuelles : %s %%" % A["h_indiv"]), (C1, "Fermetures, examens, formation : %s %%" % A["h_org"])])


def figure_niveau_mini(d: ImageDraw.ImageDraw, P: dict) -> None:
    """Ressource « Le niveau des élèves baisse-t-il ? » (08/10/2026) : variation des scores PISA 2015-2025, France (orange)
    contre la médiane des pays de l'OCDE (gris), par domaine."""
    x0, x1, top = 660, 1126, 150
    vmax = 50.0
    sx = lambda v: (x1 - x0 - 90) * v / vmax
    fa, fb = font("inter", 20, 500), font("inter", 22, 600)
    for k, (dom, lib) in enumerate((("lecture", "Lecture"), ("mathematiques", "Mathématiques"), ("sciences", "Sciences"))):
        y = top + k * 92
        fr, med = -P[dom]["variation_2015_2025"]["v"], -P[dom]["mediane_ocde"]
        d.text((x0, y), lib, font=fa, fill=URL_GREY)
        d.rectangle([x0, y + 30, x0 + sx(fr), y + 54], fill=C2)
        d.text((x0 + sx(fr) + 10, y + 28), "−%d" % round(fr), font=fb, fill=C2)
        d.rectangle([x0, y + 58, x0 + sx(med), y + 72], fill=(170, 166, 160))
    d.text((x0, top + 280), "Baisse du score PISA de 2015 à 2025, en points :", font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, top + 302), "France (orange), médiane des pays de l'OCDE (gris)", font=font("inter", 17, 400), fill=URL_GREY)


def carte_niveau() -> None:
    """Ressource « Le niveau des élèves baisse-t-il ? » (08/10/2026). Chiffres lus dans le jeu publié ; le contraste annoncé
    (en mathématiques, baisse française plus forte que dans les trois quarts des pays) est contrôlé ici. Français seulement."""
    f = ROOT / "data" / "niveau_eleves.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_niveau_eleves.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, P = j["affichage"], j["pisa"]
    for dom in P:
        pays = sorted(P[dom]["pays_ocde_2015_2025"].values())
        n = len(pays)
        P[dom]["mediane_ocde"] = (pays[n // 2] + pays[(n - 1) // 2]) / 2
        P[dom]["q1"] = sorted(pays)[n // 4]
    if not (P["mathematiques"]["variation_2015_2025"]["v"] < P["mathematiques"]["q1"]):
        fail("carte niveau : le contraste annoncé n'est plus vrai dans les données")
    carte("og-niveau-eleves.jpg",
          ["Le niveau des élèves", "baisse-t-il ?"],
          "En maths, une des plus fortes baisses de l'OCDE.",
          "OCDE, PISA 2025 · calcul de l'auteur · CC BY 4.0",
          "stephane-lalut.com/le-niveau-des-eleves-baisse-t-il/",
          lambda d: figure_niveau_mini(d, P),
          [(C2, "France, 2015-2025 : −%s points en maths" % A["math_v15"]), ((170, 166, 160), "Médiane des pays de l'OCDE : −%s" % A["math_med"])])


def figure_langue_mini(d: ImageDraw.ImageDraw, A: dict, X: dict) -> None:
    """Ressource « Les élèves maîtrisent-ils moins bien la langue française ? » (09/10/2026) : même dictée de CM2, erreurs
    lexicales (bleu) et autres erreurs (orange), 1987-2021."""
    x0, top, base, hmax, bw, gap = 680, 120, 430, 280, 80, 30
    tot, lx = X["dictee"]["total"], X["dictee"]["lexicales"]
    sy = lambda v: hmax * v / 22.0
    fb, fa = font("inter", 22, 600), font("inter", 18, 500)
    for i, a in enumerate(("1987", "2007", "2015", "2021")):
        x = x0 + i * (bw + gap)
        d.rectangle([x, base - sy(lx[a]), x + bw, base], fill=C1)
        d.rectangle([x, base - sy(tot[a]), x + bw, base - sy(lx[a])], fill=C2)
        d.text((x + 8, base - sy(tot[a]) - 32), A["tot" + a[2:]], font=fb, fill=C2)
        d.text((x + 16, base + 8), a, font=fa, fill=URL_GREY)


def carte_langue() -> None:
    """Ressource « Les élèves maîtrisent-ils moins bien la langue française ? » (09/10/2026). Chiffres lus dans le jeu
    publié ; la part de la hausse annoncée (orthographe des mots, environ un dixième) est contrôlée ici."""
    f = ROOT / "data" / "langue_eleves.json"
    if not f.is_file():
        fail("jeu de données absent : %s — lancer scripts/update_langue_eleves.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, dic = j["affichage"], j["dictee"]
    t, l = dic["total"], dic["lexicales"]
    # Refonte du 10/10 (arbitrage de phase A, C1) : la carte dit la part de la HAUSSE, plus « surtout la grammaire »
    # (le détail par type n'existe que pour 1987-2007).
    if not (0 < l["2021"] - l["1987"] and 0.07 <= (l["2021"] - l["1987"]) / (t["2021"] - t["1987"]) <= 0.14):
        fail("carte langue : « environ un dixième de la hausse » n'est plus vrai dans les données")
    carte("og-langue-eleves.jpg",
          ["Les élèves maîtrisent-ils", "moins bien la langue ?"],
          "Même dictée : %s erreurs de plus, dont %s sur l'orthographe des mots." % (A["h_tot"], A["h_lex"]),
          "DEPP, NI 22.37 · calcul de l'auteur · CC BY 4.0",
          "stephane-lalut.com/les-eleves-maitrisent-ils-moins-bien-la-langue-francaise/",
          lambda d: figure_langue_mini(d, A, j),
          [(C1, "Orthographe des mots : %s puis %s erreurs" % (A["lex87"], A["lex21"])), (C2, "Autres erreurs : %s puis %s" % (A["aut87"], A["aut21"]))])


def main() -> int:
    if "--langue" in sys.argv[1:]:
        carte_langue()
        return 0
    if "--collectivites" in sys.argv[1:]:
        carte_collectivites()
        return 0
    if "--generations" in sys.argv[1:]:
        carte_generations()
        return 0
    if "--inflation" in sys.argv[1:]:
        carte_inflation()
        return 0
    if "--lycee" in sys.argv[1:]:
        carte_lycee()
        return 0
    if "--niveau" in sys.argv[1:]:
        carte_niveau()
        return 0
    if "--monde" in sys.argv[1:]:
        carte_monde()
        carte_dynamique()
        carte_baisse()
        carte_generations()   # mêmes séries Eurostat, même workflow (dette-monde.yml), 03/10/2026
        return 0
    carte_monde()
    carte_dynamique()
    carte_baisse()
    carte_collectivites()
    carte_generations()
    carte_inflation()
    carte_lycee()
    carte_niveau()
    carte_langue()
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
    carte("og-qui-paie-dette-en.jpg",
          ["Same adjustment,", "different payers"],
          "Who pays the debt depends on the decision taken to adjust.",
          "Insee, distributional national accounts %s · CC BY 4.0" % ex["millesime"],
          "stephane-lalut.com/en/who-really-pays-public-debt/",
          lambda d: figure_exposition(d, ex, "en"),
          [(C2, "Cut in education spending"), (C1, "Higher taxes (income, wealth)"),
           (SEC, "Cut in pensions")])

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
