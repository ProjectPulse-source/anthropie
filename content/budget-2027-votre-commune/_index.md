---
title: "Budget 2027 : que sait-on réellement pour votre commune ?"
description: "Projet de loi de finances pour 2027 : ce que prévoyait le texte déposé pour les communes, ce que l'Assemblée nationale en a fait en séance le {coll.plf_vote_date}, ce qu'une commune peut en déduire, et quand elle connaîtra ses montants. État du texte daté, sources primaires."
chapo: "En séance, le {coll.plf_vote_date}, l'Assemblée nationale {coll.plf_vote_resume} : trois des cinq mesures que le projet déposé destinait aux collectivités, dont les deux plus importantes en montant, ne figurent plus dans le texte qu'elle examine. Rien n'est acquis pour autant : la procédure continue ({coll.plf_etape_suivante}), le Sénat suivra, et une mesure supprimée peut être rétablie. Aucun montant communal ne se déduit d'un projet ; les montants viendront de la loi votée, puis des notifications et arrêtés que cette page indique mesure par mesure."
date: 2026-10-22
lastmod: 2026-10-22
# Série « Votre commune face aux décisions de l'État » (auteur, 22/10/2026), ressource n° 1. Arbitrage de l'auteur :
# D:\PRO\06_PROMOTION\RECHERCHE_VOTRE_COMMUNE_2026-10-22\ARBITRAGE_1807_COMMUNES.md (pièce 1807_Communes.txt). État du
# texte : jetons {coll.plf_*}, tirés de scripts/sources_collectivites/plf_votes.json (citations verbatim des comptes
# rendus officiels, retrouvées par verifier_plf_votes.py) par scripts/update_dette_collectivites.py ; montants du projet
# lus dans son archive. Taux, seuils et articles cités en clair : texte du projet déposé (PDF, SHA-256 132274b8…) et
# CGCT relu sur Légifrance le 22/10/2026. Une étape parlementaire = une entrée du registre + une ligne de journal.
og_title: "Budget 2027 : que sait-on réellement pour votre commune ? — S. Lalut"
og_image: "images/og-budget-2027-commune.jpg"
og_image_alt: "Carte de partage : « Budget 2027 : ce qu'il en reste » — les cinq mesures du projet de loi de finances déposé visant les collectivités, en milliards d'euros, évidées quand l'Assemblée nationale les a supprimées ou n'a pas adopté leur article."
donnees: [dette_collectivites]
dossier_source: "plf"   # barre du dossier : source = état du projet au Parlement (shortcode dossier-dette)
journal:
  - {date: 2026-10-22, texte: "Publication : état du texte après la séance de l'Assemblée nationale du 19 octobre 2026."}
faq:
  - question: "La contribution progressive à l'effort budgétaire (CPEB) s'applique-t-elle à ma commune ?"
    answer: "Pas à ce stade : l'article 37 qui l'instituait a été supprimé en séance par l'Assemblée nationale le {coll.plf_vote_date}. La procédure budgétaire n'est pas achevée et l'article peut être rétabli. S'il l'était tel que le projet l'avait déposé, la contribution d'une commune non exonérée serait comprise entre 0,5 % et 3 % de ses recettes réelles de fonctionnement de 2025, minorées ; son montant exact serait fixé par un arrêté publié au Journal officiel."
  - question: "La baisse du taux du FCTVA touche-t-elle les investissements déjà réalisés ?"
    answer: "Dans le projet déposé, le nouveau taux visait les attributions versées à compter du 1er janvier 2027. Pour une commune au régime de droit commun, ces attributions portent sur les dépenses de l'avant-dernière année : en 2027, celles de 2025, déjà réalisées. L'article 35 a été supprimé en séance par l'Assemblée nationale le {coll.plf_vote_date} ; il peut être rétabli avant la loi définitive."
  - question: "Quand ma commune connaîtra-t-elle sa DGF pour 2027 ?"
    answer: "Après le vote de la loi de finances, par la notification de ses attributions individuelles. Le montant national pour {coll.plf_edition} voté par l'Assemblée en première partie le {coll.plf_vote_date}, {coll.plf_dgf_an} milliards d'euros, ne dit rien d'une commune : la répartition dépend des critères de chaque dotation et des choix du Comité des finances locales."
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
dossier_dette: prolongement   # panneau « Prolongements » de la barre du dossier
dossier_dette_titre: "Budget 2027 : votre commune"
dossier_dette_role: "projet de loi, état du texte"
dossier_dette_titre_en: "Budget 2027: your municipality"
dossier_dette_role_en: "draft budget bill, state of the text"
---

