#!/usr/bin/env python3
"""Règles typographiques du site, appliquées et contrôlées sur le HTML FINAL (auteur, 01/11/2026 : « ces règles doivent
être appliquées de façon constante »).

MOTIF. Mesuré le 01/11/2026 sur le texte servi : 752 espaces ordinaires devant la ponctuation haute, 372 chiffres
séparables de leur mot, 3 940 apostrophes droites en français, des guillemets français et des « DOI : » sur les pages
anglaises, des titres d'œuvres en romain. Ces textes viennent du front matter, des données, des générateurs et des
gabarits : check-typo-fr.py ne lit que le corps des .md et l'anglais n'avait aucun organe. Une correction source par
source redériverait à chaque mise à jour des données ; ici, la règle s'applique à tout ce qui sort, d'où qu'il vienne.

CE QUI EST TOUCHÉ : les seuls nœuds de texte du <body>, selon la langue de l'élément (lang, héritée). Jamais les
attributs, <head>, script, style, code, pre, textarea, svg. Idempotent. Les titres : data/titres_oeuvres.json.
Une citation française sur une page anglaise prend les guillemets et les espaces anglais ; ses mots ne changent pas.

Hors champ, déclaré : balises <title> et meta (texte brut, sans italique ni coupure de ligne), flux RSS, images SVG et
PNG (chaque générateur en répond), mots étrangers en italique, ponctuation manquante d'une citation anglaise sur une
page française non balisée (indécidable par motif).

Usage : python scripts/typo_build.py <build>             applique, puis contrôle (sortie 1 s'il reste un défaut)
        python scripts/typo_build.py <build> --controle  contrôle seul
        python scripts/typo_build.py --temoin            témoin positif
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
NB, FINE = " ", " "
BLANC = f"[ \\n\\t{NB}{FINE}]"
BRUT = {"script", "style", "code", "pre", "textarea", "svg", "title", "head", "template", "math"}
VIDES = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
ITALIQUES = {"em", "i", "cite"}
BALISE = re.compile(r"""<!--.*?-->|<!\w[^>]*>|<(/?)([a-zA-Z][a-zA-Z0-9-]*)((?:[^>"']|"[^"]*"|'[^']*')*)>""", re.S)
LANG = re.compile(r"""(?:^|\s)lang=["']?([a-zA-Z]{2})""")
MOIS = "janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre"
MOTS = (r"milliards?|millions?|milliers|points?|pages?|ans|euros?|dollars?|siècles?|mois|jours|heures|km|kg|ha|kWh|MWh|GWh"
        r"|TWh|GW|MW|Mt|Gt|Md€|M€|k€|m²|m³|°C")
UNITE = re.compile(rf"(?<=\d) (?=(?:%|€|\$|£|{MOTS})(?![\w]))")
DATE = re.compile(rf"(?<=\d) (?=(?:{MOIS})\b)|(?<=\b1er) (?=(?:{MOIS})\b)")
MILLIERS = re.compile(r"(?<![\d,.])\d{1,3}(?: \d{3})+(?!\d)")
PREFIXE = re.compile(r"(\b[nN]°|§|\bpp?\.|\b[aA]rt\.) (?=\d)")


def apostrophes(t: str) -> str:
    return re.sub(r"(?<=\w)'(?=[\w«]|$)", "’", t)


def paires(t: str, ouvre: str, ferme: str) -> str:
    """Guillemets droits, seulement par paires : un guillemet isolé reste visible pour le contrôle."""
    if not t.count('"') or t.count('"') % 2:
        return t
    m = t.split('"')
    return "".join(x + ("" if i == len(m) - 1 else ouvre if i % 2 == 0 else ferme) for i, x in enumerate(m))


def fr(t: str) -> str:
    t = apostrophes(paires(t, f"«{NB}", f"{NB}»"))
    t = re.sub(r"(?:(?<=\S)|^)[ \n\t]+(?=[;:!?»])", NB, t)
    t = re.sub(r"«[ \n\t]+", f"«{NB}", t)
    t = re.sub(rf"«(?=[^{NB}{FINE}\s])", f"«{NB}", t)
    t = re.sub(rf"(?<=[^{NB}{FINE}\s«])»", f"{NB}»", t)
    t = re.sub(r"(?<=\S) (—|–) ", rf"{NB}\1 ", t)
    t = t.replace("...", "…")
    t = re.sub(rf"(?<=[\s(≈])-(?=\d)", "−", t)
    t = UNITE.sub(NB, t)
    t = DATE.sub(NB, t)
    t = MILLIERS.sub(lambda m: m.group(0).replace(" ", NB), t)
    return PREFIXE.sub(lambda m: m.group(1) + NB, t)


def en(t: str) -> str:
    t = apostrophes(paires(t, "“", "”"))
    t = re.sub(rf"«{BLANC}*", "“", t)
    t = re.sub(rf"{BLANC}*»", "”", t)
    t = re.sub(rf"{BLANC}+(?=[;:!?](?:{BLANC}|$|[”)\]]))", "", t)
    t = t.replace(FINE, " ")
    t = re.sub(rf"(?<=\d){BLANC}+%", "%", t)
    t = t.replace("...", "…")
    return PREFIXE.sub(lambda m: m.group(1) + NB, t)


class Titres:
    def __init__(self, f: Path):
        d = json.loads(f.read_text(encoding="utf-8"))
        self.exempt = set(d["sans_italique_si_seul_dans"])
        self.jamais = set(d["jamais_dans"])
        def souple(s):
            return "".join({" ": f"{BLANC}+", "’": "['’]"}.get(c, re.escape(c)) for c in s)
        self.variantes = [(re.compile(rf"(?<!\w){souple(a)}(?!\w)"), b) for a, b in d["variantes"].items()]
        tous = sorted(d["titres"], key=len, reverse=True)
        self.motif = re.compile("|".join([rf"(?<![\w-]){souple(t)}(?![\w])" for t in tous] + d.get("motifs", [])))
        self.liste = {self.normal(t) for t in tous}

    @staticmethod
    def normal(s: str) -> str:
        return re.sub(rf"{BLANC}+", " ", s.replace("'", "’")).replace(" ?", "?").strip()

    def corrige(self, t: str) -> str:
        for m, b in self.variantes:
            t = m.sub(b, t)
        return t


class Pile:
    """Éléments ouverts et langue courante, seul suivi d'état, partagé par la transformation et le contrôle."""

    def __init__(self):
        self.p, self.lang = [], "fr"

    def noms(self):
        return [b for b, _ in self.p]

    def langue(self):
        return next((l for _, l in reversed(self.p) if l), self.lang)

    def lit(self, m):
        nom, attrs = m.group(2).lower(), m.group(3) or ""
        l = LANG.search(attrs)
        if nom == "html":
            self.lang = l.group(1).lower() if l else self.lang
        elif m.group(1):
            for i in range(len(self.p) - 1, -1, -1):
                if self.p[i][0] == nom:
                    del self.p[i:]
                    break
        elif nom not in VIDES and not attrs.rstrip().endswith("/"):
            self.p.append((nom, l.group(1).lower() if l else None))


def transformer(html: str, titres: Titres) -> str:
    sortie, pile, pos = [], Pile(), 0

    def texte(brut: str) -> str:
        ouverts = pile.noms()
        if not brut.strip() or "body" not in ouverts or any(b in BRUT for b in ouverts):
            return brut
        t = brut.replace("&#39;", "'").replace("&#34;", '"').replace("&quot;", '"').replace("&nbsp;", NB)
        t = titres.corrige(t)
        t = (fr if pile.langue() == "fr" else en)(t)
        if any(b in ITALIQUES or b in titres.jamais for b in ouverts):
            return t
        parent = next((b for b in reversed(ouverts) if b not in {"a", "span", "strong"}), "")
        if parent in titres.exempt and titres.normal(t) in titres.liste:
            return t
        return titres.motif.sub(lambda m: f"<em>{m.group(0)}</em>", t)

    for m in BALISE.finditer(html):
        sortie.append(texte(html[pos:m.start()]))
        sortie.append(m.group(0))
        pos = m.end()
        if m.group(2):
            pile.lit(m)
    sortie.append(html[pos:])
    return "".join(sortie)


# Contrôle : relit le résultat par blocs, y compris les signes à cheval sur deux balises.
BLOC = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "figcaption", "blockquote", "summary", "dd", "dt", "div",
        "section", "article", "aside", "header", "footer", "main", "nav", "ul", "ol", "table", "tr", "figure", "details", "br"}
DEFAUTS = {
    "fr": [("espace devant la ponctuation haute", re.compile(r"(?<=\S) (?=[;:!?»])")),
           ("espace après «", re.compile(r"« ")),
           ("chiffre séparé de son unité", re.compile(rf"\d (?:%|€|{MOTS})(?![\w])")),
           ("milliers", re.compile(r"(?<![\d,.])\d{1,3} \d{3}(?!\d)")),
           ("guillemet droit", re.compile(r'"')),
           ("apostrophe droite", re.compile(r"\w'\w"))],
    "en": [("espace devant la ponctuation", re.compile(rf"[ {NB}{FINE}][;:!?](?=\s|$)")),
           ("guillemet français", re.compile(r"[«»]")),
           ("espace devant %", re.compile(rf"\d[ {NB}{FINE}]%")),
           ("guillemet droit", re.compile(r'"')),
           ("apostrophe droite", re.compile(r"\w'\w"))],
}


def blocs(html: str):
    """Rend (langue, texte) par bloc, hors zones brutes."""
    pile, pos, cour, lg = Pile(), 0, [], None
    for m in BALISE.finditer(html):
        brut = html[pos:m.start()]
        pos = m.end()
        ouverts = pile.noms()
        if brut and "body" in ouverts and not any(b in BRUT for b in ouverts):
            if cour and pile.langue() != lg:          # fragment d'une autre langue : jugé selon SA langue
                yield lg, "".join(cour)
                cour = []
            lg = pile.langue()
            cour.append(brut.replace("&nbsp;", NB))
        if not m.group(2):
            continue
        if m.group(2).lower() in BLOC and cour:
            yield lg, "".join(cour)
            cour = []
        pile.lit(m)
    if cour:
        yield lg, "".join(cour)


def defauts(html: str):
    for lg, s in blocs(html):
        for nom, r in DEFAUTS.get(lg, []):
            for m in r.finditer(s):
                yield lg, nom, s[max(0, m.start() - 40):m.end() + 30].replace("\n", " ")


def temoin(titres: Titres) -> int:
    brut_fr = """<html lang=fr><body><p>Coût : 3 536,1 milliards, soit 5 %, l'an 1 234 ; "oui" ? Livresque des mots <em>Candide</em></p></body></html>"""
    brut_en = "<html lang=en><body><p>DOI : « yes » 5 % <a>Livresque des mots</a></p></body></html>"
    brut_zone = """<html lang=fr><body><code>a : b</code><a title="x : y">z</a><script>a ? b : c</script></body></html>"""
    a, b = transformer(brut_fr, titres), transformer(brut_en, titres)
    essais = {
        "fr insecables": all(x in a for x in (f"Coût{NB}:", f"536,1{NB}milliards", f"5{NB}%", f"1{NB}234{NB};")),
        "fr apostrophe et guillemets": "l’an" in a and f"«{NB}oui{NB}»" in a,
        "fr titre": "<em>Livresque des mots</em>" in a and "<em><em>" not in a,
        "en": "DOI:" in b and "“yes”" in b and "5%" in b and "<em>Livresque" in b,
        "idempotence": transformer(a, titres) == a and transformer(b, titres) == b,
        "zones brutes": transformer(brut_zone, titres) == brut_zone,
        "le controle mord": len(list(defauts(brut_fr))) >= 4 and len(list(defauts(brut_en))) >= 3,
        "resultat propre": not list(defauts(a)) and not list(defauts(b)),
    }
    for k, v in essais.items():
        print(f"  {k} : {'ok' if v else 'ECHEC'}")
    return 0 if all(essais.values()) else 1


def main() -> int:
    a = sys.argv[1:]
    titres = Titres(RACINE / "data" / "titres_oeuvres.json")
    if "--temoin" in a:
        return temoin(titres)
    cibles = [x for x in a if not x.startswith("--")]
    if len(cibles) != 1:
        print(__doc__)
        return 2
    build = Path(cibles[0])
    fichiers = [f for f in build.rglob("*.html") if f.is_file()]
    if not fichiers:
        print(f"typo_build : aucun HTML dans {build}")
        return 2
    if "--controle" not in a:
        n = 0
        for f in fichiers:
            h = f.read_text(encoding="utf-8")
            r = transformer(h, titres)
            if r != h:
                f.write_text(r, encoding="utf-8", newline="")
                n += 1
        print(f"typo_build : {n} page(s) corrigee(s) sur {len(fichiers)}.")
    total = 0
    for f in fichiers:
        for lg, nom, ex in defauts(f.read_text(encoding="utf-8")):
            total += 1
            if total <= 60:
                print(f"  {f.relative_to(build).as_posix()} [{lg}] {nom} : ...{ex}...")
    print(f"typo_build : {total} defaut(s) restant(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
