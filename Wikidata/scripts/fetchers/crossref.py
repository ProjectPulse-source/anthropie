# -*- coding: utf-8 -*-
"""
Fetcher Crossref : récupère les métadonnées d'un DOI Crossref (articles).

API Crossref : https://api.crossref.org/works/{doi}
"""

import json
import urllib.request
from typing import Optional


class CrossrefMetadata:
    """Métadonnées d'un article via Crossref."""

    def __init__(self, doi: str, title: str, authors: list,
                 publisher: str, journal: str, publication_date: str,
                 language: str, container_title: str):
        self.doi = doi
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.journal = journal
        self.publication_date = publication_date
        self.language = language
        self.container_title = container_title

    def __repr__(self):
        return f"CrossrefMetadata(doi={self.doi}, title={self.title[:50]}...)"


def fetch_crossref_metadata(doi: str) -> Optional[CrossrefMetadata]:
    """
    Récupère les métadonnées via l'API Crossref.

    Args:
        doi: DOI complet (ex: '10.1234/journal.5678')

    Returns:
        CrossrefMetadata si succès, None si échec.
    """
    url = f"https://api.crossref.org/works/{doi.strip()}"

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Lalut-Anthropie-Tool/1.0 (mailto:Stephane-lalut@outlook.fr)"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERROR] Échec fetch Crossref {doi}: {e}")
        return None

    msg = data.get("message", {})

    title_list = msg.get("title", [])
    title = title_list[0] if title_list else ""

    authors = []
    for a in msg.get("author", []):
        name = f"{a.get('given', '')} {a.get('family', '')}".strip()
        if name:
            authors.append(name)

    container_list = msg.get("container-title", [])
    container_title = container_list[0] if container_list else ""

    pub_date_parts = msg.get("published", {}).get("date-parts", [[]])[0]
    if len(pub_date_parts) >= 3:
        publication_date = f"{pub_date_parts[0]:04d}-{pub_date_parts[1]:02d}-{pub_date_parts[2]:02d}"
    elif len(pub_date_parts) >= 2:
        publication_date = f"{pub_date_parts[0]:04d}-{pub_date_parts[1]:02d}-01"
    elif len(pub_date_parts) >= 1:
        publication_date = f"{pub_date_parts[0]:04d}-01-01"
    else:
        publication_date = ""

    return CrossrefMetadata(
        doi=doi,
        title=title,
        authors=authors,
        publisher=msg.get("publisher", ""),
        journal=container_title,
        publication_date=publication_date,
        language=msg.get("language", ""),
        container_title=container_title,
    )
