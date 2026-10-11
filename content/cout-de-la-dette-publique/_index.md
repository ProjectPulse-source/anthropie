---
title: "Combien coûte la dette publique ?"
description: "Combien coûte la dette publique ? {dette.interets_mdeur} milliards d'euros d'intérêts en {dette.interets_annee}, {dette.interets_sur_recettes_pct} % des recettes : une remontée rapide, à un niveau déjà connu en {dette.niv_pib_annee}. D'où vient la hausse, et pourquoi elle peut durer."
chapo: "En {dette.interets_annee}, les administrations publiques doivent {dette.interets_mdeur} milliards d'euros d'intérêts, {dette.interets_sur_recettes_pct} % de leurs recettes : {dette.interets_hausse_pct} % de plus qu'au creux de {dette.interets_creux_annee}. La remontée est rapide, mais le niveau n'est pas inédit : en part du PIB, la charge retrouve celui de {dette.niv_pib_annee} et reste sous celui de 1995. Pendant vingt-cinq ans, la dette a doublé en part de PIB pendant que sa facture baissait. Cette page explique pourquoi, d'où vient la remontée, et pourquoi elle peut durer même si la dette cesse d'augmenter."
date: 2026-08-15
lastmod: 2026-10-11
donnees: [dette_officielle]
og_title: "Combien coûte la dette publique ? — données officielles à jour — S. Lalut"
og_image: "images/og-cout-dette.jpg"
og_image_alt: "Carte de partage : « Combien coûte la dette publique ? » — encours de dette et charge d'intérêts en % du PIB, 1995-2025, sources INSEE et Eurostat."
# Émet le JSON-LD Dataset (partials/schema-dataset-dette.html) : la page ne
# fait pas que citer des chiffres, elle publie une compilation réutilisable.
dataset_dette: true
faq:
  - question: "Combien la dette publique coûte-t-elle chaque année à la France ?"
    answer: "La mesure la plus directe est la charge d'intérêts des administrations publiques : {dette.interets_mdeur} milliards d'euros en {dette.interets_annee}, soit {dette.interets_pct_pib} % du PIB et {dette.interets_sur_recettes_pct} % des recettes publiques (Eurostat, série D41PAY, intérêts comptés quand ils sont dus). C'est {dette.interets_hausse_pct} % de plus qu'au creux de {dette.interets_creux_annee}, et {dette.interets_hausse_2019_pct} % de plus qu'en 2019. Le niveau n'est pas inédit : en part du PIB, la charge retrouve celui de {dette.niv_pib_annee}, en part des recettes celui de {dette.niv_rec_annee}, et reste sous celui de 1995 ({dette.interets_1995_pct_pib} % du PIB). Nette des intérêts que les administrations reçoivent, elle vaut {dette.interets_nets_mdeur} milliards."
  - question: "Quel est le montant de la dette publique française ?"
    answer: "{dette.dette_mdeur} milliards d'euros au {dette.dette_periode}, soit {dette.dette_pct_pib} % du PIB (INSEE, dette de Maastricht des administrations publiques). Sur la série INSEE disponible (depuis 1995), le maximum du ratio dette/PIB est atteint au {dette.dette_pic_periode} ({dette.dette_pic_pct_pib} %)."
  - question: "Pourquoi la charge de la dette augmente-t-elle si vite ?"
    answer: "Parce que deux termes montent ensemble : la quantité de dette et son coût moyen, le taux implicite. De {dette.dec_a0} à {dette.dec_a1}, la charge augmente de {dette.dec_delta} milliards d'euros ; en décomposition comptable, {dette.dec_volume} tiennent à la hausse de l'encours et {dette.dec_taux} à celle du taux implicite (depuis 2019, avant la crise sanitaire, le partage s'inverse : {dette.dec19_volume} pour l'encours, {dette.dec19_taux} pour le taux). Le taux implicite a fait l'essentiel de son chemin en {dette.dec_saut_annee}, l'année où l'inflation a gonflé la charge des titres indexés ; depuis, c'est la hausse de l'encours qui pèse le plus. Cette décomposition ne mesure pas l'effet des taux de marché : la part du taux implicite mêle refinancement, composition de la dette et indexation."
  - question: "La charge de la dette dépasse-t-elle le budget de la justice ?"
    answer: "En {dette.equiv_annee}, dernier millésime où toutes les séries sont comparables, les intérêts ({dette.interets_equiv_mdeur} milliards d'euros) se situent entre le poste « ordre et sécurité publics » ({dette.ordre_mdeur} milliards, qu'ils dépassent) et l'enseignement ({dette.education_mdeur} milliards), loin de la santé ({dette.sante_mdeur} milliards). Les tribunaux, au sens de la classification européenne COFOG (poste GF0303, et non le budget total de la mission Justice), représentent {dette.justice_mdeur} milliards. Ces comparaisons disent un ordre de grandeur : aucun euro d'intérêts n'est réputé pris à l'un de ces postes."
  - question: "La hausse des intérêts a-t-elle déjà fait baisser les dépenses de santé ou d'éducation ?"
    answer: "Pas dans les agrégats observés : en euros, les dépenses publiques de santé ({dette.sante_mdeur} milliards d'euros en {dette.equiv_annee}) et d'enseignement ({dette.education_mdeur} milliards) ont continué de croître ; en part du PIB, elles sont au-dessus de 2019, un peu sous leur pic de la crise sanitaire, quand le PIB s'est contracté. Cela ne veut pas dire qu'il n'y a pas eu d'éviction : un budget qui passe de 100 à 105 au lieu de 110 n'a pas baissé, et a pourtant été évincé. Ces séries ne permettent ni d'attribuer leur trajectoire à la dette, ni d'exclure qu'elles auraient été plus élevées sans la contrainte d'intérêts. Ce qu'elles établissent : une charge plus élevée augmente le besoin de financement à politiques inchangées, et ses conséquences sur les dépenses, les prélèvements et le déficit dépendent ensuite des arbitrages ; qui absorbera l'ajustement est l'objet de la page « Qui paie vraiment la dette publique ? »."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  bloc: "dette"
  rang: 10
  nature: "Séries officielles (INSEE, Eurostat) et calculs de l'auteur"
  accueil: 1
