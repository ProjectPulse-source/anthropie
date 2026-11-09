---
title: "Peut-on changer les règles du jeu de la dette publique ?"
description: "À politique inchangée, la Commission européenne projette une dette publique française de {futurs.ref_2030} % du PIB en 2030 et {futurs.ref_2035} % en 2035. {futurs.n_operations_maj} façons de changer les règles du jeu, de l'ajustement budgétaire à la restructuration : ce que chacune change, qui la décide, qui en porte le coût."
chapo: "Oui, mais sans effet automatique : selon son mécanisme et ses conditions, une même opération peut réduire la dette, déplacer des charges ou des risques vers d'autres, ou l'aggraver. À politique inchangée, la Commission européenne projette une dette publique française de {futurs.ref_2030} % du PIB en 2030 et de {futurs.ref_2035} % en 2035 ; changer les règles du jeu ne modifie cette trajectoire qu'en passant par le solde budgétaire, les taux, la croissance ou le stock de dette, et les {futurs.n_operations} façons de le faire examinées ici ne relèvent ni des mêmes décideurs ni des mêmes accords."
og_title: "Peut-on changer les règles du jeu de la dette publique ?"
og_image: "images/og-dette-futurs.jpg"
og_image_alt: "Carte de partage : « Dette publique : quels futurs ? » — éventail des projections de la Commission européenne pour la dette française jusqu'en 2030, trajectoire à politique inchangée et prévision du Gouvernement."
date: 2026-11-09
lastmod: 2026-11-09
# Volet 6 du dossier dette (onglet « Quels futurs ? »), ouvert le 09/11/2026 (commande /dette-quels-futurs ; pièce Dette-02).
# Fiche de conception : docs/conception/dette-publique-quels-futurs.md ; arbitrages PRO-20261109-063209, ENTRANTE Dette-04,
# PRO-20261109-075318, PRO-20261109-092834, ENTRANTE Dette-07, PRO-20261109-095636, PRO-20261109-104650.
# Décisions verrouillées : scénario ≠ prévision ; aucune recommandation ; probabilités = celles de la Commission, jamais
# attribuées à un choix politique ; leviers de solde en calcul comptable ; l'hypothèse de l'auteur dans un bloc séparé.
# Aucun chiffre saisi : jetons {futurs.*}, shortcodes futurs-val et futurs-matrice (scripts/update_dette_futurs.py et
# scripts/matrice_dette_futurs.py). Les années d'horizon (2025, 2030, 2035) sont celles du générateur, qui les fixe : une
# nouvelle édition du DSM demande une phase B du générateur, et de cette page.
donnees: [dette_futurs]
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_futurs"
  nom: "Quels futurs pour la dette publique française : projections de la Commission européenne, trajectoires du Gouvernement, sensibilités et matrice institutionnelle"
  description: "Trajectoire de la dette publique française à politique inchangée et distribution stochastique publiées par la Commission européenne (Debt Sustainability Monitor 2025), engagements et prévisions du Gouvernement (plan d'octobre 2024, PLF 2027) placés dans cette distribution, sensibilités au solde, aux taux et à la croissance calculées sur la référence de la Commission, et matrice institutionnelle de neuf opérations (ce qui change, effet, qui décide, droit applicable, répartition, robustesse, issue), en français et en anglais."
  couverture_temporelle: "2024/2036"
  couverture_spatiale: "France"
  variables:
    - {nom: "Dette publique (Maastricht)", unite: "% du PIB", description: "référence à politique inchangée, variantes et centiles de la Commission ; prévisions du Gouvernement"}
    - {nom: "Centile atteint", unite: "centile", description: "position d'une trajectoire du Gouvernement dans la distribution de la Commission, en niveau et en variation depuis 2025"}
    - {nom: "Sensibilité", unite: "points de PIB ou milliards d'euros", description: "écart à la référence en 2030 et 2035, un paramètre modifié à la fois"}
    - {nom: "Matrice institutionnelle", unite: "texte", description: "neuf opérations × sept dimensions, statut de source par case"}
  sources:
    - "https://economy-finance.ec.europa.eu/publications/debt-sustainability-monitor-2025_en"
    - "https://www.budget.gouv.fr/documentation/documents-budgetaires"
    - "https://www.aft.gouv.fr/fr/encours-detaille-oat"
  mots: ["dette publique", "France", "projections", "Commission européenne", "Debt Sustainability Monitor", "règles budgétaires", "euro-obligations", "restructuration", "clauses d'action collective", "règle d'or"]
  fichiers: ["dette_futurs.csv", "dette_futurs.json", "dette_futurs_matrice.csv"]
