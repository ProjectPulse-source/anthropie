# -*- coding: utf-8 -*-
"""moteur_dette_futurs.py -- moteur de projection du volet « Quels futurs ? » (module, sans effet de bord hors lecture).

Code repris À L'IDENTIQUE, pour la mécanique, de D:\PRO\06_PROMOTION\RECHERCHE_QUELS_FUTURS_DETTE_2026-11-09\test_decisif\
moteur_a22.py (09/11/2026), où il a été testé : protocole PROTOCOLE_MOTEUR_A22.md et PROTOCOLE_ETAPE2.md écrits avant
le calcul, résultats RESULTATS_MOTEUR_A22.md et RESULTATS_ETAPE2.md. Seuls changent ici la lecture de la pièce (la fiche
France du DSM 2025 archivée pour le volet « générations futures », une pièce pour deux générateurs) et l'absence de
programme de test (les témoins sont rejoués par update_dette_futurs.py, à chaque exécution).

d_t = d_{t-1}(1+i_t)/(1+g_t) - sp_t + sfa_t, calibré sur la SEULE référence à politique inchangée de la Commission ;
passage des taux de marché au taux implicite selon l'annexe A2.2 (part à court terme, générations à long terme) ;
choc de solde structurel : multiplicateur 0,6, écart refermé en trois ans, solde effectif = structurel + eps x écart.
Un choc de taux ou de solde se donne ANNÉE PAR ANNÉE (dict année -> valeur) : une seule année = un choc d'un an.
"""
import csv, hashlib, sys
from pathlib import Path
import openpyxl

