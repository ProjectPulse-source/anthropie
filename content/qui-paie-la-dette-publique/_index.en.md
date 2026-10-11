---
title: "Who really pays for public debt?"
url: /en/who-really-pays-public-debt/
description: "Who pays for public debt? Holding it is not paying for it: taxes, spending and inflation do not spread the adjustment across the same groups. Official French data."
chapo: "The same €{qp.exp_effort} billion adjustment falls on different households depending on the decision taken: through education, it weighs mostly on the least well-off; through taxes, on the best-off. Who pays for public debt depends on what it finances, how it is financed and the adjustments chosen to service it."
date: 2026-09-30
lastmod: 2026-10-11
donnees: [dette_officielle]
og_title: "Who really pays for public debt? — what the data show — S. Lalut"
og_image: "images/og-qui-paie-dette-en.jpg"
og_image_alt: "Share card: “Same adjustment, different payers” — the same €10 billion adjustment, as a % of the income of each standard-of-living decile, under three decisions: cutting education, raising taxes, cutting pensions (INSEE, 2023)."
# English version of part 2 of the public debt dossier (FR: content/qui-paie-la-dette-publique/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/qui_paie_donnees.json.
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html); tokens resolved at build time
  jeu: "qui_paie_donnees"
  nom: "Who pays for public debt: holdings, redistribution and exposure to the same adjustment"
  description: "Compilation derived from official series: public debt by government subsector (INSEE) and holders of French central-government marketable debt securities (Banque de France via Agence France Trésor); taxes, contributions and public transfers by standard-of-living decile and by age, distributional national accounts 2023 (INSEE); exposure of each decile to the same €{qp.exp_effort} billion adjustment under three decisions (taxes, pensions, education), an accounting profile, not a simulation, with its robustness tests."
  couverture_temporelle: "2020/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Taxes, contributions and public transfers by standard-of-living decile", unite: "euros per consumption unit"}
    - {nom: "Share of people who are net beneficiaries", unite: "% of people"}
    - {nom: "Exposure to the same adjustment, by decision", unite: "% of the decile's disposable income"}
    - {nom: "Holders of French central-government marketable debt securities", unite: "% at market value"}
  sources:
    - "https://www.insee.fr/fr/statistiques/8974371"
    - "https://www.insee.fr/fr/statistiques/8574663"
    - "https://www.aft.gouv.fr/"
  mots: ["public debt", "redistribution", "distributional national accounts", "INSEE", "who pays for public debt", "holders of public debt"]
  fichiers: ["qui_paie_donnees.csv", "qui_paie_donnees.json"]
faq:
  - question: "Is public debt really a problem?"
    answer: "The reassuring argument is a serious one: when the interest rate stays below growth, the debt ratio can stabilise, provided the deficit excluding interest — the primary balance — stays below a threshold that depends on the gap between the two rates and on the level of the debt. Beyond it, the ratio rises regardless. And even when stable, a debt has to be serviced every year: its financing and its adjustments distribute costs and benefits among taxpayers, users of public services, savers and generations. The useful question is then what it finances and who bears the adjustments — and it is answered configuration by configuration, not in principle."
  - question: "Is public debt a burden on future generations?"
    answer: "Not mechanically. The next generations inherit the obligations, but also what they financed — infrastructure, education, public assets — and part of the securities themselves, held directly or through French assurance-vie savings policies (life-insurance-based savings) — which does not necessarily neutralise the burden, since debt can also crowd out productive capital. The net transfer depends on the use: debt that finances current consumption with no lasting counterpart mostly passes on a cost; an investment they will benefit from can pass on more than it costs. What remains true in every case: the decision is taken without them."
  - question: "Who holds French public debt, and who receives the interest?"
    answer: "Central government accounts for {qp.etat_pct}% of public debt ({qp.periode_a}, INSEE). In {qp.det_periode}, its marketable securities were held, at market value, {qp.nonres_pct}% by non-residents, {qp.bafs_pct}% by resident banks, insurers and funds, {qp.autres_fr_pct}% by other resident holders — among them the Banque de France, whose share is not published (Banque de France, via Agence France Trésor). Holders are classified by residence, not nationality. For households, the French Treasury (Direction générale du Trésor), tracing the investments of assurance-vie policies, funds and banks, estimates that out of every {qp.tresor_sur} euros of financial wealth, {qp.tresor_dette} finances general government debt, mostly French. No published statistic, however, distributes the interest on public debt by income or wealth, and a share of the securities held is not a share of the interest paid. Holding is not paying: the holder advanced the funds and receives the return on them; the breakdown of holders does not say who bears the final burden."
  - question: "Should public debt be repaid?"
    answer: "Each security that matures is repaid, but the debt as a whole is refinanced: the government issues new securities to repay the old ones, and the stock evolves with the deficit. Repaying the whole stock is therefore a largely theoretical hypothesis. The operative question is what happens while the debt is continuously rolled over: who bears the interest, which budgets carry the adjustments, who inherits the obligations and what they financed. Refinancing renews a maturity on the terms of the day: it can lighten or increase the burden, and on its own it does not identify who will bear it."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 20
  nature: "Analysis based on public data"
  accueil: 2
