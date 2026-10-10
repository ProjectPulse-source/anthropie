---
title: "Les élèves maîtrisent-ils moins bien la langue française ?"
description: "Dictée, lecture, vocabulaire, plaisir de lire, écrans : ce que mesurent vraiment les enquêtes. À la même dictée de CM2, {lan.tot87} erreurs en 1987, {lan.tot21} en 2021, mais l'orthographe des mots passe seulement de {lan.lex87} à {lan.lex21} erreurs. Les reculs les plus anciens précèdent la généralisation du smartphone. Données DEPP, OCDE, IEA, ministère de la Culture, recalculées."
chapo: "Pas d'un bloc. Les reculs les plus anciens, ceux de l'orthographe et de la lecture en fin d'école et du temps que les jeunes de 15 ans passent à lire pour leur plaisir, précèdent la généralisation du smartphone chez les adolescents. À la même dictée de CM2, les élèves faisaient {lan.tot87} erreurs en 1987 et {lan.tot21} en 2021 ; mais l'orthographe des mots eux-mêmes ne compte que pour une petite part de cette hausse ({lan.lex87} erreurs, puis {lan.lex21}) : c'est surtout l'orthographe grammaticale qui recule. PISA, à 15 ans, ne baisse qu'après 2012, quand d'autres évaluations, à l'école et en fin de collège, ne reculent pas significativement sur des périodes qui recouvrent en partie cette baisse. Quant au vocabulaire des élèves, aucune des séries publiques recensées ne permet de suivre son évolution."
date: 2026-10-09T00:00:00+02:00
lastmod: 2026-10-10
og_title: "Les élèves maîtrisent-ils moins bien la langue française ? Dictée, lecture, vocabulaire, écrans — S. Lalut"
og_image: "images/og-langue-eleves.jpg"
og_image_alt: "Carte de partage : « Les élèves maîtrisent-ils moins bien la langue française ? » — à la même dictée de CM2, nombre moyen d'erreurs de 1987 à 2021 : les erreurs d'orthographe des mots, en bleu, bougent peu ; les autres erreurs, en orange, ont presque doublé."
# Troisième onglet du bloc École et lycée, né d'une question de l'auteur (09/10/2026 : vocabulaire, lecture, numérique).
# Recherche : D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_LECTURE_2026-10-09 (plan contre-analysé et arbitré, protocole écrit avant
# calcul, commit ddab2bc ; verdict ; contrôle de seconde lecture ; pièces archivées avec empreintes). Aucun chiffre saisi :
# jetons {lan.*} et shortcode lan-val (scripts/update_langue_eleves.py, extrait figé et empreintes dans
# scripts/sources_langue_eleves/). Français seulement : langue, programmes et statistique français (exclusion déclarée).
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée)
donnees: [langue_eleves]
dataset:
  jeu: "langue_eleves"
  nom: "Maîtrise de la langue des élèves en France : dictée et lecture en CM2 depuis 1987, CEDRE, PIRLS, évaluations de sixième, test de seconde, PISA, lecture pour le plaisir, enquêtes Pratiques culturelles, numérique de loisir"
  description: "Séries officielles reprises et recalculées : nombre moyen d'erreurs à la même dictée de CM2 (1987-2021), dont erreurs lexicales ; lecture en CM2 aux épreuves de 1987 ; CEDRE fin d'école (2003-2021) et fin de collège (2015-2021) avec leur significativité ; PIRLS CM1 ; évaluation de début de sixième (2017-2025) et maîtrise par domaine en 2025 ; test de positionnement de seconde ; PISA, compréhension de l'écrit (2000-2025), temps de lecture pour le plaisir et indice de plaisir de lire ; lecteurs de 15-24 ans (1973-2008) ; équipement en smartphone des 12-17 ans ; numérique de loisir déclaré dans PISA 2022 et 2025 (calcul sur les données individuelles)."
  couverture_temporelle: "1973/2025"
  couverture_spatiale: "France"
  variables:
    - {nom: "Erreurs à la dictée de CM2", unite: "erreurs (moyenne)", description: "total et erreurs lexicales, 1987, 2007, 2015, 2021 (DEPP)"}
    - {nom: "Score CEDRE, maîtrise de la langue", unite: "points", description: "fin d'école 2003-2021, fin de collège 2015-2021, avec la significativité publiée par la DEPP"}
    - {nom: "Score PISA en compréhension de l'écrit", unite: "points", description: "France, 2000-2025, avec erreurs types (OCDE)"}
    - {nom: "Lecture pour le plaisir", unite: "heures par semaine ; indice ; %", description: "PISA 2000, 2009, 2018 (OCDE) ; élèves de la sixième à la seconde en 2023 (DEPP)"}
    - {nom: "Numérique de loisir déclaré", unite: "% des élèves", description: "PISA 2022 et 2025, France, données individuelles, avec la non-réponse"}
  sources:
    - "https://www.education.gouv.fr/depp"
    - "https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en.html"
    - "https://www.oecd.org/en/publications/21st-century-readers_a83d84cb-en.html"
    - "https://pirls2021.org/"
    - "https://www.culture.gouv.fr/Thematiques/Etudes-et-statistiques"
    - "https://www.credoc.fr/"
  mots: ["maîtrise de la langue", "vocabulaire", "orthographe", "dictée", "lecture", "plaisir de lire", "écrans", "smartphone", "PISA", "PIRLS", "CEDRE", "DEPP", "élèves", "lycée"]
  fichiers: ["langue_eleves.csv", "langue_eleves.json"]
  apropos: "maîtrise de la langue française par les élèves en France"
