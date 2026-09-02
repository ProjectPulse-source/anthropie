#!/usr/bin/env python3
"""Parite fiche <-> registre canonique (data/works.yaml).

MOTIF (2026-08-11). Trois defauts signales par l'auteur en deux jours avaient la
meme forme : une donnee EXISTE quelque part, et la surface qui la consomme ne la
recoit pas -- sans erreur, sans warning, sans trace.

  · le livre publie, absent du mur /a-propos/ (liste de presence manuelle) ;
  · `pages` absent de la fiche Livresque -> pagination manquante sur DEUX pages ;
  · `subtitle` absent -> pas de hook sur /ressources-offertes/ ;
  · et, trouve par ce script au moment de l'ecrire : le QID Wikidata de Livresque
    (Q140517745) etait connu de works.yaml depuis le 01/08 mais absent de la
    fiche, donc absent du `sameAs` du JSON-LD Book. Idem edition anglaise.

Les deux premiers sont desormais couverts par le gabarit (auteur-wall) et par
`check-corpus-counters.py`. Ce script couvre le reste de la classe : ce que le
REGISTRE sait et que la FICHE ne dit pas, et les valeurs presentes des deux
cotes qui ont DIVERGE.

EXTENSIONS (2026-09-02) : meme regle pour les working papers (fiches FR et EN d'un
AWP portent le MEME item) et pour les articles (fiche trouvee par son url_externe ;
le QID attendu est `wikidata_review` s'il existe -- l'item de la recension seule --
sinon `wikidata`). Motif : 19 oeuvres pointaient vers l'auteur sur Wikidata quand le
registre n'en connaissait que 9, et aucune page AWP n'emettait de `sameAs` Wikidata.

Principe : le registre est la source de verite ; la fiche doit la refleter.
On ne signale JAMAIS un champ absent des deux cotes -- ce n'est pas une
incoherence, c'est un travail a faire, suivi ailleurs (checklists, works.yaml).

Sortie 0 = conforme. Sortie 1 = au moins une divergence.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML requis : pip install pyyaml")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent

# id works.yaml -> slug de la fiche FR. Une entree manquante ici est signalee :
# un livre au registre sans fiche connue est exactement le trou qu'on traque.
SLUGS = {
    "book-anthropie": "anthropie-ordre-ici-dette-ailleurs",
    "book-dette-publique": "dette-publique-qui-paie-vraiment",
    "book-premier-coup": "la-societe-du-premier-coup",
    "book-livresque-des-mots": "livresque-des-mots",
    "book-lodyssee-des-idees": "lodyssee-des-idees",
}

# champ registre -> champ front matter
CHAMPS = [("wikidata", "wikidata_qid"), ("pages", "pages"), ("isbn", "isbn")]


def front_matter(path: Path) -> dict:
    m = re.search(r"(?s)\A---\r?\n(.*?)\r?\n---", path.read_text(encoding="utf-8"))
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def compare(etiquette: str, reg: dict, fiche: dict, out: list) -> None:
    for champ_reg, champ_fm in CHAMPS:
        v_reg, v_fm = reg.get(champ_reg), fiche.get(champ_fm)
        if not v_reg:
            continue  # le registre ne sait rien : rien a refleter
        if not v_fm:
            out.append(
                f"{etiquette} : {champ_reg}={v_reg} au registre, `{champ_fm}` ABSENT "
                f"de la fiche (la surface qui le consomme ne le recevra pas)"
            )
        elif str(v_reg) != str(v_fm):
            out.append(
                f"{etiquette} : DIVERGENCE {champ_fm} — registre={v_reg} / fiche={v_fm}"
            )


def main() -> int:
    registre = yaml.safe_load((ROOT / "data" / "works.yaml").read_text(encoding="utf-8"))
    livres = {w["id"]: w for w in registre["works"] if w.get("type") == "book"}
    awps = {w["id"]: w for w in registre["works"] if w.get("type") == "awp"}
    articles = [w for w in registre["works"]
                if w.get("type") == "article" and (w.get("wikidata") or w.get("wikidata_review"))]
    ecarts: list[str] = []

    for bid, oeuvre in livres.items():
        slug = SLUGS.get(bid)
        if not slug:
            ecarts.append(f"{bid} : livre au registre sans slug de fiche connu (completer SLUGS)")
            continue
        fiche = ROOT / "content" / "livres" / f"{slug}.md"
        if not fiche.exists():
            ecarts.append(f"{bid} : fiche content/livres/{slug}.md INTROUVABLE")
            continue
        compare(slug, oeuvre, front_matter(fiche), ecarts)

        # Edition dans une autre langue : meme regle, fiche .en.md
        edition_en = oeuvre.get("english_edition")
        if edition_en:
            fiche_en = ROOT / "content" / "livres" / f"{slug}.en.md"
            if fiche_en.exists():
                compare(f"{slug}.en", edition_en, front_matter(fiche_en), ecarts)

    # Working papers : la fiche FR et la fiche EN refletent le MEME item.
    for aid, oeuvre in awps.items():
        for suffix in (".md", ".en.md"):
            fiche = ROOT / "content" / "awp" / f"{aid}{suffix}"
            if not fiche.exists():
                ecarts.append(f"{aid} : fiche content/awp/{aid}{suffix} INTROUVABLE")
                continue
            compare(f"{aid}{suffix}", oeuvre, front_matter(fiche), ecarts)

    # Articles : fiche retrouvee par url_externe ; QID attendu = wikidata_review sinon wikidata.
    fiches_pub = {}
    for p in (ROOT / "content" / "publications").glob("*.md"):
        if p.name.startswith("_"):
            continue
        fm = front_matter(p)
        fiches_pub[(fm.get("url_externe") or "").rstrip("/")] = (p.name, fm)
    for w in articles:
        url = (w.get("url") or "").rstrip("/")
        hit = fiches_pub.get(url)
        if not hit:
            ecarts.append(f"{w['id']} : QID au registre mais aucune fiche publication ne porte son url ({url or 'url vide'})")
            continue
        nom, fm = hit
        attendu = {"wikidata": w.get("wikidata_review") or w.get("wikidata")}
        compare(nom, attendu, fm, ecarts)

    print(f"Parite fiche <-> registre : {len(livres)} livre(s), {len(awps)} AWP, {len(articles)} article(s) a QID au registre")
    if not ecarts:
        print("\nAucune divergence. OK")
        return 0
    print()
    for e in ecarts:
        print(f"  ECART  {e}")
    print(f"\n{len(ecarts)} divergence(s). Corriger la fiche, ou le registre s'il a tort.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
