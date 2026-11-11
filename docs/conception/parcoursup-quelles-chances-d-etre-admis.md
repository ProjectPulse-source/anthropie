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
  à partir de lui sa variation d'une session à l'autre (`scripts/update_parcoursup.py`, jeu `parcoursup`, écrit le
  11/11/2026), avec conservation des lignes (entrées = appariées + écartées, motif nommé) ;
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
Contre-population et sensibilités (points 3 à 5) recalculées le 11/11 sur les formations appariées après ce nettoyage
(`outils_exploratoires\p06.py` du chantier) : trois nombres dataient d'avant lui et sont corrigés ci-dessous.
Ce qui suit **décrit une dispersion passée**, jamais une prévision.

1. **Les taux d'accès présentent une forte stabilité relative d'une année à l'autre** : corrélation de 0,90 entre 2023
   et 2024 et de 0,87 entre 2024 et 2025, identique en rangs (Spearman) et à peine moindre sans les formations à 0 ou
   100 % (0,88 et 0,85) ; variation absolue médiane de 6 points les deux fois. Les formations les moins accessibles
   tendent à le rester, mais certaines connaissent des variations importantes. Cette stabilité porte sur les
   formations ; elle ne garantit rien sur l'issue d'une candidature ni ne dit rien de l'équité des décisions.
2. **Un taux d'accès décrit une année passée, pas l'année suivante.** Taux de l'année suivante, du 1er au 9e décile, selon la tranche de
   l'année (2023 → 2024 ; 2024 → 2025) : 40-60 % → 34-70 % ; 32-67 % · 60-75 % → 48-85 % ; 43-83 % · 75-90 % → 58-95 % ;
   49-92 % · 90-99 % → 76-100 % ; 59-100 % · 100 % → 91-100 % ; 80-100 %. **Validation hors échantillon** : les bornes
   de 2023-2024 ont couvert de 73 % (tranche 75-90 %) à 85 % (tranche 100 %) des formations en 2024-2025. Repère
   (corrigé le 11/11 : « 80 % attendus » était faux pour deux tranches) : dans leur propre transition, ces bornes
   contenaient 80 à 83 % des formations des tranches inférieures à 90 %, et 90 % de celles des tranches 90-99 % et
   100 %, où le 9e décile bute sur 100 %. L'écart est le plus grand dans la tranche 90-99 % (90,0 % puis 77,4 %).
