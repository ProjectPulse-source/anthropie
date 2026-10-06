#!/usr/bin/env python3
"""Volet « Décider » du dossier Promesses : inventaire de l'article 19, en citations vérifiées.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 1, E1 (v2, gelée au
commit dfd0ec9 du dépôt D:/PRO ; arbitrage PRO-20261005-164029). Le test du « zéro norme » est RETIRÉ : on n'écrit
aucune phrase « le président ne peut pas » ; on inventorie ce que le texte fait faire, exige et fait intervenir.

Entrée : data/pouvoirs_president.yaml (articles lus sur Légifrance, empreintes ; inventaire_19 ; regles) et les
réponses Légifrance archivées par le serveur `sources` (D:/PRO/02_FABRIQUE/sources/archive/<mois>/<sha256>.json).
Script LOCAL : l'archive n'est pas dans le dépôt du site ; il s'arrête si elle manque.

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  G1  chaque article cité a sa réponse archivée, et celle-ci est bien l'article annoncé (numéro, identifiant, VIGUEUR) ;
  G2  chaque citation de l'inventaire figure MOT POUR MOT dans le texte archivé de son article (espaces et apostrophes
      normalisés, rien d'autre) ;
  G3  TÉMOIN DE COMPLÉTUDE : la liste des renvois de l'inventaire est relue dans le texte de l'article 19 lui-même ;
      un renvoi manquant ou en trop arrête ;
  G4  les qualificatifs de la prose (« seulement ») sont recalculés : faux dans les données, arrêt.
Autotest de mutation (à chaque exécution) : une citation altérée doit faire mordre G2, un renvoi retiré G3.

Écrit : data/pouvoirs_president_donnees.json (+ copie static/), static/pouvoirs_president_donnees.csv (UTF-8 BOM,
format long), data/figures_pouvoirs.json, static/img/pouvoirs-article19.svg + .png (ensemble ou pas du tout).
Rien n'est écrit à données identiques. Sortie console ASCII.
"""
from __future__ import annotations

import copy
import csv
import html
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT.parents[1] / "02_FABRIQUE" / "sources" / "archive"
SRC = ROOT / "data" / "pouvoirs_president.yaml"
OUT_DATA = ROOT / "data" / "pouvoirs_president_donnees.json"
OUT_STATIC = ROOT / "static" / "pouvoirs_president_donnees.json"
OUT_CSV = ROOT / "static" / "pouvoirs_president_donnees.csv"
OUT_FIGURES = ROOT / "data" / "figures_pouvoirs.json"
OUT_IMG = ROOT / "static" / "img"
FIG = "pouvoirs-article19"
PAGE_URL = "stephane-lalut.com/pouvoirs-du-president-de-la-republique/"
LEGIFRANCE = "https://www.legifrance.gouv.fr/loda/article_lc/"
ATTRIBUTS = [("condition", "Proposition ou consultation exigée avant l'acte"),
             ("autre_autorite", "Un autre acteur intervient pour la suite"),
             ("partage", "D'autres autorités disposent d'un pouvoir de même nature"),
             ("limite", "Autre encadrement écrit : temps, objet ou effet")]
