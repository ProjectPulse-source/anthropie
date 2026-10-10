---
title: "La dette publique peut-elle baisser ?"
description: "De {baisse.d3_debut} à {baisse.annee_fin}, le poids de la dette française dans le PIB a monté de {baisse.d3_var_abs} points : les déficits primaires l'ont alourdi de {baisse.d3_def_abs}, l'effet des taux et de la croissance, favorable surtout en {baisse.d3_creux_lib}, l'a allégé de {baisse.d3_tc_abs}. Comparaison avec {baisse.cmp_autres_n} pays européens partis d'une dette plus élevée."
chapo: "Oui : son poids dans le PIB peut baisser même si son montant augmente, et il a baissé ailleurs. En France, de {baisse.d3_debut} à {baisse.annee_fin}, les déficits primaires, hors intérêts, ont dépassé l'allègement lié aux taux et à la croissance : le ratio dette/PIB a augmenté de {baisse.d3_var_abs} points."
og_title: "La dette publique peut-elle baisser ?"
og_image: "images/og-dette-baisse.jpg"
og_image_alt: "Carte de partage : « Les déficits ont pesé plus lourd » — France, trois décennies : effet des taux et de la croissance, déficits primaires et autres ajustements, en points de PIB."
date: 2026-10-02
lastmod: 2026-10-03
# Volet 5 du dossier dette (onglet depuis la barre A+ v2 du 03/10/2026), créé le 02/10/2026 sur décision de l'auteur (« construis la page autour du constat français »).
# Test décisif : D:\PRO\06_PROMOTION\RECHERCHE_SOLUTIONS_DETTE_2026-10-02\test_decisif\ ; contre-expertises et arbitrages :
# D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261002-195300_arbitrage.md (test) et PRO-20261003-064640_arbitrage.md (page) ; avis entrant final : ENTRANTE_2026-10-03_Solution_Dette_arbitrage.md.
# Décisions verrouillées : ni « presque nécessaire », ni « suffit », ni seuil de 2 % ; toute fréquence dit son événement, son
# dénominateur et sa période ; un ratio n'est pas un montant ; le solde stabilisant est dit « hors autres ajustements ».
# Aucun chiffre saisi : jetons {baisse.*} et shortcodes baisse-val / baisse-tableau (scripts/update_dette_baisse.py).
donnees: [dette_baisse]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_baisse"
  nom: "La dette publique peut-elle baisser : décomposition par décennie du ratio dette/PIB, France et pays de l'Union partis de plus de 90 % de dette"
  description: "Décomposition de la variation du ratio dette/PIB en effet des taux et de la croissance, déficits primaires et autres ajustements (flux-stock) : France par décennie de {baisse.annee_debut} à {baisse.annee_fin}, solde primaire observé et solde stabilisant hors autres ajustements année par année, et les pays de l'Union dont la dette dépassait {baisse.seuil_dette} % du PIB fin {baisse.cmp_veille}. Ratios contrôlés contre ceux que publie Eurostat ; aucune valeur saisie à la main."
  couverture_temporelle: "{baisse.annee_debut}/{baisse.annee_fin}"
  couverture_spatiale: "France ; Union européenne (27 pays)"
  variables:
    - {nom: "Variation du ratio dette/PIB", unite: "points de PIB", description: "cumulée sur dix ans"}
    - {nom: "Effet taux-croissance", unite: "points de PIB", description: "intérêts moins érosion du ratio par la croissance du PIB nominal"}
    - {nom: "Déficits primaires cumulés", unite: "points de PIB", description: "hors intérêts ; négatif en cas d'excédents"}
    - {nom: "Autres ajustements (flux-stock)", unite: "points de PIB", description: "résidu de l'identité"}
    - {nom: "Solde primaire stabilisant", unite: "% du PIB", description: "solde qui aurait laissé le ratio inchangé dans l'année, hors autres ajustements"}
    - {nom: "Encours de dette", unite: "milliards de monnaie nationale", description: "pays comparés, début et fin de la décennie"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
  mots: ["dette publique", "France", "excédent primaire", "solde primaire stabilisant", "taux implicite", "croissance nominale", "désendettement", "Eurostat"]
  fichiers: ["dette_baisse.csv", "dette_baisse.json"]
faq:
  - question: "La dette publique française peut-elle baisser ?"
    answer: "Les intérêts et les déficits primaires augmentent le ratio dette/PIB ; la croissance du PIB nominal et les excédents primaires le réduisent ; les autres ajustements jouent dans les deux sens. Le ratio baisse quand le bilan de ces contributions est négatif, même si le montant de la dette continue d'augmenter. De {baisse.d3_debut} à {baisse.annee_fin}, le ratio français a monté de {baisse.d3_var_abs} points : les déficits primaires l'ont alourdi de {baisse.d3_def_abs}, l'effet des taux et de la croissance l'a allégé de {baisse.d3_tc_abs}, surtout en {baisse.d3_creux_lib}. Sur la même décennie, il a baissé de {baisse.cmp_exc_baisse_min} à {baisse.cmp_exc_baisse_max} points dans {baisse.cmp_exc_n} pays partis d'une dette plus élevée, tous en excédent primaire moyen : {baisse.cmp_exc_pays}."
  - question: "La croissance et l'inflation suffisent-elles à faire baisser la dette ?"
    answer: "Elles allègent le ratio quand la croissance nominale dépasse le taux d'intérêt payé sur la dette, mais cet effet varie fortement d'une année à l'autre : en France, il a retiré {baisse.d3_creux_abs} points de {baisse.d3_creux_lib} et pesé {baisse.d3_pic_tc} points en {baisse.d3_pic_annee}. Dans les {baisse.cmp_n} pays de l'Union partis de plus de {baisse.seuil_dette} % de dette fin {baisse.cmp_veille}, il a été favorable partout, de {baisse.cmp_tc_min} à {baisse.cmp_tc_max} points en dix ans ; aucun de ceux qui sont restés en déficit primaire moyen n'a vu son ratio baisser de {baisse.forte_baisse} points."
  - question: "Quel solde primaire stabiliserait la dette française ?"
    answer: "Hors autres ajustements, c'est le solde qui compense l'effet des taux et de la croissance de l'année : il dépend de l'écart entre le taux implicite de la dette et la croissance nominale, et du niveau de la dette. En {baisse.annee_fin}, les deux taux étaient presque égaux ({baisse.taux_implicite_dernier} % et {baisse.croissance_derniere} %) : ce repère était proche de zéro, pour un solde observé de {baisse.pb_dernier} % du PIB. Il varie fortement, de {baisse.stab_min} % en {baisse.stab_min_annee} à {baisse.stab_max} % en {baisse.stab_max_annee}. Pour stabiliser le ratio observé, il faut aussi tenir compte des autres ajustements."
  - question: "La dette française est-elle soutenable ?"
    answer: "Aucun niveau de dette, à lui seul, ne tranche la question : elle dépend du solde primaire, de l'écart entre le taux que l'État paie et la croissance nominale, et de la confiance de ses prêteurs. Les deux premiers termes se mesurent. En {baisse.annee_fin}, taux implicite ({baisse.taux_implicite_dernier} %) et croissance nominale ({baisse.croissance_derniere} %) étaient presque égaux, et le solde primaire observé de {baisse.pb_dernier} % du PIB : le ratio a monté de {baisse.var_derniere} points. Au niveau de dette de {baisse.annee_fin} ({baisse.dette_derniere} % du PIB), un point supplémentaire d'écart entre le taux et la croissance relève d'environ {baisse.sens_pt} point de PIB le solde qui stabiliserait la dette, toutes choses égales par ailleurs ; le taux implicite, tombé à {baisse.ti_creux} % en {baisse.ti_creux_annee}, remonte à mesure que la dette se refinance. La confiance des prêteurs et l'accès au marché, eux, ne se lisent pas dans ces séries."
  - question: "La France a-t-elle déjà dégagé un excédent primaire ?"
    answer: "{baisse.exc_n_maj} fois depuis {baisse.annee_debut}, de {baisse.exc_premiere} à {baisse.exc_derniere}, au plus {baisse.exc_max} % du PIB (Eurostat). Depuis, le solde primaire des administrations publiques est resté déficitaire chaque année."
  - question: "Un excédent primaire fait-il toujours baisser la dette ?"
    answer: "Il contribue à réduire le ratio, mais la variation finale dépend aussi des taux, de la croissance et des autres ajustements : en France, le solde a atteint le repère de stabilisation hors ajustements en {baisse.suff_hausse} sans que le ratio baisse. Dans les fenêtres de dix ans des {baisse.eu_pays} pays aujourd'hui membres de l'Union où la dette de départ dépassait {baisse.seuil_dette} % du PIB, les baisses d'au moins {baisse.forte_baisse} points sont {baisse.eu_def_fb} sur {baisse.eu_def_n} avec un solde primaire moyen négatif, {baisse.eu_mid_fb} sur {baisse.eu_mid_n} avec un solde de 0 à moins de 2 %, {baisse.eu_exc_fb} sur {baisse.eu_exc_n} avec un solde d'au moins 2 % ; ces fenêtres se recouvrent et viennent de quelques pays."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 35
  nature: "Séries officielles (Eurostat) décomposées et calculs de l'auteur"
---

{{< dossier-dette volet="baisse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Mise à jour&nbsp;: {{< baisse-val "date_donnees" >}}</span> Administrations publiques, séries Eurostat de {{< baisse-val "annee_debut" >}} à {{< baisse-val "annee_fin" >}}. Télécharger&nbsp;: <a href="/dette_baisse.csv">CSV</a> · <a href="/dette_baisse.json">JSON</a> · <a href="#sources">méthode</a></p>

## Trois décennies, trois régimes {#trois-decennies}

<figure class="figure-ciseau">
  <img src="/img/dette-baisse-decennies.svg" alt="Trois groupes de barres en points de PIB cumulés sur dix ans : effet des taux et de la croissance (T), contribution des déficits ou excédents primaires (S), autres ajustements (A). {{< baisse-val "d1_lib" >}} : {{< baisse-val "d1_tc" >}}, {{< baisse-val "d1_def" >}}, {{< baisse-val "d1_sfa" >}}. {{< baisse-val "d2_lib" >}} : {{< baisse-val "d2_tc" >}}, {{< baisse-val "d2_def" >}}, {{< baisse-val "d2_sfa" >}}. {{< baisse-val "d3_lib" >}} : {{< baisse-val "d3_tc" >}}, {{< baisse-val "d3_def" >}}, {{< baisse-val "d3_sfa" >}}." width="720" height="408" loading="lazy">
  <figcaption>Ce qui a fait monter ou baisser le ratio dette/PIB français, par décennie, en points de PIB cumulés (Eurostat). Orange&nbsp;: ce qui le fait monter&nbsp;; gris&nbsp;: ce qui le fait baisser.</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< baisse-val "d3_debut" >}} à {{< baisse-val "annee_fin" >}}, les déficits primaires ont ajouté {{< baisse-val "d3_def_abs" >}} points au ratio de dette français, l'effet des taux et de la croissance, concentré en {{< baisse-val "d3_creux_lib" >}}, en a retiré {{< baisse-val "d3_tc_abs" >}}, et les autres ajustements en ont ajouté {{< baisse-val "d3_sfa_abs" >}}&nbsp;: le bilan est une hausse de {{< baisse-val "d3_var_abs" >}} points. C'est une décomposition comptable&nbsp;: elle dit par quel terme la dette a bougé, pas pourquoi les déficits ont existé.

</div>

Ce qui baisse ou monte ici, c'est le poids de la dette dans le PIB, non son montant&nbsp;: un ratio peut reculer pendant que la dette en euros augmente, si le PIB nominal croît plus vite. Ce ratio bouge sous l'effet de trois termes, détaillés dans [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)&nbsp;: l'effet taux-croissance (les intérêts, moins ce que la croissance du PIB nominal efface), le solde primaire (recettes moins dépenses, hors intérêts) et les autres ajustements, dits «&nbsp;flux-stock&nbsp;» (acquisitions d'actifs, variations de trésorerie et autres opérations qui modifient la dette sans passer par le déficit). En les cumulant par décennie, le terme qui pousse la dette change d'une période à l'autre.

