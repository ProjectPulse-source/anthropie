---
title: "Les élèves maîtrisent-ils moins bien la langue française ?"
description: "Dictée, lecture, vocabulaire, plaisir de lire, écrans : ce que mesurent vraiment les enquêtes. À la même dictée de CM2, {lan.tot87} erreurs en 1987, {lan.tot21} en 2021 : sur ces {lan.h_tot} erreurs supplémentaires, {lan.h_lex} portent sur l'orthographe des mots. Plusieurs reculs étaient déjà engagés avant la généralisation du smartphone ; le vocabulaire n'est suivi par aucune série publique recensée. Données DEPP, OCDE, IEA, ministère de la Culture, recalculées."
chapo: "Pas d'un bloc. À la même dictée de CM2, les élèves faisaient {lan.tot87} erreurs en 1987 et {lan.tot21} en 2021 ; mais sur ces {lan.h_tot} erreurs supplémentaires, {lan.h_lex} seulement portent sur l'orthographe des mots eux-mêmes. Que mesure-t-on réellement quand on dit que les élèves maîtrisent moins bien la langue ?"
date: 2026-10-09T00:00:00+02:00
lastmod: 2026-10-10
og_title: "Les élèves maîtrisent-ils moins bien la langue française ? Dictée, lecture, vocabulaire, écrans — S. Lalut"
og_image: "images/og-langue-eleves.jpg"
og_image_alt: "Carte de partage : « Les élèves maîtrisent-ils moins bien la langue française ? » — à la même dictée de CM2, nombre moyen d'erreurs de 1987 à 2021 : sur les erreurs supplémentaires, une petite part, en bleu, porte sur l'orthographe des mots ; les autres erreurs, en orange, ont presque doublé."
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
    answer: "Oui. À la même dictée de CM2, les élèves faisaient {lan.tot87} erreurs en moyenne en 1987, {lan.tot07} en 2007, {lan.tot15} en 2015 et {lan.tot21} en 2021 ; la hausse de 1987 à 2007 est significative selon la DEPP, et elle est deux fois moins forte de 2015 à 2021 que de 2007 à 2015. Sur les {lan.h_tot} erreurs supplémentaires, {lan.h_lex} portent sur l'orthographe des mots eux-mêmes ({lan.lex87} erreurs lexicales en 1987, {lan.lex21} en 2021) ; les autres erreurs passent de {lan.aut87} à {lan.aut21}. La DEPP ne détaille ces autres erreurs que pour 1987 et 2007 : la hausse y est grammaticale pour {lan.h_gram0707} erreurs sur {lan.h_tot0707}, accords et conjugaison surtout."
  - question: "Les jeunes n'utilisent-ils plus que 400 mots ?"
    answer: "Ce chiffre ne repose sur aucune étude retrouvée, et il ne dit pas ce qu'il compte : mots employés, reconnus, compris en contexte. Parmi les sources publiques françaises recensées, aucune série ne permet de suivre l'évolution du vocabulaire des élèves : l'évaluation CEDRE publie un score unique de maîtrise de la langue, le test de lexique de sixième change de questions d'une année à l'autre, et celui de seconde n'existe qu'en voie professionnelle, depuis 2025."
  - question: "Les écrans expliquent-ils la baisse de la lecture ?"
    answer: "Les données ne permettent pas de le dire. Plusieurs reculs sont antérieurs à la généralisation du smartphone chez les adolescents (plus de la moitié des 12-17 ans en sont équipés en {lan.smart_seuil}) : l'orthographe à la dictée de 1987 à 2007, la lecture en CM2 de 1997 à 2007, le temps de lecture pour le plaisir à 15 ans de 2000 à 2009. Cette chronologie exclut seulement que la généralisation du smartphone soit la seule cause de ces reculs ; elle ne dit rien de ses premiers usages ni des autres écrans. Entre 2022 et 2025, l'évolution du numérique de loisir des jeunes de 15 ans reste indéterminée : la part qui ne répond plus à la question a presque doublé, et le verdict change selon la tranche où l'on classe ces non-répondants."
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

## Les élèves font-ils plus de fautes qu'avant&nbsp;? {#dictee}

Oui. La mesure en est une même dictée de 67&nbsp;mots, donnée à des élèves de CM2 du secteur public en 1987, 2007, 2015 et 2021.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/langue-dictee-m.svg" width="300" height="689">
    <img src="/img/langue-dictee.svg" alt="Barres empilées, nombre moyen d'erreurs à la même dictée de CM2 : en 1987, {{< lan-val "lex87" >}} erreurs lexicales et {{< lan-val "aut87" >}} autres erreurs, {{< lan-val "tot87" >}} au total ; en 2007, {{< lan-val "lex07" >}} et {{< lan-val "aut07" >}}, {{< lan-val "tot07" >}} ; en 2015, {{< lan-val "lex15" >}} et {{< lan-val "aut15" >}}, {{< lan-val "tot15" >}} ; en 2021, {{< lan-val "lex21" >}} et {{< lan-val "aut21" >}}, {{< lan-val "tot21" >}}." width="720" height="412" loading="lazy">
  </picture>
  <figcaption>Nombre moyen d'erreurs à la même dictée de 67 mots, élèves de CM2 du public (DEPP, Note d'Information 22.37).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De 1987 à 2021, sur les {{< lan-val "h_tot" >}}&nbsp;erreurs supplémentaires à la même dictée, {{< lan-val "h_lex" >}} portent sur l'orthographe des mots eux-mêmes.