{{< dossier-dette volet="prolongement" >}}

{{< reutiliser-ancre >}}

<div class="encadre">

**État au {{< coll-val "plf_etat_au" >}}.** Projet de loi de finances pour {{< coll-val "plf_edition" >}} déposé le {{< coll-val "plf_depot" >}}, examiné en séance par l'Assemblée nationale le {{< coll-val "plf_vote_date" >}}. Prochaine étape&nbsp;: {{< coll-val "plf_etape_suivante" >}}. Cette page est révisée à chaque étape qui modifie ces mesures&nbsp;; ses révisions restent lisibles en pied de page.

</div>

Un maire qui prépare son débat d'orientation budgétaire lit en même temps deux choses qui ne disent pas la même chose&nbsp;: les montants annoncés à la présentation du projet, et ce que le Parlement en a fait depuis. Cette page sépare les deux. Pour chaque mesure qui touche les communes, elle répond à quatre questions&nbsp;: **que prévoyait-elle, qu'a décidé l'Assemblée, que peut-il en résulter pour une commune, et quand en saura-t-on davantage**.

{{< figure-svg fichier="collectivites-plf" alt="Cinq barres horizontales orange, en milliards d'euros : les mesures du projet de loi de finances déposé qui visent les collectivités. Les trois barres évidées, contribution progressive, baisse du FCTVA et écrêtement de la TVA, sont celles dont l'Assemblée nationale a supprimé ou n'a pas adopté l'article en séance ; les deux barres pleines, contributions de ministères et étalement du DILICO, relèvent de la seconde partie, non encore examinée." >}}Les cinq mesures du projet de loi de finances déposé qui visent les collectivités, et leur sort au Parlement. Montants du projet déposé&nbsp;; leur somme arithmétique ne mesure pas un prélèvement net.{{< /figure-svg >}}

{{< fig-actions id="plf" >}}

<div class="resultat-phrase">

**Le résultat en une phrase.** Le projet de loi de finances pour {{< coll-val "plf_edition" >}} déposé prévoyait cinq mesures visant les collectivités, d'une somme arithmétique de {{< coll-val "plf_somme" >}}&nbsp;milliards d'euros&nbsp;; le {{< coll-val "plf_vote_date" >}}, l'Assemblée nationale {{< coll-val "plf_vote_resume" >}}, sans qu'aucune soit définitivement écartée.

</div>

## Que reste-t-il du projet déposé&nbsp;? {#etat-du-texte}

{{< coll-tableau "plf" >}}

La somme arithmétique de ces cinq montants, {{< coll-val "plf_somme" >}}&nbsp;milliards d'euros, décrivait le projet déposé&nbsp;; elle ne mesurait pas un prélèvement net, et [la page consacrée aux collectivités](/dette-publique-collectivites-locales/#projet-de-loi-de-finances) explique pourquoi elle coexistait avec une hausse prévue des ressources locales. Depuis le {{< coll-val "plf_vote_date" >}}, elle ne décrit plus le texte en discussion. Un article supprimé ou non adopté en séance ne figure plus dans le texte en discussion, mais il peut y revenir, par un amendement du Gouvernement ou au Sénat. À l'ouverture du débat du 19&nbsp;octobre, la ministre chargée des collectivités, Françoise Gatel, chiffrait à 5,5&nbsp;milliards d'euros la contribution des collectivités prévue par le projet.

## Mesure par mesure {#mesure-par-mesure}

### La contribution progressive à l'effort budgétaire (article 37) {#cpeb}

**Ce que prévoyait le projet.** Une contribution de {{< coll-val "plf_cpeb" >}}&nbsp;milliards d'euros pour {{< coll-val "plf_edition" >}}, due par {{< coll-val "plf_cpeb_communes_pct" >}}&nbsp;% des communes selon l'exposé des motifs, à un taux compris entre 0,5&nbsp;% et 3&nbsp;% de leurs recettes réelles de fonctionnement, et prélevée chaque mois sur les douzièmes de fiscalité.

<details class="repli"><summary>Classement, taux, assiette et exonérations prévus par l'article 37</summary>

