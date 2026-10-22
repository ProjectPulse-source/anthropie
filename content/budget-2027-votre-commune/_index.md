---
title: "Budget 2027 : que sait-on réellement pour votre commune ?"
description: "Projet de loi de finances pour 2027 : ce que l'Assemblée nationale a décidé le {coll.plf_vote_date} pour les mesures visant les communes, ce qui peut encore les concerner, ce que le service financier peut vérifier dès maintenant et quand les montants seront connus. État du texte daté, sources primaires."
chapo: "Le {coll.plf_vote_date}, l'Assemblée nationale {coll.plf_vote_resume} : trois des cinq mesures que le projet déposé destinait aux collectivités, dont les deux plus importantes en montant, sont écartées à ce stade, sans l'être définitivement. Peuvent encore concerner la commune l'étalement du DILICO, la répartition de la DGF et toute mesure qui reviendrait. Elle peut vérifier dès maintenant ses comptes de 2024, son FCTVA et ses sommes mises en réserve ; ses montants pour 2027 viendront de la loi votée, puis des notifications."
date: 2026-10-22
lastmod: 2026-10-22
# Série « Votre commune face aux décisions de l'État » (auteur, 22/10/2026), ressource n° 1. Arbitrages de l'auteur :
# D:\PRO\06_PROMOTION\RECHERCHE_VOTRE_COMMUNE_2026-10-22\ARBITRAGE_1807_COMMUNES.md et ARBITRAGE_1924_COMMUNES-01.md
# (hiérarchie : trente secondes, puis dix minutes). État du texte : jetons {coll.plf_*}, tirés de
# scripts/sources_collectivites/plf_votes.json (citations verbatim des comptes rendus officiels, retrouvées par
# verifier_plf_votes.py) par scripts/update_dette_collectivites.py ; montants du projet lus dans son archive. Taux,
# seuils, millésimes et articles cités en clair : texte du projet déposé (PDF, SHA-256 132274b8…) et CGCT relu sur
# Légifrance le 22/10/2026. Une étape parlementaire = une entrée du registre + une ligne de journal.
og_title: "Budget 2027 : que sait-on réellement pour votre commune ? — S. Lalut"
og_image: "images/og-budget-2027-commune.jpg"
og_image_alt: "Carte de partage : « Budget 2027 : ce qu'il en reste » — les cinq mesures du projet de loi de finances déposé visant les collectivités, en milliards d'euros, évidées quand l'Assemblée nationale les a supprimées ou n'a pas adopté leur article."
donnees: [dette_collectivites]
dossier_source: "plf"   # barre du dossier : source = état du projet au Parlement (shortcode dossier-dette)
journal:
  - {date: 2026-10-22, texte: "Correction : les communes ne contribuent pas au DILICO de 2026 (seulement les intercommunalités, les départements et les régions) ; chaque reversement va pour 10 % à la péréquation, la collectivité contributrice récupère 90 % de sa contribution. Exemple chiffré corrigé."}
  - {date: 2026-10-22, texte: "Correction : la contribution progressive se serait assise sur les comptes de 2024 (antépénultième exercice), non de 2025 ; le reversement du DILICO 2025 porte sur les deux tiers restants, non sur le montant initial. Page réorganisée : l'essentiel en tête, le détail ensuite."}
  - {date: 2026-10-22, texte: "Publication : état du texte après la séance de l'Assemblée nationale du 19 octobre 2026."}
