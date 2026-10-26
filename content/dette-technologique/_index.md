---
title: "Qu'est-ce que la dette technologique ?"
description: "La dette technologique désigne le coût des infrastructures numériques — énergie, matière, territoire, attention — transformé en dette par des mécanismes d'engagement. À ne pas confondre avec la « dette technique » du génie logiciel."
date: 2026-07-04
lastmod: 2026-10-26
og_title: "Qu'est-ce que la dette technologique ? — définition et sources — S. Lalut"
faq:
  - question: "Quelle est la différence entre dette technologique et dette technique ?"
    answer: "La dette technique est une notion de génie logiciel : l'accumulation de compromis de conception dans un programme, qui rend son évolution de plus en plus coûteuse. La dette technologique, au sens de Stéphane Lalut (AWP-06, 2026), est un mécanisme économique et politique : le coût des infrastructures numériques — énergie, matière, territoire, attention — transformé en dette par des engagements de long terme. L'une est une propriété du code ; l'autre, une propriété du système économique."
  - question: "La dette technologique est-elle une dette au sens financier ?"
    answer: "Pas seulement. Une partie l'est littéralement — garanties publiques, contrats d'achat d'énergie de long terme, financements adossés à des revenus futurs. Mais la dette technologique inclut aussi des engagements non monétaires : des territoires affectés pour des décennies, des choix d'infrastructure devenus irréversibles, une attention captée. C'est une dette au sens anthropique : un désordre reporté vers l'avenir."
  - question: "Qui porte la dette technologique ?"
    answer: "Ceux qui n'ont pas signé les engagements : les budgets publics qui garantissent, les territoires qui accueillent les infrastructures et leurs besoins en énergie et en eau, les générations qui hériteront des équipements et de leurs coûts de maintenance ou de démantèlement, et les utilisateurs dont l'attention constitue le quatrième registre de coût."
  - question: "Où le concept est-il formalisé ?"
    answer: "Dans AWP-06, « Infrastructures numériques et dette technologique » (Stéphane Lalut, 2026, DOI 10.5281/zenodo.20025421), sixième des Anthropie Working Papers, et dans le livre ANTHROPIE — Ordre ici. Dette ailleurs (2025), qui déploie le cadre général."
fiche:  # encadré « La notion en bref » (shortcode notion-fiche) : reprend la page, aucun fait nouveau
  lignes:
    - t: "Définition"
      d: "Le coût des infrastructures numériques — énergie, matière, territoire, attention — transformé en dette par des mécanismes d'engagement&nbsp;: garanties publiques, contrats de long terme, irréversibilisation des choix d'infrastructure."
    - t: "Origine"
      d: "Concept formalisé par l'économiste Stéphane Lalut dans [AWP-06](/awp/awp-06/) (2026), dans le cadre de l'[anthropie](/quest-ce-que-lanthropie/)."
    - t: "À ne pas confondre"
      d: "La dette *technique* du génie logiciel&nbsp;: des compromis de conception accumulés dans un programme, une propriété du code et non du système économique."
    - t: "Exemple"
      d: "Les data centers&nbsp;: électricité et eau contractualisées sur des décennies, matériaux extraits ailleurs, emprises foncières, économie de l'attention qui finance l'ensemble."
    - t: "Nature de la dette"
      d: "Pas seulement financière&nbsp;: une partie l'est littéralement (garanties, contrats de long terme)&nbsp;; le reste est fait d'engagements non monétaires — territoires affectés, choix irréversibles, attention captée."
    - t: "Lecture anthropique"
      d: "Le numérique n'a pas allégé la matière, il l'a déplacée — dans l'espace, dans le temps et vers l'attention."
      anthropie: true