</div>

**De 1987 à 2021, ce qui est établi.** Les erreurs lexicales, celles qui portent sur l'orthographe des mots dictés, augmentent elles aussi, de {{< lan-val "lex87" >}} à {{< lan-val "lex21" >}}&nbsp;; mais elles ne pèsent qu'environ un dixième de la hausse. Les mots usuels de la dictée, «&nbsp;soir&nbsp;», «&nbsp;maison&nbsp;», «&nbsp;chien&nbsp;», restent écrits correctement par plus de neuf élèves sur dix. Le reste de la hausse tient aux autres erreurs, qui passent de {{< lan-val "aut87" >}} à {{< lan-val "aut21" >}}&nbsp;: une catégorie qui rassemble la grammaire, la ponctuation et les oublis.

**De 1987 à 2007 seulement, ce que l'on sait de ces autres erreurs.** Pour ces deux années, la DEPP publie le détail par type&nbsp;: les erreurs grammaticales passent de {{< lan-val "gram87" >}} à {{< lan-val "gram07" >}}, soit {{< lan-val "h_gram0707" >}} des {{< lan-val "h_tot0707" >}}&nbsp;erreurs supplémentaires, et la ponctuation ne progresse pas&nbsp;; «&nbsp;ce sont principalement les erreurs grammaticales qui ont augmenté&nbsp;» — l'accord du verbe avec son sujet, de l'adjectif, du participe passé. **Ce partage ne s'étend pas à toute la période.** Après 2007, la DEPP indique seulement que la baisse sur les accords n'a porté que sur 1987-2015&nbsp;; la hausse de 2015 à 2021, deux fois moins forte que celle de 2007 à 2015, n'est pas détaillée par type.

La répartition des élèves a changé avec la moyenne&nbsp;: la part de ceux qui font vingt-cinq erreurs ou plus a quadruplé, de {{< lan-val "bcp87" >}}&nbsp;% à {{< lan-val "bcp21" >}}&nbsp;%, et celle des élèves qui en font deux ou moins est tombée de {{< lan-val "peu87" >}}&nbsp;% à {{< lan-val "peu21" >}}&nbsp;% (mêmes seuils, même note de la DEPP). La hausse de 1987 à 2007 est significative selon la DEPP, qui rappelle aussi que des épreuves identiques ne suffisent pas à garantir la comparabilité d'une époque à l'autre.

Ce que cette dictée ne mesure pas compte autant&nbsp;: écrire correctement un mot dicté n'est ni le connaître ni l'employer. Elle ne dit rien du vocabulaire des élèves. Et elle ne dit qu'un âge, le CM2&nbsp;: les autres mesures de la langue racontent-elles la même histoire, et depuis quand&nbsp;?

## La langue des élèves recule-t-elle d'un bloc&nbsp;? {#chronologie}

Onze mesures de la langue des élèves, de 1987 à 2025, conduisent à trois constats&nbsp;:

- **certains reculs étaient déjà engagés avant 2013**, année où plus de la moitié des 12-17 ans ont un smartphone&nbsp;: l'orthographe à la dictée, la lecture en fin d'école, le temps de lecture pour le plaisir à 15 ans&nbsp;;
- **les indicateurs n'évoluent pas ensemble**&nbsp;: PISA, l'enquête de l'OCDE auprès des jeunes de 15 ans, recule depuis 2012, quand PIRLS (la lecture en CM1) et CEDRE (les évaluations du ministère en fin d'école et de collège) ne montrent aucun recul établi par un test sur des périodes qui recouvrent en partie cette baisse&nbsp;;
- **aucun ne désigne une cause unique**, ni l'âge auquel un recul commencerait.

La frise les détaille&nbsp;: la couleur donne le sens observé, le trait plein une évolution testée, les tirets un sens observé sans test publié.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/langue-chronologie-m.svg" width="300" height="1076">
    <img src="/img/langue-chronologie.svg" alt="Frise de 1985 à 2025, une ligne par mesure de la langue des élèves, avec le sens de chaque intervalle et un repère en {{< lan-val "smart_seuil" >}}, année où plus de la moitié des 12-17 ans ont un smartphone. Reculs significatifs avant ce repère : dictée de CM2 de 1987 à 2007, lecture en CM2 de 1997 à 2007, temps de lecture pour le plaisir à 15 ans de 2000 à 2009. PISA, compréhension de l'écrit, sans baisse significative de 2000 à 2012, en recul significatif de 2012 à 2025. Sur la période récente : PIRLS en CM1 sans évolution significative de 2016 à 2021, CEDRE fin d'école en hausse significative de 2015 à 2021, CEDRE fin de collège sans évolution significative, sixième en hausse puis en léger recul sans test publié." width="720" height="526" loading="lazy">
  </picture>
  <figcaption>Sens de chaque intervalle pour onze mesures de la langue des élèves, chacune dans sa propre échelle (DEPP, OCDE, IEA, ministère de la Culture, CREDOC).</figcaption>