---

{{< dossier-dette volet="1" >}}

{{< reutiliser-ancre >}}

À la question **«&nbsp;combien coûte la dette publique&nbsp;?&nbsp;»**, le chiffre le plus direct n'est pas l'encours, mais les **intérêts dus chaque année**&nbsp;: **{{< dette-val "interets_mdeur" >}}&nbsp;milliards d'euros en {{< dette-val "interets_annee" >}}**, soit {{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB et **{{< dette-val "interets_sur_recettes_pct" >}}&nbsp;% des recettes publiques**&nbsp;: sur 100&nbsp;euros de recettes, {{< dette-val "interets_sur_recettes_pct" >}}&nbsp;vont aux intérêts. C'est une charge **brute**, pour l'ensemble des administrations publiques (État, collectivités locales, sécurité sociale), comptée l'année où les intérêts sont dus (Eurostat, `D41PAY`).

## Le ciseau&nbsp;: vingt-cinq ans de compensation, puis le retournement

{{< figure-svg fichier="ciseau-dette-interets" alt="Deux courbes en pourcentage du PIB : en haut, la dette publique française monte presque continûment depuis 1995 ; en bas, la charge d'intérêts des administrations publiques baisse jusqu'en 2020, puis remonte." >}}Dette publique ({{< dette-val "dette_periode" >}}&nbsp;: {{< dette-val "dette_pct_pib" >}}&nbsp;% du PIB, INSEE, trimestriel) et charge d'intérêts des administrations publiques ({{< dette-val "interets_annee" >}}&nbsp;: {{< dette-val "interets_pct_pib" >}}&nbsp;% du PIB, Eurostat, annuel). Deux échelles distinctes, une même unité&nbsp;: le pourcentage du PIB.{{< /figure-svg >}}
{{< fig-actions id="ciseau" >}}

