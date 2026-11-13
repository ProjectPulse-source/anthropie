# Fiche de conception — L'économie mondiale se découple-t-elle de l'énergie ?

<!-- Page de données née de l'arbitrage PRO-20261026-033434 (G2 « transformé » : page sur le découplage et ses limites,
non sur le rebond ; décomposition arithmétique ; frontière de mesure écrite sur la figure ; phrase interdite : que le
rebond explique la hausse). Fiche écrite AVANT le texte, après lecture des séries de l'EIA, du témoin de l'Energy
Institute et de Brockway et al. (2021). -->

Page : `/decouplage-energie-croissance/` (FR) · `/en/decoupling-energy-growth/` (EN) · ouverte le 2026-10-26

## Forme

`quantitatif` : séries de l'EIA (fichier groupé international, sans clé), lues par `scripts/update_decouplage.py` ;
modèle complet des pages de données. Critères : définitions (énergie primaire selon la convention de l'EIA, mesurée :
électricité hydraulique, éolienne et solaire comptée à son contenu électrique, 3 412 Btu/kWh ; nucléaire à la chaleur
du réacteur, environ 10 400 Btu/kWh ; PIB en parité de pouvoir d'achat à prix constants, vérifié contre la Banque
mondiale) ; millésimes (énergie jusqu'en 2024, PIB et population jusqu'en 2025 : la décomposition s'arrête à la
dernière année commune) ; une décomposition comptable n'est pas une attribution causale (règle 15 du site) ; la
comparaison de fenêtres change ses deux bornes ; aucune lecture anthropique dans les constats.

## Fiche de conception

### Question centrale

Une économie mondiale qui consomme de moins en moins d'énergie par unité de richesse produite consomme-t-elle moins
d'énergie au total, et sinon, qu'est-ce qui l'emporte : la démographie, la hausse du revenu par habitant ?

### Enjeu

Le recul de l'intensité énergétique est souvent présenté comme le signe d'un découplage en cours ; les scénarios de
transition supposent une baisse de la consommation totale. Confondre découplage relatif et découplage absolu fait lire
un progrès réel comme la solution du problème.

### Croyance initiale

Deux croyances rivales circulent : « l'efficacité énergétique fait baisser la consommation » (lecture des politiques
d'efficacité ; l'AIE estime que l'efficacité a évité 24 % de la consommation de ses pays membres en 2021) ; et « si la
consommation monte, c'est d'abord parce que la population mondiale augmente » (lecture démographique courante).

### Découverte principale

