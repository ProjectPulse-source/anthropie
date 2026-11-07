---
title: "Why does French public debt rise?"
url: /en/why-does-public-debt-rise/
description: "French public debt doubled as a share of GDP in thirty years. Interest and growth almost offset each other, in two opposite periods; the rise comes mostly from deficits excluding interest. Spending or revenue: the answer changes with the years compared. A Eurostat decomposition."
chapo: "Between {dyn.annee_depart} and {dyn.annee_fin}, French public debt went from {dyn.dette_depart}% to {dyn.dette_fin}% of GDP: it doubled as a share of the wealth produced. Of these {dyn.hausse} points of GDP, public deficits excluding interest, known as primary deficits, contributed {dyn.deficits_primaires}. This balance shows which terms drove the debt up, not why the deficits existed."
og_title: "Why does French public debt rise?"
og_image: "images/og-dette-dynamique-en.jpg"
og_image_alt: "Share card: “Why the debt doubled” — waterfall of French public debt in points of GDP, 1995 to 2025: interest, nominal growth, primary deficits, stock-flow adjustments."
date: 2026-09-30
lastmod: 2026-11-05
# English version of part 1 of the public debt dossier (FR: content/pourquoi-la-dette-publique-augmente/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/dette_dynamique.json.
# Rewritten on 11/10/2026 with the French page (scenario B+), same structure and same anchors.
donnees: [dette_dynamique]
journal:  # révisions qui changent la lecture de la page (partials/page-date-visible.html affiche la plus récente)
  - {date: 2026-11-06, texte: "Added: section “Tax cuts, or revenue that slows down?”, which uses the Court of Audit's accounts to separate decided measures from the spontaneous growth of compulsory levies, and shows that part of the fall in revenue comes from how refundable tax credits, the CICE among them, are recorded, with a counterpart in spending."}
  - {date: 2026-11-05, texte: "Correction: the page attributed to the Commission a “cyclical and one-off part” of the deficit that it computed itself, by setting Eurostat's observed balance against the Commission's structural balance (two editions, two denominators). That figure is withdrawn; only the IMF's, drawn from a single edition, remains."}
  - {date: 2026-11-02, texte: "Eurostat accounts of 21 October 2026: in 2025, the implicit rate moves slightly back above nominal growth; “nominal growth has prevailed every year since 2017, except 2020” becomes “up to 2024”."}
  - {date: 2026-10-18, texte: "Addition: section “Business cycle or structure?”, the cyclically adjusted primary deficit according to the Commission, the IMF and the OECD, and its breakdown into revenue and spending."}
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_dynamique"
  nom: "Why French public debt rises: a decomposition of the change in the debt-to-GDP ratio"
  description: "Annual decomposition, from {dyn.annee_depart} to {dyn.annee_fin}, of the change in the debt-to-GDP ratio of French general government into the interest effect, the nominal growth effect, the primary balance and stock-flow adjustments; spending, revenue and balance as a share of GDP; cyclically adjusted primary balance according to the European Commission (AMECO, with its cyclically adjusted revenue and spending), the IMF and the OECD; ratios checked against those published by Eurostat. Producers' series, no value entered by hand."
  couverture_temporelle: "{dyn.annee_depart}/{dyn.annee_fin}"
  couverture_spatiale: "France"
  doi: "10.5281/zenodo.23995830"  # Zenodo concept DOI (always the latest version), published 6 November 2026; deposit = these files minus the IMF series (commercial reuse subject to authorisation)
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
    - "https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en"
    - "https://www.imf.org/external/datamapper/datasets/FM"
    - "https://data-explorer.oecd.org/"
  mots: ["public debt", "France", "primary deficit", "snowball effect", "implicit interest rate", "nominal growth", "public spending", "public revenue", "Eurostat"]
  fichiers: ["dette_dynamique.csv", "dette_dynamique.json"]
  citation: ["https://doi.org/10.5281/zenodo.23145963"]  # AWP-09 (English edition): method and benchmark of this decomposition
faq:
  - question: "Does interest make the debt rise?"
    answer: "Yes: it is a real charge, which adds to the borrowing requirement. But nominal GDP growth lowers the debt-to-GDP ratio by enlarging its denominator, and over thirty years it almost offset the accounting contribution of interest ({dyn.effet_interets} points, against {dyn.effet_croissance} of reduction). This offset is made of two opposite periods: before {dyn.tc_bascule}, the net effect added {dyn.tc_avant_abs} points to the ratio; since then, it has taken off {dyn.tc_apres_abs}. In {dyn.annee_fin}, on accounts still subject to revision, the implicit interest rate and nominal growth were almost equal ({dyn.taux_implicite_dernier}% and {dyn.croissance_derniere}%)."
  - question: "Does the debt come from too much spending or too little revenue?"
    answer: "These accounts do not settle it: a primary deficit is a gap, which can come from one, the other or both. On Eurostat's series, the diagnosis changes with the years compared: from {dyn.ofce_debut} to {dyn.ofce_fin}, public revenue changes by {dyn.ofce_rec} points of GDP and spending excluding interest by {dyn.ofce_dep_hi}; from {dyn.tresor_debut} to {dyn.tresor_fin}, spending excluding interest by {dyn.tresor_dep_hi} and revenue by {dyn.tresor_rec}; from {dyn.tresor_debut} to {dyn.ofce_fin}, revenue by {dyn.croise_rec} and spending excluding interest by {dyn.croise_dep_hi}. The end year matters as much as the start year."
  - question: "Does inflation reduce the debt?"
    answer: "It can reduce the ratio, by increasing nominal GDP faster than the interest bill. From 2021 to 2023, nominal growth — price rises included — produced an interest-growth effect of −{dyn.effet_2021_2023} points, while primary deficits added {dyn.deficits_2021_2023}; this decomposition does not separate the share of prices from that of real growth. This is not costless: it reduces the real value of nominal claims, and it raises the cost of inflation-linked bonds."
  - question: "Is a primary deficit a sign of too much spending?"
    answer: "Not necessarily: it is a gap between spending and revenue excluding interest, which can come from rising spending, falling revenue, or a recession that does both at once. These data measure the gap; they do not say which of its two terms should be corrected."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif", "explicatif-causal"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  livres: ["dette-publique-qui-paie-vraiment"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 5
  nature: "Official series (Eurostat) decomposed, and the author's calculations"
