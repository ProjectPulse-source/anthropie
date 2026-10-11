---
title: "What does French public debt actually cost?"
url: /en/cost-of-french-public-debt/
description: "What does French public debt cost? {dette.interets_mdeur} billion euros of interest in {dette.interets_annee}, {dette.interets_sur_recettes_pct}% of public revenue: a fast rise, to a level already seen in {dette.niv_pib_annee}. Where the rise comes from, and why it can last."
chapo: "In {dette.interets_annee}, French general government owes {dette.interets_mdeur} billion euros of interest, {dette.interets_sur_recettes_pct}% of its revenue: {dette.interets_hausse_pct}% more than at the {dette.interets_creux_annee} trough. The rise is fast, but the level is not unprecedented: as a share of GDP, the burden is back to its {dette.niv_pib_annee} level and remains below 1995. For twenty-five years the debt doubled as a share of GDP while its bill fell. This page explains why, where the rise comes from, and why it can last even if the debt stops growing."
date: 2026-08-17
lastmod: 2026-10-11
donnees: [dette_officielle]
og_title: "What does French public debt cost? — official data, kept current — S. Lalut"
og_image: "images/og-cout-dette-en.jpg"
og_image_alt: "Share card: “What does French public debt cost?” — debt stock and interest burden as a share of GDP, 1995-2025, sources INSEE and Eurostat."
# Émet le JSON-LD Dataset (partials/schema-dataset-dette.html), en anglais :
# un seul jeu de données, deux descriptions — voir le partial.
dataset_dette: true
faq:
  - question: "How much does French public debt cost each year?"
    answer: "The most direct measure is the interest burden of general government: {dette.interets_mdeur} billion euros in {dette.interets_annee}, or {dette.interets_pct_pib}% of GDP and {dette.interets_sur_recettes_pct}% of public revenue (Eurostat, series D41PAY, interest recorded when it falls due). That is {dette.interets_hausse_pct}% more than at the {dette.interets_creux_annee} trough, and {dette.interets_hausse_2019_pct}% more than in 2019. The level is not unprecedented: as a share of GDP, the burden is back to its {dette.niv_pib_annee} level, as a share of revenue to its {dette.niv_rec_annee} level, and it remains below 1995 ({dette.interets_1995_pct_pib}% of GDP). Net of the interest general government receives, it comes to {dette.interets_nets_mdeur} billion."
  - question: "How large is France's public debt?"
    answer: "{dette.dette_mdeur} billion euros in {dette.dette_periode}, or {dette.dette_pct_pib}% of GDP (INSEE, Maastricht debt of general government). Over the INSEE series available since 1995, the highest debt-to-GDP ratio is reached in {dette.dette_pic_periode} ({dette.dette_pic_pct_pib}%)."
  - question: "Why is the interest burden rising so fast?"
    answer: "Because two terms are rising together: the amount of debt and its average cost, the implicit interest rate. From {dette.dec_a0} to {dette.dec_a1}, the burden rises by {dette.dec_delta} billion euros; in an accounting decomposition, {dette.dec_volume} come from the larger debt stock and {dette.dec_taux} from the higher implicit rate (since 2019, before the pandemic, the split reverses: {dette.dec19_volume} from the stock, {dette.dec19_taux} from the rate). The implicit rate made most of its move in {dette.dec_saut_annee}, the year inflation also raised the cost of the State's inflation-linked bonds (the series do not measure indexation's share); since then, the larger stock has weighed most. This decomposition does not measure the effect of market rates: the implicit-rate part mixes refinancing, the composition of the debt and indexation."
  - question: "Does the interest burden exceed the justice budget?"
    answer: "In {dette.equiv_annee}, the most recent year for which all series are comparable, interest ({dette.interets_equiv_mdeur} billion euros) sits between public order and safety ({dette.ordre_mdeur} billion, which it exceeds) and education ({dette.education_mdeur} billion), far below health ({dette.sante_mdeur} billion). The law courts alone, in the sense of the European COFOG classification (item GF0303, not the whole Justice ministry budget), account for {dette.justice_mdeur} billion. These comparisons convey scale: no euro of interest is deemed to have been taken from any of these items."
  - question: "Has the rise in interest already cut health or education spending?"
    answer: "Not in the observed aggregates: in euros, public spending on health ({dette.sante_mdeur} billion euros in {dette.equiv_annee}) and education ({dette.education_mdeur} billion) kept rising; as a share of GDP, both are above 2019, slightly below their pandemic peak, when GDP contracted. That does not mean there was no crowding out: a budget that goes from 100 to 105 instead of 110 has not fallen, and has still been crowded out. These series allow neither an attribution of their path to the debt, nor a conclusion that they would not have been higher without the interest constraint. What they do establish: a higher burden raises the borrowing requirement under unchanged policies, and its consequences for spending, taxes and the deficit then depend on the choices made; who will absorb the adjustment is the subject of the page “Who really pays for public debt?”."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 10
  nature: "Official series (INSEE, Eurostat) and the author's calculations"
  accueil: 1
