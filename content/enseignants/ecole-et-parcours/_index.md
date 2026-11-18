---
title: "Avons-nous tous le même droit à l'erreur ?"
description: "Deux activités de SES pour la Terminale, chapitre sur l'École : où s'inscrivent les nouveaux bacheliers selon leur origine sociale, et ce que deviennent un an après les entrants en licence. Figures, fiches élèves, corrigés et données du SIES."
og_title: "Avons-nous tous le même droit à l'erreur ? — deux activités de SES sur l'École, Terminale"
og_image: "images/og-parcours-licence.jpg"   # scripts/og_enseignants.py ; vignette vig-parcours-licence.jpg lue par /ressources/
og_image_alt: "Quatre barres empilées : devenir des bacheliers un an après une première année de licence, selon l'origine sociale."
date: 2026-10-02
lastmod: 2026-11-18
journal:  # révisions qui changent la lecture de la page (partials/page-date-visible.html affiche la plus récente)
  - {date: 2026-11-18, texte: "Relecture des sources et contre-analyse externe : la page cite la note du SIES de juillet 2026, qui trouve faible, à caractéristiques égales, la corrélation entre origine sociale et réussite en licence ; la figure « Après le bac » est contrôlée sur le tableau 13.01 du SIES ; les questions 5 des deux activités demandent ce que la note de la figure ne nomme pas ; au corrigé 5 de la première, les parts par origine sont celles des bacheliers dont l'origine est renseignée."}
date_suit: [parcours_licence, acces_superieur]  # jeux affichés par la page : leur relevé entre dans sa date (sitemap) ; contrôle scripts/check-dates-jeux.py
# Second thème de la couche enseignants : UNE PAGE PAR THÈME (auteur, 02/10/2026 ; arbitrage
# .claude/external-audits/ARBITRATIONS/ENTRANTE_2026-10-02_Enseignants_Structure_arbitrage.md). Navigation « École et
# parcours », titre = la question de l'auteur (verrou). Deux déclencheurs de la règle « page propre » : matière
# documentaire propre (SIES, chapitre École) et cycle de mise à jour distinct (annuel, à la main, en novembre).
# Figure et jeu propres à la couche enseignants (CLAUDE.md, couche pédagogique, point 6) ; la page ne déclare pas
# `donnees:`. Français seulement. Aucune question ne demande de trancher une politique.
# L'ancre `#droit-a-l-erreur`, publiée quelques heures sur /enseignants/, y reste portée par la barre et renvoie ici.
ressource:
  type: ["usage"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "enseigner"
  discipline: "ses"   # une carte par discipline dans /ressources/ (03/10/2026)
  theme: "École et parcours"
  rang: 20
  nature: "Activités de SES — Terminale, chapitre sur l'École"
  intitule: "École et parcours : après le bac, après une année de licence"
  encart: true
  bouton: "Voir les activités"
  conception: "docs/conception/enseignants-ecole-et-parcours.md"  # fiche de conception (règle 12), écrite le 17/11/2026 après la relecture des sources
onglet:  # barre de la discipline (partials/barre-discipline.html)
  court: "École"
  role: "Terminale"
  id: "droit-a-l-erreur"   # ancre publiée le 02/10, portée par ce lien sur /enseignants/ : ne se retire pas
activite:  # JSON-LD LearningResource (partials/schema-activite.html) ; reprise du 17/11/2026
  nom: "Avons-nous tous le même droit à l'erreur ? Deux activités de SES sur l'École"
  niveau: "Terminale"
  discipline: "Sciences économiques et sociales"
  type: "Activité pédagogique"
  duree: "PT1H"  # deux activités de 20 à 30 minutes chacune (questions 1 à 5) ; timeRequired n'admet qu'une durée : borne haute cumulée
  enseigne: ["massification et démocratisation", "inégalités de réussite scolaire", "origine sociale", "écart en points et rapport", "changement de dénominateur", "inscription et choix", "association et causalité", "égalité des chances"]
  sources:
    - "https://www.education.gouv.fr/bo/19/Special8/MENE1921253A.htm"
    - "https://publication.enseignementsup-recherche.gouv.fr/eesr/FR/EESR18_ES_13/"
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
---

**Terminale, chapitre sur l'École.** Deux activités, rattachées chacune à un objectif du chapitre, sans prétendre l'épuiser. La première regarde où
s'inscrivent les nouveaux bacheliers selon leur origine sociale&nbsp;; la seconde, ce que deviennent un an après ceux
qui sont entrés en première année de licence. Elles portent sur les bacheliers de la même année (France métropolitaine et DROM pour la première, France entière pour la
seconde), dont les entrants en licence forment, à ces champs près, une partie, mais ne
permettent pas de relier un élève de l'une à l'autre. La question du titre est celle de l'auteur, non une notion du programme&nbsp;: les fiches la
ramènent à ce qui se mesure. Fiches et corrigés sont écrits à partir des séries elles-mêmes&nbsp;: un chiffre y change
quand la série change. Les fiches, les figures et la compilation des données sont sous licence CC&nbsp;BY&nbsp;4.0 (les données du SIES gardent leur propre licence), à
reprendre en citant la source&nbsp;; les questions demandent de constater, de calculer, de comparer, d'expliquer un mécanisme
ou de dire ce qu'un document permet d'affirmer, aucune ne demande de trancher une politique.

{{< dossier-lie bloc="ecole" >}}

<section class="fiche" id="fiche-acces">

### Terminale — Après le bac&nbsp;: les mêmes voies pour tous&nbsp;? {#terminale-apres-le-bac}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-acces">Imprimer la fiche élève — sans corrigé</button></p>

<div class="fiche__prof">

**Programme.** Chapitre «&nbsp;Quelle est l'action de l'École sur les destins individuels et sur l'évolution de la
société&nbsp;?&nbsp;» — «&nbsp;comprendre l'évolution, depuis les années 1950, des principaux indicateurs mesurant
l'accès à l'école et à l'enseignement supérieur (taux de scolarisation, taux d'accès à un diplôme ou à un type de
formation) en distinguant les processus de massification et de démocratisation&nbsp;» (Éduscol). Ce chapitre reste au programme, mais il ne figure pas parmi les questions évaluables à l'épreuve écrite de spécialité (note de service du 11&nbsp;septembre 2026, BO spécial n°&nbsp;4 du 17&nbsp;septembre 2026, annexe&nbsp;I, à compter de la session 2027).

