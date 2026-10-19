"""update_dette_collectivites.py -- jeu de la page /dette-publique-collectivites-locales/ (prolongement du dossier dette).

Sources, toutes interrogees a chaque passage (aucun chiffre saisi a la main) :
  - Eurostat : gov_10a_main (comptes des administrations par sous-secteur), gov_10q_ggdebt (dette trimestrielle),
    gov_10dd_ggd (dette par secteur detenteur), nama_10_gdp (PIB, temoin du denominateur) ;
  - OFGL (data.ofgl.fr) : bases consolidees des communes, intercommunalites, departements, regions ;
  - Legifrance : CGCT art. L. 1613-1 (DGF votee 2013-2017) et loi n° 2025-127 art. 186 (DILICO), reponses de l'API
    archivees dans scripts/sources_collectivites/ et controlees par empreinte.
Ecrit : data/dette_collectivites.json (+ copie static/), static/dette_collectivites.csv (UTF-8 BOM), data/figures_collectivites.json,
static/img/collectivites-*.svg + .png (ensemble ou pas du tout), en francais et en anglais (-en, depuis le 07/10/2026 :
blocs affichage et affichage_en aux memes cles, figures au meme dessin). Rien n'est ecrit a donnees identiques (releve_le conserve).

Chaque qualificatif de la prose est une GARDE (calculer()) : si la donnee le dement, arret, aucun fichier ecrit. A chaque
passage, une mutation reelle sur une copie des donnees doit faire mordre une garde (autotest_mutation), sinon arret.

Phase B de la refonte (11/10/2026, arbitrage ARBITRAGE_CE_COLLECTIVITES_PHASE_A.md) : cascade 2013-2017 dans les DEUX
unites (milliards d'euros courants et points de PIB, memes postes, meme ordre) ; PIB de la notification (gov_10dd_edpt1,
B1GQ, MIO_NAC) pour la croissance nominale et la dette notifiee, en temoin ; textes de Cahors (loi n° 2018-32, art. 13
et 29 ; loi n° 2020-290, art. 12) et CGCT L. 1612-4 lus dans leurs archives Legifrance (empreintes controlees) ; gardes
de PROSE sur la page elle-meme (une phrase d'attribution sur 2013-2017 porte ses deux unites ; aucun verdict tire de la
dette ; la somme des mesures du projet de loi n'est jamais un prelevement net) ; versions telephone (-m.svg) et pied
commun (pied_figure.py) ; langue generee par langue_generee.py pour toute cle nouvelle.

Usage : python scripts/update_dette_collectivites.py [--check] [--mutation=unite|verdict|plf_net|reclassement|plf_ecart|stables|cahors]
  --mutation : temoin positif d'une garde (prose ou donnee) ; la garde DOIT mordre (sortie 1), rien n'est ecrit.
Histoire : prototype contre-expertise en trois tours de raisonnement et trois de faits (01/10/2026), arbitrages dans
D:\PRO\.claude\external-audits\ARBITRATIONS\ (ENTRANTE_2026-10-01_Collectivites, PRO-20261001-145721, -152012, -153529).
"""
from __future__ import annotations

import csv
import hashlib
import html
import itertools
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import langue_generee as lg  # noqa: E402  -- nombre, signe, accord de « point » (organe commun)
import pied_figure  # noqa: E402  -- pied commun, version téléphone, parité (organe commun)
import releve_jeu as rj  # noqa: E402  -- jeu comparé et écrit normalisé (organe commun, 19/10/2026)

DON = Path(__file__).resolve().parent / "sources_collectivites"
GEO = ["FR", "DE", "IT", "ES"]
NOMS = {"FR": "France", "DE": "Allemagne", "IT": "Italie", "ES": "Espagne"}
ITEMS = ["B9", "P51G", "D73REC", "D2REC", "D5REC", "D91REC", "TE", "TR", "B8G"]
SECTEURS = ["S13", "S1311", "S1312", "S1313"]
# Elections municipales francaises (fait institutionnel, non une donnee statistique).
MUNICIPALES = [2001, 2008, 2014, 2020]
# Periode de la « contribution au redressement des finances publiques » (baisse de la DGF, lois de finances 2014-2017).
EPISODE = (2013, 2017)


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


class Arret(Exception):
    pass


def fail(m: str) -> None:
    raise Arret(m)


# ------------------------------------------------------------------ Eurostat
def fetch(url: str) -> bytes:
    for k in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "stephane-lalut.com (stephane@stephane-lalut.com)"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if k == 2:
                fail("reseau : %s (%s)" % (url[:120], e))
            time.sleep(3 * (k + 1))
    return b""


def eurostat(ds: str, **f) -> dict:
    q = [("format", "JSON"), ("lang", "fr")] + [(k, v) for k, vs in f.items() for v in (vs if isinstance(vs, list) else [vs])]
    url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/%s?" % ds + urllib.parse.urlencode(q)
    brut = fetch(url)
    d = json.loads(brut)
    if "dimension" not in d:
        fail("Eurostat %s : reponse sans dimensions" % ds)
    ids, size = d["id"], d["size"]
    cats = {}
    for k in ids:
        idx = d["dimension"][k]["category"]["index"]
        cats[k] = sorted(idx, key=idx.get)
    obs = []
    for combo in itertools.product(*[range(s) for s in size]):
        pos, m = 0, 1
        for i in reversed(range(len(ids))):
            pos += combo[i] * m
            m *= size[i]
        v = d["value"].get(str(pos))
        if v is not None:
            obs.append({ids[i]: cats[ids[i]][combo[i]] for i in range(len(ids))} | {"v": float(v)})
    return {"dataset": ds, "url": url, "maj_eurostat": d.get("updated"), "sha256": hashlib.sha256(brut).hexdigest(), "obs": obs}


OFGL_BASES = {"communes": "ofgl-base-communes-consolidee", "intercommunalites": "ofgl-base-gfp-consolidee",
              "departements": "ofgl-base-departements-consolidee", "regions": "ofgl-base-regions-consolidee"}
OFGL_AGREGATS = ["Dotation globale de fonctionnement", "Concours de l'Etat", "Epargne brute", "Dépenses d'équipement",
                 "Encours de dette", "TVA"]


def ofgl() -> dict:
    """Sommes nationales par categorie et par exercice (data.ofgl.fr, comptes de gestion DGFiP), en euros."""
    out, h = {}, hashlib.sha256()
    for cat, ds in OFGL_BASES.items():
        for ag in OFGL_AGREGATS:
            q = {"select": "exer, sum(montant) as m", "where": 'agregat="%s"' % ag, "group_by": "exer", "limit": 100}
            url = "https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/%s/records?" % ds + urllib.parse.urlencode(q)
            brut = fetch(url)
            h.update(brut)
            d = json.loads(brut)
            if "results" not in d:
                fail("OFGL %s / %s : reponse sans resultats" % (cat, ag))
            out.setdefault(cat, {})[ag] = {str(r["exer"])[:4]: r["m"] for r in d["results"] if r["m"] is not None}
    return {"dataset": "data.ofgl.fr (4 bases consolidees)", "maj_eurostat": datetime.now(timezone.utc).strftime("%Y-%m-%dT"),
            "sha256": h.hexdigest(), "series": out}


def relever() -> dict:
    return {
        "releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "comptes": eurostat("gov_10a_main", geo=GEO, unit="MIO_EUR", sector=SECTEURS, na_item=ITEMS),
        "pib": eurostat("nama_10_gdp", geo=GEO, unit="CP_MEUR", na_item="B1GQ"),
        # Denominateur du MEME millesime que les comptes : depenses totales des APU publiees en % du PIB.
        "te_pc": eurostat("gov_10a_main", geo=GEO, unit="PC_GDP", sector="S13", na_item="TE"),
        "dette": eurostat("gov_10q_ggdebt", geo=GEO, unit="PC_GDP", sector=["S13", "S1312", "S1313"], na_item="GD"),
        # Dette par secteur DETENTEUR (sector2) : consolidation entre echelons et part detenue par l'Etat central.
        "ggd": eurostat("gov_10dd_ggd", geo=GEO, unit="PC_GDP", na_item="GD", sector=["S1312", "S1313"],
                        sector2=["S1_S2", "S1311", "S1312", "S1313"], maturity="TOTAL"),
        "ofgl": ofgl(),
        # Notification (avril, octobre) : PIB nominal (S1, B1GQ, MIO_NAC) et dette publique notifiee (S13, GD, PC_GDP).
        # Croissance du PIB nominal 2013-2017 et ecart dette trimestrielle / notifiee, dits sur la page (B1, B5).
        "notif": eurostat("gov_10dd_edpt1", geo="FR", unit=["MIO_NAC", "PC_GDP"], sector=["S1", "S13"], na_item=["B1GQ", "GD"]),
    }


# ------------------------------------------------------------------ gardes de PROSE (refonte du 11/10/2026)
# Une identite comptable exacte ne garantit pas une interpretation exacte (contre-expertise de phase A, § 1) : les
# chiffres sont gardes par les donnees, la LECTURE l'est ici, sur le texte meme de la page (FR et EN), des fiches
# « Reutiliser » et des descriptions de figures. Trois classes de phrases sont interdites :
#   1. une attribution sur 2013-2017 (« surtout par », « grace a », « principalement »...) qui ne porte pas ses DEUX
#      unites (milliards d'euros ET points de PIB) : en euros et en points, la meme variation ne raconte pas la meme chose ;
#   2. un verdict tire de la dette (« pas une variable d'ajustement, car leur dette... ») : la regle d'or contient la
#      dette par construction, sa faiblesse ne mesure pas l'intensite d'un ajustement ;
#   3. la somme des mesures du projet de loi de finances presentee autrement que comme une somme arithmetique, ou un
#      « prelevement net » affirme : leur effet net n'est pas etabli par addition.
# Et « a monte » (tournure proscrite, lecon 16 du CLAUDE.md du site).
MUTATION = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutation=")), None)
PAGES = {"fr": Path(__file__).resolve().parent.parent / "content" / "dette-publique-collectivites-locales" / "_index.md",
         "en": Path(__file__).resolve().parent.parent / "content" / "dette-publique-collectivites-locales" / "_index.en.md"}
ATTRIB = {"fr": r"\b(?:surtout|principalement|essentiellement|avant tout|grâce aux?|en majeure partie|pour l'essentiel|l'essentiel)\b",
          "en": r"\b(?:mainly|chiefly|largely|primarily|mostly|thanks to|for the most part|the bulk)\b"}
UNITE_MD = r"_md(?:e|_s)?\b|milliards?|Md€|billion"
UNITE_PT = r"_pt\b|\bpoints?\b"
VERDICT = {"fr": (r"variable d'ajustement", r"dette|endett", r"\b(?:car|puisque|donc|parce que|ne sont pas|n'en sont pas|pas une|pas la)\b"),
           "en": (r"adjustment variable", r"\bdebt|indebted", r"\b(?:because|since|so|therefore|are not|is not|not the|not an)\b")}
NET = {"fr": (r"prélèvement net|effort net|ponction nette|montant net|contribution nette",
              r"\b(?:pas|ni|n'est|aucun|aucune)\b"),
       "en": (r"net levy|net cut|net effort|net amount|net contribution", r"\b(?:not|nor|no)\b")}
SOMME = {"fr": "somme arithmétique", "en": "arithmetic sum"}
# 4. (cloture, 11/10/2026, contre-expertise du rendu § 4 A) un reclassement de recettes presente comme une absence de baisse
#    des ressources (« les ressources ne baissent pas, elles changent de case »), ou un instrument nouveau presente comme la
#    fin des precedents (« la contrainte ne passe plus par ») : les series etablissent des substitutions, pas un montant
#    disponible inchange. Interdit sur la page entiere (FR et EN) et dans les textes generes.
RECLASSEMENT = {"fr": r"ne baissent pas|ne baisse pas,? (?:elle|elles) change|change(?:nt)? de case|changement de case|"
                      r"ne passe plus|sans les réduire",
                "en": r"did not fall,|do not fall,|changed? box|changes box|change of box|no longer works through|"
                      r"without reducing (?:it|them)"}
# 5. (cloture) l'ecart entre la somme des mesures et la variation des ressources du projet de loi n'est jamais un montant
#    preleve : toute phrase qui le cite porte une negation.
ECART_NEG = {"fr": r"\b(?:pas|ni|n'est|aucun)\b", "en": r"\b(?:not|nor|no)\b"}
MUTATIONS_PROSE = {
    "unite": "Le solde s'est redressé surtout par la baisse des dépenses ({{< coll-val \"ep_te_pt\" >}} de PIB).",
    "verdict": "Les collectivités ne sont pas une variable d'ajustement, car leur dette a peu augmenté.",
    "plf_net": "Le projet impose aux collectivités un prélèvement net de {{< coll-val \"plf_somme\" >}} milliards d'euros.",
    "reclassement": "Une dotation devient une fraction de TVA : les ressources ne baissent pas, elles changent de case.",
    "plf_ecart": "Le projet retire aux collectivités {{< coll-val \"plf_ecart_mde\" >}} de ressources.",
}


def phrases(t: str) -> list[str]:
    """Une ligne de Markdown est un paragraphe (convention de la page) ; on la coupe en phrases et en cellules."""
    import re
    out = []
    for ligne in t.replace("&nbsp;", " ").splitlines():
        ligne = re.sub(r"\s+", " ", ligne)
        out += [p_ for p_ in re.split(r"(?<=[.!?;:»])\s+(?=[A-ZÀÉÈÎÔ«*\[{(\-])|\s*\|\s*", ligne) if p_.strip()]
    return out


def fautes_prose(textes: dict) -> list[str]:
    """textes : {langue: [texte, ...]}. Rend la liste des phrases fautives (vide = conforme)."""
    import re
    out = []
    for lang, liste in textes.items():
        for t in liste:
            for ph in phrases(t):
                court = ph[:160]
                if re.search(ATTRIB[lang], ph, re.I) and re.search(r"ep_|creux|2013|2017", ph):
                    if not (re.search(UNITE_MD, ph) and re.search(UNITE_PT, ph)):
                        out.append("[%s] attribution sur %s sans ses deux unités (euros ET points de PIB) : %s" % (lang, "2013-2017", court))
                v_, d_, n_ = VERDICT[lang]
                if re.search(v_, ph, re.I) and re.search(d_, ph, re.I) and re.search(n_, ph, re.I):
                    out.append("[%s] verdict tiré de la dette : %s" % (lang, court))
                if "plf_somme" in ph and SOMME[lang] not in ph:
                    out.append("[%s] somme du projet de loi sans « %s » : %s" % (lang, SOMME[lang], court))
                n1, n2 = NET[lang]
                if re.search(n1, ph, re.I) and not re.search(n2, ph, re.I):
                    out.append("[%s] effet net affirmé : %s" % (lang, court))
                if re.search(RECLASSEMENT[lang], ph, re.I):
                    out.append("[%s] reclassement présenté comme une absence de baisse, ou instrument nouveau comme la fin "
                               "des précédents : %s" % (lang, court))
                if "plf_ecart" in ph and not re.search(ECART_NEG[lang], ph, re.I):
                    out.append("[%s] écart somme / variation du projet de loi présenté comme un montant : %s" % (lang, court))
                if lang == "fr" and re.search(r"\bmonté\b", ph):
                    out.append("[fr] « a monté » (tournure proscrite) : %s" % court)
    return out


def gardes_prose(extra: dict | None = None) -> int:
    """Page FR et EN (front matter compris) et textes generes passes en argument. Arret sur toute faute."""
    textes = {lang: [f.read_text(encoding="utf-8")] for lang, f in PAGES.items()}
    if MUTATION in MUTATIONS_PROSE:
        textes["fr"].append(MUTATIONS_PROSE[MUTATION])
    for lang, l_ in (extra or {}).items():
        textes[lang] += l_
    f_ = fautes_prose(textes)
    if f_:
        fail("garde de prose : " + " | ".join(f_))
    return sum(len(phrases(t)) for l_ in textes.values() for t in l_)


# ------------------------------------------------------------------ calcul
class Jeu:
    def __init__(self, b: dict):
        self.b = b
        self.c: dict = {}
        for o in b["comptes"]["obs"]:
            self.c[(o["geo"], o["sector"], o["na_item"], int(o["time"]))] = o["v"]
        # PIB implicite de la table des comptes publics : TE(S13) en M EUR / TE(S13) en % du PIB.
        # Precision ~0,1/55, soit 0,2 % ; nama_10_gdp, publie a une autre date, sert de temoin (revisions de PIB).
        te_pc = {(o["geo"], int(o["time"])): o["v"] for o in b["te_pc"]["obs"]}
        self.pib = {}
        for (g, y), pc in te_pc.items():
            te = self.c.get((g, "S13", "TE", y))
            if te is not None and pc:
                self.pib[(g, y)] = 100.0 * te / pc
        self.pib_nama = {(o["geo"], int(o["time"])): o["v"] for o in b["pib"]["obs"]}
        self.ggd = {(o["geo"], o["sector"], o["sector2"], int(o["time"])): o["v"] for o in b["ggd"]["obs"]}
        self.ofgl = b["ofgl"]["series"]
        self.notif = {(o["sector"], o["na_item"], o["unit"], int(o["time"])): o["v"] for o in b["notif"]["obs"]}
        self.d = {}
        for o in b["dette"]["obs"]:
            if o["time"].endswith("Q4"):
                self.d[(o["geo"], o["sector"], int(o["time"][:4]))] = o["v"]

    def mio(self, g, s, i, y):
        return self.c.get((g, s, i, y))

    def pc(self, g, s, i, y):
        """% du PIB, recalcule depuis les millions d'euros (deux decimales utiles, la table PC_GDP n'en a qu'une)."""
        v, p = self.mio(g, s, i, y), self.pib.get((g, y))
        return None if v is None or not p else 100.0 * v / p

    def annees(self, g, s, i):
        return sorted(y for (gg, ss, ii, y) in self.c if (gg, ss, ii) == (g, s, i))

    def dette(self, g, s, y):
        return self.d.get((g, s, y))

    def detenu(self, g, s, par, y):
        return self.ggd.get((g, s, par, y))

    def of(self, cat, ag, y):
        v = self.ofgl.get(cat, {}).get(ag, {}).get(str(y))
        return None if v is None else v / 1e9  # milliards d'euros

    def of_annees(self, cat, ag):
        return sorted(int(y) for y in self.ofgl.get(cat, {}).get(ag, {}))

    def dette_annees(self, g, s):
        return sorted(y for (gg, ss, y) in self.d if (gg, ss) == (g, s))