---

{{< dossier-dette volet="2" >}}

{{< reutiliser-ancre >}}

The question arises in every indebted country. France is a useful case study for it: its statistical office, INSEE, publishes distributional national accounts that allocate taxes, contributions and public transfers across the income scale, which makes it possible to ask not only how much the debt costs, but how a given adjustment would be distributed across households.

Who pays for public debt? The answer changes with the decision taken to adjust it. The same €{{< qp-val "exp_effort" >}} billion adjustment weighs mostly on the least well-off households if it passes through education, mostly on the best-off if it passes through taxes, and almost equally on everyone if it passes through pensions. The size of the bill — stock, interest burden, average cost of the stock — is measured on another page of this dossier, [What does French public debt actually cost?](/en/cost-of-french-public-debt/); this one asks on whom it falls, what the data do, or do not, allow us to attribute, and what a real decision, considered for {{< qp-val "pens_annee" >}} and then set aside, shows.

{{< dette-chiffres >}}

## Depending on the decision, the adjustment falls on different households {#depending-on-the-decision-the-effort-does-not-fall-on-the-same-households}

The population is ranked from the least to the most well-off, then cut into ten groups of equal size, the **standard-of-living deciles**. The exercise distributes €{{< qp-val "exp_effort" >}} billion three times: through a rise in taxes on income and wealth, a cut in retirement pensions, and a cut in education spending. Each time, it allocates the sum in proportion to what each decile already pays or receives, then relates the result to that decile's income. The tax considered is the distributional accounts' category of "taxes on income and wealth": the CSG (a broad-based social contribution on income), income tax and the other taxes in this category, such as the CRDS, the housing tax or the tax on real-estate wealth. It is neither a forecast nor a measure under consideration: no behaviour and no feedback effect enter it. It is the current structure of these items, made comparable from one decision to another.

{{< figure-svg fichier="qui-paie-exposition-en" alt="Two panels. Above, three curves by standard-of-living decile: the cut in education spending starts very high in the first decile and falls steeply; the tax rise does the opposite and climbs in the top decile; pensions stay almost flat. Below, bars showing the ratio between the heaviest and the lightest decision for each decile: high at both ends, lowest in D7-D8." >}}INSEE, distributional national accounts, table CND.101 (standard-of-living twentiles, 2020-2023, base 2020); 2023 vintage. An accounting exposure profile, not a simulation.{{< /figure-svg >}}

{{< fig-actions id="exposition" >}}

**The ranking reverses from one decision to another.** A cut in education spending would represent {{< qp-val "exp_ens_d1" >}}% of the income of the poorest 10% and {{< qp-val "exp_ens_d10" >}}% of that of the richest; a rise in taxes on income and wealth would do the opposite, up to {{< qp-val "exp_fisc_d10" >}}% for the top decile. The contrast does not come only from the lower deciles' smaller incomes: in euros, the less well-off half would bear {{< qp-val "exp_masse_ens" >}}% of the cut in education spending, against {{< qp-val "exp_masse_fisc" >}}% of the tax increase. A cut in pensions would stay within a narrow band, from {{< qp-val "exp_pens_min" >}} to {{< qp-val "exp_pens_max" >}}%, sparing no group in particular. And "taxes" do not have a single profile: a rise in taxes on products, such as VAT, distributed in the same way, would also weigh more on the least well-off as a share of their income, {{< qp-val "exp_tva_d1" >}}% against {{< qp-val "exp_tva_d10" >}}% for the best-off. The profile favourable to the least well-off is therefore that of taxes on income and wealth, not of all taxation; and this calculation follows the same proportional convention, without being the final incidence of an actual VAT rise.

**An accounting exposure, not an observed loss.** The {{< qp-val "exp_ens_d1" >}}% for the first decile is the value of the education services that INSEE's accounts attribute to it by convention, relative to its income: neither a loss of income actually suffered, nor a measure of well-being. A tax rise takes away money; a spending cut takes away a service, whose value is imputed and whose real cost for each person depends on what is cut.

<div class="resultat-phrase">

**The result in one sentence.** "Who pays for the debt?" has no answer in itself; it has one per decision: the same adjustment weighs mostly on the least well-off if it passes through education, mostly on the best-off if it passes through taxes.

</div>