---

{{< dossier-dette volet="hausse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data last updated {{< dyn-val "date_donnees" >}}</span> France, general government, Eurostat series from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}. Download: <a href="/dette_dynamique.csv">CSV</a> · <a href="/dette_dynamique.json">JSON</a> · <a href="#sources">method</a></p>

France is a telling case for a question every indebted country faces. Its debt ratio doubled in thirty years, and Eurostat's harmonised series allow that rise to be split, year by year, into the terms of a standard accounting identity. The accounting identity is general; the estimates below are for France.

## Where the rise comes from {#cascade}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-cascade-en-m.svg" width="300" height="643">
    <img src="/img/dette-dynamique-cascade-en.svg" alt="Waterfall in points of GDP: French debt starts at {{< dyn-val "dette_depart" >}}% at the end of {{< dyn-val "annee_depart" >}}; the interest effect would have pushed it up by {{< dyn-val "effet_interets" >}} points, nominal GDP growth takes away {{< dyn-val "effet_croissance" >}}; primary deficits add {{< dyn-val "deficits_primaires" >}} points and stock-flow adjustments {{< dyn-val "flux_stock" >}}; the debt reaches {{< dyn-val "dette_fin" >}}% at the end of {{< dyn-val "annee_fin" >}}. Cumulative accounting contributions, not amounts paid." width="720" height="413" loading="lazy">
  </picture>
  <figcaption>Cumulative decomposition of the change in the debt-to-GDP ratio, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}}, in points of GDP (Eurostat). Blue: the stock; orange: what pushes it up; grey: what pulls it down.</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** Interest ({{< dyn-val "effet_interets" >}} points) and nominal GDP growth (−{{< dyn-val "effet_croissance" >}}) almost offset each other: their net effect is only {{< dyn-val "effet_net" >}} points over thirty years, but it is the sum of two opposite periods, {{< dyn-val "tc_avant" >}} points before {{< dyn-val "tc_bascule" >}} and {{< dyn-val "tc_apres" >}} since; stock-flow adjustments, which do not go through the deficit, add {{< dyn-val "flux_stock_nb" >}} points.

</div>

**How can interest that is paid "cancel out"?** It does not: it is a real charge; other things being equal, it raises the borrowing requirement and adds to the debt. But the page measures a ratio, debt relative to the wealth produced in the year, and that wealth grows too. Take a debt equal to GDP and isolate interest, with no other spending, revenue or financial transaction, financing it with new borrowing: if the year's interest raises the debt by one fiftieth and GDP also rises by one fiftieth, the debt has risen in euros, but the ratio has not moved. The interest has not disappeared: it is the growth of the denominator that offsets its effect on the ratio.

The {{< dyn-val "effet_interets" >}} points mostly "erased" by growth are therefore contributions, cumulated over thirty years, to the change in a ratio, not an amount paid equal to {{< dyn-val "effet_interets" >}}% of GDP. Who receives this interest and who bears what the debt costs is the subject of [Who really pays for public debt?](/en/who-really-pays-public-debt/)

## Year by year {#annee-par-annee}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-annuelle-en-m.svg" width="300" height="747">
    <img src="/img/dette-dynamique-annuelle-en.svg" alt="Stacked bars by year, from {{< dyn-val "annee_premiere_variation" >}} to {{< dyn-val "annee_fin" >}}, in points of GDP: primary deficits in orange, the interest-growth effect in blue, stock-flow adjustments in grey, the change in the ratio as a black dot. Two peaks, 2009 (+{{< dyn-val "hausse_2009" >}} points) and 2020 (+{{< dyn-val "hausse_2020" >}}); an interest-growth effect of −{{< dyn-val "effet_2021_2023" >}} points in 2021-2023." width="720" height="369" loading="lazy">
  </picture>
  <figcaption>Annual contributions to the change in the debt-to-GDP ratio, France (Eurostat). The three bars add up to the change, marked by the black dot. Here the colours designate terms, not the direction of their effect as in the waterfall.</figcaption>
</figure>

Three periods stand out, and the dominant term changes from one to the next. The {{< dyn-val "tc_bascule" >}} turning point, which splits the series in two for the interest-growth effect, falls within the second period.

**{{< dyn-val "p1_lib" >}}: the interest-growth effect.** The ratio gains {{< dyn-val "p1_hausse_abs" >}} points. The implicit interest rate on the debt, that is, the average rate on the debt as a whole, then exceeds nominal growth on average: the interest-growth effect adds {{< dyn-val "p1_taux_croissance_abs" >}} points, while the primary balance, close to equilibrium and sometimes in surplus, contributes {{< dyn-val "p1_deficits" >}}.

**{{< dyn-val "p2_lib" >}}: primary deficits.** The ratio gains {{< dyn-val "p2_hausse_abs" >}} points, of which {{< dyn-val "p2_deficits" >}} come from primary deficits and {{< dyn-val "p2_taux_croissance" >}} from the interest-growth effect. The year 2009 alone accounts for {{< dyn-val "hausse_2009" >}} points: the primary deficit widens and GDP contracts, two effects that coincide with the financial crisis.

