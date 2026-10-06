#!/usr/bin/env python3
"""Volet « Adopter » du dossier Promesses : qui est à l'origine des lois votées, et l'engagement de responsabilité
(art. 49, al. 3).

Protocole : D:/PRO/06_PROMOTION/RECHERCHE_DOSSIER_PROMESSES_2026-10-05/FICHES_PREUVE.md, volet 2 (v2, gelée au commit
dfd0ec9). Test décisif du 06/10/2026 : test_decisif/adopter/VERDICT.md (19 mutations).
  E2 — origine formelle, au dépôt initial, des lois ordinaires promulguées, par législature de promulgation ; traités
       exclus et dénombrés ; autres natures à part. Concordance AN / Dosleg loi par loi, aucun désaccord.
  E3 — engagements de responsabilité (art. 49, al. 3), un par texte et par étape ; motions liées.
  E1 (parcours des propositions jusqu'à la séance) : NON PUBLIÉ, témoin des bulletins non réconcilié (clause 4).

Sources (scripts/sources_adopter/, constituées par extraire_sources.py) : registre loi par loi e2_lois.csv (JO, AN,
Dosleg, DOLE) ; e3_engagements.csv ; bulletins statistiques de l'AN (bulletins_493.csv) ; fiche n° 64 de l'AN et
rapport n° 802 du Sénat, p. 44 (pages_temoins.json) ; Constitution, art. 24, 39, 48, 49 (Légifrance).

Gardes (toutes ARRÊTENT, rien n'est écrit) :
  B1  articles de la Constitution en vigueur, citations retrouvées mot pour mot ;
  B2  E2 : aucun désaccord d'origine AN / Dosleg ; bornes [P - source unique ; P] ; phrases de la page : moins de la
      moitié sous la XIVe (borne haute), plus de la moitié sous les XVe et XVIe (borne basse) ;
  B3  TÉMOINS : par session 2017-2018 à 2024-2025, nombre de lois hors traités = champ du baromètre d'Appliquer
      (autre producteur) ; 2024-2025 : 45 lois parlementaires sur 56, comme le publie le Sénat ; 2023-2024 compatible
      avec « 58 % » ;
  B4  E3 : engagements par législature = fiche n° 64 de l'AN ; = bulletins, session par session ; XVIe : aucun texte
      hors finances ; aucune motion adoptée de la XIVe à la XVIe (bulletins) ; une en 2024-2025.
Autotest de mutation à chaque exécution : origine d'une loi changée dans une source -> B2 ; une loi de 2024-2025
retirée -> B3 ; un engagement de la XVIe retiré -> B4 ; citation de l'art. 49 altérée -> B1 ; XIVe rendue majoritaire
-> B2.

Écrit : data/promesses_adopter.json (+ static/), static/promesses_adopter.csv, data/figures_adopter.json,
static/img/adopter-{origine,493}.svg/.png. Rien n'est écrit à données identiques.
"""
from __future__ import annotations

