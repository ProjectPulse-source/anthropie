---
title: "Comment savoir si une promesse est tenue ?"
description: "Juger « faire baisser le chômage » : chômage au sens du BIT et inscrits en catégorie A à France Travail ne comptent pas les mêmes personnes, et la règle de comptage des inscrits a changé en 2022, fin 2024 et 2025. Estimation Insee, séries Dares, données ouvertes."
chapo: "Deux chiffres exacts peuvent raconter deux histoires différentes. En 2024, selon l'Insee, {mes.p_a} % seulement des inscrits en catégorie A à France Travail sont chômeurs au sens du Bureau international du travail (BIT). Et la règle qui compte les inscrits a changé en 2022, à la fin de 2024 et en 2025, tantôt à la baisse, tantôt à la hausse. Pour juger une promesse sur le chômage, quatre questions : selon quel indicateur, depuis quand, la règle est-elle restée la même, quelle part attribuer."
date: 2026-10-05
lastmod: 2026-10-12
donnees: [promesses_mesurer]
og_title: "Comment savoir si une promesse est tenue ? — deux mesures du chômage, deux populations — S. Lalut"
og_image: "images/og-mesurer-promesse.jpg"
og_image_alt: "Carte de partage : « Deux mesures, deux populations » — une barre en trois segments, en milliers de personnes, moyenne 2024 : 863 chômeurs au sens du BIT non inscrits en catégorie A, 1 427 dans les deux mesures à la fois, 1 466 inscrits en catégorie A non chômeurs au sens du BIT (estimation Insee)."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_mesurer"
  nom: "Chômage au sens du BIT et inscription en catégorie A : croisement 2024, séries d'inscrits avec et sans les publics inscrits d'office, série longue 2012-2025"
  description: "Restitution, vérifiée contre le PDF publié, du croisement estimé par l'Insee entre statut d'activité au sens du BIT et catégorie d'inscription à France Travail (moyenne 2024, France hors Mayotte, 15-64 ans, logement ordinaire ; Insee Références 2026, dossier 1, figure 2) ; séries trimestrielles CVS-CJO des inscrits en catégorie A et des inscrits en catégorie A hors bénéficiaires du RSA et hors jeunes en parcours (moyenne trimestrielle des inscrits en fin de mois, Dares-France Travail, France hors Mayotte, 2018 à 2026) ; moyennes annuelles 2012-2025 des deux mesures publiées par l'Insee (même dossier, figure 1) ; ruptures de règle datées."
  couverture_temporelle: "2012/2026"
  couverture_spatiale: "France hors Mayotte"
  variables:
    - {nom: "Personnes par statut au sens du BIT et catégorie d'inscription", unite: "milliers de personnes (moyenne 2024, estimation)"}
    - {nom: "Inscrits en catégorie A, avec et sans les publics inscrits d'office depuis 2025", unite: "personnes, moyenne trimestrielle des inscrits en fin de mois, CVS-CJO"}
    - {nom: "Chômeurs au sens du BIT et inscrits en catégorie A, 2012-2025", unite: "millions de personnes, moyenne annuelle"}
  sources:
    - "https://www.insee.fr/fr/statistiques/8733119?sommaire=8733125"
    - "https://data.dares.travail-emploi.gouv.fr/explore/dataset/dares_defm_stock_france_cvs_trim/"
  mots: ["chômage", "BIT", "France Travail", "catégorie A", "promesse électorale", "indicateur", "loi pour le plein emploi"]
  fichiers: ["promesses_mesurer.csv", "promesses_mesurer.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Quelle est la différence entre le chômage au sens du BIT et les inscrits en catégorie A ?"
    answer: "Ce sont deux définitions. Selon l'Insee, un chômeur au sens du BIT est « {mes.chomeur_bit} » ; il est mesuré par l'enquête Emploi. La catégorie A de France Travail regroupe « {mes.categorie_a} » ; c'est un registre administratif. En 2024, l'Insee estime que {mes.p_a} % des inscrits en catégorie A sont chômeurs au sens du BIT et que {mes.p_b} % des chômeurs au sens du BIT sont inscrits en catégorie A."
  - question: "Pourquoi le nombre d'inscrits en catégorie A a-t-il changé en 2025 ?"
    answer: "Pour plusieurs raisons à la fois, selon la Dares. Depuis janvier 2025, la loi pour le plein emploi du 18 décembre 2023 prévoit l'inscription d'office de plusieurs publics à France Travail ; la Dares cite les demandeurs et bénéficiaires du RSA, les jeunes suivis par les missions locales et les personnes handicapées suivies par Cap emploi ; de janvier à mars 2025, les nouveaux inscrits sans droit à une allocation de France Travail ont été actualisés automatiquement, donc classés en catégorie A ; en juin 2025, le régime des sanctions a changé. La règle avait déjà changé en 2022 et à la fin de 2024, avec deux versions du formulaire d'actualisation. L'Autorité de la statistique publique a suspendu la labellisation de ces séries à partir du 1er janvier 2025."
  - question: "Comment juger une promesse de baisse du chômage ?"
    answer: "En fixant d'avance l'indicateur (chômage au sens du BIT ou inscrits en catégorie A) et le point de comparaison (la date et la valeur de départ), en vérifiant que la règle de mesure n'a pas changé entre les deux dates, puis en se demandant quelle part de l'évolution peut honnêtement être attribuée aux décisions de celui qui a promis. Une évolution observée ne suffit ni à établir sa cause, ni à l'exclure."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "promesses"
  livres: ["un-president-peut-il-tenir-ses-promesses"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 50
  nature: "Estimation Insee et séries Dares, vérifiées et restituées ; données ouvertes"
  refonte: "2026-10-12"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Comment savoir si une promesse est tenue ?"
  court: "Mesurer"
  role: "indicateurs et ruptures"
---

{{< reutiliser-ancre >}}

Quand un candidat promet de «&nbsp;faire baisser le chômage&nbsp;», on croit savoir ce que l'on regardera cinq ans plus tard&nbsp;: le chiffre du chômage. Il y en a au moins deux, publiés par deux institutions selon deux définitions, et ils ne comptent pas les mêmes personnes. Cette page leur pose les quatre questions que le livre adresse à toute promesse de résultat — **selon quel indicateur, depuis quand, la règle est-elle restée la même, quelle part attribuer** — et répond à chacune avec les données publiées par l'Insee et la Dares.

## Selon quel indicateur&nbsp;? Deux mesures, deux populations {#deux-chiffres}

Le premier indicateur est le **chômage au sens du Bureau international du travail (BIT)**, mesuré chaque trimestre par l'Insee à partir de l'enquête Emploi. Est chômeur, selon l'Insee, «&nbsp;{{< mes-val "chomeur_bit" >}}&nbsp;». Le second est le nombre d'**inscrits en catégorie A à France Travail**, l'opérateur public de l'emploi, tiré de son registre&nbsp;: la catégorie A regroupe «&nbsp;{{< mes-val "categorie_a" >}}&nbsp;».

Une enquête mesure une situation&nbsp;; un registre enregistre une démarche et une catégorie administrative, qui dépendent des règles d'inscription. On peut chercher activement un emploi sans être inscrit, et être inscrit sans remplir les critères du BIT. Pour mesurer cet écart, l'Insee, la Dares et France Travail ont apparié les deux sources sur l'année 2024&nbsp;:

{{< figure-svg fichier="mesurer-recoupement" alt="Barre en trois segments, en milliers de personnes, moyenne 2024 : à gauche les chômeurs au sens du BIT non inscrits en catégorie A, au centre les personnes comptées dans les deux mesures, à droite les inscrits en catégorie A qui ne sont pas chômeurs au sens du BIT. Une accolade au-dessus regroupe les chômeurs au sens du BIT, dont 62 % sont inscrits en catégorie A ; une accolade au-dessous regroupe les inscrits en catégorie A, dont 49 % sont chômeurs au sens du BIT." >}}Croisement du statut au sens du BIT et de l'inscription à France Travail, moyenne 2024, France hors Mayotte, personnes de 15 à 64&nbsp;ans vivant dans un logement ordinaire. Estimation de l'Insee (appariement Dares-Insee-France Travail).{{< /figure-svg >}}

{{< fig-actions id="recoupement" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** En 2024, selon l'estimation de l'Insee, {{< mes-val "p_a" >}}&nbsp;% seulement des inscrits en catégorie A sont chômeurs au sens du BIT, et {{< mes-val "p_b" >}}&nbsp;% des chômeurs au sens du BIT sont inscrits en catégorie A.

</div>

Les deux mesures ont en commun {{< mes-val "commun_env" >}} de personnes. Les inscrits en catégorie A qui ne sont pas chômeurs au sens du BIT, {{< mes-val "a_seul_env" >}}, ne sont pas, pour la plupart, des personnes qui travaillent&nbsp;: {{< mes-val "a_emploi" >}} d'entre eux ont un emploi au sens du BIT. Les {{< mes-val "a_sans_emploi" >}} autres sont sans emploi. Parmi eux, {{< mes-val "a_halo" >}} se trouvent dans le «&nbsp;halo autour du chômage&nbsp;»&nbsp;: ils souhaitent travailler, mais ne sont pas disponibles dans les deux semaines ou n'ont pas fait de démarche active dans le mois. Les {{< mes-val "a_hors_halo" >}} restants sont inactifs, hors de ce halo.

<details class="repli"><summary>Ces effectifs sont une estimation d’enquête, dont la marge n’est pas publiée</summary>

L'appariement repose sur les répondants de l'enquête Emploi, et l'Insee attribue à «&nbsp;{{< mes-val "cit_alea" >}}&nbsp;» l'écart entre le nombre d'inscrits qu'il retrouve ainsi et le nombre publié. Les milliers affichés restituent l'estimation&nbsp;; ils n'en donnent pas la précision.

</details>

<details class="repli"><summary>Et les chômeurs au sens du BIT qui ne sont pas inscrits en catégorie A&nbsp;?</summary>

Ils sont {{< mes-val "bit_seul" >}}. Parmi eux, {{< mes-val "bit_non_inscrits" >}} ne sont pas inscrits du tout à France Travail, {{< mes-val "bit_bc" >}} sont inscrits en catégorie B ou C (ils ont travaillé quelques heures dans le mois, ce qui les sort de la catégorie A) et {{< mes-val "bit_de" >}} en catégorie D ou E (inscrits qui ne sont pas tenus de chercher un emploi, par exemple parce qu'ils sont en formation ou en contrat aidé).

</details>

## Depuis quand&nbsp;? Le point de départ change la lecture {#depuis-quand}

Juger une promesse, c'est comparer deux dates. Sur la longue durée, les deux mesures publiées par l'Insee, en moyenne annuelle, ne suivent pas le même chemin&nbsp;:

{{< figure-svg fichier="mesurer-serie-longue" alt="Deux courbes de 2012 à 2025, en millions de personnes : les inscrits en catégorie A, au-dessus, et les chômeurs au sens du BIT, au-dessous. L'écart entre elles s'élargit jusqu'en 2020, se réduit jusqu'en 2024 et augmente de nouveau en 2025. Quatre repères numérotés marquent les changements de règle : réforme de l'assurance chômage de 2019 à 2021, enquête Emploi rénovée en 2021, formulaire d'actualisation en 2022, formulaire de fin 2024 et loi pour le plein emploi en 2025." >}}Chômeurs au sens du BIT et inscrits en catégorie A à France Travail, moyennes annuelles publiées par l'Insee, 2012-2025, France hors Mayotte, 15-64&nbsp;ans. Repères&nbsp;: changements de règle documentés par l'Insee et la Dares.{{< /figure-svg >}}

{{< fig-actions id="serie-longue" >}}

L'écart entre inscrits en catégorie A et chômeurs au sens du BIT est passé de {{< mes-val "ecart_2012" >}} en 2012 à {{< mes-val "ecart_2020" >}} en 2020, l'année de la crise sanitaire. Il est redescendu à {{< mes-val "ecart_2024" >}} en 2024, avant de remonter à {{< mes-val "ecart_2025" >}} en 2025. L'Insee résume la période par le titre de son dossier, «&nbsp;{{< mes-val "cit_insee_titre" >}}&nbsp;», et note pour 2025 que «&nbsp;{{< mes-val "cit_divergent" >}}&nbsp;». Une même période peut donc montrer deux tendances différentes selon l'indicateur retenu.

<details class="repli"><summary>L’écart année par année</summary>

| Année | Écart entre inscrits en catégorie A et chômeurs au sens du BIT (moyenne annuelle) |
|---|---|
| 2012 | {{< mes-val "ecart_2012" >}} |
| 2019 | {{< mes-val "ecart_2019" >}} |
| 2020 | {{< mes-val "ecart_2020" >}} |
| 2021 | {{< mes-val "ecart_2021" >}} |
| 2024 | {{< mes-val "ecart_2024" >}} |
| 2025 | {{< mes-val "ecart_2025" >}} |

Moyennes annuelles publiées par l'Insee (*Emploi, chômage, revenus du travail*, édition 2026, dossier&nbsp;1, figure&nbsp;1).

</details>

Ces mouvements ne tiennent pas seulement au marché du travail&nbsp;: l'Insee en rattache une partie aux règles d'inscription et à la rénovation de l'enquête, repérées sur la figure. Pour juger une promesse, la date de départ se fixe avant de regarder les données, jamais après&nbsp;; c'est pourquoi la figure ne découpe aucun mandat.

## La règle est-elle restée la même&nbsp;? Des changements en sens opposés {#regle-de-mesure}

Non, et pas seulement en 2025. Pour les inscrits, la règle de comptage a changé plusieurs fois depuis 2022. Le registre est tenu par France Travail&nbsp;; les séries sont produites avec la Dares, «&nbsp;{{< mes-val "cit_dares_ssm" >}}&nbsp;» selon l'Insee (celui du ministère du Travail), qui date elle-même ces ruptures, et en chiffre plusieurs, dans ses publications. Voici, pour chacune, son effet sur la catégorie A tel que la source le décrit&nbsp;:

| Date | Ce qui change | Effet sur la catégorie A, selon la source |
|---|---|---|
| 2022 | Nouveau formulaire d'actualisation mensuelle, qui enregistre mieux les heures travaillées | **Baisse**&nbsp;: environ {{< mes-val "rupture_2022" >}} inscrits, reclassés surtout en catégories B et C (Dares) |
| Octobre-novembre 2024 | Formulaire modifié de nouveau | **Hausse**&nbsp;: environ {{< mes-val "formulaire_2024" >}} inscrits (Dares et France Travail) |
| Janvier 2025 | Inscription d'office des publics de la loi pour le plein emploi (RSA, jeunes suivis, personnes handicapées) | **Hausse**&nbsp;: la hausse de 2025 en résulte en partie (Insee) |
| Janvier-mars 2025 | Actualisation automatique des nouveaux inscrits sans droit à une allocation de France Travail | **Hausse** au 1er&nbsp;trimestre (Dares) |
| Avril 2025 | Actualisation automatique réservée aux premières inscriptions | **Baisse** au 2e&nbsp;trimestre (Dares) |
| Juin 2025 | Nouveau régime des sanctions | Moins de radiations des listes (Dares, Insee) |

Le formulaire d'actualisation, par lequel les inscrits déclarent chaque mois leur activité, est celui de France Travail, selon l'Insee&nbsp;; les documents lus ne disent pas qui a décidé ses changements de 2022 et de 2024. L'inscription d'office vient de la loi du 18&nbsp;décembre 2023 pour le plein emploi, votée par le Parlement. Côté enquête, la série du chômage au sens du BIT a été reconstruite après la rénovation de l'enquête Emploi en 2021.

<details class="repli"><summary>Ce que disent les sources, date par date</summary>

- **2019-2021.** La réforme de l'assurance chômage, appliquée de novembre 2019 à décembre 2021, comporte selon l'Insee «&nbsp;{{< mes-val "cit_2019" >}}&nbsp;».
- **2021.** L'enquête Emploi est rénovée&nbsp;; pour le statut au sens du BIT, «&nbsp;{{< mes-val "cit_2021" >}}&nbsp;» (Insee). La série du chômage au sens du BIT est donc, elle aussi, reconstruite.
- **2022.** Un nouveau formulaire d'actualisation mensuelle, qui enregistre mieux les heures travaillées, a selon la Dares «&nbsp;{{< mes-val "cit_2022" >}}&nbsp;»&nbsp;: elle l'estime à environ {{< mes-val "rupture_2022" >}} inscrits en moins en catégorie A entre janvier et novembre 2022, reclassés pour l'essentiel en catégories B et C.
- **Octobre-novembre 2024.** Le formulaire change de nouveau, cette fois à la hausse&nbsp;: «&nbsp;{{< mes-val "cit_2024" >}}&nbsp;», d'environ {{< mes-val "formulaire_2024" >}} personnes au niveau national au 4e&nbsp;trimestre 2024 (Dares et France Travail, publication trimestrielle reprise par la Dreets de Normandie).
- **Janvier 2025.** La loi du 18&nbsp;décembre 2023 pour le plein emploi prévoit l'inscription d'office. Selon la Dares, les demandeurs et bénéficiaires du RSA, les jeunes suivis par les missions locales en contrat d'engagement jeune (CEJ) ou en parcours contractualisé d'accompagnement (Pacea), et les personnes handicapées suivies par Cap emploi, le réseau d'accompagnement spécialisé, sont désormais inscrits systématiquement&nbsp;; pour les personnes déjà au RSA, l'orientation est progressive. Deux catégories nouvelles, F et G, accueillent les personnes orientées en parcours social et celles qui attendent leur orientation.
- **Janvier à avril 2025.** De janvier à mars, les nouveaux inscrits non indemnisables sont actualisés automatiquement, donc classés en catégorie A jusqu'à la signature de leur contrat d'engagement&nbsp;; la règle est restreinte en avril aux premières inscriptions. En mars, un incident fait compter à tort {{< mes-val "incident_2025" >}} personnes en catégorie A, reclassées en catégorie G en avril (Dares).
- **Depuis juin 2025.** Un décret change le régime des sanctions&nbsp;: une «&nbsp;suspension-remobilisation&nbsp;» précède désormais l'éventuelle radiation, ce qui réduit le nombre de radiations (Dares, Insee).

</details>

La Dares publie aussi une série d'inscrits en catégorie A **hors bénéficiaires du RSA et hors jeunes en parcours**, disponible depuis 2018. Elle neutralise ainsi une partie des changements de population liés à la loi, mais ni l'ensemble des publics concernés (les personnes suivies par Cap emploi, par exemple, y restent), ni les modifications des règles d'actualisation.

{{< figure-svg fichier="mesurer-regle" alt="Deux panneaux sur la même échelle, de 2018 à 2026 : à gauche la catégorie A publiée, à droite la série hors bénéficiaires du RSA et hors jeunes en parcours. Une bande grise marque 2022, année du nouveau formulaire d'actualisation ; une ligne en pointillés marque le 1er janvier 2025. Les deux séries montent au premier trimestre 2025 et reculent au deuxième." >}}Inscrits en catégorie A à France Travail, moyenne trimestrielle des inscrits en fin de mois, France hors Mayotte, données corrigées des variations saisonnières et des jours ouvrables, avec et sans les bénéficiaires du RSA et les jeunes en parcours. Dernier point&nbsp;: {{< mes-val "dares_fin" >}}. Ces niveaux ne se comparent pas directement à ceux du croisement de 2024, qui porte sur un autre champ.{{< /figure-svg >}}

{{< fig-actions id="regle" >}}

**La série hors RSA porte elle aussi la rupture de 2025.** Au 1er&nbsp;trimestre 2025, elle saute ({{< mes-val "dares_hors_t1_2025" >}}, contre {{< mes-val "dares_a_t1_2025" >}} pour la série publiée). Au 2e, elle recule ({{< mes-val "dares_hors_t2_2025" >}}, contre {{< mes-val "dares_a_t2_2025" >}}). Ces mouvements sont affectés par l'actualisation automatique de janvier à mars 2025, qui touchait tous les nouveaux inscrits sans droit à une allocation de France Travail et dont la Dares documente l'effet sur la catégorie A. Ils montrent que la série hors RSA et jeunes en parcours n'échappe pas à cette rupture, sans permettre d'attribuer toute son évolution à ce seul mécanisme. Et le point de départ de la comparaison, le 4e&nbsp;trimestre 2024, porte déjà le formulaire modifié en octobre-novembre 2024. Quelle part de la hausse observée en 2025 provient de ce formulaire de fin 2024&nbsp;? Les sources mobilisées ne permettent pas de l'isoler&nbsp;: l'Insee ne fournit pas de décomposition de l'écart entre les deux mesures pour 2025, et l'appariement détaillé porte sur 2024.

Sur l'ensemble de la période, entre le 4e&nbsp;trimestre 2024 et le {{< mes-val "dares_fin" >}}, la catégorie A publiée compte {{< mes-val "dares_a_var" >}} inscrits de plus. La série hors RSA en compte {{< mes-val "dares_a_hors_var" >}} de plus.

<details class="repli"><summary>Les niveaux des deux séries</summary>

| | 4e&nbsp;trimestre 2024 | {{< mes-val "dares_fin" >}} | Variation |
|---|---|---|---|
| Catégorie A publiée | {{< mes-val "dares_a_2024t4" >}} | {{< mes-val "dares_a_fin" >}} | {{< mes-val "dares_a_var" >}} de plus |
| Hors bénéficiaires du RSA et hors jeunes en parcours | {{< mes-val "dares_a_hors_2024t4" >}} | {{< mes-val "dares_a_hors_fin" >}} | {{< mes-val "dares_a_hors_var" >}} de plus |

Le croisement de 2024 est une moyenne annuelle sur les 15-64&nbsp;ans vivant en logement ordinaire&nbsp;; les séries de la Dares sont des moyennes, sur chaque trimestre, des inscrits comptés en fin de mois, sur un champ différent.

</details>

Les deux séries décrivent **deux populations différentes**&nbsp;: leur écart n'est pas l'effet de la réforme, et un faible écart ne prouverait pas un faible effet. Aucune des deux n'est un témoin intact de ce qui se serait passé sans la loi.

Ces séries ne sont plus labellisées depuis le 1er&nbsp;janvier 2025. Le 14&nbsp;novembre 2024, l'[Autorité de la statistique publique](https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/11/Delibere-ASP-statistiques-marche-du-travail_14nov2024_VF.pdf), qui certifie la qualité des statistiques publiques, a suspendu leur label pour le temps qui lui restait à courir. Son motif&nbsp;: les changements de 2025 affectent à la fois le nombre des inscrits et leurs catégories, «&nbsp;{{< mes-val "cit_asp" >}}&nbsp;». Elle demande à la Dares et à France Travail une communication claire et pédagogique pour éviter les mauvaises interprétations&nbsp;; son délibéré ne met en cause ni les chiffres publiés, ni la façon de les produire.

<details class="repli"><summary>Le délibéré de l’Autorité, en citations</summary>

La labellisation des séries d'inscrits «&nbsp;{{< mes-val "cit_asp_2021" >}}&nbsp;». La décision du 14&nbsp;novembre 2024 est de suspendre «&nbsp;{{< mes-val "cit_asp_suspend" >}}&nbsp;». L'Autorité demande aussi un suivi publié des reclassements entre catégories, et s'en tient depuis à un suivi régulier, «&nbsp;{{< mes-val "cit_asp_attente" >}}&nbsp;». Au 28&nbsp;juillet 2026, les métadonnées de la Dares indiquent toujours que l'Autorité «&nbsp;{{< mes-val "cit_dares_label" >}}&nbsp;». Le motif écrit tient à la stabilité et à l'interprétation des séries pendant la mise en place de la loi.

</details>

## Quelle part attribuer&nbsp;? Contribution, effet, et ce que les sources en disent {#quelle-part}

Sur la mesure au sens du BIT, l'Insee a chiffré la place des publics visés par la loi dans la hausse du chômage&nbsp;: «&nbsp;{{< mes-val "cit_ir192" >}}&nbsp;» (*Informations rapides* n°&nbsp;192, 7&nbsp;août 2026). Il assortit ce chiffre de deux réserves&nbsp;: «&nbsp;{{< mes-val "cit_ir192_prudence" >}}&nbsp;», et «&nbsp;{{< mes-val "cit_ir192_reserve" >}}&nbsp;». Ce chiffre porte sur la France y compris Mayotte, tandis que le croisement et les séries de la Dares portent sur la France hors Mayotte.

**Une contribution comptable n'est ni un effet de la loi, ni la preuve d'une absence d'effet.** Elle dit quelle part de la hausse se trouve chez ces publics&nbsp;; elle ne dit pas ce qui l'a provoquée, ni ce qu'aurait été le chômage sans la loi.

Dans son bilan de l'année 2025, l'Insee consacre à la loi un encadré intitulé «&nbsp;{{< mes-val "cit_ve_titre" >}}&nbsp;». Le titre parle d'effets&nbsp;; les chiffres présentés restent des contributions.

<details class="repli"><summary>Ce que dit l’encadré de l’Insee</summary>

Dans cet encadré (*Emploi, chômage, revenus du travail*, édition 2026, Vue d'ensemble, encadré&nbsp;5), l'Insee décrit un mécanisme&nbsp;: «&nbsp;{{< mes-val "cit_ve_recherche" >}}&nbsp;»&nbsp;; cette recherche plus fréquente fait partie, selon lui, de la hausse de leur taux d'activité, qui a pour corollaire celle de leur taux de chômage. Il fait état d'«&nbsp;{{< mes-val "cit_ve_contrib" >}}&nbsp;», et rappelle les limites de toute mesure par enquête&nbsp;: «&nbsp;{{< mes-val "cit_ve_limites" >}}&nbsp;».

</details>

L'Unédic, organisme paritaire qui gère l'assurance chômage, reprend le chiffre de l'Insee en écrivant que «&nbsp;{{< mes-val "cit_unedic" >}}&nbsp;», tout en citant ses réserves&nbsp;: le verbe «&nbsp;expliquer&nbsp;» prête à la contribution un pouvoir explicatif que la mesure n'établit pas. Ni l'Insee ni l'Unédic ne mesurent ce que le chômage aurait été sans la loi&nbsp;; le dire dans un sens ou dans l'autre suppose une évaluation qui n'existe pas encore dans ces publications.

## Juger une promesse&nbsp;: les quatre questions {#juger-une-promesse}

Une promesse de baisse du chômage, prise comme exemple et sans viser personne, se juge en quatre questions, qui sont les quatre dernières de la grille du livre&nbsp;:

1. **Selon quel indicateur&nbsp;?** Chômage au sens du BIT ou inscrits en catégorie A&nbsp;: en 2024, {{< mes-val "p_a" >}}&nbsp;% seulement des seconds sont comptés dans le premier, et l'un ne remplace pas l'autre en cours de route.
2. **Par rapport à quel point de comparaison&nbsp;?** Une date et une valeur dites d'avance&nbsp;: l'écart entre les deux mesures est passé de {{< mes-val "ecart_2020" >}} en 2020 à {{< mes-val "ecart_2024" >}} en 2024, si bien que le choix de l'année de départ peut changer le diagnostic.
3. **La règle qui dira si elle est tenue est-elle restée la même&nbsp;?** Pour les inscrits, non&nbsp;: formulaire de 2022 (environ {{< mes-val "rupture_2022" >}} inscrits de moins en catégorie A), formulaire de fin 2024 (environ {{< mes-val "formulaire_2024" >}} de plus), inscription d'office et actualisation automatique en 2025&nbsp;; pour le chômage au sens du BIT, enquête rénovée en 2021. Une comparaison avant et après nomme ces ruptures, ou change d'indicateur.
4. **Quelle part du résultat peut honnêtement être attribuée à celui qui a promis&nbsp;?** Une contribution n'est pas un effet&nbsp;; une évolution observée ne suffit ni à établir sa cause, ni à l'exclure.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas laquelle des deux mesures est la bonne&nbsp;: l'une décrit la situation des personnes, l'autre leur inscription. Elle ne mesure l'effet d'aucune politique, ni celui de la loi pour le plein emploi. Le croisement est une estimation de l'Insee pour la moyenne de 2024&nbsp;: il ne décrit ni 2025 ni 2026, que l'appariement ne couvre pas.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Juger une promesse jusqu'au bout" avis="non" >}}
Cette page montre qu'on ne juge pas une promesse sans choisir son indicateur ni vérifier sa règle. Le livre applique ces questions, et les quatre qui les précèdent — ce qui est promis exactement, qui peut le décider, avec le consentement de qui, dans quel délai —, à neuf promesses écrites, datées et signées, dont une sur l'emploi. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Insee**, *Emploi, chômage, revenus du travail*, Insee Références, édition 2026 (publiée le 2&nbsp;juillet 2026)&nbsp;: dossier&nbsp;1, figures&nbsp;1, 2 et 8, définitions, encadrés et sources (appariement Dares-Insee-France Travail du Fichier historique statistique et de l'enquête Emploi)&nbsp;; Vue d'ensemble, encadré&nbsp;5. *Informations rapides* n°&nbsp;192, 7&nbsp;août 2026.

**Dares et France Travail**, inscrits à France Travail, stock trimestriel, France, données CVS-CJO, et métadonnées du jeu (mises à jour le 28&nbsp;juillet 2026)&nbsp;: changements de procédure de 2022 et de 2025, catégories F et G, série hors bénéficiaires du RSA et hors jeunes en parcours. Formulaire d'actualisation d'octobre-novembre 2024&nbsp;: avertissement de la publication trimestrielle du 4e&nbsp;trimestre 2024 (Dreets de Normandie, source France Travail-Dares).

**Autorité de la statistique publique**, délibéré du 14&nbsp;novembre 2024 sur les statistiques du marché du travail. **Loi** n°&nbsp;2023-1196 du 18&nbsp;décembre 2023 pour le plein emploi. **Unédic**, «&nbsp;Comprendre le chômage au sens du BIT&nbsp;».

**Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_mesurer.csv), en format long&nbsp;; [JSON](/promesses_mesurer.json), avec les définitions, les ruptures datées et le compte rendu des contrôles. Une version antérieure de ce jeu, sans la série longue, est archivée sur Zenodo avec les six autres de la même série et leur note de méthode, sous un identifiant permanent&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

<details class="repli"><summary>Comment ces chiffres ont été vérifiés</summary>

Les effectifs du croisement viennent du tableur publié par l'Insee&nbsp;; une seconde extraction, écrite séparément à partir du document PDF publié, retrouve les mêmes 35&nbsp;valeurs (24&nbsp;cases et 11&nbsp;totaux), la même année et le même champ, et les trois ensembles restitués par soustraction égalent ceux que l'Insee imprime dans un autre tableau du même dossier. Les écarts de la série longue égalent ceux que l'Insee écrit dans le texte du dossier. Ces contrôles vérifient que la page restitue exactement ce qui est publié&nbsp;; ils ne refont pas l'appariement, dont les données individuelles ne sont pas publiques.

Les chiffres, les passages cités, les contrôles et les figures sont produits par un script unique, qui relit les fichiers publiés par l'Insee, la Dares, l'Autorité de la statistique publique, l'Unédic et la Dreets de Normandie, archivés le 12&nbsp;octobre 2026, et s'arrête si une donnée relue ne remplit plus les conditions dont dépendent les principales phrases&nbsp;; chaque passage cité et chaque nombre de la chronologie sont retrouvés mot pour mot dans ces fichiers, et seules les dates de la chronologie sont écrites dans le texte. Les données Dares sont celles de la mise à jour du 28&nbsp;juillet 2026&nbsp;; une publication postérieure n'entre qu'après un nouveau relevé.

</details>

{{< reutiliser figures="figures_mesurer" jeu="promesses_mesurer" sources="Insee et Dares" donnees="Le croisement 2024 du statut au sens du BIT et de la catégorie d'inscription (24 cases et totaux, en milliers), les séries trimestrielles des inscrits en catégorie A avec et sans les publics inscrits d'office, et les moyennes annuelles 2012-2025 des deux mesures ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Pour juger une promesse sur le chômage, il faut d'abord choisir son chiffre&nbsp;: en 2024, selon l'estimation de l'Insee, {{< mes-val "p_a" >}}&nbsp;% seulement des inscrits en catégorie A sont chômeurs au sens du BIT. Il faut ensuite vérifier la règle&nbsp;: le comptage des inscrits a changé en 2022 (environ {{< mes-val "rupture_2022" >}} inscrits de moins en catégorie A), à la fin de 2024 (environ {{< mes-val "formulaire_2024" >}} de plus) et en 2025 (inscription d'office, actualisation automatique), et ces séries ne sont plus labellisées depuis le 1er&nbsp;janvier 2025. Une contribution n'est pas un effet, et une évolution observée ne dit pas sa cause.
{{< /reutiliser >}}
