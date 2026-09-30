---
title: "Dette publique : pourquoi 100 % du PIB ne pèse pas partout de la même façon"
description: "Stock, taux d'intérêt, recettes, refinancement : quatre dimensions pour comparer ce que représente réellement une dette publique. Dans l'Union européenne, le prix payé ne suit pas le niveau de la dette ; la France, à {monde.fr_stock_fin} du PIB, consacre {monde.fr_charge} de ses recettes aux intérêts, moins que plusieurs pays moins endettés."
date: 2026-09-29
lastmod: 2026-09-29
# Brouillon : construite le 29/09/2026, publiée après le World Economic Outlook d'octobre 2026 du FMI
# (arbitrages du dossier 06_PROMOTION/DOSSIER_PAGE_DETTE_INTERNATIONALE.md, dépôt D:\PRO).
draft: true
donnees: [dette_monde]
faq:
  - question: "La France est-elle plus endettée que les autres pays ?"
    answer: "Plus que la plupart : fin {monde.annee}, sa dette publique atteint {monde.fr_stock_fin} du PIB, la troisième de l'Union européenne après la Grèce et l'Italie (Eurostat, dette de Maastricht). Mais le niveau de la dette ne dit pas ce qu'elle coûte : en {monde.annee}, la France a consacré {monde.fr_charge} de ses recettes publiques aux intérêts, moins que {monde.n_plus_charges_moins_endettes} pays pourtant moins endettés ({monde.plus_charges_moins_endettes})."
  - question: "La dette de la France lui coûte-t-elle plus cher qu'à ses voisins ?"
    answer: "Pas systématiquement. En {monde.annee}, son taux implicite — les intérêts de l'année rapportés à la dette de fin {monde.annee_1} — est de {monde.fr_prix}, proche de la moyenne de la zone euro ({monde.prix_moyen_euro}) : certains pays paient moins, notamment l'Allemagne ({monde.de_prix}), d'autres davantage. Le rendement à 10 ans dépasse ce taux implicite de {monde.fr_ecart_taux}, et {monde.fr_part_1an} de la dette arrive à échéance dans l'année : si les conditions de financement restaient supérieures au coût de la dette remplacée, les refinancements pousseraient ce coût moyen à la hausse."
  - question: "Pourquoi deux pays aussi endettés ne paient-ils pas les mêmes intérêts ?"
    answer: "Parce que la charge dépend de trois termes : le stock de dette, le prix auquel il a été financé et les recettes disponibles pour le servir. En {monde.annee}, la {monde.j_bas} ({monde.j_bas_stock} du PIB) et la {monde.j_haut} ({monde.j_haut_stock}) ont des dettes voisines ; la seconde consacre pourtant {monde.j_rapport} fois plus de ses recettes aux intérêts, parce qu'elle paie {monde.j_haut_prix} sur son stock contre {monde.j_bas_prix}."
  - question: "L'euro fait-il baisser le coût de la dette ?"
    answer: "Les données ne permettent pas de l'affirmer. Dans l'Union européenne en {monde.annee}, les pays hors zone euro paient en moyenne davantage ({monde.prix_moyen_hors} contre {monde.prix_moyen_euro}), mais l'écart est très hétérogène : la Suède, hors euro, paie {monde.se_prix}, comme l'Allemagne. Hors de la zone euro, le taux implicite est étroitement associé à l'inflation récente ; dans la zone euro, beaucoup moins. C'est une association observée sur une année, non une causalité."
  - question: "Une dette élevée provoque-t-elle forcément une crise ?"
    answer: "Ces données ne permettent pas d'estimer le risque de crise. Elles montrent seulement qu'un même niveau de dette peut correspondre à des charges courantes très différentes. Le risque de crise dépend aussi de la croissance, du solde primaire, de la structure des créanciers, de la monnaie, des maturités, des actifs publics et des conditions financières."
---

