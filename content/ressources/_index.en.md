---
title: "Resources — Data, explainers and reference material"
date: 2026-09-28  # mise en ligne de l'index (commit c664bc2) ; la date de mise à jour se déduit des ressources (page-date.html)
description: "The figures of public debate often circulate without their source or method. The dossiers take them back to the official series and texts, recalculate them and say what they show and what they do not. In a separate space, the author’s analytical framework is set out, with its concepts and documentary tools."
url: /en/resources/
# Same mechanism as the French index: presence comes from each page's `ressource` block.
# French-only pages appear here only when they declare `ressource.en_francais` (with `titre_en`),
# and are labelled "in French".
parcours:  # three entry points at the top of the index, one per use (author, 02/11/2026)
  - titre: "Discover"
    texte: "The anthropy hypothesis, its definition and the concepts it draws on."
    lien: "Read the definition"
    url: "/en/quest-ce-que-lanthropie/"
  - titre: "Look up"
    texte: "A figure or a rule: public debt and presidential powers, taken from official series and texts."
    lien: "Go to the dossiers"
    url: "#dette"
  - titre: "Reuse"
    texte: "Figures, data and citation ready to reuse: data pages have their own “Reuse” block."
    lien: "See an example"
    url: "/en/why-does-public-debt-rise/#reutiliser"
blocs:
  - id: dette
    titre: "Public debt"
    barre: "propre"   # each page calls `dossier-dette volet="…"`
    dossier: true     # dossier header in the index (variant A, 06/10/2026)
    pastille: "Public debt dossier"
    bande_donnees: "dossier_dette"
    chapo: "Why it rises, what it costs, who pays, how it compares elsewhere and under what conditions it can come down."
  - id: promesses
    titre: "Presidential promises: from power to results"
    titre_barre: "Presidential promises"   # bar badge: the full title overflows at 390 px
    dossier: true
    chapo: "Who can decide, with whose agreement, within what time — and how to check the result? The French case."
  - id: notions
    # Same decision as the French index (PRO-20261025-225715): framework block; `notions` id kept (published anchor).
    titre: "Anthropy: the author’s analytical framework"
    titre_barre: "The author’s analytical framework"
    chapo: "The author’s hypothesis and its definition, the concepts it draws on, each credited to whoever coined it, and the Register that applies it to deep history."
  - id: guides
    titre: "Figures checked at source"   # replaces "Data and law"; also the pages' membership line; no legal page in English (13/11/2026)
    chapo: "Questions from public debate, examined in official data series: data centres, radioactive waste, energy decoupling, unexpected expenses."
  - id: reperes
    titre: "Ideas and method"
    chapo: "Two texts on method, on writing and on research outside an institution."
---

Pages marked *in French* have no English version yet.
