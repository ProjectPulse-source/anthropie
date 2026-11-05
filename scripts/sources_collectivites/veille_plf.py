# -*- coding: utf-8 -*-
"""Veille et mise a jour automatique de l'etat du projet de loi de finances (registre plf_votes.json).

    python scripts/sources_collectivites/veille_plf.py releve      # lit les seances nouvelles, n'ecrit rien
    python scripts/sources_collectivites/veille_plf.py integrer    # ecrit le registre si un resultat est sans ambiguite
    python scripts/sources_collectivites/veille_plf.py temoin      # temoin positif : retrouve les decisions du 19/10

Decision de l'auteur (05/11/2026) : « pour la mise a jour des donnees du site il faut une surveillance et une mise a
jour automatisee ». Lancee par .github/workflows/plf-veille.yml.

Ce qui s'integre seul : un resultat ecrit dans la formule officielle du compte rendu, pour un article suivi
(« (L'article 84 est supprime.) », « en consequence, l'article 35 est supprime », « (L'article 34, amende, est
adopte.) ») et l'adoption de la premiere partie ; la date de l'etat avance a la derniere seance lue. Chaque resultat
garde sa citation verbatim et le texte du compte rendu, archive dans comptes_rendus/ avec son empreinte, que
verifier_plf_votes.py relit. Tout le reste devient un ticket (ligne VEILLE) : premiere partie rejetee, formule
inconnue autour d'un article suivi, ensemble du texte vote, saisine du Senat. Rien n'est jamais ecrase : une etape
nouvelle est une entree nouvelle.

Condition de mort : la tache s'arrete d'elle-meme quand le registre porte "termine": true (loi de finances
promulguee) ; le workflow se retire alors dans le meme commit que ce drapeau.
"""
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

ICI = Path(__file__).parent
REGISTRE = ICI / "plf_votes.json"
ARCHIVE = ICI / "comptes_rendus"
LISTE = "https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance"
BASE = "https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/"
UA = {"User-Agent": "stephane-lalut.com veille-plf/1.0 (+https://stephane-lalut.com/budget-2027-votre-commune/)"}
MOIS = {"janvier": 1, "fevrier": 2, "février": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7, "aout": 8,
        "août": 8, "septembre": 9, "octobre": 10, "novembre": 11, "decembre": 12, "décembre": 12}
RANG = {"premiere": 1, "deuxieme": 2, "troisieme": 3, "quatrieme": 4, "seance-unique": 1}
APOS = "[’']"


