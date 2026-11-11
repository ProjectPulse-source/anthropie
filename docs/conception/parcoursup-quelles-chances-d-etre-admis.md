# Fiche de conception — Parcoursup : quelles sont vraiment vos chances d'être admis ?

Page : `/parcoursup-quelles-chances-d-etre-admis/` (FR) · pas de version anglaise (exclusion déclarée : procédure
française, bloc « École, lycée et université » français seulement ; onglet EN `lang_repli: "/en/resources/"`, comme les
pages voisines) · ouverte le 2026-11-10, **refondue le même jour** après que le critère de sortie a joué (arbitrage de
la pièce 03) ; **écrite avant tout texte de la page**.

Chantier : `D:\PRO\06_PROMOTION\RECHERCHE_RESSOURCE_UNIVERSITE_2026-11-03\`. Arbitrages qui font foi : pièce 01
(choix de la ressource, `0fd9b703…1691`), pièce 02 (périmètres, `8bcb0978…811e`), pièce 03 (critère de sortie joué,
`1db971c2…ed40`), pièce 04 (scénarios, `814531b5…147b`), pièce 05 (fiche refondue, `8b5fbb66…c2c5`). Version précédente de cette fiche (angle « trois mesures d'une formation ») archivée dans le chantier :
`FICHE_A_V1_trois-mesures_2026-11-10_ARCHIVE.md`. Page A du programme ; la page B (« Une première année ratée est-elle
une année perdue ? ») est une ressource distincte, ouverte après celle-ci.

Titre conservé (proche de la requête réelle, arbitrage 01) ; la question que la page tranche est plus précise : elle
est ci-dessous.

## Forme

`quantitatif`. La page apprend à lire la fiche officielle d'une formation et éprouve sur trois sessions les règles de
lecture qu'on en tire. Elle ne démontre aucun mécanisme causal.

Critères `quantitatif`, un par ligne :
- définitions : candidat, candidat classé, « en position de recevoir une proposition » (fiche : « ont pu recevoir une
  proposition »), proposition, admis, taux d'accès, taux d'accès par type de bac (fiche seulement), répartition par bac
  des appelables (données ouvertes seulement) — chacune citée à sa source (méthodologie 2025, fiche de la plateforme) ;
- périmètres et millésimes : sessions 2023, 2024, 2025 (jeux `fr-esr-parcoursup_2023`, `_2024`, `fr-esr-parcoursup`),
  2026 quand le jeu paraît ; appariement des formations par `cod_aff_form` **et** intitulé identique ; formations sans
  taux d'accès écartées avec motif (2025 : 15, aucun candidat en phase principale) ; apprentissage hors du jeu ;
- unités : un taux d'accès est en points de pourcentage ; une variation d'une session à l'autre s'écrit en points,
  jamais en pourcentage ; un vœu n'est pas une personne (1 046 000 candidats en 2026 se citent depuis le bilan officiel) ;
- dénominateurs : taux d'accès sur les candidats scolarisés en France ou européens ayant confirmé un vœu en phase
  principale ; effectifs des données ouvertes sur tous les candidats, toutes phases ; fiche de la plateforme arrêtée à
  la fin de la phase principale (mi-juillet), données ouvertes au 10 septembre — jamais mêlés sans le dire ;
- reproductibilité : le taux d'accès n'est pas recalculable (méthodologie 2025, p. 3) ; la page le **reprend** et calcule
  à partir de lui sa variation d'une session à l'autre (`scripts/update_parcoursup.py`, jeu `parcoursup`, à écrire),
  avec conservation des lignes (entrées = appariées + écartées, motif nommé) ;
- changements de série : calcul modifié en 2022 (Boyer et Gossa, 2024) ; la série commence donc en 2023. Méthodologies
  2023 (`f8a25c1a…6750`), 2024 (`61f317ba…0098`) et 2025 lues le 10/11 : même définition, et chacune précise « le mode
  de calcul de ces indicateurs est identique à celui de l'année dernière » ; la mention explicite des candidats en
  réorientation et en reprise d'études apparaît en 2024, sans changement de calcul déclaré. La définition se relit à
  chaque session ; une session de hausse générale des candidats se signale.

## Fiche de conception

### Question centrale

Jusqu'où peut-on se fier au taux d'accès d'une formation pour choisir ses vœux ?

### Enjeu

Plus d'un million de candidats (1 046 000 en 2026, bilan officiel) composent dix vœux entre « ambitieux », « réalistes »
et « de sécurité », sur un chiffre : le taux d'accès de l'année précédente. La plateforme le publie avec soin (fiche de
chaque formation : cascade, taux par type de bac, possibilités selon la série et la moyenne) ; les conseils qui en
dérivent sont plus rapides — « au-dessus de 90 %, c'est réaliste » (Onisep), « le taux d'accès est la part des
candidats qui ont reçu une proposition » (moyenne.org), « si peu d'élèves de ma série sont recrutés, c'est ambitieux »
(Onisep). Une erreur coûte le plus là où on la voit le moins : sur le vœu de sécurité, celui qui doit tenir quand les
autres tombent. Contexte : mobilisation lycéenne d'octobre 2026 contre Parcoursup, mesures du gouvernement le 26/10
(L'Étudiant, 28/10) ; carte des formations 2027 le 17/12/2026, vœux du 18/01 au 11/03/2027 (calendrier officiel lu).

### Croyance initiale

Deux lectures opposées. La lecture rassurante : un taux d'accès élevé l'an dernier fait un vœu sûr cette année. La
lecture désenchantée : avec dix vœux pour une place, les chiffres ne disent rien et Parcoursup est une loterie. La
première fiche de cette page en portait une troisième, réfutée par la plateforme elle-même : que le candidat ne voit pas
les mesures côte à côte (la fiche les déroule pas à pas).

### Découverte principale

**Exploratoire, à reproduire par le générateur** (calculs du 10/11/2026 ; exports 2023 `f0a8b6b0…cf5`, 2024
`7215f6c4…9c54`, 2025 `0a5a95ab…4b04` ; règles : `PROTOCOLE_QUANTITATIF_PAGE_A_2026-11-10.md` du chantier ;
appariées 12 065 sur 14 616 en 2023-2024, 12 816 sur 14 791 en 2024-2025, écartées avec motif, dont 23 formations
« aucun classé » — taux 0 % en 2025, vide en 2024 : même objet, deux codages ; arbitrage de la pièce 04).
Ce qui suit **décrit une dispersion passée**, jamais une prévision.

1. **Les taux d'accès présentent une forte stabilité relative d'une année à l'autre** : corrélation de 0,90 entre 2023
   et 2024 et de 0,87 entre 2024 et 2025, identique en rangs (Spearman) et à peine moindre sans les formations à 0 ou
   100 % (0,88 et 0,85) ; variation absolue médiane de 6 points les deux fois. Les formations les moins accessibles
   tendent à le rester, mais certaines connaissent des variations importantes. Cette stabilité porte sur les
   formations ; elle ne garantit rien sur l'issue d'une candidature ni ne dit rien de l'équité des décisions.
2. **Un taux d'accès décrit une année passée, pas l'année suivante.** Taux de l'année suivante, du 1er au 9e décile, selon la tranche de
   l'année (2023 → 2024 ; 2024 → 2025) : 40-60 % → 34-70 % ; 32-67 % · 60-75 % → 48-85 % ; 43-83 % · 75-90 % → 58-95 % ;
   49-92 % · 90-99 % → 76-100 % ; 59-100 % · 100 % → 91-100 % ; 80-100 %. **Validation hors échantillon** : les bornes
   de 2023-2024 ont couvert de 73 % (tranche 75-90 %) à 85 % (tranche 100 %) des formations en 2024-2025, pour 80 %
   attendus par construction.
3. **Au-dessus de 90 %, le conseil courant tient le plus souvent.** Tranche 90-99 % : restent à 90 % ou plus 66,9 %
   (1 138 sur 1 701) puis 55,2 % (936 sur 1 695) ; perdent 20 points ou plus 10,1 % (172) puis 21,7 % (367).
   Tranche 100 % : restent à 90 % ou plus 91,1 % puis 85,3 % ; perdent 20 points ou plus 3,6 % puis 10,4 %. En perte
   relative (un cinquième du niveau), ces deux tranches sont les plus stables. Les formations très sélectives restent
   sélectives : sous 20 % une année, 17 sur 1 116 puis 20 sur 1 246 dépassent 40 % l'année suivante.
4. **Certaines filières connaissent des variations que la moyenne générale masque.** Variation médiane 2024-2025 :
   CPGE −11 points (974 formations ; candidats médians 993,5 → 940,5, places 45 → 45), BTS −3, licence 0 ; 2023-2024 :
   de −3 à +1. Les baisses de 20 points ou plus ont environ doublé entre les deux transitions dans les tranches de 40 à
   99 %, et restent plus fréquentes après correction par filière (tranche 75-90 % : 20,0 % contre 13,7 %). En CPGE, le
   classement des formations lui-même se recompose : corrélation de 0,93 puis 0,75 (licence : 0,94 puis 0,95). Constat
   descriptif, aucune cause avancée.
5. **Les petites formations n'expliquent pas l'instabilité** : sans les formations de moins de 50 candidats, les
   proportions bougent de moins d'un point, sauf à 100 % (baisses de 20 points ou plus en 2024-2025 : 10,8 % → 6,0 %).
6. **La chance par type de bac n'existe que sur la fiche.** La plateforme affiche un taux d'accès par bac (Illkirch,
   bac général : 23 %) ; le fichier ouvert ne publie qu'une répartition des appelables par bac (vérifié, méthodologie
   p. 3), qui ne permet pas de le retrouver. Les outils bâtis sur le fichier ouvert lisent donc une composition comme une
   chance ; l'activité de l'Onisep fait le même glissement avec la part des admis d'une série.

**Hypothèse de la version précédente, réfutée par le test décisif** (10/11) : « le taux est le moins fiable là où l'on
cherche la sécurité ». En perte relative, c'est l'inverse ; en points, la tranche 90-99 % décroche moins que la tranche
75-90 %.

### Mécanisme explicatif

Non causal : mécanique d'un indicateur. Le taux d'accès compte, parmi les candidats d'une session, ceux dont le rang ne
dépassait pas celui du dernier appelé. Il dépend des places, du nombre de candidats et de leurs autres vœux — trois
grandeurs qui changent d'une année à l'autre, en partie ensemble pour toute une filière (CPGE en 2025). Une formation à
100 % n'avait plus aucun candidat du champ en attente à la fin de la phase principale : son taux baisse dès que
l'appel ne va plus jusqu'au dernier classé, ce qui peut tenir à la demande, aux places, au classement, aux groupes
d'appel ou aux renoncements. Une formation de milieu de
tableau appelle une part d'une liste dont la longueur varie : c'est elle qui bouge le plus. Les données agrégées ne
séparent pas les parts des places, des candidatures et des désistements ; la hausse des candidats en 2025 est
compatible avec la baisse générale, sans la prouver. Ce que la page ne fait pas : prédire l'admission d'un dossier, ni
le taux de 2027.

### Preuve décisive

1. Jeux ouverts 2023, 2024, 2025 : taux d'accès publiés, appariés par formation (preuve des points 1 à 5).
2. Méthodologie open data 2025 (PDF de 42 pages, `95904fc5…d879`), lue en entier : définitions, champ France et
   Europe, non-recalculabilité, répartition par bac (point 6).
3. Fiche Parcoursup d'une formation (Illkirch, `g_ta_cod=7970`), lue par navigateur le 10/11 : cascade, taux d'accès
   par bac et sa définition affichée, possibilités par série et moyenne sur trois ans.
4. Activité de l'Onisep « Évaluer son niveau d'ambition dans MonProjetSup », lue par navigateur le 10/11 (les trois
   règles de lecture citées dans l'Enjeu).
5. **Témoin** : la série longue (trois sessions) contre l'année unique que montre la fiche ; et la contre-population
   des formations très sélectives, où la règle « le chiffre de l'an dernier vaut cette année » devrait tenir et tient.

**Test décisif — fait le 10/11/2026**, sur les mêmes exports : (a) effet plafond neutralisé, en perte relative (au moins
un cinquième du niveau) et en points par tranche ; (b) formations de moins de 50 candidats retirées ; (c) variation
corrigée de la médiane de la filière. Résultat : sous (a), l'hypothèse « le vœu sûr est le moins fiable » **tombe**
(points 2 et 3 réécrits) ; (b) ne change presque rien (point 5) ; (c) réduit l'écart entre 2024 et 2025 sans l'annuler
(point 4). Ce qui survit : la stabilité d'ensemble, la fourchette par tranche, l'effet d'année par filière.

### Pouvoir discriminant

- **Explications rivales réellement soutenues** : (1) « au-dessus de 90 %, le vœu est réaliste » (Onisep, activité
  pour les terminales) ; (2) « les chiffres ne disent rien, c'est une loterie » (lecture courante dans le débat de 2026) ;
  (3) « le taux d'accès est la part qui a reçu une proposition » (moyenne.org) ; (4) « peu d'admis de ma série, donc
  vœu ambitieux » (Onisep). Le témoin ne change qu'une chose : la session (2023 → 2024 → 2025), sur les mêmes
  formations.
- **Ce que révèle la figure qu'une série isolée ne montre pas** : pour chaque tranche de taux une année, la fourchette
  du taux l'année suivante ; la fiche officielle ne montre qu'une année.
- **Explications départagées** : (2) est contredite pour les formations (forte stabilité relative, corrélation 0,87 à
  0,90, en valeurs comme en rangs), sans rien dire d'un dossier ; (1) est **confirmée le plus souvent** et
  bornée (une formation sur dix à une sur cinq de la tranche 90-99 % perd 20 points ou plus) ; (3) est corrigée par la
  définition officielle ; (4) est reconnue comme une composition, la chance par bac se lisant à l'étape 2 de la fiche.
- **Robustesse** : deux paires de sessions, dont une sans baisse générale ; effet plafond, petites formations,
  correction par filière (test décisif, 10/11, exploratoire). Reste : trois sessions d'affilée pour une même formation
  (la fiche officielle calcule ses possibilités sur trois ans).
- **Levier ou risque éclairé** : lire le taux de l'an dernier comme une photographie d'une année, dont on connaît la
  dispersion l'année suivante ; un taux élevé est généralement un indice favorable, jamais une garantie, même à 100 % ;
  la page ne démontre aucune stratégie de vœux (la diversification se cite comme recommandation de la plateforme) ;
  chercher les chiffres de son profil (taux par bac, possibilités par série) sur la fiche, pas sur un site qui reprend le
  fichier ouvert — aucun n'est une probabilité individuelle ; ne pas renoncer à un vœu
  sélectif sur un rapport admis / candidats.
- **Critère de sortie** : la page apporte-t-elle ce que la fiche officielle et l'Onisep ne donnent pas ? Ce qu'elle seule
  donne : la dispersion du taux l'année suivante pour chaque tranche, avec sa validation hors échantillon, sur toutes les formations, et l'effet d'année
  par filière. Si un travail publié l'a déjà fait (recherche du 10/11, § Singularité), la page ne sort pas sous cette
  forme.

### Limite

- Aucune prédiction pour un dossier ni pour 2027 : trois sessions décrivent une variabilité passée.
- Le taux d'accès est repris, pas recalculé ; son champ (France et Europe) n'est pas celui des effectifs.
- Trois sessions seulement, dont une de baisse générale ; les causes de la variation (places, candidats, autres vœux)
  ne se séparent pas dans des données agrégées.
- Une variation de taux n'est pas un échec de candidats : une formation à 80 % appelle encore quatre candidats sur cinq.
- L'accès n'est pas la réussite : rien ici sur ce que deviennent les admis (page B).
- Formations appariées par code et intitulé : une formation renommée ou recodée sort de l'appariement (écartées
  comptées et motivées par le générateur). Les écartées sont plus petites et plus accessibles que les appariées (taux
  médian 66 à 78 % contre 60 %), et les renommages de 2025 touchent surtout des BTS : les résultats portent sur les
  formations restées identiques (test de sélection, 11/11, arbitrage de la pièce 05).

### Valeur finale

Après lecture, le candidat ou le parent sait quels chiffres correspondent le mieux à son profil (fiche de la formation, étapes 2 et 3, son bac et sa
série) et quelle fourchette donner au taux de l'an dernier ; il sait que le conseil « au-dessus de 90 %, c'est
réaliste » tient le plus souvent, et quand il échoue. Le professeur principal dispose d'un tableau des fourchettes par
tranche et par filière, recalculé et téléchargeable. Outil réutilisable : « ce chiffre de l'an dernier, quelle
fourchette l'année suivante ? », applicable à Mon Master et à tout indicateur d'admission.

### Singularité

Cette page existe parce qu'elle éprouve, sur toutes les formations et trois sessions, les règles de lecture qu'on tire
du taux d'accès, et montre comment le taux de l'an dernier a évolué l'année suivante, tranche par tranche. **Lu le 10/11** : la fiche de la
plateforme montre la cascade, le taux par bac et les possibilités par série et moyenne, pour une formation et une
année ; l'Onisep propose une activité qui classe les vœux par le taux (« taux d'admission » supérieur à 90 % :
« réaliste ») ; moyenne.org publie les médianes par filière et une définition inexacte ; OuiSup affiche les 14 252
formations sans définir le taux. Aucune de ces sources ne compare le taux d'une formation d'une année sur l'autre.
**Recherche de travaux antérieurs, 10/11/2026** (environ 25 requêtes en français et en anglais, lectures ci-dessous ;
non exhaustive : ni HAL ni Google Scholar interrogés directement) : **à notre connaissance, les publications consultées
ne proposent pas cette mesure d'ensemble de la stabilité des taux d'accès par tranche, entre sessions successives, avec
vérification sur une seconde transition.** Les plus proches, lus : Boyer et Gossa, « Si Parcoursup
m'était compté », *Éducation et Socialisation* n° 72 (2024), qui jugent l'indicateur « peu fiable et très peu
comparable » et renoncent à le suivre dans le temps (calcul changé en 2022) ; ParcoursData, qui affiche l'historique
d'une formation sans analyse d'ensemble ; Parcoursioux, qui affirme que le taux « se compare d'une année à l'autre »
sans le mesurer ; un notebook de cours (teachpyx, sessions 2021-2025) qui ne compare pas le taux. Signalent la
variabilité sans la chiffrer : le 8e rapport du comité éthique et scientifique de Parcoursup (avril 2026, p. 23-24 :
des « résultats des années passées », « moins complètes pour les formations à petite capacité ») ; Fox'Up, Digischool,
France-Jeunes. L'Étudiant (16/01/2026) conseille d'analyser le taux de l'année précédente sans mise en garde.
La page fait cette mesure sur une période de calcul homogène, ce qui répond en partie à la réserve de Boyer et Gossa
sur la comparabilité : sur 2023-2025, le taux d'une formation est stable en général (corrélation 0,87 à 0,90), avec des
filières où il l'est moins.

### Raccords

- **Retenu — la page enseignants `/enseignants/ecole-et-parcours/`** (activité « Après une première année de licence »,
  générateur `scripts/generer_parcours_licence.py`) : « Ce que devient un étudiant une fois admis en licence : l'activité
  le suit sur les données du SIES. » Relation : l'accès ici, la suite là-bas ; et l'activité de l'Onisep a désormais un
  pendant chiffré à proposer aux professeurs principaux.
- **Retenu sous réserve — le livre *La Société du premier coup*** (`appel-livre`, `avis="non"`) : « Ce qu'un premier
  choix engage dépend de ce qu'il permet de rattraper : c'est la question du livre. » Le vœu de sécurité est un
  dispositif de rattrapage ; le raccord se rejuge au gate (circulation).
- **Différé — la page B** et le working paper AWP-08 (réversibilité sociale) : la seconde chance après l'admission ;
  le lien se pose quand B existe.
- **Écartée — la définition de l'anthropie** : aucune application démontrée par une page de lecture d'indicateurs.
- **Écartées — `/les-etudiants-vont-ils-plus-mal/`, `/manque-t-il-des-professeurs/`** : même bloc (barre automatique),
  aucune relation intellectuelle propre à justifier un lien dans le texte.

## Fiche D0

Résultat visé, au plus près de la finalité : que la page soit reprise par des professeurs principaux, des journalistes
d'éducation ou des moteurs de réponse comme la référence sur la lecture du taux d'accès (crédibilité de l'auteur sur
l'éducation ; découverte du site par des familles concernées par la question du premier choix). Diagnostics :
impressions et clics Search Console sur « taux d'accès parcoursup », « taux d'accès parcoursup signification »,
« parcoursup taux d'accès ou taux d'admission », « chances parcoursup », « vœu de sécurité parcoursup » (hiérarchie à
mesurer, hypothèse de la pièce 03) ; citations par les moteurs de réponse (relevé VEILLE_GEO) ; reprises. État initial :
page inexistante au 10/11/2026, aucune impression. Relevés : J+30 et J+60 après publication, puis au 11/03/2027 (fin des
vœux). **À inscrire dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` avant publication** (non fait :
la page n'existe pas).

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait (10/11/2026, sortie lue : méthode des ressources, MAGNIFIER,
  séries publiques, vérificateur de références, relecture de langue, recette, panel).
- Faisabilité des données, méthodologie 2025 lue en entier, périmètres (pièce 02) : fait (10/11/2026).
- Lecture des outils institutionnels : fait (10/11/2026 : fiche Parcoursup d'Illkirch, Onisep, moyenne.org, OuiSup,
  calendrier officiel, L'Étudiant). Critère de sortie joué sur le premier angle (pièce 03).
- Refonte sur l'angle « stabilité du taux d'accès » : fait (10/11/2026, cette fiche ; calculs exploratoires 2023-2025).
- Test décisif (effet plafond, petites formations, baisse générale) : fait (10/11/2026) ; l'hypothèse « le vœu sûr est
  le moins fiable » tombe ; découverte réécrite (fourchette, accord avec le conseil courant, effet d'année).
- Recherche de travaux antérieurs sur la stabilité du taux : fait (10/11/2026, § Singularité) ; aucun travail ne la
  mesure sous cette forme (formulation « à notre connaissance », pièce 05) ; homogénéité du calcul 2023-2025 vérifiée dans les trois méthodologies. Critère de sortie : passé.
  Reste non lu : Cour des comptes 2020, rapports du comité 2021-2025 (extraits sans comparaison pluriannuelle).
- Scénarios d'architecture : fait (10/11/2026,
  `06_PROMOTION\RECHERCHE_RESSOURCE_UNIVERSITE_2026-11-03\SCENARIOS_ARCHITECTURE_PAGE_A_2026-11-10.md`) — A « anatomie
  d'un chiffre » écarté (redit la fiche officielle), B « trois conseils à l'épreuve », C « composer ses vœux » ;
  **retenu C+** (décision du candidat, avec les épreuves de B) ; deux figures (fourchette, effet d'année) ; pas de
  contre-expertise du plan (R4).
- Panel avant : à faire (page d'entrée d'un volet neuf) ; critère de réussite repris de la pièce 03 : cinq profils
  (lycéens général, technologique, professionnel, parent, professeur principal) répondent juste à « 8,5 % d'admis par
  candidat, est-ce 8,5 % de chances ? » et « 89 % des appelables ont un bac général, est-ce que 89 % des bacheliers
  généraux étaient appelables ? », plus une question sur la stabilité du taux ; deux phrases d'ouverture en
  concurrence (pièce 05).
- Contre-expertises : pièces 02 et 03 (fiche), 04 (scénarios : C+ resserré en six mouvements, trois P0 traités dont un
  défaut de codage trouvé et corrigé) arbitrées le 10/11 ; 05 (fiche refondue : trois formulations corrigées, témoin
  Spearman, corrélation par filière, test de sélection de l'appariement) arbitrée le 11/11 ; la prochaine porte sur la
  page.
- Protocole `quantitatif` : fait (10/11/2026, `PROTOCOLE_QUANTITATIF_PAGE_A_2026-11-10.md` du chantier ; sept gardes).
- Test sur de vrais lecteurs (pièce 04) : décision de l'auteur requise ; le panel simulé ne vaut que diagnostic.
- Relecture contre les fiches 2027 à l'ouverture de la carte (17/12/2026) : à faire avant publication.
- Générateur, gardes vues mordre, figures téléphone : non fait.
- Relecture de langue, recette 320-1280, panel après, gate éditorial, relecture phrase à phrase, instantané,
  contre-expertise de la page, accord de l'auteur : non fait.
