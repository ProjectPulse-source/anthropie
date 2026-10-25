---
title: "What can the French president decide alone?"
url: /en/what-can-the-french-president-decide-alone/
description: "What the French Constitution allows the president to do without countersignature, under what conditions, and who else steps in: the {pv.n_renvois} provisions of article 19 read act by act, each element backed by an exact quotation. Open data."
chapo: "The president appoints the Prime Minister. Can he dismiss him? No: the Constitution provides that the Prime Minister's appointment ends when the resignation of the Government is tendered. As a general rule, an instrument of the president also bears the signature of a minister: this is countersignature. Article 19 exempts the instruments of {pv.n_renvois} provisions from it; even there, the text most often brings in someone else, before or after the president. His most visible powers (the armed forces, pardon, treaties, appointments) are not on that list: they are countersigned."
date: 2026-10-06
lastmod: 2026-10-11
# English version of tab 1 of the "Presidential promises" dossier (FR: content/pouvoirs-du-president-de-la-republique/_index.md).
# Values come from the affichage_en block of data/pouvoirs_president_donnees.json and texts from
# data/pouvoirs_president_en.yaml (scripts/update_pouvoirs_president.py, guard G2-EN). The Constitution is quoted in the
# English translation published by the Conseil constitutionnel, checked word for word.
donnees: [pouvoirs_president_donnees]
textes_lus: pouvoirs_president  # dates de lecture sur Légifrance (lu_le) affichées sous le chapô : partials/page-date-visible.html
og_title: "What can the French president decide alone? The text, quotation by quotation — S. Lalut"
og_image: "images/og-pouvoirs-president-en.jpg"
og_image_alt: "Share card: \"Deciding alone: what the text says\" — a matrix of twelve rows, one per act contained in the eight provisions that article 19 of the French Constitution exempts from countersignature, and four columns: required before the act, another actor afterwards, shared power, other written limit; filled cell when the article contains an exact quotation of the element."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "pouvoirs_president_donnees"
  nom: "Acts of the French president exempt from countersignature: an inventory of article 19, act by act, in quotations"
  description: "For each of the acts contained in the eight provisions that article 19 of the French Constitution exempts from countersignature (art. 8 para. 1, 11, 12, 16, 18, 54, 56, 61): the act, what the text requires before it (recommendation, consultation or act of another actor), the other actor called on to intervene afterwards, the other authorities holding a power of the same kind and the other written limit, each backed by an exact quotation of the article, checked against the text in force read on Légifrance and against the English translation published by the Conseil constitutionnel, with its timing, its optional character and the reason for its classification (in French); and the articles that assign statute law and regulation (arts. 13, 19, 21, 34, 37, 38, 47, 49)."
  couverture_temporelle: "2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Attribute of the act (act, condition, other actor, sharing, limit)", unite: "present or absent in the text of the article"}
    - {nom: "Exact quotation of the article", unite: "text (French; English in the published translation)"}
    - {nom: "Timing, optional character and reason for the classification", unite: "text (French)"}
  sources:
    - "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
  mots: ["French president", "countersignature", "article 19", "French Constitution", "presidential powers", "statute law", "political promises"]
  fichiers: ["pouvoirs_president_donnees.csv", "pouvoirs_president_donnees.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "electoral promises and French political institutions"
faq:
  - question: "What can the French president decide alone?"
    answer: "The Constitution does not speak of deciding alone. Article 19 exempts from the Prime Minister's countersignature the instruments of {pv.n_renvois} provisions: appointing the Prime Minister and terminating his appointment, submitting a text to a referendum, dissolving the National Assembly, exercising emergency powers, addressing Parliament, referring a treaty or a statute to the Constitutional Council, appointing to the Constitutional Council. Of the {pv.n_actes} acts they contain, {pv.n_encadres_acte} bring in, in their own article, another actor before or after the president: a recommendation for the referendum, a consultation and then an election for dissolution. His other instruments are countersigned."
  - question: "Can the French president dismiss the Prime Minister?"
    answer: "No. Article 8 describes a single route: the president terminates the Prime Minister's appointment \"when the latter tenders the resignation of the Government\" (English translation published by the Conseil constitutionnel). Article 50 describes the case in which this resignation becomes compulsory: when the National Assembly passes a resolution of no-confidence or fails to endorse the Government programme or a general policy statement. This obligation arises from a vote of the Assembly; the text does not give it to the president."
  - question: "Who sets taxes in France: the president, the Government or Parliament?"
    answer: "Article 34 reserves to statute law \"the base, rates and methods of collection of all types of taxes\" (English translation published by the Conseil constitutionnel). A tax promise therefore goes through Parliament, but not always through a vote on the text: on a finance bill, the Prime Minister may, after deliberation by the Council of Ministers, make its passing an issue of a vote of confidence, and the bill is considered passed unless a resolution of no-confidence is carried (article 49, paragraph 3); if Parliament fails to reach a decision within the time limit set by article 47, the provisions of the bill may be brought into force by ordinance. In none of these cases is the president's signature enough."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"
  bloc: "promesses"
  livres: ["un-president-peut-il-tenir-ses-promesses"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 10
  nature: "The text of the French Constitution, quotation by quotation; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "What can the French president decide alone?"
  court: "Decide"
  role: "signatures and conditions"
---

{{< reutiliser-ancre >}}

"{{< pv-val "cit8a" >}} {{< pv-val "cit8b" >}}" (article 8). The appointment rests on his signature alone; the end of the appointment requires an act of the Prime Minister, the resignation he tenders.

To measure the gap between the image of a president who decides alone and what the text says, the page starts from the only list the Constitution draws up: the instruments the president signs **without countersignature**, that is, without the signature of a minister next to his own. It reads them one by one, and records an element only if it is written, word for word, in the article. The Constitution is quoted in the English translation published by the Conseil constitutionnel, itself checked word for word; the French text, read on Légifrance, remains the reference.

*Status: a documentary reading of the French Constitution, without legal certification. Each quotation is checked word for word; its classification is a reading, justified cell by cell [further down](#methode).*

{{< figure-svg fichier="pouvoirs-article19-en" alt="Matrix of twelve rows, one per act contained in the eight provisions that article 19 exempts from countersignature, grouped by article, and four columns: required before the act (recommendation, consultation or act of another actor), another actor afterwards, power shared with other authorities, other written limit. The filled cells are listed, quotation by quotation, in the section on method." >}}The table: one row per act, grouped by provision of article 19; one column per element. Filled cell: the article itself contains an exact quotation of the element; empty cell: that article does not contain it, which says nothing of other articles or of practice. Another actor afterwards: an institution, authority or electorate to which the article assigns a distinct intervention, after the president's act, including an optional one; mere practical arrangements for carrying out the act are not counted.{{< /figure-svg >}}

{{< fig-actions id="article19" >}}

<div class="resultat-phrase">

**The finding in one sentence.** Of the {{< pv-val "n_actes" >}} acts that article 19 exempts from countersignature, {{< pv-val "n_encadres_acte" >}} bring in someone else, before or after the president, in the very text of their article.

**This count reads the text of each article, not practice nor the rest of the Constitution.**

Stepping in does not always mean blocking: before dissolving, the president must consult the Prime Minister, not obtain his agreement. That leaves {{< pv-val "n_seuls_acte" >}} acts: {{< pv-val "seuls_acte_liste" >}}. For these, the article provides for neither a recommendation, consultation or act of another actor beforehand, nor the intervention of another actor afterwards.

</div>

## What does "deciding alone" mean for a French president? {#decider-seul}

Article 19 sets the rule: "{{< pv-val "cit19" >}}" The exceptions are therefore the acts no minister has to sign. In the text, this is what comes closest to "deciding alone", without being the same thing.

**Without countersignature does not mean without condition.** The text may require, before the act, a recommendation (for the referendum), a consultation (for dissolution) or an act of another actor (the resignation the Prime Minister tenders). It may bring in afterwards the voters, Parliament or the Constitutional Council, sometimes merely as a possibility: a statement before Congress may be followed by a debate, without a vote. Other authorities may hold a power of the same kind. Finally, the text may limit the act in time, in subject or in effect. These are the four columns of the table above; a single act may fill several.

**Three levels of reading.** The table and the counts read only the text of the article referred to in article 19. The entries below add what other articles, Institutional Acts and two court decisions say. The section on the policy of the Nation then deals with practice. These last two levels change the scope of an act, never the content of a cell.

An example. To appoint the Prime Minister, article 8 brings in no one else. But the Government appointed falls under article 20: "{{< pv-val "cit20b" >}}". If the National Assembly censures it, it must tender its resignation (article 50).

## Which acts does the president sign without countersignature? {#sans-contreseing}

One entry per provision, {{< pv-val "n_renvois" >}} in all: the short answer first, then, when unfolded, the detail quotation by quotation (what the text requires before the act, who steps in afterwards, what the act produces, what other texts add). They are read alongside the role that article 5 gives the president: to ensure due respect for the Constitution and to ensure, "{{< pv-val "cit5" >}}".

{{< pouvoirs-president vue="sans_contreseing" >}}

## Which powers are attributed to him personally although they are countersigned? {#pouvoirs-contresignes}

Commander-in-Chief, pardon, treaties, decrees, appointments: these are the most visible attributes of the office, and none appears in the list of article 19. When they give rise to an instrument of the president, that instrument is subject to the countersignature this article provides for. Some also bring in Parliament or another institution: part of the treaties may be ratified only by an Act of Parliament, and some appointments go through a consultation of the parliamentary committees or through the High Council of the Judiciary.

{{< pouvoirs-president vue="contresigne" >}}

## Who sets the rules citizens feel? {#qui-fixe-les-regles}

**Signing is not enough to govern.** A tax cut, a reform, a new rule: through which signatures other than his own must a president's promise go? The text sorts rules into two categories. **Statute law**, which goes through Parliament, covers the matters of article 34, including taxation. **Regulation** covers the rest: "{{< pv-val "cit37" >}}" (article 37). The Prime Minister exercises the power to make regulations (article 21). The exception: decrees deliberated upon in the Council of Ministers, which the president signs (article 13) and which are countersigned (article 19). Finally, with Parliament's authorisation, the Government may take, by ordinance, measures that are normally the preserve of statute law (article 38).

{{< pouvoirs-president vue="regles" >}}

A tax promise therefore goes through Parliament, but not always through a vote on the text. On a finance bill, the Prime Minister may, after deliberation by the Council of Ministers, which the president chairs (article 9), make its passing an issue of a vote of confidence: "{{< pv-val "cit49" >}}" unless a resolution of no-confidence is carried (article 49, paragraph 3). And if Parliament fails to reach a decision within the time limit set by article 47, the provisions of the bill may be brought into force by ordinance. These procedures are set out in the page "[Who can get a law passed in France?](/en/who-can-get-a-law-passed-in-france/)". A promise implemented by decree also brings in signatures other than the president's: the Prime Minister's, or the countersignature if the decree is deliberated upon in the Council of Ministers.

## Who determines the policy of the Nation? {#politique-de-la-nation}

**Why, then, does the Élysée seem to decide everything?** The answer is not in the list of article 19, but in article 20: "{{< pv-val "cit20" >}}" It has at its disposal the civil service and the armed forces, and it answers to Parliament.

**The Government answers to the Assembly.** A resolution of no-confidence can be passed only by a majority of the members of the National Assembly (article 49); if it is, "{{< pv-val "cit50" >}}" (article 50). The Government therefore cannot remain in office against an absolute majority of deputies voting to censure it, nor when the Assembly fails to endorse its programme or a general policy statement (article 50). The Prime Minister may also tender his resignation without having been censured (article 8).

**When the Assembly's majority supports the president**, the Government he appointed conducts the policy on which the president was elected: this is where the image of a president who decides everything comes from. That link belongs to political practice, which the text does not describe. When a Prime Minister leaves office at the president's request, which belongs to the same practice, the end of the appointment still goes, in law, through the resignation he tenders (article 8). The text makes that resignation compulsory only after a vote of the Assembly (article 50).

**When that majority is opposed to him**, that is, in cohabitation, the same text gives a different presidency: the Government, accountable to that majority, determines and conducts the policy of the Nation, and the president keeps the acts exempt from countersignature, with their conditions. Dissolution allows him to ask the voters again for a majority; they are the ones who grant it. The law allocates the powers; the majority conditions their political exercise.

{{< pouvoirs-president vue="gouvernement" >}}

## Before assessing a presidential promise, what should be checked? {#avant-d-evaluer}

A campaign promise is not judged by its wording, but by the path it will have to follow. Five checks, each based on a page of this dossier, apply to any promise, whichever candidate makes it:

1. **Who signs?** Does the act fall to the president without countersignature, and what does its article then require before and after it? Or are other signatures needed? See [the acts without countersignature](#sans-contreseing), and [who sets the rules](#qui-fixe-les-regles).
2. **Is a law needed, and who can get it passed?** See [who can get a law passed](/en/who-can-get-a-law-passed-in-france/), and, for a reform put to the voters, [the referendum](/en/can-the-french-president-call-a-referendum/).
3. **Is the decision taken in Paris?** In some matters it is taken in the European Union, with other States: see [what France can decide in the European Union](/en/what-can-france-decide-in-the-european-union/).
4. **Once passed, does the measure apply, and how long does it take to produce its effects?** See [the implementation of laws](/en/does-a-law-apply-as-soon-as-it-is-passed/) and [the time a training takes](/en/can-a-campaign-promise-produce-results-within-five-years/).
5. **Which observable criterion will say whether it was kept?** An indicator, an act, a threshold or a deadline, set in advance. See [how to tell whether a promise was kept](/en/how-can-we-tell-whether-a-promise-was-kept/).

These questions do not say whether a promise is good or bad: they say what its fulfilment depends on. That another actor intervenes does not mean that it blocks: it only means that the outcome does not rest on a single signature. And they concern authorisations and procedures, not means: appropriations voted in the finance act, staff and departments to carry it out, local authorities and public bodies that apply it, courts that may be seized. A promise may clear every step of this series and still lack those means.

## How is the table established? {#methode}

**A documentary reading of the French Constitution, without legal certification.** Two things must be told apart. That each quotation appears word for word in the text in force: a script checks it at each generation of the data, against the archived Légifrance response for each text (and the English quotations against the translation published by the Conseil constitutionnel), and refuses to write otherwise. That each quotation sits in the right column: this is a reading, made cell by cell by the editorial team and submitted to an external review; no lawyer has reviewed it to date. Each classification carries its reason, as does each decisive empty cell: they are in the dataset, in French.

**The criterion.** An act is retained when the text of its article requires before it no recommendation, no consultation and no act of another actor, and brings in no other actor afterwards, even optionally. Shared powers and other written limits do not enter the criterion. Counted act by act, it retains {{< pv-val "n_seuls_acte" >}} acts out of {{< pv-val "n_actes" >}}.

**Another actor afterwards**: an institution, authority or electorate to which the article assigns a distinct intervention, after the president's act, including an optional one. Mere practical arrangements for carrying out the act are not counted. The Constitutional Council, when a treaty or a statute is referred to it, rules: that is a distinct intervention. The reading aloud of the message the president addresses to the Houses is not counted: it is the way the message reaches them, not a distinct intervention. A retained act is therefore not an act performed by no one else; likewise, appointing the Prime Minister produces a Government accountable to Parliament.

<details class="repli"><summary>Counted by provision: why an earlier version found a different number</summary>

An earlier version of this dataset, published on 6 October 2026, counted by provision: each was represented by the first act its article gives the president. The same criterion then retains {{< pv-val "n_seuls_renvoi" >}} provisions out of {{< pv-val "n_renvois" >}}; counted act by act, it retains {{< pv-val "n_seuls_acte" >}} acts out of {{< pv-val "n_actes" >}}.

The act that escaped the first count is the designation of the president of the Constitutional Council, which article 56 provides for after the appointment of three members. Those appointments go through an opinion of the parliamentary committees; the designation of the president requires none.

</details>

<details class="repli"><summary>The quotations that fill the table, act by act</summary>

{{< pouvoirs-president vue="citations" >}}

</details>

## What this page does not say {#limites}

It keeps to the texts in force, reread on Légifrance, and to two decisions of the Conseil d'État read in full. It does not describe institutional practice beyond what the section on the policy of the Nation says of it, and it is not legal advice. Where the text is silent, for instance on whether the president may refuse to sign an ordinance, the page says so without deciding. The counts measure neither the president's autonomy nor the number of his own powers.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Following a promise beyond the signature" avis="non" >}}
This page says who signs. The book asks the next question: once the elected official is in office, through which chain does a campaign promise pass? It proposes a grid in four zones — what a president decides within his own chain of power, what he has to get voted, what he has to negotiate with those whose signature is missing, and what will never depend on him — and tests it on nine written, dated and signed promises. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

All the texts cited here were read in their version in force, on Légifrance, on the date indicated; article 17 was also read in its 1958 version, for the comparison drawn in the entry on pardon. The Constitution is quoted in the English translation published by the Conseil constitutionnel ([Constitution of 4 October 1958](https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958)); other French texts are quoted in French, with our translation. Each entry refers to the texts on which it rests.

{{< pouvoirs-president vue="sources" >}}

**Download the data** (CC BY 4.0 licence): [CSV](/pouvoirs_president_donnees.csv), long format, one row per quotation or empty cell, with its timing, its optional character and the reason for its classification (French quotations); [JSON](/pouvoirs_president_donnees.json), with definitions, counting criteria and the record of the checks (in French). An earlier version of this dataset, one row per provision, is archived on Zenodo with the six others of the same series and their methods note: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664); the dataset downloadable here, act by act, replaces it.

{{< reutiliser figures="figures_pouvoirs" jeu="pouvoirs_president_donnees" sources="Légifrance (Constitution of 4 October 1958) and the Conseil constitutionnel's English translation" donnees="The inventory of the eight provisions of article 19, act by act: each element with its exact quotation, its article, its reading date, its timing and the reason for its classification, and the articles that assign statute law and regulation; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
This page reads, in the text of the French Constitution, the {{< pv-val "n_renvois" >}} provisions that article 19 exempts from countersignature. Read act by act, they contain {{< pv-val "n_actes" >}} acts; only {{< pv-val "n_seuls_acte" >}}, {{< pv-val "seuls_acte_liste" >}}, provide in their article for neither a recommendation, consultation or act of another actor beforehand nor the intervention of another actor afterwards. This count describes the text of each article, not practice. Statute law, which goes through Parliament but not always through a vote on the text (arts. 47 and 49, para. 3), sets taxes in particular (art. 34); the Prime Minister exercises the power to make regulations (art. 21), except for the decrees deliberated upon in the Council of Ministers, which the president signs and which are countersigned.
{{< /reutiliser >}}