**Deux pays peuvent afficher le même niveau de dette et supporter des charges très différentes.** En {{< monde-val "annee" >}}, la {{< monde-val "j_bas" >}} et la {{< monde-val "j_haut" >}} avaient des dettes voisines — {{< monde-val "j_bas_stock" >}} et {{< monde-val "j_haut_stock" >}} du PIB. La {{< monde-val "j_haut" >}} a pourtant consacré **{{< monde-val "j_haut_charge" >}} de ses recettes publiques aux intérêts, la {{< monde-val "j_bas" >}} {{< monde-val "j_bas_charge" >}}**&nbsp;: {{< monde-val "j_rapport" >}} fois moins. Le ratio dette/PIB, souvent mis en avant dans le débat public, n'est qu'un terme de l'équation.

Cette page compare ce que représente réellement une dette publique, d'abord dans les {{< monde-val "n_pays" >}} pays de l'Union européenne, où les données sont strictement comparables, puis pour quelques grandes économies hors d'Europe, avec leur niveau de comparabilité affiché. <span class="badge-donnees">Données&nbsp;: {{< monde-val "date_donnees" >}}</span>

## Quatre mots, quatre mesures {#quatre-mesures}

- **Le stock**&nbsp;: la dette publique rapportée au PIB. C'est le chiffre le plus cité. Il se lit à deux dates&nbsp;: le **stock de clôture** (dette de fin d'année) sert au classement&nbsp;; le **stock de départ** (dette de fin d'année précédente, rapportée au PIB de l'année) sert à expliquer les intérêts de l'année.
- **Le prix**&nbsp;: le taux implicite, c'est-à-dire les intérêts versés une année rapportés à la dette de la fin de l'année précédente. Il mesure le coût moyen du stock, non le taux auquel l'État emprunte aujourd'hui. Eurostat publie aussi un «&nbsp;coût apparent&nbsp;», fondé sur la dette moyenne de l'année&nbsp;: les deux conventions sont proches mais non identiques.
- **La charge**&nbsp;: les intérêts rapportés aux recettes publiques. C'est ce que la dette prend, chaque année, sur les moyens de l'État.
- **La transmission**&nbsp;: la vitesse à laquelle les nouveaux taux gagnent le prix du stock, selon la part de la dette qui arrive à échéance et l'écart entre le taux de marché et le prix moyen.

Les trois premiers sont liés par une identité exacte, vérifiée pour chaque pays&nbsp;:

<p class="formule">charge = stock de départ × prix ÷ recettes<br><small>intérêts / recettes = (dette de fin d'année précédente / PIB) × (intérêts / dette de fin d'année précédente) ÷ (recettes / PIB)</small></p>

Deux pays au même stock peuvent donc supporter des charges différentes pour deux raisons, et deux seulement&nbsp;: ils ne paient pas le même prix, ou ils ne disposent pas des mêmes recettes.

## Le stock&nbsp;: un classement qui ne dit pas tout {#stock}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-stock.svg" alt="Barres horizontales de la dette publique en pourcentage du PIB, fin {{< monde-val "annee" >}}, pour les 27 pays de l'Union européenne, de la Grèce, la plus endettée, à l'Estonie ; la France est troisième, à {{< monde-val "fr_stock_fin" >}}." width="720" height="543" loading="lazy">
  <figcaption>Eurostat, dette brute de Maastricht des administrations publiques, fin {{< monde-val "annee" >}}. En bleu, la zone euro&nbsp;; en orange, les pays hors zone euro.</figcaption>
</figure>

Fin {{< monde-val "annee" >}}, la France est le {{< monde-val "fr_rang_stock" >}} pays le plus endetté de l'Union européenne, à **{{< monde-val "fr_stock_fin" >}} du PIB**. Ce classement est celui que retiennent la plupart des comparaisons. Il mesure un stock brut&nbsp;: il ne compte ni les actifs publics, ni les engagements qui ne sont pas de la dette, comme les retraites futures.

