---
title: "Une promesse peut-elle produire ses effets en cinq ans ?"
description: "Combien de temps faut-il pour former un médecin généraliste, et que peut-on faire avant ? La durée du cursus écrite dans les textes en vigueur, comparée à celle du mandat présidentiel, et les admissions en études de médecine depuis 1972. Données ouvertes."
chapo: "Le cas-test de la formation des médecins généralistes. Le temps de la décision et celui de ses effets ne coïncident pas nécessairement. Aux règles en vigueur pour les étudiants qui commencent le troisième cycle depuis 2023, le cursus standard de médecine générale dure au moins {del.duree} ans depuis la première année, soit {del.nmax} fois la durée d'un mandat présidentiel. Cela ne signifie pas qu'aucun effet n'apparaisse auparavant : les étudiants réalisent des actes de soins au cours de leur formation, sous supervision."
date: 2026-10-06
lastmod: 2026-10-06
donnees: [promesses_delais]
og_title: "Une promesse peut-elle produire ses effets en cinq ans ? — le cas-test de la formation des médecins — S. Lalut"
og_image: "images/og-delais-promesse.jpg"
og_image_alt: "Carte de partage : « Au moins 10 ans pour former un généraliste. Deux fois la durée d'un mandat présidentiel. » Deux barres de même échelle : le cursus de médecine générale en trois cycles, et un mandat présidentiel ; comparaison d'échelle seulement."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_delais"
  nom: "Durée du cursus de médecine générale et admissions en études de médecine, 1972-2025"
  description: "Durées minimales du cursus de médecine générale lues dans les textes en vigueur (arrêté du 8 avril 2013, art. 1 ; code de l'éducation, art. L632-2 ; loi n° 2022-1616, art. 37) et durée du mandat présidentiel (Constitution, art. 6) ; places pourvues en études de médecine de 1972 à 2020 (DREES, Dossier n° 76, source ONDPS) et admis de 2021 à 2025 (ONDPS) ; part des médecins actifs diplômés à l'étranger en 2012 et 2026 (DREES, RPPS)."
  couverture_temporelle: "1972/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Places pourvues puis admis en études de médecine", unite: "étudiants par an"}
    - {nom: "Durées minimales du cursus et du mandat", unite: "semestres ou années"}
    - {nom: "Médecins actifs diplômés à l'étranger", unite: "médecins au 1er janvier"}
  sources:
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046812307"
    - "https://drees.solidarites-sante.gouv.fr/sites/default/files/2021-03/DD76_0.pdf"
  mots: ["médecins", "études de médecine", "numerus clausus", "médecine générale", "mandat présidentiel", "délais"]
  fichiers: ["promesses_delais.csv", "promesses_delais.json"]
  doi: "10.5281/zenodo.23212665"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Combien de temps faut-il pour former un médecin généraliste ?"
    answer: "Aux règles en vigueur pour les étudiants qui commencent le troisième cycle depuis la rentrée 2023, au moins {del.duree} ans depuis la première année : {del.cycle1} semestres de premier cycle, {del.cycle2} semestres de deuxième cycle (arrêté du 8 avril 2013), puis un troisième cycle de médecine générale « d'une durée de quatre années » (code de l'éducation, art. L632-2). C'est une durée minimale, sans redoublement, interruption ni passerelle. La dernière année se déroule en stage, sous un régime d'autonomie supervisée."
  - question: "Une hausse des admissions produit-elle de nouveaux médecins généralistes formés en cinq ans ?"
    answer: "Pas pour les étudiants qui entrent alors en première année : aux règles en vigueur pour ceux qui commencent le troisième cycle depuis 2023, leur cursus complet dure au moins {del.duree} ans. Des actes de soins sont toutefois réalisés avant son achèvement, sous supervision, comme le prévoient le code de l'éducation (art. L632-2) et le code de la santé publique (art. R6153-1-2)."
  - question: "Combien d'étudiants entrent en études de médecine ?"
    answer: "{del.admis_2025} en 2025, pour {del.capacites_2025} places, selon l'ONDPS ; {del.admis_2021_2025} de 2021 à 2025. Les places avaient été divisées par {del.rapport_baisse} entre 1972 ({del.places_1972}) et {del.an_min} ({del.places_min}), avant de remonter. Le champ des places a changé en 2010-2011 (passerelles et droits au remords inclus), et la série relève depuis 2021 du régime du numerus apertus."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 40
  nature: "Textes en vigueur et séries DREES et ONDPS, vérifiés ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Une promesse peut-elle produire ses effets en cinq ans ?"
  court: "Délais"
  role: "horloges et capacités"