EN_LETTRES = {0: "aucune", 1: "une", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit"}
# Page anglaise /en/local-government-debt/ (07/10/2026) : un calcul, deux blocs (affichage, affichage_en) aux memes cles,
# et des figures -en au meme dessin ; les gardes ne lisent que des nombres, une passe vaut pour les deux langues.
LETTRES_ANGLAIS = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
NOMS_EN = {"FR": "France", "DE": "Germany", "IT": "Italy", "ES": "Spain"}
CATS_EN = {"communes": "Municipalities", "intercommunalites": "Inter-municipal groupings", "departements": "Departments",
           "regions": "Regions"}
MOIS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def fr1(v: float, dec: int = 1) -> str:
    s = ("%." + str(dec) + "f") % v
    return s.replace("-", "−").replace(".", ",")


def en1(v: float, dec: int = 1) -> str:
    """Format anglais : point decimal, separateur de milliers, moins typographique (comme update_dette_baisse.py)."""
    s = ("{:,.%df}" % dec).format(v)
    if float(s.replace(",", "")) == 0:
        s = s.replace("-", "")
    return s.replace("-", "−")


def date_en(s: str) -> str:
    """« 1er octobre 2026 » -> « 1 October 2026 ». Format inattendu = arret, jamais une date francaise sur la page anglaise."""
    import re
    m = re.fullmatch(r"(\d{1,2})(?:er)?[\s ]+(\S+)[\s ]+(\d{4})", s.strip())
    if not m or m.group(2) not in MOIS_FR:
        fail("date de depot du projet de loi de finances illisible pour l'anglais : %r" % s)
    return "%d %s %s" % (int(m.group(1)), MOIS_EN[MOIS_FR.index(m.group(2))], m.group(3))


def montant_en(s: str) -> str:
    """« un milliard d’euros » / « 1,5 milliard d’euros » -> « €1 billion » / « €1.5 billion ». Sinon arret."""
    import re
    m = re.fullmatch(r"(un|deux|trois|quatre|cinq|[\d,]+)[\s ]+milliards?[\s ]+d[’']euros", s.strip())
    if not m:
        fail("montant du DILICO illisible pour l'anglais : %r" % s)
    mots = {"un": "1", "deux": "2", "trois": "3", "quatre": "4", "cinq": "5"}
    return "€%s billion" % mots.get(m.group(1), m.group(1).replace(",", "."))


LEGI = DON / "legifrance_CGCT_L1613-1_v2017.json"
LEGI_SHA = "e7f794b731f4f22efb950fa003e42a77d14b27bb2904f8862f98d47556feac38"


def dgf_votee() -> dict:
    """Montant de la DGF fixe par la loi de finances (CGCT, art. L. 1613-1, version 2017), lu dans la reponse
    Legifrance archivee par le MCP sources (empreinte controlee) : aucun montant recopie a la main."""
    import re
    brut = LEGI.read_bytes()
    if hashlib.sha256(brut).hexdigest() != LEGI_SHA:
        fail("archive Legifrance L1613-1 alteree (empreinte)")
    texte = json.loads(brut)["article"]["texte"]
    out = {int(a): int(m.replace(" ", "").replace("\u202f", "").replace("\xa0", "")) / 1e9
           for a, m in re.findall(r"En (\d{4}), ce montant(?:,)? (?:est )?égal à ([\d\s\u202f\xa0]+) €", texte)}
    if not all(a in out for a in range(2013, 2018)):
        fail("DGF votee : annees 2013-2017 introuvables dans l'article")
    return out


DILICO = DON / "legifrance_LFI2025_art186_DILICO.json"
DILICO_SHA = "db8a309145d381bd699d110260d7b792b81b9c416362747483a7bfa4c88b9f34"


def dilico_montant() -> str:
    """Montant du DILICO 2025, lu dans l'article 186 de la loi n° 2025-127 (reponse Legifrance archivee)."""
    import re
    brut = DILICO.read_bytes()
    if hashlib.sha256(brut).hexdigest() != DILICO_SHA:
        fail("archive Legifrance DILICO alteree (empreinte)")
    m = re.search(r"En 2025, ce dispositif concerne un montant d'(.+?) d'euros", json.loads(brut)["article"]["texte"])
    if not m:
        fail("DILICO : montant introuvable dans l'article 186")
    return m.group(1) + " d’euros"


# Textes relus par l'API Legifrance (PISTE, consult/getArticle) le 11/10/2026 et archives verbatim : identifiant JORF ou
# LEGI de l'article, empreinte controlee. Aucun taux, seuil ni annee recopie a la main : tout est relu par motif.
LEGI_TEXTES = {
    "lpfp13": (DON / "legifrance_LPFP2018_art13.json", "445605aa478c68b38c1a6f3eb85f07ba6b5d513f019ee15727e76e0b6bc5e03c"),
    "lpfp29": (DON / "legifrance_LPFP2018_art29.json", "fd6087913ad39b99ba29fda6a379b50920ce4f517592de53d3d5dbc282a3917b"),
    "urg12": (DON / "legifrance_loi2020-290_art12.json", "ddc2a1a35467224400ce1eb80451746b0c1cea71f4a82e246a245035ea0262ac"),
    "l1612_4": (DON / "legifrance_CGCT_L1612-4_v1996.json", "7379192cda9f1b1ffec69ffe33d9345966bd5fa0f7e60c4f015f5cb4ba0c5b76"),
    "l1612_4_2026": (DON / "legifrance_CGCT_L1612-4_v2026.json", "e177600dd99e79834ef9999a9ce41ce8d09b411e2e95e55b3d2df0afb99331da"),
}


def legi(cle: str) -> dict:
    f, sha = LEGI_TEXTES[cle]
    brut = f.read_bytes()
    if hashlib.sha256(brut).hexdigest() != sha:
        fail("archive Legifrance %s alteree (empreinte)" % f.name)
    return json.loads(brut)["article"]


def textes_regles() -> dict:
    """Pacte de Cahors et regle d'equilibre, lus dans les articles archives. Rend les grandeurs que la page cite."""
    import re
    norm = lambda t: re.sub(r"\s+", " ", t).replace("’", "'")  # noqa: E731
    a13, a29, u12 = legi("lpfp13"), legi("lpfp29"), legi("urg12")
    t13, t29, t12 = norm(a13["texte"]), norm(a29["texte"]), norm(u12["texte"])

    def un(motif, t, quoi):
        m = re.search(motif, t)
        if not m:
            fail("textes de Cahors : %s introuvable dans l'archive" % quoi)
        return m.groups()
    taux, = un(r"correspond à un taux de croissance annuel de ([\d,]+) % appliqué à une base de dépenses réelles",
               t13, "taux national (art. 13, III)")
    base, = un(r"appliqué à une base de dépenses réelles de fonctionnement en (\d{4})", t13, "année de base (art. 13, III)")
    seuil, = un(r"au titre de l'année 2016 sont supérieures à (\d+) millions d'euros", t29, "seuil des communes (art. 29, I)")
    ex = un(r"pour les exercices (\d{4}), (\d{4}) et (\d{4})", t29, "exercices du contrat (art. 29, II)")
    reprise, = un(r"reprise financière dont le montant est égal à (\d+) % de l'écart constaté", t29, "taux de reprise (art. 29, V)")
    plafond, = un(r"Le montant de cette reprise ne peut excéder (\d+) % des recettes réelles de fonctionnement", t29,
                  "plafond de la reprise (art. 29, V)")
    suspendu, = un(r"Les V et VI de l'article 29 de la loi n° 2018-32 .*? au titre de l'année (\d{4})", t12,
                   "dépenses exclues de la reprise (loi n° 2020-290, art. 12)")
    date_lpfp, = un(r"LOI n° ?2018-32 du (.+)$", norm(a13["textTitles"][0]["titre"]), "date de la loi de programmation")
    date_urg, = un(r"LOI n° ?2020-290 du (.+)$", norm(u12["textTitles"][0]["titre"]), "date de la loi d'urgence")
    for cle in ("l1612_4", "l1612_4_2026"):
        if "à l'exclusion du produit des emprunts" not in norm(legi(cle)["texte"]):
            fail("CGCT L. 1612-4 (%s) : l'exclusion de l'emprunt n'est plus dans le texte -- relire la section sur la dette" % cle)
    return {"cahors_taux": float(taux.replace(",", ".")), "cahors_base": int(base), "cahors_seuil_m": int(seuil),
            "cahors_exercices": [int(x) for x in ex], "cahors_reprise_pct": int(reprise), "cahors_plafond_pct": int(plafond),
            "cahors_suspendu": int(suspendu), "cahors_date_lpfp": date_lpfp, "cahors_date_urgence": date_urg}


PLF = DON / "plf_collectivites.json"
PLF_SHA = "0d61c45b6bdb0dc63b9407f79d69459053654514985cc07c6633b6c376b717da"


def plf_mesures() -> dict:
    """Ce que le dernier projet de loi de finances depose demande aux collectivites, relu par motif dans les pages
    archivees du projet de loi et de l'avis du Haut Conseil des finances publiques (sources_collectivites/
    archiver_plf.py ; empreinte controlee) : aucun montant recopie a la main. Montants d'un PROJET, avant examen."""
    import re
    brut = PLF.read_bytes()
    if hashlib.sha256(brut).hexdigest() != PLF_SHA:
        fail("archive du projet de loi de finances alteree (empreinte)")
    a = json.loads(brut)
    n = a["edition"]

    def texte(doc):
        return re.sub(r"\s+", " ", " ".join(a[doc]["pages"].values())).replace("\u2019", "'")
    plf, hcfp = texte("plf"), texte("hcfp")

    def lire(doc, motif, quoi):
        m = re.search(motif, plf if doc == "plf" else hcfp)
        if not m:
            fail("projet de loi de finances : %s introuvable dans l'archive (%s)" % (quoi, doc))
        return [float(g.replace(" ", "").replace(",", ".")) for g in m.groups()]
    an = str(n)
    dgf = lire("plf", r"En %s, ce montant est égal à ([\d ]+) €" % an, "montant de la DGF")[0] / 1e9
    dgf_hausse = lire("plf", r"nouvelle augmentation du montant de la DGF en %s à hauteur de (\d+) millions d'euros" % an,
                      "hausse de la DGF")[0]
    dgf_hausse_courant = lire("plf", r"À périmètre courant, le montant nominal de la DGF augmente donc de (\d+) millions",
                              "hausse de la DGF à périmètre courant")[0]
    cpeb = lire("plf", r"contribution progressive à l'effort budgétaire \(CPEB\), dont le rendement attendu s'élève à "
                       r"([\d,]+) milliards", "rendement de la contribution progressive")[0]
    part_com, part_dep = lire("plf", r"Le dispositif s'applique à (\d+) % des communes, à (\d+) % des départements",
                              "assiette de la contribution progressive")
    fctva = lire("plf", r"pour un rendement de ([\d,]+) milliards d'euros", "rendement de la réforme du FCTVA")[0]
    fctva_pts = lire("plf", r"soit une baisse de (\d+) points par rapport à la situation actuelle", "baisse du taux du FCTVA")[0]
    regions = lire("plf", r"fraction fixe d'accises sur les énergies d'un montant de ([\d,]+) millions d'euros",
                   "fraction d'accises des régions")[0]
    psr = lire("plf", r"sont évalués à ([\d ]+) euros", "prélèvements sur recettes")[0] / 1e9
    psr_lfi, psr_rev, psr_tab = lire("plf", r"Prélèvements sur les recettes de l'État au profit des collectivités territoriales "
                                            r"(\d\d \d{3}) (\d\d \d{3}) (\d\d \d{3})", "tableau des prélèvements sur recettes")
    res_md, res_pct = lire("plf", r"Les collectivités disposeront en %s de \+(\d+) Md€ de ressources supplémentaires par "
                                  r"rapport à %d \(\+([\d,]+) %%\)" % (an, n - 1), "ressources supplémentaires annoncées")
    h_cpeb, tva, minist, dilico = lire(
        "hcfp", r"un prélèvement de ([\d,]+) Md€ sur leurs avances de fiscalité, un écrêtement de ([\d,]+) Md€ de la TVA "
                r"affectée \(hors régions\), une réduction des contributions de certains ministères aux collectivités "
                r"\(([\d,]+) Md€\) ou encore un aménagement du rythme de versement du DILICO sur cinq ans au lieu de trois "
                r"\(([\d,]+) Md€\)", "liste des mesures (Haut Conseil)")
    h_fctva = lire("hcfp", r"l'État diminuant dès lors les concours à ce titre de −([\d,]+) Md€ en %s" % an, "FCTVA (Haut Conseil)")[0]
    inv_n1 = lire("hcfp", r"baisse importante de l'investissement des collectivités territoriales \(−([\d,]+) %\)",
                  "investissement prévu (Haut Conseil)")[0]
    inv_n = lire("hcfp", r"dépenses d'investissement des collectivités territoriales \(−([\d,]+) % après",
                 "investissement de l'année en cours (Haut Conseil)")[0]
    # Lecture du texte pour la page (refonte du 11/10/2026) : ce que le projet dit de la nature des mesures, relu par
    # motif ; une edition qui ne le dirait plus arrete tout (la phrase de la page ne serait plus soutenue).
    for motif, quoi in (
            (r"sans modifier le montant total des sommes restituées", "DILICO : montant total restitué inchangé (art. 84)"),
            (r"Les contributions sont notifiées par un arrêté des ministres chargés du budget et des collectivités "
             r"territoriales publié au Journal officiel, qui précise le montant prélevé par collectivité",
             "contribution progressive : arrêté publié au Journal officiel, montant par collectivité (art. 37, V)"),
            (r"imputé mensuellement, à compter de la date de notification, sur le montant des douzièmes de fiscalité .{0,200}"
             r"ainsi que sur le montant des fractions de taxe sur la valeur ajoutée",
             "contribution progressive : imputée sur les douzièmes de fiscalité et les fractions de TVA (art. 37, V)"),
            (r"Le montant de la contribution est égal au produit de ce taux par le montant des recettes réelles de "
             r"fonctionnement du budget principal de l'antépénultième exercice",
             "contribution progressive : assiette = recettes réelles de fonctionnement de l'antépénultième exercice")):
        if not re.search(motif, plf):
            fail("projet de loi de finances : %s introuvable dans l'archive" % quoi)
    src_plf = "projet de loi de finances pour %d, " % n
    mesures = [
        {"cle": "cpeb", "mesure": "Contribution progressive à l'effort budgétaire, prélevée sur les avances de fiscalité",
         "texte": "article 37", "nature": "prélèvement sur les avances de fiscalité, institué pour %d" % n, "md": cpeb,
         "source": src_plf + "article 37, exposé des motifs"},
        {"cle": "fctva", "mesure": "Fonds de compensation pour la TVA : taux abaissé de %d points, sauf dépenses vertes et voirie"
                                    % fctva_pts,
         "texte": "articles 35 et 41", "nature": "réduction d'un concours de l'État lié aux dépenses d'investissement éligibles", "md": fctva,
         "source": src_plf + "article 41, exposé des motifs"},
        {"cle": "tva", "mesure": "TVA affectée, hors régions : hausse annuelle réduite de l'inflation",
         "texte": "article 36", "nature": "écrêtement de la progression de la TVA affectée, hors régions", "md": tva,
         "source": "Haut Conseil des finances publiques, avis n° 2026-5"},
        {"cle": "ministeres", "mesure": "Contributions de certains ministères aux collectivités",
         "texte": "crédits des missions", "nature": "réduction de contributions de certains ministères", "md": minist,
         "source": "Haut Conseil des finances publiques, avis n° 2026-5"},
        {"cle": "dilico", "mesure": "Sommes mises en réserve en 2025 et 2026 (DILICO) : reversement sur cinq ans au lieu de trois",
         "texte": "article 84", "nature": "étalement du reversement ; montant total restitué inchangé", "md": dilico,
         "source": "Haut Conseil des finances publiques, avis n° 2026-5"},
    ]
    # Libelles de la page anglaise : memes mesures, meme ordre, memes nombres (lus ci-dessus).
    en = {
        "cpeb": ("Progressive contribution to the budgetary effort, levied on tax advances", "article 37",
                 "levy on tax advances, introduced for %d" % n),
        "fctva": ("VAT compensation fund: rate cut by %d percentage points, except green spending and roads" % fctva_pts,
                  "articles 35 and 41", "cut in a central government grant tied to eligible investment spending"),
        "tva": ("Assigned VAT, excluding regions: annual increase reduced by inflation", "article 36",
                "capping of the growth of assigned VAT, excluding regions"),
        "ministeres": ("Contributions of certain ministries to local authorities", "appropriations under State budget missions",
                       "cut in contributions from certain ministries"),
        "dilico": ("Sums placed in reserve in 2025 and 2026 (DILICO): repaid over five years instead of three", "article 84",
                   "repayment spread out; total amount returned unchanged"),
    }
    for m_ in mesures:
        m_["mesure_en"], m_["texte_en"], m_["nature_en"] = en[m_["cle"]]
    depot =re.search(r"déposé le (.+)$", a["plf"]["titre"])
    if not depot:
        fail("projet de loi de finances : date de dépôt introuvable dans le titre de l'archive")
    # La page cite ces deux documents par leur adresse : texte fige autour de montants qui changent a chaque edition.
    page = (Path(__file__).resolve().parent.parent / "content" / "dette-publique-collectivites-locales" / "_index.md")
    contenu = page.read_text(encoding="utf-8")
    for doc in ("plf", "hcfp"):
        if a[doc]["url"] not in contenu:
            fail("projet de loi de finances : la page ne cite pas la source archivée (%s) — nouvelle édition ? relire la "
                 "section « projet de loi de finances »" % a[doc]["url"])
    return {"plf_edition": n, "plf_depot": depot.group(1).replace(" ", "\u00a0"),  # insecables en caractere : le jeton sert aussi au JSON-LD
            "plf_dgf": dgf, "plf_dgf_hausse_m": dgf_hausse, "plf_dgf_hausse_courant_m": dgf_hausse_courant, "plf_cpeb": cpeb,
            "plf_cpeb_communes_pct": part_com, "plf_cpeb_dep_pct": part_dep, "plf_fctva": fctva, "plf_fctva_pts": fctva_pts,
            "plf_tva": tva, "plf_ministeres": minist, "plf_dilico": dilico, "plf_regions_m": regions,
            "plf_psr": psr, "plf_psr_lfi_prec": psr_lfi / 1000, "plf_psr_rev_prec": psr_rev / 1000,
            "plf_psr_tableau": psr_tab / 1000,
            "plf_ressources_md": res_md, "plf_ressources_pct": res_pct,
            "plf_inv_n_pct": -inv_n, "plf_inv_n1_pct": -inv_n1, "plf_temoin_cpeb": h_cpeb, "plf_temoin_fctva": h_fctva,
            "plf_mesures": mesures, "plf_somme": sum(m_["md"] for m_ in mesures),
            "plf_sources": {"plf": {k: a["plf"][k] for k in ("titre", "url", "sha256_pdf")},
                            "hcfp": {k: a["hcfp"][k] for k in ("titre", "url", "sha256_pdf")}}}


def calculer(J: Jeu) -> tuple[dict, list[dict]]:
    G = "FR"
    an_fin = max(J.annees(G, "S1313", "P51G"))
    an_dette_fin = max(J.dette_annees(G, "S1313"))
    an_dette_deb = min(J.dette_annees(G, "S1313"))
    r: dict = {"an_fin": an_fin, "an_dette_fin": an_dette_fin, "an_dette_deb": an_dette_deb}

    # 1. Stock : dette des collectivites contre dette publique
    r["dette_apu_deb"] = J.dette(G, "S13", an_dette_deb)
    r["dette_apu_fin"] = J.dette(G, "S13", an_dette_fin)
    r["dette_loc_deb"] = J.dette(G, "S1313", an_dette_deb)
    r["dette_loc_fin"] = J.dette(G, "S1313", an_dette_fin)
    r["part_loc_deb"] = 100 * r["dette_loc_deb"] / r["dette_apu_deb"]
    r["part_loc_fin"] = 100 * r["dette_loc_fin"] / r["dette_apu_fin"]
    r["delta_apu"] = r["dette_apu_fin"] - r["dette_apu_deb"]
    r["delta_loc"] = r["dette_loc_fin"] - r["dette_loc_deb"]
    r["part_hausse_loc"] = 100 * r["delta_loc"] / r["delta_apu"]

    # 2. Investissement : part des collectivites dans l'investissement public
    r["inv_loc_fin"] = J.pc(G, "S1313", "P51G", an_fin)
    r["part_inv_loc_fin"] = 100 * J.mio(G, "S1313", "P51G", an_fin) / J.mio(G, "S13", "P51G", an_fin)

    # 3. L'episode 2013-2017 : decomposition de la variation du solde local (identite TR - TE = B9)
    a0, a1 = EPISODE
    def delta(i):
        return J.pc(G, "S1313", i, a1) - J.pc(G, "S1313", i, a0)
    impots = lambda y: sum(J.pc(G, "S1313", i, y) or 0 for i in ("D2REC", "D5REC", "D91REC"))
    d_tr, d_te = delta("TR"), delta("TE")
    d_transf = delta("D73REC")
    d_imp = impots(a1) - impots(a0)
    d_inv = delta("P51G")
    cascade = [
        ("Transferts reçus des autres administrations publiques", d_transf, "rec"),
        ("Impôts locaux et partagés", d_imp, "rec"),
        ("Autres recettes", d_tr - d_transf - d_imp, "rec"),
        ("Investissement (moins de dépense)", -d_inv, "dep"),
        ("Autres dépenses (moins de dépense)", -(d_te - d_inv), "dep"),
    ]
    r["ep_a0"], r["ep_a1"] = a0, a1
    r["ep_transf_md"] = -(J.mio(G, "S1313", "D73REC", a1) - J.mio(G, "S1313", "D73REC", a0)) / 1000
    r["ep_inv_md"] = -(J.mio(G, "S1313", "P51G", a1) - J.mio(G, "S1313", "P51G", a0)) / 1000
    r["ep_transf"] = d_transf
    r["ep_inv"] = d_inv
    r["ep_te"] = d_te
    r["ep_imp"] = d_imp
    r["ep_solde_a0"] = J.pc(G, "S1313", "B9", a0)
    r["ep_solde_a1"] = J.pc(G, "S1313", "B9", a1)
    r["ep_solde_delta"] = r["ep_solde_a1"] - r["ep_solde_a0"]
    r["ep_etat_delta"] = J.pc(G, "S1311", "B9", a1) - J.pc(G, "S1311", "B9", a0)
    r["ep_cascade"] = [{"poste": p, "pt_pib": v, "cote": c} for p, v, c in cascade]
    # 3 bis. La MEME cascade en milliards d'euros courants (refonte du 11/10/2026, B1) : memes postes, meme ordre, meme
    # convention de signe (contribution a la variation du solde). Une lecture en points de PIB n'est pas une lecture en
    # euros : le denominateur change (PIB nominal en hausse), le numerateur peut rester stable.
    def dmd(i):
        return (J.mio(G, "S1313", i, a1) - J.mio(G, "S1313", i, a0)) / 1000
    imp_md = sum(dmd(i) for i in ("D2REC", "D5REC", "D91REC"))
    tr_md, te_md, inv_md, transf_md = dmd("TR"), dmd("TE"), dmd("P51G"), dmd("D73REC")
    cascade_md = [transf_md, imp_md, tr_md - transf_md - imp_md, -inv_md, -(te_md - inv_md)]
    r["ep_cascade_md"] = [{"poste": c_["poste"], "md_eur": v_, "cote": c_["cote"]} for c_, v_ in zip(r["ep_cascade"], cascade_md)]
    r["ep_tr_md"], r["ep_te_md"], r["ep_imp_md"], r["ep_solde_md"] = tr_md, te_md, imp_md, dmd("B9")
    r["ep_te0_md"] = J.mio(G, "S1313", "TE", a0) / 1000
    r["ep_solde_a0_md"], r["ep_solde_a1_md"] = J.mio(G, "S1313", "B9", a0) / 1000, J.mio(G, "S1313", "B9", a1) / 1000
    r["ep_inv_pct_eur"] = 100 * inv_md / (J.mio(G, "S1313", "P51G", a0) / 1000)
    r["cascade_md_somme"] = sum(cascade_md)
    # Effet du denominateur, sur le PIB MEME des points de la cascade (implicite des comptes publics) : la variation d'un
    # ratio X/Y se partage exactement en (X1 - X0)/Y1 (variation en euros) + X0 (1/Y1 - 1/Y0) (croissance du PIB).
    y0_, y1_ = J.pib[(G, a0)], J.pib[(G, a1)]
    x0_ = J.mio(G, "S1313", "TE", a0)
    r["ep_te_effet_eur"] = 100 * (J.mio(G, "S1313", "TE", a1) - x0_) / y1_
    r["ep_te_effet_pib"] = 100 * x0_ * (1 / y1_ - 1 / y0_)
    # Croissance du PIB nominal dite sur la page : PIB de la NOTIFICATION (regle 4 du modele) ; le PIB implicite des
    # points de la cascade en est le temoin (meme millesime a 0,3 point de croissance pres, garde).
    pn0, pn1 = J.notif.get(("S1", "B1GQ", "MIO_NAC", a0)), J.notif.get(("S1", "B1GQ", "MIO_NAC", a1))
    if not (pn0 and pn1):
        fail("notification : PIB nominal %d ou %d absent (gov_10dd_edpt1, S1, B1GQ, MIO_NAC)" % (a0, a1))
    r["pib_croiss_pct"] = 100 * (pn1 / pn0 - 1)
    r["pib_croiss_impl_pct"] = 100 * (y1_ / y0_ - 1)
    r["ep_te_pc_a1"] = J.pc(G, "S1313", "TE", a1)
    # Temoin comptable, independant de la decomposition : TR - TE doit redonner B9, chaque annee, en millions d'euros.
    residus = []
    for y in J.annees(G, "S1313", "B9"):
        tr, te, b9 = J.mio(G, "S1313", "TR", y), J.mio(G, "S1313", "TE", y), J.mio(G, "S1313", "B9", y)
        if None not in (tr, te, b9):
            residus.append(abs(tr - te - b9))
    r["temoin_residu_max_meur"] = max(residus)
    r["temoin_annees"] = len(residus)
    r["cascade_somme"] = sum(v for _, v, _ in cascade)
    # Temoin du denominateur : PIB implicite des comptes publics contre PIB des comptes nationaux (nama_10_gdp).
    ec = {g: max(abs(J.pib[(g, y)] / J.pib_nama[(g, y)] - 1) for (gg, y) in J.pib if gg == g and (g, y) in J.pib_nama and y >= 1995) for g in GEO}
    r["temoin_pib_ecart_pct"] = {g: 100 * v for g, v in ec.items()}

    # 4. Temoin du cycle electoral : chaque creux d'investissement apres municipales
    cycles = []
    for m in MUNICIPALES:
        pic = J.pc(G, "S1313", "P51G", m - 1)
        fen = [(y, J.pc(G, "S1313", "P51G", y)) for y in range(m, m + 3) if J.pc(G, "S1313", "P51G", y) is not None]
        ycreux, creux = lg.extremum(fen, lambda t: t[1], 2, maxi=False)   # creux publié à 2 décimales (coll-tableau)
        cycles.append({"municipales": m, "pic_annee": m - 1, "pic": pic, "creux_annee": ycreux, "creux": creux, "baisse": creux - pic})
    r["cycles"] = cycles
    c14 = next(c for c in cycles if c["municipales"] == 2014)
    autres = [c for c in cycles if c["municipales"] != 2014]
    r["creux14_baisse"] = c14["baisse"]
    r["creux14_annee"] = c14["creux_annee"]
    r["creux_autres_max"] = min(c["baisse"] for c in autres)  # la plus forte baisse des autres cycles (valeur la plus negative)
    r["creux_ratio"] = c14["baisse"] / r["creux_autres_max"]

    # 5. Rupture de 2021 : fraction de TVA en remplacement de la taxe d'habitation (transfert -> impot)
    r["rupt_transf"] = J.pc(G, "S1313", "D73REC", 2021) - J.pc(G, "S1313", "D73REC", 2020)
    r["rupt_imp"] = impots(2021) - impots(2020)

    # 6. Regime recent
    recents = [an_fin - 2, an_fin - 1, an_fin]
    r["recent_annees"] = recents
    r["recent_soldes"] = [J.pc(G, "S1313", "B9", y) for y in recents]
    r["recent_solde_fin"] = J.pc(G, "S1313", "B9", an_fin)
    r["recent_inv_deb"] = J.pc(G, "S1313", "P51G", an_fin - 2)
    r["recent_dette_deb"] = J.dette(G, "S1313", an_dette_fin - 2)
    # Pic de 2010 en milliards : temoin de l'ordre de grandeur avance par la contre-expertise (non verifie a la source)
    r["pic2010_md"] = (J.mio(G, "S1313", "D73REC", 2010) - J.mio(G, "S1313", "D73REC", 2009)) / 1000

    # 7. Comparaison europeenne a PERIMETRE TERRITORIAL : S1312 (Etats federes, DE et ES) + S1313 (administrations locales).
    # La France et l'Italie n'ont pas de S1312 (regions classees en S1313) : leur S1313 EST leur perimetre territorial.
    # Correction du tour 1 de contre-expertise (01/10/2026) : la version S1313 seule comparait des perimetres differents.
    # Somme non consolidee entre S1312 et S1313 (prets entre echelons) : limite declaree.
    def terr_dette(g, y):
        v = [J.dette(g, s, y) for s in ("S1312", "S1313")]
        return None if v[1] is None else (v[0] or 0) + v[1]

    def terr_pc(g, i, y):
        v = [J.pc(g, s, i, y) for s in ("S1312", "S1313")]
        return None if v[1] is None else (v[0] or 0) + v[1]

    pays = []
    for g in GEO:
        ys = [y for y in J.dette_annees(g, "S1313") if y >= an_dette_deb]  # meme annee de depart pour les quatre pays
        serie = {y: terr_dette(g, y) for y in ys}
        serie_loc = {y: J.dette(g, "S1313", y) for y in ys}
        ypic = lg.extremum(serie, serie.get, 1)
        inv = {y: terr_pc(g, "P51G", y) for y in J.annees(g, "S1313", "P51G") if y >= 2000}
        inv_avant = {y: v for y, v in inv.items() if y <= 2010}
        inv_apres = {y: v for y, v in inv.items() if 2011 <= y <= 2019}
        # Années du maximum et du minimum : toutes celles qui s'affichent à égalité (plateau), la première sert au calcul ;
        # la valeur publiée est la même pour toutes (contre-expertise anthropie-site-20261016-154235, point 8).
        # Les VALEURS restent les extremums exacts (la baisse publiée se calcule sur elles) ; seul le libellé des années
        # dit le plateau.
        ans_max, ans_min = lg.sommets(inv_avant, 1), lg.sommets(inv_apres, 1, maxi=False)
        yi_max = max(inv_avant, key=inv_avant.get)  # brut-ok: valeur exacte du maximum ; ses annees publiees = ans_max
        yi_min = min(inv_apres, key=inv_apres.get)  # brut-ok: valeur exacte du minimum ; ses annees publiees = ans_min
        excedents = sum(1 for y in range(2012, 2020) if (terr_pc(g, "B9", y) or 0) > 0)
        federe = J.dette(g, "S1312", max(ys)) is not None
        pays.append({
            "geo": g, "nom": NOMS[g], "nom_en": NOMS_EN[g], "federe": federe,
            "dette_deb": serie[min(ys)], "dette_pic": serie[ypic], "dette_pic_annee": ypic, "dette_fin": serie[max(ys)],
            "inv_max": inv_avant[yi_max], "inv_max_annee": yi_max, "inv_min": inv_apres[yi_min], "inv_min_annee": yi_min,
            "inv_max_annees": ans_max, "inv_min_annees": ans_min,
            "inv_rapport": inv_apres[yi_min] / inv_avant[yi_max],
            "excedents_2012_2019": excedents,
            "dette_loc_fin": serie_loc[max(ys)],
            "serie_dette": serie, "serie_dette_loc": serie_loc,
        })
    r["pays"] = pays
    P = {p["geo"]: p for p in pays}

    # 7 bis. Consolidation entre echelons (tour 2, P0) et detention par l'Etat central (architecture territoriale)
    an_ggd = max(y for (g, s_, c, y) in J.ggd)
    croise = []
    for g in ("DE", "ES"):
        # Fenetre de la comparaison publiee (depuis an_dette_deb) : en Allemagne, 1995-1999 montent a 0,3 point,
        # hors du champ de la figure.
        for y in sorted({y for (gg, s_, c, y) in J.ggd if gg == g and y >= an_dette_deb}):
            a_ = J.detenu(g, "S1312", "S1313", y)
            b_ = J.detenu(g, "S1313", "S1312", y)
            if a_ is not None or b_ is not None:
                croise.append((a_ or 0) + (b_ or 0))
    r["consolidation_ecart_max"] = max(croise)
    r["an_ggd"] = an_ggd
    for p in pays:
        g = p["geo"]
        # Denominateur : dette territoriale du 4e trimestre (meme definition pour les quatre pays ; le total par
        # detenteur S1_S2 n'est pas publie pour la France). Temoin : la ou S1_S2 existe, il doit concorder.
        tot = p["serie_dette"][an_ggd]
        par_detenteur = [J.detenu(g, s_, "S1_S2", an_ggd) for s_ in ("S1312", "S1313")]
        if J.dette(g, "S1312", an_ggd) is None:
            par_detenteur = par_detenteur[1:]
        if all(v is not None for v in par_detenteur):
            p["temoin_detenteur_ecart"] = abs(sum(par_detenteur) - tot)
        etat = sum(J.detenu(g, s_, "S1311", an_ggd) or 0 for s_ in ("S1312", "S1313"))
        p["detenu_etat"] = etat
        p["detenu_total"] = tot
        p["part_etat_pct"] = 100 * etat / tot if tot else None
        p["serie_detenu_etat"] = {y: sum(J.detenu(g, s_, "S1311", y) or 0 for s_ in ("S1312", "S1313"))
                                  for y in sorted({y for (gg, s_, c, y) in J.ggd if gg == g and c == "S1311"})}

    # 8. Deux recits : la depense locale en part de PIB, sur la plus longue serie
    te = {y: J.pc(G, "S1313", "TE", y) for y in J.annees(G, "S1313", "TE")}
    a_te0 = min(te)
    te_pics = lg.sommets(te, 1)                 # 11,8 % en 2009 et en 2013 (données du 16/10/2026) : les deux se disent
    a_tepic = te_pics[0]
    r["te_a0"], r["te_0"], r["te_apic"], r["te_pic"], r["te_fin"] = a_te0, te[a_te0], a_tepic, te[a_tepic], te[an_fin]
    r["te_apics"] = te_pics

    # 9. OFGL : la maille des praticiens (milliards d'euros courants)
    r["of_dgf_dep_13"], r["of_dgf_dep_17"] = J.of("departements", "Dotation globale de fonctionnement", 2013), J.of("departements", "Dotation globale de fonctionnement", 2017)
    r["of_dgf_reg_13"], r["of_dgf_reg_17"] = J.of("regions", "Dotation globale de fonctionnement", 2013), J.of("regions", "Dotation globale de fonctionnement", 2017)
    r["of_dgf_reg_18"], r["of_tva_reg_18"] = J.of("regions", "Dotation globale de fonctionnement", 2018), J.of("regions", "TVA", 2018)
    eb = {y: J.of("departements", "Epargne brute", y) for y in J.of_annees("departements", "Epargne brute") if y >= 2018}
    a_ebpic = lg.extremum(eb, eb.get, 1)
    a_ebmin = lg.extremum((y for y in eb if y > a_ebpic), eb.get, 1, maxi=False)
    an_of = max(eb)
    r["of_an"], r["of_eb_dep_apic"], r["of_eb_dep_pic"] = an_of, a_ebpic, eb[a_ebpic]
    r["of_eb_dep_amin"], r["of_eb_dep_min"], r["of_eb_dep_fin"] = a_ebmin, eb[a_ebmin], eb[an_of]
    eq = {y: J.of("communes", "Dépenses d'équipement", y) for y in J.of_annees("communes", "Dépenses d'équipement")}
    r["of_eq_com_20"], r["of_eq_com_fin"] = eq[2020], eq[an_of]
    cats = []
    for cat, nom in (("communes", "Communes"), ("intercommunalites", "Intercommunalités"), ("departements", "Départements"), ("regions", "Régions")):
        row = {"cat": cat, "nom": nom, "nom_en": CATS_EN[cat]}
        for ag, k in (("Epargne brute", "eb"), ("Dépenses d'équipement", "eq"), ("Encours de dette", "dette"), ("Concours de l'Etat", "concours")):
            row[k + "_21"] = J.of(cat, ag, 2021)
            row[k + "_fin"] = J.of(cat, ag, an_of)
        cats.append(row)
    r["categories"] = cats
    # 10. DGF votee (Legifrance) : troisieme mesure, distincte de la CRFP et de la DGF comptabilisee
    dv = dgf_votee()
    r["dgf_vote"] = {a: dv[a] for a in range(2013, 2018)}
    r["dgf_vote_baisses"] = [dv[a] - dv[a - 1] for a in range(2014, 2018)]
    # 11. Ecart documente, jamais corrige : somme des encours OFGL contre dette Maastricht des administrations locales
    r["of_encours_total"] = sum(c["dette_fin"] for c in cats)
    r["dette_loc_md"] = r["dette_loc_fin"] / 100 * J.pib[(G, an_dette_fin)] / 1000

    # 12. Refonte du 11/10/2026. « Depuis 2023 » : ce qui est observable dans les quatre categories (encours OFGL), sans
    # attribuer par difference le reste de la hausse aux organismes divers (consolidation et conventions differentes).
    a_rec0 = an_dette_fin - 2
    r["of_encours_rec0_annee"] = a_rec0
    r["of_encours_rec0"] = sum(J.of(c_, "Encours de dette", a_rec0) for c_ in OFGL_BASES)
    # B15 : « le besoin de financement se creuse » -- etat des deux annees precedant la fenetre recente
    r["avant_soldes"] = [J.pc(G, "S1313", "B9", y) for y in (an_fin - 4, an_fin - 3)]
    r["avant_annees"] = [an_fin - 4, an_fin - 3]
    # B5 : dette publique de fin de periode, serie trimestrielle (page) contre notification (autres volets), datees
    r["dette_maj"], r["notif_maj"] = J.b["dette"]["maj_eurostat"][:10], J.b["notif"]["maj_eurostat"][:10]
    r["dette_apu_notif_fin"] = J.notif.get(("S13", "GD", "PC_GDP", an_dette_fin))
    if r["dette_apu_notif_fin"] is None:
        fail("notification : dette publique %d absente (gov_10dd_edpt1, S13, GD, PC_GDP)" % an_dette_fin)
    r.update(textes_regles())
    if MUTATION == "cahors":  # temoin : la suspension ne porterait plus sur la derniere annee des contrats
        r["cahors_suspendu"] -= 1

    # Series des figures
    r["serie_inv_fr"] = {y: J.pc(G, "S1313", "P51G", y) for y in J.annees(G, "S1313", "P51G")}
    r["serie_transf_fr"] = {y: J.pc(G, "S1313", "D73REC", y) for y in J.annees(G, "S1313", "D73REC") if y <= 2017}

    # ------------------------------------------------------------ gardes : chaque qualificatif de la prose
    gardes = [
        ("« la dette publique a presque doublé »", 1.6 <= r["dette_apu_fin"] / r["dette_apu_deb"] < 2.0),
        ("carte de partage : « la dette locale est restée contenue » (moins d'un dixième de la hausse de la dette publique)", 0 <= r["part_hausse_loc"] < 10),
        ("« moins d'un dixième de la dette publique »", r["part_loc_fin"] < 10),
        ("« environ la moitié de l'investissement public »", 45 <= r["part_inv_loc_fin"] <= 60),
        ("« les transferts reçus ont baissé » (2013-2017)", r["ep_transf"] <= -0.3),
        ("« l'investissement local a reculé » (2013-2017)", r["ep_inv"] <= -0.3),
        ("« leur solde s'est amélioré » (2013-2017)", r["ep_solde_delta"] > 0),
        ("« jusqu'à un léger excédent »", 0 < r["ep_solde_a1"] < 0.3),
        ("« un pic isolé en 2010 » (annotation de la figure : compensation de la taxe professionnelle)", lg.extremum(r["serie_transf_fr"], r["serie_transf_fr"].get, 1) == 2010),
        ("« plus du double de la plus forte baisse des autres mandats »", r["creux_ratio"] >= 2),
        ("« en points de PIB, les impôts n'ont compensé qu'une partie de la baisse des transferts »", 0 < r["ep_imp"] < -r["ep_transf"]),
        ("« en euros, la hausse des impôts dépasse la baisse des transferts »", r["ep_imp_md"] > -r["ep_cascade_md"][0]["md_eur"] > 0),
        ("« en 2021, une recette a changé de case » (transferts en baisse, impôts en hausse)", r["rupt_transf"] <= -0.4 and r["rupt_imp"] >= 0.4),
        ("« depuis trois ans, le besoin de financement des administrations locales dépasse 0,3 point de PIB ; il était inférieur à "
         "0,1 point les deux années précédentes »", all(s < -0.3 for s in r["recent_soldes"]) and all(-0.1 < s <= 0 for s in r["avant_soldes"])),
        ("« Italie : dette territoriale redescendue nettement sous son pic »", P["IT"]["dette_fin"] < P["IT"]["dette_pic"] - 2),
        ("« Italie : huit années d'excédent sur huit (2012-2019) ; France : quatre au plus »", P["IT"]["excedents_2012_2019"] == 8 and P["FR"]["excedents_2012_2019"] <= 4),
        ("« Italie : investissement territorial divisé par deux »", 0.45 <= P["IT"]["inv_rapport"] <= 0.55),
        ("« Espagne : dette territoriale plus que doublée depuis 2000 »", P["ES"]["dette_fin"] >= 2 * P["ES"]["dette_deb"]),
        ("« Espagne : investissement territorial réduit de près des deux tiers »", 0.3 <= P["ES"]["inv_rapport"] <= 0.4),
        ("« Allemagne : dette territoriale nettement sous son pic »", P["DE"]["dette_fin"] < P["DE"]["dette_pic"] - 5),
        ("« pas de classement unique » : l'ordre des pays change d'un indicateur à l'autre",
         [p["geo"] for p in sorted(pays, key=lambda p: p["inv_rapport"])] != [p["geo"] for p in sorted(pays, key=lambda p: -p["excedents_2012_2019"])]
         or [p["geo"] for p in sorted(pays, key=lambda p: p["inv_rapport"])] != [p["geo"] for p in sorted(pays, key=lambda p: p["dette_fin"])]),
        ("consolidation entre échelons : dettes croisées S1312/S1313 ≤ 0,2 point (sinon l'agrégat brut ment)", r["consolidation_ecart_max"] <= 0.2),
        ("témoin du dénominateur : dette par détenteur (gov_10dd_ggd) = dette trimestrielle T4, à 0,2 point près, partout où les deux existent",
         all(p.get("temoin_detenteur_ecart", 0) <= 0.2 for p in pays) and sum(1 for p in pays if "temoin_detenteur_ecart" in p) >= 2),
        ("« Espagne : plus de la moitié de la dette territoriale détenue par l'État central »", P["ES"]["part_etat_pct"] > 50),
        ("« Italie : environ un quart » détenu par l'État central", 15 <= P["IT"]["part_etat_pct"] <= 35),
        ("« France et Allemagne : part quasi nulle » détenue par l'État central", P["FR"]["part_etat_pct"] < 5 and P["DE"]["part_etat_pct"] < 5),
        ("« la dépense locale a augmenté puis reculé » (deux récits)", r["te_pic"] - r["te_0"] >= 1.5 and r["te_pic"] - r["te_fin"] >= 0.3),
        ("« DGF des départements et des régions en baisse de 2013 à 2017 » (OFGL)", r["of_dgf_dep_17"] < r["of_dgf_dep_13"] - 2 and r["of_dgf_reg_17"] < r["of_dgf_reg_13"] - 1),
        ("« 2018 : la DGF des régions disparaît presque, une fraction de TVA la remplace » (OFGL)", r["of_dgf_reg_18"] < 1 and r["of_tva_reg_18"] > 3),
        ("« épargne brute des départements divisée par plus de deux » (OFGL)", r["of_eb_dep_pic"] >= 2 * r["of_eb_dep_min"]),
        ("« puis remonte » (dernier exercice OFGL au-dessus du creux)", lg.depasse(r["of_eb_dep_fin"], r["of_eb_dep_min"])),
        ("« la DGF votée baisse chaque année de 2014 à 2017, de plus de 10 milliards au total » (CGCT L. 1613-1)",
         all(d < 0 for d in r["dgf_vote_baisses"]) and r["dgf_vote"][2013] - r["dgf_vote"][2017] > 10),
        ("« la somme des quatre catégories n'atteint pas la dette Maastricht des administrations locales »",
         lg.depasse(r["dette_loc_md"], r["of_encours_total"], 0)),
        ("« équipement des communes en hausse de plus de 40 % depuis 2020 » (OFGL)", r["of_eq_com_fin"] >= 1.4 * r["of_eq_com_20"]),
        ("« depuis trois ans, le stock de dette locale augmente de nouveau »", J.dette(G, "S1313", an_dette_fin) > J.dette(G, "S1313", an_dette_fin - 2)),
        ("témoin du PIB (France) : comptes publics et comptes nationaux à 0,5 % près", r["temoin_pib_ecart_pct"]["FR"] <= 0.5),
        ("témoin comptable : TR − TE = B9 (écart ≤ 1 M€)", r["temoin_residu_max_meur"] <= 1.0),
        ("la cascade se referme sur le solde", abs(r["cascade_somme"] - r["ep_solde_delta"]) < 1e-9),
        # ---- refonte du 11/10/2026 (B1 : les deux unités ; B10, B15 ; Cahors ; « Depuis 2023 »)
        ("la cascade en euros se referme sur le solde (écart < 0,1 M€)", abs(r["cascade_md_somme"] - r["ep_solde_md"]) < 1e-4),
        ("« dépenses totales presque stables en euros courants » (variation de moins de 1 %)",
         abs(r["ep_te_md"]) < 0.01 * r["ep_te0_md"]),
        ("« rapportées au PIB, leurs dépenses ont diminué »", r["ep_te"] < -0.3),
        ("« les recettes fiscales progressaient » (en euros)", r["ep_imp_md"] > 0),
        ("« les transferts reçus reculaient » (en euros)", r["ep_cascade_md"][0]["md_eur"] < 0),
        ("« en euros, la progression des recettes explique l'essentiel du redressement du solde » (recettes > 2 × dépenses)",
         r["ep_tr_md"] > 0 and r["ep_tr_md"] > 2 * abs(r["ep_te_md"])),
        ("« les autres dépenses augmentent en euros et reculent en points de PIB » (le signe change avec l'unité)",
         r["ep_cascade_md"][4]["md_eur"] < 0 < r["ep_cascade"][4]["pt_pib"]),
        ("« l'investissement recule aussi en euros »", r["ep_inv_md"] > 0 and r["ep_inv_pct_eur"] < -5),
        ("effet du dénominateur : variation en euros + croissance du PIB = variation en points (identité)",
         abs(r["ep_te_effet_eur"] + r["ep_te_effet_pib"] - r["ep_te"]) < 1e-9),
        ("« l'essentiel du recul en points de PIB vient de la croissance du PIB » (effet du PIB > recul total)",
         r["ep_te_effet_pib"] < r["ep_te"] < 0 < r["ep_te_effet_eur"]),
        ("témoin du PIB : croissance 2013-2017 de la notification et du PIB implicite des comptes à 0,3 point près",
         abs(r["pib_croiss_pct"] - r["pib_croiss_impl_pct"]) <= 0.3),
        ("« L'investissement local baisse habituellement après les municipales » (au moins trois mandats sur quatre)",
         sum(1 for c in r["cycles"] if c["baisse"] < 0) >= 3),
        ("« la dépense locale était revenue plus bas en fin d'épisode qu'aujourd'hui » (B15)", lg.depasse(r["te_fin"], r["ep_te_pc_a1"], 1)),
        ("« Depuis 2023 : l'encours des quatre catégories (OFGL) augmente aussi »", lg.depasse(r["of_encours_total"], r["of_encours_rec0"], 1)),
        ("dette publique : série trimestrielle et notification à 0,2 point près (écart dit sur la page, jamais corrigé)",
         abs(r["dette_apu_fin"] - r["dette_apu_notif_fin"]) <= 0.2),
        ("« le stock de dette locale a augmenté en 2020 et depuis 2023 » (la règle d'équilibre ne fige pas le stock)",
         J.dette(G, "S1313", 2020) > J.dette(G, "S1313", 2019) and J.dette(G, "S1313", an_dette_fin) > J.dette(G, "S1313", 2023)),
        ("« Les deux lectures ne racontent pas la même chose » : en euros, les dépenses ne reculent pas",
         r["ep_te_md"] >= 0 > r["ep_te"]),
        ("Cahors : trois exercices contractuels, la reprise de la dernière année suspendue par la loi d'urgence",
         len(r["cahors_exercices"]) == 3 and r["cahors_suspendu"] == r["cahors_exercices"][-1]),
    ]
    r.update(plf_mesures())
    gardes += [
        ("projet de loi de finances : « la DGF augmente » (abondements et montant à périmètre courant)",
         r["plf_dgf_hausse_m"] > 0 and r["plf_dgf_hausse_courant_m"] > 0),
        ("projet de loi de finances : « les prélèvements sur recettes au profit des collectivités baissent » (contre la "
         "prévision révisée et contre la loi de finances initiale de l'année en cours)",
         r["plf_psr"] < r["plf_psr_rev_prec"] < r["plf_psr_lfi_prec"]),
        ("projet de loi de finances : témoin entre sources — la contribution progressive est chiffrée au même montant par le "
         "projet de loi et par le Haut Conseil", abs(r["plf_cpeb"] - r["plf_temoin_cpeb"]) < 0.05),
        ("projet de loi de finances : témoin entre sources — FCTVA, projet de loi et Haut Conseil à 0,05 Md€ près",
         abs(r["plf_fctva"] - r["plf_temoin_fctva"]) < 0.05),
        ("projet de loi de finances : témoin interne — l'article et le tableau des recettes donnent le même total de "
         "prélèvements sur recettes", abs(r["plf_psr"] - r["plf_psr_tableau"]) < 0.001),
        ("projet de loi de finances : « l'investissement local reculerait deux années de suite » (Haut Conseil)",
         r["plf_inv_n_pct"] < 0 and r["plf_inv_n1_pct"] < 0),
        ("projet de loi de finances : « des ressources en hausse malgré la contribution » (lecture du Gouvernement)",
         r["plf_ressources_md"] > 0),
        ("projet de loi de finances : « augmenter de X alors que la somme arithmétique des mesures atteint Y » (Y > X > 0 ; "
         "leur différence n'est jamais présentée comme un montant prélevé : garde de prose)",
         r["plf_somme"] > r["plf_ressources_md"] > 0),
        ("projet de loi de finances : somme arithmétique des cinq montants = somme des lignes du tableau",
         abs(r["plf_somme"] - sum(m_["md"] for m_ in r["plf_mesures"])) < 1e-9 and len(r["plf_mesures"]) == 5),
        ("projet de loi de finances : la somme affichée égale la somme des montants affichés (arrondis au dixième)",
         abs(round(sum(round(m_["md"], 1) for m_ in r["plf_mesures"]), 1) - round(r["plf_somme"], 1)) < 1e-9),
    ]
    rapport = [{"garde": g, "ok": bool(ok)} for g, ok in gardes]
    dementies = [g["garde"] for g in rapport if not g["ok"]]
    if dementies:  # toutes les gardes dementies, pas seulement la premiere : une mutation se verifie sur SA garde
        fail("garde dementie par les donnees : " + " | ".join(dementies))
    return r, rapport


def affichage(r: dict, lang: str = "fr") -> dict:
    """Un bloc par langue, memes cles ; seul le format change (en1 : point decimal, separateur de milliers)."""
    P = {p["geo"]: p for p in r["pays"]}
    fr1 = en1 if lang == "en" else globals()["fr1"]  # noqa: F811 -- format de la langue demandee
    a = {
        "an_fin": str(r["an_fin"]), "an_dette_deb": str(r["an_dette_deb"]), "an_dette_fin": str(r["an_dette_fin"]),
        "dette_apu_deb": fr1(r["dette_apu_deb"]), "dette_apu_fin": fr1(r["dette_apu_fin"]),
        "dette_loc_deb": fr1(r["dette_loc_deb"]), "dette_loc_fin": fr1(r["dette_loc_fin"]),
        "delta_apu": fr1(r["delta_apu"], 0), "delta_loc": fr1(r["delta_loc"]),
        "part_loc_deb": fr1(r["part_loc_deb"], 0), "part_loc_fin": fr1(r["part_loc_fin"], 0),
        "part_hausse_loc": fr1(r["part_hausse_loc"], 0),
        "inv_loc_fin": fr1(r["inv_loc_fin"]), "part_inv_loc_fin": fr1(r["part_inv_loc_fin"], 0),
        "ep_a0": str(r["ep_a0"]), "ep_a1": str(r["ep_a1"]),
        "ep_transf": fr1(-r["ep_transf"], 2), "ep_inv": fr1(-r["ep_inv"], 2), "ep_te": fr1(-r["ep_te"], 2),
        "ep_imp": fr1(r["ep_imp"], 2),
        "ep_autres_rec": fr1(-r["ep_cascade"][2]["pt_pib"], 2), "ep_autres_dep": fr1(r["ep_cascade"][4]["pt_pib"], 2),
        "ep_solde_a0": fr1(r["ep_solde_a0"], 2), "ep_solde_a1": fr1(r["ep_solde_a1"], 2),
        "ep_solde_delta": fr1(r["ep_solde_delta"], 2), "ep_etat_delta": fr1(r["ep_etat_delta"], 2),
        "creux14_baisse": fr1(-r["creux14_baisse"], 2), "creux14_annee": str(r["creux14_annee"]),
        "creux_autres_max": fr1(-r["creux_autres_max"], 2), "creux_ratio": fr1(r["creux_ratio"], 1),
        "rupt_transf": fr1(-r["rupt_transf"], 2), "rupt_imp": fr1(r["rupt_imp"], 2),
        "recent_a0": str(r["recent_annees"][0]), "recent_solde_fin": fr1(r["recent_solde_fin"], 2),
        "recent_inv_deb": fr1(r["recent_inv_deb"], 2), "recent_dette_deb": fr1(r["recent_dette_deb"]),
        "pic2010_md": fr1(r["pic2010_md"], 0),
        "temoin_residu": fr1(r["temoin_residu_max_meur"], 1), "temoin_annees": str(r["temoin_annees"]),
        "te_a0": str(r["te_a0"]), "te_0": fr1(r["te_0"]), "te_apic": lg.enumere([str(y) for y in r["te_apics"]], lang), "te_pic": fr1(r["te_pic"]), "te_fin": fr1(r["te_fin"]),
        "an_ggd": str(r["an_ggd"]), "consolidation_ecart": fr1(r["consolidation_ecart_max"]),
        "of_an": str(r["of_an"]),
        "of_dgf_dep_13": fr1(r["of_dgf_dep_13"]), "of_dgf_dep_17": fr1(r["of_dgf_dep_17"]), "of_dgf_dep_baisse": fr1(r["of_dgf_dep_13"] - r["of_dgf_dep_17"]),
        "of_dgf_reg_13": fr1(r["of_dgf_reg_13"]), "of_dgf_reg_17": fr1(r["of_dgf_reg_17"]), "of_dgf_reg_baisse": fr1(r["of_dgf_reg_13"] - r["of_dgf_reg_17"]),
        "of_dgf_reg_18": fr1(r["of_dgf_reg_18"]), "of_tva_reg_18": fr1(r["of_tva_reg_18"]),
        "of_eb_dep_apic": str(r["of_eb_dep_apic"]), "of_eb_dep_pic": fr1(r["of_eb_dep_pic"]), "of_eb_dep_amin": str(r["of_eb_dep_amin"]),
        "of_eb_dep_min": fr1(r["of_eb_dep_min"]), "of_eb_dep_fin": fr1(r["of_eb_dep_fin"]),
        "of_eq_com_20": fr1(r["of_eq_com_20"]), "of_eq_com_fin": fr1(r["of_eq_com_fin"]),
        "of_eq_com_hausse_pct": fr1(100 * (r["of_eq_com_fin"] / r["of_eq_com_20"] - 1), 0),
        "ep_transf_md": fr1(r["ep_transf_md"], 1), "ep_inv_md": fr1(r["ep_inv_md"], 1),
        "dilico_2025": montant_en(dilico_montant()) if lang == "en" else dilico_montant(),
        "plf_edition": str(r["plf_edition"]), "plf_prec": str(r["plf_edition"] - 1), "plf_depot": date_en(r["plf_depot"]) if lang == "en" else r["plf_depot"],
        "plf_dgf": fr1(r["plf_dgf"]), "plf_dgf_hausse_m": fr1(r["plf_dgf_hausse_m"], 0),
        "plf_dgf_hausse_courant_m": fr1(r["plf_dgf_hausse_courant_m"], 0),
        "plf_cpeb": fr1(r["plf_cpeb"]), "plf_cpeb_communes_pct": fr1(r["plf_cpeb_communes_pct"], 0),
        "plf_cpeb_dep_pct": fr1(r["plf_cpeb_dep_pct"], 0),
        "plf_fctva": fr1(r["plf_fctva"]), "plf_fctva_pts": fr1(r["plf_fctva_pts"], 0),
        "plf_tva": fr1(r["plf_tva"]), "plf_ministeres": fr1(r["plf_ministeres"]), "plf_dilico": fr1(r["plf_dilico"]),
        "plf_regions_m": fr1(r["plf_regions_m"], 0), "plf_psr_rev_prec": fr1(r["plf_psr_rev_prec"], 2),
        "plf_psr": fr1(r["plf_psr"]), "plf_psr_lfi_prec": fr1(r["plf_psr_lfi_prec"], 2),
        "plf_ressources_md": fr1(r["plf_ressources_md"], 0), "plf_ressources_pct": fr1(r["plf_ressources_pct"]),
        "plf_inv_n_pct": fr1(-r["plf_inv_n_pct"]), "plf_inv_n1_pct": fr1(-r["plf_inv_n1_pct"]),

        "dgf_vote_13": fr1(r["dgf_vote"][2013]), "dgf_vote_17": fr1(r["dgf_vote"][2017]),
        "dgf_vote_baisse": fr1(r["dgf_vote"][2013] - r["dgf_vote"][2017]),
        "dgf_vote_b14": fr1(-r["dgf_vote_baisses"][0]), "dgf_vote_b15": fr1(-r["dgf_vote_baisses"][1]),
        "dgf_vote_b16": fr1(-r["dgf_vote_baisses"][2]), "dgf_vote_b17": fr1(-r["dgf_vote_baisses"][3]),
        "of_encours_total": fr1(r["of_encours_total"]), "dette_loc_md": fr1(r["dette_loc_md"], 0),
        "of_ecart_maastricht": fr1(r["dette_loc_md"] - r["of_encours_total"], 0),
        "pib_ecart_fr": fr1(r["temoin_pib_ecart_pct"]["FR"], 2), "pib_ecart_de": fr1(r["temoin_pib_ecart_pct"]["DE"], 1),
        "pib_ecart_it": fr1(r["temoin_pib_ecart_pct"]["IT"], 1), "pib_ecart_es": fr1(r["temoin_pib_ecart_pct"]["ES"], 1),
    }
    # ---- cles de la refonte du 11/10/2026 : langue generee par l'organe commun (langue_generee.py), jamais recopiee
    L = "en" if lang == "en" else "fr"

    def pt(v, dec=2):  # « 0,82 point » / « 0.82 points » : accord sur la valeur affichee, sans signe (le verbe porte le sens)
        return lg.points(abs(v), dec, L)

    def mde(v, dec=1, signe=False):  # « 9,7 milliards d'euros » / « €9.7 billion » ; « +1,2 milliard d'euros » / « +€1.2 billion »
        n_ = (lg.signe if signe else lg.nombre)(abs(v) if not signe else v, dec, L)
        if L == "en":
            return (n_[0] if n_[:1] in "+−" else "") + "€" + n_.lstrip("+−") + " billion"
        a_ = abs(float(lg.sans_signe(v, dec, L).replace(lg.NBSP, "").replace(",", ".")))
        return n_ + lg.NBSP + ("milliard" if a_ < 2 else "milliards") + " d’euros"  # apostrophe typographique, comme le texte servi

    def date_txt(iso):
        y_, m_, d_ = (int(x) for x in iso.split("-"))
        return ("%d %s %d" % (d_, MOIS_EN[m_ - 1], y_)) if L == "en" else (("1er" if d_ == 1 else str(d_)) + " %s %d" % (MOIS_FR[m_ - 1], y_))
    cm, cp = r["ep_cascade_md"], r["ep_cascade"]
    a.update({
        "ep_solde_mde": mde(r["ep_solde_md"]), "ep_solde_pt": pt(r["ep_solde_delta"]),
        "ep_tr_mde": mde(r["ep_tr_md"]), "ep_te_mde_s": mde(r["ep_te_md"], signe=True),
        "ep_te0_md": lg.nombre(r["ep_te0_md"], 1, L), "ep_te1_md": lg.nombre(r["ep_te0_md"] + r["ep_te_md"], 1, L),
        "ep_imp_mde": mde(r["ep_imp_md"]), "ep_imp_md": lg.nombre(r["ep_imp_md"], 1, L),
        "recent_a1": str(r["recent_annees"][1]), "recent_solde_mid_pt": pt(r["recent_soldes"][1]), "ep_transf_mde": mde(cm[0]["md_eur"]), "ep_autres_rec_mde": mde(cm[2]["md_eur"]),
        "ep_inv_mde": mde(cm[3]["md_eur"]), "ep_autres_dep_mde": mde(cm[4]["md_eur"]),
        "ep_te_pt": pt(r["ep_te"]), "ep_inv_pt": pt(r["ep_inv"]), "ep_transf_pt": pt(r["ep_transf"]), "ep_imp_pt": pt(r["ep_imp"]),
        "ep_autres_rec_pt": pt(cp[2]["pt_pib"]), "ep_autres_dep_pt": pt(cp[4]["pt_pib"]),
        "ep_solde_a0_md": lg.nombre(abs(r["ep_solde_a0_md"]), 1, L), "ep_solde_a1_md": lg.nombre(r["ep_solde_a1_md"], 1, L),
        "pib_croiss_pct": lg.nombre(r["pib_croiss_pct"], 1, L),
        "ep_te_effet_pib_pt": pt(r["ep_te_effet_pib"]), "ep_te_effet_eur_pt": pt(r["ep_te_effet_eur"]),
        "ep_inv_pct_eur": lg.nombre(abs(r["ep_inv_pct_eur"]), 0, L), "ep_te_pc_a1": lg.nombre(r["ep_te_pc_a1"], 1, L),
        "dette_apu_notif_fin": lg.nombre(r["dette_apu_notif_fin"], 1, L),
        "dette_maj": date_txt(r["dette_maj"]), "notif_maj": date_txt(r["notif_maj"]),
        "avant_a0": str(r["avant_annees"][0]), "avant_a1": str(r["avant_annees"][1]),
        "recent_solde_deb_pt": pt(r["recent_soldes"][0]), "recent_solde_fin_pt": pt(r["recent_solde_fin"]),
        "recent_inv_deb1": lg.nombre(r["recent_inv_deb"], 1, L),
        "of_encours_rec0": lg.nombre(r["of_encours_rec0"], 1, L), "of_encours_rec0_annee": str(r["of_encours_rec0_annee"]),
        "of_encours_hausse": lg.nombre(r["of_encours_total"] - r["of_encours_rec0"], 1, L),
        "consolidation_ecart_pt": lg.points(r["consolidation_ecart_max"], 1, L),
        "plf_somme": lg.nombre(r["plf_somme"], 1, L),
        # Cloture (11/10/2026) : difference entre la somme arithmetique des mesures et la variation annoncee des ressources,
        # citee seulement pour dire qu'elle n'est pas un prelevement net (garde de prose ECART_NEG).
        "plf_ecart_mde": mde(r["plf_somme"] - r["plf_ressources_md"]),
        "cahors_taux": lg.nombre(r["cahors_taux"], 1, L), "cahors_base": str(r["cahors_base"]),
        "cahors_seuil_m": str(r["cahors_seuil_m"]), "cahors_ex1": str(r["cahors_exercices"][0]),
        "cahors_ex2": str(r["cahors_exercices"][1]), "cahors_ex3": str(r["cahors_exercices"][2]),
        "cahors_reprise_pct": str(r["cahors_reprise_pct"]), "cahors_plafond_pct": str(r["cahors_plafond_pct"]),
        "cahors_suspendu": str(r["cahors_suspendu"]),
        "cahors_date_lpfp": date_en(r["cahors_date_lpfp"]) if L == "en" else r["cahors_date_lpfp"],
        "cahors_date_urgence": date_en(r["cahors_date_urgence"]) if L == "en" else r["cahors_date_urgence"],
    })
    for g, p in P.items():
        k = g.lower()
        a[f"{k}_dette_deb"] = fr1(p["dette_deb"])
        a[f"{k}_dette_pic"] = fr1(p["dette_pic"])
        a[f"{k}_dette_pic_annee"] = str(p["dette_pic_annee"])
        a[f"{k}_dette_fin"] = fr1(p["dette_fin"])
        a[f"{k}_inv_max"] = fr1(p["inv_max"])
        a[f"{k}_inv_max_annee"] = lg.enumere([str(y) for y in p["inv_max_annees"]], lang)
        a[f"{k}_inv_min"] = fr1(p["inv_min"])
        a[f"{k}_inv_min_annee"] = lg.enumere([str(y) for y in p["inv_min_annees"]], lang)
        a[f"{k}_inv_baisse_pct"] = fr1(100 * (1 - p["inv_rapport"]), 0)
        a[f"{k}_dette_loc_fin"] = fr1(p["dette_loc_fin"])
        a[f"{k}_detenu_etat"] = fr1(p["detenu_etat"])
        a[f"{k}_detenu_total"] = fr1(p["detenu_total"])
        a[f"{k}_part_etat_pct"] = fr1(p["part_etat_pct"], 0)
        a[f"{k}_excedents"] = (LETTRES_ANGLAIS if lang == "en" else EN_LETTRES).get(p["excedents_2012_2019"], str(p["excedents_2012_2019"]))
    return a


# ------------------------------------------------------------------ figures (fichiers SVG autonomes, charte du dossier)
# Une figure servie en fichier ne recoit pas le CSS de la page : polices, tailles et couleurs sont inscrites dans le
# SVG. Titre, source, precaution et licence sont IMPRIMES dans l'image (regle 5 du modele) ; les fiches « Reutiliser »
# les relisent dans le SVG (fiches_figures), jamais recopies.
W = 720
BLEU, GRIS, ORANGE = "#184f95", "#8a8f98", "#eb6834"
INK, INK2, MUTED, GRID, AXIS, BANDE = "#0A0A0E", "#52514e", "#898781", "#e1e0d9", "#c3c2b7", "#f3efe6"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
TY_TITRE, TY_AXE, TY_ANNOT = 13, 11, 11
CARTOUCHE_H = 48
PAGE_URL = "stephane-lalut.com/dette-publique-collectivites-locales/"
PAGE_URL_EN = "stephane-lalut.com/en/local-government-debt/"
LICENCES = {"fr": "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL, "en": "Compiled by Stéphane Lalut, CC BY 4.0 · " + PAGE_URL_EN}
LICENCE = LICENCES["fr"]
SUFFIXE = {"fr": "", "en": "-en"}


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def entete(h: int, ident: str, titre: str, desc: str) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, h + CARTOUCHE_H, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, h + CARTOUCHE_H),
            '<text x="0" y="18" font-size="%d" font-weight="600" fill="%s">%s</text>' % (TY_TITRE, INK, esc(titre))]


