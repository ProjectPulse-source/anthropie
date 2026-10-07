---
title: "Manque-t-il des professeurs au lycée ?"
description: "Concours, taille des classes, cours non assurés, dépense : ce que les séries officielles disent du « manque de professeurs » au lycée. Une heure de cours sur {lyc.h_un_sur_l} n'a pas lieu au lycée général et technologique ; les concours de mathématiques et de physique-chimie restent sous quatre postes pourvus sur cinq. Données DEPP, OCDE, recalculées."
chapo: "En partie, et pas seulement là où on le dit. Les concours de mathématiques et de physique-chimie restent sous quatre postes pourvus sur cinq depuis trois sessions, alors que l'ensemble des concours se redresse. Les classes du lycée général et technologique comptent plus de 30 élèves en moyenne depuis 2020, mais les divisions de 35 élèves et plus sont moins fréquentes qu'en 2015. Une heure de cours sur {lyc.h_un_sur_l} n'a pas lieu ; en 2024-2025, plus de la moitié de ces heures tient à l'organisation (examens, fermetures, formation) plutôt qu'aux absences des professeurs."
date: 2026-10-07
lastmod: 2026-10-07
og_title: "Manque-t-il des professeurs au lycée ? Concours, classes, cours perdus — S. Lalut"
og_image: "images/og-lycee-professeurs.jpg"
og_image_alt: "Carte de partage : « Manque-t-il des professeurs au lycée ? » — deux barres : part des heures de cours non assurées au lycée général et technologique en 2024-2025 pour absences individuelles des enseignants, et pour l'organisation (examens, fermetures, formation), plus longue."
# Page née du mouvement lycéen de l'automne 2026, pendant la consultation nationale des lycéens (5-23/10/2026).
# Recherche : D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_MOYENS_2026-10-07 (protocole écrit avant calcul, deux contre-expertises
# arbitrées, énoncés des acteurs relus à la source, verdict). Aucun chiffre saisi : jetons {lyc.*} et shortcode lyc-val
# (scripts/update_lycee_professeurs.py, extrait figé et empreintes dans scripts/sources_lycee_professeurs/).
# Français seulement : débat, programme et statistique français (exclusion déclarée).
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
donnees: [lycee_professeurs]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "lycee_professeurs"
  nom: "Lycée : heures de cours non assurées par motif, taille des classes, concours d'enseignants, dépense par élève"
  description: "Séries officielles reprises et recalculées : heures d'enseignement non assurées par motif et par type d'établissement (DEPP, 2023-2024 et 2024-2025), élèves par classe au lycée général et technologique depuis 1994, distribution des tailles de classe et taille vécue par l'élève, élèves par cours selon la discipline, part des heures en groupe, couverture des concours externes, part des contractuels, dépense par lycéen en euros constants, comparaison OCDE."
  couverture_temporelle: "1994/2025"
  couverture_spatiale: "France"
  variables:
    - {nom: "Heures d'enseignement non assurées", unite: "% des heures prévues", description: "par motif : fermeture, examens et commissions, formation, absences individuelles ; établissements publics"}
    - {nom: "Élèves par classe (division)", unite: "élèves", description: "lycée général et technologique, public et privé sous contrat"}
    - {nom: "Part des postes pourvus aux concours externes", unite: "%", description: "CAPES de mathématiques, de physique-chimie, ensemble des concours d'enseignants du second degré public"}
    - {nom: "Dépense par lycéen", unite: "euros de 2024", description: "formations générales et technologiques en lycée, compte de l'éducation"}
  sources:
    - "https://www.education.gouv.fr/depp/reperes-et-references-statistiques-2026-505320"
    - "https://www.education.gouv.fr/depp/la-part-du-temps-d-enseignement-non-assure-dans-les-etablissements-publics-du-second-degre-en-2024-504512"
    - "https://www.education.gouv.fr/depp/le-nombre-d-eleves-devant-un-enseignant-dans-le-second-degre-la-rentree-2025-moins-d-eleves-dans-les-505404"
    - "https://data-explorer.oecd.org/"
  mots: ["lycée", "professeurs", "enseignants", "concours", "CAPES", "taille des classes", "remplacement", "heures non assurées", "DEPP", "éducation"]
  fichiers: ["lycee_professeurs.csv", "lycee_professeurs.json"]
  apropos: "professeurs du second degré et lycée"
