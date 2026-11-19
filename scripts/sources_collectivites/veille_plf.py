# -*- coding: utf-8 -*-
"""Veille et mise a jour automatique de l'etat du projet de loi de finances (registre plf_votes.json).

    python scripts/sources_collectivites/veille_plf.py releve      # lit les seances nouvelles, n'ecrit rien
    python scripts/sources_collectivites/veille_plf.py integrer    # ecrit le registre si un resultat est sans ambiguite
    python scripts/sources_collectivites/veille_plf.py temoin      # temoins : Assemblee (19/10/2026), Senat (03/12/2025)

Decision de l'auteur (05/11/2026) : « pour la mise a jour des donnees du site il faut une surveillance et une mise a
jour automatisee ». Lancee par .github/workflows/plf-veille.yml. Etendue au Senat le 19/11/2026 (auteur : « la mise a
jour de la page AMF doit etre automatique, geree par le module dedie »).

ASSEMBLEE. Ce qui s'integre seul : un resultat ecrit dans la formule officielle du compte rendu, pour un article suivi
(« (L'article 84 est supprime.) », « en consequence, l'article 35 est supprime », « (L'article 34, amende, est
adopte.) ») et l'adoption de la premiere partie. Tout le reste devient un ticket (ligne VEILLE).

SENAT (19/11/2026). Trois canaux officiels, lus sans contourner quoi que ce soit (pages publiques, agent identifie) :
  - le dossier legislatif (dossier-legislatif/pjlfAAAA.html) : transmission du texte (« Texte n° 155 (2026-2027)
    transmis au Senat le 19 novembre 2026 »), qui fait passer le texte de « attendu » a « transmis » ;
  - le compte rendu INTEGRAL de chaque seance (seances/sAAAAMM/sAAAAMMJJ/sAAAAMMJJ_mono.html), decouvert par l'index du
    mois, qui porte le numero de la seance et la mention « version provisoire » ; la version provisoire, complete et
    publiee en 24 a 36 heures, est lue et dite telle dans le registre (la definitive arrive une a deux semaines plus
    tard). Le compte rendu ANALYTIQUE, en ligne en deux heures, n'est PAS lu : sur la seance du 3/12/2025 il porte
    « L'article 40, modifie, n'est pas adopte. » la ou le compte rendu integral et le texte adopte par le Senat (n° 29,
    2025-2026) disent l'article adopte (temoin du 19/11/2026) ;
  - le jeu des amendements (Ameli, CSV du texte) : un amendement de la commission des finances sur un article suivi,
    nouveau au registre ; une suppression s'integre (page de l'amendement archivee), toute autre redaction est un ticket.
Le compte rendu se lit par sa STRUCTURE (intitule de point de l'ordre du jour « Loi de finances pour AAAA », mention
d'article, lien de navigation vers le dossier du texte) : un « article 34 » du projet de loi de financement de la
securite sociale, examine les memes semaines, ne compte pas. Formules integrees : « Je mets aux voix l'article N[,
modifie]. (L'article N est adopte.) », « (L'article N n'est pas adopte.) », le meme vote par scrutin public (« Le Senat
a adopte. »), « En consequence, l'article N est supprime » et « ... est ainsi redige » ; adoption de la premiere partie ;
sort des amendements de la commission des finances deja au registre. BLOQUANT (ticket, seance ni integree ni comptee
comme lue, date de l'etat arretee avant elle) : formule inconnue autour d'un article suivi, premiere partie non
adoptee, vote sur l'ensemble, vote unique, article du dossier hors du point de l'ordre du jour ou l'inverse, contenu
illisible. La date de l'etat avance a la derniere seance lue sans trou dans la numerotation du Senat, et seulement par
le Senat tant qu'il est saisi du texte (une seance de l'Assemblee sur un autre texte ne date pas l'etat).

Chaque resultat garde sa citation verbatim et le texte du compte rendu, archive dans comptes_rendus/ avec son empreinte,
que verifier_plf_votes.py relit. Rien n'est jamais ecrase : une etape nouvelle est une entree nouvelle.

Condition de mort : la tache s'arrete d'elle-meme quand le registre porte "termine": true (loi de finances
promulguee) ; le workflow se retire alors dans le meme commit que ce drapeau.
"""
import csv
import datetime as dt
import hashlib
import html
import io
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
        # 19/11/2026 (lecon du Senat, propagee) : « en conséquence, l'article 33 est ainsi rédigé » se lit a l'interieur de la
        # parenthese d'un amendement ; sans ce motif, il n'etait ni integre ni signale.
        for m in re.finditer(r"en conséquence, l{a}article {n}(?!\d)(?!(?:er)?\s+(?:bis|ter|quater|quinquies|sexies|septies|[A-Z])\b)"
                             r"[^.;)]*".format(a=APOS, n=n), plf):
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


# Articles dont les pages affichent l'etat (Budget 2027 et Collectivites, 19/11/2026) : les cinq mesures (34 a 37, 84),
# l'article 41 (FCTVA, avec le 35), et les dispositions citees « Autres dispositions » et « DGF » (40, 53, 83, 85, 87).
# Lu aussi par update_dette_collectivites.py (etat de chacun au Senat) : une seule liste.
ARTICLES_PAGE = (34, 35, 36, 37, 40, 41, 53, 83, 84, 85, 87)


def suivis(v: dict) -> set[int]:
    """Articles dont la page affiche l'etat : ceux du registre, les articles de la page, ceux des commissions."""
    return {a["article"] for a in v["articles"]} | {int(k) for k in v.get("non_examines", {}) if k.isdigit()} | \
        {c["article"] for c in v.get("commission", [])} | {c["article"] for c in v.get("commission_senat", [])} | \
        set(ARTICLES_PAGE)


