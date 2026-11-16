# Fiche de conception — La Société du premier coup : sources, compléments et mises à jour

Page : `/premier-coup/` (FR seul ; repli `/en/books/`, exclusion déclarée) · ouverte le 2026-07-29 · fiche écrite le
2026-11-16, après la relecture des sources du lot « reperes-b » (reprise des ressources), page existante sans fiche.

## Forme

**Corpus** (`ressource.type: ["corpus"]`), appareil d'un livre (`appareil_de`), hors de l'index `/ressources/`
(arbitrage PRO-20261025-225715). Critères propres, une ligne chacun : grille uniforme pour chaque entrée (double statut
d'existence et de preuve pour le répertoire ; source primaire, millésime, portée, qualification et réserve pour les
repères) ; chaque entrée datée et sourcée ; ancres permanentes ; frontière explicite entre le documenté et l'inféré.

## Fiche de conception

### Question centrale

Que sait-on, preuves à l'appui, des dispositifs qui rouvrent une trajectoire, et que valent les chiffres sur lesquels
*La Société du premier coup* fonde son constat ?

### Enjeu

- **L'internaute, lecteur du livre** : retrouver la source et la date de chaque chiffre du livre, et ses corrections.
- **Le politique et les associations** : une gamme de dispositifs avec, pour chacun, ce qui est prouvé et ce qui ne
  l'est pas — de quoi ne pas confondre une loi votée, un dispositif fréquenté et un effet mesuré.
- **Le chercheur** : les références exactes, les statuts probatoires, et les pistes données pour ce qu'elles sont,
  inférées et non testées.

### Croyance initiale

Un dispositif qui existe et qui est très utilisé « marche » ; un chiffre de rapport public vaut pour tous et pour
longtemps.

### Découverte principale

Les dispositifs dont l'effet est établi causalement sont peu nombreux, et ils viennent des publics les plus lourds
(« Un chez-soi d'abord », soutien à l'emploi IPS) ; beaucoup d'autres sont légiférés, déployés ou fréquentés sans effet
mesuré. Porté par la relecture `premier-coup_R1a.md` (lignes 62-63 et notes 16-17 : CONFORMES À LA SOURCE ; Tinland
et al. 2020, Frederick et VanderWeele 2019) et par ses écarts, qui ont fait retirer à la page ce qu'elle disait de trop
(le crédit renchéri « pour tous » : S3 ; le Connecticut « premier » : S2).

### Mécanisme explicatif

L'écart d'usage : entre un droit ouvert et son usage, la démarche à faire écarte ceux qui ne la font pas (Michigan :
environ 6,5 % des éligibles obtiennent l'effacement en cinq ans, Prescott et Starr 2020, R1a note 1, CONFORME À LA
SOURCE) ; le non-recours mesuré par la DREES en est la version française (R1b, RSA et prime d'activité, CONFORMES). Que
cet écart favorise les mieux informés est une synthèse de l'auteur, non un résultat mesuré (R1a P1-6) : la page le dit
désormais.

### Preuve décisive

Les deux essais randomisés et la méta-analyse cités (Tinland et al., *Epidemiology and Psychiatric Sciences*, 2020 ;
Frederick et VanderWeele, *PLoS ONE*, 2019, risque relatif 1,63), et l'expérience de terrain d'Agan et Starr (*QJE*,
2018) pour l'avertissement causal ; pour les repères, les publications des producteurs (DREES, IGAS, Céreq, Banque de
France, MESR), relues dans leur version la plus récente (R1b ; sondes S12 à S14).

### Pouvoir discriminant

Sans objet au sens d'une page de données : la page ne trace aucun graphe. Son pouvoir de tri est le double statut
(existence, preuve), qui sépare ce qu'une lecture rapide confond : un dispositif légiféré (fichier positif, censuré), un
dispositif fréquenté (France Services, sans contrefactuel) et un effet mesuré (IPS).

### Limite

La page recense, elle ne prescrit pas ; les pistes de la partie II sont inférées ou spéculatives, jamais testées. Les
repères sont ceux du livre : plusieurs séries ont paru depuis (lignes « Mise à jour ») ; deux nombres sur Visale restent
non vérifiés (`LOTS\reperes-b\A_ARBITRER.md`).

### Valeur finale

Le lecteur peut dire, pour un dispositif donné, s'il existe, s'il est utilisé et si son effet est prouvé, et retrouver
la source et la date de chaque chiffre du livre.

### Singularité

Cette page existe parce qu'elle donne, pour chaque dispositif, son statut de preuve, que le lecteur ne trouve pas dans
le livre (qui annonce le répertoire p. 105 sans le reproduire) ni dans les rapports publics, qui décrivent un dispositif
à la fois.

### Raccords

- **Retenu — le livre *La Société du premier coup*** (`ressource.livres`, bloc `consultation`) : la page est son appareil.
- **Retenu — `/reversibilite-sociale/`** et **AWP-08** : « pour le concept, voir […] ; pour sa formalisation
  scientifique, AWP-08 » (ouverture de la page).
- **Retenu — `/combien-de-temps-une-erreur-reste-inscrite/`** : renvois des repères FICP et casier.
- **Écartée — une FAQ** : volontaire (doctrine GEO-04, front matter) ; la question conceptuelle appartient à
  `/reversibilite-sociale/`.

## Fiche D0

Résultat visé : citations exactes de la page et du livre par les lecteurs, enseignants et chercheurs (renvois vers les
ancres des repères). Diagnostics : visites des ancres `#reperes` et `#repertoire`, mentions par les moteurs génératifs.
État initial et dates de relevé : à inscrire à la publication dans `06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`.

## Étapes de la méthode

- Relecture des sources : fait (16/11/2026, `LOTS\reperes-b\SOURCES\premier-coup_R1a.md` et `_R1b.md`, sondes S1-S3 et
  S12-S14).
- Fiche de conception : fait (16/11/2026, après la relecture).
- Corrections d'exactitude et définitions : fait dans la version proposée (`specs\premier-coup_a.py`, `_b.py`).
- Juge interne à l'aveugle, contre-expertise externe : à faire (lot « reperes-b »).
- Instantané de relecture, accord de l'auteur, publication : non fait (session « publier »).
- Jugement externe à l'aveugle (audit PRO-20261116-165827, 16/11/2026, réponse archivée avant lecture, SHA-256 2D243C03…65C0) : la version proposée retenue ; corrections tirées de son arbitrage (`06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\reperes-b\specs\externe.py`, `JUGE\ARBITRAGE_EXTERNE.md`). L'étude de Gropp, Scholz et White porte sur les exemptions patrimoniales de la faillite personnelle ; Housing First : absence de différence significative, non absence d'effet ; Visale : réponse d'enquête, non mesure d'effet ; « non évalué » ne veut pas dire « sans effet », dans la règle de lecture.
