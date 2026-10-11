#!/usr/bin/env python3
"""Volet « Décider » du dossier Promesses : inventaire de l'article 19, acte par acte, en citations vérifiées.

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 1, E1 (v2 ; arbitrage
PRO-20261005-164029) ; refonte du 11/10/2026 (phase B) : D:/PRO/06_PROMOTION/RECHERCHE_LYCEES_LECTURE_2026-10-09/
REFONTE_PILOTE/PRESIDENT/ARBITRAGE_CE_PRESIDENT_PHASE_A.md et ARBITRAGE_CE_PRESIDENT_RELECTURE_JURIDIQUE.md. On n'écrit
aucune phrase « le président ne peut pas » ; on inventorie ce que le texte fait faire, exige et fait intervenir.

Entrée : data/pouvoirs_president.yaml (textes lus sur Légifrance, empreintes ; inventaire_19 acte par acte ; regles ;
fiches) et les réponses archivées par le serveur `sources` (D:/PRO/02_FABRIQUE/sources/archive/<mois>/<sha256>.json).
Script LOCAL : l'archive n'est pas dans le dépôt du site ; il s'arrête si elle manque.

DEUX COMPTES, DEUX UNITÉS (relecture juridique, 11/10/2026) — critère commun : un acte « sans proposition,
consultation ou acte d'un autre acteur exigé avant, ni intervention prévue d'un autre acteur pour la suite » quand ses
colonnes `condition` et `autre_autorite` sont vides dans le texte de SON article (niveau 1) ; les colonnes `partage`
et `limite` n'entrent pas dans le critère.
  - PAR RENVOI (convention du jeu publié le 06/10/2026) : chaque renvoi de l'article 19 est représenté par son acte
    `principal`, le premier que son article attribue au président ;
  - PAR ACTE : chaque acte distingué dans un même article (art. 8, 11, 18, 56 : deux actes).
Jamais présentés comme un dénombrement d'actes accomplis sans intervention de personne.

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  G1  chaque texte cité a sa réponse archivée, et celle-ci est bien le texte annoncé (numéro, identifiant, état) ;
  G2  chaque citation de l'inventaire, des règles, des fiches (entre « », réponse courte `bref` comprise) et du texte de la page figure MOT POUR MOT
      dans le texte archivé (espaces et apostrophes normalisés ; casse tolérée pour les fiches) ;
  G3  TÉMOIN DE COMPLÉTUDE : la liste des renvois de l'inventaire est relue dans le texte de l'article 19 lui-même ;
      un renvoi manquant ou en trop arrête ; chaque renvoi a le nombre d'actes attendu et un seul acte principal, le
      premier (ACTES_PAR_RENVOI : un acte fusionné ou oublié arrête) ;
  G4  « seulement » recalculé pour les deux comptes (strictement minoritaires) ; G4 bis : la colonne des pouvoirs
      partagés ne change aucun compte ;
  G5  le motif « sans tiers », « aucun tiers », « ni tiers », « without any third party », « no third party » est
      interdit dans les deux pages, les deux bases et les figures (relecture juridique : il donne au compte un sens
      général qu'il n'a pas) ;
  G6  chaque citation des colonnes porte temporalité, caractère facultatif et justification ; chaque case vide des
      colonnes condition, autre_autorite et limite porte sa justification (`vides`) ;
  G7  COMPTES TENUS : par renvoi = ATTENDU["renvoi"], par acte = ATTENDU["acte"] ; tout écart arrête jusqu'à relecture
      de la prose qui les commente ;
  G8  PROSE (réécrite le 11/10/2026 après la contre-expertise du rendu, Q1 ; resserrée, pas desserrée) : le compte par
      renvoi n'apparaît QUE dans un repli `<details class="repli">` de la section de méthode (`#methode`), jamais
      dans le parcours principal ni dans le front matter (chapô, description, FAQ, carte) ; tout paragraphe qui le
      donne porte son dénominateur (nombre de renvois) ET le compte par acte avec le sien (nombre d'actes) ; la
      description et les fiches de la figure ne le donnent pas ; chapô et description donnent le nombre de renvois
      par jeton ;
  G2-EN version anglaise : data/pouvoirs_president_en.yaml couvre chaque acte et chaque case (même nombre de
      citations) ; chaque citation anglaise de la Constitution figure mot pour mot dans la traduction publiée par le
      Conseil constitutionnel (scripts/sources_promesses_en/) ; “…” des fiches dans cette traduction, « … » en français.
Autotest de mutation (à chaque exécution) : chaque garde ci-dessus doit mordre sur une mutation réelle.

Écrit : data/pouvoirs_president_donnees.json (+ copie static/), static/pouvoirs_president_donnees.csv (UTF-8 BOM,
format long, une ligne par citation ou par case vide), data/figures_pouvoirs.json, static/img/pouvoirs-article19
{,-en}{,-m}.svg + .png (ensemble ou pas du tout). Rien n'est écrit à sorties identiques. Sortie console ASCII.
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
sys.path.insert(0, str(ROOT / "scripts" / "sources_promesses_en"))
sys.path.insert(0, str(ROOT / "scripts"))
import constitution_en as cen  # noqa: E402
import langue_generee as lg  # noqa: E402
import pied_figure  # noqa: E402

SRC = ROOT / "data" / "pouvoirs_president.yaml"
SRC_EN = ROOT / "data" / "pouvoirs_president_en.yaml"
PAGES = {"fr": ROOT / "content" / "pouvoirs-du-president-de-la-republique" / "_index.md",
         "en": ROOT / "content" / "pouvoirs-du-president-de-la-republique" / "_index.en.md"}
ARCHIVE = ROOT.parents[1] / "02_FABRIQUE" / "sources" / "archive"
OUT_DATA = ROOT / "data" / "pouvoirs_president_donnees.json"
OUT_STATIC = ROOT / "static" / "pouvoirs_president_donnees.json"
OUT_CSV = ROOT / "static" / "pouvoirs_president_donnees.csv"
OUT_FIGURES = ROOT / "data" / "figures_pouvoirs.json"
OUT_IMG = ROOT / "static" / "img"
FIG = "pouvoirs-article19"
PAGE_URL = "stephane-lalut.com/pouvoirs-du-president-de-la-republique/"
PAGE_URL_EN = "stephane-lalut.com/en/what-can-the-french-president-decide-alone/"
LEGIFRANCE = "https://www.legifrance.gouv.fr/loda/article_lc/"
JADE = "https://www.legifrance.gouv.fr/ceta/id/"

COLS = ["condition", "autre_autorite", "partage", "limite"]
ATTRIBUTS = [("condition", "Proposition, consultation ou acte d'un autre acteur exigé avant l'acte"),
             ("autre_autorite", "Un autre acteur intervient pour la suite (y compris de façon facultative)"),
             ("partage", "D'autres autorités disposent d'un pouvoir de même nature"),
             ("limite", "Autre encadrement écrit : temps, objet ou effet")]
ATTRIBUTS_EN = {"condition": "Recommendation, consultation or act of another actor required before the act",
                "autre_autorite": "Another actor steps in for what follows (including optionally)",
                "partage": "Other authorities hold a power of the same kind",
                "limite": "Other written limit: time, subject or effect"}
COURTS = {"fr": ["Exigé avant l'acte", "Autre acteur pour la suite", "Pouvoir partagé", "Autre cadre écrit"],
          "en": ["Required before the act", "Another actor afterwards", "Shared power", "Other written limit"]}
TEMPORALITES = {"avant", "pendant", "après", "permanent"}
# Structure des renvois (relecture juridique, § 2) : nombre d'actes distingués dans chaque article visé.
ACTES_PAR_RENVOI = {"8": 2, "11": 2, "12": 1, "16": 1, "18": 2, "54": 1, "56": 2, "61": 1}
# G7 : comptes tenus par la prose (arbitrage de la relecture juridique : « deux par renvoi », « trois par acte »).
ATTENDU = {"renvoi": 2, "acte": 3}
MOTIF_INTERDIT = re.compile(r"\b(?:sans|aucun|ni)\s+tiers\b|without\s+any\s+third\s+part|\bno\s+third\s+part", re.I)

# Citations du texte courant de la page (hors base) : un jeton par citation, vérifié dans les deux langues.
PROSE = {
    "cit19": ("19", "Les actes du Président de la République autres que ceux prévus aux articles 8 (1er alinéa), 11, 12, 16, 18, 54, 56 et 61 sont contresignés par le Premier ministre et, le cas échéant, par les ministres responsables.",
              "Instruments of the President of the Republic, other than those provided for under articles 8 (paragraph one), 11, 12, 16, 18, 54, 56 and 61, shall be countersigned by the Prime Minister and, where required, by the ministers concerned."),
    "cit8a": ("8", "Le Président de la République nomme le Premier ministre.",
              "The President of the Republic shall appoint the Prime Minister."),
    "cit8b": ("8", "Il met fin à ses fonctions sur la présentation par celui-ci de la démission du Gouvernement.",
              "He shall terminate the appointment of the Prime Minister when the latter tenders the resignation of the Government."),
    "cit5": ("5", "par son arbitrage, le fonctionnement régulier des pouvoirs publics ainsi que la continuité de l'Etat",  # graphie de Légifrance
             "by his arbitration, the proper functioning of the public authorities and the continuity of the State"),
    "cit37": ("37", "Les matières autres que celles qui sont du domaine de la loi ont un caractère réglementaire",
              "Matters other than those coming under the scope of statute law shall be matters for regulation"),
    "cit20": ("20", "Le Gouvernement détermine et conduit la politique de la Nation.",
              "The Government shall determine and conduct the policy of the Nation."),
    "cit20b": ("20", "Il est responsable devant le Parlement dans les conditions et suivant les procédures prévues aux articles 49 et 50",
               "It shall be accountable to Parliament in accordance with the terms and procedures set out in articles 49 and 50"),
    "cit50": ("50", "le Premier ministre doit remettre au Président de la République la démission du Gouvernement",
              "the Prime Minister shall tender the resignation of the Government to the President of the Republic"),
    "cit49": ("49", "ce projet est considéré comme adopté",
              "the Bill shall be considered passed"),
}


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r" ([,.;:])", r"\1", s)
    return s.strip()


def est_constitution(cle: str) -> bool:
    return re.fullmatch(r"\d+", cle) is not None


def charger_articles(base: dict) -> dict:
    """G1 : texte archivé de chaque source, contrôlé contre son identifiant, son numéro et son état."""
    if not ARCHIVE.is_dir():
        raise Arret("archive Legifrance introuvable (%s) : script local, lancer depuis D:/PRO" % ARCHIVE)
    textes = {}
    for cle, a in base["articles"].items():
        if not a.get("lu_le"):
            continue
        f = sorted(ARCHIVE.glob("*/%s.json" % a["empreinte"]))
        # Une même réponse relue un autre mois porte le même nom (son empreinte) : doublon permis s'il est identique.
        if not f or len({x.read_bytes() for x in f}) != 1:
            raise Arret("G1 %s : reponse archivee %s introuvable, ou doublons differents" % (cle, a["empreinte"][:12]))
        j = json.loads(f[0].read_text(encoding="utf-8"))
        if a.get("cetatext"):
            t = j.get("text") or {}
            if t.get("id") != a["cetatext"]:
                raise Arret("G1 %s : l'archive ne porte pas la decision annoncee (%s)" % (cle, t.get("id")))
            textes[str(cle)] = norm(html.unescape(re.sub(r"<[^>]+>", " ", t.get("texteHtml") or t.get("texte") or "")))
            continue
        art = j.get("article") or {}
        num, etat = str(a.get("num", cle)), a.get("etat", "VIGUEUR")
        if str(art.get("num")) != num or art.get("id") != a["legiarti"] or art.get("etat") != etat:
            raise Arret("G1 %s : l'archive ne porte pas l'article annonce (num %s, id %s, etat %s)"
                        % (cle, art.get("num"), art.get("id"), art.get("etat")))
        textes[str(cle)] = art["texte"]
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


def num_renvoi(e: dict) -> str:
    return re.match(r"\d+", e["renvoi"]).group(0)


def cases(e: dict, col: str) -> list[dict]:
    return e.get(col) or []


def sans_avant_ni_apres(e: dict) -> bool:
    return not (cases(e, "condition") or cases(e, "autre_autorite"))


def chaines(x) -> list[str]:
    """Toutes les chaînes d'une structure YAML (valeurs seulement, jamais les commentaires)."""
    if isinstance(x, str):
        return [x]
    if isinstance(x, dict):
        return [s for v in x.values() for s in chaines(v)]
    if isinstance(x, list):
        return [s for v in x for s in chaines(v)]
    return []


