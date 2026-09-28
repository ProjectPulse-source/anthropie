#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures et données de la page « Qui paie vraiment la dette publique ? ».

    python scripts/generer_figures_qui_paie.py

Arbitrage PRO-20260921-DIPTYQUE, étape 3 : trois figures, et non quatre par
symétrie avec la page du coût.

  F1  qui-paie-detention      Qui emprunte ? Qui détient les titres de l'État ?
                              DEUX panneaux, sans flux entre eux : A en valeur
                              nominale (INSEE), B en valeur de marché (Banque de
                              France via l'AFT). Les emboîter inviterait à
                              multiplier des parts de marché par des montants
                              nominaux.
  F2  qui-paie-redistribution Prélèvements et transferts publics par dixième de
                              niveau de vie (Insee, comptes nationaux distribués
                              2023). Décrit qui contribue et qui reçoit
                              aujourd'hui ; ne mesure pas l'incidence de la dette.
  F3  qui-paie-mecanismes     Schéma NON quantitatif des canaux de répartition.

SOURCES — une seule chacune, jamais recopiée à la main :
  - F1 : le registre du livre (03_LIVRES/dette-publique/01_SOURCE/
    REGISTRE_DONNEES.yaml, bloc infographie_detention) -- la même source que la
    p. 101 du livre. Le site n'en garde qu'un instantané, régénéré ici ; la
    révision annuelle du livre (maj_edition.py) relance ce script.
  - F2 : le fichier de l'Insee archivé dans scripts/sources/, contrôlé par son
    empreinte. Un fichier remplacé sans que l'empreinte suive arrête tout.

Sorties : static/img/qui-paie-*.svg et .png, data/figures_qui_paie.json (cartes
du bloc « Réutiliser »), data/ et static/qui_paie_donnees.json (données publiées,
et bloc `affichage` lu par le shortcode qp-val : aucun chiffre en dur dans la
prose de la page).

Les PNG sont rendus dans la MÊME exécution que les SVG, et le script s'arrête si
cairosvg manque : SVG et PNG ne peuvent donc pas diverger, et aucun contrôle de
dérive n'est nécessaire (à la différence des figures de la page du coût, rendues
en CI par une étape tolérante).

Les phrases qualitatives de la page (« plus de la moitié », « varient beaucoup
moins ») sont vérifiées ici contre les données : si l'une cesse d'être vraie, le
script s'arrête au lieu de laisser la prose mentir.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
REGISTRE = Path(os.environ.get(
    "REGISTRE_DETTE",
    r"D:\PRO\03_LIVRES\dette-publique\01_SOURCE\REGISTRE_DONNEES.yaml"))
XLSX = REPO / "scripts" / "sources" / "insee_IA118_comptes_distribues_2023.xlsx"
XLSX_SHA256 = "6f5f27809be12e192afdca5008022a0e0c63f832869d29be8dc837abbdeec0eb"
XLSX_URL = "https://www.insee.fr/fr/statistiques/8974371"

# DATE DE RELEVÉ DES SOURCES, publiée dans la citation prête à copier du bloc
# « Réutiliser ». Elle était écrite à la main et ne s'appuyait sur RIEN : le XLSX
# de l'Insee avait bien sa garde d'empreinte, le registre du livre n'en avait
# aucune. Le registre est pourtant une source VIVANTE — la révision annuelle du
# livre la régénère. Il pouvait donc changer, les chiffres de la page suivre, et
# la date de relevé rester au 21/09 sans que rien ne le signale : la citation
# qu'un tiers reprend sous licence aurait porté une date fausse.
# Les deux empreintes gouvernent maintenant la date. Une source qui bouge sans
# que la date suive arrête la génération — l'erreur devient impossible au lieu
# d'être documentée.
REGISTRE_SHA256 = "5f765eeb27581421b08dac9622af0cb0f767cb73c48a3b29bd6bcb75811b9b37"
SOURCES_RELEVEES_LE = "21 septembre 2026"

IMG = REPO / "static" / "img"
URL_PAGE = "stephane-lalut.com/qui-paie-la-dette-publique/"

# Palette — charte du 2026-09-28 (mémoire feedback_langage_graphique_figures,
# rappelée dans CLAUDE.md § « Figures de données »). DEUX couleurs de données au
# maximum, hors gris, et la même grandeur toujours de la même couleur :
#   C1 bleu profond = ce qui est reçu (transferts, bénéficiaires nets) et le stock
#                     de dette — même bleu que la page du coût ;
#   C2 orange       = ce qui est versé, et les intérêts — donc aussi les porteurs
#                     des titres, qui en sont les destinataires ;
#   SEC gris moyen  = série secondaire : la part imputée (services publics
#                     valorisés), celle qui porte la convention de calcul.
# L'aqua #1baf7a du triplet de septembre est RETIRÉ : il faisait une troisième
# couleur de données, ce que la charte interdit, et il avertissait en contraste.
# Le gris pour une série secondaire a son précédent validé dans
# update_dette_insee.py (build_svg_masses) : aucune teinte nouvelle n'entre ici,
# donc rien à soumettre à validate_palette.js.
C1, C2 = "#184f95", "#eb6834"
INK, INK2, MUTED, GRID, AXIS = "#2b2a28", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
SEC = MUTED
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
# Échelle typographique COMMUNE aux deux générateurs du dépôt (mêmes noms, mêmes
# valeurs que update_dette_insee.py) : les figures des deux volets du dossier
# forment une famille, et non deux collections.
TY_TITRE, TY_AXE, TY_ANNOT, TY_VALEUR, TY_MINEUR = 13, 11, 12, 15, 11
NBSP = "\u00a0"
W = 720


def fail(msg: str) -> None:
    print("ECHEC : " + msg)
    sys.exit(1)


