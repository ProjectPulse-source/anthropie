---
title: "Is the world economy decoupling from energy?"
url: "/en/decoupling-energy-growth/"
description: "From {dc.an0} to {dc.an1}, the energy used per unit of world GDP fell by {dc.di_pct}%, and energy consumption rose by {dc.de_pct}%. Decomposed, the rise owes more to income per head than to population; in the European Union, consumption fell (EIA, author's calculation)."
chapo: "The world economy uses less and less energy for each unit of wealth it produces: {dc.di_pct}% less in {dc.an1} than in {dc.an0}. Its energy consumption, meanwhile, rose by {dc.de_pct}% over the same period. Falling energy intensity slowed the rise; it did not reverse it."
date: 2026-10-26
lastmod: 2026-10-26
og_title: "Is the world economy decoupling from energy? — S. Lalut"
og_image: "images/og-decouplage-en.jpg"
og_image_alt: "Share card: “Energy intensity falls, world consumption rises” — effects of population, income per head and energy intensity on world energy consumption (EIA)."
donnees: [decouplage]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "decouplage"
  nom: "Energy consumption, GDP and population, world and European Union, and decomposition of the change in consumption (EIA)"
  description: "Primary energy consumption, GDP at purchasing power parity in constant prices and population, world and EU-27, annual EIA series; decomposition of the change in consumption from {dc.an0} to {dc.an1} into population, income-per-head and energy-intensity effects (Divisia index), computed by the author, with a recalculation on Energy Institute and World Bank data."
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
  mots: ["decoupling", "energy intensity", "energy consumption", "energy efficiency", "rebound effect", "Jevons paradox", "energy transition", "sufficiency", "primary energy", "GDP", "EIA"]
  fichiers: ["decouplage.csv", "decouplage.json"]
faq:
  - question: "Is world energy consumption falling?"
    answer: "No. From {dc.an0} to {dc.an1}, it went from {dc.e0} to {dc.e1} exajoules, a rise of {dc.de_pct}%, while the energy used per unit of GDP fell by {dc.di_pct}%. This is relative decoupling: consumption grows more slowly than the economy, without falling."
  - question: "Does the rise in energy consumption come mainly from population growth?"
    answer: "Not primarily. In an accounting decomposition of the rise from {dc.an0} to {dc.an1}, the income-per-head effect ({dc.rev_ej} exajoules) weighs about twice as much as the population effect ({dc.pop_ej}), and falling energy intensity takes away {dc.int_ej}. The decomposition says how much each term weighed, not why."
  - question: "Can a country or region use less energy while getting richer?"
    answer: "Yes, on its territory: in the European Union, primary energy consumption fell by {dc.ue_de_pct}% from {dc.an0} to {dc.an1} while GDP rose by {dc.ue_dy_pct}%. These data do not count the energy embodied in imported goods: they do not say whether the fall comes from efficiency, from a change in the economy or from production moving outside Europe."
  - question: "Where do these figures come from?"
    answer: "From EIA international data (energy, GDP at purchasing power parity in constant prices, population), retrieved by a script that stops if a figure no longer meets the conditions on which the page's main sentences depend, and recalculated on Energy Institute and World Bank data. No value is transcribed by hand. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
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
    <source media="(max-width: 600px)" srcset="/img/decouplage-decomposition-en-m.svg" width="300" height="831">
    <img src="/img/decouplage-decomposition-en.svg" alt="Decomposition of the change in primary energy consumption from {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, as % of {{< dc-val "an0" >}} consumption. World: population effect {{< dc-val "w_pop_pct" >}}%, income-per-head effect {{< dc-val "w_rev_pct" >}}%, energy-intensity effect {{< dc-val "w_int_pct" >}}%, change in consumption {{< dc-val "w_tot_pct" >}}%. European Union: population effect {{< dc-val "u_pop_pct" >}}%, income-per-head effect {{< dc-val "u_rev_pct" >}}%, energy-intensity effect {{< dc-val "u_int_pct" >}}%, change in consumption {{< dc-val "u_tot_pct" >}}%." width="720" height="427" loading="lazy">
  </picture>
  <figcaption>Primary energy consumed on the territory, EIA convention; effects computed with a Divisia index, which add up exactly to the change (EIA, international data).</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world energy consumption rose by {{< dc-val "de_pct" >}}%: population and income per head added {{< dc-val "poussee_ej" >}} exajoules to it, and falling energy intensity took away only {{< dc-val "int_ej" >}}.

