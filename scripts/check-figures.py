#!/usr/bin/env python3
"""check-figures.py -- lisibilite MESUREE des figures SVG : aucun libelle ne se mord, aucun ne mene au mauvais point.

Consigne de l'auteur (03/11/2026, apres le chantier des figures de /enseignants/) : « cette methodologie de
verification et d'optimisation des graphes doit etre enregistree et cablee pour etre systematiquement utilisee,
rigueur et pas d'erreur ». Methode complete : skill `controle-figures` (D:/PRO/.claude/skills/controle-figures/).
Ce script en est la part MECANIQUE ; il ne remplace ni le recalcul des valeurs contre la source, ni la relecture
du rendu.

    python scripts/check-figures.py                    # toutes les figures de static/img (bloquant, check-all --ci)
    python scripts/check-figures.py fichier.svg dossier/ --detail
    python scripts/check-figures.py --temoin           # temoin positif : chaque regle doit mordre
    python scripts/check-figures.py --metriques        # regenere la table de chasses depuis les polices du poste

Regles BLOQUANTES (une figure en defaut fait sortir 1) :
  R1  deux textes ne se chevauchent pas (boite d'encre : chasse reelle, hampe 0,72 em, jambage 0,22 em) ;
  R2  un texte ne recouvre aucune marque de donnee (cercle de rayon <= 8, carre <= 12 px) ;
  R3  un texte reste dans le cadre (viewBox) ;
  R4  un filet de rattachement (trait #52514e, 1 px) part d'une marque, mene a un texte, ne croise aucun autre filet
      et passe a 3 px au moins du bord de toute autre marque ;
  R5  aucune ligne de texte ne finit par un signe seul (« + », « − », « – ») ni ne commence par « : ; ? ! % » ;
  R6  aucun texte ne s'affiche sous 12 px a la plus petite largeur ou sa version est servie (11/11/2026) : une figure
      detaillee (720 de large) s'affiche a 786 px au plus etroit (bloc « dette en chiffres », a 900 px d'ecran), une
      figure telephone (300) a 277 px -- mesure sur les 53 pages du site ; soit 11 px dessines au moins dans la premiere, 13 px dans la seconde ; et toute figure
      detaillee du site a sa version telephone (X-m.svg), sans laquelle elle est servie telle quelle sous 900 px
      (une seule en etait privee le 11/11/2026 : texte de 5,6 px sur telephone, hors du champ de tous les essais) ;
  R7  tout texte a un contraste d'au moins 4,5:1 avec son fond (3:1 pour un grand texte : 24 px affiches, ou 18,66 px
      en gras) ; le fond est le blanc de la figure ou la derniere forme pleine (rectangle, cercle) dessinee sous lui.
      Plus aucune exception de charte (11/11/2026) : l'auteur a retenu l'orange fonce pour le texte d'une serie
      orange (pied_figure.ORANGE_TEXTE) et l'encre foncee pour le texte pose sur une marque orange ou grise
      (pied_figure.encre_sur) ; un texte reste en #eb6834, ou blanc sur une telle marque, est un defaut. Non juge,
      signale avec --detail : un texte clair sans forme pleine reconnue sous lui (trace, polygone). Sur le site entier, toute figure porte un fond blanc opaque
      (rectangle de la largeur du dessin) : R7 juge le texte sur ce blanc, et sans lui les motifs du fond de page
      traversent le trace (22 figures detaillees en etaient privees le 11/11/2026).
Signalement NON bloquant (--detail) : nom de nuage dont les deux marques les plus proches sont presque a egale distance
(rattachement a regarder au rendu ; le script ne sait pas quel pays porte chaque marque, le generateur le sait).

Mesure INDEPENDANTE des generateurs (doctrine R5 : un controle qui partage le filtre de ce qu'il controle ne controle
rien) : les generateurs placent les noms avec une chasse approchee par classes de lettres ; ce controle lit la table
`scripts/metriques_polices.json`, tiree des polices reelles (maximum d'Arial, Segoe UI et Roboto, regulier et gras),
sans dependance a l'execution -- la CI n'a ni ces polices ni Pillow.

Cas fondateur (03/11/2026) : « Autriche » pose au-dessus du point de la Finlande, « Croatie » lue comme Chypre, piles
de barres remontees de 2 px, « − » seul en fin de ligne -- aucun controle ne les voyait ; tous trouves en relisant.
Dispositif permanent (il protege tout ce qui est publie) : reexamine a la revue annuelle comme les autres.
"""
from __future__ import annotations

