---
title: "La dette publique est-elle un fardeau pour les générations futures ?"
description: "Depuis {gen.a0}, {gen.part_k} % seulement des déficits publics français ont correspondu, dans les comptes, à un accroissement net des actifs publics comptabilisés, et {gen.nr_fin} % de la dette est détenue hors de France. Selon la Commission européenne, l'effort que laisse la dette tient à la position budgétaire présente bien plus qu'au vieillissement. Séries Eurostat et BCE recalculées et contrôlées."
chapo: "Deux arguments allègent le poids de la dette pour ceux qui viennent ; les comptes ne les soutiennent pas pour la France. Sur le champ des actifs comptabilisés, {gen.part_k} % seulement des déficits ont correspondu depuis {gen.a0} à un accroissement net des actifs publics ; et {gen.nr_fin} % de la dette est aujourd'hui détenue hors du pays. Le troisième, qui place le vrai fardeau dans les retraites, ne tient pas mieux : selon l'indicateur de la Commission européenne, l'effort qui stabiliserait la dette tient à la position budgétaire présente bien plus qu'au vieillissement."
date: 2026-07-24
lastmod: 2026-10-06
og_title: "La dette est-elle un fardeau pour les générations futures ? — S. Lalut"
og_image: "images/og-dette-generations.jpg"
og_image_alt: "Carte de partage : « Des déficits pour le courant » — France, part des déficits publics qui a correspondu, dans les comptes, à des actifs, par décennie, et le reste à des dépenses courantes non couvertes."
# Refonte du 03/10/2026 en ressource de données, sur le modèle du dossier dette (plan de diffusion d'octobre, § 5).
# Test décisif avant la page, protocole écrit avant le calcul : D:\PRO\06_PROMOTION\RECHERCHE_GENERATIONS_FUTURES_2026-10-03\test_decisif\
# (PROTOCOLE.md, VERDICT.md) : les trois arguments tombent. Contre-expertise PRO-20261003-195656, arbitrée le 03/10 :
# jamais « financé » (composition comptable, Auerbach, Gokhale et Kotlikoff 1991) ; patrimoine complet ; COR hors de S2.
# Aucun chiffre saisi : jetons {gen.*} et shortcodes gen-val / gen-tableau (scripts/update_dette_generations.py).
donnees: [dette_generations]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_generations"
  nom: "Dette publique et générations futures : emplois du besoin de financement, patrimoine, détention de la dette et indicateur S2, France et Union européenne"
  description: "Compilation dérivée automatiquement des sources officielles : emplois du besoin de financement des administrations publiques (désépargne nette, acquisitions nettes d'actifs non financiers, transferts en capital), France de {gen.a0} à {gen.fin} et 27 pays de l'Union de {gen.cp_a0} à {gen.fin} (Eurostat) ; patrimoine des administrations publiques ({gen.s0}-{gen.s1}) ; dette par secteur détenteur ({gen.h0}-{gen.h_fin}, BCE ; dette négociable de l'État, Banque de France) ; indicateur S2 de la Commission européenne ({gen.dsm_lib}) ; dépenses de retraite projetées par le COR. Ratios contrôlés contre ceux que publie Eurostat."
  couverture_temporelle: "{gen.h0}/{gen.fin}"
  couverture_spatiale: "France ; Union européenne (27 pays)"
  variables:
    - {nom: "Besoin de financement des administrations publiques", unite: "points de PIB", description: "cumulé par période, et ses trois emplois"}
    - {nom: "Acquisitions nettes d'actifs non financiers", unite: "points de PIB", description: "investissement moins consommation de capital fixe, terrains, stocks"}
    - {nom: "Patrimoine net des administrations publiques", unite: "% du PIB", description: "actifs non financiers produits et non produits, valeur financière nette"}
    - {nom: "Dette détenue par les non-résidents et par la banque centrale", unite: "% du PIB et % de la dette", description: "dette de Maastricht par secteur détenteur"}
    - {nom: "Indicateur S2 et ses composantes", unite: "points de PIB", description: "position budgétaire initiale, coût du vieillissement"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/nama_10_nfa_bs/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/nasa_10_f_bs/default/table?lang=fr"
    - "https://data.ecb.europa.eu/data/datasets/GFS"
    - "https://webstat.banque-france.fr/fr/catalogue/det/DET.Q.FR.1315.F33000.M.Z9.8.F"
    - "https://economy-finance.ec.europa.eu/publications/debt-sustainability-monitor-2025_en"
    - "https://www.cor-retraites.fr/rapports-du-cor/rapport-annuel-cor-juin-2026-evolutions-perspectives-retraites-france"
  mots: ["dette publique", "générations futures", "investissement public", "patrimoine public", "détention de la dette", "non-résidents", "retraites", "indicateur S2", "Eurostat", "BCE"]
  fichiers: ["dette_generations.csv", "dette_generations.json"]
faq:
  - question: "La dette publique pèse-t-elle sur les générations futures ?"
    answer: "Elle leur laisse une charge, et ce qui a été acquis en même temps. En France, de {gen.a0} à {gen.fin}, {gen.part_k} % des déficits publics ont correspondu, dans les comptes, à un accroissement net des actifs publics comptabilisés, {gen.part_t} % à des transferts en capital vers d'autres secteurs et {gen.part_e} % à des dépenses courantes que les recettes courantes ne couvraient pas ; le patrimoine net des administrations publiques est passé de {gen.pn0} % à {gen.pn1} % du PIB de {gen.s0} à {gen.s1}. C'est une composition comptable, non une mesure de la charge entre générations ; et ce que les dépenses courantes ont produit, en éducation ou en santé, n'est pas compté comme un actif."
  - question: "« On se la doit à nous-mêmes » : est-ce vrai pour la France ?"
    answer: "Pour {gen.res_fin} % de la dette seulement : en {gen.h_fin}, {gen.nr_fin} % de la dette des administrations publiques était détenue par des non-résidents, contre {gen.nr0} % en {gen.h0} (BCE). La part détenue en France a été soutenue par les achats de la Banque de France, qui en détenait {gen.bc_max} % en {gen.bc_max_annee} et {gen.bc_fin} % en {gen.h_fin}. Et la part détenue dans le pays n'est pas neutre pour autant : son service implique des paiements, financés par les ressources publiques, à ceux qui détiennent les titres."
  - question: "Le vrai fardeau, ce sont les retraites ?"
    answer: "Pas selon l'indicateur de soutenabilité de long terme de la Commission européenne : l'ajustement permanent qui stabiliserait la dette française vaut {gen.s2} points de PIB, dont {gen.ibp} au titre de la position budgétaire présente et {gen.coa} au titre du vieillissement ({gen.dsm_lib}), et la position présente reste le premier terme dans les scénarios de risque de la Commission. Le Conseil d'orientation des retraites projette des dépenses de retraite plus élevées ; un ordre de grandeur, qui n'est pas un calcul de même nature, laisse le même classement, sauf à cumuler cette trajectoire avec le scénario de risque de la Commission sur la santé et la dépendance."
  - question: "Une dette qui finance de l'investissement est-elle un fardeau ?"
    answer: "Moins qu'une autre : emprunter pour acquérir un actif laisse le capital avec la charge. C'est pourquoi l'usage est le bon critère. En France, la part des déficits qui a correspondu, dans les comptes, à un accroissement net des actifs publics est passée de {gen.d1_part} % ({gen.d1_lib}) à {gen.d2_part} % ({gen.d2_lib}) puis {gen.d3_part} % ({gen.d3_lib})."
  - question: "Quel est le lien avec le cadre anthropique ?"
    answer: "La dette publique est un cas type de transfert temporel : un coût présent peut être reporté vers des payeurs futurs qui n'ont pas pris part à la décision. Le cadre y ajoute une hypothèse sociale : à l'intérieur de chaque génération, l'ajustement peut peser davantage sur les groupes les moins mobiles, fiscalement ou géographiquement — une hypothèse qui se teste réforme par réforme. L'analyse est formalisée dans AWP-03 (DOI 10.5281/zenodo.19268769), mise à l'épreuve des comptes dans AWP-09 (DOI 10.5281/zenodo.23143030), et déployée dans le livre Dette Publique : Qui paie vraiment ? (2025)."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 40
  nature: "Séries officielles (Eurostat, BCE, Commission européenne, COR) et calculs de l'auteur"
  prolongement: true   # option B : rangée « Prolongements du dossier », sous la grille des volets
dossier_dette: prolongement   # panneau « Prolongements » de la barre du dossier (A+ v2, 03/10/2026)
dossier_dette_titre: "Un fardeau pour les générations futures ?"
dossier_dette_role: "actifs, détention, retraites"
dossier_dette_titre_en: "A burden for future generations?"
dossier_dette_role_en: "assets passed on, holders, pensions"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Mise à jour&nbsp;: {{< gen-val "date_donnees" >}}</span> Administrations publiques, séries Eurostat et BCE de {{< gen-val "h0" >}} à {{< gen-val "fin" >}}&nbsp;; Commission européenne et COR, projections. Télécharger&nbsp;: <a href="/dette_generations.csv">CSV</a> · <a href="/dette_generations.json">JSON</a> · <a href="#sources">méthode</a></p>

## À quoi les déficits ont correspondu dans les comptes {#actifs}

<figure class="figure-ciseau">
  <img src="/img/dette-generations-actifs.svg" alt="Quatre barres horizontales, chacune représentant cent pour cent du besoin de financement des administrations publiques françaises sur une période : {{< gen-val "d1_lib" >}}, {{< gen-val "d1_part" >}} % en actifs ; {{< gen-val "d2_lib" >}}, {{< gen-val "d2_part" >}} % ; {{< gen-val "d3_lib" >}}, {{< gen-val "d3_part" >}} % ; sur l'ensemble, {{< gen-val "part_k" >}} % en actifs, {{< gen-val "part_t" >}} % en transferts en capital et {{< gen-val "part_e" >}} % en dépenses courantes non couvertes." width="720" height="352" loading="lazy">
  <figcaption>Part du besoin de financement des administrations publiques françaises qui a correspondu à des actifs, à des transferts en capital et à des dépenses courantes non couvertes, par décennie (Eurostat, calcul de l'auteur).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< gen-val "a0" >}} à {{< gen-val "fin" >}}, le besoin de financement des administrations publiques françaises a totalisé {{< gen-val "b" >}} points de PIB&nbsp;: {{< gen-val "k" >}} ont correspondu à un accroissement net de leurs actifs comptabilisés ({{< gen-val "part_k" >}}&nbsp;%), {{< gen-val "t" >}} à des transferts en capital vers d'autres secteurs, et {{< gen-val "e" >}}, près des deux tiers, à des dépenses courantes que leurs recettes courantes ne couvraient pas. C'est une lecture comptable&nbsp;: elle dit à quoi les déficits ont correspondu, non ce qu'ils ont produit.

</div>

L'argument le plus solide pour dire qu'une dette ne pèse pas sur ceux qui viennent est celui de l'actif transmis&nbsp;: une dette contractée pendant qu'on construit une route, une école ou un réseau lègue un capital en même temps qu'une charge. Les comptes nationaux permettent de le mettre à l'épreuve, parce que le déficit public — le besoin de financement des administrations — s'y décompose exactement en trois emplois. L'argent public étant fongible, cette décomposition ne dit pas quel euro emprunté a payé quelle dépense&nbsp;: elle dit à quoi, globalement, le déficit a correspondu. Les **acquisitions nettes d'actifs**&nbsp;: l'investissement, moins l'usure du capital existant, plus les achats nets de terrains et les variations de stocks — seul ce surplus accroît le patrimoine. Les **transferts en capital nets**&nbsp;: aides à l'investissement versées à d'autres secteurs, moins les recettes en capital, droits de succession compris. Et la **désépargne**&nbsp;: les dépenses courantes, usure du capital comprise, que les recettes courantes ne couvrent pas.

**La part investie a baissé de décennie en décennie**&nbsp;: {{< gen-val "d1_part" >}}&nbsp;% de {{< gen-val "d1_lib" >}}, {{< gen-val "d2_part" >}}&nbsp;% de {{< gen-val "d2_lib" >}}, {{< gen-val "d3_part" >}}&nbsp;% de {{< gen-val "d3_lib" >}}. Sur la dernière décennie, les acquisitions nettes d'actifs n'ont représenté que {{< gen-val "d3_k_moy" >}} point de PIB par an en moyenne, pour un besoin de financement de {{< gen-val "d3_b" >}} points en dix ans. En trente ans, les recettes courantes n'ont couvert les dépenses courantes que {{< gen-val "ep_pos_n" >}} années, en {{< gen-val "ep_pos_lib" >}}, et aucune année les acquisitions d'actifs n'ont égalé le besoin de financement.

Une partie des transferts correspond bien à du capital, mais détenu ailleurs&nbsp;: les aides à l'investissement versées aux entreprises, aux ménages ou aux organismes hors du champ des administrations ont totalisé {{< gen-val "d92" >}} points de PIB sur la période. Les compter toutes comme un capital acquis porterait la part à {{< gen-val "part_max" >}}&nbsp;% au plus&nbsp;: toujours moins de la moitié.

**Le bilan va dans le même sens.** De {{< gen-val "s0" >}} à {{< gen-val "s1" >}}, le patrimoine net des administrations publiques — tous leurs actifs non financiers, produits ou non, moins leurs dettes nettes de leurs actifs financiers — est passé de {{< gen-val "pn0" >}}&nbsp;% à {{< gen-val "pn1" >}}&nbsp;% du PIB, et il baisse quelle que soit l'année de départ retenue parmi les seize premières de la série. Leurs actifs produits ont à peine bougé ({{< gen-val "prod_var" >}} point), leur valeur financière nette a reculé de {{< gen-val "bf_var_abs" >}} points, et c'est principalement la hausse de la valeur des terrains ({{< gen-val "terr_var" >}} points), qui ne doit rien aux déficits, qui a limité la baisse. Contre-calcul descriptif&nbsp;: sans cette hausse, la baisse aurait été de {{< gen-val "pn_hors_terr" >}} points de PIB.

**La France n'est pas un cas extrême.** De {{< gen-val "cp_a0" >}} à {{< gen-val "fin" >}}, même calcul pour les {{< gen-val "cp_n" >}} pays de l'Union. Parmi les {{< gen-val "cp_groupe_n" >}} dont le besoin de financement cumulé a atteint {{< gen-val "cp_seuil" >}} points de PIB, la part des acquisitions nettes d'actifs a atteint au moins la moitié dans {{< gen-val "cp_sup_n" >}} — {{< gen-val "cp_sup_pays" >}} —, et elle a été plus faible qu'en France ({{< gen-val "cp_fr_part" >}}&nbsp;%) dans {{< gen-val "cp_inf_n" >}}, dont l'Allemagne et l'Italie. {{< gen-val "cp_exc_pays_maj" >}}, proches de l'équilibre ou en excédent sur la période, ne se comparent pas sur ce ratio.

<details class="repli"><summary>Les {{< gen-val "cp_n" >}} pays, emploi par emploi</summary>

{{< gen-tableau >}}

</details>

## «&nbsp;On se la doit à nous-mêmes&nbsp;»&nbsp;? {#detention}

L'argument classique d'Abba Lerner suppose que la dette soit détenue dans le pays&nbsp;: la servir reviendrait alors à prélever sur des contribuables nationaux pour payer des épargnants nationaux, et la génération qui paie serait aussi celle qui encaisse. Pour la France, cette prémisse ne vaut plus que pour {{< gen-val "res_fin" >}}&nbsp;% de la dette.

<figure class="figure-ciseau">
  <img src="/img/dette-generations-detention.svg" alt="Aires empilées de {{< gen-val "h0" >}} à {{< gen-val "h_fin" >}}, en pourcentage de la dette des administrations publiques : Banque de France, autres résidents, non-résidents. Les non-résidents passent de {{< gen-val "nr0" >}} % à {{< gen-val "nr_fin" >}} %, avec un maximum de {{< gen-val "nr_max" >}} % en {{< gen-val "nr_max_annee" >}} ; la Banque de France monte à {{< gen-val "bc_max" >}} % en {{< gen-val "bc_max_annee" >}} puis redescend à {{< gen-val "bc_fin" >}} %." width="720" height="352" loading="lazy">
  <figcaption>Part de la dette des administrations publiques détenue par les non-résidents, la Banque de France et les autres résidents (BCE, statistiques de finances publiques).</figcaption>
</figure>

En {{< gen-val "h0" >}}, {{< gen-val "nr0" >}}&nbsp;% de la dette des administrations publiques était détenue par des non-résidents. La part a dépassé la moitié en {{< gen-val "nr_maj_premiere" >}}, l'est restée {{< gen-val "nr_maj_n" >}} années sur {{< gen-val "nr_maj_tot" >}} depuis, et a culminé à {{< gen-val "nr_max" >}}&nbsp;% en {{< gen-val "nr_max_annee" >}}. La Banque de France est alors devenue un détenteur majeur, à la faveur des programmes d'achats de titres publics de l'Eurosystème&nbsp;: {{< gen-val "bc0" >}}&nbsp;% de la dette en {{< gen-val "h0" >}}, {{< gen-val "bc_max" >}}&nbsp;% en {{< gen-val "bc_max_annee" >}}. Depuis, ses avoirs refluent — {{< gen-val "bc_fin" >}}&nbsp;% en {{< gen-val "h_fin" >}}, soit {{< gen-val "bc_var" >}} points de moins — et la part des non-résidents a monté de {{< gen-val "nr_var_bc" >}} points, à {{< gen-val "nr_fin" >}}&nbsp;%. Depuis {{< gen-val "bc10_premiere" >}}, la Banque de France détient plus du dixième de la dette, et la progression de ses avoirs a compensé le recul de la part des autres résidents&nbsp;: ceux-ci, qui en détenaient {{< gen-val "ar_avant" >}}&nbsp;% en {{< gen-val "an_avant" >}}, n'en détiennent plus que {{< gen-val "ar_fin" >}}&nbsp;% en {{< gen-val "h_fin" >}}.

La Banque de France publie la même mesure sur un autre champ, celui que suit l'Agence France Trésor&nbsp;: les seuls titres négociables de l'État, en valeur de marché. Fin {{< gen-val "h_fin" >}}, {{< gen-val "etat_fin" >}}&nbsp;% de ces titres étaient détenus par des non-résidents, contre {{< gen-val "etat_0" >}}&nbsp;% fin {{< gen-val "etat_a0" >}}&nbsp;; la part a culminé à {{< gen-val "etat_max" >}}&nbsp;% en {{< gen-val "etat_max_annee" >}}, est retombée à {{< gen-val "etat_min" >}}&nbsp;% en {{< gen-val "etat_min_annee" >}}, au plus fort des achats de la banque centrale, et remonte depuis&nbsp;: {{< gen-val "etat_der" >}}&nbsp;% au {{< gen-val "etat_der_trim" >}}, dernière observation publiée par l'Agence France Trésor d'après la Banque de France. Malgré leurs périmètres et leurs valorisations différents, les deux séries convergent sur trois faits&nbsp;: une majorité non résidente aujourd'hui, un creux au moment des achats de la banque centrale, une remontée depuis.

La résidence comptée ici est celle du détenteur enregistré — un fonds, un dépositaire —, non celle de l'épargnant final&nbsp;: un fonds étranger peut gérer l'épargne de ménages français, et inversement. Surtout, la part détenue dans le pays n'est pas neutre pour autant&nbsp;: son service implique des paiements, financés par les ressources publiques, à ceux qui détiennent les titres&nbsp;; ces séries ne disent pas qui en supporte ni qui en reçoit finalement la charge nette. Ailleurs, la prémisse de Lerner est mieux vérifiée qu'en France, en Italie ({{< gen-val "h_it" >}}&nbsp;% de dette détenue par des non-résidents en {{< gen-val "h_fin" >}}) ou en Suède ({{< gen-val "h_se" >}}&nbsp;%)&nbsp;; elle l'est moins en Autriche ({{< gen-val "h_at" >}}&nbsp;%) ou en Belgique ({{< gen-val "h_be" >}}&nbsp;%).

## Le vrai fardeau est-il dans les retraites&nbsp;? {#vieillissement}

Un troisième argument déplace la question&nbsp;: la dette visible serait secondaire, le vrai fardeau tiendrait aux retraites et au vieillissement. L'indicateur de soutenabilité de long terme de la Commission européenne, dit S2, permet de le mettre à l'épreuve. Il mesure l'ajustement permanent du solde primaire structurel qui stabiliserait la dette à horizon infini, et le partage en deux termes&nbsp;: la position budgétaire de départ, et le coût projeté du vieillissement — retraites, santé, dépendance, éducation.

<figure class="figure-ciseau">
  <img src="/img/dette-generations-vieillissement.svg" alt="Barres horizontales par scénario de la Commission, en points de PIB : position budgétaire présente {{< gen-val "ibp" >}} et vieillissement {{< gen-val "coa" >}} dans le scénario de base ; {{< gen-val "ibp_prod" >}} et {{< gen-val "coa_prod" >}} avec une productivité plus faible ; {{< gen-val "ibp_risque" >}} et {{< gen-val "coa_risque" >}} dans le scénario de risque sur la santé et la dépendance ; {{< gen-val "ibp_prec" >}} et {{< gen-val "coa_prec" >}} dans l'édition précédente." width="720" height="322" loading="lazy">
  <figcaption>Ajustement qui stabiliserait la dette française, partagé entre la position budgétaire présente et le coût du vieillissement, selon la Commission européenne (trois scénarios et édition précédente).</figcaption>
</figure>

Pour la France, dans le *{{< gen-val "dsm_lib" >}}*, S2 vaut {{< gen-val "s2" >}} points de PIB&nbsp;: {{< gen-val "ibp" >}} au titre de la position budgétaire présente, {{< gen-val "coa" >}} au titre du vieillissement. Les retraites y comptent pour {{< gen-val "pen" >}} point — la Commission projette une dépense de pensions en baisse dans le PIB, nette des prélèvements qui la frappent —, la santé et la dépendance pour {{< gen-val "hc_ltc" >}}, l'éducation pour {{< gen-val "edu" >}}. La position présente reste le premier terme dans les deux scénarios de risque de la Commission, y compris celui qui alourdit la santé et la dépendance (vieillissement&nbsp;: {{< gen-val "coa_risque" >}} points, contre {{< gen-val "ibp_risque" >}}). Et l'indicateur sait montrer l'inverse&nbsp;: dans {{< gen-val "pays_coa_n" >}} pays de l'Union sur {{< gen-val "pays_n" >}}, dont la Belgique, l'Espagne et le Luxembourg, le vieillissement l'emporte sur la position de départ.

Qui parle compte ici. La Commission est l'institution qui fait appliquer les règles budgétaires européennes, et sa projection des retraites françaises suppose la réforme de 2023 appliquée&nbsp;; sa composante «&nbsp;pensions&nbsp;» est nette des impôts et cotisations payés par les retraités. Le Conseil d'orientation des retraites, instance pluraliste qui réunit partenaires sociaux, parlementaires et administrations, projette dans son scénario de référence ({{< gen-val "cor_lib" >}}) une dépense de retraite brute passant de {{< gen-val "cor_dep0" >}}&nbsp;% du PIB en {{< gen-val "cor_a0" >}} à {{< gen-val "cor_dep1" >}}&nbsp;% en {{< gen-val "cor_a1" >}}, soit {{< gen-val "cor_var" >}} point, là où la Commission retient une baisse.

**Un ordre de grandeur, non une composante de S2.** Si l'on remplace, à titre purement illustratif, la composante «&nbsp;pensions&nbsp;» de la Commission par cette variation du COR — deux grandeurs de nature différente, une valeur actualisée nette d'un côté, une variation brute entre deux dates de l'autre —, le coût du vieillissement passerait à {{< gen-val "coa_cor" >}} point, toujours moins que la position présente ({{< gen-val "ibp" >}}). Le même exercice, cumulé avec le scénario de risque de la Commission sur la santé et la dépendance, inverserait l'ordre ({{< gen-val "coa_cor_risque" >}} points contre {{< gen-val "ibp_risque" >}}). Ce calcul de l'auteur indique une sensibilité&nbsp;; il ne remplace pas l'indicateur.

**Deux projections, deux jeux d'hypothèses.** Le COR établit la sienne sur les nouvelles projections démographiques de l'Insee, avec une fécondité plus basse et un solde migratoire plus élevé que dans ses rapports précédents, et souligne combien son diagnostic financier en dépend&nbsp;; la Commission reprend les projections du vieillissement de son rapport de 2024, établies avant elles. Le COR suppose aussi, pour l'Agirc-Arrco, une revalorisation du point moins freinée à partir de 2038 que dans ses rapports antérieurs, ce qui relève la dépense projetée. Une partie de l'écart entre les deux institutions peut donc tenir à leurs hypothèses, et non à la seule situation financière du système de retraite.

Le déficit que le COR projette pour le système de retraite, {{< gen-val "cor_solde1" >}} points de PIB en {{< gen-val "cor_a1" >}}, tient d'ailleurs autant à la baisse projetée de ses ressources, de {{< gen-val "cor_res0" >}}&nbsp;% à {{< gen-val "cor_res1" >}}&nbsp;% du PIB, qu'à la hausse de ses dépenses. Ces chiffres sont des projections conditionnelles&nbsp;: ils ne disent pas que les retraites ne posent aucun problème, mais que l'effort qu'exige la dette française tient d'abord à l'écart présent entre ses recettes et ses dépenses.

## Ce que ces données ne disent pas {#limites}

- **Ce que les dépenses courantes ont produit.** La comptabilité nationale ne compte pas comme actifs l'éducation, la santé ou la recherche non capitalisée&nbsp;: une part des dépenses courantes laisse aux générations suivantes un capital humain que ces séries ne voient pas. La page juge l'argument sur le champ des actifs comptabilisés, non la valeur de toute dépense.
- **La charge entre générations.** La composition comptable des déficits n'est pas, à elle seule, une mesure de ce que chaque génération paie et reçoit sur sa vie&nbsp;: c'est l'objet de la comptabilité générationnelle, que ces séries ne construisent pas.
- **Une causalité.** Les emplois du besoin de financement disent à quoi les déficits ont correspondu dans les comptes, non pourquoi ils ont existé, ni ce qui se serait passé sans eux.
- **Le détenteur final.** La résidence est celle du détenteur enregistré, non celle de l'épargnant final. La série des administrations publiques est en valeur nominale, celle des titres négociables de l'État en valeur de marché&nbsp;: leurs niveaux ne se comparent pas point par point.
- **L'avenir.** S2 et les projections du COR sont des scénarios conditionnels à leurs hypothèses (démographie, productivité, législation), produits par deux institutions aux mandats différents&nbsp;; ils ne se valident pas par l'observation.
- **La répartition à l'intérieur d'une génération.** Aucune de ces séries ne dit qui, dans une même génération, paie et reçoit&nbsp;: c'est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)

## La lecture anthropique&nbsp;: de la question du volume à celle de la répartition {#anthropie}

Le cadre anthropique ne tranche pas la controverse macroéconomique — il y ajoute une question. La dette publique est un cas type de **transfert temporel**&nbsp;: un coût présent peut être reporté vers des payeurs qui n'ont pas participé aux arbitrages. Personne ne vote «&nbsp;contre&nbsp;» les générations futures&nbsp;; on vote des budgets dont une part des coûts leur reviendra, et cette part n'est jamais présentée sous ce nom. Les comptes de cette page en documentent deux dimensions observables pour la France&nbsp;: la faible part des déficits qui a correspondu à un accroissement net des actifs comptabilisés, et une dette aujourd'hui majoritairement détenue hors du pays.

Il y ajoute une hypothèse que le débat en volume ignore&nbsp;: **à l'intérieur de chaque génération, l'ajustement peut peser inégalement**. Les ménages mobiles — fiscalement, géographiquement — disposent de capacités d'évitement que les groupes les moins mobiles n'ont pas&nbsp;; si l'ajustement suit la ligne de moindre résistance, ce sont eux qui le portent, par l'impôt, les tarifs ou les services. L'hypothèse se teste sur des réformes précises, avec des groupes définis d'avance&nbsp;; elle serait affaiblie par un ajustement portant surtout sur d'autres groupes, ou par des compensations accordées aux perdants. De même, un budget contraint par le service de la dette peut reporter l'investissement écologique&nbsp;; là où ce report est établi, les mêmes héritiers reçoivent la dette financière et le désordre climatique différé.

Le working paper [AWP-09](/awp/awp-09/) rend le verdict de ces comptes sur la lecture de l'AWP-03&nbsp;: le report vers les générations suivantes y est soutenu dans un périmètre patrimonial, celui des actifs comptabilisés, sans que la charge finale de chaque génération soit établie.

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="le critère de l'usage et le recul de l'investissement sont retrouvés&nbsp;; lire la détention par des résidents comme une absence de fardeau, ou la composition des déficits comme une mesure de la charge entre générations, est mis en danger" >}}
**Mesuré ici.** Les emplois du besoin de financement des administrations publiques françaises et européennes, le patrimoine des administrations, la détention de la dette par secteur, sur les séries d'Eurostat et de la BCE&nbsp;; la décomposition de l'indicateur S2, reprise de la Commission. Aucun des textes lus ne calcule ces grandeurs sur ces sources et ces périodes&nbsp;: elles se valident par reproduction.

