#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""og_ressources_livre_base.py -- fond de la carte de partage des pages /ressources-offertes/<livre>/.

Chaque page ciblee partage l'image de SON livre, pas la carte collective de la page mere : c'est ce
qu'un lecteur voit dans WhatsApp avant d'ouvrir le lien. La carte est composee AU BUILD par Hugo
(layouts/partials/head.html) : ce fond + la couverture assets/images/livres/<livre>.jpg posee dans
la zone de gauche. Un nouveau livre a donc sa carte sans geste ; ce script ne se relance que pour
changer le fond lui-meme (texte, couleurs).

Style repris de static/images/og-ressources-offertes.jpg (mesure le 2026-09-23) : fond creme en
degrade, Newsreader pour le texte, filet bleu, URL en Inter gris. La zone de couverture tient dans
le carre central 630x630 (x = 285..915) que WhatsApp recadre pour son apercu compact.

Le meme script fabrique la carte COLLECTIVE de la page mere, static/images/og-ressources-offertes.jpg :
les couvertures de tous les livres de `$order` (layouts/ressources-offertes/list.html), lu a chaque
execution, en grille de trois colonnes. Elle, en revanche, est figee : un livre ajoute a `$order`
n'y entre qu'en relancant ce script.

Usage : python scripts/og_ressources_livre_base.py
Sorties : assets/images/og-ressources-livre-base.jpg et static/images/og-ressources-offertes.jpg (1200x630)
"""
from __future__ import annotations

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "og-ressources-livre-base.jpg"
OUT_MERE = ROOT / "static" / "images" / "og-ressources-offertes.jpg"
LIST = ROOT / "layouts" / "ressources-offertes" / "list.html"
COVERS = ROOT / "assets" / "images" / "livres"
FONTS = ROOT / "static" / "fonts"
W, H = 1200, 630

# Zone de la couverture -- DOIT rester egale aux constantes du partial og-ressources-livre.html.
COVER_CX, COVER_TOP, COVER_H = 450, 75, 480
SHADOW_W = 310  # largeur moyenne d'une couverture 2:3 a 480 px de haut

TEXT_X = 650
NAVY = (31, 43, 77)
INK = (38, 38, 48)
GREY_ITAL = (85, 82, 80)
RULE = (86, 110, 146)
URL = (150, 146, 143)


def font(name: str, size: int, weight: int = 400, italic: bool = False) -> ImageFont.FreeTypeFont:
    fam = "newsreader" if name == "newsreader" else "inter"
    base = "Newsreader" if fam == "newsreader" else "Inter"
    path = FONTS / fam / f"{base}-{'Italic-' if italic else ''}Variable.woff2"
    f = ImageFont.truetype(str(path), size)
    axes = f.get_variation_axes()
    vals = []
    for ax in axes:
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
    # Degrade diagonal mesure sur la carte collective : (249,245,242) en haut a gauche,
    # (237,233,230) en bas a droite.
    a, b = (249, 245, 242), (237, 233, 230)
    im = Image.new("RGB", (W, H))
    px = im.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            px[x, y] = tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))
    return im


def text_block(im: Image.Image, x: int, sub: tuple[str, str], ital: tuple[str, str]) -> None:
    d = ImageDraw.Draw(im)
    y = 150
    d.text((x, y), "Ressources offertes", font=font("newsreader", 62), fill=NAVY)
    y += 100
    f_sub = font("newsreader", 30)
    for line in sub:
        d.text((x, y), line, font=f_sub, fill=INK)
        y += 40
    y += 26
    f_it = font("newsreader", 23, italic=True)
    for line in ital:
        d.text((x, y), line, font=f_it, fill=GREY_ITAL)
        y += 32
    y += 24
    d.rectangle((x, y, x + 56, y + 3), fill=RULE)
    y += 22
    d.text((x, y), "stephane-lalut.com", font=font("inter", 19), fill=URL)


def drop_shadow(im: Image.Image, box: tuple[int, int, int, int], dx: int, dy: int, blur: int, alpha: int) -> None:
    shadow = Image.new("L", (W, H), 0)
    x0, y0, x1, y1 = box
    ImageDraw.Draw(shadow).rectangle((x0 + dx, y0 + dy, x1 + dx, y1 + dy), fill=alpha)
    im.paste(Image.new("RGB", (W, H), (60, 55, 50)), (0, 0), shadow.filter(ImageFilter.GaussianBlur(blur)))


def base_livre() -> None:
    im = background()
    x0 = COVER_CX - SHADOW_W // 2
    drop_shadow(im, (x0, COVER_TOP, x0 + SHADOW_W, COVER_TOP + COVER_H), 6, 10, 14, 110)
    text_block(im, TEXT_X, ("Un livre numérique déjà financé,", "transmis à un lecteur invité"),
               ("Lisez. Et si vous aimez,", "faites circuler le savoir."))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT, "JPEG", quality=92, optimize=True)
    print(f"ecrit : {OUT.relative_to(ROOT)} ({W}x{H})")


def order() -> list[str]:
    m = re.search(r'\$order := slice ((?:"[^"]+"\s*)+)\}\}', LIST.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"$order introuvable dans {LIST}")
    return re.findall(r'"([^"]+)"', m.group(1))


def carte_mere() -> None:
    slugs = order()
    missing = [s for s in slugs if not (COVERS / f"{s}.jpg").exists()]
    if missing:
        raise SystemExit(f"couverture absente : {missing}")
    cols = 3
    rows = -(-len(slugs) // cols)
    ch = 232 if rows == 2 else min(480, 480 // rows)
    gap, left, top = 16, 70, (H - rows * ch - (rows - 1) * 16) // 2
    cw = round(ch * 2 / 3)
    im = background()
    places = []
    for i, slug in enumerate(slugs):
        r, c = divmod(i, cols)
        cov = Image.open(COVERS / f"{slug}.jpg").convert("RGB")
        w = round(cov.width * ch / cov.height)
        cov = cov.resize((w, ch), Image.LANCZOS)
        x = left + c * (cw + gap) + (cw - w) // 2
        y = top + r * (ch + gap)
        places.append((cov, x, y))
        drop_shadow(im, (x, y, x + w, y + ch), 4, 7, 9, 95)
    for cov, x, y in places:
        im.paste(cov, (x, y))
    text_x = left + cols * cw + (cols - 1) * gap + 44
    text_block(im, text_x, ("Des livres numériques déjà financés,", "transmis aux lecteurs invités"),
               ("Recevez un livre sans paiement", "et faites circuler le savoir."))
    im.save(OUT_MERE, "JPEG", quality=85, optimize=True)
    print(f"ecrit : {OUT_MERE.relative_to(ROOT)} ({W}x{H}) -- {len(slugs)} livres : {', '.join(slugs)}")


def main() -> None:
    base_livre()
    carte_mere()


if __name__ == "__main__":
    main()
