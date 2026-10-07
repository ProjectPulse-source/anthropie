---
title: "Le niveau des élèves baisse-t-il ?"
description: "PISA 2025, tests d'entrée en seconde, TIMSS Advanced : ce que les séries officielles disent du niveau des élèves en France. De 2015 à 2025, les jeunes de 15 ans ont perdu {niv.lect_v15} points en lecture et {niv.math_v15} en mathématiques ; en mathématiques, l'une des plus fortes baisses de l'OCDE. Mais le test d'entrée en seconde ne dit pas la même chose. Données OCDE et DEPP, recalculées."
chapo: "Selon PISA, oui. De 2015 à 2025, les jeunes Français de 15 ans ont perdu {niv.lect_v15} points en compréhension de l'écrit, {niv.math_v15} en mathématiques et {niv.sci_v15} en sciences. En lecture et en sciences, la baisse ressemble à celle de la plupart des pays de l'OCDE ; en mathématiques, elle compte parmi les plus fortes. La France perd aussi bien plus de très bons élèves qu'ailleurs : la part des meilleurs lecteurs est passée de {niv.lect_haut15} % à {niv.lect_haut25} %. Mais les évaluations ne racontent pas toutes la même histoire : sur la même génération, le test national d'entrée en seconde baisse en français comme PISA, et progresse en mathématiques quand PISA recule."
date: 2026-10-08T00:00:00+02:00
lastmod: 2026-10-08
og_title: "Le niveau des élèves baisse-t-il ? PISA 2025, seconde, comparaison OCDE — S. Lalut"
og_image: "images/og-niveau-eleves.jpg"
og_image_alt: "Carte de partage : « Le niveau des élèves baisse-t-il ? » — baisse du score PISA de 2015 à 2025 en lecture, en mathématiques et en sciences, France en orange contre la médiane des pays de l'OCDE en gris ; en mathématiques, la France recule plus que la plupart des pays."
# Deuxième onglet du bloc École et lycée, né d'un avis externe déposé par l'auteur le 07/10/2026.
# Recherche : D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_NIVEAU_2026-10-07 (protocole écrit avant calcul, commit 2986dfc ;
# verdict ; pièces archivées avec empreintes). Aucun chiffre saisi : jetons {niv.*} et shortcode niv-val
# (scripts/update_niveau_eleves.py, extrait figé et empreintes dans scripts/sources_niveau_eleves/).
# Français seulement : débat, programme et statistique français (exclusion déclarée).
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
donnees: [niveau_eleves]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "niveau_eleves"
  nom: "Niveau des élèves en France : PISA 2000-2025 et comparaison OCDE, tests de positionnement de seconde, TIMSS Advanced, recrutement des professeurs"
  description: "Séries officielles reprises et recalculées : scores PISA de la France et de la moyenne de l'OCDE depuis le premier cycle de chaque domaine, variation 2015-2025 des 38 pays de l'OCDE, parts d'élèves en difficulté et de meilleurs élèves, écart de score lié au milieu social ; scores moyens au test de positionnement de seconde 2019-2025 ; écarts entre générations calculés par la DEPP ; TIMSS Advanced 1995 et 2015 ; candidats et admis au CAPES externe, contractuels, enseignants non pleinement qualifiés, manque d'enseignants déclaré."
  couverture_temporelle: "1995/2025"
  couverture_spatiale: "France ; pays de l'OCDE"
  variables:
    - {nom: "Score moyen PISA", unite: "points", description: "compréhension de l'écrit, culture mathématique, culture scientifique ; France, moyenne de l'OCDE, pays membres"}
    - {nom: "Élèves en difficulté et meilleurs élèves", unite: "% des élèves de 15 ans", description: "sous le niveau 2 ; niveaux 5 et 6"}
    - {nom: "Score moyen au test de positionnement de seconde", unite: "points (échelle fixée à 250 en 2019)", description: "français et mathématiques, voie générale et technologique, voie professionnelle"}
    - {nom: "Candidats présents par admis", unite: "ratio", description: "CAPES externe, cinq disciplines, sessions 2010-2012 et 2023-2025"}
  sources:
    - "https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en.html"
    - "https://www.education.gouv.fr/depp/pisa-2025-les-acquis-des-eleves-de-15-ans-en-comprehension-de-l-ecrit-et-en-culture-mathematique-en-505645"
    - "https://www.education.gouv.fr/depp/test-de-positionnement-de-seconde-2025-des-resultats-en-baisse-en-francais-dans-les-deux-voies-et-en-505001"
    - "https://www.education.gouv.fr/depp/reperes-et-references-statistiques-2026-505320"
    - "https://timssandpirls.bc.edu/timss2015/advanced/"
  mots: ["niveau des élèves", "PISA", "PISA 2025", "baisse du niveau", "test de positionnement", "seconde", "lycée", "mathématiques", "lecture", "DEPP", "OCDE", "CAPES"]
  fichiers: ["niveau_eleves.csv", "niveau_eleves.json"]
  apropos: "niveau scolaire des élèves en France"
