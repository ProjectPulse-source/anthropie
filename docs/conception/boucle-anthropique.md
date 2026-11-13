# Fiche de conception — Qu'est-ce que la boucle anthropique ?

<!-- Fiche écrite le 13/11/2026 par la reprise du lot « notions-a » (méthode METHODE_REPRISE_RESSOURCE.md, étape 4),
APRÈS la relecture des sources (`06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\notions-a\SOURCES\boucle-anthropique_R1.md`,
désignée ci-dessous « R1 »). La page existait sans fiche (en ligne depuis le 24/07/2026). -->

Page : `/boucle-anthropique/` (FR) · `/en/anthropic-loop/` (EN) · ouverte le 2026-07-24 · fiche du 2026-11-13

## Forme

`notion` : une définition sourcée (cinq états conditionnels, AWP-07) ; son origine (l'auteur, et ses filiations : Kapp,
Georgescu-Roegen, Stiegler, Beck) ; sa frontière (homonymie avec la néguanthropie de Stiegler ; voisins nommés par
AWP-07) ; des exemples à niveaux de preuve différents (Rome, dette publique, environnement, numérique) et un tour complet
codé (l'amiante) ; ses limites (ce qui n'est pas établi, dans chaque lecture). L'encart sur la dette publie des nombres
tirés du jeu `dette_dynamique` ; le texte de la lecture « Dette publique » est saisi dans `data/boucle_exemples.yaml`,
hors des gardes (point ouvert).

## Fiche de conception

### Question centrale

Que devient une charge qu'un système social déplace ailleurs ?

### Enjeu

On voit l'ordre et rarement le trajet de ce qu'il déplace ; sans grille, chaque retour se lit comme un problème neuf.

### Croyance initiale

Un coût déplacé disparaît dans un ailleurs sans mémoire ; ou, à l'inverse, il revient toujours.

### Découverte principale

Aucun passage n'est obligé : déplacement, accumulation, saturation, retour, bifurcation sont des états conditionnels,
et sur les quatre lectures de la page, seuls les deux premiers états sont documentés (dette, numérique) ou le
déplacement seul (environnement) ; la saturation n'est établie dans aucun cas contemporain. Porté par R1, l. 12-17 et
24-31 (conformes à la v2 d'AWP-07, **non déposée** : R1, § 0) et P1 l. 143 (saturation non établie).

### Mécanisme explicatif

Une charge s'accumule si les apports dépassent ce que le réceptacle absorbe ; la saturation vient d'une limite de
capacité ou de la contestation ; le retour peut changer de forme. Porté par R1, l. 14-16 et 106-107 ; borné par R1-P0-2
(l'exemple du coût social en instabilité politique est un retour isomorphe) et R1-P1 l. 108 (que la transmutation
explique la rareté des imputations est une hypothèse, non un résultat).

### Preuve décisive

AWP-07 (définitions, conditions, protocole ex ante) ; pour l'amiante, le rapport du Sénat de 2005 (latence, financement
par la branche AT-MP) et l'interdiction de 1997 ; pour la dette, les comptes publics (jeu `dette_dynamique`, Eurostat
et Insee, 115,7 % du PIB fin 2025).

### Pouvoir discriminant

Partiel. L'encart sur la dette montre une décomposition comptable, qui décrit sans attribuer de cause (la page le dit) ;
pour la hausse des intérêts, deux lectures sont posées (début d'un retour, ou hausse des taux et de l'inflation) et la
page dit qu'elle ne les départage pas. Ailleurs, sans objet : les lectures illustrent la grille, elles ne la testent pas.

### Limite

Un modèle conditionnel, non une trajectoire démontrée ; Rome est une lecture illustrative ; l'emboîtement des tours est
une hypothèse de recherche ; l'amiante montre l'usage de la grille, il ne la valide pas. La page décrit la v2 d'AWP-07,
non déposée, sous le DOI de la v1 (R1, § 0) : décision de l'auteur (`A_ARBITRER.md`).

### Valeur finale

Devant un coût déplacé, demander où il s'accumule, ce qui le ferait saturer, sous quelle forme il pourrait revenir — et
nommer le réceptacle et la latence avant l'analyse.

### Singularité

Cette page existe parce qu'elle montre la boucle sur quatre terrains, avec ce qui est établi et ce qui ne l'est pas dans
chacun, ce que le lecteur ne trouve ni dans AWP-07 (formel, un seul cas codé dans la v1) ni dans la page de définition
de l'anthropie (cinq lignes de la spirale).

### Raccords

- Définition de l'anthropie — retenu (renvoi au premier paragraphe et « Pour aller plus loin »).
- Livre — retenu, sans lui prêter la boucle (le livre n'emploie pas l'expression : R1-P1 l. 150).
- Working papers — retenus : AWP-07 (formalisation), AWP-02, AWP-04, AWP-06, AWP-08, AWP-09.
- Pages voisines — effet rebond, générations futures et dette, réversibilité sociale : retenues ; glossaire : retenu.

## Fiche D0

Non faite dans cette reprise (motif : préparation, sans publication ; à poser à la publication dans
`06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`). Résultat visé : une notion citée avec ses conditions (« aucun passage
n'est obligé »), sans être prise pour une trajectoire démontrée.

## Étapes de la méthode

- Plan d'outils : non fait dans cette reprise (motif : page existante, méthode de reprise).
- Protocole du type `notion` : fait le 13/11/2026 (R1 : 111 phrases, 2 P0, 10 P1, 13 P2).
- Scénarios d'architecture : non fait (motif : reprise localisée, architecture inchangée).
- Panel avant / après : non fait (motif : la méthode de reprise écarte la lecture simulée de la page entière).
- Gardes vues mordre : non fait — le texte de la lecture « Dette publique » (`boucle_exemples.yaml`) est saisi à la main,
  hors garde ; la valeur 115,6 % était périmée (R1-P1 l. 43). Point ouvert : jetons du jeu `dette_dynamique` dans ce
  texte.
- Figures : la spirale et ses quatre lectures sont inchangées en géométrie ; leur texte change (lot du 13/11/2026).
- Relecture de langue : faite sur les phrases nouvelles (13/11/2026, voir le lot).
- Recette 320-1280 : faite sur la version proposée (13/11/2026, `captures.py`).
- Gate éditorial, relecture phrase à phrase FR et EN, instantané de relecture : non faits (motif : à la publication).
- Accord de l'auteur : non demandé (motif : jugement externe d'abord ; décision sur AWP-07 v2 requise).