De 1995 au tournant des années 2020, les deux courbes font ciseau&nbsp;: l'encours passe de {{< dette-val "dette_1995_pct_pib" >}}&nbsp;% à plus de 100&nbsp;% du PIB, pendant que la charge d'intérêts **descend** de {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% à {{< dette-val "interets_creux_pct_pib" >}}&nbsp;% ({{< dette-val "interets_creux_annee" >}}, {{< dette-val "interets_creux_mdeur" >}}&nbsp;Md€).

<div class="resultat-phrase">

**Le résultat en une phrase.** De 1995 à {{< dette-val "interets_creux_annee" >}}, la dette est passée de {{< dette-val "dette_1995_pct_pib" >}}&nbsp;% à plus de 100&nbsp;% du PIB pendant que sa charge d'intérêts tombait de {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% à {{< dette-val "interets_creux_pct_pib" >}}&nbsp;% du PIB&nbsp;: la baisse du coût moyen du stock compensait la hausse de l'encours. Depuis, les deux forces jouent de nouveau dans le même sens.

</div>

<div class="equation" role="group" aria-label="La charge d'intérêts, produit de l'encours et de son coût moyen">
  <p class="equation__titre">Ce qui fait la facture</p>
  <div class="equation__ligne">
    <span class="equation__terme"><b>l'encours</b><small>la dette accumulée, sans cesse refinancée</small></span>
    <span class="equation__op" aria-label="multiplié par">×</span>
    <span class="equation__terme"><b>son coût moyen</b><small>le taux implicite</small></span>
    <span class="equation__op" aria-label="égale">=</span>
    <span class="equation__terme equation__terme--resultat"><b>la charge d'intérêts</b><small>due chaque année</small></span>
  </div>
  <p class="equation__exacte">L'encours grossit avec les déficits&nbsp;; le coût moyen ne suit les taux de marché qu'au fil des renouvellements de titres.</p>
</div>

Le **taux implicite** est le rapport entre les intérêts d'une année et l'encours de dette à la fin de l'année précédente. C'est un indicateur du coût moyen du stock, non le taux auquel la France emprunte aujourd'hui. Pendant vingt-cinq ans, sa baisse a compensé la hausse de l'encours&nbsp;: c'est pourquoi doubler la dette n'a pas doublé la facture.

## D'où vient la hausse depuis le creux&nbsp;: de l'encours ou du taux implicite&nbsp;? {#hausse-depuis-le-creux}

{{< figure-svg fichier="charge-encours-taux" alt="Barres empilées par année depuis 2021, en milliards d'euros : la contribution de la hausse de l'encours, en bleu, et celle du taux implicite, en orange, à la variation de la charge d'intérêts ; la barre de 2022 est dominée par le taux implicite, celles des années suivantes surtout par l'encours." >}}Décomposition comptable de la variation annuelle de la charge d'intérêts entre la hausse de l'encours (bleu) et celle du taux implicite (orange), en milliards d'euros&nbsp;; le point noir est la variation. Calcul sur séries Eurostat et INSEE.{{< /figure-svg >}}
{{< fig-actions id="decomp" >}}

De {{< dette-val "dec_a0" >}} à {{< dette-val "dec_a1" >}}, la charge d'intérêts augmente de **{{< dette-val "dec_delta" >}}&nbsp;milliards d'euros**. Puisqu'elle est le produit de l'encours et du taux implicite, sa hausse se décompose en deux parts&nbsp;: **{{< dette-val "dec_volume" >}}&nbsp;milliards tiennent à la hausse de l'encours, {{< dette-val "dec_taux" >}} à celle du taux implicite**, soit {{< dette-val "dec_part_taux_pct" >}}&nbsp;% de la hausse. Ce second chiffre mesure la hausse du coût moyen du stock, non l'effet des taux de marché&nbsp;: c'est un découpage comptable, qui dit combien chaque terme a pesé, pas pourquoi le coût moyen a monté.

**Le partage dépend de l'année de départ.** Depuis 2019, avant la crise sanitaire, la charge augmente de {{< dette-val "dec19_delta" >}}&nbsp;milliards, dont {{< dette-val "dec19_volume" >}} au titre de l'encours et {{< dette-val "dec19_taux" >}} au titre du taux implicite&nbsp;: c'est alors l'encours qui pèse le plus, parce que 2020, où le coût moyen a baissé, entre dans le calcul. Partir du creux grossit la part du taux&nbsp;; les deux bases sont exactes, et aucune ne dit à elle seule ce qui «&nbsp;fait&nbsp;» la hausse.

**Le taux implicite a fait l'essentiel de son chemin en une seule année.** En {{< dette-val "dec_saut_annee" >}}, il passe de {{< dette-val "taux_saut_avant" >}}&nbsp;% à {{< dette-val "taux_saut_apres" >}}&nbsp;%, et la charge augmente de {{< dette-val "dec_saut_delta" >}}&nbsp;milliards, dont {{< dette-val "dec_saut_taux" >}} au titre du taux implicite. Cette année-là, l'inflation a fortement accru la charge des obligations de l'État indexées sur les prix, comptée dès qu'elle est due, selon le [rapport du Sénat sur les comptes de l'année](https://www.senat.fr/rap/l22-771-1/l22-771-17.html). Ces séries ne séparent pas, dans ce saut, la part de l'indexation de celle du refinancement.

**Depuis {{< dette-val "dec_saut_annee" >}}, c'est la hausse de l'encours qui pèse le plus.** De {{< dette-val "dec_saut_annee" >}} à {{< dette-val "dec_a1" >}}, la charge augmente encore de {{< dette-val "dec_apres_delta" >}}&nbsp;milliards, dont {{< dette-val "dec_apres_volume" >}} au titre de l'encours et {{< dette-val "dec_apres_taux" >}} au titre du taux implicite, qui ne progresse plus que lentement.

**Pourquoi le coût moyen a monté, ces séries ne le séparent pas.** Sa hausse mêle trois causes possibles&nbsp;: des titres renouvelés à des taux plus élevés, une dette composée autrement, l'indexation sur l'inflation. Les montants d'indexation publiés pour l'État ne s'ajoutent pas à ce calcul, qui porte sur l'ensemble des administrations publiques.

## Pourquoi les taux de marché ne se transmettent-ils pas tout de suite&nbsp;? {#transmission}

{{< figure-svg fichier="taux-marche-apparent" alt="Deux courbes en pourcentage par an, sur la même échelle : le taux à 10 ans et le taux implicite de la dette publique restent proches jusqu'au début des années 2010 ; ensuite le taux à 10 ans descend jusqu'à zéro puis remonte fortement, tandis que le taux implicite descend moins bas et remonte plus lentement." >}}Le taux à 10&nbsp;ans, moyenne annuelle et indicateur de référence des conditions d'emprunt (non le coût effectif des émissions), et le taux implicite, coût moyen de tout le stock, sur la même échelle — Eurostat <code>irt_lt_mcby_a</code> et <code>gov_10a_main</code>, INSEE.{{< /figure-svg >}}
{{< fig-actions id="marche" >}}

La charge d'une année rémunère des titres émis à des dates différentes, à des taux différents. Le taux implicite ne suit donc les taux de marché qu'au fil des renouvellements&nbsp;: il est passé d'environ {{< dette-val "taux_apparent_premier" >}}&nbsp;% en {{< dette-val "taux_apparent_premier_annee" >}} à {{< dette-val "taux_apparent_creux" >}}&nbsp;% en {{< dette-val "taux_apparent_creux_annee" >}}, moins bas que le taux à 10&nbsp;ans, et ne remonte qu'à {{< dette-val "taux_apparent_dernier" >}}&nbsp;% en {{< dette-val "taux_apparent_dernier_annee" >}}, quand le taux à 10&nbsp;ans est à {{< dette-val "taux_marche_dernier" >}}&nbsp;%&nbsp;: un titre renouvelé à ce taux coûte plus que la moyenne du stock. **Tant que des titres anciens, émis à bas taux, arrivent à échéance et se renouvellent plus cher, le coût moyen peut continuer de monter, même si les taux de marché se stabilisent.**

**Deux mécanismes, deux vitesses.** Les titres indexés transmettent l'inflation à la charge l'année même&nbsp;; le renouvellement des titres ne transmet les taux de marché qu'au fil des échéances, sur plusieurs années. L'un et l'autre se lisent dans les mêmes intérêts, et ces séries ne les séparent pas.

**Trois repères mesurent ces deux transmissions.**

- **La durée de vie moyenne** de la dette négociable de l'État&nbsp;: {{< dette-val "aft_dvm_ans" >}}&nbsp;ans et {{< dette-val "aft_dvm_jours" >}}&nbsp;jours à {{< dette-val "aft_date" >}} (Agence France Trésor). Elle ne signifie pas qu'il faut attendre {{< dette-val "aft_dvm_ans" >}}&nbsp;ans&nbsp;: une partie des titres arrive à échéance chaque année, et les titres de court terme se renouvellent en quelques mois.
- **Les titres indexés sur l'inflation**&nbsp;: {{< dette-val "aft_indexes_mdeur" >}}&nbsp;milliards sur {{< dette-val "aft_encours_mdeur" >}} à la même date, soit {{< dette-val "aft_part_indexes_pct" >}}&nbsp;%. Leur charge suit les prix sans attendre leur remboursement&nbsp;: selon le Gouvernement, cité par le Haut Conseil des finances publiques, un point d'inflation de plus ajoute environ {{< dette-val "sens_inflation_mdeur" >}}&nbsp;milliards à la charge la même année.
- **La sensibilité aux taux**&nbsp;: selon la même source, une hausse permanente d'un point de tous les taux ajouterait {{< dette-val "sens_taux_an1_mdeur" >}}&nbsp;milliards à la charge la première année et {{< dette-val "sens_taux_an2_mdeur" >}} la deuxième, puis davantage au fil des renouvellements. C'est un scénario de sensibilité, non une prévision.

Ces repères portent sur la dette de l'État, quand la charge de cette page couvre l'ensemble des administrations publiques&nbsp;: ils disent l'ordre de grandeur du retard, pas son calendrier exact.

<details class="repli"><summary>Le taux implicite seul, de {{< dette-val "taux_apparent_premier_annee" >}} à {{< dette-val "taux_apparent_dernier_annee" >}}&nbsp;: baisse sur vingt-cinq ans, point bas en {{< dette-val "taux_apparent_creux_annee" >}}, saut en {{< dette-val "dec_saut_annee" >}}</summary>

{{< figure-svg fichier="taux-apparent-dette" alt="Une courbe en pourcentage par an : le coût moyen du stock de dette publique descend pendant près de vingt-cinq ans jusqu'à son minimum, puis remonte, surtout par un saut en 2022." >}}<strong>Taux implicite</strong>&nbsp;: intérêts d'une année rapportés à l'encours au 31&nbsp;décembre précédent — calcul sur séries Eurostat (<code>gov_10a_main</code>) et INSEE. Le coût apparent que publie Eurostat retient, lui, l'encours moyen de l'année. La série complète est dans <a href="/dette_officielle.json">dette_officielle.json</a>.{{< /figure-svg >}}
{{< fig-actions id="taux" >}}

</details>

## Est-ce beaucoup&nbsp;? {#est-ce-beaucoup}

**Le niveau n'est pas inédit&nbsp;; la remontée est rapide.** En part du PIB ({{< dette-val "interets_pct_pib" >}}&nbsp;%), la charge de {{< dette-val "interets_annee" >}} retrouve son niveau de {{< dette-val "niv_pib_annee" >}}&nbsp;; en part des recettes publiques ({{< dette-val "interets_sur_recettes_pct" >}}&nbsp;%), celui de {{< dette-val "niv_rec_annee" >}}. En 1995, elle pesait {{< dette-val "interets_1995_pct_pib" >}}&nbsp;% du PIB et {{< dette-val "interets_1995_sur_recettes_pct" >}}&nbsp;% des recettes. Mais depuis le creux de {{< dette-val "interets_creux_annee" >}}, elle a augmenté de {{< dette-val "interets_hausse_pct" >}}&nbsp;% en euros, et de {{< dette-val "interets_hausse_2019_pct" >}}&nbsp;% depuis 2019&nbsp;: les deux bases mènent à la même conclusion. Les deux constats tiennent ensemble, et répondent aussi bien à «&nbsp;la dette ne coûte presque rien&nbsp;» qu'à «&nbsp;jamais la dette n'a coûté aussi cher&nbsp;».

{{< figure-svg fichier="charge-interets-mdeur" alt="Une courbe en milliards d'euros courants depuis 1995 : la charge d'intérêts oscille longtemps, descend jusqu'à son creux de 2020, puis remonte fortement ; deux cercles évidés, non reliés à la courbe, portent la prévision du Gouvernement." >}}Eurostat, intérêts dus par les administrations publiques, en euros courants non corrigés de l'inflation&nbsp;; cercles évidés&nbsp;: prévision du Gouvernement, sur une base qui n'est pas réconciliée avec Eurostat.{{< /figure-svg >}}
{{< fig-actions id="charge" >}}

**Brute, puis nette.** Les administrations perçoivent aussi des intérêts&nbsp;: {{< dette-val "interets_recus_mdeur" >}}&nbsp;milliards en {{< dette-val "interets_annee" >}}. Le solde entre intérêts dus et intérêts reçus est de {{< dette-val "interets_nets_mdeur" >}}&nbsp;milliards, en hausse de {{< dette-val "interets_nets_hausse_pct" >}}&nbsp;% depuis {{< dette-val "interets_creux_annee" >}}&nbsp;: la conclusion ne change pas. Ce solde n'est pas un «&nbsp;coût économique net&nbsp;» de la dette&nbsp;; il ne retranche que les intérêts perçus.

<details class="repli"><summary>Environ {{< interets-par-foyer >}}&nbsp;€ d'intérêts par foyer fiscal&nbsp;: une division arithmétique, ni un impôt dû ni la répartition réelle de la charge</summary>

**À l'échelle d'un foyer.** Rapportée aux {{< interets-par-foyer "foyers" >}}&nbsp;millions de foyers fiscaux ({{< interets-par-foyer "periode" >}}, DGFiP), la charge d'intérêts de {{< dette-val "interets_annee" >}} représente environ {{< interets-par-foyer >}}&nbsp;€ par foyer. C'est une division uniforme théorique de la charge totale&nbsp;: ce montant n'est pas un impôt dû par chaque foyer, et il ne dit pas qui la supporte — ménages, entreprises et non-résidents contribuent aux recettes publiques dans des proportions que ce calcul ignore. Qui la supporte est [l'objet du troisième volet](/qui-paie-la-dette-publique/).

</details>

<h3 id="masses-comparees">{{< dette-val "interets_equiv_mdeur" >}}&nbsp;milliards d’euros d’intérêts en {{< dette-val "equiv_annee" >}}&nbsp;: quel ordre de grandeur&nbsp;?</h3>

Sur **le même millésime**, {{< dette-val "equiv_annee" >}} (la ventilation par fonction paraît avec près de deux ans de retard), les intérêts ({{< dette-val "interets_equiv_mdeur" >}}&nbsp;Md€) représentent **{{< dette-val "interets_sur_recettes_equiv_pct" >}}&nbsp;% des recettes publiques**. Ils se situent entre le poste **«&nbsp;ordre et sécurité publics&nbsp;» (GF03, {{< dette-val "ordre_mdeur" >}}&nbsp;Md€)**, qu'ils dépassent, et l'**enseignement (GF09, {{< dette-val "education_mdeur" >}}&nbsp;Md€)**, dont ils représentent environ {{< dette-val "pct_interets_education" >}}&nbsp;%, loin de la **santé (GF07, {{< dette-val "sante_mdeur" >}}&nbsp;Md€)**, environ {{< dette-val "pct_interets_sante" >}}&nbsp;%. Face aux tribunaux seuls (GF0303, {{< dette-val "justice_mdeur" >}}&nbsp;Md€, et non le budget total de la mission Justice), la charge d'intérêts pèse environ {{< dette-val "ratio_interets_justice" >}}&nbsp;fois plus.

{{< figure-svg fichier="masses-comparees" alt="Quatre courbes en milliards d'euros courants depuis 1995 : la santé et l'enseignement montent régulièrement et restent les plus élevés ; la charge d'intérêts, longtemps stable puis en baisse, remonte après 2020 et repasse au-dessus du poste « ordre et sécurité »." >}}Eurostat, intérêts dus et dépenses des administrations par fonction. Toutes les séries s'arrêtent au même millésime.{{< /figure-svg >}}
{{< fig-actions id="masses" >}}

**Depuis le creux de {{< dette-val "creux_ref_annee" >}}, la charge progresse plus vite que chacune des neuf autres grandes fonctions de dépense**&nbsp;: +{{< dette-val "croiss_interets_depuis_creux_pct" >}}&nbsp;%, contre +{{< dette-val "croiss_max_autres_pct" >}}&nbsp;% pour la plus rapide d'entre elles ({{< dette-val "croiss_max_autres_nom" >}}). La dixième, les services publics généraux, contient les intérêts eux-mêmes. Sur l'ensemble de la période, c'était l'inverse&nbsp;: la baisse des taux allégeait la facture pendant que la dépense publique progressait.

<details class="repli"><summary>Précaution&nbsp;: ces équivalences comparent des masses, pas des causes — aucun euro d'intérêts n'est réputé pris à la santé, à l'école ou à la justice</summary>

Les intérêts sont une **nature** de dépense, les trois autres des **fonctions**. Ce n'est pas le même découpage — les intérêts figurent d'ailleurs dans la fonction «&nbsp;services publics généraux&nbsp;» — et la comparaison ne dit pas qu'un euro d'intérêts a été pris à l'un de ces budgets&nbsp;: elle donne un ordre de grandeur, un poids rapporté à la ressource publique.

</details>

## Quel stock cette facture rémunère-t-elle&nbsp;? {#stock-remunere}

Cette facture rémunère un stock&nbsp;: l'**encours** accumulé, le chiffre que l'on cite le plus souvent. Sa formation (ce qu'il doit aux déficits, aux intérêts et à la croissance) est l'objet du premier volet du dossier, [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)

{{< dette-chiffres live="true" historique="true" >}}
{{< fig-actions id="longue" >}}

Depuis {{< dette-val "hist_annee_debut" >}}, la dette publique est passée de {{< dette-val "hist_pct_debut" >}}&nbsp;% à {{< dette-val "dette_pct_pib" >}}&nbsp;% du PIB, multipliée par {{< dette-val "hist_multiple" >}}. Elle monte par paliers&nbsp;: les principaux sauts **coïncident avec les crises**, puis la **persistance des déficits** empêche d'effacer le palier atteint&nbsp;; dans la série observée, le ratio n'est jamais revenu à son niveau de dix ans auparavant. Sur la série trimestrielle de l'INSEE, disponible depuis 1995, le maximum du ratio est atteint au {{< dette-val "dette_pic_periode" >}} ({{< dette-val "dette_pic_pct_pib" >}}&nbsp;%).

<details class="repli"><summary>Les paliers depuis {{< dette-val "hist_annee_debut" >}}&nbsp;: 30, 60, 80 puis 100&nbsp;% du PIB, franchis après les chocs pétroliers, la récession de 1993, la crise financière et la crise sanitaire</summary>

- **{{< dette-val "hist_annee_debut" >}}&nbsp;— {{< dette-val "hist_pct_debut" >}}&nbsp;%.** Trente ans de forte croissance et d'inflation ont dilué la dette d'après-guerre&nbsp;: l'État rembourse dans une monnaie qui perd de sa valeur. Le désendettement éclair que l'on prête à l'inflation de la Libération est, lui, à réviser&nbsp;: en réintégrant les prix du marché noir, que l'indice officiel ignorait, Baubeau et Teixeira montrent que les prix ont bien plus monté pendant la guerre, et moins ensuite, qu'on ne le croyait&nbsp;; rapportée au revenu national, la dette a donc moins gonflé pendant le conflit, et moins fondu après ([*Economic History Review*, 2026](https://doi.org/10.1111/ehr.70127)).
- **{{< dette-val "hist_seuil_30_annee" >}}&nbsp;— 30&nbsp;%.** Après les deux chocs pétroliers, la croissance ralentit sans que les dépenses suivent&nbsp;: le déficit devient permanent, non par une décision datable, mais parce qu'il ne se referme plus entre deux ralentissements.
- **{{< dette-val "hist_seuil_60_annee" >}}&nbsp;— 60&nbsp;%.** La récession de 1993 creuse les comptes&nbsp;; le traité de Maastricht, signé en 1992 et entré en vigueur en novembre 1993, a fait de 60&nbsp;% la valeur de référence européenne. La dette la franchit en {{< dette-val "hist_seuil_60_annee" >}} et ne repassera en dessous qu'en {{< dette-val "hist_sous60_annees" >}}.
- **{{< dette-val "hist_seuil_80_annee" >}}&nbsp;— 80&nbsp;%.** La crise financière fait chuter les recettes et impose des plans de soutien&nbsp;: {{< dette-val "hist_choc_crise_pts" >}}&nbsp;points de PIB de plus entre fin {{< dette-val "hist_choc_crise_debut" >}} et fin {{< dette-val "hist_seuil_80_annee" >}}. La reprise qui suit ne les rattrape pas.
- **{{< dette-val "hist_seuil_100_annee" >}}&nbsp;— 100&nbsp;%.** L'arrêt de l'économie et le soutien aux revenus ajoutent {{< dette-val "hist_choc_sanitaire_pts" >}}&nbsp;points en une seule année. La dette dépasse la taille du PIB.
- **{{< dette-val "dette_periode" >}}&nbsp;— {{< dette-val "dette_pct_pib" >}}&nbsp;%.** L'encours reste orienté à la hausse, et son coût moyen remonte depuis son point bas de {{< dette-val "taux_apparent_creux_annee" >}}, surtout par le saut de {{< dette-val "dec_saut_annee" >}}.

</details>

## La facture peut-elle monter si la dette cesse d'augmenter&nbsp;? {#ce-que-la-facture-ne-dit-pas-la-dette-augmente-t-elle}

**Oui, tant que le coût moyen rattrape les taux de marché.** Stabiliser le ratio de dette ne stabiliserait pas la facture à court terme&nbsp;: les titres anciens, émis à bas taux, continuent d'arriver à échéance et de se renouveler plus cher. Même à ratio de dette et taux implicite constants, la charge en euros augmenterait avec l'encours et le PIB nominal&nbsp;; son poids dans le PIB, lui, resterait à peu près stable. La facture et le ratio de dette sont deux questions distinctes&nbsp;: ce qui fait monter le ratio (les déficits, les intérêts, la croissance) est l'objet du premier volet du dossier, [Pourquoi la dette publique augmente-t-elle&nbsp;?](/pourquoi-la-dette-publique-augmente/)

**Ce que prévoit le Gouvernement.** Selon le scénario du Gouvernement présenté au Haut Conseil des finances publiques pour le projet de loi de finances pour {{< dette-val "prev_edition" >}}, la charge d'intérêts atteindrait {{< dette-val "prev_charge_n_mdeur" >}}&nbsp;Md€ en {{< dette-val "prev_n_annee" >}}, puis {{< dette-val "prev_charge_n1_mdeur" >}}&nbsp;Md€ en {{< dette-val "prev_n1_annee" >}}, soit {{< dette-val "prev_charge_n1_pct_pib" >}}&nbsp;% du PIB, le niveau de {{< dette-val "prev_niveau_annee" >}}, tandis que la dette atteindrait {{< dette-val "prev_dette_n1_pct_pib" >}}&nbsp;% du PIB fin {{< dette-val "prev_n1_annee" >}}, {{< dette-val "prev_dette_revision_pts" >}}&nbsp;points de plus que dans le projet de loi de finances pour {{< dette-val "prev_edition_prec" >}}. Le Haut Conseil, que la loi charge d'apprécier le réalisme de ces prévisions, estime que la charge pourrait dépasser ce montant si l'inflation ou les taux montaient encore. Il relève aussi que la charge prévue pour {{< dette-val "prev_n_annee" >}} dépasse de {{< dette-val "prev_ecart_lfi_mdeur" >}}&nbsp;Md€ celle de la loi de finances initiale, essentiellement à cause des obligations indexées sur les prix&nbsp;: l'indexation ne joue pas qu'en 2022.

**Ces prévisions ne prolongent pas la courbe observée.** Le Haut Conseil écrit que la charge de {{< dette-val "prev_n1_annee" >}} serait «&nbsp;en hausse de plus de {{< dette-val "prev_hausse_plus_de_mdeur" >}}&nbsp;Md€ par rapport à 2025&nbsp;», ce qui suppose une base 2025 inférieure aux {{< dette-val "interets_mdeur" >}}&nbsp;milliards d'Eurostat&nbsp;: les deux séries ne sont pas réconciliées. Sur les figures, la prévision est faite de cercles évidés, non reliés à la courbe, et aucune hausse entre l'observé et le prévu ne se calcule par soustraction.

## Ce que les données ne montrent pas

**Les dépenses observées de santé et d'enseignement n'ont pas baissé.** En euros, elles ont continué de croître. En part du PIB, elles sont au-dessus de 2019 (santé&nbsp;: {{< dette-val "sante_pct_2019" >}}&nbsp;% puis {{< dette-val "sante_pct_equiv" >}}&nbsp;% en {{< dette-val "equiv_annee" >}}&nbsp;; enseignement&nbsp;: {{< dette-val "education_pct_2019" >}}&nbsp;% puis {{< dette-val "education_pct_equiv" >}}&nbsp;%), un peu sous leur pic de la crise sanitaire ({{< dette-val "sante_pct_pic" >}}&nbsp;% en {{< dette-val "sante_pic_annee" >}} pour la santé), quand le PIB s'est contracté. Quiconque affirme que la dette a «&nbsp;déjà fait baisser&nbsp;» ces budgets dit plus que les données. Mais l'inverse ne se déduit pas davantage&nbsp;: ces séries ne permettent **ni d'attribuer leur trajectoire à la dette, ni d'exclure qu'elles auraient été plus élevées** sans la contrainte d'intérêts. Un budget qui passe de 100 à 105 au lieu de 110 n'a pas baissé, et a pourtant été évincé. Sans contrefactuel, pas de causalité — dans un sens comme dans l'autre.

<details class="repli"><summary>Budgets en hausse, services sous tension&nbsp;: une explication plausible (coûts salariaux, effet Baumol, besoins croissants) que ces séries ne démontrent pas</summary>

D'où un paradoxe apparent&nbsp;: si les budgets montent, pourquoi l'hôpital, l'école ou les tribunaux semblent-ils manquer de moyens&nbsp;? L'explication la plus courante — **plausible, mais que les séries de cette page ne démontrent pas** — tient en deux mécanismes classiques. Un service public est d'abord fait de personnes&nbsp;: ses coûts suivent les salaires, pas les gains de productivité des machines (l'effet Baumol, classique en économie des services — son ampleur varie selon les secteurs). Et la demande de certains d'entre eux croîtrait plus vite que le PIB&nbsp;: vieillissement et progrès médical coûteux en santé, judiciarisation en justice. Si ces deux mécanismes jouent, la stabilité d'un poste en part de PIB **ne garantit pas** la stabilité du volume ni de la qualité du service rendu. Établir qu'il a effectivement baissé demanderait ce que cette page ne mesure pas&nbsp;: inflation sectorielle, salaires, productivité, démographie, et volumes réellement produits.

</details>

Ce que les données établissent est plus étroit&nbsp;: une charge d'intérêts plus élevée **augmente le besoin de financement à politiques inchangées**&nbsp;; ses conséquences sur les dépenses, les prélèvements et le déficit dépendent ensuite des arbitrages, de la conjoncture et du financement disponible — ce n'est pas la même chose que de dire qu'elle manque euro pour euro à la santé ou à l'école. La question n'est donc pas «&nbsp;les budgets baissent-ils&nbsp;?&nbsp;» mais «&nbsp;**qui absorbera l'ajustement**&nbsp;»&nbsp;: impôts supplémentaires, réduction d'autres dépenses, déficit accru, inflation, ou générations futures. C'est l'objet de la page [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/) et des scénarios 2025-2035 du livre [*Dette Publique&nbsp;: Qui paie vraiment&nbsp;?*](/livres/dette-publique-qui-paie-vraiment/) (2025, 225&nbsp;p.).

**Une hypothèse interprétative de l'auteur, distincte des constats.** Dans le cadre de l'anthropie, que l'auteur développe dans le working paper [AWP-07 — *La boucle anthropique*](/awp/awp-07/), appliqué à la dette dans [AWP-03](/awp/awp-03/), cette séquence peut être lue comme un coût déplacé dans le temps qui revient&nbsp;: déplacement, saturation, retour. Les séries de cette page établissent la baisse puis la remontée de la charge et de son coût moyen&nbsp;; elles ne testent pas cette lecture, ni ne disent que le retour était inévitable ou quelle sera son ampleur. Ce qu'elle ajoute à la notion ordinaire de coût différé est une condition qu'on peut mettre à l'épreuve, proposée dans le working paper [AWP-09](/awp/awp-09/)&nbsp;: comparer le coût des émissions nouvelles au coût moyen du stock.

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

**Pourquoi la facture a longtemps baissé.** Pendant vingt-cinq ans, la baisse du coût moyen du stock a compensé la hausse de l'encours&nbsp;: la dette a doublé en part de PIB, sa charge a baissé.

**Pourquoi elle remonte.** Depuis {{< dette-val "dec_a0" >}}, encours et coût moyen montent ensemble&nbsp;: {{< dette-val "dec_volume" >}}&nbsp;milliards de la hausse tiennent à l'encours, {{< dette-val "dec_taux" >}} au taux implicite, dont l'essentiel en {{< dette-val "dec_saut_annee" >}}, l'année du choc d'inflation sur les titres indexés&nbsp;; depuis 2019, c'est l'encours qui pèse le plus. Le niveau atteint n'est pas inédit (celui de {{< dette-val "niv_pib_annee" >}} en part du PIB)&nbsp;; la remontée, elle, est rapide.

**Pourquoi elle peut continuer.** Le coût moyen ne rattrape les taux de marché qu'au fil des renouvellements&nbsp;: la facture peut monter alors même que la dette cesse d'augmenter. Les {{< dette-val "interets_mdeur" >}}&nbsp;milliards ne se retranchent d'aucun budget en particulier&nbsp;: à politiques inchangées, ils augmentent le besoin de financement, et les arbitrages décident du reste.

<details class="repli"><summary>Règle&nbsp;: chaque comparaison porte sur une seule année — {{< dette-val "equiv_annee" >}} pour les masses, {{< dette-val "interets_annee" >}} pour la charge la plus récente —, jamais sur deux années mélangées</summary>

Une règle gouverne toutes les comparaisons de cette page&nbsp;: **le millésime commun le plus récent, le même pour tous les termes**. La ventilation des dépenses par fonction paraissant avec près de deux ans de retard, les masses comparées portent sur {{< dette-val "equiv_annee" >}}, quand la charge d'intérêts la plus récente porte sur {{< dette-val "interets_annee" >}}. Les deux années sont dites, jamais mélangées.

</details>

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

Reste une question que ces chiffres ne tranchent pas&nbsp;: qui supporte in fine cette charge, et une partie de son coût est-elle déplacée vers d'autres&nbsp;? C'est l'objet de la page suivante.

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Pour prolonger l’analyse" avis="non" >}}
Cette page chiffre la facture. Elle ne dit pas qui la règle — et c'est là que tout se joue&nbsp;: une dette ne s'efface pas, et son coût peut se déplacer — vers le contribuable, vers l'épargnant par l'inflation, vers des services publics dont la marge se resserre, vers ceux qui ne votent pas encore — selon les décisions prises pour l'ajuster. Le livre suit ces canaux un par un, chiffres officiels à l'appui, et conduit aux scénarios 2025-2035. Vous saurez, à la fin, reconnaître celui qui est en train de se réaliser.
{{< /appel-livre >}}

## D'où viennent ces chiffres

Les valeurs de cette page sont **dérivées automatiquement des sources officielles** (INSEE, Eurostat), jamais recopiées, et réinterrogées chaque semaine&nbsp;; dernier relevé ayant fait bouger une valeur&nbsp;: {{< dette-val "releve_le" >}}. Deux familles de valeurs sont saisies à la main, avec leur source et leur date&nbsp;: les prévisions du Gouvernement et les repères de l'Agence France Trésor. Données en accès libre&nbsp;: [dette_officielle.json](/dette_officielle.json), licence CC&nbsp;BY&nbsp;4.0.

<details class="repli"><summary>Séries INSEE et Eurostat, intérêts en droits constatés, taux implicite sur la dette de fin d'année précédente, valeurs saisies datées&nbsp;; compilation sous licence CC&nbsp;BY&nbsp;4.0</summary>

Valeurs **dérivées automatiquement des sources officielles**&nbsp;: dette de Maastricht trimestrielle de l'INSEE (séries [010777616](https://www.insee.fr/fr/statistiques/serie/010777616) — encours en milliards d'euros — et [010777608](https://www.insee.fr/fr/statistiques/serie/010777608) — % du PIB)&nbsp;; intérêts dus (D41PAY), intérêts reçus (D41REC) et recettes totales (TR) des administrations publiques ([Eurostat, `gov_10a_main`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table?lang=fr))&nbsp;; dépenses par fonction COFOG, dont les dix grandes fonctions ([Eurostat, `gov_10a_exp`](https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table?lang=fr))&nbsp;; taux à 10&nbsp;ans ([Eurostat, `irt_lt_mcby_a`](https://ec.europa.eu/eurostat/databrowser/view/irt_lt_mcby_a/default/table?lang=fr)). Le taux implicite est calculé comme intérêts de l'année rapportés à l'encours de fin d'année précédente&nbsp;; la décomposition de la hausse de la charge en partage la variation entre encours et taux implicite par contributions à mi-chemin. La charge d'intérêts retenue est la série `D41PAY`, enregistrée en droits constatés — rattachée à l'année où les intérêts sont dus, non à la date de paiement, ce qui y fait entrer l'indexation des titres indexés dès qu'elle est acquise — et portant sur le même ensemble, toutes administrations publiques, que les recettes auxquelles elle est rapportée&nbsp;; les comptes de l'INSEE présentent les intérêts hors correction SIFIM (services d'intermédiation financière indirectement mesurés) et affichent, pour la même année, un montant légèrement différent&nbsp;: deux conventions voisines, non deux mesures contradictoires.

**Valeurs saisies.** Les prévisions du Gouvernement pour {{< dette-val "prev_n_annee" >}} et {{< dette-val "prev_n1_annee" >}} et sa sensibilité aux taux et à l'inflation sont lues dans l'[avis du Haut Conseil des finances publiques sur les projets de lois de finances pour {{< dette-val "prev_edition" >}}](https://www.hcfp.fr/liste-avis/avis-ndeg2026-5-lois-de-finances-2027) (paragraphes 113, 115 et 116), qui les rapporte&nbsp;; l'avis est archivé avec son empreinte. Elles ne sont pas soustraites de l'observation d'Eurostat&nbsp;: la valeur 2025 sous-jacente aux prévisions n'est pas réconciliée avec la série utilisée ici. La durée de vie moyenne et les titres indexés de la dette négociable de l'État sont ceux que publie l'[Agence France Trésor](https://www.aft.gouv.fr/fr/principaux-chiffres-dette) pour {{< dette-val "aft_date" >}}.

Les séries officielles sont réinterrogées chaque semaine&nbsp;; la date du relevé ne change que lorsqu'une publication modifie un chiffre. Les données consolidées sont publiées en accès libre&nbsp;: [dette_officielle.json](/dette_officielle.json), sous licence [CC&nbsp;BY&nbsp;4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) — réutilisation libre, y compris commerciale, à la seule condition de citer la source. Les séries brutes appartiennent à l'INSEE et à Eurostat&nbsp;; ce qui est mis sous licence ici, c'est la compilation&nbsp;: l'assemblage des séries, les grandeurs dérivées (taux implicite, décomposition, ratios, équivalences à millésime unique) et leur mise en cohérence. Le compteur animé de la page est une extrapolation mécanique entre deux publications trimestrielles — jamais une donnée.

</details>

{{< reutiliser figures="figures_dette" jeu="dette_officielle" sources="INSEE et Eurostat" >}}
Cette page mesure ce que la dette publique coûte chaque année — la charge d'intérêts, {{< dette-val "interets_mdeur" >}}&nbsp;milliards d'euros en {{< dette-val "interets_annee" >}} — et non le montant de l'encours. Elle montre pourquoi un encours deux fois plus lourd n'a pas doublé la facture, décompose la remontée depuis {{< dette-val "dec_a0" >}} entre la hausse de l'encours et celle du taux implicite (décomposition comptable, non mesure de l'effet des taux de marché), situe le niveau atteint dans la série longue et explique pourquoi la facture peut continuer de monter alors même que la dette cesse d'augmenter. Elle compare des masses à périmètre et millésime identiques, sans établir qu'un euro d'intérêts ait été retiré à un autre budget.
{{< /reutiliser >}}

{{< canonical-definition >}}
