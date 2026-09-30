---
title: "Pourquoi la dette publique augmente-t-elle ?"
description: "La dette française a doublé en trente ans. Les intérêts et la croissance se sont presque annulés : la hausse tient surtout aux déficits primaires. Décomposition Eurostat."
chapo: "De {dyn.dette_depart} % à {dyn.dette_fin} % du PIB entre {dyn.annee_depart} et {dyn.annee_fin} : la dette publique française a doublé. Les intérêts l'ont poussée de {dyn.effet_interets} points, la croissance du PIB nominal l'a freinée d'autant ou presque ; ce qui reste, pour {dyn.part_deficits} % de la hausse, ce sont les déficits primaires, hors intérêts."
og_title: "Pourquoi la dette publique augmente-t-elle ?"
og_image: "images/og-dette-dynamique.jpg"
og_image_alt: "Carte de partage : « Pourquoi la dette a doublé » — cascade de la dette française en points de PIB, de 1995 à 2025 : intérêts, croissance nominale, déficits primaires, ajustements flux-stock."
date: 2026-09-30
lastmod: 2026-09-30
# Volet 1 du dossier dette (arbitrage PRO-20260930-092814, option E). Créé le 30/09/2026 sur décision de l'auteur,
# qui lève pour cette page le gel des nouveaux ensembles jusqu'au 25/10 (feuille de route GEO). Test décisif passé :
# la décomposition se referme exactement (résidu flux-stock = témoin comptable), scripts/update_dette_dynamique.py.
donnees: [dette_dynamique]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "dette_dynamique"
  nom: "Pourquoi la dette publique française augmente : décomposition de la variation du ratio dette/PIB"
  description: "Décomposition annuelle, de {dyn.annee_depart} à {dyn.annee_fin}, de la variation du ratio dette/PIB des administrations publiques françaises en effet des intérêts, effet de la croissance nominale, solde primaire et ajustements flux-stock ; résidu vérifié contre le témoin comptable. Séries Eurostat, aucune valeur saisie à la main."
  couverture_temporelle: "{dyn.annee_depart}/{dyn.annee_fin}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Variation du ratio dette/PIB", unite: "points de PIB"}
    - {nom: "Effet des intérêts", unite: "points de PIB"}
    - {nom: "Effet de la croissance nominale", unite: "points de PIB"}
    - {nom: "Contribution du solde primaire", unite: "points de PIB", description: "déficit hors intérêts ; négative en cas d'excédent"}
    - {nom: "Ajustements flux-stock", unite: "points de PIB"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table?lang=fr"
  mots: ["dette publique", "France", "déficit primaire", "effet boule de neige", "taux implicite", "croissance nominale", "Eurostat"]
  fichiers: ["dette_dynamique.csv", "dette_dynamique.json"]
faq:
  - question: "Pourquoi la dette publique française augmente-t-elle ?"
    answer: "Sur {dyn.annee_depart}-{dyn.annee_fin}, le ratio dette/PIB est passé de {dyn.dette_depart} % à {dyn.dette_fin} %. En décomposant chaque année sa variation, les intérêts l'ont poussé de {dyn.effet_interets} points et la croissance du PIB nominal l'a freiné de {dyn.effet_croissance} : leur effet net n'est que de {dyn.effet_net} point. La hausse tient pour l'essentiel aux déficits primaires, l'écart entre dépenses et recettes publiques hors intérêts ({dyn.deficits_primaires} points), et pour le reste aux ajustements flux-stock ({dyn.flux_stock}). C'est une décomposition comptable : elle dit par quel terme la dette a monté, pas pourquoi les déficits ont existé."
  - question: "Les intérêts font-ils monter la dette ?"
    answer: "Oui, mais la croissance du PIB nominal les a presque compensés sur trente ans : {dyn.effet_interets} points de hausse d'un côté, {dyn.effet_croissance} points de baisse de l'autre. Ce solde dépend de l'écart entre le taux implicite de la dette et la croissance nominale : en {dyn.annee_fin}, ils étaient presque égaux ({dyn.taux_implicite_dernier} % et {dyn.croissance_derniere} %)."
  - question: "L'inflation fait-elle baisser la dette ?"
    answer: "Elle fait baisser le ratio, en gonflant le PIB nominal plus vite que la charge d'intérêts : de 2021 à 2023, l'effet taux-croissance a retiré {dyn.effet_2021_2023} points au ratio, alors que les déficits primaires en ajoutaient {dyn.deficits_2021_2023}. Elle ne le fait pas sans coût : elle réduit la valeur réelle des créances nominales, et cette perte a des porteurs."
  - question: "Un déficit primaire, est-ce trop de dépenses ?"
    answer: "Pas nécessairement : c'est un écart entre dépenses et recettes hors intérêts, qui peut venir de dépenses en hausse, de recettes en baisse, ou d'une récession qui fait les deux à la fois. Ces données mesurent l'écart ; elles ne disent pas lequel de ses deux termes il faudrait corriger."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 5
  nature: "Séries officielles (Eurostat) décomposées et calculs de l'auteur"
  en_francais: true
  titre_en: "Why does public debt rise?"
  nature_en: "Official series (Eurostat) decomposed, and author's calculations"
---

{{< dossier-dette volet="hausse" >}}
{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données Eurostat jusqu’en {{< dyn-val "annee_fin" >}}</span> France, administrations publiques, séries Eurostat de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}. Télécharger&nbsp;: <a href="/dette_dynamique.csv">CSV</a> · <a href="/dette_dynamique.json">JSON</a> · <a href="#sources">méthode</a></p>

Cette page ouvre un dossier en quatre questions&nbsp;: ce qui fait monter la dette, ce qu'elle coûte, qui en supporte les effets, et ce qui change ailleurs. Elle répond à la première à partir d'une identité comptable, appliquée année par année aux séries officielles.

## D'où vient la hausse {#cascade}

<figure class="figure-ciseau">
  <img src="/img/dette-dynamique-cascade.svg" alt="Cascade en points de PIB : la dette française part de {{< dyn-val "dette_depart" >}} % fin {{< dyn-val "annee_depart" >}} ; les intérêts l'auraient poussée de {{< dyn-val "effet_interets" >}} points, la croissance du PIB nominal en efface {{< dyn-val "effet_croissance" >}} ; les déficits primaires ajoutent {{< dyn-val "deficits_primaires" >}} points et les ajustements flux-stock {{< dyn-val "flux_stock" >}} ; la dette atteint {{< dyn-val "dette_fin" >}} % fin {{< dyn-val "annee_fin" >}}." width="720" height="386" loading="lazy">
  <figcaption>Décomposition cumulée de la variation du ratio dette/PIB, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}}, en points de PIB (Eurostat). Bleu&nbsp;: le stock&nbsp;; orange&nbsp;: ce qui le fait monter&nbsp;; gris&nbsp;: ce qui le fait baisser.</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur trente ans, les intérêts et la croissance du PIB nominal se sont presque annulés (effet net {{< dyn-val "effet_net" >}} point)&nbsp;: la hausse de la dette tient pour l'essentiel aux déficits primaires, {{< dyn-val "deficits_primaires" >}} points sur {{< dyn-val "hausse" >}}. C'est une décomposition comptable&nbsp;: elle dit par quel terme la dette a monté, pas pourquoi les déficits ont existé.