import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
METRIQUES = ROOT / "scripts" / "metriques_polices.json"
NS = "{http://www.w3.org/2000/svg}"
FILET = "#52514e"
HAMPE, JAMBAGE = 0.72, 0.22
# R6 : largeur d'affichage la plus etroite de chaque version (largeur de dessin -> px), mesuree le 11/11/2026 sur le
# site servi (52 pages, ecrans de 320 et 900 px). Independante des generateurs : ils declarent une police minimale,
# ce controle mesure la taille AFFICHEE.
LARGEUR_SERVIE_MIN = {720: 786.0, 300: 277.0}
TAILLE_AFFICHEE_MIN = 12.0


def charger_metriques() -> dict:
    return json.loads(METRIQUES.read_text(encoding="utf-8"))


def chasse(texte: str, taille: float, gras: bool, M: dict) -> float:
    t = M["gras" if gras else "regulier"]
    defaut = M["defaut_gras" if gras else "defaut_regulier"]
    return sum(t.get(c, defaut) for c in texte) * taille / 1000


def hexa(c: str | None) -> str | None:
    c = (c or "").strip().lower()
    c = {"white": "#ffffff", "black": "#000000"}.get(c, c)
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(x * 2 for x in c[1:])
    return c if re.fullmatch(r"#[0-9a-f]{6}", c) else None


def rvb(c: str) -> tuple[float, float, float]:
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def melange(dessus: str, dessous: str, op: float) -> str:
    return "#%02x%02x%02x" % tuple(round(op * a + (1 - op) * b) for a, b in zip(rvb(dessus), rvb(dessous)))


def luminance(c: str) -> float:
    v = [x / 255 for x in rvb(c)]
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]


