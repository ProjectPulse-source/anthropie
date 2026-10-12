---
title: "What can France decide in the European Union?"
url: /en/what-can-france-decide-in-the-european-union/
description: "What France decides alone, what it decides with the other Member States and what it can prevent: the Treaty on European Union and the TFEU quoted word for word, the voting rule in the Council, France's public votes from {ue.debut} to {ue.fin} ({ue.fr_c} against, {ue.fr_a} abstentions), each linked to the result published by the Council and to the act in the Official Journal, and the transposition of directives as at {ue.tr_date}. Open data."
chapo: "What the Treaties have not conferred on the Union remains with the Member States: France decides alone there, while respecting the common rules. Where the Union has competence, the Commission proposes and France votes with the other governments in the Council: under qualified majority, it can be outvoted; under unanimity, its single vote against can block. In the public votes of the Council on legislative acts, from {ue.debut} to {ue.fin}, France voted against {ue.fr_contre} and abstained {ue.fr_abst}. These votes record its position at the last moment, not what it obtained in the negotiation that precedes them."
date: 2026-10-06
lastmod: 2026-10-12
# English version of the "Europe" further topic of the "Presidential promises" dossier (FR:
# content/ce-que-la-france-peut-decider-dans-l-union-europeenne/_index.md). Same tokens, same keys: values come from the
# affichage_en block of data/promesses_europe.json (scripts/update_promesses_europe.py). The Treaties are quoted in their
# official English version (same Official Journal, read from Cellar and checked by the script).
donnees: [promesses_europe]
og_title: "What can France decide in the European Union? Competences, voting rules and France's votes in the Council — S. Lalut"
og_image: "images/og-europe-promesse-en.jpg"
og_image_alt: "Share card: \"France in the EU Council\" — number of votes against and abstentions of the Member States in public votes of the Council on legislative acts; France, in blue, is at the bottom of the list."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_europe"
  nom: "Competences and voting rules of the European Union, public votes of the Member States in the Council (2009-2026) and transposition of directives by France"
  description: "Typology of competences in the TFEU (art. 2 to 6, 2016 consolidated version); inventory of the legal bases of the ordinary legislative procedure and of unanimity in the Council, checked against the list of the General Secretariat of the Council; votes against, abstentions and non-participation of each Member State in the public votes of the Council on legislative acts, from {ue.debut} to {ue.fin}, checked against the SWP / GESIS dataset (doi 10.7802/2560) up to {ue.fin_temoin}; count, Council note and published act for the five acts on which France did not vote in favour; transposition indicators for France as at {ue.tr_date} (European Commission)."
  couverture_temporelle: "2009/2026"
  couverture_spatiale: "European Union"
  variables:
    - {nom: "Member States' votes in the Council: against, abstention, not taking part", unite: "public votes"}
    - {nom: "Council count for the acts on which France did not vote in favour: in favour, against, abstention, not taking part", unite: "Member States"}
    - {nom: "TFEU legal bases by decision rule", unite: "paragraphs of the Treaty"}
    - {nom: "Transposition and conformity deficits", unite: "% of Single Market directives"}
  sources:
    - "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016E/TXT"
    - "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016M/TXT"
    - "https://www.consilium.europa.eu/en/general-secretariat/corporate-policies/transparency/voting-results/"
    - "https://doi.org/10.7802/2560"
    - "https://single-market-scoreboard.ec.europa.eu/enforcement-tools/transposition_en"
  mots: ["European Union", "Council of the European Union", "qualified majority", "unanimity", "EU competences", "principle of conferral", "TFEU", "transposition", "France", "promises"]
  fichiers: ["promesses_europe.csv", "promesses_europe.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Can France block a European law?"
    answer: "That depends on the voting rule the Treaty sets for the area. Under qualified majority, the most frequent rule, no Member State can block alone: as a general rule, a blocking minority must include at least four Council members, and where some Member States do not take part in the vote, it is calculated on the participating Member States alone (article 238(3) TFEU). Where the Treaty requires unanimity, for example for indirect taxation (article 113 TFEU) or the multiannual financial framework (article 312), a single vote against is enough to prevent adoption; an abstention is not."
  - question: "How many times has France voted against a European law?"
    answer: "In the public votes of the Council of the European Union on legislative acts, from {ue.debut} to {ue.fin}, France voted against {ue.fr_contre} and abstained {ue.fr_abst}. The texts it voted against were adopted by qualified majority. In the same record, Germany voted against {ue.de_c} times and the Netherlands {ue.nl_c} times; these raw counts do not measure a Member State's influence."
  - question: "Does France transpose EU directives on time?"
    answer: "According to the European Commission's Single Market Scoreboard, as at {ue.tr_date}, {ue.tr_def}% of Single Market directives whose deadline had passed had not been transposed in France, the same as the EU average. The Commission's target is 0.5%. The directives it considers incorrectly transposed, on the basis of its infringement proceedings, amounted to {ue.tr_conf}% for France. The EU average was {ue.tr_conf_ue}%. These values come from a single edition of the scoreboard."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocoles de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-12"
  bloc: "promesses"
  rang: 70
  prolongement: true
  nature: "Treaties (EUR-Lex), EU Council votes checked against a second dataset, results and acts read at the source, European Commission; open data"
onglet:  # "Further topics" panel of the dossier bar (partials/barre-bloc.html)
  long: "What can France decide in the European Union?"
  court: "Europe"
  role: "alone, with others, despite itself"
---

{{< reutiliser-ancre >}}

The figure is surprising: across all the public votes recorded, France has almost never opposed a European law in the Council. It lends itself to three readings. France would obtain most of what it asks for before the vote; it would contribute to compromises without obtaining everything; or it would rally to texts it would have wanted otherwise. The vote count does not decide between these three stories, and this page does not claim to.

A Member State's power in the Union is not measured by the number of times it says no. It depends on the area, which sets who decides; on the voting rule, which sets what a single Member State can prevent; and on the negotiation, which the final vote does not show. The page follows that boundary: what France decides alone, what it decides with others, what it can block or must accept, and what it does with the adopted text. It relies on the text of the Treaties in force and on the votes published by the Council.

## What can France decide alone? {#decider-seule}

Whatever the Treaties have not entrusted to the Union remains with the Member States: this is the principle of conferral (Treaty on European Union, or TEU, art. 4 and 5). The Treaty itself names one matter that stays national: "{{< ue-val "cit_tue4_2" >}}" (TEU, art. 4(2)). In other areas, the law stays national and the Union only supports, coordinates or supplements the action of the Member States, without harmonising their laws: {{< ue-val "appui" >}} (Treaty on the Functioning of the European Union, or TFEU, art. 2(5) and art. 6).

Holding a competence does not exempt a Member State from the common rules when it exercises it. Each Member State must ensure fulfilment of the obligations arising from the Treaties (sincere cooperation, TEU, art. 4(3)) and may not discriminate on grounds of nationality (TFEU, art. 18); a French law that affects trade may also come up against the freedoms of movement of the internal market. France decides alone in these matters; it does not decide outside Union law. The same sector may also fall under several competences: supporting competence does not, on that basis alone, allow national laws to be harmonised, but in health, for example, the Treaty also allows the Union to set standards of quality and safety for organs, blood, medicinal products and medical devices (TFEU, art. 168(4)).

<details class="repli"><summary>The articles quoted, word for word</summary>

The TEU sets the rule: "{{< ue-val "cit_tue4_1" >}}" (art. 4(1)). The principle of conferral: "{{< ue-val "cit_tue5_2" >}}" (art. 5(2)). In the areas of support, coordination and supplement, the Union's legally binding acts "{{< ue-val "cit_2_5b" >}}" (TFEU, art. 2(5)). Sincere cooperation: "{{< ue-val "cit_tue4_3" >}}" (TEU, art. 4(3)). Non-discrimination: "{{< ue-val "cit_18" >}}" (TFEU, art. 18).

Both Treaties are quoted in their 2016 consolidated version, that is the text in force with its successive amendments incorporated, as published in the Official Journal of the Union, in their official English text and without the case law of the Court that interprets them.

</details>

**"France decides alone" does not mean "the president decides alone".** A national decision may require a law, a decree or the involvement of other French authorities: the page [What can the French president decide alone?](/en/what-can-the-french-president-decide-alone/#decider-seul) sets them apart.

## In which areas does the Union decide? {#competences}

The TFEU classifies the competences conferred on the Union into three categories (art. 2 to 6).

- **Exclusive competence** (art. 3): only the Union legislates, the Member States being able to do so only if empowered by the Union or to implement its acts. It covers {{< ue-val "exclusives" >}}, as well as certain international agreements.
- **Shared competence** (art. 4): the Union and the Member States may legislate, the Member States as long as the Union has not exercised its competence. It covers in particular the internal market, agriculture and fisheries, the environment, transport and energy.
- **Support, coordination, supplement** (art. 6): human health, industry, culture, education and the other areas named in the previous section, where the law stays national.

<details class="repli"><summary>What articles 2 to 6 of the TFEU say</summary>

Article 2(1), on exclusive competence: "{{< ue-val "cit_2_1" >}}" Article 2(2), on shared competence: "{{< ue-val "cit_2_2" >}}" The list of shared competences is not closed: any competence conferred that is neither exclusive nor supporting is shared (art. 4(1)). In research, technological development, space, development cooperation and humanitarian aid, Union action cannot prevent the Member States from exercising their own competence (art. 4(3) and (4)). The Union also has exclusive competence for certain international agreements (art. 3(2)).

The Member States also coordinate their economic and employment policies under arrangements set by the Treaty, and the Union may take initiatives to coordinate their social policies (art. 5); the common foreign and security policy follows the TEU's own rules (art. 2(4)).

</details>

{{< ue-tableau "competences" "The areas, quoted from the Treaty" >}}

## Who puts a text on the agenda, who proposes it, who adopts it? {#initiative}

Where the Union has competence, three powers are distinct.

**Proposing** belongs, as a rule, to the Commission (TEU, art. 17(2); TFEU, art. 294(2)). A government therefore does not itself table a draft European law.

**Putting a subject on the agenda** remains open to it, together with others. The Council may ask the Commission to submit proposals to it, and if the Commission does not, it must give the Council its reasons (TFEU, art. 241). In judicial cooperation in criminal matters and police cooperation, acts may also be adopted "{{< ue-val "cit_76" >}}" (art. 76).

**Adopting** belongs, under the ordinary legislative procedure, to the European Parliament and to the Council of the European Union. Two institutions have similar names: in the Council of the European Union sits one minister from each Member State, depending on the subject (agriculture, finance, environment…); in the European Council sit the Heads of State or Government, who set the general political directions and do not vote on laws (TEU, art. 15(1): "{{< ue-val "cit_tue15" >}}"). The votes on this page are those of the Council of the European Union.

**What the proposal changes for France.** Once the proposal has been tabled, the Council may amend it only unanimously, except in the cases the Treaty lists (conciliation with the European Parliament, budgetary and financial procedures); the Commission, for its part, may alter its proposal as long as the Council has not acted (TFEU, art. 293). Outside these exceptions, the rule works both ways: the other Member States cannot rewrite the proposal in the Council without France's agreement, and a majority of Member States, France included, is not enough to rewrite it either.

<details class="repli"><summary>The articles quoted, word for word</summary>

The Commission's initiative: "{{< ue-val "cit_17_2" >}}" (TEU, art. 17(2)); the article describing the ordinary legislative procedure opens thus: "{{< ue-val "cit_294_2" >}}" (TFEU, art. 294(2)). The Council's request, and what follows a refusal: "{{< ue-val "cit_241" >}}" (TFEU, art. 241). The Council of the European Union consists of a representative of each Member State at ministerial level (TEU, art. 16(2)).

Article 293 TFEU, first paragraph: where the Council acts on a proposal from the Commission, "{{< ue-val "cit_293_1" >}}". Second paragraph: "{{< ue-val "cit_293_2" >}}".

</details>

## What voting rules apply in the Council? {#regles-de-vote}

The rule depends on the legal basis, the article of the Treaty on which the act is founded. The general case is **qualified majority**, defined as "{{< ue-val "cit_16_4" >}}" (TEU, art. 16(4)); where the Council does not act on a proposal from the Commission, it takes "{{< ue-val "cit_238_2" >}}" (TFEU, art. 238(2)). The same article 16 adds: "{{< ue-val "cit_tue16" >}}". That is the general rule; where not all the members of the Council take part in the vote, the Treaty calculates the qualified majority and the blocking minority on the participating Member States alone (TFEU, art. 238(3)). No Member State therefore forms a blocking minority on its own, and France can be outvoted.

The record of votes, further down, spans three regimes of qualified majority: weighted votes, then the double majority with the option of requesting the former calculation, then the double majority alone. The Member States' votes were weighted until {{< ue-val "dm_fin_ancien" >}}. The double majority has applied since {{< ue-val "dm_debut" >}}; until {{< ue-val "dm_option_fin" >}}, a member of the Council could still request the former calculation (Protocol No 36 on transitional provisions).

In other areas, the Council acts **unanimously**: indirect taxation, the Union's own resources or the multiannual financial framework, for example (table below).

**Voting against or abstaining.** Under qualified majority, voting against and abstaining both prevent the Member State's vote from counting towards the favourable majority. But the two positions do not say the same thing politically. Under unanimity, an abstention does not block: a vote against can block. The Treaty puts it this way: "{{< ue-val "cit_238_4" >}}" (TFEU, art. 238(4)).

{{< ue-tableau "instruments" "The rule, area by area, for the instruments named in the book and in programmes" >}}

<details class="repli"><summary>How many legal bases, and how they were counted</summary>

The inventory of the TFEU contains {{< ue-val "n_plo" >}} legal bases of the ordinary legislative procedure, in {{< ue-val "n_plo_art" >}} articles, and {{< ue-val "n_una" >}} legal bases where the Council acts unanimously, in {{< ue-val "n_una_art" >}} articles; the latter ground legislative and non-legislative acts. These numbers measure neither the weight of the areas nor how often acts are adopted on each base.

The text is the consolidated version of the TFEU published in the Official Journal of the European Union on 7 June 2016, read in French and in English. Each area of articles 3, 4 and 6 is quoted word for word, the completeness of each list is reread in the text, and the English lists have the same number of areas as the French ones. These {{< ue-val "n_plo" >}} legal bases and the {{< ue-val "n_cond_min" >}} conditional ones were compared with the list published by the General Secretariat of the Council in its guide to that procedure (annex III, {{< ue-val "n_temoin" >}} entries): the two lists match exactly. This comparison brought out bases that refer to the procedure without naming it (articles 42, 62 and 177), which were read and added. {{< ue-val "n_cond" >}} bases follow a procedure that depends on the measure (articles 83(2) and 136(1)). Mentions that do not ground an act (emergency brakes, bridging clauses, articles describing the procedure) are set aside, each with its reason, in the data file.

The unanimity list relies on the word: a base that referred to unanimity without using it would escape the inventory, and the list has no second producer on the same scope. A 2014 academic inventory (S. Polidori, *Eurostudium3w*) counts {{< ue-val "polidori_tfue" >}} TFEU provisions requiring unanimity, European Council included; it is not the same unit, so it does not check this inventory.

</details>

## How does France vote in the Council? {#votes-au-conseil}

<div class="resultat-phrase">

**The result in one sentence.** In the public votes of the Council of the European Union on legislative acts, from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}, France voted against {{< ue-val "fr_contre" >}} and abstained {{< ue-val "fr_abst" >}}; it voted in favour in every other case.

</div>

All {{< ue-val "n_actes" >}} texts were adopted. On the {{< ue-val "fr_c_l" >}} it voted against, France was outvoted: qualified majority at work. On the {{< ue-val "fr_a_l" >}} acts on which it abstained, France did not vote against. But under qualified majority, its abstention does not help to reach the favourable majority, any more than a vote against does. Each row of the table links to the result published by the Council and to the act in the Official Journal, dated after the vote, once signed.

{{< ue-tableau "france" "The acts on which France did not vote in favour" "ouvert" >}}

**Two votes against that the Council does not attest.** A second dataset, drawn from the Council's files by a German institute, SWP, counts two more votes against by France, dated {{< ue-val "ecart_date" >}}, with no title or subject. We looked for them in the Council's publications: its summary of the month's acts mentions neither a meeting nor a legislative act on that day, and its search of votes returns none between {{< ue-val "ecart_avant" >}} and {{< ue-val "ecart_apres" >}}. These two entries are therefore not counted. Not having found them does not prove that no vote took place: what they referred to remains unknown, and the details of the search are in the collapsed section "How the record was compiled and checked".

A country that rarely votes against is not necessarily a country that obtains more. These bars show votes, not balances of power.

{{< figure-svg fichier="europe-votes-en" alt="Horizontal bars, one per Member State, sorted by total: votes against in dark, abstentions in light, with both numbers after each bar; France, in blue, is at the bottom of the list. The values are in the table below the figure." >}}Votes against and abstentions of each Member State in the public votes of the Council of the European Union on legislative acts, from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}. The United Kingdom appears only until its withdrawal, Croatia since its accession in 2013, and Denmark and Ireland do not take part in some acts: these raw counts are not a ranking of influence.{{< /figure-svg >}}

