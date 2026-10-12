---
title: "Who can get a law passed in France?"
url: /en/who-can-get-a-law-passed-in-france/
description: "Tabling a bill, bringing it to the floor, having the final say: the French Constitution shares these keys between the Government, members of Parliament and the two Houses. It gives Parliament the passing of statutes, and three situations must be distinguished (article 49.3, budget ordinances, referendum). The origin of the laws promulgated since 2012, matched law by law between the National Assembly, the Senate and the Journal officiel, the fate of private members' bills, and the uses of article 49, paragraph 3. Open data."
chapo: "Do laws mostly come from the Government? Since the 15th legislature (2017-2022; a legislature is the term of the National Assembly), most ordinary laws promulgated in France, excluding treaties, have arisen from a bill tabled by a deputy or a senator; for the 15th, narrowly (at least {ado.Pmin15} laws out of {ado.N15}). This result depends on what is counted: adding the laws with a procedure of their own (the State and social security budgets, laws that supplement or amend the Constitution), the parliamentary majority only appears with the 16th (2022-2024). Yet about {ado.Zdix} in ten private members' bills tabled in the National Assembly were not debated in plenary before their legislature ended. The two findings fit together because getting a law passed takes several keys, which the Constitution shares out: the Prime Minister and members of Parliament can table bills, but the Government has priorities on the agenda and alone can ask the National Assembly to reach a final decision. The passing of statutes belongs to Parliament, and three situations must be distinguished: the passing of a bill at one stage without the National Assembly voting on it (article 49, paragraph 3), the bringing into force of budget provisions by ordinance without a statute passed by vote (articles 47 and 47-1), and the passing of a law by referendum (article 11)."
date: 2026-10-06
lastmod: 2026-10-12
# English version of tab 2 of the "Presidential promises" dossier (FR: content/qui-peut-faire-adopter-une-loi/_index.md).
# Same tokens, same keys: values come from the affichage_en block of data/promesses_adopter.json
# (scripts/update_promesses_adopter.py), whose guards cover both languages. The Constitution is quoted in the English
# translation published by the Conseil constitutionnel, checked word for word; other French texts are quoted in French,
# followed by our translation.
donnees: [promesses_adopter]
og_title: "Who can get a law passed in France? The origin of laws, bills never debated in plenary, the agenda and article 49.3 — S. Lalut"
og_image: "images/og-adopter-promesse-en.jpg"
og_image_alt: "Share card: who initiated the laws promulgated in France? Ordinary laws, by legislature, from the 14th to the 17th (ongoing on 6 October 2026): government bills, private members' bills tabled in the National Assembly and in the Senate."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_adopter"
  nom: "Origin of the laws promulgated in France from 2012 to 2026, private members' bills tabled in the National Assembly, and uses of article 49, paragraph 3"
  description: "Formal origin at the initial tabling (government bill, private member's bill tabled in the National Assembly or in the Senate) of the laws promulgated from the 14th to the 17th legislature, matched law by law between National Assembly data, the Senate's Dosleg database and the Journal officiel: ordinary laws (excluding treaties, finance acts, social security financing acts, institutional and constitutional acts), all kinds except treaties, and laws promulgated between two legislatures; ordinary private members' bills tabled in the National Assembly with no plenary debate before the end of the legislature, with the worst-case bound against the statistical bulletins; uses of article 49, paragraph 3 by legislature, and the finance acts promulgated after at least one use."
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
  mots: ["French Parliament", "private member's bill", "government bill", "parliamentary agenda", "article 49.3", "article 45", "National Assembly", "Senate", "France", "political promises"]
  fichiers: ["promesses_adopter.csv", "promesses_adopter.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Who can propose a law in France?"
    answer: "Under article 39 of the Constitution, \"{ado.cit_art39}\" (English translation published by the Conseil constitutionnel). A text from the Government is a government bill (projet de loi); one from a deputy or a senator is a private member's bill (proposition de loi). In the scope studied ({ado.champ}), {ado.P16} of the {ado.N16} laws promulgated during the 16th legislature arose from a private member's bill, {ado.G16} from a government bill. A private member's bill is, however, not admissible if it creates or increases public expenditure, nor if it reduces public revenue without offsetting the loss by another revenue (article 40, as the National Assembly applies it)."
  - question: "Can a law be passed in France without Parliament voting on its text?"
    answer: "Three situations must be distinguished: making the passing of a bill an issue of a vote of confidence, which has the bill considered passed at one stage without the deputies voting on it, unless a motion of no confidence is carried (articles 49, paragraph 3, and 50); bringing a budget into force by ordinance if Parliament has not reached a decision within the time limits, without a statute passed by vote (articles 47 and 47-1); passing a law by referendum (article 11)."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 20
  refonte: "2026-10-12"
  nature: "National Assembly, Senate and Journal officiel data, matched law by law; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "Who can get a law passed in France?"
  court: "Pass"
  role: "tabling, floor, final say, 49.3"
---

{{< reutiliser-ancre >}}

The Constitution gives Parliament the passing of statutes: "{{< ado-val "cit_art24" >}}" (art. 24). Three situations stand apart from it. When the Prime Minister makes a bill an issue of a vote of confidence, the bill is considered passed at that stage, unless a motion of no confidence is carried (art. 49, para. 3). If Parliament has not reached a decision within the time limits, the provisions of a Finance Bill or Social Security Financing Bill (the State budget or the social security budget) may be brought into force by ordinance, without becoming a statute passed by vote (arts. 47 and 47-1). Lastly, a law may be passed by referendum (art. 11). This page follows the route almost every law takes, through Parliament: who tabled, law by law, the laws promulgated in France since 2012, what became of the private members' bills tabled in the National Assembly, how many times article 49, paragraph 3 was used. The Constitution is quoted in the English translation published by the Conseil constitutionnel.

**Short answer.** Getting a law passed takes four keys. Tabling: "{{< ado-val "cit_art39" >}}" (art. 39). Reaching the floor: each House sets its agenda, but the Government has priorities in it (art. 48). Concluding: the two Houses must agree on an identical text or, failing that, the National Assembly has the final say, which only the Government can ask it to exercise (art. 45). And the Prime Minister can make the passing of a bill an issue of a vote of confidence, at the risk of a no-confidence vote (arts. 49 and 50). So the Government does not get laws passed on its own, and members of Parliament, who have tabled most of the laws promulgated since 2017 in the scope studied, do not hold the other keys on their own.

## Who initiated the laws promulgated? {#origine-des-lois}

Do laws mostly come from the Government? The origin of each law promulgated, at the tabling of the text, makes it possible to check. A text from the Government is a government bill; one from a deputy or a senator, a private member's bill. The count covers ordinary laws, those that follow the common procedure. It leaves aside the laws with a procedure or an origin of their own: {{< ado-val "champ_def" >}}.

{{< figure-svg fichier="adopter-origine-en" alt="100% bars by legislature, from the 14th to the ongoing 17th: share of the laws arising from a private member's bill tabled in the National Assembly, from one tabled in the Senate, from a Government bill; a dotted line marks half, a triangle the lower bound where the origin of some laws rests on a single source. The share of parliamentary origin is below half for the 14th and above for the following ones; on the right, the share for all kinds except treaties. The values are in the table below the figure." >}}Laws promulgated, assigned to the legislature of their promulgation, by the origin of the text at its initial tabling. Scope studied: ordinary laws, {{< ado-val "champ" >}}.{{< /figure-svg >}}

{{< fig-actions id="origine" >}}

{{< ado-tableau "lois" "The figure's values in a table" >}}

<div class="resultat-phrase">

**The finding in one sentence.** In the scope studied, the share of the laws promulgated that arose from a private member's bill is {{< ado-val "Ppct14" >}}% during the 14th legislature (2012-2017), then above half: {{< ado-val "Ppct15" >}}% during the 15th (at least {{< ado-val "Pminpct15" >}}%), {{< ado-val "Ppct16" >}}% during the 16th and {{< ado-val "Ppct17" >}}% during the 17th, ongoing on {{< ado-val "releve" >}}.

</div>

**What origin does not tell.** It says who tabled the text, not who wanted it nor what became of it. A private member's bill may have been prepared with a ministry or supported by the Government; a government bill may be deeply changed by Parliament. The rising share of private members' bills therefore does not measure growing autonomy of members of Parliament: none of these series observes such influences.

**Does the scope change the answer?** For the 15th legislature, yes. During the 15th, {{< ado-val "Ppct15" >}}% of the laws in the scope studied are of parliamentary origin, but only {{< ado-val "Ptotpct15" >}}% counting all kinds except treaties ({{< ado-val "Ptot15" >}} laws out of {{< ado-val "Ntot15" >}}). This second count puts finance, institutional and constitutional acts back in; it also gives {{< ado-val "Ptotpct14" >}}% during the 14th, {{< ado-val "Ptotpct16" >}}% during the 16th and {{< ado-val "Ptotpct17" >}}% during the 17th. **The parliamentary majority of the 15th therefore depends on the scope chosen.** That of the 16th and 17th does not.

These laws are left out of the main count because their origin or procedure is set apart. Articles 47 and 47-1 of the Constitution speak only of Finance Bills and Social Security Financing Bills, and all these acts come here from a government bill. Institutional acts follow their own rules (art. 46): failing agreement between the two Houses, the National Assembly may pass them on a final reading only by an absolute majority of its members, and those relating to the Senate must be passed in identical terms by the two Houses. Laws authorising a treaty, all from a government bill, are counted nowhere.

<details class="repli"><summary>The wording of article 46</summary>

Article 46: "{{< ado-val "cit_art46c" >}}" And: "{{< ado-val "cit_art46d" >}}"

</details>

{{< ado-tableau "natures" "All kinds except treaties, by legislature" >}}

Lastly, {{< ado-val "HLn" >}} laws promulgated in {{< ado-val "HLmois" >}}, after the dissolution of the Assembly and before the 17th legislature, belong to no legislature: they have their own row in the table, and all of them originated as private members' bills.

<details class="repli"><summary>What was checked, and how</summary>

Each law promulgated since June 2012 is matched, by its number in the Journal officiel, between the National Assembly's open data and the Senate's Dosleg database. When both sources know a law, they give the same origin for all laws. Some laws of the 14th and 15th legislatures are missing from the Assembly's files, because their file was opened under the previous legislature: their origin rests on the Senate alone, hence the "at least" bound in the table and the triangle in the figure.

Two checks come from elsewhere. Session by session, from 2017-2018 to 2024-2025, the number of laws promulgated excluding treaties is exactly the one counted by the barometer of the application of laws, published by the National Assembly from DILA data. And the Senate writes, for 2024-2025: «&nbsp;{{< ado-val "cit_senat_origine" >}}&nbsp;» [our translation: "{{< ado-val "cit_senat_origine_tr" >}}"]; the law-by-law count gives {{< ado-val "s2425_P" >}} laws of parliamentary origin out of {{< ado-val "s2425_N" >}}. For 2023-2024, it gives {{< ado-val "s2324_P" >}} out of {{< ado-val "s2324_N" >}}, or {{< ado-val "s2324_pct" >}}%, which the table rounds to {{< ado-val "s2324_arr" >}}%; the Senate, quoted above, gives the whole number below. The Senate speaks of laws adopted, this count of laws promulgated: the two counts coincide for 2024-2025.

{{< ado-tableau "sessions" "By session, all kinds except treaties" >}}

</details>

## How many private members' bills are debated in plenary? {#propositions-en-seance}

Few. In each of the three completed legislatures, about {{< ado-val "Zdix" >}} in ten ordinary private members' bills tabled first in the National Assembly had not been debated in plenary by the end of the legislature, according to the Assembly's data: {{< ado-val "Z14" >}} out of {{< ado-val "NZ14" >}} during the 14th ({{< ado-val "Zpct14" >}}%), {{< ado-val "Z15" >}} out of {{< ado-val "NZ15" >}} during the 15th ({{< ado-val "Zpct15" >}}%), {{< ado-val "Z16" >}} out of {{< ado-val "NZ16" >}} during the 16th ({{< ado-val "Zpct16" >}}%). The ongoing 17th is not counted.

A bill that was not debated in plenary has been neither rejected nor barred, and its content has not necessarily disappeared: it may be taken up in another text, or in an amendment. Nor do these fractions compare from one legislature to the next like rates: the 16th, cut short by the dissolution, left texts less than half as much time to be considered (median time from tabling to the end of the legislature: {{< ado-val "med16" >}} days, against {{< ado-val "med14" >}} during the 14th).

<details class="repli"><summary>The worst case: bills the Assembly's bulletins do not count</summary>

These figures count the bills tabled in the Assembly's open data. Its statistical bulletins count slightly fewer: {{< ado-val "exces14" >}}, {{< ado-val "exces15" >}} and {{< ado-val "exces16" >}} fewer private members' bills depending on the legislature, with no list that would identify the texts concerned. Removing this whole excess both from the total and from the bills not debated leaves {{< ado-val "Zw14" >}} out of {{< ado-val "Nw14" >}}, {{< ado-val "Zw15" >}} out of {{< ado-val "Nw15" >}} and {{< ado-val "Zw16" >}} out of {{< ado-val "Nw16" >}}: still about {{< ado-val "Zdix" >}} in ten.

{{< ado-tableau "e1" "The values in a table, with the worst-case bound" >}}

</details>

**How do the two findings fit together?** They do not contradict each other, because they do not bear on the same texts. The first starts from the laws promulgated, Senate bills included, assigned to the legislature of their promulgation; the second from the private members' bills tabled in the Assembly, assigned to the legislature of their tabling. A small share of private members' bills that succeed can supply most of the laws promulgated, because private members' bills far outnumber government bills: according to the Assembly's bulletins, {{< ado-val "bul14" >}} private members' bills were tabled there on first reading during the 14th legislature, against {{< ado-val "pjl14" >}} government bills, and the gap exceeds a factor of five in each of the three completed legislatures.

| What these measures establish | What they do not establish |
|---|---|
| Who tabled each law promulgated, at the initial tabling | Who wanted or drafted the text, or what amendments made of it |
| That most private members' bills tabled in the Assembly were not debated in plenary before their legislature ended | Why: no data links this fate to an agenda decision, or to article 40 |
| The number of uses of article 49.3 and the bills concerned | The content of the resulting laws, or what a vote would have produced |

## Who decides what reaches the floor? {#ordre-du-jour}

Each House, first: under article 48, "{{< ado-val "cit_art48a" >}}" The same article reserves two sitting weeks out of four for the Government, for the texts and debates it asks to have placed on the agenda, in the order it sets. It also gives it priority, at its request, for certain texts, including the State and social security budget bills. And it guarantees one sitting day a month to opposition and minority groups.

The agenda is therefore shared, and priority on the agenda does not guarantee that a text will be passed. Another rule limits what members of Parliament can propose: their bills and amendments are not admissible where their enactment would reduce public revenue, or create or increase public expenditure (art. 40). The National Assembly allows no offset for expenditure, but allows a loss of revenue offset by another revenue (the "gage"). The data on this page do not say which of these filters set aside a given bill: they contain neither the decisions to place bills on the agenda nor the rulings of inadmissibility.

<details class="repli"><summary>The wording of articles 48 and 40</summary>

Article 48, paragraph 2: "{{< ado-val "cit_art48" >}}" Paragraph 3: "{{< ado-val "cit_art48c" >}}" Paragraph 5: "{{< ado-val "cit_art48e" >}}"

Article 40: "{{< ado-val "cit_art40" >}}"

According to the National Assembly's summary sheet no. 52 (September 2023), on "public revenue", in the plural: «&nbsp;{{< ado-val "cit_fiche52" >}}&nbsp;» [our translation: "{{< ado-val "cit_fiche52_tr" >}}"]. On "public expenditure", in the singular ("une charge publique" in the French text): «&nbsp;{{< ado-val "cit_fiche52b" >}}&nbsp;» [our translation: "{{< ado-val "cit_fiche52b_tr" >}}"].

</details>

## Who has the final say between the two Houses? {#voie-ordinaire}

The principle is agreement: "{{< ado-val "cit_art45a" >}}" (Constitution, art. 45). When agreement does not come, article 45 sets a sequence, and each step has its actor.

1. A joint committee, with equal numbers of deputies and senators, may be convened to propose a text on the provisions still under debate. It may be convened after two readings in each House, or after a single one if the Government has applied the accelerated procedure without the Conferences of Presidents of the two Houses being jointly opposed. Convening it falls to the Prime Minister or, for a private member's bill, to the Presidents of the two Houses acting jointly.
2. The committee's text goes through the Government: it is the Government that may submit it to both Houses, and no amendment to it is admissible without its consent.
3. If that fails, the final say of the National Assembly can only come from the Government: if the committee fails to agree on a common text, or if that text is not passed, the Government may, after a further reading in each House, ask the National Assembly to reach a final decision. This holds for a private member's bill too. The Government can open this procedure; it cannot guarantee that the Assembly will pass the text.

Lastly, the Government has a floor tool, the single vote (art. 44): at its request, the House proceeds to a single vote on all or part of the text, on the sole basis of the amendments the Government has proposed or accepted. The House still votes, but on the text as the Government accepts it.

<details class="repli"><summary>The wording of articles 45 and 44</summary>

Article 45, paragraph 2: "{{< ado-val "cit_art45d" >}}" Paragraph 3: "{{< ado-val "cit_art45e" >}}" Paragraph 4: "{{< ado-val "cit_art45f" >}}"

Article 44, paragraph 3: "{{< ado-val "cit_art44c" >}}"

</details>

## What does article 49, paragraph 3 change? {#article-49-3}

It allows the Prime Minister, after deliberation by the Council of Ministers, to make the passing of a bill an issue of a vote of confidence before the National Assembly: the bill is then considered passed at that stage of its consideration, without the deputies voting on it, unless a motion of no confidence, tabled within the following twenty-four hours, is carried. The paragraph covers Finance Bills and Social Security Financing Bills; beyond those texts, the Prime Minister may use the procedure for only one other government or private member's bill per session. The bill is not thereby finally passed: the use covers one stage, and consideration goes on. The same bill may be subject to several uses, including during the same reading; each is counted once.

The motion of no confidence targets the Government, and paragraph 2 of the article allows it to be carried only by a majority of the members of the Assembly, only the votes cast in favour being counted. If it is carried, the bill is not considered passed at that stage, and the Government must tender its resignation (art. 50).

<details class="repli"><summary>The wording of articles 49 and 50</summary>

Article 49, paragraph 3: "{{< ado-val "cit_art49a" >}}" And: "{{< ado-val "cit_art49b" >}}" Paragraph 2: "{{< ado-val "cit_art49c" >}}"

Article 50: "{{< ado-val "cit_art50" >}}"

</details>

{{< figure-svg fichier="adopter-493-en" alt="Horizontal bars by legislature: uses of article 49, paragraph 3 on a Finance Bill or Social Security Financing Bill, and on another bill, with under each bar the number of distinct bills and the motions of no confidence carried. Those of the 14th and 15th concern other bills; those of the 16th mostly, and those of the ongoing 17th entirely, concern Finance Bills or Social Security Financing Bills. The values are in the table below the figure." >}}Uses of article 49, paragraph 3, each counted once, by the categories of that paragraph: the public finance programming act falls under "one other bill". This count covers all bills, finance bills included.{{< /figure-svg >}}

{{< fig-actions id="493" >}}

{{< ado-tableau "engagements" "The figure's values in a table" >}}

During the 14th legislature, article 49, paragraph 3 was used {{< ado-val "E14" >}} times, on {{< ado-val "Etextes14" >}} bills that were neither Finance Bills nor Social Security Financing Bills; during the 15th, {{< ado-val "Efois15" >}}; during the 16th, {{< ado-val "E16" >}} times on {{< ado-val "Etextes16" >}} bills, {{< ado-val "Efin16" >}} of these uses on Finance Bills or Social Security Financing Bills and {{< ado-val "Eautre16" >}} on the public finance programming act; during the ongoing 17th, {{< ado-val "E17" >}} times on {{< ado-val "Etextes17" >}} bills, all of them finance bills. The National Assembly's summary sheet on this procedure gives the same totals up to the 16th: «&nbsp;{{< ado-val "cit_fiche64" >}}&nbsp;» [our translation: "{{< ado-val "cit_fiche64_tr" >}}"].

Counting laws rather than uses changes the picture. During the 16th legislature, {{< ado-val "Lfineng16" >}} of the {{< ado-val "Lfin16" >}} finance or social security financing acts promulgated went through at least one use, at one stage or more of their consideration; the others went through none. During the ongoing 17th, it is {{< ado-val "Lfineng17" >}} out of {{< ado-val "Lfin17" >}}. These numbers describe the procedure followed, not the content of the bills nor what a vote would have produced, and they do not explain why use differs from one legislature to another.

No motion of no confidence was carried on these uses, from the 14th to the 16th legislature. On {{< ado-val "censure_date" >}}, article 49, paragraph 3 was used on the {{< ado-val "censure_etape" >}} of {{< ado-val "censure_texte" >}}; according to the same sheet, «&nbsp;{{< ado-val "cit_censure" >}}&nbsp;» [our translation: "{{< ado-val "cit_censure_tr" >}}"]. The bill was not considered passed at that stage, and the Government had to resign.

**The two other situations.** If Parliament has not reached a decision within the time limit set by the Constitution, the provisions of the State budget bill (art. 47) or of the social security budget bill (art. 47-1) may be brought into force by ordinance. These ordinances do not make a statute passed by vote: they bring the provisions of a bill into force. A referendum, by contrast, passes a law without Parliament voting on its text: where the outcome is favourable to the bill, the President of the Republic promulgates the resulting statute (art. 11). When it is held on the Government's recommendation, Parliament debates without voting: the Government makes a statement before each House, followed by a debate. The page [Can the French president call a referendum?](/en/can-the-french-president-call-a-referendum/) counts them.

<details class="repli"><summary>The wording of articles 47, 47-1 and 11</summary>

Article 47: "{{< ado-val "cit_art47c" >}}" Article 47-1: "{{< ado-val "cit_art471c" >}}"

Article 11: "{{< ado-val "cit_art11a" >}}" And: "{{< ado-val "cit_art11b" >}}"

</details>

<details class="repli"><summary>What was checked, and how</summary>

The uses are read in the National Assembly's legislative files, and counted twice by two different routes of the same producer, with the same dates. They are compared, session by session, with the Assembly's statistical bulletins: same numbers of uses and of motions. A single date differs, by one day, for a use in November 2022; the official record of the sitting confirms the date in the data. For a few motions, the data do not contain the vote; the bulletins give their ballots, all below the required majority. The finance acts concerned are found through the Assembly's file identifier, common to both files; the script checks that each use classed as on a Finance Bill or Social Security Financing Bill bears on an act of that kind, and no other.

</details>

## How to judge a promise that requires a law? {#trois-questions}

Three questions are enough to place a promise of a law, without assuming anything about its content.

1. **Who will table the text?** The Government or a member of Parliament. A bill or an amendment from a member of Parliament cannot create or increase public expenditure, and a loss of revenue must be offset by another revenue (art. 40, as the National Assembly applies it); this rule does not cover the Government's texts.
2. **Who will put it on the agenda?** The Government in its priority weeks, a House in its own, an opposition or minority group on its monthly day (art. 48).
3. **Who will have the final say?** Agreement between the two Houses; failing that, the National Assembly, if the Government asks it to (art. 45); or a use of article 49.3, at the risk of a no-confidence vote (arts. 49 and 50).

A law passed is not yet a law applied: the page [Does a law apply as soon as it is passed?](/en/does-a-law-apply-as-soon-as-it-is-passed/) takes it from there. And the page [What can the French president decide alone?](/en/what-can-the-french-president-decide-alone/) deals with what he decides without going through a law.

## What this page does not say {#limites}

It does not measure the Government's influence on private members' bills, nor Parliament's on government bills: the origin of a law is not its content, and amendments are not counted. It does not link the number of uses of article 49.3 to the composition of the Assembly: a coincidence in time does not establish a link. It does not say what becomes of the bills that are not debated, nor why they did not reach the floor. The counts of bills tabled do not match the Assembly's bulletins text by text: the sentence on private members' bills rests only on the worst-case bound. It counts neither budget ordinances nor laws passed by referendum.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="What has to be voted" avis="non" >}}
This page shows who tables laws, who brings them to the floor, who has the final say and what article 49.3 allows. The book follows nine written, dated and signed promises along the chain that runs from the decision to its outcome: what a president decides within his own chain of power, what he has to get voted, what he has to negotiate, and what will never depend on him. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**National Assembly**, open data on the legislative files of the 14th to 17th legislatures (version of {{< ado-val "releve" >}}); annual statistical bulletins; summary sheets no. 64 on the Government's responsibility and no. 52 on the financial admissibility of parliamentary initiatives (in French).

**Senate**, Dosleg database (version of {{< ado-val "releve" >}}); information report no. 802 (2025-2026) on the application of laws, p. 44 (in French).

**Journal officiel**, DILA data; **Constitution**, arts. 11, 24, 39, 40, 44, 45, 46, 47, 47-1, 48, 49 and 50, read on Légifrance (API) in French and quoted in the English translation published by the Conseil constitutionnel.

The figures, quotations, checks and charts are produced by a single script. It reads the origin of laws, the private members' bills and the uses of article 49.3 in the data of the National Assembly, the Senate and the Journal officiel, and finds each quotation word for word in its archived document. The bills counted by the Assembly's statistical bulletins, published as images, are transcribed by hand and serve only for the worst case; the bulletins' uses of article 49.3, read in their text, serve as a cross-check. The script stops if a figure no longer meets the conditions on which the main sentences rest. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_adopter.csv), long format; [JSON](/promesses_adopter.json), with definitions and the record of the checks (field names and some labels in French). This dataset is also archived on Zenodo, with the six others of the same series and their methods note, under a permanent identifier for citation: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664); the archived version does not yet contain the series added on 12 October 2026 (all kinds, laws between two legislatures, finance acts after a use of article 49.3).

{{< reutiliser figures="figures_adopter" jeu="promesses_adopter" sources="National Assembly, Senate (Dosleg), Journal officiel, Conseil constitutionnel" donnees="The origin of the laws promulgated by legislature, by kind and by session, the private members' bills tabled in the National Assembly and not debated in the chamber, and the uses of article 49, paragraph 3; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
In the scope studied ({{< ado-val "champ" >}}), the share of the laws promulgated in France that arose from a private member's bill is {{< ado-val "Ppct14" >}}% during the 14th legislature, {{< ado-val "Ppct15" >}}% during the 15th (at least {{< ado-val "Pminpct15" >}}%), {{< ado-val "Ppct16" >}}% during the 16th and {{< ado-val "Ppct17" >}}% during the ongoing 17th; counting all kinds except treaties, the 15th falls below half ({{< ado-val "Ptotpct15" >}}%). About {{< ado-val "Zdix" >}} in ten ordinary private members' bills tabled in the National Assembly were not debated in plenary before their legislature ended, from the 14th to the 16th, worst case included. Article 49, paragraph 3 was used {{< ado-val "E16" >}} times during the 16th legislature, {{< ado-val "Efin16" >}} of them on Finance Bills or Social Security Financing Bills.
{{< /reutiliser >}}
