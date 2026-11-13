---
title: "Is the world economy decoupling from energy?"
url: "/en/decoupling-energy-growth/"
description: "From {dc.an0} to {dc.an1}, the energy used per unit of world GDP, measured at purchasing power parity, fell by {dc.di_pct}%, and energy consumption rose by {dc.de_pct}%. In the decomposition, the GDP-per-head effect exceeds the population effect; in the European Union, consumption fell on its territory (EIA, author's calculation)."
chapo: "The world economy uses less energy for each unit of output it produces, measured by GDP at purchasing power parity: {dc.di_pct}% less in {dc.an1} than in {dc.an0}. But over the same period, that GDP rose by {dc.dy_pct}%, and energy consumption by {dc.de_pct}%: the decoupling is relative, not absolute."
date: 2026-10-26
lastmod: 2026-11-12
journal:
  - {date: 2026-10-26, texte: "Correction: the check recalculation relied on an Our World in Data primary energy series using the substitution method, wrongly attributed to the Energy Institute, which adopted the physical energy content method in 2025; it now relies on the Energy Institute's total energy supply (EU fall from 2000 to 2024: 17% instead of 12%). The EIA convention is checked for wind as for hydro, not for solar. Added: a variant with GDP at market exchange rates, a comparison with Eurostat; “income per head” becomes “GDP per head”."}
  - {date: 2026-11-12, texte: "Revision: the decomposition presented as an accounting one, with no counterfactual (chart title and note, standfirst); measurement convention and changes in the energy mix among the possible explanations of the European fall; the three producers compared over 2000-2024, with Eurostat's complete energy balances; Brockway et al. rendered faithfully, and the page states that an aggregate intensity does not measure efficiency; the observation shared with them is limited to the world level; the chart gives the fall in intensity itself; solar is removed from the electricity said to be counted at its electrical content."}
og_title: "Is the world economy decoupling from energy? — S. Lalut"
og_image: "images/og-decouplage-en.jpg"
og_image_alt: "Share card: “Energy intensity falls, world consumption rises” — accounting decomposition of the change in world energy consumption into contributions from population, GDP per head and energy intensity, with GDP at purchasing power parity (EIA)."
donnees: [decouplage]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "decouplage"
  apropos: "decoupling of energy consumption from economic growth"
  nom: "Energy consumption, GDP and population, world and European Union, and decomposition of the change in consumption (EIA)"
  description: "Primary energy consumption, GDP at purchasing power parity in constant prices and population, world and EU-27, annual EIA series; decomposition of the change in consumption from {dc.an0} to {dc.an1} into population, GDP-per-head and energy-intensity effects (Divisia index), computed by the author, with a recalculation using Energy Institute and World Bank data, a variant at market exchange rates and a comparison with Eurostat for the European Union."
  couverture_temporelle: "1980/{dc.an1}"
  couverture_spatiale: "World; European Union (27 countries)"
  variables:
    - {nom: "Primary energy consumption", unite: "terajoules", description: "EIA convention, by area and year"}
    - {nom: "GDP at purchasing power parity", unite: "billion dollars, constant prices", description: "by area and year"}
    - {nom: "Population", unite: "thousand people", description: "by area and year"}
  sources:
    - "https://www.eia.gov/international/data/world"
    - "https://www.energyinst.org/statistical-review"
    - "https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.KD"
    - "https://data.worldbank.org/indicator/NY.GDP.MKTP.KD"
    - "https://ec.europa.eu/eurostat/databrowser/view/nrg_bal_c/default/table"
  mots: ["decoupling", "energy intensity", "energy consumption", "energy efficiency", "rebound effect", "Jevons paradox", "energy transition", "sufficiency", "primary energy", "GDP", "EIA"]
  fichiers: ["decouplage.csv", "decouplage.json"]
