---
title: "Is the world economy decoupling from energy?"
url: "/en/decoupling-energy-growth/"
description: "From {dc.an0} to {dc.an1}, the energy used per unit of world GDP fell by {dc.di_pct}%, and energy consumption rose by {dc.de_pct}%. Decomposed, the rise owes more to GDP per head than to population; in the European Union, consumption fell (EIA, author's calculation)."
chapo: "The world economy uses less and less energy for each unit of wealth it produces: {dc.di_pct}% less in {dc.an1} than in {dc.an0}. Its energy consumption, meanwhile, rose by {dc.de_pct}% over the same period. Falling energy intensity slowed the rise; it did not reverse it."
date: 2026-10-26
lastmod: 2026-10-26
journal:
  - {date: 2026-10-26, texte: "Correction: the check recalculation relied on an Our World in Data primary energy series using the substitution method, wrongly attributed to the Energy Institute, which adopted the physical energy content method in 2025; it now relies on the Energy Institute's total energy supply (EU fall from 2000 to 2024: 17% instead of 12%). The EIA convention is checked for wind as for hydro, not for solar. Added: a variant with GDP at market exchange rates, a comparison with Eurostat; “income per head” becomes “GDP per head”."}
og_title: "Is the world economy decoupling from energy? — S. Lalut"
og_image: "images/og-decouplage-en.jpg"
og_image_alt: "Share card: “Energy intensity falls, world consumption rises” — effects of population, GDP per head and energy intensity on world energy consumption (EIA)."
donnees: [decouplage]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "decouplage"
  nom: "Energy consumption, GDP and population, world and European Union, and decomposition of the change in consumption (EIA)"
  description: "Primary energy consumption, GDP at purchasing power parity in constant prices and population, world and EU-27, annual EIA series; decomposition of the change in consumption from {dc.an0} to {dc.an1} into population, GDP-per-head and energy-intensity effects (Divisia index), computed by the author, with a recalculation on Energy Institute and World Bank data, a variant at market exchange rates and a comparison with Eurostat for the European Union."
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
    - "https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_eff/default/table"
  mots: ["decoupling", "energy intensity", "energy consumption", "energy efficiency", "rebound effect", "Jevons paradox", "energy transition", "sufficiency", "primary energy", "GDP", "EIA"]
  fichiers: ["decouplage.csv", "decouplage.json"]
faq:
  - question: "Is world energy consumption falling?"
    answer: "No. From {dc.an0} to {dc.an1}, it went from {dc.e0} to {dc.e1} exajoules, a rise of {dc.de_pct}%, while the energy used per unit of GDP fell by {dc.di_pct}%. This is relative decoupling: consumption grows more slowly than the economy, without falling."
  - question: "Does the rise in energy consumption come mainly from population growth?"
    answer: "Not primarily. In an accounting decomposition of the rise from {dc.an0} to {dc.an1}, the GDP-per-head effect ({dc.rev_ej} exajoules) weighs {dc.ratio_rp} times as much as the population effect ({dc.pop_ej}), and falling energy intensity takes away {dc.int_ej}. The decomposition says how much each term weighed, not why."
  - question: "Can a country or region use less energy while getting richer?"
    answer: "Yes, on its territory: in the European Union, primary energy consumption fell by {dc.ue_de_pct}% from {dc.an0} to {dc.an1} while GDP rose by {dc.ue_dy_pct}%. These data do not count the energy embodied in imported goods: they do not say whether the fall comes from efficiency, from a change in the economy or from production moving outside Europe."
  - question: "Where do these figures come from?"
    answer: "From EIA international data (energy, GDP at purchasing power parity in constant prices, population), retrieved by a script that stops if a figure no longer meets the conditions on which the page's main sentences depend, and recalculated on Energy Institute, World Bank and Eurostat data. Only one value is transcribed by hand: the world total published by the Energy Institute for {dc.an_ei_publie}, used to check where the recalculation comes from. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]
  conception: "docs/conception/decouplage-energie-croissance.md"
  refonte: "2026-10-26"
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]
  rang: 50
  nature: "Public data recalculated (EIA, Energy Institute, World Bank)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data as of: {{< dc-val "date_donnees" >}}</span> EIA, international data: primary energy consumption, GDP at purchasing power parity in constant prices and population, world and European Union, 1980 to {{< dc-val "an1" >}}. Download: <a href="/decouplage.csv">CSV</a> · <a href="/decouplage.json">JSON</a></p>

## Intensity falls, consumption rises {#paradox}

From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world GDP, measured at purchasing power parity in constant prices, rose by {{< dc-val "dy_pct" >}}%. The energy used to produce each unit of that GDP, energy intensity, fell by {{< dc-val "di_pct" >}}%. And world primary energy consumption went from {{< dc-val "e0" >}} to {{< dc-val "e1" >}} exajoules (one exajoule is 10¹⁸ joules): {{< dc-val "de_pct" >}}% more.

