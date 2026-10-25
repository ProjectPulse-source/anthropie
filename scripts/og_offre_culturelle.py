#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""og_offre_culturelle.py -- image de partage des pages de comité (/offre-culturelle/<id>/).

Maquette B retenue par l'auteur le 25/10/2026 (planche « Vignettes des livres offerts ») : L'Odyssée des idées en
avant, les cinq autres titres en éventail, le message à gauche. Une seule image pour tous les comités : leur nom passe
par le titre de partage (head.html, branche « offre-culturelle »), jamais par l'image, qui ne porte aucun logo.

Couvertures lues dans assets/images/livres/ (la source de la fiche) : une couverture qui change se reporte ici en
relançant le script. Polices du site : Inter (scripts/polices/) et Newsreader (static/fonts/, woff2 converti en
mémoire). Sortie : static/images/og-offre-culturelle.jpg, 1200 x 630, JPEG ; le script s'arrête au-delà de 300 Ko
(seuil couramment cité pour l'aperçu en grand de WhatsApp, non documenté par WhatsApp).

Usage : python scripts/og_offre_culturelle.py [--dry]
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
LIVRES = ROOT / "assets" / "images" / "livres"
SORTIE = ROOT / "static" / "images" / "og-offre-culturelle.jpg"
INTER = ROOT / "scripts" / "polices" / "Inter-VariableFont_opsz,wght.ttf"
NEWSREADER = ROOT / "static" / "fonts" / "newsreader" / "Newsreader-Variable.woff2"
POIDS_MAX = 300_000

W, H = 1200, 630
FOND, BLEU, ENCRE, GRIS = (246, 247, 250), (24, 79, 149), (27, 42, 78), (74, 86, 114)
SURTITRE = "OFFRE CULTURELLE DE VOTRE COMITÉ"
TITRE = ["Un livre numérique", "offert, à garder"]
TEXTE = "Six titres au choix, sans paiement. Choisissez le vôtre : il arrive sur votre compte Amazon.fr."
PIED = "STÉPHANE LALUT · LIVRES OFFERTS"
# (fichier, largeur, gauche, haut, angle CSS en degrés, sens horaire) — ordre de pose : le dernier passe devant.
COUVERTURES = [
    ("anthropie-ordre-ici-dette-ailleurs", 138, 1040, 150, 10),
    ("un-president-peut-il-tenir-ses-promesses", 138, 978, 116, 6),
    ("la-societe-du-premier-coup", 138, 916, 94, 2),
    ("dette-publique-qui-paie-vraiment", 138, 854, 84, -2),
    ("livresque-des-mots", 138, 792, 94, -6),
    ("lodyssee-des-idees", 232, 696, 156, -4),
]


def police(chemin: Path, taille: int, poids: int, opsz: int) -> ImageFont.FreeTypeFont:
    if chemin.suffix == ".woff2":
        f = TTFont(str(chemin))
        f.flavor = None
        buf = io.BytesIO()
        f.save(buf)
        buf.seek(0)
        p = ImageFont.truetype(buf, taille)
    else:
        p = ImageFont.truetype(str(chemin), taille)
    valeurs = []
    for a in p.get_variation_axes():
        nom = a["name"].decode() if isinstance(a["name"], bytes) else a["name"]
        valeurs.append(poids if nom == "Weight" else max(a["minimum"], min(a["maximum"], opsz)))
    p.set_variation_by_axes(valeurs)
    return p


def espace(d: ImageDraw.ImageDraw, xy, texte, p, couleur, interlettre: float) -> None:
    """Texte avec interlettrage (en fraction de la taille), comme letter-spacing en CSS."""
    x, y = xy
    for c in texte:
        d.text((x, y), c, font=p, fill=couleur)
        x += d.textlength(c, font=p) + interlettre * p.size


def lignes(d, texte, p, largeur):
    mots, res, cour = texte.split(), [], ""
    for m in mots:
        essai = (cour + " " + m).strip()
        if d.textlength(essai, font=p) <= largeur:
            cour = essai
        else:
            res.append(cour)
            cour = m
    return res + [cour]


def couverture(img: Image.Image, nom, largeur, gauche, haut, angle) -> None:
    c = Image.open(LIVRES / f"{nom}.jpg").convert("RGB")
    c = c.resize((largeur, round(c.height * largeur / c.width)), Image.LANCZOS)
    cx, cy = gauche + c.width / 2, haut + c.height / 2
    # ombre : box-shadow 0 6px 19px rgba(10,20,45,.35) de la maquette
    marge = 40
    om = Image.new("L", (c.width + 2 * marge, c.height + 2 * marge), 0)
    ImageDraw.Draw(om).rectangle([marge, marge + 6, marge + c.width, marge + c.height + 6], fill=int(255 * .35))
    om = om.filter(ImageFilter.GaussianBlur(9)).rotate(-angle, resample=Image.BICUBIC, expand=True)
    img.paste(Image.new("RGB", om.size, (10, 20, 45)), (round(cx - om.width / 2), round(cy - om.height / 2)), om)
    masque = Image.new("L", c.size, 255).rotate(-angle, resample=Image.BICUBIC, expand=True)
    cr = c.rotate(-angle, resample=Image.BICUBIC, expand=True)
    img.paste(cr, (round(cx - cr.width / 2), round(cy - cr.height / 2)), masque)


def dessiner() -> Image.Image:
    img = Image.new("RGB", (W, H), FOND)
    d = ImageDraw.Draw(img)
    for c in COUVERTURES:
        couverture(img, *c)
    d = ImageDraw.Draw(img)
    p_sur = police(INTER, 26, 600, 26)
    p_titre = police(NEWSREADER, 60, 600, 60)
    p_texte = police(INTER, 28, 400, 28)
    p_pied = police(INTER, 23, 600, 23)
    espace(d, (66, 84), SURTITRE, p_sur, BLEU, .12)
    y = 84 + 26 + 26
    for l in TITRE:
        d.text((66, y), l, font=p_titre, fill=ENCRE)
        y += round(60 * 1.06)
    y += 29
    for l in lignes(d, TEXTE, p_texte, 552):
        d.text((66, y), l, font=p_texte, fill=GRIS)
        y += round(28 * 1.35)
    d.rectangle([66, 515, 66 + 96, 515 + 6], fill=BLEU)
    espace(d, (66, 541), PIED, p_pied, BLEU, .04)
    return img


def main() -> None:
    dry = "--dry" in sys.argv
    img = dessiner()
    for q in (88, 85, 82, 80):
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= POIDS_MAX:
            break
    else:
        raise SystemExit(f"ARRET : {buf.tell()} octets au-delà de {POIDS_MAX}, même à la qualité 80")
    print(f"{SORTIE.name} : {W}x{H}, qualité {q}, {buf.tell()} octets{' (essai, rien écrit)' if dry else ''}")
    if not dry:
        SORTIE.write_bytes(buf.getvalue())


if __name__ == "__main__":
    main()