De 2000 à 2024, l'intensité énergétique mondiale a baissé de 28,5 % (PIB en parité de pouvoir d'achat ; 20,8 % aux taux de marché : R1-4) et la consommation d'énergie a augmenté de 58 % :
découplage relatif, pas absolu. Dans la décomposition, la hausse du PIB par habitant pèse 1,8 fois plus que
celle de la population (+263 EJ contre +144 EJ, PIB en parité de pouvoir d'achat), et la baisse de l'intensité en retire 172 : elle compense environ
deux cinquièmes de la poussée, pas davantage. Dans l'Union européenne, même producteur, même définition, la
consommation a baissé de 18 % pendant que le PIB augmentait de 43 % : un découplage absolu, sur son territoire. Eurostat, autre producteur et autre convention, donne −14,5 % de 2000 à 2024 (R2-1, sonde de la session).

### Mécanisme explicatif

Identité comptable E = population × (PIB / population) × (E / PIB), décomposée par la méthode de l'indice de Divisia
logarithmique moyen (somme exacte, sans résidu). Elle dit combien chaque terme a pesé, pas pourquoi : la baisse de
l'intensité mêle progrès d'efficacité, changement de la composition de l'économie et effet de la convention de comptage, constante, sur un bouquet qui change (part de l'électricité comptée à son contenu énergétique : R1-6, DE-8 à arbitrer) ; elle ne permet pas d'estimer un effet rebond (phrase interdite par l'arbitrage). Brockway et al. (2021) ne disent pas ce que la page leur prêtait (R2-3, DE-1). Relecture des sources du 12/11/2026 : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\SOURCES\decouplage-energie-croissance_SYNTHESE.md`.

### Preuve décisive

Séries de l'EIA (énergie, PIB PPA constant, population), monde et UE, lues par script ; somme exacte de la
décomposition contrôlée ; témoin d'un autre producteur, même convention de contenu physique : offre totale d'énergie de
l'Energy Institute (jeu `owid_energy` d'Our World in Data, total mondial 2024 contrôlé contre celui de l'édition 2025),
et PIB de la Banque mondiale à prix constants (`NY.GDP.MKTP.PP.KD`), recalcul complet de la décomposition ; variante du
PIB aux taux de change de marché (`NY.GDP.MKTP.KD`) ; baisse européenne depuis 2005 chez Eurostat (`nrg_ind_eff`).
Jusqu'à la contre-expertise du 26/10/2026, le témoin était la série en substitution d'Our World in Data (mêlant EI et
EIA), présentée à tort comme celle de l'Energy Institute.

### Pouvoir discriminant

- **Lectures rivales réellement soutenues.** (a) La hausse de la consommation mondiale tient d'abord à la démographie ;
  (b) elle tient d'abord à la hausse du revenu par habitant ; (c) l'efficacité fait baisser la consommation (lecture
  des politiques d'efficacité, et des scénarios qui projettent un découplage absolu, que Brockway et al. discutent).
- **Ce que le graphe tranche.** Comptablement, (b) l'emporte sur (a) dans toutes les fenêtres testées (1990, 2000,
  2010, 2015 et 2019 jusqu'en 2024) ; (c) est vraie pour l'intensité et fausse pour le total mondial : l'effet
  d'intensité est négatif mais plus petit que les deux autres réunis. Le témoin à une seule variable est l'UE : même
  producteur, même définition, autre population ; le total y baisse. Ce que le graphe ne tranche pas : pourquoi
  l'intensité baisse (efficacité, composition de l'économie, convention), ni si la baisse européenne tient à
  l'efficacité ou au déplacement de productions énergivores hors d'Europe (G2b, suspendu faute d'empreinte
  énergétique) ; la page le dit.
- **Ce que la série isolée ne montre pas.** Une courbe d'intensité qui baisse et une courbe de consommation qui monte
  se lisent séparément partout ; leur réunion dans une décomposition exacte, en exajoules, dit de combien chaque terme
  a pesé.
- **Robustesse, montrée par des variantes calculées.** Recalcul sur l'Energy Institute et la Banque mondiale (autre
  producteur, même convention) ; PIB aux taux de change de marché (l'ordre PIB par habitant > population tient dans les
  cinq fenêtres ; la baisse de l'intensité tombe à −20,8 % et passe sous l'effet de la population en partant de 1990 ou
  2000) ; trois producteurs pour l'UE depuis 2005 ; fenêtres 1990, 2000, 2010, 2015 et 2019.
- **Niveau atteint.** Descriptif et comptable ; discriminant entre (a) et (b) au sens arithmétique seulement ; pas
  décisionnel.
- **Levier ou risque éclairé.** Un objectif de baisse de la consommation totale ne s'atteint pas par la seule baisse
  de l'intensité si le PIB par habitant croît plus vite qu'elle ne baisse : c'est un ordre de grandeur, non une
  prescription.

### Limite

La décomposition est comptable : elle n'attribue aucune cause. L'intensité énergétique n'est pas l'efficacité d'un
usage. L'EIA et l'Energy Institute comptent l'électricité hydraulique et éolienne à son contenu électrique (le solaire de
l'EIA à un rapport voisin en 2024, plus élevé avant) : avec la méthode de substitution, la croissance des renouvelables
pèserait plus (variante non calculée, faute d'une série identifiée). La
consommation est territoriale : l'énergie contenue dans les importations n'est pas comptée (limite décisive pour
l'UE). Le PIB en parité de pouvoir d'achat dépend d'une année de base et de révisions.

### Valeur finale

Trois chiffres réutilisables, en exajoules, et leur somme exacte ; la distinction découplage relatif / absolu,
illustrée par deux populations ; la question qui reste ouverte (ce que l'UE consomme hors de ses frontières).

### Singularité

Cette page existe parce qu'elle décompose la hausse de la consommation mondiale d'énergie en population, revenu par
habitant et intensité, en exajoules et sur deux producteurs, ce que le lecteur ne trouve pas réuni dans les
publications lues : l'AIE publie la baisse de l'intensité mondiale (−36 % de 1990 à 2021) et décompose la consommation
de ses seuls pays membres ; Brockway et al. donnent les taux annuels de croissance sans décomposition (recherche du
26/10/2026, non exhaustive).

### Raccords

- Définition de l'anthropie — écartée du corps (page de faits) ; un encadré séparé renvoie à la notion d'effet rebond,
  présentée comme lecture de l'auteur, non testée ici.
- Livre — retenu : *ANTHROPIE — Ordre ici. Dette ailleurs* (le livre que prolonge déjà la notion d'effet rebond,
  `ressource.livres`).
- Working paper — retenu dans l'encadré séparé : [AWP-04](/awp/awp-04/) (*Transition énergétique ou transfert
  entropique ?*), où l'auteur replace l'effet rebond parmi les mécanismes de transfert de la transition ; la fiche disait
  d'abord « aucun AWP », erreur corrigée en lisant la notion d'effet rebond.
- Pages voisines — `/effet-rebond/` (phrase de renvoi ajoutée dans la notion : la page de données montre le découplage
  relatif, elle ne mesure pas le rebond).

## Fiche D0

Résultat visé : la page citée pour la décomposition de la consommation mondiale d'énergie (presse, enseignants de SES et
de physique, débat sur la sobriété). Diagnostics : vues, citations. État initial : page nouvelle ; relevé au J+60.

## Étapes de la méthode

- Plan d'outils : fait le 26/10/2026 (`outils_du_produit.py ressource`) ; serveur MCP `sources` déconnecté : API
  publiques lues directement.
- Protocole du type `quantitatif` : fait (conventions mesurées dans le fichier de l'EIA, PIB constant vérifié contre la
  Banque mondiale, somme exacte, fenêtres).
- Scénarios d'architecture : paradoxe (« l'intensité baisse, la consommation monte ») retenu contre l'anatomie d'un
  chiffre (partir de l'intensité) : le paradoxe pose la question que la décomposition résout.
- Panel avant : remplacé par le test de compréhension simulé, comme pour G1 et G3.
- Contre-expertise de phase A : faite (PRO-20261026-033434, G2 accepté avec modification).
- Source de l'énergie mondiale : l'Energy Institute refuse les scripts (403) ; canal changé (règle constante du
  03/10/2026) : EIA, source primaire, fichier groupé sans clé ; Energy Institute gardé comme témoin par son dépôt chez
  Our World in Data.
- Gardes vues mordre : faites — 12 gardes, 10 mutations (`hausse`, `double`, `apres2019`, `fenetres`, `ue`, `somme`,
  `constant`, `convention`, `temoin`, `bande`), chacune arrêtée par une garde ; `ue` l'est par la garde « 2019 », placée
  avant la sienne. Pic de l'UE pris par `lg.extremum` (contrôle `check-lecture-donnees.py`, qui refusait `max` brut).
- Figures téléphone : faites (parité contrôlée ; elle a mordu sur « 27 » absent de la description). Barres renommées
  « effet de… » après le premier rendu : la carte de partage mettait « −43 % » (effet) et « −28,5 % » (intensité) sous le
  même mot.
- Relecture de langue : faite (LanguageTool FR et EN sur le texte servi ; signalements tranchés : « recalcul » correct,
  extraction, identifiants ; « a billion billion joules » remplacé par « 10¹⁸ joules »).
- Relecture phrase à phrase FR et EN : faite le 26/10/2026 ; corrections : CSV annoncé « au format long » alors qu'il a
  une ligne par zone et par année ; qualificatifs non gardés retirés (« presque nul », « modeste ») ; affiliation de
  Brockway et al. complétée ; « 0,715 » saisi à la main remplacé par un jeton.
- Recette 320-1600 : faite (`recette.py`, 12/12, FR et EN).
- Instantané de relecture : fait (FR, EN).
- Raccord inverse : phrase ajoutée dans « Pour aller plus loin » de `/effet-rebond/` (FR, EN).
- Registre des ressources et fiche D0 : faits (`REGISTRE_RESSOURCES.csv`, `FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`) ; l'oubli
  des fiches D0 et du registre pour G1 et G3 a été réparé dans le même geste.
- Gate éditorial — auto-évaluation, non indépendante : exactitude *tenu* (12 gardes, témoin d'un autre producteur et
  d'une autre convention, fenêtres et année d'arrivée éprouvées) ; clarté *partiel* (vocabulaire technique : exajoule
  défini, parité de pouvoir d'achat et indice de Divisia restent difficiles pour un lecteur pressé) ; accroche *tenu* ;
  progression *tenu* (paradoxe → décomposition → témoin UE → robustesse → recherche → limites) ; originalité *partiel*
  (le découplage relatif est connu ; l'apport est la décomposition chiffrée et son recalcul) ; valeur finale *tenu*.
- Contre-expertise de la page : faite le 26/10/2026, paquet transmis à la main hors navette (`G2-DECOUPLAGE-20261026`),
  réponse archivée verbatim (SHA-256 `c1b8e19b…3362`), arbitrage
  `D:\PRO\.claude\external-audits\ARBITRATIONS\G2-DECOUPLAGE-20261026_arbitrage.md`. Deux erreurs confirmées et
  corrigées : témoin attribué à tort à l'Energy Institute (série en substitution d'Our World in Data ; l'EI est passé au
  contenu physique en 2025, total mondial 2024 publié 592,22 EJ) ; convention éolien et solaire affirmée sans mesure
  (éolien mesuré à 3 412 chaque année ; solaire NON, 3 443 en 2024 et beaucoup plus avant : la page le dit). Ajouts
  calculés et gardés : variante aux taux de change de marché (elle infirme l'« idée-force » proposée, intensité >
  population, rejetée), comparaison EIA, EI, Eurostat pour l'UE depuis 2005 (−22,7, −21,7, −20,3 %). « Revenu par
  habitant » devient « PIB par habitant ». Gardes : 16, mutations : 16 (`eolien`, `solaire`, `provenance`, `marche`,
  `marche_ordre`, `eurostat` ajoutées), chacune vue mordre. Antécédents de méthode (Kaya au GIEC, décompositions de
  l'AIE) : non cités, sources non encore lues (point ouvert). Recette 12/12 après correction d'un défaut commun : la
  section « Révisions » (journal) passait sous l'en-tête collant (`scroll-margin-top` ajouté à `.revisions`, vaut pour
  toutes les pages à journal). Relecture du texte servi et LanguageTool (FR, EN) : faits, signalements tous faux
  positifs ; instantanés refaits.
- Accord de l'auteur : demandé avec le diff du 26/10/2026.

## Test de compréhension simulé (26/10/2026)

Trois lecteurs simulés isolés, texte servi seul (même protocole que G1 et G3).

| Lecteur | Ce qu'il a retenu ; contresens ou gêne (citations) |
|---|---|
| Lectrice rapide, sans formation économique | retenu juste (« on consomme moins par euro produit, mais comme on s'enrichit, la consommation mondiale a quand même grimpé de 58 % ») ; perdue par « exajoules », « indice de Divisia », et par « −43 % » contre « 42 % de cette poussée » (« j'ai cru à une erreur ») |
| Professeur de SES | aucun contresens ; arithmétique vérifiée ; signale l'arrondi de la figure UE (5 + 28 − 50 ≠ −18), la confusion −43 % / 42 %, l'encadré obscur, les fenêtres annoncées sans chiffres, « mesuré » pour une constante de conversion |
| Journaliste énergie | phrase publiable exacte ; demande si la convention de l'EIA vaut sur toute la série, signale que l'année d'arrivée 2024 de l'UE suit la crise de 2022, et l'édition du témoin non dite |

Corrections : résultat et figure en exajoules ajoutés, « part compensée » retirée de la prose ; figure au dixième avec
note d'arrondi ; encadré « Pourquoi… » chiffré (0,715, logarithme, moyenne logarithmique) ; tableau des cinq fenêtres en
repli ; convention contrôlée chaque année de 1990 à 2024 (garde) ; année d'arrivée de l'UE éprouvée (2019 : −6,4 %, plus
de la moitié de la baisse après 2019, garde) ; édition 2025 de l'Energy Institute lue et citée ; exajoule défini. Non
retesté après correction.

### Reprise du lot « guides » (12/11/2026)

Méthode `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\METHODE_REPRISE_RESSOURCE.md` ; dossier `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\` (rapport
`RAPPORTS\decouplage-energie-croissance.md`, état `LOT.md`).

- Relecture des sources : faite le 12/11/2026, deux relecteurs indépendants et les sondes de la session
  (`SOURCES\decouplage-energie-croissance_R1.md`, `_R2.md`, `_SYNTHESE.md`) : valeurs recalculées sur le fichier de l'EIA,
  toutes identiques à la page ; Brockway et al. (2021) relus sur le PDF archivé ; Eurostat `nrg_bal_c` lu (1990-2024).
  Écarts de la version en ligne corrigés : verbes causaux pour une décomposition comptable (« a freiné ») ; 28,5 % sans la
  conversion du PIB ; deux propositions prêtées à Brockway et al. que l'article ne porte pas ; indicateur d'Eurostat dit
  commencer en 2005 ; convention de comptage absente des explications possibles de la baisse européenne ; moyenne
  logarithmique (513 EJ). Reste à relire (R1-2) : la définition de l'EIA (soutes internationales, chaleur renouvelable),
  avant de dire « sur le territoire » sans réserve.
- Interventions : `specs\decouplage-energie-croissance.py`, 164 remplacements (FR et EN), dont cinq explications (DE-2,
  DE-8, DE-11, DE-23, DE-24) tranchées par le contradicteur externe en faveur de la version proposée ; témoin : la
  spécification appliquée à la page d'origine (`c2b25c2`) redonne cette page, en-tête de publication, sujet du jeu de données
  et organes de forme (`figure-lecture`, questions sur deux colonnes) à part.
- Contradicteur externe `PRO-20261112-140721` (réponse archivée avant lecture, SHA-256 `A71FAC4D…`) : version proposée
  retenue sur 19 passages sur 20, le passage 12 laissé à la version en ligne ; décisions 14 à 19 appliquées : « une intensité
  agrégée ne mesure pas l'efficacité » rendu comme constat de la page, la citation de Brockway et al. restant fidèle ; titre
  et note de la figure comptables, sans contrefactuel ; « selon la convention de mesure et l'évolution du mix » ; texte
  réutilisable avec sa source et sa mesure. Décision 19 : relevé du 12/11/2026, fichier groupé INTL.zip dont les séries
  portent une mise à jour au plus tard le 21/08/2026 ; la mise à jour du 9 au 11/11 qu'il signalait (non vérifiée) n'y
  apparaît pas, la vérification par un autre canal revient à une session de données. Juge interne (P1) : les trois
  producteurs comparés sur 2000-2024 avec les bilans complets d'Eurostat (garde « baisse chez les trois, un peu moins forte
  chez Eurostat », vue mordre).
- Générateur (`scripts/update_decouplage.py`) : Eurostat lu dans les bilans complets (`nrg_bal_c`, même indicateur que
  `nrg_ind_eff` à 5 ktep près sur 2005-2024) ; chaque rangée de la figure porte la variation propre de son facteur (un effet
  se lisait comme cette variation : −42,6 % pour une intensité en baisse de 28,5 %) ; note : ce que mêle l'effet de
  l'intensité (efficacité, structure de l'économie, conventions), ni causes ni contrefactuel, borne d'arrondi exacte
  (0,1 point), « biens importés » ; description intégrée avec la conversion du PIB, le territoire et les variations propres ;
  rapport et logarithme à quatre et trois décimales (513 × 0,336 redonne 172). Cartes (`scripts/og_decouplage.py`) :
  conversion du PIB dans la ligne de source, « mondiale » dans le titre français, variation propre de chaque facteur, dessin
  décalé hors de la gouttière de l'accroche, total au bleu de la charte ; fabrique commune (`og_dossier_dette.py`) : « % »
  soudé à son nombre (78 cartes simulées par le contrôleur : aucune autre coupure changée).
- Figure : `check-figures` 0 défaut ; contrôleur de géométrie et de données (nombres recalculés, Banque mondiale en témoin)
  et contrôleur de lecture, puis trois passages sur l'état corrigé (second : cinq défauts nouveaux, cosmétiques ; troisième :
  deux gênants et quatre cosmétiques ; corrigés) ; quatrième passage : un défaut nouveau, cosmétique (la parenthèse d'un libellé allongé au contact de l'axe sur la carte
  anglaise), corrigé par la correction que le contrôleur avait simulée et mesurée ; sortie identique à sa simulation, octet
  pour octet (`JUGE\FIGURE_DECOUPLAGE_CONTROLE_{GEOMETRIE,LECTURE,2,3,4}.md`).
- Relecture de langue phrase à phrase du texte servi, FR (194 phrases : 6 fautes, 19 maladresses) et EN (192 : 3 erreurs,
  39 maladresses) : corrigées. Points de fond tranchés au passage : l'effet, non la baisse réelle, sujet des verbes ;
  périmètre de l'Union ; solaire retiré des électricités comptées à leur contenu électrique (convention non vérifiée pour lui
  avant 2024, journal du 26/10) ; constat partagé avec Brockway et al. borné à l'échelle mondiale ; rang « pour chaque année
  de départ testée » ; FAQ au sens comptable. Relecture de contrôle des phrases changées
  (`JUGE\RELECTURE_LANGUE_DECOUPLAGE_CONTROLE.md`) : un défaut nécessaire (chapô anglais) ; bornes d'arrondi rétablies à
  la borne exacte ; « les scénarios énergétiques mondiaux », comme le résumé de Brockway et al. ; corrigés.
- Données structurées : sujet du jeu de données déclaré (`apropos`) ; sans lui, le gabarit déclarait « dette publique »
  (relecture de langue de la page dépense imprévue).
- Contrôles : `check-all --ci` 0 ; build et `typo_build` 0 défaut ; rendu 0 ; liens 0 critique ; dates 83/83, 0 bloc sans
  période ; couverture : 15 signaux, aucun nouveau.
- Envois : la page est citée par un courriel de la campagne ANTHROPY-EN (LOT3, parti le 12/11) ; aucun envoi non parti ne
  la cite.
- Instantané de relecture : fait le 12/11/2026 (195 phrases FR, 193 EN) ; `refonte` porté au 12/11/2026 ; journal : entrée du 12/11/2026.
- Mise en ligne : poussée sur le mandat de l'auteur, le 12/11/2026 (commit 42a4540) ; déploiement `hugo.yml`
  n° 43289023871 réussi (build, relecture, deploy, contrôle de fumée de la production).
- Attestation de la version servie : faite le 12/11/2026 vers 20 h 22 (heure de Paris). HTML servi identique au build
  contrôlé (arbre propre extrait de l'index), aux empreintes de cache des feuilles et scripts près, en FR et en EN ; les
  quatre SVG de la figure, le PNG du bureau, les deux cartes de partage et leurs vignettes, le JSON et le CSV servis
  identiques, octet pour octet, au commit.
- Laissés à l'auteur : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\A_ARBITRER.md`.

### Reprise du style (13/11/2026)

- Consigne de l'auteur (13/11/2026) : une mise en page « ultra lisible », au niveau de la page Parcoursup (règle 17
  du `CLAUDE.md` du site), adaptée au sujet. Étude, choix et mesures :
  `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\guides\ETUDE_STYLE.md`. Organes existants seulement
  (`_ressource-relief.scss`, `reperes-page.html`) ; les phrases ne changent pas, elles prennent une forme.
- Organes : trois repères (+58 % de consommation d'énergie primaire dans le monde selon l'EIA, PIB en parité de pouvoir
  d'achat ; le poids du PIB par habitant est 1,8 fois celui de la population dans la décomposition comptable ;
  −18 % dans l'Union européenne à 27, sur son territoire, selon l'EIA, −15 % selon Eurostat) ; les deux réserves sur
  l'Union européenne en paire de cartes ; les trois contrôles de robustesse en cartes numérotées ; un paragraphe coupé.
  Jetons `{dc.*}` seulement.
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
