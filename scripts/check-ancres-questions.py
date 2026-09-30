#!/usr/bin/env python3
"""Controle : toute section-question porte un identifiant d'ancre FIGE.

REGLE (arbitrage GEO-PLUS, 2026-09-29/30 ; registre des decisions, ref. A3, dans
D:\\PRO\\06_PROMOTION\\ARBITRAGE_CONTRE_EXPERTISE_GEO-PLUS_2026-09-29.md). Une question se
traite par defaut en SECTION ANCREE d'une page mere, pas par une URL nouvelle. L'ancre
devient donc ce que les liens, les partages et les citations visent. Sans identifiant
explicite, Hugo le tire du LIBELLE : une reecriture du titre (passes MAGNIFIER) change
l'ancre et casse, sans aucun message, tout ce qui pointait vers la section.

Mesure fondatrice (30/09) : 0 titre-question sur 13 avait un identifiant fige. Les 12
publies ont ete figes a leur valeur de l'epoque (relevee dans le HTML construit), pour
qu'aucun lien existant ne casse.

Perimetre : les lignes `## ...` de content/**/*.md dont le libelle finit par « ? », hors
blocs de code. Une page en brouillon (`draft: true`) est EXEMPTEE et comptee : la regle
mord a sa publication, la ou elle compte. Controle aussi l'unicite des identifiants
dans un meme fichier.

Remede quand il echoue : ajouter ` {#identifiant}` en fin de titre. Pour un titre deja
publie, reprendre l'identifiant que la page porte aujourd'hui (voir le HTML), jamais en
inventer un autre.

Sortie console ASCII pur (console Windows cp1252). Condition de mort : aucune -- regle
permanente ; a reexaminer si l'architecture « section ancree par defaut » est abandonnee.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TITRE = re.compile(r"^##\s+(.*?)\s*$")
ANCRE = re.compile(r"\{#([^}\s]+)\}\s*$")
FIN_QUESTION = re.compile(r"\?\s*(\{#[^}]*\})?\s*$")


def est_brouillon(texte: str) -> bool:
    if not texte.startswith("---"):
        return False
    fin = texte.find("\n---", 3)
    fm = texte[3:fin] if fin > 0 else ""
    return re.search(r"^draft:\s*true\s*$", fm, re.M) is not None


def main() -> int:
    fautes: list[str] = []
    exemptes: list[str] = []
    vus = 0
    for p in sorted(CONTENT.rglob("*.md")):
        texte = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT).as_posix()
        brouillon = est_brouillon(texte)
        dans_code = False
        ids: dict[str, int] = {}
        for n, ligne in enumerate(texte.splitlines(), 1):
            if ligne.lstrip().startswith("```"):
                dans_code = not dans_code
                continue
            if dans_code:
                continue
            m = TITRE.match(ligne)
            if not m:
                continue
            libelle = m.group(1).replace("&nbsp;", " ")
            a = ANCRE.search(libelle)
            if a:
                if a.group(1) in ids:
                    fautes.append(f"{rel}:{n} identifiant '{a.group(1)}' deja pris ligne {ids[a.group(1)]}")
                ids[a.group(1)] = n
            if not FIN_QUESTION.search(libelle):
                continue
            vus += 1
            if a:
                continue
            if brouillon:
                exemptes.append(f"{rel}:{n}")
            else:
                fautes.append(f"{rel}:{n} titre-question sans identifiant fige {{#...}}")
    for e in exemptes:
        print(f"  exempte (brouillon) : {e}")
    for f in fautes:
        print(f"  ECHEC {f}")
    if fautes:
        print(f"Ancres des questions : {len(fautes)} faute(s) sur {vus} titre(s)-question. ECHEC")
        return 1
    print(f"Ancres des questions : {vus} titre(s)-question, tous figes"
          f"{f' ({len(exemptes)} brouillon(s) exempte(s))' if exemptes else ''}. OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
