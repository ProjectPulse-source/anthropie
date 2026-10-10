---
title: "Is public debt a burden on future generations?"
url: /en/public-debt-future-generations/
description: "Since {gen.a0}, only {gen.part_k}% of French public deficits have corresponded, in the accounts, to a net increase in recorded public assets, and {gen.nr_fin}% of the debt is held outside France. According to the European Commission, the effort the debt leaves behind stems from the current budgetary position far more than from ageing. Eurostat and ECB series recalculated and checked."
chapo: "Two arguments lighten the weight of debt for those who come after; the accounts do not support them for France. On the scope of recorded assets, only {gen.part_k}% of deficits have corresponded since {gen.a0} to a net increase in public assets; and {gen.nr_fin}% of the debt is now held outside the country. The third, which places the real burden in pensions, holds up no better: according to the European Commission's indicator, the effort that would stabilise the debt stems from the current budgetary position far more than from ageing."
date: 2026-07-24
lastmod: 2026-10-08
og_title: "Is public debt a burden on future generations? — S. Lalut"
og_image: "images/og-dette-generations-en.jpg"
og_image_alt: "Share card: “Deficits for current spending” — France, share of public deficits that corresponded, in the accounts, to assets, by decade, and the rest to uncovered current spending."
# English version of the "future generations" extension of the public debt dossier (FR: content/dette-publique-generations-futures/_index.md),
# 07/10/2026. Same tokens, same keys: values come from the affichage_en block of data/dette_generations.json
# (scripts/update_dette_generations.py), whose guards cover both languages. Table: ue.tableau_en; figures and share card: -en.
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
    - {nom: "S2 indicator and its components", unite: "points of GDP", description: "initial budgetary position, cost of ageing"}
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
    answer: "It leaves them a charge to bear, and also what was acquired at the same time. In France, from {gen.a0} to {gen.fin}, {gen.part_k}% of public deficits corresponded, in the accounts, to a net increase in recorded public assets, {gen.part_t}% to capital transfers to other sectors and {gen.part_e}% to current spending that current revenue did not cover; general government net worth went from {gen.pn0}% to {gen.pn1}% of GDP between {gen.s0} and {gen.s1}. This is an accounting composition, not a measure of the burden between generations; and what current spending produced, in education or health, is not counted as an asset."
  - question: "The “we owe it to ourselves” argument: does it hold for France?"
    answer: "For only {gen.res_fin}% of the debt: in {gen.h_fin}, {gen.nr_fin}% of general government debt was held by non-residents, against {gen.nr0}% in {gen.h0} (ECB). The share held in France has been supported by purchases by the Banque de France, which held {gen.bc_max}% of it in {gen.bc_max_annee} and {gen.bc_fin}% in {gen.h_fin}. And the share held within the country is not neutral for all that: servicing it involves payments, funded from public resources, to those who hold the securities."
  - question: "Are pensions the real burden?"
    answer: "Not according to the European Commission's long-term sustainability indicator: the permanent adjustment that would stabilise French debt amounts to {gen.s2} points of GDP, of which {gen.ibp} due to the current budgetary position and {gen.coa} due to ageing ({gen.dsm_lib}), and the current position remains the dominant component in the Commission's risk scenarios. The Conseil d'orientation des retraites (COR), the French pensions advisory council, projects higher pension spending; an order of magnitude, which is not a calculation of the same kind, leaves the ranking unchanged, unless that path is combined with the Commission's risk scenario on health and long-term care."
  - question: "Is debt that finances investment a burden?"
    answer: "Less than other debt: borrowing to acquire an asset leaves the capital along with the charge. That is why use is the right criterion. In France, the share of deficits that corresponded, in the accounts, to a net increase in public assets went from {gen.d1_part}% ({gen.d1_lib}) to {gen.d2_part}% ({gen.d2_lib}) and then {gen.d3_part}% ({gen.d3_lib})."
  - question: "What is the link with the anthropic framework?"
    answer: "Public debt is a textbook case of temporal transfer: a present cost can be shifted onto future payers who took no part in the decision. The framework adds a social hypothesis: within each generation, the adjustment may weigh more heavily on the least mobile groups, fiscally or geographically — a hypothesis to be tested reform by reform. The analysis is formalised in AWP-03 (DOI 10.5281/zenodo.19434094), tested against the accounts in AWP-09 (DOI 10.5281/zenodo.23145963), and developed in the book Dette Publique : Qui paie vraiment ? (2025, in French)."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 40
  nature: "Official series (Eurostat, ECB, European Commission, COR) and the author's calculations"
  prolongement: true   # option B: "Further topics of the dossier" row, under the grid of the dossier's parts
