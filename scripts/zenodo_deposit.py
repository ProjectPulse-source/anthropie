#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Création d'une deposition BROUILLON Zenodo pour un AWP + réservation de DOI.

Doctrine maison (03_DOCTRINE_PRODUCTION_v1.md §11) : réserver le DOI AVANT le build
PDF, NE JAMAIS publier par script — la publication est un geste auteur.
Garde-fous : dry-run par défaut ; vérification anti-doublon sur les brouillons
existants ; le token n'est jamais affiché.

Usage :
  python zenodo_deposit.py --list                      # inventaire des brouillons
  python zenodo_deposit.py --papers                    # fiches disponibles
  python zenodo_deposit.py --mirror 21200286           # lire licence/communauté d'un record
  python zenodo_deposit.py --create awp01-es           # dry-run (affiche le payload)
  python zenodo_deposit.py --create awp01-es --apply   # crée le brouillon + réserve le DOI
  python zenodo_deposit.py --upload ID FICHIER         # attache un fichier au brouillon

⚠ L'ORCID est posé par le générateur (contrôle n°2 de zenodo_audit_complet.py).
   AWP-08 était sorti sans lui : la correction avait porté sur le dépôt, pas sur
   le script — donc le défaut se reproduisait à chaque création. Corrigé le 2026-08-03.
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

BASE = "https://zenodo.org/api"

# Identité auteur — DOIT correspondre à ORCID dans zenodo_audit_complet.py.
ORCID = "0009-0002-1794-4895"
# Affiliation ajoutee le 2026-10-04 : les records publies la portent (AWP-08), le generateur non.
CREATORS = [{"name": "Lalut, Stéphane", "affiliation": "Independent Researcher", "orcid": ORCID}]
COMMUNITY = "anthropie-working-papers"

TITLE = ("La réversibilité sociale comme dimension de l'inégalité — "
         "Repli, mémoire institutionnelle et agenda de mesure "
         "(Anthropie Working Paper No. 8)")

DESCRIPTION = (
    "<p>Working paper de cadre et d'agenda (série <em>Anthropie Working Papers</em>, "
    "AWP-08). L'inégalité est usuellement mesurée en niveaux et positions observés à une "
    "date (patrimoine, revenu courant, diplômes) et en trajectoires (mobilité) ; elle ne "
    "l'est presque jamais en <strong>réversibilité</strong> — la capacité, évaluée avant une "
    "tentative donnée, d'en supporter l'échec sans fermeture durable des options. Le paper "
    "définit la réversibilité comme un profil conditionnel d'options récupérables, articule "
    "deux fonctions (capacité de repli, régime de réadmission), sépare tarif institutionnel, "
    "capacité individuelle et conditions d'accès, et formule quatre prédictions "
    "pré-spécifiées — dont une hypothèse propre de non-séparabilité entre repli et mémoire "
    "institutionnelle de l'échec, dont le signe et la forme dépendent de la contournabilité "
    "de la porte de réadmission. Quatre terrains français de quasi-expériences sont "
    "spécifiés (loi Lemoine 2022, suppression de l'indicateur 040 en 2013, garantie Visale, "
    "non-recours), avec stratégie d'accès aux données et critères de réfutation par claim.</p>"
)

KEYWORDS = ["réversibilité sociale", "inégalité", "seconde chance", "mémoire institutionnelle",
            "droit à l'oubli", "quasi-expérience"]


def token() -> str:
    # Même source que les autres scripts Zenodo du dépôt : la variable d'environnement
    # utilisateur. L'ancien fichier `_secrets/zenodo_token.txt` n'existait plus sous D:\PRO.
    t = (os.environ.get("ZENODO_TOKEN") or "").strip()
    if not t:
        sys.exit("ERREUR : variable ZENODO_TOKEN absente")
    return t


def auth_headers(extra: dict) -> dict:
    # Jeton en en-tête, jamais dans l'URL (une URL finit dans les journaux et les messages d'erreur).
    return {**extra, "Authorization": f"Bearer {token()}"}