def txt(x, y, s, size=TY_ANNOT, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


# Textes des figures (refonte du 11/10/2026) : titre, description, source, precaution, par langue ; les nombres viennent
# des blocs d'affichage (jetons gardes), jamais saisis. Le pied commun (pied_figure.py) porte source, precaution, licence.
LICENCES_M = {"fr": "Stéphane Lalut, CC BY 4.0 · stephane-lalut.com", "en": "Stéphane Lalut, CC BY 4.0 · stephane-lalut.com"}
TXTF = {
    "fr": dict(
        sig_titre="Investissement des administrations locales et transferts reçus, France, en % du PIB",
        sig_titre_m="Investissement local et transferts reçus, en % du PIB",
        sig_desc="Deux courbes depuis {a_min} : l'investissement local (formation brute de capital fixe) oscille autour de 2 % du "
                 "PIB ; de {ep_a0} à {ep_a1}, il passe de {inv0} % à {inv1} % du PIB et les transferts reçus de {tr0} % à {tr1} %. "
                 "La série comparable des transferts s'arrête en {ep_a1}.",
        sig_fin="{ep_a1} : fin de la série comparable",
        sig_rupt=["Transferts : série arrêtée", "en {ep_a1} ; en 2018 et 2021,", "des dotations deviennent", "des fractions de TVA"],
        sig_bande="baisse des dotations", sig_mun="municipales {m}", sig_pic=["{a} : compensation", "de la taxe professionnelle"],
        sig_inv="investissement local", sig_tr="transferts reçus",
        sig_m_tr="Transferts reçus : {tr0} % → {tr1} %", sig_m_inv="Investissement : {inv0} % → {inv1} %",
        sig_m_txt="De {ep_a0} à {ep_a1}, en % du PIB. Série des transferts arrêtée en {ep_a1} : en 2018 et en 2021, des dotations "
                  "deviennent des fractions de TVA, comptées en impôts.",
        sig_src="Eurostat gov_10a_main, administrations publiques locales (S1313) : investissement P51G, transferts courants reçus "
                "D73REC ; France. Données relevées le {releve}.",
        sig_note="Transferts reçus : de l'État et de la sécurité sociale, toutes dotations confondues ; ce n'est pas la DGF. "
                 "Série comparable arrêtée en {ep_a1} : en 2018 puis en 2021, des dotations sont remplacées par des fractions de "
                 "TVA, comptées en impôts. Ce reclassement change la catégorie de la recette ; il ne dit pas, à lui seul, si "
                 "les ressources ont augmenté ou baissé.",
        cas_titre="Solde des administrations locales, {ep_a0}-{ep_a1} : la même variation, en euros et en points de PIB",
        cas_titre_m="Solde local {ep_a0}-{ep_a1}, en euros et en points de PIB",
        cas_desc="Deux cascades, mêmes postes, même ordre. En milliards d'euros courants : solde de −{s0_md} en {ep_a0} ; transferts "
                 "reçus {c0_md}, impôts {c1_md}, autres recettes {c2_md}, investissement {c3_md}, autres dépenses {c4_md} ; solde de "
                 "{s1_md} en {ep_a1}. En points de PIB : solde de {s0_pt} ; transferts {c0_pt}, impôts {c1_pt}, autres recettes "
                 "{c2_pt}, investissement {c3_pt}, autres dépenses {c4_pt} ; solde de {s1_pt}. Le PIB nominal augmente de "
                 "{pib_croiss_pct} %.",
        cas_postes=["Transferts reçus", "Impôts", "Autres recettes", "Investissement (dépense)", "Autres dépenses"],
        cas_solde="Solde {a}", cas_md="Milliards d'euros courants", cas_pt="Points de PIB", cas_sous="contribution au solde",
        cas_m_unites="milliards d'euros · points de PIB",
        cas_src="Eurostat gov_10a_main, administrations publiques locales (S1313), France ; points calculés sur le PIB des mêmes "
                "comptes. Données relevées le {releve}.",
        cas_note="Barres : contribution de chaque poste à la variation du solde ; pour une dépense, l'inverse de sa variation. "
                 "Les autres dépenses augmentent de {ep_autres_dep_mde} (barre négative) et reculent de {ep_autres_dep_pt} de PIB "
                 "(barre positive) : le PIB nominal augmente de {pib_croiss_pct} %. Lecture comptable : les postes reconstituent "
                 "le solde ; ils ne disent pas ce qui l'a décidé.",
        # Version telephone (cloture, contre-expertise du rendu § 2) : pas de barres, des valeurs en deux colonnes ; le sens
        # des valeurs est dit en tete, le signe des depenses au contact, les soldes distingues des contributions.
        cas_m_sous="Contribution à la variation du solde",
        cas_m_cols=["en Md€", "en points de PIB"],
        cas_m_postes=["Transferts reçus", "Impôts", "Autres recettes", "Investissement (baisse de la dépense)",
                      "Autres dépenses (hausse en euros, baisse en points de PIB)"],
        cas_m_dep="Dépenses : signe inversé, une baisse améliore le solde.",
        cas_m_solde=["Solde {a}, point de départ", "Solde {a}, point d'arrivée"],
        cas_note_m="Valeurs : contribution de chaque poste à la variation du solde ; pour une dépense, l'inverse de sa "
                   "variation. Les autres dépenses augmentent de {ep_autres_dep_mde} (contribution négative) et reculent de "
                   "{ep_autres_dep_pt} de PIB (contribution positive) : le PIB nominal augmente de {pib_croiss_pct} %. Lecture "
                   "comptable : les postes reconstituent le solde ; ils ne disent pas ce qui l'a décidé.",
        eu_titre="Dette des administrations territoriales et part détenue par l’État central, en % du PIB",
        eu_titre_m="Dette territoriale et part détenue par l’État central, en % du PIB",
        eu_desc="Quatre petits graphiques, de {an_dette_deb} à {an_dette_fin}. {pays_desc}",
        eu_pays_desc="{nom} : {deb} % du PIB en {an_dette_deb}, {fin} % en {an_dette_fin} ; part détenue par l'État central "
                     "en {an_ggd} : {etat_pt} de PIB.",
        eu_dont="dont État central, {an_ggd}", eu_leg1="dette des administrations territoriales",
        eu_leg2="dont détenue par l’État central (publiée depuis 2020 pour l’Espagne, la France et l’Italie)",
        eu_m_ligne=["{a1} : {fin} % du PIB", "dont État central : {etat_pt}"],
        eu_src="Eurostat gov_10q_ggdebt (4e trimestre) et gov_10dd_ggd (secteur détenteur S1311), S1312 + S1313, en % du PIB. "
               "Données relevées le {releve}.",
        eu_note="Périmètre statistique, non compétences : la France et l'Italie n'ont pas d'échelon d'États fédérés (S1312).",
    ),
    "en": dict(
        sig_titre="Local government investment and transfers received, France, in % of GDP",
        sig_titre_m="Local investment and transfers received, in % of GDP",
        sig_desc="Two lines since {a_min}: local investment (gross fixed capital formation) hovers around 2% of GDP; from {ep_a0} "
                 "to {ep_a1}, it went from {inv0}% to {inv1}% of GDP and transfers received from {tr0}% to {tr1}%. The comparable "
                 "transfer series stops in {ep_a1}.",
        sig_fin="{ep_a1}: end of the comparable series",
        sig_rupt=["Transfers: series stops", "in {ep_a1}; in 2018 and 2021,", "some grants became", "shares of VAT"],
        sig_bande="grant cuts", sig_mun="municipal elections {m}", sig_pic=["{a}: compensation for the", "abolished business tax"],
        sig_inv="local investment", sig_tr="transfers received",
        sig_m_tr="Transfers received: {tr0}% → {tr1}%", sig_m_inv="Investment: {inv0}% → {inv1}%",
        sig_m_txt="From {ep_a0} to {ep_a1}, in % of GDP. The transfer series stops in {ep_a1}: in 2018 and 2021, some grants "
                  "became shares of VAT, counted as taxes.",
        sig_src="Eurostat gov_10a_main, local government (S1313): investment P51G, current transfers received D73REC; France. "
                "Data retrieved on {releve}.",
        sig_note="Transfers received: from central government and social security, all grants together; this is not the DGF "
                 "grant. Comparable series stops in {ep_a1}: in 2018 and again in 2021, some grants were replaced by shares of "
                 "VAT, counted as taxes. This reclassification changes the category of the revenue; on its own, it does not "
                 "say whether resources rose or fell.",
        cas_titre="Local government balance, {ep_a0}-{ep_a1}: the same change, in euros and in percentage points of GDP",
        cas_titre_m="Local balance {ep_a0}-{ep_a1}, in euros and in percentage points of GDP",
        cas_desc="Two waterfalls, same items, same order. In billions of current euros: balance of −{s0_md} in {ep_a0}; transfers "
                 "received {c0_md}, taxes {c1_md}, other revenue {c2_md}, investment {c3_md}, other spending {c4_md}; balance of "
                 "{s1_md} in {ep_a1}. In percentage points of GDP: balance of {s0_pt}; transfers {c0_pt}, taxes {c1_pt}, other revenue "
                 "{c2_pt}, investment {c3_pt}, other spending {c4_pt}; balance of {s1_pt}. Nominal GDP rose by {pib_croiss_pct}%.",
        cas_postes=["Transfers received", "Taxes", "Other revenue", "Investment (spending)", "Other spending"],
        cas_solde="Balance {a}", cas_md="Billions of current euros", cas_pt="Percentage points of GDP", cas_sous="contribution to the balance",
        cas_m_unites="€ billion · percentage points of GDP",
        cas_src="Eurostat gov_10a_main, local government (S1313), France; percentage points computed on the GDP of the same "
                "accounts. Data retrieved on {releve}.",
        cas_note="Bars: each item's contribution to the change in the balance; for spending, the opposite of its change. Other "
                 "spending rose by {ep_autres_dep_mde} (negative bar) and fell by {ep_autres_dep_pt} of GDP (positive bar): "
                 "nominal GDP rose by {pib_croiss_pct}%. An accounting reading: the items add up to the balance; they do not say "
                 "what decided it.",
        cas_m_sous="Contribution to the change in the balance",
        cas_m_cols=["€ billion", "percentage points of GDP"],
        cas_m_postes=["Transfers received", "Taxes", "Other revenue", "Investment (lower spending)",
                      "Other spending (higher in euros, lower as a share of GDP)"],
        cas_m_dep="Spending: sign reversed, a fall improves the balance.",
        cas_m_solde=["Balance {a}, starting point", "Balance {a}, end point"],
        cas_note_m="Values: each item's contribution to the change in the balance; for spending, the opposite of its change. "
                   "Other spending rose by {ep_autres_dep_mde} (negative contribution) and fell by {ep_autres_dep_pt} of GDP "
                   "(positive contribution): nominal GDP rose by {pib_croiss_pct}%. An accounting reading: the items add up to "
                   "the balance; they do not say what decided it.",
        eu_titre="Subnational government debt and the share held by central government, in % of GDP",
        eu_titre_m="Subnational debt and the share held by central government, in % of GDP",
        eu_desc="Four small charts, from {an_dette_deb} to {an_dette_fin}. {pays_desc}",
        eu_pays_desc="{nom}: {deb}% of GDP in {an_dette_deb}, {fin}% in {an_dette_fin}; share held by central government "
                     "in {an_ggd}: {etat_pt} of GDP.",
        eu_dont="held by central govt, {an_ggd}", eu_leg1="subnational government debt",
        eu_leg2="of which held by central government (published since 2020 for Spain, France and Italy)",
        eu_m_ligne=["{a1}: {fin}% of GDP", "held by central government:", "{etat_pt}"],
        eu_src="Eurostat gov_10q_ggdebt (4th quarter) and gov_10dd_ggd (holding sector S1311), S1312 + S1313, in % of GDP. "
               "Data retrieved on {releve}.",
        eu_note="Statistical scope, not responsibilities: France and Italy have no state-government tier (S1312).",
    ),
}
WM, FS_MIN = pied_figure.LARGEUR_M, pied_figure.POLICE_M


def _pied(e, y0, t, lang):
    return pied_figure.pied(e, y0, W, [(t[0], INK2, "pied-source"), (t[1], INK2, "pied-note"),
                                       (LICENCES[lang], MUTED, "pied-licence")], GRID)


def _pied_m(e, y0, t, lang):
    return pied_figure.pied_mobile(e, y0, [(t[0], INK2, "pied-source"), (t[1], INK2, "pied-note"),
                                           (LICENCES_M[lang], MUTED, "pied-licence")], GRID)


def desc_de(svg):
    import re as _re
    return html.unescape(_re.search(r"<desc[^>]*>(.*?)</desc>", svg, _re.S).group(1))


def _sig_vals(r, A):
    inv, tr = r["serie_inv_fr"], r["serie_transf_fr"]
    a0, a1 = r["ep_a0"], r["ep_a1"]
    nb = lambda v: A["_fmt"](v, 1)  # noqa: E731
    return dict(a_min=min(inv), ep_a0=a0, ep_a1=a1, inv0=nb(inv[a0]), inv1=nb(inv[a1]), tr0=nb(tr[a0]), tr1=nb(tr[a1]))


def fig_signature(r: dict, A: dict, lang: str = "fr") -> str:
    T = TXTF[lang]
    H = 420
    x0, x1, y0, y1 = 48, W - 12, 64, 352
    inv, tr = r["serie_inv_fr"], r["serie_transf_fr"]
    a_min, a_max = min(inv), max(inv)
    vmin, vmax = 1.5, 5.0
    X = lambda a: x0 + (a - a_min) / (a_max - a_min) * (x1 - x0)  # noqa: E731
    Y = lambda v: y1 - (v - vmin) / (vmax - vmin) * (y1 - y0)  # noqa: E731
    V = _sig_vals(r, A)
    e = entete(H, "cs", T["sig_titre"], T["sig_desc"].format(**V))
    bx0, bx1 = X(2014), X(2017.999)
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (bx0, y0, bx1 - bx0, y1 - y0, BANDE))
    for v in (2, 3, 4, 5):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (x0, Y(v), x1, Y(v), GRID))
        e.append(txt(x0 - 6, Y(v) + 4, ("%d%%" if lang == "en" else "%d %%") % v, TY_AXE, MUTED, "end"))
    for a in range(a_min, a_max + 1, 5):
        e.append(txt(X(a), y1 + 15, str(a), TY_AXE, MUTED, "middle"))
    e.append(txt((bx0 + bx1) / 2, y1 + 32, "2014-2017", TY_ANNOT, INK2, "middle"))
    e.append(txt((bx0 + bx1) / 2, y1 + 45, T["sig_bande"], TY_ANNOT, INK2, "middle"))
    for m in MUNICIPALES:
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="2 4"/>' % (X(m), y0, X(m), y1, AXIS))
        e.append(txt(X(m), y0 - 6, T["sig_mun"].format(m=m), 10, MUTED, "middle"))
    for s, col in ((tr, GRIS), (inv, BLEU)):
        pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(s.items()) if v is not None)
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6"/>' % (pts, col))
    a_pic = lg.extremum(tr, tr.get, 1)
    for k, l in enumerate(T["sig_pic"]):
        e.append(txt(X(a_pic) - 8, Y(tr[a_pic]) + 4 + 13 * k, l.format(a=a_pic), anchor="end"))
    # Repere terminal de la serie des transferts (pas de lecture au-dela de 2017) et reclassements au contact
    af = max(tr)
    e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="%s" stroke-width="2"/>' % (X(af), Y(tr[af]), GRIS))
    e.append(txt(X(af) + 8, Y(tr[af]) - 8, T["sig_fin"].format(ep_a1=af), 10, INK2))
    for k, l in enumerate(T["sig_rupt"]):
        e.append(txt(x1, Y(4.3) + 13 * k, l.format(ep_a1=af), 10, INK2, "end"))
    e.append(txt(X(2003), Y(tr[2003]) - 12, T["sig_tr"], TY_ANNOT, GRIS, "middle", "600"))
    e.append(txt(X(1997), Y(inv[1997]) + 22, T["sig_inv"], TY_ANNOT, BLEU, "middle", "600"))
    return _pied(e, H + 2, (T["sig_src"].format(releve=A["_releve"]), T["sig_note"].format(ep_a1=af)), lang)


