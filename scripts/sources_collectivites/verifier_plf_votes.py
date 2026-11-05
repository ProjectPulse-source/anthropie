"""Relit chaque citation de plf_votes.json dans le compte rendu archive de sa seance (empreinte controlee).
Usage : python verifier_plf_votes.py [<dossier des comptes rendus archives>]
Le dossier contient AN_CR_<date>_<premiere|deuxieme>_seance.html (06_PROMOTION/RECHERCHE_VOTRE_COMMUNE_2026-10-22/_SOURCES).
Une seance integree par la veille automatique (veille_plf.py, 05/11/2026) porte son texte dans le depot
(`texte`, `sha256_texte`, dossier comptes_rendus/) : elle se relit sans le dossier, donc aussi en CI. Sans dossier, les
seances archivees hors depot sont dites « hors depot » et ne sont pas relues.
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


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    d = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    v = json.loads((ICI / "plf_votes.json").read_text(encoding="utf-8"))
    par_sha = {hashlib.sha256(p.read_bytes()).hexdigest(): p for p in d.glob("*.html")} if d else {}
    textes, hors = {}, set()
    for cle, s in v["seances"].items():
        if "texte" in s:
            p = ICI / s["texte"]
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != s["sha256_texte"]:
                sys.exit(f"ECHEC : texte du compte rendu {cle} absent du depot ou empreinte differente")
            textes[cle] = p.read_text(encoding="utf-8")
        elif d is None:
            hors.add(cle)
        elif s["sha256_html"] not in par_sha:
            sys.exit(f"ECHEC : compte rendu {cle} absent du dossier ou empreinte differente")
        else:
            textes[cle] = texte(par_sha[s["sha256_html"]])
    n = 0
    for a in v["articles"]:
        if a["seance"] in hors:
            continue
        t = textes[a["seance"]]
        for c in [a["citation"], *a.get("citations_complementaires", [])]:
            if norm(c) not in t:
                sys.exit(f"ECHEC : art. {a['article']} : « {c} » introuvable dans {a['seance']}")
        if "pour" in a:
            m = f"Pour l’adoption {a['pour']} Contre {a['contre']}"
            if m not in t:
                sys.exit(f"ECHEC : art. {a['article']} : scrutin {a['pour']}-{a['contre']} introuvable")
        n += 1
        print(f"art. {a['article']} : {a['statut']} -- citation retrouvee" + (" + scrutin" if "pour" in a else ""))
    # Etape annoncee en seance (05/11/2026) et etapes integrees par la veille : la date de l'etape se cite aussi.
    for e in [v["etape_source"]] if "etape_source" in v else []:
        if e["seance"] not in hors:
            if norm(e["citation"]) not in textes[e["seance"]]:
                sys.exit(f"ECHEC : etape suivante : « {e['citation']} » introuvable dans {e['seance']}")
            print("etape suivante -- citation retrouvee")
    for e in v.get("etapes", []):
        if e["seance"] not in hors and norm(e["citation"]) not in textes[e["seance"]]:
            sys.exit(f"ECHEC : etape {e['etape']} : « {e['citation']} » introuvable dans {e['seance']}")
    # Decisions de commission (05/11/2026) : citees sur la page de l'amendement archivee (hors depot).
    for c in v.get("commission", []):
        if d is None:
            continue
        if c["sha256_html"] not in par_sha:
            sys.exit(f"ECHEC : amendement {c['amendement']} absent du dossier ou empreinte differente")
        t = texte(par_sha[c["sha256_html"]])
        for x in c["citations"]:
            if norm(x) not in t:
                sys.exit(f"ECHEC : art. {c['article']} ({c['amendement']}) : « {x} » introuvable")
        print(f"art. {c['article']} : {c['statut']} en commission ({c['amendement']}) -- citations retrouvees")
    print("OK : %d article(s) relu(s), %d decision(s) de commission%s ; toutes citations retrouvees"
          % (n, len(v.get("commission", [])) if d else 0,
             (" ; hors depot, non relues ici : %s" % ", ".join(sorted(hors))) if hors else ""))


if __name__ == "__main__":
    main()