faq:
  - question: "Manque-t-il des professeurs au lycée ?"
    answer: "Aucune statistique publique ne mesure le besoin d'enseignants. Ce qu'elles mesurent dit plusieurs choses à la fois : les concours de mathématiques et de physique-chimie restent sous quatre postes pourvus sur cinq ({lyc.m25} % et {lyc.pc25} % en 2025), alors que l'ensemble des concours externes se redresse ; la part des contractuels parmi les enseignants du second degré public est passée de {lyc.contr_debut} % à {lyc.contr_fin} % ; une heure de cours sur {lyc.h_un_sur_l} n'a pas lieu au lycée général et technologique."
  - question: "Combien d'heures de cours sont perdues au lycée ?"
    answer: "En 2024-2025, {lyc.h_total} % des heures prévues n'ont pas été assurées dans les lycées généraux et technologiques publics : {lyc.h_indiv} points pour absences individuelles des enseignants non remplacées (maladie, congés, grèves), {lyc.h_sys} pour des enseignants mobilisés par les examens ou les commissions, {lyc.h_ferm} pour la fermeture de l'établissement, surtout pendant les examens, et {lyc.h_form} pour la formation continue (DEPP)."
  - question: "Les classes de lycée sont-elles surchargées ?"
    answer: "Le mot n'a pas de seuil officiel. Les classes du lycée général et technologique comptent {lyc.ed} élèves en moyenne en {lyc.ed_an}, plus qu'à toute année de 1994 à 2015 ; deux sur trois ont 30 élèves ou plus. Près d'un lycéen du public sur quatre ({lyc.el35_pub} %) est dans une classe de 35 ou plus, mais la part des classes de 35 et plus est plus faible qu'en 2015 ({lyc.div35_25} % contre {lyc.div35_15} %)."
  - question: "La France dépense-t-elle peu pour ses lycéens ?"
    answer: "Non en comparaison internationale : selon l'OCDE, la dépense publique par élève du lycée général dépasse l'agrégat de l'OCDE de {lyc.c3_pct} % en {lyc.c3_an}, et chaque année depuis {lyc.c3_debut}, avec un écart qui se resserre. Dans le temps, la dépense par lycéen général et technologique, en euros constants, est {lyc.c1_baisse} % sous son niveau de 2010 (DEPP)."
  - question: "Quel lien avec le livre La Société du premier coup ?"
    answer: "Cette page décrit les moyens du lycée. Le livre pose la question qui vient ensuite : après un premier échec, qui peut réellement recommencer, et à quel coût selon son parcours et son milieu ? Une prochaine ressource la traitera à partir des données sur les parcours d'élèves."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "ecole"
  rang: 10
  nature: "Séries officielles reprises et recalculées (DEPP, OCDE) ; énoncés du débat testés"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Manque-t-il des professeurs au lycée ?"
  court: "Professeurs"
  role: "concours, classes, cours perdus"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Relevé du&nbsp;: {{< lyc-val "date_donnees" >}}</span> DEPP&nbsp;: Repères et références statistiques 2026, Notes d'Information 26-14, 25-36 et 26-38&nbsp;; OCDE, dépense par élève (2012-2023)&nbsp;; énoncés relus à leur source. Télécharger&nbsp;: <a href="/lycee_professeurs.csv">CSV</a> · <a href="/lycee_professeurs.json">JSON</a> · <a href="#sources">méthode</a></p>

## Une heure de cours sur dix n'a pas lieu&nbsp;: pourquoi&nbsp;? {#heures-perdues}

