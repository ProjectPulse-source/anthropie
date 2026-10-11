---
title: "Pourquoi la dette publique augmente-t-elle ?"
description: "La dette publique française a doublé en part de PIB en trente ans. Intérêts et croissance se sont presque compensés, en deux périodes opposées ; la hausse tient surtout aux déficits hors intérêts. Dépenses ou recettes : la réponse change avec les années comparées. Décomposition Eurostat."
chapo: "Entre {dyn.annee_depart} et {dyn.annee_fin}, la dette publique française est passée de {dyn.dette_depart} % à {dyn.dette_fin} % du PIB : elle a doublé en part de la richesse produite. D'où viennent ces {dyn.hausse} points de PIB ? Les intérêts font monter le ratio, la croissance du PIB nominal le fait baisser, et sur trente ans ces deux effets se compensent presque. L'essentiel de la hausse vient des déficits publics hors intérêts, dits primaires : {dyn.deficits_primaires} points sur {dyn.hausse}. Ce bilan cache deux périodes opposées, et il dit par où la dette a monté, pas pourquoi les déficits ont existé."
og_title: "Pourquoi la dette publique augmente-t-elle ?"
og_image: "images/og-dette-dynamique.jpg"
og_image_alt: "Carte de partage : « Pourquoi la dette a doublé » — cascade de la dette française en points de PIB, de 1995 à 2025 : intérêts, croissance nominale, déficits primaires, ajustements flux-stock."
date: 2026-09-30
lastmod: 2026-10-11
# Volet 1 du dossier dette (arbitrage PRO-20260930-092814, option E). Créé le 30/09/2026 sur décision de l'auteur,
# qui lève pour cette page le gel des nouveaux ensembles jusqu'au 25/10 (feuille de route GEO). Test décisif passé :
# la décomposition se referme exactement (résidu flux-stock = témoin comptable), scripts/update_dette_dynamique.py.
# Refonte du 11/10/2026 (scénario B+, arbitrage de phase A : D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_LECTURE_2026-10-09\
# REFONTE_PILOTE\DETTE\PHASE_A_ARBITRAGE_POURQUOI_AUGMENTE.md). Bilingue : toute correction se reporte dans _index.en.md.
donnees: [dette_dynamique]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_dynamique"
  nom: "Pourquoi la dette publique française augmente : décomposition de la variation du ratio dette/PIB"
  description: "Décomposition annuelle, de {dyn.annee_depart} à {dyn.annee_fin}, de la variation du ratio dette/PIB des administrations publiques françaises en effet des intérêts, effet de la croissance nominale, solde primaire et ajustements flux-stock ; dépenses, recettes et solde en % du PIB ; ratios contrôlés contre ceux que publie Eurostat. Séries Eurostat, aucune valeur saisie à la main."
  couverture_temporelle: "{dyn.annee_depart}/{dyn.annee_fin}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Variation du ratio dette/PIB", unite: "points de PIB"}
    - {nom: "Effet des intérêts", unite: "points de PIB", description: "contribution comptable au ratio, non somme versée"}
    - {nom: "Effet de la croissance nominale", unite: "points de PIB"}
    - {nom: "Contribution du solde primaire", unite: "points de PIB", description: "déficit hors intérêts ; négative en cas d'excédent"}
    - {nom: "Ajustements flux-stock", unite: "points de PIB"}
    - {nom: "Dépenses, recettes et solde des administrations publiques", unite: "% du PIB"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
  mots: ["dette publique", "France", "déficit primaire", "effet boule de neige", "taux implicite", "croissance nominale", "dépenses publiques", "recettes publiques", "Eurostat"]
  fichiers: ["dette_dynamique.csv", "dette_dynamique.json"]
  citation: ["https://doi.org/10.5281/zenodo.23143030"]  # AWP-09 : méthode et témoin de cette décomposition
faq:
  - question: "Pourquoi la dette publique française augmente-t-elle ?"
    answer: "Sur {dyn.annee_depart}-{dyn.annee_fin}, le ratio dette/PIB est passé de {dyn.dette_depart} % à {dyn.dette_fin} %. En décomposant chaque année sa variation, les intérêts l'ont poussé de {dyn.effet_interets} points et la croissance du PIB nominal l'a freiné de {dyn.effet_croissance} : leur effet net n'est que de {dyn.effet_net} point, mais il additionne deux périodes opposées. La hausse tient pour l'essentiel aux déficits primaires, l'écart entre dépenses et recettes publiques hors intérêts ({dyn.deficits_primaires} points), et pour le reste aux ajustements flux-stock ({dyn.flux_stock}). C'est une décomposition comptable : elle dit par quel terme la dette a monté, pas pourquoi les déficits ont existé."
  - question: "Les intérêts font-ils monter la dette ?"
    answer: "Oui : ils sont une charge réelle, qui accroît le besoin de financement. Mais la croissance du PIB nominal fait baisser le ratio dette/PIB en agrandissant son dénominateur, et sur trente ans elle a presque compensé la contribution comptable des intérêts ({dyn.effet_interets} points, contre {dyn.effet_croissance} de baisse). Cette compensation est faite de deux périodes opposées : avant {dyn.tc_bascule}, l'effet net a ajouté {dyn.tc_avant} points au ratio ; depuis, il en a retiré {dyn.tc_apres}. En {dyn.annee_fin}, selon des comptes encore révisables, taux implicite et croissance nominale étaient presque égaux ({dyn.taux_implicite_dernier} % et {dyn.croissance_derniere} %)."
  - question: "La dette vient-elle de trop de dépenses ou de pas assez de recettes ?"
    answer: "Ces comptes ne le tranchent pas : un déficit primaire est un écart, qui peut venir de l'une, de l'autre ou des deux. Sur les séries d'Eurostat, le diagnostic change avec les années comparées : de {dyn.ofce_debut} à {dyn.ofce_fin}, les recettes publiques varient de {dyn.ofce_rec} points de PIB et les dépenses hors intérêts de {dyn.ofce_dep_hi} ; de {dyn.tresor_debut} à {dyn.tresor_fin}, les dépenses hors intérêts de {dyn.tresor_dep_hi} et les recettes de {dyn.tresor_rec} ; de {dyn.tresor_debut} à {dyn.ofce_fin}, les recettes de {dyn.croise_rec} et les dépenses hors intérêts de {dyn.croise_dep_hi}. L'année d'arrivée compte autant que l'année de départ."
  - question: "L'inflation fait-elle baisser la dette ?"
    answer: "Elle peut faire baisser le ratio, en gonflant le PIB nominal plus vite que la charge d'intérêts. De 2021 à 2023, la croissance nominale — hausse des prix comprise — a produit un effet taux-croissance de −{dyn.effet_2021_2023} points, alors que les déficits primaires en ajoutaient {dyn.deficits_2021_2023} ; cette décomposition ne sépare pas la part des prix de celle de la croissance réelle. Elle ne le fait pas sans coût : elle réduit la valeur réelle des créances nominales, et elle renchérit les titres indexés sur l'inflation."
  - question: "Un déficit primaire, est-ce trop de dépenses ?"
    answer: "Pas nécessairement : c'est un écart entre dépenses et recettes hors intérêts, qui peut venir de dépenses en hausse, de recettes en baisse, ou d'une récession qui fait les deux à la fois. Ces données mesurent l'écart ; elles ne disent pas lequel de ses deux termes il faudrait corriger."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 5
  nature: "Séries officielles (Eurostat) décomposées et calculs de l'auteur"
---

{{< dossier-dette volet="hausse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Mise à jour&nbsp;: {{< dyn-val "date_donnees" >}}</span> France, administrations publiques, séries Eurostat de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}. Télécharger&nbsp;: <a href="/dette_dynamique.csv">CSV</a> · <a href="/dette_dynamique.json">JSON</a> · <a href="#sources">méthode</a></p>

## D'où vient la hausse {#cascade}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-cascade-m.svg" width="300" height="660">
    <img src="/img/dette-dynamique-cascade.svg" alt="Cascade en points de PIB : la dette française part de {{< dyn-val "dette_depart" >}} % fin {{< dyn-val "annee_depart" >}} ; l'effet des intérêts l'aurait poussée de {{< dyn-val "effet_interets" >}} points, la croissance du PIB nominal en efface {{< dyn-val "effet_croissance" >}} ; les déficits primaires ajoutent {{< dyn-val "deficits_primaires" >}} points et les ajustements flux-stock {{< dyn-val "flux_stock" >}} ; la dette atteint {{< dyn-val "dette_fin" >}} % fin {{< dyn-val "annee_fin" >}}. Contributions comptables cumulées, non sommes versées." width="720" height="413" loading="lazy">
  </picture>
  <figcaption>Décomposition cumulée de la variation du ratio dette/PIB, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}}, en points de PIB (Eurostat). Bleu&nbsp;: le stock&nbsp;; orange&nbsp;: ce qui le fait monter&nbsp;; gris&nbsp;: ce qui le fait baisser.</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur trente ans, l'effet net des intérêts et de la croissance du PIB nominal est faible ({{< dyn-val "effet_net" >}} point), mais il additionne deux périodes opposées, {{< dyn-val "tc_avant" >}} points avant {{< dyn-val "tc_bascule" >}} et {{< dyn-val "tc_apres" >}} depuis&nbsp;: la hausse de la dette tient pour l'essentiel aux déficits primaires, {{< dyn-val "deficits_primaires" >}} points sur {{< dyn-val "hausse" >}}. C'est une décomposition comptable&nbsp;: elle dit par quel terme la dette a monté, pas pourquoi les déficits ont existé.

</div>

**Comment des intérêts payés peuvent-ils «&nbsp;s'annuler&nbsp;»&nbsp;?** Ils ne s'annulent pas&nbsp;: ils sont une charge réelle, qui accroît le besoin de financement&nbsp;; leur effet sur la dette dépend aussi du solde primaire et des autres opérations. Mais la page mesure un ratio, la dette rapportée à la richesse produite dans l'année, et cette richesse grossit elle aussi. Prenez une dette égale au PIB et isolez les intérêts, sans autre dépense ni recette, en les finançant par un nouvel emprunt&nbsp;: si les intérêts de l'année augmentent la dette d'un cinquantième et que le PIB augmente aussi d'un cinquantième, la dette a monté en euros, mais le ratio n'a pas bougé. Les intérêts n'ont pas disparu&nbsp;: c'est la progression du dénominateur qui compense leur effet sur le ratio. C'est tout le sens des {{< dyn-val "effet_interets" >}} points «&nbsp;effacés&nbsp;» pour l'essentiel par la croissance&nbsp;: ce sont des contributions, cumulées sur trente ans, à l'évolution d'un ratio, pas une somme versée égale à {{< dyn-val "effet_interets" >}}&nbsp;% du PIB. Les intérêts sont d'ailleurs comptés quand ils sont dus, non quand ils sont versés&nbsp;: c'est le cas du supplément dû sur les obligations de l'État dont le remboursement suit les prix. Et un déficit primaire peut venir d'une baisse des recettes, impôts compris, autant que d'une hausse des dépenses&nbsp;: le terme ne désigne ni l'une ni l'autre. Qui reçoit ces intérêts et qui supporte ce que la dette coûte est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/) Les totaux sont calculés avant arrondi&nbsp;: une somme de chiffres affichés peut s'écarter d'un dixième du total affiché.

