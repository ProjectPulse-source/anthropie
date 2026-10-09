---
title: "Did inflation really ease France's debt burden?"
url: /en/inflation-and-french-public-debt/
description: "The 2021–2023 inflation surprise reduced the real value of payments promised on France's end-2020 fixed-rate marketable government debt by about €{infl.t}bn in 2020 euros. The erosion is measurable; an equally precise net fiscal gain is not. Computed line by line on the AFT's outstanding debt and the monthly HICP."
chapo: "Yes, for legacy nominal liabilities. Relative to the inflation path expected in early 2021, the 2021–2023 inflation surprise reduced the real value of payments promised on France's fixed-rate marketable government debt outstanding at end-2020 by about €{infl.t}bn, measured in 2020 French consumer-price euros. But that is neither €{infl.t}bn in cash for the government nor an identifiable net fiscal gain, and it does not tell us who ultimately bore the loss. This study measures the nominal-debt channel. It does not measure the total fiscal effect of inflation on the public finances."
date: 2026-10-07
lastmod: 2026-10-08
og_title: "Did inflation really ease France's debt burden? — S. Lalut"
og_image: "images/og-dette-inflation-en.jpg"
og_image_alt: "Share card: “Inflation eroded legacy debt” — cumulative real-value erosion of the payments promised on France's end-2020 fixed-rate marketable government debt, as payments fall due, and the range of forecasts published in early 2021."
# English mirror of /inflation-et-dette-publique/ (07/10/2026). Same calculation, same tokens (affichage_en block).
# English lexicon locked on 08/10/2026 (external language review, arbitration Wolf-07): marketable (not negotiable) debt;
# government / central-government (not State); legacy debt; real value; €Xbn in 2020 euros; en dash in year ranges.
donnees: [dette_inflation]
dataset:
  jeu: "dette_inflation"
  nom: "The 2021–2023 inflation surprise and France's end-2020 fixed-rate marketable government debt: real-value erosion of promised payments, timing, sensitivities"
  description: "Author's calculation: real-value erosion, in 2020 euros at French consumer prices, of the coupons and principal promised on France's fixed-rate central-government marketable debt at 31/12/2020 (OATs line by line, and BTFs), when realised 2021–2023 inflation (monthly HICP) replaces the inflation expected in early 2021; cumulative by year of payment up to {infl.fin}, forecasts published in early 2021, market breakevens, inflation-linked bonds, simplified consolidation with the Banque de France; for central-bank purchases, monthly interest-rate exposure and refixing period since 2015, yield gap 2016–2025 and comparison with Germany, Italy and Spain."
  couverture_temporelle: "2021/{infl.fin}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Cumulative real-value erosion of promised payments", unite: "billions of 2020 euros", description: "by year of payment, closed shock after 2023"}
    - {nom: "Total erosion by expectation used", unite: "billions of 2020 euros", description: "forecasts published in early 2021 and market breakevens, discounting from -1% to +1%"}
    - {nom: "Inflation-linked bonds: transfer the government forwent", unite: "billions of 2020 euros", description: "nominal fixed-rate counterfactual using breakevens of the same index and maturity"}
    - {nom: "First-year rise in the interest bill if the whole yield curve shifted up by one point (scenario)", unite: "billions of euros", description: "monthly since March 2015; central-government market debt alone, and government plus Banque de France"}
    - {nom: "Average refixing period of fixed-rate central-government debt", unite: "years", description: "monthly; unadjusted and adjusted for bonds held by the Banque de France"}
    - {nom: "Gap between the yield on public-sector bonds held by the Banque de France and the ECB reference rate", unite: "millions of euros", description: "annual 2016–2025, with published monetary-income sharing balances"}
  sources:
    - "https://www.aft.gouv.fr/en/publications/annual-reports"
    - "https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_midx/default/table?lang=en"
    - "https://www.ecb.europa.eu/stats/ecb_surveys/survey_of_professional_forecasters/html/index.en.html"
    - "https://webstat.banque-france.fr/en/"
    - "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016D0036(01)-20250101"
    - "https://data.ecb.europa.eu/"
  mots: ["public debt", "inflation", "French government bonds", "inflation-linked bonds", "inflation expectations", "Banque de France", "AFT", "HICP", "quantitative easing", "debt maturity", "average time to refixing"]
  fichiers: ["dette_inflation.csv", "dette_inflation.json"]
