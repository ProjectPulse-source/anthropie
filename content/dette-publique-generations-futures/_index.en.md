---
title: "Is public debt a burden on future generations?"
url: /en/public-debt-future-generations/
description: "Since {gen.a0}, only {gen.part_k}% of French public deficits have corresponded, in the accounts, to a net increase in recorded public assets ({gen.d3_part}% over {gen.d3_lib}). The page also tests “we owe it to ourselves” and “the real burden will come from ageing”, without calculating a bill for each generation. Eurostat, ECB and European Commission series recalculated and checked."
chapo: "A debt can leave the next generations a charge, but also schools, roads and other equipment. What do the French accounts show? From {gen.a0} to {gen.fin}, only {gen.part_k}% of public deficits corresponded to new public assets (equipment, buildings, land), after wear and tear; that share fell to {gen.d3_part}% over {gen.d3_lib}. Two other arguments deserve scrutiny: “we owe the debt to ourselves” and “the real burden will come from ageing”. Three tests put them to the proof, without claiming to calculate each generation’s bill."
date: 2026-07-24
lastmod: 2026-10-11
og_title: "Is public debt a burden on future generations? — S. Lalut"
og_image: "images/og-dette-generations-en.jpg"
og_image_alt: "Share card: “What did thirty years of deficits correspond to?” — France, share of public deficits that corresponded, in the accounts, to assets, by decade, and the rest to uncovered current spending."
# English version of the "future generations" extension of the public debt dossier (FR: content/dette-publique-generations-futures/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/dette_generations.json
# (scripts/update_dette_generations.py), whose guards cover both languages, text guards included (phase B, 11/10/2026).
donnees: [dette_generations]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html); tokens resolved at build time
  jeu: "dette_generations"
  nom: "Public debt and future generations: uses of net borrowing, net worth, debt holdings and the S2 indicator, France and European Union"
  description: "Compilation derived automatically from official sources: uses of general government net borrowing (net dissaving, net acquisitions of non-financial assets, capital transfers), France from {gen.a0} to {gen.fin} and the 27 EU countries from {gen.cp_a0} to {gen.fin} (Eurostat); general government net worth ({gen.s0}-{gen.s1}); debt by holding sector ({gen.h0}-{gen.h_fin}, ECB; central-government marketable debt, Banque de France); the European Commission's S2 indicator ({gen.dsm_lib}); pension spending projected by the COR. Ratios checked against those published by Eurostat."
  couverture_temporelle: "{gen.h0}/{gen.fin}"
  couverture_spatiale: "France; European Union (27 countries)"
  variables:
    - {nom: "General government net borrowing", unite: "points of GDP", description: "cumulated by period, and its three uses"}
    - {nom: "Net acquisitions of non-financial assets", unite: "points of GDP", description: "investment minus consumption of fixed capital, land, inventories"}
    - {nom: "General government net worth", unite: "% of GDP", description: "produced and non-produced non-financial assets, net financial worth"}
    - {nom: "Debt held by non-residents and by the central bank", unite: "% of GDP and % of debt", description: "Maastricht debt by holding sector"}
    - {nom: "S2 indicator and its components", unite: "points of GDP", description: "initial budgetary position, effect of future changes in age-related spending"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/nama_10_nfa_bs/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/nasa_10_f_bs/default/table?lang=en"
    - "https://data.ecb.europa.eu/data/datasets/GFS"
    - "https://webstat.banque-france.fr/fr/catalogue/det/DET.Q.FR.1315.F33000.M.Z9.8.F"
    - "https://economy-finance.ec.europa.eu/publications/debt-sustainability-monitor-2025_en"
    - "https://www.cor-retraites.fr/rapports-du-cor/rapport-annuel-cor-juin-2026-evolutions-perspectives-retraites-france"
  mots: ["public debt", "future generations", "public investment", "public sector net worth", "debt holdings", "non-residents", "pensions", "S2 indicator", "Eurostat", "ECB"]
  fichiers: ["dette_generations.csv", "dette_generations.json"]
faq:
  - question: "Does public debt weigh on future generations?"
    answer: "It leaves them a charge, and also what was acquired at the same time; no single statistic measures the balance of the two. In France, from {gen.a0} to {gen.fin}, {gen.part_k}% of public deficits corresponded, in the accounts, to a net increase in recorded public assets, {gen.part_t}% to capital transfers to other sectors and {gen.part_e}% to current spending that current revenue did not cover. This is an accounting composition: it measures neither what each generation will pay, nor what current spending on education or health produced."
  - question: "Does debt taken on to invest weigh less?"
    answer: "It leaves capital along with the charge: that is why use is a relevant criterion, though it does not say what the spending yields. In France, the share of deficits that corresponded, in the accounts, to a net increase in public assets went from {gen.d1_part}% ({gen.d1_lib}) to {gen.d2_part}% ({gen.d2_lib}), and then to {gen.d3_part}% ({gen.d3_lib}). These shares measure neither the return on spending nor its usefulness to future generations."
  - question: "The “we owe it to ourselves” argument: does it hold for France?"
    answer: "In {gen.h_fin}, {gen.res_fin}% of general government debt was recorded as held by residents and {gen.nr_fin}% by non-residents (ECB): the assumption of a debt held entirely within the country does not describe France. This statistic gives the residence of registered holders, not the burden: it measures neither the net charge left to the following generations nor the country’s net external position. And a debt held at home is not painless for all that."
  - question: "Are pensions the real burden?"
    answer: "The European Commission’s S2 indicator does not answer that question in that form. It puts at {gen.s2} points of GDP the permanent adjustment that would stabilise French debt, of which {gen.ibp} for the initial budgetary position, which includes current pension spending, and {gen.coa} for the future change in age-related spending ({gen.dsm_lib}). That small second term does not mean that pensions cost little; and the Conseil d’orientation des retraites (COR), the French pensions advisory council, projects rising pension spending where the Commission assumes a fall."
  - question: "What will future generations actually pay?"
    answer: "These series cannot put a figure on a bill per child: that would require knowing future policies. A debt is rolled over without any particular generation repaying all of it; it may call for future tax or spending adjustments, weigh on capital accumulation, or come with assets and services from which those who follow will benefit. Its weight also depends on the gap between the interest rate the government pays and the growth of the economy."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif", "explicatif-causal"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 40
  nature: "Official series (Eurostat, ECB, European Commission, COR) and the author's calculations"
  prolongement: true   # option B: "Further topics of the dossier" row, under the grid of the dossier's parts
dossier_dette: prolongement   # "Further topics" panel of the dossier bar
dossier_dette_titre: "A burden for future generations?"
dossier_dette_role: "assets, holders, pensions"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Updated: {{< gen-val "date_donnees" >}}</span> General government, Eurostat and ECB series from {{< gen-val "h0" >}} to {{< gen-val "fin" >}}; European Commission and COR, projections. Download: <a href="/dette_generations.csv">CSV</a> · <a href="/dette_generations.json">JSON</a> · <a href="#sources">method</a></p>

## What deficits corresponded to in the accounts {#assets}

Borrowing to build a school, a road or a network leaves capital as well as a debt. This is an essential argument in assessing the weight of that debt on future generations, provided we know what was acquired and what it will bring. The national accounts answer the first question.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-generations-actifs-en-m.svg" width="300" height="708">
    <img src="/img/dette-generations-actifs-en.svg" alt="Four horizontal bars, each representing one hundred per cent of French general government net borrowing over a period: {{< gen-val "d1_lib" >}}, {{< gen-val "d1_part" >}}% in assets; {{< gen-val "d2_lib" >}}, {{< gen-val "d2_part" >}}%; {{< gen-val "d3_lib" >}}, {{< gen-val "d3_part" >}}%; over the whole period, {{< gen-val "part_k" >}}% in assets, {{< gen-val "part_t" >}}% in capital transfers and {{< gen-val "part_e" >}}% in current spending not covered by current revenue." width="720" height="385" loading="lazy">
  </picture>
  <figcaption>Share of French general government net borrowing that corresponded to assets, to capital transfers and to uncovered current spending, by decade (Eurostat, author’s calculation).</figcaption>
</figure>

<div class="resultat-phrase">

**The finding in one sentence.** From {{< gen-val "a0" >}} to {{< gen-val "fin" >}}, only {{< gen-val "part_k" >}}% of French public deficits corresponded to a net increase in recorded public assets, and {{< gen-val "part_e" >}}%, nearly two thirds, to current spending that current revenue did not cover; the share in assets fell from {{< gen-val "d1_part" >}}% over {{< gen-val "d1_lib" >}} to {{< gen-val "d3_part" >}}% over {{< gen-val "d3_lib" >}}. This is an accounting reading: it says what deficits corresponded to, not what they produced.

</div>

Every year, the public deficit breaks down exactly into three uses. **Net acquisitions of assets**: additional public equipment, land and inventories, once the wear and tear of what already exists has been deducted. **Capital transfers**, {{< gen-val "part_t" >}}% of the total: grants paid to others, firms, households or other bodies, so that they invest, minus revenue of the same kind. **Uncovered current spending**: the part of current spending (running costs, social benefits, interest…) that current revenue did not cover. Since public money is not earmarked for a given expense, this breakdown does not say which borrowed euro paid for which expense: it says what, overall, the deficit corresponded to.

<details class="repli"><summary>The three uses in accounting terms, and what the cumulated amounts mean</summary>

Net acquisitions of assets are investment, minus the wear and tear of existing capital, plus net purchases of land and changes in inventories; only this surplus adds to public net worth. Net capital transfers are investment grants paid to other sectors, minus capital revenue, inheritance taxes included. Uncovered current spending is the excess of current spending, wear and tear of capital included, over current revenue, which accountants call dissaving.

The shares can be read directly. The amounts, for their part, add up yearly net borrowing, each relative to the GDP of its year: the {{< gen-val "b" >}} points of GDP cumulated from {{< gen-val "a0" >}} to {{< gen-val "fin" >}} are neither {{< gen-val "b" >}}% of {{< gen-val "fin" >}} GDP nor the rise in the debt ratio over the period. Investment grants paid to firms, households or bodies outside general government totalled {{< gen-val "d92" >}} points of GDP, cumulated over the period.

</details>

**The share in assets fell decade by decade**, from {{< gen-val "d1_part" >}}% to {{< gen-val "d2_part" >}}% and then to {{< gen-val "d3_part" >}}%, and the two declines do not reflect the same accounting movement. From the first decade to the second, the share fell mainly because cumulated net borrowing rose, from {{< gen-val "d1_b" >}} to {{< gen-val "d2_b" >}} points of GDP, while net acquisitions of assets stayed almost unchanged ({{< gen-val "d1_k" >}}, then {{< gen-val "d2_k" >}} points); from the second to the third, net borrowing stayed almost the same ({{< gen-val "d3_b" >}} points) and net acquisitions of assets nearly halved ({{< gen-val "d3_k" >}} points). Over the last decade, net acquisitions of assets amounted to only {{< gen-val "d3_k_moy_pt" >}} of GDP a year on average. In thirty years, current revenue exceeded current spending in only {{< gen-val "ep_pos_n" >}} years, {{< gen-val "ep_pos_lib" >}}, and in no year did acquisitions of assets match net borrowing. Even counting as capital acquired all the investment grants paid outside general government, the share would reach {{< gen-val "part_max" >}}% at most: still less than half.

**What this share does not measure.** That only {{< gen-val "part_k" >}}% of deficits correspond to recorded assets does not mean that the remaining {{< gen-val "part_hors_k" >}}% produced nothing. The accounts record counterparts, not all benefits: education, health and non-capitalised research are current spending, which may leave the following generations a human capital that these series do not count. Nor do these shares measure the return on spending, or whether a deficit run in a recession, which spreads the effort over time, was justified.

**Neither universal nor exceptional.** The same calculation, applied to the {{< gen-val "cp_n" >}} EU countries over a common window from {{< gen-val "cp_a0" >}} to {{< gen-val "fin" >}}, puts France at {{< gen-val "cp_fr_part" >}}% (against {{< gen-val "part_k" >}}% over {{< gen-val "a0" >}}-{{< gen-val "fin" >}}: the difference comes from the window). Among the {{< gen-val "cp_groupe_n" >}} countries whose cumulated net borrowing reached {{< gen-val "cp_seuil" >}} points of GDP, the share in assets reached at least one half in {{< gen-val "cp_sup_n" >}}, including {{< gen-val "cp_cite_sup" >}}; it was lower than in France in {{< gen-val "cp_inf_n" >}}, including {{< gen-val "cp_cite_inf" >}}. The composition of deficits is therefore not a fate common to all states.

<details class="repli"><summary>The {{< gen-val "cp_n" >}} countries, use by use</summary>

{{< gen-tableau >}}

{{< gen-val "cp_exc_pays_maj" >}}, whose cumulated net borrowing stayed below that threshold or was negative, cannot be compared on this ratio.

</details>

<details class="repli"><summary>The general government balance sheet: a complement, not a proof</summary>

The general government balance sheet seems to offer confirmation: from {{< gen-val "s0" >}} to {{< gen-val "s1" >}}, its net worth — all its non-financial assets, produced or not, minus its debts net of its financial assets — went from {{< gen-val "pn0" >}}% to {{< gen-val "pn1" >}}% of GDP. But this stock depends on the two years being compared. It reached {{< gen-val "pn_haut" >}}% in {{< gen-val "pn_haut_annee" >}}, was still above its starting level in {{< gen-val "pn_sup_annee" >}} ({{< gen-val "pn_sup" >}}%), and it rose by {{< gen-val "pn_d3_var_pt" >}} from {{< gen-val "pn_d3_an0" >}} to {{< gen-val "s1" >}}, the decade in which the share of deficits corresponding to assets fell to {{< gen-val "d3_part" >}}%. Of the {{< gen-val "pn_fen_n" >}} possible comparisons between two years at least ten years apart, {{< gen-val "pn_fen_hausse" >}} show it rising.

Its changes mix flows and revaluations. The value of land changed by {{< gen-val "terr_var_pt" >}} of GDP over the period, unrelated to deficits; even produced assets, which changed by only {{< gen-val "prod_var_pt" >}}, are stocks valued at current prices and relative to GDP, sensitive to prices as well as to the denominator. A flow identity, checked year by year, is not validated by a stock whose changes also obey other mechanisms: the balance sheet remains complementary information here.

</details>

## The “we owe it to ourselves” argument {#holders}

The economist Abba Lerner’s classic argument assumes that the debt is held within the country: servicing it would then amount to levying national taxpayers to pay national savers, and the generation that pays would also be the one that receives. Holdings statistics make it possible to check its premise, not its conclusion.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-generations-detention-en-m.svg" width="300" height="566">
    <img src="/img/dette-generations-detention-en.svg" alt="Stacked areas from {{< gen-val "h0" >}} to {{< gen-val "h_fin" >}}, as a percentage of general government debt: Banque de France, other residents, non-residents. Non-residents go from {{< gen-val "nr0" >}}% to {{< gen-val "nr_fin" >}}%, peaking at {{< gen-val "nr_max" >}}% in {{< gen-val "nr_max_annee" >}}; the Banque de France rises to {{< gen-val "bc_max" >}}% in {{< gen-val "bc_max_annee" >}} and then falls back to {{< gen-val "bc_fin" >}}%." width="720" height="367" loading="lazy">
  </picture>
  <figcaption>Share of general government debt held by non-residents, the Banque de France and other residents (ECB, government finance statistics).</figcaption>
</figure>

In {{< gen-val "h_fin" >}}, {{< gen-val "nr_fin" >}}% of French public debt was recorded as held by non-residents, and {{< gen-val "res_fin" >}}% by residents (ECB). Of the latter, the Banque de France held {{< gen-val "bc_fin" >}}% of the total, and other residents {{< gen-val "ar_fin" >}}%. The Banque de France is set apart because its role is not that of an ordinary private creditor: its holdings rose sharply with the Eurosystem’s purchases of public securities, before receding. With more than half of the debt held by non-residents, the assumption of a debt held entirely within the country does not describe the French situation. It describes Italy ({{< gen-val "h_it" >}}% of debt held by non-residents in {{< gen-val "h_fin" >}}) or Sweden ({{< gen-val "h_se" >}}%) better, and Austria ({{< gen-val "h_at" >}}%) or Belgium ({{< gen-val "h_be" >}}%) less well.

It has not always been so. In {{< gen-val "h0" >}}, {{< gen-val "nr0" >}}% of the debt was held by non-residents; the share passed one half in {{< gen-val "nr_maj_premiere" >}} and stayed above it in {{< gen-val "nr_maj_n" >}} years out of {{< gen-val "nr_maj_tot" >}} since. With these purchases, the Banque de France became a major holder, with up to {{< gen-val "bc_max" >}}% of the debt in {{< gen-val "bc_max_annee" >}}; since then, its holdings have been receding and the non-resident share has risen by {{< gen-val "nr_var_bc" >}} points. The page [Who really pays for public debt?](/en/who-really-pays-public-debt/#creanciers) breaks central-government securities down by holder, and [Did inflation really ease France’s debt burden?](/en/inflation-and-french-public-debt/#detenteurs) shows who held the debt when inflation reduced its real value.

<details class="repli"><summary>Holders year by year, and the scope of central-government securities</summary>

The non-resident share peaked at {{< gen-val "nr_max" >}}% in {{< gen-val "nr_max_annee" >}}. The Banque de France held {{< gen-val "bc0" >}}% of the debt in {{< gen-val "h0" >}}; since {{< gen-val "bc10_premiere" >}}, it has held more than a tenth of it, and the growth of its holdings has offset the decline of other residents, from {{< gen-val "ar_avant" >}}% in {{< gen-val "an_avant" >}} to {{< gen-val "ar_fin" >}}% in {{< gen-val "h_fin" >}}. In {{< gen-val "h_fin" >}}, it held {{< gen-val "bc_var" >}} points less than in {{< gen-val "bc_max_annee" >}}.

On the narrower scope of central-government marketable securities, at market value, the Banque de France describes the same movement: {{< gen-val "etat_fin" >}}% held by non-residents at end-{{< gen-val "h_fin" >}}, a trough of {{< gen-val "etat_min" >}}% in {{< gen-val "etat_min_annee" >}}, at the height of central bank purchases, and {{< gen-val "etat_der" >}}% in the {{< gen-val "etat_der_trim" >}} according to Agence France Trésor, the French debt management office. The general government series is at nominal value, the series for central-government marketable securities at market value: their levels cannot be compared point by point.

</details>

**What holdings statistics do not establish.** They show where creditors are registered, not who bears the charge. They establish neither the residence of each final saver, since a foreign fund may manage the savings of French households and vice versa; nor the net charge left to the following generations; nor France’s net external position, since residents also hold claims on the rest of the world; nor the effects of the debt on capital, incomes and growth. A debt held at home is not neutral for all that: servicing it involves payments, drawn from public resources, to those who hold the securities. And a debt held abroad is not, mechanically, a net loss equal to its value.

## Does future ageing weigh more than the current budget imbalance? {#ageing}

The third argument treats the visible debt as secondary: the real burden would come from ageing. The European Commission makes it possible to test this with its S2 indicator: the permanent improvement in the budget, excluding interest on the debt, that would stabilise debt relative to GDP in the long term, with neither the date nor the level of stabilisation set in advance. To stabilise its debt in the long term, France would thus have to durably improve its budget by {{< gen-val "s2_pt" >}} of GDP, under the Commission’s assumptions (*{{< gen-val "dsm_lib" >}}*).

Of these {{< gen-val "s2_pt" >}}, {{< gen-val "ibp_pt" >}} correspond to the **initial budgetary position**, that is, the gap between the current budget and the one that would stabilise the debt, and {{< gen-val "coa_pt" >}} to the effect of **future changes in age-related spending** (pensions, health, long-term care, education), which the Commission labels the “cost of ageing”.

**A small effect of the future change does not mean that pensions cost little.** Current pension spending, {{< gen-val "cor_dep0" >}}% of GDP in {{< gen-val "cor_a0" >}} in gross terms according to the Conseil d’orientation des retraites (COR), the French pensions advisory council, is already counted in the initial position; the second term measures only its projected change, added to that of other age-related spending.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-generations-vieillissement-en-m.svg" width="300" height="812">
    <img src="/img/dette-generations-vieillissement-en.svg" alt="Horizontal bars by Commission scenario, in points of GDP, with the S2 total: baseline scenario, S2 {{< gen-val "s2" >}}, initial position {{< gen-val "ibp" >}} and effect of future changes in age-related spending {{< gen-val "coa" >}}; lower productivity, S2 {{< gen-val "s2_prod" >}}, {{< gen-val "ibp_prod" >}} and {{< gen-val "coa_prod" >}}; health and long-term care risk, S2 {{< gen-val "s2_risque" >}}, {{< gen-val "ibp_risque" >}} and {{< gen-val "coa_risque" >}}; previous edition, another set of projections, S2 {{< gen-val "s2_prec" >}}, {{< gen-val "ibp_prec" >}} and {{< gen-val "coa_prec" >}}." width="720" height="383" loading="lazy">
  </picture>
  <figcaption>Adjustment that would stabilise French debt (S2 indicator), split between the initial budgetary position and the effect of future changes in age-related spending, according to the European Commission (three scenarios and previous edition).</figcaption>
</figure>

**The result depends on the assumptions.** In the risk scenario where the Commission assumes heavier health and long-term care spending, the effect of future changes in age-related spending reaches {{< gen-val "coa_risque_pt" >}}, against {{< gen-val "coa_pt" >}} in the baseline scenario; S2 then reaches {{< gen-val "s2_risque_pt" >}}. The initial position nevertheless remains the larger term there, as in the lower-productivity scenario. Yet the indicator can show the opposite: in {{< gen-val "pays_coa_n" >}} EU countries out of {{< gen-val "pays_n" >}}, including Belgium, Spain and Luxembourg, the future change in age-related spending weighs more than the initial position.

The COR, for its part, projects pension spending rising as a share of GDP, where the Commission assumes a fall: the two projections rest on different assumptions and cannot be compared directly.

<details class="repli"><summary>Technical definition of S2, and the second term item by item</summary>

S2 is the permanent improvement in the structural primary balance (the balance excluding interest, adjusted for the economic cycle), made in {{< gen-val "s2_an" >}}, that would stabilise the debt over an infinite horizon. Unlike the S1 indicator, which targets {{< gen-val "s1_cible" >}}% of GDP by {{< gen-val "s1_horizon" >}}, it sets neither the level at which the debt stabilises nor the date. The initial budgetary position is the gap between the starting structural balance and the one that would stabilise the ratio.

The effect of future changes in age-related spending is small because it nets out opposite movements. The Commission projects pension spending falling as a share of GDP ({{< gen-val "pen_pt" >}}), net of the taxes and contributions paid by pensioners, with the 2023 reform applied; health spending ({{< gen-val "sante_pt" >}}) and long-term care spending ({{< gen-val "dep_pt" >}}) rise; education spending falls ({{< gen-val "edu_pt" >}}).

</details>

<details class="repli"><summary>Commission and COR: two projections, two sets of assumptions</summary>

**Who is speaking matters here.** The Commission is the institution that enforces the European fiscal rules. The COR, a pluralist body that brings together the social partners, members of parliament and government departments, projects in its baseline scenario ({{< gen-val "cor_lib" >}}) gross pension spending rising from {{< gen-val "cor_dep0" >}}% of GDP in {{< gen-val "cor_a0" >}} to {{< gen-val "cor_dep1" >}}% in {{< gen-val "cor_a1" >}}, a change of {{< gen-val "cor_var_pt" >}}, where the Commission assumes a fall. The two figures cannot be compared term by term: one is gross spending between two dates, the other a net component. Their gap, which may stem from each institution’s assumptions, shows how much the projection depends on them; it does not yield another S2.

The COR bases its projection on INSEE’s new demographic projections, with lower fertility and higher net migration than in its previous reports, and stresses how much its financial diagnosis depends on them; the Commission uses the ageing projections of its 2024 report, drawn up before them. The COR also assumes, for Agirc-Arrco, the supplementary pension scheme for private-sector employees, an uprating of the pension point that is less restrained from 2038 than in its earlier reports, which raises projected spending. Part of the gap between the two institutions may therefore stem from their assumptions, and not from the financial situation of the pension system alone.

The deficit the COR projects for the pension system, {{< gen-val "cor_deficit1_pt" >}} of GDP in {{< gen-val "cor_a1" >}}, stems as much from the projected fall in its resources, from {{< gen-val "cor_res0" >}}% to {{< gen-val "cor_res1" >}}% of GDP, as from the rise in its spending. These are projections conditional on their assumptions.

The Commission’s previous edition ({{< gen-val "dsm_prec_an" >}}) gave {{< gen-val "ibp_prec" >}} for the initial position and {{< gen-val "coa_prec" >}} for the future change in age-related spending: this is another set of projections, not an observed change.

</details>

<details class="repli"><summary>S2 is not the gap calculated on another page of the dossier</summary>

The page [Can public debt come down?](/en/can-public-debt-come-down/#solde-stabilisant) measures a gap of similar size: {{< gen-val "v5_ecart_pt" >}} of GDP in {{< gen-val "v5_annee" >}}, against {{< gen-val "s2_pt" >}} for S2. The first concerns the observed balance of a single year; the second is a permanent adjustment, which includes the projected change in age-related spending. The two numbers are neither two interchangeable estimates nor a validation of each other.

- **Value.** Part 5: {{< gen-val "v5_ecart_pt" >}} of GDP in {{< gen-val "v5_annee" >}}. S2: {{< gen-val "s2_pt" >}} of GDP ({{< gen-val "dsm_lib" >}}).
- **Nature.** Part 5: observed primary balance, one year. S2: structural primary balance, permanent adjustment from {{< gen-val "s2_an" >}}.
- **Horizon.** Part 5: stabilise the ratio that year, at that year’s interest rate and growth. S2: stabilise the debt over an infinite horizon, with no set level or date.
- **Age-related spending to come.** Part 5: not projected. S2: projected change included.

</details>

**What S2 does not say.** It does not say which spending or which revenue should change, or whether pensions pose a problem: it is a projection conditional on its assumptions.

## Why none of these figures is a bill {#bill}

The three tests answer three different questions. The composition of deficits says what they corresponded to in the accounts; holdings say where creditors are registered; S2 says what adjustment would stabilise the debt, under assumptions. None measures what each generation will pay and receive over its lifetime: that is the subject of generational accounting, which these series do not construct.

**What will my children actually pay?** None of these series can put a figure on a bill per child: that would require knowing future policies. They do shed light on the mechanisms through which a debt weighs, or not, on those who come after. A debt is rolled over: the government repays maturing securities by issuing others, and no particular generation repays all of it. It may call for future adjustments, higher taxes or lower spending, if the balance does not stabilise it. It may weigh on capital, if the saving placed in it stops being invested elsewhere. And it may have come with assets and services from which the following generations benefit: the roads and schools counted here, the education and health that are not.

Finally, the weight of the same stock depends on the gap between the interest rate the government pays and the growth of the economy. When the rate exceeds growth, stabilising the debt ratio requires a primary surplus; when it is below growth, a primary deficit can leave it stable. The page [Can public debt come down?](/en/can-public-debt-come-down/#soutenable) measures this gap for France.

## What these data do not say {#limits}

- **What current spending produced.** The page assesses the argument on the scope of recorded assets, not the value of all spending.
- **Causality.** The uses of net borrowing say what deficits corresponded to in the accounts, not why they existed, nor what would have happened without them.
- **The final holder.** Residence is that of the registered holder, not of the final saver.
- **The future.** S2 and the COR projections are scenarios conditional on their assumptions (demography, productivity, legislation), produced by two institutions with different mandates; they cannot be validated by observation.
- **Distribution within a generation.** None of these series says who, within the same generation, pays and receives: that is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

## The anthropic reading: who decides today, who will have to adapt tomorrow? {#anthropic-reading}

The anthropic framework does not settle the macroeconomic controversy; it moves the question from the volume of debt to participation in decisions and the future distribution of adjustments. It comes down to three propositions.

1. One generation can commit to spending whose consequences concern people absent from the decision: no one votes “against” future generations; people vote for budgets part of whose costs will fall to them.
2. A transfer over time does not, on its own, determine who will actually bear the charge: within each generation, the adjustment may go through taxes, user charges, services or savings, and not fall on the same people.
3. Unequal capacities for mobility, avoidance or negotiation may influence that distribution: mobile households, fiscally or geographically, have room for manoeuvre that the least mobile lack.

The third proposition is a refutable hypothesis, not a finding of this page. It is tested on specific reforms, with groups defined in advance; it would be weakened by an adjustment falling mainly on other groups, or by compensation granted to the losers. It is formalised in [AWP-03](/en/awp/awp-03/); [AWP-09](/en/awp/awp-09/) confronts this reading with the public accounts, without establishing the final burden on each generation.

That leaves the question these accounts keep open: will those who must bear the consequences of today’s decisions have the same possibilities of choice, adaptation and protection as those who benefited from them?

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="the use criterion and the decline in investment are found again; reading resident holding as an absence of burden, or the composition of deficits as a measure of the burden between generations, is challenged" >}}
**Measured here.** The uses of French and European general government net borrowing, general government net worth, debt holdings by sector, on Eurostat and ECB series; the breakdown of the S2 indicator, taken from the Commission. None of the texts read calculates these quantities on these sources and these periods: they are validated by reproduction.

**Consistent with.** The use criterion: in Diamond’s model, issuing debt to acquire public capital makes the government a mere intermediary between savers and entrepreneurs, with no short-run or long-run effect. The decline in the share invested: in 21 OECD countries, including France, from 1979 to 2003, a heavier interest burden goes together, five years later, with a lower share of public investment and a higher share of pensions, postponing an investment costing less, politically, than cutting an entitlement (Breunig and Busemeyer). These are associations in a panel, over another period: they do not say why the share invested has fallen in France since. The approach of the S2 indicator, finally, is the one called for by Auerbach, Gokhale and Kotlikoff: starting from the government’s budget constraint over a long horizon and from age-related spending, rather than from a single year’s deficit.

**Challenged by.** Any reading of the breakdown of deficits as a measure of the burden between generations. For Auerbach, Gokhale and Kotlikoff, the measured deficit has, in theory, no necessary relationship with the stance of fiscal policy between generations: it depends on how revenue and spending are labelled. They replace it with generational accounts, which estimate what each generation pays and receives over the rest of its life; for the United States in 1989, under unchanged policy, they found a net burden about 20% heavier for future generations than for newborns. Hence the page’s limit: its breakdown gives the accounting composition of deficits, not the burden on each generation. Any reading, too, according to which only the share held by non-residents would weigh on the following generations. In the efficient case of Diamond’s model, where the interest rate exceeds population growth, internal debt lowers long-run welfare **more** than external debt, because it takes the place of productive capital in wealth holdings. In Blanchard, even a debt rolled over without ever raising taxes reduces capital accumulation; in the case he regards as most representative, welfare rises for the first generation and generally falls afterwards, calculations he himself describes as too rudimentary for an estimate. Barro argues the opposite: altruistic parents would offset the burden through their voluntary transfers, provided these transfers are operative for most people; he acknowledges that in 1989 most economists leaned towards the models in which debt weighs.

**Not established.** The extent to which capital is crowded out in France, and the value of what current spending produced for the following generations: none of the five texts measures them.

**References read**

- Diamond, P. A. (1965), “National Debt in a Neoclassical Growth Model”, *American Economic Review*, 55(5), pp. 1126-1150.
- Auerbach, A. J., Gokhale, J. and Kotlikoff, L. J. (1991), “Generational Accounts: A Meaningful Alternative to Deficit Accounting”, *Tax Policy and the Economy*, 5, pp. 55-110.
- Barro, R. J. (1989), “The Ricardian Approach to Budget Deficits”, *Journal of Economic Perspectives*, 3(2), pp. 37-54.
- Blanchard, O. (2019), “Public Debt and Low Interest Rates”, *American Economic Review*, 109(4), pp. 1197-1229 (read in its PIIE working paper version, no. 19-4).
- Breunig, C. and Busemeyer, M. R. (2012), “Fiscal austerity and the trade-off between public investment and social spending”, *Journal of European Public Policy*, 19(6), pp. 921-938.
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Summary</p>

## What to take away {#takeaways}

**What holds.** Use distinguishes one debt from another, and the French share is low: {{< gen-val "part_k" >}}% of deficits have corresponded to recorded assets since {{< gen-val "a0" >}}, {{< gen-val "d3_part" >}}% over {{< gen-val "d3_lib" >}}, while other EU countries exceed one half. The assumption of a debt held at home does not describe France: {{< gen-val "nr_fin" >}}% of public debt was registered to non-residents in {{< gen-val "h_fin" >}}.

**What is not enough.** None of these figures is a bill: the composition of deficits is not a charge per generation, the residence of creditors is not a net transfer, and S2 is a conditional projection.

**What cannot be concluded.** A debt that corresponds little to recorded assets is not necessarily a debt without benefit. A debt held at home is not necessarily painless. A small effect of the future change in age-related spending does not imply low current pension spending.

To judge what debt leaves to future generations, knowing its amount is not enough: one must know what was acquired at the same time, to whom it is owed, on what conditions it stabilises, and how costs and benefits will be shared.

</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [Why does French public debt rise?](/en/why-does-public-debt-rise/)
- [What does French public debt actually cost?](/en/cost-of-french-public-debt/)
- [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- [And elsewhere?](/en/public-debt-international-comparison/)
- [Can public debt come down?](/en/can-public-debt-come-down/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page puts three arguments to the test of the accounts: what deficits corresponded to, who holds the debt, and what adjustment would stabilise it according to the Commission. It remains to be seen who, within each generation, will bear that adjustment: the taxpayer, the user of public services, the saver through inflation, the creditor through a restructuring? The book, *Dette Publique&nbsp;: Qui paie vraiment&nbsp;?* (in French), takes this analysis further, with official figures, by examining these choices and their consequences.
{{< /appel-livre >}}

## Where these figures come from {#sources}

**Uses of net borrowing.** Eurostat, general government (S.13), ESA 2010 accounts, in national currency (`gov_10a_main`): net lending or borrowing (B9), net saving (B8N), gross fixed capital formation (P51G), consumption of fixed capital (P51C), acquisitions less disposals of non-produced assets (NP), changes in inventories (P52_P53), capital transfers paid and received (D9), of which investment grants paid (D92). Each year, net borrowing = net dissaving + net acquisitions of assets + net capital transfers; the identity is checked year by year, to within 0.05 points. Ratios are calculated on the GDP published with the deficit and debt notification (`gov_10dd_edpt1`) and cumulated by period in points of GDP; the share in assets calculated in current euros gives {{< gen-val "part_k_eur" >}}%, against {{< gen-val "part_k" >}}% in points of GDP. Excluding land and inventories, net investment alone represents {{< gen-val "part_n" >}}% of net borrowing.

**Net worth.** Non-financial assets of general government, produced and non-produced (`nama_10_nfa_bs`, N1N and N2N, current prices), of which land (N211N), and consolidated net financial worth (`nasa_10_f_bs`, BF90), relative to GDP. Asset stocks are valued at current prices: their changes mix flows and revaluations.

**Holdings.** ECB, government finance statistics (GFS): Maastricht debt of general government by counterpart area (rest of the world, residents) and holding sector (central bank). Checks: non-residents and residents add up to total debt each year; over the common years, the values equal those of Eurostat (`gov_10dd_ggd`), reported by the same administration. Scope witness: {{< gen-val "etat_lib" >}}, on Webstat (share of central-government marketable securities held by non-residents, at market value, end of quarter; file from the series’ public page, latest observation published on {{< gen-val "etat_maj" >}}, archived with its hash); latest observation: chart from Agence France Trésor (source Banque de France), read on {{< gen-val "etat_der_lu" >}} with the image’s hash, and checked against Webstat over the common period. The script stops if the two series cease to converge, or if Webstat publishes a period that the reading no longer goes beyond.

**S2 indicator.** European Commission, *{{< gen-val "dsm_lib" >}}*, country tables (file of the edition, archived with its hash): the components used are those of the spreadsheet; table 3.2 of the report prints the initial position as the difference between S2 and the second term, hence {{< gen-val "ibp_pdf" >}} instead of {{< gen-val "ibp" >}} for France. Definitions of S2, of its two terms and of S1: section 3.1 and annex A6 of the report (Institutional Paper 332), read for this page. **Part 5.** The gap to the stabilising balance is read from the data of [Can public debt come down?](/en/can-public-debt-come-down/); the script stops if the year or the value differ. **Pensions.** COR, {{< gen-val "cor_lib" >}}, data from the summary, baseline scenario; Agirc-Arrco indexation rule: part 1, chapter 2 of the report.

Check: for each country and each year, the calculated ratios are compared with those Eurostat publishes as a percentage of GDP, which the calculation does not use. Beyond a gap of {{< gen-val "tolerance" >}} points, the year is excluded and counted ({{< gen-val "cons_ecartees" >}} out of {{< gen-val "cons_calculables" >}}); for France, the script stops. No figure on this page is entered by hand: all come from the same script, which checks the main quantitative statements and stops if their conditions are no longer met; their wording is reviewed editorially. The arguments were tested before the page was written, following a protocol set before the calculation.

{{< reutiliser figures="figures_generations" jeu="dette_generations" sources="Eurostat, ECB, European Commission, COR" donnees="The uses of general government net borrowing (France by decade, 27 EU countries), general government net worth, debt holdings by sector and the Commission’s S2 indicator; the same content exists as CSV, in long format." >}}
From {{< gen-val "a0" >}} to {{< gen-val "fin" >}}, {{< gen-val "part_k" >}}% of French general government net borrowing corresponded, in the accounts, to a net increase in its recorded assets, and {{< gen-val "part_e" >}}% to current spending not covered by current revenue; the share in assets went from {{< gen-val "d1_part" >}}% ({{< gen-val "d1_lib" >}}) to {{< gen-val "d3_part" >}}% ({{< gen-val "d3_lib" >}}). This is an accounting reading, not a causal attribution: these shares measure neither the return on spending nor its usefulness to future generations. In {{< gen-val "h_fin" >}}, {{< gen-val "nr_fin" >}}% of public debt was registered to non-residents, which gives the residence of holders, not the burden.
{{< /reutiliser >}}