The world economy has therefore decoupled from energy in the relative sense: its consumption grows more slowly than its output. It has not decoupled in the absolute sense, where consumption would fall while the economy grows.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/decouplage-decomposition-en-m.svg" width="300" height="848">
    <img src="/img/decouplage-decomposition-en.svg" alt="Decomposition of the change in primary energy consumption from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, as % of {{< dc-val "an0" >}} consumption. World: population effect {{< dc-val "w_pop_pct" >}}%, GDP-per-head effect {{< dc-val "w_rev_pct" >}}%, energy-intensity effect {{< dc-val "w_int_pct" >}}%, change in consumption {{< dc-val "w_tot_pct" >}}%. European Union: population effect {{< dc-val "u_pop_pct" >}}%, GDP-per-head effect {{< dc-val "u_rev_pct" >}}%, energy-intensity effect {{< dc-val "u_int_pct" >}}%, change in consumption {{< dc-val "u_tot_pct" >}}%." width="720" height="441" loading="lazy">
  </picture>
  <figcaption>Primary energy consumed on the territory, EIA convention; effects computed with a Divisia index, which add up exactly to the change (EIA, international data).</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world energy consumption rose by {{< dc-val "de_pct" >}}%: the decomposition attributes {{< dc-val "poussee_ej" >}} exajoules of increase to population and GDP per head, and only {{< dc-val "int_ej" >}} of decrease to energy intensity.

</div>

## Population or growing wealth? {#population-income}

It is often said that energy consumption rises because the world's population rises. An accounting decomposition separates the two. Energy consumption is the product of three terms: population, GDP per head, and the energy used per unit of GDP. From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, the decomposition attributes {{< dc-val "pop_ej" >}} exajoules to the population effect, {{< dc-val "rev_ej" >}} to the GDP-per-head effect and −{{< dc-val "int_ej" >}} to falling intensity: {{< dc-val "tot_ej" >}} exajoules more in all.

GDP per head therefore weighed {{< dc-val "ratio_rp" >}} times as much as demography. That ranking does not depend on the starting year: in each of the windows tested, starting in {{< dc-val "fenetres" >}} and ending in {{< dc-val "an1" >}}, the GDP-per-head effect exceeds the population effect, and consumption rose.

<details class="repli">
<summary>The five windows, in exajoules</summary>

| Start | Population effect | GDP-per-head effect | Intensity effect | Change in consumption |
|---|---|---|---|---|
| 1990 | {{< dc-val "f1990_pop" >}} | {{< dc-val "f1990_rev" >}} | {{< dc-val "f1990_int" >}} | {{< dc-val "f1990_tot" >}} |
| 2000 | {{< dc-val "f2000_pop" >}} | {{< dc-val "f2000_rev" >}} | {{< dc-val "f2000_int" >}} | {{< dc-val "f2000_tot" >}} |
| 2010 | {{< dc-val "f2010_pop" >}} | {{< dc-val "f2010_rev" >}} | {{< dc-val "f2010_int" >}} | {{< dc-val "f2010_tot" >}} |
| 2015 | {{< dc-val "f2015_pop" >}} | {{< dc-val "f2015_rev" >}} | {{< dc-val "f2015_int" >}} | {{< dc-val "f2015_tot" >}} |
| 2019 | {{< dc-val "f2019_pop" >}} | {{< dc-val "f2019_rev" >}} | {{< dc-val "f2019_int" >}} | {{< dc-val "f2019_tot" >}} |

Each window ends in {{< dc-val "an1" >}}; world, EIA. Values rounded to the exajoule: their sum may differ from the total by one.

</details>

**An accounting decomposition is not an explanation.** It says how much each term weighed, not why. It does not say that getting richer causes the rise in consumption, nor that falling intensity comes from more efficient uses: intensity also falls when the economy shifts towards services, or when a measurement convention counts electricity differently. Nor can it be used to estimate a rebound effect.

<details class="repli">
<summary>Why the intensity effect (−{{< dc-val "int_ej" >}} exajoules) exceeds the fall in intensity itself</summary>

The {{< dc-val "di_pct" >}}% measures the change in intensity; the {{< dc-val "int_ej" >}} exajoules, its contribution to the change in consumption. The decomposition measures each change in logarithms, which makes the sum of the effects exact. Intensity was multiplied by {{< dc-val "ratio_i" >}} (a fall of {{< dc-val "di_pct" >}}%), whose logarithm is {{< dc-val "ln_i" >}}. That value applies to the period's average consumption, {{< dc-val "lmoy_ej" >}} exajoules (a so-called logarithmic mean, between {{< dc-val "e0" >}} and {{< dc-val "e1" >}}): hence an effect of −{{< dc-val "int_ej" >}} exajoules. Set against the {{< dc-val "e0" >}} exajoules of {{< dc-val "an0" >}}, it is worth {{< dc-val "int_pct_e0" >}}%, the figure in the chart: it is the same fall in intensity, measured on a wider base, not a second fall.