faq:
  - question: "Did inflation ease France's debt burden?"
    answer: "Yes, for legacy nominal liabilities. Relative to the inflation expected in early 2021, realised 2021–2023 inflation reduced the real value of payments promised on France's end-2020 fixed-rate marketable government debt by about €{infl.t}bn in 2020 euros, about {infl.pts_pib}% of 2020 GDP; depending on which forecast published in early 2021 is used, €{infl.a_bas}bn to €{infl.a_haut}bn. It is not a net fiscal gain: the data do not identify how much of the later rise in funding costs the episode caused."
  - question: "Did the ECB's bond purchases make France more sensitive to interest rates?"
    answer: "Yes, mainly in the short run. Had the whole yield curve shifted up permanently by one point at end-2022, the combined interest bill of the government and the Banque de France would have risen by €{infl.qe_sc1}bn in the first year, against €{infl.qe_sm1}bn for the government's market debt alone, {infl.qe_r1} times as much; over five years, only {infl.qe_r5} times. The reason: when the Eurosystem computes the income it pools, government bonds bought by the Banque de France are deemed to earn the ECB reference rate. This scenario measures an exposure: it is neither a forecast nor the cost of QE, since no one knows what rates would have been without the purchases."
  - question: "Why is this not a fiscal gain for the government?"
    answer: "Because the erosion falls on payments spread out until {infl.fin}: only a fifth had been paid by end-2023, about half will have been by {infl.demi}. Because the government then borrowed at higher rates, and no one can say how much of that rise the episode caused. And because inflation-linked bonds, the Banque de France and the unit of account change the reading: measured in units of domestic output rather than in consumer purchasing power, the same erosion is smaller."
  - question: "Who ultimately bore the real-value loss?"
    answer: "We know which sectors held the bonds; we cannot infer from that who ultimately bore the loss. At end-2020, half of France's marketable government debt was held by non-residents and nearly a quarter by the Banque de France. But the direct holder is not necessarily the one who ultimately loses: insurers, banks and funds have nominal liabilities of their own, and bonds change hands. The page gives a mechanical allocation by end-2020 holdings, which does not identify the ultimate incidence."
ressource:
  bloc: "dette"
  rang: 45
  nature: "Author's calculation on official data (AFT, Eurostat, ECB, Banque de France)"
  prolongement: true
dossier_dette: prolongement
dossier_dette_titre: "Did inflation ease the debt burden?"
dossier_dette_role: "2021–2023, government debt"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Computed: {{< infl-val "date_donnees" >}}</span> Central-government marketable debt at 31 December 2020 (AFT, line by line); monthly HICP for France, 2020–2023 (Eurostat); forecasts published between November 2020 and February 2021. Download: <a href="/dette_inflation.csv">CSV</a> · <a href="/dette_inflation.json">JSON</a> · <a href="#sources">method</a></p>

## How much did inflation erode the real value of legacy debt? {#erosion}

<figure class="figure-ciseau">
  <img src="/img/dette-inflation-calendrier-en.svg" alt="Cumulative curve, from 2021 to {{< infl-val "fin" >}}, of the real-value erosion of the payments promised on France's end-2020 fixed-rate marketable government debt, in 2020 euros: €{{< infl-val "cum23" >}}bn by end-2023, {{< infl-val "cum27" >}} by end-{{< infl-val "demi" >}}, {{< infl-val "t_exact" >}} in total; a band shows the range of forecasts published in early 2021, €{{< infl-val "a_bas" >}}bn to €{{< infl-val "a_haut" >}}bn." width="720" height="344" loading="lazy">
  <figcaption>Cumulative real-value erosion of the payments promised on France's end-2020 fixed-rate marketable government debt, by year of payment, in billions of 2020 euros at consumer prices (author's calculation; AFT, Eurostat, ECB).</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** In our counterfactual, relative to the inflation expected in early 2021, realised 2021–2023 inflation reduces the cumulative real value of the payments promised on the fixed-rate marketable debt outstanding at end-2020 by about €{{< infl-val "t" >}}bn in 2020 euros, about {{< infl-val "pts_pib" >}}% of 2020 GDP; depending on which forecast published in early 2021 is used, the estimate runs from €{{< infl-val "a_bas" >}}bn to €{{< infl-val "a_haut" >}}bn. On that debt, about half of the erosion materialises in payments made by {{< infl-val "demi" >}}.

