#!/usr/bin/env python3
"""Carte de partage et vignette d'index du prolongement « Europe » (dossier Promesses).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Tout est LU dans data/promesses_europe.json
(scripts/update_promesses_europe.py) : votes contre et abstentions des États au Conseil, France en bleu.
Écrit : static/images/og-europe-promesse(-en).jpg et vig-europe-promesse(-en).jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402

GRIS = (82, 81, 78)
GRIS_CLAIR = (201, 205, 211)


def barres(d, etats: list, lang: str = "fr") -> None:
    x0, y0, wmax = 830, 120, 270
    vmax = max(int(c) + int(a) for _, c, a, _ in etats)
    sel = sorted(etats, key=lambda e: -(int(e[1]) + int(e[2])))[:8]
    sel += [e for e in etats if e[0] in ("France",) and e not in sel]
    f = og.font("inter", 16, 400)
    fb = og.font("inter", 16, 600)
    for k, (nom, c, a, _) in enumerate(sel):
        y = y0 + k * 30
        estfr = nom == "France"
        wc, wa = wmax * int(c) / vmax, wmax * int(a) / vmax
        d.text((x0 - 12 - d.textlength(nom, font=fb if estfr else f), y), nom, font=fb if estfr else f, fill=og.INK)
        d.rectangle([x0, y + 2, x0 + max(wc, 1), y + 20], fill=og.C1 if estfr else GRIS)
        d.rectangle([x0 + wc, y + 2, x0 + wc + max(wa, 1), y + 20], fill=(157, 181, 216) if estfr else GRIS_CLAIR)
        s = "%s · %s" % (c, a)
        d.text((x0 + wc + wa + 8, y), s, font=fb if estfr else f, fill=og.INK if estfr else og.GREY)


def main() -> int:
    f = og.ROOT / "data" / "promesses_europe.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_promesses_europe.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    v = j["calcul"]["votes"]
    a, e = j["affichage"], j["affichage_en"]
    fr = [l for l in j["tableaux"]["etats"]["lignes"] if l[0] == "France"][0]
    if (int(fr[1]), int(fr[2])) != (v["fr_contre"], v["fr_abst"]):
        og.fail("carte : tableau et calcul divergent pour la France")
    og.carte("og-europe-promesse-en.jpg",
             ["France in the", "EU Council"],
             "Public votes on legislative acts, %s-%s." % (e["debut"][-4:], e["fin"][-4:]),
             "Council of the EU · SWP/GESIS · CC BY 4.0",
             "stephane-lalut.com/en/what-can-france-decide-in-the-european-union/",
             lambda d: barres(d, [[r[0]] + r[1:] for r in j["tableaux_en"]["etats"]["lignes"]], "en"),
             [(GRIS, "Votes against"), (GRIS_CLAIR, "Abstentions (count after each bar)")])
    og.carte("og-europe-promesse.jpg",
             ["La France au", "Conseil de l'UE"],
             "Votes publics sur des actes législatifs, %s-%s." % (a["debut"][-4:], a["fin"][-4:]),
             "Conseil de l'UE · SWP/GESIS · CC BY 4.0",
             "stephane-lalut.com/ce-que-la-france-peut-decider-dans-l-union-europeenne/",
             lambda d: barres(d, j["tableaux"]["etats"]["lignes"]),
             [(GRIS, "Votes contre"), (GRIS_CLAIR, "Abstentions (nombres après la barre)")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