**Du programme au document.** Le programme demande une évolution depuis les années 1950&nbsp;; la figure donne une
seule année, celle des bacheliers {{< acces-val "annee" >}}. Elle ne donne pas un taux d'accès, rapporté à une génération ou à toute une catégorie, mais la répartition entre types de formation des
seuls bacheliers qui poursuivent leurs études&nbsp;: ceux qui ne s'inscrivent nulle part n'y figurent pas. Elle
décrit des inscriptions observées, non des choix&nbsp;: une inscription dépend aussi de la série du baccalauréat, des
candidatures et des admissions. «&nbsp;Université&nbsp;» comprend les IUT&nbsp;; les sections de technicien supérieur
(STS) comprennent l'apprentissage. L'origine sociale est la catégorie socioprofessionnelle du parent, telle que la
source la classe, sans jugement sur les personnes&nbsp;; elle est renseignée pour
{{< acces-val "origine_renseignee" >}}&nbsp;% des inscrits. Elle manque surtout pour les inscrits en STS&nbsp;: les parts de la figure sont
calculées sur les seuls inscrits dont l'origine est connue.

**Durée indicative**&nbsp;: 20 à 30&nbsp;minutes pour les questions 1 à 5&nbsp;; la question 6 est un prolongement.
**Support**&nbsp;: la figure ci-dessous, construite pour cette activité à partir d'un tableau du service statistique du
ministère de l'Enseignement supérieur (SIES).

</div>

{{< figure-svg fichier="acces-superieur-origine" alt="Sept barres horizontales empilées à 100 %, une par catégorie socioprofessionnelle du parent puis l'ensemble des inscrits d'origine renseignée : répartition des nouveaux bacheliers inscrits dans l'enseignement supérieur entre l'université, les classes préparatoires, les sections de technicien supérieur et d'autres formations. Les valeurs sont dans le tableau qui suit la figure." >}}Source&nbsp;: MESRE-SIES, *État de l'enseignement supérieur, de la recherche et de l'innovation en France* {{< acces-val "edition" >}}. [Agrandir la figure](/img/acces-superieur-origine.png){{< /figure-svg >}}

{{< acces-tableau >}}

