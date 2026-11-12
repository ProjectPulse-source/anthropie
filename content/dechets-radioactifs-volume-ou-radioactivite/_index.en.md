---
title: "Radioactive waste: does volume tell the problem?"
url: /en/radioactive-waste-volume-or-radioactivity/
description: "At end-{dr.an_act}, high-level waste made up {dr.ha_vol_a}% of the volume of radioactive waste recorded in Andra's balances and {dr.ha_act}% of the declared radioactivity (mostly an upper bound, not an exact measurement); its final disposal, planned at Bure (Cigéo), is not yet licensed. Volume, radioactivity and disposal route, category by category (Andra, open data and Les Essentiels 2026)."
chapo: "Radioactive waste is first counted in cubic metres: {dr.tot5} million at end-{dr.an_vol} in Andra's balances. But volume says neither where the radioactivity is nor what remains unresolved. At end-{dr.an_act}, high-level waste made up {dr.ha_vol_a}% of the volume and {dr.ha_act}% of the declared radioactivity (mostly an upper bound, not an exact measurement); its final disposal is planned at Bure (Cigéo), but not yet licensed."
date: 2026-10-26
lastmod: 2026-11-12
journal:  # revisions that change how the page reads
  - {date: 2026-11-12, texte: "Revision: declared radioactivity, mostly an upper bound, stated next to each share and documented in the data file and the chart; the Manche centre in its closure phase, not under surveillance; two rankings that on their own measure neither doses, nor how long the waste remains hazardous, nor cost; Malvési reconciled with the volumes Andra publishes; volumes outside the balances counted in tonnes, not added to cubic metres; status of Cigéo checked as of 12 November 2026."}
og_title: "Radioactive waste: does volume tell the problem? — S. Lalut"
og_image: "images/og-dechets-radioactifs-en.jpg"
og_image_alt: "Share card: “Volume does not show where the radioactivity is” — share of volume and of declared radioactivity (mostly an upper bound) of high-level waste, and of short-lived and very-low-level waste, end-2021 (Andra, National Inventory)."
donnees: [dechets_radioactifs]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "dechets_radioactifs"
  nom: "Radioactive waste in France: volume and declared radioactivity by category, volume located in Andra's facilities (Andra National Inventory)"
  description: "Volumes in conditioned equivalent and declared activity of radioactive waste, by category (HA, MA-VL, FA-VL, FMA-VC, TFA, DSF, VTC, outside the balances), for each annual open file of Andra's National Inventory (end-2013 to end-{dr.an_vol}), with, for FMA-VC and TFA, the volumes located in Andra's facilities; shares computed by the author."
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
    answer: "At end-{dr.an_act}, the latest year for which the inventory declares the radioactivity of each category, high-level waste accounted for {dr.ha_vol_a}% of the volume of the five categories in Andra's balances and {dr.ha_act}% of the declared radioactivity (mostly an upper bound, not an exact measurement). At end-{dr.an_vol}, it takes up {dr.ha_m3} m³ in conditioned equivalent, {dr.ha_vol}% of the volume."
  - question: "Is the most radioactive waste disposed of?"
    answer: "No: it is held in storage — that is, placed temporarily with the intention of retrieving it — and not disposed of, a term French law reserves for potentially permanent emplacement (Environment Code, Article L. 542-1-1). High-level waste and long-lived intermediate-level waste, which together hold {dr.ha_mavl_act}% of the declared radioactivity (end-{dr.an_act}), are stored on the sites that produce or hold them: their deep geological disposal, Cigéo, is planned at Bure; after the 2026 public inquiry and the inquiry commission's favourable opinion, with two reservations, no creation licence decree had been published as of 12 November 2026. Low- and intermediate-level short-lived waste and very-low-level waste, over nine tenths of the volume, have disposal facilities in operation."
  - question: "Where do these figures come from?"
    answer: "From the open files of Andra's National Inventory (waste declared at end-{dr.an_vol}, and at end-{dr.an_act} for activity), read by a script that stops if a figure no longer meets the conditions on which the page's main sentences depend. The status of disposal routes and the Malvési volumes are transcribed from Andra's publications (Les Essentiels 2026, read on 26 October 2026). The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/dechets-radioactifs-volume-ou-radioactivite.md"  # fiche de conception (regle 12)
  refonte: "2026-11-12"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]
  rang: 45
  nature: "Open data recomputed (Andra, National Inventory)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data last updated {{< dr-val "date_donnees" >}}</span> Andra, National Inventory of radioactive materials and waste, open files (data.gouv.fr): volume and declared radioactivity at end-{{< dr-val "an_act" >}} (latest edition declaring radioactivity), volumes at end-{{< dr-val "an_vol" >}}. Download: <a href="/dechets_radioactifs.csv">CSV</a> · <a href="/dechets_radioactifs.json">JSON</a></p>

