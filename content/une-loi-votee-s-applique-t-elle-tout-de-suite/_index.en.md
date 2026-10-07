---
title: "Does a French law apply as soon as it is passed?"
url: /en/does-a-law-apply-as-soon-as-it-is-passed/
description: "A law promulgated in France often waits for decrees and ministerial orders. How many implementing measures the laws passed since 2017 are still waiting for, how many laws call for none, and why the French Senate and Government publish different implementation rates. Open data."
chapo: "Not by the vote alone. Once the law has been promulgated and published, some of its provisions still wait for the measures needed to implement them. On {app.releve}, the barometer of the application of laws classifies {app.A} of the {app.nmes} measures listed for the laws promulgated from October 2017 to September 2025 as still pending. And the \"implementation rate\" itself depends on counting conventions: for two sessions documented here, the Senate publishes its rate and reports a different one calculated by the General Secretariat of the Government."
date: 2026-10-06
lastmod: 2026-10-06
# English version of tab 3 of the "Presidential promises" dossier (FR: content/une-loi-votee-s-applique-t-elle-tout-de-suite/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_appliquer.json
# (scripts/update_promesses_appliquer.py), whose guards cover both languages. The Constitution is quoted in the English
# translation published by the Conseil constitutionnel; other French texts in French, followed by our translation (every
# number in a translation must appear in the original: guard A7 bis).
donnees: [promesses_appliquer]
og_title: "Does a French law apply as soon as it is passed? Implementing measures still pending — S. Lalut"
og_image: "images/og-appliquer-promesse-en.jpg"
og_image_alt: "Share card: the number of implementing measures still pending for the laws passed in France from October 2017 to September 2025, with bars by session of the law: measures with a published instrument, pending, classified as “not applicable”, at the date of the barometer reading."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_appliquer"
  nom: "Implementing measures of the laws promulgated in France from 2017 to 2025, directly applicable laws, and rates published by the French Senate"
  description: "Status of the implementing measures of the laws promulgated in France from 1 October 2017 to 30 September 2025, excluding treaties, on 5 October 2026 (barometer of the application of laws, National Assembly and LexImpact, DILA data); directly applicable laws by session according to the barometer and to the Senate, matched law by law; implementation rates published by the Senate from 2002-2003 to 2024-2025, by segment of definition."
  couverture_temporelle: "2002/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Implementing measures by status", unite: "measures"}
    - {nom: "Laws promulgated and directly applicable laws", unite: "laws"}
    - {nom: "Implementation rate published by the Senate", unite: "%"}
  sources:
    - "https://barometre.assemblee-nationale.fr/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
  mots: ["application of laws", "implementing decrees", "regulations", "French Senate", "General Secretariat of the Government", "France", "political promises"]
  fichiers: ["promesses_appliquer.csv", "promesses_appliquer.json"]
faq:
  - question: "Does a French law apply as soon as it is published in the Journal officiel?"
    answer: "Not by the vote alone: \"{app.cit_art10}\" (Constitution, art. 10, English translation published by the Conseil constitutionnel). Once published, it enters into force on the date it sets or, failing that, the day after its publication. But under article 1 of the Civil Code, provisions whose implementation requires implementing measures wait for them (our translation). A law can therefore be in force in part and wait for its decrees and orders in another part."
  - question: "How many implementing measures are still pending?"
    answer: "On {app.releve}, the barometer of the application of laws lists {app.nmes} measures for the laws promulgated from October 2017 to September 2025, excluding treaties: {app.P} have an identified published instrument, {app.A} are pending, {app.S} are classified as “not applicable” (sans objet) and {app.U} have an incomplete status. For the laws of 2017-2018, {app.A_1718} measures out of {app.N_1718} are still pending. This is neither a historical rate nor a measure of efficiency."
  - question: "What is the implementation rate of laws in France?"
    answer: "It depends on counting conventions. For the 2018-2019 session, the Senate publishes {app.senat_1819} and reports that the General Secretariat of the Government arrives at {app.sgg_1819}: according to the Senate, it counts ministerial orders and measures whose entry into force is deferred, the Government does not. The two levels are not directly comparable without harmonising these conventions."
  - question: "Is one law in two left unapplied?"
    answer: "The phrase depends on what is counted. A fully applied law, a published implementing measure, a status recorded on a given date: these are not the same objects. The Senate counts orders and measures whose entry into force is deferred, the General Secretariat of the Government does not; the National Assembly's barometer gives a status on a date, not a rate. Before repeating \"one law in two\", one must know which convention the phrase uses, on what date and for which laws."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 30
  nature: "Barometer of the application of laws, Senate reports and Government report, matched law by law; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "Does a French law apply as soon as it is passed?"
  court: "Implement"
  role: "decrees and implementing measures"
