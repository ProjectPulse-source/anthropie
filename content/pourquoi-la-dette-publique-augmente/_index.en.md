---
title: "Why does French public debt rise?"
url: /en/why-does-public-debt-rise/
description: "French public debt doubled in thirty years. Interest and growth almost cancelled out: the rise comes mostly from primary deficits. A Eurostat decomposition."
chapo: "From {dyn.dette_depart}% to {dyn.dette_fin}% of GDP between {dyn.annee_depart} and {dyn.annee_fin}: French public debt doubled. Interest pushed it up by {dyn.effet_interets} points, and nominal GDP growth held it back by almost as much; what remains, in this accounting decomposition, is primary deficits, excluding interest: {dyn.deficits_primaires} points of a net rise of {dyn.hausse}, or {dyn.part_deficits}%."
og_title: "Why does French public debt rise?"
og_image: "images/og-dette-dynamique-en.jpg"
og_image_alt: "Share card: “Why the debt doubled” — waterfall of French public debt in points of GDP, 1995 to 2025: interest, nominal growth, primary deficits, stock-flow adjustments."
date: 2026-09-30
lastmod: 2026-09-30
# English version of part 1 of the public debt dossier (FR: content/pourquoi-la-dette-publique-augmente/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/dette_dynamique.json.
donnees: [dette_dynamique]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_dynamique"
  nom: "Why French public debt rises: a decomposition of the change in the debt-to-GDP ratio"
  description: "Annual decomposition, from {dyn.annee_depart} to {dyn.annee_fin}, of the change in the debt-to-GDP ratio of French general government into the interest effect, the nominal growth effect, the primary balance and stock-flow adjustments; the residual is checked against a second accounting identity. Eurostat series, no value entered by hand."
  couverture_temporelle: "{dyn.annee_depart}/{dyn.annee_fin}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Change in the debt-to-GDP ratio", unite: "points of GDP"}
    - {nom: "Interest effect", unite: "points of GDP"}
    - {nom: "Nominal growth effect", unite: "points of GDP"}
    - {nom: "Contribution of the primary balance", unite: "points of GDP", description: "deficit excluding interest; negative in case of a surplus"}
    - {nom: "Stock-flow adjustments", unite: "points of GDP"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table?lang=fr"
  mots: ["public debt", "France", "primary deficit", "snowball effect", "implicit interest rate", "nominal growth", "Eurostat"]
  fichiers: ["dette_dynamique.csv", "dette_dynamique.json"]
faq:
  - question: "Why does French public debt rise?"
    answer: "Over {dyn.annee_depart}-{dyn.annee_fin}, the debt-to-GDP ratio went from {dyn.dette_depart}% to {dyn.dette_fin}%. Decomposing its change year by year, interest pushed it up by {dyn.effet_interets} points and nominal GDP growth held it back by {dyn.effet_croissance}: their net effect is only {dyn.effet_net} points. The rise comes mostly from primary deficits, the gap between public spending and revenue excluding interest ({dyn.deficits_primaires} points), and for the rest from stock-flow adjustments ({dyn.flux_stock}). This is an accounting decomposition: it identifies which accounting components contributed to the increase, not why the deficits existed."
  - question: "Does interest make the debt rise?"
    answer: "All else equal, yes: it adds to the borrowing requirement. But over thirty years nominal GDP growth almost offset it: its accounting contribution is {dyn.effet_interets} points, against {dyn.effet_croissance} points of reduction due to nominal growth. That balance depends on the gap between the implicit interest rate on the debt and nominal growth: in {dyn.annee_fin} the two were almost equal ({dyn.taux_implicite_dernier}% and {dyn.croissance_derniere}%)."
  - question: "Does inflation reduce the debt?"
    answer: "It can reduce the ratio, by increasing nominal GDP faster than the interest bill. From 2021 to 2023, nominal growth — inflation included — produced an interest-growth effect of −{dyn.effet_2021_2023} points, while primary deficits added {dyn.deficits_2021_2023}; this decomposition does not separate the share of inflation from that of real growth. This is not costless: it reduces the real value of nominal claims, and that loss is borne by someone."
  - question: "Is a primary deficit a sign of too much spending?"
    answer: "Not necessarily: it is a gap between spending and revenue excluding interest, which can come from rising spending, falling revenue, or a recession that does both at once. These data measure the gap; they do not say which of its two terms should be corrected."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 5
  nature: "Official series (Eurostat) decomposed, and the author's calculations"
---

{{< dossier-dette volet="hausse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Updated: {{< dyn-val "date_donnees" >}}</span> France, general government, Eurostat series from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}. Download: <a href="/dette_dynamique.csv">CSV</a> · <a href="/dette_dynamique.json">JSON</a> · <a href="#sources">method</a></p>

France is a telling case for a question every indebted country faces. Its debt ratio doubled in thirty years, and Eurostat's harmonised series allow that rise to be split, year by year, into the terms of a standard accounting identity. The accounting identity is general; the estimates below are for France.

## Where the rise comes from {#cascade}

<figure class="figure-ciseau">
  <img src="/img/dette-dynamique-cascade-en.svg" alt="Waterfall in points of GDP: French debt starts at {{< dyn-val "dette_depart" >}}% at the end of {{< dyn-val "annee_depart" >}}; interest would have pushed it up by {{< dyn-val "effet_interets" >}} points, nominal GDP growth takes away {{< dyn-val "effet_croissance" >}}; primary deficits add {{< dyn-val "deficits_primaires" >}} points and stock-flow adjustments {{< dyn-val "flux_stock" >}}; the debt reaches {{< dyn-val "dette_fin" >}}% at the end of {{< dyn-val "annee_fin" >}}." width="720" height="386" loading="lazy">
  <figcaption>Cumulative decomposition of the change in the debt-to-GDP ratio, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}}, in points of GDP (Eurostat). Blue: the stock; orange: what pushes it up; grey: what pulls it down.</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** Over thirty years, interest and nominal GDP growth almost cancelled out (net effect {{< dyn-val "effet_net" >}} points): the rise in the debt comes mostly from primary deficits, {{< dyn-val "deficits_primaires" >}} points out of {{< dyn-val "hausse" >}}. This is an accounting decomposition: it identifies which accounting components contributed to the increase, not why the deficits existed.

</div>

## One identity, three terms {#identite}

<div class="equation" role="group" aria-label="The change in the debt ratio, decomposed">
  <p class="equation__titre">What moves the debt-to-GDP ratio from one year to the next</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>the interest-growth effect</b><small>interest minus nominal GDP growth</small></span>
    <span class="equation__op" aria-label="plus">+</span>
    <span class="equation__terme"><b>the primary deficit</b><small>spending minus revenue, excluding interest</small></span>
    <span class="equation__op" aria-label="plus">+</span>
    <span class="equation__terme"><b>stock-flow adjustments</b><small>what does not pass through the deficit</small></span>
    <span class="equation__op" aria-label="equals">=</span>
    <span class="equation__terme equation__terme--resultat"><b>the change in the ratio</b><small>in points of GDP</small></span>
  </div>
  <p class="equation__exacte">Exact identity: d<sub>t</sub> − d<sub>t−1</sub> = (i − g) / (1 + g) × d<sub>t−1</sub> − primary balance<sub>t</sub> + stock-flow<sub>t</sub>, where d is the debt-to-GDP ratio, i the implicit interest rate (the year's interest / debt at the end of the previous year) and g nominal GDP growth.</p>
</div>

- **The interest-growth effect.** All else equal, the year's interest adds to the borrowing requirement, and therefore to the debt; but nominal GDP growth — real growth plus inflation — lowers the ratio even without any repayment. The balance of the two is positive when the implicit interest rate exceeds nominal growth, negative in the opposite case.
- **The primary deficit.** The gap between public spending and revenue excluding interest. It does not say whether spending is too high or revenue too low: it measures the gap, not its cause.
- **Stock-flow adjustments.** Debt that moves without passing through the deficit: cash set aside, loans and equity stakes, valuation effects. Here they are obtained as the residual of the identity, then checked against a second accounting identity built on the same series (change in the debt minus the deficit): the two match every year.

## Year by year {#annee-par-annee}

<figure class="figure-ciseau">
  <img src="/img/dette-dynamique-annuelle-en.svg" alt="Stacked bars by year, from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}, in points of GDP: primary deficits in orange, the interest-growth effect in blue, stock-flow adjustments in grey, the change in the ratio as a black dot. Two peaks, 2009 and 2020; a strongly negative interest-growth effect in 2021-2023." width="720" height="356" loading="lazy">
  <figcaption>Annual contributions to the change in the debt-to-GDP ratio, France (Eurostat). The three bars add up to the change, marked by the black dot.</figcaption>
</figure>

Three periods stand out, and the dominant term changes from one to the next.

**{{< dyn-val "p1_lib" >}}: the interest-growth effect.** The ratio gains {{< dyn-val "p1_hausse" >}} points. The implicit interest rate on the debt then exceeds, on average, nominal growth: the interest-growth effect adds {{< dyn-val "p1_taux_croissance" >}} points, while the primary balance, close to equilibrium and sometimes in surplus, contributes {{< dyn-val "p1_deficits" >}}.

**{{< dyn-val "p2_lib" >}}: primary deficits.** The ratio gains {{< dyn-val "p2_hausse" >}} points, of which {{< dyn-val "p2_deficits" >}} come from primary deficits and {{< dyn-val "p2_taux_croissance" >}} from the interest-growth effect. The year 2009 alone accounts for {{< dyn-val "hausse_2009" >}} points: the primary deficit widens and GDP contracts, two effects that coincide with the financial crisis.

**{{< dyn-val "p3_lib" >}}: nominal growth holds back, deficits push.** The ratio gains {{< dyn-val "p3_hausse" >}} points. In 2020 it jumps by {{< dyn-val "hausse_2020" >}} points, with the pandemic. From 2021 to 2023, strong nominal GDP growth, driven in particular by inflation, brings the ratio down: the interest-growth effect takes {{< dyn-val "effet_2021_2023" >}} points off the ratio, more than primary deficits add ({{< dyn-val "deficits_2021_2023" >}}). Since 2024 it has been rising again.

Over the {{< dyn-val "annees_total" >}} years of the series, the primary balance was in surplus only {{< dyn-val "annees_excedent" >}} times. This count describes a recurrence; it does not say whether each of these deficits was desirable, avoidable or cyclical.

## What this decomposition does not say {#limites}

- **An accounting decomposition, not a causal explanation.** It identifies which accounting components moved the debt; it does not say why the deficits existed, or whether they were avoidable.
- **Terms that are not independent.** In a recession, revenue falls and some spending rises: the primary deficit itself depends on growth.
- **Inflation does not reduce the real burden of nominal debt without cost.** It reduces the real value of nominal claims, and that loss is borne by someone: this is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- **Nothing about the future.** What comes next depends on the gap between the implicit interest rate and nominal growth, and on the primary balance. In {{< dyn-val "annee_fin" >}}, the implicit rate ({{< dyn-val "taux_implicite_dernier" >}}%) and nominal growth ({{< dyn-val "croissance_derniere" >}}%) were almost equal: the interest-growth effect was close to zero ({{< dyn-val "net_dernier" >}} points).
- **A series that starts in {{< dyn-val "annee_depart" >}}.** Eurostat's harmonised interest data go back no further; the long-run debt series, since 1978, is in [What does French public debt actually cost?](/en/cost-of-french-public-debt/)

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier** — [What does French public debt actually cost?](/en/cost-of-french-public-debt/) · [Who really pays for public debt?](/en/who-really-pays-public-debt/) · [And elsewhere?](/en/public-debt-international-comparison/)

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page identifies which accounting components contributed to the rise in the debt. It does not say who bears its cost, or through which channels that cost is shifted — onto the taxpayer, onto the saver through inflation, onto public services whose resources are squeezed — depending on the decisions taken to adjust it. The book follows these channels one by one, on official figures, to show in which configurations each group bears a cost. By the end you will have a method for identifying who bears what, depending on the decision taken. The book exists in French only.
{{< /appel-livre >}}

## Where these figures come from {#sources}

Eurostat, general government (S.13), national accounts ESA 2010, in national currency: Maastricht debt (`gov_10dd_edpt1`), interest paid (`gov_10a_main`, D41PAY), net lending or borrowing (B9), nominal GDP (`nama_10_gdp`). The primary balance is the general government balance plus interest paid. Each year, the identity is applied as written above; stock-flow adjustments are the residual, and the script stops if that residual differs from the second accounting identity (change in the debt minus the deficit), computed on the same series. The ratios may differ by a few tenths of a point from first releases (deficit and debt notifications, quarterly accounts), following revisions of the national accounts: this page uses Eurostat's annual series in their latest version. No figure on this page is entered by hand: all come from the same script, re-run with each release of the sources, which also stops if a sentence on the page ceased to be true.

{{< reutiliser figures="figures_dynamique" jeu="dette_dynamique" sources="Eurostat" donnees="The annual decomposition of the change in the debt-to-GDP ratio, France, with its four terms, the implicit interest rate and nominal growth; the same content is available as CSV, one row per year." >}}
This page decomposes the change in the French debt-to-GDP ratio, from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}, into the interest effect, the nominal growth effect, the primary balance and stock-flow adjustments. Over the period, interest and nominal growth almost cancelled out, and the rise comes mostly from primary deficits, excluding interest. This is an accounting decomposition, not a causal attribution: it does not say why the deficits existed.
{{< /reutiliser >}}
