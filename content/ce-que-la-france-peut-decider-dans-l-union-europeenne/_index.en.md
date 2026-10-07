---
title: "What can France decide in the European Union?"
url: /en/what-can-france-decide-in-the-european-union/
description: "In which areas the Union decides, under which rule, and how France voted in the Council: the competences set by the Treaty, {ue.n_plo} legal bases of the ordinary legislative procedure and {ue.n_una} legal bases requiring unanimity found in the TFEU, France's public votes from {ue.debut} to {ue.fin} ({ue.fr_c} against, {ue.fr_a} abstentions) and the transposition of directives as at {ue.tr_date}. Open data."
chapo: "A promise that touches the internal market, trade or agriculture is decided partly in Brussels, with others. The Treaty sets the areas where only the Union may legislate, those where it shares this competence with the Member States and those where it only supports their action; it also sets the voting rule, most often qualified majority, sometimes unanimity. In the public votes of the Council on legislative acts, from {ue.debut} to {ue.fin}, France voted against {ue.fr_contre} and abstained {ue.fr_abst}; it voted in favour in every other case. That final vote does not say what France obtained or gave up in the negotiation that precedes it."
date: 2026-10-06
lastmod: 2026-10-06
# English version of the "Europe" further topic of the "Presidential promises" dossier (FR:
# content/ce-que-la-france-peut-decider-dans-l-union-europeenne/_index.md). Same tokens, same keys: values come from the
# affichage_en block of data/promesses_europe.json (scripts/update_promesses_europe.py). The Treaties are quoted in their
# official English version (same Official Journal, read from Cellar and checked by the script).
donnees: [promesses_europe]
og_title: "What can France decide in the European Union? Competences, voting rules and France's votes in the Council — S. Lalut"
og_image: "images/og-europe-promesse-en.jpg"
og_image_alt: "Share card: \"France in the EU Council\" — votes against and abstentions of the Member States in public votes on legislative acts, 2009-2026; France is at the bottom of the list, with two votes against and three abstentions."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_europe"
  nom: "Competences and voting rules of the European Union, public votes of the Member States in the Council (2009-2026) and transposition of directives by France"
  description: "Typology of competences in the TFEU (art. 2 to 6, 2016 consolidated version); inventory of the legal bases of the ordinary legislative procedure and of unanimity in the Council, checked against the list of the General Secretariat of the Council; votes against, abstentions and non-participation of each Member State in the public votes of the Council on legislative acts, from {ue.debut} to {ue.fin}, checked against the SWP / GESIS dataset (doi 10.7802/2560); transposition indicators for France as at {ue.tr_date} (European Commission)."
  couverture_temporelle: "2009/2026"
  couverture_spatiale: "European Union"
  variables:
    - {nom: "Member States' votes in the Council: against, abstention, not taking part", unite: "public votes"}
    - {nom: "TFEU legal bases by decision rule", unite: "paragraphs of the Treaty"}
    - {nom: "Transposition and conformity deficits", unite: "% of Single Market directives"}
  sources:
    - "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016E/TXT"
    - "https://www.consilium.europa.eu/en/general-secretariat/corporate-policies/transparency/voting-results/"
    - "https://doi.org/10.7802/2560"
    - "https://single-market-scoreboard.ec.europa.eu/enforcement-tools/transposition_en"
  mots: ["European Union", "Council of the European Union", "qualified majority", "unanimity", "EU competences", "TFEU", "transposition", "France", "promises"]
  fichiers: ["promesses_europe.csv", "promesses_europe.json"]
  doi: "10.5281/zenodo.23212665"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Can France block a European law?"
    answer: "That depends on the voting rule the Treaty sets for the area. Under the ordinary legislative procedure, the Council acts by qualified majority: no Member State can block alone. Where the Treaty requires unanimity in the Council (indirect taxation, article 113 TFEU, or the multiannual financial framework, article 312), a single Member State can object. The TFEU contains {ue.n_plo} legal bases of the ordinary legislative procedure and {ue.n_una} legal bases where the Council acts unanimously; these numbers measure neither the weight of the areas nor how often acts are adopted on each base."
  - question: "How many times has France voted against a European law?"
    answer: "In the public votes of the Council of the European Union on legislative acts, from {ue.debut} to {ue.fin}, France voted against {ue.fr_contre} and abstained {ue.fr_abst}; it voted in favour in every other case. For comparison, in the same record, Germany voted against {ue.de_c} times, the Netherlands {ue.nl_c} times, Poland {ue.pl_c} times. A vote in favour does not say what France was asking for at the outset."
  - question: "Does France transpose EU directives on time?"
    answer: "According to the European Commission's Single Market Scoreboard, as at {ue.tr_date}, {ue.tr_def}% of Single Market directives had not been transposed in France ({ue.tr_retard} directives), the same as the EU average; the target, set at 1% in 2007, was lowered to 0.5% by the Commission. The conformity deficit, based on the Commission's proceedings for incorrect transposition, was {ue.tr_conf}%, against {ue.tr_conf_ue}% on average."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 70
  prolongement: true
  nature: "Treaty (EUR-Lex), EU Council votes checked against a second dataset, European Commission; open data"