def api(method: str, path: str, payload=None):
    url = f"{BASE}{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers=auth_headers({"Content-Type": "application/json"}))
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"HTTP {e.code} sur {method} {path} : {body[:800]}")


def cmd_list():
    rows = api("GET", "/deposit/depositions?status=draft&size=50")
    if not rows:
        print("Aucun brouillon.")
        return
    for d in rows:
        print(f"- id={d['id']}  titre={d.get('title') or d.get('metadata', {}).get('title', '(sans titre)')!r}")


def cmd_mirror(rec_id: str):
    rec = api("GET", f"/records/{rec_id}")
    md = rec.get("metadata", {})
    print("licence :", md.get("license", {}))
    print("communautés :", [c for c in md.get("communities", [])])
    print("type :", md.get("resource_type", {}))
    print("langue :", md.get("language"))


def cmd_create(apply: bool):
    # anti-doublon
    for d in api("GET", "/deposit/depositions?status=draft&size=50") or []:
        t = d.get("title") or d.get("metadata", {}).get("title", "")
        if "AWP-08" in t or "Anthropie Working Paper No. 8" in t or "réversibilité sociale" in t.lower():
            sys.exit(f"REFUS anti-doublon : un brouillon existe déjà (id={d['id']}, titre={t!r}). "
                     f"Cibler ce brouillon, ne pas en créer un autre.")
    payload = {
        "metadata": {
            "title": TITLE,
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": DESCRIPTION,
            "creators": CREATORS,
            "language": "fra",
            "license": "cc-by-4.0",
            "keywords": KEYWORDS,
            "communities": [{"identifier": COMMUNITY}],
            "prereserve_doi": True,
            "version": "1.0",
            "related_identifiers": [
                {"identifier": "10.5281/zenodo.19266862", "relation": "references", "scheme": "doi"},
                {"identifier": "10.5281/zenodo.21200286", "relation": "references", "scheme": "doi"},
            ],
        }
    }
    if not apply:
        print("DRY-RUN — payload qui serait envoyé :")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    dep = api("POST", "/deposit/depositions", payload)
    doi = dep.get("metadata", {}).get("prereserve_doi", {}).get("doi", "(non retourné)")
    print("BROUILLON CRÉÉ (non publié).")
    print("deposition_id :", dep.get("id"))
    print("DOI réservé   :", doi)
    print("Édition web   :", dep.get("links", {}).get("html", ""))


TITLE_EN = ("Social Reversibility as a Dimension of Inequality — "
            "Fallback, Institutional Memory, and a Measurement Agenda "
            "(Anthropie Working Paper No. 8)")

DESCRIPTION_EN = (
    "<p>Framework-and-agenda working paper (<em>Anthropie Working Papers</em> series, AWP-08; "
    "English edition of the French original, DOI 10.5281/zenodo.21506320). Inequality is "
    "usually measured through levels and positions observed at a date (wealth, current "
    "income, credentials) and through trajectories (mobility); it is almost never measured "
    "through <strong>social reversibility</strong> — the capacity, assessed before a given "
    "attempt, to withstand its failure without a lasting closure of options. The paper "
    "defines reversibility as a conditional profile of recoverable options, articulates two "
    "functions (fallback capacity, readmission regime), separates the institutional tariff "
    "of failure, individual capacity, and access conditions, and states four pre-specified "
    "families of predictions — including a distinctive non-separability hypothesis between "
    "fallback and the institutional memory of failure, whose sign and shape depend on the "
    "circumventability of the readmission gate. Four French quasi-experimental settings are "
    "specified (the 2022 Lemoine Act, the 2013 removal of the 040 indicator, the Visale "
    "guarantee, non-take-up), with a data-access strategy and claim-by-claim refutation "
    "criteria.</p>"
)

KEYWORDS_EN = ["social reversibility", "inequality", "second chance", "institutional memory",
               "right to be forgotten", "quasi-experiment"]


