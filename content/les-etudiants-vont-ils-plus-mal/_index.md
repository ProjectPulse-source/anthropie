---
title: "Les étudiants vont-ils plus mal que les autres jeunes ?"
description: "Dépression déclarée, traitements, patients hospitalisés, suicides : ce que les séries officielles disent de la santé mentale des étudiants et des autres jeunes. De 2019 à {etu.hosp_der}, le taux de jeunes femmes de 18 à 24 ans hospitalisées pour un geste auto-infligé a augmenté de {etu.hosp_f_var} %, celui des jeunes hommes de {etu.hosp_h_var} % ; chez les étudiants, l'épisode dépressif déclaré est passé de {etu.etu_2017} % à {etu.etu_2021} % de 2017 à 2021. La comparaison avec les autres jeunes du même âge et du même sexe n'est pas publiée. Données Santé publique France, DREES, Assurance maladie, Eurostat, Insee, recalculées."
chapo: "La dépression déclarée a fortement augmenté chez les étudiants de 2017 à 2021, et les traitements comme le taux de jeunes hospitalisés pour un geste auto-infligé confirment une dégradation réelle dans cette classe d'âge. Mais cette dégradation touche d'abord les jeunes femmes, commence avant l'université et avant le covid, et aucune statistique publiée ne dit encore si les étudiants vont plus mal que les autres jeunes du même âge et du même sexe."
date: 2026-11-06
lastmod: 2026-11-06
# Brouillon jusqu'à la relecture phrase à phrase du texte servi (ressource.refonte posée alors) ; build local : --buildDrafts.
draft: true
og_title: "Les étudiants vont-ils plus mal que les autres jeunes ? Dépression, soins, hôpital — S. Lalut"
og_image: "images/og-etudiants-mal.jpg"
og_image_alt: "Carte de partage : « Les étudiants vont-ils plus mal que les autres jeunes ? » — deux courbes depuis 2012 : le taux de jeunes femmes de 18 à 24 ans hospitalisées pour un geste auto-infligé, en baisse jusqu'en 2014, à peu près plat jusqu'en 2017, puis en forte hausse, et celui des jeunes hommes, qui remonte après 2017, plus modérément."
# Troisième onglet du bloc « École, lycée et université », premier sur le supérieur. Recherche :
# D:\PRO\06_PROMOTION\RECHERCHE_MALAISE_ETUDIANT_2026-10-23 (note de l'auteur du 23/10, six contre-expertises arbitrées,
# sources relues dans leur document original le 06/11, texte v1 dans REDACTION\). Aucun chiffre saisi : jetons {etu.*} et
# shortcode etu-val (scripts/update_malaise_etudiant.py, extrait figé et empreintes dans scripts/sources_malaise_etudiant/).
# Français seulement : statistique et débat français, comme les pages voisines du bloc (exclusion déclarée).
lang_repli: "/en/resources/"  # pas de version anglaise (exclusion déclarée) : cible de l'onglet EN, partials/lang-cible.html
donnees: [malaise_etudiant]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "malaise_etudiant"
  nom: "Santé mentale des étudiants et des jeunes : dépression déclarée, traitements, hospitalisations, suicides, dépense par étudiant"
  description: "Séries officielles reprises et recalculées : épisode dépressif déclaré par situation professionnelle et chez les 18-24 ans par sexe (Santé publique France, 2010, 2017, 2021), patients hospitalisés pour geste auto-infligé par âge et par sexe depuis 2012 (DREES), traitements antidépresseurs des 20-24 ans (Assurance maladie), suicides des 20-24 ans (Eurostat, CépiDc), risque de dépression des lycéens (EnCLASS), dépense par étudiant en euros constants (Insee, compte de l'éducation), part des femmes parmi les étudiants et les non-étudiants de 18 à 24 ans et simulation de l'effet de composition."
  couverture_temporelle: "2010/2025"
  couverture_spatiale: "France"
  variables:
    - {nom: "Épisode dépressif caractérisé au cours des douze derniers mois", unite: "%", description: "déclaré, Baromètre santé ; étudiants, chômeurs, actifs occupés ; 18-24 ans par sexe"}
    - {nom: "Patients hospitalisés pour geste auto-infligé", unite: "pour 100 000 habitants", description: "par sexe et classe d'âge, recalculés à partir des effectifs par âge détaillé"}
    - {nom: "Traitements antidépresseurs", unite: "% de la population", description: "20-24 ans, par sexe, hors pathologies psychiatriques repérées"}
    - {nom: "Taux de suicide", unite: "pour 100 000 habitants", description: "20-24 ans, par sexe"}
    - {nom: "Risque important de dépression des lycéens", unite: "%", description: "EnCLASS, par sexe"}
    - {nom: "Dépense par étudiant", unite: "euros constants de 2024", description: "enseignement supérieur, et par filière en 2024"}
  sources:
    - "https://beh.santepubliquefrance.fr/beh/2023/2/pdf/2023_2_1.pdf"
    - "https://beh.santepubliquefrance.fr/beh/2025/14/pdf/2025_14.pdf"
    - "https://www.santepubliquefrance.fr/sites/default/files/cadic_files/documents/spf00006678.pdf"
    - "https://data.drees.solidarites-sante.gouv.fr/"
    - "https://data.ameli.fr/pages/data-pathologies/"
    - "https://ec.europa.eu/eurostat/databrowser/view/hlth_cd_acdr2/default/table"
    - "https://www.insee.fr/fr/statistiques/8612572"
  mots: ["santé mentale", "étudiants", "malaise étudiant", "dépression", "jeunes", "jeunes femmes", "geste auto-infligé", "tentative de suicide", "antidépresseurs", "lycéens", "université", "dépense par étudiant"]
  fichiers: ["malaise_etudiant.csv", "malaise_etudiant.json"]
  apropos: "santé mentale des étudiants et des jeunes en France"
