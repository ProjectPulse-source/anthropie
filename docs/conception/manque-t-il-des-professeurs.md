# Fiche de conception — Manque-t-il des professeurs au lycée ?

Page : `/manque-t-il-des-professeurs/` (FR seul ; exclusion de l'anglais déclarée dans la page : débat, programme et
statistique français) · ouverte le 2026-10-07 · fiche écrite le 2026-11-13, à la reprise de la page (méthode de reprise
des ressources, lot « manque-t-il-des-professeurs »), **après** la relecture des sources par deux relecteurs séparés.
Pièces de la reprise : `D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\manque-t-il-des-professeurs\`
(`SOURCES\R1.md`, `SOURCES\R2.md`, `SOURCES\SYNTHESE.md`). Recherche d'origine :
`D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_MOYENS_2026-10-07\` (protocole écrit avant calcul, test décisif, verdict).

## Forme

Données (`quantitatif`, `donnees: [lycee_professeurs]`) : définitions, périmètres, millésimes, unités, calculs
reproductibles, changements de série, dénominateurs et incertitudes ; chaque chiffre important relié à sa source, son
calcul, sa figure et sa formulation. La page juxtapose des séries de producteurs différents (DEPP, ministère, OCDE,
DGFiP) : chaque rapprochement dit son champ (règle 13 du modèle des ressources de données).

## Fiche de conception

### Question centrale

Manque-t-il des professeurs au lycée, et que mesurent réellement les chiffres qui circulent sous ce nom ?

### Enjeu

Le mouvement lycéen de l'automne 2026 et la consultation nationale ont fait circuler trois familles de chiffres (cours
perdus, postes non pourvus, classes chargées) comme s'ils mesuraient la même chose ; décisions et revendications
portent sur des leviers différents (organisation des examens et du remplacement, concours, répartition des moyens).

### Croyance initiale

« Une heure de cours sur dix n'a pas lieu parce qu'il manque des professeurs » : cours perdus, concours désertés et
classes de 35 seraient trois symptômes d'un même manque, que l'on pourrait chiffrer.

### Découverte principale

Au lycée général et technologique public, en 2024-2025, les heures non assurées pour absences individuelles non
remplacées (3,9 points) pèsent moins que les trois autres motifs réunis (6,6 : fermetures presque toutes dues aux
examens, enseignants mobilisés par les examens ou les commissions, formation) — R1, lignes 2-3, 23, 28-29 : CONFORME À
LA SOURCE (NI 26-14, figures 2, 3 et 3.1), avec la réserve de la ligne 35 (enquête par échantillon, une année, sans
marge d'erreur : comparaison descriptive). Et le manque de professeurs lui-même n'est pas compté par ces séries : la
plus récente estimation publiée par l'OCDE, sur les données de la France, est de 0,4 % des postes du secondaire public
avant ou au début de la rentrée 2023, calculée sur les besoins de recrutement prévus ; ce n'est pas un décompte des
postes restés vacants (R2, écart E1, vérifié par la session sur la note pays de l'OCDE du 29/09/2026 ; valeur entrée
au jeu le 13/11/2026 sur décision de l'arbitrage, `scripts/sources_lycee_professeurs/complements.json`).

### Mécanisme explicatif

Trois mesures, trois objets. Les heures non assurées comptent des cours prévus qui n'ont pas eu lieu, quel qu'en soit
le motif ; un enseignant en poste mobilisé par un examen ou en formation fait perdre des heures sans qu'aucun poste ne
soit vide (R1, lignes 21-22, avec la précision que seules les heures non remplacées sont comptées). Les concours
comptent des candidats et des postes offerts, que fixe la décision publique : leur couverture dit combien on recrute,
pas le besoin (R1, lignes 74-75, CONFORME ; « que fixe le budget » : incise non sourcée, NON VÉRIFIÉ). La taille des
classes dit comment les élèves se répartissent entre les enseignants en poste (R2, lignes 79-88 : CONFORME À LA SOURCE,
réserve de nomenclature pour 2015). Aucun de ces mécanismes n'est une cause testée ici : la page juxtapose, elle
n'explique pas pourquoi les candidats ont baissé ni pourquoi les classes ont grossi (ligne 173).

### Preuve décisive

La décomposition par motif de la DEPP (NI 26-14, figure 2) et les jours de fermeture du lycée (figure 3.1 : 5,8 jours
d'examens sur 6,3), relus à la source par R1 et par la session (sondes). Pour les concours : fiches 9.27 et 9.28 du RERS
2026 (relues par R1 et la session), session 2026 hors série (résultats du ministère par section, deux concours externes,
troisième concours exclu : R1, écart 10).

### Pouvoir discriminant

Explications rivales réellement soutenues : (a) « les cours perdus viennent des professeurs absents non remplacés »
(USL, SNES) ; (b) « ils viennent de l'organisation du service, surtout des examens » (lecture que permet la DEPP). Le
témoin qui les départage sans changer d'autre variable : le même indicateur, même année, même champ, ventilé par motif
et par type d'établissement — au collège, les deux parts s'équilibrent (4,7 contre 4,9), au lycée la fermeture d'examen
fait l'écart. Quatre questions : *surprise* — la part des absences individuelles est minoritaire au lycée, pas au
collège ; *explications départagées* — (a) et (b) seulement pour la part de chaque motif, une année ; la question
« combien de professeurs manquent » n'est pas départagée ; *robustesse* — 2023-2024, publié à l'unité, donne le même
sens (6 contre 4), variante lue à la source (R1, ligne 34) ; *levier* — l'organisation du calendrier et des lieux
d'examens, et celle du remplacement, sans que la page dise quelle part serait évitable (lignes 30-31). Pour les concours
et les classes, la page décrit, elle ne tranche pas entre explications : elle le dit (ligne 173).

### Limite

Une seule année publiée au dixième ; enquête par échantillon sans marge d'erreur ; pas de ventilation par académie ni
par établissement ; le besoin d'enseignants n'est suivi par aucune série publique annuelle (des estimations ponctuelles
de l'OCDE, sur les besoins prévus) ; séries de champs différents pour la dépense (OCDE, DEPP, crédits budgétaires), qui ne
se prolongent pas ; dépenses des régions : treize collectivités, relations descriptives sans test.

### Valeur finale

Le lecteur sait distinguer trois chiffres qu'il reçoit ensemble, dire à quelle question chacun répond, et refuser deux
phrases qui circulent : « il manque tant de professeurs » et « une heure sur dix est perdue faute de professeurs ».

### Singularité

Cette page existe parce qu'elle décompose le « 10 % d'heures non assurées » par motif et le place à côté des concours et
des classes, ce que le lecteur ne trouve pas dans la NI 26-14 (qui ne parle ni des concours ni des classes), dans le RERS
(fiches séparées) ni dans les communiqués des acteurs (un chiffre chacun) — lus, pas supposés (relevé des énoncés,
`RECHERCHE_LYCEES_MOYENS_2026-10-07\test_decisif\ENONCES.md`).

### Raccords

- Définition de l'anthropie : **écartée** — page de faits (`quantitatif`), aucune lecture anthropique dans l'exposé.
- Livre : **retenu**, *La Société du premier coup*, par la question qui suit (« Après un premier échec, qui peut
  recommencer ? ») ; relation de prolongement, non de preuve.
- Working paper : **écarté**, aucun ne porte sur ces séries.
- Pages voisines : **retenue** `/le-niveau-des-eleves-baisse-t-il/`, qui renvoie déjà ici pour le recrutement : renvoi
  réciproque ajouté dans « Ce que ces données ne disent pas » (les causes), sur l'effet de ces moyens sur le niveau, que
  ni l'une ni l'autre page ne mesure.

## Fiche D0

Résultat visé, au plus près de la finalité : que la page soit citée pour ce qu'elle établit (décomposition des heures
non assurées, distinction des trois mesures) sans que sa réponse soit déformée en « il manque N professeurs ».
Diagnostics : requêtes et citations par les moteurs (Search Console, Bing) ; état initial et dates de relevé à inscrire
dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` à la publication — **non fait** (la reprise du 13/11
prépare la page, elle ne la publie pas).

