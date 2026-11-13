---
title: "What is technological debt?"
og_image: "images/og-notion-dette-techno-en.jpg"
og_image_alt: "Share card: “Technological debt” and its diagram"
url: /en/technological-debt/
description: "Technological debt is the cost of digital infrastructures — energy, matter, territory, and possibly attention — turned into debt by commitment, guarantee and irreversibilisation. Not to be confused with the “technical debt” of software engineering."
sans_chapo: true  # le premier paragraphe dit déjà la description (07/11/2026)
date: 2026-07-04
lastmod: 2026-11-13
journal:  # révisions qui changent la lecture de la page
  - {date: 2026-11-13, texte: "Source check (AWP-06): attention a possible register, not a constituted debt; reserved capacity instead of contracted electricity and water; contingent guarantees; Gabor's derisking transposed by AWP-06; exposed populations among those who bear it; data centres as candidate negative commons."}
  - date: 2026-11-04
    texte: "Three wordings aligned with AWP-06 and with what the page demonstrates: attention is no longer presented as \"the economy that finances the whole\"; cooling water belongs to matter; the shift from one register to the others becomes what the grid must establish case by case."
og_title: "What is technological debt? — definition and sources — S. Lalut"
faq:
  - question: "What is the difference between technological debt and technical debt?"
    answer: "Technical debt is a software-engineering notion: the accumulation of design compromises in a program, which makes its evolution ever more costly. Technological debt, in Stéphane Lalut's sense (AWP-06, 2026), is an economic and political mechanism: the cost of digital infrastructures — energy, matter, territory, and possibly attention — turned into debt by three operations: commitment, guarantee, irreversibilisation. One is a property of code; the other, a property of the economic system."
  - question: "Is technological debt a debt in the financial sense?"
    answer: "Not only. Part of it is financial — long-term energy purchase contracts, financing backed by future revenues, and public guarantees, which remain contingent commitments and become a debt only if they are called. But technological debt also includes non-monetary commitments: territories assigned for decades, infrastructure choices that have become irreversible, and possibly solicited attention. It is a debt in the anthropic sense: a displaced cost that has become durable, guaranteed or hard to reverse."
  - question: "Who bears technological debt?"
    answer: "The public budgets that guarantee, and above all those who did not sign the commitments: the territories that host the infrastructures and their energy and water needs, the populations exposed to the mines, factories and waste of the supply chain, the generations that will inherit the equipment and its maintenance or dismantling costs, and possibly the users, whose attention may become a fourth register of cost."
  - question: "Where is the concept formalised?"
    answer: "In AWP-06, “Digital Infrastructures and Technological Debt” (Stéphane Lalut, 2026, DOI 10.5281/zenodo.20077993), sixth of the Anthropie Working Papers. The book ANTHROPY – A Big History of Civilization's Hidden Costs deploys the general framework of which this concept is one application."
fiche:  # "The notion at a glance" box (notion-fiche shortcode): restates the page, no new fact
  lignes:
    - t: "Definition"
      d: "The cost of digital infrastructures — energy, matter, territory, and possibly attention — turned into debt by three operations: commitment (long-term contracts), public guarantee and the irreversibilisation of infrastructure choices."
    - t: "Origin"
      d: "A concept formalised by the economist Stéphane Lalut in [AWP-06](/en/awp/awp-06/) (2026), within the framework of [anthropy](/en/quest-ce-que-lanthropie/)."
    - t: "Not to be confused with"
      d: "The *technical* debt of software engineering: design compromises accumulated in a program, a property of code rather than of the economic system."
    - t: "Example"
      d: "Data centers: reserved electrical capacity and networks sized for several decades, water needs depending on the site, materials extracted elsewhere, land take."
    - t: "Nature of the debt"
      d: "Not only financial: part of it is (long-term contracts; guarantees, which become a debt if they are called); the rest is made of non-monetary commitments — territories assigned, irreversible choices, and possibly solicited attention."
    - t: "Anthropic reading"
      d: "Digital technology has not lightened matter, it has displaced it — in space, in time and onto other groups."
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
          - {t: "Guarantee", d: "Public arrangements that make the investment attractive: where they apply, if the bet fails, the public pays"}
          - {t: "Irreversibilisation", d: "Going back costs more than carrying on"}
        fleche: "across four coupled registers"
      - titre: "The coupled cost registers (AWP-06)"
        boites:
          - {t: "Energy", d: "Reserved capacity, horizons of several decades", ton: "cout"}
          - {t: "Matter", d: "Materials extracted elsewhere, cooling water", ton: "cout"}
          - {t: "Territory", d: "Land take, networks sized for them", ton: "cout"}
          - {t: "Attention", d: "Solicitation, dependence on interfaces: a possible register, not yet a constituted debt", ton: "cout"}
        fleche: "borne above all by those who did not sign"
      - boites:
          - {t: "Who bears it", d: "The public budgets that guarantee, the territories that host, the populations exposed to mines and waste, the generations that will inherit the equipment, possibly the users whose attention is solicited", ton: "cout"}
    note: "The registers do not add up: they are coupled. Reducing one can shift the load toward the others: establishing this, case by case, is what the grid is for."
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

