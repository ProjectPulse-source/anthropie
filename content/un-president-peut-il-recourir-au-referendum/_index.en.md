---
title: "Can the French president call a referendum?"
url: /en/can-the-french-president-call-a-referendum/
description: "Who can put a text to a referendum in France, on which subjects, and what the referendums held so far decided: the {ref.N} national referendums of the Fifth Republic, as at {ref.arrete}, and the {ref.S} bills referred to the Conseil constitutionnel under the shared-initiative referendum. Conseil constitutionnel register, checked against the Journal officiel; open data."
chapo: "The French Constitution allows the president to put a Government Bill to a referendum, under conditions it sets: a recommendation from the Government when Parliament is in session or a joint motion of the two Houses, and a subject it defines. From 4 October 1958 to {ref.arrete}, {ref.N} national referendums were held; the proposed text was approved in {ref.A} and rejected in {ref.R}, and the last one took place on {ref.dernier}. The route opened in 2015 to an initiative of one fifth of the members of Parliament, then subject to the support of one tenth of voters, has not yet led to any vote."
date: 2026-10-06
lastmod: 2026-10-06
# English version of the "Referendum" further topic of the "Presidential promises" dossier (FR:
# content/un-president-peut-il-recourir-au-referendum/_index.md). Same tokens, same keys: values come from the
# affichage_en block of data/promesses_referendum.json (scripts/update_promesses_referendum.py). The Constitution is quoted
# in the English translation published by the Conseil constitutionnel; other French texts in French, with our translation.
donnees: [promesses_referendum]
og_title: "Can the French president call a referendum? The register of referendums of the Fifth Republic and the shared initiative — S. Lalut"
og_image: "images/og-referendum-promesse-en.jpg"
og_image_alt: "Share card: \"Nine national referendums since 4 October 1958\" — timeline of France's national referendums, with the share of 'yes' among valid votes; seven adopted, two rejected (1969 and 2005); none since 29 May 2005, as at 5 October 2026."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_referendum"
  nom: "National referendums of the French Fifth Republic and the shared-initiative referendum: register as at 5 October 2026"
  description: "Register of the national referendums whose results were proclaimed by the Conseil constitutionnel since 1958 (registered voters, voters, valid votes, yes, no, outcome, article of the Constitution), matched vote by vote against the Journal officiel (decree putting the text to the vote, promulgated act); decisions of the Conseil constitutionnel on bills introduced under article 11, paragraph 3 (outcome, condition not met, signatures collected). Source: DILA CONSTIT database, as at {ref.arrete}."
  couverture_temporelle: "1958/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "National referendums: registered voters, voters, valid votes, yes, no", unite: "voters"}
    - {nom: "Bills under article 11: outcome of the Conseil constitutionnel's review, signatures collected", unite: "decisions; voters"}
  sources:
    - "https://echanges.dila.gouv.fr/OPENDATA/CONSTIT/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
    - "https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006071194"
  mots: ["referendum", "France", "article 11", "article 89", "shared-initiative referendum", "Conseil constitutionnel", "Fifth Republic", "promises"]
  fichiers: ["promesses_referendum.csv", "promesses_referendum.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Can the French president hold a referendum whenever he wants?"
    answer: "No, not alone and not on any subject. Under article 11 of the Constitution, he may submit to a referendum a Government Bill, \"{ref.cit_art11_1}\", and only a Bill \"{ref.cit_art11_objet}\". Amendments to the Constitution follow article 89: for a Government Bill to amend the Constitution passed by the two Houses in identical terms, the president chooses between a referendum and Parliament convened in Congress; a Private Member's Bill to amend the Constitution does not have that second route: \"{ref.cit_art89_ref}\""
  - question: "How many referendums have been held under the Fifth Republic?"
    answer: "From 4 October 1958 to {ref.arrete}, {ref.N} national referendums, whose results were proclaimed by the Conseil constitutionnel: the proposed text was approved in {ref.A} and rejected in {ref.R} (in 1969 and 2005). The last one took place on {ref.dernier}. This count excludes the referendum of 28 September 1958, which adopted the Constitution, and local consultations."
  - question: "Has the shared-initiative referendum ever been used?"
    answer: "From {ref.rip_depuis} to {ref.arrete}, the Conseil constitutionnel received {ref.S} bills under article 11; {ref.C} was found to meet the statutory conditions, the one on the Paris airports, and it collected {ref.soutiens} signatures of support, against {ref.seuil} required (one tenth of registered voters). None was put to a referendum."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 60
  prolongement: true
  nature: "Conseil constitutionnel register, checked against the Journal officiel; open data"
onglet:  # "Further topics" panel of the dossier bar (partials/barre-bloc.html)
  long: "Can the French president call a referendum?"
  court: "Referendum"
  role: "register and shared initiative"
---

{{< reutiliser-ancre >}}

Promising to put a reform to the voters means promising to use a route other than a parliamentary vote alone. The French Constitution provides for it: "{{< ref-val "cit_art3" >}}" (art. 3). This page sets out who can put a text to a referendum, on which subjects, and what the votes held so far decided, from the register of the Conseil constitutionnel, which proclaims their results, matched vote by vote against the Journal officiel. No numerical value is entered manually. The Constitution is quoted in the English translation published by the Conseil constitutionnel; other French texts are quoted in French, followed by our translation.

**Short answer.** The president may submit to a referendum a Government Bill, on a recommendation from the Government when Parliament is in session or on a joint motion of the two Houses, and only on the subjects set by article 11; under article 89, a Bill to amend the Constitution first passed by the two Houses in identical terms is submitted to a referendum, unless the president decides to submit it to Parliament convened in Congress. From 4 October 1958 to {{< ref-val "arrete" >}}, {{< ref-val "N" >}} national referendums were held, and none since {{< ref-val "dernier" >}}.

## Who can put a text to a referendum? {#qui-peut}

Two articles of the Constitution open the way, under different conditions.

- **Article 11** allows the president to submit to a referendum a Government Bill, "{{< ref-val "cit_art11_1" >}}". The subject is defined: a Bill "{{< ref-val "cit_art11_objet" >}}".
- **Article 89** governs amendments to the Constitution. A Bill to amend the Constitution passed by the two Houses is in principle submitted to a referendum. "However, {{< ref-val "cit_art89_voies" >}}", where it must obtain a three-fifths majority of the votes cast. A Private Member's Bill to amend the Constitution does not have that second route: "{{< ref-val "cit_art89_ref" >}}"

The act by which the president submits a Bill to a referendum (art. 11) does not need the countersignature of the Prime Minister: it is one of the exceptions of article 19 (see [what the president can decide alone](/en/what-can-the-french-president-decide-alone/)). But he cannot take it without the recommendation or motion that precedes it, and it is the electorate that adopts or rejects the text. The Conseil constitutionnel ensures the proper conduct of the proceedings; under article 60, it "{{< ref-val "cit_art60" >}}".

## How many referendums have been held, and what did they decide? {#registre}

{{< figure-svg fichier="referendum-registre-en" alt="Timeline from 1958 to 2026: one stem per national referendum, its height giving the share of yes among valid votes, filled for an adopted text, hollow for a rejected one; a line marks half of the valid votes; a shaded area covers the years since the last vote, in 2005. The values are in the table below the figure." >}}National referendums whose results were proclaimed by the Conseil constitutionnel, from 4 October 1958 to {{< ref-val "arrete" >}}. Excludes the referendum of 28 September 1958 (adoption of the Constitution, before the Conseil was created) and local consultations.{{< /figure-svg >}}

{{< fig-actions id="registre" >}}

{{< ref-tableau "registre" "The votes in a table" >}}

<div class="resultat-phrase">

**The result in one sentence.** From 4 October 1958 to {{< ref-val "arrete" >}}, {{< ref-val "N" >}} national referendums were held in France; the proposed text was approved in {{< ref-val "A" >}} and rejected in {{< ref-val "R" >}}, and the last one took place on {{< ref-val "dernier" >}}.

</div>

{{< ref-val "n_loi" >}} votes were held under article 11, {{< ref-val "n_rev" >}} under article 89: the five-year presidential term, in 2000. Two Bills put to the vote under article 11 nevertheless concerned the Constitution itself: the 1962 Bill, adopted, which amends its articles 6 and 7 so that the president is elected by direct universal suffrage (Act no. 62-1292 of 6 November 1962), and the 1969 Bill, rejected. This use of article 11 to amend the Constitution was contested: when the President of the Senate referred the 1962 Act to it, the Conseil constitutionnel held that it had no jurisdiction (decision no. 62-20 DC of 6 November 1962); according to the National Assembly, the practice has not been used since the failure of 1969. Turnout ranged from {{< ref-val "part_min" >}}% of registered voters ({{< ref-val "part_min_an" >}}) to {{< ref-val "part_max" >}}% ({{< ref-val "part_max_an" >}}). The two rejected texts were rejected in 1969 (regions and Senate) and in 2005 (Treaty establishing a Constitution for Europe), with {{< ref-val "non_2005" >}}% of valid votes cast for No.

<details class="repli"><summary>What was checked</summary>

**The register.** The decisions of the Conseil constitutionnel are read in the database published by the DILA, the French official publications office (open files, as at {{< ref-val "arrete" >}}). Among the decisions classified "referendum", only the proclamations of results enter the register; the others are appointments of delegates, answers to complaints and observations. For each vote, the numbers of registered voters, voters, valid votes, yes and no are read in the proclamation, and their consistency is checked (yes and no add up to the valid votes; valid votes, voters and registered voters are in order). The percentages on this page are recalculated from these numbers and rounded to the nearest value; the Conseil constitutionnel's summary table gives them truncated, hence differences of one hundredth of a point for some votes.

**The Journal officiel as a cross-check.** Each vote was matched against the Journal officiel: the decree by which the president puts the text to the vote, at the date given by the proclamation, and, for each adopted text, the promulgated act. The {{< ref-val "A" >}} acts exist; no act exists for the {{< ref-val "R" >}} rejected texts. Only one decree was not found in the Légifrance archive, that of 2 October 1962, whose act is published. A title search of the Journal officiel shows no vote missing from the register.

**The limits.** There is no second independent source for the vote counts for 1961-1988: they are checked for consistency, not against another source. The results published by the Ministry of the Interior for 1992, 2000 and 2005 precede the Conseil's corrections: same vote, different definition, so not a cross-check.

</details>

## Has the shared-initiative referendum ever succeeded? {#initiative-partagee}

Since the 2008 constitutional amendment, another route exists, the shared-initiative referendum (*référendum d'initiative partagée*, RIP): a referendum may be held "{{< ref-val "cit_art11_rip" >}}". The bill is referred to the Conseil constitutionnel, which checks that it is signed by one fifth of the members of Parliament, that it concerns a subject of article 11 and that none of its provisions is contrary to the Constitution; if it meets these conditions, signatures of support are collected for nine months. If it gathers its support and the two Houses do not consider it within the set period, article 11 provides that "{{< ref-val "cit_art11_soumet" >}}". The French text reads "la soumet" (literally, "submits it"), whereas the published English translation reads "may submit it". This page notes the difference in wording without taking a position on its legal effect. The procedure has been in force since 1 January {{< ref-val "rip_depuis" >}}.

{{< figure-svg fichier="referendum-rip-en" alt="Four bars in a funnel, each with its number: bills referred to the Conseil constitutionnel, meeting the statutory conditions, having gathered the support of one tenth of registered voters, put to a referendum; below, a gauge shows the signatures collected for the bill on the Paris airports, against the required threshold." >}}Bills introduced under article 11, paragraph 3, referred to the Conseil constitutionnel, from {{< ref-val "rip_depuis" >}} to {{< ref-val "arrete" >}}, and what became of them.{{< /figure-svg >}}

{{< fig-actions id="rip" >}}

<div class="resultat-phrase">

**The result in one sentence.** From {{< ref-val "rip_depuis" >}} to {{< ref-val "arrete" >}}, the Conseil constitutionnel received {{< ref-val "S" >}} bills under article 11; {{< ref-val "C" >}} was found to meet the statutory conditions and did not gather the support of one tenth of registered voters ({{< ref-val "soutiens" >}} signatures for {{< ref-val "seuil" >}} required); none was put to a referendum.

</div>

{{< ref-tableau "rip" "The decisions in a table" >}}

The other {{< ref-val "non_conformes" >}} bills did not meet the statutory conditions, for two reasons that the Conseil names itself. {{< ref-val "cond2_maj" >}} did not concern a subject of article 11: for retirement at 62, for instance, the bill «&nbsp;{{< ref-val "cit_motif_2023_4" >}}&nbsp;» (decision 2023-4 RIP; our translation: does not relate, within the meaning of Article 11 of the Constitution, to a "reform" concerning social policy). {{< ref-val "cond3_maj" >}} contained a provision contrary to the Constitution (2021-2 and 2024-6 RIP). The page does not assess these decisions; it reports their grounds.

**{{< ref-val "depots_sans_saisine_maj" >}} other bills** were tabled «&nbsp;en application de l'article 11&nbsp;» (under article 11) without any decision of the Conseil constitutionnel concerning them in the register consulted: in the Senate, No. 459 (20 April 2018, immigration control); in the National Assembly, No. 1749 (6 March 2019, measures against French jihadists who fought in Iraq and Syria) and No. 5203 (5 April 2022, mistreatment of animals). They bore the signatures of {{< ref-val "depots_auteurs" >}} members of Parliament, whereas article 11 provides for an initiative by one fifth of the members of Parliament. They are therefore not counted among the {{< ref-val "S" >}} referrals. The organic law provides that the bill is forwarded to the Conseil constitutionnel; the sources consulted do not establish what became of these texts.

## What a referendum decides, and what it does not {#ce-qu-il-decide}

A referendum settles the text put to the vote: once adopted, an article 11 Bill becomes an act, which the president promulgates, and an article 89 amendment changes the Constitution. It does not guarantee, on its own, that the text will be implemented, nor the result a promise attaches to it. An act adopted by referendum may require [implementing measures](/en/does-a-law-apply-as-soon-as-it-is-passed/), does not shorten a [ten-year training](/en/can-a-campaign-promise-produce-results-within-five-years/), and does not choose [the indicator](/en/how-can-we-tell-whether-a-promise-was-kept/) that will tell whether the promise was kept. The proclamation says how many ballots read yes and no; it does not say why.

## What happened after the 2005 rejection? {#apres-2005}

On 29 May 2005, the Bill authorising the ratification of the Treaty establishing a Constitution for Europe was rejected. The Treaty of Lisbon, signed afterwards, is a different treaty: as its title says ("Treaty of Lisbon amending the Treaty on European Union and the Treaty establishing the European Community"), it amends the existing treaties. It was referred to the Conseil constitutionnel, which held that the authorisation to ratify it «&nbsp;{{< ref-val "cit_2007_560" >}}&nbsp;» (decision No. 2007-560 DC of 20 December 2007; our translation: can take place only after the Constitution has been amended). On 4 February 2008, Parliament convened in Congress adopted the Bill amending Title XV of the Constitution, under the conditions of article 89 ([Congress vote](https://www.assemblee-nationale.fr/13/scrutins/jo9000.asp)); this is Act No. 2008-103 of the same day, amending the Constitution. The ratification of the Treaty of Lisbon was then authorised by act No. 2008-125 of 13 February 2008. No referendum was held in 2008. The page keeps to this sequence of acts.

## What this page does not say {#limites}

It does not say whether the referendum is a good or a bad instrument, nor why none has been held since 2005: no source establishes it, and an intention cannot be read in an act. It counts neither the referendum of 28 September 1958, before the Conseil constitutionnel existed, nor local consultations (New Caledonia, Corsica, overseas territories), proclaimed by other authorities. It examines the Constitution as currently in force, without legal doctrine or case law beyond the decisions cited. The register stands as at {{< ref-val "arrete" >}}.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="What a vote decides" avis="non" >}}
This page shows that a referendum settles a text, not what follows from it. The book, in French, follows nine written, dated and signed promises to their last obstacle, and its closing chapter is devoted to the 2005 referendum and what became of it. It gives no voting advice.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Constitution** of 4 October 1958, art. 3, 11, 60 and 89, text in force (Légifrance; English translation published by the Conseil constitutionnel). **Ordinance** No. 58-1067 of 7 November 1958, art. 45-1 and 45-2; **institutional act** No. 2013-1114 of 6 December 2013 implementing article 11.

**Conseil constitutionnel**, proclamations of referendum results (decisions 61-4, 62-7, 62-9, 69-10, 72-11, 88-14, 92-19, 2000-29, 2005-38) and decisions on bills under article 11 (2019-1 and 2019-1-8, 2021-2, 2022-3, 2023-4, 2023-5, 2024-6, 2026-7 RIP), read in the CONSTIT database published by the DILA, as at {{< ref-val "arrete" >}}; decision No. 2007-560 DC.

**Journal officiel** (Légifrance), decrees putting texts to a referendum and acts adopted by referendum; **National Assembly**, open data of the 15th to 17th legislatures (bills under article 11), and Congress vote of 4 February 2008.

The figures, the checks and the charts are produced by a single script, which rereads the archived decisions and articles and refuses to write if a piece of data stops supporting a sentence; no figure on this page is typed by hand. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_referendum.csv), long format; [JSON](/promesses_referendum.json), with the identifiers of the decisions and the report of the checks. This dataset is also archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier for citation: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_referendum" jeu="promesses_referendum" sources="Conseil constitutionnel and Journal officiel" donnees="The register of national referendums (registered voters, voters, valid votes, yes, no, article, outcome), the decisions on the shared-initiative referendum and the bills with no decision; the same content exists in CSV, long format, readable in a spreadsheet." >}}
A French president may put a Government Bill to a referendum, on a recommendation from the Government when Parliament is in session or on a joint motion of the two Houses, and on the subjects set by article 11 of the Constitution. From 4 October 1958 to {{< ref-val "arrete" >}}, {{< ref-val "N" >}} national referendums were held; the proposed text was approved in {{< ref-val "A" >}} and rejected in {{< ref-val "R" >}}, and the last one took place on {{< ref-val "dernier" >}}. The shared-initiative referendum, open since {{< ref-val "rip_depuis" >}}, has not yet led to any vote.
{{< /reutiliser >}}