def cmd_create_en(apply: bool):
    for d in api("GET", "/deposit/depositions?status=draft&size=50") or []:
        t = d.get("title") or d.get("metadata", {}).get("title", "")
        if "Social Reversibility" in t:
            sys.exit(f"REFUS anti-doublon : brouillon EN existant (id={d['id']}, titre={t!r}).")
    payload = {
        "metadata": {
            "title": TITLE_EN,
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": DESCRIPTION_EN,
            "creators": CREATORS,
            "language": "eng",
            "license": "cc-by-4.0",
            "keywords": KEYWORDS_EN,
            "communities": [{"identifier": COMMUNITY}],
            "prereserve_doi": True,
            "version": "1.0",
            "related_identifiers": [
                {"identifier": "10.5281/zenodo.21506320", "relation": "isDerivedFrom", "scheme": "doi"},
                {"identifier": "10.5281/zenodo.19431208", "relation": "references", "scheme": "doi"},
                {"identifier": "10.5281/zenodo.21200288", "relation": "references", "scheme": "doi"},
            ],
        }
    }
    if not apply:
        print("DRY-RUN — payload EN :")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    dep = api("POST", "/deposit/depositions", payload)
    doi = dep.get("metadata", {}).get("prereserve_doi", {}).get("doi", "(non retourné)")
    print("BROUILLON EN CRÉÉ (non publié).")
    print("deposition_id :", dep.get("id"))
    print("DOI réservé   :", doi)



# ---------------------------------------------------------------------------
# AWP-01 → espagnol (pilote ES-00). Traduction de l'original français
# 10.5281/zenodo.19266862. Version espagnole révisée par l'auteur : le § 1.1
# porte une précision terminologique absente du français, sur l'usage de
# « antropía » dans la réception hispanophone de Bernard Stiegler.
# ---------------------------------------------------------------------------

TITLE_ES = ("¿Qué es la antropía? Principios de una hipótesis "
            "(Anthropie Working Paper n.º 1)")

DESCRIPTION_ES = (
    "<p>Texto fundacional de la serie <em>Anthropie Working Papers</em> (AWP-01; "
    "edición española del original francés, DOI 10.5281/zenodo.19266862). La antropía "
    "es la hipótesis según la cual todo orden social local se construye exportando su "
    "desorden hacia otros lugares, otros tiempos u otros grupos sociales: "
    "<strong>los sistemas sociales desplazan el desorden en lugar de resolverlo</strong>. "
    "El artículo sostiene que ese desplazamiento —espacial (del centro a la periferia), "
    "temporal (deuda y traslado de los costes a las generaciones futuras) y social "
    "(transferencia de las cargas a los grupos cautivos)— constituye un mecanismo "
    "estructural observable en toda configuración de orden estable, y no un accidente "
    "de mercado reducible a la noción de externalidad. En diálogo con la termodinámica "
    "económica (Georgescu-Roegen), la teoría de sistemas (Luhmann), la ecología-mundo "
    "(Moore), la antropología de la deuda (Graeber) y la sociología del riesgo (Beck), "
    "construye una matriz unificada de análisis de los costes desplazados, "
    "operacionalizable mediante tres preguntas: quién crea el orden, quién absorbe el "
    "desorden y qué mecanismo vuelve invisible esa transferencia.</p>"
    "<p><em>Versión española revisada por el autor. Esta versión incorpora en el § 1.1 "
    "una aclaración terminológica específica relativa al uso de «antropía» en la "
    "recepción hispanohablante de Bernard Stiegler.</em></p>"
)

KEYWORDS_ES = ["antropía", "entropía social", "transferencia de desorden",
               "costes desplazados", "hipótesis"]


