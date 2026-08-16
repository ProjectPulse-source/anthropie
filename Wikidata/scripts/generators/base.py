# -*- coding: utf-8 -*-
"""
Classe abstraite pour les générateurs de batch QuickStatements.
"""

from datetime import date
from pathlib import Path
from typing import List


class BatchGenerator:
    """
    Base abstraite. Les sous-classes implémentent generate() pour produire
    une liste de lignes QuickStatements.
    """

    def __init__(self):
        self.lines: List[str] = []
        self.today = date.today().isoformat()  # "2026-05-13"

    def add_header(self, title: str, subtitle: str = ""):
        """Ajoute un en-tête de batch."""
        self.lines.append("# " + "=" * 77)
        self.lines.append(f"# {title}")
        if subtitle:
            self.lines.append(f"# {subtitle}")
        self.lines.append(f"# Généré le {self.today} par generate_wikidata_batch.py")
        self.lines.append("# " + "=" * 77)
        self.lines.append("")

    def add_section(self, label: str):
        """Ajoute un séparateur de section."""
        self.lines.append("")
        self.lines.append("# " + "-" * 77)
        self.lines.append(f"# {label}")
        self.lines.append("# " + "-" * 77)

    def add_statement(self, qid: str, prop: str, value: str, sources: list = None):
        """
        Ajoute une déclaration au batch.

        Args:
            qid: Q-ID de l'item (ou "CREATE" ou "LAST")
            prop: P-ID de la propriété
            value: Valeur (string ou Q-ID)
            sources: Liste de tuples (S_prop, S_value) pour les références
        """
        parts = [qid, prop, value]
        if sources:
            for s_prop, s_value in sources:
                parts.append(s_prop)
                parts.append(s_value)
        # Ajout du timestamp de récupération si pas déjà présent
        if sources and not any(s[0] == "S813" for s in sources):
            parts.append("S813")
            parts.append(f"+{self.today}T00:00:00Z/11")
        self.lines.append("\t".join(parts))

    def add_label(self, lang: str, value: str):
        """Ajoute un label pour une langue."""
        self.lines.append(f'LAST\tL{lang}\t"{value}"')

    def add_description(self, lang: str, value: str):
        """Ajoute une description pour une langue."""
        self.lines.append(f'LAST\tD{lang}\t"{value}"')

    def generate(self) -> List[str]:
        """À implémenter par les sous-classes."""
        raise NotImplementedError

    def to_file(self, output_dir: Path, filename: str) -> Path:
        """Écrit le batch dans un fichier."""
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(self.lines) + "\n", encoding="utf-8")
        return output_path
