---
title: "Ressources — données, dossiers et repères"
description: "Les chiffres du débat public circulent souvent sans leur source ni leur méthode. Ces ressources les reprennent aux séries officielles, les recalculent et disent ce qu'ils montrent et ce qu'ils ne montrent pas : sur la dette publique, l'école, les institutions, et le cadre d'analyse qui les relie."
# Index éditorial. La PRÉSENCE vient des pages elles-mêmes : une page entre ici en déclarant
# `ressource.bloc` dans son front matter (layouts/ressources/list.html). Ce fichier ne porte
# que l'ordre et l'intitulé des blocs. Un bloc inconnu arrête le build ; un bloc vide avertit.
# Arbitrage : .claude/external-audits/ARBITRATIONS/PRO-20260921-105434_arbitrage_2026-09-28.md
blocs:
  - id: dette
    titre: "Dette publique"
    chapo: "Pourquoi elle augmente, ce qu'elle coûte, qui la paie, ce qui se passe ailleurs et à quelles conditions elle peut baisser."
  - id: enseigner
    titre: "Pour enseigner"
    chapo: "Un dossier par discipline, des activités prêtes pour la classe : fiches élèves et corrigés, et en SES des figures et des données tirées des mêmes séries que les analyses."
    # UN DOSSIER PAR DISCIPLINE (auteur, 03/10/2026) : l'index montre une carte par discipline, qui ouvre la page à
    # onglets de ses thèmes. Les pages déclarent `ressource.discipline` et `ressource.theme` ; une discipline sans page
    # s'affiche grisée, sans lien (« à venir »), et prend sa carte active avec sa première page.
    disciplines:
      - id: "ses"
        titre: "Sciences économiques et sociales"
        nature: "SES — Première et Terminale"
        desc: "Chaque activité part d'une figure projetable et se prolonge en fiche élève imprimable, avec son corrigé et ses données."
        bouton: "Ouvrir le dossier SES"
      - id: "litterature"
        titre: "Littérature"
      - id: "philosophie"
        titre: "Philosophie"
  - id: notions
    titre: "Notions et cadre d'analyse"
    chapo: "Les définitions du cadre anthropique, chacune reliée à ses sources."
  - id: corpus
    titre: "Corpus et documentation"
    chapo: "Les appareils documentaires qui accompagnent les livres, consultables pour eux-mêmes."
  - id: guides
    titre: "Guides et éclairages"
    chapo: "Deux textes de méthode, sur l'écriture et sur le travail de recherche hors institution."
---