import collections
import copy
import csv
import html
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "sources_adopter"
REG_APPLIQUER = ROOT / "scripts" / "sources_appliquer" / "registre_concordance.csv"
PAGE_URL = "stephane-lalut.com/qui-peut-faire-adopter-une-loi/"
OUT_DATA = ROOT / "data" / "promesses_adopter.json"
OUT_STATIC = ROOT / "static" / "promesses_adopter.json"
OUT_CSV = ROOT / "static" / "promesses_adopter.csv"
OUT_FIGURES = ROOT / "data" / "figures_adopter.json"
OUT_IMG = ROOT / "static" / "img"
RELEVE = "06/10/2026"
LEGS = ["14", "15", "16"]
ROMAIN = {"14": "XIVe", "15": "XVe", "16": "XVIe", "17": "XVIIe"}
PERIODE = {"14": "2012-2017", "15": "2017-2022", "16": "2022-2024", "17": "depuis 2024"}
SESSIONS = ["%d-%d" % (a, a + 1) for a in range(2017, 2025)]
MOTS = {"une": 1, "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
CONST = {  # article -> (fichier, citation exacte)
    "24": ("legifrance_f1e5f5212fef6ab730c4ed48b20035974af48b59ee63d13a3331e0b76eeae4fa.json", "Le Parlement vote la loi."),
    "39": ("legifrance_751fa83fbb33037dfca31b34cb249316880035dc384b20d05a1b3e138b8df786.json",
           "L'initiative des lois appartient concurremment au Premier ministre et aux membres du Parlement."),
    "48": ("legifrance_376cbf6be973f815b0e9c33efecf371b16a12234c1193d3601a1df641c7b12bb.json",
           "Deux semaines de séance sur quatre sont réservées par priorité, et dans l'ordre que le Gouvernement a fixé, à "
           "l'examen des textes et aux débats dont il demande l'inscription à l'ordre du jour."),
    "49a": ("legifrance_8a30c40da44752bff91c17c1b15577bd338063c08a795785629c90d08ea40ccd.json",
            "Le Premier ministre peut, après délibération du Conseil des ministres, engager la responsabilité du "
            "Gouvernement devant l'Assemblée nationale sur le vote d'un projet de loi de finances ou de financement de la "
            "sécurité sociale. Dans ce cas, ce projet est considéré comme adopté, sauf si une motion de censure, déposée "
            "dans les vingt-quatre heures qui suivent, est votée dans les conditions prévues à l'alinéa précédent."),
    "49b": ("legifrance_8a30c40da44752bff91c17c1b15577bd338063c08a795785629c90d08ea40ccd.json",
            "Le Premier ministre peut, en outre, recourir à cette procédure pour un autre projet ou une proposition de loi "
            "par session."),
}
TEMOINS = {
    "cit_fiche64": ("fiche64", "Cet instrument a néanmoins été utilisé à six reprises, sur deux projets de loi différents, "
                    "sous la XIVe législature, à une reprise sous la XVe législature, et à 23 reprises sous la XVIe législature."),
    "cit_censure": ("fiche64", "La première motion déposée a été adoptée selon la majorité qualifiée requise"),
    "cit_senat_origine": ("r25-802|44", "Sur la session, 80 % des lois adoptées (45 sur 56) sont d'origine parlementaire, "
                          "contre 58 % en 2023-2024"),
}
FINANCIER = re.compile(r"finances|financement (rectificative )?de la sécurité sociale", re.I)


class Arret(Exception):
    pass


def log(m: str) -> None:
    print(m.encode("ascii", "replace").decode("ascii"))


def norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2019", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def fr(n, dec=0) -> str:
    return ("{:,.%df}" % dec).format(n).replace(",", "\u202f").replace(".", ",")


def session(d: str) -> str:
    a = int(d[:4]) if int(d[5:7]) >= 10 else int(d[:4]) - 1
    return "%d-%d" % (a, a + 1)


def lire_csv(p: Path, sep=",") -> list[dict]:
    return list(csv.DictReader(io.StringIO(p.read_text(encoding="utf-8")), delimiter=sep))


def lire() -> dict:
    const = {}
    for k, (f, _) in CONST.items():
        a = json.loads((SRC / f).read_text(encoding="utf-8"))
        a = a.get("contenu") or a.get("article")
        const[k] = {"etat": a["etat"], "texte": norm(a["texte"]), "id": a["id"]}
    return {"const": const, "lois": lire_csv(SRC / "e2_lois.csv"), "eng": lire_csv(SRC / "e3_engagements.csv"),
            "bull": lire_csv(SRC / "bulletins_493.csv"), "reg": lire_csv(REG_APPLIQUER, ";"),
            "pages": json.loads((SRC / "pages_temoins.json").read_text(encoding="utf-8"))}


# ------------------------------------------------------------------ calcul et gardes
def calculer(S: dict) -> tuple[dict, list[str]]:
    g, cit = [], {}
    for k, (_, c) in CONST.items():
        if S["const"][k]["etat"] != "VIGUEUR" or norm(c) not in S["const"][k]["texte"]:
            raise Arret("B1 : Constitution art. %s : texte non en vigueur ou citation introuvable" % k)
        cit["cit_art" + k] = norm(c)
    for k, (pg, c) in TEMOINS.items():
        if norm(c) not in S["pages"][pg]["texte"]:
            raise Arret("B1 : citation %s absente de %s" % (k, pg))
        cit[k] = norm(c)
    g.append("B1 : %d citations de la Constitution, %d des temoins, retrouvees mot pour mot" % (len(CONST), len(TEMOINS)))

    # --- E2
    L = S["lois"]
    for r in L:
        if r["origine_AN"] and r["origine_Dosleg"] and r["origine_AN"] != r["origine_Dosleg"]:
            raise Arret("B2 : %s : origine AN (%s) != Dosleg (%s)" % (r["numero"], r["origine_AN"], r["origine_Dosleg"]))
    leg = {}
    for l in LEGS + ["17"]:
        o = [r for r in L if r["legislature"] == l and r["nature"] == "ordinaire"]
        c = collections.Counter(r["origine"] for r in o)
        P = c["parlementaire AN"] + c["parlementaire Sénat"]
        uniq = sum(1 for r in o if r["origine"].startswith("parlementaire") and r["origine_source"].startswith("source unique"))
        leg[l] = {"N": len(o), "P": P, "Pmin": P - uniq, "gouv": c["gouvernement"], "AN": c["parlementaire AN"],
                  "SEN": c["parlementaire Sénat"], "traites": sum(1 for r in L if r["legislature"] == l and r["nature"] == "traite"),
                  "autres": sum(1 for r in L if r["legislature"] == l and r["nature"] not in ("ordinaire", "traite"))}
        if leg[l]["N"] != leg[l]["P"] + leg[l]["gouv"]:
            raise Arret("B2 : %s : origine indeterminee ou inconnue" % l)
    fin_parl = [r["numero"] for r in L if r["legislature"] in LEGS and r["nature"] == "finances_fss" and r["origine"] != "gouvernement"]
    if fin_parl:  # phrase : « les lois de finances et de financement de la sécurité sociale viennent toutes d'un projet »
        raise Arret("B2 : lois financieres d'origine parlementaire : %s" % fin_parl)
    x14, x15, x16 = leg["14"], leg["15"], leg["16"]
    if not (2 * x14["P"] < x14["N"] and 2 * x15["Pmin"] > x15["N"] and 2 * x16["Pmin"] > x16["N"]):
        raise Arret("B2 : « moins de la moitie sous la XIVe, plus de la moitie sous les XVe et XVIe » faux")
    g.append("B2 : origine concordante AN/Dosleg ; parlementaires XIV %d/%d, XV %d-%d/%d, XVI %d/%d"
             % (x14["P"], x14["N"], x15["Pmin"], x15["P"], x15["N"], x16["P"], x16["N"]))

    # --- témoins par session (autre producteur pour le champ ; publication du Sénat pour l'origine)
    regN = collections.Counter(r["session"] for r in S["reg"])
    ses = {}
    for s in SESSIONS:
        o = [r for r in L if r["nature"] != "traite" and r["legislature"] != "" and session(r["date_promulgation"]) == s]
        ses[s] = {"N": len(o), "P": sum(1 for r in o if r["origine"].startswith("parlementaire"))}
        if ses[s]["N"] != regN[s]:
            raise Arret("B3 : session %s : %d lois hors traites ici, %d au barometre (Appliquer)" % (s, ses[s]["N"], regN[s]))
    if (ses["2024-2025"]["P"], ses["2024-2025"]["N"]) != (45, 56) or "(45 sur 56)" not in cit["cit_senat_origine"]:
        raise Arret("B3 : 2024-2025 : %d/%d contre 45 sur 56 publies par le Senat" % (ses["2024-2025"]["P"], ses["2024-2025"]["N"]))
    if not abs(100 * ses["2023-2024"]["P"] / ses["2023-2024"]["N"] - 58) < 1:
        raise Arret("B3 : 2023-2024 incompatible avec « 58 % »")
    g.append("B3 : champ par session = barometre (8 sessions) ; 2024-2025 45/56 = Senat ; 2023-2024 %d/%d ~ 58 %%"
             % (ses["2023-2024"]["P"], ses["2023-2024"]["N"]))

    # --- E3
    E = S["eng"]
    eng = {}
    for l in LEGS + ["17"]:
        e = [r for r in E if r["legislature"] == l]
        eng[l] = {"n": len(e), "fin": sum(1 for r in e if FINANCIER.search(r["titre"])),
                  "textes": len({r["dossier_texte"] for r in e}),
                  "adoptees": sum(int(r["motions_adoptees"] or 0) for r in e)}
    m = re.search(r"à (\w+) reprises, sur (\w+) projets de loi différents, sous la XIVe législature, à (\w+) reprise sous "
                  r"la XVe législature, et à (\w+) reprises sous la XVIe", cit["cit_fiche64"])
    nb = [int(v) if v.isdigit() else MOTS[v] for v in m.groups()]
    if [eng["14"]["n"], eng["14"]["textes"], eng["15"]["n"], eng["16"]["n"]] != nb:
        raise Arret("B4 : engagements %s != fiche n° 64 %s" % ([eng[l]["n"] for l in LEGS], nb))
    B = S["bull"]
    for l in LEGS + ["17"]:  # sur la période couverte par les bulletins (XVIIe : jusqu'au 30/09/2025)
        bl = [r for r in B if r["legislature"] == l]
        b = sum(int(r["engagements_493"]) for r in bl)
        fin = max(r["fin"] for r in bl)
        n = sum(1 for r in E if r["legislature"] == l and r["date"] <= fin)
        if b != n:
            raise Arret("B4 : legislature %s : %d engagements aux bulletins, %d extraits jusqu'au %s" % (l, b, n, fin))
    if eng["14"]["fin"] != 0:  # phrase : « sur N projets de loi qui n'étaient pas des textes financiers »
        raise Arret("B4 : XIVe : engagement sur un texte financier")
    if eng["16"]["fin"] != eng["16"]["n"]:
        raise Arret("B4 : XVIe : engagement hors texte financier")
    adoptees_bull = {l: sum(int(r["motions_493_adoptees"] or 0) for r in B if r["legislature"] == l) for l in LEGS + ["17"]}
    if any(adoptees_bull[l] for l in LEGS) or adoptees_bull["17"] != 1:
        raise Arret("B4 : motions adoptees aux bulletins : %s" % adoptees_bull)
    cens = [r for r in E if int(r["motions_adoptees"] or 0) > 0]
    if len(cens) != 1 or cens[0]["legislature"] != "17":
        raise Arret("B4 : engagements suivis d'une motion adoptee : %d" % len(cens))
    MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    an, mo, jo = map(int, cens[0]["date"].split("-"))
    cit["censure_date"] = "%d%s %s %d" % (jo, "er" if jo == 1 else "", MOIS[mo - 1], an)
    g.append("B4 : engagements XIV %d, XV %d, XVI %d (= fiche 64 et bulletins) ; XVI tous financiers ; 0 motion adoptee XIV-XVI"
             % (eng["14"]["n"], eng["15"]["n"], eng["16"]["n"]))
    return {"leg": leg, "ses": ses, "eng": eng, "cit": cit}, g


def affichage(r: dict) -> dict:
    A = {"releve": RELEVE}
    for l, x in r["leg"].items():
        A.update({"N%s" % l: fr(x["N"]), "P%s" % l: fr(x["P"]), "Pmin%s" % l: fr(x["Pmin"]), "G%s" % l: fr(x["gouv"]),
                  "AN%s" % l: fr(x["AN"]), "SEN%s" % l: fr(x["SEN"]), "T%s" % l: fr(x["traites"]),
                  "Ppct%s" % l: fr(100 * x["P"] / x["N"])})
    for l, x in r["eng"].items():
        A.update({"E%s" % l: fr(x["n"]), "Efin%s" % l: fr(x["fin"]), "Etextes%s" % l: fr(x["textes"])})
    s1, s2 = r["ses"]["2017-2018"], r["ses"]["2024-2025"]
    A.update({"s1718_P": fr(s1["P"]), "s1718_N": fr(s1["N"]), "s2425_P": fr(s2["P"]), "s2425_N": fr(s2["N"]),
              "releve_le": "06/10/2026 (données de l'Assemblée nationale et base Dosleg du Sénat du 06/10/2026, Journal "
                           "officiel ; bulletins statistiques de l'Assemblée nationale)"})
    A.update(r["cit"])
    return A


def tableaux(r: dict) -> dict:
    lois = [[ROMAIN[l] + " (" + PERIODE[l] + (", en cours au " + RELEVE if l == "17" else "") + ")", fr(x["N"]), fr(x["gouv"]),
             fr(x["AN"]), fr(x["SEN"]), fr(x["P"]) + ("" if x["Pmin"] == x["P"] else " (au moins %s)" % fr(x["Pmin"])),
             fr(x["traites"])] for l, x in r["leg"].items()]
    ses = [[s, fr(x["N"]), fr(x["P"]), fr(100 * x["P"] / x["N"]) + " %"] for s, x in r["ses"].items()]
    eng = [[ROMAIN[l] + (" (en cours)" if l == "17" else ""), fr(x["n"]), fr(x["fin"]), fr(x["n"] - x["fin"]), fr(x["adoptees"])]
           for l, x in r["eng"].items()]
    return {
        "lois": {"entetes": ["Législature de promulgation", "Lois ordinaires", "Projet du Gouvernement",
                             "Proposition déposée à l'Assemblée", "Proposition déposée au Sénat", "Origine parlementaire",
                             "Lois autorisant un traité (exclues)"], "lignes": lois},
        "sessions": {"entetes": ["Session", "Lois promulguées hors traités", "D'origine parlementaire", "Part"], "lignes": ses},
        "engagements": {"entetes": ["Législature", "Engagements (art. 49, al. 3)", "Sur un texte financier", "Sur un autre texte",
                                    "Motions de censure adoptées"], "lignes": eng},
    }


# ------------------------------------------------------------------ figures
W = 720
BLEU, BLEU_CLAIR, GRIS, GRIS_CLAIR = "#184f95", "#7fa3cf", "#8a8781", "#c9c5c0"
INK, INK2, MUTED, GRID = "#0A0A0E", "#52514e", "#898781", "#e1e0d9"
FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
LICENCE = "Compilation Stéphane Lalut, CC BY 4.0 · " + PAGE_URL


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def txt(x, y, s, size=11, fill=INK2, anchor="start", weight=None) -> str:
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%.1f" y="%.1f" font-size="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, fill, anchor, w, esc(s))