def cle(date: str, rang: int) -> str:
    return "AN-%s-%d" % (date, rang)


ETAPE_SECONDE = ("examen de la seconde partie, dont la mission « Relations avec les collectivités territoriales » et "
                 "l'article 84 ; délai de l'Assemblée : 17 novembre à minuit")
ETAPE_SECONDE_EN = ("examination of the second part, including the “Relations with local authorities” mission and "
                    "article 84; the Assembly's deadline: midnight on 17 November")


def etape(v: dict, nom: str) -> dict | None:
    return next((e for e in v.get("etapes", []) if e["etape"] == nom), None)


def au_senat(v: dict) -> bool:
    """Le Senat est saisi du texte (rejet par l'Assemblee, ou transmission lue) et ne l'a pas encore vote : seules ses
    seances datent l'etat. Le vote du Senat sur l'ensemble n'entre au registre que par un geste humain (ticket)."""
    return bool(v.get("texte_rejete") or etape(v, "senat_transmis")) and not etape(v, "senat_ensemble")


def passer_an(v: dict, ecrire: bool, tickets: list) -> bool:
    lues = set(v.get("veille_seances_lues", []))
    depuis = v["etat_au"]
    liste = seances_listees(lire_url(LISTE).decode("utf-8", "replace"), v["edition"])
    nouvelles = [s for s in liste if s[0] >= depuis and cle(s[0], s[2]) not in lues and cle(s[0], s[2]) not in v["seances"]]
    print("Assemblee : seances listees : %d ; nouvelles depuis le %s : %d" % (len(liste), depuis, len(nouvelles)))
    change, derniere = False, None
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
            if any(x["article"] == a["article"] and x["seance"] == k and x["statut"] == a["statut"]
                   and x["citation"] == a["citation"] for x in v["articles"]):
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
    # 19/11/2026 : tant que le Senat est saisi, une seance de l'Assemblee (sur un autre texte) ne date pas l'etat.
    if derniere and derniere > v["etat_au"] and not au_senat(v):
        v["etat_au"] = derniere
        change = True
    if sorted(lues) != v.get("veille_seances_lues", []):
        v["veille_seances_lues"] = sorted(lues)
        change = change or bool(nouvelles)
    return change


# ------------------------------------------------------------------ Senat (19/11/2026)
SENAT = "https://www.senat.fr"
DOSLEG = SENAT + "/dossier-legislatif/pjlf%d.html"
MOIS_NOMS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
             "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def date_longue(iso: str) -> str:
    d = dt.date.fromisoformat(iso)
    return "%s %s %s %d" % (JOURS[d.weekday()], "1er" if d.day == 1 else d.day, MOIS_NOMS[d.month - 1], d.year)


def lignes_senat(brut: str) -> list[tuple[str, str]]:
    """Contenu d'un compte rendu integral du Senat (entre « START : cri » et « END cri »), en lignes (type, texte) :
    S1 = intitule d'un point de l'ordre du jour (classe titre_S1), ART = mention d'article (mention_article), NAV = dossier
    vise par la navigation d'un article (lien « dossierleg »), P = tout autre paragraphe. Les balises de mise en forme
    (span, a, i, sup...) sont retirees SANS espace : le compte rendu coupe « (L’article 40 est adopté.) » en plusieurs
    <span> (temoin du 19/11/2026 : « (L ’ amendement n ’ est pas adopté.) » avec la normalisation de l'Assemblee)."""
    i = brut.find("<!-- START : cri -->")
    j = brut.find("<!-- END cri -->", i + 1)
    if i < 0 or j < 0:
        return []
    t = re.sub(r"\s+", " ", brut[i:j])
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"<!--.*?-->", " ", t)
    t = re.sub(r"<div align='right'>(.*?)</div>",
               lambda m: "".join("\n\x01NAV\t%s\n" % d for d in re.findall(r"href='/dossierleg/([a-z0-9_]+)\.html'", m.group(1))),
               t)
    t = re.sub(r'<p\b[^>]*class="titre_S1"[^>]*>', "\n\x01S1\t", t)
    t = re.sub(r'<p\b[^>]*class="mention_article"[^>]*>', "\n\x01ART\t", t)
    t = re.sub(r"<(?:p|div|td|th|tr|li|br|h[1-6]|table|ul|ol)\b[^>]*>", "\n\x01P\t", t)
    t = re.sub(r"<[^>]+>", "", t)
    out = []
    for ligne in html.unescape(t).split("\n"):
        typ, txt = ligne.split("\t", 1) if ligne.startswith("\x01") and "\t" in ligne else ("\x01P", ligne)
        txt = re.sub(r"\s+", " ", txt).strip()
        if txt:
            out.append((typ[1:], txt))
    return out


def lignes_archive(lignes: list[tuple[str, str]]) -> str:
    """Format d'archive « lignes » : une ligne par paragraphe, « TYPE<tab>texte ». verifier_plf_votes.py relit les
    citations dans le texte plat (paragraphes joints par une espace), la structure reste relisible par l'extracteur."""
    return "".join("%s\t%s\n" % (typ, txt) for typ, txt in lignes)


def lire_lignes(s: str) -> list[tuple[str, str]]:
    return [tuple(x.split("\t", 1)) for x in s.splitlines() if "\t" in x]


def plat(lignes: list[tuple[str, str]]) -> str:
    return " ".join(txt for typ, txt in lignes if typ != "NAV")


