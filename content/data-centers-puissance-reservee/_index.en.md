---
title: "Data centres: do reserved gigawatts foretell consumption?"
url: /en/data-centres-reserved-capacity/
description: "In November 2025, data centres had reserved {dtc.res_nov2025} GW of grid connection capacity with RTE, {dtc.st_2030} GW of it for commissioning from 2030; those connected to RTE's grid consumed nearly {dtc.rpt_2025} TWh in 2025. Reserved capacity, timing, abandonments and consumption in France, from RTE's publications."
chapo: "The figure in circulation is the one for reservations: nearly {dtc.res_mai2026} gigawatts on RTE's transmission grid in May 2026, against about {dtc.res_fin2024} at end-2024. But reserved capacity is not consumption. In November 2025, more than half of the reserved capacity was for commissioning from 2030; other reservations have already been abandoned, and the data centres connected to the transmission grid consumed nearly {dtc.rpt_2025} terawatt-hour in 2025."
date: 2026-10-27
lastmod: 2026-11-12
journal:  # revisions that change how the page reads
  - {date: 2026-11-05, texte: "Clarification: next to the 10 TWh of RTE's web page, the Bilan prévisionnel also gives 5 to 10 TWh in 2024 including in-house data centres; the web page does not state its scope."}
  - {date: 2026-11-12, texte: "Revision: the 18 GW referred to RTE's transmission grid; the SDES census presented as a cross-check, not as an independent control; multiple reservations noted by RTE for all applicants; the two uses of 20% told apart (observation, assumption); conditions and effects of a suspension, according to RTE; RTE's reading tied to its texts; a reservation guarantees access under the terms of its contract."}
og_title: "Data centres: do reserved gigawatts foretell consumption? — S. Lalut"
og_image: "images/og-data-centers-en.jpg"
og_image_alt: "Share card: “Reserved is not consumed” — capacity reserved by data centres with RTE and consumption of the centres connected to its grid (RTE)."
donnees: [data_centers]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "data_centers"
  nom: "Data centres in France: grid connection capacity reserved with RTE, breakdown by status and electricity consumption (RTE publications, SDES census)"
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
  - question: "How much capacity have data centres reserved on the French transmission grid?"
    answer: "According to RTE, data centres had reserved nearly {dtc.res_mai2026} gigawatts on its transmission grid in May 2026, for about {dtc.projets_2026} projects, against about {dtc.res_fin2024} GW at end-2024. In November 2025, of {dtc.res_nov2025} GW reserved, {dtc.st_2030} GW was for commissioning from 2030; reservations totalling about {dtc.st_abandon} GW had been abandoned since 2023 (breakdown and abandonments measured on an RTE figure, to within a tenth of a gigawatt)."
  - question: "How much electricity do data centres consume in France?"
    answer: "Dedicated-site data centres connected to RTE's transmission grid consumed nearly {dtc.rpt_2025} TWh in 2025, against {dtc.rpt_2024} TWh in 2024; those on Enedis's distribution grid, {dtc.enedis_2024} TWh in 2024. RTE estimates the consumption of all dedicated sites at {dtc.sd_bas} to {dtc.sd_haut} TWh in 2024, and at {dtc.int_bas} to {dtc.int_haut} TWh including the in-house data centres of companies and public bodies; its two pathways, which are assumptions, give {dtc.l2030} to {dtc.r2030} TWh in 2030 for dedicated sites."
  - question: "Where do these figures come from?"
    answer: "From three RTE publications (Bilan prévisionnel 2025-2035, Bilan électrique 2025, web page “Les data centers en chiffres clés”) and, as a cross-check, the SDES census (July 2026), which follows its own method but takes its consumption figures primarily from Enedis and RTE databases. These publications are downloaded by a script that reads each value in the dataset from the sentence or figure label that contains it, measures the breakdown by status on a figure in the Bilan prévisionnel, and stops if a value no longer meets the conditions on which the page's main sentences depend. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  accueil: 5  # ordre sur l'accueil (maquette du 04/11/2026, arbitrage PRO-20261104-181823)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/data-centers-puissance-reservee.md"  # fiche de conception (regle 12)
  refonte: "2026-11-12"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]
  rang: 47
  nature: "RTE publications read and measured"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data last updated {{< dtc-val "date_donnees" >}}</span> RTE, Bilan prévisionnel 2025-2035 (December 2025), Bilan électrique 2025 (February 2026) and web page “Les data centers en chiffres clés” (updated {{< dtc-val "date_web" >}}); SDES, data-centre census ({{< dtc-val "date_sdes" >}}). Values read in the text, breakdown by status measured on a figure. Download: <a href="/data_centers.csv">CSV</a> · <a href="/data_centers.json">JSON</a></p>

