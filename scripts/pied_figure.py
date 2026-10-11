"""pied_figure.py -- pied des figures détaillées (720 de large) : source, précaution, licence.

Organe commun (11/10/2026), né de la contre-expertise de la page « Professeurs » : à 9 px dans une figure de 720, le
pied tombait à 8,1 px affichés sur une tablette de 768 px (figure réduite à 649 px). Il passe à 11 px et va à la ligne
dans la largeur de la figure ; la hauteur du SVG suit. Les lignes portent une classe (pied-source, pied-note,
pied-licence) : les fiches « Réutiliser » les relisent par classe, plus par la taille de police.

Adopté par update_langue_eleves.py, update_niveau_eleves.py, update_lycee_professeurs.py (générateurs à extrait figé,
relançables sans réseau). Les autres générateurs l'adoptent à la phase B de leur ressource (méthode de la refonte),
quand leurs figures sont reprises : jamais par une régénération en masse qui tirerait des données nouvelles en silence.
"""
from __future__ import annotations

import html
import re

TAILLE, INTERLIGNE, CARACTERES = 11, 14, 118


def coupe(s: str, n: int) -> list[str]:
    out, cur = [], ""
    for mot in s.split():
        if cur and len(cur) + 1 + len(mot) > n:
            out.append(cur)
            cur = mot
        else:
            cur = (cur + " " + mot).strip()
    return out + ([cur] if cur else [])


def pied(e: list[str], y0: float, largeur: int, blocs, filet: str) -> str:
    """blocs : [(texte, couleur, classe)] dans l'ordre source, précaution, licence. Ferme le SVG et ajuste sa hauteur."""
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, largeur, y0, filet))
    y = y0 + 1
    for texte, couleur, classe in blocs:
        for ligne in coupe(texte, CARACTERES):
            y += INTERLIGNE
            e.append('<text class="%s" x="0" y="%.1f" font-size="%d" fill="%s">%s</text>'
                     % (classe, y, TAILLE, couleur, html.escape(ligne, quote=False)))
    e.append("</svg>")
    h = int(round(y + 8))
    s = "\n".join(e)
    s = re.sub(r'viewBox="0 0 %d [0-9.]+"' % largeur, 'viewBox="0 0 %d %d"' % (largeur, h), s, count=1)
    return re.sub(r'<rect width="%d" height="[0-9.]+"' % largeur, '<rect width="%d" height="%d"' % (largeur, h), s, count=1)


def lire(svg: str, classe: str) -> str:
    """Texte d'un bloc du pied, lignes rejointes (fiches « Réutiliser »)."""
    return " ".join(html.unescape(t) for t in re.findall(r'<text class="%s"[^>]*>(.*?)</text>' % classe, svg))


def hauteur(svg: str, largeur: int) -> str:
    return re.search(r'viewBox="0 0 %d ([0-9.]+)"' % largeur, svg).group(1)


def controler_page(page_md: str, figs: dict) -> list[str]:
    """Hauteurs déclarées dans la page (<img … width height>, <source srcset … width height>) contre celles des SVG.

    Les dimensions sont recopiées dans la page pour réserver la place avant chargement ; une figure qui change de hauteur
    doit les faire suivre. Mesure fondatrice (11/10/2026) : 6 hauteurs sur 24 avaient déjà dérivé sur Langue, Niveau et
    Professeurs (niveau-composition : 288 déclarés pour 352). Rend la liste des écarts ; vide = conforme."""
    ecarts = []
    for nom, svg in figs.items():
        if not nom.endswith(".svg"):
            continue
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
        w, h = m.group(1), m.group(2)
        motif = (r'<source [^>]*srcset="/img/%s" width="%s" height="(\d+)"' if nom.endswith("-m.svg")
                 else r'<img src="/img/%s" alt=".*?" width="%s" height="(\d+)"') % (re.escape(nom), w)
        d = re.search(motif, page_md, re.S)
        if d is None:
            ecarts.append("%s : absente de la page ou largeur %s non déclarée" % (nom, w))
        elif d.group(1) != h:
            ecarts.append("%s : hauteur %s dans la page, %s dans le SVG" % (nom, d.group(1), h))
    return ecarts


def parite(svg_detaille: str, svg_mobile: str, fs_min: float, couleurs=()) -> list[str]:
    """Version téléphone contre version détaillée : chaque nombre dessiné en mobile (textes en gras ou dans une des
    couleurs données) figure dans la description de la détaillée ; aucune police sous fs_min. Rend la liste des écarts.

    Généralisation du contrôle de la page « Professeurs » (11/10/2026), vu mordre sur une valeur faussée et une police
    trop petite. Un contrôle qui ne lit aucun nombre est aveugle : il échoue."""
    desc = html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_detaille, re.S).group(1))
    nombres = set(re.findall(r"\d+(?:[,.]\d+)?", desc))
    textes = re.findall(r'<text [^>]*font-weight="600"[^>]*>([^<]*)</text>', svg_mobile)
    for c in couleurs:
        textes += re.findall(r'<text [^>]*fill="%s"[^>]*>([^<]*)</text>' % re.escape(c), svg_mobile)
    dessines = {n for t in textes for n in re.findall(r"\d+(?:[,.]\d+)?", html.unescape(t)) if not re.fullmatch(r"(19|20)\d\d", n)}
    ecarts = []
    if not dessines:
        ecarts.append("aucune valeur dessinée lue (contrôle aveugle)")
    manquants = dessines - nombres
    if manquants:
        ecarts.append("valeurs dessinées absentes de la version détaillée : %s" % sorted(manquants))
    tailles = [float(x) for x in re.findall(r'font-size="([0-9.]+)"', svg_mobile)]
    if tailles and min(tailles) < fs_min:
        ecarts.append("police %.1f sous le minimum %.1f" % (min(tailles), fs_min))
    return ecarts