## Année par année {#annee-par-annee}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-dynamique-annuelle-m.svg" width="300" height="742">
    <img src="/img/dette-dynamique-annuelle.svg" alt="Barres empilées par année, de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}, en points de PIB : déficits primaires en orange, effet taux-croissance en bleu, ajustements flux-stock en gris, variation du ratio en point noir. Deux pics, 2009 (+{{< dyn-val "hausse_2009" >}} points) et 2020 (+{{< dyn-val "hausse_2020" >}}) ; un effet taux-croissance de −{{< dyn-val "effet_2021_2023" >}} points en 2021-2023." width="720" height="383" loading="lazy">
  </picture>
  <figcaption>Contributions annuelles à la variation du ratio dette/PIB, France (Eurostat). La somme des trois barres égale la variation, marquée par le point noir. Ici, les couleurs désignent des termes, non le sens de leur effet comme dans la cascade.</figcaption>
</figure>

Trois périodes se dégagent, et le terme qui domine change de l'une à l'autre. La bascule de {{< dyn-val "tc_bascule" >}}, qui partage la série en deux pour l'effet taux–croissance, tombe à l'intérieur de la deuxième.

**{{< dyn-val "p1_lib" >}}&nbsp;: l'effet taux–croissance.** Le ratio gagne {{< dyn-val "p1_hausse" >}} points. Le taux implicite de la dette, c'est-à-dire le taux moyen que coûte l'ensemble de la dette, dépasse alors, en moyenne, la croissance nominale&nbsp;: l'effet taux–croissance ajoute {{< dyn-val "p1_taux_croissance" >}} points, quand le solde primaire, proche de l'équilibre et parfois excédentaire, contribue pour {{< dyn-val "p1_deficits" >}}.

