# Fiche de conception — Les étudiants vont-ils plus mal que les autres jeunes ?

Page : `/les-etudiants-vont-ils-plus-mal/` (FR) · pas de version anglaise (exclusion déclarée : le bloc « École, lycée et
université » est français seulement, statistique, débat et institutions français ; cible de l'onglet EN
`lang_repli: "/en/resources/"`, comme les trois pages voisines) · ouverte le 2026-10-23, **écrite avant tout texte de
la page**.

Chantier : `D:\PRO\06_PROMOTION\RECHERCHE_MALAISE_ETUDIANT_2026-10-23\` — note de l'auteur reçue le 23/10
(`_PIECES_RECUES/Ressources_Education_recu_2026-10-23.txt`, SHA-256 `262bd229…`), neuf avis contradictoires,
contre-expertise `PRO-20261023-180856` arbitrée (`D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261023-180856_arbitrage.md`).
**L'arbitrage fait foi** sur tout point où cette fiche le résume.

## Forme

`explicatif-causal` et `quantitatif` (deux types déclarés). La page éprouve une explication causale en six maillons
(la note de l'auteur) et publie des séries officielles qui la testent.

Critères `explicatif-causal`, un par ligne :
- mécanisme écrit pour chaque hypothèse, avec la grille de l'arbitrage (Q7) : fait observé → mécanisme possible →
  élément concordant → observation qui l'invaliderait → conclusion limitée ;
- hypothèses concurrentes à égalité de traitement : causes propres aux études, causes communes à la génération, effet
  de composition, effet de déclaration, causalité inverse ;
- contrefactuels nommés : les jeunes qui n'étudient pas (même âge), les lycéens (avant l'entrée dans le supérieur),
  les périodes d'avant 2017 ;
- temporalités : chaque cause datée, et confrontée à la date de la dégradation qu'elle prétend expliquer (l'inflation de
  2022 ne peut pas expliquer la hausse de 2020-2021) ;
- constat, interprétation et causalité séparés dans la phrase même ; « peut contribuer » ne devient jamais « provoque » ;
- dire ce qui ferait varier la conclusion (le test à âge égal, § Limite).

Critères `quantitatif`, un par ligne :
- définitions et instruments : épisode dépressif caractérisé (CIDI-SF, douze mois), état anxieux (HAD-A > 10),
  détresse psychologique (MHI-5, quatre semaines) — trois objets, jamais additionnés ni confondus ;
- périmètres et millésimes : chaque vague d'enquête avec son champ (inscrits à l'université ou tous établissements,
  répondants réinterrogés), sa période de référence et sa date ;
- changements de série : Baromètre santé 2024 non comparable à 2021 ; deux chiffres OVE pour 2016 (20 % enquête Santé,
  28 % repris par le SIES) montrés tels quels ; une seule édition du SIES (n° 19) pour la série de dépense, jamais une
  série composite ;
- dénominateurs : dépense **par étudiant** ≠ dépense totale ; bacheliers dans une génération ≠ taux de réussite ≠
  entrée à l'université ; chômage des actifs de 15-24 ans ≠ situation de tous les jeunes ;
- calculs reproductibles : générateur à écrire (`scripts/update_malaise_etudiant.py`, jeu `malaise_etudiant`), jetons et
  gardes, JSON et CSV ; les valeurs lues dans des PDF ou des figures en image sont **transcrites et vérifiées contre la
  source archivée**, et la phrase de méthode le dit (catégories de l'audit du 12/10/2026).

## Fiche de conception

### Question centrale

Les étudiants vont-ils plus mal que les autres jeunes, et quelle part de la dégradation observée depuis 2017 tient à ce
qui est propre aux études plutôt qu'à ce que vit toute leur génération ?

### Enjeu

Le « malaise étudiant » fonde des demandes de moyens, des politiques (repas à 1 €, aide psychologique, restrictions du
téléphone) et un récit public de l'université abandonnée. Si la dégradation est surtout commune à la génération, les
réponses universitaires visent à côté ; si elle est plus forte chez les étudiants, l'argument de la génération sert
d'excuse. Se tromper de population, c'est se tromper de politique — et l'enjeu concerne les lycéens qui y entrent.

### Croyance initiale

Celle de la note reçue : massification de 1985 sans moyens, réformes qui fragmentent les études, smartphone, chocs du
covid, de l'inflation et du logement, absence de perspectives — six causes empilées qui produisent un « malaise étudiant
généralisé ». Et son contre-récit, celui de nos premiers avis : un malaise générationnel et mondial, à peu près
indépendant de l'université. La page les éprouve tous les deux.

### Découverte principale

Ni l'un ni l'autre ne tient tel quel. De 2017 à 2021, la dépression progresse chez tous les adultes, mais **le plus chez
les étudiants** : +7 points, contre +5,3 chez les chômeurs et +4,4 chez les actifs occupés (Santé publique France, BEH
2023 n° 2, 18-75 ans) ; dans le même temps, l'anxiété, mesurée autrement, reste stable (BEH 2025 n° 14). Ces écarts ne
sont pas standardisés selon l'âge : aucune donnée publiée ne permet encore de dire si être étudiant ajoute quelque chose
à être jeune. Le « malaise » n'est pas un objet unique, et la question décisive n'a pas encore reçu de réponse
publique. **Candidate, à confirmer par la lecture** : la dégradation commence avant le supérieur (enquête EnCLASS,
collégiens et lycéens, 2018-2022) — si c'est le cas, elle déplace la question vers le lycée.

### Mécanisme explicatif

Deux familles de mécanismes, qui peuvent se combiner et ne s'excluent pas :
- **communs à la génération** : le choc du confinement (isolement, rupture des routines, 2020-2021), certains usages
  numériques (effet causal possible de pratiques précises, Castelo et al. 2025 ; effet non détecté de politiques
  scolaires restrictives, SMART Schools 2025), des anticipations dégradées (climat, logement, défiance) ;
- **associés au fait d'étudier** : la pression sur les moyens par étudiant depuis 2014 (dépense moyenne en baisse alors
  que la dépense totale augmente ; 12 460 € à l'université contre 19 070 € en classe préparatoire en 2024), le coût du
  logement et la précarité financière (associée à la détresse dans les enquêtes OVE), l'isolement résidentiel, les
  examens ;
- **et deux mécanismes qui faussent la lecture** : la composition (la massification change qui étudie ; les femmes
  déclarent davantage de détresse) et la sélection (le malaise fait décrocher, on n'observe que ceux qui restent ;
  causalité inverse entre difficultés d'études et détresse).
La massification de 1985 (deux vagues, 1985-1995 puis 2009-2023) et les réformes LMD restent des transformations
documentées dont la contribution au malaise n'est pas identifiée.

### Preuve décisive

1. Les hausses de l'épisode dépressif par situation professionnelle, BEH 2023 n° 2 (Léon, du Roscoät, Beck), texte et
   figure 3 — **figure à lire dans le PDF** (`beh.santepubliquefrance.fr/beh/2023/2/pdf/2023_2_1.pdf`) pour les niveaux
   2017 et 2021 de chaque statut ; les écarts (+7,0 / +5,3 / +4,4 / +1,7) sont relus dans le texte (23/10).
2. La stabilité des états anxieux 2017-2021, BEH 2025 n° 14 (relu le 23/10).
3. La série EnCLASS (bien-être des collégiens et lycéens) — **non lue** : si elle ne montre pas de dégradation avant le
   supérieur, l'angle « avant l'université » tombe et la page le dit.
4. Témoin de comptabilité des sources : chaque valeur OVE avec son enquête et son champ (fiche SIES n° 16, lue le 23/10
   dans l'archive du web, le site du SIES répondant 503) ; la dépense par étudiant dans la seule édition n° 19 du SIES.

**Test décisif avant d'écrire la page** (modèle dette, discipline 4) : la page ne s'écrit que si la figure 3 du BEH
confirme, en niveaux, que l'écart d'évolution étudiants / autres statuts est lisible avec ses intervalles ; s'il ne
l'est pas (intervalles qui se recouvrent), la découverte principale devient « aucune donnée publique ne distingue les
étudiants », et le plan se réécrit autour de ce manque.

### Limite

- **Aucune estimation à âge égal** : le BEH compare des statuts de structures d'âge différentes ; la différence de
  différences étudiants / non-étudiants de 18-24 ans (Baromètres 2017 et 2021, âge et sexe contrôlés) exige les
  microdonnées ou une tabulation de Santé publique France — décision de l'auteur en attente (arbitrage, § 4). Cette
  limite fixe le sens du résultat : elle a son unité de texte propre (leçon 8 du pilote), jamais une subordonnée.
- Même à âge égal, l'écart serait descriptif : les groupes sont sélectionnés ; une absence d'écart ne disculperait pas
  l'université (protections et contraintes peuvent se compenser).
- Les séries OVE ne forment pas une évolution homogène ; aucune hausse 2016-2024 n'est calculée.
- Aucune comparaison internationale tant qu'elle n'est pas faite sur séries.
- Déclarer n'est pas souffrir : une partie des hausses peut tenir à la libération de la parole ; la page ne sait pas
  dire laquelle.

### Valeur finale

Après lecture, on sait dire sans jargon : ce qu'on croyait (six causes, ou une génération perdue) ; ce qu'on sait (la
dépression a augmenté, plus vite chez les étudiants, l'anxiété non ; les moyens par étudiant reculent depuis 2014) ; sur
quelles preuves (deux bulletins de Santé publique France, les séries du SIES et de la DEPP) ; et quelle question
s'ouvre (le test à âge égal, qui n'a jamais été publié). Outil réutilisable : la grille « fait → mécanisme →
concordance → ce qui l'invaliderait → conclusion limitée », appliquée aux six maillons dans un encadré.

### Singularité

Cette page existe parce qu'elle confronte le malaise des étudiants à celui des autres jeunes et distingue trois mesures
qui n'évoluent pas ensemble, ce que le lecteur ne découvre pas dans les publications de l'OVE (étudiants seulement, vagues
présentées à la suite), dans le bulletin de Santé publique France (statuts comparés sans lecture étudiante ni réserve
d'âge mise en avant) ni dans le débat public, qui oppose le récit de l'université abandonnée à celui de la génération
des écrans sans tester ni l'un ni l'autre (lus : synthèse MESR des enquêtes OVE, BEH 2023 n° 2 et 2025 n° 14, fiche SIES
n° 16, débat Haidt-Odgers par sources secondaires — **la revue de presse et des rapports militants reste à faire** avant
de figer cette phrase).

### Raccords

- **Retenu — le livre *La Société du premier coup*** (`appel-livre slug="la-societe-du-premier-coup"`, `avis="non"`,
  surtitre vrai) : « Ce qu'une année ratée coûte dépend de qui la rate : le livre mesure combien de tentatives une
  trajectoire autorise réellement. » Relation : le maillon des perspectives et l'anxiété de la performance renvoient à
  ce qu'un échec d'études ferme ou non ; la page **ne teste pas** cette lecture, elle l'ouvre. Même livre que les deux
  pages voisines (professeurs, niveau) : continuité du bloc.
- **Retenu — le working paper AWP-08, « La réversibilité sociale comme dimension de l'inégalité »**, et la notion
  `/reversibilite-sociale/` : dans le bloc séparé de l'hypothèse de l'auteur, présenté comme cadre réfutable non testé
  ici (« Une hypothèse de l'auteur, non testée sur ces données : … »).
- **Retenu — pages voisines** : `/le-niveau-des-eleves-baisse-t-il/` (le lecteur qui demande si les étudiants vont plus
  mal demande aussi s'ils arrivent moins bien préparés ; une phrase dans la partie « histoire », sans en tirer de
  cause) ; `/manque-t-il-des-professeurs/` (moyens du lycée contre moyens du supérieur : même distinction entre dépense
  totale et dépense par élève). Barre du bloc automatique (`ressource.bloc: ecole`).
- **Écartée — la définition de l'anthropie** : aucune application du concept n'est démontrée par cette page ; le lien
  documentaire passe, s'il y a lieu, par le gabarit du bloc d'hypothèse (`canonical-definition`), et rien n'est ajouté à
  « Quelques domaines d'application ».
- **Écartées — les pages de la dette** : la dépense par étudiant n'y est pas traitée ; un lien ne s'y justifierait que
  par la densité.

## Fiche D0

Résultat visé, au plus près de la finalité : que la page soit citée ou reprise comme la référence qui distingue étudiants
et autres jeunes (crédibilité de l'auteur sur l'éducation) et qu'elle ouvre la demande du test à âge égal ; diagnostics :
impressions et clics Search Console sur les requêtes « santé mentale étudiants », « malaise étudiant », « détresse
psychologique étudiants » ; citations par des moteurs de réponse (relevé VEILLE_GEO) ; reprises. État initial : page
inexistante au 23/10/2026, aucune impression. Relevés : J+30 et J+60 après publication. **À inscrire dans
`D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` avant publication** (non fait à ce jour : la page n'existe pas).

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait le 23/10 — retenus : MCP `sources` (séries Insee, OCDE),
  vérificateur de références (articles du BEH, *PNAS Nexus*, *Lancet*), `check_langue.py`, recette, panel, MAGNIFIER en
  finition.
- Forme et rattachement : fait le 23/10 — bloc `ecole`, élargi en « École, lycée et université » sur décision de
  l'auteur (en ligne, commit du site `c6e4b01`).
- Contre-expertise de phase A : faite et arbitrée le 23/10 (`PRO-20261023-180856`, audit fermé).
- Protocole du type : non fait — lectures à faire avant le texte : figure 3 du BEH 2023 (PDF) ; EnCLASS ; série DEPP des
  bacheliers par génération ; tableau rétrospectif du SIES n° 19 ; chômage des 15-24 ans (Insee, série longue) ;
  enquête OVE 2024 (champ, sélection des répondants) ; Castelo et al. 2025 (durée, effectif) ; revue de presse.
- Test décisif (figure 3 du BEH) : non fait.
- Scénarios d'architecture : non fait — deux à écrire : B+A retenu par l'arbitrage (constat → témoin → histoire →
  ruptures depuis 2020 → explications disputées → ce qui reste à établir, six maillons en encadré) ; A pur (la chaîne
  maillon par maillon). Un troisième si la lecture d'EnCLASS le justifie (« le malaise commence au lycée »).
- Panel avant : non fait (page nouvelle dont la réception décide du choix d'architecture : à faire sur les scénarios).
- Gardes vues mordre : non fait (générateur à écrire).
- Figures téléphone : non fait.
- Relecture de langue : non fait.
- Recette 320-1280 (`recette.py`) : non fait.
- Panel après : non fait.
- Gate éditorial : non fait.
- Relecture phrase à phrase : non fait (FR seulement, exclusion déclarée de l'EN).
- Instantané de relecture : non fait.
- Contre-expertise de la page : non faite.
- Accord de l'auteur : non donné — deux décisions en attente : demander ou non la tabulation à Santé publique France ou
  l'accès aux microdonnées ; accepter que la découverte principale contredise la note reçue.