**Fiche élève**

1. Parmi les nouveaux bacheliers inscrits dans l'enseignement supérieur et dont l'origine sociale est renseignée, relevez la part de ceux qui sont inscrits en sections de technicien supérieur, puis en classes préparatoires, pour les enfants de cadres et pour les enfants d'ouvriers.
2. Pour chacune de ces deux filières, calculez combien de fois l'inscription est plus fréquente dans une catégorie que dans l'autre.
3. Quelle est la première destination des enfants d'ouvriers&nbsp;? Celle des cinq autres catégories&nbsp;?
4. Pour l'université, puis pour les classes préparatoires, calculez l'écart entre la catégorie où la part inscrite dans cette filière est la plus forte et celle où elle est la plus faible, d'abord en points, puis en rapport (la plus forte part divisée par la plus faible). Les deux mesures donnent-elles la même image&nbsp;?
5. Ce document permet-il d'affirmer que les élèves d'origines sociales différentes choisissent différemment&nbsp;? Justifiez à l'aide de la note en bas de la figure, puis citez deux informations que cette note ne nomme pas et qu'il faudrait connaître pour répondre.
6. *Prolongement.* Le programme distingue massification et démocratisation. Que faudrait-il ajouter à ce document pour parler de l'une et de l'autre&nbsp;? Quelles données faudrait-il recueillir pour savoir si les différences d'inscription selon l'origine sociale se retrouvent ensuite dans le parcours des mêmes élèves&nbsp;?

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

Pour les questions d'interprétation, tenir pour juste toute réponse qui sépare ce que les données établissent, ce qui reste plausible sans être démontré et ce que les documents contredisent.

