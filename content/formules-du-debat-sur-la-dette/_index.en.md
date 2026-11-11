---
title: "What are the claims of the French debt debate worth?"
url: /en/public-debt-debate-claims/
description: "Eleven numerical cases from the French National Assembly debate of 8 September 2025, tested against the data available that day. Many amounts withstand checking, but changing the date, scope or unit is often enough to change the answer, and measuring a change is enough neither to identify its cause nor to justify a decision."
chapo: "On 8 September 2025, in the French National Assembly, every group invoked the figures on public debt. Many amounts withstand checking. But changing the date, the scope or the unit is often enough to get another answer, and measuring a change is enough neither to identify its cause nor to justify a decision. Eleven cases, tested against the data available that day, show how the same figure can support different conclusions, not all of them demonstrated. The campaign texts of the candidates for the 2027 presidential election, put through the same tests, run into the same measurement difficulties."
date: 2026-11-02
og_title: "What are the claims of the French debt debate worth? — S. Lalut"
og_image: "images/og-dette-formules-en.jpg"
og_image_alt: "Share card: “Eleven claims from the French debt debate, tested” — monthly gap between the ten-year yields of France and Greece, from January 2024 to 2026, negative until spring 2025, positive in the month of the debate of 8 September 2025."
# English mirror of /formules-du-debat-sur-la-dette/ (02/11/2026). Same calculation, same tokens (affichage_en block).
# Quotations are the author's translations of the official French record.
donnees: [dette_formules]
dataset:
  jeu: "dette_formules"
  nom: "Eleven claims from the French public debt debate (National Assembly, 8 September 2025) tested against official series"
  description: "For eleven numerical claims from the debate of 8 September 2025: the question they ask, the verdict on that question, the neighbouring question that changes the verdict and the qualification of the conclusion drawn. Series included: general government balance since 1949 (Insee), deficit and change in debt 1996-2025, windows of spending and revenue (May 2025 accounts and revised accounts), increase in debt by presidency, monthly ten-year yields of France, Greece and Germany (Eurostat) and daily (Banque de France, Bank of Greece), interest and education spending under three scopes, interest projections (Court of Audit, Government), counts from the inventory of the debate; for the campaign texts of the candidates for the 2027 presidential election, counts by register and numerical statements tested at the date of their text, with the address and fingerprint of each document."
  couverture_temporelle: "1949/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Verdict per claim", unite: "text", description: "question asked, verdict, other question, qualification of the conclusion"}
    - {nom: "Ten-year yield gap, France minus Greece", unite: "percentage point", description: "monthly averages, Eurostat"}
    - {nom: "General government net lending or borrowing", unite: "billion euros and % of GDP", description: "annual since 1949, Insee"}
    - {nom: "Increase in Maastricht debt", unite: "billion euros", description: "by starting date, as of 8 September 2025 and revised"}
  sources:
    - "https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance"
    - "https://www.insee.fr/fr/statistiques/2381402"
    - "https://ec.europa.eu/eurostat/databrowser/view/irt_lt_mcby_m/default/table?lang=en"
    - "https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2025"
    - "https://www.banque-france.fr/en/statistics/rates-and-prices"
  mots: ["public debt", "public debate", "fact-checking", "government deficit", "debt interest", "interest rates", "Greece", "French National Assembly", "François Bayrou"]
  fichiers: ["dette_formules.csv", "dette_formules.json"]
faq:
  - question: "Were the figures quoted in the National Assembly on 8 September 2025 wrong?"
    answer: "The amounts are often accurate or close to the available references: “over €1,000bn of extra debt since 2017”, “no balanced budget for fifty-one years”, “higher rates than Greece”. That does not automatically make the propositions they serve accurate: the verdict often changes with the date, the unit, the scope or the year, and the conclusion drawn needs further evidence. Only one error of definition is established: debt service defined as including repayment of principal, then quantified without it."
  - question: "Was France borrowing at higher rates than Greece in September 2025?"
    answer: "Yes. On the day of the debate, 8 September 2025, France borrowed at ten years at {form.f8_tec8}% (Banque de France) and Greece at {form.f8_hdat8}% (Bank of Greece). On 4 September, the Bank of Greece, using the same measure for both countries, gave {form.f8_j4_fr}% against {form.f8_j4_gr}%. France had moved above in {form.f8_premier}, as a monthly average; Greece moved above it again from {form.f8_dessous}. The market price alone does not show that one country is weaker than the other."
  - question: "Does a 3% deficit stop debt from rising?"
    answer: "Not in euros: a 3% deficit is a borrowing requirement of about €{form.f16_eur}bn a year, which adds to the debt give or take stock-flow adjustments. As a share of GDP, it stabilises the ratio only if nominal growth exceeds a threshold, about {form.f16_seuil24}% with the 2024 ratio and no gap between deficit and debt increase. Growth exceeded that threshold in 2024 ({form.f16_g24}%), not in 2025 ({form.f16_g25}%, known after the debate). In July 2025 the French Court of Audit warned that getting back below 3% would not, on its own, be enough to ensure debt sustainability."
  - question: "How does this relate to the book Dette publique : qui paie vraiment ?"
    answer: "Chapter 9 of the book (in French) analyses these claims through language: who speaks, by what right, closing off which options. This page tests them against the accounts. The book was put through the same tests: its central figures hold, some steps from figure to cause are not established."
ressource:
  type: ["explicatif-causal", "quantitatif"]
  conception: "docs/conception/formules-du-debat-sur-la-dette.md"
  refonte: "2026-11-02"
  bloc: "dette"
  livres: ["dette-publique-qui-paie-vraiment"]
  rang: 50
  nature: "Public claims tested against official series (National Assembly, Insee, Eurostat, Court of Audit)"
  prolongement: true
dossier_dette: prolongement
dossier_dette_titre: "What are the debate's claims worth?"
dossier_dette_role: "8 September 2025, eleven claims"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Computed: {{< form-val "date_donnees" >}}</span> Full record of the sitting of 8 September 2025 (French National Assembly); general government accounts (Insee, Eurostat); ten-year yields (Eurostat, Banque de France, Bank of Greece); Court of Audit, Government, Senate. Download: <a href="/dette_formules.csv">CSV</a> · <a href="/dette_formules.json">JSON</a> · <a href="#sources">method</a></p>