def paragraphes(md: str) -> list[str]:
    corps = md.split("\n---", 2)[-1] if md.startswith("---") else md
    return [p for p in re.split(r"\n\s*\n", corps) if p.strip()]


def front_matter(md: str) -> dict:
    return yaml.safe_load(md.split("\n---", 1)[0][3:]) if md.startswith("---") else {}


def jeton(p: str, nom: str) -> bool:
    return ('pv-val "%s"' % nom) in p or ("{pv.%s}" % nom) in p


def replis_methode(corps: str) -> list[tuple[int, int]]:
    """Étendues des replis `<details class="repli">` de la section `#methode` (jusqu'à l'intertitre suivant)."""
    m = re.search(r"^## [^\n]*\{#methode\}[ \t]*$", corps, re.M)
    if not m:
        return []
    fin = re.compile(r"^## ", re.M).search(corps, m.end())
    sec_fin = fin.start() if fin else len(corps)
    return [(m.end() + d.start(), m.end() + d.end())
            for d in re.finditer(r'<details class="repli">.*?</details>', corps[m.end():sec_fin], re.S)]


def garde_prose(pages: dict) -> str:
    """G8 (réécrite) : compte par renvoi seulement dans le repli de méthode, avec son dénominateur et le compte par acte."""
    n = 0
    for lang, md in pages.items():
        tete, corps = (md.split("\n---", 1) if md.startswith("---") else ("", md))
        if "n_seuls_renvoi" in tete:
            raise Arret("G8 page %s : compte par renvoi dans le front matter (chapo, description, FAQ ou carte) : "
                        "hors du repli de methode" % lang)
        replis = replis_methode(corps)
        pos = 0
        for bloc in re.split(r"(\n\s*\n)", corps):
            debut, pos = pos, pos + len(bloc)
            if not jeton(bloc, "n_seuls_renvoi"):
                continue
            n += 1
            if not any(a <= debut < b for a, b in replis):
                raise Arret("G8 page %s : compte par renvoi hors du repli de methode (#methode) : %r" % (lang, bloc.strip()[:80]))
            manque = [t for t in ("n_renvois", "n_seuls_acte", "n_actes") if not jeton(bloc, t)]
            if manque:
                raise Arret("G8 page %s : compte par renvoi sans %s dans le paragraphe %r"
                            % (lang, ", ".join(manque), bloc.strip()[:80]))
        fm = front_matter(md)
        for champ in ("chapo", "description"):
            if "{pv.n_renvois}" not in (fm.get(champ) or ""):
                raise Arret("G8 page %s : %s sans le jeton {pv.n_renvois} (nombre de renvois saisi a la main ?)" % (lang, champ))
    if n == 0:
        raise Arret("G8 : aucun paragraphe ne donne le compte par renvoi (la sensibilite exigee par l'arbitrage a disparu)")
    return ("G8 : %d paragraphe(s) donnent le compte par renvoi, tous dans le repli de methode, avec son denominateur et "
            "le compte par acte ; chapo et description par jeton" % n)


