#!/usr/bin/env python3
"""Cartes de partage et vignettes d'index des six notions à schéma (02/11/2026, demande de l'auteur).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Le schéma de la page est redessiné à l'échelle de
la carte, jamais recadré. Chaque libellé est relu dans la page source : s'il n'y figure plus, la carte n'est pas dessinée.
Écrit : static/images/{og,vig}-notion-<nom>{,-en}.jpg.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

X0, X1, HAUT, BAS = 660, 1126, 100, 424
FOND, TRAIT = (244, 241, 234), (214, 210, 205)


def plat(s: str) -> str:
    return s.replace("’", "'").replace(" ", " ").replace(" ", " ").lower()


def verifie(page: str, en: bool, libelles: list[str]) -> None:
    src = og.ROOT / "content" / page / ("_index.en.md" if en else "_index.md")
    texte = plat(src.read_text(encoding="utf-8"))
    for dossier in ("layouts/shortcodes", "layouts/partials"):
        for f in (og.ROOT / dossier).glob("*notion*"):
            texte += plat(f.read_text(encoding="utf-8"))
    for f in (og.ROOT / "static" / "img" / "figures").glob("spirale-anthropique-desktop*.svg"):
        texte += plat(f.read_text(encoding="utf-8"))
    absents = [x for x in libelles if plat(x) not in texte]
    if absents:
        og.fail("carte %s : libelles absents de la page : %s" % (page, absents))


def boite(d, x0, y0, x1, y1, txt, couleur, clair=False) -> None:
    d.rounded_rectangle([x0, y0, x1, y1], radius=6, fill=couleur if clair else FOND, outline=None if clair else TRAIT, width=2)
    d.rectangle([x0, y0, x0 + (x1 - x0), y0 + 4], fill=couleur)
    t = 19
    f = og.font("inter", t, 600)
    while d.textlength(txt, font=f) > x1 - x0 - 12 and t > 12:
        t -= 1
        f = og.font("inter", t, 600)
    d.text(((x0 + x1 - d.textlength(txt, font=f)) / 2, (y0 + y1) / 2 - t * 0.55), txt, font=f,
           fill=(255, 255, 255) if clair else og.INK)


def fleche(d, x, y0, y1) -> None:
    d.line([x, y0, x, y1 - 8], fill=og.GREY, width=3)
    d.polygon([(x - 8, y1 - 10), (x + 8, y1 - 10), (x, y1)], fill=og.GREY)


def rangee(d, y0, y1, noms, couleur, clair=False) -> None:
    n, g = len(noms), 12
    w = (X1 - X0 - g * (n - 1)) / n
    for i, t in enumerate(noms):
        x = X0 + i * (w + g)
        boite(d, x, y0, x + w, y1, t, couleur, clair)


def schema(etages):
    """etages : (libellés, couleur, plein). Un étage d'une boîte ou de plusieurs, reliés de haut en bas."""
    def dessin(d) -> None:
        h = 68
        n = len(etages)
        pas = (BAS - HAUT - h) / (n - 1)
        for i, (noms, col, plein) in enumerate(etages):
            y = HAUT + i * pas
            rangee(d, y, y + h, noms, col, plein)
            if i < n - 1:
                fleche(d, (X0 + X1) / 2, y + h + 6, y + pas - 6)
    return dessin


def spirale(noms):
    """Cinq états sur une spirale montante, comme la figure de la page (dessin réduit, sans échelle)."""
    def dessin(d) -> None:
        cx, cy = (X0 + X1) / 2 - 70, (HAUT + BAS) / 2 + 6
        pts = []
        for k in range(0, 361):
            a = math.radians(k * 2.0 - 90)
            r = 42 + k * 0.32
            pts.append((cx + r * math.cos(a) * 1.05, cy + r * math.sin(a) * 0.92))
        d.line(pts, fill=og.C1, width=4, joint="curve")
        f = og.font("inter", 19, 600)
        for i, t in enumerate(noms):
            k = 72 + i * 72
            x, y = pts[k]
            col = og.C2 if i >= 3 else og.C1
            d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=col)
            d.text((X1 - 150, HAUT + 34 + i * 54), t, font=f, fill=og.INK)
            d.ellipse([X1 - 174, HAUT + 40 + i * 54, X1 - 160, HAUT + 54 + i * 54], fill=col)
    return dessin


