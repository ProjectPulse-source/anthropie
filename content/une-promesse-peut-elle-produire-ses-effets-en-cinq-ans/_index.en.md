---
title: "Can a campaign promise produce results within five years?"
url: /en/can-a-campaign-promise-produce-results-within-five-years/
description: "How long does it take to train a general practitioner in France, and what happens before? The length of the curriculum written in the texts in force, compared with the presidential term, and admissions to medical studies since 1972. Open data."
chapo: "The test case of training general practitioners in France. The time of the decision and the time of its effects do not necessarily coincide. Under the rules in force for students who start the third cycle from 2023, the standard training pathway to become a general practitioner takes at least {del.duree} years from the first year, {del.nfois} the length of a presidential term. This does not mean that no effect appears before: students provide care during their training, under supervision."
date: 2026-10-06
lastmod: 2026-10-06
# English version of tab 4 of the "Presidential promises" dossier (FR: content/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_delais.json
# (scripts/update_promesses_delais.py), whose guards cover both languages. The Constitution is quoted in the English
# translation published by the Conseil constitutionnel; other French texts in French, followed by our translation.
donnees: [promesses_delais]
og_title: "Can a campaign promise produce results within five years? The test case of training doctors in France — S. Lalut"
og_image: "images/og-delais-promesse-en.jpg"
og_image_alt: "Share card: \"At least 10 years to train a general practitioner. Twice the length of a presidential term.\" Two bars on the same scale: the general practice curriculum in three cycles, and a presidential term; comparison of scale only."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_delais"
  nom: "Length of the general practice curriculum and admissions to medical studies in France, 1972-2025"
  description: "Minimum durations of the general practice curriculum read in the texts in force (order of 8 April 2013, art. 1; Education Code, art. L632-2; Law no. 2022-1616, art. 37) and length of the presidential term (Constitution, art. 6); places filled in medical studies from 1972 to 2020 (DREES, Dossier no. 76, source ONDPS) and admissions from 2021 to 2025 (ONDPS); share of practising doctors who qualified abroad in 2012 and 2026 (DREES, RPPS)."
  couverture_temporelle: "1972/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Places filled, then admissions, in medical studies", unite: "students per year"}
    - {nom: "Minimum durations of the curriculum and of the term", unite: "semesters or years"}
    - {nom: "Practising doctors who qualified abroad", unite: "doctors on 1 January"}
  sources:
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046812307"
    - "https://drees.solidarites-sante.gouv.fr/sites/default/files/2021-03/DD76_0.pdf"
  mots: ["doctors", "medical studies", "numerus clausus", "general practice", "presidential term", "France", "political promises"]
  fichiers: ["promesses_delais.csv", "promesses_delais.json"]
faq:
  - question: "How long does it take to train a general practitioner in France?"
    answer: "Under the rules in force for students who start the third cycle from the 2023 academic year, at least {del.duree} years from the first year: {del.cycle1} semesters of first cycle, {del.cycle2} semesters of second cycle (order of 8 April 2013), then a third cycle in general practice lasting four years (Education Code, art. L632-2). This is a minimum duration, without repeating a year, interruption or alternative-entry route. The last year is spent as an internship, under a regime of supervised autonomy."
  - question: "Does a rise in admissions produce newly trained general practitioners within five years?"
    answer: "Not for the students who enter the first year at that point: under the rules in force for those who start the third cycle from 2023, their full curriculum takes at least {del.duree} years. Doctors in training nevertheless provide care before it ends, under supervision, as provided for by the Education Code (art. L632-2) and the Public Health Code (art. R6153-1-2)."
  - question: "How many students enter medical studies in France?"
    answer: "{del.admis_2025} in 2025, for {del.capacites_2025} places, according to the ONDPS; {del.admis_2021_2025} from 2021 to 2025. Places had been divided by {del.rapport_baisse} between 1972 ({del.places_1972}) and {del.an_min} ({del.places_min}), before rising again. The scope of places changed in 2010-2011 (alternative-entry routes (passerelles) and reorientation entries (droit au remords) included), and since 2021 the series falls under the numerus apertus regime."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 40
  nature: "Texts in force and DREES and ONDPS series, checked; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "Can a campaign promise produce results within five years?"
  court: "Time"
  role: "clocks and capacities"
---

{{< reutiliser-ancre >}}

The time of the decision and the time of its effects do not necessarily coincide. Training doctors gives a clear measure of this, because its length is written in the texts. This page compares that length with the presidential term, shows what acts before the curriculum ends, and traces the number of places since 1972. All durations are read in the texts in force, and none is entered by hand. The Constitution is quoted in the English translation published by the Conseil constitutionnel; other French texts in French, followed by our translation.