faq:
  - question: "Le niveau des élèves baisse-t-il en France ?"
    answer: "Oui selon PISA : de 2015 à 2025, le score moyen des jeunes de 15 ans a baissé de {niv.lect_v15} points en compréhension de l'écrit, de {niv.math_v15} en culture mathématique et de {niv.sci_v15} en culture scientifique, trois baisses statistiquement significatives selon l'OCDE. Sur une période plus longue, la baisse atteint {niv.lect_vlong} points en lecture depuis 2000 et {niv.math_vlong} en mathématiques depuis 2003."
  - question: "La France baisse-t-elle plus que les autres pays ?"
    answer: "En lecture et en sciences, non : sa baisse depuis 2015 se situe dans la moitié centrale des 38 pays de l'OCDE, en lecture tout près de sa limite. En mathématiques, oui : avec {niv.math_v15} points, sa baisse dépasse, sur les estimations ponctuelles, celle de {niv.math_mieux} des {niv.n_autres} autres pays membres, quand la moitié des pays perdent moins de {niv.math_med} points ; l'OCDE ne publie pas de test de cet écart."
  - question: "Les meilleurs élèves baissent-ils aussi ?"
    answer: "Oui, et plus qu'ailleurs. La part des élèves de 15 ans aux deux niveaux les plus élevés de PISA est passée de {niv.lect_haut15} % à {niv.lect_haut25} % en compréhension de l'écrit entre 2015 et 2025, et de {niv.math_haut15} % à {niv.math_haut25} % en mathématiques ; dans la moyenne de l'OCDE, de {niv.lect_ohaut15} % à {niv.lect_ohaut25} % et de {niv.math_ohaut15} % à {niv.math_ohaut25} %."
  - question: "PISA mesure-t-il le niveau des lycéens ?"
    answer: "En grande partie : PISA évalue les jeunes de 15 ans, et en France {niv.lycee} % de l'échantillon de 2025 était au lycée, dont {niv.seconde_gt} % en seconde générale et technologique. Le test de positionnement passé par tous les élèves entrant en seconde donne une autre mesure : sur la même génération, il baisse en français comme PISA, mais il monte en mathématiques quand PISA baisse."
  - question: "La baisse vient-elle du recrutement des professeurs ?"
    answer: "Les données publiques ne permettent pas de le dire : aucune ne relie un enseignant aux résultats de ses élèves, ni ne mesure le niveau de formation des recrutés. Elles montrent seulement que le nombre de candidats présents par admis au CAPES externe a diminué de {niv.p1_min} % à {niv.p1_max} % entre 2010-2012 et 2023-2025 selon la discipline, et que la part des contractuels parmi les enseignants du second degré public est passée de {niv.contr_0} % en {niv.contr_a0} à {niv.contr_1} % en {niv.contr_a1}."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "ecole"
  rang: 20
  nature: "Séries officielles reprises et recalculées (OCDE, DEPP, IEA) ; protocole écrit avant calcul"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Le niveau des élèves baisse-t-il ?"
  court: "Niveau"
  role: "PISA, seconde, recrutement"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Relevé du&nbsp;: {{< niv-val "date_donnees" >}}</span> OCDE&nbsp;: PISA 2025, volume&nbsp;I, et <em>Regards sur l'éducation</em> 2026&nbsp;; DEPP&nbsp;: Notes d'Information 26-39, 26-40 et 26-22, <em>Repères et références statistiques</em>&nbsp;; IEA&nbsp;: TIMSS Advanced 2015. Télécharger&nbsp;: <a href="/niveau_eleves.csv">CSV</a> · <a href="/niveau_eleves.json">JSON</a> · <a href="#sources">méthode</a></p>