**{{< dyn-val "p3_lib" >}}: nominal growth holds the ratio back, deficits push it up.** The ratio gains {{< dyn-val "p3_hausse_abs" >}} points. In 2020 it jumps by {{< dyn-val "hausse_2020" >}} points, with the pandemic. From 2021 to 2023, strong nominal GDP growth, price rises included, brings the ratio down: the interest-growth effect takes {{< dyn-val "effet_2021_2023" >}} points off the ratio, more than primary deficits add ({{< dyn-val "deficits_2021_2023" >}}). The share of prices in that growth is the subject of the page [Did inflation really ease France's debt burden?](/en/inflation-and-french-public-debt/) Since 2024, the ratio has been rising again.

**The implicit interest rate has been rising since its low of {{< dyn-val "ti_creux_an" >}}, mostly through a jump in 2022.** After {{< dyn-val "ti_creux" >}}% in {{< dyn-val "ti_creux_an" >}}, it edges up in 2021 ({{< dyn-val "ti_2021" >}}%), jumps in 2022 ({{< dyn-val "ti_2022" >}}%), then rises more slowly. That jump does not come only from bonds being renewed at the new rates: in 2022, inflation also sharply raised the recorded cost of the State's inflation-linked bonds, according to the French Senate's report on that year's accounts. The accounts presented here do not make it possible to separate the share of each mechanism in the implicit rate of general government as a whole.

**The {{< dyn-val "annee_fin" >}} accounts are still subject to revision.** Those on this page are the Eurostat series {{< dyn-val "maj_long" >}}. {{< dyn-val "insee_phrase" >}} That year, the implicit rate ({{< dyn-val "taux_implicite_dernier" >}}%) and nominal growth ({{< dyn-val "croissance_derniere" >}}%) are almost equal, and the interest-growth effect is close to zero: so narrow a gap does not say which way the effect will go next.

Over the {{< dyn-val "annees_total" >}} years of the series, the primary balance was in surplus only {{< dyn-val "annees_excedent" >}} times. This count describes a recurrence; it does not say whether each of these deficits was desirable, avoidable or cyclical.

## Too much spending or too little revenue? {#depenses-recettes}

The primary deficit is the gap between spending excluding interest and public revenue. It does not say whether that gap comes from rising spending, falling revenue or both at once. To describe it, one has to pick two years and compare spending and revenue, as a share of GDP, between them. Eurostat's series then give different answers depending on the years chosen.

- **From {{< dyn-val "ofce_debut" >}} to {{< dyn-val "ofce_fin" >}}**, the period chosen by the OFCE: public revenue changes by {{< dyn-val "ofce_rec" >}} points of GDP, spending excluding interest by {{< dyn-val "ofce_dep_hi" >}}. The fall in revenue dominates.
- **From {{< dyn-val "tresor_debut" >}} to {{< dyn-val "tresor_fin" >}}**, the period chosen by the French Treasury: spending excluding interest changes by {{< dyn-val "tresor_dep_hi" >}} points, revenue by {{< dyn-val "tresor_rec" >}}. The rise in spending dominates.
- **From {{< dyn-val "tresor_debut" >}} to {{< dyn-val "ofce_fin" >}}**, the window common to both: spending excluding interest changes by {{< dyn-val "croise_dep_hi" >}} points, revenue by {{< dyn-val "croise_rec" >}}. The fall in revenue dominates again.

**The diagnosis depends on both ends.** It changes with the start year, but also with the end year: ending in {{< dyn-val "ofce_fin" >}} rather than {{< dyn-val "tresor_fin" >}}, the same start year gives the opposite conclusion. Two accurate comparisons over different periods can therefore lead to opposite descriptive findings — neither, on its own, establishes the causes of the deficits or identifies the policy that should have been pursued. The page measures one Eurostat indicator over these windows; it does not treat the OFCE's and the Treasury's work as equivalent, since they also differ in their definitions and questions. Faced with either, the first question to ask is "from which year to which year?". Yet two equally accurate windows are not equally relevant: a period is justified by the question asked (the effect of decisions taken since a given date, the situation before a crisis), not by the result it gives. 

**What reverses the conclusion between the two windows starting in {{< dyn-val "tresor_debut" >}} is revenue.** Spending excluding interest changes by the same amount in both, to within rounding; revenue, by contrast, rises by {{< dyn-val "rec_fin_abs" >}} {{< dyn-val "rec_fin_pt" >}} of GDP in {{< dyn-val "tresor_fin" >}}. Over {{< dyn-val "tresor_debut" >}}-{{< dyn-val "tresor_fin" >}}, the rise in spending outweighs the fall in revenue by only {{< dyn-val "tresor_marge" >}} points: a revision of the accounts of that size would be enough to reverse the finding. The finding over {{< dyn-val "ofce_debut" >}}-{{< dyn-val "ofce_fin" >}}, which ends before {{< dyn-val "tresor_fin" >}}, does not depend on that revision. It is the easing of the fall in revenue, not a movement in spending, that tips their relative weight. These movements are measured as shares of GDP: they can come from the numerator, the denominator, or both. And a shrinking deficit has not disappeared: in {{< dyn-val "tresor_fin" >}}, the primary balance is still in deficit and the debt keeps rising. These comparisons, on accounts still subject to revision, do not say which decisions produced these movements, or what should be corrected. The conclusions the OFCE and the French Treasury draw from them, and the objects they examine, are compared below.

## Business cycle or structure? {#conjoncture}

A deficit can stem from the business cycle: when activity stays below its potential level, revenue weakens and some spending rises, then the deficit shrinks with the recovery. It can also be structural, and remain once the economy is back at its potential. Three institutions estimate this split, each with its own method: the European Commission, the IMF and the OECD.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-conjoncture-en-m.svg" width="300" height="744">
    <img src="/img/dette-dynamique-conjoncture-en.svg" alt="Lines of the cyclically adjusted primary balance, as % of potential GDP: IMF since 1996, Commission and OECD since 2010, and the observed balance in grey. Over {{< dyn-val "cs_avant_lib" >}} then {{< dyn-val "cs_apres_lib" >}}: Commission {{< dyn-val "cs_ce_avant" >}} then {{< dyn-val "cs_ce_apres" >}}, IMF {{< dyn-val "cs_fmi_avant" >}} then {{< dyn-val "cs_fmi_apres" >}}, OECD {{< dyn-val "cs_ocde_avant" >}} then {{< dyn-val "cs_ocde_apres" >}}." width="720" height="373" loading="lazy" decoding="async">
  </picture>
  <figcaption>Cyclically adjusted primary balance according to three estimates, and observed primary balance (Eurostat). The grey bands mark the two periods compared.</figcaption>
</figure>

**Over {{< dyn-val "cs_apres_lib" >}}, the deficit would not disappear with the business cycle alone.** Cyclically adjusted, the primary balance is lower over {{< dyn-val "cs_apres_lib" >}} than over {{< dyn-val "cs_avant_lib" >}} in all three estimates: by {{< dyn-val "cs_ce_saut_pt" >}} according to the Commission ({{< dyn-val "cs_ce_avant" >}}% then {{< dyn-val "cs_ce_apres" >}}% of potential GDP), by {{< dyn-val "cs_fmi_saut_pt" >}} according to the IMF ({{< dyn-val "cs_fmi_avant" >}}% then {{< dyn-val "cs_fmi_apres" >}}%) and by {{< dyn-val "cs_ocde_saut_pt" >}} according to the OECD ({{< dyn-val "cs_ocde_avant" >}}% then {{< dyn-val "cs_ocde_apres" >}}%). Over {{< dyn-val "cs_apres_lib" >}}, the cyclical part of the deficit is only {{< dyn-val "cs_fmi_conj_pt" >}} of GDP according to the IMF, which publishes the observed and the cyclically adjusted balance in the same edition.

**These are three estimates, and they do not coincide.** The Commission and the OECD also remove one-off measures, the IMF does not; and each relies on an estimate of potential output, which is not a measurement and gets revised. The page gives the three values, without averaging them.

**Before 2008, the cyclically adjusted balance was close to zero.** Only the IMF goes back before 2010. Its cyclically adjusted primary balance averages {{< dyn-val "cs_fmi_long" >}}% of potential GDP over {{< dyn-val "cs_long_lib" >}}, {{< dyn-val "cs_fmi_crise" >}}% over {{< dyn-val "cs_crise_lib" >}}, {{< dyn-val "cs_fmi_avant" >}}% over {{< dyn-val "cs_avant_lib" >}}, then {{< dyn-val "cs_fmi_apres" >}}% over {{< dyn-val "cs_apres_lib" >}}. The adjusted deficit that appeared after 2008 was partly absorbed; the one after 2020 has not been so far. This sequence dates the deteriorations; it is not enough to establish that the crises produced them.

**Where: revenue over the recent period, spending over the long run.** The cyclically adjusted revenue and non-interest spending published by the Commission add up exactly to its adjusted balance. From {{< dyn-val "cs_avant_lib" >}} to {{< dyn-val "cs_apres_lib" >}}, that balance falls by {{< dyn-val "cs_ca_saut_pt" >}}: adjusted revenue falls by {{< dyn-val "cs_rec_pt" >}}, adjusted spending changes by {{< dyn-val "cs_dep" >}} points. The structural balance cited above falls by {{< dyn-val "cs_ce_saut_pt" >}} because it also removes one-off measures, present above all in 2019. Since {{< dyn-val "cs_long_lib" >}}, by contrast, adjusted spending has risen by {{< dyn-val "cs_l_dep" >}} points of potential GDP and revenue by {{< dyn-val "cs_l_rec" >}}: over the long run, the rise in spending dominates. As with the OFCE and Treasury windows above, the answer depends on the years compared.

**What this split does not say.** Cyclically adjusted revenue that falls mixes decided tax cuts and the spontaneous yield of taxes, which can grow more slowly than the economy. These series do not separate the two: they say where the deficit deepened, and that the business cycle alone does not explain it, not which decisions deepened it. The Court of Audit's accounts separate them, and show that part of this fall in revenue has a counterpart in spending (next section).

<details class="repli"><summary>Year-by-year values, definitions and editions</summary>

| Year | Commission, structural | IMF, cyclically adjusted | OECD, underlying | Observed (Eurostat) |
|---|---|---|---|---|
| 2015 | {{< dyn-val "cs_2015_ce" >}} | {{< dyn-val "cs_2015_fmi" >}} | {{< dyn-val "cs_2015_ocde" >}} | {{< dyn-val "cs_2015_obs" >}} |
| 2016 | {{< dyn-val "cs_2016_ce" >}} | {{< dyn-val "cs_2016_fmi" >}} | {{< dyn-val "cs_2016_ocde" >}} | {{< dyn-val "cs_2016_obs" >}} |
| 2017 | {{< dyn-val "cs_2017_ce" >}} | {{< dyn-val "cs_2017_fmi" >}} | {{< dyn-val "cs_2017_ocde" >}} | {{< dyn-val "cs_2017_obs" >}} |
| 2018 | {{< dyn-val "cs_2018_ce" >}} | {{< dyn-val "cs_2018_fmi" >}} | {{< dyn-val "cs_2018_ocde" >}} | {{< dyn-val "cs_2018_obs" >}} |
| 2019 | {{< dyn-val "cs_2019_ce" >}} | {{< dyn-val "cs_2019_fmi" >}} | {{< dyn-val "cs_2019_ocde" >}} | {{< dyn-val "cs_2019_obs" >}} |
| 2020 | {{< dyn-val "cs_2020_ce" >}} | {{< dyn-val "cs_2020_fmi" >}} | {{< dyn-val "cs_2020_ocde" >}} | {{< dyn-val "cs_2020_obs" >}} |
| 2021 | {{< dyn-val "cs_2021_ce" >}} | {{< dyn-val "cs_2021_fmi" >}} | {{< dyn-val "cs_2021_ocde" >}} | {{< dyn-val "cs_2021_obs" >}} |
| 2022 | {{< dyn-val "cs_2022_ce" >}} | {{< dyn-val "cs_2022_fmi" >}} | {{< dyn-val "cs_2022_ocde" >}} | {{< dyn-val "cs_2022_obs" >}} |
| 2023 | {{< dyn-val "cs_2023_ce" >}} | {{< dyn-val "cs_2023_fmi" >}} | {{< dyn-val "cs_2023_ocde" >}} | {{< dyn-val "cs_2023_obs" >}} |
| 2024 | {{< dyn-val "cs_2024_ce" >}} | {{< dyn-val "cs_2024_fmi" >}} | {{< dyn-val "cs_2024_ocde" >}} | {{< dyn-val "cs_2024_obs" >}} |
| 2025 | {{< dyn-val "cs_2025_ce" >}} | {{< dyn-val "cs_2025_fmi" >}} | {{< dyn-val "cs_2025_ocde" >}} | {{< dyn-val "cs_2025_obs" >}} |

As % of potential GDP (% of GDP for the observed balance); a negative number is a deficit.

**Three definitions.** The Commission's structural primary balance removes the estimated effect of the cycle and one-off measures; it is published for France only since 2010. The OECD's underlying primary balance does the same. The IMF's cyclically adjusted primary balance removes the effect of the cycle only. Cyclically adjusted revenue and spending are the Commission's (AMECO series), whose difference gives back, each year, its cyclically adjusted primary balance.

**Why Eurostat's observed balance differs from the IMF's.** This page's primary balance excludes interest paid; the IMF's excludes net interest, paid minus received. The gap between the two is therefore the interest received by general government: {{< dyn-val "cs_int_long" >}} points of GDP on average over {{< dyn-val "cs_long_lib" >}} and {{< dyn-val "cs_int_apres" >}} points over {{< dyn-val "cs_apres_lib" >}}, to within a few hundredths. It is essentially a difference of definition.

**Editions.** European Commission, {{< dyn-val "cs_ed_ameco" >}}; IMF, {{< dyn-val "cs_ed_fmi" >}}; OECD, {{< dyn-val "cs_ed_ocde" >}}. The three were published on different dates and will be revised.

</details>

## Tax cuts, or revenue that slows down? {#mesures}

Revenue can fall as a share of GDP because the law cut it, or because, with the law unchanged, it grows more slowly than the economy. Each year, the French Court of Audit (Cour des comptes) separates these two movements for compulsory levies (taxes and social contributions): their spontaneous growth, at constant legislation, and new measures, the increases or cuts that were decided, as costed by the administration. Accumulated since 2015 and set against the two periods of the previous section, its series make it possible to test one reading of the recent deficit: lasting tax cuts whose cost stayed hidden until 2023 behind buoyant revenue.

**More than a third of the fall in observed revenue comes from how refundable tax credits are recorded, and it has a counterpart in spending.** These credits can be paid out beyond the tax due. Under European rules, Eurostat, like the Commission, therefore records taxes before these credits and classifies the credits as spending; INSEE and the Court of Audit compute compulsory levies net of them. The largest of them, the CICE, was replaced in 2019 by a permanent cut in employer social contributions: gross revenue fell, and so did tax-credit spending. The tax credits that Eurostat adds to revenue go from {{< dyn-val "mn_ptc_avant" >}}% of GDP over {{< dyn-val "cs_avant_lib" >}} to {{< dyn-val "mn_ptc_apres" >}}% over {{< dyn-val "cs_apres_lib" >}}. Net of these credits, compulsory levies fall by {{< dyn-val "mn_po" >}} {{< dyn-val "mn_po_pt" >}} of GDP, not by {{< dyn-val "mn_tr" >}} like total revenue, cyclically adjusted or not; the remainder, a reconciliation gap between these series, changes by {{< dyn-val "mn_hors_po" >}} {{< dyn-val "mn_hors_po_pt" >}}. Removed from observed spending excluding interest as well, the same series brings its rise to about {{< dyn-val "mn_dep_nette" >}} {{< dyn-val "mn_dep_nette_pt" >}} of GDP instead of {{< dyn-val "mn_dep" >}}. That figure remains an estimate: in its current accounts, on the 2020 base, INSEE records tax-credit spending in the year the entitlement arises, and the revenue in the year the credit is set against tax. The balance itself does not change: what changes is the split between revenue and spending.

**The measures alone take away more than this net fall.**

| Between {{< dyn-val "cs_avant_lib" >}} and {{< dyn-val "cs_apres_lib" >}} | Points of GDP |
|---|---|
| Compulsory levies net of tax credits (INSEE), observed change | {{< dyn-val "mn_po_sg" >}} |
| New measures, accumulated, excluding the CICE | {{< dyn-val "mn_mes" >}} |
| Replacement of the CICE (double year of 2019, then knock-on effects) | {{< dyn-val "mn_cice" >}} |
| Spontaneous growth faster than GDP (accumulated elasticity effect) | {{< dyn-val "mn_el" >}} |
| Closing gap | {{< dyn-val "mn_ecart" >}} |

In this reconstruction, the accumulated measures take away {{< dyn-val "mn_mes_abs" >}} {{< dyn-val "mn_mes_abs_pt" >}}, nearly twice the observed fall: revenue that grew spontaneously faster than GDP still offsets {{< dyn-val "mn_el_abs" >}} of it. For 2017-2022, the Court of Audit publishes, on the 2020 base, measures of {{< dyn-val "mn_c_mes" >}} points and spontaneous growth of {{< dyn-val "mn_c_sp" >}}; it divides the cumulative measures in euros by 2022 GDP, and the same calculation gives {{< dyn-val "mn_tc_mes" >}} and {{< dyn-val "mn_tc_sp" >}} here. Each divided by the GDP of its own year, as in the table, these measures weigh {{< dyn-val "mn_t_mes" >}}. From one year to the next, the closing gap with the rate published by INSEE never exceeds {{< dyn-val "mn_ec_max" >}} {{< dyn-val "mn_ec_max_pt" >}}.

**The masking, then the normalisation.** From 2017 to 2022, elasticity almost exactly offsets the cuts that were decided, the largest of which the Court of Audit lists: abolition of the housing tax (EUR {{< dyn-val "mn_th" >}} billion), cuts in production taxes (EUR {{< dyn-val "mn_ip" >}} billion) and in the corporate income tax rate (EUR {{< dyn-val "mn_is" >}} billion), reform of the income tax schedule (EUR {{< dyn-val "mn_ir" >}} billion). The 2022 levy rate, {{< dyn-val "mn_po2022" >}}% of GDP, is thus close to that of 2017, {{< dyn-val "mn_po2017" >}}%. Then elasticity turns and takes away {{< dyn-val "mn_el_2324" >}} {{< dyn-val "mn_el_2324_pt" >}} in 2023 and 2024: the effect of the cuts on the levy rate then becomes visible. The Court of Audit wrote as early as July 2024 that this spontaneous buoyancy "was still masking, at the end of 2022, the effect of the cuts in compulsory levies made since 2018" (our translation). From 2024 to {{< dyn-val "mn_fin" >}}, new measures change direction and bring back {{< dyn-val "mn_mes_24fin" >}} {{< dyn-val "mn_mes_24fin_pt" >}}. Those of 2024 include a EUR {{< dyn-val "mn_fru" >}} billion cut in banks' contributions to the European Single Resolution Fund, with no effect on the government balance; excluding these levies earmarked for Europe, they reach EUR {{< dyn-val "mn_24_hors_ue" >}} billion. The total of measures since 2015 goes from {{< dyn-val "mn_cum_2023" >}} in 2023 to {{< dyn-val "mn_cum_fin" >}} in {{< dyn-val "mn_fin" >}}. Nearly EUR {{< dyn-val "mn_tempo_md" >}} billion of the 2025 increases, or {{< dyn-val "mn_tempo_pt" >}} {{< dyn-val "mn_tempo_pt_pt" >}} of GDP, come from schemes announced as temporary, two of which were extended in 2026.

**What this test establishes, and what it leaves open.** The mechanism is established by the Court of Audit itself: lasting cuts in levies, offset until 2022 by spontaneously buoyant revenue, whose effect appeared in 2023 and 2024. The test measures its scope between the two periods. Of the fall in observed revenue, {{< dyn-val "mn_tr" >}} {{< dyn-val "mn_tr_pt" >}}, {{< dyn-val "mn_ptc" >}} comes from the fall in refundable tax credits, mostly the end of the CICE, which has its counterpart in spending. Of the net fall of {{< dyn-val "mn_po" >}} {{< dyn-val "mn_po_pt" >}}, measures, the CICE and elasticity leave a closing gap of {{< dyn-val "mn_ecart" >}}. This is an accounting breakdown, not a causal attribution: the administration costs the measures mostly with behaviour unchanged, leaving out their effect on activity and on tax bases, and these effects blend into so-called spontaneous growth. Some measures are temporary, others have no effect on the government balance. Finally, the test describes a change between two periods; it does not say why the deficit was already high before.

## How the calculation works {#identite}

Each year, the debt-to-GDP ratio moves under the effect of three terms. The **interest-growth effect**: the year's interest adds to the debt, while nominal GDP growth — real growth plus price rises — lowers the ratio even without any repayment; their balance is positive when the implicit interest rate exceeds nominal growth, negative in the opposite case. The **primary deficit**: the gap between public spending and revenue excluding interest, which measures its size, not its cause. **Stock-flow adjustments**: debt that moves without passing through the deficit (cash set aside, loans and equity stakes, valuation effects), obtained here as a residual. The waterfall shows the interest-growth effect as its two components, interest and growth: hence its four steps for three terms.

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
- **A last year subject to revision.** The {{< dyn-val "annee_fin" >}} accounts are those of the Eurostat series {{< dyn-val "maj_court" >}}.
- **A series that starts in {{< dyn-val "annee_depart" >}}.** Eurostat's harmonised interest data go back no further; the long-run debt series, since 1978, is in [What does French public debt actually cost?](/en/cost-of-french-public-debt/)

{{< confrontation-recherche verifie="2026-11-06" publie="oui" resume="the weight of primary deficits recurs over fifty years; reading the near-cancellation of interest and growth as neutrality is challenged; spending or revenue: the diagnosis depends on the period and the comparison chosen" >}}
**Measured here.** The annual decomposition of the French ratio from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}, on Eurostat series, checked against the published ratios. None of the texts read decomposes this window with this source: the measurement is validated by reproduction, not by citation.