# Registre des fiches. Une entrée = un dépôt possible.
#   marqueurs : chaînes qui déclenchent le refus anti-doublon sur les brouillons.
PAPERS = {
    "awp01-es": {
        "titre": TITLE_ES,
        "description": DESCRIPTION_ES,
        "keywords": KEYWORDS_ES,
        "language": "spa",
        "marqueurs": ["¿Qué es la antropía?", "Anthropie Working Paper n.º 1"],
        # Provenance explicite. La distinction version/concept est portée ici parce
        # qu'elle a déjà induit une erreur : le P0 avait étiqueté 19266862 « concept »
        # alors que c'est le DOI DE VERSION (le concept est 19266861).
        # Gate exécutée le 2026-08-03 : le PDF scellé (103 757 o, sha256 824b8464…)
        # a le même md5 que le fichier du record 19266862 — ce38… → MATCH.
        "source": {
            "version_doi": "10.5281/zenodo.19266862",
            "concept_doi": "10.5281/zenodo.19266861",
            "sha256": "824b84642ef132dae8c0c82ed32ce3415224a72cf822259448b28001f1e25aba",
            "md5": "ce313be7f3c0e740f7670315b96893c9",
            "fichier": "AWP-01_anthropie_principes_hypothese.pdf",
        },
        "related": [
            # L'original français dont cette version dérive. Cible = DOI de VERSION,
            # pas le concept : la traduction dérive d'un fichier précis, pas d'un ensemble.
            {"identifier": "10.5281/zenodo.19266862", "relation": "isDerivedFrom", "scheme": "doi"},
            # ⚠ AUCUNE relation vers la version anglaise. « references » signifie en
            # DataCite que la ressource citée a servi de source d'information. Or la
            # doctrine de ce chantier pose que l'anglais est un CONTRÔLE CROISÉ, jamais
            # une source. La déclarer contredirait la génétique réelle du texte.
            # ES et EN pointent chacun séparément vers le français : la parenté se
            # reconstruit sans relation directe entre les deux traductions.
            # (« isTranslationOf » existe dans DataCite 4.7 mais n'est pas encore
            #  documenté comme accepté par l'API de dépôt Zenodo — ne pas l'inventer.)
        ],
        # ⚠ isDescribedBy vers la page du site : ABSENT volontairement.
        # Le site ne déclare que fr et en (config/_default/hugo.toml) ; il n'existe
        # pas de /es/awp/awp-01/. L'audit signalera ce trou tant que la décision
        # d'ajouter l'espagnol au site n'est pas prise. Ne pas pointer vers la page
        # française : ce serait déclarer que ce dépôt est décrit par un texte
        # qui n'est pas le sien.
    },
    "awp09-fr": {
        "titre": ("Ce que les comptes publics permettent d'établir sur le déplacement de la charge de la dette — "
                  "Identités comptables, témoins indépendants et limites (France, 1995-2025) "
                  "(Anthropie Working Paper No. 9)"),
        "description": "<p>L'anthropie est l'hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent.</p><p>Working paper de méthode et de résultats datés (série <em>Anthropie Working Papers</em>, AWP-09). La dette publique déplace une charge\xa0: dans le temps, vers les générations suivantes, entre ménages, entre pays et entre échelons d'administration. Ce document de travail établit ce que les comptes publics permettent, ou non, d'affirmer sur chacun de ces déplacements, en France de 1995 à 2025. Sa méthode tient en une règle\xa0: les ratios d'une décomposition sont contrôlés par un témoin que le calcul n'utilise pas, vérifié par l'algèbre puis vu rejeter une erreur réelle, son partage par la reproduction d'autres producteurs, et toute lecture installée est testée là où elle devrait échouer. D'où trois apports. Le premier rapproche des lectures publiques contradictoires\xa0: l'effet des intérêts nets de la croissance pèse 43\xa0% de la hausse du ratio de 1996 à 2012 et retire 1,74 point par an depuis 2017\xa0; fenêtres et objets expliquent une grande part de leur écart. Le deuxième dresse un relevé daté\xa0: la hausse de 57,8\xa0% à 115,6\xa0% tient aux déficits primaires, comme l'a déjà établi la Cour des comptes\xa0; moins d'un cinquième des déficits depuis 1996 a correspondu à un accroissement net des actifs publics\xa0; plus de la moitié de la dette est détenue par des non-résidents\xa0; le sens de l'effort entre ménages s'inverse avec l'instrument. Le troisième met à l'épreuve une lecture antérieure (AWP-03), qui faisait de la dette un transfert vers les générations futures et les moins mobiles\xa0: elle n'est soutenue que dans un périmètre patrimonial sur l'héritage et comme mécanique comptable sur l'écart entre taux et croissance, et son asymétrie sociale est hors de portée des comptes.</p><p><em>Abstract.</em> French fiscal institutions now agree that primary deficits, not the interest-growth “snowball,” account for most of the rise in public debt. Yet public readings that attributed nearly 40% of that rise to the snowball, or more than half of the debt to accumulated interest, also rested on official accounts, and the disagreement has not been reconciled in published work. Nor does the debt ratio say who bears the burden, a question that interpretive frameworks, including an earlier paper in this series (AWP-03), have addressed through illustration rather than measurement. This paper asks what official accounts can and cannot establish about the displacement of the debt burden over time, toward later generations, across households, across countries, and across levels of government, in France from 1995 to 2025. It applies standard debt-dynamics identities under a verification rule: the ratios entering a decomposition are checked against an independent published benchmark, validated algebraically and then seen to reject an actual error, its split is checked against reproductions by other producers, and every established narrative is tested where it should fail. Windows and measures account for much of the conflict: the snowball accounts for 43% of the rise in 1996-2012 and has subtracted 1.74 points a year since 2017. Less than one-fifth of deficits since 1996 matched a net increase in recorded public assets; more than half of the debt is held by non-residents; and the household distribution of fiscal effort reverses with the instrument. Tested against them, the earlier framework is supported only within a narrow wealth perimeter on inheritance and as accounting mechanics on the interest-growth differential, while its social asymmetry lies beyond what the accounts can test.</p>",
        "keywords": ["anthropie", "dette publique", "dynamique de la dette", "générations futures",
                     "vérification des données", "working paper", "économie hétérodoxe", "sciences sociales",
                     "open access", "public debt", "debt dynamics", "heterodox economics", "social sciences",
                     "institutional analysis", "JEL:H63", "JEL:H62", "JEL:H72", "JEL:E62", "JEL:C82"],
        "language": "fra",
        "marqueurs": ["AWP-09", "Anthropie Working Paper No. 9", "permettent d'établir sur le déplacement"],
        "related": [
            {"identifier": "10.5281/zenodo.19268769", "relation": "references", "scheme": "doi"},   # AWP-03, mis a l'epreuve
            {"identifier": "10.5281/zenodo.19266862", "relation": "references", "scheme": "doi"},   # AWP-01, definition
            {"identifier": "https://stephane-lalut.com/awp/awp-09/", "relation": "isDescribedBy", "scheme": "url"},
            {"identifier": "https://stephane-lalut.com/pourquoi-la-dette-publique-augmente/",
             "relation": "isDerivedFrom", "scheme": "url"},   # jeux et generateurs du dossier dette
        ],
    },
    "awp09-en": {
        "titre": ("What Public Accounts Can Establish about the Displacement of the Public Debt Burden — "
                  "Accounting Identities, Independent Benchmarks, and Limits (France, 1995-2025) "
                  "(Anthropie Working Paper No. 9)"),
        "description": '<p>Anthropy is the hypothesis that social systems displace disorder rather than resolve it.</p><p>Methods-and-dated-results working paper (<em>Anthropie Working Papers</em> series, AWP-09; English edition of the French original, DOI 10.5281/zenodo.23143030). French fiscal institutions now agree that primary deficits, not the interest-growth “snowball,” account for most of the rise in public debt. Yet public readings that attributed nearly 40% of that rise to the snowball, or more than half of the debt to accumulated interest, also rested on official accounts, and the disagreement has not been reconciled in published work. Nor does the debt ratio say who bears the burden, a question that interpretive frameworks, including an earlier paper in this series (AWP-03), have addressed through illustration rather than measurement. This paper asks what official accounts can and cannot establish about the displacement of the debt burden over time, toward later generations, across households, across countries, and across levels of government, in France from 1995 to 2025. It applies standard debt-dynamics identities under a verification rule: the ratios entering a decomposition are checked against an independent published benchmark, validated algebraically and then seen to reject an actual error, its split is checked against reproductions by other producers, and every established narrative is tested where it should fail. Windows and measures account for much of the conflict: the snowball accounts for 43% of the rise in 1996-2012 and has subtracted 1.74 points a year since 2017. Less than one-fifth of deficits since 1996 matched a net increase in recorded public assets; more than half of the debt is held by non-residents; and the household distribution of fiscal effort reverses with the instrument. Tested against them, the earlier framework is supported only within a narrow balance-sheet scope on inheritance and as accounting mechanics on the interest-growth differential, while its social asymmetry lies beyond what the accounts can test.</p>',
        "keywords": ["anthropy", "public debt", "debt dynamics", "intergenerational burden", "data verification",
                     "working paper", "heterodox economics", "social sciences", "institutional analysis",
                     "open access", "JEL:H63", "JEL:H62", "JEL:H72", "JEL:E62", "JEL:C82"],
        "language": "eng",
        "marqueurs": ["What Public Accounts Can Establish"],  # le numero de serie seul reconnaitrait le depot FR (faux doublon constate le 04/10)
        "related": [
            {"identifier": "10.5281/zenodo.23143030", "relation": "isDerivedFrom", "scheme": "doi"},  # original francais
            {"identifier": "10.5281/zenodo.19434094", "relation": "references", "scheme": "doi"},   # AWP-03 EN
            {"identifier": "10.5281/zenodo.19431208", "relation": "references", "scheme": "doi"},   # AWP-01 EN
            {"identifier": "https://stephane-lalut.com/en/awp/awp-09/", "relation": "isDescribedBy", "scheme": "url"},
        ],
    },
}


