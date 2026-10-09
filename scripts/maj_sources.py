#!/usr/bin/env python3
"""maj_sources.py -- module de mise à jour des données : détecter une édition nouvelle, l'archiver, relancer les pages.

Décision de l'auteur (02/10/2026) : « un module qui, à chaque mise à jour d'une donnée que nous utilisons, déclenche la
mise à jour et la réécriture des pages ». UN registre (data/sources_maj.json), UN script, UN workflow quotidien
(.github/workflows/maj-sources.yml). Les pages se réécrivent d'elles-mêmes parce que leur prose est faite de jetons ;
ce module leur apporte l'édition nouvelle et laisse les gardes des générateurs décider.

    python scripts/maj_sources.py etat        tableau des sources : édition lue, prochaine attendue, retard
    python scripts/maj_sources.py detecter    cherche les éditions nouvelles, n'écrit rien
    python scripts/maj_sources.py integrer    détecte, archive, inscrit au registre, relance les générateurs
    python scripts/maj_sources.py essai       TÉMOIN POSITIF : chaque détecteur retrouve-t-il l'édition déjà connue ?
    python scripts/maj_sources.py veille      sources en veille (page lycée) : éditions nouvelles à signaler, rien écrit
    python scripts/maj_sources.py sorties     chemins à commiter (pour le workflow)
    python scripts/maj_sources.py controle    sortie 1 si une édition attendue n'est pas intégrée après sa fenêtre

CE QUE LE MODULE COUVRE. Les sources en mode « fichier » du registre : note du SIES sur la licence, fiches de l'État de
l'enseignement supérieur, Insee Première sur l'empreinte carbone. Les sources en mode « api » (dossier dette) gardent
leur générateur et leur workflow, qui interrogent déjà la source à chaque passage ; elles figurent au registre pour le
tableau d'état. Les fondre dans ce workflow est une suite possible, non faite ici.

RÈGLE D'ADOPTION. Une édition n'est adoptée que si TOUS les générateurs concernés passent en --check (témoins et
gardes de prose). Sinon : registre, empreintes et pièces sont remis dans leur état d'avant, sortie 1, et le workflow
ouvre un ticket. Une phrase que la donnée dément se réécrit à la main ; elle ne se publie jamais.

UN DÉTECTEUR SANS TÉMOIN EST RÉPUTÉ ABSENT : `essai` retire de sa copie du registre la dernière édition connue et
vérifie que chaque détecteur la retrouve à la source, octet pour octet quand la pièce est un fichier.

LIMITES DITES. Les pages du ministère de l'Enseignement supérieur refusent les scripts : la note du SIES se détecte par
l'archive publique de sa page (web.archive.org), donc avec le retard de cette archive ; faute de mieux, `controle`
signale une fois la fenêtre passée. L'Insee Première se retrouve par le flux des parutions de l'Insee, qui ne garde
que les parutions récentes : ce maillon ne se teste qu'au jour d'une parution réelle (`integrer --publication URL`
désigne la pièce à la main).

MODE « VEILLE » (page lycée, 07/10/2026, arbitrage PRO-20261007-160259, point 11). Le générateur de
/manque-t-il-des-professeurs/ lit un extrait FIGÉ calculé hors dépôt (test décisif de l'auteur : une vingtaine de pièces,
dont des PDF lus par position et validés à la main) : l'adoption automatique n'y est ni légère ni sûre. Le module y fait
donc le seul geste que le défaut constaté exigeait -- deux publications parues après l'édition lue avaient été manquées :
il DÉTECTE l'édition nouvelle, la valide par son contenu (racine XML du catalogue, titre et DOI de la note, tableaux des
concours, observation de l'OCDE), et la SIGNALE par un ticket, un seul par édition (titre unique) :
    python scripts/maj_sources.py veille      une ligne « VEILLE<TAB>titre<TAB>détail » par édition nouvelle
L'intégration reste humaine : relancer extrait.py dans le dossier de recherche, recopier l'extrait et son empreinte,
relancer le générateur, puis porter l'édition lue (« lu ») au registre. Les détecteurs de veille ont leur témoin dans
`essai`, comme les autres.

CONDITION DE MORT (R2), en prédicat : ce module disparaît si aucune source du registre n'est plus en mode « fichier »
ni « veille », ou si deux années passent sans qu'il ait adopté ou signalé une seule édition
(`git log -- data/sources_maj.json`).
"""
from __future__ import annotations

import hashlib
import html
import io
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
import warnings
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "data" / "sources_maj.json"
SRC = ROOT / "scripts" / "sources_enseignants"
SUMS = SRC / "SHA256SUMS"
UA = "stephane-lalut.com (stephane@stephane-lalut.com)"
MINISTERE = "https://www.enseignementsup-recherche.gouv.fr"
EESR = "https://publication.enseignementsup-recherche.gouv.fr/eesr/FR/EESR%d_ES_%s/%s/"
SLUG_13, SLUG_09 = "l_acces_a_l_enseignement_superieur", "les_nouveaux_bacheliers_et_leur_entree_dans_les_filieres_de_l_enseignement_superieur"
MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre")
ORDRE = ["generer_parcours_licence.py", "generer_acces_superieur.py", "generer_empreinte_carbone.py", "og_enseignants.py"]