faq:
  - question: "Les étudiants vont-ils plus mal que les autres jeunes ?"
    answer: "Personne ne peut encore le dire. De 2017 à 2021, la part des étudiants déclarant un épisode dépressif dans l'année est passée de {etu.etu_2017} % à {etu.etu_2021} %, la plus forte hausse parmi les situations professionnelles publiées par Santé publique France ({etu.h_etu}, contre {etu.h_chom} chez les chômeurs et {etu.h_actifs} chez les actifs occupés). Mais ces groupes n'ont ni le même âge ni la même composition par sexe, et la comparaison entre étudiants et non-étudiants du même âge et du même sexe n'a pas été publiée."
  - question: "La santé mentale des jeunes s'est-elle vraiment dégradée, ou en parle-t-on davantage ?"
    answer: "Elle s'est dégradée : des indicateurs qui enregistrent des actes, et non des réponses à un questionnaire, vont dans le même sens. De 2019 à {etu.hosp_der}, le taux de jeunes femmes de 18 à 24 ans hospitalisées pour un geste auto-infligé a augmenté de {etu.hosp_f_var} % (DREES) ; la part des femmes de 20 à 24 ans traitées par antidépresseurs est passée de {etu.ad_f_2017} % en 2017 à {etu.ad_f_2024} % en 2024 (Assurance maladie). Une partie de la hausse des déclarations peut toutefois tenir à une parole plus libre."
  - question: "Les jeunes femmes sont-elles plus touchées ?"
    answer: "Oui, dans toutes les sources. Chez les 18-24 ans, l'épisode dépressif déclaré est passé de {etu.f1824_2017} % à {etu.f1824_2021} % chez les femmes entre 2017 et 2021, de {etu.h1824_2017} % à {etu.h1824_2021} % chez les hommes. Le taux de jeunes femmes hospitalisées pour un geste auto-infligé a augmenté de {etu.hosp_f_var} % de 2019 à {etu.hosp_der}, celui des jeunes hommes de {etu.hosp_h_var} %. Au lycée, {etu.lyc_f_2024} % des filles présentent un risque important de dépression en 2024, contre {etu.lyc_g_2024} % des garçons (EnCLASS)."
  - question: "Le malaise des étudiants vient-il du covid ?"
    answer: "Il ne commence pas avec lui. La part des étudiants déclarant un épisode dépressif était déjà passée de {etu.etu_2010} % en 2010 à {etu.etu_2017} % en 2017, et le taux de jeunes femmes hospitalisées pour un geste auto-infligé remonte dès 2018. Le confinement a frappé particulièrement les étudiants ; il a accéléré une hausse déjà engagée, sans la déclencher."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["explicatif-causal", "quantitatif"]  # protocoles de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/les-etudiants-vont-ils-plus-mal.md"  # fiche de conception (regle 12)
  bloc: "ecole"
  livres: ["la-societe-du-premier-coup"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 30
  nature: "Séries officielles reprises et recalculées (Santé publique France, DREES, Assurance maladie, Eurostat, Insee) ; six causes du débat confrontées aux données"
onglet:  # barre du dossier de son bloc (partials/barre-bloc.html, posée par le gabarit)
  long: "Les étudiants vont-ils plus mal que les autres jeunes ?"
  court: "Étudiants"
  role: "santé mentale, 18-24 ans"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< etu-val "date_donnees" >}}</span> Santé publique France&nbsp;: Baromètre santé (BEH 2023 n°&nbsp;2 et 2025 n°&nbsp;14), EnCLASS 2024&nbsp;; DREES, patients hospitalisés pour geste auto-infligé depuis 2012&nbsp;; Assurance maladie, cartographie des pathologies&nbsp;; Eurostat (CépiDc-Inserm)&nbsp;; Insee, compte de l'éducation. Télécharger&nbsp;: <a href="/malaise_etudiant.csv">CSV</a> · <a href="/malaise_etudiant.json">JSON</a> · <a href="#sources">méthode</a></p>

