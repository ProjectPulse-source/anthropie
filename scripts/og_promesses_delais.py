#!/usr/bin/env python3
"""Carte de partage et vignette d'index du volet « Délais » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les durées sont LUES dans
data/promesses_delais.json (scripts/update_promesses_delais.py), elles-mêmes lues dans les textes en vigueur.
Écrit : static/images/{og,vig}-delais-promesse{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

GRIS_CLAIR = (201, 205, 211)
BLEU_CLAIR = (127, 163, 207)


def barres(d, c: dict, lang: str = "fr") -> None:
    x0, x1 = 660, 1126
    duree = c["duree"]
    X = lambda a: x0 + (x1 - x0) * a / duree  # noqa: E731
    fl = og.font("inter", 17, 500)
    y = 186
    d.text((x0, y - 30), "General practice" if lang == "en" else "Médecine générale", font=fl, fill=og.INK)
    segs = ((0, c["s1"] / 2, GRIS_CLAIR), (c["s1"] / 2, c["s2"] / 2, GRIS_CLAIR), (c["s1"] / 2 + c["s2"] / 2, c["mg"], BLEU_CLAIR))
    for a0, l, col in segs:
        d.rectangle([X(a0) + 2, y, X(a0 + l) - 2, y + 54], fill=col)
    y2 = 306
    d.text((x0, y2 - 30), "Presidential term" if lang == "en" else "Mandat présidentiel", font=fl, fill=og.INK)
    d.rectangle([X(0) + 2, y2, X(c["mandat"]) - 2, y2 + 54], fill=og.C1)
    fa = og.font("inter", 17, 400)
    for a in (0, 5, 10):
        s = str(a)
        d.text((X(a) - d.textlength(s, font=fa) / 2, y2 + 66), s, font=fa, fill=og.URL_GREY)
    d.text((x0, y2 + 96), "years; comparison of scale only" if lang == "en" else "années ; comparaison d'échelle seulement", font=fa, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_delais.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_delais.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    c, A = j["calcul"], j["affichage"]
    if c["duree"] != c["mandat"] * c["nmax"]:
        og.fail("carte : « deux fois la durée d'un mandat » n'est plus vrai dans les textes")
    E = j["affichage_en"]
    og.carte("og-delais-promesse-en.jpg",
             ["At least %s years to" % E["duree_chiffre"], "train a GP in France"],
             "%s the length of a presidential term." % {"two": "Twice", "three": "Three times"}.get(E["nmax"], E["nmax"].capitalize() + " times"),
             "Texts in force (Légifrance) · DREES · ONDPS · CC BY 4.0",
             "stephane-lalut.com/en/can-a-campaign-promise-produce-results-within-five-years/",
             lambda d: barres(d, c, "en"),
             [(BLEU_CLAIR, "Third cycle: %s years" % E["mg"]), (og.C1, "Term: %s years" % E["mandat"])])
    og.carte("og-delais-promesse.jpg",
             ["Au moins %s ans pour" % A["duree_chiffre"], "former un généraliste"],
             "%s fois la durée d'un mandat présidentiel." % A["nmax"].capitalize(),
             "Textes en vigueur (Légifrance) · DREES · ONDPS · CC BY 4.0",
             "stephane-lalut.com/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/",
             lambda d: barres(d, c),
             [(BLEU_CLAIR, "Troisième cycle : %s ans" % A["mg"]),
              (og.C1, "Mandat : %s ans" % A["mandat"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
