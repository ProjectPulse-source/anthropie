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
  R5  aucune ligne de texte ne finit par un signe seul (« + », « − », « – ») ni ne commence par « : ; ? ! % ».
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


def charger_metriques() -> dict:
    return json.loads(METRIQUES.read_text(encoding="utf-8"))


def chasse(texte: str, taille: float, gras: bool, M: dict) -> float:
    t = M["gras" if gras else "regulier"]
    defaut = M["defaut_gras" if gras else "defaut_regulier"]
    return sum(t.get(c, defaut) for c in texte) * taille / 1000


def lire(svg: str, M: dict) -> dict:
    racine = ET.fromstring(svg)
    vb = [float(v) for v in (racine.get("viewBox") or "0 0 0 0").split()]
    textes, marques, filets = [], [], []
    for el in racine.iter():
        tag = el.tag.replace(NS, "")
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
            textes.append(dict(t=contenu, b=(x0, y - HAMPE * taille, x0 + larg, y + bas * taille), taille=taille))
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


def examiner(F: dict) -> tuple[list[str], list[str]]:
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


# Exceptions DECLAREES : figure en defaut dont la correction est faite dans le generateur mais ne peut pas encore etre
# regeneree. Chacune meurt d'elle-meme : si la figure passe, le controle echoue tant que la ligne n'est pas retiree.
# Règle R5 étendue au « · » le 04/11/2026 : 36 figures, régénérées par leurs générateurs au fil de leurs mises à jour
# (jamais en masse) ; chaque exception meurt d'elle-même quand sa figure passe.
EXCEPTIONS: dict[str, str] = {
    "ciseau-dette-interets-en-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "ciseau-dette-interets-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-cascade-en-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-cascade-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-europe-en-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-europe-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-investissement-en-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-investissement-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-plf-en-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "collectivites-plf-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "dechets-volume-activite-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "decouplage-decomposition-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "delais-admissions-en.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "delais-cursus-en.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "dette-formules-grece-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "dette-formules-grille-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "dette-inflation-achats-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "dette-inflation-calendrier-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "imprevu-menages-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "langue-chronologie-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "langue-dictee-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "langue-ecarts-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "langue-plaisir-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "lycee-classes-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "lycee-concours-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "lycee-heures-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "niveau-baisse-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "niveau-composition-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "niveau-sommet-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "niveau-thermometres-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "qui-paie-mecanismes-en-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "qui-paie-mecanismes-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "qui-paie-redistribution-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
    "qui-paie-solde-net-m.svg": "« · » en fin de ligne du pied : organe corrigé (pied_figure.coupe, 04/11/2026), passera à la prochaine régénération",
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
    tete = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">'
    cas = {
        "propre": ('<circle cx="100" cy="100" r="5"/><text x="109" y="104" font-size="11">Autriche</text>'
                   '<circle cx="200" cy="150" r="5"/><line x1="200" y1="145" x2="200" y2="120" stroke="#52514e" stroke-width="1"/>'
                   '<text x="200" y="117" font-size="11" text-anchor="middle">Chypre</text>', None),
        "R1": ('<text x="10" y="50" font-size="11">Finlande</text><text x="30" y="52" font-size="11">Autriche</text>', "R1"),
        "R2": ('<circle cx="40" cy="47" r="5"/><text x="10" y="50" font-size="11">Croatie</text>', "R2"),
        "R3": ('<text x="290" y="50" font-size="11">Slovaquie</text>', "R3"),
        "R4": ('<circle cx="50" cy="50" r="5"/><circle cx="70" cy="70" r="5"/>'
               '<line x1="50" y1="55" x2="90" y2="95" stroke="#52514e" stroke-width="1"/>'
               '<text x="92" y="100" font-size="11">Irlande</text>', "R4"),
        "R5": ('<text x="10" y="50" font-size="11">en points de PIB ; + fait monter, −</text>', "R5"),
        "R5b": ('<text x="10" y="50" font-size="11">Calcul Stéphane Lalut, CC BY 4.0 ·</text>', "R5"),
    }
    ok = True
    for nom, (corps, attendu) in cas.items():
        d, _ = examiner(lire(tete + corps + "</svg>", M))
        mord = any(x.startswith(attendu) for x in d) if attendu else not d
        print("  temoin %-6s : %s%s" % (nom, "OK" if mord else "ECHEC", "" if mord else " -- " + "; ".join(d)))
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
        d, s = examiner(lire(p.read_text(encoding="utf-8"), M))
        if p.name in EXCEPTIONS and not args:
            if d:
                print("%s : exception declaree (%s)" % (p.name, EXCEPTIONS[p.name]))
                continue
            n_def += 1
            print("%s : passe desormais -- retirer son exception de check-figures.py" % p.name)
            continue
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