schemas:  # schéma de mécanisme (shortcode notion-schema)
  mecanisme:
    titre: "Comment un coût d'infrastructure devient une dette"
    etages:
      - boites:
          - {t: "Infrastructure numérique", d: "La promesse d'un service immatériel, «&nbsp;le cloud&nbsp;»", ton: "ordre"}
        fleche: "trois opérations"
      - titre: "Le coût se convertit en engagement"
        boites:
          - {t: "Engagement", d: "Contrats d'énergie, baux, commandes&nbsp;: le coût futur est verrouillé au présent"}
          - {t: "Garantie", d: "Dispositifs publics qui rendent l'investissement attractif&nbsp;: si le pari échoue, la collectivité paie"}
          - {t: "Irréversibilisation", d: "Revenir en arrière coûte plus cher que continuer"}
        fleche: "sur quatre registres couplés"
      - titre: "Les registres de coûts couplés (AWP-06)"
        boites:
          - {t: "Énergie", d: "Électricité et eau contractualisées", ton: "cout"}
          - {t: "Matière", d: "Matériaux extraits ailleurs", ton: "cout"}
          - {t: "Territoire", d: "Emprises foncières, réseaux dimensionnés", ton: "cout"}
          - {t: "Attention", d: "L'économie qui finance l'ensemble", ton: "cout"}
        fleche: "portée par ceux qui n'ont pas signé"
      - boites:
          - {t: "Qui la porte", d: "Les budgets publics qui garantissent, les territoires qui accueillent, les générations qui hériteront des équipements, les utilisateurs dont l'attention est captée", ton: "cout"}
    note: "Les registres ne s'additionnent pas&nbsp;: ils se couplent. Réduire l'un déplace souvent la charge vers les trois autres."