def cmd_papers():
    print("Fiches disponibles :")
    for k, v in PAPERS.items():
        print(f"  {k:12} {v['language']}  {v['titre'][:70]}")


def cmd_create_paper(key: str, apply: bool):
    """Création générique à partir du registre PAPERS."""
    fiche = PAPERS.get(key)
    if fiche is None:
        sys.exit(f"Fiche inconnue : {key!r}. Disponibles : {', '.join(PAPERS)}")
    for d in api("GET", "/deposit/depositions?status=draft&size=50") or []:
        t = d.get("title") or d.get("metadata", {}).get("title", "")
        for marq in fiche["marqueurs"]:
            if marq in t:
                sys.exit(f"REFUS anti-doublon : brouillon existant (id={d['id']}, titre={t!r}). "
                         f"Cibler ce brouillon, ne pas en créer un autre.")
    payload = {
        "metadata": {
            "title": fiche["titre"],
            "upload_type": "publication",
            "publication_type": "workingpaper",
            "description": fiche["description"],
            "creators": CREATORS,
            "language": fiche["language"],
            "license": "cc-by-4.0",
            "keywords": fiche["keywords"],
            "communities": [{"identifier": COMMUNITY}],
            "prereserve_doi": True,
            "version": "1.0",
            "related_identifiers": fiche["related"],
        }
    }
    if not apply:
        print(f"DRY-RUN — payload {key} :")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    dep = api("POST", "/deposit/depositions", payload)
    doi = dep.get("metadata", {}).get("prereserve_doi", {}).get("doi", "(non retourné)")
    print(f"BROUILLON {key} CRÉÉ (NON publié).")
    print("deposition_id :", dep.get("id"))
    print("DOI réservé   :", doi)
    print("Édition web   :", dep.get("links", {}).get("html", ""))


