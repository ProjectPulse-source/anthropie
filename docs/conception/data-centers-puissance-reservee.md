# Fiche de conception — Data centers : les gigawatts réservés annoncent-ils la consommation ?

<!-- Page de données née de l'arbitrage PRO-20261026-033434 (graphe G4, « accepté avec modification, en file » : deux
panneaux, puissances réservées et consommation effective et projetée, jamais un taux d'utilisation calculé entre GW et
TWh ; condition : chiffres lus dans une publication de RTE, datés ; une réservation n'est pas une charge irréversible).
Scénario S2 : page de faits distincte de la notion de dette technologique. Fiche écrite AVANT le texte, après la lecture
des trois publications de RTE (27/10/2026). -->

Page : `/data-centers-puissance-reservee/` (FR) · `/en/data-centres-reserved-capacity/` (EN) · ouverte le 2026-10-27

## Forme

`quantitatif` : publications de RTE (Bilan prévisionnel 2025-2035, volet consommation, décembre 2025 ; Bilan électrique
2025, février 2026 ; page « Les data centers en chiffres clés », mise à jour le 01/06/2026), téléchargées et lues par
`scripts/update_data_centers.py`. Aucune série statistique ouverte n'existe : les valeurs sont **transcrites**, et chaque
valeur transcrite est retrouvée par le script dans le texte de sa publication (garde) ; la répartition par statut des
réservations est **mesurée par script sur la géométrie vectorielle** de la figure 2.3 du Bilan prévisionnel, et
contrôlée contre les totaux que RTE écrit en toutes lettres (14 / 9,5 / 6,5 GW). Critères du type : définitions (puissance
de raccordement réservée ≠ puissance appelée ≠ consommation ; sites dédiés ≠ centres internes ; réseau de transport ≠
distribution), dates distinctes de chaque valeur, périmètres non mélangés, valeurs transcrites déclarées, écart entre
publications du même producteur dit, aucune lecture anthropique dans les constats.

## Fiche de conception

### Question centrale

Les gigawatts que les data centers réservent sur le réseau électrique annoncent-ils une consommation du même ordre, et
pour quand ?

### Enjeu

Le chiffre qui circule est celui des réservations (« 18 GW »), souvent converti en réacteurs ou en logements. Si une
réservation n'est qu'une option sur le réseau, dont une part se réalise lentement et une autre s'abandonne, le débat
public mesure le mauvais objet — et ne voit pas ce qui engagerait vraiment la collectivité.

### Croyance initiale

Une puissance réservée est une consommation annoncée : 18 GW de data centers, c'est l'équivalent d'une douzaine de
réacteurs qui tourneront pour eux.

### Découverte principale

En dix-huit mois, la puissance réservée par les data centers auprès de RTE a plus que triplé (environ 5 GW fin 2024,
14 GW en novembre 2025, près de 18 GW en mai 2026). La consommation mesurée des centres raccordés au réseau de transport,
elle, est passée de 0,8 TWh en 2024 à près de 1 TWh en 2025. Sur les 14 GW de novembre 2025, plus de la moitié vise une
mise en service à partir de 2030, et près d'un gigawatt de réservations a été abandonné depuis 2023. RTE lui-même ne
convertit pas les réservations en consommation : ses deux trajectoires donnent 10 à 15 TWh en 2030.

### Mécanisme explicatif

Une réservation (proposition technique et financière signée) garantit une capacité d'accès au réseau ; elle ne
dit ni si le site sera construit, ni quand, ni à quelle puissance il tournera. Selon RTE : doublons (un même projet sur
plusieurs points du réseau), concurrence de développeurs pour un même client, montée en charge d'une dizaine d'années,
puissance appelée inférieure à la puissance de raccordement (marges de sécurité) ; la règle « premier arrivé, premier
servi » rend la réservation peu engageante.

### Preuve décisive

Les trois publications de RTE, téléchargées et lues par script (empreintes SHA-256 consignées dans le jeu) ; la
répartition par statut mesurée sur la figure 2.3 et retrouvée contre les totaux du texte (somme des centres de données
13,9 GW pour « 14 GW » écrits ; hydrogène 9,4 pour 9,5 ; industrie 6,5 pour 6,5 : l'attribution des couleurs est
vérifiée par trois totaux indépendants) ; les trajectoires de la figure 2.10 mesurées sur les tracés et retrouvées contre
les étiquettes (15 et 32 TWh, 10 et 21 TWh).

### Pouvoir discriminant

- **Lectures rivales réellement soutenues.** (a) La puissance réservée annonce une consommation du même ordre, bientôt :
  lecture des conversions en réacteurs ou en foyers dans la presse grand public, et des annonces d'investissement (Choose
  France 2026 : 93 milliards d'euros de promesses, selon RTE). (b) La réservation est une option, dont une part se réalise
  lentement et une autre pas du tout : lecture de RTE, gestionnaire du réseau, qui attribue ces réservations et prépare la
  réforme de leur file d'attente (« saturation administrative », passage au « premier prêt, premier servi ») — une
  lecture située, puisqu'elle sert aussi l'argument de la réforme.