<figure class="figure-ciseau">
  <img src="/img/lycee-heures.svg" alt="Barres empilées, 2024-2025, part des heures de cours non assurées : lycée général et technologique {{< lyc-val "h_total" >}} %, dont absences individuelles {{< lyc-val "h_indiv" >}}, examens et commissions {{< lyc-val "h_sys" >}}, fermeture {{< lyc-val "h_ferm" >}}, formation {{< lyc-val "h_form" >}} ; lycée professionnel {{< lyc-val "lp_total" >}} % ; collège {{< lyc-val "col_total" >}} %, dont absences individuelles {{< lyc-val "col_indiv" >}}." width="720" height="322" loading="lazy">
  <figcaption>Heures d'enseignement prévues et non assurées, par motif, dans les établissements publics du second degré, 2024-2025 (DEPP, Note d'Information 26-14).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** Au lycée général et technologique public, {{< lyc-val "h_total" >}}&nbsp;% des heures de cours prévues n'ont pas eu lieu en 2024-2025, une sur {{< lyc-val "h_un_sur_l" >}}&nbsp;; les absences individuelles des enseignants non remplacées en expliquent {{< lyc-val "h_indiv" >}}&nbsp;points, l'organisation {{< lyc-val "h_org" >}}&nbsp;: fermetures pendant les examens, enseignants mobilisés par les examens ou les commissions, formation.

</div>

Le chiffre circule&nbsp;: «&nbsp;10&nbsp;% d'heures non assurées dans les lycées&nbsp;». Il est exact pour le lycée général et technologique public, {{< lyc-val "h_total" >}}&nbsp;%. Mais il réunit des heures perdues pour des raisons très différentes, que la DEPP distingue. Les **absences individuelles** non remplacées (maladie, congé, grève, convenance personnelle) pèsent {{< lyc-val "h_indiv_pt" >}}. Le reste tient au fonctionnement même du système&nbsp;: {{< lyc-val "h_ferm_pt" >}} de **fermeture** de l'établissement, presque entièrement pour l'organisation des examens, {{< lyc-val "h_sys_pt" >}} d'enseignants **mobilisés par les examens ou les commissions**, {{< lyc-val "h_form_pt" >}} de **formation** continue.

Le lycée se distingue sur ce point. Au collège, les deux parts s'équilibrent ({{< lyc-val "col_indiv" >}}&nbsp;points d'absences individuelles, {{< lyc-val "col_org" >}} d'organisation)&nbsp;: c'est le calendrier des examens qui fait la différence, et il pèse surtout sur les lycées généraux et technologiques. En 2023-2024, l'enquête ne publiait ses résultats qu'à l'unité&nbsp;: {{< lyc-val "h3_org" >}}&nbsp;points d'organisation contre {{< lyc-val "h3_indiv" >}} d'absences individuelles, même sens, mais à l'arrondi près. Le constat tient donc sur une année publiée au dixième&nbsp;; il ne s'écrit pas comme une constante.

Ce n'est pas dire que les absences sont rares. Dans l'ensemble du second degré public, {{< lyc-val "sd_nr" >}}&nbsp;% des heures sont perdues faute de remplacement, et les journées d'absence de plus de quinze jours non remplacées ont augmenté de {{< lyc-val "e9_h" >}}&nbsp;% entre 2018-2019 et 2023-2024 ({{< lyc-val "e9_j" >}}&nbsp;journées, chiffres du ministère publiés par le Sénat), la seule série publique trouvée sur les absences longues. La statistique ne dit pas, en revanche, où ces heures se perdent&nbsp;: elle n'est publiée ni par académie ni selon la durée des absences.

## Les concours manquent-ils de candidats&nbsp;? {#concours}

<figure class="figure-ciseau">
  <img src="/img/lycee-concours.svg" alt="Courbes 2008-2025 de la part des postes pourvus aux concours externes : CAPES de mathématiques {{< lyc-val "m23" >}} % en 2023, {{< lyc-val "m24" >}} en 2024, {{< lyc-val "m25" >}} en 2025 ; CAPES de physique-chimie {{< lyc-val "pc23" >}}, {{< lyc-val "pc24" >}}, {{< lyc-val "pc25" >}} ; ensemble des concours externes d'enseignants du second degré {{< lyc-val "nat15" >}} % en 2015, {{< lyc-val "nat25" >}} en 2025." width="720" height="342" loading="lazy">
  <figcaption>Part des postes offerts aux concours externes pourvus par des admis, enseignement public (DEPP, Repères et références statistiques 2026).</figcaption>
</figure>

