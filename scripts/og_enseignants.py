#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""og_enseignants.py -- cartes de partage et vignettes des pages /enseignants/ecole-et-parcours/ et /enseignants/environnement/.

    python scripts/og_enseignants.py

Même organe que les cartes du dossier dette : `carte()`, l'habillage, les polices et la palette viennent de
og_dossier_dette.py, importé tel quel -- une seconde copie de ces constantes ferait deux identités. Seul le dessin
est propre : les quatre barres empilées de la figure, redessinées à l'échelle de la carte À PARTIR DU JEU PUBLIÉ
(data/parcours_licence.json), jamais recadrées dans le SVG. Aucun chiffre en dur.

À relancer après scripts/generer_parcours_licence.py quand la cohorte change (édition annuelle du SIES, novembre) :
le millésime et les valeurs de la clé en dépendent.

SORTIES : static/images/og-parcours-licence.jpg et og-empreinte-carbone.jpg (1200x630), avec leurs vignettes vig-*.jpg
(720x378, fond blanc, lues par l'index /ressources/), déclarées par `og_image` dans les deux pages. La seconde carte
se relance après scripts/generer_empreinte_carbone.py (édition annuelle Insee-SDES, mi-octobre).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
JEU = ROOT / "data" / "parcours_licence.json"
GRIS_CLAIR = (201, 197, 192)
ISSUES = [("passage", og.C1), ("redoublement", og.SEC), ("reorientation", GRIS_CLAIR), ("sortie", og.C2)]
ORIGINES = [("tf", "Très favorisée"), ("f", "Favorisée"), ("ad", "Assez défavorisée"), ("d", "Défavorisée")]


def figure_barres(d, cohorte: dict) -> None:
    """Quatre barres empilées à 100 %, une par origine sociale ; le nom de l'origine au-dessus de sa barre."""
    x0, x1, top, hb, pas = 660, 1126, 122, 34, 76
    fa = og.font("inter", 18, 500)
    for n, (cle, lib) in enumerate(ORIGINES):
        t = cohorte["origines"][cle]["taux_publies"]
        y = top + pas * n
        d.text((x0, y - 26), lib, font=fa, fill=og.GREY)
        total = sum(t[k] for k, _ in ISSUES)
        x = float(x0)
        for k, col in ISSUES:
            w = (x1 - x0) * t[k] / total
            d.rectangle([x, y, x + w - 2, y + hb], fill=col)      # 2 px de blanc : séparateur lisible en gris
            x += w
    yb = top + pas * len(ORIGINES) - 14
    fl = og.font("inter", 17, 400)
    d.text((x0, yb), "Un an après une première année de licence,", font=fl, fill=og.URL_GREY)
    d.text((x0, yb + 22), "selon l'origine sociale, en % des inscrits", font=fl, fill=og.URL_GREY)


def main() -> int:
    if not JEU.is_file():
        og.fail("jeu de données absent : %s — lancer scripts/generer_parcours_licence.py d'abord" % JEU)
    j = json.loads(JEU.read_text(encoding="utf-8"))
    A = j["affichage"]
    cohorte = max(j["cohortes"], key=lambda c: c["annee"])
    if str(cohorte["annee"]) != A["cohorte"]:
        og.fail("carte licence : la cohorte du bloc affichage n'est pas la plus récente du jeu")
    o = cohorte["origines"]
    # Ce que la carte montre au premier regard, contrôlé : le passage décroît de gauche à droite de l'échelle sociale.
    p = [o[c]["taux_publies"]["passage"] for c, _ in ORIGINES]
    if not all(a > b for a, b in zip(p, p[1:])):
        og.fail("carte licence : le passage en deuxième année ne décroît plus d'une origine à la suivante")
    og.carte("og-parcours-licence.jpg",
             ["Avons-nous tous", "le même droit", "à l'erreur ?"],
             "",      # titre sur trois lignes : l'accroche toucherait la clé ; elle est sous la figure
             "MESRE-SIES, bacheliers %s · activité de SES, Terminale · CC BY 4.0" % A["cohorte"],
             "stephane-lalut.com/enseignants/ecole-et-parcours/",
             lambda d: figure_barres(d, cohorte),
             [(og.C1, "Passés en deuxième année : %s à %s %%" % (A["d_passage"], A["tf_passage"])),
              (og.SEC, "Recommencent une première année"),
              (GRIS_CLAIR, "Réorientés hors licence : %s à %s %%" % (A["reorientation_min"], A["reorientation_max"])),
              (og.C2, "Non retrouvés dans les fichiers")])
    carte_empreinte()
    return 0


def figure_deux_totaux(d, dec: dict) -> None:
    """Les deux barres de la figure, à la même échelle : émissions des unités résidentes, empreinte."""
    x0, larg, top, hb, pas = 660, 400, 150, 58, 118
    ech = larg / dec["empreinte"]
    fa, fv = og.font("inter", 18, 500), og.font("inter", 22, 600)
    for n, (lib, postes, total) in enumerate([("Émissions des unités résidentes", [("menages", GRIS_CLAIR), ("interieure", og.C1), ("exportee", og.SEC)], dec["emissions"]),
                                              ("Empreinte carbone", [("menages", GRIS_CLAIR), ("interieure", og.C1), ("importee", og.C2)], dec["empreinte"])]):
        y = top + pas * n
        d.text((x0, y - 28), lib, font=fa, fill=og.GREY)
        x = float(x0)
        for cle, col in postes:
            w = dec[cle] * ech
            d.rectangle([x, y, x + w - 2, y + hb], fill=col)
            x += w
        d.text((x + 10, y + 14), "%d" % round(total), font=fv, fill=og.INK)
    fl = og.font("inter", 17, 400)
    yb = top + pas * 2 - 26
    d.text((x0, yb), "Gaz à effet de serre, France,", font=fl, fill=og.URL_GREY)
    d.text((x0, yb + 22), "en millions de tonnes équivalent CO2", font=fl, fill=og.URL_GREY)


def carte_empreinte() -> None:
    """Page /enseignants/environnement/ : valeurs lues dans data/empreinte_carbone.json."""
    f = ROOT / "data" / "empreinte_carbone.json"
    if not f.is_file():
        og.fail("jeu de données absent : %s — lancer scripts/generer_empreinte_carbone.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    A, dec = j["affichage"], j["decomposition"]
    if not dec["empreinte"] > dec["emissions"] > 0:
        og.fail("carte empreinte : l'empreinte ne dépasse plus les émissions des unités résidentes")
    og.carte("og-empreinte-carbone.jpg",
             ["Émissions, empreinte", "carbone : pourquoi", "deux totaux ?"],
             "",
             "Insee et SDES, France %s · activité de SES, Terminale · CC BY 4.0" % A["annee"],
             "stephane-lalut.com/enseignants/environnement/",
             lambda d: figure_deux_totaux(d, dec),
             [(GRIS_CLAIR, "Émissions directes des ménages : %s" % A["menages"]),
              (og.C1, "Production en France, demande française : %s" % A["interieure"]),
              (og.SEC, "Production en France exportée : %s" % A["exportee"]),
              (og.C2, "Importations, demande française : %s" % A["importee"])])


if __name__ == "__main__":
    sys.exit(main())