{{< fig-actions id="votes" >}}

{{< ue-tableau "etats" "Each Member State's votes in a table" >}}

In the same record, Germany voted against {{< ue-val "de_c" >}} times and abstained {{< ue-val "de_a" >}} times. The Netherlands voted against {{< ue-val "nl_c" >}} times, Poland {{< ue-val "pl_c" >}} times. Hungary did so {{< ue-val "hu_c" >}} times.

**What these figures do not say.** They describe the formal position of the Member States at the final vote. They measure neither their influence in the negotiation, nor what they obtained or gave up, nor their general capacity to block a decision. The record covers only **public** votes on **legislative** acts: not non-legislative acts, not foreign policy, not the discussions that precede the vote.

<details class="repli"><summary>How the record was compiled and checked</summary>

**The record.** The Council discontinued its open datasets in March 2025; its voting results are now published only through its search page, which does not accept automated programs. The record was therefore compiled in a browser, on {{< ue-val "releve" >}}, page by page: {{< ue-val "entrees" >}} entries, exactly the total announced by the page; the search, filtered in turn on France and on Germany, returns the same entries. Among them, {{< ue-val "qmv" >}} were taken by qualified majority, {{< ue-val "una" >}} by unanimity and {{< ue-val "qmv_sp" >}} by qualified majority without a proposal from the Commission. The Council displays {{< ue-val "doublons" >}} duplicate entries, identical in every field: the number of acts lies between {{< ue-val "entrees_min" >}} and {{< ue-val "entrees" >}}. These duplicates are unanimous votes and change no count of votes against or abstentions.