1. Sections de technicien supérieur&nbsp;: {{< acces-val "cad_sts" >}}&nbsp;% des enfants de cadres inscrits dans le supérieur, {{< acces-val "ouv_sts" >}}&nbsp;% des enfants d'ouvriers inscrits. Classes préparatoires&nbsp;: {{< acces-val "cad_cpge" >}}&nbsp;% et {{< acces-val "ouv_cpge" >}}&nbsp;%.
2. Parmi les inscrits dont l'origine est connue, l'inscription en STS est {{< acces-val "sts_ouv_sur_cad" >}}&nbsp;fois plus fréquente pour les enfants d'ouvriers&nbsp;; l'inscription en classes préparatoires, {{< acces-val "cpge_cad_sur_ouv" >}}&nbsp;fois plus fréquente pour les enfants de cadres.
3. Les STS pour les enfants d'ouvriers ({{< acces-val "ouv_sts" >}}&nbsp;%, contre {{< acces-val "ouv_univ" >}}&nbsp;% à l'université)&nbsp;; l'université pour les cinq autres catégories, y compris les enfants de retraités et d'inactifs, pour qui les deux parts sont proches ({{< acces-val "ret_univ" >}}&nbsp;% et {{< acces-val "ret_sts" >}}&nbsp;%)&nbsp;; comme l'origine manque surtout en STS, ce dernier classement est fragile.
4. Université&nbsp;: professions intermédiaires ({{< acces-val "pi_univ" >}}&nbsp;%) et ouvriers ({{< acces-val "ouv_univ" >}}&nbsp;%), {{< acces-val "ecart_univ" >}}&nbsp;points d'écart, un rapport de 1 à {{< acces-val "rapport_univ" >}}. Classes préparatoires&nbsp;: cadres ({{< acces-val "cad_cpge" >}}&nbsp;%) et ouvriers ({{< acces-val "ouv_cpge" >}}&nbsp;%), {{< acces-val "ecart_cpge" >}}&nbsp;points, un rapport de 1 à {{< acces-val "rapport_cpge" >}}. En points, l'écart est plus faible pour les classes préparatoires&nbsp;; en rapport, il est bien plus fort. Une filière qui n'accueille qu'une faible part de chaque catégorie ne peut pas produire un grand écart en points&nbsp;: le rapport dit mieux ce qui sépare les catégories, l'écart en points dit mieux combien d'élèves, sur cent de chaque catégorie, sont concernés. Aucune des deux mesures n'est la bonne en soi, et ni l'une ni l'autre ne donne un nombre d'élèves&nbsp;: il faudrait pour cela les effectifs de chaque catégorie.
5. Non. Le document établit que les inscriptions diffèrent selon l'origine sociale&nbsp;; il n'observe ni les vœux, ni les admissions, ni les raisons. Une partie de l'écart peut passer par la série du baccalauréat, que ce tableau ne croise pas avec l'origine&nbsp;: {{< acces-val "cpge_bac_general" >}}&nbsp;% des nouveaux inscrits en classes préparatoires ont un baccalauréat général, contre {{< acces-val "sts_bac_general" >}}&nbsp;% en STS, où {{< acces-val "sts_bac_professionnel" >}}&nbsp;% ont un baccalauréat professionnel&nbsp;; et, parmi les bacheliers dont l'origine est renseignée, {{< acces-val "bac_general_cadres" >}}&nbsp;% des bacheliers généraux sont enfants de cadres et {{< acces-val "bac_general_ouvriers" >}}&nbsp;% enfants d'ouvriers, contre {{< acces-val "bac_professionnel_cadres" >}}&nbsp;% et {{< acces-val "bac_professionnel_ouvriers" >}}&nbsp;% des bacheliers professionnels. L'origine sociale est donc associée à la filière d'inscription, et une partie de cette association peut passer par le parcours scolaire antérieur&nbsp;; ces tableaux ne permettent pas de dire quelle partie. La note en bas de la figure nomme déjà la série du baccalauréat, les candidatures et les admissions&nbsp;; deux autres informations à connaître, par exemple parmi celles-ci&nbsp;: les raisons ou préférences déclarées des élèves, les résultats au baccalauréat, la distance aux formations et l'offre proche, les ressources de la famille et le coût des études.
6. Pour la massification, il faudrait la part d'une génération qui accède au baccalauréat puis à l'enseignement supérieur, à plusieurs dates. Pour la démocratisation, qui porte selon Éduscol sur l'égalité ou l'inégalité des chances d'accès, ici selon l'origine sociale, il faudrait les taux d'accès au baccalauréat et à l'enseignement supérieur selon l'origine, à plusieurs dates, puis ce même tableau à plusieurs dates, pour voir si l'association entre origine et filière s'affaiblit. Avec les deux éditions retenues ici, une seule comparaison est possible&nbsp;: d'une année à la suivante, aucune valeur ne bouge de plus d'un point et demi ({{< acces-val "chrono1_ouv_sts" >}}&nbsp;% des enfants d'ouvriers inscrits le sont en STS en {{< acces-val "chrono1_annee" >}}, {{< acces-val "chrono2_ouv_sts" >}}&nbsp;% en {{< acces-val "chrono2_annee" >}}&nbsp;; {{< acces-val "chrono1_cad_cpge" >}}&nbsp;% puis {{< acces-val "chrono2_cad_cpge" >}}&nbsp;% des enfants de cadres inscrits le sont en classes préparatoires), ce qui ne dit rien d'une évolution longue. Les deux activités de cette page ne suivent pas les élèves de l'une à l'autre&nbsp;: celle-ci porte sur tous les bacheliers qui poursuivent, la suivante sur les seuls entrants en licence. Pour savoir si les écarts se cumulent chez les mêmes élèves, il faudrait les suivre du baccalauréat aux années suivantes.

</details>

<div class="fiche__prof">

**Données**&nbsp;: [acces_superieur.csv](/acces_superieur.csv), une ligne par année, origine et filière.

</div>

</section>

<section class="fiche" id="fiche-licence">

### Terminale — Après une première année de licence&nbsp;: les mêmes suites pour tous&nbsp;? {#terminale-licence}

<p class="fiche__actions"><button type="button" class="how-to-cite__btn how-to-cite__btn--secondary" data-imprimer-fiche="fiche-licence">Imprimer la fiche élève — sans corrigé</button></p>

<div class="fiche__prof">

**Programme.** Chapitre «&nbsp;Quelle est l'action de l'École sur les destins individuels et sur l'évolution de la
société&nbsp;?&nbsp;» — «&nbsp;Comprendre la multiplicité des facteurs d'inégalités de réussite scolaire (notamment,
rôle de l'École, rôle du capital culturel et des investissements familiaux, socialisation selon le genre, effets des
stratégies des ménages) dans la construction des trajectoires individuelles de formation&nbsp;» (Éduscol). Même chapitre, même statut&nbsp;: au programme, hors des questions évaluables à l'épreuve écrite de spécialité à compter de la session 2027.