**{{< dyn-val "p2_lib" >}}&nbsp;: les déficits primaires.** Le ratio gagne {{< dyn-val "p2_hausse" >}} points, dont {{< dyn-val "p2_deficits" >}} par les déficits primaires et {{< dyn-val "p2_taux_croissance" >}} par l'effet taux–croissance. L'année 2009 compte à elle seule {{< dyn-val "hausse_2009" >}} points&nbsp;: le déficit primaire se creuse et le PIB recule, deux effets qui coïncident avec la crise financière.

**{{< dyn-val "p3_lib" >}}&nbsp;: la croissance nominale freine, les déficits poussent.** Le ratio gagne {{< dyn-val "p3_hausse" >}} points. En 2020, il bondit de {{< dyn-val "hausse_2020" >}} points, avec la crise sanitaire. De 2021 à 2023, la forte croissance du PIB nominal, hausse des prix comprise, fait baisser le ratio&nbsp;: l'effet taux–croissance retire {{< dyn-val "effet_2021_2023" >}} points au ratio, plus que les déficits primaires n'en ajoutent ({{< dyn-val "deficits_2021_2023" >}}). La part des prix dans cette croissance est l'objet de [L'inflation a-t-elle allégé la dette&nbsp;?](/inflation-et-dette-publique/) Depuis 2024, le ratio remonte.

