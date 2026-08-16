# -*- coding: utf-8 -*-
"""
CLI principal pour générer un batch QuickStatements pour une nouvelle publication.

Usage :
    python generate_wikidata_batch.py --type awp --zenodo-doi 10.5281/zenodo.XXXX --awp-number 7
    python generate_wikidata_batch.py --type article --url "https://..." --title "..." --date 2026-05-13
    python generate_wikidata_batch.py --type book --isbn 978-X-XXX-XX-X --title "..." --date 2026-MM-DD
"""

import argparse
import sys
from pathlib import Path

# Permettre les imports relatifs depuis ce script
sys.path.insert(0, str(Path(__file__).parent))

from generators.awp import AwpGenerator
from generators.article import ArticleGenerator
from generators.book import BookGenerator
from validators import validate_batch_lines, ValidationError


OUTPUT_DIR = Path(__file__).parent.parent / "batches-generated"


def cmd_awp(args):
    """Génère un batch pour un nouvel AWP."""
    print(f"[INFO] Génération batch AWP-{args.awp_number:02d} depuis {args.zenodo_doi}...")
    gen = AwpGenerator(
        zenodo_doi_fr=args.zenodo_doi,
        zenodo_doi_en=args.zenodo_doi_en,
        awp_number=args.awp_number,
    )
    lines = gen.generate()
    return gen, lines, f"awp-{args.awp_number:02d}-{gen.today}.qs"


def cmd_article(args):
    """Génère un batch pour un nouvel article."""
    print(f"[INFO] Génération batch article '{args.title[:50]}'...")
    gen = ArticleGenerator(
        title=args.title,
        url=args.url,
        journal_qid=args.journal_qid,
        publication_date=args.date,
        language=args.language,
        doi=args.doi,
    )
    lines = gen.generate()
    safe_title = "".join(c if c.isalnum() else "-" for c in args.title[:40]).strip("-")
    return gen, lines, f"article-{safe_title}-{gen.today}.qs"


def cmd_book(args):
    """Génère un batch pour un nouveau livre."""
    print(f"[INFO] Génération batch livre ISBN {args.isbn}...")
    gen = BookGenerator(
        isbn_13=args.isbn,
        title=args.title,
        subtitle=args.subtitle or "",
        publication_date=args.date or "",
        asin=args.asin,
        amazon_url=args.amazon_url,
    )
    lines = gen.generate()
    isbn_clean = args.isbn.replace("-", "")
    return gen, lines, f"book-{isbn_clean}-{gen.today}.qs"


def main():
    parser = argparse.ArgumentParser(
        description="Génère un batch QuickStatements pour une nouvelle publication."
    )
    subparsers = parser.add_subparsers(dest="type", required=True)

    # AWP
    p_awp = subparsers.add_parser("awp", help="Nouveau working paper")
    p_awp.add_argument("--zenodo-doi", required=True, help="DOI Zenodo (FR)")
    p_awp.add_argument("--zenodo-doi-en", help="DOI Zenodo (EN, optionnel)")
    p_awp.add_argument("--awp-number", type=int, required=True, help="Numéro AWP")

    # Article
    p_art = subparsers.add_parser("article", help="Nouvel article de revue")
    p_art.add_argument("--title", required=True)
    p_art.add_argument("--url", required=True)
    p_art.add_argument("--journal-qid", help="Q-ID de la revue (optionnel)")
    p_art.add_argument("--date", required=True, help="YYYY-MM-DD")
    p_art.add_argument("--language", default="fr", choices=["fr", "en"])
    p_art.add_argument("--doi", help="DOI si l'article en a un")

    # Livre
    p_book = subparsers.add_parser("book", help="Nouveau livre")
    p_book.add_argument("--isbn", required=True, help="ISBN-13")
    p_book.add_argument("--title", required=True)
    p_book.add_argument("--subtitle")
    p_book.add_argument("--date", help="YYYY-MM-DD ou YYYY")
    p_book.add_argument("--asin", help="ASIN Amazon")
    p_book.add_argument("--amazon-url", help="URL produit Amazon")

    args = parser.parse_args()

    dispatch = {"awp": cmd_awp, "article": cmd_article, "book": cmd_book}
    gen, lines, filename = dispatch[args.type](args)

    # Validation
    print("[INFO] Validation du batch...")
    try:
        warnings = validate_batch_lines(lines)
        for w in warnings:
            print(f"[WARN] {w}")
    except ValidationError as e:
        print(f"[ERROR] Validation échouée : {e}")
        sys.exit(1)

    # Écriture
    output_path = gen.to_file(OUTPUT_DIR, filename)
    print(f"\n[OK] Batch écrit : {output_path}")
    print(f"[OK] {len([l for l in lines if l and not l.startswith('#')])} commandes générées")
    print("\n--- RÉCAP POUR VALIDATION HUMAINE ---")
    print(f"Type : {args.type}")
    print(f"Fichier : {filename}")
    print(f"Lignes totales : {len(lines)}")
    print(f"\n[ACTION] Vérifier visuellement {output_path} avant transmission à Laura.")
    print("[ACTION] Nom de lot QuickStatements recommandé :")
    print(f"         Lalut-Anthropie-{args.type.capitalize()}-{gen.today}")


if __name__ == "__main__":
    main()
