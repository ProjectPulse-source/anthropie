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

# Texte des figures : encre atténuée et police minimale (11/11/2026). Une valeur, un organe : les générateurs les
# importent, ils ne les recopient pas.
# - ENCRE_ATTENUEE : graduations, crédit, valeurs d'une série grise. 5,23:1 sur blanc, 4,65:1 sur le plus foncé des
#   fonds teintés en usage (#f3f2ee). Elle remplace les gris #96928f (3,09:1) et #898781 (3,59:1) pour le TEXTE
#   seulement : une marque grise (barre, point, filet) garde son gris, qui n'a besoin que de 3:1.
# - POLICE_MIN : plus petite police d'une figure détaillée (720 de large). Mesure du 11/11/2026 sur les 52 pages : la
#   version détaillée est servie à partir de 900 px d'écran et s'y affiche à 786 px au plus étroit (bloc « dette en
#   chiffres » ; 804 px dans un repli) ; 11 px déclarés y font 12,0 px, 10,5 px n'en font que 11,5. La version téléphone (300 de large) s'affiche à 277 px
#   au plus étroit (320 px d'écran) : POLICE_M_MIN = 13 y fait 12,0 px. Contrôle : check-figures.py, règles R6 et R7.
ENCRE_ATTENUEE = "#6f6c66"
POLICE_MIN, POLICE_M_MIN = 11, 13

# Texte écrit dans la couleur d'une série ORANGE (décision de l'auteur, 11/11/2026 : « Je valide l'orange foncé pour le
# texte »). L'orange de la charte (#eb6834) ne fait que 3,20:1 sur blanc : il reste la couleur des MARQUES (barres,
# courbes, points) ; le TEXTE de la même série s'écrit en ORANGE_TEXTE, 5,49:1 sur blanc et 5,0:1 sur les fonds
# teintés. Passé à validate_palette.js avec le bleu de la charte : toutes vérifications tenues. L'orange atténué des
# repères anciens (#b8703f, 3,87:1) prend la même encre : un second orange de texte ne se distinguerait pas du premier
# (écart de 6,9, seuil 15) ; la distinction récent / ancien reste portée par les marques et par la graisse.
ORANGE_TEXTE = "#b8420f"
_ENCRE_DE_SERIE = {"#eb6834": ORANGE_TEXTE, "#b8703f": ORANGE_TEXTE,
                   "#96928f": ENCRE_ATTENUEE, "#898781": ENCRE_ATTENUEE, "#8a8781": ENCRE_ATTENUEE,
                   "#8a8f98": ENCRE_ATTENUEE, "#a5a39a": ENCRE_ATTENUEE}


# Texte posé SUR une marque pleine, barre ou pastille (décision de l'auteur, 11/11/2026 : « Je valide l'encre foncée sur
# les marques orange et grises »). Le blanc ne fait que 3,2:1 sur l'orange et 3,3 à 3,6:1 sur les gris de marque ; il
# reste sur le bleu (8,2:1). Ailleurs le texte s'écrit à l'encre la plus foncée : 6,2:1 sur l'orange, 5,5:1 sur le gris
# (#26262f n'y ferait que 4,2:1).
ENCRE_SUR_MARQUE = "#0A0A0E"


def _luminance(c: str) -> float:
    v = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]


def contraste(a: str, b: str) -> float:
    la, lb = _luminance(a), _luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def encre_sur(fond: str) -> str:
    """Couleur du TEXTE posé sur une marque de couleur `fond` (#rrggbb) : le blanc s'il y fait 4,5:1 au moins (bleu de la
    charte), sinon l'encre la plus foncée. À appeler là où un texte est écrit DANS une barre, un segment ou une pastille."""
    return "#ffffff" if contraste("#ffffff", fond) >= 4.5 else ENCRE_SUR_MARQUE


def encre_texte(couleur: str) -> str:
    """Couleur du TEXTE pour une couleur de série : l'orange et le gris des marques ont chacun leur encre, plus foncée ;
    toute autre couleur (bleu, encres) s'écrit telle quelle. À appeler là où un texte reçoit la couleur de sa série ;
    la marque, elle, garde la couleur d'origine."""
    return _ENCRE_DE_SERIE.get((couleur or "").lower(), couleur)


