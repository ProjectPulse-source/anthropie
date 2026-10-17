---
title: "La dette publique peut-elle baisser ?"
description: "Le poids de la dette dans le PIB peut baisser même quand son montant augmente. En France, de {baisse.d3_debut} à {baisse.annee_fin}, il a augmenté de {baisse.d3_var_abs} points ; dans {baisse.cmp_exc_n} pays qui partaient d'un niveau de dette plus élevé, il a nettement reculé, d'abord sous l'effet de la croissance, ensuite de leurs excédents primaires."
chapo: "Oui : ce qui peut baisser, c'est le poids de la dette dans le PIB, même quand son montant augmente. Au Portugal, la dette publique est passée de {baisse.cmp_pt_enc0} à {baisse.cmp_pt_enc1} milliards d'euros de fin {baisse.cmp_veille} à fin {baisse.annee_fin}, et son poids de {baisse.cmp_pt_d0} % à {baisse.cmp_pt_d1} % du PIB. En France, il a augmenté de {baisse.d3_var_abs} points sur la même période : les administrations ont dépensé plus qu'elles n'encaissaient, même sans compter les intérêts, et ce déficit a pesé plus lourd que l'aide des taux et de la croissance."
og_title: "La dette publique peut-elle baisser ?"
og_image: "images/og-dette-baisse.jpg"
og_image_alt: "Carte de partage : « Les déficits ont pesé plus lourd » — France, trois décennies : effet des taux et de la croissance, déficits primaires et autres ajustements, en points de PIB."
date: 2026-10-02
lastmod: 2026-10-11
# Volet 5 du dossier dette (onglet depuis la barre A+ v2 du 03/10/2026), créé le 02/10/2026 sur décision de l'auteur (« construis la page autour du constat français »).
# Test décisif : D:\PRO\06_PROMOTION\RECHERCHE_SOLUTIONS_DETTE_2026-10-02\test_decisif\ ; contre-expertises et arbitrages :
# D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261002-195300_arbitrage.md (test) et PRO-20261003-064640_arbitrage.md (page) ; avis entrant final : ENTRANTE_2026-10-03_Solution_Dette_arbitrage.md.
# Décisions verrouillées : ni « presque nécessaire », ni « suffit », ni seuil de 2 % ; toute fréquence dit son événement, son
# dénominateur et sa période ; un ratio n'est pas un montant ; le solde stabilisant est dit « hors autres ajustements ».
# Refonte (phase B du volet 5, 11/10/2026, contre-expertise OPTIMUM-24) : la hiérarchie mesurée des deux ressorts (taux et
# croissance, puis excédents), les taux séparés de la croissance, l'écart de la dernière année en milliards comme écart
# comptable, jamais comme montant à trouver (formules interdites, gardées par le générateur).
# Aucun chiffre saisi : jetons {baisse.*} et shortcodes baisse-val / baisse-tableau (scripts/update_dette_baisse.py).
donnees: [dette_baisse]
journal:  # révisions qui changent la lecture de la page (partials/page-date-visible.html affiche la plus récente)
  - {date: 2026-10-16, texte: "Correction : le taux implicite a dépassé la croissance nominale 15 années, et non 16 ; la comparaison se fait désormais à la précision affichée."}
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_baisse"
  nom: "La dette publique peut-elle baisser : décomposition par décennie du ratio dette/PIB, France et pays de l'Union dont la dette dépassait 90 % du PIB"
  description: "Décomposition de la variation du ratio dette/PIB en effet des taux et de la croissance, déficits primaires et autres ajustements (flux-stock) : France par décennie de {baisse.annee_debut} à {baisse.annee_fin}, solde primaire observé et solde stabilisant hors autres ajustements année par année, et les pays de l'Union dont la dette dépassait {baisse.seuil_dette} % du PIB fin {baisse.cmp_veille} ; moyennes des pays de la zone euro sur plusieurs périodes, avec le solde primaire structurel de la Commission européenne (AMECO) en témoin. Ratios contrôlés contre ceux que publie Eurostat ; aucune valeur saisie à la main."
  couverture_temporelle: "{baisse.annee_debut}/{baisse.annee_fin}"
  couverture_spatiale: "France ; Union européenne (27 pays)"
  variables:
    - {nom: "Variation du ratio dette/PIB", unite: "points de PIB", description: "cumulée sur dix ans"}
    - {nom: "Effet taux-croissance", unite: "points de PIB", description: "intérêts moins érosion du ratio par la croissance du PIB nominal"}
    - {nom: "Déficits primaires cumulés", unite: "points de PIB", description: "hors intérêts ; négatif en cas d'excédents"}
    - {nom: "Autres ajustements (flux-stock)", unite: "points de PIB", description: "résidu de l'identité"}
    - {nom: "Solde primaire stabilisant", unite: "% du PIB", description: "solde qui aurait laissé le ratio inchangé dans l'année, hors autres ajustements"}
    - {nom: "Encours de dette", unite: "milliards de monnaie nationale", description: "pays comparés, début et fin de la décennie"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table?lang=fr"
    - "https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr"
  mots: ["dette publique", "France", "excédent primaire", "solde primaire stabilisant", "taux implicite", "croissance nominale", "désendettement", "Eurostat"]
  fichiers: ["dette_baisse.csv", "dette_baisse.json"]
faq:
  - question: "La croissance et l'inflation suffisent-elles à faire baisser la dette ?"
    answer: "Elles allègent le ratio quand la croissance nominale dépasse le taux d'intérêt payé sur la dette, et ce sont elles qui ont le plus fait reculer le ratio dans les {baisse.cmp_exc_n} pays de l'Union où il a nettement baissé, parmi ceux dont la dette dépassait {baisse.seuil_dette} % du PIB fin {baisse.cmp_veille} : environ deux fois plus que leurs excédents primaires. Mais l'effet varie fortement d'une année à l'autre : en France, il a retiré {baisse.d3_creux_abs} points au ratio en {baisse.d3_creux_lib} et compté pour {baisse.d3_pic_tc} points en {baisse.d3_pic_annee}. Dans ce groupe, aucun pays resté en déficit primaire moyen n'a vu son ratio baisser de {baisse.forte_baisse} points ; la Slovénie, sous le seuil, l'a fait."
  - question: "La France a-t-elle déjà dégagé un excédent primaire ?"
    answer: "{baisse.exc_n_maj} fois depuis {baisse.annee_debut}, de {baisse.exc_premiere} à {baisse.exc_derniere}, au plus {baisse.exc_max} % du PIB (Eurostat). Depuis, le solde primaire des administrations publiques est resté déficitaire chaque année."
  - question: "Un excédent primaire fait-il toujours baisser la dette ?"
    answer: "Il contribue à réduire le ratio, mais la variation finale dépend aussi des taux, de la croissance et des autres ajustements : en France, le solde a atteint le repère de stabilisation hors ajustements en {baisse.suff_hausse} sans que le ratio baisse. Dans les fenêtres de dix ans des {baisse.eu_pays} pays aujourd'hui membres de l'Union où la dette de départ dépassait {baisse.seuil_dette} % du PIB, le ratio a baissé d'au moins {baisse.forte_baisse} points dans {baisse.eu_mid_fb} des {baisse.eu_mid_n} fenêtres à solde primaire moyen de 0 à moins de 2 % et dans {baisse.eu_exc_fb} des {baisse.eu_exc_n} à solde d'au moins 2 %, mais dans aucune des {baisse.eu_def_n} à solde primaire moyen négatif ; ces fenêtres se recouvrent et viennent de quelques pays."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 35
  nature: "Séries officielles (Eurostat) décomposées et calculs de l'auteur"
---

{{< dossier-dette volet="baisse" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< baisse-val "date_donnees" >}}</span> Administrations publiques, séries Eurostat de {{< baisse-val "annee_debut" >}} à {{< baisse-val "annee_fin" >}}. Télécharger&nbsp;: <a href="/dette_baisse.csv">CSV</a> · <a href="/dette_baisse.json">JSON</a> · <a href="#sources">méthode</a></p>

## Le poids de la dette, pas son montant {#poids-et-montant}

Le ratio de dette rapporte ce que doivent les administrations publiques à la richesse produite en un an, le produit intérieur brut (PIB), mesuré en euros courants, dit nominal. Il baisse dès que le PIB nominal croît plus vite que la dette&nbsp;: au Portugal, de fin {{< baisse-val "cmp_veille" >}} à fin {{< baisse-val "annee_fin" >}}, la dette publique est passée de {{< baisse-val "cmp_pt_enc0" >}} à {{< baisse-val "cmp_pt_enc1" >}} milliards d'euros pendant que son poids reculait de {{< baisse-val "cmp_pt_d0" >}}&nbsp;% à {{< baisse-val "cmp_pt_d1" >}}&nbsp;% du PIB. Ce recul a suivi un programme d'aide et d'ajustement, dont ces séries ne mesurent pas le coût pour les Portugais ([limites](#limites)).

Chaque année, trois termes font bouger ce ratio, détaillés dans [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)&nbsp;:

- **les taux et la croissance**&nbsp;: les intérêts payés alourdissent le ratio, la croissance du PIB nominal, en volume et en prix, l'allège&nbsp;; la page appelle leur bilan «&nbsp;l'effet des taux et de la croissance&nbsp;»&nbsp;;
- **le solde primaire**, recettes moins dépenses hors intérêts&nbsp;: un déficit alourdit le ratio, un excédent l'allège&nbsp;;
- **les autres ajustements**, dits «&nbsp;flux-stock&nbsp;»&nbsp;: acquisitions d'actifs, variations de trésorerie et autres opérations qui modifient la dette sans passer par le déficit.

Les variations du ratio se mesurent en points de PIB. En {{< baisse-val "annee_fin" >}}, un point correspond à environ {{< baisse-val "point_md" >}} milliards d'euros&nbsp;; mais les contributions cumulées sur dix ans, calculées chaque année sur le PIB de l'année, ne représentent pas des sommes versées ou économisées. Cette décomposition est comptable&nbsp;: elle dit par quel canal le ratio a bougé. Les conditions économiques (croissance, inflation, taux) et les décisions budgétaires agissent sur plusieurs termes à la fois, et elle ne les sépare pas.

## La France&nbsp;: trois décennies, et trois années à part {#trois-decennies}

{{< figure-svg fichier="dette-baisse-decennies" alt="Pour chacune des trois dernières décennies, quatre barres : effet des taux et de la croissance, solde primaire, autres ajustements, et la variation du ratio de dette, leur somme. Sur la dernière décennie, taux et croissance font baisser le ratio, les déficits primaires le font monter davantage." >}}Ce qui a fait monter ou baisser le ratio dette/PIB français, par décennie, en points de PIB cumulés (Eurostat). Orange&nbsp;: ce qui le fait monter&nbsp;; gris&nbsp;: ce qui le fait baisser&nbsp;; bleu&nbsp;: la variation, somme des trois.{{< /figure-svg >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** De {{< baisse-val "d3_debut" >}} à {{< baisse-val "annee_fin" >}}, les déficits primaires ont ajouté {{< baisse-val "d3_def_abs" >}} points au ratio de dette français, l'effet des taux et de la croissance, concentré en {{< baisse-val "d3_creux_lib" >}}, en a retiré {{< baisse-val "d3_tc_abs" >}}, et les autres ajustements en ont ajouté {{< baisse-val "d3_sfa_abs" >}}&nbsp;: le bilan est une hausse de {{< baisse-val "d3_var_abs" >}} points. C'est une décomposition comptable&nbsp;: elle dit par quel terme la dette a bougé, pas pourquoi les déficits ont existé.

</div>

**Les deux décennies précédentes.** De {{< baisse-val "d1_debut" >}} à {{< baisse-val "d2_fin" >}}, le ratio passe de {{< baisse-val "d1_dette_deb" >}}&nbsp;% à {{< baisse-val "d2_dette_fin" >}}&nbsp;% du PIB&nbsp;: l'effet des taux et de la croissance pousse d'abord le ratio à la hausse, le budget hors intérêts restant proche de l'équilibre, puis les déficits primaires prennent le dessus, avec la crise financière de 2008-2009.

<details class="repli"><summary>Les deux décennies précédentes, terme par terme</summary>

**{{< baisse-val "d1_lib" >}}&nbsp;: les taux et la croissance poussent à la hausse.** Le ratio passe de {{< baisse-val "d1_dette_deb" >}}&nbsp;% à {{< baisse-val "d1_dette_fin" >}}&nbsp;% du PIB. L'effet des taux et de la croissance ajoute {{< baisse-val "d1_tc_abs" >}} points&nbsp;; le solde primaire, excédentaire {{< baisse-val "d1_exc" >}} années sur dix, en retire {{< baisse-val "d1_def_abs" >}}.

**{{< baisse-val "d2_lib" >}}&nbsp;: les deux termes poussent ensemble.** Le ratio gagne {{< baisse-val "d2_var_abs" >}} points, la plus forte hausse des trois décennies&nbsp;: {{< baisse-val "d2_def_abs" >}} par les déficits primaires, {{< baisse-val "d2_tc_abs" >}} par l'effet des taux et de la croissance. La période contient la crise financière de 2008-2009.

D'une décennie à l'autre, la contribution des déficits primaires est passée de {{< baisse-val "d1_def" >}} à {{< baisse-val "d2_def" >}} puis {{< baisse-val "d3_def" >}} points. Ce constat décrit une récurrence&nbsp;; il ne dit pas si ces déficits étaient évitables, ni lequel de leurs deux termes, dépenses ou recettes, les explique.

</details>

**{{< baisse-val "d3_lib" >}}&nbsp;: un allègement de trois ans, dépassé par les déficits.** Sur la décennie, les intérêts ajoutent {{< baisse-val "d3_interets" >}} points au ratio et la croissance du PIB nominal en efface {{< baisse-val "d3_croissance" >}}&nbsp;: l'effet des taux et de la croissance est de {{< baisse-val "d3_tc" >}} points. Ce n'est pas un avantage régulier. Les années {{< baisse-val "d3_creux_lib" >}} en retirent à elles seules {{< baisse-val "d3_creux_abs" >}} points&nbsp;; les {{< baisse-val "d3_reste_n" >}} autres pèsent ensemble {{< baisse-val "d3_reste" >}} point, dont {{< baisse-val "d3_pic_tc" >}} en {{< baisse-val "d3_pic_annee" >}}, quand le PIB reculait. En {{< baisse-val "d3_creux_rebond" >}}, l'activité rebondit ({{< baisse-val "d3_creux_rebond_gv" >}}&nbsp;% en volume)&nbsp;; les deux années suivantes, la croissance nominale doit davantage aux prix qu'au volume. Une baisse du ratio par l'inflation n'est pas un enrichissement du même montant&nbsp;: une inflation supérieure à celle qui était anticipée réduit la valeur réelle des paiements fixes dus aux créanciers, un effet redistributif qui dépend de l'indexation des titres et de leur durée. Aucune année de la décennie n'est en excédent primaire&nbsp;: les déficits cumulés ajoutent {{< baisse-val "d3_def_abs" >}} points, plus que toute la hausse du ratio ({{< baisse-val "d3_var" >}}).

## Ce qui a fait baisser le ratio ailleurs {#pays-compares}

La même décomposition, sur la même décennie, s'applique aux pays de l'Union dont la dette dépassait {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB fin {{< baisse-val "cmp_veille" >}}&nbsp;: la France, à {{< baisse-val "cmp_fr_d0" >}}&nbsp;%, et {{< baisse-val "cmp_autres_n" >}} autres, qui partaient tous d'un niveau plus élevé. Ce seuil est une convention de présentation, proche du niveau français&nbsp;; il ne fait pas de ces pays des expériences équivalentes, et, à 100&nbsp;%, la France sort du groupe.

{{< figure-svg fichier="dette-baisse-comparaison" alt="Pour chaque pays du groupe, quatre barres : effet des taux et de la croissance, solde primaire, autres ajustements, et la variation du ratio de dette, leur somme. L'effet des taux et de la croissance fait baisser le ratio partout ; dans les trois pays où le ratio a nettement baissé, il pèse environ deux fois plus que les excédents primaires." >}}Effet des taux et de la croissance, solde primaire et autres ajustements, et leur somme, la variation du ratio de dette, {{< baisse-val "cmp_lib" >}}, en points de PIB cumulés (Eurostat). Pays triés par variation du ratio.{{< /figure-svg >}}

**Deux ressorts, dans l'ordre de leur poids.** Dans les {{< baisse-val "cmp_exc_n" >}} pays dont le ratio a nettement baissé, {{< baisse-val "cmp_exc_pays" >}}, la contribution comptable la plus forte vient des taux et de la croissance&nbsp;: de {{< baisse-val "cmp_exc_tc_min" >}} à {{< baisse-val "cmp_exc_tc_max" >}} points en dix ans, environ deux fois celle de leurs excédents primaires, de {{< baisse-val "cmp_exc_sp_min" >}} à {{< baisse-val "cmp_exc_sp_max" >}} points (rapport de {{< baisse-val "cmp_exc_rapport_min" >}} à {{< baisse-val "cmp_exc_rapport_max" >}}). Les deux contributions dépendent de la conjoncture, et ni l'une ni l'autre ne permet d'attribuer la baisse à une politique particulière.

<div class="encadre">

**Ce qui est établi.** Ces trois baisses ont coïncidé avec un excédent primaire moyen, de {{< baisse-val "cmp_exc_pb_min" >}} à {{< baisse-val "cmp_exc_pb_max" >}}&nbsp;% du PIB, et l'effet des taux et de la croissance y a pesé davantage que l'excédent.

**Ce qui ne l'est pas.** Que les excédents aient provoqué ces baisses, ou qu'ils aient été indispensables. Sans compter les excédents, les autres termes réunis font déjà baisser le ratio, de {{< baisse-val "cmp_exc_tcsfa_min" >}} à {{< baisse-val "cmp_exc_tcsfa_max" >}} points selon le pays. Cela ne veut pas dire que le ratio aurait baissé sans excédent, car les termes ne sont pas indépendants&nbsp;: un excédent peut freiner l'activité, une croissance forte gonfle les recettes. Mais la décomposition ne permet pas, à elle seule, de faire de l'excédent une condition nécessaire. La Slovénie en donne un exemple&nbsp;: partie d'une dette de {{< baisse-val "s80_exc_d0" >}}&nbsp;% du PIB, sous le seuil de {{< baisse-val "seuil_dette" >}}&nbsp;% retenu ici, elle a vu son ratio baisser de {{< baisse-val "s80_exc_var" >}} points avec un solde primaire moyen de {{< baisse-val "s80_exc_pb" >}}&nbsp;% du PIB.

</div>

**Leur taux implicite n'était pas plus bas.** Sur la décennie, le taux implicite moyen de leur dette, intérêts payés rapportés à la dette, va de {{< baisse-val "cmp_exc_ti_min" >}} à {{< baisse-val "cmp_exc_ti_max" >}}&nbsp;%, contre {{< baisse-val "cmp_fr_ti" >}}&nbsp;% en France, le plus bas du groupe. Cet indicateur porte sur le stock&nbsp;: il reflète l'histoire des émissions, leur durée et les prêts officiels, et ne dit pas à quelles conditions ces pays empruntaient sur les marchés. Ce qui les distingue, c'est la croissance du PIB nominal&nbsp;: de {{< baisse-val "cmp_exc_g_min" >}} à {{< baisse-val "cmp_exc_g_max" >}}&nbsp;% par an en moyenne, contre {{< baisse-val "cmp_fr_g" >}}&nbsp;% en France. En volume, elle y a dépassé celle de la France, de {{< baisse-val "cmp_exc_gv_min" >}} à {{< baisse-val "cmp_exc_gv_max" >}}&nbsp;% par an contre {{< baisse-val "cmp_fr_gv" >}}&nbsp;%&nbsp;; la hausse des prix y a été de {{< baisse-val "cmp_exc_gp_min" >}} à {{< baisse-val "cmp_exc_gp_max" >}}&nbsp;% par an, contre {{< baisse-val "cmp_fr_gp" >}}&nbsp;%.

**Le niveau de la dette compte aussi.** Le même écart entre taux et croissance retire d'autant plus de points que le ratio est élevé. La Grèce affiche à peu près le même taux implicite que la France ({{< baisse-val "cmp_el_ti" >}}&nbsp;% contre {{< baisse-val "cmp_fr_ti" >}}&nbsp;%), et sa croissance nominale dépasse à peine la française ({{< baisse-val "cmp_el_g" >}}&nbsp;% contre {{< baisse-val "cmp_fr_g" >}}&nbsp;%)&nbsp;: son écart entre taux et croissance n'est guère plus favorable ({{< baisse-val "cmp_el_rg" >}} point par an, contre {{< baisse-val "cmp_fr_rg" >}}). Mais sa dette, {{< baisse-val "cmp_dm_max" >}}&nbsp;% du PIB en moyenne, la plus élevée du groupe, démultiplie cet écart&nbsp;: l'effet des taux et de la croissance y atteint {{< baisse-val "cmp_el_tc" >}} points, contre {{< baisse-val "cmp_fr_tc" >}} en France. Une partie de la dette grecque est due à ses partenaires européens depuis les programmes d'aide&nbsp;; ces séries ne séparent pas le taux de ces prêts de celui du reste de la dette. Plus la dette de départ est élevée, plus un même écart entre taux et croissance amplifie la variation du ratio, à la baisse comme à la hausse.

**Les autres pays du groupe.** En France, le ratio a augmenté de {{< baisse-val "d3_var_abs" >}} points, la plus forte hausse du groupe, avec le déficit primaire moyen le plus élevé ({{< baisse-val "cmp_fr_pb" >}}&nbsp;% du PIB)&nbsp;; le ratio est resté à peu près stable pour {{< baisse-val "cmp_def_autres" >}}, en déficit primaire moyen, malgré un effet des taux et de la croissance favorable. Le Portugal, Chypre et la Grèce ont bénéficié de financements officiels de leurs partenaires européens et du FMI, l'Espagne d'une aide à la recapitalisation de ses banques (calendrier dans le repli ci-dessous). Sept pays sur une décennie ne font pas une régularité générale.

<details class="repli"><summary>Les {{< baisse-val "cmp_n" >}} pays, terme par terme, taux par taux, et les programmes d'aide</summary>

{{< baisse-tableau >}}

{{< baisse-tableau vue="taux" >}}

Le ratio est resté à peu près stable pour {{< baisse-val "cmp_def_autres" >}} ({{< baisse-val "cmp_def_var_min" >}} à {{< baisse-val "cmp_def_var_max" >}} points), en déficit primaire moyen, malgré un effet des taux et de la croissance favorable. En Belgique, les contributions des taux et de la croissance et du solde primaire totalisent {{< baisse-val "cmp_be_tcdef" >}} points&nbsp;; les autres ajustements en ajoutent {{< baisse-val "cmp_be_sfa_abs" >}}, portant la variation à {{< baisse-val "cmp_be_var" >}} points.

Ces pays n'ont pas été financés dans les mêmes conditions. Le Portugal (de 2011 à mi-2014), Chypre (d'avril 2013 à mars 2016) et la Grèce (de mai 2010 à août 2018, dernier programme, financé par le Mécanisme européen de stabilité, d'août 2015 à août 2018) ont bénéficié de financements officiels de leurs partenaires européens et du FMI&nbsp;; l'Espagne a reçu, de juillet 2012 à janvier 2014, une aide à la recapitalisation de ses banques ([Commission européenne](https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries_en)&nbsp;; [Mécanisme européen de stabilité](https://www.esm.europa.eu/assistance/greece/greece-successfully-concludes-esm-programme)). La restructuration de la dette grecque, en 2012, précède la décennie étudiée.

Abaisser le seuil à 80&nbsp;% fait entrer dans le groupe {{< baisse-val "s80_ajouts" >}}.

</details>

## Quel solde stabiliserait la dette&nbsp;? {#solde-stabilisant}

Une année donnée, et hors autres ajustements, le ratio ne bouge pas si le solde primaire compense exactement l'effet des taux et de la croissance de l'année. Ce solde, dit stabilisant, est la courbe grise&nbsp;; le solde réellement observé est la courbe orange.

{{< figure-svg fichier="dette-baisse-stabilisant" alt="Deux courbes annuelles sur trente ans, en pourcentage du PIB : le solde primaire observé et le solde qui aurait stabilisé le ratio de dette, qui bondit l'année du recul du PIB et plonge l'année du rebond ; la dernière année, un pointillé marque l'écart entre les deux." >}}Solde primaire observé et solde primaire qui aurait stabilisé le ratio de dette dans l'année, hors autres ajustements, France, en&nbsp;% du PIB (Eurostat, calcul de l'auteur).{{< /figure-svg >}}

**Pourquoi le repère change d'une année à l'autre.** Il dépend de l'écart entre le taux implicite et la croissance nominale, multiplié par le niveau de la dette. En {{< baisse-val "stab_max_annee" >}}, le PIB nominal a reculé&nbsp;: il aurait fallu un solde primaire de {{< baisse-val "stab_max" >}}&nbsp;% du PIB, un excédent, pour stabiliser le ratio. En {{< baisse-val "stab_min_annee" >}}, il a rebondi&nbsp;: un solde de {{< baisse-val "stab_min" >}}&nbsp;%, donc un déficit, l'aurait laissé stable. Ces mouvements ne mesurent pas un changement de discipline budgétaire&nbsp;: c'est la croissance qui a bougé.

**En {{< baisse-val "annee_fin" >}}.** Taux implicite ({{< baisse-val "taux_implicite_dernier" >}}&nbsp;%) et croissance nominale ({{< baisse-val "croissance_derniere" >}}&nbsp;%) étaient presque égaux&nbsp;: le repère était proche de zéro. Le solde observé était de {{< baisse-val "pb_dernier" >}}&nbsp;% du PIB, soit un écart de {{< baisse-val "ecart_dernier" >}} points, environ {{< baisse-val "ecart_md" >}} milliards d'euros rapportés au PIB de {{< baisse-val "annee_fin" >}} ({{< baisse-val "pib_dernier_md" >}} milliards), calculés sur l'écart avant arrondi. C'est un écart comptable constaté pour cette année-là, aux taux et à la croissance de cette année-là et hors autres ajustements&nbsp;: il change chaque année avec eux, et il ne dit ni quelles dépenses, ni quelles recettes devraient bouger. Il se réduirait aussi par la croissance&nbsp;: à ce niveau de dette, et à taux inchangé, chaque point de croissance nominale supplémentaire abaisserait d'environ {{< baisse-val "sens_pt" >}} point le solde qui stabilise le ratio. C'est une propriété de l'identité, à dette et à taux donnés&nbsp;; elle ne dit pas qu'un point de croissance s'obtienne aussi aisément, ni au même coût, qu'un ajustement budgétaire.

<details class="repli"><summary>Le repère, année par année, et les excédents français</summary>

Sur {{< baisse-val "annees_total" >}} ans, le solde observé a atteint ou dépassé ce repère {{< baisse-val "suffisant_n" >}} années. Le ratio a effectivement baissé {{< baisse-val "suff_baisse_n" >}} de ces années&nbsp;; en {{< baisse-val "suff_hausse" >}}, il a augmenté malgré tout, sous l'effet des autres ajustements. La France n'a dégagé un excédent primaire que {{< baisse-val "exc_n" >}} fois, de {{< baisse-val "exc_premiere" >}} à {{< baisse-val "exc_derniere" >}}, au plus {{< baisse-val "exc_max" >}}&nbsp;% du PIB.

</details>

Stabiliser le ratio et le faire baisser sont deux objectifs distincts. Un montant d'ajustement se lit avec son objectif, son horizon et ses hypothèses&nbsp;; le repère calculé ici pour {{< baisse-val "annee_fin" >}} vaut pour cette année-là et ne permet pas d'évaluer les estimations pluriannuelles des institutions.

### Dans la zone euro, ce qui distingue la France {#zone-euro}

Le même calcul, mené sur les membres actuels de la zone euro, sépare ce que l'écart au repère, à lui seul, confond&nbsp;: le taux payé sur la dette, la croissance de l'économie et le solde primaire. Sur {{< baisse-val "ze_lib" >}}, {{< baisse-val "ze_n" >}} des {{< baisse-val "ze_total" >}} pays sont comparés&nbsp;; {{< baisse-val "ze_ecartes" >}} sont hors du calcul, parce qu'une de leurs années au moins s'écarte des ratios publiés par Eurostat au-delà de la marge d'arrondi.

{{< figure-svg fichier="dette-baisse-zone-euro" alt="Trois rangées de points, une par grandeur, en moyenne sur les dix dernières années : un point par pays de la zone euro, la France en orange, la médiane marquée d'un trait. Taux implicite de la dette : la France parmi les plus bas. Croissance du PIB nominal : la France la plus faible des pays comparés, à égalité avec un autre pays. Solde primaire : la France la plus basse." >}}Taux implicite, croissance nominale et solde primaire, moyennes annuelles {{< baisse-val "ze_lib" >}}, pays de la zone euro (Eurostat, calcul de l'auteur).{{< /figure-svg >}}

**Un taux implicite parmi les plus bas.** En moyenne sur {{< baisse-val "ze_lib" >}}, les administrations publiques françaises ont payé des intérêts égaux à {{< baisse-val "ze_fr_ti" >}}&nbsp;% de leur dette, contre une médiane de {{< baisse-val "ze_med_ti" >}}&nbsp;%&nbsp;; seuls {{< baisse-val "ze_ti_moins_n" >}} des pays comparés ont eu un taux implicite moins élevé, et, hors du calcul, {{< baisse-val "ze_ti_ecartes_sous" >}}. Ce taux rapporte les intérêts à toute la dette, émise au fil des années&nbsp;: il dit ce que coûte le stock, pas le taux auquel l'État emprunte aujourd'hui.

**Une croissance nominale parmi les plus faibles.** Le PIB nominal français a progressé de {{< baisse-val "ze_fr_g" >}}&nbsp;% par an, contre une médiane de {{< baisse-val "ze_med_g" >}}&nbsp;%&nbsp;: c'est, à égalité à l'arrondi avec {{< baisse-val "ze_g_avec" >}}, la croissance la plus faible des pays comparés&nbsp;; hors du calcul, celle de {{< baisse-val "ze_g_ecartes_sous" >}} a été plus faible encore ({{< baisse-val "ze_g_ecartes_val" >}}&nbsp;%). Le solde primaire qui aurait stabilisé le ratio, hors autres ajustements, est de {{< baisse-val "ze_fr_stab" >}}&nbsp;% du PIB en moyenne, proche de la médiane ({{< baisse-val "ze_med_stab" >}}&nbsp;%)&nbsp;: il dépend à la fois du taux implicite, de la croissance nominale et du niveau de la dette.

**Le solde primaire le plus bas.** Le solde primaire français a été de {{< baisse-val "ze_fr_pb" >}}&nbsp;% du PIB en moyenne, contre une médiane de {{< baisse-val "ze_med_pb" >}}&nbsp;%&nbsp;: aucun autre des pays comparés n'a eu, sur la période, un solde primaire moyen aussi bas. Le classement reste le même si l'on réintègre {{< baisse-val "ze_ecartes" >}}, années écartées comprises.

<div class="encadre">

**Ce qui est établi.** Sur {{< baisse-val "ze_lib" >}}, ce qui distingue la France dans la zone euro n'est ni le taux payé sur sa dette, parmi les plus bas, ni le solde qui la stabiliserait, proche de la médiane&nbsp;: c'est son solde primaire, le plus bas des pays comparés, avec une croissance nominale parmi les plus faibles.

**Ce qui ne l'est pas.** Que l'écart vienne des dépenses plutôt que des recettes, ou l'inverse&nbsp;: le solde primaire ne les sépare pas. Ni quel ajustement serait souhaitable, ni s'il aurait changé les taux payés.

</div>

**Avec l'indicateur structurel de la Commission, le classement est le même.** Le solde primaire structurel de la France, que la Commission européenne calcule hors effets estimés du cycle et hors mesures ponctuelles, est lui aussi le plus bas des pays comparés sur la même période&nbsp;: {{< baisse-val "ze_fr_sps" >}}&nbsp;% du PIB potentiel en moyenne, contre une médiane de {{< baisse-val "ze_med_sps" >}}&nbsp;% (base AMECO, édition de {{< baisse-val "ze_edition" >}}). Ce témoin ne sert pas au calcul, sans en être tout à fait indépendant&nbsp;: la Commission part des mêmes comptes publics, et sa correction repose sur une estimation du PIB potentiel qu'elle révise d'une édition à l'autre et que d'autres institutions estiment autrement.

**Le repère s'est abaissé, pas le solde.** Sur les cinq dernières années ({{< baisse-val "ze_cinq_lib" >}}), une forte croissance nominale, reprise après 2020 puis hausse des prix, a abaissé le repère de tous les pays par rapport aux cinq années d'avant 2020&nbsp;: la France n'est plus, en moyenne, sous le sien ({{< baisse-val "ze_cinq_ecart" >}} point), et {{< baisse-val "ze_cinq_pire_n" >}} pays ont un écart plus défavorable. Son solde primaire reste pourtant le plus bas des pays comparés, et son solde structurel parmi les deux plus bas. Sur les cinq années qui ont précédé 2020, la France était le seul pays de la zone euro dont le solde primaire moyen restait sous le repère.

<details class="repli"><summary>La France dans la zone euro selon la période retenue, et ce que l'écart moyen n'ajoute pas</summary>

{{< baisse-tableau vue="zone-euro" >}}

Moyennes annuelles, en&nbsp;% du PIB (du PIB potentiel pour le solde structurel)&nbsp;; rangs lus à la précision affichée&nbsp;; quand plusieurs pays s'affichent à égalité, le rang donne les places qu'ils occupent ensemble. Sur {{< baisse-val "ze_lib" >}} sans l'année 2020, la France garde le solde primaire et le solde structurel les plus bas, et la croissance nominale la plus faible.

**Ce que l'écart moyen n'ajoute pas.** Sur une période, l'écart moyen entre le solde observé et le repère est égal, au signe près et par construction, à la hausse du ratio hors autres ajustements, divisée par le nombre d'années&nbsp;: il redit la variation de la dette, il ne la confirme pas. Ce qui ne s'en déduit pas, c'est la part qui tient aux taux et à la croissance, le repère, et celle qui tient au solde primaire&nbsp;: c'est pourquoi la figure montre ces grandeurs plutôt que l'écart.

La zone euro est prise dans sa composition au 1er&nbsp;janvier 2026&nbsp;: la Croatie y est entrée en 2023, la Bulgarie en 2026. Le classement de la dernière année seule dépend de sa conjoncture, d'où les moyennes sur plusieurs années.

</details>

## La dette française est-elle soutenable&nbsp;? {#soutenable}

Aucun niveau de dette, à lui seul, ne tranche cette question. Une dette est dite soutenable quand l'État peut la servir et la refinancer sans un ajustement budgétaire hors de portée&nbsp;; cela dépend de son solde primaire, de l'écart entre le taux qu'il paie et la croissance nominale, et de la confiance de ceux qui lui prêtent. Les deux premiers termes se mesurent ici&nbsp;; le troisième, non.

**Ce qui le rend fragile.** L'égalité de {{< baisse-val "annee_fin" >}} entre taux et croissance n'est pas un état acquis. Sur {{< baisse-val "annees_total" >}} ans, le taux implicite a dépassé la croissance nominale {{< baisse-val "rg_pos_n" >}} années. Tombé à {{< baisse-val "ti_creux" >}}&nbsp;% en {{< baisse-val "ti_creux_annee" >}}, il remonte, à mesure que la dette ancienne se refinance aux conditions de marché, pendant que la croissance nominale retombe après les années d'inflation&nbsp;: l'allègement de la dernière décennie tenait pour l'essentiel à {{< baisse-val "d3_creux_lib" >}}. Au niveau de dette et de croissance de {{< baisse-val "annee_fin" >}} ({{< baisse-val "dette_derniere" >}}&nbsp;% du PIB), et toutes choses égales par ailleurs, un point supplémentaire d'écart entre le taux et la croissance relève le solde stabilisant d'environ {{< baisse-val "sens_pt" >}} point de PIB&nbsp;: plus la dette est élevée, plus sa trajectoire dépend de taux que le budget ne commande pas directement, et dont les travaux cités plus bas trouvent l'écart à la croissance plus élevé quand la dette l'est aussi.

**Ce que ces données ne disent pas.** La confiance des prêteurs, l'accès au marché et le coût des refinancements à venir dépendent de la maturité de la dette et de l'écart entre les taux de marché et le taux implicite (voir [la transmission](/dette-publique-comparaison-internationale/#transmission)), de ceux qui la détiennent ([Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)) et des décisions de la banque centrale. Les diagnostics de soutenabilité que publient les institutions reposent sur des projections conditionnelles, que ces données ne permettent ni de confirmer ni d'écarter.

## Trente ans de fenêtres européennes {#europe}

<details class="repli"><summary>Soldes primaires et baisses du ratio&nbsp;: les périodes européennes de dix ans</summary>

La comparaison ci-dessus ne porte que sur une décennie. Pour la replacer dans un ensemble plus large, la même décomposition a été appliquée à toutes les fenêtres de dix ans des {{< baisse-val "eu_pays" >}} pays aujourd'hui membres de l'Union, depuis {{< baisse-val "eu_premiere" >}}&nbsp;: {{< baisse-val "eu_fenetres" >}} fenêtres, qui se recouvrent, ne sont donc pas autant d'expériences indépendantes et contiennent la décennie déjà comparée. C'est un contexte, non une contre-épreuve.

Parmi les {{< baisse-val "eu_hautes_n" >}} fenêtres où la dette de départ dépassait {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB&nbsp;:

- **solde primaire moyen négatif**&nbsp;: {{< baisse-val "eu_def_n" >}} fenêtres, dans {{< baisse-val "eu_def_pays_n" >}} pays ({{< baisse-val "eu_def_pays" >}}). Le ratio baisse dans {{< baisse-val "eu_def_baisses" >}} d'entre elles, jamais de {{< baisse-val "forte_baisse" >}} points&nbsp;;
- **solde primaire moyen de 0 à moins de 2&nbsp;% du PIB**&nbsp;: {{< baisse-val "eu_mid_n" >}} fenêtres, dans {{< baisse-val "eu_mid_pays_n" >}} pays. Le ratio baisse dans {{< baisse-val "eu_mid_baisses" >}} d'entre elles, de {{< baisse-val "forte_baisse" >}} points ou plus dans {{< baisse-val "eu_mid_fb" >}}&nbsp;;
- **solde primaire moyen d'au moins 2&nbsp;% du PIB**&nbsp;: {{< baisse-val "eu_exc_n" >}} fenêtres, dans {{< baisse-val "eu_exc_pays_n" >}} pays seulement ({{< baisse-val "eu_exc_pays" >}}). Le ratio baisse dans les {{< baisse-val "eu_exc_baisses" >}}, de {{< baisse-val "forte_baisse" >}} points ou plus dans {{< baisse-val "eu_exc_fb" >}}.

Ces fréquences décrivent des périodes passées, dans quelques pays. Elles ne donnent ni un seuil d'excédent à atteindre, ni une probabilité de réussite&nbsp;: les fenêtres à fort excédent commencent pour la plupart avant 2003.

</details>

## Ce que ces données ne disent pas {#limites}

- **Mesure de la dette.** Une baisse du ratio ne signifie pas que le montant de dette a diminué. La dette suivie est brute&nbsp;: les autres ajustements mêlent achats d'actifs, prêts et écarts de valorisation, et un pays qui emprunte pour acquérir des actifs voit sa dette brute monter sans que sa situation financière se dégrade d'autant.
- **Interprétation économique.** Une décomposition comptable, non causale&nbsp;: les termes dépendent les uns des autres, et le solde observé contient la conjoncture, il ne mesure pas un effort. La croissance retenue est nominale&nbsp;; sa scission en volume et en prix est comptable et n'identifie pas la contribution propre de chacun. Rien ici ne dit lequel, des dépenses ou des recettes, devrait bouger.
- **Coût des ajustements.** Ces séries ne mesurent ni le chômage, ni les salaires, ni les services publics, ni les conséquences des programmes d'ajustement qu'ont suivis la Grèce, le Portugal ou Chypre&nbsp;: une forte baisse du ratio n'est pas, en elle-même, une réussite économique et sociale. Qui supporte un ajustement est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- **Périmètre de comparaison.** Les 27 pays aujourd'hui membres de l'Union, depuis {{< baisse-val "eu_premiere" >}}&nbsp;; rien avant, rien hors de l'Union. Le groupe comparé dépend du seuil de dette et de la décennie retenus. {{< baisse-val "cons_ecartees_maj" >}} années-pays sur {{< baisse-val "cons_calculables" >}} sont écartées par le contrôle décrit plus bas.
- **Portée dans le temps.** La page décrit trente années observées. Les trajectoires que prévoient le Gouvernement, la Commission européenne ou le FMI sont des scénarios conditionnels, que ces données ne permettent ni de confirmer ni d'écarter.

{{< confrontation-recherche verifie="2026-10-16" publie="oui" resume="le solde stabilisant et la distinction entre stabiliser et faire baisser sont retrouvés&nbsp;; lire l'écart nul de la dernière année comme un état durable, ou l'excédent comme le seul ressort des baisses, est mis en danger" >}}
**Mesuré ici.** La décomposition par décennie du ratio français, le solde stabilisant année par année et la comparaison des pays de l'Union dont la dette dépassait {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB, sur les séries d'Eurostat. Aucun des textes lus ne calcule ces grandeurs sur cette source et ces périodes&nbsp;: elles se valident par reproduction.

**Cohérent avec.** Le solde primaire qui stabilise la dette dépend de l'écart entre taux et croissance et du niveau de la dette, dans la même identité de dynamique de la dette, exprimée en termes nominaux ici et en termes réels dans le Focus, chez Clavères (direction générale du Trésor), dans la Note n°&nbsp;82 du Conseil d'analyse économique (Auclert, Philippon et Ragot) et dans son Focus n°&nbsp;124 (Auclert, Barbara, Jaravel, Laveissière, Lasterra, Ragot et Renaud), qui part d'un écart nul, comme le repère de la page pour la dernière année. La Note distingue dans les mêmes termes stabiliser, qui exige un solde primaire nul quand taux et croissance sont égaux, et faire baisser, qui exige un excédent. Sur les pays du G7 depuis la fin du XIX<sup>e</sup>&nbsp;siècle, Clavères trouve que, dans la grande majorité des cas, les consolidations budgétaires réussies se sont appuyées à la fois sur un écart taux-croissance négatif et sur des excédents primaires. La direction générale du Trésor présente la stabilisation du ratio comme une condition nécessaire de la soutenabilité, qu'elle rattache aussi à la capacité de l'État à financer durablement sa dette&nbsp;; elle situe le solde stabilisant de 2025 à −2,1&nbsp;% du PIB, en solde public total, pour un déficit de 5,1&nbsp;%. Deux conventions différentes, et un écart à combler presque identique en 2025&nbsp;: environ trois points de PIB chez le Trésor, {{< baisse-val "ecart_dernier" >}} points mesurés ici en solde primaire. L'OFCE estime à 2,1 points, en 2024, l'écart entre le solde primaire et celui qui stabiliserait la dette&nbsp;; la mesure Eurostat de la page donne {{< baisse-val "ecart_prec" >}} points pour {{< baisse-val "annee_prec" >}}.

**Mis en danger par.** Deux lectures que la page doit éviter. La première ferait de l'excédent primaire le seul ressort des baisses&nbsp;: après 1945, c'est l'écart fortement négatif entre taux et croissance qui a le plus contribué à la baisse des dettes des économies avancées, les excédents primaires ayant aussi joué un rôle (Clavères)&nbsp;; au Portugal, l'excédent a coïncidé avec une croissance de 4,38&nbsp;% par an de 2015 à 2019, et en Italie, quand le taux dépassait la croissance, la dette a augmenté malgré un solde primaire structurel positif (Note du CAE). D'où la réserve de la page&nbsp;: la comparaison n'isole pas l'effet d'une politique. La seconde lirait l'écart nul de la dernière année comme un état durable&nbsp;: à l'automne 2025, l'État empruntait à 10&nbsp;ans à 3,5&nbsp;%, au-dessus d'un taux apparent estimé à 2,0&nbsp;% (Focus du CAE)&nbsp;; la hausse des taux ne se transmet au stock que progressivement, la maturité moyenne de la dette étant de 8,5&nbsp;ans en 2023, les valeurs futures de l'écart ne se prévoient pas, et, dans l'estimation de Clavères sur 18 économies avancées de 1950 à 2019, mesurée avec le taux à 10 ans, une dette plus élevée va de pair avec un écart plus élevé l'année suivante, estimation que son auteur dit à prendre avec précaution. Trois économistes du FMI (Lian, Presbitero et Wiriadinata), qui mesurent l'écart avec un taux de marché à long terme, le plus souvent le rendement des obligations publiques à 10&nbsp;ans, et non avec le taux implicite de cette page, trouvent une association de même sens, qu'ils étudient sous d'autres formes. Dans 17 économies avancées, dont la France, de 1950 à 2019, les épisodes d'écart négatif d'au moins trois ans sont d'autant plus courts que la dette de départ est élevée, de près de cinq mois par dix points de dette, et la probabilité qu'un écart négatif d'au moins deux ans laisse place à un écart moyen positif sur les cinq années suivantes passe d'environ 25&nbsp;% quand la dette est inférieure à la médiane à près de 75&nbsp;% dans le quart le plus endetté. Dans 31 économies avancées et 25 émergentes de 2000 à 2019, quand la dette passe de 40 à 120&nbsp;% du PIB, le neuvième décile de l'écart moyen des cinq années suivantes passe d'environ 0 à environ 2&nbsp;points, tandis que sa médiane augmente d'environ 0,8&nbsp;point et son premier décile d'environ 1,2&nbsp;point&nbsp;: toute la distribution se déplace vers le haut, sa partie haute davantage. Ce sont des associations. Une analyse complémentaire des auteurs montre que la monnaie d'émission compte&nbsp;: quand la dette est séparée selon sa monnaie, l'écart suit, à l'intérieur de chaque pays, la dette libellée en devises, alors que son association avec la dette en monnaie nationale n'y est pas statistiquement significative&nbsp;; et les pays plus endettés que la médiane dont la part de dette en devises est inférieure à la médiane gardent en moyenne un écart faible et négatif. Ces résultats ne se transposent pas mécaniquement aux États de la zone euro, que le document ne traite pas à part&nbsp;: leur dette est émise dans la monnaie commune, mais aucun ne dispose seul du pouvoir monétaire de la Banque centrale européenne. Sur la zone euro elle-même, deux études publiées divergent. Deux économistes de la BCE, l'institution qui conduit cette politique monétaire (Checherita-Westphal et Domingues Semeano), mesurent l'écart avec le taux implicite, comme cette page, dans les douze premiers membres de la zone euro, dont la France, de 1985 à 2017&nbsp;: dix points de dette de plus y vont de pair avec un écart plus élevé de 0,4 à 0,6&nbsp;point, sans seuil apparent, et les auteurs écrivent que leur analyse met au jour surtout des corrélations, la causalité jouant probablement dans les deux sens. Philipp Heimberger, de l'Institut viennois d'études économiques internationales, ne retrouve pas cette association dans 22 pays de l'OCDE, dont 11 de la zone euro, de 1970 à 2018&nbsp;: la dette de l'année précédente n'y prédit pas un écart plus défavorable, ni dans la zone euro ni hors d'elle, et la durée des épisodes d'écart négatif n'y dépend pas de la dette de départ&nbsp;; c'est la crise de l'euro, de 2008 à 2012, qui va avec un écart plus élevé, dans les seuls pays de la périphérie, et d'autant plus que leurs titres passaient auparavant pour moins sûrs. Les deux études ne mesurent pas le même objet. La seconde rapporte le taux à 10&nbsp;ans à la croissance du PIB en dollars courants, non en euros&nbsp;: pour la France, 5,2&nbsp;% en 2016 dans ses données, 1,4&nbsp;% en euros selon Eurostat. Elle estime en outre l'association de la dette avec l'écart à taux réel de long terme et inflation donnés, alors qu'une partie de l'effet cherché passerait précisément par les taux. La direction générale du Trésor écrit, elle aussi, que la remontée des taux inverse la période d'écart négatif et exige désormais un léger excédent primaire, et que la hausse des taux se répercute sur le stock à mesure qu'il est refinancé. Le diagnostic n'est pas unanime&nbsp;: l'OFCE tient la hausse de la charge d'intérêts pour probable, mais son ampleur pour moins certaine que dans les projections officielles. Renouveler au taux à 10 ans de juillet 2025 les 900 milliards d'euros de titres arrivant à échéance d'ici 2029 coûterait environ 0,5 point de PIB&nbsp;; les auteurs le rapprochent d'une hausse totale de 1,2 point projetée par le FMI, sans que les deux calculs aient le même périmètre. Son modèle suppose en outre un taux apparent inférieur à la croissance nominale à partir de 2026. Enfin, la Note du CAE avance qu'il serait difficile de laisser la dette dépasser 125&nbsp;% du PIB sans risquer une forte hausse des taux, et le Focus retient 130&nbsp;% comme plafond de son modèle, le niveau de la Grèce en 2009&nbsp;: le premier chiffre est motivé par l'observation de quelques cas européens, le second est un paramètre choisi&nbsp;; aucun n'est un seuil estimé, ce qui laisse intacte la phrase de la page selon laquelle aucun niveau de dette, à lui seul, ne tranche la question.

**Non établi.** Le montant de l'effort. Les 112&nbsp;milliards d'euros du Focus du CAE font 3,7&nbsp;points de PIB&nbsp;: un déficit primaire **structurel** estimé de 2,7&nbsp;points, prévu en octobre 2025, et un point de marge pour la crise suivante. Ils ne se comparent pas terme à terme à l'écart observé de la page pour {{< baisse-val "annee_fin" >}}, hors autres ajustements. L'OFCE (Heyer, Plane, Ragot, Sampognaro et Timbeau) chiffre à 2,8&nbsp;points de PIB d'ici 2029 un ajustement progressif qui stabiliserait la dette à 110&nbsp;%, 2,5&nbsp;points avec des taux plus bas&nbsp;: une projection de modèle. L'effet de la dette sur l'écart futur&nbsp;: les études lues ne livrent pas un coefficient unique, leur résultat dépend de la mesure du taux, de la période, de ce qu'elles tiennent constant et des institutions monétaires&nbsp;; seule la relation comptable ne dépend d'aucune estimation&nbsp;: le solde qui stabilise la dette est le produit de l'écart et du niveau de la dette, de sorte que plus elle est élevée, plus une même remontée de l'écart coûte cher, ce que rappelle l'article de Heimberger. L'accès au marché&nbsp;: aucun des neuf textes ne le mesure&nbsp;; la direction générale du Trésor invoque la crédibilité auprès des investisseurs sans la mesurer.

**Références lues**

- Auclert, A., Philippon, T. et Ragot, X., «&nbsp;Quelle trajectoire pour les finances publiques françaises&nbsp;?&nbsp;», *Les notes du Conseil d'analyse économique*, n°&nbsp;82, juillet 2024.
- Auclert, A., Barbara, M.-A., Jaravel, X., Laveissière, E., Lasterra, O., Ragot, X. et Renaud, D., «&nbsp;Comment stabiliser la dette publique&nbsp;?&nbsp;», *Focus du Conseil d'analyse économique*, n°&nbsp;124, octobre 2025.
- Checherita-Westphal, C. et Domingues Semeano, J., «&nbsp;Interest rate-growth differentials on government debt: an empirical investigation for the euro area&nbsp;», *ECB Working Paper Series*, n°&nbsp;2486, Banque centrale européenne, novembre 2020 (en anglais).
- Clavères, G., «&nbsp;Taux d'intérêt, croissance et soutenabilité de la dette publique&nbsp;», *Trésor-Éco*, n°&nbsp;334, direction générale du Trésor, octobre 2023.
- Heimberger, P., «&nbsp;Public debt and r-g risks in advanced economies: Eurozone versus stand-alone&nbsp;», *Journal of International Money and Finance*, vol.&nbsp;136, article 102877, septembre 2023 (en anglais).
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., «&nbsp;Quelles trajectoires pour les finances publiques de la France&nbsp;?&nbsp;», *Blog de l'OFCE*, 2025.
- Direction générale du Trésor, «&nbsp;Finances publiques&nbsp;: une situation dégradée, un redressement nécessaire&nbsp;», *Trésor-Éco*, n°&nbsp;403, septembre 2026.
- Heyer, É., Plane, M., Ragot, X., Sampognaro, R. et Timbeau, X., «&nbsp;Quelles trajectoires pour les finances publiques de la France&nbsp;?&nbsp;», document de travail de l'OFCE n°&nbsp;13, juillet 2025.
- Lian, W., Presbitero, A. F. et Wiriadinata, U., «&nbsp;Public Debt and r - g at Risk&nbsp;», *IMF Working Paper*, n°&nbsp;20/137, Fonds monétaire international, juillet 2020 (en anglais).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

Le poids d'une dette peut baisser sans que son montant diminue&nbsp;: au Portugal, la dette est passée de {{< baisse-val "cmp_pt_enc0" >}} à {{< baisse-val "cmp_pt_enc1" >}} milliards d'euros en dix ans pendant que son poids reculait de {{< baisse-val "cmp_pt_d0" >}}&nbsp;% à {{< baisse-val "cmp_pt_d1" >}}&nbsp;% du PIB.

Parmi les pays de l'Union qui partaient d'un niveau de dette plus élevé que la France, le ratio a nettement reculé dans {{< baisse-val "cmp_exc_n" >}} d'entre eux&nbsp;: {{< baisse-val "cmp_exc_pays" >}}. La contribution la plus forte y vient des taux et de la croissance, environ deux fois celle de leurs excédents primaires. Leur taux implicite moyen n'était pas plus bas que celui de la France&nbsp;: leur croissance nominale a été plus forte. La Slovénie, sous le seuil retenu, a réduit le sien sans excédent.

En France, sur la même décennie, les taux et la croissance ont retiré {{< baisse-val "d3_tc_abs" >}} points au ratio, à la faveur des années {{< baisse-val "d3_creux_lib" >}}&nbsp;; les déficits primaires en ont ajouté {{< baisse-val "d3_def_abs" >}}, et le ratio a augmenté de {{< baisse-val "d3_var_abs" >}} points.

En {{< baisse-val "annee_fin" >}}, taux implicite et croissance nominale étaient presque égaux&nbsp;: le solde primaire observé était inférieur de {{< baisse-val "ecart_dernier" >}} points de PIB, environ {{< baisse-val "ecart_md" >}} milliards d'euros, au repère qui aurait stabilisé le ratio cette année-là, hors autres ajustements. Ce repère change chaque année avec les taux et la croissance&nbsp;; à ce niveau de dette, un point d'écart entre taux et croissance le déplace d'environ {{< baisse-val "sens_pt" >}} point de PIB, dans un sens comme dans l'autre.

Aucune des combinaisons observées n'est une recette transposable&nbsp;: ces comparaisons ne disent ni quelle politique produirait une baisse, ni à quel prix, ni qui le paierait. Ce dernier point est l'objet de [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)
- [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Et ailleurs&nbsp;?](/dette-publique-comparaison-internationale/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page décompose la hausse du ratio de dette français et les baisses observées ailleurs. Faire baisser ce ratio peut déplacer des coûts. Qui les supporte&nbsp;: le contribuable, l'usager des services publics, l'épargnant par l'inflation, le créancier par une restructuration&nbsp;? Le livre prolonge cette analyse, chiffres officiels à l'appui, en examinant ces choix et leurs conséquences.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

Eurostat, administrations publiques (S.13), comptes SEC 2010, en monnaie nationale&nbsp;: dette de Maastricht et PIB nominal publiés avec la notification de déficit et de dette (`gov_10dd_edpt1`), intérêts versés et capacité ou besoin de financement (`gov_10a_main`, D41PAY et B9)&nbsp;; PIB en volume (`nama_10_gdp`, volumes chaînés), pour scinder la croissance nominale en volume et en prix. Le solde primaire est le solde des administrations publiques augmenté des intérêts versés. L'identité est celle du volet [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/#identite)&nbsp;; les termes annuels sont cumulés sur dix ans, de la fin de l'année qui précède la décennie à la fin de sa dernière année. Le solde stabilisant d'une année est l'effet taux-croissance de cette année, hors autres ajustements. Les variations et totaux sont calculés avant arrondi&nbsp;: les nombres affichés peuvent présenter un écart de 0,1 point.

Solde primaire structurel&nbsp;: Commission européenne, base AMECO, série UBLGBPS (solde des administrations publiques hors intérêts, corrigé du cycle et des mesures ponctuelles, en&nbsp;% du PIB potentiel), édition de {{< baisse-val "ze_edition" >}}, extrait archivé avec son empreinte&nbsp;; il sert de témoin et n'entre dans aucun calcul.

Contrôle&nbsp;: pour chaque pays et chaque année, le ratio de dette et le solde primaire calculés sont comparés à ceux qu'Eurostat publie en pourcentage du PIB, que le calcul n'utilise pas. Au-delà de {{< baisse-val "tolerance" >}} point d'écart, l'année est écartée et comptée ({{< baisse-val "cons_ecartees" >}} sur {{< baisse-val "cons_calculables" >}}, listées dans le fichier JSON)&nbsp;; pour la France et les pays comparés, le script s'arrête. Une fenêtre qui contient une année de croissance nominale supérieure à 35&nbsp;% (hyperinflation, rupture de série) est écartée. Les pays comparés à la France sont désignés par une règle, non choisis&nbsp;: dette supérieure à {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB à la fin de {{< baisse-val "cmp_veille" >}}&nbsp;; le même calcul est refait à 80 et à 100&nbsp;%. Les chiffres calculés sur les séries d'Eurostat viennent tous du même script, qui vérifie les principales affirmations chiffrées et s'arrête si leurs conditions ne sont plus remplies&nbsp;; leur formulation fait l'objet d'une relecture éditoriale. Les chiffres attribués à la direction générale du Trésor, au Conseil d'analyse économique et à l'OFCE sont repris tels qu'ils les publient.

{{< reutiliser figures="figures_baisse" jeu="dette_baisse" sources="Eurostat et Commission européenne (AMECO)" donnees="La décomposition par décennie du ratio dette/PIB français, le solde primaire observé et le solde stabilisant hors autres ajustements année par année, la même décomposition pour les pays de l'Union dont la dette dépassait 90 % du PIB, et les moyennes des pays de la zone euro (solde primaire, solde stabilisant, taux implicite, croissance nominale, solde structurel AMECO) ; le même contenu existe en CSV, au format long." >}}
De {{< baisse-val "d3_debut" >}} à {{< baisse-val "annee_fin" >}}, les déficits primaires ont ajouté {{< baisse-val "d3_def_abs" >}} points de PIB au ratio de dette français, l'effet des taux et de la croissance, concentré en {{< baisse-val "d3_creux_lib" >}}, en a retiré {{< baisse-val "d3_tc_abs" >}}, et les autres ajustements en ont ajouté {{< baisse-val "d3_sfa_abs" >}}&nbsp;: une hausse de {{< baisse-val "d3_var_abs" >}} points. Parmi les {{< baisse-val "cmp_n" >}} pays de l'Union dont la dette dépassait {{< baisse-val "seuil_dette" >}}&nbsp;% du PIB fin {{< baisse-val "cmp_veille" >}}, le ratio a nettement baissé dans {{< baisse-val "cmp_exc_n" >}}, d'abord par l'effet des taux et de la croissance, environ deux fois plus fort que celui de leurs excédents primaires. C'est une décomposition comptable, non une attribution causale.
{{< /reutiliser >}}
