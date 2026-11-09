#!/usr/bin/env python3
"""matrice_dette_futurs.py -- matrice institutionnelle du volet « Quels futurs ? » : de la source au jeu publié.

Appelé par update_dette_futurs.py (jamais seul). Source écrite à la main, sans montant saisi :
scripts/sources_futurs/matrice_institutionnelle.yaml. Arbitrages : PRO-20261109-095636 (forme publique, option C :
fiches courtes + tableau complet téléchargeable) et PRO-20261109-104650 (libellés conditionnels).

Catégories des valeurs (règle « une phrase de méthode dit ce que le script fait ») :
  - CALCULÉES par le moteur de la page (jetons solde_*, invest_*, taux20_*, croiss_*) ;
  - CALCULÉES sur une pièce archivée : la part des lignes soumises en principe aux clauses d'action collective, recalculée
    sur sources_futurs/aft_lignes_2026-11-09.csv (76 fiches de ligne de l'AFT et 35 BTF, lues par navigateur le
    09/11/2026, le serveur refusant les scripts ; empreinte dans SHA256SUMS) ;
  - LUES dans les jeux du site déjà publiés : data/annulation_bdf.json (détention de la Banque de France) et
    data/dette_generations.json (part des non-résidents) ;
  - TRANSCRITES d'une source lue, vérifiées contre la pièce archivée hors dépôt (empreinte inscrite dans le bloc
    « valeurs » de la source) : jetons {v.*}.

GARDES (arrêt sinon) : structure complète FR et EN ; statuts, issues et robustesse dans leurs listes fermées ; aucun
montant écrit en clair dans un texte ; aucun jeton inconnu ni laissé non résolu ; sens des effets conforme aux verbes de la
prose (« abaisse », « relève ») ; somme des lignes AFT = total ; classement par la loi (date de création) et mention de la
fiche concordants hors des écarts déclarés (ECARTS_DECLARES) ; total de l'encours pris en compte au milliard près.
"""
from __future__ import annotations

import csv
import io
import json
import re
from pathlib import Path

import yaml

import langue_generee as lg

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "scripts" / "sources_futurs" / "matrice_institutionnelle.yaml"
AFT_PIECE = "aft_lignes_2026-11-09.csv"
AFT_DATE = {"fr": "9 novembre 2026", "en": "9 November 2026"}
CHAMPS = ("ce_qui_change", "effet", "qui_decide", "droit", "repartition", "robustesse", "issue")
FICHE = ("ce_qui_change", "effet", "qui_decide", "issue")          # fiche courte (option C)
# Champ facultatif du repli (arbitrage Dette-13, 09/11/2026) : les estimations et études publiées, chiffres, méthodes et
# auteurs ; le premier niveau (« effet ») garde le fait du désaccord et sa nature, jamais une estimation privilégiée.
OPTIONNELS = ("detail",)
# Familles d'opérations (arbitrages Dette-12 et Dette-13) : titres H3 de la matrice, dans cet ordre ; chaque opération en
# déclare une, et l'ordre des opérations les garde contiguës.
FAMILLES = {
    "budget": {"fr": "Le budget", "en": "The budget"},
    "europe": {"fr": "Les règles et le financement européens", "en": "European rules and financing"},
    "engagements": {"fr": "Les engagements existants et la monnaie", "en": "Existing commitments and the currency"},
}
ORDRE = ["solde", "impot_patrimoines", "allongement", "regle_or", "emprunt_commun", "mutualisation", "eurosysteme",
         "restructuration", "sortie_euro"]
