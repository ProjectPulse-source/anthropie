---
title: "Can public debt come down?"
url: /en/can-public-debt-come-down/
description: "The weight of debt in GDP can fall even while its amount rises. In France, from {baisse.d3_debut} to {baisse.annee_fin}, it rose by {baisse.d3_var_abs} points; in {baisse.cmp_exc_n} countries whose debt started from a higher level, it fell markedly, first through growth, then through their primary surpluses."
chapo: "Yes: what can fall is the weight of debt in GDP, even while its amount rises. In Portugal, public debt went from {baisse.cmp_pt_enc0} to {baisse.cmp_pt_enc1} billion euros from end-{baisse.cmp_veille} to end-{baisse.annee_fin}, and its weight from {baisse.cmp_pt_d0}% to {baisse.cmp_pt_d1}% of GDP. In France, it rose by {baisse.d3_var_abs} points over the same period: general government spent more than it took in, even leaving interest aside, and that deficit weighed more than the help from interest rates and growth."
og_title: "Can public debt come down?"
og_image: "images/og-dette-baisse-en.jpg"
og_image_alt: "Share card: “Deficits weighed more” — France, three decades: interest-growth effect, primary deficits and other adjustments, in points of GDP."
date: 2026-10-03
lastmod: 2026-10-11
# English version of part 5 of the public debt dossier (FR: content/dette-publique-peut-elle-baisser/_index.md), a mirror
# requested by the author on 03/10/2026. Same tokens, same keys: values come from the affichage_en block of
# data/dette_baisse.json (scripts/update_dette_baisse.py), whose guards cover both languages.
donnees: [dette_baisse]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_baisse"
  nom: "Can public debt come down: a decade-by-decade decomposition of the debt-to-GDP ratio, France and EU countries whose debt exceeded 90% of GDP"
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
  - question: "Are growth and inflation enough to bring debt down?"
    answer: "They lighten the ratio when nominal growth exceeds the interest rate paid on the debt, and they did most to bring the ratio down in the {baisse.cmp_exc_n} EU countries where it fell markedly, among those whose debt exceeded {baisse.seuil_dette}% of GDP at end-{baisse.cmp_veille}: about twice as much as their primary surpluses. But the effect varies a great deal from year to year: in France, it took off {baisse.d3_creux_abs} points in {baisse.d3_creux_lib} and accounted for {baisse.d3_pic_tc} points in {baisse.d3_pic_annee}. In this group, no country that stayed in average primary deficit saw its ratio fall by {baisse.forte_baisse} points; Slovenia, below the threshold, did."
  - question: "Has France ever run a primary surplus?"
    answer: "{baisse.exc_n_maj} times since {baisse.annee_debut}, from {baisse.exc_premiere} to {baisse.exc_derniere}, at most {baisse.exc_max}% of GDP (Eurostat). Since then, the general government primary balance has been in deficit every year."
  - question: "Does a primary surplus always bring debt down?"
    answer: "It helps reduce the ratio, but the final change also depends on interest rates, growth and other adjustments: in France, the balance reached the stabilising benchmark excluding adjustments in {baisse.suff_hausse} without the ratio falling. In the ten-year windows of the {baisse.eu_pays} current EU members where starting debt exceeded {baisse.seuil_dette}% of GDP, the ratio fell by at least {baisse.forte_baisse} points in {baisse.eu_def_fb} of the {baisse.eu_def_n} windows with a negative average primary balance, in {baisse.eu_mid_fb} of the {baisse.eu_mid_n} with a balance from 0 to under 2%, in {baisse.eu_exc_fb} of the {baisse.eu_exc_n} with a balance of at least 2%; these windows overlap and come from a few countries."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 35
  nature: "Official series (Eurostat) decomposed, and the author's calculations"
---

