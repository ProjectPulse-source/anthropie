---
title: "Why does French public debt rise?"
url: /en/why-does-public-debt-rise/
description: "French public debt doubled as a share of GDP in thirty years. Interest and growth almost offset each other, in two opposite periods; the rise comes mostly from deficits excluding interest. Spending or revenue: the answer changes with the years compared. A Eurostat decomposition."
chapo: "Between {dyn.annee_depart} and {dyn.annee_fin}, French public debt went from {dyn.dette_depart}% to {dyn.dette_fin}% of GDP: it doubled as a share of the wealth produced. Where do these {dyn.hausse} points of GDP come from? Interest pushes the ratio up, nominal GDP growth pulls it down, and over thirty years the two almost offset each other. Most of the rise comes from public deficits excluding interest, known as primary deficits: {dyn.deficits_primaires} points out of {dyn.hausse}. This balance hides two opposite periods, and it says through which terms the debt rose, not why the deficits existed."
og_title: "Why does French public debt rise?"
og_image: "images/og-dette-dynamique-en.jpg"
og_image_alt: "Share card: “Why the debt doubled” — waterfall of French public debt in points of GDP, 1995 to 2025: interest, nominal growth, primary deficits, stock-flow adjustments."
date: 2026-09-30
lastmod: 2026-10-11
# English version of part 1 of the public debt dossier (FR: content/pourquoi-la-dette-publique-augmente/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/dette_dynamique.json.
# Rewritten on 11/10/2026 with the French page (scenario B+), same structure and same anchors.
donnees: [dette_dynamique]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_dynamique"
  nom: "Why French public debt rises: a decomposition of the change in the debt-to-GDP ratio"
  description: "Annual decomposition, from {dyn.annee_depart} to {dyn.annee_fin}, of the change in the debt-to-GDP ratio of French general government into the interest effect, the nominal growth effect, the primary balance and stock-flow adjustments; spending, revenue and balance as a share of GDP; ratios checked against those published by Eurostat. Eurostat series, no value entered by hand."
  couverture_temporelle: "{dyn.annee_depart}/{dyn.annee_fin}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Change in the debt-to-GDP ratio", unite: "points of GDP"}
    - {nom: "Interest effect", unite: "points of GDP", description: "accounting contribution to the ratio, not an amount paid"}
    - {nom: "Nominal growth effect", unite: "points of GDP"}
    - {nom: "Contribution of the primary balance", unite: "points of GDP", description: "deficit excluding interest; negative in case of a surplus"}
    - {nom: "Stock-flow adjustments", unite: "points of GDP"}
    - {nom: "General government spending, revenue and balance", unite: "% of GDP"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
  mots: ["public debt", "France", "primary deficit", "snowball effect", "implicit interest rate", "nominal growth", "public spending", "public revenue", "Eurostat"]
  fichiers: ["dette_dynamique.csv", "dette_dynamique.json"]
  citation: ["https://doi.org/10.5281/zenodo.23145963"]  # AWP-09 (English edition): method and benchmark of this decomposition
faq:
  - question: "Why does French public debt rise?"
    answer: "Over {dyn.annee_depart}-{dyn.annee_fin}, the debt-to-GDP ratio went from {dyn.dette_depart}% to {dyn.dette_fin}%. Decomposing its change year by year, interest pushed it up by {dyn.effet_interets} points and nominal GDP growth held it back by {dyn.effet_croissance}: their net effect is only {dyn.effet_net} points, but it adds up two opposite periods. The rise comes mostly from primary deficits, the gap between public spending and revenue excluding interest ({dyn.deficits_primaires} points), and for the rest from stock-flow adjustments ({dyn.flux_stock}). This is an accounting decomposition: it identifies which accounting components contributed to the increase, not why the deficits existed."
  - question: "Does interest make the debt rise?"
    answer: "Yes: it is a real charge, which adds to the borrowing requirement. But nominal GDP growth lowers the debt-to-GDP ratio by enlarging its denominator, and over thirty years it almost offset the accounting contribution of interest ({dyn.effet_interets} points, against {dyn.effet_croissance} of reduction). This offset is made of two opposite periods: before {dyn.tc_bascule}, the net effect added {dyn.tc_avant} points to the ratio; since then, it has taken off {dyn.tc_apres}. In {dyn.annee_fin}, on accounts still subject to revision, the implicit interest rate and nominal growth were almost equal ({dyn.taux_implicite_dernier}% and {dyn.croissance_derniere}%)."
  - question: "Does the debt come from too much spending or too little revenue?"
    answer: "These accounts do not settle it: a primary deficit is a gap, which can come from one, the other or both. On Eurostat's series, the diagnosis changes with the years compared: from {dyn.ofce_debut} to {dyn.ofce_fin}, public revenue changes by {dyn.ofce_rec} points of GDP and spending excluding interest by {dyn.ofce_dep_hi}; from {dyn.tresor_debut} to {dyn.tresor_fin}, spending excluding interest by {dyn.tresor_dep_hi} and revenue by {dyn.tresor_rec}; from {dyn.tresor_debut} to {dyn.ofce_fin}, revenue by {dyn.croise_rec} and spending excluding interest by {dyn.croise_dep_hi}. The end year matters as much as the start year."
  - question: "Does inflation reduce the debt?"
    answer: "It can reduce the ratio, by increasing nominal GDP faster than the interest bill. From 2021 to 2023, nominal growth — price rises included — produced an interest-growth effect of −{dyn.effet_2021_2023} points, while primary deficits added {dyn.deficits_2021_2023}; this decomposition does not separate the share of prices from that of real growth. This is not costless: it reduces the real value of nominal claims, and it raises the cost of inflation-linked bonds."
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
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-cascade-en-m.svg" width="300" height="660">
    <img src="/img/dette-dynamique-cascade-en.svg" alt="Waterfall in points of GDP: French debt starts at {{< dyn-val "dette_depart" >}}% at the end of {{< dyn-val "annee_depart" >}}; the interest effect would have pushed it up by {{< dyn-val "effet_interets" >}} points, nominal GDP growth takes away {{< dyn-val "effet_croissance" >}}; primary deficits add {{< dyn-val "deficits_primaires" >}} points and stock-flow adjustments {{< dyn-val "flux_stock" >}}; the debt reaches {{< dyn-val "dette_fin" >}}% at the end of {{< dyn-val "annee_fin" >}}. Cumulative accounting contributions, not amounts paid." width="720" height="413" loading="lazy">
  </picture>
  <figcaption>Cumulative decomposition of the change in the debt-to-GDP ratio, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}}, in points of GDP (Eurostat). Blue: the stock; orange: what pushes it up; grey: what pulls it down.</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** Over thirty years, the net effect of interest and nominal GDP growth is small ({{< dyn-val "effet_net" >}} points), but it adds up two opposite periods, {{< dyn-val "tc_avant" >}} points before {{< dyn-val "tc_bascule" >}} and {{< dyn-val "tc_apres" >}} since: the rise in the debt comes mostly from primary deficits, {{< dyn-val "deficits_primaires" >}} points out of {{< dyn-val "hausse" >}}. This is an accounting decomposition: it identifies which accounting components contributed to the increase, not why the deficits existed.