## Le malaise déclaré est-il confirmé par les soins&nbsp;? {#malaise-confirme-par-les-soins}

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/etudiants-hospit-m.svg" width="300" height="713">
    <img src="/img/etudiants-hospit.svg" alt="Deux courbes de 2012 à {{< etu-val "hosp_der" >}}, patients hospitalisés pour un geste auto-infligé pour 100 000 habitants : femmes de 18 à 24 ans {{< etu-val "hosp_f_2012" >}} en 2012, {{< etu-val "hosp_f_2014" >}} en 2014, {{< etu-val "hosp_f_2017" >}} en 2017, {{< etu-val "hosp_f_2019" >}} en 2019, {{< etu-val "hosp_f_der" >}} en {{< etu-val "hosp_der" >}} ; hommes de 18 à 24 ans {{< etu-val "hosp_h_2012" >}} en 2012, {{< etu-val "hosp_h_2017" >}} en 2017, {{< etu-val "hosp_h_2019" >}} en 2019, {{< etu-val "hosp_h_der" >}} en {{< etu-val "hosp_der" >}}." width="720" height="389" loading="lazy">
  </picture>
  <figcaption>Patients hospitalisés pour un geste auto-infligé, 18-24 ans, par sexe (DREES, calcul de l'auteur).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De 2019 à {{< etu-val "hosp_der" >}}, le taux de jeunes femmes de 18 à 24 ans hospitalisées pour un geste auto-infligé a augmenté de {{< etu-val "hosp_f_var" >}}&nbsp;%, celui des jeunes hommes de {{< etu-val "hosp_h_var" >}}&nbsp;%&nbsp;: la dégradation est réelle, touche d'abord les jeunes femmes et commence avant le covid&nbsp;; chez les étudiants, la dépression déclarée est passée de {{< etu-val "etu_2017" >}}&nbsp;% à {{< etu-val "etu_2021" >}}&nbsp;% de 2017 à 2021, la plus forte hausse parmi les situations professionnelles publiées, mais **personne n'a encore publié la comparaison qui trancherait&nbsp;: avec les jeunes non étudiants du même âge et du même sexe.**

</div>

Le chiffre qui a installé l'idée d'un «&nbsp;malaise étudiant&nbsp;» vient du Baromètre santé de Santé publique France&nbsp;: en 2021, {{< etu-val "etu_2021" >}}&nbsp;% des étudiants déclarent un épisode dépressif caractérisé au cours des douze derniers mois, contre {{< etu-val "etu_2017" >}}&nbsp;% en 2017 et {{< etu-val "etu_2010" >}}&nbsp;% en 2010. Dans aucune autre situation professionnelle la hausse n'est aussi forte&nbsp;: {{< etu-val "h_etu" >}} chez les étudiants, {{< etu-val "h_chom" >}} chez les chômeurs, {{< etu-val "h_actifs" >}} chez les actifs occupés.

Un questionnaire mesure ce que l'on déclare. Or déclarer plus n'est pas forcément souffrir plus&nbsp;: la parole sur la santé mentale s'est libérée, et une partie de la hausse peut en venir. Pour savoir si quelque chose a changé au-delà des mots, il faut des indicateurs d'une autre nature, qui enregistrent des actes plutôt que des réponses.

Trois d'entre eux vont dans le même sens chez les jeunes adultes.

- **Ce que l'on soigne.** La part des jeunes femmes de 20 à 24 ans traitées par antidépresseurs, hors maladie psychiatrique repérée, passe de {{< etu-val "ad_f_2017" >}}&nbsp;% en 2017 à {{< etu-val "ad_f_2021" >}}&nbsp;% en 2021 puis à {{< etu-val "ad_f_2024" >}}&nbsp;% en 2024 (Assurance maladie). Pour l'ensemble des 20-24 ans, la hausse commence dès 2018, avant le covid.
- **Ce qui conduit à l'hôpital.** Les jeunes femmes de 18 à 24 ans hospitalisées pour un geste auto-infligé (tentative de suicide, automutilation) étaient {{< etu-val "hosp_f_2019" >}} pour 100&nbsp;000 en 2019&nbsp;; elles sont {{< etu-val "hosp_f_der" >}} en {{< etu-val "hosp_der" >}}, soit {{< etu-val "hosp_f_var" >}}&nbsp;% de plus (DREES).
- **Ce qui est irréversible.** Les suicides de jeunes femmes de 20 à 24 ans restent rares, une centaine par an, mais leur taux a augmenté de {{< etu-val "sf_var" >}}&nbsp;% entre 2018-2019 et 2021-2023 (de {{< etu-val "sf_avant" >}} à {{< etu-val "sf_apres" >}} pour 100&nbsp;000). Celui des hommes du même âge est resté à peu près stable ({{< etu-val "sm_var" >}}&nbsp;%). En 2024, {{< etu-val "s_n24" >}}&nbsp;décès contre {{< etu-val "s_n23" >}} l'année précédente&nbsp;: le niveau élevé se maintient, sans nouvelle hausse établie.

**Ces séries ne distinguent pas les étudiants des autres jeunes.** Elles établissent qu'une dégradation réelle touche la tranche d'âge des étudiants&nbsp;; elles ne disent rien de leur situation propre.

Elles laissent aussi une part d'incertitude. Un traitement suppose l'accès à un médecin, et une hausse des prescriptions peut traduire un meilleur recours aux soins autant qu'une souffrance accrue. Les trois indicateurs ne sont d'ailleurs pas indépendants&nbsp;: un même geste peut conduire à l'hôpital puis à un traitement. Leur accord écarte l'idée d'une hausse purement déclarative&nbsp;; il ne mesure pas la part de chaque cause.

Toutes les mesures ne bougent pas, enfin. Sur la même période, les enquêtes ne détectent pas de hausse significative des états anxieux (Santé publique France, 2025). Le «&nbsp;malaise&nbsp;» n'est pas une grandeur unique&nbsp;: la dépression déclarée a augmenté, l'anxiété mesurée par un autre instrument non.

## Qui connaît la plus forte dégradation&nbsp;? {#qui-se-degrade-le-plus}

Dans toutes les sources, l'écart le plus constant sépare les femmes des hommes, bien plus que les étudiants des autres jeunes.

Chez les 18-24 ans, l'épisode dépressif déclaré passe de {{< etu-val "f1824_2017" >}}&nbsp;% à {{< etu-val "f1824_2021" >}}&nbsp;% chez les femmes entre 2017 et 2021 ({{< etu-val "f1824_hausse" >}}), de {{< etu-val "h1824_2017" >}}&nbsp;% à {{< etu-val "h1824_2021" >}}&nbsp;% chez les hommes ({{< etu-val "h1824_hausse" >}}). Le taux de jeunes femmes hospitalisées pour un geste auto-infligé a augmenté de {{< etu-val "hosp_f_var" >}}&nbsp;% de 2019 à {{< etu-val "hosp_der" >}}, celui des jeunes hommes de {{< etu-val "hosp_h_var" >}}&nbsp;% (de {{< etu-val "hosp_h_2019" >}} à {{< etu-val "hosp_h_der" >}} pour 100&nbsp;000). Même contraste sur les suicides et sur les traitements&nbsp;: chez les 20-24&nbsp;ans, la part des jeunes femmes sous antidépresseurs passe de {{< etu-val "ad_f_2017" >}}&nbsp;% à {{< etu-val "ad_f_2024" >}}&nbsp;% de 2017 à 2024, celle des jeunes hommes de {{< etu-val "ad_h_2017" >}}&nbsp;% à {{< etu-val "ad_h_2024" >}}&nbsp;%.

Le calendrier diffère, lui aussi, selon l'âge et le sexe&nbsp;:

- le taux de **femmes de 18 à 24 ans** hospitalisées pour un geste auto-infligé baisse jusqu'en 2014, reste à peu près stable jusqu'en 2017, puis monte&nbsp;;
- celui des **filles de 15 à 17 ans** monte dès le milieu des années 2010 et bondit en 2021, après le creux de 2020&nbsp;;
- celui des **jeunes hommes** remonte après 2017, mais beaucoup moins&nbsp;;
- celui des **femmes de 25 à 44 ans** baisse jusqu'en 2022 et ne remonte qu'à partir de 2023.

Le récit public réunit «&nbsp;les jeunes&nbsp;» dans une même crise, datée du covid. Les séries montrent des trajectoires distinctes, dont la plus marquée est celle des adolescentes et des jeunes femmes. Ce constat n'est pas propre à cette page&nbsp;: l'Observatoire national du suicide situe le début de cette hausse en 2017 dans son rapport de 2025, la DREES au «&nbsp;milieu des années 2010&nbsp;» dans sa publication du 11&nbsp;mai 2026, qui s'appuie sur la même série hospitalière que nous. Nos calculs s'accordent avec eux.

## Le phénomène existe-t-il avant l'université&nbsp;? {#avant-l-universite}

Si la dégradation tenait d'abord aux études, elle devrait apparaître à l'entrée dans le supérieur. Elle est visible avant.

Chez les 15-17 ans, tous sexes confondus, le taux de patients hospitalisés pour un geste auto-infligé passe de {{< etu-val "hosp_t1517_2019" >}} à {{< etu-val "hosp_t1517_der" >}} pour 100&nbsp;000 entre 2019 et {{< etu-val "hosp_der" >}}. En 2025, la DREES compte {{< etu-val "hosp_f1019_2025" >}} patientes hospitalisées pour 100&nbsp;000 filles de 10 à 19 ans, davantage que chez les jeunes femmes de 18 à 24 ans la même année.

Les enquêtes auprès des lycéens disent la même chose sous une autre forme. La part des lycéens qui présentent un risque important de dépression passe de {{< etu-val "lyc_2022" >}}&nbsp;% en 2022 à {{< etu-val "lyc_2024" >}}&nbsp;% en 2024, après une première hausse d'environ deux points entre 2018 et 2022&nbsp;; chez les lycéennes, de {{< etu-val "lyc_f_2018" >}}&nbsp;% en 2018 à {{< etu-val "lyc_f_2024" >}}&nbsp;% en 2024, contre {{< etu-val "lyc_g_2024" >}}&nbsp;% chez les garçons en 2024 (Santé publique France, EnCLASS). Ce risque continue de croître alors que le bien-être déclaré remonte par rapport à 2022 ({{< etu-val "be_lycee" >}} au lycée)&nbsp;: là encore, le «&nbsp;malaise&nbsp;» n'est pas une grandeur unique.

Une détresse qui précède l'université ne disculpe pas l'université. Les études peuvent l'aggraver, la révéler ou l'atténuer, et ce que l'on observe chez les étudiants mêle ce qu'ils apportent de leur adolescence à ce que les études y ajoutent. Mais l'origine d'un trouble ne désigne pas le lieu du remède&nbsp;: un service de santé universitaire peut être utile pour une souffrance née au lycée.

## Les conditions sociales et d'études modifient-elles le risque&nbsp;? {#conditions-sociales-et-d-etudes}

Plusieurs conditions d'études se sont dégradées, et certaines sont associées à la détresse.

- **Les moyens par étudiant.** En euros constants, la dépense moyenne par étudiant culmine en 2009 ({{< etu-val "dep_2009" >}}&nbsp;€) et n'a plus retrouvé ce niveau depuis&nbsp;: {{< etu-val "dep_2024" >}}&nbsp;€ en 2024. Elle varie fortement selon les filières&nbsp;: {{< etu-val "dep_univ" >}}&nbsp;€ par étudiant à l'université contre {{< etu-val "dep_cpge" >}}&nbsp;€ en classe préparatoire en 2024 (Insee, d'après le compte de l'éducation de la Depp).
- **L'argent.** Dans les enquêtes de l'Observatoire de la vie étudiante, les difficultés financières vont de pair avec une détresse plus fréquente.
- **L'isolement.** Le premier confinement a frappé particulièrement les étudiants&nbsp;: dans l'étude CONFINS, menée en ligne au printemps 2020, leur risque de symptômes dépressifs était plus élevé que celui des non-étudiants après ajustement (rapport de cotes {{< etu-val "confins_or" >}}).

Ces associations ne font pas une cause. La précarité peut entraîner la détresse&nbsp;; la détresse peut aussi faire échouer ou abandonner les études, et ceux qui vont le plus mal sortent alors de la population observée. CONFINS ne représente pas l'ensemble des jeunes et ne couvre qu'un moment, le premier confinement. Enfin, la dépense par étudiant recule depuis 2009, et la dépression déclarée des étudiants monte déjà de {{< etu-val "etu_2010" >}}&nbsp;% en 2010 à {{< etu-val "etu_2017" >}}&nbsp;% en 2017&nbsp;: les deux calendriers se recouvrent. Le taux de jeunes femmes hospitalisées, qui compte toutes les jeunes femmes, étudiantes ou non, ne remonte en revanche qu'à partir de 2018. Le calendrier ne permet donc ni d'établir ni d'écarter un lien.

## Que reste-t-il de spécifiquement étudiant&nbsp;? {#specifiquement-etudiant}

**C'est la question du titre, et aucune statistique publiée n'y répond encore.**

La hausse de la dépression déclarée chez les étudiants est la plus forte parmi les situations professionnelles publiées, mais elle compare des groupes qui n'ont ni le même âge ni la même composition&nbsp;: les étudiants sont jeunes et majoritairement des femmes, les actifs occupés ont de 18 à 75&nbsp;ans. Les auteurs du Baromètre le signalent eux-mêmes. Pour savoir ce que les études ajoutent, il faudrait comparer l'évolution des étudiants à celle des jeunes non étudiants **du même âge et du même sexe**. Cette comparaison n'a pas été publiée. Nous l'avons demandée à Santé publique France.

### Ce que change la composition des populations {#composition-des-populations}

On peut au moins estimer ce que produirait le seul écart de composition par sexe.

Parmi les 18-24 ans, la part des femmes est plus élevée chez les étudiants que chez les non-étudiants&nbsp;: de {{< etu-val "comp_ecart_2017" >}} en 2017, de {{< etu-val "comp_ecart_2021" >}} en 2021 (Eurostat). Or la dépression déclarée a progressé plus vite chez les jeunes femmes. Si étudiants et non-étudiants du même sexe avaient connu exactement la même évolution, la seule différence de composition aurait rendu, de 2017 à 2021, la hausse des étudiants supérieure d'environ **{{< etu-val "comp_sim" >}}** à celle des non-étudiants.

C'est une simulation, pas une mesure. Elle dit ce que l'on devrait observer si le statut d'étudiant n'avait aucun effet, à sexe égal&nbsp;; elle ne dit pas ce que l'on observe. Quand la comparaison à âge et sexe égaux sera disponible, elle se lira ainsi&nbsp;:

| Si l'écart de hausse 2017-2021 observé entre étudiants et non-étudiants est… | … on pourra dire |
|---|---|
| proche de {{< etu-val "comp_sim" >}} | la composition par sexe suffit à en rendre compte, sans que cela prouve qu'il n'y ait rien d'autre |
| nettement supérieur | le sexe ne suffit pas&nbsp;; d'autres différences sont à chercher (âge détaillé, origine sociale, argent, logement, conditions d'études) |
| inférieur ou négatif | d'autres mécanismes compensent, ou la simulation surestime l'effet de composition |