def lire_url(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
        return r.read()


def texte(brut: str) -> str:
    """Meme normalisation que verifier_plf_votes.texte() : la citation se relit sur le meme texte."""
    t = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", brut)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def seances_listees(page: str, edition: int) -> list[tuple[str, str, int]]:
    """[(date ISO, slug, rang)] des seances de la session qui couvre l'automne de l'edition - 1."""
    session = "session-ordinaire-de-%d-%d" % (edition - 1, edition)
    out = set()
    for slug in re.findall(session + r"/([a-z0-9-]+-seance-du-[a-z]+-\d{1,2}-[a-zà-ÿ]+-\d{4})", page):
        m = re.match(r"([a-z]+)-seance-du-[a-z]+-(\d{1,2})-([a-zà-ÿ]+)-(\d{4})$", slug)
        if m and m.group(3) in MOIS and m.group(1) in RANG:
            d = dt.date(int(m.group(4)), MOIS[m.group(3)], int(m.group(2)))
            out.add((d.isoformat(), session + "/" + slug, RANG[m.group(1)]))
    return sorted(out)


def troncon_plf(t: str, edition: int) -> str:
    """Partie du compte rendu consacree au projet de loi de finances : un « article 34 » d'un autre texte ne compte pas."""
    tete = "Projet de loi de finances pour %d" % edition
    # Chaque occurrence de l'intitule ouvre un troncon jusqu'a l'ordre du jour suivant : le sommaire en tete du compte
    # rendu en porte une, vide de resultats (temoin du 05/11/2026 : 0 decision retrouvee sans cela).
    morceaux, i = [], t.find(tete)
    while i >= 0:
        fin = t.find("Ordre du jour de la prochaine séance", i)
        morceaux.append(t[i:fin if fin > 0 else len(t)])
        i = t.find(tete, fin if fin > 0 else len(t))
    return " ".join(morceaux)


FORMULES = [  # (motif, statut) : formules du compte rendu officiel, citees verbatim
    (r"\(L{a}article (\d+), amendé, est adopté\.\)", "adopte_modifie"),
    (r"\(L{a}article (\d+) est adopté\.\)", "adopte"),
    (r"\(L{a}article (\d+), amendé, n{a}est pas adopté\.\)", "non_adopte"),
    (r"\(L{a}article (\d+) n{a}est pas adopté\.\)", "non_adopte"),
    (r"en conséquence, l{a}article (\d+) est supprimé", "supprime"),
    (r"\(L{a}article (\d+) est supprimé\.\)", "supprime"),
]
PREMIERE_ADOPTEE = r"\(L{a}ensemble de la première partie du projet de loi de finances pour %d(?:, amendé,)? est adopté\.\)|\(La première partie du projet de loi de finances pour %d(?:, amendée,)? est adoptée\.\)"
PREMIERE_REJETEE = r"première partie du projet de loi de finances pour %d[^.]{0,40}n{a}est pas adoptée?|L{a}ensemble de la première partie[^.]{0,80}n{a}est pas adopté"
ENSEMBLE = r"\(L{a}ensemble du projet de loi de finances pour %d(?:, amendé,)? est adopté\.\)|ensemble du projet de loi de finances pour %d[^.]{0,40}n{a}est pas adopté"


def extraire(t: str, suivis: set[int], edition: int) -> dict:
    """Resultats d'une seance : articles suivis (citation verbatim), premiere partie, ensemble, ordre du jour suivant,
    et les mentions d'un article suivi qu'aucune formule connue ne qualifie (ticket)."""
    plf = troncon_plf(t, edition)
    res = {"articles": [], "premiere": None, "ensemble": None, "inconnus": [], "prochaine": None}
    if not plf:
        return res
    for motif, statut in FORMULES:
        for m in re.finditer(motif.replace("{a}", APOS), plf):
            n = int(m.group(1))
            if n in suivis:
                res["articles"].append({"article": n, "statut": statut, "citation": m.group(0)})
    vus = {a["article"] for a in res["articles"]}
    for n in suivis - vus:
        for m in re.finditer(r"\((?:L{a}article {n}|Les articles[^)]*\b{n}\b)[^)]*\)".format(a=APOS, n=n), plf):
            res["inconnus"].append(m.group(0))
    m = re.search(PREMIERE_ADOPTEE.replace("{a}", APOS) % (edition, edition), plf)
    if m:
        res["premiere"] = {"statut": "adoptee", "citation": m.group(0)}
    elif re.search(PREMIERE_REJETEE.replace("{a}", APOS) % edition, plf):
        res["premiere"] = {"statut": "rejetee"}
    if re.search(ENSEMBLE.replace("{a}", APOS) % (edition, edition), plf):
        res["ensemble"] = True
    p = re.search(r"Prochaine séance, ([^:]{3,80}) : ([^.]{5,300})\.", t)
    if p:
        res["prochaine"] = p.group(0)
    return res


def suivis(v: dict) -> set[int]:
    """Articles dont la page affiche l'etat : ceux du registre, plus l'article 84 (seconde partie)."""
    return {a["article"] for a in v["articles"]} | {int(k) for k in v.get("non_examines", {}) if k.isdigit()} | \
        {c["article"] for c in v.get("commission", [])}


def cle(date: str, rang: int) -> str:
    return "AN-%s-%d" % (date, rang)


ETAPE_SECONDE = ("examen de la seconde partie, dont la mission « Relations avec les collectivités territoriales » et "
                 "l'article 84 ; délai de l'Assemblée : 17 novembre à minuit")
ETAPE_SECONDE_EN = ("examination of the second part, including the “Relations with local authorities” mission and "
                    "article 84; the Assembly's deadline: midnight on 17 November")


def passer(ecrire: bool) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    v = json.loads(REGISTRE.read_text(encoding="utf-8"))
    if v.get("termine"):
        print("Registre clos (loi promulguee) : veille terminee.")
        return 0
    lues = set(v.get("veille_seances_lues", []))
    depuis = v["etat_au"]
    liste = seances_listees(lire_url(LISTE).decode("utf-8", "replace"), v["edition"])
    nouvelles = [s for s in liste if s[0] >= depuis and cle(s[0], s[2]) not in lues and cle(s[0], s[2]) not in v["seances"]]
    print("Seances listees : %d ; nouvelles depuis le %s : %d" % (len(liste), depuis, len(nouvelles)))
    tickets, change, derniere = [], False, None
    for date, slug, rang in nouvelles:
        brut = lire_url(BASE + slug)
        t = texte(brut.decode("utf-8", "replace"))
        if "Avertissement: version provisoire" in t or "version provisoire" in t[:4000]:
            print("  %s : version provisoire, relue au passage suivant" % slug)
            continue
        k = cle(date, rang)
        r = extraire(t, suivis(v), v["edition"])
        derniere = max(derniere or date, date)
        lues.add(k)
        retenus = []
        for a in r["articles"]:
            deja = [x for x in v["articles"] if x["article"] == a["article"]]
            if deja and deja[-1]["statut"] == a["statut"] and v["seances"][deja[-1]["seance"]]["date"] <= date \
                    and deja[-1]["citation"] == a["citation"] and deja[-1]["seance"] == k:
                continue
            retenus.append(dict(a, seance=k))
        if r["inconnus"]:
            tickets.append("Formule non reconnue (%s) : %s -- a qualifier a la main" % (k, " | ".join(r["inconnus"][:5])))
        if r["premiere"] and r["premiere"]["statut"] == "rejetee":
            tickets.append("Premiere partie NON adoptee (%s) : consequences de procedure a ecrire a la main" % k)
        if r["ensemble"]:
            tickets.append("Vote sur l'ensemble du projet (%s) : frise (data/plf_procedure.json) et saisine du Senat a la main" % k)
        if retenus or (r["premiere"] and r["premiere"]["statut"] == "adoptee"):
            ARCHIVE.mkdir(exist_ok=True)
            arch = ARCHIVE / ("%s.txt" % k)
            if ecrire:
                arch.write_text(t, encoding="utf-8")
            v["seances"][k] = {"date": date, "assemblee": "Assemblée nationale", "seance": slug.split("/")[-1].replace("-", " "),
                               "url": BASE + slug, "sha256_html": hashlib.sha256(brut).hexdigest(),
                               "texte": "comptes_rendus/%s.txt" % k,
                               "sha256_texte": hashlib.sha256(t.encode("utf-8")).hexdigest()}
            for a in retenus:
                v["articles"].append(a)
                v.get("non_examines", {}).pop(str(a["article"]), None)
                print("  %s : art. %d %s -- « %s »" % (k, a["article"], a["statut"], a["citation"]))
            if r["premiere"] and r["premiere"]["statut"] == "adoptee":
                v.setdefault("etapes", []).append({"etape": "premiere_partie_adoptee", "seance": k, "citation": r["premiere"]["citation"]})
                v["etape_suivante"], v["etape_suivante_en"] = ETAPE_SECONDE, ETAPE_SECONDE_EN
                v["etape_source"] = {"seance": k, "citation": r["premiere"]["citation"]}
                print("  %s : premiere partie adoptee -- « %s »" % (k, r["premiere"]["citation"]))
            change = True
    if derniere and derniere > v["etat_au"]:
        v["etat_au"] = derniere
        change = True
    v["veille_seances_lues"] = sorted(lues)
    for x in tickets:
        # Titre (unique : un ticket par fait) puis detail, separes par une tabulation (format de maj-sources.yml).
        sys.stdout.buffer.write(("VEILLE\tProjet de loi de finances : %s\t%s\n" % (x.split(" : ")[0], x)).encode("utf-8"))
    if change and ecrire:
        REGISTRE.write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("Registre ecrit : etat au %s" % v["etat_au"])
    elif change:
        print("(releve) changements possibles : etat au %s ; rien ecrit" % v["etat_au"])
    else:
        print("Aucun changement.")
    return 0


def temoin() -> int:
    """Le releve doit retrouver, dans le compte rendu archive du 19/10, les decisions deja au registre."""
    sys.stdout.reconfigure(encoding="utf-8")
    v = json.loads(REGISTRE.read_text(encoding="utf-8"))
    attendu = {(a["article"], a["statut"]) for a in v["articles"] if a["seance"].startswith("AN-2026-10-19")}
    trouve = set()
    for k in ("AN-2026-10-19-1", "AN-2026-10-19-2"):
        brut = lire_url(v["seances"][k]["url"])
        t = texte(brut.decode("utf-8", "replace"))
        trouve |= {(a["article"], a["statut"]) for a in extraire(t, suivis(v), v["edition"])["articles"]}
    manque, trop = attendu - trouve, trouve - attendu
    print("Temoin veille PLF : attendu %d, retrouve %d, manquant %s, en trop %s" % (len(attendu), len(trouve & attendu),
                                                                                   sorted(manque), sorted(trop)))
    return 1 if manque or trop else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "releve"
    sys.exit(temoin() if cmd == "temoin" else passer(cmd == "integrer"))