---

{{< reutiliser-ancre >}}

Le temps de la décision et le temps de ses effets ne coïncident pas nécessairement. La formation des médecins en donne une mesure nette, parce que sa durée est écrite dans les textes. Cette page compare cette durée à celle du mandat présidentiel, montre ce qui agit avant la fin du cursus, et retrace le nombre de places depuis 1972. Toutes les durées sont lues dans les textes en vigueur, et aucune n'est saisie à la main.

**Réponse courte.** Pour des étudiants qui entrent en première année, l'achèvement du cursus de médecine générale ne tient pas dans un mandat de cinq ans aux règles actuelles. Cela ne signifie pas que la mesure n'aurait aucun effet avant&nbsp;: les étudiants réalisent des actes de soins au cours de leur formation.

## Combien de temps faut-il pour former un médecin généraliste&nbsp;? {#duree-du-cursus}

Le premier cycle et le deuxième cycle comptent chacun {{< del-val "cycle1" >}} semestres. Le troisième cycle de médecine générale dure quatre ans pour les étudiants qui l'ont commencé depuis la rentrée 2023. Le mandat présidentiel dure cinq ans.

{{< figure-svg fichier="delais-cursus" alt="Deux barres de même échelle, en années. En haut, le cursus de médecine générale en trois cycles, la dernière année en autonomie supervisée. En bas, un mandat présidentiel, deux fois plus court. Les valeurs sont dans le texte qui suit." >}}Durées minimales écrites dans les textes en vigueur, sans redoublement, interruption ni passerelle. Comparaison d'échelle uniquement&nbsp;: elle ne mesure ni l'effet d'une politique ni la date à laquelle ses premiers effets peuvent apparaître.{{< /figure-svg >}}