onglet:  # "Further topics" panel of the dossier bar (partials/barre-bloc.html)
  long: "What can France decide in the European Union?"
  court: "Europe"
  role: "competences, votes and transposition"
---

{{< reutiliser-ancre >}}

A promise that touches the internal market, trade, agriculture or asylum is not decided in Paris alone. The Treaty on the Functioning of the European Union (TFEU) says in which areas the Union decides and under which rule; the Council of the Union, where governments sit, publishes each Member State's vote on legislative acts. This page reads the Treaty article by article, records the published votes and checks them against a second dataset. No numerical value is entered manually. The Treaties are quoted in their official English version.

**Short answer.** In areas of exclusive Union competence, France cannot itself legislate or adopt legally binding acts, except where empowered by the Union or for the implementation of Union acts; it takes part in Union decisions according to the procedures laid down in the Treaties. In areas of shared competence, the Member States exercise their competence to the extent that the Union has not exercised its own. In the Council, the rule is most often qualified majority, and unanimity in some areas. In the public votes from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}, France voted against {{< ue-val "fr_contre" >}} and abstained {{< ue-val "fr_abst" >}}.

## In which areas does the Union decide? {#competences}

The Treaty classifies the Union's competences into three main categories, and says for each what remains with the Member States.

- **Exclusive competence** (art. 3): {{< ue-val "exclusives" >}}. "{{< ue-val "cit_2_1" >}}" (art. 2(1)). The Union also has exclusive competence for certain international agreements (art. 3(2)).
- **Shared competence** (art. 4): the "principal areas" are {{< ue-val "partagees" >}}. "{{< ue-val "cit_2_2" >}}" (art. 2(2)). The list is not closed: any competence conferred that is neither exclusive nor supporting is shared (art. 4(1)). In research, space, development cooperation and humanitarian aid, Union action cannot prevent Member States from exercising theirs (art. 4(3) and (4)).
- **Competence to support, coordinate or supplement** (art. 6): {{< ue-val "appui" >}}. In these areas, "{{< ue-val "cit_2_5" >}}" (art. 2(5)).

Economic and employment policies are coordinated (art. 5), and the common foreign and security policy follows its own rules, set by the Treaty on European Union (art. 2(4)).

{{< ue-tableau "competences" "The areas, quoted from the Treaty" >}}

## What voting rules apply in the Council? {#regles-de-vote}

Two rules dominate. Under the **ordinary legislative procedure**, the European Parliament and the Council adopt the act together, and the Council acts by qualified majority: no Member State can block alone, since, under the Treaty on European Union, "{{< ue-val "cit_tue16" >}}" (art. 16(4)). In other areas, the Council **acts unanimously**: a single Member State can object. The full inventory of the TFEU contains {{< ue-val "n_plo" >}} legal bases of the ordinary legislative procedure, in {{< ue-val "n_plo_art" >}} articles, and {{< ue-val "n_una" >}} legal bases where the Council acts unanimously, in {{< ue-val "n_una_art" >}} articles. These numbers measure neither the weight of the areas nor how often acts are adopted on each base: a single base, article 114 on the internal market, underpins a large number of acts.

{{< ue-tableau "instruments" "The rule, area by area, for the instruments named in the book and in programmes" >}}

<details class="repli"><summary>What was checked</summary>

The text is the consolidated version of the TFEU published in the Official Journal of the European Union on 7 June 2016, read in French and in English. Each area of articles 3, 4 and 6 is quoted word for word, the completeness of each list is reread in the text, and the English lists have the same number of areas as the French ones. The {{< ue-val "n_plo" >}} legal bases were compared with the list published by the General Secretariat of the Council in its guide to the ordinary legislative procedure (annex III, {{< ue-val "n_temoin" >}} entries): the two lists match exactly. This comparison brought out bases that refer to the procedure without naming it (articles 42, 62 and 177), which were read and added. {{< ue-val "n_cond" >}} bases follow a procedure that depends on the measure (articles 83(2) and 136(1)). Mentions that do not ground an act (emergency brakes, bridging clauses, articles describing the procedure) are set aside, each with its reason, in the data file. The unanimity list has no second producer on the same scope: a 2014 academic inventory (S. Polidori, *Eurostudium3w*) counts {{< ue-val "polidori_tfue" >}} TFEU provisions requiring unanimity, European Council included; it is not the same unit, so it does not check this list.

