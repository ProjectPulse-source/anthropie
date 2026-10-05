---
title: "Qui paie vraiment la dette publique ?"
description: "Qui paie la dette publique ? Détenir n'est pas payer : impôts, dépenses et inflation ne répartissent pas l'effort entre les mêmes groupes. Données officielles."
chapo: "Un même effort de {qp.exp_effort} milliards d'euros ne tombe pas sur les mêmes ménages selon la décision prise : par l'enseignement, il pèse surtout sur les plus modestes, par l'impôt sur les plus aisés. Qui paie la dette publique dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir."
date: 2026-07-04
lastmod: 2026-09-29
donnees: [dette_officielle]
og_title: "Qui paie vraiment la dette publique ? — ce que montrent les données — S. Lalut"
og_image: "images/og-qui-paie-dette.jpg"
og_image_alt: "Carte de partage : « Même effort, d'autres payeurs » — un même effort de 10 milliards d'euros, en % du revenu de chaque dixième de niveau de vie, selon trois décisions : baisse de l'enseignement, hausse des impôts, baisse des pensions (Insee, 2023)."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "qui_paie_donnees"
  nom: "Qui paie la dette publique : détention, redistribution et exposition à un même effort"
  description: "Compilation dérivée des séries officielles : dette publique par administration (INSEE) et détenteurs des titres négociables de l'État (Banque de France via l'Agence France Trésor) ; prélèvements et transferts publics par dixième de niveau de vie et par âge, comptes nationaux distribués 2023 (Insee) ; exposition des dixièmes à un même effort de {qp.exp_effort} milliards d'euros selon trois décisions — impôts, pensions, enseignement —, profil comptable et non simulation."
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
    answer: "L'argument rassurant est sérieux : quand le taux d'intérêt reste inférieur à la croissance, le ratio de dette peut se stabiliser, à condition que le déficit hors intérêts — le solde primaire — reste sous un seuil qui dépend de l'écart entre ces deux taux et du niveau de la dette. Au-delà, le ratio monte malgré tout. Et même stable, une dette se sert chaque année : son financement et ses ajustements répartissent des coûts et des avantages entre contribuables, usagers, épargnants et générations. La question utile porte alors sur ce qu'elle finance et sur qui supporte les ajustements — elle se traite configuration par configuration, pas par principe."
  - question: "La dette publique est-elle un fardeau pour les générations futures ?"
    answer: "Pas mécaniquement. Les générations suivantes héritent des engagements, mais aussi de ce qu'ils ont financé — infrastructures, formation, patrimoine public — et d'une partie des titres eux-mêmes, détenus directement ou par l'assurance-vie — ce qui ne neutralise pas nécessairement la charge, la dette pouvant aussi évincer du capital productif. Le transfert net dépend de l'usage : une dette qui finance une consommation courante sans contrepartie durable leur transmet surtout un coût ; un investissement dont elles profiteront peut leur transmettre davantage qu'il ne coûte. Ce qui reste vrai dans tous les cas : la décision est prise sans elles. Ce que les déficits ont effectivement financé, dans les comptes, est mesuré sur la page « La dette publique est-elle un fardeau pour les générations futures ? » (https://stephane-lalut.com/dette-publique-generations-futures/)."
  - question: "Qui détient la dette publique française ?"
    answer: "L'État porte {qp.etat_pct} % de la dette publique ({qp.periode_a}, INSEE). Pour ses titres négociables, la Banque de France publie, via l'Agence France Trésor, une répartition des porteurs en valeur de marché : au premier trimestre 2026, {qp.nonres_pct} % sont détenus par des non-résidents, {qp.bafs_pct} % par des banques, assureurs et fonds résidents, {qp.autres_fr_pct} % par d'autres porteurs résidents — parmi lesquels la Banque de France, dont la part n'est pas publiée. Le classement se fait par résidence du détenteur, non par nationalité, et un ménage peut détenir des titres indirectement, par son assurance-vie ou un fonds. Surtout, détenir n'est pas payer : le porteur a avancé les fonds et en reçoit la rémunération ; la répartition des porteurs ne dit pas qui supporte la charge finale."
  - question: "Qui reçoit plus qu'il ne verse aux administrations publiques ?"
    answer: "En {qp.cd_annee}, d'après les comptes nationaux distribués de l'Insee, {qp.benef_ensemble} % des personnes recevaient plus de transferts publics qu'elles n'en versaient : {qp.benef_d1} % dans le dixième de niveau de vie le plus modeste, {qp.benef_d10} % dans le plus aisé. Le solde bascule au dixième {qp.net_bascule} : les {qp.net_benef_n} premiers dixièmes sont bénéficiaires nets, les trois derniers contributeurs nets, le dernier de {qp.net_d10} euros par unité de consommation. Deux précautions : c'est le solde d'une année et non d'une vie — les pensions de retraite y comptent comme transferts reçus —, et il décrit toute la redistribution publique, pas l'effet propre de la dette."
  - question: "Vaut-il mieux augmenter les impôts ou réduire les dépenses ?"
    answer: "Les données ne tranchent pas ce choix ; elles disent qui supporterait quoi. En répartissant un même effort de {qp.exp_effort} milliards d'euros au prorata des montants existants, une baisse des dépenses d'enseignement représenterait {qp.exp_ens_d1} % du revenu des 10 % les plus modestes contre {qp.exp_ens_d10} % pour les plus aisés ; une hausse des impôts sur les revenus et le patrimoine fait l'inverse, jusqu'à {qp.exp_fisc_d10} % pour le dernier dixième. Le résultat le moins attendu concerne le milieu de l'échelle : aux deux extrémités, la décision la plus lourde pèse au moins {qp.exp_ecart_d10} fois la plus légère, mais en {qp.exp_creux_zone} ce rapport tombe à {qp.exp_ecart_creux} — c'est là que le levier retenu différencie le moins les ménages. Ce creux se situe en {qp.exp_creux_millesimes} sur les quatre millésimes {qp.exp_millesimes} publiés par l'Insee, et il ne dépend pas de la manière de mesurer l'écart. C'est un profil comptable et non une prévision : ni comportement ni effet en retour n'y entrent, et un service public valorisé n'est pas un revenu monétaire."
  - question: "Faut-il rembourser la dette publique ?"
    answer: "Chaque titre arrivé à échéance est remboursé, mais la dette dans son ensemble se refinance : l'État émet de nouveaux titres pour rembourser les anciens, et le stock évolue avec le déficit. Le remboursement intégral du stock est donc une hypothèse largement théorique. La question opératoire porte sur ce que la dette organise pendant qu'elle roule : qui supporte les intérêts, sur quels budgets portent les ajustements, qui hérite des engagements et de ce qu'ils ont financé. Le refinancement renouvelle une échéance aux conditions du moment : il peut alléger ou alourdir la charge, et ne permet pas à lui seul d'identifier qui la supportera."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 20
  nature: "Analyse, appuyée sur des données publiques"
  accueil: 2