STATUTS = {"lu", "calc", "site", "infere", "non_etabli"}
ISSUES = {"reduite", "deplacee", "aggravee", "conditionnelle", "non_determinee"}
ROBUSTESSES = {"calculee", "mecanisme_documente", "non_determinee"}
LIBELLES = {
    "fr": {"ce_qui_change": "Ce qui change", "effet": "Effet", "qui_decide": "Qui décide", "droit": "Droit applicable",
           "repartition": "Qui gagne, qui paie", "robustesse": "Robustesse", "issue": "Issue provisoire",
           "detail": "Les estimations publiées",
           "lu": "texte lu", "calc": "calcul", "site": "établi sur le site", "infere": "déduit", "non_etabli": "non établi",
           "reduite": "contrainte réduite", "deplacee": "contrainte déplacée", "aggravee": "contrainte aggravée",
           "conditionnelle": "selon les conditions", "non_determinee": "non déterminée",
           "calculee": "calculée", "mecanisme_documente": "mécanisme documenté"},
    "en": {"ce_qui_change": "What changes", "effet": "Effect", "qui_decide": "Who decides", "droit": "Applicable law",
           "repartition": "Who gains, who pays", "robustesse": "Robustness", "issue": "Provisional outcome",
           "detail": "Published estimates",
           "lu": "text read", "calc": "calculation", "site": "established on this site", "infere": "inferred",
           "non_etabli": "not established", "reduite": "constraint reduced", "deplacee": "constraint shifted",
           "aggravee": "constraint aggravated", "conditionnelle": "depends on conditions", "non_determinee": "not determined",
           "calculee": "calculated", "mecanisme_documente": "documented mechanism"},
}
# Lignes dont la fiche AFT ne porte pas la mention des clauses alors que la loi les y soumet (créées après le 01/01/2013) :
# écart déclaré, arbitrage PRO-20261109-104650 (arrêtés de création à lire). Toute autre divergence arrête.
ECARTS_DECLARES = {"FR0014001N38", "FR001400JI88", "FR0013327491"}
# Montant écrit en clair dans un texte : interdit (jetons seulement).
MONTANT = re.compile(r"\d+(?:[,.]\d+)?\s*(?:%|Md€|M€|milliards?|millions?|points?\b|pts?\b|centimes|pb\b)|€\s*\d")
JETON = re.compile(r"\{([a-z0-9_.]+)\}")


class Garde(Exception):
    pass


def fail(msg: str) -> None:
    raise Garde("matrice : " + msg)


# ------------------------------------------------------------------ AFT : part des lignes soumises aux clauses
def aft(piece, ecarts: set | None = None) -> dict:
    lignes = list(csv.DictReader(io.StringIO(piece(AFT_PIECE).read_text(encoding="utf-8-sig")), delimiter=";"))
    if len({l["isin"] for l in lignes}) != len(lignes):
        fail("AFT : ISIN en double")
    oat = [l for l in lignes if l["type"] in ("oat", "oati", "oatei")]
    btf = [l for l in lignes if l["type"] == "btf"]
    if len(oat) < 60 or len(btf) < 10:
        fail("AFT : releve incomplet (%d lignes longues, %d BTF)" % (len(oat), len(btf)))
    avec, sans, fins, divergences = 0, 0, [], set()
    for l in oat:
        v = int(l["encours_nominal_eur"])
        an = re.search(r"(\d{4})$", l["arrete_de_creation"].strip())
        if an:
            loi = int(an.group(1)) >= 2013          # L. 213-22-1 II, D. 213-25-1 I : titres créés depuis le 01/01/2013
        elif l["mention_cac_fiche"] == "oui":
            loi = True                              # arrêté absent de la fiche : la mention fait foi (lignes récentes)
        else:
            fail("AFT : %s sans arrete ni mention : classement impossible" % l["isin"])
        if loi != (l["mention_cac_fiche"] == "oui"):
            divergences.add(l["isin"])
        if loi:
            avec += v
        else:
            sans += v
            fins.append(int(re.search(r"(20\d\d)\s*$", l["libelle"]).group(1)))
    ecarts = ECARTS_DECLARES if ecarts is None else ecarts
    if divergences != ecarts:
        fail("AFT : divergences loi / fiche %s, declarees %s" % (sorted(divergences), sorted(ecarts)))
    tot = avec + sans
    if not 0.5 < avec / tot < 1:
        fail("AFT : part couverte %.3f hors de la plage que la prose suppose" % (avec / tot))
    btf_md = sum(int(l["encours_nominal_eur"]) for l in btf) / 1e9
    return {"cac_md": avec / 1e9, "sans_cac_md": sans / 1e9, "oat_md": tot / 1e9, "cac_part": 100 * avec / tot,
            "sans_cac_n": len(fins), "sans_cac_fin": max(fins), "btf_md": btf_md,
            "ecarts_declares_md": sum(int(l["encours_nominal_eur"]) for l in oat if l["isin"] in ECARTS_DECLARES) / 1e9}