- **Témoin.** Ce qui ne dépend pas des trajectoires de RTE : la consommation **mesurée** (réseau de transport, RTE ;
  réseau de distribution, Enedis, cité par RTE) et le **calendrier déclaré par les porteurs** dans les réservations
  elles-mêmes (figure 2.3). Une seule variable change entre les deux panneaux : l'objet mesuré (droit d'accès contre
  énergie consommée), jamais l'unité convertie.
- **Que révèle le graphe qu'une série isolée ne montre pas ?** Que la croissance des réservations et celle de la
  consommation mesurée ne suivent pas le même rythme, et que la majorité des réservations elles-mêmes sont datées après
  2030.
- **Quelles explications départage-t-il ?** Il tranche une question de **calendrier** : la lecture (a) au sens « bientôt »
  est démentie par les porteurs eux-mêmes (plus de la moitié des gigawatts visent 2030 ou après) ; l'existence
  d'abandons dément la lecture « une réservation est acquise ». Il **ne tranche pas** le volume final : la part qui se
  réalisera reste une hypothèse (30 % et 60 % dans les deux trajectoires de RTE). La page le dit.
- **Résiste-t-il à un autre périmètre ?** Le décalage tient sur les deux réseaux mesurés (transport : 0,8 puis près de
  1 TWh ; distribution : 3 TWh en 2024) et sur l'estimation la plus large de RTE (4 à 5 TWh pour l'ensemble des sites
  dédiés en 2024, 5 à 10 avec les centres internes).
- **Levier ou risque éclairé.** Ce qui engagerait la collectivité n'est pas la réservation (suspendue ou abandonnée sans
  ouvrage construit) mais les ouvrages de réseau construits pour l'accueillir et les engagements de long terme qui les
  financent : la page ne les mesure pas, et le dit.

### Limite