**The second dataset.** The dataset compiled by the German Institute for International and Security Affairs (SWP) from the Council's data, from {{< ue-val "debut" >}} to {{< ue-val "fin_temoin" >}}, was matched against the record act by act, then Member State by Member State: the counts of votes against and abstentions of {{< ue-val "etats_identiques" >}} Member States out of {{< ue-val "etats_total" >}} are identical in both sources, and the gaps of the others are explained. One act of 28 March 2023 is missing from the SWP dataset, frozen two weeks later. Two untitled, unanimous entries of the SWP dataset could not be corroborated; they change no count of votes against or abstentions.

**The two votes against of {{< ue-val "ecart_date" >}}.** They appear only in the SWP dataset, with no title or subject, each with France alone against. They carry voting-procedure identifiers from the Council's open files, which the Council no longer publishes. The Council's monthly summary of acts for May 2021 (document ST 8962/21, published on 28 June 2021) mentions no Council meeting on that day; it lists only one act then, a common foreign and security policy decision adopted by written procedure, outside the scope of legislative acts, and no legislative written procedure in the month. The Council's search of votes, read on 12 October 2026, returns votes on {{< ue-val "ecart_avant" >}} and then on {{< ue-val "ecart_apres" >}}, and none in between; the Council's document register contains no voting result in the week of {{< ue-val "ecart_date" >}}, while it does contain those of the previous week. As they could not be corroborated, the published count does not include them. Where these two entries come from, a data-entry error or a vote never published, none of the documents read makes it possible to say.

