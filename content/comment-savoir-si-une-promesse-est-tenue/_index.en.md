---
title: "How to tell whether a promise was kept?"
url: /en/how-to-tell-whether-a-promise-was-kept/
description: "To judge \"bringing unemployment down\" in France, two measures are most used: the unemployed in the ILO sense and the registrants in category A at France Travail do not cover exactly the same population, and the registration rules changed on 1 January 2025. Insee 2024 estimate and Dares series, open data."
chapo: "Unemployment as a test case: choose the indicator and the starting point, and check that the rule has not changed. For unemployment in France, two measures are most used, unemployment in the ILO sense and the registrants in category A at France Travail; they rest on different definitions, and their populations only partly coincide. Since 2025, the rules for registering with France Travail have also changed, which affects comparisons over time."
date: 2026-10-06
lastmod: 2026-10-06
# English version of tab 5 of the "Presidential promises" dossier (FR: content/comment-savoir-si-une-promesse-est-tenue/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_mesurer.json
# (scripts/update_promesses_mesurer.py), whose guards cover both languages. French texts are quoted in French, followed
# by our translation.
donnees: [promesses_mesurer]
og_title: "How to tell whether a promise was kept? Two measures of unemployment in France, two populations — S. Lalut"
og_image: "images/og-mesurer-promesse-en.jpg"
og_image_alt: "Share card: \"Two measures, two populations\" — a bar in three segments, in thousands of people, 2024 average: the ILO-unemployed not registered in category A, those counted in both measures, and the category A registrants who are not ILO-unemployed (Insee estimate)."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_mesurer"
  nom: "Unemployment in the ILO sense and category A registration in France: 2024 cross-tabulation and registrant series with and without automatically registered groups"
  description: "Restitution, checked against the published PDF, of Insee's estimated cross-tabulation of ILO activity status and France Travail registration category (2024 average, France excluding Mayotte, aged 15-64, ordinary housing; Insee Références 2026, file 1, figure 2); quarterly seasonally adjusted series of category A registrants and of category A registrants excluding RSA recipients and young people in programmes (Dares-France Travail, France excluding Mayotte, 2018 to 2026)."
  couverture_temporelle: "2018/2026"
  couverture_spatiale: "France excluding Mayotte"
  variables:
    - {nom: "People by ILO status and registration category", unite: "thousands of people (2024 average, estimate)"}
    - {nom: "Category A registrants, with and without the groups registered automatically since 2025", unite: "people, end of quarter, seasonally adjusted"}
  sources:
    - "https://www.insee.fr/fr/statistiques/8733119?sommaire=8733125"
    - "https://data.dares.travail-emploi.gouv.fr/explore/dataset/dares_defm_stock_france_cvs_trim/"
  mots: ["unemployment", "ILO", "France Travail", "category A", "election promise", "indicator", "full employment act", "France"]
  fichiers: ["promesses_mesurer.csv", "promesses_mesurer.json"]
faq:
  - question: "What is the difference between ILO unemployment and category A registrants in France?"
    answer: "They are two definitions. According to Insee, an unemployed person in the ILO sense is a person aged 15 or over without a job, available to take one within fifteen days and who has actively looked for one in the previous month (our translation); this is measured by the Labour Force Survey. Category A at France Travail groups people with no activity during the month and required to look for a job (our translation); it is an administrative register. For 2024, Insee estimates that {mes.p_a}% of category A registrants are unemployed in the ILO sense and that {mes.p_b}% of the ILO-unemployed are registered in category A."
  - question: "Why did the number of category A registrants change in 2025?"
    answer: "Since January 2025, under the full employment act of 18 December 2023, applicants for and recipients of the RSA (minimum income), young people followed by local youth missions in a youth commitment contract or Pacea, and disabled people followed by Cap emploi are registered automatically with France Travail. The Dares, which publishes these series, reports other changes the same year (rules for monthly updating, sanctions regime) and publishes a series excluding RSA recipients and young people in programmes. The French Official Statistics Authority suspended the official label of these series for the period from 1 January 2025 to 20 May 2026."
  - question: "How should a promise to reduce unemployment be judged?"
    answer: "By setting in advance the indicator (ILO unemployment or category A registrants) and the point of comparison (the starting date and value), and by checking that the measurement rule has not changed between the two dates; then by asking what share of the change can honestly be attributed to the decisions of whoever made the promise. An observed change is not enough to establish its cause."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 50
  nature: "Insee estimate and Dares series, checked and restated; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "How to tell whether a promise was kept?"
  court: "Measure"
  role: "indicators and breaks"
---

{{< reutiliser-ancre >}}