**In the middle of the scale, the choice of lever matters least.** For the {{< qp-val "exp_creux_zone_mots" >}} decile, a little above the middle, the average burden would change little from one decision to another: the heaviest would cost {{< qp-val "exp_ecart_creux" >}} times the lightest there. For the richest 10%, it would cost {{< qp-val "exp_ecart_d10" >}} times the lightest, and at least as much for the poorest 10%: at both ends of the scale, the choice of lever decides almost everything. These deciles would not bear less of the adjustment; changing the lever would simply alter their average exposure less, which does not describe the situation of each household in them. The convergence appears in all four vintages {{< qp-val "exp_millesimes" >}} (which share conventions and structures, and are therefore not independent replications), and it holds only for these three levers distributed in this way.

<details class="repli"><summary>Three tests of the trough in {{< qp-val "exp_creux_zone" >}}, and the limits of the exercise</summary>

**In twentiles.** With the population split into twenty groups instead of ten, the minimum still falls in the {{< qp-val "exp_creux_zone" >}} zone: in the {{< qp-val "exp_t1_rangs" >}} twentile depending on the year. The trough does not come from grouping by deciles.

**By pairs of levers.** The tax curve rises with the standard of living, the education curve falls: taken two at a time, they come closest in {{< qp-val "exp_t3_croise" >}}, and it is their crossing that makes the trough; the pensions curve, almost flat, passes close to both. The coefficient of variation and the range relative to the mean place the minimum in the same zone as the ratio of the heaviest to the lightest.

**Measured in percentage points of income** rather than as a ratio, the gap between the heaviest and the lightest decision is still smallest in {{< qp-val "exp_creux_zone" >}}. **Without pensions**, taxes and education alone come closest in {{< qp-val "exp_t3_croise" >}}: the trough owes nothing to the third curve. **With a fourth lever**, taxes on products, it stays in {{< qp-val "exp_creux_zone" >}}.

**With other forms of measures (calculation assumptions, not measures under consideration).** An education cut of the same amount for each decile, or concentrated where spending is already high, leaves the trough in {{< qp-val "exp_creux_zone" >}}; sparing the education of the first three deciles places it in {{< qp-val "exp_ens_epargne" >}} depending on the year; sparing their pensions leaves it in {{< qp-val "exp_creux_zone" >}}. A more progressive tax, distributed in proportion to the square of what each decile already pays, moves it to {{< qp-val "exp_t2_progressif" >}}, however. The trough therefore withstands the choice of measure and several distributions, but its location follows the progressivity of the measures: it is a result of the proportional scenario, not a general property of redistribution.

**The reference income only affects the level of the curves.** For a given decile, it is common to all three levers: the ratio of the heaviest to the lightest, and the points where two curves cross, do not depend on it. The gap measured in percentage points of income, however, does: with another denominator, its minimum could move.

**The limits.** A public service valued in euros is not income: education spending imputed to a household is not paid to it, and cutting it would not cost the household exactly that sum. The three decisions are proportional by construction; the figure says nothing about "taxes" or "public spending" in general. Finally, the first-decile point is excluded for the tax decision: income tax of the first twentile makes up {{< qp-val "exp_part_ir_v1" >}}% of the item there while the neighbouring twentiles are at zero, an atypical cell in the source. The gap for this decile, computed on the two other levers, is therefore a lower bound.

</details>

<span id="four-roles-not-to-be-confused"></span>
<span id="what-the-data-make-visible"></span>
<span id="creditors--financing-is-not-gaining"></span>

## Who borrows, who holds, who receives the interest {#creanciers}

Four questions are often confused: who borrows, who finances and receives the interest, through which mechanisms financing and adjustments operate, and who ultimately bears their effects. These are not four populations: the same person pays taxes, is treated in a public hospital and holds government securities through an assurance-vie policy. And "who pays" is always said relative to another decision: borrowing less would have meant another tax, another cut in spending, with their own losers.

{{< figure-svg fichier="qui-paie-detention-en" alt="Two separate panels of horizontal bars. Above, public debt by borrowing government subsector, at nominal value: central government far ahead. Below, holders of central-government marketable securities, at market value: non-residents ahead." >}}Two distinct scopes: A at nominal value (INSEE), B at market value (Banque de France, via Agence France Trésor). The values come from the same register as the figure on p. 101 of the book.{{< /figure-svg >}}

{{< fig-actions id="detention" >}}

**Who borrows, who holds.** Central government accounts for most of the public debt: {{< qp-val "etat_mdeur" >}} billion euros out of {{< qp-val "total_mdeur" >}}, or {{< qp-val "etat_pct" >}}% ({{< qp-val "periode_a" >}}). In {{< qp-val "det_periode" >}}, its marketable securities were held {{< qp-val "nonres_pct" >}}% by non-residents; resident banks, insurers and funds together held {{< qp-val "bafs_pct" >}}%; the other resident holders, {{< qp-val "autres_fr_pct" >}}%, include the Banque de France, whose share the source does not publish. The two panels cannot be combined: one is at nominal value, the other at market value.