faq:
  - question: "Is world energy consumption falling?"
    answer: "No. From {dc.an0} to {dc.an1}, world primary energy consumption went from {dc.e0} to {dc.e1} exajoules according to the EIA, a rise of {dc.de_pct}%, while the energy used per unit of GDP, measured at purchasing power parity, fell by {dc.di_pct}%. This is relative decoupling: consumption grows more slowly than the economy, without falling."
  - question: "Does the rise in energy consumption come mainly from population growth?"
    answer: "Not primarily, in accounting terms: in a decomposition of the rise in world energy consumption from {dc.an0} to {dc.an1}, with GDP at purchasing power parity, the GDP-per-head effect ({dc.rev_ej} exajoules) weighs {dc.ratio_rp} times as much as the population effect ({dc.pop_ej}), and the energy-intensity effect takes away {dc.int_ej}. The decomposition says how much each term weighed, not why."
  - question: "Can a country or region use less energy while getting richer?"
    answer: "Yes, on its territory: in the European Union, according to the EIA, primary energy consumption fell by {dc.ue_de_pct}% from {dc.an0} to {dc.an1} while GDP rose by {dc.ue_dy_pct}%, and more than half of that fall came after 2019. These data do not count the energy embodied in imported goods; nor do they say whether the fall comes from efficiency, from a change in the structure of the economy, from production moving outside the EU or from the way the measurement convention counts electricity."
  - question: "Where do these figures come from?"
    answer: "From EIA international data (energy, GDP at purchasing power parity in constant prices, population), retrieved by a script that stops if a figure no longer meets the conditions on which the page's main sentences depend; the figures are recalculated using Energy Institute, World Bank and Eurostat data. Only one value is transcribed by hand: the world total published by the Energy Institute for {dc.an_ei_publie}, used to verify the provenance of the data behind the recalculation. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]
  conception: "docs/conception/decouplage-energie-croissance.md"
  refonte: "2026-11-12"
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]
  rang: 50
  nature: "Public data recalculated (EIA, Energy Institute, World Bank)"
reperes:  # three key results under the standfirst, from 600 px wide (partials/reperes-page.html ; règle 17 du site,
  # reprise du style du 13/11/2026, test du premier écran). Same results, periods and tokens as the French page.
  - ancre: "paradox"
    fort: "+{dc.de_pct}%"
    texte: "in primary energy consumption worldwide from {dc.an0} to {dc.an1} according to the EIA, with GDP up {dc.dy_pct}% at purchasing power parity: the decoupling is relative, not absolute"
  - ancre: "population-income"
    fort: "The weight of GDP per head"
    texte: "is {dc.ratio_rp} times that of population in the accounting decomposition of the rise in world energy consumption, from {dc.an0} to {dc.an1} (GDP at purchasing power parity)"
  - ancre: "european-union"
    fort: "−{dc.ue_de_pct}%"
    texte: "in primary energy consumption in the EU-27, on its territory, from {dc.an0} to {dc.an1} according to the EIA (−{dc.es_es_pct}% according to Eurostat), with GDP up {dc.ue_dy_pct}% at purchasing power parity"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data last updated {{< dc-val "date_donnees" >}}</span> EIA, international data: primary energy consumption, GDP at purchasing power parity in constant prices and population, the world and the European Union, 1980 to {{< dc-val "an1" >}}. Download: <a href="/decouplage.csv">CSV</a> · <a href="/decouplage.json">JSON</a></p>

## Intensity falls, consumption rises {#paradox}

From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world GDP, measured at purchasing power parity in constant prices, rose by {{< dc-val "dy_pct" >}}%. The energy used per unit of that GDP — energy intensity — fell by {{< dc-val "di_pct" >}}%. And world primary energy consumption went from {{< dc-val "e0" >}} to {{< dc-val "e1" >}} exajoules (one exajoule is 10¹⁸ joules): {{< dc-val "de_pct" >}}% more.