**Short answer.** For students entering the first year, completing training as a general practitioner does not fit within a five-year term under the current rules. This does not mean the measure would have no effect before: students provide care during their training.

## How long does it take to train a general practitioner? {#duree-du-cursus}

The first and second cycles each comprise {{< del-val "cycle1" >}} semesters. The third cycle in general practice lasts four years for students who started it from the 2023 academic year. The presidential term lasts five years.

{{< figure-svg fichier="delais-cursus-en" alt="Two bars on the same scale, in years. Above, the general practice curriculum in three cycles, the last year under supervised autonomy. Below, a presidential term, half as long. The values are in the text that follows." >}}Minimum durations written in the texts in force, without repeating a year, interruption or alternative-entry route. Comparison of scale only: it measures neither the effect of a policy nor the date on which its first effects can appear.{{< /figure-svg >}}

{{< fig-actions id="cursus" >}}

<div class="resultat-phrase">

**The finding in one sentence.** Under the rules in force for students who entered the third cycle from the start of the 2023 academic year, the standard training pathway to become a general practitioner in France takes at least {{< del-val "duree" >}} years from the first year, {{< del-val "nfois" >}} the length of a presidential term.

</div>

<details class="repli"><summary>The texts that set these durations, quoted word for word</summary>

- **First cycle** (order of 8 April 2013, art. 1): «&nbsp;{{< del-val "cit_cycle1" >}}&nbsp;» [our translation: "{{< del-val "cit_cycle1_tr" >}}"].
- **Second cycle** (same article): «&nbsp;{{< del-val "cit_cycle2" >}}&nbsp;» [our translation: "{{< del-val "cit_cycle2_tr" >}}"].
- **Third cycle in general practice** (Education Code, art. L632-2): a third cycle «&nbsp;{{< del-val "cit_mg" >}}&nbsp;» [our translation: "{{< del-val "cit_mg_tr" >}}"].
- **Application** (Law no. 2022-1616 of 23 December 2022, art. 37, II): «&nbsp;{{< del-val "cit_37" >}}&nbsp;» [our translation: "{{< del-val "cit_37_tr" >}}"]
- **Term** (Constitution, art. 6, English translation published by the Conseil constitutionnel): "{{< del-val "cit_art6a_en" >}}"

These quotations are extracted from the official texts by the script that produces the page, and checked word for word at each run; the durations in the figure are calculated from the words «&nbsp;six semestres&nbsp;», «&nbsp;quatre années&nbsp;» and «&nbsp;cinq ans&nbsp;», and the script recalculates their ratio at each run. Other specialties have third cycles of different lengths, which this page does not describe.

</details>

## Do students provide care before the end of the curriculum? {#avant-la-fin}

Yes, and the texts organise it. «&nbsp;{{< del-val "cit_supervision" >}}&nbsp;» [our translation: "{{< del-val "cit_supervision_tr" >}}"] (Education Code, art. L632-2). The Public Health Code specifies the regime of the *docteur junior*, a doctor in the final supervised phase of training: «&nbsp;{{< del-val "cit_dj1" >}}&nbsp;» [our translation: "{{< del-val "cit_dj1_tr" >}}"] But «&nbsp;{{< del-val "cit_dj2" >}}&nbsp;» [our translation: "{{< del-val "cit_dj2_tr" >}}"] (art. R6153-1-2). Doctors in training therefore provide care, under the regime these texts provide for; the texts do not measure its share of all care.

This length of training does not, on its own, describe the number of doctors already in practice. Separately, on 1 January 2026, according to the DREES, {{< del-val "etr_26" >}} of the {{< del-val "tot_26" >}} practising doctors, or {{< del-val "etr_p26" >}}%, had obtained their diploma abroad, against {{< del-val "etr_p12" >}}% in 2012. This is a stock present at a date, not the number of arrivals in a year, and the place of the diploma does not tell nationality. This comparison does not measure any compensation of French training capacity by diplomas obtained abroad.

## How many students start medical studies? {#admissions}

{{< figure-svg fichier="delais-admissions-en" alt="Annual bars of admissions to medical studies from 1972 to 2025: a fall to a minimum in the early 1990s, then a rise; two dotted lines mark the changes of scope of 2010-2011 and 2021. The values are in the text that follows." >}}Places filled in medical studies from 1972 to 2020 (DREES, source ONDPS), then admissions from 2021 to 2025 (ONDPS), by year. Each bar shows the places filled or the admissions attached to the year published by the source; no value is shifted to an assumed year of practice.{{< /figure-svg >}}

