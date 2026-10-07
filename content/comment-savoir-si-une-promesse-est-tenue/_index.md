---
title: "Comment savoir si une promesse est tenue ?"
description: "Pour juger « faire baisser le chômage », deux mesures sont particulièrement utilisées : chômeurs au sens du BIT et inscrits en catégorie A à France Travail ne recouvrent pas exactement la même population, et les règles d'inscription ont changé au 1er janvier 2025. Estimation Insee 2024 et séries Dares, données ouvertes."
chapo: "Le chômage comme cas-test : choisir l'indicateur, le point de départ, et vérifier que la règle n'a pas changé. Pour le chômage, deux mesures sont particulièrement utilisées, le chômage au sens du BIT et les inscrits en catégorie A à France Travail ; elles reposent sur des définitions différentes, et leurs populations ne coïncident que partiellement. Depuis 2025, les règles d'inscription à France Travail ont en outre changé, ce qui affecte les comparaisons dans le temps."
date: 2026-10-05
lastmod: 2026-10-05
donnees: [promesses_mesurer]
og_title: "Comment savoir si une promesse est tenue ? — deux mesures du chômage, deux populations — S. Lalut"
og_image: "images/og-mesurer-promesse.jpg"
og_image_alt: "Carte de partage : « Deux mesures, deux populations » — une barre en trois segments, en milliers de personnes, moyenne 2024 : 863 chômeurs au sens du BIT non inscrits en catégorie A, 1 427 dans les deux mesures à la fois, 1 466 inscrits en catégorie A non chômeurs au sens du BIT (estimation Insee)."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html)
  jeu: "promesses_mesurer"
  nom: "Chômage au sens du BIT et inscription en catégorie A : croisement 2024 et séries d'inscrits avec et sans les publics inscrits d'office"
  description: "Restitution, vérifiée contre le PDF publié, du croisement estimé par l'Insee entre statut d'activité au sens du BIT et catégorie d'inscription à France Travail (moyenne 2024, France hors Mayotte, 15-64 ans, logement ordinaire ; Insee Références 2026, dossier 1, figure 2) ; séries trimestrielles CVS-CJO des inscrits en catégorie A et des inscrits en catégorie A hors bénéficiaires du RSA et hors jeunes en parcours (Dares-France Travail, France hors Mayotte, 2018 à 2026)."
  couverture_temporelle: "2018/2026"
  couverture_spatiale: "France hors Mayotte"
  variables:
    - {nom: "Personnes par statut au sens du BIT et catégorie d'inscription", unite: "milliers de personnes (moyenne 2024, estimation)"}
    - {nom: "Inscrits en catégorie A, avec et sans les publics inscrits d'office depuis 2025", unite: "personnes, fin de trimestre, CVS-CJO"}
  sources:
    - "https://www.insee.fr/fr/statistiques/8733119?sommaire=8733125"
    - "https://data.dares.travail-emploi.gouv.fr/explore/dataset/dares_defm_stock_france_cvs_trim/"
  mots: ["chômage", "BIT", "France Travail", "catégorie A", "promesse électorale", "indicateur", "loi pour le plein emploi"]
  fichiers: ["promesses_mesurer.csv", "promesses_mesurer.json"]
  doi: "10.5281/zenodo.23212664"
  apropos: "promesses électorales et institutions politiques françaises"
faq:
  - question: "Quelle est la différence entre le chômage au sens du BIT et les inscrits en catégorie A ?"
    answer: "Ce sont deux définitions. Selon l'Insee, un chômeur au sens du BIT est « une personne âgée de 15 ans ou plus sans emploi, disponible pour en occuper un dans les quinze jours et qui a activement cherché un emploi dans le mois précédent » ; il est mesuré par l'enquête Emploi. La catégorie A de France Travail regroupe « les personnes sans activité au cours du mois et tenues de rechercher un emploi » ; c'est un registre administratif. En 2024, l'Insee estime que {mes.p_a} % des inscrits en catégorie A sont chômeurs au sens du BIT et que {mes.p_b} % des chômeurs au sens du BIT sont inscrits en catégorie A."
  - question: "Pourquoi le nombre d'inscrits en catégorie A a-t-il changé en 2025 ?"
    answer: "Depuis janvier 2025, en application de la loi pour le plein emploi du 18 décembre 2023, les demandeurs et bénéficiaires du RSA, les jeunes suivis par les missions locales en contrat d'engagement jeune ou en Pacea et les personnes handicapées suivies par Cap emploi sont inscrits d'office à France Travail. La Dares, qui publie ces séries, signale d'autres changements la même année (règles d'actualisation, régime des sanctions) et publie une série hors bénéficiaires du RSA et hors jeunes en parcours. L'Autorité de la statistique publique a suspendu la labellisation de ces séries pour la période du 1er janvier 2025 au 20 mai 2026."
  - question: "Comment juger une promesse de baisse du chômage ?"
    answer: "En fixant d'avance l'indicateur (chômage au sens du BIT ou inscrits en catégorie A), le point de comparaison (la date et la valeur de départ) et en vérifiant que la règle de mesure n'a pas changé entre les deux dates ; puis en se demandant quelle part de l'évolution peut honnêtement être attribuée aux décisions de celui qui a promis. Une évolution observée ne suffit pas à établir sa cause."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "promesses"
  rang: 50
  nature: "Estimation Insee et séries Dares, vérifiées et restituées ; données ouvertes"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Comment savoir si une promesse est tenue ?"
  court: "Mesurer"
  role: "indicateurs et ruptures"