faq:
  - question: "Qu'a décidé l'Assemblée nationale le 19 octobre 2026 ?"
    answer: "En séance, le {coll.plf_vote_date}, elle {coll.plf_vote_resume} ; elle a porté la DGF nationale pour {coll.plf_edition} à {coll.plf_dgf_an} milliards d'euros. Ce sont des votes en première lecture : aucune de ces décisions n'est définitive."
  - question: "Quelles mesures pourraient encore concerner ma commune en 2027 ?"
    answer: "Celles de la seconde partie du projet, que l'Assemblée n'avait pas examinées au {coll.plf_etat_au} : l'étalement du reversement des sommes mises en réserve en 2025 (DILICO ; celui de 2026 ne vise que les intercommunalités, les départements et les régions), la répartition de la DGF et une nouvelle dotation pour les communes rurales de faible densité. Et toute mesure écartée qui serait rétablie d'ici la loi définitive."
  - question: "Quels chiffres ma commune peut-elle vérifier dès maintenant ?"
    answer: "Ses propres comptes, pas des montants pour 2027 : les sommes qu'elle a mises en réserve au DILICO en 2025, notifiées par arrêté (les communes n'y contribuent pas en 2026) ; le FCTVA qu'elle perçoit et l'année des dépenses sur laquelle il porte ; ses recettes réelles de fonctionnement de 2024, exercice qui aurait servi d'assiette à la contribution progressive si elle revenait."
  - question: "Quand ma commune connaîtra-t-elle ses montants pour 2027 ?"
    answer: "Après le vote définitif de la loi de finances : le préfet communique alors le montant de chacune des dotations de la DGF, et les mesures nouvelles passent par leurs arrêtés ou décrets. Prochaine étape au {coll.plf_etat_au} : {coll.plf_etape_suivante}."
dataset:  # JSON-LD Dataset (partials/schema-dataset-page.html) ; jetons résolus au build
  jeu: "dette_collectivites"
  nom: "Projet de loi de finances pour {coll.plf_edition} : mesures visant les collectivités et état du texte au Parlement"
  description: "Montants pour {coll.plf_edition} des cinq mesures du projet de loi de finances déposé visant les collectivités (exposés des motifs et avis du Haut Conseil des finances publiques, archivés avec leur empreinte), état de chaque article au Parlement tiré des comptes rendus officiels des séances, montant de la DGF adopté par l'Assemblée nationale en première partie. Compris dans le jeu « collectivités locales et finances publiques »."
  couverture_temporelle: "{coll.plf_edition}"
  couverture_spatiale: "France"
  variables:
    - {nom: "Montant de chaque mesure du projet déposé", unite: "milliards d'euros", description: "contribution progressive, FCTVA, TVA affectée, contributions de ministères, DILICO"}
    - {nom: "État de l'article au Parlement", unite: "texte daté", description: "supprimé, non adopté, adopté modifié ou non examiné, avec la séance"}
    - {nom: "DGF adoptée par l'Assemblée nationale en première partie", unite: "milliards d'euros"}
  sources:
    - "https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf"
    - "https://www.assemblee-nationale.fr/dyn/17/dossiers/PLF_2027"
    - "https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf"
  mots: ["projet de loi de finances 2027", "collectivités locales", "communes", "contribution progressive", "CPEB", "FCTVA", "DGF", "DILICO", "finances locales"]
  fichiers: ["dette_collectivites.csv", "dette_collectivites.json"]
ressource:  # index /ressources/ (layouts/ressources/list.html)
  type: ["juridique-institutionnel", "quantitatif"]  # protocole de la page (CLAUDE.md du site, « Production des ressources »)
  bloc: "dette"
  rang: 35
  nature: "Projet de loi, comptes rendus de séance et code, lus et datés"
  prolongement: true   # rangée « Prolongements du dossier », comme la page collectivités dont elle est la suite
  refonte: "2026-10-22"
  conception: "docs/conception/budget-2027-votre-commune.md"  # fiche de conception (regle 12)
dossier_dette: prolongement   # panneau « Prolongements » de la barre du dossier
dossier_dette_titre: "Budget 2027 : votre commune"
dossier_dette_role: "projet de loi, état du texte"
dossier_dette_titre_en: "Budget 2027: your municipality"
dossier_dette_role_en: "draft budget bill, state of the text"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<span id="questions-frequentes"></span>

## L'essentiel pour votre commune {#essentiel}

