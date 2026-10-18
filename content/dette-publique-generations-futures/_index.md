---
title: "La dette publique est-elle un fardeau pour les générations futures ?"
description: "Depuis {gen.a0}, {gen.part_k} % seulement des déficits publics français ont correspondu, dans les comptes, à un accroissement net des actifs publics comptabilisés ({gen.d3_part} % sur {gen.d3_lib}). La page éprouve aussi « on se la doit à nous-mêmes » et « le véritable fardeau viendra du vieillissement », sans calculer de facture par génération. Séries Eurostat, BCE et Commission européenne recalculées et contrôlées."
chapo: "Une dette peut laisser aux générations suivantes une charge, mais aussi des écoles, des routes et d'autres équipements. Que montrent les comptes français ? De {gen.a0} à {gen.fin}, {gen.part_k} % seulement des déficits publics ont correspondu à des actifs publics nouveaux (équipements, bâtiments, terrains), usure déduite ; cette part est tombée à {gen.d3_part} % sur {gen.d3_lib}. Le capital humain que peuvent laisser l'enseignement ou la santé n'y figure pas : ce chiffre dit à quoi les déficits ont correspondu, non ce qu'ils ont produit. Deux autres arguments méritent examen : « nous nous devons la dette à nous-mêmes » et « le véritable fardeau viendra du vieillissement ». Trois tests les éprouvent, sans prétendre calculer la facture de chaque génération."
date: 2026-07-24
lastmod: 2026-10-11
og_title: "La dette est-elle un fardeau pour les générations futures ? — S. Lalut"
og_image: "images/og-dette-generations.jpg"
og_image_alt: "Carte de partage : « À quoi ont correspondu trente ans de déficits ? » — France, part des déficits publics qui a correspondu, dans les comptes, à des actifs, par décennie, et le reste à des dépenses courantes non couvertes."
# Refonte du 03/10/2026 en ressource de données, sur le modèle du dossier dette (plan de diffusion d'octobre, § 5).
# Test décisif avant la page, protocole écrit avant le calcul : D:\PRO\06_PROMOTION\RECHERCHE_GENERATIONS_FUTURES_2026-10-03\test_decisif\
# Contre-expertise PRO-20261003-195656, arbitrée le 03/10 : jamais « financé », « transmis », « couvert » pour la décomposition.
# Phase B de la refonte (11/10/2026, ARBITRAGE_CE_GENERATIONS_PHASE_A.md) : trois éclairages partiels, aucun n'est une facture ;
# bilan en complément replié ; S2 lu comme position de départ + effet des variations futures des dépenses liées à l'âge ;
# substitution chiffrée COR -> S2 retirée. Gardes de texte dans le générateur (bilan hors conclusion, vocabulaire).
# Aucun chiffre saisi : jetons {gen.*} et shortcodes gen-val / gen-tableau (scripts/update_dette_generations.py).
donnees: [dette_generations]
journal:  # révisions qui changent la lecture de la page (partials/page-date-visible.html affiche la plus récente)
  - {date: 2026-10-18, texte: "Ajout : où le recul de l'investissement net s'est produit, administrations locales et autres administrations, avec son point bas de 2016."}
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
    - {nom: "Indicateur S2 et ses composantes", unite: "points de PIB", description: "position budgétaire initiale, effet des variations futures des dépenses liées à l'âge"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/nama_10_nfa_bs/default/table?lang=fr"
    - "https://www.insee.fr/fr/statistiques/8988859"
    - "https://ec.europa.eu/eurostat/databrowser/view/nasq_10_f_bs/default/table?lang=fr"
    - "https://data.ecb.europa.eu/data/datasets/GFS"
    - "https://webstat.banque-france.fr/fr/catalogue/det/DET.Q.FR.1315.F33000.M.Z9.8.F"
    - "https://economy-finance.ec.europa.eu/publications/debt-sustainability-monitor-2025_en"
    - "https://www.cor-retraites.fr/rapports-du-cor/rapport-annuel-cor-juin-2026-evolutions-perspectives-retraites-france"
  mots: ["dette publique", "générations futures", "investissement public", "patrimoine public", "détention de la dette", "non-résidents", "retraites", "indicateur S2", "Eurostat", "BCE"]
  fichiers: ["dette_generations.csv", "dette_generations.json"]
faq:
  - question: "La dette publique pèse-t-elle sur les générations futures ?"
    answer: "Elle leur laisse une charge, et ce qui a été acquis en même temps ; aucune statistique ne mesure à elle seule le solde des deux. En France, de {gen.a0} à {gen.fin}, {gen.part_k} % des déficits publics ont correspondu, dans les comptes, à un accroissement net des actifs publics comptabilisés, {gen.part_t} % à des transferts en capital vers d'autres secteurs et {gen.part_e} % à des dépenses courantes que les recettes courantes ne couvraient pas. C'est une composition comptable : elle ne mesure ni ce que chaque génération paiera, ni ce que les dépenses courantes, en éducation ou en santé, ont produit."
  - question: "Une dette contractée pour investir pèse-t-elle moins ?"
    answer: "Elle laisse un capital en même temps qu'une charge : c'est pourquoi l'usage est un critère pertinent, qui ne dit pas pour autant ce que rapportent les dépenses. En France, la part des déficits qui a correspondu, dans les comptes, à un accroissement net des actifs publics est passée de {gen.d1_part} % ({gen.d1_lib}) à {gen.d2_part} % ({gen.d2_lib}), puis à {gen.d3_part} % ({gen.d3_lib}). Ces parts ne mesurent ni la rentabilité des dépenses ni leur utilité pour les générations futures."
  - question: "« On se la doit à nous-mêmes » : est-ce vrai pour la France ?"
    answer: "En {gen.h_fin}, {gen.res_fin} % de la dette des administrations publiques était enregistrée comme détenue par des résidents et {gen.nr_fin} % par des non-résidents (BCE) : l'hypothèse d'une dette entièrement détenue dans le pays ne décrit pas la France. Cette statistique dit la résidence des détenteurs enregistrés, non le fardeau : elle ne mesure ni la charge nette laissée aux générations suivantes, ni la position extérieure nette du pays. Et une dette détenue dans le pays n'est pas indolore pour autant."
  - question: "Les retraites sont-elles le vrai fardeau ?"
    answer: "L'indicateur S2 de la Commission européenne ne répond pas à cette question sous cette forme. Il évalue à {gen.s2} points de PIB l'ajustement permanent qui stabiliserait la dette française, dont {gen.ibp} pour la position budgétaire de départ, qui contient la dépense de retraite actuelle, et {gen.coa} pour l'évolution future des dépenses liées à l'âge ({gen.dsm_lib}). Ce faible second terme ne dit pas que les retraites coûtent peu ; et le Conseil d'orientation des retraites projette une dépense de retraite en hausse, là où la Commission retient une baisse."
  - question: "Que paieront concrètement les générations futures ?"
    answer: "Ces séries ne permettent pas de chiffrer une facture par enfant : il faudrait connaître les politiques à venir. Une dette se renouvelle sans qu'une génération précise la rembourse en entier ; elle peut appeler des ajustements futurs d'impôts ou de dépenses, peser sur l'accumulation de capital, ou s'accompagner d'actifs et de services dont bénéficieront les suivants. Son poids dépend aussi de l'écart entre le taux d'intérêt que paie l'État et la croissance de l'économie."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif", "explicatif-causal"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 40
  nature: "Séries officielles (Eurostat, Insee, BCE, Commission européenne, COR) et calculs de l'auteur"
  prolongement: true   # option B : rangée « Prolongements du dossier », sous la grille des volets
dossier_dette: prolongement   # panneau « Prolongements » de la barre du dossier (A+ v2, 03/10/2026)
dossier_dette_titre: "Un fardeau pour les générations futures ?"
dossier_dette_role: "actifs, détention, retraites"
dossier_dette_titre_en: "A burden for future generations?"
dossier_dette_role_en: "assets, holders, pensions"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< gen-val "date_donnees" >}}</span> Administrations publiques, séries Eurostat, Insee et BCE de {{< gen-val "h0" >}} à {{< gen-val "fin" >}}&nbsp;; Commission européenne et COR, projections. Télécharger&nbsp;: <a href="/dette_generations.csv">CSV</a> · <a href="/dette_generations.json">JSON</a> · <a href="#sources">méthode</a></p>