---

{{< dossier-dette volet="1" >}}

{{< reutiliser-ancre >}}

France is a useful case well beyond France itself. It is a large advanced economy where a general mechanism became unusually clear: for three decades the debt stock grew while the cost of carrying it fell, so the burden stayed quiet — and then, within a few years, the scissor began to close. What happens when that reversal arrives is now playing out in public, on a scale large enough to make the mechanism visible.

To the question **"what does the debt cost"**, the most direct figure is not the stock but the **interest due each year**: **{{< dette-val "interets_mdeur" >}} billion euros in {{< dette-val "interets_annee" >}}**, or {{< dette-val "interets_pct_pib" >}}% of GDP and **{{< dette-val "interets_sur_recettes_pct" >}}% of public revenue**: out of every 100 euros of revenue, {{< dette-val "interets_sur_recettes_pct" >}} go to interest. It is a **gross** burden, for general government as a whole (central government, local authorities, social security), recorded in the year the interest falls due (Eurostat, `D41PAY`).

## The scissor: twenty-five years of offset, then the turn

{{< figure-svg fichier="ciseau-dette-interets-en" alt="Two curves as a percentage of GDP: above, French public debt rises almost continuously since 1995; below, the interest burden of general government falls until 2020, then climbs back." >}}Public debt ({{< dette-val "dette_periode" >}}: {{< dette-val "dette_pct_pib" >}}% of GDP, INSEE, quarterly) and the interest burden of general government ({{< dette-val "interets_annee" >}}: {{< dette-val "interets_pct_pib" >}}% of GDP, Eurostat, annual). Two separate scales, one shared unit: percent of GDP.{{< /figure-svg >}}
{{< fig-actions id="ciseau" >}}

From 1995 to the turn of the 2020s the two curves open like a pair of scissors: the stock climbs from {{< dette-val "dette_1995_pct_pib" >}}% to over 100% of GDP, while the interest burden **falls** from {{< dette-val "interets_1995_pct_pib" >}}% to {{< dette-val "interets_creux_pct_pib" >}}% ({{< dette-val "interets_creux_annee" >}}, {{< dette-val "interets_creux_mdeur" >}} billion euros).

<div class="resultat-phrase">

**The result in one sentence.** From 1995 to {{< dette-val "interets_creux_annee" >}}, the debt rose from {{< dette-val "dette_1995_pct_pib" >}}% to over 100% of GDP while its interest burden fell from {{< dette-val "interets_1995_pct_pib" >}}% to {{< dette-val "interets_creux_pct_pib" >}}% of GDP: the falling average cost of the stock offset the rising stock. Since then, the two forces have been pulling in the same direction again.

</div>

<div class="equation" role="group" aria-label="The interest burden, the product of the debt stock and its average cost">
  <p class="equation__titre">What makes the bill</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>the stock</b><small>accumulated debt, constantly refinanced</small></span>
    <span class="equation__op" aria-label="times">×</span>
    <span class="equation__terme"><b>its average cost</b><small>the implicit interest rate</small></span>
    <span class="equation__op" aria-label="equals">=</span>
    <span class="equation__terme equation__terme--resultat"><b>the interest burden</b><small>due every year</small></span>
  </div>
  <p class="equation__exacte">The stock grows with deficits; the average cost follows market rates only as securities are renewed.</p>
</div>

The **implicit interest rate** is a year's interest divided by the debt outstanding at the end of the previous year. It is a proxy for the average cost of the stock, not the rate at which France borrows today. For twenty-five years its fall offset the rising stock: that is why doubling the debt did not double the bill.

## Where has the rise since the trough come from: the debt stock or the implicit rate? {#rise-since-the-trough}

{{< figure-svg fichier="charge-encours-taux-en" alt="Stacked bars by year since 2021, in billion euros: the contribution of the larger debt stock, in blue, and of the higher implicit rate, in orange, to the change in the interest burden; the 2022 bar is dominated by the implicit rate, the following years mostly by the stock." >}}Accounting decomposition of the annual change in the interest burden between the rise in the debt stock (blue) and in the implicit rate (orange), in billion euros; the black dot is the change. Computed on Eurostat and INSEE series.{{< /figure-svg >}}
{{< fig-actions id="decomp" >}}