3. **Le seuil de 90 % garde une valeur de repère et ne garantit rien** (formulation du 11/11 après la pièce 08 : les
   données mesurent la tenue du seuil par des formations, pas le réalisme d'un vœu pour un candidat ; « le conseil
   tient » validait ce qui n'est pas testé). Tranche 90-99 % : restent à 90 % ou plus 66,9 %
   (1 138 sur 1 701) puis 55,2 % (936 sur 1 695) ; perdent 20 points ou plus 10,1 % (172) puis 21,7 % (367).
   Tranche 100 % : restent à 90 % ou plus 91,1 % puis 85,3 % ; perdent 20 points ou plus 3,6 % puis 10,4 %. En perte
   relative (un cinquième du niveau), ces deux tranches sont les plus stables. Les formations très sélectives restent
   sélectives : sous 20 % une année, 17 sur 1 116 puis 20 sur 1 239 atteignent 40 % ou plus l'année suivante.
4. **Certaines filières connaissent des variations que la moyenne générale masque.** Variation médiane 2024-2025 :
   CPGE −11 points (974 formations ; candidats médians 993,5 → 940,5, places 45 → 45), BTS −3, licence 0 ; 2023-2024 :
   de −3 à +1. Les baisses de 20 points ou plus sont 1,5 à 2,1 fois plus fréquentes dans la seconde transition, de la
   tranche 40-60 % à la tranche 90-99 % ; au-dessus de 60 %, elles le restent après correction par filière (tranche
   75-90 % : 19,9 % contre 13,7 %). En CPGE, le
   classement des formations lui-même se recompose : corrélation de 0,93 puis 0,75 (licence : 0,94 les deux fois ;
   « 0,95 » venait d'un double arrondi de 0,9445). Constat
   descriptif, aucune cause avancée.
5. **Les petites formations n'expliquent pas l'instabilité** : sans les formations de moins de 50 candidats, les
   proportions bougent de moins d'un point, sauf à 100 % (baisses de 20 points ou plus en 2024-2025 : 10,4 % → 5,9 %).
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
  0,90, en valeurs comme en rangs), sans rien dire d'un dossier ; (1) n'est pas testée comme conseil (le
  réalisme d'un vœu dépend aussi du dossier) ; la tenue du seuil, elle, est mesurée : elle vaut pour plus d'une formation
  sur deux, et elle est
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
  comptées et motivées par le générateur). Les formations disparues ou renommées sont plus petites et plus accessibles
  que les appariées (taux médian 66 à 78 % contre 60 %) ; les nouvelles formations de 2025 ne le sont pas (54 %) ; les
  renommages de 2025 touchent surtout des BTS : les résultats portent sur les formations restées identiques (test de
  sélection, 11/11, arbitrage de la pièce 05 ; formule précisée le 11/11 en écrivant la garde).

### Valeur finale

Après lecture, le candidat ou le parent sait quels chiffres correspondent le mieux à son profil (fiche de la formation, étapes 2 et 3, son bac et sa
série) et quelle fourchette donner au taux de l'an dernier ; il sait ce que le seuil de 90 % a garanti et n'a pas garanti d'une année à l'autre. Le professeur principal dispose d'un tableau des fourchettes par
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
vœux). **Inscrite dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` le 11/11/2026** (avant
publication, page écrite et non publiée).

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
- Panel avant : fait (11/11/2026, `06_PROMOTION\RECHERCHE_RESSOURCE_UNIVERSITE_2026-11-03\PANEL_AVANT_2026-11-11\DIAGNOSTIC.md` ;
  pré-inscription écrite avant lancement ; cinq profils de la pièce 03, vingt lectures simulées isolées sur une
  maquette du plan, dont un tour de contrôle). Résultats : (1) le critère de la pièce 03 **n'est pas évaluable en
  simulation** — cinq témoins répondent juste aux trois questions sans avoir rien lu ; (2) ouverture « question
  d'abord », phrase de résultat sous la figure 1 (le panel ne départage pas au seuil fixé, le modèle de page tranche) ;
  (3) huit changements au plan, dont la stabilité chiffrée (une formation sur deux varie de 6 points ou moins) et le
  bloc par filière adressé au lecteur — plan à suivre : section finale du document des scénarios ; (4) **décision de
  l'auteur requise sur la promesse du titre** : neuf lecteurs sur dix, puis trois sur cinq après correction du plan,
  demandent comment composer leur liste, ce que la page ne démontre pas. Hypothèses de réception, pas preuve de
  compréhension.
- Contre-expertises : pièces 02 et 03 (fiche), 04 (scénarios : C+ resserré en six mouvements, trois P0 traités dont un
  défaut de codage trouvé et corrigé) arbitrées le 10/11 ; 05 (fiche refondue : trois formulations corrigées, témoin
  Spearman, corrélation par filière, test de sélection de l'appariement) arbitrée le 11/11 ; la prochaine porte sur la
  page.
- Protocole `quantitatif` : fait (10/11/2026, `PROTOCOLE_QUANTITATIF_PAGE_A_2026-11-10.md` du chantier ; neuf gardes ;
  complété le 11/11 : contre-population, stabilité en langage courant, parts par filière, fractions en lettres, témoin
  `p06.py`).
- Test sur de vrais lecteurs (pièces 04, 06 et 08) : non fait (auteur, 11/11/2026 : pas de lecteur réel disponible
  dans l'immédiat) ; protocole prêt ; le panel simulé ne vaut que diagnostic, la compréhension n'est pas mesurée.
- Relecture contre les fiches 2027 à l'ouverture de la carte (17/12/2026) : non fait, à faire ce jour-là (la page est
  publiée avant, sur décision de l'auteur du 11/11/2026 ; elle date ses lectures de la fiche officielle des 10 et
  11 novembre 2026).
- Générateur, jetons, gardes : fait (11/11/2026) — `scripts/update_parcoursup.py` ; exports des trois sessions archivés
  dans `scripts/sources_parcoursup/` (manifeste, SHA256SUMS ; export 2023 retéléchargé complet, identique à l'archive du
  chantier sur les colonnes communes, 13 869 lignes) ; sorties `data/` et `static/parcoursup.json`,
  `static/parcoursup.csv` ; shortcode `psup-val` ; 733 jetons, portés par un rôle (transition précédente, dernière
  transition) et non par une année. 76 conditions de garde passées ; **32 mutations, chacune fait mordre la garde
  visée** (`--mutations` ; le banc répond « aucune garde » à une mutation sans effet) ; égalité avec le témoin
  indépendant (`temoin.json` : appariement de `p04b.py`, corrélations de `p05.py`, export 2023 d'origine) à 0,1 point.
  `check-all --ci` à 0, build à 0. Non fait : gardes 6 et 8 sur la page réelle (elle n'existe pas : vues mordre sur
  une page témoin) ; ligne au registre `data/sources_maj.json` (avec la page).
- Figures : fait (11/11/2026, skill `controle-figures`) — `parcoursup-tranches` (taux de l'année suivante par tranche :
  du 1er au 9e décile, médiane, deux transitions, bande de la tranche de départ) et `parcoursup-filieres` (variation
  médiane par filière), chacune en version bureau et téléphone, SVG et PNG, fiches « Réutiliser » lues dans le SVG
  (`data/figures_parcoursup.json`). Parité téléphone et cadre contrôlés par le générateur ; `check-figures.py` à 0. Deux
  contrôleurs indépendants en lecture seule : (a) géométrie et données — 154 marques reconverties, 280 nombres
  imprimés, recalcul complet depuis les CSV, aucun écart de tracé ; **un défaut de fond trouvé** : en 2024 seulement,
  162 formations paramédicales sont classées `IFSI` par le ministère, et la règle « filière de l'année d'arrivée »
  mêlait deux populations (ligne IFSI à 0 au lieu de +1) → règle changée : même filière les deux sessions, formations
  reclassées comptées à part (163 puis 172) ; (b) lecture du rendu — un défaut bloquant (la note de la figure 1 se
  lisait « huit formations sur dix ont un taux inférieur à 90 % ») et une vingtaine de défauts gênants ou
  cosmétiques, corrigés dans le générateur : note réécrite en exemple de lecture, libellés de tranche à bornes entières
  (« 60 à 74 % » : les tranches ne changent pas), en-têtes vrais pour les deux séries, valeurs au-dessus des barres,
  unité de la figure 2 (« points de pourcentage », « −11 points »), valeurs écartées de l'axe du zéro, versions
  téléphone resserrées. Second passage du contrôleur de géométrie sur l'état final : aucun défaut bloquant ni gênant
  nouveau, les onze filières et le groupe reclassé recalculés à l'unité près, 156 marques conformes ; cinq défauts
  cosmétiques, dont quatre corrigés (bande de la tranche 100 % retirée, lignes de la figure 2 espacées, bande au ras
  de la barre, exemple de la note présenté comme une illustration de l'unité) ; reste, déclaré : sur la ligne « 100 % »,
  médiane et 9e décile partagent une étiquette. Trois résumés d'une même baisse entrent au jeu et au témoin (classes
  préparatoires 2024-2025 : médiane des variations −11 points, moyenne −14,9, taux médian de 62 % à 43 %). Limites
  déclarées : franges de couleur du rendu PNG (propriété du rendu local, commune aux figures du site) ; la table de
  chasses de `check-figures.py` n'a pas la police Inter (le contrôleur a remesuré aux largeurs réelles : aucun
  chevauchement) ; second passage de lecture du rendu reporté après la contre-expertise externe, qui lit les figures.
- Contre-expertise externe des figures et des constats : fait (11/11/2026 ; paquet du sas
  `D:\CONTRE_EXPERTISE\2026-11-11_PARCOURSUP_FIGURES\`, réponse archivée avant lecture, pièce 06 ; arbitrage
  `06_PROMOTION\RECHERCHE_RESSOURCE_UNIVERSITE_2026-11-03\ARBITRAGE_PIECE_06_2026-11-11.md`). Verdict : deux figures
  gardées, pas de refonte. Vérifié à la source : empreintes du paquet conformes, notices du ministère (correction du
  16/01/2025 hors de nos colonnes ; calcul du taux déclaré inchangé de 2023 à 2025). Contrôles demandés, faits en
  exploratoire (`p07.py`) : le recul de 2024-2025 se retrouve sur les 11 087 formations appariées aux deux transitions,
  sans les classes préparatoires aussi ; apparier par le code seul ne déplace aucun repère de plus d'un point.
  Corrigé dans le générateur : clé de la figure 1 (« au moins huit formations sur dix », gardé ; bande « tranche de
  départ, placée sur le même axe »), gris des séries secondaires (`#8a8781`, 3,58 pour 1), parts en baisse, en hausse
  et inchangées de l'ensemble (jeu, CSV, jetons, témoin), « le plus souvent » et « personne ne peut calculer » retirés
  par la garde 8, garde 4 durcie (une clé absente du témoin arrête). 81 conditions de garde, 741 jetons, 35 mutations
  sur 35.