Pour la session 2026, le ministère annonce que {{< lyc-val "e7" >}}&nbsp;% des postes des concours externes du second degré «&nbsp;seront pourvus&nbsp;», contre {{< lyc-val "e7_25" >}}&nbsp;% en 2025. Le chiffre inclut les conseillers d'éducation et les psychologues, et les listes complémentaires&nbsp;; la série de la DEPP, qui ne compte que les admis aux concours d'enseignants, donnait {{< lyc-val "nat25" >}}&nbsp;% en 2025. Ramené à cette base, le taux de 2026 serait d'environ {{< lyc-val "e7_base" >}}&nbsp;%&nbsp;: au-dessus de toutes les années publiées depuis 2015 (au plus {{< lyc-val "nat_max" >}}&nbsp;% en {{< lyc-val "nat_max_an" >}}), en dessous des niveaux de 2005 et 2010 ({{< lyc-val "nat05" >}} et {{< lyc-val "nat10" >}}&nbsp;%). La session 2026 est particulière&nbsp;: deux concours, à bac+3 et à bac+5, et nettement plus de postes offerts qu'en 2025.

La moyenne nationale cache les disciplines. Le CAPES de mathématiques a pourvu {{< lyc-val "m23" >}}&nbsp;%, {{< lyc-val "m24" >}}&nbsp;% puis {{< lyc-val "m25" >}}&nbsp;% de ses postes aux trois dernières sessions publiées, celui de physique-chimie {{< lyc-val "pc23" >}}&nbsp;%, {{< lyc-val "pc24" >}}&nbsp;% et {{< lyc-val "pc25" >}}&nbsp;%&nbsp;: moins de quatre postes sur cinq à chaque fois. L'agrégation de mathématiques reste au-dessus ({{< lyc-val "agm23" >}}&nbsp;% en 2023). En 2024 et 2025, d'autres concours de l'enseignement technologique et professionnel sont aussi restés sous 85&nbsp;% (sciences de l'ingénieur, mathématiques-physique en lycée professionnel)&nbsp;; la session 2023 n'est pas lisible de façon sûre pour eux.

Les postes non pourvus ne restent pas vides&nbsp;: ils sont souvent confiés à des contractuels. Leur part parmi les enseignants du second degré public est passée de {{< lyc-val "contr_debut" >}}&nbsp;% en {{< lyc-val "contr_a0" >}} à {{< lyc-val "contr_fin" >}}&nbsp;% en {{< lyc-val "contr_a1" >}}. Un taux de couverture se rapporte enfin aux postes **offerts**, que fixe le budget&nbsp;: il ne mesure pas le besoin.

## Les classes sont-elles plus chargées qu'avant&nbsp;? {#classes}

<figure class="figure-ciseau">
  <img src="/img/lycee-classes.svg" alt="Courbe du nombre moyen d'élèves par classe au lycée général et technologique, de 1994 à {{< lyc-val "ed_an" >}} : {{< lyc-val "ed_1994" >}} en 1994, {{< lyc-val "ed_max_avant" >}} en {{< lyc-val "ed_an_max_avant" >}}, {{< lyc-val "ed_2021" >}} en 2021, {{< lyc-val "ed" >}} en {{< lyc-val "ed_an" >}}." width="720" height="322" loading="lazy">
  <figcaption>Nombre moyen d'élèves par division, formations générales et technologiques en lycée, public et privé sous contrat (DEPP).</figcaption>
</figure>

Oui en moyenne&nbsp;: {{< lyc-val "ed" >}}&nbsp;élèves par classe en {{< lyc-val "ed_an" >}}, et plus de 30 chaque année depuis 2020, un niveau jamais atteint de 1994 à 2015 (au plus {{< lyc-val "ed_max_avant" >}} en {{< lyc-val "ed_an_max_avant" >}}). La hausse s'est faite entre 2016 et 2020&nbsp;; la moyenne est stable depuis. Deux classes sur trois comptent 30&nbsp;élèves ou plus ({{< lyc-val "div30_25" >}}&nbsp;%, contre {{< lyc-val "div30_15" >}}&nbsp;% en 2015). Mais la part des classes de 35 et plus est **plus faible** qu'en 2015&nbsp;: {{< lyc-val "div35_25" >}}&nbsp;% contre {{< lyc-val "div35_15" >}}&nbsp;%. La classe de 30 à 34 élèves est devenue la norme.