## Where is the radioactivity? {#volume-radioactivity}

At end-{{< dr-val "an_act" >}}, the latest year for which Andra's inventory declares the radioactivity of each category, France held {{< dr-val "tot5_a" >}} million cubic metres of radioactive waste, in conditioned equivalent, in the five categories of Andra's balances. Over nine tenths of this volume ({{< dr-val "masse_vol_a" >}}%) was low- and intermediate-level short-lived waste and very-low-level waste: it carried {{< dr-val "masse_act" >}}% of the declared radioactivity. High-level waste, for its part, made up {{< dr-val "ha_vol_a" >}}% of the volume — a few thousandths — and {{< dr-val "ha_act" >}}% of the declared radioactivity (mostly an upper bound, not an exact measurement); together with long-lived intermediate-level waste, it held {{< dr-val "ha_mavl_act" >}}% of the declared radioactivity.

The categories that hold most of the declared radioactivity are therefore not those that take up the most volume, and they do not fall under the same management routes. Their radioactivity does not, on its own, measure how hazardous they are or the risk to which the public is exposed.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/dechets-volume-activite-en-m.svg" width="300" height="1009">
    <img src="/img/dechets-volume-activite-en.svg" alt="For each of the five categories of radioactive waste in Andra's balances, share of volume and share of declared radioactivity (mostly an upper bound), end-{{< dr-val "an_act" >}}, and disposal route. High-level: {{< dr-val "vol_ha" >}}% of volume, {{< dr-val "act_ha" >}}% of radioactivity, deep geological disposal planned. Intermediate-level long-lived: {{< dr-val "vol_mavl" >}}%, {{< dr-val "act_mavl" >}}%, same project. Low-level long-lived: {{< dr-val "vol_favl" >}}%, {{< dr-val "act_favl" >}}%, disposal under study. Low- and intermediate-level short-lived: {{< dr-val "vol_fmavc" >}}%, {{< dr-val "act_fmavc" >}}%, disposal in operation. Very-low-level: {{< dr-val "vol_tfa" >}}%, {{< dr-val "act_tfa" >}}%, disposal in operation." width="720" height="425" loading="lazy">
  </picture>
  <figcaption>Volume in conditioned equivalent and declared radioactivity, in becquerels, for the same year; disposal routes according to Andra (National Inventory, open data; Les Essentiels 2026).</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**The result in one sentence.** In France, at end-{{< dr-val "an_act" >}}, high-level waste made up {{< dr-val "ha_vol_a" >}}% of the volume of radioactive waste recorded in Andra's balances and {{< dr-val "ha_act" >}}% of the declared radioactivity (mostly an upper bound, not an exact measurement); its final disposal, planned at Bure (Cigéo), is not yet licensed.

</div>
</div>
</div>

Volume has kept growing since: {{< dr-val "tot5" >}} million cubic metres at end-{{< dr-val "an_vol" >}}, including {{< dr-val "ha_m3" >}} m³ of high-level waste, still {{< dr-val "ha_vol" >}}% of the total. Radioactivity, by contrast, is declared for the bulk of the volume only in the files of the inventory's editions, the latest at end-{{< dr-val "an_act" >}}.

## What the chart shows, and what it does not {#reading}

The two rankings are very different, and the chart sets them side by side: by volume, short-lived and very-low-level waste dominates; by declared radioactivity, high-level waste. But neither, on its own, measures the doses to which a population may be exposed, how long the waste remains hazardous or the cost of management solutions.

The chart also shows that high-level waste and the two long-lived categories (intermediate- and low-level long-lived) have no final disposal route in operation yet, including low-level long-lived waste, which holds only {{< dr-val "act_favl" >}}% of the declared radioactivity. This reflects management constraints linked in particular to half-life, activity level and the properties of the waste; it does not allow the situation to be attributed to lifespan alone.