faq:
  - question: "Les élèves font-ils plus de fautes qu'avant ?"
    answer: "Oui. À la même dictée de CM2, les élèves faisaient {lan.tot87} erreurs en moyenne en 1987, {lan.tot07} en 2007, {lan.tot15} en 2015 et {lan.tot21} en 2021 ; la hausse de 1987 à 2007 est significative selon la DEPP, et elle est deux fois moins forte de 2015 à 2021 que de 2007 à 2015. L'orthographe des mots eux-mêmes ne compte que pour une petite part de cette hausse : {lan.lex87} erreurs lexicales en 1987, {lan.lex21} en 2021. Les autres erreurs passent de {lan.aut87} à {lan.aut21} ; selon la DEPP, ce sont principalement les erreurs grammaticales, accords et conjugaison, qui ont augmenté."
  - question: "Les jeunes n'utilisent-ils plus que 400 mots ?"
    answer: "Ce chiffre ne repose sur aucune étude retrouvée, et il ne dit pas ce qu'il compte : mots employés, reconnus, compris en contexte. Parmi les sources publiques françaises recensées, aucune série ne permet de suivre l'évolution du vocabulaire des élèves : l'évaluation CEDRE publie un score unique de maîtrise de la langue, le test de lexique de sixième change de questions d'une année à l'autre, et celui de seconde n'existe qu'en voie professionnelle, depuis 2025."
  - question: "Les écrans expliquent-ils la baisse de la lecture ?"
    answer: "Les données ne permettent pas de le dire. Plusieurs reculs sont antérieurs à la généralisation du smartphone chez les adolescents (plus de la moitié des 12-17 ans en sont équipés en {lan.smart_seuil}) : l'orthographe à la dictée de 1987 à 2007, la lecture en CM2 de 1997 à 2007, le temps de lecture pour le plaisir à 15 ans de 2000 à 2009. Cette chronologie exclut seulement que la généralisation du smartphone soit la seule cause de ces reculs ; elle ne dit rien de ses premiers usages. Entre 2022 et 2025, l'évolution du numérique de loisir des jeunes de 15 ans reste indéterminée : la part qui ne répond plus à la question a presque doublé, et ces élèves ont des scores très inférieurs aux autres."
  - question: "Les élèves lisent-ils moins pour leur plaisir ?"
    answer: "À 15 ans, le temps de lecture pour le plaisir, estimé par l'OCDE à partir des réponses des élèves, a baissé significativement de 2000 à 2009 ({lan.h00} puis {lan.h09} heures par semaine), sans évolution significative ensuite ; l'indice de plaisir de lire de l'OCDE a baissé significativement de 2009 à 2018, et la part des élèves qui ne lisent que s'ils y sont obligés est passée de {lan.obl09} % à {lan.obl18} %. En 2023, {lan.np6} % des élèves de sixième déclarent ne pas lire pour leur plaisir, {lan.np2gt} % en seconde générale et technologique et {lan.np2pro} % en seconde professionnelle."
  - question: "Le niveau en français baisse-t-il à tous les âges ?"
    answer: "Les évaluations ne disent pas toutes la même chose. PISA, à 15 ans, recule depuis 2012 ({lan.pisa12} points en 2012, {lan.pisa25} en 2025). Sur des périodes qui recouvrent en partie cette baisse, PIRLS en CM1 et CEDRE en fin de collège ne montrent pas d'évolution significative, CEDRE en fin d'école progresse significativement, et l'évaluation de début de sixième reste au-dessus de 2017. Ces enquêtes ne mesurent ni les mêmes compétences ni les mêmes élèves, et aucune ne suit les mêmes élèves d'un âge à l'autre : elles ne permettent pas de dire à quel âge un recul commencerait."
  - question: "Les manuels de lecture se sont-ils simplifiés ?"
    answer: "Personne ne peut le dire aujourd'hui pour la France : aucune mesure publiée n'a été retrouvée, et il manque la liste des manuels publiés d'où tirer un échantillon. La base Emmanuelle, qui recense les manuels scolaires depuis 1789, ne couvre pas encore le français, et le catalogue de la BnF ne signale pas les manuels comme tels : une recherche par le titre manque toutes les notices des méthodes Daniel et Valérie et Rémi et Colette, des années 1970, et retrouve en partie Taoki, des années 2010. Les textes encore protégés ne peuvent en outre être analysés automatiquement qu'à défaut d'opposition de leurs ayants droit."
ressource:
  bloc: "ecole"
  rang: 30
  nature: "Séries officielles reprises et recalculées (DEPP, OCDE, IEA, Culture, CREDOC) ; protocole écrit avant calcul"
onglet:
  long: "Les élèves maîtrisent-ils moins bien la langue ?"
  court: "Langue"
  role: "Dictée, lecture, vocabulaire, écrans"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Relevé du&nbsp;: {{< lan-val "date_donnees" >}}</span> DEPP&nbsp;: Notes d'Information 98.39, 08.38, 16.20, 22.28, 22.29, 22.37, 25.66, 26.21, 26.22&nbsp;; OCDE&nbsp;: PISA 2025, <em>21st-Century Readers</em>&nbsp;; IEA&nbsp;: PIRLS&nbsp;; ministère de la Culture&nbsp;; CREDOC. Télécharger&nbsp;: <a href="/langue_eleves.csv">CSV</a> · <a href="/langue_eleves.json">JSON</a> · <a href="#sources">méthode</a></p>

