---
title: "Que peut décider la France dans l'Union européenne ?"
description: "Ce que la France décide seule, ce qu'elle décide avec les autres États et ce qu'elle peut empêcher : le traité sur l'Union européenne et le TFUE cités mot pour mot, la règle de vote au Conseil, les votes publics de la France du {ue.debut} au {ue.fin} ({ue.fr_c} contre, {ue.fr_a} abstentions), chacun relié au résultat publié par le Conseil et à l'acte paru au Journal officiel, et la transposition des directives au {ue.tr_date}. Données ouvertes."
chapo: "Ce que les traités n'ont pas attribué à l'Union reste aux États : la France y décide seule, en respectant les règles communes. Là où l'Union est compétente, la Commission propose et la France vote avec les autres gouvernements au Conseil : à la majorité qualifiée, elle peut être mise en minorité ; à l'unanimité, son seul vote contre peut bloquer. Sur les votes publics du Conseil sur des actes législatifs, du {ue.debut} au {ue.fin}, la France a voté contre {ue.fr_contre} et s'est abstenue {ue.fr_abst}. Ces votes disent sa position au dernier moment, non ce qu'elle a obtenu dans la négociation qui les précède."
date: 2026-10-06
lastmod: 2026-10-12
donnees: [promesses_europe]
og_title: "Que peut décider la France dans l'Union européenne ? — compétences, règles de vote et votes de la France au Conseil — S. Lalut"
og_image: "images/og-europe-promesse.jpg"
og_image_alt: "Carte de partage : « La France au Conseil de l'UE » — nombre de votes contre et d'abstentions des États membres dans les votes publics du Conseil sur des actes législatifs ; la France, en bleu, est en bas de la liste."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_europe"
  nom: "Compétences et règles de vote de l'Union européenne, votes publics des États membres au Conseil (2009-2026) et transposition des directives par la France"
  description: "Typologie des compétences du TFUE (art. 2 à 6, texte consolidé de 2016) ; inventaire des bases juridiques de la procédure législative ordinaire et de l'unanimité au Conseil, contrôlé contre la liste du Secrétariat général du Conseil ; votes contre, abstentions et non-participations de chaque État membre dans les votes publics du Conseil sur des actes législatifs, du {ue.debut} au {ue.fin}, contrôlés contre le jeu SWP / GESIS (doi 10.7802/2560) jusqu'au {ue.fin_temoin} ; décompte, note du Conseil et acte publié des cinq actes où la France n'a pas voté pour ; indicateurs de transposition de la France au {ue.tr_date} (Commission)."
  couverture_temporelle: "2009/2026"
  couverture_spatiale: "Union européenne"
  variables:
    - {nom: "Votes des États membres au Conseil : contre, abstention, ne participe pas", unite: "votes publics"}
    - {nom: "Décompte au Conseil des actes où la France n'a pas voté pour : pour, contre, abstention, ne participe pas", unite: "États membres"}
    - {nom: "Bases juridiques du TFUE selon la règle de décision", unite: "paragraphes du traité"}
    - {nom: "Déficits de transposition et de conformité", unite: "% des directives du marché unique"}
  sources:
    - "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12016E/TXT"
    - "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12016M/TXT"
    - "https://www.consilium.europa.eu/en/general-secretariat/corporate-policies/transparency/voting-results/"
    - "https://doi.org/10.7802/2560"
    - "https://single-market-scoreboard.ec.europa.eu/enforcement-tools/transposition_en"
  mots: ["Union européenne", "Conseil de l'Union européenne", "majorité qualifiée", "unanimité", "compétences de l'Union", "principe d'attribution", "TFUE", "transposition", "promesses"]
  fichiers: ["promesses_europe.csv", "promesses_europe.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "La France peut-elle bloquer une loi européenne ?"
    answer: "Cela dépend de la règle de vote que le traité fixe pour la matière. À la majorité qualifiée, la règle la plus fréquente, aucun État ne bloque seul : en règle générale, une minorité de blocage doit réunir au moins quatre membres du Conseil, et quand certains États ne prennent pas part au vote, elle se calcule sur les seuls États participants (article 238, paragraphe 3, du TFUE). Là où le traité exige l'unanimité, par exemple pour la fiscalité indirecte (article 113 du TFUE) ou le cadre financier pluriannuel (article 312), un seul vote contre suffit à empêcher l'adoption ; une abstention, non."
  - question: "Combien de fois la France a-t-elle voté contre une loi européenne ?"
    answer: "Sur les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {ue.debut} au {ue.fin}, la France a voté contre {ue.fr_contre} et s'est abstenue {ue.fr_abst}. Les textes contre lesquels elle a voté ont été adoptés à la majorité qualifiée. Sur le même relevé, l'Allemagne a voté contre {ue.de_c} fois et les Pays-Bas {ue.nl_c} fois ; ces comptes bruts ne mesurent pas l'influence d'un État."
  - question: "La France transpose-t-elle les directives européennes à temps ?"
    answer: "Selon le tableau d'affichage du marché unique de la Commission, au {ue.tr_date}, {ue.tr_def} % des directives du marché unique dont l'échéance était passée n'étaient pas transposées en France, comme en moyenne dans l'Union. La Commission vise 0,5 %. Les directives qu'elle tient pour mal transposées, d'après ses procédures d'infraction, représentaient {ue.tr_conf} % pour la France. La moyenne de l'Union était de {ue.tr_conf_ue} %. Ces valeurs viennent d'une seule édition du tableau d'affichage."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocoles de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-12"
  bloc: "promesses"
  livres: ["un-president-peut-il-tenir-ses-promesses"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 70
  prolongement: true
  nature: "Traités (EUR-Lex), votes du Conseil de l'UE contrôlés par un second jeu, résultats et actes relus à la source, Commission ; données ouvertes"
onglet:  # panneau « Prolongements » de la barre du dossier (partials/barre-bloc.html)
  long: "Que peut décider la France dans l'Union européenne ?"
  court: "Europe"
  role: "seule, à plusieurs, malgré elle"
---

{{< reutiliser-ancre >}}

Le chiffre surprend&nbsp;: sur l'ensemble des votes publics relevés, la France ne s'est presque jamais opposée à une loi européenne au Conseil. Il se prête à trois lectures. Elle obtiendrait l'essentiel de ce qu'elle demande avant le vote&nbsp;; elle contribuerait à des compromis sans tout obtenir&nbsp;; ou elle se rallierait à des textes qu'elle aurait voulus autres. Le décompte des votes ne départage pas ces trois histoires, et cette page ne prétend pas le faire.

Le pouvoir d'un État dans l'Union ne se mesure pas au nombre de fois où il dit non. Il dépend de la matière, qui fixe qui décide&nbsp;; de la règle de vote, qui fixe ce qu'un seul État peut empêcher&nbsp;; et de la négociation, que le vote final ne montre pas. La page suit cette frontière&nbsp;: ce que la France décide seule, ce qu'elle décide avec les autres, ce qu'elle peut bloquer ou doit accepter, ce qu'elle fait du texte adopté. Elle s'appuie sur le texte des traités en vigueur et sur les votes que publie le Conseil.

## Que peut décider la France seule&nbsp;? {#decider-seule}

Ce que les traités n'ont pas confié à l'Union reste aux États&nbsp;: c'est le principe d'attribution (traité sur l'Union européenne, ou TUE, art.&nbsp;4 et 5). Le traité nomme lui-même une matière qui reste nationale&nbsp;: «&nbsp;{{< ue-val "cit_tue4_2" >}}&nbsp;» (TUE, art.&nbsp;4, §&nbsp;2). Dans d'autres domaines, la loi reste nationale et l'Union ne fait qu'appuyer, coordonner ou compléter l'action des États, sans harmoniser leurs législations&nbsp;: {{< ue-val "appui" >}} (traité sur le fonctionnement de l'Union européenne, ou TFUE, art.&nbsp;2, §&nbsp;5, et art.&nbsp;6).

Détenir une compétence ne dispense pas de respecter les règles communes en l'exerçant. Chaque État doit assurer l'exécution des obligations nées des traités (coopération loyale, TUE, art.&nbsp;4, §&nbsp;3) et ne peut pas discriminer en raison de la nationalité (TFUE, art.&nbsp;18)&nbsp;; une loi française qui touche aux échanges peut en outre rencontrer les libertés de circulation du marché intérieur. La France décide seule dans ces matières&nbsp;; elle n'y décide pas hors du droit de l'Union. Un même secteur peut d'ailleurs relever de plusieurs compétences&nbsp;: la compétence d'appui ne permet pas, sur ce seul fondement, d'harmoniser les lois nationales, mais en santé, par exemple, le traité permet aussi à l'Union de fixer des normes de qualité et de sécurité pour les organes, le sang, les médicaments et les dispositifs médicaux (TFUE, art.&nbsp;168, §&nbsp;4).

<details class="repli"><summary>Les articles cités, mot pour mot</summary>

Le TUE pose la règle&nbsp;: «&nbsp;{{< ue-val "cit_tue4_1" >}}&nbsp;» (art.&nbsp;4, §&nbsp;1). Le principe d'attribution&nbsp;: «&nbsp;{{< ue-val "cit_tue5_2" >}}&nbsp;» (art.&nbsp;5, §&nbsp;2). Dans les domaines d'appui, de coordination et de complément, les actes de l'Union «&nbsp;{{< ue-val "cit_2_5b" >}}&nbsp;» (TFUE, art.&nbsp;2, §&nbsp;5). La coopération loyale&nbsp;: «&nbsp;{{< ue-val "cit_tue4_3" >}}&nbsp;» (TUE, art.&nbsp;4, §&nbsp;3). La non-discrimination&nbsp;: «&nbsp;{{< ue-val "cit_18" >}}&nbsp;» (TFUE, art.&nbsp;18).

Les deux traités sont cités dans leur version consolidée de 2016, c'est-à-dire le texte en vigueur, modifications successives intégrées, publié au Journal officiel de l'Union, et sans la jurisprudence de la Cour qui les interprète.

</details>

**«&nbsp;La France décide seule&nbsp;» ne veut pas dire «&nbsp;le président décide seul&nbsp;».** Une décision nationale peut demander une loi, un décret ou l'intervention d'autres autorités françaises&nbsp;: la page [Que peut décider le président de la République seul&nbsp;?](/pouvoirs-du-president-de-la-republique/#decider-seul) les distingue.

## Dans quelles matières l'Union décide-t-elle&nbsp;? {#competences}

Le TFUE range les compétences attribuées à l'Union en trois catégories (art.&nbsp;2 à 6).

- **Compétence exclusive** (art.&nbsp;3)&nbsp;: seule l'Union légifère, les États ne le pouvant que si elle les y habilite ou pour appliquer ses actes. Elle couvre {{< ue-val "exclusives" >}}, ainsi que certains accords internationaux.
- **Compétence partagée** (art.&nbsp;4)&nbsp;: l'Union et les États peuvent légiférer, les États tant que l'Union n'a pas exercé sa compétence. Elle couvre notamment le marché intérieur, l'agriculture et la pêche, l'environnement, les transports et l'énergie.
- **Appui, coordination, complément** (art.&nbsp;6)&nbsp;: la santé humaine, l'industrie, la culture, l'éducation et les autres domaines nommés dans la section précédente, où la loi reste nationale.

<details class="repli"><summary>Ce que disent les articles 2 à 6 du TFUE</summary>

L'article&nbsp;2, §&nbsp;1, sur la compétence exclusive&nbsp;: «&nbsp;{{< ue-val "cit_2_1" >}}&nbsp;» L'article&nbsp;2, §&nbsp;2, sur la compétence partagée&nbsp;: «&nbsp;{{< ue-val "cit_2_2" >}}&nbsp;» La liste des compétences partagées n'est pas fermée&nbsp;: est partagée toute compétence attribuée qui n'est ni exclusive ni d'appui (art.&nbsp;4, §&nbsp;1). Pour la recherche, le développement technologique, l'espace, la coopération au développement et l'aide humanitaire, l'action de l'Union ne peut pas empêcher les États d'exercer leur propre compétence (art.&nbsp;4, §&nbsp;3 et 4). L'Union dispose aussi d'une compétence exclusive pour certains accords internationaux (art.&nbsp;3, §&nbsp;2).

Les États coordonnent en outre leurs politiques économiques et de l'emploi selon les modalités du traité, et l'Union peut prendre des initiatives pour coordonner leurs politiques sociales (art.&nbsp;5)&nbsp;; la politique étrangère et de sécurité commune suit les règles propres du TUE (art.&nbsp;2, §&nbsp;4).

</details>

{{< ue-tableau "competences" "Les domaines, cités dans le texte du traité" >}}

## Qui met un texte à l'agenda, qui le propose, qui l'adopte&nbsp;? {#initiative}

Là où l'Union est compétente, trois pouvoirs se distinguent.

**Proposer** revient en règle à la Commission (TUE, art.&nbsp;17, §&nbsp;2&nbsp;; TFUE, art.&nbsp;294, §&nbsp;2). Un gouvernement ne dépose donc pas lui-même un projet de loi européenne.

**Mettre un sujet à l'agenda** lui reste ouvert, avec d'autres. Le Conseil peut demander à la Commission de lui soumettre des propositions, et, si elle ne le fait pas, elle doit lui en donner les raisons (TFUE, art.&nbsp;241). Dans la coopération judiciaire en matière pénale et la coopération policière, les actes peuvent aussi être adoptés «&nbsp;{{< ue-val "cit_76" >}}&nbsp;» (art.&nbsp;76).

**Adopter** revient, dans la procédure législative ordinaire, au Parlement européen et au Conseil de l'Union européenne. Deux institutions portent un nom voisin&nbsp;: au Conseil de l'Union européenne siège un ministre de chaque État, selon le sujet traité (agriculture, finances, environnement…)&nbsp;; au Conseil européen siègent les chefs d'État ou de gouvernement, qui fixent les orientations générales et ne votent pas les lois (TUE, art.&nbsp;15, §&nbsp;1&nbsp;: «&nbsp;{{< ue-val "cit_tue15" >}}&nbsp;»). Les votes de cette page sont ceux du Conseil de l'Union européenne.

**Ce que la proposition change pour la France.** Une fois la proposition déposée, le Conseil ne peut l'amender qu'à l'unanimité, sauf dans les cas que le traité énumère (conciliation avec le Parlement européen, procédures budgétaires et financières)&nbsp;; la Commission, elle, peut modifier sa proposition tant que le Conseil n'a pas statué (TFUE, art.&nbsp;293). Hors ces exceptions, la règle joue dans les deux sens&nbsp;: les autres États ne peuvent pas réécrire la proposition au Conseil sans l'accord de la France, et une majorité d'États, la France comprise, ne suffit pas non plus à la réécrire.

<details class="repli"><summary>Les articles cités, mot pour mot</summary>

L'initiative de la Commission&nbsp;: «&nbsp;{{< ue-val "cit_17_2" >}}&nbsp;» (TUE, art.&nbsp;17, §&nbsp;2)&nbsp;; l'article qui décrit la procédure législative ordinaire s'ouvre ainsi&nbsp;: «&nbsp;{{< ue-val "cit_294_2" >}}&nbsp;» (TFUE, art.&nbsp;294, §&nbsp;2). La demande du Conseil, et ce qui suit un refus&nbsp;: «&nbsp;{{< ue-val "cit_241" >}}&nbsp;» (TFUE, art.&nbsp;241). Le Conseil de l'Union européenne réunit un représentant de chaque État membre au niveau ministériel (TUE, art.&nbsp;16, §&nbsp;2).

L'article&nbsp;293 du TFUE, premier paragraphe&nbsp;: lorsque le Conseil statue sur proposition de la Commission, «&nbsp;{{< ue-val "cit_293_1" >}}&nbsp;». Deuxième paragraphe&nbsp;: «&nbsp;{{< ue-val "cit_293_2" >}}&nbsp;».

</details>

## Selon quelle règle le Conseil décide-t-il&nbsp;? {#regles-de-vote}

La règle dépend de la base juridique, l'article du traité sur lequel l'acte est fondé. Le cas général est la **majorité qualifiée**, définie comme «&nbsp;{{< ue-val "cit_16_4" >}}&nbsp;» (TUE, art.&nbsp;16, §&nbsp;4)&nbsp;; quand le Conseil ne statue pas sur proposition de la Commission, il faut «&nbsp;{{< ue-val "cit_238_2" >}}&nbsp;» (TFUE, art.&nbsp;238, §&nbsp;2). Le même article&nbsp;16 ajoute&nbsp;: «&nbsp;{{< ue-val "cit_tue16" >}}&nbsp;». C'est la règle générale&nbsp;; quand tous les membres du Conseil ne prennent pas part au vote, le traité calcule la majorité qualifiée et la minorité de blocage sur les seuls États participants (TFUE, art.&nbsp;238, §&nbsp;3). Aucun État ne forme donc seul une minorité de blocage, et la France peut être mise en minorité.

Le relevé des votes, plus bas, traverse trois régimes de la majorité qualifiée&nbsp;: les voix pondérées, puis la double majorité avec la faculté de demander l'ancien calcul, puis la double majorité seule. Les voix des États ont été pondérées jusqu'au {{< ue-val "dm_fin_ancien" >}}. La double majorité s'applique depuis le {{< ue-val "dm_debut" >}}&nbsp;; jusqu'au {{< ue-val "dm_option_fin" >}}, un membre du Conseil pouvait encore demander l'ancien calcul (protocole n°&nbsp;36 sur les dispositions transitoires).

Dans d'autres matières, le Conseil statue à l'**unanimité**&nbsp;: la fiscalité indirecte, les ressources propres de l'Union ou le cadre financier pluriannuel, par exemple (tableau ci-dessous).

**Voter contre ou s'abstenir.** À la majorité qualifiée, voter contre et s'abstenir empêchent tous deux que la voix de l'État contribue à la majorité favorable. Mais les deux positions ne disent pas la même chose politiquement. À l'unanimité, une abstention ne bloque pas&nbsp;: un vote contre peut bloquer. Le traité l'écrit ainsi&nbsp;: «&nbsp;{{< ue-val "cit_238_4" >}}&nbsp;» (TFUE, art.&nbsp;238, §&nbsp;4).

{{< ue-tableau "instruments" "La règle, matière par matière, pour les instruments que nomment le livre et les programmes" >}}

<details class="repli"><summary>Combien de bases juridiques, et comment elles ont été comptées</summary>

Le relevé du TFUE compte {{< ue-val "n_plo" >}}&nbsp;bases de la procédure législative ordinaire, dans {{< ue-val "n_plo_art" >}}&nbsp;articles, et {{< ue-val "n_una" >}}&nbsp;bases où le Conseil statue à l'unanimité, dans {{< ue-val "n_una_art" >}}&nbsp;articles&nbsp;; ces dernières fondent des actes législatifs et non législatifs. Ces nombres ne mesurent ni le poids des matières, ni la fréquence des actes adoptés sur chacune de ces bases.

Le texte est la version consolidée du TFUE publiée au Journal officiel de l'Union le 7&nbsp;juin 2016. Chaque domaine des articles&nbsp;3, 4 et 6 est cité mot pour mot, et la complétude de chaque liste est relue dans le texte. Ces {{< ue-val "n_plo" >}}&nbsp;bases et les {{< ue-val "n_cond_min" >}}&nbsp;bases conditionnelles ont été comparées à la liste que publie le Secrétariat général du Conseil dans son guide de cette procédure (annexe&nbsp;III, {{< ue-val "n_temoin" >}}&nbsp;entrées)&nbsp;: les deux listes concordent exactement. Cette comparaison a fait apparaître des bases qui renvoient à la procédure sans la nommer (articles&nbsp;42, 62 et 177), lues et ajoutées. {{< ue-val "n_cond" >}}&nbsp;bases suivent une procédure qui dépend de la mesure (articles&nbsp;83, §&nbsp;2, et 136, §&nbsp;1). Les mentions qui ne fondent pas un acte (freins d'urgence, passerelles, articles qui décrivent la procédure) sont écartées, chacune avec son motif, dans le fichier de données.

La liste de l'unanimité repose sur le mot&nbsp;: une base qui y renverrait sans l'employer échapperait au relevé, et elle n'a pas de second producteur sur le même périmètre. Un inventaire universitaire de 2014 (S.&nbsp;Polidori, *Eurostudium3w*) compte {{< ue-val "polidori_tfue" >}}&nbsp;dispositions du TFUE à l'unanimité, Conseil européen compris&nbsp;; ce n'est pas la même unité, et il ne contrôle donc pas ce relevé.

</details>

## Comment la France vote-t-elle au Conseil&nbsp;? {#votes-au-conseil}

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}, la France a voté contre {{< ue-val "fr_contre" >}} et s'est abstenue {{< ue-val "fr_abst" >}}&nbsp;; elle a voté pour dans tous les autres cas.

</div>

Les {{< ue-val "n_actes" >}}&nbsp;textes ont tous été adoptés. Sur les {{< ue-val "fr_c_l" >}} contre lesquels elle a voté, la France a été mise en minorité&nbsp;: c'est la majorité qualifiée à l'œuvre. Sur les {{< ue-val "fr_a_l" >}} actes où elle s'est abstenue, la France n'a pas voté contre. Mais, à la majorité qualifiée, son abstention ne contribue pas à réunir la majorité favorable, pas davantage qu'un vote contre. Chaque ligne du tableau renvoie au résultat publié par le Conseil et à l'acte paru au Journal officiel, daté après le vote, le temps de la signature.

{{< ue-tableau "france" "Les actes où la France n'a pas voté pour" "ouvert" >}}

**Deux votes contre que le Conseil n'atteste pas.** Un second jeu de données, tiré des fichiers du Conseil par un institut allemand, la SWP, compte deux votes contre de la France de plus, datés du {{< ue-val "ecart_date" >}}, sans titre ni objet. Nous les avons cherchés dans les publications du Conseil&nbsp;: son récapitulatif des actes du mois ne mentionne ni réunion ni acte législatif ce jour-là, et sa recherche des votes n'en rend aucun entre le {{< ue-val "ecart_avant" >}} et le {{< ue-val "ecart_apres" >}}. Ces deux entrées ne sont donc pas comptées. Ne pas les avoir retrouvées ne prouve pas qu'aucun vote n'a eu lieu&nbsp;: ce qu'elles désignaient reste inconnu, et le détail de la recherche est dans le repli «&nbsp;Comment le relevé a été fait et contrôlé&nbsp;».

Un pays qui vote rarement contre n'est pas nécessairement un pays qui obtient davantage. Ces barres montrent des votes, pas des rapports de force.

{{< figure-svg fichier="europe-votes" alt="Barres horizontales, une par État membre, triées par total : votes contre en foncé, abstentions en clair, avec les deux nombres après chaque barre ; la France, en bleu, est en bas de la liste. Les valeurs sont dans le tableau sous la figure." >}}Votes contre et abstentions de chaque État membre dans les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}. Le Royaume-Uni n'y figure que jusqu'à son retrait, la Croatie depuis son adhésion en 2013, et le Danemark et l'Irlande ne participent pas à certains actes&nbsp;: ces comptes bruts ne constituent pas un classement d'influence.{{< /figure-svg >}}

