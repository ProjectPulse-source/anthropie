#!/usr/bin/env python3
"""Les PNG des figures de la dette sont-ils encore ceux de leurs SVG ?

MOTIF (2026-09-21). Les SVG sont regeneres chaque semaine par la chaine INSEE /
Eurostat, en CI. Les PNG, eux, sont derives EN LOCAL : la chaine ne peut pas les
produire sans une dependance graphique, et faire dependre la mise a jour des
DONNEES d'une bibliotheque d'images serait mettre l'essentiel a la merci de
l'accessoire. Consequence : des qu'un chiffre bouge, le SVG suit et le PNG
reste en arriere -- sans rien casser, sans aucune erreur, et en continuant
d'etre propose au telechargement. Une figure fausse qui circule est exactement
le defaut que ce controle guette.

Il ne compare pas des images : il compare l'EMPREINTE DU SVG SOURCE au moment
ou le PNG a ete produit (static/img/_png_source.json) a celle du SVG courant.
Deux rendus du meme SVG peuvent differer d'une version de cairo a l'autre ;
la source, elle, ne ment pas.

CONDITION DE MORT (R2), en predicat et non en date : ce controle disparait le
jour ou les PNG sont produits dans la meme execution que les SVG -- c'est-a-dire
le jour ou la chaine de production sait rendre une image. Il n'y a alors plus
de derive possible, donc plus rien a surveiller.

Sortie 0 = a jour ; 1 = au moins un PNG perime ou orphelin ; 2 = rien a
conclure (manifeste absent : les PNG n'ont jamais ete produits).
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "static" / "img"
MANIFESTE = ROOT / "data" / "png_dette_source.json"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    if not MANIFESTE.is_file():
        print("Aucun PNG derive (manifeste absent) : rien a conclure.")
        return 2

    ref = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    entrees = ref.get("sources", {})
    if not entrees:
        print("Manifeste vide : rien a conclure.")
        return 2

    perimes, orphelins, ok = [], [], 0
    for nom_png, sha_svg in sorted(entrees.items()):
        png = IMG / nom_png
        svg = IMG / (Path(nom_png).stem + ".svg")
        if not png.is_file():
            orphelins.append("%s : PNG absent" % nom_png)
            continue
        if not svg.is_file():
            orphelins.append("%s : SVG source absent" % svg.name)
            continue
        if sha(svg) != sha_svg:
            perimes.append(nom_png)
        else:
            ok += 1

    # Conservation : tout ce qui entre ressort classe, et l'ecarte porte un motif.
    total = len(entrees)
    assert total == ok + len(perimes) + len(orphelins), "conservation rompue"

    for m in orphelins:
        print("  ORPHELIN  " + m)
    for m in perimes:
        print("  PERIME    %s : son SVG a change depuis le rendu" % m)

    if perimes or orphelins:
        print("%d PNG a jour, %d perime(s), %d orphelin(s) sur %d."
              % (ok, len(perimes), len(orphelins), total))
        print("  -> relancer : python scripts/update_dette_insee.py --png")
        return 1

    print("PNG des figures : %d/%d a jour avec leur SVG. OK" % (ok, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