def fig_signature_m(r: dict, A: dict, lang: str, svg_d: str) -> str:
    T = TXTF[lang]
    V = _sig_vals(r, A)
    e, y = pied_figure.tete_mobile("csm", T["sig_titre_m"], desc_de(svg_d), INK, FONT)
    inv, tr = r["serie_inv_fr"], r["serie_transf_fr"]
    a_min, a_max = min(inv), max(inv)
    X0, X1, TOP = 30, WM - 6, y + 20
    BAS = TOP + 170
    vmin, vmax = 1.5, 5.0
    X = lambda a: X0 + (a - a_min) / (a_max - a_min) * (X1 - X0)  # noqa: E731
    Y = lambda v: BAS - (v - vmin) / (vmax - vmin) * (BAS - TOP)  # noqa: E731
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (X(2014), TOP, X(2017.999) - X(2014), BAS - TOP, BANDE))
    for v in (2, 3, 4, 5):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, Y(v), X1, Y(v), GRID))
        e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(v) + 5, FS_MIN, MUTED, v))
    for a in (a_min, 2014, a_max):
        e.append('<text x="%.1f" y="%d" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                 % (X(a), BAS + 18, FS_MIN, MUTED, "start" if a == a_min else ("end" if a == a_max else "middle"), a))
    for s, col in ((tr, GRIS), (inv, BLEU)):
        pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(s.items()) if v is not None)
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6"/>' % (pts, col))
    af = max(tr)
    e.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="%s" stroke-width="2"/>' % (X(af), Y(tr[af]), GRIS))
    y = BAS + 26
    for lib, col in ((T["sig_m_tr"].format(**V), GRIS), (T["sig_m_inv"].format(**V), BLEU)):
        y += 20
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, col, esc(lib)))
    for l in pied_figure.coupe(T["sig_m_txt"].format(**V), 38):
        y += 19
        e.append('<text x="0" y="%d" font-size="%s" fill="%s">%s</text>' % (y, FS_MIN, INK2, esc(l)))
    return _pied_m(e, y + 14, (T["sig_src"].format(releve=A["_releve"]), T["sig_note"].format(ep_a1=af)), lang)


