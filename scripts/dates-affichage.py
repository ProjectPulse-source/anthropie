#!/usr/bin/env python3
"""Date d'un TEXTE affiché modifié sans que ses données changent : registre data/dates_affichage.json.

MOTIF (2026-10-16, arbitrage PRO-20261016-174136, angle mort n° 2 du contradicteur). Les générateurs ne réécrivent
`releve_le` que si une DONNÉE change ; une correction du texte qu'ils produisent (un compte « 13 » devenu « 12 pays »,
une date de maximum rectifiée) changeait la page servie sans changer sa date. Mesuré le 16/10/2026 : six jeux
(dette_baisse, dette_collectivites, dette_inflation, dette_monde, niveau_eleves, et empreinte_carbone, celui-ci daté
par son relevé) avaient un bloc `affichage` modifié depuis la veille, cinq sans nouveau relevé.

Pourquoi un registre à part, et pas un champ dans le jeu : les générateurs comparent le fichier entier pour décider
« rien écrit » ; un champ qu'ils ne connaissent pas les ferait réécrire, avec un relevé du jour, à données identiques.

RÈGLE
    Pour un jeu dont `affichage` ou `affichage_en` diffère de la référence (HEAD par défaut), hors clés `releve_le`,
    alors que son `releve_le` racine est inchangé : chaque PAGE qui affiche une clé modifiée (jeton `{pref.cle}`,
    argument `"cle"` d'un shortcode, ou shortcode dont le gabarit lit `"cle"`) doit porter la date du jour dans le
    registre, au grain de la page. Au grain du jeu, `/enseignants/` aurait pris la date d'une correction qu'elle
    n'affiche pas (mesuré le 16/10) : ce serait une date artificielle. La date de page (layouts/partials/page-date.html)
    prend le maximum ; le Dataset garde son relevé.
    Sans écart avec HEAD (cas de la CI, où l'arbre est le commit), le contrôle ne trouve rien à exiger.

FOND ET FORME (contre-expertise PRO-20261016-195302, P3) : la typographie (espaces insécables, apostrophes,
guillemets) est normalisée avant comparaison et ne redate jamais rien. Tout autre écart se CLASSE explicitement :
--ecrire (fond : chiffre, rang, période, sens) date la page ; --forme (orthographe, tournure sans changement de
sens) le consigne dans `formes` sans toucher à la date. L'outil ne choisit jamais à la place de la session.

Usage : python scripts/dates-affichage.py [--base REV] [--ecrire | --forme] [--temoin]
    sans option  : contrôle, sortie 1 si une page touchée n'est pas classée (dans check-all, avant commit) ;
    --ecrire     : classe « fond » et pose la date du jour pour chaque page touchée ;
    --forme      : classe « forme », sans date ;
    --base REV   : référence autre que HEAD (rattrapage d'un texte déjà commité) ;
    --temoin     : mute en mémoire une valeur d'affichage et exige d'être signalé.
RELEVÉ AVANCÉ SANS DONNÉE (17/10/2026, arbitrage anthropie-site-20261017-030435, § 6) : un jeu dont `releve_le` change
par rapport à la référence alors que ses DONNÉES (scripts/releve_jeu.py : hors dates, licence, blocs de texte, textes de
méthode) sont identiques est refusé. Le bandeau « Données mises à jour le » mentirait. Sept générateurs le faisaient ; ils
passent désormais par l'organe commun, et ce contrôle couvre aussi tout générateur futur. Témoin 3 dans --temoin.
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import releve_jeu as rj  # noqa: E402  -- même définition des données que les générateurs (organe commun)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "data" / "dates_affichage.json"


def charger_ref(rev: str, chemin: str):
    r = subprocess.run(["git", "-C", str(RACINE), "show", f"{rev}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout.decode("utf-8-sig"))
    except ValueError:
        return None


def releve(d: dict):
    return d.get("releve_le") or (d.get("meta") or {}).get("releve_le")


# Changements de FORME reconnus d'office (contre-expertise PRO-20261016-195302, P3) : espaces (insécable, fine
# insécable, ordinaire), apostrophe et guillemets typographiques ou droits. Ils ne redatent jamais une page.
FORME = str.maketrans({" ": " ", " ": " ", " ": " ", "’": "'", "‘": "'",
                       "“": '"', "”": '"', "«": '"', "»": '"'})


def normaliser(v) -> str:
    return re.sub(r"\s+", " ", str(v).translate(FORME)).strip()


def affichage_change(ancien: dict, nouveau: dict) -> list:
    """Clés dont la valeur a changé AU FOND : les différences de pure typographie sont ignorées."""
    cles = []
    for bloc in ("affichage", "affichage_en"):
        a, b = ancien.get(bloc), nouveau.get(bloc)
        if isinstance(a, dict) and isinstance(b, dict):
            cles += [f"{bloc}.{k}" for k in sorted(set(a) | set(b))
                     if k != "releve_le" and normaliser(a.get(k)) != normaliser(b.get(k))]
    return cles


def jeux_modifies(rev: str, muter=None) -> dict:
    out = {}
    suivis = subprocess.run(["git", "-C", str(RACINE), "ls-files", "data/*.json"], capture_output=True, text=True).stdout.split()
    for chemin in suivis:
        if chemin.endswith("dates_affichage.json"):
            continue
        ancien = charger_ref(rev, chemin)
        try:
            nouveau = json.loads((RACINE / chemin).read_text(encoding="utf-8-sig"))
        except (ValueError, FileNotFoundError):
            continue
        if not isinstance(ancien, dict) or not isinstance(nouveau, dict):
            continue
        if muter:
            nouveau = muter(Path(chemin).stem, nouveau)
        cles = affichage_change(ancien, nouveau)
        if cles and releve(ancien) == releve(nouveau):
            out[Path(chemin).stem] = cles
    return out


def releves_avances(rev: str, muter=None) -> list:
    """Jeux dont le relevé a changé sans qu'aucune donnée change (référence `rev`)."""
    out = []
    suivis = subprocess.run(["git", "-C", str(RACINE), "ls-files", "data/*.json"], capture_output=True, text=True).stdout.split()
    for chemin in suivis:
        if chemin.endswith("dates_affichage.json"):
            continue
        ancien = charger_ref(rev, chemin)
        try:
            nouveau = json.loads((RACINE / chemin).read_text(encoding="utf-8-sig"))
        except (ValueError, FileNotFoundError):
            continue
        if not isinstance(ancien, dict) or not isinstance(nouveau, dict):
            continue
        if muter:
            nouveau = muter(Path(chemin).stem, nouveau)
        if releve(ancien) and releve(nouveau) != releve(ancien) and rj.donnees(ancien) == rj.donnees(nouveau):
            out.append((Path(chemin).stem, releve(ancien), releve(nouveau)))
    return out