---

{{< reutiliser-ancre >}}

A promise that goes through the law does not stop at the vote. Some provisions wait for the measures needed to implement them, notably decrees or ministerial orders (arrêtés). This page counts these measures for the laws promulgated in France since 2017 (by parliamentary session, from 1 October to 30 September), shows how many laws call for none, and explains why the published implementation rates do not all say the same thing. All the figures come from public sources, matched law by law, and none is entered by hand. The Constitution is quoted in the English translation published by the Conseil constitutionnel; other French texts in French, followed by our translation.

**Short answer.** Not by the vote alone. Once promulgated and published, a law enters into force on the date it sets or the day after its publication; but those of its provisions that call for implementing measures wait for these measures. On {{< app-val "releve" >}}, {{< app-val "A" >}} of the {{< app-val "nmes" >}} measures listed for the laws of 2017 to 2025 are still pending.

Between the vote and entry into force, the Constitution places promulgation: "{{< app-val "cit_art10" >}}" (art. 10). If the matter is referred to the Constitutional Council, "{{< app-val "cit_art61" >}}" (art. 61). Once the law is published in the Journal officiel, the Civil Code sets the rule: «&nbsp;{{< app-val "cit_cciv" >}}&nbsp;» [our translation: "{{< app-val "cit_cciv_tr" >}}"] (art. 1).

## How many implementing measures are still pending? {#mesures-en-attente}

{{< figure-svg fichier="appliquer-mesures-en" alt="Horizontal bars, one per session of the law, from 2017-2018 to 2024-2025: measures with an identified published instrument, pending, classified as “not applicable”. A pending share remains in every session, including the oldest. The values are in the table below the figure." >}}Implementing measures listed by the barometer of the application of laws for the laws promulgated in each session, excluding treaties, and their status on {{< app-val "releve" >}}. It is a status at a date: neither a historical rate nor a measure of efficiency.{{< /figure-svg >}}

{{< fig-actions id="mesures" >}}

{{< app-tableau "mesures" "The figure's values in a table" >}}

<div class="resultat-phrase">

**The finding in one sentence.** On {{< app-val "releve" >}}, of the {{< app-val "nmes" >}} implementing measures listed for the laws promulgated in France from October 2017 to September 2025, {{< app-val "P" >}} have an identified published instrument, {{< app-val "A" >}} are pending and {{< app-val "S" >}} are classified as “not applicable” (sans objet).

</div>

On {{< app-val "releve" >}}, {{< app-val "A_1718" >}} of the {{< app-val "N_1718" >}} measures listed for the laws of the 2017-2018 session remain classified as "pending" by the barometer; for those of 2024-2025, {{< app-val "A_2425" >}} out of {{< app-val "N_2425" >}}. This status is not enough, on its own, to qualify a delay: {{< app-val "differ_A" >}} of the {{< app-val "A" >}} pending measures carry, in their subject or their observation, the word «&nbsp;différé&nbsp;» or «&nbsp;différée&nbsp;» (deferred), and the law itself may set a later date.

**A caveat about the classification.** {{< app-val "obs_acte" >}} of the measures classified as “not applicable” (sans objet) carry in their observation the reference of an order or a decree, {{< app-val "obs_acte_2425" >}} of them for the laws of 2024-2025. This finding does not allow them to be reclassified: “not applicable” is taken here as the producer's label. For one of them, law no. 2025-138 on the care of amyotrophic lateral sclerosis, the observation reads «&nbsp;{{< app-val "cas_2025_138" >}}&nbsp;» (an arrêté is a ministerial order), and the Government's report at 31 December 2025 counts its measure as pending. The label therefore does not prove that a measure was abandoned.

<details class="repli"><summary>What was checked, and how</summary>

The measures are those of the barometer of the application of laws, published by the National Assembly and LexImpact from DILA's implementation schedules, in its version of {{< app-val "releve" >}}. A measure counts as published if its status is "applied" and an instrument is identified; "applied" without an identified instrument gives an incomplete status. The script checks that each measure falls into one and only one category, session by session, and that the same producer's file of laws gives, law by law, the same number of measures applied and to be applied. A second program, written separately, recounted the same categories from the raw file: the numbers match.

The barometer only publishes the current status. DILA's open data on implementation schedules only go back to July 2025. No "six months after the law" rate can therefore be recalculated for earlier sessions, and the page publishes none.

</details>

## Can a law apply without any decree? {#lois-application-directe}

