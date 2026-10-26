---
title: "Radioactive waste: does volume tell the problem?"
url: /en/radioactive-waste-volume-or-radioactivity/
description: "At end-{dr.an_act}, high-level waste made up {dr.ha_vol_a}% of the volume of French radioactive waste and {dr.ha_act}% of its declared radioactivity; its final disposal, planned at Bure (Cigéo), is not yet licensed. Volume, radioactivity and disposal route, category by category (Andra, open data)."
chapo: "Radioactive waste is first counted in cubic metres: {dr.tot5} million at end-{dr.an_vol}. But volume says neither where the radioactivity is nor what remains unresolved. At end-{dr.an_act}, high-level waste made up {dr.ha_vol_a}% of the volume and {dr.ha_act}% of the declared radioactivity; its final disposal is planned at Bure (Cigéo), but not yet licensed."
date: 2026-10-26
lastmod: 2026-10-26
og_title: "Radioactive waste: does volume tell the problem? — S. Lalut"
og_image: "images/og-dechets-radioactifs-en.jpg"
og_image_alt: "Share card: “Volume does not show where the radioactivity is” — share of volume and radioactivity of high-level waste, and of low- and very-low-level waste (Andra, National Inventory)."
donnees: [dechets_radioactifs]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "dechets_radioactifs"
  nom: "Radioactive waste in France: volume, declared radioactivity and location by category (Andra National Inventory)"
  description: "Volumes in conditioned equivalent and declared activity of radioactive waste, by category (HA, MA-VL, FA-VL, FMA-VC, TFA, VTC, outside the balances), for each annual open file of Andra's National Inventory (end-2013 to end-{dr.an_vol}), with the volumes located in Andra's disposal facilities; shares computed by the author."
  couverture_temporelle: "2013/{dr.an_vol}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Volume of radioactive waste", unite: "m³ in conditioned equivalent", description: "by category and year"}
    - {nom: "Declared activity", unite: "becquerels", description: "by category, inventory edition years"}
    - {nom: "Volume in an Andra disposal facility", unite: "m³", description: "FMA-VC and TFA"}
  sources:
    - "https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs"
    - "https://inventaire.andra.fr/"
  mots: ["radioactive waste", "nuclear waste", "high-level waste", "Cigéo", "Andra", "National Inventory", "radioactivity", "disposal", "Malvési", "Cires", "Aube disposal facility"]
  fichiers: ["dechets_radioactifs.csv", "dechets_radioactifs.json"]
faq:
  - question: "What share of the volume of radioactive waste is high-level waste?"
    answer: "At end-{dr.an_act}, the latest edition of the inventory declaring radioactivity, high-level waste accounted for {dr.ha_vol_a}% of the volume of the five categories in Andra's balances and {dr.ha_act}% of the declared radioactivity. At end-{dr.an_vol}, it takes up {dr.ha_m3} m³ in conditioned equivalent, {dr.ha_vol}% of the volume."
  - question: "Is the most radioactive waste disposed of?"
    answer: "Not yet in final form. High-level and long-lived intermediate-level waste, which together hold {dr.ha_mavl_act}% of the declared radioactivity (end-{dr.an_act}), is stored on its production sites: its deep geological disposal, Cigéo, is planned at Bure; after the 2026 public inquiry and the inquiry commission's favourable opinion, the creation licence is still to be decided. Low- and intermediate-level short-lived waste and very-low-level waste, over nine tenths of the volume, have disposal facilities in operation."
  - question: "Where do these figures come from?"
    answer: "From the open files of Andra's National Inventory (waste declared at end-{dr.an_vol}, and at end-{dr.an_act} for activity), read by a script that refuses to publish if a figure stops supporting a sentence of the page; the status of disposal routes comes from Andra's publications. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/dechets-radioactifs-volume-ou-radioactivite.md"  # fiche de conception (regle 12)
  refonte: "2026-10-26"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]
  rang: 45
  nature: "Open data recomputed (Andra, National Inventory)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data as of: {{< dr-val "date_donnees" >}}</span> Andra, National Inventory of radioactive materials and waste, open files (data.gouv.fr): volume and declared radioactivity at end-{{< dr-val "an_act" >}} (latest edition declaring radioactivity), volumes at end-{{< dr-val "an_vol" >}}. Download: <a href="/dechets_radioactifs.csv">CSV</a> · <a href="/dechets_radioactifs.json">JSON</a></p>

## Where is the radioactivity? {#volume-radioactivity}