def contraste(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def opacite(el) -> float:
    try:
        return float(el.get("opacity", 1) or 1) * float(el.get("fill-opacity", 1) or 1)
    except ValueError:
        return 1.0


def lire(svg: str, M: dict) -> dict:
    racine = ET.fromstring(svg)
    vb = [float(v) for v in (racine.get("viewBox") or "0 0 0 0").split()]
    textes, marques, filets = [], [], []
    parent = {c: p for p in racine.iter() for c in p}
    formes = []      # formes pleines dans l'ordre du document : ("r", x0, y0, x1, y1, couleur, opacite) ou ("c", cx, cy, r, ...)
    for el in racine.iter():
        tag = el.tag.replace(NS, "")
        if tag in ("rect", "circle") and hexa(el.get("fill")):
            if tag == "rect":
                x, y = float(el.get("x", 0) or 0), float(el.get("y", 0) or 0)
                formes.append(("r", x, y, x + float(el.get("width", 0) or 0), y + float(el.get("height", 0) or 0),
                               hexa(el.get("fill")), opacite(el)))
            else:
                formes.append(("c", float(el.get("cx", 0) or 0), float(el.get("cy", 0) or 0), float(el.get("r", 0) or 0), 0,
                               hexa(el.get("fill")), opacite(el)))
        if tag == "text":
            if el.get("aria-hidden") == "true":
                continue   # liseré blanc : le meme texte, dessous
            contenu = "".join(el.itertext())
            if not contenu.strip():
                continue
            x, y = float(el.get("x", 0)), float(el.get("y", 0))
            taille = float(el.get("font-size", 11))
            gras = (el.get("font-weight") or "400") in ("600", "700", "bold")
            larg = chasse(contenu, taille, gras, M)
            anc = el.get("text-anchor", "start")
            x0 = {"start": x, "middle": x - larg / 2, "end": x - larg}.get(anc, x)
            # Jambage compté seulement si une lettre descend (p, q, g, j, y, virgule...) : sinon la boîte touchait à tort
            # un point posé juste sous le texte (« point écarté », 03/11/2026).
            bas = JAMBAGE if re.search(r"[gjpqyçQ,;()\[\]{}/|µ]", contenu) else 0.05
            # Couleur du texte (heritee d'un groupe a defaut d'attribut) et fond : le blanc, puis chaque forme pleine
            # deja dessinee qui couvre le centre du texte.
            n, encre = el, None
            while n is not None and encre is None:
                encre = hexa(n.get("fill"))
                n = parent.get(n)
            encre = encre or "#000000"
            xc, yc = x0 + larg / 2, y - 0.3 * taille
            fond, sous_forme = "#ffffff", False
            for f in formes:
                dedans = (f[1] <= xc <= f[3] and f[2] <= yc <= f[4]) if f[0] == "r" else math.hypot(xc - f[1], yc - f[2]) <= f[3]
                if dedans:
                    fond = melange(f[5], fond, f[6])
                    sous_forme = sous_forme or f[5] != "#ffffff"
            op = opacite(el)
            textes.append(dict(t=contenu, b=(x0, y - HAMPE * taille, x0 + larg, y + bas * taille), taille=taille, gras=gras,
                               encre=melange(encre, fond, op) if op < 1 else encre, encre_declaree=encre, fond=fond,
                               sous_forme=sous_forme))
        elif tag == "circle":
            r = float(el.get("r", 0))
            if 0 < r <= 8:
                marques.append((float(el.get("cx", 0)), float(el.get("cy", 0)), r))
        elif tag == "rect":
            w, h = float(el.get("width", 0) or 0), float(el.get("height", 0) or 0)
            if 0 < w <= 12 and abs(w - h) < 0.01:
                marques.append((float(el.get("x", 0)) + w / 2, float(el.get("y", 0)) + h / 2, w / 2))
        elif tag == "line" and (el.get("stroke") or "").lower() == FILET and el.get("stroke-width") in ("1", "1.0"):
            filets.append(tuple(float(el.get(k, 0)) for k in ("x1", "y1", "x2", "y2")))
    return dict(vb=vb, textes=textes, marques=marques, filets=filets)


def d_boite(x, y, b) -> float:
    return math.hypot(x - min(max(x, b[0]), b[2]), y - min(max(y, b[1]), b[3]))


def d_segment(x, y, s) -> float:
    vx, vy = s[2] - s[0], s[3] - s[1]
    k = max(0.0, min(1.0, ((x - s[0]) * vx + (y - s[1]) * vy) / ((vx * vx + vy * vy) or 1)))
    return math.hypot(x - s[0] - k * vx, y - s[1] - k * vy)


def croise(a, b) -> bool:
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    p1, p2, p3, p4 = (a[0], a[1]), (a[2], a[3]), (b[0], b[1]), (b[2], b[3])
    return o(p1, p2, p3) * o(p1, p2, p4) < 0 and o(p3, p4, p1) * o(p3, p4, p2) < 0


def fr(x: float, n: int = 1) -> str:
    return ("%.*f" % (n, x)).replace(".", ",")


def examiner(F: dict, strict: bool = False) -> tuple[list[str], list[str]]:
    defauts, signal = [], []
    T, Mq, Fl = F["textes"], F["marques"], F["filets"]
    # R1
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i]["b"], T[j]["b"]
            if a[0] < b[2] - 0.5 and b[0] < a[2] - 0.5 and a[1] < b[3] - 0.5 and b[1] < a[3] - 0.5:
                defauts.append("R1 « %s » chevauche « %s »" % (T[i]["t"], T[j]["t"]))
    # R2 (sauf pastille : un chiffre centré DANS son cercle, comme les étapes numérotées d'une frise)
    for t in T:
        b = t["b"]
        for (cx, cy, r) in Mq:
            if abs((b[0] + b[2]) / 2 - cx) < 1 and b[2] - b[0] < 2 * r and b[0] > cx - r and b[2] < cx + r:
                continue
            if d_boite(cx, cy, b) < r - 0.5:
                defauts.append("R2 « %s » recouvre une marque (%.1f, %.1f)" % (t["t"], cx, cy))
                break
    # R3
    x0, y0, w, h = F["vb"]
    for t in T:
        b = t["b"]
        if w and (b[0] < x0 - 0.5 or b[2] > x0 + w + 0.5 or b[1] < y0 - 0.5 or b[3] > y0 + h + 0.5):
            defauts.append("R3 « %s » sort du cadre" % t["t"])
    # R4
    for k, s in enumerate(Fl):
        dep = min(Mq, key=lambda m: math.hypot(m[0] - s[0], m[1] - s[1]) - m[2], default=None)  # brut-ok: marque de depart
        if dep is None or math.hypot(dep[0] - s[0], dep[1] - s[1]) - dep[2] > 4:
            defauts.append("R4 filet (%.0f, %.0f) ne part d'aucune marque" % (s[0], s[1]))
            continue
        if not any(d_boite(s[2], s[3], t["b"]) < 4 for t in T):
            defauts.append("R4 filet (%.0f, %.0f) ne mene a aucun texte" % (s[0], s[1]))
        for m in Mq:
            if m is not dep and d_segment(m[0], m[1], s) < m[2] + 3:
                defauts.append("R4 filet (%.0f, %.0f) frole une autre marque (%.1f, %.1f)" % (s[0], s[1], m[0], m[1]))
        for s2 in Fl[k + 1:]:
            if croise(s, s2):
                defauts.append("R4 deux filets se croisent (%.0f, %.0f)" % (s[0], s[1]))
    # R5
    for t in T:
        brut = t["t"].rstrip()
        # « · » inclus (04/11/2026) : un séparateur ne finit jamais une ligne (règle de l'auteur : signe seul en FIN de ligne ;
        # en début de ligne il n'est pas visé — 123 pieds de figure ainsi coupés, conformes à la règle)
        if re.search(r"(^|\s)[+\u2212\u2013\u00b7]$", brut):
            defauts.append("R5 « %s » finit par un signe seul" % t["t"])
        if re.match(r"^[:;?!%]", t["t"].lstrip()):
            defauts.append("R5 « %s » commence par une ponctuation haute" % t["t"])
    # R6 : taille affichee a la plus petite largeur servie
    servie = LARGEUR_SERVIE_MIN.get(round(w))
    echelle = servie / w if servie else None
    if echelle is None and T and w:
        (defauts if strict else signal).append(
            "R6 largeur de dessin %d sans largeur servie connue (LARGEUR_SERVIE_MIN) : taille non controlee" % round(w))
    if echelle:
        petits = sorted((t for t in T if t["taille"] * echelle < TAILLE_AFFICHEE_MIN - 0.005), key=lambda t: t["taille"])
        if petits:
            defauts.append("R6 %d texte(s) sous %d px affiches a %d px de large (le plus petit : %s px dessines, %s px affiches) : %s"
                           % (len(petits), TAILLE_AFFICHEE_MIN, servie, fr(petits[0]["taille"]), fr(petits[0]["taille"] * echelle),
                              " ; ".join("« %s »" % t["t"][:28] for t in petits[:3])))
    # R7 : contraste du texte avec son fond
    faibles, non_juges = {}, 0
    for t in T:
        c = contraste(t["encre"], t["fond"])
        affiche = t["taille"] * (echelle or 1)
        seuil = 3.0 if affiche >= 24 or (t["gras"] and affiche >= 18.66) else 4.5
        if c >= seuil - 0.005:
            continue
        cle = (t["encre"], t["fond"])
        if luminance(t["encre"]) > 0.5 and not t["sous_forme"]:
            non_juges += 1          # texte clair sans forme pleine reconnue dessous : fond inconnu de ce controle
        else:
            faibles.setdefault(cle, []).append(t["t"])
    for (encre, fond), L in sorted(faibles.items(), key=lambda kv: -len(kv[1])):
        defauts.append("R7 %d texte(s) %s sur %s : contraste %s:1, minimum 4,5 -- %s"
                       % (len(L), encre, fond, fr(contraste(encre, fond), 2), " ; ".join("« %s »" % x[:28] for x in L[:3])))
    if non_juges:
        signal.append("R7 non juge : %d texte(s) clair(s) sans forme pleine reconnue dessous" % non_juges)
    # Signalement : rattachement dans un nuage (au moins 8 marques), noms sans filet
    if len(Mq) >= 8:
        bouts = [(s[2], s[3]) for s in Fl]
        for t in T:
            if any(d_boite(x, y, t["b"]) < 4 for x, y in bouts):
                continue
            ds = sorted(d_boite(m[0], m[1], t["b"]) - m[2] for m in Mq)
            if len(ds) > 1 and ds[0] < 8 and ds[1] - ds[0] < 2:
                signal.append("« %s » : deux marques presque a egale distance (%.1f et %.1f px)" % (t["t"], ds[0], ds[1]))
    return defauts, signal