Pourquoi des lycéens disent-ils «&nbsp;nous sommes 35&nbsp;» quand la moyenne est de 30&nbsp;? D'abord parce qu'une moyenne par classe n'est pas la moyenne vécue&nbsp;: une classe de 35 compte 35 témoins, une classe de 15 n'en compte que 15. Dans le public, la classe moyenne compte {{< lyc-val "ed_pub" >}}&nbsp;élèves, mais l'élève moyen est dans une classe de {{< lyc-val "vecue_pub" >}}, et près d'un lycéen sur quatre ({{< lyc-val "el35_pub" >}}&nbsp;%) est dans une classe de 35 ou plus. Ensuite parce que la classe n'est pas toujours le groupe&nbsp;: devant un professeur, un lycéen général et technologique est en moyenne avec {{< lyc-val "es_gt" >}} élèves, de {{< lyc-val "es_min" >}} en {{< lyc-val "es_min_disc" >}} à {{< lyc-val "es_max" >}} en {{< lyc-val "es_max_disc" >}} (mathématiques {{< lyc-val "es_maths" >}}, histoire-géographie {{< lyc-val "es_hg" >}}, philosophie {{< lyc-val "es_philo" >}}). Depuis la réforme du baccalauréat, une grande partie des cours de spécialité se fait en groupe&nbsp;: en première générale, la part des heures en groupe est passée de {{< lyc-val "grp_1g_18" >}}&nbsp;% en 2018 à {{< lyc-val "grp_1g_19" >}}&nbsp;% en 2019, et atteint {{< lyc-val "grp_1g" >}}&nbsp;% en première et {{< lyc-val "grp_tg" >}}&nbsp;% en terminale générales en {{< lyc-val "grp_an" >}}&nbsp;; en seconde, elle a baissé ({{< lyc-val "grp_2nde" >}}&nbsp;%).

## Les moyens ont-ils suivi le nombre d'élèves&nbsp;? {#moyens}

Pas sur vingt ans. Entre {{< lyc-val "a0" >}} et {{< lyc-val "a1" >}}, les lycées généraux et technologiques ont gagné {{< lyc-val "el_var" >}}&nbsp;% d'élèves et perdu {{< lyc-val "div_baisse" >}}&nbsp;% de leurs classes&nbsp;; les heures d'enseignement par élève sont passées de {{< lyc-val "he_a0" >}} à {{< lyc-val "he_a1" >}} par semaine ({{< lyc-val "he_baisse" >}}&nbsp;% de moins), la baisse s'étant faite entre 2010 et 2015 ({{< lyc-val "he_2010" >}} puis {{< lyc-val "he_2015" >}}). Depuis 2020, heures et élèves évoluent au même rythme. En euros constants, la dépense par lycéen général et technologique est de {{< lyc-val "c1_dern" >}}&nbsp;€ en {{< lyc-val "c1_an" >}}, {{< lyc-val "c1_baisse" >}}&nbsp;% sous son niveau de 2010 ({{< lyc-val "c1_max" >}}&nbsp;€).

La comparaison internationale dit autre chose. Selon l'OCDE, la dépense publique par élève du lycée général atteint {{< lyc-val "c3_fra" >}}&nbsp;dollars en parité de pouvoir d'achat en France en {{< lyc-val "c3_an" >}}, contre {{< lyc-val "c3_oecd" >}} pour l'agrégat de l'OCDE&nbsp;: {{< lyc-val "c3_pct" >}}&nbsp;% de plus. La France est au-dessus chaque année depuis {{< lyc-val "c3_debut" >}}, mais l'écart se resserre (il était de {{< lyc-val "c3_pct_debut" >}}&nbsp;%). Ce que coûte un lycéen dépend aussi du nombre d'heures de cours, élevé en France, et des salaires.

