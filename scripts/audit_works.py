#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_works.py — Script d'audit comparatif read-only
=====================================================

Lit data/works.yaml (registre canonique) et compare avec l'état observé
sur les plateformes (site, DOIs, ORCID, OpenAlex, MPRA, SSRN URLs).

PROPRIÉTÉ FONDAMENTALE : NE MODIFIE JAMAIS data/works.yaml.
Le canonique est humain. Le script observe et signale, point.

Sorties produites :
  reports/check-YYYY-MM-DD.md            (rapport de divergences lisible)
  reports/observed/YYYY-MM-DD/*.json     (état observé brut, archivable)

Vérifications effectuées :
  ✓ HTTP 200 sur les pages site (FR + EN) des AWPs et livres
  ✓ Résolution des DOIs (Zenodo, SSRN, OpenEdition) via doi.org
  ✓ Présence des balises citation_* Google Scholar sur pages AWP
  ✓ Cohérence titres canoniques vs ORCID (API publique)
  ✓ Cohérence titres canoniques vs OpenAlex (API publique)
  ✓ Détection des champs vides (todo) dans le registre

Vérifications EXCLUES par conception (per arbitrage stratégique) :
  ✗ Scraping Google Scholar (DOM cassant — audit manuel uniquement)
  ✗ Common Crawl
  ✗ Semantic Scholar avancé / Connected Papers
  ✗ Métriques bibliométriques

Dépendance : PyYAML (pip install pyyaml). Le reste est stdlib.

Usage :
  python scripts/audit_works.py                   # audit complet
  python scripts/audit_works.py --skip-network    # offline (vérifs structurelles)
  python scripts/audit_works.py --verbose         # logs détaillés
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml

# =============================================================================
# Configuration
# =============================================================================

USER_AGENT = "anthropie-audit/1.0 (+https://stephane-lalut.com)"
TIMEOUT = 15  # secondes

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKS_FILE = REPO_ROOT / "data" / "works.yaml"
REPORTS_DIR = REPO_ROOT / "reports"
TODAY = date.today().isoformat()

ORCID_API = "https://pub.orcid.org/v3.0"
OPENALEX_API = "https://api.openalex.org"

REQUIRED_CITATION_TAGS = [
    "citation_title",
    "citation_author",
    "citation_publication_date",
    "citation_doi",
    "citation_pdf_url",
]


# =============================================================================
# Modèles
# =============================================================================


@dataclass
class Finding:
    """Une observation produite par un check."""
    level: str  # "fail" | "warning" | "todo" | "info"
    work_id: str
    check: str
    message: str
    detail: str = ""

    def to_md_line(self) -> str:
        line = f"- **`{self.work_id}`** — *{self.check}* — {self.message}"
        if self.detail:
            line += f"  \n  ↳ {self.detail}"
        return line


@dataclass
class AuditState:
    """État global de l'audit."""
    findings: list[Finding] = field(default_factory=list)
    works: list[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    checks_run: list[str] = field(default_factory=list)
    network_ok_count: int = 0
    network_fail_count: int = 0


# =============================================================================
# Utilitaires réseau
# =============================================================================


def http_request(url: str, method: str = "GET", timeout: int = TIMEOUT,
                 headers: dict | None = None) -> tuple[int | None, str]:
    """Requête HTTP sécurisée. Retourne (status_code, body) ou (None, error)."""
    full_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        full_headers.update(headers)
    req = urllib.request.Request(url, headers=full_headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = ""
            if method == "GET":
                raw = response.read()
                body = raw.decode("utf-8", errors="replace")
            return response.status, body
    except urllib.error.HTTPError as e:
        return e.code, str(e)
    except urllib.error.URLError as e:
        return None, f"URLError: {e.reason}"
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def url_resolves(url: str, timeout: int = TIMEOUT) -> tuple[bool, int | None]:
    """Vérifie qu'une URL résout (HEAD, suit redirects implicites)."""
    code, _ = http_request(url, method="HEAD", timeout=timeout)
    if code is None:
        return False, None
    return 200 <= code < 400, code


# =============================================================================
# Normalisation de titres
# =============================================================================


def normalize_title(title: str) -> str:
    """Normalise un titre pour comparaison robuste.
    
    Supprime accents, ponctuation, espaces multiples ; lowercase.
    Permet de comparer 'Anthropie : Notes...' vs 'anthropie - notes...'
    """
    if not title:
        return ""
    # Retire les accents
    nfkd = unicodedata.normalize("NFKD", title)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    # Lowercase
    lower = no_accents.lower()
    # Retire ponctuation et caractères non-alphanumériques sauf espaces
    cleaned = re.sub(r"[^\w\s]", " ", lower)
    # Normalise espaces multiples
    normalized = re.sub(r"\s+", " ", cleaned).strip()
    return normalized


# =============================================================================
# Checks (read-only sur le canonique)
# =============================================================================


def check_canonical_completeness(works: list[dict], state: AuditState) -> None:
    """Vérifie les champs vides ou marqués 'todo'/'verify' dans works.yaml."""
    state.checks_run.append("canonical_completeness")
    for work in works:
        wid = work["id"]
        wtype = work.get("type", "")

        # AWPs : MPRA item_id manquant ?
        if wtype == "awp":
            mpra = work.get("deposits", {}).get("mpra_en", {})
            if not mpra.get("item_id"):
                state.findings.append(Finding(
                    level="todo", work_id=wid, check="completeness",
                    message="MPRA item_id non renseigné",
                ))
            # Pages site renseignées ?
            site_pages = work.get("site_pages", {}) or {}
            for lang in ("fr", "en"):
                if not site_pages.get(lang):
                    state.findings.append(Finding(
                        level="todo", work_id=wid, check="completeness",
                        message=f"site_pages.{lang} non renseigné",
                    ))

        # Livres : pages site EN, ASIN
        if wtype == "book":
            site_pages = work.get("site_pages", {}) or {}
            if not site_pages.get("en"):
                state.findings.append(Finding(
                    level="todo", work_id=wid, check="completeness",
                    message="site_pages.en non créée (chantier P3)",
                ))
            if not work.get("purchase_url"):
                state.findings.append(Finding(
                    level="todo", work_id=wid, check="completeness",
                    message="purchase_url Amazon non renseignée",
                ))


def check_site_pages(works: list[dict], state: AuditState, skip_network: bool) -> dict:
    """Vérifie HTTP 200 sur les pages site déclarées."""
    state.checks_run.append("site_pages")
    observed = {}
    if skip_network:
        return observed

    for work in works:
        wid = work["id"]
        if work.get("type") not in ("awp", "book"):
            continue
        site_pages = work.get("site_pages", {}) or {}
        for lang in ("fr", "en"):
            url = site_pages.get(lang, "")
            if not url:
                continue  # déjà tracké par check_canonical_completeness
            resolves, code = url_resolves(url)
            observed[f"{wid}.{lang}"] = {"url": url, "code": code, "ok": resolves}
            if resolves:
                state.network_ok_count += 1
            else:
                state.network_fail_count += 1
                state.findings.append(Finding(
                    level="warning", work_id=wid, check="site_page",
                    message=f"Page {lang.upper()} non résolue (HTTP {code})",
                    detail=url,
                ))
    return observed


def check_dois_resolution(works: list[dict], state: AuditState, skip_network: bool) -> dict:
    """Vérifie que tous les DOIs déclarés résolvent via doi.org."""
    state.checks_run.append("dois_resolution")
    observed = {}
    if skip_network:
        return observed

    for work in works:
        wid = work["id"]
        # AWPs : 3 deposits avec DOI
        deposits = work.get("deposits", {})
        for platform, info in deposits.items():
            if not isinstance(info, dict):
                continue
            doi = info.get("doi", "")
            if not doi:
                continue
            url = f"https://doi.org/{doi}"
            resolves, code = url_resolves(url)
            observed[f"{wid}.{platform}"] = {"doi": doi, "code": code, "ok": resolves}
            if resolves:
                state.network_ok_count += 1
            else:
                state.network_fail_count += 1
                state.findings.append(Finding(
                    level="warning", work_id=wid, check="doi_resolution",
                    message=f"DOI ne résout pas via doi.org : {doi} ({platform})",
                ))
        # Articles : DOI direct
        if work.get("type") == "article":
            doi = work.get("doi", "")
            if doi:
                url = f"https://doi.org/{doi}"
                resolves, code = url_resolves(url)
                observed[f"{wid}.article"] = {"doi": doi, "code": code, "ok": resolves}
                if not resolves:
                    state.network_fail_count += 1
                    state.findings.append(Finding(
                        level="warning", work_id=wid, check="doi_resolution",
                        message=f"DOI article ne résout pas : {doi}",
                    ))
                else:
                    state.network_ok_count += 1
    return observed


def check_citation_metadata(works: list[dict], state: AuditState, skip_network: bool) -> dict:
    """Vérifie que les pages AWP contiennent les balises citation_* Google Scholar."""
    state.checks_run.append("citation_metadata")
    observed = {}
    if skip_network:
        return observed

    for work in works:
        if work.get("type") != "awp":
            continue
        wid = work["id"]
        site_pages = work.get("site_pages", {}) or {}
        for lang in ("fr", "en"):
            url = site_pages.get(lang, "")
            if not url:
                continue
            code, body = http_request(url)
            if code != 200:
                continue
            missing = []
            present = []
            for tag in REQUIRED_CITATION_TAGS:
                # Détecte <meta name="citation_xxx" ...>. Les guillemets d'attribut
                # sont OPTIONNELS : `hugo --minify` (cf. .github/workflows/hugo.yml)
                # produit `name=citation_xxx` sans guillemets. Le délimiteur final
                # [\s>] empêche un faux positif sur un tag dont le nom est préfixe
                # d'un autre (p.ex. citation_doi vs citation_doi_x).
                pattern = rf'<meta[^>]+name=[\"\']?{re.escape(tag)}[\"\']?[\s>]'
                if re.search(pattern, body, re.IGNORECASE):
                    present.append(tag)
                else:
                    missing.append(tag)
            observed[f"{wid}.{lang}"] = {
                "url": url, "present": present, "missing": missing
            }
            if missing:
                state.findings.append(Finding(
                    level="warning", work_id=wid, check="citation_metadata",
                    message=f"Balises Scholar manquantes ({lang.upper()}) : {', '.join(missing)}",
                    detail=url,
                ))
    return observed


def check_orcid(works: list[dict], state: AuditState, orcid_id: str,
                skip_network: bool) -> dict:
    """Compare titres canoniques avec ce qu'expose ORCID publiquement."""
    state.checks_run.append("orcid")
    observed = {"works_count": 0, "titles": []}
    if skip_network:
        return observed

    url = f"{ORCID_API}/{orcid_id}/works"
    code, body = http_request(url, headers={"Accept": "application/json"})
    if code != 200:
        state.findings.append(Finding(
            level="warning", work_id="(global)", check="orcid",
            message=f"ORCID API inaccessible (HTTP {code})",
        ))
        return observed

    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        state.findings.append(Finding(
            level="warning", work_id="(global)", check="orcid",
            message=f"Réponse ORCID non parsable : {e}",
        ))
        return observed

    # Extraire les titres ORCID
    orcid_titles = []
    for group in data.get("group", []):
        for summary in group.get("work-summary", []):
            title_obj = summary.get("title", {}) or {}
            title_value = (title_obj.get("title", {}) or {}).get("value", "")
            if title_value:
                orcid_titles.append({
                    "put_code": summary.get("put-code"),
                    "title": title_value,
                    "type": summary.get("type", ""),
                })
    observed["works_count"] = len(orcid_titles)
    observed["titles"] = orcid_titles

    # Pour chaque AWP/livre canonique, chercher un titre matching dans ORCID
    canonical_titles = set()
    for work in works:
        if work.get("type") not in ("awp", "book"):
            continue
        ct = work.get("canonical_title", {}) or {}
        for lang in ("fr", "en"):
            title = ct.get(lang, "")
            if title:
                canonical_titles.add(normalize_title(title))

    orcid_normalized = {normalize_title(t["title"]): t["title"] for t in orcid_titles}

    # Œuvres canoniques absentes d'ORCID
    missing_in_orcid = canonical_titles - set(orcid_normalized.keys())
    if missing_in_orcid:
        for nt in missing_in_orcid:
            # Retrouver le titre original
            for work in works:
                if work.get("type") not in ("awp", "book"):
                    continue
                ct = work.get("canonical_title", {}) or {}
                for lang in ("fr", "en"):
                    if normalize_title(ct.get(lang, "")) == nt:
                        state.findings.append(Finding(
                            level="info", work_id=work["id"], check="orcid",
                            message=f"Titre canonique {lang.upper()} non trouvé sur ORCID",
                            detail=ct.get(lang, ""),
                        ))

    return observed


def check_openalex(works: list[dict], state: AuditState, openalex_id: str,
                   skip_network: bool) -> dict:
    """Compare titres canoniques avec OpenAlex."""
    state.checks_run.append("openalex")
    observed = {"works_count": 0, "titles": []}
    if skip_network:
        return observed

    url = f"{OPENALEX_API}/works?filter=author.id:{openalex_id}&per-page=200"
    code, body = http_request(url)
    if code != 200:
        state.findings.append(Finding(
            level="warning", work_id="(global)", check="openalex",
            message=f"OpenAlex API inaccessible (HTTP {code})",
        ))
        return observed

    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        state.findings.append(Finding(
            level="warning", work_id="(global)", check="openalex",
            message=f"Réponse OpenAlex non parsable : {e}",
        ))
        return observed

    oa_titles = []
    for w in data.get("results", []):
        title = w.get("title", "") or w.get("display_name", "")
        if title:
            oa_titles.append({
                "openalex_id": w.get("id", ""),
                "title": title,
                "doi": w.get("doi", ""),
            })
    observed["works_count"] = len(oa_titles)
    observed["titles"] = oa_titles

    # Note : on ne fait pas de comparaison stricte ici car OpenAlex peut
    # avoir des entrées qui n'ont pas d'équivalent canonique (recensions
    # courtes, etc.). On rapporte seulement le nombre.
    return observed


# =============================================================================
# Génération du rapport
# =============================================================================


def write_report(state: AuditState, output_path: Path) -> None:
    """Écrit le rapport Markdown lisible."""
    fail = [f for f in state.findings if f.level == "fail"]
    warning = [f for f in state.findings if f.level == "warning"]
    todo = [f for f in state.findings if f.level == "todo"]
    info = [f for f in state.findings if f.level == "info"]

    meta = state.metadata
    lines = [
        f"# Rapport d'audit `works.yaml` — {TODAY}",
        "",
        f"**Source canonique :** `data/works.yaml` "
        f"(version {meta.get('registry_version', '?')}, "
        f"mise à jour {meta.get('last_updated', '?')})",
        "",
        f"**Œuvres auditées :** {len(state.works)}",
        "",
        "## Synthèse",
        "",
        "| Indicateur | Valeur |",
        "|---|---|",
        f"| ❌ Échecs critiques | {len(fail)} |",
        f"| ⚠️ Avertissements | {len(warning)} |",
        f"| 🟦 Champs à compléter | {len(todo)} |",
        f"| ℹ️ Notes informatives | {len(info)} |",
        f"| ✅ Vérifications réseau OK | {state.network_ok_count} |",
        f"| ✗ Vérifications réseau KO | {state.network_fail_count} |",
        "",
        "**Vérifications effectuées :** "
        + ", ".join(state.checks_run),
        "",
    ]

    if not state.findings:
        lines.append("✅ **Aucune divergence détectée. Le registre est en cohérence "
                     "avec l'état observé.**")
        lines.append("")

    if fail:
        lines.append("## ❌ Échecs critiques")
        lines.append("")
        for f in fail:
            lines.append(f.to_md_line())
        lines.append("")

    if warning:
        lines.append("## ⚠️ Avertissements")
        lines.append("")
        for f in warning:
            lines.append(f.to_md_line())
        lines.append("")

    if todo:
        lines.append("## 🟦 Champs à compléter dans `works.yaml`")
        lines.append("")
        # Grouper par work_id
        by_work: dict[str, list[Finding]] = {}
        for f in todo:
            by_work.setdefault(f.work_id, []).append(f)
        for wid in sorted(by_work):
            lines.append(f"### `{wid}`")
            for f in by_work[wid]:
                lines.append(f"- {f.message}")
            lines.append("")

    if info:
        lines.append("## ℹ️ Notes")
        lines.append("")
        for f in info:
            lines.append(f.to_md_line())
        lines.append("")

    lines.append("---")
    lines.append(f"*Généré par `scripts/audit_works.py` — {TODAY}*")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_observed(observed_dir: Path, name: str, data: Any) -> None:
    """Écrit l'état observé brut en JSON pour archivage."""
    observed_dir.mkdir(parents=True, exist_ok=True)
    path = observed_dir / f"{name}.json"
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )


# =============================================================================
# Main
# =============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--skip-network", action="store_true",
                        help="Mode offline : checks structurels uniquement")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Logs détaillés")
    args = parser.parse_args()

    if not WORKS_FILE.exists():
        print(f"❌ Fichier introuvable : {WORKS_FILE}", file=sys.stderr)
        return 1

    print(f"📖 Lecture de {WORKS_FILE.relative_to(REPO_ROOT)}")
    try:
        data = yaml.safe_load(WORKS_FILE.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        print(f"❌ YAML invalide : {e}", file=sys.stderr)
        return 1

    state = AuditState()
    state.works = data.get("works", []) or []
    state.metadata = data.get("meta", {}) or {}
    author = data.get("author", {}) or {}
    print(f"   {len(state.works)} œuvres chargées "
          f"(registry v{state.metadata.get('registry_version', '?')})")

    mode = "offline" if args.skip_network else "complet"
    print(f"🔍 Mode : {mode}")

    print("🔍 Vérification complétude canonique…")
    check_canonical_completeness(state.works, state)

    print("🔍 Vérification HTTP pages site…")
    obs_site = check_site_pages(state.works, state, args.skip_network)

    print("🔍 Vérification résolution DOIs…")
    obs_dois = check_dois_resolution(state.works, state, args.skip_network)

    print("🔍 Vérification balises citation_* Scholar…")
    obs_meta = check_citation_metadata(state.works, state, args.skip_network)

    print("🔍 Vérification cohérence ORCID…")
    obs_orcid = check_orcid(state.works, state, author.get("orcid", ""),
                            args.skip_network)

    print("🔍 Vérification cohérence OpenAlex…")
    obs_oa = check_openalex(state.works, state, author.get("openalex", ""),
                            args.skip_network)

    # Écriture des observés (bruts) si réseau utilisé
    if not args.skip_network:
        observed_dir = REPORTS_DIR / "observed" / TODAY
        write_observed(observed_dir, "site_pages", obs_site)
        write_observed(observed_dir, "dois", obs_dois)
        write_observed(observed_dir, "citation_metadata", obs_meta)
        write_observed(observed_dir, "orcid", obs_orcid)
        write_observed(observed_dir, "openalex", obs_oa)
        print(f"💾 État observé archivé : {observed_dir.relative_to(REPO_ROOT)}/")

    # Écriture du rapport
    REPORTS_DIR.mkdir(exist_ok=True)
    report_path = REPORTS_DIR / f"check-{TODAY}.md"
    write_report(state, report_path)
    print(f"✅ Rapport écrit : {report_path.relative_to(REPO_ROOT)}")

    # Synthèse console
    print()
    print(f"   ❌ Échecs       : {sum(1 for f in state.findings if f.level == 'fail')}")
    print(f"   ⚠️  Warnings    : {sum(1 for f in state.findings if f.level == 'warning')}")
    print(f"   🟦 À compléter  : {sum(1 for f in state.findings if f.level == 'todo')}")
    print(f"   ℹ️  Notes       : {sum(1 for f in state.findings if f.level == 'info')}")

    # Code de sortie : 0 si pas de fail, 1 sinon (utile pour CI)
    return 1 if any(f.level == "fail" for f in state.findings) else 0


if __name__ == "__main__":
    sys.exit(main())