## Le niveau baisse-t-il vraiment&nbsp;? {#baisse}

<figure class="figure-ciseau">
  <img src="/img/niveau-baisse.svg" alt="Pour chaque domaine de PISA, variation du score moyen de 2015 à 2025 des {{< niv-val "n_ocde" >}} pays de l'OCDE, France en orange : compréhension de l'écrit −{{< niv-val "lect_v15" >}} points ({{< niv-val "lect_rang" >}}e plus forte baisse), culture mathématique −{{< niv-val "math_v15" >}} ({{< niv-val "math_rang" >}}e), culture scientifique −{{< niv-val "sci_v15" >}} ({{< niv-val "sci_rang" >}}e)." width="720" height="344" loading="lazy">
  <figcaption>Variation du score moyen PISA entre 2015 et 2025, pays membres de l'OCDE (OCDE, PISA 2025, volume&nbsp;I).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De 2015 à 2025, les jeunes Français de 15 ans ont perdu {{< niv-val "lect_v15" >}}&nbsp;points en compréhension de l'écrit, {{< niv-val "math_v15" >}} en culture mathématique et {{< niv-val "sci_v15" >}} en culture scientifique&nbsp;; en lecture et en sciences, la baisse française est dans la moitié centrale des pays de l'OCDE, en mathématiques elle compte parmi les plus fortes&nbsp;: sur les estimations ponctuelles, elle dépasse celle de {{< niv-val "math_mieux" >}} des {{< niv-val "n_autres" >}} autres pays.

</div>

Selon PISA, oui. Les trois baisses qu'il mesure entre 2015 et 2025 sont statistiquement significatives selon l'OCDE&nbsp;: le score moyen de la France passe de {{< niv-val "lect_15" >}} à {{< niv-val "lect_25" >}} en compréhension de l'écrit, de {{< niv-val "math_15" >}} à {{< niv-val "math_25" >}} en culture mathématique, de {{< niv-val "sci_15" >}} à {{< niv-val "sci_25" >}} en culture scientifique. L'essentiel s'est produit depuis 2018&nbsp;: entre 2022 et 2025 encore, la lecture a perdu {{< niv-val "lect_v22" >}}&nbsp;points et les mathématiques {{< niv-val "math_v22" >}}, quand les sciences sont restées stables.

Sur une période plus longue, le constat est plus nuancé. La lecture a perdu {{< niv-val "lect_vlong" >}}&nbsp;points depuis {{< niv-val "lect_an0" >}} et les mathématiques {{< niv-val "math_vlong" >}} depuis {{< niv-val "math_an0" >}}, deux baisses significatives. En sciences, l'écart depuis {{< niv-val "sci_an0" >}} ({{< niv-val "sci_vlong" >}}&nbsp;points) ne l'est pas.

Ces chiffres viennent d'une enquête par échantillon, passée sur ordinateur depuis 2015. L'OCDE ne signale pas l'échantillon français de 2025 comme hors normes, et publie les variations de la France sur toute la série.