**Cohérent avec.** Le critère de l'usage&nbsp;: dans le modèle de Diamond, émettre de la dette pour acquérir du capital public fait de l'État un simple intermédiaire entre épargnants et entrepreneurs, sans effet de court ni de long terme. Le recul de la part investie&nbsp;: dans 21 pays de l'OCDE, dont la France, de 1979 à 2003, une charge d'intérêts plus lourde va de pair, cinq ans plus tard, avec une part de l'investissement public plus faible et une part des retraites plus forte, reporter un investissement coûtant moins, politiquement, que réduire un droit (Breunig et Busemeyer). Ce sont des associations dans un panel, sur une autre période&nbsp;: elles ne disent pas pourquoi la part investie a baissé en France depuis. La démarche de l'indicateur S2, enfin, est celle que réclament Auerbach, Gokhale et Kotlikoff&nbsp;: partir de la contrainte budgétaire de l'État sur un horizon long et des dépenses liées à l'âge, plutôt que du déficit d'une année.

**Mis en danger par.** Toute lecture de la décomposition des déficits comme une mesure de la charge entre générations. Pour Auerbach, Gokhale et Kotlikoff, le déficit mesuré n'a, en théorie, aucune relation nécessaire avec la position de la politique budgétaire entre générations&nbsp;: il dépend de la façon dont on étiquette recettes et dépenses. Ils lui substituent des comptes générationnels, qui chiffrent ce que chaque génération paie et reçoit sur le reste de sa vie&nbsp;; pour les États-Unis de 1989, à politique inchangée, ils trouvaient une charge nette d'environ 20&nbsp;% plus lourde pour les générations futures que pour les nouveau-nés. D'où la limite de la page&nbsp;: sa décomposition dit la composition comptable des déficits, non la charge de chaque génération. Toute lecture, aussi, selon laquelle seule la part détenue par des non-résidents pèserait sur les générations suivantes. Dans le cas efficace du modèle de Diamond, où le taux d'intérêt dépasse la croissance de la population, la dette intérieure abaisse **davantage** le bien-être de long terme que la dette extérieure, parce qu'elle prend la place du capital productif dans les patrimoines. Chez Blanchard, même une dette que l'on fait rouler sans jamais relever l'impôt réduit l'accumulation de capital&nbsp;; dans le cas qu'il juge le plus représentatif, le bien-être monte pour la première génération et baisse généralement ensuite, des calculs qu'il dit lui-même trop rudimentaires pour une estimation. Barro soutient l'inverse&nbsp;: des parents altruistes compenseraient la charge par leurs transferts volontaires, à condition que ces transferts soient opérants pour la plupart des gens&nbsp;; il reconnaît qu'en 1989 la majorité des économistes penche vers les modèles où la dette pèse.