def pp_fig(s: str, lang: str) -> str:
    """Figures anglaises (cloture, 11/10/2026) : « 0.32 points » -> « 0.32 percentage points » (points de PIB). L'accord
    (pluriel sauf 1) reste celui de langue_generee.py ; la prose de la page garde « points of GDP »."""
    import re as _re
    return _re.sub(r"(\d) (points?)\b", r"\1 percentage \2", s) if lang == "en" else s


def _cas_vals(r, A, lang):
    f = A["_fmt"]
    L = "en" if lang == "en" else "fr"
    V = dict(ep_a0=r["ep_a0"], ep_a1=r["ep_a1"], s0_md=f(abs(r["ep_solde_a0_md"]), 1), s1_md=f(r["ep_solde_a1_md"], 1),
             s0_pt=f(r["ep_solde_a0"], 2), s1_pt=f(r["ep_solde_a1"], 2), pib_croiss_pct=A["pib_croiss_pct"],
             ep_autres_dep_mde=A["ep_autres_dep_mde"], ep_autres_dep_pt=pp_fig(A["ep_autres_dep_pt"], lang))
    for k, (cm, cp) in enumerate(zip(r["ep_cascade_md"], r["ep_cascade"])):
        V["c%d_md" % k], V["c%d_pt" % k] = lg.signe(cm["md_eur"], 1, L), lg.signe(cp["pt_pib"], 2, L)
    return V


