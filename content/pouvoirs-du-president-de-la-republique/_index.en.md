---
title: "What can the French president decide alone?"
url: /en/what-can-the-french-president-decide-alone/
description: "What the French Constitution allows the president to do without countersignature, under what conditions, and who else steps in: the eight provisions of article 19 read in the text, each element backed by an exact quotation. Open data."
chapo: "Without countersignature, the French president can notably appoint the Prime Minister and dissolve the National Assembly, under the conditions the Constitution sets. Article 19 lists eight provisions exempt from countersignature; the president's other instruments are, in principle, subject to the countersignature this article provides for."
date: 2026-10-06
lastmod: 2026-10-06
# English version of tab 1 of the "Presidential promises" dossier (FR: content/pouvoirs-du-president-de-la-republique/_index.md).
# Values come from the affichage_en block of data/pouvoirs_president_donnees.json and texts from
# data/pouvoirs_president_en.yaml (scripts/update_pouvoirs_president.py, guard G2-EN). The Constitution is quoted in the
# English translation published by the Conseil constitutionnel, checked word for word.
donnees: [pouvoirs_president_donnees]
og_title: "What can the French president decide alone? The text, quotation by quotation — S. Lalut"
og_image: "images/og-pouvoirs-president-en.jpg"
og_image_alt: "Share card: \"Deciding alone: what the text says\" — a matrix of eight rows, one per act that article 19 of the French Constitution exempts from countersignature, and four columns: prior condition, other actor, power of the same kind, other written limit; filled cell when the article contains an exact quotation of the element."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "pouvoirs_president_donnees"
  nom: "Acts of the French president exempt from countersignature: an inventory of article 19 in quotations"
  description: "For each of the eight provisions that article 19 of the French Constitution exempts from countersignature (art. 8 para. 1, 11, 12, 16, 18, 54, 56, 61): the act, the recommendation or consultation required, the other actor called on to intervene, the other authorities holding a power of the same kind and the other written limit, each backed by an exact quotation of the article, checked against the text in force read on Légifrance and against the English translation published by the Conseil constitutionnel; and the articles that assign statute law and regulation (arts. 13, 19, 21, 34, 37, 38)."
  couverture_temporelle: "2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Attribute of the act (act, condition, other authority, sharing, limit)", unite: "present or absent in the text of the article"}
    - {nom: "Exact quotation of the article", unite: "text (French; English in the published translation)"}
  sources:
    - "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/"
    - "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
  mots: ["French president", "countersignature", "article 19", "French Constitution", "presidential powers", "statute law", "political promises"]
  fichiers: ["pouvoirs_president_donnees.csv", "pouvoirs_president_donnees.json"]
faq:
  - question: "What can the French president decide alone?"
    answer: "The Constitution does not speak of deciding alone. In article 19, it lists eight provisions whose instruments are exempt from the Prime Minister's countersignature: appointing the Prime Minister, submitting a Government Bill to a referendum, dissolving the National Assembly, exercising emergency powers, sending messages to Parliament, referring a treaty to the Constitutional Council, appointing to the Constitutional Council, referring a law to it. Several have written conditions: the referendum requires a recommendation from the Government or from the two Houses, dissolution requires consulting the Prime Minister and the Presidents of the Houses, emergency powers require a defined crisis and review by the Constitutional Council. His other instruments are subject to the countersignature provided for by article 19: that of the Prime Minister and, where required, of the ministers concerned."
  - question: "Can the French president dismiss the Prime Minister?"
    answer: "Article 8 describes a single route: the president terminates the Prime Minister's appointment \"when the latter tenders the resignation of the Government\" (English translation published by the Conseil constitutionnel). The text provides for no dismissal by the president; it provides for the Government's accountability to the National Assembly (article 20, which refers to articles 49 and 50)."
  - question: "Can the French president refuse to promulgate a law?"
    answer: "Article 10 sets a time limit, not a veto. The president promulgates the law within fifteen days of its transmission; within that time, he may ask Parliament to reopen debate on the Act or some of its sections, which cannot be refused, and Parliament votes again. He may also refer the law to the Constitutional Council before its promulgation (article 61), which suspends the time limit: he then obtains a review of constitutionality, not a judgement of expediency."
  - question: "Who sets taxes in France: the president, the Government or Parliament?"
    answer: "Article 34 of the Constitution reserves to statute law \"the base, rates and methods of collection of all types of taxes\" (English translation published by the Conseil constitutionnel): statutes are passed by Parliament. Matters outside statute law are matters for regulation (article 37), and the power to make regulations is exercised by the Prime Minister (article 21), subject to the decrees deliberated upon in the Council of Ministers that the president signs (article 13), which are countersigned (article 19). After authorisation by Parliament, the Government may also act by ordinances (article 38), issued in the Council of Ministers and signed by the president (article 13)."