From {{< dette-val "dec_a0" >}} to {{< dette-val "dec_a1" >}}, the interest burden rises by **{{< dette-val "dec_delta" >}} billion euros**. Since it is the product of the stock and the implicit rate, its rise splits into two parts: **{{< dette-val "dec_volume" >}} billion come from the larger stock, {{< dette-val "dec_taux" >}} from the higher implicit rate**, or {{< dette-val "dec_part_taux_pct" >}}% of the rise. That second figure measures the rise in the average cost of the stock, not the effect of market rates: it is an accounting split, which says how much each term weighed, not why the average cost rose.

**The split depends on the starting year.** Since 2019, before the pandemic, the burden has risen by {{< dette-val "dec19_delta" >}} billion, of which {{< dette-val "dec19_volume" >}} from the stock and {{< dette-val "dec19_taux" >}} from the implicit rate: the stock then weighs most, because 2020, when the average cost fell, enters the calculation. Starting from the trough enlarges the rate's share; both bases are exact, and neither alone says what "drives" the rise.

**The implicit rate made most of its move in a single year.** In {{< dette-val "dec_saut_annee" >}}, it goes from {{< dette-val "taux_saut_avant" >}}% to {{< dette-val "taux_saut_apres" >}}%, and the burden rises by {{< dette-val "dec_saut_delta" >}} billion, of which {{< dette-val "dec_saut_taux" >}} are attributed, in accounting terms, to the higher implicit rate. Inflation meanwhile raised the cost of the State's inflation-linked bonds, recorded as soon as it is due, as the [French Senate's report on that year's accounts](https://www.senat.fr/rap/l22-771-1/l22-771-17.html) notes. **But these series do not measure the share of indexation in those {{< dette-val "dec_saut_taux" >}} billion**, nor do they separate it from refinancing and other changes in the composition of the debt.

**Since {{< dette-val "dec_saut_annee" >}}, the larger stock has weighed most.** From {{< dette-val "dec_saut_annee" >}} to {{< dette-val "dec_a1" >}}, the burden rises by a further {{< dette-val "dec_apres_delta" >}} billion, of which {{< dette-val "dec_apres_volume" >}} from the stock and {{< dette-val "dec_apres_taux" >}} from the implicit rate, which now rises only slowly.

**Why the average cost rose, these series cannot separate.** Its rise mixes three possible causes: securities renewed at higher rates, a differently composed debt, indexation to inflation. The indexation amounts published for the State cannot be added to this calculation, which covers general government as a whole.

## Why do market rates not pass through at once? {#transmission}

{{< figure-svg fichier="taux-marche-apparent-en" alt="Two curves in percent per year, on the same scale: the 10-year rate and the implicit interest rate on French public debt stay close until the early 2010s; then the 10-year rate falls to zero and climbs back sharply, while the implicit rate falls less far and rises more slowly." >}}The 10-year yield, an annual average and a reference indicator of borrowing conditions (not the actual cost of issuance), and the implicit rate, the average cost of the whole stock, on the same scale — Eurostat <code>irt_lt_mcby_a</code> and <code>gov_10a_main</code>, INSEE.{{< /figure-svg >}}
{{< fig-actions id="marche" >}}

A given year's interest pays for securities issued at different dates, at different rates. The implicit rate therefore follows market rates only as securities are renewed: it went from about {{< dette-val "taux_apparent_premier" >}}% in {{< dette-val "taux_apparent_premier_annee" >}} to {{< dette-val "taux_apparent_creux" >}}% in {{< dette-val "taux_apparent_creux_annee" >}}, not as low as the 10-year rate, and is back only to {{< dette-val "taux_apparent_dernier" >}}% in {{< dette-val "taux_apparent_dernier_annee" >}}, when the 10-year rate stands at {{< dette-val "taux_marche_dernier" >}}%: a security renewed at that rate costs more than the stock's average. **As long as old securities, issued at low rates, mature and are renewed at higher ones, the average cost can keep rising even if market rates settle.**

**Two mechanisms, two speeds.** Inflation-linked bonds pass inflation on to the burden within the year; the renewal of securities passes market rates on only as they mature, over several years. Both show up in the same interest figures, and these series do not separate them.