**Consistent with.** The 2014 citizens' audit attributed a large share of the rise in the debt from 1980 to 2012 to the effect of interest rates. The two analyses share neither the same end points nor necessarily the same counterfactual; but over their common period, from end-{{< dyn-val "annee_depart" >}} to end-{{< dyn-val "cit_fin" >}}, the interest-growth effect is, here too, the largest term in the rise: {{< dyn-val "cit_tc" >}} points out of {{< dyn-val "cit_hausse" >}}, ahead of primary deficits ({{< dyn-val "cit_def" >}}) and stock-flow adjustments ({{< dyn-val "cit_sfa" >}}). The comparison of their methods is set out in the working paper [AWP-09](/en/awp/awp-09/). Over 1970-2023, using INSEE accounts and a historical database, Auclert, Philippon and Ragot find that primary deficits and stock-flow adjustments account for 88 points of a rise of nearly 90 (from 21% to 110% of GDP), and a "snowball" effect close to zero on average: the same identity, another period, another source, and a primary deficit that includes the adjustments this page isolates. Clavères, at the French Treasury, finds the same sequence of signs: the effective interest rate on the debt moves above nominal growth in the course of the 1980s, and growth moves back above it from 2016. That rate is close to this page's implicit interest rate without being identical to it: both relate interest to a debt stock, not necessarily the same one, the apparent cost published by Eurostat using the year's average stock, this page the stock at the end of the previous year. The OFCE (Heyer, Plane, Ragot, Sampognaro and Timbeau) links France's 53-point rise in debt from 2000 to 2024 (against 44 points in Spain, 27 in Italy and 5 in Germany) to deficits, without decomposing these rises. The French Treasury describes debt rising almost continuously since 2001, with deficit reductions in favourable periods only stabilising the ratio, and a deficit that stayed above the stabilising balance until 2019. It describes 2001-2007 as "relative stability"; the page's series nonetheless records a rise from {{< dyn-val "dette_2001" >}}% to {{< dyn-val "dette_2007" >}}% of GDP, and the OFCE estimates that nearly half of the deficit gap with the euro area had formed before the 2007-2008 crisis.

