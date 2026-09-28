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

SORTIES : static/images/og-qui-paie-dette.jpg et og-cout-dette.jpg (1200x630),
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


def figure_deciles(d: ImageDraw.ImageDraw, r: dict) -> None:
    """Prélèvements et transferts par dixième — la figure la plus reconnaissable
    du volet 2 : le contraste entre un versé qui explose et un reçu presque plat."""
    esp = [v / 1000 for v in r["prestations_especes"][:10]]
    nat = [v / 1000 for v in r["transferts_non_monetaires"][:10]]
    prel = [-v / 1000 for v in r["prelevements"][:10]]
    x0, x1, top, bas = 648, 1126, 100, 424
    vmax, vmin = 35, -100
    k = (bas - top) / (vmax - vmin)

    def Y(v):
        return top + (vmax - v) * k

    pas = (x1 - x0) / 10
    bw = 30
    for g in (-75, -50, -25, 0, 25):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=GRID, width=2 if g == 0 else 1)
    y0 = Y(0)
    for i in range(10):
        cx = x0 + pas * (i + 0.5)
        g, dte = cx - bw / 2, cx + bw / 2
        h1, h2, hp = esp[i] * k, nat[i] * k, prel[i] * k
        d.rectangle([g, y0 - h1, dte, y0], fill=C1)
        d.rectangle([g, y0 - h1 - 2 - h2, dte, y0 - h1 - 2], fill=SEC)
        d.rectangle([g, y0 + 2, dte, y0 + hp], fill=C2)
    fa = font("inter", 18, 500)
    d.text((x0, bas + 14), "D1", font=fa, fill=URL_GREY)
    d.text((x1 - 34, bas + 14), "D10", font=fa, fill=URL_GREY)
    d.text((x0, bas + 40), "Prélèvements et transferts publics par dixième de niveau",
           font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "de vie, 2023, en euros par unité de consommation",
           font=font("inter", 17, 400), fill=URL_GREY)


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
    d.text((x0, bas + 40), "Encours de dette et charge d'intérêts, en % du PIB",
           font=font("inter", 17, 400), fill=URL_GREY)
    d.text((x0, bas + 62), "deux échelles distinctes, une même unité",
           font=font("inter", 17, 400), fill=URL_GREY)


def carte(nom: str, titre: list[str], accroche: str, source: str, url: str,
          dessin, cle: list[tuple]) -> None:
    im = background()
    d = ImageDraw.Draw(im)
    dessin(d)
    habillage(d, titre, accroche, source, url, cle)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    p = OUT_DIR / nom
    im.save(p, "JPEG", quality=92, optimize=True)
    print("OK  %s (%dx%d, %d ko)" % (nom, W, H, p.stat().st_size // 1024))


def main() -> int:
    qp = ROOT / "data" / "qui_paie_donnees.json"
    do = ROOT / "data" / "dette_officielle.json"
    for f in (qp, do):
        if not f.is_file():
            fail("jeu de données absent : %s — lancer son générateur d'abord" % f)
    r = json.loads(qp.read_text(encoding="utf-8"))["redistribution"]
    o = json.loads(do.read_text(encoding="utf-8"))

    # Les phrases de la carte reprennent celles de la page ; le contraste qu'elles
    # annoncent est CONTRÔLÉ ici, comme le générateur de figures contrôle le sien.
    recus = [r["prestations_especes"][i] + r["transferts_non_monetaires"][i] for i in range(10)]
    prel = [-v for v in r["prelevements"][:10]]
    if not (max(recus) / min(recus)) < (max(prel) / min(prel)) / 3:
        fail("la carte annonce un reçu « beaucoup plus plat » que le versé : ce n'est "
             "plus vrai dans les données")

    carte("og-qui-paie-dette.jpg",
          ["Qui paie vraiment", "la dette publique ?"],
          "Ce qui est versé suit le niveau de vie. Ce qui est reçu, beaucoup moins.",
          "Données Insee et Banque de France via l'AFT · CC BY 4.0",
          "stephane-lalut.com/qui-paie-la-dette-publique/",
          lambda d: figure_deciles(d, r),
          [(C1, "Prestations en espèces"), (SEC, "Services publics valorisés"),
           (C2, "Prélèvements")])

    # Volet 1 : la fenêtre COMMUNE aux deux séries, lue dans le jeu publié. Le
    # ciseau n'a de sens que si les deux grandeurs couvrent les mêmes années.
    dpib = o["dette_annuelle_longue"]["series"]["pct_pib"]
    ipib = o["interets_annuels"]["series"]["pct_pib"]
    ans = sorted(set(dpib) & set(ipib))
    if len(ans) < 10:
        fail("volet 1 : années communes insuffisantes (%d) dans data/dette_officielle.json"
             % len(ans))
    carte("og-cout-dette.jpg",
          ["Combien coûte", "la dette publique ?"],
          "L'encours a doublé en part de PIB ; la facture, elle, a d'abord baissé.",
          "Données INSEE et Eurostat · CC BY 4.0",
          "stephane-lalut.com/cout-de-la-dette-publique/",
          lambda d: figure_ciseau(d, [int(a) for a in ans],
                                  [dpib[a] for a in ans], [ipib[a] for a in ans]),
          [(C1, "Encours de dette"), (C2, "Charge d'intérêts")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
