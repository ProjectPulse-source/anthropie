---
title: "Can public debt come down?"
url: /en/can-public-debt-come-down/
description: "From {baisse.d3_debut} to {baisse.annee_fin}, the weight of French debt in GDP rose by {baisse.d3_var_abs} points: primary deficits added {baisse.d3_def_abs}, and the interest-growth effect, favourable mostly in {baisse.d3_creux_lib}, took off {baisse.d3_tc_abs}. Compared with {baisse.cmp_autres_n} European countries that started from higher debt."
chapo: "Yes: its weight in GDP can fall even while its amount rises, and it has fallen elsewhere. In France, from {baisse.d3_debut} to {baisse.annee_fin}, primary deficits, excluding interest, outweighed the relief from interest rates and growth: the debt-to-GDP ratio rose by {baisse.d3_var_abs} points."
og_title: "Can public debt come down?"
og_image: "images/og-dette-baisse-en.jpg"
og_image_alt: "Share card: “Deficits weighed more” — France, three decades: interest-growth effect, primary deficits and other adjustments, in points of GDP."
date: 2026-10-03
lastmod: 2026-10-03
# English version of part 5 of the public debt dossier (FR: content/dette-publique-peut-elle-baisser/_index.md), a mirror
# requested by the author on 03/10/2026. Same tokens, same keys: values come from the affichage_en block of
# data/dette_baisse.json (scripts/update_dette_baisse.py), whose guards cover both languages.
donnees: [dette_baisse]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_baisse"
  nom: "Can public debt come down: a decade-by-decade decomposition of the debt-to-GDP ratio, France and EU countries that started above 90% of GDP"
  description: "Decomposition of the change in the debt-to-GDP ratio into the interest-growth effect, primary deficits and other (stock-flow) adjustments: France by decade from {baisse.annee_debut} to {baisse.annee_fin}, the observed and the stabilising primary balance year by year, and the EU countries whose debt exceeded {baisse.seuil_dette}% of GDP at end-{baisse.cmp_veille}. Ratios checked against those published by Eurostat; no value entered by hand."
  couverture_temporelle: "{baisse.annee_debut}/{baisse.annee_fin}"
  couverture_spatiale: "France; European Union (27 countries)"
  variables:
    - {nom: "Change in the debt-to-GDP ratio", unite: "points of GDP", description: "cumulated over ten years"}
    - {nom: "Interest-growth effect", unite: "points of GDP", description: "interest minus the erosion of the ratio by nominal GDP growth"}
    - {nom: "Cumulated primary deficits", unite: "points of GDP", description: "excluding interest; negative for surpluses"}
    - {nom: "Other (stock-flow) adjustments", unite: "points of GDP", description: "residual of the identity"}
    - {nom: "Stabilising primary balance", unite: "% of GDP", description: "balance that would have kept the ratio unchanged that year, excluding other adjustments"}
    - {nom: "Debt outstanding", unite: "billions of national currency", description: "compared countries, start and end of the decade"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
  mots: ["public debt", "France", "primary surplus", "stabilising primary balance", "implicit interest rate", "nominal growth", "debt reduction", "Eurostat"]
  fichiers: ["dette_baisse.csv", "dette_baisse.json"]
faq:
  - question: "Can French public debt come down?"
    answer: "Interest and primary deficits push the debt-to-GDP ratio up; nominal GDP growth and primary surpluses pull it down; other adjustments work both ways. The ratio falls when these contributions add up to a negative total, even if the amount of debt keeps rising. From {baisse.d3_debut} to {baisse.annee_fin}, the French ratio rose by {baisse.d3_var_abs} points: primary deficits added {baisse.d3_def_abs}, the interest-growth effect took off {baisse.d3_tc_abs}, mostly in {baisse.d3_creux_lib}. Over the same decade, it fell by {baisse.cmp_exc_baisse_min} to {baisse.cmp_exc_baisse_max} points in {baisse.cmp_exc_n} countries that started from higher debt, all with an average primary surplus: {baisse.cmp_exc_pays}."
  - question: "Are growth and inflation enough to bring debt down?"
    answer: "They lighten the ratio when nominal growth exceeds the interest rate paid on the debt, but the effect varies a great deal from year to year: in France, it took off {baisse.d3_creux_abs} points in {baisse.d3_creux_lib} and added {baisse.d3_pic_tc} points in {baisse.d3_pic_annee}. In the {baisse.cmp_n} EU countries whose debt exceeded {baisse.seuil_dette}% of GDP at end-{baisse.cmp_veille}, it was favourable everywhere, by {baisse.cmp_tc_min} to {baisse.cmp_tc_max} points over ten years; none of those that stayed in average primary deficit saw its ratio fall by {baisse.forte_baisse} points."
  - question: "What primary balance would stabilise French debt?"
    answer: "Excluding other adjustments, it is the balance that offsets that year's interest-growth effect: it depends on the gap between the implicit interest rate on the debt and nominal growth, and on the level of the debt. In {baisse.annee_fin}, the two rates were almost equal ({baisse.taux_implicite_dernier}% and {baisse.croissance_derniere}%): this benchmark was close to zero, against an observed balance of {baisse.pb_dernier}% of GDP. It varies widely, from {baisse.stab_min}% in {baisse.stab_min_annee} to {baisse.stab_max}% in {baisse.stab_max_annee}. Stabilising the observed ratio also requires taking other adjustments into account."
  - question: "Is French public debt sustainable?"
    answer: "No level of debt, on its own, settles the question: it depends on the primary balance, on the gap between the interest rate the State pays and nominal growth, and on the confidence of its lenders. The first two terms can be measured. In {baisse.annee_fin}, the implicit interest rate ({baisse.taux_implicite_dernier}%) and nominal growth ({baisse.croissance_derniere}%) were almost equal, and the observed primary balance was {baisse.pb_dernier}% of GDP: the ratio rose by {baisse.var_derniere} points. At the {baisse.annee_fin} level of debt ({baisse.dette_derniere}% of GDP), one additional point of gap between the interest rate and growth raises the balance that would stabilise the debt by about {baisse.sens_pt} points of GDP, all else equal; the implicit rate, down to {baisse.ti_creux}% in {baisse.ti_creux_annee}, is rising as the debt is refinanced. Lenders' confidence and market access, for their part, cannot be read in these series."
  - question: "Has France ever run a primary surplus?"
    answer: "{baisse.exc_n_maj} times since {baisse.annee_debut}, from {baisse.exc_premiere} to {baisse.exc_derniere}, at most {baisse.exc_max}% of GDP (Eurostat). Since then, the general government primary balance has been in deficit every year."
  - question: "Does a primary surplus always bring debt down?"
    answer: "It helps reduce the ratio, but the final change also depends on interest rates, growth and other adjustments: in France, the balance reached the stabilising benchmark excluding adjustments in {baisse.suff_hausse} without the ratio falling. In the ten-year windows of the {baisse.eu_pays} current EU members where starting debt exceeded {baisse.seuil_dette}% of GDP, falls of at least {baisse.forte_baisse} points number {baisse.eu_def_fb} out of {baisse.eu_def_n} with a negative average primary balance, {baisse.eu_mid_fb} out of {baisse.eu_mid_n} with a balance from 0 to under 2%, {baisse.eu_exc_fb} out of {baisse.eu_exc_n} with a balance of at least 2%; these windows overlap and come from a few countries."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 35
  nature: "Official series (Eurostat) decomposed, and the author's calculations"
---

{{< dossier-dette volet="baisse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Updated: {{< baisse-val "date_donnees" >}}</span> General government, Eurostat series from {{< baisse-val "annee_debut" >}} to {{< baisse-val "annee_fin" >}}. Download: <a href="/dette_baisse.csv">CSV</a> · <a href="/dette_baisse.json">JSON</a> · <a href="#sources">method</a></p>

## Three decades, three regimes {#trois-decennies}

<figure class="figure-ciseau">
  <img src="/img/dette-baisse-decennies-en.svg" alt="Three groups of bars in points of GDP cumulated over ten years: interest-growth effect (T), contribution of primary deficits or surpluses (S), other adjustments (A). {{< baisse-val "d1_lib" >}}: {{< baisse-val "d1_tc" >}}, {{< baisse-val "d1_def" >}}, {{< baisse-val "d1_sfa" >}}. {{< baisse-val "d2_lib" >}}: {{< baisse-val "d2_tc" >}}, {{< baisse-val "d2_def" >}}, {{< baisse-val "d2_sfa" >}}. {{< baisse-val "d3_lib" >}}: {{< baisse-val "d3_tc" >}}, {{< baisse-val "d3_def" >}}, {{< baisse-val "d3_sfa" >}}." width="720" height="408" loading="lazy">
  <figcaption>What pushed the French debt-to-GDP ratio up or down, by decade, in points of GDP cumulated (Eurostat). Orange: what pushes it up; grey: what pulls it down.</figcaption>
</figure>

<div class="resultat-phrase">

**The finding in one sentence.** From {{< baisse-val "d3_debut" >}} to {{< baisse-val "annee_fin" >}}, primary deficits added {{< baisse-val "d3_def_abs" >}} points to the French debt ratio, the interest-growth effect, concentrated in {{< baisse-val "d3_creux_lib" >}}, took off {{< baisse-val "d3_tc_abs" >}}, and other adjustments added {{< baisse-val "d3_sfa_abs" >}}: the net result is a rise of {{< baisse-val "d3_var_abs" >}} points. This is an accounting decomposition: it says through which term the debt moved, not why the deficits occurred.

</div>

What falls or rises here is the weight of the debt in GDP, not its amount: a ratio can decline while the debt in euros grows, if nominal GDP grows faster. The ratio moves under three terms, set out in [Why does French public debt rise?](/en/why-does-public-debt-rise/): the interest-growth effect (interest, minus what nominal GDP growth erases), the primary balance (revenue minus spending, excluding interest) and other adjustments, known as “stock-flow” (acquisitions of assets, changes in cash holdings and other operations that change the debt without going through the deficit). Cumulated by decade, the term that pushes the debt changes from one period to the next.

**{{< baisse-val "d1_lib" >}}: interest rates push, the budget excluding interest is close to balance.** The ratio goes from {{< baisse-val "d1_dette_deb" >}}% to {{< baisse-val "d1_dette_fin" >}}% of GDP. Over the decade as a whole, the interest-growth effect adds {{< baisse-val "d1_tc_abs" >}} points. The primary balance, in surplus {{< baisse-val "d1_exc" >}} years out of ten, takes off {{< baisse-val "d1_def_abs" >}}.

**{{< baisse-val "d2_lib" >}}: both terms push together.** The ratio gains {{< baisse-val "d2_var_abs" >}} points, the largest rise of the three decades: {{< baisse-val "d2_def_abs" >}} from primary deficits, {{< baisse-val "d2_tc_abs" >}} from the interest-growth effect. The period includes the 2008-2009 financial crisis.

**{{< baisse-val "d3_lib" >}}: an interest-growth effect favourable in total, outweighed by primary deficits.** Interest adds {{< baisse-val "d3_interets" >}} points, nominal GDP growth erases {{< baisse-val "d3_croissance" >}}: in total, the interest-growth effect is {{< baisse-val "d3_tc" >}} points. This relief is concentrated in {{< baisse-val "d3_creux_lib" >}}, years of rebound in activity and then inflation, which alone take off {{< baisse-val "d3_creux_abs" >}} points; the other {{< baisse-val "d3_reste_n" >}} years together weigh {{< baisse-val "d3_reste" >}} points, including {{< baisse-val "d3_pic_tc" >}} in {{< baisse-val "d3_pic_annee" >}}, when GDP fell. No year of the decade shows a primary surplus: cumulated deficits add {{< baisse-val "d3_def_abs" >}} points, more than the whole rise of the ratio ({{< baisse-val "d3_var" >}}).

From one decade to the next, the contribution of primary deficits went from {{< baisse-val "d1_def" >}} to {{< baisse-val "d2_def" >}} and then {{< baisse-val "d3_def" >}} points. This describes a recurrence; it does not say whether these deficits were avoidable, nor which of their two terms, spending or revenue, explains them.

## Countries that started from higher debt {#pays-compares}

The same decomposition, over the same decade, applies to the EU countries whose debt exceeded {{< baisse-val "seuil_dette" >}}% of GDP at end-{{< baisse-val "cmp_veille" >}}: France, at {{< baisse-val "cmp_fr_d0" >}}%, and {{< baisse-val "cmp_autres_n" >}} others, all starting from higher. This threshold is a presentation convention, close to the French level; it does not make these countries equivalent experiments.

<figure class="figure-ciseau">
  <img src="/img/dette-baisse-comparaison-en.svg" alt="For each of the {{< baisse-val "cmp_n" >}} countries, three bars in points of GDP cumulated over {{< baisse-val "cmp_lib" >}}: the interest-growth effect, negative everywhere; the contribution of the primary balance, negative in {{< baisse-val "cmp_exc_n" >}} countries and positive in {{< baisse-val "cmp_def_n" >}}; other adjustments. France: interest-growth effect {{< baisse-val "cmp_fr_tc" >}}, primary deficits {{< baisse-val "cmp_fr_def" >}}, other adjustments {{< baisse-val "cmp_fr_sfa" >}}, ratio {{< baisse-val "cmp_fr_var" >}} points." width="720" height="418" loading="lazy">
  <figcaption>Interest-growth effect (T), contribution of the primary balance (S) and other adjustments (A) to the change in the debt ratio, {{< baisse-val "cmp_lib" >}}, in points of GDP cumulated (Eurostat). Countries sorted by change in the ratio.</figcaption>
</figure>

<div class="encadre">

**What the group allows us to say, and what it does not.** Within this group, the {{< baisse-val "cmp_exc_n" >}} large falls in the ratio go together with an average primary surplus. But the favourable contributions of interest rates and growth range from {{< baisse-val "cmp_tc_min" >}} to {{< baisse-val "cmp_tc_max" >}} points: this is not a common environment. And the finding depends on the scope: at 80%, the group has {{< baisse-val "s80_n" >}} countries, adding {{< baisse-val "s80_ajouts" >}}; {{< baisse-val "s80_exc_pays" >}}, starting from {{< baisse-val "s80_exc_d0" >}}%, saw its ratio fall by {{< baisse-val "s80_exc_var" >}} points with an average primary balance of {{< baisse-val "s80_exc_pb" >}}% of GDP. At 100%, France drops out of the group.

</div>

- **The interest-growth effect pulled the ratio down in all {{< baisse-val "cmp_n" >}} countries**, by {{< baisse-val "cmp_tc_min" >}} to {{< baisse-val "cmp_tc_max" >}} points over ten years. France's ({{< baisse-val "cmp_fr_tc" >}}) is not the smallest in the group.
- **The ratio fell by {{< baisse-val "cmp_exc_baisse_min" >}} to {{< baisse-val "cmp_exc_baisse_max" >}} points in the {{< baisse-val "cmp_exc_n" >}} countries whose primary balance was in surplus on average**: {{< baisse-val "cmp_exc_pays" >}}, with an average surplus of {{< baisse-val "cmp_exc_pb_min" >}} to {{< baisse-val "cmp_exc_pb_max" >}}% of GDP. The amount of their debt, however, did not decrease: in Portugal, it went from {{< baisse-val "cmp_pt_enc0" >}} to {{< baisse-val "cmp_pt_enc1" >}} billion euros. Their other adjustments, positive, slowed the fall.
- **It stayed roughly stable for {{< baisse-val "cmp_def_autres" >}}** ({{< baisse-val "cmp_def_var_min" >}} to {{< baisse-val "cmp_def_var_max" >}} points), with an average primary deficit. In Belgium, the contributions of interest-growth and of the primary balance total {{< baisse-val "cmp_be_tcdef" >}} points; other adjustments add {{< baisse-val "cmp_be_sfa_abs" >}}, bringing the change to {{< baisse-val "cmp_be_var" >}} points.
- **It rose by {{< baisse-val "d3_var_abs" >}} points in France**, the largest rise in the group, with the highest average primary deficit ({{< baisse-val "cmp_fr_pb" >}}% of GDP).

<details class="repli"><summary>The {{< baisse-val "cmp_n" >}} countries, term by term</summary>

{{< baisse-tableau >}}

</details>

These countries were not financed on the same terms. Portugal (from 2011 to mid-2014), Cyprus (from April 2013 to March 2016) and Greece (from May 2010 to August 2018, with a last programme, financed by the European Stability Mechanism, from August 2015 to August 2018) received official financing from their European partners and the IMF; Spain received, from July 2012 to January 2014, assistance to recapitalise its banks ([European Commission](https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries_en); [European Stability Mechanism](https://www.esm.europa.eu/assistance/greece/greece-successfully-concludes-esm-programme)). The restructuring of Greek debt, in 2012, predates the decade studied. The average nominal growth of the three surplus countries exceeded that of France, which increases their interest-growth effect; and a primary balance itself depends on the economic cycle: a fast-growing economy collects more revenue. Seven countries over one decade do not make a general regularity, and the comparison does not isolate the effect of a policy.

## What primary balance would stabilise the debt? {#solde-stabilisant}

Excluding other adjustments, the debt ratio stays unchanged in a given year if the primary balance offsets that year's interest-growth effect: this is the benchmark plotted below. It is not a constant: it rises when the interest rate exceeds growth, and turns negative in the opposite case, where a limited primary deficit leaves the ratio stable. Stabilising the observed ratio also requires taking other adjustments into account: in {{< baisse-val "suff_hausse" >}}, the balance reached this benchmark and the ratio still rose.

<figure class="figure-ciseau">
  <img src="/img/dette-baisse-stabilisant-en.svg" alt="Two annual lines from {{< baisse-val "annee_debut" >}} to {{< baisse-val "annee_fin" >}}, in % of GDP: the observed primary balance, positive from {{< baisse-val "exc_premiere" >}} to {{< baisse-val "exc_derniere" >}} only, and the balance that would have stabilised the ratio excluding other adjustments, from {{< baisse-val "stab_min" >}}% in {{< baisse-val "stab_min_annee" >}} (GDP rebound) to {{< baisse-val "stab_max" >}}% in {{< baisse-val "stab_max_annee" >}} (GDP fell)." width="720" height="372" loading="lazy">
  <figcaption>Observed primary balance and the primary balance that would have stabilised the debt ratio that year, excluding other adjustments, France, in % of GDP (Eurostat, author's calculation).</figcaption>
</figure>

In {{< baisse-val "annee_fin" >}}, the implicit interest rate ({{< baisse-val "taux_implicite_dernier" >}}%) and nominal growth ({{< baisse-val "croissance_derniere" >}}%) were almost equal: the stabilising benchmark was close to zero. The observed primary balance was {{< baisse-val "pb_dernier" >}}% of GDP, a gap of {{< baisse-val "ecart_dernier" >}} points.

Over {{< baisse-val "annees_total" >}} years, this benchmark ranged from {{< baisse-val "stab_min" >}}% of GDP in {{< baisse-val "stab_min_annee" >}}, when nominal GDP rebounded, to {{< baisse-val "stab_max" >}}% in {{< baisse-val "stab_max_annee" >}}, when it fell. The observed balance reached or exceeded it in {{< baisse-val "suffisant_n" >}} years out of {{< baisse-val "annees_total" >}}. This count measures the years in which the benchmark excluding adjustments was reached; it is not the number of years in which the ratio actually fell, which it did in {{< baisse-val "suff_baisse_n" >}} of those years. France ran a primary surplus {{< baisse-val "exc_n" >}} times, from {{< baisse-val "exc_premiere" >}} to {{< baisse-val "exc_derniere" >}}, at most {{< baisse-val "exc_max" >}}% of GDP.

Stabilising the ratio and bringing it down are two different objectives. An adjustment amount is read with its objective, its horizon and its assumptions; the benchmark calculated here for {{< baisse-val "annee_fin" >}} applies to that year and cannot be used to assess institutions' multi-year estimates.

## Is French public debt sustainable? {#soutenable}

No level of debt, on its own, settles this question. A debt is called sustainable when the State can service and refinance it without a budgetary adjustment beyond reach; that depends on its primary balance, on the gap between the interest rate it pays and nominal growth, and on the confidence of those who lend to it. The first two terms are measured here; the third is not.

**What the data measure.** In {{< baisse-val "annee_fin" >}}, the balance that would have stabilised the ratio, excluding other adjustments, was close to zero; the observed balance was {{< baisse-val "pb_dernier" >}}% of GDP, and the ratio rose by {{< baisse-val "var_derniere" >}} points. At that year's interest rates and growth, stabilising it would have required a primary balance about {{< baisse-val "ecart_dernier" >}} points of GDP higher; bringing it down, more.

**What makes it fragile.** The equality between interest and growth in {{< baisse-val "annee_fin" >}} is not a settled state. Over {{< baisse-val "annees_total" >}} years, the implicit interest rate exceeded nominal growth in {{< baisse-val "rg_pos_n" >}} of them. Down to {{< baisse-val "ti_creux" >}}% in {{< baisse-val "ti_creux_annee" >}}, it is rising as old debt is refinanced on market terms, while nominal growth falls back after the inflation years: the relief of the last decade came mostly from {{< baisse-val "d3_creux_lib" >}}. At {{< baisse-val "annee_fin" >}} levels of debt and growth ({{< baisse-val "dette_derniere" >}}% of GDP), and all else equal, one additional point of gap between the interest rate and growth raises the stabilising balance by about {{< baisse-val "sens_pt" >}} points of GDP: the higher the debt, the more its path depends on interest rates the budget does not control.

**What these data do not say.** Lenders' confidence, market access and the cost of future refinancing depend on the maturity of the debt and on the gap between market rates and the implicit rate (see [transmission](/en/public-debt-international-comparison/#transmission)), on who holds it ([Who really pays for public debt?](/en/who-really-pays-public-debt/)) and on central bank decisions. The sustainability assessments that institutions publish rest on conditional projections, which these data can neither confirm nor rule out.

## Thirty years of European windows {#europe}

<details class="repli"><summary>Primary balances and falls in the ratio: European ten-year periods</summary>

The comparison above covers a single decade. To place it in a wider set, the same decomposition was applied to every ten-year window of the {{< baisse-val "eu_pays" >}} current EU members, since {{< baisse-val "eu_premiere" >}}: {{< baisse-val "eu_fenetres" >}} windows, which overlap, are therefore not as many independent experiments, and include the decade already compared. This is context, not a counter-test.

Among the {{< baisse-val "eu_hautes_n" >}} windows where starting debt exceeded {{< baisse-val "seuil_dette" >}}% of GDP:

- **negative average primary balance**: {{< baisse-val "eu_def_n" >}} windows, in {{< baisse-val "eu_def_pays_n" >}} countries ({{< baisse-val "eu_def_pays" >}}). The ratio falls in {{< baisse-val "eu_def_baisses" >}} of them, never by {{< baisse-val "forte_baisse" >}} points;
- **average primary balance from 0 to under 2% of GDP**: {{< baisse-val "eu_mid_n" >}} windows, in {{< baisse-val "eu_mid_pays_n" >}} countries. The ratio falls in {{< baisse-val "eu_mid_baisses" >}} of them, by {{< baisse-val "forte_baisse" >}} points or more in {{< baisse-val "eu_mid_fb" >}};
- **average primary balance of at least 2% of GDP**: {{< baisse-val "eu_exc_n" >}} windows, in only {{< baisse-val "eu_exc_pays_n" >}} countries ({{< baisse-val "eu_exc_pays" >}}). The ratio falls in all {{< baisse-val "eu_exc_baisses" >}}, by {{< baisse-val "forte_baisse" >}} points or more in {{< baisse-val "eu_exc_fb" >}}.

These frequencies describe past periods, in a few countries. They give neither a surplus threshold to reach nor a probability of success: the high-surplus windows mostly start before 2003.

</details>

## What these data do not say {#limites}

- **Measuring the debt.** A fall in the ratio does not mean that the amount of debt has decreased. The debt tracked is gross: other adjustments mix asset purchases, loans and valuation changes, and a country that borrows to acquire assets sees its gross debt rise without its financial position worsening by as much.
- **Economic interpretation.** An accounting decomposition, not a causal one: the terms depend on one another, and the observed balance includes the economic cycle; it does not measure an effort. Nothing here says which of spending or revenue should move, nor who would bear the cost: that is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/) The interest-growth effect is based on nominal GDP: lowering the ratio through inflation reduces the real value of claims, and that loss is borne by someone.
- **Scope of the comparison.** The 27 current EU members, since {{< baisse-val "eu_premiere" >}}; nothing before, nothing outside the Union. The compared group depends on the debt threshold and the decade chosen. {{< baisse-val "cons_ecartees_maj" >}} country-years out of {{< baisse-val "cons_calculables" >}} are excluded by the check described below.
- **Time horizon.** The page describes thirty observed years. The paths forecast by the French government, the European Commission or the IMF are conditional scenarios, which these data can neither confirm nor rule out.

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="the stabilising balance and the distinction between stabilising and reducing are found again; reading the last year's zero gap as a lasting state, or the surplus as the only driver of falls, is challenged" >}}
**Measured here.** The decade-by-decade decomposition of the French ratio, the stabilising balance year by year and the comparison of EU countries that started above {{< baisse-val "seuil_dette" >}}% of GDP, on Eurostat series. None of the texts read calculates these quantities on this source and these periods: they are validated by reproduction.

**Consistent with.** The primary balance that stabilises the debt depends on the gap between interest and growth and on the level of the debt, in the same identity of debt dynamics, written in nominal terms here and in real terms in the Focus, in Clavères (French Treasury), in note no. 82 of the Conseil d'analyse économique (Auclert, Philippon and Ragot) and in its Focus no. 124 (Auclert, Barbara, Jaravel, Laveissière, Lasterra, Ragot and Renaud), which starts from a zero gap, like the page's benchmark for the last year. The note draws the same distinction between stabilising, which requires a zero primary balance when interest and growth are equal, and reducing, which requires a surplus. Across the G7 countries since the late nineteenth century, Clavères finds that, in the great majority of cases, successful fiscal consolidations rested both on a negative interest-growth gap and on primary surpluses. The French Treasury presents stabilising the ratio as a necessary condition of sustainability, which it also links to the State's capacity to finance its debt durably; it puts the stabilising balance for 2025 at −2.1% of GDP, as a total public balance, against a deficit of 5.1%. Two different conventions, and an almost identical gap to close in 2025: about three points of GDP for the Treasury, {{< baisse-val "ecart_dernier" >}} points measured here as a primary balance. The OFCE puts at 2.1 points, in 2024, the gap between the primary balance and the one that would stabilise the debt; the page's Eurostat measure gives {{< baisse-val "ecart_prec" >}} points for {{< baisse-val "annee_prec" >}}.

**Challenged by.** Two readings the page must avoid. The first would make the primary surplus the only driver of falls: after 1945, it was the strongly negative gap between interest and growth that contributed most to the fall in advanced economies' debt, primary surpluses also playing a part (Clavères); in Portugal, the surplus coincided with growth of 4.38% a year from 2015 to 2019, and in Italy, when the interest rate exceeded growth, debt rose despite a positive structural primary balance (CAE note). Hence the page's caveat: the comparison does not isolate the effect of a policy. The second would read the last year's zero gap as a lasting state: in autumn 2025, the State was borrowing at 10 years at 3.5%, above an effective interest rate estimated at 2.0% (CAE Focus); rate rises pass through to the stock only gradually, the average maturity of the debt being 8.5 years in 2023, future values of the gap cannot be forecast, and, in Clavères's estimate over 18 advanced economies from 1950 to 2019, measured with the 10-year rate, higher debt goes with a higher gap the following year, an estimate its author says should be taken with caution. The French Treasury also writes that rising rates reverse the period of negative gap and now require a slight primary surplus, and that rate rises pass through to the stock as it is refinanced. The diagnosis is not unanimous: the OFCE regards a rise in the interest bill as likely, but its size as less certain than in official projections. Refinancing at the July 2025 10-year rate the 900 billion euros of bonds maturing by 2029 would cost about 0.5 points of GDP; the authors set this against a total rise of 1.2 points projected by the IMF, though the two calculations do not cover the same scope. Its model also assumes an effective interest rate below nominal growth from 2026. Finally, the CAE note argues that it would be hard to let debt exceed 125% of GDP without risking a sharp rise in interest rates, and the Focus uses 130% as the ceiling of its model, Greece's level in 2009: the first figure is motivated by the observation of a few European cases, the second is a chosen parameter; neither is an estimated threshold, which leaves intact the page's statement that no level of debt, on its own, settles the question.

**Not established.** The size of the effort. The CAE Focus's 112 billion euros amount to 3.7 points of GDP: an estimated **structural** primary deficit of 2.7 points, as forecast in October 2025, plus one point of margin for the next crisis. They cannot be compared term by term with the page's observed gap for {{< baisse-val "annee_fin" >}}, excluding other adjustments. The OFCE (Heyer, Plane, Ragot, Sampognaro and Timbeau) puts at 2.8 points of GDP by 2029 a gradual adjustment that would stabilise debt at 110%, 2.5 points with lower interest rates: a model projection. Market access: none of the six texts measures it; the French Treasury invokes credibility with investors without measuring it.

**References read**

- Auclert, A., Philippon, T. and Ragot, X., "Quelle trajectoire pour les finances publiques françaises ?" [What path for French public finances?], *Les notes du Conseil d'analyse économique*, no. 82, July 2024 (in French).
- Auclert, A., Barbara, M.-A., Jaravel, X., Laveissière, E., Lasterra, O., Ragot, X. and Renaud, D., "Comment stabiliser la dette publique ?" [How to stabilise public debt?], *Focus du Conseil d'analyse économique*, no. 124, October 2025 (in French).
- Clavères, G., "Taux d'intérêt, croissance et soutenabilité de la dette publique" [Interest rates, growth and public debt sustainability], *Trésor-Éco*, no. 334, French Treasury, October 2023 (in French).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. and Timbeau, X., "Quelles trajectoires pour les finances publiques de la France ?" [What paths for France's public finances?], *Blog de l'OFCE*, 2025 (in French).
- French Treasury (Direction générale du Trésor), "Finances publiques : une situation dégradée, un redressement nécessaire" [Public finances: a deteriorated situation, a necessary recovery], *Trésor-Éco*, no. 403, September 2026 (in French).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. and Timbeau, X., "Quelles trajectoires pour les finances publiques de la France ?" [What paths for France's public finances?], OFCE working paper no. 13, July 2025 (in French).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## What to take away {#retenir}

The weight of a debt can fall without its amount decreasing, and it has fallen elsewhere: among EU countries that started from higher debt than France, the ratio fell by {{< baisse-val "cmp_exc_baisse_min" >}} to {{< baisse-val "cmp_exc_baisse_max" >}} points in ten years in the {{< baisse-val "cmp_exc_n" >}} that ran an average primary surplus, without their debt in euros decreasing.

In France, over the same decade, interest rates and growth helped: {{< baisse-val "d3_tc_abs" >}} points less, mostly in {{< baisse-val "d3_creux_lib" >}}. Primary deficits weighed more, {{< baisse-val "d3_def_abs" >}} points, and the ratio rose by {{< baisse-val "d3_var_abs" >}} points.

That help has run out: in {{< baisse-val "annee_fin" >}}, the implicit interest rate and nominal growth were almost equal. On those terms, and excluding other adjustments, an unchanged primary balance would push the ratio up by about {{< baisse-val "ecart_dernier" >}} points a year; stabilising it means closing that gap, bringing it down means going further. And, at this level of debt, one additional point of gap between the interest rate and growth would raise the balance to be reached by about {{< baisse-val "sens_pt" >}} points of GDP.

These comparisons say neither which policy would produce this result, nor at what price: the surplus countries had stronger nominal growth than France, and three of them received official financing. Who would bear the adjustment is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [Why does French public debt rise?](/en/why-does-public-debt-rise/)
- [What does French public debt actually cost?](/en/cost-of-french-public-debt/)
- [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- [And elsewhere?](/en/public-debt-international-comparison/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page decomposes the rise in the French debt ratio and the falls observed elsewhere. Bringing that ratio down can shift costs. Who bears them: the taxpayer, the user of public services, the saver through inflation, the creditor through a restructuring? The book takes this analysis further, with official figures, by examining these choices and their consequences.
{{< /appel-livre >}}

## Where these figures come from {#sources}

Eurostat, general government (S.13), ESA 2010 accounts, in national currency: Maastricht debt and nominal GDP as published with the deficit and debt notification (`gov_10dd_edpt1`), interest paid and net lending or borrowing (`gov_10a_main`, D41PAY and B9). The primary balance is the general government balance plus interest paid. The identity is the one set out in [Why does French public debt rise?](/en/why-does-public-debt-rise/#identite); annual terms are cumulated over ten years, from the end of the year before the decade to the end of its last year. A year's stabilising balance is that year's interest-growth effect, excluding other adjustments. Changes and totals are computed before rounding: displayed figures may differ by 0.1 point.

Check: for each country and each year, the calculated debt ratio and primary balance are compared with those Eurostat publishes as a percentage of GDP, which the calculation does not use. Beyond a gap of {{< baisse-val "tolerance" >}} point, the year is excluded and counted ({{< baisse-val "cons_ecartees" >}} out of {{< baisse-val "cons_calculables" >}}, listed in the JSON file); for France and the compared countries, the script stops. A window containing a year of nominal growth above 35% (hyperinflation, series break) is excluded. The countries compared with France are designated by a rule, not chosen: debt above {{< baisse-val "seuil_dette" >}}% of GDP at end-{{< baisse-val "cmp_veille" >}}; the same calculation is redone at 80% and 100%. No figure on this page is entered by hand: all come from the same script, which checks the main quantitative statements and stops if their conditions are no longer met; their wording is reviewed editorially.

{{< reutiliser figures="figures_baisse" jeu="dette_baisse" sources="Eurostat" donnees="The decade-by-decade decomposition of the French debt-to-GDP ratio, the observed and stabilising primary balance (excluding other adjustments) year by year, and the same decomposition for the EU countries that started above 90% of GDP; the same content exists as CSV, in long format." >}}
From {{< baisse-val "d3_debut" >}} to {{< baisse-val "annee_fin" >}}, primary deficits added {{< baisse-val "d3_def_abs" >}} points of GDP to the French debt ratio, the interest-growth effect, concentrated in {{< baisse-val "d3_creux_lib" >}}, took off {{< baisse-val "d3_tc_abs" >}}, and other adjustments added {{< baisse-val "d3_sfa_abs" >}}: a rise of {{< baisse-val "d3_var_abs" >}} points. Among the {{< baisse-val "cmp_n" >}} EU countries that started above {{< baisse-val "seuil_dette" >}}% of debt at end-{{< baisse-val "cmp_veille" >}}, the falls of more than {{< baisse-val "forte_baisse" >}} points are those of the {{< baisse-val "cmp_exc_n" >}} countries with an average primary surplus, a finding that depends on the threshold chosen. This is an accounting decomposition, not a causal attribution.
{{< /reutiliser >}}
