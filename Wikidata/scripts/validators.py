# -*- coding: utf-8 -*-
"""
Validateurs Wikidata. Empêche les erreurs de design avant écriture.

Référence : les 8 erreurs accumulées dans le chantier Phase A+B+C
(mai 2026) ont permis d'identifier les pièges récurrents. Ce module
les bloque dès la génération.
"""

import re
from typing import List, Tuple

from config import (
    REGEX_DOI, REGEX_ISBN_13, REGEX_ZENODO_COMMUNITY,
    MAIN_VALUE_ONLY, FORBIDDEN_QUALIFIERS, DOI, LANGUAGE_OF_WORK
)


class ValidationError(Exception):
    """Levée si une violation de contrainte Wikidata est détectée."""
    pass


def validate_doi(doi: str) -> None:
    """Vérifie le format DOI."""
    if not re.match(REGEX_DOI, doi):
        raise ValidationError(
            f"DOI '{doi}' ne respecte pas le format Wikidata "
            f"(regex {REGEX_DOI})"
        )


def validate_isbn13(isbn: str) -> None:
    """Vérifie le format ISBN-13."""
    if not re.match(REGEX_ISBN_13, isbn):
        raise ValidationError(
            f"ISBN '{isbn}' ne respecte pas le format ISBN-13 "
            f"(regex {REGEX_ISBN_13})"
        )


def validate_zenodo_community(slug: str) -> None:
    """Vérifie le format d'un slug Zenodo Community."""
    if not re.match(REGEX_ZENODO_COMMUNITY, slug):
        raise ValidationError(
            f"Slug Zenodo Community '{slug}' invalide. "
            f"Ne doit contenir que minuscules, chiffres, tirets, underscores."
        )


def validate_batch_lines(lines: List[str]) -> List[str]:
    """
    Vérifie une liste de lignes de batch QuickStatements.

    Erreurs détectées :
    1. P9934 utilisé comme qualifier ou source (scope = main value only)
    2. P407 utilisé comme qualifier de P356
    3. P356 multiples sans qualifier valide sur le même item

    Args:
        lines: Liste de lignes de batch (sans les commentaires #).

    Returns:
        Liste de warnings (str). Lève ValidationError si erreur critique.
    """
    warnings = []
    p356_per_item = {}  # {QID: count}

    for i, line in enumerate(lines, start=1):
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue

        # Découper la ligne
        parts = line_stripped.split("\t")
        if len(parts) < 3:
            continue

        qid = parts[0]
        prop = parts[1]

        # Erreur 1 : P9934 (et autres MAIN_VALUE_ONLY) en qualifier ou source
        for j in range(3, len(parts), 2):
            qual = parts[j] if j < len(parts) else ""
            # Préfixes Q (qualifier) ou S (source) qui pointent vers une P mainvalue
            if qual.startswith("S") or qual.startswith("P"):
                pid_qual = "P" + qual[1:] if qual[0] in "PS" else qual
                if pid_qual in MAIN_VALUE_ONLY:
                    raise ValidationError(
                        f"Ligne {i}: '{pid_qual}' est en scope 'main value only' "
                        f"et ne peut pas être utilisé comme qualifier/source. "
                        f"Erreur Phase A 2026-05-12 (P9934) reproduite. "
                        f"Ligne en cause : {line_stripped[:120]}"
                    )

        # Erreur 2 : P407 comme qualifier de P356
        if prop == DOI:
            for j in range(3, len(parts), 2):
                qual = parts[j] if j < len(parts) else ""
                if qual == LANGUAGE_OF_WORK:
                    raise ValidationError(
                        f"Ligne {i}: P407 (langue) n'est PAS un qualifier valide "
                        f"de P356 (DOI). Erreur Phase B 2026-05-12 reproduite. "
                        f"Utiliser P953 (full work URL) pour les variantes "
                        f"linguistiques d'une œuvre. "
                        f"Ligne en cause : {line_stripped[:120]}"
                    )

        # Comptage P356 par item (pour erreur 3)
        if prop == DOI and qid not in ("CREATE", "LAST"):
            p356_per_item[qid] = p356_per_item.get(qid, 0) + 1

    # Erreur 3 : P356 multiples sur un même item
    for qid, count in p356_per_item.items():
        if count > 1:
            warnings.append(
                f"L'item {qid} reçoit {count} P356 (DOI). "
                f"Contrainte d'unicité Wikidata : un seul DOI par item. "
                f"Considérer P953 (URL) pour les DOIs supplémentaires."
            )

    return warnings