{{< dossier-dette volet="baisse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Updated: {{< baisse-val "date_donnees" >}}</span> General government, Eurostat series from {{< baisse-val "annee_debut" >}} to {{< baisse-val "annee_fin" >}}. Download: <a href="/dette_baisse.csv">CSV</a> · <a href="/dette_baisse.json">JSON</a> · <a href="#sources">method</a></p>

## The weight of debt, not its amount {#poids-et-montant}

The debt ratio sets what general government owes against the wealth produced in a year, gross domestic product (GDP), measured in current euros, known as nominal GDP. It falls as soon as nominal GDP grows faster than the debt: in Portugal, from end-{{< baisse-val "cmp_veille" >}} to end-{{< baisse-val "annee_fin" >}}, public debt went from {{< baisse-val "cmp_pt_enc0" >}} to {{< baisse-val "cmp_pt_enc1" >}} billion euros while its weight fell from {{< baisse-val "cmp_pt_d0" >}}% to {{< baisse-val "cmp_pt_d1" >}}% of GDP. That fall followed an assistance and adjustment programme whose cost to the Portuguese these series do not measure ([limits](#limites)).

Every year, three terms move this ratio, set out in [Why does French public debt rise?](/en/why-does-public-debt-rise/):

- **interest and growth**: the interest paid pushes the ratio up, nominal GDP growth, in volume and in prices, pulls it down; the page calls the net result "the interest-growth effect";
- **the primary balance**, revenue minus spending excluding interest: a deficit pushes the ratio up, a surplus pulls it down;
- **other adjustments**, known as "stock-flow": acquisitions of assets, changes in cash holdings and other operations that change the debt without going through the deficit.

Changes in the ratio are measured in points of GDP. In {{< baisse-val "annee_fin" >}}, one point is about {{< baisse-val "point_md" >}} billion euros; but contributions cumulated over ten years, each computed on that year's GDP, do not represent sums paid or saved. This decomposition is an accounting one: it says through which channel the ratio moved. Economic conditions (growth, inflation, interest rates) and budget decisions act on several terms at once, and it does not separate them.

## France: three decades, and three years apart {#trois-decennies}

{{< figure-svg fichier="dette-baisse-decennies-en" alt="For each of the last three decades, four bars: the interest-growth effect, the primary balance, other adjustments, and the change in the debt ratio, their sum. Over the last decade, interest and growth pull the ratio down, primary deficits push it up by more." >}}What pushed the French debt-to-GDP ratio up or down, by decade, in points of GDP cumulated (Eurostat). Orange: what pushes it up; grey: what pulls it down; blue: the change, the sum of the three.{{< /figure-svg >}}

<div class="resultat-phrase">

**The finding in one sentence.** From {{< baisse-val "d3_debut" >}} to {{< baisse-val "annee_fin" >}}, primary deficits added {{< baisse-val "d3_def_abs" >}} points to the French debt ratio, the interest-growth effect, concentrated in {{< baisse-val "d3_creux_lib" >}}, took off {{< baisse-val "d3_tc_abs" >}}, and other adjustments added {{< baisse-val "d3_sfa_abs" >}}: the net result is a rise of {{< baisse-val "d3_var_abs" >}} points. This is an accounting decomposition: it says through which term the debt moved, not why the deficits existed.

</div>

**The two previous decades.** From {{< baisse-val "d1_debut" >}} to {{< baisse-val "d2_fin" >}}, the ratio goes from {{< baisse-val "d1_dette_deb" >}}% to {{< baisse-val "d2_dette_fin" >}}% of GDP: the interest-growth effect first pushes the ratio up, with the budget excluding interest close to balance, then primary deficits take over, with the 2008-2009 financial crisis.

<details class="repli"><summary>The two previous decades, term by term</summary>

**{{< baisse-val "d1_lib" >}}: interest and growth push upwards.** The ratio goes from {{< baisse-val "d1_dette_deb" >}}% to {{< baisse-val "d1_dette_fin" >}}% of GDP. The interest-growth effect adds {{< baisse-val "d1_tc_abs" >}} points; the primary balance, in surplus {{< baisse-val "d1_exc" >}} years out of ten, takes off {{< baisse-val "d1_def_abs" >}}.

**{{< baisse-val "d2_lib" >}}: both terms push together.** The ratio gains {{< baisse-val "d2_var_abs" >}} points, the largest rise of the three decades: {{< baisse-val "d2_def_abs" >}} from primary deficits, {{< baisse-val "d2_tc_abs" >}} from the interest-growth effect. The period contains the 2008-2009 financial crisis.

From one decade to the next, the contribution of primary deficits went from {{< baisse-val "d1_def" >}} to {{< baisse-val "d2_def" >}} then {{< baisse-val "d3_def" >}} points. This finding describes a recurrence; it does not say whether these deficits were avoidable, nor which of their two terms, spending or revenue, explains them.

</details>

**{{< baisse-val "d3_lib" >}}: three years of relief, outweighed by deficits.** Over the decade, interest adds {{< baisse-val "d3_interets" >}} points to the ratio and nominal GDP growth erases {{< baisse-val "d3_croissance" >}}: the interest-growth effect is {{< baisse-val "d3_tc" >}} points. This is not a steady advantage. The years {{< baisse-val "d3_creux_lib" >}} alone take off {{< baisse-val "d3_creux_abs" >}} points; the other {{< baisse-val "d3_reste_n" >}} together weigh {{< baisse-val "d3_reste" >}} points, including {{< baisse-val "d3_pic_tc" >}} in {{< baisse-val "d3_pic_annee" >}}, when GDP fell. In {{< baisse-val "d3_creux_rebond" >}}, activity rebounds ({{< baisse-val "d3_creux_rebond_gv" >}}% in volume); in the next two years, nominal growth owes more to prices than to volume. A fall in the ratio through inflation is not an equivalent gain in wealth: inflation higher than expected reduces the real value of fixed payments owed to creditors, a redistributive effect that depends on the indexation of the securities and their maturity. No year of the decade shows a primary surplus: cumulated deficits add {{< baisse-val "d3_def_abs" >}} points, more than the whole rise in the ratio ({{< baisse-val "d3_var" >}}).

## What brought the ratio down elsewhere {#pays-compares}

The same decomposition, over the same decade, applies to the EU countries whose debt exceeded {{< baisse-val "seuil_dette" >}}% of GDP at end-{{< baisse-val "cmp_veille" >}}: France, at {{< baisse-val "cmp_fr_d0" >}}%, and {{< baisse-val "cmp_autres_n" >}} others, all starting from a higher level. This threshold is a presentation convention, close to the French level; it does not make these countries equivalent experiences, and, at 100%, France drops out of the group.

{{< figure-svg fichier="dette-baisse-comparaison-en" alt="For each country in the group, four bars: the interest-growth effect, the primary balance, other adjustments, and the change in the debt ratio, their sum. The interest-growth effect pulls the ratio down everywhere; in the three countries where the ratio fell markedly, it weighs about twice as much as primary surpluses." >}}Interest-growth effect, primary balance and other adjustments, and their sum, the change in the debt ratio, {{< baisse-val "cmp_lib" >}}, in points of GDP cumulated (Eurostat). Countries sorted by change in the ratio.{{< /figure-svg >}}

**Two drivers, in order of weight.** In the {{< baisse-val "cmp_exc_n" >}} countries where the ratio fell markedly, {{< baisse-val "cmp_exc_pays" >}}, the largest accounting contribution comes from interest and growth: {{< baisse-val "cmp_exc_tc_min" >}} to {{< baisse-val "cmp_exc_tc_max" >}} points over ten years, about twice that of their primary surpluses, {{< baisse-val "cmp_exc_sp_min" >}} to {{< baisse-val "cmp_exc_sp_max" >}} points (a ratio of {{< baisse-val "cmp_exc_rapport_min" >}} to {{< baisse-val "cmp_exc_rapport_max" >}}). Both contributions depend on economic conditions, and neither allows the fall to be attributed to a particular policy.

<div class="encadre">

**What is established.** These three falls coincided with an average primary surplus, of {{< baisse-val "cmp_exc_pb_min" >}}% to {{< baisse-val "cmp_exc_pb_max" >}}% of GDP, and the interest-growth effect weighed more in them than the surplus.

**What is not.** That the surpluses caused these falls, or that they were indispensable. Leaving the surpluses aside, the other terms together already pull the ratio down, by {{< baisse-val "cmp_exc_tcsfa_min" >}} to {{< baisse-val "cmp_exc_tcsfa_max" >}} points depending on the country. This does not mean the ratio would have fallen without a surplus, because the terms are not independent: a surplus can slow activity, strong growth swells revenue. But the decomposition cannot, on its own, make the surplus a necessary condition. Slovenia gives an example: starting from debt of {{< baisse-val "s80_exc_d0" >}}% of GDP, below the {{< baisse-val "seuil_dette" >}}% threshold used here, it saw its ratio fall by {{< baisse-val "s80_exc_var" >}} points with an average primary balance of {{< baisse-val "s80_exc_pb" >}}% of GDP.

</div>

**Their implicit interest rate was not lower.** Over the decade, the average implicit interest rate on their debt, interest paid relative to debt, ranges from {{< baisse-val "cmp_exc_ti_min" >}}% to {{< baisse-val "cmp_exc_ti_max" >}}%, against {{< baisse-val "cmp_fr_ti" >}}% in France, the lowest in the group. This indicator concerns the stock: it reflects the history of issuance, its maturity and official loans, and does not say on what terms these countries borrowed on the markets. What sets them apart is nominal GDP growth: {{< baisse-val "cmp_exc_g_min" >}}% to {{< baisse-val "cmp_exc_g_max" >}}% a year on average, against {{< baisse-val "cmp_fr_g" >}}% in France. In volume, it exceeded that of France, at {{< baisse-val "cmp_exc_gv_min" >}}% to {{< baisse-val "cmp_exc_gv_max" >}}% a year against {{< baisse-val "cmp_fr_gv" >}}%; price growth was {{< baisse-val "cmp_exc_gp_min" >}}% to {{< baisse-val "cmp_exc_gp_max" >}}% a year, against {{< baisse-val "cmp_fr_gp" >}}%.

**The level of debt matters too.** The same gap between interest rate and growth takes off more points the higher the ratio. Greece's implicit interest rate is roughly the same as France's ({{< baisse-val "cmp_el_ti" >}}% against {{< baisse-val "cmp_fr_ti" >}}%), and its nominal growth barely exceeds France's ({{< baisse-val "cmp_el_g" >}}% against {{< baisse-val "cmp_fr_g" >}}%): its gap between rate and growth is hardly more favourable ({{< baisse-val "cmp_el_rg" >}} points a year, against {{< baisse-val "cmp_fr_rg" >}}). But its debt, {{< baisse-val "cmp_dm_max" >}}% of GDP on average, the highest in the group, multiplies that gap: the interest-growth effect reaches {{< baisse-val "cmp_el_tc" >}} points there, against {{< baisse-val "cmp_fr_tc" >}} in France. Part of Greek debt has been owed to its European partners since the assistance programmes; these series do not separate the rate on those loans from that on the rest of the debt. The higher the starting debt, the more a given gap between interest rate and growth amplifies the change in the ratio, downwards as well as upwards.

**The other countries in the group.** In France, the ratio rose by {{< baisse-val "d3_var_abs" >}} points, the largest rise in the group, with the highest average primary deficit ({{< baisse-val "cmp_fr_pb" >}}% of GDP); {{< baisse-val "cmp_def_autres" >}}, with an average primary deficit, stayed roughly stable, despite a favourable interest-growth effect. Portugal, Cyprus and Greece received official financing from their European partners and the IMF, Spain assistance to recapitalise its banks (timeline in the folded section below). Seven countries over one decade do not make a general regularity.

<details class="repli"><summary>The {{< baisse-val "cmp_n" >}} countries, term by term, rate by rate, and the assistance programmes</summary>

{{< baisse-tableau >}}

{{< baisse-tableau vue="taux" >}}

The ratio stayed roughly stable for {{< baisse-val "cmp_def_autres" >}} ({{< baisse-val "cmp_def_var_min" >}} to {{< baisse-val "cmp_def_var_max" >}} points), with an average primary deficit, despite a favourable interest-growth effect. In Belgium, the contributions of interest-growth and of the primary balance total {{< baisse-val "cmp_be_tcdef" >}} points; other adjustments add {{< baisse-val "cmp_be_sfa_abs" >}}, bringing the change to {{< baisse-val "cmp_be_var" >}} points.

These countries were not financed on the same terms. Portugal (from 2011 to mid-2014), Cyprus (from April 2013 to March 2016) and Greece (from May 2010 to August 2018, with a last programme, financed by the European Stability Mechanism, from August 2015 to August 2018) received official financing from their European partners and the IMF; Spain received, from July 2012 to January 2014, assistance to recapitalise its banks ([European Commission](https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries_en); [European Stability Mechanism](https://www.esm.europa.eu/assistance/greece/greece-successfully-concludes-esm-programme)). The restructuring of Greek debt, in 2012, predates the decade studied.

Lowering the threshold to 80% brings {{< baisse-val "s80_ajouts" >}} into the group.

</details>

## What primary balance would stabilise the debt? {#solde-stabilisant}

In a given year, and excluding other adjustments, the ratio does not move if the primary balance exactly offsets that year's interest-growth effect. This balance, called stabilising, is the grey line; the balance actually observed is the orange line.

{{< figure-svg fichier="dette-baisse-stabilisant-en" alt="Two annual lines over thirty years, as a percentage of GDP: the observed primary balance and the balance that would have stabilised the debt ratio, which jumps in the year GDP fell and plunges in the year of the rebound; in the last year, a dotted line marks the gap between the two." >}}Observed primary balance and the primary balance that would have stabilised the debt ratio within the year, excluding other adjustments, France, in % of GDP (Eurostat, author's calculation).{{< /figure-svg >}}

**Why the marker changes from year to year.** It depends on the gap between the implicit interest rate and nominal growth, multiplied by the level of debt. In {{< baisse-val "stab_max_annee" >}}, nominal GDP fell: stabilising the ratio would have taken a primary balance of {{< baisse-val "stab_max" >}}% of GDP, a surplus. In {{< baisse-val "stab_min_annee" >}}, it rebounded: a balance of {{< baisse-val "stab_min" >}}%, hence a deficit, would have kept it stable. These swings do not measure a change in budget discipline: growth is what moved.

**In {{< baisse-val "annee_fin" >}}.** The implicit interest rate ({{< baisse-val "taux_implicite_dernier" >}}%) and nominal growth ({{< baisse-val "croissance_derniere" >}}%) were almost equal: the marker was close to zero. The observed balance was {{< baisse-val "pb_dernier" >}}% of GDP, a gap of {{< baisse-val "ecart_dernier" >}} points, about {{< baisse-val "ecart_md" >}} billion euros relative to {{< baisse-val "annee_fin" >}} GDP ({{< baisse-val "pib_dernier_md" >}} billion), computed on the gap before rounding. It is an accounting gap observed for that year, at that year's interest rates and growth and excluding other adjustments: it changes every year with them, and it says neither which spending nor which revenue should move. It would also narrow through growth: at this level of debt, and with the interest rate unchanged, each additional point of nominal growth would lower the balance that stabilises the ratio by about {{< baisse-val "sens_pt" >}} points. This is a property of the identity, for a given debt and interest rate; it does not say that a point of growth is as easy to obtain, or as cheap, as a budget adjustment.

<details class="repli"><summary>The marker, year by year, and French surpluses</summary>

Over {{< baisse-val "annees_total" >}} years, the observed balance reached or exceeded this marker in {{< baisse-val "suffisant_n" >}} years. The ratio actually fell in {{< baisse-val "suff_baisse_n" >}} of those years; in {{< baisse-val "suff_hausse" >}}, it rose all the same, because of other adjustments. France has run a primary surplus only {{< baisse-val "exc_n" >}} times, from {{< baisse-val "exc_premiere" >}} to {{< baisse-val "exc_derniere" >}}, at most {{< baisse-val "exc_max" >}}% of GDP.

</details>

Stabilising the ratio and bringing it down are two distinct objectives. An adjustment amount is read with its objective, its horizon and its assumptions; the marker calculated here for {{< baisse-val "annee_fin" >}} holds for that year and does not allow the multi-year estimates of institutions to be assessed.

## Is French public debt sustainable? {#soutenable}

No level of debt, on its own, settles this question. A debt is called sustainable when the State can service and refinance it without a budgetary adjustment beyond reach; that depends on its primary balance, on the gap between the interest rate it pays and nominal growth, and on the confidence of those who lend to it. The first two terms are measured here; the third is not.

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

- **Measuring debt.** A fall in the ratio does not mean the amount of debt has decreased. The debt tracked is gross: other adjustments mix asset purchases, loans and valuation changes, and a country that borrows to acquire assets sees its gross debt rise without its financial position deteriorating by as much.
- **Economic interpretation.** An accounting decomposition, not a causal one: the terms depend on one another, and the observed balance contains the economic cycle; it does not measure an effort. The growth used is nominal; splitting it into volume and prices is an accounting step that does not identify the separate contribution of each. Nothing here says which of spending or revenue should move.
- **Cost of adjustment.** These series measure neither unemployment, nor wages, nor public services, nor the consequences of the adjustment programmes followed by Greece, Portugal or Cyprus: a large fall in the ratio is not, in itself, an economic and social success. Who bears an adjustment is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- **Scope of comparison.** The 27 current EU members, since {{< baisse-val "eu_premiere" >}}; nothing before, nothing outside the Union. The group compared depends on the debt threshold and the decade chosen. {{< baisse-val "cons_ecartees_maj" >}} country-years out of {{< baisse-val "cons_calculables" >}} are excluded by the check described below.
- **Reach in time.** The page describes thirty observed years. The paths forecast by the Government, the European Commission or the IMF are conditional scenarios, which these data can neither confirm nor rule out.

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="the stabilising balance and the distinction between stabilising and reducing are found again; reading the last year's zero gap as a lasting state, or the surplus as the only driver of falls, is challenged" >}}
**Measured here.** The decade-by-decade decomposition of the French ratio, the stabilising balance year by year and the comparison of EU countries whose debt exceeded {{< baisse-val "seuil_dette" >}}% of GDP, on Eurostat series. None of the texts read calculates these quantities on this source and these periods: they are validated by reproduction.

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

<p class="retenir__surtitre">Summary</p>

## What to take away {#retenir}

The weight of a debt can fall without its amount decreasing: in Portugal, debt went from {{< baisse-val "cmp_pt_enc0" >}} to {{< baisse-val "cmp_pt_enc1" >}} billion euros in ten years while its weight fell from {{< baisse-val "cmp_pt_d0" >}}% to {{< baisse-val "cmp_pt_d1" >}}% of GDP.

Among EU countries whose debt started from a higher level than France's, the ratio fell markedly in {{< baisse-val "cmp_exc_n" >}} of them: {{< baisse-val "cmp_exc_pays" >}}. The largest contribution there comes from interest and growth, about twice that of their primary surpluses. Their average implicit interest rate was not lower than France's: their nominal growth was stronger. Slovenia, below the threshold used, reduced its ratio without a surplus.

In France, over the same decade, interest and growth took {{< baisse-val "d3_tc_abs" >}} points off the ratio, thanks to the years {{< baisse-val "d3_creux_lib" >}}; primary deficits added {{< baisse-val "d3_def_abs" >}}, and the ratio rose by {{< baisse-val "d3_var_abs" >}} points.

In {{< baisse-val "annee_fin" >}}, the implicit interest rate and nominal growth were almost equal: the observed primary balance was {{< baisse-val "ecart_dernier" >}} points of GDP, about {{< baisse-val "ecart_md" >}} billion euros, below the marker that would have stabilised the ratio that year, excluding other adjustments. This marker changes every year with interest rates and growth; at this level of debt, one point of gap between interest rate and growth shifts it by about {{< baisse-val "sens_pt" >}} points of GDP, in either direction.

None of the combinations observed is a transferable recipe: these comparisons say neither which policy would bring about a fall, nor at what price, nor who would pay it. That last point is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

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

Eurostat, general government (S.13), ESA 2010 accounts, in national currency: Maastricht debt and nominal GDP as published with the deficit and debt notification (`gov_10dd_edpt1`), interest paid and net lending or borrowing (`gov_10a_main`, D41PAY and B9); GDP in volume (`nama_10_gdp`, chain-linked volumes), to split nominal growth into volume and prices. The primary balance is the general government balance plus interest paid. The identity is the one set out in [Why does French public debt rise?](/en/why-does-public-debt-rise/#identite); annual terms are cumulated over ten years, from the end of the year before the decade to the end of its last year. A year's stabilising balance is that year's interest-growth effect, excluding other adjustments. Changes and totals are computed before rounding: displayed figures may differ by 0.1 points.

Check: for each country and each year, the calculated debt ratio and primary balance are compared with those Eurostat publishes as a percentage of GDP, which the calculation does not use. Beyond a gap of {{< baisse-val "tolerance" >}} points, the year is excluded and counted ({{< baisse-val "cons_ecartees" >}} out of {{< baisse-val "cons_calculables" >}}, listed in the JSON file); for France and the compared countries, the script stops. A window containing a year of nominal growth above 35% (hyperinflation, series break) is excluded. The countries compared with France are designated by a rule, not chosen: debt above {{< baisse-val "seuil_dette" >}}% of GDP at end-{{< baisse-val "cmp_veille" >}}; the same calculation is redone at 80% and 100%. The figures computed from Eurostat series all come from the same script, which checks the main quantitative statements and stops if their conditions are no longer met; their wording is reviewed editorially. Figures attributed to the French Treasury, the Conseil d'analyse économique and the OFCE are given as they publish them.

{{< reutiliser figures="figures_baisse" jeu="dette_baisse" sources="Eurostat" donnees="The decade-by-decade decomposition of the French debt-to-GDP ratio, the observed and stabilising primary balance (excluding other adjustments) year by year, and the same decomposition for the EU countries whose debt exceeded 90% of GDP; the same content exists as CSV, in long format." >}}
From {{< baisse-val "d3_debut" >}} to {{< baisse-val "annee_fin" >}}, primary deficits added {{< baisse-val "d3_def_abs" >}} points of GDP to the French debt ratio, the interest-growth effect, concentrated in {{< baisse-val "d3_creux_lib" >}}, took off {{< baisse-val "d3_tc_abs" >}}, and other adjustments added {{< baisse-val "d3_sfa_abs" >}}: a rise of {{< baisse-val "d3_var_abs" >}} points. Among the {{< baisse-val "cmp_n" >}} EU countries whose debt exceeded {{< baisse-val "seuil_dette" >}}% of GDP at end-{{< baisse-val "cmp_veille" >}}, the ratio fell markedly in {{< baisse-val "cmp_exc_n" >}}, first through the interest-growth effect, about twice as strong as that of their primary surpluses. This is an accounting decomposition, not a causal attribution.
{{< /reutiliser >}}