Si un écart subsiste à âge et sexe égaux, il restera une association avec le fait d'étudier, qui ne prouvera pas que l'université en soit la cause. Même ajustée, une comparaison entre étudiants et non-étudiants reste descriptive&nbsp;: les deux groupes ne sont pas tirés au hasard, et une absence d'écart ne disculperait pas l'université, puisque ses effets protecteurs et ses effets néfastes peuvent se compenser.

## Les six causes du récit courant, à l'épreuve {#six-causes-a-l-epreuve}

Le récit le plus répandu empile six causes&nbsp;: la massification de l'université depuis 1985 sans moyens à la hauteur&nbsp;; des réformes qui fragmentent les études&nbsp;; le smartphone&nbsp;; le covid&nbsp;; l'inflation et le coût du logement&nbsp;; l'absence de perspectives. Son contre-récit en fait un malaise de génération, sans rapport avec l'université. Chacun de ces récits est confronté aux faits selon la même grille.

| Cause invoquée | Ce qui concorde | Ce qui l'affaiblit ou l'affaiblirait | Ce que l'on peut dire |
|---|---|---|---|
| Massification sans moyens | dépense par étudiant en recul depuis 2009 | une dégradation aussi forte chez les jeunes qui n'étudient pas | une transformation documentée, dont la contribution au malaise n'est pas mesurée |
| Réformes des études | — | — | aucun indicateur ne les relie à la santé mentale&nbsp;: non testé ici |
| Smartphone et réseaux sociaux | dégradation visible au lycée, plus forte chez les filles | des politiques scolaires restrictives sans effet détecté (étude SMART Schools, 2025) | un effet possible de certaines pratiques, non un facteur établi |
| Covid et confinement | accélération après 2020&nbsp;; risque plus élevé chez les étudiants en 2020 (CONFINS) | la hausse commence au milieu des années 2010 | un accélérateur, pas l'origine |
| Inflation et logement | précarité associée à la détresse | l'inflation commence en 2022, après la hausse de 2017-2021 | l'inflation ne peut pas expliquer la hausse mesurée jusqu'en 2021&nbsp;; le logement n'est pas mesuré ici |
| Absence de perspectives | — | — | non mesuré par ces sources |
| Malaise de génération (contre-récit) | dégradation aussi chez les autres jeunes, lycéens compris | un écart propre aux étudiants à âge et sexe égaux | plausible, non démontré&nbsp;; la comparaison manquante les départagera |