dossier_dette: prolongement   # "Further topics" panel of the dossier bar
dossier_dette_titre: "A burden for future generations?"
dossier_dette_role: "assets passed on, holders, pensions"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Updated: {{< gen-val "date_donnees" >}}</span> General government, Eurostat and ECB series from {{< gen-val "h0" >}} to {{< gen-val "fin" >}}; European Commission and COR, projections. Download: <a href="/dette_generations.csv">CSV</a> · <a href="/dette_generations.json">JSON</a> · <a href="#sources">method</a></p>

## What deficits corresponded to in the accounts {#assets}

<figure class="figure-ciseau">
  <img src="/img/dette-generations-actifs-en.svg" alt="Four horizontal bars, each representing one hundred per cent of French general government net borrowing over a period: {{< gen-val "d1_lib" >}}, {{< gen-val "d1_part" >}}% in assets; {{< gen-val "d2_lib" >}}, {{< gen-val "d2_part" >}}%; {{< gen-val "d3_lib" >}}, {{< gen-val "d3_part" >}}%; over the whole period, {{< gen-val "part_k" >}}% in assets, {{< gen-val "part_t" >}}% in capital transfers and {{< gen-val "part_e" >}}% in uncovered current spending." width="720" height="352" loading="lazy">
  <figcaption>Share of French general government net borrowing that corresponded to assets, to capital transfers and to uncovered current spending, by decade (Eurostat, author’s calculation).</figcaption>
</figure>

<div class="resultat-phrase">

**The finding in one sentence.** From {{< gen-val "a0" >}} to {{< gen-val "fin" >}}, French general government net borrowing totalled {{< gen-val "b" >}} points of GDP: {{< gen-val "k" >}} corresponded to a net increase in its recorded assets ({{< gen-val "part_k" >}}%), {{< gen-val "t" >}} to capital transfers to other sectors, and {{< gen-val "e" >}}, nearly two thirds, to current spending that its current revenue did not cover. This is an accounting reading: it says what deficits corresponded to, not what they produced.

</div>

The strongest argument for saying that a debt does not weigh on those who come after is that of the asset passed on: a debt taken on while building a road, a school or a network bequeaths capital along with a charge. The national accounts make it possible to test this, because the public deficit — general government net borrowing — breaks down exactly into three uses. Since public money is fungible, this breakdown does not say which borrowed euro paid for which expense: it says what, overall, the deficit corresponded to. **Net acquisitions of assets**: investment, minus the wear and tear of existing capital, plus net purchases of land and changes in inventories — only this surplus adds to net worth. **Net capital transfers**: investment grants paid to other sectors, minus capital revenue, inheritance taxes included. And **dissaving**: current spending, wear and tear of capital included, that current revenue does not cover.

**The share invested fell decade by decade**: {{< gen-val "d1_part" >}}% in {{< gen-val "d1_lib" >}}, {{< gen-val "d2_part" >}}% in {{< gen-val "d2_lib" >}}, {{< gen-val "d3_part" >}}% in {{< gen-val "d3_lib" >}}. Over the last decade, net acquisitions of assets amounted to only {{< gen-val "d3_k_moy" >}} points of GDP a year on average, against net borrowing of {{< gen-val "d3_b" >}} points over ten years. In thirty years, current revenue covered current spending in only {{< gen-val "ep_pos_n" >}} years, {{< gen-val "ep_pos_lib" >}}, and in no year did acquisitions of assets match net borrowing.

Part of the transfers does correspond to capital, but capital held elsewhere: investment grants paid to firms, households or bodies outside general government totalled {{< gen-val "d92" >}} points of GDP over the period. Counting all of them as capital acquired would raise the share to {{< gen-val "part_max" >}}% at most: still less than half.

