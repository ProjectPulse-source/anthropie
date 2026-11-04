---
title: "Data centres: do reserved gigawatts foretell consumption?"
url: /en/data-centres-reserved-capacity/
description: "In November 2025, data centres had reserved {dtc.res_nov2025} GW of grid connection capacity with RTE, {dtc.st_2030} GW of it for commissioning from 2030; those connected to RTE's grid consumed nearly {dtc.rpt_2025} TWh in 2025. Reserved capacity, timing, abandonments and consumption in France, from RTE's publications."
chapo: "The figure that circulates is that of reservations: nearly {dtc.res_mai2026} gigawatts in May 2026, against about {dtc.res_fin2024} at end-2024. But reserved capacity is not consumption. More than half of the capacity reserved in November 2025 is for commissioning from 2030, other reservations have already been abandoned, and the data centres connected to the transmission grid consumed nearly {dtc.rpt_2025} terawatt-hour in 2025."
date: 2026-10-27
lastmod: 2026-10-27
og_title: "Data centres: do reserved gigawatts foretell consumption? — S. Lalut"
og_image: "images/og-data-centers-en.jpg"
og_image_alt: "Share card: “Reserved is not consumed” — capacity reserved by data centres with RTE and consumption of the centres connected to its grid (RTE)."
donnees: [data_centers]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "data_centers"
  nom: "Data centres in France: grid connection capacity reserved with RTE, breakdown by status and electricity consumption (RTE publications)"
  description: "Grid connection capacity reserved by data centres with RTE (end-2024, November 2025, May 2026), November 2025 breakdown by status (connected, under construction, commissioning 2025-2029 or from 2030, suspended, abandoned) measured on figure 2.3 of RTE's Bilan prévisionnel 2025-2035, metered and estimated consumption, RTE pathways for 2030 and 2035; each value carries its nature (read in the text or measured on the figure) and its source."
  couverture_temporelle: "2024/2035"
  couverture_spatiale: "France"
  variables:
    - {nom: "Reserved grid connection capacity", unite: "GW", description: "data centres, public transmission grid"}
    - {nom: "Reserved capacity by status", unite: "GW", description: "November 2025, measured on figure 2.3"}
    - {nom: "Electricity consumption", unite: "TWh per year", description: "metered, estimated, or projected in RTE's pathways"}
  sources:
    - "https://assets.rte-france.com/prod/public/2025-12/2025-12-23-bilan-previsionnel-2025-consommation.pdf"
    - "https://assets.rte-france.com/prod/public/2026-02/Bilan-electrique-2025-principaux-resultats.pdf"
    - "https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france"
    - "https://www.statistiques.developpement-durable.gouv.fr/la-consommation-delectricite-des-data-centers-en-2024"
  mots: ["data centres", "data centers", "RTE", "grid connection", "reserved capacity", "electricity consumption", "artificial intelligence", "France", "connection queue", "electricity grid"]
  fichiers: ["data_centers.csv", "data_centers.json"]
faq:
  - question: "How much grid capacity have data centres reserved in France?"
    answer: "According to RTE, nearly {dtc.res_mai2026} gigawatts in May 2026, for about {dtc.projets_2026} projects, against about {dtc.res_fin2024} at end-2024. In November 2025, of {dtc.res_nov2025} GW reserved, {dtc.st_2030} GW was for commissioning from 2030, and reservations totalling about {dtc.st_abandon} GW had been abandoned since 2023."
  - question: "How much electricity do data centres consume in France?"
    answer: "Dedicated-site data centres connected to RTE's transmission grid consumed nearly {dtc.rpt_2025} TWh in 2025, against {dtc.rpt_2024} TWh in 2024; those on Enedis's distribution grid, {dtc.enedis_2024} TWh in 2024. RTE estimates all dedicated sites at {dtc.sd_bas} to {dtc.sd_haut} TWh in 2024, and its two pathways give {dtc.l2030} to {dtc.r2030} TWh in 2030."
  - question: "Where do these figures come from?"
    answer: "From three RTE publications (Bilan prévisionnel 2025-2035, Bilan électrique 2025, web page “Les data centers en chiffres clés”) and, as an independent check, the SDES census (July 2026), downloaded by a script that reads each value in the sentence that carries it, measures the breakdown by status on a figure of the Bilan prévisionnel, and stops if a figure no longer meets the conditions on which the page's main sentences depend. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/data-centers-puissance-reservee.md"  # fiche de conception (regle 12)
  refonte: "2026-10-27"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]
  rang: 47
  nature: "RTE publications read and measured"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data as of: {{< dtc-val "date_donnees" >}}</span> RTE, Bilan prévisionnel 2025-2035 (December 2025), Bilan électrique 2025 (February 2026) and web page “Les data centers en chiffres clés” (updated {{< dtc-val "date_web" >}}): values read in the text, breakdown by status measured on a figure. Download: <a href="/data_centers.csv">CSV</a> · <a href="/data_centers.json">JSON</a></p>