COMPTE_DISPOSITION = re.compile(r"compt\w* par disposition|counted by provision", re.I)


def garde_prose_figure(textes: list[str]) -> str:
    """G8, figures : leur description et leurs fiches ne donnent pas le compte par renvoi (il vit dans le repli de méthode)."""
    for t in textes:
        m = COMPTE_DISPOSITION.search(t)
        if m:
            raise Arret("G8 figure : compte par disposition hors du repli de methode : %r" % t[max(0, m.start() - 30):m.end() + 30])
    return "G8 figure : aucun compte par disposition dans %d textes de figure" % len(textes)


def garde_motif(base: dict, en: dict, pages: dict, svgs: list[str] | None = None) -> str:
    """G5 : motif interdit dans les pages, les bases et les figures."""
    lieux = [("page " + l, md) for l, md in pages.items()]
    lieux += [("base FR", s) for s in chaines({k: v for k, v in base.items() if k not in ("articles", "_en")})]
    lieux += [("base EN", s) for s in chaines(en)]
    lieux += [("figure", s) for s in (svgs or [])]
    for ou, s in lieux:
        m = MOTIF_INTERDIT.search(s)
        if m:
            raise Arret("G5 %s : motif interdit %r (dire : sans proposition, consultation ou acte d'un autre acteur avant, "
                        "ni intervention prevue d'un autre acteur pour la suite)" % (ou, m.group(0)))
    return "G5 : aucun motif « sans tiers » dans %d textes (%s)" % (len(lieux), "pages, bases, figures" if svgs else "pages, bases")


