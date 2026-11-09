# -*- coding: utf-8 -*-
"""update_annulation_bdf.py -- chiffres de la section « Annuler la dette détenue par la Banque de France : qui
paierait ? » de /qui-paie-la-dette-publique/ (#annuler-banque-de-france), FR et EN.

Conception : docs/conception/annuler-dette-banque-de-france.md ; contre-expertise PRO-20261109-025514 et son arbitrage
(la comparaison se fait entre deux trajectoires : refinancer les titres sur le marché, ou garder les réserves).

Ce que le script LIT :
- scripts/sources_qe_maturite/rendement_cycle.tsv (extrait figé, SHA256SUMS) : taux de référence de la BCE retenu pour le
  revenu monétaire (i, moyenne annuelle ; taux de dépôt depuis 2025), rendement comptable des titres de l'État détenus
  par la Banque de France (r_t), encours moyen (B) et écart de portage publié (C) ;
- data/dette_officielle.json (update_dette_insee.py) : rendement à dix ans de l'État (Eurostat irt_lt_mcby_a, m),
  dette de Maastricht et son ratio au dernier trimestre (INSEE).
Ce que le script ne lit pas mais reprend, TRANSCRIT et vérifié contre la source archivée :
- scripts/sources_annulation_bdf/valeurs_transcrites.json : encours de dette publique détenu par la Banque de France au
  titre de l'APP et du PEPP (coût amorti ; communiqué de la Banque de France) et taux de la facilité de dépôt en vigueur
  (BCE). Chaque valeur porte sa source, sa date et la date de vérification.

Gardes (une phrase de la page = une condition ; si la donnée ne la remplit plus, arrêt, rien écrit) et témoin comptable
(C recalculé = C publié). Usage :
  python scripts/update_annulation_bdf.py            # calcule, contrôle, écrit data/annulation_bdf.json
  python scripts/update_annulation_bdf.py --check    # contrôle seulement
  python scripts/update_annulation_bdf.py --temoin   # chaque garde vue mordre (mutation de la donnée qu'elle garde)
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRAIT = os.path.join(RACINE, "scripts", "sources_qe_maturite", "rendement_cycle.tsv")
OFFICIELLE = os.path.join(RACINE, "data", "dette_officielle.json")
SOURCES = os.path.join(RACINE, "scripts", "sources_annulation_bdf")
TRANSCRITES = os.path.join(SOURCES, "valeurs_transcrites.json")
DFR = os.path.join(SOURCES, "dfr_2022_2026.csv")
SORTIE = os.path.join(RACINE, "data", "annulation_bdf.json")
ANNEES = ("2023", "2024", "2025")


class Arret(Exception):
    pass


def fr(v: float, d: int = 1) -> str:
    return ("{:,.%df}" % d).format(v).replace(",", " ").replace(".", ",")


def en(v: float, d: int = 1) -> str:
    return ("{:,.%df}" % d).format(v)


def empreinte_ok(chemin: str) -> None:
    """Le fichier de l'extrait figé doit avoir l'empreinte inscrite dans le SHA256SUMS de son dossier."""
    dossier, nom = os.path.split(chemin)
    sommes = open(os.path.join(dossier, "SHA256SUMS"), encoding="utf-8").read()
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if h not in sommes or nom not in sommes:
        raise Arret("empreinte de %s absente de SHA256SUMS" % nom)


def lire() -> dict:
    empreinte_ok(EXTRAIT)
    cyc = {}
    with open(EXTRAIT, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["rendement_comptable_A71"] and r["C_Meur"]:
                cyc[r["annee"]] = dict(i=float(r["taux_reference_moyen"]), rt=float(r["rendement_comptable_A71"]),
                                       B=float(r["B_moyen_Md"]), C=float(r["C_Meur"]))
    off = json.load(open(OFFICIELLE, encoding="utf-8"))
    m = off["taux_long_terme_annuels"]["series"]["pct"]
    tri = off["dette_trimestrielle"]
    per = tri["derniere_periode"]
    tr = json.load(open(TRANSCRITES, encoding="utf-8"))
    empreinte_ok(DFR)
    # Taux de la facilité de dépôt : dernière observation de la série BCE archivée, et date du dernier changement.
    with open(DFR, encoding="utf-8") as f:
        obs = [(r["TIME_PERIOD"], float(r["OBS_VALUE"])) for r in csv.DictReader(f) if r.get("OBS_VALUE")]
    obs.sort()
    depuis = obs[-1][0]
    for d, v in reversed(obs):
        if v != obs[-1][1]:
            break
        depuis = d
    tr["taux_depot"] = dict(valeur_pct=obs[-1][1], au=obs[-1][0], depuis=depuis)
    # Moyennes annuelles du taux de dépôt (série quotidienne, tous les jours calendaires). C'est le taux qui rémunère
    # les réserves placées à la facilité de dépôt ; le « taux de référence » de l'extrait n'est le taux de dépôt que
    # depuis 2025 (décision (UE) 2024/2939) : avant, c'était le taux des opérations principales de refinancement
    # (contrôle du rendu, 09/11/2026 : les pertes de 2023 et 2024 étaient surestimées).
    dfr_moy = {}
    for a in {d[:4] for d, _ in obs}:
        v = [x for d, x in obs if d.startswith(a)]
        if len(v) >= 365:
            dfr_moy[a] = sum(v) / len(v)
    # Montants transcrits : présents tels quels dans le texte du communiqué archivé (contrôle local ; sans PyMuPDF,
    # l'empreinte du PDF suffit, le texte ayant été lu le jour de la transcription).
    for cle in ("encours_recent", "encours_fin_annee"):
        pdf = os.path.join(SOURCES, tr[cle]["fichier"])
        empreinte_ok(pdf)
        try:
            import fitz  # noqa: PLC0415
            texte = " ".join(p.get_text() for p in fitz.open(pdf)).replace(" ", " ").replace(" ", " ")
            if tr[cle]["texte_source"] not in texte:
                raise Arret("%s : « %s » absent du communiqué archivé" % (cle, tr[cle]["texte_source"]))
        except ImportError:
            pass
    return dict(cyc=cyc, m={a: float(m[a]) for a in m}, per=per, dette=float(tri["series"]["mdeur"][per]),
                ratio=float(tri["series"]["pct_pib"][per]), tr=tr, dfr_moy=dfr_moy)


def calculer(D: dict) -> dict:
    cyc, m, tr = D["cyc"], D["m"], D["tr"]
    for a in ANNEES:
        if a not in cyc or a not in m or a not in D["dfr_moy"]:
            raise Arret("année %s absente de l'extrait, des taux à dix ans ou du taux de dépôt" % a)
    # Témoin croisé : en 2025, le taux de référence de l'extrait EST le taux de dépôt ; les deux sources concordent.
    if abs(D["dfr_moy"]["2025"] - cyc["2025"]["i"]) > 0.01:
        raise Arret("témoin : taux de dépôt moyen 2025 (BCE) ≠ taux de référence 2025 (extrait)")
    E = tr["encours_recent"]["valeur_mdeur"]
    E0 = tr["encours_fin_annee"]["valeur_mdeur"]
    pib = D["dette"] / D["ratio"] * 100            # PIB implicite du dernier ratio publié (INSEE)
    R = dict(E=E, E0=E0, pts=E / pib * 100, part=E / D["dette"] * 100, dfr=tr["taux_depot"]["valeur_pct"])
    for a in ANNEES:
        c = cyc[a]
        R["d" + a], R["m" + a], R["rt" + a] = D["dfr_moy"][a], m[a], c["rt"]
        R["ecart" + a] = m[a] - R["d" + a]                   # points : marché à dix ans moins taux de dépôt moyen
        # = Md€ par an pour 100 Md€ refinancés ; plafond si tout l'encours récent l'était la même année :
        R["flux" + a] = R["ecart" + a] / 100 * E
    R["prod25"] = E * cyc["2025"]["rt"] / 100                # produit comptable estimé des titres, Md€ par an
    # Témoin comptable : l'écart de portage publié C = (r_t - i) x B, recalculé.
    for a, c in cyc.items():
        if abs((c["rt"] - c["i"]) / 100 * c["B"] * 1000 - c["C"]) > max(30, 0.02 * abs(c["C"])):
            raise Arret("témoin : C recalculé ≠ C publié en %s" % a)
    gardes(R)
    return R


def gardes(R: dict) -> None:
    """Chaque condition porte une phrase de la section."""
    G = [
        ("« en baisse au fil des échéances » : encours récent < encours de fin d'année", R["E"] < R["E0"]),
        ("« en 2025, un gain » : taux à dix ans 2025 > taux de dépôt moyen 2025", R["ecart2025"] > 0),
        ("« en 2023 et en 2024, l'inverse » : taux à dix ans < taux de dépôt moyen ces deux années", R["ecart2023"] < 0 and R["ecart2024"] < 0),
        ("« un rendement comptable inférieur au taux de marché » : rt2025 < m2025", R["rt2025"] < R["m2025"]),
        ("« environ » un point de PIB arrondi : 5 < pts < 30", 5 < R["pts"] < 30),
        ("taux de dépôt transcrit plausible (−1 à 6 %)", -1 <= R["dfr"] <= 6),
    ]
    rates = [lib for lib, ok in G if not ok]
    if rates:
        raise Arret("garde(s) : " + " ; ".join(rates))


MOIS = {"fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
                "décembre"],
        "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]}


def date_txt(iso: str, lang: str) -> str:
    a, m, j = iso.split("-")
    return "%d %s %s" % (int(j), MOIS[lang][int(m) - 1], a)


def affichage(R: dict, tr: dict) -> tuple[dict, dict]:
    A, B = {}, {}
    for f, d, cible in ((fr, "fr", A), (en, "en", B)):
        cible.update(
            e=f(R["E"], 0), e0=f(R["E0"], 0), pts=f(R["pts"], 0), part=f(R["part"], 0), dfr=f(R["dfr"], 2),
            prod25=f(R["prod25"], 0), rt25=f(R["rt2025"], 2),
            date_e=tr["encours_recent"]["date_" + d], date_e0=tr["encours_fin_annee"]["date_" + d],
            date_dfr=date_txt(tr["taux_depot"]["depuis"], d), partage=f(tr["partage_risques"]["valeur_pct"], 0),
            div_de=str(tr["sans_dividende"]["de"]), div_a=str(tr["sans_dividende"]["a"]))
        for a in ANNEES:
            cible["d" + a[2:]] = f(R["d" + a], 2)
            cible["e100_" + a[2:]] = f(abs(R["ecart" + a]), 1)
            # Accord de « milliard » sur la valeur AFFICHÉE (français : singulier sous 2 ; anglais : invariable).
            v = round(abs(R["ecart" + a]), 1)
            cible["u100_" + a[2:]] = ("milliard" if v < 2 else "milliards") if d == "fr" else "billion"
            cible["m" + a[2:]] = f(R["m" + a], 2)
            cible["flux" + a[2:]] = f(abs(R["flux" + a]), 1)
    return A, B


def main() -> int:
    arg = sys.argv[1:]
    try:
        D = lire()
        if "--temoin" in arg:
            return temoin(D)
        R = calculer(D)
    except Arret as x:
        print("ECHEC : %s. Aucun fichier ecrit." % x)
        return 1
    A, B = affichage(R, D["tr"])
    sortie = {"_licence": "CC BY 4.0, Stéphane Lalut ; sources : Banque de France, BCE, Eurostat, INSEE.",
              "releve_le": D["tr"]["verifie_le"], "periode_dette": D["per"],
              "valeurs": {k: round(v, 6) for k, v in R.items()}, "affichage": A, "affichage_en": B}
    print("Encours %.0f Md€ = %.1f pts de PIB ; 2025 : m %.2f, d %.2f, flux %+.1f Md€/an ; 2023 %+.1f ; 2024 %+.1f"
          % (R["E"], R["pts"], R["m2025"], R["d2025"], R["flux2025"], R["flux2023"], R["flux2024"]))
    if "--check" in arg:
        print("--check : gardes passees, rien ecrit.")
        return 0
    ancien = json.load(open(SORTIE, encoding="utf-8")) if os.path.exists(SORTIE) else None
    if ancien and {k: ancien.get(k) for k in ("valeurs", "affichage", "affichage_en")} == \
            {k: sortie[k] for k in ("valeurs", "affichage", "affichage_en")}:
        print("Donnees identiques : rien ecrit.")
        return 0
    with open(SORTIE, "w", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print("Ecrit : data/annulation_bdf.json")
    return 0


def temoin(D: dict) -> int:
    """Chaque mutation doit faire échouer une garde ou le témoin comptable ; le cas réel doit passer."""
    calculer(copy.deepcopy(D))
    mutations = {
        "taux de dépôt 2025 différent du taux de référence de l'extrait": lambda X: X["dfr_moy"].update({"2025": 3.0}),
        "encours récent supérieur à la fin d'année": lambda X: X["tr"]["encours_recent"].update(valeur_mdeur=600.0),
        "taux à dix ans 2025 sous le taux de référence": lambda X: X["m"].update({"2025": 1.0}),
        "taux à dix ans 2023 au-dessus du taux de référence": lambda X: X["m"].update({"2023": 5.0}),
        "écart de portage publié faussé": lambda X: X["cyc"]["2024"].update(C=-1000.0),
        "taux de dépôt aberrant": lambda X: X["tr"]["taux_depot"].update(valeur_pct=25.0),
    }
    rates = []
    for nom, mut in mutations.items():
        X = copy.deepcopy(D)
        mut(X)
        try:
            calculer(X)
            rates.append(nom)
        except Arret:
            pass
    if rates:
        print("TEMOIN : mutation(s) non detectee(s) : %s" % ", ".join(rates))
        return 1
    print("Temoin : %d mutations, toutes arretees ; le cas reel passe. OK" % len(mutations))
    return 0


if __name__ == "__main__":
    sys.exit(main())