def fr(v: float, dec: int = 0) -> str:
    s = ("{:,." + str(dec) + "f}").format(v)
    return s.replace(",", NBSP).replace(".", ",")


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None):
    w = ' font-weight="%s"' % weight if weight else ""
    return ('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, size, fill, anchor, w, esc(s)))


def etiquettes_directes(x: float, bouts: list, y_min: float, y_max: float,
                        ecart: float = 34.0) -> list[str]:
    """Nomme chaque série À CÔTÉ d'elle, sans légende séparée (charte du 28/09).

    `bouts` : (y visée, couleur, nom, précision) — la hauteur visée est le milieu
    du segment de la DERNIÈRE catégorie, celle que la lecture atteint en dernier.
    Le placement est CALCULÉ, jamais estimé : tri, écart minimum garanti, puis
    bornage dans [y_min, y_max]. Sans cela, deux séries voisines dans la dernière
    colonne écriraient l'une sur l'autre — le défaut qui a fait sortir du cadre la
    troisième étiquette de la légende le 21/09, ici rendu impossible.
    """
    b = sorted(bouts, key=lambda t: t[0])
    for i in range(1, len(b)):
        if b[i][0] - b[i - 1][0] < ecart:
            b[i] = (b[i - 1][0] + ecart,) + tuple(b[i][1:])
    # Le paquet peut dépasser par le bas après décalage : on le remonte en bloc.
    debord = b[-1][0] - y_max
    if debord > 0:
        b = [(y - debord,) + tuple(reste) for y, *reste in b]
    b = [(max(y, y_min),) + tuple(reste) for y, *reste in b]
    out = []
    for y, col, nom, precision in b:
        out.append(txt(x, y, nom, TY_AXE, col, weight="600"))
        if precision:
            out.append(txt(x, y + 13, precision, TY_AXE - 1, MUTED))
    return out


def cartouche(y0: float, lignes: list[tuple[str, str]]) -> list[str]:
    out = ['<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
           % (y0, W, y0, GRID)]
    for i, (s, col) in enumerate(lignes):
        out.append('<text x="0" y="%.1f" font-family="%s" font-size="9" fill="%s">%s</text>'
                   % (y0 + 13 + i * 12, FONT, col, esc(s)))
    return out


def entete(h: float, ident: str, titre: str, desc: str) -> list[str]:
    # Chiffres tabulaires : mêmes largeurs, donc les valeurs et les graduations
    # s'alignent d'une figure à l'autre et d'un volet du dossier à l'autre (28/09).
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" '
            'font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h, ident, ident, FONT),
            '<title id="%s-t">%s</title>' % (ident, esc(titre)),
            '<desc id="%s-d">%s</desc>' % (ident, esc(desc))]


# ------------------------------------------------------------------ données
def lire_registre() -> dict:
    try:
        import yaml
    except ImportError:
        fail("PyYAML absent : le registre du livre ne peut pas être lu")
    if not REGISTRE.is_file():
        fail("registre introuvable : %s (variable REGISTRE_DETTE pour un autre chemin)" % REGISTRE)
    brut = REGISTRE.read_bytes()
    sha = hashlib.sha256(brut).hexdigest()
    if sha != REGISTRE_SHA256:
        fail("empreinte du registre du livre changée (%s…) : relire les valeurs à la "
             "source, puis mettre à jour REGISTRE_SHA256 ET SOURCES_RELEVEES_LE — sans "
             "quoi la page publierait une date de relevé fausse" % sha[:12])
    reg = yaml.safe_load(brut.decode("utf-8"))
    info = reg["infographie_detention"]
    total_txt = reg["grandeurs"]["dette_fin_annee_mdeur"]["valeur_imprimee"]
    periode_a = reg["grandeurs"]["dette_fin_annee_mdeur"]["periode"]
    total = float(total_txt.replace(" ", "").replace(NBSP, "").replace(",", "."))
    ss, det = info["sous_secteurs"], info["detenteurs_etat"]
    somme = sum(s["mdeur"] for s in ss)
    if abs(somme - total) > 1.0:
        fail("sous-secteurs %s Md€ contre un total de %s Md€" % (somme, total_txt))
    if abs(sum(d["pct"] for d in det) - 100) > 0.05:
        fail("les parts des détenteurs ne somment pas à 100")
    ff = reg["grandeurs"]["foyers_fiscaux"]
    foyers = float(str(ff["valeur_imprimee"]).replace(",", "."))
    if not 30 < foyers < 50:
        fail("foyers fiscaux hors plage plausible : %s millions" % foyers)
    return {"ss": ss, "det": det, "total": total, "total_txt": total_txt,
            "periode_a": periode_a, "sources": info["sources"],
            "foyers": {"millions": foyers, "periode": ff["periode"],
                       "periode_en": ff.get("periode_en", ""),
                       "source": ff["source_citee"], "url": ff.get("url_source", "")},
            "sha256": sha}