{{< fig-actions id="votes" >}}

{{< ue-tableau "etats" "Les votes de chaque État membre en tableau" >}}

Sur le même relevé, l'Allemagne a voté contre {{< ue-val "de_c" >}}&nbsp;fois et s'est abstenue {{< ue-val "de_a" >}}&nbsp;fois. Les Pays-Bas ont voté contre {{< ue-val "nl_c" >}}&nbsp;fois, la Pologne {{< ue-val "pl_c" >}}&nbsp;fois. La Hongrie l'a fait {{< ue-val "hu_c" >}}&nbsp;fois.

**Ce que ces chiffres ne disent pas.** Ils décrivent la position formelle des États au vote final. Ils ne mesurent ni leur influence dans la négociation, ni ce qu'ils ont obtenu ou cédé, ni leur capacité générale à bloquer une décision. Le relevé ne couvre que les votes **publics** sur des actes **législatifs**&nbsp;: ni les actes non législatifs, ni la politique étrangère, ni les discussions qui précèdent le vote.

<details class="repli"><summary>Comment le relevé a été fait et contrôlé</summary>

**Le relevé.** Le Conseil a arrêté ses fichiers de données ouverts en mars 2025&nbsp;; ses résultats de vote ne sont plus publiés que par sa page de recherche, qui n'accepte pas les programmes. Le relevé a donc été fait dans un navigateur, le {{< ue-val "releve" >}}, page par page&nbsp;: {{< ue-val "entrees" >}}&nbsp;entrées, exactement le total que la page annonce&nbsp;; la recherche, filtrée tour à tour sur la France et sur l'Allemagne, rend les mêmes entrées. Parmi ces votes, {{< ue-val "qmv" >}} relevaient de la majorité qualifiée, {{< ue-val "una" >}} de l'unanimité et {{< ue-val "qmv_sp" >}} de la majorité qualifiée sans proposition de la Commission. Le Conseil affiche {{< ue-val "doublons" >}}&nbsp;entrées en double, identiques dans tous leurs champs&nbsp;: le nombre d'actes est compris entre {{< ue-val "entrees_min" >}} et {{< ue-val "entrees" >}}. Ces doublons sont des votes unanimes et ne changent aucun compte de votes contre ou d'abstentions.