def fig_cascade(r: dict, A: dict, lang: str = "fr") -> str:
    T = TXTF[lang]
    f = A["_fmt"]
    L = "en" if lang == "en" else "fr"
    V = _cas_vals(r, A, lang)
    H = 352
    lab_x, top, rh = 192, 84, 34
    panneaux = [("md", T["cas_md"], 212, 452,
                 [r["ep_solde_a0_md"]] + [c["md_eur"] for c in r["ep_cascade_md"]] + [r["ep_solde_a1_md"]], 1),
                ("pt", T["cas_pt"], 482, 708,
                 [r["ep_solde_a0"]] + [c["pt_pib"] for c in r["ep_cascade"]] + [r["ep_solde_a1"]], 2)]
    libs = [T["cas_solde"].format(a=r["ep_a0"])] + T["cas_postes"] + [T["cas_solde"].format(a=r["ep_a1"])]
    e = entete(H, "cc", T["cas_titre"].format(**V), T["cas_desc"].format(**V))
    for k, lab in enumerate(libs):
        e.append(txt(lab_x, top + k * rh + rh / 2 + 4, lab, TY_ANNOT, INK, "end", "600" if k in (0, len(libs) - 1) else None))
    for ident, titre, px0, px1, vals, dec in panneaux:
        cum, mn, mx = vals[0], min(0, vals[0]), max(0, vals[0])
        for v in vals[1:-1]:
            cum += v
            mn, mx = min(mn, cum), max(mx, cum)
        pas = 5.0 if ident == "md" else 0.25
        import math as _m
        vmin, vmax = (_m.floor(mn / pas) - 1) * pas, (_m.ceil(mx / pas) + 1) * pas
        X = lambda v, a=px0, b=px1, lo=vmin, hi=vmax: a + (v - lo) / (hi - lo) * (b - a)  # noqa: E731
        e.append(txt((px0 + px1) / 2, 50, titre, TY_ANNOT, INK, "middle", "600"))
        e.append(txt((px0 + px1) / 2, 64, T["cas_sous"], 10, MUTED, "middle"))
        y_bas = top + len(vals) * rh
        n_ = int(round((vmax - vmin) / pas))
        for j in range(n_ + 1):
            g = vmin + j * pas
            e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(g), top, X(g), y_bas, AXIS if abs(g) < 1e-9 else GRID))
            if abs(g / (2 * pas) - round(g / (2 * pas))) < 1e-9:  # graduations multiples de 10 Md EUR / 0,5 point
                e.append(txt(X(g), y_bas + 14, lg.nombre(g, 0 if ident == "md" else 1, L), 10, MUTED, "middle"))
        cum = 0.0
        for k, v in enumerate(vals):
            yy, hh = top + k * rh + rh * 0.2, rh * 0.6
            base = k in (0, len(vals) - 1)
            if base:
                a_, b_, col = min(0, v), max(0, v), INK2
                cum = v
            else:
                a_, b_ = sorted((cum, cum + v))
                col = ORANGE if v < 0 else BLEU
                cum += v
            e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (X(a_), yy, max(X(b_) - X(a_), 1.5), hh, col))
            lib = lg.nombre(v, dec, L) if base else lg.signe(v, dec, L)
            if X(b_) + 6 + 6.0 * len(lib) <= px1 + 6:
                e.append(txt(X(b_) + 5, yy + hh / 2 + 4, lib, 10, INK))
            else:
                e.append(txt(X(a_) - 5, yy + hh / 2 + 4, lib, 10, INK, "end"))
    return _pied(e, H + 2, (T["cas_src"].format(releve=A["_releve"]), T["cas_note"].format(**V)), lang)