</div>

**How can interest that is paid "cancel out"?** It does not: it is a real charge, which adds to the borrowing requirement; its effect on the debt also depends on the primary balance and other transactions. But the page measures a ratio, debt relative to the wealth produced in the year, and that wealth grows too. Take a debt equal to GDP and isolate interest, with no other spending or revenue, financing it with new borrowing: if the year's interest raises the debt by one fiftieth and GDP also rises by one fiftieth, the debt has risen in euros, but the ratio has not moved. The interest has not disappeared: it is the growth of the denominator that offsets its effect on the ratio. That is what the {{< dyn-val "effet_interets" >}} points mostly "erased" by growth mean: contributions, cumulated over thirty years, to the change in a ratio, not an amount paid equal to {{< dyn-val "effet_interets" >}}% of GDP. Interest is also recorded when it falls due, not when it is paid: this is the case for the extra amount owed on State bonds whose repayment follows prices. And a primary deficit can come from falling revenue, taxes included, as much as from rising spending: the term designates neither. Who receives this interest and who bears what the debt costs is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/) Totals are computed before rounding: a sum of displayed figures may differ by a tenth from the displayed total.

## Year by year {#annee-par-annee}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-annuelle-en-m.svg" width="300" height="764">
    <img src="/img/dette-dynamique-annuelle-en.svg" alt="Stacked bars by year, from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}, in points of GDP: primary deficits in orange, the interest-growth effect in blue, stock-flow adjustments in grey, the change in the ratio as a black dot. Two peaks, 2009 (+{{< dyn-val "hausse_2009" >}} points) and 2020 (+{{< dyn-val "hausse_2020" >}}); an interest-growth effect of −{{< dyn-val "effet_2021_2023" >}} points in 2021-2023." width="720" height="383" loading="lazy">
  </picture>
  <figcaption>Annual contributions to the change in the debt-to-GDP ratio, France (Eurostat). The three bars add up to the change, marked by the black dot. Here the colours designate terms, not the direction of their effect as in the waterfall.</figcaption>