def lire_insee() -> dict:
    if not XLSX.is_file():
        fail("fichier Insee absent : %s" % XLSX)
    sha = hashlib.sha256(XLSX.read_bytes()).hexdigest()
    if sha != XLSX_SHA256:
        fail("empreinte du fichier Insee changée (%s) : relire la source, puis mettre "
             "à jour XLSX_SHA256" % sha[:12])
    import openpyxl
    wb = openpyxl.load_workbook(XLSX, data_only=True)

    def ligne(feuille: str, debut: str) -> list:
        for r in wb[feuille].iter_rows(values_only=True):
            if r[0] and str(r[0]).startswith(debut):
                return [x for x in r[1:] if x is not None]
        fail("%s : ligne « %s » introuvable" % (feuille, debut))

    ws = wb["Figure 1c"]
    entetes = [x for x in next(r for r in ws.iter_rows(values_only=True)
                               if r[0] == "Nature des revenus")[1:] if x is not None]
    if entetes != ["D%d" % i for i in range(1, 11)] + ["Ensemble"]:
        fail("Figure 1c : colonnes inattendues %s" % entetes)
    prel = ligne("Figure 1c", "Prélèvements")
    esp = ligne("Figure 1c", "Prestations sociales en espèces")
    nat = ligne("Figure 1c", "Transferts non monétaires")
    solde_uc = ligne("Figure 2a", "Solde de la redistribution publique nationale")[-1]
    solde_md = ligne("Figure 2b", "Solde de la redistribution publique nationale")[-1]
    for nom, l in (("prélèvements", prel), ("prestations", esp), ("transferts", nat)):
        if len(l) != 11:
            fail("Figure 1c : %s sur %d colonnes" % (nom, len(l)))
    net = ligne("Figure 2a", "Transferts nets de la redistribution publique nationale")
    part_benef = ligne("Figure 2a", "Part de personnes bénéficiaires nettes")
    wsa = wb["Figure 1e"]
    age_entetes = [x for x in next(r for r in wsa.iter_rows(values_only=True)
                                   if r[0] == "Nature des revenus")[1:] if x is not None]
    if len(age_entetes) != 6 or age_entetes[-1] != "Ensemble":
        fail("Figure 1e : colonnes inattendues %s" % age_entetes)
    age = {"groupes": [str(x).replace("\u00a0", " ") for x in age_entetes[:5]],
           "prel": ligne("Figure 1e", "Prélèvements"),
           "esp": ligne("Figure 1e", "Prestations sociales en espèces"),
           "nat": ligne("Figure 1e", "Transferts non monétaires")}
    # Conservation : les trois lignes de la figure 1c redonnent le solde net publié.
    for i in range(10):
        if abs(prel[i] + esp[i] + nat[i] + net[i]) > 200:   # arrondis Insee à la centaine
            fail("dixième %d : i+ii+iii = %s mais transferts nets publiés = %s"
                 % (i + 1, prel[i] + esp[i] + nat[i], net[i]))
    return {"prel": prel, "esp": esp, "nat": nat, "solde_uc": solde_uc,
            "solde_md": solde_md, "net": net, "part_benef": part_benef, "age": age,
            "sha256": sha}