The world economy has therefore decoupled from energy in the relative sense: its energy consumption grows more slowly than its output. It has not decoupled in the absolute sense, in which consumption falls while the economy grows.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/decouplage-decomposition-en-m.svg" width="300" height="988">
    <img src="/img/decouplage-decomposition-en.svg" alt="Accounting decomposition of the change in primary energy consumption from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, as % of {{< dc-val "an0" >}} consumption, with GDP at purchasing power parity. World: population effect {{< dc-val "w_pop_pct" >}}% (population: {{< dc-val "w_var_pop" >}}%), GDP-per-head effect {{< dc-val "w_rev_pct" >}}% (GDP per head: {{< dc-val "w_var_rev" >}}%), energy-intensity effect {{< dc-val "w_int_pct" >}}% (energy per unit of GDP: {{< dc-val "w_var_int" >}}%), change in consumption {{< dc-val "w_tot_pct" >}}%. European Union: population effect {{< dc-val "u_pop_pct" >}}% (population: {{< dc-val "u_var_pop" >}}%), GDP-per-head effect {{< dc-val "u_rev_pct" >}}% (GDP per head: {{< dc-val "u_var_rev" >}}%), energy-intensity effect {{< dc-val "u_int_pct" >}}% (energy per unit of GDP: {{< dc-val "u_var_int" >}}%), change in consumption {{< dc-val "u_tot_pct" >}}%." width="720" height="455" loading="lazy">
  </picture>
  <figcaption>Territorial primary energy consumption, EIA convention; effects computed with a Divisia index; they add up exactly to the change (EIA, international data).</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**The result in one sentence.** From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world energy consumption rose by {{< dc-val "de_pct" >}}%: the accounting decomposition, with GDP at purchasing power parity, attributes an increase of {{< dc-val "poussee_ej" >}} exajoules to population and GDP per head, and a decrease of {{< dc-val "int_ej" >}} to energy intensity — shares of a calculation, not the additional amount that would have been consumed without the fall in intensity.

</div>
</div>
</div>

## Population or growing wealth? {#population-income}

One might think that energy consumption rises mainly because the world's population is growing. An accounting decomposition separates the population effect from the GDP-per-head effect.

Energy consumption is the product of three quantities: population, GDP per head and the energy used per unit of GDP. From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, the decomposition attributes {{< dc-val "pop_ej" >}} exajoules to the population effect, {{< dc-val "rev_ej" >}} to the GDP-per-head effect and −{{< dc-val "int_ej" >}} to the intensity effect: {{< dc-val "tot_ej" >}} exajoules more in all.

With GDP at purchasing power parity, the GDP-per-head effect therefore weighs {{< dc-val "ratio_rp" >}} times as much as the population effect. That ranking holds for every starting year tested: in each of the windows (starting in {{< dc-val "fenetres" >}}, all ending in {{< dc-val "an1" >}}), the GDP-per-head effect exceeds the population effect, and consumption rises.

<details class="repli">
<summary>The five windows, in exajoules</summary>

| Start | Population effect | GDP-per-head effect | Intensity effect | Change in consumption |
|---|---|---|---|---|
| 1990 | {{< dc-val "f1990_pop" >}} | {{< dc-val "f1990_rev" >}} | {{< dc-val "f1990_int" >}} | {{< dc-val "f1990_tot" >}} |
| 2000 | {{< dc-val "f2000_pop" >}} | {{< dc-val "f2000_rev" >}} | {{< dc-val "f2000_int" >}} | {{< dc-val "f2000_tot" >}} |
| 2010 | {{< dc-val "f2010_pop" >}} | {{< dc-val "f2010_rev" >}} | {{< dc-val "f2010_int" >}} | {{< dc-val "f2010_tot" >}} |
| 2015 | {{< dc-val "f2015_pop" >}} | {{< dc-val "f2015_rev" >}} | {{< dc-val "f2015_int" >}} | {{< dc-val "f2015_tot" >}} |
| 2019 | {{< dc-val "f2019_pop" >}} | {{< dc-val "f2019_rev" >}} | {{< dc-val "f2019_int" >}} | {{< dc-val "f2019_tot" >}} |