def lire_registre() -> dict:
    if REGISTRE.exists():
        return json.loads(REGISTRE.read_text(encoding="utf-8"))
    return {"_doc": "", "pages": {}}


def pages_touchees(mod: dict) -> dict:
    """{chemin de page relatif a content/ : [cles]} pour les cles modifiees que la page affiche."""
    cles = sorted({c.split(".", 1)[1] for cs in mod.values() for c in cs})
    sc = {}
    for f in (RACINE / "layouts" / "shortcodes").glob("*.html"):
        t = f.read_text(encoding="utf-8")
        lues = [k for k in cles if f'"{k}"' in t]
        if lues:
            sc[f.stem] = lues
    out = {}
    for f in sorted((RACINE / "content").rglob("*.md")):
        t = f.read_text(encoding="utf-8")
        vues = {k for k in cles if f".{k}}}" in t or f'"{k}"' in t}
        for nom, lues in sc.items():
            if re.search(r"\{\{[<%]\s*" + re.escape(nom) + r"\b", t):
                vues |= set(lues)
        if vues:
            out[f.relative_to(RACINE / "content").as_posix()] = sorted(vues)
    return out


def main() -> int:
    rev = sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "HEAD"
    auj = date.today().isoformat()

    if "--temoin" in sys.argv:
        cible = {"jeu": None}

        def muter(jeu, d):
            if cible["jeu"] is None and jeu == "dette_baisse":
                cible["jeu"] = jeu
                d = dict(d, affichage=dict(d["affichage"], rg_pos_n=str(d["affichage"].get("rg_pos_n")) + " (témoin)"))
            return d
        pt = pages_touchees(jeux_modifies("HEAD", muter))
        ok1 = "dette-publique-peut-elle-baisser/_index.md" in pt and "enseignants/_index.md" not in pt
        print("TÉMOIN 1 " + ("OK : la clé mutée date sa page, et elle seule parmi les pages témoins." if ok1
                             else f"EN ÉCHEC : pages trouvées {sorted(pt)}"))

        def muter_forme(jeu, d):
            if jeu == "dette_baisse":
                aff = {k: (v.replace(" ", " ") if isinstance(v, str) else v) for k, v in d["affichage"].items()}
                d = dict(d, affichage=aff)
            return d
        pt2 = pages_touchees(jeux_modifies("HEAD", muter_forme))
        ok2 = not pt2
        print("TÉMOIN 2 " + ("OK : une retouche de pure typographie (espaces insécables) ne date aucune page." if ok2
                             else f"EN ÉCHEC : la typographie seule a daté {sorted(pt2)}"))

        def muter_date(jeu, d):
            if jeu == "dette_baisse":
                d = dict(d, releve_le="2099-01-01", affichage=dict(d["affichage"], rg_pos_n="(témoin)"))
            return d
        av = releves_avances("HEAD", muter_date)
        ok3 = [x[0] for x in av] == ["dette_baisse"]
        print("TÉMOIN 3 " + ("OK : un relevé avancé sur un changement de texte seul est refusé." if ok3
                             else f"EN ÉCHEC : jeux signalés {av}"))
        return 0 if (ok1 and ok2 and ok3) else 1

    avances = releves_avances(rev)
    if avances:
        for jeu, a, n in avances:
            print(f"  RELEVÉ AVANCÉ SANS DONNÉE NOUVELLE : data/{jeu}.json, {a} → {n}")
        print("Correctif : le générateur doit passer par scripts/releve_jeu.py (releve conservé à données identiques), puis "
              "dater la page par --ecrire ou --forme.")
        return 1
    mod = jeux_modifies(rev)
    pt = pages_touchees(mod)
    reg = lire_registre()
    reg.setdefault("pages", {})
    reg.setdefault("formes", {})
    # Classification EXPLICITE (contre-expertise du 16/10, P3) : un écart qui reste après normalisation de la
    # typographie est soit de FOND (--ecrire : date la page), soit de FORME (--forme : consigné, sans date) ; jamais
    # choisi par l'outil.
    manquants = {pg: c for pg, c in pt.items()
                 if reg["pages"].get(pg, "") < auj and reg["formes"].get(pg, "") < auj}
    for opt, cle, effet in (("--ecrire", "pages", "datée(s) (fond)"), ("--forme", "formes", "classée(s) forme, sans date")):
        if opt in sys.argv:
            for pg in manquants:
                reg[cle][pg] = auj
            reg[cle] = dict(sorted(reg[cle].items()))
            REGISTRE.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"Registre : {len(manquants)} page(s) {effet} du {auj} : {', '.join(manquants) or 'aucune'}")
            return 0
    print(f"Jeux au texte modifié sans nouveau relevé (référence {rev}) : {len(mod)} ; pages qui l'affichent : {len(pt)} ; "
          f"non classées : {len(manquants)}")
    for pg, c in manquants.items():
        print(f"  À CLASSER {pg} : {', '.join(c[:4])}{' …' if len(c) > 4 else ''}")
    if manquants:
        print("Correctif : --ecrire si le texte change au fond (chiffre, rang, période, sens) ; --forme si c'est une "
              "retouche de forme (orthographe, tournure sans changement de sens). Puis, si la lecture change, `journal:`.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
