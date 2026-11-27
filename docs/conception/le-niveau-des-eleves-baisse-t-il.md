# Fiche de conception — Le niveau des élèves baisse-t-il ?

Page : `/le-niveau-des-eleves-baisse-t-il/` (FR) · pas de version anglaise (exclusion déclarée au front matter :
débat, programme et statistique français) · publiée le 2026-10-08, refondue le 2026-10-10, reprise le 2026-11-11
(branche A' du pilote « intelligibilité des ressources »), version définitive appliquée et publiée le 2026-11-12.

Fiche écrite **après coup**, sur la page publiée : la refonte d'octobre est antérieure à la règle 12 (22/10/2026) et la
page n'a pas de fiche dans `docs/conception/`. Elle dit l'état réel ; ce qui vient du dossier de refonte est daté, ce
qui n'a pas été fait dans cette passe est écrit « non fait ».

## Forme

`quantitatif` (front matter : `ressource.type: ["quantitatif"]`), parce que la page reprend et recalcule des séries
officielles (OCDE, IEA, DEPP) et que chacune de ses affirmations est un nombre muni d'un périmètre, d'un millésime et
d'une qualification de significativité. Critères propres du protocole, un par ligne :

- **définitions** : chaque évaluation, chaque terme statistique dont dépend une conclusion est défini là où il sert ;
- **périmètres** : quels élèves (un âge, une classe, une voie), quels pays (38 membres pour les rangs, moyenne de
  l'OCDE sur les pays comparables) ;
- **millésimes** : la fenêtre de chaque variation est dite, et les fenêtres différentes ne sont pas confondues ;
- **unités** : points de chaque échelle, parts en %, centièmes d'écart-type, jamais mêlés sans le dire ;
- **calculs reproductibles** : générateur, extrait figé avec empreintes, jeu en JSON et CSV ;
- **changements de série** : indice social de l'OCDE, test de la journée défense et citoyenneté, test de seconde
  de 2025 en mathématiques ;
- **dénominateurs** : de qui une part est-elle la part (population représentée, échantillon) ;
- **décompositions** : une standardisation décrit, elle n'attribue pas ;
- **incertitudes** : significativité publiée, erreur type, absence de test dite comme telle ;
- **chaque chiffre important** se relie à sa source, son calcul, sa figure et sa formulation.

## Fiche de conception

### Question centrale

Le niveau des élèves baisse-t-il ? Sous sa forme travaillable, arbitrée le 10/10/2026 : que mesure chaque évaluation,
que peut-on conclure de leur désaccord, et que ne permet-il pas de conclure ?

### Enjeu

Un chiffre, celui de PISA, porte à lui seul le débat public sur l'école. Lu comme « tout s'effondre » ou comme « c'est
exagéré, tout le monde baisse », il conduit à chercher la cause d'un recul dont on n'a établi ni le périmètre (quels
élèves), ni la date, ni la généralité. Le lecteur — parent, enseignant, journaliste, élu — a besoin de savoir ce qu'il
peut affirmer sans être démenti par une autre mesure officielle.

### Croyance initiale

Deux croyances symétriques, relevées par le panel « avant » du 10/10 : « le niveau baisse, point » (un déclin général,
toutes mesures confondues) ; « c'est exagéré » (tout le monde baisse, et les tests passés en classe ne montrent rien).
Les deux supposent qu'une seule mesure peut répondre.

### Découverte principale

*Reprise du 27/11/2026 (lot `niveau-depp-2026`), écrite après la relecture des sources.* La réponse dépend de
l'instrument et de la discipline, et ce désaccord n'est pas une contradiction. PISA, à 15 ans, établit une baisse
significative de 2015 à 2025, plus forte que celle de la moyenne de l'OCDE sur les estimations ponctuelles, et hors de la
moitié centrale des pays en mathématiques. Parmi les évaluations passées en classe, CEDRE établit aussi, par un test, des
baisses en mathématiques (2014-2019, en fin d'école et de collège) et en sciences en fin de collège (2018, 2024) ; les
évaluations nationales de sixième, de quatrième et de seconde reculent en français depuis 2021 (2023 pour la quatrième),
sans test publié, mais ne vont pas dans le même sens en mathématiques ; PIRLS et TIMSS ne mettent pas en évidence de
baisse sur leurs derniers intervalles, ce qui ne prouve pas que les tendances diffèrent. Lignes qui la portent :
protocoles 1 et 2 (`VERDICT.md`, N1, N2 ; `VERDICT_2.md`, N11) ; `VERDICT_9.md`, N24 TIENT (français) et N25 SENS DIVERS
(mathématiques) ; `VERDICT_10.md`, N27 TIENT et tableau des sciences ; relecture des sources du 27/11, R1 É1 et R2 P0-1
(la phrase « les évaluations passées en classe ne mettent pas en évidence la même baisse » était fausse membre par
membre).

Deux découvertes secondes, subordonnées à la première : en France, le milieu et le sommet de la distribution reculent
autant que le bas, dans chaque quart social, quand la moyenne de l'OCDE amortit la baisse vers le haut ; et le fait
qu'à 15 ans moins d'élèves soient encore au collège atténue arithmétiquement la baisse observée (trois mesures : 35,
43 et 36 points en mathématiques au relevé du 9 octobre 2026). Cette lecture ne nomme qu'un des deux mouvements de la
répartition (la seconde professionnelle et le CAP jouent en sens inverse) : relevé par la relecture R3 du 27/11, renvoyé
à l'auteur (`A_ARBITRER.md` du lot, § 4.2).

La règle « une page, une découverte principale » n'est donc tenue que par cette hiérarchie ; l'architecture (scénario
C2) a été arbitrée le 10/10 et n'est pas rouverte.

### Mécanisme explicatif

Deux mécanismes sont établis sur la page. Pourquoi des mesures peuvent différer sans se contredire : chacune a ses
élèves (un âge ou une classe), sa compétence (appliquée ou proche des programmes), sa période, son échelle, son enjeu et
sa façon d'établir une évolution (un test sur échantillon, ou aucun test pour une évaluation proposée à tous) ; et une
baisse significative d'un côté, une variation non significative de l'autre, ne font pas une différence de tendance
(`VERDICT.md`, contrôle 5 ; `VERDICT_9.md`, R9-1 ; `VERDICT_10.md`, R10-1 ; relecture R2, § 3, tableau des membres). Pourquoi la composition par classe joue : la moyenne est la somme des scores de chaque classe pondérés
par leur part ; à scores de classe donnés, moins d'élèves dans la classe aux scores les plus bas relève la moyenne.

Deux mécanismes ne sont pas établis, et la page le dit : pourquoi PISA baisse ; pourquoi les évaluations ne disent pas
toutes la même chose (règle 14 : « mécanisme encore inconnu »).

### Preuve décisive

- OCDE, *PISA 2025 Results*, volume I, tableaux I.B1.2a.36 à 38 : trois baisses significatives (règle de 1,96 fois
  l'erreur type) ; séries de la France identiques à celles de la DEPP à 0,05 point près, la DEPP arrondissant au
  dixième (témoin).
- IEA : symboles de significativité des tableaux de tendance de TIMSS, et PIRLS — aucune variation significative sur
  le dernier intervalle, niveaux de 1995 et de 2001 significativement au-dessus des derniers.
- DEPP, Note d'Information 26-40, figure 11 web : pour des cohortes largement correspondantes, +9 centièmes
  d'écart-type au test de seconde contre −18 à PISA en mathématiques — le producteur fait lui-même le rapprochement.
- Données individuelles de PISA 2015 et 2025 : standardisation qui retrouve au centième les moyennes publiées par
  l'OCDE.
- DEPP, CEDRE : évolutions significatives indiquées en gras par la DEPP (NI 20-33, 20-34, 22-28, 22-29, 26-12, 26-13),
  police lue par script, valeurs transcrites des mathématiques contrôlées par le rapport du HCSP (`VERDICT_10.md`).
- DEPP, évaluations nationales de 2026 (DT 2026-E24, E26, E27) : valeurs lues par script dans le texte des documents,
  séries antérieures dans les tableurs des NI 26-21 et 26-22 (`VERDICT_9.md`).
- Générateur : 138 gardes et 42 mutations à la publication du 27/11/2026, toutes vues mordre (étapes ci-dessous).

### Pouvoir discriminant

Explications rivales réellement soutenues, et le témoin qui les départage :

| Rivale (qui la soutient) | Témoin, une variable changée | Ce que montre la page |
|---|---|---|
| « Tout le monde baisse » (récit courant ; lecteurs du panel) | même période, moyenne de l'OCDE puis place de la baisse française parmi 38 pays | la France perd davantage que la moyenne dans les trois domaines ; en mathématiques elle sort de la moitié centrale ; même place parmi les seuls pays de l'Union européenne ou sans les cinq pays signalés (variantes calculées). Rang descriptif : l'OCDE ne publie pas de test de l'écart |
| « C'est la composition : moins de redoublants, donc d'autres classes » (lecture qui relativise) | scores de 2025, répartition entre classes de 2015 | la baisse est plus forte à répartition de 2015, et n'est pas réduite à composition de 2015 pour la classe, le sexe et la famille (six variantes avec la classe : aucune ne la réduit de plus d'un point) ; sans la classe, la repondération sur la famille la réduit (de 35 à 25 points en mathématiques), et avec la classe les deux mouvements se compensent presque exactement. Calculs descriptifs : aucune part de la baisse n'est attribuée à la composition |
| « Les élèves ne s'appliquent plus à une épreuve sans enjeu » | élèves de 2025 repondérés à la répartition d'effort déclaré de 2022 | plus des neuf dixièmes de la baisse demeurent ; calcul descriptif, l'effort étant déclaré après l'épreuve |
| « C'est le bas qui décroche » | seuils fixes, puis positions dans la distribution, puis les mêmes par quart social | le sommet et le milieu reculent autant que le bas, dans chaque quart |
| « PISA est un artefact : les autres tests ne montrent rien » | même pays, autres instruments, dont ceux qui ont un test (CEDRE) et ceux qui n'en ont pas (évaluations nationales) ; cohortes correspondantes (DEPP) ; longue période | la rivale ne tient pas : CEDRE établit des baisses en mathématiques et en sciences en fin de collège, les évaluations nationales reculent en français ; pas de baisse significative récente dans PIRLS et TIMSS, sans que cela prouve des tendances différentes ; baisse significative de TIMSS et de PIRLS sur la longue période ; comparaison de 28 pays descriptive, non concluante en sciences |

Les quatre questions :

1. *Que révèle le graphe qu'une série isolée ne montre pas ?* La figure signature place la baisse française parmi
   celles de 38 pays : dans la moitié centrale en sciences, à sa frontière en lecture, hors d'elle en mathématiques.
2. *Quelles explications départage-t-il ?* Il écarte « tout le monde baisse » comme réponse suffisante pour les
   mathématiques, sur les estimations ponctuelles ; il ne l'écarte ni pour la lecture ni pour les sciences ; il ne
   dit rien des causes.
3. *Résiste-t-il à un autre périmètre, indicateur ou période ?* Variantes calculées : pays de l'Union européenne,
   sans les cinq pays signalés ; séries longues (2000, 2003 : baisses significatives ; sciences depuis 2006 : non) ;
   seuils et positions dans la distribution. Ce qui ne résiste pas à l'examen se dit : les rangs ne sont pas testés.
4. *Quel levier, contrainte ou risque aide-t-il à voir ?* Un risque : conduire un débat ou une politique sur un seul
   instrument. Aucun levier : ces séries mesurent un recul, pas sa cause, et la page l'écrit.

La confrontation est sur la page, en langage courant, après le chiffre principal (sections `comparaison`,
`composition`, repli sur l'effort). Dans la version publiée, la section `comparaison` ne désignait pas la figure
qu'elle commente : corrigé dans cette passe (intervention 3).

### Limite

Aucune cause n'est établie. Aucun test ne compare les tendances de deux évaluations, ni les baisses de deux pays. Les
standardisations décrivent. Le rapport technique de l'OCDE ne traite plus son indice social comme une échelle de
tendance (son volume I en publie pourtant la variation). Les évaluations nationales et le test de seconde n'ont pas de
test de significativité publié, et leurs résultats de 2026 excluent l'académie de Toulouse ; les mathématiques de
seconde de 2025 ne se comparent pas strictement à 2024. Les mathématiques de CEDRE sont transcrites (notes refusées aux
scripts), contrôlées par le rapport du HCSP ; ses sciences de 2024 en fin d'école reposent sur un échantillon réduit.
Aucune des mesures réunies ici ne suit dans le temps le niveau en fin de lycée. Les calculs de l'auteur n'ont pas été reproduits par un tiers (note de
clôture du 10/10).

### Valeur finale

Après lecture, on peut dire sans jargon : je croyais qu'un chiffre répondait ; je sais que PISA mesure à 15 ans une
baisse significative, plus forte qu'en moyenne dans l'OCDE ; qu'en classe, CEDRE établit aussi des baisses en
mathématiques et en sciences en fin de collège, que les évaluations nationales reculent en français mais pas toutes en
mathématiques, et que PIRLS et TIMSS ne montrent pas de baisse sur leurs périodes récentes sans pour autant la démentir ;
que les meilleurs reculent aussi et que le changement de répartition entre classes ne suffit pas à rendre compte de la baisse ; cela repose sur les tableaux de l'OCDE, de l'IEA et de la DEPP, recalculés ; et la question
qui s'ouvre est : pourquoi. Outil réemployable : quatre questions devant tout chiffre sur le niveau (quels élèves,
quelle compétence, quelle période, et avec quelle incertitude) — implicite dans la version publiée, écrit dans la
synthèse par cette passe (intervention 10). S'y ajoutent les figures et le jeu sous licence libre.

### Singularité

Cette page existe parce qu'elle révèle, pour un même pays et côte à côte, ce que six évaluations disent et ne
disent pas — leurs élèves, leurs fenêtres, leur significativité, et la discipline où elles s'accordent ou non (le
français recule dans toutes les évaluations nationales, les mathématiques non) — et trois mesures de la même baisse
selon la composition retenue, que le lecteur ne découvre pas dans les publications des producteurs prises une à une (volume I
de PISA 2025, notes de la DEPP, rapports de l'IEA), où chaque évaluation est commentée dans sa propre échelle.

Statut de ce « Y » : **non relu dans cette passe** — ces publications ne font pas partie des pièces lues. L'affirmation
est reprise du dossier de recherche et de la page ; une exception est connue et dite par la page : la DEPP rapproche
elle-même le test de seconde et PISA (Note 26-40). La singularité tient donc à l'ensemble, à la standardisation sur
données individuelles et au classement des baisses, non à ce rapprochement.

### Raccords

- **Définition de l'anthropie** : écarté. Page de faits de type `quantitatif` : aucune lecture anthropique dans
  l'exposé des constats (règle 4 de « Architecture des ressources ») ; aucune hypothèse de l'auteur n'y est testée.
- **Livre** : retenu, comme prolongement et non comme condition. Phrase qui le porte (`appel-livre`, *La Société du
  premier coup*) : « Cette page mesure ce que savent les élèves à un moment donné. La question qui vient ensuite est
  celle des parcours […]. » Constat : le front matter ne déclare pas `ressource.livres` ; la réciprocité livre →
  ressource n'est donc pas posée par cette page (hors du périmètre de la passe, front matter intouché).
- **Working paper** : écarté — aucun ne fonde cette page.
- **Pages voisines** : retenues, deux. *Langue* : « Pour la langue seule, avec la dictée de CM2 depuis 1987 et la
  lecture pour le plaisir, la frise de la page voisine montre des mesures qui n'évoluent pas toutes de la même façon, et
  des reculs plus anciens » (reformulée le 27/11/2026, comme la page Langue)
  (section `evaluations`). *Professeurs* : « Les concours, les classes et les heures de cours perdues sont traités
  dans la page Manque-t-il des professeurs au lycée ? » (section `limites`). Écartées : *Parcoursup* et *Étudiants*,
  qui répondent à d'autres questions (accès au supérieur, santé des étudiants) sans relation de preuve avec la mesure
  du niveau.

## Fiche D0

**Non relevée dans cette passe** : la feuille de route GEO ne fait pas partie des pièces lues, et la passe ne publie
rien, donc n'ouvre aucun point zéro. État connu par le seul front matter : page publiée le 08/10/2026, refondue
(relecture attestée du 11/10/2026), dernière révision de lecture le 11/11/2026 (figure des pays). Si cette version est
retenue pour publication, la fiche D0 s'écrit alors : résultat visé au plus près de la finalité, diagnostics, état
initial, dates de relevé.

**Écrite le 12/11/2026, à la mise en ligne de la version définitive** : `06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`
du dépôt de pilotage, section « reprise de `/le-niveau-des-eleves-baisse-t-il/` » (résultat visé, mécanisme,
diagnostics, état initial, ce qui l'infirme ; relevés le 12/12/2026 et le 11/01/2027).

## Étapes de la méthode

État réel de chaque étape, de la plus récente à la plus ancienne : la publication du 27/11/2026, la reprise du même
jour (préparée), la session de publication du 12/11/2026, puis la passe du 11/11/2026 sur la branche A' du pilote.

### Publication du 27/11/2026 (`/reprise-ressource niveau-depp-2026 publier`)

- **Jugement externe à l'aveugle** : réponse archivée avant lecture (`paquet_externe\REPONSE_EXTERNE_2026-11-27_verbatim.txt`
  du lot, SHA-256 `63767d29…c145cfd2`), arbitrée point par point (`ARBITRAGE_REPONSE_EXTERNE_2026-11-27.md`) : version
  proposée retenue ; son P0 (la repondération sans la classe, absente du corps) corrigé avec la limite de `VERDICT_6`
  (non-réponse en hausse) ; une variation sans test publié se décrit sans seuil, « stable » n'est écrit qu'attribué à la
  DEPP ; CEDRE en grille ; périmètre de la figure des évaluations dans sa légende ; « significatif » défini par le test ;
  « réunies ici » là où une absence générale n'est pas établie ; synthèse en trois résultats ; méthode raccourcie, nature
  des vérifications dite (modèles de langage, arbitrage écrit). Rejetés, avec motif : retirer « tout le monde baisse »,
  une accroche qui promettrait un « pourquoi ».
- **Générateur** : 138 gardes ; mutation `sans_classe` ajoutée, `ma_2526` réécrite ; 42 mutations, toutes vues mordre.
- **Contrôles** : `check-all --ci` 0 ; build 0 ; `typo_build` 0 ; liens 0 critique ; rendu 0 ; dates 83/83 ; lettre
  (`CONTROLE_LETTRE.md` du lot, § 2 ter : 37 réserves réécrites, chacune justifiée, aucun nombre publié changé) ; langue :
  signalements lus, aucun défaut ; règle « crédibilité par le résultat » : 0 occurrence servie ; captures de 320 à
  1 440 px : 0 débordement, lecture contre figure à +74 px au plus ; grilles CEDRE et évaluations nationales à 320, 390
  et 768 px, avec et sans script : 0 débordement, 0 chevauchement.
- **Juge neuf** sur les 28 passages changés depuis la version jugée à l'extérieur (`JUGE\JUGEMENT_TOUR3.md` du lot) :
  aucun P0, version à publier retenue 24 fois sur 28 ; un P1 qu'elle portait, introduit par la méthode raccourcie
  (« ces contrôles ont arrêté le calcul », faux pour le test de seconde et les concours, qui signalent l'écart), corrigé ;
  remarques mineures corrigées ou écartées avec motif (`JUGE\SORTS_TOUR3.md`). Tour 4 (12 passages) : aucun P0 ni P1
  propre ; P1 commun : la réserve du passage à l'écran (R10-4) manquait dans les résumés. Tour 5 : la demi-réserve
  (« dont la DEPP a mesuré l'effet ») tait le report sur les scores, et les **sciences de fin de collège sont aussi
  passées à l'écran en 2018** (NI 19.33) ; vérifié par la session à la source (visionneuse de la DEPP, les scripts étant
  refusés) et archivé (`pieces\cedre\TRANSITION_PAPIER_NUMERIQUE_NI_19-33_20-33_20-34.md` du dossier de recherche ;
  addendum de `VERDICT_10.md`). Tour 6 : réserve complète, symétrique et attribuée, **aucun P0 ni P1** ; remarques de
  forme corrigées (`JUGE\SORTS_TOUR5.md`). TIMSS Advanced (conclusion interdite n° 18) : P1 commun, en ligne depuis
  octobre, renvoyé à l'auteur (`A_ARBITRER.md`, § 4.5).
- **Premier écran**, retesté à chaque changement du chapô (v1 à v5, question 7 ajoutée sur l'écran) : la réserve placée
  après les sciences était rattachée à elles seules, par les lecteurs comme par le témoin ; placée sur CEDRE, avant
  l'énumération (« dont les scores tiennent compte du passage des épreuves à l'écran »), deux lecteurs conformes sur
  sept questions et témoin vu mordre (`JUGE\PREMIER_ECRAN_PUBLICATION_V5_RESULTATS.md` du lot).
- **Relecture** : phrases changées relues une à une, instantané refait, `refonte` au 27/11/2026.
- **Fiche D0** : republication inscrite dans la feuille de route GEO, sous la fiche du 12/11 (relevés inchangés).

### Reprise du 27/11/2026 (`/reprise-ressource niveau-depp-2026`, mode préparer)

Dossier : `06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\niveau-depp-2026\` du dépôt de pilotage (`LOT.md`).

- **Relecture des sources** : fait, trois relecteurs neufs, consigne scellée, sans le verdict du 19/11 (`SOURCES\`,
  `SYNTHESE.md` : 44 écarts, chacun avec son sort). Deux P0 de généralisation retrouvés par deux relecteurs ; CEDRE
  sciences, en baisse significative en fin de collège, trouvé par un relecteur et absent du verdict du 19/11.
- **Protocoles 9 et 10** : écrits et scellés avant calcul (évaluations nationales 2026 ; CEDRE), calculs, verdicts
  (`VERDICT_9.md`, `VERDICT_10.md`), extraits recopiés dans `scripts/sources_niveau_eleves/` avec leurs empreintes.
- **Générateur** : 137 gardes, 39 mutations, toutes vues mordre ; jeu JSON et CSV augmentés (CEDRE, évaluations
  nationales, seconde 2026).
- **Interventions** : chapô, repère 2, synthèse, « En trois phrases », questions fréquentes 1, 2, 3 et 6, liste des
  évaluations, grille des évaluations nationales (organe `grille-reperes`), paragraphe CEDRE, corrections de la relecture.
  Aucun nombre publié ne change de valeur (contrôle de la lettre : `CONTROLE_LETTRE.md`, 26 réserves réécrites, chacune
  justifiée).
- **Figures** : aucune régénérée sur le fond ; les SVG ne diffèrent que par les espaces insécables de l'organe commun
  `pied_figure.py` (18/11), les PNG sont identiques à l'octet. Deux corrections de figure renvoyées à l'auteur.
- **Forme** : lecture contre figure à +97 px au plus (seuil 150), aucun débordement de 320 à 1 440 px, grille lisible
  à 320 px avec et sans script.
- **Juge interne** (à l'aveugle, un tour, repères compris) : la version proposée retenue, aucun P0, contre treize dans la
  version en ligne ; un P1 commun aux deux versions (fenêtre de 2019 en mathématiques) et trois P1 du texte commun,
  traités (`JUGE\SORTS.md` du lot) : fenêtres de sensibilité ajoutées (2017, 2019), « l'essentiel depuis 2018 » borné à
  la lecture et aux mathématiques, repli TIMSS / PISA sans opposition d'échelles ; TIMSS Advanced renvoyé à l'auteur.
  Passages changés rejugés par un juge neuf : aucun P0 ni P1. La sixième en mathématiques, de 2025 à 2026, est dite « au
  même niveau, à un point près » (la DEPP l'écrit stable). Générateur : 137 gardes, 41 mutations vues mordre.
- **Premier écran** : deux lecteurs conformes sur six questions, témoin trompeur vu mordre.
- **Jugement externe** : paquet validé, en attente d'enregistrement dans la navette (`LOT.md` du lot).
- **Non fait** : publication (mode préparer) ; instantané de relecture (`check-relecture --strict` : 88 phrases changées
  depuis le 12/11, à refaire sur la version publiée) ; fiche D0 (inchangée, la page n'est pas republiée).

### Mise en page du 12/11/2026 (contre-expertise technique PRO-20261112-045621)

- La figure collante sortait sous la barre d'onglets en fin de bloc : retirée. À côté de chaque figure, le résultat en
  une phrase et un premier niveau d'explication ; la suite du raisonnement passe sous le bloc (baisse, seconde,
  composition). Aucune lecture ne dépasse sa figure de plus de 150 px (mesure : `outils\captures.py` du chantier).
- « Elle revient près de la baisse observée », occurrence manquée le matin, devient « elle n'en est pas réduite ».

### Mise à jour du 12/11/2026, sur l'avis du contradicteur externe

- Trois corrections décidées par le contradicteur (`LOTS\niveau\ARBITRAGE_REPONSE_NIVEAU_2026-11-12.md` du chantier) :
  décompte « 12 pays sur 28 » retiré (points de deux échelles), page et jeu ; recul du milieu et du sommet circonscrit à
  la lecture et aux mathématiques ; « revient à peu près au niveau observé » remplacé par « la baisse n'en est pas
  réduite » (`VERDICT_7.md`, B), chiffres présentés comme ceux de la spécification retenue.
- Gardes : 116 (une retirée avec l'affirmation qu'elle protégeait) ; 32 mutations, toutes vues mordre.

### Session du 12/11/2026 (`/reprise-ressource niveau publier`)

- **Chaîne de recherche** : effort déclaré recalculé sur les niveaux 2022 et 2025 (la colonne de différence de la DEPP
  est désalignée à partir du Luxembourg), 37 pays au lieu de 38, rang inchangé ; protocole 8 (catégorie « première »)
  entré dans l'extrait ; extrait recopié, différence vérifiée (`n_pays`, bloc `p8_premiere`, date de relevé).
- **Gardes** : 117 (99 auparavant) ; six mutations nouvelles (`effort_n`, `premiere_sig`, `premiere_reste`,
  `premiere_gt`, `bloc_saisi`, `bloc_saisi_seconde`) ; les 32 mutations mordent.
- **Figure des évaluations** : titre « la variation comparée » ; fenêtre 2021-2024 du test de seconde nommée dans la
  légende, le texte alternatif, le résultat en une phrase, le corps et la FAQ.
- **Version définitive** appliquée (`PILOTE\VERSION_DEFINITIVE\_index.md` du chantier), jugée à l'aveugle par le
  contradicteur externe (arbitrages `PRO-20261112-000538` et `REPONSE-04`).
- **Écarts relevés par la relecture des sources du calibrage du 12/11 et encore présents** : déclarés, avec leur
  formulation proposée, dans `LOTS\niveau\A_ARBITRER.md` du chantier ; ils n'ont pas eu de jugement externe et ne sont
  pas publiés dans cette session.

### Passe du 11/11/2026 (branche A')

- **Plan d'outils** (`outils_du_produit.py ressource`) : non fait (script hors des pièces de la passe).
- **Protocole du type** : fait dans cette passe (`DIAGNOSTIC.md`, § 1) ; en amont, sept protocoles écrits avant
  calcul (front matter, `ressource.nature`).
- **Scénarios d'architecture** : fait le 10/10/2026 (`PHASE_A_NIVEAU.md`, § 2 ; C2 retenu par test d'inversion,
  `PHASE_B_NIVEAU.md`, § 2). Non rouverts.
- **Panel avant** : fait le 10/10/2026 (cinq lecteurs simulés, annexe de `PHASE_A_NIVEAU.md`). Non refait.
- **Contre-expertise de phase A** : faite le 10/10/2026 (`PHASE_A_ARBITRAGE_NIVEAU.md`).
- **Gardes vues mordre** : fait le 10/10/2026 (mutations `conjointe`, `conjointe_forte`, `ocde_moyenne`). Cette passe
  n'ajoute aucune garde (générateur en lecture seule) et, en conséquence, aucun qualificatif chiffré nouveau.
- **Figures téléphone** : fait le 10/10/2026 ; figures inchangées.
- **Relecture de langue** : faite dans cette passe sur le texte servi d'un build local, pour les passages modifiés et
  leurs voisins ; motifs de `check-rendu-ressources.py` et `check-typo-fr.py` à 0 sur ce build.
- **Recette 320-1280** (`recette.py`) : non faite (aucun navigateur dans cette passe ; les interventions n'ajoutent ni
  bloc, ni figure, ni tableau — un paragraphe, un lien interne, une coupe de paragraphe).
- **Panel après** : non fait. Aucune mesure de réception ne soutient donc les interventions : ce sont des jugements
  instrumentés, pas des résultats.
- **Gate éditorial** : fait dans cette passe (`DIAGNOSTIC.md`, § 2 à 4).
- **Relecture phrase à phrase FR et EN** : FR, faite sur les phrases changées (`PHRASES_CHANGEES.md`) ; EN, sans
  objet.
- **Instantané de relecture** : non refait. `check-relecture.py --strict` signale 23 phrases absentes de l'instantané
  du 2026-11-11 — exactement celles de cette passe ; l'instantané se refait après relecture et accord.
- **Contre-expertise de la page** : faite le 10/10/2026 sur la version refondue (`PHASE_C_CLOTURE_NIVEAU.md`). Non
  refaite sur cette version.
- **Accord de l'auteur** : non demandé. Rien n'est commité, rien n'est publié.
- **Déclaration de la fiche** (`ressource.conception`, règle 12) : non faite — le front matter et `docs/conception/`
  sont hors du périmètre ; cette fiche est à y verser si la version est retenue.
