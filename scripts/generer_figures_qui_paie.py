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

# F6 — profil d'exposition. Tableau CND.101 : comptes distribués par VINGTIÈME de
# niveau de vie, avec une feuille par année de 2020 à 2023. Le classeur IA118
# ci-dessus ne porte que 2023 ; sans les quatre millésimes, la figure ne pourrait
# pas dire que son résultat est structurel plutôt que conjoncturel.
XLSX_CND = REPO / "scripts" / "sources" / "insee_T_CND_101_vingtiemes_2020_2023.xlsx"
XLSX_CND_SHA256 = "8e4d2ec005e9351f7105c796ac2e0ae8afc1f53b70b165d04f9387ed8cf838ef"
XLSX_CND_URL = "https://www.insee.fr/fr/statistiques/8574663"
CND_ANNEES = ("2020", "2021", "2022", "2023")
EFFORT_MDEUR = 10.0

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


def lire_cnd(d_ia118: dict) -> dict:
    """Profil d'exposition par dixième, sur les quatre millésimes de CND.101.

    Répartir un effort de 10 Md€ au prorata d'un poste puis le rapporter au revenu
    revient à afficher le PROFIL du poste dans le revenu, à une constante près par
    courbe. Aucun comportement, aucune élasticité, aucun effet en retour : c'est ce
    qui rend le résultat robuste, et c'est pourquoi la figure dit « profil
    d'exposition » et jamais « simulation ».

    Quatre gardes, toutes bloquantes, et toutes AVANT le résultat :
      G1  la structure du tableau est la même d'une année à l'autre ;
      G2  témoin croisé — le millésime 2023 de CND.101 est confronté au classeur
          IA118, qui est une AUTRE publication de la même source ;
      G3  le U — test écrit d'avance : le creux tombe dans D5-D9 et les deux
          extrémités valent au moins deux fois ce creux, les quatre années ;
      G4  la cellule atypique qui fait écarter le point D1 du scénario fiscal est
          TOUJOURS atypique. C'est la condition de mort de cet écartement : si
          l'Insee la corrige, la réserve n'a plus d'objet et la figure doit être
          refaite au lieu de continuer à retirer un point valide.
    """
    if not XLSX_CND.is_file():
        fail("tableau CND.101 absent : %s" % XLSX_CND)
    sha = hashlib.sha256(XLSX_CND.read_bytes()).hexdigest()
    if sha != XLSX_CND_SHA256:
        fail("empreinte du tableau CND.101 changée (%s) : relire la source, refaire les "
             "contrôles du § 4.3 de l'arbitrage, puis mettre à jour XLSX_CND_SHA256" % sha[:12])
    import openpyxl
    wb = openpyxl.load_workbook(XLSX_CND, data_only=True)

    postes = {"csg": "Contribution sociale", "ir": "Impôt sur le revenu",
              "autres": "Autres impôts sur les revenus", "pensions": "Pensions de retraite",
              "enseignement": "Enseignement", "rdn": "Revenu disponible net (RDN)"}

    def lire_an(an: str) -> tuple[dict, dict]:
        vals, rangs = {}, {}
        lignes = list(wb["CND_" + an].iter_rows(values_only=True))
        for cle, debut in postes.items():
            trouve = [(i, r) for i, r in enumerate(lignes, 1)
                      if r[0] and str(r[0]).strip().startswith(debut)]
            if not trouve:
                fail("CND_%s : ligne « %s » introuvable" % (an, debut))
            i, r = trouve[0]
            v = [abs(float(x)) if isinstance(x, (int, float)) else 0.0 for x in r[1:21]]
            if len(v) != 20:
                fail("CND_%s : « %s » sur %d vingtièmes au lieu de 20" % (an, debut, len(v)))
            vals[cle], rangs[cle] = v, i
        return vals, rangs

    brut = {an: lire_an(an) for an in CND_ANNEES}
    ref = brut["2023"][1]
    for an in CND_ANNEES:                                                    # G1
        if brut[an][1] != ref:
            fail("CND.101 : la structure de %s diffère de celle de 2023 (%s contre %s) — "
                 "les lignes ne peuvent plus être lues par leur libellé sans vérification"
                 % (an, brut[an][1], ref))

    # G2 — témoin croisé. IA118 porte une colonne « Ensemble » en tête, CND.101 non.
    ia = {}
    import openpyxl as _o
    wb118 = _o.load_workbook(XLSX, data_only=True)
    for cle, debut in postes.items():
        for r in wb118["Tableau complémentaire"].iter_rows(values_only=True):
            if r[0] and str(r[0]).strip().startswith(debut):
                ia[cle] = [abs(float(x)) if isinstance(x, (int, float)) else 0.0
                           for x in r[2:22]]
                break
        else:
            fail("IA118 : ligne « %s » introuvable pour le témoin croisé" % debut)
    ecart = max(max(abs(a - b) for a, b in zip(ia[c], brut["2023"][0][c])) for c in postes)
    if ecart > 0.15:
        fail("témoin croisé : CND.101 et IA118 divergent de %.2f Md€ sur 2023 alors qu'ils "
             "publient la même source — l'un des deux fichiers n'est pas celui qu'on croit"
             % ecart)

    def dix(v20: list) -> list:
        return [v20[2 * i] + v20[2 * i + 1] for i in range(10)]

    def profil(an: str, ecarter_d1_fiscal: bool) -> dict:
        v = brut[an][0]
        rdn = dix(v["rdn"])
        fisc = [v["csg"][i] + v["ir"][i] + v["autres"][i] for i in range(20)]
        out = {}
        for nom, poste in (("fiscal", fisc), ("pensions", v["pensions"]),
                           ("enseignement", v["enseignement"])):
            p = dix(poste)
            out[nom] = [100 * (EFFORT_MDEUR * p[i] / sum(p)) / rdn[i] for i in range(10)]
        out["_masse_d1_d5"] = {nom: 100 * sum(dix(poste)[:5]) / sum(dix(poste))
                               for nom, poste in (("fiscal", fisc), ("pensions", v["pensions"]),
                                                  ("enseignement", v["enseignement"]))}
        if ecarter_d1_fiscal:
            out["fiscal"][0] = None
        return out

    def ratios(p: dict) -> list:
        out = []
        for i in range(10):
            v = [p[n][i] for n in ("fiscal", "pensions", "enseignement") if p[n][i] is not None]
            out.append(max(v) / min(v))
        return out

    # G3 — le U, sur les données BRUTES : le test ne doit rien devoir au point écarté.
    stab = {}
    for an in CND_ANNEES:
        r = ratios(profil(an, False))
        creux = min(r[4:9])
        imin = r.index(min(r))
        if not 4 <= imin <= 8:
            fail("le creux de l'écart entre décisions tombe en D%d en %s, hors de D5-D9 : "
                 "la figure ne peut plus dire que le milieu est le moins sensible"
                 % (imin + 1, an))
        if not (r[0] >= 2 * creux and r[9] >= 2 * creux):
            fail("en %s, les extrémités ne valent plus le double du creux (D1 %.1f, D10 %.1f, "
                 "creux %.1f) : le U ne se lit plus" % (an, r[0], r[9], creux))
        stab[an] = {"ratios": [round(x, 2) for x in r], "creux_en": "D%d" % (imin + 1)}

    p23 = profil("2023", True)
    r23 = ratios(p23)
    # G4 — condition de mort de l'écartement du point D1 fiscal.
    ir = brut["2023"][0]["ir"]
    if not (ir[0] > 0.5 and ir[1] + ir[2] < 0.2):
        fail("l'impôt sur le revenu du premier vingtième n'est plus atypique (V1 %.1f, "
             "V2+V3 %.1f) : l'écartement du point D1 du scénario fiscal n'a plus de motif, "
             "la figure et son cartouche doivent être refaits" % (ir[0], ir[1] + ir[2]))
    if not (p23["enseignement"][0] > p23["pensions"][0]
            and p23["fiscal"][9] > p23["enseignement"][9]):
        fail("l'inversion que la figure démontre n'est plus dans les données : "
             "enseignement D1 %.2f, pensions D1 %.2f, fiscal D10 %.2f, enseignement D10 %.2f"
             % (p23["enseignement"][0], p23["pensions"][0],
                p23["fiscal"][9], p23["enseignement"][9]))
    # G5 — le creux ne doit rien au choix de la mesure. Le rapport max/min est une
    # mesure de dispersion parmi d'autres ; si le creux changeait de place avec le
    # coefficient de variation ou l'étendue rapportée à la moyenne, il serait un
    # artefact de la mesure et non un fait sur les données. Contrôle demandé par la
    # contre-expertise du 29/09, qui l'avait fait de son côté sur le millésime 2023.
    def dispersions(p: dict) -> dict:
        out = {"max_min": [], "coef_variation": [], "etendue_sur_moyenne": []}
        for i in range(10):
            v = [p[n][i] for n in ("fiscal", "pensions", "enseignement") if p[n][i] is not None]
            moy = sum(v) / len(v)
            var = sum((x - moy) ** 2 for x in v) / len(v)
            out["max_min"].append(max(v) / min(v))
            out["coef_variation"].append(var ** 0.5 / moy)
            out["etendue_sur_moyenne"].append((max(v) - min(v)) / moy)
        return out
    # Les QUATRE millésimes, et non le seul 2023 : la garde couvrait une année pendant
    # que le cartouche parlait de quatre, ce qu'un lecteur pouvait lire comme « trois
    # mesures sur quatre millésimes ». La preuve suit maintenant l'affirmation
    # (contre-expertise du 29/09, second tour).
    disp_an = {an: dispersions(profil(an, False)) for an in CND_ANNEES}
    disp23 = dispersions(profil("2023", True))
    # D1 ne compare que deux leviers dans la figure : il est hors comparaison de mesures.
    creux_par_mesure = {m: "D%d" % (2 + v[1:].index(min(v[1:]))) for m, v in disp23.items()}
    creux_an_mesure = {an: {m: "D%d" % (2 + v[1:].index(min(v[1:]))) for m, v in d.items()}
                       for an, d in disp_an.items()}
    hors_zone = {(an, m): dx for an, d in creux_an_mesure.items()
                 for m, dx in d.items() if dx not in ("D7", "D8")}
    # La ZONE, et non le dixième exact : D7 et D8 sont à égalité de fait (1,40 contre
    # 1,41 en rapport, 0,15 contre 0,14 en coefficient de variation), et le minimum
    # bascule de l'un à l'autre selon la mesure comme il bascule selon le millésime.
    # C'est bien ce que la figure affirme — un creux en D7-D8 —, donc ce que la garde
    # doit vérifier ; exiger le même dixième exact ferait échouer la chaîne sur un
    # écart sans portée.
    if hors_zone:
        fail("le creux de dispersion sort de D7-D8 pour %s : il dépendrait de la mesure ou du "
             "millésime, et la figure ne peut plus l'affirmer"
             % "; ".join("%s / %s -> %s" % (a, m, d) for (a, m), d in hors_zone.items()))

    creux_partout = sorted({v["creux_en"] for v in stab.values()})
    # Poids de la cellule atypique dans le poste fiscal du premier dixième, et son
    # amplitude sur les quatre millésimes : les deux chiffres du cartouche, calculés
    # ici plutôt qu'écrits à la main dans la figure.
    v23 = brut["2023"][0]
    fisc_d1 = (v23["csg"][0] + v23["ir"][0] + v23["autres"][0]
               + v23["csg"][1] + v23["ir"][1] + v23["autres"][1])
    ir_par_an = {an: brut[an][0]["ir"][0] for an in CND_ANNEES}
    return {"p": p23, "ratios": r23, "stabilite": stab, "creux_partout": creux_partout,
            "dispersions": disp23, "creux_par_mesure": creux_par_mesure,
            "creux_an_mesure": creux_an_mesure,
            "ir_v1": ir[0], "part_ir_v1": 100 * ir[0] / fisc_d1,
            "ir_v1_par_an": ir_par_an,
            "ir_v1_amplitude": max(ir_par_an.values()) / min(ir_par_an.values()),
            "masse_d1_d5": p23["_masse_d1_d5"],
            "temoin_croise_mdeur": round(ecart, 2), "sha256": sha}


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
    # « Résidents » et non « français » : la source classe par RÉSIDENCE du porteur, ce
    # que le sous-titre dit déjà. Garder « français » à côté de cette note faisait dire
    # à la figure le contraire de sa propre légende — une filiale résidente d'un groupe
    # étranger est ici résidente, un Français installé hors de France ne l'est pas.
    # Correction sur contre-expertise du 29/09 ; les libellés du registre du livre, eux,
    # ne bougent pas : le renommage est d'affichage.
    noms = {"Autres (français)": "Autres porteurs résidents *",
            "Établissements de crédit français": "Banques résidentes",
            "Assureurs français": "Assureurs résidents",
            "OPCVM français": "Fonds (OPCVM) résidents"}
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
    # « Renouvelle », et non « reporte » : un titre remboursé est remplacé par un titre
    # neuf, au taux du moment — l'échéance recule, la charge peut monter ou baisser.
    # « Reporte » suggérait une opération neutre qu'elle n'est pas (contre-expertise 29/09).
    c += boite(1, 44, 200, 70, [("Refinancement", TY_ANNOT, INK, True),
                                ("renouvelle l'échéance", TY_AXE, INK2, False),
                                ("aux taux du moment", TY_AXE, INK2, False)], tiret=True)
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
            "restructuration, cas extrême (porteurs des titres). Le refinancement renouvelle "
            "l'échéance aux taux du moment et ne permet pas, à lui seul, d'identifier qui "
            "supportera la charge. En regard figure ce que la dette a financé.")
    e = entete(h, "qp-mec", "Par quels canaux la charge de la dette peut-elle être répartie ?",
               desc) + c
    e += cartouche(y, [
        ("Synthèse de l'auteur · schéma non quantitatif, flèches d'égale épaisseur", INK2),
        ("Schéma de mécanismes possibles. Aucun poids relatif ni effet causal n'est mesuré ici.",
         INK2),
        ("Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)])
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ F6
def svg_exposition(c: dict) -> tuple[str, int]:
    """Un même effort, trois décisions — et de combien le choix change l'effort.

    DEUX panneaux, deux grandeurs : A en % du revenu du groupe, B en rapport entre
    la décision la plus lourde et la plus légère. Le panneau A montre l'inversion,
    déjà lisible dans la fiche ; le panneau B porte le résultat que rien d'autre ne
    dit — les extrémités de l'échelle dépendent du levier choisi, la moitié médiane
    non.

    Couleurs : celles des autres figures du volet, pour la même grandeur. Les
    prélèvements restent orange, les prestations en espèces (donc les pensions)
    bleues, les services publics valorisés (donc l'enseignement) gris — c'est la
    série qui porte la convention d'imputation, ici comme dans la figure 1c.
    """
    p, rat = c["p"], c["ratios"]
    # Les trois décisions se nomment en toutes lettres SOUS le titre du panneau, et
    # l'étiquette directe ne porte à côté de la courbe que le nom court et sa valeur
    # terminale : la marge droite fait 162 px, une précision plus longue y serait
    # coupée — et une étiquette tronquée ment sur la série qu'elle désigne.
    noms = {"fiscal": ("Impôts", C2),
            "pensions": ("Pensions", C1),
            "enseignement": ("Enseignement", SEC)}
    # Phrase du panneau B, vérifiée avant d'être écrite. Elle disait « ne change presque
    # rien » : à ×1,4, l'écart entre le levier le plus lourd et le plus léger reste de
    # 40 % — la formulation promettait une indifférence que les chiffres ne portent pas
    # (contre-expertise du 29/09, acceptée). Ce que la figure établit est un CREUX DE
    # DISPERSION, et c'est cela que la garde vérifie : il tombe en D7 ou D8.
    creux_dixieme = "D%d" % (rat.index(min(rat)) + 1)
    if creux_dixieme not in ("D7", "D8"):
        fail("le panneau B nomme D7-D8 comme creux de dispersion : le minimum est en %s"
             % creux_dixieme)

    ml, mr = 46, 176
    pas = (W - ml - mr) / 10

    def X(i):
        return ml + pas * (i + 0.5)

    topA, basA, vmaxA = 104, 300, 3.0
    kA = (basA - topA) / vmaxA

    def YA(v):
        return basA - v * kA

    c_ = [txt(0, 22, "Un même effort de 10" + NBSP + "milliards d'euros : qui le supporterait, "
              "selon la décision prise ?", TY_TITRE, INK2),
          txt(0, 48, "A · Montant imputé au groupe, en % de son revenu disponible net",
              TY_ANNOT, INK, weight="600"),
          txt(0, 64, "Effort réparti au prorata des montants existants de chaque poste "
              "· dixièmes de niveau de vie, 2023", TY_AXE, MUTED),
          txt(0, 78, "Décisions comparées : impôts sur les revenus et le patrimoine "
              "· pensions de retraite · dépenses d'enseignement", TY_AXE, MUTED)]
    for g in (0, 1, 2, 3):
        yy = YA(g)
        c_.append('<line x1="%d" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                  % (ml, yy, W - mr, yy, AXIS if g == 0 else GRID))
        c_.append(txt(ml - 6, yy + 4, fr(g) + NBSP + "%", TY_AXE, MUTED, "end"))
    for cle in ("enseignement", "pensions", "fiscal"):
        col = noms[cle][1]
        pts = [(X(i), YA(v)) for i, v in enumerate(p[cle]) if v is not None]
        c_.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2" '
                  'stroke-linejoin="round" stroke-linecap="round"/>'
                  % (" ".join("%.1f,%.1f" % q for q in pts), col))
        for x, y in pts:
            c_.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s"/>' % (x, y, col))
    # Le point écarté se VOIT : marque creuse, sans valeur, motif au cartouche. Le
    # taire laisserait croire à un trou dans la donnée ; l'afficher plein ferait
    # porter une affirmation à un chiffre que quatre millésimes démentent.
    c_.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="none" stroke="%s" stroke-width="1.6" '
              'stroke-dasharray="2 2"/>' % (X(0), YA(0.31), C2))
    c_.append(txt(X(0) + 9, YA(0.31) + 4, "point écarté", TY_AXE - 1, MUTED))
    c_.append(txt(X(0), YA(p["enseignement"][0]) - 10, fr(p["enseignement"][0], 2) + NBSP + "%",
                  TY_VALEUR, INK, "middle", weight="600"))
    c_ += etiquettes_directes(W - mr + 14, [
        (YA(p[cle][9]) + 4, noms[cle][1], noms[cle][0],
         "%s%s%% en D10" % (fr(p[cle][9], 2), NBSP))
        for cle in ("fiscal", "pensions", "enseignement")], topA + 8, basA - 12)
    for i in range(10):
        c_.append(txt(X(i), basA + 16, "D%d" % (i + 1), TY_AXE, MUTED, "middle"))
    c_.append(txt(ml, basA + 32, "← 10" + NBSP + "% les plus modestes", TY_AXE - 1, MUTED))
    c_.append(txt(W - mr, basA + 32, "10" + NBSP + "% les plus aisés →", TY_AXE - 1, MUTED, "end"))

    topB, basB, vmaxB = 404, 504, 8.0
    kB = (basB - topB) / (vmaxB - 1)

    def YB(v):
        return basB - (v - 1) * kB

    c_.append(txt(0, 364, "B · De combien le choix de la décision change l'effort d'un même "
                  "groupe", TY_ANNOT, INK, weight="600"))
    c_.append(txt(0, 380, "Rapport entre la décision la plus lourde et la plus légère pour ce "
                  "groupe · base 1 : aucun écart", TY_AXE, MUTED))
    # Bande d'événement : la zone que la figure démontre, libellée SOUS elle.
    c_.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#f0efe9"/>'
              % (X(4) - pas / 2, topB - 6, pas * 5, basB - topB + 6))
    for g in (1, 2, 4, 6, 8):
        yy = YB(g)
        c_.append('<line x1="%d" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                  % (ml, yy, W - mr, yy, AXIS if g == 1 else GRID))
        c_.append(txt(ml - 6, yy + 4, "×" + fr(g), TY_AXE, MUTED, "end"))
    creux = min(rat)
    for i, v in enumerate(rat):
        h_ = max((v - 1) * kB, 2.0)
        fort = v == creux
        # Une seule teinte pour toutes les barres : la charte compte deux couleurs de
        # données, et une barre d'encre en ferait une troisième. Le creux se marque par
        # la typographie et par la bande de fond, pas par une couleur de plus.
        c_.append('<rect x="%.1f" y="%.1f" width="34" height="%.1f" rx="2" fill="%s"/>'
                  % (X(i) - 17, basB - h_, h_, SEC))
        # D1 ne compare que deux leviers, le troisième étant écarté : ce qu'on lit là
        # est une BORNE INFÉRIEURE, puisqu'un troisième point ne pourrait qu'élever le
        # maximum ou abaisser le minimum. L'écrire « ≥ » est plus exact, et plus fort :
        # l'affirmation tient quelle que soit la valeur du point manquant.
        borne = i == 0 and any(p[k][0] is None for k in p if not k.startswith("_"))
        c_.append(txt(X(i), basB - h_ - 7, ("≥ ×" if borne else "×") + fr(v, 1),
                      TY_ANNOT if fort else TY_AXE - 1, INK if fort else INK2, "middle",
                      weight="600" if fort else None))
        c_.append(txt(X(i), basB + 16, "D%d" % (i + 1), TY_AXE,
                      INK if fort else MUTED, "middle", weight="600" if fort else None))
    c_.append(txt(X(6), basB + 34, "D7-D8 : dispersion minimale entre les trois leviers",
                  TY_AXE, INK2, "middle"))
    c_.append(txt(X(6), basB + 48, "le levier choisi y différencie le moins les ménages",
                  TY_AXE, INK2, "middle"))
    y = basB + 62
    lignes = [
        ("Insee, comptes nationaux distribués, tableau CND.101 (millésime 2023, base 2020) "
         "· France, dixièmes de niveau de vie usuel", INK2),
        ("Profil d'exposition, non une simulation : ni comportement, ni effet en retour. Une "
         "baisse de service valorisé n'est pas une perte de revenu monétaire.", INK2),
        ("Point D1 des impôts écarté : l'impôt sur le revenu du premier vingtième y pèse "
         "%s%s%% du poste quand les vingtièmes voisins sont à zéro, et varie de 1 à %s "
         "selon le millésime." % (fr(c["part_ir_v1"]), NBSP, fr(c["ir_v1_amplitude"], 1)), INK2),
        ("D1 porte « ≥ » : l'écart y est calculé sur les deux leviers conservés — c'est une borne "
         "inférieure, un troisième point ne pourrait que l'élever.", INK2),
        ("Le creux se situe en %s sur les quatre millésimes 2020-2023, et dans la même zone avec "
         "trois mesures de dispersion." % " ou ".join(c["creux_partout"]), INK2),
        ("Compilation Stéphane Lalut, CC BY 4.0 · " + URL_PAGE, MUTED)]
    h = int(y + 13 + 12 * len(lignes) + 8)
    desc = ("Deux panneaux. A : pour un effort de 10 milliards d'euros réparti au prorata de "
            "chaque poste, la part du revenu disponible net que représenterait ce montant pour "
            "chaque dixième de niveau de vie, en 2023. Une baisse des dépenses d'enseignement "
            "pèse %s %% du revenu du premier dixième et %s %% du dernier ; une hausse des impôts "
            "sur les revenus et le patrimoine, %s %% du dernier ; les pensions restent entre "
            "%s et %s %%. B : le rapport entre la décision la plus lourde et la plus légère pour "
            "un même groupe, en base 1. Il vaut %s au dernier dixième et au moins autant au "
            "premier, et descend à %s en D7-D8 : c'est là que le levier retenu différencie le "
            "moins les ménages." % (
                fr(p["enseignement"][0], 2), fr(p["enseignement"][9], 2), fr(p["fiscal"][9], 2),
                fr(min(p["pensions"]), 2), fr(max(p["pensions"]), 2),
                "×" + fr(max(rat[0], rat[9]), 1), "×" + fr(creux, 1)))
    e = entete(h, "qp-exp", "Un même effort de 10 milliards d'euros : qui le supporterait "
               "selon la décision prise ?", desc) + c_
    e += cartouche(y, lignes)
    e.append("</svg>")
    return "\n".join(e) + "\n", h


# ------------------------------------------------------------------ texte
def affichage(r: dict, d: dict, c: dict) -> dict:
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
    # Section « Selon la décision prise… » : ses trois affirmations, contrôlées ici.
    p, rat = c["p"], c["ratios"]
    pens = p["pensions"]
    if not max(pens) / min(pens) < 2:
        fail("la page dit que le poids d'une baisse des pensions reste dans une bande étroite : "
             "il va de %.2f à %.2f %%" % (min(pens), max(pens)))
    if not c["masse_d1_d5"]["enseignement"] > 2 * c["masse_d1_d5"]["fiscal"]:
        fail("la page oppose la part de l'effort qui reviendrait à la moitié la moins aisée selon "
             "la décision : enseignement %.1f %%, impôts %.1f %%"
             % (c["masse_d1_d5"]["enseignement"], c["masse_d1_d5"]["fiscal"]))
    creux = min(rat)
    icreux = rat.index(creux)
    if not (rat[0] > 2 * creux and rat[9] > 2 * creux):
        fail("la page dit que le choix de la décision pèse aux deux extrémités et non au milieu")
    if c["creux_par_mesure"]["max_min"] != "D%d" % (icreux + 1):
        fail("la page nomme %s comme creux ; le rapport max/min le place en %s"
             % ("D%d" % (icreux + 1), c["creux_par_mesure"]["max_min"]))
    exp = {
        "exp_effort": "10",
        "exp_ens_d1": fr(p["enseignement"][0], 2), "exp_ens_d10": fr(p["enseignement"][9], 2),
        "exp_fisc_d10": fr(p["fiscal"][9], 2),
        "exp_pens_min": fr(min(pens), 2), "exp_pens_max": fr(max(pens), 2),
        "exp_ecart_d1": fr(rat[0], 1), "exp_ecart_d10": fr(rat[9], 1),
        "exp_ecart_creux": fr(creux, 1), "exp_creux_dixieme": "D%d" % (icreux + 1),
        "exp_creux_zone": "D7-D8",
        "exp_cv_creux": fr(min(c["dispersions"]["coef_variation"][1:]), 2),
        "exp_cv_d10": fr(c["dispersions"]["coef_variation"][9], 2),
        "exp_creux_millesimes": " ou ".join(c["creux_partout"]),
        "exp_masse_ens": fr(c["masse_d1_d5"]["enseignement"], 1),
        "exp_masse_fisc": fr(c["masse_d1_d5"]["fiscal"], 1),
        "exp_millesimes": "2020-2023",
        "exp_part_ir_v1": fr(c["part_ir_v1"]),
    }
    return dict(exp, **{
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
    })


def main() -> int:
    try:
        import cairosvg
    except ImportError:
        fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout")
    r, d = lire_registre(), lire_insee()
    c = lire_cnd(d)
    aff = affichage(r, d, c)
    figs = [("qui-paie-detention", svg_detention(r)),
            ("qui-paie-redistribution", svg_redistribution(d)),
            ("qui-paie-solde-net", svg_solde_net(d)),
            ("qui-paie-age", svg_age(d)),
            ("qui-paie-mecanismes", svg_mecanismes()),
            ("qui-paie-exposition", svg_exposition(c))]
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
        {"id": "exposition", "fichier": "qui-paie-exposition",
         "titre": "Un même effort de 10 milliards d'euros : qui le supporterait selon la "
                  "décision prise ?",
         "montre": "Ce qu'un même effort représenterait pour chaque dixième de niveau de vie "
                   "selon la décision retenue — impôts, pensions ou enseignement —, puis de "
                   "combien ce choix change l'effort d'un même groupe.",
         "source": "Insee, comptes nationaux distribués, tableau CND.101 (vingtièmes de niveau "
                   "de vie, 2020-2023, base 2020) — millésime 2023",
         "precaution": "Profil d'exposition comptable, non une simulation : ni comportement ni "
                       "effet en retour. Une baisse de service valorisé n'est pas une perte de "
                       "revenu monétaire. Le point D1 de la décision fiscale est écarté, son "
                       "motif figure au cartouche."},
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
            # Convention de signe explicitée le 29/09 sur contre-expertise : les valeurs
            # reprennent celles de l'Insee, où le solde est POSITIF quand le groupe verse
            # plus qu'il ne reçoit. Un tiers qui reprend ce jeu sans le savoir inverserait
            # la lecture de la figure, et rien ne le lui signalerait.
            "transferts_nets_convention_signe": (
                "Convention Insee : valeur POSITIVE = le groupe verse plus qu'il ne reçoit "
                "(contributeur net) ; valeur NÉGATIVE = il reçoit plus qu'il ne verse "
                "(bénéficiaire net). D1 vaut -20800 et D10 +58400 en 2023."),
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
        "exposition": {
            "unite": "% du revenu disponible net du dixième",
            "effort_mdeur": EFFORT_MDEUR,
            "colonnes": ["D%d" % i for i in range(1, 11)],
            "millesime": "2023",
            "decisions": {
                "fiscal": "hausse des impôts courants sur les revenus et le patrimoine "
                          "(CSG, impôt sur le revenu, autres), au prorata des montants existants. "
                          "ATTENTION : dans la nomenclature des comptes distribués, le poste "
                          "« impôt sur le revenu » est pris HORS CRÉDIT D'IMPÔT (CND.4.2), les "
                          "crédits d'impôt étant classés ailleurs, en subventions sur les produits "
                          "(CND.11.2.3 pour les services à la personne). Ce scénario porte donc "
                          "sur un impôt BRUT de crédits, ce qui pèse surtout en bas de "
                          "distribution — une raison de plus d'écarter le point D1.",
                "pensions": "baisse des pensions de retraite, au prorata",
                "enseignement": "baisse des dépenses d'enseignement attribuées aux ménages, "
                                "au prorata",
            },
            "taux": {k: [None if v is None else round(v, 3) for v in c["p"][k]]
                     for k in ("fiscal", "pensions", "enseignement")},
            "ecart_entre_decisions": [round(v, 2) for v in c["ratios"]],
            "ecart_entre_decisions_note": (
                "Rapport entre la décision la plus lourde et la plus légère pour le groupe. "
                "En D1, calculé sur deux décisions seulement (point fiscal écarté) : c'est une "
                "BORNE INFÉRIEURE, un troisième point ne pourrait qu'élever le maximum ou "
                "abaisser le minimum."),
            "autres_mesures_de_dispersion": {
                m: [round(v, 3) for v in s] for m, s in c["dispersions"].items()},
            "creux_par_mesure": c["creux_par_mesure"],
            "creux_par_millesime_et_mesure": c["creux_an_mesure"],
            "note_sur_les_mesures": (
                "Trois mesures DISTINCTES de dispersion appliquées aux mêmes trois "
                "observations : elles se corroborent, elles ne constituent pas trois "
                "observations indépendantes. Leur minimum tombe en D7 ou en D8 selon la "
                "mesure et selon le millésime — c'est une zone, pas un dixième."),
            "part_de_l_effort_recue_par_d1_d5_pct": {k: round(v, 1)
                                                     for k, v in c["masse_d1_d5"].items()},
            "stabilite_2020_2023": c["stabilite"],
            "point_ecarte": {
                "ou": "D1, décision fiscale",
                "motif": ("l'impôt sur le revenu du premier vingtième pèse %.0f %% du poste "
                          "fiscal de ce dixième alors que les vingtièmes voisins sont à zéro, "
                          "et varie de 1 à %.1f sur 2020-2023"
                          % (c["part_ir_v1"], c["ir_v1_amplitude"])),
                "valeurs_ir_v1_mdeur": c["ir_v1_par_an"],
            },
            "nature": ("Profil d'exposition comptable, non une simulation : l'effort est réparti "
                       "au prorata des montants existants, sans comportement ni effet en retour. "
                       "Une baisse de service valorisé n'est pas une perte de revenu monétaire."),
            "temoin_croise_avec_IA118_mdeur": c["temoin_croise_mdeur"],
            "source": {"publication": "Insee, comptes nationaux distribués, tableau CND.101 "
                                      "(vingtièmes de niveau de vie, 2020-2023, base 2020)",
                       "url": XLSX_CND_URL, "sha256_fichier": c["sha256"]},
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
