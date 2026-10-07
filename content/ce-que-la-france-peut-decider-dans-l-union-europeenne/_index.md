---
title: "Ce que la France peut décider dans l'Union européenne"
description: "Dans quelles matières l'Union décide, selon quelle règle, et comment la France a voté au Conseil : les compétences fixées par le traité, {ue.n_plo} bases de la procédure législative ordinaire et {ue.n_una} bases à l'unanimité relevées dans le TFUE, les votes publics de la France du {ue.debut} au {ue.fin} ({ue.fr_c} contre, {ue.fr_a} abstentions) et la transposition des directives au {ue.tr_date}. Données ouvertes."
chapo: "Une promesse qui touche au marché intérieur, au commerce ou à l'agriculture se décide en partie à Bruxelles, avec d'autres. Le traité fixe les matières où seule l'Union peut légiférer, celles où elle partage cette compétence avec les États et celles où elle ne fait qu'appuyer leur action ; il fixe aussi la règle de vote, le plus souvent la majorité qualifiée, parfois l'unanimité. Sur les votes publics du Conseil sur des actes législatifs, du {ue.debut} au {ue.fin}, la France a voté contre {ue.fr_contre} et s'est abstenue {ue.fr_abst} ; elle a voté pour dans tous les autres cas. Ce vote final ne dit pas ce que la France a obtenu ou cédé dans la négociation qui le précède."
date: 2026-10-06
lastmod: 2026-10-06
donnees: [promesses_europe]
og_title: "Ce que la France peut décider dans l'Union européenne — compétences, règles de vote et votes de la France au Conseil — S. Lalut"
og_image: "images/og-europe-promesse.jpg"
og_image_alt: "Carte de partage : « La France au Conseil de l'UE » — votes contre et abstentions des États membres sur les votes publics d'actes législatifs, 2009-2026 ; la France est en bas de la liste, avec deux votes contre et trois abstentions."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_europe"
  nom: "Compétences et règles de vote de l'Union européenne, votes publics des États membres au Conseil (2009-2026) et transposition des directives par la France"
  description: "Typologie des compétences du TFUE (art. 2 à 6, texte consolidé de 2016) ; inventaire des bases juridiques de la procédure législative ordinaire et de l'unanimité au Conseil, contrôlé contre la liste du Secrétariat général du Conseil ; votes contre, abstentions et non-participations de chaque État membre dans les votes publics du Conseil sur des actes législatifs, du {ue.debut} au {ue.fin}, contrôlés contre le jeu SWP / GESIS (doi 10.7802/2560) ; indicateurs de transposition de la France au {ue.tr_date} (Commission)."
  couverture_temporelle: "2009/2026"
  couverture_spatiale: "Union européenne"
  variables:
    - {nom: "Votes des États membres au Conseil : contre, abstention, ne participe pas", unite: "votes publics"}
    - {nom: "Bases juridiques du TFUE selon la règle de décision", unite: "paragraphes du traité"}
    - {nom: "Déficits de transposition et de conformité", unite: "% des directives du marché unique"}
  sources:
    - "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12016E/TXT"
    - "https://www.consilium.europa.eu/en/general-secretariat/corporate-policies/transparency/voting-results/"
    - "https://doi.org/10.7802/2560"
    - "https://single-market-scoreboard.ec.europa.eu/enforcement-tools/transposition_en"
  mots: ["Union européenne", "Conseil de l'Union européenne", "majorité qualifiée", "unanimité", "compétences de l'Union", "TFUE", "transposition", "promesses"]
  fichiers: ["promesses_europe.csv", "promesses_europe.json"]
  doi: "10.5281/zenodo.23212665"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "La France peut-elle bloquer une loi européenne ?"
    answer: "Cela dépend de la règle de vote que fixe le traité pour la matière. Dans la procédure législative ordinaire, le Conseil statue à la majorité qualifiée : un État seul ne bloque pas. Là où le traité exige l'unanimité au Conseil (la fiscalité indirecte, à l'article 113 du TFUE, ou le cadre financier pluriannuel, à l'article 312), un seul État peut s'opposer. Le relevé du TFUE compte {ue.n_plo} bases de la procédure législative ordinaire et {ue.n_una} bases où le Conseil statue à l'unanimité ; ce nombre ne mesure pas le poids des matières."
  - question: "Combien de fois la France a-t-elle voté contre une loi européenne ?"
    answer: "Sur les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {ue.debut} au {ue.fin}, la France a voté contre {ue.fr_contre} et s'est abstenue {ue.fr_abst} ; elle a voté pour dans tous les autres cas. À titre de comparaison, sur le même relevé, l'Allemagne a voté contre {ue.de_c} fois, les Pays-Bas {ue.nl_c} fois, la Pologne {ue.pl_c} fois. Un vote pour ne dit pas ce que la France demandait au départ."
  - question: "La France transpose-t-elle les directives européennes à temps ?"
    answer: "Selon le tableau d'affichage du marché unique de la Commission, au {ue.tr_date}, {ue.tr_def} % des directives du marché unique n'étaient pas transposées en France ({ue.tr_retard} directives), comme en moyenne dans l'Union ; l'objectif, fixé à 1 % en 2007, a été ramené à 0,5 % par la Commission. Le déficit de conformité, tiré des procédures de la Commission pour transposition incorrecte, était de {ue.tr_conf} %, contre {ue.tr_conf_ue} % en moyenne."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 70
  prolongement: true
  nature: "Traité (EUR-Lex), votes du Conseil de l'UE contrôlés par un second jeu, Commission ; données ouvertes"
