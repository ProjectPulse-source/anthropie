---
title: "Can a campaign promise produce results within five years?"
url: /en/can-a-campaign-promise-produce-results-within-five-years/
description: "How long does it take to train a general practitioner in France, who decides how many students are admitted, and what changes before the diploma? The length of the curriculum written in the texts, compared with the presidential term; students admitted to the second year of the French medical curriculum since 1972. Open data."
chapo: "The test case of training general practitioners in France. A decision that raises the number of medical students does not reach its final result within the term that takes it. A general practitioner is trained in at least {del.duree} years from the first year, {del.nfois} the length of a presidential term (rules applying since the {del.an_reforme} academic year). Such a decision can still act sooner, because residents provide care under supervision during their training. And the number of students admitted does not depend on a single signature: the State sets a target, and each university votes its places."
date: 2026-10-06
lastmod: 2026-10-12
# English version of tab 4 of the "Presidential promises" dossier (FR: content/une-promesse-peut-elle-produire-ses-effets-en-cinq-ans/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_delais.json
# (scripts/update_promesses_delais.py), whose guards cover both languages. The Constitution is quoted in the English
# translation published by the Conseil constitutionnel; other French texts in French, followed by our translation.
donnees: [promesses_delais]
og_title: "Can a campaign promise produce results within five years? The test case of training doctors in France — S. Lalut"
og_image: "images/og-delais-promesse-en.jpg"
og_image_alt: "Share card: \"At least 10 years to train a GP in France. Twice a presidential term, under the 2023 rules.\" Two bars on the same scale: the general practice curriculum, residency included, and a presidential term; comparison of scale only."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_delais"
  nom: "Length of the general practice curriculum and students admitted to the second year of medical studies in France, 1972-2025"
  description: "Minimum durations of the general practice curriculum read in the texts in force (order of 8 April 2013, art. 1; Education Code, art. L632-2; Law no. 2022-1616, art. 37) and length of the presidential term (Constitution, art. 6); students admitted to the second year of the first cycle of medical studies (the third through an alternative-entry route): places filled under the numerus clausus from 1972 to 2020 (DREES, Dossier no. 76, source ONDPS) and admissions from 2021 to 2025 (ONDPS); share of practising doctors who qualified abroad in 2012 and 2026 (DREES, RPPS)."
  couverture_temporelle: "1972/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Places filled, then students admitted, in the second year of the first cycle of medical studies", unite: "students per year"}
    - {nom: "Minimum durations of the curriculum and of the term", unite: "semesters or years"}
    - {nom: "Practising doctors who qualified abroad", unite: "doctors on 1 January"}
  sources:
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046812307"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051820015"
    - "https://drees.solidarites-sante.gouv.fr/sites/default/files/2021-03/DD76_0.pdf"
  mots: ["doctors", "medical studies", "numerus clausus", "general practice", "presidential term", "France", "political promises"]
  fichiers: ["promesses_delais.csv", "promesses_delais.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "How long does it take to train a general practitioner in France?"
    answer: "Under the rules applying to students who enter residency (the third cycle) from the {del.an_reforme} academic year, at least {del.duree} years from the first year: {del.cycle1} semesters of first cycle, {del.cycle2} semesters of second cycle (order of 8 April 2013), then a general practice residency of {del.mg} years (Education Code, art. L632-2). From admission to the second year, at least {del.duree_adm} years remain. These are minimum durations, without repeating a year, interruption or alternative-entry route; residents provide care during these years, under supervision."
  - question: "Who decides how many students study medicine in France?"
    answer: "Since {del.d631_2020}, three tiers (Education Code, art. L631-1): the State sets national multi-year targets for the number of professionals to be trained; each university sets its targets for admission to the second cycle, on the binding opinion of the regional health agency and, since {del.d631_2025}, of the territorial health councils; each university also sets, every year, its intake capacities in the second and third years of the first cycle. Before that, the ministers for health and higher education set this number themselves every year: this was the numerus clausus."
  - question: "How many students are admitted into the French medical curriculum?"
    answer: "{del.admis_2025} in 2025, admitted to the second year of the first cycle (or the third, through an alternative-entry route) for {del.capacites_2025} places of intake capacity, according to the ONDPS; {del.admis_2021_2025} from 2021 to 2025. The first year of study is not counted. Places filled under the numerus clausus had been divided by {del.rapport_baisse} between 1972 ({del.places_1972}) and {del.an_min} ({del.places_min}), before rising again; the scope widened in 2010-2011 to alternative-entry routes (passerelles) and reorientation entries (droit au remords), and the numerus clausus ended after the 2020 intake."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 40
  refonte: "2026-10-12"
  nature: "Texts in force and DREES and ONDPS series, checked; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "Can a campaign promise produce results within five years?"
  court: "Time"
  role: "clocks and capacities"
---

{{< reutiliser-ancre >}}

Suppose a decision is taken today to train more doctors. When will patients see the effects? French general practice allows a precise answer, because every step is written down. Three clocks can be read there. The clock of the texts sets the length of the curriculum; the clock of capacity, how many students follow it; the clock of the effect says when patients see the difference, and no series here measures it. The Constitution is quoted in the English translation published by the Conseil constitutionnel; other French texts in French, followed by our translation.

## How long does it take to train a general practitioner? {#duree-du-cursus}

The curriculum has three cycles: {{< del-val "cycle1" >}} semesters of first cycle, {{< del-val "cycle2" >}} of second cycle, then residency. In general practice, residency lasts {{< del-val "mg" >}} years for students who started it from the {{< del-val "an_reforme" >}} academic year; this fourth year was created by a law of {{< del-val "loi_date" >}}. The presidential term lasts {{< del-val "mandat" >}} years.

{{< figure-svg fichier="delais-cursus-en" alt="Two bars on the same scale, in years. Above, the general practice curriculum: first cycle, second cycle, then a single block of general practice residency whose last year, darker, is spent under supervised autonomy; a bracket marks the duration counted from admission to the second year. Below, a presidential term, on the same scale. The values are in the text that follows." >}}Minimum durations written in the texts in force, without repeating a year, interruption or alternative-entry route. Comparison of scale only: it measures neither the effect of a policy nor the date on which its first effects can appear.{{< /figure-svg >}}

{{< fig-actions id="cursus" >}}

<div class="resultat-phrase">

**The finding in one sentence.** Under the rules applying since the {{< del-val "an_reforme" >}} academic year, the standard training pathway to become a general practitioner in France takes at least {{< del-val "duree" >}} years from the first year, {{< del-val "nfois" >}} the length of a presidential term.

</div>

**This length is that of a diploma, not the delay of an effect.** From admission to the second year, where the admission series on this page start, at least {{< del-val "duree_adm" >}} years remain. For the national observatory of the demography of the health professions (ONDPS), the targets set in 2021 likewise concern «&nbsp;{{< del-val "cit_ondps_9_11" >}}&nbsp;» [our translation: "{{< del-val "cit_ondps_9_11_tr" >}}"]. And residents provide care well before the end of the curriculum.

<details class="repli"><summary>The texts that set these durations, quoted word for word</summary>

- **First cycle** (order of 8 April 2013, art. 1): «&nbsp;{{< del-val "cit_cycle1" >}}&nbsp;» [our translation: "{{< del-val "cit_cycle1_tr" >}}"].
- **Second cycle** (same article): «&nbsp;{{< del-val "cit_cycle2" >}}&nbsp;» [our translation: "{{< del-val "cit_cycle2_tr" >}}"].
- **General practice residency** (Education Code, art. L632-2): a third cycle «&nbsp;{{< del-val "cit_mg" >}}&nbsp;» [our translation: "{{< del-val "cit_mg_tr" >}}"].
- **Application** (Law no. 2022-1616 of 23 December 2022 on the financing of social security for 2023, art. 37, II): «&nbsp;{{< del-val "cit_37" >}}&nbsp;» [our translation: "{{< del-val "cit_37_tr" >}}"]
- **Term** (Constitution, art. 6, English translation published by the Conseil constitutionnel): "{{< del-val "cit_art6a_en" >}}"

</details>

## Who decides how many students are admitted? {#qui-decide}

No single signature sets this number. The Education Code (art. L631-1) divides the decision between three tiers, each acting on a different count and at a different pace.

- **The State** sets national multi-year targets: a number of professionals to be trained, for five years (2021-2025, then 2026-2030).
- **Each university** sets its multi-year admission targets: a number of students to admit to the first year of the second cycle. It does so on the binding opinion of the regional health agency and, since {{< del-val "d631_2025" >}}, of the territorial health councils.
- **Each university**, again, votes its intake capacities every year: places in the second and third years of the first cycle.

**Three numbers, three objects.** The State's national target counts professionals to be trained; the intake capacity voted by the university counts places; admissions, recorded by the ONDPS, count the students who took those places. None of them counts qualified doctors, let alone consultations.

This division dates from {{< del-val "d631_2020" >}}. Before that, the ministers for health and higher education themselves set, every year, the number of students allowed to continue after the first year: this was the numerus clausus.

<details class="repli"><summary>Article L631-1 in its own words, and its versions since 2004</summary>

The text in force gives places to the universities: «&nbsp;{{< del-val "cit_631_cap" >}}&nbsp;» [our translation: "{{< del-val "cit_631_cap_tr" >}}"] The State's targets frame those of the universities: «&nbsp;{{< del-val "cit_631_onp" >}}&nbsp;» [our translation: "{{< del-val "cit_631_onp_tr" >}}"]. Candidates sit examinations for these places.

The numerus clausus appeared in the versions of L631-1 in force from 2004 to 2020. The version that entered into force on {{< del-val "d631_2020" >}} ({{< del-val "loi631_2020" >}}) gives capacities to the universities, within the State's targets; common usage calls this regime "numerus apertus", a term the law does not use. Since {{< del-val "d631_2023" >}} ({{< del-val "loi631_2023" >}}), the universities' targets are those «&nbsp;{{< del-val "cit_631_2023" >}}&nbsp;» [our translation: "{{< del-val "cit_631_2023_tr" >}}"], whereas the 2020 version listed both without order. Since {{< del-val "d631_2025" >}} ({{< del-val "loi631_2025" >}}), the binding opinion of the territorial health councils is added to that of the regional health agency.

- **From 2004 to 2010**: «&nbsp;{{< del-val "cit_631_2004" >}}&nbsp;» [our translation: "{{< del-val "cit_631_2004_tr" >}}"], by the two ministers.
- **From 2010 to 2020**: «&nbsp;{{< del-val "cit_631_2010" >}}&nbsp;» [our translation: "{{< del-val "cit_631_2010_tr" >}}"], among other things «&nbsp;{{< del-val "cit_631_2010b" >}}&nbsp;» [our translation: "{{< del-val "cit_631_2010b_tr" >}}"].
- **From {{< del-val "d631_2020" >}} to {{< del-val "d631_2023" >}}**: «&nbsp;{{< del-val "cit_631_2020" >}}&nbsp;» [our translation: "{{< del-val "cit_631_2020_tr" >}}"]
- **Since {{< del-val "d631_2025" >}}**: «&nbsp;{{< del-val "cit_631_obj" >}}&nbsp;» [our translation: "{{< del-val "cit_631_obj_tr" >}}"]

</details>

What this division has produced, the ONDPS measures. For 2021-2025, the national target set by the State was {{< del-val "onp" >}} doctors to be trained (order of 13 September 2021, according to the ONDPS). Universities admitted {{< del-val "admis_2021_2025" >}} students over these five years, to the second year of the first cycle or, through an alternative-entry route, to the third. In 2025, they admitted {{< del-val "admis_2025" >}} for {{< del-val "capacites_2025" >}} places of intake capacity. The ONDPS concludes: «&nbsp;{{< del-val "cit_ondps_sat" >}}&nbsp;» [our translation: "{{< del-val "cit_ondps_sat_tr" >}}"] And: «&nbsp;{{< del-val "cit_ondps_2026" >}}&nbsp;» [our translation: "{{< del-val "cit_ondps_2026_tr" >}}"] The targets for 2026-2030 are being prepared: on 3 July 2025, the ministers launched the «&nbsp;{{< del-val "cit_ondps_2630" >}}&nbsp;» [our translation: "{{< del-val "cit_ondps_2630_tr" >}}"] (ONDPS).

**An electoral promise therefore bears first on the national target**, which the ministers set by order. Places, for their part, are voted university by university, and admissions already fill them.

**Can the State impose more places?** It sets the target, not the places. Since {{< del-val "d631_2025" >}}, if the regional health agency and the territorial health councils consider that a university's capacities do not match the targets it set itself, «&nbsp;{{< del-val "cit_631_hausse" >}}&nbsp;» [our translation: "{{< del-val "cit_631_hausse_tr" >}}"]: the law says "may", not "must". It leaves to a decree the terms of such an increase, «&nbsp;{{< del-val "cit_631_moyens" >}}&nbsp;» [our translation: "{{< del-val "cit_631_moyens_tr" >}}"].

**Where does the saturation come from?** The ONDPS does not say, and this page does not know whether it lies in training placements, in supervising staff or in university budgets.

## How many students are admitted into the medical curriculum? {#admissions}

**Being admitted into the medical curriculum, in the sense of every series on this page, means obtaining a place in the second year of the first cycle, after a first year of study, or in the third year through an alternative-entry route.** The ONDPS does not say how many of those admitted come through the second door. The first year is not counted.

{{< figure-svg fichier="delais-admissions-en" alt="Annual bars of students admitted to the second year of the French medical curriculum, from 1972 to 2025: a fall to a minimum in the early 1990s, then a rise; two dotted lines mark the widening of scope in 2010-2011 and the end of the numerus clausus in 2021. The values are in the text that follows." >}}Places filled under the numerus clausus from 1972 to 2020 (DREES, source ONDPS), then students admitted from 2021 to 2025 (ONDPS), to the second year of the first cycle (the third for some alternative-entry routes), each at the year published by the source. No value is shifted to an assumed year of practice.{{< /figure-svg >}}

{{< fig-actions id="admissions" >}}

**Do not mechanically shift these bars to infer a year of practice**: the rules on duration have changed, students provide care before the end of the curriculum, and this series does not follow students individually until they practise.

Places filled under the numerus clausus fell by a factor of {{< del-val "rapport_baisse" >}} between 1972 and {{< del-val "an_min" >}}, then rose again. There were {{< del-val "places_1972" >}} places filled in 1972, {{< del-val "places_min" >}} in {{< del-val "an_min" >}}. According to the ONDPS, admissions in 2021-2025 exceed by {{< del-val "hausse_quinquennale" >}}% the total numerus clausus of 2016-2020, alternative-entry routes included.

Two breaks can be seen in the figure. From 2011 (partly from 2010), the DREES series adds to the main numerus clausus the alternative-entry routes (passerelles) and reorientation entries (droit au remords). In 2021, the numerus clausus disappears and the numbers come from the ONDPS, which records admissions with the universities: this step is not a jump in one and the same measure.

## Do students provide care before the end of the curriculum? {#avant-la-fin}

Yes, from residency onwards, and the texts organise it: residents do their placements in hospital and in ambulatory care, «&nbsp;{{< del-val "cit_instr_sup" >}}&nbsp;» [our translation: "{{< del-val "cit_instr_sup_tr" >}}"] (interministerial instruction of 21 May 2026).

The last year of general practice goes further. «&nbsp;{{< del-val "cit_supervision" >}}&nbsp;» [our translation: "{{< del-val "cit_supervision_tr" >}}"], in ambulatory practice alongside general practitioners, and as a priority in areas where the supply of care is insufficient or access to care difficult (Education Code, art. L632-2); a hospital placement is possible in that year only exceptionally.

During this last year, the general practice resident works as a *docteur junior*, a doctor in the final supervised phase of training. «&nbsp;{{< del-val "cit_dj1" >}}&nbsp;» [our translation: "{{< del-val "cit_dj1_tr" >}}"] A practitioner can be called on at any time, and the act remains under that practitioner's responsibility: alone for the act, then, but never without recourse. The texts organise this care; they do not measure its share of all care.

<details class="repli"><summary>The texts on residency and the docteur junior, quoted word for word</summary>

- **Residency** (instruction of 21 May 2026): «&nbsp;{{< del-val "cit_instr_interne" >}}&nbsp;» [our translation: "{{< del-val "cit_instr_interne_tr" >}}"]
- **The last year** (Education Code, art. L632-2): «&nbsp;{{< del-val "cit_supervision" >}}&nbsp;», by approved practitioners, «&nbsp;{{< del-val "cit_ambu" >}}&nbsp;» [our translation: "{{< del-val "cit_ambu_tr" >}}"]. The exception: «&nbsp;{{< del-val "cit_derog" >}}&nbsp;» [our translation: "{{< del-val "cit_derog_tr" >}}"]
- **The areas** (Public Health Code, art. L1434-4): «&nbsp;{{< del-val "cit_zones" >}}&nbsp;» [our translation: "{{< del-val "cit_zones_tr" >}}"]
- **The docteur junior** (Public Health Code, art. R6153-1-2): «&nbsp;{{< del-val "cit_dj1" >}}&nbsp;» «&nbsp;{{< del-val "cit_dj3" >}}&nbsp;» [our translation: "{{< del-val "cit_dj3_tr" >}}"] «&nbsp;{{< del-val "cit_dj2" >}}&nbsp;» [our translation: "{{< del-val "cit_dj2_tr" >}}"]

</details>

## How long does a reform of the curriculum take to apply? {#epreuve-des-dates}

The fourth year of general practice makes it possible to check this with exact dates, without projection.

- **{{< del-val "loi_date" >}}**: the law on the financing of social security for 2023 creates this year (art. 37), for students who enter residency at the start of the {{< del-val "an_reforme" >}} academic year.
- **{{< del-val "debut_conso" >}}**: the date planned by the instruction of 21 May 2026 for these residents to enter their fourth year, as *docteurs juniors*, «&nbsp;{{< del-val "cit_instr_amb" >}}&nbsp;» [our translation: "{{< del-val "cit_instr_amb_tr" >}}"].
- **In {{< del-val "fin_min" >}} at the earliest**: end of that year, since «&nbsp;{{< del-val "cit_instr_diplome" >}}&nbsp;» [our translation: "{{< del-val "cit_instr_diplome_tr" >}}"]

**The first planned effect of the law comes {{< del-val "moins_quatre" >}} after it; its final result, general practitioners trained in {{< del-val "mg" >}} years of residency, {{< del-val "pres_cinq" >}} after it, at the earliest.** In between, if the planned timetable holds, a cohort of residents provides care in general practices, as a priority where the supply of care is lacking. A decision can therefore produce effects during a term of office without reaching its final result within it, although this reform lengthens the curriculum by only one year. On 12 October 2026, the first of these years has not begun: the timetable is that of an implementing text, not an observed fact.

## When will patients see the difference? {#limites}

No series on this page answers that. The statistical service of the French health ministry (DREES) wrote in 2021 that «&nbsp;{{< del-val "cit_dd76_objet" >}}&nbsp;»: «&nbsp;{{< del-val "cit_dd76" >}}&nbsp;» [our translation: "{{< del-val "cit_dd76_objet_tr" >}}: {{< del-val "cit_dd76_tr" >}}"] (*Les Dossiers de la DREES* No. 76). Its object is the number of doctors, the "demographic situation", not care: this delay and the care given by residents do not contradict each other, they concern two different objects.

The number of practising doctors also depends on departures, choices of specialty, places of practice and doctors who qualified abroad, a stock present at a given date and not a flow of arrivals: on 1 January 2026, according to the DREES, {{< del-val "etr_p26" >}}% of practising doctors had obtained their diploma abroad, against {{< del-val "etr_p12" >}}% in 2012. That is {{< del-val "etr_26" >}} doctors out of {{< del-val "tot_26" >}}. The place of the diploma does not indicate nationality, and this comparison does not measure any compensation of French training capacity.

This page does not describe the other clocks a promise meets, such as training police officers or the length of schooling, for lack of having read their texts. One case shows that a clock can outlast the term of office; it does not say how many do.

## How should a promise that depends on training be judged? {#juger-une-promesse}

Three questions separate what such a promise can change during the term from what it can only set in motion.

1. **The clock of the texts**: what length of training does the law impose, and since when? Here, at least {{< del-val "duree" >}} years from the first year (rules applying since the {{< del-val "an_reforme" >}} academic year).
2. **The clock of capacity**: who decides the number of places, and are they already filled? Here, each university, every year, within a State target; according to the ONDPS, they are almost saturated.
3. **The clock of the effect**: what acts before the diploma, and what can only be measured afterwards? Here, residents provide care under supervision during their training; access to care depends on factors that none of these series measures.

The same grid applies to any promise whose result depends on people to be trained, provided the texts of each profession are read.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="The clock of a promise" avis="non" >}}
This page measures one clock: the time it takes to train a doctor. The book follows a promise on access to care from its campaign statement to the point where its outcome escapes the elected official, and meets other clocks along the way: a cohort of pupils, a carbon budget, the time of a law and its decrees. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Texts**, read on Légifrance (API) and in DILA's Journal officiel data (in French): order of 8 April 2013 on the regime of studies for the first and second cycles of medical studies, art. 1; Education Code, art. L631-1 (version in force and versions that entered into force in 2004, 2010, 2020 and 2023) and L632-2; Law no. 2022-1616 of 23 December 2022 on the financing of social security for 2023, art. 37; Public Health Code, art. R6153-1-2 and L1434-4; Constitution, art. 6, quoted in the English translation published by the Conseil constitutionnel. Interministerial instruction no. DGOS/RH2/DGESIP/2026/44 of 21 May 2026 on the implementation of the fourth year of the diploma of specialised studies in general practice (*Bulletin officiel* of the health ministry), an implementing text without binding force (in French).

