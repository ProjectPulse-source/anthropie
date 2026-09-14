# -*- coding: utf-8 -*-
"""Compteurs Zenodo des AWP : vues et telechargements uniques, par record.

LA LISTE VIENT DU REGISTRE, PAS D'UNE COPIE EN DUR (correction 2026-09-14).
Jusqu'a ce jour, RECORDS etait un dictionnaire code en dur de CINQ entrees.
AWP-06, AWP-07 et AWP-08 en etaient absents -- et leur absence ne se signalait
pas : le tableau s'arretait, voila tout. Un arbitrage du 2026-09-14 portait
precisement sur AWP-07 et AWP-08 ; l'instrument cense mesurer leur audience ne
les regardait pas. Meme classe que SSRN_SANS_ID dans check_deposits_status.py,
et meme regle que le CLAUDE.md du depot : la presence vient du depot, une
exclusion peut etre legitime mais le silence jamais.

Le registre data/works.yaml porte, pour chaque oeuvre, deposits.zenodo_<lg>.doi.
C'est de la que sort la liste. Ajouter un AWP au registre suffit desormais a le
faire apparaitre ici.

Usage : python scripts/zenodo_stats.py
"""
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML requis : pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
REGISTRE = ROOT / "data" / "works.yaml"


def collecte(noeud, sortie, attendus):
    """Parcourt le registre et releve tout record Zenodo d'une oeuvre AWP."""
    if isinstance(noeud, dict):
        ident = str(noeud.get("id") or "")
        if ident.lower().startswith("awp-"):
            attendus.add(ident.upper())
            depots = noeud.get("deposits") or {}
            for nom, bloc in depots.items():
                if not nom.lower().startswith("zenodo") or not isinstance(bloc, dict):
                    continue
                doi = bloc.get("doi") or ""
                if "zenodo." in doi:
                    sortie.append((ident.upper(),
                                   nom.lower().replace("zenodo_", "").upper(),
                                   doi.rsplit(".", 1)[-1]))
        for valeur in noeud.values():
            collecte(valeur, sortie, attendus)
    elif isinstance(noeud, list):
        for valeur in noeud:
            collecte(valeur, sortie, attendus)


def stats(record_id, essais=3):
    """Compteurs d'un record. Zenodo rend parfois 504 : on reessaie avant de
    conclure, sinon une indisponibilite passagere se lirait comme un zero."""
    req = urllib.request.Request(
        "https://zenodo.org/api/records/%s" % record_id,
        headers={"Accept": "application/json"})
    for essai in range(essais):
        try:
            with urllib.request.urlopen(req, timeout=40) as reponse:
                donnees = json.load(reponse)
            s = donnees.get("stats", {})
            return (s.get("unique_views", 0), s.get("unique_downloads", 0),
                    donnees.get("metadata", {}).get("publication_date", ""), None)
        except Exception as erreur:
            if essai == essais - 1:
                return (None, None, "", str(erreur)[:40])
            time.sleep(3)


records, attendus = [], set()
collecte(yaml.safe_load(REGISTRE.read_text(encoding="utf-8")), records, attendus)
records.sort()

aujourdhui = datetime.date.today()
print("# Stats Zenodo - snapshot %s" % aujourdhui.isoformat())
print("# %d record(s) derive(s) du registre, pour %d AWP connus de lui\n"
      % (len(records), len(attendus)))
print("| AWP | Langue | Record | Publie le | Jours | Vues uniq. | DL uniq. | Vues/j | DL/j |")
print("|-----|--------|--------|-----------|------:|-----------:|---------:|-------:|-----:|")

vus, echecs = set(), []
for awp, langue, rid in records:
    v, d, publie, erreur = stats(rid)
    if erreur is not None:
        echecs.append((awp, langue, rid, erreur))
        print("| %s | %s | %s | — | — | ERREUR | ERREUR | — | — |" % (awp, langue, rid))
        continue
    vus.add(awp)
    try:
        jours = max((aujourdhui - datetime.date.fromisoformat(publie)).days, 1)
        vpj, dpj = "%.2f" % (v / jours), "%.2f" % (d / jours)
    except Exception:
        jours, vpj, dpj = "—", "—", "—"
    print("| %s | %s | %s | %s | %s | %d | %d | %s | %s |"
          % (awp, langue, rid, publie, jours, v, d, vpj, dpj))
    time.sleep(0.3)

# Rendre compte : entre == retenu + ecarte, et l'ecarte porte un motif nomme.
manquants = sorted(attendus - {a for a, _, _ in records})
if manquants:
    print("\n/!\\ AWP connus du registre SANS aucun record Zenodo : %s"
          % ", ".join(manquants))
    print("    Ce n'est pas un zero d'audience : c'est une absence de depot")
    print("    declaree au registre. Verifier avant d'en conclure quoi que ce soit.")
if echecs:
    print("\n/!\\ %d record(s) NON MESURE(S) - l'API a refuse, ce n'est pas un zero :"
          % len(echecs))
    for awp, langue, rid, erreur in echecs:
        print("    %s %s (%s) : %s" % (awp, langue, rid, erreur))
if not manquants and not echecs:
    print("\nTous les AWP du registre ont ete mesures.")