def log(msg: str) -> None:
    print(msg.encode("ascii", "replace").decode("ascii"))


class Anomalie(Exception):
    """La source a bougé mais la pièce n'a pas pu être obtenue ou reconnue : à traiter par une personne."""


def http(url: str, delai: int = 60) -> tuple[int, bytes]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=delai) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001  (réseau : on rend un code, l'appelant décide)
        # Repli sur curl quand le magasin de certificats de Python refuse un site que le système accepte (mesuré le
        # 02/10/2026 sur le poste Windows : « certificate has expired » pour le site du SDES, que curl ouvre). La
        # vérification des certificats n'est JAMAIS désactivée : c'est un autre magasin, pas une absence de contrôle.
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            try:
                r = subprocess.run(["curl", "-sL", "-m", str(delai), "-A", UA, "-w", "\n%{http_code}", url],
                                   capture_output=True, timeout=delai + 10)
                corps, _, code = r.stdout.rpartition(b"\n")
                if r.returncode == 0 and code.strip().isdigit():
                    return int(code), corps
            except Exception as e2:  # noqa: BLE001
                log("  reseau (curl) : %s (%s)" % (url[:110], e2))
        log("  reseau : %s (%s)" % (url[:110], e))
        return 0, b""


def http_archive(url: str, delai: int = 90) -> tuple[int, bytes]:
    """web.archive.org répond volontiers 503 ou 429 à un premier appel (mesuré le 02/10/2026 depuis un serveur de
    GitHub : 503 sur l'index, alors que le poste obtenait 200). Trois essais espacés ; au-delà, on rend le dernier code."""
    import time
    code, corps = 0, b""
    for attente in (0, 20, 60):
        if attente:
            time.sleep(attente)
        code, corps = http(url, delai)
        if code == 200:
            break
        log("  archive publique : code %s, nouvel essai" % code)
    return code, corps


def texte(page: bytes) -> str:
    t = page.decode("utf-8", errors="replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).replace(" ", " ")


def lire_registre() -> dict:
    return json.loads(REG.read_text(encoding="utf-8"))


def src(reg: dict, ident: str) -> dict:
    return next(x for x in reg["sources"] if x["id"] == ident)


# ------------------------------------------------------------------ détecteurs
ARCHIVE_INJOIGNABLE: list[int] = []   # codes rendus par l'archive publique quand elle ne répond pas : lus par essai()


def detecter_sies(reg: dict) -> list[dict]:
    """Cohorte suivante de la note « Parcours et réussite en licence », par l'archive publique de sa page."""
    s = src(reg, "sies-licence")
    cohorte = max(int(k) for k in s["cohortes"]) + 1
    session = cohorte + 1
    prefixe = "enseignementsup-recherche.gouv.fr/fr/parcours-et-reussite-en-licence-les-resultats-de-la-session-%d" % session
    code, corps = http_archive("https://web.archive.org/cdx/search/cdx?url=%s*&fl=original,timestamp,statuscode&filter=statuscode:200&limit=20" % prefixe)
    if code != 200:
        ARCHIVE_INJOIGNABLE.append(code)
        log("  sies-licence : archive publique injoignable (code %s), rien a conclure" % code)
        return []
    lignes = [l.split() for l in corps.decode("utf-8", "replace").splitlines() if l.strip()]
    lignes = [l for l in lignes if len(l) >= 2 and "?" not in l[0]]
    if not lignes:
        return []                                   # page pas encore archivée : pas une anomalie
    original, horodatage = lignes[-1][0], lignes[-1][1]
    code, page = http_archive("https://web.archive.org/web/%s/%s" % (horodatage, original), 120)
    if code != 200:
        raise Anomalie("sies-licence : page de la session %d archivee mais illisible (code %s)" % (session, code))
    t = page.decode("utf-8", "replace")
    liens = sorted(set(re.findall(r"(/sites/default/files/[^\"'<> ]*tableaux-nationaux[^\"'<> ]*\.xlsx)", t)))
    if not liens:
        raise Anomalie("sies-licence : page de la session %d trouvee, aucun tableur « tableaux nationaux » dedans" % session)
    code, xlsx = http(MINISTERE + liens[0], 120)
    if code != 200 or not xlsx:
        raise Anomalie("sies-licence : tableur %s injoignable (code %s)" % (liens[0], code))
    import openpyxl
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        feuilles = openpyxl.load_workbook(io.BytesIO(xlsx), read_only=True).sheetnames
    feuille = "Devenir cohorte %d" % cohorte
    if feuille not in feuilles:
        raise Anomalie("sies-licence : le tableur de la session %d n'a pas de feuille %r" % (session, feuille))
    m = re.search(r"/(\d{4})-(\d{2})/nf-sies-(\d{4})-(\d+)", liens[0])
    if not m:
        raise Anomalie("sies-licence : nom du tableur inattendu : %s" % liens[0])
    annee, mois, _, numero = m.groups()
    nom = "sies_nf%s-%s_tableaux_nationaux_cohorte%d.xlsx" % (annee, numero, cohorte)
    note = "Note Flash n° %d, %s %s" % (int(numero), MOIS[int(mois) - 1], annee)

    def inscrire(r: dict) -> None:
        src(r, "sies-licence")["cohortes"][str(cohorte)] = [nom, feuille, note]
    return [dict(source="sies-licence", quoi="cohorte %d (%s)" % (cohorte, note), pieces=[(nom, xlsx)], inscrire=inscrire)]


def fiche_eesr(annee: int, numero: str) -> tuple[str, bytes] | None:
    """Fiche 13 ou 09 de l'édition qui porte sur les bacheliers de `annee`. Validée par le titre du tableau : la page
    d'une édition absente répond 200 : un autre code dit que le site ne répond pas, jamais que la fiche manque
    (05/10/2026 : délai dépassé depuis GitHub, compté à tort comme « fiche non retrouvée »)."""
    n = annee - 2005
    code, page = http(EESR % (n, numero, SLUG_13 if numero == "13" else SLUG_09))
    if code != 200:
        raise Injoignable("eesr-acces : fiche %s des bacheliers %d, code %s" % (numero, annee, code))
    t = texte(page)
    marque = ("Nouveaux bacheliers %d inscrits dans les différentes filières" % annee) if numero == "13" \
        else ("poursuivants ou non par origine sociale en %d" % annee)
    if marque not in t:
        return None
    nom = ("eesr%d_fiche13_acces_enseignement_superieur_bacheliers%d.html" if numero == "13" else "eesr%d_fiche09_nouveaux_bacheliers_%d.html") % (n, annee)
    return nom, page


def detecter_eesr(reg: dict) -> list[dict]:
    """Fiches nécessaires à l'année de la figure (dernière cohorte de la licence) et à son témoin (année suivante)."""
    s = src(reg, "eesr-acces")
    annee = max(int(k) for k in src(reg, "sies-licence")["cohortes"])
    out = []

    def fiche(a: int, numero: str, requise: bool) -> tuple[str, bytes] | None:
        # Fiche requise injoignable : l'adoption de la cohorte attend, avec le vrai motif. Fiche facultative
        # (témoin de l'année suivante, cherché chaque jour) : rien à conclure aujourd'hui.
        try:
            return fiche_eesr(a, numero)
        except Injoignable as e:
            if requise:
                raise Anomalie("%s : site injoignable, la cohorte %d attend sa fiche" % (e, annee))
            log("  %s : rien a conclure aujourd'hui" % e)
            return None
    for a in (annee, annee + 1):
        if str(a) not in s["fiches_acces"]:
            f = fiche(a, "13", a == annee)
            if f is None and a == annee:
                raise Anomalie("eesr-acces : fiche 13 des bacheliers %d introuvable, la figure ne peut pas suivre la cohorte %d" % (a, a))
            if f is not None:
                def inscrire(r: dict, a=a, nom=f[0]) -> None:
                    src(r, "eesr-acces")["fiches_acces"][str(a)] = [nom, "n° %d" % (a - 2005)]
                out.append(dict(source="eesr-acces", quoi="fiche 13, bacheliers %d" % a, pieces=[f], inscrire=inscrire))
    if str(annee) not in s["fiches_bac"]:
        f = fiche(annee, "09", True)
        if f is None:
            raise Anomalie("eesr-acces : fiche 09 des bacheliers %d introuvable (temoin du baccalaureat)" % annee)

        def inscrire9(r: dict, nom=f[0]) -> None:
            src(r, "eesr-acces")["fiches_bac"][str(annee)] = nom
        out.append(dict(source="eesr-acces", quoi="fiche 09, bacheliers %d" % annee, pieces=[f], inscrire=inscrire9))
    return out


def piece_insee(url: str, annee: int) -> tuple[str, bytes, str]:
    """Depuis la page d'une Insee Première : son fichier de données, validé par le titre de la figure 1."""
    code, page = http(url)
    if code != 200:
        raise Anomalie("insee-empreinte : page %s injoignable (code %s)" % (url, code))
    brut = page.decode("utf-8", "replace")
    liens = re.findall(r"(/fr/statistiques/fichier/\d+/[iI][pP]\d+\.xlsx)", brut)
    if not liens:
        raise Anomalie("insee-empreinte : aucun fichier de donnees dans %s" % url)
    code, xlsx = http("https://www.insee.fr" + liens[0])
    if code != 200 or not xlsx:
        raise Anomalie("insee-empreinte : fichier %s injoignable (code %s)" % (liens[0], code))
    import openpyxl
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        wb = openpyxl.load_workbook(io.BytesIO(xlsx), data_only=True)
    if "Figure 1" not in wb.sheetnames or not str(wb["Figure 1"]["A1"].value).strip().endswith(str(annee)):
        raise Anomalie("insee-empreinte : le fichier de %s ne porte pas la decomposition de %d" % (url, annee))
    numero = re.search(r"[iI][pP](\d+)\.xlsx", liens[0]).group(1)
    t = texte(page)
    m = re.search(r"Paru le\s*:?\s*(?:Paru le\s*)?(\d{2})/(\d{2})/(\d{4})", t)
    quand = ("%s %s" % (MOIS[int(m.group(2)) - 1], m.group(3))) if m else str(annee + 1)
    return "insee_premiere_%s_empreinte_carbone_%d.xlsx" % (numero, annee), xlsx, "Insee Première n° %s, %s" % (numero, quand)


def detecter_insee(reg: dict, publication: str | None = None) -> list[dict]:
    """Année suivante de l'empreinte : la page annuelle du SDES dit qu'elle est parue, le flux de l'Insee dit où."""
    s = src(reg, "insee-empreinte")
    annee = int(s["annee_donnees"]) + 1
    url = publication
    if not url:
        code, page = http("https://www.statistiques.developpement-durable.gouv.fr/lempreinte-carbone-de-la-france-de-1990-%d" % annee)
        if code == 0:
            # Une panne de réseau n'est pas « pas encore parue » : on le dit, et l'essai hebdomadaire guette la panne durable.
            log("  insee-empreinte : page annuelle du SDES injoignable, rien a conclure aujourd'hui")
            return []
        parue_sdes = code == 200 and ("1990 à %d" % annee) in texte(page)
        # Depuis le 07/10/2026, le SDES répond 403 (et non plus 404) pour l'année suivante : un 403 ne permet pas de
        # distinguer « absente » de « refusée au script ». On interroge alors le flux de l'Insee, voie indépendante.
        if not parue_sdes and code != 403:
            return []                               # 404 ou page d'une autre année : pas encore parue
        code, flux = http("https://www.insee.fr/fr/flux/1")
        if code == 200:
            for titre, lien in re.findall(r"<item>.*?<title>(.*?)</title>.*?<link>(.*?)</link>", flux.decode("utf-8", "replace"), flags=re.S):
                t = html.unescape(titre).replace(" ", " ")
                if re.search(r"empreinte carbone de la France en %d" % annee, t):
                    url = html.unescape(lien).strip()
                    break
        if not url and not parue_sdes:
            log("  insee-empreinte : page annuelle du SDES refusee (403), flux de l'Insee sans l'edition %d : pas encore parue" % annee)
            return []
        if not url:
            raise Anomalie("insee-empreinte : l'edition %d est parue (page du SDES), mais l'Insee Premiere n'est pas dans le flux des "
                           "parutions. Designer la piece : python scripts/maj_sources.py integrer --publication <adresse>" % annee)
    nom, xlsx, edition = piece_insee(url, annee)

    def inscrire(r: dict) -> None:
        x = src(r, "insee-empreinte")
        x.update(annee_donnees=annee, fichier=nom, edition=edition, publication=url)
    return [dict(source="insee-empreinte", quoi="donnees %d (%s)" % (annee, edition), pieces=[(nom, xlsx)], inscrire=inscrire)]


# ------------------------------------------------------------------ veille (détection et signal, sans adoption)
HAL = "https://api.archives-ouvertes.fr/search/?q=title_t:%s&fl=title_s,doiId_s,producedDate_s&rows=10&sort=producedDate_s%%20desc"
RERS = "https://rers.depp.education.fr/data/%d/index.xml"
SITEMAP_CONCOURS = "https://www.devenirenseignant.gouv.fr/sitemap.xml"
OCDE_PERSTUD = ("https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_FIN@DF_UOE_INDIC_FIN_PERSTUD,/FRA........"
                "?format=csvfilewithlabels&startPeriod=%d")
EXTRAIT_LYCEE = ROOT / "scripts" / "sources_lycee_professeurs" / "extrait.json"


class Injoignable(Exception):
    """La source ne répond pas : rien à conclure aujourd'hui (ce n'est ni « rien de nouveau » ni une anomalie)."""


def notes_hal(s: dict) -> list[tuple[str, str, str]]:
    """Notes de la DEPP déposées sur HAL dont le titre contient la phrase du registre : (DOI, date, titre), récentes
    d'abord. Validées par le titre et par le préfixe DOI des Notes d'Information, jamais par un code HTTP."""
    import urllib.parse
    code, corps = http(HAL % urllib.parse.quote('"%s"' % s["phrase_hal"]))
    if code != 200:
        raise Injoignable("%s : HAL code %s" % (s["id"], code))
    norm = lambda t: t.replace("’", "'").lower()
    out = [(d.get("doiId_s", ""), d.get("producedDate_s", ""), d["title_s"][0]) for d in json.loads(corps)["response"]["docs"]]
    out = [x for x in out if x[0].startswith("10.48464/ni-") and norm(s["phrase_hal"]) in norm(x[2])]
    if not out:
        raise Anomalie("%s : HAL ne rend plus aucune note dont le titre contient « %s » (détecteur à revoir)" % (s["id"], s["phrase_hal"]))
    return out


def catalogue_rers(annee: int) -> bool:
    """Le catalogue de la RERS interactive existe-t-il pour `annee` ? Une année absente répond 200 avec la page HTML de
    l'application : seule la racine XML <tbef> prouve l'édition."""
    code, corps = http(RERS % annee)
    if code == 0:
        raise Injoignable("lycee-rers : rers.depp.education.fr injoignable")
    return code == 200 and corps.lstrip()[:200].startswith(b"<?xml") and b"<tbef>" in corps[:400]


def tableaux_concours(page: bytes) -> dict[str, list[list[str]]]:
    """Tableaux d'une page « données statistiques des concours » : {intitulé (attribut summary): lignes de cellules}."""
    from html.parser import HTMLParser

    class P(HTMLParser):
        def __init__(self):
            super().__init__()
            self.t, self.cur, self.row, self.cell = {}, None, None, None

        def handle_starttag(self, tag, attrs):
            if tag == "table":
                self.cur = dict(attrs).get("summary", "")
                self.t[self.cur] = []
            elif tag == "tr" and self.cur is not None:
                self.row = []
            elif tag in ("td", "th") and self.row is not None:
                self.cell = ""

        def handle_endtag(self, tag):
            if tag in ("td", "th") and self.cell is not None:
                self.row.append(" ".join(self.cell.split()))
                self.cell = None
            elif tag == "tr" and self.row is not None:
                self.t[self.cur].append(self.row)
                self.row = None
            elif tag == "table":
                self.cur = None

        def handle_data(self, d):
            if self.cell is not None:
                self.cell += d
    p = P()
    p.feed(page.decode("utf-8", "replace"))
    return p.t


def page_concours(session: int) -> tuple[str, dict] | None:
    """Page du CAPES de la session, trouvée par le plan du site et validée par ses tableaux de résultats de la session."""
    code, plan = http(SITEMAP_CONCOURS)
    if code != 200:
        raise Injoignable("lycee-concours : plan du site code %s" % code)
    urls = re.findall(r"<loc>([^<]*les-donnees-statistiques-des-concours-du-capes-de-la-session-%d-\d+)</loc>" % session,
                      plan.decode("utf-8", "replace"))
    if not urls:
        return None
    code, page = http(urls[0])
    if code != 200:
        raise Anomalie("lycee-concours : page %s listée par le plan du site mais illisible (code %s)" % (urls[0], code))
    t = {k: v for k, v in tableaux_concours(page).items() if re.search(r"Capes externe bac \+ \d - %d" % session, k)}
    if not t:
        return None                                  # page annoncée, résultats pas encore en ligne
    return urls[0], t


def ocde_annees() -> dict[int, float]:
    """Dépense publique par élève du second cycle général, France, USD PPA : {année: valeur} servie par l'API de l'OCDE."""
    import csv
    code, corps = http(OCDE_PERSTUD % 2019, 180)
    if code != 200:
        raise Injoignable("lycee-ocde : API de l'OCDE code %s" % code)
    out = {}
    for d in csv.DictReader(io.StringIO(corps.decode("utf-8-sig", "replace"))):
        if (d.get("EDUCATION_LEV") == "ISCED11_34" and d.get("UNIT_MEASURE") == "USD_PPP_ST" and d.get("PRICE_BASE") == "V"
                and d.get("EXP_SOURCE") == "S13" and d.get("EXP_DESTINATION") == "INST_EDU"
                and d.get("EXPENDITURE_TYPE") == "DIR_EXP" and d.get("OBS_VALUE")):
            out[int(d["TIME_PERIOD"])] = float(d["OBS_VALUE"])
    if not out:
        raise Anomalie("lycee-ocde : l'API répond mais ne sert plus la série (dimensions changées ?)")
    return out


def veille_source(s: dict) -> list[tuple[str, str]]:
    """Éditions nouvelles d'une source en veille, au-delà de l'édition lue (« lu ») : [(titre du signal, détail)]."""
    lu = s["lu"]
    if s["id"] == "lycee-rers":
        return [("RERS %d" % (lu + 1), RERS % (lu + 1))] if catalogue_rers(lu + 1) else []
    if "phrase_hal" in s:
        notes = notes_hal(s)
        doi, quand, titre = notes[0]
        if doi == lu:
            return []
        if not any(d == lu for d, _, _ in notes):
            raise Anomalie("%s : l'édition lue %s n'est plus parmi les notes rendues par HAL" % (s["id"], lu))
        return [("%s (%s)" % (doi, quand[:10]), "%s -- https://doi.org/%s" % (titre, doi))]
    if s["id"] == "lycee-concours":
        p = page_concours(lu + 1)
        return [("concours de la session %d" % (lu + 1), p[0])] if p else []
    if s["id"] == "lycee-ocde":
        nouvelles = sorted(a for a in ocde_annees() if a > lu)
        return [("dépense par élève %d" % a, "API SDMX de l'OCDE, DF_UOE_INDIC_FIN_PERSTUD") for a in nouvelles]
    raise Anomalie("%s : source en veille sans détecteur" % s["id"])


def veille() -> int:
    """Une ligne par édition nouvelle ; le workflow en fait un ticket par titre. Une source injoignable n'est pas une
    édition absente : elle est dite, et le témoin du lundi guette la panne durable."""
    n = 0
    for s in [x for x in lire_registre()["sources"] if x["mode"] == "veille"]:
        try:
            for titre, detail in veille_source(s):
                n += 1
                # En UTF-8 sur la sortie binaire : un titre de note peut porter un caractère absent de la console cp1252.
                ligne = "VEILLE\tEdition nouvelle (%s) : %s\t%s -- a integrer a la main : %s\n" % (s["id"], titre, detail, s["integration"])
                sys.stdout.flush()
                sys.stdout.buffer.write(ligne.encode("utf-8"))
                sys.stdout.buffer.flush()
        except Injoignable as e:
            log("  %s : rien a conclure aujourd'hui" % e)
        except Anomalie as e:
            # Un détecteur en panne ne bloque pas l'adoption des autres sources : il devient un ticket, un seul.
            ligne = "VEILLE\tDetecteur de veille en panne (%s)\t%s\n" % (s["id"], e)
            sys.stdout.flush()
            sys.stdout.buffer.write(ligne.encode("utf-8"))
            sys.stdout.buffer.flush()
    log("Veille : %d edition(s) nouvelle(s) signalee(s)." % n)
    return 0


def essai_veille(verdict) -> None:
    """Témoin positif des détecteurs de veille : chacun doit retrouver à la source l'édition déjà lue."""
    extrait = json.loads(EXTRAIT_LYCEE.read_text(encoding="utf-8"))
    for s in [x for x in lire_registre()["sources"] if x["mode"] == "veille"]:
        lu, nom = s["lu"], s["id"]
        try:
            if nom == "lycee-rers":
                verdict(nom, catalogue_rers(lu), "catalogue %d retrouve (racine XML)" % lu)
                log("  [info] catalogue %d : %s" % (lu + 1, "PRESENT" if catalogue_rers(lu + 1) else "absent (attendu tant qu'il n'est pas paru)"))
            elif "phrase_hal" in s:
                notes = notes_hal(s)
                verdict(nom, notes[0][0] == lu, "note la plus recente rendue par HAL : %s (edition lue : %s)" % (notes[0][0], lu))
            elif nom == "lycee-concours":
                p = page_concours(lu)
                ok = False
                if p:
                    # Les valeurs lues dans la page doivent être celles de l'extrait figé de la page lycée.
                    lignes = [r for t in p[1].values() for r in t if r and r[0] == "Mathématiques" and len(r) >= 6]
                    retrouve = sorted((int(re.sub(r"\D", "", r[1])), int(re.sub(r"\D", "", r[5]))) for r in lignes)
                    fige = sorted((v["postes"], v["admis"]) for v in extrait["concours_2026"]["capes"]["Mathématiques"].values())
                    ok = retrouve == fige
                verdict(nom, ok, "session %d retrouvee, CAPES de mathematiques identique a l'extrait fige" % lu if ok
                        else "session %d non retrouvee ou valeurs differentes de l'extrait fige" % lu)
            elif nom == "lycee-ocde":
                v = ocde_annees().get(lu)
                fige = extrait["c3"][str(lu)]["FRA"]
                verdict(nom, v is not None and round(v) == fige, "France %d : %s (extrait fige : %s)" % (lu, v, fige))
            else:
                verdict(nom, False, "source en veille sans temoin")
        except Injoignable as e:
            log("  [NON CONCLUANT] %s -- %s" % (nom, e))
        except Anomalie as e:
            verdict(nom, False, str(e))


def detecter(reg: dict, publication: str | None = None) -> list[dict]:
    trouve = detecter_sies(reg)
    # La figure « après le bac » suit la cohorte de la licence : on regarde les fiches APRÈS avoir inscrit la cohorte neuve.
    vue = json.loads(json.dumps(reg))
    for t in trouve:
        t["inscrire"](vue)
    trouve += detecter_eesr(vue)
    trouve += detecter_insee(reg, publication)
    return trouve


# ------------------------------------------------------------------ intégration
def empreintes() -> dict[str, str]:
    out = {}
    for ligne in SUMS.read_text(encoding="utf-8").splitlines():
        if ligne.strip():
            h, nom = ligne.split(None, 1)
            out[nom.strip().lstrip("*")] = h
    return out


def lancer(script: str, check: bool) -> int:
    args = [sys.executable, str(ROOT / "scripts" / script)] + (["--check"] if check else [])
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    for ligne in (r.stdout + r.stderr).strip().splitlines()[-4:]:
        log("    " + ligne)
    return r.returncode


def integrer(publication: str | None) -> int:
    reg = lire_registre()
    trouve = detecter(reg, publication)
    if not trouve:
        log("Aucune edition nouvelle.")
        return 0
    avant_reg, avant_sums = REG.read_text(encoding="utf-8"), SUMS.read_text(encoding="utf-8")
    poses: list[Path] = []
    touchees = sorted({t["source"] for t in trouve})
    try:
        sums = empreintes()
        for t in trouve:
            log("Edition nouvelle : %s -- %s" % (t["source"], t["quoi"]))
            for nom, octets in t["pieces"]:
                p = SRC / nom
                if p.exists():
                    raise Anomalie("%s existe deja dans les pieces archivees : une piece ne s'ecrase pas" % nom)
                p.write_bytes(octets)
                poses.append(p)
                sums[nom] = hashlib.sha256(octets).hexdigest()
            t["inscrire"](reg)
        for ident in touchees:
            src(reg, ident)["telecharge_le"] = date.today().isoformat()
        SUMS.write_text("".join("%s *%s\n" % (h, n) for n, h in sums.items()), encoding="utf-8", newline="\n")
        REG.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
        scripts = [g for g in ORDRE if any(g in src(reg, i)["generateurs"] for i in touchees)]
        # Tous en --check d'abord : rien ne s'écrit tant qu'un seul générateur refuse l'édition.
        for g in [x for x in scripts if x != "og_enseignants.py"]:
            log("  controle : %s" % g)
            if lancer(g, True) != 0:
                raise Anomalie("ADOPTION REFUSEE : %s rejette l'edition nouvelle (temoin ou garde de prose). La donnee dement "
                               "une phrase de la page, ou le fichier a change de forme : a reprendre a la main." % g)
        for g in scripts:
            log("  ecriture : %s" % g)
            if lancer(g, False) != 0:
                raise Anomalie("ecriture interrompue dans %s apres un controle reussi : etat a verifier" % g)
    except Anomalie as e:
        REG.write_text(avant_reg, encoding="utf-8", newline="\n")
        SUMS.write_text(avant_sums, encoding="utf-8", newline="\n")
        for p in poses:
            p.unlink(missing_ok=True)
        log("ECHEC : %s" % e)
        log("Registre, empreintes et pieces remis dans leur etat d'avant.")
        return 1
    log("Adopte : %s. Pages a reconstruire : %s" % (", ".join(t["quoi"] for t in trouve),
                                                    ", ".join(sorted({p for i in touchees for p in src(reg, i)["pages"]}))))
    return 0


# ------------------------------------------------------------------ témoin positif
def essai() -> int:
    """Chaque détecteur doit retrouver, à la source, l'édition déjà archivée. Rien n'est écrit."""
    reg = lire_registre()
    sums = empreintes()
    echecs = 0
    non_conclus: list[str] = []

    def verdict(nom: str, ok: bool, detail: str) -> None:
        nonlocal echecs
        echecs += 0 if ok else 1
        log("  [%s] %s -- %s" % ("OK" if ok else "ECHEC", nom, detail))

    # SIES : on retire la dernière cohorte, le détecteur doit rapporter le même fichier, octet pour octet.
    r = json.loads(json.dumps(reg))
    s = src(r, "sies-licence")
    der = str(max(int(k) for k in s["cohortes"]))
    attendu = s["cohortes"].pop(der)[0]
    try:
        ARCHIVE_INJOIGNABLE.clear()
        t = detecter_sies(r)
        if ARCHIVE_INJOIGNABLE:
            # Une archive qui ne répond pas ne dit rien du détecteur : ni OK ni échec. Annotation visible dans le run,
            # et le compte figure au bilan ; le lundi suivant rejoue le témoin.
            non_conclus.append("sies-licence")
            print("::warning::Temoin sies-licence NON CONCLUANT : archive publique injoignable (code %s)" % ARCHIVE_INJOIGNABLE[-1])
            raise StopIteration
        ok = bool(t) and hashlib.sha256(t[0]["pieces"][0][1]).hexdigest() == sums.get(attendu)
        verdict("sies-licence", ok, "cohorte %s retrouvee, empreinte identique a la piece archivee" % der if ok
                else "cohorte %s non retrouvee ou piece differente" % der)
    except StopIteration:
        log("  [NON CONCLUANT] sies-licence -- archive publique injoignable apres trois essais")
    except Anomalie as e:
        verdict("sies-licence", False, str(e))
    # EESR : on retire le dernier millésime, la fiche retrouvée doit porter le même tableau 13.03.
    r = json.loads(json.dumps(reg))
    e_ = src(r, "eesr-acces")
    an = max(int(k) for k in e_["fiches_acces"])
    try:
        f = fiche_eesr(an, "13")
    except Injoignable as e:
        # Même règle que l'archive publique du SIES : un site muet ne dit rien du détecteur.
        f = False
        non_conclus.append("eesr-acces")
        print("::warning::Temoin eesr-acces NON CONCLUANT : %s" % e)
        log("  [NON CONCLUANT] %s" % e)
    if f is None:
        verdict("eesr-acces", False, "fiche 13 des bacheliers %d non retrouvee" % an)
    elif f:
        def tableau(octets: bytes) -> str:
            t = texte(octets)
            i = t.find("Origine sociale renseignée")
            return t[i:i + 700]
        archive = (SRC / e_["fiches_acces"][str(an)][0]).read_bytes()
        ok = tableau(f[1]) == tableau(archive) and len(tableau(archive)) > 200
        verdict("eesr-acces", ok, "fiche 13 des bacheliers %d retrouvee, tableau identique a la piece archivee" % an if ok
                else "fiche 13 retrouvee mais tableau different de la piece archivee")
    try:
        f9 = fiche_eesr(max(int(k) for k in e_["fiches_bac"]), "09")
        verdict("eesr-acces (fiche 09)", f9 is not None, "fiche 09 retrouvee" if f9 else "fiche 09 non retrouvee")
    except Injoignable as e:
        non_conclus.append("eesr-acces (fiche 09)")
        print("::warning::Temoin eesr-acces (fiche 09) NON CONCLUANT : %s" % e)
        log("  [NON CONCLUANT] %s" % e)
    # INSEE : la page annuelle du SDES existe pour l'année en cours, et la publication connue rend le même fichier.
    i_ = src(reg, "insee-empreinte")
    an = int(i_["annee_donnees"])
    code, page = http("https://www.statistiques.developpement-durable.gouv.fr/lempreinte-carbone-de-la-france-de-1990-%d" % an)
    verdict("insee-empreinte (page annuelle du SDES)", code == 200 and ("1990 à %d" % an) in texte(page), "code %s" % code)
    code, suivante = http("https://www.statistiques.developpement-durable.gouv.fr/lempreinte-carbone-de-la-france-de-1990-%d" % (an + 1))
    log("  [info] page de l'annee suivante : code %s (404 attendu tant qu'elle n'est pas parue)" % code)
    try:
        nom, xlsx, edition = piece_insee(i_["publication"], an)
        ok = hashlib.sha256(xlsx).hexdigest() == sums.get(i_["fichier"]) and edition == i_["edition"]
        verdict("insee-empreinte (fichier)", ok, "fichier identique a la piece archivee, edition « %s »" % edition if ok
                else "fichier ou libelle d'edition different (%s)" % edition)
    except Anomalie as e:
        verdict("insee-empreinte (fichier)", False, str(e))
    code, flux = http("https://www.insee.fr/fr/flux/1")
    n = len(re.findall(r"<item>", flux.decode("utf-8", "replace"))) if code == 200 else 0
    verdict("insee-empreinte (flux des parutions)", n > 5, "%d parutions lues ; le filtrage par titre ne se prouve qu'un jour de parution" % n)
    essai_veille(verdict)
    log("Essai : %d echec(s), %d non concluant(s)%s." % (echecs, len(non_conclus), (" (" + ", ".join(non_conclus) + ")") if non_conclus else ""))
    return 1 if echecs else 0


# ------------------------------------------------------------------ état, contrôle, sorties
def prochaine(s: dict) -> tuple[str, date] | None:
    """Ce que la source doit publier ensuite, et la date où la fenêtre de parution se ferme."""
    if s["id"] == "sies-licence":
        c = max(int(k) for k in s["cohortes"]) + 1
        return "cohorte %d" % c, date(c + 2, s["fenetre"]["mois_fin"], s["fenetre"]["jour_fin"])
    if s["id"] == "insee-empreinte":
        a = int(s["annee_donnees"]) + 1
        return "donnees %d" % a, date(a + 1, s["fenetre"]["mois_fin"], s["fenetre"]["jour_fin"])
    if s["id"] == "eesr-acces":
        a = max(int(k) for k in s["fiches_acces"]) + 1
        return "bacheliers %d" % a, date(a + 2, s["fenetre"]["mois_fin"], s["fenetre"]["jour_fin"])
    return None


def etat(controle: bool) -> int:
    reg = lire_registre()
    retards = []
    for s in reg["sources"]:
        jeu = ROOT / s["jeu"]
        releve = json.loads(jeu.read_text(encoding="utf-8")).get("releve_le", "?") if jeu.is_file() else "ABSENT"
        p = prochaine(s) if s["mode"] == "fichier" and "fenetre" in s else None
        suite = ("attendu : %s, fenetre close le %s" % (p[0], p[1].isoformat())) if p else \
            ("veille (signal par ticket, integration a la main) : edition lue %s" % s["lu"]) if s["mode"] == "veille" else \
            ("workflow %s" % s["workflow"] if s.get("workflow") else "aucune detection (mise a jour a la main)")
        if p and date.today() > p[1]:
            retards.append("%s : %s non integre, fenetre close depuis le %s" % (s["id"], p[0], p[1].isoformat()))
        if not controle:
            log("%-20s %-8s jeu releve le %-10s  %s" % (s["id"], s["mode"], releve, suite))
    for r in retards:
        log("RETARD  " + r)
    if controle:
        log("Sources en fichier : %d retard(s) apres fenetre de parution." % len(retards) + ("" if retards else " OK"))
        return 1 if retards else 0
    return 0


def sorties() -> int:
    reg = lire_registre()
    chemins = ["data/sources_maj.json", "scripts/sources_enseignants"]
    for s in reg["sources"]:
        if s["mode"] == "fichier":
            chemins += s.get("sorties", [])
    print(" ".join(dict.fromkeys(chemins)))
    return 0


def main() -> int:
    args = sys.argv[1:]
    cmd = args[0] if args else "etat"
    publication = args[args.index("--publication") + 1] if "--publication" in args else None
    try:
        if cmd == "etat":
            return etat(False)
        if cmd == "controle":
            return etat(True)
        if cmd == "sorties":
            return sorties()
        if cmd == "essai":
            return essai()
        if cmd == "veille":
            return veille()
        if cmd == "detecter":
            trouve = detecter(lire_registre(), publication)
            for t in trouve:
                log("Edition nouvelle : %s -- %s (%s)" % (t["source"], t["quoi"], ", ".join(n for n, _ in t["pieces"])))
            log("%d edition(s) nouvelle(s) ; rien ecrit." % len(trouve))
            return 0
        if cmd == "integrer":
            return integrer(publication)
    except Anomalie as e:
        log("ECHEC : %s" % e)
        return 1
    log("Commande inconnue : %s (etat, detecter, integrer, essai, veille, sorties, controle)" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main())