---

{{< reutiliser-ancre >}}

«&nbsp;Faire baisser le chômage&nbsp;» est un bon cas-test&nbsp;: avant même d'évaluer le résultat, il faut décider ce que l'on appelle chômage. Deux mesures sont particulièrement utilisées, publiées par deux institutions, selon deux définitions. Cette page reprend l'estimation de l'Insee qui les croise, vérifiée case par case contre le document publié, et la règle d'inscription qui a changé en 2025.

## Que comptent le chômage au sens du BIT et la catégorie A&nbsp;? {#deux-chiffres}

Le premier est le **chômage au sens du Bureau international du travail (BIT)**, mesuré par l'Insee à partir de l'enquête Emploi. Est chômeur, selon l'Insee, «&nbsp;une personne âgée de 15&nbsp;ans ou plus sans emploi, disponible pour en occuper un dans les quinze jours et qui a activement cherché un emploi dans le mois précédent&nbsp;». Le second est le nombre d'**inscrits en catégorie A à France Travail**, tiré d'un registre administratif&nbsp;: la catégorie A regroupe «&nbsp;les personnes sans activité au cours du mois et tenues de rechercher un emploi&nbsp;».

Une enquête et un registre ne voient pas les mêmes personnes&nbsp;: on peut chercher activement un emploi sans être inscrit, et être inscrit sans remplir les critères du BIT. L'Insee, la Dares et France Travail ont apparié les deux sources pour mesurer cet écart.

{{< figure-svg fichier="mesurer-recoupement" alt="Barre en trois segments, en milliers de personnes, moyenne 2024 : à gauche les chômeurs au sens du BIT non inscrits en catégorie A, au centre les personnes comptées dans les deux mesures, à droite les inscrits en catégorie A qui ne sont pas chômeurs au sens du BIT. Une accolade au-dessus regroupe les chômeurs au sens du BIT, une accolade au-dessous les inscrits en catégorie A." >}}Croisement du statut au sens du BIT et de l'inscription à France Travail, moyenne 2024, France hors Mayotte, personnes de 15 à 64&nbsp;ans vivant dans un logement ordinaire. Estimation de l'Insee (appariement Dares-Insee-France Travail).{{< /figure-svg >}}