comparaisons:  # frontière entre notions voisines (shortcode notion-comparaison)
  frontiere:
    titre: "Dette technique, dette technologique"
    colonnes: ["Dette technique", "Dette technologique"]
    accent: 2
    lignes:
      - {critere: "Domaine", valeurs: ["Génie logiciel", "Économie et politique"]}
      - {critere: "Ce qui s'endette", valeurs: ["Un programme", "Une société"]}
      - {critere: "Mécanisme", valeurs: ["Des compromis de conception s'accumulent&nbsp;: livrer vite aujourd'hui, payer la maintenance demain", "Le coût présent des infrastructures est converti en engagements que d'autres porteront"]}
      - {critere: "Ce qu'elle décrit", valeurs: ["Une propriété du code", "Une propriété du système économique"]}
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["notion"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/dette-technologique.md"  # fiche de conception (regle 12), refonte de presentation du 26/10/2026
  bloc: "notions"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 60
  nature: "Notion — définition, origine et sources"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Dette technologique"
  court: "Techno."
  long_en: "Technological debt"
---

La dette technologique est le coût des infrastructures numériques — énergie, matière, territoire, attention — transformé en dette par des mécanismes d'engagement&nbsp;: garanties publiques, contrats de long terme, irréversibilisation des choix d'infrastructure. Le concept est formalisé par l'économiste Stéphane Lalut dans le working paper [AWP-06](/awp/awp-06/) (2026) et s'inscrit dans le cadre de l'anthropie.

{{< notion-fiche >}}

## À ne pas confondre avec la «&nbsp;dette technique&nbsp;»

Sur le web, «&nbsp;dette technologique&nbsp;» renvoie presque toujours à la **dette technique** du génie logiciel&nbsp;: l'accumulation de compromis de conception dans un programme — on livre vite aujourd'hui, on paiera la maintenance demain. La métaphore est utile, mais elle décrit une propriété du code.

La dette technologique au sens anthropique désigne autre chose&nbsp;: un mécanisme **économique et politique**. Ce ne sont pas des lignes de programme qui s'endettent, ce sont des sociétés — quand elles convertissent le coût présent de leurs infrastructures numériques en engagements que d'autres porteront.

{{< notion-comparaison id="frontiere" >}}

## Le mécanisme&nbsp;: comment un coût devient une dette

{{< notion-schema id="mecanisme" >}}

Trois opérations transforment un coût d'infrastructure en dette&nbsp;:

1. **L'engagement** — contrats d'achat d'énergie de long terme, baux fonciers de plusieurs décennies, commandes d'équipements qui enjambent les cycles politiques&nbsp;: le coût futur est verrouillé au présent.
2. **La garantie** — dispositifs publics qui altèrent le profil de risque de l'investissement privé pour le rendre attractif aux capitaux institutionnels (le *derisking* décrit par Daniela Gabor)&nbsp;: si le pari échoue, la collectivité paie.
3. **L'irréversibilisation** — une fois le réseau construit, le territoire équipé, les usages installés, revenir en arrière coûte plus cher que continuer&nbsp;: le choix d'hier devient la contrainte de demain.

[AWP-06](/awp/awp-06/) propose une grille testable de **quatre registres de coûts couplés** — énergie, matière, territoire, attention. Ces registres ne s'additionnent pas&nbsp;: ils se couplent. Réduire l'un déplace souvent la charge vers les trois autres.

## Le cas des data centers

Les data centers rendent le mécanisme visible. Leur promesse est immatérielle — «&nbsp;le cloud&nbsp;» — mais leur réalité engage les quatre registres à la fois&nbsp;: une consommation d'électricité et d'eau contractualisée sur des décennies, des matériaux extraits ailleurs, des emprises foncières et des réseaux dimensionnés pour eux, et une économie de l'attention qui finance l'ensemble. Le débat public se concentre sur le «&nbsp;combien&nbsp;» (kilowattheures, mètres cubes)&nbsp;; la dette technologique pose l'autre question&nbsp;: **qui s'est engagé, pour combien de temps, et qui portera le coût si la promesse change&nbsp;?**

## D'où vient le concept

{{< canonical-definition >}}

La dette technologique est l'application de cette hypothèse aux infrastructures numériques&nbsp;: le numérique n'a pas allégé la matière, il l'a déplacée — dans l'espace (extraction, territoires d'accueil), dans le temps (engagements, équipements à démanteler) et vers l'attention. La définition courte est disponible dans le [glossaire](/glossaire/#dette-technologique)&nbsp;; l'analyse voisine de la transition énergétique dans [AWP-04](/awp/awp-04/)&nbsp;; et ce que deviennent ces infrastructures en fin de vie — un héritage partagé dont personne ne veut — sur la page [Qu'est-ce que les communs négatifs&nbsp;?](/communs-negatifs/)

## Questions fréquentes

**Quelle est la différence entre dette technologique et dette technique&nbsp;?** La dette technique est une notion de génie logiciel — des compromis de conception accumulés dans un programme. La dette technologique est un mécanisme économique et politique&nbsp;: le coût des infrastructures numériques transformé en dette par des engagements de long terme. L'une est une propriété du code, l'autre du système économique.

**Est-ce une dette au sens financier&nbsp;?** Pas seulement. Une partie l'est littéralement (garanties, contrats de long terme)&nbsp;; le reste est fait d'engagements non monétaires — territoires affectés, choix irréversibles, attention captée. C'est une dette au sens anthropique&nbsp;: un désordre reporté vers l'avenir.

**Qui la porte&nbsp;?** Ceux qui n'ont pas signé&nbsp;: les budgets publics qui garantissent, les territoires qui accueillent, les générations qui hériteront des équipements, les utilisateurs dont l'attention est le quatrième registre.

## Pour aller plus loin

- [AWP-06 — *Infrastructures numériques et dette technologique*](/awp/awp-06/) — le working paper qui formalise le concept (DOI&nbsp;: 10.5281/zenodo.20025421, PDF en accès libre).
- Le livre [*ANTHROPIE — Ordre ici. Dette ailleurs*](/livres/anthropie-ordre-ici-dette-ailleurs/) (2025, 630 p.) déploie le cadre complet dont la dette technologique est l'une des applications.
- [Qu'est-ce que l'anthropie&nbsp;?](/quest-ce-que-lanthropie/) — la page du concept général.

{{< consultation slug="anthropie-ordre-ici-dette-ailleurs" >}}