def numero_article(txt: str):
    """« Article 31 », « Article 36 (suite) » -> 31, 36 ; « Article 1er » -> 1 ; tout le reste (bis, liminaire,
    « Après l'article 34 ») -> None : un article additionnel ne se confond pas avec l'article qu'il suit."""
    m = re.match(r"Article (\d+)(?:er)?(?: \((?:suite|précédemment réservé)\))?$", txt, re.I)
    return int(m.group(1)) if m else None


def tete_plf(txt: str, edition: int) -> bool:
    return bool(re.match(r"(?:projet de )?loi de finances pour %d\b(?!\s*rectificative)" % edition, txt, re.I))


def troncons_senat(lignes: list[tuple[str, str]], edition: int) -> list[list[int]]:
    """Suites d'indices de lignes consacrees au projet de loi de finances : de l'intitule « Loi de finances pour AAAA »
    au point suivant de l'ordre du jour ; un changement de presidence (titre_S1 « Presidence de ») ne coupe pas le point.
    « Loi de finances de fin de gestion pour 2025 » n'est pas le projet de loi de finances de l'annee."""
    runs, cur, dedans = [], [], False
    for k, (typ, txt) in enumerate(lignes):
        if typ == "S1" and not re.match(r"pr[ée]sidence de", txt, re.I):
            if cur:
                runs.append(cur)
            cur, dedans = [], tete_plf(txt, edition)
        if dedans:
            cur.append(k)
    if cur:
        runs.append(cur)
    return runs


F_SEN = [  # (motif, statut) : formules du compte rendu integral du Senat, citees verbatim ; {a} = apostrophe
    (r"Je mets aux voix l{a}article (\d+), modifié\. \(L{a}article \1 est adopté\.\)", "adopte_modifie"),
    (r"Je mets aux voix l{a}article (\d+)\. \(L{a}article \1 est adopté\.\)", "adopte"),
    (r"Je mets aux voix l{a}article (\d+)(?:, modifié)?\. \(L{a}article \1 n{a}est pas adopté\.\)", "non_adopte"),
    (r"Je mets aux voix l{a}article (\d+)(, modifié)?\.(?:(?!Je mets aux voix).){0,1500}?résultat du scrutin n° ?\d+ ?:"
     r"(?:(?!Je mets aux voix).){0,300}?Le Sénat (a adopté|n{a}a pas adopté)\.", "scrutin"),
    (r"[Ee]n conséquence, l{a}article (\d+) est supprimé", "supprime"),
    (r"\(L{a}article (\d+) est supprimé\.\)", "supprime"),
    (r"[Ee]n conséquence, l{a}article (\d+) est ainsi rédigé", "redige"),
]
F_RESERVE = r"l{a}article (\d+)\b[^.]{0,80}\best réservé"
# Premiere partie et ensemble : « Je mets aux voix, modifié, l'ensemble de la première partie du projet de loi de finances
# pour 2026. » (3/12/2025) ; « le Sénat va maintenant procéder au vote sur l'ensemble du projet de loi de finances pour
# 2026, modifié. » (15/12/2025, scrutin a la tribune, d'ou la longueur admise jusqu'au resultat).
F_PREMIERE_SEN = (r"(?:Je mets aux voix(?:, modifié,)?|procéder au vote sur) l{a}ensemble de la première partie du projet de loi "
                  r"de finances pour %d(?:, modifiée?)?\.(?:(?!Je mets aux voix).){0,2500}?Le Sénat (a adopté|n{a}a pas adopté)\.")
F_PREMIERE_SEN2 = r"\(L{a}ensemble de la première partie du projet de loi de finances pour %d(?:, modifié,)? (est adopté|n{a}est pas adopté)\.\)"
F_ENSEMBLE_SEN = r"(?:Je mets aux voix(?:, modifié,)?|procéder au vote sur) l{a}ensemble du projet de loi de finances pour %d\b"
# Un article additionnel ou insere (« 3 sexies », « 34 bis », « 34 A ») n'est pas l'article dont il porte le numero.
SUFFIXE_ARTICLE = r"(?:er)?\s+(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|[A-Z])\b"
F_VOTE_UNIQUE = r"article 44, alinéa 3, de la Constitution"
SORTS = {"adopte": "adopté", "adopte_modifie": "adopté modifié", "rejete": "rejeté", "retire": "retiré", "tombe": "tombé",
         "non_soutenu": "non soutenu"}


def _f(motif: str) -> str:
    return motif.replace("{a}", APOS)


def sort_amendement(S: str, num: str) -> list[tuple[int, str, str]]:
    """[(position, sort, citation)] des formules qui disent le sort de l'amendement `num` dans le texte S."""
    n = re.escape(num) + r"(?: rectifié(?: bis| ter| quater| quinquies| sexies| septies)?)?"
    motifs = [
        (r"Je mets aux voix l{a}amendement n[°o] ?%s, modifié\. \(L{a}amendement est adopté\.\)" % n, "adopte_modifie"),
        (r"Je mets aux voix l{a}amendement n[°o] ?%s\. \(L{a}amendement est adopté\.\)" % n, "adopte"),
        (r"Je mets aux voix l{a}amendement n[°o] ?%s(?:, modifié)?\. \(L{a}amendement n{a}est pas adopté\.\)" % n, "rejete"),
        (r"Je mets aux voix les amendements identiques nos? [^.()]*?(?<![\w-])%s(?![\w-])[^.()]*\. \(Les amendements sont adoptés\.\)" % n,
         "adopte"),
        (r"Je mets aux voix les amendements identiques nos? [^.()]*?(?<![\w-])%s(?![\w-])[^.()]*\. \(Les amendements ne sont pas adoptés\.\)" % n,
         "rejete"),
        (r"Je mets aux voix l{a}amendement n[°o] ?%s(?:, modifié)?\.(?:(?!Je mets aux voix).){0,1500}?résultat du scrutin n° ?\d+ ?:"
         r"(?:(?!Je mets aux voix).){0,300}?Le Sénat a adopté\." % n, "adopte"),
        (r"Je mets aux voix l{a}amendement n[°o] ?%s(?:, modifié)?\.(?:(?!Je mets aux voix).){0,1500}?résultat du scrutin n° ?\d+ ?:"
         r"(?:(?!Je mets aux voix).){0,300}?Le Sénat n{a}a pas adopté\." % n, "rejete"),
        (r"L{a}amendement n[°o] ?%s est retiré\." % n, "retire"),
        (r"L{a}amendement n[°o] ?%s n{a}est pas soutenu\." % n, "non_soutenu"),
        (r"(?:l{a}amendement n[°o] ?%s|amendements nos? [^.()]{0,400}?(?<![\w-])%s(?![\w-])[^.()]{0,400}?) n{a}(?:a|ont) plus d{a}objet"
         % (n, n), "tombe"),
    ]
    return sorted((m.start(), s, m.group(0)) for mo, s in motifs for m in re.finditer(_f(mo), S))