{{< fig-actions id="cursus" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Aux règles en vigueur pour les étudiants entrés en troisième cycle depuis la rentrée 2023, le cursus standard de médecine générale dure au moins {{< del-val "duree" >}} ans depuis la première année, soit {{< del-val "nmax" >}} fois la durée d'un mandat présidentiel.

</div>

<details class="repli"><summary>Les textes qui fixent ces durées, cités mot pour mot</summary>

- **Premier cycle** (arrêté du 8&nbsp;avril 2013, art.&nbsp;1)&nbsp;: «&nbsp;{{< del-val "cit_cycle1" >}}&nbsp;».
- **Deuxième cycle** (même article)&nbsp;: «&nbsp;{{< del-val "cit_cycle2" >}}&nbsp;».
- **Troisième cycle de médecine générale** (code de l'éducation, art.&nbsp;L632-2)&nbsp;: un troisième cycle «&nbsp;{{< del-val "cit_mg" >}}&nbsp;».
- **Application** (loi n°&nbsp;2022-1616 du 23&nbsp;décembre 2022, art.&nbsp;37, II)&nbsp;: «&nbsp;{{< del-val "cit_37" >}}&nbsp;»
- **Mandat** (Constitution, art.&nbsp;6)&nbsp;: «&nbsp;{{< del-val "cit_art6a" >}}&nbsp;»

L'ordre de grandeur est aussi celui du service statistique du ministère de la Santé, qui écrivait en 2021&nbsp;: «&nbsp;{{< del-val "cit_dd76" >}}&nbsp;» (DREES, *Les Dossiers de la DREES* n°&nbsp;76). La page le précise à partir des textes en vigueur, quatrième année de médecine générale comprise.

Ces citations sont extraites des textes officiels par le script qui produit la page, et vérifiées mot pour mot à chaque génération&nbsp;; les durées de la figure sont calculées à partir des mots «&nbsp;six semestres&nbsp;», «&nbsp;quatre années&nbsp;» et «&nbsp;cinq ans&nbsp;», et le script recalcule leur rapport à chaque génération. Les autres spécialités ont des troisièmes cycles de durées différentes, que cette page ne décrit pas.

</details>

## Les étudiants soignent-ils avant la fin du cursus&nbsp;? {#avant-la-fin}

Oui, et les textes l'organisent. «&nbsp;{{< del-val "cit_supervision" >}}&nbsp;» (code de l'éducation, art.&nbsp;L632-2). Le code de la santé publique précise le régime du docteur junior, en dernière phase de formation&nbsp;: «&nbsp;{{< del-val "cit_dj1" >}}&nbsp;» Mais «&nbsp;{{< del-val "cit_dj2" >}}&nbsp;» (art.&nbsp;R6153-1-2). Des actes de soins sont donc réalisés par des médecins en formation, sous le régime prévu par ces textes&nbsp;; les textes n'en mesurent pas la part dans l'ensemble des soins.

Cette durée de formation ne décrit pas, à elle seule, l'effectif des médecins déjà en activité. À titre distinct, au 1er&nbsp;janvier 2026, selon la DREES, {{< del-val "etr_26" >}} des {{< del-val "tot_26" >}} médecins actifs, soit {{< del-val "etr_p26" >}}&nbsp;%, avaient obtenu leur diplôme à l'étranger, contre {{< del-val "etr_p12" >}}&nbsp;% en 2012. C'est un effectif présent, non le nombre d'arrivées d'une année, et le lieu du diplôme ne dit pas la nationalité. Ce rapprochement ne mesure aucune compensation des capacités de formation françaises par les diplômes obtenus à l'étranger.

## Combien d'étudiants commencent des études de médecine&nbsp;? {#admissions}

{{< figure-svg fichier="delais-admissions" alt="Barres annuelles des admissions en études de médecine de 1972 à 2025 : une baisse jusqu'à un minimum au début des années 1990, puis une remontée ; deux lignes en pointillés marquent les changements de champ de 2010-2011 et de 2021. Les valeurs sont dans le texte qui suit." >}}Places pourvues en études de médecine de 1972 à 2020 (DREES, source ONDPS), puis admis de 2021 à 2025 (ONDPS), à leur année. Chaque barre restitue les places pourvues ou les admis rattachés à l'année publiée par la source&nbsp;; aucune valeur n'est déplacée vers une année d'exercice supposée.{{< /figure-svg >}}

{{< fig-actions id="admissions" >}}

**Ne pas décaler mécaniquement ces barres de dix ans pour en déduire une année d'exercice**&nbsp;: les règles de durée ont changé, les étudiants réalisent des actes de soins avant la fin du cursus, et cette série ne suit pas individuellement les étudiants jusqu'à leur exercice.

Les places ont été divisées par {{< del-val "rapport_baisse" >}} entre 1972 ({{< del-val "places_1972" >}}) et {{< del-val "an_min" >}} ({{< del-val "places_min" >}}), puis sont remontées, avec des changements de champ signalés sur la série. Selon l'ONDPS, {{< del-val "admis_2021_2025" >}} étudiants ont été admis de 2021 à 2025, soit {{< del-val "hausse_quinquennale" >}}&nbsp;% de plus qu'en 2016-2020 ({{< del-val "admis_2016_2020" >}}), et {{< del-val "admis_2025" >}} en 2025 pour {{< del-val "capacites_2025" >}} places.

Deux ruptures se lisent sur la figure. Jusqu'en 2009, la série compte le seul numerus clausus principal&nbsp;; à partir de 2011, elle inclut les passerelles et les droits au remords (note de la DREES). Depuis 2021, la série relève du régime du numerus apertus&nbsp;; l'ONDPS publie les nombres d'admis.

<details class="repli"><summary>Ce qui a été vérifié, et l'écart qui reste</summary>

Les admissions de 2021 à 2025 sont lues sur une figure de l'ONDPS publiée en image&nbsp;; leur somme est contrôlée contre le total que l'ONDPS imprime, et ce total comme les admis de 2025 se retrouvent dans le texte du document. La série de la DREES est comparée aux totaux par périodes de cinq ans que publie l'ONDPS&nbsp;: elle concorde exactement pour 2001-2005, 2006-2010 et 2011-2015. Pour 2016-2020, la somme des valeurs de la DREES dépasse de {{< del-val "ecart_2016_2020" >}} places le total de l'ONDPS, soit environ {{< del-val "ecart_pct" >}}&nbsp;% de ce total&nbsp;; la valeur 2020 de la DREES porte un astérisque dont la légende n'a pas été trouvée. L'écart est publié, il n'est pas corrigé.

</details>

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas combien de médecins exerceront dans dix ans, ni si l'accès aux soins s'améliorera&nbsp;: le nombre de médecins en activité dépend aussi des départs, des diplômés étrangers, des choix de spécialité et des lieux d'installation, qu'aucune de ces séries ne mesure. Elle ne relie pas une cohorte d'admis à une année d'exercice, parce que les règles de durée ont changé au fil des décennies. Elle ne décrit pas les autres horloges qu'une promesse rencontre, comme la formation des forces de l'ordre ou le temps d'une scolarité, faute d'avoir lu leurs textes.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="L'horloge d'une promesse" avis="non" >}}
Cette page mesure une horloge&nbsp;: le temps qu'il faut pour former un médecin. Le livre suit une promesse sur l'accès aux soins depuis son énoncé de campagne jusqu'à l'endroit où son résultat échappe à l'élu, et rencontre d'autres horloges en chemin&nbsp;: une cohorte d'élèves, un budget carbone, le temps d'une loi et de ses décrets. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Textes en vigueur**, lus sur Légifrance (API) et dans le Journal officiel de la DILA&nbsp;: arrêté du 8&nbsp;avril 2013 relatif au régime des études en vue du premier et du deuxième cycle des études médicales, art.&nbsp;1&nbsp;; code de l'éducation, art.&nbsp;L632-2&nbsp;; loi n°&nbsp;2022-1616 du 23&nbsp;décembre 2022, art.&nbsp;37&nbsp;; code de la santé publique, art.&nbsp;R6153-1-2&nbsp;; Constitution, art.&nbsp;6.

