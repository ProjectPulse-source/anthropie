---
title: "Are local authorities the adjustment variable of public finances?"
url: /en/local-government-debt/
description: "Their debt does not settle the question. From {coll.ep_a0} to {coll.ep_a1}, local government improved its balance by {coll.ep_solde_mde}: spending almost flat in euros, down {coll.ep_te_pt} of GDP, taxes up, transfers received down. Eurostat and OFGL accounts, the Cahors contracts, the draft budget bill, and a comparison with Germany, Italy and Spain."
chapo: "Local authorities' debt does not settle the question: the balanced-budget rule forbids them to borrow to offset a lasting fall in the revenue that pays for their day-to-day spending, so a constraint coming from central government shows up in their revenue and spending. From {coll.ep_a0} to {coll.ep_a1}, local government improved its balance by {coll.ep_solde_mde}. Its total spending remained almost flat in current euros, while tax revenue rose and transfers received fell. Relative to GDP, its spending fell by {coll.ep_te_pt}, of which {coll.ep_inv_pt} for investment. These movements are concomitant; on their own, they do not allow the fall in investment to be attributed to the grant cuts."
date: 2026-10-07
lastmod: 2026-10-11
# English version of the "local authorities" extension of the public debt dossier (FR: content/dette-publique-collectivites-locales/_index.md),
# 07/10/2026; editorial overhaul of 11/10/2026 (same architecture as the French page). Same tokens, same keys: values come
# from the affichage_en block of data/dette_collectivites.json (scripts/update_dette_collectivites.py), whose data guards
# and PROSE guards cover both languages; tables from coll-tableau (English branch).
og_title: "Public debt: are local authorities the adjustment variable? — S. Lalut"
og_image: "images/og-collectivites-en.jpg"
og_image_alt: "Share card: “Local adjustment, outside the debt” — local government investment and transfers received, France, in % of GDP, with the 2014-2017 grant cuts."
donnees: [dette_collectivites]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html); tokens resolved at build
  jeu: "dette_collectivites"
  nom: "Local authorities and public finances: debt, investment, transfers and accounts by category, France, Germany, Italy, Spain"
  description: "Compilation derived automatically from official sources, with no value copied by hand: accounts of local government (Eurostat, S1313) and subnational government (S1312 + S1313) from 1995 to {coll.an_fin}, decomposition of the {coll.ep_a0}-{coll.ep_a1} balance in billions of euros and in points of GDP, debt by holding sector, consolidated local government accounts by category of local authority (OFGL, 2018-{coll.of_an}), amount of the general operating grant (DGF) set by the 2013-2017 budget acts (CGCT, art. L. 1613-1), measures of the draft budget bill. Identity checked every year: revenue − expenditure = published balance."
  couverture_temporelle: "1995/{coll.an_fin}"
  couverture_spatiale: "France, Germany, Italy, Spain"
  variables:
    - {nom: "Local and subnational government debt", unite: "% of GDP", description: "S1313, and S1312 + S1313 where a state-government tier exists; 4th quarter"}
    - {nom: "Share of subnational debt held by central government", unite: "% of GDP", description: "gov_10dd_ggd, holding sector S1311, published since 2020"}
    - {nom: "Local government investment and transfers received", unite: "% of GDP", description: "P51G and D73REC, local government, France"}
    - {nom: "Decomposition of the change in the local government balance, 2013-2017", unite: "billions of current euros and points of GDP", description: "transfers received, taxes, other revenue, investment, other spending; contribution to the balance"}
    - {nom: "Gross savings, capital expenditure, debt outstanding, central government grants", unite: "billions of euros", description: "OFGL, consolidated databases of municipalities, inter-municipal groupings, departments and regions"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10q_ggdebt/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_ggd/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=en"
    - "https://data.ofgl.fr/"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033810587"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051731697"
    - "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036526027"
  mots: ["local authorities", "local government finance", "public debt", "general operating grant", "gross savings", "local investment", "Cahors contracts", "Eurostat", "OFGL"]
  fichiers: ["dette_collectivites.csv", "dette_collectivites.json"]
faq:
  - question: "How can I tell whether my local authority is affected by the draft budget bill?"
    answer: "The progressive contribution targets {coll.plf_cpeb_communes_pct}% of municipalities, {coll.plf_cpeb_dep_pct}% of departments and the inter-municipal groupings of metropolitan France, under the criteria of article 37 of the bill tabled on {coll.plf_depot}; according to that text, the amount levied on each authority will be set by a ministerial order published in the Journal officiel. The national amounts give no individual amount."
  - question: "How should the rise in local taxation be read?"
    answer: "From {coll.ep_a0} to {coll.ep_a1}, local government taxes rose by {coll.ep_imp_mde}, more than transfers received fell ({coll.ep_transf_mde}); relative to GDP, they offset only part of that fall ({coll.ep_imp_pt} against {coll.ep_transf_pt}). Since 2018, part of tax revenue has come from a reclassification: grants or abolished taxes have been replaced by shares of VAT, and this change of classification does not, on its own, say whether available resources are rising or falling. These accounts do not separate the effect of voted tax rates from that of tax bases."
  - question: "Why does a fall in investment not mean a fall in total spending?"
    answer: "From {coll.ep_a0} to {coll.ep_a1}, local government investment fell by {coll.ep_inv_mde}, but its other spending rose by {coll.ep_autres_dep_mde}: total spending remained almost flat in euros ({coll.ep_te_mde_s}). Relative to GDP, which grew by {coll.pib_croiss_pct}% over the period, it nevertheless fell by {coll.ep_te_pt}. A fall in a ratio does not prove a fall in spending in euros."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # phase B de la refonte (méthode OPTIMUM-26)
  bloc: "dette"
  rang: 30
  nature: "Official series (Eurostat, OFGL) and the author's calculations"
  prolongement: true   # "Further topics in the dossier" row, under the grid of the dossier's parts
dossier_dette: prolongement   # "Further topics" panel of the dossier bar
dossier_dette_titre: "Local authorities: the adjustment variable?"
dossier_dette_role: "debt, grants, local investment"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

**Draft budget bill for {{< coll-val "plf_edition" >}}**: what it asks of local authorities, measure by measure, and what the sum of its amounts does not say → [last section of the page](#draft-budget-bill).

**How can a constraint fail to show up in the debt?** The question in the title amounts to asking whether central government, when it tightens its finances, passes part of the effort on to local authorities, and where that would show. Three paradoxes structure this page. Local debt has stayed contained, from {{< coll-val "dette_loc_deb" >}}% of GDP in {{< coll-val "an_dette_deb" >}} to {{< coll-val "dette_loc_fin" >}}% in {{< coll-val "an_dette_fin" >}}: on its own, this observation does not say whether local authorities bore a constraint. From {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}, their spending was almost flat in euros and fell markedly as a share of GDP: two correct readings that do not tell the same story. In Spain, central government holds more than half of subnational debt: carrying a debt and financing it are two distinct realities.

{{< figure-svg fichier="collectivites-investissement-en" alt="Two lines in percent of GDP since 1995: local government investment, fairly stable, dips sharply after 2014; the transfers it receives fall from 2013 to 2017, where their comparable series stops, after a one-off peak in 2010." >}}Investment by local government (gross fixed capital formation) and current transfers it receives from other general government units, in % of GDP. These transfers include those from social security: they are not just central government grants. The 2010 peak is a one-off: that year the State compensated for the abolition of the business tax (*taxe professionnelle*), a reform “neutral for the balance of local government” according to Insee (May 2011, our translation). The comparable transfer series stops in 2017: in 2018 and again in 2021, some grants were replaced by shares of VAT, counted as taxes, a reclassification that does not, on its own, say whether resources rose or fell ([details](/en/local-government-debt/#reclassifications)).{{< /figure-svg >}}

{{< fig-actions id="investissement" >}}

<div class="resultat-phrase">

**The finding in one sentence.** From {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}, the transfers received by local government fell by {{< coll-val "ep_transf_mde" >}} ({{< coll-val "ep_transf_pt" >}} of GDP) and its investment by {{< coll-val "ep_inv_mde" >}} ({{< coll-val "ep_inv_pt" >}}); after the 2014 municipal elections, the fall in investment was {{< coll-val "creux_ratio" >}} times as large as the largest of the falls that followed those of 2001, 2008 and 2020.

</div>

These figures, like all the statistical results on this page, concern **local government in the national-accounts sense**: local authorities, but also inter-municipal syndicates and other local public bodies.

<details class="repli"><summary>Exact scope, and the bridge between local government accounts and national accounts</summary>

This scope is subsector S1313 of the national accounts; it includes other local government bodies, among them Île-de-France Mobilités and the Société des grands projets (Insee). Its debt (€{{< coll-val "dette_loc_md" >}} billion in {{< coll-val "an_dette_fin" >}}) exceeds by about €{{< coll-val "of_ecart_maastricht" >}} billion the sum of the debt outstanding of municipalities, inter-municipal groupings, departments and regions.

This page draws on two sources that do not speak the same language. Eurostat publishes the national accounts, harmonised across Europe; the Observatory of local public finance and management (*Observatoire des finances et de la gestion publique locales*, OFGL) publishes aggregates from the local government accounting records (*comptes de gestion*), the ones finance departments read. The quantities correspond without being identical.

| What a finance department reads (OFGL) | What Eurostat publishes | What separates them |
|---|---|---|
| General operating grant (DGF), central government financial support | Current transfers received from other general government units (D73) | Eurostat includes transfers from social security; a grant replaced by a share of VAT moves into taxes. |
| Capital expenditure | Gross fixed capital formation (P51G) | Investment grants paid out are capital transfers, outside P51G. |
| Net lending or borrowing | Net lending (+) or net borrowing (−) (B9) | Same concept; recording dates and scopes differ. |
| Gross savings | Gross saving (B8G) | Similar concepts, different adjustments. |
| Debt outstanding | Debt under the Maastricht definition | Nominal value; for local government, consolidated within the subsector, not between subsectors. |

The sum of the debt outstanding of the four categories tracked by the OFGL (€{{< coll-val "of_encours_total" >}} billion in {{< coll-val "of_an" >}}) falls short of local government debt under the Maastricht definition: the latter also includes syndicates and other local government bodies, and follows other conventions. Nor is it consolidated with the State: the share the State holds ({{< coll-val "fr_detenu_etat" >}} points of GDP) remains counted in it, which distinguishes it from the “contribution” of local government to consolidated public debt published by Insee. The gap can be documented; it cannot be corrected.

</details>

## Two narratives, one series {#two-narratives}

The Association of French Mayors (*Association des maires de France*), responding to the Court of Audit (*Cour des comptes*) in June 2025: “Treating local authorities as the adjustment variable for the executive's strategic errors only deepens the public deficit” (our translation). The Court of Audit (September 2025), “without ruling on the appropriateness of its amount”, calls for “organising, over time, local authorities' participation in the recovery of public finances” (our translation).

The same series lends support to each reading. Local government spending rose from {{< coll-val "te_0" >}}% of GDP in {{< coll-val "te_a0" >}} to {{< coll-val "te_pic" >}}% in {{< coll-val "te_apic" >}}: that is the argument for local authorities sharing in the effort. It had come back down to {{< coll-val "ep_te_pc_a1" >}}% in {{< coll-val "ep_a1" >}}, at the end of the grant cuts, and stands at {{< coll-val "te_fin" >}}% in {{< coll-val "an_fin" >}}: that is the argument of authorities already called upon to contribute. Neither reading suffices on its own; the useful question is when, through which channel and in which unit a constraint can be seen.

## Why the debt is not enough to answer {#low-debt}

The observation holds. Local government debt went from {{< coll-val "dette_loc_deb" >}}% of GDP in {{< coll-val "an_dette_deb" >}} to {{< coll-val "dette_loc_fin" >}}% in {{< coll-val "an_dette_fin" >}}, while public debt went from {{< coll-val "dette_apu_deb" >}}% to {{< coll-val "dette_apu_fin" >}}%, and it amounts to less than a tenth of public debt ({{< coll-val "part_loc_fin" >}}% in {{< coll-val "an_dette_fin" >}}). Yet local government carries out {{< coll-val "part_inv_loc_fin" >}}% of public investment ({{< coll-val "inv_loc_fin" >}}% of GDP in {{< coll-val "an_fin" >}}). The figure of {{< coll-val "dette_apu_fin" >}}% comes from Eurostat's quarterly series (updated on {{< coll-val "dette_maj" >}}); the notification of {{< coll-val "notif_maj" >}}, which the other pages of the dossier cite, gave {{< coll-val "dette_apu_notif_fin" >}}%.

The reason lies in a rule. The General Code of Local Authorities (CGCT) requires a genuinely balanced budget: operating and investment sections each voted in balance, and loan principal repaid out of own resources, **excluding the proceeds of borrowing** (article L. 1612-4). Borrowing remains open to finance investment: the rule does not freeze the stock of debt, which in fact rose in 2020 and since 2023. What it does prevent is shifting a lasting fall in operating resources onto borrowing; such a fall then goes through own revenue, current spending, gross savings or investment. Nor does the rule govern the whole subsector, which includes bodies other than local authorities.

**Contained debt is consistent with an adjustment through resources and spending, and with the absence of one: it does not measure how intense a constraint has been.** No single indicator replaces it here. The accounts make it possible to observe mechanisms and episodes; they do not make it possible to turn them into a general rule since {{< coll-val "an_dette_deb" >}}, nor to attribute those episodes to a cause.

## {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}: the grant cuts, in euros and in points of GDP {#grant-cuts}

Over these four years, the State cut its general operating grant (*dotation globale de fonctionnement*, DGF) under the heading of the “contribution to the recovery of public finances”. Three quantities describe the episode, and none replaces the others:

| Quantity | What it measures | From {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}} |
|---|---|---|
| DGF set by the budget act (article L. 1613-1 of the CGCT) | the amount of the grant set each year | from €{{< coll-val "dgf_vote_13" >}} billion to €{{< coll-val "dgf_vote_17" >}} billion |
| Transfers received (Eurostat, D73) | current transfers from central government and social security, all grants included | down {{< coll-val "ep_transf_mde" >}}, or {{< coll-val "ep_transf_pt" >}} of GDP |
| Investment (Eurostat, P51G) | local government gross fixed capital formation | down {{< coll-val "ep_inv_mde" >}}, or {{< coll-val "ep_inv_pt" >}} of GDP |

In {{< coll-val "ep_a1" >}}, the annual level of the voted DGF was €{{< coll-val "dgf_vote_baisse" >}} billion lower than in {{< coll-val "ep_a0" >}}. **This is not the total of the savings accumulated over the four years**, which would add up each year's shortfall relative to {{< coll-val "ep_a0" >}}.

{{< figure-svg fichier="collectivites-cascade-en" alt="Two waterfalls side by side, from 2013 to 2017, same items and same order. In billions of current euros, the rise in taxes exceeds the fall in transfers, and lower investment is offset by higher other spending. In points of GDP, all spending falls and taxes offset only part of the fall in transfers. Both waterfalls end at the same slight surplus." >}}Change in the local government balance between {{< coll-val "ep_a0" >}} and {{< coll-val "ep_a1" >}}, broken down into five items, in billions of current euros (left) and in points of GDP (right). Each value is the item's contribution to the change in the balance: for spending, the opposite of its change, so that lower spending improves the balance. Nominal GDP grew by {{< coll-val "pib_croiss_pct" >}}% over the period: this denominator is what separates the two readings.{{< /figure-svg >}}

{{< fig-actions id="cascade" >}}

**Both readings are correct, and they do not tell the same story.** In current euros, revenue rose by {{< coll-val "ep_tr_mde" >}}, taxes alone by €{{< coll-val "ep_imp_md" >}} billion, while transfers received fell by €{{< coll-val "ep_transf_md" >}} billion; total spending went from €{{< coll-val "ep_te0_md" >}} billion to €{{< coll-val "ep_te1_md" >}} billion. The balance thus improved by {{< coll-val "ep_solde_mde" >}} ({{< coll-val "ep_solde_pt" >}} of GDP), on the revenue side. In points of GDP, spending fell by {{< coll-val "ep_te_pt" >}}, of which {{< coll-val "ep_inv_pt" >}} for investment, and taxes offset only part of the fall in transfers ({{< coll-val "ep_imp_pt" >}} against {{< coll-val "ep_transf_pt" >}}).

The difference lies in the denominator. Nominal GDP grew by {{< coll-val "pib_croiss_pct" >}}% between {{< coll-val "ep_a0" >}} and {{< coll-val "ep_a1" >}}: spending held almost flat in euros falls as a share of GDP. **A fall in a ratio does not prove a fall in spending in euros.** Investment, for its part, also fell in euros, by {{< coll-val "ep_inv_pct_eur" >}}%, while other spending rose by {{< coll-val "ep_autres_dep_mde" >}}. No reading in volume, which would require a price index specific to local spending, is made here.

These movements are concomitant; on their own, they do not allow the fall in investment to be attributed to the grant cuts.

**The comparison does not allow the size of the trough to be put down to the municipal cycle alone.** Local investment usually falls after municipal elections. But after the 2001, 2008 and 2020 elections, the fall never exceeded {{< coll-val "creux_autres_max" >}} points of GDP; after those of 2014, it reached {{< coll-val "creux14_baisse" >}} points in {{< coll-val "creux14_annee" >}}, {{< coll-val "creux_ratio" >}} times as much, while central government grants were falling. The comparison weakens the explanation by the electoral calendar alone; it does not isolate the effect of the grants, all the more so since departments and regions, included in the aggregate, do not follow this cycle.

<details class="repli"><summary>The electoral-cycle check, term by term, the three measures of the DGF and the accounting check on the waterfall</summary>

{{< coll-tableau "cycles" >}}

Insee attributes the 2014 fall to its coming “in the wake of the municipal elections”, then that of 2015 “notably” to the municipal electoral cycle, noting that year the effect of “the cut in State transfers” (our translations).

The four episodes are not identical: 2008 came just before the financial crisis, 2020 was the year of the pandemic. Isolating the effect of the grants would require comparing, authority by authority, those most and least exposed to the cuts, before and after 2014.

The voted DGF fell every year, by €{{< coll-val "dgf_vote_b14" >}} billion in 2014, then by €{{< coll-val "dgf_vote_b15" >}} billion, €{{< coll-val "dgf_vote_b16" >}} billion and €{{< coll-val "dgf_vote_b17" >}} billion in the following three years. The amount of the DGF set by the budget act is neither the contribution demanded of each category nor the DGF each authority actually recorded in its accounts: these three measures do not add up. The local government accounts show the third measure by category: the departments' DGF fell from €{{< coll-val "of_dgf_dep_13" >}} billion to €{{< coll-val "of_dgf_dep_17" >}} billion, that of the regions from €{{< coll-val "of_dgf_reg_13" >}} billion to €{{< coll-val "of_dgf_reg_17" >}} billion.

The waterfall is checked by an identity the generator verifies on every run: total revenue minus total spending equals the balance published by Eurostat. Over the {{< coll-val "temoin_annees" >}} years available, the largest gap is €{{< coll-val "temoin_residu" >}} million, a rounding difference. Each of the two waterfalls adds up to the change in the balance. The denominator's share is computed exactly, on the GDP of the same accounts: with spending unchanged, GDP growth would have lowered the ratio of spending to GDP by {{< coll-val "ep_te_effet_pib_pt" >}}; the rise in spending in euros took back {{< coll-val "ep_te_effet_eur_pt" >}}, hence the fall of {{< coll-val "ep_te_pt" >}}.

</details>

<span id="three-channels"></span>

## The mechanism changes, the question remains {#mechanisms}

A constraint from central government can reach local authorities through channels that are not of the same kind: some reduce resources, others cap spending, others again change the make-up of revenue. Since 2014, they have followed one another.

1. **{{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}: acting on resources.** The voted DGF fell every year; investment fell over the same period.
2. **{{< coll-val "cahors_ex1" >}}-{{< coll-val "cahors_ex2" >}}: regulating spending.** The Cahors contracts set certain local authorities a target for the growth of their operating expenditure, based on a national benchmark of {{< coll-val "cahors_taux" >}}% a year. The financial clawback provided for in case of overshooting was suspended for {{< coll-val "cahors_suspendu" >}} expenditure. A new channel of constraint emerges, without implying that the earlier ones disappeared; this page cannot measure its specific effect.
3. **2018 and 2021: changing the make-up of revenue.** A grant (2018), then abolished taxes (2021), gave way to shares of VAT or to a levy on State revenue. Some resources are replaced by revenue of a different kind: their accounting classification changes, but this reclassification does not, on its own, allow us to conclude that the resources available have risen or fallen. The series then stop being comparable (details below).
4. **{{< coll-val "plf_edition" >}}: several channels at once.** A levy on resources, a grant tied to investment, the timetable of repayments: the draft budget bill combines them ([last section](#draft-budget-bill)).

<details class="repli"><summary>The Cahors contracts in the text: authorities covered, base, financial clawback</summary>

The public finance programming act of {{< coll-val "cahors_date_lpfp" >}} set local authorities a national target for the growth of their real operating expenditure of {{< coll-val "cahors_taux" >}}% a year, in value, computed on a {{< coll-val "cahors_base" >}} base (article 13). Contracts, known as the “Cahors contracts”, applied it for the years {{< coll-val "cahors_ex1" >}}, {{< coll-val "cahors_ex2" >}} and {{< coll-val "cahors_ex3" >}}; they covered the regions, the departments and the authorities with special status, as well as the municipalities and inter-municipal groupings whose real operating expenditure exceeded €{{< coll-val "cahors_seuil_m" >}} million in 2016 (article 29). For a signatory authority, overshooting triggered a financial clawback of {{< coll-val "cahors_reprise_pct" >}}% of the gap, capped at {{< coll-val "cahors_plafond_pct" >}}% of real operating revenue (article 29, V); a different rate applied to authorities that did not sign (article 29, VI).

The emergency act of {{< coll-val "cahors_date_urgence" >}} set this clawback aside for {{< coll-val "cahors_suspendu" >}} expenditure (article 12): it could therefore only apply to {{< coll-val "cahors_ex1" >}} and {{< coll-val "cahors_ex2" >}} expenditure. The effect of the contracts cannot be measured in these series: they bore only on the main budget of the authorities concerned, which the national aggregate does not separate out.

</details>

Two other channels escape these series: responsibilities transferred without full funding, whose fixed compensation falls behind the actual cost and is read responsibility by responsibility (the departments' individual solidarity allowances, for example), and unfunded standards, whose cost is read in impact assessments. All these channels share a hypothesis to test: a decision taken at one level can shift part of its cost onto another. Working paper [AWP-09](/en/awp/awp-09/) confronts it with the {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}} episode: the accounts make it compatible, without establishing it.

### 2018 and 2021: when a resource changes classification {#reclassifications}

In 2018, the regions' DGF went from €{{< coll-val "of_dgf_reg_17" >}} billion to €{{< coll-val "of_dgf_reg_18" >}} billion while they received €{{< coll-val "of_tva_reg_18" >}} billion of VAT (OFGL): a revenue item classified among transfers became a tax revenue. In 2021, transfers received by local government as a whole dropped by {{< coll-val "rupt_transf" >}} points of GDP and its taxes rose by {{< coll-val "rupt_imp" >}} points: the abolition of the residence tax on main homes (*taxe d'habitation*) and that of the regional share of the business value-added tax (CVAE) were offset by shares of VAT or, for municipalities, by the departmental share of property tax. A series limited to grants alone therefore does not, on its own, measure how resources have changed.

<details class="repli"><summary>The 2021 offsets, text by text</summary>

The abolition of the residence tax on main homes was offset by a share of VAT for inter-municipal groupings and departments, municipalities receiving the departmental share of property tax (budget act for 2020, article 16); the abolition of the regional share of the CVAE, by a share of VAT for the regions (budget act for 2021, article 8); the reduction in the rental values of industrial premises, by a levy on State revenue (same act, article 29).

</details>

## By category of authority: what the aggregate hides {#by-category}

The national aggregate adds up authorities whose revenue and costs have nothing in common. Since 2018, the Observatory of local public finance and management (OFGL) has published the consolidated accounts of each category, the ones finance departments read. Two movements appear there that are invisible in the aggregate. Departments' gross savings, that is their operating revenue minus their operating spending, fell from €{{< coll-val "of_eb_dep_pic" >}} billion in {{< coll-val "of_eb_dep_apic" >}} to €{{< coll-val "of_eb_dep_min" >}} billion in {{< coll-val "of_eb_dep_amin" >}}, before rising back to €{{< coll-val "of_eb_dep_fin" >}} billion in {{< coll-val "of_an" >}}; the causes (property transfer duties, solidarity allowances) lie in series this page does not carry. Municipalities' capital expenditure went from €{{< coll-val "of_eq_com_20" >}} billion in 2020 to €{{< coll-val "of_eq_com_fin" >}} billion in {{< coll-val "of_an" >}} (+{{< coll-val "of_eq_com_hausse_pct" >}}%), in the run-up to the 2026 municipal elections.

<details class="repli"><summary>The four categories of local authority, 2021 to {{< coll-val "of_an" >}}: central government grants, gross savings, capital expenditure, debt</summary>

{{< coll-tableau "categories" >}}

The boundaries of the categories change with reforms: the departments' consolidated database used here includes the Lyon metropolis (since 2015) and the City of Paris (since 2019), and that of the regions the single authorities of French Guiana, Martinique and Corsica — the OFGL annual report, for its part, classifies Lyon with inter-municipal groupings and Paris with municipalities. National accounts and local government accounts do not match to the million: scopes, recording dates and adjustments differ.

</details>

## Since 2023: local government debt is rising again {#since-2023}

Since {{< coll-val "recent_a0" >}}, local government net borrowing has been well above its {{< coll-val "avant_a0" >}} and {{< coll-val "avant_a1" >}} level (less than a tenth of a point of GDP): {{< coll-val "recent_solde_deb_pt" >}} in {{< coll-val "recent_a0" >}}, {{< coll-val "recent_solde_mid_pt" >}} in {{< coll-val "recent_a1" >}} and {{< coll-val "recent_solde_fin_pt" >}} in {{< coll-val "an_fin" >}}. Its investment has risen from {{< coll-val "recent_inv_deb1" >}}% to {{< coll-val "inv_loc_fin" >}}% of GDP, and its debt from {{< coll-val "recent_dette_deb" >}}% to {{< coll-val "dette_loc_fin" >}}% of GDP: the reverse of the {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}} pattern. In the accounts of the four categories of local authority, debt outstanding is rising too: €{{< coll-val "of_encours_rec0" >}} billion in {{< coll-val "of_encours_rec0_annee" >}}, €{{< coll-val "of_encours_total" >}} billion in {{< coll-val "of_an" >}}. **The rest of the increase cannot be attributed by subtraction to syndicates and other bodies**: the two sources do not consolidate in the same way and do not follow the same conventions.

<details class="repli"><summary>The tax revenue smoothing mechanism (DILICO), in 2025 and 2026</summary>

The cyclical smoothing mechanism for tax revenue (*dispositif de lissage conjoncturel des recettes fiscales*, DILICO) took {{< coll-val "dilico_2025" >}} from local authorities' tax resources in 2025, placed in reserve and paid back in thirds over the following three years — 90% to the contributing authorities, 10% to equalisation funds (budget act for 2025, article 186); it was renewed in 2026 (budget act for 2026). Neither Insee nor Eurostat documents how it is recorded in the national accounts: its own effect cannot be isolated in these series.

</details>

## Elsewhere in Europe: the same debt, opposite architectures {#elsewhere-in-europe}

Comparisons here are made by statistical scope, not by responsibilities exercised. France and Italy, where regions are classified in local government, form the main comparison; Germany and Spain, whose subnational debt adds that of the Länder or autonomous communities to that of local authorities, serve as counterpoints.

{{< figure-svg fichier="collectivites-europe-en" alt="Four small charts in percent of GDP: French subnational debt rises gently, Germany's stays high, carried by the Länder, Italy's rises then falls back, Spain's more than doubles. Under each chart, the share held by central government: almost nil in France and Germany, small in Italy, more than half in Spain." >}}Subnational government debt (state and local government, S1312 + S1313) in % of GDP, fourth quarter of each year, and the share held by central government, published since 2020 (shown under each country).{{< /figure-svg >}}

{{< fig-actions id="europe" >}}

**In Spain**, subnational debt went from {{< coll-val "es_dette_deb" >}}% of GDP in {{< coll-val "an_dette_deb" >}} to {{< coll-val "es_dette_fin" >}}% in {{< coll-val "an_dette_fin" >}}, driven by the autonomous communities, while subnational investment fell by {{< coll-val "es_inv_baisse_pct" >}}%. But this debt does not measure a constraint passed downwards: in {{< coll-val "an_ggd" >}}, {{< coll-val "es_detenu_etat" >}} points of GDP out of {{< coll-val "es_detenu_total" >}}, or {{< coll-val "es_part_etat_pct" >}}%, were held by the central State itself, notably through the Fondo de Liquidez Autonómico, created in 2012, through which the State lends to the autonomous communities (Real Decreto-ley 21/2012, articles 9 and 14). The equivalent share is {{< coll-val "it_part_etat_pct" >}}% in Italy, {{< coll-val "fr_part_etat_pct" >}}% in France and {{< coll-val "de_part_etat_pct" >}}% in Germany. **Who carries a debt and who finances it are two distinct questions.**

**In Italy**, the three indicators point the same way: subnational debt fell back from {{< coll-val "it_dette_pic" >}}% of GDP in {{< coll-val "it_dette_pic_annee" >}} to {{< coll-val "it_dette_fin" >}}% in {{< coll-val "an_dette_fin" >}}, the balance was in surplus in {{< coll-val "it_excedents" >}} years out of eight between 2012 and 2019 (France: {{< coll-val "fr_excedents" >}}), and investment fell to half its peak of the 2000s. These concomitant movements do not separate the effect of national rules — the internal stability pact, introduced in 1999 and abandoned for local authorities in 2016 — from that of the sovereign debt crisis.

**In Germany**, subnational debt remains well below its {{< coll-val "de_dette_pic_annee" >}} peak ({{< coll-val "de_dette_pic" >}}%, {{< coll-val "de_dette_fin" >}}% in {{< coll-val "an_dette_fin" >}}), with a limited fall in investment ({{< coll-val "de_inv_baisse_pct" >}}%); it is carried mainly by the Länder.

The comparison yields no single ranking: debt, balance and investment order the four countries differently. It shows that a public finance constraint can travel between levels of government in opposite forms — a cut in grants, a fall in investment, debt, or the financing of the subnational tier by the centre.

<details class="repli"><summary>The four countries, indicator by indicator</summary>

{{< coll-tableau "pays" >}}

The state government subsector (S1312) exists in the Eurostat data only in a few countries, including Germany and Spain; French and Italian regions are classified in local government (S1313). In Germany and Spain, subnational debt therefore adds the two tiers together; cross-holdings between them amount to at most {{< coll-val "consolidation_ecart_pt" >}} of GDP: the double counting is marginal and does not change the orders of magnitude. In Spain, Organic Law 2/2012 also assigns the surpluses of each level of government to reducing its net debt (article 32).

</details>

## What does the draft budget bill ask of local authorities? {#draft-budget-bill}

*State of the text: draft budget bill for {{< coll-val "plf_edition" >}} (*projet de loi de finances*), tabled on {{< coll-val "plf_depot" >}}, before examination by Parliament; its amounts may change before the act is passed.*

{{< coll-tableau "plf" >}}

The bill does not cut the DGF: it provides for €{{< coll-val "plf_dgf_hausse_m" >}} million of new increases and, taking scope changes into account, its nominal amount rises by €{{< coll-val "plf_dgf_hausse_courant_m" >}} million, to €{{< coll-val "plf_dgf" >}} billion. The contribution required from local authorities goes through the five channels in the table and, for the regions, through the removal of a share of excise duties on energy worth €{{< coll-val "plf_regions_m" >}} million (article 39). The High Council of Public Finance (*Haut Conseil des finances publiques*) groups these measures in a single package moderating local authority revenue.

**How could local authorities' resources rise by €{{< coll-val "plf_ressources_md" >}} billion when the arithmetic sum of the bill's measures comes to €{{< coll-val "plf_somme" >}} billion?**

{{< coll-tableau "plf_lectures" >}}

**Why do these figures coexist?** The arithmetic sum of €{{< coll-val "plf_somme" >}} billion brings together five measures, each assessed against the situation without it, on different baselines; the Government's €{{< coll-val "plf_ressources_md" >}} billion compares two years, measures included. Their difference, {{< coll-val "plf_ecart_mde" >}}, is therefore not a net levy, and adding up the five measures is not enough to establish their net effect: a resource can rise in euros while growing more slowly than it would have without the reform. Nor are the five measures of the same kind, and two of them bear on related flows: their exact reconciliation is not made here.

<details class="repli"><summary>Nature of the five measures, base of the progressive contribution and levies on State revenue</summary>

Spreading out the repayment of the sums placed in reserve (DILICO) shifts a timetable without changing the total amount returned (article 84); the cut in the rate of the VAT compensation fund depends on the investment local authorities will carry out. The text describes no double counting between these amounts, but two of them bear on related flows: the progressive contribution is charged to the monthly tax advances and to the shares of VAT, whose growth is also being capped (articles 36 and 37).

The progressive contribution applies to {{< coll-val "plf_cpeb_communes_pct" >}}% of municipalities, to {{< coll-val "plf_cpeb_dep_pct" >}}% of departments and to the inter-municipal groupings of metropolitan France, at a rate that rises with their resources, applied to real operating revenue of the year before last; overseas authorities and the most socially fragile departments are exempt (article 37). In the State budget, the levies on State revenue in favour of local authorities (*prélèvements sur recettes*) are estimated at €{{< coll-val "plf_psr" >}} billion for {{< coll-val "plf_edition" >}}, against €{{< coll-val "plf_psr_rev_prec" >}} billion in the revised forecast for {{< coll-val "plf_prec" >}} (€{{< coll-val "plf_psr_lfi_prec" >}} billion in the initial budget act, article 41): a series limited to grants would not see these channels, for the reason already encountered [in 2018 and 2021](#reclassifications).

</details>

The High Council forecasts a fall in local authorities' investment of {{< coll-val "plf_inv_n1_pct" >}}% in {{< coll-val "plf_edition" >}}, after {{< coll-val "plf_inv_n_pct" >}}% in {{< coll-val "plf_prec" >}}, and considers it plausible given the position of {{< coll-val "plf_edition" >}} in the municipal electoral cycle, one year after the elections, and given the reform of the compensation fund. This page measures what a fall in investment amounted to [from {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}](#grant-cuts); it does not say whether it will happen again. Texts: [draft budget bill for {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf) (in French), articles 34 to 41 and 84; [opinion of the High Council of Public Finance](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf) (in French).

## What the accounts allow us to say {#what-the-accounts-say}

Three perspectives must be kept apart. **What is decided**: grants, transferred taxes, spending rules and financing arrangements, set by budget and programming acts. **What is observed**: revenue, spending, investment, savings, balance and debt, in the national accounts and the local government accounts. **What is ultimately borne**: the effects on taxpayers, users, services and facilities, which these data do not measure.

This page documents decisions and concomitant accounting movements; it does not demonstrate the transmission from the former to the latter and does not measure what is ultimately borne.

<details class="repli"><summary>The analytical scheme: a four-link chain</summary>

Between what is decided and what is borne, a four-link chain describes the possible mechanisms. It is an analytical scheme, not a causality demonstrated at each link:

1. **national decision**: grant cut, revenue capped, spending rule;
2. **local constraint**: fewer resources, or less freedom to choose;
3. **local budgetary response**: taxation, operating spending, savings, investment, borrowing;
4. **final incidence**: services, facilities, taxpayers, users, places.

Decisions belong to the first link, accounting movements to the third; the fourth is not measured here.

</details>

<details class="repli" id="who-bears"><summary>Research hypothesis, not tested here: who ultimately bears the adjustment?</summary>

The accounts do not reveal whether the adjustment is ultimately borne by taxpayers, users, public employees, suppliers, landowners or the households that depend on local services. [Anthropy](/en/quest-ce-que-lanthropie/), the analytical framework put forward by the author, suggests that some costs are harder to avoid for the least mobile households: a household that depends on social housing, public transport and local facilities bears a fare increase or a closure more directly than a household that can move to another municipality. This page does not test it; it would be verified decision by decision, and would be weakened by adjustments falling mainly on well-off households or offset by social tariffs.

</details>

## What these data do not say {#limits}

- The national aggregate mixes municipalities, inter-municipal groupings, departments, regions, syndicates and other bodies; data by category go back only to 2018, and the boundaries of the categories change with reforms ([details](#by-category)).
- A fall in investment concurrent with a cut in grants does not establish that the latter caused the former; the effect of the Cahors contracts is not measured here.
- Amounts are in current euros and in points of GDP; no reading in volume is made.
- These data say nothing about the quality of the services provided, nor about who ultimately bore the adjustment.

## How can these results be read in your own authority's accounts? {#your-authority}

National results give no amount for any given authority. They show what to compare in its own accounts: its *compte de gestion* or single financial account (*compte financier unique*), or the aggregates the OFGL publishes authority by authority on data.ofgl.fr, the ones this page uses.

1. **Resources received from the State** (DGF and other grants): how they change in euros, bearing in mind that a grant replaced by a share of VAT moves into tax revenue, as in 2018 and 2021.
2. **Tax revenue**: separating the taxes whose rate the authority votes from the shares of national taxes it receives.
3. **Gross savings**: operating revenue minus operating spending; together with other own resources, it must cover repayment of debt principal.
4. **Investment spending**: in euros and relative to revenue, taking the municipal cycle into account.

For {{< coll-val "plf_edition" >}}, liability to the progressive contribution can be checked in article 37 of the bill (criteria, rates, exemptions), then, once the act is passed, in the ministerial order published in the Journal officiel which, according to the bill, will set the amount levied on each authority. The effect of the cut in the compensation fund's rate shows up in the authority's own eligible spending; the spreading of the sums placed in reserve concerns only the authorities that contributed to them in 2025 or 2026.

## Frequently asked questions {#questions}

{{< faq-visible >}}

**In the public debt dossier**

{{< pastilles label="In the public debt dossier" >}}
- [Why does French public debt rise?](/en/why-does-public-debt-rise/)
- [What does French public debt actually cost?](/en/cost-of-french-public-debt/)
- [Who really pays for public debt?](/en/who-really-pays-public-debt/)
- [Public debt: why 100% of GDP does not carry the same burden everywhere](/en/public-debt-international-comparison/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="To take the analysis further" avis="non" >}}
This page shows the route the adjustment of local finances takes; it does not say who, at the end of the chain, bears its cost. The book follows this shift channel by channel — taxpayer, user, public services, generations not yet old enough to vote — with official figures. The analysis is also developed in two articles by the author, [“La commune, variable d'ajustement de la République ?”](https://www.revue-projet.com/articles/2026-07-lalut-variable-d-ajustement-de-la-republique/11589) [The municipality, adjustment variable of the Republic?] (*Revue Projet*, 2026, in French) and [“Budget 2026 : la dette commande, les territoires patientent”](https://blogs.mediapart.fr/stephane-lalut/blog/150126/budget-2026-la-dette-commande-les-territoires-patientent) [Budget 2026: debt gives the orders, local areas wait] (*Mediapart*, 2026, in French).
{{< /appel-livre >}}

## Where these figures come from {#sources}

**National accounts** — Eurostat, general government by subsector, ESA 2010: annual accounts (`gov_10a_main`: gross fixed capital formation P51G, current transfers received D73REC, taxes D2, D5 and D91, revenue TR, expenditure TE, balance B9), quarterly debt (`gov_10q_ggdebt`), debt by holding sector (`gov_10dd_ggd`), nominal GDP and debt from the notification (`gov_10dd_edpt1`), GDP from the national accounts as a check on the denominator (`nama_10_gdp`). The points of GDP in the waterfall are computed on the GDP of the same annual accounts; the GDP growth quoted is that of the notification.

**Management accounts** — OFGL, consolidated databases of municipalities, inter-municipal groupings, departments and regions (data.ofgl.fr, DGFiP data).

**Texts** — General Code of Local Authorities, articles L. 1612-4 and L. 1613-1; Law no. 2018-32 of {{< coll-val "cahors_date_lpfp" >}} on public finance programming for 2018 to 2022, articles 13 and 29; Law no. 2020-290 of {{< coll-val "cahors_date_urgence" >}} on the emergency response to the covid-19 epidemic, article 12; budget acts for 2020 (art. 16), 2021 (art. 8 and 29), 2025 (art. 186) and 2026; draft budget bill tabled on {{< coll-val "plf_depot" >}} and opinion of the High Council of Public Finance on that bill; all read in full and archived with their hash; Real Decreto-ley 21/2012 and Organic Law 2/2012 (Spain); Law no. 448/1998, art. 28, and Law no. 208/2015 (Italy, internal stability pact, then balanced-budget rule); Insee, *Les comptes des administrations publiques* [General government accounts] for 2010, 2014 and 2015 (in French); Court of Audit, *Les finances publiques locales 2025* [Local public finances 2025] and published responses (in French).

The calculations, checks and figures are produced by a single script, rerun each time the sources publish; no figure on this page is entered by hand, and the script refuses to write if a piece of data stops supporting a sentence, or if a sentence draws from the figures a conclusion they do not carry. **Download the data** (CC BY 4.0 licence): [CSV](/dette_collectivites.csv), in long format, readable in a spreadsheet; [JSON](/dette_collectivites.json), with the calculations, definitions and the report of the checks (variable names and labels in French).

{{< reutiliser figures="figures_collectivites" jeu="dette_collectivites" sources="Eurostat, OFGL and Légifrance" donnees="The series by country and by category of authority, the DGF set by the budget act, the 2013-2017 decomposition in billions of euros and in points of GDP, the measures of the draft budget bill and the report of the checks; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
Local authorities' debt, restricted by the balanced-budget rule, is not enough to say whether a constraint from central government weighed on them: the constraint shows up in their revenue and spending. From {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}, local government improved its balance by {{< coll-val "ep_solde_mde" >}}, with spending almost flat in current euros, tax revenue up and transfers received down; relative to GDP, its spending fell by {{< coll-val "ep_te_pt" >}}, of which {{< coll-val "ep_inv_pt" >}} for investment. These movements are concomitant and are not enough to attribute the fall in investment to the grant cuts; elsewhere, the constraint takes other forms, as in Spain, where central government holds more than half of subnational debt.
{{< /reutiliser >}}