def extraire_senat(lignes: list[tuple[str, str]], suivis_: set[int], edition: int, amdts: dict | None = None) -> dict:
    """Resultats d'une seance du Senat, dans l'ordre du compte rendu (une seconde deliberation vient apres le premier
    vote) : articles suivis, premiere partie, sort des amendements de commission `amdts` ({numero: article}), et ce qui
    BLOQUE (formule inconnue autour d'un article suivi, premiere partie non adoptee, vote sur l'ensemble, vote unique,
    article du dossier hors du point de l'ordre du jour)."""
    res = {"articles": [], "premiere": None, "amendements": [], "bloquants": [], "ouverture": None, "plf": False}
    dossier = "pjlf%d" % edition
    dans = set(k for run in troncons_senat(lignes, edition) for k in run)
    # Temoin structurel : la navigation nomme le dossier du texte ; elle doit concorder avec le point de l'ordre du jour.
    # Placee juste avant un intitule (titre_S1), elle est celle de ce point ; sinon, celle de l'article qui precede
    # (temoin du 3/12/2025 : 58 navigations, toutes « pjlf2026 », quatre devant l'intitule du point).
    for k, (typ, txt) in enumerate(lignes):
        if typ == "NAV":
            dedans = (k + 1 in dans) if k + 1 < len(lignes) and lignes[k + 1][0] == "S1" else (k in dans)
            if txt == dossier and not dedans:
                res["bloquants"].append("article du dossier %s hors du point « Loi de finances pour %d » (ligne %d)" % (dossier, edition, k))
            if dedans and txt != dossier:
                res["bloquants"].append("navigation vers %s dans le point « Loi de finances pour %d » (ligne %d)" % (txt, edition, k))
    for ri, run in enumerate(troncons_senat(lignes, edition)):
        res["plf"] = True
        parts, arts, pos = [], [], 0
        for k in run:
            typ, txt = lignes[k]
            if typ == "NAV":
                continue
            if typ == "ART":
                arts.append((pos, numero_article(txt)))
            parts.append(txt)
            pos += len(txt) + 1
        S = " ".join(parts)
        if res["ouverture"] is None and len(run) > 1:
            res["ouverture"] = " ".join(lignes[k][1] for k in run[:2] if lignes[k][0] != "NAV")
        couverts, debuts = [], set()
        for motif, statut in F_SEN:
            for m in re.finditer(_f(motif), S):
                n = int(m.group(1))
                couverts.append((m.start(), m.end()))
                if n not in suivis_ or (statut == "scrutin" and m.start() in debuts):
                    continue
                debuts.add(m.start())
                st = statut
                if statut == "scrutin":
                    adopte = m.group(3) == "a adopté"
                    st = ("adopte_modifie" if m.group(2) else "adopte") if adopte else "non_adopte"
                res["articles"].append({"article": n, "statut": st, "citation": m.group(0), "_pos": (ri, m.start())})
        for m in re.finditer(_f(F_RESERVE), S):
            couverts.append((m.start(), m.end()))

        def couvert(i):
            return any(a <= i < b for a, b in couverts)
        verbe = r"\b(?:adoptée?s?|supprimée?s?|rédigée?s?|rejetée?s?|réservée?s?|retirée?s?|maintenue?s?|rétablie?s?)\b"
        for motif in (r"\(L{a}article (\d+)\b[^)]*\)", r"[Ee]n conséquence, l{a}article (\d+)\b[^.]*",
                      r"Je mets aux voix l{a}article (\d+)\b", r"\(Les articles [^)]*\)"):
            for m in re.finditer(_f(motif), S):
                if m.group(0).startswith("(") and not re.search(verbe, m.group(0)):
                    continue  # parenthese sans verbe de resultat : propos d'un orateur, pas une decision
                if not motif.startswith(r"\(Les") and re.match(SUFFIXE_ARTICLE, S[m.end(1):]):
                    continue  # « l'article 3 sexies » : un autre article que le 3
                nums = {int(x) for x in re.findall(r"\b(\d+)\b(?!%s)" % SUFFIXE_ARTICLE[len("(?:er)?"):], m.group(0))} \
                    if motif.startswith(r"\(Les") else {int(m.group(1))}
                if nums & suivis_ and not couvert(m.start()):
                    res["bloquants"].append("formule non reconnue : « %s »" % m.group(0)[:200])
        for m in re.finditer(r"\(Adopté\.\)", S):
            art = next((a for p_, a in reversed(arts) if p_ <= m.start()), None)
            if art in suivis_:
                res["bloquants"].append("article %d adopté sans vote nommé (« (Adopté.) ») : à qualifier" % art)
        p = re.search(_f(F_PREMIERE_SEN) % edition, S) or re.search(_f(F_PREMIERE_SEN2) % edition, S)
        if p:
            if p.group(1) in ("a adopté", "est adopté"):
                res["premiere"] = {"statut": "adoptee", "citation": p.group(0)}
            else:
                res["bloquants"].append("première partie NON adoptée par le Sénat : « %s »" % p.group(0)[-200:])
        if re.search(_f(F_ENSEMBLE_SEN) % edition, S):
            res["bloquants"].append("vote sur l'ensemble du projet de loi de finances : frise, saisine de la commission mixte "
                                    "paritaire et pages à écrire à la main, puis étape « senat_ensemble » au registre")
        if re.search(F_VOTE_UNIQUE, S):
            res["bloquants"].append("vote unique (article 44, alinéa 3, de la Constitution) : à qualifier")
        for num, art in (amdts or {}).items():
            for pos_, s, cit in sort_amendement(S, num):
                res["amendements"].append({"amendement": num, "article": art, "sort": s, "citation": cit, "_pos": (ri, pos_)})
    for liste in (res["articles"], res["amendements"]):
        liste.sort(key=lambda x: x["_pos"])  # ordre du compte rendu : point de l'ordre du jour, puis position
        for x in liste:
            del x["_pos"]
    return res


