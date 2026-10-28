---
title: "Ressources — données, dossiers et repères"
date: 2026-09-28  # mise en ligne de l'index (commit c664bc2) ; la date de mise à jour se déduit des ressources (page-date.html)
description: "Les chiffres du débat public circulent souvent sans leur source ni leur méthode. Les dossiers les reprennent aux séries officielles et aux textes, les recalculent et disent ce qu'ils montrent et ce qu'ils ne montrent pas : dette publique, école, institutions. Dans un espace distinct, l'auteur présente son cadre d'analyse, ses notions et ses outils documentaires."
# Index éditorial. La PRÉSENCE vient des pages elles-mêmes : une page entre ici en déclarant
# `ressource.bloc` dans son front matter (layouts/ressources/list.html). Ce fichier ne porte
# que l'ordre et l'intitulé des blocs. Un bloc inconnu arrête le build ; un bloc vide avertit.
# Arbitrage : .claude/external-audits/ARBITRATIONS/PRO-20260921-105434_arbitrage_2026-09-28.md
blocs:
  - id: dette
    titre: "Dette publique"
    barre: "propre"   # chaque page appelle `dossier-dette volet="…"` (questions, source, prolongements)
    dossier: true     # en-tête de dossier dans l'index (variante A, auteur, 06/10/2026)
    pastille: "Dossier dette publique"   # celle de la barre des pages
    bande_donnees: "dossier_dette"       # libellés des questions : data/dossier_dette.yaml, source de la barre
    chapo: "Pourquoi elle augmente, ce qu'elle coûte, qui la paie, ce qui se passe ailleurs et à quelles conditions elle peut baisser."
  - id: ecole
    titre: "École, lycée et université"
    dossier: true
    chapo: "Ce que les séries officielles disent des moyens du lycée et des parcours d'élèves : recrutement, classes, cours perdus, dépense, et ce qu'elles ne disent pas."
    # Bloc créé le 07/10/2026 (ressource « Manque-t-il des professeurs au lycée ? », pendant la consultation nationale des
    # lycéens). Élargi le 23/10/2026 à l'université (décision de l'auteur ; chantier
    # 06_PROMOTION/RECHERCHE_MALAISE_ETUDIANT_2026-10-23) : chapô inchangé tant qu'aucune page du supérieur n'est en
    # ligne, il décrit ce que le bloc contient. Français seulement : pas de bloc dans _index.en.md tant qu'aucune page anglaise n'existe (exclusion déclarée).
  - id: enseigner
    titre: "Pour enseigner"
    dossier: true
    chapo: "Un dossier par discipline, des activités prêtes pour la classe : fiches élèves et corrigés, et en SES des figures et des données tirées des mêmes séries que les analyses."
    # UN DOSSIER PAR DISCIPLINE (auteur, 03/10/2026) : l'index montre une carte par discipline, qui ouvre la page à
    # onglets de ses thèmes. Les pages déclarent `ressource.discipline` et `ressource.theme` ; une discipline sans page
    # s'affiche grisée, sans lien (« à venir »), et prend sa carte active avec sa première page.
    disciplines:
      - id: "ses"
        titre: "Sciences économiques et sociales"
        court: "SES"
        nature: "SES — Première et Terminale"
        desc: "Chaque activité part d'une figure projetable et se prolonge en fiche élève imprimable, avec son corrigé et ses données."
        bouton: "Ouvrir le dossier SES"
      - id: "emc"
        titre: "Enseignement moral et civique"
        court: "EMC"
        nature: "EMC — Terminale"
        desc: "Chaque activité s'appuie sur les données publiques des pages du site et se prolonge en fiche élève imprimable, avec son corrigé."
        bouton: "Ouvrir le dossier EMC"
      - id: "litterature"
        titre: "Littérature"
      - id: "philosophie"
        titre: "Philosophie"
  - id: promesses
    titre: "Promesses présidentielles : du pouvoir aux résultats"
    titre_barre: "Promesses présidentielles"   # pastille de la barre : le titre entier déborde à 390 px
    dossier: true
    chapo: "Qui peut décider, avec quels accords, dans quel délai — et comment vérifier le résultat ?"
    # Remplace le bloc « Pouvoir et institutions » (arbitrage PRO-20261005-153428, décision de l'auteur du 05/10).
  - id: notions
    # Le cadre d'analyse de l'auteur (arbitrage PRO-20261025-225715, 25/10/2026) : la définition, les notions et le
    # Registre des coûts déportés, séparés des dossiers de faits, qui ne sont jamais présentés comme ses démonstrations.
    # L'identifiant `notions` est gardé : l'ancre /ressources/#notions est publiée. Le bloc « Corpus et documentation »
    # est retiré : le Registre vient ici, le répertoire de La Société du premier coup vit sous la page de son livre.
    titre: "L'anthropie : le cadre d'analyse de l'auteur"
    titre_barre: "Cadre d'analyse de l'auteur"   # ligne d'appartenance des pages (partials/ressource-appartenance.html)
    chapo: "L'hypothèse de l'auteur et sa définition, les notions qu'elle mobilise, chacune attribuée à qui l'a forgée, et le Registre qui l'applique à l'histoire longue."
  - id: guides
    titre: "Guides et éclairages"
    chapo: "Des éclairages d'histoire des idées et de méthode : l'écriture, la tabula rasa, le travail de recherche hors institution."
---

