# Fiche de conception — Combien coûte la dette publique ?

<!-- Fiche écrite le 17/11/2026, APRÈS la relecture des sources de la reprise « dette-b » (méthode de reprise, § R2) : la
page existait depuis le 15/08/2026, refondue le 11/10/2026, sans fiche. Découverte et mécanisme citent la ligne de verdict
qui les porte (rapport `D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\dette-b\SOURCES\
cout-de-la-dette-publique_R1.md`, noté « R1 »). -->

Page : `/cout-de-la-dette-publique/` (FR) · `/en/cost-of-french-public-debt/` (EN) · ouverte le 2026-08-15 · fiche du 2026-11-17

## Forme

Données (`ressource.type: quantitatif`) : la page publie des séries tirées d'un jeu (`dette_officielle`, INSEE et Eurostat,
réinterrogés chaque semaine) et en prend tout le modèle vérifié par machine — résultat en une phrase, figures SVG et PNG
avec version téléphone, bloc « Réutiliser », `Dataset`, JSON et CSV, jetons sans chiffre saisi, gardes vues mordre.

## Fiche de conception

### Question centrale

Combien la dette publique coûte-t-elle chaque année à la France, et pourquoi cette charge peut-elle monter quand la dette
cesse d'augmenter, ou baisser pendant qu'elle augmente ?

### Enjeu

Le débat public juge la dette à son stock rapporté au PIB ; ce que l'État paie chaque année est la charge d'intérêts, qui
dépend aussi du coût moyen de ce stock. Confondre les deux fait mal juger les marges budgétaires, dans un sens comme dans
l'autre.

### Croyance initiale

Plus la dette est grosse, plus elle coûte : doubler la dette doublerait la facture, et la facture suivrait la dette.

### Découverte principale

De 1995 à 2020, la dette est passée de 57,8 % à plus de 100 % du PIB pendant que sa charge d'intérêts tombait de 3,5 % à
1,3 % du PIB (R1, l. 50 : CONFORME À LA SOURCE, Insee BDM 010777608 et Eurostat) ; depuis le creux de 2020, les deux forces
jouent dans le même sens et la charge progresse plus vite que chacune des neuf autres grandes fonctions de dépense de 2020
à 2024 (R1, l. 102 : conforme à la source, fin de période précisée par CO-8).

### Mécanisme explicatif

La charge d'une année est le produit de l'encours et de son coût moyen, le taux implicite ; ce coût moyen rémunère des
titres émis à des dates et à des taux différents (R1, l. 72 : CONFORME À LA SOURCE, AFT, Bulletin mensuel n° 437) et ne
rejoint le taux de marché qu'au fil des refinancements, la durée de vie moyenne de la dette étant de 8 ans et 158 jours
(R1, l. 77 : CONFORME À LA SOURCE). La baisse du taux implicite, de 6,5 % en 1996 à 1,2 % en 2020, a compensé la hausse de
l'encours (R1, l. 56 et 73 : taux implicite recalculé par la relecture sur les séries primaires — c'est un calcul, aucun
producteur ne le publiant sous cette convention).

### Preuve décisive

La figure en ciseaux (dette et charge en part du PIB, 1995-2025) et la décomposition de la hausse de la charge depuis 2020
en effet de volume et effet de taux, contributions annuelles additionnées (CO-4) : la seconde montre que la hausse récente
vient pour partie du coût moyen, alors que l'encours, lui, montait déjà pendant les vingt-cinq ans de baisse.

### Pouvoir discriminant

Explications rivales réellement soutenues : « la charge monte parce que la dette monte » (lecture par le stock, la plus
courante) ; « parce que les taux montent » ; « parce que l'inflation renchérit les titres indexés » (saut de 2022). Le
témoin est l'identité charge = encours × taux implicite, qui ne change qu'une variable à la fois : de 1995 à 2020, le stock
double et la charge baisse, ce qui réfute la première lecture prise seule. Ce que le graphe révèle qu'une série isolée ne
montre pas : le croisement des deux courbes. Ce qu'il ne départage pas : la part de l'indexation dans le saut de 2022 (le
Sénat la chiffre pour l'État seul ; ajout renvoyé à l'auteur, `A_ARBITRER.md` du lot, § 0-1). Résistance : la décomposition
dépend de sa méthode (contributions annuelles additionnées ou calcul direct entre deux années, R1 P2-6 : 15,1 / 20,9
contre 14,85 / 21,15) ; le sens ne change pas. Levier rendu visible : la durée de vie de la dette fixe la vitesse à laquelle
un choc de taux se transmet à la facture.

