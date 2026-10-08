---
title: "Are local authorities the adjustment variable of public finances?"
url: /en/local-government-debt/
description: "Since {coll.an_dette_deb}, local authority debt has gone from {coll.dette_loc_deb}% to {coll.dette_loc_fin}% of GDP while public debt nearly doubled. But from {coll.ep_a0} to {coll.ep_a1}, the cut in central government grants coincided with a fall in their investment. Eurostat and OFGL accounts, by category of authority, compared with Germany, Italy and Spain."
chapo: "The accounts do not support making it a general rule: since {coll.an_dette_deb}, French public debt has gone from {coll.dette_apu_deb}% to {coll.dette_apu_fin}% of GDP, that of local authorities from {coll.dette_loc_deb}% to {coll.dette_loc_fin}% only. But from {coll.ep_a0} to {coll.ep_a1}, the cut in central government grants coincided with an improvement in the local balance that came mainly through lower spending, notably on capital investment. The accounts show where the adjustment appears; on their own, they do not establish what caused it."
date: 2026-10-07
lastmod: 2026-10-07
# English version of the "local authorities" extension of the public debt dossier (FR: content/dette-publique-collectivites-locales/_index.md),
# 07/10/2026. Same tokens, same keys: values come from the affichage_en block of data/dette_collectivites.json
# (scripts/update_dette_collectivites.py), whose guards cover both languages; tables from coll-tableau (English branch).
og_title: "Public debt: are local authorities the adjustment variable? — S. Lalut"
og_image: "images/og-collectivites-en.jpg"
og_image_alt: "Share card: “Local adjustment, outside the debt” — local government investment and transfers received, France, in % of GDP, with the 2014-2017 grant cuts."
donnees: [dette_collectivites]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html); tokens resolved at build
  jeu: "dette_collectivites"
  nom: "Local authorities and public finances: debt, investment, transfers and accounts by category, France, Germany, Italy, Spain"
  description: "Compilation derived automatically from official sources, with no value copied by hand: accounts of local government (Eurostat, S1313) and subnational government (S1312 + S1313) from 1995 to {coll.an_fin}, debt by holding sector, consolidated local government accounts by category of local authority (OFGL, 2018-{coll.of_an}), amount of the general operating grant (DGF) set by the 2013-2017 budget acts (CGCT, art. L. 1613-1). Identity checked every year: revenue − expenditure = published balance."
  couverture_temporelle: "1995/{coll.an_fin}"
  couverture_spatiale: "France, Germany, Italy, Spain"
  variables:
    - {nom: "Local and subnational government debt", unite: "% of GDP", description: "S1313, and S1312 + S1313 where a state-government tier exists; 4th quarter"}
    - {nom: "Share of subnational debt held by central government", unite: "% of GDP", description: "gov_10dd_ggd, holding sector S1311, published since 2020"}
    - {nom: "Local government investment and transfers received", unite: "% of GDP", description: "P51G and D73REC, local government, France"}
    - {nom: "Gross savings, capital expenditure, debt outstanding, central government grants", unite: "billions of euros", description: "OFGL, consolidated databases of municipalities, inter-municipal groupings, departments and regions"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10q_ggdebt/default/table?lang=en"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_ggd/default/table?lang=en"
    - "https://data.ofgl.fr/"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033810587"
  mots: ["local authorities", "local government finance", "public debt", "general operating grant", "gross savings", "local investment", "Eurostat", "OFGL"]
  fichiers: ["dette_collectivites.csv", "dette_collectivites.json"]
faq:
  - question: "Are local authorities the adjustment variable of the State budget?"
    answer: "The accounts do not support making it a general rule: since {coll.an_dette_deb}, their debt has gone from {coll.dette_loc_deb}% to {coll.dette_loc_fin}% of GDP while public debt went from {coll.dette_apu_deb}% to {coll.dette_apu_fin}% (Eurostat). But from {coll.ep_a0} to {coll.ep_a1}, when the State cut the general operating grant from €{coll.dgf_vote_13} billion to €{coll.dgf_vote_17} billion, their balance improved mainly through lower spending, notably on investment. The accounts show which route the adjustment took; on their own, they do not say what caused it."
  - question: "Are local authorities heavily indebted?"
    answer: "Their debt outstanding represents about {coll.part_loc_fin}% of public debt in {coll.an_dette_fin} ({coll.dette_loc_fin}% of GDP), against {coll.part_loc_deb}% in {coll.an_dette_deb}, and yet they carry out {coll.part_inv_loc_fin}% of public investment. The law forbids them to borrow to finance their operating costs (article L. 1612-4 of the General Code of Local Authorities): they borrow only to invest."
  - question: "Did the cut in grants reduce local investment?"
    answer: "The two coincided: from {coll.ep_a0} to {coll.ep_a1}, transfers received by local authorities fell by {coll.ep_transf} points of GDP and their investment by {coll.ep_inv} points (€{coll.ep_inv_md} billion). Investment always falls after municipal elections, but after those of 2014 the fall was {coll.creux_ratio} times larger than the largest fall after the 2001, 2008 and 2020 elections. This comparison weakens the explanation by the electoral calendar alone; it does not isolate the effect of the grants."
  - question: "What does the draft budget bill ask of local authorities?"
    answer: "The draft budget bill for {coll.plf_edition}, tabled on {coll.plf_depot}, does not cut the general operating grant: its nominal amount rises by €{coll.plf_dgf_hausse_courant_m} million. The contribution required from local authorities takes the form, notably, of a progressive contribution levied on tax advances (€{coll.plf_cpeb} billion), a cut in the rate of the VAT compensation fund (€{coll.plf_fctva} billion), a capping of the growth of assigned VAT excluding regions (€{coll.plf_tva} billion), a reduction in contributions from certain ministries (€{coll.plf_ministeres} billion) and the spreading over five years of the repayment of sums placed in reserve in 2025 and 2026 (€{coll.plf_dilico} billion). These amounts stem from different mechanisms and do not add up; they are those of a bill, before examination by Parliament."
  - question: "Why did departments' gross savings fall so sharply?"
    answer: "The consolidated accounts published by the OFGL show departments' gross savings going from €{coll.of_eb_dep_pic} billion in {coll.of_eb_dep_apic} to €{coll.of_eb_dep_min} billion in {coll.of_eb_dep_amin}, before rising back to €{coll.of_eb_dep_fin} billion in {coll.of_an}. The national aggregate for local authorities, almost stable, does not show it. The causes (revenue from property transfer duties, solidarity allowances) lie in series this page does not carry."
  - question: "Are local authorities in other European countries more indebted?"
    answer: "On a comparable statistical scope, subnational debt reaches {coll.es_dette_fin}% of GDP in Spain and {coll.de_dette_fin}% in Germany, which have a tier of state governments, against {coll.fr_dette_fin}% in France and {coll.it_dette_fin}% in Italy. But in Spain, {coll.es_part_etat_pct}% of that debt is held by central government itself: carrying a debt and financing it are two different things."
ressource:  # index /ressources/ (layouts/ressources/list.html)
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

To the question **“are local authorities the adjustment variable of public finances?”**, the accounts give two answers, and both are needed. **Over the long run, the accounts do not show it:** since {{< coll-val "an_dette_deb" >}}, French public debt has gone from {{< coll-val "dette_apu_deb" >}}% to {{< coll-val "dette_apu_fin" >}}% of GDP, that of local authorities from {{< coll-val "dette_loc_deb" >}}% to {{< coll-val "dette_loc_fin" >}}% only. **Episode by episode, the adjustment appears somewhere other than in the debt:** from {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}, the cut in central government grants coincided with a sharp fall in local investment.

{{< figure-svg fichier="collectivites-investissement-en" alt="Two lines in percent of GDP since 1995: local authorities' investment, fairly stable, dips sharply after 2014; the transfers they receive fall from 2013 to 2017, after a one-off peak in 2010." >}}Investment by local government and current transfers it receives from other general government units, in % of GDP. The 2010 peak is a one-off: that year the State compensated for the abolition of the business tax (*taxe professionnelle*), a reform “neutral for the balance of local government” according to Insee (May 2011, our translation). The comparable transfer series stops in 2017.{{< /figure-svg >}}

{{< fig-actions id="investissement" >}}

<div class="resultat-phrase">

**The finding in one sentence.** Between {{< coll-val "ep_a0" >}} and {{< coll-val "ep_a1" >}}, the improvement of {{< coll-val "ep_solde_delta" >}} points of GDP in local authorities' balance shows up mainly on the spending side: spending fell by {{< coll-val "ep_te" >}} points, of which {{< coll-val "ep_inv" >}} points of investment, while transfers received fell by {{< coll-val "ep_transf" >}} points and local debt changed little.

</div>

<details class="repli"><summary>Reading these figures against your own accounts: the bridge between local government accounts and national accounts</summary>

This page draws on two sources that do not speak the same language. Eurostat publishes the national accounts, harmonised across Europe; the Observatory of local public finance and management (*Observatoire des finances et de la gestion publique locales*, OFGL) publishes aggregates from the local government accounting records (*comptes de gestion*), the ones finance departments read. The quantities correspond without being identical.

| What a finance department reads (OFGL) | What Eurostat publishes | What separates them |
|---|---|---|
| General operating grant (DGF), central government financial support | Current transfers received from other general government units (D73) | Eurostat includes transfers from social security; a grant replaced by a share of VAT moves into taxes. |
| Capital expenditure | Gross fixed capital formation (P51G) | Investment grants paid out are capital transfers, outside P51G. |
| Net lending or borrowing | Net lending (+) or net borrowing (−) (B9) | Same concept; recording dates and scopes differ. |
| Gross savings | Gross saving (B8G) | Similar concepts, different adjustments. |
| Debt outstanding | Debt under the Maastricht definition | Nominal value; for local government, consolidated within the subsector, not between subsectors. |

Nor do the two sources cover the same field. The sum of the debt outstanding of the four categories tracked by the OFGL (€{{< coll-val "of_encours_total" >}} billion in {{< coll-val "of_an" >}}) falls short by about €{{< coll-val "of_ecart_maastricht" >}} billion of local government debt under the Maastricht definition (€{{< coll-val "dette_loc_md" >}} billion, Eurostat): the latter also includes inter-municipal syndicates and other local government bodies, among them Île-de-France Mobilités and the Société des grands projets (Insee), and follows other conventions. Nor is it consolidated with the State: the share the State holds ({{< coll-val "fr_detenu_etat" >}} points of GDP) remains counted in it, which distinguishes it from the “contribution” of local government to consolidated public debt published by Insee. The gap can be documented; it cannot be corrected.

</details>

## Low debt, high investment {#low-debt}

Local government debt outstanding amounts to less than a tenth of public debt: {{< coll-val "part_loc_fin" >}}% in {{< coll-val "an_dette_fin" >}}, against {{< coll-val "part_loc_deb" >}}% in {{< coll-val "an_dette_deb" >}}. Of the {{< coll-val "delta_apu" >}} points of GDP of public debt accumulated since {{< coll-val "an_dette_deb" >}}, local authorities added {{< coll-val "delta_loc" >}}, or {{< coll-val "part_hausse_loc" >}}% of the increase. Yet they carry out {{< coll-val "part_inv_loc_fin" >}}% of public investment ({{< coll-val "inv_loc_fin" >}}% of GDP in {{< coll-val "an_fin" >}}).

This asymmetry is explained in part by local budget rules, alongside the division of responsibilities and revenue. The law requires a genuinely balanced budget, operating section included, and excludes borrowing from the resources used to repay loan principal (article L. 1612-4 of the General Code of Local Authorities, CGCT). **A lasting fall in current resources therefore cannot simply be shifted onto borrowing: it ends up weighing on own revenue, current spending, gross savings or investment.**

## Two narratives, one series {#two-narratives}

The Association of French Mayors (*Association des maires de France*), responding to the Court of Audit (*Cour des comptes*) in June 2025: “Treating local authorities as the adjustment variable for the executive's strategic errors only deepens the public deficit” (our translation). The Court of Audit (September 2025), “without ruling on the appropriateness of its amount”, calls for “organising, over time, local authorities' participation in the recovery of public finances” (our translation).

The same series lends support to each reading. Local government spending rose from {{< coll-val "te_0" >}}% of GDP in {{< coll-val "te_a0" >}} to {{< coll-val "te_pic" >}}% in {{< coll-val "te_apic" >}}: that is the argument for local authorities sharing in the effort. It came back down to {{< coll-val "te_fin" >}}% in {{< coll-val "an_fin" >}}, after the {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}} episode: that is the argument of authorities already called upon to contribute. Neither reading suffices on its own; the useful question is when, and through which item, the adjustment took place.

