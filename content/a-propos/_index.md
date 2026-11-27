---
title: "À propos"
aggregates: [publications, livres, awp]  # lastmod du sitemap = la fiche la plus recente de ces sections (layouts/sitemap.xml)
description: "Stéphane Lalut — Économiste, chercheur indépendant et essayiste. Auteur du cadre anthropique."
# ---------------------------------------------------------------------------
# MUR AUTEUR — vignette, titre et lien viennent de content/livres/<slug>.md
# (source unique, via partials/livres-merged.html : la fiche native de la langue
# l'emporte, sinon repli FR). Seules la mention d'édition et la ligne éditoriale
# vivent ici, car « À propos » cadre les livres autrement que leur fiche.
#
# Chaque `line` se monte en deux temps : un HOOK (une loi contre-intuitive qui
# agrippe le lecteur qualifié et filtre l'autre) puis une RAISON DE CLIQUER (ce
# que la fiche apporte de plus). Jamais de définition de genre en tête. Test de
# survie : aucune de ces lignes ne fonctionne si on change de livre.
# ---------------------------------------------------------------------------
# Pas d'annee dans `meta` : decision auteur 2026-08-09. Le millesime de
# l'edition courante compressait une decennie de travail en deux ans, et il
# aurait fallu arbitrer entre date d'ecriture, premiere edition et depot —
# trois annees differentes selon la source pour L'Odyssee. Le rang d'edition
# (« 3e edition », « Nouvelle edition ») dit la duree sans nommer d'annee. Les
# dates exactes restent ou elles font foi : datePublished schema.org de chaque
# fiche livre, data/works.yaml, Wikidata.
# La PRÉSENCE d'un livre vient du dépôt (content/livres/, groupé par `serie`) :
# rien à ajouter ici pour qu'un nouveau titre apparaisse. Seul l'ÉDITORIAL vit
# ici. `meta` est facultatif — sans lui, la pagination de la fiche est reprise
# (« 140 pages ») ; ne le poser que pour dire un rang d'édition. Une `line`
# manquante n'efface pas le livre : elle déclenche un avertissement au build.
wall_corpus_label: "Corpus anthropique"
wall_autres_label: "Autres ouvrages"  # même nom que /livres/ et l'accueil (auteur, 01/10/2026)
wall_lignes:
  anthropie-ordre-ici-dette-ailleurs:
    line: "Aucune société ne résout le désordre : elle le déplace — ailleurs, plus tard, sur d'autres. L'ouvrage qui pose le cadre et le met à l'épreuve de l'histoire longue."
  dette-publique-qui-paie-vraiment:
    line: "La vraie question n'est pas « qui rembourse ? » mais « qui absorbe le coût ? ». Le livre suit la chaîne, du contribuable d'aujourd'hui aux générations qui n'ont pas voté."
  la-societe-du-premier-coup:
    line: "Tout le monde tombe. Le privilège, c'est que les chutes ne collent pas. Le livre compte ce que les mesures d'inégalité laissent hors champ : le nombre d'essais dont dispose une trajectoire."
  un-president-peut-il-tenir-ses-promesses:
    line: "Un président peut décider sans que rien ne se fasse. Une grille en quatre zones pour savoir, avant de voter, où une promesse casse — et après, distinguer qui n'a pas pu de qui n'a pas essayé."
  lodyssee-des-idees:
    meta: "Nouvelle édition"
    line: "L'histoire des idées n'est pas un défilé chronologique : c'est un réseau. 250 escales et sept chemins de lecture, de l'aube de l'humanité à l'intelligence artificielle."
  livresque-des-mots:
    meta: "3ᵉ édition"
    line: "Une anthologie sans classement, ni alphabétique ni thématique : le désordre est le principe. Vingt-cinq siècles de voix à lire comme un roman, et un index des auteurs pour les retrouver."
