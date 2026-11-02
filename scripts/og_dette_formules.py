#!/usr/bin/env python3
"""Carte de partage et vignette d'index de la page « Que valent les formules du débat sur la dette ? » (02/11/2026).

Même fabrique que les cartes du dossier Dette (og_dossier_dette.carte). Les valeurs sont LUES dans data/dette_formules.json
(scripts/update_dette_formules.py). Le dessin reprend la seconde figure de la page : l'écart mensuel entre les taux à dix
ans de la France et de la Grèce, qui change de signe à l'été 2025. Le contraste annoncé (Grèce au-dessus avant, France
au-dessus le mois de la séance) est recontrôlé ici : s'il n'est plus vrai, la carte n'est pas dessinée.
Écrit : static/images/{og,vig}-dette-formules{,-en}.jpg.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402


def barres(d, ecart: dict, lang: str = "fr") -> None:
    mois = sorted(ecart)
    x0, x1, top, bas = 660, 1126, 120, 420
    vmin, vmax = -0.7, 0.3
    bw = (x1 - x0) / len(mois)
    Y = lambda v: top + (bas - top) * (vmax - v) / (vmax - vmin)  # noqa: E731
    for g in (-0.6, -0.4, -0.2, 0.2):
        d.line([(x0, Y(g)), (x1, Y(g))], fill=og.GRID, width=1)
    for i, m in enumerate(mois):
        v = ecart[m]
        ya, yb = sorted((Y(0), Y(v)))
        d.rectangle([x0 + bw * i + 2, ya, x0 + bw * (i + 1) - 2, max(yb, ya + 2)], fill=og.C2 if v > 0 else (201, 197, 192))
    d.line([(x0, Y(0)), (x1, Y(0))], fill=og.INK, width=2)
    i_s = mois.index("2025-09")
    xs = x0 + bw * (i_s + 0.5)
    for y in range(top - 10, bas, 12):
        d.line([(xs, y), (xs, y + 6)], fill=og.INK, width=2)
    fa = og.font("inter", 18, 500)
    for a in ("2024", "2025", "2026"):
        i = mois.index(a + "-01")
        d.text((x0 + bw * i, bas + 14), a, font=fa, fill=og.URL_GREY)
    en = lang == "en"
    fl = og.font("inter", 17, 400)
    d.text((x0, bas + 40), "Ten-year yield, France minus Greece, monthly," if en else "Taux à dix ans, France moins Grèce, par mois,", font=fl, fill=og.URL_GREY)
    d.text((x0, bas + 62), "in points; dotted line: the debate" if en else "en point ; pointillé : la séance", font=fl, fill=og.URL_GREY)


def main() -> int:
    f = og.ROOT / "data" / "dette_formules.json"
    if not f.is_file():
        og.fail("jeu absent : %s — lancer scripts/update_dette_formules.py d'abord" % f)
    j = json.loads(f.read_text(encoding="utf-8"))
    e = j["F8"]["ecart_france_grece_mensuel"]
    if not (e["2024-01"] < 0 and e["2025-09"] > 0):
        og.fail("carte : le contraste annonce n'est plus vrai (janvier 2024 %s, septembre 2025 %s)" % (e["2024-01"], e["2025-09"]))
    A, E = j["affichage"], j["affichage_en"]
    og.carte("og-dette-formules.jpg",
             ["Onze formules du débat", "sur la dette, à l'épreuve"],
             "Le verdict dépend de la question. Le 8 septembre 2025, taux à dix ans : France %s %%, Grèce %s %%." % (A["f8_tec8"], A["f8_hdat8"]),
             "Assemblée nationale, Eurostat, Insee · CC BY 4.0",
             "stephane-lalut.com/formules-du-debat-sur-la-dette/",
             lambda d: barres(d, e),
             [(og.C2, "France au-dessus de la Grèce"), ((201, 197, 192), "Grèce au-dessus")])
    og.carte("og-dette-formules-en.jpg",
             ["Eleven claims from the", "French debt debate, tested"],
             "The verdict depends on the question. On 8 September 2025, ten-year yields: France %s%%, Greece %s%%." % (E["f8_tec8"], E["f8_hdat8"]),
             "French National Assembly, Eurostat, Insee · CC BY 4.0",
             "stephane-lalut.com/en/public-debt-debate-claims/",
             lambda d: barres(d, e, "en"),
             [(og.C2, "France above Greece"), ((201, 197, 192), "Greece above")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
