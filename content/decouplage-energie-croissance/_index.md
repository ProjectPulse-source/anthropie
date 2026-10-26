---
title: "L'économie mondiale se découple-t-elle de l'énergie ?"
description: "De {dc.an0} à {dc.an1}, l'énergie consommée par unité de PIB a baissé de {dc.di_pct} % dans le monde, et la consommation d'énergie a augmenté de {dc.de_pct} %. Décomposée, la hausse tient plus au PIB par habitant qu'à la population ; dans l'Union européenne, la consommation a baissé (EIA, calcul de l'auteur)."
chapo: "L'économie mondiale consomme de moins en moins d'énergie pour chaque unité de richesse produite : {dc.di_pct} % de moins en {dc.an1} qu'en {dc.an0}. Sa consommation d'énergie, elle, a augmenté de {dc.de_pct} % sur la même période. La baisse de l'intensité énergétique a freiné la hausse ; elle ne l'a pas renversée."
date: 2026-10-26
lastmod: 2026-10-26
journal:  # révisions qui changent la lecture de la page (contre-expertise du 26/10/2026)
  - {date: 2026-10-26, texte: "Correction : le recalcul de contrôle reposait sur une série d'énergie primaire d'Our World in Data en méthode de substitution, attribuée à tort à l'Energy Institute, qui a adopté en 2025 la méthode du contenu physique ; il repose désormais sur l'offre totale d'énergie de l'Energy Institute (baisse européenne de 2000 à 2024 : 17 % au lieu de 12 %). La convention de l'EIA est vérifiée pour l'éolien comme pour l'hydraulique, pas pour le solaire. Ajouts : variante du PIB aux taux de change de marché, comparaison avec Eurostat ; « revenu par habitant » devient « PIB par habitant »."}
og_title: "L'économie mondiale se découple-t-elle de l'énergie ? — S. Lalut"
og_image: "images/og-decouplage.jpg"
og_image_alt: "Carte de partage : « L'intensité baisse, la consommation monte » — effets de la population, du PIB par habitant et de l'intensité énergétique sur la consommation mondiale d'énergie (EIA)."
# Page née de l'arbitrage PRO-20261026-033434 (graphe G2 transformé : le découplage et ses limites, non le rebond).
# Fiche : docs/conception/decouplage-energie-croissance.md. Aucun chiffre saisi : jetons {dc.*} et shortcode dc-val
# (scripts/update_decouplage.py, fichier groupé international de l'EIA ; témoin Energy Institute et Banque mondiale).
donnees: [decouplage]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "decouplage"
  nom: "Consommation d'énergie, PIB et population, monde et Union européenne, et décomposition de la variation de la consommation (EIA)"
  description: "Consommation d'énergie primaire, PIB en parité de pouvoir d'achat à prix constants et population, monde et Union européenne à 27, séries annuelles de l'EIA ; décomposition de la variation de la consommation de {dc.an0} à {dc.an1} en effets de la population, du PIB par habitant et de l'intensité énergétique (indice de Divisia), calculée par l'auteur, avec un recalcul sur les données de l'Energy Institute et de la Banque mondiale, une variante aux taux de change de marché et une comparaison avec Eurostat pour l'Union européenne."
  couverture_temporelle: "1980/{dc.an1}"
  couverture_spatiale: "Monde ; Union européenne (27 pays)"
  variables:
    - {nom: "Consommation d'énergie primaire", unite: "térajoules", description: "convention de l'EIA, par zone et par année"}
    - {nom: "PIB en parité de pouvoir d'achat", unite: "milliards de dollars, prix constants", description: "par zone et par année"}
    - {nom: "Population", unite: "milliers de personnes", description: "par zone et par année"}
  sources:
    - "https://www.eia.gov/international/data/world"
    - "https://www.energyinst.org/statistical-review"
    - "https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.KD"
    - "https://data.worldbank.org/indicator/NY.GDP.MKTP.KD"
    - "https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_eff/default/table"
  mots: ["découplage", "intensité énergétique", "consommation d'énergie", "efficacité énergétique", "effet rebond", "paradoxe de Jevons", "transition énergétique", "sobriété", "énergie primaire", "PIB", "EIA"]
  fichiers: ["decouplage.csv", "decouplage.json"]