**DREES**, *Quelle démographie récente et à venir pour les professions médicales et pharmaceutique&nbsp;?*, Les Dossiers de la DREES n°&nbsp;76, mars 2021, graphique&nbsp;8 (source ONDPS)&nbsp;; démographie des professionnels de santé, RPPS, publication du 2&nbsp;juillet 2026.

**ONDPS**, bilan des formations des professionnels de santé 2021-2025, note du 19&nbsp;décembre 2025.

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique&nbsp;; aucun chiffre ni aucune durée de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_delais.csv), en format long&nbsp;; [JSON](/promesses_delais.json), avec les définitions et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212665](https://doi.org/10.5281/zenodo.23212665).

{{< reutiliser figures="figures_delais" jeu="promesses_delais" sources="Légifrance, DREES et ONDPS" donnees="Les durées du cursus de médecine générale et du mandat lues dans les textes, les places pourvues de 1972 à 2020, les admis de 2021 à 2025 et les médecins actifs diplômés à l'étranger ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Aux règles en vigueur, former un médecin généraliste prend au moins {{< del-val "duree" >}} ans depuis la première année d'études, soit {{< del-val "nmax" >}} fois la durée d'un mandat présidentiel&nbsp;; comparaison d'échelle seulement. Les étudiants soignent avant la fin du cursus, en autonomie supervisée, et {{< del-val "etr_p26" >}}&nbsp;% des médecins actifs ont été diplômés à l'étranger. Les places en études de médecine ont été divisées par {{< del-val "rapport_baisse" >}} entre 1972 et {{< del-val "an_min" >}}, avant de remonter&nbsp;; {{< del-val "admis_2021_2025" >}} étudiants ont été admis de 2021 à 2025.
{{< /reutiliser >}}