The radioactivity of each category appears in {{< dr-val "nb_editions" >}} files ({{< dr-val "editions" >}}): declared every year up to the end-2016 data, it has since been declared, for the bulk of the volume, only in the inventory's editions; the files for other years give it for less than a thousandth of the volume. In each of these five files, high-level waste accounts for between {{< dr-val "ha_ed_bas" >}}% and {{< dr-val "ha_ed_haut" >}}% of the radioactivity recorded in the five categories of the balances, and high-level together with long-lived intermediate-level waste for at least {{< dr-val "ha_mavl_ed_bas" >}}%. The available data do not, without further harmonisation, allow these shares to be read as a trend, nor the variation from one edition to the next to be explained. Part of the volume has no declared radioactivity; assuming it has the average activity of its category, an unverified assumption, the share of high-level waste would be {{< dr-val "ha_act_aj" >}}%.

**What the chart does not show.** The becquerel measures a number of decays per second. It does not directly measure the dose received, the toxicity of a radionuclide, health risk, or the difficulty or cost of management. The chart shows how declared radioactivity is distributed across categories; it ranks neither risks nor costs.

## Where is this waste today? {#disposal}

At end-{{< dr-val "an_vol" >}}, {{< dr-val "stocke_fmavc" >}}% of the volume of low- and intermediate-level short-lived waste is recorded in Andra's disposal facilities: the one in the Aube, which is in operation, and the one in the Manche, which has received no waste since 1994 and is in its closure phase. Cires, in the Aube, holds {{< dr-val "stocke_tfa" >}}% of very-low-level waste.

The categories in which the radioactivity is concentrated have no final disposal yet. According to Andra, some high-level and long-lived intermediate-level waste is "produced and stored on its production sites, pending the creation of the disposal facility intended to receive it: Cigéo" (our translation); disposal for low-level long-lived waste is under study.

Cigéo is a deep geological disposal facility planned at Bure (Meuse). Andra applied for Cigéo's creation licence in January 2023. The public inquiry closed on 16 July 2026, and the inquiry commission issued a favourable opinion in August, with two reservations and two recommendations. This opinion is not a licence: the procedure then provides for a preliminary draft decree sent to Andra for comments, an opinion from the Nuclear Safety and Radiation Protection Authority (ASNR), and a decree issued after consulting the Conseil d'État. As of 12 November 2026, no creation licence decree had been published in the Journal officiel.

## What remains outside the balances {#outside-balances}

Some waste does not appear in Andra's balances. This includes the historical uranium conversion residues at Orano's Malvési site: Andra reports about {{< dr-val "malvesi" >}} m³ (ECRIN facility, evaporation and settling ponds) and states that these volumes "are not counted in the balances" and that "the search for a safe long-term management route on the Malvési site is under way" (our translations). Also outside the balances are, in particular, residues from the processing of uranium ore at former mining sites and waste with enhanced natural radioactivity: Andra counts them in tonnes (tens of millions), so they cannot be added to these cubic metres. Historical disposal sites, which are the responsibility of their holders, are also absent from them.

## What these data do not say {#limits}

- **Radioactivity is neither risk nor cost.** It is a number of decays per second; danger depends on the radionuclides, their half-lives and exposure.
- **Declared radioactivity, mostly an upper bound.** In the end-{{< dr-val "an_act" >}} file, {{< dr-val "maj_5" >}}% of the declared radioactivity of the five categories ({{< dr-val "maj_ha" >}}% for high-level waste) carries the “&lt;” sign, which, according to the inventory's data dictionary, flags an upper-bound activity: a maximum, not an exact measurement. The page's shares are shares of these declared values; the data file gives, by category and year, the declared activity and its upper-bound part.
- **One vintage for the comparison.** Volume and radioactivity are compared at end-{{< dr-val "an_act" >}}, the latest year for which the inventory declares the radioactivity of each category; end-{{< dr-val "an_vol" >}} volumes are given separately, without radioactivity.
- **Volumes without declared radioactivity.** The variant crediting them with the average activity of their category rests on an assumption: it tests the sensitivity of the result; it does not validate it.
- **An unreconciled scope outside the balances.** Since the end-{{< dr-val "an_hors" >}} file, the open file has classified, outside the categories of the balances, a volume that reaches {{< dr-val "hors" >}} million cubic metres at end-{{< dr-val "an_vol" >}}; its uranium conversion residues family ({{< dr-val "rtcu" >}} million m³) includes, in addition to the volumes Andra publishes for Malvési, an entry for waste rock from a former sulphur mine that Andra does not count in those volumes. That total is not interpreted here.
- **Waste, not materials.** Radioactive materials (depleted uranium, spent fuel awaiting reprocessing) are not waste under French law, unless the administrative authority reclassifies them as such (Environment Code, Articles L.&nbsp;542-1-1 and L.&nbsp;542-13-2), and are not included in these figures.
- **The status of disposal routes and of Cigéo is taken from published sources.** It is not computed by the data-reading script: the status of disposal routes is taken from Andra's *Les Essentiels 2026*, and that of Cigéo was checked on 12 November 2026 on Légifrance (Journal officiel) and on the Meuse prefecture's web page.

