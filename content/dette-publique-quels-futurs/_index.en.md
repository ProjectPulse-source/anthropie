---
title: "Can the rules of the public debt game be changed?"
url: /en/public-debt-what-futures/
description: "With unchanged policy, the European Commission projects French public debt at {futurs.ref_2030}% of GDP in 2030 and {futurs.ref_2035}% in 2035. {futurs.n_operations_maj} ways of changing the rules of the game, from fiscal adjustment to restructuring: what each one changes, who decides it, who bears the cost."
chapo: "Yes, but with no automatic effect: depending on its mechanism and conditions, the same operation can reduce debt, shift burdens or risks onto others, or worsen it. With unchanged policy, the European Commission projects French public debt at {futurs.ref_2030}% of GDP in 2030 and {futurs.ref_2035}% in 2035; changing the rules of the game alters that path only through the budget balance, interest rates, growth or the stock of debt, and the {futurs.n_operations} ways of doing so examined here do not involve the same decision-makers or the same agreements."
og_title: "Can the rules of the public debt game be changed?"
og_image: "images/og-dette-futurs-en.jpg"
og_image_alt: "Share card: “Public debt: what futures?” — fan of the European Commission's projections for French debt up to 2030, the unchanged-policy path and the Government's forecast."
date: 2026-11-09
lastmod: 2026-11-09
# English version of part 6 of the public debt dossier (FR: content/dette-publique-quels-futurs/_index.md). Same tokens,
# same keys: values come from the affichage_en block and the matrice.en block of data/dette_futurs.json. Slug confirmed
# with the page (the licence printed in the charts already carries it).
donnees: [dette_futurs]
dataset:
  jeu: "dette_futurs"
  nom: "What futures for French public debt: European Commission projections, Government paths, sensitivities and an institutional matrix"
  description: "Path of French public debt with unchanged policy and stochastic distribution published by the European Commission (Debt Sustainability Monitor 2025), the Government's commitments and forecasts (October 2024 plan, 2027 draft budget) placed within that distribution, sensitivities to the balance, interest rates and growth calculated on the Commission's baseline, and an institutional matrix of nine operations (what changes, effect, who decides, applicable law, distribution, robustness, outcome), in French and English."
  couverture_temporelle: "2024/2036"
  couverture_spatiale: "France"
  variables:
    - {nom: "Public debt (Maastricht)", unite: "% of GDP", description: "Commission's unchanged-policy baseline, variants and percentiles; Government forecasts"}
    - {nom: "Percentile reached", unite: "percentile", description: "position of a Government path within the Commission's distribution, in level and in change since 2025"}
    - {nom: "Sensitivity", unite: "points of GDP or billion euros", description: "gap to the baseline in 2030 and 2035, one parameter changed at a time"}
    - {nom: "Institutional matrix", unite: "text", description: "nine operations × seven dimensions, source status for each cell"}
  sources:
    - "https://economy-finance.ec.europa.eu/publications/debt-sustainability-monitor-2025_en"
    - "https://www.budget.gouv.fr/documentation/documents-budgetaires"
    - "https://www.aft.gouv.fr/fr/encours-detaille-oat"
  mots: ["public debt", "France", "projections", "European Commission", "Debt Sustainability Monitor", "fiscal rules", "Eurobonds", "restructuring", "collective action clauses", "golden rule"]
  fichiers: ["dette_futurs.csv", "dette_futurs.json", "dette_futurs_matrice.csv"]
faq:
  - question: "What will French public debt be in 2030?"
    answer: "Nobody knows: the available figures are conditional projections. With unchanged policy, the European Commission projects {futurs.ref_2030}% of GDP in 2030; under shocks comparable to past ones, in 80% of the Commission's simulations debt would be between {futurs.p10_2030}% and {futurs.p90_2030}%. The Government forecasts {futurs.plf_2030}% in the 2027 draft budget, a path that assumes new measures."
  - question: "Would cancelling the debt held by the Banque de France reduce debt?"
    answer: "A cancellation that extinguishes the claim would lower measured debt; converting into interest-free perpetual bonds that keep their face value would not necessarily do so. In both cases the net saving is not secured: the cost of bank reserves, remunerated by the central bank, remains and changes hands. And, under the current Treaties, the State cannot impose the operation: neither the ECB nor the Banque de France may take instructions from a government."
  - question: "Would a restructuring of French debt be legal?"
    answer: "Government securities of more than one year created since 2013 carry collective action clauses: the State can change their terms with qualified majorities of holders, counted in principal; for a substantial change to a single line, three quarters of the principal present or represented, provided that two thirds of the outstanding principal are present or represented, with other rules across several lines (Art. D. 213-25-12 and D. 213-25-13 of the Monetary and Financial Code). According to our reconstruction from the Agence France Trésor's line sheets, {futurs.cac_part}% of the non-indexed nominal outstanding of bonds belongs to these lines. The clauses make a change possible; they guarantee neither creditors' consent nor the absence of higher interest rates afterwards."
