---
title: "What is social reversibility?"
url: /en/social-reversibility/
description: "Social reversibility is the capacity, assessed before an attempt, to withstand its possible failure without a lasting closure of one's future. Neither a stock nor a flow: a third dimension of inequality — what one can afford to fail."
date: 2026-07-24
lastmod: 2026-10-26
og_title: "What is social reversibility? — definition and sources — S. Lalut"
faq:
  - question: "What is social reversibility?"
    answer: "The capacity, assessed before an attempt, to withstand its possible failure without lasting closure of the set of accessible options. Neither a stock (like wealth) nor a flow (like mobility): a conditional profile of recoverable options. The concept is formalised by economist Stéphane Lalut in AWP-08 (2026, DOI 10.5281/zenodo.21507249)."
  - question: "How does it differ from standard inequality measures?"
    answer: "Income and wealth measure what one owns; mobility, what one crosses. Reversibility measures what one can afford to fail. Two people with similar incomes can face very different futures depending on their capacity to survive error."
  - question: "What does the capacity to bounce back after failure depend on?"
    answer: "On three components that combine: fallback capacity (holding out through the interval after the fall — savings, support networks, institutional safety nets), the institutional price of failure (what a recorded failure costs, in law and in practice) and the readmission environment (the conditions under which doors reopen). The central hypothesis of AWP-08 is their complementarity: a solid fallback protects no one if the trace of failure locks readmission, and open readmission protects no one who cannot hold out through the interval."
  - question: "Why is the second chance not the same for everyone?"
    answer: "Because the price of failure is stratified: two people with similar incomes can face very different futures depending on whether their error is erased or durably recorded in an institutional memory — payment-incident files, default histories, credit records. That inequality appears neither in income statistics nor in mobility statistics."
  - question: "Can social reversibility be measured?"
    answer: "That is the programme opened by AWP-08: a measurement architecture (V = f(C, T, A)), four families of testable propositions and an identification protocol on two dated French institutional reforms — the removal of the 040 indicator from the Banque de France's FIBEN file and the insurance right-to-be-forgotten of the Lemoine Act. It is a refutable framework, not yet an empirical result."
  - question: "Who proposed the concept of social reversibility?"
    answer: "Stéphane Lalut, economist and independent researcher, in the working paper AWP-08 — Social Reversibility as a Dimension of Inequality (2026, DOI 10.5281/zenodo.21507249), eighth of the Anthropie Working Papers. The concept extends the framework of anthropy: the stratified price of failure is a mechanism of social disorder distribution."
fiche:  # "The notion at a glance" box (notion-fiche shortcode): restates the page, no new fact
  lignes:
    - t: "Definition"
      d: "The capacity, assessed *before* an attempt, to withstand its possible failure without lasting closure of the set of accessible options."
    - t: "Origin"
      d: "Proposed by the economist Stéphane Lalut in [AWP-08](/en/awp/awp-08/) (2026), as a third dimension of inequality."
    - t: "Not to be confused with"
      d: "Resilience, an individual psychological capacity to overcome hardship; social reversibility is a structural position that exists before any hardship."
    - t: "Example"
      d: "Two people with identical incomes: one can attempt a business, a fallback exists; for the other, the same failure triggers the gears — overdraft, negative records, housing."
    - t: "Limit"
      d: "A refutable framework, not an empirical result: AWP-08 proposes a measurement architecture and an identification protocol on two dated settings."
    - t: "Anthropic reading"
      d: "The cost of failure does not disappear: it is displaced and distributed, unequally. The stratified price of failure distributes social disorder."
      anthropie: true
schemas:  # mechanism diagram (notion-schema shortcode)
  mecanisme:
    titre: "What makes bouncing back possible: V = f(C, T, A)"
    etages:
      - titre: "Three complementary components"
        boites:
          - {t: "C — Fallback capacity", d: "Holding out through the interval between the fall and the next attempt: savings, support networks, safety nets"}
          - {t: "T — Price of failure", d: "What failure costs in law and in practice, including the trace it leaves"}
          - {t: "A — Readmission", d: "Doors that reopen: employers, lenders, institutions"}
        fleche: "the effect of each depends on the level of the others"
      - boites:
          - {t: "V — Social reversibility", d: "Withstanding a failure without durably closing one's future", ton: "ordre"}
        fleche: "it acts before and after failure"
      - boites:
          - {t: "Before: the decision to try", d: "Whoever knows a failure would be irrecoverable abstains — an abstention invisible in the statistics", ton: "cout"}
          - {t: "After: the price of failure", d: "Stratified by social position; the trace conditions credit, insurance, housing", ton: "cout"}
    note: "A solid fallback is worth little if the trace locks readmission; open readmission protects no one who cannot hold out through the interval."