**{{< baisse-val "d1_lib" >}}&nbsp;: les taux poussent, le budget hors intérêts est proche de l'équilibre.** Le ratio passe de {{< baisse-val "d1_dette_deb" >}}&nbsp;% à {{< baisse-val "d1_dette_fin" >}}&nbsp;% du PIB. Sur l'ensemble de la décennie, l'effet taux-croissance ajoute {{< baisse-val "d1_tc_abs" >}} points. Le solde primaire, excédentaire {{< baisse-val "d1_exc" >}} années sur dix, en retire {{< baisse-val "d1_def_abs" >}}.

**{{< baisse-val "d2_lib" >}}&nbsp;: les deux termes poussent ensemble.** Le ratio gagne {{< baisse-val "d2_var_abs" >}} points, la plus forte hausse des trois décennies&nbsp;: {{< baisse-val "d2_def_abs" >}} par les déficits primaires, {{< baisse-val "d2_tc_abs" >}} par l'effet taux-croissance. La période contient la crise financière de 2008-2009.

**{{< baisse-val "d3_lib" >}}&nbsp;: un effet taux-croissance favorable en cumul, dépassé par les déficits primaires.** Les intérêts ajoutent {{< baisse-val "d3_interets" >}} points, la croissance du PIB nominal en efface {{< baisse-val "d3_croissance" >}}&nbsp;: en cumul, l'effet taux-croissance est de {{< baisse-val "d3_tc" >}} points. Cet allègement se concentre en {{< baisse-val "d3_creux_lib" >}}, années de rebond de l'activité puis d'inflation, qui retirent à elles seules {{< baisse-val "d3_creux_abs" >}} points&nbsp;; les {{< baisse-val "d3_reste_n" >}} autres années pèsent ensemble {{< baisse-val "d3_reste" >}} point, dont {{< baisse-val "d3_pic_tc" >}} en {{< baisse-val "d3_pic_annee" >}}, quand le PIB reculait. Aucune année de la décennie n'est en excédent primaire&nbsp;: les déficits cumulés ajoutent {{< baisse-val "d3_def_abs" >}} points, plus que toute la hausse du ratio ({{< baisse-val "d3_var" >}}).