Each window ends in {{< dc-val "an1" >}}; world, EIA. Values rounded to the nearest exajoule: their sum may differ from the total by one.

</details>

**An accounting decomposition is not an explanation.** It says how much each term weighed, not why. It does not say that getting richer causes the rise in consumption, nor that falling intensity comes from more efficient energy use: intensity also falls when the economy shifts towards services, or when wind or hydro electricity, counted at its electrical content, replaces fuels counted at their heat content. Nor can it be used to estimate a rebound effect.

<details class="repli">
<summary>Why an effect, as a share of starting consumption, differs from the change in its factor</summary>

The {{< dc-val "di_pct" >}}% measures the change in intensity; the {{< dc-val "int_ej" >}} exajoules, its contribution to the change in consumption. The decomposition measures each change in logarithmic terms, which makes the sum of the effects exact. Intensity was multiplied by {{< dc-val "ratio_i" >}} (a fall of {{< dc-val "di_pct" >}}%); the natural logarithm of that ratio is {{< dc-val "ln_i" >}}. That value is applied to a reference consumption, known as the logarithmic mean of {{< dc-val "e0" >}} and {{< dc-val "e1" >}}, that is, {{< dc-val "lmoy_ej" >}} exajoules: hence an effect of −{{< dc-val "int_ej" >}} exajoules. Expressed as a share of the {{< dc-val "e0" >}} exajoules of {{< dc-val "an0" >}} (computed on unrounded values), it amounts to {{< dc-val "int_pct_e0" >}}%, the figure in the chart: it is the same fall in intensity, measured on a larger base, not a second fall. The other two effects also differ from the change in their factor, in either direction, for the same reason (logarithm and reference consumption): {{< dc-val "w_var_pop" >}}% for population and an effect of {{< dc-val "w_pop_pct" >}}%; {{< dc-val "w_var_rev" >}}% for GDP per head and an effect of {{< dc-val "w_rev_pct" >}}%.

</details>

## The European Union: absolute decoupling, on its territory {#european-union}

The same producer, using the same definition, shows the other case for the EU-27. From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, its primary energy consumption fell by {{< dc-val "ue_de_pct" >}}%, from {{< dc-val "ue_e0" >}} to {{< dc-val "ue_e1" >}} exajoules, while its GDP rose by {{< dc-val "ue_dy_pct" >}}%; consumption peaked in {{< dc-val "an_pic_ue" >}}. The population effect adds {{< dc-val "ue_pop_ej" >}} exajoules and the GDP-per-head effect {{< dc-val "ue_rev_ej" >}}; the intensity effect, for a {{< dc-val "ue_di_pct" >}}% fall in intensity, takes away {{< dc-val "ue_int_ej" >}}: more than the other two combined.

<div class="cartes-paire">
<div class="carte-point">
<p class="carte-point__titre">The end year matters</p>

If the window ends in 2019, before the pandemic and the 2022 surge in energy prices, European consumption falls by {{< dc-val "ue19_de_pct" >}}% from {{< dc-val "an0" >}}, with GDP up {{< dc-val "ue19_dy_pct" >}}%. Absolute decoupling is already visible over that period, but more than half of the fall measured to {{< dc-val "an1" >}} came after 2019; these data do not say how much of it will last.

</div>
<div class="carte-point">
<p class="carte-point__titre">What the comparison does not say</p>

These figures count the energy consumed on EU territory, not the energy used to make the goods the EU imports. They cannot show whether the fall comes from efficiency, from the decline of the most energy-intensive industries, from their relocation outside the EU, or from the way the measurement convention counts nuclear, wind and solar electricity, whose mix has changed. Measuring the share attributable to relocation would require an energy footprint of European demand, which we have not found published in a reusable form.

</div>
</div>

## Does the result depend on the source? {#robustness}

<div class="liste-cartes">