**Who receives the interest: what is observed, what can be approximated, what is unknown.** We *observe* the direct holders, classified by residence: a stock captured at a given date, not the flow of coupons, which depends on the securities held and when they were issued. We can *approximate* the indirect holders: tracing the investments of assurance-vie policies, funds and banks to their final use, the French Treasury (Direction générale du Trésor) estimates that out of every {{< qp-val "tresor_sur" >}} euros of French households' financial wealth, {{< qp-val "tresor_dette" >}} finances general government debt, mostly French ([*Trésor-Éco* no. {{< qp-val "tresor_numero" >}}, January 2026](https://www.tresor.economie.gouv.fr/Articles/2026/01/08/que-finance-l-epargne-financiere-des-menages-francais), in French). We do *not know* which households receive that interest: no published statistic distributes it by income or wealth, which would require following each security, its return and its intermediaries. Two readings are therefore ruled out: {{< qp-val "nonres_pct" >}}% of the securities is not {{< qp-val "nonres_pct" >}}% of the interest, and holdings of financial assets by decile do not tell each decile's share of that interest. The absence of this breakdown does not mean that this income is negligible: it limits what can be asserted. Two further points: today's holder is not necessarily the one who lent at issuance, since a security is then traded on the market; and the securities held by the Banque de France under Eurosystem programmes cannot be analysed like those of a private creditor.

<details class="repli"><summary>Residence is not nationality, and financing is not gaining</summary>

**Financing is not gaining.** The creditor advanced the funds: interest pays for that advance, for time and for risk. Its real return takes account of inflation and of changes in the security's value, and its advantage over another investment is measured at a comparable horizon and risk. "We owe it to ourselves" is therefore only partly true, and does not say which of "us" receive and which finance.

The published breakdown classifies holders by **residence**, not nationality: a "non-resident" can be a foreign fund managing the savings of French households, and a French household can hold government securities without knowing it, through its assurance-vie policy. The Banque de France statistic on the long-term securities of general government as a whole covers a different scope from Agence France Trésor's, which is limited to central government's marketable securities: the two shares are not interchangeable.

</details>

## Who contributes, who receives today {#redistribution}

INSEE's distributional national accounts allocate, for {{< qp-val "cd_annee" >}}, taxes, contributions and public transfers across **standard-of-living deciles** — the population ranked from the least to the most well-off, then cut into ten groups of equal size. Amounts are expressed **per consumption unit** (CU), the unit that makes households of different sizes comparable: a single person counts as 1 CU, a couple with two children under 14 as 2.1.

{{< figure-svg fichier="qui-paie-redistribution-en" alt="Bars by standard-of-living decile, in 2023. Above zero, transfers received, at a similar level from one decile to the next; below zero, taxes and contributions, which rise steeply from the first to the top decile." >}}INSEE, distributional national accounts 2023 (*Insee Analyses* no. 118, 16 April 2026, figure 1c), in euros per consumption unit.{{< /figure-svg >}}

{{< fig-actions id="redistribution" >}}
{{< qp-tableau-redistribution >}}

Taxes and contributions range from €{{< qp-val "d1_prel" >}} per CU for the poorest 10% to €{{< qp-val "d10_prel" >}} for the richest 10%, about {{< qp-val "ratio_prel" >}} times more. Transfers received — cash benefits and public services valued in euros — vary much less: they stay between €{{< qp-val "recu_min" >}} and €{{< qp-val "recu_max" >}}, with no regular progression. What is paid tracks the standard of living; what is received, much less so. These taxes and contributions are not payments recorded one by one: besides income tax and social contributions, they include taxes on products, such as VAT, and taxes on production, which INSEE attributes to households by convention.

<div class="resultat-phrase">

**Where the debt enters these accounts.** In {{< qp-val "cd_annee" >}}, transfers attributed to households exceed taxes and contributions by {{< qp-val "solde_mdeur" >}} billion euros, and INSEE links this gap to public borrowing: it is the part of the year's extended income that is not financed by the same year's taxes and contributions. These {{< qp-val "solde_mdeur" >}} billion are not the {{< dette-val "interets_annee" >}} interest burden ({{< dette-val "interets_mdeur" >}} billion): year, scope and nature differ, and the closeness of the two figures is a coincidence.

</div>

<details class="repli"><summary>A balance allocated by convention, financed on credit, which does not say who will pay tomorrow</summary>