**Le taux implicite remonte depuis 2022, d'abord par un saut.** Après un point bas de {{< dyn-val "ti_creux" >}}&nbsp;% en {{< dyn-val "ti_creux_an" >}}, le taux implicite de la dette passe de {{< dyn-val "ti_2021" >}}&nbsp;% en 2021 à {{< dyn-val "ti_2022" >}}&nbsp;% en 2022, puis monte plus lentement. Ce saut ne vient pas seulement du renouvellement des titres aux taux nouveaux&nbsp;: en 2022, l'inflation a aussi fortement accru la charge comptabilisée des obligations de l'État indexées sur les prix, selon le rapport du Sénat sur les comptes de l'année. Les comptes présentés ici ne permettent pas de séparer la part de chaque mécanisme dans le taux implicite de l'ensemble des administrations publiques.

**Les comptes de {{< dyn-val "annee_fin" >}} restent révisables.** Ceux de cette page sont les séries d'Eurostat mises à jour le {{< dyn-val "millesime_dette" >}} pour la dette, avec la notification d'avril, et le {{< dyn-val "millesime_comptes" >}} pour les comptes. Cette année-là, taux implicite ({{< dyn-val "taux_implicite_dernier" >}}&nbsp;%) et croissance nominale ({{< dyn-val "croissance_derniere" >}}&nbsp;%) sont presque égaux, et l'effet taux–croissance est voisin de zéro&nbsp;: un écart aussi mince ne dit pas dans quel sens l'effet ira ensuite.

Sur les {{< dyn-val "annees_total" >}} années de la série, le solde primaire n'a été excédentaire que {{< dyn-val "annees_excedent" >}} fois. Ce décompte décrit une récurrence&nbsp;; il ne dit pas si chacun de ces déficits était souhaitable, évitable ou conjoncturel.

## Trop de dépenses ou pas assez de recettes&nbsp;? {#depenses-recettes}

Le déficit primaire est l'écart entre les dépenses hors intérêts et les recettes publiques. Il ne dit pas si cet écart vient d'une hausse des dépenses, d'une baisse des recettes ou des deux à la fois. Pour le décrire, il faut choisir deux années et comparer, entre elles, dépenses et recettes en part de PIB. Les séries d'Eurostat donnent alors des réponses différentes selon les années choisies.

- **De {{< dyn-val "ofce_debut" >}} à {{< dyn-val "ofce_fin" >}}**, la période retenue par l'OFCE&nbsp;: les recettes publiques varient de {{< dyn-val "ofce_rec" >}} points de PIB, les dépenses hors intérêts de {{< dyn-val "ofce_dep_hi" >}}. Le recul des recettes domine.
- **De {{< dyn-val "tresor_debut" >}} à {{< dyn-val "tresor_fin" >}}**, la période retenue par la direction générale du Trésor&nbsp;: les dépenses hors intérêts varient de {{< dyn-val "tresor_dep_hi" >}} points, les recettes de {{< dyn-val "tresor_rec" >}}. La hausse des dépenses domine.
- **De {{< dyn-val "tresor_debut" >}} à {{< dyn-val "ofce_fin" >}}**, la fenêtre commune aux deux&nbsp;: les dépenses hors intérêts varient de {{< dyn-val "croise_dep_hi" >}} points, les recettes de {{< dyn-val "croise_rec" >}}. Le recul des recettes domine de nouveau.