1. **A measurement convention, checked year by year.** Primary energy is not counted in the same way everywhere. In the EIA's files, we measure, for every year from {{< dc-val "an_conv0" >}} to {{< dc-val "an_conv" >}}, the ratio of the energy counted to the electricity generated: {{< dc-val "btu_hydro" >}} Btu per kilowatt-hour for hydro and wind, that is, their electrical content, with no change of convention; from {{< dc-val "btu_nuc_min" >}} to {{< dc-val "btu_nuc_max" >}} Btu for nuclear, counted at the heat produced by the reactor. Solar is counted at {{< dc-val "btu_sol" >}} Btu in {{< dc-val "an_conv" >}} and at a higher ratio in earlier years, when it weighed very little. The Energy Institute, which publishes the *Statistical Review of World Energy*, has applied the same physical-content approach since its 2025 edition: the comparison below changes the producer, not the convention.
2. **Another producer.** With the Energy Institute's total energy supply ({{< dc-val "edition_ei" >}} edition: {{< dc-val "t_e1" >}} exajoules in {{< dc-val "an_t" >}}) and World Bank GDP and population, the decomposition keeps the same ranking: world consumption up {{< dc-val "t_de_pct" >}}% from {{< dc-val "an0" >}} to {{< dc-val "an_t" >}}; GDP-per-head effect {{< dc-val "t_rev_ej" >}} exajoules, population {{< dc-val "t_pop_ej" >}}, intensity −{{< dc-val "t_int_ej" >}}. For the European Union, from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, primary energy consumption fell by {{< dc-val "es_ei_pct" >}}% according to the Energy Institute, {{< dc-val "es_eia_pct" >}}% according to the EIA and {{< dc-val "es_es_pct" >}}% according to Eurostat's complete energy balances: a similar fall, slightly smaller in Eurostat's figures. Levels differ more ({{< dc-val "es_ej" >}} exajoules in {{< dc-val "an1" >}} for Eurostat, {{< dc-val "ue_e1" >}} for the EIA): Eurostat's indicator leaves out, among other things, non-energy uses of fuels.
3. **How GDP is converted matters.** The figures on this page use GDP converted at purchasing power parity. At market exchange rates, world GDP rises by {{< dc-val "m_dy_pct" >}}% from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, and intensity falls by only {{< dc-val "m_di_pct" >}}%; the GDP-per-head effect drops to {{< dc-val "m_rev_ej" >}} exajoules and the intensity effect shrinks to −{{< dc-val "m_int_ej" >}}, while the population effect does not change. Under both conversions, in every window, consumption rises, intensity falls and the GDP-per-head effect exceeds the population effect. How much intensity falls, however, depends on the conversion: at market exchange rates, from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, the intensity effect takes away less than the population effect adds.

</div>

## Comparison with the research {#research}

In 2021, Paul Brockway and four co-authors, researchers in energy economics and engineering (universities of Leeds, Sussex and Massachusetts, SOAS University of London, Calvin University, IFP Energies nouvelles), reviewed thirty-three studies that estimate the rebound effect for a whole economy, twenty-one based on general equilibrium models and twelve on other methods. They conclude that these effects may erode more than half of the energy savings expected from efficiency improvements, and that global energy scenarios, which take too little account of them, may underestimate future demand.

On what is observed, our figures agree with theirs: from 1971 to 2018, they write, the world experienced no absolute decoupling, only a few short-lived national cases, achieved in part, they note, by offshoring production to other countries; from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, the EIA series likewise shows no absolute decoupling at world level. On the explanation, this page does not test theirs. The same authors stress that an improvement in efficiency, measured in one way or at one level, does not necessarily bring an improvement measured in another way or at another level. An aggregate energy intensity therefore does not measure efficiency, and no rebound rate can be derived from a decomposition like this one.

## What these data do not say {#limits}