Les communes sont classées selon un indice qui pondère à 75&nbsp;% leur potentiel financier par habitant et à 25&nbsp;% le revenu par habitant, chacun rapporté à la moyenne. Le taux va de 0,5&nbsp;% pour le premier décile à 2&nbsp;% pour le dixième, et 3&nbsp;% pour les deux derniers centiles. Il s'applique aux recettes réelles de fonctionnement du budget principal de l'avant-dernier exercice, soit 2025, minorées notamment des atténuations de produits et des recettes exceptionnelles. Sont exonérées les communes des départements et régions d'outre-mer, celles que l'article L.&nbsp;2336-3 du code général des collectivités territoriales exempte déjà du fonds de péréquation intercommunal (les 250 premières communes de 10&nbsp;000 habitants et plus et les 30 premières de 5&nbsp;000 à 9&nbsp;999 au classement de la dotation de solidarité urbaine, les 2&nbsp;500 premières au classement de la fraction cible de la dotation de solidarité rurale), et celles dont la contribution serait inférieure à 5&nbsp;000&nbsp;euros. Le montant de chaque commune devait être notifié par arrêté au Journal officiel, puis **prélevé chaque mois sur les douzièmes de fiscalité**&nbsp;: un effet de trésorerie dès la notification, avant même la lecture budgétaire.

</details>

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_cpeb" >}}.

**Ce qui peut en résulter pour une commune.** Rien n'est dû en l'état du texte. Si l'article était rétabli à l'identique, une commune non exonérée pourrait situer sa contribution entre 0,5&nbsp;% et 3&nbsp;% de ses recettes réelles de fonctionnement de 2025, minorées&nbsp;: c'est une comparaison statique, pas un montant. Le taux exact dépend de son rang parmi toutes les communes, que plusieurs cabinets de conseil et associations d'élus ont simulé sur le texte initial&nbsp;; ces simulations décrivent l'article tel qu'il a été déposé, et les associations qui les publient ont demandé sa suppression ou sa réduction.

**Quand en saura-t-on davantage.** Au vote solennel de la première partie, puis au Sénat. Si la contribution était rétablie, le montant de chaque commune serait celui de l'arrêté publié au Journal officiel.

### Le fonds de compensation pour la TVA (articles 35 et 41) {#fctva}

**Ce que prévoyait le projet.** Pour les attributions versées à compter du 1er&nbsp;janvier {{< coll-val "plf_edition" >}}, un taux ramené de 16,404&nbsp;% à 11,404&nbsp;%, soit {{< coll-val "plf_fctva_pts" >}}&nbsp;points de moins, sauf pour les dépenses liées à la transition écologique et à la voirie, maintenues à 16,404&nbsp;%, et un rendement de {{< coll-val "plf_fctva" >}}&nbsp;milliards d'euros. La liste des comptes ouvrant droit au taux maintenu relevait d'un arrêté à venir.

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_fctva" >}}.

**Ce qui peut en résulter pour une commune.** La mesure portait sur les **attributions versées**, pas sur les dépenses engagées. Or, selon l'article L.&nbsp;1615-6 du code, les attributions d'une commune au régime de droit commun portent sur les dépenses de l'avant-dernière année&nbsp;: en {{< coll-val "plf_edition" >}}, celles de 2025, déjà réalisées sous l'ancien taux. Pour certaines communes, les attributions portent sur les dépenses de l'année précédente&nbsp;; pour les communes nouvelles, sur celles de l'année en cours. Pour la part des dépenses qui aurait relevé du taux réduit, {{< coll-val "plf_fctva_pts" >}}&nbsp;points sur 16,404 représentent un peu moins d'un tiers de l'attribution correspondante. Sans la ventilation de ses dépenses entre taux maintenu et taux réduit, qui dépendait de l'arrêté, une commune ne peut pas en tirer un montant.

**Quand en saura-t-on davantage.** Au vote de la loi, puis, si la mesure revenait, à la publication de l'arrêté fixant les comptes au taux maintenu.

### Les fractions de TVA (article 36) {#tva}

**Ce que prévoyait le projet.** Pour les fractions de TVA versées en remplacement d'impôts supprimés (articles 16 de la loi de finances pour 2020 et 55 de celle pour 2023), une progression annuelle diminuée de l'inflation hors tabac de l'année précédente, sans que le montant puisse baisser d'une année sur l'autre. Le Haut Conseil des finances publiques chiffrait l'écrêtement à {{< coll-val "plf_tva" >}}&nbsp;milliard d'euros pour l'ensemble des bénéficiaires.

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_tva" >}}. Les amendements qui supprimaient l'article avaient d'abord été rejetés&nbsp;; c'est l'article amendé qui n'a pas été adopté.

