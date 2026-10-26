# Fiche de conception — Qui peut faire face à une dépense imprévue ?

<!-- Page de données née de l'arbitrage PRO-20261026-033434 (graphe G1, scénario S2 : page de faits distincte, reliée à
la notion de réversibilité sociale par une phrase) et du comité de lecteurs du même jour. Fiche écrite AVANT le texte
de la page, après le test décisif sur les données (relevé direct de l'API Eurostat, 26/10/2026). -->

Page : `/qui-peut-faire-face-a-une-depense-imprevue/` (FR) · `/en/who-can-cope-with-an-unexpected-expense/` (EN) ·
ouverte le 2026-10-26

## Forme

`quantitatif` : une série officielle (Eurostat, enquête SILC, jeu `ilc_mdes04`), relevée par un générateur, modèle
complet des pages de données (jetons, gardes vues mordre, JSON et CSV, figure SVG et PNG avec version téléphone, carte de
partage et vignette, `Dataset`, « Réutiliser », mise à jour au calendrier de la source). Critères : définitions et
périmètres (personnes, non ménages ; seuil de 60 % du revenu médian équivalent ; « dépense imprévue » au sens de
l'enquête), millésimes (année d'enquête), dénominateurs, changements de série (UE à 27 depuis 2010 seulement), aucune
lecture anthropique dans l'exposé des constats (décision verrouillée).

## Fiche de conception

### Question centrale

Qui, en France, ne pourrait pas faire face à une dépense imprévue — et le revenu suffit-il à le dire ?

### Enjeu

Les politiques sociales et le débat public classent les ménages par le revenu (pauvres ou non). Si la capacité d'encaisser
un choc dépend aussi, fortement, de la composition du foyer, une partie des personnes vulnérables échappe à ce classement.

### Croyance initiale

Ne pas pouvoir faire face à une dépense imprévue, c'est être pauvre ; au-dessus du seuil de pauvreté, on s'en sort.

### Découverte principale

Au-dessus du seuil de pauvreté, être le seul adulte d'un foyer avec enfants va de pair avec une vulnérabilité au choc
nettement plus forte : en France en 2025, 46,9 % des parents seuls au-dessus du seuil ne pourraient pas faire face à une
dépense imprévue, contre 18,6 % des couples avec un enfant (chiffres à afficher par jetons, jamais saisis).

### Mécanisme explicatif

Un seul revenu et un seul filet (épargne, entourage, second salaire) pour un foyer qui porte des charges d'enfants : le
seuil de pauvreté, calculé sur un revenu par unité de consommation, ne dit rien de la réserve disponible ni du nombre
d'adultes qui pourraient la reconstituer. Mécanisme proposé, non mesuré par la série : la page le dit.

### Preuve décisive

Le témoin à une seule variable : à présence d'enfants constante, le passage de deux adultes à un seul ajoute de 21 à 29
points (France, 2015-2025, au-dessus du seuil) ; sans enfants, le même passage n'en ajoute que 9 à 13. Même ordre dans
l'UE à 27 (20 à 24 contre 10 à 11). La lecture tient chaque année de la série.

### Pouvoir discriminant

- **Explications rivales réellement soutenues.** (a) La vulnérabilité au choc est d'abord une affaire de revenu : c'est la
  lecture implicite des indicateurs de pauvreté monétaire. (b) La composition du foyer pèse en elle-même, au-delà du
  revenu par unité de consommation (travaux de l'Insee et de la Drees sur les familles monoparentales : à lire et citer
  avant publication, NON_VERIFIE à ce jour).
- **Témoin à une variable.** Parent seul contre couple avec un enfant (le nombre d'adultes change, la présence d'enfants
  reste) ; adulte seul contre couple sans enfant (même changement, sans enfants) ; le tout de chaque côté du seuil.
- **Que révèle le graphe qu'une série isolée ne montre pas ?** Que l'écart lié à la composition est le plus grand
  au-dessus du seuil, là où le classement par le revenu dit « pas pauvre ».
- **Quelles explications départage-t-il ?** Il dément (a) prise seule : à revenu relatif du même côté du seuil, la
  composition change fortement la part exposée. Il ne départage pas (b) d'une troisième lecture : les parents seuls
  au-dessus du seuil pourraient être plus proches du seuil que les couples (position dans la tranche) ; le jeu ne
  ventile pas par décile. La page l'écrit au contact du chiffre.
- **Une variable, à une nuance près.** La catégorie d'Eurostat « un adulte avec enfants dépendants » compte un enfant ou plus ;
  la variante « couple avec deux enfants » (écart maintenu) montre que le nombre d'enfants ne suffit pas à expliquer l'écart.
  La page le dit au lieu d'annoncer des foyers qui « ne diffèrent que d'une chose » (relecture du 26/10/2026).
- **Robustesse, montrée par une variante calculée.** Chaque année de 2015 à 2025 (et depuis 2004 pour l'écart principal),
  France et UE à 27 ; couple avec un enfant et couple avec deux enfants.
- **Levier ou risque éclairé.** Un ciblage des aides par le seul revenu laisse de côté une part des foyers où un seul
  adulte porte les charges ; la page le dit comme question, sans recommander une politique.

### Limite

Déclaratif (« le ménage pourrait-il faire face… ») ; un indicateur de la capacité financière d'absorber un choc, une
seule part de ce que l'auteur appelle « réversibilité sociale » (ni le tarif de l'échec, ni la réadmission) ;
association, non cause ; montant de la dépense imprévue fixé par pays dans l'enquête ; personnes, non ménages.

### Valeur finale

Un chiffre citable et sourcé, un graphe qui montre ce que le classement par le revenu ne montre pas, et la question qui
reste ouverte (la position dans la tranche de revenu).

### Singularité

Cette page existe parce qu'elle croise seuil de pauvreté et composition du foyer en ne changeant qu'une variable, ce que
le lecteur ne trouve pas, à notre connaissance, dans les publications d'Eurostat et de l'Insee sur l'indicateur
(recherche du 26/10/2026 : Eurostat publie la part des personnes seules avec enfants, 56 % en 2019, communiqué du
05/05/2020, et l'Observatoire des inégalités 56 % des familles monoparentales, tous deux sans le seuil de pauvreté ;
aucun croisement trouvé — une recherche n'est pas exhaustive ; à revoir si une publication le donne).

### Raccords

- Définition de l'anthropie — écartée du corps de la page (page de faits, décision verrouillée) ; la notion de
  réversibilité sociale renvoie à cette page par une phrase, et non l'inverse dans l'exposé des constats.
- Livre — retenu : *La Société du premier coup* (inégalités et possibilités de recommencer), appel en fin de page,
  `ressource.livres`.
- Working paper — retenu dans un bloc séparé : AWP-08, qui propose la capacité de repli comme une composante de la
  réversibilité sociale (hypothèse de l'auteur, « non testée ici »).
- Pages voisines — `/reversibilite-sociale/` (phrase de renvoi ajoutée dans la notion) ; `/premier-coup/`.

## Fiche D0

Résultat visé au plus près de la finalité : la page citée pour son croisement (enseignants, presse, chercheurs) et lue
jusqu'à la limite. Diagnostics : vues, sources d'arrivée, citations ; test de compréhension par trois lecteurs réels
(décision D2). État initial : page nouvelle, aucune vue ; relevé au J+60 de l'architecture des ressources.

## Étapes de la méthode

- Plan d'outils : fait le 26/10/2026 (méthode, LanguageTool, recette, séries statistiques).
- Protocole du type `quantitatif` : fait — définitions (personnes, seuil, déclaratif), millésime affiché, ruptures de
  série lues dans les drapeaux d'Eurostat (France 2020 et 2022) et citées par jeton, aucune lecture anthropique dans les
  constats (hypothèse de l'auteur dans un encadré séparé).
- Scénarios d'architecture : tranché par l'arbitrage PRO-20261026-033434 (S2, page distincte, renvoi depuis la notion).
- Panel avant : comité de lecteurs simulés du 26/10/2026 (D1, D2, témoin à une variable).
- Contre-expertise de phase A : faite (PRO-20261026-033434, arbitrée).
- Gardes vues mordre : faites — 12 gardes de prose et 1 bande de plausibilité, chacune mutée
  (`--mutation=total|dessus|dessous|ratio|ecarts|chaque|serre|ue|deux|majorite|rupture|annee`), toutes ont mordu.
- Figures téléphone : faites — versions `-m` recomposées, parité contrôlée par `pied_figure.parite`, hauteurs déclarées
  dans les deux pages contrôlées par le générateur.
- Relecture de langue : faite (LanguageTool FR et EN sur le texte servi ; signalements tranchés : accords justes,
  artefact d'extraction, titre français, orthographe britannique).
- Recette 320-1280 : faite (`recette.py`, 12/12) après correction du composant « Réutiliser » (marge de défilement des
  ancres intérieures, 1,5rem → 5rem, pour toutes les pages).
- Gate éditorial — **auto-évaluation, non indépendante** : exactitude *tenu* (gardes, témoin, limite au contact du
  chiffre) ; clarté *tenu* ; accroche *tenu* (question et contre-intuition en chapô) ; progression *tenu* (constat →
  test → Europe → limites) ; originalité *partiel* (croisement non trouvé publié, recherche non exhaustive) ; valeur
  finale *tenu* (chiffre citable, question ouverte). Cinq fonctions remplies ; aucun bloc sans apport repéré.
- Relecture phrase à phrase FR et EN du texte servi : faite le 26/10/2026 ; six corrections (nuance « une variable »,
  nombre d'enfants, bandeau des années, pronom, redondance, « as high »).
- Instantané de relecture : fait (`docs/relectures/`, FR 99 phrases, EN 92).
- Test de compréhension par trois lecteurs réels (D2) : non fait (recrutement par l'auteur).
- Contre-expertise de la page : non faite (à décider après publication).
- Accord de l'auteur : demandé avec le diff du 26/10/2026.