**Challenged by.** Any reading of the near-cancellation of interest and growth as neutrality. The match depends on the starting point, to within about ten points (Auclert, Philippon and Ragot), and the gap between interest and growth changed sign during the period (Clavères). This page's data confirm it: the interest-growth effect contributed {{< dyn-val "tc_avant" >}} points before {{< dyn-val "tc_bascule" >}}, {{< dyn-val "tc_apres" >}} since. The CAE note, for its part, interprets this accounting finding as the direct result of budgetary choices ("our debt is the direct consequence of our budgetary choices"), while judging the share of crises hard to estimate; an OFCE estimate, cited by the note, puts it at about half of the rise since 2007.

**Not established.** Which of spending or revenue widened the recent deficits. The OFCE, which puts forward a more gradual adjustment path, starts the recent period at the 2017 presidential election and attributes most of the deterioration of the structural balance to an unfunded fall in compulsory levies, which declined by 2.5 points of GDP from 2017 to 2024; over that period, according to the OFCE, total spending stays stable as a share of GDP and primary spending falls slightly as a share of potential GDP (on Eurostat's series, as a share of actual GDP, total spending changes by {{< dyn-val "ofce_dep" >}} points). The French Treasury, for which consolidation "could go first" through cutting spending, starts from 2019, the situation before the pandemic, and notes that several spending items (interest charge, social security, central and local government) contributed to the 2.7-point deterioration of the balance up to 2025, while noting that reforms durably reduced revenue. Over the common window, the OFCE and the French Treasury converge on one fact: public spending rose less in France than in the euro area (1.8 points against 2.6 according to the OFCE, 1.6 against 2.4 according to the Treasury); Eurostat's series find the same direction and order of magnitude (spending {{< dyn-val "croise_dep" >}} points, total revenue {{< dyn-val "croise_rec" >}}). They do not, however, then analyse the same object: the OFCE explains the gap between France and the euro area, which it links mainly to revenue, while the French Treasury breaks down the deterioration of the French balance over 2019-2025; and Eurostat's total revenue is not the OFCE's compulsory levies. On Eurostat's series, the diagnosis depends on both ends of the window (section "Too much spending or too little revenue?"). The Court of Audit separates, for compulsory levies, decided measures from spontaneous growth; its reports from 2017 to 2026 feed the section "Tax cuts, or revenue that slows down?", which reproduces its 2017-2022 breakdown and measures what tax credits change in the split between revenue and spending. The causes, finally: the CAE note attributes the recent deterioration to the pandemic, the energy price shields and unfunded tax cuts, the French Treasury to the crises and the support measures, but none of the texts read provides a causal decomposition of the primary deficits observed from {{< dyn-val "annee_depart" >}} to {{< dyn-val "annee_fin" >}}.

**References read**

- Auclert, A., Philippon, T. and Ragot, X., "Quelle trajectoire pour les finances publiques françaises ?" [What path for French public finances?], *Les notes du Conseil d'analyse économique*, no. 82, July 2024 (in French).
- Clavères, G., "Taux d'intérêt, croissance et soutenabilité de la dette publique" [Interest rates, growth and public debt sustainability], *Trésor-Éco*, no. 334, French Treasury, October 2023 (in French).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. and Timbeau, X., "Quelles trajectoires pour les finances publiques de la France ?" [What paths for France's public finances?], *Blog de l'OFCE*, 2025 (in French).
- French Treasury (Direction générale du Trésor), "Finances publiques : une situation dégradée, un redressement nécessaire" [Public finances: a deteriorated situation, a necessary recovery], *Trésor-Éco*, no. 403, September 2026 (in French).
- Cour des comptes (French Court of Audit), *La situation et les perspectives des finances publiques* [The state and outlook of public finances], June or July editions 2017 to 2026 (breakdown of the change in compulsory levies; July 2023, p. 31; June 2026, pp. 27-30) (in French).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. and Timbeau, X., "Quelles trajectoires pour les finances publiques de la France ?" [What paths for France's public finances?], OFCE working paper no. 13, July 2025 (in French).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Summary</p>

## What to take away {#retenir}

Once interest and growth have almost offset each other, what remains in the Eurostat decomposition used here is primary deficits, {{< dyn-val "part_deficits" >}}% of the rise: excluding interest, the public accounts were in surplus in only {{< dyn-val "annees_excedent" >}} years out of {{< dyn-val "annees_total" >}}. These figures separate the terms of the rise, not the reasons for budget decisions.

This near-cancellation is an offset over time, not neutrality. Before {{< dyn-val "tc_bascule" >}}, the implicit interest rate usually exceeded nominal growth, and the interest-growth effect added {{< dyn-val "tc_avant_abs" >}} points to the ratio; since then, nominal growth has prevailed every year up to {{< dyn-val "tc_fin_neg" >}}, except 2020, when GDP fell, and the effect has contributed {{< dyn-val "tc_apres" >}} points. In {{< dyn-val "annee_fin" >}}, on accounts still subject to revision, the implicit rate moves slightly back above nominal growth ({{< dyn-val "taux_implicite_dernier" >}}% against {{< dyn-val "croissance_derniere" >}}%): the gap is too thin to say that a new period is starting. As long as the two stay this close, the direction in which the ratio moves is set by the primary balance, give or take stock-flow adjustments; if the gap is confirmed, the ratio will rise more for the same primary balance.

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

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="The same question over the long run" avis="non" >}}
This page breaks down the rise since 1995 in accounting terms. *ANTHROPY* takes the long view: how crises, from the 2008 bank bailouts to the pandemic, ended up on public balance sheets, and who then carried them.
{{< /appel-livre >}}

## Where these figures come from {#sources}

Eurostat, general government (S.13), national accounts ESA 2010, in national currency: Maastricht debt ([`gov_10dd_edpt1`](https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=en)), interest due ([`gov_10a_main`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=en), D41PAY, recorded on an accrual basis), net lending or borrowing (B9), nominal GDP as published with the deficit and debt notification (`gov_10dd_edpt1`, B1GQ); spending (TE), revenue (TR) and balance as a share of GDP as Eurostat publishes them (`gov_10a_main`). The primary balance is the general government balance plus interest (D41PAY). Each year, the identity is applied as written above; stock-flow adjustments are the residual. The script then compares, year by year, the debt ratio and the primary balance it computes with those Eurostat publishes as a percentage of GDP, and stops beyond a gap of 0.11 points. The figures computed from Eurostat series all come from the same script, re-run with each release of the sources, which checks the main quantitative statements and stops if their conditions are no longer met; their wording is reviewed editorially. Figures attributed to other studies (CAE, OFCE, French Treasury) are given as they publish them. Indexation cost of State bonds in 2022: French Senate, [report on the 2022 budget settlement bill](https://www.senat.fr/rap/l22-771-1/l22-771-17.html) (in French).

Section "Tax cuts, or revenue that slows down?": new measures, spontaneous growth and nominal GDP growth transcribed from the Court of Audit's reports on the state and outlook of public finances, using the latest vintage for each year, and checked against the archived reports; INSEE's rate of compulsory levies net of tax credits ([national accounts, base 2020](https://www.insee.fr/fr/statistiques/2381412), in French); Eurostat's payable tax credits (PTC) and total revenue (`gov_10a_main`). Each year, the Court's identity, Δτ = τ<sub>t−1</sub> × (s − g) / (1 + g) + new measures / GDP, with s the spontaneous growth and g GDP growth, is checked against the rate published by INSEE; the script stops if the gap exceeds 0.3 points in any year, or if the calculation strays more than 0.3 points from the breakdown the Court publishes for 2017-2022.

The method behind this decomposition (the identity, the benchmark formed by the ratios Eurostat publishes, and the error it rejected) and its reconciliation with three public readings of the same debt (the 2014 citizens' audit, the iFRAP Foundation, the French Court of Audit) are set out in the working paper [AWP-09 — *What Public Accounts Can Establish about the Displacement of the Public Debt Burden*](/en/awp/awp-09/) (DOI: 10.5281/zenodo.23145963, open-access PDF).

{{< reutiliser figures="figures_dynamique" jeu="dette_dynamique" sources="Eurostat, European Commission (AMECO), IMF and OECD" reserve="the IMF" donnees="The annual decomposition of the change in the debt-to-GDP ratio, France, with its four terms, the implicit interest rate and nominal growth; spending, revenue and balance as a share of GDP; the same content is available as CSV, one row per year." >}}
From end-{{< dyn-val "annee_depart" >}} to end-{{< dyn-val "annee_fin" >}}, the French debt-to-GDP ratio went from {{< dyn-val "dette_depart" >}}% to {{< dyn-val "dette_fin" >}}%. Of these {{< dyn-val "hausse" >}} points, primary deficits contributed {{< dyn-val "deficits_primaires" >}}, stock-flow adjustments {{< dyn-val "flux_stock_nb" >}} and the net effect of interest and nominal growth {{< dyn-val "effet_net_nb" >}}, made of two opposite periods. This is an accounting decomposition, not a causal attribution: it does not say why the deficits existed, and the answer to “spending or revenue” changes with the two years compared.
{{< /reutiliser >}}
