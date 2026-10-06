#!/usr/bin/env python3
"""Constitue les sources du générateur update_promesses_appliquer.py, à partir des pièces brutes du dossier de
recherche (D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/), qui restent hors du dépôt du site.

Écrit dans ce dossier :
  barometre_lois_extrait.csv     lignes BRUTES du baromètre (lois publiées du 01/10/2017 au 30/09/2025, conventions
                                 comprises : le générateur les écarte lui-même et en rend compte)
  barometre_mesures_extrait.csv  lignes BRUTES des mesures de ces lois
  senat_pages.json               texte de chaque page citée des rapports et communiqués du Sénat, avec l'empreinte
                                 du document entier (le document se retélécharge et se recontrôle)
  registre_concordance.csv       registre loi par loi baromètre / Sénat (test décisif du 06/10/2026)
  senat_effectifs.json           effectifs par catégorie annoncés dans les annexes du Sénat
  sgg_bilan_31-12-2025_extrait.txt  extrait verbatim du bilan semestriel du SGG, lu par navigateur
Chaque extrait de baromètre porte en tête l'empreinte et le nombre de lignes du fichier complet.
Relance : python scripts/sources_appliquer/extraire_sources.py (pièces brutes requises).
"""
import csv
import hashlib
import io
import json
import re
import shutil
from pathlib import Path

ICI = Path(__file__).resolve().parent
R = Path(r"D:\PRO\06_PROMOTION\RECHERCHE_DOSSIER_PROMESSES_2026-10-05")
SONDE = R / "sondes" / "appliquer"
TEST = R / "test_decisif" / "appliquer"
URL = "https://barometre.assemblee-nationale.fr/"

# (document, page PDF 1-indexée ou None pour une page HTML) cités par la page
PAGES = [("r18-542", 5), ("r18-542", 539), ("r19-523", 7), ("r19-523", 13), ("r25-802", 7), ("r25-802", 45),
         ("r25-802", 47), ("r25-802", 271), ("r24-710", 3)]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def extrait_barometre() -> None:
    fl = SONDE / "barometre_application_lois_assemblee.csv"
    fm = SONDE / "barometre_application_mesures_assemblee.csv"
    tl = fl.read_text(encoding="utf-8-sig")
    lignes = list(csv.reader(io.StringIO(tl), delimiter=";"))
    garde = [l for l in lignes[1:] if "2017-10-01" <= l[0] <= "2025-09-30"]
    ids = {l[2] for l in garde}
    out = io.StringIO()
    out.write("# source: %sbarometre_application_lois_assemblee.csv ; version du 05/10/2026 ; sha256 %s ; %d lois au "
              "fichier complet ; extrait : lois publiees du 01/10/2017 au 30/09/2025 (%d)\n" % (URL, sha(fl), len(lignes) - 1, len(garde)))
    w = csv.writer(out, delimiter=";", lineterminator="\n")
    w.writerow(lignes[0])
    w.writerows(garde)
    (ICI / "barometre_lois_extrait.csv").write_text(out.getvalue(), encoding="utf-8")
    m = list(csv.reader(io.StringIO(fm.read_text(encoding="utf-8-sig")), delimiter=";"))
    gm = [l for l in m[1:] if l[1] in ids]
    out = io.StringIO()
    out.write("# source: %sbarometre_application_mesures_assemblee.csv ; version du 05/10/2026 ; sha256 %s ; %d mesures "
              "au fichier complet ; extrait : mesures des lois de l'extrait des lois (%d)\n" % (URL, sha(fm), len(m) - 1, len(gm)))
    w = csv.writer(out, delimiter=";", lineterminator="\n")
    w.writerow(m[0])
    w.writerows(gm)
    (ICI / "barometre_mesures_extrait.csv").write_text(out.getvalue(), encoding="utf-8")
    print("barometre : %d lois, %d mesures" % (len(garde), len(gm)))


def pages_senat() -> None:
    import fitz
    serie = list(csv.DictReader((TEST / "serie_longue.csv").open(encoding="utf-8"), delimiter=";"))
    voulu = list(PAGES)
    for s in serie:
        p = None if s["page_pdf"] == "(HTML)" else int(s["page_pdf"])
        if (s["document"], p) not in voulu:
            voulu.append((s["document"], p))
    out = {}
    for doc, p in voulu:
        base = SONDE / "senat_bilans"
        f = base / doc if doc.endswith(".html") else base / (doc + ".pdf")
        if p is None:
            t = f.read_bytes().decode("utf-8", "replace")
            if "charset=iso-8859-1" in t.lower() or "\ufffd" in t:
                t = f.read_bytes().decode("cp1252")
            t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S | re.I)
            import html as h
            t = h.unescape(re.sub(r"<[^>]+>", " ", t))
        else:
            t = fitz.open(f)[p - 1].get_text()
        out["%s|%s" % (doc, p if p else "html")] = {"document": f.name, "page": p, "sha256_document": sha(f), "texte": norm(t)}
    (ICI / "senat_pages.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("senat : %d pages" % len(out))


def copies() -> None:
    shutil.copyfile(TEST / "registre_concordance.csv", ICI / "registre_concordance.csv")
    shutil.copyfile(TEST / "sgg_bilan_31-12-2025_extrait.txt", ICI / "sgg_bilan_31-12-2025_extrait.txt")
    S = json.loads((TEST / "_senat_listes.json").read_text(encoding="utf-8"))
    eff = {s: {"document": v["source"], "annonces": v.get("annonces")} for s, v in S.items()}
    eff["2024-2025"]["annonces_commissions"] = {k: v for k, v in S["2024-2025"]["annonces_textuelles"].items() if v}
    (ICI / "senat_effectifs.json").write_text(json.dumps(eff, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    extrait_barometre()
    pages_senat()
    copies()