Le gouvernement fait valoir une hausse des crédits de l'Éducation nationale de {{< lyc-val "e4_17" >}} à {{< lyc-val "e4_27" >}}&nbsp;milliards d'euros entre 2017 et le projet de budget 2027, hors pensions, soit {{< lyc-val "e4_nom" >}}&nbsp;% en euros courants. Les prix ont déjà monté de {{< lyc-val "e4_prix" >}}&nbsp;% de 2017 à {{< lyc-val "e4_prix_an" >}}&nbsp;: la hausse réelle est donc **au plus** de {{< lyc-val "e4_reel" >}}&nbsp;%, et sera plus faible une fois connus les prix de 2026 et 2027. Comme les élèves seront {{< lyc-val "e4_el_baisse" >}}&nbsp;% moins nombreux en 2027 qu'en 2017 (projection de la DEPP), la hausse réelle par élève atteint au plus {{< lyc-val "e4_par_el" >}}&nbsp;%&nbsp;: elle tient pour une large part à la baisse du nombre d'élèves.

## Tous les lycées sont-ils logés à la même enseigne&nbsp;? {#academies}

Non. Devant un professeur, un lycéen général et technologique du public est en moyenne avec {{< lyc-val "ac_hi_v" >}} élèves dans l'académie de {{< lyc-val "ac_hi" >}}, {{< lyc-val "ac_lo_v" >}} en {{< lyc-val "ac_lo" >}}, en métropole&nbsp;; {{< lyc-val "ac_lo_all_v" >}} en {{< lyc-val "ac_lo_all" >}}. Un écart de {{< lyc-val "ac_ecart" >}} élèves par cours entre les académies extrêmes de métropole. Les heures non assurées, elles, ne sont pas publiées par académie&nbsp;: on ne peut pas savoir, avec la statistique publique, dans quels territoires les lycéens perdent le plus de cours. Le Premier ministre a demandé aux recteurs un premier bilan des absences longues et des postes non pourvus pour le 16&nbsp;octobre 2026&nbsp;; sa publication n'est pas annoncée.

## Ce que disent les acteurs du débat, et ce que montrent les chiffres {#enonces}