def calculer(base: dict, textes: dict, pages: dict) -> tuple[dict, list[str]]:
    gardes = []
    inv = base["inventaire_19"]
    ids = [e["id"] for e in inv]
    if len(set(ids)) != len(ids):
        raise Arret("G3 : identifiant d'acte en double")
    n_cites = 0
    for e in inv:
        verifier_cite(e["acte"], textes, "acte %s" % e["id"])
        n_cites += 1
        for col in COLS:
            v = e.get(col)
            if v is not None and not isinstance(v, list):
                raise Arret("G6 acte %s, %s : une case pleine est une liste de citations" % (e["id"], col))
            for i, c in enumerate(cases(e, col)):
                verifier_cite(c, textes, "acte %s, %s" % (e["id"], col))
                n_cites += 1
                # G6 : champ sémantique contrôlé de chaque citation.
                if c.get("temporalite") not in TEMPORALITES or not isinstance(c.get("facultatif"), bool) \
                        or not (c.get("justification") or "").strip():
                    raise Arret("G6 acte %s, %s, citation %d : temporalite, facultatif ou justification manquant"
                                % (e["id"], col, i + 1))
            if not cases(e, col) and col != "partage" and not ((e.get("vides") or {}).get(col) or "").strip():
                raise Arret("G6 acte %s, %s : case vide sans justification (`vides`)" % (e["id"], col))
    gardes.append("G2 : %d citations de l'inventaire retrouvees mot pour mot" % n_cites)
    gardes.append("G6 : chaque citation porte temporalite, facultatif et justification ; chaque case vide decisive est justifiee")
    for c in base["regles"]:
        verifier_cite(c, textes, "regles")
    gardes.append("G2 : %d citations de « qui fixe les regles » retrouvees" % len(base["regles"]))
    # G2 étendue : toute citation entre guillemets dans les fiches doit figurer dans l'un des textes que la fiche cite ;
    # « […] » sépare des fragments, chacun contrôlé. Des guillemets promettent une lettre.
    n_fiches = 0
    for p in base["pouvoirs"]:
        corpus = " ".join(norm(textes[str(a)]) for a in p["articles"] if str(a) in textes).casefold()
        for champ in ("bref", "decide", "condition", "tiers", "portee_texte", "chaine"):
            for q in re.findall(r"«\s*(.+?)\s*»", p.get(champ) or ""):
                for frag in re.split(r"\s*\[…\]\s*", q):
                    if norm(frag).casefold() not in corpus:  # seule tolérance : la casse (usage de citation)
                        raise Arret("G2 fiche %s, %s : citation absente des textes %s : %r"
                                    % (p["id"], champ, ",".join(p["articles"]), frag[:60]))
                    n_fiches += 1
    gardes.append("G2 : %d citations entre guillemets des fiches retrouvees" % n_fiches)

    attendus = renvois_article19(textes["19"])
    inventaire = sorted({num_renvoi(e) for e in inv}, key=int)
    if sorted(attendus, key=int) != inventaire:
        raise Arret("G3 : renvois de l'article 19 %s != inventaire %s" % (attendus, inventaire))
    for r in inventaire:
        actes = [e for e in inv if num_renvoi(e) == r]
        if len(actes) != ACTES_PAR_RENVOI.get(r):
            raise Arret("G3 renvoi %s : %d acte(s) dans l'inventaire pour %s attendu(s) (acte fusionne ou oublie ?)"
                        % (r, len(actes), ACTES_PAR_RENVOI.get(r)))
        if [bool(e.get("principal")) for e in actes] != [True] + [False] * (len(actes) - 1):
            raise Arret("G3 renvoi %s : il faut un seul acte principal, le premier" % r)
    gardes.append("G3 : inventaire complet, %d renvois relus dans l'article 19 (%s), %d actes"
                  % (len(attendus), ", ".join(attendus), len(inv)))

    principaux = [e for e in inv if e.get("principal")]
    seuls_r = [e for e in principaux if sans_avant_ni_apres(e)]
    seuls_a = [e for e in inv if sans_avant_ni_apres(e)]
    # G4 : « seulement » n'est écrit que si les actes retenus sont strictement minoritaires, pour chaque unité.
    for unite, seuls, tous in (("renvoi", seuls_r, principaux), ("acte", seuls_a, inv)):
        if not (0 < len(seuls) and 2 * len(seuls) < len(tous)):
            raise Arret("G4 par %s : %d sur %d sans condition ni intervention ulterieure : « seulement » est faux"
                        % (unite, len(seuls), len(tous)))
    gardes.append("G4 : « seulement » tenu par renvoi (%d sur %d) et par acte (%d sur %d)"
                  % (len(seuls_r), len(principaux), len(seuls_a), len(inv)))
    partage_seul = [e["id"] for e in seuls_a if cases(e, "partage")]
    if partage_seul:
        raise Arret("G4 bis : %s : seul un pouvoir partage les distingue ; « n'y change rien » est faux" % partage_seul)
    gardes.append("G4 bis : la colonne des pouvoirs partages ne change aucun compte")
    # G7 : les comptes que la prose commente.
    if len(seuls_r) != ATTENDU["renvoi"] or len(seuls_a) != ATTENDU["acte"]:
        raise Arret("G7 : comptes par renvoi %d et par acte %d, la prose est relue pour %d et %d : relire la page, puis "
                    "ATTENDU" % (len(seuls_r), len(seuls_a), ATTENDU["renvoi"], ATTENDU["acte"]))
    gardes.append("G7 : comptes tenus (par renvoi %d, par acte %d)" % (len(seuls_r), len(seuls_a)))

    compte = {col: sum(1 for e in inv if cases(e, col)) for col in COLS}
    r = {"n_renvois": len(principaux), "n_actes": len(inv), "compte": compte,
         "seuls_renvoi": [e["id"] for e in seuls_r], "seuls_acte": [e["id"] for e in seuls_a],
         "inventaire": inv, "regles": base["regles"]}
    for k, (art, c_fr, c_en) in PROSE.items():
        verifier_cite({"art": art, "cite": c_fr}, textes, "texte de la page, " + k)
        try:
            cen.citer(art, c_en)
        except ValueError as e:
            raise Arret("G2-EN texte de la page, %s : %s" % (k, e))
    gardes.append("G2 : %d citations du texte de la page retrouvees (FR et EN)" % len(PROSE))
    if base.get("_en") is not None:
        gardes.append(verifier_en(base, base["_en"], textes))
        gardes.append(garde_motif(base, base["_en"], pages))
    gardes.append(garde_prose(pages))
    return r, gardes


def en_cite(x) -> tuple[str, str | None]:
    return (x, None) if isinstance(x, str) else (x["cite"], x.get("contexte"))


def verifier_en(base: dict, en: dict, textes: dict) -> str:
    """G2-EN : couverture de la couche anglaise, citations dans la traduction du Conseil constitutionnel."""
    try:
        tcen = cen.texte()
        n = 0
        for e in base["inventaire_19"]:
            x = en["inventaire_19"].get(e["id"])
            if not x or not x.get("pouvoir") or not x.get("acte"):
                raise Arret("G2-EN : acte %s sans traduction" % e["id"])
            cen.citer(str(e["acte"]["art"]), en_cite(x["acte"])[0], tcen)
            n += 1
            for col in COLS:
                fr, tr = cases(e, col), x.get(col) or []
                if len(fr) != len(tr):
                    raise Arret("G2-EN : acte %s, %s : %d citation(s) en francais, %d en anglais" % (e["id"], col, len(fr), len(tr)))
                for c, t in zip(fr, tr):
                    cen.citer(str(c["art"]), en_cite(t)[0], tcen)
                    if bool(c.get("contexte")) != bool(en_cite(t)[1]):
                        raise Arret("G2-EN : acte %s, %s : contexte present dans une seule langue" % (e["id"], col))
                    n += 1
        if len(en["regles"]) != len(base["regles"]):
            raise Arret("G2-EN : regles : %d en anglais pour %d" % (len(en["regles"]), len(base["regles"])))
        for c, x in zip(base["regles"], en["regles"]):
            cen.citer(str(c["art"]), x["cite"], tcen)
            n += 1
        for g in base["groupes"]:
            if not (en["groupes"].get(g["id"]) or {}).get("titre"):
                raise Arret("G2-EN : groupe %s sans traduction" % g["id"])
        q = 0
        for p in base["pouvoirs"]:
            x = en["pouvoirs"].get(p["id"])
            if not x or any(not x.get(k) for k in ("question", "pouvoir", "bref", "decide", "condition", "tiers", "portee_texte")):
                raise Arret("G2-EN : fiche %s : traduction incomplete" % p["id"])
            if bool(p.get("chaine")) != bool(x.get("chaine")):
                raise Arret("G2-EN : fiche %s : champ chaine present dans une seule langue" % p["id"])
            corpus = " ".join(cen.article(str(a), tcen) for a in p["articles"] if est_constitution(str(a))).casefold()
            corpus_fr = " ".join(norm(textes[str(a)]) for a in p["articles"] if str(a) in textes).casefold()
            for champ in ("bref", "decide", "condition", "tiers", "portee_texte", "chaine"):
                for s in re.findall(r"“(.+?)”", x.get(champ) or ""):
                    if cen.norm(s).rstrip(".,;:").casefold() not in corpus:
                        raise Arret("G2-EN fiche %s, %s : citation absente de la traduction des articles %s : %r"
                                    % (p["id"], champ, ",".join(p["articles"]), s[:60]))
                    q += 1
                for s in re.findall(r"«\s*(.+?)\s*»", x.get(champ) or ""):
                    if norm(s).casefold() not in corpus_fr:
                        raise Arret("G2-EN fiche %s, %s : citation francaise absente : %r" % (p["id"], champ, s[:60]))
                    q += 1
    except ValueError as e:
        raise Arret("G2-EN : %s" % e)
    return "G2-EN : %d citations anglaises (Conseil constitutionnel) et %d citations des fiches anglaises retrouvees" % (n, q)