At end-{{< dr-val "an_act" >}}, the latest year in which Andra's inventory declares the radioactivity of each category, France held {{< dr-val "tot5_a" >}} million cubic metres of radioactive waste in the five categories of its balances, in conditioned equivalent. Over nine tenths of this volume ({{< dr-val "masse_vol_a" >}}%) was low- and intermediate-level short-lived waste and very-low-level waste: it carried {{< dr-val "masse_act" >}}% of the declared radioactivity. High-level waste, for its part, made up {{< dr-val "ha_vol_a" >}}% of the volume, a few thousandths, and {{< dr-val "ha_act" >}}% of the radioactivity; together with long-lived intermediate-level waste, {{< dr-val "ha_mavl_act" >}}%.

The categories that hold most of the declared radioactivity are therefore not those that take up the most volume, and they do not fall under the same management routes. Their radioactivity does not, on its own, measure their dangerousness or the risk to which the population is exposed.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dechets-volume-activite-en-m.svg" width="300" height="871">
    <img src="/img/dechets-volume-activite-en.svg" alt="For each category of radioactive waste, share of volume and share of declared radioactivity, end-{{< dr-val "an_act" >}}, and disposal route. High-level: {{< dr-val "vol_ha" >}}% of volume, {{< dr-val "act_ha" >}}% of radioactivity, deep geological disposal planned. Intermediate-level long-lived: {{< dr-val "vol_mavl" >}}%, {{< dr-val "act_mavl" >}}%, same project. Low-level long-lived: {{< dr-val "vol_favl" >}}%, {{< dr-val "act_favl" >}}%, disposal under study. Low- and intermediate-level short-lived: {{< dr-val "vol_fmavc" >}}%, {{< dr-val "act_fmavc" >}}%, disposal in operation. Very-low-level: {{< dr-val "vol_tfa" >}}%, {{< dr-val "act_tfa" >}}%, disposal in operation." width="720" height="397" loading="lazy">
  </picture>
  <figcaption>Volume in conditioned equivalent and declared radioactivity, in becquerels, for the same year; disposal routes according to Andra (National Inventory, open data; Les Essentiels 2026).</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** In France, at end-{{< dr-val "an_act" >}}, high-level waste made up {{< dr-val "ha_vol_a" >}}% of the volume of radioactive waste and {{< dr-val "ha_act" >}}% of its declared radioactivity; its final disposal, planned at Bure (Cigéo), is not yet licensed.

</div>

Volume has kept growing since: {{< dr-val "tot5" >}} million cubic metres at end-{{< dr-val "an_vol" >}}, including {{< dr-val "ha_m3" >}} m³ of high-level waste, still {{< dr-val "ha_vol" >}}% of the total. Radioactivity is declared only at the inventory's editions.

## What the chart shows, and what it does not {#reading}

Two ways of measuring the problem circulate. The first counts cubic metres: the more waste, the bigger the problem. The second looks at where the radioactivity is and what remains unresolved. The chart shows that the two measures give very different hierarchies: by volume, short-lived and very-low-level waste dominates; by radioactivity, high-level waste.

It also shows that the three long-lived categories (high-level, intermediate- and low-level long-lived) have no final disposal route in operation yet, including low-level long-lived waste, which is barely radioactive. This reflects management constraints linked in particular to half-life, activity level and the properties of the waste; it does not allow the situation to be attributed to lifespan alone.

The inventory declares radioactivity at its editions: {{< dr-val "nb_editions" >}} files record it ({{< dr-val "editions" >}}). In each, high-level waste accounts for between {{< dr-val "ha_ed_bas" >}} and {{< dr-val "ha_ed_haut" >}}% of the recorded radioactivity, and high-level together with long-lived intermediate-level waste for at least {{< dr-val "ha_mavl_ed_bas" >}}%. The available data do not, without further harmonisation, explain the variation from one edition to the next. Part of the volume has no declared radioactivity; assuming it has the average activity of its category, an unverified assumption, the share of high-level waste would be {{< dr-val "ha_act_aj" >}}%.

**What the chart does not show.** The becquerel measures a number of decays per second. It does not directly measure the dose received, the toxicity of a radionuclide, health risk, or the difficulty or cost of management. The chart shows how declared radioactivity is distributed across categories; it ranks neither risks nor costs.

## Where is this waste today? {#disposal}

At end-{{< dr-val "an_vol" >}}, {{< dr-val "stocke_fmavc" >}}% of the volume of low- and intermediate-level short-lived waste is recorded in Andra's disposal facilities: in the Aube, in operation, and in the Manche, closed to new deliveries since 1994 and under surveillance. {{< dr-val "stocke_tfa" >}}% of very-low-level waste is at Cires, in the Aube.

The categories that concentrate the radioactivity have no final disposal yet. According to Andra, high-level and long-lived intermediate-level waste is "produced and stored on its production sites, pending the creation of the disposal facility intended to receive it: Cigéo" (our translation); disposal for low-level long-lived waste is under study.

