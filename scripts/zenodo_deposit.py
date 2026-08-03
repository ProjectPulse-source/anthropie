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
import sys
import urllib.request
import urllib.error
from pathlib import Path

TOKEN_FILE = Path(r"D:\anthropie\_secrets\zenodo_token.txt")
BASE = "https://zenodo.org/api"

# Identité auteur — DOIT correspondre à ORCID dans zenodo_audit_complet.py.
ORCID = "0009-0002-1794-4895"
CREATORS = [{"name": "Lalut, Stéphane", "orcid": ORCID}]
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
    t = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not t:
        sys.exit("Token vide.")
    return t


def api(method: str, path: str, payload=None):
    url = f"{BASE}{path}"
    sep = "&" if "?" in url else "?"
    url = f"{url}{sep}access_token={token()}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
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


def cmd_upload(dep_id: str, filepath: str):
    fp = Path(filepath)
    if not fp.is_file():
        sys.exit(f"Fichier introuvable : {fp}")
    dep = api("GET", f"/deposit/depositions/{dep_id}")
    bucket = dep.get("links", {}).get("bucket")
    if not bucket:
        sys.exit("Pas de lien bucket sur cette deposition.")
    url = f"{bucket}/{fp.name}?access_token={token()}"
    data = fp.read_bytes()
    req = urllib.request.Request(url, data=data, method="PUT",
                                 headers={"Content-Type": "application/octet-stream"})
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
    p.add_argument("--apply", action="store_true")
    a = p.parse_args()
    if a.list:
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