def cadre(H, ident, titre, sous, desc) -> list[str]:
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" font-variant-numeric="tabular-nums" '
            'aria-labelledby="%s-t %s-d" font-family="%s">' % (W, H + 48, ident, ident, FONT),
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>' % (ident, esc(titre), ident, esc(desc)),
            '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H + 48),
            txt(0, 18, titre, 13, INK, weight="600"), txt(0, 36, sous, 12, INK2)]


def cartouche(H, src, note) -> list[str]:
    out = ['<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (H + 2, W, H + 2, GRID)]
    for k, (t, c) in enumerate(((src, INK2), (note, INK2), (LICENCE, MUTED))):
        out.append('<text x="0" y="%d" font-size="9" fill="%s">%s</text>' % (H + 15 + 12 * k, c, esc(t)))
    return out


def legende(e, y, items) -> None:
    x = 0
    for col, lab in items:
        e.append('<rect x="%d" y="%d" width="11" height="11" fill="%s"/>' % (x, y - 9, col))
        e.append(txt(x + 16, y, lab, 10, INK2))
        x += 16 + 6.2 * len(lab) + 18


SRC1 = "Assemblée nationale (données ouvertes, dossiers législatifs) et Sénat (base Dosleg), 06/10/2026 ; Journal officiel"
NOTE1 = "Origine formelle au dépôt initial : elle ne mesure ni l'influence du Gouvernement ni les amendements. Traités exclus."
SRC2 = "Assemblée nationale : dossiers législatifs, bulletins statistiques, fiche n° 64 (engagements de responsabilité)"
NOTE2 = "Un engagement par texte et par étape de lecture. XVIIe législature en cours au " + RELEVE + "."


def fig_origine(r: dict, A: dict) -> str:
    H = 250
    x0, x1, y0, pas = 150, W - 70, 74, 34
    vmax = 250
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    e = cadre(H, "ao", "Qui est à l'origine des lois ordinaires promulguées ?",
              "nombre de lois, par législature de promulgation ; trait noir : la moitié des lois",
              "Barres horizontales par législature : lois issues d'un projet du Gouvernement, d'une proposition déposée à "
              "l'Assemblée, d'une proposition déposée au Sénat. XIVe : %s d'origine parlementaire sur %s ; XVe : %s sur %s ; "
              "XVIe : %s sur %s ; XVIIe en cours." % (A["P14"], A["N14"], A["P15"], A["N15"], A["P16"], A["N16"]))
    legende(e, 58, [(GRIS_CLAIR, "projet du Gouvernement"), (BLEU, "proposition déposée à l'Assemblée"),
                    (BLEU_CLAIR, "proposition déposée au Sénat")])
    for v in range(0, vmax + 1, 50):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 4 - 6, GRID))
        e.append(txt(X(v), y0 + pas * 4 + 8, str(v), 9, MUTED, "middle"))
    for i, (l, x) in enumerate(r["leg"].items()):
        y = y0 + i * pas
        e.append(txt(0, y + 14, ROMAIN[l] + " (" + PERIODE[l] + ")" + (" *" if l == "17" else ""), 10, INK))
        a = 0
        for v, col in ((x["gouv"], GRIS_CLAIR), (x["AN"], BLEU), (x["SEN"], BLEU_CLAIR)):
            e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2"/>' % (X(x["N"] / 2), y - 3, X(x["N"] / 2), y + 23, INK))
        e.append(txt(X(a) + 4, y + 14, "%s lois" % fr(x["N"]), 9, INK2))
    e.append(txt(0, y0 + pas * 4 + 22, "* en cours au %s" % RELEVE, 9, INK2))
    e += cartouche(H, SRC1, NOTE1)
    e.append("</svg>")
    return "\n".join(e)


