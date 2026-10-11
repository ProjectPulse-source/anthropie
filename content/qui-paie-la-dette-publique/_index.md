---
title: "Qui paie vraiment la dette publique ?"
description: "Qui paie la dette publique ? Détenir n'est pas payer : impôts, dépenses et inflation ne répartissent pas l'effort entre les mêmes groupes. Données officielles."
chapo: "Un même effort de {qp.exp_effort} milliards d'euros ne tombe pas sur les mêmes ménages selon la décision prise : par l'enseignement, il pèse surtout sur les plus modestes, par l'impôt sur les plus aisés. Qui paie la dette publique dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir."
date: 2026-07-04
lastmod: 2026-10-11
donnees: [dette_officielle]
og_title: "Qui paie vraiment la dette publique ? — ce que montrent les données — S. Lalut"
og_image: "images/og-qui-paie-dette.jpg"
og_image_alt: "Carte de partage : « Même effort, d'autres payeurs » — un même effort de 10 milliards d'euros, en % du revenu de chaque dixième de niveau de vie, selon trois décisions : baisse de l'enseignement, hausse des impôts, baisse des pensions (Insee, 2023)."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "qui_paie_donnees"
  nom: "Qui paie la dette publique : détention, redistribution et exposition à un même effort"
  description: "Compilation dérivée des séries officielles : dette publique par administration (INSEE) et détenteurs des titres négociables de l'État (Banque de France via l'Agence France Trésor) ; prélèvements et transferts publics par dixième de niveau de vie et par âge, comptes nationaux distribués 2023 (Insee) ; exposition des dixièmes à un même effort de {qp.exp_effort} milliards d'euros selon trois décisions — impôts, pensions, enseignement —, profil comptable et non simulation, avec ses tests de robustesse."
  couverture_temporelle: "2020/2026"
  couverture_spatiale: "France"
  variables:
    - {nom: "Prélèvements et transferts publics par dixième de niveau de vie", unite: "euros par unité de consommation"}
    - {nom: "Part des personnes bénéficiaires nettes", unite: "% des personnes"}
    - {nom: "Exposition à un même effort selon la décision", unite: "% du revenu disponible du dixième"}
    - {nom: "Détenteurs des titres négociables de l'État", unite: "% en valeur de marché"}
  sources:
    - "https://www.insee.fr/fr/statistiques/8974371"
    - "https://www.insee.fr/fr/statistiques/8574663"
    - "https://www.aft.gouv.fr/"
  mots: ["dette publique", "redistribution", "comptes nationaux distribués", "Insee", "qui paie la dette", "détenteurs de la dette"]
  fichiers: ["qui_paie_donnees.csv", "qui_paie_donnees.json"]
faq:
  - question: "La dette publique est-elle vraiment un problème ?"
    answer: "L'argument rassurant est sérieux : quand le taux d'intérêt reste inférieur à la croissance, le ratio de dette peut se stabiliser, à condition que le déficit hors intérêts — le solde primaire — reste sous un seuil qui dépend de l'écart entre ces deux taux et du niveau de la dette. Au-delà, le ratio monte malgré tout. Et même stable, une dette doit être servie chaque année : son financement et ses ajustements répartissent des coûts et des avantages entre contribuables, usagers, épargnants et générations. La question utile porte alors sur ce qu'elle finance et sur qui supporte les ajustements — elle se traite configuration par configuration, pas par principe."
  - question: "La dette publique est-elle un fardeau pour les générations futures ?"
    answer: "Pas mécaniquement. Les générations suivantes héritent des engagements, mais aussi de ce qu'ils ont financé — infrastructures, formation, patrimoine public — et d'une partie des titres eux-mêmes, détenus directement ou par l'assurance-vie — ce qui ne neutralise pas nécessairement la charge, la dette pouvant aussi évincer du capital productif. Le transfert net dépend de l'usage : une dette qui finance une consommation courante sans contrepartie durable leur transmet surtout un coût ; un investissement dont elles profiteront peut leur transmettre davantage qu'il ne coûte. Ce qui reste vrai dans tous les cas : la décision est prise sans elles. La page « La dette publique est-elle un fardeau pour les générations futures ? » du même dossier décompose, dans les comptes, les emplois des déficits."
  - question: "Qui détient la dette publique française, et qui en touche les intérêts ?"
    answer: "L'État porte {qp.etat_pct} % de la dette publique ({qp.periode_a}, INSEE). Au {qp.det_periode}, ses titres négociables sont détenus en valeur de marché à {qp.nonres_pct} % par des non-résidents, {qp.bafs_pct} % par des banques, assureurs et fonds résidents, {qp.autres_fr_pct} % par d'autres porteurs résidents, parmi lesquels la Banque de France, dont la part n'est pas publiée (Banque de France, via l'Agence France Trésor). Le classement se fait par résidence, non par nationalité. Pour les ménages, la Direction générale du Trésor estime, en remontant les placements de l'assurance-vie, des fonds et des banques, que sur {qp.tresor_sur} euros de patrimoine financier, {qp.tresor_dette} finance de la dette des administrations publiques, majoritairement françaises. Aucune statistique publiée ne répartit en revanche les intérêts de la dette publique par niveau de vie ou de patrimoine, et une part des titres détenus n'est pas une part des intérêts versés. Détenir n'est pas payer : le porteur a avancé les fonds et en reçoit la rémunération ; la répartition des porteurs ne dit pas qui supporte la charge finale."
  - question: "Faut-il rembourser la dette publique ?"
    answer: "Chaque titre arrivé à échéance est remboursé, mais la dette dans son ensemble se refinance : l'État émet de nouveaux titres pour rembourser les anciens, et le stock évolue avec le déficit. Le remboursement intégral du stock est donc une hypothèse largement théorique. La question opératoire porte sur ce que la dette organise pendant qu'elle roule : qui supporte les intérêts, sur quels budgets portent les ajustements, qui hérite des engagements et de ce qu'ils ont financé. Le refinancement renouvelle une échéance aux conditions du moment : il peut alléger ou alourdir la charge, et ne permet pas à lui seul d'identifier qui la supportera."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-10-11"  # date de la relecture attestée ; absente = page pas encore refondue
  bloc: "dette"
  rang: 20
  nature: "Analyse, appuyée sur des données publiques"
  accueil: 2
---

{{< dossier-dette volet="2" >}}

{{< reutiliser-ancre >}}