</div>

## Population or income? {#population-income}

It is often said that energy consumption rises because the world's population rises. An accounting decomposition separates the two. Energy consumption is the product of three terms: population, income per head, and the energy used per unit of income. From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, the population effect added {{< dc-val "pop_ej" >}} exajoules, the income-per-head effect {{< dc-val "rev_ej" >}}, and falling intensity took away {{< dc-val "int_ej" >}}: {{< dc-val "tot_ej" >}} exajoules more in all.

Income per head therefore weighed about twice as much as demography. The ranking does not depend on the starting year: it is the same in each of the windows tested, starting in {{< dc-val "fenetres" >}} and ending in {{< dc-val "an1" >}}; in each, consumption rose.

<details class="repli">
<summary>The five windows, in exajoules</summary>

| Start | Population effect | Income-per-head effect | Intensity effect | Change in consumption |
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

The decomposition measures each change in logarithms, which makes the sum of the effects exact. Intensity was multiplied by {{< dc-val "ratio_i" >}} (a fall of {{< dc-val "di_pct" >}}%), whose logarithm is {{< dc-val "ln_i" >}}. That value applies to the period's average consumption, {{< dc-val "lmoy_ej" >}} exajoules (a so-called logarithmic mean, between {{< dc-val "e0" >}} and {{< dc-val "e1" >}}): hence an effect of −{{< dc-val "int_ej" >}} exajoules. Set against the {{< dc-val "e0" >}} exajoules of {{< dc-val "an0" >}}, it is worth {{< dc-val "int_pct_e0" >}}%, the figure in the chart: it is the same fall in intensity, measured on a wider base, not a second fall.

</details>

## The European Union: absolute decoupling, on its territory {#european-union}

The same producer, with the same definition, gives the other case for the EU-27. From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, its primary energy consumption fell by {{< dc-val "ue_de_pct" >}}%, from {{< dc-val "ue_e0" >}} to {{< dc-val "ue_e1" >}} exajoules, while its GDP rose by {{< dc-val "ue_dy_pct" >}}%; it peaked in {{< dc-val "an_pic_ue" >}}. The population effect adds {{< dc-val "ue_pop_ej" >}} exajoules, the income-per-head effect {{< dc-val "ue_rev_ej" >}}, and the {{< dc-val "ue_di_pct" >}}% fall in intensity takes away {{< dc-val "ue_int_ej" >}}: more than the other two combined.

**The end year matters.** Stopping in 2019, before the pandemic and the 2022 surge in energy prices, European consumption falls by {{< dc-val "ue19_de_pct" >}}% from {{< dc-val "an0" >}}, with GDP up {{< dc-val "ue19_dy_pct" >}}%. Absolute decoupling is already there, but more than half of the fall measured to {{< dc-val "an1" >}} came after 2019; these data do not say how much of it will last.

**What the comparison does not say.** These figures count the energy consumed on European territory, not the energy used to make the goods Europe imports. They cannot tell whether the fall comes from efficiency, from the decline of the most energy-intensive industries or from their relocation outside Europe. Settling that would require an energy footprint of European demand, which we have not found published in a reusable form.

## Does the result depend on the source? {#robustness}

Primary energy conventions differ from one producer to another. The EIA counts hydro, wind and solar electricity at its electrical content, {{< dc-val "btu_hydro" >}} Btu per kilowatt-hour, and nuclear at the heat produced by the reactor, from {{< dc-val "btu_nuc_min" >}} to {{< dc-val "btu_nuc_max" >}} Btu per kilowatt-hour depending on the year: we find these ratios in its files every year from {{< dc-val "an_conv0" >}} to {{< dc-val "an_conv" >}}, with no change of convention. The Energy Institute, which publishes the *Statistical Review of World Energy*, counts all non-fossil electricity as the amount of fossil fuel that would have had to be burned to produce it.

With its primary energy ({{< dc-val "edition_ei" >}} edition) and World Bank GDP and population, the decomposition gives the same ranking: world consumption up {{< dc-val "t_de_pct" >}}% from {{< dc-val "an0" >}} to {{< dc-val "an_t" >}}, income-per-head effect {{< dc-val "t_rev_ej" >}} exajoules, population {{< dc-val "t_pop_ej" >}}, intensity −{{< dc-val "t_int_ej" >}}: {{< dc-val "t_int_ej" >}} taken away from the {{< dc-val "t_poussee_ej" >}} added. For the European Union, the fall is {{< dc-val "t_ue_de_pct" >}}% instead of {{< dc-val "ue_de_pct" >}}%: the direction does not change, the size depends on the convention.

