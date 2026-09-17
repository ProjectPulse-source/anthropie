#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""og_couverture_livre.py -- remplace la couverture d'un livre sur sa fiche ET dans les images de partage.

Quand une couverture change, elle vit a deux endroits du site : `assets/images/livres/<slug>.jpg`
(fiche, mur /a-propos/, JSON-LD) et, inclinee, dans les images de partage `static/images/og-*.jpg`
(accueil, ressources offertes). Les poser a la main a coute une mesure au cas par cas (ANTHROPIE,
16/09) ; ce script la refait a chaque fois :

1. fiche : 1000x1500 tiree du master HD, JPEG progressif a la qualite de l'image remplacee ;
2. images de partage : pose de l'ANCIENNE couverture mesuree (SIFT + RANSAC, similitude), couvertures
   voisines mesurees de meme ; une couverture plus a droite passe devant (ordre des piles du site) ;
3. temoin avant ecriture : l'image est recomposee avec l'ANCIENNE couverture et comparee a l'image
   en ligne sur la zone visible -- au-dela du seuil, rien n'est ecrit ;
4. la nouvelle couverture est posee a la meme place, meme echelle, meme angle ; hors de sa zone,
   les pixels sont ceux de l'image d'origine.

Usage : python scripts/og_couverture_livre.py <slug> <master.png> [--dry]
"""
from __future__ import annotations

import io
import math
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
LIVRES = ROOT / "assets" / "images" / "livres"
OG = ROOT / "static" / "images"
SEUIL_TEMOIN = 3.0      # ecart moyen (niveaux) des images lissees entre l'image en ligne et sa recomposition
sift = cv2.SIFT_create(nfeatures=6000)


def jpeg_quality_of(path: Path) -> int:
    """Qualite libjpeg dont la table de luminance a la meme moyenne que celle du fichier."""
    target = sum(Image.open(path).quantization[0]) / 64
    best = min(range(50, 101), key=lambda q: abs(_qavg(q) - target))
    return best


def _qavg(q: int) -> float:
    buf = io.BytesIO()
    Image.new("RGB", (16, 16)).save(buf, "JPEG", quality=q)
    return sum(Image.open(io.BytesIO(buf.getvalue())).quantization[0]) / 64


def pose(cover: np.ndarray, scene_gray: np.ndarray):
    """Similitude cover(1000x1500) -> scene ; None si non trouvee."""
    small = cv2.resize(cover, (cover.shape[1] // 5, cover.shape[0] // 5), interpolation=cv2.INTER_AREA)
    k1, d1 = sift.detectAndCompute(cv2.cvtColor(small, cv2.COLOR_RGB2GRAY), None)
    k2, d2 = sift.detectAndCompute(scene_gray, None)
    if d1 is None or d2 is None:
        return None
    good = [a for a, b in cv2.BFMatcher().knnMatch(d1, d2, k=2) if a.distance < 0.75 * b.distance]
    if len(good) < 12:
        return None
    src = np.float32([k1[g.queryIdx].pt for g in good]) * 5
    dst = np.float32([k2[g.trainIdx].pt for g in good])
    M, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=2.0,
                                         maxIters=20000, confidence=0.999)
    if M is None or inl.sum() < 30:
        return None
    return M


def render(cover: np.ndarray, M: np.ndarray, size: tuple[int, int]):
    """Couverture posee par M ; renvoie (rgb, alpha) flottants. Reduction Lanczos a l'echelle de la
    pose, puis rotation bicubique : c'est la chaine qui reproduit le mieux les images en ligne
    (ecart 4,1 niveaux contre 6,4 a 15 pour les autres combinaisons mesurees le 2026-09-17)."""
    s = math.hypot(M[0, 0], M[1, 0])
    h0, w0 = cover.shape[:2]
    w, h = max(1, round(w0 * s)), max(1, round(h0 * s))
    small = np.asarray(Image.fromarray(cover).resize((w, h), Image.LANCZOS)).astype(np.float32)
    Ms = M.copy()
    Ms[:, 0] *= w0 / w
    Ms[:, 1] *= h0 / h
    rgb = cv2.warpAffine(small, Ms, size, flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    a = cv2.warpAffine(np.ones((h, w), np.float32), Ms, size, flags=cv2.INTER_LINEAR,
                       borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return rgb, a[..., None]


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) < 2:
        print(__doc__)
        return 2
    slug, master, dry = argv[0], Path(argv[1]), "--dry" in argv
    fiche = LIVRES / f"{slug}.jpg"
    old = np.asarray(Image.open(fiche).convert("RGB"))
    m = Image.open(master).convert("RGB")
    ratio = 1000 / 1500
    if abs(m.width / m.height - ratio) > 0.002:                       # recadrage centre au 2:3
        cw = round(m.height * ratio)
        m = m.crop(((m.width - cw) // 2, 0, (m.width - cw) // 2 + cw, m.height))
    new_img = m.resize((1000, 1500), Image.LANCZOS)
    new = np.asarray(new_img)
    others = {p.stem: np.asarray(Image.open(p).convert("RGB")) for p in sorted(LIVRES.glob("*.jpg"))
              if p.stem != slug and not p.stem.endswith(".en")}

    q = jpeg_quality_of(fiche)
    print(f"fiche {fiche.relative_to(ROOT)} : 1000x1500 depuis {master.name}, JPEG progressif q{q}")
    if not dry:
        new_img.save(fiche, "JPEG", quality=q, progressive=True, optimize=True)

    ecarts = 0
    for og in sorted(OG.glob("og-*.jpg")):
        scene = np.asarray(Image.open(og).convert("RGB")).astype(np.float32)
        gray = cv2.cvtColor(scene.astype(np.uint8), cv2.COLOR_RGB2GRAY)
        M = pose(old, gray)
        if M is None:
            continue
        s, ang = math.hypot(M[0, 0], M[1, 0]), math.degrees(math.atan2(M[1, 0], M[0, 0]))
        size = (scene.shape[1], scene.shape[0])
        _, a_t = render(old, M, size)
        cx_t = (M @ np.array([500, 750, 1]))[0]
        front = []
        for name, img in others.items():
            Mo = pose(img, gray)
            if Mo is not None and (Mo @ np.array([500, 750, 1]))[0] > cx_t:
                front.append(name)
                _, a_o = render(img, Mo, size)
                a_t = a_t * (1 - a_o)
        old_rgb, _ = render(old, M, size)
        vis = a_t[..., 0] > 0.98
        brut = float(np.abs(scene - old_rgb)[vis].mean())
        # le temoin compare les images LISSEES : une pose, un masquage ou une lumiere faux s'y voient ;
        # le grain JPEG et le detail fin du reechantillonnage, non (brut 4 a 6 niveaux sur un motif dense).
        # Lissage NORMALISE sur la zone visible : un flou ordinaire melait la couverture voisine au bord
        # (accueil, 17/09 : +19,7 niveaux dans les 6 px contre ANTHROPIE, 0 au pixel pres).
        mv = vis.astype(np.float32)[..., None]
        den = np.maximum(cv2.GaussianBlur(mv, (0, 0), 2.0)[..., None], 1e-3)
        lisse = lambda im: cv2.GaussianBlur(im * mv, (0, 0), 2.0) / den
        temoin = float(np.abs(lisse(scene) - lisse(old_rgb))[vis].mean())
        print(f"{og.name:34s} echelle {s:.4f} angle {ang:+.2f} deg | devant : {front or 'aucune'} | "
              f"zone visible {int(vis.sum())} px | temoin ancienne couverture {temoin:.2f} niveaux (brut {brut:.2f})")
        if temoin > SEUIL_TEMOIN:
            print(f"   ECART : recomposition != image en ligne, {og.name} non modifiee")
            ecarts += 1
            continue
        new_rgb, _ = render(new, M, size)
        out = scene * (1 - a_t) + new_rgb * a_t
        if not dry:
            qo = jpeg_quality_of(og)
            Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8)).save(og, "JPEG", quality=qo, optimize=True)
            print(f"   ecrite (JPEG q{qo})")
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
