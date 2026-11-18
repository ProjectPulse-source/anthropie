# Fiche de conception — Que peut décider le président de la République seul ?

Page : `/pouvoirs-du-president-de-la-republique/` (FR) · `/en/what-can-the-french-president-decide-alone/` (EN) · ouverte le
2026-09-30 ; refondue le 2026-10-11 ; fiche écrite le 2026-11-17, à la reprise du lot « promesses-a »
(`D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\promesses-a\`), après la relecture des sources.

## Forme

`juridique-institutionnel`. Critères : distinguer pouvoir formel, initiative, décision, contreseing, mise en œuvre et effet
réel ; références juridiques datées (version en vigueur, date de lecture) ; conditions, exceptions et séquences de décision
contrôlées séparément ; aucun jeu de données artificiel (le jeu est un inventaire de citations, acte par acte).

## Fiche de conception

### Question centrale

Que peut décider le président de la République sans la signature d'un autre, et que le texte exige-t-il alors avant et après
lui ?

### Enjeu

Une promesse présidentielle suppose souvent un président qui décide seul. Savoir ce que la Constitution lui confie sans
contreseing, et à quelles conditions, dit ce qu'une promesse demande à d'autres acteurs : Gouvernement, Parlement, électeurs,
Conseil constitutionnel.

### Croyance initiale

Le président « décide de tout » ; ses pouvoirs les plus visibles (armées, grâce, traités, nominations aux emplois civils et
militaires) lui seraient personnels.

### Découverte principale

Sur les douze actes que la page distingue dans les huit dispositions dispensées de contreseing par l'article 19, neuf font
intervenir un autre acteur dans le texte même de leur article ; trois n'en prévoient aucun (nommer le Premier ministre,
adresser un message au Parlement, désigner le président du Conseil constitutionnel). Les pouvoirs les plus visibles sont
contresignés. — Ligne qui la porte : relecture `_R1a`, § 1 bis (recompte acte par acte à la source, le 17/11/2026 : 3 sur
12, 2 sur 8 par disposition) et `_R1b`, § 2 (53 citations exactes, 35 textes inchangés depuis leur lecture).

### Mécanisme explicatif

Le contreseing partage la responsabilité d'un acte entre le président et le Gouvernement. L'article 19 en dispense certains
actes, mais chacun de leurs articles fixe ses conditions (proposition, consultation, acte d'un autre acteur) et ses suites
(électeurs, Parlement, Conseil constitutionnel). Le reste passe par un Gouvernement responsable devant l'Assemblée (art. 20,
49, 50). — Lignes qui le portent : `_R1a`, l. 32-46 et 433-446 (conformes à la source) ; la l. 440 (« c'est de là que vient
l'image d'un président qui décide de tout ») est une lecture de la pratique, non vérifiée, qualifiée dans la version proposée
(« vraisemblablement »).

### Preuve décisive

L'inventaire acte par acte, en citations exactes des articles en vigueur lus sur Légifrance, chaque case pleine ou vide
justifiée ; le générateur retrouve chaque citation mot pour mot dans la réponse archivée (G2) et relit la liste des renvois
dans l'article 19 lui-même (G3, témoin de complétude).

### Pouvoir discriminant

Sans objet au sens d'une page de données : la page ne départage pas des explications mesurées ; elle confronte une lecture
courante (« le président décide seul ») au texte, article par article. Le témoin qui pourrait la démentir est la liste des
renvois relue dans l'article 19 : un acte oublié ou ajouté arrête le générateur.

### Limite

Lecture documentaire, sans certification juridique ; le découpage en douze actes est celui de la page (un autre, qui
compterait à part le message de l'article 16 ou la promulgation de l'article 11, changerait le nombre d'actes) ; les comptes
ne mesurent ni l'autonomie du président ni la pratique ; intervenir ne veut pas toujours dire empêcher.

### Valeur finale

Une grille réutilisable : pour une promesse, qui signe, ce qu'il faut avant et après, s'il faut une loi ; les citations et le
jeu, acte par acte, sous licence CC BY 4.0.

### Singularité

Cette page existe parce qu'elle montre, citation par citation, que même les actes dispensés de contreseing sont le plus
souvent encadrés par leur propre article — ce que le lecteur ne découvre pas dans l'article 19 lu seul, qui énumère des
articles sans dire ce que chacun exige ni qui il fait intervenir.

### Raccords

- Définition de l'anthropie : écartée (page de faits, règle 4 de « Architecture des ressources »).
- Livre *Un président peut-il tenir ses promesses ?* : retenu (bloc d'appel : « Cette page dit qui signe. Le livre pose la
  question suivante… »).
- Working paper : écarté (aucun ne fonde cette lecture).
- Pages voisines : retenues — « Qui peut faire adopter une loi ? » (« Ces procédures sont détaillées dans la page… »),
  « Un président peut-il recourir au référendum ? » et « Que peut décider la France dans l'Union européenne ? » (section
  « Avant d'évaluer une promesse présidentielle, que faut-il vérifier ? »).

## Fiche D0

Résultat visé, au plus près de la finalité : qu'un lecteur (internaute, élu, association, chercheur) puisse dire, sans la
déformer, ce que le président signe seul et ce que cela exige ; diagnostics : requêtes de la Search Console (« pouvoirs du
président », « contreseing », « article 19 »), citations par les moteurs génératifs ; état initial et dates de relevé
(J+30, J+60 après la publication) : à inscrire dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` le jour de la
mise en ligne de la version reprise.

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : non fait à la reprise (page existante ; outillage du lot : `LOT.md`).
- Protocole du type (juridique-institutionnel) : fait (2026-11-17, relecture des sources `_R1a`, `_R1b`, textes relus sur
  Légifrance le 17/11).
- Scénarios d'architecture, panel avant, contre-expertise de phase A : faits à la refonte du 11/10/2026
  (`REFONTE_PILOTE\PRESIDENT\`) ; non refaits à la reprise (motif : méthode de reprise, § R2).
- Gardes vues mordre : fait (autotest du générateur, 15 gardes, 2026-11-17).
- Figures téléphone : fait (parité vérifiée par le générateur ; date de lecture ajoutée à la figure le 17/11).
- Relecture de langue : faite sur les phrases nouvelles (rapport du lot).
- Recette 320-1 440 px : faite (`CAPTURES\`, débordement 0).
- Juge interne à l'aveugle : voir `LOT.md`.
- Relecture phrase à phrase FR et EN, instantané de relecture : à la publication.
- Contre-expertise de la page : paquet externe du lot (à envoyer par l'auteur).
- Accord de l'auteur : non fait (préparation de nuit).
