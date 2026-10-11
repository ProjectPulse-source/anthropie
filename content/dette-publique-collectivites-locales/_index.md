---
title: "Les collectivités locales sont-elles une variable d'ajustement des finances publiques ?"
description: "Leur dette ne permet pas de trancher. De {coll.ep_a0} à {coll.ep_a1}, les administrations locales améliorent leur solde de {coll.ep_solde_mde} : dépenses presque stables en euros, en recul de {coll.ep_te_pt} de PIB, impôts en hausse, transferts reçus en baisse. Comptes Eurostat et OFGL, contrats de Cahors, projet de loi de finances, comparaison avec l'Allemagne, l'Italie et l'Espagne."
chapo: "La dette des collectivités ne permet pas de trancher : la règle d'équilibre de leurs budgets leur interdit d'emprunter pour compenser une baisse durable des recettes qui financent leurs dépenses courantes, si bien qu'une contrainte venue de l'État se lit dans leurs recettes et leurs dépenses. De {coll.ep_a0} à {coll.ep_a1}, les administrations publiques locales ont amélioré leur solde de {coll.ep_solde_mde}. Leurs dépenses totales sont restées presque stables en euros courants, tandis que les recettes fiscales progressaient et que les transferts reçus reculaient. Rapportées au PIB, leurs dépenses ont diminué de {coll.ep_te_pt}, dont {coll.ep_inv_pt} pour l'investissement. Ces évolutions sont concomitantes ; elles ne permettent pas, à elles seules, d'attribuer le recul de l'investissement à la baisse des dotations."
date: 2026-07-24
lastmod: 2026-10-11
# Refonte du 01/10/2026 en ressource de données, sur la matrice du dossier dette (prolongement de « Qui paie ») ; refonte
# éditoriale du 11/10/2026 (architecture B+ : trois paradoxes, deux unités, mécanismes successifs, projet de loi en dernier),
# arbitrage D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_LECTURE_2026-10-09\REFONTE_PILOTE\COLLECTIVITES\ARBITRAGE_CE_COLLECTIVITES_PHASE_A.md.
# Public premier : les acteurs des collectivités (consigne de l'auteur, 01/10/2026). Aucun chiffre saisi : jetons {coll.*}
# et shortcodes coll-val / coll-tableau, depuis data/dette_collectivites.json (scripts/update_dette_collectivites.py, qui
# garde aussi la PROSE de cette page : attribution sur 2013-2017 sans ses deux unités, verdict tiré de la dette, somme du
# projet de loi présentée comme un effet démontré).
og_title: "Dette publique : les collectivités locales sont-elles une variable d'ajustement ? — S. Lalut"
og_image: "images/og-collectivites.jpg"
og_image_alt: "Carte de partage : « L'ajustement local, hors de la dette » — investissement des collectivités et transferts reçus, France, en % du PIB, avec la baisse des dotations de 2014-2017."
donnees: [dette_collectivites]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_collectivites"
  nom: "Collectivités locales et finances publiques : dette, investissement, transferts et comptes par catégorie, France, Allemagne, Italie, Espagne"
  description: "Compilation dérivée automatiquement des sources officielles, sans valeur recopiée à la main : comptes des administrations locales (Eurostat, S1313) et territoriales (S1312 + S1313) de 1995 à {coll.an_fin}, décomposition du solde {coll.ep_a0}-{coll.ep_a1} en milliards d'euros et en points de PIB, dette par secteur détenteur, comptes de gestion consolidés par catégorie de collectivités (OFGL, 2018-{coll.of_an}), montant de la DGF fixé par la loi de finances 2013-2017 (CGCT, art. L. 1613-1), mesures du projet de loi de finances. Identité vérifiée chaque année : recettes − dépenses = solde publié."
  couverture_temporelle: "1995/{coll.an_fin}"
  couverture_spatiale: "France, Allemagne, Italie, Espagne"
  variables:
    - {nom: "Dette des administrations locales et territoriales", unite: "% du PIB", description: "S1313, et S1312 + S1313 là où un échelon d'États fédérés existe ; 4e trimestre"}
    - {nom: "Part de la dette territoriale détenue par l'État central", unite: "% du PIB", description: "gov_10dd_ggd, secteur détenteur S1311, publiée depuis 2020"}
    - {nom: "Investissement et transferts reçus des administrations locales", unite: "% du PIB", description: "P51G et D73REC, administrations locales, France"}
    - {nom: "Décomposition de la variation du solde local, 2013-2017", unite: "milliards d'euros courants et points de PIB", description: "transferts reçus, impôts, autres recettes, investissement, autres dépenses ; contribution au solde"}
    - {nom: "Épargne brute, dépenses d'équipement, encours de dette, concours de l'État", unite: "milliards d'euros", description: "OFGL, bases consolidées des communes, intercommunalités, départements et régions"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10q_ggdebt/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_ggd/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://data.ofgl.fr/"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033810587"
    - "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051731697"
    - "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036526027"
  mots: ["collectivités locales", "finances locales", "dette publique", "DGF", "épargne brute", "investissement local", "contrats de Cahors", "Eurostat", "OFGL"]
  fichiers: ["dette_collectivites.csv", "dette_collectivites.json"]
faq:
  - question: "Comment savoir si ma collectivité est concernée par le projet de loi de finances ?"
    answer: "La contribution progressive vise {coll.plf_cpeb_communes_pct} % des communes, {coll.plf_cpeb_dep_pct} % des départements et les intercommunalités de métropole, selon les critères de l'article 37 du projet déposé le {coll.plf_depot} ; selon ce texte, le montant prélevé sur chaque collectivité sera fixé par un arrêté publié au Journal officiel. Les montants nationaux ne donnent aucun montant individuel."
  - question: "Comment interpréter la hausse de la fiscalité locale ?"
    answer: "De {coll.ep_a0} à {coll.ep_a1}, les impôts des administrations publiques locales augmentent de {coll.ep_imp_mde}, davantage que les transferts reçus ne baissent ({coll.ep_transf_mde}) ; rapportés au PIB, ils n'en compensent qu'une partie ({coll.ep_imp_pt} contre {coll.ep_transf_pt}). Depuis 2018, une partie des recettes fiscales provient d'un reclassement : des dotations ou des impôts supprimés sont remplacés par des fractions de TVA, et ce changement de classement ne dit pas, à lui seul, si les ressources disponibles augmentent ou baissent. Ces comptes ne séparent pas l'effet des taux votés de celui des bases."
  - question: "Pourquoi un recul de l'investissement ne signifie-t-il pas une baisse des dépenses totales ?"
    answer: "De {coll.ep_a0} à {coll.ep_a1}, l'investissement des administrations publiques locales recule de {coll.ep_inv_mde}, mais leurs autres dépenses augmentent de {coll.ep_autres_dep_mde} : leurs dépenses totales restent presque stables en euros ({coll.ep_te_mde_s}). Rapportées au PIB, qui augmente de {coll.pib_croiss_pct} % sur la période, elles reculent pourtant de {coll.ep_te_pt}. La baisse d'un ratio ne prouve pas une baisse de la dépense en euros."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # phase B de la refonte (méthode OPTIMUM-26) ; relecture attestée par docs/relectures/
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

**Projet de loi de finances pour {{< coll-val "plf_edition" >}}**&nbsp;: ce qu'il demande aux collectivités, mesure par mesure, et ce que la somme de ses montants ne dit pas → [dernière section de la page](#projet-de-loi-de-finances).

**Comment une contrainte peut-elle ne pas apparaître dans la dette&nbsp;?** La question du titre revient à demander si l'État, quand il resserre ses finances, reporte une part de l'effort sur les collectivités, et où cela se verrait. Trois paradoxes organisent cette page. La dette locale est restée contenue, de {{< coll-val "dette_loc_deb" >}}&nbsp;% du PIB en {{< coll-val "an_dette_deb" >}} à {{< coll-val "dette_loc_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}&nbsp;: cette observation ne dit pas, seule, si les collectivités ont supporté une contrainte. De {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}, leurs dépenses sont presque stables en euros et reculent nettement en part du PIB&nbsp;: deux lectures exactes, qui ne racontent pas la même histoire. En Espagne, l'État central détient plus de la moitié de la dette territoriale&nbsp;: porter une dette et la financer sont deux réalités distinctes.

{{< figure-svg fichier="collectivites-investissement" alt="Deux courbes en pourcentage du PIB depuis 1995 : l'investissement des administrations locales, assez stable, se creuse nettement après 2014 ; les transferts qu'elles reçoivent baissent de 2013 à 2017, où leur série comparable s'arrête, après un pic ponctuel en 2010." >}}Investissement des administrations publiques locales (formation brute de capital fixe) et transferts courants qu'elles reçoivent des autres administrations publiques, en % du PIB. Ces transferts comprennent ceux de la sécurité sociale&nbsp;: ce ne sont pas les seules dotations de l'État. Le pic de 2010 est ponctuel&nbsp;: l'État compense cette année-là la suppression de la taxe professionnelle, réforme «&nbsp;neutre sur le solde des administrations publiques locales&nbsp;» selon l'Insee (mai 2011). La série comparable des transferts s'arrête en 2017&nbsp;: en 2018 puis en 2021, des dotations sont remplacées par des fractions de TVA, comptées en impôts, un reclassement qui ne dit pas, à lui seul, si les ressources ont augmenté ou baissé ([détail](/dette-publique-collectivites-locales/#ruptures)).{{< /figure-svg >}}

{{< fig-actions id="investissement" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}, les transferts reçus par les administrations publiques locales reculent de {{< coll-val "ep_transf_mde" >}} ({{< coll-val "ep_transf_pt" >}} de PIB) et leur investissement de {{< coll-val "ep_inv_mde" >}} ({{< coll-val "ep_inv_pt" >}})&nbsp;; après les élections municipales de 2014, le recul de l'investissement est {{< coll-val "creux_ratio" >}}&nbsp;fois plus marqué que le plus fort des reculs qui ont suivi celles de 2001, 2008 et 2020.

</div>

Ces chiffres, comme tous les résultats statistiques de cette page, portent sur les **administrations publiques locales, au sens de la comptabilité nationale**&nbsp;: les collectivités territoriales, mais aussi les syndicats intercommunaux et d'autres organismes publics locaux.

<details class="repli"><summary>Périmètre exact, et table de passage entre comptes de gestion et comptabilité nationale</summary>

Ce périmètre est le sous-secteur S1313 des comptes nationaux&nbsp;; il comprend les organismes divers d'administration locale, dont Île-de-France Mobilités et la Société des grands projets (Insee). Sa dette ({{< coll-val "dette_loc_md" >}}&nbsp;milliards d'euros en {{< coll-val "an_dette_fin" >}}) dépasse d'environ {{< coll-val "of_ecart_maastricht" >}}&nbsp;milliards la somme des encours des communes, des intercommunalités, des départements et des régions.

Cette page s'appuie sur deux sources qui ne parlent pas la même langue. Eurostat publie la comptabilité nationale, harmonisée en Europe&nbsp;; l'Observatoire des finances et de la gestion publique locales (OFGL) publie les agrégats des comptes de gestion, ceux que lisent les directions financières. Les grandeurs se correspondent, sans être identiques.

| Ce que lit une direction financière (OFGL) | Ce que publie Eurostat | Ce qui les sépare |
|---|---|---|
| Dotation globale de fonctionnement, concours financiers de l'État | Transferts courants reçus des autres administrations publiques (D73) | Eurostat inclut les transferts de la sécurité sociale&nbsp;; une dotation remplacée par une fraction de TVA passe dans les impôts. |
| Dépenses d'équipement | Formation brute de capital fixe (P51G) | Les subventions d'équipement versées sont des transferts en capital, hors P51G. |
| Capacité ou besoin de financement | Capacité (+) ou besoin (−) de financement (B9) | Même notion&nbsp;; dates d'enregistrement et périmètres diffèrent. |
| Épargne brute | Épargne brute (B8G) | Notions voisines, retraitements différents. |
| Encours de dette | Dette au sens de Maastricht | Valeur nominale&nbsp;; pour les administrations locales, consolidée à l'intérieur du sous-secteur, non entre sous-secteurs. |

La somme des encours des quatre catégories suivies par l'OFGL ({{< coll-val "of_encours_total" >}}&nbsp;milliards d'euros en {{< coll-val "of_an" >}}) reste inférieure à la dette des administrations locales au sens de Maastricht&nbsp;: celle-ci comprend aussi les syndicats et les organismes divers, et suit d'autres conventions. Elle n'est pas non plus consolidée avec l'État&nbsp;: la part que celui-ci en détient ({{< coll-val "fr_detenu_etat" >}}&nbsp;point de PIB) y reste comptée, ce qui la distingue de la «&nbsp;contribution&nbsp;» des administrations locales à la dette publique consolidée que publie l'Insee. L'écart se documente&nbsp;; il ne se corrige pas.

</details>

## Deux récits, une même série {#deux-recits}

L'Association des maires de France, en réponse à la Cour des comptes (juin 2025)&nbsp;: «&nbsp;Considérer les collectivités locales comme la variable d'ajustement des erreurs de stratégie de l'exécutif ne fait que creuser le déficit public.&nbsp;» La Cour des comptes (septembre 2025), «&nbsp;sans se prononcer en opportunité sur son montant&nbsp;», appelle à «&nbsp;organiser dans la durée la participation des collectivités au redressement des finances publiques&nbsp;».

La même série donne un appui à chaque lecture. La dépense des administrations locales est passée de {{< coll-val "te_0" >}}&nbsp;% du PIB en {{< coll-val "te_a0" >}} à {{< coll-val "te_pic" >}}&nbsp;% en {{< coll-val "te_apic" >}}&nbsp;: c'est l'argument d'une participation des collectivités à l'effort. Elle était revenue à {{< coll-val "ep_te_pc_a1" >}}&nbsp;% en {{< coll-val "ep_a1" >}}, au terme de la baisse des dotations, et s'établit à {{< coll-val "te_fin" >}}&nbsp;% en {{< coll-val "an_fin" >}}&nbsp;: c'est l'argument de collectivités déjà mises à contribution. Aucune des deux lectures ne suffit seule&nbsp;; la question utile est de savoir quand, par quel canal et dans quelle unité une contrainte s'observe.

<span id="le-paradoxe-apparent-peu-endettées-très-contraintes"></span>

## Pourquoi la dette ne suffit pas à répondre {#peu-endettees}

L'observation tient. La dette des administrations locales est passée de {{< coll-val "dette_loc_deb" >}}&nbsp;% du PIB en {{< coll-val "an_dette_deb" >}} à {{< coll-val "dette_loc_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}, pendant que la dette publique passait de {{< coll-val "dette_apu_deb" >}}&nbsp;% à {{< coll-val "dette_apu_fin" >}}&nbsp;%, et elle représente moins d'un dixième de la dette publique ({{< coll-val "part_loc_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}). Ces administrations réalisent pourtant {{< coll-val "part_inv_loc_fin" >}}&nbsp;% de l'investissement public ({{< coll-val "inv_loc_fin" >}}&nbsp;% du PIB en {{< coll-val "an_fin" >}}). Le chiffre de {{< coll-val "dette_apu_fin" >}}&nbsp;% vient de la série trimestrielle d'Eurostat (mise à jour du {{< coll-val "dette_maj" >}})&nbsp;; la notification du {{< coll-val "notif_maj" >}}, que citent les autres pages du dossier, donnait {{< coll-val "dette_apu_notif_fin" >}}&nbsp;%.

La raison tient à une règle. Le code général des collectivités territoriales impose l'équilibre réel du budget&nbsp;: section de fonctionnement et section d'investissement votées en équilibre, et remboursement du capital des emprunts couvert par des ressources propres, **à l'exclusion du produit des emprunts** (article L.&nbsp;1612-4). L'emprunt reste ouvert pour financer l'investissement&nbsp;: la règle ne fige pas le stock de dette, qui a d'ailleurs augmenté en 2020 et depuis 2023. Elle empêche en revanche de reporter sur l'emprunt une baisse durable des ressources de fonctionnement, qui passe alors par les recettes propres, la dépense courante, l'épargne brute ou l'investissement. Elle ne régit pas non plus tout le sous-secteur, qui comprend d'autres organismes que les collectivités.

**Une dette contenue est compatible avec un ajustement par les ressources et les dépenses comme avec son absence&nbsp;: elle ne mesure pas l'intensité d'une contrainte.** Aucun indicateur unique ne la remplace ici. Les comptes permettent d'observer des mécanismes et des épisodes&nbsp;; ils ne permettent ni d'en faire une règle générale depuis {{< coll-val "an_dette_deb" >}}, ni d'attribuer ces épisodes à une cause.

## {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}&nbsp;: la baisse des dotations, en euros et en points de PIB {#baisse-des-dotations}

Pendant ces quatre années, l'État réduit sa dotation globale de fonctionnement (DGF) au titre de la «&nbsp;contribution au redressement des finances publiques&nbsp;». Trois grandeurs décrivent l'épisode, et aucune ne remplace les autres&nbsp;:

| Grandeur | Ce qu'elle mesure | De {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}} |
|---|---|---|
| DGF votée (loi de finances, article L.&nbsp;1613-1 du CGCT) | le montant de la dotation fixé chaque année | de {{< coll-val "dgf_vote_13" >}} à {{< coll-val "dgf_vote_17" >}}&nbsp;milliards d'euros |
| Transferts reçus (Eurostat, D73) | les transferts courants de l'État et de la sécurité sociale, toutes dotations comprises | en baisse de {{< coll-val "ep_transf_mde" >}}, soit {{< coll-val "ep_transf_pt" >}} de PIB |
| Investissement (Eurostat, P51G) | la formation brute de capital fixe des administrations locales | en baisse de {{< coll-val "ep_inv_mde" >}}, soit {{< coll-val "ep_inv_pt" >}} de PIB |

En {{< coll-val "ep_a1" >}}, le niveau annuel de la DGF votée est inférieur de {{< coll-val "dgf_vote_baisse" >}}&nbsp;milliards à celui de {{< coll-val "ep_a0" >}}. **Ce n'est pas le total des économies cumulées sur les quatre exercices**, qui additionnerait le manque de chaque année par rapport à {{< coll-val "ep_a0" >}}.

{{< figure-svg fichier="collectivites-cascade" alt="Deux cascades côte à côte, de 2013 à 2017, mêmes postes et même ordre. En milliards d'euros courants, la hausse des impôts dépasse la baisse des transferts, et l'investissement en moins est compensé par la hausse des autres dépenses. En points de PIB, toutes les dépenses reculent et les impôts ne compensent qu'une partie de la baisse des transferts. Les deux cascades aboutissent au même solde légèrement excédentaire." >}}Variation du solde des administrations publiques locales entre {{< coll-val "ep_a0" >}} et {{< coll-val "ep_a1" >}}, décomposée en cinq postes, en milliards d'euros courants (à gauche) et en points de PIB (à droite). Chaque valeur est la contribution du poste à la variation du solde&nbsp;: pour une dépense, l'inverse de sa variation, si bien qu'une dépense en baisse améliore le solde. Le PIB nominal augmente de {{< coll-val "pib_croiss_pct" >}}&nbsp;% sur la période&nbsp;: c'est ce dénominateur qui sépare les deux lectures.{{< /figure-svg >}}

{{< fig-actions id="cascade" >}}

**Les deux lectures sont exactes et ne racontent pas la même chose.** En euros courants, les recettes augmentent de {{< coll-val "ep_tr_mde" >}}, les impôts à eux seuls de {{< coll-val "ep_imp_md" >}}&nbsp;milliards, quand les transferts reçus reculent de {{< coll-val "ep_transf_md" >}}&nbsp;milliards&nbsp;; les dépenses totales passent de {{< coll-val "ep_te0_md" >}} à {{< coll-val "ep_te1_md" >}}&nbsp;milliards. Le solde se redresse ainsi de {{< coll-val "ep_solde_mde" >}} ({{< coll-val "ep_solde_pt" >}} de PIB), par le côté des recettes. En points de PIB, les dépenses reculent de {{< coll-val "ep_te_pt" >}}, dont {{< coll-val "ep_inv_pt" >}} pour l'investissement, et les impôts ne compensent qu'une partie de la baisse des transferts ({{< coll-val "ep_imp_pt" >}} contre {{< coll-val "ep_transf_pt" >}}).

L'écart tient au dénominateur. Le PIB nominal augmente de {{< coll-val "pib_croiss_pct" >}}&nbsp;% entre {{< coll-val "ep_a0" >}} et {{< coll-val "ep_a1" >}}&nbsp;: une dépense presque gelée en euros recule en part du PIB. **La baisse d'un ratio ne prouve pas une baisse de la dépense en euros.** L'investissement, lui, recule aussi en euros, de {{< coll-val "ep_inv_pct_eur" >}}&nbsp;%, quand les autres dépenses augmentent de {{< coll-val "ep_autres_dep_mde" >}}. Aucune lecture en volume, qui demanderait un indice des prix propre aux dépenses locales, n'est faite ici.

Ces évolutions sont concomitantes&nbsp;; elles ne permettent pas, à elles seules, d'attribuer le recul de l'investissement à la baisse des dotations.

**La comparaison ne permet pas de ramener l'ampleur du creux au seul cycle municipal.** L'investissement local baisse habituellement après les municipales. Mais après les élections de 2001, 2008 et 2020, le recul n'a jamais dépassé {{< coll-val "creux_autres_max" >}}&nbsp;point de PIB&nbsp;; après celles de 2014, il atteint {{< coll-val "creux14_baisse" >}}&nbsp;point en {{< coll-val "creux14_annee" >}}, {{< coll-val "creux_ratio" >}}&nbsp;fois plus, pendant que les concours de l'État diminuent. La comparaison affaiblit l'explication par le seul calendrier électoral&nbsp;; elle n'isole pas l'effet des dotations, d'autant que les départements et les régions, compris dans l'agrégat, ne suivent pas ce cycle.

<details class="repli"><summary>Le témoin du cycle électoral, mandat par mandat, les trois mesures de la DGF et le témoin comptable de la cascade</summary>

{{< coll-tableau "cycles" >}}

L'Insee rattache le recul de 2014 «&nbsp;à la suite des élections municipales&nbsp;» puis celui de 2015 «&nbsp;notamment&nbsp;» au cycle électoral communal, en notant cette année-là l'effet de «&nbsp;la baisse des transferts de l'État&nbsp;».

Les quatre épisodes ne sont pas identiques&nbsp;: 2008 précède la crise financière, 2020 est l'année de la pandémie. Isoler l'effet des dotations demanderait de comparer, collectivité par collectivité, les plus et les moins exposées à leur baisse, avant et après 2014.

La DGF votée baisse chaque année, de {{< coll-val "dgf_vote_b14" >}}&nbsp;milliard d'euros en 2014, puis de {{< coll-val "dgf_vote_b15" >}}, de {{< coll-val "dgf_vote_b16" >}} et de {{< coll-val "dgf_vote_b17" >}}&nbsp;milliards les trois années suivantes. Le montant de la DGF fixé par la loi de finances n'est ni la contribution demandée à chaque catégorie, ni la DGF que chaque collectivité a effectivement inscrite dans ses comptes&nbsp;: ces trois mesures ne s'additionnent pas. Les comptes de gestion montrent la troisième mesure par catégorie&nbsp;: la DGF des départements passe de {{< coll-val "of_dgf_dep_13" >}} à {{< coll-val "of_dgf_dep_17" >}}&nbsp;milliards d'euros, celle des régions de {{< coll-val "of_dgf_reg_13" >}} à {{< coll-val "of_dgf_reg_17" >}}&nbsp;milliards.

La cascade se vérifie par une identité que le générateur contrôle à chaque passage&nbsp;: recettes totales moins dépenses totales égalent le solde publié par Eurostat. Sur les {{< coll-val "temoin_annees" >}}&nbsp;années disponibles, l'écart maximal est de {{< coll-val "temoin_residu" >}}&nbsp;million d'euros, un arrondi. Les deux cascades se referment chacune sur la variation du solde. La part du dénominateur se calcule exactement, sur le PIB des mêmes comptes&nbsp;: à dépense inchangée, la croissance du PIB aurait fait reculer de {{< coll-val "ep_te_effet_pib_pt" >}} le ratio des dépenses au PIB&nbsp;; la hausse des dépenses en euros en a repris {{< coll-val "ep_te_effet_eur_pt" >}}, d'où le recul de {{< coll-val "ep_te_pt" >}}.

</details>

<span id="trois-canaux"></span>

<span id="les-trois-mécanismes-du-transfert"></span>

## Le mécanisme change, la question demeure {#mecanismes}

Une contrainte de l'État peut atteindre les collectivités par des canaux qui ne sont pas de même nature&nbsp;: certains réduisent des ressources, d'autres encadrent des dépenses, d'autres encore changent la composition des recettes. Depuis 2014, ils se sont succédé.

1. **{{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}&nbsp;: agir sur les ressources.** La DGF votée baisse chaque année&nbsp;; l'investissement recule dans le même temps.
2. **{{< coll-val "cahors_ex1" >}}-{{< coll-val "cahors_ex2" >}}&nbsp;: encadrer les dépenses.** Les contrats de Cahors imposent à certaines collectivités un objectif de progression de leurs dépenses de fonctionnement, sur la base d'une référence nationale de {{< coll-val "cahors_taux" >}}&nbsp;% par an. La reprise financière prévue en cas de dépassement est suspendue pour les dépenses de {{< coll-val "cahors_suspendu" >}}. Un nouveau canal de contrainte apparaît, qui n'implique pas la disparition des précédents&nbsp;; cette page ne peut pas en mesurer l'effet propre.
3. **2018 et 2021&nbsp;: changer la composition des recettes.** Une dotation (2018), puis des impôts supprimés (2021), font place à des fractions de TVA ou à un prélèvement sur les recettes de l'État. Certaines ressources sont remplacées par des recettes d'une autre nature&nbsp;: leur classement comptable change, sans que ce reclassement permette, à lui seul, de conclure à une hausse ou à une baisse des ressources disponibles. Les séries cessent alors d'être comparables (détail ci-dessous).
4. **{{< coll-val "plf_edition" >}}&nbsp;: plusieurs canaux à la fois.** Prélèvement sur les ressources, concours lié à l'investissement, calendrier de reversements&nbsp;: le projet de loi de finances les combine ([dernière section](#projet-de-loi-de-finances)).

<details class="repli"><summary>Les contrats de Cahors dans le texte&nbsp;: collectivités concernées, base, reprise financière</summary>

La loi de programmation des finances publiques du {{< coll-val "cahors_date_lpfp" >}} fixe aux collectivités un objectif national d'évolution de leurs dépenses réelles de fonctionnement de {{< coll-val "cahors_taux" >}}&nbsp;% par an, en valeur, calculé sur la base de {{< coll-val "cahors_base" >}} (article 13). Des contrats, dits «&nbsp;de Cahors&nbsp;», le déclinent pour les exercices {{< coll-val "cahors_ex1" >}}, {{< coll-val "cahors_ex2" >}} et {{< coll-val "cahors_ex3" >}}&nbsp;; ils visent les régions, les départements et les collectivités à statut particulier, ainsi que les communes et intercommunalités dont les dépenses réelles de fonctionnement dépassaient {{< coll-val "cahors_seuil_m" >}}&nbsp;millions d'euros en 2016 (article 29). Pour une collectivité signataire, un dépassement entraîne une reprise financière de {{< coll-val "cahors_reprise_pct" >}}&nbsp;% de l'écart, plafonnée à {{< coll-val "cahors_plafond_pct" >}}&nbsp;% des recettes réelles de fonctionnement (article 29, V)&nbsp;; un taux distinct s'applique aux collectivités qui n'ont pas signé (article 29, VI).

La loi d'urgence du {{< coll-val "cahors_date_urgence" >}} écarte cette reprise pour les dépenses de {{< coll-val "cahors_suspendu" >}} (article 12)&nbsp;: elle n'a donc pu s'appliquer qu'aux dépenses de {{< coll-val "cahors_ex1" >}} et de {{< coll-val "cahors_ex2" >}}. L'effet des contrats ne se mesure pas dans ces séries&nbsp;: ils ne portent que sur le budget principal des collectivités concernées, que l'agrégat national ne sépare pas.

</details>

Deux autres canaux échappent à ces séries&nbsp;: les compétences transférées sans financement complet, dont la compensation figée décroche du coût réel et se lit compétence par compétence (les allocations individuelles de solidarité des départements, par exemple), et les normes non financées, dont le coût se lit dans les évaluations préalables. Tous ces canaux partagent une hypothèse à tester&nbsp;: une décision prise à un niveau peut déplacer une partie de son coût vers un autre. Le document de travail [AWP-09](/awp/awp-09/) la confronte à l'épisode {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}&nbsp;: les comptes la rendent compatible, sans l'établir.

### 2018 et 2021&nbsp;: quand une ressource change de classement {#ruptures}

En 2018, la DGF des régions passe de {{< coll-val "of_dgf_reg_17" >}} à {{< coll-val "of_dgf_reg_18" >}}&nbsp;milliard d'euros pendant qu'elles reçoivent {{< coll-val "of_tva_reg_18" >}}&nbsp;milliards de TVA (OFGL)&nbsp;: une recette classée parmi les transferts devient une recette fiscale. En 2021, les transferts reçus par l'ensemble des administrations locales chutent de {{< coll-val "rupt_transf" >}}&nbsp;point de PIB et leurs impôts augmentent de {{< coll-val "rupt_imp" >}}&nbsp;point&nbsp;: la suppression de la taxe d'habitation sur les résidences principales et celle de la part régionale de la cotisation sur la valeur ajoutée des entreprises (CVAE) sont compensées par des fractions de TVA ou, pour les communes, par la part départementale de taxe foncière. Une série limitée aux seules dotations ne mesure donc pas, à elle seule, l'évolution des ressources.

<details class="repli"><summary>Les compensations de 2021, texte par texte</summary>

La suppression de la taxe d'habitation sur les résidences principales est compensée par une fraction de TVA aux intercommunalités et aux départements, les communes recevant la part départementale de taxe foncière (loi de finances pour 2020, article&nbsp;16)&nbsp;; la suppression de la part régionale de la CVAE, par une fraction de TVA aux régions (loi de finances pour 2021, article&nbsp;8)&nbsp;; la réduction des valeurs locatives des établissements industriels, par un prélèvement sur les recettes de l'État (même loi, article&nbsp;29).

</details>

## Par catégorie de collectivités&nbsp;: ce que l'agrégat cache {#par-categorie}

L'agrégat national additionne des collectivités dont les recettes et les charges n'ont rien de commun. Depuis 2018, l'Observatoire des finances et de la gestion publique locales (OFGL) publie les comptes de gestion consolidés de chaque catégorie, ceux que lisent les directions financières. Deux mouvements y apparaissent, invisibles dans l'agrégat. L'épargne brute des départements, c'est-à-dire leurs recettes de fonctionnement moins leurs dépenses de fonctionnement, tombe de {{< coll-val "of_eb_dep_pic" >}}&nbsp;milliards d'euros en {{< coll-val "of_eb_dep_apic" >}} à {{< coll-val "of_eb_dep_min" >}} en {{< coll-val "of_eb_dep_amin" >}}, avant de remonter à {{< coll-val "of_eb_dep_fin" >}} en {{< coll-val "of_an" >}}&nbsp;; ses causes (droits de mutation, allocations de solidarité) relèvent de séries que cette page ne porte pas. Les dépenses d'équipement des communes passent de {{< coll-val "of_eq_com_20" >}}&nbsp;milliards en 2020 à {{< coll-val "of_eq_com_fin" >}} en {{< coll-val "of_an" >}} (+{{< coll-val "of_eq_com_hausse_pct" >}}&nbsp;%), à l'approche des municipales de 2026.

<details class="repli"><summary>Les quatre catégories de collectivités, de 2021 à {{< coll-val "of_an" >}}&nbsp;: concours de l'État, épargne brute, équipement, dette</summary>

{{< coll-tableau "categories" >}}

Les périmètres des catégories changent au fil des réformes&nbsp;: la base consolidée des départements utilisée ici incorpore la métropole de Lyon (depuis 2015) et la Ville de Paris (depuis 2019), celle des régions les collectivités uniques de Guyane, de Martinique et de Corse — le rapport annuel de l'OFGL, lui, classe Lyon avec les intercommunalités et Paris avec les communes. Comptabilité nationale et comptes de gestion ne coïncident pas au million près&nbsp;: périmètres, dates d'enregistrement et retraitements diffèrent.

</details>

## Depuis 2023&nbsp;: la dette des administrations locales remonte {#depuis-2023}

Depuis {{< coll-val "recent_a0" >}}, le besoin de financement des administrations publiques locales dépasse nettement celui de {{< coll-val "avant_a0" >}} et de {{< coll-val "avant_a1" >}} (moins d'un dixième de point de PIB)&nbsp;: {{< coll-val "recent_solde_deb_pt" >}} en {{< coll-val "recent_a0" >}}, {{< coll-val "recent_solde_mid_pt" >}} en {{< coll-val "recent_a1" >}} et {{< coll-val "recent_solde_fin_pt" >}} en {{< coll-val "an_fin" >}}. Leur investissement remonte de {{< coll-val "recent_inv_deb1" >}}&nbsp;% à {{< coll-val "inv_loc_fin" >}}&nbsp;% du PIB, et leur dette de {{< coll-val "recent_dette_deb" >}}&nbsp;% à {{< coll-val "dette_loc_fin" >}}&nbsp;% du PIB&nbsp;: c'est l'inverse du schéma de {{< coll-val "ep_a0" >}}-{{< coll-val "ep_a1" >}}. Dans les comptes de gestion des quatre catégories de collectivités, l'encours de dette augmente aussi&nbsp;: {{< coll-val "of_encours_rec0" >}}&nbsp;milliards d'euros en {{< coll-val "of_encours_rec0_annee" >}}, {{< coll-val "of_encours_total" >}} en {{< coll-val "of_an" >}}. **Le reste de la hausse ne s'attribue pas par différence aux syndicats et aux organismes divers**&nbsp;: les deux sources ne consolident pas de la même façon et ne suivent pas les mêmes conventions.

<details class="repli"><summary>Le dispositif de lissage des recettes fiscales (DILICO), en 2025 et en 2026</summary>

Le dispositif de lissage conjoncturel des recettes fiscales (DILICO) a prélevé en 2025 {{< coll-val "dilico_2025" >}} sur les ressources fiscales des collectivités, mis en réserve et reversé par tiers les trois années suivantes — 90&nbsp;% aux collectivités contributrices, 10&nbsp;% aux fonds de péréquation (loi de finances pour 2025, article&nbsp;186)&nbsp;; il est reconduit en 2026 (loi de finances pour 2026). Ni l'Insee ni Eurostat ne documentent son enregistrement en comptabilité nationale&nbsp;: son effet propre ne s'isole pas dans ces séries.

</details>

<span id="ce-que-cette-lecture-change"></span>

## Ailleurs en Europe&nbsp;: une même dette, des architectures opposées {#ailleurs-en-europe}

Les comparaisons se font ici par périmètre statistique, non par compétences exercées. La France et l'Italie, où les régions sont classées parmi les administrations locales, forment la comparaison principale&nbsp;; l'Allemagne et l'Espagne, dont la dette territoriale additionne celle des Länder ou des communautés autonomes et celle des collectivités locales, servent de contrepoints.

{{< figure-svg fichier="collectivites-europe" alt="Quatre petits graphiques en pourcentage du PIB : la dette territoriale française monte doucement, l'allemande reste haute, portée par les Länder, l'italienne monte puis redescend, l'espagnole fait plus que doubler. Sous chaque graphique, la part détenue par l'État central : quasi nulle en France et en Allemagne, faible en Italie, plus de la moitié en Espagne." >}}Dette des administrations territoriales en % du PIB, quatrième trimestre de chaque année, et part détenue par l'administration centrale, publiée depuis 2020 (indiquée sous chaque pays).{{< /figure-svg >}}

{{< fig-actions id="europe" >}}

**En Espagne**, la dette territoriale passe de {{< coll-val "es_dette_deb" >}}&nbsp;% du PIB en {{< coll-val "an_dette_deb" >}} à {{< coll-val "es_dette_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}, portée par les communautés autonomes, pendant que l'investissement territorial perd {{< coll-val "es_inv_baisse_pct" >}}&nbsp;%. Mais cette dette ne mesure pas un report de contrainte vers le bas&nbsp;: en {{< coll-val "an_ggd" >}}, {{< coll-val "es_detenu_etat" >}}&nbsp;points de PIB sur {{< coll-val "es_detenu_total" >}}, soit {{< coll-val "es_part_etat_pct" >}}&nbsp;%, sont détenus par l'État central lui-même, notamment par le Fondo de Liquidez Autonómico, créé en 2012, par lequel l'État prête aux communautés autonomes (Real Decreto-ley 21/2012, articles&nbsp;9 et 14). La part équivalente est de {{< coll-val "it_part_etat_pct" >}}&nbsp;% en Italie, de {{< coll-val "fr_part_etat_pct" >}}&nbsp;% en France et de {{< coll-val "de_part_etat_pct" >}}&nbsp;% en Allemagne. **Qui porte une dette et qui la finance sont deux questions distinctes.**

**En Italie**, les trois indicateurs vont dans le même sens&nbsp;: la dette territoriale redescend de {{< coll-val "it_dette_pic" >}}&nbsp;% du PIB en {{< coll-val "it_dette_pic_annee" >}} à {{< coll-val "it_dette_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}, le solde est excédentaire {{< coll-val "it_excedents" >}}&nbsp;années sur huit entre 2012 et 2019 (France&nbsp;: {{< coll-val "fr_excedents" >}}), l'investissement tombe à la moitié de son maximum des années 2000. Ces concomitances n'isolent pas l'effet des règles nationales — le pacte de stabilité interne, institué en 1999 et abandonné pour les collectivités locales en 2016 — de celui de la crise des dettes souveraines.

**En Allemagne**, la dette territoriale reste nettement sous son pic de {{< coll-val "de_dette_pic_annee" >}} ({{< coll-val "de_dette_pic" >}}&nbsp;%, {{< coll-val "de_dette_fin" >}}&nbsp;% en {{< coll-val "an_dette_fin" >}}), avec un recul d'investissement limité ({{< coll-val "de_inv_baisse_pct" >}}&nbsp;%)&nbsp;; elle est portée surtout par les Länder.

La comparaison ne fait apparaître aucun classement unique&nbsp;: dette, solde et investissement ordonnent les quatre pays différemment. Elle montre qu'une contrainte de finances publiques peut circuler entre niveaux d'administration sous des formes opposées — baisse de dotation, recul d'investissement, dette, ou financement du niveau territorial par le centre.

<details class="repli"><summary>Les quatre pays, indicateur par indicateur</summary>

{{< coll-tableau "pays" >}}

Le sous-secteur des administrations d'États fédérés (S1312) n'existe, dans les données Eurostat, que dans quelques pays, dont l'Allemagne et l'Espagne&nbsp;; les régions françaises et italiennes sont classées parmi les administrations locales (S1313). En Allemagne et en Espagne, la dette territoriale additionne donc les deux échelons&nbsp;; les dettes croisées entre eux représentent au plus {{< coll-val "consolidation_ecart_pt" >}} de PIB&nbsp;: le double compte est marginal et ne modifie pas les ordres de grandeur. En Espagne, la loi organique 2/2012 affecte en outre les excédents de chaque niveau d'administration à la réduction de son endettement net (article&nbsp;32).

</details>

## Que demande le projet de loi de finances aux collectivités&nbsp;? {#projet-de-loi-de-finances}

*État du texte&nbsp;: projet de loi de finances pour {{< coll-val "plf_edition" >}}, déposé le {{< coll-val "plf_depot" >}}, avant examen par le Parlement&nbsp;; ses montants peuvent changer d'ici la loi votée.*

{{< coll-tableau "plf" >}}

Le projet ne baisse pas la DGF&nbsp;: il prévoit {{< coll-val "plf_dgf_hausse_m" >}}&nbsp;millions d'euros d'abondements nouveaux et, compte tenu des mesures de périmètre, son montant nominal augmente de {{< coll-val "plf_dgf_hausse_courant_m" >}}&nbsp;millions, à {{< coll-val "plf_dgf" >}}&nbsp;milliards. La mise à contribution passe par les cinq canaux du tableau et, pour les régions, par la suppression d'une fraction d'accises sur les énergies de {{< coll-val "plf_regions_m" >}}&nbsp;millions d'euros (article&nbsp;39). Le Haut Conseil des finances publiques réunit ces mesures dans un même paquet de modération des recettes des collectivités.

**Comment les ressources des collectivités pourraient-elles augmenter de {{< coll-val "plf_ressources_md" >}}&nbsp;milliards d'euros, alors que la somme arithmétique des mesures du projet atteint {{< coll-val "plf_somme" >}}&nbsp;milliards&nbsp;?**

{{< coll-tableau "plf_lectures" >}}

**Pourquoi ces chiffres coexistent-ils&nbsp;?** La somme arithmétique de {{< coll-val "plf_somme" >}}&nbsp;milliards rassemble cinq mesures évaluées chacune par rapport à la situation sans elle, selon des références différentes&nbsp;; les {{< coll-val "plf_ressources_md" >}}&nbsp;milliards du Gouvernement comparent deux années, mesures comprises. Leur différence, {{< coll-val "plf_ecart_mde" >}}, ne représente donc pas un prélèvement net, et additionner les cinq mesures ne suffit pas à établir leur effet net&nbsp;: une ressource peut augmenter en euros tout en progressant moins vite qu'en l'absence de réforme. Les cinq mesures ne sont pas non plus de même nature, et deux d'entre elles portent sur des flux voisins&nbsp;: leur rapprochement exact n'est pas fait ici.

<details class="repli"><summary>Nature des cinq mesures, assiette de la contribution progressive et prélèvements sur recettes</summary>

L'étalement du reversement des sommes mises en réserve (DILICO) déplace un calendrier sans modifier le montant total restitué (article&nbsp;84)&nbsp;; la baisse du taux du fonds de compensation pour la TVA dépend des investissements que les collectivités réaliseront. Le texte ne décrit pas de double compte entre ces montants, mais deux d'entre eux portent sur des flux voisins&nbsp;: la contribution progressive est imputée sur les douzièmes de fiscalité et sur les fractions de TVA, dont la progression est par ailleurs écrêtée (articles&nbsp;36 et 37).

La contribution progressive s'applique à {{< coll-val "plf_cpeb_communes_pct" >}}&nbsp;% des communes, à {{< coll-val "plf_cpeb_dep_pct" >}}&nbsp;% des départements et aux intercommunalités de métropole, à un taux qui croît avec leurs ressources, appliqué aux recettes réelles de fonctionnement de l'antépénultième exercice&nbsp;; les collectivités d'outre-mer et les départements les plus fragiles socialement en sont exonérés (article&nbsp;37). Dans le budget de l'État, les prélèvements sur recettes au profit des collectivités sont évalués à {{< coll-val "plf_psr" >}}&nbsp;milliards d'euros pour {{< coll-val "plf_edition" >}}, contre {{< coll-val "plf_psr_rev_prec" >}}&nbsp;milliards dans la prévision révisée pour {{< coll-val "plf_prec" >}} ({{< coll-val "plf_psr_lfi_prec" >}}&nbsp;milliards dans la loi de finances initiale, article&nbsp;41)&nbsp;: une série limitée aux dotations ne verrait pas ces canaux, pour la raison déjà rencontrée [en 2018 et en 2021](#ruptures).

</details>

Le Haut Conseil prévoit un recul de l'investissement des collectivités de {{< coll-val "plf_inv_n1_pct" >}}&nbsp;% en {{< coll-val "plf_edition" >}}, après {{< coll-val "plf_inv_n_pct" >}}&nbsp;% en {{< coll-val "plf_prec" >}}, et le juge vraisemblable au regard de la position de {{< coll-val "plf_edition" >}} dans le cycle électoral communal, une année après les élections, ainsi que de la réforme du fonds de compensation. Cette page mesure ce qu'un recul de l'investissement a représenté [de {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}](#baisse-des-dotations)&nbsp;; elle ne dit pas s'il se reproduira. Textes&nbsp;: [projet de loi de finances pour {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf), articles 34 à 41 et 84&nbsp;; [avis du Haut Conseil des finances publiques](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf).

## Ce que les comptes permettent de dire {#ce-que-disent-les-comptes}

Trois perspectives sont à tenir séparées. **Ce qui est décidé**&nbsp;: dotations, impôts transférés, règles de dépense, modalités de financement, que fixent les lois de finances et de programmation. **Ce qui s'observe**&nbsp;: recettes, dépenses, investissement, épargne, solde et dette, dans les comptes nationaux et les comptes de gestion. **Ce qui est finalement supporté**&nbsp;: les effets sur les contribuables, les usagers, les services et les équipements, que ces données ne mesurent pas.

Cette page documente des décisions et des évolutions comptables concomitantes&nbsp;; elle ne démontre pas la transmission des unes aux autres et ne mesure pas ce qui est finalement supporté.

<details class="repli"><summary>Le schéma d'analyse&nbsp;: une chaîne en quatre maillons</summary>

Entre ce qui est décidé et ce qui est supporté, une chaîne en quatre maillons décrit les mécanismes possibles. C'est un schéma d'analyse, non une causalité démontrée sur chaque maillon&nbsp;:

1. **décision nationale**&nbsp;: dotation réduite, recette encadrée, règle de dépense&nbsp;;
2. **contrainte territoriale**&nbsp;: moins de ressources, ou moins de liberté d'arbitrage&nbsp;;
3. **réponse budgétaire locale**&nbsp;: fiscalité, fonctionnement, épargne, investissement, emprunt&nbsp;;
4. **incidence finale**&nbsp;: services, équipements, contribuables, usagers, territoires.

Les décisions relèvent du premier maillon, les évolutions comptables du troisième&nbsp;; le quatrième n'est pas mesuré ici.

</details>

<span id="et-au-bout-de-la-chaîne-une-hypothèse-sur-les-ménages-les-moins-mobiles"></span>

<details class="repli" id="qui-supporte"><summary>Hypothèse de recherche, non testée ici&nbsp;: qui supporte finalement l'ajustement&nbsp;?</summary>

Les comptes ne permettent pas de savoir si l'ajustement est finalement supporté par les contribuables, les usagers, les agents publics, les fournisseurs, les propriétaires fonciers ou les ménages qui dépendent des services locaux. L'[anthropie](/quest-ce-que-lanthropie/), cadre d'analyse proposé par l'auteur, formule l'hypothèse que certains coûts sont plus difficiles à éviter pour les ménages les moins mobiles&nbsp;: un ménage qui dépend du logement social, des transports publics et des équipements de proximité subit plus directement une hausse de tarif ou une fermeture qu'un ménage qui peut changer de commune. Cette page ne la teste pas&nbsp;; elle se vérifierait décision par décision, et serait affaiblie par des ajustements portant surtout sur les ménages aisés ou compensés par des tarifs sociaux.

</details>

## Ce que ces données ne disent pas {#limites}

- L'agrégat national mêle communes, intercommunalités, départements, régions, syndicats et organismes divers&nbsp;; les données par catégorie ne remontent qu'à 2018, et les périmètres des catégories changent au fil des réformes ([détail](#par-categorie)).
- Une baisse d'investissement concomitante d'une baisse de dotations n'établit pas que la seconde a causé la première&nbsp;; l'effet des contrats de Cahors n'est pas mesuré ici.
- Les montants sont en euros courants et en points de PIB&nbsp;; aucune lecture en volume n'est faite.
- Elles ne disent rien de la qualité des services rendus, ni de qui a finalement supporté l'ajustement.

## Comment lire ces résultats dans les comptes de votre collectivité&nbsp;? {#votre-collectivite}

Les résultats nationaux ne donnent aucun montant pour une collectivité donnée. Ils indiquent quoi comparer dans ses propres comptes&nbsp;: son compte de gestion ou son compte financier unique, ou les agrégats que l'OFGL publie collectivité par collectivité sur data.ofgl.fr, ceux qu'utilise cette page.

1. **Les ressources reçues de l'État** (DGF et autres concours)&nbsp;: leur évolution en euros, sachant qu'une dotation remplacée par une fraction de TVA passe dans les recettes fiscales, comme en 2018 et en 2021.
2. **Les recettes fiscales**&nbsp;: en séparant les impôts dont la collectivité vote le taux des fractions d'impôts nationaux qu'elle reçoit.
3. **L'épargne brute**&nbsp;: les recettes de fonctionnement moins les dépenses de fonctionnement&nbsp;; avec les autres ressources propres, elle doit couvrir le remboursement du capital de la dette.
4. **Les dépenses d'investissement**&nbsp;: en euros et rapportées aux recettes, en tenant compte du cycle municipal.

Pour {{< coll-val "plf_edition" >}}, l'assujettissement à la contribution progressive se vérifie dans l'article 37 du projet (critères, taux, exonérations), puis, une fois la loi votée, dans l'arrêté publié au Journal officiel qui fixera, selon le projet, le montant prélevé sur chaque collectivité. L'effet de la baisse du taux du fonds de compensation se lit dans ses propres dépenses éligibles&nbsp;; l'étalement des sommes mises en réserve ne concerne que les collectivités qui y ont contribué en 2025 ou en 2026.

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

**Comptabilité nationale** — Eurostat, administrations publiques par sous-secteur, SEC 2010&nbsp;: comptes annuels (`gov_10a_main`&nbsp;: formation brute de capital fixe P51G, transferts courants reçus D73REC, impôts D2, D5 et D91, recettes TR, dépenses TE, solde B9), dette trimestrielle (`gov_10q_ggdebt`), dette par secteur détenteur (`gov_10dd_ggd`), PIB nominal et dette de la notification (`gov_10dd_edpt1`), PIB des comptes nationaux en témoin du dénominateur (`nama_10_gdp`). Les points de PIB de la cascade sont calculés sur le PIB des mêmes comptes annuels&nbsp;; la croissance du PIB citée est celle de la notification.

**Comptes de gestion** — OFGL, bases consolidées des communes, des intercommunalités, des départements et des régions (data.ofgl.fr, données DGFiP).

**Textes** — code général des collectivités territoriales, articles L.&nbsp;1612-4 et L.&nbsp;1613-1&nbsp;; loi n°&nbsp;2018-32 du {{< coll-val "cahors_date_lpfp" >}} de programmation des finances publiques pour les années 2018 à 2022, articles 13 et 29&nbsp;; loi n°&nbsp;2020-290 du {{< coll-val "cahors_date_urgence" >}} d'urgence pour faire face à l'épidémie de covid-19, article 12&nbsp;; lois de finances pour 2020 (art.&nbsp;16), 2021 (art.&nbsp;8 et 29), 2025 (art.&nbsp;186) et 2026&nbsp;; projet de loi de finances déposé le {{< coll-val "plf_depot" >}} et avis du Haut Conseil des finances publiques sur ce projet&nbsp;; tous lus dans le texte et archivés avec leur empreinte&nbsp;; Real Decreto-ley 21/2012 et loi organique 2/2012 (Espagne)&nbsp;; loi n°&nbsp;448/1998, art.&nbsp;28, et loi n°&nbsp;208/2015 (Italie, pacte de stabilité interne puis règle d'équilibre)&nbsp;; Insee, *Les comptes des administrations publiques* en 2010, 2014 et 2015&nbsp;; Cour des comptes, *Les finances publiques locales 2025* et réponses publiées.

Les calculs, les gardes et les figures sont produits par un script unique, relancé à chaque publication des sources&nbsp;; aucun chiffre de cette page n'est saisi à la main, et le script refuse d'écrire si une donnée cesse de soutenir une phrase, ou si une phrase tire des chiffres une conclusion qu'ils ne portent pas. **Télécharger les données** (licence CC BY 4.0)&nbsp;: [CSV](/dette_collectivites.csv), en format long, lisible dans un tableur&nbsp;; [JSON](/dette_collectivites.json), avec les calculs, les définitions et le compte rendu des gardes.

{{< reutiliser figures="figures_collectivites" jeu="dette_collectivites" sources="Eurostat, OFGL et Légifrance" donnees="Les séries par pays et par catégorie de collectivités, la DGF votée, la décomposition 2013-2017 en milliards d'euros et en points de PIB, les mesures du projet de loi de finances et le compte rendu des contrôles ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
La dette des collectivités, encadrée par la règle d'équilibre réel, ne suffit pas à dire si une contrainte venue de l'État a pesé sur elles&nbsp;: cette contrainte se lit dans leurs recettes et leurs dépenses. De {{< coll-val "ep_a0" >}} à {{< coll-val "ep_a1" >}}, les administrations publiques locales améliorent leur solde de {{< coll-val "ep_solde_mde" >}}, avec des dépenses presque stables en euros courants, des recettes fiscales en hausse et des transferts reçus en baisse&nbsp;; rapportées au PIB, leurs dépenses diminuent de {{< coll-val "ep_te_pt" >}}, dont {{< coll-val "ep_inv_pt" >}} pour l'investissement. Ces évolutions sont concomitantes et ne suffisent pas à attribuer le recul de l'investissement à la baisse des dotations&nbsp;; ailleurs, la contrainte prend d'autres formes, comme en Espagne, où l'État central détient plus de la moitié de la dette territoriale.
{{< /reutiliser >}}