</div>

## Une identité, trois termes {#identite}

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

- **L'effet taux–croissance.** Les intérêts de l'année s'ajoutent à la dette&nbsp;; mais la croissance du PIB nominal — croissance réelle et inflation — fait baisser le ratio même sans remboursement. Le solde des deux est positif quand le taux implicite dépasse la croissance nominale, négatif dans le cas inverse.
- **Le déficit primaire.** L'écart entre dépenses et recettes publiques hors intérêts. Il ne dit pas si les dépenses sont trop hautes ou les recettes trop basses&nbsp;: il mesure l'écart, pas sa cause.
- **Les ajustements flux-stock.** La dette qui bouge sans passer par le déficit&nbsp;: trésorerie mise en réserve, prêts et participations, écarts de valorisation. Ils sont calculés ici comme résidu, et vérifiés contre le témoin comptable (variation de la dette moins déficit)&nbsp;: les deux coïncident chaque année.

## Année par année {#annee-par-annee}

<figure class="figure-ciseau">
  <img src="/img/dette-dynamique-annuelle.svg" alt="Barres empilées par année, de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}, en points de PIB : déficits primaires en orange, effet taux-croissance en bleu, ajustements flux-stock en gris, variation du ratio en point noir. Deux pics, 2009 et 2020 ; un effet taux-croissance fortement négatif en 2021-2023." width="720" height="356" loading="lazy">
  <figcaption>Contributions annuelles à la variation du ratio dette/PIB, France (Eurostat). La somme des trois barres égale la variation, marquée par le point noir.</figcaption>
</figure>

Trois périodes se dégagent, et le terme qui domine change de l'une à l'autre.

**{{< dyn-val "p1_lib" >}}&nbsp;: l'effet taux–croissance.** Le ratio gagne {{< dyn-val "p1_hausse" >}} points. Le taux implicite de la dette dépasse alors, en moyenne, la croissance nominale&nbsp;: l'effet taux–croissance ajoute {{< dyn-val "p1_taux_croissance" >}} points, quand le solde primaire, proche de l'équilibre et parfois excédentaire, contribue pour {{< dyn-val "p1_deficits" >}}.

