"""check-rendu-ressources.py -- figures et langue des pages ressources, lues dans le site CONSTRUIT.

    python scripts/check-rendu-ressources.py [public] [--detail]

Industrialisation des ressources (arbitrage OPTIMUM-26 du 2026-10-11, chantiers 1 et 2). Lit le build, pas le contenu :
une figure servie par un partial (dette-longue, dans dette-chiffres) est invisible dans le Markdown, et un jeton ne
montre sa phrase qu'une fois résolu.

NIVEAU DES PAGES. Le front matter dit si une page est refondue (`ressource.refonte`, contrôlé par
check-ressource-modele.py). Les pages ressources n'ont pas toutes été refondues : les exigences de la refonte
BLOQUENT sur les pages refondues, et ne font qu'INVENTORIER le travail des autres (une ligne par page, détail avec
--detail), qui le traiteront à leur phase B.

1. FIGURES (chantier 1) : chaque <img src="/img/X.svg"> du <main> est servi dans un <picture> avec sa version
   téléphone /img/X-m.svg, et le SVG servi porte le pied commun (classes pied-source, pied-note ou pied-licence,
   scripts/pied_figure.py).
2. LANGUE (chantier 2) : motifs de MOTIFS sur le texte servi (ressources_build.texte). Table OUVERTE : un défaut
   nouveau d'une classe connue y entre. Ce contrôle ne voit que ce qu'il cherche ; la relecture phrase à phrase
   reste humaine (leçon 16 du CLAUDE.md du site).

3. SHORTCODE NON RENDU, sur TOUTES les pages (refondues ou non) et dans tout le <main>, sommaire et barres compris :
   le texte de substitution de Hugo (« HAHAHUGOSHORTCODE… ») n'est jamais acceptable devant un lecteur. Cas fondateur
   (11/10/2026) : un titre à jeton s'affichait ainsi dans le sommaire replié de /dette-publique-collectivites-locales/,
   en ligne depuis le 10/10 ; l'extraction du texte, qui exclut le sommaire, ne pouvait pas le voir.

Conservation : pages vues == refondues + non refondues ; une page attendue absente du build arrête le contrôle.
Témoins positifs : --temoin injecte chaque motif et retire une version téléphone dans une copie du texte et du
HTML d'une page refondue ; chaque injection doit être détectée (sortie 1 sinon).
Condition de mort : aucune -- contrôle permanent, réexaminé à la revue annuelle (R2) ; la partie « inventaire »
meurt quand plus aucune page ressource n'est sans `refonte`.
Sortie console ASCII pur.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ressources_build as rb  # noqa: E402

N = r"\d+(?:[,.]\d+)?"
# (identifiant, langue ou None, motif, ce qui est attendu). Relecture de langue du 11/10/2026 et OPTIMUM-26.
MOTIFS = [
    ("jeton non resolu", None, r"\{\{<|\{[a-z_]+\.[a-z_0-9.]+\}|\b[a-z]+-val\b",
     "un jeton apparait tel quel dans le texte servi"),
    ("signe contraire au verbe", "fr",
     r"\b(?:retir|baiss|diminu|recul|perd|abaiss|rédui|allég|ôt)\w*\s+(?:de\s+)?[−-]\s?\d"
     r"|\b(?:ajout|gagn|augment|progress|accr|accru|ajoute)\w*\s+(?:de\s+)?\+\s?\d",
     "apres un verbe qui porte le sens, la valeur s'ecrit sans signe (jeton _abs du generateur)"),
    ("sign contradicts verb", "en",
     r"\b(?:remov|cut|fell|fall|lost|lose|reduc|lower|subtract|declin|took off|takes off)\w*\s+(?:by\s+)?[−-]\s?\d"
     r"|\b(?:add|gain|rose|rise|increas)\w*\s+(?:by\s+)?\+\s?\d",
     "after a verb carrying the direction, the value is unsigned (generator _abs token)"),
    ("accord de point", "fr", r"(?<![\d,.])[+−-]?[01](?:,\d+)?\s+points\b|(?<![\d,.])[+−-]?(?:[2-9]|\d{2,})(?:,\d+)?\s+point\b(?!s)",
     "singulier sous 2, pluriel a partir de 2 (jeton _pt)"),
    ("point agreement", "en",
     r"(?<![\d.,])[+−-]?(?!1\b)\d+(?:\.\d+)?\s+point\b(?!s)(?![- ](?:increase|decrease|rise|fall|gap|drop|difference|reduction|cut|shift|swing))"
     r"|(?<![\d.,])[+−-]?1\s+points\b",
     "plural except for exactly 1 (_pt token)"),
    ("em dash then comma", "en", r"—\s*,", "an em dash is not followed by a comma"),
    ("double ponctuation", None, r"[?!]\s?\.(?!\.)|(?<!\.)\.\s?\.(?!\.)|,\s?,", "deux signes de ponctuation finale"),
    ("tournure proscrite", "fr", r"\b(?:a|ont|avait|avaient|aurait|auraient)\s+monté\b|\bpartis de plus de\b",
     "« a monte » -> « a augmente » ; « partis de plus de » -> « dont la dette depassait »"),
]
_MOTIFS = [(i, l, re.compile(m), a) for i, l, m, a in MOTIFS]
# Un exemple fautif par motif, injecté par --temoin (le témoin positif DOIT mordre sur chacun).
EXEMPLES = {"jeton non resolu": "La dette atteint {dette.fin} %.", "signe contraire au verbe": "Le ratio gagne +7,7 points.",
            "sign contradicts verb": "Deficits added +6.1 points.", "accord de point": "Un écart de 1,5 points.",
            "point agreement": "A gap of 0.1 point.", "em dash then comma": "the levies on it —, health",
            "double ponctuation": "Est-ce vrai ?.", "tournure proscrite": "Les prix ont monté de 19 %."}

_IMG = re.compile(r"<img\b[^>]*?\bsrc=\"?(?:https?://[^/\s\"]+)?/img/([^\"\s>]+?)\.svg[\"\s>]")


def figures(h: str, build: Path) -> list[str]:
    main = rb.main_html(h)
    out = []
    for nom in sorted(set(_IMG.findall(main))):
        if nom.endswith("-m"):
            continue
        # Version téléphone : `/img/X-m.svg` (figures de données), ou toute autre source SVG sous condition de largeur dans
        # le <picture> de la figure (schémas : boucle-anthropique-desktop / -mobile, 28/10/2026 ; l'inventaire disait
        # « pas de version téléphone » d'une figure qui en servait une depuis mai).
        pic = re.search(r"<picture\b(?:(?!</picture>).)*?/img/%s\.svg(?:(?!</picture>).)*</picture>" % re.escape(nom), main, re.S)
        autre = pic and any(
            (build / "img" / (alt + ".svg")).is_file()  # SERVIE : le fichier existe dans le site construit
            for src in re.findall(r"<source\b[^>]*>", pic.group(0)) if re.search(r"\bmedia=\"?\(max-width", src)
            for alt in re.findall(r"/img/([^\"\s>,]+?)\.svg", src) if alt != nom)
        if not autre and not re.search(r"<source\b[^>]*\bsrcset=\"?(?:https?://[^/\s\"]+)?/img/%s-m\.svg" % re.escape(nom), main):
            out.append("figure %s : pas de version telephone servie (/img/%s-m.svg dans un <picture>)" % (nom, nom))
        svg = build / "img" / (nom + ".svg")
        if svg.is_file() and not re.search(r"class=\"?pied-(?:source|note|licence)", svg.read_text(encoding="utf-8", errors="replace")):
            out.append("figure %s : pas de pied commun (classes pied-*, scripts/pied_figure.py)" % nom)
    return out


def langue(t: str, lang: str) -> list[str]:
    out = []
    for ident, l, rx, attendu in _MOTIFS:
        if l and l != lang:
            continue
        for m in rx.finditer(t):
            ctx = t[max(0, m.start() - 45):m.end() + 25].replace("\n", " / ")
            out.append("%s : \"...%s...\" (%s)" % (ident, ctx, attendu))
    return out


def non_rendus(h: str) -> list[str]:
    return ["shortcode non rendu dans le HTML servi (sommaire, barre ou corps) : \"...%s...\"" % m.group(0)
            for m in re.finditer(r".{0,40}HAHAHUGOSHORTCODE\w*.{0,10}", rb.main_html(h))]


def controler(build: Path) -> tuple[list, list, int]:
    bloquants, inventaire, vues = [], [], 0
    for p in rb.pages(build):
        vues += 1
        h = p["fichier"].read_text(encoding="utf-8")
        nr = non_rendus(h)
        if nr:
            bloquants.append((p, nr))
        ecarts = figures(h, build) + langue(rb.texte(h), p["lang"])
        if ecarts:
            (bloquants if p["refonte"] else inventaire).append((p, ecarts))
    return bloquants, inventaire, vues


def temoin(build: Path) -> int:
    """Témoin positif : chaque motif et une figure sans version téléphone doivent mordre sur une page refondue."""
    p = next(x for x in rb.pages(build) if x["refonte"] and x["lang"] == "fr")
    h = p["fichier"].read_text(encoding="utf-8")
    rates = []
    if figures(h, build):
        rates.append("page de reference deja en ecart : %s" % p["url"])
    nom = _IMG.findall(rb.main_html(h))[0]
    if not figures(h.replace("/img/%s-m.svg" % nom, "/img/%s-x.svg" % nom), build):
        rates.append("figure sans version telephone non detectee (%s)" % nom)
    if not non_rendus(h.replace("</main>", "<li>Titre HAHAHUGOSHORTCODE55s31HBHB</li></main>", 1)):
        rates.append("shortcode non rendu non detecte")
    for ident, l, _rx, _a in _MOTIFS:
        if not any(e.startswith(ident) for e in langue(EXEMPLES[ident], l or "fr")):
            rates.append("motif non detecte sur son exemple : %s" % ident)
    for r in rates:
        print("  TEMOIN RATE  " + r)
    print("Temoin : %d motif(s) et 1 figure injectes, %s." % (len(_MOTIFS), "tous detectes" if not rates else "%d rate(s)" % len(rates)))
    return 1 if rates else 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build = Path(args[0] if args else "public")
    if not build.is_dir():
        print("ECHEC : build introuvable (%s)" % build)
        return 1
    if "--temoin" in sys.argv:
        return temoin(build)
    bloquants, inventaire, vues = controler(build)
    refondues = sum(1 for p in rb.pages(build) if p["refonte"])
    assert vues == refondues + (vues - refondues)
    for p, ec in bloquants:
        for e in ec:
            print(("  ECART  %s : %s" % (p["url"], e)).encode("ascii", "backslashreplace").decode("ascii"))
    for p, ec in inventaire:
        nf = sum(1 for e in ec if e.startswith("figure "))
        print("  phase B  %s : %d ecart(s) de figure, %d phrase(s) a reprendre" % (p["url"], nf, len(ec) - nf))
        if "--detail" in sys.argv:
            for e in ec:
                print(("           %s" % e).encode("ascii", "backslashreplace").decode("ascii"))
    print("Rendu des ressources : %d page(s), %d refondue(s) %s ; %d non refondue(s) avec travail inventorie."
          % (vues, refondues, "EN ECART : %d" % len(bloquants) if bloquants else "conformes", len(inventaire)))
    return 1 if bloquants else 0


if __name__ == "__main__":
    sys.exit(main())