</div>

At end-2020 the French government owed coupons and redemptions fixed in euros, line by line, until {{< infl-val "fin" >}}. When prices rise more than expected, each of those euros buys less: the creditor receives what was promised, but what was promised is worth less. The measure compares two worlds. In the first, inflation is what the professional forecasters surveyed by the ECB expected in early 2021. In the second, it is realised inflation, month by month, up to December 2023; after that prices grow again at the expected pace, so the price-level gap reached at end-2023, {{< infl-val "gap23" >}}%, remains. Each payment is deflated on its date by both price levels: the difference between the two values, summed, gives the erosion.

Amounts are in 2020 euros at French consumer prices. That unit answers a precise question: what these payments represent for a household spending in France. French consumer prices are not the relevant numeraire for every creditor, nor do they directly measure the government's fiscal capacity: the next section gives the same erosion in another unit.

In this counterfactual, where the price-level gap created in 2021–2023 persists, the fall in the real value of nominal flows already contracted is not undone by a later rise in interest rates, which applies to new financing. But most of that erosion had not yet materialised in cash flows: by end-2023 only {{< infl-val "part23" >}}% had been realised in actual payments, and about {{< infl-val "part27" >}}% will have been by end-{{< infl-val "demi" >}}. The maturity of the debt largely sets the timing; its effect on any fiscal balance depends on the measure used.

## Why this is not a net fiscal gain {#gain-net}

The available data do not identify how much of the later rise in funding costs was caused by the inflation episode itself. The government refinanced its maturing debt at higher rates from 2022 onwards; part of that rise reflects revised inflation expectations, part reflects real rates and risk premia with causes of their own. No net fiscal gain attributable to the 2021–2023 surprise can therefore be identified.

**The unit of account changes the amount.** Measured in units of domestic output (the GDP deflator) rather than in consumer purchasing power, the same erosion is of the order of €{{< infl-val "defl_bas" >}}bn to €{{< infl-val "defl_haut" >}}bn, against €{{< infl-val "t_annuel" >}}bn at consumer prices in the same calculation on annual averages. The two measures answer different questions; neither is a net fiscal gain for the government. The gap between the two price indices is measured here, not explained.

**Inflation-linked bonds worked the other way.** At end-2020, {{< infl-val "idx_n" >}} inflation-linked bonds, worth €{{< infl-val "idx_encours" >}}bn, escaped the erosion. Had otherwise comparable bonds been issued as nominal fixed-rate debt, the erosion would have been about €{{< infl-val "idx" >}}bn larger. In the central-government budget, their indexation charge peaked at €{{< infl-val "charge22" >}}bn (current euros) in 2022 (AFT).

<details class="repli"><summary>Simplified consolidation with the Banque de France: the erosion stays almost whole during the episode, then the consolidated advantage shrinks</summary>

At end-2020 the Banque de France held {{< infl-val "s_bdf" >}}% of the government's marketable debt, bought by creating bank reserves. In a balance sheet that combines the government and its central bank, those bonds cancel out, and for that share the relevant consolidated liability is instead the banking system's reserve claim on the central bank, remunerated at the deposit facility rate. The identity reads:

consolidated erosion at date *t* = erosion × (1 − share held by the Banque de France) + the sum, up to *t*, of the real losses of reserve holders,

where one year's real loss equals the stock of reserves at the start of the year, in 2020 euros, times the gap between the expected real return (a −0.5% deposit rate and expected inflation) and the real return obtained (deposit rate and realised inflation).

