#!/usr/bin/env python3
"""Carte de partage et vignette d'index du prolongement « Référendum » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Tout est LU dans data/promesses_referendum.json
(scripts/update_promesses_referendum.py) : la frise dessine les scrutins du registre, la date d'arrêté est sur la carte.
Écrit : static/images/og-referendum-promesse(-en).jpg et vig-referendum-promesse(-en).jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

GRIS = (138, 143, 152)


def frise(d, reg: list, lang: str = "fr") -> None:
    x0, x1, yb, h = 660, 1126, 330, 190
    a0, a1 = 1958, 2027
    X = lambda an: x0 + (an - a0) / (a1 - a0) * (x1 - x0)  # noqa: E731
    d.line([(x0, yb), (x1, yb)], fill=og.GREY, width=2)
    y50 = yb - h / 2
    for x in range(int(x0), int(x1), 14):
        d.line([(x, y50), (x + 7, y50)], fill=GRIS, width=1)
    for l in reg:
        an = int(l["date_scrutin"][:4]) + (int(l["date_scrutin"][5:7]) - 0.5) / 12
        p = l["oui"] / l["exprimes"]
        x, y = X(an), yb - p * h
        ad = l["oui"] > l["non"]
        d.line([(x, yb), (x, y)], fill=og.C1 if ad else GRIS, width=7)
        d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=og.C1 if ad else (255, 255, 255), outline=og.C1 if ad else og.INK, width=2)
    fl = og.font("inter", 17, 400)
    for an in (1960, 1980, 2000, 2020):
        s = str(an)
        d.text((X(an) - d.textlength(s, font=fl) / 2, yb + 10), s, font=fl, fill=og.URL_GREY)
    d.text((x0, yb - h - 34), "Share of 'yes' among valid votes" if lang == "en" else "Part des « oui » parmi les exprimés",
           font=fl, fill=og.GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_referendum.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_referendum.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    reg, a, e = j["registre"], j["affichage"], j["affichage_en"]
    if j["calcul"]["N"] != len(reg) or j["calcul"]["dernier"] != max(l["date_scrutin"] for l in reg):
        og.fail("carte : registre et calcul divergent")
    og.carte("og-referendum-promesse-en.jpg",
             ["%s referendums" % e["N"].capitalize(), "since 1958"],
             "National referendums; none since %s." % e["dernier"],
             "Conseil constitutionnel, as at %s · CC BY 4.0" % e["arrete"],
             "stephane-lalut.com/en/can-the-french-president-call-a-referendum/",
             lambda d: frise(d, reg, "en"),
             [(og.C1, "Adopted"), (GRIS, "Rejected")])
    og.carte("og-referendum-promesse.jpg",
             ["%s référendums" % a["N"].capitalize(), "depuis 1958"],
             "Référendums nationaux ; aucun depuis le %s." % a["dernier"],
             "Conseil constitutionnel, arrêté au %s · CC BY 4.0" % a["arrete"],
             "stephane-lalut.com/un-president-peut-il-recourir-au-referendum/",
             lambda d: frise(d, reg),
             [(og.C1, "Adopté"), (GRIS, "Rejeté")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