**The five acts.** For each, the Council's "voting result" note and the act published in the Official Journal, in French and in English, were archived on 12 October 2026. The count is read in the annex to the note and on the Council's search page; the script checks in the archived documents the procedure, the date of the vote and, in the act, its number, its date and the mention of the Council's decision on the date of the vote. The {{< ue-val "n_actes_temoin" >}} votes covered by the SWP dataset, up to {{< ue-val "fin_temoin" >}}, have the same count there, which the script recalculates from that dataset; the {{< ue-val "n_actes_source" >}} later ones are documented at the source, with no second dataset: the script rereads, Member State by Member State, the composition of each one in the archived annex of the Council note. {{< ue-val "n_ponderes_maj" >}} of these votes, held before {{< ue-val "dm_debut" >}}, were counted in weighted votes.

**What the producer of the second dataset already wrote.** SWP wrote in December 2021: "{{< ue-val "swp21_cit" >}}". Our record counts, from 2010 to 2021, {{< ue-val "swp21_contre" >}} vote against and {{< ue-val "swp21_abst" >}} abstentions by France: the same count, which therefore does not include the {{< ue-val "swp24_ecart" >}} votes against of {{< ue-val "ecart_date" >}} that the dataset carries. In April 2024, the same institute writes, for 2010 to September 2023: "{{< ue-val "swp24_cit" >}}". Our record counts {{< ue-val "swp24_nonpour" >}} votes against or abstentions over that period. The numerical difference is {{< ue-val "swp24_ecart" >}} occurrences, like the {{< ue-val "swp24_ecart" >}} disputed entries of {{< ue-val "ecart_date" >}}. In the absence of a list naming the {{< ue-val "swp24_annonce" >}} votes retained in the 2024 analysis, this match does not establish that they are the same acts.