## La France baisse-t-elle plus que les autres&nbsp;? {#comparaison}

Le récit courant, «&nbsp;tout le monde baisse&nbsp;», est juste en moyenne&nbsp;: la moyenne de l'OCDE perd {{< niv-val "lect_ocde_v15" >}}&nbsp;points en lecture et {{< niv-val "math_ocde_v15" >}} en mathématiques de 2015 à 2025. Il ne suffit pas pour la France.

Pour le vérifier, on peut placer la baisse française parmi celles des {{< niv-val "n_ocde" >}} pays membres de l'OCDE, sans s'arrêter au rang du score, qui dépend des autres pays. En **sciences**, la France ({{< niv-val "sci_v15" >}}&nbsp;points de moins) est dans la moitié centrale des pays. En **lecture**, avec {{< niv-val "lect_v15" >}}&nbsp;points de moins, elle est pratiquement à la frontière entre la moitié centrale et le quart des pays aux plus fortes baisses, une frontière qui ne départage rien. En **mathématiques**, la France sort de la moyenne&nbsp;: {{< niv-val "math_v15" >}}&nbsp;points de moins, quand la moitié des pays en perdent moins de {{< niv-val "math_med" >}}. Sur les estimations ponctuelles, sa baisse dépasse celle de {{< niv-val "math_mieux" >}} des {{< niv-val "n_autres" >}} autres pays, et sa place est la même parmi les seuls pays de l'Union européenne membres de l'OCDE ou sans les {{< niv-val "n_etoile" >}} pays dont l'échantillon ne respecte pas toutes les normes de l'enquête. Ce rang reste descriptif&nbsp;: l'écart entre la France et le quart des pays aux plus fortes baisses ({{< niv-val "math_ecart_q1" >}}&nbsp;points) est du même ordre que la marge d'erreur de la variation française (erreur type de {{< niv-val "math_se" >}}&nbsp;points).

L'OCDE ne publie pas de test de l'écart entre la baisse française et celle des autres pays&nbsp;: le classement des baisses est un calcul de l'auteur sur ses tableaux.

## Que disent les tests d'entrée en seconde&nbsp;? {#seconde}

