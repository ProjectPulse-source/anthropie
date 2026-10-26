---
title: "What is technological debt?"
url: /en/technological-debt/
description: "Technological debt is the cost of digital infrastructures — energy, matter, territory, attention — turned into debt by mechanisms of commitment. Not to be confused with the “technical debt” of software engineering."
date: 2026-07-04
lastmod: 2026-10-26
og_title: "What is technological debt? — definition and sources — S. Lalut"
faq:
  - question: "What is the difference between technological debt and technical debt?"
    answer: "Technical debt is a software-engineering notion: the accumulation of design compromises in a program, which makes its evolution ever more costly. Technological debt, in Stéphane Lalut's sense (AWP-06, 2026), is an economic and political mechanism: the cost of digital infrastructures — energy, matter, territory, attention — turned into debt by long-term commitments. One is a property of code; the other, a property of the economic system."
  - question: "Is technological debt a debt in the financial sense?"
    answer: "Not only. Part of it literally is — public guarantees, long-term energy purchase contracts, financing backed by future revenues. But technological debt also includes non-monetary commitments: territories assigned for decades, infrastructure choices that have become irreversible, captured attention. It is a debt in the anthropic sense: a disorder deferred toward the future."
  - question: "Who bears technological debt?"
    answer: "Those who did not sign the commitments: the public budgets that guarantee, the territories that host the infrastructures and their energy and water needs, the generations that will inherit the equipment and its maintenance or dismantling costs, and the users whose attention is the fourth register of cost."
  - question: "Where is the concept formalised?"
    answer: "In AWP-06, “Digital Infrastructures and Technological Debt” (Stéphane Lalut, 2026, DOI 10.5281/zenodo.20025421), sixth of the Anthropy Working Papers, and in the book ANTHROPY – A Big History of Civilization's Hidden Costs, which deploys the general framework."
fiche:  # "The notion at a glance" box (notion-fiche shortcode): restates the page, no new fact
  lignes:
    - t: "Definition"
      d: "The cost of digital infrastructures — energy, matter, territory, attention — turned into debt by mechanisms of commitment: public guarantees, long-term contracts, the irreversibility of infrastructure choices."
    - t: "Origin"
      d: "A concept formalised by the economist Stéphane Lalut in [AWP-06](/en/awp/awp-06/) (2026), within the framework of [anthropy](/en/quest-ce-que-lanthropie/)."
    - t: "Not to be confused with"
      d: "The *technical* debt of software engineering: design compromises accumulated in a program, a property of code rather than of the economic system."
    - t: "Example"
      d: "Data centers: electricity and water contracted for decades, materials extracted elsewhere, land take, an attention economy that finances the whole."
    - t: "Nature of the debt"
      d: "Not only financial: part of it is literally so (guarantees, long-term contracts); the rest is made of non-monetary commitments — territories assigned, irreversible choices, captured attention."
    - t: "Anthropic reading"
      d: "Digital technology has not lightened matter, it has displaced it — in space, in time and toward attention."
      anthropie: true
schemas:  # mechanism diagram (notion-schema shortcode)
  mecanisme:
    titre: "How an infrastructure cost becomes a debt"
    etages:
      - boites:
          - {t: "Digital infrastructure", d: "The promise of an immaterial service, “the cloud”", ton: "ordre"}
        fleche: "three operations"
      - titre: "The cost is converted into commitment"
        boites:
          - {t: "Commitment", d: "Energy contracts, leases, orders: the future cost is locked in the present"}
          - {t: "Guarantee", d: "Public arrangements that make the investment attractive: if the bet fails, the community pays"}
          - {t: "Irreversibility", d: "Going back costs more than carrying on"}
        fleche: "across four coupled registers"
      - titre: "The coupled cost registers (AWP-06)"
        boites:
          - {t: "Energy", d: "Electricity and water under contract", ton: "cout"}
          - {t: "Matter", d: "Materials extracted elsewhere", ton: "cout"}
          - {t: "Territory", d: "Land take, networks sized for them", ton: "cout"}
          - {t: "Attention", d: "The economy that finances the whole", ton: "cout"}
        fleche: "borne by those who did not sign"
      - boites:
          - {t: "Who bears it", d: "The public budgets that guarantee, the territories that host, the generations that will inherit the equipment, the users whose attention is captured", ton: "cout"}
    note: "The registers do not add up: they are coupled. Reducing one often shifts the load toward the other three."