| Qui parle | Ce qui est dit | Ce que montrent les données |
|---|---|---|
| SNES-FSU (syndicat d'enseignants), enquête de rentrée 2026 | Il manque au moins un professeur dans {{< lyc-val "e1_snes" >}}&nbsp;% des collèges **et** des lycées | Aucune série publique ne mesure une part d'établissements. Enquête déclarative auprès des sections du syndicat. |
| Union syndicale lycéenne (rapporté par la presse) | «&nbsp;{{< lyc-val "e1_snes" >}}&nbsp;% des lycées&nbsp;» | Même chiffre, présenté pour les seuls lycées alors que la source couvre aussi les collèges. |
| SNPDEN-Unsa (chefs d'établissement, rapporté par la presse) | {{< lyc-val "e1_snpden" >}}&nbsp;% des établissements manquent d'au moins un enseignant | Autre déclarant, même semaine, autre chiffre&nbsp;; aucune série publique ne les départage. |
| Union syndicale lycéenne (rapporté par la presse) | 10&nbsp;% d'heures non assurées dans les lycées | Exact pour le lycée général et technologique public&nbsp;: {{< lyc-val "h_total" >}}&nbsp;%, dont {{< lyc-val "h_indiv" >}} pour absences individuelles. |
| Ministère de l'Éducation nationale, communiqué du 9&nbsp;juillet 2026 | {{< lyc-val "e7" >}}&nbsp;% des postes des concours externes du second degré pourvus | Meilleur niveau des années publiées depuis 2015, sous ceux de 2005 et 2010&nbsp;; mathématiques et physique-chimie restent sous 80&nbsp;%. |
| Premier ministre, lettre du 4&nbsp;octobre 2026 | Crédits portés à {{< lyc-val "e4_27" >}}&nbsp;Md€ contre {{< lyc-val "e4_17" >}} en 2017, hors pensions | + {{< lyc-val "e4_nom" >}}&nbsp;% en euros courants&nbsp;; au plus + {{< lyc-val "e4_reel" >}}&nbsp;% en euros constants. |
| Premier ministre et ministère | Taux de remplacement des absences de moins de quinze jours «&nbsp;triplé&nbsp;» depuis 2022-2023 | De {{< lyc-val "e5_22" >}}&nbsp;% à {{< lyc-val "e5_24" >}}&nbsp;% selon la Cour des comptes&nbsp;: multiplié par {{< lyc-val "e5_f" >}}, sur une base 2022-2023 qu'elle juge fragile&nbsp;; {{< lyc-val "e5_non" >}}&nbsp;% des heures d'absence courte restent non remplacées. |
| Ministère, réponse au Sénat (2025) | «&nbsp;une baisse de 3 points du taux d'heures non assurées depuis 2022-2023&nbsp;» | Sur l'enquête de la DEPP&nbsp;: de {{< lyc-val "sd_total22" >}}&nbsp;% à {{< lyc-val "sd_total" >}}&nbsp;% ({{< lyc-val "sd_var" >}}&nbsp;point). L'indicateur du ministère est probablement un autre, celui du suivi du remplacement court&nbsp;: deux mesures, pas un démenti. |

Le SNES-FSU avance aussi un nombre de postes perdus au CAPES externe 2026&nbsp;; la DEPP n'a pas encore publié cette session, et le chiffre n'est pas vérifiable aujourd'hui.

## Ce que ces données ne disent pas {#limites}

- **Le besoin d'enseignants**&nbsp;: aucune série publique ne le mesure. Les postes offerts aux concours sont une décision budgétaire&nbsp;; «&nbsp;il manque tant de professeurs&nbsp;» ne peut pas s'écrire à partir de ces données.
- **La rentrée 2026**&nbsp;: les chiffres s'arrêtent à la rentrée 2025 pour les classes et à 2024-2025 pour les cours perdus.
- **Les causes**&nbsp;: ces séries se juxtaposent, elles ne disent pas pourquoi les classes ont grossi ou pourquoi les concours scientifiques ne se remplissent pas.
- **Le vécu des élèves**&nbsp;: la qualité des cours, la charge de travail, les conditions matérielles ne sont pas dans ces chiffres. La consultation nationale des lycéens, ouverte jusqu'au 23&nbsp;octobre 2026, en recueille une partie.
- **L'enquête sur les heures non assurées** est déclarative et faite sur un échantillon d'établissements publics&nbsp;; les grèves y sont comptées parmi les absences individuelles.

## Ce qu'il faut retenir {#retenir}

Le «&nbsp;manque de professeurs&nbsp;» recouvre au moins quatre réalités que les chiffres séparent&nbsp;: un recrutement qui se redresse dans l'ensemble mais pas en mathématiques ni en physique-chimie&nbsp;; des classes de plus de 30 élèves devenues la norme, sans que les très grandes classes se soient multipliées&nbsp;; une heure de cours sur {{< lyc-val "h_un_sur_l" >}} perdue au lycée, autant par l'organisation des examens et de la formation que par les absences&nbsp;; une dépense par élève élevée en comparaison internationale, mais inférieure à son niveau de 2010. Aucune de ces mesures ne suffit, seule, à répondre oui ou non.

## Questions fréquentes {#questions}

{{< faq-visible >}}

{{< appel-livre slug="la-societe-du-premier-coup" sur="Après un premier échec, qui peut recommencer ?" avis="non" >}}
Cette page mesure les moyens du lycée. La question qui vient ensuite est celle des parcours&nbsp;: quand un élève échoue une première fois, à un examen, une orientation, une première année d'études, qui peut réellement recommencer, et à quel coût selon son milieu&nbsp;? Le livre montre que cette possibilité de recommencer n'est pas également distribuée.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Heures non assurées.** DEPP, enquête annuelle sur le temps d'enseignement non assuré dans les établissements publics du second degré (Tenae)&nbsp;: Note d'Information 26-14 (avril 2026) pour 2024-2025, au dixième de point, et 25-36 (juin 2025) pour 2023-2024, à l'unité. Motifs&nbsp;: fermeture totale de l'établissement&nbsp;; non-remplacement d'enseignants absents pour fonctionnement du système (organisation d'examens, commissions statutaires), pour formation continue, pour raisons individuelles (maladie, congé maternité ou paternité, grève, convenance personnelle). La série a changé de méthode en 2017&nbsp;: les années antérieures ne sont pas comparables. Absences longues&nbsp;: rapport d'information du Sénat sur le remplacement des enseignants (juin 2025), d'après les données du ministère.

**Classes.** DEPP, *Repères et références statistiques* 2026, fiches 2.05 et 2.06 (série depuis 1994, distribution par taille exacte à la rentrée 2025), 9.13 (élèves par structure, par académie)&nbsp;; RERS 2016 pour la distribution de 2015&nbsp;; Note d'Information 26-38 (élèves par structure selon la discipline, part des heures en groupe). La taille vécue par l'élève est la moyenne des tailles de classe pondérée par le nombre d'élèves, calculée sur la distribution exacte. Les élèves par structure comptent les groupes&nbsp;; la DEPP précise que cet indicateur décrit l'encadrement du côté des enseignants.

**Concours et contractuels.** DEPP, RERS 2026, fiches 9.02, 9.27 et 9.28 (sessions 2008-2025)&nbsp;; RERS 2025 pour la session 2024&nbsp;; ministère de l'Éducation nationale, communiqué du 9&nbsp;juillet 2026 pour la session 2026.

**Dépense.** DEPP, compte de l'éducation (RERS 2026, fiche 10.05), euros de 2024 déflatés par le prix du PIB&nbsp;; OCDE, dépense publique des établissements par élève en équivalent temps plein, second cycle général, dollars en parité de pouvoir d'achat (base de données de *Regards sur l'éducation*, interrogée par son interface officielle). La note pays 2026 de l'OCDE donne {{< lyc-val "c3_fra" >}}&nbsp;dollars pour la France&nbsp;; sa moyenne de l'OCDE diffère légèrement de l'agrégat de la base, car l'une est une moyenne de pays, l'autre un agrégat.

**Énoncés.** Chaque énoncé a été relu à sa source primaire quand elle existe&nbsp;: SNES-FSU, «&nbsp;Rentrée 2026&nbsp;: toujours la pénurie&nbsp;» (7&nbsp;septembre 2026)&nbsp;; lettre du Premier ministre du 4&nbsp;octobre 2026 et dossier de presse du budget 2027 de l'Éducation nationale&nbsp;; réponse du ministère à la question écrite n°&nbsp;05531 (Sénat, *Journal officiel* du 20&nbsp;novembre 2025)&nbsp;; Cour des comptes, *Le temps d'enseignement perdu par les élèves au collège* (décembre 2025), p.&nbsp;47&nbsp;; DEPP, projections d'effectifs à l'horizon 2035 (avril 2026). Les propos de l'Union syndicale lycéenne et du SNPDEN-Unsa ne sont connus que par la presse. Indice des prix du PIB&nbsp;: Eurostat (comptes nationaux de l'Insee).

Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent d'un calcul de l'auteur, dont l'extrait est archivé avec ses empreintes&nbsp;; le script qui écrit la page vérifie chaque affirmation chiffrée et s'arrête si elle n'est plus vraie. Le protocole a été écrit et soumis à une contre-expertise externe avant le premier calcul, et chacun de ses contrôles a détecté les erreurs qu'on y avait introduites volontairement.

{{< reutiliser figures="figures_lycee" jeu="lycee_professeurs" sources="DEPP, ministère de l'Éducation nationale, OCDE, Cour des comptes, Sénat" donnees="Heures non assurées par motif et par type d'établissement, élèves par classe depuis 1994, distribution et taille vécue, élèves par cours selon la discipline, heures en groupe, couverture des concours, contractuels, dépense par lycéen, comparaison OCDE, élèves par cours par académie ; le même contenu existe en CSV, au format long." >}}
Au lycée général et technologique public, {{< lyc-val "h_total" >}}&nbsp;% des heures de cours prévues n'ont pas eu lieu en 2024-2025&nbsp;: {{< lyc-val "h_indiv" >}}&nbsp;points pour absences individuelles des enseignants non remplacées, {{< lyc-val "h_org" >}} pour l'organisation (examens, fermetures, formation). Les CAPES de mathématiques et de physique-chimie ont pourvu moins de quatre postes sur cinq aux trois dernières sessions publiées. Les classes comptent {{< lyc-val "ed" >}}&nbsp;élèves en moyenne en {{< lyc-val "ed_an" >}}, plus de 30 chaque année depuis 2020&nbsp;; la dépense par lycéen dépasse de {{< lyc-val "c3_pct" >}}&nbsp;% l'agrégat de l'OCDE, mais reste {{< lyc-val "c1_baisse" >}}&nbsp;% sous son niveau de 2010.
{{< /reutiliser >}}