# ------------------------------------------------------------------ jetons
def jetons(R: dict, A: dict, src: dict, lang: str) -> dict:
    s = R["sens"]
    # Sens des effets : la prose dit « abaisse » ou « relève » ; la donnée doit le soutenir.
    for cle, signe in (("solde_plus_1_comptable", -1), ("investissement_emprunte_1pt_comptable", 1),
                       ("taux_moins_20pb", -1), ("croissance_plus_05", -1), ("croissance_moins_05", 1)):
        if s[cle]["dette_2035"] * signe <= 0:
            fail("sens de %s en 2035 contraire a la prose (%.2f)" % (cle, s[cle]["dette_2035"]))
    pts = lambda v: lg.points(abs(v), 1, lang)
    J = {"solde_2035_pts": pts(s["solde_plus_1_comptable"]["dette_2035"]),
         "invest_2035_pts": pts(s["investissement_emprunte_1pt_comptable"]["dette_2035"]),
         "taux20_2035_pts": pts(s["taux_moins_20pb"]["dette_2035"]),
         "croiss_plus_2035_pts": pts(s["croissance_plus_05"]["dette_2035"]),
         "croiss_moins_2035_pts": pts(s["croissance_moins_05"]["dette_2035"]),
         "cac_part": lg.nombre(A["cac_part"], 1, lang), "cac_md": lg.nombre(A["cac_md"], 0, lang),
         "oat_md": lg.nombre(A["oat_md"], 0, lang), "sans_cac_md": lg.nombre(A["sans_cac_md"], 0, lang),
         "sans_cac_n": lg.nombre(A["sans_cac_n"], 0, lang), "sans_cac_fin": str(A["sans_cac_fin"]),
         "btf_md": lg.nombre(A["btf_md"], 0, lang), "aft_date": AFT_DATE[lang]}
    bdf = json.loads((ROOT / "data" / "annulation_bdf.json").read_text(encoding="utf-8"))
    aff = bdf["affichage" if lang == "fr" else "affichage_en"]
    J["bdf_md"], J["bdf_date"] = aff["e0"], aff["date_e0"]
    gen = json.loads((ROOT / "data" / "dette_generations.json").read_text(encoding="utf-8"))["etat_negociable"]["releve"]
    m = re.fullmatch(r"(\d{4})-Q([1-4])", gen["periode"])
    if not m:
        fail("periode des non-residents illisible : %r" % gen["periode"])
    an, q = m.group(1), int(m.group(2))
    J["nonres_pct"] = lg.nombre(gen["valeur"], 1, lang)
    J["nonres_periode"] = ("au %s trimestre %s" % ("1er" if q == 1 else "%de" % q, an) if lang == "fr"
                           else "in the %s quarter of %s" % (("first", "second", "third", "fourth")[q - 1], an))
    for k, v in src["valeurs"].items():
        if not v.get("piece_sha256"):
            fail("valeur transcrite %s sans empreinte de piece" % k)
        d = v.get("decimales", 1)
        J["v." + k] = lg.nombre(v["valeur"], d, lang)
        if v["unite"] == "point":
            J["v." + k + "_pts"] = lg.points(v["valeur"], d, lang)
    return J


def resoudre(txt: str, J: dict, ou: str) -> str:
    brut = JETON.sub("", txt)
    if MONTANT.search(brut):
        fail("montant ecrit en clair dans %s : %r" % (ou, MONTANT.search(brut).group(0)))
    inconnus = [k for k in JETON.findall(txt) if k not in J]
    if inconnus:
        fail("jetons inconnus dans %s : %s" % (ou, inconnus))
    out = JETON.sub(lambda m: J[m.group(1)], " ".join(txt.split()))
    if "{" in out or "}" in out:
        fail("jeton non resolu dans %s" % ou)
    return out