def minuscule(s: str) -> str:
    return s[0].lower() + s[1:]


def affichage(r: dict, base: dict, lang: str) -> dict:
    en = base["_en"]["inventaire_19"] if lang == "en" else None
    nom = (lambda i: en[i]["pouvoir"]) if lang == "en" else (lambda i: next(e["pouvoir"] for e in r["inventaire"] if e["id"] == i))
    L = lambda n: lg.lettres(n, lang)  # noqa: E731
    seuls_a = [minuscule(nom(i)) for i in r["seuls_acte"]]
    seuls_r = [minuscule(nom(i)) for i in r["seuls_renvoi"]]
    d = {
        "n_renvois": L(r["n_renvois"]),
        "n_actes": L(r["n_actes"]),
        "n_seuls_renvoi": L(len(r["seuls_renvoi"])),
        "n_seuls_acte": L(len(r["seuls_acte"])),
        "n_seuls_acte_maj": L(len(r["seuls_acte"])).capitalize(),
        "n_encadres_acte": L(r["n_actes"] - len(r["seuls_acte"])),
        "seuls_acte_liste": lg.enumere(seuls_a, lang),
        "seuls_renvoi_liste": lg.enumere(seuls_r, lang),
        **{k: v[1 if lang == "fr" else 2] for k, v in PROSE.items()},
    }
    if lang == "fr":
        d["releve_le"] = "%s (textes lus sur Légifrance du %s au %s)" % (
            date.fromisoformat(r["releve_le"]).strftime("%d/%m/%Y"),
            date.fromisoformat(r["lu_min"]).strftime("%d/%m/%Y"), date.fromisoformat(r["releve_le"]).strftime("%d/%m/%Y"))
    else:
        f = "%#d %B %Y" if sys.platform == "win32" else "%-d %B %Y"
        d["releve_le"] = ("%s (texts read on Légifrance from %s to %s; quoted in the English translation published by "
                          "the Conseil constitutionnel)" % (date.fromisoformat(r["releve_le"]).strftime(f),
                                                            date.fromisoformat(r["lu_min"]).strftime(f),
                                                            date.fromisoformat(r["releve_le"]).strftime(f)))
    return d


# ------------------------------------------------------------------ figures (charte des dossiers du site)
W = 720
BLEU = "#184f95"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
# Contour des pastilles vides (contre-expertise du rendu, 11/10/2026 : trop pâle en GRID) : MUTED, contraste 3,6:1 sur blanc.
VIDE = MUTED
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCE = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL,
           "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCE_M = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · stephane-lalut.com",
             "en": "Compiled by Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
TXT = {
    "fr": {"titre": "Les {n} dispositions de l’article 19, acte par acte : ce que le texte de chaque article exige avant, "
                    "qui il fait intervenir ensuite",
           "t1": "L’article 19 dispense de contreseing {n} dispositions",
           "t2": "acte par acte, ce que le texte de chaque article exige ou fait intervenir",
           "titre_m": "L’article 19 dispense de contreseing {n} dispositions : acte par acte, ce que dit chaque article",
           "source": "Constitution du 4 octobre 1958, art. 8, 11, 12, 16, 18, 19, 54, 56, 61, versions en vigueur lues "
                     "sur Légifrance",
           "note": "Case pleine : citation exacte de l’article (liste et justification sur la page). Case vide : rien "
                   "dans cet article ; ne dit rien des autres articles ni de la pratique. « Exigé avant » : proposition, "
                   "consultation ou acte d’un autre acteur ; « autre acteur » : institution, autorité ou corps électoral à "
                   "qui l’article attribue une intervention distincte après l’acte, même facultative ; les modalités "
                   "matérielles d’exécution ne comptent pas.",
           "note_m": "Case pleine : citation exacte de l’article ; case vide : rien dans cet article. Définitions et "
                     "citations : section « Comment le tableau est-il établi ? » de la page.",
           "renvoi": "art. ", "plein": "présent", "vide": "absent"},
    "en": {"titre": "The {n} provisions of article 19 of the French Constitution, act by act: what the text of each "
                    "article requires beforehand, whom it brings in afterwards",
           "t1": "Article 19 exempts {n} provisions from countersignature",
           "t2": "act by act, what the text of each article requires or brings in",
           "titre_m": "Article 19 exempts {n} provisions from countersignature: act by act, what each article says",
           "source": "Constitution of 4 October 1958, arts. 8, 11, 12, 16, 18, 19, 54, 56, 61 (Légifrance; English "
                     "translation: Conseil constitutionnel)",
           "note": "Filled cell: exact quotation of the article (list and justification on the page). Empty cell: "
                   "nothing in that article; says nothing of other articles or of practice. “Required before”: "
                   "recommendation, consultation or act of another actor; “another actor”: an institution, authority or "
                   "electorate to which the article assigns a distinct intervention after the act, even an optional "
                   "one; practical arrangements for carrying out the act are not counted.",
           "note_m": "Filled cell: exact quotation of the article; empty cell: nothing in that article. Definitions and "
                     "quotations: section “How is the table established?” on the page.",
           "renvoi": "art. ", "plein": "present", "vide": "absent"},
}


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def lignes_de(inv: list[dict], base: dict, lang: str) -> list[dict]:
    out = []
    for e in inv:
        x = base["_en"]["inventaire_19"][e["id"]] if lang == "en" else e
        renvoi = e["renvoi"].replace("al.", "para.") if lang == "en" else e["renvoi"]
        out.append({"id": e["id"], "court": x.get("court", x["pouvoir"]), "renvoi": renvoi,
                    "cases": [bool(cases(e, c)) for c in COLS]})
    return out


def desc_figure(r: dict, A: dict, lang: str) -> str:
    if lang == "fr":
        return ("Matrice de %s actes répartis entre les %s dispositions de l'article 19, et quatre colonnes. Une case pleine "
                "signifie que l'article lui-même contient une citation exacte de l'élément. %s actes n'y ont ni "
                "élément exigé avant l'acte ni autre acteur pour la suite : %s."
                % (A["n_actes"], A["n_renvois"], A["n_seuls_acte_maj"], A["seuls_acte_liste"]))
    return ("Matrix of %s acts spread over the %s provisions of article 19, and four columns. A filled cell means that "
            "the article itself contains an exact quotation of the element. %s acts have neither an element required "
            "before the act nor another actor afterwards: %s."
            % (A["n_actes"], A["n_renvois"], A["n_seuls_acte_maj"], A["seuls_acte_liste"]))