def fig_493(r: dict, A: dict) -> str:
    H = 250
    x0, x1, y0, pas = 150, W - 90, 74, 34
    vmax = 25
    X = lambda v: x0 + v / vmax * (x1 - x0)  # noqa: E731
    e = cadre(H, "a4", "Engagements de responsabilité sur un texte (art. 49, al. 3)",
              "nombre d'engagements, par législature ; un engagement par texte et par étape de lecture",
              "Barres horizontales par législature : engagements sur un texte financier (loi de finances, de financement "
              "de la sécurité sociale, de programmation des finances publiques) et sur un autre texte. XIVe : %s ; XVe : %s ; "
              "XVIe : %s, tous sur des textes financiers ; XVIIe en cours." % (A["E14"], A["E15"], A["E16"]))
    legende(e, 58, [(BLEU, "texte financier"), (GRIS_CLAIR, "autre texte")])
    for v in range(0, vmax + 1, 5):
        e.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(v), y0 - 4, X(v), y0 + pas * 4 - 6, GRID))
        e.append(txt(X(v), y0 + pas * 4 + 8, str(v), 9, MUTED, "middle"))
    for i, (l, x) in enumerate(r["eng"].items()):
        y = y0 + i * pas
        e.append(txt(0, y + 14, ROMAIN[l] + " (" + PERIODE[l] + ")" + (" *" if l == "17" else ""), 10, INK))
        a = 0
        for v, col in ((x["fin"], BLEU), (x["n"] - x["fin"], GRIS_CLAIR)):
            if v:
                e.append('<rect x="%.1f" y="%d" width="%.1f" height="20" fill="%s"/>' % (X(a), y, X(a + v) - X(a), col))
            a += v
        e.append(txt(X(a) + 4, y + 14, "%s" % fr(x["n"]), 10, INK, weight="600"))
    e.append(txt(0, y0 + pas * 4 + 22, "* en cours au %s" % RELEVE, 9, INK2))
    e += cartouche(H, SRC2, NOTE2)
    e.append("</svg>")
    return "\n".join(e)