</details>

## The European Union: absolute decoupling, on its territory {#european-union}

The same producer, with the same definition, gives the other case for the EU-27. From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, its primary energy consumption fell by {{< dc-val "ue_de_pct" >}}%, from {{< dc-val "ue_e0" >}} to {{< dc-val "ue_e1" >}} exajoules, while its GDP rose by {{< dc-val "ue_dy_pct" >}}%; it peaked in {{< dc-val "an_pic_ue" >}}. The population effect adds {{< dc-val "ue_pop_ej" >}} exajoules, the GDP-per-head effect {{< dc-val "ue_rev_ej" >}}, and the {{< dc-val "ue_di_pct" >}}% fall in intensity takes away {{< dc-val "ue_int_ej" >}}: more than the other two combined.

**The end year matters.** Stopping in 2019, before the pandemic and the 2022 surge in energy prices, European consumption falls by {{< dc-val "ue19_de_pct" >}}% from {{< dc-val "an0" >}}, with GDP up {{< dc-val "ue19_dy_pct" >}}%. Absolute decoupling is already there, but more than half of the fall measured to {{< dc-val "an1" >}} came after 2019; these data do not say how much of it will last.

**What the comparison does not say.** These figures count the energy consumed on European territory, not the energy used to make the goods Europe imports. They cannot tell whether the fall comes from efficiency, from the decline of the most energy-intensive industries or from their relocation outside Europe. Settling that would require an energy footprint of European demand, which we have not found published in a reusable form.

## Does the result depend on the source? {#robustness}

**A measurement convention, checked year by year.** Primary energy is not counted the same way everywhere. In the EIA's files, we measure every year from {{< dc-val "an_conv0" >}} to {{< dc-val "an_conv" >}} the ratio between the energy counted and the electricity generated: {{< dc-val "btu_hydro" >}} Btu per kilowatt-hour for hydro and wind, that is, their electrical content, with no change of convention; from {{< dc-val "btu_nuc_min" >}} to {{< dc-val "btu_nuc_max" >}} Btu for nuclear, counted at the heat produced by the reactor. Solar is counted at {{< dc-val "btu_sol" >}} Btu in {{< dc-val "an_conv" >}}, at a higher ratio in earlier years, when it weighed very little. The Energy Institute, which publishes the *Statistical Review of World Energy*, has applied the same physical-content logic since its 2025 edition: the comparison below tests another producer, not another convention.

**Another producer.** With the Energy Institute's total energy supply ({{< dc-val "edition_ei" >}} edition: {{< dc-val "t_e1" >}} exajoules in {{< dc-val "an_t" >}}) and World Bank GDP and population, the decomposition keeps the same ranking: world consumption up {{< dc-val "t_de_pct" >}}% from {{< dc-val "an0" >}} to {{< dc-val "an_t" >}}; GDP-per-head effect {{< dc-val "t_rev_ej" >}} exajoules, population {{< dc-val "t_pop_ej" >}}, intensity −{{< dc-val "t_int_ej" >}}. For the European Union, the fall is {{< dc-val "t_ue_de_pct" >}}% instead of {{< dc-val "ue_de_pct" >}}%. Eurostat, which publishes its primary energy consumption indicator only from {{< dc-val "an_es" >}}, gives the same size within a few points: from {{< dc-val "an_es" >}} to {{< dc-val "an1" >}}, EU consumption falls by {{< dc-val "es_es_pct" >}}% according to Eurostat, {{< dc-val "es_ei_pct" >}}% according to the Energy Institute and {{< dc-val "es_eia_pct" >}}% according to the EIA. Levels differ more ({{< dc-val "es_ej" >}} exajoules in {{< dc-val "an1" >}} for Eurostat, {{< dc-val "ue_e1" >}} for the EIA): Eurostat's indicator leaves out, among other things, non-energy uses of fuels.

**How GDP is converted matters.** The figures on this page convert GDP at purchasing power parity. At market exchange rates, world GDP rises by {{< dc-val "m_dy_pct" >}}% from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, and intensity falls by only {{< dc-val "m_di_pct" >}}%; the GDP-per-head effect drops to {{< dc-val "m_rev_ej" >}} exajoules and the intensity effect to −{{< dc-val "m_int_ej" >}}, while the population effect does not change. Under both conversions, in every window, consumption rises, intensity falls and GDP per head weighs more than population. How much intensity falls, however, depends on the conversion: at market exchange rates, from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, it takes away less than population adds.