def figure(r: dict, base: dict, A: dict, lang: str) -> str:
    T = {k: v.replace("{n}", A["n_renvois"]) for k, v in TXT[lang].items()}
    rows = lignes_de(r["inventaire"], base, lang)
    top, pas, col0, colw = 104, 30, 360, 90
    e = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 0" role="img" aria-labelledby="pv-t pv-d" '
         'font-family="%s">' % (W, FONT),
         '<title id="pv-t">%s</title><desc id="pv-d">%s</desc>' % (esc(T["titre"]), esc(desc_figure(r, A, lang))),
         '<rect width="%d" height="0" fill="#ffffff"/>' % W,
         txt(0, 18, T["t1"], 14, INK, weight="600"),
         txt(0, 37, T["t2"], 12, INK2)]
    for k, lib in enumerate(COURTS[lang]):
        cx = col0 + colw * k + colw / 2
        ls = pied_figure.coupe(lib, 13)
        if len(ls) > 4:  # jamais de troncature silencieuse d'un libellé
            raise Arret("figure : libellé de colonne trop long : %r" % lib)
        for i, l in enumerate(ls):
            e.append(txt(cx, top - 12 - 13 * (len(ls) - 1 - i), l, 11, INK2, "middle"))
    y = top
    prec = None
    for i, ro in enumerate(rows):
        nr = re.match(r"\d+", ro["renvoi"]).group(0)
        if prec is not None and nr != prec:
            e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y, W, y, GRID))
        prec = nr
        ls = pied_figure.coupe(ro["court"], 44)
        h = pas if len(ls) == 1 else pas + 13 * (len(ls) - 1)
        yc = y + h / 2
        if i % 2 == 0:
            e.append('<rect x="0" y="%.1f" width="%d" height="%.1f" fill="#f7f5f0"/>' % (y, W, h))
        for j, l in enumerate(ls):
            e.append(txt(0, yc + 4 - 6.5 * (len(ls) - 1) + 13 * j, l, 12, INK))
        e.append(txt(col0 - 8, yc + 4, T["renvoi"] + ro["renvoi"], 11, MUTED, "end"))
        for k, plein in enumerate(ro["cases"]):
            cx = col0 + colw * k + colw / 2
            if plein:
                e.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/>' % (cx, yc, BLEU))
            else:
                e.append('<circle cx="%.1f" cy="%.1f" r="6.5" fill="none" stroke="%s" stroke-width="1.5"/>' % (cx, yc, VIDE))
        y += h
    return pied_figure.pied(e, y + 6, W, [(T["source"], INK2, "pied-source"), (T["note"], INK2, "pied-note"),
                                          (LICENCE[lang], MUTED, "pied-licence")], GRID)


