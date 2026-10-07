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

Usage : python scripts/update_dette_collectivites.py [--check]
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
    }


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
        "fctva": ("VAT compensation fund: rate cut by %d points, except green spending and roads" % fctva_pts,
                  "articles 35 and 41", "cut in a central government grant tied to eligible investment spending"),
        "tva": ("Assigned VAT, excluding regions: annual increase reduced by inflation", "article 36",
                "capping of the growth of assigned VAT, excluding regions"),
        "ministeres": ("Contributions of certain ministries to local authorities", "budget mission appropriations",
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
            "plf_mesures": mesures,
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
        ycreux, creux = min(fen, key=lambda t: t[1])
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
        ypic = max(serie, key=serie.get)
        inv = {y: terr_pc(g, "P51G", y) for y in J.annees(g, "S1313", "P51G") if y >= 2000}
        inv_avant = {y: v for y, v in inv.items() if y <= 2010}
        inv_apres = {y: v for y, v in inv.items() if 2011 <= y <= 2019}
        yi_max = max(inv_avant, key=inv_avant.get)
        yi_min = min(inv_apres, key=inv_apres.get)
        excedents = sum(1 for y in range(2012, 2020) if (terr_pc(g, "B9", y) or 0) > 0)
        federe = J.dette(g, "S1312", max(ys)) is not None
        pays.append({
            "geo": g, "nom": NOMS[g], "nom_en": NOMS_EN[g], "federe": federe,
            "dette_deb": serie[min(ys)], "dette_pic": serie[ypic], "dette_pic_annee": ypic, "dette_fin": serie[max(ys)],
            "inv_max": inv_avant[yi_max], "inv_max_annee": yi_max, "inv_min": inv_apres[yi_min], "inv_min_annee": yi_min,
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
    a_tepic = max(te, key=te.get)
    r["te_a0"], r["te_0"], r["te_apic"], r["te_pic"], r["te_fin"] = a_te0, te[a_te0], a_tepic, te[a_tepic], te[an_fin]

    # 9. OFGL : la maille des praticiens (milliards d'euros courants)
    r["of_dgf_dep_13"], r["of_dgf_dep_17"] = J.of("departements", "Dotation globale de fonctionnement", 2013), J.of("departements", "Dotation globale de fonctionnement", 2017)
    r["of_dgf_reg_13"], r["of_dgf_reg_17"] = J.of("regions", "Dotation globale de fonctionnement", 2013), J.of("regions", "Dotation globale de fonctionnement", 2017)
    r["of_dgf_reg_18"], r["of_tva_reg_18"] = J.of("regions", "Dotation globale de fonctionnement", 2018), J.of("regions", "TVA", 2018)
    eb = {y: J.of("departements", "Epargne brute", y) for y in J.of_annees("departements", "Epargne brute") if y >= 2018}
    a_ebpic = max(eb, key=eb.get)
    a_ebmin = min((y for y in eb if y > a_ebpic), key=eb.get)
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

    # Series des figures
    r["serie_inv_fr"] = {y: J.pc(G, "S1313", "P51G", y) for y in J.annees(G, "S1313", "P51G")}
    r["serie_transf_fr"] = {y: J.pc(G, "S1313", "D73REC", y) for y in J.annees(G, "S1313", "D73REC") if y <= 2017}

    # ------------------------------------------------------------ gardes : chaque qualificatif de la prose
    gardes = [
        ("« la dette publique a presque doublé »", 1.6 <= r["dette_apu_fin"] / r["dette_apu_deb"] < 2.0),
        ("« la dette des collectivités a peu bougé » (moins d'un dixième de la hausse)", 0 <= r["part_hausse_loc"] < 10),
        ("« moins d'un dixième de la dette publique »", r["part_loc_fin"] < 10),
        ("« environ la moitié de l'investissement public »", 45 <= r["part_inv_loc_fin"] <= 60),
        ("« les transferts reçus ont baissé » (2013-2017)", r["ep_transf"] <= -0.3),
        ("« l'investissement local a reculé » (2013-2017)", r["ep_inv"] <= -0.3),
        ("« leur solde s'est amélioré » (2013-2017)", r["ep_solde_delta"] > 0),
        ("« jusqu'à un léger excédent »", 0 < r["ep_solde_a1"] < 0.3),
        ("« un pic isolé en 2010 » (annotation de la figure : compensation de la taxe professionnelle)", max(r["serie_transf_fr"], key=r["serie_transf_fr"].get) == 2010),
        ("« plus du double de la plus forte baisse des autres mandats »", r["creux_ratio"] >= 2),
        ("« les impôts n'ont compensé qu'une partie de la baisse des transferts »", 0 < r["ep_imp"] < -r["ep_transf"]),
        ("« en 2021, une recette a changé de case » (transferts en baisse, impôts en hausse)", r["rupt_transf"] <= -0.4 and r["rupt_imp"] >= 0.4),
        ("« depuis trois ans, les collectivités sont de nouveau en besoin de financement »", all(s < 0 for s in r["recent_soldes"])),
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
        ("« Espagne : plus de la moitié de la dette des communautés autonomes détenue par l'État central »", P["ES"]["part_etat_pct"] > 50),
        ("« Italie : environ un quart » détenu par l'État central", 15 <= P["IT"]["part_etat_pct"] <= 35),
        ("« France et Allemagne : part quasi nulle » détenue par l'État central", P["FR"]["part_etat_pct"] < 5 and P["DE"]["part_etat_pct"] < 5),
        ("« la dépense locale a monté puis reculé » (deux récits)", r["te_pic"] - r["te_0"] >= 1.5 and r["te_pic"] - r["te_fin"] >= 0.3),
        ("« DGF des départements et des régions en baisse de 2013 à 2017 » (OFGL)", r["of_dgf_dep_17"] < r["of_dgf_dep_13"] - 2 and r["of_dgf_reg_17"] < r["of_dgf_reg_13"] - 1),
        ("« 2018 : la DGF des régions disparaît presque, une fraction de TVA la remplace » (OFGL)", r["of_dgf_reg_18"] < 1 and r["of_tva_reg_18"] > 3),
        ("« épargne brute des départements divisée par plus de deux » (OFGL)", r["of_eb_dep_pic"] >= 2 * r["of_eb_dep_min"]),
        ("« puis remonte » (dernier exercice OFGL au-dessus du creux)", r["of_eb_dep_fin"] > r["of_eb_dep_min"]),
        ("« la DGF votée baisse chaque année de 2014 à 2017, de plus de 10 milliards au total » (CGCT L. 1613-1)",
         all(d < 0 for d in r["dgf_vote_baisses"]) and r["dgf_vote"][2013] - r["dgf_vote"][2017] > 10),
        ("« la somme des quatre catégories n'atteint pas la dette Maastricht des administrations locales »",
         r["of_encours_total"] < r["dette_loc_md"]),
        ("« équipement des communes en hausse de plus de 40 % depuis 2020 » (OFGL)", r["of_eq_com_fin"] >= 1.4 * r["of_eq_com_20"]),
        ("« depuis trois ans, le stock de dette locale augmente de nouveau »", J.dette(G, "S1313", an_dette_fin) > J.dette(G, "S1313", an_dette_fin - 2)),
        ("témoin du PIB (France) : comptes publics et comptes nationaux à 0,5 % près", r["temoin_pib_ecart_pct"]["FR"] <= 0.5),
        ("témoin comptable : TR − TE = B9 (écart ≤ 1 M€)", r["temoin_residu_max_meur"] <= 1.0),
        ("la cascade se referme sur le solde", abs(r["cascade_somme"] - r["ep_solde_delta"]) < 1e-9),
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
    ]
    rapport = [{"garde": g, "ok": bool(ok)} for g, ok in gardes]
    for g in rapport:
        if not g["ok"]:
            fail("garde dementie par les donnees : " + g["garde"])
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
        "te_a0": str(r["te_a0"]), "te_0": fr1(r["te_0"]), "te_apic": str(r["te_apic"]), "te_pic": fr1(r["te_pic"]), "te_fin": fr1(r["te_fin"]),
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
    for g, p in P.items():
        k = g.lower()
        a[f"{k}_dette_deb"] = fr1(p["dette_deb"])
        a[f"{k}_dette_pic"] = fr1(p["dette_pic"])
        a[f"{k}_dette_pic_annee"] = str(p["dette_pic_annee"])
        a[f"{k}_dette_fin"] = fr1(p["dette_fin"])
        a[f"{k}_inv_max"] = fr1(p["inv_max"])
        a[f"{k}_inv_max_annee"] = str(p["inv_max_annee"])
        a[f"{k}_inv_min"] = fr1(p["inv_min"])
        a[f"{k}_inv_min_annee"] = str(p["inv_min_annee"])
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


def cartouche(y0: float, source: str, note: str, lang: str = "fr") -> list[str]:
    lignes = [(source, INK2)] + ([(note, INK2)] if note else []) + [(LICENCES[lang], MUTED)]
    out = ['<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (y0, W, y0, GRID)]
    for k, (t, c) in enumerate(lignes):
        out.append('<text x="0" y="%.1f" font-size="9" fill="%s">%s</text>' % (y0 + 13 + 12 * k, c, esc(t)))
    return out


def txt(x, y, s, size=TY_ANNOT, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


SRC_SIGNATURE = "Eurostat gov_10a_main (S1313 : P51G, D73REC ; S13 : TE en % du PIB pour le dénominateur), administrations locales, France"
NOTE_SIGNATURE = "Transferts : série comparable arrêtée en 2017 (DGF des régions remplacée par une fraction de TVA en 2018)."
SRC_CASCADE = "Eurostat gov_10a_main, administrations locales (S1313), France ; points de PIB"
NOTE_CASCADE = "Lecture comptable : les postes reconstituent exactement la variation du solde ; ils ne disent pas ce qui l'a décidé."
SRC_EUROPE = "Eurostat gov_10q_ggdebt (4e trimestre) et gov_10dd_ggd (détention), S1312 + S1313, en % du PIB"
NOTE_EUROPE = "Périmètre statistique, non compétences : la France et l'Italie n'ont pas d'échelon d'États fédérés (S1312)."
# Textes des figures anglaises : meme dessin, memes donnees ; seuls les mots et le format des nombres changent.
FIG_EN = dict(
    src_signature="Eurostat gov_10a_main (S1313: P51G, D73REC; S13: TE in % of GDP for the denominator), local government, France",
    note_signature="Transfers: comparable series stops in 2017 (the regions' DGF grant was replaced by a share of VAT in 2018).",
    src_cascade="Eurostat gov_10a_main, local government (S1313), France; points of GDP",
    note_cascade="An accounting reading: the items add up exactly to the change in the balance; they do not say what decided it.",
    src_europe="Eurostat gov_10q_ggdebt (4th quarter) and gov_10dd_ggd (holdings), S1312 + S1313, in % of GDP",
    note_europe="Statistical scope, not responsibilities: France and Italy have no state-government tier (S1312).",
    postes=["Transfers received from other government units", "Local and shared taxes", "Other revenue",
            "Investment (lower spending)", "Other spending (lower spending)"],
)


def fig_signature(r: dict, lang: str = "fr") -> str:
    en = lang == "en"
    H = 420
    x0, x1, y0, y1 = 48, W - 12, 64, 352
    inv, tr = r["serie_inv_fr"], r["serie_transf_fr"]
    a_min, a_max = min(inv), max(inv)
    vmin, vmax = 1.5, 5.0
    X = lambda a: x0 + (a - a_min) / (a_max - a_min) * (x1 - x0)  # noqa: E731
    Y = lambda v: y1 - (v - vmin) / (vmax - vmin) * (y1 - y0)  # noqa: E731
    if en:
        titre = "Local government investment and transfers received, France, in % of GDP"
        e = entete(H, "cs", titre, "Two lines since %d: local investment hovers around 2%% of GDP, with a marked trough "
                   "after %s; transfers received fall from %s to %s." % (a_min, r["ep_a0"], r["ep_a0"], r["ep_a1"]))
    else:
        titre = "Investissement des collectivités et transferts reçus, France, en % du PIB"
        e = entete(H, "cs", titre, "Deux courbes depuis %d : l'investissement local oscille autour de 2 %% du PIB, avec un creux "
                   "marqué après %s ; les transferts reçus baissent de %s à %s." % (a_min, r["ep_a0"], r["ep_a0"], r["ep_a1"]))
    bx0, bx1 = X(2014), X(2017.999)
    e.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (bx0, y0, bx1 - bx0, y1 - y0, BANDE))
    for v in (2, 3, 4, 5):
        e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (x0, Y(v), x1, Y(v), GRID))
        e.append(txt(x0 - 6, Y(v) + 4, ("%d%%" if en else "%d %%") % v, TY_AXE, MUTED, "end"))
    for a in range(a_min, a_max + 1, 5):
        e.append(txt(X(a), y1 + 15, str(a), TY_AXE, MUTED, "middle"))
    e.append(txt((bx0 + bx1) / 2, y1 + 32, "2014-2017", TY_ANNOT, INK2, "middle"))
    e.append(txt((bx0 + bx1) / 2, y1 + 45, "grant cuts" if en else "baisse des dotations", TY_ANNOT, INK2, "middle"))
    for m in MUNICIPALES:
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="2 4"/>' % (X(m), y0, X(m), y1, AXIS))
        e.append(txt(X(m), y0 - 6, ("municipal elections %d" if en else "municipales %d") % m, 10, MUTED, "middle"))
    for s, col in ((tr, GRIS), (inv, BLEU)):
        pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(s.items()) if v is not None)
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6"/>' % (pts, col))
    a_pic = max(tr, key=tr.get)
    e.append(txt(X(a_pic) + 8, Y(tr[a_pic]) + 4, ("%d: compensation for the" if en else "%d : compensation") % a_pic))
    e.append(txt(X(a_pic) + 8, Y(tr[a_pic]) + 17, "abolished business tax" if en else "de la taxe professionnelle"))
    e.append(txt(X(2003), Y(tr[2003]) - 12, "transfers received" if en else "transferts reçus", TY_ANNOT, GRIS, "middle", "600"))
    e.append(txt(X(1997), Y(inv[1997]) + 22, "local investment" if en else "investissement local", TY_ANNOT, BLEU, "middle", "600"))
    e += (cartouche(H + 2, FIG_EN["src_signature"], FIG_EN["note_signature"], "en") if en
          else cartouche(H + 2, SRC_SIGNATURE, NOTE_SIGNATURE))
    e.append("</svg>")
    return "\n".join(e)


def fig_cascade(r: dict, lang: str = "fr") -> str:
    en = lang == "en"
    nb = en1 if en else fr1
    H = 330
    x0, x1, y0, y1 = 330, W - 50, 40, 300
    solde = "Balance " if en else "Solde "
    postes = FIG_EN["postes"] if en else [c["poste"] for c in r["ep_cascade"]]
    if len(postes) != len(r["ep_cascade"]):
        fail("cascade : libelles anglais et postes en nombre different")
    rows = ([(solde + str(r["ep_a0"]), r["ep_solde_a0"], "base")] + [(p_, c["pt_pib"], "pas") for p_, c in zip(postes, r["ep_cascade"])]
            + [(solde + str(r["ep_a1"]), r["ep_solde_a1"], "base")])
    vmin, vmax = -1.2, 1.4
    X = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)  # noqa: E731
    h = (y1 - y0) / len(rows)
    if en:
        titre = "Where the improvement in the local government balance came from, %s-%s" % (r["ep_a0"], r["ep_a1"])
        e = entete(H, "cc", titre, "Waterfall in points of GDP: lower transfers worsen the balance; higher taxes and lower "
                   "spending, mainly on investment, bring it back up to a slight surplus.")
    else:
        titre = "D’où vient l’amélioration du solde des collectivités, %s-%s" % (r["ep_a0"], r["ep_a1"])
        e = entete(H, "cc", titre, "Cascade en points de PIB : la baisse des transferts creuse le solde ; la hausse des impôts et "
                   "la baisse des dépenses, surtout d'investissement, le remontent jusqu'à un léger excédent.")
    for v in (-1, -0.5, 0, 0.5, 1):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0, X(v), y1, AXIS if v == 0 else GRID))
        e.append(txt(X(v), y1 + 15, nb(v, 1), TY_AXE, MUTED, "middle"))
    cum = 0.0
    for k, (lab, v, t) in enumerate(rows):
        yy, hh = y0 + k * h + h * 0.18, h * 0.64
        if t == "base":
            a, b, col, cum = min(0, v), max(0, v), INK2, v
        else:
            a, b = sorted((cum, cum + v))
            col = ORANGE if v < 0 else BLEU
            cum += v
        e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (X(a), yy, max(X(b) - X(a), 1.5), hh, col))
        e.append(txt(x0 - 10, yy + hh / 2 + 4, lab, TY_ANNOT, INK, "end"))
        e.append(txt(X(b) + 6, yy + hh / 2 + 4, ("+" if v > 0 and t == "pas" else "") + nb(v, 2)))
    e += (cartouche(H + 2, FIG_EN["src_cascade"], FIG_EN["note_cascade"], "en") if en
          else cartouche(H + 2, SRC_CASCADE, NOTE_CASCADE))
    e.append("</svg>")
    return "\n".join(e)


