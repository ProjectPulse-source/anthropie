---
title: "Enseigner en SES avec les données officielles : dette publique, parcours après le bac"
description: "Activités de SES prêtes pour la classe : déficit et emprunt en Première, politiques budgétaires européennes, redistribution et devenir après une première année de licence en Terminale, avec les données de l'INSEE, d'Eurostat et du SIES."
og_title: "Enseigner en SES avec les données officielles — quatre activités prêtes pour la classe"
og_image: "images/og-dette-dynamique.jpg"
og_image_alt: "La dette publique française décomposée depuis 1995 : la figure d'où part l'activité de Première."
date: 2026-09-30
lastmod: 2026-10-02
# Page d'USAGE pour les enseignants, non une analyse : elle transforme les ressources existantes en activités,
# sans en recopier aucun chiffre (jetons dyn-val, monde-val, qp-val, lus dans les mêmes jeux que les pages).
# Quatrième activité (02/10/2026) : figure et jeu PROPRES à cette page (décision de l'auteur, exception écrite dans
# CLAUDE.md, « Couche pédagogique ») ; jetons licence-val, générateur scripts/generer_parcours_licence.py. La page ne
# déclare pas `donnees:` : elle reste une page d'usage.
# Exception au STOP des nouveaux ensembles accordée par l'auteur le 30/09 (arbitrage
# .claude/external-audits/ARBITRATIONS/ENTRANTE_2026-09-30_Dette_Pedagogie_arbitrage.md, tours 1 et 2), étendue par
# lui le 02/10 à la quatrième activité et à ses fichiers.
# Français seulement : le programme de SES est français (exclusion déclarée, pas d'oubli).
# Invariant de neutralité : chaque question fait constater, calculer, comparer ou expliquer un mécanisme ;
# aucune ne demande de trancher une politique.
ressource:
  bloc: "enseigner"
  rang: 10
  nature: "Activités pédagogiques construites sur les séries officielles"
  encart: true
  bouton: "Voir les activités"
---

Chaque activité part d'une figure du site, projetable telle quelle, et d'une question du programme. La fiche élève et
son corrigé sont écrits **à partir des séries elles-mêmes**&nbsp;: un chiffre y change quand la série change, jamais
séparément. Les figures et la compilation des données sont sous licence CC&nbsp;BY&nbsp;4.0, à
reprendre en citant la source&nbsp;; les séries brutes restent soumises aux conditions de l'INSEE, d'Eurostat et du
service statistique du ministère de l'Enseignement supérieur (SIES).

Les questions demandent de constater, de calculer, de comparer ou d'expliquer un mécanisme. Aucune ne demande de
trancher une politique.

## Dette publique, Première et Terminale {#dette-publique}

Trois activités, du financement de l'État en Première aux politiques budgétaires européennes en Terminale, puis un
prolongement sur la redistribution. Chacune tient en une vingtaine de minutes.

<section class="fiche" id="fiche-premiere">

### Première — Comment l'État finance-t-il son déficit&nbsp;? {#premiere-financement}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-premiere">Imprimer la fiche élève — sans corrigé</button></p>

**Programme.** Chapitre «&nbsp;Comment les agents économiques se financent-ils&nbsp;?&nbsp;» — «&nbsp;Savoir que le solde
budgétaire résulte de la différence entre les recettes (fiscales et non fiscales) et les dépenses de l'État&nbsp;;
comprendre que le déficit budgétaire est financé par l'emprunt&nbsp;» (Éduscol).

**Du programme au document.** Le programme porte ici sur le budget de l'État. La figure élargit l'analyse à
l'ensemble des administrations publiques — État, collectivités locales, administrations de sécurité sociale — et
isole le déficit primaire, calculé hors intérêts. Les notions sont liées, leurs périmètres ne sont pas identiques.