faq:
  - question: "Quelle sera la dette publique française en 2030 ?"
    answer: "Personne ne le sait : les chiffres disponibles sont des projections conditionnelles. À politique inchangée, la Commission européenne projette {futurs.ref_2030} % du PIB en 2030 ; sous des chocs comparables à ceux du passé, dans 80 % des simulations de la Commission la dette serait entre {futurs.p10_2030} % et {futurs.p90_2030} %. Le Gouvernement prévoit {futurs.plf_2030} % dans le projet de loi de finances pour 2027, une trajectoire qui suppose des mesures nouvelles."
  - question: "Annuler la dette détenue par la Banque de France ferait-il baisser la dette ?"
    answer: "Une annulation qui éteint la créance baisserait la dette mesurée ; une conversion en titres perpétuels sans intérêt qui garde la valeur nominale ne la baisserait pas nécessairement. Dans les deux cas, l'économie nette n'est pas acquise : le coût des réserves des banques, rémunérées par la banque centrale, demeure et change de porteur. Et, en l'état des traités, l'État ne peut pas imposer l'opération : ni la BCE ni la Banque de France ne peuvent recevoir d'instructions d'un gouvernement."
  - question: "Une restructuration de la dette française serait-elle légale ?"
    answer: "Les titres d'État de plus d'un an créés depuis 2013 portent des clauses d'action collective : l'État peut modifier leurs conditions avec des majorités qualifiées de détenteurs, comptées en principal ; pour une modification substantielle d'une seule ligne, les trois quarts du principal présent ou représenté, à condition que les deux tiers du principal en circulation soient présents ou représentés, et d'autres règles pour plusieurs lignes (art. D. 213-25-12 et D. 213-25-13 du code monétaire et financier). Selon notre reconstitution des fiches de l'Agence France Trésor, {futurs.cac_part} % de l'encours nominal non indexé des obligations relève de ces lignes. Ces clauses rendent une modification possible ; elles ne garantissent ni l'accord des créanciers ni l'absence de hausse des taux ensuite."
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["quantitatif", "juridique-institutionnel"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  refonte: "2026-11-09"  # page de données neuve : naît refondue ; instantané de relecture à faire après la relecture attestée
  conception: "docs/conception/dette-publique-quels-futurs.md"  # fiche de conception (règle 12)
  bloc: "dette"
  livres: ["dette-publique-qui-paie-vraiment"]
  rang: 36
  nature: "Projections de la Commission européenne, prévisions du Gouvernement, textes juridiques lus et calculs de l'auteur"
---

{{< dossier-dette volet="futurs" >}}

{{< reutiliser-ancre >}}

<p class="donnees-ligne"><span class="badge-donnees">Données mises à jour le {{< futurs-val "date_donnees" >}}</span> Projections de la Commission européenne publiées le {{< futurs-val "dsm_publie" >}}, prévisions du projet de loi de finances pour 2027. Télécharger&nbsp;: <a href="/dette_futurs.csv">CSV</a> · <a href="/dette_futurs.json">JSON</a> · <a href="/dette_futurs_matrice.csv">matrice (CSV)</a> · <a href="#sources">méthode</a></p>

<div class="futurs-carte">

**Trois questions pour examiner chaque opération.** Une dette peut disparaître d'un bilan sans que disparaissent les obligations, les coûts ou les risques qui lui étaient attachés&nbsp;; une réforme peut aussi produire un gain réel. Pour distinguer les deux, chaque opération examinée ici passe par les mêmes questions.

- **Quel effet&nbsp;?** Réduire le ratio de dette, alléger les intérêts ou transférer une obligation ne produisent pas le même résultat.
- **Qui décide&nbsp;?** Selon l'opération&nbsp;: le Gouvernement et le Parlement, sous surveillance européenne, ou l'accord du Conseil de l'Union, de la banque centrale, de chacun des États membres ou des créanciers.
- **Qui paie&nbsp;?** Les contribuables visés, les détenteurs de titres et leurs épargnants, d'autres États ou les années suivantes.

[Les neuf opérations, en trois familles&nbsp;→](#matrice)

</div>

## Où mène la trajectoire actuelle&nbsp;? {#trajectoire}

Trois sortes de chiffres circulent sur l'avenir de la dette, et ils ne disent pas la même chose. La Commission européenne projette la dette **à politique inchangée**&nbsp;: sans mesure nouvelle, ce que deviendrait le ratio avec les seules décisions déjà prises. Ce n'est ni une prévision ni le scénario le plus probable, elle l'écrit elle-même. La Commission n'est pas un observateur extérieur&nbsp;: elle veille au respect des règles budgétaires européennes. Sa référence sert ici d'étalon commun parce qu'elle est publiée, datée et reproductible, non parce qu'elle serait neutre. Le Gouvernement publie des **engagements**, en octobre 2024 dans son plan budgétaire et structurel à moyen terme, et des **prévisions**, en 2026 dans le rapport sur la dette annexé au projet de loi de finances pour 2027&nbsp;: elles supposent des mesures qui ne sont pas toutes votées. Cette page ajoute la troisième sorte, des **sensibilités**&nbsp;: ce que changerait un seul paramètre, sur la référence de la Commission.

{{< figure-svg fichier="dette-futurs-eventail" alt="Éventail des projections de la dette publique française de 2025 à 2030 : trois bandes emboîtées, du 10e au 90e, du 20e au 80e et du 40e au 60e centile, la trajectoire à politique inchangée de la Commission qui monte au centre, la prévision du Gouvernement qui monte jusqu'en 2028 puis redescend vers le bas de l'éventail, et l'engagement d'octobre 2024, plus bas." >}}Dette publique de la France, en&nbsp;% du PIB&nbsp;: distribution des trajectoires simulées par la Commission européenne (centiles 10 à 90), trajectoire à politique inchangée, prévision du PLF 2027 et engagement d'octobre 2024. Ces trajectoires ne partent pas du même point en 2025 et ne supposent pas les mêmes politiques.{{< /figure-svg >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** À politique inchangée, la Commission projette une dette de {{< futurs-val "ref_2030" >}}&nbsp;% du PIB en 2030, contre {{< futurs-val "ref_2025" >}}&nbsp;% en 2025, et juge à {{< futurs-val "proba_2030_pct" >}}&nbsp;% la probabilité que la dette de 2030 dépasse celle de 2025.

</div>

**Lire l'éventail.** La prévision du Gouvernement, {{< futurs-val "plf_2030" >}}&nbsp;%, se place dans la moitié basse de cet éventail, vers le {{< futurs-val "plf_2030_c_niv" >}}<sup>e</sup>&nbsp;centile&nbsp;: environ {{< futurs-val "plf_2030_c_niv" >}}&nbsp;% des trajectoires simulées finissent plus bas. Les deux exercices n'ont toutefois ni les mêmes politiques, ni les mêmes points de départ, ni les mêmes hypothèses économiques&nbsp;: ce rang ne mesure ni l'effet propre des décisions du Gouvernement ni leur probabilité de réussite. Si l'économie connaît des à-coups de croissance, de taux et de budget semblables à ceux que la France a déjà connus, la dette de 2030 se situerait, dans 80&nbsp;% des simulations de la Commission, entre {{< futurs-val "p10_2030" >}}&nbsp;% et {{< futurs-val "p90_2030" >}}&nbsp;% du PIB, un écart de {{< futurs-val "ecart_p90_p10" >}} points&nbsp;: ce sont les bandes de la figure, que la Commission calcule jusqu'en 2030. Ces probabilités, celles du modèle de la Commission, supposent l'absence de mesures nouvelles. Elles ne mesurent pas la probabilité qu'un gouvernement tienne ses engagements, et cette page n'en attribue aucune à un choix politique. Au-delà de 2030, la Commission ne publie plus d'éventail&nbsp;: sa projection à politique inchangée atteint {{< futurs-val "ref_2035" >}}&nbsp;% en 2035.

**Engagement de 2024, prévision de 2026.** En octobre 2024, le Gouvernement s'engageait sur une dette de {{< futurs-val "psmt_2027" >}}&nbsp;% du PIB en 2027&nbsp;; en 2026, il en prévoit {{< futurs-val "plf_2027" >}}&nbsp;%, {{< futurs-val "ecart_promesse_2027" >}} points de plus, deux ans après l'engagement.

<details class="repli"><summary>Où se placent ces trajectoires dans l'éventail de la Commission</summary>

Placé dans l'éventail de la Commission, l'engagement de 2024 pour 2029, {{< futurs-val "psmt_2029" >}}&nbsp;%, tombe sous le 10<sup>e</sup>&nbsp;centile en niveau. Mais il partait de plus bas&nbsp;: les trois trajectoires ne partent pas du même point en 2025 ({{< futurs-val "ref_2025" >}}&nbsp;% pour la Commission, {{< futurs-val "plf_2025" >}}&nbsp;% dans le PLF 2027, {{< futurs-val "psmt_2025" >}}&nbsp;% dans le plan de 2024). Mesuré en variation depuis 2025, le même engagement se place vers le {{< futurs-val "psmt_2029_c_var" >}}<sup>e</sup>&nbsp;centile, et la prévision du PLF 2027 pour 2030 vers le {{< futurs-val "plf_2030_c_var" >}}<sup>e</sup>. Le rang d'une trajectoire dans l'éventail dépend donc aussi de son point de départ.

</details>

## Ce que changent le solde, les taux et la croissance {#leviers}

Une trajectoire de dette ne bouge que par quatre canaux&nbsp;: le solde primaire, c'est-à-dire les recettes moins les dépenses hors intérêts, le taux d'intérêt payé sur la dette, la croissance du PIB nominal, et les opérations sur le stock de dette lui-même. Toute réforme, y compris un changement de règle, n'agit sur la trajectoire qu'à travers eux. La figure applique à la référence de la Commission un seul changement à la fois.

{{< figure-svg fichier="dette-futurs-leviers" alt="Barres horizontales de l'écart de dette en 2035 par rapport à la référence de la Commission, regroupées en trois familles : solde primaire, conditions de financement et activité économique. Un solde primaire supérieur d'un point de PIB chaque année abaisserait le plus la dette, par un calcul comptable dessiné en contour pointillé ; des taux plus bas de 0,2 point l'abaisseraient peu ; des taux plus hauts d'un point ou une croissance plus faible d'un demi-point la relèveraient à peu près autant qu'une croissance plus forte l'abaisserait." >}}Écart de dette publique en 2035 par rapport à la référence de la Commission européenne, en points de PIB, un paramètre modifié à la fois (calculs de l'auteur sur la référence du Debt Sustainability Monitor 2025).{{< /figure-svg >}}

**Le solde.** Un solde primaire supérieur d'un point de PIB chaque année de 2028 à 2035 abaisserait la dette de {{< futurs-val "solde_2030_pts" >}} en 2030 et de {{< futurs-val "solde_2035_pts" >}} en 2035. C'est un calcul comptable&nbsp;: il suppose que l'ajustement ne freine pas la croissance et ne change pas les taux, ce qu'il ferait en partie. Un point de PIB d'investissement emprunté chaque année, sans effet sur la croissance, ferait l'inverse&nbsp;: {{< futurs-val "invest_2035_pts" >}} de plus.

**Les taux.** Des taux de marché plus bas de 0,2&nbsp;point (vingt points de base) sur tous les nouveaux emprunts publics abaisseraient la dette de {{< futurs-val "taux20_2035_pts" >}} en 2035 et la charge d'intérêts d'environ {{< futurs-val "taux20_int_2035" >}}&nbsp;milliards d'euros cette année-là&nbsp;; de dix points de base, de {{< futurs-val "taux10_2035_pts" >}}. Une hausse d'un point la relèverait de {{< futurs-val "taux100_2035_pts" >}}, et la charge d'intérêts d'environ {{< futurs-val "taux100_int_2035" >}}&nbsp;milliards. L'effet est lent&nbsp;: un taux de marché ne touche d'abord que la dette à court terme et les titres émis dans l'année, puis le reste à mesure qu'il est renouvelé.

**La croissance.** Un demi-point de croissance nominale de plus chaque année abaisserait la dette de {{< futurs-val "croiss_plus_2035_pts" >}} en 2035&nbsp;; un demi-point de moins la relèverait de {{< futurs-val "croiss_moins_2035_pts" >}}. La croissance n'est pas une décision&nbsp;: c'est une hypothèse, qui module toutes les autres. Elle joue avec le taux&nbsp;: par simple arithmétique de la dette, à solde primaire nul et hors ajustements flux-stock, le ratio monte quand le taux d'intérêt moyen de la dette dépasse la croissance nominale et baisse dans le cas inverse&nbsp;; un déficit primaire ou des ajustements flux-stock peuvent toutefois inverser ce résultat. Le progrès technique entre dans la croissance comme l'un de ses déterminants possibles&nbsp;; cette page ne lui attribue aucun effet propre chiffré.

Ces barres ne se comparent pas comme des efforts équivalents&nbsp;: un point de solde primaire est un effort budgétaire à renouveler chaque année, alors qu'un taux ou une croissance ne se décrètent pas. Elles disent l'ordre de grandeur de chaque canal, non ce qu'une politique coûterait ni ce qu'elle rapporterait.

<details class="repli"><summary>Comment ces sensibilités sont calculées, et contre quoi elles ont été testées</summary>

Le calcul reprend la dynamique de la dette décrite par la Commission dans l'annexe de son Debt Sustainability Monitor&nbsp;: la dette à court terme suit le taux de marché dans l'année, la dette à long terme seulement à mesure qu'elle est renouvelée&nbsp;; un choc de solde passe par un multiplicateur budgétaire et une composante conjoncturelle, sauf dans les calculs comptables, où l'un et l'autre sont nuls. Avant d'écrire la page, le calcul a été confronté à deux variantes que publie la Commission (une hausse de l'écart entre taux et croissance, une crise financière)&nbsp;: il les reproduit dans les tolérances écrites d'avance, et une erreur volontaire sur la transmission des taux le fait échouer. Il a aussi été confronté à la sensibilité que publie l'Agence France Trésor pour une hausse d'un point de tous les taux&nbsp;: {{< futurs-val "aft_an2" >}}&nbsp;milliards d'euros d'intérêts la deuxième année, {{< futurs-val "aft_an5" >}} la cinquième, que le calcul retrouve à quelques pour cent près&nbsp;; la première année ({{< futurs-val "aft_an1" >}}&nbsp;milliards), non, à cause du calendrier des émissions&nbsp;: les effets de taux ne sont donc lus qu'à partir de la deuxième année. Aucun témoin extérieur n'existe pour un choc de solde durable&nbsp;: d'où le calcul comptable.

</details>

## Changer les règles&nbsp;: qui décide, qui paie&nbsp;? {#matrice}

Les propositions du débat promettent souvent d'alléger la dette autrement que par l'ajustement budgétaire. Les {{< futurs-val "n_operations" >}} opérations ci-dessous sont examinées une à une avec la même grille&nbsp;: ce qu'elles changent, leur effet quand il se calcule, qui les décide, et l'issue provisoire (contrainte réduite, déplacée vers d'autres, aggravée, ou dépendante de conditions nommées). Chaque ligne porte le statut de ce qu'elle affirme&nbsp;: un texte lu, un calcul, un résultat établi ailleurs sur ce site, une déduction, ou ce qui n'est pas établi. Le droit applicable, la répartition des coûts et la robustesse se déplient sous chaque fiche&nbsp;; le tableau complet se télécharge ([CSV](/dette_futurs_matrice.csv)).

{{< futurs-matrice >}}

## Ce que la matrice fait apparaître {#constats}

**Cinq distinctions pour comprendre ces opérations.** Les quatre canaux disent par où passe l'effet sur la dette&nbsp;; ces distinctions disent ce qu'il faut séparer pour juger chaque opération.

| Ce que l'opération modifie | Ce qu'il faut distinguer |
|---|---|
| Le flux budgétaire | l'effort de chaque année et sur qui il porte |
| Les règles européennes | la souplesse accordée et l'effet économique |
| Le financement commun | le coût de l'emprunt et le transfert du risque |
| Les titres existants | la baisse du stock comptable et le coût économique net |
| La monnaie | la redénomination, le change et les engagements juridiques |

**Une même réforme peut réduire la dette mesurée, déplacer des charges, modifier les risques ou produire des effets opposés, selon les conditions de sa mise en œuvre.** Sur les {{< futurs-val "n_operations" >}} opérations, aucune ne se classe une fois pour toutes&nbsp;: la plupart dépendent d'une condition que la grille nomme, le rendement d'un investissement, le coût effectif d'un emprunt commun, la réaction des créanciers ou des contribuables. Modifier les règles de la dette ne revient pas à choisir entre payer et ne pas payer&nbsp;: chaque opération modifie un ensemble de droits, d'obligations, de risques et de capacités.

**Changer les règles peut aussi changer qui décide.** Certaines opérations relèvent principalement des institutions françaises, sous surveillance européenne&nbsp;; d'autres exigent l'accord du Conseil de l'Union, de la banque centrale, de chacun des États membres ou des créanciers. La possibilité d'agir dépend autant de ces accords que du résultat économique recherché. Sur qui retombe le coût (contribuables visés, détenteurs de titres et leurs épargnants, autres États, années suivantes), chaque fiche le dit sous «&nbsp;Qui gagne, qui paie&nbsp;», dans son repli.

**L'ampleur économique d'une réforme ne dit pas sa difficulté juridique.** Exclure certaines dépenses du suivi européen des dépenses nettes passe par une modification de règlement, à la majorité qualifiée&nbsp;; un emprunt commun, même borné, par l'unanimité et l'approbation de chaque État&nbsp;; changer la définition du déficit de référence, par l'unanimité du Conseil.

**Le droit européen distingue trois choses que le débat confond&nbsp;:** la souplesse des trajectoires budgétaires (allonger l'ajustement, traiter l'investissement), l'emprunt européen (prêter à un État ou dépenser pour l'Union), et la prise en charge des engagements d'un autre État, que les traités encadrent strictement. Ce ne sont pas trois variantes d'une même réforme.

## Ce que ces projections ne disent pas {#limites}

- **Projection, prévision, sensibilité.** La référence de la Commission est une projection conditionnelle à politique inchangée, non une prévision du scénario le plus probable. Les trajectoires du Gouvernement sont des prévisions, qui reposent sur des hypothèses économiques et sur des mesures dont certaines restent à adopter. Les sensibilités changent un paramètre à la fois. Aucun de ces chiffres n'est une certitude.
- **Un levier à la fois.** Les sensibilités et la matrice prennent les opérations une à une&nbsp;; aucune combinaison n'est calculée, alors qu'un emprunt commun et une règle d'or, ou une restructuration et les taux suivants, interagissent.
- **Un ratio ne mesure pas le bien-être.** Une dépense peut alourdir le ratio et améliorer le patrimoine public ou éviter un coût futur&nbsp;; une cession peut l'alléger sans enrichir personne. Un écart en points de PIB n'est pas un montant versé.
- **Faisable n'est pas acceptable.** La matrice examine les conditions juridiques connues, les accords nécessaires et ce qui reste à établir&nbsp;; elle ne dit pas ce qu'une majorité accepterait.
- **Ce qui reste à lire.** La qualification statistique d'un titre perpétuel sans intérêt, les textes de l'Eurosystème sur une conversion, les arrêtés de création de trois lignes d'obligations indexées, l'article 65 du traité sur les exceptions à la libre circulation des capitaux et l'avis du Conseil d'État sur une imposition différentielle du patrimoine (2025) n'ont pas été lus&nbsp;: les fiches concernées le disent.

<div class="encadre">

**L'hypothèse de l'auteur, distincte des constats.** Les constats ci-dessus valent sans elle. L'auteur les lit à la lumière de l'anthropie, qu'il définit ainsi&nbsp;:

{{< canonical-definition >}}

Appliquée à la dette, cette hypothèse demande si une transformation du système d'endettement peut réduire la contrainte sans la transférer ailleurs&nbsp;: vers d'autres contribuables, d'autres créanciers, d'autres États ou d'autres années. La matrice ne la démontre pas&nbsp;; elle fournit, opération par opération, les éléments qui permettraient de l'éprouver.

</div>

<div class="retenir">

<p class="retenir__surtitre">Synthèse</p>

## Ce qu'il faut retenir {#retenir}

À politique inchangée, la Commission européenne projette une dette publique française de {{< futurs-val "ref_2030" >}}&nbsp;% du PIB en 2030 et {{< futurs-val "ref_2035" >}}&nbsp;% en 2035&nbsp;; la prévision du Gouvernement pour 2030, {{< futurs-val "plf_2030" >}}&nbsp;%, suppose des mesures nouvelles.

Une trajectoire ne change que par le solde primaire, les taux, la croissance ou le stock. Sur la référence de la Commission, un solde primaire supérieur d'un point de PIB chaque année de 2028 à 2035 réduirait le ratio de dette de {{< futurs-val "solde_2035_pts" >}} en 2035&nbsp;; une croissance nominale supérieure d'un demi-point par an, de {{< futurs-val "croiss_plus_2035_pts" >}}&nbsp;; des taux de marché inférieurs de vingt points de base, de {{< futurs-val "taux20_2035_pts" >}}. Ce sont des sensibilités conditionnelles, non les effets garantis d'une politique.

Changer les règles du jeu ne dispense d'aucun de ces canaux&nbsp;: selon l'opération, cela peut modifier les compétences et les accords nécessaires, et réduire la dette, en déplacer la charge ou l'aggraver. La matrice des {{< futurs-val "n_operations" >}} opérations le dit pour chacune, avec le statut de chaque affirmation.

</div>

## Questions fréquentes {#questions}

{{< faq-visible >}}

**Dans le dossier dette publique**

{{< pastilles label="Dans le dossier dette publique" >}}
- [La dette publique peut-elle baisser&nbsp;?](/dette-publique-peut-elle-baisser/)
- [Qui paie vraiment la dette publique&nbsp;?](/qui-paie-la-dette-publique/)
- [Annuler la dette détenue par la Banque de France&nbsp;?](/qui-paie-la-dette-publique/#annuler-banque-de-france)
- [Et ailleurs&nbsp;?](/dette-publique-comparaison-internationale/)
{{< /pastilles >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Les quatre scénarios, racontés sur dix ans" avis="non" >}}
Cette page pose côte à côte, sur une même référence, ce que changent les règles du jeu de la dette et qui en porte le coût. Le livre raconte quatre futurs possibles d'ici 2035, de la continuité à la rupture, et ce que chacun ferait peser sur les ménages, les épargnants et les créanciers. Ses ordres de grandeur reposent sur ses propres hypothèses, différentes de la référence de la Commission utilisée ici.
{{< /appel-livre >}}

## D'où viennent ces chiffres {#sources}

Commission européenne, *Debt Sustainability Monitor 2025* (Institutional Paper 332, publié le {{< futurs-val "dsm_publie" >}}), fiche France&nbsp;: trajectoire à politique inchangée, variantes déterministes et distribution stochastique, lues dans le tableur de la fiche, archivé avec son empreinte. Gouvernement&nbsp;: plan budgétaire et structurel à moyen terme 2025-2029 (octobre 2024) et rapport sur la dette des administrations publiques annexé au projet de loi de finances pour 2027, lus dans les documents archivés. Agence France Trésor&nbsp;: sensibilité de la charge d'intérêts à une hausse des taux, et fiches des lignes d'obligations (encours nominal et arrêté de création), relevées le 9&nbsp;novembre 2026. Textes juridiques lus sur EUR-Lex et Légifrance&nbsp;: traités, protocole n°&nbsp;12, règlement (UE) 2024/1263, décision 2020/2053, code monétaire et financier, arrêt Pringle de la Cour de justice&nbsp;; ils sont cités dans chaque fiche.

Les trajectoires de la Commission et du Gouvernement sont lues par le script dans les sources archivées&nbsp;; les sensibilités sont calculées par le même script, sur la référence de la Commission&nbsp;; la part des lignes soumises aux clauses d'action collective est recalculée sur le relevé archivé des fiches de l'Agence France Trésor. Les chiffres attribués à d'autres auteurs dans la matrice (Fonds monétaire international, Observatoire européen de la fiscalité, Institut de l'entreprise, Conseil d'analyse économique, comité d'évaluation de France Stratégie) sont transcrits de leurs publications, vérifiées contre les pièces archivées. Le script s'arrête si une donnée ne remplit plus les conditions dont dépendent les principales phrases de la page&nbsp;; leur formulation fait l'objet d'une relecture éditoriale.

{{< reutiliser figures="figures_futurs" jeu="dette_futurs" sources="Commission européenne, Gouvernement et Agence France Trésor" donnees="La trajectoire à politique inchangée, les variantes et la distribution stochastique de la Commission européenne pour la France, les engagements et prévisions du Gouvernement, les sensibilités calculées sur la référence de la Commission ; la matrice institutionnelle complète est un second fichier CSV." >}}
À politique inchangée, la Commission européenne projette une dette publique française de {{< futurs-val "ref_2030" >}}&nbsp;% du PIB en 2030 et de {{< futurs-val "ref_2035" >}}&nbsp;% en 2035&nbsp;; la prévision du Gouvernement pour 2030 ({{< futurs-val "plf_2030" >}}&nbsp;%) se place dans la moitié basse de l'éventail de ses projections. Une trajectoire ne change que par le solde primaire, les taux, la croissance ou le stock&nbsp;; selon l'opération, changer les règles du jeu peut modifier les compétences et les accords nécessaires, et réduire la dette, en déplacer la charge ou l'aggraver. La référence de la Commission est une projection à politique inchangée, la trajectoire du Gouvernement une prévision qui suppose des mesures nouvelles, les leviers des sensibilités&nbsp;: aucun de ces chiffres n'est une certitude.
{{< /reutiliser >}}