## {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}: the grant cuts in the accounts {#grant-cuts}

Over these four years, the State cut its general operating grant (*dotation globale de fonctionnement*, DGF) under the heading of the “contribution to the recovery of public finances”. The amount of the DGF set each year by the budget act fell from €{{< coll-val "dgf_vote_13" >}} billion in 2013 to €{{< coll-val "dgf_vote_17" >}} billion in 2017 (article L. 1613-1 of the CGCT): −{{< coll-val "dgf_vote_b14" >}} in 2014, −{{< coll-val "dgf_vote_b15" >}} in 2015, −{{< coll-val "dgf_vote_b16" >}} in 2016, −{{< coll-val "dgf_vote_b17" >}} in 2017, a total of €{{< coll-val "dgf_vote_baisse" >}} billion less over four years. This voted amount is neither the contribution demanded of each category nor the DGF each authority actually recorded in its accounts: three related measures, which do not add up. The local government accounts show the third by category: the departments' DGF fell from €{{< coll-val "of_dgf_dep_13" >}} billion to €{{< coll-val "of_dgf_dep_17" >}} billion (−{{< coll-val "of_dgf_dep_baisse" >}}), that of the regions from €{{< coll-val "of_dgf_reg_13" >}} billion to €{{< coll-val "of_dgf_reg_17" >}} billion (−{{< coll-val "of_dgf_reg_baisse" >}}). National accounts, for their part, measure all transfers received from other general government units, State and social security included: −{{< coll-val "ep_transf" >}} points of GDP, or €{{< coll-val "ep_transf_md" >}} billion less in {{< coll-val "ep_a1" >}} than in {{< coll-val "ep_a0" >}}.