</div>

**Du programme au document.** Le programme porte sur l'École dans son ensemble&nbsp;; la figure suit les bacheliers
entrés en première année de licence à l'université. Elle ne décrit pas les parcours de tous les entrants dans
l'enseignement supérieur&nbsp;; les départs de la licence vers un BUT, une section de technicien supérieur, une classe
préparatoire ou une école y sont comptés comme réorientations. Elle décrit une situation d'inscription un an après,
non un échec ni une erreur. Quatre définitions de la source sont nécessaires à la lecture. «&nbsp;Passé en deuxième
année&nbsp;» comprend l'inscription en troisième année et, pour les licences accès santé, l'entrée en études de
santé. «&nbsp;Recommencer une première année&nbsp;» comprend les changements de discipline ou d'établissement à l'intérieur de la
licence. «&nbsp;Réorienté&nbsp;» désigne une inscription dans une autre formation que la licence. «&nbsp;Non
retrouvé&nbsp;» désigne un étudiant absent des fichiers d'inscription&nbsp;: la source parle de «&nbsp;sortie de
l'enseignement supérieur&nbsp;»&nbsp;; en général, ils ne sont plus étudiants, mais une faible part peut être inscrite à l'étranger ou dans une formation que ces fichiers ne
suivent pas. L'origine sociale est une catégorie statistique, construite par le service statistique du ministère à
partir de la profession du parent référent&nbsp;; elle ne porte aucun jugement sur les personnes. Le SIES la regroupe en
quatre classes, dont il ne nomme que les principales catégories&nbsp;: très favorisée (cadres, enseignants…), favorisée
(professions intermédiaires), assez défavorisée (employés…), défavorisée (ouvriers…). «&nbsp;Défavorisée&nbsp;» ne se lit
donc pas «&nbsp;enfants d'ouvriers&nbsp;».

<div class="fiche__prof">

**Durée indicative**&nbsp;: 20 à 30&nbsp;minutes pour les questions 1 à 5, selon les acquis des élèves&nbsp;; la
question 6 est un prolongement. **Support**&nbsp;: la figure ci-dessous, construite pour cette activité à partir des
tableaux du SIES.

</div>

{{< figure-svg fichier="parcours-licence-devenir" alt="Cinq barres horizontales empilées à 100 %, une par origine sociale puis l'ensemble : part des étudiants passés en deuxième année, recommençant une première année, réorientés hors de la licence ou non retrouvés dans les fichiers d'inscription. Les valeurs sont dans le tableau qui suit la figure." >}}Source&nbsp;: MESRE-SIES, {{< licence-val "note" >}}. [Agrandir la figure](/img/parcours-licence-devenir.png){{< /figure-svg >}}

{{< licence-tableau >}}

**Fiche élève**

1. Relevez la part des étudiants passés en deuxième année pour l'origine très favorisée et pour l'origine défavorisée. Quel est l'écart en points&nbsp;?
2. Relevez la part des étudiants réorientés hors de la licence dans chacune des quatre origines. Que remarquez-vous&nbsp;?
3. Pour chacune des deux origines extrêmes, calculez la part des étudiants non passés en deuxième année (100 moins la part des étudiants passés). Parmi ces étudiants, quelle proportion n'est plus retrouvée dans les fichiers d'inscription&nbsp;? *Aide&nbsp;: part des non retrouvés ÷ part des non-passés × 100.*
4. Calculez l'écart entre les deux origines pour la part des étudiants non retrouvés, d'abord sur tous les inscrits (figure), puis parmi les seuls étudiants non passés (question 3). Pour chacun des deux calculs, précisez quelle population sert de dénominateur.
5. Parmi les facteurs d'inégalités de réussite scolaire, le programme cite le rôle de l'École, le capital culturel et les investissements familiaux, les stratégies des ménages. Proposez un mécanisme par lequel l'un d'eux pourrait jouer sur le fait de recommencer la première année, de se réorienter ou de ne plus être retrouvé dans les fichiers d'inscription. Quelle donnée, autre que le niveau scolaire à l'entrée que nomme la note de la figure, faudrait-il pour le vérifier&nbsp;?
6. *Prolongement, chapitre sur la justice sociale.* La figure décrit des parcours plus ou moins fréquents selon l'origine sociale. En quoi ces écarts peuvent-ils éclairer la question de l'égalité des chances&nbsp;? Permettent-ils de conclure sur l'égalité des droits ou sur l'égalité des situations&nbsp;? Justifiez.