Qui paie la dette publique&nbsp;? La réponse change avec la décision prise pour l'ajuster. Un même effort de {{< qp-val "exp_effort" >}}&nbsp;milliards d'euros pèse surtout sur les ménages les plus modestes s'il passe par l'enseignement, surtout sur les plus aisés s'il passe par l'impôt, et presque également sur tous s'il passe par les pensions. Le montant de la facture — encours, charge d'intérêts, coût moyen du stock — est mesuré sur une autre page de ce dossier, [Combien coûte la dette publique&nbsp;?](/cout-de-la-dette-publique/)&nbsp;; celle-ci demande sur qui elle retombe, ce que les données permettent, ou non, d'attribuer, et ce qu'une décision réelle, envisagée pour {{< qp-val "pens_annee" >}} puis écartée, en montre.

{{< dette-chiffres >}}

## Selon la décision, l'effort ne tombe pas sur les mêmes ménages

La population est rangée du plus modeste au plus aisé, puis coupée en dix groupes de même taille, les **dixièmes de niveau de vie**. L'exercice prend {{< qp-val "exp_effort" >}}&nbsp;milliards d'euros et les répartit trois fois — par une hausse des impôts sur les revenus et le patrimoine, par une baisse des pensions de retraite, par une baisse des dépenses d'enseignement —, toujours au prorata de ce que chaque dixième verse ou reçoit déjà, puis rapporte le résultat à son revenu. L'impôt retenu est la catégorie des comptes distribués «&nbsp;impôts sur les revenus et le patrimoine&nbsp;»&nbsp;: CSG, impôt sur le revenu et autres impôts de cette catégorie, comme la CRDS, la taxe d'habitation ou l'impôt sur la fortune immobilière. Ce n'est ni une prévision ni une mesure envisagée&nbsp;: aucun comportement, aucun effet en retour n'y entre. C'est la structure actuelle des postes, rendue comparable d'une décision à l'autre.

{{< figure-svg fichier="qui-paie-exposition" alt="Deux panneaux. En haut, trois courbes par dixième de niveau de vie : la baisse des dépenses d'enseignement part très haut sur le premier dixième et décroît fortement ; la hausse des impôts fait l'inverse et monte sur le dernier dixième ; les pensions restent presque plates. En bas, des barres montrant le rapport entre la décision la plus lourde et la plus légère pour chaque dixième : élevé aux deux extrémités, minimal en D7-D8." >}}Insee, comptes nationaux distribués, tableau CND.101 (vingtièmes de niveau de vie, 2020-2023, base 2020)&nbsp;; millésime 2023. Profil d'exposition comptable, non une simulation.{{< /figure-svg >}}

{{< fig-actions id="exposition" >}}

**Le classement s'inverse d'une décision à l'autre.** Une réduction des dépenses d'enseignement représenterait {{< qp-val "exp_ens_d1" >}}&nbsp;% du revenu des 10&nbsp;% les plus modestes et {{< qp-val "exp_ens_d10" >}}&nbsp;% de celui des plus aisés&nbsp;; une hausse des impôts sur les revenus et le patrimoine ferait l'inverse, jusqu'à {{< qp-val "exp_fisc_d10" >}}&nbsp;% pour le dernier dixième. Le contraste ne vient pas seulement de ce que les petits revenus sont plus petits&nbsp;: en euros, la moitié la moins aisée supporterait {{< qp-val "exp_masse_ens" >}}&nbsp;% de la coupe d'enseignement contre {{< qp-val "exp_masse_fisc" >}}&nbsp;% de l'effort fiscal. Une baisse des pensions se tiendrait dans une bande étroite, de {{< qp-val "exp_pens_min" >}} à {{< qp-val "exp_pens_max" >}}&nbsp;%, sans épargner aucun groupe en particulier. Et «&nbsp;l'impôt&nbsp;» n'a pas un seul profil&nbsp;: une hausse des taxes sur les produits, comme la TVA, répartie de même, pèserait elle aussi davantage sur les plus modestes en part de leur revenu, {{< qp-val "exp_tva_d1" >}}&nbsp;% contre {{< qp-val "exp_tva_d10" >}}&nbsp;% pour les plus aisés. Le profil favorable aux plus modestes est donc celui des impôts sur les revenus et le patrimoine, non de toute la fiscalité&nbsp;; et ce calcul suit la même convention proportionnelle, sans être l'incidence finale d'une hausse réelle de TVA.

**Une exposition comptable, non une perte observée.** Les {{< qp-val "exp_ens_d1" >}}&nbsp;% du premier dixième sont la valeur des services d'enseignement que les comptes de l'Insee lui attribuent par convention, rapportée à son revenu&nbsp;: ni une perte de revenu effectivement subie, ni une mesure de bien-être. Une hausse d'impôt retire de l'argent&nbsp;; une baisse de dépense retire un service, dont la valeur est imputée et dont le coût réel pour chacun dépend de ce qui est supprimé.

<div class="resultat-phrase">

**Le résultat en une phrase.** «&nbsp;Qui paie la dette&nbsp;?&nbsp;» n'a pas de réponse en soi, il en a une par décision&nbsp;: un même effort pèse surtout sur les plus modestes s'il passe par l'enseignement, surtout sur les plus aisés s'il passe par l'impôt.

</div>

**Au milieu de l'échelle, le choix du levier compte le moins.** Pour le {{< qp-val "exp_creux_zone_mots" >}}&nbsp;dixième, un peu au-dessus du milieu, l'effort moyen changerait peu d'une décision à l'autre&nbsp;: la plus lourde y coûterait {{< qp-val "exp_ecart_creux" >}}&nbsp;fois la plus légère. Pour les 10&nbsp;% les plus aisés, elle coûterait {{< qp-val "exp_ecart_d10" >}}&nbsp;fois la plus légère, et au moins autant pour les 10&nbsp;% les plus modestes&nbsp;: aux deux bouts de l'échelle, le choix du levier décide presque tout. Ces dixièmes ne supporteraient pas moins d'effort&nbsp;; simplement, changer de levier y modifierait moins leur exposition moyenne, qui ne dit pas la situation de chacun des ménages qui les composent. La convergence se retrouve dans les quatre millésimes {{< qp-val "exp_millesimes" >}} — qui partagent conventions et structures, et ne sont donc pas des réplications indépendantes —, et elle ne vaut que pour ces trois leviers ainsi répartis.