**Non établi.** L'ampleur de l'éviction du capital en France, et la valeur de ce que les dépenses courantes ont transmis&nbsp;: aucun des cinq textes ne les mesure.

**Références lues**

- Diamond, P. A. (1965), «&nbsp;National Debt in a Neoclassical Growth Model&nbsp;», *American Economic Review*, 55(5), p.&nbsp;1126-1150.
- Auerbach, A. J., Gokhale, J. et Kotlikoff, L. J. (1991), «&nbsp;Generational Accounts&nbsp;: A Meaningful Alternative to Deficit Accounting&nbsp;», *Tax Policy and the Economy*, 5, p.&nbsp;55-110.
- Barro, R. J. (1989), «&nbsp;The Ricardian Approach to Budget Deficits&nbsp;», *Journal of Economic Perspectives*, 3(2), p.&nbsp;37-54.
- Blanchard, O. (2019), «&nbsp;Public Debt and Low Interest Rates&nbsp;», *American Economic Review*, 109(4), p.&nbsp;1197-1229 (lu dans sa version de document de travail du PIIE, n°&nbsp;19-4).
- Breunig, C. et Busemeyer, M. R. (2012), «&nbsp;Fiscal austerity and the trade-off between public investment and social spending&nbsp;», *Journal of European Public Policy*, 19(6), p.&nbsp;921-938.
{{< /confrontation-recherche >}}

