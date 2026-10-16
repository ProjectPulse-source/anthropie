---
title: "L'inflation a-t-elle vraiment allégé la dette française ?"
description: "L'inflation de 2021-2023, plus forte que prévu, a réduit d'environ {infl.t} milliards d'euros de 2020 la valeur réelle des paiements promis sur la dette de l'État à taux fixe de fin 2020. L'État n'a pas encaissé ces milliards : l'érosion s'étale jusqu'en {infl.fin}, et elle n'est pas un gain budgétaire net identifiable. Calcul sur l'encours ligne à ligne de l'AFT et l'IPCH mensuel."
chapo: "L'État a-t-il gagné {infl.t} milliards grâce à l'inflation ? Pas sous la forme d'une recette. L'inflation de 2021-2023, plus forte que prévu, a réduit d'environ {infl.t} milliards d'euros de 2020 la valeur réelle des paiements promis sur la dette de l'État à taux fixe de fin 2020. Cet allègement se réalise au fil des paiements, jusqu'en {infl.fin} : un cinquième seulement fin 2023. Il ne prouve pas un gain budgétaire net équivalent."
date: 2026-10-07
lastmod: 2026-10-11
og_title: "L'inflation a-t-elle vraiment allégé la dette française ? — S. Lalut"
og_image: "images/og-dette-inflation.jpg"
og_image_alt: "Carte de partage : « L'inflation a érodé la vieille dette » — érosion réelle cumulée des paiements promis sur la dette de l'État à taux fixe de fin 2020, au fil des paiements, et plage des prévisions publiées début 2021."
# Page née d'une question reçue le 6/10/2026. Recherche : dépôt de recherche de l'auteur, chantier inflation et dette (V3 du 07/10,
# scripts/v3.py) ; quatre contre-expertises et arbitrage PRO-20261007-091811 (huit phrases, V3 en huit opérations).
# Refonte du 11/10/2026 (pilote de la méthode de production des ressources, arbitrage OPTIMUM-27) : ordre « l'État a-t-il
# gagné ? » -> ce qui a diminué -> qui détenait -> pourquoi l'État n'a pas encaissé -> Banque de France -> ratio -> synthèse.
# Aucun chiffre saisi : jetons {infl.*} et shortcode infl-val (scripts/update_dette_inflation.py, extrait figé et empreintes
# dans scripts/sources_inflation_dette/) ; chiffres du volet 1 par dyn-val (scripts/update_dette_dynamique.py).
donnees: [dette_inflation, dette_dynamique]
journal:  # révisions qui changent la lecture de la page (partials/page-date-visible.html affiche la plus récente)
  - {date: 2026-10-16, texte: "Correction : l'écart dû aux achats de la banque centrale culmine d'avril à juillet 2022, quatre mois à égalité à la précision affichée, et non en mai 2022."}
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_inflation"
  nom: "Surprise d'inflation 2021-2023 et dette de l'État à taux fixe de fin 2020 : érosion réelle des paiements promis, calendrier, sensibilités"
  description: "Calcul de l'auteur : érosion réelle, en euros de 2020 aux prix à la consommation français, des coupons et principaux promis sur la dette négociable de l'État à taux fixe au 31/12/2020 (OAT ligne à ligne et BTF), quand l'inflation réalisée en 2021-2023 (IPCH mensuel) remplace celle anticipée début 2021 ; cumul par année de paiement jusqu'en {infl.fin}, prévisions publiées début 2021, points morts de marché, titres indexés, consolidation simplifiée avec la Banque de France ; pour les achats de la banque centrale, exposition aux taux et durée de refixation mensuelles depuis 2015, écart de rendement 2016-2025 et comparaison avec l'Allemagne, l'Italie et l'Espagne."
  couverture_temporelle: "2021/{infl.fin}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Érosion réelle cumulée des paiements promis", unite: "milliards d'euros de 2020", description: "par année de paiement, choc fermé après 2023"}
    - {nom: "Érosion totale selon l'anticipation retenue", unite: "milliards d'euros de 2020", description: "prévisions publiées début 2021 et points morts de marché, actualisation de -1 % à +1 %"}
    - {nom: "Titres indexés : transfert auquel l'État a renoncé", unite: "milliards d'euros de 2020", description: "contrefactuel à taux fixe par points morts de même indice et de même maturité"}
    - {nom: "Hausse de la charge d'intérêts la première année si toute la courbe des taux montait d'un point (scénario)", unite: "milliards d'euros", description: "mensuel depuis mars 2015 ; dette de marché de l'État seule et ensemble État + Banque de France"}
    - {nom: "Durée moyenne de refixation de la dette de l'État à taux fixe", unite: "années", description: "mensuelle ; brute et ajustée des titres détenus par la Banque de France"}
    - {nom: "Écart entre le rendement des titres publics détenus par la Banque de France et le taux de référence de la BCE", unite: "millions d'euros", description: "annuel 2016-2025, avec les soldes de partage du revenu monétaire publiés"}
  sources:
    - "https://www.aft.gouv.fr/fr/rapports-activite"
    - "https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_midx/default/table?lang=fr"
    - "https://www.ecb.europa.eu/stats/ecb_surveys/survey_of_professional_forecasters/html/index.en.html"
    - "https://webstat.banque-france.fr/"
    - "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016D0036(01)-20250101"
    - "https://data.ecb.europa.eu/"
  mots: ["dette publique", "inflation", "OAT", "titres indexés", "anticipations d'inflation", "Banque de France", "AFT", "IPCH", "assouplissement quantitatif", "maturité de la dette", "durée de refixation"]
  fichiers: ["dette_inflation.csv", "dette_inflation.json"]