# ------------------------------------------------------------------ construction
def construire(R: dict, piece, mut: dict | None = None) -> dict:
    """mut (témoin seulement) : {"ajout": texte ajouté à solde.effet.fr} ou {"ecarts": ensemble déclaré}."""
    mut = mut or {}
    src = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    if "ajout" in mut:
        src["operations"][0]["effet"]["fr"] += mut["ajout"]
    ops = src.get("operations") or []
    if [o["cle"] for o in ops] != ORDRE:
        fail("liste ou ordre des operations modifie : %s" % [o.get("cle") for o in ops])
    fam = [o.get("famille") for o in ops]
    if any(f not in FAMILLES for f in fam):
        fail("famille absente ou inconnue : %s" % fam)
    vues = [f for i, f in enumerate(fam) if i == 0 or f != fam[i - 1]]
    if vues != list(FAMILLES):
        fail("familles non contigues ou hors de leur ordre : %s" % vues)
    A = aft(piece, mut.get("ecarts"))
    out = {"aft": {k: (round(v, 3) if isinstance(v, float) else v) for k, v in A.items()},
           "valeurs_transcrites": src["valeurs"], "fr": {}, "en": {}}
    lignes_csv = []
    for lang in ("fr", "en"):
        J = jetons(R, A, src, lang)
        L = LIBELLES[lang]
        liste = []
        for o in ops:
            # Sources par langue (relecture du 09/11/2026 : la page anglaise affichait « moteur de la page », « TFUE »…) ;
            # sources_en obligatoire et de même longueur, pour qu'aucune source ne manque d'une langue à l'autre.
            srcs = o["sources"] if lang == "fr" else o.get("sources_en")
            if not srcs or len(srcs) != len(o["sources"]):
                fail("%s : sources_en absente ou de longueur differente de sources" % o["cle"])
            e = {"cle": o["cle"], "titre": o["titre"][lang], "famille": o["famille"], "sources": srcs, "champs": {}}
            for c in CHAMPS + tuple(k for k in OPTIONNELS if k in o):
                ch = o.get(c)
                if not isinstance(ch, dict) or not ch.get("fr") or not ch.get("en"):
                    fail("%s.%s absent ou incomplet" % (o["cle"], c))
                statut = ch.get("statut", "infere" if c == "issue" else None)
                if c != "issue" and statut not in STATUTS:
                    fail("%s.%s : statut %r" % (o["cle"], c, statut))
                code = ch.get("code")
                if c == "issue" and code not in ISSUES:
                    fail("%s.issue : code %r" % (o["cle"], code))
                if c == "robustesse" and code not in ROBUSTESSES:
                    fail("%s.robustesse : code %r" % (o["cle"], code))
                # Un texte peut être une liste (variantes d'un instrument) : premier élément = phrase d'entrée, les
                # suivants = éléments de la liste ; le CSV reçoit la phrase entière.
                brut = ch[lang]
                if isinstance(brut, list):
                    if len(brut) < 3 or not all(isinstance(x, str) for x in brut):
                        fail("%s.%s.%s : liste trop courte ou non textuelle" % (o["cle"], c, lang))
                    morceaux = [resoudre(x, J, "%s.%s.%s" % (o["cle"], c, lang)) for x in brut]
                    items, texte = morceaux[1:], morceaux[0] + " " + " ".join(morceaux[1:])
                else:
                    items, texte = None, resoudre(brut, J, "%s.%s.%s" % (o["cle"], c, lang))
                e["champs"][c] = {"libelle": L[c], "texte": texte, "fiche": c in FICHE, "intro": morceaux[0] if items else None,
                                  "items": items,
                                  "statut": statut if c != "issue" else None,
                                  "statut_libelle": L[statut] if c != "issue" else None,
                                  "code": code, "code_libelle": L[code] if code else None}
                lignes_csv.append([o["cle"], o["titre"][lang], c, L[c], lang, statut or "", code or "", texte,
                                   " ; ".join(srcs), FAMILLES[o["famille"]][lang]])
            liste.append(e)
        out[lang] = {"operations": liste, "familles": {k: v[lang] for k, v in FAMILLES.items()},
                     "transversale": {"titre": src["transversale"]["titre"][lang],
                                      "texte": resoudre(src["transversale"][lang], J, "transversale." + lang)},
                     "limites": resoudre(src["limites"][lang], J, "limites." + lang)}
        lignes_csv.append(["croissance", src["transversale"]["titre"][lang], "transversale", "", lang,
                           src["transversale"]["statut"], "", out[lang]["transversale"]["texte"], "", ""])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["operation", "titre", "dimension", "libelle", "langue", "statut_source", "code", "texte", "sources", "famille"])
    w.writerows(lignes_csv)
    return {"matrice": out, "csv": buf.getvalue()}
