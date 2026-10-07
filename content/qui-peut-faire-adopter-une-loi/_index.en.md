---
title: "Who can get a law passed in France?"
url: /en/who-can-get-a-law-passed-in-france/
description: "Parliament passes statutes, but who initiates them, how many private members' bills are debated in plenary, and what does article 49.3 change? The origin of the laws promulgated in France under the last three complete legislatures, matched law by law between the National Assembly, the Senate and the Journal officiel, the fate of private members' bills, and the uses of article 49, paragraph 3. Open data."
chapo: "Parliament passes statutes, and both the Prime Minister and Members of Parliament can initiate them. Excluding finance acts, social security financing acts, institutional acts and treaties, {ado.P14} of the {ado.N14} laws promulgated during the 14th legislature (2012-2017; a legislature is the term of the National Assembly) originated as private members' bills, {ado.P15} out of {ado.N15} during the 15th and {ado.P16} out of {ado.N16} during the 16th. This origin says who tabled the text, not who shaped it, nor which tabled texts failed: in each of these legislatures, more than half of the ordinary private members' bills tabled in the National Assembly had no observed plenary debate before it ended. The ordinary procedure involves both Houses; in the National Assembly, article 49, paragraph 3 also allows the Government to make the passing of a bill an issue of a vote of confidence, so that the bill is considered passed at that stage unless it is censured."
date: 2026-10-06
lastmod: 2026-10-06
# English version of tab 2 of the "Presidential promises" dossier (FR: content/qui-peut-faire-adopter-une-loi/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_adopter.json
# (scripts/update_promesses_adopter.py), whose guards cover both languages. The Constitution is quoted in the English
# translation published by the Conseil constitutionnel, checked word for word; other French texts are quoted in French,
# followed by our translation.
donnees: [promesses_adopter]
og_title: "Who can get a law passed in France? The origin of laws, bills never debated in plenary, and article 49.3 — S. Lalut"
og_image: "images/og-adopter-promesse-en.jpg"
og_image_alt: "Share card: who initiated the laws promulgated in France in the scope studied, by legislature, from the 14th to the 16th: government bills, private members' bills tabled in the National Assembly and in the Senate."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_adopter"
  nom: "Origin of the laws promulgated in France from 2012 to 2026, private members' bills tabled in the National Assembly, and uses of article 49, paragraph 3"
  description: "Formal origin at the initial tabling (government bill, private member's bill tabled in the National Assembly or in the Senate) of the laws promulgated from the 14th to the 17th legislature, excluding treaties, finance acts, social security financing acts and institutional acts, matched law by law between National Assembly data, the Senate's Dosleg database and the Journal officiel; ordinary private members' bills tabled in the National Assembly with no observed plenary debate before the end of the legislature, with the worst-case bound against the statistical bulletins; uses of article 49, paragraph 3 by legislature."
  couverture_temporelle: "2012/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Laws promulgated by origin", unite: "laws"}
    - {nom: "Private members' bills tabled and not debated in the chamber", unite: "bills"}
    - {nom: "Uses of article 49, paragraph 3", unite: "uses"}
  sources:
    - "https://data.assemblee-nationale.fr/"
    - "https://data.senat.fr/dosleg/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
  mots: ["French Parliament", "private member's bill", "government bill", "article 49.3", "article 45", "National Assembly", "Senate", "France", "political promises"]
  fichiers: ["promesses_adopter.csv", "promesses_adopter.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Who can propose a law in France?"
    answer: "Under article 39 of the Constitution, \"{ado.cit_art39}\" (English translation published by the Conseil constitutionnel). A text from the Government is a government bill (projet de loi); one from a deputy or a senator is a private member's bill (proposition de loi). Excluding finance acts, social security financing acts, institutional acts and treaties, {ado.P16} of the {ado.N16} laws promulgated during the 16th legislature arose from a private member's bill, {ado.G16} from a government bill."
  - question: "Among the laws promulgated, what share comes from a government bill?"
    answer: "It varies with the legislature. In the scope studied (excluding treaties, finance acts, social security financing acts and institutional acts), {ado.G14} of the {ado.N14} laws promulgated came from a government bill during the 14th legislature, {ado.G15} out of {ado.N15} during the 15th and {ado.G16} out of {ado.N16} during the 16th. This is the origin at the tabling of the text: it does not measure the Government's influence on a private member's bill, nor Parliament's amendments to a government bill."
  - question: "How many private members' bills are debated in plenary?"
    answer: "Fewer than half. During the 14th legislature, {ado.Z14} of the {ado.NZ14} ordinary private members' bills tabled in the National Assembly had no observed plenary debate before the end of the legislature; {ado.Z15} out of {ado.NZ15} during the 15th; {ado.Z16} out of {ado.NZ16} during the 16th. These counts slightly exceed those of the Assembly's bulletins; even with the whole excess removed, more than half remain undebated in each legislature."
  - question: "How many times has article 49.3 been used?"
    answer: "The Government made the passing of a bill an issue of a vote of confidence {ado.E14} times during the 14th legislature, on {ado.Etextes14} bills, {ado.Efois15} during the 15th and {ado.E16} times during the 16th, {ado.Efin16} of them on a Finance Bill or Social Security Financing Bill, counting one use per bill and per reading stage. No motion of no confidence was carried on these uses; during the 17th legislature, one was carried after the use on {ado.censure_date}."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 20
  nature: "National Assembly, Senate and Journal officiel data, matched law by law; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "Who can get a law passed in France?"
  court: "Pass"
  role: "initiative, vote and 49.3"
---

{{< reutiliser-ancre >}}

A promise that requires a law has to clear the parliamentary stage. The Constitution says it in one sentence: "{{< ado-val "cit_art24" >}}" (art. 24). It shares the right of initiative: "{{< ado-val "cit_art39" >}}" (art. 39). This page counts, law by law, who tabled the laws promulgated in France since 2012, how many private members' bills are debated in plenary, and how many times the Government has made the passing of a bill an issue of a vote of confidence under article 49, paragraph 3. All the figures come from the public data of the National Assembly, the Senate and the Journal officiel, matched law by law, and none is entered by hand. The Constitution is quoted in the English translation published by the Conseil constitutionnel.

**Short answer.** Parliament passes statutes, but the text passed may come from the Government or from a member of Parliament. Excluding finance acts, social security financing acts, institutional acts and treaties, {{< ado-val "P16" >}} of the {{< ado-val "N16" >}} laws promulgated during the 16th legislature arose from a private member's bill. But more than half of the private members' bills tabled in the National Assembly have no observed plenary debate before the end of the legislature. And the Government can make the passing of a bill an issue of a vote of confidence: at that stage, the bill is then considered passed, unless a motion of no confidence is carried.

## Who initiated the laws promulgated? {#origine-des-lois}

{{< figure-svg fichier="adopter-origine-en" alt="Horizontal bars by legislature, from the 14th to the ongoing 17th: laws arising from a government bill, from a private member's bill tabled in the National Assembly, from one tabled in the Senate; a mark shows half of the laws. The share of parliamentary origin is below half for the 14th and above for the following ones. The values are in the table below the figure." >}}Laws promulgated, assigned to the legislature of their promulgation, by the origin of the text at its initial tabling. Scope studied: excluding laws authorising a treaty, finance acts, social security financing acts and institutional acts.{{< /figure-svg >}}

{{< fig-actions id="origine" >}}

{{< ado-tableau "lois" "The figure's values in a table" >}}

<div class="resultat-phrase">

**The finding in one sentence.** Excluding finance acts, social security financing acts, institutional acts and treaties, {{< ado-val "P14" >}} of the {{< ado-val "N14" >}} laws promulgated during the 14th legislature originated as private members' bills, {{< ado-val "P15" >}} out of {{< ado-val "N15" >}} during the 15th and {{< ado-val "P16" >}} out of {{< ado-val "N16" >}} during the 16th.

</div>

The share of parliamentary origin is below half during the 14th legislature and above half during the 15th and the 16th, even counting, for the 15th, only the {{< ado-val "Pmin15" >}} laws whose origin is established by both sources. These proportions describe the laws finally promulgated; they do not measure the fate of the texts tabled, which the next section examines. Finance acts and social security financing acts, outside the scope, all come from a government bill.

**What origin does not tell.** It says who tabled the text, not who wanted it nor what became of it. A private member's bill may be supported, amended or rewritten at the Government's request; a government bill may be deeply changed by Parliament. Texts tabled but not passed are absent from this count. None of these series measures such influences.

<details class="repli"><summary>What was checked, and how</summary>

Each law promulgated since June 2012 is matched, by its number in the Journal officiel, between the National Assembly's open data and the Senate's Dosleg database. When both sources know a law, they give the same origin for all laws. Some laws of the 14th and 15th legislatures are missing from the Assembly's files, because their file was opened under the previous legislature: their origin rests on the Senate alone, hence the "at least" bound in the table.

Two checks come from elsewhere. Session by session, from 2017-2018 to 2024-2025, the number of laws promulgated excluding treaties is exactly the one counted by the barometer of the application of laws, published by the National Assembly from DILA data. And the Senate writes, for 2024-2025: «&nbsp;{{< ado-val "cit_senat_origine" >}}&nbsp;» [our translation: "{{< ado-val "cit_senat_origine_tr" >}}"]; the law-by-law count gives {{< ado-val "s2425_P" >}} laws of parliamentary origin out of {{< ado-val "s2425_N" >}}.

{{< ado-tableau "sessions" "By session, all kinds except treaties" >}}

</details>

## How many private members' bills are debated in plenary? {#propositions-en-seance}

Fewer than half. During the 14th legislature, {{< ado-val "Z14" >}} of the {{< ado-val "NZ14" >}} ordinary private members' bills tabled first in the National Assembly had no observed plenary debate before the end of the legislature; {{< ado-val "Z15" >}} out of {{< ado-val "NZ15" >}} during the 15th; {{< ado-val "Z16" >}} out of {{< ado-val "NZ16" >}} during the 16th.

{{< ado-tableau "e1" "The values in a table, with the worst-case bound" >}}

These figures count the bills tabled in the Assembly's open data. Its statistical bulletins count slightly fewer: {{< ado-val "exces14" >}}, {{< ado-val "exces15" >}} and {{< ado-val "exces16" >}} fewer private members' bills depending on the legislature, with no list that would identify the texts concerned. Even removing this whole excess both from the total and from the bills not debated, more than half of the ordinary private members' bills tabled have no observed plenary debate before the end of the legislature, in each of the three legislatures: {{< ado-val "Zw14" >}} out of {{< ado-val "Nw14" >}}, {{< ado-val "Zw15" >}} out of {{< ado-val "Nw15" >}}, {{< ado-val "Zw16" >}} out of {{< ado-val "Nw16" >}}.

A bill that is not debated is not necessarily lost: its content may be taken up in another text, or in an amendment. And these fractions do not compare from one legislature to the next like rates: the 16th, cut short by the dissolution, left texts less than half as much time to be considered (median time from tabling to the end of the legislature: {{< ado-val "med16" >}} days, against {{< ado-val "med14" >}} during the 14th).

## How is a law passed under the ordinary procedure? {#voie-ordinaire}

"{{< ado-val "cit_art45a" >}}" (Constitution, art. 45). Where the two Houses persistently disagree, the Prime Minister or, for a private member's bill, the Presidents of the two Houses acting jointly "{{< ado-val "cit_art45b" >}}" If that agreement fails, "{{< ado-val "cit_art45c" >}}"

The right of initiative does not exhaust the procedural levers: under article 48, "{{< ado-val "cit_art48" >}}" This priority on the agenda does not guarantee that a text will be passed.

## What does article 49, paragraph 3 change? {#article-49-3}

It allows the Government to make the passing of a bill an issue of a vote of confidence before the National Assembly. Under article 49 of the Constitution, "{{< ado-val "cit_art49a" >}}" Beyond those texts, "{{< ado-val "cit_art49b" >}}" The bill is not voted on at that stage: it is considered passed, unless a motion of no confidence is carried. This count covers all texts, finance acts included, which the count of the origin of laws leaves aside.

{{< figure-svg fichier="adopter-493-en" alt="Horizontal bars by legislature: uses of article 49, paragraph 3 on a Finance Bill or Social Security Financing Bill, and on another bill. Those of the 14th and 15th concern other bills; those of the 16th mostly concern Finance Bills or Social Security Financing Bills. The values are in the table below the figure." >}}Uses of article 49, paragraph 3 by the Government, one per bill and per reading stage, by the categories of that paragraph: the public finance programming act falls under "one other bill".{{< /figure-svg >}}

{{< fig-actions id="493" >}}

{{< ado-tableau "engagements" "The figure's values in a table" >}}

During the 14th legislature, the Government used this procedure {{< ado-val "E14" >}} times, on {{< ado-val "Etextes14" >}} bills that were neither Finance Bills nor Social Security Financing Bills; during the 15th, {{< ado-val "Efois15" >}}; during the 16th, {{< ado-val "E16" >}} times, {{< ado-val "Efin16" >}} of them on Finance Bills or Social Security Financing Bills and {{< ado-val "Eautre16" >}} on the public finance programming act. The National Assembly's summary sheet on this procedure gives the same totals: «&nbsp;{{< ado-val "cit_fiche64" >}}&nbsp;» [our translation: "{{< ado-val "cit_fiche64_tr" >}}"]. These numbers describe the kind of bills on which the procedure was used; they do not explain why its use differs from one legislature to another.

No motion of no confidence was carried on these uses, from the 14th to the 16th legislature. During the 17th, after the use on {{< ado-val "censure_date" >}}, «&nbsp;{{< ado-val "cit_censure" >}}&nbsp;» [our translation: "{{< ado-val "cit_censure_tr" >}}"] (same sheet): the bill was not considered passed under article 49, paragraph 3, at that stage.

<details class="repli"><summary>What was checked, and how</summary>

The uses are read in the National Assembly's legislative files, and counted twice by two different routes of the same producer, with the same dates. They are compared, session by session, with the Assembly's statistical bulletins: same numbers of uses and of motions. A single date differs, by one day, for a use in November 2022; the official record of the sitting confirms the date in the data. For a few motions, the data do not contain the vote; the bulletins give their ballots, all below the required majority.

</details>

## What this page does not say {#limites}

It does not measure the Government's influence on private members' bills, nor Parliament's on government bills: the origin of a law is not its content, and amendments are not counted. It does not link the number of uses of article 49.3 to the composition of the Assembly: a coincidence in time does not establish a link. It does not say what becomes of the bills that are not debated, nor whether their content was taken up elsewhere. The counts of bills tabled do not match the Assembly's bulletins text by text: the sentence on private members' bills rests only on the worst-case bound.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="What has to be voted" avis="non" >}}
This page shows who tables laws, how many private members' bills are debated in plenary and what article 49.3 allows. The book follows nine written, dated and signed promises along the chain that runs from the decision to its outcome: what a president decides within his own chain of power, what he has to get voted, what he has to negotiate, and what will never depend on him. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**National Assembly**, open data on the legislative files of the 14th to 17th legislatures (version of {{< ado-val "releve" >}}); annual statistical bulletins; summary sheet no. 64 on the Government's responsibility (in French).

**Senate**, Dosleg database (version of {{< ado-val "releve" >}}); information report no. 802 (2025-2026) on the application of laws, p. 44 (in French).

**Journal officiel**, DILA data; **Constitution**, arts. 24, 39, 45, 48 and 49, read on Légifrance (API) in French and quoted in the English translation published by the Conseil constitutionnel.

The figures, quotations, checks and charts are produced by a single script; each quotation is checked word for word in its document, and no figure on this page is entered by hand. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_adopter.csv), long format; [JSON](/promesses_adopter.json), with definitions and the record of the checks (field names and some labels in French). This dataset is also archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier for citation: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_adopter" jeu="promesses_adopter" sources="National Assembly, Senate (Dosleg), Journal officiel, Conseil constitutionnel" donnees="The origin of the laws promulgated by legislature and by session, the private members' bills tabled in the National Assembly and not debated in the chamber, and the uses of article 49, paragraph 3; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
In the scope studied (excluding treaties, finance, social security financing and institutional acts), {{< ado-val "P14" >}} of the {{< ado-val "N14" >}} laws promulgated in France during the 14th legislature originated as private members' bills, {{< ado-val "P15" >}} out of {{< ado-val "N15" >}} during the 15th and {{< ado-val "P16" >}} out of {{< ado-val "N16" >}} during the 16th; this is the origin at tabling, not influence. More than half of the ordinary private members' bills tabled in the National Assembly have no observed plenary debate before the end of the legislature, even on the worst-case bound. The Government made the passing of a bill an issue of a vote of confidence {{< ado-val "E16" >}} times during the 16th legislature, {{< ado-val "Efin16" >}} of them on Finance Bills or Social Security Financing Bills.
{{< /reutiliser >}}