ressource:  # index /en/resources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 10
  nature: "The text of the French Constitution, quotation by quotation; open data"
onglet:  # bar of its block (partials/barre-bloc.html, set by the template)
  long: "What can the French president decide alone?"
  court: "Decide"
  role: "signatures and conditions"
---

{{< reutiliser-ancre >}}

**"Deciding alone" is not a category of the French Constitution.** It distinguishes the instruments the president signs **without countersignature**, those of the {{< pv-val "n_renvois" >}} provisions listed in article 19, from all the others, which are countersigned by the Prime Minister and, where required, by the ministers concerned. The question is nonetheless the right one, because it is the one the voter asks: of what a president promises, what depends on his signature, and whom else does the text bring in?

**Without countersignature does not mean without condition, nor without other actors.** This page describes the powers and interventions that appear in the text; it does not measure the president's political influence in practice. To show this, the page reads the {{< pv-val "n_renvois" >}} articles referred to in article 19 and fills a cell only with an **exact quotation** of the article, found word for word in the text in force by a script: no cell is filled by hand. The Constitution is quoted in the English translation published by the Conseil constitutionnel, itself checked word for word; the French text, read on Légifrance, remains the reference.

{{< figure-svg fichier="pouvoirs-article19-en" alt="Matrix of eight rows, one per act that article 19 exempts from countersignature, and four columns: prior recommendation or consultation, another actor stepping in for what follows, power of the same kind held by other authorities, other written limit. The filled cells are listed, quotation by quotation, in the table after the figure." >}}One row per provision referred to in article 19, one column per element. Filled cell: the article itself contains an exact quotation of the element (full list below); empty cell: that article does not contain it, which says nothing of other articles or of practice.{{< /figure-svg >}}

{{< fig-actions id="article19" >}}

<div class="resultat-phrase">

**The finding in one sentence.** Of the {{< pv-val "n_renvois" >}} provisions that article 19 exempts from countersignature, only {{< pv-val "n_seuls" >}} contain, in their text, no prior condition, no later intervention of another actor and no power of the same kind given to other authorities: {{< pv-val "seuls_liste" >}}. This does not mean that the president has only {{< pv-val "n_seuls" >}} powers of his own.

</div>

<details class="repli"><summary>The quotations that fill the matrix, cell by cell</summary>

{{< pouvoirs-president vue="citations" >}}

Each quotation is checked at each generation of the data: the script rereads the archived Légifrance response for the article (identifier, version in force, fingerprint) and refuses to write if a quotation is not found in it word for word; it checks the English quotations in the same way against the translation published by the Conseil constitutionnel. It also rereads the list of references in the text of article 19 itself: a forgotten or added act would stop publication.

</details>

## What does "deciding alone" mean for a French president? {#decider-seul}

Article 19 sets the general rule: "{{< pv-val "cit19" >}}" Countersignature is the signature of a member of the Government next to the president's. The list of exceptions is therefore the list of acts that no minister has to sign.

This criterion does not say everything. An act exempt from countersignature may require a recommendation (the referendum) or a consultation (dissolution, emergency powers), bring in the voters or the Constitutional Council for what follows, or also belong to other authorities: the Prime Minister, the Presidents of the Houses and sixty deputies or senators can also refer matters to the Constitutional Council. The four columns of the matrix are these four elements, and they add up.

## Which acts does the president sign without countersignature? {#sans-contreseing}

The fiches that follow set out, for each of the {{< pv-val "n_renvois" >}} provisions, who decides, the condition, the third party involved and what the act produces. They are read alongside the role that article 5 gives the president: to ensure due respect for the Constitution and to ensure, "{{< pv-val "cit5" >}}".

{{< pouvoirs-president vue="sans_contreseing" >}}

## Who sets the rules citizens feel? {#qui-fixe-les-regles}