Pour expliquer les intérêts payés en {{< monde-val "annee" >}}, il faut repartir de la dette déjà en place au début de l'année. Les figures suivantes utilisent donc le **stock de départ**, la dette de fin {{< monde-val "annee_1" >}} rapportée au PIB de {{< monde-val "annee" >}}, comme les chiffres de l'ouverture&nbsp;; le graphique précédent décrivait, lui, la situation à la fin de {{< monde-val "annee" >}}.

## Même dette, charge différente {#meme-dette}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-charge.svg" alt="Nuage de points : en abscisse la dette rapportée au PIB, en ordonnée les intérêts en pourcentage des recettes publiques, pour les 27 pays de l'Union européenne. Les pays de la zone euro s'alignent le long d'une droite peu pentue ; les pays hors zone euro, Hongrie, Roumanie et Pologne en tête, se situent bien au-dessus pour une dette comparable." width="720" height="488" loading="lazy">
  <figcaption>Stock (dette de fin {{< monde-val "annee_1" >}} / PIB {{< monde-val "annee" >}}) et charge (intérêts / recettes), {{< monde-val "annee" >}}. Les pointillés relient les faux jumeaux désignés par une règle fixée avant le calcul&nbsp;: pour chaque pays, son plus proche voisin en stock&nbsp;; couples dont l'écart est inférieur à 10 points&nbsp;; les trois plus grands écarts de charge.</figcaption>
</figure>

Sur l'ensemble des {{< monde-val "n_pays" >}} pays, le stock ne rend compte que d'une partie de la dispersion des charges (régression linéaire simple, R² = {{< monde-val "r2_charge_stock" >}}). L'association de rang est pourtant forte&nbsp;: classés par dette et par charge, les pays s'ordonnent de façon voisine (corrélation de rang de {{< monde-val "spearman" >}}).

La figure précise ce contraste. **À l'intérieur de la zone euro, le stock rend compte de l'essentiel de la charge** (R² = {{< monde-val "r2_euro" >}} sur {{< monde-val "n_euro" >}} pays)&nbsp;; il en va de même parmi les {{< monde-val "n_hors" >}} pays hors zone euro (R² = {{< monde-val "r2_hors" >}}). Mais les deux groupes ne suivent pas la même droite&nbsp;: hors de l'euro, la charge croît beaucoup plus vite avec la dette, notamment parce que les pays les plus endettés y paient aussi plus cher. La pente ne dépend d'aucun pays en particulier&nbsp;: en retirant tour à tour chacun des sept, elle reste comprise entre {{< monde-val "pente_hors_loo_min" >}} et {{< monde-val "pente_hors_loo_max" >}}.

La France illustre l'autre versant&nbsp;: avec {{< monde-val "fr_stock" >}} du PIB de dette en début d'année, elle a consacré **{{< monde-val "fr_charge" >}} de ses recettes** aux intérêts en {{< monde-val "annee" >}}, moins que {{< monde-val "n_plus_charges_moins_endettes" >}} pays moins endettés&nbsp;: {{< monde-val "plus_charges_moins_endettes" >}}.

## Pourquoi&nbsp;? Le prix et les recettes {#prix-et-recettes}

{{< dette-monde-tableau niveau="europe" >}}

Le tableau décompose la charge de chaque pays en ses trois termes. Deux constats en ressortent.

**Le prix ne suit pas le niveau de la dette.** Dans l'Union européenne en {{< monde-val "annee" >}}, le taux implicite n'a aucun lien linéaire avec le stock (R² = {{< monde-val "r2_prix_stock" >}})&nbsp;: l'Italie, très endettée, paie un prix voisin de pays qui le sont beaucoup moins, et la France paie **{{< monde-val "fr_prix" >}}**, dans la moyenne de la zone euro ({{< monde-val "prix_moyen_euro" >}}).