## What is reserved, what is consumed {#reserved-consumed}

In May 2026, according to RTE, France's transmission system operator, data centres had reserved nearly {{< dtc-val "res_mai2026" >}} gigawatts (GW) of connection capacity on its grid, for about {{< dtc-val "projets_2026" >}} projects. At end-2024, some forty projects totalled about {{< dtc-val "res_fin2024" >}} GW: in less than a year and a half, reserved capacity more than tripled. At end-November 2025, data centres held {{< dtc-val "res_nov2025" >}} GW of the roughly {{< dtc-val "tot_nov2025" >}} GW of access rights granted by RTE to large projects, ahead of hydrogen ({{< dtc-val "tot_h2" >}} GW) and industry ({{< dtc-val "tot_ind" >}} GW).

Consumption, for its part, is counted in terawatt-hours (TWh). Dedicated-site data centres connected to RTE's transmission grid consumed {{< dtc-val "rpt_2024" >}} TWh in 2024 and nearly {{< dtc-val "rpt_2025" >}} TWh in 2025; those on the distribution grid run by Enedis, {{< dtc-val "enedis_2024" >}} TWh in 2024. RTE estimates all dedicated sites at {{< dtc-val "sd_bas" >}} to {{< dtc-val "sd_haut" >}} TWh in 2024, and {{< dtc-val "int_bas" >}} to {{< dtc-val "int_haut" >}} TWh including the in-house server rooms of companies and public bodies. The statistical service of the French ministry for the ecological transition (SDES), which counts the centres themselves, reaches the same order of magnitude: {{< dtc-val "sdes_n" >}} centres using more than 1 GWh a year consumed nearly {{< dtc-val "sdes_twh" >}} TWh in 2024, and the whole is estimated at {{< dtc-val "sdes_bas" >}} to {{< dtc-val "sdes_haut" >}} TWh. The two estimates do not cover exactly the same scope: they cross-check, without replacing each other.

**Reserved capacity is not consumption.** A reservation guarantees access to the grid; it says neither whether the site will be built, nor when, nor at what power it will run. The figure places the two quantities one above the other, each on its own scale, without relating one to the other.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/data-centers-reserve-consomme-en-m.svg" width="300" height="1176">
    <img src="/img/data-centers-reserve-consomme-en.svg" alt="Two panels. Top: grid connection capacity reserved by data centres with RTE: about {{< dtc-val "res_fin2024" >}} GW at end-2024, {{< dtc-val "res_nov2025" >}} GW in November 2025, of which {{< dtc-val "st_avant2030" >}} GW for commissioning before 2030 and {{< dtc-val "st_2030" >}} GW from 2030, nearly {{< dtc-val "res_mai2026" >}} GW in May 2026; {{< dtc-val "rac_gw" >}} GW already connected to RTE's grid. Bottom: consumption: {{< dtc-val "rpt_2024" >}} TWh in 2024 and nearly {{< dtc-val "rpt_2025" >}} TWh in 2025 on RTE's grid, {{< dtc-val "sd_bas" >}} to {{< dtc-val "sd_haut" >}} TWh estimated for all dedicated sites in 2024, {{< dtc-val "l2030" >}} to {{< dtc-val "r2030" >}} TWh in 2030 and {{< dtc-val "l2035" >}} to {{< dtc-val "r2035" >}} TWh in 2035 in RTE's two pathways." width="720" height="569" loading="lazy">
  </picture>
  <figcaption>Reserved grid connection capacity (GW) and electricity consumption (TWh per year) of data centres, according to RTE; November 2025 breakdown measured on figure 2.3 of the Bilan prévisionnel 2025-2035.</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** In November 2025, data centres had reserved {{< dtc-val "res_nov2025" >}} GW of grid connection capacity with RTE, {{< dtc-val "st_2030" >}} GW of it for commissioning from 2030; those connected to RTE's grid consumed nearly {{< dtc-val "rpt_2025" >}} TWh in 2025.