onglet:  # panneau « Prolongements » de la barre du dossier (partials/barre-bloc.html)
  long: "Ce que la France peut décider dans l'Union européenne"
  court: "Europe"
  role: "compétences, votes et transposition"
---

{{< reutiliser-ancre >}}

Une promesse qui touche au marché intérieur, au commerce, à l'agriculture ou à l'asile ne se décide pas seulement à Paris. Le traité sur le fonctionnement de l'Union européenne (TFUE) dit dans quelles matières l'Union décide et selon quelle règle&nbsp;; le Conseil de l'Union, où siègent les gouvernements, publie le vote de chaque État sur les actes législatifs. Cette page lit le traité article par article, relève les votes publiés et les contrôle contre un second jeu de données. Aucun chiffre n'est saisi à la main.

**Réponse courte.** Dans les matières de compétence exclusive de l'Union, la France ne peut pas légiférer seule, sauf habilitation de l'Union ou pour mettre en œuvre ses actes&nbsp;; elle participe aux décisions de l'Union selon les procédures prévues par les traités. Dans les compétences partagées, les États exercent leur compétence dans la mesure où l'Union n'a pas exercé la sienne. Au Conseil, la règle est le plus souvent la majorité qualifiée, et l'unanimité dans quelques matières. Sur les votes publics du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}, la France a voté contre {{< ue-val "fr_contre" >}} et s'est abstenue {{< ue-val "fr_abst" >}}.

## Dans quelles matières l'Union décide-t-elle&nbsp;? {#competences}

Le traité range les compétences de l'Union en trois catégories principales, et dit pour chacune ce qui reste aux États.

- **Compétence exclusive** (art.&nbsp;3)&nbsp;: {{< ue-val "exclusives" >}}. «&nbsp;{{< ue-val "cit_2_1" >}}&nbsp;» (art.&nbsp;2, §&nbsp;1). L'Union dispose aussi d'une compétence exclusive pour certains accords internationaux (art.&nbsp;3, §&nbsp;2).
- **Compétence partagée** (art.&nbsp;4)&nbsp;: les «&nbsp;principaux domaines&nbsp;» sont {{< ue-val "partagees" >}}. «&nbsp;{{< ue-val "cit_2_2" >}}&nbsp;» (art.&nbsp;2, §&nbsp;2). La liste n'est pas fermée&nbsp;: est partagée toute compétence attribuée qui n'est ni exclusive ni d'appui (art.&nbsp;4, §&nbsp;1). Pour la recherche, l'espace, la coopération au développement et l'aide humanitaire, l'action de l'Union ne peut pas empêcher les États d'exercer la leur (art.&nbsp;4, §&nbsp;3 et 4).
- **Appui, coordination, complément** (art.&nbsp;6)&nbsp;: {{< ue-val "appui" >}}. Dans ces domaines, l'Union agit «&nbsp;{{< ue-val "cit_2_5" >}}&nbsp;» (art.&nbsp;2, §&nbsp;5).

Les politiques économiques et de l'emploi relèvent d'une coordination (art.&nbsp;5), et la politique étrangère et de sécurité commune de règles propres, fixées par le traité sur l'Union européenne (art.&nbsp;2, §&nbsp;4).

{{< ue-tableau "competences" "Les domaines, cités dans le texte du traité" >}}

## Selon quelle règle le Conseil décide-t-il&nbsp;? {#regles-de-vote}