**Three benchmarks measure these two channels** — for the State's debt, while the burden on this page covers general government as a whole: they give the order of magnitude of the lag, not its exact timetable.

- **The average maturity** of the State's negotiable debt: {{< dette-val "aft_dvm_ans" >}} years and {{< dette-val "aft_dvm_jours" >}} days at {{< dette-val "aft_date" >}} (Agence France Trésor). It does not mean waiting {{< dette-val "aft_dvm_ans" >}} years: part of the securities mature every year, and short-term bills are renewed within months.
- **Inflation-linked bonds**: {{< dette-val "aft_indexes_mdeur" >}} billion out of {{< dette-val "aft_encours_mdeur" >}} at the same date, or {{< dette-val "aft_part_indexes_pct" >}}%. Their cost follows prices without waiting for repayment: according to the Government, as reported by the Haut Conseil des finances publiques, one more point of inflation adds about {{< dette-val "sens_inflation_mdeur" >}} billion to the burden in the same year.
- **Sensitivity to rates**: according to the same source, a permanent one-point rise in all rates would add {{< dette-val "sens_taux_an1_mdeur" >}} billion to the burden in the first year and {{< dette-val "sens_taux_an2_mdeur" >}} in the second, then more as securities are renewed. This is a sensitivity scenario, not a forecast.

<details class="repli"><summary>The implicit rate alone, from {{< dette-val "taux_apparent_premier_annee" >}} to {{< dette-val "taux_apparent_dernier_annee" >}}: a twenty-five-year fall, a low in {{< dette-val "taux_apparent_creux_annee" >}}, a jump in {{< dette-val "dec_saut_annee" >}}</summary>

{{< figure-svg fichier="taux-apparent-dette-en" alt="A single curve in percent per year: the average cost of the French public debt stock falls for nearly twenty-five years to its minimum, then climbs back, mostly through a jump in 2022." >}}<strong>Implicit interest rate</strong>: a year's interest divided by the debt outstanding on 31 December of the previous year — computed from Eurostat (<code>gov_10a_main</code>) and INSEE series. The apparent cost Eurostat publishes uses the year's average debt instead. The full series is in <a href="/dette_officielle.json">dette_officielle.json</a>.{{< /figure-svg >}}
{{< fig-actions id="taux" >}}

</details>

## Is that a lot? {#is-that-a-lot}

**The level is not unprecedented; the rise is fast.** As a share of GDP, the burden went from {{< dette-val "interets_creux_pct_pib" >}}% in {{< dette-val "interets_creux_annee" >}} to {{< dette-val "interets_pct_pib" >}}% in {{< dette-val "interets_annee" >}}. As a share of GDP ({{< dette-val "interets_pct_pib" >}}%), the {{< dette-val "interets_annee" >}} burden is back to its {{< dette-val "niv_pib_annee" >}} level; as a share of public revenue ({{< dette-val "interets_sur_recettes_pct" >}}%), to its {{< dette-val "niv_rec_annee" >}} level. In 1995 it amounted to {{< dette-val "interets_1995_pct_pib" >}}% of GDP and {{< dette-val "interets_1995_sur_recettes_pct" >}}% of revenue. But since the {{< dette-val "interets_creux_annee" >}} trough it has risen by {{< dette-val "interets_hausse_pct" >}}% in euros, and by {{< dette-val "interets_hausse_2019_pct" >}}% since 2019: both baselines lead to the same conclusion. The two findings hold together, and answer "the debt costs almost nothing" as well as "debt has never cost so much".

{{< figure-svg fichier="charge-interets-mdeur-en" alt="One curve in billion euros at current prices since 1995: the interest burden hovers for a long time, falls to its 2020 trough, then climbs steeply; two open circles, not joined to the curve, show the Government's forecast." >}}Eurostat, interest due by general government, at current prices not adjusted for inflation; open circles: Government forecast, on a base not reconciled with Eurostat.{{< /figure-svg >}}
{{< fig-actions id="charge" >}}

**Gross, then net.** General government also receives interest: {{< dette-val "interets_recus_mdeur" >}} billion in {{< dette-val "interets_annee" >}}. The balance between interest due and interest received is {{< dette-val "interets_nets_mdeur" >}} billion, up {{< dette-val "interets_nets_hausse_pct" >}}% since {{< dette-val "interets_creux_annee" >}}: the conclusion does not change. That balance is not a "net economic cost" of the debt; it only deducts the interest received.

<details class="repli"><summary>About €{{< interets-par-foyer >}} of interest per tax household: an arithmetic division, neither a tax each household owes nor the actual distribution of the burden</summary>

