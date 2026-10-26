---
title: "What is the rebound effect (Jevons paradox)?"
url: /en/rebound-effect/
description: "The rebound effect is the mechanism by which improved energy efficiency, instead of reducing total consumption, tends to increase it. Described by William Stanley Jevons in 1865, it remains the blind spot of efficiency policies."
date: 2026-07-24
lastmod: 2026-10-26
og_title: "The rebound effect (Jevons paradox) — definition and sources — S. Lalut"
faq:
  - question: "What is the rebound effect?"
    answer: "The rebound effect is the mechanism by which energy-efficiency gains are partly or wholly cancelled by an increase in consumption: making a use less energy-intensive also makes it cheaper, hence more used. When the rebound exceeds the gain — total consumption rises — we speak of the Jevons paradox."
  - question: "What is the difference between the rebound effect and the Jevons paradox?"
    answer: "The Jevons paradox is the extreme case of the rebound effect. The rebound effect designates any recovery of consumption that eats into an efficiency gain; there is a Jevons paradox when this recovery exceeds 100% of the gain, that is, when the efficiency improvement ends up consuming more than before. William Stanley Jevons described it as early as 1865 in The Coal Question, about steam engines: more efficient, they made coal consumption explode."
  - question: "What are the forms of the rebound effect?"
    answer: "Three forms are classically distinguished: the direct rebound (a more economical car encourages more driving), the indirect rebound (the money saved funds other, themselves energy-intensive, consumption) and the macroeconomic rebound (efficiency lowers the implicit cost of energy across the whole economy, which stimulates overall production and demand)."
  - question: "Does the rebound effect cancel every efficiency gain?"
    answer: "No — the size of the rebound varies by use, sector and period, and is the subject of an abundant literature. But it is structural, not anecdotal: ignoring the rebound systematically leads to overestimating the energy savings expected from efficiency policies. This is why serious scenarios distinguish efficiency from sufficiency."
  - question: "What is the link between the rebound effect and anthropy?"
    answer: "In the anthropic framework (Stéphane Lalut), the rebound effect is a case of boomerang effect: the efficiency gain produces a local order — less energy per unit — whose cost comes back as a global disorder — more total consumption. The analysis is developed in AWP-04, “Energy transition or entropic transfer?” (2026, DOI 10.5281/zenodo.19269244)."
fiche:  # "The notion at a glance" box (notion-fiche shortcode): restates the page, no new fact
  lignes:
    - t: "Definition"
      d: "The mechanism by which an energy-efficiency gain, instead of reducing total consumption, tends to increase it: what becomes more efficient becomes cheaper, hence more used."
    - t: "Origin"
      d: "William Stanley Jevons, *The Coal Question* (1865), on steam engines; generalised by energy economics (the Khazzoom-Brookes postulate, 1980s)."
    - t: "Not to be confused with"
      d: "The [Jevons paradox](/en/glossaire/#jevons-effect) is the extreme case: the rebound in consumption exceeds the gain. The rebound effect is any rebound that erodes the gain."
    - t: "Example"
      d: "A more fuel-efficient car encourages more driving; heating savings pay for a plane ticket."
    - t: "Limit"
      d: "Its size varies by use, sector and period: it does not cancel every efficiency gain, but ignoring it leads to overestimating the expected savings."
    - t: "Anthropic reading"
      d: "A [boomerang effect](/en/glossaire/#boomerang-effect): the local order (less energy per unit) comes back as global disorder (more total consumption). Analysis developed in [AWP-04](/en/awp/awp-04/)."
      anthropie: true