---

{{< dossier-dette volet="2" >}}

{{< reutiliser-ancre >}}

Qui paie la dette publique&nbsp;? La question est vécue avant d'être technique&nbsp;: l'impôt qui augmente, le service public qui se resserre, l'épargne que l'inflation rogne. Demander qui supporte les coûts, qui reçoit les revenus et qui décide est une bonne discipline, à condition de ne pas fixer la réponse d'avance. Ce qui se défend d'abord est une réponse en trois temps&nbsp;: **il n'existe pas de payeur unique de la dette&nbsp;; détenir la dette n'est pas la payer&nbsp;; et la répartition de son coût dépend de la décision prise pour l'ajuster.** Que certaines configurations reportent des coûts sur des groupes moins capables de les éviter reste, plus bas, une hypothèse à tester.

Cette page examine ces configurations une à une&nbsp;: ce qui les rend plausibles, ce qui les affaiblirait, et ce que les données disponibles ne permettent pas d'attribuer. Le montant de la facture — encours, charge d'intérêts, coût moyen du stock — est mesuré dans le premier volet du dossier.

{{< dette-chiffres >}}

## Selon la décision, l'effort ne tombe pas sur les mêmes ménages

Tant qu'aucune décision n'est nommée, la question «&nbsp;qui paie&nbsp;?&nbsp;» n'a pas de réponse. Nommée, elle devient mesurable&nbsp;: à quoi ressemblerait la répartition d'un même effort, selon le poste par lequel on le fait passer&nbsp;?

L'exercice qui suit prend {{< qp-val "exp_effort" >}}&nbsp;milliards d'euros et les répartit trois fois — par une hausse des impôts sur les revenus et le patrimoine, par une baisse des pensions de retraite, par une baisse des dépenses d'enseignement —, chaque fois au prorata des montants que chaque dixième verse ou reçoit déjà, puis rapporte le résultat à son revenu. Ce n'est pas une prévision&nbsp;: ni comportement ni effet en retour n'y entrent. C'est la structure actuelle des postes, rendue comparable d'une décision à l'autre.

{{< figure-svg fichier="qui-paie-exposition" alt="Deux panneaux. En haut, trois courbes par dixième de niveau de vie : la baisse des dépenses d'enseignement part très haut sur le premier dixième et décroît fortement ; la hausse des impôts fait l'inverse et monte sur le dernier dixième ; les pensions restent presque plates. En bas, des barres montrant le rapport entre la décision la plus lourde et la plus légère pour chaque dixième : élevé aux deux extrémités, minimal au milieu de l'échelle." >}}Insee, comptes nationaux distribués, tableau CND.101 (vingtièmes de niveau de vie, 2020-2023, base 2020)&nbsp;; millésime 2023. Profil d'exposition comptable, non une simulation.{{< /figure-svg >}}

{{< fig-actions id="exposition" >}}

**Le classement s'inverse d'une décision à l'autre.** Une réduction des dépenses d'enseignement représenterait {{< qp-val "exp_ens_d1" >}}&nbsp;% du revenu des 10&nbsp;% les plus modestes et {{< qp-val "exp_ens_d10" >}}&nbsp;% de celui des plus aisés&nbsp;; une hausse des impôts sur les revenus et le patrimoine, l'inverse, jusqu'à {{< qp-val "exp_fisc_d10" >}}&nbsp;% pour le dernier dixième. Ce n'est pas un effet du dénominateur&nbsp;: en masse, la moitié la moins aisée recevrait {{< qp-val "exp_masse_ens" >}}&nbsp;% de la coupe d'enseignement contre {{< qp-val "exp_masse_fisc" >}}&nbsp;% de l'effort fiscal. Une baisse des pensions, elle, se tient dans une bande étroite — de {{< qp-val "exp_pens_min" >}} à {{< qp-val "exp_pens_max" >}}&nbsp;% — et n'épargne aucun groupe en particulier.

