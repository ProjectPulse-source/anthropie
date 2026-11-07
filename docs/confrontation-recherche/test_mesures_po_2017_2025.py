"""Test de l'objection Zemmour (20/10/2026) : le recul des recettes corrigees du cycle entre 2015-2019 et 2022-2025
tient-il aux mesures nouvelles en prelevements obligatoires (PO), a leur masquage par l'elasticite, ou a autre chose ?

Identite (Cour des comptes) : PO_t = PO_{t-1} + evolution spontanee_t + mesures nouvelles_t, d'ou, en taux de PO
(tau = PO/PIB) : tau_t - tau_{t-1} = tau_{t-1} * (s_t - g_t) / (1 + g_t) + MN_t / PIB_t.
  - effet des mesures : MN_t / PIB_t (cumul = cout persistant en part de PIB, une mesure dont l'assiette suit le PIB) ;
  - effet d'elasticite : tau_{t-1} * (s_t - g_t) / (1 + g_t), s croissance spontanee, g croissance du PIB en valeur.
Valeurs TRANSCRITES des rapports « La situation et les perspectives des finances publiques » de la Cour (dernier
millesime disponible pour chaque annee, page citee) ; PIB : Eurostat gov_10dd_edpt1 B1GQ (notification d'octobre 2026).
Pieces : D:\PRO\06_PROMOTION\RECHERCHE_SOLUTIONS_DETTE_2026-10-02\pieces_lues\cc_rspfp20XX.pdf (SHA-256 dans la note).
"""
import csv, os

PIB = {2015: 2201.4, 2016: 2231.8, 2017: 2291.7, 2018: 2355.4, 2019: 2432.2, 2020: 2318.3, 2021: 2508.1,
       2022: 2654.0, 2023: 2833.8, 2024: 2935.2, 2025: 2991.1}  # Md EUR, Eurostat, releve le 06/11/2026
# Mesures nouvelles hors effet temporaire de la transformation du CICE, Md EUR
MN = {2016: -4.0,   # ed. 2017 p. 39 T6
      2018: -9.4,   # ed. 2022 p. 25 T1 (dont -4,8 contrecoup de la surtaxe d'IS de 2017)
      2019: -9.1,   # ed. 2022 p. 25 T1
      2020: -9.2,   # ed. 2022 p. 36 T7
      2021: -15.3,  # ed. 2022 p. 36 T7
      2022: -9.4,   # ed. 2023 p. 30 T1
      2023: -10.7,  # ed. 2024 T1, « mesures ayant un impact » sur le deficit
      2024: 2.2,    # ed. 2026 p. 27 T1 : 3,2 au total, dont CICE +1,0 (ci-dessous) et fonds de resolution unique -3,9
                    # (PO verse a l'UE, neutre sur le solde public ; mesures affectant le solde : 7,1)
      2025: 23.0}   # ed. 2026 p. 28
MN_PT = {t: v / PIB[t] * 100 for t, v in MN.items()}
MN_PT[2017] = 0.2   # ed. 2018 p. 29, en points de PIB, surtaxe exceptionnelle d'IS comprise
CICE = {2019: -20.1, 2020: 14.4, 2021: 0.5, 2022: 1.7, 2023: 4.4, 2024: 1.0}  # ed. 2022 T1 et T7, 2023 T1 (note), 2024 T1, 2025 p. 31 note 21
CICE_PT = {t: v / PIB[t] * 100 for t, v in CICE.items()}
# (croissance spontanee %, croissance du PIB en valeur %), dernier millesime
SG = {2016: (2.0, 1.6), 2017: (3.9, 2.8), 2018: (2.9, 2.9), 2019: (3.4, 3.1), 2020: (-4.5, -5.2),  # ed. 2022 p. 33 T5
      2021: (9.6, 8.0),            # ed. 2023 p. 27
      2022: (1.4 * 5.8, 5.8),      # ed. 2024 (elasticite 1,4, base 2020) ; PIB : ed. 2025 T12
      2023: (2.8, 6.5),  # ed. 2025 p. 29 T8
      2024: (2.3, 3.6),  # ed. 2026 p. 27 T1
      2025: (2.2, 1.9)}            # ed. 2026 p. 27 T1
# Taux de PO, serie unique : Insee, comptes nationaux annuels base 2020 (hors cotisations imputees et credits d'impot,
# PO verses a l'UE compris) ; econ-fin-pub-prelev-oblig.xlsx, insee.fr/fr/statistiques/2381412, telecharge le 06/11/2026,
# archive pieces_lues/insee_taux_po_1959_2025.xlsx, SHA-256 1934fdb263eadb55146d066cd9da2949dd74231c6ede28145e812f0f2f1b7020.
PO_INSEE = {2014: 44.626, 2015: 44.497, 2016: 44.570, 2017: 45.300, 2018: 44.886, 2019: 43.958, 2020: 44.293,
            2021: 44.195, 2022: 45.044, 2023: 43.154, 2024: 42.723, 2025: 43.632}