## Juger les politiques sur leurs effets {#juger-les-politiques}

Une souffrance qui touche toute une génération n'interdit pas d'agir à l'université, où se trouvent une partie de ces jeunes et des services capables de les recevoir. Mais l'utilité d'une mesure ne se déduit pas de l'origine du trouble&nbsp;: repas à 1&nbsp;€, aide psychologique, restrictions du téléphone se jugent sur leurs effets mesurés, question distincte de celle que traite cette page.

## Ce que ces données ne disent pas {#limites}

- **La comparaison décisive manque**&nbsp;: étudiants et non-étudiants du même âge et du même sexe, en 2017 et en 2021.
- **Les séries de soins et d'hospitalisation ignorent le statut d'étudiant**, et les suicides comptés à partir de 2018 ne se comparent pas à ceux d'avant&nbsp;: un nouveau certificat de décès a amélioré le recueil cette année-là.
- **Le Baromètre santé de 2024 ne se compare pas à celui de 2021** (changement de méthode)&nbsp;: la série déclarative s'arrête en 2021.
- **Les enquêtes de l'Observatoire de la vie étudiante ne forment pas une série homogène**&nbsp;: aucune évolution n'est calculée à partir d'elles.
- **Ce que l'on déclare, ce que l'on soigne et ce qui conduit à l'hôpital** mesurent trois réalités distinctes&nbsp;: leur accord établit le sens de l'évolution, pas son ampleur.