### Limite

Le taux implicite est un coût moyen, non le taux auquel l'État emprunte le jour même ; la prévision du Gouvernement est
celle de la présentation du budget (l'avis du 2/11/2026 la révise, `A_ARBITRER.md`, § 1-8) ; les comparaisons de masses
portent sur 2024, dernière année de la ventilation par fonction, la charge la plus récente sur 2025 ; le calcul par foyer
fiscal est une échelle, non une répartition.

### Valeur finale

Le lecteur distingue le stock, le prix et la charge, et sait pourquoi la facture peut monter sans dette nouvelle ; le
chercheur dispose d'une série consolidée 1978-2026, de sa méthode et de ses gardes ; l'élu et l'association, d'une échelle
(la charge comparée aux grandes fonctions de dépense) qui ne mélange pas deux années.

### Singularité

Cette page existe parce qu'elle montre le ciseau 1995-2020 et sa fermeture, que le lecteur ne découvre ni dans la charge
budgétaire annuelle de l'AFT (lue : Bulletin mensuel n° 437) ni dans la seule série du ratio de dette (lue : Insee,
comptes trimestriels).

### Raccords

Livre *Dette publique : qui paie vraiment ?* — retenu, encart « Pour aller plus loin ». *ANTHROPIE* et la définition de
l'anthropie — retenus, encart « La même question sur le temps long » : où les coûts s'écoulent, qui règle la note.
AWP-07 et AWP-03 — retenus comme hypothèse interprétative de l'auteur, distincte des constats (R1, l. 147 : attribution
conforme). Pages voisines du dossier : « Pourquoi la dette augmente » (dynamique), « Qui paie » (répartition),
« Comparaison internationale » (prix et recettes), « Peut-elle baisser ? » — retenues par les onglets du dossier et les
renvois du texte.

## Fiche D0

Résultat visé, au plus près de la finalité : une page citée et reprise pour sa distinction entre stock et charge (figure
en ciseaux, série consolidée), qui serve le livre qu'elle prolonge. État initial et dates de relevé : non relevés dans
cette reprise (motif : préparation de nuit, sans accès aux tableaux de bord) ; à inscrire dans
`D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` le jour de la mise en ligne de la version reprise.

## Étapes de la méthode

- Plan d'outils : non refait (page existante ; outils de la reprise, `METHODE_REPRISE_RESSOURCE.md`).
- Relecture des sources par un agent neuf : fait (16-17/11/2026, `SOURCES\cout-de-la-dette-publique_R1.md`, 28 écarts).
- Sondes indépendantes de la session : fait (`SOURCES\SONDES_SESSION.md`, C-1 à C-9, S1-1, S1-4).
- Interventions : fait (`specs\cout.py`, `specs\generateurs.py`, `specs\complements.py`, `specs\forme.py`), chaque écart trié
  (`SYNTHESE.md`).
- Gardes vues mordre : fait (garde « ordre et sécurité », témoin `DETTE_MUTATION=gf03` : arrêt ; rejeu sans mutation : passe).
- Figures téléphone : fait (SVG et PNG régénérés par le générateur ; `check-figures.py` : 0 défaut).
- Recette 320-1 440 px : fait (`outils\captures.py`, débordement 0, lecture sous sa figure).
- Relecture de langue : fait pour les règles outillées (`check_langue.py`, aucune alerte nouvelle fondée) ; phrase à phrase
  du texte servi : non fait (à la publication, avec l'instantané).
- Juge interne à l'aveugle : voir `JUGE\` du lot.
- Panel avant et après, gate éditorial : non fait (reprise d'une page en ligne : le juge interne puis le jugement externe à
  l'aveugle en tiennent lieu, méthode de reprise § R5).
- Instantané de relecture : non fait (à la publication).
- Contre-expertise de la page : paquet préparé (`paquets_externes\`), réponse attendue.
- Accord de l'auteur : en attente.