def seances_senat(page: str) -> list[dict]:
    """Index mensuel des comptes rendus integraux du Senat (seances/sAAAAMM/sAAAAMM.html) : date, numero de seance,
    version (« version Provisoire » sinon definitive), adresse de la page unique."""
    out = []
    for m in re.finditer(r'href="(s(\d{8})/st\d{8}000\.html)">\s*([^<]*?)\(séance n°(?:&nbsp;|\s)*(\d+)\)\s*</a>(.*?)</ul>', page, re.S):
        d = m.group(2)
        iso = "%s-%s-%s" % (d[:4], d[4:6], d[6:])
        out.append({"date": iso, "numero": int(m.group(4)), "provisoire": "Provisoire" in m.group(5),
                    "url": "%s/seances/s%s/s%s/s%s_mono.html" % (SENAT, d[:6], d, d)})
    return sorted(out, key=lambda x: x["numero"])


def cle_senat(date: str) -> str:
    return "SENAT-%s" % date


def transmission(t: str) -> dict | None:
    m = re.search(r"Texte n° ?(\d+) \((\d{4}-\d{4})\) transmis au Sénat le (1er|\d{1,2}) (%s) (\d{4})" % "|".join(MOIS_NOMS), t)
    if not m:
        return None
    j = 1 if m.group(3) == "1er" else int(m.group(3))
    return {"numero": int(m.group(1)), "session": m.group(2), "citation": m.group(0),
            "date": dt.date(int(m.group(5)), MOIS_NOMS.index(m.group(4)) + 1, j).isoformat()}


def amendements_commission(brut: bytes, suivis_: set[int]) -> list[dict]:
    """Jeu complet des amendements du texte (CSV Ameli, tabulations, en-tete « sep= ») : ceux « au nom de la commission des
    finances » sur un article suivi. Le dispositif sert a reconnaitre une suppression ; il n'est pas cite (la page de
    l'amendement l'est)."""
    try:
        t = brut.decode("utf-8")
    except UnicodeDecodeError:
        t = brut.decode("cp1252")
    lignes = t.splitlines()
    if lignes and lignes[0].startswith("sep="):
        lignes = lignes[1:]
    r = list(csv.reader(io.StringIO("\n".join(lignes)), delimiter="\t"))
    if not r:
        return []
    tete = [x.strip() for x in r[0]]
    for c in ("Numéro", "Subdivision", "Au nom de", "Dispositif", "Url amendement"):
        if c not in tete:
            raise ValueError("jeu d'amendements : colonne « %s » absente (format change ?)" % c)
    out = []
    for row in r[1:]:
        x = dict(zip(tete, [y.strip() for y in row]))
        m = re.match(r"Article (\d+)$", x.get("Subdivision", ""))
        if not m or int(m.group(1)) not in suivis_ or x.get("Au nom de", "").lower() != "commission des finances":
            continue
        disp = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x.get("Dispositif", "")))).strip()
        url = x.get("Url amendement", "")
        out.append({"amendement": x["Numéro"], "article": int(m.group(1)), "suppression": disp == "Supprimer cet article.",
                    "url": ("https:" + url) if url.startswith("//") else url, "sort": x.get("Sort", "")})
    return out


def frontiere(listing: list[dict], lues: set, etat_au: str) -> str | None:
    """Derniere date de seance telle que toutes les seances du Senat, de la premiere posterieure a l'etat jusqu'a elle,
    sont publiees (numeros consecutifs dans l'index) ET lues ; None si rien n'avance."""
    avant = [s["numero"] for s in listing if s["date"] < etat_au]
    attendu = (max(avant) + 1) if avant else None
    f = None
    for s in [s for s in listing if s["date"] >= etat_au]:
        if attendu is not None and s["numero"] != attendu:
            break
        if cle_senat(s["date"]) not in lues:
            break
        f, attendu = s["date"], s["numero"] + 1
    return f