{{< figure-svg fichier="collectivites-cascade-en" alt="Waterfall in points of GDP, from 2013 to 2017: starting from a slight deficit, the fall in transfers worsens the balance; higher taxes and lower spending, mainly on investment, bring it back up to a slight surplus." >}}Change in local government revenue and spending between {{< coll-val "ep_a0" >}} and {{< coll-val "ep_a1" >}}, in points of GDP. The five items add up exactly to the change in the balance.{{< /figure-svg >}}

{{< fig-actions id="cascade" >}}

Taxes offset part of the fall in transfers (+{{< coll-val "ep_imp" >}} points) and other revenue fell further ({{< coll-val "ep_autres_rec" >}} points). The balance nevertheless improved by {{< coll-val "ep_solde_delta" >}} points: spending fell by {{< coll-val "ep_te" >}} points, of which {{< coll-val "ep_inv" >}} for investment — €{{< coll-val "ep_inv_md" >}} billion less capital spending in {{< coll-val "ep_a1" >}} than in {{< coll-val "ep_a0" >}} — and {{< coll-val "ep_autres_dep" >}} for the rest. This is the last period in which the transfer series remains comparable, before the changes of 2018 and 2021.

**The comparison does not allow the size of the trough to be put down to the municipal cycle alone.** Local investment usually falls after municipal elections, and Insee attributes the 2014 fall to its coming “in the wake of the municipal elections”, then that of 2015 “notably” to the municipal electoral cycle, noting that year the effect of “the cut in State transfers” (our translations). But after the 2001, 2008 and 2020 elections, the fall never exceeded {{< coll-val "creux_autres_max" >}} points of GDP; after those of 2014, it reached {{< coll-val "creux14_baisse" >}} points in {{< coll-val "creux14_annee" >}}, {{< coll-val "creux_ratio" >}} times as much, while central government grants were falling. The comparison weakens the explanation by the electoral calendar alone; it does not isolate the effect of the grants, all the more so since departments and regions, included in the aggregate, do not follow this cycle.