## More money for interest than for education? {#interets-education}

On 15 July 2025, the French government sent Parliament its spending ceilings for the following year. Page 3 contains one sentence: the debt brings “a debt charge for general government as a whole of more than €66bn, which today exceeds the budget of the Ministry of Education”. Eight weeks later, in the National Assembly, Laurent Wauquiez (Droite républicaine) turned it into a forecast: “At this rate, we shall soon be spending more on paying interest on the debt than on educating our children.”

The amounts in the government's sentence are accurate, and it names both scopes. Yet it compares two things of different size: the interest paid by **all** public administrations (central government, social security, local authorities) and the budget of **one** government ministry. The comparison is not like for like. It therefore does not allow anyone, without changing the question, to assert that France spends more on interest than on education.

Measured each time on the same scope, the comparison gives two answers. For general government as a whole, the two lines of spending are nowhere near crossing: in {{< form-val "f4_an" >}}, interest amounted to {{< form-val "f4_r" >}}% of education spending (€{{< form-val "f4_int" >}}bn against €{{< form-val "f4_ens" >}}bn). The Court of Audit projects €{{< form-val "f4_cour29" >}}bn of interest in 2029: still less than education spending in {{< form-val "f4_an" >}}, and a crossing would also require the latter to fall. For the central government alone, the gap narrows. In 2025 its debt charge was {{< form-val "f4_r_etat" >}}% of the appropriations of the “school education” programme, excluding pensions. The same July report set the 2026 ceiling of the budget programme that carries the debt charge at €{{< form-val "f4_ef26" >}}bn, against €{{< form-val "f4_es26" >}}bn for school education. Including teachers' pensions, the ratio falls back to {{< form-val "f4_r_pens" >}}%.

**“Soon” is therefore plausible for the central government budget, not for public spending on education.** The claim was defensible, and its scope decided everything. That a comparison is badly built does not mean interest is no burden on budget room: it is one, but this comparison cannot measure it. The eleven claims examined here, made on the same day by speakers from every group, nearly all follow this pattern.