<figure class="figure-ciseau">
  <img src="/img/niveau-seconde.svg" alt="Barres horizontales, écart standardisé entre la génération de 2021-2022 et celle de 2024-2025, calculé par la DEPP. Français : test de seconde −{{< niv-val "g_tf" >}}, PISA compréhension de l'écrit −{{< niv-val "g_pf" >}}. Mathématiques : test de seconde +{{< niv-val "g_tm" >}}, PISA culture mathématique −{{< niv-val "g_pm" >}}." width="720" height="302" loading="lazy">
  <figcaption>Écart entre deux générations d'élèves, en centièmes d'écart-type, test de positionnement de seconde et PISA (DEPP, Note d'Information 26-40).</figcaption>
</figure>

PISA parle bien du lycée&nbsp;: en France, {{< niv-val "lycee" >}}&nbsp;% des jeunes de 15 ans de l'échantillon de 2025 étaient au lycée, dont {{< niv-val "seconde_gt" >}}&nbsp;% en seconde générale et technologique et {{< niv-val "seconde_pro" >}}&nbsp;% en seconde professionnelle. Une autre mesure existe à cette entrée&nbsp;: depuis 2018, tous les élèves de seconde passent en septembre un test de positionnement en français et en mathématiques, sur une échelle fixée en 2019.

Les deux mesures se recoupent pour une même génération. Les jeunes évalués par PISA en 2022 sont, pour la plupart, entrés en seconde en 2021&nbsp;; ceux de 2025, en 2024. La DEPP a fait ce rapprochement. En **français**, les deux baissent&nbsp;: en seconde générale et technologique, le score moyen passe de {{< niv-val "sf_21" >}} en 2021 à {{< niv-val "sf_24" >}} en 2024, et PISA perd {{< niv-val "lect_v22" >}}&nbsp;points en lecture. En **mathématiques**, ils divergent&nbsp;: le test de seconde passe de {{< niv-val "sm_21" >}} à {{< niv-val "sm_24" >}}, quand PISA perd {{< niv-val "math_v22" >}}&nbsp;points. Ramenés à une même unité, la DEPP trouve +{{< niv-val "g_tm" >}} pour le test de seconde et −{{< niv-val "g_pm" >}} pour PISA en mathématiques, et écrit que la baisse de PISA «&nbsp;contraste avec la légère hausse constatée par le test de positionnement en début de seconde entre les rentrées 2021 et 2024&nbsp;».

Ce désaccord ne signifie pas qu'une évaluation se trompe. Les deux épreuves ne mesurent ni exactement les mêmes compétences, ni la même population (un âge pour PISA, une classe pour le test de seconde), ni dans le même contexte&nbsp;: PISA n'a aucun enjeu pour l'élève, le test de seconde sert à son professeur. Leur divergence montre qu'une mesure unique ne suffit pas à résumer le «&nbsp;niveau&nbsp;» des élèves&nbsp;; la DEPP ne l'explique pas. Plus récemment, la DEPP note une baisse en français en 2025 (score de {{< niv-val "sf_25" >}} en seconde générale et technologique, retour au niveau de 2019) et une stabilité en mathématiques. Elle ne publie pas de test de significativité pour ce test, passé par tous les élèves.

## Qui décroche&nbsp;: les plus faibles ou les meilleurs&nbsp;? {#qui-decroche}

<figure class="figure-ciseau">
  <img src="/img/niveau-sommet.svg" alt="Barres, en % des élèves de 15 ans, 2015 puis 2025. Lecture, sous le niveau 2 : France {{< niv-val "lect_bas15" >}} puis {{< niv-val "lect_bas25" >}}, OCDE {{< niv-val "lect_obas15" >}} puis {{< niv-val "lect_obas25" >}} ; niveaux 5-6 : France {{< niv-val "lect_haut15" >}} puis {{< niv-val "lect_haut25" >}}, OCDE {{< niv-val "lect_ohaut15" >}} puis {{< niv-val "lect_ohaut25" >}}. Mathématiques, sous le niveau 2 : France {{< niv-val "math_bas15" >}} puis {{< niv-val "math_bas25" >}} ; niveaux 5-6 : France {{< niv-val "math_haut15" >}} puis {{< niv-val "math_haut25" >}}." width="720" height="352" loading="lazy">
  <figcaption>Part des élèves de 15 ans sous le niveau 2 et aux niveaux 5 et 6, France et moyenne de l'OCDE, 2015 et 2025 (OCDE, PISA 2025).</figcaption>
</figure>

Les deux. Le bas de la distribution gonfle&nbsp;: la part des élèves sous le niveau&nbsp;2, celui où l'OCDE situe la maîtrise de base, passe de {{< niv-val "lect_bas15" >}}&nbsp;% à {{< niv-val "lect_bas25" >}}&nbsp;% en lecture et de {{< niv-val "math_bas15" >}}&nbsp;% à {{< niv-val "math_bas25" >}}&nbsp;% en mathématiques. C'est le mouvement le plus large, et il ressemble à celui de l'OCDE.

Le haut fond, et c'est là que la France se distingue. La part des meilleurs élèves, aux niveaux 5 et 6, a été presque divisée par trois en lecture, de {{< niv-val "lect_haut15" >}}&nbsp;% à {{< niv-val "lect_haut25" >}}&nbsp;%, et plus que divisée par deux en mathématiques, de {{< niv-val "math_haut15" >}}&nbsp;% à {{< niv-val "math_haut25" >}}&nbsp;%. Dans la moyenne de l'OCDE, la perte au sommet est bien plus faible&nbsp;: de {{< niv-val "lect_ohaut15" >}}&nbsp;% à {{< niv-val "lect_ohaut25" >}}&nbsp;% en lecture, de {{< niv-val "math_ohaut15" >}}&nbsp;% à {{< niv-val "math_ohaut25" >}}&nbsp;% en mathématiques.

**L'écart lié au milieu social s'est réduit, mais pas parce que le bas remonte.** En lecture, l'écart de score entre le quart des élèves les plus favorisés et le quart le moins favorisé est passé de {{< niv-val "lect_ec15" >}} à {{< niv-val "lect_ec25" >}}&nbsp;points entre 2015 et 2025 (il est de {{< niv-val "lect_oec25" >}}&nbsp;points dans la moyenne de l'OCDE en 2025). La réduction est significative dans les trois domaines, et elle correspond à une baisse beaucoup plus forte des élèves favorisés&nbsp;: en lecture, le quart le plus favorisé a perdu {{< niv-val "lect_qh" >}}&nbsp;points, le quart le moins favorisé {{< niv-val "lect_qb" >}}&nbsp;; en mathématiques, {{< niv-val "math_qh" >}} et {{< niv-val "math_qb" >}}. En lecture, le même resserrement par le haut existe dans la moyenne de l'OCDE, moins marqué&nbsp;; en mathématiques, les deux quarts de l'OCDE reculent autant. La France s'en distingue par l'ampleur&nbsp;: son quart favorisé recule presque deux fois plus que celui de l'OCDE ({{< niv-val "lect_qh" >}} contre {{< niv-val "lect_oqh" >}}&nbsp;points en lecture, {{< niv-val "math_qh" >}} contre {{< niv-val "math_oqh" >}} en mathématiques), quand son quart défavorisé recule comme lui ({{< niv-val "lect_qb" >}} contre {{< niv-val "lect_oqb" >}}, {{< niv-val "math_qb" >}} contre {{< niv-val "math_oqb" >}}). Une inégalité qui se réduit parce que tous reculent, les plus favorisés davantage, n'est pas un progrès pour les moins favorisés.