Yes. The two sources that classify the laws of each session, the barometer and the Senate in its annual reports, distinguish directly applicable laws, but they do not always give that status to the same texts. In the barometer, a law is classified as directly applicable when its schedule contains no measure other than “not applicable”; the Senate applies its own classification rules. Matched law by law over the {{< app-val "nlois" >}} laws promulgated from 2017-2018 to 2024-2025, excluding {{< app-val "conventions" >}} international treaties, they keep exactly the same scope, but classify {{< app-val "ndesacc" >}} laws differently.

{{< figure-svg fichier="appliquer-lois-en" alt="Horizontal bars, one per session: laws directly applicable for both sources, laws classified differently, laws that call for measures; a mark shows half of each session's laws. In 2018-2019, directly applicable and divergent laws together exceed half. The values are in the table below the figure." >}}Laws promulgated in each session, excluding treaties. In blue, laws directly applicable for both sources; in dark grey, those they classify differently; the black mark shows half of the session's laws.{{< /figure-svg >}}

{{< fig-actions id="lois" >}}

{{< app-tableau "lois" "The figure's values in a table" >}}

The proposition "fewer than half of the laws in every session" does not hold over the {{< app-val "nsessions" >}} sessions: in {{< app-val "ct_session" >}}, the barometer counts {{< app-val "ct_baro" >}} directly applicable laws out of {{< app-val "ct_N" >}}, more than half, while the Senate counts {{< app-val "ct_senat" >}}. In the {{< app-val "nautres" >}} other sessions, even the upper bound stays below half.

The 2024-2025 gap can be read within a single Senate report. Its summary says: «&nbsp;{{< app-val "cit_802_22" >}}&nbsp;» [our translation: "{{< app-val "cit_802_22_tr" >}}"]; another page states that «&nbsp;{{< app-val "cit_802_24" >}}&nbsp;» [our translation: "{{< app-val "cit_802_24_tr" >}}"]. The barometer counts {{< app-val "s25_baro" >}}. The gap between {{< app-val "s25_baro" >}} and {{< app-val "s25_senat" >}} is explained law by law by different classification rules; the one between {{< app-val "s25_senat" >}} and {{< app-val "s25_publie" >}} is not, for lack of a list of names.

<details class="repli"><summary>Why the two sources diverge on {{< app-val "ndesacc" >}} laws</summary>

The barometer classifies a law as "directly applicable" when its schedule contains no measure other than “not applicable”. The Senate classifies it in its annexes. Several rules explain part of the gaps: in some years, the Senate leaves out the measures that the law makes optional; the barometer classifies as "directly applicable" a law all of whose measures are now classified as “not applicable”; it classifies as "not directly applicable" a law with no schedule. Applied together, these rules remove some gaps and create others: they are not applied uniformly from one year to the next. All the laws in a gap are counted as uncertain, even when a rule explains them; hence the bounds in the table.

Defects in the Senate's annexes, such as a wrong law number or an announced count that does not match the list that follows, were corrected using the title and date of the law; the law-by-law register flags them.

</details>

## Why do the French Senate and Government publish different rates? {#taux-publies}

Because their counting conventions differ. For the 2017-2018 and 2018-2019 sessions, the Senate's reports publish its rate and report a different one calculated by the General Secretariat of the Government. For 2017-2018, the Senate writes: «&nbsp;{{< app-val "cit_senat_1718" >}}&nbsp;» [our translation: "{{< app-val "cit_senat_1718_tr" >}}"]. The General Secretariat of the Government, heard by the Senate, reports for its part that «&nbsp;{{< app-val "cit_sgg_1718" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg_1718_tr" >}}"]. For the 2018-2019 session, the Senate writes: «&nbsp;{{< app-val "cit_senat_1819" >}}&nbsp;» [our translation: "{{< app-val "cit_senat_1819_tr" >}}"], and adds that «&nbsp;{{< app-val "cit_sgg_1819" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg_1819_tr" >}}"].

The Senate itself gives the reasons for the gap: «&nbsp;{{< app-val "cit_diverge" >}}&nbsp;» [our translation: "{{< app-val "cit_diverge_tr" >}}"] First, «&nbsp;{{< app-val "cit_arretes" >}}&nbsp;» [our translation: "{{< app-val "cit_arretes_tr" >}}"] Second, «&nbsp;{{< app-val "cit_differees" >}}&nbsp;» [our translation: "{{< app-val "cit_differees_tr" >}}"] The Senate also mentions a third ground, which it itself calls political reasons: «&nbsp;{{< app-val "cit_politique" >}}&nbsp;» [our translation: "{{< app-val "cit_politique_tr" >}}"] A rate can thus include a judgement, and not only a count.