def sans_telephone(nom: str, F: dict, existe) -> str | None:
    """R6, complement : une figure detaillee (720 de large) sans version telephone est servie telle quelle sous 900 px.
    `existe(nom_de_fichier)` dit si le fichier frere est la (injecte : le temoin l'essaie sans rien ecrire)."""
    if nom.endswith("-m.svg") or round(F["vb"][2]) != 720 or not F["textes"]:
        return None
    frere = nom[:-4] + "-m.svg"
    if existe(frere):
        return None
    mini = min(t["taille"] for t in F["textes"])  # brut-ok: plus petite police dessinee
    return ("R6 pas de version telephone (%s) : sous 900 px d'ecran la version detaillee est servie a %d px au plus etroit, "
            "soit %s px pour son plus petit texte" % (frere, LARGEUR_SERVIE_MIN[300], fr(mini * LARGEUR_SERVIE_MIN[300] / 720)))


def sans_fond(svg: str, F: dict) -> str | None:
    """R7, complement : la figure a-t-elle un fond blanc opaque sur toute sa largeur (un des trois premiers rectangles) ?"""
    largeur = round(F["vb"][2])
    for r in re.findall(r"<rect\b[^>]*>", svg)[:3]:
        if (re.search(r'fill="(#fff|#ffffff|white)"', r, re.I) and 'width="%d"' % largeur in r
                and not re.search(r'\bx="[1-9]', r) and not re.search(r'opacity="0?\.', r)):
            return None
    return "R7 pas de fond blanc opaque : le fond de la page, motifs compris, se voit a travers la figure"