**Le second jeu de données.** Le jeu constitué par l'Institut allemand pour les affaires internationales et de sécurité (SWP) à partir des données du Conseil, du {{< ue-val "debut" >}} au {{< ue-val "fin_temoin" >}}, a été rapproché du relevé acte par acte, puis État par État&nbsp;: les comptes de votes contre et d'abstentions de {{< ue-val "etats_identiques" >}}&nbsp;États sur {{< ue-val "etats_total" >}} sont identiques dans les deux sources, et les écarts des autres s'expliquent. Un acte du 28&nbsp;mars 2023 manque au jeu SWP, arrêté deux semaines plus tard. Deux entrées du jeu SWP sans titre et unanimes n'ont pas pu être corroborées&nbsp;; elles ne changent aucun compte de votes contre ou d'abstentions.

**Les deux votes contre du {{< ue-val "ecart_date" >}}.** Ils n'existent que dans le jeu SWP, sans titre ni objet, chacun avec la France seule contre. Ils portent des identifiants de procédure de vote des fichiers ouverts du Conseil, que celui-ci ne publie plus. Le récapitulatif mensuel des actes du Conseil pour mai 2021 (document ST&nbsp;8962/21, publié le 28&nbsp;juin 2021) ne mentionne aucune réunion du Conseil ce jour-là&nbsp;; il n'y porte qu'un acte, une décision de politique étrangère et de sécurité commune adoptée par procédure écrite, hors du champ des actes législatifs, et aucune procédure écrite législative dans le mois. La recherche des votes du Conseil, lue le 12&nbsp;octobre 2026, rend des votes le {{< ue-val "ecart_avant" >}}, puis le {{< ue-val "ecart_apres" >}}, et aucun entre les deux&nbsp;; le registre des documents du Conseil ne contient aucun résultat de vote la semaine du {{< ue-val "ecart_date" >}}, alors qu'il contient ceux de la semaine précédente. Faute d'avoir pu les corroborer, le compte publié ne les intègre pas. D'où viennent ces deux fiches, erreur de saisie ou vote jamais publié, aucune des pièces lues ne permet de le dire.

