---
title: "Le niveau des élèves baisse-t-il ?"
description: "PISA 2025, TIMSS, PIRLS, tests d'entrée en seconde : ce que les évaluations disent du niveau des élèves en France. PISA, à 15 ans, perd {niv.lect_v15} points en lecture et {niv.math_v15} en mathématiques de 2015 à 2025 ; sur leurs derniers intervalles, TIMSS et PIRLS ne mettent pas en évidence de baisse significative. Ce que leur désaccord permet de conclure, et ce qu'il ne permet pas. Données OCDE, IEA et DEPP, recalculées."
chapo: "Selon PISA, oui : de 2015 à 2025, les jeunes Français de 15 ans ont perdu {niv.lect_v15} points en compréhension de l'écrit et {niv.math_v15} en mathématiques, une baisse significative. Mais les évaluations passées en classe, en CM1 et en quatrième, ne mettent pas en évidence la même baisse récente. Les évaluations se contredisent-elles vraiment ?"
date: 2026-10-08T00:00:00+02:00
lastmod: 2026-10-08
og_title: "Le niveau des élèves baisse-t-il ? PISA 2025, TIMSS, PIRLS, seconde — S. Lalut"
og_image: "images/og-niveau-eleves.jpg"
og_image_alt: "Carte de partage : « Le niveau des élèves baisse-t-il ? » — baisse du score PISA de 2015 à 2025 en lecture, en mathématiques et en sciences, France en orange contre la médiane des pays de l'OCDE en gris ; en mathématiques, la France recule plus que la plupart des pays."
# Deuxième onglet du bloc École et lycée, né d'un avis externe déposé par l'auteur le 07/10/2026.
# Recherche : D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_NIVEAU_2026-10-07 (protocoles 1 et 2 écrits avant calcul, commits
# 2986dfc et c586130 ; verdicts ; contre-expertise PRO-20261008-013238 ; pièces archivées avec empreintes). Aucun chiffre
# saisi : jetons {niv.*} et shortcode niv-val (scripts/update_niveau_eleves.py, extrait figé et empreintes dans
# scripts/sources_niveau_eleves/). Français seulement : débat, programme et statistique français (exclusion déclarée).
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
donnees: [niveau_eleves]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "niveau_eleves"
  nom: "Niveau des élèves en France : PISA 2000-2025 et comparaison OCDE, TIMSS et PIRLS, tests de positionnement de seconde, composition par classe, TIMSS Advanced, recrutement des professeurs"
  description: "Séries officielles reprises et recalculées : scores PISA de la France et de la moyenne de l'OCDE depuis le premier cycle de chaque domaine, variation 2015-2025 des 38 pays de l'OCDE, percentiles, parts d'élèves en difficulté et de meilleurs élèves, écart de score lié au milieu social, composition de l'échantillon par classe dans les trois domaines (2015 et 2025), effort déclaré ; TIMSS CM1 et quatrième, PIRLS CM1 ; scores moyens au test de positionnement de seconde 2019-2025 ; TIMSS Advanced 1995 et 2015 ; candidats et admis au CAPES externe, contractuels, enseignants non pleinement qualifiés."
  couverture_temporelle: "1995/2025"
  couverture_spatiale: "France ; pays de l'OCDE"
  variables:
    - {nom: "Score moyen PISA", unite: "points", description: "compréhension de l'écrit, culture mathématique, culture scientifique ; France, moyenne de l'OCDE, pays membres ; percentiles"}
    - {nom: "Score moyen TIMSS et PIRLS", unite: "points", description: "France, CM1 et quatrième, derniers cycles et séries longues, avec la significativité publiée"}
    - {nom: "Composition de l'échantillon PISA par classe", unite: "% et points", description: "trois domaines, 2015 et 2025 (données individuelles) ; culture scientifique (DEPP)"}
    - {nom: "Score moyen au test de positionnement de seconde", unite: "points (échelle fixée à 250 en 2019)", description: "français et mathématiques, voie générale et technologique, voie professionnelle"}
    - {nom: "Candidats présents par admis", unite: "ratio", description: "CAPES externe, cinq disciplines, sessions 2010-2012 et 2023-2025"}
  sources:
    - "https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en.html"
    - "https://www.education.gouv.fr/depp/pisa-2025-les-acquis-des-eleves-de-15-ans-en-comprehension-de-l-ecrit-et-en-culture-mathematique-en-505645"
    - "https://timss2023.org/"
    - "https://pirls2021.org/"
    - "https://www.education.gouv.fr/depp/test-de-positionnement-de-seconde-2025-des-resultats-en-baisse-en-francais-dans-les-deux-voies-et-en-505001"
    - "https://www.education.gouv.fr/depp/reperes-et-references-statistiques-2026-505320"
    - "https://timssandpirls.bc.edu/timss2015/advanced/"
  mots: ["niveau des élèves", "PISA", "PISA 2025", "TIMSS", "PIRLS", "baisse du niveau", "test de positionnement", "seconde", "lycée", "mathématiques", "lecture", "DEPP", "OCDE", "CAPES"]
  fichiers: ["niveau_eleves.csv", "niveau_eleves.json"]
  apropos: "niveau scolaire des élèves en France"
