"""ressources_build.py -- les pages ressources dans le site CONSTRUIT : où elles sont, quel niveau, quel texte est servi.

Organe commun (industrialisation des ressources, arbitrage OPTIMUM-26 du 2026-10-11) de check-rendu-ressources.py
(chantiers 1 et 2) et de check-relecture.py (chantier 4) : les deux lisent les mêmes pages et le même texte, sinon
la relecture attestée et le contrôle du rendu ne parleraient pas du même objet.

- pages(build) : chaque page de content/ qui déclare `ressource:` (brouillons exclus), avec sa langue, son niveau
  (`ressource.refonte`, absent = pas encore refondue) et son fichier dans le build. Une page attendue absente du
  build lève une erreur : un contrôle qui ne trouverait pas la page la croirait propre.
- texte(html) : le texte servi du <main>, balises retirées, entités résolues, une ligne par bloc (paragraphe, titre,
  élément de liste, cellule, légende) ; scripts, styles, SVG en ligne, barres de navigation (<nav>) et sommaire
  replié du gabarit exclus.
- phrases(texte) : découpage en phrases (point, ? ou ! suivis d'une espace et d'une capitale, ou fin de ligne).
"""
from __future__ import annotations

import html as _html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"


def _front_matter(texte: str) -> str:
    if not texte.startswith("---"):
        return ""
    fin = texte.find("\n---", 3)
    return texte[3:fin] if fin > 0 else ""


def pages(build: Path) -> list[dict]:
    import yaml
    out = []
    for p in sorted(CONTENT.rglob("*.md")):
        fm_txt = _front_matter(p.read_text(encoding="utf-8"))
        if not re.search(r"^ressource:", fm_txt, re.M):
            continue
        fm = yaml.safe_load(fm_txt) or {}
        if fm.get("draft") is True:
            continue
        en = p.name.endswith(".en.md")
        url = fm.get("url")
        if not url:
            dossier = p.parent.relative_to(CONTENT).as_posix()
            url = ("/en/%s/" if en else "/%s/") % dossier
        fichier = build / url.strip("/") / "index.html"
        if not fichier.is_file():
            raise FileNotFoundError("page ressource absente du build : %s -> %s" % (p.relative_to(ROOT).as_posix(), fichier))
        r = fm.get("ressource") or {}
        out.append(dict(source=p.relative_to(ROOT).as_posix(), lang="en" if en else "fr", url=url, fichier=fichier,
                        refonte=None if r.get("refonte") is None else str(r.get("refonte")),
                        cle=url.strip("/").replace("/", "__") + (".en" if en and not url.startswith("/en/") else "")))
    return out


def main_html(h: str) -> str:
    m = re.search(r"<main\b[^>]*>(.*)</main>", h, re.S)
    if not m:
        raise ValueError("pas de <main> dans la page")
    return m.group(1)


_BLOC = re.compile(r"</?(?:p|h[1-6]|li|td|th|tr|figcaption|summary|blockquote|div|section|dt|dd|br|caption)\b[^>]*>", re.I)


def texte(h: str) -> str:
    c = main_html(h)
    c = re.sub(r"<(script|style|svg|template|nav)\b.*?</\1>", " ", c, flags=re.S | re.I)
    c = re.sub(r"<details class=\"?sommaire-page\b.*?</details>", " ", c, flags=re.S)  # gabarit, pas de la prose
    c = re.sub(r"<!--.*?-->", " ", c, flags=re.S)
    c = _BLOC.sub("\n", c)
    c = re.sub(r"<[^>]+>", "", c)
    c = _html.unescape(c).replace(" ", " ").replace(" ", " ")
    lignes = [re.sub(r"[ \t\r\f\v]+", " ", l).strip() for l in c.split("\n")]
    return "\n".join(l for l in lignes if l)


_COUPE = re.compile(r"(?<=[.?!…])\s+(?=[«\"“(]?[A-ZÀÂÉÈÊÎÔÛÇ0-9])")


def phrases(t: str) -> list[str]:
    out = []
    for ligne in t.split("\n"):
        out.extend(s.strip() for s in _COUPE.split(ligne) if s.strip())
    return out