A implementation rate can therefore only be interpreted with its scope, its cut-off date and its counting rules. The Government's half-yearly report follows laws by legislature, not by session: at 31 December 2025, it follows, for the 16th legislature, the laws that «&nbsp;{{< app-val "cit_sgg16_def" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg16_def_tr" >}}"], and for the 17th, those that «&nbsp;{{< app-val "cit_sgg17_def" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg17_def_tr" >}}"] In the cases documented here, the Senate and the General Secretariat of the Government do not measure exactly the same object; their levels are therefore not directly comparable without harmonising these conventions.

## Has the implementation rate of laws risen since 2002? {#serie-senat}

The Senate's series does not allow us to say so from end to end. The corpus shows {{< app-val "nsegments" >}} successive definitions since 2002-2003, which differ in cut-off date, scope of laws and treatment of deferred and optional measures: the segments do not read as a single series.

{{< figure-svg fichier="appliquer-serie-en" alt="Points by session from 2002-2003 to 2024-2025, grouped in segments separated by changes of definition. The first segment, from 2002-2003 to 2008-2009, lies well below the following ones. The values, their document and their definition are in the table below the figure." >}}Implementation rates of laws published by the French Senate, as published. The segments correspond to different definitions: do not join them. The open circle marks the 2019-2020 figure, revised downwards in the following report.{{< /figure-svg >}}

{{< fig-actions id="serie" >}}

{{< app-tableau "serie" "The values, their document and their definition" >}}

The last point of the first segment and the first point kept from the next are separated by a change of definition, which the Senate describes as follows: «&nbsp;{{< app-val "cit_six_mois" >}}&nbsp;» [our translation: "{{< app-val "cit_six_mois_tr" >}}"] In 2024-2025, it publishes a single rate («&nbsp;{{< app-val "cit_802_66" >}}&nbsp;» [our translation: "{{< app-val "cit_802_66_tr" >}}"]), and specifies in a note: «&nbsp;{{< app-val "cit_802_note" >}}&nbsp;» [our translation: "{{< app-val "cit_802_note_tr" >}}"] Optional measures (mesures éventuelles) are those the law allows without requiring them. The 2009-2010 session is not shown in the figure, for lack of a cut-off date established in the sentence that gives its rate. A revised figure, like that of 2019-2020, and a change of definition are two distinct facts: the series keeps both.

## What this page does not say {#limites}

It does not say whether a law produces the effect the promise aimed at: a published decree is not a result achieved. It does not measure the quality of decrees, nor whether they reflect the legislature's intent, which the Senate assesses itself. It gives no average publication time, for lack of a dated history of the schedules. It does not compare the Senate's and the Government's rates with each other, nor two segments of the Senate's series.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="After the vote" avis="non" >}}
This page counts what a law still waits for after the vote. The book follows nine written, dated and signed promises along the chain that runs from the decision to its outcome: what a president decides within his own chain of power, what he has to get voted, what he has to negotiate, and what will never depend on him. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Barometer of the application of laws**, National Assembly and LexImpact, from DILA's implementation schedules: files of laws and of measures, version of {{< app-val "releve" >}}.

**French Senate**, annual reports on the application of laws from 2011 to 2026, summaries and press releases from 2003 to 2011 (in French); the document and page of each value and each quotation are given in the dataset.

**General Secretariat of the Government**, half-yearly report on the application of laws at 31 December 2025, read on Légifrance (in French).

**Constitution**, arts. 10 and 61, quoted in the English translation published by the Conseil constitutionnel; **Civil Code**, art. 1, read on Légifrance (API).

The figures, quotations, checks and charts are produced by a single script; each quotation is checked word for word in the page of the document it comes from, and no figure on this page is entered by hand. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_appliquer.csv), long format; [JSON](/promesses_appliquer.json), with definitions and the record of the checks (field names and some labels in French).

{{< reutiliser figures="figures_appliquer" jeu="promesses_appliquer" sources="National Assembly and LexImpact (DILA data), French Senate, General Secretariat of the Government, Légifrance" donnees="The status of implementing measures by session of the law, the laws directly applicable according to the two sources, and the rates published by the Senate since 2002-2003; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
On {{< app-val "releve" >}}, of the {{< app-val "nmes" >}} implementing measures listed for the laws promulgated in France from October 2017 to September 2025, {{< app-val "A" >}} are pending. For two sessions, the French Senate's reports publish its implementation rate and report a different rate calculated by the General Secretariat of the Government, under other counting conventions; the Senate's series rests on {{< app-val "nsegments" >}} successive definitions since 2002-2003.
{{< /reutiliser >}}