def fiches(figs: dict, A: dict) -> dict:
    montre = {
        "origine": ("adopter-origine", "Parmi les lois ordinaires promulguées, %s sur %s sont d'origine parlementaire sous la "
                    "XIVe législature, %s sur %s sous la XVe et %s sur %s sous la XVIe ; origine formelle au dépôt initial."
                    % (A["P14"], A["N14"], A["P15"], A["N15"], A["P16"], A["N16"])),
        "493": ("adopter-493", "Le Gouvernement a engagé sa responsabilité sur un texte %s fois sous la XIVe législature, %s fois "
                "sous la XVe et %s fois sous la XVIe, toutes sur des textes financiers." % (A["E14"], A["E15"], A["E16"])),
    }
    out = []
    for ident, (fichier, m) in montre.items():
        svg = figs[fichier + ".svg"]
        titre = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", svg).group(1))
        cart = [html.unescape(t) for t in re.findall(r'<text x="0" y="[0-9.]+" font-size="9" fill="[^"]+">(.*?)</text>', svg)]
        cart = [c for c in cart if not c.startswith("* en cours")]
        if len(cart) != 3 or cart[-1] != LICENCE:
            raise Arret("fiche %s : cartouche illisible" % fichier)
        out.append(dict(id=ident, fichier=fichier, titre=titre, montre=m, source=cart[0], precaution=cart[1]))
    return {"fr": out}