<details class="repli fiche__corrige"><summary>Corrigé pour l'enseignant</summary>

Pour les questions d'interprétation, tenir pour juste toute réponse qui sépare ce que les données établissent, ce qui reste plausible sans être démontré et ce que les documents contredisent.

1. {{< licence-val "tf_passage" >}}&nbsp;% et {{< licence-val "d_passage" >}}&nbsp;%&nbsp;: un écart de {{< licence-val "ecart_passage" >}}&nbsp;points.
2. {{< licence-val "tf_reorientation" >}}&nbsp;%, {{< licence-val "f_reorientation" >}}&nbsp;%, {{< licence-val "ad_reorientation" >}}&nbsp;% et {{< licence-val "d_reorientation" >}}&nbsp;%&nbsp;: sur tous les inscrits, presque le même taux d'une origine à l'autre, alors que les trois autres devenirs s'écartent (parmi les seuls non-passés, la réorientation diffère selon l'origine&nbsp;: voir le corrigé 4). À préciser aux élèves&nbsp;: il s'agit des départs vers une autre formation que la licence. Un étudiant qui recommence une première année dans une autre discipline ou un autre établissement est compté avec les redoublants&nbsp;; c'est le cas de {{< licence-val "tf_redoublement_autre" >}}&nbsp;% des inscrits d'origine très favorisée et de {{< licence-val "d_redoublement_autre" >}}&nbsp;% de ceux d'origine défavorisée.
3. Non passés&nbsp;: {{< licence-val "tf_non_passage" >}}&nbsp;% et {{< licence-val "d_non_passage" >}}&nbsp;% des inscrits. Non retrouvés parmi eux&nbsp;: {{< licence-val "tf_sortie" >}}&nbsp;÷&nbsp;{{< licence-val "tf_non_passage" >}}, soit {{< licence-val "tf_sortie_np" >}}&nbsp;%&nbsp;; {{< licence-val "d_sortie" >}}&nbsp;÷&nbsp;{{< licence-val "d_non_passage" >}}, soit {{< licence-val "d_sortie_np" >}}&nbsp;%.
4. Sur tous les inscrits de chaque origine (premier dénominateur), l'écart est de {{< licence-val "ecart_sortie" >}}&nbsp;points ({{< licence-val "tf_sortie" >}}&nbsp;% et {{< licence-val "d_sortie" >}}&nbsp;%). Parmi les seuls étudiants non passés, les deux proportions sont proches&nbsp;: {{< licence-val "ecart_sortie_np" >}}&nbsp;point d'écart avec les valeurs arrondies de la question 3, {{< licence-val "ecart_sortie_np_decimales" >}}&nbsp;point pour l'élève qui garde ses décimales jusqu'au bout&nbsp;; les deux démarches sont justes. Le dénominateur a changé&nbsp;: on rapporte les étudiants non retrouvés aux seuls non-passés de chaque origine. L'écart observé sur tous les inscrits correspond donc surtout à la différence de fréquence du non-passage. C'est une décomposition arithmétique (la part des non retrouvés parmi tous les inscrits est le produit de la part des non-passés et de la proportion de non retrouvés parmi eux), non une explication&nbsp;: les deux groupes de non-passés ne sont pas nécessairement comparables, et le tableau relève une seule situation à la rentrée suivante, non un échec suivi d'une réaction. Pour aller plus loin&nbsp;: parmi ces étudiants, l'inscription dans une autre formation que la licence est plus fréquente pour l'origine très favorisée ({{< licence-val "tf_reorientation_np" >}}&nbsp;% contre {{< licence-val "d_reorientation_np" >}}&nbsp;%), la réinscription en première année pour l'origine défavorisée ({{< licence-val "d_redoublement_np" >}}&nbsp;% contre {{< licence-val "tf_redoublement_np" >}}&nbsp;%). Le tableau ne dit pas si ces parcours répondent à une erreur d'orientation, à une contrainte ou à un choix. Ces constats se retrouvent sur les {{< licence-val "nb_cohortes_lettres" >}} cohortes comparables, entrées de {{< licence-val "cohortes_lib" >}}.
5. Plusieurs réponses sont recevables, à titre d'hypothèses&nbsp;: être plus ou moins accompagné en première année selon l'établissement (rôle de l'École), arriver avec des résultats scolaires que les ressources culturelles de la famille ont aidé à construire, ou connaître les formations vers lesquelles se réorienter (capital culturel), pouvoir financer une année de plus (investissements familiaux), choisir une filière en anticipant ses débouchés (stratégies des ménages). La figure ne permet d'en vérifier aucune. La même source montre de forts écarts de passage selon la mention au baccalauréat, {{< licence-val "mention_tb_passage" >}}&nbsp;% pour la mention très bien contre {{< licence-val "mention_p2_passage" >}}&nbsp;% après une admission au second groupe d'épreuves, mais elle ne croise pas la mention et l'origine sociale&nbsp;: ces tableaux ne permettent ni d'isoler l'effet propre de chaque caractéristique, ni de comparer leur poids. On décrit donc une association avec l'origine sociale, sans lui attribuer une cause. Le SIES a fait ce croisement pour une autre cohorte, les néo-bacheliers entrés en licence en 2019 (Note d'information n°&nbsp;26.06, juillet 2026), sur leurs trajectoires de quatre ans et, en annexe, sur le passage en deuxième année en un an, avec des effets très proches dans les deux modèles&nbsp;: «&nbsp;À caractéristiques égales, la corrélation entre origine sociale et réussite en licence est faible&nbsp;». Ce résultat ne dit pas que l'origine sociale ne compte pas&nbsp;: parmi les caractéristiques tenues égales, la série du baccalauréat diffère elle-même fortement selon l'origine (activité précédente). Pour la cohorte de la figure, il faudrait ce même croisement, que la note de la figure nomme déjà, et, en outre, les motifs des décisions et un suivi au-delà d'un an&nbsp;: un étudiant non retrouvé peut revenir. La même source publie aussi le devenir selon le statut de boursier sur critères sociaux (feuille «&nbsp;Devenir cohorte {{< licence-val "cohorte" >}} - BCS&nbsp;»)&nbsp;: une piste pour discuter l'hypothèse financière, non une vérification, car cette comparaison ne tient pas compte du parcours scolaire.
6. La figure décrit des fréquences de parcours différentes selon l'origine sociale, parmi des étudiants déjà entrés en licence. Elle permet d'interroger l'égalité des chances, que la ressource d'accompagnement du programme définit comme l'indépendance entre la situation sociale acquise et la situation sociale héritée, sans identifier les causes des écarts. Comparer des étudiants de même préparation scolaire apporte un éclairage de plus (c'est ce que fait, pour une autre cohorte, la note du SIES citée au corrigé 5), mais cette préparation peut elle-même porter la trace d'inégalités antérieures. La figure ne renseigne ni les règles d'inscription, donc l'égalité des droits, ni la répartition des ressources et des positions sociales, donc l'égalité des situations. Un élève qui voit dans ces écarts un indice d'inégalité des chances, en notant que ces étudiants sont déjà entrés en licence et que les causes ne sont pas identifiées, répond juste.

