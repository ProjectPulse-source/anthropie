# -*- coding: utf-8 -*-
"""
Générateur de batch pour un nouvel article de revue.

NOTE : Pour Wikidata, on enrichit principalement l'item de l'auteur (P800)
plutôt que de créer un item par article. La création d'item article n'est
généralement justifiée que si l'article a un DOI Crossref ou est cité ailleurs.
"""

from typing import Optional

from generators.base import BatchGenerator
import config as cfg


class ArticleGenerator(BatchGenerator):
    """Génère un batch QuickStatements pour un nouvel article de revue."""

    def __init__(self, title: str, url: str, journal_qid: Optional[str],
                 publication_date: str, language: str = "fr",
                 doi: Optional[str] = None):
        super().__init__()
        self.title = title
        self.url = url
        self.journal_qid = journal_qid
        self.publication_date = publication_date
        self.language = language
        self.doi = doi

    def generate(self) -> list:
        """Produit les lignes du batch."""
        self.add_header(
            f"Article — Création item Wikidata",
            f"Titre : {self.title[:80]}"
        )

        lang_qid = cfg.FRENCH if self.language == "fr" else cfg.ENGLISH

        self.lines.append("CREATE")
        self.add_label(self.language, self.title)
        self.add_description(
            self.language,
            f"Article de Stéphane Lalut publié le {self.publication_date[:10]}"
        )

        # Type
        self.lines.append(f"LAST\t{cfg.INSTANCE_OF}\t{cfg.SCHOLARLY_ARTICLE}")
        # Auteur
        self.lines.append(
            f"LAST\t{cfg.AUTHOR}\t{cfg.STEPHANE_LALUT}\t"
            f"{cfg.REF_URL}\t\"{self.url}\"\t"
            f"{cfg.REF_RETRIEVED}\t+{self.today}T00:00:00Z/11"
        )
        # Langue
        self.lines.append(f"LAST\t{cfg.LANGUAGE_OF_WORK}\t{lang_qid}")
        # Date de publication
        if self.publication_date:
            self.lines.append(
                f"LAST\t{cfg.PUBLICATION_DATE}\t+{self.publication_date}T00:00:00Z/11"
            )
        # Revue (si Q-ID connu)
        if self.journal_qid:
            self.lines.append(f"LAST\t{cfg.PUBLISHED_IN}\t{self.journal_qid}")
        # DOI si fourni
        if self.doi:
            self.lines.append(
                f'LAST\t{cfg.DOI}\t"{self.doi}"\t'
                f'{cfg.REF_URL}\t"https://doi.org/{self.doi}"\t'
                f"{cfg.REF_RETRIEVED}\t+{self.today}T00:00:00Z/11"
            )
        # URL canonique
        self.lines.append(f'LAST\t{cfg.FULL_WORK_URL}\t"{self.url}"')

        # Rétro-lien P800 sur la personne
        self.add_section("Rétro-lien (après exécution du CREATE)")
        self.lines.append(f"{cfg.STEPHANE_LALUT}\t{cfg.NOTABLE_WORK}\tNEW_QID")

        return self.lines