faq:
  - question: "La consommation mondiale d'énergie baisse-t-elle ?"
    answer: "Non. De {dc.an0} à {dc.an1}, elle est passée de {dc.e0} à {dc.e1} exajoules, une hausse de {dc.de_pct} %, alors que l'énergie consommée par unité de PIB a baissé de {dc.di_pct} %. C'est un découplage relatif : la consommation croît moins vite que l'économie, sans baisser."
  - question: "La hausse de la consommation d'énergie vient-elle surtout de la croissance démographique ?"
    answer: "Pas d'abord. Dans une décomposition comptable de la hausse de {dc.an0} à {dc.an1}, l'effet du PIB par habitant ({dc.rev_ej} exajoules) pèse {dc.ratio_rp} fois plus que celui de la population ({dc.pop_ej}), et la baisse de l'intensité énergétique en retire {dc.int_ej}. La décomposition dit combien chaque terme a pesé, pas pourquoi."
  - question: "Un pays ou une région peut-il consommer moins d'énergie tout en s'enrichissant ?"
    answer: "Oui, sur son territoire : dans l'Union européenne, la consommation d'énergie primaire a baissé de {dc.ue_de_pct} % de {dc.an0} à {dc.an1} pendant que le PIB augmentait de {dc.ue_dy_pct} %. Ces données ne comptent pas l'énergie contenue dans les biens importés : elles ne disent pas si la baisse tient à l'efficacité, au changement de l'économie ou au déplacement de productions hors d'Europe."
  - question: "D'où viennent ces chiffres ?"
    answer: "Des données internationales de l'EIA (énergie, PIB en parité de pouvoir d'achat à prix constants, population), lues par un script qui s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases de la page, et recalculées sur les données de l'Energy Institute, de la Banque mondiale et d'Eurostat. Une seule valeur est transcrite à la main : le total mondial publié par l'Energy Institute pour {dc.an_ei_publie}, qui sert à vérifier la provenance du recalcul. Les données sont téléchargeables en CSV et en JSON, sous licence CC BY 4.0."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/decouplage-energie-croissance.md"  # fiche de conception (regle 12)
  refonte: "2026-10-26"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["anthropie-ordre-ici-dette-ailleurs"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 50
  nature: "Données publiques recalculées (EIA, Energy Institute, Banque mondiale)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données du&nbsp;: {{< dc-val "date_donnees" >}}</span> EIA, données internationales&nbsp;: consommation d'énergie primaire, PIB en parité de pouvoir d'achat à prix constants et population, monde et Union européenne, de 1980 à {{< dc-val "an1" >}}. Télécharger&nbsp;: <a href="/decouplage.csv">CSV</a> · <a href="/decouplage.json">JSON</a></p>

## L'intensité baisse, la consommation monte {#paradoxe}

De {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, le PIB mondial, mesuré en parité de pouvoir d'achat à prix constants, a augmenté de {{< dc-val "dy_pct" >}}&nbsp;%. L'énergie consommée pour produire chaque unité de ce PIB, l'intensité énergétique, a baissé de {{< dc-val "di_pct" >}}&nbsp;%. Et la consommation mondiale d'énergie primaire est passée de {{< dc-val "e0" >}} à {{< dc-val "e1" >}}&nbsp;exajoules (un exajoule vaut un milliard de milliards de joules)&nbsp;: {{< dc-val "de_pct" >}}&nbsp;% de plus.

L'économie mondiale s'est donc découplée de l'énergie au sens relatif&nbsp;: sa consommation croît moins vite que sa production. Elle ne s'en est pas découplée au sens absolu, où la consommation baisserait pendant que l'économie croît.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/decouplage-decomposition-m.svg" width="300" height="865">
    <img src="/img/decouplage-decomposition.svg" alt="Décomposition de la variation de la consommation d'énergie primaire de {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, en % de la consommation de {{< dc-val "an0" >}}. Monde : effet de la population {{< dc-val "w_pop_pct" >}} %, effet du PIB par habitant {{< dc-val "w_rev_pct" >}} %, effet de l'intensité énergétique {{< dc-val "w_int_pct" >}} %, variation de la consommation {{< dc-val "w_tot_pct" >}} %. Union européenne : effet de la population {{< dc-val "u_pop_pct" >}} %, effet du PIB par habitant {{< dc-val "u_rev_pct" >}} %, effet de l'intensité énergétique {{< dc-val "u_int_pct" >}} %, variation de la consommation {{< dc-val "u_tot_pct" >}} %." width="720" height="441" loading="lazy">
  </picture>
  <figcaption>Énergie primaire consommée sur le territoire, convention de l'EIA&nbsp;; effets calculés par un indice de Divisia, qui s'additionnent exactement à la variation (EIA, données internationales).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, la consommation mondiale d'énergie a augmenté de {{< dc-val "de_pct" >}}&nbsp;%&nbsp;: la décomposition attribue {{< dc-val "poussee_ej" >}}&nbsp;exajoules de hausse à la population et au PIB par habitant, et seulement {{< dc-val "int_ej" >}} de baisse à l'intensité énergétique.

</div>

## Démographie ou enrichissement&nbsp;? {#demographie-revenu}

On lit souvent que la consommation d'énergie augmente parce que la population mondiale augmente. Une décomposition comptable sépare les deux. La consommation d'énergie est le produit de trois termes&nbsp;: la population, le PIB par habitant et l'énergie consommée par unité de PIB. De {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, la décomposition attribue {{< dc-val "pop_ej" >}}&nbsp;exajoules à l'effet de la population, {{< dc-val "rev_ej" >}} à celui du PIB par habitant et −{{< dc-val "int_ej" >}} à la baisse de l'intensité&nbsp;: au total, {{< dc-val "tot_ej" >}}&nbsp;exajoules de plus.

Le PIB par habitant a donc pesé {{< dc-val "ratio_rp" >}}&nbsp;fois plus que la démographie. Ce rang ne dépend pas de l'année de départ&nbsp;: dans chacune des fenêtres testées, qui partent de {{< dc-val "fenetres" >}} et s'arrêtent en {{< dc-val "an1" >}}, l'effet du PIB par habitant dépasse celui de la population, et la consommation a augmenté.

<details class="repli">
<summary>Les cinq fenêtres, en exajoules</summary>

| Départ | Effet de la population | Effet du PIB par habitant | Effet de l'intensité | Variation de la consommation |
|---|---|---|---|---|
| 1990 | {{< dc-val "f1990_pop" >}} | {{< dc-val "f1990_rev" >}} | {{< dc-val "f1990_int" >}} | {{< dc-val "f1990_tot" >}} |
| 2000 | {{< dc-val "f2000_pop" >}} | {{< dc-val "f2000_rev" >}} | {{< dc-val "f2000_int" >}} | {{< dc-val "f2000_tot" >}} |
| 2010 | {{< dc-val "f2010_pop" >}} | {{< dc-val "f2010_rev" >}} | {{< dc-val "f2010_int" >}} | {{< dc-val "f2010_tot" >}} |
| 2015 | {{< dc-val "f2015_pop" >}} | {{< dc-val "f2015_rev" >}} | {{< dc-val "f2015_int" >}} | {{< dc-val "f2015_tot" >}} |
| 2019 | {{< dc-val "f2019_pop" >}} | {{< dc-val "f2019_rev" >}} | {{< dc-val "f2019_int" >}} | {{< dc-val "f2019_tot" >}} |

Chaque fenêtre s'arrête en {{< dc-val "an1" >}}&nbsp;; monde, EIA. Valeurs arrondies à l'exajoule&nbsp;: leur somme peut différer d'une unité du total.

</details>

**Une décomposition comptable n'est pas une explication.** Elle dit combien chaque terme a pesé, pas pourquoi. Elle ne dit pas que l'enrichissement cause la hausse de la consommation, ni que la baisse de l'intensité vient de l'efficacité des usages&nbsp;: l'intensité baisse aussi quand l'économie se tourne vers les services, ou quand une convention de mesure compte autrement l'électricité. Elle ne permet pas, non plus, d'estimer un effet rebond.

<details class="repli">
<summary>Pourquoi l'effet de l'intensité (−{{< dc-val "int_ej" >}}&nbsp;exajoules) dépasse la baisse de l'intensité elle-même</summary>

Les {{< dc-val "di_pct" >}}&nbsp;% mesurent la variation de l'intensité&nbsp;; les {{< dc-val "int_ej" >}}&nbsp;exajoules, sa contribution à la variation de la consommation. La décomposition mesure chaque variation en logarithme, ce qui rend la somme des effets exacte. L'intensité a été multipliée par {{< dc-val "ratio_i" >}} (une baisse de {{< dc-val "di_pct" >}}&nbsp;%), dont le logarithme vaut {{< dc-val "ln_i" >}}. Cette valeur s'applique à la consommation moyenne de la période, {{< dc-val "lmoy_ej" >}}&nbsp;exajoules (une moyenne dite logarithmique, entre {{< dc-val "e0" >}} et {{< dc-val "e1" >}})&nbsp;: d'où un effet de −{{< dc-val "int_ej" >}}&nbsp;exajoules. Rapporté aux {{< dc-val "e0" >}}&nbsp;exajoules de {{< dc-val "an0" >}}, il vaut {{< dc-val "int_pct_e0" >}}&nbsp;%, le chiffre de la figure&nbsp;: c'est la même baisse de l'intensité, mesurée sur une base plus large, pas une seconde baisse.

</details>

## L'Union européenne&nbsp;: un découplage absolu, sur son territoire {#union-europeenne}

Le même producteur, avec la même définition, donne pour l'Union européenne à 27 l'autre cas de figure. De {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, sa consommation d'énergie primaire a baissé de {{< dc-val "ue_de_pct" >}}&nbsp;%, de {{< dc-val "ue_e0" >}} à {{< dc-val "ue_e1" >}}&nbsp;exajoules, pendant que son PIB augmentait de {{< dc-val "ue_dy_pct" >}}&nbsp;%&nbsp;; elle culmine en {{< dc-val "an_pic_ue" >}}. L'effet de la population y ajoute {{< dc-val "ue_pop_ej" >}}&nbsp;exajoules, celui du PIB par habitant {{< dc-val "ue_rev_ej" >}}, et la baisse de l'intensité, {{< dc-val "ue_di_pct" >}}&nbsp;%, en retire {{< dc-val "ue_int_ej" >}}&nbsp;: plus que les deux autres réunis.

**L'année d'arrivée compte.** En s'arrêtant en 2019, avant la pandémie et la flambée des prix de l'énergie de 2022, la consommation européenne baisse de {{< dc-val "ue19_de_pct" >}}&nbsp;% depuis {{< dc-val "an0" >}}, pour un PIB en hausse de {{< dc-val "ue19_dy_pct" >}}&nbsp;%. Le découplage absolu est déjà là, mais plus de la moitié de la baisse mesurée jusqu'en {{< dc-val "an1" >}} est intervenue après 2019&nbsp;; ces données ne disent pas quelle part en durera.

**Ce que la comparaison ne dit pas.** Ces chiffres comptent l'énergie consommée sur le territoire européen, pas celle qui a servi à fabriquer les biens que l'Europe importe. Ils ne permettent donc pas de dire si la baisse tient à l'efficacité, au recul des industries les plus consommatrices d'énergie ou à leur déplacement hors d'Europe. Pour trancher, il faudrait une empreinte énergétique de la demande européenne, que nous n'avons pas trouvée publiée sous une forme réutilisable.

## Le résultat dépend-il de la source&nbsp;? {#robustesse}

**Une convention de mesure, vérifiée année par année.** L'énergie primaire ne se compte pas de la même façon partout. Dans les fichiers de l'EIA, nous mesurons chaque année de {{< dc-val "an_conv0" >}} à {{< dc-val "an_conv" >}} le rapport entre l'énergie comptée et l'électricité produite&nbsp;: {{< dc-val "btu_hydro" >}}&nbsp;Btu par kilowattheure pour l'hydraulique et l'éolien, c'est-à-dire leur contenu électrique, sans rupture de convention&nbsp;; de {{< dc-val "btu_nuc_min" >}} à {{< dc-val "btu_nuc_max" >}}&nbsp;Btu pour le nucléaire, compté à la chaleur du réacteur. Le solaire est compté à {{< dc-val "btu_sol" >}}&nbsp;Btu en {{< dc-val "an_conv" >}}, à un rapport plus élevé les années précédentes, où il pesait très peu. L'Energy Institute, qui publie la *Statistical Review of World Energy*, applique la même logique de contenu physique depuis son édition de 2025&nbsp;: la comparaison qui suit éprouve un autre producteur, pas une autre convention.

**Un autre producteur.** Avec l'offre totale d'énergie de l'Energy Institute (édition {{< dc-val "edition_ei" >}}&nbsp;: {{< dc-val "t_e1" >}}&nbsp;exajoules en {{< dc-val "an_t" >}}) et le PIB et la population de la Banque mondiale, la décomposition garde le même ordre&nbsp;: consommation mondiale en hausse de {{< dc-val "t_de_pct" >}}&nbsp;% de {{< dc-val "an0" >}} à {{< dc-val "an_t" >}}&nbsp;; effet du PIB par habitant {{< dc-val "t_rev_ej" >}}&nbsp;exajoules, de la population {{< dc-val "t_pop_ej" >}}, de l'intensité −{{< dc-val "t_int_ej" >}}. Pour l'Union européenne, la baisse est de {{< dc-val "t_ue_de_pct" >}}&nbsp;% au lieu de {{< dc-val "ue_de_pct" >}}&nbsp;%. Eurostat, qui ne publie son indicateur de consommation d'énergie primaire que depuis {{< dc-val "an_es" >}}, donne la même ampleur à quelques points près&nbsp;: de {{< dc-val "an_es" >}} à {{< dc-val "an1" >}}, la consommation de l'Union baisse de {{< dc-val "es_es_pct" >}}&nbsp;% selon Eurostat, de {{< dc-val "es_ei_pct" >}}&nbsp;% selon l'Energy Institute et de {{< dc-val "es_eia_pct" >}}&nbsp;% selon l'EIA. Les niveaux diffèrent davantage ({{< dc-val "es_ej" >}}&nbsp;exajoules en {{< dc-val "an1" >}} chez Eurostat, {{< dc-val "ue_e1" >}} chez l'EIA)&nbsp;: l'indicateur d'Eurostat ne compte pas, notamment, les usages non énergétiques des combustibles.

**La conversion du PIB compte.** Les chiffres de cette page convertissent le PIB en parité de pouvoir d'achat. Aux taux de change de marché, le PIB mondial augmente de {{< dc-val "m_dy_pct" >}}&nbsp;% de {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, et l'intensité ne baisse que de {{< dc-val "m_di_pct" >}}&nbsp;%&nbsp;; l'effet du PIB par habitant tombe à {{< dc-val "m_rev_ej" >}}&nbsp;exajoules et celui de l'intensité à −{{< dc-val "m_int_ej" >}}, celui de la population ne change pas. Sous les deux conversions, dans chaque fenêtre, la consommation monte, l'intensité baisse et le PIB par habitant pèse plus que la population. L'ampleur de la baisse de l'intensité, elle, dépend de la conversion&nbsp;: aux taux de marché, de {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, elle retire moins que la population n'ajoute.

## Confrontation à la recherche {#recherche}

Paul Brockway et quatre coauteurs, chercheurs en économie et en ingénierie de l'énergie (universités de Leeds, du Sussex, du Massachusetts, SOAS et Calvin, IFP Énergies nouvelles), ont passé en revue en 2021 trente-trois études qui estiment l'effet rebond à l'échelle d'une économie entière, vingt et une fondées sur des modèles d'équilibre général et douze sur d'autres méthodes. Ils concluent que ces effets pourraient effacer plus de la moitié des économies d'énergie attendues de l'efficacité, et que des scénarios énergétiques mondiaux, qui en tiennent trop peu compte, pourraient sous-estimer la demande future.

Sur le constat, nos chiffres concordent avec le leur&nbsp;: de 1971 à 2018, écrivent-ils, le monde n'a connu aucun découplage absolu, seulement des cas nationaux&nbsp;; de {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, la série de l'EIA fait le même constat. Sur l'explication, cette page ne les teste pas. Les mêmes auteurs soulignent qu'une amélioration de l'efficacité mesurée à un niveau n'entraîne pas nécessairement une amélioration mesurée à un autre&nbsp;: une intensité énergétique agrégée ne mesure pas l'efficacité, et aucun taux de rebond ne se déduit d'une décomposition comme celle-ci.

## Ce que ces données ne disent pas {#limites}

- **Une décomposition, pas une cause.** Les trois effets s'additionnent exactement à la variation de la consommation&nbsp;; ils n'en attribuent aucune part à une cause.
- **L'intensité n'est pas l'efficacité.** L'énergie par unité de PIB baisse aussi quand la composition de l'économie change, ou quand la convention de mesure change.
- **Une convention de mesure.** L'EIA et l'Energy Institute comptent l'électricité hydraulique et éolienne à son contenu électrique. Comptée comme le combustible fossile qu'elle remplace (méthode dite de substitution), sa croissance pèserait davantage, et la baisse de l'intensité serait moindre&nbsp;; cette variante n'est pas calculée ici.
- **Le territoire, pas l'empreinte.** L'énergie contenue dans les importations n'est pas comptée&nbsp;: c'est la limite décisive de la comparaison avec l'Union européenne.
- **Un PIB en parité de pouvoir d'achat.** Il dépend d'une année de base et de révisions&nbsp;; les prix constants de l'EIA sont contrôlés contre la Banque mondiale à chaque mise à jour, et la variante aux taux de change de marché est donnée plus haut.
- **Une méthode de décomposition.** Les effets sont ceux de l'indice de Divisia logarithmique moyen&nbsp;; une autre méthode de décomposition n'a pas été essayée.
- **Un agrégat mondial.** Il additionne des trajectoires très différentes d'une région à l'autre, que cette page ne détaille pas.

<aside class="encadre">

**Une lecture de l'auteur, non testée ici.** La notion d'[effet rebond](/effet-rebond/) désigne la reprise de consommation qui rogne un gain d'efficacité. Dans le working paper [AWP-04](/awp/awp-04/), l'économiste Stéphane Lalut la range parmi les mécanismes de transfert de la transition énergétique. Les chiffres de cette page décrivent un découplage relatif&nbsp;; ils ne mesurent pas un rebond et ne démontrent pas cette lecture.

</aside>

{{< appel-livre slug="anthropie-ordre-ici-dette-ailleurs" sur="Pour prolonger la question" avis="non" >}}
*ANTHROPIE* suit, sur le temps long, ce que chaque ordre laisse derrière lui, et sur qui il en reporte la charge.
{{< /appel-livre >}}

## Sources {#sources}

- EIA (U.S. Energy Information Administration), [données internationales](https://www.eia.gov/international/data/world), fichier groupé `INTL.zip` lu par script&nbsp;: consommation totale d'énergie, PIB en parité de pouvoir d'achat, population. Convention de mesure relevée dans le même fichier (production et consommation d'électricité hydraulique, éolienne, solaire et nucléaire). Calculs de l'auteur&nbsp;: décomposition par l'indice de Divisia logarithmique moyen.
- Energy Institute, [*Statistical Review of World Energy*](https://www.energyinst.org/statistical-review), édition {{< dc-val "edition_ei" >}}, offre totale d'énergie (méthode du contenu physique), lue dans le jeu de données d'Our World in Data ([owid_energy](https://catalog.ourworldindata.org/energy/owid_energy/readme.md)), le site de l'Energy Institute refusant les lectures automatiques&nbsp;; le total mondial de {{< dc-val "an_ei_publie" >}} est contrôlé contre celui que publie l'édition 2025 ({{< dc-val "ei_publie" >}}&nbsp;exajoules), valeur transcrite du rapport.
- Banque mondiale, PIB à prix constants [en parité de pouvoir d'achat](https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.KD) et [aux taux de change de marché](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD), et population. Eurostat, [consommation d'énergie primaire](https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_eff/default/table) (indicateur de la directive sur l'efficacité énergétique), Union européenne à 27.
- Paul E. Brockway, Steve Sorrell, Gregor Semieniuk, Matthew Kuperus Heun et Victor Court, «&nbsp;Energy efficiency and economy-wide rebound effects&nbsp;: A review of the evidence and its implications&nbsp;», *Renewable and Sustainable Energy Reviews*, vol.&nbsp;141, 2021, [doi:10.1016/j.rser.2021.110781](https://doi.org/10.1016/j.rser.2021.110781), lu dans sa version en accès libre.

{{< reutiliser figures="figures_decouplage" jeu="decouplage" sources="EIA (données internationales)" donnees="Pour le monde et l'Union européenne à 27, chaque année depuis 1980 : consommation d'énergie primaire, PIB en parité de pouvoir d'achat à prix constants et population ; décomposition de la variation de la consommation et son recalcul sur d'autres sources, dans le JSON ; les séries annuelles existent aussi en CSV, une ligne par zone et par année." >}}
De {{< dc-val "an0" >}} à {{< dc-val "an1" >}}, la consommation mondiale d'énergie a augmenté de {{< dc-val "de_pct" >}}&nbsp;% pendant que l'énergie consommée par unité de PIB baissait de {{< dc-val "di_pct" >}}&nbsp;%&nbsp;: un découplage relatif, non absolu. Dans une décomposition comptable, l'effet du PIB par habitant pèse {{< dc-val "ratio_rp" >}}&nbsp;fois plus que celui de la population. Dans l'Union européenne, la consommation a baissé sur le territoire&nbsp;; ces données ne disent pas si c'est par efficacité ou par déplacement.
{{< /reutiliser >}}
