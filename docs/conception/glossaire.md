# Fiche de conception — Glossaire

<!-- Refonte de présentation du 26/10/2026 (demande de l'auteur : encadrés et graphes structurants). Fiche écrite après le
pilote de l'effet rebond et avant la publication ; la page n'est pas déclarée refondue : les étapes non faites sont dites
ci-dessous. -->

Page : `/glossaire/` (FR) · `/en/glossaire/` (EN) · ouverte le 2026-04-02 · fiche du 2026-10-26

## Forme

`notion` : une définition sourcée, son origine, sa frontière avec les notions voisines, un exemple et une limite ou un
contre-exemple. L'encadré « La notion en bref » les rend visibles en tête ; le schéma montre le mécanisme ; la comparaison
trace la frontière. Aucun chiffre publié, donc pas de jeu de données.

## Fiche de conception

### Question centrale

Quel est le vocabulaire opératoire du cadre anthropique, et comment ses termes s'articulent-ils ?

### Enjeu

Vingt-deux termes forgés ou réappropriés : sans vue d'ensemble, le lecteur les lit comme une liste.

### Croyance initiale

Un glossaire est un dictionnaire alphabétique.

### Découverte principale

Les termes s'organisent autour d'une hypothèse unique et d'ensembles nommés par l'introduction (mécanisme, seuils, configurations, posture), auxquels s'ajoutent les applications.

### Mécanisme explicatif

La carte du vocabulaire place chaque terme dans son ensemble et mène à son entrée.

### Preuve décisive

L'introduction du glossaire, qui nomme ces ensembles ; chaque entrée.

### Pouvoir discriminant

Sans objet : la page ne publie aucune série ; ses schémas décrivent un mécanisme, ils ne départagent pas d'explications
(champ ajouté le 26/10/2026, arbitrage PRO-20261026-033434).

### Limite

Le rangement des applications et du retour (boucle, effet Jevons) est un choix de présentation de la carte, non une définition ; validé par l'auteur le 26/10/2026 (« valide le rangement de la carte du glossaire »).

### Valeur finale

Une navigation par la structure du cadre, et non par l'ordre de la liste.

### Singularité

Cette page existe parce qu'elle définit les termes du cadre en un seul endroit, ce que le lecteur ne trouve pas dans les pages notions (lues : une notion chacune).

### Raccords

- Définition de l'anthropie — retenu (première entrée, cœur de la carte).
- Livre — retenu (*ANTHROPIE*).
- Working papers — retenus dans les entrées.
- Pages voisines — chaque page notion retenue par son entrée.

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