*État du projet de loi de finances pour {{< coll-val "plf_edition" >}} au {{< coll-val "plf_etat_au" >}}&nbsp;: aucune mesure n'est définitivement acquise ni définitivement écartée. Cette page est révisée à chaque étape qui modifie ces mesures&nbsp;; ses révisions restent lisibles en pied de page.*

{{< faq-visible >}}

## Ce que le service financier doit retenir, vérifier et en faire {#a-verifier}

{{< mesure-budget titre="Contribution progressive" art="37" statut="plf_statut_cpeb" retenir="Un prélèvement envisagé sur les recettes fiscales, chaque mois, si la mesure revenait" verifier="Les comptes de 2024 de la commune et de son intercommunalité&nbsp;; une éventuelle exonération (rangs DSU et DSR)" action="Ne pas l'inscrire comme une charge certaine&nbsp;; la garder en scénario conditionnel." >}}

{{< mesure-budget titre="FCTVA" art="35" statut="plf_statut_fctva" retenir="La baisse envisagée pouvait toucher des investissements déjà réalisés" verifier="L'année des dépenses sur laquelle porte l'attribution, et la part des dépenses de transition écologique et de voirie" action="Inscrire l'attribution au taux en vigueur&nbsp;; la baisse, en scénario conditionnel." >}}

{{< mesure-budget titre="DGF" art="34" statut="plf_statut_dgf" retenir="Une enveloppe nationale en hausse, sans garantie de hausse pour chaque commune" verifier="La composition de la DGF de la commune&nbsp;: dotation forfaitaire, dotations de péréquation" action="Ne pas lire la hausse nationale comme une recette garantie pour la commune." >}}

{{< mesure-budget titre="DILICO" art="84" statut="plf_statut_dilico" retenir="Des restitutions qui seraient étalées jusqu'en 2031, sans changer leur total&nbsp;; les communes ne sont concernées que par celui de 2025" verifier="Le montant mis en réserve par la commune en 2025, notifié par arrêté&nbsp;; pour 2026, celui de son intercommunalité" action="Préparer l'échéancier des reversements du DILICO 2025, selon le droit actuel et selon le projet." >}}

{{< mesure-budget titre="TVA affectée" art="36" statut="plf_statut_tva" retenir="Un écrêtement écarté à ce stade, d'effet différent selon les bénéficiaires" verifier="Une fraction de TVA perçue par la commune, ou par son intercommunalité" action="Inscrire la fraction selon les règles actuelles&nbsp;; l'écrêtement n'est plus dans le texte à ce stade." >}}