## La langue des élèves recule-t-elle d'un bloc&nbsp;? {#chronologie}

<figure class="figure-ciseau">
  <img src="/img/langue-chronologie.svg" alt="Frise de 1985 à 2025, une ligne par mesure de la langue des élèves, avec le sens de chaque intervalle et un repère en {{< lan-val "smart_seuil" >}}, année où plus de la moitié des 12-17 ans ont un smartphone. Reculs significatifs avant ce repère : dictée de CM2 de 1987 à 2007, lecture en CM2 de 1997 à 2007, temps de lecture pour le plaisir à 15 ans de 2000 à 2009. PISA, compréhension de l'écrit, sans baisse significative de 2000 à 2012, en recul significatif de 2012 à 2025. Sur la période récente : PIRLS en CM1 sans évolution significative de 2016 à 2021, CEDRE fin d'école en hausse significative de 2015 à 2021, CEDRE fin de collège sans évolution significative, sixième en hausse puis en léger recul sans test publié." width="720" height="476" loading="lazy">
  <figcaption>Sens de chaque intervalle pour onze mesures de la langue des élèves, chacune dans sa propre échelle (DEPP, OCDE, IEA, ministère de la Culture, CREDOC).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** Les reculs les plus anciens (orthographe et lecture en fin d'école, temps de lecture pour le plaisir à 15 ans) précèdent la généralisation du smartphone chez les adolescents&nbsp;; PISA ne baisse qu'après 2012, quand PIRLS et CEDRE ne reculent pas significativement sur des périodes qui recouvrent en partie cette baisse.

</div>

Onze mesures, onze histoires qui ne se superposent pas. Le repère est celui de la généralisation du smartphone&nbsp;: {{< lan-val "smart11" >}}&nbsp;% des 12-17 ans en étaient équipés en 2011, {{< lan-val "smart13" >}}&nbsp;% en {{< lan-val "smart_seuil" >}}, première année où ils sont plus de la moitié (CREDOC). Trois reculs sont acquis avant cette date&nbsp;: à la même dictée de CM2, le nombre d'erreurs a augmenté significativement de 1987 à 2007&nbsp;; aux mêmes épreuves de lecture, les élèves de CM2 étaient stables de 1987 à 1997, puis ont perdu {{< lan-val "lcm2_07" >}}&nbsp;écart-type de 1997 à 2007&nbsp;; à 15 ans, le temps de lecture pour le plaisir est passé de {{< lan-val "h00" >}} à {{< lan-val "h09" >}}&nbsp;heures par semaine entre 2000 et 2009, une baisse significative selon l'OCDE, qui estime ces heures à partir des classes de réponse des élèves.

PISA raconte autre chose. En compréhension de l'écrit, la France était à {{< lan-val "pisa00" >}}&nbsp;points en 2000 et à {{< lan-val "pisa12" >}} en 2012&nbsp;; elle recule ensuite à chaque enquête, jusqu'à {{< lan-val "pisa25" >}} en 2025, soit {{< lan-val "pisa_v12" >}}&nbsp;points de moins qu'en 2012. Sur des périodes qui recouvrent en partie cette baisse, les autres évaluations ne reculent pas significativement&nbsp;: PIRLS en CM1 passe de {{< lan-val "pirls16" >}} à {{< lan-val "pirls21" >}}&nbsp;points entre 2016 et 2021, sans évolution significative&nbsp;; l'évaluation CEDRE de fin d'école, stable de 2003 à 2015, progresse significativement en 2021 ({{< lan-val "ce15" >}} puis {{< lan-val "ce21" >}})&nbsp;; celle de fin de collège passe de {{< lan-val "cc15" >}} à {{< lan-val "cc21" >}}, sans évolution significative. L'évaluation de début de sixième, passée par tous les élèves, est à {{< lan-val "six25" >}}&nbsp;points en 2025, au-dessus de 2017 ({{< lan-val "six17" >}}) mais sous son sommet de 2020-2021 ({{< lan-val "six21" >}}). L'OCDE fait le même constat pour PIRLS&nbsp;: la France figure parmi les pays dont les résultats PISA baissent malgré des résultats PIRLS stables. Le test d'entrée en seconde générale et technologique, enfin, revient en 2025 à son niveau de 2019 ({{< lan-val "sec25" >}}), après un sommet en 2020-2021 ({{< lan-val "sec21" >}}).

Ce que cette chronologie permet de dire est étroit. Un recul acquis avant {{< lan-val "smart_seuil" >}} ne peut pas avoir pour seule cause la généralisation du smartphone&nbsp;; il ne dit rien des autres formes du numérique, ni des premiers usages du smartphone, ni de son effet par la suite. Et les mesures ne se comparent que par le sens de leur tendance&nbsp;: âges, compétences, enjeux et années diffèrent, et aucune ne suit les mêmes élèves d'un âge à l'autre&nbsp;: elles ne disent pas à quel âge un recul commencerait.

<details class="repli">
<summary>Le verdict série par série, et ce qui ne peut pas être conclu</summary>

- **Dictée de CM2**&nbsp;: hausse significative des erreurs de 1987 à 2007 (DEPP)&nbsp;; hausse ensuite, sans test publié, deux fois moins forte de 2015 à 2021 que de 2007 à 2015. Recul antérieur au smartphone&nbsp;: établi.
- **Lecture en CM2, épreuves de 1987**&nbsp;: stable de 1987 à 1997, baisse significative de 1997 à 2007. Recul antérieur&nbsp;: établi.
- **PISA, compréhension de l'écrit**&nbsp;: aucune baisse significative entre 2000 et 2012 ({{< lan-val "pisa00" >}} puis {{< lan-val "pisa12" >}}), un creux en 2006 sans tendance&nbsp;; baisse significative de 2012 à 2025. Pas de recul antérieur.
- **PIRLS, CM1**&nbsp;: {{< lan-val "pirls01" >}} en 2001, {{< lan-val "pirls11" >}} en 2011, {{< lan-val "pirls16" >}} en 2016&nbsp;; la DEPP publie la significativité des écarts à cinq, dix et quinze ans comptés depuis 2016, pas celle de 2001 à 2011&nbsp;: non identifiable.
- **Livres lus par les 15-24 ans**&nbsp;: la part qui lit vingt livres ou plus dans l'année passe de {{< lan-val "cul88" >}}&nbsp;% en 1988 à {{< lan-val "cul08" >}}&nbsp;% en 2008 (enquêtes Pratiques culturelles, après la rupture de série de 1981-1988)&nbsp;; aucune erreur type publiée&nbsp;: montré sans verdict.

</details>

## Les élèves connaissent-ils moins de mots&nbsp;? {#vocabulaire}

Aucune des séries publiques françaises recensées ici ne permet de le dire&nbsp;: l'évaluation CEDRE note la grammaire, le vocabulaire, l'orthographe et la conjugaison, mais n'en publie qu'un score global par année&nbsp;; l'évaluation de sixième contient un test de lexique dont les questions changent d'une année à l'autre&nbsp;; le test de seconde n'en a un qu'en voie professionnelle, et depuis 2025 seulement. Le chiffre souvent cité selon lequel les jeunes n'utiliseraient plus que quelques centaines de mots ne repose sur aucune étude retrouvée, et il ne dit pas ce qu'il compte&nbsp;: mots employés spontanément, reconnus, compris en contexte, ou disponibles pour s'exprimer avec précision.

Ce qui est mesuré dans la durée, c'est l'orthographe d'une même dictée, et elle répond en partie à la question.

<figure class="figure-ciseau">
  <img src="/img/langue-dictee.svg" alt="Barres empilées, nombre moyen d'erreurs à la même dictée de CM2 : en 1987, {{< lan-val "lex87" >}} erreurs lexicales et {{< lan-val "aut87" >}} autres erreurs, {{< lan-val "tot87" >}} au total ; en 2007, {{< lan-val "lex07" >}} et {{< lan-val "aut07" >}}, {{< lan-val "tot07" >}} ; en 2015, {{< lan-val "lex15" >}} et {{< lan-val "aut15" >}}, {{< lan-val "tot15" >}} ; en 2021, {{< lan-val "lex21" >}} et {{< lan-val "aut21" >}}, {{< lan-val "tot21" >}}." width="720" height="412" loading="lazy">
  <figcaption>Nombre moyen d'erreurs à la même dictée de 67 mots, élèves de CM2 du public (DEPP, Note d'Information 22.37).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** À la même dictée, l'orthographe des mots eux-mêmes bouge peu ({{< lan-val "lex87" >}} erreurs en 1987, {{< lan-val "lex21" >}} en 2021)&nbsp;; ce sont les autres erreurs, surtout grammaticales, qui ont presque doublé ({{< lan-val "aut87" >}} puis {{< lan-val "aut21" >}}).

