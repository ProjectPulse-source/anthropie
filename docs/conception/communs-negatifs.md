# Fiche de conception — Qu'est-ce que les communs négatifs ?

<!-- Refonte de présentation du 26/10/2026 (demande de l'auteur : encadrés et graphes structurants). Fiche écrite après le
pilote de l'effet rebond et avant la publication ; la page n'est pas déclarée refondue : les étapes non faites sont dites
ci-dessous. -->

Page : `/communs-negatifs/` (FR) · `/en/negative-commons/` (EN) · ouverte le 2026-07-26 · fiche du 2026-10-26

## Forme

`notion` : une définition sourcée, son origine, sa frontière avec les notions voisines, un exemple et une limite ou un
contre-exemple. L'encadré « La notion en bref » les rend visibles en tête ; le schéma montre le mécanisme ; la comparaison
trace la frontière. Aucun chiffre publié, donc pas de jeu de données.

## Fiche de conception

### Question centrale

Que faire de ce dont nous héritons sans l'avoir choisi ?

### Enjeu

Déchets, sols pollués, infrastructures obsolètes : des charges qui exigent soin et institutions, pas seulement un prix.

### Croyance initiale

Un dommage environnemental est une externalité, corrigible par un prix.

### Découverte principale

Les communs négatifs inversent la figure d'Ostrom : la chose partagée est une charge, et la question devient qui en prend soin, comment, et combien de temps.

### Mécanisme explicatif

Lecture anthropique : le désordre déplacé s'accumule et sature ; ce qui reste devient un héritage matériel.

### Preuve décisive

Monnin, Bonnet et Landivar (*Héritage et fermeture*, 2021) ; Kapp (cost-shifting) ; Vuillemey (responsabilité limitée).

### Limite

La page ne mesure aucun stock d'héritage ; le numérique y est un commun négatif *candidat* (AWP-06).

### Valeur finale

Une notion d'action : maintenir, refermer, démanteler, dépolluer.

### Singularité

Cette page existe parce qu'elle relie les communs négatifs à la boucle anthropique (le trajet) et à la dette technologique, ce que le lecteur ne trouve ni chez Monnin (lu : sans le cadre anthropique) ni dans l'entrée du glossaire.

### Raccords

- Définition de l'anthropie — retenu (lecture anthropique).
- Livre — retenu (*ANTHROPIE*).
- Working paper — retenu : AWP-06.
- Pages voisines — boucle anthropique (schéma) et dette technologique retenues.

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
