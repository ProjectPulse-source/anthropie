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

De 2000 à 2024, l'intensité énergétique mondiale a baissé de 28,5 % et la consommation d'énergie a augmenté de 58 % :
découplage relatif, pas absolu. Dans la décomposition, la hausse du revenu par habitant pèse environ deux fois plus que
celle de la population (+263 EJ contre +144 EJ), et la baisse de l'intensité en retire 172 : elle compense environ
deux cinquièmes de la poussée, pas davantage. Dans l'Union européenne, même producteur, même définition, la
consommation a baissé de 18 % pendant que le PIB augmentait de 42 % : un découplage absolu, sur son territoire.

### Mécanisme explicatif

Identité comptable E = population × (PIB / population) × (E / PIB), décomposée par la méthode de l'indice de Divisia
logarithmique moyen (somme exacte, sans résidu). Elle dit combien chaque terme a pesé, pas pourquoi : la baisse de
l'intensité mêle progrès d'efficacité, changement de la composition de l'économie et changement de convention de
mesure des énergies ; elle ne permet pas d'estimer un effet rebond (phrase interdite par l'arbitrage).

### Preuve décisive

Séries de l'EIA (énergie, PIB PPA constant, population), monde et UE, lues par script ; somme exacte de la
décomposition contrôlée ; témoin d'un autre producteur et d'une autre convention : énergie primaire de l'Energy
Institute (méthode de substitution), relayée par Our World in Data, et PIB de la Banque mondiale à prix constants
(`NY.GDP.MKTP.PP.KD`), recalcul complet de la décomposition sur ces sources.

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
- **Robustesse, montrée par une variante calculée.** Recalcul sur l'Energy Institute et la Banque mondiale (autre
  producteur, autre convention pour l'électricité non fossile) ; fenêtres 1990, 2000, 2010, 2015 et 2019.
- **Niveau atteint.** Descriptif et comptable ; discriminant entre (a) et (b) au sens arithmétique seulement ; pas
  décisionnel.
- **Levier ou risque éclairé.** Un objectif de baisse de la consommation totale ne s'atteint pas par la seule baisse
  de l'intensité si le revenu par habitant croît plus vite qu'elle ne baisse : c'est un ordre de grandeur, non une
  prescription.

### Limite

La décomposition est comptable : elle n'attribue aucune cause. L'intensité énergétique n'est pas l'efficacité d'un
usage. La convention de l'EIA compte l'électricité renouvelable à son contenu électrique : la croissance des
renouvelables y pèse moins qu'avec la méthode de substitution de l'Energy Institute (variante calculée). La
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
- Contre-expertise de la page : non faite (à décider par l'auteur, comme pour G1 et G3).
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