</div>

## Does a reservation foretell consumption? {#timing}

Between a reservation and consumption, each step carries its own uncertainty: the project has to be built and connected; once connected, it draws only part of the reserved capacity, and only after a ramp-up; finally, it is how long that capacity is drawn that makes the terawatt-hours consumed.

Two readings of the reservation figure circulate. The first sees in it announced, and imminent, consumption: it is the reading that any conversion of reserved gigawatts into nuclear reactors or households assumes. The second sees an option on the grid, part of which will materialise slowly and part never: this is the reading of RTE, which grants these reservations and is preparing a reform of their queue. It is not neutral for all that: it also supports the case for that reform.

The reservations themselves settle one point between them: timing. On {{< dtc-val "date_fig23" >}}, of the capacity reserved by data centres (measured on an RTE figure, to within 0.1 GW), {{< dtc-val "st_travaux" >}} GW was under construction, {{< dtc-val "st_2529" >}} GW signed for commissioning between 2025 and 2029, {{< dtc-val "st_2030" >}} GW for commissioning from 2030 and {{< dtc-val "st_suspendu" >}} GW suspended. More than half of the reserved capacity therefore targets 2030 or later. And since 2023, reservations totalling about {{< dtc-val "st_abandon" >}} GW have been abandoned, against {{< dtc-val "st_raccorde" >}} GW of projects actually connected. The {{< dtc-val "sites_rte" >}} data centres directly connected to RTE's grid total {{< dtc-val "rac_mw" >}} megawatts.

RTE gives three reasons for this gap between reservation and consumption. Some developers have secured grid access at several points for what are in fact similar projects. Sites ramp up slowly: according to the main operators, cited by RTE, it takes {{< dtc-val "montee" >}} to reach about {{< dtc-val "montee_pct" >}}% of the capacity requested, because the very expensive servers are installed only as usage grows. Finally, the power drawn stays below the connection capacity: RTE observes that data centres connected to its grid for two to three years consume for now, on average, only {{< dtc-val "util_obs" >}}% of the capacity they requested.

**This graph settles a question of timing, not of volume.** It shows that reserved capacity translates into consumption neither immediately nor in full; it does not say what share will materialise by 2035.

## What RTE projects {#pathways}

In its Bilan prévisionnel 2025-2035, RTE retains two pathways for the consumption of dedicated-site data centres: {{< dtc-val "l2030" >}} to {{< dtc-val "r2030" >}} TWh in 2030, {{< dtc-val "l2035" >}} to {{< dtc-val "r2035" >}} TWh in 2035. The higher one assumes that about {{< dtc-val "concret_r" >}}% of the projects that requested a transmission-grid connection for commissioning before 2030 materialise ({{< dtc-val "concret_r_gw" >}} GW), and that these sites use on average {{< dtc-val "util_2030" >}}% of their connection capacity by then; the lower one, a materialisation rate of about {{< dtc-val "concret_l" >}}%. These are assumptions, not measurements.

RTE itself gives the order of magnitude of what these assumptions set aside: if all the roughly {{< dtc-val "tot_nov2025" >}} GW reserved by large projects, data centres, hydrogen and industry together, ran at full power all year, consumption would theoretically reach about {{< dtc-val "theo_twh" >}} TWh, “a level out of all proportion” with its assumptions.

RTE's publications do not all give the same figures. Its web page “Les data centers en chiffres clés”, updated on {{< dtc-val "date_web" >}}, attributes to the same Bilan prévisionnel a consumption of {{< dtc-val "w30_bas" >}} to {{< dtc-val "w30_haut" >}} TWh in 2030 and {{< dtc-val "w35_bas" >}} to {{< dtc-val "w35_haut" >}} TWh in 2035 “in a rapid decarbonisation pathway”, and a current consumption of about {{< dtc-val "web_conso" >}} TWh. The published document gives {{< dtc-val "r2030" >}} and {{< dtc-val "r2035" >}} TWh for that pathway, and {{< dtc-val "sd_bas" >}} to {{< dtc-val "sd_haut" >}} TWh in 2024 for dedicated sites. This page follows the published document; the web page does not explain the gap.

