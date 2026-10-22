---
title: "Budget 2027: what do we actually know for your municipality?"
url: /en/2027-budget-your-municipality/
description: "France's draft budget bill for 2027: what the National Assembly decided on {coll.plf_vote_date} about the measures aimed at municipalities, what may still affect them, what finance departments can check now and when the amounts will be known. Dated state of the text, primary sources."
chapo: "On {coll.plf_vote_date}, the National Assembly {coll.plf_vote_resume}: three of the five measures the bill as tabled aimed at local authorities, including the two largest by amount, are set aside at this stage, though not for good. Still able to affect the municipality: the spreading of DILICO repayments, the distribution of the DGF and any measure that comes back. It can check its 2024 accounts, its FCTVA and its sums placed in reserve now; its amounts for 2027 will come from the act as passed, then from notifications."
date: 2026-10-22
lastmod: 2026-10-22
# English version of /budget-2027-votre-commune/ (series "Your municipality and central government decisions", author,
# 22/10/2026; reorganised after the author's decision 1924_Communes-01). Same tokens, values from the affichage_en block of
# data/dette_collectivites.json; state of the text from scripts/sources_collectivites/plf_votes.json (verbatim quotations
# from the official records).
og_title: "Budget 2027: what do we actually know for your municipality? — S. Lalut"
og_image: "images/og-budget-2027-commune-en.jpg"
og_image_alt: "Share card: “Budget 2027: what is left of it” — the five measures of the draft budget bill as tabled aimed at local authorities, in € billion, hollow where the National Assembly deleted or did not adopt their article."
donnees: [dette_collectivites]
dossier_source: "plf"
journal:
  - {date: 2026-10-22, texte: "Correction: the progressive contribution would have been based on the 2024 accounts (third preceding year), not 2025; the repayment of the 2025 DILICO concerns the remaining two thirds, not the initial amount. Page reorganised: the essentials first, the detail after."}
  - {date: 2026-10-22, texte: "Publication: state of the text after the National Assembly sitting of 19 October 2026."}
faq:
  - question: "What did the National Assembly decide on 19 October 2026?"
    answer: "In plenary, on {coll.plf_vote_date}, it {coll.plf_vote_resume}; it raised the national DGF for {coll.plf_edition} to €{coll.plf_dgf_an} billion. These are first-reading votes: none of these decisions is final."
  - question: "Which measures could still affect my municipality in 2027?"
    answer: "Those in the second part of the bill, which the National Assembly had not examined by {coll.plf_etat_au}: the spreading of the repayment of the sums placed in reserve in 2025 and 2026 (DILICO), the distribution of the DGF and a new grant for low-density rural municipalities. And any measure set aside that is reinstated before the final act."
  - question: "Which figures can my municipality check now?"
    answer: "Its own accounts, not amounts for 2027: the sums it placed in reserve under DILICO in 2025 and 2026, notified by order; the FCTVA it receives and the year of spending it relates to; its 2024 real operating revenue, the year that would have served as the base of the progressive contribution if it came back."
  - question: "When will my municipality know its amounts for 2027?"
    answer: "After the budget act is finally passed: the prefect then communicates the amount of each DGF grant, and new measures go through their orders or decrees. Next step on {coll.plf_etat_au}: {coll.plf_etape_suivante}."
dataset:
  jeu: "dette_collectivites"
  nom: "Draft budget bill for {coll.plf_edition}: measures aimed at local authorities and state of the text in Parliament"
  description: "Amounts for {coll.plf_edition} of the five measures of the draft budget bill as tabled aimed at local authorities (explanatory memoranda and opinion of the High Council of Public Finance, archived with their hash), state of each article in Parliament from the official records of the sittings, DGF amount adopted by the National Assembly in the first part. Part of the dataset “local authorities and public finances”."
  couverture_temporelle: "{coll.plf_edition}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Amount of each measure in the bill as tabled", unite: "€ billion", description: "progressive contribution, FCTVA, assigned VAT, contributions from ministries, DILICO"}
    - {nom: "State of the article in Parliament", unite: "dated text", description: "deleted, not adopted, adopted as amended or not yet examined, with the sitting"}
    - {nom: "DGF adopted by the National Assembly in the first part", unite: "€ billion"}
  sources:
    - "https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf"
    - "https://www.assemblee-nationale.fr/dyn/17/dossiers/PLF_2027"
    - "https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf"
  mots: ["France 2027 budget bill", "local authorities", "municipalities", "progressive contribution", "FCTVA", "DGF", "DILICO", "local government finance"]
  fichiers: ["dette_collectivites.csv", "dette_collectivites.json"]
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]
  bloc: "dette"
  rang: 35
  nature: "Bill, records of the sittings and Code, read and dated"
  prolongement: true
  refonte: "2026-10-22"
  conception: "docs/conception/budget-2027-votre-commune.md"  # fiche de conception (regle 12)