# Jeux de données (upload_type « dataset »), ajouté le 2026-10-07 pour le dossier « Promesses présidentielles »
# (décision D1 de l'arbitrage PRO-20261007-102607). Pas de communauté : `anthropie-working-papers` réunit les working
# papers, un jeu de données n'y a pas sa place (choix délégué par l'auteur le 07/10). Fichiers et note de méthode :
# D:\PRO\06_PROMOTION\RECHERCHE_DOSSIER_PROMESSES_2026-10-05\DEPOT_DONNEES\ (note_methode.py les tire du dépôt git,
# identiques au site octet pour octet).
_PAGES_PROMESSES = ["pouvoirs-du-president-de-la-republique", "qui-peut-faire-adopter-une-loi",
                    "une-loi-votee-s-applique-t-elle-tout-de-suite",
                    "une-promesse-peut-elle-produire-ses-effets-en-cinq-ans",
                    "comment-savoir-si-une-promesse-est-tenue", "un-president-peut-il-recourir-au-referendum",
                    "ce-que-la-france-peut-decider-dans-l-union-europeenne"]
DATASETS = {
    "promesses-2026-10": {
        "marqueurs": ["sept jeux de données vérifiés sur les institutions françaises"],
        "titre": ("Ce qu'un président peut décider, faire voter, faire appliquer et mesurer : sept jeux de données "
                  "vérifiés sur les institutions françaises (version du 7 octobre 2026)"),
        "language": "fra",
        "version": "2026-10-07",
        "description": (
            "<p>Sept jeux de données sur le chemin d'une promesse présidentielle en France : les huit dispositions que "
            "l'article 19 de la Constitution dispense de contreseing ; l'origine de chaque loi promulguée depuis 2012 et "
            "le sort des propositions de loi déposées ; l'état des mesures d'application ; la durée de formation des "
            "médecins ; le croisement du chômage au sens du BIT et des inscrits en catégorie A ; le registre des "
            "référendums nationaux et des référendums d'initiative partagée ; les votes publics de chaque État au "
            "Conseil de l'Union européenne sur les actes législatifs (2009-2026).</p>"
            "<p>Chaque jeu est produit par un script unique qui relit les sources officielles archivées, refuse d'écrire "
            "si une donnée cesse de soutenir une phrase publiée, et est contrôlé par un témoin indépendant lorsqu'un témoin comparable existe ; sinon, la page le dit et décrit les contrôles de cohérence appliqués. Aucun nombre "
            "n'est saisi à la main. Chaque jeu accompagne une page publique de stephane-lalut.com, qui en donne la "
            "lecture, les limites et les sources ; la note de méthode jointe décrit sources, témoins, limites et "
            "empreintes SHA-256 des fichiers.</p>"
            "<p><em>Seven verified datasets on what a French president can decide, get passed, get implemented and "
            "measure: the eight provisions exempt from countersignature (art. 19), the origin of every law promulgated "
            "since 2012 and the fate of bills tabled, the status of implementing measures, the length of medical "
            "training, the overlap between ILO unemployment and registered jobseekers, the register of national and "
            "shared-initiative referendums, and the public votes of each Member State in the Council of the EU on "
            "legislative acts (2009-2026). Each dataset is produced by a single script that rereads archived official "
            "sources and is checked against an independent witness where a comparable one exists; where none exists, the page says so and describes the consistency checks applied.</em></p>"),
        "keywords": ["Constitution française", "contreseing", "procédure législative", "article 49.3",
                     "application des lois", "référendum", "référendum d'initiative partagée",
                     "Conseil de l'Union européenne", "votes au Conseil", "promesses électorales", "chômage BIT",
                     "formation des médecins"],
        "related": ([{"relation": "isSupplementTo", "identifier": f"https://stephane-lalut.com/{p}/",
                      "resource_type": "publication-other"} for p in _PAGES_PROMESSES]
                    + [{"relation": "references", "identifier": "10.7802/2560", "scheme": "doi"}]),
    },
}


