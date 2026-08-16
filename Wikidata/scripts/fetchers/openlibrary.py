# -*- coding: utf-8 -*-
"""
Fetcher OpenLibrary : récupère les métadonnées d'un livre via ISBN.

API OpenLibrary : https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data
"""

import json
import urllib.request
from typing import Optional


class OpenLibraryMetadata:
    """Métadonnées d'un livre via OpenLibrary."""

    def __init__(self, isbn: str, title: str, authors: list,
                 publisher: str, publication_date: str,
                 number_of_pages: int, url: str):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.publication_date = publication_date
        self.number_of_pages = number_of_pages
        self.url = url

    def __repr__(self):
        return f"OpenLibraryMetadata(isbn={self.isbn}, title={self.title[:50]}...)"


def fetch_openlibrary_metadata(isbn: str) -> Optional[OpenLibraryMetadata]:
    """
    Récupère les métadonnées via l'API OpenLibrary.

    Args:
        isbn: ISBN 10 ou 13, avec ou sans tirets

    Returns:
        OpenLibraryMetadata si succès, None si échec ou inconnu.
    """
    isbn_clean = isbn.replace("-", "").replace(" ", "").strip()
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn_clean}&format=json&jscmd=data"

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERROR] Échec fetch OpenLibrary {isbn_clean}: {e}")
        return None

    key = f"ISBN:{isbn_clean}"
    if key not in data:
        print(f"[WARN] ISBN {isbn_clean} non trouvé dans OpenLibrary")
        return None

    book = data[key]
    publishers = book.get("publishers", [])
    publisher = publishers[0].get("name", "") if publishers else ""

    return OpenLibraryMetadata(
        isbn=isbn_clean,
        title=book.get("title", ""),
        authors=[a.get("name", "") for a in book.get("authors", [])],
        publisher=publisher,
        publication_date=book.get("publish_date", ""),
        number_of_pages=book.get("number_of_pages", 0),
        url=book.get("url", ""),
    )
