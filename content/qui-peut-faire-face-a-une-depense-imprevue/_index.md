---
title: "Qui peut faire face à une dépense imprévue ?"
description: "En France, {imp.total} % des personnes ne pourraient pas faire face à une dépense imprévue ({imp.annee}, Eurostat). Le seuil de pauvreté ne dit pas tout : au-dessus de ce seuil, {imp.ps_dessus} % des personnes vivant dans un foyer monoparental sont dans ce cas, contre {imp.c1_dessus} % de celles vivant dans un foyer de deux adultes avec un enfant."
chapo: "Ne pas pouvoir faire face à une dépense imprévue, est-ce une affaire de pauvreté ? En partie seulement. En France, en {imp.annee}, {imp.dessous} % des personnes sous le seuil de pauvreté sont dans ce cas, et {imp.dessus} % au-dessus. Mais au-dessus du seuil, les situations diffèrent nettement selon la composition du foyer : {imp.ps_dessus} % des personnes vivant dans un foyer monoparental ne pourraient pas faire face à une dépense imprévue, contre {imp.c1_dessus} % de celles vivant dans un foyer de deux adultes avec un enfant."
date: 2026-10-26
lastmod: 2026-11-12
journal:  # révisions qui changent la lecture de la page
  - {date: 2026-11-12, texte: "Reprise : la comparaison présentée pour ce qu'elle permet de dire et ce qu'elle ne permet pas (deux groupes, non le passage d'un foyer de deux adultes à un seul ; d'autres différences possibles entre ces foyers), au lieu d'un « test » ; le foyer d'un adulte compte un ou plusieurs enfants, celui de deux adultes un enfant, couple ou non ; la figure retitrée, sa note et la carte de partage portent la réserve ; l'indicateur, déclaré par le ménage, ne saisit que le volet financier de la capacité individuelle de repli."}
  - {date: 2026-11-07, texte: "Correction : les parts sont celles des personnes vivant dans chaque type de foyer (enfants compris), non des parents ni des foyers ; le texte, les figures et la carte de partage le disent désormais. Valeurs inchangées."}
  - {date: 2026-11-05, texte: "Correction : les fourchettes de taux sont arrondies vers l'extérieur (borne basse à l'unité inférieure, borne haute à l'unité supérieure), pour contenir toutes les valeurs qu'elles résument."}
og_title: "Qui peut faire face à une dépense imprévue ? — S. Lalut"
og_image: "images/og-imprevu-menages.jpg"
og_image_alt: "Carte de partage : « Dépense imprévue : être au-dessus du seuil de pauvreté ne suffit pas » — part des personnes qui ne pourraient pas faire face à une dépense imprévue, au-dessus du seuil de pauvreté, en France : foyers de deux adultes sans enfant, de deux adultes avec un enfant et d'un adulte avec enfants (Eurostat, EU-SILC) ; association, non cause, pas à revenu égal."
# Page née de l'arbitrage PRO-20261026-033434 (graphe G1, page de faits distincte de la notion de réversibilité sociale) et du
# comité de lecteurs du 26/10/2026 (témoin à une seule variable). Fiche : docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md.
# Aucun chiffre saisi : jetons {imp.*} et shortcode imp-val (scripts/update_menages_imprevu.py, Eurostat ilc_mdes04).
donnees: [menages_imprevu]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "menages_imprevu"
  apropos: "capacité des ménages à faire face à une dépense imprévue"
  nom: "Incapacité à faire face à une dépense imprévue, selon la composition du ménage et le seuil de pauvreté — France et Union européenne"
  description: "Part des personnes dont le ménage ne pourrait pas faire face à une dépense imprévue (Eurostat, EU-SILC, jeu ilc_mdes04), par composition du ménage (un ou deux adultes, avec ou sans enfants dépendants) et position par rapport au seuil de pauvreté (60 % du revenu disponible médian national équivalent), France et Union européenne à 27, séries annuelles relevées par l'API d'Eurostat."
  couverture_temporelle: "2004/{imp.annee}"
  couverture_spatiale: "France ; Union européenne à 27"
  variables:
    - {nom: "Personnes incapables de faire face à une dépense imprévue", unite: "% des personnes", description: "par composition du ménage et position par rapport au seuil de pauvreté"}
  sources:
    - "https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table"
  mots: ["dépense imprévue", "épargne de précaution", "familles monoparentales", "parent seul", "seuil de pauvreté", "EU-SILC", "privation matérielle", "inégalités", "composition du ménage"]
  fichiers: ["menages_imprevu.csv", "menages_imprevu.json"]
