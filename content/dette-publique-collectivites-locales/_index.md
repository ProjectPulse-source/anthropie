---
title: "Les collectivités locales sont-elles une variable d'ajustement des finances publiques ?"
description: "Depuis {coll.an_dette_deb}, la dette des collectivités est passée de {coll.dette_loc_deb} % à {coll.dette_loc_fin} % du PIB pendant que la dette publique doublait presque. Mais de {coll.ep_a0} à {coll.ep_a1}, la baisse des dotations a coïncidé avec un recul de leur investissement. Comptes Eurostat et OFGL, par catégorie, comparés à l'Allemagne, l'Italie et l'Espagne."
chapo: "Les comptes ne permettent pas d'en faire une règle générale : depuis {coll.an_dette_deb}, la dette publique française est passée de {coll.dette_apu_deb} % à {coll.dette_apu_fin} % du PIB, celle des collectivités de {coll.dette_loc_deb} % à {coll.dette_loc_fin} % seulement. Mais de {coll.ep_a0} à {coll.ep_a1}, la baisse des concours de l'État a coïncidé avec un redressement du solde local passé surtout par la baisse des dépenses, notamment d'équipement. Les comptes montrent où l'ajustement apparaît ; ils n'établissent pas, seuls, ce qui l'a causé."
date: 2026-07-24
lastmod: 2026-10-02
# Refonte du 01/10/2026 en ressource de données, sur la matrice du dossier dette (prolongement de « Qui paie »).
# Thèse de l'auteur mise à l'épreuve de ses propres données ; trois tours de raisonnement et trois de faits arbitrés :
# D:\PRO\.claude\external-audits\ARBITRATIONS\ (ENTRANTE_2026-10-01_Collectivites, PRO-20261001-145721, -152012, -153529).
# Public premier : les acteurs des collectivités (consigne de l'auteur, 01/10/2026). Aucun chiffre saisi : jetons {coll.*}
# et shortcodes coll-val / coll-tableau, depuis data/dette_collectivites.json (scripts/update_dette_collectivites.py).
og_title: "Dette publique : les collectivités locales sont-elles une variable d'ajustement ? — S. Lalut"
og_image: "images/og-collectivites.jpg"
og_image_alt: "Carte de partage : « L'ajustement local, hors de la dette » — investissement des collectivités et transferts reçus, France, en % du PIB, avec la baisse des dotations de 2014-2017."
donnees: [dette_collectivites]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_collectivites"
  nom: "Collectivités locales et finances publiques : dette, investissement, transferts et comptes par catégorie, France, Allemagne, Italie, Espagne"
  description: "Compilation dérivée automatiquement des sources officielles, sans valeur recopiée à la main : comptes des administrations locales (Eurostat, S1313) et territoriales (S1312 + S1313) de 1995 à {coll.an_fin}, dette par secteur détenteur, comptes de gestion consolidés par catégorie de collectivités (OFGL, 2018-{coll.of_an}), montant de la DGF fixé par la loi de finances 2013-2017 (CGCT, art. L. 1613-1). Identité vérifiée chaque année : recettes − dépenses = solde publié."
  couverture_temporelle: "1995/{coll.an_fin}"
  couverture_spatiale: "France, Allemagne, Italie, Espagne"
  variables:
    - {nom: "Dette des administrations locales et territoriales", unite: "% du PIB", description: "S1313, et S1312 + S1313 là où un échelon d'États fédérés existe ; 4e trimestre"}
    - {nom: "Part de la dette territoriale détenue par l'État central", unite: "% du PIB", description: "gov_10dd_ggd, secteur détenteur S1311, publiée depuis 2020"}
    - {nom: "Investissement et transferts reçus des collectivités", unite: "% du PIB", description: "P51G et D73REC, administrations locales, France"}
    - {nom: "Épargne brute, dépenses d'équipement, encours de dette, concours de l'État", unite: "milliards d'euros", description: "OFGL, bases consolidées des communes, intercommunalités, départements et régions"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10q_ggdebt/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_ggd/default/table?lang=fr"
    - "https://data.ofgl.fr/"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033810587"
  mots: ["collectivités locales", "finances locales", "dette publique", "DGF", "épargne brute", "investissement local", "Eurostat", "OFGL"]
  fichiers: ["dette_collectivites.csv", "dette_collectivites.json"]
faq:
  - question: "Les collectivités locales sont-elles la variable d'ajustement du budget de l'État ?"
    answer: "Les comptes ne permettent pas d'en faire une règle générale : depuis {coll.an_dette_deb}, leur dette est passée de {coll.dette_loc_deb} % à {coll.dette_loc_fin} % du PIB pendant que la dette publique passait de {coll.dette_apu_deb} % à {coll.dette_apu_fin} % (Eurostat). Mais de {coll.ep_a0} à {coll.ep_a1}, quand l'État a réduit la dotation globale de fonctionnement de {coll.dgf_vote_13} à {coll.dgf_vote_17} milliards d'euros, leur solde s'est redressé surtout par la baisse de leurs dépenses, notamment d'investissement. Les comptes montrent par où l'ajustement est passé ; ils ne disent pas, seuls, ce qui l'a causé."
  - question: "Les collectivités locales sont-elles très endettées ?"
    answer: "Leur encours de dette représente environ {coll.part_loc_fin} % de la dette publique en {coll.an_dette_fin} ({coll.dette_loc_fin} % du PIB), contre {coll.part_loc_deb} % en {coll.an_dette_deb}, et réalisent pourtant {coll.part_inv_loc_fin} % de l'investissement public. La loi leur interdit d'emprunter pour financer leur fonctionnement (article L. 1612-4 du code général des collectivités territoriales) : elles n'empruntent que pour investir."
  - question: "La baisse des dotations a-t-elle fait baisser l'investissement local ?"
    answer: "Les deux ont coïncidé : de {coll.ep_a0} à {coll.ep_a1}, les transferts reçus par les collectivités ont reculé de {coll.ep_transf} point de PIB et leur investissement de {coll.ep_inv} point ({coll.ep_inv_md} milliards d'euros). L'investissement baisse toujours après des municipales, mais après celles de 2014 le recul a été {coll.creux_ratio} fois plus fort qu'au plus fort des mandats 2001, 2008 et 2020. Cette comparaison affaiblit l'explication par le seul calendrier électoral ; elle n'isole pas l'effet des dotations."
  - question: "Que demande le projet de loi de finances aux collectivités locales ?"
    answer: "Le projet de loi de finances pour {coll.plf_edition}, déposé le {coll.plf_depot}, ne baisse pas la dotation globale de fonctionnement : son montant nominal augmente de {coll.plf_dgf_hausse_courant_m} millions d'euros. La mise à contribution passe notamment par une contribution progressive prélevée sur les avances de fiscalité ({coll.plf_cpeb} milliards d'euros), la baisse du taux du fonds de compensation pour la TVA ({coll.plf_fctva} milliards), un écrêtement de la progression de la TVA affectée hors régions ({coll.plf_tva} milliard), la réduction de contributions de certains ministères ({coll.plf_ministeres} milliard) et l'étalement sur cinq ans du reversement des sommes mises en réserve en 2025 et 2026 ({coll.plf_dilico} milliard). Ces montants relèvent de mécanismes différents et ne s'additionnent pas ; ce sont ceux d'un projet, avant examen par le Parlement."
  - question: "Pourquoi l'épargne brute des départements a-t-elle chuté ?"
    answer: "Les comptes consolidés publiés par l'OFGL montrent l'épargne brute des départements passée de {coll.of_eb_dep_pic} milliards d'euros en {coll.of_eb_dep_apic} à {coll.of_eb_dep_min} en {coll.of_eb_dep_amin}, avant de remonter à {coll.of_eb_dep_fin} en {coll.of_an}. L'agrégat national des collectivités, quasi stable, ne le montre pas. Les causes (recettes de droits de mutation, allocations de solidarité) relèvent de séries que cette page ne porte pas."
  - question: "Les collectivités d'autres pays européens sont-elles plus endettées ?"
    answer: "À périmètre statistique comparable, la dette territoriale atteint {coll.es_dette_fin} % du PIB en Espagne et {coll.de_dette_fin} % en Allemagne, qui ont un échelon d'États fédérés, contre {coll.fr_dette_fin} % en France et {coll.it_dette_fin} % en Italie. Mais en Espagne, {coll.es_part_etat_pct} % de cette dette est détenue par l'État central lui-même : porter une dette et la financer sont deux choses distinctes."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 30
  nature: "Séries officielles (Eurostat, OFGL) et calculs de l'auteur"
  prolongement: true   # option B : rangée « Prolongements du dossier », sous la grille des quatre volets
dossier_dette: prolongement   # panneau « Prolongements » de la barre du dossier (A+ v2, 03/10/2026)
dossier_dette_titre: "Les collectivités locales, variable d'ajustement ?"
dossier_dette_role: "dette, dotations, investissement local"
dossier_dette_titre_en: "Local authorities: the adjustment variable?"
dossier_dette_role_en: "debt, grants, local investment"
---

{{< dossier-dette volet="collectivites" >}}

{{< reutiliser-ancre >}}

À la question **«&nbsp;les collectivités locales sont-elles la variable d'ajustement des finances publiques&nbsp;?&nbsp;»**, les comptes donnent deux réponses, et il faut les deux. **Dans la durée, les comptes ne le montrent pas&nbsp;:** depuis {{< coll-val "an_dette_deb" >}}, la dette publique française est passée de {{< coll-val "dette_apu_deb" >}}&nbsp;% à {{< coll-val "dette_apu_fin" >}}&nbsp;% du PIB, celle des collectivités de {{< coll-val "dette_loc_deb" >}}&nbsp;% à {{< coll-val "dette_loc_fin" >}}&nbsp;% seulement. **Par épisodes, l'ajustement apparaît ailleurs que dans la dette&nbsp;:** de {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}, la baisse des concours de l'État a coïncidé avec un net recul de l'investissement local.

{{< figure-svg fichier="collectivites-investissement" alt="Deux courbes en pourcentage du PIB depuis 1995 : l'investissement des collectivités, assez stable, se creuse nettement après 2014 ; les transferts qu'elles reçoivent baissent de 2013 à 2017, après un pic ponctuel en 2010." >}}Investissement des administrations locales et transferts courants qu'elles reçoivent des autres administrations publiques, en % du PIB. Le pic de 2010 est ponctuel&nbsp;: l'État compense cette année-là la suppression de la taxe professionnelle, réforme «&nbsp;neutre sur le solde des administrations publiques locales&nbsp;» selon l'Insee (mai 2011). La série comparable des transferts s'arrête en 2017.{{< /figure-svg >}}

{{< fig-actions id="investissement" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Entre {{< coll-val "ep_a0" >}} et {{< coll-val "ep_a1" >}}, l'amélioration de {{< coll-val "ep_solde_delta" >}}&nbsp;point de PIB du solde des collectivités s'observe surtout du côté des dépenses&nbsp;: elles diminuent de {{< coll-val "ep_te" >}}&nbsp;point, dont {{< coll-val "ep_inv" >}}&nbsp;point d'investissement, pendant que les transferts reçus reculent de {{< coll-val "ep_transf" >}}&nbsp;point et que la dette locale varie peu.

</div>

<details class="repli"><summary>Lire ces chiffres avec ses propres comptes&nbsp;: la table de passage entre comptes de gestion et comptabilité nationale</summary>

Cette page s'appuie sur deux sources qui ne parlent pas la même langue. Eurostat publie la comptabilité nationale, harmonisée en Europe&nbsp;; l'Observatoire des finances et de la gestion publique locales (OFGL) publie les agrégats des comptes de gestion, ceux que lisent les directions financières. Les grandeurs se correspondent, sans être identiques.

| Ce que lit une direction financière (OFGL) | Ce que publie Eurostat | Ce qui les sépare |
|---|---|---|
| Dotation globale de fonctionnement, concours financiers de l'État | Transferts courants reçus des autres administrations publiques (D73) | Eurostat inclut les transferts de la sécurité sociale&nbsp;; une dotation remplacée par une fraction de TVA passe dans les impôts. |
| Dépenses d'équipement | Formation brute de capital fixe (P51G) | Les subventions d'équipement versées sont des transferts en capital, hors P51G. |
| Capacité ou besoin de financement | Capacité (+) ou besoin (−) de financement (B9) | Même notion&nbsp;; dates d'enregistrement et périmètres diffèrent. |
| Épargne brute | Épargne brute (B8G) | Notions voisines, retraitements différents. |
| Encours de dette | Dette au sens de Maastricht | Valeur nominale&nbsp;; pour les administrations locales, consolidée à l'intérieur du sous-secteur, non entre sous-secteurs. |

Les deux sources ne couvrent pas non plus le même champ. La somme des encours de dette des quatre catégories suivies par l'OFGL ({{< coll-val "of_encours_total" >}}&nbsp;milliards d'euros en {{< coll-val "of_an" >}}) reste inférieure d'environ {{< coll-val "of_ecart_maastricht" >}}&nbsp;milliards à la dette des administrations locales au sens de Maastricht ({{< coll-val "dette_loc_md" >}}&nbsp;milliards, Eurostat)&nbsp;: celle-ci comprend aussi les syndicats intercommunaux et les organismes divers d'administration locale, dont Île-de-France Mobilités et la Société des grands projets (Insee), et suit d'autres conventions. Elle n'est pas non plus consolidée avec l'État&nbsp;: la part que celui-ci en détient ({{< coll-val "fr_detenu_etat" >}}&nbsp;point de PIB) y reste comptée, ce qui la distingue de la «&nbsp;contribution&nbsp;» des administrations locales à la dette publique consolidée que publie l'Insee. L'écart se documente&nbsp;; il ne se corrige pas.

</details>

<span id="le-paradoxe-apparent-peu-endettées-très-contraintes"></span>

## Peu endettées, grandes investisseuses {#peu-endettees}

L'encours de dette des administrations locales représente moins d'un dixième de la dette publique&nbsp;: {{< coll-val "part_loc_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}, contre {{< coll-val "part_loc_deb" >}}&nbsp;% en {{< coll-val "an_dette_deb" >}}. Sur les {{< coll-val "delta_apu" >}}&nbsp;points de PIB de dette publique accumulés depuis {{< coll-val "an_dette_deb" >}}, elles en ont ajouté {{< coll-val "delta_loc" >}}, soit {{< coll-val "part_hausse_loc" >}}&nbsp;% de la hausse. Elles réalisent pourtant {{< coll-val "part_inv_loc_fin" >}}&nbsp;% de l'investissement public ({{< coll-val "inv_loc_fin" >}}&nbsp;% du PIB en {{< coll-val "an_fin" >}}).

Cette asymétrie s'explique en partie par les règles budgétaires locales, à côté du partage des compétences et des recettes. La loi impose l'équilibre réel du budget, section de fonctionnement comprise, et exclut l'emprunt des ressources qui remboursent le capital des emprunts (article L.&nbsp;1612-4 du code général des collectivités territoriales). **Une baisse durable des ressources courantes ne peut donc pas être simplement reportée sur l'emprunt&nbsp;: elle finit par peser sur les recettes propres, les dépenses courantes, l'épargne brute ou l'investissement.**

## Deux récits, une même série {#deux-recits}

L'Association des maires de France, en réponse à la Cour des comptes (juin 2025)&nbsp;: «&nbsp;Considérer les collectivités locales comme la variable d'ajustement des erreurs de stratégie de l'exécutif ne fait que creuser le déficit public.&nbsp;» La Cour des comptes (septembre 2025), «&nbsp;sans se prononcer en opportunité sur son montant&nbsp;», appelle à «&nbsp;organiser dans la durée la participation des collectivités au redressement des finances publiques&nbsp;».

La même série donne un appui à chaque lecture. La dépense des administrations locales est passée de {{< coll-val "te_0" >}}&nbsp;% du PIB en {{< coll-val "te_a0" >}} à {{< coll-val "te_pic" >}}&nbsp;% en {{< coll-val "te_apic" >}}&nbsp;: c'est l'argument d'une participation des collectivités à l'effort. Elle est revenue à {{< coll-val "te_fin" >}}&nbsp;% en {{< coll-val "an_fin" >}}, après l'épisode {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}&nbsp;: c'est l'argument de collectivités déjà mises à contribution. Aucune des deux lectures ne suffit seule&nbsp;; la question utile est de savoir quand, et par quel poste, l'ajustement a eu lieu.

## {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}&nbsp;: la baisse des dotations dans les comptes {#baisse-des-dotations}

Pendant ces quatre années, l'État a réduit sa dotation globale de fonctionnement au titre de la «&nbsp;contribution au redressement des finances publiques&nbsp;». Le montant de la DGF fixé chaque année par la loi de finances passe de {{< coll-val "dgf_vote_13" >}}&nbsp;milliards d'euros en 2013 à {{< coll-val "dgf_vote_17" >}} en 2017 (article L.&nbsp;1613-1 du CGCT)&nbsp;: −{{< coll-val "dgf_vote_b14" >}} en 2014, −{{< coll-val "dgf_vote_b15" >}} en 2015, −{{< coll-val "dgf_vote_b16" >}} en 2016, −{{< coll-val "dgf_vote_b17" >}} en 2017, soit {{< coll-val "dgf_vote_baisse" >}}&nbsp;milliards de moins en quatre ans. Ce montant voté n'est ni la contribution demandée à chaque catégorie, ni la DGF que chaque collectivité a effectivement inscrite dans ses comptes&nbsp;: trois mesures voisines, qui ne s'additionnent pas. Les comptes de gestion montrent la troisième par catégorie&nbsp;: la DGF des départements passe de {{< coll-val "of_dgf_dep_13" >}} à {{< coll-val "of_dgf_dep_17" >}}&nbsp;milliards d'euros (−{{< coll-val "of_dgf_dep_baisse" >}}), celle des régions de {{< coll-val "of_dgf_reg_13" >}} à {{< coll-val "of_dgf_reg_17" >}}&nbsp;milliards (−{{< coll-val "of_dgf_reg_baisse" >}}). La comptabilité nationale mesure, elle, l'ensemble des transferts reçus des autres administrations publiques, État et sécurité sociale compris&nbsp;: −{{< coll-val "ep_transf" >}}&nbsp;point de PIB, soit {{< coll-val "ep_transf_md" >}}&nbsp;milliards d'euros de moins en {{< coll-val "ep_a1" >}} qu'en {{< coll-val "ep_a0" >}}.

{{< figure-svg fichier="collectivites-cascade" alt="Cascade en points de PIB, de 2013 à 2017 : partant d'un léger déficit, la baisse des transferts creuse le solde, la hausse des impôts et la baisse des dépenses, surtout d'investissement, le remontent jusqu'à un léger excédent." >}}Variation des recettes et des dépenses des administrations locales entre {{< coll-val "ep_a0" >}} et {{< coll-val "ep_a1" >}}, en points de PIB. Les cinq postes reconstituent exactement la variation du solde.{{< /figure-svg >}}

{{< fig-actions id="cascade" >}}

Les impôts compensent une partie de la baisse des transferts (+{{< coll-val "ep_imp" >}}&nbsp;point) et les autres recettes reculent encore ({{< coll-val "ep_autres_rec" >}}&nbsp;point). Le solde s'améliore pourtant de {{< coll-val "ep_solde_delta" >}}&nbsp;point&nbsp;: les dépenses reculent de {{< coll-val "ep_te" >}}&nbsp;point, dont {{< coll-val "ep_inv" >}} pour l'investissement — {{< coll-val "ep_inv_md" >}}&nbsp;milliards d'euros d'équipement en moins en {{< coll-val "ep_a1" >}} qu'en {{< coll-val "ep_a0" >}} — et {{< coll-val "ep_autres_dep" >}} pour le reste. C'est la dernière période où la série des transferts reste comparable avant les changements de 2018 et 2021.

**La comparaison ne permet pas de ramener l'ampleur du creux au seul cycle municipal.** L'investissement local baisse habituellement après les municipales, et l'Insee rattache le recul de 2014 «&nbsp;à la suite des élections municipales&nbsp;» puis celui de 2015 «&nbsp;notamment&nbsp;» au cycle électoral communal, en notant cette année-là l'effet de «&nbsp;la baisse des transferts de l'État&nbsp;». Mais après les élections de 2001, 2008 et 2020, le recul n'a jamais dépassé {{< coll-val "creux_autres_max" >}}&nbsp;point de PIB&nbsp;; après celles de 2014, il atteint {{< coll-val "creux14_baisse" >}}&nbsp;point en {{< coll-val "creux14_annee" >}}, {{< coll-val "creux_ratio" >}}&nbsp;fois plus, pendant que les concours de l'État diminuent. La comparaison affaiblit l'explication par le seul calendrier électoral&nbsp;; elle n'isole pas l'effet des dotations, d'autant que les départements et les régions, compris dans l'agrégat, ne suivent pas ce cycle.

<details class="repli"><summary>Le témoin du cycle électoral, mandat par mandat, et le témoin comptable de la cascade</summary>

{{< coll-tableau "cycles" >}}

Les quatre épisodes ne sont pas identiques&nbsp;: 2008 précède la crise financière, 2020 est l'année de la pandémie. Isoler l'effet des dotations demanderait de comparer, collectivité par collectivité, les plus et les moins exposées à leur baisse, avant et après 2014.

La cascade se vérifie par une identité que le générateur contrôle à chaque passage&nbsp;: recettes totales moins dépenses totales égalent le solde publié par Eurostat. Sur les {{< coll-val "temoin_annees" >}}&nbsp;années disponibles, l'écart maximal est de {{< coll-val "temoin_residu" >}}&nbsp;million d'euros, un arrondi.

</details>

## Par catégorie de collectivités&nbsp;: ce que l'agrégat cache {#par-categorie}

L'agrégat national additionne des collectivités dont les recettes et les charges n'ont rien de commun. Depuis 2018, les comptes de gestion consolidés publiés par l'OFGL permettent de les séparer. Deux mouvements y apparaissent, invisibles dans l'agrégat&nbsp;: l'épargne brute des départements tombe de {{< coll-val "of_eb_dep_pic" >}}&nbsp;milliards d'euros en {{< coll-val "of_eb_dep_apic" >}} à {{< coll-val "of_eb_dep_min" >}} en {{< coll-val "of_eb_dep_amin" >}}, avant de remonter à {{< coll-val "of_eb_dep_fin" >}} en {{< coll-val "of_an" >}}&nbsp;; les dépenses d'équipement des communes passent de {{< coll-val "of_eq_com_20" >}}&nbsp;milliards en 2020 à {{< coll-val "of_eq_com_fin" >}} en {{< coll-val "of_an" >}} (+{{< coll-val "of_eq_com_hausse_pct" >}}&nbsp;%), à l'approche des municipales de 2026.

{{< coll-tableau "categories" >}}

## 2018 et 2021&nbsp;: quand une ressource change de case {#ruptures}

En 2018, la DGF des régions passe de {{< coll-val "of_dgf_reg_17" >}} à {{< coll-val "of_dgf_reg_18" >}}&nbsp;milliard d'euros pendant qu'elles reçoivent {{< coll-val "of_tva_reg_18" >}}&nbsp;milliards de TVA (OFGL). En 2021, les transferts reçus par l'ensemble des collectivités chutent de {{< coll-val "rupt_transf" >}}&nbsp;point de PIB et leurs impôts montent de {{< coll-val "rupt_imp" >}}&nbsp;point&nbsp;: la suppression de la taxe d'habitation sur les résidences principales est compensée par une fraction de TVA aux intercommunalités et aux départements, les communes recevant la part départementale de taxe foncière (loi de finances pour 2020, article&nbsp;16)&nbsp;; la suppression de la part régionale de CVAE, par une fraction de TVA aux régions (loi de finances pour 2021, article&nbsp;8)&nbsp;; la réduction des valeurs locatives des établissements industriels, par un prélèvement sur les recettes de l'État (même loi, article&nbsp;29). En 2018, une recette classée parmi les transferts devient une recette fiscale. En 2021, plusieurs impôts supprimés ou réduits sont compensés soit par d'autres recettes fiscales, notamment la TVA, soit par un prélèvement sur les recettes de l'État. Une série limitée aux seules dotations ne mesure donc pas, à elle seule, l'évolution des ressources.

## Depuis 2023&nbsp;: la dette locale remonte {#depuis-2023}

Depuis {{< coll-val "recent_a0" >}}, les collectivités sont de nouveau en besoin de financement ({{< coll-val "recent_solde_fin" >}}&nbsp;point de PIB en {{< coll-val "an_fin" >}}), leur investissement remonte de {{< coll-val "recent_inv_deb" >}}&nbsp;% à {{< coll-val "inv_loc_fin" >}}&nbsp;% du PIB, et le stock de leur dette passe de {{< coll-val "recent_dette_deb" >}}&nbsp;% à {{< coll-val "dette_loc_fin" >}}&nbsp;% du PIB&nbsp;: c'est l'inverse du schéma de {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}. Le dispositif de lissage conjoncturel des recettes fiscales (DILICO) a prélevé en 2025 {{< coll-val "dilico_2025" >}} sur les ressources fiscales des collectivités, mis en réserve et reversés par tiers les trois années suivantes — 90&nbsp;% aux collectivités contributrices, 10&nbsp;% aux fonds de péréquation (loi de finances pour 2025, article&nbsp;186)&nbsp;; il est reconduit en 2026 (loi de finances pour 2026). Ni l'Insee ni Eurostat ne documentent son enregistrement en comptabilité nationale&nbsp;: son effet propre ne s'isole pas dans ces séries.

## Que demande le projet de loi de finances aux collectivités&nbsp;? {#projet-de-loi-de-finances}

Le projet de loi de finances pour {{< coll-val "plf_edition" >}}, déposé le {{< coll-val "plf_depot" >}}, prévoit {{< coll-val "plf_dgf_hausse_m" >}}&nbsp;millions d'euros d'abondements nouveaux de la dotation globale de fonctionnement&nbsp;; compte tenu des mesures de périmètre, son montant nominal augmente de {{< coll-val "plf_dgf_hausse_courant_m" >}}&nbsp;millions d'euros, à {{< coll-val "plf_dgf" >}}&nbsp;milliards. La mise à contribution ne passe donc pas par une baisse de la DGF&nbsp;: elle passe notamment par cinq canaux chiffrés ci-dessous, qui portent sur les avances de fiscalité, le fonds de compensation pour la TVA, la progression de la TVA affectée et certains concours de l'État.

{{< coll-tableau "plf" >}}

Le Haut Conseil des finances publiques réunit ces mesures dans un même paquet de modération des recettes des collectivités. Leurs montants ne sont pas additionnés ici&nbsp;: ils correspondent à des mécanismes et à des bases de comparaison différents. Pour les régions s'ajoute la suppression d'une fraction d'accises sur les énergies de {{< coll-val "plf_regions_m" >}}&nbsp;millions d'euros (article&nbsp;39). Dans le budget de l'État, les prélèvements sur recettes au profit des collectivités sont évalués à {{< coll-val "plf_psr" >}}&nbsp;milliards d'euros pour {{< coll-val "plf_edition" >}}, contre {{< coll-val "plf_psr_rev_prec" >}}&nbsp;milliards dans la prévision révisée pour {{< coll-val "plf_prec" >}} ({{< coll-val "plf_psr_lfi_prec" >}}&nbsp;milliards dans la loi de finances initiale, article&nbsp;41). Une série limitée aux dotations ne verrait pas ces canaux, pour la raison déjà rencontrée [en 2018 et en 2021](#ruptures).

La contribution progressive s'applique à {{< coll-val "plf_cpeb_communes_pct" >}}&nbsp;% des communes, à {{< coll-val "plf_cpeb_dep_pct" >}}&nbsp;% des départements et aux intercommunalités de métropole, à un taux qui croît avec leurs ressources&nbsp;; les collectivités d'outre-mer et les départements les plus fragiles socialement en sont exonérés (article&nbsp;37). Ces montants nationaux ne permettent pas d'estimer l'effet pour une collectivité donnée&nbsp;: pour la contribution progressive, l'assujettissement et le taux dépendent de la strate et des indicateurs prévus à l'article&nbsp;37&nbsp;; pour le fonds de compensation, l'effet dépend de la composition des dépenses éligibles&nbsp;; la modulation de la TVA ne concerne pas les régions.

Les documents budgétaires décrivent deux dimensions distinctes du scénario. Le Gouvernement indique qu'après les mesures de mise à contribution les collectivités disposeraient en {{< coll-val "plf_edition" >}} de {{< coll-val "plf_ressources_md" >}}&nbsp;milliards d'euros de ressources supplémentaires par rapport à {{< coll-val "plf_prec" >}} (+{{< coll-val "plf_ressources_pct" >}}&nbsp;%). Le Haut Conseil prévoit parallèlement un recul de leur investissement de {{< coll-val "plf_inv_n1_pct" >}}&nbsp;%, après {{< coll-val "plf_inv_n_pct" >}}&nbsp;% en {{< coll-val "plf_prec" >}}, et juge cette baisse vraisemblable au regard de la position de {{< coll-val "plf_edition" >}} dans le cycle électoral communal, une année après les élections, ainsi que de la réforme du fonds de compensation. Ces deux chiffres portent sur des grandeurs différentes. Cette page mesure ce qu'un recul de l'investissement a représenté [de {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}](#baisse-des-dotations)&nbsp;; elle ne dit pas s'il se reproduira, et ces montants sont ceux d'un projet, que le Parlement peut modifier. Textes&nbsp;: [projet de loi de finances pour {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf), articles 34 à 41 et 84&nbsp;; [avis du Haut Conseil des finances publiques](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf).

## Ailleurs en Europe&nbsp;: une même dette, des architectures opposées {#ailleurs-en-europe}

Les comparaisons se font ici par périmètre statistique, non par compétences exercées. Le sous-secteur des administrations d'États fédérés (S1312) n'existe, dans les données Eurostat, que dans quelques pays, dont l'Allemagne et l'Espagne&nbsp;; les régions françaises et italiennes sont classées parmi les administrations locales (S1313), et ces deux pays forment la comparaison principale. L'Allemagne et l'Espagne, avec leurs Länder et leurs communautés autonomes, servent de contrepoints. Leur dette territoriale additionne les deux échelons&nbsp;; les dettes croisées entre ces deux échelons représentent au plus {{< coll-val "consolidation_ecart" >}}&nbsp;point de PIB&nbsp;: le double compte est marginal et ne modifie pas les ordres de grandeur.

{{< figure-svg fichier="collectivites-europe" alt="Quatre petits graphiques en pourcentage du PIB : la dette territoriale française monte doucement, l'allemande reste haute, portée par les Länder, l'italienne monte puis redescend, l'espagnole fait plus que doubler ; en Espagne, plus de la moitié en est détenue par l'État central." >}}Dette des administrations territoriales en % du PIB, quatrième trimestre de chaque année, et part détenue par l'administration centrale, publiée depuis 2020.{{< /figure-svg >}}

{{< fig-actions id="europe" >}}

**En Italie**, les trois indicateurs vont dans le même sens sur la période&nbsp;: la dette territoriale redescend de {{< coll-val "it_dette_pic" >}}&nbsp;% du PIB en {{< coll-val "it_dette_pic_annee" >}} à {{< coll-val "it_dette_fin" >}}&nbsp;%, le solde est excédentaire {{< coll-val "it_excedents" >}}&nbsp;années sur huit entre 2012 et 2019 (France&nbsp;: {{< coll-val "fr_excedents" >}}), l'investissement tombe à la moitié de son maximum des années 2000. Ces concomitances n'isolent pas l'effet des règles nationales — le pacte de stabilité interne, institué en 1999 et abandonné pour les collectivités locales en 2016 — de celui d'une crise bien plus profonde qu'en France.

**En Espagne**, la dette territoriale passe de {{< coll-val "es_dette_deb" >}}&nbsp;% à {{< coll-val "es_dette_fin" >}}&nbsp;% du PIB, portée par les communautés autonomes, pendant que l'investissement territorial perd {{< coll-val "es_inv_baisse_pct" >}}&nbsp;%. Mais cette dette ne mesure pas un report de contrainte vers le bas&nbsp;: en {{< coll-val "an_ggd" >}}, {{< coll-val "es_detenu_etat" >}}&nbsp;points de PIB sur {{< coll-val "es_detenu_total" >}}, soit {{< coll-val "es_part_etat_pct" >}}&nbsp;%, sont détenus par l'État central lui-même, notamment par le Fondo de Liquidez Autonómico, créé en 2012, par lequel l'État prête aux communautés autonomes (Real Decreto-ley 21/2012, articles&nbsp;9 et 14). La part équivalente est de {{< coll-val "it_part_etat_pct" >}}&nbsp;% en Italie, de {{< coll-val "fr_part_etat_pct" >}}&nbsp;% en France et de {{< coll-val "de_part_etat_pct" >}}&nbsp;% en Allemagne. La loi organique espagnole 2/2012 affecte en outre les excédents de chaque niveau d'administration à la réduction de son endettement net (article&nbsp;32). **Qui porte une dette et qui la finance sont deux questions distinctes.**

**En Allemagne**, la dette territoriale reste nettement sous son pic de {{< coll-val "de_dette_pic_annee" >}} ({{< coll-val "de_dette_pic" >}}&nbsp;%, {{< coll-val "de_dette_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}), avec un recul d'investissement limité ({{< coll-val "de_inv_baisse_pct" >}}&nbsp;%)&nbsp;; elle est portée surtout par les Länder.

<details class="repli"><summary>Les quatre pays, indicateur par indicateur</summary>

{{< coll-tableau "pays" >}}

</details>

<span id="ce-que-cette-lecture-change"></span>

La comparaison ne fait apparaître aucun classement unique&nbsp;: dette, solde et investissement ordonnent les quatre pays différemment. Elle montre qu'une contrainte de finances publiques peut circuler entre niveaux d'administration sous des formes opposées — baisse de dotation, recul d'investissement, dette, ou financement du niveau territorial par le centre.

<span id="les-trois-mécanismes-du-transfert"></span>

## Trois canaux, une hypothèse à tester {#trois-canaux}

1. **Les dotations réduites ou gelées.** Observées dans les comptes&nbsp;: c'est l'épisode {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}.
2. **Les compétences transférées sans financement complet.** Non mesurées ici&nbsp;: une compensation figée qui décroche du coût réel se lit compétence par compétence (allocations individuelles de solidarité des départements, par exemple), non dans un agrégat.
3. **Les normes non financées.** Non mesurées ici&nbsp;: le coût d'une norme se lit dans les évaluations préalables.

Ces trois mécanismes ont en commun une hypothèse à tester&nbsp;: une décision prise à un niveau peut déplacer une partie de son coût vers un autre. Seul le premier est observé ici&nbsp;; les deux autres exigent des données propres. Le working paper [AWP-09](/awp/awp-09/) confronte le premier à cet énoncé&nbsp;: sur l'épisode {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}, les comptes le rendent compatible, sans l'établir.

## Ce que ces données ne disent pas {#limites}

- L'agrégat national mêle communes, intercommunalités, départements et régions&nbsp;; les données par catégorie ne remontent qu'à 2018 pour les communes et les intercommunalités, et les périmètres des catégories changent au fil des réformes&nbsp;: la base consolidée des départements utilisée ici incorpore la métropole de Lyon (depuis 2015) et la Ville de Paris (depuis 2019), celle des régions les collectivités uniques de Guyane, de Martinique et de Corse — le rapport annuel de l'OFGL, lui, classe Lyon avec les intercommunalités et Paris avec les communes.
- Les transferts reçus comprennent ceux de la sécurité sociale, pas seulement de l'État.
- Une baisse d'investissement concomitante d'une baisse de dotations n'établit pas que la seconde a causé la première.
- Comptabilité nationale et comptes de gestion ne coïncident pas au million près&nbsp;: périmètres, dates d'enregistrement et retraitements diffèrent.
- Elles ne disent rien de la qualité des services rendus, ni de qui a finalement supporté l'ajustement.

<span id="et-au-bout-de-la-chaîne-une-hypothèse-sur-les-ménages-les-moins-mobiles"></span>

<details class="repli" id="qui-supporte"><summary>Hypothèse de recherche, non testée ici&nbsp;: qui supporte finalement l'ajustement&nbsp;?</summary>

Les comptes ne permettent pas de savoir si l'ajustement est finalement supporté par les contribuables, les usagers, les agents publics, les fournisseurs, les propriétaires fonciers ou les ménages qui dépendent des services locaux. Le cadre de l'[anthropie](/quest-ce-que-lanthropie/) formule l'hypothèse que certains coûts sont plus difficiles à éviter pour les ménages les moins mobiles&nbsp;: un ménage qui dépend du logement social, des transports publics et des équipements de proximité subit plus directement une hausse de tarif ou une fermeture qu'un ménage qui peut changer de commune. Cette page ne la teste pas&nbsp;; elle se vérifierait décision par décision, et serait affaiblie par des ajustements portant surtout sur les ménages aisés ou compensés par des tarifs sociaux.

</details>

## Questions fréquentes {#questions-fréquentes}

{{< faq-visible >}}

<span id="pour-aller-plus-loin"></span>

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)
- [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Dette publique&nbsp;: pourquoi 100&nbsp;% du PIB ne pèse pas partout de la même façon](/dette-publique-comparaison-internationale/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Prolonger l'analyse" avis="non" >}}
Cette page montre par où passe l'ajustement des finances locales&nbsp;; elle ne dit pas qui, au bout de la chaîne, en supporte le coût. Le livre suit ce déplacement canal par canal — contribuable, usager, services publics, générations qui ne votent pas encore —, chiffres officiels à l'appui. L'analyse est aussi développée dans deux articles de l'auteur, [«&nbsp;La commune, variable d'ajustement de la République&nbsp;?&nbsp;»](https://www.revue-projet.com/articles/2026-07-lalut-variable-d-ajustement-de-la-republique/11589) (*Revue Projet*, 2026) et [«&nbsp;Budget 2026&nbsp;: la dette commande, les territoires patientent&nbsp;»](https://blogs.mediapart.fr/stephane-lalut/blog/150126/budget-2026-la-dette-commande-les-territoires-patientent) (*Mediapart*, 2026).
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Comptabilité nationale** — Eurostat, administrations publiques par sous-secteur, SEC 2010&nbsp;: comptes annuels (`gov_10a_main`&nbsp;: formation brute de capital fixe P51G, transferts courants reçus D73REC, impôts D2, D5 et D91, recettes TR, dépenses TE, solde B9), dette trimestrielle (`gov_10q_ggdebt`), dette par secteur détenteur (`gov_10dd_ggd`), PIB des comptes nationaux en témoin du dénominateur (`nama_10_gdp`).

**Comptes de gestion** — OFGL, bases consolidées des communes, des intercommunalités, des départements et des régions (data.ofgl.fr, données DGFiP).

**Textes** — code général des collectivités territoriales, articles L.&nbsp;1612-4 et L.&nbsp;1613-1&nbsp;; lois de finances pour 2020 (art.&nbsp;16), 2021 (art.&nbsp;8 et 29), 2025 (art.&nbsp;186) et 2026&nbsp;; projet de loi de finances déposé le {{< coll-val "plf_depot" >}} et avis du Haut Conseil des finances publiques sur ce projet, lus dans le texte et archivés avec leur empreinte&nbsp;; Real Decreto-ley 21/2012 et loi organique 2/2012 (Espagne)&nbsp;; loi n°&nbsp;448/1998, art.&nbsp;28, et loi n°&nbsp;208/2015 (Italie, pacte de stabilité interne puis règle d'équilibre)&nbsp;; Insee, *Les comptes des administrations publiques* en 2010, 2014 et 2015&nbsp;; Cour des comptes, *Les finances publiques locales 2025* et réponses publiées.

Les calculs, les gardes et les figures sont produits par un script unique, relancé à chaque publication des sources&nbsp;; aucun chiffre de cette page n'est saisi à la main, et le script refuse d'écrire si une donnée cesse de soutenir une phrase. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/dette_collectivites.csv), en format long, lisible dans un tableur&nbsp;; [JSON](/dette_collectivites.json), avec les calculs, les définitions et le compte rendu des gardes.

{{< reutiliser figures="figures_collectivites" jeu="dette_collectivites" sources="Eurostat, OFGL et Légifrance" donnees="Les séries par pays et par catégorie de collectivités, la DGF votée, les mesures du projet de loi de finances, la décomposition 2013-2017 et le compte rendu des contrôles ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Cette page vérifie une thèse courante sur les finances locales&nbsp;: dans la durée, l'endettement des collectivités françaises est resté contenu&nbsp;; de {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}, la baisse des concours de l'État a coïncidé avec un recul de leur investissement plus fort qu'après les autres municipales. Comparée à l'Allemagne, l'Italie et l'Espagne à périmètre statistique égal, la France ne se classe pas sur une échelle unique, et en Espagne la dette territoriale est pour plus de la moitié détenue par l'État central. Ces séries décrivent des concomitances, non des causes.
{{< /reutiliser >}}
