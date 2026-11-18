# Fiche de conception — Dette publique : pourquoi 100 % du PIB ne pèse pas partout de la même façon

<!-- Fiche écrite le 17/11/2026, APRÈS la relecture des sources de la reprise « dette-b » : la page existait depuis le
29/09/2026 (arbitrages : `D:\PRO\06_PROMOTION\DOSSIER_PAGE_DETTE_INTERNATIONALE.md`), sans fiche. Découverte et mécanisme
citent la ligne de verdict qui les porte (rapport `D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\
dette-b\SOURCES\dette-publique-comparaison-internationale_R1.md`, noté « R1 »). -->

Page : `/dette-publique-comparaison-internationale/` (FR) · `/en/public-debt-international-comparison/` (EN) · ouverte le 2026-09-29 · fiche du 2026-11-17

## Forme

Données (`ressource.type: quantitatif`) : la page publie un jeu (`dette_monde` : Eurostat pour l'Union, strictement
comparable ; OCDE, FMI et Banque mondiale hors d'Europe, avec réserve) et en prend tout le modèle vérifié par machine ; elle
distingue trois niveaux de comparabilité et ne compare ses statistiques que sur une année.

## Fiche de conception

### Question centrale

Pourquoi deux pays également endettés ne consacrent-ils pas la même part de leurs recettes aux intérêts, et la monnaie
commune a-t-elle fixé le prix de la dette de ses membres ?

### Enjeu

Le classement par ratio de dette est le chiffre le plus repris des comparaisons ; il ne dit pas ce qu'une dette coûte, ni
ce qu'elle laisse de marge. Juger la France à son seul rang dans ce classement, c'est ignorer le prix de sa dette et le
niveau de ses recettes.

### Croyance initiale

À dette égale, charge égale ; et l'euro aurait fait converger les taux de ses membres vers celui de l'Allemagne.

### Découverte principale

En 2025, entre deux pays de l'Union voisins par la dette, la part des recettes absorbée par les intérêts peut varier de 1 à
3,2 (R1, l. 21 : CONFORME À LA SOURCE pour la Slovénie et la Hongrie, recalcul 3,238, maximum des paires de plus proches
voisins ; portée précisée par MO-30) ; la Hongrie ne doit que 1,09 fois ce que doit la Slovénie (R1, l. 23 : conforme).

### Mécanisme explicatif

La part des recettes absorbée par les intérêts est exactement le produit du stock de dette, de son prix (le taux implicite)
et de l'inverse des recettes, chacun rapporté au PIB : pour la Hongrie et la Slovénie, 1,09 × 2,75 × 1,08 = 3,2 (R1, l. 24 :
CONFORME À LA SOURCE, recalcul 3,2383) ; en logarithmes, le prix porte 86 % de l'écart, le stock et les recettes 7 % chacun
(R1, l. 25 : conforme). Cette décomposition dit ce qui contribue arithmétiquement, non pourquoi un pays se finance à ce taux
(R1, l. 26 : réserve exacte).

### Preuve décisive

Le nuage des pays de l'Union (dette et intérêts rapportés aux recettes), où les paires de plus proches voisins sont reliées
par une règle fixée avant le calcul, et la décomposition stock × prix × recettes qui l'accompagne ; pour la monnaie
commune, trente ans d'écarts de taux avec l'Allemagne, avec des pays restés hors de l'euro comme témoins.

### Pouvoir discriminant