# Exceptions DECLAREES : figure en defaut dont la correction est faite dans le generateur mais ne peut pas encore etre
# regeneree. Chacune meurt d'elle-meme : si la figure passe, le controle echoue tant que la ligne n'est pas retiree.
# Règle R5 étendue au « · » le 04/11/2026 : 36 figures, régénérées par leurs générateurs au fil de leurs mises à jour
# (jamais en masse) ; chaque exception meurt d'elle-même quand sa figure passe. Toutes passées le 05/11/2026 (la dernière, le ciseau, après la soudure des espaces multiples dans l'organe).
EXCEPTIONS: dict[str, str] = {
}


def fichiers(args: list[str]) -> list[Path]:
    if not args:
        return sorted((ROOT / "static" / "img").glob("*.svg"))
    out = []
    for a in args:
        p = Path(a)
        out += sorted(p.glob("*.svg")) if p.is_dir() else [p]
    return out


def temoin(M: dict) -> int:
    """Chaque regle doit mordre sur un SVG fabrique pour elle, et un SVG propre doit passer."""
    # En-tete de 720 de large (version detaillee) : a 11 px, les textes des cas R1 a R5 passent R6. Le cas « propre »
    # porte aussi ce que R6 et R7 doivent laisser passer : encre attenuee, texte blanc sur le bleu, grand titre orange.
    tete = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 200">'
    tete_m = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">'
    cas = {
        "propre": ('<circle cx="100" cy="100" r="5"/><text x="109" y="104" font-size="11">Autriche</text>'
                   '<circle cx="200" cy="150" r="5"/><line x1="200" y1="145" x2="200" y2="120" stroke="#52514e" stroke-width="1"/>'
                   '<text x="200" y="117" font-size="11" text-anchor="middle">Chypre</text>'
                   '<text x="400" y="50" font-size="11" fill="#6f6c66">Source : Eurostat</text>'
                   '<rect x="400" y="80" width="120" height="24" fill="#184f95"/>'
                   '<text x="410" y="96" font-size="11" fill="#ffffff">42 %</text>'
                   '<text x="400" y="150" font-size="26" fill="#eb6834">3 000 Md€</text>'
                   '<text x="560" y="50" font-size="11" fill="#b8420f">119,0 %</text>'
                   '<rect x="560" y="80" width="120" height="24" fill="#eb6834"/>'
                   '<text x="570" y="96" font-size="11" fill="#0A0A0E">66 %</text>'
                   '<rect x="560" y="110" width="120" height="24" fill="#8a8781"/>'
                   '<text x="570" y="126" font-size="11" fill="#0A0A0E">123</text>', None),
        "propre_m": ("M" + '<text x="10" y="50" font-size="13.5" fill="#6f6c66">Source : Insee</text>', None),
        "R1": ('<text x="10" y="50" font-size="11">Finlande</text><text x="30" y="52" font-size="11">Autriche</text>', "R1"),
        "R2": ('<circle cx="40" cy="47" r="5"/><text x="10" y="50" font-size="11">Croatie</text>', "R2"),
        "R3": ('<text x="700" y="50" font-size="11">Slovaquie</text>', "R3"),
        "R4": ('<circle cx="50" cy="50" r="5"/><circle cx="70" cy="70" r="5"/>'
               '<line x1="50" y1="55" x2="90" y2="95" stroke="#52514e" stroke-width="1"/>'
               '<text x="92" y="100" font-size="11">Irlande</text>', "R4"),
        "R5": ('<text x="10" y="50" font-size="11">en points de PIB ; + fait monter, −</text>', "R5"),
        "R5b": ('<text x="10" y="50" font-size="11">Calcul Stéphane Lalut, CC BY 4.0 ·</text>', "R5"),
        "R6": ('<text x="10" y="50" font-size="10.5">Taux en %</text>', "R6"),
        "R6m": ("M" + '<text x="10" y="50" font-size="12">Taux en %</text>', "R6"),
        "R7": ('<text x="10" y="50" font-size="11" fill="#96928f">2024</text>', "R7"),
        "R7fond": ('<rect x="0" y="30" width="200" height="40" fill="#e4dfd7"/>'
                   '<text x="10" y="50" font-size="11" fill="#6f6c66">Crise de 2008</text>', "R7"),
        "R7gris": ('<text x="10" y="50" font-size="11" fill="#898781">Zone euro</text>', "R7"),
        "R7orange": ('<text x="10" y="50" font-size="11" fill="#eb6834">119,0 %</text>', "R7"),
        "R7blanc": ('<rect x="0" y="30" width="200" height="40" fill="#eb6834"/>'
                    '<text x="10" y="50" font-size="11" fill="#ffffff">66 %</text>', "R7"),
        "R7blancg": ('<rect x="0" y="30" width="200" height="40" fill="#8a8781"/>'
                     '<text x="10" y="50" font-size="11" fill="#ffffff">123</text>', "R7"),
    }
    ok = True
    for nom, (corps, attendu) in cas.items():
        corps, t = (corps[1:], tete_m) if corps.startswith("M") else (corps, tete)
        d, _ = examiner(lire(t + corps + "</svg>", M))
        mord = any(x.startswith(attendu) for x in d) if attendu else not d
        print("  temoin %-6s : %s%s" % (nom, "OK" if mord else "ECHEC", "" if mord else " -- " + "; ".join(d)))
        ok &= mord
    # R6, version telephone : une figure detaillee sans frere « -m » mord ; avec lui, ou en 300 de large, elle passe.
    F720 = lire(tete + '<text x="10" y="50" font-size="11">Taux en %</text></svg>', M)
    F300 = lire(tete_m + '<text x="10" y="50" font-size="13.5">Taux en %</text></svg>', M)
    fond = '<rect width="720" height="200" fill="#ffffff"/>'
    for nom, mord in (("R7fd", (sans_fond(tete + "</svg>", F720) or "").startswith("R7")),
                      ("R7fd+", sans_fond(tete + fond + "</svg>", F720) is None),
                      ("R7fd%", (sans_fond(tete + fond.replace("/>", ' opacity="0.5"/>') + "</svg>", F720) or "").startswith("R7")),
                      ("R6tel", (sans_telephone("x.svg", F720, lambda n: False) or "").startswith("R6")),
                      ("R6tel+", sans_telephone("x.svg", F720, lambda n: n == "x-m.svg") is None),
                      ("R6tel-m", sans_telephone("x-m.svg", F300, lambda n: False) is None)):
        print("  temoin %-6s : %s" % (nom, "OK" if mord else "ECHEC"))
        ok &= mord
    print("Temoin check-figures : %s" % ("chaque regle mord, le cas propre passe. OK" if ok else "ECHEC"))
    return 0 if ok else 1