<details class="repli"><summary>Trois épreuves du creux en {{< qp-val "exp_creux_zone" >}}, et les limites de l'exercice</summary>

**En vingtièmes.** Découpée en vingt groupes au lieu de dix, la population place encore le minimum dans la zone de {{< qp-val "exp_creux_zone" >}}&nbsp;: au {{< qp-val "exp_t1_rangs" >}} vingtième selon l'année. Le creux ne vient donc pas du regroupement par dixièmes.

**Par paires de leviers.** La courbe de l'impôt monte avec le niveau de vie, celle de l'enseignement descend&nbsp;: prises deux à deux, elles se rapprochent le plus en {{< qp-val "exp_t3_croise" >}}, et c'est leur croisement qui fait le creux, la courbe des pensions, presque plate, passant tout près des deux. Le coefficient de variation et l'étendue rapportée à la moyenne placent le minimum dans la même zone que le rapport du plus lourd au plus léger.

**Mesuré en points de revenu** plutôt qu'en rapport, l'écart entre la décision la plus lourde et la plus légère est encore le plus faible en {{< qp-val "exp_creux_zone" >}}. **Sans les pensions**, impôt et enseignement seuls se rapprochent le plus en {{< qp-val "exp_t3_croise" >}}&nbsp;: le creux ne doit rien à la troisième courbe. **Avec un quatrième levier**, les taxes sur les produits, il reste en {{< qp-val "exp_creux_zone" >}}.

**Avec d'autres formes de mesures — hypothèses de calcul, non mesures envisagées.** Une baisse d'enseignement du même montant pour chaque dixième, ou concentrée là où la dépense est déjà forte, laisse le creux en {{< qp-val "exp_creux_zone" >}}&nbsp;; épargner l'enseignement des trois premiers dixièmes le place en {{< qp-val "exp_ens_epargne" >}} selon l'année&nbsp;; épargner leurs pensions le laisse en {{< qp-val "exp_creux_zone" >}}. Un impôt plus progressif, réparti au prorata du carré de ce que chaque dixième paie déjà, le déplace en revanche en {{< qp-val "exp_t2_progressif" >}}. Le creux résiste donc à la mesure et à plusieurs répartitions, mais sa place suit la progressivité des mesures&nbsp;: c'est un résultat du scénario proportionnel, non une propriété générale de la redistribution.

**Le revenu de référence ne joue que sur le niveau des courbes.** Pour un même dixième, il est commun aux trois leviers&nbsp;: le rapport du plus lourd au plus léger, et les points où deux courbes se croisent, ne dépendent pas de lui. L'écart mesuré en points de revenu, lui, en dépend&nbsp;: avec un autre dénominateur, son minimum pourrait se déplacer.

**Les limites.** Un service public valorisé n'est pas un revenu&nbsp;: une dépense d'enseignement imputée à un ménage ne lui est pas versée, et sa réduction ne lui coûterait pas exactement cette somme. Les trois décisions sont proportionnelles par construction&nbsp;; la figure ne dit rien de «&nbsp;l'impôt&nbsp;» ni de «&nbsp;la dépense publique&nbsp;» en général. Enfin, le point du premier dixième est écarté pour la décision fiscale&nbsp;: l'impôt sur le revenu du premier vingtième y pèse {{< qp-val "exp_part_ir_v1" >}}&nbsp;% du poste quand les vingtièmes voisins sont à zéro, une cellule atypique de la source. L'écart de ce dixième, calculé sur les deux autres leviers, est donc une borne inférieure.

</details>

<span id="quatre-rôles-à-ne-pas-confondre"></span>
<span id="ce-que-les-données-permettent-de-voir"></span>
<span id="les-créanciers--financer-nest-pas-gagner"></span>

## Qui emprunte, qui détient, qui reçoit les intérêts {#creanciers}

Quatre questions se confondent souvent&nbsp;: qui emprunte, qui finance et reçoit les intérêts, par quels mécanismes le financement et les ajustements opèrent, et qui en supporte finalement les effets. Ce ne sont pas quatre populations&nbsp;: une même personne paie l'impôt, se soigne à l'hôpital public et détient des titres de l'État par son assurance-vie. Et «&nbsp;qui paie&nbsp;» se dit toujours par rapport à une autre décision&nbsp;: moins emprunter aurait signifié un autre impôt, une autre dépense, avec leurs propres perdants.