Toutes les valeurs viennent d'un seul producteur, RTE, partie prenante (il attribue les réservations et en réforme la
file) ; la consommation du réseau de distribution est reprise de RTE, non lue chez Enedis. Les valeurs de la page web de
RTE ne sont pas toutes celles du Bilan prévisionnel qu'elle cite (15 à 20 TWh en 2030 et 23 à 28 TWh en 2035 « dans une
trajectoire de décarbonation rapide », contre 15 et 32 TWh dans le PDF ; « environ 10 TWh » de consommation, contre 4 à
5 TWh pour les sites dédiés) : la page suit la publication, dit l'écart et ne l'interprète pas. La répartition par statut
est mesurée sur une figure (précision de l'ordre de 0,1 GW) et datée du 1er novembre 2025, quand le total de 14 GW est
daté de fin novembre. Les trajectoires sont des hypothèses, non des prévisions de marché. Ni l'eau, ni le foncier, ni les
coûts de réseau ne sont mesurés.

### Valeur finale

Deux échelles que le lecteur peut reprendre sans les confondre : ce qui est réservé (GW, droit d'accès) et ce qui est
consommé ou projeté (TWh, énergie) ; et une question qui reste ouverte : quels ouvrages seront construits pour ces
réservations, et qui en portera le coût si elles ne se réalisent pas.

### Singularité

Cette page existe parce qu'elle met côte à côte, datées, les réservations, leur calendrier par statut (mesuré sur la
figure de RTE, absent de son texte), les abandons et la consommation mesurée, ce que le lecteur ne trouve réuni ni sur la
page de RTE (lue : 18 GW et la projection, sans calendrier ni abandons), ni dans le Bilan électrique (lu : 14 GW, sans
consommation projetée), ni dans la presse (lue partiellement : conversion des GW en réacteurs ou en foyers).

### Raccords

- Définition de l'anthropie — écartée du corps (page de faits) ; un encadré séparé renvoie à la notion de dette
  technologique, présentée comme lecture de l'auteur.
- Livre — retenu : *ANTHROPIE — Ordre ici. Dette ailleurs* (appel en fin de page, `ressource.livres`).
- Working paper — AWP-06 (infrastructures numériques et dette technologique) cité dans l'encadré séparé ; non retenu
  dans le corps.
- Pages voisines — `/dette-technologique/` (phrase de renvoi ajoutée dans la notion, section « Le cas des data
  centers ») ; `/decouplage-energie-croissance/` écartée : la question n'est pas celle de l'intensité énergétique.

## Fiche D0

Résultat visé : la page citée quand le chiffre des réservations circule (presse, élus des territoires d'accueil, débat
sur la réforme du raccordement). Diagnostics : vues, citations. État initial : page nouvelle ; relevé au J+60.

## Étapes de la méthode

- Plan d'outils : fait le 27/10/2026 (`outils_du_produit.py ressource`).
- Protocole du type `quantitatif` : fait (trois publications lues, dates et périmètres séparés, valeurs lues par script
  dans la phrase qui les porte, une seule occurrence exigée par phrase ; répartition mesurée sur la figure 2.3 et
  contrôlée par trois totaux écrits ; trajectoires de 2030 mesurées sur la figure 2.10 et contrôlées par ses étiquettes ;
  écart entre la page web de RTE et le Bilan prévisionnel consigné et gardé).
- Scénarios d'architecture : tranché par l'arbitrage PRO-20261026-033434 (S2, deux panneaux, aucun rapport GW / TWh).
- Panel avant : non fait (forme des pages G1 à G3, déjà soumise au test de compréhension simulé du 26/10/2026).
- Contre-expertise de phase A : faite (PRO-20261026-033434, G4 accepté avec modification ; condition « chiffres lus
  dans une publication de RTE, datés » remplie le 27/10/2026).
- Gardes vues mordre : faites — 14 gardes, 13 mutations (`triple`, `devant`, `moitie`, `abandon`, `totaux`,
  `trace2035`, `trace2030`, `conso`, `ordre`, `ecart`, `raccorde`, `texte`, `doublon`), chacune vue mordre. Défaut
  trouvé en écrivant : la première expression de `util_2030` lisait le taux d'un autre secteur (60 % au lieu de 20 %),
  sans erreur ; corrigé (phrase ancrée) et rendu impossible (une seule occurrence par phrase, mutation `doublon`).
- Écriture conditionnelle : rien n'est réécrit à sortie identique (vérifié : second passage « rien écrit ») ; empreinte
  des seuls PDF (le HTML de la page web ferait avancer `releve_le` sans donnée nouvelle).
- Figures téléphone : faites (versions `-m`, parité contrôlée ; deux-points typographiques par langue).
- Relecture de langue : faite (LanguageTool FR et EN sur le texte servi, 18 signalements, tous faux positifs :
  extraction, orthographe britannique, titres français cités).
- Relecture phrase à phrase FR et EN : faite le 27/10/2026 ; corrections : accords portés par un jeton (« 1,0 GW
  étaient », « 0,4 GW ont été raccordés ») supprimés par la construction de la phrase ; lecture « conversions en
  réacteurs » attribuée à la presse sans source, reformulée en ce que suppose toute conversion ; « abattements » non
  défini ; « l'écart n'est pas expliqué par RTE » ramené à ce qui est vérifié (la page web ne l'explique pas).
- Recette 320-1600 : faite (`recette.py`, 12/12 FR et EN).
- Instantané de relecture : fait (FR, EN).
- Contrôles : `check-all --ci` à 0, build 0, `audit-liens-build` 0, `check-rendu-ressources` conforme,
  `check-dates-build` concordant.
- Gate éditorial — auto-évaluation, non indépendante : exactitude *tenu* (valeurs lues par script, témoins de figure,
  écart entre publications dit) ; clarté *tenu* (une unité de texte « un gigawatt réservé n'est pas un gigawatt
  consommé » au contact des premiers chiffres) ; accroche *tenu* ; progression *tenu* (réservé / consommé → calendrier →
  projections → engagement → limites) ; originalité *partiel* (les chiffres sont ceux de RTE ; l'apport est le calendrier
  mesuré sur la figure, les abandons et l'écart entre publications) ; valeur finale *tenu*.
- Panel après, test de compréhension : non fait (à décider par l'auteur, comme pour G1 à G3).
- Contre-expertise de la page : paquet écrit le 27/10/2026 (`D:\PRO_PROMOTION\GRAPHES_NOTIONS_2026-10-26\PAQUET_PAGE_DATA_CENTERS.md`, P1 à P12) ; deux erreurs trouvées en l'écrivant et déclarées non corrigées (E1 : « RTE donne trois raisons », synthèse de deux documents ; E2 : panneau du bas mêlant mesure du réseau de transport et grandeurs de tous les sites dédiés) ; une troisième corrigée (E3 : colonnes de la figure 2.3 associées aux statuts par l'ordre seul, désormais contrôlées par leurs libellés, contrôle vu mordre). Réponse : à archiver avant lecture, puis arbitrer.
- Renvoi depuis `/dette-technologique/` (FR, EN) : fait, sans chiffre (la notion ne porte aucun qualificatif que le
  générateur ne garde pas).
- Accord de l'auteur : demande « lance le graphe G4 » (27/10/2026) ; publication sur sa demande.

### Révisions du 04/11/2026 (après publication)

- Chaîne réservation → consommation en une phrase (section `#calendrier`).
- SDES (publication du 02/07/2026, lue à la source) : quatrième source du générateur, garde « même ordre de grandeur »
  vue mordre (`--mutation=sdes`) ; réponse « d'où viennent ces chiffres » et limite « un seul producteur » rendues exactes.
- Figure : périmètre écrit sur chaque ligne de consommation ; légende rattachée à « En novembre 2025 » (le bleu foncé
  faisait lire les totaux 2024 et 2026 comme « avant 2030 ») ; « déjà raccordés » en contour (le gris désignait aussi
  « suspendu ») ; légende de la fourchette ; nombre et unité insécables ; séparateurs jamais seuls en bord de ligne.
  Skill `controle-figures` : deux contrôleurs indépendants, second passage sur l'état final.