</figure>

Le repère est celui de la généralisation du smartphone&nbsp;: {{< lan-val "smart11" >}}&nbsp;% des 12-17 ans en étaient équipés en 2011, {{< lan-val "smart13" >}}&nbsp;% en {{< lan-val "smart_seuil" >}}, première année où ils sont plus de la moitié (CREDOC). Avant cette date, la dictée de CM2 a déjà reculé&nbsp;; aux mêmes épreuves de lecture, les élèves de CM2 étaient stables de 1987 à 1997, puis ont perdu {{< lan-val "lcm2_07" >}}&nbsp;écart-type de 1997 à 2007&nbsp;; à 15 ans, le temps de lecture pour le plaisir est passé de {{< lan-val "h00" >}} à {{< lan-val "h09" >}}&nbsp;heures par semaine entre 2000 et 2009, une baisse significative selon l'OCDE, qui estime ces heures à partir des classes de réponse des élèves. Ces trois reculs ne peuvent donc pas avoir pour seule cause la généralisation du smartphone&nbsp;; la chronologie ne dit rien, en revanche, des premiers usages du smartphone, des autres écrans, ni de ce qui a pu s'ajouter ensuite.

PISA raconte autre chose. En compréhension de l'écrit, la France était à {{< lan-val "pisa00" >}}&nbsp;points en 2000 et à {{< lan-val "pisa12" >}} en 2012&nbsp;; elle recule ensuite à chaque enquête, jusqu'à {{< lan-val "pisa25" >}} en 2025, soit {{< lan-val "pisa_v12" >}}&nbsp;points de moins qu'en 2012. Sur des périodes qui recouvrent en partie cette baisse, les autres évaluations ne reculent pas significativement&nbsp;: PIRLS en CM1 passe de {{< lan-val "pirls16" >}} à {{< lan-val "pirls21" >}}&nbsp;points entre 2016 et 2021, sans évolution significative&nbsp;; l'évaluation CEDRE de fin d'école (le cycle d'évaluations disciplinaires de la DEPP), stable de 2003 à 2015, progresse significativement en 2021 ({{< lan-val "ce15" >}} puis {{< lan-val "ce21" >}})&nbsp;; celle de fin de collège passe de {{< lan-val "cc15" >}} à {{< lan-val "cc21" >}}, sans évolution significative. L'évaluation de début de sixième, passée par tous les élèves, est à {{< lan-val "six25" >}}&nbsp;points en 2025, au-dessus de 2017 ({{< lan-val "six17" >}}) mais sous son sommet de 2020-2021 ({{< lan-val "six21" >}})&nbsp;; le test d'entrée en seconde générale et technologique revient en 2025 à son niveau de 2019 ({{< lan-val "sec25" >}}), après un sommet en 2020-2021 ({{< lan-val "sec21" >}}). L'OCDE fait le même constat pour PIRLS&nbsp;: la France figure parmi les pays dont les résultats PISA baissent malgré des résultats PIRLS stables.

Ces mesures divergent sans se contredire&nbsp;: âges, compétences, enjeux et années diffèrent, et aucune ne suit les mêmes élèves d'un âge à l'autre. Elles ne disent donc pas à quel âge un recul commencerait. La même divergence entre PISA et les évaluations passées en classe se retrouve en mathématiques&nbsp;; ce qu'elle permet et interdit de conclure est détaillé sur la page voisine&nbsp;: [pourquoi les évaluations ne montrent pas toutes la même baisse](/le-niveau-des-eleves-baisse-t-il/#evaluations).

<details class="repli">
<summary>Le verdict série par série, et ce qui ne peut pas être conclu</summary>

- **Dictée de CM2**&nbsp;: hausse significative des erreurs de 1987 à 2007 (DEPP)&nbsp;; hausse ensuite, sans test publié, deux fois moins forte de 2015 à 2021 que de 2007 à 2015. Recul antérieur au smartphone&nbsp;: établi.
- **Lecture en CM2, épreuves de 1987**&nbsp;: stable de 1987 à 1997, baisse significative de 1997 à 2007. Recul antérieur&nbsp;: établi.
- **PISA, compréhension de l'écrit**&nbsp;: aucune baisse significative entre 2000 et 2012 ({{< lan-val "pisa00" >}} puis {{< lan-val "pisa12" >}}), un creux en 2006 sans tendance&nbsp;; baisse significative de 2012 à 2025. Pas de recul antérieur.
- **PIRLS, CM1**&nbsp;: {{< lan-val "pirls01" >}} en 2001, {{< lan-val "pirls11" >}} en 2011, {{< lan-val "pirls16" >}} en 2016&nbsp;; la DEPP publie la significativité des écarts à cinq, dix et quinze ans comptés depuis 2016, pas celle de 2001 à 2011&nbsp;: non identifiable.
- **Livres lus par les 15-24 ans**&nbsp;: la part qui lit vingt livres ou plus dans l'année passe de {{< lan-val "cul88" >}}&nbsp;% en 1988 à {{< lan-val "cul08" >}}&nbsp;% en 2008 (enquêtes Pratiques culturelles, après la rupture de série de 1981-1988)&nbsp;; aucune erreur type publiée&nbsp;: montré sans verdict.

