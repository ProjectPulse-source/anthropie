---
title: "Une promesse peut-elle produire ses effets en cinq ans ?"
description: "Combien de temps faut-il pour former un médecin généraliste, qui décide du nombre d'étudiants admis, et qu'est-ce qui change avant le diplôme ? La durée du cursus écrite dans les textes, comparée au mandat présidentiel ; les étudiants admis en deuxième année du cursus de médecine depuis 1972. Données ouvertes."
chapo: "Le cas-test de la formation des médecins généralistes. Une décision qui augmente le nombre d'étudiants n'atteint pas son résultat final dans le mandat qui la prend. Un généraliste se forme en au moins {del.duree} ans depuis la première année, {del.nfois} la durée d'un mandat présidentiel (règles applicables depuis la rentrée {del.an_reforme}). Une telle décision peut pourtant agir avant, car les internes soignent sous supervision pendant leur formation. Et le nombre d'étudiants admis ne dépend pas d'une seule signature : l'État fixe un objectif, chaque université vote ses places."
date: 2026-10-06
lastmod: 2026-10-12
donnees: [promesses_delais]
og_title: "Une promesse peut-elle produire ses effets en cinq ans ? — le cas-test de la formation des médecins — S. Lalut"
og_image: "images/og-delais-promesse.jpg"
og_image_alt: "Carte de partage : « Au moins 10 ans pour former un généraliste. Deux fois un mandat, aux règles de 2023. » Deux barres de même échelle : le cursus de médecine générale, internat compris, et un mandat présidentiel ; comparaison d'échelle seulement."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_delais"
  nom: "Durée du cursus de médecine générale et étudiants admis en deuxième année du cursus de médecine, 1972-2025"
  description: "Durées minimales du cursus de médecine générale lues dans les textes en vigueur (arrêté du 8 avril 2013, art. 1 ; code de l'éducation, art. L632-2 ; loi n° 2022-1616, art. 37) et durée du mandat présidentiel (Constitution, art. 6) ; étudiants admis en deuxième année du premier cycle de médecine (en troisième par une passerelle) : places pourvues du numerus clausus de 1972 à 2020 (DREES, Dossier n° 76, source ONDPS) et admis de 2021 à 2025 (ONDPS) ; part des médecins actifs diplômés à l'étranger en 2012 et 2026 (DREES, RPPS)."
  couverture_temporelle: "1972/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Places pourvues puis admis en deuxième année du premier cycle de médecine", unite: "étudiants par an"}
    - {nom: "Durées minimales du cursus et du mandat", unite: "semestres ou années"}
    - {nom: "Médecins actifs diplômés à l'étranger", unite: "médecins au 1er janvier"}
  sources:
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046812307"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051820015"
    - "https://drees.solidarites-sante.gouv.fr/sites/default/files/2021-03/DD76_0.pdf"
  mots: ["médecins", "études de médecine", "numerus clausus", "médecine générale", "mandat présidentiel", "délais"]
  fichiers: ["promesses_delais.csv", "promesses_delais.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Combien de temps faut-il pour former un médecin généraliste ?"
    answer: "Aux règles applicables aux étudiants qui entrent en internat (le troisième cycle) à partir de la rentrée {del.an_reforme}, au moins {del.duree} ans depuis la première année : {del.cycle1} semestres de premier cycle, {del.cycle2} semestres de deuxième cycle (arrêté du 8 avril 2013), puis un internat de médecine générale de {del.mg} ans (code de l'éducation, art. L632-2). Depuis l'admission en deuxième année, il reste au moins {del.duree_adm} ans. Ce sont des durées minimales, sans redoublement, interruption ni passerelle ; les internes soignent pendant ces années, sous supervision."
  - question: "Qui décide du nombre d'étudiants en médecine ?"
    answer: "Depuis le {del.d631_2020}, trois étages (code de l'éducation, art. L631-1) : l'État fixe des objectifs nationaux pluriannuels de professionnels à former ; chaque université arrête ses objectifs d'admission en deuxième cycle, sur avis conforme de l'agence régionale de santé et, depuis le {del.d631_2025}, des conseils territoriaux de santé ; chaque université détermine aussi, chaque année, ses capacités d'accueil en deuxième et troisième années du premier cycle. Auparavant, les ministres chargés de la santé et de l'enseignement supérieur fixaient eux-mêmes chaque année ce nombre : c'était le numerus clausus."
  - question: "Combien d'étudiants sont admis dans le cursus de médecine ?"
    answer: "{del.admis_2025} en 2025, admis en deuxième année du premier cycle (ou en troisième par une passerelle) pour {del.capacites_2025} places de capacité d'accueil, selon l'ONDPS ; {del.admis_2021_2025} de 2021 à 2025. La première année d'études n'est pas comptée. Les places pourvues du numerus clausus avaient été divisées par {del.rapport_baisse} entre 1972 ({del.places_1972}) et {del.an_min} ({del.places_min}), avant de remonter ; le champ s'est élargi en 2010-2011 aux passerelles et aux droits au remords, et le numerus clausus a pris fin après la rentrée 2020."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  rang: 40
  refonte: "2026-10-12"
  nature: "Textes en vigueur et séries DREES et ONDPS, vérifiés ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Une promesse peut-elle produire ses effets en cinq ans ?"
  court: "Délais"
  role: "horloges et capacités"
---

{{< reutiliser-ancre >}}

On décide aujourd'hui de former davantage de médecins. Quand les patients en verront-ils les effets&nbsp;? La médecine générale permet de distinguer précisément ce que les textes permettent de dater de ce que les données ne permettent pas encore de mesurer. On y lit trois horloges. Celle des textes fixe la durée du cursus&nbsp;; celle des capacités, combien d'étudiants le suivent&nbsp;; celle de l'effet dit quand les patients voient la différence, et aucune série ne la mesure ici.

## Combien de temps faut-il pour former un médecin généraliste&nbsp;? {#duree-du-cursus}

Le cursus compte trois cycles&nbsp;: {{< del-val "cycle1" >}} semestres de premier cycle, {{< del-val "cycle2" >}} de deuxième cycle, puis l'internat. En médecine générale, l'internat dure {{< del-val "mg" >}} ans pour les étudiants qui l'ont commencé à partir de la rentrée {{< del-val "an_reforme" >}}&nbsp;; cette quatrième année a été créée par une loi du {{< del-val "loi_date" >}}. Le mandat présidentiel dure {{< del-val "mandat" >}} ans.

{{< figure-svg fichier="delais-cursus" alt="Deux barres de même échelle, en années. En haut, le cursus de médecine générale : premier cycle, deuxième cycle, puis un seul bloc d'internat de médecine générale dont la dernière année, plus foncée, se fait en autonomie supervisée ; une accolade marque la durée comptée depuis l'admission en deuxième année. En bas, un mandat présidentiel, à la même échelle. Les valeurs sont dans le texte qui suit." >}}Durées minimales écrites dans les textes en vigueur, sans redoublement, interruption ni passerelle. Comparaison d'échelle uniquement&nbsp;: elle ne mesure ni l'effet d'une politique ni la date à laquelle ses premiers effets peuvent apparaître.{{< /figure-svg >}}

{{< fig-actions id="cursus" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Aux règles applicables depuis la rentrée {{< del-val "an_reforme" >}}, le cursus standard de médecine générale dure au moins {{< del-val "duree" >}} ans depuis la première année, soit {{< del-val "nfois" >}} la durée d'un mandat présidentiel.

</div>

**Cette durée est celle d'un diplôme, pas le délai d'un effet.** Pour la voie ordinaire, depuis l'admission en deuxième année du premier cycle, il reste au moins {{< del-val "duree_adm" >}} ans de formation. Certaines passerelles permettent une admission directe en troisième année&nbsp;; les séries agrégées présentées ici ne permettent pas d'en isoler l'effectif. Pour l'Observatoire national de la démographie des professions de santé (ONDPS), les objectifs fixés en 2021 visent de même «&nbsp;{{< del-val "cit_ondps_9_11" >}}&nbsp;». Et les internes soignent bien avant la fin du cursus.

<details class="repli"><summary>Les textes qui fixent ces durées, cités mot pour mot</summary>

- **Premier cycle** (arrêté du 8&nbsp;avril 2013, art.&nbsp;1)&nbsp;: «&nbsp;{{< del-val "cit_cycle1" >}}&nbsp;».
- **Deuxième cycle** (même article)&nbsp;: «&nbsp;{{< del-val "cit_cycle2" >}}&nbsp;».
- **Internat de médecine générale** (code de l'éducation, art.&nbsp;L632-2)&nbsp;: un troisième cycle «&nbsp;{{< del-val "cit_mg" >}}&nbsp;».
- **Application** (loi n°&nbsp;2022-1616 du 23&nbsp;décembre 2022 de financement de la sécurité sociale pour 2023, art.&nbsp;37, II)&nbsp;: «&nbsp;{{< del-val "cit_37" >}}&nbsp;»
- **Mandat** (Constitution, art.&nbsp;6)&nbsp;: «&nbsp;{{< del-val "cit_art6a" >}}&nbsp;»

</details>

## Qui décide du nombre d'étudiants admis&nbsp;? {#qui-decide}

Aucune signature ne fixe seule ce nombre. Le code de l'éducation (art.&nbsp;L631-1) répartit la décision entre trois étages, chacun sur un effectif différent et à un rythme différent.

- **L'État** fixe des objectifs nationaux pluriannuels&nbsp;: un nombre de professionnels à former, pour cinq ans (2021-2025, puis 2026-2030).
- **Chaque université** arrête ses objectifs pluriannuels d'admission&nbsp;: un nombre d'étudiants à admettre en première année du deuxième cycle. Elle le fait sur avis conforme, c'est-à-dire un avis qui la lie, de l'agence régionale de santé et, depuis le {{< del-val "d631_2025" >}}, des conseils territoriaux de santé.
- **Chaque université**, encore, vote chaque année ses capacités d'accueil&nbsp;: des places en deuxième et troisième années du premier cycle.

**Trois nombres, trois objets.** L'objectif national de l'État compte des professionnels à former&nbsp;; la capacité d'accueil votée par l'université compte des places&nbsp;; l'admission, relevée par l'ONDPS, compte les étudiants entrés sur ces places. Aucun ne compte des médecins diplômés, encore moins des consultations.

Ce partage date du {{< del-val "d631_2020" >}}. Auparavant, les ministres chargés de la santé et de l'enseignement supérieur fixaient eux-mêmes, chaque année, le nombre d'étudiants admis à poursuivre après la première année&nbsp;: c'était le numerus clausus.

<details class="repli"><summary>L'article L631-1 dans le texte, et ses versions depuis 2004</summary>

Le texte en vigueur confie les places aux universités&nbsp;: «&nbsp;{{< del-val "cit_631_cap" >}}&nbsp;» Les objectifs de l'État encadrent ceux des universités&nbsp;: «&nbsp;{{< del-val "cit_631_onp" >}}&nbsp;». Les candidats passent des épreuves pour obtenir ces places.

Le numerus clausus figurait dans les versions de L631-1 en vigueur de 2004 à 2020. La version entrée en vigueur le {{< del-val "d631_2020" >}} ({{< del-val "loi631_2020" >}}) confie les capacités aux universités, dans le cadre des objectifs de l'État&nbsp;; l'usage appelle ce régime «&nbsp;numerus apertus&nbsp;», un terme que la loi n'emploie pas. Depuis le {{< del-val "d631_2023" >}} ({{< del-val "loi631_2023" >}}), les objectifs des universités sont ceux «&nbsp;{{< del-val "cit_631_2023" >}}&nbsp;», alors que la version de 2020 citait les deux sans ordre. Depuis le {{< del-val "d631_2025" >}} ({{< del-val "loi631_2025" >}}), l'avis conforme des conseils territoriaux de santé s'ajoute à celui de l'agence régionale de santé.

- **De 2004 à 2010**&nbsp;: «&nbsp;{{< del-val "cit_631_2004" >}}&nbsp;», par les deux ministres.
- **De 2010 à 2020**&nbsp;: «&nbsp;{{< del-val "cit_631_2010" >}}&nbsp;» notamment «&nbsp;{{< del-val "cit_631_2010b" >}}&nbsp;».
- **Du {{< del-val "d631_2020" >}} au {{< del-val "d631_2023" >}}**&nbsp;: «&nbsp;{{< del-val "cit_631_2020" >}}&nbsp;»
- **Depuis le {{< del-val "d631_2025" >}}**&nbsp;: «&nbsp;{{< del-val "cit_631_obj" >}}&nbsp;»

</details>

Ce que ce partage a produit, l'ONDPS le mesure. Pour 2021-2025, l'objectif national fixé par l'État était de {{< del-val "onp" >}} médecins à former (arrêté du 13&nbsp;septembre 2021, selon l'ONDPS). Les universités ont admis {{< del-val "admis_2021_2025" >}} étudiants sur ces cinq ans, en deuxième année du premier cycle ou, par une passerelle, en troisième. En 2025, elles en ont admis {{< del-val "admis_2025" >}} pour {{< del-val "capacites_2025" >}} places de capacité d'accueil. L'ONDPS en conclut&nbsp;: «&nbsp;{{< del-val "cit_ondps_sat" >}}&nbsp;» Il rapporte aussi une prévision des UFR, non un constat de la rentrée&nbsp;: «&nbsp;{{< del-val "cit_ondps_2026" >}}&nbsp;» Les objectifs de 2026-2030 sont en préparation&nbsp;: le 3&nbsp;juillet 2025, les ministres ont lancé les «&nbsp;{{< del-val "cit_ondps_2630" >}}&nbsp;» (ONDPS).

**Relever l'objectif national, que fixent les ministres par arrêté, est l'un des leviers de l'État.** Mais augmenter effectivement les admissions suppose aussi des capacités universitaires adaptées, éventuellement des moyens supplémentaires et, selon les décisions envisagées, une évolution du cadre juridique. Les places, elles, se votent université par université&nbsp;; à l'échelle nationale, les admissions les remplissent déjà.

**L'État peut-il imposer davantage de places&nbsp;?** Dans le cadre juridique actuellement en vigueur, il fixe l'objectif, pas les places. Depuis le {{< del-val "d631_2025" >}}, si l'agence régionale de santé et les conseils territoriaux de santé jugent que les capacités d'une université ne correspondent pas aux objectifs qu'elle a elle-même arrêtés, «&nbsp;{{< del-val "cit_631_hausse" >}}&nbsp;»&nbsp;: la loi écrit «&nbsp;peut&nbsp;», non «&nbsp;doit&nbsp;». Elle renvoie à un décret les modalités de cette hausse, «&nbsp;{{< del-val "cit_631_moyens" >}}&nbsp;». Le seul verbe «&nbsp;peut&nbsp;» n'établit pas l'absence de toute obligation&nbsp;: une obligation pourrait résulter d'autres textes ou de ces modalités d'application.

**D'où vient la saturation&nbsp;?** L'ONDPS ne le dit pas, et cette page ne sait pas si elle tient aux terrains de stage, à l'encadrement ou au budget des universités. La saturation nationale ne renseigne ni sur les marges de chaque université ni sur les moyens qui permettraient d'accroître ses capacités.

## Combien d'étudiants sont admis dans le cursus de médecine&nbsp;? {#admissions}

**Être admis dans le cursus de médecine, au sens de toutes les séries de cette page, c'est obtenir une place en deuxième année du premier cycle, à l'issue d'une première année d'études, ou en troisième année par une passerelle.** L'ONDPS ne dit pas combien d'admis passent par la seconde porte. La première année n'est pas comptée.

{{< figure-svg fichier="delais-admissions" alt="Barres annuelles des étudiants admis en deuxième année du cursus de médecine, de 1972 à 2025 : une baisse jusqu'à un minimum au début des années 1990, puis une remontée ; deux lignes en pointillés marquent l'élargissement du champ en 2010-2011 et la fin du numerus clausus en 2021. Les valeurs sont dans le texte qui suit." >}}Places pourvues du numerus clausus de 1972 à 2020 (DREES, source ONDPS), puis étudiants admis de 2021 à 2025 (ONDPS), en deuxième année du premier cycle (en troisième pour certaines passerelles), chacun à l'année publiée par la source. Aucune valeur n'est déplacée vers une année d'exercice supposée.{{< /figure-svg >}}

{{< fig-actions id="admissions" >}}

**Ne pas décaler mécaniquement ces barres pour en déduire une année d'exercice**&nbsp;: les règles de durée ont changé, les étudiants soignent avant la fin du cursus, et cette série ne suit pas individuellement les étudiants jusqu'à leur exercice.

Les places pourvues du numerus clausus ont été divisées par {{< del-val "rapport_baisse" >}} entre 1972 et {{< del-val "an_min" >}}, puis sont remontées. On comptait {{< del-val "places_1972" >}} places pourvues en 1972, {{< del-val "places_min" >}} en {{< del-val "an_min" >}}. Selon l'ONDPS, les admissions de 2021-2025 dépassent de {{< del-val "hausse_quinquennale" >}}&nbsp;% le numerus clausus total de 2016-2020, passerelles comprises.

Deux ruptures se lisent sur la figure. À partir de 2011 (en partie dès 2010), la série de la DREES ajoute au numerus clausus principal les passerelles et les droits au remords. En 2021, le numerus clausus disparaît et les nombres viennent de l'ONDPS, qui relève les admissions auprès des universités&nbsp;: ce passage n'est pas un saut d'une même mesure.

## Les étudiants soignent-ils avant la fin du cursus&nbsp;? {#avant-la-fin}

Oui, dès l'internat, et les textes l'organisent&nbsp;: l'interne fait ses stages à l'hôpital et en ambulatoire, «&nbsp;{{< del-val "cit_instr_sup" >}}&nbsp;» (instruction interministérielle du 21&nbsp;mai 2026).

La dernière année de médecine générale va plus loin. «&nbsp;{{< del-val "cit_supervision" >}}&nbsp;», en pratique ambulatoire auprès de médecins généralistes, et en priorité dans les zones où l'offre de soins est insuffisante ou l'accès aux soins difficile (code de l'éducation, art.&nbsp;L632-2)&nbsp;; un stage à l'hôpital n'y est possible qu'à titre exceptionnel.

Pendant cette dernière année, l'interne de médecine générale exerce comme docteur junior. «&nbsp;{{< del-val "cit_dj1" >}}&nbsp;» Un praticien peut être appelé à tout moment, et l'acte reste sous sa responsabilité&nbsp;: seul pour l'acte, donc, mais jamais sans recours. Les textes organisent ces soins&nbsp;; ils n'en mesurent pas la part dans l'ensemble des soins.

<details class="repli"><summary>Les textes de l'internat et du docteur junior, cités mot pour mot</summary>

- **L'internat** (instruction du 21&nbsp;mai 2026)&nbsp;: «&nbsp;{{< del-val "cit_instr_interne" >}}&nbsp;»
- **La dernière année** (code de l'éducation, art.&nbsp;L632-2)&nbsp;: «&nbsp;{{< del-val "cit_supervision" >}}&nbsp;», par des praticiens agréés, «&nbsp;{{< del-val "cit_ambu" >}}&nbsp;». L'exception&nbsp;: «&nbsp;{{< del-val "cit_derog" >}}&nbsp;»
- **Les zones** (code de la santé publique, art.&nbsp;L1434-4)&nbsp;: «&nbsp;{{< del-val "cit_zones" >}}&nbsp;»
- **Le docteur junior** (code de la santé publique, art.&nbsp;R6153-1-2)&nbsp;: «&nbsp;{{< del-val "cit_dj1" >}}&nbsp;» «&nbsp;{{< del-val "cit_dj3" >}}&nbsp;» «&nbsp;{{< del-val "cit_dj2" >}}&nbsp;»

</details>

## Combien de temps une réforme du cursus met-elle à s'appliquer&nbsp;? {#epreuve-des-dates}

La quatrième année de médecine générale permet de le vérifier en dates exactes, sans projection.

- **{{< del-val "loi_date" >}}**&nbsp;: la loi de financement de la sécurité sociale pour 2023 crée cette année (art.&nbsp;37), pour les étudiants qui entrent en internat à la rentrée {{< del-val "an_reforme" >}}.
- **{{< del-val "debut_conso" >}}**&nbsp;: date prévue par l'instruction du 21&nbsp;mai 2026 pour l'entrée de ces internes dans leur quatrième année, comme docteurs juniors, «&nbsp;{{< del-val "cit_instr_amb" >}}&nbsp;».
- **À {{< del-val "fin_min" >}} au plus tôt**&nbsp;: fin de cette année, puisque «&nbsp;{{< del-val "cit_instr_diplome" >}}&nbsp;»

**La réforme créée par la loi du {{< del-val "loi_date" >}} doit connaître une première application à la cohorte concernée à la date prévue du {{< del-val "debut_conso" >}}, avec son entrée dans une quatrième année d'internat sous le statut de docteur junior.** Le diplôme de cette cohorte pourra être obtenu au plus tôt à {{< del-val "fin_min" >}}. Ce calendrier établit quand la réforme s'applique et quand le nouveau cursus peut s'achever. Il ne démontre ni un supplément de consultations ni une amélioration de l'accès aux soins. Il faut distinguer cette réforme de la décision d'augmenter les admissions, dont les effets sur le nombre de médecins diplômés suivent une autre chronologie. Le délai d'une réforme et son effet sur les délais ne sont pas non plus la même chose&nbsp;: celle-ci s'applique {{< del-val "moins_quatre" >}} après la loi, et elle allonge d'un an le temps nécessaire pour former un généraliste. Au 12&nbsp;octobre 2026, la première de ces années n'a pas commencé&nbsp;: le calendrier est celui d'un texte d'application, non un fait constaté.

## Quand les patients verront-ils la différence&nbsp;? {#limites}

Aucune série de cette page ne le dit. Le service statistique du ministère de la Santé (DREES) écrivait en 2021 que «&nbsp;{{< del-val "cit_dd76_objet" >}}&nbsp;»&nbsp;: «&nbsp;{{< del-val "cit_dd76" >}}&nbsp;» (*Les Dossiers de la DREES* n°&nbsp;76). Son objet est l'effectif des médecins, la «&nbsp;situation démographique&nbsp;», non les soins&nbsp;: ce délai et les soins donnés par les internes ne se contredisent pas, ils portent sur deux objets différents.

Le nombre de médecins en activité dépend aussi des départs, des choix de spécialité, des lieux d'installation et des médecins diplômés à l'étranger, un effectif présent et non un flux d'arrivées&nbsp;: au 1er&nbsp;janvier 2026, selon la DREES, {{< del-val "etr_p26" >}}&nbsp;% des médecins actifs avaient obtenu leur diplôme à l'étranger, contre {{< del-val "etr_p12" >}}&nbsp;% en 2012. Cela fait {{< del-val "etr_26" >}} médecins sur {{< del-val "tot_26" >}}. Le lieu du diplôme ne dit pas la nationalité, et ce rapprochement ne mesure aucune compensation des capacités de formation françaises.

Cette page ne décrit pas les autres horloges qu'une promesse rencontre, comme la formation des forces de l'ordre ou le temps d'une scolarité, faute d'avoir lu leurs textes. Un cas montre qu'une horloge peut dépasser le mandat&nbsp;; il ne dit pas combien le font.

## Comment juger une promesse qui passe par une formation&nbsp;? {#juger-une-promesse}

Trois questions séparent ce qu'une telle promesse peut changer pendant le mandat de ce qu'elle ne peut que lancer.

1. **L'horloge des textes**&nbsp;: quelle durée de formation la loi impose-t-elle, et depuis quand&nbsp;? Ici, au moins {{< del-val "duree" >}} ans depuis la première année (règles applicables depuis la rentrée {{< del-val "an_reforme" >}}).
2. **L'horloge des capacités**&nbsp;: qui décide du nombre de places, et sont-elles déjà remplies&nbsp;? Ici, chaque université, chaque année, dans le cadre d'un objectif de l'État&nbsp;; selon l'ONDPS, elles sont presque saturées.
3. **L'horloge de l'effet**&nbsp;: qu'est-ce qui agit avant le diplôme, et qu'est-ce qui ne se mesure qu'après&nbsp;? Ici, les internes soignent sous supervision pendant leur formation&nbsp;; l'accès aux soins dépend de facteurs qu'aucune de ces séries ne mesure.

La même grille s'applique à toute promesse dont le résultat passe par des personnes à former, à condition de lire les textes de chaque métier.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="L'horloge d'une promesse" avis="non" >}}
Cette page mesure une horloge&nbsp;: le temps qu'il faut pour former un médecin. Le livre suit une promesse sur l'accès aux soins depuis son énoncé de campagne jusqu'à l'endroit où son résultat échappe à l'élu, et rencontre d'autres horloges en chemin&nbsp;: une cohorte d'élèves, un budget carbone, le temps d'une loi et de ses décrets. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Textes**, lus sur Légifrance (API) et dans le Journal officiel de la DILA&nbsp;: arrêté du 8&nbsp;avril 2013 relatif au régime des études en vue du premier et du deuxième cycle des études médicales, art.&nbsp;1&nbsp;; code de l'éducation, art.&nbsp;L631-1 (version en vigueur et versions entrées en vigueur en 2004, 2010, 2020 et 2023) et L632-2&nbsp;; loi n°&nbsp;2022-1616 du 23&nbsp;décembre 2022 de financement de la sécurité sociale pour 2023, art.&nbsp;37&nbsp;; code de la santé publique, art.&nbsp;R6153-1-2 et L1434-4&nbsp;; Constitution, art.&nbsp;6. Instruction interministérielle n°&nbsp;DGOS/RH2/DGESIP/2026/44 du 21&nbsp;mai 2026 relative à la mise en œuvre de la quatrième année du diplôme d'études spécialisées de médecine générale (*Bulletin officiel* santé), texte d'application non opposable.

**DREES**, *Quelle démographie récente et à venir pour les professions médicales et pharmaceutique&nbsp;?*, Les Dossiers de la DREES n°&nbsp;76, mars 2021, graphique&nbsp;8 (source ONDPS)&nbsp;; démographie des professionnels de santé, RPPS, publication du 2&nbsp;juillet 2026.

**ONDPS**, note de bilan des objectifs nationaux pluriannuels 2021-2025, formation de médecins, sages-femmes, chirurgiens-dentistes et pharmaciens, 19&nbsp;décembre 2025.

**Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_delais.csv), en format long&nbsp;; [JSON](/promesses_delais.json), avec les définitions et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664)&nbsp;; la version archivée précède la refonte du 12&nbsp;octobre 2026.

<details class="repli"><summary>Comment ces chiffres ont été vérifiés, et l'écart qui reste</summary>

Les chiffres, les citations, les contrôles et les figures sont produits par un script unique. Les durées et les citations sont lues dans les textes archivés, la série de la DREES dans son fichier, les dates du calendrier de la quatrième année dans la loi et dans l'instruction. Les admissions de 2021 à 2025 et les totaux par périodes de cinq ans, publiés en image par l'ONDPS, sont transcrits&nbsp;: le script contrôle la somme des admissions annuelles par le total imprimé (une erreur sur une année compensée par une autre passerait), retrouve ce total, les admis et les capacités de 2025 et l'objectif national dans le texte du document, compare les totaux de 2001 à 2015 à la série de la DREES, et vérifie que le total de 2016-2020, lu deux fois sur l'image, redonne la hausse et la moyenne annuelle que le texte imprime. Il s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases.

**Le niveau d'admission des admis de 2021-2025.** La loi prévoit que des candidats «&nbsp;{{< del-val "cit_631_pass" >}}&nbsp;» (code de l'éducation, art.&nbsp;L631-1). L'ONDPS compte les capacités d'accueil en places offertes «&nbsp;{{< del-val "cit_ondps_cae1" >}}&nbsp;» et précise que «&nbsp;{{< del-val "cit_ondps_onp_pass" >}}&nbsp;». Il compare ses admis au numerus clausus total de 2016-2020, qui comprend les passerelles. Il ne publie pas la part des admis entrés en troisième année.

**La hausse de {{< del-val "hausse_quinquennale" >}}&nbsp;%.** Selon l'ONDPS, {{< del-val "admis_2021_2025" >}} étudiants ont été admis en deuxième année ou, par une passerelle, en troisième, de 2021 à 2025. Le numerus clausus total de 2016-2020, passerelles comprises, comptait {{< del-val "admis_2016_2020" >}} places. L'ONDPS compare ainsi des admis à des places, en assimilant le numerus clausus à un nombre d'admissions, hypothèse qu'il juge solide en médecine.

**L'écart entre les deux sources.** La série de la DREES concorde exactement avec les totaux par périodes de cinq ans que publie l'ONDPS pour 2001-2005, 2006-2010 et 2011-2015. Pour 2016-2020, la somme des valeurs de la DREES dépasse de {{< del-val "ecart_2016_2020" >}} places le total de l'ONDPS, soit environ {{< del-val "ecart_pct" >}}&nbsp;% de ce total. Ce total, lu deux fois sur l'image, est le seul des deux qui redonne la hausse de {{< del-val "hausse_quinquennale" >}}&nbsp;% imprimée par l'ONDPS (la somme de la DREES donnerait {{< del-val "hausse_drees" >}}&nbsp;%)&nbsp;: l'écart n'est pas une erreur de lecture. La valeur 2020 de la DREES porte un astérisque dont la légende n'a pas été trouvée. L'écart est publié, il n'est pas corrigé.

</details>

{{< reutiliser figures="figures_delais" jeu="promesses_delais" sources="Légifrance, Bulletin officiel santé, DREES et ONDPS" donnees="Les durées du cursus de médecine générale et du mandat lues dans les textes, les places pourvues du numerus clausus de 1972 à 2020, les admis en deuxième année (ou en troisième par une passerelle) de 2021 à 2025 et les médecins actifs diplômés à l'étranger ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Aux règles applicables aux étudiants entrés en internat à partir de la rentrée {{< del-val "an_reforme" >}}, former un médecin généraliste prend au moins {{< del-val "duree" >}} ans depuis la première année, {{< del-val "nfois" >}} la durée d'un mandat présidentiel&nbsp;; comparaison d'échelle seulement. Le nombre d'étudiants admis en deuxième année se décide sur trois étages&nbsp;: l'objectif de l'État, puis les objectifs et les capacités votés par chaque université. Les places pourvues ont été divisées par {{< del-val "rapport_baisse" >}} entre 1972 et {{< del-val "an_min" >}}, avant de remonter&nbsp;; {{< del-val "admis_2021_2025" >}} étudiants ont été admis en deuxième année (ou en troisième par une passerelle) de 2021 à 2025.
{{< /reutiliser >}}
