#!/usr/bin/env python3
"""Garde de transition : l'image des runners GitHub est-elle encore maitrisee ?

POURQUOI. GitHub fait migrer le label `ubuntu-latest` vers Ubuntu 26.04 « over a
period of several weeks beginning October 19, 2026 [...] complete the migration by
November 19, 2026 » (actions/runner-images#14748, lu a la source le 2026-09-29).
Pendant cette fenetre, un meme workflow peut tomber un jour sur Ubuntu 24.04 et le
lendemain sur 26.04, SANS aucun changement de code : un echec intermittent, qu'on
attribue alors a la donnee, au reseau ou au hasard. C'est la classe « etat declare
!= etat reel » appliquee a l'infrastructure.

Le depot a donc epingle ses runners. Ce controle verifie que l'epinglage TIENT, et
rappelle l'echeance -- il ne bloque pas le deploiement (hors `--ci`, comme
check-png-dette.py) : une image a migrer n'est pas une raison de ne plus publier.

CONDITION DE MORT, en predicat verifiable et non en date : ce fichier se SUPPRIME,
avec sa ligne dans check-all.py, le jour ou tous les workflows portent une image
>= 26.04 et ou un run vert l'a constate. Il l'annonce lui-meme quand c'est le cas.
Tant qu'il vit, c'est qu'il reste quelque chose a faire.

Sortie : 0 si l'epinglage tient (avec ou sans rappel), 1 si un workflow est revenu
a un label flottant alors que la fenetre est ouverte.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / ".github" / "workflows"

# Dates lues a la source (issue 14748), pas deduites d'une annonce de tiers.
DEBUT = date(2026, 10, 19)
FIN = date(2026, 11, 19)
CIBLE = "ubuntu-26.04"          # ce vers quoi il faut arriver
EPINGLE = "ubuntu-24.04"        # ce qui est fige en attendant
# Banc de test deja passe au VERT sur la cible (run 36545145119) : Ubuntu 26.04.1,
# Python 3.14.4, glibc 2.43, Hugo Extended par dpkg, build, gardes du script et porte
# bloquante -- tout passe. La migration ne coutera donc rien. Reste a la faire quand
# l'image cible aura fini de bouger, c'est-a-dire apres la fin de la bascule.
DERNIER_TEST_VERT = date(2026, 9, 29)

# Le motif s'arrete au premier blanc ou au premier « # » : une ligne epinglee porte
# un commentaire de renvoi, et un motif ancre sur la fin de ligne ne l'aurait pas vue.
# Defaut commis puis constate ici meme le 2026-09-29, a la premiere execution : le
# controle comptait 1 declaration sur 8 et annoncait « MIGRATION TERMINEE ». Un
# controle textuel a un VOCABULAIRE, et ce vocabulaire est un filtre au meme titre
# qu'un glob de fichiers -- la lecon du meme jour sur check-corpus-counters.py.
RUNS_ON = re.compile(r"^\s*runs-on:\s*([^\s#]+)", re.M)


def main() -> int:
    if not WORKFLOWS.is_dir():
        print("aucun dossier .github/workflows -- controle sans objet")
        return 0

    flottants: list[tuple[str, int, str]] = []
    epingles = 0
    cibles = 0
    autres: list[tuple[str, int, str]] = []

    for f in sorted(WORKFLOWS.glob("*.yml")) + sorted(WORKFLOWS.glob("*.yaml")):
        texte = f.read_text(encoding="utf-8")
        for m in RUNS_ON.finditer(texte):
            label = m.group(1).strip().strip('"\'')
            ligne = texte[: m.start()].count("\n") + 1
            if label.endswith("-latest"):
                flottants.append((f.name, ligne, label))
            elif label == EPINGLE:
                epingles += 1
            elif label == CIBLE:
                cibles += 1
            else:
                autres.append((f.name, ligne, label))

    total = epingles + cibles + len(flottants) + len(autres)
    aujourdhui = date.today()
    print("Runners : %d declaration(s) runs-on -- %d sur %s, %d sur %s, %d flottante(s)"
          % (total, epingles, EPINGLE, cibles, CIBLE, len(flottants)))
    for nom, ligne, label in autres:
        print("  info : %s:%d porte %s (ni l'un ni l'autre)" % (nom, ligne, label))

    # -- la condition de mort, annoncee par le controle lui-meme
    if total and not flottants and not epingles and not autres:
        print("\nMIGRATION TERMINEE : tous les runners sont sur %s." % CIBLE)
        print("Ce controle a fini son office -- SUPPRIMER scripts/check-runner-image.py")
        print("et sa ligne dans scripts/check-all.py (LOCAL_DERIVES).")
        return 0

    if flottants:
        print("\nATTENTION : %d declaration(s) revenue(s) a un label flottant."
              % len(flottants))
        for nom, ligne, label in flottants:
            print("  %s:%d  runs-on: %s" % (nom, ligne, label))
        if aujourdhui >= DEBUT:
            print("\nLa fenetre de migration est OUVERTE depuis le %s : un label flottant"
                  % DEBUT.isoformat())
            print("peut changer d'image d'un run a l'autre, donc produire un echec")
            print("intermittent qu'on attribuera a autre chose. Epingler %s ou %s."
                  % (EPINGLE, CIBLE))
            return 1
        print("Epingler avant le %s (debut de la bascule)." % DEBUT.isoformat())
        return 1

    # -- rappel d'echeance, proportionne au temps qui reste
    jours_test = (aujourdhui - DERNIER_TEST_VERT).days
    if aujourdhui > FIN:
        print("\nA FAIRE : la bascule GitHub est achevee depuis le %s." % FIN.isoformat())
        print("C'est le moment prevu pour migrer. Relancer le banc puis basculer :")
        print("  gh workflow run test-runner-ubuntu26.yml")
        print("  puis remplacer %s par %s dans les 9 declarations (7 ici, 2 dans"
              % (EPINGLE, CIBLE))
        print("  le depot monitoring), et SUPPRIMER banc, garde et dossier.")
        print("Le dernier banc vert date de %s, soit %d jours : le refaire, l'image"
              % (DERNIER_TEST_VERT.isoformat(), jours_test))
        print("cible a bouge depuis.")
    elif aujourdhui >= DEBUT:
        print("\nBascule GitHub EN COURS (%s -> %s) ; l'epinglage protege."
              % (DEBUT.isoformat(), FIN.isoformat()))
        print("Rien a faire avant la fin : migrer pendant que l'image cible bouge")
        print("encore echangerait un risque nul contre un risque inconnu.")
    else:
        print("\nBascule GitHub du %s au %s, dans %d jours -- l'epinglage protege."
              % (DEBUT.isoformat(), FIN.isoformat(), (DEBUT - aujourdhui).days))
        print("Banc de test deja VERT sur %s le %s : la migration ne coutera rien."
              % (CIBLE, DERNIER_TEST_VERT.isoformat()))
        print("Elle se fera APRES le %s, quand l'image cible aura fini de bouger."
              % FIN.isoformat())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
