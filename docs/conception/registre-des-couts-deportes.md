# Fiche de conception — Le Registre des coûts déportés

<!-- Fiche écrite le 26/10/2026, après coup : la page existe depuis le 15/08/2026 (dérivée de l'ancienne page
d'accueil) et n'a pas été conçue par la méthode. Elle fixe ce que la page doit tenir depuis l'arbitrage
PRO-20261025-225715 et les deux relectures contre le livre (630 p. FR, 644 p. EN). Page non déclarée refondue :
les étapes de la refonte non faites sont dites ci-dessous. -->

Page : `/registre-des-couts-deportes/` (FR) · `/en/register-of-offloaded-costs/` (EN) · ouverte le 2026-08-15 · fiche du 2026-10-26

## Forme

`corpus` (appareil documentaire d'un livre), doublé de `notion` (la grille ordre créé / dette déportée applique la
définition de l'anthropie). Critères du corpus : grille uniforme pour chaque entrée (date, titre, ordre créé, dette
déportée, catégories, pagination — tenu) ; chaque entrée datée et sourcée (pagination de l'édition en vente, 630 p. FR,
644 p. EN — tenu depuis le 26/10) ; fidélité au livre publié, dernière édition (relu chapitre par chapitre en FR le
26/10, puis contre l'édition anglaise le même jour) ; une ancre stable par entrée (`anchorize` du titre, figée par le
champ `ancre` quand un titre est corrigé) ; périmètre écrit en tête (« les 168 jalons du livre », sept âges du livre) et
ce que le Registre ne dit pas (section dédiée) ; aucune entrée ajoutée, retirée ou réécrite sans trace (journal de
page, trace dans `D:\PRO\06_PROMOTION\ARCHITECTURE_RESSOURCES_2026-10-25\FIDELITE_REGISTRE\`).

## Fiche de conception

### Question centrale

Que coûte chaque ordre que l'humanité a créé, et où ce coût est-il allé ? Le Registre pose la même question aux 168
jalons du livre ANTHROPIE.

### Enjeu

Le lecteur du livre (le QR code de « Pour aller plus loin », p. 619 FR, p. 631 EN, mène ici) et le lecteur qui découvre
l'hypothèse anthropique sans le livre : l'un cherche l'appareil du livre, l'autre la preuve que la grille s'applique
au-delà d'un exemple choisi.

### Croyance initiale

L'histoire se lit comme une suite de solutions — l'écriture, la monnaie, l'imprimerie, l'antibiotique règlent un
problème — et leurs coûts comme des effets secondaires accidentels.

### Découverte principale

Sur 168 jalons, de −3,3 millions d'années à 2024, chaque solution a un coût déplacé hors de son périmètre visible, et la
destination de ce coût migre : de l'espace (âges 1 à 3) au social (4 et 5), puis au temps et à l'attention (6 et 7).

### Mécanisme explicatif

L'hypothèse anthropique : un système qui crée de l'ordre localement exporte du désordre ailleurs, plus tard ou sur
d'autres ; quand un espace de déportation sature, la fuite s'invente ailleurs, plus abstraite et moins politisable
(postface du livre ; AWP-07 pour la boucle).

### Preuve décisive

La grille uniforme appliquée sans exception aux 168 chapitres, chaque entrée renvoyant à sa pagination dans le livre :
le lecteur peut vérifier une entrée contre son chapitre. La preuve est documentaire, pas statistique : la forme
documente, elle ne démontre pas.

### Limite

Le Registre condense un chapitre en deux phrases : il hérite des choix du livre (sélection des jalons, lecture de
l'auteur) et n'en teste pas l'exhaustivité ; « dette déportée » est une lecture interprétative, pas une mesure. La
section « Ce que le Registre ne dit pas » le dit en clair ; la limite figure aussi dans la définition liée.

### Valeur finale

Un index citable, entrée par entrée (ancres stables), qui permet de retrouver un chapitre du livre, de citer une
application précise de la grille et de juger l'hypothèse sur pièces plutôt que sur un exemple.

### Singularité

Cette page existe parce qu'elle révèle la grille appliquée aux 168 jalons d'un coup, ce que le lecteur ne découvre pas
dans la définition `/quest-ce-que-lanthropie/` (lue : un exemple par domaine) ni dans le glossaire (lu : les termes, sans
les jalons) ; le livre déploie chaque jalon mais ne les met jamais en regard sur une seule grille consultable.

### Raccords

- Définition de l'anthropie — retenu : « [les systèmes sociaux déplacent le désordre plutôt qu'ils ne le
  résolvent](/quest-ce-que-lanthropie/) » (section « Comment lire un jalon ») et `{{< canonical-definition >}}`.
- Livre — retenu : ligne d'appartenance (« Appareil documentaire du livre ANTHROPIE »), premier paragraphe, section
  sur le livre, exemplaire de consultation (`{{< consultation >}}`) ; réciproque sur la fiche du livre
  (`ressource.livres`).
- Working papers — retenus : AWP-07 (la boucle, qui formalise la trajectoire) et AWP-02 (lecture du Registre en longue
  durée), section « La trajectoire ».
- Pages voisines — glossaire retenu (vocabulaire du cadre, et distinction avec les registres de coûts couplés
  d'AWP-06) ; dossiers de faits (dette) écartés : le cadre ne se présente pas comme leur démonstration (arbitrage
  PRO-20261025-225715).

## Fiche D0

Non faite (motif : page antérieure à la règle, aucune fiche D0 dans la feuille de route GEO). Résultat visé au plus
près de la finalité : lecteurs arrivant du QR code du livre et citations du Registre par entrée ; état initial à
relever (Search Console, page FR et EN, 26/10/2026) au relevé J+60 déjà prévu pour l'architecture des ressources.

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : non fait (motif : fiche écrite après coup, page existante).
- Protocole du type `corpus` : fait le 26/10/2026 — grille, pagination (signets des PDF 630 et 644 p.), ancres
  (168/168 conservées, vérifiées contre la page en ligne), périmètre, journal.
- Scénarios d'architecture : fait le 25/10/2026 (arbitrage PRO-20261025-225715 : place dans l'index, ligne
  d'appartenance au lieu d'une barre de dossier).
- Panel avant / après : non fait (motif : pas de refonte narrative ; décision de l'auteur à prendre).
- Contre-expertise de phase A : faite pour l'architecture (PRO-20261025-225715), pas pour le texte des entrées.
- Gardes vues mordre : sans objet (aucun chiffre calculé) ; le compteur « Les N jalons du livre » est dérivé du JSON.
- Figures téléphone : sans objet (pas de figure).
- Relecture de langue : faite le 26/10/2026 sur les textes neufs et corrigés (LanguageTool FR et EN, signalements tous
  tranchés : termes du livre).
- Fidélité au livre : faite le 26/10/2026 — FR contre l'édition de 630 p. (43 corrections), EN contre l'édition de
  644 p. (51 titres, 20 corrections EN, 14 corrections FR reportées), âges alignés sur le livre (20 jalons).
- Recette 320-1280 : faite le 26/10/2026 (28 combinaisons en ligne, puis 8 sur le build avec pagination : aucun
  débordement ; arrivée par ancre sous l'en-tête collant, `scroll-margin-top` ajouté).
- Gate éditorial : non fait (motif : pas de refonte narrative).
- Relecture phrase à phrase FR et EN du texte servi en entier : non faite (seuls les textes neufs et corrigés ont été
  relus) ; condition de `ressource.refonte`, qui n'est donc pas posée.
- Instantané de relecture : non fait (suit la relecture entière).
- Contre-expertise de la page : non faite.
- Accord de l'auteur : demandé avec le diff du 26/10/2026.