</details>

## How does France vote in the Council? {#votes-au-conseil}

{{< figure-svg fichier="europe-votes-en" alt="Horizontal bars, one per Member State, sorted by total: votes against in dark, abstentions in light, with both numbers after each bar; France, in blue, is at the bottom of the list. The values are in the table below the figure." >}}Votes against and abstentions of each Member State in the public votes of the Council of the European Union on legislative acts, from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}. The United Kingdom appears only until its withdrawal, Croatia since its accession in 2013. These raw counts are not a ranking of influence: length of membership and non-participation in some acts differ between Member States.{{< /figure-svg >}}

{{< fig-actions id="votes" >}}

<div class="resultat-phrase">

**The result in one sentence.** In the public votes of the Council of the European Union on legislative acts, from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}, France voted against {{< ue-val "fr_contre" >}} and abstained {{< ue-val "fr_abst" >}}; it voted in favour in every other case.

</div>

{{< ue-tableau "france" "The acts on which France did not vote in favour" >}}

{{< ue-tableau "etats" "Each Member State's votes in a table" >}}

For comparison, in the same record, Germany voted against {{< ue-val "de_c" >}} times and abstained {{< ue-val "de_a" >}} times, the Netherlands voted against {{< ue-val "nl_c" >}} times, Poland {{< ue-val "pl_c" >}} times, Hungary {{< ue-val "hu_c" >}} times. Among the published votes, {{< ue-val "qmv" >}} were taken by qualified majority and {{< ue-val "una" >}} by unanimity.

**What these figures do not say.** A vote in favour, at the end of a negotiation, does not say what France was asking for at the outset, nor what it obtained or gave up. The record covers only **public** votes on **legislative** acts: not non-legislative acts, not foreign policy, not the discussions that precede the vote. These counts describe the formal position of the Member States at the final vote. They measure neither their influence in the negotiation, nor what they obtained or gave up, nor their general capacity to block a decision.

<details class="repli"><summary>What was checked</summary>

**The record.** The Council discontinued its open datasets in March 2025; its voting results are now published only through its search page, which does not accept automated programs. The dataset was therefore compiled in a browser, on {{< ue-val "releve" >}}, page by page: {{< ue-val "entrees" >}} entries, exactly the total announced by the page, and the same entries seen from France and from Germany. The Council displays {{< ue-val "doublons" >}} duplicate entries, identical in every field: the number of acts lies between {{< ue-val "entrees_min" >}} and {{< ue-val "entrees" >}}. These duplicates are unanimous votes and change no count of votes against or abstentions.

**The cross-check.** The dataset compiled by the German Institute for International and Security Affairs (SWP) from the Council's data, from 2010 to March 2023, was matched against the record act by act, then Member State by Member State: the counts of votes against and abstentions of {{< ue-val "etats_identiques" >}} Member States out of {{< ue-val "etats_total" >}} are identical in both sources, and the gaps of the others are explained: one act of 28 March 2023 is missing from the SWP dataset, frozen two weeks later; two votes against by France dated 17 May 2021 appear only in the SWP dataset, with no title or subject, and the Council's document register contains no voting result that week, while it does contain those of the previous week. These two votes appear in the SWP dataset but could not be corroborated in the Council results and documents used for this page; they are therefore not included in the published count. Two other entries of the SWP dataset, untitled and unanimous, could not be corroborated either; they change no count of votes against or abstentions.

**What the producer of the cross-check already wrote.** The German institute that compiled this dataset (SWP) wrote in December 2021: "{{< ue-val "swp21_cit" >}}". Our record counts, from 2010 to 2021, {{< ue-val "swp21_contre" >}} vote against and {{< ue-val "swp21_abst" >}} abstentions by France; that finding cannot include the {{< ue-val "swp24_ecart" >}} votes against of 17 May 2021 that the dataset carries. In April 2024, the same institute writes, for 2010 to September 2023: "{{< ue-val "swp24_cit" >}}". Our record counts {{< ue-val "swp24_nonpour" >}} votes against or abstentions over that period; the difference equals the {{< ue-val "swp24_ecart" >}} dataset entries that this page sets aside, although the 2024 note does not list the votes it counts.

</details>

## Does France transpose directives on time? {#transposition}

