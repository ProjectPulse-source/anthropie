---
title: "Pour enseigner : activités SES à partir de données officielles"
description: "Des activités prêtes pour la classe de SES, en Première et en Terminale : figures projetables, fiches élèves, corrigés et données, tirées des séries officielles de l'INSEE et d'Eurostat."
date: 2026-09-30
lastmod: 2026-09-30
# Page d'USAGE pour les enseignants, non une analyse : elle transforme les ressources existantes en activités,
# sans en recopier aucun chiffre (jetons dyn-val, monde-val, qp-val, lus dans les mêmes jeux que les pages).
# Exception au STOP des nouveaux ensembles accordée par l'auteur le 30/09 (arbitrage
# .claude/external-audits/ARBITRATIONS/ENTRANTE_2026-09-30_Dette_Pedagogie_arbitrage.md, tours 1 et 2).
# Français seulement : le programme de SES est français (exclusion déclarée, pas d'oubli).
# Invariant de neutralité : chaque question fait constater, calculer, comparer ou expliquer un mécanisme ;
# aucune ne demande de trancher une politique.
ressource:
  bloc: "enseigner"
  rang: 10
  nature: "Activités pédagogiques construites sur les séries officielles"
---

Chaque activité part d'une figure du site, projetable telle quelle, et d'une question du programme. La fiche élève et
son corrigé utilisent **les mêmes séries que les analyses** dont ils sont tirés&nbsp;: un chiffre y change quand il
change dans la page d'origine, jamais séparément. Les figures et les données sont sous licence CC&nbsp;BY&nbsp;4.0, à
reprendre en citant la source.

Les questions demandent de constater, de calculer, de comparer ou d'expliquer un mécanisme. Aucune ne demande de
trancher une politique.

## Dette publique, Première et Terminale {#dette-publique}

Trois activités, du financement de l'État en Première aux politiques budgétaires européennes en Terminale, puis un
prolongement sur la redistribution. Chacune tient en une vingtaine de minutes.

### Première — Comment l'État finance-t-il son déficit&nbsp;? {#premiere-financement}

<section class="fiche" id="fiche-premiere">

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-premiere">Imprimer la fiche élève</button></p>

**Programme.** Chapitre «&nbsp;Comment les agents économiques se financent-ils&nbsp;?&nbsp;» — «&nbsp;Savoir que le solde
budgétaire résulte de la différence entre les recettes (fiscales et non fiscales) et les dépenses de l'État&nbsp;;
comprendre que le déficit budgétaire est financé par l'emprunt&nbsp;» (Éduscol).