Because the deposit rate stayed at −0.5% until July 2022 while prices rose, reserve holders earned negative real returns, as holders of nominal fixed-rate claims did: consolidated, the erosion is still about €{{< infl-val "cons23" >}}bn at end-2023. The sign then reverses: in 2024 and 2025 reserves were paid above inflation, and the consolidated erosion falls to about €{{< infl-val "cons25" >}}bn at end-2025. This is a simplified model, not a statistical consolidation: the Banque de France is outside general government, and its losses reach the government through its dividends and taxes, with a lag.

</details>

## Did the ECB's bond purchases make the debt more sensitive to interest rates? {#achats-banque-centrale}

<figure class="figure-ciseau">
  <img src="/img/dette-inflation-achats-en.svg" alt="Two monthly lines, from March 2015 to {{< infl-val "qe_dern" >}}, of the first-year rise in the interest bill if the whole yield curve shifted up permanently by one point: for the government and the Banque de France taken together, €{{< infl-val "qe_sc1" >}}bn at end-2022 and {{< infl-val "qe_sc1_d" >}} in {{< infl-val "qe_dern" >}}; for the government's market debt alone, {{< infl-val "qe_sm1" >}} at end-2022 and {{< infl-val "qe_sm1_d" >}} in {{< infl-val "qe_dern" >}}." width="720" height="344" loading="lazy">
  <figcaption>First-year rise in the interest bill if the whole yield curve shifted up permanently by one point, at a constant stock of debt, in billions of euros: fixed-rate central-government debt alone, and the government and the Banque de France taken together (a scenario, not a forecast; author's calculation; AFT, Banque de France, ECB).</figcaption>
</figure>

Yes: mainly by bringing the exposure to interest rates forward. Had the whole yield curve, from the ECB reference rate to the longest maturities, shifted up permanently by one point at end-2022, the interest bill of the government and the Banque de France taken together, an analytical perimeter rather than a unit of the public accounts, would have risen by €{{< infl-val "qe_sc1" >}}bn in the first year ({{< infl-val "qe_sc1_pib" >}} percentage points of GDP), against €{{< infl-val "qe_sm1" >}}bn for market debt alone: {{< infl-val "qe_r1" >}} times as much. Over five years the ratio falls to {{< infl-val "qe_r5" >}} (€{{< infl-val "qe_sc5" >}}bn against €{{< infl-val "qe_sm5" >}}bn): central-bank purchases mainly brought the repricing forward in time. This scenario measures an exposure, it forecasts nothing: a rise in policy rates need not shift the whole curve.

The mechanism lies in Eurosystem rules. From 2015 to 2022, the Banque de France bought government bonds by creating bank reserves. When euro-area central banks compute the income they pool, those bonds are deemed to earn the ECB reference rate, whatever their coupon (Decision (EU) 2016/2248); that income is then shared out among them according to their share in the ECB's capital, which moves the result by only a few billion (see below). In the consolidated measure used here, the share held by the Banque de France is therefore treated as debt that reprices at once at the reference rate, in place of long-term fixed-rate debt. The mechanism is close to that of the simplified consolidation above, which works through the remuneration of reserves at the deposit rate; since 2025, that rate has also been the reference rate.

Meanwhile the Agence France Trésor lengthened its issuance: the average maturity of its issues rose from {{< infl-val "qe_em14" >}} years in 2014 to between {{< infl-val "qe_em_min" >}} and {{< infl-val "qe_em_max" >}} years in each year from 2016 to 2022, and the average refixing period of fixed-rate central-government debt from {{< infl-val "qe_atr15" >}} years in March 2015 to {{< infl-val "qe_atr22" >}} years at end-2022. Counting, by convention, bonds held by the Banque de France as repricing immediately, the adjusted measure stayed between {{< infl-val "qe_aj_min" >}} and {{< infl-val "qe_aj_max" >}} years over the same period. Since net purchases ended, the Banque de France has held a smaller share of that debt, {{< infl-val "qe_h_d" >}}% in {{< infl-val "qe_dern" >}} against {{< infl-val "qe_h22" >}}% at end-2022, at face value (the {{< infl-val "s_bdf" >}}% given above for end-2020 covered all marketable debt, at market value): the gap between the two lines is narrowing, without closing ({{< infl-val "qe_r_d" >}} times in {{< infl-val "qe_dern" >}}).

**The carry turns negative.** According to the Banque de France's accounts, its monetary-policy securities yielded {{< infl-val "qe_rdt_min" >}}% to {{< infl-val "qe_rdt_max" >}}% a year, while the ECB reference rate, close to zero until 2021, rose to about {{< infl-val "qe_tref_max" >}}% as an annual average. On the French public-sector securities held, the gap between that yield and that rate amounted to about +€{{< infl-val "qe_gain" >}}bn cumulatively from 2016 to 2022, then −€{{< infl-val "qe_cout" >}}bn from 2023 to 2025: a balance of −€{{< infl-val "qe_solde" >}}bn over the period observed, while the Banque de France still holds part of these securities. The sharing of monetary income among euro-area central banks moves it by a few billion, to between −€{{< infl-val "qe_net_haut" >}}bn and −€{{< infl-val "qe_net_bas" >}}bn. The yield used is that of the whole monetary-policy portfolio, corporate bonds included, which probably yield more than public-sector securities: for public-sector securities alone, the balance would probably be less favourable. This is neither government budget spending nor the cost of QE: the calculation keeps market rates as they were, and no one knows what they would have been without the purchases.

**What the Banque de France's accounts show.** The Banque de France, which carried out these purchases for the Eurosystem, sets its losses since 2023 against the profits it made and paid to the government before. Its accounts, which cover its whole balance sheet, bear this out: an ordinary result of €{{< infl-val "qe_bdf_ro_avant" >}}bn from 2015 to 2022, of which €{{< infl-val "qe_bdf_verse" >}}bn paid to the government in tax and dividends, then −€{{< infl-val "qe_bdf_ro_apres" >}}bn from 2023 to 2025. On the narrower perimeter of French public-sector securities alone, measured above, the carry does not balance over the period observed: −€{{< infl-val "qe_solde" >}}bn. Both findings are correct; they do not concern the same object.

**Elsewhere in the euro area.** The rule applies to every Eurosystem central bank. On a common basis published by the ECB, which covers all of general government and its loans, at year-end, the ratio of the consolidated first-year exposure to that of market debt ranged from {{< infl-val "qe_t4_2015_bas" >}} to {{< infl-val "qe_t4_2015_haut" >}} across countries in 2015; its peak ranges from {{< infl-val "qe_t4_bas" >}} to {{< infl-val "qe_t4_haut" >}} in Germany, Italy, Spain and France. For France this broader basis gives at most {{< infl-val "qe_t4_fr" >}}, against {{< infl-val "qe_r1" >}} at end-2022 in the measure focused on fixed-rate central-government debt: the two perimeters differ. Differences between countries reflect the structure of their market debt: they do not make a ranking.

## What moves the number {#sensibilite}

**The starting forecast.** Four inflation forecasts published between November 2020 and February 2021 give: €{{< infl-val "spf" >}}bn with the ECB Survey of Professional Forecasters (January 2021, euro area), {{< infl-val "bdf" >}} with the Banque de France projections (December 2020), {{< infl-val "ce_aut" >}} and {{< infl-val "ce_hiv" >}} with those of the European Commission (autumn 2020, winter 2021). The Commission published no 2023 horizon: its 2022 forecast, 1.5%, is carried over to 2023, its last published horizon. Beyond 2023, all of them return to the ECB survey's path, so only the years of the episode differ. The ECB survey is the reference because it is the only one of the four to cover the whole horizon of payments, beyond 2023 to the long term, and it fixes a single information date, January 2021, when the December 2020 price level is known; it covers the euro area, and the three forecasts specific to France bracket the result it gives.

**Inflation breakevens.** The yield gaps between nominal and inflation-linked bonds at 31 December 2020 (AFT) would give more: €{{< infl-val "b_fr" >}}bn with the French 10-year breakeven, {{< infl-val "b_eu" >}} with the euro-area one. They embed risk and liquidity premia, which then pulled them down: they serve only as a sensitivity here, not for the range.

**Discounting.** Amounts are summed undiscounted. Discounted at a real rate from −1% to +1%, they run from €{{< infl-val "a_tout_bas" >}}bn to €{{< infl-val "a_tout_haut" >}}bn across all the forecasts.

**The timing of prices.** The calculation follows the HICP month by month, on the date of each payment. On annual averages it gave €{{< infl-val "t_annuel" >}}bn: the difference mostly reflects the fact that the price-level gap that persists after the episode is the December 2023 one, larger than the gap in the 2023 average.

## What these data do not tell {#limites}

They do not measure the total fiscal effect of inflation: neither tax revenue swollen by prices, nor the indexation of pensions and benefits, nor support measures, nor the nominal assets held by government. They cover only central-government marketable debt, not the debt of social security or local government. They do not say who ultimately bore the loss. They do not allow any share of the subsequent rise in interest rates to be attributed to the episode. And they rest on a counterfactual: another starting expectation gives another number, within the range shown. For central-bank purchases they measure an exposure and a yield gap: not the causal cost of QE, nor what rates would have been without it, nor the income the Eurosystem earns on banknotes and unremunerated reserves, nor debt sustainability.

{{< confrontation-recherche verifie="2026-10-08" publie="oui" resume="the order of magnitude is recovered in Pallotti et al. once conventions are aligned, but the literature does not support interpreting it as a net fiscal gain; the effect of purchases on the refixing period is close to the one the OECD published" >}}
**Measured here.** The real-value erosion of the payments promised on France's end-2020 fixed-rate marketable government debt, at the pace at which the price gap actually built up, with its timing of realisation.

**Consistent with.** Pallotti, Paz-Pardo, Slacalek, Tristani and Violante measure a much larger gain for French general government, an estimate {{< infl-val "pal_rapport" >}} times as large as ours when expressed on a common basis. The gap can be decomposed: their shock is instantaneous and measured December to December against a lower expectation, they value debt at market prices, and their perimeter covers all of general government and its inflation-linked bonds. These three factors explain about {{< infl-val "pal_explique" >}}% of the gap; a residual of about {{< infl-val "pal_residu" >}}% remains to be reconciled. The two calculations do not measure the same object. Hilscher, Raviv and Reis set out the method that ties the relief to the maturity of the debt; Andreolli and Rey apply it ex post to France up to mid-2022. For central-bank purchases, the OECD published France's adjusted measure at a single point, end-2022: the effect of purchases read from its chart, {{< infl-val "qe_ocde_effet" >}} years, is close to the one we measure under its convention ({{< infl-val "qe_nous_effet" >}}). The Bundesbank estimated in 2024, without publishing its method, that the adjusted refixing period could be up to two years shorter than residual maturity; for France the gap due to purchases peaks here at {{< infl-val "qe_e1_max" >}} years ({{< infl-val "qe_e1_date" >}}). The OBR measured the same shortening in the United Kingdom.

**Challenged by.** Any reading of the amount as a gain for the government. Pallotti et al. themselves subtract the episode's fiscal costs from their gross gain: support, pensions, public purchases. And the Bundesbank noted in 2022 that, for the share bought by the central bank, the government is in effect exposed to the deposit rate rather than to the bond coupon: this is what the simplified consolidation above addresses.

**Not established.** The share of the later rise in rates caused by the episode, the ultimate incidence of the loss, and what rates would have been without central-bank purchases.

**References read**

- Pallotti, F., Paz-Pardo, G., Slacalek, J., Tristani, O. and Violante, G. L. (2024), "Who Bears the Costs of Inflation? Euro Area Households and the 2021–2023 Shock", NBER Working Paper 31896, September 2024 revision (published in the *Journal of Monetary Economics*, 148; journal version not read).
- Hilscher, J., Raviv, A. and Reis, R. (2022), "Inflating Away the Public Debt? An Empirical Assessment", *Review of Financial Studies*, 35(3), pp. 1553–1595.
- Deutsche Bundesbank (2022), "Government debt in the euro area: developments in creditor structure", *Monthly Report*, July 2022, pp. 77 ff.
- OECD (2023), *Sovereign Borrowing Outlook for OECD Countries 2023*, chapter 1, figure 1.16 (average time to refixing adjusted for central-bank holdings, end-2022).
- Deutsche Bundesbank (2024), *Monthly Report*, April 2024, on the creditor structure of euro-area government debt.
- Office for Budget Responsibility (2021), *Economic and fiscal outlook*, March 2021, box 4.1.
- Andreolli, M. and Rey, H. (2024), "Fiscal Consequences of Missing an Inflation Target", March 2024 version (NBER Working Paper 30819; *IMF Economic Review*, 72(2)).
{{< /confrontation-recherche >}}

## Key takeaways {#retenir}

Inflation reduced the real value of legacy debt: relative to the inflation path expected in early 2021, the real value of payments promised on France's end-2020 fixed-rate marketable government debt is about €{{< infl-val "t" >}}bn lower in 2020 euros, and that loss of real value will not be given back if the price gap persists.

We can measure the erosion of legacy nominal debt quite well. What we cannot honestly turn it into is an equally precise fiscal gain: it is realised slowly, it is measured differently depending on the unit of account, and the cost of the borrowing that followed cannot be attributed to the episode in any known proportion. Central-bank purchases add a question of timing: they mainly brought forward the exposure of the government and the Banque de France taken together to interest rates, which changes when the costs arrive, without making it possible to compute a net gain from inflation.

## Frequently asked questions {#questions}

{{< faq-visible >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page measures how much real value the 2021–2023 inflation took from legacy government debt, and what cannot be concluded from it. Inflation is only one of the possible payers of the debt: the taxpayer, the user of public services and the creditor are others. The book examines those choices and their consequences, on official figures.
{{< /appel-livre >}}

## Where these numbers come from {#sources}

**Debt.** Agence France Trésor, *Rapport d'activité 2020*, central-government marketable debt outstanding at 31 December 2020, line by line: fixed-rate OATs (face value, coupon, maturity date) and BTFs. Each coupon is paid on the anniversary of the maturity date, principal at maturity; end-2020 BTFs are spread over the twelve months of 2021.

**Prices.** Eurostat, monthly HICP for France (`prc_hicp_midx`, 2015 = 100), checked against INSEE's figures for the 36 months of 2021–2023. The expected path starts from the December 2020 level, known in January 2021, grows each year at the expected rate and carries the seasonal pattern observed over 2017–2020; without the seasonal adjustment the result barely changes. Amounts are converted into euros of the 2020 average. The calculation in units of domestic output uses the annual GDP deflator (Eurostat), compared with two expected paths: the ECB survey's HICP expectation and the deflator forecast by the Commission in autumn 2020.

**Expectations.** ECB, *Survey of Professional Forecasters*, first quarter of 2021 (euro area; 2024 interpolated between its 2023 and 2025 horizons, then its long-term expectation); Banque de France, December 2020 projections; European Commission, autumn 2020 and winter 2021 forecasts. Breakevens at 31 December 2020: AFT (Bloomberg data).

**Inflation-linked bonds.** In the counterfactual, the {{< infl-val "idx_n" >}} inflation-linked bonds outstanding at end-2020 receive a fixed coupon equal to their real coupon plus the breakeven of the same index and maturity: at 31 December 2020 the AFT publishes four points (France 5 and 10 years, euro area 10 and 30 years), interpolated by residual maturity; with no short euro-area point, the French curve is shifted by the gap observed at 10 years. Result: €{{< infl-val "idx_j" >}}bn, against {{< infl-val "idx_1" >}} with the euro-area 10-year breakeven alone. Adding the gap between each bond's index and the French HICP (€{{< infl-val "idx_ecart" >}}bn), the ex-post cost to the government of the inflation protection embedded in those bonds reaches €{{< infl-val "idx_tot" >}}bn. The AFT's indexation charge (€{{< infl-val "charge_cum" >}}bn in current euros from 2021 to 2025) covers the whole indexed stock of each year, new issues included: it is not the same quantity.

**Consolidation.** Banque de France share of central-government marketable debt at end-2020: Banque de France, Webstat (holdings by sector, market value). Reserves proxied by the market value of the Banque de France's holdings of government bonds at the start of each year; ECB deposit rate, annual average.

**Central-bank purchases.** Line-by-line schedule of central-government marketable debt at each month-end since December 2013, taken from the AFT's monthly bulletins; the recomputed average life matches each bulletin's to within half a day. Government bonds held by the Banque de France, all portfolios: Banque de France, Webstat, market-value share applied to the outstanding face value, below the bound given by the ECB's government finance statistics. Average maturity of the bonds held: ECB; their breakdown by maturity is not published and is assumed to match the stock's, which slightly overstates the consolidated exposure. Rule for pooled income: Decision (EU) 2016/2248, consolidated version at 1 January 2025 (reference rate: main refinancing operations rate, then the deposit facility rate from 2025). Yield: interest on monetary-policy securities over their average stock, and monetary-income sharing balances, from the Banque de France's annual reports. Country comparison: ECB, government finance statistics (debt by residual maturity, debt held by the national central bank). The income the Eurosystem earns on banknotes and unremunerated reserves is left out. This calculation was subjected to external critical review, which led to rewording the result (a shift of the whole curve, dated end-2022) and to checking, in the accounts, the effect of redistribution among central banks.

**Reconciliation with Pallotti et al.** Done on the annual-average version of the calculation (€{{< infl-val "t_annuel" >}}bn): we explain about {{< infl-val "pal_explique" >}}% of the gap with Pallotti et al.; a residual of about {{< infl-val "pal_residu" >}}% remains to be reconciled.

<details class="repli"><summary>Annex: mechanical allocation of the erosion by end-2020 holdings, which does not identify the ultimate incidence</summary>

Spread according to the shares of central-government marketable debt held at end-2020 (Banque de France, market value), the €{{< infl-val "t" >}}bn erosion would give: non-residents {{< infl-val "part_non_residents" >}}%, i.e. €{{< infl-val "alloc_non_residents" >}}bn; Banque de France {{< infl-val "part_BdF" >}}%, €{{< infl-val "alloc_BdF" >}}bn; insurers {{< infl-val "part_assureurs" >}}%, €{{< infl-val "alloc_assureurs" >}}bn; banks {{< infl-val "part_banques" >}}%, €{{< infl-val "alloc_banques" >}}bn; funds {{< infl-val "part_OPC" >}}%, €{{< infl-val "alloc_OPC" >}}bn; others {{< infl-val "part_autres" >}}%, €{{< infl-val "alloc_autres" >}}bn.

This is a mechanical allocation, not a measure of who lost. Bonds change hands over the years, and the erosion, computed on flows, is spread according to shares measured at market value. The direct holder is not necessarily the one who ultimately loses: an insurer has nominal liabilities to its policyholders, a bank has deposits.

</details>

No number on this page is typed by hand: all come from a reproducible calculation by the author, whose extract is archived with its checksums; the script that writes the page checks the main numerical statements and stops if their conditions no longer hold. Before the page was written, the calculation was subjected to external critical review, which led to revisions to the timing of prices, the construction of the range and the treatment of inflation-linked bonds.

{{< reutiliser figures="figures_inflation" jeu="dette_inflation" sources="AFT, Eurostat, ECB, Banque de France, European Commission" donnees="Cumulative real-value erosion by year of payment, results for each forecast and each breakeven, inflation-linked bonds, simplified consolidation, mechanical allocation by holder and, for the central bank's purchases, the monthly exposure, the refixing period and the yield gap by year; the same content is available as CSV, in long format." >}}
In this page's counterfactual, relative to the inflation expected in early 2021, realised 2021–2023 inflation reduces the real value of the payments promised on France's end-2020 fixed-rate marketable government debt by about €{{< infl-val "t" >}}bn in 2020 euros (€{{< infl-val "a_bas" >}}bn to €{{< infl-val "a_haut" >}}bn depending on the forecast used); about half materialises by {{< infl-val "demi" >}}. It is not an identifiable net fiscal gain.
{{< /reutiliser >}}