def fig_europe(r: dict, lang: str = "fr") -> str:
    en = lang == "en"
    nb = en1 if en else fr1
    H = 300
    pw, ph, gap = 150, 170, 22
    vmax = 30.0
    if en:
        titre = "Subnational government debt and the share held by central government, in % of GDP"
        e = entete(H, "ce", titre, "Four small charts. France: between 7 and 10%. Germany: between 20 and 30%, carried by the "
                   "Länder. Italy: rises, then falls back below 5%. Spain: from about 9% to more than 20%, more than half of it "
                   "held by central government.")
    else:
        titre = "Dette des administrations territoriales et part détenue par l’État central, en % du PIB"
        e = entete(H, "ce", titre, "Quatre petits graphiques. France : entre 7 et 10 %. Allemagne : entre 20 et 30 %, portée par les "
                   "Länder. Italie : monte puis redescend sous 5 %. Espagne : d'environ 9 % à plus de 20 %, dont plus de la moitié "
                   "détenue par l'État central.")
    for k, p in enumerate(r["pays"]):
        ox, oy = 46 + k * (pw + gap), 78
        s = p["serie_dette"]
        a0, a1 = min(s), max(s)
        X = lambda a: ox + (a - a0) / (a1 - a0) * pw  # noqa: E731
        Y = lambda v: oy + ph - v / vmax * ph  # noqa: E731
        e.append(txt(ox, oy - 14, p["nom_en"] if en else p["nom"], TY_ANNOT, INK, "start", "600"))
        for v in (0, 10, 20, 30):
            e.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (ox, Y(v), ox + pw, Y(v), GRID))
            if k == 0:
                e.append(txt(ox - 6, Y(v) + 4, ("%d%%" if en else "%d %%") % v, TY_AXE, MUTED, "end"))
        se = {a: v for a, v in p["serie_detenu_etat"].items() if a >= a0}  # meme fenetre que la dette, rien hors du panneau
        if se:
            pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(se.items()))
            e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % (pts, GRIS))
            if p["part_etat_pct"] >= 40:  # etiquette seulement la ou la part est majoritaire ; les autres sont dans le texte
                e.append(txt(X(a1), Y(se[a1]) + 16, ("of which central govt " if en else "dont État central ") + nb(se[a1]), 10, INK2, "end"))
        pts = " ".join("%.1f,%.1f" % (X(a), Y(v)) for a, v in sorted(s.items()))
        e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"/>' % (pts, BLEU))
        e.append(txt(X(a0), Y(s[a0]) - 6, nb(s[a0]), 10))
        e.append(txt(X(a1), Y(s[a1]) - 6, nb(s[a1]), 10, INK, "end", "600"))
        e.append(txt(ox, oy + ph + 15, str(a0), TY_AXE, MUTED))
        e.append(txt(ox + pw, oy + ph + 15, str(a1), TY_AXE, MUTED, "end"))
    e.append('<line x1="0" y1="36" x2="18" y2="36" stroke="%s" stroke-width="2.4"/>' % BLEU)
    e.append(txt(24, 40, "subnational government debt" if en else "dette des administrations territoriales", 10))
    e.append('<line x1="230" y1="36" x2="248" y2="36" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % GRIS)
    e.append(txt(254, 40, "of which held by central government (published since 2020 for Spain, France and Italy)" if en
                 else "dont détenue par l’État central (publiée depuis 2020 pour l’Espagne, la France et l’Italie)", 10))
    e += (cartouche(H + 2, FIG_EN["src_europe"], FIG_EN["note_europe"], "en") if en
          else cartouche(H + 2, SRC_EUROPE, NOTE_EUROPE))
    e.append("</svg>")
    return "\n".join(e)


def figures(r: dict) -> dict:
    out = {}
    for lang, x in SUFFIXE.items():
        out["collectivites-investissement%s.svg" % x] = fig_signature(r, lang)
        out["collectivites-cascade%s.svg" % x] = fig_cascade(r, lang)
        out["collectivites-europe%s.svg" % x] = fig_europe(r, lang)
    return out


def fiches_figures(figs: dict, A: dict, A_en: dict) -> dict:
    """Cartes du bloc « Réutiliser » : « montre » est écrit ici, ses chiffres viennent des jetons gardés ; titre,
    source et précaution sont relus dans le SVG."""
    import re as _re
    MONTRE = [
        ("investissement", "collectivites-investissement",
         "De %s à %s, les transferts reçus par les collectivités reculent de %s point de PIB et leur investissement de %s point ; "
         "le recul de l'investissement après les municipales de 2014 dépasse nettement celui des autres mandats."
         % (A["ep_a0"], A["ep_a1"], A["ep_transf"], A["ep_inv"])),
        ("cascade", "collectivites-cascade",
         "Le solde des collectivités s'améliore de %s point de PIB entre %s et %s, surtout par la baisse des dépenses, "
         "malgré la baisse des transferts reçus." % (A["ep_solde_delta"], A["ep_a0"], A["ep_a1"])),
        ("europe", "collectivites-europe",
         "Une même dette territoriale peut recouvrir des architectures opposées : en Espagne, %s %% en est détenue par l'État "
         "central ; en France, %s %%." % (A["es_part_etat_pct"], A["fr_part_etat_pct"])),
    ]
    MONTRE_EN = [
        ("investissement", "collectivites-investissement",
         "From %s to %s, the transfers received by local authorities fell by %s points of GDP and their investment by %s points; "
         "the fall in investment after the 2014 municipal elections clearly exceeds that of the other terms of office."
         % (A_en["ep_a0"], A_en["ep_a1"], A_en["ep_transf"], A_en["ep_inv"])),
        ("cascade", "collectivites-cascade",
         "The local government balance improved by %s points of GDP between %s and %s, mainly through lower spending, "
         "despite lower transfers received." % (A_en["ep_solde_delta"], A_en["ep_a0"], A_en["ep_a1"])),
        ("europe", "collectivites-europe",
         "The same subnational debt can conceal opposite architectures: in Spain, %s%% of it is held by central government; "
         "in France, %s%%." % (A_en["es_part_etat_pct"], A_en["fr_part_etat_pct"])),
    ]
    res = {}
    for lang, liste in (("fr", MONTRE), ("en", MONTRE_EN)):
        out = []
        for ident, fichier, montre in liste:
            fichier = fichier + SUFFIXE[lang]
            svg = figs[fichier + ".svg"]
            titre = html.unescape(_re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
            cart = [html.unescape(t) for t in _re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
            if len(cart) < 2 or cart[-1] != LICENCES[lang]:
                fail("fiche %s : cartouche illisible dans le SVG" % fichier)
            out.append(dict(id=ident, fichier=fichier, titre=titre, montre=montre, source=cart[0],
                            precaution=cart[1] if len(cart) == 3 else ""))
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
    return buf.getvalue()


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
    check = "--check" in sys.argv[1:]
    if not check:
        try:
            import cairosvg  # noqa: F401
        except ImportError:
            fail("cairosvg absent : SVG et PNG se produisent ensemble ou pas du tout (pip install cairosvg)")
    b = relever()
    J = Jeu(b)
    r, rapport = calculer(J)
    mord = autotest_mutation(b)
    log("autotest : la mutation a fait mordre -> " + mord)
    a = affichage(r)
    a_en = affichage(r, "en")
    if set(a) != set(a_en):
        fail("blocs affichage et affichage_en : cles differentes (%s)" % sorted(set(a) ^ set(a_en)))
    if check:
        log("--check : %d gardes tenues, rien ecrit." % len(rapport))
        return 0
    figs = figures(r)
    fiches = fiches_figures(figs, a, a_en)
    csvt = csv_texte(r)
    payload = {
        "meta": {"page": "https://" + PAGE_URL, "licence": "CC BY 4.0",
                 "sources": {k: {"jeu": b[k]["dataset"], "maj_source": b[k]["maj_eurostat"], "sha256": b[k]["sha256"]}
                             for k in ("comptes", "te_pc", "pib", "dette", "ggd", "ofgl")},
                 "definitions": {"perimetre_local": "S1313 : administrations publiques locales (collectivités, syndicats, ODAL)",
                                 "perimetre_territorial": "S1312 + S1313 (États fédérés, s'il en existe, et administrations locales)",
                                 "transferts": "D73REC : transferts courants reçus des autres administrations publiques (État et sécurité sociale)",
                                 "dgf_votee": "montant de la DGF fixé par la loi de finances (CGCT art. L. 1613-1)"}},
        "gardes": rapport,
        "calcul": {k: v for k, v in r.items() if not k.startswith("serie_")},
        "series": {k: v for k, v in r.items() if k.startswith("serie_")},
        "affichage": a,
        "affichage_en": a_en,
    }
    releve = b["releve_le"]
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