C1, C2, SEC = og.C1, og.C2, og.SEC
CARTES = [
    ("anthropie", "quest-ce-que-lanthropie", "quest-ce-que-lanthropie", "en/quest-ce-que-lanthropie",
     ["Qu’est-ce que", "l’anthropie ?"], ["What is", "anthropy?"],
     "Une hypothèse : le désordre est déplacé, pas résolu.", "A hypothesis: disorder is displaced, not resolved.",
     lambda m: schema([(m[0], C1, True), (m[1], SEC, False)]),
     ([["Ordre local"], ["Spatial", "Temporel", "Social"]], [["Local order"], ["Spatial", "Temporal", "Social"]]), False),
    ("boucle", "boucle-anthropique", "boucle-anthropique", "en/anthropic-loop",
     ["La boucle", "anthropique"], ["The anthropic", "loop"],
     "Un modèle conditionnel, de l’ordre à son retour.", "A conditional model, from order to its return.",
     lambda m: spirale(m), (["Déplacement", "Accumulation", "Saturation", "Retour", "Bifurcation"],
                            ["Displacement", "Accumulation", "Saturation", "Return", "Bifurcation"]), True),
    ("rebond", "effet-rebond", "effet-rebond", "en/rebound-effect",
     ["L’effet rebond"], ["The rebound", "effect"],
     "Comment un gain d’efficacité revient en consommation.", "How an efficiency gain comes back as consumption.",
     lambda m: schema([(m[0], C1, True), (m[1], SEC, False), (m[2], C2, True)]),
     ([["Gain d’efficacité"], ["Direct", "Indirect", "Macroéconomique"], ["Rebond partiel", "Paradoxe de Jevons"]],
      [["Efficiency gain"], ["Direct", "Indirect", "Macroeconomic"], ["Partial rebound", "Jevons paradox"]]), False),
    ("communs", "communs-negatifs", "communs-negatifs", "en/negative-commons",
     ["Les communs", "négatifs"], ["Negative", "commons"],
     "Du transfert à l’héritage.", "From transfer to legacy.",
     lambda m: schema([(m[0], C1, True), (m[1], SEC, False), (m[2], C2, True)]),
     ([["Un ordre produit"], ["Déplacement", "Accumulation", "Saturation"], ["Un commun négatif"]],
      [["An order produced"], ["Displacement", "Accumulation", "Saturation"], ["A negative commons"]]), False),
    ("dette-techno", "dette-technologique", "dette-technologique", "en/technological-debt",
     ["La dette", "technologique"], ["Technological", "debt"],
     "Comment un coût d’infrastructure devient une dette.", "How an infrastructure cost becomes a debt.",
     lambda m: schema([(m[0], C1, True), (m[1], SEC, False), (m[2], C2, True)]),
     ([["Infrastructure numérique"], ["Engagement", "Garantie", "Irréversibilisation"],
       ["Énergie", "Matière", "Territoire", "Attention"]],
      [["Digital infrastructure"], ["Commitment", "Guarantee", "Irreversibility"],
       ["Energy", "Matter", "Territory", "Attention"]]), False),
    ("reversibilite", "reversibilite-sociale", "reversibilite-sociale", "en/social-reversibility",
     ["La réversibilité", "sociale"], ["Social", "reversibility"],
     "Ce qui permet de rebondir : V = f(C, T, A).", "What makes bouncing back possible: V = f(C, T, A).",
     lambda m: schema([(m[0], SEC, False), (m[1], C1, True)]),
     ([["Capacité de repli", "Tarif d’échec", "Réadmission"], ["Réversibilité sociale"]],
      [["Fallback capacity", "Price of failure", "Readmission"], ["Social reversibility"]]), False),
]


def main() -> int:
    for nom, page, url_fr, url_en, t_fr, t_en, a_fr, a_en, fab, (m_fr, m_en), plat_liste in CARTES:
        for en, m in ((False, m_fr), (True, m_en)):
            verifie(page, en, m if plat_liste else [x for r in m for x in r])
        og.carte("og-notion-%s-en.jpg" % nom, t_en, a_en, "Stéphane Lalut · CC BY 4.0",
                 "stephane-lalut.com/%s/" % url_en, fab(m_en), [])
        og.carte("og-notion-%s.jpg" % nom, t_fr, a_fr, "Stéphane Lalut · CC BY 4.0",
                 "stephane-lalut.com/%s/" % url_fr, fab(m_fr), [])
    return 0


if __name__ == "__main__":
    sys.exit(main())