**Les cinq actes.** Pour chacun, la note «&nbsp;résultat de vote&nbsp;» du Conseil et l'acte publié au Journal officiel, en français et en anglais, ont été archivés le 12&nbsp;octobre 2026. Le décompte est lu dans l'annexe de la note et sur la page de recherche du Conseil&nbsp;; le script vérifie dans les pièces archivées la procédure, la date du vote et, dans l'acte, son numéro, sa date et la mention de la décision du Conseil à la date du vote. Les {{< ue-val "n_actes_temoin" >}}&nbsp;votes couverts par le jeu SWP, jusqu'au {{< ue-val "fin_temoin" >}}, y ont le même décompte, que le script recalcule depuis ce jeu&nbsp;; les {{< ue-val "n_actes_source" >}} suivants sont documentés à la source, sans second jeu&nbsp;: le script relit, État par État, la composition de chacun dans l'annexe archivée de la note du Conseil. {{< ue-val "n_ponderes_maj" >}} de ces votes, antérieurs au {{< ue-val "dm_debut" >}}, ont été comptés en voix pondérées.

**Ce que le producteur du second jeu écrivait déjà.** La SWP écrivait en décembre&nbsp;2021&nbsp;: «&nbsp;{{< ue-val "swp21_cit" >}}&nbsp;». Notre relevé compte, de 2010 à 2021, {{< ue-val "swp21_contre" >}}&nbsp;vote contre et {{< ue-val "swp21_abst" >}}&nbsp;abstentions de la France&nbsp;: le même compte, qui ne comprend donc pas les {{< ue-val "swp24_ecart" >}}&nbsp;votes contre du {{< ue-val "ecart_date" >}} que porte le jeu de données. En avril&nbsp;2024, le même institut écrit, pour 2010 à septembre&nbsp;2023&nbsp;: «&nbsp;{{< ue-val "swp24_cit" >}}&nbsp;». Notre relevé compte {{< ue-val "swp24_nonpour" >}}&nbsp;votes contre ou abstentions sur cette période. L'écart numérique est de {{< ue-val "swp24_ecart" >}}&nbsp;occurrences, comme les {{< ue-val "swp24_ecart" >}}&nbsp;fiches litigieuses du {{< ue-val "ecart_date" >}}. Faute de liste nominative des {{< ue-val "swp24_annonce" >}}&nbsp;votes retenus dans l'analyse de 2024, cette concordance ne permet pas d'établir qu'il s'agit des mêmes actes.