<div class="resultat-phrase">

**Le résultat en une phrase.** «&nbsp;Qui paie la dette&nbsp;?&nbsp;» n'a pas de réponse en soi, il en a une par décision&nbsp;: un même effort pèse surtout sur les plus modestes s'il passe par l'enseignement, surtout sur les plus aisés s'il passe par l'impôt.

</div>

Le second panneau porte le résultat le moins attendu. Pour les 10&nbsp;% les plus aisés, la décision la plus lourde pèse {{< qp-val "exp_ecart_d10" >}}&nbsp;fois la plus légère, et au moins autant pour les 10&nbsp;% les plus modestes&nbsp;: aux deux extrémités de l'échelle, le choix de l'instrument décide presque tout. Au milieu, ce rapport tombe à {{< qp-val "exp_ecart_creux" >}}. **C'est en {{< qp-val "exp_creux_zone" >}} que le levier retenu différencie le moins les ménages.** Cela ne veut pas dire que ces dixièmes supporteraient moins d'effort&nbsp;: seulement que, dans cet exercice, changer de levier y modifie moins l'exposition qu'aux extrémités de l'échelle. Ce creux ne tient ni à l'année — il se situe en {{< qp-val "exp_creux_millesimes" >}} sur les quatre millésimes {{< qp-val "exp_millesimes" >}} publiés par l'Insee — ni à la manière de mesurer l'écart&nbsp;: le coefficient de variation et l'étendue rapportée à la moyenne le placent dans la même zone.

<details class="repli"><summary>Trois limites&nbsp;: un service public valorisé n'est pas un revenu, les décisions sont proportionnelles par construction, un autre dénominateur déplacerait les croisements sans effacer les contrastes</summary>

Trois limites encadrent cette lecture. Un service public valorisé n'est pas un revenu&nbsp;: une dépense d'enseignement imputée à un ménage ne lui est pas versée, et sa réduction ne lui coûterait pas exactement cette somme. Les trois décisions sont proportionnelles par construction&nbsp;; une mesure ciblée — sur certaines pensions, sur certains impôts — dessinerait d'autres courbes, et la figure ne dit donc rien de «&nbsp;l'impôt&nbsp;» ni de «&nbsp;la dépense publique&nbsp;» en général. Enfin l'effort est rapporté au revenu disponible&nbsp;; un autre dénominateur déplacerait les points de croisement sans faire disparaître ces contrastes.

</details>

## Quatre rôles à ne pas confondre

Le débat mélange souvent quatre rôles. L'**emprunteur** est l'administration qui émet la dette — l'État d'abord, puis la sécurité sociale et les collectivités. Le **créancier** avance les fonds et reçoit des intérêts en retour. Le **bénéficiaire** profite de ce que l'emprunt a financé&nbsp;: une route, une école, un revenu de soutien pendant une crise. Celui qui **supporte un coût** subit, par rapport à l'alternative considérée, une perte de revenu, de patrimoine ou de services liée aux choix de financement ou d'ajustement&nbsp;: le contribuable qui paie un impôt supplémentaire, l'usager d'un service dont les moyens se resserrent, l'épargnant dont l'inflation érode le placement.

Une même personne tient souvent plusieurs de ces rôles&nbsp;: elle paie l'impôt, se soigne à l'hôpital public et détient des titres de l'État par son assurance-vie. Les groupes examinés plus bas se recoupent donc&nbsp;; ils ne se partagent pas la dette comme les parts d'un gâteau.

Reste une question que toute réponse doit nommer&nbsp;: «&nbsp;qui paie&nbsp;» — par rapport à quelle autre décision&nbsp;? Moins emprunter aurait signifié augmenter un impôt, renoncer à une dépense ou la décaler. Attribuer une perte suppose de dire à quelle alternative on la compare.

## Ce que les données permettent de voir

Trois choses se mesurent&nbsp;: qui emprunte, qui détient les titres, et qui contribue ou reçoit aujourd'hui.

