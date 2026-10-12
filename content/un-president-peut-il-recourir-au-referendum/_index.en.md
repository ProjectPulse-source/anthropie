---
title: "Can the French president call a referendum?"
url: /en/can-the-french-president-call-a-referendum/
description: "Who can put a text to a referendum in France, by which route (articles 11, 89 and 88-5 of the Constitution) and on which subjects; what the {ref.N} national referendums of the Fifth Republic decided, as at {ref.arrete}, and what became of the {ref.S} shared-initiative bills reviewed by the Conseil constitutionnel, with their grounds quoted. Conseil constitutionnel register, checked against the Journal officiel; open data."
chapo: "Can a French president put a reform to the voters whenever he wants? The Constitution gives him that power through three routes, each with its own conditions: for a Government Bill, a recommendation from the Government or a joint motion of the two Houses, and a subject defined by article 11; for an amendment to the Constitution, a vote of the two Houses in identical terms; for the accession of a State to the European Union, a referendum is the rule unless Parliament decides otherwise. From 4 October 1958 to {ref.arrete}, {ref.N} national referendums were held, the last one on {ref.dernier}. Since {ref.rip_depuis}, members of Parliament backed by voters can also initiate a procedure that may lead to one: it has not led to any vote."
date: 2026-10-06
lastmod: 2026-10-12
# English version of the "Referendum" further topic of the "Presidential promises" dossier (FR:
# content/un-president-peut-il-recourir-au-referendum/_index.md). Same tokens, same keys: values come from the
# affichage_en block of data/promesses_referendum.json (scripts/update_promesses_referendum.py). The Constitution is quoted
# in the English translation published by the Conseil constitutionnel; other French texts in French, with our translation
# (keys *_tr).
donnees: [promesses_referendum]
og_title: "Can the French president call a referendum? The register of referendums of the Fifth Republic and the shared initiative — S. Lalut"
og_image: "images/og-referendum-promesse-en.jpg"
og_image_alt: "Share card: \"Nine national referendums since 4 October 1958\" — timeline of France's national referendums, with the share of 'yes' among valid votes; seven adopted, two rejected (1969 and 2005); none since 29 May 2005, as at 5 October 2026."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_referendum"
  nom: "National referendums of the French Fifth Republic and the shared-initiative referendum: register as at 5 October 2026"
  description: "Register of the national referendums whose results were proclaimed by the Conseil constitutionnel since 1958 (registered voters, voters, valid votes, yes, no, outcome, article of the Constitution), matched vote by vote against the Journal officiel (decree putting the text to the vote, promulgated act); decisions of the Conseil constitutionnel on bills introduced under article 11, paragraph 3 (outcome, condition not met, grounds quoted with their paragraph number, signatures collected). Source: DILA CONSTIT database, as at {ref.arrete}."
  couverture_temporelle: "1958/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "National referendums: registered voters, voters, valid votes, yes, no", unite: "voters"}
    - {nom: "Bills under article 11: outcome of the Conseil constitutionnel's review, condition of article 45-2, grounds quoted, signatures collected", unite: "decisions; voters"}
  sources:
    - "https://echanges.dila.gouv.fr/OPENDATA/CONSTIT/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
    - "https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006071194"
  mots: ["referendum", "France", "article 11", "article 89", "article 88-5", "shared-initiative referendum", "Conseil constitutionnel", "Fifth Republic", "promises"]
  fichiers: ["promesses_referendum.csv", "promesses_referendum.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "Can the French president hold a referendum whenever he wants?"
    answer: "No, not alone and not on any subject. Under article 11 of the Constitution, he may submit to a referendum a Government Bill \"{ref.cit_art11_1}\", and only on the subjects the article lists. An amendment to the Constitution (article 89) must first be passed by the two Houses in identical terms. For the ratification of a treaty on the accession of a State to the European Union (article 88-5), a referendum is the rule, unless the two Houses pass a motion by a three-fifths majority."
  - question: "Must the president put to a referendum a recommendation he receives?"
    answer: "For article 11, the French text says that he \"peut soumettre\" (may submit) on a recommendation from the Government or a joint motion of the two Houses: the recommendation is required, and the article does not make it an obligation. For the shared initiative, once the bill has gathered the support of one tenth of voters and the two Houses have not considered it within the time limit, the French text of article 11 reads \"la soumet\" (submits it), where the published English translation reads \"may submit it\". For a Bill to amend the Constitution passed by the two Houses, article 89 leaves him the choice of Congress instead of a referendum."
  - question: "Does the shared-initiative referendum allow citizens to trigger a referendum?"
    answer: "Not on their own. The initiative belongs to one fifth of the members of Parliament; registered voters support it, and one tenth of them is required. The Conseil constitutionnel first reviews the bill. From {ref.rip_depuis} to {ref.arrete}, it reviewed {ref.S}; {ref.C} was found to meet the statutory conditions and collected {ref.soutiens} signatures of support, against {ref.seuil} required. None was put to a referendum."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 60
  prolongement: true
  nature: "Conseil constitutionnel register, checked against the Journal officiel; open data"
  refonte: "2026-10-12"
onglet:  # "Further topics" panel of the dossier bar (partials/barre-bloc.html)
  long: "Can the French president call a referendum?"
  court: "Referendum"
  role: "register and shared initiative"
---

{{< reutiliser-ancre >}}

Promising to put a reform to the voters means promising to use a route other than a parliamentary vote alone. The French Constitution provides for it: "{{< ref-val "cit_art3" >}}" (art. 3). This page sets out who can put a text to a referendum, by which route and on which subjects, then what the votes held so far decided and what became of the shared-initiative bills, from the register of the Conseil constitutionnel, matched vote by vote against the Journal officiel. It rests on the letter of the texts, the decisions cited and the official documents read, and keeps apart what the texts say, what has been applied and what the Conseil constitutionnel has inferred from them; it is not legal advice. The Constitution is quoted in the English translation published by the Conseil constitutionnel; other French texts are quoted in French, followed by our translation.

## Who can put a text to a referendum? {#qui-peut}

Three articles of the Constitution allow a text to be put to a referendum: article 11 for a Government Bill, article 89 for an amendment to the Constitution, article 88-5 for the accession of a State to the European Union. They do not leave the president the same latitude: depending on the route, he decides on a recommendation he does not make himself, after a vote of the two Houses (the National Assembly and the Senate), or because the article provides that the Bill "shall be submitted" to a referendum. Three articles, but four routes: article 11 also opens the shared initiative, in which members of Parliament backed by voters initiate the procedure ([below](#initiative-partagee)).

**Article 11, for a Government Bill.** The recommendation comes from the Government, when Parliament is in session, or from the two Houses jointly, by a motion; it is published in the Journal officiel. The president then decides: he may "{{< ref-val "cit_art11_peut" >}}", on one of the subjects the article lists (the organisation of the public authorities, reforms of economic, social or environmental policy and the public services contributing to it, the ratification of certain treaties). Where it is the Government that recommends, it makes a statement before each House, followed by a debate. The article says "may": the recommendation is required, and the text does not make it an obligation for the president. He signs the instrument of submission alone: article 19 lists it among the exceptions to countersignature, that is, to the signature of the Prime Minister (and, where required, of the ministers responsible) added to that of the president (see [what the president can decide alone](/en/what-can-the-french-president-decide-alone/)). If the text is adopted, the president promulgates the act within fifteen days.

<details class="repli"><summary>Article 11, word for word</summary>

The president may "{{< ref-val "cit_art11_peut" >}}", but only "{{< ref-val "cit_art11_1" >}}", and on a subject the article defines: "{{< ref-val "cit_art11_objet" >}}". Where the referendum is held on the recommendation of the Government, "{{< ref-val "cit_art11_decl" >}}". If the text is adopted, "{{< ref-val "cit_art11_promulgue" >}}".

</details>

**Article 89, for an amendment to the Constitution.** The text may come from the Government: the president presents it on the recommendation of the Prime Minister, and it is then called a Government Bill. It may also come from deputies or senators: it is then a Private Member's Bill. Either way, it must "{{< ref-val "cit_art89_identiques" >}}", then be approved by referendum. The Government Bill, and it alone, has a second route: the president may submit it to Parliament convened in Congress, where it must obtain three fifths of the votes cast. A Private Member's Bill to amend the Constitution can therefore only be finally adopted by referendum. The decision to convene Congress is not among the exceptions listed in article 19; by the letter of that article, it is countersigned.

<details class="repli"><summary>Article 89, word for word</summary>

"{{< ref-val "cit_art89_init" >}}" A Government Bill or a Private Member's Bill must "{{< ref-val "cit_art89_identiques" >}}". Once the text is passed, "{{< ref-val "cit_art89_ref" >}}" However, "{{< ref-val "cit_art89_voies" >}}", where it must obtain three fifths of the votes cast. The article also sets limits to any amendment: "{{< ref-val "cit_art89_limites" >}}"

</details>

**Article 88-5, for the accession of a State to the European Union.** Here the referendum is the rule: the Government Bill authorising the ratification of an accession treaty is submitted to a referendum by the president. Parliament can avoid it if each House passes the same motion by a three-fifths majority: the Bill then goes to Congress, with three fifths of the votes cast. The article does not cover all accessions: the constitutional act of 23 July 2008 (art. 47) excludes some of them, depending on the date of the conference that prepared them. The instrument of submission is not in the list of article 19 either: it is countersigned. None of the {{< ref-val "N" >}} votes in the register was held under this article. What France decides alone or with the other member States is the subject of [another page of this dossier](/en/what-can-france-decide-in-the-european-union/).

<details class="repli"><summary>Article 88-5 and its 2004 clause, word for word</summary>

"{{< ref-val "cit_art88_5_1" >}}" However, "{{< ref-val "cit_art88_5_2" >}}", that is, by Congress, with three fifths of the votes cast. Under the constitutional act of 23 July 2008 (art. 47), as the Conseil constitutionnel's translation notes, "{{< ref-val "cit_art88_5_2004" >}}"

</details>

**The Conseil constitutionnel oversees; it submits nothing.** "{{< ref-val "cit_art60" >}}" (art. 60). Article 61 also has it review "{{< ref-val "cit_art61" >}}": this is the shared-initiative route, below.

## How many referendums have been held, and what did they decide? {#registre}

{{< figure-svg fichier="referendum-registre-en" alt="Timeline from 1958 to 2026: one stem per national referendum, its height giving the share of yes among valid votes, filled for an adopted text, hollow for a rejected one; a line marks half of the valid votes; a shaded area covers the years since the last vote, in 2005. The values are in the table below the figure." >}}National referendums whose results were proclaimed by the Conseil constitutionnel, from 4 October 1958 to {{< ref-val "arrete" >}}. Excludes the referendum of 28 September 1958 (adoption of the Constitution, before the Conseil was created) and local consultations. Yes is shown as a share of valid votes, turnout is a share of registered voters: in 2000, {{< ref-val "oui_2000" >}}% yes among valid votes, with a turnout of {{< ref-val "part_2000" >}}% of registered voters.{{< /figure-svg >}}

{{< fig-actions id="registre" >}}

{{< ref-tableau "registre" "The votes in a table" >}}

<div class="resultat-phrase">

**The result in one sentence.** From 4 October 1958 to {{< ref-val "arrete" >}}, {{< ref-val "N" >}} national referendums were held in France; the proposed text was approved in {{< ref-val "A" >}} and rejected in {{< ref-val "R" >}}, and the last one took place on {{< ref-val "dernier" >}}.

</div>

{{< ref-val "n_loi" >}} votes were held under article 11, {{< ref-val "n_rev" >}} under article 89: the five-year presidential term, in 2000. Two Bills put to the vote under article 11 nevertheless concerned the Constitution itself: the 1962 Bill, adopted, which amends its articles 6 and 7 so that the president is elected by direct universal suffrage (Act no. 62-1292 of 6 November 1962), and the 1969 Bill, rejected. This use of article 11 to amend the Constitution was contested: when the President of the Senate referred the 1962 Act to it, the Conseil constitutionnel held that it had no jurisdiction (decision no. 62-20 DC of 6 November 1962); according to the National Assembly, the practice has not been used since the failure of 1969.

Turnout ranged from {{< ref-val "part_min" >}}% ({{< ref-val "part_min_an" >}}) to {{< ref-val "part_max" >}}% ({{< ref-val "part_max_an" >}}). The two rejected texts were rejected in 1969 (regions and Senate), with {{< ref-val "non_1969" >}}% of valid votes cast for No, and in 2005 (Treaty establishing a Constitution for Europe), with {{< ref-val "non_2005" >}}%.

## Has the shared-initiative referendum ever succeeded? {#initiative-partagee}

Another route, created by the 2008 constitutional amendment, the shared-initiative referendum (*référendum d'initiative partagée*, RIP), has applied since 1 January {{< ref-val "rip_depuis" >}}: a referendum may be held "{{< ref-val "cit_art11_rip" >}}". It is not a citizens' initiative: the text comes from members of Parliament, and voters support it.

The process has always stopped short of a vote: from {{< ref-val "rip_depuis" >}} to {{< ref-val "arrete" >}}, {{< ref-val "S" >}} bills were referred to the Conseil constitutionnel, {{< ref-val "C" >}} was found to meet the statutory conditions, none gathered the support of one tenth of registered voters, and none was therefore put to a referendum. Even past that threshold, a last filter would remain: it is enough for each House to consider the bill once, even without passing it, for the condition of its submission to a referendum not to be met. The procedure has four steps.

1. At least one fifth of the members of Parliament table a bill; «&nbsp;{{< ref-val "cit_lo1" >}}&nbsp;» (institutional act of 6 December 2013, art. 1; our translation: "{{< ref-val "cit_lo1_tr" >}}").
2. The Conseil constitutionnel checks, «&nbsp;{{< ref-val "cit_o45_2_delai" >}}&nbsp;» (our translation: "{{< ref-val "cit_o45_2_delai_tr" >}}"), that the one-fifth threshold is met, that the subject falls under article 11 and respects two time limits, and that no provision is contrary to the Constitution (ordinance of 7 November 1958, art. 45-2). The two time limits are those of article 11: the bill "{{< ref-val "cit_art11_abrog" >}}", and, after a rejection by the people, "{{< ref-val "cit_art11_deux_ans" >}}".
3. If it meets the conditions, registered voters can support it: «&nbsp;{{< ref-val "cit_lo4" >}}&nbsp;» (institutional act, art. 4; our translation: "{{< ref-val "cit_lo4_tr" >}}").
4. If one tenth of registered voters has supported it, the Conseil constitutionnel declares so, and each of the two Houses has six months from the publication of that decision in the Journal officiel to consider the bill; «&nbsp;{{< ref-val "cit_lo9_susp" >}}&nbsp;» (institutional act, art. 9; our translation: "{{< ref-val "cit_lo9_susp_tr" >}}"). If either House has not considered it within that period, the president submits it to a referendum. For there to be no referendum, it is therefore enough for each House to consider the bill at least once, even without passing it. For this step, the published translation of article 11 reads "{{< ref-val "cit_art11_soumet" >}}", whereas the French text reads "la soumet" (literally, "submits it"), in the indicative, where its first paragraph says "peut soumettre" (may submit). This page notes the difference in wording without taking a position on its legal effect.

<details class="repli"><summary>Article 9 of the institutional act, word for word</summary>

The president submits the bill to a referendum if it «&nbsp;{{< ref-val "cit_lo9" >}}&nbsp;» (our translation: "{{< ref-val "cit_lo9_tr" >}}"). «&nbsp;{{< ref-val "cit_lo9_susp" >}}&nbsp;» (our translation: "{{< ref-val "cit_lo9_susp_tr" >}}")

</details>

{{< figure-svg fichier="referendum-rip-en" alt="Four bars in a funnel, each with its number: bills referred to the Conseil constitutionnel, meeting the statutory conditions, having gathered the support of one tenth of registered voters, put to a referendum; below, a gauge shows the signatures collected for the bill on the Paris airports, against the required threshold." >}}Bills introduced under article 11, paragraph 3, referred to the Conseil constitutionnel, from {{< ref-val "rip_depuis" >}} to {{< ref-val "arrete" >}}, and what became of them.{{< /figure-svg >}}

{{< fig-actions id="rip" >}}

<div class="resultat-phrase">

**The result in one sentence.** From {{< ref-val "rip_depuis" >}} to {{< ref-val "arrete" >}}, the Conseil constitutionnel received {{< ref-val "S" >}} bills under article 11; {{< ref-val "C" >}} was found to meet the statutory conditions and collected {{< ref-val "soutiens" >}} signatures for {{< ref-val "seuil" >}} required, {{< ref-val "part_seuil" >}}% of the threshold; none was put to a referendum.

</div>

{{< ref-tableau "rip" "The decisions in a table, with their grounds" >}}

The other {{< ref-val "non_conformes" >}} bills did not meet the statutory conditions. {{< ref-val "cond3_maj" >}} contained a provision contrary to the Constitution (2021-2 and 2024-6 RIP). {{< ref-val "cond2_maj" >}} did not meet the condition on their subject. The Conseil states why, and this page quotes its reasons without assessing them; the table above gives, decision by decision, the grounds and their paragraph numbers.

**The bills on retirement at 62.** At the date of referral, the Conseil notes, «&nbsp;{{< ref-val "m23_7" >}}&nbsp;» (decision 2023-4 RIP, para. {{< ref-val "m23_7_n" >}}; our translation: "{{< ref-val "m23_7_tr" >}}"). The bill, which prohibited setting that age any higher, «&nbsp;{{< ref-val "m23_8" >}}&nbsp;» ("{{< ref-val "m23_8_tr" >}}", para. {{< ref-val "m23_8_n" >}}), and its adoption by referendum would not alter this, because «&nbsp;{{< ref-val "m23_9" >}}&nbsp;» ("{{< ref-val "m23_9_tr" >}}", para. {{< ref-val "m23_9_n" >}}). The Conseil concludes that «&nbsp;{{< ref-val "m23_10" >}}&nbsp;» ("{{< ref-val "m23_10_tr" >}}", para. {{< ref-val "m23_10_n" >}}). The second bill, tabled in the Senate (2023-5 RIP), was rejected for the same reason; of the increase in a levy on income from assets and investment products that it added, the Conseil notes: «&nbsp;{{< ref-val "m235_10" >}}&nbsp;» ("{{< ref-val "m235_10_tr" >}}", para. {{< ref-val "m235_10_n" >}}).

**The bill on end of life.** Decision 2026-7 RIP rests first on another ground, based on the preparatory work for the 1995 constitutional amendment: «&nbsp;{{< ref-val "m26_7" >}}. {{< ref-val "m26_7b" >}}.&nbsp;» (para. {{< ref-val "m26_7_n" >}}; our translation: "{{< ref-val "m26_7_tr" >}}. {{< ref-val "m26_7b_tr" >}}."). This is the Conseil's interpretation of that preparatory work: article 11 does not mention «&nbsp;questions de société&nbsp;» (questions of society). The decision concerns the subjects that the first paragraph of article 11 opens to a referendum; it says nothing about a revision of the Constitution (article 89). As the bill concerned end of life, the Conseil concludes that «&nbsp;{{< ref-val "m26_9" >}}&nbsp;» ("{{< ref-val "m26_9_tr" >}}", para. {{< ref-val "m26_9_n" >}}). The decision then adds the ground used for retirement: the bill «&nbsp;{{< ref-val "m26_11" >}}&nbsp;» ("{{< ref-val "m26_11_tr" >}}", para. {{< ref-val "m26_11_n" >}}), so «&nbsp;{{< ref-val "m26_13" >}}&nbsp;» ("{{< ref-val "m26_13_tr" >}}", para. {{< ref-val "m26_13_n" >}}).

**{{< ref-val "depots_sans_saisine_maj" >}} other bills** were tabled «&nbsp;en application de l'article 11&nbsp;» (under article 11) without any decision of the Conseil constitutionnel concerning them in the register consulted: in the Senate, No. 459 (20 April 2018, immigration control); in the National Assembly, No. 1749 (6 March 2019, measures against French jihadists who fought in Iraq and Syria) and No. 5203 (5 April 2022, mistreatment of animals). They are not counted among the {{< ref-val "S" >}} referrals, whose unit is a decision of the Conseil. They bore the signatures of {{< ref-val "depots_auteurs" >}} members of Parliament respectively. Article 11 provides for an initiative by one fifth of the members of Parliament. The institutional act provides that the bill is forwarded to the Conseil constitutionnel by the president of the House in which it was tabled; the sources consulted do not establish what became of these texts.

## What a referendum decides, and what it does not {#ce-qu-il-decide}

A referendum settles the text put to the vote: once adopted, an article 11 Bill becomes an act, which the president promulgates within fifteen days, and an article 89 amendment changes the Constitution. The vote does not guarantee, on its own, that the text will be implemented, nor the result a promise attaches to it. An act adopted by referendum remains an act: the legislature may later amend or repeal it, as the Conseil constitutionnel recalls in decision 2023-4 RIP, quoted above. Some of its provisions may have to wait for implementing measures, since the Civil Code provides that, for acts, «&nbsp;{{< ref-val "cit_cc1" >}}&nbsp;» (art. 1; our translation: "{{< ref-val "cit_cc1_tr" >}}"; see [does a law apply as soon as it is passed?](/en/does-a-law-apply-as-soon-as-it-is-passed/)). Nor does the vote shorten the time a measure takes to produce its effects ([can a campaign promise produce results within five years?](/en/can-a-campaign-promise-produce-results-within-five-years/)), and it does not choose [the indicator](/en/how-can-we-tell-whether-a-promise-was-kept/) that will tell whether the promise was kept. The proclamation says how many ballots read yes and no; it does not say why.

## What happened after the 2005 rejection? {#apres-2005}

On 29 May 2005, the Bill authorising the ratification of the Treaty establishing a Constitution for Europe was rejected. In 2008, the ratification of another treaty, the Treaty of Lisbon, was authorised by an act, after an amendment to the Constitution approved by Congress; no referendum was held.

The Treaty of Lisbon, signed after the 2005 rejection, is a different treaty; its title ("Treaty of Lisbon amending the Treaty on European Union and the Treaty establishing the European Community") says that it amends the existing treaties. The Conseil constitutionnel held that the authorisation to ratify it «&nbsp;{{< ref-val "cit_2007_560" >}}&nbsp;» (decision No. 2007-560 DC of 20 December 2007; our translation: can take place only after the Constitution has been amended). On 4 February 2008, Parliament convened in Congress approved the Bill amending Title XV of the Constitution «&nbsp;{{< ref-val "cit_congres_2008" >}}&nbsp;» (under the conditions laid down in article 89, paragraph 3, of the Constitution; [Congress vote](https://www.assemblee-nationale.fr/13/scrutins/jo9000.asp)); this is Act No. 2008-103 of the same day, amending the Constitution. The ratification of the Treaty of Lisbon was then authorised by act No. 2008-125 of 13 February 2008.

Three levels need to be kept apart here. **In law**, article 53 provides that the treaties it lists "{{< ref-val "cit_art53" >}}"; article 11 allows a Bill authorising the ratification of certain treaties to be put to a referendum, but the text says that the president "may" do so, without making it an obligation. **On content**, the title establishes the form of the Treaty of Lisbon, not how its content relates to that of the rejected text, which this page does not compare. **In politics**, the page keeps to two published votes. On {{< ref-val "congres_date" >}}, Congress approved the amendment by {{< ref-val "congres_pour" >}} votes to {{< ref-val "congres_contre" >}}, with a required majority of {{< ref-val "congres_majorite" >}}, three fifths of the votes cast. On {{< ref-val "motion_date" >}}, the National Assembly rejected, by {{< ref-val "motion_contre" >}} votes to {{< ref-val "motion_pour" >}}, a motion tabled by Mr Ayrault and several of his colleagues to put the Bill authorising ratification to a referendum ([vote No. 82](https://www.assemblee-nationale.fr/13/scrutins/jo0082.asp)).

**An amendment announced with a referendum, in 2020 and 2021.** On {{< ref-val "declaration_2020" >}}, before the Citizens' Convention for Climate, the President of the Republic said he was in favour of the rewriting of article 1 of the Constitution that the Convention proposed, to introduce biodiversity, the environment and the fight against climate change, and declared: «&nbsp;{{< ref-val "cit_elysee" >}}&nbsp;» (text published by the Élysée; our translation: "I am ready to resort to a referendum if it were then constitutionally possible after the vote of the Houses, strictly within the framework of our Constitution"). The Government Bill to amend the Constitution supplementing article 1 and concerning the preservation of the environment was tabled in the National Assembly on {{< ref-val "e2021_depot" >}}. Passed by the Assembly on {{< ref-val "e2021_an1" >}}, amended by the Senate on {{< ref-val "e2021_se1" >}}, passed with amendments by the Assembly on {{< ref-val "e2021_an2" >}}, it was amended again by the Senate on {{< ref-val "e2021_se2" >}}: this is the last step in the Senate's legislative file. The two Houses therefore never passed it in identical terms, which article 89 requires before any referendum.

This case shows a condition of article 89 that was not met; it does not explain why no referendum has been held since 2005.

## What to ask of a referendum promise? {#grille}

1. **On what?** A Government Bill on a subject of article 11, an amendment to the Constitution, or the accession of a State to the European Union: each subject has its route, and for the shared initiative the Conseil constitutionnel reviews the subject before any signatures are collected.
2. **By which route?** Article 11, article 89, article 88-5, or the shared initiative.
3. **With whom?** The Government or the two Houses, which recommend or move (art. 11); the two Houses, which pass the text in identical terms (art. 89); one fifth of the members of Parliament and one tenth of voters (shared initiative).
4. **Which conditions remain to be met, and who checks them?** A recommendation or motion published, a statement followed by a debate, an identical vote of the two Houses, or the review of the Conseil constitutionnel and the collection of signatures; the Conseil then ensures the proper conduct of the vote.
5. **To obtain what?** The vote settles a text: an act, which the president promulgates within fifteen days, or an amendment to the Constitution. Its implementing measures and its effects come afterwards, and are judged separately.

## What this page does not say {#limites}

It does not say whether the referendum is a good or a bad instrument, nor why none has been held since 2005: the sources consulted (register of the Conseil constitutionnel, Journal officiel, legislative files, the 2020 statement) do not establish it, and an intention cannot be read in an act. It counts neither the referendum of 28 September 1958, before the Conseil constitutionnel existed, nor local consultations. It reads the Constitution as currently in force and the decisions cited, without legal doctrine or other case law, and is not legal advice. The register stands as at {{< ref-val "arrete" >}}; the 2020-2021 case rests on pages consulted on 12 October 2026.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="What a vote decides" avis="non" >}}
This page shows that a referendum settles a text, not what follows from it. The book, in French, follows nine written, dated and signed promises to their last obstacle, and its closing chapter is devoted to the 2005 referendum and what became of it. It gives no voting advice.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Constitution** of 4 October 1958, art. 3, 11, 19, 53, 60, 61, 88-5 and 89, text in force (Légifrance; English translation published by the Conseil constitutionnel). **Constitutional act** No. 2008-724 of 23 July 2008, art. 47 (text adopted by Congress on 21 July 2008, published by the Senate); **constitutional act** No. 2008-103 of 4 February 2008 (text adopted by Congress the same day, published by the Senate); **act** No. 2008-125 of 13 February 2008. **Ordinance** No. 58-1067 of 7 November 1958, art. 45-2; **institutional act** No. 2013-1114 of 6 December 2013 implementing article 11, art. 1, 4 and 9; **Civil Code**, art. 1.

**Conseil constitutionnel**, proclamations of referendum results (decisions 61-4, 62-7, 62-9, 69-10, 72-11, 88-14, 92-19, 2000-29, 2005-38) and decisions on bills under article 11 (2019-1 and 2019-1-8, 2021-2, 2022-3, 2023-4, 2023-5, 2024-6, 2026-7 RIP), read in the CONSTIT database published by the DILA, as at {{< ref-val "arrete" >}}; decision No. 2007-560 DC.

**Journal officiel** (Légifrance), decrees putting texts to a referendum and acts adopted by referendum; **National Assembly**, open data of the 15th to 17th legislatures (bills under article 11), and analyses of the Congress vote of 4 February 2008 and of vote No. 82 of 6 February 2008 (13th legislature), consulted on 12 October 2026; **Senate**, bill No. 459 (2017-2018) and legislative file of Government Bill to amend the Constitution No. 449 (2020-2021), consulted on 12 October 2026; **Presidency of the Republic**, speech of 29 June 2020 to the Citizens' Convention for Climate (elysee.fr), consulted on 12 October 2026.

<details class="repli"><summary>How the referendum register was checked</summary>

**The register.** The decisions of the Conseil constitutionnel are read in the database published by the DILA, the French official publications office (open files, as at {{< ref-val "arrete" >}}). Among the decisions classified "referendum", only the proclamations of results enter the register; the others are appointments of delegates, answers to complaints and observations. For each vote, the numbers of registered voters, voters, valid votes, yes and no are read in the proclamation, and their consistency is checked (yes and no add up to the valid votes; valid votes, voters and registered voters are in order). The percentages on this page are recalculated from these numbers and rounded to the nearest value; the Conseil constitutionnel's summary table gives them truncated, hence differences of one hundredth of a point for some votes.

**The Journal officiel as a cross-check.** Each vote was matched against the Journal officiel: the decree by which the president puts the text to the vote, at the date given by the proclamation, and, for each adopted text, the promulgated act. The {{< ref-val "A" >}} acts exist; no act exists for the {{< ref-val "R" >}} rejected texts. Only one decree was not found in the Légifrance archive, that of 2 October 1962, whose act is published. A title search of the Journal officiel shows no vote missing from the register.

**The limits.** There is no second independent source for the vote counts for 1961-1988: they are checked for consistency, not against another source. The results published by the Ministry of the Interior for 1992, 2000 and 2005 precede the Conseil's corrections: same vote, different definition, so not a cross-check.

</details>

The figures, the checks and the charts are produced by a single script. It rereads the archived decisions and texts and stops if a figure no longer meets the conditions on which the main sentences rest. It finds word for word each quotation from the Constitution, the ordinance, the institutional act and the Civil Code, and each ground of a decision in the paragraph indicated; it checks the fingerprint of the archived Senate, Élysée and National Assembly pages, finds in them the passages quoted and the dates of the 2021 file, and reads in the two 2008 votes the vote counts the page gives. The list of bills tabled without a decision is checked against Assemblée and Sénat data; the number of their signatories, transcribed in the script, is reread in those data and in the bill tabled in the Senate. The subjects of the votes and bills are written by hand, and the English translations of French texts other than the Constitution are ours. **Download the data** (CC BY 4.0 licence): [CSV](/promesses_referendum.csv), long format; [JSON](/promesses_referendum.json), with the identifiers of the decisions, the grounds quoted and the report of the checks. An earlier version of this dataset, without the grounds quoted added on 12 October 2026, is archived on Zenodo with the six others of the same series and their methods note, under a permanent identifier: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_referendum" jeu="promesses_referendum" sources="Conseil constitutionnel and Journal officiel" donnees="The register of national referendums (registered voters, voters, valid votes, yes, no, article, outcome), the decisions on the shared-initiative referendum with their grounds quoted, and the bills with no decision; the same content exists in CSV, long format, readable in a spreadsheet." >}}
A French president may put a Government Bill to a referendum on a recommendation from the Government or a joint motion of the two Houses, and on the subjects set by article 11 of the Constitution; an amendment to the Constitution (article 89) and the accession of a State to the European Union (article 88-5) have their own routes. From 4 October 1958 to {{< ref-val "arrete" >}}, {{< ref-val "N" >}} national referendums were held; the proposed text was approved in {{< ref-val "A" >}} and rejected in {{< ref-val "R" >}}, and the last one took place on {{< ref-val "dernier" >}}. The shared-initiative referendum, open since {{< ref-val "rip_depuis" >}}, has not yet led to any vote.
{{< /reutiliser >}}
