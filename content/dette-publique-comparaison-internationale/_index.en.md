---
title: "Public debt: why 100% of GDP does not carry the same burden everywhere"
url: /en/public-debt-international-comparison/
description: "Same debt, different burden: in the European Union, the average interest cost of public debt does not follow its level. Stock, rates and revenue compared across 27 countries and beyond Europe."
chapo: "In {monde.annee}, at almost equal debt levels, {monde.j_haut_le} devotes {monde.j_haut_charge} of its public revenue to interest; {monde.j_bas_le}, {monde.j_bas_charge}. The stock alone therefore cannot measure what a public debt weighs: one must also look at its average interest cost, the revenue available to service it, and the weight of old borrowing in what it costs today."
og_title: "Public debt: what 100% of GDP does not tell you"
og_image: "images/og-dette-monde-en.jpg"
og_image_alt: "Share card: “Same debt, different burden” — the 27 European Union countries, debt as a % of GDP and interest as a % of revenue; two countries with similar debt are linked, one paying more than three times as much as the other."
date: 2026-09-30
lastmod: 2026-10-11
# English version of part 3 of the public debt dossier (FR: content/dette-publique-comparaison-internationale/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/dette_monde.json.
donnees: [dette_monde]
journal:  # révisions qui changent la lecture de la page (partials/page-date-visible.html affiche la plus récente)
  - {date: 2026-10-16, texte: "Correction: as a share of GDP, interest puts France seventh in the Union, tied with Belgium, not eighth; four less indebted countries exceed it, not five."}
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html); tokens resolved at build time
  jeu: "dette_monde"
  nom: "Public debt compared: stock, average interest cost, revenue and interest burden in the European Union and beyond Europe"
  description: "Compilation derived automatically from official series, with no value copied by hand: the 27 European Union countries in {monde.annee} (Eurostat, strictly comparable); advanced economies outside the EU (OECD, with caveats); major emerging economies (IMF and World Bank, indicative). Exact identity checked for each European country: interest / revenue = starting stock × implicit interest rate ÷ revenue. 10-year yield spreads against Germany since 1995."
  couverture_temporelle: "1995/{monde.annee}"
  couverture_spatiale: "European Union, OECD advanced economies and major emerging economies"
  variables:
    - {nom: "Public debt stock", unite: "% of GDP", description: "gross debt / GDP; starting stock (end of previous year) for the decomposition"}
    - {nom: "Average interest cost (implicit interest rate)", unite: "% per year", description: "the year's interest / debt at the end of the previous year"}
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
    answer: "More than most: at the end of {monde.annee}, its public debt stands at {monde.fr_stock_fin} of GDP, the third highest in the European Union after Greece and Italy (Eurostat, Maastricht debt). But the level of the debt does not say what it costs: in {monde.annee}, France devoted {monde.fr_charge} of its public revenue to interest, less than {monde.n_plus_charges_moins_endettes_mots} countries that are nonetheless less indebted ({monde.plus_charges_moins_endettes}). Relative to GDP, its interest ({monde.fr_ipib}) puts it in {monde.fr_rang_ipib} place{monde.fr_egal_ipib}, and only {monde.n_plus_ipib_mots} less indebted countries rank above it: its public revenue, the {monde.fr_rang_recettes} highest in the Union, makes the first measure more favourable without changing the amount paid."
  - question: "Does France pay more to service its debt than its neighbours?"
    answer: "Not systematically. In {monde.annee}, its implicit interest rate — the year's interest divided by debt at the end of {monde.annee_1} — is {monde.fr_prix}, slightly below the simple average of euro-area countries ({monde.prix_moyen_euro}): some countries pay less, notably Germany ({monde.de_prix}), others more. The 10-year yield exceeds this implicit rate by {monde.fr_ecart_taux}, and {monde.fr_part_1an} of the debt matures within the year: if financing conditions remained above the cost of the debt being replaced, refinancing would push this average cost up."
  - question: "Does the euro lower the cost of debt?"
    answer: "Not automatically. Before 1999, yield spreads against Germany narrowed sharply in the future euro countries, but also in Sweden, which never joined. In 2012, spreads widened sharply for the most vulnerable members (Greece was borrowing at {monde.ec_el_2012} points above Germany), more than any country that stayed outside; the ECB's interventions contributed to the easing that followed. In {monde.annee}, Sweden and Denmark borrow more cheaply than Germany at 10 years, France more expensively. On its debt stock, Sweden pays {monde.se_prix}, like Germany ({monde.de_prix}). The euro removes exchange-rate risk between its members; it does not guarantee them the German rate."
  - question: "Does high debt necessarily lead to a crisis?"
    answer: "These data do not make it possible to estimate the risk of a crisis. They show only that the same level of debt can correspond to very different current burdens. The risk of a crisis also depends on growth, the primary balance, the structure of creditors, the currency, maturities, public assets and financial conditions."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  livres: ["dette-publique-qui-paie-vraiment"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 30
  nature: "Official series compared (Eurostat, OECD, IMF, World Bank) and the author's calculations"
---

{{< dossier-dette volet="3" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data last updated {{< monde-val "date_donnees" >}}</span> The {{< monde-val "n_pays" >}} countries of the European Union, main data {{< monde-val "annee" >}}; outside Europe, the vintage is given country by country. Download: <a href="/dette_monde.csv">CSV</a> · <a href="/dette_monde.json">JSON</a> · <a href="#sources">method</a></p>

The debt-to-GDP ratio is one of the most widely quoted figures in public-finance comparisons, and on its own it does not say what a debt costs. This page sets France alongside the other members of the European Union and a few economies beyond Europe, and asks what the ratio leaves out.

## Same debt, different burden {#meme-dette}

{{< figure-svg fichier="dette-monde-charge-en" alt="Scatter plot: debt relative to GDP on the horizontal axis, interest as a percentage of public revenue on the vertical axis, for the 27 European Union countries. Euro-area countries, blue circles, line up along a gently sloping line; countries outside the euro area, orange squares, led by Hungary, Romania and Poland, sit well above it for comparable debt." >}}Starting stock (debt at end-{{< monde-val "annee_1" >}} / {{< monde-val "annee" >}} GDP) and burden (interest / revenue), {{< monde-val "annee" >}}. Dotted lines link the "look-alike pairs", two countries with similar debt whose burden differs most, picked out by a rule set before the calculation: for each country, its nearest neighbour by debt stock; pairs less than 10 percentage points apart; the three largest gaps in burden. Groups as in the data year: Bulgaria, outside the euro area in {{< monde-val "annee" >}}, joined it on {{< monde-val "bg_entree" >}}.{{< /figure-svg >}}

<div class="resultat-phrase">

**The result in one sentence.** In {{< monde-val "annee" >}}, at similar debt levels, the share of revenue absorbed by interest can differ by a factor of {{< monde-val "j_rapport" >}}: the stock does not determine the burden, because it sets neither the average interest cost of the debt nor the level of public revenue.

</div>

**Why does {{< monde-val "j_haut_le" >}} pay {{< monde-val "j_rapport" >}} times as much as {{< monde-val "j_bas_le" >}}?** Not because of its debt: relative to GDP, it is only {{< monde-val "j_f_stock" >}} times higher. The average rate paid on that debt is {{< monde-val "j_f_prix" >}} times higher ({{< monde-val "j_haut_prix" >}} against {{< monde-val "j_bas_prix" >}}), and its lower public revenue ({{< monde-val "j_haut_rec" >}} of GDP against {{< monde-val "j_bas_rec" >}}) adds a further factor of {{< monde-val "j_f_rec" >}}: {{< monde-val "j_f_stock" >}} × {{< monde-val "j_f_prix" >}} × {{< monde-val "j_f_rec" >}} does give {{< monde-val "j_rapport" >}}. Most of the gap therefore comes from the price of the debt. This calculation says what contributes arithmetically to the gap, not why {{< monde-val "j_haut_le" >}} finances itself at that rate.

**Two groups, two lines.** In {{< monde-val "annee" >}}, among the {{< monde-val "n_hors_mots" >}} EU countries that remained outside the euro area, the relationship between debt and interest burden is {{< monde-val "pente_rapport" >}} times steeper than among the {{< monde-val "n_euro_mots" >}} euro-area members. This is an association between countries observed in the same year, not a rate of change over time. It reflects in particular the high financing costs of some of these countries, and does not measure an effect of the common currency: the countries outside the euro do not form a homogeneous monetary regime, some keeping a fixed parity with the euro (Denmark, and Bulgaria until it joined), others letting their currency float.

<details class="repli"><summary>The figure's statistics: a relationship partly expected by construction, two lines that depend on no single country taken alone</summary>

Ranked by debt and by burden, the countries fall in a similar order (rank correlation of {{< monde-val "spearman" >}}); the stock accounts for only part of the dispersion of the burden (R² = {{< monde-val "r2_charge_stock" >}}). Within each group, it accounts for more: R² = {{< monde-val "r2_euro" >}} across the {{< monde-val "n_euro_mots" >}} euro-area countries, {{< monde-val "r2_hors" >}} across the {{< monde-val "n_hors_mots" >}} others. Part of this relationship is expected by construction: the burden is the stock multiplied by the price and divided by revenue, so that with similar prices and revenue it tracks the stock. What the figure adds is the heterogeneity of prices and revenue across countries. The slope outside the euro area depends on no single country: when each of the {{< monde-val "n_hors_mots" >}} countries is removed in turn, it stays between {{< monde-val "pente_hors_loo_min" >}} and {{< monde-val "pente_hors_loo_max" >}}. This test says nothing about the collective weight of the countries that pay the most.

</details>

## France: two readings of the same burden {#france-deux-lectures}

**Depending on the measure, France looks better or worse placed.** In {{< monde-val "annee" >}}, interest on its debt amounts to **{{< monde-val "fr_ipib" >}} of GDP** and **{{< monde-val "fr_charge" >}} of public revenue**. Relative to revenue, it is lower than in {{< monde-val "n_plus_charges_moins_endettes_mots" >}} countries that are nonetheless less indebted ({{< monde-val "plus_charges_moins_endettes" >}}); relative to GDP, it puts France in {{< monde-val "fr_rang_ipib" >}} place in the Union{{< monde-val "fr_egal_ipib" >}}, and only {{< monde-val "n_plus_ipib_mots" >}} less indebted countries rank above it ({{< monde-val "plus_ipib" >}}). The gap between the two readings comes from French public revenue, which amounts to {{< monde-val "fr_recettes" >}} of GDP, the {{< monde-val "fr_rang_recettes" >}} highest share in the Union. Changing the denominator changes France's relative position, not the amount of interest it pays. High revenue mechanically lowers the ratio of interest to revenue; on its own, it says neither whether more could be levied nor which spending the interest displaces. The first ratio measures the burden relative to the wealth produced; the second, the share of public resources absorbed by interest. Neither, on its own, measures sustainability.

**Two figures for French debt are in circulation.** {{< monde-val "fr_stock_fin" >}} of GDP, debt at the end of {{< monde-val "annee" >}}: the one used in rankings. {{< monde-val "fr_stock" >}}, debt at the end of {{< monde-val "annee_1" >}} relative to {{< monde-val "annee" >}} GDP: the starting stock, used as the denominator of the year's implicit interest rate, and the one in the figure.

<details class="repli"><summary>Why the gap between these two figures is not the rise in the ratio over one year</summary>

The {{< monde-val "fr_ecart_stocks" >}} points between the two figures measure the rise of the debt in euros during {{< monde-val "annee" >}}, relative to the same GDP. The debt ratio, by contrast, is computed each year on that year's GDP: it stood at {{< monde-val "fr_stock_fin_prec" >}} at the end of {{< monde-val "annee_1" >}} and rose by {{< monde-val "fr_var_ratio" >}} points in {{< monde-val "annee" >}}. A third figure is a market price: the 10-year yield ({{< monde-val "fr_taux10" >}}), which is neither the average cost of debt already issued nor necessarily that of future borrowing.

</details>

## Why? One equation, three terms {#quatre-mesures}

<div class="equation" role="group" aria-label="The debt burden broken down into three terms">
  <p class="equation__titre">What the debt weighs on public revenue depends on three terms</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>the debt</b><small>starting stock, % of GDP</small></span>
    <span class="equation__op" aria-label="multiplied by">×</span>
    <span class="equation__terme"><b>its average cost</b><small>price: implicit interest rate</small></span>
    <span class="equation__op" aria-label="divided by">÷</span>
    <span class="equation__terme"><b>public revenue</b><small>% of GDP</small></span>
    <span class="equation__op" aria-label="equals">=</span>
    <span class="equation__terme equation__terme--resultat"><b>the burden</b><small>interest as a % of revenue</small></span>
  </div>
  <p class="equation__exacte">Exact identity, checked for every country: interest / revenue = (debt at end of previous year / GDP) × (interest / debt at end of previous year) ÷ (revenue / GDP)</p>
</div>

The **price** is the implicit interest rate: the interest paid in a year divided by the debt at the end of the previous year. It measures the average cost of the stock, not the rate at which a government borrows today; Eurostat also publishes an "apparent cost", based on the year's average debt, close but not identical. With the same starting stock, two countries can differ in burden only through their price or their revenue. One mechanism adds to this over time, **transmission**: old borrowing continues to weigh on today's cost, and is replaced only as it matures.

## Cost and revenue {#prix-et-recettes}

**The price does not follow the stock.** In the European Union in {{< monde-val "annee" >}}, the level of debt does not predict its price (R² = {{< monde-val "r2_prix_stock" >}}), which does not mean it never affects it. Italy, heavily indebted, pays an implicit interest rate close to that of far less indebted countries, and France pays **{{< monde-val "fr_prix" >}}**, slightly below the simple average of euro-area countries ({{< monde-val "prix_moyen_euro" >}}): the {{< monde-val "fr_rang_prix_euro" >}} lowest rate out of {{< monde-val "n_euro_mots" >}}.

**Revenue matters too.** At the same price, a government that collects a smaller share of national income devotes a larger share of its revenue to interest: this is the third factor in the gap between {{< monde-val "j_haut_le" >}} and {{< monde-val "j_bas_le" >}}, and the reason for the two readings of the French burden.

{{< dette-monde-tableau niveau="europe" repli="See the 27 countries: stock, cost, revenue and burden" >}}

### Average interest cost and recent inflation {#prix-et-inflation}

{{< figure-svg fichier="dette-monde-prix-en" alt="Scatter plot: average inflation over the three previous years on the horizontal axis, the implicit interest rate on the debt on the vertical axis. High-inflation countries outside the euro area, Romania, Hungary, Poland, pay the most; the Baltic states, in the euro area, saw high inflation without paying much; Sweden pays like Germany." >}}Implicit interest rate on the debt ({{< monde-val "annee" >}}) and average inflation over the three previous years (harmonised index of consumer prices, Eurostat). Descriptive relationship over one year.{{< /figure-svg >}}

**Outside the euro area, the implicit interest rate is closely associated with recent inflation** (R² = {{< monde-val "r2_prix_inflation_hors" >}}); **within the euro area, much less so** (R² = {{< monde-val "r2_prix_inflation_euro" >}}): the Baltic states saw high inflation without paying much. Monetary membership is not enough either: **Sweden, outside the euro, pays {{< monde-val "se_prix" >}}**, like Germany. These data describe one year and a set of countries; they say neither that the euro makes debt cheaper nor the opposite. Nor do they allow a "real" rate to be calculated: subtracting past inflation from an average rate paid on borrowing taken out at various dates measures neither the real return to creditors nor the erosion of the debt.

<details class="repli"><summary>Descriptive regression: −{{< monde-val "effet_euro_pts" >}} for the euro area, +{{< monde-val "effet_inflation_pts" >}} per point of inflation, stable from one window to the next — associations, not causal effects</summary>

In a descriptive regression, average inflation over the three previous years and euro-area membership together account for a large share of the observed dispersion (R² = {{< monde-val "r2_prix_euro_inflation" >}}). The coefficient on euro-area membership is −{{< monde-val "effet_euro_pts" >}}, that on one additional point of average inflation +{{< monde-val "effet_inflation_pts" >}}. These coefficients do not measure causal effects, and the three-year window is a choice: with average inflation over two, four or five years, their sign does not change and their order of magnitude holds (from −{{< monde-val "rob_euro_min" >}} to −{{< monde-val "rob_euro_max_pts" >}} for the euro area, from +{{< monde-val "rob_infl_min" >}} to +{{< monde-val "rob_infl_max_pts" >}} per point of inflation, R² from {{< monde-val "rob_r2_min" >}} to {{< monde-val "rob_r2_max" >}}).

</details>

## Is a common currency enough to set borrowing costs? Thirty years of spreads against Germany {#euro-et-taux}

{{< figure-svg fichier="dette-monde-ecarts-en" alt="Lines showing 10-year yield spreads over Germany from 1995 to today, for Greece, Italy, Portugal and France, euro-area members, and for Sweden and Hungary, which stayed outside. Before 1999, all spreads narrow, Sweden included; in 2010-2013, those of the fragile members surge, Greece going off the scale; they then narrow. Today Sweden borrows below Germany, Hungary well above." >}}10-year convergence yields, Eurostat. Market rates, not the implicit interest rate on the stock; the countries outside the euro are comparators, not a control group.{{< /figure-svg >}}

No, judging by thirty years of 10-year rates compared with Germany's. **Before 1999, convergence was not specific to the euro**: the Italian spread narrows from {{< monde-val "ec_it_1995" >}} to {{< monde-val "ec_it_1998_pts" >}}, but so does Sweden's, from {{< monde-val "ec_se_1995" >}} to {{< monde-val "ec_se_1998" >}}, although it would not adopt the common currency. **In 2012, the common currency does not guarantee convergence**: Greece borrows at {{< monde-val "ec_el_2012" >}} points above Germany, Portugal at {{< monde-val "ec_pt_2012" >}}, more than any country that stayed outside; the ECB's interventions from summer 2012 contributed to narrowing the spreads, though their role cannot be isolated from the other factors of the period. **Today, the euro's border does not separate those who borrow expensively from the others**: Sweden and Denmark borrow more cheaply than Germany, France {{< monde-val "ec_fr_an_pts" >}} more, Hungary {{< monde-val "ec_hu_an" >}} points. **The euro removed exchange-rate risk between its members; it did not guarantee them the German rate.** The Swedish case refutes the idea that adopting the euro alone explains the convergence; it does not measure what the euro brought to those who adopted it.

<details class="repli"><summary>The series: convergence before 1999, outside the euro too; the fragile members' break in 2012; narrowing after 2012</summary>

{{< dette-monde-tableau niveau="ecarts" >}}

**Before the euro, spreads narrow, including outside the euro.** From 1995 to 1998, the Italian spread falls from {{< monde-val "ec_it_1995" >}} to {{< monde-val "ec_it_1998_pts" >}}, the Spanish spread from {{< monde-val "ec_es_1995" >}} to {{< monde-val "ec_es_1998" >}}. Sweden's falls over the same period from {{< monde-val "ec_se_1995" >}} to {{< monde-val "ec_se_1998" >}}. The prospect of joining the euro may have weighed for the future members, but these figures do not allow its share to be isolated.

**In 2012, the euro does not protect its most fragile members.** Greece then borrows at {{< monde-val "ec_el_2012" >}} points above Germany, Portugal at {{< monde-val "ec_pt_2012" >}}, Ireland at {{< monde-val "ec_ie_2012" >}}, Spain at {{< monde-val "ec_es_2012" >}}, Italy at {{< monde-val "ec_it_2012" >}}. Outside the euro, Sweden stays {{< monde-val "ec_se_2012_pts" >}} above Germany and Denmark {{< monde-val "ec_dk_2012_pts" >}} below; but Hungary pays {{< monde-val "ec_hu_2012" >}} points: keeping one's own currency did not protect everyone. No country that stayed outside the euro reaches the Greek and Portuguese levels, however, those of states borrowing in a currency whose issuance they no longer controlled. Spreads narrow after the ECB's commitment, in summer 2012, to defend the euro, then with its large-scale purchases of government bonds from 2015: these interventions contributed, though their role cannot be isolated from the other factors of the period (the Greek restructuring, European support mechanisms, the perceived risk of exit from the euro). Euro membership, by contrast, was already in place in 2012.

**Today, staying outside the euro is not necessarily more expensive.** In {{< monde-val "annee" >}}, Sweden's 10-year yield is {{< monde-val "ec_se_an_pts" >}} **below** Germany's, Denmark's {{< monde-val "ec_dk_an_pts" >}} below; France pays {{< monde-val "ec_fr_an_pts" >}} more than Germany, Italy {{< monde-val "ec_it_an" >}}. Outside the euro, Poland and Hungary pay much more ({{< monde-val "ec_pl_an" >}} and {{< monde-val "ec_hu_an" >}} points), but their recent inflation is also much higher; and since Sweden too is outside the euro, it is not euro membership that separates them from Sweden.

</details>

## How long can the advantage last? {#transmission}

{{< figure-svg fichier="dette-monde-transmission-en" alt="Scatter plot: the share of debt maturing within the year on the horizontal axis, the gap between the 10-year yield and the implicit interest rate on the stock on the vertical axis. France is among the countries where the market yield most exceeds the implicit rate; Sweden and Portugal have a much larger share of their debt maturing within a year; in Denmark, the 10-year yield is below the implicit rate." >}}Share of debt maturing within the year (Eurostat, debt by residual maturity) and gap between the harmonised 10-year yield and the implicit interest rate on the stock, {{< monde-val "annee" >}}. A pressure gauge, not a forecast.{{< /figure-svg >}}

A year's implicit interest rate pays for debt issued at different dates: it only moves towards market conditions as debt is refinanced. Two measures capture this inertia: the share of debt maturing within the year, and the gap between the harmonised 10-year yield and the implicit rate. Neither is a forecast: a government does not borrow only at 10 years, today's yield is not tomorrow's, and debt maturing within a year does not exhaust future financing needs, to which future deficits and successive rollovers of short-term debt are added.

**In France, {{< monde-val "fr_part_1an" >}} of the debt outstanding at the end of {{< monde-val "annee" >}} has a residual maturity of less than one year, and the 10-year yield exceeds the implicit interest rate on the stock by {{< monde-val "fr_ecart_taux" >}}.** If financing conditions remained above the cost of the debt being replaced, each refinancing would bring the price of the stock closer to the market price: interest could rise with unchanged debt. Its share of revenue would not necessarily rise, if revenue grew too. The mechanism is set out on the page [What does French public debt actually cost?](/en/cost-of-french-public-debt/) In Denmark, the indicator points the other way: the 10-year yield is below the implicit interest rate on the stock ({{< monde-val "dk_ecart_taux" >}}).

## The stock: a ranking that does not tell the whole story {#stock}

{{< figure-svg fichier="dette-monde-stock-en" alt="Horizontal bars of public debt as a percentage of GDP, at the end of the year, for the 27 European Union countries, from Greece, the most indebted, to Estonia; France is third." >}}Closing stock: Eurostat, Maastricht gross debt of general government, end-{{< monde-val "annee" >}}. In blue, the euro area; in orange, countries outside the euro area.{{< /figure-svg >}}

At the end of {{< monde-val "annee" >}}, France is the {{< monde-val "fr_rang_stock" >}} most indebted country in the European Union, at **{{< monde-val "fr_stock_fin" >}} of GDP**. This is the ranking most comparisons use. It measures a gross stock, excluding public assets and liabilities that are not debt, such as future pensions; and it says neither the price paid on that debt nor the share of revenue it absorbs.

## And outside Europe? {#hors-europe}

Outside the European Union, the data are no longer harmonised. For advanced economies, the OECD (*Economic Outlook*) allows a similar calculation on a broader basis, gross financial liabilities rather than Maastricht debt; the ratio of interest to these liabilities is therefore not exactly the European implicit interest rate. France is included, on the same basis, as a benchmark: its interest there amounts to {{< monde-val "fra_charge" >}} of its revenue, against {{< monde-val "fr_charge" >}} according to Eurostat, because the scopes differ. Three cases help the comparison.

{{< dette-monde-cas >}}

**Japan's** gross financial liabilities are, relative to GDP, nearly twice France's, but its interest-to-liabilities ratio is {{< monde-val "jpn_prix" >}} against {{< monde-val "fra_prix" >}}, and it devotes less of its revenue to interest ({{< monde-val "jpn_charge" >}} against {{< monde-val "fra_charge" >}}). **Switzerland**, with its own currency, pays little on a small debt, and its financial assets exceed its liabilities. **The United States**, with liabilities close to France's, devotes a share of its revenue to interest equal to {{< monde-val "usa_fra_rapport" >}} times France's.

{{< dette-monde-tableau niveau="avances" repli="See all advanced economies (OECD)" >}}

<details class="repli"><summary>Major emerging economies (indicative): India devotes {{< monde-val "ind_charge" >}} of its central government revenue to interest, Brazil {{< monde-val "bra_charge" >}} — average cost and weak revenue cannot be separated without harmonised data</summary>

Only indicative measures exist: debt according to the IMF, and central-government interest payments only according to the World Bank, always taken in the same year. India devotes {{< monde-val "ind_charge" >}} of its central government revenue to interest, Brazil {{< monde-val "bra_charge" >}}, South Africa {{< monde-val "zaf_charge" >}}, for debts of {{< monde-val "ind_stock" >}}, {{< monde-val "bra_stock" >}} and {{< monde-val "zaf_stock" >}} of GDP according to the IMF, respectively in {{< monde-val "ind_charge_annee" >}}, {{< monde-val "bra_charge_annee" >}} and {{< monde-val "zaf_charge_annee" >}}, the latest years published by the World Bank. Part of the gap comes from the average interest cost, another from the relative weakness of revenue: without harmonised data, the two cannot be separated.

{{< dette-monde-tableau niveau="emergents" >}}

</details>

## What these data do not say {#limites}

- **A one-year cross-section.** The comparisons of stock, price and burden cover {{< monde-val "annee" >}}; only the yield spreads against Germany cover thirty years.
- **Correlations, not causes.** A regression across {{< monde-val "n_pays" >}} countries describes an association. Euro membership and past inflation are, moreover, related to each other.
- **A gross stock.** Maastricht debt does not deduct public assets; Switzerland, whose net financial liabilities are negative, shows how much this matters.
- **Similar, not identical, definitions.** Outside Europe, the OECD measures gross financial liabilities, the IMF gross debt, the World Bank central-government interest only.
- **The risk of a crisis.** It also depends on growth, the primary balance, the currency, maturities and creditors: this page does not measure it.
- **The holders of the debt.** Central bank, non-residents, domestic savers: their share changes the risk and the cost of a debt; what is known for France is examined on the page [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- **Liabilities outside debt**, such as future pensions, are not included in any of these figures.

{{< confrontation-recherche verifie="2026-09-30" publie="oui" resume="the absence of a cross-sectional link is found elsewhere too; reading it as an absence of effect is contradicted over time and in times of crisis" >}}
**Measured here.** Over one year and across the {{< monde-val "n_pays" >}} countries of the Union, the absence of a linear relationship between the starting stock and the implicit interest rate; thirty years of 10-year yield spreads against Germany. Calculations from official series that can be independently reproduced: none of the texts read measures the implicit rate in a cross-section.

**Consistent with.** In their cross-sectional charts, Gruber and Kamin find no apparent relationship between debt and long-term rates across 19 OECD countries; in bond issues from 1999 to 2005, the debt ratio no longer explains the yield spreads of euro members (Bernoth, von Hagen and Schuknecht). The page's caveat also holds: in estimates based on variation within each country, projected debt raises long-term rates by a few basis points per point of GDP (Gruber and Kamin; Laubach, on expected US rates). On the euro, De Grauwe and Ji estimate that in 2010-2011 a large part of the rise in the spreads of peripheral countries is not explained by their fiscal fundamentals, a part that varies by country, Greece being the exception; Saka, Fuertes and Kalotychou, who put this hypothesis to the test, find that the significant contagion coming from Spain before the ECB's announcement of 26 July 2012 disappears afterwards. From 1993 to 1997, the yields of all EU countries except Greece, including those outside the euro, converge towards German and US levels (Bernoth, von Hagen and Schuknecht).

**Challenged by.** Any reading of the absence of a cross-sectional link as an absence of effect: Gruber and Kamin attribute it to an omitted variable, the solvency that markets ascribe to each State; De Grauwe and Ji find in the euro area, after 2008, a significant and non-linear relationship; before 1999, the relative level of debt predicted the spread at issuance, afterwards it was the weight of debt service in revenue (Bernoth, von Hagen and Schuknecht). Hence the page's wording: the level is **not enough** to predict the average interest cost. An overly broad reading of 2012: credit default swap premiums fall everywhere after the announcement, including outside the euro; the study establishes the end of contagion, not that all of the easing came from the ECB, and its authors interpret their results as supportive of its programme.

**Not established.** The link between the implicit interest rate and past inflation outside the euro: Gruber and Kamin relate long-term rates to projected inflation, not to current inflation. The euro's own share in the convergence before 1999: Bernoth, von Hagen and Schuknecht compare bonds issued in the same currency, with no exchange-rate risk, and do not separate future members from countries that stayed outside.

**References read**

- Gruber, J. and Kamin, S., "Fiscal Positions and Government Bond Yields in OECD Countries", Federal Reserve, International Finance Discussion Paper 1011, 2010.
- Bernoth, K., von Hagen, J. and Schuknecht, L., "Sovereign Risk Premiums in the European Government Bond Market", revised version, May 2006 (published in the *Journal of International Money and Finance*, 31(5), 2012).
- De Grauwe, P. and Ji, Y., "Self-Fulfilling Crises in the Eurozone: An Empirical Test", CEPS Working Document no. 367, 2012 (published in the *Journal of International Money and Finance*, 34, 2013).
- Saka, O., Fuertes, A.-M. and Kalotychou, E., "ECB Policy and Eurozone Fragility: Was De Grauwe Right?", CEPS Working Document no. 397, 2014 (published in the *Journal of International Money and Finance*, 54, 2015).
- Laubach, T., "New Evidence on the Interest Rate Effects of Budget Deficits and Debt", Finance and Economics Discussion Series 2003-12, Federal Reserve (published, revised, in the *Journal of the European Economic Association*, 7(4), 2009).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Summary</p>

## What to take away {#retenir}

**The level of a debt does not, on its own, say what it weighs.** In the Union, at similar debt levels, the share of revenue absorbed by interest varies by a factor of {{< monde-val "j_rapport" >}}; between {{< monde-val "j_haut_le" >}} and {{< monde-val "j_bas_le" >}}, most of the gap comes from the price paid on the debt, not from its level.

**France's position depends on the measure.** With the {{< monde-val "fr_rang_stock" >}} highest debt in the Union, at {{< monde-val "fr_stock_fin" >}} of GDP, it pays an implicit interest rate slightly below the simple euro-area average and devotes {{< monde-val "fr_charge" >}} of its revenue to interest, but {{< monde-val "fr_ipib" >}} of its GDP: public revenue among the highest in the Union makes the first measure more favourable than the second. And this position has a horizon: if the market yield stayed above the average cost, refinancing would bring the two closer, without the debt needing to grow.

**A common currency does not set the price.** The euro removed exchange-rate risk between its members, not the yield spread: convergence before 1999 also reached Sweden, which stayed outside; in 2012, Greece was borrowing at {{< monde-val "ec_el_2012" >}} points above Germany, and the ECB's interventions contributed to the easing that followed, among other factors.

What remains is the trajectory: the same level of debt can rise or fall depending on the gap between interest rates and growth and on the primary balance. That is the subject of [Can public debt come down?](/en/can-public-debt-come-down/)

</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [Why does French public debt rise?](/en/why-does-public-debt-rise/)
- [What does French public debt actually cost?](/en/cost-of-french-public-debt/)
- [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- [Can it come down?](/en/can-public-debt-come-down/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page measures what debt costs, and why the same debt does not carry the same burden everywhere. It does not say who bears its cost. The book follows that shift channel by channel — taxpayer, saver, public services, generations not yet old enough to vote — on official figures, to show in which configurations each bears a cost. It offers a three-question method — are the facts established, does the system keep its promise, who decides — and, for the outcomes it considers, the split between who pays and who gains. The book, on the French case, exists in French only.
{{< /appel-livre >}}

## Where these figures come from {#sources}

**Europe (strictly comparable)** — Eurostat, general government (S.13), national accounts ESA 2010, amounts in national currency: interest paid and revenue (`gov_10a_main`, D41PAY and TR), Maastricht debt (`gov_10dd_edpt1`), GDP (`nama_10_gdp`), debt by residual maturity (`gov_10dd_ggd`), 10-year yields (`irt_lt_mcby_a`), harmonised index of consumer prices (`prc_hicp_aind`).

The working paper [AWP-09](/en/awp/awp-09/) uses the charge identity and these yield spreads, with countries that stayed outside the euro as comparison groups, to test the narrative that the euro made interest rates converge.

**Advanced economies outside the EU (with caveats)** — OECD, *Economic Outlook*: gross interest, revenue, GDP and gross financial liabilities of general government.

**Major emerging economies (indicative)** — IMF, *World Economic Outlook* (general government gross debt); World Bank, *World Development Indicators* (interest as a % of central government revenue).

Debt stocks are those of Eurostat's annual series (`gov_10dd_edpt1`) as retrieved on the date shown at the top of the page; quarterly data, published at other dates, may differ slightly from them, as on the page [What does French public debt actually cost?](/en/cost-of-french-public-debt/), drawn from INSEE's quarterly series. The calculations, statistics and figures are produced by a single script, re-run with each release of the sources; every computed figure comes from official series, and figures from the studies cited are given as they publish them. **Download the data** (CC BY 4.0 licence): [CSV](/dette_monde.csv), one row per country, readable in a spreadsheet; [JSON](/dette_monde.json), with the statistics and definitions. Method: the burden, the stock and the implicit interest rate satisfy the exact identity given above, using debt at the end of the previous year (the ECB's implicit interest rate convention, distinct from Eurostat's "apparent cost", based on average debt); the robustness of the coefficients is recalculated at each update over inflation windows of two to five years; the statistics are simple, descriptive least squares.

{{< reutiliser figures="figures_monde" jeu="dette_monde" sources="Eurostat, OECD, IMF and World Bank" donnees="The 27 European Union countries and the economies outside Europe, with their levels of comparability, their definitions and their statistics; the same content is available as CSV, one row per country, readable in a spreadsheet." >}}
This page compares what a public debt represents: its stock, its average interest cost and the revenue that services it, then the weight of old borrowing in what it costs today. In the European Union in {{< monde-val "annee" >}}, two countries with similar debt can devote shares of their revenue to interest that differ by a factor of {{< monde-val "j_rapport" >}}, mainly because the price of their debt differs, and that price has no linear relationship with the level of debt. These relationships describe one year and associations, not causes; they do not measure the risk of a crisis.
{{< /reutiliser >}}
