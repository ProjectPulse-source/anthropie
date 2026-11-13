---
title: "Who can cope with an unexpected expense?"
url: /en/who-can-cope-with-an-unexpected-expense/
description: "In France, {imp.total}% of people could not face an unexpected expense ({imp.annee}, Eurostat). The poverty threshold is not the whole story: above it, {imp.ps_dessus}% of people in single-parent households are in this situation, against {imp.c1_dessus}% of people in two-adult households with one child."
chapo: "Is being unable to face an unexpected expense a matter of poverty? Only in part. In France, in {imp.annee}, {imp.dessous}% of people below the poverty threshold are in this situation, and {imp.dessus}% above it. But above the threshold, situations differ sharply by household composition: {imp.ps_dessus}% of people in single-parent households could not face an unexpected expense, against {imp.c1_dessus}% of people in two-adult households with one child."
date: 2026-10-26
lastmod: 2026-11-13
journal:  # révisions qui changent la lecture de la page
  - {date: 2026-11-13, texte: "Correction: the European comparison covers the EU as a whole, France included; “the finding is not specific to France” is replaced by what it establishes."}
  - {date: 2026-11-12, texte: "Revision: the comparison presented for what it can and cannot tell us (two groups, not a household going from two adults to one; other possible differences between these households), instead of a “test”; the one-adult household has one or more children, the two-adult household one child, couple or not; the chart retitled, its note and the share card carry the caveat; the indicator, reported by the household, captures only the financial side of individual fallback capacity."}
  - {date: 2026-11-07, texte: "Correction: the shares are those of people living in each type of household (children included), not of parents or households; the wording, the figures and the share card now say so. Values unchanged."}
  - {date: 2026-11-05, texte: "Correction: the ranges of rates are rounded outwards (lower bound down, upper bound up), so that they contain every value they summarise."}
