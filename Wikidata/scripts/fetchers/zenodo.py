# -*- coding: utf-8 -*-
"""
Fetcher Zenodo : récupère les métadonnées d'un dépôt Zenodo via son DOI.

API Zenodo : https://zenodo.org/api/records/{id}
Format DOI : 10.5281/zenodo.{id} (extraction de {id} automatique)
"""

import json
import re
import urllib.request
from typing import Optional


class ZenodoMetadata:
    """Métadonnées d'un dépôt Zenodo, structurées pour génération de batch."""

    def __init__(self, doi: str, title: str, description: str,
                 publication_date: str, language: str,
                 keywords: list, pdf_url: str, record_id: str):
        self.doi = doi
        self.title = title
        self.description = description
        self.publication_date = publication_date  # ISO 8601
        self.language = language  # code ISO 639-1 (fr, en)
        self.keywords = keywords
        self.pdf_url = pdf_url
        self.record_id = record_id

    def __repr__(self):
        return f"ZenodoMetadata(doi={self.doi}, title={self.title[:50]}...)"


def fetch_zenodo_metadata(doi: str) -> Optional[ZenodoMetadata]:
    """
    Récupère les métadonnées d'un dépôt Zenodo via son DOI.

    Args:
        doi: DOI au format '10.5281/zenodo.XXXXX'

    Returns:
        ZenodoMetadata si succès, None si échec.

    Raises:
        ValueError si DOI mal formaté.
    """
    # Extraire l'ID Zenodo du DOI
    match = re.match(r"^10\.5281/zenodo\.(\d+)$", doi.strip())
    if not match:
        raise ValueError(
            f"DOI '{doi}' n'est pas un DOI Zenodo valide "
            "(format attendu : 10.5281/zenodo.XXXXX)"
        )

    record_id = match.group(1)
    url = f"https://zenodo.org/api/records/{record_id}"

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERROR] Échec fetch Zenodo {record_id}: {e}")
        return None

    metadata = data.get("metadata", {})

    # Construction du PDF URL canonique
    files = data.get("files", [])
    pdf_url = ""
    for f in files:
        key = f.get("key", "")
        if key.lower().endswith(".pdf"):
            pdf_url = f"https://zenodo.org/records/{record_id}/files/{key}"
            break

    return ZenodoMetadata(
        doi=doi,
        title=metadata.get("title", ""),
        description=metadata.get("description", ""),
        publication_date=metadata.get("publication_date", ""),
        language=metadata.get("language", ""),
        keywords=metadata.get("keywords", []),
        pdf_url=pdf_url,
        record_id=record_id,
    )