**On the scale of a household.** Divided among France's {{< interets-par-foyer "foyers" >}} million tax households ({{< interets-par-foyer "periode" >}}, DGFiP), the {{< dette-val "interets_annee" >}} interest burden comes to about €{{< interets-par-foyer >}} per household. This is a notional, uniform division of the total: it is not a tax owed by each household, and it says nothing about who bears the burden — households, firms and non-residents contribute to public revenue in proportions this calculation ignores. Who bears it is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

</details>

<h3 id="compared-magnitudes">{{< dette-val "interets_equiv_mdeur" >}} billion euros of interest in {{< dette-val "equiv_annee" >}}: what order of magnitude?</h3>

In **the same year**, {{< dette-val "equiv_annee" >}} (spending by function is published with close to a two-year lag), interest ({{< dette-val "interets_equiv_mdeur" >}} billion euros) amounted to **{{< dette-val "interets_sur_recettes_equiv_pct" >}}% of public revenue**. It sits between **public order and safety (GF03, {{< dette-val "ordre_mdeur" >}} billion)**, which it exceeds, and **education (GF09, {{< dette-val "education_mdeur" >}} billion)**, of which it represents about {{< dette-val "pct_interets_education" >}}%, far below **health (GF07, {{< dette-val "sante_mdeur" >}} billion)**, about {{< dette-val "pct_interets_sante" >}}%. Against the law courts alone (GF0303, {{< dette-val "justice_mdeur" >}} billion, not the whole Justice ministry budget), the interest burden is about {{< dette-val "ratio_interets_justice" >}} times larger.

{{< figure-svg fichier="masses-comparees-en" alt="Four curves in billion euros at current prices since 1995: health and education rise steadily and stay the highest; the interest burden, long flat then falling, climbs after 2020 and moves back above the public order and safety function." >}}Eurostat, interest due and general government expenditure by function. Every series stops at the same vintage.{{< /figure-svg >}}
{{< fig-actions id="masses" >}}

**Since the {{< dette-val "creux_ref_annee" >}} trough, the burden has risen faster than each of the nine other main functions of spending**: +{{< dette-val "croiss_interets_depuis_creux_pct" >}}%, against +{{< dette-val "croiss_max_autres_pct" >}}% for the fastest of them ({{< dette-val "croiss_max_autres_nom" >}}). The tenth, general public services, contains interest itself. Over the whole period it was the other way round: falling rates lightened the bill while public spending rose.

<details class="repli"><summary>Caveat: these comparisons set masses side by side, not causes — no euro of interest is deemed to have been taken from health, education or the courts</summary>

Interest is a **type** of spending, the other three are **functions**. Not the same breakdown — interest sits inside the general public services function — and the comparison does not say that a euro of interest was taken from any of these budgets: it conveys scale, a weight relative to public resources.

</details>

## What stock does this bill pay for? {#stock-paid-for}

This bill pays for a stock: the accumulated **debt**, the figure most often quoted. How it built up (what it owes to deficits, interest and growth) is the subject of the first part of the file, [Why does public debt rise?](/en/why-does-public-debt-rise/)

{{< dette-chiffres historique="true" >}}
{{< fig-actions id="longue" >}}

Since {{< dette-val "hist_annee_debut" >}}, French public debt has gone from {{< dette-val "hist_pct_debut" >}}% to {{< dette-val "dette_pct_pib" >}}% of GDP, multiplied by {{< dette-val "hist_multiple" >}}. It climbs in steps: the main jumps **coincide with crises**, then the **persistence of deficits** prevents the step from being undone; in the observed series, the ratio has never returned to its level of ten years earlier. On INSEE's quarterly series, available since 1995, the highest ratio is reached in {{< dette-val "dette_pic_periode" >}} ({{< dette-val "dette_pic_pct_pib" >}}%).

<details class="repli"><summary>The thresholds since {{< dette-val "hist_annee_debut" >}}: 30, 60, 80 then 100% of GDP, crossed after the oil shocks, the 1993 recession, the financial crisis and the pandemic</summary>

