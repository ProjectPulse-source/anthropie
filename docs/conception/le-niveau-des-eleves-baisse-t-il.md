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

La réponse dépend de l'instrument, et ce désaccord n'est pas une contradiction. PISA, à 15 ans, établit une baisse
significative de 2015 à 2025, plus forte que celle de la moyenne de l'OCDE dans les trois domaines sur les estimations
ponctuelles, et hors de la moitié centrale des pays en mathématiques ; PIRLS en CM1 et TIMSS en CM1 et en quatrième
ne la mettent pas en évidence sur leurs derniers intervalles, qui ne sont pas les mêmes, ce qui ne prouve pas que les
tendances diffèrent ; sur la longue période, TIMSS en mathématiques en quatrième et PIRLS baissent aussi (TIMSS en
sciences en quatrième, non). Lignes qui la portent : protocole 1 (N1, N2) et protocole 2 (N11), `VERDICT.md` et
`VERDICT_2.md` du dossier de recherche ; relecture des sources du calibrage du 12/11/2026, écart 4.

Deux découvertes secondes, subordonnées à la première : en France, le milieu et le sommet de la distribution reculent
autant que le bas, dans chaque quart social, quand la moyenne de l'OCDE amortit la baisse vers le haut ; et le fait
qu'à 15 ans moins d'élèves soient encore au collège atténue arithmétiquement la baisse observée (trois mesures : 35,
43 et 36 points en mathématiques au relevé du 9 octobre 2026).

La règle « une page, une découverte principale » n'est donc tenue que par cette hiérarchie ; l'architecture (scénario
C2) a été arbitrée le 10/10 et n'est pas rouverte.

### Mécanisme explicatif

Deux mécanismes sont établis sur la page. Pourquoi des mesures peuvent diverger sans se contredire : chacune a ses
élèves (un âge ou une classe), sa compétence (appliquée ou proche des programmes), sa période, son échelle et son
enjeu ; et une baisse significative d'un côté, une variation non significative de l'autre, ne font pas une différence
de tendance. Pourquoi la composition par classe joue : la moyenne est la somme des scores de chaque classe pondérés
par leur part ; à scores de classe donnés, moins d'élèves dans la classe aux scores les plus bas relève la moyenne.

Deux mécanismes ne sont pas établis, et la page le dit : pourquoi PISA baisse ; pourquoi les évaluations divergent
(règle 14 : « mécanisme encore inconnu »).

### Preuve décisive