dossier_dette: prolongement
dossier_dette_titre: "Budget 2027: your municipality"
dossier_dette_role: "draft budget bill, state of the text"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<span id="questions"></span>

## The essentials for your municipality {#essentials}

*State of the draft budget bill for {{< coll-val "plf_edition" >}} on {{< coll-val "plf_etat_au" >}}: no measure is settled, and none has been set aside for good. This page is revised at each step that changes these measures; its revisions remain readable at the foot of the page.*

{{< faq-visible >}}

## What finance departments should note, check and do {#to-check}

| Measure | What to note | What can be checked now | For the 2027 budget |
|---|---|---|---|
| **Progressive contribution** (art. 37) · {{< coll-val "plf_statut_cpeb" >}} | A monthly levy on tax revenue, were the measure to come back | The 2024 accounts of the municipality and of its inter-municipal body; any exemption (urban and rural solidarity grant rankings) | Do not enter it as a certain charge; keep it as a conditional scenario |
| **FCTVA** (art. 35) · {{< coll-val "plf_statut_fctva" >}} | The proposed cut could also hit investment already carried out | The year of spending the payment relates to, and the share of ecological transition and road spending | Enter the payment at the current rate; the cut, as a conditional scenario |
| **DGF** (art. 34) · {{< coll-val "plf_statut_dgf" >}} | A larger national envelope, with no guaranteed rise for each municipality | The make-up of the municipality's DGF: lump-sum grant, equalisation grants | Do not read the national rise as guaranteed revenue for the municipality |
| **DILICO** (art. 84) · {{< coll-val "plf_statut_dilico" >}} | Repayments that would be spread to 2031, their total unchanged | The amounts placed in reserve in 2025 and 2026, notified by order | Prepare the repayment schedule, year by year, under current law and under the bill |
| **Assigned VAT** (art. 36) · {{< coll-val "plf_statut_tva" >}} | A capping set aside at this stage, with effects that differ by recipient | A share of VAT received by the municipality, or by its inter-municipal body | Enter the share under the current rules; the capping is no longer in the text at this stage |