LETTRES_F = {0: "aucune", 1: "une", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit"}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r" ([,.;:])", r"\1", s)
    return s.strip()


def charger_articles(base: dict) -> dict:
    """G1 : texte archivé de chaque article, contrôlé contre son identifiant."""
    if not ARCHIVE.is_dir():
        raise Arret("archive Legifrance introuvable (%s) : script local, lancer depuis D:/PRO" % ARCHIVE)
    textes = {}
    for num, a in base["articles"].items():
        if not a.get("lu_le"):
            continue
        f = list(ARCHIVE.glob("*/%s.json" % a["empreinte"]))
        if len(f) != 1:
            raise Arret("G1 art. %s : reponse archivee %s introuvable ou en double" % (num, a["empreinte"][:12]))
        j = json.loads(f[0].read_text(encoding="utf-8"))
        art = j.get("article") or {}
        if str(art.get("num")) != str(num) or art.get("id") != a["legiarti"] or art.get("etat") != "VIGUEUR":
            raise Arret("G1 art. %s : l'archive ne porte pas l'article annonce (num %s, id %s, etat %s)"
                        % (num, art.get("num"), art.get("id"), art.get("etat")))
        textes[str(num)] = art["texte"]
    return textes


def verifier_cite(c: dict, textes: dict, ou: str) -> None:
    """G2 : citation mot pour mot."""
    art = str(c["art"])
    if art not in textes:
        raise Arret("G2 %s : article %s sans lecture archivee" % (ou, art))
    if norm(c["cite"]) not in norm(textes[art]):
        raise Arret("G2 %s : citation absente du texte de l'article %s : %r" % (ou, art, c["cite"][:70]))


def renvois_article19(texte19: str) -> list[str]:
    """G3, témoin : la liste des renvois relue dans l'article 19 lui-même."""
    m = re.search(r"autres que ceux prévus aux articles (.+?) sont contresignés", norm(texte19))
    if not m:
        raise Arret("G3 : la phrase des renvois est introuvable dans le texte de l'article 19")
    return re.findall(r"\d+", re.sub(r"\(1er alinéa\)", "", m.group(1)))


def calculer(base: dict, textes: dict) -> tuple[dict, list[str]]:
    gardes = []
    inv = base["inventaire_19"]
    for e in inv:
        for k in ["acte"] + [a for a, _ in ATTRIBUTS]:
            if e.get(k):
                verifier_cite(e[k], textes, "renvoi %s, %s" % (e["renvoi"], k))
    gardes.append("G2 : %d citations de l'inventaire retrouvees mot pour mot"
                  % sum(1 for e in inv for k in ["acte"] + [a for a, _ in ATTRIBUTS] if e.get(k)))
    for c in base["regles"]:
        verifier_cite(c, textes, "regles")
    gardes.append("G2 : %d citations de « qui fixe les regles » retrouvees" % len(base["regles"]))
    # G2 étendue : toute citation entre guillemets dans les fiches (decide, condition, tiers, portee_texte, chapo des
    # groupes exclus) doit figurer dans l'un des articles que la fiche cite ; « […] » sépare des fragments, chacun
    # contrôlé. Des guillemets promettent une lettre : sans cette garde ils promettraient sans preuve.
    n_fiches = 0
    for p in base["pouvoirs"]:
        corpus = " ".join(norm(textes[str(a)]) for a in p["articles"] if str(a) in textes).casefold()
        for champ in ("decide", "condition", "tiers", "portee_texte"):
            for q in re.findall(r"«\s*(.+?)\s*»", p.get(champ) or ""):
                for frag in re.split(r"\s*\[…\]\s*", q):
                    if norm(frag).casefold() not in corpus:  # seule tolérance : la casse (usage de citation)
                        raise Arret("G2 fiche %s, %s : citation absente des articles %s : %r"
                                    % (p["id"], champ, ",".join(p["articles"]), frag[:60]))
                    n_fiches += 1
    gardes.append("G2 : %d citations entre guillemets des fiches retrouvees" % n_fiches)

    attendus = renvois_article19(textes["19"])
    inventaire = [re.match(r"\d+", e["renvoi"]).group(0) for e in inv]
    if sorted(attendus, key=int) != sorted(inventaire, key=int):
        raise Arret("G3 : renvois de l'article 19 %s != inventaire %s" % (attendus, inventaire))
    gardes.append("G3 : inventaire complet, %d renvois relus dans l'article 19 (%s)" % (len(attendus), ", ".join(attendus)))

    n = len(inv)
    compte = {a: sum(1 for e in inv if e.get(a)) for a, _ in ATTRIBUTS}
    seuls = [e for e in inv if not (e.get("condition") or e.get("autre_autorite") or e.get("partage"))]
    # G4 : « seulement » n'est écrit que si les actes sans condition, ni autre autorité, ni pouvoir partagé sont
    # strictement minoritaires ; sinon la phrase de la page serait fausse.
    if not (0 < len(seuls) and 2 * len(seuls) < n):
        raise Arret("G4 : %d actes sur %d sans condition ni autre autorite ni pouvoir partage : « seulement » est faux"
                    % (len(seuls), n))
    gardes.append("G4 : « seulement » tenu (%d sur %d)" % (len(seuls), n))
    r = {"n": n, "compte": compte, "seuls": [e["pouvoir"] for e in seuls], "seuls_renvois": [e["renvoi"] for e in seuls],
         "inventaire": inv, "regles": base["regles"]}
    return r, gardes


def affichage(r: dict) -> dict:
    seuls = [s[0].lower() + s[1:] for s in r["seuls"]]
    return {
        "n_renvois": LETTRES_F[r["n"]],
        "n_condition": LETTRES_F[r["compte"]["condition"]],
        "n_autre": LETTRES_F[r["compte"]["autre_autorite"]],
        "n_partage": LETTRES_F[r["compte"]["partage"]],
        "n_limite": LETTRES_F[r["compte"]["limite"]],
        "n_seuls": LETTRES_F[len(r["seuls"])],
        "n_seuls_maj": LETTRES_F[len(r["seuls"])].capitalize(),
        "seuls_liste": " et ".join(seuls) if len(seuls) <= 2 else ", ".join(seuls[:-1]) + " et " + seuls[-1],
        # Deux dates distinctes (pièce entrante du 05/10, point 1) : la dernière lecture et l'étendue des lectures.
        "releve_le": "%s (textes lus sur Légifrance du %s au %s)" % (
            date.fromisoformat(r["releve_le"]).strftime("%d/%m/%Y"),
            date.fromisoformat(r["lu_min"]).strftime("%d/%m/%Y"), date.fromisoformat(r["releve_le"]).strftime("%d/%m/%Y")),
    }


# ------------------------------------------------------------------ figure (charte des dossiers du site)
W = 720
BLEU = "#184f95"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCE = "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def figure(r: dict) -> str:
    inv = r["inventaire"]
    top, pas, col0, colw = 126, 34, 330, 97
    H = top + pas * len(inv) + 8
    cart_h = 48
    titre = "Les huit dispositions que l’article 19 dispense de contreseing : ce que leur texte exige ou fait intervenir"
    desc = ("Matrice de %d lignes et 4 colonnes. Une case pleine signifie que l'article lui-même contient une citation "
            "exacte de l'élément ; seules %s lignes n'ont ni condition préalable, ni autre autorité, ni pouvoir partagé : %s."
            % (r["n"], LETTRES_F[len(r["seuls"])], " et ".join(r["seuls"])))
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="pv-t pv-d" font-family="%s">'
         % (W, H + cart_h, FONT),
         '<title id="pv-t">%s</title><desc id="pv-d">%s</desc>' % (esc(titre), esc(desc)),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + cart_h),
         txt(0, 18, "Les huit dispositions que l’article 19 dispense de contreseing", 13, INK, weight="600"),
         txt(0, 36, "ce que le texte de chaque article exige ou fait intervenir", 12, INK2)]
    for k, (_, lib) in enumerate(ATTRIBUTS):
        cx = col0 + colw * k + colw / 2
        mots, lignes, cur = lib.split(), [], ""
        for m in mots:
            if len(cur) + len(m) > 15 and cur:
                lignes.append(cur)
                cur = m
            else:
                cur = (cur + " " + m).strip()
        lignes.append(cur)
        if len(lignes) > 5:  # jamais de troncature silencieuse d'un libellé (défaut vu le 06/10 : « D'autres » perdu)
            raise Arret("figure : libellé de colonne trop long (%d lignes) : %r" % (len(lignes), lib))
        for i, l in enumerate(lignes):
            e.append(txt(cx, top - 12 - 13 * (len(lignes) - 1 - i), l, 10, INK2, "middle"))
    for i, ent in enumerate(inv):
        y = top + pas * i + pas / 2
        if i % 2 == 0:
            e.append('<rect x="0" y="%.1f" width="%d" height="%d" fill="#f7f5f0"/>' % (y - pas / 2, W, pas))
        e.append(txt(0, y + 4, ent.get("court", ent["pouvoir"]), 11, INK))
        e.append(txt(col0 - 10, y + 4, "art. " + ent["renvoi"], 10, MUTED, "end"))
        for k, (a, _) in enumerate(ATTRIBUTS):
            cx = col0 + colw * k + colw / 2
            if ent.get(a):
                e.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>' % (cx, y, BLEU))
            else:
                e.append('<circle cx="%.1f" cy="%.1f" r="6.5" fill="none" stroke="%s" stroke-width="1.5"/>' % (cx, y, GRID))
    y0 = H + 2
    src = "Constitution du 4 octobre 1958, art. 8, 11, 12, 16, 18, 19, 54, 56, 61, versions en vigueur lues sur Légifrance"
    note = "Case pleine : citation exacte de l’article (liste sur la page). Case vide : rien dans cet article ; ni autres articles, ni pratique."
    e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID))
    for k, (t, c) in enumerate(((src, INK2), (note, INK2), (LICENCE, MUTED))):
        e.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, c, esc(t)))
    e.append("</svg>")
    return "\n".join(e)


