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
    """Coupe aux espaces ORDINAIRES seulement (11/10/2026) : str.split() sans argument coupait aussi a l'espace
    insecable, et rejetait « : » ou « % » seul en debut de ligne (regle typographique du site). La ponctuation haute
    francaise est d'abord soudee a ce qui la precede."""
    s = re.sub(r" ([:;?!»%])", "\u00a0\\1", s)
    s = s.replace("« ", "«\u00a0").replace("> ", ">\u00a0")
    out, cur = [], ""
    for mot in [m for m in s.split(" ") if m]:
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


# ---------------------------------------------------------------- téléphone
# Version téléphone d'une figure (300 de large, police jamais sous 13,5) : en-tête et pied communs. Nés dans
# update_dette_dynamique.py (volet 1 du dossier dette, 11/10/2026), remontés ici pour le volet 2 au lieu d'être recopiés
# (une règle, un organe). Le volet 1 garde ses deux copies tant que sa sortie n'a pas été vérifiée identique avec ces
# fonctions : point ouvert de la reprise de la refonte.
LARGEUR_M, POLICE_M = 300, 13.5


def tete_mobile(ident: str, titre: str, desc: str, encre: str, police: str, car: int = 30) -> tuple[list[str], int]:
    """Ouvre le SVG (hauteur provisoire 0, fixée par pied_mobile) et pose le titre sur plusieurs lignes."""
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" font-variant-numeric="tabular-nums" '
         'aria-labelledby="%s-t %s-d" font-family="%s">' % (LARGEUR_M, ident, ident, html.escape(police)),
         '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>'
         % (ident, html.escape(titre, quote=False), ident, html.escape(desc, quote=False)),
         '<rect width="%d" height="0" fill="#ffffff"/>' % LARGEUR_M]
    lignes = coupe(titre, car)
    for k, l in enumerate(lignes):
        e.append('<text x="0" y="%d" font-size="17" font-weight="600" fill="%s">%s</text>'
                 % (20 + 22 * k, encre, html.escape(l, quote=False)))
    return e, 20 + 22 * len(lignes)


def pied_mobile(e: list[str], y0: float, blocs, filet: str, car: int = 38) -> str:
    """blocs : [(texte, couleur, classe)] — source, précaution, licence. Ferme le SVG et fixe sa hauteur."""
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, LARGEUR_M, y0, filet))
    y = y0 + 4
    for texte, couleur, classe in blocs:
        for l in coupe(texte, car):
            y += 17
            e.append('<text class="%s" x="0" y="%.1f" font-size="%s" fill="%s">%s</text>'
                     % (classe, y, POLICE_M, couleur, html.escape(l, quote=False)))
        y += 4
    e.append("</svg>")
    h = int(round(y + 6))
    out = "\n".join(e)
    out = out.replace('viewBox="0 0 %d 0"' % LARGEUR_M, 'viewBox="0 0 %d %d"' % (LARGEUR_M, h), 1)
    return out.replace('<rect width="%d" height="0"' % LARGEUR_M, '<rect width="%d" height="%d"' % (LARGEUR_M, h), 1) + "\n"


def hors_cadre(svg: str, largeur: float, coef: float = 0.52) -> list[str]:
    """Estimation des textes qui sortent du cadre (largeur ≈ coef × police × caractères, selon l'ancrage).

    Une estimation, pas une mesure : elle signale, le rendu tranche (règle « ne jamais prédire un moteur de rendu »).
    Rend la liste des textes suspects."""
    out = []
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', svg, re.S):
        att, contenu = m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        x = re.search(r'\bx="([-0-9.]+)"', att)
        fs = re.search(r'font-size="([0-9.]+)"', att)
        if not x or not fs:
            continue
        x, l = float(x.group(1)), coef * float(fs.group(1)) * len(contenu)
        ancre = re.search(r'text-anchor="(\w+)"', att)
        ancre = ancre.group(1) if ancre else "start"
        g = x if ancre == "start" else (x - l if ancre == "end" else x - l / 2)
        if g < -1 or g + l > largeur + 1:
            out.append("%s (%.0f à %.0f sur %d)" % (contenu[:50], g, g + l, largeur))
    return out