{{< figure-svg fichier="qui-paie-detention" alt="Deux panneaux de barres horizontales, séparés. En haut, la dette publique par administration emprunteuse, en valeur nominale : l'État très largement en tête. En bas, les porteurs des titres négociables de l'État, en valeur de marché : les non-résidents en tête." >}}Deux champs distincts&nbsp;: A en valeur nominale (INSEE), B en valeur de marché (Banque de France, via l'Agence France Trésor). Les valeurs viennent du même registre que la figure de la p.&nbsp;101 du livre.{{< /figure-svg >}}

{{< fig-actions id="detention" >}}

**Qui emprunte, qui détient.** L'État porte l'essentiel de la dette publique&nbsp;: {{< qp-val "etat_mdeur" >}}&nbsp;milliards d'euros sur {{< qp-val "total_mdeur" >}}, soit {{< qp-val "etat_pct" >}}&nbsp;%, {{< qp-val "periode_a" >}}. Au {{< qp-val "det_periode" >}}, ses titres négociables sont détenus à {{< qp-val "nonres_pct" >}}&nbsp;% par des non-résidents&nbsp;; banques, assureurs et fonds résidents en portent ensemble {{< qp-val "bafs_pct" >}}&nbsp;%&nbsp;; les autres porteurs résidents, {{< qp-val "autres_fr_pct" >}}&nbsp;%, comprennent la Banque de France, dont la source ne publie pas la part. Les deux panneaux ne se combinent pas&nbsp;: l'un est en valeur nominale, l'autre en valeur de marché.

**Qui reçoit les intérêts&nbsp;: ce qu'on observe, ce qu'on approche, ce qu'on ignore.** On *observe* les porteurs directs, classés par résidence&nbsp;: c'est un stock photographié à une date, non le flux des coupons, qui dépend des titres détenus et de leur date d'émission. On *approche* les porteurs indirects&nbsp;: en remontant les placements de l'assurance-vie, des fonds et des banques jusqu'à leur usage final, la Direction générale du Trésor estime que sur {{< qp-val "tresor_sur" >}}&nbsp;euros de patrimoine financier des ménages français, {{< qp-val "tresor_dette" >}} finance de la dette des administrations publiques, majoritairement françaises ([*Trésor-Éco* n°&nbsp;{{< qp-val "tresor_numero" >}}, janvier 2026](https://www.tresor.economie.gouv.fr/Articles/2026/01/08/que-finance-l-epargne-financiere-des-menages-francais)). On *ignore* qui, parmi les ménages, reçoit ces intérêts&nbsp;: aucune statistique publiée ne les répartit par niveau de vie ou de patrimoine, ce qui demanderait de suivre chaque titre, sa rémunération et ses intermédiaires. Deux lectures sont donc exclues&nbsp;: {{< qp-val "nonres_pct" >}}&nbsp;% des titres ne font pas {{< qp-val "nonres_pct" >}}&nbsp;% des intérêts, et la détention d'actifs financiers par dixième ne dit pas la part de chacun dans ces intérêts. L'absence de cette ventilation ne signifie pas que ces revenus sont négligeables&nbsp;: elle borne ce qu'on peut affirmer. Deux précisions encore&nbsp;: le porteur d'aujourd'hui n'est pas forcément celui qui a prêté à l'émission, un titre s'échangeant ensuite sur le marché&nbsp;; et les titres détenus par la Banque de France au titre des programmes de l'Eurosystème ne s'analysent pas comme ceux d'un créancier privé.

<details class="repli"><summary>Résidence n'est pas nationalité, et financer n'est pas gagner</summary>

**Financer n'est pas gagner.** Le créancier a avancé les fonds&nbsp;: les intérêts rémunèrent cette avance, le temps et le risque. Son rendement réel tient compte de l'inflation et de la variation de valeur du titre, et son avantage sur un autre placement se mesure à horizon et risque comparables. «&nbsp;On se la doit à nous-mêmes&nbsp;» n'est donc vrai qu'en partie, et ne dit pas lesquels d'entre «&nbsp;nous&nbsp;» reçoivent et lesquels financent.

La répartition publiée classe les porteurs par **résidence**, non par nationalité&nbsp;: un «&nbsp;non-résident&nbsp;» peut être un fonds étranger qui gère l'épargne de ménages français, et un ménage français peut détenir des titres de l'État sans le savoir, par son assurance-vie. La statistique de la Banque de France sur les titres de long terme de l'ensemble des administrations publiques porte sur un autre champ que celle de l'Agence France Trésor, limitée aux titres négociables de l'État&nbsp;: les deux parts ne se substituent pas l'une à l'autre.

</details>

## Qui contribue, qui reçoit aujourd'hui {#redistribution}

Les comptes nationaux distribués de l'Insee répartissent, pour {{< qp-val "cd_annee" >}}, prélèvements et transferts publics entre les **dixièmes de niveau de vie** — la population rangée du plus modeste au plus aisé, puis coupée en dix parts d'effectif égal. Les montants y sont exprimés **par unité de consommation** (UC), l'unité qui rend comparables des ménages de tailles différentes&nbsp;: une personne seule compte 1&nbsp;UC, un couple avec deux enfants de moins de 14&nbsp;ans, 2,1.

{{< figure-svg fichier="qui-paie-redistribution" alt="Barres par dixième de niveau de vie, en 2023. Au-dessus de zéro, les transferts reçus, d'un niveau voisin d'un dixième à l'autre ; sous zéro, les prélèvements, qui croissent fortement du premier au dernier dixième." >}}Insee, comptes nationaux distribués 2023 (*Insee Analyses* n°&nbsp;118, 16&nbsp;avril 2026, figure&nbsp;1c), en euros par unité de consommation.{{< /figure-svg >}}

{{< fig-actions id="redistribution" >}}
{{< qp-tableau-redistribution >}}

Les prélèvements vont de {{< qp-val "d1_prel" >}}&nbsp;€ par UC pour les 10&nbsp;% les plus modestes à {{< qp-val "d10_prel" >}}&nbsp;€ pour les 10&nbsp;% les plus aisés, environ {{< qp-val "ratio_prel" >}}&nbsp;fois plus. Les transferts reçus — prestations en espèces et services publics valorisés en euros — varient beaucoup moins&nbsp;: ils restent compris entre {{< qp-val "recu_min" >}} et {{< qp-val "recu_max" >}}&nbsp;€, sans progression régulière. Ce qui est versé suit le niveau de vie&nbsp;; ce qui est reçu, beaucoup moins. Ces prélèvements ne sont pas des paiements relevés un à un&nbsp;: outre l'impôt sur le revenu et les cotisations, ils comprennent les taxes sur les produits, comme la TVA, et des impôts sur la production, que l'Insee attribue aux ménages par convention.

<div class="resultat-phrase">

**Où la dette entre dans ces comptes.** En {{< qp-val "cd_annee" >}}, les transferts attribués aux ménages dépassent les prélèvements de {{< qp-val "solde_mdeur" >}}&nbsp;milliards d'euros, et l'Insee rattache cet écart à l'endettement public&nbsp;: c'est la part du revenu élargi de l'année qui n'est pas financée par des prélèvements de la même année. Ces {{< qp-val "solde_mdeur" >}}&nbsp;milliards ne sont pas la charge d'intérêts de {{< dette-val "interets_annee" >}} ({{< dette-val "interets_mdeur" >}}&nbsp;milliards)&nbsp;: année, champ et nature diffèrent, et la proximité des deux nombres est une coïncidence.

</div>

<details class="repli"><summary>Un solde réparti par convention, financé à crédit, qui ne dit pas qui paiera demain</summary>

Ce total porte sur le champ des comptes distribués, qui n'est pas celui du déficit public&nbsp;: les deux montants ne se substituent pas l'un à l'autre. Dans cette construction, l'écart élève le niveau de vie élargi des ménages de l'année — un bénéfice présent, financé à crédit —, mais ce ne sont pas {{< qp-val "solde_mdeur" >}}&nbsp;milliards de versements identifiables&nbsp;: c'est un solde réparti par convention, que l'Insee impute pour moitié à de moindres prélèvements et pour moitié à des transferts supplémentaires quand il calcule un niveau de vie «&nbsp;net de l'endettement&nbsp;». Les figures de cette page présentent les transferts courants, avant ce retraitement. Le solde n'implique pas que les bénéficiaires de la redistribution aient «&nbsp;créé&nbsp;» cette dette, ni que leur position dise qui la remboursera.

</details>

{{< figure-svg fichier="qui-paie-solde-net" alt="Deux panneaux. En haut, le solde des transferts publics par dixième de niveau de vie, défini comme ce que le groupe verse moins ce qu'il reçoit : négatif, donc bénéficiaire net, pour les premiers dixièmes, positif, donc contributeur net, pour les derniers, très fortement pour le dernier. En bas, la part de personnes bénéficiaires nettes, décroissante du premier au dernier dixième." >}}Insee, comptes nationaux distribués 2023 (figure&nbsp;2a). Deux unités, deux panneaux&nbsp;: euros par unité de consommation, puis part de personnes.{{< /figure-svg >}}

{{< fig-actions id="solde-net" >}}

**Qui verse net, qui reçoit net.** En moyenne par UC, les transferts reçus dépassent les prélèvements dans chacun des {{< qp-val "net_benef_n_mots" >}} premiers dixièmes — de {{< qp-val "net_d1" >}}&nbsp;€ par UC dans le premier —, et le solde bascule au dixième {{< qp-val "net_bascule" >}}&nbsp;: dans les {{< qp-val "net_contrib_n_mots" >}} derniers, c'est l'inverse, et le dernier dixième verse en moyenne {{< qp-val "net_d10" >}}&nbsp;€ par UC de plus qu'il ne reçoit.

<div class="resultat-phrase">

**Une moyenne de groupe ne décrit pas ses membres.** {{< qp-val "benef_ensemble" >}}&nbsp;% des personnes sont bénéficiaires nettes cette année-là, {{< qp-val "benef_d1" >}}&nbsp;% dans le premier dixième et {{< qp-val "benef_d10" >}}&nbsp;% dans le dernier. Mais elles ne sont majoritaires que dans les {{< qp-val "benef_majo_n_mots" >}} premiers dixièmes&nbsp;: dans le dixième {{< qp-val "benef_dernier_moyen" >}}, qui reçoit en moyenne {{< qp-val "net_dernier_moyen" >}}&nbsp;€ par UC de plus qu'il ne verse, elles ne sont plus que {{< qp-val "benef_dernier_moyen_pct" >}}&nbsp;%. **Le signe d'une moyenne ne dit pas la situation de la majorité.** Un groupe peut recevoir plus qu'il ne verse en moyenne alors que la majorité de ses membres versent plus qu'ils ne reçoivent&nbsp;: il suffit que ce que reçoivent en moyenne les bénéficiaires nets l'emporte sur ce que versent en moyenne les autres. Les données regroupées ne disent pas comment ces soldes se répartissent.

</div>

Recevoir plus que l'on ne verse, en moyenne, ne protège donc pas d'un ajustement&nbsp;: la position dans la redistribution d'aujourd'hui et l'exposition à une décision de demain sont deux classements distincts.

<details class="repli"><summary>Conventions&nbsp;: le solde d'une année, non d'une vie&nbsp;; des services publics imputés, non mesurés&nbsp;; toute la redistribution, pas l'effet propre de la dette</summary>

C'est le solde d'une **année**, non d'une vie&nbsp;: les pensions de retraite y sont comptées comme prestations courantes. Les transferts comprennent des services publics — soins, éducation, services collectifs — valorisés en euros et répartis par imputation statistique, non un relevé des services utilisés par chacun&nbsp;; la part de bénéficiaires nets en dépend à la marge. Le revenu «&nbsp;avant transferts&nbsp;» est une étape de calcul, non le revenu qu'aurait chacun dans une économie sans impôts ni services publics. Et ce solde décrit la redistribution dans son ensemble, pas l'effet propre de la dette.

</details>

<details class="repli"><summary>Par âge du ménage&nbsp;: une photographie de l'année, non un bilan de vie</summary>

{{< figure-svg fichier="qui-paie-age" alt="Barres par groupe d'âge du ménage, en 2023 : les transferts reçus augmentent avec l'âge, modérément jusqu'à 64 ans puis très fortement pour les ménages de 65 ans ou plus ; les prélèvements versés croissent jusqu'aux 50-64 ans, puis chutent pour ce dernier groupe." >}}Insee, comptes nationaux distribués 2023 (figure&nbsp;1e). Groupes d'âge moyen des adultes du ménage.{{< /figure-svg >}}

{{< fig-actions id="age" >}}

En {{< qp-val "cd_annee" >}}, selon ces conventions, les ménages dont l'âge moyen des adultes atteint 65&nbsp;ans ou plus reçoivent {{< qp-val "age_recu_65" >}}&nbsp;€ de transferts par unité de consommation — dont {{< qp-val "age_esp_65" >}}&nbsp;€ de prestations en espèces, pensions comprises — et versent {{< qp-val "age_prel_65" >}}&nbsp;€ de prélèvements, contre {{< qp-val "age_prel_5064" >}}&nbsp;€ pour les ménages de 50 à 64&nbsp;ans. Les pensions correspondent pour une part à des droits acquis au cours de la carrière, ici comptés comme prestations courantes&nbsp;; l'âge du ménage n'est pas le statut de retraite de chacun de ses membres, et un montant élevé de soins imputés traduit aussi des besoins plus élevés. Cette photographie ne désigne aucun payeur de demain.

</details>

## Par quels canaux la charge peut se répartir

Quatre mécanismes peuvent modifier la charge de la dette et sa répartition, et ils se combinent. Les deux premiers relèvent de l'**ajustement budgétaire ordinaire**, décidé chaque année&nbsp;: les **prélèvements** — impôts et cotisations supplémentaires, ou baisses d'impôt auxquelles on renonce — et les **dépenses et prestations** réduites, gelées ou reportées. Le troisième ne se décide pas seul&nbsp;: l'**inflation non anticipée** réduit la valeur réelle des créances déjà émises et reporte une partie de la charge sur leurs détenteurs et sur les revenus mal indexés. Le quatrième est un cas extrême&nbsp;: la **restructuration** impose une perte de premier rang aux porteurs des titres, qui peuvent la répercuter sur leurs actionnaires, assurés ou épargnants.

{{< figure-svg fichier="qui-paie-mecanismes" alt="Schéma sans quantités : la charge de la dette et sa répartition mènent, par des flèches d'égale épaisseur, à quatre mécanismes regroupés en trois familles — l'ajustement budgétaire ordinaire (prélèvements, dépenses et prestations), l'inflation non anticipée, effet de prix qui ne se décide pas seul, et la restructuration, cas extrême ; le refinancement renouvelle l'échéance aux taux du moment ; en regard, ce que la dette a financé." >}}Schéma de mécanismes possibles&nbsp;: aucun poids relatif ni effet causal n'y est mesuré.{{< /figure-svg >}}

{{< fig-actions id="mecanismes" >}}

Le refinancement, lui, renouvelle une échéance aux conditions du moment&nbsp;: il peut alléger ou alourdir la charge, sans désigner qui la supportera. Et en face de ces coûts se trouve ce que la dette a financé&nbsp;: services, prestations et investissements profitent à des ménages aujourd'hui et demain, et une analyse qui ne compterait que les coûts ne décrirait que la moitié du bilan.

<details class="repli"><summary>Pourquoi seule l'inflation non anticipée transfère la charge, et ce qui joue en sens inverse</summary>

L'inflation attendue au moment où le taux d'un titre a été fixé tend à être déjà incorporée au taux exigé à l'émission, et n'opère alors aucun transfert. C'est l'écart entre l'inflation réalisée et celle-là qui réduit la valeur réelle des créances nominales déjà émises. Deux mécanismes jouent en sens inverse&nbsp;: les titres indexés voient leur charge monter avec les prix, et le refinancement se fait aux taux nouveaux. L'effet net dépend donc de la part indexée, du calendrier de refinancement et de ce qui était anticipé — et la France ne choisit pas seule son inflation. À ne pas confondre avec l'effet de l'inflation sur le *ratio* de dette, qui passe par le PIB nominal et ne désigne, lui, aucun perdant. La liste des canaux n'est pas exhaustive&nbsp;: la croissance, les cessions d'actifs et les conditions de financement interviennent aussi, et l'histoire connaît la répression financière, qui contraint les rendements.

</details>

## Trois hypothèses à tester {#hypotheses}

Les canaux disent par où la charge peut passer&nbsp;; trois hypothèses plus fortes circulent quant à ceux qu'elle atteindrait. Aucune n'est établie par les données de cette page, et chacune demande sa propre épreuve.

### Les générations futures — ce dont elles héritent

La dette convertit une dépense présente en engagements futurs&nbsp;: ceux qui viendront après en héritent sans avoir pris part à la décision. Mais ils héritent aussi de ce qu'elle a financé et d'une partie des titres eux-mêmes&nbsp;: le transfert net n'est pas mesuré ici.

<details class="repli"><summary>Ce dont dépend le transfert net, et ce que la dette nette ne dit pas</summary>

Les générations suivantes héritent des infrastructures, de la formation et du patrimoine public financés, et de titres que leurs parents détiennent directement ou par l'assurance-vie. Cela ne neutralise pas nécessairement la charge&nbsp;: certains modèles identifient un canal d'éviction du capital productif, que cette page ne mesure pas en France. Le transfert net dépend de l'usage, du financement, des créances transmises et de l'alternative retenue. La dette nette publiée par l'INSEE ne tranche pas non plus&nbsp;: elle ne déduit que certains actifs financiers, pas les routes, le capital humain ni l'environnement. La page [La dette publique est-elle un fardeau pour les générations futures&nbsp;?](/dette-publique-generations-futures/) décompose, dans les comptes, les emplois des déficits, sans dire quel euro emprunté a payé quelle dépense.

</details>

### Les groupes moins mobiles — une hypothèse à tester

Les ménages et les entreprises qui peuvent déplacer leurs revenus, leur patrimoine ou leur activité échappent plus facilement à un prélèvement que les salariés, les retraités ou les usagers d'un service public local. D'où l'hypothèse&nbsp;: quand l'ajustement suit la ligne de moindre résistance, il **peut** peser davantage sur ceux qui ne peuvent pas partir.

<details class="repli"><summary>Pour l'éprouver&nbsp;: des groupes définis d'avance, un ajustement précis, une mesure fixée</summary>

Pour l'éprouver, il faut définir ces groupes avant d'observer l'ajustement, préciser l'ajustement étudié et fixer une mesure de l'effort&nbsp;; l'hypothèse serait affaiblie par un ajustement portant surtout sur d'autres groupes, ou par des compensations accordées aux perdants. Mobilité géographique, mobilité de la base imposable et capacité à remplacer un service public sont trois propriétés distinctes. Le canal territorial est examiné sur la page [Dette publique&nbsp;: pourquoi les collectivités locales sont-elles la variable d'ajustement&nbsp;?](/dette-publique-collectivites-locales/)