ressource:
  type: ["quantitatif", "juridique-institutionnel"]
  refonte: "2026-11-09"
  conception: "docs/conception/dette-publique-quels-futurs.md"
  bloc: "dette"
  livres: ["dette-publique-qui-paie-vraiment"]
  rang: 36
  nature: "European Commission projections, Government forecasts, legal texts read and the author's calculations"
---

{{< dossier-dette volet="futurs" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Data updated on {{< futurs-val "date_donnees" >}}</span> European Commission projections published on {{< futurs-val "dsm_publie" >}}, forecasts of the 2027 draft budget. Download: <a href="/dette_futurs.csv">CSV</a> · <a href="/dette_futurs.json">JSON</a> · <a href="/dette_futurs_matrice.csv">matrix (CSV)</a> · <a href="#sources">method</a></p>

<div class="futurs-carte">

**Three questions to examine each operation.** A debt can disappear from a balance sheet while the obligations, costs or risks attached to it remain; a reform can also produce a real gain. To tell the two apart, each operation examined here goes through the same questions.

- **What effect?** Reducing the debt ratio, easing interest payments or transferring an obligation do not produce the same result.
- **Who decides?** Depending on the operation: the Government and Parliament, under European surveillance, or the agreement of the Council of the Union, the central bank, each Member State or creditors.
- **Who pays?** The taxpayers targeted, holders of securities and their savers, other States or later years.

[The nine operations, in three families →](#matrice)

</div>

## Where does the current path lead? {#trajectoire}

Three kinds of figures circulate about the future of debt, and they do not say the same thing. The European Commission projects debt **with unchanged policy**: with no new measure, what the ratio would become with only the decisions already taken. It is neither a forecast nor the most likely scenario, as the Commission itself writes. The Commission is not an outside observer: it oversees compliance with the European fiscal rules. Its baseline serves here as a common yardstick because it is published, dated and reproducible, not on any claim to neutrality. The Government publishes **commitments**, in October 2024 in its medium-term fiscal-structural plan, and **forecasts**, in 2026 in the debt report annexed to the 2027 draft budget: they assume measures not all of which have been passed. This page adds the third kind, **sensitivities**: what a single parameter would change, on the Commission's baseline.

{{< figure-svg fichier="dette-futurs-eventail-en" alt="Fan of projections of French public debt from 2025 to 2030: three nested bands, from the 10th to the 90th, the 20th to the 80th and the 40th to the 60th percentile, the Commission's unchanged-policy path rising through the middle, the Government's forecast rising until 2028 then falling back towards the lower part of the fan, and the October 2024 commitment, lower still." >}}French public debt, % of GDP: distribution of the paths simulated by the European Commission (10th to 90th percentiles), unchanged-policy path, 2027 draft budget forecast and October 2024 commitment. These paths do not start from the same point in 2025 and do not assume the same policies.{{< /figure-svg >}}

<div class="resultat-phrase">

**The result in one sentence.** With unchanged policy, the Commission projects debt at {{< futurs-val "ref_2030" >}}% of GDP in 2030, against {{< futurs-val "ref_2025" >}}% in 2025, and puts at {{< futurs-val "proba_2030_pct" >}}% the probability that debt in 2030 exceeds its 2025 level.

</div>

**Reading the fan.** The Government's forecast, {{< futurs-val "plf_2030" >}}%, sits in the lower half of this fan, around the {{< futurs-val "plf_2030_c_niv_ord" >}} percentile: about {{< futurs-val "plf_2030_c_niv" >}}% of the simulated paths end lower. The two exercises, however, rest on different policies, starting points and economic assumptions: this rank measures neither the specific effect of the Government's decisions nor their probability of success. If the economy goes through growth, interest-rate and budget swings similar to those France has already experienced, debt in 2030 would lie, in 80% of the Commission's simulations, between {{< futurs-val "p10_2030" >}}% and {{< futurs-val "p90_2030" >}}% of GDP, a gap of {{< futurs-val "ecart_p90_p10" >}} points: these are the chart's bands, which the Commission calculates up to 2030. These probabilities come from the Commission's model and assume no new measures. They do not measure the probability that a government keeps its commitments, and this page attributes none to a political choice. Beyond 2030 the Commission no longer publishes a fan: its unchanged-policy projection reaches {{< futurs-val "ref_2035" >}}% in 2035.

**The 2024 commitment, the 2026 forecast.** In October 2024 the Government committed to debt of {{< futurs-val "psmt_2027" >}}% of GDP in 2027; in 2026 it forecasts {{< futurs-val "plf_2027" >}}%, {{< futurs-val "ecart_promesse_2027" >}} points more, two years after the commitment.

<details class="repli"><summary>Where these paths sit within the Commission's fan</summary>

Placed within the Commission's fan, the 2024 commitment for 2029, {{< futurs-val "psmt_2029" >}}%, falls below the 10th percentile in level. But it started lower: the three paths do not start from the same point in 2025 ({{< futurs-val "ref_2025" >}}% for the Commission, {{< futurs-val "plf_2025" >}}% in the 2027 draft budget, {{< futurs-val "psmt_2025" >}}% in the 2024 plan). Measured as a change since 2025, the same commitment sits around the {{< futurs-val "psmt_2029_c_var_ord" >}} percentile, and the 2027 draft budget's forecast for 2030 around the {{< futurs-val "plf_2030_c_var_ord" >}}. A path's rank in the fan therefore also depends on its starting point.

</details>

## What the balance, interest rates and growth change {#leviers}

A debt path moves only through four channels: the primary balance, that is revenue minus spending excluding interest, the interest rate paid on the debt, nominal GDP growth, and operations on the stock of debt itself. Any reform, including a change of rule, acts on the path only through them. The chart applies a single change at a time to the Commission's baseline.

{{< figure-svg fichier="dette-futurs-leviers-en" alt="Horizontal bars showing the gap in debt in 2035 relative to the Commission's baseline, grouped into three families: primary balance, financing conditions and economic activity. A primary balance one percentage point of GDP higher every year would lower debt the most, in an accounting calculation drawn as a dotted outline; interest rates 0.2 percentage point lower would lower it little; rates one point higher or growth half a point lower would raise it about as much as stronger growth would lower it." >}}Gap in public debt in 2035 relative to the European Commission's baseline, in points of GDP, one parameter changed at a time (author's calculations on the Debt Sustainability Monitor 2025 baseline).{{< /figure-svg >}}

**The balance.** A primary balance 1 percentage point of GDP higher every year from 2028 to 2035 would lower debt by {{< futurs-val "solde_2030_pts" >}} in 2030 and by {{< futurs-val "solde_2035_pts" >}} in 2035. It is an accounting calculation: it assumes the adjustment neither slows growth nor changes interest rates, which it would partly do. One point of GDP of borrowed investment every year, with no effect on growth, would do the opposite: {{< futurs-val "invest_2035_pts" >}} more.

**Interest rates.** Market rates 0.2 percentage point (twenty basis points) lower on all new public borrowing would lower debt by {{< futurs-val "taux20_2035_pts" >}} in 2035 and the interest bill by about €{{< futurs-val "taux20_int_2035" >}} billion that year; ten basis points lower, by {{< futurs-val "taux10_2035_pts" >}}. A rise of one point would raise it by {{< futurs-val "taux100_2035_pts" >}}, and the interest bill by about €{{< futurs-val "taux100_int_2035" >}} billion. The effect is slow: a market rate first affects only short-term debt and the securities issued during the year, then the rest as it is rolled over.

**Growth.** Half a point of extra nominal growth every year would lower debt by {{< futurs-val "croiss_plus_2035_pts" >}} in 2035; half a point less would raise it by {{< futurs-val "croiss_moins_2035_pts" >}}. Growth is not a decision: it is an assumption, which modulates all the others. It works together with the interest rate: by the simple arithmetic of debt, with a zero primary balance and no stock-flow adjustments, the ratio rises when the average interest rate on the debt exceeds nominal growth and falls in the opposite case; a primary deficit or stock-flow adjustments can nevertheless reverse that result. Technical progress enters growth as one possible driver; this page assigns it no separately quantified effect.

These bars are not to be compared as equivalent efforts: a point of primary balance is a budgetary effort to be renewed every year, whereas an interest rate or growth cannot be decreed. They give the order of magnitude of each channel, not what a policy would cost or yield.

<details class="repli"><summary>How these sensitivities are calculated, and what they were tested against</summary>

The calculation follows the debt dynamics described by the Commission in the annex to its Debt Sustainability Monitor: short-term debt follows the market rate within the year, long-term debt only as it is rolled over; a balance shock passes through a fiscal multiplier and a cyclical component, except in the accounting calculations, where both are zero. Before writing the page, the calculation was checked against two variants published by the Commission (a rise in the gap between interest and growth, a financial crisis): it reproduces them within tolerances written in advance, and a deliberate error in the pass-through of rates makes it fail. It was also checked against the sensitivity published by the Agence France Trésor for a one-point rise in all rates: €{{< futurs-val "aft_an2" >}} billion of interest in the second year, €{{< futurs-val "aft_an5" >}} billion in the fifth, which the calculation finds within a few per cent; the first year (€{{< futurs-val "aft_an1" >}} billion) it does not, because of the issuance calendar: rate effects are therefore read only from the second year. No outside benchmark exists for a lasting balance shock: hence the accounting calculation.

</details>

## Changing the rules: who decides, who pays? {#matrice}

Proposals in the debate often promise to ease the debt other than through fiscal adjustment. The {{< futurs-val "n_operations" >}} operations below are examined one by one with the same grid: what they change, their effect when it can be calculated, who decides them, and the provisional outcome (a constraint reduced, shifted onto others, aggravated, or dependent on named conditions). Each line carries the status of what it states: a text read, a calculation, a result established elsewhere on this site, an inference, or what is not established. Applicable law, the distribution of costs and robustness unfold under each card; the complete table can be downloaded ([CSV](/dette_futurs_matrice.csv)).

{{< futurs-matrice >}}

## What the matrix brings out {#constats}

**Five distinctions for understanding these operations.** The four channels say how the effect on debt travels; these distinctions say what must be kept apart to judge each operation.

| What the operation changes | What must be distinguished |
|---|---|
| The budget flow | the effort each year and whom it falls on |
| European rules | the flexibility granted and the economic effect |
| Joint financing | the cost of borrowing and the transfer of risk |
| Existing securities | the fall in the accounting stock and the net economic cost |
| The currency | redenomination, the exchange rate and legal commitments |

**The same reform can reduce measured debt, shift burdens, change risks or produce opposite effects, depending on how it is implemented.** Of the {{< futurs-val "n_operations" >}} operations, none can be classified once and for all: most depend on a condition the grid names, the return on an investment, the actual cost of joint borrowing, the reaction of creditors or taxpayers. Changing the rules of debt does not amount to choosing between paying and not paying: each operation changes a set of rights, obligations, risks and capacities.

**Changing the rules can also change who decides.** Some operations lie mainly with French institutions, under European surveillance; others require the agreement of the Council of the Union, the central bank, each Member State or creditors. The possibility of acting depends as much on these agreements as on the economic result sought. Each card says who bears the cost (targeted taxpayers, bondholders and their savers, other States, later years) under "Who gains, who pays", in its fold-out.

**The economic size of a reform says nothing about its legal difficulty.** Excluding some spending from European monitoring of net expenditure requires amending a regulation, by qualified majority; joint borrowing, even capped, requires unanimity and the approval of each State; changing the definition of the reference deficit, unanimity in the Council.

**European law distinguishes three things the debate conflates:** flexibility in fiscal paths (extending the adjustment, treating investment), European borrowing (lending to a State or spending for the Union), and taking over another State's commitments, which the Treaties strictly limit. These are not three variants of the same reform.

## What these projections do not say {#limites}

- **Projection, forecast, sensitivity.** The Commission's baseline is a conditional unchanged-policy projection, not a forecast of the most likely outcome. The Government's paths are forecasts, resting on economic assumptions and on measures some of which have yet to be enacted. The sensitivities change one parameter at a time. None of these figures is certain.
- **One lever at a time.** The sensitivities and the matrix take operations one by one; no combination is calculated, whereas joint borrowing and a golden rule, or a restructuring and subsequent interest rates, interact.
- **A ratio does not measure welfare.** Spending can raise the ratio and improve public assets or avoid a future cost; a sale can lower it without making anyone richer. A gap in points of GDP is not an amount paid.
- **Feasible is not acceptable.** The matrix examines the known legal conditions, the agreements required and what remains to be established; it does not say what a majority would accept.
- **What remains to be read.** The statistical classification of an interest-free perpetual security, the Eurosystem's texts on a conversion, the creation orders of three index-linked bond lines, Article 65 of the Treaty on exceptions to the free movement of capital and the Conseil d'État's opinion on a differential wealth tax (2025) have not been read: the cards concerned say so.

<div class="encadre">

**The author's hypothesis, separate from the findings.** The findings above stand without it. The author reads them in the light of anthropy, which the author defines as follows:

{{< canonical-definition >}}

Applied to debt, this hypothesis asks whether a transformation of the debt system can reduce the constraint without transferring it elsewhere: to other taxpayers, other creditors, other States or other years. The matrix does not demonstrate it; it provides, operation by operation, the elements that would allow it to be tested.

</div>

<div class="retenir">

<p class="retenir__surtitre">Summary</p>

## Key points {#retenir}

With unchanged policy, the European Commission projects French public debt at {{< futurs-val "ref_2030" >}}% of GDP in 2030 and {{< futurs-val "ref_2035" >}}% in 2035; the Government's forecast for 2030, {{< futurs-val "plf_2030" >}}%, assumes new measures.

A path changes only through the primary balance, interest rates, growth or the stock. On the Commission's baseline, a primary balance one percentage point of GDP higher every year from 2028 to 2035 would lower the debt ratio by {{< futurs-val "solde_2035_pts" >}} in 2035; nominal growth half a point higher every year, by {{< futurs-val "croiss_plus_2035_pts" >}}; market rates twenty basis points lower, by {{< futurs-val "taux20_2035_pts" >}}. These are conditional sensitivities, not the guaranteed effects of a policy.

Changing the rules of the game spares none of these channels: depending on the operation, it can change the powers and agreements required, and reduce debt, shift its burden or worsen it. The matrix of {{< futurs-val "n_operations" >}} operations says so for each, with the status of every statement.

</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [Can public debt come down?](/en/can-public-debt-come-down/)
- [Who really pays public debt?](/en/who-really-pays-public-debt/)
- [What about elsewhere?](/en/public-debt-international-comparison/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="The four scenarios, told over ten years" avis="non" >}}
This page sets side by side, on a single baseline, what changing the rules of the debt game alters and who bears the cost. The book tells four possible futures up to 2035, from continuity to rupture, and what each would impose on households, savers and creditors. Its orders of magnitude rest on its own assumptions, different from the Commission baseline used here.
{{< /appel-livre >}}

## Where these figures come from {#sources}

European Commission, *Debt Sustainability Monitor 2025* (Institutional Paper 332, published on {{< futurs-val "dsm_publie" >}}), France country fiche: unchanged-policy path, deterministic variants and stochastic distribution, read from the fiche's spreadsheet, archived with its hash. Government: medium-term fiscal-structural plan 2025-2029 (October 2024) and the report on general government debt annexed to the 2027 draft budget, read from the archived documents. Agence France Trésor: sensitivity of the interest bill to a rise in rates, and the bond line sheets (nominal outstanding and creation order), read on 9 November 2026. Legal texts read on EUR-Lex and Légifrance: Treaties, Protocol No 12, Regulation (EU) 2024/1263, Decision 2020/2053, Monetary and Financial Code, the Court of Justice's Pringle judgment; they are cited in each card.

The Commission's and the Government's paths are read by the script from the archived sources; the sensitivities are calculated by the same script, on the Commission's baseline; the share of lines subject to collective action clauses is recalculated from the archived record of the Agence France Trésor's line sheets. Figures attributed to other authors in the matrix (International Monetary Fund, EU Tax Observatory, Institut de l'entreprise, Conseil d'analyse économique, France Stratégie's evaluation committee) are transcribed from their publications, checked against the archived documents. The script stops if a data point no longer meets the conditions on which the page's main sentences depend; their wording is subject to editorial review.

{{< reutiliser figures="figures_futurs" jeu="dette_futurs" sources="European Commission, French Government and Agence France Trésor" donnees="The European Commission's unchanged-policy path, variants and stochastic distribution for France, the Government's commitments and forecasts, and the sensitivities calculated on the Commission's baseline; the complete institutional matrix is a second CSV file." >}}
With unchanged policy, the European Commission projects French public debt at {{< futurs-val "ref_2030" >}}% of GDP in 2030 and {{< futurs-val "ref_2035" >}}% in 2035; the Government's forecast for 2030 ({{< futurs-val "plf_2030" >}}%) sits in the lower half of the fan of its projections. A path changes only through the primary balance, interest rates, growth or the stock; depending on the operation, changing the rules of the game can change the powers and agreements required, and reduce debt, shift its burden or worsen it. The Commission's baseline is an unchanged-policy projection, the Government's path a forecast that assumes new measures, the levers sensitivities: none of these figures is certain.
{{< /reutiliser >}}