def figure_m(r: dict, base: dict, A: dict, lang: str, svg_d: str) -> str:
    """Version téléphone, par disposition : un bloc par acte, ses quatre éléments en clair."""
    T = {k: v.replace("{n}", A["n_renvois"]) for k, v in TXT[lang].items()}
    desc = html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", svg_d, re.S).group(1))
    e, y = pied_figure.tete_mobile("pvm", T["titre_m"], desc, INK, FONT)
    rows = lignes_de(r["inventaire"], base, lang)
    prec = None
    for ro in rows:
        nr = re.match(r"\d+", ro["renvoi"]).group(0)
        y += 10
        if nr != prec:
            e.append('<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y - 4, pied_figure.LARGEUR_M, y - 4, GRID))
            prec = nr
        for l in pied_figure.coupe(ro["court"], 32):
            y += 18
            e.append(txt(0, y, l, 15, INK, weight="600"))
        y += 17
        e.append(txt(0, y, T["renvoi"] + ro["renvoi"], pied_figure.POLICE_M, MUTED))
        for k, plein in enumerate(ro["cases"]):
            y += 19
            if plein:
                e.append('<circle cx="7" cy="%.1f" r="6" fill="%s"/>' % (y - 4.5, BLEU))
            else:
                e.append('<circle cx="7" cy="%.1f" r="5.5" fill="none" stroke="%s" stroke-width="1.5"/>' % (y - 4.5, VIDE))
            e.append(txt(20, y, COURTS[lang][k], pied_figure.POLICE_M, INK if plein else MUTED))
    return pied_figure.pied_mobile(e, y + 14, [(T["source"], INK2, "pied-source"), (T["note_m"], INK2, "pied-note"),
                                               (LICENCE_M[lang], MUTED, "pied-licence")], GRID)


def parite(svg_d: str, svg_m: str) -> list[str]:
    """Témoin de la version téléphone : autant de cases pleines et vides, même ordre, police jamais sous le minimum."""
    pl = lambda s: re.findall(r'<circle [^>]*?(fill="%s"|fill="none")' % BLEU, s)  # noqa: E731
    out = []
    if pl(svg_d) != pl(svg_m):
        out.append("cases pleines et vides differentes entre bureau (%d) et telephone (%d)" % (len(pl(svg_d)), len(pl(svg_m))))
    if not pl(svg_d):
        out.append("aucune case lue (controle aveugle)")
    tailles = [float(x) for x in re.findall(r'font-size="([0-9.]+)"', svg_m)]
    if min(tailles) < pied_figure.POLICE_M:
        out.append("police %.1f sous le minimum" % min(tailles))
    return out


def fiches_figures(svgs: dict, A: dict) -> dict:
    out = {}
    for lang, sf in (("fr", ""), ("en", "-en")):
        svg = svgs[FIG + sf + ".svg"]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        a = A[lang]
        if lang == "fr":
            montre = ("Les %s dispositions que l'article 19 dispense de contreseing contiennent %s actes. %s de ces actes font intervenir, dans leur "
                      "propre article, un autre acteur avant ou après la décision du président. %s seulement n'y prévoient "
                      "ni proposition, consultation ou acte d'un autre acteur avant l'acte, ni intervention d'un autre "
                      "acteur pour la suite : %s. Ce compte décrit le texte de chaque article, non la pratique."
                      % (a["n_renvois"], a["n_actes"], a["n_encadres_acte"].capitalize(), a["n_seuls_acte_maj"],
                         a["seuls_acte_liste"]))
        else:
            montre = ("The %s provisions that article 19 exempts from countersignature contain %s acts. %s of these acts bring in, in their own article, "
                      "another actor before or after the president's decision. Only %s provide there for neither a "
                      "recommendation, consultation or act of another actor before the act nor the intervention of "
                      "another actor afterwards: %s. This count describes the text of each article, not practice."
                      % (a["n_renvois"], a["n_actes"], a["n_encadres_acte"].capitalize(), a["n_seuls_acte"],
                         a["seuls_acte_liste"]))
        out[lang] = [dict(id="article19", fichier=FIG + sf, titre=titre, montre=montre,
                          source=pied_figure.lire(svg, "pied-source"), precaution=pied_figure.lire(svg, "pied-note"))]
        if out[lang][0]["source"] == "" or out[lang][0]["precaution"] == "":
            raise Arret("fiche : pied illisible dans le SVG %s" % lang)
    return out


def csv_texte(r: dict, base: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["acte_id", "renvoi", "acte", "principal", "attribut", "present", "article", "citation", "contexte",
                "temporalite", "facultatif", "justification", "legiarti", "lu_le"])
    for e in r["inventaire"]:
        rang = ["oui" if e.get("principal") else "non"]
        a = base["articles"][str(e["acte"]["art"])]
        w.writerow([e["id"], e["renvoi"], e["pouvoir"]] + rang + ["acte", "oui", e["acte"]["art"], e["acte"]["cite"],
                    e["acte"].get("contexte", ""), "", "", "", a["legiarti"], a["lu_le"]])
        for col in COLS:
            if not cases(e, col):
                w.writerow([e["id"], e["renvoi"], e["pouvoir"]] + rang + [col, "non", "", "", "", "", "",
                            (e.get("vides") or {}).get(col, ""), "", ""])
            for c in cases(e, col):
                a = base["articles"][str(c["art"])]
                w.writerow([e["id"], e["renvoi"], e["pouvoir"]] + rang + [col, "oui", c["art"], c["cite"],
                            c.get("contexte", ""), c["temporalite"], "oui" if c["facultatif"] else "non",
                            c["justification"], a["legiarti"], a["lu_le"]])
    for c in r["regles"]:
        a = base["articles"][str(c["art"])]
        w.writerow(["", "", "qui fixe les regles : " + c["objet"], "", "regle", "oui", c["art"], c["cite"], "", "", "",
                    "", a["legiarti"], a["lu_le"]])
    return buf.getvalue()


def mordre(m_base: dict, textes: dict, pages: dict, prefixe: str, nom: str) -> str:
    try:
        calculer(m_base, textes, pages)
    except Arret as e:
        if not str(e).startswith(prefixe):
            raise Arret("mutation %s : arret par une autre garde que %s : %s" % (nom, prefixe, e))
        return "%s -> %s" % (nom, str(e)[:70])
    raise Arret("mutation %s : %s n'a pas mordu, controle ABSENT" % (nom, prefixe))


def autotest(base: dict, textes: dict, pages: dict) -> list[str]:
    """Mutations réelles : chacune DOIT faire mordre sa garde, sinon le contrôle est réputé absent."""
    out = []
    m = copy.deepcopy(base)
    next(e for e in m["inventaire_19"] if e["id"] == "12")["condition"][0]["cite"] += " sans délai"
    out.append(mordre(m, textes, pages, "G2", "citation alteree"))
    m = copy.deepcopy(base)
    fiche = next(p for p in m["pouvoirs"] if "«" in (p.get("portee_texte") or ""))
    fiche["portee_texte"] = fiche["portee_texte"].replace("«", "« selon toute vraisemblance", 1)
    out.append(mordre(m, textes, pages, "G2 fiche", "guillemets de fiche alteres"))
    # Passe B2 (11/10/2026) : la reponse courte (`bref`, seule visible) est sous la meme garde que le reste de la fiche.
    m = copy.deepcopy(base)
    next(p for p in m["pouvoirs"] if p["id"] == "dissolution")["bref"] += " « Il peut dissoudre sans consulter personne. »"
    out.append(mordre(m, textes, pages, "G2 fiche", "citation inventee dans une reponse courte"))
    m = copy.deepcopy(base)
    m["_en"]["pouvoirs"]["dissolution"].pop("bref")
    out.append(mordre(m, textes, pages, "G2-EN", "reponse courte anglaise absente"))
    m = copy.deepcopy(base)
    m["_en"]["inventaire_19"]["12"]["condition"][0] += " without delay"
    out.append(mordre(m, textes, pages, "G2-EN", "citation anglaise alteree"))
    m = copy.deepcopy(base)
    next(e for e in m["inventaire_19"] if e["id"] == "54")["autre_autorite"] = None
    m["inventaire_19"][[e["id"] for e in m["inventaire_19"]].index("54")].setdefault("vides", {})["autre_autorite"] = "mutation"
    out.append(mordre(m, textes, pages, "G4 bis", "pouvoir partage seul"))
    m = copy.deepcopy(base)
    m["inventaire_19"] = [e for e in m["inventaire_19"] if num_renvoi(e) != "54"]
    out.append(mordre(m, textes, pages, "G3", "renvoi retire"))
    # Nouvelles (11/10/2026) : acte fusionné, case sans justification, motif interdit, sensibilité absente, compte changé.
    m = copy.deepcopy(base)
    m["inventaire_19"] = [e for e in m["inventaire_19"] if e["id"] != "56-president"]
    out.append(mordre(m, textes, pages, "G3", "acte fusionne (56 : president du Conseil retire)"))
    m = copy.deepcopy(base)
    next(e for e in m["inventaire_19"] if e["id"] == "16")["autre_autorite"][0]["justification"] = " "
    out.append(mordre(m, textes, pages, "G6", "case sans justification"))
    m = copy.deepcopy(base)
    next(e for e in m["inventaire_19"] if e["id"] == "8-nommer")["vides"].pop("limite")
    out.append(mordre(m, textes, pages, "G6", "case vide sans justification"))
    m = copy.deepcopy(base)
    next(p for p in m["pouvoirs"] if p["id"] == "messages-parlement")["tiers"] = "Aucun : le président agit sans tiers."
    out.append(mordre(m, textes, pages, "G5", "motif « sans tiers » dans une fiche"))
    m = copy.deepcopy(base)
    m["_en"]["pouvoirs"]["messages-parlement"]["tiers"] = "None: without any third party."
    out.append(mordre(m, textes, pages, "G5", "motif « without any third party » dans une fiche anglaise"))
    m = copy.deepcopy(base)
    e12 = next(e for e in m["inventaire_19"] if e["id"] == "12")
    e12["condition"], e12["autre_autorite"] = None, None
    e12["vides"] = {"condition": "mutation", "autre_autorite": "mutation"}
    out.append(mordre(m, textes, pages, "G7", "compte change (dissolution sans consultation ni electeurs)"))
    p2 = dict(pages)
    p2["fr"] = pages["fr"] + '\n\nDeux seulement : {{< pv-val "n_seuls_renvoi" >}}, sans plus.\n'
    out.append(mordre(base, textes, p2, "G8", "compte par renvoi sans sa sensibilite"))
    # G8 réécrite (11/10/2026) : le paragraphe complet du repli, remis dans le parcours principal, doit être refusé ;
    # le même paragraphe privé de son dénominateur, resté dans le repli, aussi.
    for lang in ("fr", "en"):
        corps = pages[lang]
        par = next(b for b in re.split(r"\n\s*\n", corps) if jeton(b, "n_seuls_renvoi"))
        p2 = dict(pages)
        p2[lang] = corps.replace('<div class="resultat-phrase">\n', '<div class="resultat-phrase">\n\n' + par + "\n", 1)
        if p2[lang] == corps:
            raise Arret("mutation G8 : bloc du resultat introuvable (%s)" % lang)
        out.append(mordre(base, textes, p2, "G8", "compte par disposition remis dans le parcours principal (%s)" % lang))
        sans = re.sub(r'(?:sur|out of) \{\{< pv-val "n_renvois" >\}\}', "", par, count=1)
        if sans == par:
            raise Arret("mutation G8 : denominateur introuvable (%s)" % lang)
        p2 = dict(pages)
        p2[lang] = corps.replace(par, sans, 1)
        out.append(mordre(base, textes, p2, "G8", "compte par disposition sans son denominateur (%s)" % lang))
    try:
        garde_prose_figure(["Compté par disposition, chacune représentée par son premier acte, le même critère en retient deux."])
    except Arret as e:
        out.append("compte par disposition dans la description de la figure -> %s" % str(e)[:70])
    else:
        raise Arret("mutation G8 figure : n'a pas mordu, controle ABSENT")
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
    base["_en"] = yaml.safe_load(SRC_EN.read_text(encoding="utf-8"))
    pages = {l: f.read_text(encoding="utf-8") for l, f in PAGES.items()}
    textes = charger_articles(base)
    r, gardes = calculer(base, textes, pages)
    for m in autotest(base, textes, pages):
        log("autotest : la mutation a mordu : " + m)
    lus = [str(base["articles"][str(c["art"])]["lu_le"]) for e in r["inventaire"]
           for c in [e["acte"]] + [x for col in COLS for x in cases(e, col)]]
    lus += [str(base["articles"][str(c["art"])]["lu_le"]) for c in r["regles"]]
    r["releve_le"], r["lu_min"] = max(lus), min(lus)
    A = {lang: affichage(r, base, lang) for lang in ("fr", "en")}
    if set(A["fr"]) != set(A["en"]):
        raise Arret("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(A["fr"]) ^ set(A["en"])))
    svgs = {}
    for lang, sf in (("fr", ""), ("en", "-en")):
        svgs[FIG + sf + ".svg"] = figure(r, base, A[lang], lang)
        svgs[FIG + sf + "-m.svg"] = figure_m(r, base, A[lang], lang, svgs[FIG + sf + ".svg"])
        ec = parite(svgs[FIG + sf + ".svg"], svgs[FIG + sf + "-m.svg"])
        if ec:
            raise Arret("parite telephone %s : %s" % (lang, " ; ".join(ec)))
        for nom in (FIG + sf + ".svg", FIG + sf + "-m.svg"):
            hc = pied_figure.hors_cadre(svgs[nom], W if not nom.endswith("-m.svg") else pied_figure.LARGEUR_M)
            if hc:
                log("ALERTE estimation hors cadre (%s) : %s" % (nom, " | ".join(hc[:3])))
    gardes.append(garde_motif(base, base["_en"], pages, [html.unescape(re.sub(r"<[^>]+>", " ", s)) for s in svgs.values()]))
    fiches_fig = fiches_figures(svgs, A)
    gardes.append(garde_prose_figure([html.unescape(re.sub(r"<[^>]+>", " ", s)) for s in svgs.values()]
                                     + [f["montre"] for l in fiches_fig.values() for f in l]))
    gardes.append("parite telephone : 4 figures, cases identiques au bureau, police >= %.1f" % pied_figure.POLICE_M)
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(gardes))
        for g in gardes:
            log("   " + g)
        return 0
    try:
        import cairosvg
    except ImportError:
        raise Arret("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout")
    fiches = fiches_fig
    csvt = csv_texte(r, base)
    principaux = [e for e in r["inventaire"] if e.get("principal")]
    payload = {
        "releve_le": r["releve_le"],
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; textes : Légifrance (DILA), Licence Ouverte",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Décider, E1 ; refonte du 11/10/2026",
                 "statut": "lecture documentaire de la Constitution, sans certification juridique ; chaque case « lue sur "
                           "le texte » par l'équipe de rédaction, aucune relue par un juriste",
                 "definitions": dict(ATTRIBUTS),
                 "niveaux": {"1": "texte de l'article visé par l'article 19 (seul périmètre de la matrice et des comptes)",
                             "2": "chaîne constitutionnelle et organique (fiches, champ chaine)",
                             "3": "exercice politique, jurisprudence et pratique (prose de la page)"},
                 "criteres": {"commun": "acte sans proposition, consultation ou acte d'un autre acteur exigé avant, ni "
                                        "intervention prévue d'un autre acteur pour la suite, dans le texte de son article "
                                        "(colonnes condition et autre_autorite vides)",
                              "par_renvoi": "chaque renvoi de l'article 19 représenté par son acte principal, le premier "
                                            "que son article attribue au président (convention du jeu publié le 06/10/2026)",
                              "par_acte": "chaque acte distingué dans un même article"},
                 "lecture": "Une case renseignée = une ou plusieurs citations exactes de l'article indiqué ; une case vide "
                            "ne dit rien des autres articles ni de la pratique institutionnelle."},
        "gardes": gardes,
        "inventaire": [dict(e, legifrance={col: [LEGIFRANCE + base["articles"][str(c["art"])]["legiarti"] for c in cases(e, col)]
                                            for col in COLS if cases(e, col)}) for e in r["inventaire"]],
        "regles": r["regles"],
        "comptes": dict(r["compte"], n_renvois=r["n_renvois"], n_actes=r["n_actes"],
                        par_renvoi=r["seuls_renvoi"], par_acte=r["seuls_acte"],
                        renvois_principaux=[e["id"] for e in principaux]),
        "affichage": A["fr"],
        "affichage_en": A["en"],
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    identiques = (OUT_DATA.exists() and OUT_DATA.read_text(encoding="utf-8") == txt_json and OUT_CSV.exists()
                  and OUT_CSV.read_text(encoding="utf-8-sig") == csvt
                  and all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s for n, s in svgs.items())
                  and all((OUT_IMG / n.replace(".svg", ".png")).exists() for n in svgs)
                  and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches)
    if identiques:
        log("Donnees et figures identiques : rien ecrit.")
        return 0
    OUT_DATA.write_text(txt_json, encoding="utf-8")
    OUT_STATIC.write_text(txt_json, encoding="utf-8")
    OUT_CSV.write_text(csvt, encoding="utf-8-sig", newline="\n")
    for n, s in svgs.items():
        (OUT_IMG / n).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")),
                         output_width=1440 if not n.endswith("-m.svg") else 900, background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for g in gardes:
        log("OK " + g)
    log("Ecrit : data/pouvoirs_president_donnees.json, static/pouvoirs_president_donnees.{json,csv}, "
        "data/figures_pouvoirs.json, static/img/%s{,-en}{,-m}.svg + .png" % FIG)
    return 0


if __name__ == "__main__":
    sys.exit(main())
