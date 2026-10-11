---
title: "How can we tell whether a promise was kept?"
url: /en/how-can-we-tell-whether-a-promise-was-kept/
description: "Judging \"bringing unemployment down\" in France: ILO unemployment and category A registrants at France Travail do not count the same people, and the rule for counting registrants changed in 2022, late 2024 and 2025. Insee estimate, Dares series, open data."
chapo: "Two accurate figures can tell two different stories. In 2024, according to Insee, only {mes.p_a}% of category A registrants at France Travail are unemployed in the sense of the International Labour Organization (ILO). And the rule for counting registrants changed in 2022, at the end of 2024 and in 2025, sometimes downwards, sometimes upwards. To judge a promise on unemployment, four questions: by which indicator, since when, has the rule stayed the same, what share can be attributed."
date: 2026-10-06
lastmod: 2026-10-12
# English version of tab 5 of the "Presidential promises" dossier (FR: content/comment-savoir-si-une-promesse-est-tenue/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_mesurer.json
# (scripts/update_promesses_mesurer.py), whose guards cover both languages. French texts are quoted in our translation
# (the French originals are in the French page and in the JSON); the numbers of each translation are checked against
# the original (guard M7).
donnees: [promesses_mesurer]
og_title: "How can we tell whether a promise was kept? Two measures of unemployment in France, two populations — S. Lalut"
og_image: "images/og-mesurer-promesse-en.jpg"
og_image_alt: "Share card: \"Two measures, two populations\" — a bar in three segments, in thousands of people, 2024 average: the people unemployed under the ILO definition not registered in category A, those counted in both measures, and the category A registrants who are not unemployed under the ILO definition (Insee estimate)."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_mesurer"
  nom: "Unemployment in the ILO sense and category A registration in France: 2024 cross-tabulation, registrant series with and without automatically registered groups, long series 2012-2025"
  description: "Restitution, checked against the published PDF, of Insee's estimated cross-tabulation of ILO activity status and France Travail registration category (2024 average, France excluding Mayotte, aged 15-64, ordinary households; Insee Références 2026, file 1, figure 2); quarterly seasonally adjusted series of category A registrants and of category A registrants excluding RSA recipients and young people in programmes (quarterly average of end-of-month registrants, Dares-France Travail, France excluding Mayotte, 2018 to 2026); 2012-2025 annual averages of both measures published by Insee (same file, figure 1); dated rule changes."
  couverture_temporelle: "2012/2026"
  couverture_spatiale: "France excluding Mayotte"
  variables:
    - {nom: "People by ILO status and registration category", unite: "thousands of people (2024 average, estimate)"}
    - {nom: "Category A registrants, with and without the groups registered automatically since 2025", unite: "people, quarterly average of end-of-month registrants, seasonally adjusted"}
    - {nom: "ILO unemployed and category A registrants, 2012-2025", unite: "millions of people, annual average"}
  sources:
    - "https://www.insee.fr/fr/statistiques/8733119?sommaire=8733125"
    - "https://data.dares.travail-emploi.gouv.fr/explore/dataset/dares_defm_stock_france_cvs_trim/"
  mots: ["unemployment", "ILO", "France Travail", "category A", "election promise", "indicator", "full employment act", "France"]
  fichiers: ["promesses_mesurer.csv", "promesses_mesurer.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "What is the difference between ILO unemployment and category A registrants in France?"
    answer: "They are two definitions. According to Insee, an unemployed person in the ILO sense is \"{mes.chomeur_bit}\" (our translation); this is measured by the Labour Force Survey. Category A at France Travail groups \"{mes.categorie_a}\" (our translation); it is an administrative register. For 2024, Insee estimates that {mes.p_a}% of category A registrants are unemployed in the ILO sense and that {mes.p_b}% of the people unemployed under the ILO definition are registered in category A."
  - question: "Why did the number of category A registrants change in 2025?"
    answer: "For several reasons at once, according to the Dares. Since January 2025, the full employment act of 18 December 2023 has provided for the automatic registration of several groups with France Travail; the Dares lists applicants for and recipients of the RSA (minimum income), young people followed by local youth employment services (missions locales) and disabled people followed by Cap emploi (the specialised employment service for disabled people); from January to March 2025, new registrants without entitlement to a France Travail allowance were updated automatically, and therefore counted in category A; in June 2025, the sanctions regime changed. The rule had already changed in 2022 and at the end of 2024, with two versions of the monthly updating form. The French Official Statistics Authority suspended the statistical quality label of these series from 1 January 2025."
  - question: "How should a promise to reduce unemployment be judged?"
    answer: "By setting in advance the indicator (ILO unemployment or category A registrants) and the point of comparison (the starting date and value), by checking that the measurement rule has not changed between the two dates, and then by asking what share of the change can honestly be attributed to the decisions of whoever made the promise. An observed change is not enough either to establish its cause or to rule it out."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 50
  nature: "Insee estimate and Dares series, checked and restated; open data"
  refonte: "2026-10-12"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "How can we tell whether a promise was kept?"
  court: "Measure"
  role: "indicators and breaks"
---

{{< reutiliser-ancre >}}

When a candidate promises to "bring unemployment down", we think we know what we will look at five years later: the unemployment figure. In France there are at least two, published by two institutions under two definitions, and they do not count the same people. This page puts to them the four questions that the book asks of any promise of results — **by which indicator, since when, has the rule stayed the same, what share can be attributed** — and answers each one with the data published by Insee, the French statistics institute, and the Dares. French texts are quoted in our translation.

## By which indicator? Two measures, two populations {#deux-chiffres}

The first indicator is **unemployment in the sense of the International Labour Organization (ILO)**, measured each quarter by Insee from the Labour Force Survey. According to Insee, an unemployed person is "{{< mes-val "chomeur_bit" >}}". The second is the number of **registrants in category A at France Travail**, the public employment service, taken from its register: category A groups "{{< mes-val "categorie_a" >}}".

A survey measures a situation; a register records a step taken and an administrative category, which depend on the registration rules. One can actively look for a job without being registered, and be registered without meeting the ILO criteria. To measure this gap, Insee, the Dares and France Travail matched the two sources for 2024:

{{< figure-svg fichier="mesurer-recoupement-en" alt="Bar in three segments, in thousands of people, 2024 average: on the left the people unemployed under the ILO definition not registered in category A, in the centre the people counted in both measures, on the right the category A registrants who are not unemployed under the ILO definition. A bracket above groups the people unemployed under the ILO definition, 62% of whom are registered in category A; a bracket below groups the category A registrants, 49% of whom are unemployed under the ILO definition." >}}Cross-tabulation of ILO status and registration with France Travail, 2024 average, France excluding Mayotte, people aged 15 to 64 living in ordinary households. Insee estimate (Dares-Insee-France Travail matching).{{< /figure-svg >}}

{{< fig-actions id="recoupement" >}}

<div class="resultat-phrase">

**The finding in one sentence.** In 2024, according to the Insee estimate, only {{< mes-val "p_a" >}}% of category A registrants are unemployed in the ILO sense, and {{< mes-val "p_b" >}}% of the people unemployed under the ILO definition are registered in category A.

</div>

The two measures have {{< mes-val "commun_env" >}} people in common. The category A registrants who are not unemployed in the ILO sense, {{< mes-val "a_seul_env" >}}, are, for the most part, not people in work: {{< mes-val "a_emploi" >}} of them have a job in the ILO sense. The other {{< mes-val "a_sans_emploi" >}} are without a job. Among them, {{< mes-val "a_halo" >}} are in the "halo around unemployment": they want to work, but are not available within two weeks or have not searched actively in the month. The remaining {{< mes-val "a_hors_halo" >}} are inactive, outside that halo.

<details class="repli"><summary>These counts are a survey estimate, whose margin is not published</summary>

The matching rests on the respondents of the Labour Force Survey, and Insee attributes to "{{< mes-val "cit_alea" >}}" the difference between the number of registrants it finds this way and the published number. The thousands shown restate the estimate; they do not give its precision.

</details>

<details class="repli"><summary>And the people unemployed in the ILO sense who are not registered in category A?</summary>

There are {{< mes-val "bit_seul" >}} of them. Among them, {{< mes-val "bit_non_inscrits" >}} are not registered at all with France Travail, {{< mes-val "bit_bc" >}} are registered in category B or C (they worked a few hours in the month, which takes them out of category A) and {{< mes-val "bit_de" >}} in category D or E (registrants who are not required to look for work, for instance because they are in training or in a subsidised job).

</details>

## Since when? The starting point changes the reading {#depuis-quand}

Judging a promise means comparing two dates. Over the long run, the two measures published by Insee, as annual averages, do not follow the same path:

{{< figure-svg fichier="mesurer-serie-longue-en" alt="Two lines from 2012 to 2025, in millions of people: category A registrants, above, and the ILO unemployed, below. The gap between them widens until 2020, narrows until 2024 and widens again in 2025. Four numbered markers show rule changes: unemployment insurance reform from 2019 to 2021, Labour Force Survey redesigned in 2021, monthly updating form in 2022, form of late 2024 and full employment act in 2025." >}}ILO unemployed and category A registrants at France Travail, annual averages published by Insee, 2012-2025, France excluding Mayotte, aged 15-64. Markers: rule changes documented by Insee and the Dares.{{< /figure-svg >}}

{{< fig-actions id="serie-longue" >}}

The gap between category A registrants and the ILO unemployed went from {{< mes-val "ecart_2012" >}} in 2012 to {{< mes-val "ecart_2020" >}} in 2020, the year of the health crisis. It came back down to {{< mes-val "ecart_2024" >}} in 2024, before rising again to {{< mes-val "ecart_2025" >}} in 2025. Insee sums up the period in the title of its study, "{{< mes-val "cit_insee_titre" >}}", and notes for 2025 that "{{< mes-val "cit_divergent" >}}". The same period can therefore show two different trends depending on the indicator chosen.

<details class="repli"><summary>The gap year by year</summary>

| Year | Gap between category A registrants and the ILO unemployed (annual average) |
|---|---|
| 2012 | {{< mes-val "ecart_2012" >}} |
| 2019 | {{< mes-val "ecart_2019" >}} |
| 2020 | {{< mes-val "ecart_2020" >}} |
| 2021 | {{< mes-val "ecart_2021" >}} |
| 2024 | {{< mes-val "ecart_2024" >}} |
| 2025 | {{< mes-val "ecart_2025" >}} |

Annual averages published by Insee (*Emploi, chômage, revenus du travail*, 2026 edition, file 1, figure 1).

</details>

These movements do not stem from the labour market alone: Insee links part of them to registration rules and to the redesign of the survey, marked on the figure. To judge a promise, the starting date is set before looking at the data, never afterwards; that is why the figure cuts out no term of office.

## Has the rule stayed the same? Changes in opposite directions {#regle-de-mesure}

No, and not only in 2025. For registrants, the counting rule has changed several times since 2022. The register is kept by France Travail; the series are produced with the Dares, "{{< mes-val "cit_dares_ssm" >}}" according to Insee (that of the labour ministry), which itself dates these breaks, and quantifies several of them, in its publications. Here is the effect of each on category A, as the source describes it:

| Date | What changes | Effect on category A, according to the source |
|---|---|---|
| 2022 | New monthly updating form, which records hours worked better | **Down**: about {{< mes-val "rupture_2022" >}} registrants, mostly reclassified into categories B and C (Dares) |
| October-November 2024 | Form changed again | **Up**: about {{< mes-val "formulaire_2024" >}} registrants (Dares and France Travail) |
| January 2025 | Automatic registration of the groups covered by the full employment act (RSA, young people in programmes, disabled people) | **Up**: the 2025 rise partly results from it (Insee) |
| January-March 2025 | Automatic updating of new registrants without entitlement to a France Travail allowance | **Up** in the first quarter (Dares) |
| April 2025 | Automatic updating restricted to first-time registrations | **Down** in the second quarter (Dares) |
| June 2025 | New sanctions regime | Fewer removals from the register (Dares, Insee) |

The updating form, by which registrants declare their activity each month, is France Travail's, according to Insee; the documents read do not say who decided its changes of 2022 and 2024. Automatic registration comes from the full employment act of 18 December 2023, passed by Parliament. On the survey side, the ILO unemployment series was rebuilt after the redesign of the Labour Force Survey in 2021.

<details class="repli"><summary>What the sources say, date by date</summary>

- **2019-2021.** The unemployment insurance reform, applied from November 2019 to December 2021, includes, according to Insee, "{{< mes-val "cit_2019" >}}".
- **2021.** The Labour Force Survey is redesigned; for ILO status, "{{< mes-val "cit_2021" >}}" (Insee). The ILO unemployment series is therefore rebuilt as well.
- **2022.** A new monthly updating form, which records hours worked better, has, according to the Dares, "{{< mes-val "cit_2022" >}}": it estimates it at about {{< mes-val "rupture_2022" >}} fewer registrants in category A between January and November 2022, mostly reclassified into categories B and C.
- **October-November 2024.** The form changes again, this time upwards: "{{< mes-val "cit_2024" >}}", by about {{< mes-val "formulaire_2024" >}} people at national level in the fourth quarter of 2024 (Dares and France Travail, quarterly publication reproduced by the regional labour directorate of Normandy).
- **January 2025.** The full employment act of 18 December 2023 provides for automatic registration. According to the Dares, applicants for and recipients of the RSA (minimum income), young people followed by local youth employment services (missions locales) in a youth commitment contract (CEJ) or a contractual support pathway (Pacea), and disabled people followed by Cap emploi, the specialised support network, are now registered systematically; for people already on the RSA, their direction to a support track is gradual. Two new categories, F and G, take in people directed to a social pathway and those awaiting orientation.
- **January to April 2025.** From January to March, new registrants without benefit entitlement are updated automatically, and therefore counted in category A until they sign their commitment contract; the rule is restricted in April to first-time registrations. In March, an incident wrongly counts {{< mes-val "incident_2025" >}} people in category A, reclassified into category G in April (Dares).
- **Since June 2025.** A decree changes the sanctions regime: a "suspension-remobilisation" now precedes any removal from the register, which reduces the number of removals (Dares, Insee).

</details>

The Dares also publishes a series of category A registrants **excluding RSA recipients and young people in programmes**, available since 2018. It removes the groups covered by the law; it does not remove the other changes.

{{< figure-svg fichier="mesurer-regle-en" alt="Two panels on the same scale, from 2018 to 2026: on the left published category A, on the right the series excluding RSA recipients and young people in programmes. A grey band marks 2022, the year of the new monthly updating form; a dotted line marks 1 January 2025. Both series rise in the first quarter of 2025 and fall back in the second." >}}Category A registrants at France Travail, quarterly average of end-of-month registrants, France excluding Mayotte, seasonally and working-day adjusted, with and without RSA recipients and young people in programmes. Latest point: {{< mes-val "dares_fin" >}}. These levels cannot be compared directly with those of the 2024 cross-tabulation, which covers a different scope.{{< /figure-svg >}}

{{< fig-actions id="regle" >}}

**The series excluding RSA also carries the 2025 break.** In the first quarter of 2025, it jumps ({{< mes-val "dares_hors_t1_2025" >}}, against {{< mes-val "dares_a_t1_2025" >}} for the published series). In the second, it falls back ({{< mes-val "dares_hors_t2_2025" >}}, against {{< mes-val "dares_a_t2_2025" >}}). This is the signature of the automatic updating from January to March 2025, which applied to all new registrants without entitlement to a France Travail allowance, not only to the groups covered by the law. And the starting point of the comparison, the fourth quarter of 2024, already carries the form changed in October-November 2024.

Over the whole period, between the fourth quarter of 2024 and the {{< mes-val "dares_fin" >}}, published category A has {{< mes-val "dares_a_var" >}} more registrants. The series excluding RSA has {{< mes-val "dares_a_hors_var" >}} more.

<details class="repli"><summary>The levels of the two series</summary>

| | Fourth quarter of 2024 | Latest point ({{< mes-val "dares_fin" >}}) | Change |
|---|---|---|---|
| Published category A | {{< mes-val "dares_a_2024t4" >}} | {{< mes-val "dares_a_fin" >}} | {{< mes-val "dares_a_var" >}} more |
| Excluding RSA recipients and young people in programmes | {{< mes-val "dares_a_hors_2024t4" >}} | {{< mes-val "dares_a_hors_fin" >}} | {{< mes-val "dares_a_hors_var" >}} more |

The cross-tabulation is a 2024 annual average for people aged 15-64 living in ordinary households; the Dares series are averages, over each quarter, of the registrants counted at the end of each month, on a different scope.

</details>

The two series describe **two different populations**: their gap is not the effect of the reform, and a small gap would not prove a small effect. Neither is an intact witness of what would have happened without the law.

These series have not carried a statistical quality label since 1 January 2025. On 14 November 2024, the [French Official Statistics Authority](https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/11/Delibere-ASP-statistiques-marche-du-travail_14nov2024_VF.pdf) (Autorité de la statistique publique), which certifies the quality of public statistics, suspended their label for the time it still had to run. Its reason: the 2025 changes affect both the number of registrants and their categories, "{{< mes-val "cit_asp" >}}". It asks the Dares and France Travail for clear and educational communication to avoid misinterpretations; its decision calls into question neither the published figures nor the way they are produced.

<details class="repli"><summary>The Authority’s decision, in quotations</summary>

The label of the registrant series "{{< mes-val "cit_asp_2021" >}}". The decision of 14 November 2024 is to suspend "{{< mes-val "cit_asp_suspend" >}}". The Authority also asks for published monitoring of reclassifications between categories, and has since kept to regular monitoring, "{{< mes-val "cit_asp_attente" >}}". On 28 July 2026, the Dares metadata still state that the Authority "{{< mes-val "cit_dares_label" >}}". The stated reason concerns the stability and interpretation of the series while the law is being phased in.

</details>

## What share can be attributed? Contribution, effect, and what the sources say {#quelle-part}

On the ILO measure, Insee quantified the share of the groups targeted by the law in the rise in unemployment: "{{< mes-val "cit_ir192" >}}" (*Informations rapides* No. 192, 7 August 2026). Insee attaches two caveats to this figure: "{{< mes-val "cit_ir192_prudence" >}}", and "{{< mes-val "cit_ir192_reserve" >}}". This figure covers France including Mayotte, whereas the cross-tabulation and the Dares series cover France excluding Mayotte.

**An accounting contribution is neither an effect of the law nor proof that there was no effect.** It says what share of the rise is found among these groups; it does not say what caused it, nor what unemployment would have been without the law.

In its review of 2025, Insee devotes a box to the law, headed "{{< mes-val "cit_ve_titre" >}}". The heading speaks of effects; the figures presented remain contributions.

<details class="repli"><summary>What the Insee box says</summary>

In this box (*Emploi, chômage, revenus du travail*, 2026 edition, overview, box 5), Insee describes a mechanism: "{{< mes-val "cit_ve_recherche" >}}"; this more frequent search is, according to Insee, part of the rise in their activity rate, whose corollary is the rise in their unemployment rate. It reports "{{< mes-val "cit_ve_contrib" >}}", and recalls the limits of any survey-based measure: "{{< mes-val "cit_ve_limites" >}}".

</details>

Unédic, the joint body that runs unemployment insurance, repeats Insee's figure, writing that "{{< mes-val "cit_unedic" >}}", while quoting its caveats: the verb "explain" lends the contribution an explanatory power that the measurement does not establish. Neither Insee nor Unédic measures what unemployment would have been without the law; saying so either way requires an evaluation that these publications do not yet contain.

## Judging a promise: the four questions {#juger-une-promesse}

A promise to reduce unemployment, taken as an example and aimed at no one, is judged with four questions, which are the last four of the book's grid:

1. **By which indicator?** ILO unemployment or category A registrants: in 2024, only {{< mes-val "p_a" >}}% of the latter are counted in the former, and one cannot be swapped for the other along the way.
2. **Against which point of comparison?** A date and a value stated in advance: the gap between the two measures went from {{< mes-val "ecart_2020" >}} in 2020 to {{< mes-val "ecart_2024" >}} in 2024, so the choice of starting year can change the diagnosis.
3. **Has the rule that will say whether it was kept stayed the same?** For registrants, no: the 2022 form (about {{< mes-val "rupture_2022" >}} fewer registrants in category A), the late-2024 form (about {{< mes-val "formulaire_2024" >}} more), automatic registration and automatic updating in 2025; for ILO unemployment, the survey redesigned in 2021. A before-and-after comparison names these breaks, or changes indicator.
4. **What share of the result can honestly be attributed to whoever made the promise?** A contribution is not an effect; an observed change is not enough either to establish its cause or to rule it out.

## What this page does not say {#limites}

It does not say which of the two measures is the right one: one describes people's situation, the other their registration. It measures the effect of no policy, including the full employment act. The cross-tabulation is an Insee estimate for the 2024 average: it describes neither 2025 nor 2026, which the matching does not cover.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Judging a promise to the end" avis="non" >}}
This page shows that a promise cannot be judged without choosing its indicator and checking its rule. The book applies these questions, and the four that precede them — what exactly is promised, who can decide it, with whose consent, within what time —, to nine written, dated and signed promises, one of them on employment. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Insee**, *Emploi, chômage, revenus du travail* [Employment, unemployment, labour income], Insee Références, 2026 edition (published 2 July 2026): file 1, figures 1, 2 and 8, definitions, boxes and sources (Dares-Insee-France Travail matching of the Historical Statistical File and the Labour Force Survey); overview, box 5. *Informations rapides* No. 192, 7 August 2026 (in French).

**Dares and France Travail**, registrants at France Travail, quarterly stock, France, seasonally and working-day adjusted data, and the dataset's metadata (updated 28 July 2026): procedural changes of 2022 and 2025, categories F and G, series excluding RSA recipients and young people in programmes. October-November 2024 updating form: warning of the fourth-quarter 2024 quarterly publication (regional labour directorate of Normandy, source France Travail-Dares) (in French).

**Autorité de la statistique publique** (French Official Statistics Authority), decision of 14 November 2024 on labour market statistics. **Law** no. 2023-1196 of 18 December 2023 on full employment. **Unédic**, "Comprendre le chômage au sens du BIT" (in French).

**Download the data** (CC BY 4.0 licence): [CSV](/promesses_mesurer.csv), long format; [JSON](/promesses_mesurer.json), with definitions, dated breaks and the record of the checks (field names and some labels in French). An earlier version of this dataset, without the long series, is archived on Zenodo with the six others of the same series and their methods note, under a permanent identifier: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

<details class="repli"><summary>How these figures were checked</summary>

The counts of the cross-tabulation come from the spreadsheet published by Insee; a second extraction, written separately from the published PDF document, finds the same 35 values (24 cells and 11 totals), the same year and the same scope, and the three sets restated by subtraction equal those Insee prints in another table of the same file. The gaps of the long series equal those Insee writes in the text of the file. These checks verify that the page restates exactly what is published; they do not redo the matching, whose individual data are not public.

The figures, quoted passages, checks and charts are produced by a single script, which rereads the files published by Insee, the Dares, the French Official Statistics Authority, Unédic and the regional labour directorate of Normandy, archived on 12 October 2026, and stops if a reread figure no longer meets the conditions on which the main sentences rest; each quoted passage and each number in the timeline is found word for word in these files, and only the dates of the timeline are written into the text. The Dares data are those of the 28 July 2026 update; a later release enters only after a new reading.

</details>

{{< reutiliser figures="figures_mesurer" jeu="promesses_mesurer" sources="Insee and Dares" donnees="The 2024 cross-tabulation of ILO status and registration category (24 cells and totals, in thousands), the quarterly series of category A registrants with and without the groups registered automatically, and the 2012-2025 annual averages of both measures; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
To judge a promise on unemployment in France, one must first choose its figure: in 2024, according to the Insee estimate, only {{< mes-val "p_a" >}}% of category A registrants are unemployed in the ILO sense. One must then check the rule: the counting of registrants changed in 2022 (about {{< mes-val "rupture_2022" >}} fewer registrants in category A), at the end of 2024 (about {{< mes-val "formulaire_2024" >}} more) and in 2025 (automatic registration, automatic updating), and these series have not carried the statistical quality label since 1 January 2025. A contribution is not an effect, and an observed change does not tell its cause.
{{< /reutiliser >}}
