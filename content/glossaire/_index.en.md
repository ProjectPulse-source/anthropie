---
date: 2026-04-15  # premier commit de la page (git log --follow)
lastmod: 2026-11-16
journal:  # révisions qui changent la lecture de la page
  - {date: 2026-11-05, texte: "Correction: the “Anthropic loop” entry now gives the AWP-07 definition (five states, from displacement to bifurcation); the return toward cognition becomes one case of it, specific to the digital metaprogramme."}
  - {date: 2026-11-05, texte: "Corrections: Jevons effect (extreme case of the rebound effect), boomerang effect (credit to Ulrich Beck, balance not asserted), registers of debt (a possible displacement, to be established case by case)."}
  - {date: 2026-11-16, texte: "Source review: definitions aligned with the deposited working papers (including saturation, and the anthropic loop following the revised AWP-07); “entropic externalisation” presented as an inquiry the hypothesis directs, without prejudging its outcome."}
title: "Glossary"
og_title: "Glossary — the concepts, defined and sourced — S. Lalut"
description: "Key terms of the anthropic framework."
og_image: "images/og-glossaire.en.jpg"
og_image_alt: "Glossary — Anthropy. Order here. Debt elsewhere."
carte:  # vocabulary map (glossaire-carte shortcode): sets named by the introduction; every anchor must exist (errorf at build)
  titre: "Map of the vocabulary"
  coeur: {id: "anthropy", t: "Anthropy", d: "Social systems displace disorder rather than resolve it."}
  groupes:
    - t: "The mechanism"
      role: "Transfer and its three dimensions: where disorder goes."
      ton: "ordre"
      termes:
        - {id: "anthropic-transfer", t: "Anthropic transfer"}
        - {id: "spatial-transfer", t: "Spatial transfer"}
        - {id: "temporal-transfer", t: "Temporal transfer"}
        - {id: "social-transfer", t: "Social transfer"}
        - {id: "local-order", t: "Local order"}
        - {id: "displacement-space", t: "Displacement space"}
    - t: "Thresholds and return"
      role: "When the displacement space saturates and disorder comes back."
      ton: "cout"
      termes:
        - {id: "saturation", t: "Saturation"}
        - {id: "rising-marginal-cost", t: "Rising marginal cost"}
        - {id: "boomerang-effect", t: "Boomerang effect"}
        - {id: "jevons-effect", t: "Jevons effect"}
        - {id: "anthropic-loop", t: "Anthropic loop"}
    - t: "Configurations"
      role: "The historical arrangements of transfer, over 3.3 million years."
      termes:
        - {id: "configuration", t: "Configuration"}
        - {id: "metaprogramme", t: "Metaprogramme"}
        - {id: "register-of-offloaded-costs", t: "Register of Offloaded Costs"}
    - t: "The posture"
      role: "Before any stable order, ask where the disorder flows."
      termes:
        - {id: "discipline-of-attention", t: "Discipline of attention"}
    - t: "Applications"
      large: true
      role: "The framework applied to a field: digital technology, legacies, inequality, knowledge."
      termes:
        - {id: "technological-debt", t: "Technological debt"}
        - {id: "coupled-cost-registers", t: "Coupled cost registers"}
        - {id: "derisking", t: "Derisking"}
        - {id: "negative-commons", t: "Negative commons"}
        - {id: "social-reversibility", t: "Social reversibility"}
        - {id: "epistemic-order", t: "Epistemic order"}
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["notion"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/glossaire.md"  # fiche de conception (regle 12), refonte de presentation du 26/10/2026
  bloc: "notions"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 10
  nature: "Definitions"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Glossary"
---

This glossary brings together the terms specific to the anthropic framework. It is not a general dictionary: each entry gives the meaning that a term, coined by the framework or borrowed from other authors, takes in the anthropic hypothesis. Definitions refer to the *Anthropie Working Papers* and to the book [*ANTHROPIE — Ordre ici. Dette ailleurs*](/livres/anthropie-ordre-ici-dette-ailleurs/) (in French), which develop them; two names, flagged in their entry, are specific to this glossary.

Anthropy rests on a single hypothesis — social systems displace disorder rather than resolve it — and the terms below constitute its working vocabulary. They are organised around three sets — the **mechanism** (anthropic transfer and its three dimensions), the **thresholds** (saturation, rising marginal cost, boomerang effect), and the **configurations** (historical arrangements of transfer over 3.3 million years) — to which is added an analytical posture: the **discipline of attention**.

{{< glossaire-carte >}}

<dl>

<div class="glossaire-entry" id="anthropy">
<dt>Anthropy</dt>
<dd>The hypothesis that social systems displace disorder rather than resolve it. On this hypothesis, every observable order presupposes disorder exported elsewhere; AWP-01 specifies that it does not postulate that everything is transfer, but that every observable stability deserves to be questioned about its offloaded costs. This displacement operates along three axes — spatial, temporal, social — which, in many configurations, combine and reinforce one another. Hypothesis proposed by the economist Stéphane Lalut (book <em>ANTHROPIE</em>, 2025; AWP series, 2026). See <a href="/en/quest-ce-que-lanthropie/">What is anthropy?</a></dd>
</div>

<div class="glossaire-entry" id="anthropic-transfer">
<dt>Anthropic transfer</dt>
<dd>The mechanism by which disorder is displaced from one place, one time, or one group to another. Transfer may be spatial (toward other territories), temporal (toward the future), or social (toward captive groups). It is the central operation of the anthropic framework: what other frameworks classify separately as externality, debt, inequality, or risk is read here as variations of a single mechanism. See <a href="/en/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="spatial-transfer">
<dt>Spatial transfer (entropic externalisation)</dt>
<dd>The spatial form of anthropic transfer (<a href="/en/awp/awp-01/">AWP-01</a>); the name "entropic externalisation" is specific to this glossary. Disorder is displaced toward other territories — remote extraction, offshored pollution, territorial relegation. Metropolises shine, peripheries pay: the digital consumption of the North rests on the extraction of cobalt and rare earths in the global South. See <a href="/en/awp/awp-04/">AWP-04</a>.</dd>
</div>

<div class="glossaire-entry" id="temporal-transfer">
<dt>Temporal transfer (anthropic debt)</dt>
<dd>The temporal form of transfer (<a href="/en/awp/awp-01/">AWP-01</a>); the name "anthropic debt" is specific to this glossary. Disorder is deferred to the future — public debt, underinvestment, deferred maintenance. Temporal transfer converts a present cost into a future debt: the generations that inherit the disorder did not contract the loan. See <a href="/en/awp/awp-03/">AWP-03</a>.</dd>
</div>

<div class="glossaire-entry" id="social-transfer">
<dt>Social transfer</dt>
<dd>The social form of anthropic transfer. Disorder is displaced toward groups least able to escape it — precarisation, exclusion, asymmetric cost shifting. Social transfer is measured by the unequal capacity of groups to refuse, negotiate, or flee the burden imposed on them. See <a href="/en/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="local-order">
<dt>Local order</dt>
<dd>A social configuration resulting from the displacement of disorder beyond the perimeter under consideration. The hypothesis leads one to look, behind a local order, for an elsewhere that would absorb its cost and whose recipients would remain out of frame. This search does not prejudge its outcome: inquiry may conclude that no displacement is established (see the entry <a href="#anthropy">Anthropy</a>). See <a href="/en/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="discipline-of-attention">
<dt>Discipline of attention</dt>
<dd>The analytical posture proposed by anthropy: when confronted with any stable order, ask where disorder flows. It leads to questioning the blind spots of apparent stability. The discipline of attention does not consist in abstractly denouncing the disorder of the world, but in identifying, in each concrete configuration, the mechanism that renders transfer opaque. See <a href="/en/awp/awp-01/">AWP-01</a>.</dd>
</div>

<div class="glossaire-entry" id="saturation">
<dt>Saturation</dt>
<dd>The state of a displacement space that can no longer absorb disorder quietly: its capacity is reached, or the transfer becomes legible and contested (<a href="/en/awp/awp-07/">AWP-07</a>, saturation conditions). <a href="/en/awp/awp-02/">AWP-02</a> had given a first sketch: a space saturates when exporting disorder costs more than managing it on the spot, which two criteria signal, rising marginal cost and the boomerang effect; AWP-07 places the first on the side of the system that displaces disorder and makes the second a return, which comes after saturation. When no space — geographical, social, temporal, cognitive — can absorb the burden any longer, complexity holds, according to AWP-02, only through an internal tension bound to break.</dd>
</div>

<div class="glossaire-entry" id="rising-marginal-cost">
<dt>Rising marginal cost</dt>
<dd>The first criterion of saturation according to AWP-02: transfer becomes increasingly costly as the displacement space fills up, each unit of exported disorder costing more than the last. AWP-07 makes it a condition on the side of the system that displaces disorder, distinct from the saturation of the space that receives it. See <a href="/en/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="boomerang-effect">
<dt>Boomerang effect</dt>
<dd>The second criterion of saturation according to AWP-02: displaced disorder returns to the system that displaced it, sometimes in a form more costly than the initial disorder; AWP-07 makes it a return, which comes after saturation. Climate change is its planetary illustration: the disorder exported into the atmosphere over two centuries of industrialisation returns as costs that the original export had not counted. In the sense of risks returning to those who produce them, the notion comes from Ulrich Beck (<em>Risikogesellschaft</em>, 1986; <em>Risk Society</em>, 1992 in English). See <a href="/en/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="jevons-effect">
<dt>Jevons effect (Jevons paradox)</dt>
<dd>The extreme case of the rebound effect: increased use takes back more than the efficiency gain, and total consumption of the resource rises instead of falling (Jevons, <em>The Coal Question</em>, 1865). The anthropic framework can read it as a boomerang effect: according to AWP-04, the efficiency gains of the energy transition open new spaces of consumption, hence new transfers. See the page <a href="/en/rebound-effect/">What is the rebound effect?</a> and <a href="/en/awp/awp-04/">AWP-04</a>.</dd>
</div>

<div class="glossaire-entry" id="metaprogramme">
<dt>Metaprogramme</dt>
<dd>The contemporary configuration of anthropic transfer operating at a digital and planetary scale. The metaprogramme displaces disorder at unprecedented speed and scale. It articulates two formerly distinct dynamics: an energy and material debt projected toward the future, and a cognitive capture operating in the present — attention siphoned, meaning diluted, subjectivities contracted. See <a href="/en/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="anthropic-loop">
<dt>Anthropic loop</dt>
<dd>A sequence of five conditional states describing what becomes of the disorder a social system makes others bear: displacement toward a receptacle (E1), accumulation (E2), saturation (E3), a possible return toward the emitting system (E4), bifurcation (E5) — new displacement, reconfiguration or partial collapse. After displacement, no passage is compulsory. Formalised in <a href="/en/awp/awp-07/">AWP-07</a>: this definition follows its revised version, not yet deposited; the version deposited in July 2026 treats accumulation as automatic and states the cycle without conditions. Presented on the page <a href="/en/anthropic-loop/">What is the anthropic loop?</a>. In the digital metaprogramme, the return can target the very capacity that made displacement possible, cognition: captured attention, delegated judgement. It is then a return, not a fourth axis of transfer. See also <a href="/en/quest-ce-que-lanthropie/">What is anthropy?</a> and <a href="/en/awp/awp-06/">AWP-06</a>.</dd>
</div>

<div class="glossaire-entry" id="epistemic-order">
<dt>Epistemic order</dt>
<dd>The system of hierarchies of legitimacy, criteria of validity, and circuits of recognition produced by the academic field. On AWP-05's hypothesis, this order presupposes an epistemic disorder exported to its margins. The institution simultaneously produces legitimate selection and cost transfer: certain questions, certain formats, certain postures are relegated through a mechanism analogous to anthropic transfer. See <a href="/en/awp/awp-05/">AWP-05</a>.</dd>
</div>

<div class="glossaire-entry" id="displacement-space">
<dt>Displacement space</dt>
<dd>A place, time, or social group towards which disorder is transferred. A displacement space may be geographical, temporal (the future), or social (a captive group). "Whenever a displacement space saturates, flight reinvents itself elsewhere: more abstract, more distant, less readily politicised." See <a href="/en/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="configuration">
<dt>Configuration</dt>
<dd>A particular historical arrangement of anthropic transfer mechanisms. The framework identifies seven major configurations over 3.3 million years. Transfer does not repeat identically: its forms migrate. From the founding programmes to the Neolithic trap, transfer remains primarily spatial; from ancient systems to transcontinental networks, the social takes over; from industrialisation to the digital metaprogramme, the temporal and cognitive prevail (AWP-02, version 1.1). The seven ages of the book follow another periodisation, in which the spatial dominates up to the ancient systems. See <a href="/en/awp/awp-02/">AWP-02</a>.</dd>
</div>

<div class="glossaire-entry" id="derisking">
<dt>Derisking</dt>
<dd>Mechanism by which the state alters the risk profile of a private investment to make it attractive to institutional capital (Daniela Gabor). Derisking operates the transformation of present cost into future debt: public guarantees, long-term commitment contracts, stabilisation devices. A conceptual pivot for understanding how the investability of digital infrastructures is constructed at the price of technological debt. See <a href="/en/awp/awp-06/">AWP-06</a>.</dd>
</div>

<div class="glossaire-entry" id="technological-debt">
<dt>Technological debt</dt>
<dd>The cost of digital infrastructures — energy, matter, territory, and perhaps attention — turned into debt by three operations: commitment (long-term contracts), public guarantee and the irreversibilisation of infrastructure choices. Attention is a possible register there, not a debt already constituted. Not to be confused with the "technical debt" of software engineering, which designates accumulated design compromises in a program: technological debt in the anthropic sense is an economic and political mechanism, not a property of code. Concept formalised by Stéphane Lalut (AWP-06, 2026). See <a href="/en/technological-debt/">What is technological debt?</a>, <a href="/en/awp/awp-06/">AWP-06</a> and the book <a href="/livres/anthropie-ordre-ici-dette-ailleurs/"><em>ANTHROPIE — Ordre ici. Dette ailleurs</em></a> (in French).</dd>
</div>

<div class="glossaire-entry" id="negative-commons">
<dt>Negative commons</dt>
<dd>Notion developed by Alexandre Monnin, with Emmanuel Bonnet and Diego Landivar (<em>Héritage et fermeture</em>, 2021), from an expression Monnin traces back to Maria Mies and Veronika Bennholdt-Thomsen (2001), to designate what we inherit without having chosen: waste, ruins, obsolete infrastructures. Negative commons are not goods voluntarily shared, but burdens transmitted — an anthropic transfer crystallised in the materiality of the world. Monnin places digital technologies among candidate negative commons; AWP-06 analyses some digital infrastructures as candidates, under conditions. See the page <a href="/en/negative-commons/">What are negative commons?</a> and <a href="/en/awp/awp-06/">AWP-06</a>.</dd>
</div>

<div class="glossaire-entry" id="social-reversibility">
<dt>Social reversibility</dt>
<dd>The capacity, assessed before an attempt, to withstand its possible failure without a lasting closure of one's future. Neither a stock nor a flow: a third dimension of inequality — what one can afford to fail. See <a href="/en/social-reversibility/">What is social reversibility?</a></dd>
</div>

<div class="glossaire-entry" id="coupled-cost-registers">
<dt>Coupled cost registers</dt>
<dd>AWP-06's central contribution: a testable grid of four registers — energy, matter, territory, attention — for examining how digital infrastructure may simultaneously displace disorder along several irreducible axes. These registers do not add up: they couple. Reducing one may shift the burden onto the others: that is what the grid asks to be established, case by case. See <a href="/en/awp/awp-06/">AWP-06</a>. Not to be confused with the <em>Register of Offloaded Costs</em>, which is a chronology rather than an analytical grid.</dd>
</div>

<div class="glossaire-entry" id="register-of-offloaded-costs">
<dt>Register of Offloaded Costs</dt>
<dd>The documentary apparatus of the book <em>ANTHROPY – A Big History of Civilization's Hidden Costs</em> (2026; French original 2025): a chronology of 168 milestones, from the first stone tools (≈ 3.3 million years ago) to contemporary algorithms, documenting for each innovation the order created and the debt displaced, with the categories of the transfer. Browsable online, all 168 milestones: <a href="/en/register-of-offloaded-costs/">The Register of Offloaded Costs</a>. Not to be confused with the <a href="#coupled-cost-registers">coupled cost registers</a> of AWP-06, which are an analytical grid rather than a chronology.</dd>
</div>

</dl>
