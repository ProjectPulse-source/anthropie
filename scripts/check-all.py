#!/usr/bin/env python3
"""Runner des controles de coherence du site -- un seul geste, une seule sortie.

MOTIF (2026-09-02). Les controles existaient en cinq scripts que chaque checklist
enumerait ; on en oubliait toujours un. Ce runner les lance tous et rend UN verdict.
Il n'ajoute aucune regle : c'est un organe de plus pour les memes lois, pas une copie.

  --ci      : les controles HORS RESEAU seulement (compteurs de corpus, parite registre
              <-> fiches, encodage console) -- porte bloquante de .github/workflows/hugo.yml.
  --reseau  : ajoute les controles qui interrogent l'exterieur (Wikidata <-> registre,
              sondage des noeuds externes). A lancer en local a chaque cloture.
  (defaut)  : hors reseau + couverture GEO (lit content/, sans reseau).

Sortie 0 = tout est a 0 ; 1 = au moins un controle en echec ; 2 = aucun echec mais au
moins un controle n'a rien pu conclure (reseau injoignable) -- a relancer, pas a ignorer.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

HORS_RESEAU = [
    ("compteurs de corpus", "check-corpus-counters.py", []),
    ("parite registre <-> fiches", "check-fiches-registre.py", []),
    ("encodage console des scripts", "check-console-encoding.py", []),
]
LOCAL = [
    ("couverture GEO FR/EN", "check-geo-coverage.py", []),
]
RESEAU = [
    ("parite Wikidata <-> registre", "check-wikidata-registre.py", []),
    ("sondage des noeuds externes", "sondage-noeuds-externes.py", []),
]


def run(nom: str, script: str, args: list[str]) -> int:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPTS / script), *args], cwd=ROOT, env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    sortie = (r.stdout or "").strip().splitlines()
    derniere = sortie[-1] if sortie else (r.stderr or "").strip().splitlines()[-1:] or [""]
    if isinstance(derniere, list):
        derniere = derniere[0] if derniere else ""
    etat = {0: "OK", 2: "NON CONCLU"}.get(r.returncode, "ECHEC")
    print(f"  [{etat:10s}] {nom:32s} {script}  --  {derniere[:90]}")
    if r.returncode not in (0, 2):
        for line in sortie[-12:]:
            print(f"               {line}")
        if r.stderr and r.stderr.strip():
            print("               stderr: " + r.stderr.strip().splitlines()[-1][:120])
    return r.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ci", action="store_true", help="hors reseau seulement (porte CI)")
    ap.add_argument("--reseau", action="store_true", help="ajoute les controles reseau")
    a = ap.parse_args()
    lots = list(HORS_RESEAU)
    if not a.ci:
        lots += LOCAL
    if a.reseau:
        lots += RESEAU
    print(f"check-all : {len(lots)} controle(s){' (mode CI)' if a.ci else ''}")
    codes = [run(*lot) for lot in lots]
    if any(c not in (0, 2) for c in codes):
        print("\nAu moins un controle en ECHEC : corriger avant de committer.")
        return 1
    if any(c == 2 for c in codes):
        print("\nAucun echec, mais un controle n'a rien pu conclure : relancer quand le reseau repond.")
        return 2
    print("\nTout est a 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