# ------------------------------------------------------------------ F1
def svg_detention(r: dict) -> tuple[str, int]:
    ss, det, total = r["ss"], r["det"], r["total"]
    e = []
    y = 50
    corps = [txt(0, 22, "Qui emprunte ? Qui détient les titres de l'État ? Deux questions, deux champs",
                 TY_TITRE, INK2),
             txt(0, y, "A · Qui emprunte ? Contribution des administrations à la dette publique, "
                 + r["periode_a"], TY_ANNOT, INK, weight="600"),
             txt(0, y + 16, "Valeur nominale, en milliards d'euros · total " + r["total_txt"]
                 + NBSP + "Md€", TY_AXE, MUTED)]
    x0, larg = 190, 400
    y = y + 34
    # ANCRAGE. Dans une série ordonnée par rangs et non par le temps, la valeur qui
    # ancre la lecture n'est pas la dernière mais la DOMINANTE : elle se calcule
    # (max), elle ne se choisit pas au regard — sinon un jour l'emphase resterait
    # sur un rang que les données ont cessé de placer en tête.
    domin_a = max(x["mdeur"] for x in ss)
    for s in ss:
        w = max(2.0, larg * s["mdeur"] / domin_a)
        pct = 100 * s["mdeur"] / total
        fort = s["mdeur"] == domin_a
        corps.append(txt(x0 - 10, y + 11, s["libelle"], TY_AXE, INK2, "end"))
        corps.append('<rect x="%d" y="%.1f" width="%.1f" height="14" rx="3" fill="%s"/>'
                     % (x0, y, w, C1))
        corps.append(txt(x0 + w + 8, y + 11, "%s%sMd€ · %s%s%%" % (fr(s["mdeur"]), NBSP,
                                                                   fr(pct), NBSP),
                         TY_ANNOT if fort else TY_AXE, C1 if fort else INK2,
                         weight="600" if fort else None))
        y += 22
    y += 16
    corps.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (y, W, y, AXIS))
    y += 28
    corps.append(txt(0, y, "B · Qui détient les titres négociables de l'État ? 1er trimestre 2026",
                     TY_ANNOT, INK, weight="600"))
    corps.append(txt(0, y + 16, "Valeur de marché, en % · classement par résidence du détenteur, "
                     "non par nationalité", TY_AXE, MUTED))
    y += 34
    noms = {"Autres (français)": "Autres porteurs français *",
            "Établissements de crédit français": "Banques françaises",
            "Assureurs français": "Assureurs français",
            "OPCVM français": "Fonds (OPCVM) français"}
    domin_b = max(x["pct"] for x in det)
    for d in det:
        w = max(2.0, larg * d["pct"] / domin_b)
        fort = d["pct"] == domin_b
        corps.append(txt(x0 - 10, y + 11, noms.get(d["libelle"], d["libelle"]),
                         TY_AXE, INK2, "end"))
        corps.append('<rect x="%d" y="%.1f" width="%.1f" height="14" rx="3" fill="%s"/>'
                     % (x0, y, w, C2))
        corps.append(txt(x0 + w + 8, y + 11, "%s%s%%" % (fr(d["pct"], 1), NBSP),
                         TY_ANNOT if fort else TY_AXE, C2 if fort else INK2,
                         weight="600" if fort else None))
        y += 22
    corps.append(txt(0, y + 10, "* dont la Banque de France (programmes de l'Eurosystème) : "
                     "part non publiée par la source.", TY_AXE - 1, MUTED))
    y += 30
    h = int(y + 13 + 12 * 3 + 8)
    desc = ("Deux panneaux séparés, sans lien de proportion entre eux. A, en valeur nominale : "
            + "; ".join("%s %s Md€" % (s["libelle"], fr(s["mdeur"])) for s in ss)
            + ", sur %s Md€, %s. B, en valeur de marché, porteurs des titres négociables de "
              "l'État au 1er trimestre 2026 : " % (r["total_txt"], r["periode_a"])
            + "; ".join("%s %s %%" % (noms.get(d["libelle"], d["libelle"]).rstrip(" *"),
                                       fr(d["pct"], 1)) for d in det) + ".")
    e += entete(h, "qp-det", "Qui emprunte ? Qui détient les titres de l'État ?", desc)
    e += corps
    e += cartouche(y, [
        ("A : INSEE, Informations rapides n° 79 (27/03/2026), dette de Maastricht par "
         "sous-secteur · B : Banque de France, via l'AFT", INK2),
        ("Deux champs distincts. A : valeur nominale ; B : valeur de marché. "
         "La détention ne mesure pas la charge finale.", INK2),
        ("Compilation Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)])
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ F2
def svg_redistribution(d: dict) -> tuple[str, int]:
    prel = [v / 1000 for v in d["prel"][:10]]
    esp = [v / 1000 for v in d["esp"][:10]]
    nat = [v / 1000 for v in d["nat"][:10]]
    vmax, vmin = 35, -100
    top, bas = 58, 340
    k = (bas - top) / (vmax - vmin)

    def Y(v):
        return top + (vmax - v) * k

    # mr : la marge droite n'est plus un bord, c'est la place des étiquettes
    # directes. La légende à pastilles a disparu avec elle.
    ml, mr = 46, 168
    pas = (W - ml - mr) / 10
    bw = 34
    c = []
    c.append(txt(0, 22, "Prélèvements et transferts publics par dixième de niveau de vie, 2023, "
                 "en milliers d'euros par UC", TY_TITRE, INK2))
    # Grille HORIZONTALE seule, cinq lignes, sans ligne au ras du cadre : une
    # graduation de plus ne se lirait pas mieux, elle ferait une boîte.
    for g in (-75, -50, -25, 0, 25):
        yy = Y(g)
        c.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, yy, W - mr, yy, AXIS if g == 0 else GRID))
        c.append(txt(ml - 6, yy + 4, fr(g) if g >= 0 else "−" + fr(-g), TY_AXE, MUTED, "end"))
    for i in range(10):
        cx = ml + pas * (i + 0.5)
        x = cx - bw / 2
        y0 = Y(0)
        h1 = esp[i] * k
        h2 = nat[i] * k
        fort = i == 9                      # ancrage : le dernier dixième
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="%s"/>'
                 % (x, y0 - h1, bw, h1, C1))
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                 % (x, y0 - h1 - 2 - h2, bw, h2, SEC))
        hp = -prel[i] * k
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                 % (x, y0 + 2, bw, hp - 2, C2))
        tv, cv = (TY_ANNOT, INK) if fort else (TY_AXE - 1, INK2)
        pv = "600" if fort else None
        c.append(txt(cx, y0 - h1 - h2 - 7, fr(esp[i] + nat[i], 1), tv, cv, "middle", weight=pv))
        c.append(txt(cx, y0 + hp + 13, "−" + fr(-prel[i], 1), tv, cv, "middle", weight=pv))
        c.append(txt(cx, bas + 16, "D%d" % (i + 1), TY_AXE,
                     INK if fort else MUTED, "middle", weight=pv))
    # Étiquetage DIRECT : chaque série nommée à la hauteur de son segment dans le
    # dernier dixième, celui que la lecture atteint en dernier.
    y0 = Y(0)
    h1, h2 = esp[9] * k, nat[9] * k
    c += etiquettes_directes(W - mr + 14, [
        (y0 - h1 / 2 + 4, C1, "Prestations", "en espèces"),
        (y0 - h1 - 2 - h2 / 2 + 4, SEC, "Transferts non monétaires", "services publics valorisés"),
        (y0 + 2 + (-prel[9] * k) / 2 + 4, C2, "Prélèvements", "impôts et cotisations"),
    ], top + 8, bas - 12)
    c.append(txt(ml, bas + 32, "← 10 % les plus modestes", TY_AXE - 1, MUTED))
    c.append(txt(W - mr, bas + 32, "10 % les plus aisés →", TY_AXE - 1, MUTED, "end"))
    y = bas + 46
    h = int(y + 13 + 12 * 3 + 8)
    desc = ("Barres par dixième de niveau de vie, en 2023, en milliers d'euros par unité de "
            "consommation. Au-dessus de zéro, les transferts reçus (prestations en espèces et "
            "transferts non monétaires) : de %s pour le premier dixième à %s pour le dernier. "
            "Sous zéro, les prélèvements : de %s à %s." % (
                fr(esp[0] + nat[0], 1), fr(esp[9] + nat[9], 1), fr(-prel[0], 1), fr(-prel[9], 1)))
    e = entete(h, "qp-red", "Prélèvements et transferts publics par dixième de niveau de vie, 2023",
               desc) + c
    e += cartouche(y, [
        ("Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, 16/04/2026, figure 1c) "
         "· France, euros par UC", INK2),
        ("Répartition avec conventions d'imputation ; ne mesure pas l'incidence spécifique "
         "de la dette.", INK2),
        ("Compilation Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)])
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ F4
def svg_solde_net(d: dict) -> tuple[str, int]:
    """Contributeurs nets et bénéficiaires nets, par dixième.

    DEUX panneaux, deux unités : A en euros par UC, B en part de personnes.
    Jamais deux échelles sur un même axe.
    """
    net = [v / 1000 for v in d["net"][:10]]      # convention Insee : + = verse net
    part = d["part_benef"][:10]
    c = [txt(0, 22, "Qui verse plus qu'il ne reçoit ? Solde des transferts publics par dixième "
             "de niveau de vie, 2023", TY_TITRE, INK2)]
    ml, mr = 46, 12
    pas = (W - ml - mr) / 10
    bw = 34
    vmax, vmin = 60, -25
    top, bas = 84, 260
    k = (bas - top) / (vmax - vmin)

    def Y(v):
        return top + (vmax - v) * k

    c.append(txt(0, 38, "A · Transferts nets, en milliers d'euros par UC", TY_AXE, MUTED))
    # Clé de lecture DIRECTE : chaque énoncé porte la couleur des barres qu'il
    # décrit, et se pose DU CÔTÉ où elles se trouvent — les dixièmes bénéficiaires
    # nets à gauche, les contributeurs nets à droite. Une clé posée du côté opposé
    # à ses barres oblige le lecteur à traverser la figure pour la vérifier.
    # Deux ancrages opposés sur une ligne vide : aucune largeur à estimer.
    c.append(txt(0, 54, "en dessous de zéro : reçoit plus qu'il ne verse", TY_AXE - 1, C1))
    c.append(txt(W - mr, 54, "au-dessus : verse plus qu'il ne reçoit", TY_AXE - 1, C2, "end"))
    for g in range(-20, 61, 20):
        yy = Y(g)
        c.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, yy, W - mr, yy, AXIS if g == 0 else GRID))
        c.append(txt(ml - 6, yy + 4, fr(g) if g >= 0 else "−" + fr(-g), TY_AXE, MUTED, "end"))
    for i in range(10):
        cx = ml + pas * (i + 0.5)
        v = net[i]
        y0 = Y(0)
        haut = abs(v) * k
        col = C2 if v > 0 else C1
        y = y0 - haut - 2 if v > 0 else y0 + 2
        fort = i == 9
        # Plancher de 2 px : un dixième presque équilibré (D7, −1,8) donnait une
        # barre d'un pixel, et la charte interdit d'attacher une valeur à une
        # marque invisible. La distorsion reste inférieure au pixel d'affichage.
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                 % (cx - bw / 2, y, bw, max(haut - 2, 2), col))
        etiq = ("+" if v > 0 else "−") + fr(abs(v), 1)
        tv, cv = (TY_ANNOT, INK) if fort else (TY_AXE - 1, INK2)
        pv = "600" if fort else None
        c.append(txt(cx, (y - 6) if v > 0 else (y + haut + 11), etiq, tv, cv, "middle", weight=pv))
        c.append(txt(cx, bas + 30, "D%d" % (i + 1), TY_AXE,
                     INK if fort else MUTED, "middle", weight=pv))
    y = bas + 56
    c.append(txt(0, y, "B · Part de personnes bénéficiaires nettes, en %", TY_AXE, MUTED))
    top2, bas2 = y + 16, y + 106
    k2 = (bas2 - top2) / 100.0
    for g in (0, 50, 100):
        yy = bas2 - g * k2
        c.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, yy, W - mr, yy, AXIS if g == 0 else GRID))
        c.append(txt(ml - 6, yy + 4, fr(g), TY_AXE, MUTED, "end"))
    for i in range(10):
        cx = ml + pas * (i + 0.5)
        haut = part[i] * k2
        fort = i == 9
        # Bénéficiaires nets : même bleu qu'au panneau A, où ils sont sous zéro.
        # Une même grandeur ne change pas de couleur d'un panneau à l'autre.
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                 % (cx - bw / 2, bas2 - haut, bw, haut, C1))
        c.append(txt(cx, bas2 - haut - 6, fr(part[i]) + NBSP + "%",
                     TY_ANNOT if fort else TY_AXE - 1, INK if fort else INK2, "middle",
                     weight="600" if fort else None))
    y = bas2 + 30
    h = int(y + 13 + 12 * 3 + 8)
    desc = ("Deux panneaux. A : transferts nets par dixième de niveau de vie, en milliers d'euros "
            "par unité de consommation ; en moyenne, les sept premiers dixièmes reçoivent plus qu'ils ne "
            "versent, les trois derniers versent plus qu'ils ne reçoivent, le dernier de %s. "
            "B : part de personnes bénéficiaires nettes, de %s %% dans le premier dixième à "
            "%s %% dans le dernier." % (fr(net[9], 1), fr(part[0]), fr(part[9])))
    e = entete(h, "qp-net", "Contributeurs nets et bénéficiaires nets par dixième, 2023", desc) + c
    e += cartouche(y, [
        ("Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, 16/04/2026, figure 2a) "
         "· France, euros par UC", INK2),
        ("Moyennes par UC ; pensions et services publics valorisés (imputés) inclus ; solde d'une "
         "année, non d'une vie.", INK2),
        ("Compilation Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)])
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ F5
def svg_age(d: dict) -> tuple[str, int]:
    a = d["age"]
    prel = [v / 1000 for v in a["prel"][:5]]
    esp = [v / 1000 for v in a["esp"][:5]]
    nat = [v / 1000 for v in a["nat"][:5]]
    vmax, vmin = 52, -40
    top, bas = 58, 330
    k = (bas - top) / (vmax - vmin)

    def Y(v):
        return top + (vmax - v) * k

    ml, mr = 46, 168          # mr : place des étiquettes directes, plus de légende
    pas = (W - ml - mr) / 5
    bw = 64
    c = [txt(0, 22, "Prélèvements et transferts publics par âge du ménage, 2023, "
             "en milliers d'euros par UC", TY_TITRE, INK2)]
    for g in (-25, 0, 25, 50):
        yy = Y(g)
        c.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                 % (ml, yy, W - mr, yy, AXIS if g == 0 else GRID))
        c.append(txt(ml - 6, yy + 4, fr(g) if g >= 0 else "−" + fr(-g), TY_AXE, MUTED, "end"))
    dernier = len(a["groupes"]) - 1
    for i, g in enumerate(a["groupes"]):
        cx = ml + pas * (i + 0.5)
        x = cx - bw / 2
        y0 = Y(0)
        h1, h2 = esp[i] * k, nat[i] * k
        fort = i == dernier
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="%s"/>'
                 % (x, y0 - h1, bw, h1, C1))
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                 % (x, y0 - h1 - 2 - h2, bw, h2, SEC))
        hp = -prel[i] * k
        c.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="2" fill="%s"/>'
                 % (x, y0 + 2, bw, hp - 2, C2))
        tv, cv = (TY_ANNOT, INK) if fort else (TY_AXE - 1, INK2)
        pv = "600" if fort else None
        c.append(txt(cx, y0 - h1 - h2 - 7, fr(esp[i] + nat[i], 1), tv, cv, "middle", weight=pv))
        c.append(txt(cx, y0 + hp + 13, "−" + fr(-prel[i], 1), tv, cv, "middle", weight=pv))
        c.append(txt(cx, bas + 16, g, TY_AXE, INK if fort else MUTED, "middle", weight=pv))
    y0 = Y(0)
    h1, h2 = esp[dernier] * k, nat[dernier] * k
    c += etiquettes_directes(W - mr + 14, [
        (y0 - h1 / 2 + 4, C1, "Prestations en espèces", "dont les retraites"),
        (y0 - h1 - 2 - h2 / 2 + 4, SEC, "Transferts non monétaires", "services publics valorisés"),
        (y0 + 2 + (-prel[dernier] * k) / 2 + 4, C2, "Prélèvements", "impôts et cotisations"),
    ], top + 8, bas - 12)
    y = bas + 34
    h = int(y + 13 + 12 * 3 + 8)
    desc = ("Barres par groupe d'âge du ménage, en 2023, en milliers d'euros par unité de "
            "consommation. Les transferts reçus passent de %s pour les 18-29 ans à %s pour les "
            "ménages dont l'âge moyen des adultes atteint 65 ans ou plus, tandis que les prélèvements passent de %s à %s."
            % (fr(esp[0] + nat[0], 1), fr(esp[4] + nat[4], 1), fr(-prel[0], 1), fr(-prel[4], 1)))
    e = entete(h, "qp-age", "Prélèvements et transferts publics par âge du ménage, 2023", desc) + c
    e += cartouche(y, [
        ("Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, 16/04/2026, figure 1e) "
         "· groupes d'âge moyen des adultes du ménage", INK2),
        ("Photographie d'une année, non le bilan d'une génération : les pensions de retraite y "
         "sont comptées en transferts reçus.", INK2),
        ("Compilation Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)])
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ F3
def svg_mecanismes() -> tuple[str, int]:
    """Schéma NON quantitatif : trois règles de la charte y sont sans objet.

    Pas de grille, pas de valeur terminale, pas de bande datée — il n'y a ni axe
    ni série. Ce qui s'y applique s'y applique : deux couleurs au maximum (le bleu
    du stock au seul nœud central, le reste à l'encre), boîtes en trait et non en
    aplat, cartouche dans l'image, échelle typographique commune. Exclusion dite,
    non silencieuse.
    """
    c = [txt(0, 22, "Par quels canaux la charge de la dette peut-elle être répartie ?",
             TY_TITRE, INK2)]

    def boite(x, y, w, h, lignes, trait=AXIS, tiret=False, fond="#ffffff"):
        d = ' stroke-dasharray="4 3"' if tiret else ""
        out = ['<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="%s" stroke="%s" '
               'stroke-width="1.5"%s/>' % (x, y, w, h, fond, trait, d)]
        for i, (s, taille, col, gras) in enumerate(lignes):
            out.append(txt(x + 12, y + 20 + i * 16, s, taille, col, weight="600" if gras else None))
        return out

    def fleche(x1, y1, x2, y2):
        return ['<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5" '
                'stroke-dasharray="5 4" marker-end="url(#qp-fl)"/>' % (x1, y1, x2, y2, MUTED)]

    c.append('<defs><marker id="qp-fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
             '</defs>' % MUTED)
    c += boite(1, 150, 200, 74, [("Charge de la dette", TY_ANNOT, INK, True),
                                 ("et sa répartition", TY_ANNOT, INK, True),
                                 ("intérêts, échéances", TY_AXE, INK2, False)], trait=C1)
    canaux = [
        ("Prélèvements", "contribuables : impôts, cotisations"),
        ("Dépenses et prestations", "usagers, bénéficiaires : réduites, gelées, reportées"),
        ("Inflation", "détenteurs de créances et de revenus mal indexés"),
        ("Restructuration (cas extrême)", "porteurs des titres"),
    ]
    y = 44
    for tit, qui in canaux:
        c += boite(300, y, 418, 50, [(tit, TY_ANNOT, INK, True), (qui, TY_AXE, INK2, False)])
        c += fleche(200, 187, 296, y + 25)
        y += 64
    c += boite(1, 44, 200, 70, [("Refinancement", TY_ANNOT, INK, True),
                                ("reporte l'échéance ;", TY_AXE, INK2, False),
                                ("ne désigne aucun perdant", TY_AXE, INK2, False)], tiret=True)
    c += fleche(100, 150, 100, 118)
    c += boite(1, 316, 717, 52, [("En regard : ce que la dette a financé", TY_ANNOT, INK, True),
                                 ("services, prestations, investissements, soutien en crise — "
                                  "bénéfices présents et futurs", TY_AXE, INK2, False)],
               tiret=True, fond="#f7f7f4")
    y = 392
    h = int(y + 13 + 12 * 3 + 8)
    desc = ("Schéma sans quantités. Quatre mécanismes, non exhaustifs, peuvent modifier la charge de la dette et sa répartition, et "
            "se combinent : prélèvements (contribuables), dépenses et prestations (usagers, "
            "bénéficiaires), inflation (détenteurs de créances et de revenus mal indexés), "
            "restructuration, cas extrême (porteurs des titres). Le refinancement reporte "
            "l'échéance sans désigner de perdant. En regard figure ce que la dette a financé.")
    e = entete(h, "qp-mec", "Par quels canaux la charge de la dette peut-elle être répartie ?",
               desc) + c
    e += cartouche(y, [
        ("Synthèse de l'auteur · schéma non quantitatif, flèches d'égale épaisseur", INK2),
        ("Schéma de mécanismes possibles. Aucun poids relatif ni effet causal n'est mesuré ici.",
         INK2),
        ("Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)])
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ texte
def affichage(r: dict, d: dict) -> dict:
    ss = {s["libelle"]: s["mdeur"] for s in r["ss"]}
    det = {x["libelle"]: x["pct"] for x in r["det"]}
    etat_pct = 100 * ss["État"] / r["total"]
    nonres = det["Non-résidents"]
    bafs = det["Établissements de crédit français"] + det["Assureurs français"] + det["OPCVM français"]
    recus = [d["esp"][i] + d["nat"][i] for i in range(10)]
    prel = [-v for v in d["prel"][:10]]
    # Phrases qualitatives de la page : vérifiées ici, sinon arrêt.
    if not nonres > 50:
        fail("la page dit « plus de la moitié » des titres de l'État aux non-résidents : %s %%" % nonres)
    if not etat_pct > 50:
        fail("la page dit que l'État porte l'essentiel de la dette : %s %%" % etat_pct)
    if not (max(recus) / min(recus)) < (max(prel) / min(prel)) / 3:
        fail("la page dit que les transferts reçus varient « beaucoup moins » que les prélèvements")
    if not d["solde_uc"] < 0:
        fail("la page dit que la puissance publique a versé plus qu'elle n'a prélevé")
    net = d["net"][:10]
    part = d["part_benef"][:10]
    bascule = next((i for i, v in enumerate(net) if v > 0), None)
    if bascule is None or not all(v < 0 for v in net[:bascule]):
        fail("solde net : la bascule contributeur/bénéficiaire n'est pas unique (%s)" % net)
    if not part[0] > part[-1]:
        fail("la page dit que la part de bénéficiaires nets décroît avec le niveau de vie")
    # Contraste moyenne / personnes (contre-expertise du 27/09) : un dixième peut être
    # bénéficiaire net EN MOYENNE alors que la majorité de ses membres sont contributeurs
    # nets. La page l'énonce ; il doit rester vrai dans les données, sinon arrêt.
    majo = next((i for i, v in enumerate(part) if v <= 50), len(part))
    if not majo < bascule:
        fail("la page dit que la majorité de bénéficiaires nets s'arrête avant la bascule "
             "du solde moyen (majorité jusqu'à D%d, bascule en D%d)" % (majo, bascule + 1))
    age = d["age"]
    if not (age["esp"][4] > age["esp"][0] and -age["prel"][4] < -age["prel"][0]):
        fail("la page dit que les 65 ans ou plus reçoivent plus et versent moins que les 18-29 ans")
    return {
        "releve_le": SOURCES_RELEVEES_LE,
        "net_bascule": "D%d" % (bascule + 1),
        "net_benef_n": fr(bascule),
        "net_d10": fr(net[9]),
        "net_d1": fr(-net[0]),
        "benef_d1": fr(part[0]), "benef_d10": fr(part[9]),
        "benef_majo_n": fr(majo),
        "benef_dernier_moyen": "D%d" % bascule, "benef_dernier_moyen_pct": fr(part[bascule - 1]),
        "benef_ensemble": fr(d["part_benef"][-1]),
        "age_recu_65": fr(age["esp"][4] + age["nat"][4]),
        "age_prel_65": fr(-age["prel"][4]),
        "age_recu_jeunes": fr(age["esp"][0] + age["nat"][0]),
        "age_prel_5064": fr(-age["prel"][3]),
        "age_esp_65": fr(age["esp"][4]),
        "total_mdeur": r["total_txt"], "periode_a": r["periode_a"],
        "etat_mdeur": fr(ss["État"]), "etat_pct": fr(etat_pct),
        "nonres_pct": fr(nonres, 1), "bafs_pct": fr(bafs, 1),
        "autres_fr_pct": fr(det["Autres (français)"], 1),
        "cd_annee": "2023",
        "d1_prel": fr(prel[0]), "d10_prel": fr(prel[9]),
        "ratio_prel": fr(prel[9] / prel[0]),
        "recu_min": fr(min(recus)), "recu_max": fr(max(recus)),
        "solde_uc": fr(-d["solde_uc"]), "solde_mdeur": fr(-d["solde_md"]),
    }


def main() -> int:
    try:
        import cairosvg
    except ImportError:
        fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout")
    r, d = lire_registre(), lire_insee()
    aff = affichage(r, d)
    figs = [("qui-paie-detention", svg_detention(r)),
            ("qui-paie-redistribution", svg_redistribution(d)),
            ("qui-paie-solde-net", svg_solde_net(d)),
            ("qui-paie-age", svg_age(d)),
            ("qui-paie-mecanismes", svg_mecanismes())]
    for nom, (svg, _h) in figs:
        p = IMG / (nom + ".svg")
        p.write_text(svg, encoding="utf-8")
        cairosvg.svg2png(url=str(p), write_to=str(p.with_suffix(".png")), output_width=1440,
                         background_color="white")
    cartes = {"fr": [
        {"id": "detention", "fichier": "qui-paie-detention",
         "titre": "Qui emprunte ? Qui détient les titres de l'État ?",
         "montre": "Les administrations qui empruntent, puis les porteurs des titres de l'État : "
                   "deux champs distincts, sans lien de proportion.",
         "source": "INSEE, IR n° 79 (27/03/2026), %s  ·  Banque de France via l'AFT, "
                   "1er trimestre 2026" % r["periode_a"],
         "precaution": "A : valeur nominale ; B : valeur de marché. La détention ne mesure pas "
                       "la charge finale."},
        {"id": "redistribution", "fichier": "qui-paie-redistribution",
         "titre": "Prélèvements et transferts publics par dixième de niveau de vie, 2023",
         "montre": "Les prélèvements croissent fortement avec le niveau de vie ; les transferts "
                   "reçus, prestations et services publics, varient beaucoup moins.",
         "source": "Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, figure 1c)",
         "precaution": "Répartition avec conventions d'imputation ; ne mesure pas l'incidence "
                       "spécifique de la dette."},
        {"id": "solde-net", "fichier": "qui-paie-solde-net",
         "titre": "Contributeurs nets et bénéficiaires nets par dixième, 2023",
         "montre": "En moyenne par UC, les dixièmes modestes et médians reçoivent plus qu'ils ne versent, "
                   "les plus aisés l'inverse ; mais dès le milieu de l'échelle, la majorité des personnes versent plus qu'elles ne reçoivent.",
         "source": "Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, figure 2a)",
         "precaution": "Moyennes par UC ; pensions et services publics valorisés par imputation inclus ; "
                       "solde d'une année, non d'une vie ; ne mesure pas l'effet propre de la dette."},
        {"id": "age", "fichier": "qui-paie-age",
         "titre": "Prélèvements et transferts publics par âge du ménage, 2023",
         "montre": "En 2023, selon ces conventions : ce que verse et reçoit chaque groupe, classé par "
                   "âge moyen des adultes du ménage, retraites et services publics compris.",
         "source": "Insee, comptes nationaux distribués 2023 (Insee Analyses n° 118, figure 1e)",
         "precaution": "Photographie d'une année, non le bilan d'une génération ni des générations futures ; "
                       "l'âge du ménage n'est pas le statut de retraite de ses membres."},
        {"id": "mecanismes", "fichier": "qui-paie-mecanismes",
         "titre": "Par quels canaux la charge peut-elle être répartie ?",
         "montre": "Quatre mécanismes possibles, non exhaustifs, le refinancement qui reporte sans désigner de "
                   "perdant, et en regard ce que la dette a financé.",
         "source": "Synthèse de l'auteur, schéma non quantitatif",
         "precaution": "Aucun poids relatif ni effet causal n'est mesuré ici."},
    ]}
    (REPO / "data" / "figures_qui_paie.json").write_text(
        json.dumps(cartes, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    donnees = {
        "_licence": ("Compilation Stéphane Lalut, CC BY 4.0 (assemblage, grandeurs dérivées, mise "
                     "en cohérence). Données d'origine : INSEE (Licence Ouverte Etalab), "
                     "Banque de France via l'Agence France Trésor, sous leurs propres conditions."),
        "_genere_le": date.today().isoformat(),
        "affichage": aff,
        "detention": {
            "A_sous_secteurs": {"unite": "milliards d'euros, valeur nominale",
                                "periode": r["periode_a"], "total": r["total"],
                                "valeurs": [{"libelle": s["libelle"], "mdeur": s["mdeur"]}
                                            for s in r["ss"]]},
            "B_detenteurs_titres_etat": {"unite": "% des titres négociables de l'État, valeur de "
                                                  "marché", "periode": "1er trimestre 2026",
                                         "valeurs": [{"libelle": x["libelle"], "pct": x["pct"]}
                                                     for x in r["det"]]},
            "sources": r["sources"],
            "note": "Deux champs distincts : ne pas multiplier les parts de B par les montants de A.",
            "registre_sha256": r["sha256"],
        },
        # Denominateur de l'ordre de grandeur « par foyer » de la page du cout
        # (shortcode interets-par-foyer) : meme entree du registre que le livre.
        "echelle_foyer": r["foyers"],
        "redistribution": {
            "unite": "euros par unité de consommation (UC), 2023",
            "colonnes": ["D%d" % i for i in range(1, 11)] + ["Ensemble"],
            "prelevements": d["prel"], "prestations_especes": d["esp"],
            "transferts_non_monetaires": d["nat"],
            "transferts_nets": d["net"],
            "part_beneficiaires_nets_pct": d["part_benef"],
            "par_age": d["age"],
            "solde_finance_par_endettement_uc": d["solde_uc"],
            "solde_finance_par_endettement_mdeur": d["solde_md"],
            "convention": ("Insee : le supplément financé par endettement est imputé par "
                           "convention pour moitié à de moindres prélèvements, pour moitié à des "
                           "transferts supplémentaires."),
            "source": {"publication": "Insee Analyses n° 118, 16/04/2026, figures 1c, 1e, 2a et 2b",
                       "url": XLSX_URL, "sha256_fichier": d["sha256"]},
        },
    }
    corps = json.dumps(donnees, ensure_ascii=False, indent=1) + "\n"
    (REPO / "data" / "qui_paie_donnees.json").write_text(corps, encoding="utf-8")
    (REPO / "static" / "qui_paie_donnees.json").write_text(corps, encoding="utf-8")
    for nom, (_s, h) in figs:
        print("OK  %s.svg (720 x %d) + PNG 1440 px" % (nom, h))
    print("OK  data/figures_qui_paie.json, data/ et static/qui_paie_donnees.json")
    print("    registre %s…  ·  Insee %s…" % (r["sha256"][:12], d["sha256"][:12]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