- Second contrôle des figures, après correction : fait (11/11/2026) — géométrie et données, 152 marques reconverties
  et 338 nombres imprimés sans écart, contrôle vu mordre sur vingt mutations ; lecture du rendu, deux passages
  indépendants, aucun défaut bloquant, formulations corrigées (clés, notes, bande prolongée, « formations comparées »,
  formations reclassées dites non dessinées). `check-figures.py`, `check-all --ci` et build à 0. Non fait : relecture
  indépendante des toutes dernières formulations (elles seront relues avec la page). Limites déclarées et points de
  l'organe commun : arbitrage 06, § 5.4.
- Avis du contradicteur sur l'arbitrage 06 (pièce 07) : arbitré (11/11/2026, `ARBITRAGE_PIECE_07_2026-11-11.md` du
  chantier). Figures closes. Réserve sur la cohorte : acceptée, formulation reprise mot pour mot (« ne s'explique pas
  par la seule modification du périmètre des formations comparées »), cohorte entrée au générateur et au témoin.
  Réserve sur la corrélation entre variations successives : le fait reste exploratoire et hors de la page (lire deux
  années au lieu d'une ne réduit l'écart moyen que de 4 à 5 % et ne déplace pas l'écart médian, `p07.py` § 4).
- Page (phase B) : fait, première version (11/11/2026) — `content/parcoursup-quelles-chances-d-etre-admis/_index.md`,
  six mouvements, limites, six questions fréquentes, appel au livre, sources en repli, bloc « Réutiliser » ; tous les
  nombres en jetons (`psup-val`, `{psup.*}` câblé dans `desc-figures.html`) ; carte de partage et vignette
  (`og_dossier_dette.py --parcoursup`, contraste annoncé contrôlé) ; ligne `parcoursup` au registre
  `data/sources_maj.json` (mode manuel, à revoir avant le 31/03/2027). Sources relues à la source le 11/11 :
  recommandation de Parcoursup sur la diversification et sa définition du taux d'accès (foire aux questions
  « Formuler ses vœux », par navigateur ; le site refuse les scripts), notices des trois jeux.