</details>

## Pourquoi un État peut-il voter oui à un texte qu'il voulait différent&nbsp;? {#voter-oui}

Le vote final n'enregistre que la dernière étape d'une séquence. **D'abord**, chaque gouvernement arrive avec une position&nbsp;: ce qu'il demande, ce qu'il refuse. **Ensuite**, le texte se négocie. La Commission peut modifier sa proposition tant que le Conseil n'a pas statué, le Parlement européen arrête ses propres positions et, du côté des gouvernements, «&nbsp;{{< ue-val "cit_16_7" >}}&nbsp;» (TUE, art.&nbsp;16, §&nbsp;7). **Puis** un texte final est mis aux voix, qui peut s'écarter de ce que chaque État demandait au départ. **Enfin**, chaque État vote pour, contre, s'abstient ou ne participe pas.

Un «&nbsp;oui&nbsp;» à cette dernière étape est compatible avec les trois histoires du début&nbsp;: l'État a obtenu l'essentiel de ce qu'il demandait, il a contribué à un compromis sans tout obtenir, ou il s'est rallié à un texte qu'il aurait voulu autre. Le décompte ne permet pas de les départager. Il faudrait, pour cela, des sources sur la négociation elle-même, acte par acte, que le relevé des votes ne contient pas. Le vote final est une observation, non l'historique des préférences et des concessions.

