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
mise en service à partir de 2030, et près d'un gigawatt de réservations a été abandonné depuis 2023. RTE ne déduit pas sa projection des réservations : ses deux trajectoires donnent 10 à 15 TWh en 2030, valeurs lues sur une figure (R2-E7) ; sa page web illustre pourtant une puissance demandée par la consommation d'une ville (R1-3).

### Mécanisme explicatif

Une réservation (proposition technique et financière signée) garantit une capacité d'accès au réseau ; elle ne
dit ni si le site sera construit, ni quand, ni à quelle puissance il tournera. Selon RTE : doublons (un même projet sur plusieurs points du réseau, que RTE observe « parfois » sur l'ensemble des demandes, pas seulement celles des data centers : R1-4), concurrence de développeurs pour un même client, montée en charge d'une dizaine d'années,
puissance appelée inférieure à la puissance de raccordement (marges de sécurité) ; la règle « premier arrivé, premier
servi » rend la réservation peu engageante « pour les porteurs de projet » (R1-7) ; elle n'est pas sans effet pour la collectivité (raccordements retardés, saturation contractuelle : R1, conclusion 3). Relecture des sources du 12/11/2026 : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\SOURCES\data-centers-puissance-reservee_SYNTHESE.md`.

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
- Contre-expertise de la page : faite le 04/11/2026 sur la page construite (pièce `Data_Center.txt`, SHA-256 `9780418f…`, arbitrage `D:\PRO\06_PROMOTION\REVISION_DATA_CENTERS_2026-11-04\ARBITRAGE_DATA_CENTER_2026-11-04.md`), avant publication. Le paquet du 27/10 (`GRAPHES_NOTIONS_2026-10-26\PAQUET_PAGE_DATA_CENTERS.md`, P1 à P12) n'a pas été déposé : caduc. Ses trois erreurs : E3 corrigée le 27/10 (colonnes de la figure 2.3 contrôlées par leurs libellés) ; E2 corrigée le 04/11 (`c9fc429`, périmètre écrit sur chaque ligne de consommation) ; E1 corrigée le 10/11/2026 (« RTE donne trois raisons » → « Trois mécanismes, relevés dans le Bilan prévisionnel et sur la page web de RTE », FR et EN, instantanés refaits). Reportés par l'arbitrage, à la prochaine révision : troisième lecture d'une réservation, cohortes, allocation des capacités ; restés sans réponse du paquet : dates de mise en service déclarées (P5), qui paie le raccordement (P9).
- Renvoi depuis `/dette-technologique/` (FR, EN) : fait, sans chiffre (la notion ne porte aucun qualificatif que le
  générateur ne garde pas).
- Accord de l'auteur : demande « lance le graphe G4 » (27/10/2026) ; publication sur sa demande.

### Révisions du 04/11/2026 (après publication)

- Chaîne réservation → consommation en une phrase (section `#calendrier`).
- SDES (publication du 02/07/2026, lue à la source) : quatrième source du générateur, garde « même ordre de grandeur »
  vue mordre (`--mutation=sdes`) ; réponse « d'où viennent ces chiffres » et limite « un seul producteur » rendues exactes.
- Figure : périmètre écrit sur chaque ligne de consommation ; légende rattachée à « En novembre 2025 » (le bleu foncé
  faisait lire les totaux 2024 et 2026 comme « avant 2030 ») ; « déjà raccordés » distinct du gris de « suspendu » (contour
  d'abord, puis plein anthracite : totaux hachurés, chaque marque un seul sens) ; légende de la fourchette ; nombre et unité insécables ; séparateurs jamais seuls en bord de ligne.
  Skill `controle-figures` : deux contrôleurs indépendants, second passage sur l'état final.
- Troisième passage des contrôleurs (04/11) : 14 GW tracés à 13,9 (répartition mesurée) → somme écrite au pied par jeton
  (`actif_dc`) ; segment « suspendu » de 3 px → légende « trait gris en bout de barre » ; « environ 0,9 GW », « about
  0.9 GW », « 1 June 2026 » soudés, « 1ᵉʳ juin » ; contour des fourchettes aligné sur le plein (1 px) ; texte alternatif :
  sites raccordés, suspendu, abandonné. Écartés : teinte non grise pour « déjà raccordés » (ligne à libellé propre) ; date
  de la figure 2.3 (lue dans le Bilan prévisionnel par le générateur ; « fin novembre » est celle du Bilan électrique).
- Quatrième passage (04/11) : légende des hachures sortie du bloc « En novembre 2025 » ; « déjà raccordés » daté (« en juin
  2026 », jeton `mois_web`, page RTE du 1ᵉʳ juin ; distinct des 0,4 GW raccordés depuis 2023) dans la figure, son desc et
  le texte alternatif ; « avant 2030 » soudé ; texte alternatif : « trajectoires de décarbonation lente et rapide de RTE »
  (le Bilan prévisionnel, p. 11, étudie aussi une trajectoire de stagnation, en test de sensibilité : « les deux
  trajectoires » était inexact). Écartés : légende de l'orange foncé (libellés « mesurée ») ; largeur minimale du segment
  « suspendu » au téléphone (elle fausserait la valeur ; la légende le désigne).

### Reprise du lot « guides » (12/11/2026)

Méthode `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\METHODE_REPRISE_RESSOURCE.md` ; dossier `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\` (rapport
`RAPPORTS\data-centers-puissance-reservee.md`, état `LOT.md`).

- Relecture des sources : faite le 12/11/2026, deux relecteurs indépendants et les sondes de la session
  (`SOURCES\data-centers-puissance-reservee_R1.md`, `_R2.md`, `_SYNTHESE.md`, `SONDES_SESSION.md`) ; écarts de la version
  en ligne corrigés : 18 GW rapportés au réseau de transport de RTE (non à tout le réseau français) ; recensement du SDES
  présenté comme un recoupement (il tire en priorité ses données de consommation des bases d'Enedis et de RTE), non comme
  un contrôle indépendant ; réservations multiples observées par RTE sur l'ensemble des demandes ; deux emplois de 20 %
  distingués (observation, hypothèse) ; condition et effets d'une suspension, selon RTE.
- Interventions : `specs\data-centers-puissance-reservee.py`, 121 remplacements (FR et EN), dont trois explications (DC-3,
  DC-4, DC-16, FR et EN), tranchées en faveur de la version proposée par le contradicteur externe ; témoin : la spécification
  appliquée à la page d'origine (`c2b25c2`) redonne cette page, en-tête de publication et organe de forme (`figure-lecture`)
  à part.
- Juge interne à l'aveugle : deux tours sur le lot, version proposée préférée, sans P0 ; contradicteur externe
  `PRO-20261112-140721` (réponse archivée avant lecture, SHA-256 `A71FAC4D…`) : version proposée retenue aux 22 passages ; P0
  de la page en ligne (18 GW lus sur tout le réseau ; SDES « contrôle indépendant ») corrigés par elle ; repris sur sa
  décision : attribution à RTE rendue visible (« selon RTE »), réserve « répartition et abandons mesurés sur une figure »
  (les 0,9 GW abandonnés sont mesurés sur la figure 2.3 : relecture R1, l. 44), lecture de RTE rattachée à ses textes et
  proportion inconnue, réservation garantie « dans les conditions de son contrat et des règles de raccordement » ;
  arbitrage `ARBITRATIONS\PRO-20261112-140721_arbitrage.md`.
- Premier écran : deux lecteurs (élu local, grand public) sur le chapô proposé, témoin trompeur pris
  (`P\premier_ecran.md`).
- Relecture de langue phrase à phrase du texte servi, FR (135 phrases : 2 fautes, 24 maladresses) et EN (132 : 2 erreurs,
  34 maladresses) : corrigées, préférences retenues quand elles éclairent (44 corrections FR, 56 EN, pastille et contrôle compris). Points de fond
  tranchés au passage : les 800 MW attribués à la page de RTE du 1er juin 2026, qui ne les date pas (relecture des
  sources, R1-8), et cumulés, ce qui les distingue des 0,4 GW raccordés depuis 2023 ; les 0,9 GW abandonnés bornés au
  1er novembre 2025 ; « recoupement » pour le rôle du SDES partout ; la réserve du résumé couvre
  la répartition et les abandons ; on « utilise » une puissance, on consomme une énergie. Écartés avec motif : « 1er »
  (convention du site non unifiée : décision transversale), titres en italique dans le corps (préférence), texte de
  l'offre de livre (gabarit, formule de l'auteur), texte inscrit dans l'image (juxtaposition admise), libellés de la
  colonne « nature » du CSV ; ponctuation de la citation quand le titre finit par « ? » : gabarit commun, traitée à part.
  Relecture de contrôle des phrases changées (`JUGE\RELECTURE_LANGUE_DATA_CENTERS_CONTROLE.md`) : aucune faute ; un changement de sens (les 800 MW datés de juin 2026, ce que la relecture des sources interdisait) et quatre maladresses, corrigés.
- Fiche de figure (« ce que montre la figure ») : « consommaient » devient « ont consommé », dans le générateur et dans
  `data/figures_data_centers.json` ; figure inchangée. Pastille : « Données mises à jour le », libellé des pages modèles
  (date du relevé ; au premier écran, « Données du » se lisait comme la date des données). Reste dans la figure et son
  texte alternatif l'étiquette « déjà raccordés au réseau de RTE en juin 2026 » (R1-8, renvoyé) : elle se corrige au
  prochain passage du générateur, qui relit les publications de RTE en ligne, avec la mise à jour des données (R2-E1).
- Contrôles : `check-all --ci` 0 ; build et `typo_build` 0 défaut ; rendu 0 ; liens 0 critique ; dates 83/83, 0 bloc sans
  période ; couverture : 15 signaux, aucun nouveau ; lettre : chaque écart rattaché à son intervention, sauf la date de mise
  à jour (en-tête).
- Envois : la page est citée par deux courriels de la campagne ANTHROPY-EN (LOT3, parti le 12/11 ; LOT6, 17-18/11) ; publication
  décidée par l'auteur le 12/11/2026, un écart avec un envoi non parti se corrigeant dans le courriel ; les deux restent
  exacts face à la page corrigée.
- Instantané de relecture : fait le 12/11/2026 (139 phrases FR, 135 EN) ; `refonte` porté au 12/11/2026 ; journal : entrée du 12/11/2026 ;
  `data/dates_affichage.json` : 05/11/2026 versé à l'historique.
- Mise en ligne : poussée sur mandat de l'auteur, le 12/11/2026 (commit 0095bb4) ; déploiement `hugo.yml`
  n° 43241566593 réussi (build, relecture, deploy, contrôle de fumée de la production).
- Attestation de la version servie : faite le 12/11/2026 vers 15 h 55 (heure de Paris). HTML servi identique au build
  contrôlé, aux empreintes de cache des scripts près (neuf en FR, huit en EN : fins de ligne du poste) ; les quatre SVG
  de la figure servis identiques, octet pour octet, au commit ; « Page mise à jour le 12 novembre 2026 ».
- Laissés à l'auteur : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\A_ARBITRER.md`.

### Reprise du style (13/11/2026)

- Consigne de l'auteur (13/11/2026) : une mise en page « ultra lisible », au niveau de la page Parcoursup (règle 17
  du `CLAUDE.md` du site), adaptée au sujet. Étude, choix et mesures :
  `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\ETUDE_STYLE.md`. Organes existants seulement
  (`_ressource-relief.scss`, `reperes-page.html`) ; les phrases ne changent pas, elles prennent une forme.
- Organes : trois repères sous le chapô, tous en puissance réservée (près de 18 GW en mai 2026 ; 7,6 GW sur 13,9 GW
  au 1er novembre 2025 visaient 2030 ou après ; environ 0,9 GW abandonnés de 2023 à cette date, contre 0,4 GW raccordés sur la même période).
  Aucun repère en TWh : côte à côte, GW et TWh invitaient la comparaison que la page interdit. Les trois mécanismes en
  cartes numérotées (le numéro remplace « D'abord, Ensuite, Enfin » ; le gras de la première carte porte son périmètre,
  « pas seulement celles des data centers ») ; deux paragraphes coupés. Périodes des repères écrites en clair, comme
  dans le chapô : jeu transcrit, la période fait partie du motif de lecture du générateur (écart déclaré à « aucun
  nombre saisi » ; aucune valeur saisie).
- Inchangés : titre, adresse, ancres, chapô, figures, nombres, réserves, questions fréquentes, sources, « Réutiliser ».
  Aucune modification de fond : `lastmod`, journal et `data/dates_affichage.json` inchangés ; `refonte` reste au
  12/11/2026 (instantané du 13/11, postérieur).
- Contrôles : `check-all --ci` 19/19 à 0 ; build CI et `typo_build` 0 défaut ; liens 0 critique ; rendu 0 ; dates 83/83,
  0 bloc sans période ; 0 débordement sur onze largeurs de 320 à 1 440 px, avec et sans JavaScript ; aucun texte des
  blocs sous 12 px ; repères absents sous 600 px ; lecture à côté de la figure dans la limite. Lettre : texte servi avant
  et après, phrase à phrase ; seules changent les phrases mises en forme ; nombres inchangés. Langue et fidélité : la
  session, puis un relecteur indépendant (aucun P0 ; P1 traités). Premier écran : deux tours de lecteurs neufs (FR, EN) et un témoin trompeur vu mordre
  (`LOTS\guides\P\premier_ecran_style.md`) ; constats sur le chapô, inchangé : `LOTS\guides\A_ARBITRER.md`.
- Instantané de relecture refait le 13/11/2026.
- Mise en ligne : poussée sur demande de l'auteur le 13/11/2026 (commits `cf3ad02` à `17d3598`) ; déploiement `hugo.yml`
  n° 43351148379 réussi (build, mise en ligne, relecture). Attestation de la version servie : faite le 13/11/2026 vers 03 h 20 (heure de
  Paris) ; HTML servi identique au build contrôlé, aux empreintes de cache des feuilles et scripts près.

### Arbitrage externe et relectures (13/11/2026)

- Pièce remise par l'auteur, archivée avant lecture et arbitrée par écrit : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\ARBITRAGE_EXTERNE_2026-11-13.md`.
- Fond : les 800 MW des data centers déjà raccordés (huit sites) ne sont plus datés de juin 2026, mois de mise à jour de la
  page de RTE, qui ne dit pas quand ils ont été mesurés (figure régénérée par `scripts/update_data_centers.py`, FR et EN,
  bureau et téléphone ; texte alternatif). Chapô : « En France » ; la part qui vise 2030 rapportée aux 14 GW réservés en
  novembre 2025, une seule base de date ; « sur sites dédiés » pour la consommation. « La figure ci-dessus précise un
  calendrier, pas un volume. » `lastmod` au 13/11/2026, journal, historique des dates.
- Non repris, faute de source lue : 18,2 GW à la mi-juin 2026 et 12,4 GW (absents du jeu et des sources du générateur),
  770 MW raccordés fin 2025, programme de 300 M€ ; lot P3 (DC-16).
- Langue : relecteur indépendant, aucun P0 ni P1 ; texte alternatif « selon la page de RTE mise à jour le … » (le
  possessif pouvait viser le réseau). « Against » gardé en anglais : usage britannique des comparaisons, employé sur toute
  la page.
- Figure : deux contrôleurs indépendants (géométrie et données ; lecture du rendu), aucun défaut sur les quatre versions ;
  page de RTE relue, aucune date n'y est attachée aux 800 MW. Premier écran, troisième tour : aucune conclusion interdite ;
  le lecteur français rattache encore « plus de la moitié » aux 18 GW en le racontant, et le signale lui-même.
- Contrôles : `check-all --ci` à 0 ; build CI et typographie 0 défaut ; liens 0 critique ; rendu 0 ; dates 83/83 ;
  0 débordement sur onze largeurs de 320 à 1 440 px, avec et sans JavaScript (la mesure vérifie désormais le statut
  HTTP de chaque page) ; lettre : texte servi avant et après, phrase à phrase, seules changent les phrases décidées.
- Instantanés de relecture refaits le 13/11/2026.
- Mise en ligne : poussée sur demande de l'auteur le 13/11/2026 (commits `98cc594` à `56ec209`) ; déploiement
  `hugo.yml` n° 43393816179 réussi (build, mise en ligne, contrôle de fumée, relecture). Attestation de la version
  servie : faite le 13/11/2026 à 9 h 33 (heure de Paris) ; HTML servi identique au build contrôlé, aux empreintes de
  cache des feuilles et scripts près ; fichiers statiques servis (figures, cartes de partage) identiques au commit.