faq:
  - question: "Quelle part des personnes vivant en France ne pourrait pas faire face à une dépense imprévue ?"
    answer: "En {imp.annee}, {imp.total} % des personnes vivant en France font partie d'un ménage qui déclare ne pas pouvoir faire face, par ses seuls moyens, à une dépense imprévue de {imp.montant_question} € (Eurostat, enquête EU-SILC). La part est de {imp.dessous} % sous le seuil de pauvreté et de {imp.dessus} % au-dessus."
  - question: "Les personnes vivant dans un foyer monoparental sont-elles plus souvent dans l'incapacité de faire face à une dépense imprévue, même sans être pauvres ?"
    answer: "Oui, au sens d'une association, non d'une cause ; l'écart est plus net au-dessus du seuil de pauvreté qu'en dessous. En France, en {imp.annee}, au-dessus du seuil, {imp.ps_dessus} % des personnes vivant dans un foyer monoparental (un adulte avec un ou plusieurs enfants) ne pourraient pas faire face à une dépense imprévue de {imp.montant_question} €, contre {imp.c1_dessus} % de celles vivant dans un foyer de deux adultes avec un enfant, soit {imp.ecart_enf} d'écart. Sans enfant, l'écart entre foyers d'un et de deux adultes n'est que de {imp.ecart_sans}. La série ne dit pas si l'écart tient à la composition du foyer, à un revenu plus proche du seuil ou à d'autres différences entre ces foyers (nombre et âge des enfants, emploi, dépenses contraintes, aides sociales reçues)."
  - question: "D'où viennent ces chiffres ?"
    answer: "De l'enquête européenne sur les revenus et les conditions de vie (EU-SILC), jeu ilc_mdes04 d'Eurostat (séries depuis 2004 pour la France et 2010 pour l'Union européenne, jusqu'à {imp.annee}), relevé par un script qui s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases de la page. Seul le montant de la question de l'enquête {imp.annee}, {imp.montant_question} € en France, est transcrit d'une publication de l'Insee. Les données sont téléchargeables en CSV et en JSON, sous licence CC BY 4.0."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  conception: "docs/conception/qui-peut-faire-face-a-une-depense-imprevue.md"  # fiche de conception (regle 12)
  refonte: "2026-11-12"  # page de données nouvelle : née refondue (relecture attestée du jour)
  bloc: "guides"
  livres: ["la-societe-du-premier-coup"]  # livre que la page prolonge (fiche du livre, « Ressources et données du livre »)
  rang: 40
  nature: "Données officielles recalculées (Eurostat, EU-SILC)"
reperes:  # trois repères sous le chapô, à partir de 600 px de large (partials/reperes-page.html ; règle 17 du site,
  # reprise du style du 13/11/2026, test du premier écran). Chacun reprend un résultat écrit dans sa section, avec sa
  # période et sa réserve. Aucun nombre saisi : jetons {imp.*} (scripts/update_menages_imprevu.py). Pas de repère pour
  # l'Union européenne : la question française porte sur un montant plus bas (limites de la page).
  - ancre: "qui"
    fort: "{imp.total} %"
    texte: "des personnes vivant en France font partie, en {imp.annee}, d'un ménage qui déclare ne pas pouvoir faire face, par ses seuls moyens, à une dépense imprévue de {imp.montant_question} €"
  - ancre: "qui"
    fort: "{imp.dessous} %"
    texte: "des personnes sous le seuil de pauvreté ne pourraient pas faire face à la dépense, contre {imp.dessus} % de celles qui vivent au-dessus, en {imp.annee}"
  - ancre: "test"
    fort: "{imp.ps_dessus} %"
    texte: "des personnes vivant dans un foyer monoparental ne pourraient pas faire face à la dépense, contre {imp.c1_dessus} % de celles vivant dans un foyer de deux adultes avec un enfant, dans les deux cas au-dessus du seuil de pauvreté, en {imp.annee} : un écart entre deux groupes, qui ne mesure pas ce qui arriverait si un foyer passait de deux adultes à un seul"
