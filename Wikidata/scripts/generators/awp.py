# -*- coding: utf-8 -*-
"""
Générateur de batch pour un nouveau working paper (AWP).
"""

from typing import Optional

from generators.base import BatchGenerator
from fetchers.zenodo import fetch_zenodo_metadata, ZenodoMetadata
import config as cfg


class AwpGenerator(BatchGenerator):
    """Génère un batch QuickStatements pour un nouvel AWP."""

    def __init__(self, zenodo_doi_fr: str, awp_number: int,
                 zenodo_doi_en: Optional[str] = None,
                 url_site_fr: Optional[str] = None,
                 url_site_en: Optional[str] = None,
                 main_subjects: Optional[list] = None):
        super().__init__()
        self.zenodo_doi_fr = zenodo_doi_fr
        self.zenodo_doi_en = zenodo_doi_en
        self.awp_number = awp_number
        self.url_site_fr = url_site_fr or f"https://stephane-lalut.com/awp/awp-{awp_number:02d}/"
        self.url_site_en = url_site_en or f"https://stephane-lalut.com/en/awp/awp-{awp_number:02d}/"
        self.main_subjects = main_subjects or [cfg.ANTHROPY_CONCEPT]
        self.metadata: Optional[ZenodoMetadata] = None

    def fetch(self):
        """Récupère les métadonnées Zenodo."""
        self.metadata = fetch_zenodo_metadata(self.zenodo_doi_fr)
        if self.metadata is None:
            raise RuntimeError(f"Impossible de fetch Zenodo {self.zenodo_doi_fr}")

    def generate(self) -> list:
        """Produit les lignes du batch."""
        if self.metadata is None:
            self.fetch()

        m = self.metadata
        self.add_header(
            f"AWP-{self.awp_number:02d} — Création item Wikidata",
            f"DOI Zenodo FR : {self.zenodo_doi_fr}"
        )

        self.lines.append("CREATE")
        self.add_label("fr", m.title)
        self.add_description(
            "fr",
            f"Working paper de Stéphane Lalut "
            f"(AWP-{self.awp_number:02d}, {m.publication_date[:4]})"
        )

        # Type
        self.lines.append(f"LAST\t{cfg.INSTANCE_OF}\t{cfg.SCHOLARLY_ARTICLE}")
        # Auteur
        self.lines.append(
            f"LAST\t{cfg.AUTHOR}\t{cfg.STEPHANE_LALUT}\t"
            f"{cfg.REF_URL}\t\"https://orcid.org/0009-0002-1794-4895\"\t"
            f"{cfg.REF_RETRIEVED}\t+{self.today}T00:00:00Z/11"
        )
        # DOI principal (Zenodo FR)
        self.lines.append(
            f'LAST\t{cfg.DOI}\t"{self.zenodo_doi_fr}"\t'
            f'{cfg.REF_URL}\t"https://doi.org/{self.zenodo_doi_fr}"\t'
            f"{cfg.REF_RETRIEVED}\t+{self.today}T00:00:00Z/11"
        )
        # Langue principale
        self.lines.append(f"LAST\t{cfg.LANGUAGE_OF_WORK}\t{cfg.FRENCH}")
        # Date de publication
        if m.publication_date:
            self.lines.append(
                f"LAST\t{cfg.PUBLICATION_DATE}\t+{m.publication_date}T00:00:00Z/11"
            )
        # Sujets principaux
        for subject in self.main_subjects:
            self.lines.append(f"LAST\t{cfg.MAIN_SUBJECT}\t{subject}")
        # Part of (série AWP)
        self.lines.append(f"LAST\t{cfg.PART_OF}\t{cfg.AWP_SERIES}")
        # URLs (full work + site canonique FR/EN)
        self.lines.append(
            f'LAST\t{cfg.FULL_WORK_URL}\t"https://zenodo.org/records/{m.record_id}"'
        )
        self.lines.append(
            f'LAST\t{cfg.FULL_WORK_URL}\t"{self.url_site_fr}"\t'
            f'{cfg.LANGUAGE_OF_WORK}\t{cfg.FRENCH}'
        )
        self.lines.append(
            f'LAST\t{cfg.FULL_WORK_URL}\t"{self.url_site_en}"\t'
            f'{cfg.LANGUAGE_OF_WORK}\t{cfg.ENGLISH}'
        )
        # DOI version EN en P953 si fourni (cf. décision Option B)
        if self.zenodo_doi_en:
            self.lines.append(
                f'LAST\t{cfg.FULL_WORK_URL}\t"https://doi.org/{self.zenodo_doi_en}"\t'
                f'{cfg.LANGUAGE_OF_WORK}\t{cfg.ENGLISH}'
            )

        # Rétro-liens (Phase C inline)
        self.add_section(
            f"AWP-{self.awp_number:02d} — Rétro-liens (à exécuter APRÈS création)"
        )
        self.lines.append(
            "# NOTE : Substituer 'NEW_QID' par le QID assigné après exécution du CREATE"
        )
        self.lines.append(f"{cfg.AWP_SERIES}\t{cfg.HAS_PART}\tNEW_QID")
        self.lines.append(f"{cfg.STEPHANE_LALUT}\t{cfg.NOTABLE_WORK}\tNEW_QID")

        return self.lines