**Le diagnostic dépend des deux bornes.** Il change avec l'année de départ, mais aussi avec l'année d'arrivée&nbsp;: en finissant en {{< dyn-val "ofce_fin" >}} plutôt qu'en {{< dyn-val "tresor_fin" >}}, la même année de départ donne la conclusion inverse. Deux comparaisons exactes, sur des périodes différentes, peuvent donc conduire à des constats descriptifs opposés — ce qui ne rend pas fondées pour autant les interprétations causales qu'on en tire. La page mesure un même indicateur d'Eurostat sur ces fenêtres&nbsp;; elle ne rend pas équivalents les travaux de l'OFCE et du Trésor, qui diffèrent aussi par leurs définitions et leurs questions&nbsp;: devant l'une ou l'autre, la première question à poser est «&nbsp;de quelle année à quelle année&nbsp;?&nbsp;». 

**Ce qui retourne la conclusion entre les deux fenêtres qui partent de {{< dyn-val "tresor_debut" >}}, ce sont les recettes.** Les dépenses hors intérêts y varient d'autant, à l'arrondi près&nbsp;; les recettes, elles, remontent de {{< dyn-val "rec_fin" >}} point de PIB en {{< dyn-val "tresor_fin" >}}. C'est l'atténuation du recul des recettes, non un mouvement des dépenses, qui fait basculer leur poids relatif. Ces mouvements sont mesurés en part de PIB&nbsp;: ils peuvent venir du numérateur, du dénominateur, ou des deux. Ce constat descriptif, sur des comptes encore révisables, ne dit pas quelles décisions ont produit cette remontée. Et un déficit qui se réduit n'a pas disparu&nbsp;: en {{< dyn-val "tresor_fin" >}}, le solde primaire reste déficitaire et la dette continue de monter. Ces comparaisons décrivent des mouvements en part de PIB&nbsp;; elles ne disent pas quelles décisions les ont produits, ni ce qu'il faudrait corriger. Ce que l'OFCE et la direction générale du Trésor en concluent, et sur quels objets, est confronté plus bas.

## Comment le calcul fonctionne {#identite}

Chaque année, le ratio dette/PIB bouge sous l'effet de trois termes. L'**effet taux–croissance**&nbsp;: les intérêts de l'année accroissent la dette, quand la croissance du PIB nominal — croissance réelle et hausse des prix — fait baisser le ratio même sans remboursement&nbsp;; leur solde est positif quand le taux implicite dépasse la croissance nominale, négatif dans le cas inverse. Le **déficit primaire**&nbsp;: l'écart entre dépenses et recettes publiques hors intérêts, qui mesure l'écart, pas sa cause. Les **ajustements flux-stock**&nbsp;: la dette qui bouge sans passer par le déficit (trésorerie mise en réserve, prêts et participations, écarts de valorisation), obtenue ici comme résidu. La cascade présente l'effet taux–croissance en ses deux composantes, intérêts et croissance&nbsp;: d'où ses quatre marches pour trois termes.

<details class="repli"><summary>L'identité exacte, terme à terme</summary>

<div class="equation" role="group" aria-label="La variation du ratio de dette décomposée">
  <p class="equation__titre">Ce qui fait bouger le ratio dette/PIB d'une année à l'autre</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>l'effet taux–croissance</b><small>intérêts moins croissance du PIB nominal</small></span>
    <span class="equation__op" aria-label="plus">+</span>
    <span class="equation__terme"><b>le déficit primaire</b><small>dépenses moins recettes, hors intérêts</small></span>
    <span class="equation__op" aria-label="plus">+</span>
    <span class="equation__terme"><b>les ajustements flux-stock</b><small>ce qui ne passe pas par le déficit</small></span>
    <span class="equation__op" aria-label="égale">=</span>
    <span class="equation__terme equation__terme--resultat"><b>la variation du ratio</b><small>en points de PIB</small></span>
  </div>
  <p class="equation__exacte">Identité exacte&nbsp;: d<sub>t</sub> − d<sub>t−1</sub> = (i − g) / (1 + g) × d<sub>t−1</sub> − solde primaire<sub>t</sub> + flux-stock<sub>t</sub>, avec d le ratio dette/PIB, i le taux implicite (intérêts de l'année / dette de fin d'année précédente) et g la croissance du PIB nominal.</p>
</div>

</details>

## Ce que cette décomposition ne dit pas {#limites}