**Durée**&nbsp;: 20&nbsp;minutes. **Support**&nbsp;: la cascade ci-dessous, tirée de [Pourquoi la dette publique
augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/#cascade)

{{< figure-svg fichier="dette-dynamique-cascade" alt="Cascade de la variation du ratio dette/PIB de la France sur trente ans : l'effet des intérêts monte, celui de la croissance nominale redescend presque d'autant, les déficits primaires portent l'essentiel de la hausse, les ajustements flux-stock ajoutent le reste." >}}D'où vient la hausse du ratio dette/PIB, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}} (Eurostat).{{< /figure-svg >}}

**Fiche élève**

1. Relevez le ratio dette publique/PIB en {{< dyn-val "annee_depart" >}} et en {{< dyn-val "annee_fin" >}}. De combien de points a-t-il augmenté&nbsp;?
2. Un **déficit primaire** est l'écart entre les dépenses et les recettes publiques, hors intérêts. Expliquez pourquoi un déficit fait augmenter la dette.
3. Parmi les trois termes de la figure, lequel explique l'essentiel de la hausse&nbsp;? Quelle part de la hausse représente-t-il&nbsp;?
4. Les intérêts versés ont poussé le ratio de {{< dyn-val "effet_interets" >}}&nbsp;points. Pourquoi ne suffisent-ils pas à expliquer la hausse&nbsp;?

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

1. De {{< dyn-val "dette_depart" >}}&nbsp;% à {{< dyn-val "dette_fin" >}}&nbsp;% du PIB&nbsp;: une hausse de {{< dyn-val "hausse" >}}&nbsp;points.
2. Quand les dépenses dépassent les recettes, l'État emprunte la différence&nbsp;: le déficit de l'année s'ajoute à la dette accumulée. C'est le lien que fixe le programme entre solde budgétaire et emprunt.
3. Les déficits primaires&nbsp;: {{< dyn-val "deficits_primaires" >}}&nbsp;points sur {{< dyn-val "hausse" >}}, soit {{< dyn-val "part_deficits" >}}&nbsp;% de la hausse.
4. Parce que la croissance du PIB nominal a joué en sens inverse&nbsp;: elle a retiré {{< dyn-val "effet_croissance" >}}&nbsp;points au ratio, car une dette constante pèse moins dans un PIB qui grandit. Les deux effets se compensent presque (effet net {{< dyn-val "effet_net" >}}&nbsp;point). À faire remarquer&nbsp;: c'est une décomposition comptable, qui dit par quel terme la dette a monté, pas pourquoi les déficits ont existé.

</details>

**Données**&nbsp;: [dette_dynamique.csv](/dette_dynamique.csv), une ligne par année.

</section>

### Terminale — La dette pèse-t-elle partout de la même façon&nbsp;? {#terminale-europe}

<section class="fiche" id="fiche-terminale">

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-terminale">Imprimer la fiche élève</button></p>

**Programme.** Chapitre «&nbsp;Quelles politiques économiques dans le cadre européen&nbsp;?&nbsp;» — la politique budgétaire
est «&nbsp;du ressort de chaque pays membre mais contrainte par les traités européens&nbsp;» (Éduscol). La ressource
d'accompagnement du chapitre pose la question de la soutenabilité de la dette et rappelle le repère de 60&nbsp;% du PIB.

**Durée**&nbsp;: 20&nbsp;minutes. **Support**&nbsp;: le nuage de points ci-dessous, tiré de [Dette publique&nbsp;: pourquoi
100&nbsp;% du PIB ne pèse pas partout de la même façon](/dette-publique-comparaison-internationale/#meme-dette)

{{< figure-svg fichier="dette-monde-charge" alt="Nuage de points pour les 27 pays de l'Union européenne : en abscisse la dette rapportée au PIB, en ordonnée les intérêts en pourcentage des recettes publiques. Des pays de dette voisine se situent à des hauteurs très différentes." >}}Dette de départ et part des recettes publiques consacrée aux intérêts, Union européenne, {{< monde-val "annee" >}} (Eurostat).{{< /figure-svg >}}

**Fiche élève**

1. Repérez la France sur la figure. Quelle est sa dette de départ, et quelle part de ses recettes consacre-t-elle aux intérêts&nbsp;?
2. {{< monde-val "j_haut_le_maj" >}} et {{< monde-val "j_bas_le" >}} ont une dette voisine ({{< monde-val "j_haut_stock" >}} et {{< monde-val "j_bas_stock" >}} du PIB). Comparez la part de leurs recettes consacrée aux intérêts.
3. {{< monde-val "j_haut_le_maj" >}} paie un taux de {{< monde-val "j_haut_prix" >}} sur sa dette, {{< monde-val "j_bas_le" >}} {{< monde-val "j_bas_prix" >}}&nbsp;; ses recettes représentent {{< monde-val "j_haut_rec" >}} du PIB, contre {{< monde-val "j_bas_rec" >}}. Expliquez l'écart de charge à l'aide de ces deux éléments.
4. Le repère européen de 60&nbsp;% porte sur le niveau de la dette. D'après la figure, ce niveau suffit-il à dire ce que la dette coûte à un pays&nbsp;? Justifiez.

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

1. Une dette de départ de {{< monde-val "fr_stock" >}} du PIB&nbsp;; {{< monde-val "fr_charge" >}} de ses recettes consacrés aux intérêts.
2. {{< monde-val "j_haut_charge" >}} pour {{< monde-val "j_haut_le" >}}, {{< monde-val "j_bas_charge" >}} pour {{< monde-val "j_bas_le" >}}&nbsp;: à dette voisine, une charge de 1 à {{< monde-val "j_rapport" >}}.
3. La charge rapporte les intérêts aux recettes&nbsp;: elle dépend du **prix** de la dette (le taux payé sur le stock) et du **niveau des recettes**. {{< monde-val "j_haut_le_maj" >}} cumule un prix plus élevé et des recettes plus faibles.
4. Non&nbsp;: le stock ne fixe ni le prix de la dette ni les recettes disponibles pour la servir. C'est une limite d'un indicateur, pas un jugement sur la règle.

**Approfondissement, hors objectifs du programme.** En {{< dyn-val "annee_fin" >}}, le taux implicite de la dette française ({{< dyn-val "taux_implicite_dernier" >}}&nbsp;%) et la croissance nominale ({{< dyn-val "croissance_derniere" >}}&nbsp;%) étaient presque égaux&nbsp;: à solde primaire nul, le ratio serait resté presque stable. Si le taux dépasse durablement la croissance, le ratio monte même sans déficit primaire&nbsp;: c'est la mécanique de la soutenabilité, détaillée dans [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/#identite)

</details>

**Données**&nbsp;: [dette_monde.csv](/dette_monde.csv), un pays par ligne.

</section>

### Prolongement — Qui verse, qui reçoit&nbsp;? {#prolongement-redistribution}

<section class="fiche" id="fiche-prolongement">

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-prolongement">Imprimer la fiche élève</button></p>

**Usage.** Un prolongement documentaire sur la fiscalité et la redistribution, à rattacher au chapitre de Terminale
sur la justice sociale selon la progression de la classe.

**Durée**&nbsp;: 20&nbsp;minutes. **Support**&nbsp;: la figure ci-dessous, tirée de [Qui paie vraiment la dette
publique&nbsp;?](/qui-paie-la-dette-publique/)

{{< figure-svg fichier="qui-paie-redistribution" alt="Barres par dixième de niveau de vie : au-dessus de zéro, les transferts publics reçus ; sous zéro, les prélèvements versés, qui croissent fortement du premier au dernier dixième." >}}Prélèvements versés et transferts reçus par dixième de niveau de vie, en euros par unité de consommation, {{< qp-val "cd_annee" >}} (INSEE, comptes nationaux distribués).{{< /figure-svg >}}

**Fiche élève**

1. Relevez les prélèvements versés par unité de consommation par les 10&nbsp;% les plus modestes et par les 10&nbsp;% les plus aisés. Combien de fois plus paient les seconds&nbsp;?
2. À partir de quel dixième, en moyenne, les prélèvements versés dépassent-ils les transferts reçus&nbsp;?
3. Une moyenne par dixième décrit un groupe, pas chaque personne. Expliquez pourquoi, dans un même dixième, certaines personnes peuvent recevoir plus qu'elles ne versent et d'autres l'inverse.

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

1. {{< qp-val "d1_prel" >}}&nbsp;€ et {{< qp-val "d10_prel" >}}&nbsp;€ par unité de consommation en {{< qp-val "cd_annee" >}}&nbsp;: environ {{< qp-val "ratio_prel" >}}&nbsp;fois plus.
2. À partir du dixième noté {{< qp-val "net_bascule" >}}, en moyenne par unité de consommation.
3. Les situations diffèrent à revenu voisin&nbsp;: âge, retraite ou activité, enfants, patrimoine. Rapporté aux personnes, {{< qp-val "benef_ensemble" >}}&nbsp;% sont bénéficiaires nettes cette année-là. Ce sont des comptes d'une année, selon les conventions de l'INSEE&nbsp;: ils ne disent pas qui paiera la dette demain.

</details>

**Données**&nbsp;: [qui_paie_donnees.csv](/qui_paie_donnees.csv).

</section>

### Exemplaire de consultation {#exemplaire}

Les enseignants de SES qui souhaitent prolonger ces activités peuvent disposer, dans la limite des exemplaires
disponibles, d'un exemplaire numérique de consultation de *Dette publique&nbsp;: qui paie vraiment&nbsp;?* Il est
proposé sans contrepartie et sous réserve des règles applicables dans votre établissement.
[Demander un exemplaire →](/ressources-offertes/dette-publique-enseignants/)

### Méthode et sources {#methode}

Toutes les figures viennent des quatre pages du dossier, qui en donnent la méthode, les limites et les sources&nbsp;:
[Pourquoi la dette augmente](/pourquoi-la-dette-publique-augmente/) · [Combien elle coûte](/cout-de-la-dette-publique/)
· [Qui paie](/qui-paie-la-dette-publique/) · [Et ailleurs](/dette-publique-comparaison-internationale/). Les extraits
du programme viennent des ressources d'accompagnement publiées par Éduscol pour la Première (juin 2019) et la
Terminale (août 2020).

<script src="/js/fiche-imprimer.js" defer></script>