{{< fig-actions id="admissions" >}}

**Do not mechanically shift these bars by ten years to infer a year of practice**: the rules on duration have changed, students provide care before the end of the curriculum, and this series does not follow students individually until they practise.

Places were divided by {{< del-val "rapport_baisse" >}} between 1972 ({{< del-val "places_1972" >}}) and {{< del-val "an_min" >}} ({{< del-val "places_min" >}}), then rose again, with changes of scope marked on the series. According to the ONDPS, {{< del-val "admis_2021_2025" >}} students were admitted from 2021 to 2025, {{< del-val "hausse_quinquennale" >}}% more than in 2016-2020 ({{< del-val "admis_2016_2020" >}}), and {{< del-val "admis_2025" >}} in 2025 for {{< del-val "capacites_2025" >}} places.

Two breaks can be seen in the figure. Until 2009, the series counts only the main numerus clausus; from 2011, it includes alternative-entry routes (passerelles) and reorientation entries (droit au remords) (DREES note). Since 2021, the series falls under the numerus apertus regime; the ONDPS publishes the numbers admitted.

<details class="repli"><summary>What was checked, and the gap that remains</summary>

Admissions from 2021 to 2025 are read on an ONDPS figure published as an image; their sum is checked against the total printed by the ONDPS, and this total, like the 2025 admissions, is found in the text of the document. The DREES series is compared with the five-year totals published by the ONDPS: it matches exactly for 2001-2005, 2006-2010 and 2011-2015. For 2016-2020, the sum of the DREES values exceeds the ONDPS total by {{< del-val "ecart_2016_2020" >}} places, about {{< del-val "ecart_pct" >}}% of that total; the DREES value for 2020 carries an asterisk whose legend was not found. The gap is published, not corrected.

</details>

## What this page does not say {#limites}

It does not say how many doctors will practise in ten years, nor whether access to care will improve: the number of doctors in practice also depends on departures, doctors who qualified abroad, choices of specialty and places of practice, which none of these series measures. It does not link a cohort of admissions to a year of practice, because the rules on duration have changed over the decades. It does not describe the other clocks a promise meets, such as training police officers or the length of schooling, for lack of having read their texts.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="The clock of a promise" avis="non" >}}
This page measures one clock: the time it takes to train a doctor. The book follows a promise on access to care from its campaign statement to the point where its outcome escapes the elected official, and meets other clocks along the way: a cohort of pupils, a carbon budget, the time of a law and its decrees. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Texts in force**, read on Légifrance (API) and in DILA's Journal officiel data (in French): order of 8 April 2013 on the regime of studies for the first and second cycles of medical studies, art. 1; Education Code, art. L632-2; Law no. 2022-1616 of 23 December 2022, art. 37; Public Health Code, art. R6153-1-2; Constitution, art. 6, quoted in the English translation published by the Conseil constitutionnel.

**DREES**, *Quelle démographie récente et à venir pour les professions médicales et pharmaceutique ?* [What recent and future demography for the medical and pharmaceutical professions?], Les Dossiers de la DREES no. 76, March 2021, chart 8 (source ONDPS); demography of health professionals, RPPS, published 2 July 2026 (in French).

**ONDPS**, report on the training of health professionals 2021-2025, note of 19 December 2025 (in French).

The figures, quotations, checks and charts are produced by a single script; no figure and no duration on this page is entered by hand. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_delais.csv), long format; [JSON](/promesses_delais.json), with definitions and the record of the checks (field names and some labels in French).

{{< reutiliser figures="figures_delais" jeu="promesses_delais" sources="Légifrance, Conseil constitutionnel, DREES and ONDPS" donnees="The lengths of the general practice curriculum and of the term read in the texts, the places filled from 1972 to 2020, the admissions from 2021 to 2025 and the practising doctors who qualified abroad; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
Under the rules in force, training a general practitioner in France takes at least {{< del-val "duree" >}} years from the first year of studies, {{< del-val "nfois" >}} the length of a presidential term; comparison of scale only. Students provide care before the end of the curriculum, under supervised autonomy, and {{< del-val "etr_p26" >}}% of practising doctors qualified abroad. Places in medical studies were divided by {{< del-val "rapport_baisse" >}} between 1972 and {{< del-val "an_min" >}}, before rising again; {{< del-val "admis_2021_2025" >}} students were admitted from 2021 to 2025.
{{< /reutiliser >}}