This total covers the scope of the distributional accounts, which is not that of the public deficit: the two amounts are not interchangeable. In this construction, the gap raises households' extended standard of living for the year (a present benefit, financed on credit), but these are not {{< qp-val "solde_mdeur" >}} billion of identifiable payments: it is a balance allocated by convention, which INSEE attributes half to lower taxes and contributions and half to additional transfers when it computes a standard of living "net of borrowing". The figures on this page show current transfers, before that adjustment. The balance does not imply that the beneficiaries of redistribution "created" this debt, nor that their position says who will repay it.

</details>

{{< figure-svg fichier="qui-paie-solde-net-en" alt="Two panels. Above, the balance of public transfers by standard-of-living decile, defined as what the group pays in minus what it receives: negative, hence net beneficiary, for the first deciles, positive, hence net contributor, for the last ones, very strongly so for the top decile. Below, the share of people who are net beneficiaries, falling from the first to the top decile." >}}INSEE, distributional national accounts 2023 (figure 2a). Two units, two panels: euros per consumption unit, then share of people.{{< /figure-svg >}}

{{< fig-actions id="solde-net" >}}

**Net contributors, net beneficiaries.** On average per CU, transfers received exceed taxes and contributions in each of the first {{< qp-val "net_benef_n_mots" >}} deciles (by €{{< qp-val "net_d1" >}} per CU in the first), and the balance tips at decile {{< qp-val "net_bascule" >}}: in the last {{< qp-val "net_contrib_n_mots" >}}, it is the reverse, and the top decile pays in, on average, €{{< qp-val "net_d10" >}} per CU more than it receives.

<div class="resultat-phrase">

**A group average does not describe its members.** {{< qp-val "benef_ensemble" >}}% of people are net beneficiaries that year, {{< qp-val "benef_d1" >}}% in the first decile and {{< qp-val "benef_d10" >}}% in the top one. But they are a majority only in the first {{< qp-val "benef_majo_n_mots" >}} deciles: in decile {{< qp-val "benef_dernier_moyen" >}}, which receives on average €{{< qp-val "net_dernier_moyen" >}} per CU more than it pays in, they are only {{< qp-val "benef_dernier_moyen_pct" >}}%. **The sign of an average does not reveal the situation of the majority.** A group can receive more than it pays in on average while most of its members pay in more than they receive: it is enough for what net beneficiaries receive on average to outweigh what the others pay in on average. The grouped data do not say how these balances are distributed.

</div>

Receiving more than one pays in, on average, therefore offers no protection from an adjustment: position in today's redistribution and exposure to tomorrow's decision are two distinct rankings.

<details class="repli"><summary>Conventions: the balance of one year, not of a lifetime; public services imputed, not measured; redistribution as a whole, not the specific effect of the debt</summary>

This is the balance of one **year**, not of a lifetime: retirement pensions count as current benefits. Transfers include public services — health care, education, collective services — valued in euros and allocated by statistical imputation, not a record of the services each person used; the share of net beneficiaries depends on this at the margin. Income "before transfers" is a step in the calculation, not the income each person would have in an economy without taxes or public services. And this balance describes redistribution as a whole, not the specific effect of the debt.

</details>

<details class="repli"><summary>By household age: a snapshot of the year, not a lifetime balance</summary>

{{< figure-svg fichier="qui-paie-age-en" alt="Bars by household age group, in 2023: transfers received rise with age, moderately up to 64 then very sharply for households aged 65 or over; taxes and contributions paid rise up to the 50-64 group, then drop for the oldest group." >}}INSEE, distributional national accounts 2023 (figure 1e). Groups by average age of the adults in the household.{{< /figure-svg >}}

{{< fig-actions id="age" >}}

In {{< qp-val "cd_annee" >}}, under these conventions, households whose adults are on average 65 or over receive €{{< qp-val "age_recu_65" >}} per consumption unit in transfers — of which €{{< qp-val "age_esp_65" >}} in cash benefits, pensions included — and pay €{{< qp-val "age_prel_65" >}} in taxes and contributions, against €{{< qp-val "age_prel_5064" >}} for households aged 50 to 64. Pensions partly correspond to entitlements earned over a career, counted here as current benefits; a household's age is not the retirement status of each of its members, and a high amount of imputed health care also reflects greater needs. This snapshot designates no payer of tomorrow.

</details>

## Through which channels the burden can be distributed

Four mechanisms can change the burden of the debt and its distribution, and they combine. The first two belong to **ordinary budget adjustment**, decided every year: **taxes and contributions** — additional taxes and contributions, or tax cuts forgone — and **spending and benefits** cut, frozen or postponed. The third is not decided alone: **unanticipated inflation** reduces the real value of claims already issued and shifts part of the burden onto their holders and onto poorly indexed incomes. The fourth is an extreme case: **restructuring** imposes a first-round loss on the holders of the securities, who may pass it on to their shareholders, policyholders or savers.

