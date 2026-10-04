# -*- coding: utf-8 -*-
"""Archive les pages du projet de loi de finances qui concernent les collectivites, et celles de l'avis du Haut
Conseil des finances publiques qui chiffrent les mesures : texte brut, page par page, avec l'empreinte des PDF.

    python scripts/sources_collectivites/archiver_plf.py <projet-loi.pdf> <avis-hcfp.pdf> <edition>

Geste ANNUEL, a la main, apres le depot du projet de loi (pas d'API pour ces deux documents). Le generateur
(update_dette_collectivites.py) ne lit que l'archive produite ici, dont il controle l'empreinte : aucun montant
n'est recopie a la main, tous sont relus dans le texte par motif. Les numeros de page ci-dessous sont ceux de
l'edition 2027 (texte n° 3210 depose le 01/10/2026 ; avis n° HCFP-2026-5) : a une nouvelle edition, les relever
dans le sommaire du projet de loi (« Dispositions relatives aux collectivites territoriales ») et les corriger ici.
"""
import hashlib
import json
import sys
from pathlib import Path

PAGES = {
    "2027": {"plf": [14, 22, 23, 25, 110, 111, 112, 113, 114, 115, 116, 117, 123, 126, 127, 218],
             "hcfp": [24, 27, 28],
             "plf_url": "https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf",
             "plf_titre": "Projet de loi de finances pour 2027, n° 3210, déposé le 1er octobre 2026",
             "hcfp_url": "https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf",
             "hcfp_titre": "Haut Conseil des finances publiques, avis n° HCFP-2026-5 du 25 septembre 2026"},
}


def pages(pdf: Path, numeros: list[int]) -> dict:
    import fitz  # PyMuPDF
    doc = fitz.open(pdf)
    return {str(n): doc[n - 1].get_text() for n in numeros}


def main() -> int:
    plf, hcfp, edition = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    P = PAGES[edition]
    out = {
        "edition": int(edition),
        "archive_le": __import__("datetime").date.today().isoformat(),
        "plf": {"titre": P["plf_titre"], "url": P["plf_url"], "sha256_pdf": hashlib.sha256(plf.read_bytes()).hexdigest(),
                "pages": pages(plf, P["plf"])},
        "hcfp": {"titre": P["hcfp_titre"], "url": P["hcfp_url"], "sha256_pdf": hashlib.sha256(hcfp.read_bytes()).hexdigest(),
                 "pages": pages(hcfp, P["hcfp"])},
    }
    cible = Path(__file__).resolve().parent / "plf_collectivites.json"
    txt = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    cible.write_bytes(txt.encode("utf-8"))
    print("archive :", cible.name, "| empreinte :", hashlib.sha256(txt.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
