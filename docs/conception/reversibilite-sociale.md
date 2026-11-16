# Fiche de conception — Qu'est-ce que la réversibilité sociale ?

<!-- Refonte de présentation du 26/10/2026 (demande de l'auteur : encadrés et graphes structurants). Fiche écrite après le
pilote de l'effet rebond et avant la publication ; la page n'est pas déclarée refondue : les étapes non faites sont dites
ci-dessous. -->

Page : `/reversibilite-sociale/` (FR) · `/en/social-reversibility/` (EN) · ouverte le 2026-07-24 · fiche du 2026-10-26

## Forme

`notion` : une définition sourcée, son origine, sa frontière avec les notions voisines, un exemple et une limite ou un
contre-exemple. L'encadré « La notion en bref » les rend visibles en tête ; le schéma montre le mécanisme ; la comparaison
trace la frontière. Aucun chiffre publié, donc pas de jeu de données.

## Fiche de conception

### Question centrale

Que peut-on se permettre de rater, et cette capacité est-elle également répartie ?

### Enjeu

Une inégalité que ni le revenu ni la mobilité ne mesurent gouverne qui peut essayer.

### Croyance initiale

Rebondir après un échec est affaire de psychologie (résilience).

### Découverte principale

Selon AWP-08, la capacité de rebondir dépend du repli, de la trace (tarif d'échec) et de la réadmission ; l'hypothèse propre du cadre est la complémentarité du repli et de la trace, et sa première proposition, à tester, est que cette capacité agit avant l'échec, sur la décision d'essayer (relecture R1, l. 79 et 85-87 ; AWP-08, résumé et § 5.1-5.2 ; sonde de la session, AWP-08 l. 23-24).

### Mécanisme explicatif

V = f(C, T, A), avec complémentarité du repli et de la trace (P4), hypothèse à tester ; quand la trace ferme une porte en tout-ou-rien, le repli ne la rouvre pas (R1, l. 73 et 79 ; AWP-08 § 2.2 et § 5.2).

### Preuve décisive

AWP-08 (architecture de mesure, protocole d'identification) ; deux terrains datés : indicateur 040 du FIBEN (supprimé en 2013, décret n° 2013-799 ; le même décret a porté de trois à cinq ans la communication de l'information de liquidation : R1, l. 52 a), loi Lemoine (2022).

### Pouvoir discriminant

Sans objet : la page ne publie aucune série ; ses schémas décrivent un mécanisme, ils ne départagent pas d'explications
(champ ajouté le 26/10/2026, arbitrage PRO-20261026-033434).

### Limite

Un cadre réfutable, non un résultat empirique.

### Valeur finale

Lire les politiques de la seconde chance selon les composantes sur lesquelles elles agissent.

### Singularité

Cette page existe parce qu'elle pose une troisième dimension de l'inégalité, ce que le lecteur ne trouve ni dans les mesures de revenu et de mobilité ni dans le discours sur la résilience (lus).

### Raccords

- Définition de l'anthropie — retenu (lecture anthropique, AWP-01 et AWP-07).
- Livre — retenu : *La Société du premier coup* et sa page compagnon.
- Working paper — retenu : AWP-08.
- Pages voisines — glossaire retenu.

## Fiche D0

Non faite pour cette refonte de présentation (motif : aucune fiche D0 antérieure dans la feuille de route GEO pour
cette page). Résultat visé au plus près de la finalité : une notion comprise et citée correctement (lecteurs, enseignants,
moteurs de réponse) ; état initial à relever au relevé J+60 déjà prévu pour l'architecture des ressources (25/10/2026).

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait le 26/10/2026 (méthode et fiche, LanguageTool, recette retenus ;
  MAGNIFIER et panel : voir ci-dessous).
- Protocole du type `notion` : fait le 26/10/2026 — l'encadré « La notion en bref » rend visibles définition, origine,
  frontière, exemple, limite ou portée, lecture anthropique, tous repris de la page (aucun fait nouveau).
- Scénarios d'architecture : deux pesés le 26/10/2026 — (a) figures SVG dessinées page par page, version téléphone à part ;
  (b) un organe commun en HTML et CSS (fiche, schéma en étages, comparaison, carte), contenu dans le front matter de
  chaque page. Retenu : (b), texte lisible, traduit et indexable, une seule mise en page qui passe en colonne.
- Panel avant / après : non fait (motif : refonte de présentation, texte de la page inchangé ; à décider par l'auteur).
- Contre-expertise de phase A : non faite (motif : aucune décision de fond en dépend).
- Gardes vues mordre : `glossaire-carte` arrête le build sur une ancre absente (témoin : `derisking-x`, build en échec,
  26/10/2026) ; `notion-comparaison` arrête le build sur une ligne au mauvais nombre de valeurs.
- Figures téléphone : faites — mise en page en colonne sous 600-680 px, mesurée à 320 et 390 px.
- Relecture de langue : faite le 26/10/2026 (LanguageTool FR et EN sur tous les textes des encadrés ; signalements
  tranchés : orthographe britannique des pages, « a commons », « marché de droits »).
- Fidélité à la page : faite le 26/10/2026 ; une ligne retirée parce qu'elle ne venait pas de la page (« Ce qu'elle
  gouverne », réversibilité sociale).
- Recette 320-1280 : faite le 26/10/2026 (10 pages × 4 largeurs, aucun débordement de page ni de composant).
- Gate éditorial : non fait (motif : présentation seule).
- Relecture phrase à phrase FR et EN du texte servi en entier : non faite (seuls les textes neufs relus) ; condition de
  `ressource.refonte`, qui n'est donc pas posée.
- Instantané de relecture : non fait (suit la relecture entière).
- Contre-expertise de la page : non faite.
- Accord de l'auteur : demandé avec le diff du 26/10/2026.

### Reprise du 16/11/2026 (lot « notions-b », `/reprise-ressource`, mode préparer)

- Relecture des sources par un relecteur neuf : faite (`06_PROMOTION/INTELLIGIBILITE_RESSOURCES_2026-11-11/LOTS/notions-b/SOURCES/reversibilite-sociale_R1.md`), trois lignes sondées à la source par la session (`SONDES_SESSION.md`).
- Interventions : spécification rejouable `LOTS/notions-b/specs/reversibilite-sociale.py` ; contrôle de la lettre justifié ligne à ligne.
- Juge interne à l'aveugle et jugement externe : voir `LOTS/notions-b/LOT.md`. `ressource.refonte` : non posée (relecture phrase à phrase entière et instantané à faire à la publication).