</details>

### Les investissements à bénéfices différés — un mécanisme à établir cas par cas

Un budget contraint par le service de la dette **peut inciter à reporter** les dépenses dont les bénéfices sont lointains et le report peu coûteux politiquement&nbsp;: recherche, entretien du patrimoine, formation, transition écologique. Le mécanisme est plausible, non établi.

<details class="repli"><summary>Plausible, non établi&nbsp;: aucun agrégat ne mesure un investissement empêché par les intérêts</summary>

Il reste à l'établir décision par décision — quelle dépense, reportée par quelle décision, pour quel motif budgétaire —, car aucun agrégat ne mesure un investissement empêché par les intérêts. Là où il est établi, il alourdit le transfert&nbsp;: aux engagements transmis s'ajoute le bénéfice qui n'a pas été construit, et celui-là n'apparaît dans aucun encours.

</details>

<span id="les-objections-qui-comptent"></span>

## Une décision réelle, datée {#decision-reelle}

<aside class="encadre">

**Exemple réel, distinct de l'exercice théorique.** Le projet de loi de financement de la sécurité sociale pour 2026 prévoyait, à son [article&nbsp;44](https://www.assemblee-nationale.fr/dyn/17/textes/l17b1907_projet-loi.pdf), de ne pas revaloriser en {{< qp-val "pens_annee" >}} les pensions de retraite des régimes de base — un coefficient «&nbsp;égal à un&nbsp;». La disposition a été écartée au cours de l'examen parlementaire&nbsp;: la [loi de financement de la sécurité sociale pour 2026](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053226384), promulguée le 30&nbsp;décembre 2025, ne comporte pas de gel, et l'[instruction interministérielle du 15&nbsp;décembre 2025](https://legislation.lassuranceretraite.fr/Pdf/instruction_ministerielle_2025_174_15122025.pdf) revalorise ces pensions au 1er&nbsp;janvier {{< qp-val "pens_annee" >}} d'un coefficient de {{< qp-val "pens_coef" >}}, soit {{< qp-val "pens_taux" >}}&nbsp;%, «&nbsp;conformément au droit en vigueur&nbsp;».

