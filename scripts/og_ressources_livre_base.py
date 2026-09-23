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

Usage : python scripts/og_ressources_livre_base.py
Sortie : assets/images/og-ressources-livre-base.jpg (1200x630)
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "og-ressources-livre-base.jpg"
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


def main() -> None:
    im = background()

    # Ombre portee douce sous la couverture (la couverture elle-meme est posee par Hugo).
    shadow = Image.new("L", (W, H), 0)
    x0 = COVER_CX - SHADOW_W // 2
    ImageDraw.Draw(shadow).rectangle((x0 + 6, COVER_TOP + 10, x0 + SHADOW_W + 6, COVER_TOP + COVER_H + 10), fill=110)
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    im.paste(Image.new("RGB", (W, H), (60, 55, 50)), (0, 0), shadow)

    d = ImageDraw.Draw(im)
    y = 150
    d.text((TEXT_X, y), "Ressources offertes", font=font("newsreader", 62), fill=NAVY)
    y += 100
    f_sub = font("newsreader", 30)
    for line in ("Un livre numérique déjà financé,", "transmis à un lecteur invité"):
        d.text((TEXT_X, y), line, font=f_sub, fill=INK)
        y += 40
    y += 26
    f_it = font("newsreader", 23, italic=True)
    for line in ("Lisez. Et si vous aimez,", "faites circuler le savoir."):
        d.text((TEXT_X, y), line, font=f_it, fill=GREY_ITAL)
        y += 32
    y += 24
    d.rectangle((TEXT_X, y, TEXT_X + 56, y + 3), fill=RULE)
    y += 22
    d.text((TEXT_X, y), "stephane-lalut.com", font=font("inter", 19), fill=URL)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT, "JPEG", quality=92, optimize=True)
    print(f"ecrit : {OUT.relative_to(ROOT)} ({W}x{H})")


if __name__ == "__main__":
    main()