<details class="repli"><summary>The electoral-cycle check, term by term, and the accounting check on the waterfall</summary>

{{< coll-tableau "cycles" >}}

The four episodes are not identical: 2008 came just before the financial crisis, 2020 was the year of the pandemic. Isolating the effect of the grants would require comparing, authority by authority, those most and least exposed to the cuts, before and after 2014.

The waterfall is checked by an identity the generator verifies on every run: total revenue minus total spending equals the balance published by Eurostat. Over the {{< coll-val "temoin_annees" >}} years available, the largest gap is €{{< coll-val "temoin_residu" >}} million, a rounding difference.

</details>

## By category of authority: what the aggregate hides {#by-category}

The national aggregate adds up authorities whose revenue and costs have nothing in common. Since 2018, the consolidated local government accounts published by the OFGL make it possible to separate them. Two movements appear there that are invisible in the aggregate: departments' gross savings fell from €{{< coll-val "of_eb_dep_pic" >}} billion in {{< coll-val "of_eb_dep_apic" >}} to €{{< coll-val "of_eb_dep_min" >}} billion in {{< coll-val "of_eb_dep_amin" >}}, before rising back to €{{< coll-val "of_eb_dep_fin" >}} billion in {{< coll-val "of_an" >}}; municipalities' capital expenditure went from €{{< coll-val "of_eq_com_20" >}} billion in 2020 to €{{< coll-val "of_eq_com_fin" >}} billion in {{< coll-val "of_an" >}} (+{{< coll-val "of_eq_com_hausse_pct" >}}%), in the run-up to the 2026 municipal elections.