**DREES**, *Quelle démographie récente et à venir pour les professions médicales et pharmaceutique ?* [What recent and future demography for the medical and pharmaceutical professions?], Les Dossiers de la DREES no. 76, March 2021, chart 8 (source ONDPS); demography of health professionals, RPPS, published 2 July 2026 (in French).

**ONDPS**, review of the national multi-year targets 2021-2025 for the training of doctors, midwives, dentists and pharmacists, note of 19 December 2025 (in French).

**Download the data** (CC BY 4.0 licence): [CSV](/promesses_delais.csv), long format; [JSON](/promesses_delais.json), with definitions and the record of the checks (field names and some labels in French). This dataset is also archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier for citation: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664); the archived version predates the revision of 12 October 2026.

<details class="repli"><summary>How these figures were checked, and the gap that remains</summary>

The figures, quotations, checks and charts are produced by a single script. Durations and quotations are read in the archived texts, the DREES series in its file, and the dates of the fourth-year timetable in the law and in the instruction. The admissions from 2021 to 2025 and the five-year totals, published as an image by the ONDPS, are transcribed: the script checks the sum of the annual admissions against the printed total (an error in one year offset by another would go unnoticed), finds that total, the 2025 admissions and capacity and the national target in the text of the document, compares the totals from 2001 to 2015 with the DREES series, and checks that the 2016-2020 total, read twice on the image, gives back the increase and the annual average that the text prints. It stops if a piece of data no longer meets the conditions on which the main sentences depend.