- **Une décomposition comptable, non une explication causale.** Elle dit par quel terme la dette a bougé&nbsp;; elle ne dit pas pourquoi les déficits ont existé, ni s'ils étaient évitables, ni qui en porte la responsabilité.
- **Des contributions, non des sommes versées.** Les points de PIB de la cascade mesurent l'effet sur un ratio, cumulé sur trente ans&nbsp;; ils ne disent pas combien a été payé, à qui, ni quand.
- **Des termes qui ne sont pas indépendants.** En récession, les recettes baissent et certaines dépenses montent&nbsp;: le déficit primaire dépend lui-même de la croissance.
- **L'inflation n'efface pas la dette sans coût.** Elle réduit la valeur réelle des créances nominales, et cette perte a des porteurs&nbsp;: c'est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- **Rien sur l'avenir.** La suite dépend de l'écart entre le taux implicite et la croissance nominale, et du solde primaire&nbsp;: ce qu'il a fallu ailleurs pour que la dette baisse est l'objet de [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)
- **Une dernière année révisable.** Les comptes de {{< dyn-val "annee_fin" >}} sont ceux des séries d'Eurostat mises à jour le {{< dyn-val "millesime_dette" >}} (dette) et le {{< dyn-val "millesime_comptes" >}} (comptes).
- **Une série qui commence en {{< dyn-val "annee_depart" >}}.** Les intérêts harmonisés d'Eurostat ne remontent pas plus loin&nbsp;; la courbe longue de la dette, depuis 1978, est dans [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="le poids des déficits primaires est retrouvé sur cinquante ans&nbsp;; lire la quasi-annulation des intérêts et de la croissance comme une neutralité est mis en danger&nbsp;; dépenses ou recettes&nbsp;: le diagnostic dépend de la période et de la comparaison retenues" >}}
**Mesuré ici.** La décomposition annuelle du ratio français de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}, sur les séries d'Eurostat, contrôlée contre les ratios publiés. Aucun des textes lus ne décompose cette fenêtre avec cette source&nbsp;: la mesure se valide par reproduction, non par citation.

**Cohérent avec.** L'audit citoyen de 2014 attribuait une large part de la hausse de la dette de 1980 à 2012 à l'effet des taux d'intérêt. Les deux analyses ne portent ni sur les mêmes bornes, ni nécessairement sur le même contrefactuel&nbsp;; sur une fenêtre qui s'arrête avant le milieu des années 2010, l'effet taux–croissance pèse lourd ici aussi, avant {{< dyn-val "tc_bascule" >}}. La confrontation de leurs méthodes est exposée dans le working paper [AWP-09](/awp/awp-09/). Sur 1970-2023, avec les comptes de l'Insee et une base historique, Auclert, Philippon et Ragot trouvent que les déficits primaires et les ajustements flux-stock font 88 points d'une hausse de près de 90 (de 21&nbsp;% à 110&nbsp;% du PIB), et un effet «&nbsp;boule de neige&nbsp;» proche de zéro en moyenne&nbsp;: même identité, autre période, autre source, et un déficit primaire qui inclut les ajustements que la page isole. Clavères, à la direction générale du Trésor, retrouve la même chronologie des signes&nbsp;: le taux apparent de la dette, proche du taux implicite de cette page sans lui être identique (les deux rapportent les intérêts à un encours de dette, pas nécessairement au même&nbsp;: le coût apparent publié par Eurostat retient l'encours moyen de l'année, cette page celui de la fin de l'année précédente), passe au-dessus de la croissance nominale dans le courant des années 1980, et la croissance repasse au-dessus à partir de 2016. L'OFCE (Heyer, Plane, Ragot, Sampognaro et Timbeau) rattache aux déficits une hausse de la dette de 53 points en France de 2000 à 2024, contre 44 en Espagne, 27 en Italie et 5 en Allemagne, sans décomposer ces hausses. La direction générale du Trésor décrit une dette qui augmente presque continûment depuis 2001, les réductions du déficit ne permettant, dans les périodes favorables, que de stabiliser le ratio, et un déficit resté supérieur au solde stabilisant jusqu'en 2019. Elle qualifie la période 2001-2007 de «&nbsp;relative stabilité&nbsp;»&nbsp;; la série de la page y enregistre néanmoins une hausse de {{< dyn-val "dette_2001" >}}&nbsp;% à {{< dyn-val "dette_2007" >}}&nbsp;% du PIB, et l'OFCE estime que près de la moitié de l'écart de déficit avec la zone euro s'était formée avant la crise de 2007-2008.

**Mis en danger par.** Toute lecture de la quasi-annulation des intérêts et de la croissance comme une neutralité. La coïncidence dépend du point de départ, à une dizaine de points près (Auclert, Philippon et Ragot), et l'écart entre taux et croissance a changé de signe en cours de période (Clavères). Les données de la page le confirment&nbsp;: l'effet taux-croissance a pesé {{< dyn-val "tc_avant" >}} points avant {{< dyn-val "tc_bascule" >}}, {{< dyn-val "tc_apres" >}} depuis. La Note du CAE, elle, interprète ce constat comptable comme résultant directement des choix budgétaires («&nbsp;notre dette est la conséquence directe de nos choix budgétaires&nbsp;»), tout en jugant difficile d'estimer la part des crises, qu'une estimation de l'OFCE, citée par la Note, situe autour de la moitié de la hausse depuis 2007.

