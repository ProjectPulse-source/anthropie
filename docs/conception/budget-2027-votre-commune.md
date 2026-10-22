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
