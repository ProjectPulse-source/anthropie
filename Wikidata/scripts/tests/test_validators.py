# -*- coding: utf-8 -*-
"""
Tests unitaires pour validators.py.

Exécution : python -m unittest tests.test_validators
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from validators import (
    validate_doi, validate_isbn13, validate_zenodo_community,
    validate_batch_lines, ValidationError
)


class TestValidators(unittest.TestCase):

    def test_valid_doi(self):
        validate_doi("10.5281/zenodo.19266862")
        validate_doi("10.2139/ssrn.6543618")
        validate_doi("10.31235/osf.io/z6x38_v1")

    def test_invalid_doi(self):
        with self.assertRaises(ValidationError):
            validate_doi("not-a-doi")
        with self.assertRaises(ValidationError):
            validate_doi("10/missing-prefix")

    def test_valid_isbn(self):
        validate_isbn13("978-2-9586347-2-8")
        validate_isbn13("9782958634728")

    def test_invalid_isbn(self):
        with self.assertRaises(ValidationError):
            validate_isbn13("123")

    def test_zenodo_community_valid(self):
        validate_zenodo_community("anthropie-working-papers")

    def test_zenodo_community_invalid(self):
        with self.assertRaises(ValidationError):
            validate_zenodo_community("anthropie-working-papers/records?q=")

    def test_p9934_as_qualifier_rejected(self):
        """Reproduit le bug Phase A 2026-05-12."""
        bad_lines = [
            'Q138909233\tP106\tQ188094\tS248\tQ22661177\tS9934\t"anthropie-working-papers"'
        ]
        with self.assertRaises(ValidationError) as ctx:
            validate_batch_lines(bad_lines)
        self.assertIn("P9934", str(ctx.exception))

    def test_p407_qualifier_on_p356_rejected(self):
        """Reproduit le bug Phase B 2026-05-12."""
        bad_lines = [
            'Q139771989\tP356\t"10.5281/zenodo.19431208"\tP407\tQ1860'
        ]
        with self.assertRaises(ValidationError) as ctx:
            validate_batch_lines(bad_lines)
        self.assertIn("P407", str(ctx.exception))

    def test_multiple_p356_warning(self):
        lines = [
            'Q139771989\tP356\t"10.5281/zenodo.19266862"',
            'Q139771989\tP356\t"10.2139/ssrn.6543618"',
        ]
        warnings = validate_batch_lines(lines)
        self.assertTrue(any("Q139771989" in w for w in warnings))


if __name__ == "__main__":
    unittest.main()