- OCDE, *PISA 2025 Results*, volume I, tableaux I.B1.2a.36 à 38 : trois baisses significatives (règle de 1,96 fois
  l'erreur type) ; séries de la France identiques à celles de la DEPP à 0,04 point près (témoin).
- IEA : symboles de significativité des tableaux de tendance de TIMSS, et PIRLS — aucune variation significative sur
  le dernier intervalle, niveaux de 1995 et de 2001 significativement au-dessus des derniers.
- DEPP, Note d'Information 26-40, figure 11 web : pour des cohortes largement correspondantes, +9 centièmes
  d'écart-type au test de seconde contre −18 à PISA en mathématiques — le producteur fait lui-même le rapprochement.
- Données individuelles de PISA 2015 et 2025 : standardisation qui retrouve au centième les moyennes publiées par
  l'OCDE.
- Générateur : 99 gardes au 10/10/2026 (dossier de refonte, note de clôture), dont des mutations vues mordre. **Non
  rejoué dans cette passe** : le générateur est en lecture seule.

### Pouvoir discriminant

Explications rivales réellement soutenues, et le témoin qui les départage :

| Rivale (qui la soutient) | Témoin, une variable changée | Ce que montre la page |
|---|---|---|
| « Tout le monde baisse » (récit courant ; lecteurs du panel) | même période, moyenne de l'OCDE puis place de la baisse française parmi 38 pays | la France perd davantage que la moyenne dans les trois domaines ; en mathématiques elle sort de la moitié centrale ; même place parmi les seuls pays de l'Union européenne ou sans les cinq pays signalés (variantes calculées). Rang descriptif : l'OCDE ne publie pas de test de l'écart |
| « C'est la composition : moins de redoublants, donc d'autres classes » (lecture qui relativise) | scores de 2025, répartition entre classes de 2015 | la baisse est plus forte à répartition de 2015, et revient au niveau observé à composition de 2015 pour la classe, le sexe et la famille ; six variantes, aucune ne la réduit de plus d'un point |
| « Les élèves ne s'appliquent plus à une épreuve sans enjeu » | élèves de 2025 repondérés à la répartition d'effort déclaré de 2022 | plus des neuf dixièmes de la baisse demeurent ; calcul descriptif, l'effort étant déclaré après l'épreuve |
| « C'est le bas qui décroche » | seuils fixes, puis positions dans la distribution, puis les mêmes par quart social | le sommet et le milieu reculent autant que le bas, dans chaque quart |
| « PISA est un artefact : les autres tests ne montrent rien » | même pays, autres instruments ; cohortes correspondantes (DEPP) ; longue période | pas de baisse significative récente ailleurs, sans que cela prouve des tendances différentes ; baisse significative de TIMSS et de PIRLS sur la longue période ; comparaison de 28 pays descriptive, non concluante en sciences |

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
standardisations décrivent. L'indice social de l'OCDE ne se compare plus entre 2015 et 2025. Le test de seconde n'a
pas de test de significativité publié, et ses mathématiques de 2025 ne se comparent pas strictement à 2024. Rien ne
mesure dans le temps le niveau en fin de lycée. Les calculs de l'auteur n'ont pas été reproduits par un tiers (note de
clôture du 10/10).

### Valeur finale

Après lecture, on peut dire sans jargon : je croyais qu'un chiffre répondait ; je sais que PISA mesure à 15 ans une
baisse significative, plus forte qu'en moyenne dans l'OCDE, que les autres évaluations ne la montrent pas sur leurs
périodes récentes sans pour autant la démentir, que les meilleurs reculent aussi et que la répartition entre classes
n'explique pas la baisse ; cela repose sur les tableaux de l'OCDE, de l'IEA et de la DEPP, recalculés ; et la question
qui s'ouvre est : pourquoi. Outil réemployable : quatre questions devant tout chiffre sur le niveau (quels élèves,
quelle compétence, quelle période, écart significatif ou non) — implicite dans la version publiée, écrit dans la
synthèse par cette passe (intervention 10). S'y ajoutent les figures et le jeu sous licence libre.

### Singularité

Cette page existe parce qu'elle révèle, pour un même pays et côte à côte, ce que quatre évaluations disent et ne
disent pas — leurs élèves, leurs fenêtres, leur significativité — et trois mesures de la même baisse selon la
composition retenue, que le lecteur ne découvre pas dans les publications des producteurs prises une à une (volume I
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
  lecture pour le plaisir, la frise de la page voisine montre la même divergence et des reculs plus anciens »
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

État réel de chaque étape, de la plus récente à la plus ancienne : la session de publication du 12/11/2026, puis la
passe du 11/11/2026 sur la branche A' du pilote.

### Mise en page du 12/11/2026 (contre-expertise technique PRO-20261112-045621)

- La figure collante sortait sous la barre d'onglets en fin de bloc : retirée. À côté de chaque figure, le résultat en
  une phrase et un premier niveau d'explication ; la suite du raisonnement passe sous le bloc (baisse, seconde,
  composition). Aucune lecture ne dépasse sa figure de plus de 150 px (mesure : `outils\captures.py` du chantier).
- « Elle revient près de la baisse observée », occurrence manquée le matin, devient « elle n'en est pas réduite ».

### Mise à jour du 12/11/2026, sur l'avis du contradicteur externe

- Trois corrections décidées par le contradicteur (`LOTS
iveau\ARBITRAGE_REPONSE_NIVEAU_2026-11-12.md` du chantier) :
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
  formulation proposée, dans `LOTS
iveau\A_ARBITRER.md` du chantier ; ils n'ont pas eu de jugement externe et ne sont
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
