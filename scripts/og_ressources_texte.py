#!/usr/bin/env python3
"""Cartes de partage et vignettes des ressources sans figure de données (02/11/2026, demande de l'auteur).

Le dessin n'est pas forcément un graphe : nuage de mots du glossaire, frise, tuiles. Il ne montre que ce que la page dit :
termes lus dans le front matter, jalons comptés dans le jeu du Registre, libellés relus dans la page (og_notions.verifie).
Écrit : static/images/{og,vig}-texte-<nom>{,-en}.jpg, et la carte du glossaire sous son nom d'origine.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import og_dossier_dette as og  # noqa: E402
import og_notions as n  # noqa: E402

SIGNE = "Stéphane Lalut · CC BY 4.0"


def nuage(termes: list[str], coeur: str):
    """Nuage déterministe : le cœur au centre, les termes par rangées autour, sans échelle de fréquence."""
    def dessin(d) -> None:
        tailles, cols = (26, 19, 22), (og.C1, og.SEC, og.C2)
        cy = (n.HAUT + n.BAS) / 2
        fc = og.font("newsreader", 50, 600)
        d.text(((n.X0 + n.X1 - d.textlength(coeur, font=fc)) / 2, cy - 32), coeur, font=fc, fill=og.NAVY)
        rangs = [cy - 150, cy - 104, cy - 66, cy + 44, cy + 84, cy + 128]
        i = 0
        for y in rangs:
            x = float(n.X0)
            ligne = []
            while i < len(termes):
                f = og.font("inter", tailles[i % 3], 600)
                w = d.textlength(termes[i], font=f)
                if x + w > n.X1:
                    break
                ligne.append((termes[i], f, w, cols[i % 3]))
                x += w + 18
                i += 1
            libre = (n.X1 - (x - 18)) / 2
            x = n.X0 + libre
            for t, f, w, c in ligne:
                d.text((x, y), t, font=f, fill=c)
                x += w + 18
    return dessin


def frise(points: list[tuple[str, str]]):
    """Jalons également espacés : frise de lecture, sans échelle de temps."""
    def dessin(d) -> None:
        y = (n.HAUT + n.BAS) / 2 - 10
        d.line([n.X0 + 8, y, n.X1 - 8, y], fill=og.C1, width=4)
        pas = (n.X1 - n.X0 - 80) / (len(points) - 1)
        fd, fl = og.font("inter", 20, 600), og.font("inter", 18, 600)
        for i, (date, nom) in enumerate(points):
            x = n.X0 + 40 + i * pas
            d.ellipse([x - 10, y - 10, x + 10, y + 10], fill=og.C2 if i == len(points) - 1 else og.C1)
            if date:
                d.text((x - d.textlength(date, font=fd) / 2, y - 48), date, font=fd, fill=og.GREY)
            mots = nom.split(" ")
            for k, m in enumerate(mots[:2] if len(mots) > 1 and d.textlength(nom, font=fl) > pas else [nom]):
                d.text((x - d.textlength(m, font=fl) / 2, y + 24 + k * 24), m, font=fl, fill=og.INK)
    return dessin


def tuiles(noms: list[str], par: int):
    def dessin(d) -> None:
        lignes = [noms[i:i + par] for i in range(0, len(noms), par)]
        g, h = 12, (n.BAS - n.HAUT - 12 * (len(lignes) - 1)) / len(lignes)
        h = min(h, 92)
        y = (n.HAUT + n.BAS - h * len(lignes) - g * (len(lignes) - 1)) / 2
        for i, l in enumerate(lignes):
            n.rangee(d, y + i * (h + g), y + i * (h + g) + h, l, og.C1 if i == 0 else og.SEC, False)
    return dessin


def rangees(etages):
    """Étages de boîtes sans flèche : une flèche centrale désignerait une boîte comme la réponse."""
    def dessin(d) -> None:
        h, g = 68, 56
        y = (n.HAUT + n.BAS - h * len(etages) - g * (len(etages) - 1)) / 2
        for i, (noms, col, plein) in enumerate(etages):
            n.rangee(d, y + i * (h + g), y + i * (h + g) + h, noms, col, plein)
    return dessin


def registre(reg: dict, mot: str):
    """Sept barres : nombre de jalons par âge, compté dans le jeu publié."""
    nb = [sum(1 for j in reg["jalons"] if j["age"] == a["num"]) for a in reg["ages"]]
    if sum(nb) != len(reg["jalons"]):
        og.fail("registre : jalons hors des sept ages")

    def dessin(d) -> None:
        fl, fv = og.font("inter", 18, 600), og.font("inter", 18, 500)
        pas = (n.BAS - n.HAUT) / len(nb)
        for i, v in enumerate(nb):
            y = n.HAUT + i * pas
            d.text((n.X0, y + 8), "%s %d" % (mot, i + 1), font=fl, fill=og.INK)
            xa, xb = n.X0 + 84, n.X0 + 84 + (n.X1 - n.X0 - 134) * v / max(nb)
            d.rectangle([xa, y + 8, xb, y + pas - 14], fill=og.C2 if i == len(nb) - 1 else og.C1)
            d.text((xb + 8, y + 8), str(v), font=fv, fill=og.GREY)
    return dessin


def termes_glossaire(f: Path) -> tuple[str, list[str]]:
    fm = f.read_text(encoding="utf-8").split("---")[1]
    coeur = re.search(r'coeur:.*?\bt: "([^"]+)"', fm).group(1)
    t = re.findall(r'-\s*\{id: "[^"]+", t: "([^"]+)"', fm)
    if len(t) < 12:
        og.fail("glossaire : carte du vocabulaire illisible (%d termes)" % len(t))
    return coeur, t


def cartes() -> list:
    R = og.ROOT
    gf, ge = termes_glossaire(R / "content/glossaire/_index.md"), termes_glossaire(R / "content/glossaire/_index.en.md")
    rf = json.loads((R / "data/registre_couts_deportes.json").read_text(encoding="utf-8"))
    re_ = json.loads((R / "data/registre_couts_deportes_en.json").read_text(encoding="utf-8"))
    nj = len(rf["jalons"])
    th_f = ["Santé", "Salaires", "Prix", "École", "Emploi", "Sécurité", "Dette", "Immigration", "Climat"]
    th_e = ["Health", "Wages", "Prices", "Schools", "Jobs", "Security", "Debt", "Immigration", "Climate"]
    return [
        ("glossaire", False, "og-glossaire.jpg", ["Glossaire"], "Les termes du cadre anthropique.",
         "glossaire", nuage(gf[1], gf[0]), []),
        ("glossaire", True, "og-glossaire.en.jpg", ["Glossary"], "The terms of the anthropic framework.",
         "en/glossaire", nuage(ge[1], ge[0]), []),
        ("registre-des-couts-deportes", False, "og-texte-registre.jpg", ["Le Registre des", "coûts déportés"],
         "%d jalons en sept âges, par âge." % nj, "registre-des-couts-deportes", registre(rf, "Âge"), []),
        ("registre-des-couts-deportes", True, "og-texte-registre-en.jpg", ["The Register of", "Offloaded Costs"],
         "%d milestones in seven ages, by age." % nj, "en/register-of-offloaded-costs", registre(re_, "Age"), []),
        ("que-peut-faire-un-president-promesse-par-promesse", False, "og-texte-promesses.jpg", ["Neuf promesses", "de campagne"],
         "Ce qu’un président peut vraiment faire.", "que-peut-faire-un-president-promesse-par-promesse",
         tuiles(th_f, 3), th_f),
        ("que-peut-faire-un-president-promesse-par-promesse", True, "og-texte-promesses-en.jpg", ["Nine campaign", "promises"],
         "What a president can really do.", "en/what-can-a-president-do-promise-by-promise", tuiles(th_e, 3), th_e),
        ("chercheur-independant", False, "og-texte-chercheur.jpg", ["Chercheur", "indépendant"],
         "Publier des travaux citables hors institution.", "chercheur-independant",
         n.schema([(["ORCID", "Zenodo", "SSRN", "HAL"], og.SEC, False), (["Travaux citables"], og.C1, True)]),
         ["ORCID", "Zenodo", "SSRN", "HAL", "citables"]),
        ("chercheur-independant", True, "og-texte-chercheur-en.jpg", ["Independent", "researcher"],
         "Publishing citable work outside an institution.", "en/independent-researcher",
         n.schema([(["ORCID", "Zenodo", "SSRN", "HAL"], og.SEC, False), (["Citable work"], og.C1, True)]),
         ["ORCID", "Zenodo", "SSRN", "HAL", "citable"]),
        ("citations-celebres-verifiees", False, "og-texte-citations.jpg", ["Citations célèbres", "vérifiées"],
         "Ce qu’ils ont vraiment écrit, relu au texte.", "citations-celebres-verifiees",
         tuiles(["Hugo", "Voltaire", "Molière", "La Fontaine", "Wilde"], 3), ["Hugo", "Voltaire", "Molière", "La Fontaine", "Wilde"]),
        # Page Littérature (auteur, 10/11/2026) : sa propre carte, sans Wilde, absent de l'activité.
        ("enseignants/litterature", False, "og-texte-litterature.jpg", ["Authentique, retouchée", "ou introuvable ?"],
         "Vérifier une citation : une activité de Première.", "enseignants/litterature",
         rangees([(["Voltaire", "Hugo", "La Fontaine", "Molière"], og.SEC, False),
                  (["Authentique", "Retouchée", "Introuvable"], og.C1, True)]),
         ["Voltaire", "Hugo", "La Fontaine", "Molière", "authentique", "retouchée", "introuvable"]),
        ("combien-de-temps-une-erreur-reste-inscrite", False, "og-texte-erreur.jpg", ["Une erreur inscrite,", "pour combien de temps ?"],
         "Ce qu\u2019il faut vérifier, durée par durée.", "combien-de-temps-une-erreur-reste-inscrite",
         tuiles(["Banque de France", "Casier", "Points", "Malus", "Maladie"], 3), ["Banque de France", "casier", "points", "malus", "maladie"]),
        ("comment-lecriture-a-transforme-la-pensee", False, "og-texte-ecriture.jpg", ["Comment l’écriture", "a transformé la pensée"],
         "De la voix à l’intelligence artificielle.", "comment-lecriture-a-transforme-la-pensee",
         frise([("", "Voix"), ("", "Écriture"), ("", "Imprimerie"), ("", "Intelligence artificielle")]),
         ["voix", "écriture", "imprimerie", "intelligence artificielle"]),
        ("comment-lecriture-a-transforme-la-pensee", True, "og-texte-ecriture-en.jpg", ["How writing", "transformed thought"],
         "From the voice to artificial intelligence.", "en/how-writing-transformed-thought",
         frise([("", "Voice"), ("", "Writing"), ("", "Printing press"), ("", "Artificial intelligence")]),
         ["voice", "writing", "printing press", "artificial intelligence"]),
        ("le-pouvoir-de-machiavel-a-foucault", False, "og-texte-pouvoir.jpg", ["À quoi tient", "l’obéissance ?"],
         "Le pouvoir, de Machiavel à Foucault et au-delà.", "le-pouvoir-de-machiavel-a-foucault",
         frise([("1513", "Machiavel"), ("1651", "Hobbes"), ("1789", "Légitimité"), ("1975", "Foucault"), ("1979", "Thatcher")]),
         ["1513", "Machiavel", "1651", "Hobbes", "1789", "légitimité", "1975", "Foucault", "1979", "Thatcher"]),
        ("tabula-rasa-locke", False, "og-texte-tabula.jpg", ["La tabula rasa"],
         "Locke a-t-il vraiment parlé d’une page blanche ?", "tabula-rasa-locke",
         frise([("", "Tablette"), ("", "Locke"), ("", "Leibniz")]), ["tablette", "Locke", "Leibniz"]),
    ]


def main() -> int:
    for page, en, nom, titre, accroche, url, dessin, libelles in cartes():
        n.verifie(page, en, libelles)
        og.carte(nom, titre, accroche, SIGNE, "stephane-lalut.com/%s/" % url, dessin, [])
    return 0


if __name__ == "__main__":
    sys.exit(main())
