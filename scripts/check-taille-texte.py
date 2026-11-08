#!/usr/bin/env python3
"""check-taille-texte.py -- aucun texte servi sous 12 px (règle du site, acquis de la reprise du 06-08/11/2026).

MOTIF (08/11/2026). La règle était écrite dans la méthode des ressources depuis le 06/11 ; un inventaire mesuré sur les
185 pages construites a pourtant trouvé 1 233 textes visibles sous 12 px au bureau et 903 au téléphone (mentions légales,
« Réutiliser », onglets de dossier, encadré du livre, tableaux…). Cause unique : deux variables (`--fs-tiny` 11 px,
`--fs-micro` 10 px) et 29 tailles écrites en dur. Une règle de forme non contrôlée dérive : ce verrou lit la source.

Ce qu'il lit : toute déclaration `font-size` des feuilles `assets/scss/*.scss` et des gabarits `layouts/**/*.html`
(styles en ligne compris) ; px, rem (x 16) et variables `--fs-*` résolues depuis `_variables.scss`. Une valeur en `em`,
`%`, `clamp()` ou `calc()` n'est pas jugée (relative à son parent) : limite déclarée.
Ce qu'il ne voit pas : une taille obtenue par cascade d'unités relatives, un texte de SVG (règles des figures,
`check-figures.py`), la feuille d'impression (points, papier). Le contrôle navigateur reste la recette.

Exceptions : liste EXCEPTIONS ci-dessous, chacune avec son motif ; une exception devenue sans objet est signalée
« à retirer » sans bloquer.

Usage : python scripts/check-taille-texte.py [--temoin]
Sortie 0 = conforme ; 1 = au moins une taille sous 12 px hors exception.
Condition de réexamen (règle permanente, R2) : à la revue de clôture, si le contrôle n'a rien arrêté depuis six mois et que
l'inventaire navigateur reste à 0, il peut céder la place à la recette seule.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
MIN_PX = 12.0
RACINE_PX = 16.0

# (fichier relatif, fragment de la ligne) -> motif. Le fragment doit se trouver sur la ligne de la déclaration.
EXCEPTIONS = {
    ("assets/scss/_citations.scss", "&::before"): "puce décorative (glyphe U+25CF), pas un texte",
    ("assets/scss/_home.scss", ".axes-c__eti"): "étiquettes d'axe d'un SVG de l'accueil : règles des figures (check-figures)",
}
IGNORES = {"assets/scss/_print.scss"}  # feuille d'impression, en points : le papier n'est pas l'écran

DECL = re.compile(r"font-size\s*:\s*([^;}\"]+)")
VAR = re.compile(r"(--fs-[a-z0-9-]+)\s*:\s*([0-9.]+)(px|rem)\s*;")


def en_px(valeur: str, variables: dict) -> float | None:
    v = valeur.strip().replace("!important", "").strip()
    m = re.fullmatch(r"var\((--fs-[a-z0-9-]+)\)", v)
    if m:
        return variables.get(m.group(1))
    m = re.fullmatch(r"([0-9]*\.?[0-9]+)(px|rem)", v)
    if not m:
        return None  # em, %, clamp(), calc(), mots-clés : non jugés
    x = float(m.group(1))
    return x if m.group(2) == "px" else x * RACINE_PX


def variables_racine(texte: str) -> dict:
    """Valeurs des --fs-* de :root (première définition : la valeur de base, avant les surcharges de media)."""
    out = {}
    for nom, val, unite in VAR.findall(texte):
        out.setdefault(nom, float(val) * (RACINE_PX if unite == "rem" else 1.0))
    return out


def fichiers():
    for f in sorted((ROOT / "assets" / "scss").glob("*.scss")):
        yield f
    for f in sorted((ROOT / "layouts").rglob("*.html")):
        yield f


def controler(sources: dict) -> tuple[list[str], list[str]]:
    """sources : {chemin relatif : texte}. Rend (défauts, exceptions sans objet)."""
    variables = {}
    for rel, txt in sources.items():
        if rel.endswith("_variables.scss"):
            variables.update(variables_racine(txt))
    defauts, servies = [], set()
    for nom, px in variables.items():
        if px < MIN_PX:
            defauts.append("assets/scss/_variables.scss : %s = %g px (< %g)" % (nom, px, MIN_PX))
    for rel, txt in sources.items():
        if rel in IGNORES:
            continue
        for n, ligne in enumerate(txt.split("\n"), 1):
            for m in DECL.finditer(ligne):
                px = en_px(m.group(1), variables)
                if px is None or px >= MIN_PX:
                    continue
                exc = [k for k in EXCEPTIONS if k[0] == rel and k[1] in ligne]
                if exc:
                    servies.update(exc)
                    continue
                defauts.append("%s:%d : font-size %s (%g px < %g)" % (rel, n, m.group(1).strip(), px, MIN_PX))
    sans_objet = ["%s « %s »" % k for k in EXCEPTIONS if k not in servies]
    return defauts, sans_objet


def lire() -> dict:
    return {f.relative_to(ROOT).as_posix(): f.read_text(encoding="utf-8", errors="replace") for f in fichiers()}


def temoin() -> int:
    """Témoin positif : chaque forme de défaut plantée doit être arrêtée, et l'état réel ne doit rien gagner d'autre."""
    base = lire()
    cas = {
        "px en dur": ("assets/scss/_temoin.scss", ".x { font-size: 11px; }"),
        "rem en dur": ("assets/scss/_temoin.scss", ".x { font-size: 0.7rem; }"),
        "variable": ("assets/scss/_temoin.scss", ".x { font-size: var(--fs-tiny); }"),
        "style en ligne": ("layouts/partials/_temoin.html", '<span style="font-size: 10px">x</span>'),
        "!important": ("assets/scss/_temoin.scss", ".x { font-size: 11.5px !important; }"),
    }
    d0, _ = controler(base)
    rate = []
    for nom, (rel, txt) in cas.items():
        src = dict(base)
        src[rel] = txt
        if nom == "variable":  # la variable elle-même est remise sous le seuil
            v = "assets/scss/_variables.scss"
            src[v] = re.sub(r"--fs-tiny:\s*[0-9.]+px;", "--fs-tiny: 11px;", src[v], count=1)
        d, _ = controler(src)
        if len(d) <= len(d0):
            rate.append(nom)
    propre = dict(base)
    propre["assets/scss/_temoin.scss"] = ".x { font-size: 12px; } .y { font-size: 0.75rem; } .z { font-size: 0.9em; }"
    if len(controler(propre)[0]) != len(d0):
        rate.append("cas propre arrêté à tort")
    if rate:
        print("Temoin check-taille-texte : ECHEC, cas non arretes : %s" % ", ".join(rate))
        return 1
    print("Temoin check-taille-texte : chaque forme de defaut est arretee, le cas propre passe. OK")
    return 0


def main() -> int:
    if "--temoin" in sys.argv[1:]:
        return temoin()
    defauts, sans_objet = controler(lire())
    for e in sans_objet:
        print("  exception sans objet, a retirer : %s" % e)
    for d in defauts:
        print("  " + d)
    if defauts:
        print("Taille de texte : %d declaration(s) sous %g px. ECHEC" % (len(defauts), MIN_PX))
        return 1
    print("Taille de texte : aucune declaration sous %g px hors exceptions (%d). OK" % (MIN_PX, len(EXCEPTIONS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
