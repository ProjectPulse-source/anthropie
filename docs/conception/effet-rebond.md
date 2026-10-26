# Fiche de conception — Qu'est-ce que l'effet rebond (paradoxe de Jevons) ?

<!-- Refonte de présentation du 26/10/2026 (demande de l'auteur : encadrés et graphes structurants). Fiche écrite après le
pilote de l'effet rebond et avant la publication ; la page n'est pas déclarée refondue : les étapes non faites sont dites
ci-dessous. -->

Page : `/effet-rebond/` (FR) · `/en/rebound-effect/` (EN) · ouverte le 2026-07-24 · fiche du 2026-10-26

## Forme

`notion` : une définition sourcée, son origine, sa frontière avec les notions voisines, un exemple et une limite ou un
contre-exemple. L'encadré « La notion en bref » les rend visibles en tête ; le schéma montre le mécanisme ; la comparaison
trace la frontière. Aucun chiffre publié, donc pas de jeu de données.

## Fiche de conception

### Question centrale

Pourquoi un gain d'efficacité énergétique ne réduit-il pas forcément la consommation totale ?

### Enjeu

Les politiques d'efficacité annoncent des économies que le rebond rogne ; le lecteur doit pouvoir dire pourquoi, et jusqu'où.

### Croyance initiale

Plus efficace veut dire moins consommé.

### Découverte principale

Le service devenu moins cher est davantage utilisé : par trois canaux (direct, indirect, macroéconomique), la reprise rogne le gain, et peut le dépasser (paradoxe de Jevons).

### Mécanisme explicatif

Le prix : l'efficacité abaisse le coût du service, la demande augmente.

### Preuve décisive

Jevons, *The Coal Question* (1865) ; postulat de Khazzoom-Brookes ; Fressoz (*Sans transition*, 2024) sur l'addition des énergies.

### Limite

L'ampleur de chaque canal varie selon les usages et les secteurs ; le rebond n'annule pas tout gain.

### Valeur finale

Distinguer efficacité et sobriété, et demander où le coût s'est déplacé.

### Singularité

Cette page existe parce qu'elle relie le rebond au cadre anthropique (effet boomerang, AWP-04), ce que le lecteur ne découvre pas dans l'entrée courte du glossaire (lue : une définition de trois phrases).

### Raccords

- Définition de l'anthropie — retenu (« Pour aller plus loin »).
- Livre — retenu (*ANTHROPIE*, exemplaire de consultation).
- Working paper — retenu : AWP-04 (lecture anthropique et encadré).
- Pages voisines — glossaire retenu (paradoxe de Jevons, effet boomerang).

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