</details>

## Why can a Member State vote yes to a text it wanted to be different? {#voter-oui}

The final vote records only the last step of a sequence. **First**, each government arrives with a position: what it asks for, what it refuses. **Next**, the text is negotiated. The Commission may alter its proposal as long as the Council has not acted, the European Parliament adopts its own positions and, on the governments' side, "{{< ue-val "cit_16_7" >}}" (TEU, art. 16(7)). **Then** a final text is put to the vote, which may depart from what each Member State asked for at the outset. **Finally**, each Member State votes in favour, against, abstains or does not take part.

A "yes" at this last step is compatible with the three stories of the opening: the Member State obtained most of what it asked for, it contributed to a compromise without obtaining everything, or it rallied to a text it would have wanted otherwise. The count does not allow them to be told apart. That would require sources on the negotiation itself, act by act, which the record of votes does not contain. The final vote is an observation, not a history of preferences and concessions.

## Does France transpose directives on time? {#transposition}

After the vote, France must apply what has been adopted, whether or not it voted for it. For a directive, the Treaty states: "{{< ue-val "cit_288" >}}" (TFEU, art. 288); each directive sets the date by which it must be transposed. Twice a year, the European Commission measures the share of Single Market directives that are not transposed on time: this is the transposition deficit.

As at {{< ue-val "tr_date" >}}, this deficit stood at {{< ue-val "tr_def" >}}% in France, the same value as the EU average. That amounts to {{< ue-val "tr_retard" >}} directives out of {{< ue-val "tr_dues" >}}. The Commission also counts the directives it considers incorrectly transposed, on the basis of its infringement proceedings: this is the conformity deficit, at {{< ue-val "tr_conf" >}}% for France. The EU average is {{< ue-val "tr_conf_ue" >}}%, and the opening of infringement proceedings does not itself establish a breach found by the Court. The Commission places France among the {{< ue-val "tr_double" >}} Member States that combine a high transposition deficit and a high conformity deficit.

