# Fiche de conception — Avons-nous tous le même droit à l'erreur ?

Page : `/enseignants/ecole-et-parcours/` (FR) · pas de version anglaise (exclusion déclarée : le programme de SES est
français, `lang_repli: "/en/resources/"`) · ouverte le 2026-10-02 · fiche écrite le 2026-11-17, à la reprise de la page
(lot « enseignants-ecole-et-parcours », `D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\enseignants-ecole-et-parcours\`),
**après** la relecture des sources (`SOURCES\RELECTURE_R1.md`, activité « Après le bac », et `SOURCES\RELECTURE_R2.md`,
activité « Licence », cités « R1 » et « R2 » ci-dessous ; sort de chaque écart : `SOURCES\SYNTHESE.md`).

## Forme

`usage` : deux activités pour la classe, une par objectif du chapitre sur l'École, chacune avec sa figure propre
(couche pédagogique du site, point 6). Critères : programme cité tel qu'il est écrit, à sa source ; activités prêtes à
l'emploi ; aucune question qui fasse trancher une politique ; fiche élève imprimable sans corrigé, qui se suffit à
elle-même (termes définis sur la feuille, réponses absentes de la feuille) ; corrigé qui n'affirme rien que les
documents ou la source ne portent, et qui dit les réponses alternatives recevables ; aucun chiffre saisi (jetons
`acces-val` et `licence-val`, gardes des deux générateurs) ; limites de la source reprises telles quelles.

## Fiche de conception

### Question centrale

Les parcours après le bac — où l'on s'inscrit, ce que l'on devient un an après l'entrée en licence — diffèrent-ils
selon l'origine sociale, et que permettent de conclure ces écarts ?

### Enjeu

Le programme de Terminale demande de distinguer massification et démocratisation, et de comprendre la multiplicité des
facteurs d'inégalités de réussite scolaire. Dans le débat public, les écarts de parcours selon l'origine se lisent
souvent comme des choix (« les enfants d'ouvriers choisissent les BTS »), ou comme l'effet direct de l'origine au
moment des études (« les étudiants modestes abandonnent faute de moyens »).

### Croyance initiale

Une inscription dit un choix ; et si les étudiants d'origine défavorisée sont plus souvent « non retrouvés » un an
après, c'est que l'origine les fait partir.

### Découverte principale

Rapporter à la bonne population change la lecture. Parmi les seuls étudiants non passés en deuxième année, la part des
non retrouvés est presque la même aux deux extrémités (27,1 % et 28,9 % pour la cohorte 2023) : l'écart de 6,0 points
observé sur tous les inscrits tient surtout à la fréquence du non-passage. Porté par R2, § 5 (« surtout » refait dans
les deux sens de la décomposition, 76 à 88 % selon la cohorte et le sens, sur les trois cohortes comparables), par la
sonde S3 de la session (83 à 88 % pour 2023) et par la garde du générateur (« plus des deux tiers »). Et le même service
qui publie la figure trouve, pour les entrants de 2019, qu'« à caractéristiques égales, la corrélation entre origine
sociale et réussite en licence est faible » (Note d'information n° 2026-06, R2, P1-2, sondée par la session).

### Mécanisme explicatif

Une part est un produit de parts : la part des non retrouvés parmi tous les inscrits est la part des non-passés
multipliée par la proportion de non retrouvés parmi eux (R2, § 3, Q3 et Q4). Les écarts de filière selon l'origine
passent en partie par la série du baccalauréat, très différente selon l'origine (tableaux 09.03 et 09.04 ; R1, § 5,
point 6 : ordre de grandeur sous hypothèse, non une mesure) ; à caractéristiques scolaires égales, l'association entre
origine et passage devient faible (NI 2026-06), l'origine agissant en amont sur ces caractéristiques mêmes. Ce sont des
décompositions et des associations, non des causes établies : la page le dit à chaque corrigé.

### Preuve décisive

Le tableau 13.03 de l'*État de l'enseignement supérieur* n° 18 (témoin : n° 19) et la feuille « Devenir cohorte
2023 » des tableaux nationaux de la Note Flash n° 29 du SIES : valeurs rejouées par R1 (28 cellules sur 28, 70 lignes du
CSV) et par R2 (20 cellules sur 20, chaque nombre du corrigé), chacun avec son propre lecteur ; constats retrouvés sur
les trois cohortes comparables, 2021 à 2023 (R2).

### Pouvoir discriminant

Page d'usage avec figures propres. Activité « Après le bac » : la figure ne départage pas « choix » et « contraintes »,
et la question 5 le fait dire ; elle départage deux mesures d'un écart (en points, en rapport), qui ne classent pas les
filières de la même façon (garde). Activité « Licence » : le changement de dénominateur départage deux lectures
descriptives de l'écart de non-retrouvés (« l'origine fait partir » contre « l'origine va avec un non-passage plus
fréquent, et les non-passés partent dans les mêmes proportions ») ; il ne dit rien des causes. Autre période : trois
cohortes, mêmes constats. Autre périmètre : l'origine manque pour environ un entrant en STS sur quatre (R1, P1-1) ; les
rapports de la première activité valent pour les inscrits d'origine connue, et la page le dit. Levier ou contrainte :
aucun ; aucune question ne tranche une politique.

### Limite

Deux populations différentes (tous les nouveaux bacheliers inscrits ; les seuls entrants en licence) et deux champs
(France métropolitaine et DROM ; France entière) ; une seule année pour la figure ; origine non renseignée pour 11,1 %
des inscrits, surtout en STS ; « non retrouvé » n'est pas « sorti des études » ; une situation d'inscription à un an,
non un diplôme ; associations, non causes ; le croisement origine × niveau scolaire n'existe que pour une autre cohorte
(2019) ; aucune relecture par un enseignant de SES (décision de l'auteur du 16/11/2026, écrite sur la page). Les
données suivent l'édition annuelle du SIES : la note de la cohorte 2024 est annoncée pour le 26/11/2026 (R2, § 8).

### Valeur finale

Deux séances de 20 à 30 minutes, prêtes à l'emploi, dont les figures, les fiches et les corrigés suivent seuls les
éditions du SIES ; l'élève sait ensuite comparer un écart en points et en rapport, changer de dénominateur, refuser de
lire une inscription comme un choix et une association comme une cause, et dire quelles données manquent pour
conclure.

### Singularité

Cette page fait calculer ce que la Note Flash du SIES ne publie pas (les parts parmi les non-passés), et confronte la
lecture de cette note, « l'origine sociale a une influence importante sur la réussite des étudiants », à celle de la
Note d'information de juillet 2026 du même service, qui trouve l'association faible à caractéristiques égales (Y = Note
Flash n° 29 et NI 2026-06, lues par R2, § 5, « Qui parle et d'où »).

### Raccords

Livre : *La Société du premier coup*, **retenu** (encart d'exemplaire de consultation : « L'activité ci-dessus décrit des
parcours d'inscription ; elle ne le met pas à l'épreuve. »). Définition de l'anthropie : **écartée** (sans rapport avec
l'activité). Working paper AWP-08 (réversibilité sociale) : **écarté** (l'activité ne le teste pas ; un lien la
présenterait comme son application). Pages voisines : le dossier « École, lycée et université » est relié par son
encart ; la page `/parcoursup-quelles-chances-d-etre-admis/` renvoie déjà ici (raccord entrant, « l'accès ici, la suite
là-bas ») : rien à ajouter.

## Fiche D0

Écrite le 02/10/2026 avant la mise en ligne (`06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`, section de la page) :
résultat visé, une adoption pédagogique identifiable ; diagnostics : visites, téléchargements de `parcours_licence.csv`,
réponses des lycées ; réexamen début janvier 2027. À mettre à jour à la publication de la reprise.

## Étapes de la méthode

- Plan d'outils : non fait (motif : reprise d'une page existante, outils fixés par la commande `/reprise-ressource`).
- Protocole du type `usage` et chaîne pédagogique (méthode du chantier, § M5) : fait (17/11/2026) ; programme relu à sa
  source (arrêté du 19/07/2019, BO spécial n° 8, par Internet Archive) et note de service du 11/09/2026 (BO spécial
  n° 4, PDF) ; chaîne question par question dans R1, § 3, et R2, § 3.
- Relecture des sources par deux rédacteurs séparés : faite (17/11/2026) ; aucun nombre faux ; R1 : 2 P1, 5 P2, 18 P3 ;
  R2 : 2 P1, 4 P2, 9 P3 ; sort de chaque écart dans `SOURCES\SYNTHESE.md` du lot.
- Scénarios d'architecture, panel avant : non fait (motif : reprise localisée, architecture de la page inchangée).
- Gardes vues mordre : fait (17/11/2026) ; 21 mutations des deux générateurs, dont cinq sur les gardes nouvelles
  (origine manquante surtout en STS, lue dans le tableau 13.01 ; catégories nommées au corrigé 4 ; ligne « Ensemble »
  dans la dérive ; témoin de population 13.01/13.03), toutes vues mordre, témoins propres
  (`RAPPORTS\MUTATIONS_GENERATEURS_P.txt` du lot).
- Figures : pieds complétés (origine manquante surtout en STS, « Autres », IUT, « ne se réduit pas à un choix » ;
  classes d'origine, changements d'établissement, degré de la réserve sur les non-retrouvés) ; skill `controle-figures`
  étapes 1 à 4 faites (valeurs inchangées, `check-figures` à 0 et témoin vu mordre, rendus bureau et téléphone
  regardés) ; étape 5 (deux contrôleurs indépendants) : à faire par la session « publier » sur l'état final.
- Juge interne à l'aveugle, premier écran, contre-analyse externe propre à la page : voir `LOT.md` du lot.
- Instantané de relecture : sans objet (aucune page « Pour enseigner » n'est marquée `refonte`).
- Accord de l'auteur : non fait (session de préparation, rien n'est publié).