- Contrôles de la page : fait (11/11/2026) — générateur appliqué à la page réelle, 95 conditions de garde (gardes 6 et
  8 comprises), 758 jetons, 37 mutations sur 37 ; `check-all --ci` à 0 ; build à 0 ; `typo_build.py`,
  `audit-liens-build.py`, `check-rendu-ressources.py`, `check-dates-build.py` à 0 ; recette `recette.py` conforme de
  320 à 1 600 px ; `check_langue.py` sur le texte servi, quatre signalements lus, tous écartés.
- Relecture phrase à phrase du texte servi : fait (11/11/2026, session ; instantané `docs/relectures/`, 236 phrases).
  Non fait : relecture par un tiers.
- Panel après : fait (11/11/2026, `PANEL_APRES_2026-11-11\DIAGNOSTIC.md` du chantier ; pré-inscription écrite avant
  lancement, mêmes profils, même consigne, huit questions, bras témoin sans texte). Les faits propres à la page passent
  chez quatre lecteurs sur cinq et chez aucun témoin ; trois lecteurs butaient sur « classés assez haut » et aucun ne
  retenait spontanément la stabilité. Cinq corrections appliquées (définition, chapô, épreuve des 90 %, vérification en
  repli, question sur la liste d'attente). Non fait : nouveau passage simulé sur le texte corrigé (motif : ces
  corrections se jugent sur des lecteurs réels).