</div>

Les mots usuels de la dictée, «&nbsp;soir&nbsp;», «&nbsp;maison&nbsp;», «&nbsp;chien&nbsp;», restent écrits correctement par plus de neuf élèves sur dix. Ce qui se perd, c'est l'orthographe grammaticale&nbsp;: l'accord du verbe avec son sujet, de l'adjectif, du participe passé. Pour 1987 et 2007, la DEPP a publié le détail des erreurs par type&nbsp;: les erreurs grammaticales passent de {{< lan-val "gram87" >}} à {{< lan-val "gram07" >}}, quand le total va de {{< lan-val "tot87" >}} à {{< lan-val "tot07" >}}, et la ponctuation ne progresse pas&nbsp;; «&nbsp;ce sont principalement les erreurs grammaticales qui ont augmenté&nbsp;». La part des élèves qui font vingt-cinq erreurs ou plus a quadruplé, de {{< lan-val "bcp87" >}}&nbsp;% à {{< lan-val "bcp21" >}}&nbsp;%, et celle des élèves qui en font deux ou moins est tombée de {{< lan-val "peu87" >}}&nbsp;% à {{< lan-val "peu21" >}}&nbsp;%. Selon la DEPP, la baisse sur les accords n'a porté que sur la période 1987-2015&nbsp;: elle ne se poursuit pas en 2021. Ce constat ne mesure pas le vocabulaire&nbsp;: écrire correctement un mot dicté n'est pas le connaître ni l'employer. Il montre que le recul le mieux documenté porte sur la grammaire de la phrase plus que sur l'orthographe des mots.