- **{{< dette-val "hist_annee_debut" >}} — {{< dette-val "hist_pct_debut" >}}%.** Thirty years of strong growth and inflation had diluted the post-war debt: the state repaid in a currency that was losing its value. The lightning deleveraging usually credited to post-Liberation inflation, however, needs revising: by bringing back the black-market prices that the official index ignored, Baubeau and Teixeira show that prices rose far more during the war, and less afterwards, than was believed; relative to national income, the debt therefore swelled less during the conflict, and melted less afterwards ([*Economic History Review*, 2026](https://doi.org/10.1111/ehr.70127)).
- **{{< dette-val "hist_seuil_30_annee" >}} — 30%.** After the two oil shocks growth slowed while spending did not: the deficit became permanent, not through any datable decision, but because it no longer closed between two slowdowns.
- **{{< dette-val "hist_seuil_60_annee" >}} — 60%.** The 1993 recession widened the gap; the Maastricht Treaty, signed in 1992 and in force since November 1993, had made 60% the European reference value. Debt crossed it in {{< dette-val "hist_seuil_60_annee" >}} and fell back below it only in {{< dette-val "hist_sous60_annees" >}}.
- **{{< dette-val "hist_seuil_80_annee" >}} — 80%.** The financial crisis cut revenue and forced support plans: {{< dette-val "hist_choc_crise_pts" >}} more points of GDP between the end of {{< dette-val "hist_choc_crise_debut" >}} and the end of {{< dette-val "hist_seuil_80_annee" >}}. The recovery that followed did not win them back.
- **{{< dette-val "hist_seuil_100_annee" >}} — 100%.** The shutdown of the economy and income support added {{< dette-val "hist_choc_sanitaire_pts" >}} points in a single year. Debt passed the size of GDP.
- **{{< dette-val "dette_periode" >}} — {{< dette-val "dette_pct_pib" >}}%.** The stock remains on an upward trend, and its average cost has been rising since its {{< dette-val "taux_apparent_creux_annee" >}} low, mostly through the {{< dette-val "dec_saut_annee" >}} jump.

</details>

## Can the bill rise if the debt stops growing? {#what-the-bill-does-not-tell-you-is-the-debt-rising}

**Yes, but "the debt stops growing" can mean two things.** If the stock in euros stopped growing, the burden could keep rising: old securities, issued at low rates, would gradually be replaced by costlier ones. If only the debt-to-GDP ratio stabilises, a second mechanism adds to the first: with nominal GDP growth, the debt still rises in euros, and its burden with it, even at a constant implicit rate — while its weight in GDP would stay roughly stable. Stabilising the debt in euros and stabilising its weight in the economy are not the same thing. What drives the ratio up (deficits, interest, growth) is the subject of the first part of the file, [Why does public debt rise?](/en/why-does-public-debt-rise/)

**What the Government forecasts.** According to the Government's scenario presented to the Haut Conseil des finances publiques for the {{< dette-val "prev_edition" >}} budget bill, interest would reach {{< dette-val "prev_charge_n_mdeur" >}} billion euros in {{< dette-val "prev_n_annee" >}}, then {{< dette-val "prev_charge_n1_mdeur" >}} billion in {{< dette-val "prev_n1_annee" >}}, or {{< dette-val "prev_charge_n1_pct_pib" >}}% of GDP, the {{< dette-val "prev_niveau_annee" >}} level, while debt would reach {{< dette-val "prev_dette_n1_pct_pib" >}}% of GDP at the end of {{< dette-val "prev_n1_annee" >}}, {{< dette-val "prev_dette_revision_pts" >}} points more than in the {{< dette-val "prev_edition_prec" >}} budget bill. The Haut Conseil, the independent fiscal council charged by law with assessing how realistic these forecasts are, considers that the burden could exceed that amount if inflation or interest rates rose further. It also notes that the burden forecast for {{< dette-val "prev_n_annee" >}} exceeds the initial budget act by {{< dette-val "prev_ecart_lfi_mdeur" >}} billion euros, mainly because of inflation-linked bonds: indexation is not a 2022 story only.

**These forecasts do not extend the observed curve.** The Haut Conseil writes that the {{< dette-val "prev_n1_annee" >}} burden would be "more than {{< dette-val "prev_hausse_plus_de_mdeur" >}} billion euros higher than in 2025", which implies a 2025 base below Eurostat's {{< dette-val "interets_mdeur" >}} billion: the two series are not reconciled. On the charts, the forecast is drawn as open circles, not joined to the curve, and no rise between observed and forecast values is computed by subtraction.

## What the data does not show

**Observed health and education spending has not fallen.** In euros, both kept rising. As a share of GDP, both are above 2019 (health: {{< dette-val "sante_pct_2019" >}}% then {{< dette-val "sante_pct_equiv" >}}% in {{< dette-val "equiv_annee" >}}; education: {{< dette-val "education_pct_2019" >}}% then {{< dette-val "education_pct_equiv" >}}%), slightly below their pandemic peak ({{< dette-val "sante_pct_pic" >}}% in {{< dette-val "sante_pic_annee" >}} for health), when GDP contracted. Anyone claiming that debt has "already cut" those budgets is saying more than the data does. But the reverse does not follow either: these series allow **neither an attribution of their path to the debt, nor a conclusion that they would not have been higher** without the interest constraint. A budget that goes from 100 to 105 instead of 110 has not fallen, and has still been crowded out. No counterfactual, no causal claim — in either direction.

<details class="repli"><summary>Rising budgets, services under strain: a plausible explanation (labour costs, Baumol's cost disease, growing needs) that these series do not demonstrate</summary>

Hence an apparent paradox: if budgets rise, why do hospitals, schools and courts seem starved? The most common explanation — **plausible, but not demonstrated by the series on this page** — rests on two standard mechanisms. Public services rely heavily on human labour: their costs track wages, not the productivity gains of machines (Baumol's cost disease, a standard result in the economics of services — its magnitude varies by sector). Demand for some of them may also grow faster than GDP: ageing and costly medical progress in health, litigation in justice. If both mechanisms hold, a spending category that remains stable as a share of GDP **does not guarantee** a stable volume or quality of service. Establishing that it actually fell would require what this page does not measure: sectoral inflation, wages, productivity, demographics, and the volumes actually delivered.

</details>

What the data does establish is narrower: a higher interest burden **raises the borrowing requirement under unchanged policies**; its consequences for spending, taxes and the deficit then depend on the choices made, the economic cycle and the financing available — which is not the same as saying that every euro of interest is a euro taken from health or education. The question is therefore not "are budgets falling?" but "**who will absorb the adjustment**": higher taxes, cuts to other spending, wider deficits, inflation, or future generations. That is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

**An interpretative hypothesis of the author's, distinct from the findings.** Within the framework of anthropy, which the author sets out in the working paper [AWP-07 — *The anthropic loop*](/en/awp/awp-07/), applied to debt in [AWP-03](/en/awp/awp-03/), this sequence can be read as a cost displaced in time and then returning: displacement, saturation, return. The series on this page establish the fall and then the rise of the burden and of its average cost; they do not test that reading, nor do they say that the return was inevitable or how large it will be. Comparing the cost of new issuance with the average cost of the stock, as the working paper [AWP-09](/en/awp/awp-09/) proposes, measures delayed transmission; on its own, it does not distinguish this reading from an ordinary financial explanation based on the maturity of the debt. Testing it would require a prediction of its own.

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## What to take away

**Why the bill long fell.** For twenty-five years, the falling average cost of the stock offset the rising stock: the debt doubled as a share of GDP, its burden fell.

**Why it is rising.** Since {{< dette-val "dec_a0" >}}, stock and average cost have risen together: {{< dette-val "dec_volume" >}} billion of the rise come from the stock, {{< dette-val "dec_taux" >}} from the implicit rate, most of it in {{< dette-val "dec_saut_annee" >}}, the year inflation also raised the cost of indexed bonds, without these series measuring its share; since 2019, the stock weighs most. The level reached is not unprecedented (the {{< dette-val "niv_pib_annee" >}} level as a share of GDP); the rise, though, is fast.

**Why it can go on.** The average cost catches up with market rates only as securities are renewed: the bill can rise even as the debt stops growing. The {{< dette-val "interets_mdeur" >}} billion are not subtracted from any single budget: under unchanged policies, they raise the borrowing requirement, and choices decide the rest.

<details class="repli"><summary>Rule: each comparison uses a single year — {{< dette-val "equiv_annee" >}} for the magnitudes, {{< dette-val "interets_annee" >}} for the latest burden — never two years mixed</summary>

One rule governs every comparison on this page: **the most recent common vintage, the same for every term**. Since spending by function is published with close to a two-year lag, the compared magnitudes are for {{< dette-val "equiv_annee" >}}, while the most recent interest figure is for {{< dette-val "interets_annee" >}}. Both years are stated, never mixed.

</details>

</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}

Which leaves a question these figures do not settle: who ultimately bears this burden, and is part of its cost shifted onto others? That is the subject of the next page.

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page prices the bill. It does not say who settles it — and that is where everything is decided: a debt is never cancelled, and its cost can be shifted — onto the taxpayer, onto the saver through inflation, onto public services whose resources are squeezed, onto those who cannot yet vote — depending on the decisions taken to adjust it. The book follows each of these channels in turn, on official figures, and ends in scenarios for 2025-2035. By the end you will recognise which one is unfolding.
{{< /appel-livre >}}

## Where these figures come from

The figures on this page are **derived automatically from official sources** (INSEE, Eurostat), never copied by hand, and re-queried every week; last retrieval that changed a value: {{< dette-val "releve_le" >}}. Two families of values are entered by hand, with their source and date: the Government's forecasts and the Agence France Trésor benchmarks. Open data: [dette_officielle.json](/dette_officielle.json), CC BY 4.0 licence.

<details class="repli"><summary>INSEE and Eurostat series, interest on an accrual basis, implicit rate on the stock at the end of the previous year, dated values entered by hand; compilation under a CC BY 4.0 licence</summary>

Values **derived automatically from official sources**: quarterly Maastricht debt from INSEE (series [010777616](https://www.insee.fr/fr/statistiques/serie/010777616) — stock in billions of euros — and [010777608](https://www.insee.fr/fr/statistiques/serie/010777608) — % of GDP); interest due (D41PAY), interest received (D41REC) and total revenue (TR) of general government ([Eurostat, `gov_10a_main`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=en)); expenditure by COFOG function, including the ten main functions ([Eurostat, `gov_10a_exp`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table?lang=en)); the 10-year yield ([Eurostat, `irt_lt_mcby_a`](https://ec.europa.eu/eurostat/databrowser/view/irt_lt_mcby_a/default/table?lang=en)). The implicit rate is a year's interest over the stock at the end of the previous year; the decomposition of the rise in the burden splits the change between stock and implicit rate using midpoint contributions. The interest burden used here is the `D41PAY` series, recorded on an accrual basis — attributed to the year the interest falls due, not the date of payment, which brings the indexation of inflation-linked bonds in as soon as it accrues — and covering the same universe, general government as a whole, as the revenue it is set against; INSEE's accounts present interest before the FISIM adjustment (financial intermediation services indirectly measured) and report a slightly different amount for the same year: two closely related conventions, not two contradictory measurements.

**Values entered by hand.** The Government's forecasts for {{< dette-val "prev_n_annee" >}} and {{< dette-val "prev_n1_annee" >}} and its sensitivity to rates and inflation are read in the [opinion of the Haut Conseil des finances publiques on the {{< dette-val "prev_edition" >}} budget bills](https://www.hcfp.fr/liste-avis/avis-ndeg2026-5-lois-de-finances-2027) (paragraphs 113, 115 and 116), which reports them; the opinion is archived with its fingerprint. They are not subtracted from the Eurostat observation: the 2025 value underlying the forecasts is not reconciled with the series used here. The average maturity and the inflation-linked bonds of the State's negotiable debt are those published by the [Agence France Trésor](https://www.aft.gouv.fr/fr/principaux-chiffres-dette) for {{< dette-val "aft_date" >}}.

The official series are re-queried every week; the retrieval date changes only when a release changes a figure. The consolidated data is published openly as [dette_officielle.json](/dette_officielle.json) under a [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) licence — free reuse, including commercial use, on the single condition that the source is cited. The raw series belong to INSEE and Eurostat; what is licensed here is the compilation: the assembly of series, the derived quantities (implicit rate, decomposition, ratios, single-vintage equivalences) and their reconciliation.

</details>

The framework used to interpret these figures is set out in [What is anthropy?](/en/quest-ce-que-lanthropie/) and in the book [*ANTHROPY — A Big History of Civilization's Hidden Costs*](/en/livres/anthropie-ordre-ici-dette-ailleurs/). The book-length treatment of French public debt, *Dette Publique&nbsp;: Qui paie vraiment&nbsp;?*, exists in French only.

{{< reutiliser figures="figures_dette" jeu="dette_officielle" sources="INSEE and Eurostat" >}}
This page measures what public debt costs each year — the interest burden, {{< dette-val "interets_mdeur" >}} billion euros in {{< dette-val "interets_annee" >}} — rather than the size of the stock. It shows why a stock twice as heavy did not double the bill, breaks down the rise since {{< dette-val "dec_a0" >}} between the larger stock and the higher implicit rate (an accounting decomposition, not a measure of the effect of market rates), places the level reached in the long series and explains why the bill can keep rising even as the debt stops growing. It compares magnitudes on one perimeter and one vintage, without establishing that a euro of interest was taken from another budget.
{{< /reutiliser >}}

{{< canonical-definition >}}
