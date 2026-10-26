---
title: "Qui peut faire face à une dépense imprévue ?"
description: "En France, {imp.total} % des personnes ne pourraient pas faire face à une dépense imprévue ({imp.annee}, Eurostat). Le revenu ne dit pas tout : au-dessus du seuil de pauvreté, {imp.ps_dessus} % des parents seuls sont dans ce cas, contre {imp.c1_dessus} % des couples avec un enfant."
chapo: "Ne pas pouvoir faire face à une dépense imprévue, est-ce une affaire de pauvreté ? En partie seulement. En France, en {imp.annee}, {imp.dessous} % des personnes sous le seuil de pauvreté sont dans ce cas, et {imp.dessus} % au-dessus. Mais au-dessus du seuil, la composition du foyer change tout : {imp.ps_dessus} % des parents seuls ne pourraient pas faire face à une dépense imprévue, contre {imp.c1_dessus} % des couples avec un enfant."
date: 2026-10-26
lastmod: 2026-10-26
og_title: "Qui peut faire face à une dépense imprévue ? — S. Lalut"
og_image: "images/og-imprevu-menages.jpg"
og_image_alt: "Carte de partage : « Le revenu ne dit pas tout » — part des personnes qui ne pourraient pas faire face à une dépense imprévue, au-dessus du seuil de pauvreté : parents seuls et couples avec un enfant, France (Eurostat, EU-SILC)."
# Page née de l'arbitrage PRO-20261026-033434 (graphe G1, page de faits distincte de la notion de réversibilité sociale) et du
# comité de lecteurs du 26/10/2026 (témoin à une seule variable). Fiche : docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md.
# Aucun chiffre saisi : jetons {imp.*} et shortcode imp-val (scripts/update_menages_imprevu.py, Eurostat ilc_mdes04).
donnees: [menages_imprevu]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "menages_imprevu"
  nom: "Incapacité à faire face à une dépense imprévue, selon la composition du ménage et le seuil de pauvreté — France et Union européenne"
  description: "Part des personnes dont le ménage ne pourrait pas faire face à une dépense imprévue (Eurostat, EU-SILC, jeu ilc_mdes04), par composition du ménage (couple ou adulte seul, avec ou sans enfants) et position par rapport au seuil de pauvreté (60 % du revenu médian équivalent), France et Union européenne à 27, séries annuelles relevées par l'API d'Eurostat."
  couverture_temporelle: "2003/{imp.annee}"
  couverture_spatiale: "France ; Union européenne à 27"
  variables:
    - {nom: "Personnes incapables de faire face à une dépense imprévue", unite: "% des personnes", description: "par composition du ménage et position par rapport au seuil de pauvreté"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table"
  mots: ["dépense imprévue", "épargne de précaution", "familles monoparentales", "parent seul", "seuil de pauvreté", "EU-SILC", "privation matérielle", "inégalités", "composition du ménage"]
  fichiers: ["menages_imprevu.csv", "menages_imprevu.json"]
faq:
  - question: "Quelle part des Français ne pourrait pas faire face à une dépense imprévue ?"
    answer: "En {imp.annee}, {imp.total} % des personnes vivant en France déclarent que leur ménage ne pourrait pas faire face à une dépense imprévue (Eurostat, enquête EU-SILC). La part atteint {imp.dessous} % sous le seuil de pauvreté et {imp.dessus} % au-dessus."
  - question: "Les parents seuls sont-ils plus exposés, même sans être pauvres ?"
    answer: "Oui, et c'est au-dessus du seuil de pauvreté que l'écart est le plus net : en {imp.annee}, {imp.ps_dessus} % des parents seuls au-dessus du seuil ne pourraient pas faire face à une dépense imprévue, contre {imp.c1_dessus} % des couples avec un enfant, soit {imp.ecart_enf} d'écart. Sans enfant, le même passage de deux adultes à un seul n'ajoute que {imp.ecart_sans}. C'est une association : la série ne dit pas si l'écart tient à la composition du foyer ou à une position plus basse dans la tranche de revenu."
  - question: "D'où viennent ces chiffres ?"
    answer: "De l'enquête européenne sur les revenus et les conditions de vie (EU-SILC), jeu ilc_mdes04 d'Eurostat (séries de 2003 à {imp.annee}), relevé par un script qui refuse de publier si une donnée cesse de soutenir une phrase de la page. Les données sont téléchargeables en CSV et en JSON, sous licence CC BY 4.0."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md"  # fiche de conception (regle 12)
  refonte: "2026-10-26"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["la-societe-du-premier-coup"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 40
  nature: "Données officielles recalculées (Eurostat, EU-SILC)"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données du&nbsp;: {{< imp-val "date_donnees" >}}</span> Eurostat, enquête EU-SILC, jeu ilc_mdes04&nbsp;: France et Union européenne à&nbsp;27, séries complètes depuis le début de l'enquête&nbsp;; écarts étudiés de {{< imp-val "debut" >}} à {{< imp-val "annee" >}}. Télécharger&nbsp;: <a href="/menages_imprevu.csv">CSV</a> · <a href="/menages_imprevu.json">JSON</a></p>

## Qui ne pourrait pas faire face à une dépense imprévue&nbsp;? {#qui}

En France, en {{< imp-val "annee" >}}, {{< imp-val "total" >}}&nbsp;% des personnes vivent dans un ménage qui, selon ses propres déclarations, ne pourrait pas faire face à une dépense imprévue&nbsp;: près de trois sur dix. Le revenu pèse lourd. Sous le seuil de pauvreté, la part atteint {{< imp-val "dessous" >}}&nbsp;%, environ deux tiers&nbsp;; au-dessus, {{< imp-val "dessus" >}}&nbsp;%, environ une sur cinq.

Mais le revenu ne dit pas tout. Au-dessus du seuil, là où le classement par le revenu dit «&nbsp;pas pauvre&nbsp;», la composition du foyer sépare nettement les situations.

<figure class="figure-ciseau">
  <picture>
    <source media="(max-width: 600px)" srcset="/img/imprevu-menages-m.svg" width="300" height="710">
    <img src="/img/imprevu-menages.svg" alt="Barres horizontales, France {{< imp-val "annee" >}}, part des personnes qui ne pourraient pas faire face à une dépense imprévue. Au-dessus du seuil de pauvreté : couple sans enfant {{< imp-val "c0_dessus" >}} %, adulte seul {{< imp-val "seul_dessus" >}} %, couple avec un enfant {{< imp-val "c1_dessus" >}} %, parent seul {{< imp-val "ps_dessus" >}} %. En dessous du seuil : {{< imp-val "c0_dessous" >}} %, {{< imp-val "seul_dessous" >}} %, {{< imp-val "c1_dessous" >}} % et {{< imp-val "ps_dessous" >}} %." width="720" height="335" loading="lazy">
  </picture>
  <figcaption>Part des personnes, déclaratif&nbsp;; seuil de pauvreté&nbsp;: 60&nbsp;% du revenu médian par unité de consommation (Eurostat, EU-SILC).</figcaption>
</figure>

<div class="resultat-phrase">

**Le résultat en une phrase.** En France, en {{< imp-val "annee" >}}, au-dessus du seuil de pauvreté, {{< imp-val "ps_dessus" >}}&nbsp;% des parents seuls ne pourraient pas faire face à une dépense imprévue, contre {{< imp-val "c1_dessus" >}}&nbsp;% des couples avec un enfant&nbsp;: {{< imp-val "ratio" >}}&nbsp;fois plus.

</div>

## Deux explications, un test {#test}

On pourrait croire que tout se joue sur le revenu&nbsp;: être au-dessus ou en dessous du seuil de pauvreté. Si c'était le cas, deux foyers situés du même côté du seuil devraient avoir des parts voisines. Le test compare des foyers qui diffèrent d'abord par une chose&nbsp;: un adulte de plus ou de moins.

- **Avec un enfant**, passer de deux adultes à un seul ajoute {{< imp-val "ecart_enf" >}} au-dessus du seuil en {{< imp-val "annee" >}}, et de {{< imp-val "plage_enf_bas" >}} à {{< imp-val "plage_enf_haut" >}}&nbsp;points chaque année depuis {{< imp-val "debut" >}}.
- **Sans enfant**, le même passage n'ajoute que {{< imp-val "ecart_sans" >}} (de {{< imp-val "plage_sans_bas" >}} à {{< imp-val "plage_sans_haut" >}}&nbsp;points sur la même période).
- **Le nombre d'enfants ne suffit pas à expliquer l'écart.** La statistique compte comme «&nbsp;parent seul&nbsp;» tout adulte seul avec un enfant ou plus&nbsp;; face aux couples avec deux enfants, l'écart reste de {{< imp-val "ecart_enf2" >}}.

L'écart lié au fait d'être seul est donc deux à trois fois plus grand quand il y a des enfants, et c'est au-dessus du seuil de pauvreté qu'il est le plus net. En dessous, il se resserre ({{< imp-val "ecart_enf_dessous" >}} en {{< imp-val "annee" >}})&nbsp;: parents seuls comme couples avec un enfant y sont en grande majorité exposés. Être au-dessus ou en dessous du seuil ne suffit donc pas à expliquer ces écarts.

**Ce que le test ne tranche pas.** Une troisième explication reste possible&nbsp;: au-dessus du seuil, les parents seuls pourraient être en moyenne plus proches du seuil que les couples avec un enfant. Le jeu d'Eurostat ne détaille pas la position dans la tranche de revenu&nbsp;; il ne permet donc pas de séparer ce que pèse la composition du foyer de ce que pèse cette position.

## Le même constat dans l'Union européenne {#europe}

Dans l'Union européenne à&nbsp;27, {{< imp-val "ue_total" >}}&nbsp;% des personnes ne pourraient pas faire face à une dépense imprévue en {{< imp-val "annee" >}}. Au-dessus du seuil de pauvreté, le passage de deux adultes à un seul ajoute {{< imp-val "ue_ecart_enf" >}} avec un enfant (de {{< imp-val "ue_plage_enf_bas" >}} à {{< imp-val "ue_plage_enf_haut" >}}&nbsp;points depuis {{< imp-val "debut" >}}), contre {{< imp-val "ue_ecart_sans" >}} sans enfant (de {{< imp-val "ue_plage_sans_bas" >}} à {{< imp-val "ue_plage_sans_haut" >}}). Le constat n'est pas propre à la France.

## Ce que ces données ne disent pas {#limites}

- **Une déclaration, pas un compte en banque.** La question porte sur la capacité perçue du ménage à couvrir une dépense imprévue d'un montant fixé par l'enquête pour chaque pays&nbsp;; elle ne mesure ni l'épargne ni les actifs disponibles.
- **Des personnes, pas des ménages.** Les parts sont calculées sur les personnes&nbsp;: un enfant d'un foyer exposé compte comme exposé.
- **Le seuil de pauvreté est relatif.** Il vaut 60&nbsp;% du revenu médian par unité de consommation&nbsp;; il tient compte de la taille du ménage, pas de la réserve dont il dispose.
- **Une association, non une cause.** Le graphe montre que la composition du foyer et la vulnérabilité au choc vont ensemble, pas que l'une produit l'autre&nbsp;; la position dans la tranche de revenu n'est pas contrôlée.
- **Des ruptures de série.** Eurostat signale des ruptures en France en {{< imp-val "ruptures_fr" >}}&nbsp;: les plages pluriannuelles se lisent avec prudence. Le constat principal compare des ménages la même année, et la rupture ne l'atteint pas.

<aside class="encadre">

**Une hypothèse de l'auteur, non testée ici.** Dans le working paper [AWP-08](/awp/awp-08/), l'économiste Stéphane Lalut propose de lire la capacité de repli financier comme l'une des trois composantes de ce que l'auteur appelle la [réversibilité sociale](/reversibilite-sociale/)&nbsp;: ce qu'une personne peut se permettre de rater sans fermer durablement son avenir. L'indicateur de cette page n'en mesure qu'une partie&nbsp;; il ne dit rien du coût d'un échec ni de la possibilité de recommencer.

</aside>

{{< appel-livre slug="la-societe-du-premier-coup" sur="Pour prolonger la question" avis="non" >}}
*La Société du premier coup* raconte, à partir de cas concrets, ce que coûte un échec selon la position sociale de celui qui le subit, et pourquoi certains ne peuvent pas se permettre d'essayer.
{{< /appel-livre >}}

## Sources {#sources}

- Eurostat, enquête européenne sur les revenus et les conditions de vie (EU-SILC), jeu [ilc_mdes04](https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table) («&nbsp;Incapacité à faire face à des dépenses financières imprévues&nbsp;»), relevé par l'API de diffusion. Calculs de l'auteur&nbsp;: écarts entre compositions de ménage, plages annuelles.

{{< reutiliser figures="figures_imprevu" jeu="menages_imprevu" sources="Eurostat (EU-SILC)" donnees="La part des personnes incapables de faire face à une dépense imprévue, pour la France et l'Union européenne à 27, par composition du ménage et position par rapport au seuil de pauvreté, chaque année depuis le début de l'enquête ; le même contenu existe en CSV, au format long, avec les drapeaux d'Eurostat." >}}
Au-dessus du seuil de pauvreté, la part des personnes incapables de faire face à une dépense imprévue est plus de deux fois plus élevée chez les parents seuls que chez les couples avec un enfant. Quand il y a des enfants, le passage de deux adultes à un seul pèse deux à trois fois plus qu'en l'absence d'enfants. Le revenu relatif ne dit donc pas tout de la capacité d'encaisser un choc.
{{< /reutiliser >}}