<aside class="encadre">

**A reading by the author, not tested here.** The philosophy of the ecology of dismantling calls [negative commons](/en/negative-commons/) what a society inherits without having chosen it: waste, polluted soils, infrastructures to close down. The economist Stéphane Lalut reads it as a displaced disorder turned into a material legacy. The figures on this page describe such a legacy; they do not demonstrate that reading.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="To take the question further" avis="non" >}}
*ANTHROPY* follows, over the long run, what each constructed order leaves behind and on whom it leaves the burden.
{{< /appel-livre >}}

## Frequently asked questions {#faq}

{{< faq-visible >}}

## Sources {#sources}

- Andra, National Inventory of radioactive materials and waste, [open files of declared waste](https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs) (end-2013 to end-{{< dr-val "an_vol" >}}), read by script; author's calculations: shares by category, activity variant, volumes located in Andra's disposal facilities (identified by site name).
- Andra, [National Inventory](https://inventaire.andra.fr/), *Les Essentiels 2026* and the page "Classification des déchets radioactifs et filières de gestion": status of disposal routes, Malvési volumes and quotations, read on 26 October 2026. Calculation check: the volumes by category published by Andra for end-2024 are reproduced to within rounding; the disposed volumes, to within a few hundred cubic metres, as the script counts what is located in an Andra facility.
- Nuclear Safety and Radiation Protection Authority (ASNR), [letter of 30 March 2026](https://reglementation-controle.asnr.fr/Media/Files/demande-d-autorisation-de-creation-de-l-installation-nucleaire-de-base-cigeo) (CODEP-DRC-2026-012666): Cigéo licence application. Prefecture of Haute-Marne, [public inquiry page](https://www.haute-marne.gouv.fr/index.php/Actions-de-l-Etat/CIGEO/Demande-d-autorisation-de-creation-de-Cigeo) (in French), read on 26 October 2026: inquiry dates (18 May to 16 July 2026, after extension), favourable opinion of the commission with two reservations and two recommendations, report online since 14 September 2026, decision still to come, by decree issued after consulting the Conseil d'État. Légifrance, search for “Cigéo” in the Journal officiel, and Prefecture of Meuse, [creation licence application page](https://www.meuse.gouv.fr/Actions-de-l-Etat/CIGEO/Demande-d-autorisation-de-creation-de-Cigeo) (in French), read on 12 November 2026: no creation licence decree published, no step in the procedure after 14 September 2026. AFP dispatch of 14 September 2026, [as published by Connaissance des énergies](https://www.connaissancedesenergies.org/afp/dechets-nucleaires-avis-favorable-de-la-commission-denquete-pour-cigeo-260914): close of the public inquiry and the commission's opinion.

{{< reutiliser figures="figures_dechets" jeu="dechets_radioactifs" sources="Andra, National Inventory" donnees="In the CSV, in long format, for each annual file of the National Inventory since end-2013: volume in conditioned equivalent and declared activity by category, volume with declared activity, upper-bound declared activity and, for FMA-VC (low- and intermediate-level short-lived) and TFA (very-low-level), volume located in an Andra facility (not identified for 2013, 2014 and 2023); the JSON gives the computed shares, including those drawn by the chart (volume and declared radioactivity for the same year)." >}}
In France, at end-{{< dr-val "an_act" >}}, high-level waste made up {{< dr-val "ha_vol_a" >}}% of the volume of radioactive waste recorded in Andra's balances and {{< dr-val "ha_act" >}}% of the declared radioactivity (mostly an upper bound, not an exact measurement). High-level waste and the two long-lived categories (intermediate- and low-level long-lived) have no final disposal route in operation yet: disposal of high-level and long-lived intermediate-level waste is planned at Bure (Cigéo) but not yet licensed. Volume, for its part, lies mostly in categories that have a disposal facility in operation.
{{< /reutiliser >}}