---

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< imp-val "date_donnees" >}}</span> Eurostat, enquête EU-SILC, jeu ilc_mdes04&nbsp;: France (séries depuis 2004) et Union européenne à&nbsp;27 (depuis 2010)&nbsp;; écarts étudiés de {{< imp-val "debut" >}} à {{< imp-val "annee" >}}. Télécharger&nbsp;: <a href="/menages_imprevu.csv">CSV</a> · <a href="/menages_imprevu.json">JSON</a></p>

## Qui ne pourrait pas faire face à une dépense imprévue&nbsp;? {#qui}

En France, en {{< imp-val "annee" >}}, {{< imp-val "total" >}}&nbsp;% des personnes vivent dans un ménage qui, selon ses propres déclarations, ne pourrait pas, par ses seuls moyens, faire face à une dépense imprévue de {{< imp-val "montant_question" >}}&nbsp;€&nbsp;: près de trois sur dix. L'écart est très marqué de part et d'autre du seuil de pauvreté&nbsp;:

<div class="grille-reperes" role="table" aria-label="Part des personnes dont le ménage ne pourrait pas faire face à une dépense imprévue, selon la position par rapport au seuil de pauvreté, France, {{< imp-val "annee" >}}">
<div class="grille-reperes__rang grille-reperes__tete" role="row"><span role="columnheader"></span> <span role="columnheader">en dessous du seuil de pauvreté</span> <span role="columnheader">au-dessus du seuil</span></div>
<div class="grille-reperes__rang" role="row"><span role="rowheader">ne pourraient pas faire face à la dépense, en {{< imp-val "annee" >}}</span> <span class="grille-reperes__val" role="cell"><b>environ deux tiers</b> <small>{{< imp-val "dessous" >}}&nbsp;%</small> <span class="barre-part" style="--v:{{< imp-val "dessous" "css" >}}"><i></i></span></span> <span class="grille-reperes__val" role="cell"><b>environ une sur cinq</b> <small>{{< imp-val "dessus" >}}&nbsp;%</small> <span class="barre-part" style="--v:{{< imp-val "dessus" "css" >}}"><i></i></span></span></div>
</div>

Mais être au-dessus ou en dessous du seuil ne dit pas tout. Au-dessus du seuil, là où le classement par le revenu dit «&nbsp;pas pauvre&nbsp;», les situations diffèrent nettement selon la composition du foyer.

<div class="figure-lecture">
<figure class="figure-ciseau">
  <picture>
    <source media="screen and (max-width: 899px)" srcset="/img/imprevu-menages-m.svg" width="300" height="833">
    <img src="/img/imprevu-menages.svg" alt="Barres horizontales, France {{< imp-val "annee" >}}, part des personnes dont le ménage déclare ne pas pouvoir faire face à une dépense imprévue de {{< imp-val "montant_question" >}} €, selon le type de foyer où elles vivent. Au-dessus du seuil de pauvreté : deux adultes sans enfant {{< imp-val "c0_dessus" >}} %, un adulte sans enfant {{< imp-val "seul_dessus" >}} %, deux adultes avec un enfant {{< imp-val "c1_dessus" >}} %, un adulte avec un ou plusieurs enfants {{< imp-val "ps_dessus" >}} %. En dessous du seuil, dans le même ordre : {{< imp-val "c0_dessous" >}} %, {{< imp-val "seul_dessous" >}} %, {{< imp-val "c1_dessous" >}} % et {{< imp-val "ps_dessous" >}} %. Association, non cause." width="720" height="363" loading="lazy">
  </picture>
  <figcaption>Part des personnes (et non des ménages), selon la déclaration du ménage&nbsp;; seuil de pauvreté&nbsp;: 60&nbsp;% du revenu disponible médian national par unité de consommation (Eurostat, EU-SILC).</figcaption>