def fig_cascade_m(r: dict, A: dict, lang: str, svg_d: str) -> str:
    """Version telephone de la double cascade (cloture, 11/10/2026, contre-expertise du rendu § 2) : pas de barres, des
    valeurs en deux colonnes (euros, points de PIB). En tete, ce que sont les valeurs (contribution a la variation du
    solde) ; au contact des depenses, leur signe inverse et le sens de leur variation dans le libelle ; les soldes de
    depart et d'arrivee sur fond teinte, en gras, distincts des contributions (bleu : ameliore le solde ; orange : le
    degrade, comme les barres de la version detaillee)."""
    T = TXTF[lang]
    V = _cas_vals(r, A, lang)
    e, y = pied_figure.tete_mobile("ccm", T["cas_titre_m"].format(**V), desc_de(svg_d), INK, FONT)
    y -= 16
    for l_ in pied_figure.coupe(T["cas_m_sous"], 36):
        y += 22
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(l_)))
    C1, C2 = 120, WM  # bords droits des deux colonnes
    y += 24
    for xc, lib in zip((C1, C2), T["cas_m_cols"]):
        e.append('<text x="%d" y="%d" font-size="%s" fill="%s" text-anchor="end">%s</text>' % (xc, y, FS_MIN, MUTED, esc(lib)))
    soldes = [s_.format(a=a_) for s_, a_ in zip(T["cas_m_solde"], (r["ep_a0"], r["ep_a1"]))]
    lignes = ([(soldes[0], "−" + V["s0_md"], V["s0_pt"], None, None)]
              + [(T["cas_m_postes"][k], V["c%d_md" % k], V["c%d_pt" % k], r["ep_cascade_md"][k]["md_eur"],
                  r["ep_cascade"][k]["pt_pib"]) for k in range(5)]
              + [(soldes[1], V["s1_md"], V["s1_pt"], None, None)])
    for k, (lab, vm, vp, nm, np_) in enumerate(lignes):
        solde = nm is None
        if k == 4:  # premiere depense : le signe inverse se dit au contact
            y += 4
            for l_ in pied_figure.coupe(T["cas_m_dep"], 36):
                y += 18
                e.append('<text x="0" y="%d" font-size="%s" font-style="italic" fill="%s">%s</text>' % (y, FS_MIN, MUTED, esc(l_)))
        lab_l = pied_figure.coupe(lab, 40)
        haut = 19 * len(lab_l) + 19
        if solde:
            e.append('<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (y + 8, WM, haut + 8, BANDE))
        for l_ in lab_l:
            y += 19
            e.append('<text x="%d" y="%d" font-size="%s" fill="%s"%s>%s</text>'
                     % (4 if solde else 0, y + 4, FS_MIN, INK if solde else INK2, ' font-weight="600"' if solde else "", esc(l_)))
        y += 23
        for xc, val, num in ((C1, vm, nm), (C2, vp, np_)):
            col = INK if num is None else (BLEU if num > 0 else ORANGE)
            e.append('<text x="%d" y="%d" font-size="15" font-weight="600" fill="%s" text-anchor="end">%s</text>'
                     % (xc - (4 if solde else 0), y, col, esc(val)))
        y += 6 if solde else 0
    return _pied_m(e, y + 16, (T["cas_src"].format(releve=A["_releve"]), T["cas_note_m"].format(**V)), lang)


def _eu_vals(r, A, lang):
    T = TXTF[lang]
    f = A["_fmt"]
    L = "en" if lang == "en" else "fr"
    pays = []
    for p in r["pays"]:
        pays.append(dict(nom=p["nom_en"] if lang == "en" else p["nom"], deb=f(p["dette_deb"], 1), fin=f(p["dette_fin"], 1),
                         etat=f(p["detenu_etat"], 1), etat_pt=pp_fig(lg.points(p["detenu_etat"], 1, L), lang)))
    base = dict(an_dette_deb=r["an_dette_deb"], an_dette_fin=r["an_dette_fin"], an_ggd=r["an_ggd"])
    desc = " ".join(T["eu_pays_desc"].format(**base, **q) for q in pays)
    return pays, dict(base, pays_desc=desc)


def fig_europe(r: dict, A: dict, lang: str = "fr") -> str:
    T = TXTF[lang]
    f = A["_fmt"]
    pays, B = _eu_vals(r, A, lang)
    H = 336
    pw, ph, gap = 150, 170, 22
    vmax = 30.0
    e = entete(H, "ce", T["eu_titre"], T["eu_desc"].format(**B))
    e.append('<line x1="0" y1="36" x2="18" y2="36" stroke="%s" stroke-width="2.4"/>' % BLEU)
    e.append(txt(24, 40, T["eu_leg1"], 10))
    e.append('<line x1="0" y1="52" x2="18" y2="52" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % GRIS)
    e.append(txt(24, 56, T["eu_leg2"], 10))
    for k, (p, q) in enumerate(zip(r["pays"], pays)):
        ox, oy = 46 + k * (pw + gap), 96
        s = p["serie_dette"]
        a0, a1 = min(s), max(s)
        X = lambda a, ox=ox, a0=a0, a1=a1: ox + (a - a0) / (a1 - a0) * pw  # noqa: E731
        Y = lambda v, oy=oy: oy + ph - v / vmax * ph  # noqa: E731
        e.append(txt(ox, oy - 10, q["nom"], TY_ANNOT, INK, "start", "600"))
        for v in (0, 10, 20, 30):
            e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (ox, Y(v), ox + pw, Y(v), GRID))
            if k == 0:
                e.append(txt(ox - 6, Y(v) + 4, ("%d%%" if lang == "en" else "%d %%") % v, TY_AXE, MUTED, "end"))
        se = {a: v for a, v in p["serie_detenu_etat"].items() if a >= a0}
        if se:
            pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(se.items()))
            e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % (pts, GRIS))
        pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(s.items()))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"/>' % (pts, BLEU))
        # etiquettes au-dessus des trois premiers / derniers points (jamais sur la courbe)
        hd = max(v for a, v in s.items() if a <= a0 + 3)
        hf = max(v for a, v in s.items() if a >= a1 - 3)
        e.append(txt(X(a0), Y(hd) - 7, f(s[a0], 1), 10))
        e.append(txt(X(a1), Y(hf) - 7, f(s[a1], 1), 10, INK, "end", "600"))
        e.append(txt(ox, oy + ph + 15, str(a0), TY_AXE, MUTED))
        e.append(txt(ox + pw, oy + ph + 15, str(a1), TY_AXE, MUTED, "end"))
        # Part detenue par l'Etat central pour CHAQUE pays (France et Italie comprises), sous le panneau : aucune collision
        e.append(txt(ox, oy + ph + 34, T["eu_dont"].format(**B), 10, INK2))
        e.append(txt(ox, oy + ph + 49, q["etat_pt"], 11, INK2, "start", "600"))
    return _pied(e, H + 2, (T["eu_src"].format(releve=A["_releve"]), T["eu_note"]), lang)


def fig_europe_m(r: dict, A: dict, lang: str, svg_d: str) -> str:
    T = TXTF[lang]
    pays, B = _eu_vals(r, A, lang)
    e, y = pied_figure.tete_mobile("cem", T["eu_titre_m"], desc_de(svg_d), INK, FONT)
    vmax = 30.0
    for p, q in zip(r["pays"], pays):
        y += 26
        e.append('<text x="0" y="%d" font-size="15" font-weight="600" fill="%s">%s</text>' % (y, INK, esc(q["nom"])))
        s = p["serie_dette"]
        a0, a1 = min(s), max(s)
        X0, X1, TOP = 28, WM - 6, y + 10
        BAS = TOP + 80
        X = lambda a, a0=a0, a1=a1, X0=X0, X1=X1: X0 + (a - a0) / (a1 - a0) * (X1 - X0)  # noqa: E731
        Y = lambda v, TOP=TOP, BAS=BAS: BAS - v / vmax * (BAS - TOP)  # noqa: E731
        for v in (0, 30):
            e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (X0, Y(v), X1, Y(v), GRID))
            e.append('<text x="%d" y="%.1f" font-size="%s" fill="%s" text-anchor="end">%d</text>' % (X0 - 4, Y(v) + 5, FS_MIN, MUTED, v))
        se = {a: v for a, v in p["serie_detenu_etat"].items() if a >= a0}
        if se:
            pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(se.items()))
            e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % (pts, GRIS))
        pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(s.items()))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"/>' % (pts, BLEU))
        # Bornes de l'axe horizontal (cloture, contre-expertise du rendu § 3) : premiere et derniere annee de la serie
        for a_, ancre in ((a0, "start"), (a1, "end")):
            e.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s">%d</text>'
                     % (X(a_), BAS + 17, FS_MIN, MUTED, ancre, a_))
        y = BAS + 18
        for l_ in T["eu_m_ligne"]:
            y += 19
            e.append('<text x="0" y="%d" font-size="%s" font-weight="600" fill="%s">%s</text>'
                     % (y, FS_MIN, INK, esc(l_.format(a1=a1, **q))))
    return _pied_m(e, y + 16, (T["eu_src"].format(releve=A["_releve"]), T["eu_note"]), lang)


def barres_absentes(svg_m: str) -> list[str]:
    """Une version telephone ne dessine pas de barres : son texte (titre, description exceptee, pied) n'en parle pas
    (cloture, 11/10/2026 : la note « Barres : ... » survivait dans la cascade telephone). Rend les ecarts."""
    import re as _re
    sans_desc = _re.sub(r"<desc[^>]*>.*?</desc>", "", svg_m, flags=_re.S)
    textes = " ".join(html.unescape(t) for t in _re.findall(r"<text[^>]*>([^<]*)</text>", sans_desc))
    return ["mention de barres absentes : %s" % m for m in _re.findall(r"\b(?:[Bb]arres?|[Bb]ars?)\b", textes)]


def figures(r: dict, Aff: dict, releve: str) -> dict:
    out = {}
    for lang, x in SUFFIXE.items():
        A = dict(Aff[lang], _fmt=(lambda v, d, L=lang: lg.nombre(v, d, L)), _releve=date_longue(releve, lang))
        for nom, f_d, f_m in (("investissement", fig_signature, fig_signature_m), ("cascade", fig_cascade, fig_cascade_m),
                              ("europe", fig_europe, fig_europe_m)):
            d = f_d(r, A, lang)
            out["collectivites-%s%s.svg" % (nom, x)] = d
            out["collectivites-%s%s-m.svg" % (nom, x)] = f_m(r, A, lang, d)
    return out


MONTRE = {
    "fr": [
        ("investissement", "collectivites-investissement",
         "De {ep_a0} à {ep_a1}, les transferts reçus par les administrations publiques locales reculent de {ep_transf_mde} "
         "({ep_transf_pt} de PIB) et leur investissement de {ep_inv_mde} ({ep_inv_pt}) ; la série comparable des transferts "
         "s'arrête en {ep_a1}."),
        ("cascade", "collectivites-cascade",
         "De {ep_a0} à {ep_a1}, le solde des administrations publiques locales s'améliore de {ep_solde_mde} ({ep_solde_pt} de "
         "PIB). Leurs dépenses totales restent presque stables en euros courants ({ep_te_mde_s}) ; rapportées au PIB, elles "
         "diminuent de {ep_te_pt}, dont {ep_inv_pt} pour l'investissement, pendant que les recettes fiscales progressent et que "
         "les transferts reçus reculent. Ces évolutions sont concomitantes ; elles n'attribuent pas le recul de l'investissement "
         "à la baisse des dotations."),
        ("europe", "collectivites-europe",
         "Une même dette territoriale peut recouvrir des architectures opposées : en Espagne, {es_part_etat_pct} % en est "
         "détenue par l'État central ; en France, {fr_part_etat_pct} %."),
    ],
    "en": [
        ("investissement", "collectivites-investissement",
         "From {ep_a0} to {ep_a1}, the transfers received by local government fell by {ep_transf_mde} ({ep_transf_pt} of GDP) "
         "and its investment by {ep_inv_mde} ({ep_inv_pt}); the comparable transfer series stops in {ep_a1}."),
        ("cascade", "collectivites-cascade",
         "From {ep_a0} to {ep_a1}, the local government balance improved by {ep_solde_mde} ({ep_solde_pt} of GDP). Total "
         "spending stayed almost flat in current euros ({ep_te_mde_s}); relative to GDP, it fell by {ep_te_pt}, of which "
         "{ep_inv_pt} for investment, while tax revenue rose and transfers received fell. These movements are concomitant; "
         "they do not attribute the fall in investment to the grant cuts."),
        ("europe", "collectivites-europe",
         "The same subnational debt can conceal opposite architectures: in Spain, {es_part_etat_pct}% of it is held by central "
         "government; in France, {fr_part_etat_pct}%."),
    ],
}