**Non établi.** Lequel, des dépenses ou des recettes, a creusé les déficits récents. L'OFCE, qui propose une trajectoire d'ajustement plus progressive, fait débuter la période récente à l'élection présidentielle de 2017 et attribue l'essentiel de la dégradation du solde structurel à une baisse non financée des prélèvements obligatoires, qui ont diminué de 2,5 points de PIB de 2017 à 2024&nbsp;; sur cette période, selon lui, la dépense totale reste stable en part de PIB et la dépense primaire recule légèrement en part de PIB potentiel (sur les séries d'Eurostat, en part du PIB effectif, la dépense totale varie de {{< dyn-val "ofce_dep" >}} point). La direction générale du Trésor, pour qui la consolidation «&nbsp;pourrait passer en priorité&nbsp;» par la réduction de la dépense, part de 2019, situation d'avant la crise sanitaire, et relève que plusieurs dépenses (charge d'intérêts, sécurité sociale, administrations centrales et locales) ont participé à la dégradation de 2,7 points du solde jusqu'en 2025, tout en notant que des réformes ont réduit durablement les recettes. Sur la fenêtre commune, l'OFCE et la direction générale du Trésor convergent sur un fait&nbsp;: la dépense publique a moins progressé en France que dans la zone euro (1,8 point contre 2,6 pour l'un, 1,6 contre 2,4 pour l'autre)&nbsp;; les séries d'Eurostat en retrouvent le sens et l'ordre de grandeur (dépenses {{< dyn-val "croise_dep" >}} points, recettes totales {{< dyn-val "croise_rec" >}}). Ils n'analysent toutefois pas ensuite le même objet&nbsp;: l'OFCE explique l'écart entre la France et la zone euro, qu'il rattache surtout aux recettes, la direction générale du Trésor décompose la dégradation du solde français sur 2019-2025&nbsp;; et les recettes totales d'Eurostat ne sont pas les prélèvements obligatoires de l'OFCE. Sur les séries d'Eurostat, le diagnostic dépend des deux bornes de la fenêtre (section «&nbsp;Trop de dépenses ou pas assez de recettes&nbsp;?&nbsp;»). Les causes, enfin&nbsp;: la Note du CAE attribue la dégradation récente à la crise sanitaire, aux boucliers tarifaires sur l'énergie et à des baisses d'impôts non financées, la direction générale du Trésor aux crises et aux mesures de soutien, mais aucun des six textes ne fournit une décomposition causale des déficits primaires observés de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}.

**Références lues**

- Auclert, A., Philippon, T. et Ragot, X., «&nbsp;Quelle trajectoire pour les finances publiques françaises&nbsp;?&nbsp;», *Les notes du Conseil d'analyse économique*, n°&nbsp;82, juillet 2024.
- Clavères, G., «&nbsp;Taux d'intérêt, croissance et soutenabilité de la dette publique&nbsp;», *Trésor-Éco*, n°&nbsp;334, direction générale du Trésor, octobre 2023.
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., «&nbsp;Quelles trajectoires pour les finances publiques de la France&nbsp;?&nbsp;», *Blog de l'OFCE*, 2025.
- Direction générale du Trésor, «&nbsp;Finances publiques&nbsp;: une situation dégradée, un redressement nécessaire&nbsp;», *Trésor-Éco*, n°&nbsp;403, septembre 2026.
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., «&nbsp;Quelles trajectoires pour les finances publiques de la France&nbsp;?&nbsp;», document de travail de l'OFCE n°&nbsp;13, juillet 2025.
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

En trente ans, la dette publique française a doublé en part de PIB, de {{< dyn-val "dette_depart" >}}&nbsp;% à {{< dyn-val "dette_fin" >}}&nbsp;%. Les intérêts l'ont poussée, mais sur l'ensemble de la période la croissance du PIB nominal en a effacé presque autant&nbsp;; ce qui reste, dans la décomposition Eurostat utilisée ici, ce sont les déficits primaires, {{< dyn-val "part_deficits" >}}&nbsp;% de la hausse&nbsp;: hors intérêts, les comptes publics n'ont été excédentaires que {{< dyn-val "annees_excedent" >}} années sur {{< dyn-val "annees_total" >}}.

Cette quasi-annulation est une compensation dans le temps, non une neutralité. Avant {{< dyn-val "tc_bascule" >}}, le taux implicite dépassait le plus souvent la croissance nominale, et l'effet taux-croissance a ajouté {{< dyn-val "tc_avant" >}} points au ratio&nbsp;; depuis, la croissance nominale l'emporte chaque année, sauf en 2020, quand le PIB a reculé, et l'effet a pesé {{< dyn-val "tc_apres" >}} points. En {{< dyn-val "annee_fin" >}}, selon des comptes encore révisables, taux implicite et croissance nominale sont presque égaux&nbsp;: tant qu'ils le restent, le sens du ratio se joue sur le solde primaire, aux ajustements flux-stock près. Le taux implicite remonte depuis 2022&nbsp;; s'il repasse au-dessus de la croissance, le ratio montera davantage à solde primaire égal.

Dépenses ou recettes&nbsp;: les comptes décrivent des mouvements, ils ne désignent pas de responsable, et leur réponse change avec les deux années que l'on compare. Ce qu'il a fallu ailleurs pour que la dette baisse est l'objet de [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Et ailleurs&nbsp;?](/dette-publique-comparaison-internationale/)
- [Peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page montre par quels termes la dette a monté. Elle ne dit pas qui en supporte le coût, ni par quels canaux il se déplace — vers le contribuable, vers l'épargnant par l'inflation, vers des services publics dont la marge se resserre — selon les décisions prises pour l'ajuster. Le livre suit ces canaux un par un, chiffres officiels à l'appui, pour montrer dans quelles configurations chacun supporte un coût. Il propose une méthode en trois questions — les faits sont-ils établis, le système tient-il sa promesse, qui décide — et, pour les issues qu'il envisage, le partage entre qui paie et qui gagne.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

Eurostat, administrations publiques (S.13), comptes nationaux SEC 2010, en monnaie nationale&nbsp;: dette de Maastricht ([`gov_10dd_edpt1`](https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr)), intérêts dus ([`gov_10a_main`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr), D41PAY, comptés en droits constatés), capacité ou besoin de financement (B9), PIB nominal publié avec la notification de déficit et de dette (`gov_10dd_edpt1`, B1GQ)&nbsp;; dépenses (TE), recettes (TR) et solde en % du PIB tels qu'Eurostat les publie (`gov_10a_main`). Le solde primaire est le solde des administrations publiques augmenté des intérêts (D41PAY). Chaque année, l'identité est appliquée telle qu'écrite plus haut&nbsp;; les ajustements flux-stock sont le résidu. Le script compare ensuite, année par année, le ratio de dette et le solde primaire qu'il calcule à ceux qu'Eurostat publie en pourcentage du PIB, et s'arrête au-delà de 0,11 point d'écart. Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent du même script, relancé à chaque publication des sources, qui vérifie les principales affirmations chiffrées et s'arrête si leurs conditions ne sont plus remplies&nbsp;; leur formulation fait l'objet d'une relecture éditoriale. Charge d'indexation des titres de l'État en 2022&nbsp;: Sénat, [rapport sur le projet de loi de règlement du budget 2022](https://www.senat.fr/rap/l22-771-1/l22-771-17.html).

La méthode de cette décomposition (l'identité, le témoin que forment les ratios publiés par Eurostat et l'erreur qu'il a rejetée) et son rapprochement avec trois lectures publiques de la même dette (l'audit citoyen de 2014, la Fondation iFRAP, la Cour des comptes) sont exposés dans le working paper [AWP-09 — *Ce que les comptes publics permettent d'établir sur le déplacement de la charge de la dette*](/awp/awp-09/) (DOI&nbsp;: 10.5281/zenodo.23143030, PDF en accès libre).

{{< reutiliser figures="figures_dynamique" jeu="dette_dynamique" sources="Eurostat" donnees="La décomposition annuelle de la variation du ratio dette/PIB, France, avec ses quatre termes, le taux implicite et la croissance nominale ; dépenses, recettes et solde en % du PIB ; le même contenu existe en CSV, une ligne par année." >}}
Cette page décompose la variation du ratio dette/PIB français, de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}, en effet des intérêts, effet de la croissance nominale, solde primaire et ajustements flux-stock. Sur la période, intérêts et croissance nominale se sont presque annulés, en deux périodes opposées, et la hausse tient pour l'essentiel aux déficits primaires, hors intérêts. Dépenses ou recettes&nbsp;: la réponse des comptes change avec les deux années comparées. C'est une décomposition comptable, non une attribution causale&nbsp;: elle ne dit pas pourquoi les déficits ont existé.
{{< /reutiliser >}}