## La France transpose-t-elle les directives à temps&nbsp;? {#transposition}

Après le vote, la France doit appliquer ce qui a été adopté, qu'elle l'ait voté ou non. Pour une directive, le traité dit&nbsp;: «&nbsp;{{< ue-val "cit_288" >}}&nbsp;» (TFUE, art.&nbsp;288)&nbsp;; chaque directive fixe la date avant laquelle la transposer. La Commission mesure, deux fois par an, la part des directives du marché unique qui ne sont pas transposées à temps&nbsp;: c'est le déficit de transposition.

Au {{< ue-val "tr_date" >}}, ce déficit était de {{< ue-val "tr_def" >}}&nbsp;% en France, la même valeur que la moyenne de l'Union. Cela représente {{< ue-val "tr_retard" >}}&nbsp;directives sur {{< ue-val "tr_dues" >}}. La Commission compte aussi les directives qu'elle tient pour mal transposées, d'après ses procédures d'infraction&nbsp;: c'est le déficit de conformité, de {{< ue-val "tr_conf" >}}&nbsp;% pour la France. La moyenne de l'Union est de {{< ue-val "tr_conf_ue" >}}&nbsp;%, et une procédure engagée n'est pas un manquement constaté par la Cour. La Commission range la France parmi les {{< ue-val "tr_double" >}}&nbsp;États qui cumulent un déficit de transposition élevé et un déficit de conformité élevé.