def cmd_create_dataset(key: str, apply: bool):
    """Brouillon de jeu de données + réservation du DOI. Jamais de publication par script."""
    fiche = DATASETS.get(key)
    if fiche is None:
        sys.exit(f"Jeu inconnu : {key!r}. Disponibles : {', '.join(DATASETS)}")
    for d in api("GET", "/deposit/depositions?status=draft&size=50") or []:
        t = d.get("title") or d.get("metadata", {}).get("title", "")
        if any(m in t for m in fiche["marqueurs"]):
            sys.exit(f"REFUS anti-doublon : brouillon existant (id={d['id']}, titre={t!r}).")
    payload = {"metadata": {
        "title": fiche["titre"], "upload_type": "dataset", "description": fiche["description"],
        "creators": CREATORS, "language": fiche["language"], "license": "cc-by-4.0", "keywords": fiche["keywords"],
        "prereserve_doi": True, "version": fiche["version"], "related_identifiers": fiche["related"],
    }}
    if not apply:
        print(f"DRY-RUN — payload {key} :")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    dep = api("POST", "/deposit/depositions", payload)
    doi = dep.get("metadata", {}).get("prereserve_doi", {}).get("doi", "(non retourné)")
    print(f"BROUILLON {key} CRÉÉ (NON publié).")
    print("deposition_id :", dep.get("id"))
    print("DOI réservé   :", doi)
    print("Édition web   :", dep.get("links", {}).get("html", ""))