## Et à la fin du lycée&nbsp;? {#fin-du-lycee}

La seule mesure internationale date. TIMSS Advanced, l'enquête de l'IEA sur les élèves scientifiques en fin d'études secondaires, a évalué la terminale S en 1995 et en 2015&nbsp;: le score moyen de la France est passé de {{< niv-val "timss_math_95" >}} à {{< niv-val "timss_math_15" >}} en mathématiques ({{< niv-val "timss_math_v" >}}&nbsp;points de moins) et de {{< niv-val "timss_phys_95" >}} à {{< niv-val "timss_phys_15" >}} en physique ({{< niv-val "timss_phys_v" >}}&nbsp;points de moins), deux baisses significatives. L'enquête n'a pas été refaite depuis, et la série S a disparu avec la réforme du lycée.

La journée défense et citoyenneté évalue chaque année la lecture des jeunes d'environ 17 ans. Son test a changé en 2019, et la DEPP indique que les résultats de 2024 ne se comparent pas à ceux des années précédentes&nbsp;: elle ne permet pas de suivre une tendance.

## Les professeurs sont-ils recrutés comme avant&nbsp;? {#recrutement}

Les données publiques ne permettent ni de relier le recrutement des professeurs aux résultats des élèves, aucune ne rapprochant un enseignant de ses élèves, ni de mesurer le niveau de formation des enseignants recrutés. Elles décrivent deux évolutions. Au CAPES externe, le nombre de candidats présents par admis a diminué de {{< niv-val "p1_min" >}}&nbsp;% à {{< niv-val "p1_max" >}}&nbsp;% entre les sessions 2010-2012 et 2023-2025, selon les cinq disciplines suivies (mathématiques, physique-chimie, lettres modernes, histoire-géographie, anglais)&nbsp;: ce ratio mesure la concurrence au concours, pas le niveau des recrutés. La part des contractuels parmi les personnels enseignants du second degré public est passée de {{< niv-val "contr_0" >}}&nbsp;% en {{< niv-val "contr_a0" >}} à {{< niv-val "contr_1" >}}&nbsp;% en {{< niv-val "contr_a1" >}}&nbsp;; l'OCDE les range parmi les enseignants «&nbsp;non pleinement qualifiés&nbsp;» ({{< niv-val "nq_fr" >}}&nbsp;% dans le secondaire public en France, {{< niv-val "nq_ocde" >}}&nbsp;% en moyenne dans l'OCDE), une catégorie administrative qui désigne l'absence du concours, non un diplôme ou une compétence mesurés. Les concours, les classes et les heures de cours perdues sont traités dans la page [Manque-t-il des professeurs au lycée&nbsp;?](/manque-t-il-des-professeurs/).

