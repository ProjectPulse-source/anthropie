# Fiche de conception — Budget 2027 : que sait-on réellement pour votre commune ?

Page : `/budget-2027-votre-commune/` (FR) · `/en/2027-budget-your-municipality/` (EN) · ouverte le 2026-10-22

**Écrite APRÈS la publication du 22/10/2026** : la page est partie sans fiche, faute de point d'entrée qui l'impose
(constat de l'auteur le même soir, « rattachée à rien »). Les champs ci-dessous reprennent le livrable 1 et l'arbitrage
de l'auteur (`D:\PRO\06_PROMOTION\RECHERCHE_VOTRE_COMMUNE_2026-10-22\`) ; les étapes disent ce qui a été fait, et ce qui
ne l'a pas été.

## Forme

Juridique-institutionnel et quantitatif : un texte en discussion, suivi article par article (dispositions, sort en
séance, actes d'application à venir), et des montants tirés du projet déposé. Critères propres retenus : chaque statut
d'article cité mot pour mot du compte rendu officiel (registre `scripts/sources_collectivites/plf_votes.json`) ; dater
chaque mesure (déposé, séance, promulgué) ; distinguer décision, entrée en vigueur et décaissement ; trois statuts pour
chaque chiffre (mesuré, comparaison statique, non déterminable) ; aucun montant national réparti entre communes.

## Fiche de conception

### Question centrale

Que change le projet de loi de finances pour 2027 pour une commune, et qu'en peut-on réellement chiffrer à ce jour ?

### Enjeu

Les maires préparent leur débat d'orientation budgétaire avec des montants annoncés au dépôt du projet ; le Parlement
en a déjà défait une partie. Se tromper d'état du texte, c'est inscrire au budget un prélèvement supprimé, ou en oublier
un qui reviendra.

### Croyance initiale

Le projet demande 6,2 milliards d'euros aux collectivités, et des simulateurs disent combien chaque commune paiera.

### Découverte principale

Le 19/10/2026, l'Assemblée nationale a supprimé ou n'a pas adopté trois des cinq mesures, dont les deux plus importantes
en montant ; la presse spécialisée (Localtis, 20/10) a rendu l'article 36 à l'envers ; les six simulateurs publiés
calculent un article supprimé.

### Mécanisme explicatif

Une mesure du projet n'atteint la commune qu'au bout d'une chaîne : vote, acte d'application (arrêté, décret, Comité des
finances locales), notification, imputation (douzièmes de fiscalité, attributions versées). Chaque maillon a sa date ;
la commune vote son budget avant de les connaître tous (CGCT L. 1612-2). Pour le FCTVA, le taux visait les attributions
versées, donc des dépenses déjà faites (CGCT L. 1615-6).

### Preuve décisive

Les comptes rendus officiels des deux séances du 19/10/2026 (archivés, empreintes dans `plf_votes.json`), chaque
citation retrouvée par `verifier_plf_votes.py` ; le texte du projet n° 3210 (PDF archivé, SHA-256 `132274b8…`).

### Limite

La page ne prévoit pas le texte définitif et ne donne aucun montant communal ; ses ordres de grandeur sont des
comparaisons statiques ; elle ne couvre que les dispositions qui visent directement les communes.

### Valeur finale

Un état du texte daté et contrôlable, mesure par mesure, avec ce que la commune peut en déduire et quand elle en saura
davantage : ce que ni la presse ni les simulateurs ne donnent.

### Singularité

Cette page existe parce qu'elle révèle l'état réel du texte au Parlement et le calendrier de ce qu'une commune peut
savoir, que le lecteur ne découvre pas dans les simulateurs publiés (Klopfer, Exfilo, France urbaine, Seldon,
Intercommunalités de France, FMPC : tous sur le texte initial, lus le 22/10) ni dans la presse spécialisée (Localtis,
article 36 rendu à l'envers).

### Raccords

Retenus : la page collectivités (« la page consacrée aux collectivités explique pourquoi elle coexistait avec une hausse
prévue des ressources locales », et en retour l'encadré d'état de cette page) ; le livre *Dette publique : qui paie
vraiment ?* (« le livre explique pourquoi les finances locales deviennent, d'un budget à l'autre, un levier de
l'ajustement national ») ; le dossier dette (prolongement, barre). Écartés : la définition de l'anthropie (page de faits
sur un texte en discussion ; aucune lecture anthropique n'y est démontrée) ; les working papers (aucun ne porte sur les
finances locales).

## Fiche D0

Résultat visé : que les maires et services financiers destinataires de la campagne MAIRES-COLL (363 mairies, 23 au
28/10/2026) reprennent l'état du texte dans leur débat d'orientation budgétaire ; diagnostics : réponses aux courriels,
reprises, consultations de la page (Search Console à J+30). État initial : page publiée le 22/10/2026, aucune visite.
**Non inscrite à ce jour dans `FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`** : à faire à la prochaine révision de la page.

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : non fait au départ (le type « ressource » n'existait pas) ; créé le
  22/10 au soir.
- Protocole du type : fait — juridique (comptes rendus, CGCT relu sur Légifrance le 22/10), quantitatif (montants lus
  dans le projet archivé).
- Scénarios d'architecture : un seul au départ ; réorganisation le 22/10 au soir sur l'arbitrage de l'auteur (pièce
  `1924_Communes-01.txt`, SHA-256 `0c8567d6…`) : l'essentiel en trente secondes (quatre questions), tableau du service
  financier, puis le détail ; cinq rubriques par mesure. Exception déclarée au point 9 du modèle (« conclusion → livre →
  sources → Réutiliser ») : le livre passe après Réutiliser, sur décision de l'auteur pour cette page.
- Panel avant : non fait.
- Contre-expertise de phase A : remplacée par l'arbitrage de l'auteur (pièce `1807_Communes.txt`, SHA-256 `df76dcc3…`).
- Arbitrage final de l'auteur (pièce `1942_Communes-02.txt`, SHA-256 `e0f1b148…`) : publication autorisée après deux
  vérifications, faites le 22/10 — premier écran à 390 px (le chapô répond aux quatre questions ; capture relue) ;
  cohérence des 363 courriels (phrase corrigée dans chaque message, aucune ancienne formule, empreintes approuvées).
  Rubrique « Pour préparer le budget 2027 » ajoutée à chaque mesure et au tableau.
- Corrections de fond du 22/10 au soir (relues à la source) : assiette de la contribution = comptes de 2024
  (antépénultième exercice), non 2025 ; DILICO 2025 = deux tiers restants par cinquièmes ; délai de l'article
  L. 1612-2 limité aux informations de l'article D. 1612-1. Journal de la page mis à jour.
- Gardes vues mordre : fait — état périmé, « trois des cinq mesures », « les deux plus importantes en montant », citations
  du registre des votes (deux mutations).
- Figures téléphone : fait — `collectivites-plf-m.svg` FR et EN, parité tenue.
- Relecture de langue : fait — LanguageTool FR et EN sur le texte servi, signalements tranchés (faux positifs).
- Recette 320-1280 : fait le 22/10 au soir — `recette.py`, FR et EN, « RECETTE OK », refaite après la réorganisation
  (« RECETTE OK », tableau de synthèse en cartes sur téléphone).
- Panel après : non fait.
- Gate éditorial : non fait.
- Relecture phrase à phrase FR et EN : faite le 22/10 (texte servi relu).
- Instantané de relecture : fait — `docs/relectures/budget-2027-votre-commune.txt` et la version anglaise.
- Contre-expertise de la page : non faite.
- Accord de l'auteur : publication autorisée (pièce `1807_Communes.txt`), « pousse » du 22/10.

## Extension — la fiche de votre commune (conception écrite le 22/10/2026, AVANT le code)

Décision de l'auteur : option A (pièce `2024_Communes-04.txt`) — une page outil unique, recherche par nom, département ou
code Insee, fiche individualisée à la demande, lien direct `?insee=`, aucune page par commune. **Architecture retenue** :
une section de `/budget-2027-votre-commune/` (`#fiche`), non une page neuve — règle 1 de « Architecture des ressources »
(une question = une section d'une page mère) ; le contenu indexable reste la page, l'outil en est la couche individualisée.

- **Forme** : quantitatif (comptes publiés, comparaison à un groupe) et juridique-institutionnel (statut des mesures,
  exonérations). Critères : chaque valeur porte sa source, son exercice et son statut (mesuré / calcul conditionnel /
  non déterminable) ; donnée absente = « non disponible », jamais zéro ; commune et intercommunalité toujours séparées ;
  aucun intervalle « votre contribution entre X et Y » (pièce 04) ; un changement de statut parlementaire met toutes
  les fiches à jour sans toucher aux comptes historiques.
- **Question centrale** : pour MA commune, quels chiffres officiels sont connus, quelles mesures du PLF pouvaient la
  toucher, quel est leur statut, que peut-on chiffrer et avec quelle fiabilité, que vérifier ou anticiper ?
- **Découverte attendue** : sa position dans son groupe de taille (épargne, dette, dépendance à la DGF), lue en un écran.
- **Preuve décisive** : comptes OFGL du budget principal (2024, 2025), relevés par script ; témoin par une seconde requête ;
  registre des votes pour les statuts.
- **Limites** : budgets annexes exclus ; assiette légale de la contribution non publiée (recettes OFGL ≠ assiette) ;
  exonération lue sur les rangs de 2026 (DSU : « classées l'année précédente », CGCT L. 2336-3, III, lu le 22/10 ; DSR
  cible : année non précisée par le texte, la fiche le dit) ; DILICO et DGF lus dans le jeu OFGL « dotations-communes »
  (données DGCL) : le site de la DGCL répondait 503 et les annexes des arrêtés sur Légifrance refusent un script — même
  donnée, autre canal ; pièces officielles (DA 0011/2025, 0008/2026, 0006/2026) à télécharger par l'auteur pour témoin.
- **Singularité** : les outils gratuits existants (BP Avocats, Sine Cera, AMF 56) chiffrent le texte INITIAL ; la fiche
  dit l'état du texte au jour dit et situe la commune dans son groupe — ce qu'aucun ne fait sous cette forme (lus le 22/10).
- **Étapes de l'extension** (22/10/2026) :
  - fait — générateur `scripts/update_budget_communes.py` : 34 778 communes, 165 écartées (motif nommé), dotations
    rattachées à toutes ; gardes vues mordre par mutation (DILICO total +100 € → arrêt ; 2 501 communes sous le rang
    2 500 → arrêt) ; témoins par seconde voie (10 communes comptes, 5 communes dotations, 0 écart) ;
  - fait — recette 320 à 1600 px FR et EN, valeurs visibles (mesure ajoutée après le défaut des valeurs cachées sur
    téléphone, témoin vu mordre) ; tableaux Markdown en cartes : libellé de colonne posé par `_markup/render-table.html`
    (15 pages, seul `data-label` change, comparaison du build) ;
  - fait — LanguageTool sur le texte servi de cinq fiches FR et EN (signalements lus : accord correct, orthographe
    britannique du site) ; relecture phrase à phrase et instantanés FR et EN refaits ; check-all, liens, rendu, dates à 0 ;
  - fait — contre-expertise externe PRO-20261022-215525 (paquet autoportant, cinq fiches servies) : verdict « publier
    après corrections » ; arbitrage `D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261022-215525_arbitrage.md`,
    article 37 relu au texte déposé ; trois P0 corrigés (Paris : coefficients 70,87 % et 29,13 % ; intercommunalités
    d'outre-mer exonérées ; « non exonérée » remplacé par « aucun critère d'exonération établi ») ; exonération graduée
    (établie / possible, à confirmer / aucun critère établi) ; plafond à 3 % retiré des fiches ; libellés DGF, FCTVA et
    désendettement précisés ;
  - fait — arbitrage final de l'auteur (pièce 2231_Communes-06) : DGF et dotation des communes nouvelles séparées ;
    périmètres documentés ; annexes officielles téléchargées par le navigateur et versionnées
    (`scripts/sources_budget_communes/`) ; témoin complet dans le générateur, vu mordre : 91 459 montants, 0 écart à l'euro ;
  - non fait — panel (motif : deux contre-expertises ont porté sur le texte servi ; l'auteur a clos la phase scientifique).
- **Refonte de la fiche, architecture v3** (23/10/2026 ; pièces `0124_Communes-11` et `0133_Communes-12`, arbitrage dans
  `D:\PRO\06_PROMOTION\RECHERCHE_VOTRE_COMMUNE_2026-10-22\ARBITRAGE_1924_COMMUNES-01.md` ; maquettes et recettes dans
  `MAQUETTE_FICHE\` du même dossier). Ordre : 01 la réponse → 02 principales mesures examinées → 03 conséquence DILICO
  (contributrices) → 04 situation financière → preuves repliées. **Réponse, critères explicites** : écart DILICO 2027
  (conditionnel à l'article 84 en l'état) ; sinon part de la DGF ≥ 1,5 fois la médiane de la strate et ≥ 5 points
  au-dessus, dite comme part observée ; sinon exonération établie ; sinon limites. Les textes de la fiche du 22/10
  (exonération graduée, Paris, intercommunalité, TVA affectée) sont gardés dans le repli « Comprendre le calcul » ; la
  frise de procédure de la maquette n'est pas reprise (état figé), remplacée par un lien vers `#etat-du-texte`.
  - fait — générateur : médiane de la part de la DGF par strate, compte du témoin des annexes et documents officiels
    (titres FR et EN, liens) écrits dans la méta et lus par la fiche (aucun chiffre écrit dans le script) ; relevé daté
    par les données (`releve_jeu`, date du cache avec `--cache`) : relevé inchangé (22/10), fiches par département
    identiques ;
  - fait — page : présentation de la fiche réécrite ; limite « aucun montant pour une commune » corrigée (fausse depuis
    le 22/10 : la fiche donnait déjà les montants DILICO) en « aucun montant certain pour 2027 », FR et EN ;
  - fait — recette 320, 390, 768, 1 280 et 1 600 px, FR et EN, neuf communes (contributrices Nanterre, Bandol, Paris ;
    part de la DGF Oyonnax, Conques-en-Rouergue sans compte 2024 ; outre-mer Les Abymes ; commune nouvelle Les Auxons ;
    sans intercommunalité Île-de-Bréhat ; seuil de 5 000 € Artemps) : aucun débordement, police ≥ 11 px, calendrier en
    tableau sous 720 px, aucune erreur de console ; témoin relu dans le JSON servi (catégorie de réponse, écart, lignes du
    calendrier), vu mordre (montant servi faussé : 24 défauts) ; impression de la fiche seule, A4 (4 à 5 pages, replis
    ouverts) ; script `MAQUETTE_FICHE\recette_fiche_site.py` ;
  - fait — LanguageTool sur le texte servi de huit fiches FR et EN (signalements restants lus : cellules accolées par
    l'extraction) ; relecture phrase à phrase : quatre défauts corrigés (« 1,9 ans », majuscule et parenthèses
    imbriquées de l'arrêté, accord « contribution… supprimé », nom pluriel « Les Abymes serait ») ; instantanés FR et EN
    refaits ; check-all, liens, rendu, dates à 0 ;
  - fait — push sur demande de l'auteur (23/10/2026, commit 8e9c9ec, sans le commit ANTHROPIE 6b1cc4d), déploiement
    réussi ; version servie attestée sans session : script et méta en ligne, fiches de Nanterre, Oyonnax (FR) et Les
    Abymes (EN) conformes (réponse, liens vers les sources, calendrier en tableau à 390 px) ;
  - fait — cache (23/10, constat de l'auteur : v3 invisible chez lui) : les dix scripts portent une empreinte de contenu
    (`partials/js-url.html`, `?v=` = 12 premiers caractères du SHA-256), vue changer sur mutation ; script absent = arrêt ;
  - fait — contre-expertise PRO-20261023-024713 (pièce `0255_Communes-13`, arbitrage dans
    `D:\PRO_PROMOTION\RECHERCHE_VOTRE_COMMUNE_2026-10-22\ARBITRAGE_1924_COMMUNES-01.md`) : titre tiré de la DGF
    sans question suggérant un effet du projet (« …, dont le montant 2027 reste à notifier ») ; coût de trésorerie du
    report dit sans montant ; contrôle de bout en bout de la version servie (profil de navigateur ayant l'ancien script en
    cache) ;
  - non fait — contre-expertise de la fiche intégrée seule (motif : la pièce 12 a validé l'architecture ; à proposer à
    l'auteur si une décision en dépend) ; panel (même motif qu'au 22/10).