Technological debt is the cost of digital infrastructures — energy, matter, territory, and possibly attention — turned into debt by three operations: commitment (long-term contracts), public guarantee and the irreversibilisation of infrastructure choices. Attention is still only a possible register: AWP-06 does not treat it as a constituted debt. The concept is formalised by the economist Stéphane Lalut in the working paper [AWP-06](/en/awp/awp-06/) (2026) and belongs to the framework of [anthropy](/en/quest-ce-que-lanthropie/), the hypothesis that social systems displace disorder rather than resolve it.

{{< notion-fiche >}}

## Not to be confused with "technical debt"

On the web, "technological debt" almost always refers to the **technical debt** of software engineering: the accumulation of design compromises in a program — ship fast today, pay for maintenance tomorrow. The metaphor is useful, but it describes a property of code.

Technological debt in the anthropic sense designates something else: an **economic and political** mechanism. It is not lines of code that go into debt, it is societies — when they convert the present cost of their digital infrastructures into commitments that others will bear.

{{< notion-comparaison id="frontiere" >}}

## The mechanism: how a cost becomes a debt

{{< notion-schema id="mecanisme" >}}

Three operations turn an infrastructure cost into a debt:

1. **Commitment** — long-term energy purchase contracts, land leases of several decades, equipment orders that straddle political cycles: the future cost is locked in at the present.
2. **Guarantee** — public schemes that alter the risk profile of private investment to make it attractive to institutional capital (pension funds, insurers, asset managers) (the *derisking* that Daniela Gabor describes for development investment and that AWP-06 transposes to digital infrastructures): where this arrangement applies, if the bet fails, the public bears the cost.
3. **Irreversibilisation** — once the network is built, the territory equipped, the uses installed, going back costs more than continuing: yesterday's choice becomes tomorrow's constraint.

[AWP-06](/en/awp/awp-06/) proposes a testable grid of **four coupled cost registers** — energy, matter, territory, attention: for a given case, one documents what each register commits, and what easing one shifts onto the others. AWP-06 proposes it; it does not yet report a test. These registers do not add up: they couple. Reducing one can shift the burden to the others: establishing this, case by case, is what the grid is for.

## The case of data centers

Data centers make the mechanism visible. Their promise is immaterial — "the cloud" — but their reality engages all four registers at once: reserved electrical capacity and networks sized for several decades, water needs depending on the site, materials extracted elsewhere, land footprints, and, through the uses they serve, demands on users' attention. Public debate focuses on "how much" (kilowatt-hours, cubic metres); technological debt poses the other question: **who has committed, for how long, and who will bear the cost if the promise changes?**

What data centres reserve on the French electricity grid, in figures: the data page [Data centres: do reserved gigawatts foretell consumption?](/en/data-centres-reserved-capacity/) separates what data centres reserve on the grid, what they consume and what RTE, the French transmission system operator, projects; a grid connection reservation is not yet consumption, nor an irreversible commitment.

## Where the concept comes from

{{< canonical-definition >}}

Technological debt is the application of this hypothesis to digital infrastructures: digital technology did not lighten matter, it displaced it — in space (extraction, host territories), in time (commitments, equipment to be dismantled) and onto other groups (exposed populations, users whose attention is solicited). The short definition is available in the [glossary](/en/glossaire/#technological-debt); the neighbouring analysis of the energy transition in [AWP-04](/en/awp/awp-04/); and what these infrastructures may become at the end of their life — a shared inheritance nobody wants, which AWP-06 treats as a candidate negative commons, under conditions — on the page [What are negative commons?](/en/negative-commons/)

## Frequently asked questions

{{< faq-visible >}}

## Further reading

- [AWP-06 — *Digital Infrastructures and Technological Debt*](/en/awp/awp-06/) — the working paper that formalises the concept (DOI: 10.5281/zenodo.20077993, open-access PDF).
- The book [*ANTHROPY – A Big History of Civilization's Hidden Costs*](/en/livres/anthropie-ordre-ici-dette-ailleurs/) (2026, 644 p.) deploys the complete framework of which technological debt is one of the applications.
- [What is anthropy?](/en/quest-ce-que-lanthropie/) — the page of the general concept.