Le seul test de lexique récent dit autre chose, sur les écarts plutôt que sur l'évolution. En début de sixième, en 2025, {{< lan-val "lex_sat" >}}&nbsp;% des élèves ont une maîtrise satisfaisante du lexique&nbsp;: {{< lan-val "lex_ips1" >}}&nbsp;% dans les collèges qui accueillent les élèves les plus défavorisés, {{< lan-val "lex_ips5" >}}&nbsp;% dans les plus favorisés. Parmi les cinq domaines de français évalués, c'est en lexique que cet écart est le plus grand.

## Les textes qu'on donne à lire se sont-ils simplifiés&nbsp;? {#textes}

La question revient souvent avec celle du vocabulaire&nbsp;: les livres donnés aux enfants, à commencer par les manuels de lecture, emploieraient moins de mots, et de plus simples. Pour les manuels français, aucune mesure publiée de cette évolution n'a été retrouvée, et il n'est pas possible aujourd'hui d'en construire une solide. Mesurer une évolution suppose de tirer, pour chaque période, un échantillon représentatif des manuels publiés&nbsp;; cette liste n'existe pas pour le français. La base Emmanuelle de la bibliothèque Diderot (ENS de Lyon), qui recense les manuels scolaires publiés en France depuis 1789, couvre {{< lan-val "emma_ndisc" >}}&nbsp;disciplines, des langues anciennes à la géographie, mais pas le français, dont la saisie est annoncée en cours&nbsp;; interrogée le {{< lan-val "tx_date" >}}, elle ne contient pas la méthode *Daniel et Valérie*. Le catalogue de la BnF, lui, ne signale pas les manuels comme tels, et une recherche par le titre ne retrouve pas les mêmes livres selon les époques. Les méthodes *Daniel et Valérie* ({{< lan-val "dv_cat" >}}&nbsp;notices au catalogue) et *Rémi et Colette* ({{< lan-val "rc_cat" >}}), des années 1970, échappent entièrement à une recherche des titres qui associent «&nbsp;lecture&nbsp;» à un niveau de classe, quand *Taoki*, des années 2010, y est retrouvé en partie ({{< lan-val "taoki_r1" >}}&nbsp;notices sur {{< lan-val "taoki_cat" >}}). Un corpus composé ainsi changerait de nature d'une décennie à l'autre, et ce changement suffirait à fabriquer une tendance.

Le droit borne aussi l'exercice. En règle générale, un manuel dont un auteur est mort il y a moins de soixante-dix ans reste protégé&nbsp;; la fouille automatique de son texte n'est permise qu'à défaut d'opposition de ses ayants droit (code de la propriété intellectuelle, article L.&nbsp;122-5-3), et la Société des gens de lettres publie depuis avril 2026 une liste des œuvres dont les auteurs s'y opposent. Pour les livres anciens numérisés par la BnF, les conditions de Gallica ne rendent cette fouille gratuite que pour la recherche académique à but non lucratif. Répondre demanderait donc d'abord de recenser les manuels de français, comme Emmanuelle l'a fait pour d'autres disciplines, puis de tirer au sort des ouvrages en nombre suffisant&nbsp;: pour déceler entre deux périodes un écart d'un écart-type, il faut déjà {{< lan-val "n_d1" >}}&nbsp;ouvrages par période et par niveau, et {{< lan-val "n_d05" >}} pour un écart deux fois plus petit. C'est un travail d'équipe de recherche, avec l'accès des bibliothèques qui conservent ces manuels.

## Les élèves lisent-ils moins pour leur plaisir&nbsp;? {#plaisir}