## Confronting the research {#research}

Paul Brockway and four co-authors, researchers in energy economics and engineering (universities of Leeds, Sussex, Massachusetts, SOAS and Calvin, IFP Energies nouvelles), reviewed in 2021 thirty-three studies that estimate the rebound effect for a whole economy, twenty-one based on general equilibrium models and twelve on other methods. They conclude that these effects may erode more than half of the energy savings expected from efficiency, and that global scenarios take too little account of them: this is the thesis they defend against the models that project absolute decoupling.

On the observation, our figures agree with theirs: from 1971 to 2018, they write, the world experienced no absolute decoupling, only national cases; the EIA series extends that observation to {{< dc-val "an1" >}}. On the explanation, this page does not test them. The same authors stress that an improvement in efficiency measured at one level does not necessarily bring an improvement measured at another: an aggregate energy intensity does not measure efficiency, and no rebound rate can be derived from a decomposition like this one.

## What these data do not say {#limits}

- **A decomposition, not a cause.** The three effects add up exactly to the change in consumption; they attribute no part of it to a cause.
- **Intensity is not efficiency.** Energy per unit of GDP also falls when the make-up of the economy changes, or when the measurement convention changes.
- **A measurement convention.** The EIA counts renewable electricity at its electrical content: its growth weighs less than in the Energy Institute's convention. The recalculation on that other convention is given above.
- **Territory, not footprint.** Energy embodied in imports is not counted: this is the decisive limit of the comparison with the European Union.
- **GDP at purchasing power parity.** It depends on a base year and on revisions; the EIA's constant prices are checked against the World Bank at each update.
- **A world aggregate.** It adds up very different regional trajectories, which this page does not detail.

<aside class="encadre">

**A reading by the author, not tested here.** The notion of the [rebound effect](/en/rebound-effect/) refers to the renewed consumption that erodes an efficiency gain. In the working paper [AWP-04](/en/awp/awp-04/), the economist Stéphane Lalut places it among the transfer mechanisms of the energy transition. The figures on this page describe relative decoupling; they do not measure a rebound and do not demonstrate that reading.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, what each order leaves behind it and on whom it leaves the burden.
{{< /appel-livre >}}

## Sources {#sources}

- EIA (U.S. Energy Information Administration), [international data](https://www.eia.gov/international/data/world), bulk file `INTL.zip` read by script: total energy consumption, GDP at purchasing power parity, population. Measurement convention read from the same file (hydro and nuclear electricity generation and consumption). Author's calculations: logarithmic mean Divisia index decomposition.
- Energy Institute, [*Statistical Review of World Energy*](https://www.energyinst.org/statistical-review), {{< dc-val "edition_ei" >}} edition, primary energy, read in Our World in Data's data repository ([owid/energy-data](https://github.com/owid/energy-data)), as the Energy Institute's site refuses automated reads; World Bank, [GDP at purchasing power parity in constant prices](https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.KD) and population.
- Paul E. Brockway, Steve Sorrell, Gregor Semieniuk, Matthew Kuperus Heun and Victor Court, “Energy efficiency and economy-wide rebound effects: A review of the evidence and its implications”, *Renewable and Sustainable Energy Reviews*, vol. 141, 2021, [doi:10.1016/j.rser.2021.110781](https://doi.org/10.1016/j.rser.2021.110781), read in its open-access version.

{{< reutiliser figures="figures_decouplage" jeu="decouplage" sources="EIA (international data)" donnees="For the world and the EU-27, every year since 1980: primary energy consumption, GDP at purchasing power parity in constant prices and population; decomposition of the change in consumption and its recalculation on other sources, in the JSON; the annual series are also available as CSV, one row per area and year." >}}
From {{< dc-val "an0" >}} to {{< dc-val "an1" >}}, world energy consumption rose by {{< dc-val "de_pct" >}}% while the energy used per unit of GDP fell by {{< dc-val "di_pct" >}}%: relative, not absolute, decoupling. In an accounting decomposition, the income-per-head effect weighs about twice as much as the population effect. In the European Union, consumption fell on its territory; these data do not say whether through efficiency or relocation.
{{< /reutiliser >}}