comparaisons:  # boundary between neighbouring notions (notion-comparaison shortcode)
  frontiere:
    titre: "Technical debt, technological debt"
    colonnes: ["Technical debt", "Technological debt"]
    accent: 2
    lignes:
      - {critere: "Field", valeurs: ["Software engineering", "Economics and politics"]}
      - {critere: "What goes into debt", valeurs: ["A program", "A society"]}
      - {critere: "Mechanism", valeurs: ["Design compromises accumulate: ship fast today, pay for maintenance tomorrow", "The present cost of infrastructures is converted into commitments that others will bear"]}
      - {critere: "What it describes", valeurs: ["A property of code", "A property of the economic system"]}
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["notion"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/dette-technologique.md"  # fiche de conception (regle 12), refonte de presentation du 26/10/2026
  bloc: "notions"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 60
  nature: "Notion — definition, origin and sources"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Technological debt"
  court: "Techno."
  long_en: "Technological debt"
---

Technological debt is the cost of digital infrastructures — energy, matter, territory, attention — turned into debt by mechanisms of commitment: public guarantees, long-term contracts, the irreversibility of infrastructure choices. The concept is formalised by the economist Stéphane Lalut in the working paper [AWP-06](/en/awp/awp-06/) (2026) and belongs to the framework of anthropy.

{{< notion-fiche >}}

## Not to be confused with "technical debt"

On the web, "technological debt" almost always refers to the **technical debt** of software engineering: the accumulation of design compromises in a program — ship fast today, pay for maintenance tomorrow. The metaphor is useful, but it describes a property of code.

Technological debt in the anthropic sense designates something else: an **economic and political** mechanism. It is not lines of code that go into debt, it is societies — when they convert the present cost of their digital infrastructures into commitments that others will bear.

{{< notion-comparaison id="frontiere" >}}

## The mechanism: how a cost becomes a debt

{{< notion-schema id="mecanisme" >}}

Three operations turn an infrastructure cost into a debt:

1. **Commitment** — long-term energy purchase contracts, land leases of several decades, equipment orders that straddle political cycles: the future cost is locked in at the present.
2. **Guarantee** — public schemes that alter the risk profile of private investment to make it attractive to institutional capital (the *derisking* described by Daniela Gabor): if the bet fails, the public bears the cost.
3. **Irreversibilisation** — once the network is built, the territory equipped, the uses installed, going back costs more than continuing: yesterday's choice becomes tomorrow's constraint.

[AWP-06](/en/awp/awp-06/) proposes a testable grid of **four coupled cost registers** — energy, matter, territory, attention. These registers do not add up: they couple. Reducing one often shifts the burden to the other three.

## The case of data centers

Data centers make the mechanism visible. Their promise is immaterial — "the cloud" — but their reality engages all four registers at once: electricity and water consumption contracted over decades, materials extracted elsewhere, land footprints and networks sized for them, and an attention economy that funds the whole. Public debate focuses on "how much" (kilowatt-hours, cubic metres); technological debt poses the other question: **who has committed, for how long, and who will bear the cost if the promise changes?**

## Where the concept comes from

{{< canonical-definition >}}

Technological debt is the application of this hypothesis to digital infrastructures: digital technology did not lighten matter, it displaced it — in space (extraction, host territories), in time (commitments, equipment to be dismantled) and toward attention. The short definition is available in the [glossary](/en/glossaire/#technological-debt); the neighbouring analysis of the energy transition in [AWP-04](/en/awp/awp-04/); and what becomes of these infrastructures at the end of their life — a shared inheritance nobody wants — on the page [What are negative commons?](/en/negative-commons/)

## Frequently asked questions

**What is the difference between technological debt and technical debt?** Technical debt is a software-engineering notion — design compromises accumulated in a program. Technological debt is an economic and political mechanism: the cost of digital infrastructures turned into debt by long-term commitments. One is a property of code, the other of the economic system.

**Is it a debt in the financial sense?** Not only. Part of it literally is (guarantees, long-term contracts); the rest is made of non-monetary commitments — assigned territories, irreversible choices, captured attention. It is a debt in the anthropic sense: a disorder deferred toward the future.

**Who bears it?** Those who did not sign: the public budgets that guarantee, the territories that host, the generations that will inherit the equipment, the users whose attention is the fourth register.

## Further reading

- [AWP-06 — *Digital Infrastructures and Technological Debt*](/en/awp/awp-06/) — the working paper that formalises the concept (DOI: 10.5281/zenodo.20025421, open-access PDF).
- The book [*ANTHROPY – A Big History of Civilization's Hidden Costs*](/en/livres/anthropie-ordre-ici-dette-ailleurs/) (2026, 644 p.) deploys the complete framework of which technological debt is one of the applications.
- [What is anthropy?](/en/quest-ce-que-lanthropie/) — the page of the general concept.
