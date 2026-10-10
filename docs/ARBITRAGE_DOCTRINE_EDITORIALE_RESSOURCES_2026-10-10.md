# Arbitrage — doctrine éditoriale et expérience de lecture des ressources (10/10/2026)

- **Pièce** : `DOCTRINE_EDITORIALE_RESSOURCES_ANTHROPIE_CC.md`, version 1.0 du 10/10/2026, 26 016 o, SHA-256
  `be2a23018546fa6827844653ed425e468405a8837b5cc30a146953185785a49c`, remise par l'auteur. Archivée verbatim avant
  lecture : `D:\PRO\00_PILOTAGE\_PIECES_RECUES\DOCTRINE_EDITORIALE_RESSOURCES_ANTHROPIE_CC_2026-10-10.md` (empreinte
  identique, fichier suivi par git). Original rangé : `D:\CONTRE_EXPERTISE\PRO\ENTRANTES_2026-10-10\`.
- **Nature** : mandat opérationnel adressé à Claude Code, rédigé à partir du HTML de la page pilote
  `/les-eleves-maitrisent-ils-moins-bien-la-langue-francaise/` — son rédacteur n'a vu ni le dépôt, ni les
  générateurs, ni les règles déjà actées. Il propose ; les règles du site et les décisions datées de l'auteur
  restent en vigueur tant qu'elles ne sont pas remplacées ici.
- **Deux principes de l'auteur, donnés avec la pièce (10/10/2026), qui gouvernent l'ensemble** :
  1. **liberté maximale sur la construction narrative** — réorganisation, condensation, nouvelles visualisations,
     redistribution entre ressources ;
  2. **intransigeance sur la rigueur scientifique** — aucune dramatisation, simplification abusive ou causalité
     inventée pour augmenter l'engagement.

## Vérifications faites avant d'arbitrer

Les constats de la pièce sur la page pilote (§ 11) ont été relus sur le fichier de contenu, et non sur le HTML :

| Constat de la pièce | Mesure sur `content/…/_index.md` | Statut |
|---|---|---|
| Ouverture d'« environ 130 mots » qui énonce presque toute la conclusion | `chapo:` = 133 mots ; il donne les quatre résultats (chronologie, dictée, PISA, vocabulaire) | **confirmé** |
| Trois encadrés « Le résultat en une phrase » | `div.resultat-phrase` aux sections `#chronologie`, `#vocabulaire`, `#plaisir` | **confirmé** |
| Six réponses de FAQ | six entrées `faq:` | **confirmé** |
| Longue investigation *Club des Cinq* au milieu du fil | section `#textes`, 737 mots, insérée le 10/10 (`b745716`, `1e6bda8`) entre vocabulaire et plaisir de lire | **confirmé** |

## Verdicts