</details>

L'un des reculs les plus anciens ne porte pas sur une compétence, mais sur un choix&nbsp;: le temps que les adolescents consacrent à lire quand rien ne les y oblige.

## Les élèves lisent-ils moins pour leur plaisir&nbsp;? {#plaisir}

Deux choses reculent l'une après l'autre. Le temps de lecture pour le plaisir à 15 ans, estimé par l'OCDE à partir des classes de réponse, a baissé significativement de 2000 à 2009 ({{< lan-val "h00" >}} puis {{< lan-val "h09" >}}&nbsp;heures par semaine), puis n'a plus évolué significativement ({{< lan-val "h18" >}} en 2018). C'est le goût qui a reculé ensuite&nbsp;: l'indice de plaisir de lire, construit pour se comparer de 2009 à 2018, baisse significativement, et la part des élèves qui disent ne lire que s'ils y sont obligés passe de {{< lan-val "obl09" >}}&nbsp;% à {{< lan-val "obl18" >}}&nbsp;%. Chez les 15-24 ans, la lecture assidue de livres reculait déjà de 1988 à 2008&nbsp;: {{< lan-val "cul88" >}}&nbsp;% lisaient vingt livres ou plus dans l'année, puis {{< lan-val "cul08" >}}&nbsp;%.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/langue-plaisir-m.svg" width="300" height="572">
    <img src="/img/langue-plaisir.svg" alt="Barres, part des élèves qui déclarent ne pas lire pour leur plaisir en 2023 : sixième {{< lan-val "np6" >}} %, quatrième {{< lan-val "np4" >}} %, seconde générale et technologique {{< lan-val "np2gt" >}} %, seconde professionnelle {{< lan-val "np2pro" >}} %, première année de CAP {{< lan-val "npcap" >}} %." width="720" height="306" loading="lazy">
  </picture>
  <figcaption>Part des élèves qui déclarent ne pas lire pour leur plaisir, selon la classe, septembre 2023 (DEPP, Note d'Information 25.66).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** En 2023, un élève de sixième sur huit déclare ne pas lire pour son plaisir&nbsp;; ils sont {{< lan-val "np2gt" >}}&nbsp;% en seconde générale et technologique et près de la moitié en seconde professionnelle.

</div>

Cette enquête de la DEPP, menée auprès de tous les élèves de quatre niveaux, compare des élèves différents la même année&nbsp;: elle décrit un écart entre les âges et les filières, pas une évolution. Elle ne dit pas que les élèves perdent le goût de lire en grandissant, seulement qu'en 2023 les plus âgés, et ceux de la voie professionnelle, sont plus nombreux à ne pas lire pour leur plaisir.

Le goût de lire recule de 2009 à 2018, période où le smartphone se généralise. La coïncidence pose la question des écrans.

## Les écrans expliquent-ils la baisse&nbsp;? {#ecrans}

Les données disponibles ne permettent pas de le dire. La chronologie ne règle qu'un point&nbsp;: la généralisation du smartphone ne peut pas être la seule cause des reculs qui lui sont antérieurs. Tout le reste demeure ouvert, des premiers usages du smartphone aux autres écrans.

Les réponses des élèves de 15 ans eux-mêmes, dans PISA, ne tranchent pas davantage. De 2022 à 2025, parmi ceux qui répondent, la part qui déclare plus de trois heures de numérique de loisir par jour, avant et après l'école, passe de {{< lan-val "e3h22" >}}&nbsp;% à {{< lan-val "e3h25" >}}&nbsp;%, et le week-end de {{< lan-val "w3h22" >}}&nbsp;% à {{< lan-val "w3h25" >}}&nbsp;%. Mais la part de ceux qui ne répondent pas à la question a presque doublé, de {{< lan-val "nr22" >}}&nbsp;% à {{< lan-val "nr25" >}}&nbsp;%, et le verdict change selon la tranche où on les classe&nbsp;: s'ils passaient tous plus de trois heures devant un écran les jours de classe, cette part aurait augmenté. L'évolution reste donc indéterminée. Ces non-répondants ont par ailleurs des scores de lecture très inférieurs aux autres ({{< lan-val "nrs25" >}}&nbsp;points en 2025, contre {{< lan-val "reps25" >}})&nbsp;: un fait sur ce groupe, qui ne renseigne pas sur son temps d'écran. Et 2022 suit de peu la crise sanitaire.

De 2022 à 2025, la baisse du score de lecture est significative chez les élèves qui déclarent le plus de numérique de loisir (−{{< lan-val "d35" >}}&nbsp;points entre trois et cinq heures, −{{< lan-val "d5p" >}} au-delà), et pas chez ceux qui en déclarent peu. Ces groupes ne réunissent pas les mêmes élèves d'une enquête à l'autre, et leur composition comme leur taux de réponse ont pu changer&nbsp;: c'est une description, pas une mesure d'effet du numérique. L'OCDE elle-même écrit que la montée du temps d'écran et le recul de la lecture pour le plaisir ont coïncidé avec des résultats plus faibles, et que ses données n'établissent pas de lien direct.

**Confrontation à la recherche.** Les travaux qui suivent des enfants dans le temps associent la lecture pour le plaisir aux progrès en vocabulaire&nbsp;: dans une cohorte britannique suivie depuis la naissance, ceux qui lisaient souvent dans l'enfance et à l'adolescence ont davantage progressé en vocabulaire, à niveau initial égal, ce que les auteurs ne présentent que comme un indice prudent d'effet (Sullivan et Brown, 2015). Une méta-analyse trouve que l'exposition à l'écrit va de pair avec le langage oral, de plus en plus nettement avec l'âge, et l'interprète comme une spirale où chaque progrès nourrit l'autre (Mol et Bus, 2011). Pour le numérique, les résultats sont plus partagés&nbsp;: la lecture numérique de loisir n'est que très faiblement associée à la compréhension, négativement chez les plus jeunes et positivement chez les plus âgés (Altamura, Vargas et Salmerón, 2023)&nbsp;; une méta-analyse d'expériences trouve qu'on comprend un peu mieux un texte informatif sur papier que sur écran, surtout en temps limité (Delgado et al., 2018), un résultat propre aux conditions qu'elle examine&nbsp;; chez les jeunes enfants, le temps d'écran est faiblement associé à un langage moins développé, et les programmes éducatifs regardés avec un adulte à un langage plus développé (Madigan et al., 2020). Aucun de ces travaux n'établit que les écrans ont fait baisser le vocabulaire des adolescents français.

Aucune des séries de cette page ne départage d'ailleurs les explications en présence&nbsp;: programmes, temps d'enseignement du français, pratiques de lecture, écrans, composition des classes, crise sanitaire. Si les données ne désignent pas de cause, une moyenne nationale dit-elle au moins quels élèves reculent&nbsp;?

## Les écarts se creusent-ils&nbsp;? {#ecarts}

Pas de façon démontrée&nbsp;; mais la moyenne cache des trajectoires différentes, et c'est là que les évaluations françaises sont les plus nettes. En fin de collège, le score CEDRE de l'ensemble des élèves n'évolue pas significativement de 2015 à 2021. Pourtant, celui de l'éducation prioritaire baisse significativement ({{< lan-val "ccep15" >}} puis {{< lan-val "ccep21" >}}), comme celui des garçons ({{< lan-val "ccg15" >}} puis {{< lan-val "ccg21" >}}). Le public hors éducation prioritaire restant stable, l'écart entre les deux passe, selon la DEPP, de {{< lan-val "ccec15" >}} à {{< lan-val "ccec21" >}}&nbsp;points, et celui entre filles et garçons augmente aussi&nbsp;; la DEPP ne publie pas de test de l'évolution de ces écarts eux-mêmes&nbsp;: on ne peut donc pas dire qu'ils se creusent significativement. En fin d'école, la hausse de 2021 vient du public hors éducation prioritaire&nbsp;; l'éducation prioritaire n'évolue pas significativement. À l'entrée du lycée, près de la moitié des élèves de seconde professionnelle déclarent ne pas lire pour leur plaisir. Une moyenne stable peut ainsi recouvrir un recul de ceux qui partaient déjà de plus bas.

Reste ce que la question de départ vise le plus directement, et que ces enquêtes mesurent le moins&nbsp;: les mots que les élèves connaissent, et les textes qu'on leur donne à lire.

## Les élèves connaissent-ils moins de mots&nbsp;? {#vocabulaire}

Aucune des séries publiques françaises recensées pour cette page, dont la liste figure dans «&nbsp;D'où viennent ces chiffres&nbsp;», ne permet de le dire. L'évaluation CEDRE note la grammaire, le vocabulaire, l'orthographe et la conjugaison, mais n'en publie qu'un score global par année&nbsp;; l'évaluation de sixième contient un test de lexique dont les questions changent d'une année à l'autre&nbsp;; le test de seconde n'en a un qu'en voie professionnelle, et depuis 2025 seulement. Ce constat ne dit pas que le vocabulaire des élèves se maintient&nbsp;: il dit qu'aucune série publique ne permet d'en suivre l'évolution. Le chiffre souvent cité selon lequel les jeunes n'utiliseraient plus que quelques centaines de mots ne repose sur aucune étude retrouvée, et il ne dit pas ce qu'il compte&nbsp;: mots employés spontanément, reconnus, compris en contexte, ou disponibles pour s'exprimer avec précision.

L'évaluation de début de sixième fournit, pour 2025, une photographie des écarts en lexique. Cette année-là, {{< lan-val "lex_sat" >}}&nbsp;% des élèves ont une maîtrise satisfaisante du lexique&nbsp;: {{< lan-val "lex_ips1" >}}&nbsp;% dans les collèges qui accueillent les élèves les plus défavorisés, {{< lan-val "lex_ips5" >}}&nbsp;% dans les plus favorisés. Parmi les cinq domaines de français évalués, c'est en lexique que cet écart est le plus grand.

## Les textes qu'on donne à lire se sont-ils simplifiés&nbsp;? {#textes}

La question revient avec celle du vocabulaire&nbsp;: les livres donnés aux enfants, à commencer par les manuels de lecture, emploieraient moins de mots, et de plus simples. **Pour la France, ce n'est pas établi&nbsp;: aucune mesure publiée n'a été retrouvée, et il n'est pas possible aujourd'hui d'en construire une solide.** La raison décisive tient à l'échantillon&nbsp;: mesurer une évolution suppose de tirer, pour chaque période, un échantillon représentatif des manuels publiés, et cette liste n'existe pas pour le français. Un corpus composé au hasard des catalogues changerait de nature d'une décennie à l'autre, et ce changement suffirait à fabriquer une tendance.

Répondre demanderait d'abord de recenser les manuels de français, puis de tirer au sort des ouvrages en nombre suffisant&nbsp;: pour déceler entre deux périodes un écart d'un écart-type, il faut déjà, en ordre de grandeur (comparaison de deux moyennes, test à 5&nbsp;%, puissance de 80&nbsp;%, avant toute stratification), {{< lan-val "n_d1" >}}&nbsp;ouvrages par période et par niveau, et {{< lan-val "n_d05" >}} pour un écart deux fois plus petit. C'est un travail d'équipe de recherche, avec l'accès des bibliothèques qui conservent ces manuels.

<details class="repli">
<summary>Pourquoi l'échantillon manque, ce que le droit permet, et le cas du Club des Cinq</summary>

**Les catalogues.** La base Emmanuelle de la bibliothèque Diderot (ENS de Lyon), qui recense les manuels scolaires publiés en France depuis 1789, couvre {{< lan-val "emma_ndisc" >}}&nbsp;disciplines, des langues anciennes à la géographie, mais pas le français, dont la saisie est annoncée en cours&nbsp;; interrogée le {{< lan-val "tx_date" >}}, elle ne contient pas la méthode *Daniel et Valérie*. Le catalogue de la BnF, lui, ne signale pas les manuels comme tels, et une recherche par le titre ne retrouve pas les mêmes livres selon les époques. Les méthodes *Daniel et Valérie* ({{< lan-val "dv_cat" >}}&nbsp;notices au catalogue) et *Rémi et Colette* ({{< lan-val "rc_cat" >}}), des années 1970, échappent entièrement à une recherche des titres qui associent «&nbsp;lecture&nbsp;» à un niveau de classe, quand *Taoki*, des années 2010, y est retrouvé en partie ({{< lan-val "taoki_r1" >}}&nbsp;notices sur {{< lan-val "taoki_cat" >}}).

**Le droit.** En règle générale, un manuel dont un auteur est mort il y a moins de soixante-dix ans reste protégé&nbsp;; la fouille automatique de son texte n'est permise qu'à défaut d'opposition de ses ayants droit (code de la propriété intellectuelle, article L.&nbsp;122-5-3), et la Société des gens de lettres publie depuis avril 2026 une liste des œuvres dont les auteurs s'y opposent. Pour les livres anciens numérisés par la BnF, les conditions de Gallica ne rendent cette fouille gratuite que pour la recherche académique à but non lucratif.

**Un cas mesurable à petite échelle.** Le *Club des Cinq* existe en français dans trois textes&nbsp;: une traduction parue à partir de 1955, une seconde dans les années 1970, et une traduction revue publiée en 2006. Le seul travail universitaire retrouvé les compare sans les compter&nbsp;: le passé simple y cède partout la place au présent, des objets sont modernisés, de nombreuses descriptions disparaissent (Maisonneuve, 2014). De combien la langue en sort simplifiée, aucune mesure publiée ne le dit. Une telle mesure ne suppose pas de numériser les livres&nbsp;: la longueur des phrases, la part de chaque temps verbal ou celle des dialogues se relèvent à la main sur des exemplaires achetés, et seuls les comptes se publient. Elle demande en revanche une précaution&nbsp;: ne comparer que les passages conservés d'une version à l'autre effacerait une partie de la simplification, puisque des descriptions entières ont disparu&nbsp;; les suppressions se comptent à part.

</details>

Plusieurs recherches combleraient ces manques&nbsp;:

- **recenser les manuels de lecture de français**, sur le modèle de ce que la base Emmanuelle a fait pour d'autres disciplines&nbsp;: c'est le préalable à toute série&nbsp;;
- **mesurer les réécritures de classiques pour la jeunesse**, le *Club des Cinq* et les autres séries rééditées, en comparant les mêmes tomes d'une version à l'autre, passages conservés et supprimés comptés séparément&nbsp;;
- **refaire, avec la même méthode, la photographie du vocabulaire des manuels de lecture** que la base Manulex a publiée en 2004&nbsp;: deux photographies comparables diraient déjà ce qui a changé, sans attendre une série complète&nbsp;;
- **relier la langue des textes à celle des élèves**&nbsp;: aux États-Unis, une étude a mesuré la simplification du vocabulaire des manuels sur la plus grande partie du XXᵉ&nbsp;siècle et l'a rapprochée du recul des résultats au volet verbal du SAT, le test d'entrée à l'université, en rappelant que seule une expérience pourrait établir un lien de cause (Hayes, Wolfer et Wolfe, 1996)&nbsp;; son équivalent français n'existe pas.

## Ce que ces données ne disent pas {#limites}

- **La pensée**&nbsp;: l'idée que la maîtrise des mots est le support de la pensée est une thèse sur le langage, que ces enquêtes ne peuvent ni confirmer ni réfuter&nbsp;; elles mesurent des compétences scolaires, pas la richesse d'un raisonnement.
- **Les réponses des élèves**&nbsp;: le temps d'écran et le temps de lecture sont déclarés&nbsp;; dans PISA 2025, près d'un élève sur quatre ne répond pas à la question sur le numérique de loisir.
- **Les instruments**&nbsp;: CEDRE de fin de collège interroge des élèves de troisième, PISA tous les jeunes de 15 ans scolarisés&nbsp;; PISA se passe sur ordinateur depuis 2015 et son cadre de lecture a été revu en 2018. Les évaluations de sixième et de seconde, passées par tous les élèves, ne publient pas de test de significativité&nbsp;: leurs variations sont descriptives.
- **Les séries anciennes**&nbsp;: les enquêtes Pratiques culturelles n'ont pas d'erreur type publiée et changent de définition entre 1981 et 1988.

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

La question se pose souvent comme celle d'un déclin d'ensemble, centré sur les mots et précipité par les écrans. Les mesures dessinent autre chose. La plus longue, une même dictée depuis 1987, montre une hausse des erreurs qui tient pour l'essentiel à d'autres erreurs que l'orthographe des mots, grammaticales d'abord sur la période où elles sont détaillées&nbsp;; elle est engagée, comme le recul de la lecture en fin d'école et du temps de lecture pour le plaisir, avant la généralisation du smartphone, qui ne peut donc pas être la seule cause de son apparition. À 15 ans, PISA recule depuis 2012, sans que les évaluations de l'école et du collège suivent toutes cette pente&nbsp;; le goût de lire recule de 2009 à 2018&nbsp;; en fin de collège, l'éducation prioritaire recule quand l'ensemble ne bouge pas significativement. Quant au vocabulaire, que la question vise d'abord, aucune série publique recensée ne le suit. Là où le diagnostic est le plus souvent proclamé, la mesure manque&nbsp;; là où elle existe, elle oblige à le préciser&nbsp;: quelles compétences reculent, chez quels élèves, et depuis quand.

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

{{< appel-livre slug="livresque-des-mots" sur="Et si l'on rouvrait les livres par les mots ?" avis="non" offert="avant" >}}
Cette page montre que le temps passé à lire pour le plaisir recule avant la généralisation du smartphone, que le goût de lire recule ensuite, et qu'aucune des séries publiques recensées ne suit le vocabulaire des élèves. *Livresque des mots* prend la question par l'autre bout&nbsp;: une anthologie qui fait rencontrer, sans ordre imposé, des phrases d'auteurs de vingt-cinq siècles, pour donner envie de lire plutôt que d'en mesurer le manque.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Dictée et lecture en CM2.** DEPP, Note d'Information 22.37 (dictée de 67&nbsp;mots, 1987, 2007, 2015, 2021, secteur public&nbsp;; erreurs lexicales, accords)&nbsp;; Note 08.38 (lecture et dictée 1987-1997-2007, aux mêmes épreuves, avec la significativité des évolutions&nbsp;; tableau&nbsp;4&nbsp;: erreurs lexicales, grammaticales, de ponctuation et autres, 1987 et 2007)&nbsp;; Note 98.39 (lecture 1987-1997)&nbsp;; Note 16.28 pour la dictée de 2015 (chiffres révisés par la Note 22.37, qui fait foi). Les seuils de la Note 08.38 («&nbsp;moins de deux&nbsp;», «&nbsp;plus de vingt-cinq&nbsp;» erreurs) diffèrent de ceux de la Note 22.37&nbsp;: les deux séries ne sont pas mêlées.

**CEDRE.** DEPP, Notes d'Information 16.20, 22.28 (maîtrise de la langue en fin d'école, 2003-2021) et 22.29 (compétences langagières et littératie en fin de collège, 2015-2021, cadre revu en 2015&nbsp;: pas de comparaison avec 2003 et 2009), leurs données et les rapports techniques de 2021&nbsp;; significativité lue dans les tableaux de la DEPP, où les évolutions significatives sont en gras.

