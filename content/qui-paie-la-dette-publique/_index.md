---
title: "Qui paie vraiment la dette publique ?"
description: "Qui supporte le coût de la dette publique ? Cela dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir ; certaines configurations reportent des coûts sur ceux qui peuvent le moins les éviter. Les rôles, les canaux, leurs conditions — et ce que les données ne permettent pas d'attribuer."
date: 2026-07-04
lastmod: 2026-09-21
faq:
  - question: "La dette publique est-elle vraiment un problème ?"
    answer: "L'argument rassurant est sérieux : quand le taux d'intérêt reste inférieur à la croissance, le ratio de dette peut se stabiliser, à condition que le déficit hors intérêts — le solde primaire — reste sous un seuil qui dépend de l'écart entre ces deux taux et du niveau de la dette. Au-delà, le ratio monte malgré tout. Et même stable, une dette se sert chaque année : son financement et ses ajustements répartissent des coûts et des avantages entre contribuables, usagers, épargnants et générations. La question utile porte alors sur ce qu'elle finance et sur qui supporte les ajustements — elle se traite configuration par configuration, pas par principe."
  - question: "La dette publique est-elle un fardeau pour les générations futures ?"
    answer: "Pas mécaniquement. Les générations suivantes héritent des engagements, mais aussi de ce qu'ils ont financé — infrastructures, formation, patrimoine public — et d'une partie des titres eux-mêmes, détenus directement ou par l'assurance-vie. Le transfert net dépend de l'usage : une dette qui finance une consommation courante sans contrepartie durable leur transmet surtout un coût ; un investissement dont elles profiteront peut leur transmettre davantage qu'il ne coûte. Ce qui reste vrai dans tous les cas : la décision est prise sans elles."
  - question: "Qui détient la dette publique française ?"
    answer: "L'État porte {qp.etat_pct} % de la dette publique ({qp.periode_a}, INSEE). Pour ses titres négociables, la Banque de France publie, via l'Agence France Trésor, une répartition des porteurs en valeur de marché : au premier trimestre 2026, {qp.nonres_pct} % sont détenus par des non-résidents, {qp.bafs_pct} % par des banques, assureurs et fonds français, {qp.autres_fr_pct} % par d'autres porteurs français — parmi lesquels la Banque de France, dont la part n'est pas publiée. Le classement se fait par résidence du détenteur, non par nationalité, et un ménage peut détenir des titres indirectement, par son assurance-vie ou un fonds. Surtout, détenir n'est pas payer : le porteur a avancé les fonds et en reçoit la rémunération ; la répartition des porteurs ne dit pas qui supporte la charge finale."
  - question: "Faut-il rembourser la dette publique ?"
    answer: "Chaque titre arrivé à échéance est remboursé, mais la dette dans son ensemble se refinance : l'État émet de nouveaux titres pour rembourser les anciens, et le stock évolue avec le déficit. Le remboursement intégral du stock est donc une hypothèse largement théorique. La question opératoire porte sur ce que la dette organise pendant qu'elle roule : qui supporte les intérêts, sur quels budgets portent les ajustements, qui hérite des engagements et de ce qu'ils ont financé. Le refinancement reporte une échéance ; il ne désigne à lui seul aucun perdant."
---

{{< dossier-dette volet="2" >}}

{{< reutiliser-ancre >}}

Qui paie la dette publique&nbsp;? La question est vécue avant d'être technique&nbsp;: l'impôt qui augmente, le service public qui se resserre, l'épargne que l'inflation rogne. Demander qui supporte les coûts, qui reçoit les revenus et qui décide est une bonne discipline, à condition de ne pas fixer la réponse d'avance. Ce qui se défend tient en une proposition conditionnelle&nbsp;: **la répartition des effets de la dette dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir&nbsp;; certaines configurations peuvent reporter des coûts sur des groupes moins capables de les éviter.**

Cette page examine ces configurations une à une&nbsp;: ce qui les rend plausibles, ce qui les affaiblirait, et ce que les données disponibles ne permettent pas d'attribuer. Le montant de la facture — encours, charge d'intérêts, coût moyen du stock — est mesuré dans le premier volet du dossier.

{{< dette-chiffres >}}

## Quatre rôles à ne pas confondre

Le débat mélange souvent quatre rôles. L'**emprunteur** est l'administration qui émet la dette — l'État d'abord, puis la sécurité sociale et les collectivités. Le **créancier** avance les fonds et reçoit des intérêts en retour. Le **bénéficiaire** profite de ce que l'emprunt a financé&nbsp;: une route, une école, un revenu de soutien pendant une crise. Celui qui **supporte le coût** est celui dont l'effort sert la dette&nbsp;: le contribuable qui paie un impôt supplémentaire, l'usager d'un service dont les moyens se resserrent, l'épargnant dont l'inflation érode le placement.

