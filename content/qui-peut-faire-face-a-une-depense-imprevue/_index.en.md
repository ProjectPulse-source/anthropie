---
title: "Who can cope with an unexpected expense?"
url: /en/who-can-cope-with-an-unexpected-expense/
description: "In France, {imp.total}% of people could not face an unexpected expense ({imp.annee}, Eurostat). Income is not the whole story: above the poverty threshold, {imp.ps_dessus}% of single parents are in this situation, against {imp.c1_dessus}% of couples with one child."
chapo: "Is being unable to face an unexpected expense a matter of poverty? Only in part. In France, in {imp.annee}, {imp.dessous}% of people below the poverty threshold are in this situation, and {imp.dessus}% above it. But above the threshold, household composition changes everything: {imp.ps_dessus}% of single parents could not face an unexpected expense, against {imp.c1_dessus}% of couples with one child."
date: 2026-10-26
lastmod: 2026-10-26
og_title: "Who can cope with an unexpected expense? — S. Lalut"
og_image: "images/og-imprevu-menages-en.jpg"
og_image_alt: "Share card: “Income is not the whole story” — share of people who could not face an unexpected expense, above the poverty threshold: single parents and couples with one child, France (Eurostat, EU-SILC)."
donnees: [menages_imprevu]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; tokens resolved at build
  jeu: "menages_imprevu"
  nom: "Inability to face an unexpected expense, by household composition and poverty threshold — France and European Union"
  description: "Share of people whose household could not face an unexpected expense (Eurostat, EU-SILC, dataset ilc_mdes04), by household composition (couple or single adult, with or without children) and position relative to the poverty threshold (60% of median equivalised income), France and EU-27, annual series retrieved through the Eurostat API."
  couverture_temporelle: "2003/{imp.annee}"
  couverture_spatiale: "France; European Union (27)"
  variables:
    - {nom: "People unable to face an unexpected expense", unite: "% of people", description: "by household composition and position relative to the poverty threshold"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table"
  mots: ["unexpected expense", "precautionary savings", "single-parent families", "single parent", "poverty threshold", "EU-SILC", "material deprivation", "inequality", "household composition"]
  fichiers: ["menages_imprevu.csv", "menages_imprevu.json"]
faq:
  - question: "What share of people in France could not face an unexpected expense?"
    answer: "In {imp.annee}, {imp.total}% of people living in France say their household could not face an unexpected expense (Eurostat, EU-SILC survey). The share reaches {imp.dessous}% below the poverty threshold and {imp.dessus}% above it."
  - question: "Are single parents more exposed, even when they are not poor?"
    answer: "Yes, and the gap is widest above the poverty threshold: in {imp.annee}, {imp.ps_dessus}% of single parents above the threshold could not face an unexpected expense, against {imp.c1_dessus}% of couples with one child, a gap of {imp.ecart_enf}. Without children, the same move from two adults to one adds only {imp.ecart_sans}. This is an association: the series does not say whether the gap comes from household composition or from a lower position within the income band."
  - question: "Where do these figures come from?"
    answer: "From the European survey on income and living conditions (EU-SILC), Eurostat dataset ilc_mdes04 (series from 2003 to {imp.annee}), retrieved by a script that stops if a figure no longer meets the conditions on which the page's main sentences depend. Only the amount of the question, €{imp.montant_question} in France, is transcribed from an Insee publication, and checked for each survey year cited. The data can be downloaded as CSV and JSON, under a CC BY 4.0 licence."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md"  # fiche de conception (regle 12)
  refonte: "2026-10-26"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["la-societe-du-premier-coup"]
  rang: 40
  nature: "Official data recomputed (Eurostat, EU-SILC)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data as of: {{< imp-val "date_donnees" >}}</span> Eurostat, EU-SILC survey, dataset ilc_mdes04: France and the EU-27, full series since the start of the survey; gaps studied from {{< imp-val "debut" >}} to {{< imp-val "annee" >}}. Download: <a href="/menages_imprevu.csv">CSV</a> · <a href="/menages_imprevu.json">JSON</a></p>

## Who could not face an unexpected expense? {#who}

In France, in {{< imp-val "annee" >}}, {{< imp-val "total" >}}% of people live in a household that, by its own account, could not meet an unexpected expense of €{{< imp-val "montant_question" >}} from its own resources: nearly three in ten. Income weighs heavily. Below the poverty threshold the share reaches {{< imp-val "dessous" >}}%, about two thirds; above it, {{< imp-val "dessus" >}}%, about one in five.

But income is not the whole story. Above the threshold, where an income-based classification says "not poor", household composition sharply separates situations.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/imprevu-menages-en-m.svg" width="300" height="693">
    <img src="/img/imprevu-menages-en.svg" alt="Horizontal bars, France {{< imp-val "annee" >}}, share of people who could not face an unexpected expense. Above the poverty threshold: couple without children {{< imp-val "c0_dessus" >}}%, single adult {{< imp-val "seul_dessus" >}}%, couple with one child {{< imp-val "c1_dessus" >}}%, single parent {{< imp-val "ps_dessus" >}}%. Below the threshold: {{< imp-val "c0_dessous" >}}%, {{< imp-val "seul_dessous" >}}%, {{< imp-val "c1_dessous" >}}% and {{< imp-val "ps_dessous" >}}%." width="720" height="335" loading="lazy">
  </picture>
  <figcaption>Share of people (not households), self-reported; poverty threshold: 60% of median equivalised income (Eurostat, EU-SILC).</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** In France, in {{< imp-val "annee" >}}, above the poverty threshold, {{< imp-val "ps_dessus" >}}% of single parents could not face an unexpected expense, against {{< imp-val "c1_dessus" >}}% of couples with one child, a gap of {{< imp-val "ecart_enf" >}}.

</div>

## Two explanations, one test {#test}

One might think that everything turns on income: being above or below the poverty threshold. If so, two households on the same side of the threshold should show similar shares. The test compares households that differ first of all in one thing: one adult more or less.

- **With one child**, moving from two adults to one adds {{< imp-val "ecart_enf" >}} above the threshold in {{< imp-val "annee" >}}, and between {{< imp-val "plage_enf_bas" >}} and {{< imp-val "plage_enf_haut" >}} points every year since {{< imp-val "debut" >}}.
- **Without children**, the same move adds only {{< imp-val "ecart_sans" >}} (between {{< imp-val "plage_sans_bas" >}} and {{< imp-val "plage_sans_haut" >}} points over the same period).
- **The number of children is not enough to explain the gap.** The statistics count as a "single parent" any single adult with one child or more; against couples with two children, the gap remains {{< imp-val "ecart_enf2" >}}.

Above the threshold, the gap between one- and two-adult households is thus two to three times larger with children than without. It persists throughout the series, but it does not isolate the effect of household composition itself: the number and age of children, employment, social transfers and expenses may also differ between these households. Below it, the gap narrows ({{< imp-val "ecart_enf_dessous" >}} in {{< imp-val "annee" >}}): single parents and couples with one child are both exposed in a large majority. Being above or below the threshold is therefore not enough to explain these gaps.

**What the test does not settle.** A third explanation remains possible: above the threshold, single parents might on average sit closer to the threshold than couples with one child. The Eurostat dataset does not detail position within the income band, so it cannot separate what household composition weighs from what that position weighs.

## The same finding across the European Union {#europe}

In the EU-27, {{< imp-val "ue_total" >}}% of people could not face an unexpected expense in {{< imp-val "annee" >}}. Above the poverty threshold, moving from two adults to one adds {{< imp-val "ue_ecart_enf" >}} with one child (between {{< imp-val "ue_plage_enf_bas" >}} and {{< imp-val "ue_plage_enf_haut" >}} points since {{< imp-val "debut" >}}), against {{< imp-val "ue_ecart_sans" >}} without children (between {{< imp-val "ue_plage_sans_bas" >}} and {{< imp-val "ue_plage_sans_haut" >}}). The finding is not specific to France.

## What these data do not say {#limits}

- **A statement, not a bank balance.** The question asks whether the household could pay an unexpected expense without outside help or new borrowing; it measures neither savings nor available assets.
- **An amount below the common rule.** In France, the {{< imp-val "annee" >}} survey asks about an expense of €{{< imp-val "montant_question" >}} (Insee). Eurostat's guidelines set this amount, country by country, at one twelfth of the poverty threshold taken from the survey two years earlier, rounded to within 5%: about €{{< imp-val "douzieme" >}} for France in {{< imp-val "annee" >}}, on the {{< imp-val "annee_seuil" >}} threshold. The French question therefore tests a smaller sum, which matters when its level is compared with other countries; it does not affect the comparison between French households, who all answer the same question.
- **People, not households.** Shares are computed over people: a child in an exposed household counts as exposed.
- **The poverty threshold is relative.** It is 60% of median equivalised income; it accounts for household size, not for the reserve the household holds.
- **An association, not a cause.** The chart shows that household composition and vulnerability to a shock go together, not that one produces the other; position within the income band is not controlled.
- **Precision not published.** Eurostat publishes no confidence intervals for these subgroups; none of the values used is flagged by Eurostat as of low reliability. That flag does not make a gap of a few tenths of a point significant: the page comments only on gaps of several points.
- **Breaks in series.** Eurostat flags breaks in France in {{< imp-val "ruptures_fr" >}}: multi-year ranges should be read with caution. The main finding compares households in the same year, and the break does not affect it.

<aside class="encadre">

**A hypothesis of the author, not tested here.** In the working paper [AWP-08](/en/awp/awp-08/), the economist Stéphane Lalut proposes reading financial fallback capacity as one of the three components of what the author calls [social reversibility](/en/social-reversibility/): what a person can afford to fail without durably closing their future. The indicator on this page measures only part of it; it says nothing about the cost of a failure or the possibility of trying again.

</aside>

To go further: [*La Société du premier coup*](/livres/la-societe-du-premier-coup/) (**in French**) tells, through concrete cases, what a failure costs depending on the social position of the person who suffers it, and why some cannot afford to try.

## Sources {#sources}

- Eurostat, European Union Statistics on Income and Living Conditions (EU-SILC), dataset [ilc_mdes04](https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table) ("Inability to face unexpected financial expenses"), retrieved through the dissemination API. Author's calculations: gaps between household compositions, annual ranges.
- Amount of the question: Insee, press release launching the SRCV survey, [31 January 2025](https://www.insee.fr/fr/information/8348643) (in French: "are you able to face an unexpected expense of 1,000 euros?"); common rule: Eurostat, *EU-SILC Methodological guidelines, 2025 operation*, variable HS060, p. 154; poverty threshold for a single person: Eurostat, dataset [ilc_li01](https://ec.europa.eu/eurostat/databrowser/view/ilc_li01/default/table), retrieved by the script.

{{< reutiliser figures="figures_imprevu" jeu="menages_imprevu" sources="Eurostat (EU-SILC)" donnees="The share of people unable to face an unexpected expense, for France and the EU-27, by household composition and position relative to the poverty threshold, every year since the start of the survey; the same content is available as CSV, in long format, with Eurostat's flags." >}}
Above the poverty threshold, the share of people unable to face an unexpected expense is more than twice as high among single parents as among couples with one child. When there are children, the gap between one- and two-adult households is two to three times larger than without children; this is an association, not an isolated effect. Relative income therefore does not tell the whole story about coping with a shock.
{{< /reutiliser >}}