<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/dette-formules-grille-en-m.svg" width="300" height="2614">
    <img src="/img/dette-formules-grille-en.svg" alt="Table of eleven claims made on 8 September 2025, in three groups (measuring, explaining, concluding): for each, the speaker, the verdict on the question it asks, what changes if another question is asked, and the qualification of the conclusion drawn. For example: no balanced budget since 1974, accurate; higher rates than Greece, accurate on the day, {{< form-val "f8_tec8" >}}% against {{< form-val "f8_hdat8" >}}% on 8 September 2025; over €1,000bn of extra debt since 2017, accurate under every variant tested; the burden grows by €18m an hour, understated for debt ({{< form-val "f5_hausse" >}})." width="720" height="792" loading="lazy">
  </picture>
  <figcaption>One row per claim, no “true” or “false” box: the verdict on the question asked, then the neighbouring question that changes it (author's calculation; National Assembly, Insee, Eurostat, Court of Audit, Government, Senate, Banque de France, Bank of Greece).</figcaption>
</figure>

<div class="resultat-phrase">

**The result in one sentence.** Of eleven numerical cases from the debate of 8 September 2025, only one remains accurate under every variant tested (“over €1,000bn of extra debt” since 2017), only one rests on an established error of definition, and for the others the strength of the finding varies with the date, unit, scope or year chosen; none of the conclusions drawn from them is demonstrated by the figure.

</div>

Each claim takes four steps, and each needs its own evidence: a verifiable **quantity** (€67bn of interest, a 3% deficit); a chosen **framing** (period, unit, scope, definition); an **explanation** (“it is the result of…”); a **conclusion** (“we have no choice”, “we must act differently”). The figure acquires an authority that passes, without enough evidence, to the next step. The table follows this order in three stages: **measuring**, which figures often settle; **explaining**, rarely; **concluding**, never on their own.

## Measuring: the same quantity, other questions {#mesurer}

**“France has not had a balanced budget for fifty-one years”** (François Bayrou, Prime Minister). Accurate: the last surplus of general government, central government included, dates from {{< form-val "f1_an" >}}, €{{< form-val "f1_exc" >}}bn, and every year since {{< form-val "f1_an1" >}} has been in deficit (Insee, series since 1949). The claim holds on the question it asks, the overall balance. Excluding interest, the balance was positive in {{< form-val "f1_prim_l" >}} years since 1995, from {{< form-val "f1_prim" >}}: “we spend more than our resources” therefore depends on what is counted as spending.

**“A euro of deficit is a euro of extra debt”** (François Bayrou). The equality only holds if stock-flow adjustments (cash, loans, issuance premiums) are set aside, and they are a normal part of the step from deficit to debt, not an anomaly. They matter: in more than four years out of ten, the gap between the deficit and the increase in debt exceeds 20% of the deficit, {{< form-val "f2_sup" >}} years out of {{< form-val "f2_n" >}} from {{< form-val "f2_an0" >}} to {{< form-val "f2_an1" >}}. In 2020, debt rose by €{{< form-val "f2_2020" >}}bn more than the deficit, because the government built up cash during the health crisis. Over thirty years the cumulative totals come close (€{{< form-val "f2_def" >}}bn of deficits, €{{< form-val "f2_var" >}}bn of extra debt), but gaps in opposite directions that cancel out do not make an equality.

**“Reaching in 2029 the threshold of a 3% public deficit, the threshold at which debt stops rising”** (François Bayrou). The sentence says “debt” without saying which, and its two readings give two verdicts. In euros it is inaccurate: a deficit of 3% of GDP is a borrowing requirement of about €{{< form-val "f16_eur" >}}bn a year (2024 GDP, the last year known on the day of the debate, in the current edition of the accounts), which adds to the debt give or take stock-flow adjustments. As a share of GDP, the ratio stabilises when the deficit equals the debt ratio times nominal growth, divided by one plus that growth. With the 2024 ratio, the last year known on the day of the debate ({{< form-val "f16_dette24" >}}%), and no gap between deficit and debt increase, 3% is enough if nominal growth exceeds about {{< form-val "f16_seuil24" >}}%. It had done so in 2024 ({{< form-val "f16_g24" >}}%): on the day, the sentence therefore held for the ratio, under that condition. It did not in 2025, which was only known later: {{< form-val "f16_g25" >}}%, against a threshold of {{< form-val "f16_seuil" >}}% at the 2025 ratio. **The deciding variable goes unnamed: growth.** The Court of Audit, which recommends the adjustment, went further in July 2025: “getting the overall deficit back below 3% will not be enough. The imperative of debt sustainability requires stabilising and then reducing the debt ratio”.

**“France borrows at higher rates than Greece”** (Laurent Wauquiez). Accurate on the day. On 8 September 2025, France borrowed at ten years at {{< form-val "f8_tec8" >}}% according to the Banque de France, Greece at {{< form-val "f8_hdat8" >}}% according to the Bank of Greece. The two central banks do not measure quite the same thing (a constant-maturity rate, the benchmark bond). But on 4 September the Bank of Greece, using the same measure for both countries, gave {{< form-val "f8_j4_fr" >}}% against {{< form-val "f8_j4_gr" >}}%, and the gap between methods was a few hundredths at most: far less than France's lead on the 8th. Six months earlier, the claim was false:

<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/dette-formules-grece-en-m.svg" width="300" height="651">
    <img src="/img/dette-formules-grece-en.svg" alt="Monthly bars from January 2024 to {{< form-val "f8_dernier" >}} of the gap between the ten-year yields of France and Greece: Greece above until spring 2025, France above from {{< form-val "f8_premier" >}} ({{< form-val "f8_aout_fr" >}}% against {{< form-val "f8_aout_el" >}}%), then in September 2025 ({{< form-val "f8_sept_fr" >}}% against {{< form-val "f8_sept_el" >}}%), Greece above again from {{< form-val "f8_dessous" >}}." width="720" height="381" loading="lazy">
  </picture>
  <figcaption>Monthly averages (Eurostat); the dotted line marks the debate. A market price gives the current cost of borrowing, not the relative soundness of two countries.</figcaption>
</figure>

France moved above Greece in {{< form-val "f8_premier" >}}, as a monthly average. Greece moved above it again from {{< form-val "f8_dessous" >}}. In 2025, the spread of their ten-year government bond yields over Germany was almost identical: as an average of monthly spreads, {{< form-val "f8_frde_pt" >}} for France, {{< form-val "f8_elde" >}} for Greece. The same fact is true one month and false another: everything depends on the date of measurement. As for the implied conclusion, “we have reached the point where…”, an interest rate gives the price lenders ask at that moment: it does not measure the debt, the rating or the holder structure, which set the two countries apart.

**“It is not the rise in public spending, which has stayed stable since 2017, that has widened the deficit, but the fall in revenue”** (Cyrielle Chatelain, Écologiste et social). The breakdown of the balance in GDP points, on the accounts published at the date of the debate, confirms that falling revenue dominates in accounting terms, without establishing its causes: from 2017 to 2024, public spending changed by {{< form-val "f6d_dep_pt" >}} of GDP and revenue by {{< form-val "f6d_rec_pt" >}} (Insee, May 2025). Starting from 2019 changes the answer: spending rises by {{< form-val "f6d_dep19_hausse" >}}. The two starting years answer two questions, and 2017 is not an arbitrary choice for anyone judging the policy pursued since. An accounting breakdown does not, however, say which decisions lowered revenue: tax measures and the economic cycle are mixed in it. The Court of Audit explained the 2024 slippage by spending as well as by over-optimistic revenue forecasts: another year, another question. The [full breakdown, window by window](/en/why-does-public-debt-rise/#depenses-recettes), is in the first part of the dossier. A revision of the accounts is enough to move the line: over 2019–2024, the May 2025 accounts made the rise in spending dominate ({{< form-val "f6d_dep19" >}} against {{< form-val "f6d_rec19" >}}), the revised accounts the fall in revenue ({{< form-val "f6_dep19" >}} against {{< form-val "f6_rec19" >}}).

**“€66bn in 2026” against “€75bn in 2026”.** On the same day, Éric Ciotti (UDR) announced a debt charge of €66bn in 2026, and François Bayrou €75bn of “annual payments” for the same year. Both explicitly refer to 2026: their forecasts diverge. The €75bn is consistent with the rise the Court of Audit projected for general government (€{{< form-val "f3_25" >}}bn in 2025, €{{< form-val "f3_29" >}}bn in 2029), though no 2026 value allows it to be checked. The €66bn matches no forecast for 2026 found here: neither for general government nor for the central government programme that carries the debt charge (€{{< form-val "f14_ef26" >}}bn set as a ceiling in July). It does, however, equal the official figure for **2025**, from the July report. A slip of year is a possible explanation; it is not proven.

## Explaining: an accurate amount is not a cause {#expliquer}

**“We shall therefore create €50bn through work and transfer more than €100bn to our creditors, double that!”** (François Bayrou). The interest figures come from the Court of Audit and are accurate; the €50bn of extra output comes from another calculation, the speaker's own. According to the Court, general government interest would rise from €{{< form-val "f3_25" >}}bn in 2025 to €{{< form-val "f3_29" >}}bn in 2029 and €{{< form-val "f3_31" >}}bn in 2031, on the government's path. Yet three shifts produce the “double”.
- **The definition shifts.** One sentence earlier, the speaker defines debt service as “the interest and the share of principal that must be repaid”. The Court's amounts contain interest only. Principal, of a different order of magnitude, is mostly refinanced.
- **The dates cross.** Interest in 2029 is set against today's extra output (2025's was €{{< form-val "f3_surcroit25" >}}bn). The Court's path implies GDP of about €{{< form-val "f3_pib29" >}}bn in 2029. At nominal growth of 2 to 3%, extra output in 2029 would be €{{< form-val "f3_s29_bas" >}}bn to €{{< form-val "f3_s29_haut" >}}bn: interest would be {{< form-val "f3_r_bas" >}} to {{< form-val "f3_r_haut" >}} times that, not double. This is an order of magnitude, based on a growth assumption by the author of this page, not by the Court.
- **The conclusion does not follow.** “The fruit of all the work […] is handed over in full to our creditors!” Even with the years aligned, the comparison brings together three distinct things: the annual cost of interest, extra output and the public resources that pay the interest.

An independent institution supplies accurate figures, and a speaker draws from them a conclusion it does not state. What the interest charge represents, and what it pays for, is the subject of the [part on the cost of debt](/en/cost-of-french-public-debt/).

**“Debt has risen by more than €1,000bn”** (Boris Vallaud, Socialists); **“the reckless speculation of the Mozart of finance has cost us €1,000bn of extra debt”** (Mathilde Panot, La France insoumise). The amount holds under every variant tested. At the last quarter published on the day of the debate, debt had risen by €{{< form-val "f12d_elec" >}}bn since the 2017 election, by €{{< form-val "f12d_jan" >}}bn since January 2017. It is the only claim that remains accurate under every variant tested: start and end dates, vintage of the accounts. “Has cost us” nevertheless asks another question: measuring an increase is not attributing it to a policy. The period includes the health crisis and inflation, and no scenario without those policies is set out.

**“€1,200bn of extra debt since 2017, […] after it rose by €400bn under François Hollande”** (Éric Ciotti). Judged at the precision they state, to the nearest hundred billion, the €400bn holds: the increase was €{{< form-val "f12d_hol" >}}bn. The €1,200bn only just holds from January 2017 (€{{< form-val "f12d_jan" >}}bn, a few billion from the rounding limit), not from the election (€{{< form-val "f12d_elec" >}}bn), which the sentence nonetheless points to (“under the presidency of Emmanuel Macron”). The implied comparison between the two presidencies then depends on the unit: in euros, debt rose by €{{< form-val "f13_eur_mac" >}}bn a year against €{{< form-val "f13_eur_hol" >}}bn, nearly double; in GDP points, by {{< form-val "f13_pts_mac_pt" >}} a year against {{< form-val "f13_pts_hol" >}}, almost the same.

## Concluding: from the figure to the decision {#conclure}

**“Let us take full measure of the burden we shall leave to our children, which grows by €18m every hour!”** (Paul Christophe, Horizons). The figure is close to the deficit planned for 2025 (about €{{< form-val "f5_prevu" >}}m an hour), not to the increase in debt, which is the word in the sentence: €{{< form-val "f5_hausse" >}}m an hour, from the first quarter of 2024 to the first quarter of 2025. Eighteen million an hour is €5,000 a second: the same figure as François Bayrou's line of 15 July 2025, that debt grows by €5,000 every second, in another unit, with the same gap from the measured increase. The conclusion raises a question the hourly figure does not settle: what net transfers between generations result from the debt, its repayment and what it financed? Later generations inherit future taxes, but also public assets and the securities themselves. Refinancing does not remove the constraint: it changes its timing. It is also a question of distribution, between households holding the securities, foreign creditors, taxpayers and those who benefit from the spending: the [part on future generations](/en/public-debt-future-generations/) measures what the deficits corresponded to, the part on [who pays](/en/who-really-pays-public-debt/) who bears the burden.

**Two uses of the constraint.** Beyond the eleven cases, the {{< form-val "inv_n" >}} statements about debt in the debate were collected and coded twice, then disagreements were settled by a third party. Two registers appear, each almost entirely on one side of the chamber.
- **Those in government present the constraint as a technical necessity**: “impossible not to pay it; otherwise, it is bankruptcy”, “we cannot live without borrowing”. There are {{< form-val "inv_tech" >}} such statements depending on the coding, all from the government or its supporters. François Bayrou makes {{< form-val "inv_bayrou" >}} of them on his own: it is the register of one speaker, the one staking his government's survival, more than of a camp. The obligation to pay interest is real; what is open to debate is its extension to a policy presented as having no alternative.
- **The opposition plays down the constraint or disputes its use**, in {{< form-val "inv_neg" >}} statements. Most do not dispute the figures: they dispute the use of alarm (“you use the debt to frighten the French”). Contesting a policy in whose name debt is invoked is not denying the constraint.
- “If we do nothing…” is a phrase of the government and its supporters ({{< form-val "inv_cond" >}} statements); it never appears in the opposition.

These registers are not symmetrical. Recognising a constraint, judging how binding it is and using it politically are three different things, which each camp mixes in its own way. In this debate, the registers follow the position held (governing or opposing) more than a simple left-right divide; other configurations would be needed to confirm it. The [page on bringing debt down](/en/can-public-debt-come-down/) shows what other countries did with that constraint, and the [page on the rules of the game](/en/public-debt-what-futures/) what the proposals to change it would change, and who would have to decide.

## Outside the Assembly: the 2027 candidates {#hors-hemicycle}

Parties without members of the Assembly have no voice on 8 September, and candidates for the presidency do not speak there in their own name. To extend the inquiry to the currents absent from the debate, the same protocol was applied to another corpus: the commitment texts published in 2026 by the declared candidates for the 2027 presidential election (programmes, projects, booklets, measures) and, for those who had not yet published any, their latest official text (2022 presidential declaration, 2024 European election address). Of the {{< form-val "hh_declares" >}} candidates declared on 2 November 2026, {{< form-val "hh_avec" >}} have at least one text in the corpus, {{< form-val "hh_docs" >}} documents in all. For the other {{< form-val "hh_sans_l" >}}, including François Asselineau (Union populaire républicaine), no text was found. Philippe Poutou is not a candidate: his party supports Jean-Luc Mélenchon. For the Rassemblement national, no text meets the criteria: on 2 November 2026 the party's website publishes only its parliamentary group's counter-budget for 2026, which the rule excludes, and no text of the counter-budget presented by Marine Le Pen on 6 October 2026; her 2022 declaration contains no statement about debt. Its members of the Assembly, for their part, speak in the September 2025 debate.

Collection follows the rule used for the debate: {{< form-val "hh_enonces" >}} statements about debt from {{< form-val "hh_cand" >}} candidates, coded by two automated agents of the same language model, one of them without the candidate's name, then arbitrated by a third. Of these, {{< form-val "hh_test" >}} carry a checkable figure; all were tested, each at the date of its text and on the data published at that date.

**Only one statement explicitly denies the constraint.** Of the {{< form-val "hh_enonces" >}}, {{< form-val "hh_crpc" >}} accept the constraint while rejecting the policy derived from it (of the type: the debt exists, but…), {{< form-val "hh_nec" >}} present it as a necessity that closes the choice, {{< form-val "hh_ala" >}} contest the use of alarm, {{< form-val "hh_dil" >}} call for cancelling part of the debt (including {{< form-val "hh_dil_melenchon" >}} from Jean-Luc Mélenchon, about the securities held by the European Central Bank, a proposal whose effects are examined in [who would pay for it](/en/who-really-pays-public-debt/#annuler-banque-de-france)); the other {{< form-val "hh_auc" >}} take no position in any of these registers (findings, measures). These counts do not measure the candidates' acceptance of the constraint: they show how their texts use it. The register of the acknowledged constraint is the most frequent for Jean-Luc Mélenchon ({{< form-val "hh_crpc_melenchon" >}} statements), François Ruffin ({{< form-val "hh_crpc_ruffin" >}}), Marine Tondelier ({{< form-val "hh_crpc_tondelier" >}}) and Florian Philippot ({{< form-val "hh_crpc_philippot" >}}), who advocates leaving the European Union: a shared use of the argument, which says nothing of a convergence of programmes. Necessity comes first from Gabriel Attal ({{< form-val "hh_nec_attal" >}}); it also appears with Jean-François Legendre ({{< form-val "hh_nec_legendre" >}}), David Lisnard ({{< form-val "hh_nec_lisnard" >}}) and François Ruffin ({{< form-val "hh_nec_ruffin" >}}), whose texts use both registers. The two corpora differ in nature, a written campaign text against an oral debate: their counts are not comparable.

**The same measurement difficulties recur.** For the same debt, a few months apart, the texts write “3000”, “3.305”, “3417”, “3500” and “3,600” billion. The quarterly accounts gave €{{< form-val "hh_t1" >}}bn in the first quarter of 2026, €{{< form-val "hh_t2" >}}bn in the second. David Lisnard cites the mid-2025 amount. Florian Philippot cites the end-2024 amount as published in May 2025, revised since, but writes it as a threshold (“exceeds”) that the debt has indeed passed. The rise since 2017 is written “1,300” by Jean-Luc Mélenchon and “1,400” by Nicolas Dupont-Aignan: the gap lies in the starting point, the 2017 election or January 2017, and in the date of observation (€{{< form-val "hh_elec2" >}}bn and €{{< form-val "hh_jan2" >}}bn by the second quarter of 2026), as with Éric Ciotti in the debate. Written in July, on the first quarter, Bernard Cazeneuve's “one thousand four hundred billion” holds under neither reading (€{{< form-val "hh_elec1" >}}bn and €{{< form-val "hh_jan1" >}}bn).

**Largest item, second, or ahead of National Education?** Three candidates give three ranks to the debt charge in the State budget, and the document read decides. Florian Philippot speaks of 2025: in the Finance Act, the programme that carries the debt charge, €{{< form-val "hh_ef25" >}}bn, was the second, behind school education (€{{< form-val "hh_es25" >}}bn) and ahead of Defence (€{{< form-val "hh_def25" >}}bn). In the 2026 Finance Act, the order is the same (€{{< form-val "hh_ef26" >}}bn against €{{< form-val "hh_es26" >}}bn): when Nathalie Arthaud writes, in early July, that this item “has overtaken that of National Education”, it is true only when the interest of all general government (€{{< form-val "hh_int_c" >}}bn in {{< form-val "hh_an_c" >}}) is compared with a single ministry's budget, as in the government's July 2025 report with which this page opens. On {{< form-val "hh_p26_date" >}}, the ceilings proposed for 2027 put the programme first: €{{< form-val "hh_ef27" >}}bn, ahead of school education (€{{< form-val "hh_es27" >}}bn) and Defence (€{{< form-val "hh_def27" >}}bn). Bernard Cazeneuve's letter, dated the same day, writes “the largest item”: accurate for that document, not for the budget in force. These are the ranks of a budget programme, excluding pensions and tax refunds, which contains the debt charge and other spending; they are no universal ranking of interest.

**Do tax cuts explain the rise?** On the left, the rise in debt is attributed to tax cuts. Jean-Luc Mélenchon puts a figure on a counterfactual: had revenue stayed at its 2017 share of GDP ({{< form-val "hh_rec17" >}}%), “the deficit would be 2.9% of GDP” instead of {{< form-val "hh_solde_c" >}}%. The calculation is accurate with the spring 2026 accounts, which put revenue at {{< form-val "hh_rec_c" >}}% of GDP in {{< form-val "hh_an_c" >}}; the Eurostat edition of {{< form-val "hh_rec_rev_maj" >}}, which raises it to {{< form-val "hh_rec_rev_c" >}}%, gives {{< form-val "hh_sans_rev" >}}%. This is arithmetic at unchanged spending: it does not say what share of the fall in revenue comes from tax measures, what share from the economic cycle, nor whether tax cuts were offset by other levies. Cumulated from 2018 to {{< form-val "hh_an_c" >}}, the same calculation gives €{{< form-val "hh_manque" >}}bn, about {{< form-val "hh_manque_pts" >}} of GDP, before interest and effects on activity. It can neither establish nor refute the debt “at least 400 billion euros lower” that Jean-Luc Mélenchon infers, nor Marine Tondelier's attribution: “because of these tax giveaways, public debt has risen by 20 points of GDP”. The rise is accurate ({{< form-val "hh_pts_h14" >}} since the end of 2017); its attribution to tax cuts alone is not established by these data, which does not mean it is refuted.

**Scope decides again.** Nicolas Dupont-Aignan describes a debt “more than 55% held by foreign operators”: this is accurate for the State's negotiable debt ({{< form-val "hh_nr_etat" >}}% {{< form-val "hh_nr_etat_per" >}}), not for general government debt as a whole ({{< form-val "hh_nr_apu" >}}%). Bruno Retailleau writes that the pension system “is short of at least 40 billion euros every year”; the Conseil d'orientation des retraites, the official pensions advisory council, puts the system's financing need at {{< form-val "hh_cor_pct" >}} of GDP in {{< form-val "hh_cor_an" >}}, about €{{< form-val "hh_cor_md" >}}bn. Other presentations count as a need the balancing contributions the State pays, as employer, to its civil servants' scheme; the text does not say which convention gives 40 billion, and the verdict depends on it.

Outside the Assembly as inside it, several gaps lie less in the arithmetic than in conventions that are often implicit: the date, the starting point, the scope, the document. To these is added the more fundamental distance between an accurate calculation and the explanation drawn from it: the four steps of a claim, from the quantity to the conclusion, recur in the campaign texts.

<details class="repli"><summary>The candidates' statements tested</summary>

The table shows {{< form-val "hh_n_page" >}} statements: those discussed in this section, chosen because they illustrate the difficulties of date, scope, precision and attribution, and two accurate statements from candidates it does not otherwise cite. They are not a representative sample. All {{< form-val "hh_test" >}} testable statements, with their text and document, are in the downloadable data; their tests are recorded in the author's research file, and some remain undetermined there for want of a document the site holds (autumn 2026 forecasts, social security financing acts, European comparisons), neither confirmed nor refuted. Quotations are the author's translations; the French originals, with the numbers as the candidates wrote them, are in the downloadable data, and each was checked against the full text of its document.

| Candidate, date of the text | What the text says | Verdict, on the data published at that date |
|---|---|---|
| {{< form-val "hh_n_H00" >}}, {{< form-val "hh_d_H00" >}} (campaign summary) | “{{< form-val "hh_c_H00" >}}” | {{< form-val "hh_v_H00" >}} |
| {{< form-val "hh_n_H01" >}}, {{< form-val "hh_d_H01" >}} | “{{< form-val "hh_c_H01" >}}” | {{< form-val "hh_v_H01" >}} |
| {{< form-val "hh_n_H03" >}}, {{< form-val "hh_d_H03" >}} | “{{< form-val "hh_c_H03" >}}” | {{< form-val "hh_v_H03" >}} |
| {{< form-val "hh_n_H02" >}}, {{< form-val "hh_d_H02" >}} | “{{< form-val "hh_c_H02" >}}” | {{< form-val "hh_v_H02" >}} |
| {{< form-val "hh_n_H04" >}}, {{< form-val "hh_d_H04" >}} | “{{< form-val "hh_c_H04" >}}” | {{< form-val "hh_v_H04" >}} |
| {{< form-val "hh_n_H05" >}}, {{< form-val "hh_d_H05" >}} | “{{< form-val "hh_c_H05" >}}” | {{< form-val "hh_v_H05" >}} |
| {{< form-val "hh_n_H06" >}}, {{< form-val "hh_d_H06" >}} | “{{< form-val "hh_c_H06" >}}” | {{< form-val "hh_v_H06" >}} |
| {{< form-val "hh_n_H07" >}}, {{< form-val "hh_d_H07" >}} | “{{< form-val "hh_c_H07" >}}” | {{< form-val "hh_v_H07" >}} |
| {{< form-val "hh_n_H09" >}}, {{< form-val "hh_d_H09" >}} | “{{< form-val "hh_c_H09" >}}” | {{< form-val "hh_v_H09" >}} |
| {{< form-val "hh_n_H10" >}}, {{< form-val "hh_d_H10" >}} | debt service “{{< form-val "hh_c_H10" >}}” | {{< form-val "hh_v_H10" >}} |
| {{< form-val "hh_n_H08" >}}, {{< form-val "hh_d_H08" >}} | “{{< form-val "hh_c_H08" >}}” | {{< form-val "hh_v_H08" >}} |
| {{< form-val "hh_n_H11" >}}, {{< form-val "hh_d_H11" >}} | “{{< form-val "hh_c_H11" >}}” | {{< form-val "hh_v_H11" >}} |
| {{< form-val "hh_n_H17" >}}, {{< form-val "hh_d_H17" >}} | “{{< form-val "hh_c_H17" >}}” | {{< form-val "hh_v_H17" >}} |
| {{< form-val "hh_n_H18" >}}, {{< form-val "hh_d_H18" >}} | “{{< form-val "hh_c_H18" >}}” | {{< form-val "hh_v_H18" >}} |
| {{< form-val "hh_n_H12" >}}, {{< form-val "hh_d_H12" >}} | had revenue stayed at its 2017 level, “{{< form-val "hh_c_H12" >}}” | {{< form-val "hh_v_H12" >}} |
| {{< form-val "hh_n_H13" >}}, {{< form-val "hh_d_H13" >}} | “{{< form-val "hh_c_H13" >}}” | {{< form-val "hh_v_H13" >}} |
| {{< form-val "hh_n_H14" >}}, {{< form-val "hh_d_H14" >}} | “{{< form-val "hh_c_H14" >}}” | {{< form-val "hh_v_H14" >}} |
| {{< form-val "hh_n_H15" >}}, {{< form-val "hh_d_H15" >}} | the debt, “{{< form-val "hh_c_H15" >}}” | {{< form-val "hh_v_H15" >}} |
| {{< form-val "hh_n_H16" >}}, {{< form-val "hh_d_H16" >}} | “{{< form-val "hh_c_H16" >}}” (the pension system) | {{< form-val "hh_v_H16" >}} |

</details>

## One shared stock of figures {#meme-stock}

Several speakers from different camps draw on quantities from the same official statistical stock, and those figures circulate. The government's July report itself compares two scopes, and a speaker from the camp supporting the government turns it into a forecast. An opposition speaker announces for 2026 the amount that report gave for 2025, and makes a similar argument (“more than the budget of any ministry”). The Court of Audit supplies the Prime Minister with accurate amounts from which he draws a conclusion it does not write.

These overlaps establish shared figures and, for the argument about the overtaken ministry, an earlier official wording. They prove no borrowing: a resemblance is not a lineage.

## Six questions to ask of a numerical claim {#six-questions}

1. **Which date?** A market day, a month, an annual average (the Greek rates).
2. **Which unit?** Current euros or GDP points (the presidencies compared).
3. **Which scope?** The central government, general government, the nation (interest and education).
4. **Which window?** The start year, the end year, and the vintage of the accounts (spending since 2017).
5. **Which object?** A stock or a ratio, a deficit or a debt increase, interest or repayments (the 3% threshold).
6. **Which conclusion, and what more would it take to establish it?** A cause, a responsibility or a decision requires evidence the figure alone does not give.

## The book put through the same tests {#livre}

The book this page extends, *Dette publique : qui paie vraiment ?* (in French), was put through the same tests as the speakers, in its latest edition. Its central figures hold: the level of debt at end-2025, the central government's debt charge, the arithmetic of interest rates and growth. The weaknesses lie elsewhere, in the step from figure to cause. Setting the payment of interest beside closures of maternity units, as the book does, suggests a budget trade-off. Coincidence does not demonstrate the link: one would need to identify the funding decisions, the local constraints and the resources that could actually have been reallocated. The national aggregate does not settle it the other way either: since 2011, interest has gone from {{< form-val "lv_int0" >}} to {{< form-val "lv_int1" >}} points of GDP and public health spending from {{< form-val "lv_sante0" >}} to {{< form-val "lv_sante1" >}}, which rules out neither the closures nor a local trade-off. The book also attributes a stock of securities “at end-2025” to the euro-area central banks as a whole; the site's series cannot check it, since they only give the Banque de France's share. As for the discourse of fatality described in chapter 9, one debate can neither establish nor refute how frequent it is. The debate of 8 September, which was not the book's corpus, shows it in its technical form and mainly in one speaker; it does not dominate there.

<details class="repli"><summary>The thirteen claims from the book that were tested</summary>

Online edition of 17 October 2026, chapters 9 and 10 and the appendix “7 arguments”. Every claim about an observable fact that the site's series can test, wholly or partly, is included; same two verdicts and same rules as for the speakers. Numbers in the second column are the book's.

| | Claim in the book (page) | Verdict on the fact | Verdict on the reasoning |
|---|---|---|---|
| L1 | €3,460bn, 115.6% of GDP at end-2025; per-head conversions (p. 131, 135) | accurate; conversions not checked, consistent with each other | normative (“that buys…”) |
| L2 | €65bn of interest in 2025, 77 in 2026, over 100 in 2029 (p. 131, 135) | inaccurate to the unit for 2025 (series revised since); 2026 below the published forecast; 2029 consistent | no inference |
| L3 | €54bn of central government interest, 17% of its taxes (p. 134) | accurate for 54; denominator not checked | not established: the book draws a conclusion about hospitals, which fall under another scope |
| L4 | “cutting taxes by €60bn” (p. 132) | amount not checked; direction accurate | supported as an accounting contribution, not established as a cause |
| L5 | the debt equation, growth against interest rate (p. 130, 207) | accurate | **demonstrated** (identity) |
| L6 | Japan and France (p. 207) | accurate on gross debt; rates and central bank not checked | not established |
| L7 | Greece borrowed “almost at the German rate” (p. 207) | accurate | not established (“who paid”) |
| L8 | the Eurosystem held about €660bn of French debt at end-2025, declining since 2023 (p. 208) | cannot be checked on the site's series, which only give the Banque de France's share; decline accurate | no inference |
| L9 | “no saver affected”, “the State owes itself” (p. 208) | accurate on the holder | not established; normative |
| L10 | maternity units, interest, infant mortality (p. 208–209) | accurate on interest; closures and mortality not checked | causal link not established; opportunity cost out of reach without a scenario |
| L11 | IMF multiplier, emergency service (p. 207) | not checked | not established |
| L12 | decoupling of GDP and emissions (p. 208) | accurate for France; not checked for the world | normative |
| L13 | chapter 9 thesis: the subject erased, the register of fatality (p. 119–124) | not checked on the book's corpus; undetermined on the debate | not established |

No inference is contradicted by the series; only one is demonstrated. As with the speakers, the weaknesses lie mostly in the step from an accurate figure to a cause.

</details>

## What this page does not say {#limites}

**One debate is not the debate.** The corpus is the record of a single sitting, chosen so that no quotation is cherry-picked: every group spoke about debt on the same day. It does not represent television, the press or other sittings. The eleven claims are those carrying a testable figure: this is a case study, not a sample, and no proportion is drawn from it.

**The verdicts judge sentences, not policies.** An accurate claim does not validate the policy it supports, and an inaccurate one does not refute it.

**Not every current speaks in this debate, and the others are heard only through their texts.** The section “Outside the Assembly” tests the candidates' campaign texts, not their public speech (speeches, interviews, social media), which the corpus rule excludes. No text was found for {{< form-val "hh_sans_l" >}} declared candidates, including that of the Union populaire républicaine; the far left is represented by Lutte ouvrière, and the Nouveau Parti anticapitaliste-Révolutionnaires by a 2024 text with no statement about debt.

**A collection can miss a statement.** A keyword filter, checked by an unfiltered reading of a random sample, missed statements in {{< form-val "hh_tem_manq" >}} documents out of {{< form-val "hh_tem_docs" >}}, beyond the threshold set in advance ({{< form-val "hh_tem_seuil" >}}%): every text was then read in full. That reading still let through a sentence of Bernard Cazeneuve's letter that does not contain the word “debt”; the same statement, present in the summary published by his campaign, is tested.

**Automated checks verify consistency, not relevance.** The script that writes the page checks that each sentence stays consistent with the numbers; it proves neither the soundness of the categories nor that of the interpretations.

**The inventory was coded by automated agents**, for the debate as for the campaign texts. Two coders, one blind to the speaker, and an arbiter are instances of the same language model, applying the same written rule. On the campaign texts, their agreement (kappa) is {{< form-val "hh_k_ret" >}} for the choice of statements and {{< form-val "hh_k_reg" >}} for the register; {{< form-val "hh_arb" >}} disagreements were arbitrated. This agreement measures the rule's reproducibility, not the absence of a shared bias. No human coder has reviewed the sample.

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [Why is French public debt rising?](/en/why-does-public-debt-rise/)
- [What does French public debt cost?](/en/cost-of-french-public-debt/)
- [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- [And elsewhere?](/en/public-debt-international-comparison/)
- [Can French public debt fall?](/en/can-public-debt-come-down/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
Chapter 9 of the book (in French) analyses these claims through language: who speaks, by what right, closing off which options. This page tests them against the accounts. The book then examines who pays for the debt, and the choices that decide it.
{{< /appel-livre >}}

## Where these figures come from {#sources}

**The claims.** French National Assembly, full record of the sitting of 8 September 2025 (government statement followed by a vote), *Journal officiel*, debates, p. 7691 ff. Quotations are the author's translations of the official French text; the page of each quotation is given in the downloadable data. The {{< form-val "inv_n" >}} statements about debt were collected using a rule written before reading, then the whole sitting was re-read without a filter to check that none had been missed. The eleven cases come from a list of eighteen claims drawn up before the calculations: those carrying a figure testable against a published series are kept; normative claims or claims without a measurable quantity (“France cannot live on credit forever”) are set aside, and two cases combine two speakers.

**Public balance.** Insee, [general government net lending or borrowing](https://www.insee.fr/fr/statistiques/2381402) since 1949, national accounts base 2020. Deficit, spending, revenue and debt since 1995: Eurostat and Insee, datasets of the debt dossier. For the accounts known on the day of the debate: Insee, *Informations rapides* no. 163 (debt in the first quarter of 2025, 26 June 2025, corrected on 15 July) and *Insee Première* no. 2054 (general government accounts for 2024, 28 May 2025). The verdicts are judged on those accounts; the accounts revised since change no verdict, but they change whether spending or revenue dominates over 2019–2024.

**Rates.** Eurostat, [long-term government bond yields](https://ec.europa.eu/eurostat/databrowser/view/irt_lt_mcby_m/default/table?lang=en), monthly averages. Daily: Banque de France, daily bond indices (ten-year constant-maturity rate, {{< form-val "f8_tec8" >}}% on 8 September 2025); Bank of Greece, official prices and yields of benchmark bonds (HDAT platform, {{< form-val "f8_hdat8" >}}% on 8 September, read on an archived copy of its last-30-trading-days page); Bank of Greece, *Note on the Greek economy* of 5 and 19 September 2025, table 7.1 (ten-year yields of Greece and France, same source for both).

**Debt charge and education.** Court of Audit, [*La situation des finances publiques début 2025*](https://www.ccomptes.fr/fr/publications/la-situation-des-finances-publiques-debut-2025), p. 70 (projected interest) and summary of the report of 2 July 2025; Government, report on the spending ceilings of the 2026 budget bill, 15 July 2025, p. 3 and table of programmes; Senate, reports on the “Engagements financiers de l'État” and “Enseignement scolaire” programmes (2025 Finance Act appropriations). General government education spending: Eurostat, classification of the functions of government. The “Engagements financiers de l'État” programme contains the debt charge and other spending: it slightly overstates the debt charge alone.

**Campaign texts.** Campaign websites of the candidates, or of their party failing that, captured on 2 November 2026; list of candidates declared at that date, cross-checked across several media. Each document is archived with its fingerprint, and its address is given in the downloadable data. A text without a legible date is judged at its capture date. Quarterly debt: Insee; end-2024 debt as published in May 2025: *Insee Première* no. 2054; State programmes (2025 and 2026 Finance Acts, 2027 ceilings): government reports of 15 July 2025, table 1 bis, and of 15 July 2026, table 2 bis (read on a copy published by a third party); central government interest forecast for 2027: same report, table 1; revenue for the counterfactual: Eurostat, edition of {{< form-val "hh_rec_rev_maj" >}}; holders: Banque de France for the State's negotiable debt, European Central Bank for general government as a whole; pensions: Conseil d'orientation des retraites, annual report of June 2026. The cumulative revenue shortfall adds up, from 2018 to {{< form-val "hh_an_c" >}}, the gap between the revenue share of GDP in 2017 and that of each year, applied to that year's GDP.

**Judgement rules.** A round number is judged at the precision it states: €400bn to the nearest hundred, €18m to the nearest unit. “More than” is checked against the threshold, “soon” against the horizon of the paths published at the date, “stable” to within one point of GDP. “Since 2017” can be read in two ways, from January or from the event the sentence points to, and both verdicts are given. A figure or forecast published after the debate can shed light on a verdict, never ground it. These thresholds were set after the first values were read; two verdicts are sensitive to them and say so: the €1,200bn, a few billion from the rounding limit, and the stability of spending since 2017, which holds to within one point but not always to within half a point.

**Method.** Values from the accounts and rates are read by the script that writes the page. Those from published documents (Court of Audit, government report, Senate, Banque de France, Bank of Greece) are transcribed, each with its page and extract, and checked against the archived document. The script stops if a data point no longer meets the conditions on which the main sentences depend. The testing protocol was written before the calculations; the tolerance rules were set after the first values and are published as such. The work was submitted to five external reviews, which led to misleading proportions being withdrawn, several verdicts being corrected, the Greek rate for the day of the debate being found and the page being reorganised. The same rule, fixing the window and the object before comparing, reconciles in working paper [AWP-09](/en/awp/awp-09/) three scholarly estimates thought to be contradictory.

{{< reutiliser figures="figures_dette_formules" jeu="dette_formules" sources="French National Assembly, Insee, Eurostat, Court of Audit, Government, Senate, Banque de France, Bank of Greece" donnees="The verdict on each of the eleven claims, with the question asked and the neighbouring question; the public balance since 1949, the deficit and the increase in debt year by year, the windows of spending and revenue (May 2025 accounts and revised accounts), the increase in debt by starting date, monthly and daily ten-year yields, interest and education under three scopes, the counts from the inventory; for the 2027 candidates, the counts by register and the statements tested, with their documents; the same content is available as CSV, in long format." >}}
Of eleven numerical cases from the French National Assembly debate of 8 September 2025, many amounts withstand checking, but the verdict often changes with the date, unit, scope or year. Only one remains accurate under every variant tested, only one rests on an established error of definition. None of the conclusions drawn from them is demonstrated by the figure.
{{< /reutiliser >}}