**These values come from a single edition of the scoreboard.** They do not say whether France's delay is growing or shrinking.

<details class="repli"><summary>How these values were recorded, and the target set</summary>

The Commission publishes these values only in an interactive table, with no file: they were recorded from an archived screenshot, and the EU averages checked against the Commission's text. The European Council set a transposition deficit target of 1% in 2007. The Commission lowered it to 0.5% (Single Market Act of 2011, Communication of March 2023).

</details>

{{< ue-tableau "transposition" "France's transposition indicators" >}}

A delay can lead to infringement proceedings: the Commission delivers a reasoned opinion, then may bring the matter before the Court of Justice (TFEU, art. 258); another Member State may also do so (art. 259). Where a Member State has failed to notify measures transposing a directive adopted under a legislative procedure, the Court may impose a lump sum or a penalty payment as soon as it finds the infringement (art. 260(3)).

## Before assessing a European promise, what should be checked? {#avant-d-evaluer}

A campaign promise that touches on Europe can be read with five questions, in this order.

1. **Has the area been conferred on the Union?** If not, France decides alone, while respecting the common rules; if the competence is shared, the room for manoeuvre depends on what the Union has already adopted.
2. **Who must propose?** As a rule the Commission: France can ask for a proposal, through the Council or with other Member States, not table one alone.
3. **Which voting rule does the legal basis set?** Under qualified majority, France can be outvoted; under unanimity, its vote against can block, its abstention cannot.
4. **What will France have to do after adoption?** Apply a regulation, transpose a directive by the set date, under the supervision of the Commission and the Court.
5. **What will the final vote show?** France's position at the last moment, not what it obtained along the way.