A directive sets a result; each Member State transposes it into its own law, before a deadline. Twice a year, the European Commission measures the share of Single Market directives that are not transposed on time. As at {{< ue-val "tr_date" >}}, {{< ue-val "tr_def" >}}% of the Single Market directives whose deadline had passed were not transposed in France, that is {{< ue-val "tr_retard" >}} directives out of {{< ue-val "tr_dues" >}}, the same value as the EU average. The European Council set a 1% target in 2007, which the Commission lowered to 0.5% (Single Market Act of 2011, Communication of March 2023). The conformity deficit, the percentage of Single Market directives considered incorrectly transposed in the Commission's infringement monitoring, stands at {{< ue-val "tr_conf" >}}% there, against {{< ue-val "tr_conf_ue" >}}% on average. The opening of infringement proceedings does not itself establish a breach of EU law: only the Court of Justice can rule definitively that it has occurred. The Commission places France among the {{< ue-val "tr_double" >}} Member States that combine a high transposition deficit and a high conformity deficit.

{{< ue-tableau "transposition" "France's transposition indicators" >}}

These values come from a single edition of the Commission's scoreboard, which publishes them only in an interactive table, with no file: they were recorded from an archived screenshot, and the EU averages checked against the Commission's text. A late transposition can lead to infringement proceedings (art. 258 to 260 TFEU), which the Commission opens and the Court of Justice decides.

## What this page does not say {#limites}

It does not say whether the Union decides too much or too little, nor whether France carries much or little weight in it: none of the measures presented measures that. It counts neither acts of the Commission, nor decisions of the European Central Bank, nor judgments of the Court of Justice. Nor does it count Council votes on non-legislative acts, such as decisions on signing a trade agreement: the January 2026 decisions on signing the agreement between the Union and Mercosur, adopted by written procedure, fall outside the record, whatever each State's vote. It examines the Treaty as currently in force, without case law: it is the Court that rules on the choice of a legal basis. The votes stand as at {{< ue-val "fin" >}}, transposition as at {{< ue-val "tr_date" >}}.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Changing the European rules" avis="non" >}}
This page shows what France can decide alone, what it decides within the Union and what the Treaties reserve for the Union's institutions. The book, in French, follows two French preferences all the way to the European rule, one adopted, the other blocked, and compares promises to "change Europe" with what the Treaty allows. It gives no voting advice.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Treaty on the Functioning of the European Union**, consolidated version, Official Journal of the European Union C 202 of 7 June 2016 (EUR-Lex), art. 2 to 6 and the whole Treaty for the legal bases; **Treaty on European Union**, art. 16.

**Council of the European Union**, search of voting results on legislative acts (recorded on {{< ue-val "releve" >}}); public register of documents; General Secretariat of the Council, *Guide to the ordinary legislative procedure*, 2010, annex III (doi 10.2860/74684).

**Ondarza, Nicolai von and Bochtler, Paul**, *Public Voting Data of the Council of the EU*, version 2.0.0, SWP, 2023, doi [10.7802/2560](https://doi.org/10.7802/2560), CC BY 4.0 licence.

**European Commission**, Single Market and Competitiveness Scoreboard, transposition, edition as at {{< ue-val "tr_date" >}}.

The figures, the checks and the chart are produced by a single script, which rereads the Treaty, the SWP dataset and the archived records, and refuses to write if a piece of data stops supporting a sentence. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_europe.csv), long format; [JSON](/promesses_europe.json), with the legal bases, the explained gaps and the report of the checks. This dataset is also archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier for citation: [doi:10.5281/zenodo.23212665](https://doi.org/10.5281/zenodo.23212665).

{{< reutiliser figures="figures_europe" jeu="promesses_europe" sources="TFEU, Council of the EU, SWP / GESIS and European Commission" donnees="The votes against, abstentions and non-participation of each Member State in the Council, the acts on which France did not vote in favour, the TFEU legal bases by decision rule and France's transposition indicators; the same content exists in CSV, long format, readable in a spreadsheet." >}}
What France can decide in the European Union depends on the area: exclusive competence of the Union, shared with the Member States, or mere support, under articles 2 to 6 of the Treaty on the Functioning of the European Union. In the Council, the rule is most often qualified majority, sometimes unanimity. In the public votes of the Council on legislative acts, from {{< ue-val "debut" >}} to {{< ue-val "fin" >}}, France voted against {{< ue-val "fr_contre" >}} and abstained {{< ue-val "fr_abst" >}}; a vote in favour does not say what it obtained or gave up in the negotiation.
{{< /reutiliser >}}