Deux règles dominent. Dans la **procédure législative ordinaire**, le Parlement européen et le Conseil adoptent ensemble l'acte, et le Conseil statue à la majorité qualifiée&nbsp;: aucun État ne peut bloquer seul, puisque, selon le traité sur l'Union européenne, «&nbsp;{{< ue-val "cit_tue16" >}}&nbsp;» (art.&nbsp;16, §&nbsp;4). Dans d'autres matières, le Conseil **statue à l'unanimité**&nbsp;: un seul État peut s'opposer. Le relevé complet du TFUE compte {{< ue-val "n_plo" >}} bases de la procédure législative ordinaire, dans {{< ue-val "n_plo_art" >}} articles, et {{< ue-val "n_una" >}} bases où le Conseil statue à l'unanimité, dans {{< ue-val "n_una_art" >}} articles. Ces nombres ne mesurent ni le poids des matières, ni la fréquence des actes adoptés sur chacune de ces bases&nbsp;: une seule base, l'article&nbsp;114 sur le marché intérieur, fonde un grand nombre d'actes.

{{< ue-tableau "instruments" "La règle, matière par matière, pour les instruments que nomment le livre et les programmes" >}}

<details class="repli"><summary>Ce qui a été vérifié</summary>

Le texte est la version consolidée du TFUE publiée au Journal officiel de l'Union le 7&nbsp;juin 2016. Chaque domaine des articles&nbsp;3, 4 et 6 est cité mot pour mot, et la complétude de chaque liste est relue dans le texte. Les {{< ue-val "n_plo" >}} bases ont été comparées à la liste que publie le Secrétariat général du Conseil dans son guide de la procédure législative ordinaire (annexe&nbsp;III, {{< ue-val "n_temoin" >}}&nbsp;entrées)&nbsp;: les deux listes concordent exactement. Cette comparaison a fait apparaître des bases qui renvoient à la procédure sans la nommer (articles&nbsp;42, 62 et 177), lues et ajoutées. {{< ue-val "n_cond" >}}&nbsp;bases suivent une procédure qui dépend de la mesure (articles&nbsp;83, §&nbsp;2, et 136, §&nbsp;1). Les mentions qui ne fondent pas un acte (freins d'urgence, passerelles, articles qui décrivent la procédure) sont écartées, chacune avec son motif, dans le fichier de données. La liste de l'unanimité n'a pas de second producteur sur le même périmètre&nbsp;: un inventaire universitaire de 2014 (S.&nbsp;Polidori, *Eurostudium3w*) compte {{< ue-val "polidori_tfue" >}} dispositions du TFUE à l'unanimité, Conseil européen compris&nbsp;; ce n'est pas la même unité, et il ne la contrôle donc pas.

</details>

## Comment la France vote-t-elle au Conseil&nbsp;? {#votes-au-conseil}

{{< figure-svg fichier="europe-votes" alt="Barres horizontales, une par État membre, triées par total : votes contre en foncé, abstentions en clair, avec les deux nombres après chaque barre ; la France, en bleu, est en bas de la liste. Les valeurs sont dans le tableau sous la figure." >}}Votes contre et abstentions de chaque État membre dans les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}. Le Royaume-Uni n'y figure que jusqu'à son retrait, la Croatie depuis son adhésion en 2013. Ces comptes bruts ne constituent pas un classement d'influence&nbsp;: durée d'appartenance et non-participation à certains actes diffèrent selon les États.{{< /figure-svg >}}