schemas:  # mechanism diagram (notion-schema shortcode)
  mecanisme:
    titre: "How an efficiency gain comes back as consumption"
    etages:
      - boites:
          - {t: "Efficiency gain", d: "Less energy per unit of service", ton: "ordre"}
        fleche: "the service becomes cheaper"
      - titre: "Three rebound channels"
        boites:
          - {t: "Direct", d: "The more economical use is consumed more"}
          - {t: "Indirect", d: "The money saved funds other consumption"}
          - {t: "Macroeconomic", d: "The implicit cost of energy falls across the economy: production and demand rise"}
        fleche: "the rebounds add up"
      - titre: "Two outcomes"
        boites:
          - {t: "Partial rebound", d: "The rebound erodes the gain: consumption falls less than announced", ton: "cout"}
          - {t: "Jevons paradox", d: "The rebound exceeds the gain: total consumption rises", ton: "cout"}
    note: "A diagram of the mechanism, not to scale: the size of each channel varies by use and sector, and is the subject of a debated literature."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["notion"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/effet-rebond.md"  # fiche de conception (regle 12), refonte de presentation du 26/10/2026
  bloc: "notions"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 50
  nature: "Notion — definition, origin and sources"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Rebound effect"
  court: "Rebound"
  long_en: "Rebound effect"
---

The rebound effect is the mechanism by which improved energy efficiency, instead of reducing total energy consumption, tends to increase it: what becomes more efficient becomes cheaper, hence more used. Described by the economist William Stanley Jevons as early as 1865, it remains the blind spot of most energy-efficiency policies.

{{< notion-fiche >}}

## The origin: Jevons and the steam engine

In *The Coal Question* (1865), Jevons observes a counter-intuitive fact: the steam engines of his day, far more efficient than Newcomen's a century earlier, did not reduce England's coal consumption — they made it explode. The reason is economic: a machine that draws more work from each ton of coal lowers the cost of that work, opens up new profitable uses and multiplies machines. "It is wholly a confusion of ideas to suppose that the economical use of fuel is equivalent to a diminished consumption," he writes. "The very contrary is the truth."

The mechanism was rediscovered and generalised by contemporary energy economics — notably under the name of the Khazzoom-Brookes postulate, after the work of Daniel Khazzoom and Leonard Brookes around the turn of the 1980s.

## The three forms of rebound

{{< notion-schema id="mecanisme" >}}

The literature classically distinguishes three channels:

1. **The direct rebound** — the use that has become more economical is consumed more: a car that uses less fuel encourages more driving, a better-insulated home encourages heating more widely.
2. **The indirect rebound** — the money saved does not evaporate: it funds other consumption, itself carrying energy and matter (the plane ticket paid for by heating savings).
3. **The macroeconomic rebound** — across the whole economy, efficiency lowers the implicit cost of energy, which stimulates production, demand and innovation in new uses.

The size of each channel varies by use and sector; their sum is the subject of an abundant and debated literature. But the direction of the mechanism is hardly in doubt: **ignoring the rebound systematically leads to overestimating the savings expected** from efficiency policies.

## Why the rebound is structural

The rebound effect is not a behavioural anomaly that better information would correct. It follows from the very logic of prices: efficiency makes the energy service cheaper, and a cheaper service is more in demand — from households, from firms, from uses that did not yet exist. That is why efficiency alone, without constraints on volumes, guarantees no fall in total consumption. The historian Jean-Baptiste Fressoz (*Sans transition*, 2024, in French) shows it over two centuries: energies never replaced one another, they **added up** — coal does not replace wood, it is added to it; oil is added to coal; and efficiency gains accompanied, rather than contradicted, this accumulation.

## The anthropic reading: a boomerang effect

The anthropic framework of the economist Stéphane Lalut proposes to read the rebound effect as a case of [boomerang effect](/en/glossaire/#boomerang-effect): the efficiency gain produces a **local order** — less energy per unit produced, an improving balance sheet — whose cost comes back as a **global disorder** — more total consumption, more extraction, more waste.

This reading is developed in [AWP-04 — *Energy transition or entropic transfer?*](/en/awp/awp-04/) (2026), which places the rebound among three transfer mechanisms at work in the energy transition: extraction externalised toward lithium- and cobalt-producing countries, technological waste deferred to the coming decades, and the unaccounted rebound effect. What the three have in common: the disorder the transition claims to eliminate is not resolved, it is **displaced** — in space, in time, or by the detour of volumes.

The rebound effect incidentally shows why the anthropic question — *where does disorder go?* — is not rhetorical: in the case of the rebound, disorder comes back through the least visible channel there is, the aggregation of millions of individually rational decisions.

## Efficiency or sufficiency

The practical consequence is known to serious energy scenarios: efficiency is necessary but not sufficient. Without a mechanism that constrains or steers volumes — sufficiency, caps, pricing — efficiency gains feed demand instead of reducing consumption. The question posed by the anthropic framework goes one step further: when a mechanism does reduce consumption *here*, it remains to check where the cost has moved — toward which territories, which groups, which decades.

## Frequently asked questions

**Rebound effect, Jevons effect, Jevons paradox: are they the same thing?** The rebound effect is the general phenomenon — any recovery of consumption that eats into an efficiency gain. We speak of the Jevons paradox (or effect) in the extreme case where the recovery exceeds the gain: total consumption rises. The short definition is in the [glossary](/en/glossaire/#jevons-effect).

**Does the rebound effect apply outside energy?** Yes. The mechanism is observed wherever an efficiency gain lowers the cost of a use: transport time (speed gains lengthened distances rather than shortening journeys), digital technology (processor efficiency fed the explosion of uses), materials.

**Can the rebound effect be "corrected"?** It can be contained — by coupling efficiency with volume constraints — but not abolished by technology alone: it follows from prices, not from a consumer error. The first step is to count it, which the forecast assessments of efficiency policies still often omit.

## Further reading

- [AWP-04 — *Energy transition or entropic transfer?*](/en/awp/awp-04/) — the working paper that places the rebound effect among the transfer mechanisms of the transition (DOI: 10.5281/zenodo.19269244, open-access PDF).
- [What is anthropy?](/en/quest-ce-que-lanthropie/) — the general framework: local order, displaced disorder, boomerang effect.
- The book [*ANTHROPY – A Big History of Civilization's Hidden Costs*](/en/livres/anthropie-ordre-ici-dette-ailleurs/) (2026, 644 p.) devotes a chapter to energy and to the transfers of the transition.