def fiches_figures(svg: str, A: dict) -> dict:
    titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
    cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
    if len(cart) != 3 or cart[-1] != LICENCE:
        raise Arret("fiche : cartouche illisible dans le SVG")
    montre = ("Sur les %s dispositions que l'article 19 dispense de contreseing, %s seulement ne contiennent ni condition "
              "préalable, ni intervention ultérieure d'un autre acteur, ni pouvoir de même nature attribué à d'autres autorités : %s. "
              "Cette observation ne signifie pas que le président ne disposerait que de %s pouvoirs propres."
              % (A["n_renvois"], A["n_seuls"], A["seuls_liste"], A["n_seuls"]))
    return {"fr": [dict(id="article19", fichier=FIG, titre=titre, montre=montre, source=cart[0], precaution=cart[1])]}


def csv_texte(r: dict, base: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["renvoi", "pouvoir", "attribut", "present", "article", "citation", "legiarti", "lu_le"])
    for e in r["inventaire"]:
        for a in ["acte"] + [x for x, _ in ATTRIBUTS]:
            c = e.get(a)
            art = base["articles"][str(c["art"])] if c else None
            w.writerow([e["renvoi"], e["pouvoir"], a, "oui" if c else "non", c["art"] if c else "", c["cite"] if c else "",
                        art["legiarti"] if art else "", art["lu_le"] if art else ""])
    for c in r["regles"]:
        art = base["articles"][str(c["art"])]
        w.writerow(["", "qui fixe les regles : " + c["objet"], "regle", "oui", c["art"], c["cite"], art["legiarti"], art["lu_le"]])
    return buf.getvalue()