Prochaine échéance&nbsp;: {{< coll-val "plf_etape_suivante" >}}. Chaque ligne est développée [mesure par mesure](#mesure-par-mesure), avec ce qu'il serait trompeur de chiffrer à ce stade.

## Le projet déposé et ce qu'il en reste {#etat-du-texte}

{{< figure-svg fichier="collectivites-plf" alt="Cinq barres horizontales orange, en milliards d'euros : les mesures du projet de loi de finances déposé qui visent les collectivités. Les trois barres évidées, contribution progressive, baisse du FCTVA et écrêtement de la TVA, sont celles dont l'Assemblée nationale a supprimé ou n'a pas adopté l'article en séance ; les deux barres pleines, contributions de ministères et étalement du DILICO, relèvent de la seconde partie, non encore examinée." >}}Les cinq mesures du projet de loi de finances déposé qui visent les collectivités, et leur sort au Parlement. Montants du projet déposé&nbsp;: ils décrivent le cadrage initial, non l'état actuel du texte&nbsp;; leur somme arithmétique ne mesure pas un prélèvement net.{{< /figure-svg >}}

{{< fig-actions id="plf" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Le projet de loi de finances pour {{< coll-val "plf_edition" >}} déposé prévoyait cinq mesures visant les collectivités, d'une somme arithmétique de {{< coll-val "plf_somme" >}}&nbsp;milliards d'euros&nbsp;; le {{< coll-val "plf_vote_date" >}}, l'Assemblée nationale {{< coll-val "plf_vote_resume" >}}, sans qu'aucune soit définitivement écartée.

</div>

Cette somme décrivait le projet déposé&nbsp;; elle ne mesurait pas un prélèvement net, et [la page consacrée aux collectivités](/dette-publique-collectivites-locales/#projet-de-loi-de-finances) explique pourquoi elle coexistait avec une hausse prévue des ressources locales. Un article supprimé ou non adopté en séance ne figure plus dans le texte en discussion, mais il peut y revenir, par un amendement du Gouvernement ou au Sénat. À l'ouverture du débat du 19&nbsp;octobre, la ministre chargée des collectivités, Françoise Gatel, chiffrait à 5,5&nbsp;milliards d'euros la contribution des collectivités prévue par le projet.

<details class="repli"><summary>Le détail des cinq mesures du projet déposé&nbsp;: texte, nature, montant</summary>

{{< coll-tableau "plf" >}}

</details>

## Mesure par mesure {#mesure-par-mesure}

### La contribution progressive à l'effort budgétaire (article 37) {#cpeb}

**Ce que prévoyait le projet.** Une contribution de {{< coll-val "plf_cpeb" >}}&nbsp;milliards d'euros pour {{< coll-val "plf_edition" >}}, due selon l'exposé des motifs par {{< coll-val "plf_cpeb_communes_pct" >}}&nbsp;% des communes et par les intercommunalités, à un taux de 0,5&nbsp;% à 3&nbsp;% des recettes réelles de fonctionnement de 2024, retraitées, et prélevée chaque mois sur les douzièmes de fiscalité&nbsp;: un effet de trésorerie dès la notification. Un fonds de soutien de 50&nbsp;millions d'euros était prévu pour les communes contributrices en difficulté (article 87), dont le texte déposé renvoie encore à un «&nbsp;article X&nbsp;»&nbsp;: une référence non finalisée, et un fonds qui dépend du sort de la contribution.

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_cpeb" >}}. Si elle revenait, le montant de chaque collectivité serait fixé par un arrêté publié au Journal officiel.

**Ce que cela signifie pour une commune.** Rien n'est dû en l'état du texte. La commune et son intercommunalité étaient visées par deux contributions distinctes&nbsp;; ce que celle de l'intercommunalité ferait peser sur ses membres dépendrait de leurs relations financières, que le texte ne règle pas.

**Ce que le service financier peut vérifier dès maintenant.** Les recettes réelles de fonctionnement du budget principal de 2024, l'exercice qui aurait servi d'assiette, en sachant que l'assiette légale en retranche les atténuations de produits, les recettes exceptionnelles et les mises à disposition de personnel facturées à l'intercommunalité&nbsp;; les rangs de la commune dans les classements de la dotation de solidarité urbaine et de la fraction cible de la dotation de solidarité rurale, qui ouvraient une exonération.

**Ce qu'il serait trompeur de chiffrer.** Un montant&nbsp;: le taux dépend du rang de la commune parmi toutes les autres. Plusieurs cabinets de conseil et associations d'élus l'ont simulé sur le texte initial&nbsp;; ces simulations décrivent un article supprimé à ce stade, et les associations qui les publient ont demandé sa suppression ou sa réduction. Entre 0,5&nbsp;% et 3&nbsp;% de l'assiette retraitée, c'est une comparaison statique, pas une prévision.

**Pour préparer le budget 2027.** Ne pas inscrire la contribution comme une charge certaine&nbsp;; la garder dans un scénario conditionnel, calculé sur l'assiette de 2024 retraitée, à réactiver si l'article revenait.

<details class="repli"><summary>Classement, taux, assiette et exonérations prévus par l'article 37</summary>

Les communes sont classées selon un indice qui pondère à 75&nbsp;% leur potentiel financier par habitant et à 25&nbsp;% le revenu par habitant, chacun rapporté à la moyenne. Le taux va de 0,5&nbsp;% pour le premier décile à 2&nbsp;% pour le dixième, et 3&nbsp;% pour les deux derniers centiles. Il s'applique aux recettes réelles de fonctionnement du budget principal constatées dans le compte financier unique de l'antépénultième exercice, soit 2024 pour une contribution due en 2027, minorées des atténuations de produits, des recettes exceptionnelles et du produit des mises à disposition de personnel facturées dans le cadre d'une mutualisation avec l'intercommunalité. Sont exonérées les communes des départements et régions d'outre-mer, celles que l'article L.&nbsp;2336-3 du code général des collectivités territoriales exempte déjà du fonds de péréquation intercommunal (les 250 premières communes de 10&nbsp;000 habitants et plus et les 30 premières de 5&nbsp;000 à 9&nbsp;999 au classement de la dotation de solidarité urbaine, les 2&nbsp;500 premières au classement de la fraction cible de la dotation de solidarité rurale), et celles dont la contribution serait inférieure à 5&nbsp;000&nbsp;euros. Les intercommunalités sont classées de même, sur leur potentiel fiscal, à un taux de 0,5&nbsp;% à 2&nbsp;%.

</details>

### Le fonds de compensation pour la TVA (articles 35 et 41) {#fctva}

**Ce que prévoyait le projet.** Pour les attributions versées à compter du 1er&nbsp;janvier {{< coll-val "plf_edition" >}}, un taux ramené de 16,404&nbsp;% à 11,404&nbsp;%, soit {{< coll-val "plf_fctva_pts" >}}&nbsp;points de moins, sauf pour les dépenses liées à la transition écologique et à la voirie, maintenues à 16,404&nbsp;%, et un rendement de {{< coll-val "plf_fctva" >}}&nbsp;milliards d'euros. La liste des comptes ouvrant droit au taux maintenu relevait d'un arrêté à venir.

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_fctva" >}}. Si la mesure revenait, l'arrêté fixant les comptes au taux maintenu dirait quelles dépenses en bénéficient.

**Ce que cela signifie pour une commune.** La mesure portait sur les **attributions versées**, pas sur les dépenses engagées. Selon l'article L.&nbsp;1615-6 du code, les attributions d'une commune au régime de droit commun portent sur les dépenses de l'avant-dernière année&nbsp;: en {{< coll-val "plf_edition" >}}, celles de 2025, déjà réalisées sous l'ancien taux. Pour certaines communes, elles portent sur les dépenses de l'année précédente&nbsp;; pour les communes nouvelles, sur celles de l'année en cours.

**Ce que le service financier peut vérifier dès maintenant.** Le régime de versement de la commune, donc l'année de dépenses concernée&nbsp;; la part de ces dépenses imputée sur des comptes de transition écologique ou de voirie.

**Ce qu'il serait trompeur de chiffrer.** Une perte&nbsp;: sans la liste des comptes au taux maintenu, la ventilation des dépenses reste inconnue. Pour la seule part qui aurait relevé du taux réduit, {{< coll-val "plf_fctva_pts" >}}&nbsp;points sur 16,404 représentent un peu moins d'un tiers de l'attribution correspondante&nbsp;: une comparaison statique, pas une prévision du versement de 2027.

**Pour préparer le budget 2027.** Inscrire l'attribution au taux en vigueur, 16,404&nbsp;%, sur les dépenses de l'année de référence&nbsp;; garder la baisse dans un scénario conditionnel.

### La dotation globale de fonctionnement (articles 34 et 83) {#dgf}

**Ce que prévoyait le projet.** Un montant national de {{< coll-val "plf_dgf" >}}&nbsp;milliards d'euros&nbsp;; une hausse des dotations de solidarité urbaine et rurale financée en partie par l'écrêtement de la dotation forfaitaire (article 83, seconde partie). La présentation générale du projet et l'exposé des motifs de l'article 83 ne répartissent pas cette hausse de la même manière entre les deux dotations&nbsp;: c'est le Comité des finances locales qui la fixera.

**Ce qu'a décidé l'Assemblée.** Article 34 adopté modifié&nbsp;: la DGF pour {{< coll-val "plf_edition" >}} est portée à {{< coll-val "plf_dgf_an" >}}&nbsp;milliards d'euros, soit {{< coll-val "plf_dgf_an_m" >}}&nbsp;millions de plus que le projet. C'est un montant pour {{< coll-val "plf_edition" >}}, non une règle d'indexation. L'article 83 relève de la seconde partie, que l'Assemblée n'a pas encore examinée.

**Ce que cela signifie pour une commune.** Un montant national ne se répartit pas entre communes par simple proportion&nbsp;: chaque dotation obéit à ses propres critères, et une commune peut voir sa dotation forfaitaire écrêtée tandis que sa dotation de solidarité augmente.

**Ce que le service financier peut vérifier dès maintenant.** La composition de la DGF de la commune en 2026&nbsp;: dotation forfaitaire et écrêtement éventuel, dotations de solidarité urbaine et rurale, dotation nationale de péréquation.

**Ce qu'il serait trompeur de chiffrer.** La DGF de la commune pour 2027&nbsp;: elle dépend de la loi votée et de la répartition du Comité des finances locales.

**Pour préparer le budget 2027.** Ne pas lire la hausse nationale comme une recette garantie pour la commune&nbsp;; retenir une estimation prudente jusqu'à la notification.

### Les sommes mises en réserve en 2025 et 2026 (DILICO, article 84) {#dilico}

Le dispositif de lissage des recettes fiscales a mis en réserve, en 2025, une part des recettes des communes, des intercommunalités, des départements et des régions (loi de finances pour 2025, article 186)&nbsp;; en 2026, **les communes n'y contribuent pas**&nbsp;: seulement les intercommunalités dont l'indice de ressources et de charges dépasse 110&nbsp;% de la moyenne, les départements et les régions (loi de finances pour 2026, article 196). Chaque reversement annuel va pour 10&nbsp;% à la péréquation (pour le bloc communal, le fonds de péréquation intercommunal), le reste aux contributeurs&nbsp;: une collectivité récupère ainsi 90&nbsp;% de sa contribution.

**Ce que prévoyait le projet.** Étaler jusqu'en 2031 le reversement des sommes mises en réserve, sans changer leur total&nbsp;; selon l'exposé des motifs, environ 2&nbsp;000 collectivités sont concernées. Les deux dispositifs ne se traitent pas de la même façon&nbsp;: pour celui de 2025, un tiers a déjà été reversé en 2026 et les **deux tiers restants** seraient reversés par cinquièmes de 2027 à 2031, au lieu de deux tiers en 2027 et 2028&nbsp;; pour celui de 2026, la **totalité** serait reversée par cinquièmes de 2027 à 2031, au lieu de tiers de 2027 à 2029.

| Pour 300&nbsp;000&nbsp;€ mis en réserve (exemple), part revenant au contributeur | DILICO 2025 (commune ou intercommunalité) | DILICO 2026 (intercommunalité, pas la commune) |
|---|---|---|
| Déjà reçu en 2026 | 90&nbsp;000&nbsp;€ | 0&nbsp;€ |
| Chaque année, selon le droit actuel | 90&nbsp;000&nbsp;€ en 2027 et en 2028 | 90&nbsp;000&nbsp;€ de 2027 à 2029 |
| Chaque année, selon le projet déposé | 36&nbsp;000&nbsp;€ de 2027 à 2031 | 54&nbsp;000&nbsp;€ de 2027 à 2031 |
| Total reçu | 270&nbsp;000&nbsp;€ dans les deux cas | 270&nbsp;000&nbsp;€ dans les deux cas |

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_dilico" >}}. Le projet prévoit un arrêté unique de reversement.

**Ce que cela signifie pour une commune.** Seul le DILICO 2025 la concerne directement&nbsp;; celui de 2026 touche, le cas échéant, son intercommunalité. Pour une commune contributrice en 2025, le total restitué ne change pas&nbsp;; ses versements annuels baissent et s'étalent jusqu'en 2031, ce qui pèse sur sa trésorerie et, si l'inflation se poursuit, sur la valeur réelle des sommes restituées.

**Ce que le service financier peut vérifier dès maintenant.** Le montant mis en réserve par la commune en 2025, notifié par arrêté, et ce qu'elle a déjà reçu en 2026&nbsp;; pour 2026, la contribution éventuelle de son intercommunalité. Avec ces montants, le calcul ci-dessus est exact, si le texte est voté tel quel.

**Ce qu'il serait trompeur de chiffrer.** Rien de plus que ce calcul&nbsp;: il ne vaut que pour le projet déposé.

**Pour préparer le budget 2027.** Établir l'échéancier des reversements du DILICO 2025, une colonne selon le droit actuel, une selon le projet&nbsp;; retenir la seconde si l'article 84 est voté&nbsp;; signaler, dans les relations financières avec l'intercommunalité, l'étalement de son propre DILICO 2026.

### Les fractions de TVA (article 36) {#tva}

**Ce que prévoyait le projet.** Pour les fractions de TVA versées en remplacement d'impôts supprimés (articles 16 de la loi de finances pour 2020 et 55 de celle pour 2023), une progression annuelle diminuée de l'inflation hors tabac de l'année précédente, sans que le montant puisse baisser d'une année sur l'autre. Le Haut Conseil des finances publiques chiffrait l'écrêtement à {{< coll-val "plf_tva" >}}&nbsp;milliard d'euros pour l'ensemble des bénéficiaires.

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_tva" >}}. Les amendements qui supprimaient l'article avaient d'abord été rejetés&nbsp;; c'est l'article amendé qui n'a pas été adopté.

**Ce que cela signifie pour une commune.** Seules sont concernées les collectivités qui perçoivent une telle fraction&nbsp;; si c'est l'intercommunalité, l'effet sur la commune passerait par leurs relations financières.

**Ce que le service financier peut vérifier dès maintenant.** Si la commune perçoit elle-même une fraction de TVA, ou si c'est son intercommunalité.

**Ce qu'il serait trompeur de chiffrer.** L'effet&nbsp;: il aurait dépendu de la TVA encaissée et de l'inflation, inconnues à ce jour.

**Pour préparer le budget 2027.** Inscrire la fraction selon les règles actuelles&nbsp;: l'écrêtement n'est plus dans le texte à ce stade.

### Les autres dispositions {#autres}

- **Dotation pour les communes rurales de faible densité** (article 85, seconde partie)&nbsp;: 50&nbsp;millions d'euros, réservés aux communes peu ou très peu denses de la grille de l'Insee dont la densité est inférieure à une moyenne de référence, à l'exclusion des bénéficiaires de la dotation pour les aménités rurales, et répartis selon la superficie par un décret à venir.
- **Forfaits de post-stationnement** (article 53, première partie, dont l'examen se poursuit)&nbsp;: 1,9&nbsp;% des forfaits acquittés après l'émission d'un titre exécutoire reversés au budget de l'État, pour les titres émis à compter du 1er&nbsp;janvier 2027.
- **Métropole du Grand Paris** (article 40)&nbsp;: la prolongation du financement transitoire jusqu'en 2028 n'a pas été adoptée le {{< coll-val "plf_vote_date" >}}&nbsp;; les communes de la métropole sont concernées par l'intermédiaire de leur établissement public territorial.

## Quand la commune connaîtra-t-elle ses montants&nbsp;? {#calendrier}

1. **Au Parlement**&nbsp;: {{< coll-val "plf_etape_suivante" >}}&nbsp;; puis le Sénat, et l'adoption définitive.
2. **Après la loi**&nbsp;: les arrêtés et décrets qu'elle prévoit, puis les informations que le préfet communique aux maires, dont le montant de chacune des dotations de la DGF (article D.&nbsp;1612-1 du code).
3. **Le budget primitif** doit être adopté avant le 15&nbsp;avril.

Le délai du 15&nbsp;avril ne cède que dans un cas précis&nbsp;: lorsque des informations que la réglementation dit indispensables à l'établissement du budget, comme les montants de la DGF, n'ont pas été communiquées avant le 31&nbsp;mars&nbsp;; le conseil dispose alors de quinze jours après leur communication (article L.&nbsp;1612-2). Attendre un autre montant, celui d'une mesure nouvelle par exemple, n'ouvre aucun délai&nbsp;: le budget se vote avec les informations disponibles, et se corrige ensuite par décision modificative.

## Ce que ses comptes publiés permettent déjà {#dans-vos-comptes}

L'Observatoire des finances et de la gestion publique locales publie, commune par commune sur data.ofgl.fr, les comptes de 2024 et de 2025&nbsp;: recettes réelles de fonctionnement, FCTVA perçu, DGF, épargne brute. Ces agrégats ne sont pas l'assiette légale de la contribution progressive, qui en retranche plusieurs postes&nbsp;; ils situent un ordre de grandeur, et l'épargne brute dit la marge dont la commune dispose pour absorber une baisse de recettes. [La page consacrée aux collectivités](/dette-publique-collectivites-locales/#votre-collectivite) détaille comment lire ces lignes.

## Ce que cette page ne dit pas {#limites}

- Elle ne prévoit pas le texte définitif&nbsp;: une mesure supprimée en séance peut être rétablie.
- Elle ne donne aucun montant pour une commune&nbsp;; les ordres de grandeur qu'elle indique sont des comparaisons statiques, sous les conditions écrites à côté d'eux.
- Elle ne reprend que les dispositions du projet qui visent directement les communes&nbsp;; les mesures fiscales générales peuvent aussi peser sur leurs recettes.

## D'où viennent ces chiffres {#sources}

**État du texte** — Assemblée nationale, comptes rendus des [première](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/premiere-seance-du-lundi-19-octobre-2026) et [deuxième](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-lundi-19-octobre-2026) séances du 19&nbsp;octobre 2026&nbsp;; chaque résultat repris ici y est cité mot pour mot dans le registre des votes de la page, archivé avec l'empreinte des comptes rendus. [Dossier législatif](https://www.assemblee-nationale.fr/dyn/17/dossiers/PLF_2027) pour le calendrier.

**Textes** — [Projet de loi de finances pour {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf), n°&nbsp;3210, déposé le {{< coll-val "plf_depot" >}}, articles 34 à 41, 53 et 83 à 87 et leurs exposés des motifs&nbsp;; [avis du Haut Conseil des finances publiques](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf) sur ce projet&nbsp;; code général des collectivités territoriales, articles [L.&nbsp;1612-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051731704), [D.&nbsp;1612-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006395280), [L.&nbsp;1615-6](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053547367) et [L.&nbsp;2336-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053549170), relus sur Légifrance le 22&nbsp;octobre 2026.

{{< reutiliser figures="figures_plf_communes" jeu="dette_collectivites" sources="Assemblée nationale, Haut Conseil des finances publiques et Légifrance" donnees="Les montants des cinq mesures du projet déposé, l'état de chaque article au Parlement et la DGF adoptée par l'Assemblée nationale, dans le jeu « collectivités locales et finances publiques » ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Le projet de loi de finances pour {{< coll-val "plf_edition" >}} déposé prévoyait cinq mesures visant les collectivités, d'une somme arithmétique de {{< coll-val "plf_somme" >}}&nbsp;milliards d'euros, qui ne mesure pas un prélèvement net. Le {{< coll-val "plf_vote_date" >}}, l'Assemblée nationale {{< coll-val "plf_vote_resume" >}}. Aucun montant communal ne se déduit d'un projet&nbsp;: il viendra de la loi votée, puis des arrêtés et notifications.
{{< /reutiliser >}}

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Prolonger l'analyse" avis="non" >}}
Cette page suit un texte en discussion&nbsp;; le livre explique pourquoi les finances locales deviennent, d'un budget à l'autre, un levier de l'ajustement national, et qui en supporte le coût au bout de la chaîne.
{{< /appel-livre >}}
