---
title: "Combien coûte la dette publique ?"
description: "Le coût de la dette ne suit pas son volume : pendant trente ans, l'encours montait pendant que la charge d'intérêts baissait — depuis 2022, les deux montent ensemble. Chiffres officiels INSEE et Eurostat actualisés, et ce que la charge d'intérêts représente face aux budgets de la justice, de l'enseignement et de la santé."
date: 2026-08-15
lastmod: 2026-08-15
faq:
  - question: "Combien la dette publique coûte-t-elle chaque année à la France ?"
    answer: "Le coût annuel effectif de la dette est sa charge d'intérêts : {dette.interets_mdeur} milliards d'euros versés en {dette.interets_annee} par les administrations publiques, soit {dette.interets_pct_pib} % du PIB (Eurostat, série D41PAY). Ce montant a augmenté de {dette.interets_hausse_pct} % depuis le point bas de {dette.interets_creux_annee} ({dette.interets_creux_mdeur} milliards d'euros)."
  - question: "Quel est le montant de la dette publique française ?"
    answer: "{dette.dette_mdeur} milliards d'euros au {dette.dette_periode}, soit {dette.dette_pct_pib} % du PIB (INSEE, dette de Maastricht des administrations publiques). En pourcentage du PIB, le pic historique reste celui du {dette.dette_pic_periode} ({dette.dette_pic_pct_pib} %) ; en euros courants, les trimestres récents établissent en revanche des records successifs."
  - question: "La charge de la dette dépasse-t-elle le budget de la justice ?"
    answer: "Oui, largement. En {dette.equiv_annee} — dernier millésime où toutes les séries sont comparables —, les administrations publiques ont versé {dette.interets_equiv_mdeur} milliards d'euros d'intérêts, contre {dette.justice_mdeur} milliards de dépenses publiques pour les tribunaux (Eurostat, fonction COFOG GF0303) : environ {dette.ratio_interets_justice} fois plus. Les intérêts dépassent même l'ensemble du poste « ordre et sécurité publics » ({dette.ordre_mdeur} milliards, GF03)."
  - question: "Pourquoi la charge de la dette augmente-t-elle si vite alors que la dette montait déjà avant ?"
    answer: "Parce que le coût et le volume ont divergé pendant trente ans : de {dette.interets_1995_pct_pib} % du PIB en 1995, la charge d'intérêts est descendue jusqu'à {dette.interets_creux_pct_pib} % en {dette.interets_creux_annee}, pendant que l'encours doublait en part de PIB — la baisse des taux anesthésiait le coût du stock. Depuis 2022, la remontée des taux frappe un encours devenu deux fois plus lourd : les deux courbes montent désormais ensemble. Ce mécanisme — déplacer un coût, le laisser s'accumuler, le voir revenir — est formalisé dans le working paper AWP-07 (la boucle anthropique)."
  - question: "La hausse des intérêts a-t-elle déjà fait baisser les dépenses de santé ou d'éducation ?"
    answer: "Non, pas dans les agrégats : en {dette.equiv_annee}, les dépenses publiques de santé ({dette.sante_mdeur} milliards d'euros) et d'enseignement ({dette.education_mdeur} milliards) sont stables ou en hausse, en euros comme en part de PIB. Le risque est prospectif : à mesure que le service de la dette monte, la question devient de savoir qui absorbera l'ajustement — impôts, services, générations futures. C'est l'objet de la page « Qui paie vraiment la dette publique ? » et des scénarios 2025-2035 du livre."
---

À la question «&nbsp;combien coûte la dette publique&nbsp;?&nbsp;», la réponse utile n'est pas le montant de l'encours — c'est ce que la France **paie chaque année** pour le porter&nbsp;: **{{< dette-val "interets_mdeur" >}}&nbsp;milliards d'euros d'intérêts en {{< dette-val "interets_annee" >}}**, soit {{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB (Eurostat). Ce coût a augmenté de **{{< dette-val "interets_hausse_pct" >}}&nbsp;%** depuis le point bas de {{< dette-val "interets_creux_annee" >}}. L'encours, lui&nbsp;:

{{< dette-chiffres >}}

## Le ciseau&nbsp;: trente ans d'anesthésie, puis le retournement