- **A decomposition, not a cause.** The three effects add up exactly to the change in consumption; they attribute no part of it to a cause.
- **Intensity is not efficiency.** Energy per unit of GDP can also fall when the make-up of the economy changes, and it depends on the measurement convention and on how the energy mix evolves.
- **A measurement convention.** The EIA and the Energy Institute count hydro and wind electricity at its electrical content. If it were counted as the fossil fuel it replaces (known as the substitution method), its growth would weigh more, and intensity would fall less; that variant is not computed here.
- **Territory, not footprint.** Energy embodied in imported goods is not counted: this is one limitation of the comparison with the European Union.
- **GDP at purchasing power parity.** It depends on a base year and on revisions; the EIA's constant-price GDP is checked against the World Bank's at each update, and the variant at market exchange rates is given above.
- **One decomposition method.** The effects are those of the logarithmic mean Divisia index (LMDI); no other decomposition method has been tried.
- **A world aggregate.** It adds up very different regional trajectories, which this page does not detail.

<aside class="encadre">

**A reading by the author, not tested here.** The [rebound effect](/en/rebound-effect/) refers to the extra consumption that erodes an efficiency gain. In the working paper [AWP-04](/en/awp/awp-04/), the economist Stéphane Lalut places it among the transfer mechanisms of the energy transition. The world figures on this page describe relative decoupling; they do not measure a rebound and do not demonstrate that reading.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, what each order leaves behind and on whom it leaves the burden.
{{< /appel-livre >}}

## Frequently asked questions {#faq}

{{< faq-visible colonnes="2" >}}

## Sources {#sources}

- EIA (U.S. Energy Information Administration), [international data](https://www.eia.gov/international/data/world), bulk file `INTL.zip` read by script: total energy consumption, GDP at purchasing power parity, population. Measurement convention read from the same file (hydro, wind, solar and nuclear electricity generation and primary energy consumption). Author's calculations: logarithmic mean Divisia index (LMDI) decomposition.
- Energy Institute, [*Statistical Review of World Energy*](https://www.energyinst.org/statistical-review), {{< dc-val "edition_ei" >}} edition, total energy supply (physical energy content method), read from Our World in Data's dataset ([owid_energy](https://catalog.ourworldindata.org/energy/owid_energy/readme.md)); the {{< dc-val "an_ei_publie" >}} world total is checked against the one published in the report of the {{< dc-val "ei_publie_ed" >}} edition ({{< dc-val "ei_publie" >}} exajoules), a value transcribed from the report.
- World Bank, GDP in constant prices [at purchasing power parity](https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.KD) and [at market exchange rates](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD), and population. Eurostat, [complete energy balances](https://ec.europa.eu/eurostat/databrowser/view/nrg_bal_c/default/table), primary energy consumption (Energy Efficiency Directive indicator), EU-27, from 1990.
- Paul E. Brockway, Steve Sorrell, Gregor Semieniuk, Matthew Kuperus Heun and Victor Court, “Energy efficiency and economy-wide rebound effects: A review of the evidence and its implications”, *Renewable and Sustainable Energy Reviews*, vol. 141, 2021, [doi:10.1016/j.rser.2021.110781](https://doi.org/10.1016/j.rser.2021.110781), read in its open-access version.

{{< reutiliser figures="figures_decouplage" jeu="decouplage" sources="EIA" donnees="In the CSV, one row per area and year since 1980, for the world and the EU-27: primary energy consumption, GDP at purchasing power parity in constant prices and population (EIA aggregates of varying composition before 1993); in the JSON, the decomposition of the change in consumption and its recalculation using other sources." >}}
From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world energy consumption rose by {{< dc-val "de_pct" >}}% while the energy used per unit of GDP, measured at purchasing power parity, fell by {{< dc-val "di_pct" >}}%: relative, not absolute, decoupling. In an accounting decomposition, with GDP measured the same way, the GDP-per-head effect weighs {{< dc-val "ratio_rp" >}} times as much as the population effect. In the European Union, according to the EIA, consumption fell on its territory; these data do not say whether it fell through efficiency, the decline of the most energy-intensive industries, relocation of production outside the EU or the effect of the convention used to count electricity.
{{< /reutiliser >}}