D'une décennie à l'autre, la contribution des déficits primaires est passée de {{< baisse-val "d1_def" >}} à {{< baisse-val "d2_def" >}} puis {{< baisse-val "d3_def" >}} points. Ce constat décrit une récurrence&nbsp;; il ne dit pas si ces déficits étaient évitables, ni lequel de leurs deux termes, dépenses ou recettes, les explique.

## Les pays partis d'une dette plus élevée {#pays-compares}

La même décomposition, sur la même décennie, s'applique aux pays de l'Union dont la dette dépassait {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB fin {{< baisse-val "cmp_veille" >}}&nbsp;: la France, à {{< baisse-val "cmp_fr_d0" >}}&nbsp;%, et {{< baisse-val "cmp_autres_n" >}} autres, tous partis de plus haut. Ce seuil est une convention de présentation, proche du niveau français&nbsp;; il ne fait pas de ces pays des expériences équivalentes.

<figure class="figure-ciseau">
  <img src="/img/dette-baisse-comparaison.svg" alt="Pour chacun des {{< baisse-val "cmp_n" >}} pays, trois barres en points de PIB cumulés de {{< baisse-val "cmp_lib" >}} : l'effet taux-croissance, négatif partout ; la contribution du solde primaire, négative dans {{< baisse-val "cmp_exc_n" >}} pays et positive dans {{< baisse-val "cmp_def_n" >}} ; les autres ajustements. France : effet taux-croissance {{< baisse-val "cmp_fr_tc" >}}, déficits primaires {{< baisse-val "cmp_fr_def" >}}, autres ajustements {{< baisse-val "cmp_fr_sfa" >}}, ratio {{< baisse-val "cmp_fr_var" >}} points." width="720" height="418" loading="lazy">
  <figcaption>Effet taux-croissance (T), contribution du solde primaire (S) et autres ajustements (A) à la variation du ratio de dette, {{< baisse-val "cmp_lib" >}}, en points de PIB cumulés (Eurostat). Pays triés par variation du ratio.</figcaption>
</figure>

<div class="encadre">

**Ce que le groupe permet de dire, et ce qu'il ne permet pas.** Dans ce groupe, les {{< baisse-val "cmp_exc_n" >}} fortes baisses du ratio s'accompagnent d'un excédent primaire moyen. Mais les contributions favorables des taux et de la croissance vont de {{< baisse-val "cmp_tc_min" >}} à {{< baisse-val "cmp_tc_max" >}} points&nbsp;: ce n'est pas un environnement commun. Et le constat dépend du périmètre&nbsp;: à 80&nbsp;%, le groupe compte {{< baisse-val "s80_n" >}} pays, avec {{< baisse-val "s80_ajouts" >}}&nbsp;; {{< baisse-val "s80_exc_pays" >}}, partie de {{< baisse-val "s80_exc_d0" >}}&nbsp;%, a vu son ratio baisser de {{< baisse-val "s80_exc_var" >}} points avec un solde primaire moyen de {{< baisse-val "s80_exc_pb" >}}&nbsp;% du PIB. À 100&nbsp;%, la France sort du groupe.

</div>

- **L'effet taux-croissance a fait baisser le ratio dans les {{< baisse-val "cmp_n" >}} pays**, de {{< baisse-val "cmp_tc_min" >}} à {{< baisse-val "cmp_tc_max" >}} points en dix ans. Celui de la France ({{< baisse-val "cmp_fr_tc" >}}) n'est pas le plus faible du groupe.
- **Le ratio a reculé de {{< baisse-val "cmp_exc_baisse_min" >}} à {{< baisse-val "cmp_exc_baisse_max" >}} points dans les {{< baisse-val "cmp_exc_n" >}} pays dont le solde primaire a été excédentaire en moyenne**&nbsp;: {{< baisse-val "cmp_exc_pays" >}}, avec un excédent moyen de {{< baisse-val "cmp_exc_pb_min" >}} à {{< baisse-val "cmp_exc_pb_max" >}}&nbsp;% du PIB. Le montant de leur dette, lui, n'a pas diminué&nbsp;: au Portugal, il est passé de {{< baisse-val "cmp_pt_enc0" >}} à {{< baisse-val "cmp_pt_enc1" >}} milliards d'euros. Leurs autres ajustements, positifs, ont freiné la baisse.
- **Il est resté à peu près stable pour {{< baisse-val "cmp_def_autres" >}}** ({{< baisse-val "cmp_def_var_min" >}} à {{< baisse-val "cmp_def_var_max" >}} points), en déficit primaire moyen. En Belgique, les contributions des taux et de la croissance et du solde primaire totalisent {{< baisse-val "cmp_be_tcdef" >}} points&nbsp;; les autres ajustements en ajoutent {{< baisse-val "cmp_be_sfa_abs" >}}, portant la variation à {{< baisse-val "cmp_be_var" >}} points.
- **Il a monté de {{< baisse-val "d3_var_abs" >}} points en France**, la plus forte hausse du groupe, avec le déficit primaire moyen le plus élevé ({{< baisse-val "cmp_fr_pb" >}}&nbsp;% du PIB).

<details class="repli"><summary>Les {{< baisse-val "cmp_n" >}} pays, terme par terme</summary>

{{< baisse-tableau >}}

</details>

Ces pays n'ont pas été financés dans les mêmes conditions. Le Portugal (de 2011 à mi-2014), Chypre (d'avril 2013 à mars 2016) et la Grèce (de mai 2010 à août 2018, dernier programme, financé par le Mécanisme européen de stabilité, d'août 2015 à août 2018) ont bénéficié de financements officiels de leurs partenaires européens et du FMI&nbsp;; l'Espagne a reçu, de juillet 2012 à janvier 2014, une aide à la recapitalisation de ses banques ([Commission européenne](https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries_en)&nbsp;; [Mécanisme européen de stabilité](https://www.esm.europa.eu/assistance/greece/greece-successfully-concludes-esm-programme)). La restructuration de la dette grecque, en 2012, précède la décennie étudiée. La croissance nominale moyenne des trois pays en excédent a dépassé celle de la France, ce qui accroît leur effet taux-croissance&nbsp;; et un solde primaire dépend lui-même de la conjoncture&nbsp;: une économie qui croît vite encaisse plus de recettes. Sept pays sur une décennie ne font pas une régularité générale, et la comparaison n'isole pas l'effet d'une politique.

## Quel solde stabiliserait la dette&nbsp;? {#solde-stabilisant}

Hors autres ajustements, le ratio de dette reste inchangé une année donnée si le solde primaire compense l'effet taux-croissance de cette année-là&nbsp;: c'est le repère tracé ci-dessous. Il n'est pas une constante&nbsp;: il monte quand le taux dépasse la croissance, et devient négatif dans le cas inverse, où un déficit primaire limité laisse le ratio stable. Pour stabiliser le ratio observé, il faut aussi tenir compte des autres ajustements&nbsp;: en {{< baisse-val "suff_hausse" >}}, le solde a atteint ce repère et le ratio a pourtant monté.

<figure class="figure-ciseau">
  <img src="/img/dette-baisse-stabilisant.svg" alt="Deux courbes annuelles de {{< baisse-val "annee_debut" >}} à {{< baisse-val "annee_fin" >}}, en % du PIB : le solde primaire observé, positif de {{< baisse-val "exc_premiere" >}} à {{< baisse-val "exc_derniere" >}} seulement, et le solde qui aurait stabilisé le ratio hors autres ajustements, de {{< baisse-val "stab_min" >}} % en {{< baisse-val "stab_min_annee" >}} (rebond du PIB) à {{< baisse-val "stab_max" >}} % en {{< baisse-val "stab_max_annee" >}} (recul du PIB)." width="720" height="372" loading="lazy">
  <figcaption>Solde primaire observé et solde primaire qui aurait stabilisé le ratio de dette dans l'année, hors autres ajustements, France, en&nbsp;% du PIB (Eurostat, calcul de l'auteur).</figcaption>
</figure>

En {{< baisse-val "annee_fin" >}}, taux implicite ({{< baisse-val "taux_implicite_dernier" >}}&nbsp;%) et croissance nominale ({{< baisse-val "croissance_derniere" >}}&nbsp;%) étaient presque égaux&nbsp;: le repère de stabilisation était proche de zéro. Le solde primaire observé était de {{< baisse-val "pb_dernier" >}}&nbsp;% du PIB, soit un écart de {{< baisse-val "ecart_dernier" >}} points.

Sur {{< baisse-val "annees_total" >}} ans, ce repère est allé de {{< baisse-val "stab_min" >}}&nbsp;% du PIB en {{< baisse-val "stab_min_annee" >}}, quand le PIB nominal rebondissait, à {{< baisse-val "stab_max" >}}&nbsp;% en {{< baisse-val "stab_max_annee" >}}, quand il reculait. Le solde observé l'a atteint ou dépassé {{< baisse-val "suffisant_n" >}} années sur {{< baisse-val "annees_total" >}}. Ce décompte mesure les années où le repère hors ajustements a été atteint&nbsp;; il ne correspond pas au nombre d'années de baisse effective du ratio, qui a reculé {{< baisse-val "suff_baisse_n" >}} de ces années. La France a dégagé un excédent primaire {{< baisse-val "exc_n" >}} fois, de {{< baisse-val "exc_premiere" >}} à {{< baisse-val "exc_derniere" >}}, au plus {{< baisse-val "exc_max" >}}&nbsp;% du PIB.

Stabiliser le ratio et le faire baisser sont deux objectifs distincts. Un montant d'ajustement se lit avec son objectif, son horizon et ses hypothèses&nbsp;; le repère calculé ici pour {{< baisse-val "annee_fin" >}} vaut pour cette année-là et ne permet pas d'évaluer les estimations pluriannuelles des institutions.

## La dette française est-elle soutenable&nbsp;? {#soutenable}

Aucun niveau de dette, à lui seul, ne tranche cette question. Une dette est dite soutenable quand l'État peut la servir et la refinancer sans un ajustement budgétaire hors de portée&nbsp;; cela dépend de son solde primaire, de l'écart entre le taux qu'il paie et la croissance nominale, et de la confiance de ceux qui lui prêtent. Les deux premiers termes se mesurent ici&nbsp;; le troisième, non.

**Ce que mesurent les données.** En {{< baisse-val "annee_fin" >}}, le solde qui aurait stabilisé le ratio, hors autres ajustements, était proche de zéro&nbsp;; le solde observé était de {{< baisse-val "pb_dernier" >}}&nbsp;% du PIB, et le ratio a monté de {{< baisse-val "var_derniere" >}} points. Aux taux et à la croissance de cette année-là, le stabiliser aurait demandé un solde primaire supérieur d'environ {{< baisse-val "ecart_dernier" >}} points de PIB&nbsp;; le faire baisser, davantage.

**Ce qui le rend fragile.** L'égalité de {{< baisse-val "annee_fin" >}} entre taux et croissance n'est pas un état acquis. Sur {{< baisse-val "annees_total" >}} ans, le taux implicite a dépassé la croissance nominale {{< baisse-val "rg_pos_n" >}} années. Tombé à {{< baisse-val "ti_creux" >}}&nbsp;% en {{< baisse-val "ti_creux_annee" >}}, il remonte, à mesure que la dette ancienne se refinance aux conditions de marché, pendant que la croissance nominale retombe après les années d'inflation&nbsp;: l'allègement de la dernière décennie tenait pour l'essentiel à {{< baisse-val "d3_creux_lib" >}}. Au niveau de dette et de croissance de {{< baisse-val "annee_fin" >}} ({{< baisse-val "dette_derniere" >}}&nbsp;% du PIB), et toutes choses égales par ailleurs, un point supplémentaire d'écart entre le taux et la croissance relève le solde stabilisant d'environ {{< baisse-val "sens_pt" >}} point de PIB&nbsp;: plus la dette est élevée, plus sa trajectoire dépend de taux que le budget ne commande pas.

**Ce que ces données ne disent pas.** La confiance des prêteurs, l'accès au marché et le coût des refinancements à venir dépendent de la maturité de la dette et de l'écart entre les taux de marché et le taux implicite (voir [la transmission](/dette-publique-comparaison-internationale/#transmission)), de ceux qui la détiennent ([Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)) et des décisions de la banque centrale. Les diagnostics de soutenabilité que publient les institutions reposent sur des projections conditionnelles, que ces données ne permettent ni de confirmer ni d'écarter.

## Trente ans de fenêtres européennes {#europe}

<details class="repli"><summary>Soldes primaires et baisses du ratio&nbsp;: les périodes européennes de dix ans</summary>

La comparaison ci-dessus ne porte que sur une décennie. Pour la replacer dans un ensemble plus large, la même décomposition a été appliquée à toutes les fenêtres de dix ans des {{< baisse-val "eu_pays" >}} pays aujourd'hui membres de l'Union, depuis {{< baisse-val "eu_premiere" >}}&nbsp;: {{< baisse-val "eu_fenetres" >}} fenêtres, qui se recouvrent, ne sont donc pas autant d'expériences indépendantes et contiennent la décennie déjà comparée. C'est un contexte, non une contre-épreuve.

Parmi les {{< baisse-val "eu_hautes_n" >}} fenêtres où la dette de départ dépassait {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB&nbsp;:

- **solde primaire moyen négatif**&nbsp;: {{< baisse-val "eu_def_n" >}} fenêtres, dans {{< baisse-val "eu_def_pays_n" >}} pays ({{< baisse-val "eu_def_pays" >}}). Le ratio baisse dans {{< baisse-val "eu_def_baisses" >}} d'entre elles, jamais de {{< baisse-val "forte_baisse" >}} points&nbsp;;
- **solde primaire moyen de 0 à moins de 2&nbsp;% du PIB**&nbsp;: {{< baisse-val "eu_mid_n" >}} fenêtres, dans {{< baisse-val "eu_mid_pays_n" >}} pays. Le ratio baisse dans {{< baisse-val "eu_mid_baisses" >}} d'entre elles, de {{< baisse-val "forte_baisse" >}} points ou plus dans {{< baisse-val "eu_mid_fb" >}}&nbsp;;
- **solde primaire moyen d'au moins 2&nbsp;% du PIB**&nbsp;: {{< baisse-val "eu_exc_n" >}} fenêtres, dans {{< baisse-val "eu_exc_pays_n" >}} pays seulement ({{< baisse-val "eu_exc_pays" >}}). Le ratio baisse dans les {{< baisse-val "eu_exc_baisses" >}}, de {{< baisse-val "forte_baisse" >}} points ou plus dans {{< baisse-val "eu_exc_fb" >}}.

Ces fréquences décrivent des périodes passées, dans quelques pays. Elles ne donnent ni un seuil d'excédent à atteindre, ni une probabilité de réussite&nbsp;: les fenêtres à fort excédent commencent pour la plupart avant 2003.

</details>

## Ce que ces données ne disent pas {#limites}

- **Mesure de la dette.** Une baisse du ratio ne signifie pas que le montant de dette a diminué. La dette suivie est brute&nbsp;: les autres ajustements mêlent achats d'actifs, prêts et écarts de valorisation, et un pays qui emprunte pour acquérir des actifs voit sa dette brute monter sans que sa situation financière se dégrade d'autant.
- **Interprétation économique.** Une décomposition comptable, non causale&nbsp;: les termes dépendent les uns des autres, et le solde observé contient la conjoncture, il ne mesure pas un effort. Rien ici ne dit lequel, des dépenses ou des recettes, devrait bouger, ni qui en supporterait le coût&nbsp;: c'est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/) L'effet taux-croissance repose sur le PIB nominal&nbsp;: la baisse du ratio par l'inflation réduit la valeur réelle des créances, elle a des porteurs.
- **Périmètre de comparaison.** Les 27 pays aujourd'hui membres de l'Union, depuis {{< baisse-val "eu_premiere" >}}&nbsp;; rien avant, rien hors de l'Union. Le groupe comparé dépend du seuil de dette et de la décennie retenus. {{< baisse-val "cons_ecartees_maj" >}} années-pays sur {{< baisse-val "cons_calculables" >}} sont écartées par le contrôle décrit plus bas.
- **Portée dans le temps.** La page décrit trente années observées. Les trajectoires que prévoient le Gouvernement, la Commission européenne ou le FMI sont des scénarios conditionnels, que ces données ne permettent ni de confirmer ni d'écarter.

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="le solde stabilisant et la distinction entre stabiliser et faire baisser sont retrouvés&nbsp;; lire l'écart nul de la dernière année comme un état durable, ou l'excédent comme le seul ressort des baisses, est mis en danger" >}}
**Mesuré ici.** La décomposition par décennie du ratio français, le solde stabilisant année par année et la comparaison des pays de l'Union partis de plus de {{< baisse-val "seuil_dette" >}}&nbsp;% de dette, sur les séries d'Eurostat. Aucun des textes lus ne calcule ces grandeurs sur cette source et ces périodes&nbsp;: elles se valident par reproduction.

**Cohérent avec.** Le solde primaire qui stabilise la dette dépend de l'écart entre taux et croissance et du niveau de la dette, dans la même identité de dynamique de la dette, exprimée en termes nominaux ici et en termes réels dans le Focus, chez Clavères (direction générale du Trésor), dans la Note n°&nbsp;82 du Conseil d'analyse économique (Auclert, Philippon et Ragot) et dans son Focus n°&nbsp;124 (Auclert, Barbara, Jaravel, Laveissière, Lasterra, Ragot et Renaud), qui part d'un écart nul, comme le repère de la page pour la dernière année. La Note distingue dans les mêmes termes stabiliser, qui exige un solde primaire nul quand taux et croissance sont égaux, et faire baisser, qui exige un excédent. Sur les pays du G7 depuis la fin du XIX<sup>e</sup>&nbsp;siècle, Clavères trouve que, dans la grande majorité des cas, les consolidations budgétaires réussies se sont appuyées à la fois sur un écart taux-croissance négatif et sur des excédents primaires. La direction générale du Trésor présente la stabilisation du ratio comme une condition nécessaire de la soutenabilité, qu'elle rattache aussi à la capacité de l'État à financer durablement sa dette&nbsp;; elle situe le solde stabilisant de 2025 à −2,1&nbsp;% du PIB, en solde public total, pour un déficit de 5,1&nbsp;%. Deux conventions différentes, et un écart à combler presque identique en 2025&nbsp;: environ trois points de PIB chez le Trésor, {{< baisse-val "ecart_dernier" >}} points mesurés ici en solde primaire. L'OFCE estime à 2,1 points, en 2024, l'écart entre le solde primaire et celui qui stabiliserait la dette&nbsp;; la mesure Eurostat de la page donne {{< baisse-val "ecart_prec" >}} points pour {{< baisse-val "annee_prec" >}}.

**Mis en danger par.** Deux lectures que la page doit éviter. La première ferait de l'excédent primaire le seul ressort des baisses&nbsp;: après 1945, c'est l'écart fortement négatif entre taux et croissance qui a le plus contribué à la baisse des dettes des économies avancées, les excédents primaires ayant aussi joué un rôle (Clavères)&nbsp;; au Portugal, l'excédent a coïncidé avec une croissance de 4,38&nbsp;% par an de 2015 à 2019, et en Italie, quand le taux dépassait la croissance, la dette a monté malgré un solde primaire structurel positif (Note du CAE). D'où la réserve de la page&nbsp;: la comparaison n'isole pas l'effet d'une politique. La seconde lirait l'écart nul de la dernière année comme un état durable&nbsp;: à l'automne 2025, l'État empruntait à 10&nbsp;ans à 3,5&nbsp;%, au-dessus d'un taux apparent estimé à 2,0&nbsp;% (Focus du CAE)&nbsp;; la hausse des taux ne se transmet au stock que progressivement, la maturité moyenne de la dette étant de 8,5&nbsp;ans en 2023, les valeurs futures de l'écart ne se prévoient pas, et, dans l'estimation de Clavères sur 18 économies avancées de 1950 à 2019, mesurée avec le taux à 10 ans, une dette plus élevée va de pair avec un écart plus élevé l'année suivante, estimation que son auteur dit à prendre avec précaution. La direction générale du Trésor écrit, elle aussi, que la remontée des taux inverse la période d'écart négatif et exige désormais un léger excédent primaire, et que la hausse des taux se répercute sur le stock à mesure qu'il est refinancé. Le diagnostic n'est pas unanime&nbsp;: l'OFCE tient la hausse de la charge d'intérêts pour probable, mais son ampleur pour moins certaine que dans les projections officielles. Renouveler au taux à 10 ans de juillet 2025 les 900 milliards d'euros de titres arrivant à échéance d'ici 2029 coûterait environ 0,5 point de PIB&nbsp;; les auteurs le rapprochent d'une hausse totale de 1,2 point projetée par le FMI, sans que les deux calculs aient le même périmètre. Son modèle suppose en outre un taux apparent inférieur à la croissance nominale à partir de 2026. Enfin, la Note du CAE avance qu'il serait difficile de laisser la dette dépasser 125&nbsp;% du PIB sans risquer une forte hausse des taux, et le Focus retient 130&nbsp;% comme plafond de son modèle, le niveau de la Grèce en 2009&nbsp;: le premier chiffre est motivé par l'observation de quelques cas européens, le second est un paramètre choisi&nbsp;; aucun n'est un seuil estimé, ce qui laisse intacte la phrase de la page selon laquelle aucun niveau de dette, à lui seul, ne tranche la question.

**Non établi.** Le montant de l'effort. Les 112&nbsp;milliards d'euros du Focus du CAE font 3,7&nbsp;points de PIB&nbsp;: un déficit primaire **structurel** estimé de 2,7&nbsp;points, prévu en octobre 2025, et un point de marge pour la crise suivante. Ils ne se comparent pas terme à terme à l'écart observé de la page pour {{< baisse-val "annee_fin" >}}, hors autres ajustements. L'OFCE (Heyer, Plane, Ragot, Sampognaro et Timbeau) chiffre à 2,8&nbsp;points de PIB d'ici 2029 un ajustement progressif qui stabiliserait la dette à 110&nbsp;%, 2,5&nbsp;points avec des taux plus bas&nbsp;: une projection de modèle. L'accès au marché&nbsp;: aucun des six textes ne le mesure&nbsp;; la direction générale du Trésor invoque la crédibilité auprès des investisseurs sans la mesurer.

**Références lues**

- Auclert, A., Philippon, T. et Ragot, X., «&nbsp;Quelle trajectoire pour les finances publiques françaises&nbsp;?&nbsp;», *Les notes du Conseil d'analyse économique*, n°&nbsp;82, juillet 2024.
- Auclert, A., Barbara, M.-A., Jaravel, X., Laveissière, E., Lasterra, O., Ragot, X. et Renaud, D., «&nbsp;Comment stabiliser la dette publique&nbsp;?&nbsp;», *Focus du Conseil d'analyse économique*, n°&nbsp;124, octobre 2025.
- Clavères, G., «&nbsp;Taux d'intérêt, croissance et soutenabilité de la dette publique&nbsp;», *Trésor-Éco*, n°&nbsp;334, direction générale du Trésor, octobre 2023.
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., «&nbsp;Quelles trajectoires pour les finances publiques de la France&nbsp;?&nbsp;», *Blog de l'OFCE*, 2025.
- Direction générale du Trésor, «&nbsp;Finances publiques&nbsp;: une situation dégradée, un redressement nécessaire&nbsp;», *Trésor-Éco*, n°&nbsp;403, septembre 2026.
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., «&nbsp;Quelles trajectoires pour les finances publiques de la France&nbsp;?&nbsp;», document de travail de l'OFCE n°&nbsp;13, juillet 2025.
{{< /confrontation-recherche >}}

<div class="retenir">

## Ce qu'il faut retenir {#retenir}

Le poids d'une dette peut baisser sans que son montant diminue, et il a baissé ailleurs&nbsp;: parmi les pays de l'Union partis d'une dette plus élevée que la France, le ratio a reculé de {{< baisse-val "cmp_exc_baisse_min" >}} à {{< baisse-val "cmp_exc_baisse_max" >}} points en dix ans dans les {{< baisse-val "cmp_exc_n" >}} qui ont dégagé un excédent primaire moyen, sans que leur dette en euros diminue.

En France, sur la même décennie, les taux et la croissance ont aidé&nbsp;: {{< baisse-val "d3_tc_abs" >}} points de moins, surtout en {{< baisse-val "d3_creux_lib" >}}. Les déficits primaires ont pesé davantage, {{< baisse-val "d3_def_abs" >}} points, et le ratio a monté de {{< baisse-val "d3_var_abs" >}} points.

Cette aide s'est éteinte&nbsp;: en {{< baisse-val "annee_fin" >}}, taux implicite et croissance nominale étaient presque égaux. À ces conditions, et hors autres ajustements, un solde primaire inchangé ferait monter le ratio d'environ {{< baisse-val "ecart_dernier" >}} points par an&nbsp;; le stabiliser demande de combler cet écart, le faire baisser d'aller au-delà. Et, à ce niveau de dette, un point supplémentaire d'écart entre le taux et la croissance relèverait d'environ {{< baisse-val "sens_pt" >}} point de PIB le solde à atteindre.

Ces comparaisons ne disent ni quelle politique produirait ce résultat, ni à quel prix&nbsp;: les pays en excédent ont eu une croissance nominale plus forte que la France, et trois d'entre eux des financements officiels. Qui supporterait l'ajustement est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)
- [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Et ailleurs&nbsp;?](/dette-publique-comparaison-internationale/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page décompose la hausse du ratio de dette français et les baisses observées ailleurs. Faire baisser ce ratio peut déplacer des coûts. Qui les supporte&nbsp;: le contribuable, l'usager des services publics, l'épargnant par l'inflation, le créancier par une restructuration&nbsp;? Le livre prolonge cette analyse, chiffres officiels à l'appui, en examinant ces choix et leurs conséquences.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

Eurostat, administrations publiques (S.13), comptes SEC 2010, en monnaie nationale&nbsp;: dette de Maastricht et PIB nominal publiés avec la notification de déficit et de dette (`gov_10dd_edpt1`), intérêts versés et capacité ou besoin de financement (`gov_10a_main`, D41PAY et B9). Le solde primaire est le solde des administrations publiques augmenté des intérêts versés. L'identité est celle du volet [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/#identite)&nbsp;; les termes annuels sont cumulés sur dix ans, de la fin de l'année qui précède la décennie à la fin de sa dernière année. Le solde stabilisant d'une année est l'effet taux-croissance de cette année, hors autres ajustements. Les variations et totaux sont calculés avant arrondi&nbsp;: les nombres affichés peuvent présenter un écart de 0,1 point.

Contrôle&nbsp;: pour chaque pays et chaque année, le ratio de dette et le solde primaire calculés sont comparés à ceux qu'Eurostat publie en pourcentage du PIB, que le calcul n'utilise pas. Au-delà de {{< baisse-val "tolerance" >}} point d'écart, l'année est écartée et comptée ({{< baisse-val "cons_ecartees" >}} sur {{< baisse-val "cons_calculables" >}}, listées dans le fichier JSON)&nbsp;; pour la France et les pays comparés, le script s'arrête. Une fenêtre qui contient une année de croissance nominale supérieure à 35&nbsp;% (hyperinflation, rupture de série) est écartée. Les pays comparés à la France sont désignés par une règle, non choisis&nbsp;: dette supérieure à {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB à la fin de {{< baisse-val "cmp_veille" >}}&nbsp;; le même calcul est refait à 80 et à 100&nbsp;%. Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent du même script, qui vérifie les principales affirmations chiffrées et s'arrête si leurs conditions ne sont plus remplies&nbsp;; leur formulation fait l'objet d'une relecture éditoriale.

{{< reutiliser figures="figures_baisse" jeu="dette_baisse" sources="Eurostat" donnees="La décomposition par décennie du ratio dette/PIB français, le solde primaire observé et le solde stabilisant hors autres ajustements année par année, et la même décomposition pour les pays de l'Union partis de plus de 90 % de dette ; le même contenu existe en CSV, au format long." >}}
De {{< baisse-val "d3_debut" >}} à {{< baisse-val "annee_fin" >}}, les déficits primaires ont ajouté {{< baisse-val "d3_def_abs" >}} points de PIB au ratio de dette français, l'effet des taux et de la croissance, concentré en {{< baisse-val "d3_creux_lib" >}}, en a retiré {{< baisse-val "d3_tc_abs" >}}, et les autres ajustements en ont ajouté {{< baisse-val "d3_sfa_abs" >}}&nbsp;: une hausse de {{< baisse-val "d3_var_abs" >}} points. Parmi les {{< baisse-val "cmp_n" >}} pays de l'Union partis de plus de {{< baisse-val "seuil_dette" >}}&nbsp;% de dette fin {{< baisse-val "cmp_veille" >}}, les baisses de plus de {{< baisse-val "forte_baisse" >}} points sont celles des {{< baisse-val "cmp_exc_n" >}} pays en excédent primaire moyen, un constat qui dépend du seuil retenu. C'est une décomposition comptable, non une attribution causale.
{{< /reutiliser >}}
