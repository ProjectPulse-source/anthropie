#!/usr/bin/env python3
"""Les PNG des figures de la dette sont-ils encore ceux de leurs SVG ?

MOTIF (2026-09-21, reecrit le meme jour). Les SVG sont regeneres chaque semaine
par la chaine INSEE / Eurostat, en CI, et depuis ce jour la CI rend aussi les
PNG. Mais elle le fait par une etape DELIBEREMENT non bloquante : l'installation
de la bibliotheque de rendu porte `continue-on-error`, parce que faire dependre
la mise a jour des DONNEES d'une bibliotheque d'images suspendrait l'essentiel a
l'accessoire. Cette tolerance a un prix, et c'est lui que ce controle guette :
le jour ou l'installation echoue, le script l'annonce, poursuit, et publie des
SVG neufs a cote de PNG anciens -- sans erreur, sans echec de workflow, et en
continuant d'offrir les PNG au telechargement. Une figure fausse qui circule est
exactement le defaut vise.

Il ne compare pas des images : il compare l'EMPREINTE DU SVG SOURCE au moment
ou le PNG a ete produit (data/png_dette_source.json) a celle du SVG courant.
Deux rendus du meme SVG peuvent differer d'une version de cairo ou d'un jeu de
polices a l'autre ; la source, elle, ne ment pas.

CONDITION DE MORT (R2), en predicat et non en date : ce controle disparait le
jour ou le rendu des PNG cesse de pouvoir echouer separement de la publication
des donnees -- soit qu'il devienne bloquant, soit qu'il n'ait plus de dependance
a installer. Il n'y a alors plus de divergence possible, donc plus rien a
surveiller.

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
