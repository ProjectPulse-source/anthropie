"""check-relecture.py -- le texte servi des pages refondues est-il celui qui a été relu ?

    python scripts/check-relecture.py [public]                      contrôle (CI : hugo.yml)
    python scripts/check-relecture.py [public] --strict             idem, sortie 2 si une phrase a changé (session)
    python scripts/check-relecture.py [public] --instantane [URL]   après une relecture : refait l'instantané
                                                                    (de la page URL, ou de toutes les pages refondues)
    python scripts/check-relecture.py [public] --json sortie.json   phrases changées, pour l'issue de hugo.yml
    python scripts/check-relecture.py [public] --temoin             témoin positif

Industrialisation des ressources (arbitrage OPTIMUM-26 du 2026-10-11, chantier 4 ; décision de l'auteur : une phrase
changée ouvre une issue, sans bloquer la mise à jour -- les gardes de prose des générateurs bloquent déjà les phrases
devenues FAUSSES, la relecture rattrape les phrases devenues MALADROITES).

L'instantané docs/relectures/<page>.txt garde, phrase par phrase, le texte servi tel qu'il a été relu (même
extraction que check-rendu-ressources.py : scripts/ressources_build.py). Le contrôle liste les phrases du build qui
n'y sont pas : ajoutées, ou changées par un jeton, une mise à jour de données ou une retouche.
- BLOQUANT (sortie 1) : une page refondue (`ressource.refonte`) sans instantané -- « refondue » veut dire « relue »,
  et la date de l'instantané doit être celle de `ressource.refonte` ou postérieure.
- ALERTE (sortie 0, ou 2 avec --strict) : phrases changées ; hugo.yml en fait une issue « Relecture ciblée » par page.
Les pages non refondues n'ont pas d'instantané : leur relecture vient à leur phase B.

Témoin : --temoin modifie un nombre dans une copie en mémoire du HTML d'une page refondue ; la phrase doit sortir.
Condition de mort : aucune -- permanent, réexaminé à la revue annuelle (R2).
Sortie console ASCII pur.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ressources_build as rb  # noqa: E402

DOSSIER = rb.ROOT / "docs" / "relectures"


def nom(p: dict) -> Path:
    return DOSSIER / (p["url"].strip("/").replace("/", "__") + ".txt")


def lire(f: Path) -> tuple[str | None, list[str]]:
    lignes = f.read_text(encoding="utf-8").splitlines()
    m = re.search(r"relu le (\d{4}-\d{2}-\d{2})", lignes[0]) if lignes else None
    return (m.group(1) if m else None), [l for l in lignes if l and not l.startswith("# ")]


def changees(servies: list[str], relues: list[str]) -> list[str]:
    reste = Counter(relues)
    out = []
    for s in servies:
        if reste[s] > 0:
            reste[s] -= 1
        else:
            out.append(s)
    return out


def ascii_(s: str) -> str:
    return s.encode("ascii", "backslashreplace").decode("ascii")


def instantane(build: Path, cible: str | None) -> int:
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=rb.ROOT, capture_output=True, text=True).stdout.strip()
    sale = subprocess.run(["git", "status", "--porcelain", "content", "data", "layouts", "i18n"], cwd=rb.ROOT,
                          capture_output=True, text=True).stdout.strip()
    DOSSIER.mkdir(parents=True, exist_ok=True)
    n = 0
    pages = rb.pages(build)
    if cible:   # la correspondance la plus longue seule : « /x/ » est aussi la fin de « /en/x/ »
        c = cible.replace("\\", "/").rstrip("/")
        ok = [p for p in pages if p["refonte"] and c.endswith(p["url"].rstrip("/"))]
        pages = sorted(ok, key=lambda p: len(p["url"]))[-1:] if ok else []
    for p in pages:
        # cible comparée par la fin : Git Bash réécrit « /page/ » en « C:/Program Files/Git/page/ » (11/10/2026 : l'adresse
        # n'était plus reconnue et TOUTES les pages refondues étaient refaites, en silence)
        if not p["refonte"] or (cible and not cible.replace("\\", "/").rstrip("/").endswith(p["url"].rstrip("/"))):
            continue
        ph = rb.phrases(rb.texte(p["fichier"].read_text(encoding="utf-8")))
        tete = "# relu le %s ; texte servi de %s, build de %s%s ; une phrase par ligne (scripts/check-relecture.py)" % (
            date.today().isoformat(), p["url"], commit, " + modifications locales" if sale else "")
        nom(p).write_text(tete + "\n" + "\n".join(ph) + "\n", encoding="utf-8", newline="\n")
        n += 1
        print("  instantane  %s : %d phrase(s)" % (p["url"], len(ph)))
    if cible and not n:
        print("ECHEC : %s n'est pas une page refondue du build" % cible)
        return 1
    print("Relecture : %d instantane(s) ecrit(s) dans docs/relectures/." % n)
    return 0


def controler(build: Path) -> tuple[list, list]:
    manquants, ecarts = [], []
    for p in rb.pages(build):
        if not p["refonte"]:
            continue
        f = nom(p)
        if not f.is_file():
            manquants.append((p, "aucun instantane relu (%s)" % f.relative_to(rb.ROOT).as_posix()))
            continue
        quand, relues = lire(f)
        if not quand or quand < p["refonte"]:
            manquants.append((p, "instantane du %s anterieur a la refonte du %s" % (quand, p["refonte"])))
            continue
        ch = changees(rb.phrases(rb.texte(p["fichier"].read_text(encoding="utf-8"))), relues)
        if ch:
            ecarts.append((p, quand, ch))
    return manquants, ecarts


def temoin(build: Path) -> int:
    p = next(x for x in rb.pages(build) if x["refonte"] and nom(x).is_file())
    h = p["fichier"].read_text(encoding="utf-8")
    _q, relues = lire(nom(p))
    m = re.search(r"(?<=>)([^<>]*?)(\d+,\d)([^<>]*?)(?=<)", rb.main_html(h))
    mute = h.replace(m.group(0), m.group(1) + "99,9" + m.group(3), 1)
    ch = changees(rb.phrases(rb.texte(mute)), relues)
    ok = any("99,9" in s for s in ch)
    print("Temoin (%s, \"%s\" -> \"99,9\") : %s." % (p["url"], m.group(2), "phrase detectee" if ok else "PHRASE NON DETECTEE"))
    return 0 if ok else 1


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build = Path(args[0] if args else "public")
    if not build.is_dir():
        print("ECHEC : build introuvable (%s)" % build)
        return 1
    if "--temoin" in sys.argv:
        return temoin(build)
    if "--instantane" in sys.argv:
        i = sys.argv.index("--instantane")
        cible = sys.argv[i + 1] if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--") else None
        return instantane(build, cible)
    manquants, ecarts = controler(build)
    for p, raison in manquants:
        print("  ECART  %s : %s" % (p["url"], raison))
    for p, quand, ch in ecarts:
        print("  relecture ciblee  %s : %d phrase(s) changee(s) depuis la relecture du %s" % (p["url"], len(ch), quand))
        for s in ch:
            print("      " + ascii_(s[:200]))
    if "--json" in sys.argv:
        sortie = sys.argv[sys.argv.index("--json") + 1]
        Path(sortie).write_text(json.dumps([dict(url=p["url"], relu_le=q, phrases=ch) for p, q, ch in ecarts],
                                           ensure_ascii=False), encoding="utf-8")
    print("Relecture attestee : %d page(s) refondue(s) sans instantane valable, %d avec phrase(s) changee(s)."
          % (len(manquants), len(ecarts)))
    if manquants:
        return 1
    return 2 if (ecarts and "--strict" in sys.argv) else 0


if __name__ == "__main__":
    sys.exit(main())
