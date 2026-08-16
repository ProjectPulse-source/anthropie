# -*- coding: utf-8 -*-
"""
Générateur de batch pour un nouveau livre.
"""

from typing import Optional

from generators.base import BatchGenerator
from fetchers.openlibrary import fetch_openlibrary_metadata
import config as cfg


class BookGenerator(BatchGenerator):
    """Génère un batch QuickStatements pour un nouveau livre."""

    def __init__(self, isbn_13: str, title: str, subtitle: str = "",
                 publication_date: str = "", asin: Optional[str] = None,
                 amazon_url: Optional[str] = None):
        super().__init__()
        self.isbn_13 = isbn_13.replace("-", "").replace(" ", "")
        self.title = title
        self.subtitle = subtitle
        self.publication_date = publication_date
        self.asin = asin
        self.amazon_url = amazon_url

    def fetch(self):
        """Tente de récupérer les métadonnées OpenLibrary (optionnel)."""
        meta = fetch_openlibrary_metadata(self.isbn_13)
        if meta:
            if not self.title:
                self.title = meta.title
            if not self.publication_date:
                self.publication_date = meta.publication_date

    def generate(self) -> list:
        """Produit les lignes du batch."""
        self.fetch()
        self.add_header(
            f"Livre — Création item Wikidata",
            f"ISBN-13 : {self.isbn_13} | Titre : {self.title[:60]}"
        )

        full_title = self.title
        if self.subtitle:
            full_title = f"{self.title} : {self.subtitle}"

        self.lines.append("CREATE")
        self.add_label("fr", full_title)
        self.add_description("fr", f"Livre de Stéphane Lalut")
        self.add_label("en", full_title)
        self.add_description("en", f"Book by Stéphane Lalut")

        # Type
        self.lines.append(f"LAST\t{cfg.INSTANCE_OF}\t{cfg.BOOK}")
        # Auteur
        self.lines.append(
            f"LAST\t{cfg.AUTHOR}\t{cfg.STEPHANE_LALUT}\t"
            f"{cfg.REF_URL}\t\"https://orcid.org/0009-0002-1794-4895\"\t"
            f"{cfg.REF_RETRIEVED}\t+{self.today}T00:00:00Z/11"
        )
        # ISBN-13
        self.lines.append(f'LAST\t{cfg.ISBN_13}\t"{self.isbn_13}"')
        # Langue
        self.lines.append(f"LAST\t{cfg.LANGUAGE_OF_WORK}\t{cfg.FRENCH}")
        # Date
        if self.publication_date:
            try:
                pub_date_iso = self.publication_date
                if len(pub_date_iso) == 4:  # année seule
                    pub_date_iso += "-01-01"
                self.lines.append(
                    f"LAST\t{cfg.PUBLICATION_DATE}\t+{pub_date_iso}T00:00:00Z/11"
                )
            except Exception:
                pass
        # ASIN Amazon
        if self.asin:
            self.lines.append(f'LAST\t{cfg.AMAZON_ASIN}\t"{self.asin}"')
        # URL Amazon
        if self.amazon_url:
            self.lines.append(f'LAST\t{cfg.FULL_WORK_URL}\t"{self.amazon_url}"')

        # Rétro-lien P800 sur la personne
        self.add_section("Rétro-lien (après exécution du CREATE)")
        self.lines.append(f"{cfg.STEPHANE_LALUT}\t{cfg.NOTABLE_WORK}\tNEW_QID")

        return self.lines