**Ces valeurs viennent d'une seule édition du tableau d'affichage.** Elles ne disent pas si le retard de la France augmente ou diminue.

<details class="repli"><summary>Comment ces valeurs ont été relevées, et l'objectif fixé</summary>

La Commission ne publie ces valeurs que dans un tableau interactif, sans fichier&nbsp;: elles ont été relevées sur une capture archivée, et les moyennes de l'Union contrôlées par le texte de la Commission. Le Conseil européen avait fixé en 2007 un objectif de déficit de transposition de 1&nbsp;%. La Commission l'a ramené à 0,5&nbsp;% (Acte pour le marché unique de 2011, communication de mars 2023).

</details>

{{< ue-tableau "transposition" "Les indicateurs de transposition de la France" >}}

Un retard peut ouvrir une procédure en manquement&nbsp;: la Commission émet un avis motivé, puis peut saisir la Cour de justice (TFUE, art.&nbsp;258)&nbsp;; un autre État peut aussi la saisir (art.&nbsp;259). Lorsque l'État n'a pas communiqué ses mesures de transposition d'une directive adoptée selon une procédure législative, la Cour peut lui infliger une somme forfaitaire ou une astreinte dès qu'elle constate le manquement (art.&nbsp;260, §&nbsp;3).

## Avant d'évaluer une promesse européenne, que faut-il vérifier&nbsp;? {#avant-d-evaluer}

Une promesse de campagne qui touche à l'Europe se lit avec cinq questions, dans cet ordre.

