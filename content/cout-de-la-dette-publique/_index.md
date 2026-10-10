---
title: "Combien coûte la dette publique ?"
description: "Combien coûte la dette publique ? {dette.interets_mdeur} milliards d'euros d'intérêts en {dette.interets_annee}, {dette.interets_sur_recettes_pct} % des recettes publiques : pourquoi la facture a baissé vingt-cinq ans, puis remonte."
chapo: "Pendant vingt-cinq ans, la dette publique a doublé en part de PIB pendant que sa facture baissait. Depuis 2022, le ciseau se referme : {dette.interets_mdeur} milliards d'euros d'intérêts en {dette.interets_annee}, {dette.interets_sur_recettes_pct} % des recettes publiques. Chiffres officiels de l'INSEE et d'Eurostat, actualisés à chaque publication."
date: 2026-08-15
lastmod: 2026-09-30
donnees: [dette_officielle]
og_title: "Combien coûte la dette publique ? — données officielles à jour — S. Lalut"
og_image: "images/og-cout-dette.jpg"
og_image_alt: "Carte de partage : « Combien coûte la dette publique ? » — encours de dette et charge d'intérêts en % du PIB, 1995-2025, sources INSEE et Eurostat."
# Émet le JSON-LD Dataset (partials/schema-dataset-dette.html) : la page ne
# fait pas que citer des chiffres, elle publie une compilation réutilisable.
dataset_dette: true
faq:
  - question: "Combien la dette publique coûte-t-elle chaque année à la France ?"
    answer: "La mesure la plus directe est la charge d'intérêts versés par les administrations publiques : {dette.interets_mdeur} milliards d'euros en {dette.interets_annee}, soit {dette.interets_pct_pib} % du PIB et {dette.interets_sur_recettes_pct} % de l'ensemble des recettes publiques (Eurostat, série D41PAY). Cette charge a augmenté de {dette.interets_hausse_pct} % depuis le creux exceptionnel de {dette.interets_creux_annee} ({dette.interets_creux_mdeur} milliards) — et de {dette.interets_hausse_2019_pct} % depuis 2019, avant la rupture sanitaire : les deux bases mènent à la même conclusion."
  - question: "Quel est le montant de la dette publique française ?"
    answer: "{dette.dette_mdeur} milliards d'euros au {dette.dette_periode}, soit {dette.dette_pct_pib} % du PIB (INSEE, dette de Maastricht des administrations publiques). Sur la série INSEE disponible (depuis 1995), le maximum du ratio dette/PIB est atteint au {dette.dette_pic_periode} ({dette.dette_pic_pct_pib} %)."
  - question: "La charge de la dette dépasse-t-elle le budget de la justice ?"
    answer: "Oui, largement. En {dette.equiv_annee} — dernier millésime où toutes les séries sont comparables —, les administrations publiques ont versé {dette.interets_equiv_mdeur} milliards d'euros d'intérêts, contre {dette.justice_mdeur} milliards de dépenses publiques pour les tribunaux, au sens de la classification fonctionnelle européenne COFOG (poste GF0303) — et non du budget total de la mission Justice : environ {dette.ratio_interets_justice} fois plus. Les intérêts dépassent même l'ensemble du poste « ordre et sécurité publics » ({dette.ordre_mdeur} milliards, GF03)."
  - question: "Pourquoi la charge de la dette augmente-t-elle si vite alors que la dette montait déjà avant ?"
    answer: "Parce que le coût moyen du stock et son volume ont divergé pendant environ vingt-cinq ans : le taux implicite de la dette — les intérêts d'une année rapportés à l'encours en début d'année — est passé d'environ {dette.taux_apparent_premier} % en {dette.taux_apparent_premier_annee} à {dette.taux_apparent_creux} % en {dette.taux_apparent_creux_annee}, pendant que l'encours doublait en part de PIB. Depuis 2021, ce coût moyen remonte, avec une accélération en 2022 ({dette.taux_apparent_dernier} % en {dette.taux_apparent_dernier_annee}) et frappe un encours deux fois plus lourd ; sa transmission est retardée — la charge peut continuer de monter même si les taux de marché se stabilisent, à mesure que la dette ancienne se refinance. Dans le cadre de l'anthropie, cette séquence peut être lue comme un coût déplacé dans le temps qui finit par revenir (AWP-07, la boucle anthropique)."
  - question: "La hausse des intérêts a-t-elle déjà fait baisser les dépenses de santé ou d'éducation ?"
    answer: "Pas dans les agrégats observés : en {dette.equiv_annee}, les dépenses publiques de santé ({dette.sante_mdeur} milliards d'euros) et d'enseignement ({dette.education_mdeur} milliards) sont stables ou en hausse, en euros comme en part de PIB. Cela ne veut pas dire qu'il n'y a pas eu d'éviction : un budget qui passe de 100 à 105 au lieu de 110 n'a pas baissé, et a pourtant été évincé. Ces séries ne permettent ni d'attribuer leur trajectoire à la dette, ni d'exclure qu'elles auraient été plus élevées sans la contrainte d'intérêts. Si les services semblent pourtant manquer de moyens, l'explication la plus courante — plausible, mais que ces séries ne démontrent pas — est que leurs coûts et leurs besoins (salaires, vieillissement, progrès médical, judiciarisation) croîtraient plus vite que le PIB : la stabilité d'un budget en part de PIB ne garantirait alors pas un service rendu stable, sans que ce budget baisse pour autant. L'établir exigerait des données que cette page ne porte pas : inflation sectorielle, productivité, démographie, volumes produits. Ces données n'attribuent pas cet écart à la dette ; ce qu'elles établissent, c'est qu'à recettes et besoin de financement donnés, la charge d'intérêts pince la marge qui permettrait de le combler. La question devient de savoir qui absorbera l'ajustement — impôts supplémentaires, réduction d’autres dépenses, déficit accru, inflation, ou générations futures. C'est l'objet de la page « Qui paie vraiment la dette publique ? » et des scénarios 2025-2035 du livre."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 10
  nature: "Séries officielles (INSEE, Eurostat) et calculs de l'auteur"
  accueil: 1