## What is reserved, what is consumed {#reserved-consumed}

In May 2026, according to RTE, France's transmission system operator, data centres had reserved nearly {{< dtc-val "res_mai2026" >}} gigawatts (GW) of connection capacity on its grid, for about {{< dtc-val "projets_2026" >}} projects. At end-2024, some forty projects totalled about {{< dtc-val "res_fin2024" >}} GW: in less than a year and a half, reserved capacity more than tripled. At end-November 2025, of the roughly {{< dtc-val "tot_nov2025" >}} GW of grid access rights (that is, reserved connection capacity) granted by RTE to large projects, data centres held {{< dtc-val "res_nov2025" >}} GW, ahead of hydrogen ({{< dtc-val "tot_h2" >}} GW) and industry ({{< dtc-val "tot_ind" >}} GW).

Consumption, by contrast, is measured in terawatt-hours (TWh). Dedicated-site data centres connected to RTE's transmission grid consumed {{< dtc-val "rpt_2024" >}} TWh in 2024 and nearly {{< dtc-val "rpt_2025" >}} TWh in 2025; those on the distribution grid run by Enedis, {{< dtc-val "enedis_2024" >}} TWh in 2024. RTE estimates the consumption of all dedicated sites at {{< dtc-val "sd_bas" >}} to {{< dtc-val "sd_haut" >}} TWh in 2024, and at {{< dtc-val "int_bas" >}} to {{< dtc-val "int_haut" >}} TWh including the in-house data centres of companies and public bodies. The statistical service of the French ministry for the ecological transition (SDES), which counts the centres itself but takes their consumption figures primarily from the Enedis and RTE databases, reaches the same order of magnitude: {{< dtc-val "sdes_n" >}} centres using more than 1 GWh a year consumed nearly {{< dtc-val "sdes_twh" >}} TWh in 2024, and the total for all centres is estimated at {{< dtc-val "sdes_bas" >}} to {{< dtc-val "sdes_haut" >}} TWh. The two estimates do not cover exactly the same scope: they cross-check each other without being interchangeable.

**Reserved capacity is not consumption.** A reservation guarantees access to the grid, under the terms of its contract and the connection rules; it guarantees neither that the site will be built, nor when it will be commissioned, nor at what power it will run. The chart places the two quantities one above the other, each on its own scale, without calculating any ratio between them.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/data-centers-reserve-consomme-en-m.svg" width="300" height="1252">
    <img src="/img/data-centers-reserve-consomme-en.svg" alt="Two panels. Top: grid connection capacity reserved by data centres with RTE: about {{< dtc-val "res_fin2024" >}} GW at end-2024, {{< dtc-val "res_nov2025" >}} GW in November 2025, of which {{< dtc-val "st_avant2030" >}} GW for commissioning before 2030, {{< dtc-val "st_2030" >}} GW from 2030 and {{< dtc-val "st_suspendu" >}} GW suspended, nearly {{< dtc-val "res_mai2026" >}} GW in May 2026; {{< dtc-val "rac_gw" >}} GW of combined capacity already connected to RTE's grid in {{< dtc-val "mois_web" >}} ({{< dtc-val "sites_rte" >}} sites); about {{< dtc-val "st_abandon" >}} GW abandoned since 2023. Bottom: consumption: {{< dtc-val "rpt_2024" >}} TWh in 2024 and nearly {{< dtc-val "rpt_2025" >}} TWh in 2025 on RTE's grid, {{< dtc-val "sd_bas" >}} to {{< dtc-val "sd_haut" >}} TWh estimated for all dedicated sites in 2024, {{< dtc-val "l2030" >}} to {{< dtc-val "r2030" >}} TWh in 2030 and {{< dtc-val "l2035" >}} to {{< dtc-val "r2035" >}} TWh in 2035 in RTE's slow and fast decarbonisation pathways." width="720" height="628" loading="lazy">
  </picture>
  <figcaption>Reserved grid connection capacity (GW) and electricity consumption (TWh per year) of data centres, according to RTE; November 2025 breakdown measured on figure 2.3 of the Bilan prévisionnel 2025-2035.</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**The result in one sentence.** In November 2025, data centres had reserved {{< dtc-val "res_nov2025" >}} GW of grid connection capacity with RTE, {{< dtc-val "st_2030" >}} GW of it for commissioning from 2030; those connected to RTE's grid consumed nearly {{< dtc-val "rpt_2025" >}} TWh in 2025.

</div>
</div>
</div>

## Does a reservation foretell consumption? {#timing}

From reservation to consumption, each step carries its own uncertainty: the project has to be built and connected; once connected, it draws only part of the reserved capacity, and only after a ramp-up; finally, how long that capacity is drawn is what turns it into terawatt-hours consumed.