{{< coll-tableau "categories" >}}

## 2018 and 2021: when a resource changes box {#reclassifications}

In 2018, the regions' DGF went from €{{< coll-val "of_dgf_reg_17" >}} billion to €{{< coll-val "of_dgf_reg_18" >}} billion while they received €{{< coll-val "of_tva_reg_18" >}} billion of VAT (OFGL). In 2021, transfers received by all local authorities dropped by {{< coll-val "rupt_transf" >}} points of GDP and their taxes rose by {{< coll-val "rupt_imp" >}} points: the abolition of the residence tax on main homes (*taxe d'habitation*) was offset by a share of VAT for inter-municipal groupings and departments, municipalities receiving the departmental share of property tax (budget act for 2020, article 16); the abolition of the regional share of the business value-added tax (CVAE), by a share of VAT for the regions (budget act for 2021, article 8); the reduction in the rental values of industrial premises, by a levy on State revenue (same act, article 29). In 2018, a revenue item classified among transfers became a tax revenue. In 2021, several taxes abolished or reduced were offset either by other tax revenue, notably VAT, or by a levy on State revenue. A series limited to grants alone therefore does not, on its own, measure how resources have changed.

## Since 2023: local debt is rising again {#since-2023}

Since {{< coll-val "recent_a0" >}}, local authorities have again been net borrowers ({{< coll-val "recent_solde_fin" >}} points of GDP in {{< coll-val "an_fin" >}}), their investment has risen from {{< coll-val "recent_inv_deb" >}}% to {{< coll-val "inv_loc_fin" >}}% of GDP, and the stock of their debt from {{< coll-val "recent_dette_deb" >}}% to {{< coll-val "dette_loc_fin" >}}% of GDP: the reverse of the {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}} pattern. These series cover Eurostat's local government sector: besides the local authorities, it includes other local government bodies, among them the departmental fire and rescue services, Île-de-France Mobilités and the major-project companies (*sociétés de grands projets*, Insee); a note limited to the local authorities alone therefore finds a different net borrowing. The cyclical smoothing mechanism for tax revenue (*dispositif de lissage conjoncturel des recettes fiscales*, DILICO) took {{< coll-val "dilico_2025" >}} from local authorities' tax resources in 2025, placed in reserve and paid back in thirds over the following three years — 90% to the contributing authorities, 10% to equalisation funds (budget act for 2025, article 186); it was renewed in 2026 (budget act for 2026). Neither Insee nor Eurostat documents how it is recorded in the national accounts: its own effect cannot be isolated in these series.