Explications rivales réellement soutenues : « le niveau de la dette détermine son coût » ; « l'euro a fait converger les
taux » (lecture que l'on trouve chez la BCE, qui conduit cette politique) ; « garder sa monnaie protège ». Témoins : la
décomposition, qui ne change qu'un facteur à la fois, réfute la première pour la paire Hongrie-Slovénie ; la Suède, hors de
l'euro, converge avant 1999 comme l'Italie, ce qui réfute une explication de la convergence par la seule adoption de
l'euro ; la Hongrie décroche en 2012, ce qui réfute que garder sa monnaie protège tout le monde. Ce que la page ne tranche
pas : le rôle propre des interventions de la BCE, qu'elle ne sépare pas des autres facteurs de la période. Résistance : les
coefficients de la régression sur l'inflation gardent leur signe et leur ordre de grandeur d'une fenêtre de deux à cinq ans
à l'autre (MO-13).

### Limite

Une seule année pour les comparaisons de stock, de prix et de recettes ; hors de l'Union, des données moins comparables
(OCDE : passifs financiers bruts, estimations de l'édition n° 119 ; Banque mondiale : administration centrale seule) ; des
associations, non des causes ; aucune mesure du risque de crise.

### Valeur finale

Le lecteur sait pourquoi un ratio de dette ne suffit pas à comparer deux pays, et où se situe la France (prix, recettes,
part de dette à refinancer dans l'année) ; le chercheur dispose du tableau, du CSV et des statistiques ; l'élu, d'une
réponse chiffrée à la comparaison qu'on lui oppose.

### Singularité

Cette page existe parce qu'elle décompose la charge en stock, prix et recettes et éprouve le récit de la convergence par des
pays témoins, ce que le lecteur ne trouve ni dans les classements de dette d'Eurostat (lus : ratios seuls) ni dans les
rapports de convergence de la BCE (lus : juin 2024, qui ne confrontent pas l'euro aux pays restés en dehors sur trente ans).

### Raccords

Livre *Dette publique : qui paie vraiment ?* — retenu (encart). Définition de l'anthropie — retenue par l'encart
*ANTHROPIE*. Pages voisines : « Combien coûte la dette publique ? » (la transmission des taux au stock, mécanisme renvoyé
par le texte), « Qui paie » (les détenteurs de la dette), « Pourquoi la dette augmente » — retenues par les onglets du
dossier et des renvois. De Grauwe et Ji, Saka et al. — retenus, cités comme sources de lectures concurrentes.

## Fiche D0

Résultat visé, au plus près de la finalité : une page citée pour sa décomposition et son épreuve de la convergence, qui
serve le livre. Dates de relevé : non relevées dans cette reprise (motif : préparation de nuit) ; à inscrire dans
`D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` à la mise en ligne de la version reprise.

## Étapes de la méthode

- Relecture des sources par un agent neuf : fait (16-17/11/2026, R1, 30 écarts ; P1 de l'OCDE vérifié à la source par la
  session : version 1.5, édition n° 119).
- Sondes indépendantes de la session : fait (M-1 à M-6, S1-2, S1-5, S1-6).
- Interventions : fait (`specs\comparaison.py`, `specs\generateurs.py`, `specs\complements.py`, `specs\forme.py`), chaque
  écart trié (`SYNTHESE.md`) ; générateur relancé sur l'édition n° 119 (valeurs hors Union seules changées ; révision
  d'Eurostat de l'échéancier, `gov_10dd_ggd`, reprise et déclarée).
- Gardes vues mordre : garde « le Japon doit nettement plus que la France » (rapport des passifs > 1,3) ; jetons nouveaux
  `ocde_edition`, `jpn_fra_fois`.
- Figures téléphone : fait (transmission et zoom des prix régénérés ; `check-figures.py` : 0 défaut).
- Recette 320-1 440 px : fait (débordement 0 ; lecture sous sa figure).
- Relecture de langue outillée : fait ; phrase à phrase : à la publication.
- Premier écran : change (résultat, question « Pourquoi la Hongrie… ») ; test par lecteurs du premier écran seul : voir
  `PREMIER_ECRAN\` du lot.
- Juge interne à l'aveugle : voir `JUGE\` du lot. Panel et gate : non fait (reprise ; juge interne et jugement externe en
  tiennent lieu). Instantané : à la publication. Contre-expertise : paquet préparé. Accord de l'auteur : en attente.
