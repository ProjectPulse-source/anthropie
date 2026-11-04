"""Relit chaque citation de plf_votes.json dans le compte rendu archive de sa seance (empreinte controlee).
Usage : python verifier_plf_votes.py <dossier des comptes rendus archives>
Le dossier contient AN_CR_<date>_<premiere|deuxieme>_seance.html (06_PROMOTION/RECHERCHE_VOTRE_COMMUNE_2026-10-22/_SOURCES).
Sort 1 a la premiere citation introuvable ou a la premiere empreinte fausse : une citation non retrouvee ne se publie pas."""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ICI = Path(__file__).parent


def texte(p: Path) -> str:
    t = p.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    d, v = Path(sys.argv[1]), json.loads((ICI / "plf_votes.json").read_text(encoding="utf-8"))
    par_sha = {hashlib.sha256(p.read_bytes()).hexdigest(): p for p in d.glob("*.html")}
    for cle, s in v["seances"].items():
        if s["sha256_html"] not in par_sha:
            sys.exit(f"ECHEC : compte rendu {cle} absent du dossier ou empreinte differente")
    for a in v["articles"]:
        t = texte(par_sha[v["seances"][a["seance"]]["sha256_html"]])
        norm = lambda s: re.sub(r"\s+", " ", s)
        for c in [a["citation"], *a.get("citations_complementaires", [])]:
            if norm(c) not in t:
                sys.exit(f"ECHEC : art. {a['article']} : « {c} » introuvable dans {a['seance']}")
        if "pour" in a:
            m = f"Pour l’adoption {a['pour']} Contre {a['contre']}"
            if m not in t:
                sys.exit(f"ECHEC : art. {a['article']} : scrutin {a['pour']}-{a['contre']} introuvable")
        print(f"art. {a['article']} : {a['statut']} -- citation retrouvee" + (" + scrutin" if "pour" in a else ""))
    # Etape annoncee en seance (05/11/2026) : la date de l'etape suivante se cite aussi.
    if "etape_source" in v:
        e = v["etape_source"]
        if norm(e["citation"]) not in texte(par_sha[v["seances"][e["seance"]]["sha256_html"]]):
            sys.exit(f"ECHEC : etape suivante : « {e['citation']} » introuvable dans {e['seance']}")
        print("etape suivante -- citation retrouvee")
    # Decisions de commission (05/11/2026) : citees sur la page de l'amendement archivee.
    for c in v.get("commission", []):
        if c["sha256_html"] not in par_sha:
            sys.exit(f"ECHEC : amendement {c['amendement']} absent du dossier ou empreinte differente")
        t = texte(par_sha[c["sha256_html"]])
        for x in c["citations"]:
            if norm(x) not in t:
                sys.exit(f"ECHEC : art. {c['article']} ({c['amendement']}) : « {x} » introuvable")
        print(f"art. {c['article']} : {c['statut']} en commission ({c['amendement']}) -- citations retrouvees")
    print("OK : %d articles, %d decision(s) de commission, toutes citations retrouvees"
          % (len(v["articles"]), len(v.get("commission", []))))


if __name__ == "__main__":
    main()