<figure class="figure-ciseau">
  <img src="/img/langue-plaisir.svg" alt="Barres, part des élèves qui déclarent ne pas lire pour leur plaisir en 2023 : sixième {{< lan-val "np6" >}} %, quatrième {{< lan-val "np4" >}} %, seconde générale et technologique {{< lan-val "np2gt" >}} %, seconde professionnelle {{< lan-val "np2pro" >}} %, première année de CAP {{< lan-val "npcap" >}} %." width="720" height="304" loading="lazy">
  <figcaption>Part des élèves qui déclarent ne pas lire pour leur plaisir, selon la classe, septembre 2023 (DEPP, Note d'Information 25.66).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** En 2023, un élève de sixième sur huit déclare ne pas lire pour son plaisir&nbsp;; ils sont {{< lan-val "np2gt" >}}&nbsp;% en seconde générale et technologique et près de la moitié en seconde professionnelle.

</div>

Cette enquête, menée auprès de tous les élèves de quatre niveaux, compare des élèves différents la même année&nbsp;: elle décrit un écart entre les âges et les filières, pas une évolution. L'évolution, c'est PISA qui la donne, à 15 ans. Le temps de lecture pour le plaisir, estimé par l'OCDE à partir des classes de réponse, a baissé significativement de 2000 à 2009 ({{< lan-val "h00" >}} puis {{< lan-val "h09" >}}&nbsp;heures par semaine), puis n'a plus évolué significativement ({{< lan-val "h18" >}} en 2018)&nbsp;; c'est le goût qui a reculé ensuite&nbsp;: l'indice de plaisir de lire, construit pour se comparer de 2009 à 2018, baisse significativement, et la part des élèves qui disent ne lire que s'ils y sont obligés passe de {{< lan-val "obl09" >}}&nbsp;% à {{< lan-val "obl18" >}}&nbsp;%. Chez les 15-24 ans, la lecture assidue de livres reculait déjà de 1988 à 2008&nbsp;: {{< lan-val "cul88" >}}&nbsp;% lisaient vingt livres ou plus dans l'année, puis {{< lan-val "cul08" >}}&nbsp;%.

## Les écrans expliquent-ils la baisse&nbsp;? {#ecrans}

Les données disponibles ne permettent pas de le dire. La chronologie n'écarte qu'une explication&nbsp;: plusieurs reculs sont antérieurs à la généralisation du smartphone, qui ne peut donc pas en être la seule cause. Les réponses des élèves de 15 ans eux-mêmes, dans PISA, ne tranchent pas davantage&nbsp;: de 2022 à 2025, l'évolution de leur numérique de loisir reste indéterminée. La part de ceux qui ne répondent pas à la question a presque doublé, de {{< lan-val "nr22" >}}&nbsp;% à {{< lan-val "nr25" >}}&nbsp;%, et ces élèves ont des scores très inférieurs aux autres ({{< lan-val "nrs25" >}}&nbsp;points en 2025, contre {{< lan-val "reps25" >}} pour ceux qui répondent). Parmi les élèves qui répondent, la part qui déclare plus de trois heures de numérique de loisir par jour, avant et après l'école, passe de {{< lan-val "e3h22" >}}&nbsp;% en 2022 à {{< lan-val "e3h25" >}}&nbsp;% en 2025, et le week-end de {{< lan-val "w3h22" >}}&nbsp;% à {{< lan-val "w3h25" >}}&nbsp;%&nbsp;; mais si les non-répondants passaient tous plus de trois heures devant un écran, cette part aurait augmenté. Et 2022 suit de peu la crise sanitaire.

De 2022 à 2025, la baisse du score de lecture est significative chez les élèves qui déclarent le plus de numérique de loisir (−{{< lan-val "d35" >}}&nbsp;points entre trois et cinq heures, −{{< lan-val "d5p" >}} au-delà), et pas chez ceux qui en déclarent peu. Ces groupes ne réunissent pas les mêmes élèves d'une enquête à l'autre, et leur composition comme leur taux de réponse ont pu changer&nbsp;: c'est une description, pas une mesure d'effet du numérique. L'OCDE elle-même écrit que la montée du temps d'écran et le recul de la lecture pour le plaisir ont coïncidé avec des résultats plus faibles, et que ses données n'établissent pas de lien direct.

**Confrontation à la recherche.** Les travaux qui suivent des enfants dans le temps associent la lecture pour le plaisir aux progrès en vocabulaire&nbsp;: dans une cohorte britannique suivie depuis la naissance, ceux qui lisaient souvent dans l'enfance et à l'adolescence ont davantage progressé en vocabulaire, à niveau initial égal, ce que les auteurs ne présentent que comme un indice prudent d'effet (Sullivan et Brown, 2015). Une méta-analyse trouve que l'exposition à l'écrit va de pair avec le langage oral, de plus en plus nettement avec l'âge, et l'interprète comme une spirale où chaque progrès nourrit l'autre (Mol et Bus, 2011). Pour le numérique, les résultats sont plus partagés&nbsp;: la lecture numérique de loisir n'est que très faiblement associée à la compréhension, négativement chez les plus jeunes et positivement chez les plus âgés (Altamura, Vargas et Salmerón, 2023)&nbsp;; une méta-analyse d'expériences trouve qu'on comprend un peu mieux un texte informatif sur papier que sur écran, surtout en temps limité (Delgado et al., 2018), un résultat propre aux conditions qu'elle examine&nbsp;; chez les jeunes enfants, le temps d'écran est faiblement associé à un langage moins développé, et les programmes éducatifs regardés avec un adulte à un langage plus développé (Madigan et al., 2020). Aucun de ces travaux n'établit que les écrans ont fait baisser le vocabulaire des adolescents français.

## Les écarts se creusent-ils&nbsp;? {#ecarts}

Certains, et c'est là que les évaluations françaises sont les plus nettes. En fin de collège, le score CEDRE de l'ensemble des élèves n'évolue pas significativement de 2015 à 2021, mais celui de l'éducation prioritaire baisse significativement ({{< lan-val "ccep15" >}} puis {{< lan-val "ccep21" >}}), comme celui des garçons ({{< lan-val "ccg15" >}} puis {{< lan-val "ccg21" >}}). Le public hors éducation prioritaire restant stable, l'écart entre les deux passe, selon la DEPP, de {{< lan-val "ccec15" >}} à {{< lan-val "ccec21" >}}&nbsp;points, et celui entre filles et garçons augmente aussi&nbsp;; la DEPP ne publie pas de test de l'évolution de ces écarts eux-mêmes. En fin d'école, la hausse de 2021 vient du public hors éducation prioritaire&nbsp;; l'éducation prioritaire n'évolue pas significativement. En sixième, l'écart entre collèges favorisés et défavorisés est plus grand en lexique que dans tout autre domaine de français. Et à l'entrée du lycée, près de la moitié des élèves de seconde professionnelle déclarent ne pas lire pour leur plaisir. Une moyenne stable peut ainsi recouvrir un recul de ceux qui partaient déjà de plus bas.

## Ce que ces données ne disent pas {#limites}

- **Le vocabulaire**&nbsp;: aucune des séries publiques recensées ne le suit&nbsp;; les erreurs lexicales d'une dictée mesurent l'orthographe de mots donnés, pas le nombre de mots connus ou employés.
- **La pensée**&nbsp;: l'idée que la maîtrise des mots est le support de la pensée est une thèse sur le langage, que ces enquêtes ne peuvent ni confirmer ni réfuter&nbsp;; elles mesurent des compétences scolaires, pas la richesse d'un raisonnement.
- **Les causes**&nbsp;: aucune de ces séries ne départage les programmes, le temps d'enseignement du français, les pratiques de lecture, les écrans, la composition des classes ou la crise sanitaire. La chronologie n'exclut qu'une explication&nbsp;: la généralisation du smartphone comme seule cause des reculs qui lui sont antérieurs.
- **La comparaison entre instruments**&nbsp;: chacun a son âge, sa compétence, son échelle et ses années&nbsp;; aucun ne suit les mêmes élèves. Deux enquêtes peuvent diverger parce que les compétences évoluent différemment, ou parce que les instruments ont changé&nbsp;: PISA se passe sur ordinateur depuis 2015 et son cadre de lecture a été revu en 2018&nbsp;; CEDRE de fin de collège interroge des élèves de troisième, PISA tous les jeunes de 15 ans scolarisés. Les évaluations de sixième et de seconde, passées par tous les élèves, ne publient pas de test de significativité&nbsp;; leurs variations sont descriptives.
- **Les réponses des élèves**&nbsp;: le temps d'écran et le temps de lecture sont déclarés&nbsp;; dans PISA 2025, près d'un élève sur quatre ne répond pas à la question sur le numérique de loisir.
- **Les séries anciennes**&nbsp;: la DEPP rappelle que des épreuves identiques ne suffisent pas à garantir la comparabilité&nbsp;; les enquêtes Pratiques culturelles n'ont pas d'erreur type publiée et changent de définition entre 1981 et 1988.

## Ce qu'il faut retenir {#retenir}

La langue des élèves ne s'effondre pas d'un bloc, et elle ne tient pas non plus. Le recul le plus ancien est celui de l'orthographe grammaticale, de la lecture en fin d'école et du temps passé à lire pour le plaisir&nbsp;: il est engagé avant la généralisation du smartphone, et il porte sur la grammaire plus que sur l'orthographe des mots. La baisse récente se voit à 15 ans, dans PISA, depuis 2012&nbsp;; sur des périodes qui la recouvrent en partie, les évaluations de l'école et du collège ne suivent pas toutes la même évolution. Elle va de pair avec un recul du goût de lire et, en fin de collège, avec un recul significatif de l'éducation prioritaire quand l'ensemble ne bouge pas significativement. Le vocabulaire, que l'on croit en chute libre, n'est suivi par aucune des séries publiques recensées&nbsp;: c'est la première chose qu'il faudrait mesurer pour répondre à la question. Aucune de ces observations ne permet, à elle seule, d'attribuer ces évolutions aux écrans. Le résultat le plus solide n'est pas un déclin général, mais des compétences, des élèves et des périodes dont les évolutions ne se superposent pas&nbsp;: la question n'est pas seulement de savoir si le niveau baisse, mais quelles compétences reculent, chez quels élèves, et à quel moment de leur scolarité.

## Questions fréquentes {#questions}

{{< faq-visible >}}

{{< appel-livre slug="livresque-des-mots" sur="Et si l'on rouvrait les livres par les mots ?" avis="non" offert="avant" >}}
Cette page montre que le temps passé à lire pour le plaisir recule avant même les écrans, que le goût de lire recule ensuite, et qu'aucune des séries publiques recensées ne suit le vocabulaire des élèves. *Livresque des mots* prend la question par l'autre bout&nbsp;: une anthologie qui fait rencontrer, sans ordre imposé, des phrases d'auteurs de vingt-cinq siècles, pour donner envie de lire plutôt que d'en mesurer le manque.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Dictée et lecture en CM2.** DEPP, Note d'Information 22.37 (dictée de 67&nbsp;mots, 1987, 2007, 2015, 2021, secteur public&nbsp;; erreurs lexicales, accords)&nbsp;; Note 08.38 (lecture et dictée 1987-1997-2007, aux mêmes épreuves, avec la significativité des évolutions&nbsp;; tableau&nbsp;4&nbsp;: erreurs lexicales, grammaticales, de ponctuation et autres, 1987 et 2007)&nbsp;; Note 98.39 (lecture 1987-1997)&nbsp;; Note 16.28 pour la dictée de 2015 (chiffres révisés par la Note 22.37, qui fait foi). Les seuils de la Note 08.38 («&nbsp;moins de deux&nbsp;», «&nbsp;plus de vingt-cinq&nbsp;» erreurs) diffèrent de ceux de la Note 22.37&nbsp;: les deux séries ne sont pas mêlées.

**CEDRE.** DEPP, Notes d'Information 16.20, 22.28 (maîtrise de la langue en fin d'école, 2003-2021) et 22.29 (compétences langagières et littératie en fin de collège, 2015-2021, cadre revu en 2015&nbsp;: pas de comparaison avec 2003 et 2009), leurs données et les rapports techniques de 2021&nbsp;; significativité lue dans les tableaux de la DEPP, où les évolutions significatives sont en gras.