## What this page does not say {#limites}

It does not say whether the Union decides too much or too little, nor whether France carries much or little weight in it: none of the measures presented measures that. It does not relate votes against and abstentions to the number of votes in which each Member State could take part; such a normalisation would require building these denominators, and would still say nothing about influence. It counts neither acts of the Commission, nor decisions of the European Central Bank, nor judgments of the Court of Justice, nor Council votes on non-legislative acts, such as decisions on signing a trade agreement: the January 2026 decisions on signing the agreement between the Union and Mercosur, adopted by written procedure, fall outside the record, whatever each Member State's vote. It reads the Treaties in force, without case law. The votes stand as at {{< ue-val "fin" >}}, transposition as at {{< ue-val "tr_date" >}}.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Changing the European rules" avis="non" >}}
This page draws the boundary between what France decides alone, what it decides with the other Member States and what it can prevent. The book, in French, follows two French preferences all the way to the European rule, one adopted, the other blocked, and compares promises to "change Europe" with what the Treaty allows. It gives no voting advice.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Treaty on European Union**, consolidated version, Official Journal of the European Union C 202 of 7 June 2016 (EUR-Lex), art. 4, 5, 15, 16 and 17.

**Treaty on the Functioning of the European Union**, same Official Journal, art. 2 to 6, 18, 76, 238, 241, 258 to 260, 288, 293 and 294, and the whole Treaty for the legal bases; Protocol No 36 on transitional provisions.

**Council of the European Union**, search of voting results on legislative acts (recorded on {{< ue-val "releve" >}}); "voting result" notes of the public register of documents, linked to the five acts of the table; monthly summary of Council acts, May 2021 (ST 8962/21, 28 June 2021); General Secretariat of the Council, *Guide to the ordinary legislative procedure*, 2010, annex III (doi 10.2860/74684).

**Official Journal of the European Union** (EUR-Lex), the five acts of the table, linked row by row.

**Ondarza, Nicolai von and Bochtler, Paul**, *Public Voting Data of the Council of the EU*, version 2.0.0, SWP, 2023, doi [10.7802/2560](https://doi.org/10.7802/2560), CC BY 4.0 licence.

**European Commission**, Single Market and Competitiveness Scoreboard, transposition, edition as at {{< ue-val "tr_date" >}}.

The figures, the checks and the chart are produced by a single script. It rereads the archived Treaty, where each quotation is found word for word, the SWP dataset and the archived documents of the five acts. The counts of votes by Member State, recorded in a browser, and the count of each act, read in the annex to the Council's note, are transcribed in the script, which stops if the recalculation from the SWP dataset contradicts them over the common period; votes after March 2023 have no second dataset. For the two votes against in the SWP dataset that the count sets aside, the script rereads the archived summary of the Council's acts for May 2021 and checks that the SWP dataset carries nothing but them between the two votes that frame them in the Council's search, which are transcribed. The transposition indicators are transcribed from a screenshot, and their EU averages checked against the Commission's text. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_europe.csv), long format; [JSON](/promesses_europe.json), with the legal bases, the explained gaps, the five acts and the report of the checks. An earlier version of this dataset is archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_europe" jeu="promesses_europe" sources="TEU and TFEU, Council of the EU, Official Journal, SWP / GESIS and European Commission" donnees="The votes against, abstentions and non-participation of each Member State in the Council, the five acts on which France did not vote in favour with their count and references, the TFEU legal bases by decision rule and France's transposition indicators; the same content exists in CSV, long format, readable in a spreadsheet." >}}
What the Treaties have not conferred on the Union remains with the Member States: France decides alone there, while respecting the common rules. Where the Union has competence, the Commission proposes, and the Council votes most often by qualified majority, sometimes unanimously. In the public votes of the Council on legislative acts, from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}, France voted against {{< ue-val "fr_contre" >}} and abstained {{< ue-val "fr_abst" >}}; a vote in favour does not say what it obtained or gave up in the negotiation.
{{< /reutiliser >}}