## What does the draft budget bill ask of local authorities? {#draft-budget-bill}

The draft budget bill for {{< coll-val "plf_edition" >}} (*projet de loi de finances*), tabled on {{< coll-val "plf_depot" >}}, provides for €{{< coll-val "plf_dgf_hausse_m" >}} million of new increases in the general operating grant; taking scope changes into account, its nominal amount rises by €{{< coll-val "plf_dgf_hausse_courant_m" >}} million, to €{{< coll-val "plf_dgf" >}} billion. The contribution required from local authorities therefore does not take the form of a cut in the DGF: it takes the form, notably, through five channels quantified below, which concern tax advances, the VAT compensation fund, the growth of assigned VAT and certain central government grants.

{{< coll-tableau "plf" >}}

The High Council of Public Finance (*Haut Conseil des finances publiques*) groups these measures in a single package moderating local authority revenue. Their amounts are not added up here: they correspond to different mechanisms and bases of comparison. For the regions, there is in addition the removal of a share of excise duties on energy worth €{{< coll-val "plf_regions_m" >}} million (article 39). In the State budget, the levies on State revenue in favour of local authorities (*prélèvements sur recettes*) are estimated at €{{< coll-val "plf_psr" >}} billion for {{< coll-val "plf_edition" >}}, against €{{< coll-val "plf_psr_rev_prec" >}} billion in the revised forecast for {{< coll-val "plf_prec" >}} (€{{< coll-val "plf_psr_lfi_prec" >}} billion in the initial budget act, article 41). A series limited to grants would not see these channels, for the reason already encountered [in 2018 and 2021](#reclassifications).

The progressive contribution applies to {{< coll-val "plf_cpeb_communes_pct" >}}% of municipalities, to {{< coll-val "plf_cpeb_dep_pct" >}}% of departments and to the inter-municipal groupings of metropolitan France, at a rate that rises with their resources; overseas authorities and the most socially fragile departments are exempt (article 37). These national amounts do not make it possible to estimate the effect on a given authority: for the progressive contribution, liability and rate depend on the authority's size band and on the indicators set out in article 37; for the compensation fund, the effect depends on the composition of eligible spending; the VAT adjustment does not concern the regions.

The budget documents describe two distinct dimensions of the scenario. The Government states that, after the measures calling on them to contribute, local authorities would have €{{< coll-val "plf_ressources_md" >}} billion more in resources in {{< coll-val "plf_edition" >}} than in {{< coll-val "plf_prec" >}} (+{{< coll-val "plf_ressources_pct" >}}%). The High Council, for its part, forecasts a fall in their investment of {{< coll-val "plf_inv_n1_pct" >}}%, after {{< coll-val "plf_inv_n_pct" >}}% in {{< coll-val "plf_prec" >}}, and considers this fall plausible given the position of {{< coll-val "plf_edition" >}} in the municipal electoral cycle, one year after the elections, and given the reform of the compensation fund. These two figures concern different quantities. This page measures what a fall in investment amounted to [from {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}](#grant-cuts); it does not say whether it will happen again, and these amounts are those of a bill, which Parliament may amend. Texts: [draft budget bill for {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf) (in French), articles 34 to 41 and 84; [opinion of the High Council of Public Finance](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf) (in French).

## Elsewhere in Europe: the same debt, opposite architectures {#elsewhere-in-europe}

Comparisons here are made by statistical scope, not by responsibilities exercised. The state government subsector (S1312) exists in the Eurostat data only in a few countries, including Germany and Spain; French and Italian regions are classified in local government (S1313), and these two countries form the main comparison. Germany and Spain, with their Länder and autonomous communities, serve as counterpoints. Their subnational debt adds the two tiers together; cross-holdings between the two tiers amount to at most {{< coll-val "consolidation_ecart" >}} points of GDP: the double counting is marginal and does not change the orders of magnitude.

{{< figure-svg fichier="collectivites-europe-en" alt="Four small charts in percent of GDP: French subnational debt rises gently, Germany's stays high, carried by the Länder, Italy's rises then falls back, Spain's more than doubles; in Spain, more than half of it is held by central government." >}}Subnational government debt (state and local government, S1312 + S1313) in % of GDP, fourth quarter of each year, and the share held by central government, published since 2020.{{< /figure-svg >}}

{{< fig-actions id="europe" >}}

**In Italy**, the three indicators point the same way over the period: subnational debt fell back from {{< coll-val "it_dette_pic" >}}% of GDP in {{< coll-val "it_dette_pic_annee" >}} to {{< coll-val "it_dette_fin" >}}%, the balance was in surplus in {{< coll-val "it_excedents" >}} years out of eight between 2012 and 2019 (France: {{< coll-val "fr_excedents" >}}), and investment fell to half its peak of the 2000s. These concomitant movements do not separate the effect of national rules — the internal stability pact, introduced in 1999 and abandoned for local authorities in 2016 — from that of a crisis far deeper than in France.

**In Spain**, subnational debt went from {{< coll-val "es_dette_deb" >}}% to {{< coll-val "es_dette_fin" >}}% of GDP, driven by the autonomous communities, while subnational investment fell by {{< coll-val "es_inv_baisse_pct" >}}%. But this debt does not measure a constraint passed downwards: in {{< coll-val "an_ggd" >}}, {{< coll-val "es_detenu_etat" >}} points of GDP out of {{< coll-val "es_detenu_total" >}}, or {{< coll-val "es_part_etat_pct" >}}%, are held by the central State itself, notably through the Fondo de Liquidez Autonómico, created in 2012, through which the State lends to the autonomous communities (Real Decreto-ley 21/2012, articles 9 and 14). The equivalent share is {{< coll-val "it_part_etat_pct" >}}% in Italy, {{< coll-val "fr_part_etat_pct" >}}% in France and {{< coll-val "de_part_etat_pct" >}}% in Germany. Spain's Organic Law 2/2012 also assigns the surpluses of each level of government to reducing its net debt (article 32). **Who carries a debt and who finances it are two distinct questions.**

**In Germany**, subnational debt remains well below its {{< coll-val "de_dette_pic_annee" >}} peak ({{< coll-val "de_dette_pic" >}}%, {{< coll-val "de_dette_fin" >}}% in {{< coll-val "an_dette_fin" >}}), with a limited fall in investment ({{< coll-val "de_inv_baisse_pct" >}}%); it is carried mainly by the Länder.

<details class="repli"><summary>The four countries, indicator by indicator</summary>

{{< coll-tableau "pays" >}}

</details>

The comparison yields no single ranking: debt, balance and investment order the four countries differently. It shows that a public finance constraint can travel between levels of government in opposite forms — a cut in grants, a fall in investment, debt, or the financing of the subnational tier by the centre.

## Three channels, one hypothesis to test {#three-channels}

1. **Grants cut or frozen.** Observed in the accounts: this is the {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}} episode.
2. **Responsibilities transferred without full funding.** Not measured here: a fixed compensation that falls behind the actual cost is read responsibility by responsibility (the departments' individual solidarity allowances, for example), not in an aggregate.
3. **Unfunded standards.** Not measured here: the cost of a standard is read in the impact assessments.

These three mechanisms share a hypothesis to test: a decision taken at one level can shift part of its cost onto another. Only the first is observed here; the other two require data of their own. Working paper [AWP-09](/en/awp/awp-09/) confronts the first with this statement: over the {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}} episode, the accounts make it compatible, without establishing it.

## What these data do not say {#limits}

- The national aggregate mixes municipalities, inter-municipal groupings, departments and regions; data by category go back only to 2018 for municipalities and inter-municipal groupings, and the boundaries of the categories change with reforms: the departments' consolidated database used here includes the Lyon metropolis (since 2015) and the City of Paris (since 2019), and that of the regions the single authorities of French Guiana, Martinique and Corsica — the OFGL annual report, for its part, classifies Lyon with inter-municipal groupings and Paris with municipalities.
- Transfers received include those from social security, not only from the State.
- A fall in investment concurrent with a cut in grants does not establish that the latter caused the former.
- National accounts and local government accounts do not match to the million: scopes, recording dates and adjustments differ.
- These data say nothing about the quality of the services provided, nor about who ultimately bore the adjustment.

<details class="repli" id="who-bears"><summary>Research hypothesis, not tested here: who ultimately bears the adjustment?</summary>

The accounts do not reveal whether the adjustment is ultimately borne by taxpayers, users, public employees, suppliers, landowners or the households that depend on local services. The framework of [anthropy](/en/quest-ce-que-lanthropie/) puts forward the hypothesis that some costs are harder to avoid for the least mobile households: a household that depends on social housing, public transport and local facilities bears a fare increase or a closure more directly than a household that can move to another municipality. This page does not test it; it would be verified decision by decision, and would be weakened by adjustments falling mainly on well-off households or offset by social tariffs.

</details>

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

**National accounts** — Eurostat, general government by subsector, ESA 2010: annual accounts (`gov_10a_main`: gross fixed capital formation P51G, current transfers received D73REC, taxes D2, D5 and D91, revenue TR, expenditure TE, balance B9), quarterly debt (`gov_10q_ggdebt`), debt by holding sector (`gov_10dd_ggd`), GDP from the national accounts as a check on the denominator (`nama_10_gdp`).

**Management accounts** — OFGL, consolidated databases of municipalities, inter-municipal groupings, departments and regions (data.ofgl.fr, DGFiP data).

**Texts** — General Code of Local Authorities, articles L. 1612-4 and L. 1613-1; budget acts for 2020 (art. 16), 2021 (art. 8 and 29), 2025 (art. 186) and 2026; draft budget bill tabled on {{< coll-val "plf_depot" >}} and opinion of the High Council of Public Finance on that bill, read in full and archived with their hash; Real Decreto-ley 21/2012 and Organic Law 2/2012 (Spain); Law no. 448/1998, art. 28, and Law no. 208/2015 (Italy, internal stability pact, then balanced-budget rule); Insee, *Les comptes des administrations publiques* [General government accounts] for 2010, 2014 and 2015 (in French); Court of Audit, *Les finances publiques locales 2025* [Local public finances 2025] and published responses (in French).

The calculations, checks and figures are produced by a single script, rerun each time the sources publish; no figure on this page is entered by hand, and the script refuses to write if a piece of data stops supporting a sentence. **Download the data** (CC BY 4.0 licence): [CSV](/dette_collectivites.csv), in long format, readable in a spreadsheet; [JSON](/dette_collectivites.json), with the calculations, definitions and the report of the checks (variable names and labels in French).

{{< reutiliser figures="figures_collectivites" jeu="dette_collectivites" sources="Eurostat, OFGL and Légifrance" donnees="The series by country and by category of authority, the DGF set by the budget act, the measures of the draft budget bill, the 2013-2017 decomposition and the report of the checks; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
This page checks a common thesis about local finances: over the long run, the indebtedness of French local authorities has remained contained; from {{< coll-val "ep_a0" >}} to {{< coll-val "ep_a1" >}}, the cut in central government grants coincided with a fall in their investment larger than after the other municipal elections. Compared with Germany, Italy and Spain on an equal statistical scope, France does not rank on a single scale, and in Spain more than half of subnational debt is held by central government. These series describe concomitant movements, not causes.
{{< /reutiliser >}}