faq:
  - question: "L'État a-t-il gagné de l'argent grâce à l'inflation de 2021-2023 ?"
    answer: "Pas sous la forme d'une recette. La surprise d'inflation a réduit d'environ {infl.t} milliards d'euros de 2020 la valeur réelle des paiements promis sur la dette de l'État à taux fixe de fin 2020 (de {infl.a_bas} à {infl.a_haut} selon la prévision de départ). C'est un avantage brut, étalé jusqu'en {infl.fin}, pas la preuve d'un gain budgétaire net : refinancement, recettes et dépenses suivent d'autres mécanismes."
  - question: "Les épargnants ont-ils perdu ce que la dette a perdu en valeur réelle ?"
    answer: "On ne peut pas le chiffrer. Fin 2020, la moitié de la dette négociable de l'État était détenue par des non-résidents, près d'un quart par la Banque de France, {infl.part_assureurs} % par les assureurs. Les ménages y sont exposés par l'assurance-vie ou les dépôts, mais le rendement servi, les engagements de l'intermédiaire et les changements de détenteurs empêchent de leur attribuer une part des {infl.t} milliards."
  - question: "Les achats de dette de la BCE ont-ils rendu la France plus sensible aux taux ?"
    answer: "Oui, surtout à court terme. La Banque de France a payé ses achats d'obligations en réserves bancaires, rémunérées au taux du moment : une hausse des taux pèse donc tout de suite sur cette part, au lieu d'attendre l'échéance des obligations. Fin 2022, une hausse durable d'un point de toute la courbe des taux aurait accru la charge de la première année de {infl.qe_sc1} milliards d'euros pour l'ensemble État + Banque de France, contre {infl.qe_sm1} pour la seule dette de marché ; à cinq ans, l'écart n'est plus que de {infl.qe_r5} fois. C'est une mesure d'exposition, ni une prévision ni le coût du QE."
  - question: "Quel est le lien avec le livre Dette publique : qui paie vraiment ?"
    answer: "L'inflation est l'un des payeurs possibles de la dette : le créancier, par la perte de valeur réelle de ses titres. Cette page mesure ce canal pour 2021-2023 ; le livre examine les autres payeurs et les choix qui les désignent."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif", "explicatif-causal"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 45
  nature: "Calcul de l'auteur sur données officielles (AFT, Eurostat, BCE, Banque de France)"
  prolongement: true
dossier_dette: prolongement
dossier_dette_titre: "L'inflation a-t-elle allégé la dette ?"
dossier_dette_role: "2021-2023, dette de l'État"
dossier_dette_titre_en: "Did inflation ease the debt burden?"
dossier_dette_role_en: "2021–2023, government debt"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Calcul du&nbsp;: {{< infl-val "date_donnees" >}}</span> Dette négociable de l'État au 31&nbsp;décembre 2020 (AFT, ligne à ligne)&nbsp;; IPCH mensuel de la France 2020-2023 (Eurostat)&nbsp;; prévisions publiées entre novembre 2020 et février 2021. Télécharger&nbsp;: <a href="/dette_inflation.csv">CSV</a> · <a href="/dette_inflation.json">JSON</a> · <a href="#sources">méthode</a></p>

## Qu'est-ce que l'inflation a réellement diminué&nbsp;? {#erosion}

Fin 2020, l'État devait des coupons et des remboursements fixés en euros, ligne par ligne, jusqu'en {{< infl-val "fin" >}}. Quand les prix montent plus que prévu, chacun de ces euros achète moins&nbsp;: le créancier reçoit ce qui était promis, mais ce qui était promis vaut moins.

Pour le mesurer, on compare deux mondes. Dans le premier, l'inflation est celle que prévoyaient début 2021 les prévisionnistes professionnels interrogés par la BCE. Dans le second, c'est l'inflation réalisée, mois par mois, jusqu'en décembre 2023. Fin 2023, les prix étaient plus élevés de {{< infl-val "gap23" >}}&nbsp;% que dans le premier monde, et l'on suppose que cet écart demeure ensuite. Chaque paiement promis est converti en euros de 2020 avec le niveau des prix de sa date, dans l'un et l'autre monde&nbsp;; l'écart entre les deux valeurs, additionné sur tous les paiements, donne l'érosion.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-inflation-calendrier-m.svg" width="300" height="742">
    <img src="/img/dette-inflation-calendrier.svg" alt="Courbe cumulée, de 2021 à {{< infl-val "fin" >}}, de l'érosion réelle des paiements promis sur la dette de l'État à taux fixe de fin 2020, en trait plein jusqu'en 2023 puis en pointillé, l'écart de prix étant supposé persister : {{< infl-val "cum23" >}} milliards d'euros de 2020 fin 2023, {{< infl-val "cum27" >}} fin {{< infl-val "demi" >}}, soit environ {{< infl-val "part27" >}} %, {{< infl-val "t_exact" >}} au total ; un trait vertical au point final indique la plage selon la prévision de départ, de {{< infl-val "a_bas" >}} à {{< infl-val "a_haut" >}} milliards." width="720" height="373" loading="lazy">
  </picture>
  <figcaption>Somme non actualisée des écarts de valeur réelle, en milliards d'euros de 2020, pas de la dette effacée (calcul de l'auteur&nbsp;; AFT, Eurostat, BCE).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** L'écart entre l'inflation réalisée en 2021-2023 et celle anticipée début 2021 réduit d'environ {{< infl-val "t" >}}&nbsp;milliards d'euros de 2020 la valeur réelle des paiements promis sur la dette négociable de l'État à taux fixe existant fin 2020, sans actualisation, soit environ {{< infl-val "pts_pib" >}}&nbsp;% du PIB de 2020&nbsp;; selon la prévision retenue parmi celles publiées début 2021, de {{< infl-val "a_bas" >}} à {{< infl-val "a_haut" >}}&nbsp;milliards.

</div>

D'autres travaux trouvent davantage&nbsp;: Pallotti et al. obtiennent pour les administrations publiques françaises un montant {{< infl-val "pal_rapport" >}}&nbsp;fois plus élevé, avec un périmètre, une valorisation et un choc d'inflation différents. La confrontation à la recherche, plus bas, explique la majeure partie de cet écart, sans le réconcilier entièrement.

Ce chiffre ne dit pas que la dette a diminué de {{< infl-val "t" >}}&nbsp;milliards&nbsp;: les montants dus restent les mêmes en euros. Il ne dit pas non plus que l'État a encaissé quoi que ce soit. La courbe montre pourquoi. Fin 2023, l'écart de prix était formé, mais {{< infl-val "part23" >}}&nbsp;% seulement de l'érosion s'était traduite dans des paiements effectifs, soit {{< infl-val "cum23" >}}&nbsp;milliards. Environ {{< infl-val "part27" >}}&nbsp;% le seront fin {{< infl-val "demi" >}}&nbsp;; le reste attend les échéances lointaines, jusqu'en {{< infl-val "fin" >}}. Le choc a duré trois ans&nbsp;; ses effets sur la dette héritée se paient sur plusieurs décennies.