**Les recettes comptent aussi.** À prix égal, un État qui prélève une plus faible part de sa richesse consacre une plus grande part de ses recettes aux intérêts. C'est l'un des deux termes qui séparent les faux jumeaux&nbsp;: la {{< monde-val "j_haut" >}} paie {{< monde-val "j_haut_prix" >}} sur son stock contre {{< monde-val "j_bas_prix" >}} pour la {{< monde-val "j_bas" >}}, et ses recettes représentent {{< monde-val "j_haut_rec" >}} du PIB contre {{< monde-val "j_bas_rec" >}}.

### Prix de la dette et inflation récente&nbsp;: ce que montre l'Europe {#prix-et-inflation}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-prix.svg" alt="Nuage de points : en abscisse l'inflation moyenne des trois années précédentes, en ordonnée le taux implicite de la dette. Les pays hors zone euro à forte inflation, Roumanie, Hongrie, Pologne, paient le plus cher ; les pays baltes, en zone euro, ont connu une forte inflation sans payer cher ; la Suède paie comme l'Allemagne." width="720" height="488" loading="lazy">
  <figcaption>Taux implicite de la dette ({{< monde-val "annee" >}}) et inflation moyenne des trois années précédentes (indice des prix harmonisé, Eurostat). Relation descriptive sur une année.</figcaption>
</figure>