**Évaluations nationales.** DEPP, Note d'Information 26.21 et document de travail sur l'évaluation de début de sixième 2025 (scores 2017-2025, échelle fixée à 250 en 2017&nbsp;; maîtrise par domaine en 2025)&nbsp;; Note 26.22 et document de travail 2025-E15 (test de positionnement de seconde, échelle fixée à 250 en 2019)&nbsp;; Note 25.66 (pratiques de lecture, septembre 2023).

**PIRLS et PISA.** DEPP, Notes 17.24 et 23.21 (PIRLS)&nbsp;; OCDE, *PISA 2025 Results*, volume&nbsp;I, tableau I.B1.2a.37 (compréhension de l'écrit, 2000-2025, avec erreurs types) et annexe A1 (tendances de lecture 2018-2025)&nbsp;; *21st-Century Readers* (OCDE, 2021), tableaux B.4.4a (indice de plaisir de lire, déclaré comparable de 2009 à 2018) et B.4.8 (temps de lecture pour le plaisir, 2000, 2009, 2018). PISA 2000-2012&nbsp;: aucune baisse significative, d'après un test de l'auteur sur les erreurs types publiées, sans erreur de liaison&nbsp;; ce test détecte une baisse plus facilement que celui de l'OCDE, qui l'inclut. Temps de lecture pour le plaisir&nbsp;: heures estimées par l'OCDE à partir des classes de réponse&nbsp;; significativité marquée dans son tableau. Numérique de loisir&nbsp;: bases PISA 2022 et 2025 (fichiers élèves publics), questions ST326Q05 et ST326Q06, mêmes modalités les deux années, en quatre tranches fixées avant le calcul&nbsp;; dix valeurs plausibles, 80&nbsp;poids répliqués, erreur de liaison 2022-2025 déduite du tableau de l'OCDE&nbsp;; témoin&nbsp;: les moyennes de la France publiées par l'OCDE, retrouvées au centième&nbsp;; sensibilité à la non-réponse en classant tous les non-répondants dans la tranche la plus haute, puis la plus basse.

**Lecture de livres et smartphone.** Ministère de la Culture, enquêtes Pratiques culturelles des Français, tableaux d'évolution 1973-2008 (lecture de livres, 15-24 ans) et Lombardo et Wolff, *Cinquante ans de pratiques culturelles en France* (2020) pour la rupture de série&nbsp;; CREDOC, Baromètre du numérique 2015 (tableau&nbsp;3, 12-17 ans, 2011-2015), confirmé par le dossier de l'ARCEP de 2013.

**Textes donnés à lire.** Base Emmanuelle, bibliothèque Diderot de Lyon (page d'accueil et recherche dans la base)&nbsp;; catalogue général de la BnF, interrogé par son service SRU, avec une liste de manuels témoins fixée avant la recherche&nbsp;; code de la propriété intellectuelle, articles L.&nbsp;122-5-3, R.&nbsp;122-27 et R.&nbsp;122-28&nbsp;; conditions d'utilisation de Gallica&nbsp;; *Livres Hebdo*, 15&nbsp;avril 2026, pour la liste d'opposition de la Société des gens de lettres. Effectifs&nbsp;: comparaison de deux moyennes, test bilatéral à 5&nbsp;%, puissance de 80&nbsp;%.

**Recherche.** Sullivan et Brown, *British Educational Research Journal*, 2015&nbsp;; Mol et Bus, *Psychological Bulletin*, 2011&nbsp;; Altamura, Vargas et Salmerón, *Review of Educational Research*, 2023&nbsp;; Delgado, Vargas, Ackerman et Salmerón, *Educational Research Review*, 2018&nbsp;; Madigan et al., *JAMA Pediatrics*, 2020.

Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent d'un calcul de l'auteur, dont l'extrait est archivé avec ses empreintes&nbsp;; le script qui écrit la page vérifie chaque affirmation chiffrée et s'arrête si elle n'est plus vraie. Le plan a été soumis à une contre-analyse externe avant le calcul, puis un protocole a été écrit avant le calcul, avec ses règles de verdict. Toutes les valeurs ont été lues deux fois, par deux extracteurs indépendants&nbsp;; ce contrôle a détecté l'erreur qu'on y avait introduite volontairement.

{{< reutiliser figures="figures_langue" jeu="langue_eleves" sources="DEPP, OCDE (PISA), IEA (PIRLS), ministère de la Culture, CREDOC" donnees="Dictée de CM2 1987-2021 (total et erreurs lexicales), lecture en CM2 1987-2007, CEDRE fin d'école et fin de collège, PIRLS, évaluation de sixième et maîtrise par domaine, test de seconde, PISA compréhension de l'écrit 2000-2025, temps de lecture et plaisir de lire, lecteurs de 15-24 ans, smartphone des 12-17 ans, pratiques de lecture 2023, numérique de loisir dans PISA 2022 et 2025 ; le même contenu existe en CSV, au format long." >}}
La langue des élèves ne recule pas d'un bloc. À la même dictée de CM2, les erreurs passent de {{< lan-val "tot87" >}} à {{< lan-val "tot21" >}} entre 1987 et 2021, mais l'orthographe des mots ne compte que pour une petite part de la hausse&nbsp;: c'est surtout l'orthographe grammaticale qui recule. Les reculs les plus anciens précèdent la généralisation du smartphone&nbsp;; PISA ne baisse qu'après 2012, quand d'autres évaluations, à l'école et en fin de collège, ne reculent pas significativement sur des périodes qui recouvrent en partie cette baisse. Aucune des séries publiques recensées ne permet de suivre l'évolution du vocabulaire des élèves.
{{< /reutiliser >}}