<figure class="figure-ciseau">
  <img src="/img/ciseau-dette-interets.svg" alt="Deux courbes en pourcentage du PIB : en haut, la dette publique française monte presque continûment de 1995 à aujourd'hui ; en bas, les intérêts versés par les administrations publiques baissent jusqu'en 2020, puis remontent fortement après 2022." width="720" height="480" loading="lazy">
  <figcaption>Dette publique ({{< dette-val "dette_periode" >}}&nbsp;: {{< dette-val "dette_pct_pib" >}}&nbsp;% du PIB, INSEE, trimestriel) et intérêts versés par les administrations publiques ({{< dette-val "interets_annee" >}}&nbsp;: {{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB, Eurostat, annuel). Deux échelles distinctes, une même unité&nbsp;: le pourcentage du PIB.</figcaption>
</figure>

De 1995 au tournant des années 2020, les deux courbes font ciseau&nbsp;: l'encours passe de {{< dette-val "dette_1995_pct_pib" >}}&nbsp;% à plus de 100&nbsp;% du PIB, pendant que la charge d'intérêts **descend** de {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% à {{< dette-val "interets_creux_pct_pib" >}}&nbsp;% ({{< dette-val "interets_creux_annee" >}}, {{< dette-val "interets_creux_mdeur" >}}&nbsp;Md€). Tant que les taux baissaient, emprunter davantage coûtait moins&nbsp;: le coût du stock était différé, invisible, indolore — c'est l'anesthésie.

Depuis 2022, le ciseau se referme&nbsp;: la remontée des taux rencontre un encours devenu deux fois plus lourd, et la charge remonte à {{< dette-val "interets_mdeur" >}}&nbsp;Md€ ({{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB) en {{< dette-val "interets_annee" >}}. Dans le cadre de l'anthropie, cette séquence a un nom&nbsp;: **déplacement, saturation, retour** — un coût déplacé dans le temps ne disparaît pas, il s'accumule jusqu'à revenir. Le mécanisme est formalisé dans le working paper [AWP-07 — *La boucle anthropique*](/awp/awp-07/) et appliqué à la dette dans [AWP-03](/awp/awp-03/).

Précision d'honnêteté&nbsp;: en part de PIB, le pic historique de l'encours reste celui du {{< dette-val "dette_pic_periode" >}} ({{< dette-val "dette_pic_pct_pib" >}}&nbsp;%, au cœur de la crise sanitaire)&nbsp;; c'est en euros courants que chaque trimestre récent établit un record.

## Ce que représentent {{< dette-val "interets_equiv_mdeur" >}}&nbsp;milliards d'intérêts

Comparaison à masses égales, sur le même millésime {{< dette-val "equiv_annee" >}} (dernières données Eurostat comparables, dépenses des administrations publiques par fonction)&nbsp;:

- **Justice (tribunaux, GF0303)&nbsp;: {{< dette-val "justice_mdeur" >}}&nbsp;Md€** — la charge d'intérêts en représente environ **{{< dette-val "ratio_interets_justice" >}}&nbsp;fois** le montant&nbsp;;
- **Ordre et sécurité publics, poste entier (GF03)&nbsp;: {{< dette-val "ordre_mdeur" >}}&nbsp;Md€** — les intérêts dépassent le poste complet&nbsp;;
- **Enseignement (GF09)&nbsp;: {{< dette-val "education_mdeur" >}}&nbsp;Md€** — les intérêts en représentent environ {{< dette-val "pct_interets_education" >}}&nbsp;%&nbsp;;
- **Santé (GF07)&nbsp;: {{< dette-val "sante_mdeur" >}}&nbsp;Md€** — les intérêts en représentent environ {{< dette-val "pct_interets_sante" >}}&nbsp;%.

Ces équivalences comparent des masses, pas des causes&nbsp;: elles disent l'ordre de grandeur de ce que le service de la dette prélève chaque année sur la ressource publique, avant tout choix budgétaire.

## Ce que les données ne montrent pas

L'honnêteté oblige à le dire&nbsp;: **les agrégats ne montrent aucune baisse des dépenses de santé ou d'enseignement** — en {{< dette-val "equiv_annee" >}}, les deux postes sont stables ou en hausse, en euros comme en part de PIB. Quiconque affirme que la dette a «&nbsp;déjà fait baisser&nbsp;» ces budgets dit plus que les données. Ce que les agrégats ne mesurent pas, en revanche&nbsp;: les charges différées, les arbitrages fins à l'intérieur des postes, et la question de répartition — **qui** absorbera l'ajustement à mesure que le service de la dette monte. C'est précisément l'objet de la page [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/) — et des scénarios 2025-2035 du livre [*Dette Publique&nbsp;: Qui paie vraiment&nbsp;?*](/livres/dette-publique-qui-paie-vraiment/) (2025, 224&nbsp;p.).

## D'où viennent ces chiffres

Toutes les valeurs de cette page sont **dérivées automatiquement des sources officielles**, jamais recopiées&nbsp;: dette de Maastricht trimestrielle de l'INSEE (séries 010777616 — encours en milliards d'euros — et 010777608 — % du PIB)&nbsp;; intérêts versés par les administrations publiques (Eurostat, `gov_10a_main`, D41PAY)&nbsp;; dépenses par fonction COFOG (Eurostat, `gov_10a_exp`). Dernier relevé&nbsp;: {{< dette-val "releve_le" >}}. Les données consolidées sont publiées en accès libre&nbsp;: [dette_officielle.json](/dette_officielle.json). Pour suivre l'encours en continu, le [compteur de la dette](https://projectpulse-source.github.io/dette-publique-france/) — site compagnon du livre — offre la visualisation interactive.

{{< canonical-definition >}}
