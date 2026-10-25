---
title: "Does a French law apply as soon as it is passed?"
url: /en/does-a-law-apply-as-soon-as-it-is-passed/
description: "From the vote to the last measure: the steps between a law passed in France and its application, how many of the laws promulgated since 2017 still wait for a decree or an order, what the Conseil d'État requires of the Government, and why the French Senate and Government publish different implementation rates. Open data."
chapo: "Not by the vote alone. Once the law has been promulgated and published, those of its provisions whose implementation requires decrees or ministerial orders wait for these measures. On {app.releve}, according to the barometer of the application of laws, {app.L_att} of the {app.nlois} laws promulgated from October 2017 to September 2025, excluding treaties (laws authorising the ratification or approval of an international agreement, or accession to one), were still waiting for at least one measure; {app.L_tout} had received all of them and {app.L_dir} were classified as having no measure to take. A pending measure is not necessarily late, but the Government is not free to wait indefinitely: the Conseil d'État requires it to act within a reasonable time, and a refusal to adopt a measure that is due can be brought before the administrative courts, which can annul it and order the measure to be adopted."
date: 2026-10-06
lastmod: 2026-10-12
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
  nom: "Implementing measures of the laws promulgated in France from 2017 to 2025, status of the laws, directly applicable laws, and rates published by the French Senate and Government"
  description: "Status, law by law, of the laws promulgated in France from 1 October 2017 to 30 September 2025, excluding treaties, and status of their implementing measures on 5 October 2026 (barometer of the application of laws, National Assembly and LexImpact, DILA data); sorting of the “not applicable” observations by written rules; directly applicable laws by session according to the barometer and to the Senate, matched law by law; implementation rates published by the Senate from 2002-2003 to 2024-2025, by segment of definition, and by the General Secretariat of the Government at 31 December 2025."
  couverture_temporelle: "2002/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Laws by implementation status", unite: "laws"}
    - {nom: "Implementing measures by status", unite: "measures"}
    - {nom: "Laws promulgated and directly applicable laws", unite: "laws"}
    - {nom: "Implementation rates published by the Senate and by the Government", unite: "%"}
  sources:
    - "https://barometre.assemblee-nationale.fr/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
    - "https://www.legifrance.gouv.fr/contenu/menu/autour-de-la-loi/legislatif-et-reglementaire/application-des-lois/bilan-semestriel-au-31-decembre-2025"
  mots: ["application of laws", "implementing decrees", "regulations", "reasonable time", "Conseil d'État", "French Senate", "General Secretariat of the Government", "France", "political promises"]
  fichiers: ["promesses_appliquer.csv", "promesses_appliquer.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Does a French law apply as soon as it is published in the Journal officiel?"
    answer: "In principle, it enters into force on the date it sets or, failing that, the day after its publication; in case of urgency, on its publication if the promulgation decree so prescribes (Civil Code, art. 1). But provisions whose implementation requires implementing measures do not enter into force until those measures do (our translation). A law can therefore be in force in part and wait for its decrees or orders in another part."
  - question: "How many French laws are still waiting for an implementing measure?"
    answer: "On {app.releve}, according to the barometer of the application of laws, {app.L_att} of the {app.nlois} laws promulgated from October 2017 to September 2025, excluding treaties, still had at least one measure classified as pending; {app.L_tout} had received all their measures, {app.L_dir} were classified as having no measure to take and one had no schedule. Of the {app.nmes} measures listed for these laws, {app.A} were pending. A pending measure is not necessarily late."
  - question: "What is the implementation rate of laws in France?"
    answer: "It depends on counting conventions. At 31 December 2025, the General Secretariat of the Government publishes {app.sgg16_taux} for the laws of the 16th legislature, decrees only, and {app.sgg17_taux} for those of the 17th, decrees or orders; the Senate publishes {app.s2425} for the 2024-2025 session, at 31 March 2026. These rates cover neither the same laws, nor the same measures, nor the same date: they cannot be ranked."
  - question: "Is one law in two left unapplied?"
    answer: "On {app.releve}, according to the barometer, {app.L_att} of the {app.nlois} laws promulgated from October 2017 to September 2025, excluding treaties, still had at least one measure classified as pending. Measured against the {app.L_mes} laws whose schedule contained at least one measure to take, pending or taken, they make up {app.L_att_pct_mes}, about one in two: this is a ratio between two categories of the barometer at the reading date, not the share of pending laws among those that provided for a measure. This means neither that these laws were wholly inapplicable, nor that each of these measures was late. A phrase like \"one law in two\" may come from this second count, from a rate per measure, from a single session or from another date: before repeating it, one must know what it counts, on what date and for which laws."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocoles de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-12"
  bloc: "promesses"
  livres: ["un-president-peut-il-tenir-ses-promesses"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 30
  nature: "Barometer of the application of laws, Senate reports, Government report and Conseil d'État decisions, matched law by law; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "Does a French law apply as soon as it is passed?"
  court: "Implement"
  role: "decrees and implementing measures"
---

{{< reutiliser-ancre >}}

A promise that goes through the law does not stop at the vote. Between adoption and application, a French law goes through several steps, and some of its provisions then wait for decrees or ministerial orders (arrêtés). This page follows these steps, counts the laws and the measures still pending for the laws promulgated since 2017 (by session as the Senate counts it: laws published from 1 October to 30 September), sets out what the courts require of the Government, and explains why the published implementation rates do not all say the same thing. Counts of laws and measures are recalculated law by law from public sources; the rates published by the Senate and by the Government, transcribed from their reports, are reread by the script in the archived documents. The Constitution is quoted in the English translation published by the Conseil constitutionnel; other French texts in French, followed by our translation.

## From the vote to application: what steps does a law go through? {#du-vote-a-l-application}

Five steps separate a law that has been passed from its application, and each has its own actor.

1. **The vote.** Parliament gives the text its final adoption.
2. **Promulgation.** The President of the Republic promulgates the law within fifteen days of its final passage and transmission to the Government, and may, within that time, ask Parliament to reopen debate on it (Constitution, art. 10). The Constitutional Council steps in here: it must review Institutional Acts before their promulgation, other laws may be referred to it, and a referral suspends the time allotted for promulgation (art. 61).
3. **Publication and entry into force.** Once published in the Journal officiel, the law enters into force on the date it sets or, failing that, the day after its publication (Civil Code, art. 1, para. 1). The next paragraph adds: «&nbsp;{{< app-val "cit_cciv" >}}&nbsp;» [our translation: "{{< app-val "cit_cciv_tr" >}}"] A third opens a faster route: «&nbsp;{{< app-val "cit_cciv_urg" >}}&nbsp;» [our translation: "{{< app-val "cit_cciv_urg_tr" >}}"].
4. **Implementing measures.** The Prime Minister ensures the implementation of legislation and, subject to article 13, has power to make regulations (art. 21). The President of the Republic signs the decrees deliberated upon in the Council of Ministers (art. 13), and the instruments of the Prime Minister are countersigned, where required, by the ministers responsible for their implementation (art. 22). The law may also provide for ministerial orders, and a decree may itself refer matters to an order of a minister.
5. **Implementation on the ground.** Then come the departments, budgets and local authorities that apply the rule. This step lies beyond the data on this page: a published decree is not a result achieved. Nor does the page say whether the necessary funds were made available, or what the local authorities responsible for applying certain laws do: no source was read on these two points.

<details class="repli"><summary>The articles of the Constitution, word for word</summary>

**Article 10.** "{{< app-val "cit_art10" >}}" "{{< app-val "cit_art10_al2" >}}"

**Article 61.** Institutional Acts are referred to the Constitutional Council before their promulgation (para. 1). For the others, paragraph 2 provides: "{{< app-val "cit_art61_saisine" >}}" In these cases, "{{< app-val "cit_art61" >}}"

**Article 21**, on the Prime Minister: "{{< app-val "cit_art21_exec" >}}" Subject to article 13, "{{< app-val "cit_art21_regl" >}}".

**Article 13.** "{{< app-val "cit_art13" >}}"

**Article 22.** "{{< app-val "cit_art22" >}}"

</details>

The Civil Code does not cover every provision that announces a decree: it covers those whose implementation "requires" measures («&nbsp;dont l'exécution nécessite&nbsp;»). A law may refer to a decree for a provision that already applies without it. In case of dispute, the court decides, provision by provision. In 2021, on buildings for caged laying hens, the Conseil d'État thus held that «&nbsp;{{< app-val "cit_ce_precision" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_precision_tr" >}}"] (CE, 27 May 2021, no. 441660).

## How many laws are still waiting for a measure? {#lois-en-attente}

{{< figure-svg fichier="appliquer-statut-en" alt="Horizontal bars, one per session from 2017-2018 to 2024-2025: laws waiting for at least one measure, laws that have received all their measures, laws classified as having no measure to take, a law with no schedule. Every session has laws still waiting, including the oldest. The values are in the table below the figure." >}}Laws promulgated in each session, excluding treaties, and their administrative status at the reading date ({{< app-val "releve" >}}), according to the barometer of the application of laws. A "pending" measure is not necessarily late.{{< /figure-svg >}}

{{< fig-actions id="statut" >}}

{{< app-tableau "statut" "The figure's values in a table" >}}

<div class="resultat-phrase">

**The finding in one sentence.** On {{< app-val "releve" >}}, according to the barometer, {{< app-val "L_att" >}} of the {{< app-val "nlois" >}} laws promulgated in France from October 2017 to September 2025, excluding treaties, still had at least one measure classified as pending; {{< app-val "L_tout" >}} had received all their measures, {{< app-val "L_dir" >}} were classified as having no measure to take, and one had no schedule.

</div>

**Measured against the laws classified with measures to take.** At the reading date, the barometer classifies {{< app-val "L_dir" >}} of the {{< app-val "nlois" >}} laws promulgated as having no measure to take. Of the others, {{< app-val "L_mes" >}} have a schedule that contains at least one measure to take, still pending or already taken, and one has no schedule. Among these {{< app-val "L_mes" >}} laws, the {{< app-val "L_att" >}} pending laws make up {{< app-val "L_att_pct_mes" >}}, about one in two. The law with no schedule is counted on neither side. Both shares are accurate: one sets the pending laws against all the laws promulgated, the other against only the laws that the barometer classifies with at least one measure to take.

**A category of the barometer is not an initial need.** The barometer classifies a law as having "no measure to take" when all its measures are classified as “not applicable” (sans objet) at the reading date: it is a current status, not proof that the law provided for no measure. Law no. 2025-138 on amyotrophic lateral sclerosis is the counter-example: classified as having no measure to take, it provided for a ministerial order, since adopted, whose reference is given in the barometer's observation («&nbsp;{{< app-val "cas_2025_138" >}}&nbsp;»; see the next section). The ratio of {{< app-val "L_att" >}} to {{< app-val "L_mes" >}} therefore compares two categories of the barometer; it does not say what share of the laws that provided for a measure are still waiting for one.

**What these two shares do not say.** They say neither that these {{< app-val "L_att" >}} laws were wholly inapplicable, nor that each of their pending measures was late. A law may apply for the most part while waiting for a decree on one point, and the law itself may defer a measure. The planned date is missing for {{< app-val "A_sans_date" >}} of the {{< app-val "A" >}} pending measures: without a date, the page cannot say whether a measure is late. Age does not settle everything: for the 2017-2018 session, the oldest, {{< app-val "L_att_1718" >}} laws out of {{< app-val "L_N_1718" >}} are still waiting for at least one measure.

**The Senate as a check.** The Senate, for its part, counts "fully applicable" laws: those directly applicable and those that have received all the planned measures. For the 2024-2025 session, it writes: «&nbsp;{{< app-val "cit_802_36" >}}&nbsp;» [our translation: "{{< app-val "cit_802_36_tr" >}}"] It adds: «&nbsp;{{< app-val "cit_802_detail" >}}&nbsp;» [our translation: "{{< app-val "cit_802_detail_tr" >}}"] The barometer also counts {{< app-val "s25_N" >}} laws for this session. On {{< app-val "releve" >}}, these same two categories cover {{< app-val "s25_dirtout" >}} of them: {{< app-val "s25_dir" >}} with no measure to take and {{< app-val "s25_tout" >}} whose measures have all been taken. These are two findings, on two dates, by two producers that do not classify laws in the same way: they neither add up nor confirm each other, and nothing establishes that the laws counted on each side are the same.

## How many implementing measures are still pending? {#mesures-en-attente}

A law waits for measures; it is in measures that the barometer tracks application.

{{< figure-svg fichier="appliquer-mesures-en" alt="Horizontal bars, one per session of the law, from 2017-2018 to 2024-2025: measures with an identified published instrument, pending, classified as “not applicable”, with an incomplete status. A pending share remains in every session, including the oldest. The values are in the table below the figure." >}}Implementing measures listed by the barometer of the application of laws for the laws promulgated in each session, excluding treaties, and their status on {{< app-val "releve" >}}. It is a status at a date: neither a historical rate nor a measure of efficiency.{{< /figure-svg >}}

{{< fig-actions id="mesures" >}}

{{< app-tableau "mesures" "The figure's values in a table" >}}

On {{< app-val "releve" >}}, of the {{< app-val "nmes" >}} measures listed for these laws, {{< app-val "P" >}} have an identified published instrument, {{< app-val "A" >}} are pending, {{< app-val "S" >}} are classified as “not applicable” (sans objet) and {{< app-val "U" >}} have an incomplete status ("applied" with no identified instrument). For the laws of 2017-2018, {{< app-val "A_1718" >}} measures out of {{< app-val "N_1718" >}} remain pending; for those of 2024-2025, {{< app-val "A_2425" >}} out of {{< app-val "N_2425" >}}.

**"Pending" does not mean "late".** {{< app-val "differ_A" >}} of the {{< app-val "A" >}} pending measures carry, in their subject or their observation, the word «&nbsp;différé&nbsp;» or «&nbsp;différée&nbsp;» (deferred), {{< app-val "differ_1819" >}} of them for the laws of 2018-2019 and {{< app-val "differ_1920" >}} for those of 2019-2020; the word does not say whether the deferred date has passed. The planned date is missing for {{< app-val "A_sans_date" >}} of the {{< app-val "A" >}} pending measures: how long a measure has been waiting therefore cannot be calculated, and the page publishes no time frame.

**“Not applicable” is a label, not a proof.** The producer files {{< app-val "S" >}} measures under this label and gives the reason in an observation. Sorted by written rules, these observations most often say that the measure is already implemented by an existing text ({{< app-val "tri_deja" >}}), that its legal basis was repealed, rewritten or stripped of its reference to a decree ({{< app-val "tri_base" >}}), or that no measure is needed ({{< app-val "tri_aucune" >}}); {{< app-val "tri_event" >}} concern optional measures that were not used, {{< app-val "tri_nonprise" >}} say that a decree was not adopted, and {{< app-val "tri_indet" >}} remain undetermined, since they do not fall under a single rule. This sorting repeats what the producer writes; it reclassifies no measure.

Of the {{< app-val "S" >}} “not applicable” observations, there remain the {{< app-val "tri_acte" >}} that begin with the reference of an order or a decree. For the laws of 2024-2025, they number {{< app-val "obs_acte_2425" >}}. The {{< app-val "obs_ecartes" >}} observations that begin with «&nbsp;Décret non pris&nbsp;» (decree not adopted), with no reference to an instrument, are not counted among them. For law no. 2025-138, the observation reads «&nbsp;{{< app-val "cas_2025_138" >}}&nbsp;» (an arrêté is a ministerial order), and the Government's report at 31 December 2025 counts its measure as pending: the two sources describe two states, on two dates, and do not contradict each other.

<details class="repli"><summary>What was checked, and how</summary>

The measures are those of the barometer of the application of laws, published by the National Assembly and LexImpact from DILA's implementation schedules, in its version of {{< app-val "releve" >}}. A measure counts as published if its status is "applied" and an instrument is identified; "applied" without an identified instrument gives an incomplete status. The script checks that each measure falls into one and only one category, session by session, and that the same producer's file of laws gives, law by law, the same number of measures applied and to be applied; it also checks that each law falls under one and only one of the four statuses. A second program, written separately, recounted the categories of measures from the raw file: the numbers match.

The rules used to sort the “not applicable” observations are published in the dataset; an observation that falls under none or several of the rules is undetermined. An observation counts as carrying the reference of an instrument if it begins with «&nbsp;Arrêté du&nbsp;», «&nbsp;Décret du&nbsp;» or «&nbsp;Décret n°&nbsp;»; those that begin with the word but no reference are listed in the dataset, with their reason.

The barometer only publishes the current status. DILA's open data on implementation schedules only go back to July 2025. No "six months after the law" rate can therefore be recalculated for earlier sessions, and the page publishes none.

</details>

## Can a law apply without any decree? {#lois-application-directe}

Yes. The barometer and the Senate, in its annual reports, each classify laws as directly applicable, but not always the same ones. The barometer classifies a law this way when its schedule contains no measure other than “not applicable”; the Senate applies its own rules. Matched law by law over the {{< app-val "nlois" >}} laws promulgated from 2017-2018 to 2024-2025, excluding {{< app-val "conventions" >}} international treaties, the two sources keep exactly the same scope, but classify {{< app-val "ndesacc" >}} laws differently.

{{< figure-svg fichier="appliquer-lois-en" alt="Horizontal bars, one per session: laws directly applicable for both sources, laws classified differently, laws that neither source classifies as directly applicable; a mark shows half of each session's laws. In 2018-2019, directly applicable and divergent laws together exceed half. The values are in the table below the figure." >}}Laws promulgated in each session, excluding treaties. In blue, laws directly applicable for both sources; in dark grey, those they classify differently; the black mark shows half of the session's laws. For 2024-2025, the Senate publishes {{< app-val "s25_senat" >}} directly applicable laws in its summary and {{< app-val "s25_publie" >}} elsewhere in the same report: the gap is counted in dark grey.{{< /figure-svg >}}

{{< fig-actions id="lois" >}}

{{< app-tableau "lois" "The figure's values in a table" >}}

In {{< app-val "nautres" >}} sessions out of {{< app-val "nsessions" >}}, directly applicable laws stay below half, whatever the source. In {{< app-val "ct_session" >}}, the barometer counts {{< app-val "ct_baro" >}} out of {{< app-val "ct_N" >}}, more than half, while the Senate counts {{< app-val "ct_senat" >}}.

The 2024-2025 gap can be read within a single Senate report. Its summary says: «&nbsp;{{< app-val "cit_802_22" >}}&nbsp;» [our translation: "{{< app-val "cit_802_22_tr" >}}"]; another page states that «&nbsp;{{< app-val "cit_802_24" >}}&nbsp;» [our translation: "{{< app-val "cit_802_24_tr" >}}"]. The barometer counts {{< app-val "s25_baro" >}}. The gap between {{< app-val "s25_baro" >}} and {{< app-val "s25_senat" >}} is explained law by law by different classification rules; the one between {{< app-val "s25_senat" >}} and {{< app-val "s25_publie" >}} is not, for lack of a list of names.

<details class="repli"><summary>Why the two sources diverge on {{< app-val "ndesacc" >}} laws</summary>

The Senate classifies laws in the annexes to its reports. Several rules explain part of the gaps with the barometer: in some years, the Senate leaves out the measures that the law makes optional; the barometer classifies as "directly applicable" a law all of whose measures are now classified as “not applicable”; it classifies as "not directly applicable" a law with no schedule. Applied together, these rules remove some gaps and create others: they are not applied uniformly from one year to the next. All the laws in a gap are counted as uncertain, even when a rule explains them; hence the bounds in the table.

Defects in the Senate's annexes, such as a wrong law number or an announced count that does not match the list that follows, were corrected using the title and date of the law; the law-by-law register flags them.

</details>

## Does the Government have a deadline to adopt the decrees? {#delai-raisonnable}

Articles 13 and 21 of the Constitution set no deadline. The Government sets itself a six-month deadline, according to the Senate (see the series below). The courts, for their part, impose an obligation: «&nbsp;{{< app-val "cit_ce_principe" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_principe_tr" >}}"] (Conseil d'État, 27 May 2021, no. 441660; the same wording appears in its decisions of 29 June 2011 and 21 January 2021). It also applies to the ministerial order to which an implementing decree refers certain measures (CE, 21 January 2021, no. 429956).

The reasonable time is not set once and for all: it is assessed «&nbsp;{{< app-val "cit_ce_nature" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_nature_tr" >}}"] (CE, 27 July 2005, no. 261694). Periods held excessive in one case do not therefore make a rule.

A refusal to adopt a measure that is due can be brought before the administrative courts, which can annul it and order the measure to be adopted: in May 2021, the Conseil d'État ordered the Prime Minister to adopt a decree, and in January 2021 it ordered the Minister of Justice to adopt an order, each time within a period it set. The delay may also make the State liable and give rise to compensation (CE, 27 July 2005).

A planned measure is not always due. In 2011, about an order provided for by a decree and never adopted, the Conseil d'État held that the minister was not bound to adopt it: the article that provided for this order already set out exhaustively the content of the file in question, and referred to the order only the model of that file (CE, 29 June 2011, no. 343188).

<details class="repli"><summary>The Conseil d’État’s decisions, word for word</summary>

**Orders adopted on referral from a decree** (CE, 21 January 2021, no. 429956): «&nbsp;{{< app-val "cit_ce_arrete" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_arrete_tr" >}}"]

**Injunctions.** In May 2021, the Conseil d'État decided «&nbsp;{{< app-val "cit_ce_injonction" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_injonction_tr" >}}"] (no. 441660); in January 2021, «&nbsp;{{< app-val "cit_ce_arrete_injonction" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_arrete_injonction_tr" >}}"] (no. 429956).

**Compensation** (CE, 27 July 2005, no. 261694): «&nbsp;{{< app-val "cit_ce_reparation" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_reparation_tr" >}}"].

**A planned measure that was not due** (CE, 29 June 2011, no. 343188). The Conseil d'État notes that «&nbsp;{{< app-val "cit_ce_exhaustif" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_exhaustif_tr" >}}"], and concludes that «&nbsp;{{< app-val "cit_ce_pas_tenu" >}}&nbsp;» [our translation: "{{< app-val "cit_ce_pas_tenu_tr" >}}"].

</details>

**What these decisions do not say.** They lay down a rule and settle cases; they say neither how many refusals are brought before the courts nor what becomes of the orders issued, and no data read here measures it. Nor does the barometer's "pending" status say whether a measure is due, or whether the reasonable time has been exceeded.

## Why do the French Senate and Government publish different rates? {#taux-publies}

Because their counting conventions have differed and still differ in part. The gap has a history.

**In 2012-2013, rates that matched.** The Senate writes that, «&nbsp;{{< app-val "cit_1213" >}}&nbsp;» [our translation: "{{< app-val "cit_1213_tr" >}}"]. That year, the rate changed depending on whether laws or measures were counted, not on who produced it.

**In 2017-2019, a gap and its reasons.** For 2017-2018, once deferred measures are set aside, the Senate's and the Government's rates come closer, {{< app-val "s1718_hd" >}} for the Senate and {{< app-val "sgg1718" >}} for the Government; ministerial orders, which only the Senate counted, remain a difference of scope. For 2018-2019, the Senate publishes {{< app-val "senat_1819" >}} and reports that the Government reaches {{< app-val "sgg_1819" >}}. In 2019, the Senate itself gave two technical reasons for the gap, ministerial orders and deferred measures, and a third ground, which it called political reasons, in particular when it considers that a decree adopted does not respect the legislature's intent: the expected measure then counts for it as not taken. A rate can thus include a judgement, and not only a count.

<details class="repli"><summary>What the Senate and the Government wrote in 2018 and 2019, word for word</summary>

For 2017-2018, the Senate writes: «&nbsp;{{< app-val "cit_senat_1718" >}}&nbsp;» [our translation: "{{< app-val "cit_senat_1718_tr" >}}"]. The General Secretariat of the Government, heard by the Senate, states: «&nbsp;{{< app-val "cit_sgg_1718" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg_1718_tr" >}}"].

For 2018-2019, the Senate writes: «&nbsp;{{< app-val "cit_senat_1819" >}}&nbsp;» [our translation: "{{< app-val "cit_senat_1819_tr" >}}"] and adds that «&nbsp;{{< app-val "cit_sgg_1819" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg_1819_tr" >}}"].

In 2019, it gave the reasons: «&nbsp;{{< app-val "cit_diverge" >}}&nbsp;» [our translation: "{{< app-val "cit_diverge_tr" >}}"] First, «&nbsp;{{< app-val "cit_arretes" >}}&nbsp;» [our translation: "{{< app-val "cit_arretes_tr" >}}"] Second, «&nbsp;{{< app-val "cit_differees" >}}&nbsp;» [our translation: "{{< app-val "cit_differees_tr" >}}"] It also mentions a third ground: «&nbsp;{{< app-val "cit_politique" >}}&nbsp;» [our translation: "{{< app-val "cit_politique_tr" >}}"]

</details>

**Since 2024, methods brought closer.** The Senate's 2026 report says so: «&nbsp;{{< app-val "cit_802_arretes" >}}&nbsp;» [our translation: "{{< app-val "cit_802_arretes_tr" >}}"] For the Senate itself, «&nbsp;{{< app-val "cit_802_differees" >}}&nbsp;» [our translation: "{{< app-val "cit_802_differees_tr" >}}"]. It adds: «&nbsp;{{< app-val "cit_802_appreciation" >}}&nbsp;» [our translation: "{{< app-val "cit_802_appreciation_tr" >}}"]

**The rates published today.** At 31 December 2025, the Government's half-yearly report on the 16th legislature «&nbsp;{{< app-val "cit_sgg16_def" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg16_def_tr" >}}"] It gives a rate of {{< app-val "sgg16_taux" >}}, over {{< app-val "sgg16_n" >}} measures. The report on the 17th legislature «&nbsp;{{< app-val "cit_sgg17_def" >}}&nbsp;» [our translation: "{{< app-val "cit_sgg17_def_tr" >}}"] It gives {{< app-val "sgg17_taux" >}}, over {{< app-val "sgg17_n" >}} measures. The Senate publishes {{< app-val "s2425" >}} for the 2024-2025 session. These three rates cover neither the same laws, nor the same measures, nor the same date: the table below sets them out by definition, it does not rank them. An implementation rate can only be interpreted with its scope, its cut-off date and its counting rules.

{{< app-tableau "taux" "The definition of each rate" >}}

## Has the implementation rate of laws risen since 2002? {#serie-senat}

The Senate's series does not allow us to say so from end to end. The corpus shows {{< app-val "nsegments" >}} successive definitions since 2002-2003, which differ in cut-off date, scope of laws and treatment of deferred and optional measures: the segments do not read as a single series. The Senate nevertheless reads a trend across its own breaks: «&nbsp;{{< app-val "cit_802_baisse" >}}&nbsp;» [our translation: "{{< app-val "cit_802_baisse_tr" >}}"]. Its series only allows this reading to be tested segment by segment: 2024-2025 falls under a different definition from the previous sessions.

{{< figure-svg fichier="appliquer-serie-en" alt="Points by session from 2002-2003 to 2024-2025, grouped in segments separated by changes of definition. The first segment, from 2002-2003 to 2008-2009, lies well below the following ones. The values, their document and their definition are in the table below the figure." >}}Implementation rates of laws published by the French Senate, as published. The segments correspond to different definitions: do not join them. The open circle marks the 2019-2020 figure given by the following report.{{< /figure-svg >}}

{{< fig-actions id="serie" >}}

{{< app-tableau "serie" "The values, their document and their definition" >}}

The last point of the first segment and the first point kept from the next are separated by a change of definition: in order to count the measures taken only once the time limit the Government sets itself has expired, the Senate then shifts the period it uses. In 2024-2025, it publishes a single rate («&nbsp;{{< app-val "cit_802_66" >}}&nbsp;» [our translation: "{{< app-val "cit_802_66_tr" >}}"]), and specifies in a note: «&nbsp;{{< app-val "cit_802_note" >}}&nbsp;» [our translation: "{{< app-val "cit_802_note_tr" >}}"] Optional measures (mesures éventuelles) are those the law allows without requiring them.

The "+ {{< app-val "plus4" >}} points" cannot be read in the table, which gives {{< app-val "s2324" >}} for 2023-2024: the Senate compares with its 2023-2024 rate excluding deferred measures. The previous report said so: «&nbsp;{{< app-val "cit_2324_62" >}}&nbsp;» [our translation: "{{< app-val "cit_2324_62_tr" >}}"].

For 2019-2020, the reports give two values, that of the 2020 report and that of the following report, marked with an open circle in the figure. A revised figure or another variant of the rate: the documents do not settle it, and the series keeps both values. The 2009-2010 session is not shown in the figure, for lack of a cut-off date established in the sentence that gives its rate. Two values for the same session and a change of definition are two distinct facts: the series keeps both.

<details class="repli"><summary>The change of definition and the two 2019-2020 values, word for word</summary>

The break between the first two segments, according to the Senate: «&nbsp;{{< app-val "cit_six_mois" >}}&nbsp;» [our translation: "{{< app-val "cit_six_mois_tr" >}}"]

For 2019-2020, the 2020 report says: «&nbsp;{{< app-val "cit_2020_62" >}}&nbsp;» [our translation: "{{< app-val "cit_2020_62_tr" >}}"]. The next one, on 2020-2021, writes «&nbsp;{{< app-val "cit_2021_60" >}}&nbsp;» [our translation: "{{< app-val "cit_2021_60_tr" >}}"], then: «&nbsp;{{< app-val "cit_2021_62" >}}&nbsp;» [our translation: "{{< app-val "cit_2021_62_tr" >}}"].

</details>

## What this page does not say {#limites}

It does not say whether a law produces the effect the promise aimed at. It does not measure the quality of decrees, nor whether they reflect the legislature's intent, which the Senate assesses itself. It gives no publication time, for lack of a dated history of the schedules. It sets the Senate's and the Government's rates side by side with their definitions, without ranking them, and does not join two segments of the Senate's series.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="After the vote" avis="non" >}}
This page counts what a law still waits for after the vote. The book follows nine written, dated and signed promises along the chain that runs from the decision to its outcome: what a president decides within his own chain of power, what he has to get voted, what he has to negotiate, and what will never depend on him. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Barometer of the application of laws**, National Assembly and LexImpact, from DILA's implementation schedules: files of laws and of measures, version of {{< app-val "releve" >}}.

**French Senate**, annual reports on the application of laws from 2011 to 2026, summaries and press releases from 2003 to 2011 (in French); the document and page of each value and each quotation are given in the dataset.

**General Secretariat of the Government**, half-yearly report on the application of laws at 31 December 2025, read on Légifrance through a browser (in French).

**Conseil d'État**, decisions of 27 July 2005 (no. 261694), 29 June 2011 (no. 343188), 21 January 2021 (no. 429956) and 27 May 2021 (no. 441660), read on ArianeWeb (in French).

**Constitution**, arts. 10, 13, 21, 22 and 61, quoted in the English translation published by the Conseil constitutionnel; **Civil Code**, art. 1, read on Légifrance (API).

The figures, quotations, checks and charts are produced by a single script, which stops if a piece of data no longer meets the conditions on which the main sentences rest. Each quotation is checked word for word in the archived document it comes from: pages of the Senate's reports, articles of the Constitution and of the Civil Code, decisions of the Conseil d'État; for the report of the General Secretariat of the Government, which Légifrance refuses to scripts, in an extract of the page read through a browser, whose fingerprint is the one the browser computed. Counts of laws and measures are recalculated from the barometer's files; the Senate's rates, transcribed in the script, are reread in the archived pages of its reports; the sorting of the “not applicable” observations follows rules written in the script. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_appliquer.csv), long format; [JSON](/promesses_appliquer.json), with definitions, the sorting rules and the record of the checks (field names and some labels in French). This dataset is also archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier for citation: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_appliquer" jeu="promesses_appliquer" sources="National Assembly and LexImpact (DILA data), French Senate, General Secretariat of the Government, Conseil d'État, Légifrance" donnees="The status of laws and of their implementing measures by session, the sorting of the “not applicable” observations, the laws directly applicable according to the two sources, and the rates published by the Senate since 2002-2003 and by the Government at 31 December 2025; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
On {{< app-val "releve" >}}, according to the barometer of the application of laws, {{< app-val "L_att" >}} of the {{< app-val "nlois" >}} laws promulgated in France from October 2017 to September 2025, excluding treaties, were still waiting for at least one measure; {{< app-val "L_tout" >}} had received all of them and {{< app-val "L_dir" >}} were classified as having no measure to take. The Conseil d'État requires the measures that the application of the law necessarily implies to be taken within a reasonable time. The implementation rates of the Senate and the Government rest on different counting conventions, and the Senate's series on {{< app-val "nsegments" >}} successive definitions since 2002-2003.
{{< /reutiliser >}}