1. **La matière a-t-elle été attribuée à l'Union&nbsp;?** Sinon, la France décide seule, dans le respect des règles communes&nbsp;; si la compétence est partagée, la marge dépend de ce que l'Union a déjà adopté.
2. **Qui doit proposer&nbsp;?** En règle la Commission&nbsp;: la France peut demander une proposition, par le Conseil ou avec d'autres États, non la déposer seule.
3. **Quelle règle de vote fixe la base juridique&nbsp;?** À la majorité qualifiée, la France peut être mise en minorité&nbsp;; à l'unanimité, son vote contre peut bloquer, son abstention non.
4. **Que devra faire la France après l'adoption&nbsp;?** Appliquer un règlement, transposer une directive avant la date fixée, sous le contrôle de la Commission et de la Cour.
5. **Que montrera le vote final&nbsp;?** La position de la France au dernier moment, non ce qu'elle a obtenu en chemin.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas si l'Union décide trop ou trop peu, ni si la France y pèse beaucoup ou peu&nbsp;: aucune des mesures présentées ne le mesure. Elle ne rapporte pas les votes contre et les abstentions au nombre de votes auxquels chaque État pouvait prendre part&nbsp;; une telle normalisation demanderait de construire ces dénominateurs, et ne dirait toujours rien de l'influence. Elle ne compte ni les actes de la Commission, ni les décisions de la Banque centrale européenne, ni les arrêts de la Cour de justice, ni les votes du Conseil sur des actes non législatifs, comme les décisions relatives à la signature d'un accord commercial&nbsp;: les décisions de janvier&nbsp;2026 sur la signature de l'accord entre l'Union et le Mercosur, adoptées par procédure écrite, sont hors du relevé, quel qu'ait été le vote de chaque État. Elle lit les traités en vigueur, sans jurisprudence. Les votes sont arrêtés au {{< ue-val "fin" >}}, la transposition au {{< ue-val "tr_date" >}}.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Changer les règles européennes" avis="non" >}}
Cette page trace la frontière entre ce que la France décide seule, ce qu'elle décide avec les autres États et ce qu'elle peut empêcher. Le livre suit deux préférences françaises jusqu'à la règle européenne, l'une adoptée, l'autre bloquée, et confronte les promesses de «&nbsp;changer l'Europe&nbsp;» à ce que le traité permet. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Traité sur l'Union européenne**, version consolidée, Journal officiel de l'Union européenne C&nbsp;202 du 7&nbsp;juin 2016 (EUR-Lex), art.&nbsp;4, 5, 15, 16 et 17.

**Traité sur le fonctionnement de l'Union européenne**, même Journal officiel, art.&nbsp;2 à 6, 18, 76, 238, 241, 258 à 260, 288, 293 et 294, ensemble du traité pour les bases juridiques&nbsp;; protocole n°&nbsp;36 sur les dispositions transitoires.

**Conseil de l'Union européenne**, recherche des résultats de vote sur les actes législatifs (relevé du {{< ue-val "releve" >}})&nbsp;; notes «&nbsp;résultat de vote&nbsp;» du registre public des documents, liées aux cinq actes du tableau&nbsp;; récapitulatif mensuel des actes du Conseil, mai 2021 (ST&nbsp;8962/21, 28&nbsp;juin 2021)&nbsp;; Secrétariat général du Conseil, *Guide to the ordinary legislative procedure*, 2010, annexe&nbsp;III (doi 10.2860/74684).

**Journal officiel de l'Union européenne** (EUR-Lex), les cinq actes du tableau, liés ligne par ligne.

**Ondarza, Nicolai von et Bochtler, Paul**, *Public Voting Data of the Council of the EU*, version 2.0.0, SWP, 2023, doi [10.7802/2560](https://doi.org/10.7802/2560), licence CC BY 4.0.

**Commission européenne**, tableau d'affichage du marché unique et de la compétitivité, transposition, édition arrêtée au {{< ue-val "tr_date" >}}.

Les chiffres, les contrôles et la figure sont produits par un script unique. Il relit le traité archivé, où chaque citation est retrouvée mot pour mot, le jeu SWP et les pièces archivées des cinq actes. Les comptes de votes par État, relevés dans le navigateur, et le décompte de chaque acte, lu dans l'annexe de la note du Conseil, sont transcrits dans le script, qui s'arrête si le recalcul depuis le jeu SWP les contredit sur la période commune&nbsp;; les votes postérieurs à mars 2023 n'ont pas de second jeu. Pour les deux votes contre du jeu SWP que le compte écarte, le script relit le récapitulatif archivé des actes du Conseil de mai 2021 et vérifie que le jeu SWP ne porte qu'eux entre les deux votes qui les encadrent dans la recherche du Conseil, transcrits. Les indicateurs de transposition sont transcrits d'une capture, et leurs moyennes de l'Union contrôlées par le texte de la Commission. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_europe.csv), en format long&nbsp;; [JSON](/promesses_europe.json), avec les bases juridiques, les écarts expliqués, les cinq actes et le compte rendu des contrôles. Une version antérieure de ce jeu est archivée sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_europe" jeu="promesses_europe" sources="TUE et TFUE, Conseil de l'UE, Journal officiel, SWP / GESIS et Commission" donnees="Les votes contre, abstentions et non-participations de chaque État membre au Conseil, les cinq actes où la France n'a pas voté pour avec leur décompte et leurs références, les bases juridiques du TFUE par règle de décision et les indicateurs de transposition de la France ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Ce que les traités n'ont pas attribué à l'Union reste aux États&nbsp;: la France y décide seule, en respectant les règles communes. Là où l'Union est compétente, la Commission propose, et le Conseil vote le plus souvent à la majorité qualifiée, parfois à l'unanimité. Sur les votes publics du Conseil sur des actes législatifs, du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}, la France a voté contre {{< ue-val "fr_contre" >}} et s'est abstenue {{< ue-val "fr_abst" >}}&nbsp;; un vote pour ne dit pas ce qu'elle a obtenu ou cédé dans la négociation.
{{< /reutiliser >}}