{{< figure-svg fichier="qui-paie-mecanismes-en" alt="Diagram without quantities: the burden of the debt and its distribution lead, through arrows of equal thickness, to four mechanisms grouped into three families — ordinary budget adjustment (taxes and contributions, spending and benefits), unanticipated inflation, a price effect not decided alone, and restructuring, an extreme case; refinancing renews the maturity at the rates of the day; alongside, what the debt financed." >}}A diagram of possible mechanisms: no relative weight or causal effect is measured in it.{{< /figure-svg >}}

{{< fig-actions id="mecanismes" >}}

Refinancing, for its part, renews a maturity on the terms of the day: it can lighten or increase the burden, without designating who will bear it. And set against these costs is what the debt financed: services, benefits and investment benefit households today and tomorrow, and an analysis that counted only the costs would describe only half of the balance sheet.

<details class="repli"><summary>Why only unanticipated inflation transfers the burden, and what works in the opposite direction</summary>

The inflation expected when a security's rate was set tends to be already built into the rate required at issuance, and then makes no transfer. It is the gap between realised inflation and that expectation that reduces the real value of nominal claims already issued. Two mechanisms work in the opposite direction: inflation-linked securities see their cost rise with prices, and refinancing takes place at the new rates. The net effect therefore depends on the indexed share, on the refinancing calendar and on what was anticipated — and France does not choose its inflation alone. Not to be confused with the effect of inflation on the debt *ratio*, which works through nominal GDP and, for its part, designates no loser. The list of channels is not exhaustive: growth, asset sales and financing conditions also play a role, and history also offers cases of financial repression, which constrains returns.

</details>

## Three hypotheses to be tested {#hypotheses}

The channels say where the burden can pass; three stronger hypotheses circulate about whom it would reach. None is established by the data on this page, and each calls for its own test.

### Future generations — what they inherit

Debt converts present spending into future obligations: those who come after inherit them without having taken part in the decision. But they also inherit what it financed and part of the securities themselves: the net transfer is not measured here.

<details class="repli"><summary>What the net transfer depends on, and what net debt does not say</summary>

The next generations inherit the infrastructure, education and public assets financed, and securities that their parents hold directly or through assurance-vie. This does not necessarily neutralise the burden: some models identify a channel through which debt crowds out productive capital, which this page does not measure for France. The net transfer depends on the use, the financing, the claims passed on and the alternative chosen. Net debt as published by INSEE does not settle the matter either: it deducts only certain financial assets, not roads, human capital or the environment. The page [Is public debt a burden on future generations?](/en/public-debt-future-generations/) breaks down, in the accounts, what deficits were used for, without saying which borrowed euro paid for which expense.

</details>

### Less mobile groups — a hypothesis to be tested

Households and firms that can move their income, wealth or activity escape a levy more easily than employees, retirees or users of a local public service. Hence the hypothesis: when adjustment follows the line of least resistance, it **may** weigh more on those who cannot leave.

<details class="repli"><summary>To test it: groups defined in advance, a specified adjustment, a fixed measure</summary>

Testing it requires defining these groups before observing the adjustment, specifying the adjustment studied and fixing a measure of effort; the hypothesis would be weakened by an adjustment falling mainly on other groups, or by compensation granted to the losers. Geographical mobility, mobility of the tax base and the capacity to replace a public service are three distinct properties. The territorial channel is examined on the page [Public debt: why are local authorities the adjustment variable?](/en/local-government-debt/)

</details>

### Investments with deferred benefits — a mechanism to be established case by case

A budget constrained by debt service **may encourage the postponement** of spending whose benefits are distant and whose postponement is politically cheap: research, maintenance of public assets, training, the ecological transition. The mechanism is plausible, not established.

<details class="repli"><summary>Plausible, not established: no aggregate measures an investment prevented by interest payments</summary>

It remains to be established decision by decision (which spending, postponed by which decision, for which budgetary reason), since no aggregate measures an investment prevented by interest payments. Where it is established, it compounds the transfer: the benefit that was never built adds to the obligations passed on, and appears in no stock of debt.

</details>

<span id="the-objections-that-matter"></span>

## A real, dated decision {#decision-reelle}

<aside class="encadre">