faq:
  - question: "Le niveau des élèves baisse-t-il en France ?"
    answer: "Selon PISA, oui : de 2015 à 2025, le score moyen des jeunes de 15 ans a baissé de {niv.lect_v15} points en compréhension de l'écrit, de {niv.math_v15} en culture mathématique et de {niv.sci_v15} en culture scientifique, trois baisses statistiquement significatives selon l'OCDE. Sur leurs derniers intervalles, PIRLS en CM1 (2016-2021) et TIMSS en CM1 et en quatrième (2019-2023) ne mettent pas en évidence de baisse significative, ce qui ne prouve pas que leurs tendances diffèrent de celle de PISA. Sur la longue période, elles baissent elles aussi."
  - question: "Les autres évaluations confirment-elles PISA ?"
    answer: "Pas sur la période récente. PIRLS en CM1 passe de {niv.pirls_16} à {niv.pirls_21} points entre 2016 et 2021, TIMSS en CM1 de {niv.tcm1_19} à {niv.tcm1_23} et TIMSS en quatrième de {niv.t4e_19} à {niv.t4e_23} en mathématiques entre 2019 et 2023 : aucune variation n'est significative. Le score du test d'entrée en seconde monte en mathématiques, sans test publié. Ces évaluations portent sur d'autres élèves et d'autres années que PISA : elles ne le réfutent pas, mais elles interdisent de dire que toutes les mesures montrent la même chute."
  - question: "La France baisse-t-elle plus que les autres pays ?"
    answer: "Elle perd davantage de points que la moyenne de l'OCDE dans les trois domaines entre 2015 et 2025 : {niv.lect_v15} contre {niv.lect_ocde_v15} en compréhension de l'écrit, {niv.math_v15} contre {niv.math_ocde_v15} en mathématiques, {niv.sci_v15} contre {niv.sci_ocde_v15} en sciences. Parmi les pays pris un à un, sa baisse se situe, sur les estimations ponctuelles, près de la limite du quart des plus fortes en lecture, parmi ce quart en mathématiques, et dans la moitié centrale en sciences. Ces rangs ne constituent pas un test de la différence entre pays, que l'OCDE ne publie pas."
  - question: "La baisse vient-elle du changement de répartition des élèves entre classes ?"
    answer: "Non. Entre 2015 et 2025, la part des jeunes de 15 ans encore en troisième ou avant est passée de {niv.comp_retard15} % à {niv.comp_retard25} % de l'échantillon PISA. Ces élèves ont des scores plus bas : leur recul relève la moyenne. À la répartition entre classes de 2015, la baisse passe de {niv.p5_math_obs} à {niv.p5_math_rec} points en mathématiques, et de {niv.p5_lect_obs} à {niv.p5_lect_rec} en lecture. À la composition de 2015 pour la classe, le sexe, le diplôme des parents et l'origine migratoire, elle revient à peu près au niveau observé ({niv.p6_math_rec} points en mathématiques, {niv.p6_lect_rec} en lecture). Ces calculs décrivent, ils n'attribuent pas de cause ; ils ne reconstituent pas les parcours scolaires et dépendent de la qualité des réponses sur les familles."
  - question: "Les meilleurs élèves baissent-ils aussi ?"
    answer: "Oui, et plus qu'ailleurs. La part des élèves de 15 ans aux deux niveaux les plus élevés de PISA est passée de {niv.lect_haut15} % à {niv.lect_haut25} % en compréhension de l'écrit entre 2015 et 2025, et de {niv.math_haut15} % à {niv.math_haut25} % en mathématiques ; dans la moyenne de l'OCDE, de {niv.lect_ohaut15} % à {niv.lect_ohaut25} % et de {niv.math_ohaut15} % à {niv.math_ohaut25} %."
  - question: "La baisse vient-elle du recrutement des professeurs ?"
    answer: "Les données publiques ne permettent pas de le dire : aucune ne relie un enseignant aux résultats de ses élèves, ni ne mesure le niveau de formation des recrutés. Elles montrent seulement que le nombre de candidats présents par admis au CAPES externe a diminué de {niv.p1_min} % à {niv.p1_max} % entre 2010-2012 et 2023-2025 selon la discipline, et que la part des contractuels parmi les enseignants du second degré public est passée de {niv.contr_0} % en {niv.contr_a0} à {niv.contr_1} % en {niv.contr_a1}."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "ecole"
  rang: 20
  nature: "Séries officielles reprises et recalculées (OCDE, IEA, DEPP) ; sept protocoles écrits avant calcul"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Le niveau des élèves baisse-t-il ?"
  court: "Niveau"
  role: "PISA, TIMSS, PIRLS, seconde"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Relevé du&nbsp;: {{< niv-val "date_donnees" >}}</span> OCDE&nbsp;: PISA 2025, volume&nbsp;I, et <em>Regards sur l'éducation</em> 2026&nbsp;; IEA&nbsp;: TIMSS 2023, TIMSS Advanced 2015&nbsp;; DEPP&nbsp;: PIRLS 2021, Notes d'Information 16-37, 26-39, 26-40 et 26-22, <em>Repères et références statistiques</em>. Télécharger&nbsp;: <a href="/niveau_eleves.csv">CSV</a> · <a href="/niveau_eleves.json">JSON</a> · <a href="#sources">méthode</a></p>

## Que mesure PISA, et combien baisse-t-il&nbsp;? {#baisse}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/niveau-baisse-m.svg" width="300" height="605">
    <img src="/img/niveau-baisse.svg" alt="Pour chaque domaine de PISA, variation du score moyen de 2015 à 2025 des {{< niv-val "n_ocde" >}} pays de l'OCDE, France en orange : compréhension de l'écrit −{{< niv-val "lect_v15" >}} points ({{< niv-val "lect_rang" >}}e plus forte baisse), culture mathématique −{{< niv-val "math_v15" >}} ({{< niv-val "math_rang" >}}e), culture scientifique −{{< niv-val "sci_v15" >}} ({{< niv-val "sci_rang" >}}e)." width="720" height="344" loading="lazy">
  </picture>
  <figcaption>Variation du score moyen PISA entre 2015 et 2025, pays membres de l'OCDE (OCDE, PISA 2025, volume&nbsp;I).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De 2015 à 2025, PISA mesure en France une baisse significative dans les trois domaines&nbsp;: {{< niv-val "lect_v15" >}}&nbsp;points de moins en compréhension de l'écrit, {{< niv-val "math_v15" >}} en mathématiques, {{< niv-val "sci_v15" >}} en sciences.

</div>

PISA, l'enquête de l'OCDE, interroge tous les trois ans des jeunes de 15 ans, quelle que soit leur classe, sur des compétences appliquées (comprendre un texte, résoudre un problème), dans une épreuve sans enjeu pour eux&nbsp;; ses résultats se lisent en points, sur une échelle propre construite autour de la moyenne des pays de l'OCDE. En France, {{< niv-val "lycee" >}}&nbsp;% de l'échantillon de 2025 était au lycée, dont {{< niv-val "seconde_gt" >}}&nbsp;% en seconde générale et technologique et {{< niv-val "seconde_pro" >}}&nbsp;% en seconde professionnelle&nbsp;: PISA parle bien de l'entrée au lycée.

Le score moyen de la France passe de {{< niv-val "lect_15" >}} à {{< niv-val "lect_25" >}} en compréhension de l'écrit, de {{< niv-val "math_15" >}} à {{< niv-val "math_25" >}} en culture mathématique, de {{< niv-val "sci_15" >}} à {{< niv-val "sci_25" >}} en culture scientifique&nbsp;; selon l'OCDE, les trois baisses sont statistiquement significatives. L'essentiel s'est produit depuis 2018&nbsp;: entre 2022 et 2025 encore, la lecture a perdu {{< niv-val "lect_v22" >}}&nbsp;points et les mathématiques {{< niv-val "math_v22" >}}, quand l'évolution des sciences n'est pas significative. Sur une période plus longue, la lecture a perdu {{< niv-val "lect_vlong" >}}&nbsp;points depuis {{< niv-val "lect_an0" >}} et les mathématiques {{< niv-val "math_vlong" >}} depuis {{< niv-val "math_an0" >}}, deux baisses significatives&nbsp;; en sciences, l'écart depuis {{< niv-val "sci_an0" >}} ({{< niv-val "sci_vlong" >}}&nbsp;points) ne l'est pas. L'OCDE ne signale pas l'échantillon français de 2025 comme hors normes.