**{{< dyn-val "p2_lib" >}}&nbsp;: les déficits primaires.** Le ratio gagne {{< dyn-val "p2_hausse" >}} points, dont {{< dyn-val "p2_deficits" >}} par les déficits primaires et {{< dyn-val "p2_taux_croissance" >}} par l'effet taux–croissance. L'année 2009 compte à elle seule {{< dyn-val "hausse_2009" >}} points&nbsp;: le déficit primaire se creuse et le PIB recule, deux effets qui coïncident avec la crise financière.

**{{< dyn-val "p3_lib" >}}&nbsp;: l'inflation freine, les déficits poussent.** Le ratio gagne {{< dyn-val "p3_hausse" >}} points. En 2020, il bondit de {{< dyn-val "hausse_2020" >}} points, avec la crise sanitaire. De 2021 à 2023, l'inflation gonfle le PIB nominal&nbsp;: l'effet taux–croissance retire {{< dyn-val "effet_2021_2023" >}} points au ratio, plus que les déficits primaires n'en ajoutent ({{< dyn-val "deficits_2021_2023" >}}), et le ratio baisse. Depuis 2024, l'inflation retombée, il remonte.

Sur les {{< dyn-val "annees_total" >}} années de la série, le solde primaire n'a été excédentaire que {{< dyn-val "annees_excedent" >}} fois.

## Ce que cette décomposition ne dit pas {#limites}

- **Une décomposition comptable, non une explication causale.** Elle dit par quel terme la dette a bougé&nbsp;; elle ne dit pas pourquoi les déficits ont existé, ni s'ils étaient évitables.
- **Des termes qui ne sont pas indépendants.** En récession, les recettes baissent et certaines dépenses montent&nbsp;: le déficit primaire dépend lui-même de la croissance.
- **L'inflation n'efface pas la dette sans coût.** Elle réduit la valeur réelle des créances nominales, et cette perte a des porteurs&nbsp;: c'est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- **Rien sur l'avenir.** La suite dépend de l'écart entre le taux implicite et la croissance nominale, et du solde primaire. En {{< dyn-val "annee_fin" >}}, taux implicite ({{< dyn-val "taux_implicite_dernier" >}}&nbsp;%) et croissance nominale ({{< dyn-val "croissance_derniere" >}}&nbsp;%) étaient presque égaux&nbsp;: l'effet taux–croissance était proche de zéro ({{< dyn-val "net_dernier" >}} point).
- **Une série qui commence en {{< dyn-val "annee_depart" >}}.** Les intérêts harmonisés d'Eurostat ne remontent pas plus loin&nbsp;; la courbe longue de la dette, depuis 1978, est dans [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique** — [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/) · [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/) · [Et ailleurs&nbsp;?](/dette-publique-comparaison-internationale/)

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page montre par quels termes la dette a monté. Elle ne dit pas qui en supporte le coût, ni par quels canaux il se déplace — vers le contribuable, vers l'épargnant par l'inflation, vers des services publics dont la marge se resserre — selon les décisions prises pour l'ajuster. Le livre suit ces canaux un par un, chiffres officiels à l'appui. À la fin, vous saurez qui paie vraiment une dette publique, et par quels canaux.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

Eurostat, administrations publiques (S.13), comptes nationaux SEC 2010, en monnaie nationale&nbsp;: dette de Maastricht (`gov_10dd_edpt1`), intérêts versés (`gov_10a_main`, D41PAY), capacité ou besoin de financement (B9), PIB nominal (`nama_10_gdp`). Le solde primaire est le solde des administrations publiques augmenté des intérêts versés. Chaque année, l'identité est appliquée telle qu'écrite plus haut&nbsp;; les ajustements flux-stock sont le résidu, et le script s'arrête si ce résidu diffère du témoin comptable calculé par une autre voie. Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent du même script, relancé à chaque publication des sources, qui s'arrête aussi si une phrase de la page cessait d'être vraie.

{{< reutiliser figures="figures_dynamique" jeu="dette_dynamique" sources="Eurostat" donnees="La décomposition annuelle de la variation du ratio dette/PIB, France, avec ses quatre termes, le taux implicite et la croissance nominale ; le même contenu existe en CSV, une ligne par année." >}}
Cette page décompose la variation du ratio dette/PIB français, de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}, en effet des intérêts, effet de la croissance nominale, solde primaire et ajustements flux-stock. Sur la période, intérêts et croissance nominale se sont presque annulés, et la hausse tient pour l'essentiel aux déficits primaires, hors intérêts. C'est une décomposition comptable, non une attribution causale&nbsp;: elle ne dit pas pourquoi les déficits ont existé.
{{< /reutiliser >}}