## À quoi les déficits ont correspondu dans les comptes {#actifs}

Emprunter pour construire une école, une route ou un réseau laisse un capital en même temps qu'une dette. C'est un argument essentiel pour en apprécier le poids sur les générations futures&nbsp;: encore faut-il savoir ce qui a été acquis et ce que cela apportera. Les comptes nationaux répondent à la première question.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-generations-actifs-m.svg" width="300" height="747">
    <img src="/img/dette-generations-actifs.svg" alt="Quatre barres horizontales, chacune représentant cent pour cent du besoin de financement des administrations publiques françaises sur une période : {{< gen-val "d1_lib" >}}, {{< gen-val "d1_part" >}} % en actifs ; {{< gen-val "d2_lib" >}}, {{< gen-val "d2_part" >}} % ; {{< gen-val "d3_lib" >}}, {{< gen-val "d3_part" >}} % ; sur l'ensemble, {{< gen-val "part_k" >}} % en actifs, {{< gen-val "part_t" >}} % en transferts en capital et {{< gen-val "part_e" >}} % en dépenses courantes non couvertes par les recettes courantes." width="720" height="385" loading="lazy">
  </picture>
  <figcaption>Part du besoin de financement des administrations publiques françaises qui a correspondu à des actifs, à des transferts en capital et à des dépenses courantes non couvertes, par décennie (Eurostat, calcul de l'auteur).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< gen-val "a0" >}} à {{< gen-val "fin" >}}, {{< gen-val "part_k" >}}&nbsp;% seulement des déficits publics français ont correspondu à un accroissement net des actifs publics comptabilisés, et {{< gen-val "part_e" >}}&nbsp;%, près des deux tiers, à des dépenses courantes que les recettes courantes ne couvraient pas&nbsp;; la part en actifs est tombée de {{< gen-val "d1_part" >}}&nbsp;% sur {{< gen-val "d1_lib" >}} à {{< gen-val "d3_part" >}}&nbsp;% sur {{< gen-val "d3_lib" >}}. C'est une lecture comptable&nbsp;: elle dit à quoi les déficits ont correspondu, non ce qu'ils ont produit.

</div>

Chaque année, le déficit public se décompose exactement en trois emplois. Les **acquisitions nettes d'actifs**&nbsp;: les équipements, terrains et stocks publics en plus, une fois déduite l'usure de ceux qui existent. Les **transferts en capital**, {{< gen-val "part_t" >}}&nbsp;% du total&nbsp;: des aides versées à d'autres, entreprises, ménages ou organismes, pour qu'ils investissent, moins les recettes du même type. Les **dépenses courantes non couvertes**&nbsp;: la part des dépenses courantes (fonctionnement, prestations sociales, intérêts…) que les recettes courantes ne couvraient pas. L'argent public n'étant pas affecté à une dépense précise, cette décomposition ne dit pas quel euro emprunté a payé quelle dépense&nbsp;: elle dit à quoi, globalement, le déficit a correspondu.

<details class="repli"><summary>Les trois emplois en termes comptables, et ce que valent les montants cumulés</summary>

Les acquisitions nettes d'actifs sont l'investissement, moins l'usure du capital existant, plus les achats nets de terrains et les variations de stocks&nbsp;; seul ce surplus accroît le patrimoine public. Les transferts en capital nets sont les aides à l'investissement versées à d'autres secteurs, moins les recettes en capital, droits de succession compris. Les dépenses courantes non couvertes sont l'excédent des dépenses courantes, usure du capital comprise, sur les recettes courantes, ce que les comptables appellent la désépargne.

Les parts se lisent directement. Les montants, eux, additionnent des besoins de financement annuels, chacun rapporté au PIB de son année&nbsp;: les {{< gen-val "b" >}} points de PIB cumulés de {{< gen-val "a0" >}} à {{< gen-val "fin" >}} ne sont ni {{< gen-val "b" >}}&nbsp;% du PIB de {{< gen-val "fin" >}}, ni la hausse du ratio de dette sur la période. Les aides à l'investissement versées aux entreprises, aux ménages ou aux organismes hors du champ des administrations ont totalisé {{< gen-val "d92" >}} points de PIB cumulés sur la période.

</details>

**La part en actifs a baissé de décennie en décennie**, de {{< gen-val "d1_part" >}}&nbsp;% à {{< gen-val "d2_part" >}}&nbsp;%, puis à {{< gen-val "d3_part" >}}&nbsp;%, et ces deux reculs ne relèvent pas du même mouvement comptable. De la première décennie à la deuxième, la part a reculé surtout parce que le besoin de financement cumulé a augmenté, de {{< gen-val "d1_b" >}} à {{< gen-val "d2_b" >}} points de PIB, alors que les acquisitions nettes d'actifs restaient presque stables ({{< gen-val "d1_k" >}} puis {{< gen-val "d2_k" >}} points)&nbsp;; de la deuxième à la troisième, le besoin est resté presque identique ({{< gen-val "d3_b" >}} points) et les acquisitions nettes ont diminué presque de moitié ({{< gen-val "d3_k" >}} points). Sur la dernière décennie, les acquisitions nettes d'actifs n'ont représenté que {{< gen-val "d3_k_moy_pt" >}} de PIB par an en moyenne. En trente ans, les recettes courantes n'ont dépassé les dépenses courantes que {{< gen-val "ep_pos_n" >}} années, en {{< gen-val "ep_pos_lib" >}}, et aucune année les acquisitions d'actifs n'ont égalé le besoin de financement. Même en comptant comme un capital acquis toutes les aides à l'investissement versées hors des administrations, la part atteindrait {{< gen-val "part_max" >}}&nbsp;% au plus&nbsp;: toujours moins de la moitié.

**Où ce recul s'est produit.** Les comptes ne disent pas pourquoi la part investie a baissé, mais ils disent où. L'investissement net des administrations publiques, investissement moins usure du capital, sans les terrains ni les stocks, est passé de {{< gen-val "inv_d2_pt" >}} de PIB par an en moyenne sur {{< gen-val "d2_lib" >}} à {{< gen-val "inv_d3_pt" >}} sur {{< gen-val "d3_lib" >}}. Un peu plus de la moitié de ce recul, {{< gen-val "inv_loc_var_pt" >}} sur {{< gen-val "inv_var_pt" >}}, vient des administrations locales&nbsp;; le reste, de l'État et des autres administrations. Il n'a pas été continu&nbsp;: l'investissement net local touche son point bas en {{< gen-val "inv_creux_an" >}}, à {{< gen-val "inv_creux_pt" >}} de PIB, quand les collectivités n'investissaient guère plus que l'usure de leurs équipements, puis remonte à {{< gen-val "inv_loc_fin_pt" >}} en {{< gen-val "fin" >}}. Ce point bas tombe pendant la baisse des dotations de l'État que décrit la page [Les collectivités locales sont-elles une variable d'ajustement&nbsp;?](/dette-publique-collectivites-locales/)&nbsp;; la coïncidence des dates ne prouve pas que l'une explique l'autre.{{< gen-val "inv_ccf_note" >}}

**Ce que cette part ne mesure pas.** Que {{< gen-val "part_k" >}}&nbsp;% seulement des déficits correspondent à des actifs comptabilisés ne veut pas dire que les {{< gen-val "part_hors_k" >}}&nbsp;% restants n'ont rien produit. Les comptes enregistrent des contreparties, non tous les bénéfices&nbsp;: l'éducation, la santé ou la recherche non capitalisée sont des dépenses courantes, qui peuvent laisser aux générations suivantes un capital humain que ces séries ne comptent pas. Ces parts ne disent pas non plus ce que les dépenses ont rapporté, ni si un déficit de récession, qui étale l'effort dans le temps, était justifié.

**Ni universel ni exceptionnel.** Le même calcul, appliqué aux {{< gen-val "cp_n" >}} pays de l'Union sur une fenêtre commune de {{< gen-val "cp_a0" >}} à {{< gen-val "fin" >}}, place la France à {{< gen-val "cp_fr_part" >}}&nbsp;% (contre {{< gen-val "part_k" >}}&nbsp;% sur {{< gen-val "a0" >}}-{{< gen-val "fin" >}}&nbsp;: la différence tient à la fenêtre). Parmi les {{< gen-val "cp_groupe_n" >}} pays dont le besoin de financement cumulé a atteint {{< gen-val "cp_seuil" >}} points de PIB, la part des actifs a atteint au moins la moitié dans {{< gen-val "cp_sup_n" >}}, dont {{< gen-val "cp_cite_sup" >}}&nbsp;; elle a été plus faible qu'en France dans {{< gen-val "cp_inf_n" >}}, dont {{< gen-val "cp_cite_inf" >}}. La composition des déficits n'est donc pas une fatalité commune à tous les États.

<details class="repli"><summary>Les {{< gen-val "cp_n" >}} pays, emploi par emploi</summary>

{{< gen-tableau >}}

{{< gen-val "cp_exc_pays_maj" >}}, dont le besoin cumulé est resté sous ce seuil ou négatif, ne se comparent pas sur ce ratio.

</details>

<details class="repli"><summary>Le bilan des administrations publiques&nbsp;: un complément, non une preuve</summary>

Le bilan des administrations publiques semble offrir une confirmation&nbsp;: de {{< gen-val "s0" >}} à {{< gen-val "s1" >}}, leur patrimoine net — tous leurs actifs non financiers, produits ou non, moins leurs dettes nettes de leurs actifs financiers — est passé de {{< gen-val "pn0" >}}&nbsp;% à {{< gen-val "pn1" >}}&nbsp;% du PIB. Mais ce stock dépend des deux années que l'on compare. Il atteignait {{< gen-val "pn_haut" >}}&nbsp;% en {{< gen-val "pn_haut_annee" >}}, était encore au-dessus de son niveau de départ en {{< gen-val "pn_sup_annee" >}} ({{< gen-val "pn_sup" >}}&nbsp;%), et il a augmenté de {{< gen-val "pn_d3_var_pt" >}} de {{< gen-val "pn_d3_an0" >}} à {{< gen-val "s1" >}}, décennie où la part des déficits correspondant à des actifs est tombée à {{< gen-val "d3_part" >}}&nbsp;%. Sur les {{< gen-val "pn_fen_n" >}} comparaisons possibles entre deux années distantes d'au moins dix ans, {{< gen-val "pn_fen_hausse" >}} le montrent en hausse.

Ses variations mêlent flux et réévaluations. La valeur des terrains a varié de {{< gen-val "terr_var_pt" >}} de PIB sur la période, sans rapport avec les déficits&nbsp;; même les actifs produits, qui n'ont varié que de {{< gen-val "prod_var_pt" >}}, sont des stocks évalués aux prix courants et rapportés au PIB, sensibles aux prix comme au dénominateur. Une identité de flux, vérifiée année par année, ne se valide pas par un stock dont les variations obéissent aussi à d'autres mécanismes&nbsp;: le bilan reste ici une information complémentaire.

</details>

## «&nbsp;On se la doit à nous-mêmes&nbsp;»&nbsp;? {#detention}

L'argument classique de l'économiste Abba Lerner suppose que la dette soit détenue dans le pays&nbsp;: la servir reviendrait alors à prélever sur des contribuables nationaux pour payer des épargnants nationaux, et la génération qui paie serait aussi celle qui encaisse. La statistique de détention permet d'en vérifier la prémisse, non la conclusion.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-generations-detention-m.svg" width="300" height="605">
    <img src="/img/dette-generations-detention.svg" alt="Aires empilées de {{< gen-val "h0" >}} à {{< gen-val "h_fin" >}}, en pourcentage de la dette des administrations publiques : Banque de France, autres résidents, non-résidents. Les non-résidents passent de {{< gen-val "nr0" >}} % à {{< gen-val "nr_fin" >}} %, avec un maximum de {{< gen-val "nr_max" >}} % en {{< gen-val "nr_max_annee" >}} ; la Banque de France monte à {{< gen-val "bc_max" >}} % en {{< gen-val "bc_max_annee" >}} puis redescend à {{< gen-val "bc_fin" >}} %." width="720" height="381" loading="lazy">
  </picture>
  <figcaption>Part de la dette des administrations publiques détenue par les non-résidents, la Banque de France et les autres résidents (BCE, statistiques de finances publiques).</figcaption>
</figure>

En {{< gen-val "h_fin" >}}, {{< gen-val "nr_fin" >}}&nbsp;% de la dette publique française était enregistrée comme détenue par des non-résidents, et {{< gen-val "res_fin" >}}&nbsp;% par des résidents (BCE). Parmi ces derniers, la Banque de France en détenait {{< gen-val "bc_fin" >}}&nbsp;% du total, et les autres résidents {{< gen-val "ar_fin" >}}&nbsp;%. La Banque de France est mise à part parce que son rôle n'est pas celui d'un créancier privé ordinaire&nbsp;: ses avoirs ont fortement augmenté avec les achats de titres publics de l'Eurosystème, avant de refluer. Avec plus de la moitié de la dette détenue par des non-résidents, l'hypothèse d'une dette entièrement détenue dans le pays ne décrit pas la situation française. Elle décrit mieux l'Italie ({{< gen-val "h_it" >}}&nbsp;% de dette détenue par des non-résidents en {{< gen-val "h_fin" >}}) ou la Suède ({{< gen-val "h_se" >}}&nbsp;%), moins bien l'Autriche ({{< gen-val "h_at" >}}&nbsp;%) ou la Belgique ({{< gen-val "h_be" >}}&nbsp;%).

Il n'en a pas toujours été ainsi. En {{< gen-val "h0" >}}, {{< gen-val "nr0" >}}&nbsp;% de la dette était détenue par des non-résidents&nbsp;; la part a dépassé la moitié en {{< gen-val "nr_maj_premiere" >}} et l'est restée {{< gen-val "nr_maj_n" >}} années sur {{< gen-val "nr_maj_tot" >}} depuis. Avec ces achats, la Banque de France est devenue un détenteur majeur, jusqu'à {{< gen-val "bc_max" >}}&nbsp;% de la dette en {{< gen-val "bc_max_annee" >}}&nbsp;; depuis, ses avoirs refluent et la part des non-résidents a augmenté de {{< gen-val "nr_var_bc" >}} points. Le volet [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/#creanciers) répartit les titres de l'État par détenteur, et la page [L'inflation a-t-elle vraiment allégé la dette française&nbsp;?](/inflation-et-dette-publique/#detenteurs) dit qui détenait la dette quand l'inflation en a réduit la valeur réelle.

<details class="repli"><summary>Les détenteurs année par année, et le champ des titres de l’État</summary>

La part des non-résidents a culminé à {{< gen-val "nr_max" >}}&nbsp;% en {{< gen-val "nr_max_annee" >}}. La Banque de France détenait {{< gen-val "bc0" >}}&nbsp;% de la dette en {{< gen-val "h0" >}}&nbsp;; depuis {{< gen-val "bc10_premiere" >}}, elle en détient plus du dixième, et la progression de ses avoirs a compensé le recul des autres résidents, passés de {{< gen-val "ar_avant" >}}&nbsp;% en {{< gen-val "an_avant" >}} à {{< gen-val "ar_fin" >}}&nbsp;% en {{< gen-val "h_fin" >}}. En {{< gen-val "h_fin" >}}, elle en détenait {{< gen-val "bc_var" >}} points de moins qu'en {{< gen-val "bc_max_annee" >}}.

Sur le seul champ des titres négociables de l'État, en valeur de marché, la Banque de France décrit le même mouvement&nbsp;: {{< gen-val "etat_fin" >}}&nbsp;% de non-résidents fin {{< gen-val "h_fin" >}}, un creux à {{< gen-val "etat_min" >}}&nbsp;% en {{< gen-val "etat_min_annee" >}}, au plus fort des achats de la banque centrale, et {{< gen-val "etat_der" >}}&nbsp;% au {{< gen-val "etat_der_trim" >}} selon l'Agence France Trésor. La série des administrations publiques est en valeur nominale, celle des titres négociables de l'État en valeur de marché&nbsp;: leurs niveaux ne se comparent pas point par point.

</details>

**Ce que la statistique de détention n'établit pas.** Elle dit où sont enregistrés les créanciers, non qui porte la charge. Elle n'établit ni la résidence de chaque épargnant final, puisqu'un fonds étranger peut gérer l'épargne de ménages français et inversement&nbsp;; ni la charge nette laissée aux générations suivantes&nbsp;; ni la position extérieure nette de la France, puisque les résidents détiennent aussi des créances sur l'étranger&nbsp;; ni les effets de la dette sur le capital, les revenus et la croissance. Une dette détenue dans le pays n'est pas neutre pour autant&nbsp;: son service suppose des paiements, prélevés sur les ressources publiques, au profit de ceux qui détiennent les titres. Et une dette détenue au-dehors n'est pas, mécaniquement, une perte nette égale à sa valeur.

## Le vieillissement à venir pèse-t-il davantage que le déséquilibre budgétaire actuel&nbsp;? {#vieillissement}

Le troisième argument tient la dette visible pour secondaire&nbsp;: le véritable fardeau viendrait du vieillissement. La Commission européenne permet de l'éprouver avec son indicateur S2&nbsp;: l'amélioration permanente du budget, hors intérêts de la dette, qui stabiliserait à long terme la dette rapportée au PIB, sans que la date ni le niveau de cette stabilisation soient fixés à l'avance. Pour stabiliser sa dette à long terme, la France devrait ainsi, selon les hypothèses de la Commission (*{{< gen-val "dsm_lib" >}}*), améliorer durablement son budget de {{< gen-val "s2_pt" >}} de PIB.

Sur ces {{< gen-val "s2_pt" >}}, {{< gen-val "ibp_pt" >}} correspondent à la **position budgétaire de départ**, c'est-à-dire à l'écart entre le budget actuel et celui qui stabiliserait la dette, et {{< gen-val "coa_pt" >}} à l'effet des **variations futures des dépenses liées à l'âge** (retraites, santé, dépendance, éducation), que la Commission nomme «&nbsp;coût du vieillissement&nbsp;».

**Un faible effet de l'évolution future ne dit pas que les retraites coûtent peu.** La dépense de retraite actuelle, {{< gen-val "cor_dep0" >}}&nbsp;% du PIB en {{< gen-val "cor_a0" >}} en dépense brute selon le Conseil d'orientation des retraites (COR), est déjà comptée dans la position de départ&nbsp;; le second terme ne mesure que son évolution projetée, ajoutée à celle des autres dépenses liées à l'âge.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-generations-vieillissement-m.svg" width="300" height="829">
    <img src="/img/dette-generations-vieillissement.svg" alt="Barres horizontales par scénario de la Commission, en points de PIB, avec le total S2 : scénario de base, S2 {{< gen-val "s2" >}}, position de départ {{< gen-val "ibp" >}} et effet des variations futures des dépenses liées à l'âge {{< gen-val "coa" >}} ; productivité plus faible, S2 {{< gen-val "s2_prod" >}}, {{< gen-val "ibp_prod" >}} et {{< gen-val "coa_prod" >}} ; risque santé et dépendance, S2 {{< gen-val "s2_risque" >}}, {{< gen-val "ibp_risque" >}} et {{< gen-val "coa_risque" >}} ; édition précédente, autre jeu de projections, S2 {{< gen-val "s2_prec" >}}, {{< gen-val "ibp_prec" >}} et {{< gen-val "coa_prec" >}}." width="720" height="411" loading="lazy">
  </picture>
  <figcaption>Ajustement qui stabiliserait la dette française (indicateur S2), partagé entre la position budgétaire de départ et l'effet des variations futures des dépenses liées à l'âge, selon la Commission européenne (trois scénarios et édition précédente).</figcaption>
</figure>

**Le résultat dépend des hypothèses.** Dans le scénario de risque où la Commission retient des dépenses de santé et de dépendance plus fortes, l'effet des variations futures des dépenses liées à l'âge atteint {{< gen-val "coa_risque_pt" >}}, contre {{< gen-val "coa_pt" >}} dans le scénario de base&nbsp;; S2 y atteint {{< gen-val "s2_risque_pt" >}}. La position de départ y reste pourtant le premier terme, comme dans le scénario d'une productivité plus faible. L'indicateur sait montrer l'inverse&nbsp;: dans {{< gen-val "pays_coa_n" >}} pays de l'Union sur {{< gen-val "pays_n" >}}, dont la Belgique, l'Espagne et le Luxembourg, l'évolution future des dépenses liées à l'âge pèse davantage que la position de départ.

Le COR projette, lui, une dépense de retraite en hausse dans le PIB, là où la Commission en retient une baisse&nbsp;: les deux projections reposent sur des hypothèses différentes et ne se comparent pas directement.

<details class="repli"><summary>Définition technique de S2, et le second terme poste par poste</summary>

S2 est l'amélioration permanente du solde primaire structurel (le solde hors intérêts, corrigé de la conjoncture), engagée en {{< gen-val "s2_an" >}}, qui stabiliserait la dette sur un horizon infini. À la différence de l'indicateur S1, qui vise {{< gen-val "s1_cible" >}}&nbsp;% du PIB en {{< gen-val "s1_horizon" >}}, il ne fixe ni le niveau auquel la dette se stabilise ni la date. La position budgétaire de départ est l'écart entre le solde structurel de départ et celui qui stabiliserait le ratio.

L'effet des variations futures des dépenses liées à l'âge est faible parce qu'il additionne des mouvements contraires. La Commission projette une dépense de pensions en baisse dans le PIB ({{< gen-val "pen_pt" >}}), nette des impôts et cotisations payés par les retraités, réforme de 2023 appliquée&nbsp;; la dépense de santé ({{< gen-val "sante_pt" >}}) et celle de dépendance ({{< gen-val "dep_pt" >}}) augmentent&nbsp;; celle d'éducation baisse ({{< gen-val "edu_pt" >}}).

</details>

<details class="repli"><summary>Commission et COR&nbsp;: deux projections, deux jeux d’hypothèses</summary>

**Qui parle compte ici.** La Commission est l'institution qui fait appliquer les règles budgétaires européennes. Le COR, instance pluraliste qui réunit partenaires sociaux, parlementaires et administrations, projette dans son scénario de référence ({{< gen-val "cor_lib" >}}) une dépense de retraite brute passant de {{< gen-val "cor_dep0" >}}&nbsp;% du PIB en {{< gen-val "cor_a0" >}} à {{< gen-val "cor_dep1" >}}&nbsp;% en {{< gen-val "cor_a1" >}}, soit {{< gen-val "cor_var_pt" >}}, là où la Commission retient une baisse. Les deux chiffres ne se comparent pas terme à terme&nbsp;: l'un est une dépense brute entre deux dates, l'autre une composante nette. Leur écart, qui peut tenir aux hypothèses de chaque institution, montre combien la projection en dépend&nbsp;; il ne donne pas un autre S2.

Le COR établit sa projection sur les nouvelles projections démographiques de l'Insee, avec une fécondité plus basse et un solde migratoire plus élevé que dans ses rapports précédents, et souligne combien son diagnostic financier en dépend&nbsp;; la Commission reprend les projections du vieillissement de son rapport de 2024, établies avant elles. Le COR suppose aussi, pour l'Agirc-Arrco, une revalorisation du point moins freinée à partir de 2038 que dans ses rapports antérieurs, ce qui relève la dépense projetée. Une partie de l'écart entre les deux institutions peut donc tenir à leurs hypothèses, et non à la seule situation financière du système de retraite.

Le déficit que le COR projette pour le système de retraite, {{< gen-val "cor_deficit1_pt" >}} de PIB en {{< gen-val "cor_a1" >}}, tient autant à la baisse projetée de ses ressources, de {{< gen-val "cor_res0" >}}&nbsp;% à {{< gen-val "cor_res1" >}}&nbsp;% du PIB, qu'à la hausse de ses dépenses. Ce sont des projections conditionnelles à leurs hypothèses.

L'édition précédente de la Commission ({{< gen-val "dsm_prec_an" >}}) donnait {{< gen-val "ibp_prec" >}} pour la position de départ et {{< gen-val "coa_prec" >}} pour l'évolution future des dépenses liées à l'âge&nbsp;: c'est un autre jeu de projections, non une évolution observée.

</details>

<details class="repli"><summary>S2 n’est pas l’écart calculé dans une autre page du dossier</summary>

La page [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/#solde-stabilisant) mesure un écart de grandeur voisine&nbsp;: {{< gen-val "v5_ecart_pt" >}} de PIB en {{< gen-val "v5_annee" >}}, contre {{< gen-val "s2_pt" >}} pour S2. Le premier porte sur le solde observé d'une année&nbsp;; le second est un ajustement permanent, qui inclut l'évolution projetée des dépenses liées à l'âge. Les deux nombres ne sont ni deux estimations interchangeables, ni la validation l'un de l'autre.

- **Valeur.** Volet 5&nbsp;: {{< gen-val "v5_ecart_pt" >}} de PIB en {{< gen-val "v5_annee" >}}. S2&nbsp;: {{< gen-val "s2_pt" >}} de PIB ({{< gen-val "dsm_lib" >}}).
- **Nature.** Volet 5&nbsp;: solde primaire observé, une année. S2&nbsp;: solde primaire structurel, ajustement permanent à partir de {{< gen-val "s2_an" >}}.
- **Horizon.** Volet 5&nbsp;: stabiliser le ratio cette année-là, aux taux et à la croissance de l'année. S2&nbsp;: stabiliser la dette sur un horizon infini, sans niveau ni date fixés.
- **Dépenses liées à l'âge à venir.** Volet 5&nbsp;: non projetées. S2&nbsp;: évolution projetée incluse.

</details>

**Ce que S2 ne dit pas.** Il ne dit ni quelles dépenses ni quelles recettes devraient changer, ni si les retraites posent un problème&nbsp;: c'est une projection conditionnelle à ses hypothèses.

## Pourquoi aucun de ces chiffres n'est une facture {#facture}

Les trois tests répondent à trois questions distinctes. La composition des déficits dit à quoi ils ont correspondu dans les comptes&nbsp;; la détention dit où sont enregistrés les créanciers&nbsp;; S2 dit quel ajustement stabiliserait la dette, sous des hypothèses. Aucun ne mesure ce que chaque génération paiera et recevra sur sa vie&nbsp;: c'est l'objet de la comptabilité générationnelle, que ces séries ne construisent pas.

**Que paieront concrètement mes enfants&nbsp;?** Aucune de ces séries ne permet de chiffrer une facture par enfant&nbsp;: il faudrait connaître les politiques à venir. Elles éclairent en revanche les mécanismes par lesquels une dette pèse, ou non, sur ceux qui viennent. Une dette se renouvelle&nbsp;: l'État rembourse les titres qui arrivent à échéance en en émettant d'autres, et aucune génération précise ne la rembourse en entier. Elle peut appeler des ajustements futurs, impôts plus élevés ou dépenses moindres, si le solde ne la stabilise pas. Elle peut peser sur le capital, si l'épargne qui s'y place cesse de s'investir ailleurs. Et elle a pu s'accompagner d'actifs et de services dont les générations suivantes bénéficient&nbsp;: les routes et les écoles comptées ici, l'éducation et la santé qui ne le sont pas.

Le poids d'un même stock dépend enfin de l'écart entre le taux d'intérêt que paie l'État et la croissance de l'économie. Quand le taux dépasse la croissance, stabiliser le ratio de dette exige un excédent primaire&nbsp;; quand il lui est inférieur, un déficit primaire peut le laisser stable. La page [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/#soutenable) mesure cet écart pour la France.

## Ce que ces données ne disent pas {#limites}

- **Ce que les dépenses courantes ont produit.** La page juge l'argument sur le champ des actifs comptabilisés, non la valeur de toute dépense.
- **Une causalité.** Les emplois du besoin de financement disent à quoi les déficits ont correspondu dans les comptes, non pourquoi ils ont existé, ni ce qui se serait passé sans eux.
- **Le détenteur final.** La résidence est celle du détenteur enregistré, non celle de l'épargnant final.
- **L'avenir.** S2 et les projections du COR sont des scénarios conditionnels à leurs hypothèses (démographie, productivité, législation), produits par deux institutions aux mandats différents&nbsp;; ils ne se valident pas par l'observation.
- **La répartition à l'intérieur d'une génération.** Aucune de ces séries ne dit qui, dans une même génération, paie et reçoit&nbsp;: c'est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)

## La lecture anthropique&nbsp;: qui décide aujourd'hui, qui devra s'adapter demain&nbsp;? {#anthropie}

Le [cadre anthropique](/quest-ce-que-lanthropie/) ne tranche pas la controverse macroéconomique&nbsp;; il déplace la question du volume de la dette vers la participation aux décisions et la répartition future des ajustements. Il tient en trois propositions.

1. Une génération peut engager des dépenses dont les conséquences concernent des personnes absentes de la décision&nbsp;: personne ne vote «&nbsp;contre&nbsp;» les générations futures&nbsp;; on vote des budgets dont une part des coûts leur reviendra.
2. Le transfert dans le temps ne détermine pas, à lui seul, qui supportera effectivement la charge&nbsp;: à l'intérieur de chaque génération, l'ajustement peut passer par l'impôt, les tarifs, les services ou l'épargne, et ne pas tomber sur les mêmes.
3. Les capacités inégales de mobilité, d'évitement ou de négociation peuvent influer sur cette répartition&nbsp;: les ménages mobiles, fiscalement ou géographiquement, disposent de marges que les moins mobiles n'ont pas.

La troisième proposition est une hypothèse réfutable, non un résultat de cette page. Elle se teste sur des réformes précises, avec des groupes définis d'avance&nbsp;; elle serait affaiblie par un ajustement portant surtout sur d'autres groupes, ou par des compensations accordées aux perdants. Elle est formalisée dans l'[AWP-03](/awp/awp-03/)&nbsp;; l'[AWP-09](/awp/awp-09/) confronte cette lecture aux comptes publics, sans établir la charge finale de chaque génération.

Reste la question que ces comptes laissent ouverte&nbsp;: ceux qui devront supporter les conséquences des décisions d'aujourd'hui disposeront-ils des mêmes possibilités de choix, d'adaptation et de protection que ceux qui en ont bénéficié&nbsp;?

{{< confrontation-recherche verifie="2026-10-03" publie="oui" resume="le critère de l'usage et le recul de l'investissement sont retrouvés&nbsp;; lire la détention par des résidents comme une absence de fardeau, ou la composition des déficits comme une mesure de la charge entre générations, est mis en danger" >}}
**Mesuré ici.** Les emplois du besoin de financement des administrations publiques françaises et européennes, le patrimoine des administrations, la détention de la dette par secteur, sur les séries d'Eurostat, de l'Insee et de la BCE&nbsp;; la décomposition de l'indicateur S2, reprise de la Commission. Aucun des textes lus ne calcule ces grandeurs sur ces sources et ces périodes&nbsp;: elles se valident par reproduction.

**Cohérent avec.** Le critère de l'usage&nbsp;: dans le modèle de Diamond, émettre de la dette pour acquérir du capital public fait de l'État un simple intermédiaire entre épargnants et entrepreneurs, sans effet de court ni de long terme. Le recul de la part investie&nbsp;: dans 21 pays de l'OCDE, dont la France, de 1979 à 2003, une charge d'intérêts plus lourde va de pair, cinq ans plus tard, avec une part de l'investissement public plus faible et une part des retraites plus forte, reporter un investissement coûtant moins, politiquement, que réduire un droit (Breunig et Busemeyer). Ce sont des associations dans un panel, sur une autre période&nbsp;: elles ne disent pas pourquoi la part investie a baissé en France depuis. La démarche de l'indicateur S2, enfin, est celle que réclament Auerbach, Gokhale et Kotlikoff&nbsp;: partir de la contrainte budgétaire de l'État sur un horizon long et des dépenses liées à l'âge, plutôt que du déficit d'une année.

**Mis en danger par.** Toute lecture de la décomposition des déficits comme une mesure de la charge entre générations. Pour Auerbach, Gokhale et Kotlikoff, le déficit mesuré n'a, en théorie, aucune relation nécessaire avec la position de la politique budgétaire entre générations&nbsp;: il dépend de la façon dont on étiquette recettes et dépenses. Ils lui substituent des comptes générationnels, qui chiffrent ce que chaque génération paie et reçoit sur le reste de sa vie&nbsp;; pour les États-Unis de 1989, à politique inchangée, ils trouvaient une charge nette d'environ 20&nbsp;% plus lourde pour les générations futures que pour les nouveau-nés. D'où la limite de la page&nbsp;: sa décomposition dit la composition comptable des déficits, non la charge de chaque génération. Toute lecture, aussi, selon laquelle seule la part détenue par des non-résidents pèserait sur les générations suivantes. Dans le cas efficace du modèle de Diamond, où le taux d'intérêt dépasse la croissance de la population, la dette intérieure abaisse **davantage** le bien-être de long terme que la dette extérieure, parce qu'elle prend la place du capital productif dans les patrimoines. Chez Blanchard, même une dette que l'on fait rouler sans jamais relever l'impôt réduit l'accumulation de capital&nbsp;; dans le cas qu'il juge le plus représentatif, le bien-être monte pour la première génération et baisse généralement ensuite, des calculs qu'il dit lui-même trop rudimentaires pour une estimation. Barro soutient l'inverse&nbsp;: des parents altruistes compenseraient la charge par leurs transferts volontaires, à condition que ces transferts soient opérants pour la plupart des gens&nbsp;; il reconnaît qu'en 1989 la majorité des économistes penche vers les modèles où la dette pèse.

**Non établi.** L'ampleur de l'éviction du capital en France, et la valeur de ce que les dépenses courantes ont produit pour les générations suivantes&nbsp;: aucun des cinq textes ne les mesure.

**Références lues**

- Diamond, P. A. (1965), «&nbsp;National Debt in a Neoclassical Growth Model&nbsp;», *American Economic Review*, 55(5), p.&nbsp;1126-1150.
- Auerbach, A. J., Gokhale, J. et Kotlikoff, L. J. (1991), «&nbsp;Generational Accounts&nbsp;: A Meaningful Alternative to Deficit Accounting&nbsp;», *Tax Policy and the Economy*, 5, p.&nbsp;55-110.
- Barro, R. J. (1989), «&nbsp;The Ricardian Approach to Budget Deficits&nbsp;», *Journal of Economic Perspectives*, 3(2), p.&nbsp;37-54.
- Blanchard, O. (2019), «&nbsp;Public Debt and Low Interest Rates&nbsp;», *American Economic Review*, 109(4), p.&nbsp;1197-1229 (lu dans sa version de document de travail du PIIE, n°&nbsp;19-4).
- Breunig, C. et Busemeyer, M. R. (2012), «&nbsp;Fiscal austerity and the trade-off between public investment and social spending&nbsp;», *Journal of European Public Policy*, 19(6), p.&nbsp;921-938.
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

**Ce qui résiste.** L'usage distingue les dettes entre elles, et la part française est basse&nbsp;: {{< gen-val "part_k" >}}&nbsp;% des déficits ont correspondu à des actifs comptabilisés depuis {{< gen-val "a0" >}}, {{< gen-val "d3_part" >}}&nbsp;% sur {{< gen-val "d3_lib" >}}, quand d'autres pays de l'Union dépassent la moitié. L'hypothèse d'une dette détenue dans le pays ne décrit pas la France&nbsp;: {{< gen-val "nr_fin" >}}&nbsp;% de la dette publique était enregistrée au nom de non-résidents en {{< gen-val "h_fin" >}}.

**Ce qui ne suffit pas.** Aucun de ces chiffres n'est une facture&nbsp;: la composition des déficits n'est pas une charge par génération, la résidence des créanciers n'est pas un transfert net, et S2 est une projection conditionnelle.

**Ce qu'on ne peut pas conclure.** Une dette qui correspond peu à des actifs comptabilisés n'est pas nécessairement une dette sans bénéfice. Une dette détenue dans le pays n'est pas nécessairement indolore. Un faible effet de l'évolution future des dépenses liées à l'âge n'implique pas une faible dépense actuelle de retraite.

Pour juger ce que la dette laisse aux générations futures, connaître son montant ne suffit pas&nbsp;: il faut savoir ce qui a été acquis en même temps, à qui elle est due, à quelles conditions elle se stabilise, et comment se répartiront les coûts et les bénéfices.

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
Cette page met trois arguments à l'épreuve des comptes&nbsp;: ce à quoi les déficits ont correspondu, qui détient la dette, et quel ajustement la stabiliserait selon la Commission. Reste à savoir qui, dans chaque génération, portera cet ajustement&nbsp;: le contribuable, l'usager des services publics, l'épargnant par l'inflation, le créancier par une restructuration&nbsp;? Le livre prolonge cette analyse, chiffres officiels à l'appui, en examinant ces choix et leurs conséquences.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Emplois du besoin de financement.** Eurostat, administrations publiques (S.13), comptes SEC 2010, en monnaie nationale (`gov_10a_main`)&nbsp;: capacité ou besoin de financement (B9), épargne nette (B8N), formation brute de capital fixe (P51G), consommation de capital fixe (P51C), acquisitions moins cessions d'actifs non produits (NP), variation des stocks (P52_P53), transferts en capital versés et reçus (D9), dont aides à l'investissement versées (D92). Chaque année, besoin de financement = désépargne nette + acquisitions nettes d'actifs + transferts en capital nets&nbsp;; l'identité est vérifiée année par année, à 0,05 point près. Les ratios sont calculés sur le PIB publié avec la notification de déficit et de dette (`gov_10dd_edpt1`) et cumulés par période en points de PIB&nbsp;; la part en actifs calculée en euros courants donne {{< gen-val "part_k_eur" >}}&nbsp;%, contre {{< gen-val "part_k" >}}&nbsp;% en points de PIB. Sans les terrains ni les stocks, l'investissement net seul représente {{< gen-val "part_n" >}}&nbsp;% du besoin de financement.

**Patrimoine.** Compte de patrimoine des administrations publiques de l'Insee (tableau 8.204, comptes nationaux annuels, base 2020, corrigé le 30&nbsp;juillet 2026, fichier archivé avec son empreinte)&nbsp;: actifs non financiers produits et non produits (N1N et N2N, prix courants), dont terrains (N211N), et valeur financière nette (actifs moins passifs financiers), rapportés au PIB. Deux témoins, qui doivent concorder sous peine d'arrêt&nbsp;: les actifs non financiers publiés par Eurostat (`nama_10_nfa_bs`) et la valeur financière nette trimestrielle d'Eurostat au quatrième trimestre (`nasq_10_f_bs`, BF90). Les stocks d'actifs sont évalués aux prix courants&nbsp;: leurs variations mêlent flux et réévaluations.

**Détention.** BCE, statistiques de finances publiques (GFS)&nbsp;: dette de Maastricht des administrations publiques par zone de contrepartie (reste du monde, résidents) et secteur détenteur (banque centrale). Contrôles&nbsp;: non-résidents et résidents égalent la dette totale chaque année&nbsp;; sur les années communes, les valeurs égalent celles d'Eurostat (`gov_10dd_ggd`), déclarées par la même administration. Témoin de périmètre&nbsp;: {{< gen-val "etat_lib" >}}, sur Webstat (part des titres négociables de l'État détenue par des non-résidents, en valeur de marché, fin de trimestre&nbsp;; fichier de la page publique de la série, dernière observation publiée le {{< gen-val "etat_maj" >}}, archivé avec son empreinte)&nbsp;; dernière observation&nbsp;: graphique de l'Agence France Trésor (source Banque de France), relevé le {{< gen-val "etat_der_lu" >}} avec l'empreinte de l'image, et contrôlé contre Webstat sur la période commune. Le script s'arrête si les deux séries cessent de converger, ou si Webstat publie une période que le relevé ne dépasse plus.

**Indicateur S2.** Commission européenne, *{{< gen-val "dsm_lib" >}}*, tableaux par pays (fichier de l'édition, archivé avec son empreinte)&nbsp;: les composantes reprises sont celles du tableur&nbsp;; le tableau 3.2 du rapport imprime la position initiale comme la différence entre S2 et le second terme, d'où {{< gen-val "ibp_pdf" >}} au lieu de {{< gen-val "ibp" >}} pour la France. Définitions de S2, de ses deux termes et de S1&nbsp;: section 3.1 et annexe A6 du rapport (Institutional Paper 332), relues pour cette page. **Volet 5.** L'écart au solde stabilisant est lu dans les données de [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)&nbsp;; le script s'arrête si l'année ou la valeur diffèrent. **Retraites.** COR, {{< gen-val "cor_lib" >}}, données de la synthèse, scénario de référence&nbsp;; règle d'indexation de l'Agirc-Arrco&nbsp;: partie 1, chapitre 2 du rapport.

Contrôle&nbsp;: pour chaque pays et chaque année, les ratios calculés sont comparés à ceux qu'Eurostat publie en pourcentage du PIB, que le calcul n'utilise pas. Au-delà de {{< gen-val "tolerance" >}} point d'écart, l'année est écartée et comptée ({{< gen-val "cons_ecartees" >}} sur {{< gen-val "cons_calculables" >}})&nbsp;; pour la France, le script s'arrête. Les chiffres calculés viennent tous du même script, qui vérifie les principales affirmations chiffrées et s'arrête si leurs conditions ne sont plus remplies&nbsp;; leur formulation fait l'objet d'une relecture éditoriale. Seule la dernière part des non-résidents, lue sur le graphique de l'Agence France Trésor, est transcrite à la main&nbsp;; le relevé du trimestre précédent est contrôlé contre Webstat. Les chiffres des études citées sont repris tels qu'elles les publient. Les arguments ont été mis à l'épreuve avant l'écriture de la page, selon un protocole fixé avant le calcul.

{{< reutiliser figures="figures_generations" jeu="dette_generations" sources="Eurostat, Insee, BCE, Commission européenne, COR" donnees="Les emplois du besoin de financement des administrations publiques (France par décennie, 27 pays de l'Union), le patrimoine des administrations publiques, la détention de la dette par secteur et l'indicateur S2 de la Commission ; le même contenu existe en CSV, au format long." >}}
De {{< gen-val "a0" >}} à {{< gen-val "fin" >}}, {{< gen-val "part_k" >}}&nbsp;% du besoin de financement des administrations publiques françaises a correspondu, dans les comptes, à un accroissement net de leurs actifs comptabilisés, et {{< gen-val "part_e" >}}&nbsp;% à des dépenses courantes non couvertes par les recettes courantes&nbsp;; la part en actifs est passée de {{< gen-val "d1_part" >}}&nbsp;% ({{< gen-val "d1_lib" >}}) à {{< gen-val "d3_part" >}}&nbsp;% ({{< gen-val "d3_lib" >}}). C'est une lecture comptable, non une attribution causale&nbsp;: ces parts ne mesurent ni la rentabilité des dépenses ni leur utilité pour les générations futures. En {{< gen-val "h_fin" >}}, {{< gen-val "nr_fin" >}}&nbsp;% de la dette publique était enregistrée au nom de non-résidents, ce qui dit la résidence des détenteurs, non le fardeau.
{{< /reutiliser >}}