{{< fig-actions id="votes" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur les votes publics du Conseil de l'Union européenne sur des actes législatifs, du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}, la France a voté contre {{< ue-val "fr_contre" >}} et s'est abstenue {{< ue-val "fr_abst" >}}&nbsp;; elle a voté pour dans tous les autres cas.

</div>

{{< ue-tableau "france" "Les actes où la France n'a pas voté pour" >}}

{{< ue-tableau "etats" "Les votes de chaque État membre en tableau" >}}

À titre de comparaison, sur le même relevé, l'Allemagne a voté contre {{< ue-val "de_c" >}} fois et s'est abstenue {{< ue-val "de_a" >}} fois, les Pays-Bas ont voté contre {{< ue-val "nl_c" >}} fois, la Pologne {{< ue-val "pl_c" >}} fois, la Hongrie {{< ue-val "hu_c" >}} fois. Parmi les votes publiés, {{< ue-val "qmv" >}} relevaient de la majorité qualifiée et {{< ue-val "una" >}} de l'unanimité.

**Ce que ces chiffres ne disent pas.** Un vote pour, à la fin d'une négociation, ne dit pas ce que la France demandait au départ, ni ce qu'elle a obtenu ou cédé. Le relevé ne couvre que les votes **publics** sur des actes **législatifs**&nbsp;: ni les actes non législatifs, ni la politique étrangère, ni les discussions qui précèdent le vote. Ces comptes décrivent la position formelle des États au vote final. Ils ne mesurent ni leur influence dans la négociation, ni ce qu'ils ont obtenu ou cédé, ni leur capacité générale à bloquer une décision.

<details class="repli"><summary>Ce qui a été vérifié</summary>

**Le relevé.** Le Conseil a arrêté ses fichiers de données ouverts en mars 2025&nbsp;; ses résultats de vote ne sont plus publiés que par sa page de recherche, qui n'accepte pas les programmes. Le relevé a donc été fait dans un navigateur, le {{< ue-val "releve" >}}, page par page&nbsp;: {{< ue-val "entrees" >}} entrées, exactement le total que la page annonce, et les mêmes entrées vues depuis la France et depuis l'Allemagne. Le Conseil affiche {{< ue-val "doublons" >}} entrées en double, identiques dans tous leurs champs&nbsp;: le nombre d'actes est compris entre {{< ue-val "entrees_min" >}} et {{< ue-val "entrees" >}}. Ces doublons sont des votes unanimes et ne changent aucun compte de votes contre ou d'abstentions.

**Le témoin.** Le jeu de données constitué par l'Institut allemand pour les affaires internationales et de sécurité (SWP) à partir des données du Conseil, de 2010 à mars 2023, a été rapproché du relevé acte par acte, puis État par État&nbsp;: les comptes de votes contre et d'abstentions de {{< ue-val "etats_identiques" >}}&nbsp;États sur {{< ue-val "etats_total" >}} sont identiques dans les deux sources, et les écarts des autres s'expliquent&nbsp;: un acte du 28&nbsp;mars 2023 manque au jeu SWP, arrêté deux semaines plus tard&nbsp;; deux votes contre de la France datés du 17&nbsp;mai 2021 n'existent que dans le jeu SWP, sans titre ni objet, et le registre des documents du Conseil ne contient aucun résultat de vote cette semaine-là, alors qu'il contient bien ceux de la semaine précédente. Ces deux votes figurent dans le jeu SWP mais n'ont pas pu être corroborés dans les résultats et documents du Conseil utilisés pour cette page&nbsp;; ils ne sont donc pas intégrés au compte publié. Deux autres entrées du jeu SWP, sans titre et unanimes, n'ont pas non plus pu être corroborées&nbsp;; elles ne changent aucun compte de votes contre ou d'abstentions.

**Ce que le producteur du témoin écrivait déjà.** L'institut allemand qui a constitué ce jeu de données (SWP) écrivait en décembre&nbsp;2021&nbsp;: «&nbsp;{{< ue-val "swp21_cit" >}}&nbsp;». Notre relevé compte, de 2010 à 2021, {{< ue-val "swp21_contre" >}} vote contre et {{< ue-val "swp21_abst" >}} abstentions de la France&nbsp;; ce constat ne peut pas inclure les {{< ue-val "swp24_ecart" >}} votes contre du 17&nbsp;mai 2021 que porte le jeu de données. En avril&nbsp;2024, le même institut écrit, pour 2010 à septembre&nbsp;2023&nbsp;: «&nbsp;{{< ue-val "swp24_cit" >}}&nbsp;». Notre relevé compte {{< ue-val "swp24_nonpour" >}} votes contre ou abstentions sur cette période&nbsp;; l'écart est égal aux {{< ue-val "swp24_ecart" >}} entrées du jeu de données que la page écarte, sans que la note de 2024 liste les votes qu'elle compte.

</details>

## La France transpose-t-elle les directives à temps&nbsp;? {#transposition}

Une directive fixe un résultat&nbsp;; chaque État la transpose dans son droit, avant une date. La Commission mesure, deux fois par an, la part des directives du marché unique qui ne sont pas transposées à temps. Au {{< ue-val "tr_date" >}}, {{< ue-val "tr_def" >}}&nbsp;% des directives du marché unique dont l'échéance était passée n'étaient pas transposées en France, soit {{< ue-val "tr_retard" >}} directives sur {{< ue-val "tr_dues" >}}, la même valeur que la moyenne de l'Union. Le Conseil européen avait fixé en 2007 un objectif de 1&nbsp;%, que la Commission a ramené à 0,5&nbsp;% (Acte pour le marché unique de 2011, communication de mars 2023). Le déficit de conformité, part des directives que la Commission tient pour incorrectement transposées, à partir de ses procédures d'infraction pour transposition incorrecte, y est de {{< ue-val "tr_conf" >}}&nbsp;%, contre {{< ue-val "tr_conf_ue" >}}&nbsp;% en moyenne&nbsp;; une procédure engagée n'est pas un manquement constaté par la Cour. La Commission range la France parmi les {{< ue-val "tr_double" >}} États qui cumulent un déficit de transposition élevé et un déficit de conformité élevé.

{{< ue-tableau "transposition" "Les indicateurs de transposition de la France" >}}

Ces valeurs viennent d'une seule édition du tableau d'affichage de la Commission, qui ne les publie que dans un tableau interactif, sans fichier&nbsp;: elles ont été relevées sur une capture archivée, et les moyennes de l'Union contrôlées par le texte de la Commission. Un retard de transposition peut ouvrir une procédure de manquement (art.&nbsp;258 à 260 du TFUE), que la Commission engage et que la Cour de justice tranche.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas si l'Union décide trop ou trop peu, ni si la France y pèse beaucoup ou peu&nbsp;: aucune des mesures présentées ne le mesure. Elle ne compte ni les actes de la Commission, ni les décisions de la Banque centrale européenne, ni les arrêts de la Cour de justice. Elle ne compte pas non plus les votes du Conseil sur des actes non législatifs, comme les décisions relatives à la signature d'un accord commercial&nbsp;: les décisions de janvier&nbsp;2026 sur la signature de l'accord entre l'Union et le Mercosur, adoptées par procédure écrite, sont hors du relevé, quel qu'ait été le vote de chaque État. Elle lit le traité en vigueur, sans jurisprudence&nbsp;: c'est la Cour qui tranche le choix d'une base juridique. Les votes sont arrêtés au {{< ue-val "fin" >}}, la transposition au {{< ue-val "tr_date" >}}.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Changer les règles européennes" avis="non" >}}
Cette page montre ce que la France peut décider seule, ce qu'elle décide dans le cadre de l'Union et ce que les traités réservent aux institutions de l'Union. Le livre suit deux préférences françaises jusqu'à la règle européenne, l'une adoptée, l'autre bloquée, et confronte les promesses de «&nbsp;changer l'Europe&nbsp;» à ce que le traité permet. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Traité sur le fonctionnement de l'Union européenne**, version consolidée, Journal officiel de l'Union européenne C&nbsp;202 du 7&nbsp;juin 2016 (EUR-Lex), art.&nbsp;2 à 6 et ensemble du traité pour les bases juridiques.

**Conseil de l'Union européenne**, recherche des résultats de vote sur les actes législatifs (relevé du {{< ue-val "releve" >}})&nbsp;; registre public des documents&nbsp;; Secrétariat général du Conseil, *Guide to the ordinary legislative procedure*, 2010, annexe&nbsp;III (doi 10.2860/74684).

**Ondarza, Nicolai von et Bochtler, Paul**, *Public Voting Data of the Council of the EU*, version 2.0.0, SWP, 2023, doi [10.7802/2560](https://doi.org/10.7802/2560), licence CC BY 4.0.

**Commission européenne**, tableau d'affichage du marché unique et de la compétitivité, transposition, édition arrêtée au {{< ue-val "tr_date" >}}.

Les chiffres, les contrôles et la figure sont produits par un script unique, qui relit le traité, le jeu SWP et les relevés archivés, et refuse d'écrire si une donnée cesse de soutenir une phrase. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_europe.csv), en format long&nbsp;; [JSON](/promesses_europe.json), avec les bases juridiques, les écarts expliqués et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212665](https://doi.org/10.5281/zenodo.23212665).

{{< reutiliser figures="figures_europe" jeu="promesses_europe" sources="TFUE, Conseil de l'UE, SWP / GESIS et Commission" donnees="Les votes contre, abstentions et non-participations de chaque État membre au Conseil, les actes où la France n'a pas voté pour, les bases juridiques du TFUE par règle de décision et les indicateurs de transposition de la France ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Ce que la France peut décider dans l'Union dépend de la matière&nbsp;: compétence exclusive de l'Union, partagée avec les États, ou simple appui, selon les articles&nbsp;2 à 6 du traité sur le fonctionnement de l'Union européenne. Au Conseil, la règle est le plus souvent la majorité qualifiée, parfois l'unanimité. Sur les votes publics du Conseil sur des actes législatifs, du {{< ue-val "debut" >}} au {{< ue-val "fin" >}}, la France a voté contre {{< ue-val "fr_contre" >}} et s'est abstenue {{< ue-val "fr_abst" >}}&nbsp;; un vote pour ne dit pas ce qu'elle a obtenu ou cédé dans la négociation.
{{< /reutiliser >}}
