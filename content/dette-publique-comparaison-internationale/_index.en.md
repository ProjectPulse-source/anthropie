---
title: "Public debt: why 100% of GDP does not weigh the same everywhere"
url: /en/public-debt-international-comparison/
description: "Same debt, different burden: in the European Union, the price of public debt does not follow its level. Stock, rates and revenue compared across 27 countries and beyond Europe."
chapo: "At almost equal debt levels, {monde.j_haut_le} devotes {monde.j_haut_charge} of its public revenue to interest; {monde.j_bas_le}, {monde.j_bas_charge}. The stock alone therefore cannot measure what a public debt weighs: one must also look at its price, the revenue available to service it and the speed at which new financing conditions pass through."
og_title: "Public debt: what 100% of GDP does not tell you"
og_image: "images/og-dette-monde-en.jpg"
og_image_alt: "Share card: “Same debt, different burden” — the 27 European Union countries, debt as a % of GDP and interest as a % of revenue; two countries with similar debt are linked, one paying more than three times as much as the other."
date: 2026-09-30
lastmod: 2026-09-30
# English version of part 3 of the public debt file (FR: content/dette-publique-comparaison-internationale/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/dette_monde.json.
donnees: [dette_monde]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html); tokens resolved at build time
  jeu: "dette_monde"
  nom: "Public debt compared: stock, price, revenue and interest burden in the European Union and beyond Europe"
  description: "Compilation derived automatically from official series, with no value copied by hand: the 27 European Union countries in {monde.annee} (Eurostat, strictly comparable); advanced economies outside the EU (OECD, with caveats); major emerging economies (IMF and World Bank, indicative). Exact identity checked for each European country: interest / revenue = starting stock × implicit interest rate ÷ revenue. 10-year yield spreads against Germany since 1995."
  couverture_temporelle: "1995/{monde.annee}"
  couverture_spatiale: "European Union, OECD advanced economies and major emerging economies"
  variables:
    - {nom: "Public debt stock", unite: "% of GDP", description: "gross debt / GDP; starting stock (end of previous year) for the decomposition"}
    - {nom: "Price of debt (implicit interest rate)", unite: "% per year", description: "the year's interest / debt at the end of the previous year"}
    - {nom: "Interest burden", unite: "% of public revenue"}
    - {nom: "10-year yield spread against Germany", unite: "percentage points"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/irt_lt_mcby_a/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_aind/default/table?lang=fr"
    - "https://data-explorer.oecd.org/"
    - "https://www.imf.org/external/datamapper/GGXWDG_NGDP@WEO"
    - "https://data.worldbank.org/indicator/GC.XPN.INTP.RV.ZS"
  mots: ["public debt", "international comparison", "European Union", "implicit interest rate", "interest burden", "Eurostat", "OECD", "IMF"]
  fichiers: ["dette_monde.csv", "dette_monde.json"]
faq:
  - question: "Is France more indebted than other countries?"
    answer: "More than most: at the end of {monde.annee}, its public debt stands at {monde.fr_stock_fin} of GDP, the third highest in the European Union after Greece and Italy (Eurostat, Maastricht debt). But the level of the debt does not say what it costs: in {monde.annee}, France devoted {monde.fr_charge} of its public revenue to interest, less than {monde.n_plus_charges_moins_endettes} countries that are nonetheless less indebted ({monde.plus_charges_moins_endettes})."
  - question: "Does France's debt cost it more than its neighbours' debt costs them?"
    answer: "Not systematically. In {monde.annee}, its implicit interest rate — the year's interest divided by debt at the end of {monde.annee_1} — is {monde.fr_prix}, close to the euro area average ({monde.prix_moyen_euro}): some countries pay less, notably Germany ({monde.de_prix}), others more. The 10-year yield exceeds this implicit rate by {monde.fr_ecart_taux}, and {monde.fr_part_1an} of the debt matures within the year: if financing conditions remained above the cost of the debt being replaced, refinancing would push this average cost up."
  - question: "Why don't two equally indebted countries pay the same interest?"
    answer: "Because the burden depends on three terms: the debt stock, the price at which it was financed and the revenue available to service it. In {monde.annee}, {monde.j_bas_le} ({monde.j_bas_stock} of GDP) and {monde.j_haut_le} ({monde.j_haut_stock}) have similar debts; yet the second devotes {monde.j_rapport} times more of its revenue to interest: it pays {monde.j_haut_prix} on its stock against {monde.j_bas_prix}, and its revenue amounts to {monde.j_haut_rec} of GDP against {monde.j_bas_rec}."
  - question: "Does the euro lower the cost of debt?"
    answer: "Not automatically. Before 1999, yield spreads against Germany melted away in the future euro countries, but also in Sweden, which never joined. In 2012, the most fragile members broke away (Greece was borrowing at {monde.ec_el_2012} points above Germany), more than any country that stayed outside; the easing followed the ECB's interventions. In {monde.annee}, Sweden and Denmark borrow at 10 years more cheaply than Germany, France more expensively. On its debt stock, Sweden pays {monde.se_prix}, like Germany ({monde.de_prix}). The euro removes exchange-rate risk between its members; it does not guarantee them the German rate."
  - question: "Does high debt necessarily lead to a crisis?"
    answer: "These data do not make it possible to estimate the risk of a crisis. They show only that the same level of debt can correspond to very different current burdens. The risk of a crisis also depends on growth, the primary balance, the structure of creditors, the currency, maturities, public assets and financial conditions."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 30
  nature: "Official series compared (Eurostat, OECD, IMF, World Bank) and the author's calculations"
---

{{< dossier-dette volet="3" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Updated: {{< monde-val "date_donnees" >}}</span> The {{< monde-val "n_pays" >}} countries of the European Union, main data {{< monde-val "annee" >}}; outside Europe, the vintage is given country by country. Download: <a href="/dette_monde.csv">CSV</a> · <a href="/dette_monde.json">JSON</a> · <a href="#sources">method</a></p>

The debt-to-GDP ratio is the most quoted figure in any comparison of public finances, and on its own it does not say what a debt costs. This page sets France alongside the other members of the European Union and a few economies beyond Europe, and asks what the ratio leaves out.

## Same debt, different burden {#meme-dette}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-charge-en.svg" alt="Scatter plot: on the horizontal axis, debt as a share of GDP; on the vertical axis, interest as a percentage of public revenue, for the 27 European Union countries. Euro area countries line up along a gently sloping line; countries outside the euro area, led by Hungary, Romania and Poland, sit well above it for comparable debt." width="720" height="488" loading="lazy">
  <figcaption>Starting stock (debt at the end of {{< monde-val "annee_1" >}} / GDP {{< monde-val "annee" >}}) and burden (interest / revenue), {{< monde-val "annee" >}}. The dotted lines link the false twins picked out by a rule set before the calculation: for each country, its nearest neighbour in stock; pairs less than 10 points apart; the three largest gaps in burden.</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** At similar levels of debt, the share of revenue absorbed by interest can vary from 1 to {{< monde-val "j_rapport" >}}: the stock is not enough to determine the burden, because it fixes neither the price of the debt nor the level of public revenue.

</div>

The stock is not unrelated to the burden: ranked by debt and by burden, countries fall into a similar order (rank correlation of {{< monde-val "spearman" >}}). But it accounts for only part of the dispersion (R² = {{< monde-val "r2_charge_stock" >}}), and the figure shows why. **Within the euro area, the stock accounts for most of the burden** (R² = {{< monde-val "r2_euro" >}} across {{< monde-val "n_euro" >}} countries); the same holds among the {{< monde-val "n_hors" >}} countries outside the euro area (R² = {{< monde-val "r2_hors" >}}). But the two groups do not follow the same line: outside the euro, the burden rises much faster with debt, in particular because the most indebted countries there also pay more. The slope does not depend on any single country: removing each of the seven in turn, it stays between {{< monde-val "pente_hors_loo_min" >}} and {{< monde-val "pente_hors_loo_max" >}}.

France illustrates the other side: with debt of {{< monde-val "fr_stock" >}} of GDP at the start of the year, it devoted **{{< monde-val "fr_charge" >}} of its revenue** to interest in {{< monde-val "annee" >}}, less than {{< monde-val "n_plus_charges_moins_endettes" >}} less indebted countries: {{< monde-val "plus_charges_moins_endettes" >}}.

## Why? One equation, four measures {#quatre-mesures}

<div class="equation" role="group" aria-label="The debt burden decomposed into three terms">
  <p class="equation__titre">What debt weighs on public revenue depends on three things</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>the debt</b><small>starting stock, % of GDP</small></span>
    <span class="equation__op" aria-label="multiplied by">×</span>
    <span class="equation__terme"><b>its average cost</b><small>price: implicit interest rate</small></span>
    <span class="equation__op" aria-label="divided by">÷</span>
    <span class="equation__terme"><b>public revenue</b><small>% of GDP</small></span>
    <span class="equation__op" aria-label="equals">=</span>
    <span class="equation__terme equation__terme--resultat"><b>the burden</b><small>interest as % of revenue</small></span>
  </div>
  <p class="equation__exacte">Exact identity, checked for each country: interest / revenue = (debt at the end of the previous year / GDP) × (interest / debt at the end of the previous year) ÷ (revenue / GDP)</p>
</div>

- **The stock**: public debt relative to GDP, the most quoted figure. It is read at two dates: the **starting stock** (debt at the end of the previous year, relative to the year's GDP) explains the year's interest — it is the one used in the figure and the opening; the **closing stock** (debt at the end of the year) is used for the ranking further down.
- **The price**: the implicit interest rate, that is, the interest paid in a year divided by the debt at the end of the previous year. It measures the average cost of the stock, not the rate at which a State borrows today. Eurostat also publishes an "apparent cost", based on the year's average debt: the two conventions are close but not identical.
- **The burden**: the share of general government revenue devoted to paying interest.
- **Transmission**: the speed at which new financing conditions pass through to the average cost of the stock, depending on the share of the debt maturing and the gap between the market rate and the implicit rate.

For the same starting stock, in this accounting identity, two countries can differ in burden through only two terms: the price of their stock or the level of their revenue.

## Price and revenue {#prix-et-recettes}

**The price does not follow the stock.** In the European Union in {{< monde-val "annee" >}}, the linear relationship between the starting stock and the implicit interest rate is practically nil (R² = {{< monde-val "r2_prix_stock" >}}): over one year and across countries, the level of debt does not predict its price, which does not mean it never has an effect on it. Italy, heavily indebted, pays an implicit rate close to that of countries with much lower debt, and France pays **{{< monde-val "fr_prix" >}}**, in line with the euro area average ({{< monde-val "prix_moyen_euro" >}}).

**Revenue matters too.** At the same price, a State that collects a smaller share of its national income devotes a larger share of its revenue to interest. These are the two terms that separate the false twins: {{< monde-val "j_haut_le" >}} pays {{< monde-val "j_haut_prix" >}} on its stock against {{< monde-val "j_bas_prix" >}} for {{< monde-val "j_bas_le" >}}, and its revenue amounts to {{< monde-val "j_haut_rec" >}} of GDP against {{< monde-val "j_bas_rec" >}}.

{{< dette-monde-tableau niveau="europe" repli="See the 27 countries: stock, price, revenue and burden" >}}

### The price of debt and recent inflation {#prix-et-inflation}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-prix-en.svg" alt="Scatter plot: on the horizontal axis, average inflation over the previous three years; on the vertical axis, the implicit interest rate on the debt. High-inflation countries outside the euro area, Romania, Hungary, Poland, pay the most; the Baltic states, in the euro area, experienced high inflation without paying much; Sweden pays like Germany." width="720" height="488" loading="lazy">
  <figcaption>Implicit interest rate on the debt ({{< monde-val "annee" >}}) and average inflation over the previous three years (harmonised index of consumer prices, Eurostat). A descriptive relationship over one year.</figcaption>
</figure>

**Outside the euro area, the implicit interest rate is closely associated with recent inflation** (R² = {{< monde-val "r2_prix_inflation_hors" >}}); **within the euro area, much less so** (R² = {{< monde-val "r2_prix_inflation_euro" >}}): the Baltic states experienced high inflation without paying much. Currency membership is not the whole story either: **Sweden, outside the euro, pays {{< monde-val "se_prix" >}}**, like Germany. Over a single year and from one country to another, these data show that the level of a public debt is not enough to predict its price; they say neither that the euro makes it cheaper, nor the opposite.

<details class="repli"><summary>The regression and its robustness</summary>

In a descriptive regression, average inflation over the previous three years and euro area membership together account for a large part of the observed dispersion (R² = {{< monde-val "r2_prix_euro_inflation" >}}). The coefficient associated with the euro area is −{{< monde-val "effet_euro" >}} points, that associated with one additional point of average inflation +{{< monde-val "effet_inflation" >}} points. These coefficients do not measure causal effects, and the three-year window is a choice: with average inflation over two, four or five years, their sign does not change and their order of magnitude holds (from −{{< monde-val "rob_euro_min" >}} to −{{< monde-val "rob_euro_max" >}} points for the euro area, from +{{< monde-val "rob_infl_min" >}} to +{{< monde-val "rob_infl_max" >}} points per point of inflation, R² from {{< monde-val "rob_r2_min" >}} to {{< monde-val "rob_r2_max" >}}).

</details>

<aside class="encadre encadre--euro">

### Is a common currency enough to set the price? Thirty years of spreads against Germany {#euro-et-taux}

No, judging by thirty years of 10-year yields compared with Germany's, with countries that stayed outside the euro as controls. Before 1999, the Italian spread shrinks from {{< monde-val "ec_it_1995" >}} to {{< monde-val "ec_it_1998" >}} points, but so does Sweden's, from {{< monde-val "ec_se_1995" >}} to {{< monde-val "ec_se_1998" >}}: the convergence is not specific to the euro. In 2012, Greece borrows at {{< monde-val "ec_el_2012" >}} points above Germany and Portugal at {{< monde-val "ec_pt_2012" >}}, more than any country that stayed outside; the easing then follows the ECB's interventions. In {{< monde-val "annee" >}}, Sweden and Denmark borrow more cheaply than Germany, France {{< monde-val "ec_fr_an" >}} points more expensively. **The euro removed exchange-rate risk between its members; it did not guarantee them the German rate.**

<details class="repli"><summary>See the thirty years of data and how to read them</summary>

This is the 10-year market yield, not the implicit rate on the stock.

{{< dette-monde-tableau niveau="ecarts" >}}

**Before the euro, spreads melt away, including outside the euro.** From 1995 to 1998, the Italian spread goes from {{< monde-val "ec_it_1995" >}} to {{< monde-val "ec_it_1998" >}} points, the Spanish spread from {{< monde-val "ec_es_1995" >}} to {{< monde-val "ec_es_1998" >}}. Sweden's, which never adopted the euro, goes over the same period from {{< monde-val "ec_se_1995" >}} to {{< monde-val "ec_se_1998" >}}. The prospect of joining the euro may have played a part for the future members, but these figures do not make it possible to isolate its share.

**In 2012, the euro does not protect its most fragile members.** Greece then borrows at {{< monde-val "ec_el_2012" >}} points above Germany, Portugal at {{< monde-val "ec_pt_2012" >}}, Ireland at {{< monde-val "ec_ie_2012" >}}, Spain at {{< monde-val "ec_es_2012" >}}, Italy at {{< monde-val "ec_it_2012" >}}. Outside the euro, Sweden stays at {{< monde-val "ec_se_2012" >}} points above Germany and Denmark at {{< monde-val "ec_dk_2012" >}} points below; but Hungary pays {{< monde-val "ec_hu_2012" >}} points: keeping one's own currency did not protect everyone. No country that stayed outside the euro, however, reaches the Greek and Portuguese levels, those of States borrowing in a currency whose issuance they no longer controlled. The spreads close only after the ECB's commitment, in the summer of 2012, to defend the euro, and then its massive purchases of government bonds from 2015: the easing follows a central bank decision, which can change, and not euro membership, which already existed in 2012.

**Today, staying outside the euro does not necessarily cost more.** In {{< monde-val "annee" >}}, Sweden borrows at 10 years {{< monde-val "ec_se_an" >}} points **below** Germany, Denmark {{< monde-val "ec_dk_an" >}} points below; France pays {{< monde-val "ec_fr_an" >}} points more than Germany, Italy {{< monde-val "ec_it_an" >}}. Outside the euro, Poland and Hungary pay much more ({{< monde-val "ec_pl_an" >}} and {{< monde-val "ec_hu_an" >}} points), but their recent inflation is also much higher; and since Sweden too is outside the euro, it is not the currency that separates them from it.

</details>

</aside>

## Transmission: a pressure gauge, not a forecast {#transmission}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-transmission-en.svg" alt="Scatter plot: on the horizontal axis, the share of the debt maturing within the year; on the vertical axis, the gap between the 10-year yield and the implicit interest rate on the stock. France is among the countries where the market yield most exceeds the implicit rate; Sweden and Portugal have a much larger share of their debt maturing in under a year; in Denmark, the 10-year yield is below the implicit rate." width="720" height="488" loading="lazy">
  <figcaption>Share of the debt maturing within the year (Eurostat, debt by residual maturity) and gap between the harmonised 10-year yield and the implicit interest rate on the stock, {{< monde-val "annee" >}}. A transmission gauge, not a forecast.</figcaption>
</figure>

A given year's implicit interest rate covers debt issued at different dates: it catches up with market conditions only as the debt is refinanced. Two measures locate this inertia: the share of the debt maturing within the year, and the gap between the harmonised 10-year yield and the implicit rate. Neither is a forecast: a State does not borrow only at 10 years, and today's yield is not tomorrow's.

**In France, {{< monde-val "fr_part_1an" >}} of the debt outstanding at the end of {{< monde-val "annee" >}} has a residual maturity of less than one year. In {{< monde-val "annee" >}}, the harmonised 10-year yield ({{< monde-val "fr_taux10" >}}) was {{< monde-val "fr_ecart_taux" >}} above the implicit interest rate on the stock.** If financing conditions remained above the cost of the debt being replaced, refinancing would put upward pressure on the average cost — the mechanism detailed on the page [What does French public debt actually cost?](/en/cost-of-french-public-debt/). In Denmark, the gauge points the other way: the 10-year yield is below the implicit rate on the stock ({{< monde-val "dk_ecart_taux" >}}).

## The stock: a ranking that does not tell the whole story {#stock}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-stock-en.svg" alt="Horizontal bars of public debt as a percentage of GDP, end of {{< monde-val "annee" >}}, for the 27 European Union countries, from Greece, the most indebted, to Estonia; France is third, at {{< monde-val "fr_stock_fin" >}}." width="720" height="543" loading="lazy">
  <figcaption>Closing stock: Eurostat, Maastricht gross debt of general government, end of {{< monde-val "annee" >}}. In blue, the euro area; in orange, countries outside the euro area.</figcaption>
</figure>

At the end of {{< monde-val "annee" >}}, France has the {{< monde-val "fr_rang_stock" >}} highest public debt in the European Union, at **{{< monde-val "fr_stock_fin" >}} of GDP**. This is the ranking most comparisons use. It measures a gross stock, without public assets or commitments that are not debt, such as future pensions; and, as we have seen, it does not say what this debt costs.

## And outside Europe? {#hors-europe}

Outside the European Union, the data are no longer harmonised. For advanced economies, the OECD (*Economic Outlook*) allows a similar calculation on a broader basis, gross financial liabilities rather than Maastricht debt; the ratio of interest to these liabilities is therefore not exactly the European implicit interest rate. France is included, on the same basis, as a benchmark. Three cases serve as laboratories.

{{< dette-monde-cas >}}

**Japan** owes, on this basis, nearly twice as much as France, but its interest-to-liabilities ratio is {{< monde-val "jpn_prix" >}} against {{< monde-val "fra_prix" >}}, and it devotes less of its revenue to interest ({{< monde-val "jpn_charge" >}} against {{< monde-val "fra_charge" >}}). **Switzerland**, with its own currency, pays little on a small debt, and its financial assets exceed its liabilities. **The United States**, with liabilities close to France's, devotes {{< monde-val "usa_fra_rapport" >}} times the French share of its revenue to interest.

{{< dette-monde-tableau niveau="avances" repli="See all advanced economies (OECD)" >}}

<details class="repli"><summary>The major emerging economies: China, India, Brazil, South Africa (indicative data)</summary>

Only indicative measures exist: debt according to the IMF, and interest of the central government alone according to the World Bank, always taken in the same year. India devotes {{< monde-val "ind_charge" >}} of its central government revenue to interest, Brazil {{< monde-val "bra_charge" >}}, South Africa {{< monde-val "zaf_charge" >}}, for debts of {{< monde-val "ind_stock" >}}, {{< monde-val "bra_stock" >}} and {{< monde-val "zaf_stock" >}} of GDP according to the IMF, in {{< monde-val "ind_charge_annee" >}}, {{< monde-val "bra_charge_annee" >}} and {{< monde-val "zaf_charge_annee" >}}, the latest years published by the World Bank. Part of the gap comes from the price paid, another from the relative weakness of revenue: without harmonised data, the two cannot be separated.

{{< dette-monde-tableau niveau="emergents" >}}

</details>

<aside class="encadre">

**And to know whether the debt will rise?** This page compares what debt costs today. The question of its trajectory is a different one: a debt ratio tends to rise when the interest rate paid exceeds the nominal growth of the economy and the budget, excluding interest, remains in deficit. This gap between rates and growth is the subject of a separate analysis.

</aside>

## What these data do not say {#limites}

- **A single year.** The relationships described concern {{< monde-val "annee" >}}; they say nothing about their stability over time.
- **Correlations, not causes.** A regression across {{< monde-val "n_pays" >}} countries describes an association. Euro membership and past inflation are, moreover, linked to each other.
- **A gross stock.** Maastricht debt does not deduct public assets; Switzerland, whose net financial liabilities are negative, shows how much this gap matters.
- **Similar definitions, not identical ones.** Outside Europe, the OECD measures gross financial liabilities, the IMF gross debt, the World Bank the interest of central government alone.
- **The risk of a crisis.** It also depends on growth, the primary balance, the currency, maturities and creditors: this page does not measure it.
- **The holders of the debt.** Central bank, non-residents, domestic savers: their shares change the risk and the cost of a debt, and will be the subject of a separate analysis.
- **Commitments outside debt**, such as future pensions, enter none of these figures.

{{< confrontation-recherche verifie="2026-09-30" publie="oui" >}}
**Measured here.** Over one year and across the {{< monde-val "n_pays" >}} countries of the Union, the absence of a linear relationship between the starting stock and the implicit interest rate; thirty years of 10-year yield spreads against Germany. Calculations on official series, which are validated by reproduction: none of the texts read measures the implicit rate in a cross-section.

**Consistent with.** In their cross-sectional charts, Gruber and Kamin find no apparent relationship between debt and long-term rates across 19 OECD countries; in bond issues from 1999 to 2005, the debt ratio no longer explains the yield spreads of euro members (Bernoth, von Hagen and Schuknecht). The page's caveat also holds: estimated on variation within each country, projected debt raises long-term rates by a few basis points per point of GDP (Gruber and Kamin; Laubach, on expected US rates). On the euro, De Grauwe and Ji estimate that in 2010-2011 a large part of the rise in the spreads of peripheral countries is not explained by their fiscal fundamentals, a part that varies by country, Greece being the exception; Saka, Fuertes and Kalotychou, who put this hypothesis to the test, find that the significant contagion coming from Spain before the ECB's announcement of 26 July 2012 disappears afterwards. From 1993 to 1997, the yields of all EU countries except Greece, including those outside the euro, converge towards German and US levels (Bernoth, von Hagen and Schuknecht).

**Challenged by.** Any reading of the absence of a cross-sectional link as an absence of effect: Gruber and Kamin attribute it to an omitted variable, the solvency that markets ascribe to each State; De Grauwe and Ji find in the euro area, after 2008, a significant and non-linear relationship; before 1999, the relative level of debt predicted the spread at issuance, afterwards it was the weight of debt service in revenue (Bernoth, von Hagen and Schuknecht). Hence the page's wording: the level is **not enough** to predict the price. An overly broad reading of 2012: credit default swap premiums fall everywhere after the announcement, outside the euro included; the study establishes the end of contagion, not that all of the easing came from the ECB, and its authors interpret their results as supportive of its programme.

**Not established.** The link between the price of debt and past inflation outside the euro: Gruber and Kamin relate long-term rates to projected inflation, not to current inflation. The euro's own share in the convergence before 1999: Bernoth, von Hagen and Schuknecht compare bonds issued in the same currency, with no exchange-rate risk, and do not separate future members from countries that stayed outside.

**References read**

- Gruber, J. and Kamin, S., "Fiscal Positions and Government Bond Yields in OECD Countries", Federal Reserve, International Finance Discussion Paper 1011, 2010.
- Bernoth, K., von Hagen, J. and Schuknecht, L., "Sovereign Risk Premiums in the European Government Bond Market", revised version, May 2006 (published in the *Journal of International Money and Finance*, 31(5), 2012).
- De Grauwe, P. and Ji, Y., "Self-Fulfilling Crises in the Eurozone: An Empirical Test", CEPS Working Document no. 367, 2012 (published in the *Journal of International Money and Finance*, 34, 2013).
- Saka, O., Fuertes, A.-M. and Kalotychou, E., "ECB Policy and Eurozone Fragility: Was De Grauwe Right?", CEPS Working Document no. 397, 2014 (published in the *Journal of International Money and Finance*, 54, 2015).
- Laubach, T., "New Evidence on the Interest Rate Effects of Budget Deficits and Debt", Finance and Economics Discussion Series 2003-12, Federal Reserve (published, revised, in the *Journal of the European Economic Association*, 7(4), 2009).
{{< /confrontation-recherche >}}

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt file** — [What does French public debt actually cost?](/en/cost-of-french-public-debt/) · [Who really pays for public debt?](/en/who-really-pays-public-debt/)

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page measures what debt costs, and why the same debt does not weigh the same everywhere. It does not say who bears its cost. The book follows that shift channel by channel — taxpayer, saver, public services, generations not yet old enough to vote —, on official figures, to show in which configurations each bears a cost. By the end you will have a method for identifying who bears what, depending on the decision taken. The book, on the French case, exists in French only.
{{< /appel-livre >}}

## Where these figures come from {#sources}

**Europe (strictly comparable)** — Eurostat, general government (S.13), national accounts ESA 2010, amounts in national currency: interest paid and revenue (`gov_10a_main`, D41PAY and TR), Maastricht debt (`gov_10dd_edpt1`), GDP (`nama_10_gdp`), debt by residual maturity (`gov_10dd_ggd`), 10-year yields (`irt_lt_mcby_a`), harmonised index of consumer prices (`prc_hicp_aind`).

**Advanced economies outside the EU (with caveats)** — OECD, *Economic Outlook*: gross interest, revenue, GDP and gross financial liabilities of general government.

**Major emerging economies (indicative)** — IMF, *World Economic Outlook* (general government gross debt); World Bank, *World Development Indicators* (interest as a % of central government revenue).

The calculations, statistics and figures are produced by a single script, re-run with each release of the sources; no figure on this page is entered by hand. **Download the data** (CC BY 4.0 licence): [CSV](/dette_monde.csv), one row per country, readable in a spreadsheet; [JSON](/dette_monde.json), with the statistics and definitions. Method: the burden, the stock and the price satisfy the exact identity given above, using debt at the end of the previous year (the ECB's implicit interest rate convention, distinct from Eurostat's "apparent cost", based on average debt); the robustness of the coefficients is recalculated at each update over inflation windows of two to five years; the statistics are simple, descriptive least squares.

{{< reutiliser figures="figures_monde" jeu="dette_monde" sources="Eurostat, OECD, IMF and World Bank" donnees="The 27 European Union countries and the economies outside Europe, with their levels of comparability, their definitions and their statistics; the same content is available as CSV, one row per country, readable in a spreadsheet." >}}
This page compares what a public debt represents through four measures: the stock, its price, the revenue that services it and the speed at which new rates pass through. In the European Union in {{< monde-val "annee" >}}, two countries with similar debt can devote shares of their revenue to interest ranging from 1 to {{< monde-val "j_rapport" >}}, and the price of debt has no linear relationship with its level. These relationships describe one year and associations, not causes; they do not measure the risk of a crisis.
{{< /reutiliser >}}
