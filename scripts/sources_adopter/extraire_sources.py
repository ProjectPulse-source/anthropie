#!/usr/bin/env python3
"""Constitue les sources du générateur update_promesses_adopter.py, à partir des pièces du dossier de recherche
(D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/), qui restent hors du dépôt du site.

Écrit dans ce dossier :
  e2_lois.csv            une ligne par loi promulguée du 20/06/2012 au 06/10/2026 (JO, AN, Dosleg, DOLE), origine
                         et nature au dépôt initial, motif de chaque absence (test décisif du 06/10/2026)
  e3_engagements.csv     une ligne par engagement de responsabilité (art. 49, al. 3), motions et issue
  bulletins_493.csv      témoin : engagements et motions lus dans les bulletins statistiques de l'AN, par session
  bulletins_depots.csv   témoin d'E1 : dépôts de projets et de propositions en première lecture, par session (bulletins)
  e1_initiatives_extrait.csv  une ligne par initiative déposée en premier lieu à l'AN (XIV à XVII), état à la fin de
                         la législature (colonnes utiles d'e1_initiatives.csv)
  pages_temoins.json     texte des pages citées (fiche n° 64 de l'AN ; rapport n° 802 du Sénat, p. 44), avec
                         l'empreinte du document entier
Les articles de la Constitution sont les réponses Légifrance archivées (legifrance_<sha>.json), copiées telles quelles.
Relance : python scripts/sources_adopter/extraire_sources.py (pièces brutes requises).
"""
import hashlib
import json
import re
import shutil
from pathlib import Path

ICI = Path(__file__).resolve().parent
R = Path(r"D:\PRO\06_PROMOTION\RECHERCHE_DOSSIER_PROMESSES_2026-10-05")
TEST = R / "test_decisif" / "adopter"
PIECES = {"fiche64": (R / "sondes" / "adopter" / "AN_fiche64_responsabilite_gouvernement.pdf", None),
          "r25-802|44": (R / "sondes" / "appliquer" / "senat_bilans" / "r25-802.pdf", 44)}


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def main() -> None:
    import fitz
    for f in ("e2_lois.csv", "e3_engagements.csv", "bulletins_493.csv", "bulletins_depots.csv"):
        shutil.copyfile(TEST / f, ICI / f)
    import csv
    with (TEST / "e1_initiatives.csv").open(encoding="utf-8") as src, \
            (ICI / "e1_initiatives_extrait.csv").open("w", encoding="utf-8", newline="") as dst:
        K = ["texte_depose", "legislature", "date_depot", "duree_jours", "origine", "nature", "etat"]
        w = csv.writer(dst, lineterminator="\n")
        w.writerow(K)
        for r in csv.DictReader(src):
            w.writerow([r[k] for k in K])
    out = {}
    for k, (f, p) in PIECES.items():
        d = fitz.open(f)
        t = " ".join(x.get_text() for x in d) if p is None else d[p - 1].get_text()
        out[k] = {"document": f.name, "page": p, "sha256_document": hashlib.sha256(f.read_bytes()).hexdigest(),
                  "texte": norm(t)}
    (ICI / "pages_temoins.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("copies et %d pages" % len(out))


if __name__ == "__main__":
    main()