## Ce que ces données ne disent pas {#limites}

- **Pourquoi le niveau baisse**&nbsp;: ni les moyens, ni les professeurs, ni les écrans, ni la pandémie ne peuvent être départagés avec ces séries. Elles mesurent un recul, pas sa cause.
- **La composition de la population évaluée**&nbsp;: PISA retient un âge, le test de seconde une classe. Si la part des élèves en retard, ou celle de chaque voie, a changé entre 2015 et 2025, le score moyen de PISA peut bouger sans que le niveau à classe égale change autant&nbsp;; cet effet n'est pas mesuré ici.
- **Le lien entre recrutement et niveau**&nbsp;: aucune donnée publique ne rapproche un enseignant des résultats de ses élèves.
- **L'effort fourni à l'épreuve**&nbsp;: PISA n'a pas d'enjeu pour l'élève&nbsp;; la DEPP publie des indicateurs sur l'effort déclaré, que cette page n'exploite pas.
- **Le niveau à la sortie du lycée aujourd'hui**&nbsp;: la dernière mesure internationale date de 2015, et la journée défense et citoyenneté ne se compare pas dans le temps.
- **Le baccalauréat**&nbsp;: un taux de réussite à un examen dont les règles changent ne mesure pas un niveau.

## Ce qu'il faut retenir {#retenir}

Le niveau mesuré par PISA a baissé en France depuis 2015 dans les trois domaines. En lecture et en sciences, la France suit le mouvement de la plupart des pays de l'OCDE&nbsp;; en mathématiques, sa baisse compte parmi les plus fortes. Ce qui distingue la France est au sommet&nbsp;: plus d'élèves en difficulté, comme ailleurs, mais beaucoup moins de très bons élèves, et des élèves favorisés qui reculent presque deux fois plus que dans l'OCDE. Les évaluations, enfin, ne disent pas toutes la même chose&nbsp;: à l'entrée du lycée, le test national de seconde confirme la baisse en français, pas en mathématiques.

## Questions fréquentes {#questions}

{{< faq-visible >}}

{{< appel-livre slug="la-societe-du-premier-coup" sur="Après un premier échec, qui peut recommencer ?" avis="non" offert="avant" >}}
Cette page mesure ce que savent les élèves à un moment donné. La question qui vient ensuite est celle des parcours&nbsp;: quand un élève échoue une première fois, à un examen, une orientation, une première année d'études, qui peut réellement recommencer, et à quel coût selon son milieu&nbsp;? Le livre montre que cette possibilité de recommencer n'est pas également distribuée.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**PISA.** OCDE, *PISA 2025 Results*, volume&nbsp;I (8&nbsp;septembre 2026), tableaux de l'annexe&nbsp;B1&nbsp;: scores moyens et variations (I.B1.2a.36 à 38), niveaux de compétence (I.B1.2a.33 à 35), statut économique, social et culturel (I.B1.2b.22 à 24). Une variation est dite significative quand elle dépasse 1,96 fois son erreur type, règle de l'OCDE. La moyenne de l'OCDE est celle des 35 pays comparables sur toute la période. Témoin&nbsp;: les séries de la France publiées par la DEPP (Notes d'Information 26-39 et 26-40), identiques à 0,04&nbsp;point près. Classes des élèves de l'échantillon&nbsp;: Note 26-40, figure&nbsp;1.