Les montants sont exprimés en euros de 2020 aux prix à la consommation français&nbsp;: ce que représentent ces paiements pour un ménage qui dépense en France. Ce chiffre n'est pas non plus celui du ratio de dette publié dans le dossier, qui mesure autre chose&nbsp;: [voir la section sur le ratio](#ratio).

## Qui détenait les créances dont la valeur réelle a diminué&nbsp;? {#detenteurs}

Fin 2020, la dette négociable de l'État était détenue, en valeur de marché, à {{< infl-val "part_non_residents" >}}&nbsp;% par des non-résidents, {{< infl-val "part_BdF" >}}&nbsp;% par la Banque de France, {{< infl-val "part_assureurs" >}}&nbsp;% par les assureurs, {{< infl-val "part_banques" >}}&nbsp;% par les banques et {{< infl-val "part_fonds_autres" >}}&nbsp;% par les fonds et les autres détenteurs. C'est une répartition des porteurs, pas une répartition des pertes.

**Le porteur direct n'est pas forcément le perdant final.** Les ménages ne détiennent presque pas de titres de l'État en direct. Ils y sont exposés par leur assurance-vie ou leurs dépôts, mais ce lien ne permet pas de leur attribuer une fraction des {{< infl-val "t" >}}&nbsp;milliards&nbsp;: le rendement servi aux assurés, les engagements nominaux de l'assureur ou de la banque, et les titres qui changent de mains au fil des années modifient qui supporte finalement la perte. La moitié des titres était détenue hors de France&nbsp;; près d'un quart par la banque centrale, dont la situation est examinée [plus bas](#achats-banque-centrale).

Une allocation mécanique selon ces parts figure dans [la méthode](#sources)&nbsp;; elle ne mesure pas qui a perdu.

## Pourquoi l'État n'a pas encaissé {{< infl-val "t" >}}&nbsp;milliards {#gain-net}

La première raison est sur la courbe&nbsp;: l'érosion se réalise au rythme des paiements, jusqu'en {{< infl-val "fin" >}}. D'autres s'y ajoutent.

**Parce que l'État a ensuite emprunté plus cher.** À partir de 2022, il a refinancé ses échéances à des taux plus élevés. Une partie de cette hausse tient à la révision des anticipations d'inflation, une autre à des taux réels et à des primes de risque qui ont leurs propres causes&nbsp;: les données disponibles ne permettent pas de dire quelle part de la hausse ultérieure des coûts de financement l'épisode a causée. Dans le contrefactuel retenu, cette hausse ne rend pas l'érosion déjà acquise&nbsp;: elle porte sur les nouveaux financements, pas sur les paiements déjà promis.

**Parce que l'inflation a joué ailleurs dans le budget, hors de ce calcul.** Elle a pu gonfler des recettes exprimées en euros courants, la TVA par exemple&nbsp;; elle a aussi conduit à revaloriser les pensions et les prestations, et à prendre des mesures de soutien. Ce qui est démontré ici&nbsp;: la surprise d'inflation a réduit la valeur réelle de paiements déjà promis. Ce qui est possible&nbsp;: l'État a pu bénéficier d'autres canaux, notamment sur certaines recettes nominales. Ce qui n'est pas établi&nbsp;: le solde budgétaire total de la surprise d'inflation. L'effet net sur les recettes n'est pas chiffré ici, faute d'une estimation causale comparable&nbsp;: même périmètre, même choc imprévu, même période. L'avantage brut mesuré n'est donc pas un gain budgétaire net identifiable, ce qui ne veut pas dire qu'aucun gain n'a existé.

**Parce que les titres indexés ont joué en sens inverse.** Fin 2020, {{< infl-val "idx_n" >}}&nbsp;titres indexés sur l'inflation, pour {{< infl-val "idx_encours" >}}&nbsp;milliards d'euros, échappaient à l'érosion. Si l'État les avait émis à taux fixe plutôt qu'indexés, l'érosion aurait été plus forte d'environ {{< infl-val "idx" >}}&nbsp;milliards&nbsp;: ces titres ont protégé leurs porteurs.

**Parce que le montant dépend de l'unité de mesure.** Mesurée en unités de production intérieure (déflateur du PIB) plutôt qu'en pouvoir d'achat du consommateur, la même érosion est plus faible, de l'ordre de {{< infl-val "defl_bas" >}} à {{< infl-val "defl_haut" >}}&nbsp;milliards ([détail](#sensibilite))&nbsp;; aucune des deux unités ne mesure un gain budgétaire.

## La Banque de France&nbsp;: pourquoi les taux peuvent agir plus vite {#achats-banque-centrale}

La banque centrale change la vitesse à laquelle une hausse des taux pèse sur les finances publiques. Une obligation à taux fixe ne coûte plus cher qu'au moment où elle est remplacée, à son échéance, parfois dix ans plus tard. Or, de 2015 à 2022, la Banque de France a acheté une partie de ces obligations et les a payées avec des réserves bancaires, l'argent que les banques déposent chez elle, dont la rémunération suit les taux du moment. Pour l'État et sa banque centrale pris ensemble, une hausse des taux pèse donc tout de suite sur cette part, au lieu d'attendre les échéances.

Fin 2022, une hausse durable d'un point de toute la courbe des taux aurait accru la charge d'intérêts de la première année de {{< infl-val "qe_sc1" >}}&nbsp;milliards d'euros pour l'ensemble formé par l'État et la Banque de France ({{< infl-val "qe_sc1_pib" >}}&nbsp;point de PIB), contre {{< infl-val "qe_sm1" >}}&nbsp;milliards pour la seule dette de marché&nbsp;: {{< infl-val "qe_r1" >}}&nbsp;fois plus. À cinq ans, l'écart n'est plus que de {{< infl-val "qe_r5" >}}&nbsp;fois ({{< infl-val "qe_sc5" >}} contre {{< infl-val "qe_sm5" >}}&nbsp;milliards)&nbsp;: les achats de la banque centrale ont surtout rapproché dans le temps la refixation des taux. Ce scénario mesure une exposition, il ne prévoit rien&nbsp;: une hausse des taux directeurs ne déplace pas nécessairement toute la courbe.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/dette-inflation-achats-m.svg" width="300" height="700">
    <img src="/img/dette-inflation-achats.svg" alt="Deux courbes mensuelles, de mars 2015 à {{< infl-val "qe_dern" >}}, de la hausse de la charge d'intérêts la première année si toute la courbe des taux augmentait durablement d'un point : pour l'ensemble État + Banque de France, {{< infl-val "qe_sc1" >}} milliards d'euros fin 2022 et {{< infl-val "qe_sc1_d" >}} en {{< infl-val "qe_dern" >}} ; pour la seule dette de marché de l'État, {{< infl-val "qe_sm1" >}} fin 2022 et {{< infl-val "qe_sm1_d" >}} en {{< infl-val "qe_dern" >}}." width="720" height="373" loading="lazy">
  </picture>
  <figcaption>Scénario à encours constant, non prévision&nbsp;; l'ensemble État + Banque de France est un périmètre d'analyse, non des intérêts enregistrés au budget (calcul de l'auteur&nbsp;; AFT, Banque de France, BCE).</figcaption>
</figure>

**Comment.** Le mécanisme passe par deux canaux, qui suivent des règles différentes et donnent des mesures différentes.

**Canal économique&nbsp;: les réserves, rémunérées au taux de dépôt.** Parce que le taux de dépôt est resté à −0,5&nbsp;% jusqu'en juillet 2022 pendant que les prix montaient, les porteurs de réserves ont obtenu des rendements réels négatifs, comme les porteurs de créances nominales à taux fixe&nbsp;: dans une consolidation simplifiée, l'érosion vaut encore environ {{< infl-val "cons23" >}}&nbsp;milliards fin 2023. En 2024 et 2025, les réserves sont rémunérées au-dessus de l'inflation, et l'érosion consolidée tombe à environ {{< infl-val "cons25" >}}&nbsp;milliards fin 2025&nbsp;: une partie de l'avantage est déjà rendue, alors que les paiements s'étalent jusqu'en {{< infl-val "fin" >}}. C'est un modèle simplifié, non une consolidation statistique&nbsp;: la Banque de France n'appartient pas aux administrations publiques, et ses pertes atteignent l'État par ses dividendes et son impôt, avec retard.

<details class="repli"><summary>La formule de la consolidation simplifiée</summary>

érosion consolidée à la date *t* = érosion × (1 − part détenue par la Banque de France) + somme, jusqu'à *t*, des pertes réelles des porteurs de réserves,

où la perte réelle d'une année vaut l'encours des réserves en début d'année, en euros de 2020, multiplié par l'écart entre le rendement réel attendu (taux de dépôt de −0,5&nbsp;% et inflation anticipée) et le rendement réel obtenu (taux de dépôt et inflation réalisés). Part de la Banque de France fin 2020&nbsp;: {{< infl-val "s_bdf" >}}&nbsp;% de la dette négociable de l'État, en valeur de marché.

</details>

**Canal comptable&nbsp;: le revenu mis en commun, au taux de référence.** Pour calculer le revenu que les banques centrales de la zone euro mettent en commun, et pour ce seul calcul, les titres de l'État détenus par la Banque de France sont réputés rapporter le taux de référence de la BCE, quel que soit leur coupon, qui reste inchangé (décision (UE) 2016/2248). Dans la mesure consolidée retenue ici, la part détenue par la Banque de France est donc traitée comme une dette dont le coût se refixe aussitôt au taux de référence, à la place d'une dette à taux fixe de longue durée. Depuis 2025, le taux de référence est le taux de dépôt.

<details class="repli"><summary>Durée de refixation, retournement du portage et comptes de la Banque de France</summary>

**La durée de refixation.** Pendant les achats, l'Agence France Trésor a allongé ses émissions&nbsp;: leur durée moyenne est passée de {{< infl-val "qe_em14" >}}&nbsp;ans en 2014 à une valeur comprise entre {{< infl-val "qe_em_min" >}} et {{< infl-val "qe_em_max" >}}&nbsp;ans chaque année de 2016 à 2022, et la durée moyenne de refixation de la dette de l'État à taux fixe de {{< infl-val "qe_atr15" >}}&nbsp;ans en mars 2015 à {{< infl-val "qe_atr22" >}}&nbsp;ans fin 2022. En comptant, par convention, les titres détenus par la Banque de France comme se refixant immédiatement, l'indicateur ajusté est resté entre {{< infl-val "qe_aj_min" >}} et {{< infl-val "qe_aj_max" >}}&nbsp;ans sur la même période. Depuis la fin des achats nets, la Banque de France détient une part plus faible de cette dette, {{< infl-val "qe_h_d" >}}&nbsp;% en {{< infl-val "qe_dern" >}} contre {{< infl-val "qe_h22" >}}&nbsp;% fin 2022&nbsp;: l'écart entre les deux courbes se resserre, sans disparaître ({{< infl-val "qe_r_d" >}}&nbsp;fois en {{< infl-val "qe_dern" >}}).

**Le retournement du portage.** Selon les comptes de la Banque de France, ses titres de politique monétaire rapportaient de {{< infl-val "qe_rdt_min" >}} à {{< infl-val "qe_rdt_max" >}}&nbsp;% par an, pendant que le taux de référence de la BCE, proche de zéro jusqu'en 2021, montait jusqu'à environ {{< infl-val "qe_tref_max" >}}&nbsp;% en moyenne annuelle. Sur les titres publics français détenus, l'écart entre ce rendement et ce taux a représenté environ +{{< infl-val "qe_gain" >}}&nbsp;milliards d'euros cumulés de 2016 à 2022, puis −{{< infl-val "qe_cout" >}} de 2023 à 2025&nbsp;: un solde de −{{< infl-val "qe_solde" >}}&nbsp;milliards sur la période observée, alors que la Banque de France détient encore une partie de ces titres. Le partage du revenu monétaire entre les banques centrales de la zone euro le déplace de quelques milliards, entre −{{< infl-val "qe_net_haut" >}} et −{{< infl-val "qe_net_bas" >}}. Le rendement retenu est celui de tout le portefeuille de politique monétaire, obligations d'entreprises comprises, qui rapportent vraisemblablement plus que les titres publics&nbsp;: sur les seuls titres publics, le solde serait plutôt plus défavorable. Ce n'est ni une dépense du budget de l'État ni le coût du QE&nbsp;: le calcul garde les taux de marché tels qu'ils ont été, et l'on ne sait pas ce qu'ils auraient été sans les achats.

**Ce que montrent les comptes de la Banque de France.** La Banque de France, qui a conduit ces achats pour l'Eurosystème, met en regard ses pertes depuis 2023 et les bénéfices qu'elle a dégagés et versés à l'État auparavant. Ses comptes, qui portent sur tout son bilan, le confirment&nbsp;: un résultat ordinaire de {{< infl-val "qe_bdf_ro_avant" >}}&nbsp;milliards d'euros de 2015 à 2022, dont {{< infl-val "qe_bdf_verse" >}}&nbsp;milliards versés à l'État en impôt et en dividende, puis de −{{< infl-val "qe_bdf_ro_apres" >}}&nbsp;milliards de 2023 à 2025. Sur le périmètre plus étroit des seuls titres publics français, le portage ne s'équilibre pas sur la période observée&nbsp;: −{{< infl-val "qe_solde" >}}&nbsp;milliards. Les deux constats sont exacts&nbsp;; ils ne portent pas sur le même objet.

**Ailleurs dans la zone euro.** La règle vaut pour toutes les banques centrales de l'Eurosystème. Sur une base homogène publiée par la BCE, qui couvre toutes les administrations publiques et leurs prêts, en fin d'année, le rapport entre l'exposition de la première année de l'ensemble consolidé et celle de la dette de marché valait de {{< infl-val "qe_t4_2015_bas" >}} à {{< infl-val "qe_t4_2015_haut" >}} en 2015 selon les pays&nbsp;; son maximum va de {{< infl-val "qe_t4_bas" >}} à {{< infl-val "qe_t4_haut" >}} en Allemagne, en Italie, en Espagne et en France. Pour la France, cette base large donne au plus {{< infl-val "qe_t4_fr" >}}, contre {{< infl-val "qe_r1" >}} fin 2022 dans la mesure centrée sur la dette de l'État à taux fixe&nbsp;: les deux périmètres diffèrent. Les écarts entre pays tiennent à la structure de leur dette de marché&nbsp;: ils ne font pas un classement.

</details>

Ces mesures ne s'additionnent pas et ne se retranchent pas les unes des autres&nbsp;: aucune combinaison ne donne un gain net.

<details class="repli"><summary>Pourquoi ces quatre montants ne s'additionnent-ils pas&nbsp;?</summary>

| Chiffre | Ce qu'il mesure |
|---|---|
| {{< infl-val "cons23" >}} puis {{< infl-val "cons25" >}}&nbsp;Md€ de 2020 | l'érosion dans la consolidation simplifiée, fin 2023 et fin 2025 |
| {{< infl-val "qe_sc1" >}} contre {{< infl-val "qe_sm1" >}}&nbsp;Md€ | la sensibilité de la première année à un point de taux en plus, fin 2022, en scénario |
| −{{< infl-val "qe_solde" >}}&nbsp;Md€ | le portage cumulé des seuls titres publics français détenus, 2016-2025 |
| −{{< infl-val "qe_bdf_ro_apres" >}}&nbsp;Md€ | le résultat ordinaire de la Banque de France, tout son bilan, 2023-2025 |

</details>

## Pourquoi ce n'est pas le chiffre du ratio dette/PIB {#ratio}

Le volet du dossier [«&nbsp;Pourquoi la dette publique augmente-t-elle&nbsp;?&nbsp;»](/pourquoi-la-dette-publique-augmente/) attribue à l'effet des taux et de la croissance une contribution de −{{< dyn-val "effet_2021_2023" >}}&nbsp;points de PIB à la variation du ratio de dette en 2021-2023. Ce n'est pas la baisse observée du ratio&nbsp;: il n'a reculé que de {{< dyn-val "recul_2021_2023" >}}&nbsp;points, surtout parce que les déficits primaires l'ont poussé de {{< dyn-val "deficits_2021_2023" >}}&nbsp;points dans l'autre sens. Et les {{< infl-val "pts_pib" >}}&nbsp;% du PIB de 2020 de cette page ne sont pas {{< infl-val "pts_pib" >}}&nbsp;points de baisse du ratio&nbsp;: le premier chiffre réagit à toute la croissance du PIB nominal, inflation prévue comprise, pour toutes les administrations publiques&nbsp;; le second ne retient que la part non prévue de l'inflation, sur les seuls paiements déjà promis par l'État. Les rapprocher demanderait une décomposition qui n'est pas faite ici.

## Ce qui fait varier le chiffre {#sensibilite}

La plage publiée, de {{< infl-val "a_bas" >}} à {{< infl-val "a_haut" >}}&nbsp;milliards, vient de la prévision de départ. La référence, l'enquête de la BCE, n'a pas été choisie pour son niveau&nbsp;: c'est la seule des quatre prévisions qui couvre tout l'horizon des paiements, et les trois prévisions propres à la France encadrent son résultat. Les points morts de marché et l'actualisation l'élargissent&nbsp;; le calendrier des prix explique l'écart avec le calcul en moyennes annuelles.

<details class="repli"><summary>Unité de mesure, prévisions, points morts, actualisation et calendrier des prix</summary>

**L'unité de mesure.** Exprimée en unités de production intérieure (déflateur du PIB) plutôt qu'en pouvoir d'achat du consommateur, la même érosion est de l'ordre de {{< infl-val "defl_bas" >}} à {{< infl-val "defl_haut" >}}&nbsp;milliards. Ce calcul se fait en moyennes annuelles, où l'érosion aux prix à la consommation vaut {{< infl-val "t_annuel" >}}&nbsp;milliards au lieu de {{< infl-val "t_exact" >}} en suivant les prix mois par mois. Les deux unités répondent à des questions différentes&nbsp;; aucune ne mesure un gain budgétaire. L'écart entre les deux indices de prix est mesuré ici, non expliqué.

**La prévision de départ.** Quatre prévisions d'inflation publiées entre novembre 2020 et février 2021 donnent&nbsp;: {{< infl-val "spf" >}}&nbsp;milliards avec l'enquête de la BCE auprès des prévisionnistes professionnels (janvier 2021, zone euro), {{< infl-val "bdf" >}} avec les projections de la Banque de France (décembre 2020), {{< infl-val "ce_aut" >}} et {{< infl-val "ce_hiv" >}} avec celles de la Commission européenne (automne 2020, hiver 2021). La Commission ne publiait pas d'horizon 2023&nbsp;: sa prévision de 2022, 1,5&nbsp;%, est reconduite pour 2023, son dernier horizon publié. Au-delà de 2023, toutes reviennent au chemin de l'enquête de la BCE, si bien que seules les années de l'épisode diffèrent. L'enquête de la BCE sert de référence parce qu'elle est la seule des quatre à couvrir tout l'horizon des paiements, au-delà de 2023 jusqu'au long terme, et qu'elle fixe une date d'information unique, janvier 2021, quand le niveau des prix de décembre 2020 est connu&nbsp;; elle porte sur la zone euro, et les trois prévisions propres à la France encadrent le résultat qu'elle donne.

**Les points morts d'inflation.** Les écarts de rendement entre titres nominaux et indexés au 31&nbsp;décembre 2020 (AFT) donneraient davantage&nbsp;: {{< infl-val "b_fr" >}}&nbsp;milliards avec le point mort français à 10&nbsp;ans, {{< infl-val "b_eu" >}} avec celui de la zone euro. Ils incorporent des primes de risque et de liquidité, qui les tiraient alors vers le bas&nbsp;: ils ne servent ici qu'à la sensibilité, non à la plage.

**L'actualisation.** Les montants sont sommés sans actualisation. Actualisés à un taux réel de −1&nbsp;% à +1&nbsp;%, ils vont de {{< infl-val "a_tout_bas" >}} à {{< infl-val "a_tout_haut" >}}&nbsp;milliards sur l'ensemble des prévisions.

**Le calendrier des prix.** Le calcul suit l'IPCH mois par mois, à la date de chaque paiement. En moyennes annuelles, il donnait {{< infl-val "t_annuel" >}}&nbsp;milliards&nbsp;: l'écart tient surtout à ce que l'écart de niveau qui persiste après l'épisode est celui de décembre 2023, plus élevé que celui de la moyenne de 2023.

</details>

## Ce que ces données ne disent pas {#limites}

Elles ne mesurent pas l'effet budgétaire total de l'inflation (recettes, prestations indexées, mesures de soutien, actifs nominaux des administrations), ni la dette de la Sécurité sociale ou des collectivités. Elles ne disent pas qui a finalement supporté la perte, ni quelle part de la hausse des taux l'épisode a causée. Elles reposent sur un contrefactuel&nbsp;: une autre anticipation de départ donne un autre chiffre, dans la plage indiquée. Pour les achats de la banque centrale, elles mesurent une exposition et un écart de rendement&nbsp;: ni le coût causal du QE, ni ce qu'auraient été les taux sans lui, ni le revenu que l'Eurosystème tire des billets et des réserves non rémunérées, ni la soutenabilité de la dette.

{{< confrontation-recherche verifie="2026-10-08" publie="oui" resume="l'ordre de grandeur est retrouvé chez Pallotti et al. une fois les conventions alignées, mais la littérature ne permet pas d'y lire un gain budgétaire net ; l'effet des achats sur la durée de refixation est proche de celui que publiait l'OCDE" >}}
**Mesuré ici.** L'érosion réelle des paiements promis sur la dette de l'État à taux fixe de fin 2020, au rythme où l'écart de prix s'est formé, avec son calendrier de réalisation.

**Cohérent avec.** Pallotti, Paz-Pardo, Slacalek, Tristani et Violante mesurent un gain bien plus élevé pour les administrations publiques françaises, {{< infl-val "pal_rapport" >}}&nbsp;fois le nôtre dans une même unité. L'écart se décompose&nbsp;: leur choc est instantané et mesuré de décembre à décembre contre une anticipation plus basse, ils valorisent la dette au prix de marché, et leur périmètre couvre toutes les administrations publiques et leurs titres indexés. Ces trois facteurs expliquent environ {{< infl-val "pal_explique" >}}&nbsp;% de l'écart&nbsp;; un résidu d'environ {{< infl-val "pal_residu" >}}&nbsp;% reste à réconcilier. Les deux calculs ne portent pas sur le même objet. Hilscher, Raviv et Reis ont posé la méthode qui rapporte l'allègement à la maturité de la dette&nbsp;; Andreolli et Rey l'appliquent ex post à la France jusqu'à la mi-2022. Pour les achats de la banque centrale, l'OCDE publiait l'indicateur ajusté de la France en un seul point, fin 2022&nbsp;: l'effet des achats que l'on lit sur sa figure, {{< infl-val "qe_ocde_effet" >}}&nbsp;an, est proche de celui que nous mesurons dans sa convention ({{< infl-val "qe_nous_effet" >}}). La Bundesbank estimait en 2024, sans publier sa méthode, que la durée de refixation ajustée pouvait être jusqu'à deux ans plus courte que la maturité résiduelle&nbsp;; pour la France, l'écart dû aux achats culmine ici à {{< infl-val "qe_e1_max" >}}&nbsp;ans ({{< infl-val "qe_e1_date" >}}). L'OBR mesurait le même raccourcissement au Royaume-Uni.

**Mis en danger par.** Toute lecture du montant comme un gain de l'État. Pallotti et al. retranchent eux-mêmes de leur gain brut les coûts budgétaires de l'épisode&nbsp;: soutien, pensions, achats publics. Et la Bundesbank rappelait en 2022 que, pour la part achetée par la banque centrale, l'État paie de fait le taux de dépôt plutôt que le taux de l'obligation&nbsp;: c'est l'objet de la consolidation simplifiée ci-dessus.

**Non établi.** La part de la hausse ultérieure des taux causée par l'épisode, l'incidence finale de la perte, et ce qu'auraient été les taux sans les achats de la banque centrale.

**Références lues**

- Pallotti, F., Paz-Pardo, G., Slacalek, J., Tristani, O. et Violante, G. L. (2024), «&nbsp;Who Bears the Costs of Inflation&nbsp;? Euro Area Households and the 2021–2023 Shock&nbsp;», [NBER Working Paper 31896](https://www.nber.org/papers/w31896), révision de septembre 2024 (publié dans le *Journal of Monetary Economics*, 148&nbsp;; version de la revue non lue).
- Hilscher, J., Raviv, A. et Reis, R. (2022), «&nbsp;Inflating Away the Public Debt&nbsp;? An Empirical Assessment&nbsp;», *Review of Financial Studies*, 35(3), p.&nbsp;1553-1595, [doi:10.1093/rfs/hhab018](https://doi.org/10.1093/rfs/hhab018).
- Deutsche Bundesbank (2022), «&nbsp;Government debt in the euro area&nbsp;: developments in creditor structure&nbsp;», *Monthly Report*, juillet 2022, p.&nbsp;77 et suivantes.
- OCDE (2023), [*Sovereign Borrowing Outlook for OECD Countries 2023*](https://www.oecd.org/en/publications/oecd-sovereign-borrowing-outlook-2023_09b4cfba-en.html), chapitre 1, figure 1.16 (durée moyenne de refixation ajustée des titres détenus par la banque centrale, fin 2022).
- Deutsche Bundesbank (2024), *Monthly Report*, avril 2024, sur la structure des créanciers de la dette publique de la zone euro.
- Office for Budget Responsibility (2021), [*Economic and fiscal outlook*, mars 2021](https://obr.uk/efo/economic-and-fiscal-outlook-march-2021/), encadré 4.1.
- Andreolli, M. et Rey, H. (2024), «&nbsp;Fiscal Consequences of Missing an Inflation Target&nbsp;», version de mars 2024 ([NBER Working Paper 30819](https://www.nber.org/papers/w30819)&nbsp;; *IMF Economic Review*, 72(2)).
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce que l'on sait, et ce qui reste indéterminé {#retenir}

**Une dette ancienne peut s'alléger en valeur réelle sans diminuer en euros.** L'inflation imprévue de 2021-2023 a allégé d'environ {{< infl-val "t" >}}&nbsp;milliards d'euros de 2020 les engagements nominaux hérités de l'État&nbsp;: c'est un avantage brut, mesurable dans le scénario retenu.

**Un avantage brut n'est pas un gain budgétaire net.** Il ne constitue ni une recette de {{< infl-val "t" >}}&nbsp;milliards, ni la preuve d'un gain budgétaire net équivalent&nbsp;: les recettes, les dépenses et le refinancement suivent d'autres mécanismes.

**La date du choc n'est pas celle de ses effets.** L'érosion se répartit sur les paiements jusqu'en {{< infl-val "fin" >}}, si l'écart de prix persiste.

**La structure financière règle la vitesse de transmission des taux.** Une obligation à taux fixe ne coûte plus cher qu'à son échéance&nbsp;; la part que la Banque de France a payée en réserves, rémunérées au taux du moment, fait sentir une hausse des taux tout de suite à l'ensemble formé par l'État et sa banque centrale.

Ce que l'on ne sait pas&nbsp;: qui a finalement supporté la perte, et quelle part de la hausse des taux l'épisode a causée.

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
Cette page mesure ce que l'inflation de 2021-2023 a retiré, en valeur réelle, à la dette ancienne de l'État, et ce qu'on ne peut pas en conclure. L'inflation n'est qu'un des payeurs possibles de la dette&nbsp;: le contribuable, l'usager des services publics, le créancier en sont d'autres. Le livre examine ces choix et leurs conséquences, chiffres officiels à l'appui.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

**Dette.** Agence France Trésor, [*Rapport d'activité 2020*](https://www.aft.gouv.fr/fr/rapports-activite), encours de la dette négociable de l'État au 31&nbsp;décembre 2020, ligne à ligne&nbsp;: OAT à taux fixe (nominal, coupon, date d'échéance) et BTF. Chaque coupon est payé à la date anniversaire de l'échéance, le principal à l'échéance&nbsp;; les BTF de fin 2020 sont répartis sur les douze mois de 2021.

**Prix.** Eurostat, [IPCH mensuel de la France](https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_midx/default/table?lang=fr) (`prc_hicp_midx`, base 2015), contrôlé contre le relevé de l'Insee sur les 36&nbsp;mois de 2021-2023. Le chemin attendu part du niveau de décembre 2020, connu en janvier 2021, croît chaque année au taux anticipé et porte la saisonnalité habituelle des prix (2017-2020)&nbsp;; sans correction saisonnière, le résultat ne change presque pas. Les montants sont convertis en euros de la moyenne de 2020. Le calcul en unités de production intérieure utilise le déflateur du PIB annuel (Eurostat), contre l'anticipation d'IPCH de l'enquête de la BCE et contre le déflateur prévu par la Commission à l'automne 2020.

**Anticipations.** BCE, [*Survey of Professional Forecasters*](https://www.ecb.europa.eu/stats/ecb_surveys/survey_of_professional_forecasters/html/index.en.html), premier trimestre 2021 (zone euro&nbsp;; 2024 interpolé entre ses horizons 2023 et 2025, puis son anticipation de long terme)&nbsp;; Banque de France, projections de décembre 2020&nbsp;; Commission européenne, prévisions d'automne 2020 et d'hiver 2021. Points morts au 31&nbsp;décembre 2020&nbsp;: AFT (source Bloomberg).

**Titres indexés.** Les {{< infl-val "idx_n" >}}&nbsp;titres indexés de fin 2020 reçoivent, dans le contrefactuel, un coupon fixe égal à leur coupon réel augmenté du point mort de même indice et de même maturité&nbsp;: au 31&nbsp;décembre 2020, l'AFT publie quatre points (France 5 et 10&nbsp;ans, zone euro 10 et 30&nbsp;ans), interpolés selon la maturité résiduelle&nbsp;; faute de point court pour la zone euro, la courbe française est décalée de l'écart observé à 10&nbsp;ans. Résultat&nbsp;: {{< infl-val "idx_j" >}}&nbsp;milliards, contre {{< infl-val "idx_1" >}} avec le seul point mort à 10&nbsp;ans de la zone euro. En ajoutant l'écart entre l'indice de chaque titre et l'IPCH français ({{< infl-val "idx_ecart" >}}&nbsp;milliards), ce que la protection vendue aux porteurs a coûté à l'État, une fois le risque réalisé, atteint {{< infl-val "idx_tot" >}}&nbsp;milliards. La charge d'indexation inscrite au budget, qui a culminé à {{< infl-val "charge22" >}}&nbsp;milliards d'euros courants en 2022 ({{< infl-val "charge_cum" >}}&nbsp;milliards de 2021 à 2025, AFT), est un flux annuel sur tout l'encours indexé de chaque année, émissions nouvelles comprises&nbsp;: ce n'est pas la même grandeur que les quelque {{< infl-val "idx" >}}&nbsp;milliards du contrefactuel des titres de fin 2020.

**Détenteurs et parts de la Banque de France.** Trois parts de la Banque de France apparaissent sur cette page, sur deux périmètres et deux valorisations&nbsp;: {{< infl-val "s_bdf" >}}&nbsp;% de toute la dette négociable de l'État fin 2020, en valeur de marché (Banque de France, [Webstat](https://webstat.banque-france.fr/), détention par secteur&nbsp;; même source pour la répartition entre détenteurs)&nbsp;; {{< infl-val "qe_h22" >}}&nbsp;% fin 2022 et {{< infl-val "qe_h_d" >}}&nbsp;% en {{< infl-val "qe_dern" >}} de la dette de l'État à taux fixe, en valeur nominale (part en valeur de marché appliquée à l'encours nominal). La part des fonds et des autres détenteurs est arrondie sur les parts exactes. Réserves de la consolidation simplifiée&nbsp;: approchées par la valeur de marché des avoirs de la Banque de France en titres de l'État en début d'année&nbsp;; taux de dépôt de la BCE en moyenne annuelle.

**Achats de la banque centrale.** Échéancier de la dette négociable de l'État, ligne à ligne, à chaque fin de mois depuis décembre 2013, tiré des bulletins mensuels de l'AFT&nbsp;; la durée de vie moyenne recalculée retrouve celle de chaque bulletin à une demi-journée près. Titres de l'État détenus par la Banque de France, tous portefeuilles&nbsp;: Banque de France, Webstat, part en valeur de marché appliquée à l'encours nominal, sous la borne que donnent les statistiques de finances publiques de la BCE. Maturité moyenne des titres détenus&nbsp;: BCE&nbsp;; leur répartition par échéance n'est pas publiée, on la suppose identique à celle du stock, ce qui surestime légèrement l'exposition consolidée. Règle du revenu mis en commun&nbsp;: [décision (UE) 2016/2248](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02016D0036(01)-20250101), version consolidée au 1<sup>er</sup>&nbsp;janvier 2025 (taux de référence&nbsp;: taux des opérations principales de refinancement, puis taux de la facilité de dépôt à partir de 2025). Rendement&nbsp;: intérêts des titres de politique monétaire rapportés à leur encours moyen, et soldes de partage du revenu monétaire, dans les rapports annuels de la Banque de France. Comparaison entre pays&nbsp;: BCE, statistiques de finances publiques (dette par maturité résiduelle, dette détenue par la banque centrale nationale). Le revenu que l'Eurosystème tire des billets et des réserves non rémunérées reste hors mesure. Ce calcul a été soumis à une contre-expertise externe, qui a fait corriger la formulation du résultat (déplacement de toute la courbe, date de fin 2022) et vérifier, dans les comptes, l'effet de la redistribution entre banques centrales.

**Rapprochement avec Pallotti et al.** Fait sur la version du calcul en moyennes annuelles ({{< infl-val "t_annuel" >}}&nbsp;milliards)&nbsp;: nous expliquons environ {{< infl-val "pal_explique" >}}&nbsp;% de l'écart avec Pallotti et al.&nbsp;; un résidu d'environ {{< infl-val "pal_residu" >}}&nbsp;% reste à réconcilier.

<details class="repli"><summary>Allocation mécanique de l'érosion selon la structure de détention de fin 2020, qui n'identifie pas l'incidence finale</summary>

Répartie selon les parts de détention de la dette négociable de l'État à la fin de 2020 (Banque de France, valeur de marché), l'érosion de {{< infl-val "t" >}}&nbsp;milliards donnerait&nbsp;: non-résidents {{< infl-val "part_non_residents" >}}&nbsp;%, soit {{< infl-val "alloc_non_residents" >}}&nbsp;milliards&nbsp;; Banque de France {{< infl-val "part_BdF" >}}&nbsp;%, {{< infl-val "alloc_BdF" >}}&nbsp;milliards&nbsp;; assureurs {{< infl-val "part_assureurs" >}}&nbsp;%, {{< infl-val "alloc_assureurs" >}}&nbsp;milliards&nbsp;; banques {{< infl-val "part_banques" >}}&nbsp;%, {{< infl-val "alloc_banques" >}}&nbsp;milliards&nbsp;; fonds et autres détenteurs {{< infl-val "part_fonds_autres" >}}&nbsp;%, {{< infl-val "alloc_fonds_autres" >}}&nbsp;milliards (parts arrondies sur les valeurs exactes&nbsp;: les fonds et les autres détenteurs pèsent chacun un peu plus de 1&nbsp;%).

C'est une allocation mécanique, pas une mesure de qui a perdu. Les titres changent de mains au fil des années, et l'érosion, calculée sur des flux, est répartie selon des parts mesurées en valeur de marché. Le porteur direct n'est pas forcément le perdant final&nbsp;: un assureur a lui-même des engagements nominaux envers ses assurés, une banque des dépôts.

</details>

Les chiffres de cette page viennent d'un calcul de l'auteur, reproductible, dont l'extrait est archivé avec ses empreintes&nbsp;; le script qui écrit la page vérifie les principales affirmations chiffrées et s'arrête si leurs conditions ne sont plus remplies. Plusieurs valeurs publiées sont transcrites dans ce calcul avec leur source&nbsp;: la charge d'indexation inscrite au budget, les taux annuels des OAT et des BTF et les points morts d'inflation publiés par l'Agence France Trésor, et les prévisions d'inflation de la Banque de France et de la Commission. Avant l'écriture, le calcul a été soumis à des contre-expertises externes, qui ont fait changer le calendrier des prix, la construction de la plage et le traitement des titres indexés.

{{< reutiliser figures="figures_inflation" jeu="dette_inflation" sources="AFT, Eurostat, BCE, Banque de France, Commission européenne" donnees="L'érosion réelle cumulée par année de paiement, les résultats selon chaque prévision et chaque point mort, les titres indexés, la consolidation simplifiée, l'allocation mécanique par détenteur et, pour les achats de la banque centrale, l'exposition mensuelle, la durée de refixation et l'écart de rendement par année ; le même contenu existe en CSV, au format long." >}}
Dans le contrefactuel de cette page, l'écart entre l'inflation réalisée en 2021-2023 et celle anticipée début 2021 réduit d'environ {{< infl-val "t" >}}&nbsp;milliards d'euros de 2020 la valeur réelle des paiements promis sur la dette de l'État à taux fixe de fin 2020 (de {{< infl-val "a_bas" >}} à {{< infl-val "a_haut" >}} selon la prévision retenue)&nbsp;; environ {{< infl-val "part27" >}}&nbsp;% se matérialise d'ici fin {{< infl-val "demi" >}}. C'est un avantage brut pour l'État, pas la preuve d'un gain budgétaire net équivalent.
{{< /reutiliser >}}
