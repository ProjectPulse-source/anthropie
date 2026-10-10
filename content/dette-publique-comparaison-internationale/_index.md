---
title: "Dette publique : pourquoi 100 % du PIB ne pèse pas partout de la même façon"
description: "Même dette, charge différente : dans l'Union européenne, le prix de la dette publique ne suit pas son niveau. Stock, taux, recettes comparés en 27 pays et hors d'Europe."
chapo: "À dette presque égale, {monde.j_haut_le} consacre {monde.j_haut_charge} de ses recettes publiques aux intérêts, {monde.j_bas_le} {monde.j_bas_charge}. Le stock ne suffit donc pas à mesurer ce que pèse une dette publique : il faut regarder aussi son prix, les recettes disponibles pour la servir et la vitesse à laquelle les nouvelles conditions de financement se transmettent."
og_title: "Dette publique : ce que 100 % du PIB ne dit pas"
og_image: "images/og-dette-monde.jpg"
og_image_alt: "Carte de partage : « Même dette, charge différente » — les 27 pays de l'Union européenne, dette en % du PIB et intérêts en % des recettes ; deux pays à dette voisine reliés, l'un paie plus de trois fois plus que l'autre."
date: 2026-09-29
lastmod: 2026-10-03
# Construite le 29/09/2026, publiée le 30/09/2026 sans attendre le WEO (contre-expertise PRO-20260930-061613) ;
# hiérarchie refaite le 30/09 sur l'avis « forme et fond » (arbitrage ENTRANTE_2026-09-30_Dette_Internationale_forme) :
# surprendre, montrer, expliquer, documenter — rien de supprimé, la preuve repliée sur la même URL ; arbitrage final
# du même jour (Derre_Internationale-01) : ouverture sans redite, dates distinguées, encart livre, figures réutilisables.
# Arbitrages : 06_PROMOTION/DOSSIER_PAGE_DETTE_INTERNATIONALE.md, dépôt D:\PRO.
donnees: [dette_monde]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_monde"
  nom: "Dette publique comparée : stock, prix, recettes et charge d'intérêts dans l'Union européenne et hors d'Europe"
  description: "Compilation dérivée automatiquement des séries officielles, sans aucune valeur recopiée à la main : 27 pays de l'Union européenne en {monde.annee} (Eurostat, strictement comparable) ; économies avancées hors UE (OCDE, avec réserve) ; grands émergents (FMI et Banque mondiale, indicatif). Identité exacte vérifiée pour chaque pays européen : intérêts / recettes = stock de départ × taux implicite ÷ recettes. Écarts de taux à 10 ans avec l'Allemagne depuis 1995."
  couverture_temporelle: "1995/{monde.annee}"
  couverture_spatiale: "Union européenne, économies avancées de l'OCDE et grands émergents"
  variables:
    - {nom: "Stock de dette publique", unite: "% du PIB", description: "dette brute / PIB ; stock de départ (fin d'année précédente) pour la décomposition"}
    - {nom: "Prix de la dette (taux implicite)", unite: "% par an", description: "intérêts de l'année / dette de fin d'année précédente"}
    - {nom: "Charge d'intérêts", unite: "% des recettes publiques"}
    - {nom: "Écart de taux à 10 ans avec l'Allemagne", unite: "points de pourcentage"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/irt_lt_mcby_a/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_aind/default/table?lang=fr"
    - "https://data-explorer.oecd.org/"
    - "https://www.imf.org/external/datamapper/GGXWDG_NGDP@WEO"
    - "https://data.worldbank.org/indicator/GC.XPN.INTP.RV.ZS"
  mots: ["dette publique", "comparaison internationale", "Union européenne", "taux implicite", "charge d'intérêts", "Eurostat", "OCDE", "FMI"]
  fichiers: ["dette_monde.csv", "dette_monde.json"]
faq:
  - question: "La France est-elle plus endettée que les autres pays ?"
    answer: "Plus que la plupart : fin {monde.annee}, sa dette publique atteint {monde.fr_stock_fin} du PIB, la troisième de l'Union européenne après la Grèce et l'Italie (Eurostat, dette de Maastricht). Mais le niveau de la dette ne dit pas ce qu'elle coûte : en {monde.annee}, la France a consacré {monde.fr_charge} de ses recettes publiques aux intérêts, moins que {monde.n_plus_charges_moins_endettes} pays pourtant moins endettés ({monde.plus_charges_moins_endettes})."
  - question: "La dette de la France lui coûte-t-elle plus cher qu'à ses voisins ?"
    answer: "Pas systématiquement. En {monde.annee}, son taux implicite — les intérêts de l'année rapportés à la dette de fin {monde.annee_1} — est de {monde.fr_prix}, proche de la moyenne de la zone euro ({monde.prix_moyen_euro}) : certains pays paient moins, notamment l'Allemagne ({monde.de_prix}), d'autres davantage. Le rendement à 10 ans dépasse ce taux implicite de {monde.fr_ecart_taux}, et {monde.fr_part_1an} de la dette arrive à échéance dans l'année : si les conditions de financement restaient supérieures au coût de la dette remplacée, les refinancements pousseraient ce coût moyen à la hausse."
  - question: "Pourquoi deux pays aussi endettés ne paient-ils pas les mêmes intérêts ?"
    answer: "Parce que la charge dépend de trois termes : le stock de dette, le prix auquel il a été financé et les recettes disponibles pour le servir. En {monde.annee}, {monde.j_bas_le} ({monde.j_bas_stock} du PIB) et {monde.j_haut_le} ({monde.j_haut_stock}) ont des dettes voisines ; la seconde consacre pourtant {monde.j_rapport} fois plus de ses recettes aux intérêts : elle paie {monde.j_haut_prix} sur son stock contre {monde.j_bas_prix}, et ses recettes pèsent {monde.j_haut_rec} du PIB contre {monde.j_bas_rec}."
  - question: "L'euro fait-il baisser le coût de la dette ?"
    answer: "Pas automatiquement. Avant 1999, les écarts de taux avec l'Allemagne ont fondu dans les futurs pays de l'euro, mais aussi en Suède, qui n'y est jamais entrée. En 2012, les membres les plus fragiles ont décroché (la Grèce empruntait {monde.ec_el_2012} points au-dessus de l'Allemagne), plus qu'aucun pays resté en dehors ; la détente a suivi les interventions de la BCE. En {monde.annee}, la Suède et le Danemark empruntent à 10 ans moins cher que l'Allemagne, la France plus cher. Sur le stock de dette, la Suède paie {monde.se_prix}, comme l'Allemagne ({monde.de_prix}). L'euro supprime le risque de change entre ses membres ; il ne leur garantit pas le taux allemand."
  - question: "Une dette élevée provoque-t-elle forcément une crise ?"
    answer: "Ces données ne permettent pas d'estimer le risque de crise. Elles montrent seulement qu'un même niveau de dette peut correspondre à des charges courantes très différentes. Le risque de crise dépend aussi de la croissance, du solde primaire, de la structure des créanciers, de la monnaie, des maturités, des actifs publics et des conditions financières."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 30
  nature: "Séries officielles comparées (Eurostat, OCDE, FMI, Banque mondiale) et calculs de l'auteur"
---

{{< dossier-dette volet="3" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Mise à jour&nbsp;: {{< monde-val "date_donnees" >}}</span> Les {{< monde-val "n_pays" >}} pays de l'Union européenne, données principales {{< monde-val "annee" >}}&nbsp;; hors d'Europe, le millésime est indiqué pays par pays. Télécharger&nbsp;: <a href="/dette_monde.csv">CSV</a> · <a href="/dette_monde.json">JSON</a> · <a href="#sources">méthode</a></p>

## Même dette, charge différente {#meme-dette}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-charge.svg" alt="Nuage de points : en abscisse la dette rapportée au PIB, en ordonnée les intérêts en pourcentage des recettes publiques, pour les 27 pays de l'Union européenne. Les pays de la zone euro s'alignent le long d'une droite peu pentue ; les pays hors zone euro, Hongrie, Roumanie et Pologne en tête, se situent bien au-dessus pour une dette comparable." width="720" height="488" loading="lazy">
  <figcaption>Stock de départ (dette de fin {{< monde-val "annee_1" >}} / PIB {{< monde-val "annee" >}}) et charge (intérêts / recettes), {{< monde-val "annee" >}}. Les pointillés relient les faux jumeaux désignés par une règle fixée avant le calcul&nbsp;: pour chaque pays, son plus proche voisin en stock&nbsp;; couples dont l'écart est inférieur à 10 points&nbsp;; les trois plus grands écarts de charge.</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** À niveau de dette voisin, la part des recettes absorbée par les intérêts peut varier de 1 à {{< monde-val "j_rapport" >}}&nbsp;: le stock ne suffit pas à déterminer la charge, parce qu'il ne fixe ni le prix de la dette ni le niveau des recettes publiques.

</div>

Le stock n'est pas sans rapport avec la charge&nbsp;: classés par dette et par charge, les pays s'ordonnent de façon voisine (corrélation de rang de {{< monde-val "spearman" >}}). Mais il ne rend compte que d'une partie de sa dispersion (R² = {{< monde-val "r2_charge_stock" >}}), et la figure précise pourquoi. **À l'intérieur de la zone euro, le stock rend compte de l'essentiel de la charge** (R² = {{< monde-val "r2_euro" >}} sur {{< monde-val "n_euro" >}} pays)&nbsp;; il en va de même parmi les {{< monde-val "n_hors" >}} pays hors zone euro (R² = {{< monde-val "r2_hors" >}}). Mais les deux groupes ne suivent pas la même droite&nbsp;: hors de l'euro, la charge croît beaucoup plus vite avec la dette, notamment parce que les pays les plus endettés y paient aussi plus cher. La pente ne dépend d'aucun pays en particulier&nbsp;: en retirant tour à tour chacun des sept, elle reste comprise entre {{< monde-val "pente_hors_loo_min" >}} et {{< monde-val "pente_hors_loo_max" >}}.

La France illustre l'autre versant&nbsp;: avec {{< monde-val "fr_stock" >}} du PIB de dette en début d'année, elle a consacré **{{< monde-val "fr_charge" >}} de ses recettes** aux intérêts en {{< monde-val "annee" >}}, moins que {{< monde-val "n_plus_charges_moins_endettes" >}} pays moins endettés&nbsp;: {{< monde-val "plus_charges_moins_endettes" >}}.

## Pourquoi&nbsp;? Une équation, quatre mesures {#quatre-mesures}

<div class="equation" role="group" aria-label="La charge de la dette décomposée en trois termes">
  <p class="equation__titre">Ce que la dette pèse sur les recettes publiques dépend de trois choses</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>la dette</b><small>stock de départ, en % du PIB</small></span>
    <span class="equation__op" aria-label="multipliée par">×</span>
    <span class="equation__terme"><b>son coût moyen</b><small>prix&nbsp;: taux implicite</small></span>
    <span class="equation__op" aria-label="divisée par">÷</span>
    <span class="equation__terme"><b>les recettes publiques</b><small>en % du PIB</small></span>
    <span class="equation__op" aria-label="égale">=</span>
    <span class="equation__terme equation__terme--resultat"><b>la charge</b><small>intérêts en % des recettes</small></span>
  </div>
  <p class="equation__exacte">Identité exacte, vérifiée pour chaque pays&nbsp;: intérêts / recettes = (dette de fin d'année précédente / PIB) × (intérêts / dette de fin d'année précédente) ÷ (recettes / PIB)</p>
</div>

- **Le stock**&nbsp;: la dette publique rapportée au PIB, le chiffre le plus cité. Il se lit à deux dates&nbsp;: le **stock de départ** (dette de fin d'année précédente, rapportée au PIB de l'année) explique les intérêts de l'année — c'est celui de la figure et de l'ouverture&nbsp;; le **stock de clôture** (dette de fin d'année) sert au classement plus bas.
- **Le prix**&nbsp;: le taux implicite, c'est-à-dire les intérêts versés une année rapportés à la dette de la fin de l'année précédente. Il mesure le coût moyen du stock, non le taux auquel un État emprunte aujourd'hui. Eurostat publie aussi un «&nbsp;coût apparent&nbsp;», fondé sur la dette moyenne de l'année&nbsp;: les deux conventions sont proches mais non identiques.
- **La charge**&nbsp;: la part des recettes des administrations publiques consacrée au paiement des intérêts.
- **La transmission**&nbsp;: la vitesse à laquelle les nouvelles conditions de financement se répercutent sur le coût moyen du stock, selon la part de la dette qui arrive à échéance et l'écart entre le taux de marché et le taux implicite.

À stock de départ égal, dans cette identité comptable, deux pays ne peuvent différer en charge que par deux termes&nbsp;: le prix de leur stock ou le niveau de leurs recettes.

## Le prix et les recettes {#prix-et-recettes}

**Le prix ne suit pas le stock.** Dans l'Union européenne en {{< monde-val "annee" >}}, la relation linéaire entre le stock de départ et le taux implicite est pratiquement nulle (R² = {{< monde-val "r2_prix_stock" >}})&nbsp;: sur une année et entre pays, le niveau de la dette ne permet pas de prédire son prix, ce qui ne veut pas dire qu'il n'a jamais d'effet sur lui. L'Italie, très endettée, paie un taux implicite voisin de pays qui le sont beaucoup moins, et la France paie **{{< monde-val "fr_prix" >}}**, dans la moyenne de la zone euro ({{< monde-val "prix_moyen_euro" >}}).

**Les recettes comptent aussi.** À prix égal, un État qui prélève une plus faible part de sa richesse consacre une plus grande part de ses recettes aux intérêts. Ce sont les deux termes qui séparent les faux jumeaux&nbsp;: {{< monde-val "j_haut_le" >}} paie {{< monde-val "j_haut_prix" >}} sur son stock contre {{< monde-val "j_bas_prix" >}} pour {{< monde-val "j_bas_le" >}}, et ses recettes représentent {{< monde-val "j_haut_rec" >}} du PIB contre {{< monde-val "j_bas_rec" >}}.

{{< dette-monde-tableau niveau="europe" repli="Voir les 27 pays : stock, prix, recettes et charge" >}}

### Prix de la dette et inflation récente {#prix-et-inflation}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-prix.svg" alt="Nuage de points : en abscisse l'inflation moyenne des trois années précédentes, en ordonnée le taux implicite de la dette. Les pays hors zone euro à forte inflation, Roumanie, Hongrie, Pologne, paient le plus cher ; les pays baltes, en zone euro, ont connu une forte inflation sans payer cher ; la Suède paie comme l'Allemagne." width="720" height="488" loading="lazy">
  <figcaption>Taux implicite de la dette ({{< monde-val "annee" >}}) et inflation moyenne des trois années précédentes (indice des prix harmonisé, Eurostat). Relation descriptive sur une année.</figcaption>
</figure>

**Hors de la zone euro, le taux implicite est étroitement associé à l'inflation récente** (R² = {{< monde-val "r2_prix_inflation_hors" >}})&nbsp;; **dans la zone euro, beaucoup moins** (R² = {{< monde-val "r2_prix_inflation_euro" >}})&nbsp;: les pays baltes ont connu une forte inflation sans payer cher. L'appartenance monétaire ne suffit pas pour autant&nbsp;: **la Suède, hors de l'euro, paie {{< monde-val "se_prix" >}}**, comme l'Allemagne. Sur une seule année et d'un pays à l'autre, ces données montrent que le niveau d'une dette publique ne suffit pas à prédire son prix&nbsp;; elles ne disent ni que l'euro le rend moins cher, ni l'inverse.

<details class="repli"><summary>Régression descriptive&nbsp;: −{{< monde-val "effet_euro" >}} point pour la zone euro, +{{< monde-val "effet_inflation" >}} point par point d'inflation, stables d'une fenêtre à l'autre — des associations, non des effets causaux</summary>

Dans une régression descriptive, l'inflation moyenne des trois années précédentes et l'appartenance à la zone euro rendent compte ensemble d'une large part de la dispersion observée (R² = {{< monde-val "r2_prix_euro_inflation" >}}). Le coefficient associé à la zone euro est de −{{< monde-val "effet_euro" >}} point, celui associé à un point d'inflation moyenne supplémentaire de +{{< monde-val "effet_inflation" >}} point. Ces coefficients ne mesurent pas des effets causaux, et la fenêtre de trois ans est un choix&nbsp;: avec une inflation moyenne sur deux, quatre ou cinq ans, leur signe ne change pas et leur ordre de grandeur tient (de −{{< monde-val "rob_euro_min" >}} à −{{< monde-val "rob_euro_max" >}} point pour la zone euro, de +{{< monde-val "rob_infl_min" >}} à +{{< monde-val "rob_infl_max" >}} point par point d'inflation, R² de {{< monde-val "rob_r2_min" >}} à {{< monde-val "rob_r2_max" >}}).

</details>

<aside class="encadre encadre--euro">

### Une monnaie commune suffit-elle à fixer le prix&nbsp;? Trente ans d'écarts avec l'Allemagne {#euro-et-taux}

Non, à en juger par trente ans de taux à 10 ans comparés à ceux de l'Allemagne, avec des pays restés hors de l'euro pour témoins. Avant 1999, l'écart italien fond de {{< monde-val "ec_it_1995" >}} à {{< monde-val "ec_it_1998" >}} point, mais celui de la Suède aussi, de {{< monde-val "ec_se_1995" >}} à {{< monde-val "ec_se_1998" >}}&nbsp;: la convergence n'est pas propre à l'euro. En 2012, la Grèce emprunte {{< monde-val "ec_el_2012" >}} points au-dessus de l'Allemagne et le Portugal {{< monde-val "ec_pt_2012" >}}, plus qu'aucun pays resté en dehors&nbsp;; la détente suit ensuite les interventions de la BCE. En {{< monde-val "annee" >}}, la Suède et le Danemark empruntent moins cher que l'Allemagne, la France {{< monde-val "ec_fr_an" >}} point plus cher. **L'euro a supprimé le risque de change entre ses membres&nbsp;; il ne leur a pas garanti le taux allemand.**

<details class="repli"><summary>Trente ans d'écarts avec l'Allemagne&nbsp;: convergence avant 1999, hors de l'euro aussi&nbsp;; décrochage des membres fragiles en 2012&nbsp;; détente après les décisions de la BCE</summary>

Il s'agit du taux de marché à 10 ans, non du taux implicite du stock.

{{< dette-monde-tableau niveau="ecarts" >}}

**Avant l'euro, les écarts fondent, y compris hors de l'euro.** De 1995 à 1998, l'écart italien passe de {{< monde-val "ec_it_1995" >}} à {{< monde-val "ec_it_1998" >}} point, l'écart espagnol de {{< monde-val "ec_es_1995" >}} à {{< monde-val "ec_es_1998" >}}. Celui de la Suède, qui n'a jamais adopté l'euro, passe dans le même temps de {{< monde-val "ec_se_1995" >}} à {{< monde-val "ec_se_1998" >}}. La perspective d'entrer dans l'euro a pu peser pour les futurs membres, mais ces chiffres ne permettent pas d'en isoler la part.

**En 2012, l'euro ne protège pas ses membres les plus fragiles.** La Grèce emprunte alors {{< monde-val "ec_el_2012" >}} points au-dessus de l'Allemagne, le Portugal {{< monde-val "ec_pt_2012" >}}, l'Irlande {{< monde-val "ec_ie_2012" >}}, l'Espagne {{< monde-val "ec_es_2012" >}}, l'Italie {{< monde-val "ec_it_2012" >}}. Hors de l'euro, la Suède reste à {{< monde-val "ec_se_2012" >}} point au-dessus de l'Allemagne et le Danemark à {{< monde-val "ec_dk_2012" >}} point au-dessous&nbsp;; mais la Hongrie paie {{< monde-val "ec_hu_2012" >}} points&nbsp;: garder sa monnaie n'a pas protégé tout le monde. Aucun pays resté hors de l'euro n'atteint toutefois les niveaux grec et portugais, ceux d'États qui s'endettaient dans une monnaie dont ils ne maîtrisaient plus l'émission. Les écarts ne se referment qu'après l'engagement de la BCE, à l'été 2012, de défendre l'euro, puis ses achats massifs de titres publics à partir de 2015&nbsp;: la détente suit une décision de la banque centrale, qui peut changer, et non l'appartenance à l'euro, qui existait déjà en 2012.

**Aujourd'hui, rester hors de l'euro ne coûte pas forcément plus cher.** En {{< monde-val "annee" >}}, la Suède emprunte à 10 ans {{< monde-val "ec_se_an" >}} point **au-dessous** de l'Allemagne, le Danemark {{< monde-val "ec_dk_an" >}} point au-dessous&nbsp;; la France paie {{< monde-val "ec_fr_an" >}} point de plus que l'Allemagne, l'Italie {{< monde-val "ec_it_an" >}}. Hors de l'euro, la Pologne et la Hongrie paient bien davantage ({{< monde-val "ec_pl_an" >}} et {{< monde-val "ec_hu_an" >}} points), mais leur inflation récente est aussi bien plus forte&nbsp;; et puisque la Suède est, elle aussi, hors de l'euro, ce n'est pas la monnaie qui les en sépare.

</details>

</aside>

## La transmission&nbsp;: un repère de pression, non une prévision {#transmission}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-transmission.svg" alt="Nuage de points : en abscisse la part de la dette qui arrive à échéance dans l'année, en ordonnée l'écart entre le rendement à 10 ans et le taux implicite du stock. La France se situe parmi les pays où le rendement de marché dépasse le plus le taux implicite ; la Suède et le Portugal ont une part bien plus grande de leur dette à moins d'un an ; au Danemark, le rendement à 10 ans est inférieur au taux implicite." width="720" height="488" loading="lazy">
  <figcaption>Part de la dette arrivant à échéance dans l'année (Eurostat, dette par échéance résiduelle) et écart entre le rendement harmonisé à 10 ans et le taux implicite du stock, {{< monde-val "annee" >}}. Repère de transmission, non prévision.</figcaption>
</figure>

Le taux implicite d'une année rémunère une dette émise à des dates différentes&nbsp;: il ne rejoint les conditions de marché qu'au fil des refinancements. Deux mesures situent cette inertie&nbsp;: la part de la dette qui arrive à échéance dans l'année, et l'écart entre le rendement harmonisé à 10 ans et le taux implicite. Ni l'une ni l'autre n'est une prévision&nbsp;: un État n'emprunte pas qu'à 10 ans, et le rendement d'aujourd'hui n'est pas celui de demain.

**En France, {{< monde-val "fr_part_1an" >}} de la dette présente à fin {{< monde-val "annee" >}} a une échéance résiduelle inférieure à un an. En {{< monde-val "annee" >}}, le rendement harmonisé à 10 ans ({{< monde-val "fr_taux10" >}}) était supérieur de {{< monde-val "fr_ecart_taux" >}} au taux implicite du stock.** Si les conditions de financement demeuraient supérieures au coût de la dette remplacée, les refinancements exerceraient une pression haussière sur le coût moyen — le mécanisme que détaille la page [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/). Au Danemark, l'indicateur est orienté dans l'autre sens&nbsp;: le rendement à 10 ans se situe sous le taux implicite du stock ({{< monde-val "dk_ecart_taux" >}}).

## Le stock&nbsp;: un classement qui ne dit pas tout {#stock}

<figure class="figure-ciseau">
  <img src="/img/dette-monde-stock.svg" alt="Barres horizontales de la dette publique en pourcentage du PIB, fin {{< monde-val "annee" >}}, pour les 27 pays de l'Union européenne, de la Grèce, la plus endettée, à l'Estonie ; la France est troisième, à {{< monde-val "fr_stock_fin" >}}." width="720" height="543" loading="lazy">
  <figcaption>Stock de clôture&nbsp;: Eurostat, dette brute de Maastricht des administrations publiques, fin {{< monde-val "annee" >}}. En bleu, la zone euro&nbsp;; en orange, les pays hors zone euro.</figcaption>
</figure>

Fin {{< monde-val "annee" >}}, la France est le {{< monde-val "fr_rang_stock" >}} pays le plus endetté de l'Union européenne, à **{{< monde-val "fr_stock_fin" >}} du PIB**. C'est le classement que retiennent la plupart des comparaisons. Il mesure un stock brut, sans les actifs publics ni les engagements qui ne sont pas de la dette, comme les retraites futures&nbsp;; et, on l'a vu, il ne dit pas ce que cette dette coûte.

## Et hors d'Europe&nbsp;? {#hors-europe}

Hors de l'Union européenne, les données ne sont plus harmonisées. Pour les économies avancées, l'OCDE (*Economic Outlook*) permet un calcul voisin sur une base plus large, des passifs financiers bruts et non la dette de Maastricht&nbsp;; le rapport des intérêts à ces passifs n'est donc pas exactement le taux implicite européen. La France y figure, sur la même base, pour servir d'étalon. Trois cas font office de laboratoires.

{{< dette-monde-cas >}}

**Le Japon** doit, sur cette base, près du double de la France, mais son rapport intérêts/passifs est de {{< monde-val "jpn_prix" >}} contre {{< monde-val "fra_prix" >}}, et il consacre moins de ses recettes aux intérêts ({{< monde-val "jpn_charge" >}} contre {{< monde-val "fra_charge" >}}). **La Suisse**, avec sa propre monnaie, paie peu sur une dette faible, et ses actifs financiers dépassent ses passifs. **Les États-Unis**, pour des passifs proches de ceux de la France, consacrent aux intérêts {{< monde-val "usa_fra_rapport" >}} fois la part française de leurs recettes.

{{< dette-monde-tableau niveau="avances" repli="Voir toutes les économies avancées (OCDE)" >}}

<details class="repli"><summary>Grands émergents (indicatif)&nbsp;: l'Inde consacre {{< monde-val "ind_charge" >}} des recettes de son administration centrale aux intérêts, le Brésil {{< monde-val "bra_charge" >}} — prix et recettes non séparables sans données harmonisées</summary>

Seules des mesures indicatives existent&nbsp;: la dette selon le FMI, et les intérêts de la seule administration centrale selon la Banque mondiale, toujours pris la même année. L'Inde consacre {{< monde-val "ind_charge" >}} des recettes de son administration centrale aux intérêts, le Brésil {{< monde-val "bra_charge" >}}, l'Afrique du Sud {{< monde-val "zaf_charge" >}}, pour des dettes de {{< monde-val "ind_stock" >}}, {{< monde-val "bra_stock" >}} et {{< monde-val "zaf_stock" >}} du PIB selon le FMI, en {{< monde-val "ind_charge_annee" >}}, {{< monde-val "bra_charge_annee" >}} et {{< monde-val "zaf_charge_annee" >}}, dernières années publiées par la Banque mondiale. Une part de l'écart tient au prix payé, une autre à la faiblesse relative des recettes&nbsp;: sans données harmonisées, on ne peut pas les séparer.

{{< dette-monde-tableau niveau="emergents" >}}

</details>

<aside class="encadre">

**Et pour savoir si la dette va augmenter&nbsp;?** Cette page compare ce que la dette coûte aujourd'hui. La question de sa trajectoire est différente&nbsp;: un ratio de dette tend à croître quand le taux d'intérêt payé dépasse la croissance nominale de l'économie et que le budget, hors intérêts, reste en déficit. Cet écart entre taux et croissance, et ce qu'il a fallu ailleurs pour que la dette baisse, sont l'objet de [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)

</aside>

## Ce que ces données ne disent pas {#limites}

- **Une seule année.** Les relations décrites portent sur {{< monde-val "annee" >}}&nbsp;; elles ne disent rien de leur stabilité dans le temps.
- **Des corrélations, non des causes.** Une régression sur {{< monde-val "n_pays" >}} pays décrit une association. L'appartenance à l'euro et l'inflation passée sont d'ailleurs liées entre elles.
- **Un stock brut.** La dette de Maastricht ne déduit pas les actifs publics&nbsp;; la Suisse, dont les passifs financiers nets sont négatifs, montre l'importance de cet écart.
- **Des définitions voisines, non identiques.** Hors d'Europe, l'OCDE mesure des passifs financiers bruts, le FMI une dette brute, la Banque mondiale les seuls intérêts de l'administration centrale.
- **Le risque de crise.** Il dépend aussi de la croissance, du solde primaire, de la monnaie, des maturités et des créanciers&nbsp;: cette page ne le mesure pas.
- **Les détenteurs de la dette.** Banque centrale, non-résidents, épargnants nationaux&nbsp;: leur part change le risque et le coût d'une dette, et fera l'objet d'une analyse distincte.
- **Les engagements hors dette**, comme les retraites futures, n'entrent dans aucun de ces chiffres.

{{< confrontation-recherche verifie="2026-09-30" publie="oui" resume="l'absence de lien en coupe est retrouvée ailleurs&nbsp;; la lire comme une absence d'effet est contredit dans le temps et en période de crise" >}}
**Mesuré ici.** Sur une année et entre les {{< monde-val "n_pays" >}} pays de l'Union, l'absence de relation linéaire entre le stock de départ et le taux implicite&nbsp;; trente ans d'écarts de taux à 10&nbsp;ans avec l'Allemagne. Des calculs sur séries officielles, qui se valident par reproduction&nbsp;: aucun des textes lus ne mesure le taux implicite en coupe.

**Cohérent avec.** Dans leurs graphiques en coupe, Gruber et Kamin ne trouvent aucune relation apparente entre dette et taux longs de 19&nbsp;pays de l'OCDE&nbsp;; dans les émissions de 1999 à 2005, le ratio de dette n'explique plus les écarts de taux des membres de l'euro (Bernoth, von Hagen et Schuknecht). La réserve de la page tient aussi&nbsp;: estimée sur les variations internes à chaque pays, la dette projetée relève les taux longs de quelques points de base par point de PIB (Gruber et Kamin&nbsp;; Laubach, sur les taux anticipés américains). Sur l'euro, De Grauwe et Ji estiment qu'en 2010-2011 une part importante de la hausse des écarts des pays périphériques échappe à leurs fondamentaux budgétaires, part variable selon les pays, la Grèce faisant exception&nbsp;; Saka, Fuertes et Kalotychou, qui mettent cette hypothèse à l'épreuve, trouvent que les contagions significatives venues d'Espagne avant l'annonce de la BCE du 26&nbsp;juillet 2012 disparaissent après. De 1993 à 1997, les rendements de tous les pays de l'Union sauf la Grèce, y compris hors de l'euro, se rapprochent des niveaux allemand et américain (Bernoth, von Hagen et Schuknecht).

**Mis en danger par.** Toute lecture de l'absence de lien en coupe comme une absence d'effet&nbsp;: Gruber et Kamin l'attribuent à une variable omise, la solvabilité que les marchés prêtent à chaque État&nbsp;; De Grauwe et Ji trouvent dans la zone euro, après 2008, une relation significative et non linéaire&nbsp;; avant 1999, le niveau relatif de la dette prédisait l'écart à l'émission, après, c'est le poids du service de la dette dans les recettes (Bernoth, von Hagen et Schuknecht). D'où la formule de la page&nbsp;: le niveau ne **suffit pas** à prédire le prix. Une lecture trop large de 2012&nbsp;: les primes des contrats d'assurance contre le défaut baissent partout après l'annonce, hors de l'euro compris&nbsp;; l'étude établit la fin de la contagion, non que toute la détente vienne de la BCE, et ses auteurs interprètent leurs résultats comme favorables à son programme.

**Non établi.** Le lien entre prix de la dette et inflation passée hors de l'euro&nbsp;: Gruber et Kamin relient les taux longs à l'inflation projetée, non à l'inflation courante. La part propre de l'euro dans la convergence d'avant 1999&nbsp;: Bernoth, von Hagen et Schuknecht comparent des titres émis dans une même monnaie, sans risque de change, et ne séparent pas futurs membres et pays restés en dehors.

**Références lues**

- Gruber, J. et Kamin, S., «&nbsp;Fiscal Positions and Government Bond Yields in OECD Countries&nbsp;», Federal Reserve, International Finance Discussion Paper 1011, 2010.
- Bernoth, K., von Hagen, J. et Schuknecht, L., «&nbsp;Sovereign Risk Premiums in the European Government Bond Market&nbsp;», version révisée, mai 2006 (publié dans le *Journal of International Money and Finance*, 31(5), 2012).
- De Grauwe, P. et Ji, Y., «&nbsp;Self-Fulfilling Crises in the Eurozone: An Empirical Test&nbsp;», CEPS Working Document n°&nbsp;367, 2012 (publié dans le *Journal of International Money and Finance*, 34, 2013).
- Saka, O., Fuertes, A.-M. et Kalotychou, E., «&nbsp;ECB Policy and Eurozone Fragility: Was De Grauwe Right?&nbsp;», CEPS Working Document n°&nbsp;397, 2014 (publié dans le *Journal of International Money and Finance*, 54, 2015).
- Laubach, T., «&nbsp;New Evidence on the Interest Rate Effects of Budget Deficits and Debt&nbsp;», Finance and Economics Discussion Series 2003-12, Federal Reserve (publié, révisé, dans le *Journal of the European Economic Association*, 7(4), 2009).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

Le niveau d'une dette ne dit pas, à lui seul, ce qu'elle pèse. Dans l'Union, à dette voisine, la part des recettes absorbée par les intérêts varie de 1 à {{< monde-val "j_rapport" >}}&nbsp;: la charge dépend aussi du prix payé sur le stock et du niveau des recettes publiques.

La France en donne l'exemple. Fin {{< monde-val "annee" >}}, sa dette est la {{< monde-val "fr_rang_stock" >}} de l'Union, à {{< monde-val "fr_stock_fin" >}} du PIB&nbsp;; elle paie pourtant sur son stock un taux implicite dans la moyenne de la zone euro ({{< monde-val "fr_prix" >}}) et consacre aux intérêts {{< monde-val "fr_charge" >}} de ses recettes, moins que {{< monde-val "n_plus_charges_moins_endettes" >}} pays moins endettés qu'elle.

Cette position est une photographie, et elle a une échéance. Le taux implicite rémunère une dette émise à des dates différentes&nbsp;; en {{< monde-val "annee" >}}, le rendement à 10&nbsp;ans le dépassait de {{< monde-val "fr_ecart_taux" >}}, et {{< monde-val "fr_part_1an" >}} de la dette arrivait à échéance dans l'année. Si ces conditions duraient, chaque refinancement rapprocherait le prix du stock de celui du marché, et la charge monterait sans que la dette ait besoin de croître.

La monnaie commune ne fixe pas ce prix. L'euro a supprimé le risque de change entre ses membres, non l'écart de taux&nbsp;: en 2012, la Grèce empruntait {{< monde-val "ec_el_2012" >}}&nbsp;points au-dessus de l'Allemagne, et la détente n'est venue qu'après les interventions de la BCE.

Reste la trajectoire&nbsp;: un même niveau de dette peut monter ou baisser selon l'écart entre taux et croissance et selon le solde primaire. C'est l'objet de [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)
- [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Prolonger l'analyse" avis="non" >}}
Cette page mesure ce que la dette coûte, et pourquoi une même dette ne pèse pas partout de la même façon. Elle ne dit pas qui en supporte le coût. Le livre suit ce déplacement canal par canal — contribuable, épargnant, services publics, générations qui ne votent pas encore —, chiffres officiels à l'appui, pour montrer dans quelles configurations chacun supporte un coût. Il propose une méthode en trois questions — les faits sont-ils établis, le système tient-il sa promesse, qui décide — et, pour les issues qu'il envisage, le partage entre qui paie et qui gagne.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Europe (strictement comparable)** — Eurostat, administrations publiques (S.13), comptes nationaux SEC 2010, montants en monnaie nationale&nbsp;: intérêts versés et recettes (`gov_10a_main`, D41PAY et TR), dette de Maastricht (`gov_10dd_edpt1`), PIB (`nama_10_gdp`), dette par échéance résiduelle (`gov_10dd_ggd`), taux à 10 ans (`irt_lt_mcby_a`), indice des prix harmonisé (`prc_hicp_aind`).

Le working paper [AWP-09](/awp/awp-09/) reprend l'identité de la charge et ces écarts de taux, pays restés hors de l'euro en témoins, pour mettre à l'épreuve le récit d'une convergence des taux due à l'euro.

**Économies avancées hors UE (avec réserve)** — OCDE, *Economic Outlook*&nbsp;: intérêts bruts, recettes, PIB et passifs financiers bruts des administrations publiques.

**Grands émergents (indicatif)** — FMI, *World Economic Outlook* (dette brute des administrations publiques)&nbsp;; Banque mondiale, *World Development Indicators* (intérêts en % des recettes de l'administration centrale).

Les calculs, les statistiques et les figures sont produits par un script unique, relancé à chaque publication des sources&nbsp;; aucun chiffre de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/dette_monde.csv), une ligne par pays, lisible dans un tableur&nbsp;; [JSON](/dette_monde.json), avec les statistiques et les définitions. Méthode&nbsp;: la charge, le stock et le prix vérifient l'identité exacte donnée plus haut, avec la dette de fin d'année précédente (convention du taux implicite de la BCE, distincte du «&nbsp;coût apparent&nbsp;» d'Eurostat, fondé sur la dette moyenne)&nbsp;; la robustesse des coefficients est recalculée à chaque mise à jour sur des fenêtres d'inflation de deux à cinq ans&nbsp;; les statistiques sont des moindres carrés simples, descriptifs.

{{< reutiliser figures="figures_monde" jeu="dette_monde" sources="Eurostat, OCDE, FMI et Banque mondiale" donnees="Les 27 pays de l'Union européenne et les économies hors d'Europe, avec leurs niveaux de comparabilité, leurs définitions et leurs statistiques ; le même contenu existe en CSV, une ligne par pays, lisible dans un tableur." >}}
Cette page compare ce que représente une dette publique en quatre mesures&nbsp;: le stock, son prix, les recettes qui la servent et la vitesse à laquelle les nouveaux taux se transmettent. Dans l'Union européenne en {{< monde-val "annee" >}}, deux pays de dette voisine peuvent consacrer aux intérêts des parts de leurs recettes qui vont de 1 à {{< monde-val "j_rapport" >}}, et le prix de la dette n'a pas de lien linéaire avec son niveau. Ces relations décrivent une année et des associations, non des causes&nbsp;; elles ne mesurent pas le risque de crise.
{{< /reutiliser >}}