def mois_entre(debut: str, fin: dt.date) -> list[str]:
    d = dt.date.fromisoformat(debut).replace(day=1)
    out = []
    while d <= fin:
        out.append("%04d%02d" % (d.year, d.month))
        d = (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
    return out


def archiver(k: str, contenu: str, ecrire: bool) -> tuple[str, str]:
    ARCHIVE.mkdir(exist_ok=True)
    if ecrire:
        (ARCHIVE / ("%s.txt" % k)).write_text(contenu, encoding="utf-8", newline="\n")
    return "comptes_rendus/%s.txt" % k, hashlib.sha256(contenu.encode("utf-8")).hexdigest()


def passer_senat(v: dict, ecrire: bool, tickets: list, aujourdhui: dt.date | None = None) -> bool:
    ed, change = v["edition"], False
    aujourdhui = aujourdhui or dt.date.today()
    # 1. Transmission du texte : dossier legislatif.
    tr = etape(v, "senat_transmis")
    if not tr:
        brut = lire_url(DOSLEG % ed)
        t = texte(brut.decode("utf-8", "replace"))
        x = transmission(t)
        if x:
            k = "SENAT-DOSLEG-%s" % aujourdhui.isoformat()
            chemin, sha = archiver(k, t, ecrire)
            v["seances"][k] = {"date": aujourdhui.isoformat(), "assemblee": "Sénat",
                               "seance": "dossier législatif du projet de loi de finances pour %d, lu le %s" % (ed, date_longue(aujourdhui.isoformat())),
                               "url": DOSLEG % ed, "sha256_html": hashlib.sha256(brut).hexdigest(), "texte": chemin, "sha256_texte": sha}
            tr = {"etape": "senat_transmis", "seance": k, "citation": x["citation"], "date": x["date"],
                  "texte_senat": "n° %d (%s)" % (x["numero"], x["session"])}
            v.setdefault("etapes", []).append(tr)
            change = True
            print("Senat : transmission lue -- « %s »" % x["citation"])
        else:
            print("Senat : transmission non encore inscrite au dossier legislatif")
            if v.get("senat", {}).get("debut", "9999") <= aujourdhui.isoformat():
                tickets.append(("Senat, transmission du texte non lue (%s)" % aujourdhui.isoformat(),
                                "Le dossier legislatif ne porte pas « Texte n° ... transmis au Senat le ... » alors que "
                                "l'examen devait commencer le %s : verifier le canal." % v["senat"]["debut"], False))
            return change
    # 2. Comptes rendus integraux des seances, depuis l'etat.
    lues = set(v.get("veille_seances_lues", []))
    listing = []
    for ym in mois_entre((dt.date.fromisoformat(v["etat_au"]) - dt.timedelta(days=10)).isoformat(), aujourdhui):
        try:
            listing += seances_senat(lire_url("%s/seances/s%s/s%s.html" % (SENAT, ym, ym)).decode("utf-8", "replace"))
        except Exception as e:  # noqa: BLE001 -- un mois sans seance publiee repond 404
            print("  index %s : %s" % (ym, e))
    nouvelles = [s for s in listing if s["date"] >= v["etat_au"] and cle_senat(s["date"]) not in lues]
    print("Senat : seances listees : %d ; nouvelles depuis le %s : %d" % (len(listing), v["etat_au"], len(nouvelles)))
    amdts = {c["amendement"]: c["article"] for c in v.get("commission_senat", [])}
    S_ = suivis(v)
    for s in nouvelles:
        k = cle_senat(s["date"])
        brut = lire_url(s["url"])
        b = brut.decode("utf-8", "replace")
        L = lignes_senat(b)
        tete = texte(b[:b.find("<!-- START : cri -->")]) if "<!-- START : cri -->" in b else ""
        prov = "version provisoire" in tete.lower()
        jour = dt.date.fromisoformat(s["date"])
        titre_ok = re.search(r"Séance du %s %s %d" % ("1er" if jour.day == 1 else jour.day, MOIS_NOMS[jour.month - 1], jour.year), tete)
        if not L or not titre_ok:
            tickets.append(("Senat, compte rendu illisible (%s)" % k, "Seance du %s (n° %d) : contenu ou titre non reconnu "
                            "(%s) -- la date de l'etat s'arrete avant elle." % (s["date"], s["numero"], s["url"]), True))
            continue
        r = extraire_senat(L, S_, ed, amdts)
        if r["bloquants"]:
            tickets.append(("Senat, seance a qualifier (%s)" % k, "Seance du %s (n° %d, %s) : %s -- rien n'est integre de cette "
                            "seance et la date de l'etat s'arrete avant elle ; apres qualification, ajouter %s a "
                            "veille_seances_lues." % (s["date"], s["numero"], s["url"], " | ".join(r["bloquants"][:6]), k), True))
            continue
        nouveaux = [dict(a, seance=k) for a in r["articles"]
                    if not any(x["article"] == a["article"] and x["seance"] == k and x["statut"] == a["statut"] for x in v["articles"])]
        sorts = [dict(a, seance=k) for a in r["amendements"]
                 if not any(x["amendement"] == a["amendement"] and x["seance"] == k for x in v.get("amendements_senat", []))]
        etapes_ = []
        if r["premiere"] and not etape(v, "senat_premiere_partie_adoptee"):
            etapes_.append({"etape": "senat_premiere_partie_adoptee", "seance": k, "citation": r["premiere"]["citation"]})
        if r["plf"] and not etape(v, "senat_discussion") and r["ouverture"]:
            etapes_.append({"etape": "senat_discussion", "seance": k, "citation": r["ouverture"]})
        if nouveaux or sorts or etapes_:
            chemin, sha = archiver(k, lignes_archive(L), ecrire)
            v["seances"][k] = {"date": s["date"], "assemblee": "Sénat",
                               "seance": "séance du %s (n° %d), compte rendu intégral%s" % (date_longue(s["date"]), s["numero"],
                                                                                          ", version provisoire" if prov else ""),
                               "numero": s["numero"], "version": "provisoire" if prov else "definitive",
                               "url": s["url"], "sha256_html": hashlib.sha256(brut).hexdigest(), "format": "lignes",
                               "texte": chemin, "sha256_texte": sha}
            for a in nouveaux:
                v["articles"].append(a)
                print("  %s : art. %d %s -- « %s »" % (k, a["article"], a["statut"], a["citation"][:160]))
            for a in sorts:
                v.setdefault("amendements_senat", []).append(a)
                print("  %s : amendement %s (art. %d) %s -- « %s »" % (k, a["amendement"], a["article"], a["sort"], a["citation"][:160]))
            for e in etapes_:
                v.setdefault("etapes", []).append(e)
                print("  %s : etape %s -- « %s »" % (k, e["etape"], e["citation"][:160]))
            change = True
        # Article d'une page vote sans que l'amendement de la commission qui le visait ait un sort lu : la page n'en dira
        # rien (le generateur ne l'invente pas) ; ticket pour le qualifier.
        for a in nouveaux:
            for num, art in amdts.items():
                if art == a["article"] and not any(x["amendement"] == num for x in v.get("amendements_senat", [])):
                    tickets.append(("Senat, sort de l'amendement %s non lu" % num,
                                    "Art. %d vote le %s (%s) ; le sort de l'amendement %s de la commission des finances n'est "
                                    "pas lu dans le compte rendu : la page ne le mentionne pas." % (art, s["date"], a["statut"], num), False))
        lues.add(k)
        print("  %s (n° %d%s) : lue%s" % (k, s["numero"], ", provisoire" if prov else "", "" if r["plf"] else ", sans le projet de loi de finances"))
    if sorted(lues) != v.get("veille_seances_lues", []):
        v["veille_seances_lues"] = sorted(lues)
        change = True
    f = frontiere(listing, lues, v["etat_au"])
    if f and f > v["etat_au"]:
        v["etat_au"] = f
        change = True
        print("Senat : etat au %s (seances lues sans trou dans la numerotation)" % f)
    trou = [s for s in listing if s["date"] >= v["etat_au"] and cle_senat(s["date"]) not in lues]
    if trou and (aujourdhui - dt.date.fromisoformat(trou[0]["date"])).days > 3:
        tickets.append(("Senat, seance non integree depuis plus de trois jours (%s)" % cle_senat(trou[0]["date"]),
                        "La date de l'etat reste au %s." % v["etat_au"], False))
    # 3. Amendements de la commission des finances (jeu Ameli du texte transmis) : seconde partie et nouveaux depots.
    num = re.match(r"n° (\d+) \((\d{4}-\d{4})\)", tr.get("texte_senat", ""))
    if num:
        base = "%s/amendements/%s/%s/" % (SENAT, num.group(2), num.group(1))
        try:
            jeu = amendements_commission(lire_url(base + "jeu_complet_%s_%s.csv" % (num.group(2), num.group(1))), S_)
        except Exception as e:  # noqa: BLE001
            tickets.append(("Senat, jeu des amendements illisible", "%s : %s" % (base, e), False))
            jeu = []
        connus = {c["amendement"] for c in v.get("commission_senat", [])}
        for a in jeu:
            if a["amendement"] in connus:
                continue
            if not a["suppression"]:
                tickets.append(("Senat, amendement %s de la commission (art. %d)" % (a["amendement"], a["article"]),
                                "Amendement de la commission des finances sur l'article %d, autre qu'une suppression : a "
                                "qualifier pour la page (%s)." % (a["article"], a["url"]), False))
                continue
            brut = lire_url(a["url"])
            t = texte(brut.decode("utf-8", "replace"))
            m = re.search(r"N° %s (1er|\d{1,2}) (%s) (\d{4}) AMENDEMENT" % (re.escape(a["amendement"]), "|".join(MOIS_NOMS)), t)
            c1 = re.search(r"au nom de la commission des finances ARTICLE %d Supprimer cet article\." % a["article"], t)
            if not m or not c1:
                tickets.append(("Senat, amendement %s de la commission (art. %d)" % (a["amendement"], a["article"]),
                                "Page de l'amendement non reconnue (%s)." % a["url"], False))
                continue
            k = "SENAT-AMDT-%s" % a["amendement"]
            chemin, sha = archiver(k, t, ecrire)
            jour = dt.date(int(m.group(3)), MOIS_NOMS.index(m.group(2)) + 1, 1 if m.group(1) == "1er" else int(m.group(1)))
            v["seances"][k] = {"date": jour.isoformat(), "assemblee": "Sénat",
                               "seance": "amendement n[°o] ?%s de la commission des finances, page lue le %s" % (a["amendement"], date_longue(aujourdhui.isoformat())),
                               "url": a["url"], "sha256_html": hashlib.sha256(brut).hexdigest(), "texte": chemin, "sha256_texte": sha}
            v.setdefault("commission_senat", []).append({"article": a["article"], "amendement": a["amendement"], "seance": k,
                                                         "statut": "suppression_adoptee", "source": "ameli",
                                                         "citations": [m.group(0), c1.group(0)]})
            change = True
            print("Senat : amendement %s (commission) : suppression de l'article %d -- « %s »" % (a["amendement"], a["article"], c1.group(0)))
    return change


def passer(ecrire: bool) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    v = json.loads(REGISTRE.read_text(encoding="utf-8"))
    if v.get("termine"):
        print("Registre clos (loi promulguee) : veille terminee.")
        return 0
    tickets = []
    an = []
    change = passer_an(v, ecrire, an)
    tickets += [(x.split(" : ")[0], x, False) for x in an]
    change = passer_senat(v, ecrire, tickets) or change
    for titre, detail, bloquant in tickets:
        # Titre (unique : un ticket par fait) puis detail, separes par une tabulation (format de maj-sources.yml).
        sys.stdout.buffer.write(("VEILLE\tProjet de loi de finances : %s\t%s%s\n" % (
            titre, detail, " [BLOQUANT : la date de l'etat ne passe pas cette seance]" if bloquant else "")).encode("utf-8"))
    if change and ecrire:
        REGISTRE.write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("Registre ecrit : etat au %s" % v["etat_au"])
    elif change:
        print("(releve) changements possibles : etat au %s ; rien ecrit" % v["etat_au"])
    else:
        print("Aucun changement.")
    return 0


# Temoin du Senat (19/11/2026) : seance du 3 decembre 2025, projet de loi de finances pour 2026 (premiere lecture au
# Senat), articles des collectivites. Attendu etabli a la main sur le compte rendu integral et confronte au texte adopte
# par le Senat le 15/12/2025 (n° 29, 2025-2026 : articles 31 a 36 et 40 presents, « Articles 41 et 42 (Supprimés) »,
# article 33 reecrit « I a III. - (Supprimés) IV. - ... »). Le compte rendu analytique de la meme seance porte l'article 40
# « modifie, n'est pas adopte » : c'est pourquoi il n'est pas lu. Archive : sous-suite EXACTE (1 317 lignes sur 10 343,
# aucune modifiee) des lignes de la page (SHA-256 de la page ef3158d9c9ee22c71353b13f2d381af7d7fc77b967d1b5a85c0d1e505ac9ad07,
# lue le 19/11/2026) : intitules, numeros des points, mentions d'articles, navigations et deux lignes autour de chaque
# formule ; l'extracteur y trouve exactement ce qu'il trouve dans la page complete (verifie a la construction).
TEMOIN_SENAT = {"url": SENAT + "/seances/s202512/s20251203/s20251203_mono.html", "edition": 2026,
                "archive": "TEMOIN-SENAT-2025-12-03.txt",
                "sha256": "2e900b39d8200e0b88fcd577c12db09a7ff5d946ac47865ae7b96627aed392fb",
                "suivis": {31, 32, 33, 34, 35, 36, 40, 41, 42},
                "attendu": {(31, "adopte_modifie"), (32, "adopte_modifie"), (33, "redige"), (34, "adopte_modifie"),
                            (35, "adopte_modifie"), (36, "adopte_modifie"), (40, "adopte"), (41, "supprime"), (42, "supprime")},
                "amendements": {"I-22": 33}, "sorts": {("I-22", "adopte")}}


def temoin_senat(source: str = "archive") -> int:
    """`archive` : relit le compte rendu archive dans le depot (texte « lignes ») ; `ligne` : telecharge la page du Senat
    et la lit par le meme chemin que la veille (le canal et la structure n'ont pas change). Puis temoin NEGATIF : une
    formule inconnue sur un article suivi doit bloquer la seance, sans aucune entree."""
    T = TEMOIN_SENAT
    if source == "ligne":
        L = lignes_senat(lire_url(T["url"]).decode("utf-8", "replace"))
    else:
        brut = (ARCHIVE / T["archive"]).read_bytes()
        if hashlib.sha256(brut).hexdigest() != T["sha256"]:
            print("Temoin Senat : archive %s alteree (empreinte)" % T["archive"])
            return 1
        L = lire_lignes(brut.decode("utf-8"))
    r = extraire_senat(L, T["suivis"], T["edition"], T["amendements"])
    trouve = {(a["article"], a["statut"]) for a in r["articles"]}
    sorts = {(a["amendement"], a["sort"]) for a in r["amendements"]}
    manque, trop = T["attendu"] - trouve, trouve - T["attendu"]
    ok = not manque and not trop and not r["bloquants"] and sorts == T["sorts"]
    print("Temoin Senat (%s) : attendu %d, retrouve %d, manquant %s, en trop %s, sorts %s, bloquants %d" % (
        source, len(T["attendu"]), len(trouve & T["attendu"]), sorted(manque), sorted(trop), sorted(sorts), len(r["bloquants"])))
    # Temoin negatif : « (L'article 40 est adopté.) » devient une formule inconnue.
    L2 = [(typ, txt.replace("(L’article 40 est adopté.)", "(L’article 40 est réputé adopté.)")) for typ, txt in L]
    r2 = extraire_senat(L2, T["suivis"], T["edition"], T["amendements"])
    mord = any("article 40" in b for b in r2["bloquants"]) and not any(a["article"] == 40 for a in r2["articles"])
    print("Temoin negatif Senat : formule inconnue sur l'article 40 -> %s" % ("seance bloquee, aucune entree pour l'article 40"
                                                                            if mord else "NON DETECTEE"))
    return 0 if ok and mord else 1


def temoin() -> int:
    """Le releve doit retrouver, dans le compte rendu archive du 19/10, les decisions deja au registre (Assemblee) ;
    et, au Senat, les decisions connues du 3/12/2025 (archive du depot, puis page en ligne)."""
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
    an = 1 if manque or trop else 0
    return max(an, temoin_senat("archive"), temoin_senat("ligne"))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "releve"
    if cmd == "temoin-senat":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.exit(temoin_senat(sys.argv[2] if len(sys.argv) > 2 else "archive"))
    sys.exit(temoin() if cmd == "temoin" else passer(cmd == "integrer"))