<div class="retenir">

## Ce qu'il faut retenir {#retenir}

Une dette ne laisse pas seulement une charge&nbsp;: elle laisse aussi ce qui a été acquis en même temps. En France, sur trente ans, les acquisitions nettes d'actifs comptabilisés n'ont correspondu qu'à {{< gen-val "part_k" >}}&nbsp;% des déficits, et cette part a baissé de décennie en décennie, jusqu'à {{< gen-val "d3_part" >}}&nbsp;% de {{< gen-val "d3_lib" >}}. Le patrimoine net des administrations publiques a reculé de {{< gen-val "pn0" >}}&nbsp;% à {{< gen-val "pn1" >}}&nbsp;% du PIB.

«&nbsp;On se la doit à nous-mêmes&nbsp;» ne vaut que pour {{< gen-val "res_fin" >}}&nbsp;% de la dette, une part soutenue depuis {{< gen-val "bc10_premiere" >}} par les achats de la banque centrale, et qui reflue avec eux. Et même détenue dans le pays, son service implique des paiements, financés par les ressources publiques, aux détenteurs de titres.

Le vieillissement n'est pas, selon l'indicateur de la Commission, ce qui rend la dette française difficile à stabiliser&nbsp;: c'est l'écart présent entre recettes et dépenses ({{< gen-val "ibp" >}} points de PIB, contre {{< gen-val "coa" >}} pour le vieillissement), dans tous ses scénarios.