**Durée**&nbsp;: 20&nbsp;minutes. **Support**&nbsp;: la cascade ci-dessous, tirée de [Pourquoi la dette publique
augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/#cascade)

{{< figure-svg fichier="dette-dynamique-cascade" alt="Cascade de la variation du ratio dette/PIB de la France sur trente ans : l'effet des intérêts monte, celui de la croissance nominale redescend presque d'autant, les déficits primaires portent l'essentiel de la hausse, les ajustements flux-stock ajoutent le reste." >}}D'où vient la hausse du ratio dette/PIB, France, {{< dyn-val "annee_depart" >}}-{{< dyn-val "annee_fin" >}} (Eurostat).{{< /figure-svg >}}

**Fiche élève**

1. Relevez le ratio dette publique/PIB en {{< dyn-val "annee_depart" >}} et en {{< dyn-val "annee_fin" >}}. De combien de points a-t-il augmenté&nbsp;?
2. Un **déficit primaire** est l'écart entre les dépenses et les recettes publiques, hors intérêts. Expliquez pourquoi un déficit fait augmenter la dette.
3. Parmi les contributions représentées, laquelle explique l'essentiel de la hausse nette&nbsp;? Quelle part de la hausse représente-t-elle&nbsp;?
4. Les intérêts versés ont poussé le ratio de {{< dyn-val "effet_interets" >}}&nbsp;points. Pourquoi ne suffisent-ils pas à expliquer la hausse&nbsp;?

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

1. De {{< dyn-val "dette_depart" >}}&nbsp;% à {{< dyn-val "dette_fin" >}}&nbsp;% du PIB&nbsp;: une hausse de {{< dyn-val "hausse" >}}&nbsp;points.
2. Un déficit crée un besoin de financement, couvert par l'emprunt&nbsp;: toutes choses égales par ailleurs, il augmente la dette. C'est le lien que fixe le programme entre solde budgétaire et emprunt. La variation exacte de la dette comprend aussi des ajustements flux-stock, qui ne passent pas par le déficit.
3. Les déficits primaires&nbsp;: {{< dyn-val "deficits_primaires" >}}&nbsp;points sur {{< dyn-val "hausse" >}}, soit {{< dyn-val "part_deficits" >}}&nbsp;% de la hausse nette du ratio entre {{< dyn-val "annee_depart" >}} et {{< dyn-val "annee_fin" >}}, dans cette décomposition comptable — et non «&nbsp;87&nbsp;% de la dette&nbsp;».
4. Parce que la croissance du PIB nominal a joué en sens inverse&nbsp;: elle a retiré {{< dyn-val "effet_croissance" >}}&nbsp;points au ratio, car une dette constante pèse moins dans un PIB qui grandit. Les deux effets se compensent presque (effet net {{< dyn-val "effet_net" >}}&nbsp;point). À faire remarquer&nbsp;: c'est une décomposition comptable, qui dit par quel terme la dette a monté, pas pourquoi les déficits ont existé.

</details>

**Données**&nbsp;: [dette_dynamique.csv](/dette_dynamique.csv), une ligne par année.

</section>

<section class="fiche" id="fiche-terminale">

### Terminale — La dette pèse-t-elle partout de la même façon&nbsp;? {#terminale-europe}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-terminale">Imprimer la fiche élève — sans corrigé</button></p>

**Programme.** Chapitre «&nbsp;Quelles politiques économiques dans le cadre européen&nbsp;?&nbsp;» — la politique budgétaire
est «&nbsp;du ressort de chaque pays membre mais contrainte par les traités européens&nbsp;» (Éduscol). La ressource
d'accompagnement du chapitre pose la question de la soutenabilité de la dette et rappelle la valeur de référence de 60&nbsp;% du PIB.

**Durée**&nbsp;: 20&nbsp;minutes. **Support**&nbsp;: le nuage de points ci-dessous, tiré de [Dette publique&nbsp;: pourquoi
100&nbsp;% du PIB ne pèse pas partout de la même façon](/dette-publique-comparaison-internationale/#meme-dette)

{{< figure-svg fichier="dette-monde-charge" alt="Nuage de points pour les 27 pays de l'Union européenne : en abscisse la dette rapportée au PIB, en ordonnée les intérêts en pourcentage des recettes publiques. Des pays de dette voisine se situent à des hauteurs très différentes." >}}Dette de départ et part des recettes publiques consacrée aux intérêts, Union européenne, {{< monde-val "annee" >}} (Eurostat).{{< /figure-svg >}}

**Fiche élève**

1. Repérez la France sur la figure. Quelle est sa dette de départ (encours de fin {{< monde-val "annee_1" >}} rapporté au PIB {{< monde-val "annee" >}}), et quelle part de ses recettes consacre-t-elle aux intérêts&nbsp;?
2. {{< monde-val "j_haut_le_maj" >}} et {{< monde-val "j_bas_le" >}} ont une dette voisine ({{< monde-val "j_haut_stock" >}} et {{< monde-val "j_bas_stock" >}} du PIB). Comparez la part de leurs recettes consacrée aux intérêts.
3. {{< monde-val "j_haut_le_maj" >}} paie un taux de {{< monde-val "j_haut_prix" >}} sur sa dette, {{< monde-val "j_bas_le" >}} {{< monde-val "j_bas_prix" >}}&nbsp;; ses recettes représentent {{< monde-val "j_haut_rec" >}} du PIB, contre {{< monde-val "j_bas_rec" >}}. Expliquez l'écart de charge à l'aide de ces deux éléments.
4. La valeur de référence de 60&nbsp;% du PIB inscrite dans les traités européens porte sur le niveau de la dette. D'après la figure, ce niveau suffit-il à dire ce que la dette coûte à un pays&nbsp;? Justifiez.

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

1. Une dette de départ de {{< monde-val "fr_stock" >}} du PIB&nbsp;; {{< monde-val "fr_charge" >}} de ses recettes consacrés aux intérêts. Attention à la convention&nbsp;: l'encours de fin {{< monde-val "annee_1" >}} est rapporté au PIB de {{< monde-val "annee" >}}, l'année où la charge est payée&nbsp;; le ratio officiel publié par Eurostat pour fin {{< monde-val "annee_1" >}} le rapporte au PIB de {{< monde-val "annee_1" >}}, d'où un chiffre différent.
2. {{< monde-val "j_haut_charge" >}} pour {{< monde-val "j_haut_le" >}}, {{< monde-val "j_bas_charge" >}} pour {{< monde-val "j_bas_le" >}}&nbsp;: à dette voisine, une charge de 1 à {{< monde-val "j_rapport" >}}.
3. La charge rapporte les intérêts aux recettes&nbsp;: elle dépend du **prix** de la dette (le taux payé sur le stock) et du **niveau des recettes**. {{< monde-val "j_haut_le_maj" >}} cumule un prix plus élevé et des recettes plus faibles.
4. Non&nbsp;: le stock ne fixe ni le prix de la dette ni les recettes disponibles pour la servir. C'est une limite d'un indicateur, pas un jugement sur la règle. Le cadre budgétaire européen a été réformé en 2024&nbsp;: la valeur de référence de 60&nbsp;% demeure, mais la surveillance ne se résume pas à ce seuil.

**Approfondissement, hors objectifs du programme.** En {{< dyn-val "annee_fin" >}}, le taux implicite de la dette française ({{< dyn-val "taux_implicite_dernier" >}}&nbsp;%) et la croissance nominale ({{< dyn-val "croissance_derniere" >}}&nbsp;%) étaient presque égaux&nbsp;: à solde primaire nul et hors ajustements flux-stock, le ratio serait resté presque stable. À ajustements flux-stock nuls, si le taux implicite dépasse durablement la croissance nominale, cet effet pousse le ratio vers le haut même avec un solde primaire équilibré&nbsp;: c'est la mécanique de la soutenabilité, détaillée dans [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/#identite)

</details>

**Données**&nbsp;: [dette_monde.csv](/dette_monde.csv), un pays par ligne.

</section>

<section class="fiche" id="fiche-prolongement">

### Terminale, justice sociale — Qui verse, qui reçoit&nbsp;? {#prolongement-redistribution}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-prolongement">Imprimer la fiche élève — sans corrigé</button></p>

**Lien au programme.** Chapitre de Terminale sur la justice sociale&nbsp;: l'activité porte sur les instruments de
l'action publique — prélèvements, prestations et services collectifs. Elle n'aborde pas à elle seule les différentes
conceptions de la justice sociale, ni les débats sur leur efficacité et leur légitimité.

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

## Avons-nous tous le même droit à l'erreur&nbsp;? {#droit-a-l-erreur}

Une activité de Terminale pour le chapitre sur l'École. La question est celle de l'auteur, non une notion du
programme&nbsp;: la fiche la ramène à ce qui se mesure. Que deviennent, un an après, les bacheliers entrés en première
année de licence, selon leur origine sociale&nbsp;?

<section class="fiche" id="fiche-licence">

### Terminale — Après une première année de licence&nbsp;: les mêmes suites pour tous&nbsp;? {#terminale-licence}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-licence">Imprimer la fiche élève — sans corrigé</button></p>

**Programme.** Chapitre «&nbsp;Quelle est l'action de l'École sur les destins individuels et sur l'évolution de la
société&nbsp;?&nbsp;» — «&nbsp;Comprendre la multiplicité des facteurs d'inégalités de réussite scolaire (notamment,
rôle de l'École, rôle du capital culturel et des investissements familiaux, socialisation selon le genre, effets des
stratégies des ménages) dans la construction des trajectoires individuelles de formation&nbsp;» (Éduscol).

**Du programme au document.** Le programme porte sur l'École dans son ensemble&nbsp;; la figure suit les bacheliers
entrés en première année de licence à l'université. Elle ne décrit pas les parcours de tous les entrants dans
l'enseignement supérieur&nbsp;; les départs de la licence vers un BUT, une section de technicien supérieur, une classe
préparatoire ou une école y sont comptés comme réorientations. Elle décrit une situation d'inscription un an après,
non un échec ni une erreur. Quatre définitions de la source sont nécessaires à la lecture. «&nbsp;Passé en deuxième
année&nbsp;» comprend l'inscription en troisième année et, pour les licences accès santé, l'entrée en études de
santé. «&nbsp;Recommencer une première année&nbsp;» comprend les changements de discipline à l'intérieur de la
licence. «&nbsp;Réorienté&nbsp;» désigne une inscription dans une autre formation que la licence. «&nbsp;Non
retrouvé&nbsp;» désigne un étudiant absent des fichiers d'inscription&nbsp;: la source parle de «&nbsp;sortie de
l'enseignement supérieur&nbsp;», bien que certains étudient à l'étranger ou dans une formation que ces fichiers ne
suivent pas. L'origine sociale est une catégorie statistique, construite par le service statistique du ministère à
partir de la profession du parent référent&nbsp;; elle ne porte aucun jugement sur les personnes.

**Durée indicative**&nbsp;: 20 à 30&nbsp;minutes pour les questions 1 à 5, selon les acquis des élèves&nbsp;; la
question 6 est un prolongement. **Support**&nbsp;: la figure ci-dessous, construite pour cette activité à partir des
tableaux du SIES.

{{< figure-svg fichier="parcours-licence-devenir" alt="Cinq barres horizontales empilées à 100 %, une par origine sociale puis l'ensemble : part des étudiants passés en deuxième année, recommençant une première année, réorientés hors de la licence ou non retrouvés dans les fichiers d'inscription. La part passée en deuxième année diminue de l'origine très favorisée à l'origine défavorisée ; la part réorientée reste presque la même. Les valeurs sont dans le tableau qui suit la figure." >}}Source&nbsp;: MESRE-SIES, {{< licence-val "note" >}}. [Agrandir la figure](/img/parcours-licence-devenir.png){{< /figure-svg >}}

{{< licence-tableau >}}

**Fiche élève**

1. Relevez la part des étudiants passés en deuxième année pour l'origine très favorisée et pour l'origine défavorisée. Quel est l'écart en points&nbsp;?
2. Relevez la part des étudiants réorientés hors de la licence dans chacune des quatre origines. Que remarquez-vous&nbsp;?
3. Pour chacune des deux origines extrêmes, calculez la part des étudiants non passés en deuxième année (100 moins la part des étudiants passés). Parmi ces étudiants, quelle proportion n'est plus retrouvée dans les fichiers d'inscription&nbsp;? *Aide&nbsp;: part des non retrouvés ÷ part des non-passés × 100.*
4. Calculez l'écart entre les deux origines pour la part des étudiants non retrouvés, d'abord sur tous les inscrits (figure), puis parmi les seuls étudiants non passés (question 3). Pour chacun des deux calculs, précisez quelle population sert de dénominateur.
5. Le programme cite plusieurs facteurs d'inégalités de réussite scolaire&nbsp;: rôle de l'École, capital culturel et investissements familiaux, stratégies des ménages. Proposez un mécanisme par lequel l'un d'eux pourrait jouer sur le fait de recommencer, de se réorienter ou d'arrêter. Quelle donnée faudrait-il pour le vérifier&nbsp;?
6. *Prolongement, chapitre sur la justice sociale.* La figure décrit des parcours différents selon l'origine sociale. En quoi ces écarts peuvent-ils éclairer la question de l'égalité des chances&nbsp;? Permettent-ils de conclure sur l'égalité des droits ou sur l'égalité des situations&nbsp;? Justifiez.

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

1. {{< licence-val "tf_passage" >}}&nbsp;% et {{< licence-val "d_passage" >}}&nbsp;%&nbsp;: un écart de {{< licence-val "ecart_passage" >}}&nbsp;points.
2. {{< licence-val "tf_reorientation" >}}&nbsp;%, {{< licence-val "f_reorientation" >}}&nbsp;%, {{< licence-val "ad_reorientation" >}}&nbsp;% et {{< licence-val "d_reorientation" >}}&nbsp;%&nbsp;: presque le même taux d'une origine à l'autre, alors que les trois autres devenirs s'écartent. À préciser aux élèves&nbsp;: il s'agit des départs vers une autre formation que la licence. Un étudiant qui recommence une première année dans une autre discipline ou un autre établissement est compté avec les redoublants&nbsp;; c'est le cas de {{< licence-val "tf_redoublement_autre" >}}&nbsp;% des inscrits d'origine très favorisée et de {{< licence-val "d_redoublement_autre" >}}&nbsp;% de ceux d'origine défavorisée.
3. Non passés&nbsp;: {{< licence-val "tf_non_passage" >}}&nbsp;% et {{< licence-val "d_non_passage" >}}&nbsp;% des inscrits. Non retrouvés parmi eux&nbsp;: {{< licence-val "tf_sortie" >}}&nbsp;÷&nbsp;{{< licence-val "tf_non_passage" >}}, soit {{< licence-val "tf_sortie_np" >}}&nbsp;%&nbsp;; {{< licence-val "d_sortie" >}}&nbsp;÷&nbsp;{{< licence-val "d_non_passage" >}}, soit {{< licence-val "d_sortie_np" >}}&nbsp;%.
4. Sur tous les inscrits, l'écart est de {{< licence-val "ecart_sortie" >}}&nbsp;points ({{< licence-val "tf_sortie" >}}&nbsp;% et {{< licence-val "d_sortie" >}}&nbsp;%). Parmi les seuls étudiants non passés, les deux proportions sont proches&nbsp;: {{< licence-val "ecart_sortie_np" >}}&nbsp;point d'écart avec les valeurs arrondies de la question 3, {{< licence-val "ecart_sortie_np_decimales" >}}&nbsp;point pour l'élève qui garde ses décimales jusqu'au bout&nbsp;; les deux démarches sont justes. Le dénominateur a changé&nbsp;: on rapporte les étudiants non retrouvés aux seuls non-passés de chaque origine. L'écart observé sur tous les inscrits correspond donc surtout à la différence de fréquence du non-passage. C'est une décomposition arithmétique, non une explication&nbsp;: les deux groupes de non-passés ne sont pas nécessairement comparables, et le tableau relève une seule situation à la rentrée suivante, non un échec suivi d'une réaction. Parmi ces étudiants, l'inscription dans une autre formation que la licence est plus fréquente pour l'origine très favorisée ({{< licence-val "tf_reorientation_np" >}}&nbsp;% contre {{< licence-val "d_reorientation_np" >}}&nbsp;%), la réinscription en première année pour l'origine défavorisée ({{< licence-val "d_redoublement_np" >}}&nbsp;% contre {{< licence-val "tf_redoublement_np" >}}&nbsp;%). Le tableau ne dit pas si ces parcours répondent à une erreur d'orientation, à une contrainte ou à un choix. Ces constats se retrouvent sur les trois cohortes comparables, entrées de {{< licence-val "cohortes_lib" >}}.
5. Plusieurs réponses sont recevables, à titre d'hypothèses&nbsp;: connaître les formations vers lesquelles se réorienter (capital culturel), pouvoir financer une année de plus (investissements familiaux), choisir une filière en anticipant ses débouchés (stratégies des ménages). La figure ne permet d'en vérifier aucune. La même source montre de forts écarts de passage selon la mention au baccalauréat, {{< licence-val "mention_tb_passage" >}}&nbsp;% pour la mention très bien contre {{< licence-val "mention_p2_passage" >}}&nbsp;% après une admission au second groupe d'épreuves, mais elle ne croise pas la mention et l'origine sociale&nbsp;: ces tableaux ne permettent ni d'isoler l'effet propre de chaque caractéristique, ni de comparer leur poids. On décrit donc une association avec l'origine sociale, sans lui attribuer une cause. Il faudrait croiser origine sociale, parcours scolaire antérieur et formation suivie, recueillir les motifs des décisions et suivre les étudiants au-delà d'un an&nbsp;: un étudiant non retrouvé peut revenir.
6. La figure décrit des fréquences de parcours différentes selon l'origine sociale, parmi des étudiants déjà entrés en licence. Elle permet d'interroger l'égalité des chances, que la ressource d'accompagnement du programme définit comme l'indépendance entre la situation sociale acquise et la situation sociale héritée, sans identifier les causes des écarts. Comparer des étudiants de même préparation scolaire apporterait un éclairage de plus, mais cette préparation peut elle-même porter la trace d'inégalités antérieures. La figure ne renseigne ni les règles d'inscription, donc l'égalité des droits, ni la répartition des ressources et des positions sociales, donc l'égalité des situations.

</details>

**Données**&nbsp;: [parcours_licence.csv](/parcours_licence.csv), une ligne par cohorte, origine et devenir.

</section>

### Méthode et sources {#methode}

**Licence.** La figure sur la première année de licence est construite pour cette page à partir des tableaux nationaux
qui accompagnent la {{< licence-val "note" >}} du SIES, «&nbsp;Parcours et réussite en licence&nbsp;» (feuille
«&nbsp;Devenir cohorte {{< licence-val "cohorte" >}}&nbsp;»&nbsp;; {{< licence-val "inscrits" >}} néo-bacheliers,
universités et établissements assimilés, France entière). L'origine sociale est celle du parent référent, que le SIES
regroupe en quatre classes&nbsp;: très favorisée (cadres, enseignants), favorisée (professions intermédiaires), assez
défavorisée (employés), défavorisée (ouvriers)&nbsp;; les {{< licence-val "non_reponse_part" >}}&nbsp;% d'étudiants
dont l'origine n'est pas renseignée n'ont pas de barre distincte et restent compris dans l'ensemble. Les quatre
devenirs laissent {{< licence-val "residu" >}}&nbsp;étudiants hors compte&nbsp;; les barres reprennent les taux publiés,
arrondis au dixième, dont la somme peut différer légèrement de 100&nbsp;%. Les parts
calculées parmi les étudiants non passés sont un calcul de cette page, non une publication du SIES. Trois cohortes
seulement sont comparables&nbsp;: avant celle de 2021, le tableau ne suivait pas les réorientations hors de
l'université. Tableurs téléchargés le 2&nbsp;octobre 2026&nbsp;; les données publiques du ministère sont mises à
disposition sous Licence Ouverte. L'extrait du programme vient de l'annexe «&nbsp;Programme de sciences économiques
et sociales de terminale générale&nbsp;» publiée par Éduscol, la définition de l'égalité des chances de sa ressource
d'accompagnement sur la justice sociale (août 2020).

**Dette publique.** Les figures viennent des quatre pages du dossier, qui en donnent la méthode, les limites et les sources&nbsp;:

{{< pastilles label="Les quatre pages du dossier dette publique" >}}
- [Pourquoi la dette augmente](/pourquoi-la-dette-publique-augmente/)
- [Combien elle coûte](/cout-de-la-dette-publique/)
- [Qui paie](/qui-paie-la-dette-publique/)
- [Et ailleurs](/dette-publique-comparaison-internationale/)
{{< /pastilles >}}

Les extraits
du programme viennent des ressources d'accompagnement publiées par Éduscol pour la Première (juin 2019) et la
Terminale (août 2020).

{{< exemplaire slug="dette-publique-qui-paie-vraiment" lien="/ressources-offertes/dette-publique-enseignants/"
    surtitre="Pour les enseignants de SES" >}}
Les enseignants de SES qui souhaitent prolonger ces activités peuvent disposer, dans la limite des exemplaires
disponibles, d'un exemplaire numérique de consultation de *Dette publique&nbsp;: qui paie vraiment&nbsp;?* Il est
proposé sans contrepartie et sous réserve des règles applicables dans votre établissement.
{{< /exemplaire >}}

<script src="/js/fiche-imprimer.js" defer></script>