</figure>
<div class="figure-lecture__texte">
<div class="resultat-phrase">

**Le résultat en une phrase.** En France, en {{< imp-val "annee" >}}, au-dessus du seuil de pauvreté, {{< imp-val "ps_dessus" >}}&nbsp;% des personnes vivant dans un foyer monoparental (un adulte avec un ou plusieurs enfants) ne pourraient pas faire face à une dépense imprévue de {{< imp-val "montant_question" >}}&nbsp;€, contre {{< imp-val "c1_dessus" >}}&nbsp;% de celles vivant dans un foyer de deux adultes avec un enfant, soit {{< imp-val "ecart_enf" >}} d'écart.

</div>
</div>
</div>

## Ce que la comparaison permet&nbsp;— et ne permet pas&nbsp;— de dire {#test}

Être au-dessus du seuil de pauvreté ne garantit pas de pouvoir absorber une dépense imprévue. Parmi les personnes situées au-dessus de ce seuil en France en {{< imp-val "annee" >}}, {{< imp-val "ps_dessus" >}}&nbsp;% de celles vivant dans un foyer d'un adulte avec un ou plusieurs enfants ne pourraient pas, selon la déclaration de leur ménage, faire face à une dépense de {{< imp-val "montant_question" >}}&nbsp;€, contre {{< imp-val "c1_dessus" >}}&nbsp;% de celles vivant dans un foyer de deux adultes avec un enfant. L'écart est de {{< imp-val "ecart_enf" >}}.

Il décrit deux groupes&nbsp;: il ne mesure pas ce qui arriverait à une personne si son foyer passait de deux adultes à un seul. Ces groupes peuvent aussi différer par leur revenu exact au-dessus du seuil, le nombre et l'âge des enfants, l'emploi, les dépenses contraintes et les aides sociales reçues. Les données publiées ici ne permettent pas de départager ces explications. Au-dessus du seuil, la série permet d'autres comparaisons&nbsp;:

- **Avec des enfants**, l'écart entre les foyers d'un adulte avec un ou plusieurs enfants et ceux de deux adultes avec un enfant est compris chaque année, depuis {{< imp-val "debut" >}}, entre {{< imp-val "plage_enf_bas" >}} et {{< imp-val "plage_enf_haut" >}}&nbsp;points.
- **Sans enfant**, l'écart entre foyers d'un et de deux adultes n'est que de {{< imp-val "ecart_sans" >}} en {{< imp-val "annee" >}} (entre {{< imp-val "plage_sans_bas" >}} et {{< imp-val "plage_sans_haut" >}}&nbsp;points chaque année sur la même période).
- **Comparé aux foyers de deux adultes avec deux enfants**, l'écart des foyers d'un adulte avec un ou plusieurs enfants est encore de {{< imp-val "ecart_enf2" >}} en {{< imp-val "annee" >}}. La comparaison ne mesure pas pour autant l'effet du nombre d'enfants&nbsp;: la catégorie d'Eurostat que la page appelle «&nbsp;foyer monoparental&nbsp;» réunit tout ménage d'un seul adulte avec un ou plusieurs enfants dépendants (moins de 18 ans, ou de 18 à 24 ans s'ils sont inactifs et vivent avec un parent), et celle des foyers de deux adultes, tout ménage de deux adultes, couple ou non.

Au-dessus du seuil, l'écart entre foyers d'un et de deux adultes est donc deux à trois fois plus grand avec des enfants que sans. Il persiste chaque année depuis {{< imp-val "debut" >}}, mais il ne permet pas d'isoler l'effet propre de la composition du foyer&nbsp;: le nombre et l'âge des enfants, l'emploi, les dépenses contraintes et les aides sociales reçues peuvent aussi différer entre ces foyers.

En dessous du seuil, l'écart entre foyers monoparentaux et foyers de deux adultes avec un enfant est plus étroit ({{< imp-val "ecart_enf_dessous" >}} en {{< imp-val "annee" >}})&nbsp;: dans les uns comme dans les autres, une grande majorité des personnes ne pourraient pas faire face à une dépense imprévue. Être au-dessus ou en dessous du seuil ne suffit donc pas à expliquer ces écarts.

**Ce que la comparaison ne tranche pas.** Au-dessus du seuil, les foyers monoparentaux pourraient être en moyenne plus proches du seuil que les foyers de deux adultes avec un enfant. Le jeu d'Eurostat ne dit pas à quelle distance du seuil se situe le revenu de chaque foyer&nbsp;; il ne permet donc pas de séparer ce que pèse la composition du foyer de ce que pèse cette distance.

## Le même constat dans l'Union européenne {#europe}

Dans l'Union européenne à&nbsp;27, {{< imp-val "ue_total" >}}&nbsp;% des personnes ne pourraient pas faire face à une dépense imprévue en {{< imp-val "annee" >}}. Au-dessus du seuil de pauvreté, l'écart entre les foyers d'un adulte avec un ou plusieurs enfants et ceux de deux adultes avec un enfant est de {{< imp-val "ue_ecart_enf" >}} (entre {{< imp-val "ue_plage_enf_bas" >}} et {{< imp-val "ue_plage_enf_haut" >}}&nbsp;points chaque année depuis {{< imp-val "debut" >}}), contre {{< imp-val "ue_ecart_sans" >}} entre foyers d'un et de deux adultes sans enfant (entre {{< imp-val "ue_plage_sans_bas" >}} et {{< imp-val "ue_plage_sans_haut" >}}&nbsp;points). Le constat n'est pas propre à la France.

## Ce que ces données ne disent pas {#limites}

- **Une déclaration, pas un compte en banque.** La question porte sur la capacité perçue du ménage à payer une dépense imprévue sans aide extérieure ni nouvel emprunt&nbsp;; elle ne mesure ni l'épargne ni les actifs disponibles.
- **Un montant plus bas que celui de la règle commune.** En France, l'enquête de {{< imp-val "annee" >}} porte sur une dépense de {{< imp-val "montant_question" >}}&nbsp;€ (Insee). Le guide d'Eurostat fixe ce montant, pays par pays, au douzième du seuil de pauvreté tiré de l'enquête menée deux ans plus tôt, arrondi à 5&nbsp;% près&nbsp;: environ {{< imp-val "douzieme" >}}&nbsp;€ pour la France en {{< imp-val "annee" >}}, sur le seuil de {{< imp-val "annee_seuil" >}}. La question française porte donc sur une somme plus faible, ce qui compte quand on compare la part française à celle d'autres pays. Elle ne biaise pas la comparaison entre ménages français d'une même année, qui répondent tous à la même question&nbsp;; mais l'ampleur des écarts peut dépendre du montant demandé, qui a pu changer d'une année à l'autre.
- **Des personnes, pas des ménages.** Les parts sont calculées sur les personnes&nbsp;: un enfant d'un ménage qui ne pourrait pas faire face à la dépense est compté parmi les personnes concernées.
- **Le seuil de pauvreté est relatif.** Il vaut 60&nbsp;% du revenu disponible médian national, après transferts sociaux, par unité de consommation&nbsp;; il tient compte de la taille et de la composition du ménage, pas de la réserve dont celui-ci dispose.
- **Une association, non une cause.** Le graphique montre que la composition du foyer et l'incapacité à faire face à une dépense imprévue vont ensemble, pas que l'une produit l'autre&nbsp;; la distance au seuil n'est pas prise en compte.
- **Une marge d'erreur non publiée.** Eurostat ne publie pas d'intervalle de confiance pour ces sous-groupes&nbsp;; aucune des valeurs utilisées n'est signalée par Eurostat comme peu fiable, mais celles de l'Union européenne antérieures à 2019 sont signalées comme estimées. Cette absence de signalement ne dit pas qu'un écart de quelques dixièmes de point est significatif&nbsp;: la page ne commente que des écarts de plusieurs points, sans pouvoir dire, faute d'intervalle publié, à partir de quelle taille un écart entre ces petits groupes est sûr.
- **Des ruptures de série.** Eurostat signale des ruptures en France en {{< imp-val "ruptures_fr" >}}&nbsp;: les fourchettes sur plusieurs années se lisent avec prudence. Le constat principal compare des types de foyer la même année, et ces ruptures ne l'atteignent pas.

<aside class="encadre">

**Une hypothèse de l'auteur, non testée ici.** Dans le working paper [AWP-08](/awp/awp-08/), l'économiste Stéphane Lalut propose de lire la capacité individuelle de repli comme l'une des trois composantes de ce qu'il appelle la [réversibilité sociale](/reversibilite-sociale/)&nbsp;: ce qu'une personne peut se permettre de rater sans fermer durablement son avenir. L'indicateur de cette page, fondé sur la déclaration du ménage, ne saisit que le volet financier de cette capacité&nbsp;; il ne dit rien du coût d'un échec ni de la possibilité de recommencer.

</aside>

{{< appel-livre slug="la-societe-du-premier-coup" sur="Pour prolonger la question" avis="non" >}}
*La Société du premier coup* raconte, à partir de cas concrets, ce que coûte un échec selon la position sociale de celui qui le subit, et pourquoi certains ne peuvent pas se permettre d'essayer.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## Sources {#sources}

- Eurostat, enquête européenne sur les revenus et les conditions de vie (EU-SILC), jeu [ilc_mdes04](https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes04/default/table) («&nbsp;Incapacité à faire face à des dépenses financières imprévues&nbsp;»), relevé par l'API de diffusion. Calculs de l'auteur&nbsp;: écarts entre compositions de ménage, fourchettes des écarts annuels.
- Montant de la question&nbsp;: Insee, communiqué du [31&nbsp;janvier 2025](https://www.insee.fr/fr/information/8348643) lançant l'enquête SRCV, volet français d'EU-SILC («&nbsp;Êtes-vous en mesure de faire face à une dépense imprévue d'un montant de 1&nbsp;000&nbsp;euros&nbsp;?&nbsp;»)&nbsp;; règle commune&nbsp;: Eurostat, *EU-SILC Methodological guidelines, 2025 operation*, variable HS060, p.&nbsp;154&nbsp;; seuil de pauvreté d'une personne seule&nbsp;: Eurostat, jeu [ilc_li01](https://ec.europa.eu/eurostat/databrowser/view/ilc_li01/default/table), relevé par le script.

{{< reutiliser figures="figures_imprevu" jeu="menages_imprevu" sources="Eurostat (EU-SILC)" donnees="La part des personnes incapables de faire face à une dépense imprévue, pour la France et l'Union européenne à 27, par composition du ménage et position par rapport au seuil de pauvreté, chaque année depuis 2004 pour la France et 2010 pour l'Union européenne ; le même contenu existe en CSV, au format long, avec les annotations d'Eurostat (colonne statut_eurostat : e, valeur estimée ; b, rupture de série)." >}}
En France, en {{< imp-val "annee" >}}, au-dessus du seuil de pauvreté, la part des personnes dont le ménage déclare ne pas pouvoir faire face à une dépense imprévue de {{< imp-val "montant_question" >}}&nbsp;€ est plus de deux fois plus élevée chez les personnes vivant dans un foyer monoparental que chez celles vivant dans un foyer de deux adultes avec un enfant. Au-dessus du seuil, chaque année depuis {{< imp-val "debut" >}}, l'écart entre foyers d'un et de deux adultes est deux à trois fois plus grand quand il y a des enfants qu'en leur absence&nbsp;; c'est une association, non un effet mesuré de la composition du foyer. Être au-dessus du seuil de pauvreté ne dit donc pas tout de la capacité à faire face à une dépense imprévue.
{{< /reutiliser >}}