Ces comptes ne disent ni ce que les dépenses courantes ont produit, ni qui, dans chaque génération, portera l'ajustement&nbsp;: c'est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)
- [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Et ailleurs&nbsp;?](/dette-publique-comparaison-internationale/)
- [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page documente trois dimensions de la dette française&nbsp;: ce à quoi les déficits ont correspondu dans les comptes, qui détient la dette, et d'où vient l'effort de stabilisation mesuré par la Commission. Reste à savoir qui, dans chaque génération, portera cet effort&nbsp;: le contribuable, l'usager des services publics, l'épargnant par l'inflation, le créancier par une restructuration&nbsp;? Le livre prolonge cette analyse, chiffres officiels à l'appui, en examinant ces choix et leurs conséquences.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Emplois du besoin de financement.** Eurostat, administrations publiques (S.13), comptes SEC 2010, en monnaie nationale (`gov_10a_main`)&nbsp;: capacité ou besoin de financement (B9), épargne nette (B8N), formation brute de capital fixe (P51G), consommation de capital fixe (P51C), acquisitions moins cessions d'actifs non produits (NP), variation des stocks (P52_P53), transferts en capital versés et reçus (D9), dont aides à l'investissement versées (D92). Chaque année, besoin de financement = désépargne nette + acquisitions nettes d'actifs + transferts en capital nets&nbsp;; l'identité est vérifiée année par année, à 0,05 point près. Les ratios sont calculés sur le PIB publié avec la notification de déficit et de dette (`gov_10dd_edpt1`) et cumulés par période en points de PIB&nbsp;; la part en actifs calculée en euros courants donne {{< gen-val "part_k_eur" >}}&nbsp;%, contre {{< gen-val "part_k" >}}&nbsp;% en points de PIB. Sans les terrains ni les stocks, l'investissement net seul représente {{< gen-val "part_n" >}}&nbsp;% du besoin de financement.

**Patrimoine.** Actifs non financiers des administrations publiques, produits et non produits (`nama_10_nfa_bs`, N1N et N2N, prix courants), dont terrains (N211N), et valeur financière nette consolidée (`nasa_10_f_bs`, BF90), rapportés au PIB. Les stocks d'actifs sont évalués aux prix courants&nbsp;: leurs variations mêlent flux et réévaluations.

**Détention.** BCE, statistiques de finances publiques (GFS)&nbsp;: dette de Maastricht des administrations publiques par zone de contrepartie (reste du monde, résidents) et secteur détenteur (banque centrale). Contrôles&nbsp;: non-résidents et résidents égalent la dette totale chaque année&nbsp;; sur les années communes, les valeurs égalent celles d'Eurostat (`gov_10dd_ggd`), transmises par le même déclarant. Témoin de périmètre&nbsp;: {{< gen-val "etat_lib" >}}, sur Webstat (part des titres négociables de l'État détenue par des non-résidents, en valeur de marché, fin de trimestre&nbsp;; fichier de la page publique de la série, dernière observation publiée le {{< gen-val "etat_maj" >}}, archivé avec son empreinte)&nbsp;; dernière observation&nbsp;: graphique de l'Agence France Trésor (source Banque de France), relevé le {{< gen-val "etat_der_lu" >}} avec l'empreinte de l'image, et contrôlé contre Webstat sur la période commune. Le script s'arrête si les deux séries cessent de converger, ou si Webstat publie une période que le relevé ne dépasse plus.