| § | Point | Verdict | Décision et articulation |
|---|---|---|---|
| 0 | Ordre de priorité : véracité d'abord, aucune amélioration ne compense une dégradation du fond | **ACCEPTÉ** | Identique au noyau d'arbitrage (intégrité = contrainte supérieure). « Standardiser l'exigence et le contrôle, jamais la pensée ni l'architecture narrative » devient la règle directrice des ressources |
| 1 | Lecteur directeur non spécialiste ; quatre usages (repérer, comprendre, approfondir, réutiliser) | **ACCEPTÉ** | Les quatre usages ont déjà leurs organes : chapô, corps, `details.repli`, « Réutiliser ». Ils décrivent des besoins, pas des quotas |
| 2 | Diagnostic avant réécriture (A à F) | **ACCEPTÉ** | Proportionné : complet pour la page pilote, ramené à une page pour les suivantes (voir § 12) |
| 3.1 | Moteur narratif = écart entre l'explication spontanée et ce que les preuves imposent ; réponse loyale dès l'ouverture | **ACCEPTÉ** | Déjà la règle « le chapô donne la réponse ». Le test « inverser deux sections dégrade-t-il la compréhension ? » entre dans le gate narratif |
| 3.2 | Choisir entre plusieurs architectures, jamais en série | **ACCEPTÉ, avec articulation** | La hiérarchie « surprendre → montrer → expliquer → documenter » du modèle dette **reste l'invariant à l'intérieur d'une section** (réponse, figure, explication, preuve repliée). **L'ordre des sections et l'architecture de la page deviennent libres** (principe 1 de l'auteur). « Une page = une découverte principale » reste |
| 3.3 | Micro-règles d'écriture | **ACCEPTÉ** | Recoupent R6 et la règle « qui, quoi, quand, par rapport à quoi » ; rien à câbler |
| 4 | Garde-fous causaux non compensables ; « non significatif » ≠ « inchangé », « inconnu » ≠ « nul » ; limites au contact de l'inférence | **ACCEPTÉ** | Déjà tenus par les gardes de prose des générateurs ; **nouveau** : la limite d'une inférence s'écrit dans la phrase ou le paragraphe qui la porte, pas seulement dans « Ce que ces données ne disent pas » |
| 5 | Zéro répétition **sans fonction** ; rôles du chapô, de l'encadré, de la synthèse, de la FAQ | **ACCEPTÉ** | Le contrôle bloquant exige **au moins un** `resultat-phrase` : on peut en retirer, pas tous. FAQ visible et balisage identiques (règle GEO G5 déjà en place). « Ce qu'il faut retenir » (carte en exergue, 10/10) dit ce qui a changé, ne récite pas les sections |
| 5 | « Condensation » | **ACCEPTÉ AVEC MODIFICATION** | On condense la **redite**, jamais la **preuve** : la preuve longue passe en repli sur la même URL. Motif : R6 — condenser une matière bonne détruit de la valeur |
| 5 | Pas de pages satellites artificielles ; redistribution entre ressources | **ACCEPTÉ** | Une page propre ne naît toujours que si deux déclencheurs sont réunis, dont un observable (règle « une question, une section ») ; redistribuer entre pages **existantes** est libre (principe 1) |
| 6.1-6.2 | Hiérarchie visuelle ; trois figures qui transforment la compréhension plutôt que huit qui illustrent | **ACCEPTÉ** | Langage graphique du site inchangé (bleu stock, orange coût, deux couleurs) ; une figure nouvelle suit la discipline du modèle (générateur, SVG + PNG ensemble, titre, source et précaution dans l'image) |
| 6.3 | Recette à 360-390, 768 et 1280-1440 px, clavier, ancres, zoom | **ACCEPTÉ AVEC MODIFICATION** | Pour toute **refonte** : 390, 768 et 1280 px (au lieu de 390 seul), arrivée par chaque ancre, onglets collants. Une page neuve garde la recette actuelle |
| 7 | SEO/GEO sans pseudo-optimisation ; liens explicatifs ; livre en prolongement discret | **ACCEPTÉ** | Conforme : `appel-livre` en fin de page, exemplaire offert en tête de l'encadré (décision du 07/10, inchangée). **Une ancre publiée ne change jamais** (règle du site, plus stricte que « redirections si les URL changent ») |
| 8 | Pilote puis généralisation de la méthode, jamais du plan | **ACCEPTÉ** | Phases A-D retenues telles quelles |
| 9 | Grille /100, objectif ≥ 90, classes P0-P3 | **ACCEPTÉ AVEC MODIFICATION** | **Dimensions et classes P0-P3 retenues ; le nombre ne l'est pas.** Chaque dimension reçoit *tenu / partiel / manqué* avec sa justification et, pour un manque, sa correction vérifiable. Critère de publication : aucun P0, aucun P1 non traité. Motifs : la pièce dit elle-même « outil de revue, non vérité statistique » ; précédents — grille /100 convertie en contrôle qualitatif (papier CEP), deux notes de 93,1 et 94,5 sur un texte inchangé (double traitement), « aucune note ni score » de la fabrique |
| 10 | Instrumentation avant/après, sans faux indicateur | **ACCEPTÉ AVEC MODIFICATION** | La fiche D0 existante sert de point avant ; GoatCounter (`?src=`, `?campaign=`) mesure arrivées, parcours et demandes d'exemplaire. **Aucun capteur nouveau** (clics d'ancre, défilement) : la pièce les juge elle-même ambigus, et R2 interdit un dispositif sans condition de mort. Ce qui ne se mesure pas se dit « jugement éditorial documenté » |
| 11 | Application à la page pilote | **ACCEPTÉ** comme liste de frottements | Les quatre constats sont vérifiés (tableau ci-dessus). Les deux récits A et B sont deux scénarios à comparer en phase A, avec au moins un troisième (hybride) |
| 11 | Section `#textes` (*Club des Cinq*) : maintien condensé, repli ou ressource satellite | **ACCEPTÉ AVEC MODIFICATION** | Défaut retenu : **repli sur la même URL**, ancre `#textes` conservée, une phrase d'entrée dans le fil principal. Une page satellite exigerait les deux déclencheurs, et le chantier « langue offerte » est en sommeil sur décision de l'auteur (pas de recherche publiée) |
| 12 | Sept livrables par ressource | **ACCEPTÉ AVEC MODIFICATION** | Page pilote : les sept. Pages suivantes : **un seul fichier de chantier** (diagnostic, scénarios, tableau de traçabilité, note inter-pages) + la recette ; la refonte elle-même est dans le commit. Motif : aucune bureaucratie pour un geste qui n'en demande pas |
| final | Critère de succès : le lecteur peut dire ce qu'il croyait, ce qu'il sait, sur quelles preuves, quelle question s'ouvre | **ACCEPTÉ** | Devient la question du gate narratif ; le panel de lecteurs simulés peut l'éprouver sur la page refondue |

**Aucun point ne requiert de décision de l'auteur.** Aucun n'est rejeté : la pièce est compatible avec les règles du
site ; les modifications portent sur la mesure (pas de score), le grain des livrables et l'articulation avec la
hiérarchie du modèle dette.

## Ce qui entre dans les règles du site

Section « Doctrine éditoriale des ressources » du `CLAUDE.md` du site : les deux principes de l'auteur, l'articulation
section / page, la condensation bornée à la redite, la grille qualitative, la recette à trois largeurs pour une refonte,
le critère de succès. Rien n'est câblé en contrôle machine : aucun de ces points n'a de capteur objectif (R2).

## Suite

Phase A sur la page pilote : version horodatée (commit courant du site et empreinte du jeu `lan`), diagnostic A-F,
trois scénarios, tableau de conservation des preuves — puis refonte, recette et contre-expertise de la page construite.