PO_UE = {2015: 0.139, 2016: 0.162, 2017: 0.177, 2018: 0.195, 2019: 0.191, 2020: 0.218, 2021: 0.218, 2022: 0.289,
         2023: 0.232, 2024: 0.089, 2025: 0.096}  # dont au profit de l'Union europeenne, meme fichier
E = {t: PO_INSEE[t - 1] / 100 * (s - g) / (100 + g) * 100 for t, (s, g) in SG.items()}
ANS = range(2015, 2026)


def cumul(x):
    c, o = 0.0, {}
    for t in ANS:
        c += x.get(t, 0.0)
        o[t] = c
    return o


def moy(d, a, b):
    return sum(d[t] for t in range(a, b + 1)) / (b - a + 1)


S, SC, SE = cumul(MN_PT), cumul(CICE_PT), cumul(E)
ici = os.path.dirname(os.path.abspath(__file__))
R = {}
with open(os.path.join(ici, "..", "..", "static", "dette_dynamique.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["commission_recettes_corrigees_pct_pib_potentiel"]:
            R[int(r["annee"])] = float(r["commission_recettes_corrigees_pct_pib_potentiel"])

print("annee  MN(pt)  cumMN  elast(pt) cumE  CICE(pt)")
for t in ANS:
    print("%d  %6.2f %6.2f  %6.2f  %6.2f  %6.2f" % (t, MN_PT.get(t, 0), S[t], E.get(t, 0), SE[t], CICE_PT.get(t, 0)))
print("\nTemoin Cour (ed. 2023 p. 31), 2017->2022 : mesures -2,0 / elasticite +2,3 ; calcul : %.2f / %.2f"
      % (S[2022] - S[2017], SE[2022] - SE[2017]))
print("Somme Md EUR 2018-2023 hors CICE : %.1f (Cour : 62 en 2023, ed. 2024 ; « pres de 60 », ed. 2025)"
      % sum(MN[t] for t in range(2018, 2024)))
print("\nMoyennes 2015-2019 -> 2022-2025 (points) :")
for nom, d in (("mesures hors CICE", S), ("CICE", SC), ("elasticite", SE)):
    print("  %-18s %6.2f" % (nom, moy(d, 2022, 2025) - moy(d, 2015, 2019)))
tot = {t: S[t] + SC[t] + SE[t] for t in ANS}
dpo = moy(tot, 2022, 2025) - moy(tot, 2015, 2019)
drec = moy(R, 2022, 2025) - moy(R, 2015, 2019)
print("  total identite PO  %6.2f" % dpo)
print("  recettes corrigees du cycle (Commission, AMECO) %6.2f ; reste non explique %6.2f" % (drec, drec - dpo))


# --- Temoin de bouclage : observe = mesures + CICE + elasticite + ecart, annee par annee, en base 2020
print("\nBouclage annuel sur le taux de PO de l'Insee (points)")
print("annee  observe  MN    CICE  elast  ecart")
ec = {2015: 0.0}
for t in range(2016, 2026):
    obs = PO_INSEE[t] - PO_INSEE[t - 1]
    ec[t] = obs - MN_PT.get(t, 0) - CICE_PT.get(t, 0) - E[t]
    print("%d  %6.2f %6.2f %6.2f %6.2f %6.2f" % (t, obs, MN_PT.get(t, 0), CICE_PT.get(t, 0), E[t], ec[t]))
for a, b in ((2017, 2022), (2022, 2025)):
    print("  %d->%d : observe %.2f, calcul %.2f, ecart %.2f" % (
        a, b, PO_INSEE[b] - PO_INSEE[a], tot[b] - tot[a], sum(ec[t] for t in range(a + 1, b + 1))))
dpo_obs = moy(PO_INSEE, 2022, 2025) - moy(PO_INSEE, 2015, 2019)
print("\nEntre les fenetres : taux de PO observe %.2f (dont part UE %.2f) ; identite %.2f ; ecart de bouclage %.2f"
      % (dpo_obs, moy(PO_UE, 2022, 2025) - moy(PO_UE, 2015, 2019), dpo, dpo_obs - dpo))
print("Recettes corrigees moins PO observes (hors PO, correction du cycle, PIB potentiel) : %.2f" % (drec - dpo_obs))