</figure>

Three periods stand out, and the dominant term changes from one to the next. The {{< dyn-val "tc_bascule" >}} turning point, which splits the series in two for the interest-growth effect, falls within the second.

**{{< dyn-val "p1_lib" >}}: the interest-growth effect.** The ratio gains {{< dyn-val "p1_hausse" >}} points. The implicit interest rate on the debt, that is, the average rate the whole debt costs, then exceeds, on average, nominal growth: the interest-growth effect adds {{< dyn-val "p1_taux_croissance" >}} points, while the primary balance, close to equilibrium and sometimes in surplus, contributes {{< dyn-val "p1_deficits" >}}.

**{{< dyn-val "p2_lib" >}}: primary deficits.** The ratio gains {{< dyn-val "p2_hausse" >}} points, of which {{< dyn-val "p2_deficits" >}} come from primary deficits and {{< dyn-val "p2_taux_croissance" >}} from the interest-growth effect. The year 2009 alone accounts for {{< dyn-val "hausse_2009" >}} points: the primary deficit widens and GDP contracts, two effects that coincide with the financial crisis.

**{{< dyn-val "p3_lib" >}}: nominal growth holds back, deficits push.** The ratio gains {{< dyn-val "p3_hausse" >}} points. In 2020 it jumps by {{< dyn-val "hausse_2020" >}} points, with the pandemic. From 2021 to 2023, strong nominal GDP growth, price rises included, brings the ratio down: the interest-growth effect takes {{< dyn-val "effet_2021_2023" >}} points off the ratio, more than primary deficits add ({{< dyn-val "deficits_2021_2023" >}}). The share of prices in that growth is the subject of the French page [L'inflation a-t-elle allégé la dette ?](/inflation-et-dette-publique/) Since 2024, the ratio has been rising again.

**The implicit interest rate has been rising since 2022, first with a jump.** After a low of {{< dyn-val "ti_creux" >}}% in {{< dyn-val "ti_creux_an" >}}, the implicit interest rate on the debt goes from {{< dyn-val "ti_2021" >}}% in 2021 to {{< dyn-val "ti_2022" >}}% in 2022, then rises more slowly. That jump does not come only from bonds being renewed at the new rates: in 2022, inflation also sharply raised the recorded cost of the State's inflation-linked bonds, according to the French Senate's report on that year's accounts. The accounts presented here do not make it possible to separate the share of each mechanism in the implicit rate of general government as a whole.

**The {{< dyn-val "annee_fin" >}} accounts are still subject to revision.** Those on this page are the Eurostat series released on {{< dyn-val "millesime_dette" >}} for the debt, with the April notification, and on {{< dyn-val "millesime_comptes" >}} for the accounts. That year, the implicit rate ({{< dyn-val "taux_implicite_dernier" >}}%) and nominal growth ({{< dyn-val "croissance_derniere" >}}%) are almost equal, and the interest-growth effect is close to zero: so narrow a gap does not say which way the effect will go next.

Over the {{< dyn-val "annees_total" >}} years of the series, the primary balance was in surplus only {{< dyn-val "annees_excedent" >}} times. This count describes a recurrence; it does not say whether each of these deficits was desirable, avoidable or cyclical.

## Too much spending or too little revenue? {#depenses-recettes}

The primary deficit is the gap between spending excluding interest and public revenue. It does not say whether that gap comes from rising spending, falling revenue or both at once. To describe it, one has to pick two years and compare spending and revenue, as a share of GDP, between them. Eurostat's series then give different answers depending on the years chosen.

- **From {{< dyn-val "ofce_debut" >}} to {{< dyn-val "ofce_fin" >}}**, the period chosen by the OFCE: public revenue changes by {{< dyn-val "ofce_rec" >}} points of GDP, spending excluding interest by {{< dyn-val "ofce_dep_hi" >}}. The fall in revenue dominates.
- **From {{< dyn-val "tresor_debut" >}} to {{< dyn-val "tresor_fin" >}}**, the period chosen by the French Treasury: spending excluding interest changes by {{< dyn-val "tresor_dep_hi" >}} points, revenue by {{< dyn-val "tresor_rec" >}}. The rise in spending dominates.
- **From {{< dyn-val "tresor_debut" >}} to {{< dyn-val "ofce_fin" >}}**, the window common to both: spending excluding interest changes by {{< dyn-val "croise_dep_hi" >}} points, revenue by {{< dyn-val "croise_rec" >}}. The fall in revenue dominates again.

**The diagnosis depends on both ends.** It changes with the start year, but also with the end year: ending in {{< dyn-val "ofce_fin" >}} rather than {{< dyn-val "tresor_fin" >}}, the same start year gives the opposite conclusion. Two accurate comparisons over different periods can therefore lead to opposite descriptive findings — which does not make the causal interpretations drawn from them well founded. The page measures one Eurostat indicator over these windows; it does not make the OFCE's and the Treasury's work equivalent, as they also differ in their definitions and questions: faced with either, the first question to ask is "from which year to which year?". 

**What reverses the conclusion between the two windows starting in {{< dyn-val "tresor_debut" >}} is revenue.** Spending excluding interest changes by the same amount in both, to within rounding; revenue, for its part, rises by {{< dyn-val "rec_fin" >}} points of GDP in {{< dyn-val "tresor_fin" >}}. It is the easing of the fall in revenue, not a movement in spending, that tips their relative weight. These movements are measured as shares of GDP: they can come from the numerator, the denominator, or both. This descriptive finding, on accounts still subject to revision, does not say which decisions produced that rise. And a shrinking deficit has not disappeared: in {{< dyn-val "tresor_fin" >}}, the primary balance is still in deficit and the debt keeps rising. These comparisons describe movements as a share of GDP; they do not say which decisions produced them, or what should be corrected. What the OFCE and the French Treasury conclude from them, and about which objects, is set against each other below.

## How the calculation works {#identite}

Each year, the debt-to-GDP ratio moves under the effect of three terms. The **interest-growth effect**: the year's interest adds to the debt, while nominal GDP growth — real growth plus price rises — lowers the ratio even without any repayment; their balance is positive when the implicit interest rate exceeds nominal growth, negative in the opposite case. The **primary deficit**: the gap between public spending and revenue excluding interest, which measures the gap, not its cause. **Stock-flow adjustments**: debt that moves without passing through the deficit (cash set aside, loans and equity stakes, valuation effects), obtained here as a residual. The waterfall shows the interest-growth effect as its two components, interest and growth: hence its four steps for three terms.

<details class="repli"><summary>The exact identity, term by term</summary>

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

</details>

## What this decomposition does not say {#limites}

- **An accounting decomposition, not a causal explanation.** It identifies which accounting components moved the debt; it does not say why the deficits existed, whether they were avoidable, or who is responsible for them.
- **Contributions, not amounts paid.** The points of GDP in the waterfall measure the effect on a ratio, cumulated over thirty years; they do not say how much was paid, to whom, or when.
- **Terms that are not independent.** In a recession, revenue falls and some spending rises: the primary deficit itself depends on growth.
- **Inflation does not reduce the real burden of nominal debt without cost.** It reduces the real value of nominal claims, and that loss is borne by someone: this is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- **Nothing about the future.** What comes next depends on the gap between the implicit interest rate and nominal growth, and on the primary balance: what it took elsewhere for debt to come down is the subject of [Can public debt come down?](/en/can-public-debt-come-down/)
- **A last year subject to revision.** The {{< dyn-val "annee_fin" >}} accounts are those of the Eurostat series released on {{< dyn-val "millesime_dette" >}} (debt) and {{< dyn-val "millesime_comptes" >}} (accounts).
- **A series that starts in {{< dyn-val "annee_depart" >}}.** Eurostat's harmonised interest data go back no further; the long-run debt series, since 1978, is in [What does French public debt actually cost?](/en/cost-of-french-public-debt/)

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="the weight of primary deficits is found again over fifty years; reading the near-cancellation of interest and growth as neutrality is challenged; spending or revenue: the diagnosis depends on the period and the comparison chosen" >}}
**Measured here.** The annual decomposition of the French ratio from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}, on Eurostat series, checked against the published ratios. None of the texts read decomposes this window with this source: the measurement is validated by reproduction, not by citation.