<aside class="encadre">

**Une hypothèse de l'auteur, non testée sur ces données.** Dans le working paper [AWP-08](/awp/awp-08/), l'économiste Stéphane Lalut propose de lire aussi les inégalités à travers ce qu'il appelle la [réversibilité sociale](/reversibilite-sociale/)&nbsp;: ce qu'une personne peut se permettre de rater sans fermer durablement son avenir. Si l'échec devient moins réversible, l'enjeu de chaque épreuve monte, et avec lui l'angoisse de la performance. C'est un cadre réfutable.

</aside>

## Questions fréquentes {#questions}

{{< faq-visible >}}

{{< appel-livre slug="la-societe-du-premier-coup" sur="Ce qu'une année ratée coûte dépend de qui la rate" avis="non" >}}
Cette page mesure une souffrance&nbsp;; elle ne dit pas ce que coûte, pour un étudiant, un échec d'études. Le livre compte combien de tentatives une trajectoire autorise réellement, et montre que la possibilité de recommencer n'est pas également distribuée.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Dépression et anxiété déclarées.** Santé publique France, Baromètre santé&nbsp;: [BEH 2023 n°&nbsp;2](https://beh.santepubliquefrance.fr/beh/2023/2/pdf/2023_2_1.pdf) (Léon, du Roscoät, Beck), épisode dépressif caractérisé au cours des douze derniers mois (questionnaire CIDI-SF), 18-75&nbsp;ans, 2017 et 2021, par situation professionnelle et par sexe et âge&nbsp;; les niveaux des étudiants en 2010 et en 2017 sont lus sur la figure&nbsp;3&nbsp;; celui de 2017 est contrôlé par l'écart que publie le texte, pas celui de 2010. États anxieux&nbsp;: [BEH 2025 n°&nbsp;14](https://beh.santepubliquefrance.fr/beh/2025/14/pdf/2025_14.pdf) (échelle HAD). Le Baromètre de 2024, dont la méthode a changé, n'est pas comparé à celui de 2021.

**Lycéens.** Santé publique France, [EnCLASS 2024](https://www.santepubliquefrance.fr/sites/default/files/cadic_files/documents/spf00006678.pdf) (*Le point sur*, 2&nbsp;juin 2026)&nbsp;: risque important de dépression des lycéens, 2018, 2022 et 2024, par sexe, et bien-être déclaré.

**Patients hospitalisés.** DREES, patients hospitalisés pour geste auto-infligé depuis 2012 (PMSI, médecine, chirurgie, obstétrique)&nbsp;: taux recalculés pour chaque classe d'âge à partir des effectifs et des populations par âge détaillé. Témoin&nbsp;: les trois chiffres de la publication de la DREES du 11&nbsp;mai 2026 (filles de 10 à 19&nbsp;ans en 2025, femmes de 10 à 29&nbsp;ans en 2012 et en 2025), retrouvés à l'unité.

**Traitements.** Assurance maladie, cartographie des pathologies et des dépenses (effectifs)&nbsp;: traitements antidépresseurs ou régulateurs de l'humeur, hors pathologies psychiatriques repérées, 20-24&nbsp;ans, par sexe.

**Suicides.** Eurostat, causes de décès (CépiDc-Inserm)&nbsp;: taux de décès par suicide des 20-24&nbsp;ans résidant en France, par sexe, moyennes 2018-2019 et 2021-2023 (2018&nbsp;: nouveau certificat de décès)&nbsp;; décès de jeunes femmes de 20 à 24&nbsp;ans survenus en France, 2023 et 2024. «&nbsp;Sans nouvelle hausse établie&nbsp;»&nbsp;: l'écart entre 2023 et 2024 reste inférieur à deux fois l'écart type d'une différence de deux comptages.

**Dépense par étudiant.** Insee, [«&nbsp;Dépenses d'éducation&nbsp;»](https://www.insee.fr/fr/statistiques/8612572), d'après le compte de l'éducation de la Depp&nbsp;: dépense moyenne par étudiant du supérieur en euros constants de 2024, et par filière en 2024. Le site du SIES, qui publie la même série, était indisponible lors de la relecture.

**Composition.** Eurostat, effectifs inscrits dans l'enseignement supérieur et population, 18-24&nbsp;ans, par sexe&nbsp;: part des femmes parmi les étudiants et parmi les non-étudiants. Simulation&nbsp;: l'écart de hausse qu'aurait produit la seule composition par sexe si étudiants et non-étudiants du même sexe avaient connu la même évolution. Il se calcule comme la différence, entre 2021 et 2017, de (f<sub>E</sub>&nbsp;−&nbsp;f<sub>N</sub>)&nbsp;×&nbsp;(p<sub>F</sub>&nbsp;−&nbsp;p<sub>H</sub>), où f est la part des femmes parmi les étudiants (E) et les non-étudiants (N), et p la part des femmes (F) et des hommes (H) de 18 à 24&nbsp;ans déclarant un épisode dépressif&nbsp;; l'élargissement de l'écart de composition entre donc dans le calcul. Selon le champ et l'alignement des années, le résultat va de {{< etu-val "comp_min" >}} à {{< etu-val "comp_max" >}}&nbsp;point.

**Études citées.** CONFINS (*BMJ Open*, 2021), enquête en ligne pendant le premier confinement (questionnaire PHQ-9), sans représentativité nationale&nbsp;; Observatoire national du suicide, 6<sup>e</sup>&nbsp;rapport (février 2025)&nbsp;; étude SMART Schools (2025), sur les politiques scolaires de restriction du téléphone.

Les chiffres de cette page sont de trois sortes. La plupart sont **lus par un script** dans les données publiées (DREES, Assurance maladie, Eurostat, Insee), dont les extractions sont archivées avec leurs empreintes&nbsp;; les taux de la DREES sont recalculés par le script qui produit les données de la page. Ceux de Santé publique France sont **transcrits** des bulletins et vérifiés, lors de l'extraction, par la présence de leur phrase dans le document archivé, sauf les niveaux des étudiants en 2010 et 2017, lus sur une figure du bulletin (celui de 2017 contrôlé par l'écart que le bulletin publie). Le rapport de cotes de CONFINS est **cité**. Le script qui produit les données de la page s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases.

{{< reutiliser figures="figures_etudiants" jeu="malaise_etudiant" sources="Santé publique France, DREES, Assurance maladie, Eurostat et CépiDc-Inserm, Insee et Depp" donnees="Épisode dépressif déclaré par situation professionnelle et chez les 18-24 ans par sexe, patients hospitalisés pour geste auto-infligé par âge et par sexe depuis 2012, traitements antidépresseurs des 20-24 ans, suicides des 20-24 ans, risque de dépression des lycéens, dépense par étudiant, composition par sexe des 18-24 ans ; le même contenu existe en CSV, au format long." >}}
De 2017 à 2021, la dépression déclarée a augmenté chez les étudiants plus que dans toute autre situation professionnelle publiée. Des indicateurs non déclaratifs confirment une dégradation chez les jeunes, qui touche d'abord les jeunes femmes, commence au milieu des années 2010 et apparaît dès le lycée. La comparaison avec les jeunes non étudiants du même âge et du même sexe, qui dirait ce que les études ajoutent, n'est pas publiée.
{{< /reutiliser >}}