**The balance sheet points the same way.** From {{< gen-val "s0" >}} to {{< gen-val "s1" >}}, general government net worth — all its non-financial assets, produced or not, minus its debts net of its financial assets — went from {{< gen-val "pn0" >}}% to {{< gen-val "pn1" >}}% of GDP, and it falls whichever of the first sixteen years of the series is taken as the starting point. Its produced assets barely moved ({{< gen-val "prod_var" >}} points), its net financial worth fell by {{< gen-val "bf_var_abs" >}} points, and it was mainly the rise in the value of land ({{< gen-val "terr_var" >}} points), which owes nothing to deficits, that limited the fall. Descriptive counter-calculation: without that rise, the fall would have been {{< gen-val "pn_hors_terr" >}} points of GDP.

**France is not an extreme case.** From {{< gen-val "cp_a0" >}} to {{< gen-val "fin" >}}, the same calculation for the {{< gen-val "cp_n" >}} EU countries. Among the {{< gen-val "cp_groupe_n" >}} whose cumulated net borrowing reached {{< gen-val "cp_seuil" >}} points of GDP, the share of net acquisitions of assets reached at least one half in {{< gen-val "cp_sup_n" >}} — {{< gen-val "cp_sup_pays" >}} — and it was lower than in France ({{< gen-val "cp_fr_part" >}}%) in {{< gen-val "cp_inf_n" >}}, including Germany and Italy. {{< gen-val "cp_exc_pays_maj" >}}, close to balance or in surplus over the period, cannot be compared on this ratio.

<details class="repli"><summary>The {{< gen-val "cp_n" >}} countries, use by use</summary>

{{< gen-tableau >}}

</details>

## The “we owe it to ourselves” argument {#holders}

Abba Lerner’s classic argument assumes that the debt is held within the country: servicing it would then amount to levying national taxpayers to pay national savers, and the generation that pays would also be the one that receives. For France, this premise now holds for only {{< gen-val "res_fin" >}}% of the debt.

<figure class="figure-ciseau">
  <img src="/img/dette-generations-detention-en.svg" alt="Stacked areas from {{< gen-val "h0" >}} to {{< gen-val "h_fin" >}}, as a percentage of general government debt: Banque de France, other residents, non-residents. Non-residents go from {{< gen-val "nr0" >}}% to {{< gen-val "nr_fin" >}}%, peaking at {{< gen-val "nr_max" >}}% in {{< gen-val "nr_max_annee" >}}; the Banque de France rises to {{< gen-val "bc_max" >}}% in {{< gen-val "bc_max_annee" >}} and then falls back to {{< gen-val "bc_fin" >}}%." width="720" height="352" loading="lazy">
  <figcaption>Share of general government debt held by non-residents, the Banque de France and other residents (ECB, government finance statistics).</figcaption>
</figure>

In {{< gen-val "h0" >}}, {{< gen-val "nr0" >}}% of general government debt was held by non-residents. The share passed one half in {{< gen-val "nr_maj_premiere" >}}, stayed above it in {{< gen-val "nr_maj_n" >}} years out of {{< gen-val "nr_maj_tot" >}} since, and peaked at {{< gen-val "nr_max" >}}% in {{< gen-val "nr_max_annee" >}}. The Banque de France then became a major holder, through the Eurosystem’s public-sector purchase programmes: {{< gen-val "bc0" >}}% of the debt in {{< gen-val "h0" >}}, {{< gen-val "bc_max" >}}% in {{< gen-val "bc_max_annee" >}}. Since then, its holdings have been receding — {{< gen-val "bc_fin" >}}% in {{< gen-val "h_fin" >}}, {{< gen-val "bc_var" >}} points less — and the non-resident share has risen by {{< gen-val "nr_var_bc" >}} points, to {{< gen-val "nr_fin" >}}%. Since {{< gen-val "bc10_premiere" >}}, the Banque de France has held more than a tenth of the debt, and the growth of its holdings has offset the decline in the share of other residents: they held {{< gen-val "ar_avant" >}}% of it in {{< gen-val "an_avant" >}}, and hold only {{< gen-val "ar_fin" >}}% in {{< gen-val "h_fin" >}}.