def csv_texte(r: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["serie", "periode", "categorie", "valeur", "unite", "source"])
    for l, x in r["leg"].items():
        for k in ("N", "gouv", "AN", "SEN", "P", "Pmin", "traites", "autres"):
            w.writerow(["lois_ordinaires_promulguees", "legislature_" + l, k, x[k], "lois", "AN, Dosleg, JO"])
    for s, x in r["ses"].items():
        w.writerow(["lois_hors_traites", s, "N", x["N"], "lois", "AN, Dosleg, JO"])
        w.writerow(["lois_hors_traites", s, "origine_parlementaire", x["P"], "lois", "AN, Dosleg, JO"])
    for l, x in r["eng"].items():
        for k in ("n", "fin", "adoptees"):
            w.writerow(["engagements_49_3", "legislature_" + l, k, x[k], "engagements", "AN"])
    return buf.getvalue()


def autotest(S: dict) -> list[str]:
    out = []

    def origine(m):
        for r in m["lois"]:
            if r["legislature"] == "15" and r["origine_AN"] == "parlementaire AN":
                r["origine_AN"] = "gouvernement"
                return

    def retire(m):
        for i, r in enumerate(m["lois"]):
            if r["nature"] == "ordinaire" and session(r["date_promulgation"]) == "2024-2025":
                del m["lois"][i]
                return

    def engagement(m):
        for i, r in enumerate(m["eng"]):
            if r["legislature"] == "16":
                del m["eng"][i]
                return

    def citation(m):
        m["const"]["49b"]["texte"] = m["const"]["49b"]["texte"].replace("par session", "par an")

    def majorite(m):
        n = 0
        for r in m["lois"]:
            if r["legislature"] == "14" and r["nature"] == "ordinaire" and r["origine"] == "gouvernement" and n < 12:
                for k in ("origine", "origine_AN", "origine_Dosleg"):
                    if r[k]:
                        r[k] = "parlementaire AN"
                n += 1

    for nom, mut, pref in (("origine changee dans une source", origine, "B2"), ("loi 2024-2025 retiree", retire, "B3"),
                           ("engagement XVIe retire", engagement, "B4"), ("art. 49 altere", citation, "B1"),
                           ("XIVe rendue majoritaire", majorite, "B2")):
        m = copy.deepcopy(S)
        mut(m)
        try:
            calculer(m)
            raise Arret("mutation %s : aucune garde n'a mordu, controle ABSENT" % nom)
        except Arret as e:
            if not str(e).startswith(pref) or str(e).startswith("mutation"):
                raise
            out.append("%s -> %s" % (nom, str(e)[:70]))
    return out