---

{{< dossier-dette volet="1" >}}

{{< reutiliser-ancre >}}

À la question **«&nbsp;combien coûte la dette publique&nbsp;?&nbsp;»**, le chiffre le plus direct n'est pas l'encours, mais les **intérêts versés chaque année**&nbsp;: **{{< dette-val "interets_mdeur" >}}&nbsp;milliards d'euros en {{< dette-val "interets_annee" >}}**, soit {{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB et **{{< dette-val "interets_sur_recettes_pct" >}}&nbsp;% des recettes publiques** (Eurostat, `D41PAY`).

Il s'agit d'une charge **brute**, couvrant l'ensemble des administrations publiques — État, collectivités locales et sécurité sociale — et enregistrée l'année où les intérêts courent. La même convention est conservée sur toute la page afin de comparer des grandeurs de périmètre identique.

<details class="repli"><summary>L'INSEE affiche un montant voisin&nbsp;: deux conventions (intérêts avec ou hors correction SIFIM), pas deux mesures contradictoires</summary>

Les comptes de l'INSEE affichent pour {{< dette-val "interets_annee" >}} un montant légèrement différent, notamment parce qu'ils présentent les intérêts hors correction dite SIFIM (services d'intermédiation financière indirectement mesurés). Deux **conventions voisines**, donc, et non deux mesures contradictoires.

</details>

## Le ciseau&nbsp;: vingt-cinq ans de compensation, puis le retournement

<figure class="figure-ciseau">
  <img src="/img/ciseau-dette-interets.svg" alt="Deux courbes en pourcentage du PIB : en haut, la dette publique française monte presque continûment de 1995 à aujourd'hui ; en bas, les intérêts versés par les administrations publiques baissent jusqu'en 2020, puis remontent fortement après 2022." width="720" height="528" loading="lazy">
  <figcaption>Dette publique ({{< dette-val "dette_periode" >}}&nbsp;: {{< dette-val "dette_pct_pib" >}}&nbsp;% du PIB, INSEE, trimestriel) et intérêts versés par les administrations publiques ({{< dette-val "interets_annee" >}}&nbsp;: {{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB, Eurostat, annuel). Deux échelles distinctes, une même unité&nbsp;: le pourcentage du PIB.</figcaption>
</figure>
{{< fig-actions id="ciseau" >}}

**L'observation.** De 1995 au tournant des années 2020, les deux courbes font ciseau&nbsp;: l'encours passe de {{< dette-val "dette_1995_pct_pib" >}}&nbsp;% à plus de 100&nbsp;% du PIB, pendant que la charge d'intérêts **descend** de {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% à {{< dette-val "interets_creux_pct_pib" >}}&nbsp;% ({{< dette-val "interets_creux_annee" >}}, {{< dette-val "interets_creux_mdeur" >}}&nbsp;Md€). Pendant plus de deux décennies, la baisse du coût moyen de financement a permis à la charge de diminuer en proportion du PIB malgré la hausse continue de l'encours.

<div class="resultat-phrase">

**Le résultat en une phrase.** De 1995 à {{< dette-val "interets_creux_annee" >}}, la dette est passée de {{< dette-val "dette_1995_pct_pib" >}}&nbsp;% à plus de 100&nbsp;% du PIB pendant que sa charge d'intérêts tombait de {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% à {{< dette-val "interets_creux_pct_pib" >}}&nbsp;% du PIB&nbsp;: la baisse du coût moyen du stock compensait la hausse de l'encours. Depuis 2022, les deux forces jouent de nouveau dans le même sens.

</div>

<div class="equation" role="group" aria-label="La chaîne qui va du déficit à la charge d'intérêts">
  <p class="equation__titre">La chaîne qui fait la facture</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>le déficit</b><small>ce qui s'emprunte net chaque année</small></span>
    <span class="equation__op" aria-label="alimente">→</span>
    <span class="equation__terme"><b>le stock</b><small>la dette accumulée, sans cesse refinancée</small></span>
    <span class="equation__op" aria-label="multiplié par">×</span>
    <span class="equation__terme"><b>son coût moyen</b><small>le taux implicite</small></span>
    <span class="equation__op" aria-label="égale">=</span>
    <span class="equation__terme equation__terme--resultat"><b>la charge d'intérêts</b><small>payée chaque année</small></span>
  </div>
  <p class="equation__exacte">Le coût moyen ne suit les taux de marché qu'au fil des refinancements&nbsp;: c'est le retard de transmission.</p>
</div>

<details class="repli"><summary>La chaîne en quatre maillons&nbsp;: le déficit fait le stock, le stock a un coût moyen, ce coût se paie chaque année et suit les taux de marché avec retard</summary>

Pour lire ces chiffres sans être spécialiste, la chaîne tient en quatre maillons&nbsp;: l'État refinance en permanence les titres qui arrivent à échéance, si bien qu'emprunter beaucoup ne fait pas grossir le **stock** par soi-même — le montant des émissions brutes ne mesure donc pas l'augmentation de la dette. Ce qui la fait grossir, c'est le **déficit**, ce qu'il emprunte net, augmenté des ajustements entre flux et stock. Ce stock a un **prix moyen** — le taux auquel il a été emprunté au fil du temps. Ce prix se paie chaque année&nbsp;: ce sont les **intérêts**, une obligation déjà contractée — on ne la met pas en balance comme une dépense nouvelle, et, à recettes et besoin de financement donnés, elle réduit d'autant la marge des arbitrages&nbsp;; si cette marge n'est pas réduite, c'est le besoin de financement qui augmente. Et quand les taux de marché remontent, le prix moyen suit avec retard — la facture annuelle grossit, et la question cesse d'être «&nbsp;combien&nbsp;» pour devenir «&nbsp;**qui la paiera**&nbsp;».

</details>

{{< figure-svg fichier="charge-interets-mdeur" alt="Une courbe en milliards d'euros courants, de 1995 à 2025 : la charge d'intérêts oscille autour de 45 à 55 milliards, descend jusqu'à un creux de 29,7 milliards en 2020, puis remonte fortement jusqu'à 66,6 milliards ; un prolongement en pointillés porte la prévision du Gouvernement." >}}Eurostat, intérêts versés par les administrations publiques. En euros courants, non corrigés de l'inflation.{{< /figure-svg >}}

{{< fig-actions id="charge" >}}

**La même charge, en euros.** Le pourcentage du PIB situe le poids de la dette par rapport à la richesse produite&nbsp;; le milliard mesure la charge en euros. Ni l'un ni l'autre ne dit si la dette est **soutenable**&nbsp;: cela dépend en outre de la croissance, du taux d'intérêt et du solde primaire — le déficit hors intérêts. En euros courants, la facture est passée d'un creux de {{< dette-val "interets_creux_mdeur" >}}&nbsp;milliards en {{< dette-val "interets_creux_annee" >}} à {{< dette-val "interets_mdeur" >}}&nbsp;milliards en {{< dette-val "interets_annee" >}}. Ces euros ne sont pas corrigés de l'inflation&nbsp;: une partie de la hausse est celle des prix, et c'est pourquoi la page raisonne ailleurs en part de PIB.

**Le mécanisme.** Le chaînon entre les deux courbes est le **taux implicite** de la dette — les intérêts versés une année, rapportés à l'encours en début d'année&nbsp;: un bon **indicateur du coût moyen du stock** — non sa mesure exacte, puisqu'il rapproche un flux comptable d'intérêts et un encours arrêté à une date, avec leurs écarts de périmètre, de calendrier et d'indexation. À ne pas confondre non plus avec le taux auquel la France emprunte aujourd'hui, ni avec le «&nbsp;coût apparent&nbsp;» que publie Eurostat, fondé sur la dette moyenne de l'année&nbsp;: cette page, comme la comparaison internationale, retient la dette de fin d'année précédente. Il passe d'environ {{< dette-val "taux_apparent_premier" >}}&nbsp;% en {{< dette-val "taux_apparent_premier_annee" >}} à {{< dette-val "taux_apparent_creux" >}}&nbsp;% au creux de {{< dette-val "taux_apparent_creux_annee" >}}, avant de remonter à {{< dette-val "taux_apparent_dernier" >}}&nbsp;% en {{< dette-val "taux_apparent_dernier_annee" >}}. Sa transmission est **retardée**&nbsp;: la charge d'une année rémunère un stock émis à des dates différentes — le coût moyen peut donc continuer de monter alors même que les taux de marché se stabilisent, à mesure que la dette ancienne, peu coûteuse, se refinance aux conditions nouvelles. L'asymétrie résume l'histoire&nbsp;: en 1995, un encours de {{< dette-val "dette_1995_pct_pib" >}}&nbsp;% du PIB coûtait {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% de PIB d'intérêts&nbsp;; un stock aujourd'hui deux fois plus lourd coûte encore proportionnellement moins — mais son prix moyen remonte.

<figure class="figure-ciseau">
  <img src="/img/taux-apparent-dette.svg" alt="Une courbe en pourcentage par an : le coût moyen du stock de dette publique descend de {{< dette-val "taux_apparent_premier" >}} % en {{< dette-val "taux_apparent_premier_annee" >}} à {{< dette-val "taux_apparent_creux" >}} % en {{< dette-val "taux_apparent_creux_annee" >}}, son minimum, puis remonte à {{< dette-val "taux_apparent_dernier" >}} % en {{< dette-val "taux_apparent_dernier_annee" >}}. La baisse court sur près de vingt-cinq ans, la remontée sur les dernières années." width="720" height="388" loading="lazy">
  <figcaption><strong>Taux implicite</strong>&nbsp;: intérêts versés une année rapportés à l'encours au 31&nbsp;décembre précédent — calcul sur séries Eurostat (<code>gov_10a_main</code>) et INSEE. Trois points sont étiquetés&nbsp;: le début de la série, son minimum, le dernier millésime. La série complète, année par année, est dans <a href="/dette_officielle.json">dette_officielle.json</a>.</figcaption>
</figure>
{{< fig-actions id="taux" >}}

<figure class="figure-ciseau">
  <img src="/img/taux-marche-apparent.svg" alt="Deux courbes en pourcentage par an, sur la même échelle : le taux à 10 ans et le taux implicite de la dette publique restent proches jusqu'au début des années 2010 ; ensuite le taux à 10 ans descend jusqu'à zéro puis remonte fortement, tandis que le taux implicite descend moins bas et remonte plus lentement." width="720" height="408" loading="lazy">
  <figcaption><strong>Le retard de transmission</strong>&nbsp;: le taux à 10&nbsp;ans, moyenne annuelle et repère du coût des emprunts nouveaux, et le taux implicite, coût moyen de tout le stock, sur la même échelle — séries Eurostat <code>irt_lt_mcby_a</code> et <code>gov_10a_main</code>, INSEE.</figcaption>
</figure>
{{< fig-actions id="marche" >}}

C'est la courbe qui relie les deux autres&nbsp;: elle explique comment un stock croissant a pu longtemps produire une charge décroissante. La charge ne dépend pas d'elle seule&nbsp;: elle se lit **approximativement comme le produit** de l'encours par ce coût moyen — approximativement, parce que le taux implicite est un indicateur reconstitué, non le taux réellement servi sur chaque titre. Pendant environ vingt-cinq ans, la baisse de l'un a compensé la hausse de l'autre — c'est pourquoi doubler l'encours n'a pas doublé la facture. Aujourd'hui, la hausse du coût moyen s'applique à un encours bien plus lourd.

**La lecture.** Depuis 2022 — rupture de trajectoire où convergent inflation, titres indexés et normalisation monétaire —, le ciseau se referme&nbsp;: la remontée des taux rencontre un encours devenu deux fois plus lourd, et la charge atteint {{< dette-val "interets_mdeur" >}}&nbsp;Md€ ({{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB) en {{< dette-val "interets_annee" >}} — **{{< dette-val "interets_hausse_pct" >}}&nbsp;%** de plus qu'au creux exceptionnel de {{< dette-val "interets_creux_annee" >}}, et **{{< dette-val "interets_hausse_2019_pct" >}}&nbsp;%** de plus qu'en 2019, avant la rupture sanitaire&nbsp;: les deux bases de comparaison mènent à la même conclusion. Dans le cadre de l'anthropie, cette séquence **peut être lue** comme un déplacement temporaire du coût suivi de sa réapparition&nbsp;: déplacement, saturation, retour. Cette lecture est formalisée dans le working paper [AWP-07 — *La boucle anthropique*](/awp/awp-07/) et appliquée à la dette dans [AWP-03](/awp/awp-03/). Le working paper [AWP-09](/awp/awp-09/) en propose une mesure&nbsp;: le coût marginal du report est celui des émissions nouvelles, à comparer au coût moyen du stock, que mesure le taux implicite.

## Quel stock cette facture rémunère-t-elle&nbsp;? {#stock-remunere}

Cette facture rémunère un stock&nbsp;: l'**encours** accumulé, le chiffre que l'on cite le plus souvent.

{{< dette-chiffres live="true" historique="true" >}}
{{< fig-actions id="longue" >}}

**Ce que montre la courbe.** Depuis {{< dette-val "hist_annee_debut" >}}, la dette publique est passée de {{< dette-val "hist_pct_debut" >}}&nbsp;% à {{< dette-val "dette_pct_pib" >}}&nbsp;% du PIB&nbsp;: multipliée par {{< dette-val "hist_multiple" >}} en part de la richesse produite. La montée n'est pas régulière — sur les {{< dette-val "hist_annees_total" >}}&nbsp;années de la série annuelle, le ratio a reculé {{< dette-val "hist_annees_baisse" >}}&nbsp;fois, jamais plus de {{< dette-val "hist_plus_longue_baisse" >}}&nbsp;d'affilée. Elle procède par paliers, et deux phénomènes s'y succèdent&nbsp;: les principaux sauts **coïncident avec les crises**, puis la **persistance des déficits** empêche d'effacer le palier atteint — **dans la série observée, le ratio n'est jamais revenu à son niveau de dix ans auparavant**.

<details class="repli"><summary>Les paliers depuis {{< dette-val "hist_annee_debut" >}}&nbsp;: 30, 60, 80 puis 100&nbsp;% du PIB, franchis après les chocs pétroliers, la récession de 1993, la crise financière et la crise sanitaire</summary>

- **{{< dette-val "hist_annee_debut" >}}&nbsp;— {{< dette-val "hist_pct_debut" >}}&nbsp;%.** Trente ans de forte croissance et d'inflation ont dilué la dette d'après-guerre&nbsp;: l'État rembourse dans une monnaie qui perd de sa valeur. La dette n'est pas un sujet. Le désendettement éclair que l'on prête à l'inflation de la Libération est, lui, à réviser&nbsp;: en réintégrant les prix du marché noir, que l'indice officiel ignorait, Baubeau et Teixeira montrent que les prix ont bien plus monté pendant la guerre, et moins ensuite, qu'on ne le croyait&nbsp;; rapportée au revenu national, la dette a donc moins gonflé pendant le conflit, et moins fondu après ([*Economic History Review*, 2026](https://doi.org/10.1111/ehr.70127)).
- **{{< dette-val "hist_seuil_30_annee" >}}&nbsp;— 30&nbsp;%.** Après les deux chocs pétroliers, la croissance ralentit sans que les dépenses suivent&nbsp;: le déficit devient permanent. Le recours à l'emprunt cesse d'être occasionnel et s'installe&nbsp;— non par une décision datable, mais parce que le déficit ne se referme plus entre deux ralentissements.
- **{{< dette-val "hist_seuil_60_annee" >}}&nbsp;— 60&nbsp;%.** La récession de 1993 creuse les comptes&nbsp;; le traité de Maastricht, signé en 1992 et entré en vigueur en novembre 1993, a fait de 60&nbsp;% la valeur de référence européenne. La dette la franchit en 1996&nbsp;: la dette ne repassera en dessous que deux années, au tournant des années 2000.
- **{{< dette-val "hist_seuil_80_annee" >}}&nbsp;— 80&nbsp;%.** La crise financière fait chuter les recettes et impose des plans de soutien&nbsp;: près de vingt points de PIB en deux ans. La reprise qui suit ne les rattrape pas.
- **{{< dette-val "hist_seuil_100_annee" >}}&nbsp;— 100&nbsp;%.** L'arrêt de l'économie et le soutien aux revenus ajoutent près de dix-sept points en une seule année. La dette dépasse la taille du PIB.
- **{{< dette-val "dette_periode" >}}&nbsp;— {{< dette-val "dette_pct_pib" >}}&nbsp;%.** L'encours reste orienté à la hausse sur longue période, et son coût moyen remonte depuis 2021, avec une accélération en 2022&nbsp;: la hausse du coût moyen se combine désormais avec un encours beaucoup plus élevé&nbsp;— c'est l'objet de la suite de cette page.

</details>

Sur la série trimestrielle de l'INSEE, disponible depuis 1995, le **maximum du ratio** dette/PIB est atteint au {{< dette-val "dette_pic_periode" >}} ({{< dette-val "dette_pic_pct_pib" >}}&nbsp;%).

<details class="repli"><summary>Environ {{< interets-par-foyer >}}&nbsp;€ d'intérêts par foyer fiscal&nbsp;: une division arithmétique, ni un impôt dû ni la répartition réelle de la charge</summary>

**À l'échelle d'un foyer.** Rapportée aux {{< interets-par-foyer "foyers" >}}&nbsp;millions de foyers fiscaux ({{< interets-par-foyer "periode" >}}, DGFiP), la charge d'intérêts de {{< dette-val "interets_annee" >}} représente environ {{< interets-par-foyer >}}&nbsp;€ par foyer. C'est une division uniforme théorique de la charge totale&nbsp;: ce montant n'est pas un impôt dû par chaque foyer, et il ne dit pas qui la supporte — ménages, entreprises et non-résidents contribuent aux recettes publiques dans des proportions que ce calcul ignore. Qui la supporte est [l'objet du second volet](/qui-paie-la-dette-publique/).

</details>

## Ce que la facture ne dit pas&nbsp;: la dette augmente-t-elle&nbsp;? {#ce-que-la-facture-ne-dit-pas-la-dette-augmente-t-elle}

**La réponse détaillée est dans le premier volet du dossier**, [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)&nbsp;: de {{< dyn-val "annee_depart" >}} à {{< dyn-val "annee_fin" >}}, les intérêts et la croissance du PIB nominal se sont presque annulés, et la hausse de la dette tient pour l'essentiel aux déficits primaires ({{< dyn-val "deficits_primaires" >}} points sur {{< dyn-val "hausse" >}}). Ce qui suit en résume le principe.

Tout ce qui précède répond à «&nbsp;combien coûte&nbsp;». C'est une autre question que de savoir si le ratio de dette monte, se stabilise ou recule&nbsp;— et la réponse ne se lit dans aucun des chiffres ci-dessus. Elle dépend de trois termes, dont cette page n'en mesure qu'un et demi.

<details class="repli"><summary>Trois termes font bouger le ratio&nbsp;: l'écart entre coût moyen et croissance, le solde primaire, les ajustements flux-stock — cette page n'en mesure qu'une partie</summary>

- **L'effet «&nbsp;boule de neige&nbsp;»**&nbsp;: la dette héritée, multipliée par l'écart entre son **coût moyen** et la **croissance nominale** du PIB. Tant que la croissance nominale dépasse le coût moyen du stock, ce terme tire le ratio vers le bas **sans le moindre effort budgétaire**&nbsp;; quand l'écart s'inverse, il le pousse vers le haut. Le ratio lui-même ne baisse que si ce terme l'emporte sur le déficit primaire. C'est le terme que le retournement du taux implicite déplace, et c'est pourquoi ce retournement compte au-delà de la facture qu'il produit.
- **Le solde primaire**&nbsp;: le solde des comptes publics **hors intérêts**. Un excédent primaire fait reculer le ratio, un déficit primaire le pousse. Deux pays peuvent porter la même charge d'intérêts et diverger entièrement par ce seul terme.
- **Les ajustements flux-stock**&nbsp;: ce qui fait bouger la dette sans passer par le déficit — trésorerie, acquisitions et cessions d'actifs, écarts de valorisation. Ils expliquent qu'un encours puisse croître plus vite, ou moins vite, que le déficit de l'année.

</details>

**Ce que cette page mesure, et ce qu'elle ne mesure pas.** Elle publie le ratio de dette et le coût moyen du stock&nbsp;: la moitié du premier terme. Elle ne publie ni la croissance nominale, ni le solde primaire, ni les ajustements flux-stock. **Elle ne permet donc pas de conclure que la dette s'auto-stabilise, ni l'inverse.** Ce qu'elle établit est plus étroit, et plus sûr&nbsp;: le coût moyen du stock remonte, ce qui déplace le premier terme dans le sens défavorable, à croissance nominale inchangée.

C'est aussi la réponse à une question que le chiffre appelle naturellement&nbsp;— «&nbsp;{{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB d'intérêts, est-ce beaucoup&nbsp;?&nbsp;». Beaucoup ou peu **par rapport à quoi**&nbsp;: à la croissance qui vient, au solde primaire que l'on tient, et à ce que la dette a financé. Ce chiffre seul ne tranche pas, et aucun seuil ne le fait à sa place.

<h2 id="masses-comparees">{{< dette-val "interets_equiv_mdeur" >}}&nbsp;milliards d’euros d’intérêts en {{< dette-val "equiv_annee" >}}&nbsp;: quel ordre de grandeur&nbsp;?</h2>

Tout ce qui suit porte sur **le même millésime**, {{< dette-val "equiv_annee" >}}&nbsp;— la dernière année où toutes les séries existent, la ventilation par fonction paraissant avec près de deux ans de retard. Cette année-là, les intérêts versés ({{< dette-val "interets_equiv_mdeur" >}}&nbsp;Md€) ont représenté **{{< dette-val "interets_sur_recettes_equiv_pct" >}}&nbsp;% de l'ensemble des recettes publiques** ({{< dette-val "recettes_equiv_mdeur" >}}&nbsp;Md€, Eurostat). À masses comparées, sur ce millésime&nbsp;:

- **Justice (tribunaux)&nbsp;: {{< dette-val "justice_mdeur" >}}&nbsp;Md€** — au sens de la classification fonctionnelle européenne COFOG (poste GF0303, tribunaux), et non du budget total de la mission Justice — la charge d'intérêts en représente environ **{{< dette-val "ratio_interets_justice" >}}&nbsp;fois** le montant&nbsp;;
- **Ordre et sécurité publics, poste entier (GF03)&nbsp;: {{< dette-val "ordre_mdeur" >}}&nbsp;Md€** — les intérêts dépassent le poste complet&nbsp;;
- **Enseignement (GF09)&nbsp;: {{< dette-val "education_mdeur" >}}&nbsp;Md€** — toute la dépense publique d'enseignement, toutes administrations et tous niveaux confondus, et non la seule mission «&nbsp;Enseignement scolaire&nbsp;» du budget de l'État, environ deux fois et demie plus petite — les intérêts en représentent environ {{< dette-val "pct_interets_education" >}}&nbsp;%&nbsp;;
- **Santé (GF07)&nbsp;: {{< dette-val "sante_mdeur" >}}&nbsp;Md€** — les intérêts en représentent environ {{< dette-val "pct_interets_sante" >}}&nbsp;%.

{{< figure-svg fichier="masses-comparees" alt="Quatre courbes en milliards d'euros courants, de 1995 à 2024 : la santé et l'enseignement montent régulièrement et restent les plus élevés ; la charge d'intérêts, longtemps stable puis en baisse, remonte après 2020 et repasse au-dessus du poste « ordre et sécurité »." >}}Eurostat, intérêts versés et dépenses des administrations par fonction. Toutes les séries s'arrêtent au même millésime.{{< /figure-svg >}}

{{< fig-actions id="masses" >}}

**Ce que la courbe ajoute au tableau.** Les quatre montants ci-dessus sont une photographie&nbsp;; leur trajectoire dit autre chose. La charge d'intérêts est restée, pendant vingt ans, sous le poste «&nbsp;ordre et sécurité&nbsp;» tout entier — police, gendarmerie, justice, secours. Elle est repassée au-dessus. La santé et l'enseignement, eux, s'en éloignent&nbsp;: ce sont des masses d'un autre ordre.

**Une lecture trompeuse guette ici, et il faut l'écarter.** Sur l'ensemble de la période, ces trois budgets ont crû **plus vite** que la charge d'intérêts&nbsp;: la baisse des taux a longtemps allégé la facture pendant que la dépense publique progressait. Le rapport s'inverse depuis le creux de {{< dette-val "creux_ref_annee" >}}&nbsp;: **+{{< dette-val "croiss_interets_depuis_creux_pct" >}}&nbsp;% pour les intérêts**, contre au plus +{{< dette-val "croiss_fonctions_depuis_creux_pct" >}}&nbsp;% pour ces trois fonctions. Deux choses sont donc vraies en même temps, et cette page ne choisit pas entre elles&nbsp;: la dette **n'a pas fait baisser** ces budgets, et son coût est devenu, depuis le creux, la dépense qui progresse le plus vite.

<details class="repli"><summary>Précaution&nbsp;: ces équivalences comparent des masses, pas des causes — aucun euro d'intérêts n'est réputé pris à la santé, à l'école ou à la justice</summary>

Une précaution de lecture enfin&nbsp;: les intérêts sont une **nature** de dépense, les trois autres des **fonctions**. Ce n'est pas le même découpage — les intérêts figurent d'ailleurs dans la fonction «&nbsp;services publics généraux&nbsp;» — et la comparaison ne dit pas qu'un euro d'intérêts a été pris à l'un de ces budgets.

Ces équivalences comparent des masses, pas des causes&nbsp;: elles disent l'ordre de grandeur de ce que le service de la dette pèse, chaque année, rapporté à la ressource publique — un poids, pas une part prélevée sur un autre budget.

</details>

## Ce que les données ne montrent pas

Les agrégats sont formels sur un point&nbsp;: **les dépenses observées de santé et d'enseignement n'ont pas baissé** — en {{< dette-val "equiv_annee" >}}, les deux postes sont stables ou en hausse, en euros comme en part de PIB. Quiconque affirme que la dette a «&nbsp;déjà fait baisser&nbsp;» ces budgets dit plus que les données. Mais l'inverse ne se déduit pas davantage&nbsp;: ces séries ne permettent **ni d'attribuer leur trajectoire à la dette, ni d'exclure qu'elles auraient été plus élevées** sans la contrainte d'intérêts. Un budget qui passe de 100 à 105 au lieu de 110 n'a pas baissé, et a pourtant été évincé. Sans contrefactuel, pas de causalité — dans un sens comme dans l'autre.

<details class="repli"><summary>Budgets en hausse, services sous tension&nbsp;: une explication plausible (coûts salariaux, effet Baumol, besoins croissants) que ces séries ne démontrent pas</summary>

D'où un paradoxe apparent&nbsp;: si les budgets montent, pourquoi l'hôpital, l'école ou les tribunaux semblent-ils manquer de moyens&nbsp;? L'explication la plus courante — **plausible, mais que les séries de cette page ne démontrent pas** — tient en deux mécanismes classiques. Un service public est d'abord fait de personnes&nbsp;: ses coûts suivent les salaires, pas les gains de productivité des machines (l'effet Baumol, classique en économie des services — son ampleur varie selon les secteurs). Et la demande de certains d'entre eux croîtrait plus vite que le PIB&nbsp;: vieillissement et progrès médical coûteux en santé, judiciarisation en justice. Si ces deux mécanismes jouent, la stabilité d'un poste en part de PIB **ne garantit pas** la stabilité du volume ni de la qualité du service rendu. Établir qu'il a effectivement baissé demanderait ce que cette page ne mesure pas&nbsp;: inflation sectorielle, salaires, productivité, démographie, et volumes réellement produits. **La dégradation ressentie et la hausse des agrégats ne sont donc pas nécessairement contradictoires&nbsp;: les deux peuvent coexister si l'écart entre besoins et ressources se creuse.**

</details>

Ces données n'attribuent pas cet écart à la dette&nbsp;; ce qu'elles établissent, c'est qu'à recettes et besoin de financement donnés, la charge d'intérêts **pince la marge qui permettrait de le combler**&nbsp;: les {{< dette-val "interets_mdeur" >}}&nbsp;milliards d'intérêts versés en {{< dette-val "interets_annee" >}} réduisent chaque année l'espace budgétaire disponible pour ce rattrapage, toutes choses égales par ailleurs — ce n'est pas la même chose que de dire qu'ils manquent euro pour euro à la santé ou à l'école. La question que posent les données n'est donc pas «&nbsp;les budgets baissent-ils&nbsp;?&nbsp;» mais «&nbsp;**qui absorbera l'ajustement** à mesure que le service de la dette monte&nbsp;»&nbsp;: impôts supplémentaires, réduction d’autres dépenses, déficit accru, inflation, ou générations futures. C'est précisément l'objet de la page [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/) — et des scénarios 2025-2035 du livre [*Dette Publique&nbsp;: Qui paie vraiment&nbsp;?*](/livres/dette-publique-qui-paie-vraiment/) (2025, 225&nbsp;p.).

{{< confrontation-recherche verifie="2026-09-30" publie="non" resume="la maturité de la dette et l'effet Baumol sont retrouvés comme mécanismes&nbsp;; « sans effort » et l'absence d'éviction sont mis en danger" >}}
**Mesuré ici.** La charge d'intérêts, le taux implicite et son écart au taux à 10&nbsp;ans, pour la France depuis 1995&nbsp;: des séries officielles recalculées. La littérature éprouve les lectures que la page en tire, pas ces chiffres.

**Cohérent avec.** La maturité règle le moment où les taux atteignent l'État&nbsp;: aux États-Unis, dans les années 1970, une dette raccourcie par la loi a empêché le Trésor de profiter pleinement des taux réels négatifs (Hall et Sargent). Aucun seuil ne tranche&nbsp;: Blanchard décrit des équilibres multiples sur une large plage de dette et juge la maturité et la règle budgétaire probablement plus importantes que le niveau&nbsp;; Barro, dans une contribution ultérieure au même débat, montre que le signe de «&nbsp;taux moins croissance&nbsp;» dépend de la définition du taux. Le mécanisme de Baumol est observable dans les branches marchandes américaines à faible croissance de productivité, où les prix relatifs montent et où les salaires suivent l'économie d'ensemble (Nordhaus)&nbsp;; son application aux services publics reste à établir. Dans l'échantillon de Breunig et Busemeyer — 21&nbsp;pays de l'OCDE, dont la France, de 1979 à 2003 —, une charge d'intérêts plus lourde va de pair avec un recul d'environ 2&nbsp;points de la part de l'investissement public parmi les trois postes étudiés.

**Mis en danger par.** L'idée qu'un écart favorable entre croissance et taux fasse baisser le ratio «&nbsp;sans effort&nbsp;»&nbsp;: Blanchard calcule la baisse du ratio américain sous l'hypothèse d'un solde primaire nul, et la chute de la dette fédérale détenue par le public, en valeur de marché, de 1945 à 1974, doit à peu près autant aux excédents primaires qu'à la croissance (Hall et Sargent) — d'où la précision de la page. L'idée que l'absence de baisse des budgets de santé et d'enseignement écarte l'éviction&nbsp;: Breunig et Busemeyer trouvent, dans leur échantillon, l'investissement public particulièrement exposé, et la page ne le suit pas. La lecture de la charge comme coût économique&nbsp;: la mesure en valeur de marché de Hall et Sargent incorpore des revalorisations du stock que la série des intérêts payés ne saisit pas&nbsp;; le retard que décrit la page est celui de la facture budgétaire.

**Non établi.** L'effet Baumol dans les services publics eux-mêmes&nbsp;: Nordhaus note que la production de la santé et de l'enseignement est mesurée par leurs intrants. La rupture de 2022&nbsp;: aucun des cinq textes examinés n'utilise de données postérieures à 2019, et aucun ne porte sur la France seule.

**Références lues**

- Blanchard, O., «&nbsp;Public Debt and Low Interest Rates&nbsp;», document de travail PIIE 19-4, 2019 (publié dans l'*American Economic Review*, 109(4), 2019).
- Barro, R. J., «&nbsp;r Minus g&nbsp;», document de travail NBER 28002, 2020, révisé en 2021.
- Hall, G. J. et Sargent, T. J., «&nbsp;Interest Rate Risk and Other Determinants of Post-WWII U.S. Government Debt/GDP Dynamics&nbsp;», document de travail NBER 15702, 2010 (publié dans l'*American Economic Journal: Macroeconomics*, 3(3), 2011).
- Nordhaus, W. D., «&nbsp;Baumol's Diseases: A Macroeconomic Perspective&nbsp;», document de travail NBER 12218, 2006.
- Breunig, C. et Busemeyer, M. R. (2012), «&nbsp;Fiscal austerity and the trade-off between public investment and social spending&nbsp;», *Journal of European Public Policy*, 19(6), p.&nbsp;921-938.
{{< /confrontation-recherche >}}

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir

Pendant environ vingt-cinq ans, la facture n'a pas suivi la dette&nbsp;: la baisse du coût moyen du stock a compensé la hausse de l'encours. Son retournement accroît désormais la contrainte budgétaire.

Les {{< dette-val "interets_mdeur" >}}&nbsp;milliards d'intérêts versés en {{< dette-val "interets_annee" >}} ne se retranchent d'aucun budget en particulier&nbsp;: à recettes et besoin de financement donnés, ils réduisent la marge de tous, chaque année, avant le moindre arbitrage. C'est pourquoi la comparaison avec le budget de la justice éclaire l'ordre de grandeur sans désigner de victime.

Une conséquence mérite d'être vue d'avance&nbsp;: **stabiliser le ratio de dette ne garantirait pas, à court terme, la stabilisation de la facture**. Le coût moyen du stock suit les taux de marché avec des années de retard, à mesure que la dette ancienne, peu coûteuse, se refinance aux conditions nouvelles&nbsp;; tant que ce rattrapage court, la charge peut monter alors même que le ratio de dette cesse de croître.

**Ce que prévoit le Gouvernement.** Selon le scénario du Gouvernement présenté au Haut Conseil des finances publiques pour le projet de loi de finances pour {{< dette-val "prev_edition" >}}, la charge d'intérêts atteindrait {{< dette-val "prev_charge_n_mdeur" >}}&nbsp;Md€ en {{< dette-val "prev_n_annee" >}}, puis {{< dette-val "prev_charge_n1_mdeur" >}}&nbsp;Md€ en {{< dette-val "prev_n1_annee" >}}, soit {{< dette-val "prev_charge_n1_pct_pib" >}}&nbsp;% du PIB, tandis que la dette atteindrait {{< dette-val "prev_dette_n1_pct_pib" >}}&nbsp;% du PIB fin {{< dette-val "prev_n1_annee" >}}. Le Haut Conseil, que la loi charge d'apprécier le réalisme de ces prévisions, estime que la charge pourrait dépasser ce montant si l'inflation ou les taux montaient encore. Un repère permet de mesurer la révision de la trajectoire&nbsp;: le Haut Conseil relève que la prévision de dette pour {{< dette-val "prev_n1_annee" >}} est supérieure de {{< dette-val "prev_dette_revision_pts" >}}&nbsp;points à celle du projet de loi de finances pour {{< dette-val "prev_edition_prec" >}}. Sur les figures, ces valeurs prolongent les courbes en pointillés, sous le nom de leur émetteur&nbsp;: ce sont des prévisions, non des observations.

<details class="repli"><summary>Règle&nbsp;: chaque comparaison porte sur une seule année — {{< dette-val "equiv_annee" >}} pour les masses, {{< dette-val "interets_annee" >}} pour la charge la plus récente —, jamais sur deux années mélangées</summary>

Une règle gouverne enfin toutes les comparaisons de cette page&nbsp;: **le millésime commun le plus récent, le même pour tous les termes**. La ventilation des dépenses par fonction paraissant avec près de deux ans de retard, les masses comparées portent sur {{< dette-val "equiv_annee" >}}, quand la charge d'intérêts la plus récente porte sur {{< dette-val "interets_annee" >}}. Les deux années sont dites, jamais mélangées.

</details>

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

Reste une question que ces chiffres ne tranchent pas&nbsp;: qui supporte in fine cette charge, et une partie de son coût est-elle déplacée vers d'autres&nbsp;? C'est l'objet de la page suivante.

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page chiffre la facture. Elle ne dit pas qui la règle — et c'est là que tout se joue&nbsp;: une dette ne s'efface pas, et son coût peut se déplacer — vers le contribuable, vers l'épargnant par l'inflation, vers des services publics dont la marge se resserre, vers ceux qui ne votent pas encore — selon les décisions prises pour l'ajuster. Le livre suit ces canaux un par un, chiffres officiels à l'appui, et conduit aux scénarios 2025-2035. Vous saurez, à la fin, reconnaître celui qui est en train de se réaliser.
{{< /appel-livre >}}

## D'où viennent ces chiffres

Toutes les valeurs de cette page sont **dérivées automatiquement des sources officielles** (INSEE, Eurostat), jamais recopiées, et réinterrogées chaque semaine&nbsp;; dernier relevé ayant fait bouger une valeur&nbsp;: {{< dette-val "releve_le" >}}. Données en accès libre&nbsp;: [dette_officielle.json](/dette_officielle.json), licence CC&nbsp;BY&nbsp;4.0.

<details class="repli"><summary>Séries INSEE et Eurostat, intérêts en droits constatés, taux implicite sur la dette de fin d'année précédente&nbsp;; compilation sous licence CC&nbsp;BY&nbsp;4.0</summary>

Toutes les valeurs de cette page sont **dérivées automatiquement des sources officielles**, jamais recopiées&nbsp;: dette de Maastricht trimestrielle de l'INSEE (séries 010777616 — encours en milliards d'euros — et 010777608 — % du PIB)&nbsp;; intérêts versés par les administrations publiques et recettes totales (Eurostat, `gov_10a_main`, D41PAY et TR)&nbsp;; dépenses par fonction COFOG (Eurostat, `gov_10a_exp`)&nbsp;; taux implicite calculé comme intérêts de l'année rapportés à l'encours de fin d'année précédente. La charge d'intérêts retenue est la série `D41PAY` d'Eurostat, enregistrée en droits constatés — rattachée à l'année où elle court, non à la date de paiement — et portant sur le même ensemble, toutes administrations publiques, que les recettes auxquelles elle est rapportée&nbsp;; les comptes des administrations publiques de l'INSEE présentent les intérêts hors correction SIFIM et affichent, pour la même année, un montant légèrement différent. Cette page tient la même convention d'un bout à l'autre, de sorte que le taux implicite, le rapport aux recettes et les comparaisons par fonction portent tous sur le même périmètre. Une seule famille de valeurs est saisie à la main&nbsp;: les prévisions du Gouvernement pour {{< dette-val "prev_n_annee" >}} et {{< dette-val "prev_n1_annee" >}}, lues dans l'[avis du Haut Conseil des finances publiques sur les projets de lois de finances pour {{< dette-val "prev_edition" >}}](https://www.hcfp.fr/liste-avis/avis-ndeg2026-5-lois-de-finances-2027) (paragraphes 113 et 115), qui les rapporte&nbsp;; elles ne sont pas soustraites de l'observation d'Eurostat pour 2025&nbsp;: la valeur 2025 sous-jacente à la comparaison du Haut Conseil n'a pas été réconciliée avec la série d'Eurostat utilisée sur cette page. Les séries officielles sont réinterrogées chaque semaine&nbsp;; la date ci-après ne change que lorsqu'une publication officielle modifie un chiffre — dernier relevé ayant fait bouger une valeur&nbsp;: {{< dette-val "releve_le" >}}. Les données consolidées sont publiées en accès libre&nbsp;: [dette_officielle.json](/dette_officielle.json), sous licence [CC&nbsp;BY&nbsp;4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) — réutilisation libre, y compris commerciale, à la seule condition de citer la source. Les séries brutes appartiennent à l'INSEE et à Eurostat&nbsp;; ce qui est mis sous licence ici, c'est la compilation&nbsp;: l'assemblage des séries, les grandeurs dérivées (taux implicite, ratios, équivalences à millésime unique) et leur mise en cohérence. Le compteur animé en tête de page est une extrapolation mécanique entre deux publications trimestrielles — jamais une donnée.

</details>

{{< reutiliser figures="figures_dette" jeu="dette_officielle" sources="INSEE et Eurostat" >}}
Cette page mesure ce que la dette publique coûte chaque année — la charge d'intérêts, {{< dette-val "interets_mdeur" >}}&nbsp;milliards d'euros en {{< dette-val "interets_annee" >}} — et non le montant de l'encours. Elle montre pourquoi un encours deux fois plus lourd n'a pas doublé la facture&nbsp;: le coût moyen du stock a baissé pendant trente ans, et il remonte depuis 2022 avec le retard que lui impose le refinancement. Elle compare des masses à périmètre et millésime identiques, sans établir qu'un euro d'intérêts ait été retiré à un autre budget&nbsp;: ces données ne le montrent pas.
{{< /reutiliser >}}

{{< canonical-definition >}}