**A real example, distinct from the theoretical exercise.** [Article 44](https://www.assemblee-nationale.fr/dyn/17/textes/l17b1907_projet-loi.pdf) of France's 2026 social security financing bill provided that basic-scheme pensions would not be uprated in {{< qp-val "pens_annee" >}}: a coefficient "equal to one". The provision was set aside during the parliamentary process: the [2026 social security financing act](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053226384), promulgated on 30 December 2025, contains no freeze, and the [interministerial instruction of 15 December 2025](https://legislation.lassuranceretraite.fr/Pdf/instruction_ministerielle_2025_174_15122025.pdf) uprates these pensions on 1 January {{< qp-val "pens_annee" >}} by a coefficient of {{< qp-val "pens_coef" >}}, or {{< qp-val "pens_taux" >}}%, "in accordance with the law in force" (all three texts in French).

This is a decision of the "pensions" type, considered and then set aside. Two limits prevent the exercise from applying to it directly: a freeze on basic pensions alone does not have the profile of a cut distributed in proportion to all pensions, and nothing in these texts links the measure considered to the debt rather than to the social security deficit. A real budget combines revenue, contributions, benefits, spending and borrowing, and generally does not allow a given tax to be linked to a euro of interest. Nor, since it was never adopted, can this measure show an incidence actually borne: that would require a measure that was applied, and the situation that would have prevailed without it. The three €{{< qp-val "exp_effort" >}} billion decisions on this page are calculation assumptions, not a description of the choices made in {{< qp-val "pens_annee" >}}. Fiscal policy as a whole is examined on the page [Can public debt come down?](/en/can-public-debt-come-down/)

</aside>

## What these data do not allow us to establish

No statistic says, on its own, who ultimately bears the burden of French debt: the final incidence of a euro of interest depends on the adjustments chosen year after year, and on the alternative they are compared with. A current distribution of taxes and benefits describes who contributes and who receives today; it does not identify the future payers. An average per consumption unit is not an individual bill. What can be established is the effect of a specific decision — a reform, a freeze, a postponement — on groups defined in advance: it is at that level that "who pays?" receives verifiable answers.

{{< confrontation-recherche verifie="2026-09-30" publie="oui" resume="the direction of the spending/tax contrast recurs in consolidations actually observed; the inherited-claim argument is challenged by the crowding-out of capital" >}}
**Measured here.** An accounting profile: the same €{{< qp-val "exp_effort" >}} billion adjustment distributed in proportion to what each decile already pays or receives, according to INSEE, with no behaviour or feedback effects. The literature tests the readings drawn from it, not the profile itself.

**Consistent with.** The direction of the contrast between spending and taxes: in fiscal consolidations actually observed in 18 industrialised countries, France included, from 1978 to 2009, net income inequality rises; spending cuts appear unfavourable, tax rises equalising, although the latter effect is not significant in the baseline specification (Agnello and Sousa). The postponement of investment: in Breunig and Busemeyer's sample, a heavier interest burden goes with a decline in the share of public investment in favour of pensions, postponing an investment being politically less costly than cutting an entitlement. The role of use: in Diamond's model, borrowing to acquire physical capital makes the government a mere intermediary between savers and entrepreneurs, with no effect.

**Challenged by.** Any reading in which the inherited claim would neutralise the burden: in the efficient case of Diamond's model, where the interest rate exceeds population growth, domestically held debt lowers long-run welfare **more** than external debt, because it takes the place of productive capital in people's wealth. Barro, who defends the opposite view, bases it on voluntary transfers between parents and children, operative for most people, and acknowledges that in 1989 most economists still leaned towards the standard models. The magnitude: in Agnello and Sousa's breakdown, it is the largest tax rises that are associated with a significant fall in inequality, and the effects tend to disappear within two years. The "tax" curve read as final incidence: in 55,082 firms in nine European countries, from 1996 to 2003, about half of a rise in corporate income tax falls in the long run on wages (Arulampalam, Devereux and Maffini) — a different tax from the one on this page, but the same gap between legal and final incidence.

**Not established.** That less mobile groups bear more of the adjustment: the corporate tax study measures wage bargaining, and its only mobility contrast, between multinationals and independent firms, is not significant. That only unanticipated inflation transfers the burden: we did not find, in the texts examined, a test separating anticipated from unanticipated inflation. Finally, the page's "education" exposure has no observed equivalent: a cash income indicator does not directly value a loss of public service.

**References read**

- Agnello, L. and Sousa, R. M., "How Does Fiscal Consolidation Impact on Income Inequality?", Banque de France working paper no. 382, 2012 (published in the *Review of Income and Wealth*, 60(4), 2014).
- Breunig, C. and Busemeyer, M. R. (2012), "Fiscal austerity and the trade-off between public investment and social spending", *Journal of European Public Policy*, 19(6), pp. 921-938.
- Arulampalam, W., Devereux, M. P. and Maffini, G., "The Direct Incidence of Corporate Income Tax on Wages", revised manuscript, February 2012 (published in the *European Economic Review*, 56(6), 2012).
- Diamond, P. A. (1965), "National Debt in a Neoclassical Growth Model", *American Economic Review*, 55(5), pp. 1126-1150.
- Barro, R. J. (1989), "The Ricardian Approach to Budget Deficits", *Journal of Economic Perspectives*, 3(2), pp. 37-54.
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## What to take away

**"Who pays?" has one answer per decision, and the choice matters most at the ends of the scale.** The same adjustment falls on the least well-off through education, on the best-off through taxes; in the middle of the scale, the three levers studied produce similar exposures. Naming the decision and the alternative turns an opinion into a verifiable statement.

**Holding is not paying, and interest can be traced only so far.** Direct holders are observed, indirect holders approximated through household savings, but no statistic says which households receive the interest: the breakdown of holders tells us where the interest goes, never how it is financed.

**A group average does not describe its members.** A decile can receive more than it pays in *on average* while most of its members pay in more than they receive. A statistic by decile answers "how is the total distributed?", not "what does a person in this decile experience?".

</div>

<div class="prolongements" role="group" aria-label="Further reading in this dossier">
<p class="prolongements__titre">Further reading in this dossier: two applications of "who pays?"</p>
<a class="prolongements__carte" href="/en/local-government-debt/"><b>Local authorities</b><span>How a constraint on central government can pass down to local authorities that carry little debt but are tightly regulated.</span></a>
<a class="prolongements__carte" href="/en/public-debt-future-generations/"><b>Future generations</b><span>When does debt really amount to a transfer to those who come after?</span></a>
</div>

## Frequently asked questions {#questions}

{{< faq-visible >}}



{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="This analysis is developed in the book" avis="non" >}}
This page sets out the method: one answer per decision, creditors traced as far as the data allow, and what would need to be observed to reach a conclusion. The book applies it to the French case — the transfer over time, creditors, public services — and extends it with scenarios for 2025-2035. The book exists in French only.
{{< /appel-livre >}}