ICI = Path(__file__).resolve().parent
F = ICI / "sources_generations" / "dsm2025_country_fiches.xlsx"
AMECO = ICI / "sources_dette" / "ameco_ublgbps_2026-06-02.csv"
_sums = {}
for _l in (ICI / "sources_generations" / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
    if _l.strip():
        _h, _n = _l.split(None, 1)
        _sums[_n.strip().lstrip("*")] = _h
if hashlib.sha256(F.read_bytes()).hexdigest() != _sums.get(F.name):
    raise SystemExit("piece DSM : empreinte differente de SHA256SUMS")

AN = list(range(2024, 2037))
rows = list(openpyxl.load_workbook(F, read_only=True, data_only=True)["FR"].iter_rows(values_only=True))


def bloc(titre):
    """Lignes (libellé -> 13 valeurs) du bloc d'hypothèses dont l'en-tête est `titre` (lignes 150-180 de la fiche)."""
    i0 = next(i for i, r in enumerate(rows) if len(r) > 3 and r[3] == titre)
    out = {}
    for r in rows[i0 + 1:i0 + 12]:
        if len(r) < 20 or not isinstance(r[3], str) or r[3][:1].isdigit():
            break
        out[r[3]] = [float(x) for x in r[7:20]]
    if not out:
        raise SystemExit("bloc vide : %s" % titre)
    return out


def ligne(lib, i_max=80):
    for r in rows[:i_max]:
        if len(r) > 19 and r[3] == lib:
            return [float(x) for x in r[7:20]]
    raise SystemExit("libelle introuvable : %s" % lib)


B = bloc("1. Baseline")
d0, pb0, spb0 = B["Gross public debt"], B["Primary balance"], B["Structural primary balance (before CoA)"]
ga, gp, pi, i0 = B["Real GDP growth"], B["Potential GDP growth"], B["Inflation rate"], B["Implicit interest rate (nominal)"]
gfn = B["Gross financing needs"]
cyc = ligne("(1.2) Cyclical component")
sfa = ligne("(3) Stock-flow adjustments")
inte = ligne("(2.1) Interest expenditure")
alpha = next(float(r[27]) for r in rows if len(r) > 27 and r[22] == "short-term debt (< 1 year)") / 100
g0 = [(1 + ga[k] / 100) * (1 + pi[k] / 100) - 1 for k in range(13)]

# Écart de production de la référence (cumul ga - gp, nul en 2030 : fermeture déclarée), puis ε = cyc / écart
gap = [0.0] * 13
k30 = AN.index(2030)
for k in range(k30 - 1, -1, -1):           # remonte depuis 2030 où l'écart est nul
    gap[k] = gap[k + 1] - (ga[k + 1] - gp[k + 1])
eps_obs = [cyc[k] / gap[k] for k in range(13) if abs(gap[k]) > 0.05]
EPS = sum(eps_obs) / len(eps_obs)

# Part de la dette à long terme émise dans l'année (échéances + emprunt net), référence
beta = [None]
for k in range(1, 13):
    # Tout en % du PIB de l'année t : la dette de début d'année se ramène au PIB de t par 1/(1+g).
    # Correction du 09/11 (erreur d'implémentation, définition du protocole inchangée) : l'emprunt net est
    # l'emprunt NOMINAL de l'année rapporté au PIB, d_t - d_{t-1}/(1+g_t), non la variation du ratio.
    d_debut = d0[k - 1] / (1 + g0[k])
    lt_echu = gfn[k] - (-pb0[k]) - inte[k] - sfa[k] - alpha * d_debut
    emprunt = max(0.0, d0[k] - d_debut)
    beta.append(min(1.0, max(0.0, (lt_echu + emprunt) / ((1 - alpha) * d_debut))))

CAL = {"alpha": alpha, "epsilon": EPS, "epsilon_obs": eps_obs, "beta": beta[1:],
       "controle_g": max(abs(g0[k] * 100 - (-(ligne("(2.2) Growth effect (real)")[k] + ligne("(2.3) Inflation effect")[k])
                                             / d0[k - 1] / (1 + (-(ligne("(2.2) Growth effect (real)")[k] + ligne("(2.3) Inflation effect")[k]) / d0[k - 1]))) * 100)
                         for k in range(1, 13))}


def projeter(dspb=None, dmarche=None, dg_perm=None, mult=0.6, ferme=True, eps=None, passage=True):
    """Écarts à la référence. dspb, dmarche, dg_perm : dict année -> pt (solde structurel, taux de marché, croissance
    potentielle). Rend dict année -> (dette, taux implicite, croissance réelle, solde effectif)."""
    dspb, dmarche, dg_perm = dspb or {}, dmarche or {}, dg_perm or {}
    eps = EPS if eps is None else eps
    d, dILT, out = d0[0], 0.0, {}
    cohortes, prev_dspb = [], 0.0
    for k in range(1, 13):
        a = AN[k]
        s = dspb.get(a, prev_dspb if a > min(dspb, default=9999) else 0.0)
        impulsion = -(s - prev_dspb) * mult            # baisse du solde = relance : croissance plus forte
        prev_dspb = s
        if impulsion:
            cohortes.append([a, impulsion])
        dga = 0.0
        for c in cohortes:
            age = a - c[0]
            if age == 0:
                dga += c[1]
            elif ferme and 1 <= age <= 3:
                dga -= c[1] / 3
        dga += dg_perm.get(a, 0.0)
        gap_dev = sum(c[1] * (1 - (min(a - c[0], 3) / 3 if ferme else 0)) for c in cohortes if a >= c[0])
        dm = dmarche.get(a, 0.0) / 100
        b = 1.0 if not passage else beta[k]
        surplus = max(0.0, (d - d0[k - 1]) / ((1 - alpha) * d)) if d > 0 else 0.0
        b_eff = min(1.0, b + surplus)
        dILT = b_eff * dm + (1 - b_eff) * dILT
        di = alpha * dm + (1 - alpha) * dILT
        it = i0[k] / 100 + di
        g = (1 + (ga[k] + dga) / 100) * (1 + pi[k] / 100) - 1
        pbe = pb0[k] + s + eps * gap_dev
        d = d * (1 + it) / (1 + g) - pbe + sfa[k]
        out[a] = (d, it * 100, ga[k] + dga, pbe)
    return out




def bloc_variante(nom):
    """Variante publiée par la Commission (témoin, jamais lue par projeter) : libellé -> {année: valeur}."""
    return {lib: dict(zip(AN, v)) for lib, v in bloc(nom).items()}