Cigéo is a deep geological disposal facility planned at Bure (Meuse). Andra applied for its creation licence in January 2023. The public inquiry closed on 16 July 2026, and the inquiry commission issued a favourable opinion in August, with two reservations and two recommendations. An inquiry opinion is not a licence: as of mid-September 2026, the decision on the creation licence was still to be taken.

## What remains outside the balances {#outside-balances}

Some waste does not appear in Andra's balances. The main set is the historical uranium conversion residues at Orano's Malvési site: Andra reports about {{< dr-val "malvesi" >}} m³ (ECRIN facility, evaporation and settling ponds), states that these volumes "are not counted in the balances" and that "the search for a safe long-term management route on the Malvési site is under way" (our translations). Historical disposals, which fall to their holders, come on top.

## What these data do not say {#limits}

- **Radioactivity is neither risk nor cost.** It measures a number of decays per second; danger depends on the radionuclides, their half-life and exposure.
- **One vintage for the comparison.** Volume and radioactivity are compared at end-{{< dr-val "an_act" >}}, the latest edition declaring radioactivity; end-{{< dr-val "an_vol" >}} volumes are given separately, without radioactivity.
- **Volumes without declared radioactivity.** The variant crediting them with the average activity of their category rests on an assumption: it tests the sensitivity of the result, it does not validate it.
- **An unreconciled outside-balance scope.** Since the end-{{< dr-val "an_hors" >}} file, the open file has classified outside the categories of the balances a volume that reaches {{< dr-val "hors" >}} million cubic metres at end-{{< dr-val "an_vol" >}}; its "conversion residues" family ({{< dr-val "rtcu" >}} million m³) does not match the volumes Andra publishes for Malvési. That total is not interpreted here.
- **Waste, not materials.** Radioactive materials (depleted uranium, spent fuel awaiting reprocessing) are not waste under French law and are not included in these figures.
- **The status of disposal routes and of Cigéo is taken from published sources.** It is not computed by the script and is checked at each step of the procedure.

<aside class="encadre">

**A reading by the author, not tested here.** The philosophy of dismantling ecology calls [negative commons](/en/negative-commons/) what a society inherits without having chosen it: waste, polluted soils, infrastructures to close down. The economist Stéphane Lalut reads in it a displaced disorder turned into a material legacy. The figures on this page describe such a legacy; they do not demonstrate that reading.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, what each order leaves behind it and on whom it leaves the burden.
{{< /appel-livre >}}

## Sources {#sources}

- Andra, National Inventory of radioactive materials and waste, [open files of declared waste](https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs) (end-2013 to end-{{< dr-val "an_vol" >}}), read by script; author's calculations: shares by category, activity variant, volumes located in Andra's disposal facilities (identified by site name).
- Andra, [National Inventory](https://inventaire.andra.fr/), *Les Essentiels 2026* and the page "Classification des déchets radioactifs et filières de gestion": status of disposal routes, Malvési volumes and quotations, read on 26 October 2026. Check of the calculation: the volumes by category and disposed volumes published by Andra for end-2024 are found again to within rounding.
- Nuclear safety and radiation protection authority (ASNR), [letter of 30 March 2026](https://reglementation-controle.asnr.fr/Media/Files/demande-d-autorisation-de-creation-de-l-installation-nucleaire-de-base-cigeo) (CODEP-DRC-2026-012666): Cigéo licence application. Prefecture of Haute-Marne, [public inquiry page](https://www.haute-marne.gouv.fr/index.php/Actions-de-l-Etat/CIGEO/Demande-d-autorisation-de-creation-de-Cigeo) (in French), read on 26 October 2026: inquiry dates (18 May to 16 July 2026, after extension), favourable opinion of the commission with two reservations and two recommendations, report online since 14 September 2026, decision by decree in the Conseil d'État still to come. AFP dispatch of 14 September 2026, [as published by Connaissance des énergies](https://www.connaissancedesenergies.org/afp/dechets-nucleaires-avis-favorable-de-la-commission-denquete-pour-cigeo-260914): close of the public inquiry and the commission's opinion.

{{< reutiliser figures="figures_dechets" jeu="dechets_radioactifs" sources="Andra (National Inventory)" donnees="For each annual file of the National Inventory since end-2013: volume in conditioned equivalent and declared activity by category, volume with declared activity, volume located in an Andra disposal facility; the same content is available as CSV, in long format." >}}
In France, at end-{{< dr-val "an_act" >}}, high-level waste made up {{< dr-val "ha_vol_a" >}}% of the volume of radioactive waste and {{< dr-val "ha_act" >}}% of its declared radioactivity. Long-lived waste has no final disposal route in operation yet: disposal of high-level and long-lived intermediate-level waste is planned at Bure (Cigéo), not yet licensed. Volume, for its part, is carried mostly by categories that have a disposal facility in operation.
{{< /reutiliser >}}