</details>

<div class="fiche__prof">

**Données**&nbsp;: [parcours_licence.csv](/parcours_licence.csv), une ligne par cohorte, origine et devenir.

</div>

</section>

### Méthode et sources {#methode}

**Après le bac.** La figure reprend le tableau 13.03 de *L'état de l'Enseignement supérieur, de la Recherche et de
l'Innovation en France* {{< acces-val "edition" >}} (MESRE-SIES)&nbsp;: nouveaux bacheliers {{< acces-val "annee" >}}
inscrits dans les différentes filières selon l'origine sociale, France métropolitaine et DROM. Les six catégories sont
celles de la source, dans son ordre&nbsp;; les {{< acces-val "origine_non_renseignee" >}}&nbsp;% d'inscrits dont
l'origine n'est pas renseignée ne sont pas répartis par la source et ne figurent pas&nbsp;; le tableau 13.01, qui donne la
filière de tous les inscrits, montre qu'ils sont surtout en STS (calcul de cette page). Les rapports et les écarts sont
un calcul de cette page. L'édition {{< acces-val "edition_temoin" >}}, qui porte sur les bacheliers
{{< acces-val "annee_temoin" >}}, sert de témoin&nbsp;; la série du baccalauréat des inscrits de chaque filière (tableau 09.03) et l'origine sociale des
bacheliers de chaque série (tableau 09.04) viennent de la fiche 09 de l'édition {{< acces-val "edition" >}}&nbsp;; aucun de ces
tableaux ne croise filière, série et origine. L'année retenue est celle de la cohorte de l'activité sur la
licence. Pages consultées le {{< acces-val "telecharge_le" >}}.