{{< figure-svg fichier="qui-paie-detention" alt="Deux panneaux de barres horizontales, séparés. En haut, la dette publique par administration emprunteuse, en valeur nominale : l'État très largement en tête. En bas, les porteurs des titres négociables de l'État, en valeur de marché : les non-résidents en tête." >}}Deux champs distincts&nbsp;: A en valeur nominale (INSEE), B en valeur de marché (Banque de France, via l'Agence France Trésor). Les valeurs viennent du même registre que la figure de la p.&nbsp;101 du livre.{{< /figure-svg >}}

{{< fig-actions id="detention" >}}

**Qui emprunte, qui détient.** L'État porte l'essentiel de la dette publique&nbsp;: {{< qp-val "etat_mdeur" >}}&nbsp;milliards d'euros sur {{< qp-val "total_mdeur" >}}, soit {{< qp-val "etat_pct" >}}&nbsp;%, {{< qp-val "periode_a" >}}. Ses titres négociables sont détenus, au premier trimestre 2026, à {{< qp-val "nonres_pct" >}}&nbsp;% par des non-résidents&nbsp;; banques, assureurs et fonds résidents en portent ensemble {{< qp-val "bafs_pct" >}}&nbsp;%&nbsp;; les autres porteurs résidents, {{< qp-val "autres_fr_pct" >}}&nbsp;%, comprennent la Banque de France, dont la source ne publie pas la part. Les deux panneaux ne se combinent pas&nbsp;: le premier est en valeur nominale, le second en valeur de marché, et aucun des deux ne dit qui supporte la charge.

{{< figure-svg fichier="qui-paie-redistribution" alt="Barres par dixième de niveau de vie, en 2023. Au-dessus de zéro, les transferts reçus, d'un niveau voisin d'un dixième à l'autre ; sous zéro, les prélèvements, qui croissent fortement du premier au dernier dixième." >}}Insee, comptes nationaux distribués 2023 (*Insee Analyses* n°&nbsp;118, 16&nbsp;avril 2026, figure&nbsp;1c), en euros par unité de consommation.{{< /figure-svg >}}

{{< fig-actions id="redistribution" >}}
{{< qp-tableau-redistribution >}}

**Qui contribue, qui reçoit aujourd'hui.** Les comptes nationaux distribués de l'Insee répartissent, pour {{< qp-val "cd_annee" >}}, prélèvements et transferts publics entre les **dixièmes de niveau de vie** — la population rangée du plus modeste au plus aisé, puis coupée en dix parts d'effectif égal. Les montants y sont exprimés **par unité de consommation** (UC), l'unité qui rend comparables des ménages de tailles différentes&nbsp;: une personne seule compte 1&nbsp;UC, un couple avec deux enfants de moins de 14&nbsp;ans, 2,1.

Les prélèvements vont de {{< qp-val "d1_prel" >}}&nbsp;€ par UC pour les 10&nbsp;% les plus modestes à {{< qp-val "d10_prel" >}}&nbsp;€ pour les 10&nbsp;% les plus aisés, environ {{< qp-val "ratio_prel" >}}&nbsp;fois plus. Les transferts reçus — prestations en espèces et services publics valorisés en euros — varient beaucoup moins&nbsp;: d'un bout à l'autre de l'échelle, ils restent compris entre {{< qp-val "recu_min" >}} et {{< qp-val "recu_max" >}}&nbsp;€, sans progression régulière. C'est ce contraste, et lui seul, que la figure établit&nbsp;: ce qui est versé suit le niveau de vie, ce qui est reçu beaucoup moins.

<div class="resultat-phrase">

**Où la dette entre dans ces comptes.** En {{< qp-val "cd_annee" >}}, les transferts publics attribués aux ménages — prestations en espèces et services publics valorisés en euros — dépassent les prélèvements de {{< qp-val "solde_mdeur" >}}&nbsp;milliards d'euros dans ce cadre comptable, et l'Insee rattache ce solde à l'endettement public. Cela ne veut pas dire que les bénéficiaires de la redistribution «&nbsp;ont créé&nbsp;» cette dette, ni que leur position dit qui la remboursera&nbsp;: c'est la part du revenu élargi de l'année qui n'est pas financée par des prélèvements de la même année.

</div>

<details class="repli"><summary>Les transferts dépassent les prélèvements de {{< qp-val "solde_mdeur" >}}&nbsp;milliards d'euros&nbsp;: un solde réparti par convention, financé à crédit, qui ne dit pas qui paiera demain</summary>

La même année, les transferts attribués aux ménages ont dépassé les prélèvements&nbsp;: {{< qp-val "solde_uc" >}}&nbsp;€ par UC en moyenne, soit {{< qp-val "solde_mdeur" >}}&nbsp;milliards d'euros, financés par endettement. Ce total porte sur le champ de ces comptes distribués, qui n'est pas celui du déficit public&nbsp;: les deux montants ne se substituent pas l'un à l'autre. Dans cette construction comptable, l'écart élève le niveau de vie élargi des ménages de l'année — un bénéfice présent, financé à crédit. Ce ne sont pas pour autant {{< qp-val "solde_mdeur" >}}&nbsp;milliards de versements identifiables&nbsp;: c'est un solde réparti par convention d'imputation. Pour calculer un niveau de vie «&nbsp;net de l'endettement&nbsp;», l'Insee répartit cet écart par convention — moitié en moindres prélèvements, moitié en transferts supplémentaires&nbsp;; les figures de cette page présentent les transferts courants, avant ce retraitement. Ces comptes décrivent qui contribue et qui reçoit aujourd'hui&nbsp;; ils ne disent pas qui paiera demain la dette qui finance l'écart.

</details>

{{< figure-svg fichier="qui-paie-solde-net" alt="Deux panneaux. En haut, le solde des transferts publics par dixième de niveau de vie : en moyenne par unité de consommation, négatif pour les sept premiers dixièmes, positif pour les trois derniers, très fortement pour le dernier. En bas, la part de personnes bénéficiaires nettes, décroissante du premier au dernier dixième." >}}Insee, comptes nationaux distribués 2023 (figure&nbsp;2a). Deux unités, deux panneaux&nbsp;: euros par unité de consommation, puis part de personnes.{{< /figure-svg >}}

{{< fig-actions id="solde-net" >}}

**Qui verse net, qui reçoit net.** En moyenne par UC, le solde bascule au dixième {{< qp-val "net_bascule" >}}&nbsp;: dans chacun des {{< qp-val "net_benef_n" >}} premiers dixièmes, les transferts reçus dépassent les prélèvements — de {{< qp-val "net_d1" >}}&nbsp;€ par UC dans le premier —, dans les trois derniers c'est l'inverse, et dans le dernier dixième le prélèvement net moyen atteint {{< qp-val "net_d10" >}}&nbsp;€ par UC.

Rapporté aux personnes, le tableau change. {{< qp-val "benef_ensemble" >}}&nbsp;% sont bénéficiaires nettes cette année-là, {{< qp-val "benef_d1" >}}&nbsp;% dans le premier dixième et {{< qp-val "benef_d10" >}}&nbsp;% dans le dernier. Mais les bénéficiaires nets ne sont majoritaires que dans les {{< qp-val "benef_majo_n" >}} premiers dixièmes&nbsp;: dans le dixième {{< qp-val "benef_dernier_moyen" >}}, bénéficiaire net en moyenne, ils ne sont plus que {{< qp-val "benef_dernier_moyen_pct" >}}&nbsp;%. **Un groupe peut recevoir plus qu'il ne verse en moyenne alors que la majorité de ses membres versent plus qu'ils ne reçoivent**&nbsp;: quelques soldes très positifs suffisent à porter la moyenne.

Le rapprochement avec l'exercice du haut de page est direct. Les dixièmes du milieu sont ceux où le solde moyen dit «&nbsp;bénéficiaire net&nbsp;» alors que la majorité de leurs membres versent plus qu'ils ne reçoivent — et ce sont ceux dont l'exposition varie le moins selon le levier. Recevoir plus que l'on ne verse ne protège donc pas d'un ajustement&nbsp;: la position dans la redistribution d'aujourd'hui et l'exposition à la décision de demain sont deux classements distincts, et ils ne se recouvrent pas.

<details class="repli"><summary>Conventions&nbsp;: le solde d'une année, non d'une vie&nbsp;; des services publics imputés, non mesurés&nbsp;; toute la redistribution, pas l'effet propre de la dette</summary>

Plusieurs conventions encadrent cette lecture. C'est le solde d'une **année**, non d'une vie&nbsp;: les pensions de retraite y sont comptées comme prestations courantes. Les transferts comprennent des services publics — soins, éducation, services collectifs — valorisés en euros et répartis par imputation statistique, non un relevé des services utilisés par chacun&nbsp;; la part de bénéficiaires nets en dépend à la marge. Le revenu «&nbsp;avant transferts&nbsp;» est une étape de calcul, non le revenu qu'aurait chacun dans une économie sans impôts ni services publics. Et ce solde décrit la redistribution dans son ensemble, pas l'effet propre de la dette.

</details>

<details class="repli"><summary>Par âge&nbsp;: les ménages de 65&nbsp;ans ou plus reçoivent {{< qp-val "age_recu_65" >}}&nbsp;€ par unité de consommation, pensions comprises, et versent {{< qp-val "age_prel_65" >}}&nbsp;€ — une photographie annuelle, non un bilan de vie</summary>

{{< figure-svg fichier="qui-paie-age" alt="Barres par groupe d'âge du ménage, en 2023 : les transferts reçus augmentent avec l'âge, modérément jusqu'à 64 ans puis très fortement pour les ménages de 65 ans ou plus ; les prélèvements versés croissent jusqu'aux 50-64 ans, puis chutent pour ce dernier groupe." >}}Insee, comptes nationaux distribués 2023 (figure&nbsp;1e). Groupes d'âge moyen des adultes du ménage.{{< /figure-svg >}}

{{< fig-actions id="age" >}}

**Par âge.** En {{< qp-val "cd_annee" >}}, selon ces conventions, les ménages dont l'âge moyen des adultes atteint 65&nbsp;ans ou plus reçoivent {{< qp-val "age_recu_65" >}}&nbsp;€ par unité de consommation de transferts — dont {{< qp-val "age_esp_65" >}}&nbsp;€ de prestations en espèces, pensions comprises — et versent {{< qp-val "age_prel_65" >}}&nbsp;€ de prélèvements, contre {{< qp-val "age_prel_5064" >}}&nbsp;€ pour les ménages de 50 à 64&nbsp;ans. <details class="repli"><summary>Trois limites&nbsp;: des pensions acquises comptées comme prestations, un âge du ménage qui n'est pas un statut de retraite, une photographie qui ne désigne aucun payeur de demain</summary>

Trois limites l'encadrent. Les pensions correspondent notamment à des droits acquis au cours de la carrière&nbsp;; elles sont ici comptées comme prestations courantes, et le tableau d'une vie entière ne ressemblerait pas à celui d'une année. L'âge du ménage n'est pas le statut de retraite de chacun de ses membres, et un montant élevé de soins imputés traduit aussi des besoins plus élevés, non un avantage de bien-être. Enfin, cette photographie actuelle n'est pas une mesure du bilan des générations futures&nbsp;: elle ne désigne aucun payeur de demain.

</details>

</details>

## Par quels canaux la charge peut se répartir

Quatre mécanismes peuvent modifier la charge de la dette et sa répartition, et ils se combinent&nbsp;:

- **les prélèvements** — impôts et cotisations supplémentaires, ou baisses d'impôt auxquelles on renonce&nbsp;;
- **les dépenses et les prestations** — ce qui est réduit, gelé ou reporté pour dégager la marge&nbsp;;
- **l'inflation**, et plus précisément la part d'inflation **non anticipée au moment où le taux d'un titre a été fixé**&nbsp;: ce qui était attendu à cette date tend à être déjà incorporé au taux exigé à l'émission, et n'opère alors aucun transfert. C'est l'écart entre l'inflation réalisée et celle-là qui réduit la valeur réelle des créances nominales déjà émises, et reporte une partie de la charge sur leurs détenteurs et sur les revenus mal indexés. Deux mécanismes jouent en sens inverse&nbsp;: les titres indexés voient leur charge monter avec les prix, et le refinancement se fait aux taux nouveaux. L'effet net dépend donc de la part indexée, du calendrier de refinancement et de ce qui était anticipé — et la France ne choisit pas seule son inflation. À ne pas confondre avec l'effet de l'inflation sur le *ratio* de dette, qui passe par le PIB nominal et ne désigne, lui, aucun perdant&nbsp;;
- **la restructuration**, cas extrême&nbsp;: la perte de **premier rang** est imposée aux porteurs des titres. Où elle s'arrête est une autre question — une banque, un assureur ou un fonds la répercute sur ses actionnaires, ses assurés ou ses épargnants, et l'État peut avoir à intervenir. Ici comme ailleurs, le porteur n'est pas nécessairement celui qui supporte.

La liste n'est pas exhaustive&nbsp;: la croissance, les revenus ou cessions d'actifs et les conditions de financement interviennent aussi — une cession finance un paiement en réduisant un patrimoine, la croissance améliore le ratio sans prélever sur un groupe —, et l'histoire connaît la répression financière, qui contraint les rendements. Le refinancement, lui, renouvelle une échéance aux conditions du moment&nbsp;: il peut alléger ou alourdir la charge, et ne permet pas à lui seul d'identifier qui la supportera. Et en face de ces coûts se trouve ce que la dette a financé&nbsp;: les bénéfices, présents et futurs, de la dépense publique entrent dans le bilan au même titre que la charge.

{{< figure-svg fichier="qui-paie-mecanismes" alt="Schéma sans quantités : la charge de la dette et sa répartition mènent, par des flèches d'égale épaisseur, à quatre mécanismes possibles — prélèvements, dépenses et prestations, inflation, restructuration — ; le refinancement renouvelle l'échéance aux taux du moment ; en regard, ce que la dette a financé." >}}Schéma de mécanismes possibles&nbsp;: aucun poids relatif ni effet causal n'y est mesuré.{{< /figure-svg >}}

{{< fig-actions id="mecanismes" >}}

## Les générations futures — ce dont elles héritent

La dette convertit une dépense présente en engagements futurs. Ceux qui viendront après héritent donc de ces engagements sans avoir pris part à la décision qui les a créés. Mais ils héritent aussi de ce que cette dépense a financé — infrastructures, formation, recherche, patrimoine public — et d'une partie des titres eux-mêmes, que leurs parents détiennent directement ou par l'assurance-vie&nbsp;: dans la même succession passent la charge et la créance. Cela ne les neutralise pas nécessairement&nbsp;: certains modèles identifient aussi un canal d'éviction du capital productif, lorsque les titres publics prennent sa place dans les patrimoines — un canal que cette page ne mesure pas en France. Le transfert net dépend donc de l'usage, mais pas de lui seul&nbsp;: l'absence de bénéfice durable entre dans le bilan, et le coût net dépend aussi du financement, des créances transmises et de l'alternative retenue&nbsp;; un investissement dont ils profiteront peut leur transmettre davantage qu'il ne coûte.

<details class="repli"><summary>La dette nette ne tranche pas non plus&nbsp;: elle ne déduit ni les routes ni le capital humain&nbsp;; l'objection «&nbsp;on se la doit à nous-mêmes&nbsp;» est traitée à part</summary>

L'encours ne suffit pas à trancher, et la dette nette ne le fait pas davantage&nbsp;: celle que publie l'INSEE ne déduit que certains actifs financiers — trésorerie, prêts, titres —, pas les routes, le capital humain ni l'environnement. Ce qui vaut quel que soit l'usage, c'est que la décision se prend sans ceux qui en porteront une part. L'objection «&nbsp;on se la doit à nous-mêmes&nbsp;» et sa réponse sont développées sur la page [La dette publique est-elle un fardeau pour les générations futures&nbsp;?](/dette-publique-generations-futures/)

</details>

## Les groupes moins mobiles — une hypothèse à tester

Tous les contribuables ne sont pas égaux devant l'ajustement. Les ménages et les entreprises qui peuvent déplacer leurs revenus, leur patrimoine ou leur activité échappent plus facilement à un prélèvement que les salariés, les retraités ou les usagers qui dépendent d'un service public local. D'où l'hypothèse&nbsp;: quand l'ajustement suit la ligne de moindre résistance, il **peut** peser davantage sur ceux qui ne peuvent pas partir. Pour être testable, elle doit fixer ses mesures avant d'observer l'ajustement&nbsp;: à ajustement donné et situations initiales comparables, une moindre capacité d'évitement devrait aller avec un effort plus élevé. Et la capacité d'évitement n'est pas une variable unique&nbsp;: mobilité géographique, mobilité de la base imposable et capacité à remplacer un service public sont trois propriétés différentes.

<details class="repli"><summary>Pour la tester&nbsp;: des groupes définis d'avance, un ajustement précis, une mesure de l'effort fixée, et les cas qui l'affaibliraient nommés avant l'observation</summary>

Pour la tester, il faut définir ces groupes indépendamment du résultat, préciser l'ajustement étudié — telle réforme fiscale, tel gel de prestations — et choisir une mesure de l'effort. Elle serait affaiblie par un ajustement portant surtout sur d'autres groupes, ou par des compensations accordées aux perdants identifiés&nbsp;; ces cas ne se relisent pas après coup comme des confirmations. Le canal territorial — l'État qui reporte une part de sa contrainte sur les collectivités — est examiné sur la page [Dette publique&nbsp;: pourquoi les collectivités locales sont-elles la variable d'ajustement&nbsp;?](/dette-publique-collectivites-locales/)

</details>

## Les créanciers — financer n'est pas gagner

«&nbsp;Qui détient la dette&nbsp;?&nbsp;» est la question la plus posée, et elle ne dit pas qui paie. Le créancier a avancé les fonds&nbsp;: les intérêts rémunèrent cette avance, le temps et le risque. Son **rendement réel** tient compte des intérêts, de la variation de valeur du titre et de l'inflation&nbsp;; son **avantage par rapport à un autre placement** se mesure séparément, à horizon et risque comparables. Les deux varient selon la date d'achat et le type de titre. La détention renseigne sur la destination des intérêts, pas sur ceux qui les financent.

<details class="repli"><summary>Porteurs classés par résidence, non par nationalité, et photographiés en stock&nbsp;: la répartition ne mesure pas la part des intérêts versés hors de France</summary>

Pour les titres négociables de l'État, la répartition des porteurs est publiée par la Banque de France, via l'Agence France Trésor, en valeur de marché. Elle classe les porteurs par **résidence**, non par nationalité&nbsp;: un «&nbsp;non-résident&nbsp;» peut être un fonds étranger qui gère l'épargne de ménages français, et un ménage français peut détenir des titres de l'État sans le savoir, par son assurance-vie. Une part du stock détenue hors de France ne mesure pas non plus la part des intérêts versés hors de France&nbsp;: une photographie de fin de période ne donne pas un flux annuel.

</details>

## Les investissements à bénéfices différés — un mécanisme à établir cas par cas

Un budget contraint par le service de la dette **peut inciter à reporter** des dépenses dont les bénéfices sont lointains, notamment lorsque leur report produit peu de coût politique ou budgétaire immédiat&nbsp;: recherche, entretien du patrimoine, formation, transition écologique. <details class="repli"><summary>Plausible, non établi&nbsp;: aucun agrégat ne mesure un investissement empêché par les intérêts&nbsp;; il faut remonter décision par décision</summary>

C'est une classe, et non un cas particulier — l'exemple écologique n'a rien de singulier, il est seulement celui où l'écart entre la dépense et son bénéfice est le plus long. Le mécanisme est plausible&nbsp;; il reste à l'établir projet par projet&nbsp;: quelle dépense a été reportée, par quelle décision, pour quel motif budgétaire. Les agrégats ne suffisent pas&nbsp;: l'investissement public total n'est pas l'investissement climatique, et la fonction «&nbsp;protection de l'environnement&nbsp;» des comptes publics ne couvre pas toute la transition. Aucun d'eux ne mesure un investissement empêché par les intérêts. Là où le mécanisme est établi, il double le transfert&nbsp;: aux engagements financiers transmis s'ajoute le bénéfice qui n'a pas été construit — un patrimoine non entretenu, une transition retardée —, et ce second transfert-là n'apparaît dans aucun encours.

</details>

## Les objections qui comptent

- **La dette finance aussi des bénéfices présents.** Services, prestations et investissements financés à crédit profitent à des ménages aujourd'hui&nbsp;; une analyse qui ne compte que les coûts ne décrit que la moitié du bilan.
- **On se la doit en partie à nous-mêmes.** Une part des titres est détenue, directement ou non, par des ménages résidents&nbsp;: les intérêts qu'ils reçoivent sont aussi un revenu. Reste à savoir qui, parmi les résidents, reçoit ces intérêts et qui les finance.
- **Moins emprunter aurait aussi coûté.** Un impôt plus lourd ou une dépense abandonnée plus tôt auraient eu leurs propres perdants&nbsp;; la comparaison honnête porte sur ces alternatives, pas sur un monde sans coût.
- **Tant que la croissance nominale dépasse le taux d'intérêt implicite, le ratio de dette peut se stabiliser.** L'argument est sérieux et il a souvent été vrai&nbsp;: sous cette condition, le ratio de dette peut rester stable même avec un déficit hors intérêts, pourvu que ce déficit primaire reste sous un seuil qui dépend de l'écart entre les deux taux et du niveau de la dette. Au-delà, le ratio monte malgré tout. Et même stable, une dette se sert chaque année&nbsp;: la question de la répartition demeure.

## Ce que ces données ne permettent pas d'établir

Aucune statistique ne dit, à elle seule, qui supporte au bout du compte la charge de la dette française&nbsp;: l'incidence finale d'un euro d'intérêts dépend des ajustements choisis année après année, et de l'alternative à laquelle on les compare. Une répartition actuelle des impôts et des prestations décrit qui contribue et qui reçoit aujourd'hui&nbsp;; elle n'identifie pas les payeurs futurs de la dette. Une moyenne par unité de consommation n'est pas une facture individuelle&nbsp;: elle est compatible avec une dispersion considérable, et une personne qui reçoit beaucoup de prestations peut perdre à une réforme précise.

Ce qui peut s'établir, c'est l'effet d'une décision déterminée — une réforme, un gel, un report — sur des groupes définis d'avance. C'est à ce niveau que la question «&nbsp;qui paie&nbsp;?&nbsp;» reçoit des réponses vérifiables.

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

## Ce qu'il faut retenir

**Une question de répartition n'a pas de réponse en soi&nbsp;; elle en a une par décision.** L'incidence d'un euro d'intérêts ne se lit nulle part dans les comptes, parce qu'elle se forme ailleurs&nbsp;: dans l'ajustement retenu cette année-là — impôt, dépense, inflation, report — et dans l'alternative à laquelle on le compare. Nommer les deux transforme une opinion en énoncé vérifiable&nbsp;; ne nommer ni l'un ni l'autre produit une réponse qui ne peut être ni établie, ni réfutée.

**Détenir n'est pas payer.** Le porteur d'un titre a avancé les fonds et reçoit une rémunération en retour&nbsp;; le paiement des intérêts relève du budget public, qui peut le financer par ses recettes ou par de nouveaux emprunts. La question distributive commence ensuite&nbsp;: quels prélèvements, quelles dépenses, quelle inflation ou quelle restructuration accompagnent l'ajustement, et par rapport à quelle alternative. La répartition des porteurs renseigne sur la destination des intérêts, jamais sur leur origine — deux questions que la même figure ne peut pas trancher, d'où ses deux panneaux séparés.

**Une moyenne de groupe ne décrit pas ses membres.** C'est le résultat le moins intuitif de cette page&nbsp;: un dixième de niveau de vie peut recevoir plus qu'il ne verse *en moyenne* alors que la majorité des personnes qui le composent versent plus qu'elles ne reçoivent — quelques soldes très positifs suffisent à porter la moyenne. Une statistique de dixièmes répond donc à «&nbsp;comment se répartit la masse&nbsp;?&nbsp;», pas à «&nbsp;que vit une personne de ce dixième&nbsp;?&nbsp;».

**Sur les générations, un seul énoncé résiste à l'objection du bilan.** Qu'une dette pèse ou profite à ceux qui suivent dépend de son usage, du financement et des créances transmises&nbsp;: l'encours ne le dit pas, et la dette nette publiée ne le dit pas davantage, puisqu'elle ne déduit que certains actifs financiers. Ce qui reste vrai dans tous les cas est d'un autre ordre&nbsp;: la décision se prend sans ceux qui en porteront une part.

<div class="prolongements" role="group" aria-label="Prolongements du dossier">
<p class="prolongements__titre">Prolongements du dossier&nbsp;: deux applications de «&nbsp;qui paie&nbsp;?&nbsp;»</p>
<a class="prolongements__carte" href="/dette-publique-collectivites-locales/"><b>Collectivités locales</b><span>Comment une contrainte de l'État peut descendre vers des collectivités peu endettées mais très encadrées.</span></a>
<a class="prolongements__carte" href="/dette-publique-generations-futures/"><b>Générations futures</b><span>Quand la dette constitue-t-elle réellement un transfert vers ceux qui viennent après&nbsp;?</span></a>
</div>



{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Cette analyse est développée dans le livre" avis="non" >}}
Cette page pose la méthode&nbsp;: quatre rôles, quatre canaux, et ce qu'il faudrait observer pour conclure. Le livre la déploie sur le cas français — le transfert dans le temps, les créanciers, les services publics — et la prolonge par des scénarios 2025-2035.
{{< /appel-livre >}}

## D'où vient cette analyse

{{< canonical-definition >}}

Appliquée aux finances publiques, cette hypothèse est formalisée dans le working paper [AWP-03 — *Dette publique et anthropie&nbsp;: qui paie vraiment le désordre&nbsp;?*](/awp/awp-03/) (DOI&nbsp;: 10.5281/zenodo.19268769, PDF en accès libre). Le working paper [AWP-09](/awp/awp-09/) met cette lecture à l'épreuve des comptes publics&nbsp;: l'incidence d'un même effort dépend de l'instrument retenu, mais l'asymétrie entre ménages mobiles et ménages captifs reste hors de portée des comptes, qui n'observent pas la soustraction des premiers.

{{< reutiliser figures="figures_qui_paie" jeu="qui_paie_donnees" sources="Insee et Banque de France via l'AFT" donnees="Détention de la dette publique (registre du livre, sources INSEE et Banque de France) et comptes nationaux distribués 2023 de l'Insee, avec leurs périodes, unités et conventions." >}}
La répartition des effets de la dette publique dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir&nbsp;; certaines configurations peuvent reporter des coûts sur des groupes moins capables de les éviter. Les données disponibles montrent qui emprunte, qui détient les titres de l'État et qui contribue ou reçoit aujourd'hui — pas qui supportera la charge finale. Une perte ne s'attribue qu'à une décision déterminée, comparée à son alternative.
{{< /reutiliser >}}