Dans une régression descriptive, l'inflation moyenne des trois années précédentes et l'appartenance à la zone euro rendent compte ensemble d'une large part de la dispersion observée (R² = {{< monde-val "r2_prix_euro_inflation" >}}). Le coefficient associé à la zone euro est de −{{< monde-val "effet_euro" >}} point, celui associé à un point d'inflation moyenne supplémentaire de +{{< monde-val "effet_inflation" >}} point. Ces coefficients ne mesurent pas des effets causaux, et la fenêtre de trois ans est un choix&nbsp;: avec une inflation moyenne sur deux, quatre ou cinq ans, leur signe ne change pas et leur ordre de grandeur tient (de −{{< monde-val "rob_euro_min" >}} à −{{< monde-val "rob_euro_max" >}} point pour la zone euro, de +{{< monde-val "rob_infl_min" >}} à +{{< monde-val "rob_infl_max" >}} point par point d'inflation, R² de {{< monde-val "rob_r2_min" >}} à {{< monde-val "rob_r2_max" >}}). Surtout, l'association n'a pas la même force selon la monnaie&nbsp;: **hors de la zone euro, le taux implicite est étroitement associé à l'inflation récente** (R² = {{< monde-val "r2_prix_inflation_hors" >}})&nbsp;; **dans la zone euro, beaucoup moins** (R² = {{< monde-val "r2_prix_inflation_euro" >}}), comme le montrent les pays baltes, qui ont connu une forte inflation sans payer cher.

L'appartenance monétaire ne suffit pas pour autant&nbsp;: **la Suède, hors de l'euro, paie {{< monde-val "se_prix" >}}**, exactement comme l'Allemagne. Les données ne disent donc ni que l'euro rend la dette moins chère, ni l'inverse&nbsp;; elles montrent que le prix d'une dette publique ne découle pas de son niveau.

## La transmission&nbsp;: un repère de pression, non une prévision {#transmission}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-transmission.svg" alt="Nuage de points : en abscisse la part de la dette qui arrive à échéance dans l'année, en ordonnée l'écart entre le rendement à 10 ans et le taux implicite du stock. La France se situe parmi les pays où le rendement de marché dépasse le plus le taux implicite ; la Suède et le Portugal ont une part bien plus grande de leur dette à moins d'un an ; au Danemark, le rendement à 10 ans est inférieur au taux implicite." width="720" height="488" loading="lazy">
  <figcaption>Part de la dette arrivant à échéance dans l'année (Eurostat, dette par échéance résiduelle) et écart entre le rendement harmonisé à 10 ans et le taux implicite du stock, {{< monde-val "annee" >}}. Repère de transmission, non prévision.</figcaption>
</figure>

Le taux implicite d'une année rémunère une dette émise à des dates différentes&nbsp;: il ne rejoint les conditions de marché qu'au fil des refinancements. Deux mesures situent cette inertie&nbsp;: la part de la dette qui arrive à échéance dans l'année, et l'écart entre le rendement harmonisé à 10 ans et le taux implicite. Ni l'une ni l'autre n'est une prévision&nbsp;: l'État n'emprunte pas qu'à 10 ans, et le rendement d'aujourd'hui n'est pas celui de demain.

**En France, {{< monde-val "fr_part_1an" >}} de la dette présente à fin {{< monde-val "annee" >}} a une échéance résiduelle inférieure à un an. En {{< monde-val "annee" >}}, le rendement harmonisé à 10 ans ({{< monde-val "fr_taux10" >}}) était supérieur de {{< monde-val "fr_ecart_taux" >}} au taux implicite du stock.** Si les conditions de financement demeuraient supérieures au coût de la dette remplacée, les refinancements exerceraient une pression haussière sur le coût moyen — le mécanisme que détaille la page [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/). Au Danemark, l'indicateur est orienté dans l'autre sens&nbsp;: le rendement à 10 ans se situe sous le taux implicite du stock ({{< monde-val "dk_ecart_taux" >}}).

## Et hors d'Europe&nbsp;? {#hors-europe}

Hors de l'Union européenne, les données ne sont plus harmonisées&nbsp;: deux tableaux, deux niveaux de comparabilité. Pour les économies avancées, les séries de l'OCDE (*Economic Outlook*) permettent un calcul voisin, sur une base plus large&nbsp;: des passifs financiers bruts, et non la dette de Maastricht — la France y figure pour mesurer l'écart entre les deux sources. Le rapport des intérêts à ces passifs n'est donc pas exactement le taux implicite européen.

{{< dette-monde-tableau niveau="avances" >}}

Pour les grands émergents, seules des mesures indicatives existent&nbsp;: la dette selon le FMI, et les intérêts de la seule administration centrale selon la Banque mondiale, toujours pris la même année.

{{< dette-monde-tableau niveau="emergents" >}}

Trois cas éclairent la page. **Le Japon**, dont les passifs financiers bruts atteignent {{< monde-val "jpn_stock" >}} du PIB, présente sur cette base un rapport intérêts/passifs de {{< monde-val "jpn_prix" >}}, contre {{< monde-val "fra_prix" >}} pour la France, et consacre {{< monde-val "jpn_charge" >}} de ses recettes aux intérêts — moins que la France sur la même base ({{< monde-val "fra_charge" >}}). **La Suisse**, avec sa propre monnaie et des passifs bruts de {{< monde-val "che_stock" >}} du PIB, présente un rapport de {{< monde-val "che_prix" >}} et n'y consacre que {{< monde-val "che_charge" >}} de ses recettes&nbsp;; ses passifs financiers nets sont négatifs ({{< monde-val "che_dette_nette" >}} du PIB)&nbsp;: ses actifs financiers dépassent ses passifs. **Les États-Unis**, à {{< monde-val "usa_stock" >}}, présentent un rapport de {{< monde-val "usa_prix" >}} et y consacrent {{< monde-val "usa_charge" >}} de leurs recettes — {{< monde-val "usa_fra_rapport" >}} fois la part française, pour une dette comparable.

Pour les grands émergents, les chiffres sont indicatifs et ne se comparent pas directement aux autres&nbsp;: l'Inde consacre {{< monde-val "ind_charge" >}} des recettes de son administration centrale aux intérêts, le Brésil {{< monde-val "bra_charge" >}}, l'Afrique du Sud {{< monde-val "zaf_charge" >}}, pour des dettes de {{< monde-val "ind_stock" >}}, {{< monde-val "bra_stock" >}} et {{< monde-val "zaf_stock" >}} du PIB selon le FMI, en {{< monde-val "ind_charge_annee" >}}, {{< monde-val "bra_charge_annee" >}} et {{< monde-val "zaf_charge_annee" >}}, dernières années publiées par la Banque mondiale. Une part de l'écart tient au prix payé, une autre à la faiblesse relative des recettes&nbsp;: sans données harmonisées, on ne peut pas les séparer.

<aside class="encadre">

**Et pour savoir si la dette va augmenter&nbsp;?** Cette page compare ce que la dette coûte aujourd'hui. La question de sa trajectoire est différente&nbsp;: un ratio de dette tend à croître quand le taux d'intérêt payé dépasse la croissance nominale de l'économie et que le budget, hors intérêts, reste en déficit. Cet écart entre taux et croissance est l'objet d'une autre analyse.

</aside>

## Ce que ces données ne disent pas {#limites}

- **Une seule année.** Les relations décrites portent sur {{< monde-val "annee" >}}&nbsp;; elles ne disent rien de leur stabilité dans le temps.
- **Des corrélations, non des causes.** Une régression sur {{< monde-val "n_pays" >}} pays décrit une association. L'appartenance à l'euro et l'inflation passée sont d'ailleurs liées entre elles.
- **Un stock brut.** La dette de Maastricht ne déduit pas les actifs publics&nbsp;; la Suisse, dont les passifs financiers nets sont négatifs, montre l'importance de cet écart.
- **Des définitions voisines, non identiques.** Hors d'Europe, l'OCDE mesure des passifs financiers bruts, le FMI une dette brute, la Banque mondiale les seuls intérêts de l'administration centrale.
- **Le risque de crise.** Il dépend aussi de la croissance, du solde primaire, de la monnaie, des maturités et des créanciers&nbsp;: cette page ne le mesure pas.
- **Les détenteurs de la dette.** Banque centrale, non-résidents, épargnants nationaux&nbsp;: leur part change le risque et le coût d'une dette, et fera l'objet d'une analyse distincte.
- **Les engagements hors dette**, comme les retraites futures, n'entrent dans aucun de ces chiffres.

## Questions fréquentes {#questions}

{{< faq-visible >}}

## D'où viennent ces chiffres {#sources}

**Europe (strictement comparable)** — Eurostat, administrations publiques (S.13), comptes nationaux SEC 2010, montants en monnaie nationale&nbsp;: intérêts versés et recettes (`gov_10a_main`, D41PAY et TR), dette de Maastricht (`gov_10dd_edpt1`), PIB (`nama_10_gdp`), dette par échéance résiduelle (`gov_10dd_ggd`), taux à 10 ans (`irt_lt_mcby_a`), indice des prix harmonisé (`prc_hicp_aind`).

**Économies avancées hors UE (avec réserve)** — OCDE, *Economic Outlook*&nbsp;: intérêts bruts, recettes, PIB et passifs financiers bruts des administrations publiques.

**Grands émergents (indicatif)** — FMI, *World Economic Outlook* (dette brute des administrations publiques)&nbsp;; Banque mondiale, *World Development Indicators* (intérêts en % des recettes de l'administration centrale).

Les calculs, les statistiques et les figures sont produits par un script unique, relancé à chaque publication des sources&nbsp;; aucun chiffre de cette page n'est saisi à la main. Les données sont téléchargeables en [JSON](/dette_monde.json) sous licence CC BY 4.0. Méthode&nbsp;: la charge, le stock et le prix vérifient l'identité exacte donnée plus haut, avec la dette de fin d'année précédente (convention du taux implicite de la BCE, distincte du «&nbsp;coût apparent&nbsp;» d'Eurostat, fondé sur la dette moyenne)&nbsp;; la robustesse des coefficients est recalculée à chaque mise à jour sur des fenêtres d'inflation de deux à cinq ans&nbsp;; les statistiques sont des moindres carrés simples, descriptifs.

**Pour aller plus loin** — le dossier sur la dette française&nbsp;: [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/) et [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/). Les précédents historiques — Italie 2011, Grèce 2015, Allemagne 1953 — sont analysés dans le livre [*Dette publique&nbsp;: qui paie vraiment&nbsp;?*](/livres/dette-publique-qui-paie-vraiment/).