The Banque de France publishes the same measure on another scope, the one followed by Agence France Trésor, the French debt management office: central-government marketable securities alone, at market value. At end-{{< gen-val "h_fin" >}}, {{< gen-val "etat_fin" >}}% of these securities were held by non-residents, against {{< gen-val "etat_0" >}}% at end-{{< gen-val "etat_a0" >}}; the share peaked at {{< gen-val "etat_max" >}}% in {{< gen-val "etat_max_annee" >}}, fell back to {{< gen-val "etat_min" >}}% in {{< gen-val "etat_min_annee" >}}, at the height of central bank purchases, and has been rising since: {{< gen-val "etat_der" >}}% in the {{< gen-val "etat_der_trim" >}}, the latest observation published by Agence France Trésor based on Banque de France data. Despite their different scopes and valuations, the two series converge on three facts: a non-resident majority today, a trough at the time of central bank purchases, a rise since.

The residence counted here is that of the registered holder — a fund, a custodian — not that of the final saver: a foreign fund may manage the savings of French households, and vice versa. Above all, the share held within the country is not neutral for all that: servicing it involves payments, funded from public resources, to those who hold the securities; these series do not say who ultimately bears or receives the net charge. Elsewhere, Lerner’s premise holds better than in France, in Italy ({{< gen-val "h_it" >}}% of debt held by non-residents in {{< gen-val "h_fin" >}}) or in Sweden ({{< gen-val "h_se" >}}%); it holds less in Austria ({{< gen-val "h_at" >}}%) or Belgium ({{< gen-val "h_be" >}}%).

## Does the real burden lie in pensions? {#ageing}

A third argument shifts the question: visible debt would be secondary, the real burden would lie in pensions and ageing. The European Commission’s long-term sustainability indicator, known as S2, makes it possible to test this. It measures the permanent adjustment of the structural primary balance that would stabilise debt over an infinite horizon, and splits it into two terms: the starting budgetary position, and the projected cost of ageing — pensions, health, long-term care, education.

<figure class="figure-ciseau">
  <img src="/img/dette-generations-vieillissement-en.svg" alt="Horizontal bars by Commission scenario, in points of GDP: current budgetary position {{< gen-val "ibp" >}} and ageing {{< gen-val "coa" >}} in the baseline scenario; {{< gen-val "ibp_prod" >}} and {{< gen-val "coa_prod" >}} with lower productivity; {{< gen-val "ibp_risque" >}} and {{< gen-val "coa_risque" >}} in the health and long-term care risk scenario; {{< gen-val "ibp_prec" >}} and {{< gen-val "coa_prec" >}} in the previous edition." width="720" height="322" loading="lazy">
  <figcaption>Adjustment that would stabilise French debt, split between the current budgetary position and the cost of ageing, according to the European Commission (three scenarios and previous edition).</figcaption>
</figure>

For France, in the *{{< gen-val "dsm_lib" >}}*, S2 amounts to {{< gen-val "s2" >}} points of GDP: {{< gen-val "ibp" >}} due to the current budgetary position, {{< gen-val "coa" >}} due to ageing. Pensions account for {{< gen-val "pen" >}} points — the Commission projects pension spending falling as a share of GDP, net of the levies on it —, health and long-term care for {{< gen-val "hc_ltc" >}}, education for {{< gen-val "edu" >}}. The current position remains the dominant component in both of the Commission’s risk scenarios, including the one that makes health and long-term care heavier (ageing: {{< gen-val "coa_risque" >}} points, against {{< gen-val "ibp_risque" >}}). And the indicator can show the opposite: in {{< gen-val "pays_coa_n" >}} EU countries out of {{< gen-val "pays_n" >}}, including Belgium, Spain and Luxembourg, ageing outweighs the starting position.