**Ce qui peut en résulter pour une commune.** Seules sont concernées les collectivités qui perçoivent une telle fraction&nbsp;; l'effet aurait dépendu de la TVA encaissée et de l'inflation, inconnues à ce jour. Non déterminable pour une commune.

**Quand en saura-t-on davantage.** Au vote de la loi.

### La dotation globale de fonctionnement (articles 34 et 83) {#dgf}

**Ce que prévoyait le projet.** Un montant national de {{< coll-val "plf_dgf" >}}&nbsp;milliards d'euros&nbsp;; une hausse des dotations de solidarité urbaine et rurale financée en partie par l'écrêtement de la dotation forfaitaire (article 83, seconde partie). La présentation générale du projet et l'exposé des motifs de l'article 83 ne répartissent pas cette hausse de la même manière entre les deux dotations&nbsp;: c'est le Comité des finances locales qui la fixera.

**Ce qu'a décidé l'Assemblée.** Article 34 adopté modifié&nbsp;: la DGF pour {{< coll-val "plf_edition" >}} est portée à {{< coll-val "plf_dgf_an" >}}&nbsp;milliards d'euros, soit {{< coll-val "plf_dgf_an_m" >}}&nbsp;millions de plus que le projet. C'est un montant pour {{< coll-val "plf_edition" >}}, non une règle d'indexation. L'article 83 relève de la seconde partie, que l'Assemblée n'a pas encore examinée.

**Ce qui peut en résulter pour une commune.** Un montant national ne se répartit pas entre communes par simple proportion&nbsp;: chaque dotation obéit à ses propres critères, et une commune peut voir sa dotation forfaitaire écrêtée tandis que sa dotation de solidarité augmente. Non déterminable avant la répartition.

**Quand en saura-t-on davantage.** À la notification des attributions individuelles, après le vote de la loi de finances et les décisions du Comité des finances locales.

### Les sommes mises en réserve en 2025 et 2026 (DILICO, article 84) {#dilico}

**Ce que prévoyait le projet.** Rembourser sur cinq ans, par cinquièmes de 2027 à 2031, les deux tiers restants du premier dispositif et la totalité du second, au lieu de trois ans par tiers&nbsp;; selon l'exposé des motifs, environ 2&nbsp;000 collectivités sont concernées et le montant total restitué ne change pas.

**Ce qu'a décidé l'Assemblée.** État au {{< coll-val "plf_etat_au" >}}&nbsp;: {{< coll-val "plf_etat_dilico" >}}.

**Ce qui peut en résulter pour une commune.** Pour une commune contributrice, le calcul est exact&nbsp;: à partir du montant mis en réserve, que lui a notifié un arrêté, le versement annuel passerait d'un tiers à un cinquième. L'effet est de trésorerie, pas de montant.

**Quand en saura-t-on davantage.** À l'examen de la seconde partie, puis à l'arrêté unique de reversement que prévoit le projet.

### Les autres dispositions {#autres}