og_title: "Who can cope with an unexpected expense? — S. Lalut"
og_image: "images/og-imprevu-menages-en.jpg"
og_image_alt: "Share card: “Unexpected expense: being above the poverty threshold is not enough” — share of people who could not face an unexpected expense, above the poverty threshold, in France: two-adult households without children, two-adult households with one child and one-adult households with children (Eurostat, EU-SILC); association, not cause, not at equal income."
donnees: [menages_imprevu]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "menages_imprevu"
  apropos: "households' ability to face an unexpected expense"
  nom: "Inability to face an unexpected expense, by household composition and poverty threshold — France and European Union"
  description: "Share of people whose household could not face an unexpected expense (Eurostat, EU-SILC, dataset ilc_mdes04), by household composition (one or two adults, with or without dependent children) and position relative to the poverty threshold (60% of national median equivalised disposable income), France and EU-27, annual series retrieved through the Eurostat API."
  couverture_temporelle: "2004/{imp.annee}"
  couverture_spatiale: "France; European Union (27)"
  variables:
    - {nom: "People unable to face an unexpected expense", unite: "% of people", description: "by household composition and position relative to the poverty threshold"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table"
  mots: ["unexpected expense", "precautionary savings", "single-parent families", "single parent", "poverty threshold", "EU-SILC", "material deprivation", "inequality", "household composition"]
  fichiers: ["menages_imprevu.csv", "menages_imprevu.json"]
faq:
  - question: "What share of people in France could not face an unexpected expense?"
    answer: "In {imp.annee}, {imp.total}% of people living in France belong to a household that says it could not face, from its own resources, an unexpected expense of €{imp.montant_question} (Eurostat, EU-SILC survey). The share is {imp.dessous}% below the poverty threshold and {imp.dessus}% above it."
  - question: "Are people in single-parent households more often unable to face an unexpected expense, even when they are not poor?"
    answer: "Yes, as an association, not a cause; the gap is wider above the poverty threshold than below it. In France, in {imp.annee}, among people above the threshold, {imp.ps_dessus}% of those in single-parent households (one adult with one or more children) could not face an unexpected expense of €{imp.montant_question}, against {imp.c1_dessus}% of those in two-adult households with one child, a gap of {imp.ecart_enf}. Without children, the gap between one- and two-adult households is only {imp.ecart_sans}. The series does not say whether the gap comes from household composition, from incomes closer to the threshold or from other differences between these households (number and age of children, employment, committed expenses, benefits received)."
  - question: "Where do these figures come from?"
    answer: "From the EU Statistics on Income and Living Conditions survey (EU-SILC), Eurostat dataset ilc_mdes04 (series since 2004 for France and 2010 for the EU-27, up to {imp.annee}), retrieved by a script that stops if a figure no longer meets the conditions on which the page's main sentences depend. Only the amount asked about in the {imp.annee} survey, €{imp.montant_question} in France, is transcribed from an Insee publication. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md"  # fiche de conception (regle 12)
  refonte: "2026-11-12"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["la-societe-du-premier-coup"]
  rang: 40
  nature: "Official data recomputed (Eurostat, EU-SILC)"
reperes:  # three key results under the standfirst, from 600 px wide (partials/reperes-page.html ; règle 17 du site,
  # reprise du style du 13/11/2026, test du premier écran). Same results, periods, caveat and tokens as the French page.
  - ancre: "who"
    fort: "{imp.total}%"
    texte: "of people in France live in a household that says it could not meet an unexpected expense of €{imp.montant_question} from its own resources, in {imp.annee}"
  - ancre: "who"
    fort: "{imp.dessous}%"
    texte: "of people below the poverty threshold could not face the expense, against {imp.dessus}% of those above it, in {imp.annee}"
  - ancre: "test"
    fort: "{imp.ps_dessus}%"
    texte: "of people in single-parent households could not face the expense, against {imp.c1_dessus}% of those in two-adult households with one child, in both cases above the poverty threshold, in {imp.annee}: a gap between two groups, which does not measure what would happen if a household went from two adults to one"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data last updated {{< imp-val "date_donnees" >}}</span> Eurostat, EU-SILC survey, dataset ilc_mdes04: France (series since 2004) and the EU-27 (since 2010); gaps studied from {{< imp-val "debut" >}} to {{< imp-val "annee" >}}. Download: <a href="/menages_imprevu.csv">CSV</a> · <a href="/menages_imprevu.json">JSON</a></p>

## Who could not face an unexpected expense? {#who}

In France, in {{< imp-val "annee" >}}, {{< imp-val "total" >}}% of people live in a household that says it could not meet an unexpected expense of €{{< imp-val "montant_question" >}} from its own resources: nearly three in ten. The gap between people on either side of the poverty threshold is very marked:

<div class="grille-reperes" role="table" aria-label="Share of people whose household could not face an unexpected expense, by position relative to the poverty threshold, France, {{< imp-val "annee" >}}">
<div class="grille-reperes__rang grille-reperes__tete" role="row"><span role="columnheader"></span> <span role="columnheader">below the poverty threshold</span> <span role="columnheader">above the threshold</span></div>
<div class="grille-reperes__rang" role="row"><span role="rowheader">could not face the expense, in {{< imp-val "annee" >}}</span> <span class="grille-reperes__val" role="cell"><b>about two thirds</b> <small>{{< imp-val "dessous" >}}%</small> <span class="barre-part" style="--v:{{< imp-val "dessous" "css" >}}"><i></i></span></span> <span class="grille-reperes__val" role="cell"><b>about one in five</b> <small>{{< imp-val "dessus" >}}%</small> <span class="barre-part" style="--v:{{< imp-val "dessus" "css" >}}"><i></i></span></span></div>
</div>

But being above or below the threshold is not the whole story. Above the threshold, where an income-based classification says "not poor", situations differ sharply by household composition.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/imprevu-menages-en-m.svg" width="300" height="833">
    <img src="/img/imprevu-menages-en.svg" alt="Horizontal bars, France {{< imp-val "annee" >}}, share of people whose household says it could not face an unexpected expense of €{{< imp-val "montant_question" >}}, by the type of household they live in. Above the poverty threshold: two adults without children {{< imp-val "c0_dessus" >}}%, one adult without children {{< imp-val "seul_dessus" >}}%, two adults with one child {{< imp-val "c1_dessus" >}}%, one adult with one or more children {{< imp-val "ps_dessus" >}}%. Below the threshold, in the same order: {{< imp-val "c0_dessous" >}}%, {{< imp-val "seul_dessous" >}}%, {{< imp-val "c1_dessous" >}}% and {{< imp-val "ps_dessous" >}}%. Association, not cause." width="720" height="363" loading="lazy">
  </picture>
  <figcaption>Share of people (not households), as reported by their household; poverty threshold: 60% of national median equivalised disposable income (Eurostat, EU-SILC).</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**The result in one sentence.** In France, in {{< imp-val "annee" >}}, above the poverty threshold, {{< imp-val "ps_dessus" >}}% of people in single-parent households (one adult with one or more children) could not face an unexpected expense of €{{< imp-val "montant_question" >}}, against {{< imp-val "c1_dessus" >}}% of people in two-adult households with one child, a gap of {{< imp-val "ecart_enf" >}}.

</div>
</div>
</div>

## What the comparison can — and cannot — tell us {#test}

Being above the poverty threshold does not guarantee being able to absorb an unexpected expense. Among people above that threshold in France in {{< imp-val "annee" >}}, {{< imp-val "ps_dessus" >}}% of those in a household of one adult with one or more children could not, according to their household, face an expense of €{{< imp-val "montant_question" >}}, against {{< imp-val "c1_dessus" >}}% of those in two-adult households with one child. The gap is {{< imp-val "ecart_enf" >}}.

It describes two groups: it does not measure what would happen to a person if their household went from two adults to one. These groups may also differ in their exact income above the threshold, the number and age of children, employment, committed expenses and the benefits they receive. The data published here cannot tell these explanations apart. Above the threshold, the series allows other comparisons:

- **With children**, the gap between households of one adult with one or more children and two-adult households with one child has stayed between {{< imp-val "plage_enf_bas" >}} and {{< imp-val "plage_enf_haut" >}} points every year since {{< imp-val "debut" >}}.
- **Without children**, the gap between one- and two-adult households is only {{< imp-val "ecart_sans" >}} in {{< imp-val "annee" >}} (between {{< imp-val "plage_sans_bas" >}} and {{< imp-val "plage_sans_haut" >}} points each year over the same period).
- **Compared with two-adult households with two children**, the gap for households of one adult with one or more children is still {{< imp-val "ecart_enf2" >}} in {{< imp-val "annee" >}}. The comparison does not, however, measure the effect of the number of children: the Eurostat category this page calls a single-parent household covers any household of one adult with one or more dependent children (under 18, or aged 18 to 24 if economically inactive and living with a parent), and the two-adult category any household of two adults, whether or not they are a couple.

Above the threshold, the gap between one- and two-adult households is thus two to three times as wide with children as without. It has persisted every year since {{< imp-val "debut" >}}, but it does not isolate the effect of household composition itself: the number and age of children, employment, committed expenses and the benefits received may also differ between these households.

Below the threshold, the gap between single-parent households and two-adult households with one child is smaller ({{< imp-val "ecart_enf_dessous" >}} in {{< imp-val "annee" >}}): in both, a large majority of people could not face an unexpected expense. Being above or below the threshold is therefore not enough to explain these gaps.

**What the comparison does not settle.** Above the threshold, single-parent households might on average sit closer to the threshold than two-adult households with one child. The Eurostat dataset does not show how far each household's income lies above the threshold, so it cannot tell how much of the gap goes with household composition and how much with that distance.

## The same finding across the European Union {#europe}

In the EU-27, {{< imp-val "ue_total" >}}% of people could not face an unexpected expense in {{< imp-val "annee" >}}. Above the poverty threshold, the gap between households of one adult with one or more children and two-adult households with one child is {{< imp-val "ue_ecart_enf" >}} (between {{< imp-val "ue_plage_enf_bas" >}} and {{< imp-val "ue_plage_enf_haut" >}} points every year since {{< imp-val "debut" >}}), against {{< imp-val "ue_ecart_sans" >}} between one- and two-adult households without children (between {{< imp-val "ue_plage_sans_bas" >}} and {{< imp-val "ue_plage_sans_haut" >}} points). For the EU as a whole, France included, the gap is likewise wider with children than without.

## What these data do not say {#limits}

- **A statement, not a bank balance.** The question asks whether the household could pay an unexpected expense without outside help or new borrowing; it measures neither savings nor available assets.
- **An amount below the one set by the common rule.** In France, the {{< imp-val "annee" >}} survey asks about an expense of €{{< imp-val "montant_question" >}} (Insee). Eurostat's guidelines set this amount, country by country, at one twelfth of the poverty threshold taken from the survey two years earlier, rounded to within 5%: about €{{< imp-val "douzieme" >}} for France in {{< imp-val "annee" >}}, based on the {{< imp-val "annee_seuil" >}} threshold. The French question therefore asks about a smaller sum, which matters when the French share is compared with that of other countries. It does not bias comparisons between French households in a given year, since they all answer the same question; but the size of the gaps may depend on the amount asked, which may have changed from one year to the next.
- **People, not households.** Shares are computed over people: a child in a household that could not face the expense is counted among the people concerned.
- **The poverty threshold is relative.** It is 60% of national median equivalised disposable income, after social transfers; it accounts for household size and composition, not for the reserve the household holds.
- **An association, not a cause.** The chart shows that household composition and inability to face an unexpected expense go together, not that one produces the other; how far incomes lie from the threshold is not taken into account.
- **Margin of error not published.** Eurostat publishes no confidence intervals for these subgroups; none of the values used carries Eurostat's "low reliability" flag, but EU values before 2019 are flagged as estimated. The absence of that flag does not make a gap of a few tenths of a point significant: the page comments only on gaps of several points, without being able to say, for lack of published intervals, how large a gap between these small groups must be to be reliable.
- **Breaks in series.** Eurostat flags breaks in the French series in {{< imp-val "ruptures_fr" >}}: multi-year ranges should be read with caution. The main finding compares household types in the same year, and these breaks do not affect it.

<aside class="encadre">

**The author's hypothesis, not tested here.** In the working paper [AWP-08](/en/awp/awp-08/), the economist Stéphane Lalut proposes reading individual fallback capacity as one of the three components of what he calls [social reversibility](/en/social-reversibility/): what a person can afford to fail at without durably closing off their future. The indicator on this page, based on what the household reports, captures only the financial side of that capacity; it says nothing about the cost of a failure or the possibility of trying again.

</aside>

Further reading: [*La Société du premier coup*](/livres/la-societe-du-premier-coup/) (**in French**) shows, through concrete cases, what a failure costs depending on the social position of the person who suffers it, and why some cannot afford to try.

## Frequently asked questions {#faq}

{{< faq-visible >}}

## Sources {#sources}

- Eurostat, European Union Statistics on Income and Living Conditions (EU-SILC), dataset [ilc_mdes04](https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table) ("Inability to face unexpected financial expenses"), retrieved through the dissemination API. Author's calculations: gaps between household compositions, ranges of the annual gaps.
- Amount asked in the survey: Insee, press release of [31 January 2025](https://www.insee.fr/fr/information/8348643) launching the SRCV survey, the French part of EU-SILC (French wording, translated: "Are you able to face an unexpected expense of 1,000 euros?"); common rule: Eurostat, *EU-SILC Methodological guidelines, 2025 operation*, variable HS060, p. 154; poverty threshold for a single person: Eurostat, dataset [ilc_li01](https://ec.europa.eu/eurostat/databrowser/view/ilc_li01/default/table), retrieved by the script.

{{< reutiliser figures="figures_imprevu" jeu="menages_imprevu" sources="Eurostat (EU-SILC)" donnees="The share of people unable to face an unexpected expense, for France and the EU-27, by household composition and position relative to the poverty threshold, every year since 2004 for France and 2010 for the EU-27; the same content is available as CSV, in long format, with Eurostat's flags (statut_eurostat column: e, estimated value; b, break in series)." >}}
In France, in {{< imp-val "annee" >}}, above the poverty threshold, the share of people whose household says it could not face an unexpected expense of €{{< imp-val "montant_question" >}} is more than twice as high among people in single-parent households as among people in two-adult households with one child. Above the threshold, every year since {{< imp-val "debut" >}}, the gap between one- and two-adult households has been two to three times as wide with children as without; this is an association, not a measured effect of household composition. Being above the poverty threshold therefore does not tell the whole story about being able to face an unexpected expense.
{{< /reutiliser >}}