**The level of admission of those admitted in 2021-2025.** The law provides that candidates «&nbsp;{{< del-val "cit_631_pass" >}}&nbsp;» [our translation: "{{< del-val "cit_631_pass_tr" >}}"] (Education Code, art. L631-1). The ONDPS counts intake capacities as places offered «&nbsp;{{< del-val "cit_ondps_cae1" >}}&nbsp;» [our translation: "{{< del-val "cit_ondps_cae1_tr" >}}"] and specifies that «&nbsp;{{< del-val "cit_ondps_onp_pass" >}}&nbsp;» [our translation: "{{< del-val "cit_ondps_onp_pass_tr" >}}"]. It compares those admitted with the total numerus clausus of 2016-2020, which includes alternative-entry routes. It does not publish the share of those admitted to the third year.

**The {{< del-val "hausse_quinquennale" >}}% increase.** According to the ONDPS, {{< del-val "admis_2021_2025" >}} students were admitted to the second year or, through an alternative-entry route, to the third, from 2021 to 2025. The total numerus clausus of 2016-2020, alternative-entry routes included, was {{< del-val "admis_2016_2020" >}} places. The ONDPS thus compares students admitted with places, treating the numerus clausus as a number of admissions, an assumption it considers sound for medicine.

**The gap between the two sources.** The DREES series matches exactly the five-year totals published by the ONDPS for 2001-2005, 2006-2010 and 2011-2015. For 2016-2020, the sum of the DREES values exceeds the ONDPS total by {{< del-val "ecart_2016_2020" >}} places, about {{< del-val "ecart_pct" >}}% of that total. That total, read twice on the image, is the only one of the two that gives back the {{< del-val "hausse_quinquennale" >}}% increase printed by the ONDPS (the DREES sum would give {{< del-val "hausse_drees" >}}%): the gap is not a reading error. The DREES value for 2020 carries an asterisk whose legend was not found. The gap is published, not corrected.

</details>

{{< reutiliser figures="figures_delais" jeu="promesses_delais" sources="Légifrance, Conseil constitutionnel, Bulletin officiel, DREES and ONDPS" donnees="The lengths of the general practice curriculum and of the term read in the texts, the places filled under the numerus clausus from 1972 to 2020, the students admitted to the second year (or the third, through an alternative-entry route) from 2021 to 2025 and the practising doctors who qualified abroad; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
Under the rules applying to students who entered residency from the {{< del-val "an_reforme" >}} academic year, training a general practitioner in France takes at least {{< del-val "duree" >}} years from the first year, {{< del-val "nfois" >}} the length of a presidential term; comparison of scale only. The number of students admitted to the second year is decided on three tiers: the State's target, then the targets and capacities voted by each university. Places filled fell by a factor of {{< del-val "rapport_baisse" >}} between 1972 and {{< del-val "an_min" >}}, before rising again; {{< del-val "admis_2021_2025" >}} students were admitted to the second year (or the third, through an alternative-entry route) from 2021 to 2025.
{{< /reutiliser >}}