# ---------------------------------------------------------------------------
# MUR PRESSE — un ou deux mots nommant CE DONT parle le texte. Ce n'est pas le
# thème : le thème est invariant sur les dix-sept textes (le déplacement du
# coût) et donnerait dix-sept étiquettes identiques. C'est l'objet qui varie, et
# c'est lui qui rend le mur lisible d'un coup d'œil.
# Ajouter une ligne ici à chaque nouvelle fiche content/publications/ ; sans
# entrée, la tuile retombe sur le nom de la revue.
# ---------------------------------------------------------------------------
presse_objets:
  en-attendant-nadeau-muhlhoff: "IA et démocratie"
  sociologie-du-travail-pugh: "Travail de connexion"
  en-attendant-nadeau-gefen: "Histoire de l'IA"
  en-attendant-nadeau-parler-sans-savoir-a-qui: "Livre et algorithmes"
  rfse-lemoine-chasseurs-detats: "Dette souveraine"
  revue-projet-commune-republique: "Communes"
  lectures-ridde-financiarisation-sante: "Santé coloniale"
  nonfiction-vuillemey: "Responsabilité limitée"
  la-grande-conversation-dette-francaise: "Dette française"
  en-attendant-nadeau-neel-chavez: "Planification matérielle"
  en-attendant-nadeau-welgryn-alves-da-costa: "Récit de l'IA"
  lectures-kaba-main-esprit: "Ouvriers de Bhopal"
  en-attendant-nadeau-carton-malm: "Dépassement climatique"
  alternatives-economiques-teletravail: "Télétravail"
  la-vie-des-idees-khalili: "Logistique maritime"
  le-temps-votations: "Votations suisses"
  terrestres-sous-le-cloud-la-fournaise: "Data centers"
  nonfiction-fressoz: "Transition énergétique"
  en-attendant-nadeau-christophers: "Profit et transition"
statut: "Économiste · chercheur indépendant · essayiste"
textes_choisis:  # maquette D2 (25/11/2026) : la phrase est RECOPIÉE du chapô de la fiche (phrase: 2 = seconde phrase)
  - {slug: rfse-lemoine-chasseurs-detats, type: Recension}
  - {slug: sociologie-du-travail-pugh, type: Recension}
  - {slug: terrestres-sous-le-cloud-la-fournaise, type: Article}
  - {slug: la-vie-des-idees-khalili, type: Recension, phrase: 2}
  - {slug: alternatives-economiques-teletravail, type: Article}
  - {slug: en-attendant-nadeau-muhlhoff, type: Recension}
---

<blockquote class="apropos-question">«&nbsp;Quand un système paraît résoudre un problème, quels coûts peut-il déplacer, et sur qui&nbsp;?&nbsp;»</blockquote>

Cette question traverse ses travaux. Il en a fait un cadre d'analyse, le cadre anthropique&nbsp;: l'hypothèse que les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent — dans l'espace, dans le temps, ou entre groupes sociaux. De la dette publique aux inégalités, du travail aux transformations technologiques, ses recherches explorent ce que les solutions apportées aux problèmes collectifs rendent moins visible.

{{< identifiants >}}

<div class="apropos-tete"><h2 id="dans-la-presse-et-les-revues" class="apropos-tete__titre section-title">Une même question, des terrains différents</h2></div>

{{< textes-choisis >}}

<div class="apropos-tete"><h2 id="auteur" class="apropos-tete__titre section-title">Livres</h2></div>

{{< mur-livres >}}

<div class="apropos-tete"><h2 id="chercheur" class="apropos-tete__titre section-title">Recherche</h2></div>

<p id="anthropie-working-papers" class="apropos-nature"><strong>Anthropie Working Papers</strong> — documents de travail en accès ouvert, déposés sur Zenodo avec DOI, sans évaluation par les pairs.</p>

{{< liste-awp n="3" >}}

<p id="methode" class="apropos-nature"><strong>Méthode</strong> — Les travaux publiés sur ce site s'appuient sur les sources originales, des calculs reproductibles et des procédures de vérification documentées. Des outils d'intelligence artificielle servent à certains traitements documentaires, notamment lorsque le volume des textes à examiner dépasse les moyens d'une recherche individuelle&nbsp;; la méthode de chaque page précise leur intervention lorsqu'elle touche à la production ou à la portée des résultats. Les vérifications contradictoires mentionnées sur les pages sont des contre-analyses réalisées par des modèles de langage, arbitrées par écrit point par point avec retour aux sources&nbsp;: elles ne sont pas une évaluation par des pairs. L'auteur assume la responsabilité éditoriale des analyses publiées.</p>

<p class="apropos-lien"><a href="/serie-awp/">Les working papers&nbsp;→</a><a href="/chercheur-independant/">Chercheur indépendant&nbsp;→</a></p>

<div class="apropos-tete"><h2 id="contact" class="apropos-tete__titre section-title">Contact</h2></div>

<p class="apropos-contact"><a class="btn btn--secondary" href="/contact/">Me contacter&nbsp;→</a></p>
