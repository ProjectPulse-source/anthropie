---
title: "About"
aggregates: [publications, livres, awp]  # lastmod du sitemap = la fiche la plus recente de ces sections (layouts/sitemap.xml)
description: "Stéphane Lalut — Economist, independent researcher and essayist. Author of the framework of anthropy."
# Même montage que la version FR : HOOK puis RAISON DE CLIQUER.
# La fiche NATIVE de la langue l'emporte quand elle existe — aujourd'hui
# ANTHROPY seulement ; les trois autres restent des fiches FR et portent
# automatiquement le marqueur « In French », comme sur /en/books/.
# Pas d'annee dans `meta` : decision auteur 2026-08-09. Le millesime de
# l'edition courante compressait une decennie de travail en deux ans, et il
# aurait fallu arbitrer entre date d'ecriture, premiere edition et depot —
# trois annees differentes selon la source pour L'Odyssee. Le rang d'edition
# (« 3e edition », « Nouvelle edition ») dit la duree sans nommer d'annee. Les
# dates exactes restent ou elles font foi : datePublished schema.org de chaque
# fiche livre, data/works.yaml, Wikidata.
# Presence comes from the repository (content/livres/, grouped by `serie`) —
# nothing to add here for a new title to show up. Only the editorial copy lives
# here. `meta` is optional: without it the tile reuses the page count of the
# book page ("140 pages"). A missing `line` never hides the book; it raises a
# build warning.
wall_corpus_label: "The anthropic corpus"
wall_autres_label: "Other works"  # same name as /en/books/ and the home page (author, 2026-10-01)
wall_lignes:
  anthropie-ordre-ici-dette-ailleurs:
    line: "No society resolves disorder: it displaces it — elsewhere, later, onto others. The book that lays out the framework and tests it against long-range history."
  dette-publique-qui-paie-vraiment:
    line: "The real question is not who repays the debt, but who absorbs its cost. The book follows the chain, from today's taxpayers to generations that never voted."
  la-societe-du-premier-coup:
    line: "Everyone falls. The privilege is that the falls do not stick. The book counts what inequality measures leave out of frame: how many attempts a trajectory actually allows."
  un-president-peut-il-tenir-ses-promesses:
    line: "A president can decide and nothing happens. A four-zone grid to tell, before voting, where a promise breaks — and afterwards, who could not from who did not try."
  lodyssee-des-idees:
    meta: "New edition"
    line: "The history of ideas is not a chronological parade: it is a network. 250 ports of call and seven itineraries, from the dawn of humanity to artificial intelligence."
  livresque-des-mots:
    meta: "3rd edition"
    line: "An anthology with no classification, neither alphabetical nor thematic: disorder is the principle. Twenty-five centuries of voices to be read like a novel, with an index of authors to find them again."
# Les fiches publications n'ont pas de version anglaise (choix éditorial) : le
# mur lit toujours le corpus FR. Seul l'objet est traduit ; le titre révélé au
# survol reste dans la langue de l'article.
presse_objets:
  en-attendant-nadeau-muhlhoff: "AI and democracy"
  sociologie-du-travail-pugh: "Connective labour"
  en-attendant-nadeau-gefen: "History of AI"
  en-attendant-nadeau-parler-sans-savoir-a-qui: "Books and algorithms"
  rfse-lemoine-chasseurs-detats: "Sovereign debt"
  revue-projet-commune-republique: "Municipalities"
  lectures-ridde-financiarisation-sante: "Colonial health"
  nonfiction-vuillemey: "Limited liability"
  la-grande-conversation-dette-francaise: "French debt"
  en-attendant-nadeau-neel-chavez: "Material planning"
  en-attendant-nadeau-welgryn-alves-da-costa: "The AI narrative"
  lectures-kaba-main-esprit: "Bhopal workers"
  en-attendant-nadeau-carton-malm: "Climate overshoot"
  alternatives-economiques-teletravail: "Remote work"
  la-vie-des-idees-khalili: "Maritime logistics"
  le-temps-votations: "Swiss votes"
  terrestres-sous-le-cloud-la-fournaise: "Data centres"
  nonfiction-fressoz: "Energy transition"
  en-attendant-nadeau-christophers: "Profit and transition"
statut: "Economist · independent researcher · essayist"
textes_choisis:  # maquette D2 (25/11/2026) : la phrase est RECOPIÉE du chapô de la fiche (phrase: 2 = seconde phrase)
  - {slug: rfse-lemoine-chasseurs-detats, type: Recension}
  - {slug: sociologie-du-travail-pugh, type: Recension}
  - {slug: terrestres-sous-le-cloud-la-fournaise, type: Article}
  - {slug: la-vie-des-idees-khalili, type: Recension, phrase: 2}
  - {slug: alternatives-economiques-teletravail, type: Article}
  - {slug: en-attendant-nadeau-muhlhoff, type: Recension}
---

<blockquote class="apropos-question">“When a system appears to solve a problem, what costs can it displace, and onto whom?”</blockquote>

This question runs through his work. He has made it a framework of analysis, the framework of anthropy: the hypothesis that social systems displace disorder rather than resolve it — in space, in time, or between social groups. From public debt to inequality, from work to technological change, his research explores what the solutions to collective problems make less visible.

{{< identifiants >}}

<div class="apropos-tete"><h2 id="in-the-press-and-in-journals" class="apropos-tete__titre section-title">One question, many fields</h2></div>

{{< textes-choisis >}}

<div class="apropos-tete"><h2 id="author" class="apropos-tete__titre section-title">Books</h2></div>

{{< mur-livres >}}

<div class="apropos-tete"><h2 id="researcher" class="apropos-tete__titre section-title">Research</h2></div>

<p id="anthropie-working-papers" class="apropos-nature"><strong>Anthropie Working Papers</strong> — open-access working papers deposited on Zenodo with a DOI, not peer-reviewed.</p>

{{< liste-awp n="3" >}}

<p id="method" class="apropos-nature"><strong>Method</strong> — The work published on this site rests on original sources, reproducible calculations and documented verification procedures. Artificial intelligence tools are used for some documentary processing, especially when the volume of texts to examine exceeds the means of individual research; where their use bears on how results are produced or on what they can claim, each page's method says so. The adversarial checking mentioned on the pages consists of counter-analyses carried out by language models, arbitrated in writing point by point against the original sources: it is not peer review. The author takes editorial responsibility for the analyses published.</p>

<p class="apropos-lien"><a href="/en/serie-awp/">The working papers&nbsp;→</a><a href="/en/independent-researcher/">Independent researcher&nbsp;→</a></p>

<div class="apropos-tete"><h2 id="contact" class="apropos-tete__titre section-title">Contact</h2></div>

<p class="apropos-contact"><a class="btn btn--secondary" href="/en/contact/">Contact me&nbsp;→</a></p>