The reservation figure lends itself to two readings. The first reads it as consumption that is announced, and imminent. The second reads it as an option on the grid, part of which will materialise slowly and part never, in proportions no one knows: this is the reading of RTE, which grants these reservations and warns that not all connection requests will materialise. This reading is not neutral, however: RTE uses it to argue for reforming the connection queue.

The reservations themselves settle one point between the two readings: timing. On {{< dtc-val "date_fig23" >}}, of the capacity reserved by data centres (measured on an RTE figure, to within 0.1 GW), {{< dtc-val "st_travaux" >}} GW was under construction, {{< dtc-val "st_2529" >}} GW signed for commissioning between 2025 and 2029, {{< dtc-val "st_2030" >}} GW for commissioning from 2030 and {{< dtc-val "st_suspendu" >}} GW suspended. More than half of the reserved capacity therefore targeted 2030 or later. And since 2023, reservations totalling about {{< dtc-val "st_abandon" >}} GW had been abandoned, against {{< dtc-val "st_raccorde" >}} GW of projects actually connected. According to RTE's web page updated on {{< dtc-val "date_web" >}}, the {{< dtc-val "sites_rte" >}} data centres directly connected to its grid, whatever their connection date, total {{< dtc-val "rac_mw" >}} megawatts.

Three mechanisms, found in RTE's Bilan prévisionnel and on its web page, separate reservation from consumption. First, across all connection requests, and not only those of data centres, RTE observes that some developers have, on occasion, secured grid access at several points for what are in fact similar projects. Second, sites ramp up slowly: according to the main operators, cited by RTE, it takes {{< dtc-val "montee" >}} to reach about {{< dtc-val "montee_pct" >}}% of the capacity requested, because servers, which are very expensive, are installed only as usage grows. Finally, the power drawn stays below the connection capacity: RTE observes that data centres that have been connected to its grid for two to three years currently use, on average, only {{< dtc-val "util_obs" >}}% of the capacity they requested.

**The chart above settles a question of timing, not of volume.** It shows that reserved capacity translates into consumption neither immediately nor in full; it does not say what share will materialise by 2035.

## What RTE projects {#pathways}

In its Bilan prévisionnel 2025-2035, RTE adopts two pathways for the consumption of dedicated-site data centres: {{< dtc-val "l2030" >}} to {{< dtc-val "r2030" >}} TWh in 2030, {{< dtc-val "l2035" >}} to {{< dtc-val "r2035" >}} TWh in 2035. The higher one assumes that about {{< dtc-val "concret_r" >}}% of the projects that requested a transmission-grid connection for commissioning before 2030 materialise ({{< dtc-val "concret_r_gw" >}} GW), and that these sites use on average {{< dtc-val "util_2030" >}}% of their connection capacity by then; the lower one, a materialisation rate of about {{< dtc-val "concret_l" >}}%. These are assumptions, not measurements.

RTE itself gives the order of magnitude of what these assumptions set aside: if all the roughly {{< dtc-val "tot_nov2025" >}} GW reserved by large projects (data centres, hydrogen and industry together) ran at full power all year, consumption would theoretically reach about {{< dtc-val "theo_twh" >}} TWh, “a level out of all proportion” to its assumptions.

RTE's publications do not all give the same figures. The RTE web page “Les data centers en chiffres clés”, updated on {{< dtc-val "date_web" >}}, attributes to the same Bilan prévisionnel a consumption of {{< dtc-val "w30_bas" >}} to {{< dtc-val "w30_haut" >}} TWh in 2030 and {{< dtc-val "w35_bas" >}} to {{< dtc-val "w35_haut" >}} TWh in 2035 “in a rapid decarbonisation pathway”. Elsewhere, without referring to the Bilan prévisionnel, it puts the current consumption of data centres at about {{< dtc-val "web_conso" >}} TWh. The published document gives {{< dtc-val "r2030" >}} TWh in 2030 and {{< dtc-val "r2035" >}} TWh in 2035 for that pathway; for 2024, it gives {{< dtc-val "sd_bas" >}} to {{< dtc-val "sd_haut" >}} TWh for dedicated sites, and {{< dtc-val "int_bas" >}} to {{< dtc-val "int_haut" >}} TWh when in-house data centres are added. The web page does not say whether its {{< dtc-val "web_conso" >}} TWh covers dedicated sites only or in-house data centres as well, and does not explain the gap between its pathway figures and those of the published document. This page, by contrast, follows the published document.

## Does a reservation already commit the public? {#commitment}