- **Dotation pour les communes rurales de faible densité** (article 85, seconde partie)&nbsp;: 50&nbsp;millions d'euros, réservés aux communes peu ou très peu denses de la grille de l'Insee dont la densité est inférieure à une moyenne de référence, à l'exclusion des bénéficiaires de la dotation pour les aménités rurales, et répartis selon la superficie par un décret à venir.
- **Forfaits de post-stationnement** (article 53, première partie, dont l'examen se poursuit)&nbsp;: 1,9&nbsp;% des forfaits acquittés après l'émission d'un titre exécutoire reversés au budget de l'État, pour les titres émis à compter du 1er&nbsp;janvier 2027.
- **Métropole du Grand Paris** (article 40)&nbsp;: la prolongation du financement transitoire jusqu'en 2028 n'a pas été adoptée le {{< coll-val "plf_vote_date" >}}&nbsp;; les communes de la métropole sont concernées par l'intermédiaire de leur établissement public territorial.

## Quand la commune saura-t-elle&nbsp;? {#calendrier}

1. **Au Parlement**&nbsp;: {{< coll-val "plf_etape_suivante" >}}&nbsp;; puis le Sénat, et l'adoption définitive.
2. **Après la loi**&nbsp;: les arrêtés et décrets qu'elle prévoit (contribution, comptes du FCTVA, répartition de la nouvelle dotation rurale), puis la notification des dotations.
3. **Le budget primitif** doit être adopté avant le 15&nbsp;avril. Selon l'article L.&nbsp;1612-2 du code, ce délai ne s'applique pas lorsque le retard tient à l'absence de communication, avant le 31&nbsp;mars, d'informations indispensables à l'établissement du budget&nbsp;; le conseil dispose alors de quinze jours après cette communication.

Une commune peut ainsi avoir à voter son budget avant d'avoir reçu tous les montants que l'État doit lui notifier&nbsp;: l'exception de l'article L.&nbsp;1612-2 existe pour ce cas. Pour les services financiers, ce décalage compte autant que le montant des mesures.

## Ce que la commune peut regarder dès maintenant {#dans-vos-comptes}

Ses propres comptes de 2025, publiés par l'Observatoire des finances et de la gestion publique locales sur data.ofgl.fr&nbsp;: les recettes réelles de fonctionnement, assiette de la contribution si elle revenait&nbsp;; le FCTVA perçu&nbsp;; la DGF&nbsp;; l'épargne brute, qui dit la marge dont elle dispose pour absorber une baisse de recettes. [La page consacrée aux collectivités](/dette-publique-collectivites-locales/#votre-collectivite) détaille comment lire ces lignes.

## Ce que cette page ne dit pas {#limites}

- Elle ne prévoit pas le texte définitif&nbsp;: une mesure supprimée en séance peut être rétablie.
- Elle ne donne aucun montant pour une commune&nbsp;; les ordres de grandeur qu'elle indique sont des comparaisons statiques, sous les conditions écrites à côté d'eux.
- Elle ne reprend que les dispositions du projet qui visent directement les communes&nbsp;; les mesures fiscales générales peuvent aussi peser sur leurs recettes.

{{< appel-livre slug="dette-publique-qui-paie-vraiment" sur="Prolonger l'analyse" avis="non" >}}
Cette page suit un texte en discussion&nbsp;; le livre explique pourquoi les finances locales deviennent, d'un budget à l'autre, un levier de l'ajustement national, et qui en supporte le coût au bout de la chaîne.
{{< /appel-livre >}}

## Questions fréquentes {#questions-frequentes}

{{< faq-visible >}}

## D'où viennent ces chiffres {#sources}

**État du texte** — Assemblée nationale, comptes rendus des [première](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/premiere-seance-du-lundi-19-octobre-2026) et [deuxième](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-lundi-19-octobre-2026) séances du 19&nbsp;octobre 2026&nbsp;; chaque résultat repris ici y est cité mot pour mot dans le registre des votes de la page, archivé avec l'empreinte des comptes rendus. [Dossier législatif](https://www.assemblee-nationale.fr/dyn/17/dossiers/PLF_2027) pour le calendrier.

**Textes** — [Projet de loi de finances pour {{< coll-val "plf_edition" >}}](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf), n°&nbsp;3210, déposé le {{< coll-val "plf_depot" >}}, articles 34 à 41, 53 et 83 à 87 et leurs exposés des motifs&nbsp;; [avis du Haut Conseil des finances publiques](https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf) sur ce projet&nbsp;; code général des collectivités territoriales, articles [L.&nbsp;1612-2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051731704), [L.&nbsp;1615-6](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053547367) et [L.&nbsp;2336-3](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053549170), relus sur Légifrance le 22&nbsp;octobre 2026.

{{< reutiliser figures="figures_plf_communes" jeu="dette_collectivites" sources="Assemblée nationale, Haut Conseil des finances publiques et Légifrance" donnees="Les montants des cinq mesures du projet déposé, l'état de chaque article au Parlement et la DGF adoptée par l'Assemblée nationale, dans le jeu « collectivités locales et finances publiques » ; le même contenu existe en CSV, en format long, lisible dans un tableur." >}}
Le projet de loi de finances pour {{< coll-val "plf_edition" >}} déposé prévoyait cinq mesures visant les collectivités, d'une somme arithmétique de {{< coll-val "plf_somme" >}}&nbsp;milliards d'euros, qui ne mesure pas un prélèvement net. Le {{< coll-val "plf_vote_date" >}}, l'Assemblée nationale {{< coll-val "plf_vote_resume" >}}. Aucun montant communal ne se déduit d'un projet&nbsp;: il viendra de la loi votée, puis des arrêtés et notifications.
{{< /reutiliser >}}
