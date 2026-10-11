#!/usr/bin/env python3
"""Controle : toute RESSOURCE DE DONNEES suit le modele du dossier dette (auteur, 2026-09-30).

REGLE (CLAUDE.md du site, section « Modele d'une ressource de donnees ») : le dossier dette publique -- quatre volets
refaits le 30/09 sur quatre contre-expertises -- sert de modele de structure et de methode a toute ressource de
donnees. Ce controle ne verifie que ce qui se verifie MECANIQUEMENT ; le reste (ordre de lecture, formulations,
contre-expertise) est une discipline ecrite dans le CLAUDE.md, pas un verrou.

Perimetre : les fichiers content/**/*.md dont le front matter declare `donnees:` (une page qui publie des chiffres
tires d'un jeu data/<jeu>.json). Brouillons exemptes et comptes. Pour chaque page :
  1. une carte de partage propre (`og_image:`), jamais la carte generique du site ;
  2. un « resultat en une phrase » (bloc .resultat-phrase) ;
  3. le bloc commun « Reutiliser cette page » ({{< reutiliser ... >}}) ;
  4. un balisage Dataset (`dataset:` ou `dataset_dette: true`) ;
  5. chaque jeu declare publie son JSON ET son CSV dans static/ ;
  6. si la page appelle le livre ({{< appel-livre ...), sans note Amazon (`avis="non"`) : une ressource n'est pas
     une fiche produit.
  7. la vignette de l'index /ressources/ existe : `og_image: images/og-X.jpg` -> static/images/vig-X.jpg (meme dessin
     sur fond blanc, produit par le generateur de la carte). Sans elle la page s'afficherait dans la grille du
     dossier sans image, en silence (presentation de l'index retenue par l'auteur le 2026-10-01, valable pour
     toute ressource a venir).
Conservation : pages vues == conformes + en defaut + brouillons exemptes.

CLASSIFICATION (industrialisation des ressources, arbitrage OPTIMUM-26 du 2026-10-11, chantier 5). Perimetre plus large :
TOUTE page qui declare `ressource:` (avec ou sans donnees, FR et EN), sinon 14 pages echappaient au processus.
  8. `ressource.type` : liste non vide de TYPES (protocole de la page, CLAUDE.md du site, « Production des ressources ») ;
  9. `ressource.refonte` (date AAAA-MM-JJ de la relecture attestee) : le NIVEAU de la page, source unique lue par les
     controles du build (check-rendu-ressources.py) -- absent = page pas encore refondue ;
 10. une page anglaise declare le meme type et la meme refonte que sa page francaise ;
 11. une page de donnees sans `refonte` doit figurer dans NON_REFONDUES (les dix pages du 2026-10-11) ; une page de
     la liste devenue refondue doit en sortir. La liste ne peut que diminuer : une page de donnees nouvelle nait
     refondue. CONDITION DE MORT de la regle 11 : liste vide -> supprimer NON_REFONDUES et son code.

Condition de mort (regles 1 a 10) : aucune -- regles permanentes du modele ; a reexaminer si le modele est abandonne
ou refondu.
Sortie console ASCII pur.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"

TYPES = {"quantitatif", "juridique-institutionnel", "explicatif-causal", "notion", "usage"}
# Figee le 2026-10-11 : ne peut que diminuer (regle 11).
NON_REFONDUES = {
    "ce-que-la-france-peut-decider-dans-l-union-europeenne", "comment-savoir-si-une-promesse-est-tenue",
    "qui-peut-faire-adopter-une-loi",
    "un-president-peut-il-recourir-au-referendum", "une-loi-votee-s-applique-t-elle-tout-de-suite",
}


def bloc_ressource(fm: str) -> dict | None:
    """Le bloc `ressource:` lu en YAML (pyyaml : installe par hugo.yml avant check-all)."""
    import yaml
    d = yaml.safe_load(fm) or {}
    r = d.get("ressource")
    return r if isinstance(r, dict) else None


def classification() -> list[tuple[str, str]]:
    """Regles 8 a 11 sur toute page a `ressource:`. Rend [(page, ecart)]."""
    fautes, lues, fr = [], {}, {}
    for p in sorted(CONTENT.rglob("*.md")):
        texte = p.read_text(encoding="utf-8")
        fm = front_matter(texte)
        if not re.search(r"^ressource:", fm, re.M) or re.search(r"^draft:\s*true\s*$", fm, re.M):
            continue
        rel = p.relative_to(ROOT).as_posix()
        r = bloc_ressource(fm) or {}
        t, ref = r.get("type"), r.get("refonte")
        if not isinstance(t, list) or not t:
            fautes.append((rel, "ressource.type absent ou pas une liste (types : %s)" % ", ".join(sorted(TYPES))))
        else:
            for x in t:
                if x not in TYPES:
                    fautes.append((rel, "ressource.type inconnu : %r" % x))
        if ref is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(ref)):
            fautes.append((rel, "ressource.refonte n'est pas une date AAAA-MM-JJ : %r" % ref))
        cle = (p.parent.as_posix(), p.name.replace(".en.md", ".md"))
        val = (t, None if ref is None else str(ref))
        (lues if p.name.endswith(".en.md") else fr)[cle] = (rel, val)
        if not p.name.endswith(".en.md") and re.search(r"^donnees:", fm, re.M):
            nom = p.parent.relative_to(CONTENT).as_posix()
            if ref is None and nom not in NON_REFONDUES:
                fautes.append((rel, "page de donnees sans ressource.refonte, absente de NON_REFONDUES (liste figee "
                                    "le 2026-10-11) : une page de donnees nouvelle nait refondue"))
            if ref is not None and nom in NON_REFONDUES:
                fautes.append((rel, "page refondue encore dans NON_REFONDUES : la retirer de la liste"))
    for cle, (rel, val) in lues.items():
        if cle in fr and fr[cle][1] != val:
            fautes.append((rel, "type ou refonte differents de la page francaise %s : %r != %r" % (fr[cle][0], val, fr[cle][1])))
    return fautes


def front_matter(texte: str) -> str:
    if not texte.startswith("---"):
        return ""
    fin = texte.find("\n---", 3)
    return texte[3:fin] if fin > 0 else ""


def jeux(fm: str) -> list[str]:
    m = re.search(r"^donnees:\s*\[([^\]]*)\]", fm, re.M)
    return [j.strip().strip("'\"") for j in m.group(1).split(",") if j.strip()] if m else []


def main() -> int:
    vues, conformes, brouillons, fautes = 0, 0, 0, []
    for p in sorted(CONTENT.rglob("*.md")):
        texte = p.read_text(encoding="utf-8")
        fm = front_matter(texte)
        if not re.search(r"^donnees:", fm, re.M):
            continue
        vues += 1
        rel = p.relative_to(ROOT).as_posix()
        if re.search(r"^draft:\s*true\s*$", fm, re.M):
            brouillons += 1
            continue
        corps = texte[len(fm) + 6:]
        f = []
        og = re.search(r"^og_image:\s*[\"']?([^\"'\s]+)", fm, re.M)
        if not og:
            f.append("pas de carte de partage propre (og_image)")
        else:
            vig = og.group(1).replace("og-", "vig-", 1)
            if vig == og.group(1):
                f.append("og_image %s : nom sans 'og-', vignette d'index non derivable" % og.group(1))
            elif not (STATIC / vig).is_file():
                f.append("vignette d'index static/%s absente (le generateur de la carte doit la produire)" % vig)
        if not re.search(r"^ressource:", fm, re.M):
            f.append("page de donnees sans bloc ressource: (type et niveau non declares : regles 8 a 11)")
        if 'class="resultat-phrase"' not in corps:
            f.append("pas de 'resultat en une phrase' (div.resultat-phrase)")
        if "{{< reutiliser " not in corps:
            f.append("pas de bloc 'Reutiliser cette page'")
        if not (re.search(r"^dataset:", fm, re.M) or re.search(r"^dataset_dette:\s*true", fm, re.M)):
            f.append("pas de balisage Dataset (dataset: ou dataset_dette: true)")
        for j in jeux(fm):
            for ext in ("json", "csv"):
                if not (STATIC / ("%s.%s" % (j, ext))).is_file():
                    f.append("jeu %s : static/%s.%s absent" % (j, j, ext))
        for m in re.finditer(r"\{\{< appel-livre [^>]*>\}\}", corps):
            if 'avis="non"' not in m.group(0):
                f.append("appel-livre sans avis=\"non\" (note Amazon sur une ressource)")
        if f:
            fautes.append((rel, f))
        else:
            conformes += 1
    assert vues == conformes + len(fautes) + brouillons, "conservation rompue"
    for rel, f in fautes:
        for x in f:
            print("  ECART  %s : %s" % (rel, x))
    classe = classification()
    for rel, x in classe:
        print("  ECART  %s : %s" % (rel, x))
    if classe:
        print("Classification des ressources : %d ecart(s) (regles 8 a 11 de l'en-tete)." % len(classe))
    else:
        print("Classification des ressources : type et niveau declares partout ; %d page(s) de donnees non refondue(s) "
              "(liste figee)." % len(NON_REFONDUES))
    if fautes or classe:
        print("Modele des ressources : %d page(s) en ecart sur %d (brouillons exemptes : %d)." % (len(fautes), vues, brouillons))
        print("  -> voir CLAUDE.md du site, section Modele d'une ressource de donnees.")
        return 1
    print("Modele des ressources : %d/%d page(s) de donnees conformes (brouillons exemptes : %d). OK" % (conformes, vues, brouillons))
    return 0


if __name__ == "__main__":
    sys.exit(main())