def fiches_figures(figs: dict, A: dict, A_en: dict) -> dict:
    """Cartes du bloc « Réutiliser » : « montre » est écrit ici, ses chiffres viennent des jetons gardés ; titre,
    source et précaution sont relus dans le SVG (classes du pied commun)."""
    import re as _re
    res = {}
    for lang, Aff in (("fr", A), ("en", A_en)):
        out = []
        for ident, fichier, montre in MONTRE[lang]:
            fichier = fichier + SUFFIXE[lang]
            svg = figs[fichier + ".svg"]
            titre = html.unescape(_re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            src, note, lic = (pied_figure.lire(svg, c) for c in ("pied-source", "pied-note", "pied-licence"))
            if not src or lic != LICENCES[lang]:
                fail("fiche %s : pied illisible dans le SVG" % fichier)
            out.append(dict(id=ident, fichier=fichier, titre=titre, montre=montre.format(**Aff), source=src, precaution=note))
        res[lang] = out
    return res



# ------------------------------------------------------------------ sorties
ROOT = Path(__file__).resolve().parent.parent
OUT_DATA = ROOT / "data" / "dette_collectivites.json"
OUT_STATIC = ROOT / "static" / "dette_collectivites.json"
OUT_CSV = ROOT / "static" / "dette_collectivites.csv"
OUT_IMG = ROOT / "static" / "img"
OUT_FIGURES = ROOT / "data" / "figures_collectivites.json"


def csv_texte(r: dict) -> str:
    import io as _io
    buf = _io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "pays", "annee", "valeur", "unite", "source"])
    for p in r["pays"]:
        for y, v in sorted(p["serie_dette"].items()):
            w.writerow(["dette_administrations_territoriales", p["geo"], y, "%.1f" % v, "% du PIB",
                        "Eurostat gov_10q_ggdebt S1312+S1313, 4e trimestre"])
        for y, v in sorted(p["serie_dette_loc"].items()):
            w.writerow(["dette_administrations_locales", p["geo"], y, "%.1f" % v, "% du PIB", "Eurostat gov_10q_ggdebt S1313, 4e trimestre"])
        for y, v in sorted(p["serie_detenu_etat"].items()):
            w.writerow(["dette_territoriale_detenue_par_etat_central", p["geo"], y, "%.1f" % v, "% du PIB",
                        "Eurostat gov_10dd_ggd S1312+S1313 detenue par S1311"])
    for y, v in sorted(r["serie_inv_fr"].items()):
        w.writerow(["investissement_administrations_locales", "FR", y, "%.3f" % v, "% du PIB", "Eurostat gov_10a_main S1313 P51G"])
    for y, v in sorted(r["serie_transf_fr"].items()):
        w.writerow(["transferts_courants_recus_autres_administrations", "FR", y, "%.3f" % v, "% du PIB",
                    "Eurostat gov_10a_main S1313 D73REC (serie comparable jusqu'en 2017)"])
    for c in r["categories"]:
        for k, lib in (("concours", "concours_etat"), ("eb", "epargne_brute"), ("eq", "depenses_equipement"), ("dette", "encours_dette")):
            for an_, suf in ((2021, "_21"), (r["of_an"], "_fin")):
                w.writerow([lib + "_" + c["cat"], "FR", an_, "%.3f" % c[k + suf], "Md EUR", "OFGL, base consolidee " + c["cat"]])
    for a, v in sorted(r["dgf_vote"].items()):
        w.writerow(["dgf_montant_loi_de_finances", "FR", a, "%.3f" % v, "Md EUR", "CGCT art. L. 1613-1 (Legifrance)"])
    for m in r["plf_mesures"]:
        w.writerow(["projet_loi_finances_mesure_" + m["cle"], "FR", r["plf_edition"], "%.3f" % m["md"], "Md EUR",
                    m["source"] + " (projet, avant examen)"])
    w.writerow(["projet_loi_finances_dgf", "FR", r["plf_edition"], "%.3f" % r["plf_dgf"], "Md EUR",
                "projet de loi de finances pour %d, article 34 (projet, avant examen)" % r["plf_edition"]])
    # Refonte du 11/10/2026 : la decomposition 2013-2017 dans les deux unites (contribution de chaque poste a la variation
    # du solde ; pour une depense, l'inverse de sa variation). Lignes AJOUTEES ; les lignes precedentes sont inchangees.
    cles = ["transferts_recus", "impots", "autres_recettes", "investissement", "autres_depenses"]
    per = "%d-%d" % (r["ep_a0"], r["ep_a1"])
    for cle, cm, cp in zip(cles, r["ep_cascade_md"], r["ep_cascade"]):
        w.writerow(["decomposition_solde_local_" + cle, "FR", per, "%.3f" % cm["md_eur"], "Md EUR courants (contribution au solde)",
                    "Eurostat gov_10a_main S1313"])
        w.writerow(["decomposition_solde_local_" + cle, "FR", per, "%.4f" % cp["pt_pib"], "points de PIB (contribution au solde)",
                    "Eurostat gov_10a_main S1313"])
    w.writerow(["variation_solde_local", "FR", per, "%.3f" % r["ep_solde_md"], "Md EUR courants", "Eurostat gov_10a_main S1313 B9"])
    w.writerow(["variation_solde_local", "FR", per, "%.4f" % r["ep_solde_delta"], "points de PIB", "Eurostat gov_10a_main S1313 B9"])
    w.writerow(["croissance_pib_nominal", "FR", per, "%.2f" % r["pib_croiss_pct"], "%", "Eurostat gov_10dd_edpt1 B1GQ MIO_NAC (notification)"])
    w.writerow(["projet_loi_finances_somme_arithmetique_cinq_mesures", "FR", r["plf_edition"], "%.3f" % r["plf_somme"], "Md EUR",
                "somme descriptive des cinq lignes ; effet net non etabli par addition (projet, avant examen)"])
    return buf.getvalue()


def _norm(d):
    return json.loads(json.dumps(d, sort_keys=True, ensure_ascii=False, default=str))


def _egal(x, y) -> bool:
    """Bruit d'arrondi flottant (somme cote serveur OFGL : 1e-14) n'est pas une donnee nouvelle."""
    if isinstance(x, (int, float)) and isinstance(y, (int, float)) and not isinstance(x, bool):
        return abs(x - y) <= 1e-9 * max(1.0, abs(x))
    if isinstance(x, dict) and isinstance(y, dict):
        return x.keys() == y.keys() and all(_egal(x[k], y[k]) for k in x)
    if isinstance(x, list) and isinstance(y, list):
        return len(x) == len(y) and all(_egal(u, v) for u, v in zip(x, y))
    return x == y


def ecarts_publies(prev: dict, calcul: dict, series: dict) -> list[str]:
    """Grandeurs deja publiees (calcul et series du JSON precedent) qui different du calcul du jour."""
    pc_, nc_ = _norm(prev.get("calcul", {})), _norm(calcul)
    ps_, ns_ = _norm(prev.get("series", {})), _norm(series)
    return [k for k in pc_ if not _egal(pc_[k], nc_.get(k))] + [k for k in ps_ if not _egal(ps_[k], ns_.get(k))]


def date_releve(b: dict, r: dict) -> str:
    """Date de releve des DONNEES : celle deja publiee si toutes les grandeurs publiees sont retrouvees identiques."""
    if not OUT_DATA.exists():
        return b["releve_le"]
    try:
        prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
    except ValueError:
        return b["releve_le"]
    if not prev.get("releve_le"):
        return b["releve_le"]
    calcul = {k: v for k, v in r.items() if not k.startswith("serie_")}
    series = {k: v for k, v in r.items() if k.startswith("serie_")}
    return b["releve_le"] if ecarts_publies(prev, calcul, series) else prev["releve_le"]


def date_longue(iso: str, lang: str) -> str:
    """« 7 octobre 2026 » / « 7 October 2026 » (« 1er » en francais)."""
    y_, m_, d_ = (int(x) for x in iso.split("-"))
    if lang == "en":
        return "%d %s %d" % (d_, MOIS_EN[m_ - 1], y_)
    return ("1er" if d_ == 1 else str(d_)) + " %s %d" % (MOIS_FR[m_ - 1], y_)


def autotest_mutation(b: dict) -> str:
    """Mutation reelle : l'investissement local 2014-2016 ramene pres de 2013. Rend la garde qui a mordu."""
    import copy
    m = copy.deepcopy(b)
    ref = next(x["v"] for x in m["comptes"]["obs"] if (x["geo"], x["sector"], x["na_item"], x["time"]) == ("FR", "S1313", "P51G", "2013"))
    for o in m["comptes"]["obs"]:
        if (o["geo"], o["sector"], o["na_item"]) == ("FR", "S1313", "P51G") and o["time"] in ("2014", "2015", "2016"):
            o["v"] = ref * 0.97
    try:
        calculer(Jeu(m))
    except Arret as e:
        return str(e)
    raise Arret("la mutation n'a fait mordre aucune garde : controle ABSENT")


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def _main() -> int:
    check = "--check" in sys.argv[1:] or MUTATION is not None
    if MUTATION is not None and MUTATION not in MUTATIONS_PROSE and MUTATION not in ("stables", "cahors"):
        fail("mutation inconnue : %s" % MUTATION)
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    if MUTATION in MUTATIONS_PROSE:  # temoin d'une garde de prose : elle doit mordre AVANT tout releve
        gardes_prose()
        fail("mutation %s : aucune garde de prose n'a mordu (controle ABSENT)" % MUTATION)
    n_phrases = gardes_prose()
    b = relever()
    if MUTATION == "stables":  # temoin : depenses 2017 relevees de 3 % (+7,5 Md EUR) -> « presque stables » doit tomber
        for o in b["comptes"]["obs"]:
            if (o["geo"], o["sector"], o["time"]) == ("FR", "S1313", "2017") and o["na_item"] in ("TE", "TR"):
                o["v"] *= 1.03
    J = Jeu(b)
    r, rapport = calculer(J)
    if MUTATION is not None:
        fail("mutation %s : aucune garde n'a mordu (controle ABSENT)" % MUTATION)
    mord = autotest_mutation(b)
    log("autotest : la mutation a fait mordre -> " + mord[:160])
    a = affichage(r)
    a_en = affichage(r, "en")
    if set(a) != set(a_en):
        fail("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(a) ^ set(a_en)))
    # Affichage coherent : l'effet du PIB et la variation en euros, arrondis, redonnent le recul affiche en points
    if abs(round(abs(r["ep_te_effet_pib"]), 2) - round(abs(r["ep_te_effet_eur"]), 2) - round(abs(r["ep_te"]), 2)) > 0.0051:
        fail("decomposition du denominateur : les valeurs arrondies ne se referment pas (%.2f - %.2f != %.2f)"
             % (abs(r["ep_te_effet_pib"]), abs(r["ep_te_effet_eur"]), abs(r["ep_te"])))
    # Ecart du projet de loi : les valeurs affichees se referment (6,2 - 5 = 1,2), sinon le lecteur refait un calcul faux
    if abs(round(r["plf_somme"], 1) - round(r["plf_ressources_md"], 0) - round(r["plf_somme"] - r["plf_ressources_md"], 1)) > 0.051:
        fail("projet de loi de finances : somme, variation et ecart arrondis ne se referment pas")
    # Date de releve imprimee dans le pied des figures (cloture, 11/10/2026) : celle des DONNEES. A grandeurs publiees
    # identiques, la date deja publiee est conservee (meme regle que releve_le plus bas), sinon celle du releve du jour.
    releve = date_releve(b, r)
    figs = figures(r, {"fr": a, "en": a_en}, releve)
    for lang, x in SUFFIXE.items():
        for nom in ("investissement", "cascade", "europe"):
            ec = pied_figure.parite(figs["collectivites-%s%s.svg" % (nom, x)], figs["collectivites-%s%s-m.svg" % (nom, x)], FS_MIN)
            ec += barres_absentes(figs["collectivites-%s%s-m.svg" % (nom, x)])
            if ec:
                fail("parite telephone %s %s : %s" % (nom, lang, " ; ".join(ec)))
            for f_, larg in (("collectivites-%s%s.svg" % (nom, x), W), ("collectivites-%s%s-m.svg" % (nom, x), WM)):
                for h_ in pied_figure.hors_cadre(figs[f_], larg):
                    log("A VERIFIER au rendu (estimation) : %s : %s" % (f_, h_))
    fiches = fiches_figures(figs, a, a_en)
    # La lecture se garde aussi dans ce que le generateur ecrit : fiches « Reutiliser » et descriptions des figures
    import re as _re
    gen = {"fr": [], "en": []}
    for lang, l_ in fiches.items():
        gen[lang] += [c["montre"] + " " + c["precaution"] for c in l_]
    for n_, svg in figs.items():
        gen["en" if "-en" in n_ else "fr"].append(desc_de(svg))
        gen["en" if "-en" in n_ else "fr"].append(pied_figure.lire(svg, "pied-note"))
    n_phrases = gardes_prose(gen)
    if check:
        log("--check : %d gardes de donnees tenues, gardes de prose tenues (%d phrases lues), parite des 6 figures "
            "telephone tenue, rien ecrit." % (len(rapport), n_phrases))
        return 0
    csvt = csv_texte(r)
    payload = {
        "meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                 "sources": {k: {"jeu": b[k]["dataset"], "maj_source": b[k]["maj_eurostat"], "sha256": b[k]["sha256"]}
                             for k in ("comptes", "te_pc", "pib", "dette", "ggd", "ofgl", "notif")},
                 "definitions": {"perimetre_local": "S1313 : administrations publiques locales (collectivités, syndicats, ODAL)",
                                 "perimetre_territorial": "S1312 + S1313 (États fédérés, s'il en existe, et administrations locales)",
                                 "transferts": "D73REC : transferts courants reçus des autres administrations publiques (État et sécurité sociale)",
                                 "dgf_votee": "montant de la DGF fixé par la loi de finances (CGCT art. L. 1613-1)",
                                 "cascade": "contribution de chaque poste à la variation du solde (pour une dépense, l'inverse de sa variation), en Md EUR courants (ep_cascade_md) et en points de PIB (ep_cascade)",
                                 "plf_somme": "somme arithmétique des cinq montants du projet de loi de finances : descriptive, effet net non établi"}},
        "gardes": rapport,
        "calcul": {k: v for k, v in r.items() if not k.startswith("serie_")},
        "series": {k: v for k, v in r.items() if k.startswith("serie_")},
        "affichage": a,
        "affichage_en": a_en,
    }
    # Bruit de calcul au 15e chiffre : le jeu se compare et s'écrit normalisé (organe commun releve_jeu.normalise, 19/10/2026).
    payload = rj.normalise(payload)
    if OUT_DATA.exists():
        try:
            prev = json.loads(OUT_DATA.read_text(encoding="utf-8"))
            p2 = {k: v for k, v in prev.items() if k not in ("releve_le", "_licence")}
            p2["meta"] = dict(p2.get("meta", {}), sources=None)
            n2 = dict(payload)
            n2["meta"] = dict(n2["meta"], sources=None)
            same = (json.dumps(p2, sort_keys=True, ensure_ascii=False, default=str) == json.dumps(n2, sort_keys=True, ensure_ascii=False, default=str)
                    and all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s for n, s in figs.items())
                    and all((OUT_IMG / n.replace(".svg", ".png")).exists() for n in figs)
                    and OUT_CSV.exists() and OUT_CSV.read_text(encoding="utf-8-sig") == csvt
                    and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fiches)
            if prev.get("releve_le") and same:
                log("Donnees et figures identiques : rien ecrit (releve_le conserve : %s)." % prev["releve_le"])
                return 0
            # Donnees constantes, sorties nouvelles (cles calculees ajoutees, texte d'une figure, bloc d'affichage) : la date de
            # releve reste celle des DONNEES (meme defaut corrige le 11/10/2026 dans update_dette_inflation.py). Critere : toute
            # grandeur deja publiee (calcul et series) est retrouvee identique ; une seule difference = donnees nouvelles.
            ecarts = ecarts_publies(prev, payload["calcul"], payload["series"])
            if prev.get("releve_le") and not ecarts:
                releve = prev["releve_le"]
                log("Grandeurs deja publiees identiques : releve_le conserve (%s) ; sorties nouvelles ecrites." % releve)
            else:
                log("Grandeurs publiees modifiees (donnees nouvelles) : %s" % ", ".join(ecarts[:12]))
        except (ValueError, KeyError):
            pass
    payload = {"releve_le": releve, "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Eurostat, OFGL, Légifrance", **payload}
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    OUT_DATA.write_text(txt_json, encoding="utf-8")
    OUT_STATIC.write_text(txt_json, encoding="utf-8")
    OUT_CSV.write_text(csvt, encoding="utf-8-sig", newline="\n")
    import cairosvg
    for n, s in figs.items():
        (OUT_IMG / n).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")), output_width=1440,
                         background_color="white")
    OUT_FIGURES.write_text(json.dumps(fiches, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("OK : %d gardes tenues ; temoin TR-TE-B9 max %.3f MEUR sur %d annees" % (len(rapport), r["temoin_residu_max_meur"], r["temoin_annees"]))
    log("Ecrit : data/dette_collectivites.json, static/dette_collectivites.{json,csv}, data/figures_collectivites.json, "
        "%d figures SVG + PNG" % len(figs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
