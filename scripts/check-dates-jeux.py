#!/usr/bin/env python3
"""Contrôle : tout jeu de données DATÉ qu'une page affiche entre dans la date de cette page.

MOTIF (2026-10-16, arbitrage PRO-20261016-174136). `/enseignants/environnement/` a intégré le 16/10 une nouvelle
édition de l'INSEE (Insee Première n° 2130) ; son sitemap est resté au 02/10. La page lisait `empreinte_carbone` par
ses shortcodes sans le déclarer : aucun canal de date ne voyait le changement. Rien n'échouait. C'est la classe
« une mise à jour réelle reste invisible » : ce contrôle la rend impossible à reproduire en silence.

CE QUE LE CONTRÔLE LIT (jamais une déclaration : ce que la page consomme)
    - les shortcodes que la page appelle, et les jeux que chacun lit (`site.Data.<jeu>` dans layouts/shortcodes) ;
    - les jetons `{prefixe.cle}` de la page, et le jeu de chaque préfixe (table lue dans
      layouts/partials/desc-figures.html, qui les résout).
    Un jeu est « daté » s'il porte `releve_le` (racine ou bloc `affichage`) : seuls ceux-là peuvent dater une page.
    Déclaré = `donnees:` ∪ `date_suit:` du front matter (les deux clés que lit le gabarit de date).

CE QU'IL NE LIT PAS, et pourquoi (écart nommé, jamais silencieux)
    - `dossier-dette` et `reutiliser` : ils lisent les jeux des AUTRES volets pour la barre de navigation et les
      fiches ; la date d'une page n'a pas à suivre ses voisines ;
    - un jeu lu par un partial de gabarit (et non par la page) : il vaut pour toutes les pages, ce n'est pas un
      contenu propre.

Sortie 1 si une page affiche un jeu daté sans qu'il entre dans sa date. `--temoin` : rejoue le contrôle sur une
copie du front matter de `/enseignants/environnement/` privée de `date_suit` et exige qu'il morde.
"""
import json
import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
HORS_PERIMETRE = {"dossier-dette": "barre de navigation du dossier", "reutiliser": "fiches de réutilisation"}


def jeux_dates() -> set:
    out = set()
    for p in (RACINE / "data").glob("*.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8-sig"))
        except (ValueError, UnicodeDecodeError):
            continue
        if isinstance(d, dict):
            aff = d.get("affichage") if isinstance(d.get("affichage"), dict) else {}
            if d.get("releve_le") or aff.get("releve_le"):
                out.add(p.stem)
    return out


def table_shortcodes(dates: set) -> dict:
    out = {}
    for p in (RACINE / "layouts" / "shortcodes").glob("*.html"):
        if p.stem in HORS_PERIMETRE:
            continue
        lus = set(re.findall(r"site\.Data\.([a-z_]+)", p.read_text(encoding="utf-8"))) & dates
        if lus:
            out[p.stem] = lus
    return out


def table_prefixes() -> dict:
    t = (RACINE / "layouts" / "partials" / "desc-figures.html").read_text(encoding="utf-8")
    out = {}
    # Bloc « with site.Data.<jeu> » suivi de son printf "{<pref>.%s}"
    for jeu, pref in re.findall(r"with site\.Data\.([a-z_]+)\s*-?}}.*?printf \"\{([a-z]+)\.%s\}\"", t, re.S):
        out.setdefault(pref, jeu)
    # Forme « range $pref, $jeu := dict "ref" "promesses_referendum" ... »
    for bloc in re.findall(r"range \$pref, \$jeu := dict ([^}]+)", t):
        mots = re.findall(r'"([a-z_]+)"', bloc)
        for pref, jeu in zip(mots[::2], mots[1::2]):
            out[pref] = jeu
    return out


def front_matter(texte: str) -> dict:
    m = re.match(r"^---\r?\n(.*?)\r?\n---", texte, re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def ecarts_page(texte: str, sc: dict, pref: dict) -> tuple:
    fm = front_matter(texte)
    declares = set(fm.get("donnees") or []) | set(fm.get("date_suit") or [])
    lus = {}
    for nom in set(re.findall(r"\{\{[<%]\s*([a-z0-9_-]+)", texte)):
        for j in sc.get(nom, ()):
            lus.setdefault(j, f"shortcode {nom}")
    for p in set(re.findall(r"\{([a-z]+)\.[a-z0-9_]+\}", texte)):
        if p in pref:
            lus.setdefault(pref[p], f"jeton {{{p}.*}}")
    return {j: v for j, v in lus.items() if j not in declares}, lus, declares


def main() -> int:
    dates = jeux_dates()
    sc, pref = table_shortcodes(dates), table_prefixes()
    if len(pref) < 10 or len(sc) < 10:
        print(f"ERREUR : tables anormalement courtes (préfixes {len(pref)}, shortcodes {len(sc)}) : lecture des gabarits cassée")
        return 1

    if "--temoin" in sys.argv:
        p = RACINE / "content" / "enseignants" / "environnement" / "_index.md"
        t = re.sub(r"(?m)^date_suit:.*\n", "", p.read_text(encoding="utf-8"))
        ec, _, _ = ecarts_page(t, sc, pref)
        if "empreinte_carbone" in ec:
            print("TÉMOIN OK : sans `date_suit`, /enseignants/environnement/ est signalée (empreinte_carbone).")
            return 0
        print("TÉMOIN EN ÉCHEC : le contrôle ne voit pas le cas fondateur.")
        return 1

    pages = sorted((RACINE / "content").rglob("*.md"))
    examinees, fautives = 0, []
    for p in pages:
        texte = p.read_text(encoding="utf-8")
        ec, lus, _ = ecarts_page(texte, sc, pref)
        if not lus:
            continue
        examinees += 1
        if ec:
            fautives.append((p.relative_to(RACINE).as_posix(), ec))

    print(f"Jeux datés : {len(dates)} ; pages qui en affichent : {examinees} ; conformes : {examinees - len(fautives)} ; "
          f"en défaut : {len(fautives)} (hors périmètre : {', '.join(f'{k} ({v})' for k, v in HORS_PERIMETRE.items())})")
    for chemin, ec in fautives:
        print(f"  DÉFAUT {chemin} : " + " ; ".join(f"{j} ({v})" for j, v in sorted(ec.items())))
    if fautives:
        print("Correctif : ajouter le jeu à `donnees:` (page de données, modèle complet) ou à `date_suit:` (date seule).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