def main() -> int:
    try:
        return _main()
    except Arret as e:
        log("ARRET : " + str(e))
        log("Aucun fichier ecrit.")
        return 1


def _main() -> int:
    S = lire()
    r, g = calculer(S)
    for m in autotest(S):
        log("autotest : la mutation a mordu : " + m)
    A = affichage(r)
    if "--check" in sys.argv[1:]:
        log("--check : %d gardes tenues, rien ecrit." % len(g))
        return 0
    import cairosvg
    figs = {"adopter-origine.svg": fig_origine(r, A), "adopter-493.svg": fig_493(r, A)}
    fi = fiches(figs, A)
    csvt = csv_texte(r)
    payload = {
        "releve_le": "2026-10-06",
        "_licence": "CC BY 4.0 — compilation Stéphane Lalut ; sources Assemblée nationale, Sénat (Dosleg), Journal officiel "
                    "(DILA), Légifrance",
        "meta": {"page": "https://" + PAGE_URL, "protocole": "fiches de preuve v2, volet Adopter, E2 et E3 (E1 non publié)",
                 "constitution": {k: v["id"] for k, v in S["const"].items()},
                 "temoins": {k: v["sha256_document"] for k, v in S["pages"].items()},
                 "definitions": {
                     "origine": "origine formelle au dépôt initial : projet du Gouvernement, proposition déposée à l'Assemblée "
                                "nationale, proposition déposée au Sénat ; rattachement à la législature de promulgation",
                     "Pmin": "origine parlementaire établie par les deux sources (AN et Dosleg) ; l'écart avec P vient de lois "
                             "dont le dossier manque aux fichiers de l'AN pour un motif établi (dépôt sous la législature "
                             "précédente)",
                     "engagement": "un engagement de responsabilité (art. 49, al. 3) par texte et par étape de lecture",
                     "texte_financier": "loi de finances, de financement de la sécurité sociale ou de programmation des "
                                        "finances publiques (titre du dossier)"},
                 "limites": "l'origine formelle n'observe ni l'influence du Gouvernement sur une proposition, ni les "
                            "amendements ; le parcours des propositions jusqu'à la séance (E1) n'est pas publié : le décompte "
                            "des dépôts ne concorde pas encore avec les bulletins de l'Assemblée"},
        "gardes": g,
        "calcul": {"legislatures": r["leg"], "sessions": r["ses"], "engagements": r["eng"]},
        "tableaux": tableaux(r),
        "affichage": A,
    }
    txt_json = json.dumps(payload, ensure_ascii=False, indent=1, default=str)
    if (OUT_DATA.exists() and OUT_DATA.read_text(encoding="utf-8") == txt_json and OUT_CSV.exists()
            and OUT_CSV.read_text(encoding="utf-8-sig") == csvt
            and all((OUT_IMG / n).exists() and (OUT_IMG / n).read_text(encoding="utf-8") == s for n, s in figs.items())
            and OUT_FIGURES.exists() and json.loads(OUT_FIGURES.read_text(encoding="utf-8")) == fi):
        log("Donnees et figures identiques : rien ecrit.")
        return 0
    OUT_DATA.write_text(txt_json, encoding="utf-8")
    OUT_STATIC.write_text(txt_json, encoding="utf-8")
    OUT_CSV.write_text(csvt, encoding="utf-8-sig", newline="\n")
    for n, s in figs.items():
        (OUT_IMG / n).write_text(s, encoding="utf-8")
        cairosvg.svg2png(url=str(OUT_IMG / n), write_to=str(OUT_IMG / n.replace(".svg", ".png")), output_width=1440,
                         background_color="white")
    OUT_FIGURES.write_text(json.dumps(fi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in g:
        log("OK " + x)
    log("Ecrit : data/promesses_adopter.json, static/promesses_adopter.{json,csv}, data/figures_adopter.json, 2 figures SVG + PNG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