C'est une décision du type «&nbsp;pensions&nbsp;», envisagée puis écartée. Deux limites empêchent de lui appliquer directement l'exercice&nbsp;: un gel des seules pensions de base n'a pas le profil d'une baisse répartie au prorata de toutes les pensions, et rien dans ces textes ne rattache la mesure envisagée à la dette plutôt qu'au déficit de la sécurité sociale. Un budget réel combine recettes, cotisations, prestations, dépenses et emprunt, et ne permet généralement pas de rattacher un impôt donné à un euro d'intérêts. Mesure non adoptée, elle ne permet pas non plus de mesurer une incidence effectivement subie&nbsp;: il faudrait pour cela une mesure appliquée, et la situation qui aurait prévalu sans elle. Les trois décisions de {{< qp-val "exp_effort" >}}&nbsp;milliards de cette page sont des hypothèses de calcul, non une description des choix de {{< qp-val "pens_annee" >}}. La politique budgétaire d'ensemble est examinée dans le volet [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)

</aside>

## Ce que ces données ne permettent pas d'établir

Aucune statistique ne dit, à elle seule, qui supporte au bout du compte la charge de la dette française&nbsp;: l'incidence finale d'un euro d'intérêts dépend des ajustements choisis année après année, et de l'alternative à laquelle on les compare. Une répartition actuelle des impôts et des prestations décrit qui contribue et qui reçoit aujourd'hui&nbsp;; elle n'identifie pas les payeurs futurs. Une moyenne par unité de consommation n'est pas une facture individuelle. Ce qui peut s'établir, c'est l'effet d'une décision déterminée — une réforme, un gel, un report — sur des groupes définis d'avance&nbsp;: c'est à ce niveau que «&nbsp;qui paie&nbsp;?&nbsp;» reçoit des réponses vérifiables.