<details class="repli">
<summary>Une condition de la mesure a aussi changé&nbsp;: l'effort déclaré par les élèves</summary>

À la fin de l'épreuve, les élèves notent de 1 à 10 l'effort qu'ils y ont mis&nbsp;: en France, l'indice est passé de {{< niv-val "eff_22" >}} à {{< niv-val "eff_25" >}} entre 2022 et 2025, la plus forte baisse des {{< niv-val "eff_n" >}} pays de l'OCDE, deux fois celle de la moyenne ({{< niv-val "eff_od" >}}). La répartition de l'effort déclaré a donc nettement changé. Mais si l'on repondère les élèves de 2025 pour leur donner la répartition des catégories d'effort déclarées en 2022, non-réponses comprises, plus des neuf dixièmes de la baisse des scores demeurent, en mathématiques comme en lecture. Ce calcul décrit un effet de composition&nbsp;; l'effort étant déclaré après l'épreuve, il ne permet pas d'en mesurer l'effet causal sur le score.

</details>

## La France baisse-t-elle plus que les autres&nbsp;? {#comparaison}

Le récit courant, «&nbsp;tout le monde baisse&nbsp;», est juste en moyenne&nbsp;: la moyenne de l'OCDE perd {{< niv-val "lect_ocde_v15" >}}&nbsp;points en lecture, {{< niv-val "math_ocde_v15" >}} en mathématiques et {{< niv-val "sci_ocde_v15" >}} en sciences de 2015 à 2025. La France perd davantage de points dans les trois domaines, sur les estimations ponctuelles. Reste à savoir où elle se place parmi les pays pris un à un.

Pour le vérifier, on peut placer la baisse française parmi celles des {{< niv-val "n_ocde" >}} pays membres de l'OCDE, sans s'arrêter au rang du score, qui dépend des autres pays. En **sciences**, la France ({{< niv-val "sci_v15" >}}&nbsp;points de moins) est dans la moitié centrale des pays. En **lecture**, avec {{< niv-val "lect_v15" >}}&nbsp;points de moins, elle est pratiquement à la frontière entre la moitié centrale et le quart des pays aux plus fortes baisses, une frontière qui ne départage rien. En **mathématiques**, la France sort de la moyenne&nbsp;: {{< niv-val "math_v15" >}}&nbsp;points de moins, quand la moitié des pays en perdent moins de {{< niv-val "math_med" >}}. Sur les estimations ponctuelles, sa baisse dépasse celle de {{< niv-val "math_mieux" >}} des {{< niv-val "n_autres" >}} autres pays, et sa place est la même parmi les seuls pays de l'Union européenne membres de l'OCDE ou sans les {{< niv-val "n_etoile" >}} pays dont l'échantillon ne respecte pas toutes les normes de l'enquête. Ce rang reste descriptif&nbsp;: l'écart entre la France et le quart des pays aux plus fortes baisses ({{< niv-val "math_ecart_q1" >}}&nbsp;points) est du même ordre que la marge d'erreur de la variation française (erreur type de {{< niv-val "math_se" >}}&nbsp;points).

L'OCDE ne publie pas de test de l'écart entre la baisse française et celle des autres pays&nbsp;: le classement des baisses est un calcul de l'auteur sur ses tableaux. Reste à savoir si les évaluations passées en classe, en France, voient la même chose.

## Toutes les évaluations montrent-elles la même baisse&nbsp;? {#evaluations}

PISA n'est pas seule à suivre les élèves français. Trois autres évaluations le font, chacune avec ses élèves, sa compétence et sa période&nbsp;:

- **PISA** (OCDE)&nbsp;: les jeunes de 15 ans, toutes classes confondues&nbsp;; des compétences appliquées, dans une épreuve sans enjeu&nbsp;; dernière période comparée, 2022-2025.
- **PIRLS** (IEA, association internationale de chercheurs en éducation)&nbsp;: les élèves de CM1&nbsp;; la compréhension de l'écrit&nbsp;; 2016-2021.
- **TIMSS** (IEA)&nbsp;: les élèves de CM1 et de quatrième&nbsp;; les mathématiques et les sciences, proches des programmes&nbsp;; 2019-2023.
- **Test de positionnement** (DEPP, service statistique du ministère de l'Éducation nationale)&nbsp;: tous les élèves entrant en seconde&nbsp;; le français et les mathématiques, sans test de significativité publié&nbsp;; 2021-2024.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/niveau-thermometres-m.svg" width="300" height="771">
    <img src="/img/niveau-thermometres.svg" alt="Tableau de la dernière variation de chaque évaluation en France, dans sa propre échelle : PIRLS CM1, compréhension de l'écrit, 2016-2021, de {{< niv-val "pirls_16" >}} à {{< niv-val "pirls_21" >}}, non significative ; TIMSS CM1, mathématiques, 2019-2023, de {{< niv-val "tcm1_19" >}} à {{< niv-val "tcm1_23" >}}, non significative ; TIMSS quatrième, mathématiques, 2019-2023, de {{< niv-val "t4e_19" >}} à {{< niv-val "t4e_23" >}}, non significative ; test de positionnement de seconde GT, mathématiques, 2021-2024, de {{< niv-val "sm_21" >}} à {{< niv-val "sm_24" >}}, hausse observée, sans test publié ; français, de {{< niv-val "sf_21" >}} à {{< niv-val "sf_24" >}}, baisse observée, sans test publié ; PISA, 15 ans, 2022-2025, mathématiques −{{< niv-val "math_v22" >}} et compréhension de l'écrit −{{< niv-val "lect_v22" >}}, baisses significatives." width="720" height="360" loading="lazy">
  </picture>
  <figcaption>Dernière variation publiée de chaque évaluation en France, chacune dans sa propre échelle (IEA, DEPP, OCDE).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** Sur leurs derniers intervalles, qui ne sont pas les mêmes, la baisse significative est établie pour PISA&nbsp;; PIRLS en CM1 et TIMSS en CM1 et en quatrième ne la mettent pas en évidence, et le score du test d'entrée en seconde monte en mathématiques, sans test publié.

</div>

PIRLS en CM1 passe de {{< niv-val "pirls_16" >}} points en 2016 à {{< niv-val "pirls_21" >}} en 2021, TIMSS en CM1 de {{< niv-val "tcm1_19" >}} en 2019 à {{< niv-val "tcm1_23" >}} en 2023, TIMSS en quatrième de {{< niv-val "t4e_19" >}} à {{< niv-val "t4e_23" >}} en mathématiques&nbsp;: aucune de ces variations n'est significative, pas plus que celles des sciences de TIMSS. Le score du test de seconde, passé par tous les élèves, monte en mathématiques. PISA, lui, perd {{< niv-val "math_v22" >}}&nbsp;points en mathématiques et {{< niv-val "lect_v22" >}} en lecture entre 2022 et 2025, deux baisses significatives.

Ces résultats ne se contredisent pas pour autant. Une baisse significative d'un côté et une variation non significative de l'autre ne prouvent pas que les tendances diffèrent&nbsp;: il faudrait comparer directement les deux variations, avec leurs incertitudes, ce qu'aucun producteur ne publie. Et les périodes ne sont pas les mêmes (PIRLS s'arrête en 2021, TIMSS en 2023, PISA en 2025), ni les élèves&nbsp;; chaque évaluation a son échelle, et les points bruts de ces échelles ne se comparent pas directement&nbsp;: les comparer demande une conversion explicite, comme celle que fait la DEPP plus bas pour le test de seconde et PISA. Elles ne réfutent donc pas PISA&nbsp;; elles interdisent de dire que toutes les mesures montrent la même chute récente. Sur la longue période, en revanche, les évaluations par classe baissent elles aussi&nbsp;: en mathématiques, TIMSS en quatrième était à {{< niv-val "t4e_95" >}} points en 1995, et PIRLS à {{< niv-val "pirls_01" >}} en 2001, deux niveaux significativement au-dessus des derniers résultats. Pour la langue seule, avec la dictée de CM2 depuis 1987 et la lecture pour le plaisir, la frise de la page voisine montre la même divergence et des reculs plus anciens&nbsp;: [la langue des élèves recule-t-elle d'un bloc&nbsp;?](/les-eleves-maitrisent-ils-moins-bien-la-langue-francaise/#chronologie).

<details class="repli">
<summary>Le même décalage entre TIMSS et PISA dans les autres pays&nbsp;? Une comparaison descriptive de {{< niv-val "t3_n" >}} pays</summary>

Une comparaison descriptive des {{< niv-val "t3_n" >}} pays présents dans les deux enquêtes rapproche l'évolution de TIMSS en quatrième entre 2019 et 2023 de celle de PISA à 15 ans entre 2022 et 2025&nbsp;: les périodes et les populations ne sont donc pas identiques, et ce ne sont pas les mêmes élèves qui sont suivis. En France, TIMSS recule de {{< niv-val "t3_fr_dt" >}}&nbsp;points, sans variation significative, tandis que PISA perd {{< niv-val "t3_fr_dp" >}}&nbsp;points en mathématiques. Selon la règle fixée avant le calcul, la France figure parmi les {{< niv-val "t3_rang_l" >}} écarts sur {{< niv-val "t3_n" >}} les plus défavorables à PISA, et elle reste parmi les écarts les plus défavorables dans un ajustement descriptif tenant compte du score TIMSS initial. Mais les évolutions des deux enquêtes sont peu liées d'un pays à l'autre&nbsp;: dans {{< niv-val "t3_autre" >}} pays sur {{< niv-val "t3_n" >}}, PISA évolue au contraire plus favorablement que TIMSS. Ce classement reste descriptif, et le même test n'est pas concluant en sciences.

</details>

Un rapprochement va plus loin. La DEPP a confronté PISA au test d'entrée en seconde pour des cohortes largement correspondantes.

## Que disent les tests d'entrée en seconde&nbsp;? {#seconde}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/niveau-seconde-m.svg" width="300" height="601">
    <img src="/img/niveau-seconde.svg" alt="Barres horizontales, écart standardisé entre les cohortes de 2021-2022 et celles de 2024-2025, calculé par la DEPP. Français : test de seconde −{{< niv-val "g_tf" >}}, PISA compréhension de l'écrit −{{< niv-val "g_pf" >}}. Mathématiques : test de seconde +{{< niv-val "g_tm" >}}, PISA culture mathématique −{{< niv-val "g_pm" >}}." width="720" height="302" loading="lazy">
  </picture>
  <figcaption>Écart entre deux cohortes d'élèves, en centièmes d'écart-type, test de positionnement de seconde et PISA (DEPP, Note d'Information 26-40).</figcaption>
</figure>

Depuis 2018, tous les élèves de seconde passent en septembre un test de positionnement en français et en mathématiques, sur une échelle fixée en 2019. Il se rapproche de PISA pour des cohortes largement correspondantes&nbsp;: les jeunes évalués par PISA en 2022 sont, pour la plupart, entrés en seconde en 2021&nbsp;; ceux de 2025, en 2024. Ce ne sont pas les mêmes élèves suivis d'une épreuve à l'autre&nbsp;: la DEPP compare deux générations. En **français**, les deux baissent&nbsp;: en seconde générale et technologique, le score moyen passe de {{< niv-val "sf_21" >}} en 2021 à {{< niv-val "sf_24" >}} en 2024, et PISA perd {{< niv-val "lect_v22" >}}&nbsp;points en lecture. En **mathématiques**, ils divergent&nbsp;: le score du test de seconde passe de {{< niv-val "sm_21" >}} à {{< niv-val "sm_24" >}}, quand PISA perd {{< niv-val "math_v22" >}}&nbsp;points. Ramenés à une même unité, la DEPP trouve +{{< niv-val "g_tm" >}} pour le test de seconde et −{{< niv-val "g_pm" >}} pour PISA en mathématiques, et écrit que la baisse de PISA «&nbsp;contraste avec la légère hausse constatée par le test de positionnement en début de seconde entre les rentrées 2021 et 2024&nbsp;».

Ce désaccord ne signifie pas qu'une évaluation se trompe. Les deux épreuves ne mesurent ni exactement les mêmes compétences, ni la même population (un âge pour PISA, une classe pour le test de seconde), ni dans le même contexte&nbsp;: PISA n'a aucun enjeu pour l'élève, le test de seconde sert à son professeur. La DEPP ne l'explique pas. Plus récemment, elle note une baisse en français en 2025 (score de {{< niv-val "sf_25" >}} en seconde générale et technologique, retour au niveau de 2019) et, en mathématiques, un score sans changement notable&nbsp;; elle ne publie pas de test de significativité pour ce test, passé par tous les élèves.

Si les mesures divergent sur l'ampleur du recul, PISA permet au moins de voir quels élèves reculent.

## Qui décroche&nbsp;: les plus faibles ou les meilleurs&nbsp;? {#qui-decroche}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/niveau-sommet-m.svg" width="300" height="796">
    <img src="/img/niveau-sommet.svg" alt="Barres, en % des élèves de 15 ans, 2015 puis 2025. Lecture, sous le niveau 2 : France {{< niv-val "lect_bas15" >}} puis {{< niv-val "lect_bas25" >}}, OCDE {{< niv-val "lect_obas15" >}} puis {{< niv-val "lect_obas25" >}} ; niveaux 5-6 : France {{< niv-val "lect_haut15" >}} puis {{< niv-val "lect_haut25" >}}, OCDE {{< niv-val "lect_ohaut15" >}} puis {{< niv-val "lect_ohaut25" >}}. Mathématiques, sous le niveau 2 : France {{< niv-val "math_bas15" >}} puis {{< niv-val "math_bas25" >}} ; niveaux 5-6 : France {{< niv-val "math_haut15" >}} puis {{< niv-val "math_haut25" >}}." width="720" height="352" loading="lazy">
  </picture>
  <figcaption>Part des élèves de 15 ans sous le niveau 2 et aux niveaux 5 et 6, France et moyenne de l'OCDE, 2015 et 2025 (OCDE, PISA 2025).</figcaption>
</figure>

Les deux, et c'est ce qui distingue la France. Dans la moyenne de l'OCDE, la baisse de 2015 à 2025 s'atténue quand on remonte la distribution&nbsp;: en mathématiques, le score sous lequel se trouvent les 10&nbsp;% d'élèves les plus faibles recule de {{< niv-val "math_op10" >}}&nbsp;points, le score médian de {{< niv-val "math_op50" >}}, celui au-dessus duquel se trouvent les 10&nbsp;% les plus forts de {{< niv-val "math_op90" >}}. En France, cet amortissement disparaît&nbsp;: {{< niv-val "math_p10" >}}, {{< niv-val "math_p50" >}} et {{< niv-val "math_p90" >}}&nbsp;points. En lecture, le milieu et le haut reculent même bien davantage que le bas ({{< niv-val "lect_p50" >}} et {{< niv-val "lect_p90" >}}, contre {{< niv-val "lect_p10" >}}). Ce sont des positions dans des échantillons successifs, pas les mêmes élèves suivis pendant dix ans.

Les seuils de PISA le disent aussi, et ils mesurent autre chose&nbsp;: non plus une position dans la distribution, mais un niveau de compétence fixé une fois pour toutes. La part des élèves sous le niveau&nbsp;2, celui où l'OCDE situe la maîtrise de base, passe de {{< niv-val "lect_bas15" >}}&nbsp;% à {{< niv-val "lect_bas25" >}}&nbsp;% en lecture et de {{< niv-val "math_bas15" >}}&nbsp;% à {{< niv-val "math_bas25" >}}&nbsp;% en mathématiques, à peu près comme dans l'OCDE. La part des meilleurs élèves, aux niveaux 5 et 6, a été presque divisée par trois en lecture, de {{< niv-val "lect_haut15" >}}&nbsp;% à {{< niv-val "lect_haut25" >}}&nbsp;%, et plus que divisée par deux en mathématiques, de {{< niv-val "math_haut15" >}}&nbsp;% à {{< niv-val "math_haut25" >}}&nbsp;%&nbsp;; dans la moyenne de l'OCDE, la perte au sommet est bien plus faible (de {{< niv-val "lect_ohaut15" >}}&nbsp;% à {{< niv-val "lect_ohaut25" >}}&nbsp;% en lecture, de {{< niv-val "math_ohaut15" >}}&nbsp;% à {{< niv-val "math_ohaut25" >}}&nbsp;% en mathématiques).

Les meilleurs scores ne sont pas la même chose que les élèves les plus favorisés, et les deux reculent. Le sommet et le milieu de la distribution reculent dans tous les milieux sociaux&nbsp;: le 90<sup>e</sup>&nbsp;percentile, score au-dessus duquel se trouvent les 10&nbsp;% d'élèves les plus forts, baisse dans chacun des quatre quarts de statut social, de {{< niv-val "p5_lect_q_min" >}} à {{< niv-val "p5_lect_q_max" >}}&nbsp;points en lecture et de {{< niv-val "p5_math_q_min" >}} à {{< niv-val "p5_math_q_max" >}} en mathématiques, à peu près autant chez les favorisés que chez les défavorisés&nbsp;; le score médian baisse lui aussi dans chaque quart, de {{< niv-val "p6_lect_med_min" >}} à {{< niv-val "p6_lect_med_max" >}}&nbsp;points en lecture et de {{< niv-val "p6_math_med_min" >}} à {{< niv-val "p6_math_med_max" >}} en mathématiques. Ces reculs se retrouvent quand les quarts sont formés avec la profession des parents.

L'écart entre milieux sociaux, lui, ne se lit pas aussi simplement. Avec l'indice social de l'OCDE, il passerait de {{< niv-val "lect_ec15" >}} à {{< niv-val "lect_ec25" >}}&nbsp;points en lecture entre 2015 et 2025&nbsp;; mais l'OCDE a modifié en 2025 les questions sur la famille dont cet indice est tiré, et ne le traite plus comme comparable d'une enquête à l'autre&nbsp;: on n'en tire aucune tendance. Avec la profession des parents, codée sur la même échelle internationale en 2015 et en 2025, l'écart se réduit en lecture (de {{< niv-val "p7_lect_i1_15" >}} à {{< niv-val "p7_lect_i1_25" >}}&nbsp;points), mais la réduction n'est significative ni en mathématiques ni en sciences, y compris en ajoutant le diplôme des parents à la mesure.

Une question demeure&nbsp;: la baisse tient-elle à la façon dont les jeunes de 15 ans se répartissent entre les classes&nbsp;?

## Le changement de répartition entre classes explique-t-il la baisse&nbsp;? {#composition}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/niveau-composition-m.svg" width="300" height="650">
    <img src="/img/niveau-composition.svg" alt="Baisse du score moyen PISA de 2015 à 2025, observée, à la répartition entre classes de 2015, puis à la composition de 2015 pour la classe, le sexe et la famille : mathématiques {{< niv-val "p5_math_obs" >}}, {{< niv-val "p5_math_rec" >}} et {{< niv-val "p6_math_rec" >}} points, compréhension de l'écrit {{< niv-val "p5_lect_obs" >}}, {{< niv-val "p5_lect_rec" >}} et {{< niv-val "p6_lect_rec" >}}, culture scientifique {{< niv-val "p5_sci_obs" >}}, {{< niv-val "p5_sci_rec" >}} et {{< niv-val "p6_sci_rec" >}}." width="720" height="288" loading="lazy">
  </picture>
  <figcaption>Baisse du score moyen, observée, à la répartition entre classes de 2015 et à la composition de 2015, trois domaines (OCDE, bases PISA 2015 et 2025, données individuelles&nbsp;; calcul de l'auteur).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** En mathématiques, la baisse vaut {{< niv-val "p5_math_obs" >}}&nbsp;points telle qu'observée, {{< niv-val "p5_math_rec" >}} à la répartition entre classes de 2015, {{< niv-val "p6_math_rec" >}} à la composition de 2015 pour la classe, le sexe et la famille&nbsp;: trois réponses à trois questions différentes, dont aucune n'est «&nbsp;la vraie baisse&nbsp;».

</div>

Non&nbsp;: le changement de répartition entre classes ne suffit pas à expliquer la baisse. À la répartition entre classes de 2015, la baisse calculée est même plus forte, dans les trois domaines&nbsp;; ajustée aussi du sexe et de la famille, elle revient près de la baisse observée. PISA retient un âge, non une classe. Entre 2015 et 2025, en même temps que reculait le redoublement, la part des jeunes de 15 ans encore en troisième ou avant est passée de près d'un quart à moins d'un dixième de l'échantillon français ({{< niv-val "comp_retard15" >}}&nbsp;% puis {{< niv-val "comp_retard25" >}}&nbsp;%), et celle de la seconde professionnelle et du CAP de {{< niv-val "comp_pro15" >}}&nbsp;% à {{< niv-val "comp_pro25" >}}&nbsp;%. Or les élèves encore au collège à 15 ans ont des scores bien plus bas. Quand un groupe aux scores bas devient plus petit, la moyenne de l'ensemble monte, même si aucun élève ne progresse.

La standardisation pose donc une question précise&nbsp;: que vaudrait la moyenne de 2025 avec les scores de chaque classe en 2025, mais la répartition entre classes de 2015&nbsp;? Les données individuelles de PISA, qui donnent pour chaque élève sa classe et son programme, y répondent, calculées selon la méthode de l'OCDE et contrôlées en retrouvant au centième les moyennes qu'elle publie&nbsp;: la baisse passe de {{< niv-val "p5_math_obs" >}} à {{< niv-val "p5_math_rec" >}}&nbsp;points en mathématiques, de {{< niv-val "p5_lect_obs" >}} à {{< niv-val "p5_lect_rec" >}} en lecture, et de {{< niv-val "p5_sci_obs" >}} à {{< niv-val "p5_sci_rec" >}} en sciences. Le changement de répartition entre classes atténue donc arithmétiquement la baisse observée. Ce n'est pas «&nbsp;la vraie baisse&nbsp;»&nbsp;: c'est la baisse à une autre répartition, et ce chiffre ne mesure pas l'effet du redoublement, dont le recul a aussi changé qui se trouve dans chaque classe. En mathématiques et en lecture, le score moyen est plus bas en 2025 dans chacune des quatre catégories de classe observées&nbsp;; en sciences, trois catégories sur quatre reculent, et la petite catégorie «&nbsp;première et après&nbsp;», environ {{< niv-val "comp_prem25" >}}&nbsp;% des élèves, ne baisse pas. Parmi les élèves classés en seconde générale et technologique chaque année, le score moyen passe de {{< niv-val "p5_math_gt15" >}} à {{< niv-val "p5_math_gt25" >}} en mathématiques ({{< niv-val "p5_math_gtd" >}}&nbsp;points de moins) et de {{< niv-val "p5_lect_gt15" >}} à {{< niv-val "p5_lect_gt25" >}} en lecture ({{< niv-val "p5_lect_gtd" >}} de moins)&nbsp;; ces populations ne sont pas identiques, puisque des élèves qui auraient auparavant été encore au collège peuvent désormais être en seconde. La DEPP avait relevé le même effet de structure entre 2006 et 2015, et ses chiffres de 2015 et 2025 en sciences, publiés par classe, donnent le même résultat que les données individuelles.

D'autres caractéristiques ont changé en même temps. Si l'on applique à 2025 la répartition de 2015 à la fois pour la classe, le sexe, le diplôme des parents et l'origine migratoire, la baisse est de {{< niv-val "p6_math_rec" >}}&nbsp;points en mathématiques, {{< niv-val "p6_lect_rec" >}} en lecture et {{< niv-val "p6_sci_rec" >}} en sciences&nbsp;: elle revient à peu près au niveau observé. Trois nombres répondent ainsi à trois questions, en mathématiques&nbsp;: la baisse observée ({{< niv-val "p5_math_obs" >}}&nbsp;points), la baisse à la répartition entre classes de 2015 ({{< niv-val "p5_math_rec" >}}), la baisse à la composition de 2015 pour l'ensemble de ces caractéristiques ({{< niv-val "p6_math_rec" >}}). Aucun ne dit la contribution de chacune. Deux réserves comptent, au contact de ces chiffres. Le calcul ne reconstitue pas les parcours scolaires. Et les questions sur la famille restent bien plus souvent sans réponse en 2025&nbsp;: le diplôme des parents manque pour {{< niv-val "p6_dipl_nr25" >}}&nbsp;% des élèves, contre {{< niv-val "p6_dipl_nr15" >}}&nbsp;% en 2015, l'origine pour {{< niv-val "p6_orig_nr25" >}}&nbsp;%, contre {{< niv-val "p6_orig_nr15" >}}&nbsp;%. Ces élèves forment une catégorie à part dans la repondération, ce qui ne supprime pas les biais éventuels de la non-réponse&nbsp;; calculée sur les seuls élèves dont la famille est renseignée, la repondération ne réduit pas non plus la baisse.

## Et à la fin du lycée&nbsp;? {#fin-du-lycee}

La seule mesure internationale date, et elle porte sur une filière qui n'existe plus. TIMSS Advanced, l'enquête de l'IEA sur les élèves scientifiques en fin d'études secondaires, a évalué la terminale S en 1995 et en 2015&nbsp;: le score moyen de la France est passé de {{< niv-val "timss_math_95" >}} à {{< niv-val "timss_math_15" >}} en mathématiques ({{< niv-val "timss_math_v" >}}&nbsp;points de moins) et de {{< niv-val "timss_phys_95" >}} à {{< niv-val "timss_phys_15" >}} en physique ({{< niv-val "timss_phys_v" >}}&nbsp;points de moins), deux baisses significatives. L'enquête n'a pas été refaite depuis, et la série S a disparu avec la réforme du lycée&nbsp;: rien ne mesure aujourd'hui, dans le temps, le niveau des terminales.

La journée défense et citoyenneté évalue chaque année la lecture des jeunes d'environ 17 ans. Son test a changé en 2019, et la DEPP indique que les résultats de 2024 ne se comparent pas à ceux des années précédentes&nbsp;: elle ne permet pas de suivre une tendance.

## Ce que ces données ne disent pas {#limites}

- **Pourquoi PISA baisse**&nbsp;: ni les moyens, ni les professeurs, ni les écrans, ni la pandémie, ni l'effort mis dans l'épreuve ne peuvent être départagés avec ces séries. Elles mesurent un recul, pas sa cause.
- **Pourquoi les évaluations divergent**&nbsp;: âge contre classe, compétences appliquées contre programme, enjeu ou non pour l'élève, années différentes&nbsp;; aucune de ces explications n'est testée ici. D'un pays à l'autre, aucune relation suffisamment nette n'apparaît entre l'écart TIMSS / PISA et le niveau initial, la couverture des jeunes de 15 ans, leur répartition entre classes ou l'évolution de l'effort déclaré&nbsp;; ces résultats descriptifs ne permettent pas d'écarter ces facteurs comme explications.
- **La composition et la mesure du milieu social**&nbsp;: la repondération tient compte de la classe, du sexe, du diplôme des parents et de l'origine migratoire, sans reconstituer les parcours scolaires ni ce que l'enquête ne mesure pas&nbsp;; les questions sur la famille sont plus souvent restées sans réponse en 2025 et ont été reformulées, et l'indice social de l'OCDE ne se compare plus d'une enquête à l'autre, ce qui limite toute comparaison des milieux sociaux dans le temps.
- <span id="recrutement"></span>**Le recrutement des professeurs**&nbsp;: aucune donnée publique ne rapproche un enseignant des résultats de ses élèves, ni ne mesure le niveau de formation des recrutés. Au CAPES externe, le nombre de candidats présents par admis a diminué de {{< niv-val "p1_min" >}}&nbsp;% à {{< niv-val "p1_max" >}}&nbsp;% entre les sessions 2010-2012 et 2023-2025, selon la discipline&nbsp;: ce ratio mesure la concurrence au concours, pas le niveau des recrutés. Les concours, les classes et les heures de cours perdues sont traités dans la page [Manque-t-il des professeurs au lycée&nbsp;?](/manque-t-il-des-professeurs/).
- **Le niveau à la sortie du lycée aujourd'hui**&nbsp;: la dernière mesure internationale date de 2015, et la journée défense et citoyenneté ne se compare pas dans le temps.
- **Le baccalauréat**&nbsp;: un taux de réussite à un examen dont les règles changent ne mesure pas un niveau.

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

On demande souvent si le niveau baisse comme si une seule mesure pouvait répondre. Les évaluations françaises disent trois choses distinctes. PISA, à 15 ans, mesure une baisse significative depuis 2015, en mathématiques parmi le quart des plus fortes de l'OCDE sur les estimations ponctuelles&nbsp;; sur leurs derniers intervalles, différents, les évaluations passées en classe ne la mettent pas en évidence, ce qui ne prouve pas des tendances différentes, et sur la longue période elles baissent aussi. En France, le milieu et le sommet de la distribution reculent presque autant que le bas, ou davantage, quand la moyenne de l'OCDE amortit la baisse vers le haut. Et la répartition des jeunes de 15 ans entre les classes, plus avancée qu'en 2015, atténue arithmétiquement la baisse observée&nbsp;; à composition de 2015 pour la classe, le sexe et la famille, la baisse revient à peu près au niveau observé. Aucune de ces mesures ne dit pourquoi le niveau baisse&nbsp;: la divergence entre évaluations est une information à expliquer, pas une explication.

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

{{< appel-livre slug="la-societe-du-premier-coup" sur="Après un premier échec, qui peut recommencer ?" avis="non" offert="avant" >}}
Cette page mesure ce que savent les élèves à un moment donné. La question qui vient ensuite est celle des parcours&nbsp;: quand un élève échoue une première fois, à un examen, une orientation, une première année d'études, qui peut réellement recommencer, et à quel coût selon son milieu&nbsp;? Le livre montre que cette possibilité de recommencer n'est pas également distribuée.
{{< /appel-livre >}}


## D'où viennent ces chiffres {#sources}

**PISA.** OCDE, *PISA 2025 Results*, volume&nbsp;I (8&nbsp;septembre 2026), tableaux de l'annexe&nbsp;B1&nbsp;: scores moyens et variations (I.B1.2a.36 à 38), niveaux de compétence (I.B1.2a.33 à 35), percentiles (I.B1.2a.39 à 41), statut économique, social et culturel (I.B1.2b.22 à 24). Une variation est dite significative quand elle dépasse 1,96 fois son erreur type, règle de l'OCDE. La moyenne de l'OCDE est celle des 35 pays comparables sur toute la période. Témoin&nbsp;: les séries de la France publiées par la DEPP (Notes d'Information 26-39 et 26-40), identiques à 0,04&nbsp;point près. Classes des élèves de l'échantillon&nbsp;: Note 26-40, figure&nbsp;1. Effort déclaré&nbsp;: Note 26-40, figures 31 à 34 web.

**Composition par classe.** DEPP, Note d'Information 16-37 (PISA 2015, culture scientifique, figure&nbsp;3) et Note 26-39 (PISA 2025, figure 10 web)&nbsp;: part de l'échantillon et score par classe. Classes regroupées en quatre catégories (troisième et avant, seconde générale et technologique, seconde professionnelle et CAP, première)&nbsp;; la figure de 2015 n'a pas de ligne CAP&nbsp;; champs un peu différents (2015 sans La Réunion, 2025 sans Mayotte). Deux variantes de regroupement (sans la première&nbsp;; «&nbsp;autres&nbsp;» comptés avec la troisième) donnent le même sens et un effet un peu plus fort. Score de 2025 recalculé avec les parts de 2015&nbsp;; contrôle&nbsp;: les catégories doivent redonner le score moyen publié à moins de 3&nbsp;points près, seuil fixé avant le calcul, ce qu'elles font les deux années.

**Données individuelles.** OCDE, bases PISA 2015, 2022 et 2025 (fichiers élèves publics)&nbsp;: calculs avec les dix valeurs plausibles et les 80&nbsp;poids répliqués, selon la méthode de l'OCDE&nbsp;; témoin&nbsp;: les moyennes de la France publiées par l'OCDE, retrouvées au centième pour les trois domaines et les trois années. Répartition par classe à partir de la classe et du programme national de chaque élève, contrôlée contre la répartition publiée par la DEPP pour 2015. Quarts sociaux&nbsp;: quarts nationaux de l'indice de statut économique, social et culturel. Effort&nbsp;: note de 1 à 10 déclarée à la fin de l'épreuve, en quatre groupes et la non-réponse. Composition conjointe&nbsp;: repondération des élèves de 2025 par une régression logistique pondérée sur la classe, le sexe, le diplôme le plus élevé des parents (trois groupes harmonisés entre les deux cycles) et l'origine migratoire, en effets principaux, chaque réponse manquante formant une catégorie&nbsp;; avec la classe seule, elle redonne au centième la repondération par classe, et les répartitions de 2015 sont retrouvées à moins d'un demi-point, à moins d'un point pour les croisements de la classe, du diplôme et de l'origine&nbsp;; variantes (classe croisée avec le diplôme, diplôme en deux groupes, profession des parents ajoutée ou à la place du diplôme, poids plafonnés, élèves à la famille renseignée)&nbsp;: dans aucune, la baisse ne diminue de plus d'un point. Quarts sociaux comparables dans le temps&nbsp;: «&nbsp;contrairement aux cycles précédents, l'indice calculé pour PISA 2025 n'est pas traité comme une échelle de tendance&nbsp;», en raison des changements apportés aux questions sur le diplôme, la profession et les biens du foyer (OCDE, rapport technique de PISA 2025, chapitre 22, version provisoire de septembre 2026, notre traduction)&nbsp;; les conséquences en sont étudiées par Cobreros, Colomer, Correig-Fraga, Gortazar et Sayol (document de travail, septembre 2026). Les quarts sont refaits dans chaque année avec l'indice de profession des parents (même classification internationale des professions les deux années, questions reformulées en 2025), seul ou avec leur diplôme, et l'écart entre quarts de la France est recalculé (le même calcul sur l'indice de l'OCDE redonne ses chiffres publiés). Médiane par quart social&nbsp;: bornes des quarts fixées par le poids final, erreur type par les poids répliqués et les dix valeurs plausibles. Les comparaisons 2015-2025 n'intègrent pas l'erreur de liaison entre cycles.

**Autres évaluations.** IEA, *TIMSS 2023 International Results* (tableaux de tendance, CM1 et quatrième, mathématiques et sciences, avec la significativité de chaque écart)&nbsp;; DEPP, Notes d'Information 24-47, 24-48 et 24-49 (TIMSS 2023), 23-21 (PIRLS 2021) et 17-24 (PIRLS 2016). Comparaison par pays&nbsp;: variation de TIMSS en quatrième (2019-2023, tableau de tendance de l'IEA) et de PISA (2022-2025, tableau I.B1.2a.38) pour les pays présents dans les deux, entités infranationales et pays évalués en neuvième année écartés&nbsp;; écart mesuré par la différence des variations ramenées à l'écart-type entre pays (un indice de rang, non une grandeur), avec trois variantes (membres de l'OCDE seulement, sans les pays signalés par l'OCDE, écart en points) qui donnent le même résultat. Protocole écrit avant le calcul, scores de TIMSS relus dans le PDF de l'IEA. Le quatrième protocole a contrôlé le niveau de départ (régression de l'écart sur le score TIMSS de 2019, et écart de rang au lieu de l'écart standardisé)&nbsp;; il a aussi testé, sans trouver de relation lisible, l'indice de couverture des 15 ans (tableau I.A2.1 de l'OCDE), la répartition par classe (I.A2.3) et l'effort déclaré (Note 26-40, figure 31 web, 15 membres de l'OCDE).