"Bringing unemployment down" is a good test case: before even assessing the result, one has to decide what is called unemployment. In France, two measures are most used, published by two institutions, under two definitions. This page restates the Insee estimate that cross-tabulates them, checked cell by cell against the published document, and the registration rule that changed in 2025. French texts are quoted in French, followed by our translation.

## What do ILO unemployment and category A count? {#deux-chiffres}

The first is **unemployment in the sense of the International Labour Organization (ILO)**, measured by Insee, the French statistics institute, from the Labour Force Survey. According to Insee, an unemployed person is «&nbsp;une personne âgée de 15&nbsp;ans ou plus sans emploi, disponible pour en occuper un dans les quinze jours et qui a activement cherché un emploi dans le mois précédent&nbsp;» [our translation: "a person aged 15 or over without a job, available to take one within fifteen days and who has actively looked for a job in the previous month"]. The second is the number of **registrants in category A at France Travail**, the public employment service, taken from an administrative register: category A groups «&nbsp;les personnes sans activité au cours du mois et tenues de rechercher un emploi&nbsp;» [our translation: "people with no activity during the month and required to look for a job"].

A survey and a register do not see the same people: one can actively look for a job without being registered, and be registered without meeting the ILO criteria. Insee, the Dares (the labour ministry's statistics department) and France Travail matched the two sources to measure this gap.

{{< figure-svg fichier="mesurer-recoupement-en" alt="Bar in three segments, in thousands of people, 2024 average: on the left the ILO-unemployed not registered in category A, in the centre the people counted in both measures, on the right the category A registrants who are not ILO-unemployed. A bracket above groups the ILO-unemployed, a bracket below the category A registrants." >}}Cross-tabulation of ILO status and registration with France Travail, 2024 average, France excluding Mayotte, people aged 15 to 64 living in ordinary housing. Insee estimate (Dares-Insee-France Travail matching).{{< /figure-svg >}}

{{< fig-actions id="recoupement" >}}

<div class="resultat-phrase">

**The finding in one sentence.** In 2024, according to the Insee estimate, {{< mes-val "commun_env" >}} people are counted in both measures at once; {{< mes-val "a_seul_env" >}} category A registrants are not unemployed in the ILO sense, and {{< mes-val "bit_seul" >}} ILO-unemployed are not registered in category A: two definitions, populations that partly overlap.

</div>

<details class="repli"><summary>Who are those who appear in only one of the two measures?</summary>

Among the **category A registrants who are not ILO-unemployed**, Insee counts {{< mes-val "a_halo" >}} people in the "halo around unemployment" (without a job, but not available within two weeks or without active search in the month), {{< mes-val "a_hors_halo" >}} inactive people outside that halo and {{< mes-val "a_emploi" >}} people in work.

Among the **ILO-unemployed who are not registered in category A**, {{< mes-val "bit_non_inscrits" >}} are not registered at all with France Travail, {{< mes-val "bit_bc" >}} are registered in category B or C (reduced activity in the month) and {{< mes-val "bit_de" >}} in category D or E.

The shares say it another way: {{< mes-val "p_a" >}}% of category A registrants are unemployed in the ILO sense, and {{< mes-val "p_b" >}}% of the ILO-unemployed are registered in category A.

**What was checked.** The counts come from the spreadsheet published by Insee; a second extraction, written separately from the published PDF document, finds the same 35 values (24 cells and 11 totals), the same year and the same scope. The three sets restated by subtraction equal those Insee prints in another table of the same file. This check verifies that the page restates the published estimate exactly; it does not redo the matching, whose individual data are not public.

</details>

## Has the rule for counting registrants stayed the same? {#regle-de-mesure}

No: the rules for registration and monthly updating changed from 2025. Since January 2025, under the [full employment act of 18 December 2023](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048581935) (in French), applicants for and recipients of the RSA (minimum income), young people followed by local youth missions in a youth commitment contract or Pacea, and disabled people followed by Cap emploi are **registered automatically** with France Travail. The Dares, which publishes these series with France Travail, reports other changes the same year in its metadata: automatic monthly updating of new registrants from January to March 2025, restricted in April, a new sanctions regime in June, and 36,000 people wrongly counted in category A in March and then reclassified.

The [French Official Statistics Authority](https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/11/Delibere-ASP-statistiques-marche-du-travail_14nov2024_VF.pdf) (Autorité de la statistique publique), responsible among other things for labelling public statistics, **suspended the official label** of these series for the period from 1 January 2025 to the end of the label then in force, 20 May 2026. Its reason: the rule changes «&nbsp;rendr[ont] difficilement interprétables les séries statistiques de demandeurs d'emploi jusqu'ici labellisées&nbsp;» [our translation: "will make the hitherto labelled statistical series of jobseekers difficult to interpret"] (decision of 14 November 2024, in French). The point established here is narrower: the conditions in which the series is produced and read have changed, which affects comparisons over time.

The Dares also publishes a series of category A registrants **excluding RSA recipients and young people in programmes**, available since 2018.

**Note: the levels of the two figures on this page are not directly comparable.** The first is a 2024 average for people aged 15-64 living in ordinary housing; the second is an administrative stock at the end of each quarter, on a different scope.

{{< figure-svg fichier="mesurer-regle-en" alt="Two panels on the same scale, from 2018 to 2026: on the left published category A, on the right the series excluding RSA recipients and young people in programmes; in each, a dotted line marks 1 January 2025, change of rules." >}}Category A registrants at France Travail at the end of each quarter, France excluding Mayotte, seasonally and working-day adjusted, with and without RSA recipients and young people in programmes. Latest point: {{< mes-val "dares_fin" >}}.{{< /figure-svg >}}

{{< fig-actions id="regle" >}}

The two panels describe **two different populations**, and the second excludes these groups over the whole period, before as well as after 2025. Their gap is therefore not the effect of the reform, and a small gap would not prove a small effect. Insee notes for its part that the 2025 changes may also affect job search behaviour, and therefore the ILO measure: neither series is an intact witness of what would have happened without the law.

## How should a promise be judged with these figures? {#juger-une-promesse}

A promise to reduce unemployment, taken as an example and aimed at no one, is judged in four steps, which are the last four questions of the book's grid:

1. **By which indicator?** ILO unemployment or category A registrants: they do not cover exactly the same population, and one cannot be swapped for the other along the way.
2. **Against which point of comparison?** The starting value, at a date stated in advance, not the most favourable date chosen afterwards.
3. **Has the rule that will say whether it was kept stayed the same?** For registrants, not since 2025: a before-and-after comparison must deal with the break, or change indicator.
4. **What share of the result can honestly be attributed to whoever made the promise?** An observed change is not enough to establish its cause: other factors may vary at the same time.

## What this page does not say {#limites}

It does not say which of the two measures is the right one: they answer two different questions, one about people's situation, the other about their registration. It does not say whether a policy brought either one down, nor what the effect of the full employment act is: none of the series shown measures it. The cross-tabulation is an Insee **estimate**, for the 2024 average: it does not describe 2025 or 2026, which the matching does not cover.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Judging a promise to the end" avis="non" >}}
This page shows that a promise cannot be judged without choosing its indicator and checking its rule. The book applies these questions, and the four that precede them — what exactly is promised, who can decide it, with whose consent, within what time —, to nine written, dated and signed promises, one of them on employment. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Insee**, *Emploi, chômage, revenus du travail* [Employment, unemployment, labour income], Insee Références, 2026 edition, file 1 (published 2 July 2026), figures 2 and 8, definitions and methodological box; Dares-Insee-France Travail matching of the Historical Statistical File and the Labour Force Survey (in French).

**Dares and France Travail**, registrants at France Travail, quarterly stock, France, seasonally and working-day adjusted data, and the dataset's metadata (updated 28 July 2026): procedural changes of 2022 and 2025, categories F and G, series excluding RSA recipients and young people in programmes (in French).

**Autorité de la statistique publique** (French Official Statistics Authority), decision of 14 November 2024 on labour market statistics. **Law** no. 2023-1196 of 18 December 2023 on full employment (in French).

The figures, checks and charts are produced by a single script, which rereads the files published by Insee and the Dares and refuses to write if a figure stops supporting a sentence; no figure on this page is entered by hand. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_mesurer.csv), long format; [JSON](/promesses_mesurer.json), with definitions and the record of the checks (field names and some labels in French).

{{< reutiliser figures="figures_mesurer" jeu="promesses_mesurer" sources="Insee and Dares" donnees="The 2024 cross-tabulation of ILO status and registration category (24 cells and totals, in thousands), and the quarterly series of category A registrants with and without the groups registered automatically; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
To judge a promise on unemployment in France, one must first choose its figure: in 2024, according to the Insee estimate, {{< mes-val "commun_env" >}} people are counted both as unemployed in the ILO sense and as category A registrants, {{< mes-val "a_seul_env" >}} category A registrants are not ILO-unemployed and {{< mes-val "bit_seul" >}} unemployed are not registered in category A. Since 1 January 2025, the full employment act registers new groups automatically, and the official label of the registrant series was suspended for the period from 1 January 2025 to 20 May 2026. A before-and-after comparison must deal with this break, and an observed change does not tell its cause.
{{< /reutiliser >}}
