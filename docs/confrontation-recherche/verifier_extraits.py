# -*- coding: utf-8 -*-
"""Confronte chaque extrait des fiches de lecture a la page PDF qu'il cite.

Usage : python verifier_extraits.py <dossier des textes .txt> [--temoin]

Les textes sont extraits des PDF lus (PyMuPDF, marqueurs « ===== PAGE PDF n ===== ») ; chaque
fiche nomme son fichier source en ligne « Version lue » (`fichier.pdf` ou `fichier.txt`). Un extrait
passe s'il figure, a la normalisation typographique pres (espaces, cesures de fin de ligne,
ligatures, guillemets), dans le texte de la page citee. Sortie 1 si un extrait echoue.
--temoin : altere un mot de chaque extrait et exige que TOUS echouent (le controle doit mordre).

Condition de mort : les fiches sont figees une fois les blocs publies ; le script n'a plus d'objet
quand plus aucune fiche n'est ajoutee ou modifiee (fin du chantier « Confrontation a la recherche »).
"""
import re
import sys
import unicodedata
from pathlib import Path

FICHES = Path(__file__).parent / "fiches"
EXTRAIT = re.compile(r"^E(\d+)\.\s*p\.\s*PDF\s*(\d+)\s*:\s*«\s*(.+?)\s*»\s*$", re.M)
SOURCE = re.compile(r"`?([A-Za-z0-9_\-]+)\.(?:pdf|txt)`?")


def norm(t):
    t = unicodedata.normalize("NFKC", t)
    t = t.replace("­", "")
    t = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)  # cesure de fin de ligne
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("−", "-")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip().lower()


def pages(txt):
    morceaux = re.split(r"===== PAGE PDF (\d+) =====", txt)
    return {int(morceaux[i]): norm(morceaux[i + 1]) for i in range(1, len(morceaux), 2)}


def main():
    dossier = Path(sys.argv[1])
    temoin = "--temoin" in sys.argv
    total = echecs = 0
    for fiche in sorted(FICHES.glob("*.md")):
        corps = fiche.read_text(encoding="utf-8")
        ligne = next((l for l in corps.splitlines() if "Version lue" in l), "")
        src = next((m.group(1) for m in SOURCE.finditer(ligne) if (dossier / (m.group(1) + ".txt")).exists()), None)
        extraits = EXTRAIT.findall(corps)
        if not src:
            print(f"ECHEC  {fiche.name} : source introuvable dans la ligne « Version lue »")
            echecs += 1
            continue
        if len(extraits) < 4:
            print(f"ECHEC  {fiche.name} : {len(extraits)} extrait(s) au format attendu, 4 exiges")
            echecs += 1
        pg = pages((dossier / (src + ".txt")).read_text(encoding="utf-8"))
        for num, page, cit in extraits:
            total += 1
            n = norm(cit)
            if temoin:
                mots = n.split(" ")
                mots[len(mots) // 2] = "zqxw"
                n = " ".join(mots)
            ok = n in pg.get(int(page), "")
            if ok == temoin:
                echecs += 1
                ailleurs = [p for p, t in pg.items() if norm(cit) in t]
                print(f"ECHEC  {fiche.name} E{num} p.{page}" + (f" (trouve p. {ailleurs})" if ailleurs and not temoin else ""))
    etat = "temoin" if temoin else "extraits"
    print(f"{etat} : {total} controle(s), {echecs} echec(s)")
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
