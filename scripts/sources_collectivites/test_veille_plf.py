# -*- coding: utf-8 -*-
"""Essais de l'extracteur de veille_plf.py sur des formules du compte rendu officiel (05/11/2026).
Une formule connue s'integre ; une formule inconnue autour d'un article suivi devient un ticket, jamais une entree ;
un article d'un autre texte (hors troncon du projet de loi de finances) ne compte pas."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import veille_plf as V  # noqa: E402

TETE = "2. Projet de loi de finances pour 2027 Seconde partie (suite) "
FIN = " 3. Ordre du jour de la prochaine séance Prochaine séance, demain, à neuf heures : Suite de la discussion de la seconde partie du projet de loi de finances pour 2027. La séance est levée."


def essai(corps, suivis={84, 34}):
    return V.extraire("Sommaire " + TETE + "Ordre du jour de la prochaine séance " + TETE + corps + FIN, set(suivis), 2027)


def main():
    echecs = []

    def ok(cond, nom):
        if not cond:
            echecs.append(nom)

    r = essai("Je mets aux voix les amendements de suppression. (L’article 84 est supprimé.)")
    ok([(a["article"], a["statut"]) for a in r["articles"]] == [(84, "supprime")], "suppression")
    ok(r["articles"][0]["citation"] == "(L’article 84 est supprimé.)", "citation verbatim")
    r = essai("(L’article 84, amendé, est adopté.)")
    ok([(a["article"], a["statut"]) for a in r["articles"]] == [(84, "adopte_modifie")], "adopte modifie")
    r = essai("(L’article 84 n’est pas adopté.)")
    ok([(a["article"], a["statut"]) for a in r["articles"]] == [(84, "non_adopte")], "non adopte")
    r = essai("(L’article 84 est réservé.)")
    ok(r["articles"] == [] and r["inconnus"] == ["(L’article 84 est réservé.)"], "formule inconnue -> ticket")
    r = essai("(L’article 12 est adopté.)")
    ok(r["articles"] == [] and r["inconnus"] == [], "article non suivi ignore")
    r = V.extraire("1. Projet de loi de financement de la sécurité sociale (L’article 84 est supprimé.)" + FIN, {84}, 2027)
    ok(r["articles"] == [], "autre texte ignore")
    r = essai("(L’ensemble de la première partie du projet de loi de finances pour 2027 est adopté.)")
    ok(r["premiere"] and r["premiere"]["statut"] == "adoptee", "premiere partie adoptee")
    r = essai("L’ensemble de la première partie du projet de loi de finances pour 2027 n’est pas adopté.")
    ok(r["premiere"] and r["premiere"]["statut"] == "rejetee", "premiere partie rejetee -> ticket")
    ok(essai("x")["prochaine"].startswith("Prochaine séance, demain"), "ordre du jour suivant")
    print("Veille PLF : %d essai(s) en echec%s" % (len(echecs), (" : " + ", ".join(echecs)) if echecs else ". OK"))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