def autotest(base: dict, textes: dict) -> list[str]:
    """Deux mutations réelles : chacune DOIT faire mordre sa garde, sinon le contrôle est réputé absent."""
    out = []
    m = copy.deepcopy(base)
    m["inventaire_19"][2]["condition"]["cite"] += " sans délai"
    try:
        calculer(m, textes)
        raise Arret("mutation citation : G2 n'a pas mordu, controle ABSENT")
    except Arret as e:
        if not str(e).startswith("G2"):
            raise
        out.append("citation alteree -> " + str(e)[:60])
    m = copy.deepcopy(base)
    fiche = next(p for p in m["pouvoirs"] if "«" in (p.get("portee_texte") or ""))
    fiche["portee_texte"] = fiche["portee_texte"].replace("«", "« selon toute vraisemblance", 1)
    try:
        calculer(m, textes)
        raise Arret("mutation guillemets de fiche : G2 etendue n'a pas mordu, controle ABSENT")
    except Arret as e:
        if not str(e).startswith("G2 fiche"):
            raise
        out.append("guillemets de fiche alteres -> " + str(e)[:60])
    m = copy.deepcopy(base)
    del m["inventaire_19"][4]
    try:
        calculer(m, textes)
        raise Arret("mutation renvoi : G3 n'a pas mordu, controle ABSENT")
    except Arret as e:
        if not str(e).startswith("G3"):
            raise
        out.append("renvoi retire -> " + str(e)[:60])
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def _main() -> int:
    check = "--check" in sys.argv[1:]
    base = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    textes = charger_articles(base)
    r, gardes = calculer(base, textes)
    for m in autotest(base, textes):
        log("autotest : la mutation a mordu : " + m)
    lus = [str(base["articles"][str(c["art"])]["lu_le"]) for e in r["inventaire"]
           for c in [e.get(k) for k in ["acte"] + [a for a, _ in ATTRIBUTS]] if c]
    lus += [str(base["articles"][str(c["art"])]["lu_le"]) for c in r["regles"]]
    r["releve_le"], r["lu_min"] = max(lus), min(lus)
    A = affichage(r)
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(gardes))
        return 0
    try:
        import cairosvg
    except ImportError:
        raise Arret("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout")
    svg = figure(r)
    fiches = fiches_figures(svg, A)
    csvt = csv_texte(r, base)
    payload = {
        "releve_le": r["releve_le"],
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; texte de la Constitution : Légifrance (DILA), Licence Ouverte",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Décider, E1",
                 "definitions": dict(ATTRIBUTS),
                 "lecture": "Une case renseignée = une citation exacte de l'article indiqué ; une case vide ne dit rien des "
                            "autres articles ni de la pratique institutionnelle."},
        "gardes": gardes,
        "inventaire": [dict(e, legifrance={k: LEGIFRANCE + base["articles"][str(e[k]["art"])]["legiarti"]
                                            for k in ["acte"] + [a for a, _ in ATTRIBUTS] if e.get(k)})
                       for e in r["inventaire"]],
        "regles": r["regles"],
        "comptes": dict(r["compte"], n=r["n"], sans_condition_ni_autre_autorite_ni_partage=r["seuls_renvois"]),
        "affichage": A,
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    if (OUT_DATA.exists() and OUT_DATA.read_text(encoding="utf-8") == txt_json and OUT_CSV.exists()
            and OUT_CSV.read_text(encoding="utf-8-sig") == csvt and (OUT_IMG / (FIG + ".svg")).exists()
            and (OUT_IMG / (FIG + ".svg")).read_text(encoding="utf-8") == svg and (OUT_IMG / (FIG + ".png")).exists()):
        log("Donnees et figure identiques : rien ecrit.")
        return 0
    OUT_DATA.write_text(txt_json, encoding="utf-8")
    OUT_STATIC.write_text(txt_json, encoding="utf-8")
    OUT_CSV.write_text(csvt, encoding="utf-8-sig", newline="\n")
    (OUT_IMG / (FIG + ".svg")).write_text(svg, encoding="utf-8")
    cairosvg.svg2png(url=str(OUT_IMG / (FIG + ".svg")), write_to=str(OUT_IMG / (FIG + ".png")), output_width=1440,
                     background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for g in gardes:
        log("OK " + g)
    log("Ecrit : data/pouvoirs_president_donnees.json, static/pouvoirs_president_donnees.{json,csv}, "
        "data/figures_pouvoirs.json, static/img/%s.svg + .png" % FIG)
    return 0


if __name__ == "__main__":
    sys.exit(main())