{{< confrontation-recherche verifie="2026-09-30" publie="oui" resume="le sens du contraste dépense / impôt est retrouvé sur des consolidations réelles&nbsp;; l'argument de la créance héritée est mis en danger par l'éviction du capital" >}}
**Mesuré ici.** Un profil comptable&nbsp;: un même effort de {{< qp-val "exp_effort" >}}&nbsp;milliards d'euros réparti au prorata de ce que chaque dixième verse ou reçoit déjà, d'après l'Insee, sans comportement ni effet en retour. La littérature éprouve les lectures qu'on en tire, pas ce profil.

**Cohérent avec.** Le sens du contraste entre dépense et impôt&nbsp;: sur des consolidations effectivement observées dans 18&nbsp;pays industrialisés, dont la France, de 1978 à 2009, les inégalités de revenu net augmentent&nbsp;; les coupes de dépenses y paraissent défavorables, les hausses d'impôt égalisatrices, sans que ce dernier effet soit significatif dans la spécification de base (Agnello et Sousa). Le report des investissements&nbsp;: dans l'échantillon de Breunig et Busemeyer, une charge d'intérêts plus lourde va de pair avec un recul de la part de l'investissement public au profit des retraites, reporter un investissement coûtant moins, politiquement, que réduire un droit. Le rôle de l'usage&nbsp;: dans le modèle de Diamond, emprunter pour acquérir du capital physique fait de l'État un simple intermédiaire entre épargnants et entrepreneurs, sans effet.

**Mis en danger par.** Toute lecture selon laquelle la créance héritée neutraliserait la charge&nbsp;: dans le cas efficace du modèle de Diamond, où le taux d'intérêt dépasse la croissance de la population, la dette détenue dans le pays abaisse **davantage** le bien-être de long terme que la dette extérieure, parce qu'elle prend la place du capital productif dans les patrimoines. Barro, qui défend l'idée inverse, la fonde sur des transferts volontaires entre parents et enfants, opérants pour la plupart des gens, et reconnaît qu'en 1989 la majorité des économistes penche encore vers les modèles standard. L'ampleur&nbsp;: dans le découpage d'Agnello et Sousa, ce sont les hausses d'impôt les plus fortes qui s'associent à une baisse significative des inégalités, et les effets tendent à disparaître en deux ans. La courbe «&nbsp;impôt&nbsp;» lue comme incidence finale&nbsp;: dans 55&nbsp;082 entreprises de neuf pays européens, de 1996 à 2003, environ la moitié d'une hausse de l'impôt sur les sociétés retombe à long terme sur les salaires (Arulampalam, Devereux et Maffini) — un autre impôt que celui de la page, mais le même écart entre incidence légale et incidence finale.

**Non établi.** Que les groupes moins mobiles supportent davantage l'ajustement&nbsp;: l'étude sur l'impôt sur les sociétés mesure une négociation salariale, et son seul contraste de mobilité, entre multinationales et entreprises indépendantes, n'est pas significatif. Que seule l'inflation non anticipée transfère la charge&nbsp;: nous n'avons pas trouvé, dans les textes examinés, de test séparant inflation anticipée et non anticipée. L'exposition «&nbsp;enseignement&nbsp;» de la page, enfin, n'a pas d'équivalent observé&nbsp;: un indicateur de revenu monétaire ne valorise pas directement une perte de service public.

**Références lues**