## Where these figures come from {#sources}

- **Redistribution by decile and by age**: Mathias André, Alexis Barrau and Thomas Renaud (INSEE), "Revenus des ménages élargis à l'ensemble de l'économie en 2023", *Insee Analyses* [no. 118](https://www.insee.fr/fr/statistiques/8974371), 16 April 2026 (figures 1c, 1e and 2a), in French.
- **Exposure to the same adjustment**: INSEE, distributional national accounts, [table CND.101](https://www.insee.fr/fr/statistiques/8574663), standard-of-living twentiles, 2020-2023, base 2020; the author's calculation, with robustness tests published with the data.
- **Debt by level of government**: INSEE, *Informations rapides* no. 79, quarterly Maastricht debt of general government, 27 March 2026, {{< qp-val "periode_a" >}}.
- **Holders of central-government securities**: Banque de France, via [Agence France Trésor](https://www.aft.gouv.fr/), {{< qp-val "det_periode" >}}.
- **Households' indirect claims**: French Treasury (Direction générale du Trésor), "Que finance l'épargne financière des ménages français ?", [*Trésor-Éco* no. {{< qp-val "tresor_numero" >}}](https://www.tresor.economie.gouv.fr/Articles/2026/01/08/que-finance-l-epargne-financiere-des-menages-francais), 8 January 2026.
- **Pension uprating in {{< qp-val "pens_annee" >}}**: [2026 social security financing bill](https://www.assemblee-nationale.fr/dyn/17/textes/l17b1907_projet-loi.pdf), no. 1907, article 44; [act no. 2025-1403 of 30 December 2025](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053226384) on social security financing for 2026; [interministerial instruction DSS/3A/DB/6BRS/2025/174](https://legislation.lassuranceretraite.fr/Pdf/instruction_ministerielle_2025_174_15122025.pdf), 15 December 2025.

Every figure on this page is read from these documents by a generator that checks their fingerprint, not copied by hand; the compiled data can be downloaded from the "Reuse" block below.

## Where this analysis comes from

{{< canonical-definition >}}

Applied to public finances, this hypothesis is formalised in the working paper [AWP-03 — *Public debt and anthropy: who really pays for disorder?*](/en/awp/awp-03/) (DOI: 10.5281/zenodo.19434094, open-access PDF). The working paper [AWP-09](/en/awp/awp-09/) tests this reading against public accounts: the incidence of the same fiscal effort depends on the instrument chosen, but the asymmetry between mobile and captive households lies beyond what the accounts can test, since they do not observe the former escaping.

{{< reutiliser figures="figures_qui_paie" jeu="qui_paie_donnees" sources="INSEE and Banque de France via Agence France Trésor" donnees="Holdings of public debt (the book's register, sources INSEE and Banque de France) and INSEE's 2023 distributional national accounts, with their periods, units and conventions, and the robustness tests of the exposure profile." >}}
How the effects of public debt are distributed depends on what it finances, how it is financed and the adjustments chosen to service it; some configurations may shift costs onto groups less able to avoid them. The available data show who borrows, who holds central-government securities and who contributes or receives today — not who will bear the final burden. A loss can only be attributed to a specific decision, compared with its alternative.
{{< /reutiliser >}}