**Évaluations nationales.** DEPP, Note d'Information 26.21 et document de travail sur l'évaluation de début de sixième 2025 (scores 2017-2025, échelle fixée à 250 en 2017&nbsp;; maîtrise par domaine en 2025)&nbsp;; Note 26.22 et document de travail 2025-E15 (test de positionnement de seconde, échelle fixée à 250 en 2019)&nbsp;; Note 25.66 (pratiques de lecture, septembre 2023).

**PIRLS et PISA.** DEPP, Notes 17.24 et 23.21 (PIRLS)&nbsp;; OCDE, *PISA 2025 Results*, volume&nbsp;I, tableau I.B1.2a.37 (compréhension de l'écrit, 2000-2025, avec erreurs types) et annexe A1 (tendances de lecture 2018-2025)&nbsp;; *21st-Century Readers* (OCDE, 2021), tableaux B.4.4a (indice de plaisir de lire, déclaré comparable de 2009 à 2018) et B.4.8 (temps de lecture pour le plaisir, 2000, 2009, 2018). PISA 2000-2012&nbsp;: aucune baisse significative, d'après un test de l'auteur sur les erreurs types publiées, sans erreur de liaison&nbsp;; ce test détecte une baisse plus facilement que celui de l'OCDE, qui l'inclut. Temps de lecture pour le plaisir&nbsp;: heures estimées par l'OCDE à partir des classes de réponse&nbsp;; significativité marquée dans son tableau. Numérique de loisir&nbsp;: bases PISA 2022 et 2025 (fichiers élèves publics), questions ST326Q05 et ST326Q06, mêmes modalités les deux années, en quatre tranches fixées avant le calcul&nbsp;; dix valeurs plausibles, 80&nbsp;poids répliqués, erreur de liaison 2022-2025 déduite du tableau de l'OCDE&nbsp;; témoin&nbsp;: les moyennes de la France publiées par l'OCDE, retrouvées au centième&nbsp;; sensibilité à la non-réponse en classant tous les non-répondants dans la tranche la plus haute, puis la plus basse.

**Lecture de livres et smartphone.** Ministère de la Culture, enquêtes Pratiques culturelles des Français, tableaux d'évolution 1973-2008 (lecture de livres, 15-24 ans) et Lombardo et Wolff, *Cinquante ans de pratiques culturelles en France* (2020) pour la rupture de série&nbsp;; CREDOC, Baromètre du numérique 2015 (tableau&nbsp;3, 12-17 ans, 2011-2015), confirmé par le dossier de l'ARCEP de 2013.

**Textes donnés à lire.** Base Emmanuelle, bibliothèque Diderot de Lyon (page d'accueil et recherche dans la base)&nbsp;; catalogue général de la BnF, interrogé par son service SRU, avec une liste de manuels témoins fixée avant la recherche&nbsp;; code de la propriété intellectuelle, articles L.&nbsp;122-5-3, R.&nbsp;122-27 et R.&nbsp;122-28&nbsp;; conditions d'utilisation de Gallica&nbsp;; *Livres Hebdo*, 15&nbsp;avril 2026, pour la liste d'opposition de la Société des gens de lettres. Club des Cinq&nbsp;: Maisonneuve, «&nbsp;Le Club des Cinq (Enid Blyton), une série entre nostalgie et modernité&nbsp;», *Publije*, n°&nbsp;3, 2014. Manulex&nbsp;: Lété, Sprenger-Charolles et Colé, *Behavior Research Methods*, 2004. Hayes, Wolfer et Wolfe, *American Educational Research Journal*, 1996. Effectifs&nbsp;: comparaison de deux moyennes, test bilatéral à 5&nbsp;%, puissance de 80&nbsp;%.

**Recherche.** Sullivan et Brown, *British Educational Research Journal*, 2015&nbsp;; Mol et Bus, *Psychological Bulletin*, 2011&nbsp;; Altamura, Vargas et Salmerón, *Review of Educational Research*, 2023&nbsp;; Delgado, Vargas, Ackerman et Salmerón, *Educational Research Review*, 2018&nbsp;; Madigan et al., *JAMA Pediatrics*, 2020.

Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent d'un calcul de l'auteur, dont l'extrait est archivé avec ses empreintes&nbsp;; le script qui écrit la page vérifie chaque affirmation chiffrée et s'arrête si elle n'est plus vraie. Le plan a été soumis à une contre-analyse externe avant le calcul, puis un protocole a été écrit avant le calcul, avec ses règles de verdict. Toutes les valeurs ont été lues deux fois, par deux extracteurs indépendants&nbsp;; ce contrôle a détecté l'erreur qu'on y avait introduite volontairement.

{{< reutiliser figures="figures_langue" jeu="langue_eleves" sources="DEPP, OCDE (PISA), IEA (PIRLS), ministère de la Culture, CREDOC" donnees="Dictée de CM2 1987-2021 (total et erreurs lexicales), lecture en CM2 1987-2007, CEDRE fin d'école et fin de collège, PIRLS, évaluation de sixième et maîtrise par domaine, test de seconde, PISA compréhension de l'écrit 2000-2025, temps de lecture et plaisir de lire, lecteurs de 15-24 ans, smartphone des 12-17 ans, pratiques de lecture 2023, numérique de loisir dans PISA 2022 et 2025 ; le même contenu existe en CSV, au format long." >}}
La langue des élèves ne recule pas d'un bloc&nbsp;: à la même dictée de CM2, les erreurs passent de {{< lan-val "tot87" >}} à {{< lan-val "tot21" >}} entre 1987 et 2021&nbsp;; sur ces {{< lan-val "h_tot" >}}&nbsp;erreurs supplémentaires, {{< lan-val "h_lex" >}} portent sur l'orthographe des mots&nbsp;; le détail par type d'erreur n'existe que pour 1987-2007, où la hausse est surtout grammaticale. Plusieurs reculs étaient déjà engagés avant la généralisation du smartphone, qui ne peut donc pas être la seule cause de leur apparition&nbsp;; PISA ne baisse qu'après 2012, quand d'autres évaluations, à l'école et en fin de collège, ne reculent pas significativement sur des périodes qui recouvrent en partie cette baisse. Aucune des séries publiques recensées ne permet de suivre l'évolution du vocabulaire des élèves.
{{< /reutiliser >}}