- Agnello, L. et Sousa, R. M., «&nbsp;How Does Fiscal Consolidation Impact on Income Inequality?&nbsp;», document de travail de la Banque de France n°&nbsp;382, 2012 (publié dans la *Review of Income and Wealth*, 60(4), 2014).
- Breunig, C. et Busemeyer, M. R. (2012), «&nbsp;Fiscal austerity and the trade-off between public investment and social spending&nbsp;», *Journal of European Public Policy*, 19(6), p.&nbsp;921-938.
- Arulampalam, W., Devereux, M. P. et Maffini, G., «&nbsp;The Direct Incidence of Corporate Income Tax on Wages&nbsp;», manuscrit révisé en février 2012 (publié dans l'*European Economic Review*, 56(6), 2012).
- Diamond, P. A. (1965), «&nbsp;National Debt in a Neoclassical Growth Model&nbsp;», *American Economic Review*, 55(5), p.&nbsp;1126-1150.
- Barro, R. J. (1989), «&nbsp;The Ricardian Approach to Budget Deficits&nbsp;», *Journal of Economic Perspectives*, 3(2), p.&nbsp;37-54.
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir

**«&nbsp;Qui paie&nbsp;?&nbsp;» a une réponse par décision, et le choix pèse surtout aux extrémités.** Un même effort retombe sur les plus modestes par l'enseignement, sur les plus aisés par l'impôt&nbsp;; au milieu de l'échelle, les trois leviers étudiés produisent des expositions proches. Nommer la décision et l'alternative transforme une opinion en énoncé vérifiable.

**Détenir n'est pas payer, et les intérêts ne se suivent que jusqu'à un point.** On observe les porteurs directs, on approche les porteurs indirects par l'épargne des ménages, mais aucune statistique ne dit quels ménages reçoivent les intérêts&nbsp;: la répartition des porteurs renseigne sur la destination des intérêts, jamais sur qui les finance.

**Une moyenne de groupe ne décrit pas ses membres.** Un dixième peut recevoir plus qu'il ne verse *en moyenne* alors que la majorité de ses membres versent plus qu'ils ne reçoivent. Une statistique de dixièmes répond à «&nbsp;comment se répartit la masse&nbsp;?&nbsp;», pas à «&nbsp;que vit une personne de ce dixième&nbsp;?&nbsp;».

</div>

<div class="prolongements" role="group" aria-label="Prolongements du dossier">
<p class="prolongements__titre">Prolongements du dossier&nbsp;: deux applications de «&nbsp;qui paie&nbsp;?&nbsp;»</p>
<a class="prolongements__carte" href="/dette-publique-collectivites-locales/"><b>Collectivités locales</b><span>Comment une contrainte de l'État peut descendre vers des collectivités peu endettées mais très encadrées.</span></a>
<a class="prolongements__carte" href="/dette-publique-generations-futures/"><b>Générations futures</b><span>Quand la dette constitue-t-elle réellement un transfert vers ceux qui viennent après&nbsp;?</span></a>
</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}



{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Cette analyse est développée dans le livre" avis="non" >}}
Cette page pose la méthode&nbsp;: une réponse par décision, des créanciers suivis aussi loin que les données le permettent, et ce qu'il faudrait observer pour conclure. Le livre la déploie sur le cas français — le transfert dans le temps, les créanciers, les services publics — et la prolonge par des scénarios 2025-2035.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

- **Redistribution par dixième et par âge**&nbsp;: Mathias André, Alexis Barrau et Thomas Renaud (Insee), «&nbsp;Revenus des ménages élargis à l'ensemble de l'économie en 2023&nbsp;», [*Insee Analyses* n°&nbsp;118](https://www.insee.fr/fr/statistiques/8974371), 16&nbsp;avril 2026 (figures&nbsp;1c, 1e et 2a).
- **Exposition à un même effort**&nbsp;: Insee, comptes nationaux distribués, [tableau CND.101](https://www.insee.fr/fr/statistiques/8574663), vingtièmes de niveau de vie, 2020-2023, base 2020&nbsp;; calcul de l'auteur, tests de robustesse publiés avec les données.
- **Dette par administration**&nbsp;: INSEE, *Informations rapides* n°&nbsp;79, dette trimestrielle de Maastricht des administrations publiques, 27&nbsp;mars 2026, {{< qp-val "periode_a" >}}.
- **Détenteurs des titres de l'État**&nbsp;: Banque de France, via l'[Agence France Trésor](https://www.aft.gouv.fr/), {{< qp-val "det_periode" >}}.
- **Créanciers indirects des ménages**&nbsp;: Direction générale du Trésor, «&nbsp;Que finance l'épargne financière des ménages français&nbsp;?&nbsp;», [*Trésor-Éco* n°&nbsp;{{< qp-val "tresor_numero" >}}](https://www.tresor.economie.gouv.fr/Articles/2026/01/08/que-finance-l-epargne-financiere-des-menages-francais), 8&nbsp;janvier 2026.
- **Revalorisation des pensions en {{< qp-val "pens_annee" >}}**&nbsp;: [projet de loi de financement de la sécurité sociale pour 2026](https://www.assemblee-nationale.fr/dyn/17/textes/l17b1907_projet-loi.pdf), n°&nbsp;1907, article&nbsp;44&nbsp;; [loi n°&nbsp;2025-1403 du 30&nbsp;décembre 2025](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053226384) de financement de la sécurité sociale pour 2026&nbsp;; [instruction interministérielle DSS/3A/DB/6BRS/2025/174](https://legislation.lassuranceretraite.fr/Pdf/instruction_ministerielle_2025_174_15122025.pdf), 15&nbsp;décembre 2025.

Chaque chiffre de cette page est lu dans ces pièces par un générateur qui en contrôle l'empreinte, et non recopié à la main&nbsp;; les données compilées se téléchargent dans le bloc «&nbsp;Réutiliser&nbsp;» ci-dessous.

## D'où vient cette analyse

{{< canonical-definition >}}

Appliquée aux finances publiques, cette hypothèse est formalisée dans le working paper [AWP-03 — *Dette publique et anthropie&nbsp;: qui paie vraiment le désordre&nbsp;?*](/awp/awp-03/) (DOI&nbsp;: 10.5281/zenodo.19268769, PDF en accès libre). Le working paper [AWP-09](/awp/awp-09/) met cette lecture à l'épreuve des comptes publics&nbsp;: l'incidence d'un même effort dépend de l'instrument retenu, mais l'asymétrie entre ménages mobiles et ménages captifs reste hors de portée des comptes, qui n'observent pas la soustraction des premiers.

{{< reutiliser figures="figures_qui_paie" jeu="qui_paie_donnees" sources="Insee et Banque de France via l'AFT" donnees="Détention de la dette publique (registre du livre, sources INSEE et Banque de France) et comptes nationaux distribués 2023 de l'Insee, avec leurs périodes, unités et conventions, et les tests de robustesse de l'exposition." >}}
La répartition des effets de la dette publique dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir&nbsp;; certaines configurations peuvent reporter des coûts sur des groupes moins capables de les éviter. Les données disponibles montrent qui emprunte, qui détient les titres de l'État et qui contribue ou reçoit aujourd'hui — pas qui supportera la charge finale. Une perte ne s'attribue qu'à une décision déterminée, comparée à son alternative.
{{< /reutiliser >}}