- Gate éditorial : fait par la session (11/11/2026, même fichier, § 6) — exactitude, accroche, progression, originalité
  tenus ; clarté et valeur finale partielles ; aucun P0, un P1 ouvert (le souvenir « ça bouge beaucoup »). À rejuger par
  la contre-expertise de la page.
- Contre-expertise de la page : fait (11/11/2026 ; paquet du sas `D:\CONTRE_EXPERTISE\2026-11-11_PARCOURSUP_PAGE\`,
  réponse archivée avant lecture, pièce 08 ; arbitrage `ARBITRAGE_PIECE_08_2026-11-11.md` du chantier). Verdict :
  architecture gardée, trois P0. P0-1 : la définition présentait une possibilité d'appel comme un appel (« le tour est
  venu ») → « dont le rang permettait de recevoir une proposition ». P0-2 : « le conseil tient » validait un conseil que
  les données ne testent pas → le seuil de 90 % garde une valeur de repère et ne garantit rien ; les résultats
  décrivent des formations, pas le réalisme d'un vœu. P0-3 : répartition par bac de l'exemple d'Illkirch, 42, 58 et
  0 % dans le fichier du ministère (relu au portail le 11/11, identique à notre export) contre 49, 50 et 1 % dans sa
  notice méthodologique → valeurs du fichier gardées, écart documenté dans le détail des sources. Six P1 appliqués
  (stabilité dite sans « l'ordre change peu », médianes des classes préparatoires en repli, « et elle seule » retiré,
  fonction des trois vérifications, périmètre rappelé près de la première figure, liste d'attente datée). **P1-7
  (appel au livre plus court, après les sources) : écarté par l'auteur le 11/11/2026**, l'ordre de fin de page et
  l'exemplaire offert étant des constantes du site. Après corrections : 97 conditions de garde, 37 mutations sur 37,
  contrôles du dépôt et du site construit à 0, recette conforme, instantané refait (245 phrases).
- `static/llms.txt` : fait (11/11/2026, ligne de la page ajoutée dans le commit de publication).
- Accord de l'auteur : fait (11/11/2026, « pousse la page en ligne »). Publication : commit et push du 11/11/2026.
  Attestation de la version servie : consignée après déploiement dans `REPRISE.md` du chantier et au
  `PROJECT_STATUS.md` du site.
- Mise en forme (maquette B+) : fait (11/11/2026). Étude et trois maquettes HTML fabriquées sur la page servie
  (`D:\PRO\06_PROMOTION\MAQUETTES_PARCOURSUP_2026-11-11\`, A relief, B repères visuels, C outil) ; deux
  contre-expertises externes arbitrées (pièces 09 et 10 du chantier) : B retenue, corrigée en B+ (repères en mots à
  partir de 600 px, fiche à partir de l'étape 1, taux d'accès et admissions en deux encadrés distincts et non en deux
  barres, périmètre des cent cases) ; **B+ validée par l'auteur le 11/11/2026** (« je valide ce type de présentation »).
  Application : `assets/scss/_ressource-relief.scss`, `partials/reperes-page.html` (front matter `reperes:`),
  `psup-cent`, `psup-val "…" "css"`, `faq-visible colonnes="2"`. Texte de la page construite égal ligne à ligne à
  celui de la maquette validée, positions et hauteurs des blocs identiques à 390, 768 et 1 280 px (avant les écarts
  ci-dessous). Garde 6 étendue aux repères et aux encadrés ; 113 conditions de garde, 40 mutations sur 40.
  Écarts à la maquette validée, tous issus des deux contrôles indépendants : figure à 864 px au lieu de 720 et côte à
  côte à partir de 1 280 px (ses plus petits textes restent à 12 px) ; repères sur trois colonnes à partir de 1 100 px,
  mot fort souligné, signe moins en gras, troisième repère enchaîné comme les deux autres ; encadrés l'un sous l'autre
  de 760 à 1 023 px ; légende des cent cases sans carré de couleur, « (cases pleines) » dans la phrase ; effectifs
  ajoutés à la seconde ligne de la grille ; en-tête de la fiche avec deux-points ; à 320 px, cartes numérotées 28 px
  moins hautes.
- Contrôle des marques graphiques (skill `controle-figures`) : fait (11/11/2026) — deux contrôleurs indépendants en
  lecture seule. (a) Géométrie et données : recalcul depuis les trois CSV sans le jeu ni le générateur ; tous les
  nombres et toutes les largeurs exacts (barres de la grille à moins de 0,05 point, 26 cases sur 100, composition 58
  et 42) ; **un défaut de fond trouvé, présent dans la page publiée le matin** : `part_acces_gen`, `_tec` et `_pro`
  répartissent les seuls élèves de terminale en position de recevoir une proposition, la page écrivait « candidats ».
  Vérifié par la session à la source (libellé de la variable au portail et p. 11 de la notice ; 60 formations sans
  élève de terminale classé : trois parts à 0 ; aucune part positive pour un bac sans élève de terminale classé ;
  relevé archivé dans `_SOURCES\portail_2026-11-11\` du chantier). Corrigé : quatre passages de la page, définition du
  jeu, trois formules retirées par la garde 8, une mutation, entrée au journal interne. La notice se contredit
  (définition p. 3 : « candidats » ; dictionnaire p. 11 : « terminales ») : dit dans le détail des sources.
  (b) Lecture du rendu à 390, 768 et 1 280 px : aucun défaut bloquant ; corrigés : encadrés écrasés vers 768 px, texte
  de la figure à 10 px dans la mise côte à côte, signe moins maigre, repères non reconnaissables comme liens, coupures
  de « N sur N », légende des cent cases ambiguë, effectif absent du corps de la page. Non traités, déclarés : entre
  601 et 860 px la version ordinateur des figures est servie trop petite, et l'agrandissement au toucher réduit la
  figure au téléphone (organes communs du site) ; au téléphone, les notes imprimées dans l'image séparent la figure de
  « Le résultat en une phrase » (générateur) ; la barre de composition donne au bleu un troisième sens (bac
  technologique) ; la mise en garde des deux encadrés vient après eux. Second passage des contrôleurs : non fait (les
  corrections ont été relues par la session, mesures et captures ; écart à la règle « jusqu'à zéro défaut nouveau »,
  déclaré).
- Contrôles après application : `check-all --ci`, build, `typo_build.py`, `audit-liens-build.py`,
  `check-rendu-ressources.py`, `check-dates-build.py`, `check-replis.py` à 0 ; recette de 320 à 1 600 px conforme ;
  `essai_page_relief.py` du chantier à 0 (marques contre le jeu brut, contrastes, clavier, sans JavaScript) ;
  `check_langue.py` : trois signalements, tous faux positifs sur des phrases antérieures ; instantané de relecture
  refait (261 phrases). Aucun lecteur réel n'a vu la page ainsi mise en forme.