## Does a reservation already commit the public? {#commitment}

Not irreversibly yet. At its holder's request, a reservation can be suspended for one year, renewable once: the capacity remains guaranteed, but the financial and timing conditions may be revised. It can also be abandoned: this has happened to about {{< dtc-val "st_abandon" >}} GW of data-centre reservations since 2023.

What could commit the public durably lies elsewhere: in the grid infrastructure built to host these sites, and in how it is financed. This page does not measure it. RTE itself calls the current reservation system, based on “first come, first served”, “not very binding”, and notes that it can delay or block the connection of other projects; it has announced a reform based instead on “first ready, first served”.

## What these data do not say {#limits}

- **One main producer, and a stakeholder.** All values come from RTE, except the SDES census, cited as a check; RTE grants the reservations and is reforming their queue; distribution-grid consumption is taken from RTE, not read at Enedis.
- **Two quantities that cannot be compared.** Reserved capacity (GW) is neither power drawn nor consumption (TWh); no ratio is computed between them. The {{< dtc-val "util_obs" >}}% rate cited above is RTE's observation of sites connected for two to three years.
- **A breakdown measured on a figure.** The breakdown by status is read from figure 2.3 of the Bilan prévisionnel, to within 0.1 GW, as of {{< dtc-val "date_fig23" >}}; the {{< dtc-val "res_nov2025" >}} GW total is dated end-November. The measured sum, {{< dtc-val "actif_dc" >}} GW, matches it to within 0.1 GW.
- **Pathways, not forecasts.** They rest on assumed materialisation and utilisation rates.
- **Neither water, nor land, nor grid costs** are measured here.

<aside class="encadre">

**A reading by the author, not tested here.** The economist Stéphane Lalut calls [technological debt](/en/technological-debt/) the cost of digital infrastructure converted into commitments that others will bear (working paper [AWP-06](/en/awp/awp-06/)). The figures on this page show that a grid connection reservation is not yet such a commitment; they do not measure those that would be.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, what each constructed order commits, and who bears the burden.
{{< /appel-livre >}}

## Frequently asked questions {#faq}

{{< faq-visible >}}

## Sources {#sources}

- RTE, [*Bilan prévisionnel 2025-2035, La consommation d'électricité*](https://assets.rte-france.com/prod/public/2025-12/2025-12-23-bilan-previsionnel-2025-consommation.pdf) (December 2025, in French): chapter 2.1.3 (reservations, reductions, theoretical consumption, suspension of reservations, connection reform) and 2.5 (data-centre consumption, pathways, assumptions); figure 2.3 (reservations by status, measured by script) and figure 2.10 (pathways).
- RTE, [*Bilan électrique 2025, principaux résultats*](https://assets.rte-france.com/prod/public/2026-02/Bilan-electrique-2025-principaux-resultats.pdf) (February 2026, in French): access rights by sector at end-November 2025, consumption of data centres connected to the transmission and distribution grids.
- RTE, [“Les data centers en chiffres clés”](https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france) (in French), page updated on {{< dtc-val "date_web" >}}: reservations at end-2024 and in May 2026, connected sites, observed utilisation rate, ramp-up time, cited projections.
- SDES, [“La consommation d'électricité des data centers en 2024”](https://www.statistiques.developpement-durable.gouv.fr/la-consommation-delectricite-des-data-centers-en-2024) ({{< dtc-val "date_sdes" >}}): census of centres above 1 GWh and estimate of the whole, an independent check on RTE.

{{< reutiliser figures="figures_data_centers" jeu="data_centers" sources="RTE" donnees="Capacity reserved by data centres (end-2024, November 2025, May 2026), November 2025 breakdown by status, metered, estimated and projected consumption; for each value, its nature (read in the text or measured on the figure) and its source, as CSV in long format." >}}
In November 2025, data centres had reserved {{< dtc-val "res_nov2025" >}} GW of grid connection capacity with RTE, {{< dtc-val "st_2030" >}} GW of it for commissioning from 2030, and reservations totalling about {{< dtc-val "st_abandon" >}} GW had been abandoned since 2023. Those connected to RTE's grid consumed nearly {{< dtc-val "rpt_2025" >}} TWh in 2025; RTE retains {{< dtc-val "l2030" >}} to {{< dtc-val "r2030" >}} TWh in 2030 for all dedicated sites.
{{< /reutiliser >}}