**Consistent with.** The 2014 citizens' audit attributed a large share of the rise in the debt from 1980 to 2012 to the effect of interest rates. The two analyses share neither the same end points nor necessarily the same counterfactual; over a window that ends before the mid-2010s, the interest-growth effect weighs heavily here too, before {{< dyn-val "tc_bascule" >}}. The comparison of their methods is set out in the working paper [AWP-09](/en/awp/awp-09/). Over 1970-2023, using INSEE accounts and a historical database, Auclert, Philippon and Ragot find that primary deficits and stock-flow adjustments account for 88 points of a rise of nearly 90 (from 21% to 110% of GDP), and a "snowball" effect close to zero on average: the same identity, another period, another source, and a primary deficit that includes the adjustments this page isolates. Clavères, at the French Treasury, finds the same sequence of signs: the effective interest rate on the debt, close to this page's implicit interest rate without being identical to it (both relate interest to a debt stock, not necessarily the same one: the apparent cost published by Eurostat uses the year's average stock, this page the stock at the end of the previous year), moves above nominal growth in the course of the 1980s, and growth moves back above it from 2016. The OFCE (Heyer, Plane, Ragot, Sampognaro and Timbeau) links to deficits a rise in debt of 53 points in France from 2000 to 2024, against 44 in Spain, 27 in Italy and 5 in Germany, without decomposing these rises. The French Treasury describes debt rising almost continuously since 2001, with deficit reductions in favourable periods only stabilising the ratio, and a deficit that stayed above the stabilising balance until 2019. It describes 2001-2007 as "relative stability"; the page's series nonetheless records a rise from {{< dyn-val "dette_2001" >}}% to {{< dyn-val "dette_2007" >}}% of GDP, and the OFCE estimates that nearly half of the deficit gap with the euro area had formed before the 2007-2008 crisis.

**Challenged by.** Any reading of the near-cancellation of interest and growth as neutrality. The match depends on the starting point, to within about ten points (Auclert, Philippon and Ragot), and the gap between interest and growth changed sign during the period (Clavères). This page's data confirm it: the interest-growth effect weighed {{< dyn-val "tc_avant" >}} points before {{< dyn-val "tc_bascule" >}}, {{< dyn-val "tc_apres" >}} since. The CAE note, for its part, interprets this accounting finding as the direct result of budgetary choices ("our debt is the direct consequence of our budgetary choices"), while judging the share of crises hard to estimate; an OFCE estimate, cited by the note, puts it at about half of the rise since 2007.

**Not established.** Which of spending or revenue widened the recent deficits. The OFCE, which puts forward a more gradual adjustment path, starts the recent period at the 2017 presidential election and attributes most of the deterioration of the structural balance to an unfunded fall in compulsory levies, which declined by 2.5 points of GDP from 2017 to 2024; over that period, according to the OFCE, total spending stays stable as a share of GDP and primary spending falls slightly as a share of potential GDP (on Eurostat's series, as a share of actual GDP, total spending changes by {{< dyn-val "ofce_dep" >}} points). The French Treasury, for which consolidation "could go first" through cutting spending, starts from 2019, the situation before the pandemic, and notes that several spending items (interest charge, social security, central and local government) contributed to the 2.7-point deterioration of the balance up to 2025, while noting that reforms durably reduced revenue. Over the common window, the OFCE and the French Treasury converge on one fact: public spending rose less in France than in the euro area (1.8 points against 2.6 for the one, 1.6 against 2.4 for the other); Eurostat's series find the same direction and order of magnitude (spending {{< dyn-val "croise_dep" >}} points, total revenue {{< dyn-val "croise_rec" >}}). They do not, however, then analyse the same object: the OFCE explains the gap between France and the euro area, which it links mainly to revenue, while the French Treasury breaks down the deterioration of the French balance over 2019-2025; and Eurostat's total revenue is not the OFCE's compulsory levies. On Eurostat's series, the diagnosis depends on both ends of the window (section "Too much spending or too little revenue?"). The causes, finally: the CAE note attributes the recent deterioration to the pandemic, the energy price shields and unfunded tax cuts, the French Treasury to the crises and the support measures, but none of the six texts provides a causal decomposition of the primary deficits observed from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}.

**References read**

- Auclert, A., Philippon, T. and Ragot, X., "Quelle trajectoire pour les finances publiques françaises ?" [What path for French public finances?], *Les notes du Conseil d'analyse économique*, no. 82, July 2024 (in French).
- Clavères, G., "Taux d'intérêt, croissance et soutenabilité de la dette publique" [Interest rates, growth and public debt sustainability], *Trésor-Éco*, no. 334, French Treasury, October 2023 (in French).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. and Timbeau, X., "Quelles trajectoires pour les finances publiques de la France ?" [What paths for France's public finances?], *Blog de l'OFCE*, 2025 (in French).
- French Treasury (Direction générale du Trésor), "Finances publiques : une situation dégradée, un redressement nécessaire" [Public finances: a deteriorated situation, a necessary recovery], *Trésor-Éco*, no. 403, September 2026 (in French).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. and Timbeau, X., "Quelles trajectoires pour les finances publiques de la France ?" [What paths for France's public finances?], OFCE working paper no. 13, July 2025 (in French).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## What to take away {#retenir}

In thirty years, French public debt doubled as a share of GDP, from {{< dyn-val "dette_depart" >}}% to {{< dyn-val "dette_fin" >}}%. Interest pushed it up, but over the whole period nominal GDP growth erased almost as much; what remains, in the Eurostat decomposition used here, is primary deficits, {{< dyn-val "part_deficits" >}}% of the rise: excluding interest, the public accounts were in surplus in only {{< dyn-val "annees_excedent" >}} years out of {{< dyn-val "annees_total" >}}.

This near-cancellation is an offset over time, not neutrality. Before {{< dyn-val "tc_bascule" >}}, the implicit interest rate usually exceeded nominal growth, and the interest-growth effect added {{< dyn-val "tc_avant" >}} points to the ratio; since then, nominal growth has prevailed every year except 2020, when GDP fell, and the effect has weighed {{< dyn-val "tc_apres" >}} points. In {{< dyn-val "annee_fin" >}}, on accounts still subject to revision, the implicit rate and nominal growth are almost equal: as long as they stay so, the direction of the ratio is set by the primary balance, give or take stock-flow adjustments. The implicit rate has been rising since 2022; if it moves back above growth, the ratio will rise more for the same primary balance.

Spending or revenue: the accounts describe movements, they do not designate anyone responsible, and their answer changes with the two years being compared. What it took elsewhere for debt to come down is the subject of [Can public debt come down?](/en/can-public-debt-come-down/)

</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [What does French public debt actually cost?](/en/cost-of-french-public-debt/)
- [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- [And elsewhere?](/en/public-debt-international-comparison/)
- [Can it come down?](/en/can-public-debt-come-down/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page identifies which accounting components contributed to the rise in the debt. It does not say who bears its cost, or through which channels that cost is shifted — onto the taxpayer, onto the saver through inflation, onto public services whose resources are squeezed — depending on the decisions taken to adjust it. The book follows these channels one by one, on official figures, to show in which configurations each group bears a cost. It offers a three-question method — are the facts established, does the system keep its promise, who decides — and, for the outcomes it considers, the split between who pays and who gains. The book exists in French only.
{{< /appel-livre >}}

## Where these figures come from {#sources}

Eurostat, general government (S.13), national accounts ESA 2010, in national currency: Maastricht debt ([`gov_10dd_edpt1`](https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=en)), interest due ([`gov_10a_main`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=en), D41PAY, recorded on an accrual basis), net lending or borrowing (B9), nominal GDP as published with the deficit and debt notification (`gov_10dd_edpt1`, B1GQ); spending (TE), revenue (TR) and balance as a share of GDP as Eurostat publishes them (`gov_10a_main`). The primary balance is the general government balance plus interest (D41PAY). Each year, the identity is applied as written above; stock-flow adjustments are the residual. The script then compares, year by year, the debt ratio and the primary balance it computes with those Eurostat publishes as a percentage of GDP, and stops beyond a gap of 0.11 point. No figure on this page is entered by hand: all come from the same script, re-run with each release of the sources, which checks the main quantitative statements and stops if their conditions are no longer met; their wording is reviewed editorially. Indexation cost of State bonds in 2022: French Senate, [report on the 2022 budget settlement bill](https://www.senat.fr/rap/l22-771-1/l22-771-17.html) (in French).

The method behind this decomposition (the identity, the benchmark formed by the ratios Eurostat publishes, and the error it rejected) and its reconciliation with three public readings of the same debt (the 2014 citizens' audit, the iFRAP Foundation, the French Court of Audit) are set out in the working paper [AWP-09 — *What Public Accounts Can Establish about the Displacement of the Public Debt Burden*](/en/awp/awp-09/) (DOI: 10.5281/zenodo.23145963, open-access PDF).

{{< reutiliser figures="figures_dynamique" jeu="dette_dynamique" sources="Eurostat" donnees="The annual decomposition of the change in the debt-to-GDP ratio, France, with its four terms, the implicit interest rate and nominal growth; spending, revenue and balance as a share of GDP; the same content is available as CSV, one row per year." >}}
This page decomposes the change in the French debt-to-GDP ratio, from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}, into the interest effect, the nominal growth effect, the primary balance and stock-flow adjustments. Over the period, interest and nominal growth almost cancelled out, in two opposite periods, and the rise comes mostly from primary deficits, excluding interest. Spending or revenue: the accounts' answer changes with the two years compared. This is an accounting decomposition, not a causal attribution: it does not say why the deficits existed.
{{< /reutiliser >}}
