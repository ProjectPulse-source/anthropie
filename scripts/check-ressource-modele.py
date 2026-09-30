#!/usr/bin/env python3
"""Controle : toute RESSOURCE DE DONNEES suit le modele du dossier dette (auteur, 2026-09-30).

REGLE (CLAUDE.md du site, section « Modele d'une ressource de donnees ») : le dossier dette publique -- quatre volets
refaits le 30/09 sur quatre contre-expertises -- sert de modele de structure et de methode a toute ressource de
donnees. Ce controle ne verifie que ce qui se verifie MECANIQUEMENT ; le reste (ordre de lecture, formulations,
contre-expertise) est une discipline ecrite dans le CLAUDE.md, pas un verrou.

Perimetre : les fichiers content/**/*.md dont le front matter declare `donnees:` (une page qui publie des chiffres
tires d'un jeu data/<jeu>.json). Brouillons exemptes et comptes. Pour chaque page :
  1. une carte de partage propre (`og_image:`), jamais la carte generique du site ;
  2. un « resultat en une phrase » (bloc .resultat-phrase) ;
  3. le bloc commun « Reutiliser cette page » ({{< reutiliser ... >}}) ;
  4. un balisage Dataset (`dataset:` ou `dataset_dette: true`) ;
  5. chaque jeu declare publie son JSON ET son CSV dans static/ ;
  6. si la page appelle le livre ({{< appel-livre ...), sans note Amazon (`avis="non"`) : une ressource n'est pas
     une fiche produit.
Conservation : pages vues == conformes + en defaut + brouillons exemptes.

Condition de mort : aucune -- regle permanente du modele ; a reexaminer si le modele est abandonne ou refondu.
Sortie console ASCII pur.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"


def front_matter(texte: str) -> str:
    if not texte.startswith("---"):
        return ""
    fin = texte.find("\n---", 3)
    return texte[3:fin] if fin > 0 else ""


def jeux(fm: str) -> list[str]:
    m = re.search(r"^donnees:\s*\[([^\]]*)\]", fm, re.M)
    return [j.strip().strip("'\"") for j in m.group(1).split(",") if j.strip()] if m else []


def main() -> int:
    vues, conformes, brouillons, fautes = 0, 0, 0, []
    for p in sorted(CONTENT.rglob("*.md")):
        texte = p.read_text(encoding="utf-8")
        fm = front_matter(texte)
        if not re.search(r"^donnees:", fm, re.M):
            continue
        vues += 1
        rel = p.relative_to(ROOT).as_posix()
        if re.search(r"^draft:\s*true\s*$", fm, re.M):
            brouillons += 1
            continue
        corps = texte[len(fm) + 6:]
        f = []
        if not re.search(r"^og_image:\s*\S", fm, re.M):
            f.append("pas de carte de partage propre (og_image)")
        if 'class="resultat-phrase"' not in corps:
            f.append("pas de 'resultat en une phrase' (div.resultat-phrase)")
        if "{{< reutiliser " not in corps:
            f.append("pas de bloc 'Reutiliser cette page'")
        if not (re.search(r"^dataset:", fm, re.M) or re.search(r"^dataset_dette:\s*true", fm, re.M)):
            f.append("pas de balisage Dataset (dataset: ou dataset_dette: true)")
        for j in jeux(fm):
            for ext in ("json", "csv"):
                if not (STATIC / ("%s.%s" % (j, ext))).is_file():
                    f.append("jeu %s : static/%s.%s absent" % (j, j, ext))
        for m in re.finditer(r"\{\{< appel-livre [^>]*>\}\}", corps):
            if 'avis="non"' not in m.group(0):
                f.append("appel-livre sans avis=\"non\" (note Amazon sur une ressource)")
        if f:
            fautes.append((rel, f))
        else:
            conformes += 1
    assert vues == conformes + len(fautes) + brouillons, "conservation rompue"
    for rel, f in fautes:
        for x in f:
            print("  ECART  %s : %s" % (rel, x))
    if fautes:
        print("Modele des ressources : %d page(s) en ecart sur %d (brouillons exemptes : %d)." % (len(fautes), vues, brouillons))
        print("  -> voir CLAUDE.md du site, section Modele d'une ressource de donnees.")
        return 1
    print("Modele des ressources : %d/%d page(s) de donnees conformes (brouillons exemptes : %d). OK" % (conformes, vues, brouillons))
    return 0


if __name__ == "__main__":
    sys.exit(main())