def cmd_upload(dep_id: str, filepath: str):
    fp = Path(filepath)
    if not fp.is_file():
        sys.exit(f"Fichier introuvable : {fp}")
    dep = api("GET", f"/deposit/depositions/{dep_id}")
    bucket = dep.get("links", {}).get("bucket")
    if not bucket:
        sys.exit("Pas de lien bucket sur cette deposition.")
    url = f"{bucket}/{fp.name}"
    data = fp.read_bytes()
    req = urllib.request.Request(url, data=data, method="PUT",
                                 headers=auth_headers({"Content-Type": "application/octet-stream"}))
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            info = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} upload : {e.read().decode('utf-8', errors='replace')[:500]}")
    print(f"UPLOAD OK : {info.get('key')}  taille={info.get('size')}  checksum={info.get('checksum')}")
    print("(Brouillon toujours NON publié.)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--list", action="store_true")
    p.add_argument("--mirror", metavar="RECORD_ID")
    p.add_argument("--papers", action="store_true", help="liste les fiches du registre")
    p.add_argument("--create", metavar="FICHE", nargs="?", const="", help="ex. awp01-es")
    p.add_argument("--create-awp08-fr", action="store_true",
                   help="alias historique (fiche AWP-08 FR codée en dur)")
    p.add_argument("--create-en", action="store_true",
                   help="alias historique (fiche AWP-08 EN codée en dur)")
    p.add_argument("--upload", nargs=2, metavar=("DEPOSITION_ID", "FILEPATH"))
    p.add_argument("--create-dataset", metavar="JEU", help="ex. promesses-2026-10 (registre DATASETS)")
    p.add_argument("--apply", action="store_true")
    a = p.parse_args()
    if a.create_dataset:
        cmd_create_dataset(a.create_dataset, a.apply)
    elif a.list:
        cmd_list()
    elif a.papers:
        cmd_papers()
    elif a.mirror:
        cmd_mirror(a.mirror)
    elif a.create is not None and a.create != "":
        cmd_create_paper(a.create, a.apply)
    elif a.create == "":
        sys.exit("--create attend une fiche. Voir : python zenodo_deposit.py --papers")
    elif a.create_awp08_fr:
        cmd_create(a.apply)
    elif a.create_en:
        cmd_create_en(a.apply)
    elif a.upload:
        cmd_upload(a.upload[0], a.upload[1])
    else:
        p.print_help()
