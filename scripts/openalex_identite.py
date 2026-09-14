# -*- coding: utf-8 -*-
"""Inventaire des entites auteur OpenAlex, et liste des DOI a rattacher a l'ancre.

POURQUOI CET OUTIL EXISTE
OpenAlex cree une entite auteur par variante de signature : le corpus s'y trouve
disperse sur une dizaine de fiches au lieu d'une, et le defaut s'aggrave a chaque
depot (9 entites le 2026-08-22, 10 le 2026-09-13). Il n'existe AUCUNE fonction
"fusionner" : on revendique une entite (Claim), puis on lui rattache les travaux
des autres, un par un, par DOI. Le geste est donc bloque tant que la liste exacte
des DOI n'existe pas -- elle n'existait pas avant le 2026-09-14, et c'est ce qui
laissait la tache ouverte depuis trois semaines.

L'ANCRE NE SE CHOISIT PAS A LA MAIN : c'est l'entite qui porte l'ORCID. Une
checklist anterieure nommait A5130851063, qui ne porte ni l'ORCID ni la majorite
des travaux ; ancrer dessus aurait fixe l'identite sur une entite minoritaire.

CONDITION DE MORT (doctrine R2) : cet outil disparait quand une execution rend
"A RATTACHER : 0" deux fois de suite a un mois d'intervalle -- l'identite est
alors unifiee et OpenAlex n'eclate plus les nouveaux depots. Il ne s'agit pas
d'un controle permanent : il ne tourne que sur demande, avant un geste d'auteur.

USAGE
    python scripts/openalex_identite.py [fichier_sortie.txt]
    OPENALEX_MAILTO=<adresse>  (facultatif : "polite pool" OpenAlex, plus rapide)

L'API est publique ; aucune authentification, aucun secret.
"""
import io
import json
import os
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

ORCID = "0009-0002-1794-4895"
# Entites relevees le 2026-08-22 (audits/diagnostic-compare-2026-08-22.md) plus
# celle apparue au 2026-09-13. Une entite fusionnee par OpenAlex redirige : le
# script suit la redirection et affiche l'ecart.
CONNUES = [
    "A5130851063", "A5133048122", "A5134537460", "A5143515672", "A5130783250",
    "A5132995417", "A5133063046", "A5135611613", "A5135698507", "A5135768240",
]
# Homonyme au statut incertain : ne JAMAIS revendiquer (PROJECT_STATUS, 2026-09-13).
EXCLUS = {"A5138641837"}

_mail = os.environ.get("OPENALEX_MAILTO", "").strip()
UA = {"User-Agent": "anthropie-site/1.0" + ((" (mailto:" + _mail + ")") if _mail else "")}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read())


def main():
    ancre = get("https://api.openalex.org/authors/https://orcid.org/" + ORCID)
    ancre_id = ancre["id"].rsplit("/", 1)[1]
    print("ANCRE (porte l'ORCID) : %s -- %s -- %d travaux"
          % (ancre_id, ancre["display_name"], ancre["works_count"]))
    print("")

    travaux = {}
    entites = []
    for aid in CONNUES:
        if aid in EXCLUS:
            continue
        try:
            a = get("https://api.openalex.org/authors/" + aid)
        except Exception as e:                      # entite supprimee, reseau, quota
            print("  %s : INTERROGATION IMPOSSIBLE (%s)" % (aid, e))
            continue
        reel = a["id"].rsplit("/", 1)[1]
        entites.append((aid, reel, a["display_name"], a["works_count"]))
        cursor = "*"
        while cursor:
            d = get("https://api.openalex.org/works?filter=author.id:" + reel
                    + "&per-page=200&cursor=" + cursor)
            for w in d["results"]:
                doi = (w.get("doi") or "").replace("https://doi.org/", "")
                e = travaux.setdefault(doi or w["id"],
                                       {"titre": w.get("title") or "",
                                        "annee": w.get("publication_year"),
                                        "entites": set()})
                e["entites"].add(reel)
            cursor = d["meta"].get("next_cursor")
            time.sleep(0.2)

    print("ENTITES INTERROGEES")
    for aid, reel, nom, n in entites:
        red = "" if aid == reel else ("  -> redirige vers " + reel)
        print("  %-12s %-22s %3d travaux%s%s"
              % (aid, nom[:22], n, red, "  <= ANCRE" if reel == ancre_id else ""))

    a_rattacher = {k: v for k, v in travaux.items() if ancre_id not in v["entites"]}
    print("")
    print("TOTAL travaux distincts : %d" % len(travaux))
    print("  deja sur l'ancre      : %d" % (len(travaux) - len(a_rattacher)))
    print("  A RATTACHER           : %d" % len(a_rattacher))
    print("")
    print("DOI A RATTACHER A " + ancre_id)
    ordre = sorted(a_rattacher, key=lambda x: (a_rattacher[x]["annee"] or 0, x))
    for k in ordre:
        v = a_rattacher[k]
        print("  %s  (%s)  %s" % (k, v["annee"], v["titre"][:62]))

    if len(sys.argv) > 1:
        with io.open(sys.argv[1], "w", encoding="utf-8") as fh:
            for k in ordre:
                fh.write(k + "\n")
        print("")
        print("Liste brute ecrite : " + sys.argv[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