## Confronting the research {#research}

Paul Brockway and four co-authors, researchers in energy economics and engineering (universities of Leeds, Sussex, Massachusetts, SOAS and Calvin, IFP Energies nouvelles), reviewed in 2021 thirty-three studies that estimate the rebound effect for a whole economy, twenty-one based on general equilibrium models and twelve on other methods. They conclude that these effects may erode more than half of the energy savings expected from efficiency, and that global energy scenarios, which take too little account of them, may underestimate future demand.

On the observation, our figures agree with theirs: from 1971 to 2018, they write, the world experienced no absolute decoupling, only national cases; from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, the EIA series shows the same. On the explanation, this page does not test them. The same authors stress that an improvement in efficiency measured at one level does not necessarily bring an improvement measured at another: an aggregate energy intensity does not measure efficiency, and no rebound rate can be derived from a decomposition like this one.

## What these data do not say {#limits}

- **A decomposition, not a cause.** The three effects add up exactly to the change in consumption; they attribute no part of it to a cause.
- **Intensity is not efficiency.** Energy per unit of GDP also falls when the make-up of the economy changes, or when the measurement convention changes.
- **A measurement convention.** The EIA and the Energy Institute count hydro and wind electricity at its electrical content. Counted as the fossil fuel it replaces (the so-called substitution method), its growth would weigh more, and intensity would fall less; that variant is not computed here.
- **Territory, not footprint.** Energy embodied in imports is not counted: this is the decisive limit of the comparison with the European Union.
- **GDP at purchasing power parity.** It depends on a base year and on revisions; the EIA's constant prices are checked against the World Bank at each update, and the variant at market exchange rates is given above.
- **One decomposition method.** The effects are those of the logarithmic mean Divisia index; no other decomposition method has been tried.
- **A world aggregate.** It adds up very different regional trajectories, which this page does not detail.

<aside class="encadre">

**A reading by the author, not tested here.** The notion of the [rebound effect](/en/rebound-effect/) refers to the renewed consumption that erodes an efficiency gain. In the working paper [AWP-04](/en/awp/awp-04/), the economist Stéphane Lalut places it among the transfer mechanisms of the energy transition. The figures on this page describe relative decoupling; they do not measure a rebound and do not demonstrate that reading.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, what each order leaves behind it and on whom it leaves the burden.
{{< /appel-livre >}}

## Sources {#sources}

- EIA (U.S. Energy Information Administration), [international data](https://www.eia.gov/international/data/world), bulk file `INTL.zip` read by script: total energy consumption, GDP at purchasing power parity, population. Measurement convention read from the same file (hydro, wind, solar and nuclear electricity generation and consumption). Author's calculations: logarithmic mean Divisia index decomposition.
- Energy Institute, [*Statistical Review of World Energy*](https://www.energyinst.org/statistical-review), {{< dc-val "edition_ei" >}} edition, total energy supply (physical energy content method), read in Our World in Data's dataset ([owid_energy](https://catalog.ourworldindata.org/energy/owid_energy/readme.md)), as the Energy Institute's site refuses automated reads; the {{< dc-val "an_ei_publie" >}} world total is checked against the one published in the 2025 edition ({{< dc-val "ei_publie" >}} exajoules), a value transcribed from the report.
- World Bank, GDP in constant prices [at purchasing power parity](https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.KD) and [at market exchange rates](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD), and population. Eurostat, [primary energy consumption](https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_eff/default/table) (Energy Efficiency Directive indicator), EU-27.
- Paul E. Brockway, Steve Sorrell, Gregor Semieniuk, Matthew Kuperus Heun and Victor Court, “Energy efficiency and economy-wide rebound effects: A review of the evidence and its implications”, *Renewable and Sustainable Energy Reviews*, vol. 141, 2021, [doi:10.1016/j.rser.2021.110781](https://doi.org/10.1016/j.rser.2021.110781), read in its open-access version.

{{< reutiliser figures="figures_decouplage" jeu="decouplage" sources="EIA (international data)" donnees="For the world and the EU-27, every year since 1980: primary energy consumption, GDP at purchasing power parity in constant prices and population; decomposition of the change in consumption and its recalculation on other sources, in the JSON; the annual series are also available as CSV, one row per area and year." >}}
From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world energy consumption rose by {{< dc-val "de_pct" >}}% while the energy used per unit of GDP fell by {{< dc-val "di_pct" >}}%: relative, not absolute, decoupling. In an accounting decomposition, the GDP-per-head effect weighs {{< dc-val "ratio_rp" >}} times as much as the population effect. In the European Union, consumption fell on its territory; these data do not say whether through efficiency or relocation.
{{< /reutiliser >}}