**Signing is not enough to govern.** When a president promises a tax cut, a reform or a new rule, through which other signatures must he go? Taxes, benefits, obligations: the text divides them between two instruments, statute law and regulation. **Statute law**, passed by Parliament, sets the rules in the matters of article 34, including taxation. **Regulation** covers the rest: "{{< pv-val "cit37" >}}" (article 37). The power to make regulations is exercised by the Prime Minister (article 21), subject to the decrees deliberated upon in the Council of Ministers, which the president signs (article 13) and which are countersigned (article 19). After authorisation by Parliament, the Government may also take, by ordinance, measures that are normally the preserve of statute law (article 38).

{{< pouvoirs-president vue="regles" >}}

This is why a campaign promise on a tax goes through a vote. When a promise has to be implemented nationally by decree, the decree falls to the Prime Minister or, if it is deliberated upon in the Council of Ministers, is signed by the president and countersigned: in both cases, signatures other than the president's alone come in.

## Which powers are attributed to him personally although they are countersigned? {#pouvoirs-contresignes}

Commander-in-Chief, pardon, treaties, decrees, appointments: these are the most visible attributes of the office, and none appears in the list of article 19. When they give rise to an instrument of the president that does not fall under the exceptions of article 19, these attributes are subject to the countersignature this article provides for.

{{< pouvoirs-president vue="contresigne" >}}

## Who determines the policy of the Nation? {#politique-de-la-nation}

Article 20 answers plainly: "{{< pv-val "cit20" >}}" It has at its disposal the civil service and the armed forces, and it is accountable to Parliament. This is the sentence that best separates what a president promises from what he signs.

{{< pouvoirs-president vue="gouvernement" >}}

## What this page does not say {#limites}

It keeps to the text in force, reread on Légifrance. It describes neither institutional practice nor case law, and it is not legal advice: an empty cell in the matrix means that the article concerned does not contain the element, not that no other article or practice does. Where the text is silent, for instance on whether the president may refuse to sign an ordinance, the page says so without deciding.

The text sets the signatures; it does not say who inspires the decisions. A president's real weight also depends on the majority in the National Assembly, to which the Government is accountable (art. 20): this is why the same text can give very different presidencies depending on whether that majority supports him or not.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Following a promise beyond the signature" avis="non" >}}
This page says who signs. The book asks the next question: once the elected official is in office, through which chain does a campaign promise pass? It proposes a grid in four zones — what a president decides within his own chain of power, what he has to get voted, what he has to negotiate with those whose signature is missing, and what will never depend on him — and tests it on nine written, dated and signed promises. It gives no voting advice. The book exists in French only.
{{< /appel-livre >}}

## Frequently asked questions {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

All the articles cited here were read in their version in force, on Légifrance, on the date indicated, and are quoted in the English translation published by the Conseil constitutionnel ([Constitution of 4 October 1958](https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958)). Each fiche refers to the articles on which it rests.

{{< pouvoirs-president vue="sources" >}}

The inventory, quotations and matrix are produced by a single script, which rereads the archived texts and refuses to write if a quotation stops appearing in its article; no cell is filled by hand. **Download the data** (CC BY 4.0 licence): [CSV](/pouvoirs_president_donnees.csv), long format, one row per element and per article (French quotations); [JSON](/pouvoirs_president_donnees.json), with definitions and the record of the checks (in French).

{{< reutiliser figures="figures_pouvoirs" jeu="pouvoirs_president_donnees" sources="Légifrance (Constitution of 4 October 1958) and the Conseil constitutionnel's English translation" donnees="The inventory of the eight provisions of article 19, each element with its exact quotation, its article and its reading date, and the articles that assign statute law and regulation; the same content exists as CSV, in long format, readable in a spreadsheet." >}}
This page reads, in the text of the French Constitution, the {{< pv-val "n_renvois" >}} provisions that article 19 exempts from countersignature. Only {{< pv-val "n_seuls" >}}, {{< pv-val "seuls_liste" >}}, contain in their article no prior condition, no later intervention of another actor and no power of the same kind given to other authorities; this does not mean that the president has only these powers of his own. Statute law, passed by Parliament, sets taxes in particular (art. 34); regulation belongs to the Prime Minister (art. 21), except for the decrees deliberated upon in the Council of Ministers, which are countersigned.
{{< /reutiliser >}}