**Tests de positionnement de seconde.** DEPP, Note d'Information 26-22 et ses données (scores moyens 2019-2025, échelle fixée à 250 en 2019, voies générale et technologique et professionnelle), document de travail 2025-E15. Rapprochement avec PISA&nbsp;: Note 26-40, figure 11 web (deux voies ensemble). La DEPP précise que la comparaison stricte des mathématiques entre 2024 et 2025 n'est pas possible, une partie du test ayant été renouvelée.

**Fin du lycée.** IEA, *TIMSS Advanced 2015 International Results in Advanced Mathematics and Physics*&nbsp;; DEPP, Notes d'Information 16-34 et 16-35. Journée défense et citoyenneté&nbsp;: DEPP, Note d'Information 25-57 et notes antérieures.

**Recrutement.** DEPP, *Repères et références statistiques* 2011 à 2013 et 2024 à 2026 (concours de recrutement du second degré public selon les disciplines&nbsp;; troisième concours compté avec l'externe&nbsp;; Capes à affectation locale compris à partir de 2021), Note d'Information 11-24 pour la session 2010&nbsp;; la session 2012 de physique-chimie n'est pas publiée par la DEPP. Contractuels&nbsp;: RERS 2026, fiche 9.02. Enseignants non pleinement qualifiés&nbsp;: OCDE, *Regards sur l'éducation* 2026, chapitre sur la pénurie d'enseignants, tableau&nbsp;1 (France&nbsp;: année 2023-2024).

Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent d'un calcul de l'auteur, dont l'extrait est archivé avec ses empreintes&nbsp;; le script qui écrit la page vérifie chaque affirmation chiffrée et s'arrête si elle n'est plus vraie. Sept protocoles ont été écrits chacun avant son calcul, avec leurs seuils&nbsp;; le deuxième, qui a fait entrer TIMSS, PIRLS et la composition par classe, répondait à une contre-expertise externe de la première version. Les scores PISA de la France, les résultats des tests de seconde, des concours, de PIRLS et la composition par classe de 2015 ont été lus deux fois, par deux extracteurs indépendants, et les séries de la France ont été comparées entre l'OCDE et la DEPP&nbsp;; chacun de ces contrôles a détecté les erreurs qu'on y avait introduites volontairement.

{{< reutiliser figures="figures_niveau" jeu="niveau_eleves" sources="OCDE (PISA, Regards sur l'éducation), IEA (TIMSS, PIRLS), DEPP" donnees="Scores PISA de la France et de l'OCDE, variation 2015-2025 des 38 pays de l'OCDE, percentiles, élèves en difficulté et meilleurs élèves, écart social, composition par classe dans les trois domaines, effort déclaré, TIMSS CM1 et quatrième, PIRLS CM1, test de positionnement de seconde 2019-2025, écarts entre générations de la DEPP, TIMSS Advanced, candidats et admis au CAPES externe, contractuels, enseignants non pleinement qualifiés ; le même contenu existe en CSV, au format long." >}}
PISA, à 15 ans, mesure en France une baisse significative de 2015 à 2025 ({{< niv-val "lect_v15" >}}&nbsp;points en compréhension de l'écrit, {{< niv-val "math_v15" >}} en mathématiques), que les évaluations passées en classe ne mettent pas en évidence sur leurs derniers intervalles, différents, sans que cela prouve des tendances différentes. À la répartition entre classes de 2015, la baisse de PISA est plus forte dans les trois domaines, et elle revient à peu près au niveau observé quand on tient compte aussi du sexe et de la famille&nbsp;: ces calculs décrivent, ils n'attribuent pas de cause. En France, le milieu et le haut de la distribution reculent presque autant que le bas, ou davantage, quand dans la moyenne de l'OCDE la baisse s'atténue vers le haut.
{{< /reutiliser >}}