Who is speaking matters here. The Commission is the institution that enforces the European fiscal rules, and its projection of French pensions assumes the 2023 reform is applied; its “pensions” component is net of the taxes and contributions paid by pensioners. The Conseil d’orientation des retraites (COR), a pluralist body that brings together the social partners, members of parliament and government departments, projects in its baseline scenario ({{< gen-val "cor_lib" >}}) gross pension spending rising from {{< gen-val "cor_dep0" >}}% of GDP in {{< gen-val "cor_a0" >}} to {{< gen-val "cor_dep1" >}}% in {{< gen-val "cor_a1" >}}, a change of {{< gen-val "cor_var" >}} points, where the Commission assumes a fall.

**An order of magnitude, not a component of S2.** If, purely for illustration, the Commission’s “pensions” component is replaced by this COR change — two quantities of a different nature, a net present value on one side, a gross change between two dates on the other —, the cost of ageing would become {{< gen-val "coa_cor" >}} points, still less than the current position ({{< gen-val "ibp" >}}). The same exercise, combined with the Commission’s risk scenario on health and long-term care, would reverse the order ({{< gen-val "coa_cor_risque" >}} points against {{< gen-val "ibp_risque" >}}). This calculation by the author indicates a sensitivity; it does not replace the indicator.

**Two projections, two sets of assumptions.** The COR bases its projection on INSEE’s new demographic projections, with lower fertility and higher net migration than in its previous reports, and stresses how much its financial diagnosis depends on them; the Commission uses the ageing projections of its 2024 report, drawn up before them. The COR also assumes, for Agirc-Arrco, the supplementary pension scheme for private-sector employees, an uprating of the pension point that is less restrained from 2038 than in its earlier reports, which raises projected spending. Part of the gap between the two institutions may therefore stem from their assumptions, and not from the financial situation of the pension system alone.

The deficit the COR projects for the pension system, {{< gen-val "cor_solde1" >}} points of GDP in {{< gen-val "cor_a1" >}}, stems moreover as much from the projected fall in its resources, from {{< gen-val "cor_res0" >}}% to {{< gen-val "cor_res1" >}}% of GDP, as from the rise in its spending. These figures are conditional projections: they do not say that pensions pose no problem, but that the effort French debt requires stems first from the present gap between revenue and spending.

## What these data do not say {#limits}

- **What current spending produced.** The national accounts do not count education, health or non-capitalised research as assets: part of current spending leaves the following generations a human capital that these series do not see. The page assesses the argument on the scope of recorded assets, not the value of all spending.
- **The burden between generations.** The accounting composition of deficits is not, on its own, a measure of what each generation pays and receives over its lifetime: that is the subject of generational accounting, which these series do not construct.
- **Causality.** The uses of net borrowing say what deficits corresponded to in the accounts, not why they existed, nor what would have happened without them.
- **The final holder.** Residence is that of the registered holder, not that of the final saver. The general government series is at nominal value, the series for central-government marketable securities at market value: their levels cannot be compared point by point.
- **The future.** S2 and the COR projections are scenarios conditional on their assumptions (demography, productivity, legislation), produced by two institutions with different mandates; they cannot be validated by observation.
- **Distribution within a generation.** None of these series says who, within the same generation, pays and receives: that is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

## The anthropic reading: from the question of volume to that of distribution {#anthropic-reading}

The anthropic framework does not settle the macroeconomic controversy — it adds a question to it. Public debt is a textbook case of **temporal transfer**: a present cost can be shifted onto payers who took no part in the trade-offs. No one votes “against” future generations; people vote for budgets part of whose costs will fall to them, and that part is never presented under that name. The accounts on this page document two observable dimensions of it for France: the small share of deficits that corresponded to a net increase in recorded assets, and a debt now mostly held outside the country.

It adds a hypothesis that the debate on volume ignores: **within each generation, the adjustment may weigh unequally**. Mobile households — fiscally, geographically — have capacities for avoidance that the least mobile groups lack; if the adjustment follows the line of least resistance, it is the latter who bear it, through taxes, user charges or services. The hypothesis is tested on specific reforms, with groups defined in advance; it would be weakened by an adjustment falling mainly on other groups, or by compensation granted to the losers. Likewise, a budget constrained by debt service may postpone ecological investment; where this postponement is established, the same heirs receive the financial debt and the deferred climate disorder.