Une même personne tient souvent plusieurs de ces rôles&nbsp;: elle paie l'impôt, se soigne à l'hôpital public et détient des titres de l'État par son assurance-vie. Les groupes examinés plus bas se recoupent donc&nbsp;; ils ne se partagent pas la dette comme les parts d'un gâteau.

Reste une question que toute réponse doit nommer&nbsp;: «&nbsp;qui paie&nbsp;» — par rapport à quelle autre décision&nbsp;? Moins emprunter aurait signifié augmenter un impôt, renoncer à une dépense ou la décaler. Attribuer une perte suppose de dire à quelle alternative on la compare.

## Ce que les données permettent de voir

Trois choses se mesurent&nbsp;: qui emprunte, qui détient les titres, et qui contribue ou reçoit aujourd'hui.

{{< figure-svg fichier="qui-paie-detention" alt="Deux panneaux de barres horizontales, séparés. En haut, la dette publique par administration emprunteuse, en valeur nominale : l'État très largement en tête. En bas, les porteurs des titres négociables de l'État, en valeur de marché : les non-résidents en tête." >}}Deux champs distincts&nbsp;: A en valeur nominale (INSEE), B en valeur de marché (Banque de France, via l'Agence France Trésor). Les valeurs viennent du même registre que la figure de la p.&nbsp;101 du livre.{{< /figure-svg >}}
{{< fig-actions id="detention" >}}

**Qui emprunte, qui détient.** L'État porte l'essentiel de la dette publique&nbsp;: {{< qp-val "etat_mdeur" >}}&nbsp;milliards d'euros sur {{< qp-val "total_mdeur" >}}, soit {{< qp-val "etat_pct" >}}&nbsp;%, {{< qp-val "periode_a" >}}. Ses titres négociables sont détenus, au premier trimestre 2026, à {{< qp-val "nonres_pct" >}}&nbsp;% par des non-résidents&nbsp;; banques, assureurs et fonds français en portent ensemble {{< qp-val "bafs_pct" >}}&nbsp;%&nbsp;; les autres porteurs français, {{< qp-val "autres_fr_pct" >}}&nbsp;%, comprennent la Banque de France, dont la source ne publie pas la part. Les deux panneaux ne se combinent pas&nbsp;: le premier est en valeur nominale, le second en valeur de marché, et aucun des deux ne dit qui supporte la charge.

{{< figure-svg fichier="qui-paie-redistribution" alt="Barres par dixième de niveau de vie, en 2023. Au-dessus de zéro, les transferts reçus, d'un niveau voisin d'un dixième à l'autre ; sous zéro, les prélèvements, qui croissent fortement du premier au dernier dixième." >}}Insee, comptes nationaux distribués 2023 (*Insee Analyses* n°&nbsp;118, 16&nbsp;avril 2026, figure&nbsp;1c), en euros par unité de consommation.{{< /figure-svg >}}
{{< fig-actions id="redistribution" >}}
{{< qp-tableau-redistribution >}}

**Qui contribue, qui reçoit aujourd'hui.** Les comptes nationaux distribués de l'Insee répartissent, pour {{< qp-val "cd_annee" >}}, prélèvements et transferts publics entre les dixièmes de niveau de vie. Les prélèvements vont de {{< qp-val "d1_prel" >}}&nbsp;€ par unité de consommation pour les 10&nbsp;% les plus modestes à {{< qp-val "d10_prel" >}}&nbsp;€ pour les 10&nbsp;% les plus aisés, environ {{< qp-val "ratio_prel" >}}&nbsp;fois plus&nbsp;; les transferts reçus — prestations en espèces et services publics valorisés en euros — varient beaucoup moins, de {{< qp-val "recu_min" >}} à {{< qp-val "recu_max" >}}&nbsp;€. La même année, la puissance publique a versé plus qu'elle n'a prélevé&nbsp;: {{< qp-val "solde_uc" >}}&nbsp;€ par unité de consommation en moyenne, {{< qp-val "solde_mdeur" >}}&nbsp;milliards au total, financés par endettement. C'est un bénéfice présent financé à crédit, que l'Insee répartit par convention — moitié en moindres prélèvements, moitié en transferts supplémentaires. Ces comptes décrivent qui contribue et qui reçoit aujourd'hui&nbsp;; ils ne disent pas qui paiera demain la dette qui finance l'écart.

## Par quels canaux la charge se répartit

Une dette se sert par quatre voies, qui se combinent&nbsp;:

- **les prélèvements** — impôts et cotisations supplémentaires, ou baisses d'impôt auxquelles on renonce&nbsp;;
- **les dépenses et les prestations** — ce qui est réduit, gelé ou reporté pour dégager la marge&nbsp;;
- **l'inflation**, qui allège le poids réel de la dette et en reporte une partie sur les détenteurs de créances et de revenus mal indexés, selon leurs contrats&nbsp;;
- **la restructuration**, cas extrême où la perte revient aux porteurs des titres.

Le refinancement, lui, reporte une échéance&nbsp;; il ne désigne à lui seul aucun perdant. Et en face de ces coûts se trouve ce que la dette a financé&nbsp;: les bénéfices, présents et futurs, de la dépense publique entrent dans le bilan au même titre que la charge.

{{< figure-svg fichier="qui-paie-mecanismes" alt="Schéma sans quantités : le service de la dette mène, par des flèches d'égale épaisseur, à quatre canaux possibles — prélèvements, dépenses et prestations, inflation, restructuration — ; le refinancement reporte l'échéance ; en regard, ce que la dette a financé." >}}Schéma de mécanismes possibles&nbsp;: aucun poids relatif ni effet causal n'y est mesuré.{{< /figure-svg >}}
{{< fig-actions id="mecanismes" >}}

## Les générations futures — ce dont elles héritent

La dette convertit une dépense présente en engagements futurs, et ceux qui les honoreront n'ont pas voté l'emprunt. Mais ils héritent aussi de ce qu'il a financé — infrastructures, formation, recherche, patrimoine public — et d'une partie des titres eux-mêmes, que leurs parents détiennent directement ou par l'assurance-vie. Le transfert net dépend donc de l'usage&nbsp;: une dette qui finance une consommation courante sans contrepartie durable leur transmet surtout un coût&nbsp;; un investissement dont ils profiteront peut leur transmettre davantage qu'il ne coûte.

L'encours ne suffit pas à trancher, et la dette nette ne le fait pas davantage&nbsp;: celle que publie l'INSEE ne déduit que certains actifs financiers — trésorerie, prêts, titres —, pas les routes, le capital humain ni l'environnement. Ce qui vaut quel que soit l'usage, c'est que la décision se prend sans ceux qui en porteront une part. L'objection «&nbsp;on se la doit à nous-mêmes&nbsp;» et sa réponse sont développées sur la page [La dette publique est-elle un fardeau pour les générations futures&nbsp;?](/dette-publique-generations-futures/)

## Les groupes moins mobiles — une hypothèse à tester

Tous les contribuables ne sont pas égaux devant l'ajustement. Les ménages et les entreprises qui peuvent déplacer leurs revenus, leur patrimoine ou leur activité échappent plus facilement à un prélèvement que les salariés, les retraités ou les usagers qui dépendent d'un service public local. D'où l'hypothèse&nbsp;: quand l'ajustement suit la ligne de moindre résistance, il **peut** peser davantage sur ceux qui ne peuvent pas partir.

Pour la tester, il faut définir ces groupes indépendamment du résultat, préciser l'ajustement étudié — telle réforme fiscale, tel gel de prestations — et choisir une mesure de l'effort. Elle serait affaiblie par un ajustement portant surtout sur d'autres groupes, ou par des compensations accordées aux perdants identifiés&nbsp;; ces cas ne se relisent pas après coup comme des confirmations. Le canal territorial — l'État qui reporte une part de sa contrainte sur les collectivités — est examiné sur la page [Dette publique&nbsp;: pourquoi les collectivités locales sont-elles la variable d'ajustement&nbsp;?](/dette-publique-collectivites-locales/)

## Les créanciers — financer n'est pas gagner

«&nbsp;Qui détient la dette&nbsp;?&nbsp;» est la question la plus posée, et elle ne dit pas qui paie. Le créancier a avancé les fonds&nbsp;: les intérêts rémunèrent cette avance, le temps et le risque. Son **gain net** est une autre grandeur — ce qui reste une fois déduits l'inflation et ce que ce capital aurait rapporté ailleurs — et il varie selon la date d'achat et le type de titre. La détention renseigne sur la destination des intérêts, pas sur ceux qui les financent.

Pour les titres négociables de l'État, la répartition des porteurs est publiée par la Banque de France, via l'Agence France Trésor, en valeur de marché. Elle classe les porteurs par **résidence**, non par nationalité&nbsp;: un «&nbsp;non-résident&nbsp;» peut être un fonds étranger qui gère l'épargne de ménages français, et un ménage français peut détenir des titres de l'État sans le savoir, par son assurance-vie. Une part du stock détenue hors de France ne mesure pas non plus la part des intérêts versés hors de France&nbsp;: une photographie de fin de période ne donne pas un flux annuel.

## L'investissement écologique — un mécanisme à établir cas par cas

Un budget contraint par le service de la dette peut reporter les dépenses dont les bénéfices sont lointains, et l'investissement dans la transition en fait partie. Le mécanisme est plausible&nbsp;; il reste à l'établir projet par projet&nbsp;: quelle dépense a été reportée, par quelle décision, pour quel motif budgétaire. Les agrégats ne suffisent pas&nbsp;: l'investissement public total n'est pas l'investissement climatique, et la fonction «&nbsp;protection de l'environnement&nbsp;» des comptes publics ne couvre pas toute la transition. Aucun d'eux ne mesure un investissement empêché par les intérêts. Là où le mécanisme joue, il ajoute au transfert financier un transfert écologique vers les mêmes héritiers.

## Les objections qui comptent

- **La dette finance aussi des bénéfices présents.** Services, prestations et investissements financés à crédit profitent à des ménages aujourd'hui&nbsp;; une analyse qui ne compte que les coûts ne décrit que la moitié du bilan.
- **On se la doit en partie à nous-mêmes.** Une part des titres est détenue, directement ou non, par des ménages résidents&nbsp;: les intérêts qu'ils reçoivent sont aussi un revenu. Reste à savoir qui, parmi les résidents, reçoit ces intérêts et qui les finance.
- **Moins emprunter aurait aussi coûté.** Un impôt plus lourd ou une dépense abandonnée plus tôt auraient eu leurs propres perdants&nbsp;; la comparaison honnête porte sur ces alternatives, pas sur un monde sans coût.
- **Tant que la croissance dépasse le taux d'intérêt, la dette peut se stabiliser.** L'argument est sérieux et il a souvent été vrai&nbsp;: sous cette condition, le ratio de dette peut rester stable même avec un déficit hors intérêts, pourvu que ce déficit primaire reste sous un seuil qui dépend de l'écart entre les deux taux et du niveau de la dette. Au-delà, le ratio monte malgré tout. Et même stable, une dette se sert chaque année&nbsp;: la question de la répartition demeure.

## Ce que ces données ne permettent pas d'établir

Aucune statistique ne dit, à elle seule, qui supporte au bout du compte la charge de la dette française&nbsp;: l'incidence finale d'un euro d'intérêts dépend des ajustements choisis année après année, et de l'alternative à laquelle on les compare. Une répartition actuelle des impôts et des prestations décrit qui contribue et qui reçoit aujourd'hui&nbsp;; elle n'identifie pas les payeurs futurs de la dette. Une moyenne par ménage n'est pas une facture individuelle&nbsp;: elle est compatible avec une dispersion considérable, et une personne qui reçoit beaucoup de prestations peut perdre à une réforme précise.

Ce qui peut s'établir, c'est l'effet d'une décision déterminée — une réforme, un gel, un report — sur des groupes définis d'avance. C'est à ce niveau que la question «&nbsp;qui paie&nbsp;?&nbsp;» reçoit des réponses vérifiables.

{{< reutiliser figures="figures_qui_paie" jeu="qui_paie_donnees" sources="Insee et Banque de France via l'AFT" donnees="Détention de la dette publique (registre du livre, sources INSEE et Banque de France) et comptes nationaux distribués 2023 de l'Insee, avec leurs périodes, unités et conventions." >}}
La répartition des effets de la dette publique dépend de ce qu'elle finance, de la manière dont elle est financée et des ajustements choisis pour la servir&nbsp;; certaines configurations peuvent reporter des coûts sur des groupes moins capables de les éviter. Les données disponibles montrent qui emprunte, qui détient les titres de l'État et qui contribue ou reçoit aujourd'hui — pas qui supportera la charge finale. Une perte ne s'attribue qu'à une décision déterminée, comparée à son alternative.
{{< /reutiliser >}}

## D'où vient cette analyse

{{< canonical-definition >}}

Appliquée aux finances publiques, cette hypothèse est formalisée dans le working paper [AWP-03 — *Dette publique et anthropie&nbsp;: qui paie vraiment le désordre&nbsp;?*](/awp/awp-03/) (DOI&nbsp;: 10.5281/zenodo.19268769, PDF en accès libre).

{{< appel-livre slug="dette-publique-qui-paie-vraiment" >}}
Cette page pose la méthode&nbsp;: quatre rôles, quatre canaux, et ce qu'il faudrait observer pour conclure. Le livre la déploie sur le cas français — le transfert dans le temps, les créanciers, les services publics — et la prolonge par des scénarios 2025-2035.
{{< /appel-livre >}}
