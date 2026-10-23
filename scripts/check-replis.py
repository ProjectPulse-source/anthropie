#!/usr/bin/env python3
"""Controle : tout bloc depliable du site porte la ligne « Lire le detail » (regle constante de l'auteur, 2026-10-23).

REGLE (CLAUDE.md du site, « Production des ressources », gabarit) : toute partie qui se deplie, sur toute page, dit
qu'elle se deplie et ce qu'on y gagne (« Lire le detail · 2 paragraphes, 1 tableau ▾ »). Un seul organe la pose :
static/js/replis-action.js, sur TOUT <details>, y compris ceux qu'un script construit apres le chargement.
Cas fondateur : la fiche de commune de /budget-2027-votre-commune/ (replis construits par fiche-commune.js, hors de la
classe .repli, sur une condition de chargement qui ne voyait que le Markdown) n'avait pas la ligne.

Ce que ce controle verifie, parce que chacun de ces defauts passe en silence (sortie 0, aucune erreur console) :
  1. layouts/partials/head.html charge replis-action.js sans condition (une condition sur .Content manque les replis
     des gabarits et des scripts) ;
  2. replis-action.js vise tout <details>, et non une classe ;
  3. l'exemption data-repli="nav" (blocs de navigation : ils ouvrent des liens, pas un detail) ne se trouve que dans
     la liste fermee NAV ci-dessous ; l'etendre se decide ici, avec son motif.
Condition de mort : aucune -- regle permanente du gabarit ; a reexaminer si replis-action.js est remplace.
Sortie console ASCII pur.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEAD = ROOT / "layouts" / "partials" / "head.html"
JS = ROOT / "static" / "js" / "replis-action.js"
# Liste fermee des blocs de navigation exemptes (fichier -> motif).
NAV = {
    "layouts/partials/sommaire-ressource.html": "sommaire de page : liens vers les sections",
    "layouts/partials/dossier-barre.html": "menu du dossier : liens vers les autres volets",
}


def main() -> int:
    ecarts = []
    lignes = HEAD.read_text(encoding="utf-8").splitlines()
    charge = [l for l in lignes if "replis-action.js" in l and "<script" in l]
    if not charge:
        ecarts.append("head.html : replis-action.js n'est pas charge")
    elif any("{{ if" in l or "{{- if" in l for l in charge):
        ecarts.append("head.html : replis-action.js charge sous condition (doit l'etre sur toute page)")
    js = JS.read_text(encoding="utf-8")
    if 'querySelectorAll("details")' not in js or re.search(r'querySelectorAll\("details\.', js):
        ecarts.append("replis-action.js : ne vise pas tout <details>")
    vus = 0
    for base in ("layouts", "content", "static/js"):
        for f in (ROOT / base).rglob("*"):
            if not f.is_file() or f.suffix not in (".html", ".md", ".js"):
                continue
            rel = f.relative_to(ROOT).as_posix()
            if rel == "static/js/replis-action.js":
                continue
            n = len(re.findall(r'data-repli=["\\]*nav', f.read_text(encoding="utf-8", errors="replace")))
            vus += n
            if n and rel not in NAV:
                ecarts.append("%s : exemption data-repli=nav hors de la liste fermee NAV" % rel)
    print("check-replis : %d exemption(s) de navigation vue(s), %d attendue(s) au moins" % (vus, len(NAV)))
    if vus < len(NAV):
        ecarts.append("exemptions de navigation manquantes : les menus recevraient une ligne « Lire le detail »")
    for e in ecarts:
        print("  ECART " + e)
    print("check-replis : %s" % ("OK" if not ecarts else "%d ecart(s)" % len(ecarts)))
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main())