The working paper [AWP-09](/en/awp/awp-09/) gives the verdict of these accounts on the reading of AWP-03: the shift towards the following generations is supported there within a balance-sheet scope, that of recorded assets, without the final burden on each generation being established.

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="the use criterion and the decline in investment are found again; reading resident holding as an absence of burden, or the composition of deficits as a measure of the burden between generations, is challenged" >}}
**Measured here.** The uses of French and European general government net borrowing, general government net worth, debt holdings by sector, on Eurostat and ECB series; the breakdown of the S2 indicator, taken from the Commission. None of the texts read calculates these quantities on these sources and these periods: they are validated by reproduction.

**Consistent with.** The use criterion: in Diamond’s model, issuing debt to acquire public capital makes the government a mere intermediary between savers and entrepreneurs, with no short-run or long-run effect. The decline in the share invested: in 21 OECD countries, including France, from 1979 to 2003, a heavier interest burden goes together, five years later, with a lower share of public investment and a higher share of pensions, postponing an investment costing less, politically, than cutting an entitlement (Breunig and Busemeyer). These are associations in a panel, over another period: they do not say why the share invested has fallen in France since. The approach of the S2 indicator, finally, is the one called for by Auerbach, Gokhale and Kotlikoff: starting from the government’s budget constraint over a long horizon and from age-related spending, rather than from a single year’s deficit.

**Challenged by.** Any reading of the breakdown of deficits as a measure of the burden between generations. For Auerbach, Gokhale and Kotlikoff, the measured deficit has, in theory, no necessary relationship with the stance of fiscal policy between generations: it depends on how revenue and spending are labelled. They replace it with generational accounts, which estimate what each generation pays and receives over the rest of its life; for the United States in 1989, under unchanged policy, they found a net burden about 20% heavier for future generations than for newborns. Hence the page’s limit: its breakdown gives the accounting composition of deficits, not the burden on each generation. Any reading, too, according to which only the share held by non-residents would weigh on the following generations. In the efficient case of Diamond’s model, where the interest rate exceeds population growth, internal debt lowers long-run welfare **more** than external debt, because it takes the place of productive capital in wealth holdings. In Blanchard, even a debt rolled over without ever raising taxes reduces capital accumulation; in the case he regards as most representative, welfare rises for the first generation and generally falls afterwards, calculations he himself describes as too rudimentary for an estimate. Barro argues the opposite: altruistic parents would offset the burden through their voluntary transfers, provided these transfers are operative for most people; he acknowledges that in 1989 most economists leaned towards the models in which debt weighs.

**Not established.** The extent to which capital is crowded out in France, and the value of what current spending passed on: none of the five texts measures them.

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

A debt does not leave only a charge: it also leaves what was acquired at the same time. In France, over thirty years, net acquisitions of recorded assets corresponded to only {{< gen-val "part_k" >}}% of deficits, and this share fell decade by decade, down to {{< gen-val "d3_part" >}}% in {{< gen-val "d3_lib" >}}. General government net worth fell from {{< gen-val "pn0" >}}% to {{< gen-val "pn1" >}}% of GDP.

“We owe it to ourselves” holds for only {{< gen-val "res_fin" >}}% of the debt, a share supported since {{< gen-val "bc10_premiere" >}} by central bank purchases, and receding with them. And even when it is held within the country, its service involves payments, funded from public resources, to the holders of the securities.

Ageing is not, according to the Commission’s indicator, what makes French debt hard to stabilise: it is the present gap between revenue and spending ({{< gen-val "ibp" >}} points of GDP, against {{< gen-val "coa" >}} for ageing), in all its scenarios.

These accounts say neither what current spending produced, nor who, within each generation, will bear the adjustment: that is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

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
This page documents three dimensions of French debt: what deficits corresponded to in the accounts, who holds the debt, and where the stabilisation effort measured by the Commission comes from. It remains to be seen who, within each generation, will bear that effort: the taxpayer, the user of public services, the saver through inflation, the creditor through a restructuring? The book, *Dette Publique&nbsp;: Qui paie vraiment&nbsp;?* (in French), takes this analysis further, with official figures, by examining these choices and their consequences.
{{< /appel-livre >}}

## Where these figures come from {#sources}