**Tests de positionnement de seconde.** DEPP, Note d'Information 26-22 et ses données (scores moyens 2019-2025, échelle fixée à 250 en 2019, voies générale et technologique et professionnelle), document de travail 2025-E15. Rapprochement avec PISA&nbsp;: Note 26-40, figure 11 web (deux voies ensemble). La DEPP précise que la comparaison stricte des mathématiques entre 2024 et 2025 n'est pas possible, une partie du test ayant été renouvelée.

**Fin du lycée.** IEA, *TIMSS Advanced 2015 International Results in Advanced Mathematics and Physics*&nbsp;; DEPP, Notes d'Information 16-34 et 16-35. Journée défense et citoyenneté&nbsp;: DEPP, Note d'Information 25-57 et notes antérieures.

**Recrutement.** DEPP, *Repères et références statistiques* 2011 à 2013 et 2024 à 2026 (concours de recrutement du second degré public selon les disciplines&nbsp;; troisième concours compté avec l'externe&nbsp;; Capes à affectation locale compris à partir de 2021), Note d'Information 11-24 pour la session 2010&nbsp;; la session 2012 de physique-chimie n'est pas publiée par la DEPP. Contractuels&nbsp;: RERS 2026, fiche 9.02. Enseignants non pleinement qualifiés&nbsp;: OCDE, *Regards sur l'éducation* 2026, chapitre sur la pénurie d'enseignants, tableau&nbsp;1 (France&nbsp;: année 2023-2024).

Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent d'un calcul de l'auteur, dont l'extrait est archivé avec ses empreintes&nbsp;; le script qui écrit la page vérifie chaque affirmation chiffrée et s'arrête si elle n'est plus vraie. Le protocole a été écrit avant le premier calcul, avec ses seuils. Les scores PISA de la France, les résultats des tests de seconde et les chiffres des concours ont été lus deux fois, par deux extracteurs indépendants, et les séries de la France ont été comparées entre l'OCDE et la DEPP&nbsp;; chacun de ces contrôles a détecté les erreurs qu'on y avait introduites volontairement.

{{< reutiliser figures="figures_niveau" jeu="niveau_eleves" sources="OCDE (PISA, Regards sur l'éducation), DEPP, IEA" donnees="Scores PISA de la France et de l'OCDE, variation 2015-2025 des 38 pays de l'OCDE, élèves en difficulté et meilleurs élèves, écart social, test de positionnement de seconde 2019-2025, écarts entre générations de la DEPP, TIMSS Advanced, candidats et admis au CAPES externe, contractuels, enseignants non pleinement qualifiés ; le même contenu existe en CSV, au format long." >}}
De 2015 à 2025, les jeunes Français de 15 ans ont perdu {{< niv-val "lect_v15" >}}&nbsp;points en compréhension de l'écrit, {{< niv-val "math_v15" >}} en mathématiques et {{< niv-val "sci_v15" >}} en sciences à l'enquête PISA&nbsp;; en mathématiques, la baisse française dépasse, sur les estimations ponctuelles, celle de {{< niv-val "math_mieux" >}} des {{< niv-val "n_autres" >}} autres pays de l'OCDE. La part des meilleurs élèves en lecture est passée de {{< niv-val "lect_haut15" >}}&nbsp;% à {{< niv-val "lect_haut25" >}}&nbsp;%. Sur la même génération, le test de positionnement de seconde baisse en français mais monte en mathématiques.
{{< /reutiliser >}}