Next deadline: {{< coll-val "plf_etape_suivante" >}}. Each row is developed [measure by measure](#measure-by-measure), with what it would be misleading to quantify at this stage.

## The bill as tabled and what is left of it {#state-of-the-text}

{{< figure-svg fichier="collectivites-plf-en" alt="Five horizontal orange bars, in € billion: the measures of the draft budget bill as tabled aimed at local authorities. The three hollow bars, the progressive contribution, the FCTVA cut and the VAT capping, are those whose article the National Assembly deleted or did not adopt in plenary; the two solid bars, contributions from ministries and the spreading of DILICO, belong to the second part, not yet examined." >}}The five measures of the draft budget bill as tabled aimed at local authorities, and what Parliament did with them. Amounts in the bill as tabled: they describe the initial framing, not the current state of the text; their arithmetic sum does not measure a net levy.{{< /figure-svg >}}

{{< fig-actions id="plf" >}}

<div class="resultat-phrase">

**The result in one sentence.** The draft budget bill for {{< coll-val "plf_edition" >}} as tabled provided for five measures aimed at local authorities, with an arithmetic sum of €{{< coll-val "plf_somme" >}} billion; on {{< coll-val "plf_vote_date" >}}, the National Assembly {{< coll-val "plf_vote_resume" >}}, without any of them being set aside for good.

</div>

That sum described the bill as tabled; it did not measure a net levy, and [the page on local authorities](/en/local-government-debt/#draft-budget-bill) explains why it coexisted with a projected rise in local resources. An article deleted or not adopted in plenary is no longer in the text under discussion, but it may come back, through a Government amendment or in the Senate. When the debate opened on 19 October, the minister for local authorities, Françoise Gatel, put the contribution of local authorities provided for by the bill at €5.5 billion.

<details class="repli"><summary>The detail of the five measures of the bill as tabled: text, nature, amount</summary>

{{< coll-tableau "plf" >}}

</details>

## Measure by measure {#measure-by-measure}

### The progressive contribution to the budgetary effort (article 37) {#cpeb}

**What the bill provided for.** A contribution of €{{< coll-val "plf_cpeb" >}} billion for {{< coll-val "plf_edition" >}}, owed according to the explanatory memorandum by {{< coll-val "plf_cpeb_communes_pct" >}}% of municipalities and by inter-municipal bodies, at a rate of 0.5% to 3% of 2024 real operating revenue, after deductions, and deducted every month from the monthly tax advances: a cash effect from notification onwards. A support fund of €50 million was planned for contributing municipalities in difficulty (article 87); the bill as tabled still refers to an “article X” there: an unfinished reference, and a fund that depends on the fate of the contribution.

**What the National Assembly decided.** State on {{< coll-val "plf_etat_au" >}}: {{< coll-val "plf_etat_cpeb" >}}. Were it to come back, each authority's amount would be set by an order published in the Journal officiel.

**What it means for a municipality.** Nothing is owed as the text stands. The municipality and its inter-municipal body were targeted by two separate contributions; what the body's contribution would put on its members would depend on their financial relations, which the text does not settle.

**What finance departments can check now.** The real operating revenue of the 2024 main budget, the year that would have served as the base, bearing in mind that the legal base deducts revenue reductions, exceptional revenue and staff made available to the inter-municipal body and invoiced; the municipality's rankings for the urban solidarity grant and the targeted share of the rural solidarity grant, which opened an exemption.

**What it would be misleading to quantify.** An amount: the rate depends on the municipality's rank among all the others. Several consultancies and associations of elected officials have simulated it on the initial text; those simulations describe an article deleted at this stage, and the associations that publish them have called for it to be deleted or reduced. Between 0.5% and 3% of the adjusted base is a static comparison, not a forecast.

**For the 2027 budget.** Do not enter the contribution as a certain charge; keep it as a conditional scenario, computed on the adjusted 2024 base, to be reactivated if the article came back.

<details class="repli"><summary>Ranking, rates, base and exemptions provided for by article 37</summary>

Municipalities are ranked on an index that weights their financial potential per inhabitant at 75% and income per inhabitant at 25%, each relative to the average. The rate runs from 0.5% for the first decile to 2% for the tenth, and 3% for the top two percentiles. It applies to the real operating revenue of the main budget recorded in the single financial account of the third preceding year, that is 2024 for a contribution due in 2027, net of revenue reductions, exceptional revenue and the proceeds of staff made available and invoiced under service-sharing with the inter-municipal body. Exempt are municipalities in the overseas departments and regions, those that article L. 2336-3 of the General Code of Local Authorities already exempts from the inter-municipal equalisation fund (the first 250 municipalities of 10,000 inhabitants or more and the first 30 of 5,000 to 9,999 in the ranking for the urban solidarity grant, the first 2,500 in the ranking for the targeted share of the rural solidarity grant), and those whose contribution would be under €5,000. Inter-municipal bodies are ranked in the same way, on their tax potential, at a rate of 0.5% to 2%.

</details>

### The VAT compensation fund (articles 35 and 41) {#fctva}

**What the bill provided for.** For payments made from 1 January {{< coll-val "plf_edition" >}}, a rate cut from 16.404% to 11.404%, that is {{< coll-val "plf_fctva_pts" >}} percentage points lower, except for spending on the ecological transition and on roads, kept at 16.404%, and a yield of €{{< coll-val "plf_fctva" >}} billion. The list of accounts qualifying for the maintained rate was left to a forthcoming order.

**What the National Assembly decided.** State on {{< coll-val "plf_etat_au" >}}: {{< coll-val "plf_etat_fctva" >}}. Were the measure to come back, the order setting the accounts at the maintained rate would say which spending benefits.

**What it means for a municipality.** The measure bore on **payments made**, not on spending committed. Under article L. 1615-6 of the Code, the payments of a municipality under the standard regime relate to spending of the year before last: in {{< coll-val "plf_edition" >}}, spending of 2025, already carried out at the former rate. For some municipalities, payments relate to the previous year's spending; for new municipalities, to the current year's.

**What finance departments can check now.** The municipality's payment regime, hence the year of spending concerned; the share of that spending recorded in ecological transition or road accounts.

**What it would be misleading to quantify.** A loss: without the list of accounts at the maintained rate, the split of spending remains unknown. For the share alone that would have fallen under the reduced rate, {{< coll-val "plf_fctva_pts" >}} points out of 16.404 amount to a little under a third of the corresponding payment: a static comparison, not a forecast of the 2027 payment.

**For the 2027 budget.** Enter the payment at the current rate, 16.404%, on the spending of the reference year; keep the cut as a conditional scenario.

### The general operating grant (articles 34 and 83) {#dgf}

**What the bill provided for.** A national amount of €{{< coll-val "plf_dgf" >}} billion; a rise in the urban and rural solidarity grants funded partly by capping the lump-sum grant (article 83, second part). The general presentation of the bill and the explanatory memorandum to article 83 do not split that rise the same way between the two grants: the Local Finance Committee will set it.

**What the National Assembly decided.** Article 34 adopted as amended: the DGF for {{< coll-val "plf_edition" >}} is raised to €{{< coll-val "plf_dgf_an" >}} billion, €{{< coll-val "plf_dgf_an_m" >}} million more than in the bill. It is an amount for {{< coll-val "plf_edition" >}}, not an indexation rule. Article 83 belongs to the second part, which the National Assembly has not yet examined.

**What it means for a municipality.** A national amount is not shared out among municipalities in simple proportion: each grant follows its own criteria, and a municipality may see its lump-sum grant capped while its solidarity grant rises.

**What finance departments can check now.** The make-up of the municipality's DGF in 2026: lump-sum grant and any capping, urban and rural solidarity grants, national equalisation grant.

**What it would be misleading to quantify.** The municipality's DGF for 2027: it depends on the act as passed and on the Local Finance Committee's distribution.

**For the 2027 budget.** Do not read the national rise as guaranteed revenue for the municipality; keep a prudent estimate until notification.

### The sums placed in reserve in 2025 and 2026 (DILICO, article 84) {#dilico}

**What the bill provided for.** Spreading to 2031 the repayment of the sums placed in reserve, without changing their total; according to the explanatory memorandum, about 2,000 authorities are concerned. The two schemes are not treated the same way: for the 2025 one, a third was already repaid in 2026 and the **remaining two thirds** would be repaid in fifths from 2027 to 2031, instead of two thirds in 2027 and 2028; for the 2026 one, the **whole amount** would be repaid in fifths from 2027 to 2031, instead of thirds from 2027 to 2029.

| For €300,000 placed in reserve (example) | DILICO 2025 | DILICO 2026 |
|---|---|---|
| Already repaid in 2026 | €100,000 | €0 |
| Annual repayment under current law | €100,000 in 2027 and 2028 | €100,000 from 2027 to 2029 |
| Annual repayment under the bill as tabled | €40,000 from 2027 to 2031 | €60,000 from 2027 to 2031 |

**What the National Assembly decided.** State on {{< coll-val "plf_etat_au" >}}: {{< coll-val "plf_etat_dilico" >}}. The bill provides for a single repayment order.

**What it means for a municipality.** For a contributing municipality, the total returned does not change; its annual payments fall and are spread to 2031, which weighs on its cash flow and, if inflation continues, on the real value of the sums returned.

**What finance departments can check now.** The amounts placed in reserve in 2025 and 2026, notified by order, and the third already received in 2026: with them, the calculation above is exact, if the text is passed as it stands.

**What it would be misleading to quantify.** Anything beyond that calculation: it holds only for the bill as tabled.

**For the 2027 budget.** Draw up the repayment schedule distinguishing the two years, one column under current law, one under the bill; use the second if article 84 is passed.

### The shares of VAT (article 36) {#vat}

**What the bill provided for.** For the shares of VAT paid in place of abolished taxes (article 16 of the 2020 budget act and article 55 of the 2023 act), annual growth reduced by the previous year's inflation excluding tobacco, without the amount being allowed to fall from one year to the next. The High Council of Public Finance put the capping at €{{< coll-val "plf_tva" >}} billion for all recipients.

**What the National Assembly decided.** State on {{< coll-val "plf_etat_au" >}}: {{< coll-val "plf_etat_tva" >}}. The amendments deleting the article had first been rejected; it is the amended article that was not adopted.

**What it means for a municipality.** Only authorities receiving such a share are concerned; if it is the inter-municipal body, the effect on the municipality would go through their financial relations.

**What finance departments can check now.** Whether the municipality itself receives a share of VAT, or its inter-municipal body does.

**What it would be misleading to quantify.** The effect: it would have depended on VAT receipts and on inflation, unknown to date.

**For the 2027 budget.** Enter the share under the current rules: the capping is no longer in the text at this stage.

### Other provisions {#other}

- **Grant for low-density rural municipalities** (article 85, second part): €50 million, reserved for municipalities classed as sparsely or very sparsely populated in the Insee grid whose density is below a reference average, excluding recipients of the rural amenities grant, and shared out by area under a forthcoming decree.
- **Post-parking charges** (article 53, first part, whose examination continues): 1.9% of charges paid after an enforcement order is issued would go to the central government budget, for orders issued from 1 January 2027.
- **Greater Paris Metropolis** (article 40): the extension of the transitional financing arrangement to 2028 was not adopted on {{< coll-val "plf_vote_date" >}}; the metropolis's municipalities are concerned through their territorial public body.

## When will the municipality know its amounts? {#timetable}

1. **In Parliament**: {{< coll-val "plf_etape_suivante" >}}; then the Senate, and final adoption.
2. **After the act**: the orders and decrees it provides for, then the information the prefect communicates to mayors, including the amount of each DGF grant (article D. 1612-1 of the Code).
3. **The initial budget** must be adopted before 15 April.

The 15 April deadline gives way in one precise case only: when information that the regulations deem essential to drawing up the budget, such as the DGF amounts, has not been communicated before 31 March; the council then has fifteen days after it is communicated (article L. 1612-2). Waiting for another amount, that of a new measure for instance, opens no extra time: the budget is voted on the information available and corrected afterwards by an amending decision.

## What its published accounts already allow {#in-your-accounts}

The Observatory of Local Public Finance and Management (OFGL) publishes, municipality by municipality on data.ofgl.fr, the 2024 and 2025 accounts: real operating revenue, FCTVA received, DGF, gross savings. These aggregates are not the legal base of the progressive contribution, which deducts several items from them; they place an order of magnitude, and gross savings show the margin available to absorb a fall in revenue. [The page on local authorities](/en/local-government-debt/#your-authority) explains how to read these lines.

## What this page does not say {#limits}

- It does not forecast the final text: a measure deleted in plenary may be reinstated.
- It gives no amount for any municipality; the orders of magnitude it mentions are static comparisons, under the conditions written next to them.
- It covers only the provisions of the bill that target municipalities directly; general tax measures may also weigh on their revenue.

## Where these figures come from {#sources}

**State of the text** — National Assembly, records of the [first](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/premiere-seance-du-lundi-19-octobre-2026) and [second](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-lundi-19-octobre-2026) sittings of 19 October 2026 (in French); each result used here is quoted word for word in the page's register of votes, archived with the hash of the records. [Legislative file](https://www.assemblee-nationale.fr/dyn/17/dossiers/PLF_2027) (in French) for the timetable.

**Texts** — [Draft budget bill for {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf), no. 3210, tabled on {{< coll-val "plf_depot" >}}, articles 34 to 41, 53 and 83 to 87 and their explanatory memoranda (in French); [opinion of the High Council of Public Finance](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf) on that bill (in French); General Code of Local Authorities, articles [L. 1612-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051731704), [D. 1612-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006395280), [L. 1615-6](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053547367) and [L. 2336-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053549170), read on Légifrance on 22 October 2026 (in French).

{{< reutiliser figures="figures_plf_communes" jeu="dette_collectivites" sources="National Assembly, High Council of Public Finance and Légifrance" donnees="The amounts of the five measures of the bill as tabled, the state of each article in Parliament and the DGF adopted by the National Assembly, in the dataset “local authorities and public finances”; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
The draft budget bill for {{< coll-val "plf_edition" >}} as tabled provided for five measures aimed at local authorities, with an arithmetic sum of €{{< coll-val "plf_somme" >}} billion, which does not measure a net levy. On {{< coll-val "plf_vote_date" >}}, the National Assembly {{< coll-val "plf_vote_resume" >}}. No municipal amount can be inferred from a bill: it will come from the act as passed, then from orders and notifications.
{{< /reutiliser >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page follows a text under discussion; the book explains why local finances become, from one budget to the next, a lever of national adjustment, and who bears the cost at the end of the chain.
{{< /appel-livre >}}