def metriques() -> int:
    """Table des chasses (millièmes d'em), maximum de plusieurs polices : a lancer sur un poste qui les a."""
    from PIL import ImageFont
    polices = {"regulier": ["arial.ttf", "segoeui.ttf", "Roboto-Regular.ttf"],
               "gras": ["arialbd.ttf", "segoeuib.ttf", "Roboto-Bold.ttf"]}
    dossier = Path("C:/Windows/Fonts")
    jeu = set()
    for p in sorted((ROOT / "static" / "img").glob("*.svg")):
        jeu |= set(p.read_text(encoding="utf-8"))
    jeu |= set(chr(c) for c in range(32, 383)) | set("«»’–—−€×·…≤≥ \u00a0\u202f")
    out = {"_doc": "chasses en milliemes d'em, maximum des polices disponibles ; regenerer : check-figures.py --metriques"}
    for graisse, noms in polices.items():
        fontes = [ImageFont.truetype(str(dossier / n), 1000) for n in noms if (dossier / n).exists()]
        out["polices_" + graisse] = [n for n in noms if (dossier / n).exists()]
        out[graisse] = {c: max(round(f.getlength(c)) for f in fontes) for c in sorted(jeu) if c.isprintable() or c in "\u00a0\u202f"}
        out["defaut_" + graisse] = max(out[graisse].values())
    METRIQUES.write_text(json.dumps(out, ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    print("Ecrit : %s (%d caracteres)" % (METRIQUES.relative_to(ROOT), len(out["regulier"])))
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--metriques" in sys.argv:
        return metriques()
    M = charger_metriques()
    if "--temoin" in sys.argv:
        return temoin(M)
    detail = "--detail" in sys.argv
    n_def = 0
    fs = fichiers(args)
    for p in fs:
        F = lire(p.read_text(encoding="utf-8"), M)
        d, s = examiner(F, strict=not args)
        if not args:      # site entier : la version telephone se cherche a cote du fichier ; le fond blanc se lit dans le fichier
            manque = sans_telephone(p.name, F, lambda n, dossier=p.parent: (dossier / n).exists())
            if manque:
                d.append(manque)
            transparent = sans_fond(p.read_text(encoding="utf-8"), F)
            if transparent:
                d.append(transparent)
        if p.name in EXCEPTIONS and not args:
            # L'exception n'excuse QUE sa classe (« · » en fin de ligne d'un pied, R5) ; tout autre défaut de la figure
            # reste bloquant (04/11/2026 : elle excusait auparavant n'importe quel défaut). Devenue sans objet, elle est
            # signalée sans bloquer : un workflow de données qui régénère la figure avec l'organe corrigé ne doit pas
            # s'arrêter pour une ligne de liste à retirer (rien n'est masqué : il ne reste aucun défaut de la classe).
            point = [x for x in d if x.startswith("R5 ") and re.search("·\\s*»", x)]
            autres = [x for x in d if x not in point]
            if point:
                print("%s : exception declaree (%s)" % (p.name, EXCEPTIONS[p.name]))
            else:
                print("%s : exception sans objet -- a retirer de check-figures.py (non bloquant)" % p.name)
            if not autres:
                continue
            d = autres
        if d:
            n_def += 1
            print("%s : %d defaut(s)" % (p.name, len(d)))
            for x in d[: (None if detail else 5)]:
                print("    " + x)
        if detail and s:
            print("%s : a regarder au rendu" % p.name)
            for x in s:
                print("    " + x)
    print("Figures : %d SVG lus, %d en defaut. %s" % (len(fs), n_def, "OK" if not n_def else "ECHEC"))
    return 1 if n_def else 0


if __name__ == "__main__":
    sys.exit(main())
