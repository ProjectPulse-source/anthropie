# Fiche de conception — Une loi votée s'applique-t-elle tout de suite ?

Page : `/une-loi-votee-s-applique-t-elle-tout-de-suite/` (FR) · `/en/does-a-law-apply-as-soon-as-it-is-passed/` (EN) · ouverte le
2026-10-06 ; refondue le 2026-10-12 ; fiche écrite le 2026-11-17, à la reprise du lot « promesses-b », après la relecture des
sources.

## Forme

`juridique-institutionnel` et `quantitatif`. Critères : séquence vote, promulgation, publication, entrée en vigueur,
mesures d'application et mise en œuvre, chaque étape avec son acteur et son texte ; comptes de lois et de mesures recalculés
loi par loi ; taux publiés rangés par définition, jamais classés ; « en attente » distingué de « en retard ».

## Fiche de conception

### Question centrale

Une fois votée, une loi s'applique-t-elle, et combien de lois attendent encore les décrets ou arrêtés qu'elles appellent ?

### Enjeu

Une promesse qui passe par la loi n'est pas tenue au vote : entre le vote et l'application, des mesures que le
Gouvernement doit prendre peuvent manquer, et les taux publiés pour le dire ne mesurent pas la même chose.

### Croyance initiale

« Une loi sur deux n'est pas appliquée » ; ou, à l'inverse, une loi votée et publiée s'applique d'elle-même.

### Découverte principale

Au 05/10/2026, 130 des 399 lois promulguées d'octobre 2017 à septembre 2025, hors conventions, attendaient encore au moins
une mesure ; « environ une sur deux » n'est vrai qu'en rapportant ces 130 lois aux 254 que le baromètre classe avec des
mesures à prendre ; et le Conseil d'État exige que les mesures nécessaires soient prises dans un délai raisonnable. —
Lignes qui la portent : relecture `SOURCES\une-loi-votee-s-applique-t-elle-tout-de-suite_R1.md`, § 0 (comptes du baromètre
recomptés par le relecteur sur l'extrait archivé et sur les fichiers complets du producteur, état du 16/11 compatible : 129
lois, 561 mesures) et l. 118-133, 301-321 (conformes).

### Mécanisme explicatif

Le code civil reporte l'entrée en vigueur des dispositions « dont l'exécution nécessite » des mesures d'application ; le
Premier ministre les prend, et le juge en contrôle le délai. Les comptes viennent des échéanciers que tient le Secrétariat
général du Gouvernement : le baromètre met en forme la comptabilité du débiteur de l'obligation, le Sénat seul en est le
témoin extérieur. — Lignes qui le portent : `_R1`, l. 23-52 (Constitution et code civil, conformes) ; P2-6 (« Ces
échéanciers sont mis à jour manuellement par les services du SGG », page du baromètre relue par la session le 17/11).

### Preuve décisive

Le registre de concordance loi par loi entre le baromètre et le Sénat (399 lois, même champ, 24 classements divergents) et
le recompte indépendant des mesures ; les décisions du Conseil d'État citées mot pour mot.

### Pouvoir discriminant

Rivales : « une loi sur deux n'est pas appliquée » (formule courante) ; « les taux du Gouvernement sont gonflés ». La page
départage la première par ses deux dénominateurs (399 et 254) ; la seconde ne se tranche pas : les définitions diffèrent
(arrêtés, mesures différées, raisons « politiques » selon le Sénat lui-même), et la page range les taux sans les classer.

### Limite

Le baromètre ne publie que l'état courant : l'état de chaque mesure six mois après sa loi ne se reconstitue pas ; ses
indicateurs de délai portent sur l'état courant. Aucune donnée lue ne compte les refus portés devant le juge.

### Valeur finale

Une grille pour lire tout taux d'application (lois couvertes, mesures comptées, date d'arrêté) et les comptes par session,
réutilisables.

### Singularité

Cette page existe parce qu'elle rapproche loi par loi le baromètre de l'Assemblée et les rapports du Sénat, et range les
taux du Sénat et du Gouvernement par définition, ce que le lecteur ne trouve dans aucune des deux publications.

### Raccords

- Définition de l'anthropie : écartée (page de faits).
- Livre *Un président peut-il tenir ses promesses ?* : retenu (bloc d'appel « Après le vote »).
- Working paper : écarté.
- Pages voisines : « Qui peut faire adopter une loi ? » (l'étape d'avant) et « Neuf promesses de campagne » (barre du dossier).

## Fiche D0

Résultat visé : qu'un lecteur ne reprenne plus « une loi sur deux » sans dire ce qu'elle compte, et sache qu'« en
attente » n'est pas « en retard ». Diagnostics : Search Console (« décret d'application », « taux d'application des
lois »), citations par les moteurs génératifs. Relevés J+30, J+60 : feuille de route GEO, à la mise en ligne.

## Étapes de la méthode

- Plan d'outils : non fait à la reprise (page existante).
- Protocole du type : fait (2026-11-17, relecture `_R1` ; dates des rapports du Sénat lues en tête des PDF ; page
  « statistiques » du baromètre et répertoire de la DILA relus par la session).
- Scénarios, panel avant, contre-expertise de phase A : faits à la refonte du 12/10/2026 (`REFONTE_PILOTE\APPLIQUER\`).
- Gardes vues mordre : fait (autotest du générateur, 23 mutations).
- Figures : inchangées.
- Recette, juge interne à l'aveugle, premier écran : voir `LOT.md` du lot.
- Relecture phrase à phrase, instantané, accord de l'auteur : à la publication.