Not irreversibly yet. At the holder's request, typically when the project runs into difficulty obtaining its regulatory permits, a reservation can be suspended for one year, renewable once: the capacity remains guaranteed, but, according to RTE, the financial and timing conditions no longer apply and may be revised if the project is relaunched. A reservation can also be abandoned: this happened to about {{< dtc-val "st_abandon" >}} GW of data-centre reservations between 2023 and {{< dtc-val "date_fig23" >}}.

What could commit the public for the long term lies elsewhere: in the grid infrastructure built to host these sites, and in how it is financed. This page measures neither. RTE itself calls the current reservation system “not very binding” for project developers: operating on a “first come, first served” basis, it can, in some areas, delay or block the connection of other projects; RTE has announced a reform based instead on “first ready, first served”.

## What these data do not say {#limits}

- **One main producer, itself a stakeholder.** All values come from RTE, except those of the SDES census, cited as a cross-check; RTE grants the reservations and is reforming their queue; the consumption of data centres on the distribution grid is taken from RTE, not from Enedis directly.
- **Two quantities that cannot be compared.** Reserved capacity (GW) is neither power drawn nor consumption (TWh); no ratio is computed between them. Likewise, the {{< dtc-val "util_obs" >}}% rate observed by RTE covers sites that have been connected for two to three years; the {{< dtc-val "util_2030" >}}% rate of the higher pathway for 2030 is an assumption.
- **A breakdown measured on a figure.** The breakdown by status as of {{< dtc-val "date_fig23" >}} is read from figure 2.3 of the Bilan prévisionnel, to within 0.1 GW; the {{< dtc-val "res_nov2025" >}} GW total is dated end-November. The measured sum, {{< dtc-val "actif_dc" >}} GW, matches it to within 0.1 GW.
- **Pathways, not forecasts.** They rest on assumed materialisation and utilisation rates.
- **Neither water, nor land, nor grid costs** are measured here.

<aside class="encadre">

**A reading by the author, not tested here.** The economist Stéphane Lalut uses the term [technological debt](/en/technological-debt/) for the cost of digital infrastructure converted into commitments that others will bear (working paper [AWP-06](/en/awp/awp-06/)). The figures on this page show that a reservation remains revocable by its holder; they measure neither what it may already impose on other projects, by delaying their connection, nor the commitments that would turn it into such a debt.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, the commitments each constructed order entails, and who bears the burden.
{{< /appel-livre >}}

## Frequently asked questions {#faq}

{{< faq-visible >}}

## Sources {#sources}

- RTE, [*Bilan prévisionnel 2025-2035, La consommation d'électricité*](https://assets.rte-france.com/prod/public/2025-12/2025-12-23-bilan-previsionnel-2025-consommation.pdf) (December 2025, in French): sections 2.1.3 (reservations, reductions, theoretical consumption, suspension of reservations, connection reform) and 2.5 (data-centre consumption, pathways, assumptions); figure 2.3 (reservations by status, measured by script) and figure 2.10 (pathways).
- RTE, [*Bilan électrique 2025, principaux résultats*](https://assets.rte-france.com/prod/public/2026-02/Bilan-electrique-2025-principaux-resultats.pdf) (February 2026, in French): access rights by sector at end-November 2025, consumption of data centres connected to the transmission grid and to Enedis's distribution grid.
- RTE, [“Les data centers en chiffres clés”](https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france) (in French), page updated on {{< dtc-val "date_web" >}}: reservations at end-2024 and in May 2026, connected sites, observed utilisation rate, ramp-up time, cited projections.
- SDES, [“La consommation d'électricité des data centers en 2024”](https://www.statistiques.developpement-durable.gouv.fr/la-consommation-delectricite-des-data-centers-en-2024) ({{< dtc-val "date_sdes" >}}): census of centres above 1 GWh and estimate of the total, a cross-check on RTE's figures (the SDES takes its consumption figures primarily from Enedis and RTE databases).

{{< reutiliser figures="figures_data_centers" jeu="data_centers" sources="RTE and SDES" donnees="Capacity reserved by data centres (end-2024, November 2025, May 2026), the November 2025 breakdown by status, and metered, estimated and projected consumption; for each value, its nature (read in the text or measured on the figure) and its source, as CSV in long format." >}}
In November 2025, data centres had reserved {{< dtc-val "res_nov2025" >}} GW of grid connection capacity with RTE, {{< dtc-val "st_2030" >}} GW of it for commissioning from 2030, and reservations totalling about {{< dtc-val "st_abandon" >}} GW had been abandoned since 2023 (breakdown and abandonments measured on an RTE figure). Data centres connected to RTE's grid consumed nearly {{< dtc-val "rpt_2025" >}} TWh in 2025. RTE's two pathways, which are assumptions, give {{< dtc-val "l2030" >}} to {{< dtc-val "r2030" >}} TWh in 2030 for all dedicated sites.
{{< /reutiliser >}}