**Indicateur S2.** Commission européenne, *{{< gen-val "dsm_lib" >}}*, tableaux par pays (fichier de l'édition, archivé avec son empreinte)&nbsp;: les composantes reprises sont celles du tableur&nbsp;; le tableau 3.2 du rapport imprime la position initiale comme la différence entre S2 et le coût du vieillissement, d'où {{< gen-val "ibp_pdf" >}} au lieu de {{< gen-val "ibp" >}} pour la France. **Retraites.** COR, {{< gen-val "cor_lib" >}}, données de la synthèse, scénario de référence&nbsp;; règle d'indexation de l'Agirc-Arrco&nbsp;: partie 1, chapitre 2 du rapport. La substitution illustrative de la trajectoire du COR à la composante «&nbsp;pensions&nbsp;» de la Commission est un calcul de l'auteur, hors méthode de S2.

Contrôle&nbsp;: pour chaque pays et chaque année, les ratios calculés sont comparés à ceux qu'Eurostat publie en pourcentage du PIB, que le calcul n'utilise pas. Au-delà de {{< gen-val "tolerance" >}} point d'écart, l'année est écartée et comptée ({{< gen-val "cons_ecartees" >}} sur {{< gen-val "cons_calculables" >}})&nbsp;; pour la France, le script s'arrête. Aucun chiffre de cette page n'est saisi à la main&nbsp;: tous viennent du même script, qui vérifie les principales affirmations chiffrées et s'arrête si leurs conditions ne sont plus remplies&nbsp;; leur formulation fait l'objet d'une relecture éditoriale. Les arguments ont été mis à l'épreuve avant l'écriture de la page, selon un protocole fixé avant le calcul.

{{< reutiliser figures="figures_generations" jeu="dette_generations" sources="Eurostat, BCE, Commission européenne, COR" donnees="Les emplois du besoin de financement des administrations publiques (France par décennie, 27 pays de l'Union), le patrimoine des administrations publiques, la détention de la dette par secteur et l'indicateur S2 de la Commission ; le même contenu existe en CSV, au format long." >}}
De {{< gen-val "a0" >}} à {{< gen-val "fin" >}}, {{< gen-val "part_k" >}}&nbsp;% du besoin de financement des administrations publiques françaises a correspondu, dans les comptes, à un accroissement net de leurs actifs comptabilisés, et {{< gen-val "part_e" >}}&nbsp;% à des dépenses courantes non couvertes par les recettes courantes&nbsp;; la part investie est passée de {{< gen-val "d1_part" >}}&nbsp;% ({{< gen-val "d1_lib" >}}) à {{< gen-val "d3_part" >}}&nbsp;% ({{< gen-val "d3_lib" >}}). En {{< gen-val "h_fin" >}}, {{< gen-val "nr_fin" >}}&nbsp;% de la dette publique était détenue par des non-résidents. C'est une lecture comptable, non une attribution causale.
{{< /reutiliser >}}