{{< fig-actions id="recoupement" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** En 2024, selon l'estimation de l'Insee, {{< mes-val "commun_env" >}} de personnes sont comptées dans les deux mesures à la fois&nbsp;; {{< mes-val "a_seul_env" >}} d'inscrits en catégorie A ne sont pas chômeurs au sens du BIT, et {{< mes-val "bit_seul" >}} chômeurs au sens du BIT ne sont pas inscrits en catégorie A&nbsp;: deux définitions, des populations qui se recoupent en partie.

</div>

<details class="repli"><summary>Qui sont ceux qui ne figurent que dans une des deux mesures&nbsp;?</summary>

Parmi les **inscrits en catégorie A qui ne sont pas chômeurs au sens du BIT**, l'Insee compte {{< mes-val "a_halo" >}} personnes dans le «&nbsp;halo autour du chômage&nbsp;» (sans emploi, mais non disponibles dans les deux semaines ou sans démarche active dans le mois), {{< mes-val "a_hors_halo" >}} inactifs hors de ce halo et {{< mes-val "a_emploi" >}} personnes en emploi.

Parmi les **chômeurs au sens du BIT qui ne sont pas inscrits en catégorie A**, {{< mes-val "bit_non_inscrits" >}} ne sont pas inscrits du tout à France Travail, {{< mes-val "bit_bc" >}} sont inscrits en catégorie B ou C (activité réduite dans le mois) et {{< mes-val "bit_de" >}} en catégorie D ou E.

Les parts le disent autrement&nbsp;: {{< mes-val "p_a" >}}&nbsp;% des inscrits en catégorie A sont chômeurs au sens du BIT, et {{< mes-val "p_b" >}}&nbsp;% des chômeurs au sens du BIT sont inscrits en catégorie A.

**Ce qui a été vérifié.** Les effectifs viennent du tableur publié par l'Insee&nbsp;; une seconde extraction, écrite séparément à partir du document PDF publié, retrouve les mêmes 35&nbsp;valeurs (24&nbsp;cases et 11&nbsp;totaux), la même année et le même champ. Les trois ensembles restitués par soustraction égalent ceux que l'Insee imprime dans un autre tableau du même dossier. Ce contrôle vérifie que la page restitue exactement l'estimation publiée&nbsp;; il ne refait pas l'appariement, dont les données individuelles ne sont pas publiques.

</details>

## La règle de comptage des inscrits est-elle restée la même&nbsp;? {#regle-de-mesure}

Non&nbsp;: les règles d'inscription et d'actualisation ont changé à partir de 2025. Depuis janvier 2025, en application de la [loi du 18&nbsp;décembre 2023 pour le plein emploi](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048581935), les demandeurs et bénéficiaires du RSA, les jeunes suivis par les missions locales en contrat d'engagement jeune ou en Pacea et les personnes handicapées suivies par Cap emploi sont **inscrits d'office** à France Travail. La Dares, qui publie ces séries avec France Travail, signale dans ses métadonnées d'autres changements la même année&nbsp;: une actualisation automatique des nouveaux inscrits de janvier à mars 2025, restreinte en avril, un nouveau régime de sanctions en juin, et 36&nbsp;000&nbsp;personnes comptées à tort en catégorie A en mars puis reclassées.

L'[Autorité de la statistique publique](https://www.autorite-statistique-publique.fr/wp-content/uploads/2024/11/Delibere-ASP-statistiques-marche-du-travail_14nov2024_VF.pdf), chargée notamment de la labellisation de statistiques publiques, a **suspendu la labellisation** de ces séries pour la période comprise entre le 1er&nbsp;janvier 2025 et le terme de la labellisation alors en vigueur, le 20&nbsp;mai 2026. Son motif&nbsp;: les changements de règles «&nbsp;rendr[ont] difficilement interprétables les séries statistiques de demandeurs d'emploi jusqu'ici labellisées&nbsp;» (délibération du 14&nbsp;novembre 2024). Le point établi ici est plus étroit&nbsp;: les conditions de production et de lecture de la série ont changé, ce qui affecte les comparaisons dans le temps.

La Dares publie également une série d'inscrits en catégorie A **hors bénéficiaires du RSA et hors jeunes en parcours**, disponible depuis 2018.

**Attention&nbsp;: les niveaux des deux figures de cette page ne sont pas directement comparables.** La première est une moyenne 2024 sur les 15-64&nbsp;ans vivant en logement ordinaire&nbsp;; la seconde est un stock administratif de fin de trimestre, sur un champ différent.

{{< figure-svg fichier="mesurer-regle" alt="Deux panneaux sur la même échelle, de 2018 à 2026 : à gauche la catégorie A publiée, à droite la série hors bénéficiaires du RSA et hors jeunes en parcours ; dans chacun, une ligne en pointillés marque le 1er janvier 2025, changement de règles." >}}Inscrits en catégorie A à France Travail en fin de trimestre, France hors Mayotte, données corrigées des variations saisonnières et des jours ouvrables, avec et sans les bénéficiaires du RSA et les jeunes en parcours. Dernier point&nbsp;: {{< mes-val "dares_fin" >}}.{{< /figure-svg >}}

{{< fig-actions id="regle" >}}

Les deux panneaux décrivent **deux populations différentes**, et la seconde exclut ces publics sur toute la période, avant comme après 2025. Leur écart n'est donc pas l'effet de la réforme, et un faible écart ne prouverait pas un faible effet. L'Insee signale de son côté que les changements de 2025 peuvent aussi affecter les comportements de recherche d'emploi, donc la mesure au sens du BIT&nbsp;: aucune des deux séries n'est un témoin intact de ce qui se serait passé sans la loi.

Sur la mesure au sens du BIT, l'Insee a chiffré la place des publics visés par la loi dans la hausse du chômage&nbsp;: «&nbsp;{{< mes-val "cit_ir192" >}}&nbsp;» (*Informations rapides* n°&nbsp;192, 7&nbsp;août 2026). Il précise aussitôt&nbsp;: «&nbsp;{{< mes-val "cit_ir192_reserve" >}}&nbsp;». C'est donc une contribution comptable, non un effet de la loi. L'Unédic, organisme paritaire qui gère l'assurance chômage, reprend le chiffre en écrivant que «&nbsp;{{< mes-val "cit_unedic" >}}&nbsp;», tout en citant la réserve de l'Insee&nbsp;: le verbe dit plus que la mesure.

## Comment juger une promesse avec ces chiffres&nbsp;? {#juger-une-promesse}

Une promesse de baisse du chômage, prise comme exemple et sans viser personne, se juge en quatre gestes, qui sont les quatre dernières questions de la grille du livre&nbsp;:

1. **Selon quel indicateur&nbsp;?** Chômage au sens du BIT ou inscrits en catégorie A&nbsp;: ils ne recouvrent pas exactement la même population, et l'un ne se substitue pas à l'autre en cours de route.
2. **Par rapport à quel point de comparaison&nbsp;?** La valeur de départ, à une date dite d'avance, et non la date la plus favorable choisie après coup.
3. **La règle qui dira si elle est tenue est-elle restée la même&nbsp;?** Pour les inscrits, non depuis 2025&nbsp;: une comparaison avant et après doit traiter la rupture, ou changer d'indicateur.
4. **Quelle part du résultat peut honnêtement être attribuée à celui qui a promis&nbsp;?** Une évolution observée ne suffit pas à établir sa cause&nbsp;: d'autres facteurs peuvent varier en même temps.

## Ce que cette page ne dit pas {#limites}

Elle ne dit pas laquelle des deux mesures est la bonne&nbsp;: elles répondent à deux questions différentes, l'une sur la situation des personnes, l'autre sur leur inscription. Elle ne dit pas si une politique a fait baisser l'une ou l'autre, ni quel est l'effet de la loi pour le plein emploi&nbsp;: aucune des séries présentées ne le mesure. Le croisement est une **estimation** de l'Insee, pour la moyenne de 2024&nbsp;: il ne décrit pas 2025 ni 2026, que l'appariement ne couvre pas.

{{< appel-livre slug="un-president-peut-il-tenir-ses-promesses" sur="Juger une promesse jusqu'au bout" avis="non" >}}
Cette page montre qu'on ne juge pas une promesse sans choisir son indicateur ni vérifier sa règle. Le livre applique ces questions, et les quatre qui les précèdent — ce qui est promis exactement, qui peut le décider, avec le consentement de qui, dans quel délai —, à neuf promesses écrites, datées et signées, dont une sur l'emploi. Il ne donne aucun conseil de vote.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

**Insee**, *Emploi, chômage, revenus du travail*, Insee Références, édition 2026, dossier 1 (publié le 2&nbsp;juillet 2026), figures&nbsp;2 et 8, définitions et encadré méthodologique&nbsp;; appariement Dares-Insee-France Travail du Fichier historique statistique et de l'enquête Emploi.

**Dares et France Travail**, inscrits à France Travail, stock trimestriel, France, données CVS-CJO, et métadonnées du jeu (mises à jour le 28&nbsp;juillet 2026)&nbsp;: changements de procédure de 2022 et de 2025, catégories F et G, série hors bénéficiaires du RSA et hors jeunes en parcours.

**Autorité de la statistique publique**, délibération du 14&nbsp;novembre 2024 sur les statistiques du marché du travail. **Loi** n°&nbsp;2023-1196 du 18&nbsp;décembre 2023 pour le plein emploi.

Les chiffres, les contrôles et les figures sont produits par un script unique, qui relit les fichiers publiés par l'Insee et la Dares et refuse d'écrire si une donnée cesse de soutenir une phrase&nbsp;; aucun chiffre de cette page n'est saisi à la main. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/promesses_mesurer.csv), en format long&nbsp;; [JSON](/promesses_mesurer.json), avec les définitions et le compte rendu des contrôles. Ce jeu est aussi archivé sur Zenodo, avec les six autres de la même série et leur note de méthode, sous un identifiant permanent à citer&nbsp;: [doi:10.5281/zenodo.23212664](https://doi.org/10.5281/zenodo.23212664).

{{< reutiliser figures="figures_mesurer" jeu="promesses_mesurer" sources="Insee et Dares" donnees="Le croisement 2024 du statut au sens du BIT et de la catégorie d'inscription (24 cases et totaux, en milliers), et les séries trimestrielles des inscrits en catégorie A avec et sans les publics inscrits d'office ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Pour juger une promesse sur le chômage, il faut d'abord choisir son chiffre&nbsp;: en 2024, selon l'estimation de l'Insee, {{< mes-val "commun_env" >}} de personnes sont comptées à la fois comme chômeurs au sens du BIT et comme inscrits en catégorie A, {{< mes-val "a_seul_env" >}} d'inscrits en catégorie A ne sont pas chômeurs au sens du BIT et {{< mes-val "bit_seul" >}} chômeurs ne sont pas inscrits en catégorie A. Depuis le 1er&nbsp;janvier 2025, la loi pour le plein emploi inscrit d'office de nouveaux publics, et la labellisation des séries d'inscrits a été suspendue pour la période du 1er&nbsp;janvier 2025 au 20&nbsp;mai 2026. Une comparaison avant et après doit traiter cette rupture, et une évolution observée ne dit pas sa cause.
{{< /reutiliser >}}