def coupe(s: str, n: int) -> list[str]:
    """Coupe aux espaces ORDINAIRES seulement (11/10/2026) : str.split() sans argument coupait aussi a l'espace
    insecable, et rejetait « : » ou « % » seul en debut de ligne (regle typographique du site). La ponctuation haute
    francaise est d'abord soudee a ce qui la precede."""
    s = re.sub(r" ([:;?!»%])", "\u00a0\\1", s)
    s = s.replace("« ", "«\u00a0").replace("> ", ">\u00a0")
    # Soudures reprises des copies locales des générateurs promesses (03/11/2026 : cinq copies de coupe() ramenées à
    # cet organe ; l'une rejetait « ; CREDOC » en début de ligne) : « n° », abréviation + numéro, nombre + mois ou unité.
    s = s.replace("n° ", "n°\u00a0")
    s = re.sub(r"\b(art\.|al\.|no\.|para\.) (\d)", "\\1\u00a0\\2", s)
    s = re.sub(r"(\d) (January|February|March|April|May|June|July|August|September|October|November|December|ans|years|places)\b",
               "\\1\u00a0\\2", s)
    # Nombre + « point(s) », « pb », « basis points », et mois français (09/11/2026, contrôleurs des figures « Quels
    # futurs ? » : « 1 / point », « 20 basis / points », « d'octobre / 2024 »).
    s = re.sub(r"(\d) (points?|pb|percentage|basis)\b", "\\1\u00a0\\2", s)
    s = re.sub(r"\b(basis|percentage) (points?)\b", "\\1\u00a0\\2", s)
    s = re.sub(r"\b(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre) (\d{4})\b",
               "\\1\u00a0\\2", s)
    # Même soudure pour les mois anglais (11/11/2026, contrôle du rendu : « 8 September / 2025 », sept coupures de ce
    # genre dans six figures anglaises).
    s = re.sub(r"\b(January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})\b",
               "\\1\u00a0\\2", s)
    # Sigle + année et année + nom qu'elle qualifie (« DSM / 2025 », « 2027 / draft budget », « 2024 / commitment »).
    s = re.sub(r"\b(DSM|PLF|PSMT|PLFSS|LFI|LFSS) (\d{4})\b", "\\1\u00a0\\2", s)
    s = re.sub(r"\b(\d{4}) (draft|commitment|plan|budget)\b", "\\1\u00a0\\2", s)
    # Nombre et unité, jour et mois, groupes de milliers, parenthèse et son nombre (11/11/2026 : relevé sur les 277
    # figures après le passage du texte à 11 px — « environ 90 / Md€ », « −2,9 / pts », « 1,1 à 1,6 / fois »,
    # « le 8 / septembre 2025 », « (98 / lois sur 214) », et « 1 / 200 » pour 1 200, saisi avec une espace ordinaire).
    # Règle du site : un nombre ne se sépare ni de son unité ni de la suite de sa date, quel que soit le support.
    s = re.sub(r"(?<![\d\u00a0\u202f])(\d{1,3}) (?=\d{3}(?!\d))", "\\1\u00a0", s)
    s = re.sub(r"(?<=\d\u00a0\d{3}) (?=\d{3}(?!\d))", "\u00a0", s)
    s = re.sub(r"(\d) (Md€|M€|k€|€|Md|bn|pts?|fois|times|Mt|kt|GW|MW|TWh|GWh|EJ|ha|km|h)(?![\w€])", "\\1\u00a0\\2", s)
    s = re.sub(r"\b(\d{1,2}|1er) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\b",
               "\\1\u00a0\\2", s)
    s = re.sub(r"\b(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2})\b(?! ?\d)",
               "\\1\u00a0\\2", s)
    s = re.sub(r"(\([\u2212+-]?\d[\d,.\u00a0\u202f]*) ", "\\1\u00a0", s)
    # Un signe seul (« + fait monter, − fait baisser ») ne finit jamais une ligne (03/11/2026, cascade téléphone).
    s = re.sub(r"(^| )([+\u2212]) ", "\\1\\2\u00a0", s)
    # Un séparateur « · » ne finit jamais une ligne (04/11/2026 : 36 pieds de figure coupés après lui, règle R5 de
    # check-figures étendue) : soudé au mot qui le suit, il passe à la ligne avec lui.
    # Espaces multiples apr\u00e8s le \u00ab \u00b7 \u00bb (\u00ab (T2 2026)  \u00b7  Eurostat \u00bb, source du ciseau, 05/11/2026) : seule la premi\u00e8re
    # devenait ins\u00e9cable et la ligne se coupait encore apr\u00e8s le s\u00e9parateur.
    s = re.sub("\u00b7 +", "\u00b7\u00a0", s)
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
    # Fond blanc opaque pour toute figure (11/11/2026, contrôle du rendu) : 22 figures détaillées n'en avaient pas, et
    # les arcs décoratifs du fond de page traversaient leur tracé. Posé ici, une fois, juste après la description.
    if not a_fond_blanc(s, largeur):
        s = s.replace("</desc>", '</desc>\n<rect width="%d" height="%d" fill="#ffffff"/>' % (largeur, h), 1)
    return re.sub(r'<rect width="%d" height="[0-9.]+"' % largeur, '<rect width="%d" height="%d"' % (largeur, h), s, count=1)


def a_fond_blanc(svg: str, largeur: int) -> bool:
    """Un des trois premiers rectangles couvre-t-il toute la largeur, en blanc, depuis le bord gauche ?"""
    for r in re.findall(r"<rect\b[^>]*>", svg)[:3]:
        if (re.search(r'fill="(#fff|#ffffff|white)"', r, re.I) and 'width="%d"' % largeur in r
                and not re.search(r'\bx="[1-9]', r)):
            return True
    return False


def lire(svg: str, classe: str) -> str:
    """Texte d'un bloc du pied, lignes rejointes (fiches « Réutiliser »). La soudure « ·  » de coupe() ne sert
    que la coupure du SVG : elle se défait ici (05/11/2026 : depuis 8ef0d00, la licence relue ne valait plus celle du
    générateur, et dix générateurs s'arrêtaient sur « pied illisible »)."""
    return " ".join(html.unescape(t) for t in re.findall(r'<text class="%s"[^>]*>(.*?)</text>' % classe, svg)
                    ).replace("· ", "· ")


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
    # Un texte de série s'écrit dans l'ENCRE de sa couleur (encre_texte) : les deux sont lues, sinon le contrôle
    # deviendrait aveugle aux valeurs orange sans rien signaler (11/11/2026).
    for c in sorted(set(couleurs) | {encre_texte(c) for c in couleurs}):
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