comparaisons:  # boundary between neighbouring notions (notion-comparaison shortcode)
  dimensions:
    titre: "Three dimensions of inequality"
    colonnes: ["Stocks", "Trajectories", "Reversibility"]
    accent: 3
    lignes:
      - {critere: "What is measured", valeurs: ["What one owns: income, wealth", "What one crosses: mobility between social positions", "What one can afford to fail"]}
      - {critere: "When", valeurs: ["A state, at a date", "A path, between two dates", "Before the attempt"]}
    note: "Two people with identical incomes can have very different reversibility: the difference shows up neither in income statistics nor in mobility statistics."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["notion"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/reversibilite-sociale.md"  # fiche de conception (regle 12), refonte de presentation du 26/10/2026
  bloc: "notions"
  livres: ["la-societe-du-premier-coup"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 30
  nature: "Concept — definition, origins and sources"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Social reversibility"
  court: "Reversibility"
---

Social reversibility is the capacity, assessed *before* an attempt, to withstand its possible failure without lasting closure of the set of accessible options. The concept is proposed by economist Stéphane Lalut in the working paper [AWP-08](/en/awp/awp-08/) (2026) as a third dimension of inequality, alongside stocks (income, wealth) and trajectories (social mobility).

{{< notion-fiche >}}

## What one can afford to fail

Inequality is usually measured by what one owns — income, wealth — or by what one crosses — mobility between social positions. A third measure is missing: what a person can afford to **fail** without durably closing their future.

Two people with identical incomes do not stand in the same relation to risk. One can leave a job, attempt a business, return to study: if the attempt fails, a fallback exists — savings, a support network, a way back. The other plays every attempt double-or-nothing: the same failure triggers the gears — overdraft, negative records, housing, reputation. The first has high reversibility; the second, low. This difference shows up neither in income statistics nor in mobility statistics — yet it governs who gets to try.

{{< notion-comparaison id="dimensions" >}}

## The memory of failures

The pivot of the framework is the **trace**: the memory institutions keep of a failure, and the readmission regime it governs.

A payment incident, a business default, a recorded flag do not disappear with the event: they are written down — files, histories, scores — and condition future access to credit, insurance, housing, sometimes employment. Institutions choose how long they remember. In the United States, bankruptcy law is explicitly built around a *fresh start*, and the Fair Credit Reporting Act caps how long most negative items may remain on a credit report. France has recently shortened two of its own memories: in 2021 the Banque de France removed the 040 indicator from its FIBEN file, which for three years had flagged directors who had been through a judicial liquidation; and the Lemoine Act (2022) created an insurance right-to-be-forgotten, barring the declaration of a past cancer beyond a set delay. In each case, a society decided to *shorten the memory of failure* — that is, to increase the reversibility of those it concerned.

## Bouncing back: structure, not just psychology

The common discourse on bouncing back after failure is almost entirely psychological: resilience, mindset, "turning failure into learning". That grid leaves the essential in the dark: **bouncing back requires material and institutional conditions** that willpower does not replace.

{{< notion-schema id="mecanisme" >}}

The framework of AWP-08 names them. Bouncing back requires:

1. **fallback capacity** (C) — holding out through the interval between the fall and the next attempt: savings, support networks, institutional safety nets;
2. **a bearable price of failure** (T) — what failure costs in law and in practice, including the trace it leaves;
3. **a readmission environment** (A) — doors that reopen: employers, lenders, institutions willing to consider a marked file.

The framework's own hypothesis is the **complementarity** of these components: the effect of each depends on the level of the others. A solid fallback is worth little if the trace locks readmission; open readmission protects no one who cannot hold out through the interval. This is why second-chance policies acting on a single component — psychological support without the safety net, or record-clearing without the fallback — so often disappoint.

Only one of these components can be measured in public statistics today, and only in part: the financial capacity to absorb a shock. The data page [Who can cope with an unexpected expense?](/en/who-can-cope-with-an-unexpected-expense/) shows that it varies sharply with household composition, including above the poverty threshold.

## An inequality that governs attempts

Social reversibility does not act only *after* failure: it acts *before*, on the very decision to try. Whoever knows that a failure would be unrecoverable abstains — and that abstention is invisible in the statistics, since nothing happened. A low-reversibility society does not merely produce costlier failures: it produces fewer attempts, and reserves them for those who can afford to fail.

This is the link with the general framework of [anthropy](/en/quest-ce-que-lanthropie/): the cost of failure does not disappear, it is displaced and distributed — unequally. [AWP-01](/en/awp/awp-01/) states the hypothesis of disorder displacement; [AWP-07](/en/awp/awp-07/) formalises its loop (see [What is the anthropic loop?](/en/anthropic-loop/)); [AWP-08](/en/awp/awp-08/) provides its micro-institutional counterpart: the stratified price of failure is a mechanism of social disorder distribution.

## Frequently asked questions

**Is social reversibility a synonym for resilience?** No. Resilience describes an individual psychological capacity to overcome hardship. Social reversibility describes a structural position — fallback, price, readmission — that exists before any hardship and independently of a person's psychological dispositions.

**Is it measurable?** That is the programme opened by AWP-08: a measurement architecture (*V = f(C, T, A)*), four families of testable propositions, an identification protocol on two dated institutional reforms (the FIBEN 040 removal, the Lemoine Act's right-to-be-forgotten). The paper presents itself as a refutable framework, not an empirical result.

**Why "reversibility"?** Because the decisive question is that of return: an error is reversible when the options it closes can be recovered. Irreversibility — the lasting closure of one's future — is the true social cost of failure, and it is unequally distributed.

## Further reading

- [AWP-08 — *Social Reversibility as a Dimension of Inequality*](/en/awp/awp-08/) — the working paper that formalises the concept (DOI: 10.5281/zenodo.21507249, open-access PDF).
- [*La Société du premier coup*](/livres/la-societe-du-premier-coup/) — the book that turns the question into narrative, through concrete cases and without formal apparatus. **In French**; its sourced figures are gathered on its [companion page](/premier-coup/).
- [AWP-07 — *The Anthropic Loop*](/en/awp/awp-07/) — the general mechanism of which reversibility is the micro-institutional counterpart.
- [What is anthropy?](/en/quest-ce-que-lanthropie/) — the concept page, and the [glossary](/en/glossaire/) of the framework.
