# -*- coding: utf-8 -*-
"""Essais de l'extracteur de veille_plf.py sur des formules du compte rendu officiel (05/11/2026 ; Senat, 19/11/2026).
Une formule connue s'integre ; une formule inconnue autour d'un article suivi devient un ticket, jamais une entree ;
un article d'un autre texte (hors troncon du projet de loi de finances) ne compte pas. Au Senat, la page se lit par sa
structure (intitule du point, mention d'article, navigation) ; une formule inconnue BLOQUE la seance."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import veille_plf as V  # noqa: E402

TETE = "2. Projet de loi de finances pour 2027 Seconde partie (suite) "
FIN = " 3. Ordre du jour de la prochaine séance Prochaine séance, demain, à neuf heures : Suite de la discussion de la seconde partie du projet de loi de finances pour 2027. La séance est levée."


def essai(corps, suivis={84, 34}):
    return V.extraire("Sommaire " + TETE + "Ordre du jour de la prochaine séance " + TETE + corps + FIN, set(suivis), 2027)


# ---------------------------------------------------------------- Senat : page du compte rendu integral, balisage reel
def page(*points):
    """points : (intitule, [paragraphes HTML]). Meme balisage que la page du Senat (titre_S1, mention_article, navigation,
    parentheses coupees en <span>)."""
    h = ['<html><body><h1 class="page-title">Séance du 25 novembre 2026</h1><!-- START : cri --><div id="cri">']
    for k, (titre, pars) in enumerate(points):
        h.append('<p>%d</p><div align=\'right\'><a class=\'link\' href=\'/dossierleg/%s.html\'><img alt="x"></a></div>'
                 % (k + 1, "pjlf2027" if "Loi de finances pour 2027" in titre else "pjl26-autre"))
        h.append('<p class="titre_S1" id="par_%d">%s</p>' % (k, titre))
        h += pars
    h.append("</div><!-- END cri --></body></html>")
    return "\n".join(h)


def art(n, dossier="pjlf2027"):
    return ['<p class="mention_article">Article&#160;%s</p>' % n,
            "<div align='right'><a class='link' href='/dossierleg/%s.html'><img alt=\"x\"></a></div>" % dossier]


PAR = '<p><span class="info_entre_parentheses">(L</span><span class="info_entre_parentheses">&#8217;</span>' \
      '<span class="info_entre_parentheses">article %s est adopt</span>&#233;.)</p>'


def sen(html_, suivis={34, 35, 36, 37, 84}, amdts=None):
    return V.extraire_senat(V.lignes_senat(html_), set(suivis), 2027, amdts or {})


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
    # 19/11/2026 : « ainsi rédigé » dans la parenthese d'un amendement, a l'Assemblee : ticket, plus jamais un silence.
    r = essai("(L’amendement no 12 est adopté ; en conséquence, l’article 34 est ainsi rédigé.)")
    ok(r["articles"] == [] and r["inconnus"] == ["en conséquence, l’article 34 est ainsi rédigé"], "AN ainsi redige -> ticket")
    r = essai("(L’amendement no 12 est adopté ; en conséquence, l’article 34 bis est supprimé.)")
    ok(r["inconnus"] == [], "AN article 34 bis n'est pas le 34")

    # ------------------------------------------------------------ Senat
    LF = "Loi de finances pour 2027"
    h = page((LF, ["<p>Suite de la discussion d&#8217;un projet de loi</p>"]
              + art(37) + ["<p>Mme la présidente. Je mets aux voix l&#8217;amendement n&#176;&#160;I-48.</p>",
                           '<p><span class="info_entre_parentheses">(L&#8217;amendement est adopté.)</span></p>',
                           "<p>Mme la présidente. Je mets aux voix l&#8217;article&#160;37, modifié.</p>", PAR % "&#160;37"]
              + art(35) + ["<p>Je mets aux voix les amendements identiques n<sup>os</sup>&#160;I-46 et I-725.</p>",
                           '<p><span class="info_entre_parentheses">(Les amendements sont adoptés.)</span></p>',
                           "<p>Mme la présidente. En conséquence, l&#8217;article&#160;35 est supprimé.</p>"]
              + art(36) + ["<p>Mme la présidente. En conséquence, l&#8217;article&#160;36 est ainsi rédigé.</p>"]
              + art(34) + ["<p>Je mets aux voix l&#8217;article&#160;34.</p><p>J&#8217;ai été saisie d&#8217;une demande de "
                           "scrutin public émanant du groupe Les Républicains.</p><p>Le scrutin est ouvert.</p>"
                           '<p><span class="info_entre_parentheses">(Le scrutin a lieu.)</span></p><p>Voici le résultat du '
                           "scrutin n°&#160;64&#160;:</p><p>Pour l&#8217;adoption</p><p>194</p><p>Le Sénat a adopté.</p>",
                           "<p>En conséquence, l&#8217;article&#160;34 bis est supprimé.</p>"]),
             ("Financement de la sécurité sociale pour 2027", art(35, "plfss2027") + ["<p>Je mets aux voix l&#8217;article&#160;35.</p>",
                                                                                 PAR % "&#160;35"]),
             ("Loi de finances de fin de gestion pour 2026", ["<p>En conséquence, l&#8217;article&#160;37 est supprimé.</p>"]))
    r = sen(h, amdts={"I-48": 37, "I-46": 35})
    ok([(a["article"], a["statut"]) for a in r["articles"]] == [(37, "adopte_modifie"), (35, "supprime"), (36, "redige"),
                                                                 (34, "adopte")], "Senat : quatre formules dans l'ordre")
    ok(r["articles"][0]["citation"] == "Je mets aux voix l’article 37, modifié. (L’article 37 est adopté.)", "Senat : citation (span recolles)")
    ok(sorted((a["amendement"], a["sort"]) for a in r["amendements"]) == [("I-46", "adopte"), ("I-48", "adopte")], "Senat : sort des amendements")
    ok(r["bloquants"] == [], "Senat : autres textes ignores, 34 bis n'est pas le 34 (%s)" % r["bloquants"])
    ok(r["ouverture"] == "Loi de finances pour 2027 Suite de la discussion d’un projet de loi", "Senat : intitule du point")
    r = sen(page((LF, art(84) + ["<p>Mme la présidente. Je mets aux voix l&#8217;article&#160;84.</p>",
                                 '<p><span class="info_entre_parentheses">(L&#8217;article&#160;84 est rétabli.)</span></p>'])))
    ok(r["articles"] == [] and r["bloquants"], "Senat : formule inconnue -> seance bloquee, aucune entree")
    r = sen(page((LF, art(84) + ["<p>Mme la présidente. L&#8217;article&#160;84 est réservé jusqu&#8217;après l&#8217;article 87.</p>"])))
    ok(r["articles"] == [] and r["bloquants"] == [], "Senat : reserve = ni resultat ni blocage")
    r = sen(page(("Mises au point au sujet de votes", art(37)), (LF, [])))
    ok(any("hors du point" in b for b in r["bloquants"]), "Senat : article du dossier hors du point -> blocage")
    r = sen(page((LF, ["<p>Je mets aux voix, modifié, l&#8217;ensemble de la première partie du projet de loi de finances pour"
                       " 2027.</p><p>Voici le résultat du scrutin n°&#160;81&#160;:</p><p>Le Sénat a adopté.</p>"])))
    ok(r["premiere"] and r["premiere"]["statut"] == "adoptee" and not r["bloquants"], "Senat : premiere partie adoptee")
    r = sen(page((LF, ["<p>Le Sénat va maintenant procéder au vote sur l&#8217;ensemble du projet de loi de finances pour 2027, "
                       "modifié.</p>"])))
    ok(any("ensemble" in b for b in r["bloquants"]), "Senat : vote sur l'ensemble -> blocage")
    x = V.transmission("Première lecture au Sénat Texte n° 155 (2026-2027) transmis au Sénat le 19 novembre 2026 Travaux")
    ok(x == {"numero": 155, "session": "2026-2027", "citation": "Texte n° 155 (2026-2027) transmis au Sénat le 19 novembre 2026",
             "date": "2026-11-19"}, "Senat : transmission")
    csv_ = ("sep=\nNature \tNuméro \tSubdivision \tAlinéa\tAuteur \tAu nom de \tDate de dépôt \tDispositif \tObjet \tSort \t"
            "Date de saisie du sort \tUrl amendement \tFiche Sénateur\n"
            "Amt\tII-12\tArticle 84\t\tM. X\tcommission des finances\t2026-11-20\t<p>Supprimer cet article.</p>\tO\t\t\t"
            "//www.senat.fr/amendements/2026-2027/155/Amdt_II-12.html\t\n"
            "Amt\tII-13\tArticle 84\t\tM. X\tcommission des finances\t2026-11-20\t<p>Alinéa 2</p>\tO\t\t\t//u\t\n"
            "Amt\tII-14\tArticle 84\t\tM. Y\t\t2026-11-20\t<p>Supprimer cet article.</p>\tO\t\t\t//u\t\n").encode("cp1252")
    j = V.amendements_commission(csv_, {84})
    ok([(a["amendement"], a["suppression"]) for a in j] == [("II-12", True), ("II-13", False)]
       and j[0]["url"].startswith("https://www.senat.fr/"), "Senat : amendements de la commission (Ameli)")
    idx = ('<li><a class=\'link\' href="s20261120/st20261120000.html">\nvendredi 20 novembre 2026 (séance n°&nbsp;23) </a>'
           "<ul class='list-links'>\n<li><a href='s20261120/s20261120_mono.html'>une page</a>&nbsp;version Provisoire\n</li>\n</ul>")
    L = V.seances_senat(idx)
    ok(L == [{"date": "2026-11-20", "numero": 23, "provisoire": True,
              "url": "https://www.senat.fr/seances/s202611/s20261120/s20261120_mono.html"}], "Senat : index du mois")
    lst = [{"date": "2026-11-18", "numero": 21}, {"date": "2026-11-19", "numero": 22}, {"date": "2026-11-23", "numero": 24}]
    ok(V.frontiere(lst, {"SENAT-2026-11-19", "SENAT-2026-11-23"}, "2026-11-19") == "2026-11-19", "Senat : trou dans la numerotation")
    lst[2]["numero"] = 23
    ok(V.frontiere(lst, {"SENAT-2026-11-19", "SENAT-2026-11-23"}, "2026-11-19") == "2026-11-23", "Senat : frontiere sans trou")
    ok(V.frontiere(lst, {"SENAT-2026-11-23"}, "2026-11-19") is None, "Senat : seance non lue")
    print("Veille PLF : %d essai(s) en echec%s" % (len(echecs), (" : " + ", ".join(echecs)) if echecs else ". OK"))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