**Licence.** La figure est construite pour cette page à partir des tableaux nationaux
qui accompagnent la {{< licence-val "note" >}} du SIES, «&nbsp;Parcours et réussite en licence&nbsp;» (feuille
«&nbsp;Devenir cohorte {{< licence-val "cohorte" >}}&nbsp;»&nbsp;; {{< licence-val "inscrits" >}} néo-bacheliers,
universités et établissements assimilés, France entière). L'origine sociale est celle du parent référent, que le SIES
regroupe en quatre classes&nbsp;: très favorisée (cadres, enseignants…), favorisée (professions intermédiaires), assez
défavorisée (employés…), défavorisée (ouvriers…), points de suspension de la source&nbsp;; les {{< licence-val "non_reponse_part" >}}&nbsp;% d'étudiants
dont l'origine n'est pas renseignée n'ont pas de barre distincte et restent compris dans l'ensemble. Les quatre
devenirs laissent {{< licence-val "residu" >}}&nbsp;étudiants hors compte&nbsp;; les barres reprennent les taux publiés,
arrondis au dixième, dont la somme peut différer légèrement de 100&nbsp;%. Les parts
calculées parmi les étudiants non passés sont un calcul de cette page, non une publication du SIES&nbsp;: le corrigé
les calcule sur les taux arrondis de la figure, comme l'élève&nbsp;; le fichier de données, sur les effectifs. {{< licence-val "Nb_cohortes_lettres" >}}
cohortes seulement sont comparables&nbsp;: avant celle de {{< licence-val "premiere_cohorte" >}}, le tableau ne suivait pas les réorientations hors de
l'université. Tableurs téléchargés le {{< licence-val "telecharge_le" >}}&nbsp;; les données publiques du ministère sont mises à
disposition sous Licence Ouverte. Les extraits du programme viennent de son texte officiel, l'annexe «&nbsp;Programme de sciences économiques
et sociales de terminale générale&nbsp;» de l'arrêté du 19&nbsp;juillet&nbsp;2019 (Bulletin officiel spécial n°&nbsp;8 du 25&nbsp;juillet&nbsp;2019),
diffusée par Éduscol parmi les programmes en vigueur&nbsp;; la définition de l'égalité des chances vient de la ressource
d'accompagnement d'Éduscol sur la justice sociale (août 2020), celle de la démocratisation de sa ressource sur l'École
(décembre 2020). La Note d'information n°&nbsp;26.06 du SIES, citée au corrigé&nbsp;5 de la seconde activité, suit pendant quatre ans
les néo-bacheliers entrés en licence en 2019&nbsp;; son annexe&nbsp;4 porte sur le passage en deuxième année en un an. Les chiffres, les définitions et les extraits du programme de cette page ont été relus à leur
source&nbsp;; les activités n'ont pas été relues par un enseignant de sciences économiques et sociales.

{{< exemplaire slug="la-societe-du-premier-coup" lien="/ressources-offertes/premier-coup-enseignants/"
    surtitre="Pour les enseignants de SES" >}}
*La Société du premier coup* propose un cadre pour penser les conséquences d'une erreur d'orientation selon les
ressources dont on dispose. Ce cadre est présenté par l'auteur comme une hypothèse réfutable. Les activités ci-dessus
décrivent des inscriptions et des parcours&nbsp;; elles ne le mettent pas à l'épreuve.

Les enseignants qui souhaitent prendre connaissance de cet essai peuvent disposer d'un exemplaire numérique de
consultation, dans la limite des exemplaires disponibles. Il est proposé sans contrepartie&nbsp;: aucune recension,
aucune recommandation aux élèves ni aucun usage en classe n'est demandé, sous réserve des règles applicables dans
votre établissement. Un compte Amazon.fr est nécessaire.
{{< /exemplaire >}}

<script src="/js/fiche-imprimer.js" defer></script>