## Étapes de la méthode

- Plan d'outils, protocole du type, scénarios, panel avant, contre-expertises de phase A : fait à la création et à la
  refonte du 10/10/2026 (`RECHERCHE_LYCEES_LECTURE_2026-10-09\REFONTE_PILOTE\PROFESSEURS\`), avant que la fiche existe.
- Relecture des sources par deux relecteurs séparés : fait (13/11/2026, `SOURCES\R1.md`, `SOURCES\R2.md`) ; sondes de
  la session : fait (`SOURCES\SONDES_SESSION.md`).
- Gardes vues mordre : fait (13/11/2026, `--check` 77 gardes, sept familles de mutations arrêtées).
- Figures téléphone : inchangées par la reprise.
- Relecture de langue, premier écran, recette 320-1440, juge interne : voir `LOT.md` du lot.
- Juge interne à l'aveugle : fait (13/11/2026) ; jugement externe à l'aveugle `PRO-20261113-094035` : fait, arbitré
  (`.claude\external-audits\ARBITRATIONS\PRO-20261113-094035_arbitrage.md`) ; contre-arbitrage de l'auteur
  (`Arbitrage-01`, 13/11/2026) : arbitré et appliqué (`LOTS\manque-t-il-des-professeurs\ARBITRAGE_01_2026-11-13.md`).
- Publication : sur demande de l'auteur du 13/11/2026 (« ton arbitrage et publication »).