**Uses of net borrowing.** Eurostat, general government (S.13), ESA 2010 accounts, in national currency (`gov_10a_main`): net lending or borrowing (B9), net saving (B8N), gross fixed capital formation (P51G), consumption of fixed capital (P51C), acquisitions less disposals of non-produced assets (NP), changes in inventories (P52_P53), capital transfers paid and received (D9), of which investment grants paid (D92). Each year, net borrowing = net dissaving + net acquisitions of assets + net capital transfers; the identity is checked year by year, to within 0.05 point. Ratios are calculated on the GDP published with the deficit and debt notification (`gov_10dd_edpt1`) and cumulated by period in points of GDP; the share in assets calculated in current euros gives {{< gen-val "part_k_eur" >}}%, against {{< gen-val "part_k" >}}% in points of GDP. Excluding land and inventories, net investment alone represents {{< gen-val "part_n" >}}% of net borrowing.

**Net worth.** Non-financial assets of general government, produced and non-produced (`nama_10_nfa_bs`, N1N and N2N, current prices), of which land (N211N), and consolidated net financial worth (`nasa_10_f_bs`, BF90), relative to GDP. Asset stocks are valued at current prices: their changes mix flows and revaluations.

**Holdings.** ECB, government finance statistics (GFS): Maastricht debt of general government by counterpart area (rest of the world, residents) and holding sector (central bank). Checks: non-residents and residents add up to total debt each year; over the common years, the values equal those of Eurostat (`gov_10dd_ggd`), transmitted by the same reporting institution. Scope witness: {{< gen-val "etat_lib" >}}, on Webstat (share of central-government marketable securities held by non-residents, at market value, end of quarter; file from the series’ public page, latest observation published on {{< gen-val "etat_maj" >}}, archived with its hash); latest observation: chart from Agence France Trésor (source Banque de France), read on {{< gen-val "etat_der_lu" >}} with the image’s hash, and checked against Webstat over the common period. The script stops if the two series cease to converge, or if Webstat publishes a period that the reading no longer goes beyond.

**S2 indicator.** European Commission, *{{< gen-val "dsm_lib" >}}*, country tables (file of the edition, archived with its hash): the components used are those of the spreadsheet; table 3.2 of the report prints the initial position as the difference between S2 and the cost of ageing, hence {{< gen-val "ibp_pdf" >}} instead of {{< gen-val "ibp" >}} for France. **Pensions.** COR, {{< gen-val "cor_lib" >}}, data from the summary, baseline scenario; Agirc-Arrco indexation rule: part 1, chapter 2 of the report. The illustrative substitution of the COR path for the Commission’s “pensions” component is a calculation by the author, outside the S2 method.

Check: for each country and each year, the calculated ratios are compared with those Eurostat publishes as a percentage of GDP, which the calculation does not use. Beyond a gap of {{< gen-val "tolerance" >}} points, the year is excluded and counted ({{< gen-val "cons_ecartees" >}} out of {{< gen-val "cons_calculables" >}}); for France, the script stops. No figure on this page is entered by hand: all come from the same script, which checks the main quantitative statements and stops if their conditions are no longer met; their wording is reviewed editorially. The arguments were tested before the page was written, following a protocol set before the calculation.

{{< reutiliser figures="figures_generations" jeu="dette_generations" sources="Eurostat, ECB, European Commission, COR" donnees="The uses of general government net borrowing (France by decade, 27 EU countries), general government net worth, debt holdings by sector and the Commission’s S2 indicator; the same content exists as CSV, in long format." >}}
From {{< gen-val "a0" >}} to {{< gen-val "fin" >}}, {{< gen-val "part_k" >}}% of French general government net borrowing corresponded, in the accounts, to a net increase in its recorded assets, and {{< gen-val "part_e" >}}% to current spending not covered by current revenue; the share invested went from {{< gen-val "d1_part" >}}% ({{< gen-val "d1_lib" >}}) to {{< gen-val "d3_part" >}}% ({{< gen-val "d3_lib" >}}). In {{< gen-val "h_fin" >}}, {{< gen-val "nr_fin" >}}% of public debt was held by non-residents. This is an accounting reading, not a causal attribution.
{{< /reutiliser >}}
