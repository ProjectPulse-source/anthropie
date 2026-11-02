# Fiche de conception — Que valent les formules du débat sur la dette ?

<!-- Gabarit : docs/conception/_GABARIT.md. Fiche écrite AVANT la page (skill ressource-site, règle 12). Commande :
D:\PRO\06_PROMOTION\PLAN_SUJETS_LIVRES_2026-11\REPRISE_PAGE_ARGUMENTS_DETTE.md (matrice sujet → livre, § 3, vague 2).
Slug provisoire : il se fige à l'arbitrage de la contre-expertise de phase A. -->

Page : `/formules-du-debat-sur-la-dette/` (FR) · `/en/public-debt-debate-claims/` (EN) · ouverte le 2026-11-01 —
**phase A** : architecture et protocole soumis à contre-expertise, aucun texte de page écrit.

## Forme

`explicatif-causal` (forme principale) et `quantitatif` (chaque verdict repose sur une série déjà calculée par le dossier
dette). Pourquoi : la page ne publie pas de série neuve, elle confronte des énoncés à des séries ; sa question est celle
de ce qu'une formule affirme et de ce qu'une série permet d'en dire.

Critères propres, recopiés en une ligne chacun :
- *explicatif-causal* : mécanisme, hypothèses concurrentes, contrefactuels, temporalités ; séparer constat, interprétation
  et causalité ; dire ce qui ferait varier la conclusion.
- *quantitatif* : définitions, périmètres, millésimes, unités, calculs reproductibles, dénominateurs ; chaque chiffre
  important relié à sa source, son calcul, sa figure et sa formulation.
- Modèle des pages de données (elle déclarera `donnees:`) : carte de partage et vignette, résultat en une phrase, figure
  signature SVG et PNG avec version téléphone, « Réutiliser », `Dataset`, JSON et CSV, jetons sans chiffre saisi, gardes
  vues mordre. Jeu propre envisagé : `dette_formules` (généré par `scripts/update_dette_formules.py`, qui **relit** les
  jeux existants `dette_dynamique`, `dette_officielle`, `dette_generations`, `dette_monde`, `dette_baisse` et n'appelle
  aucune source nouvelle, sauf les deux extensions nommées au champ « Limite »).

## Fiche de conception

### Question centrale

Les formules par lesquelles on parle de la dette publique en France — « nous dépensons plus que nos ressources », « la
charge que nous laisserons à nos enfants », « ce n'est pas la dépense mais la baisse des recettes », « la France emprunte
plus cher que la Grèce », « un euro de déficit, c'est un euro de dette » — résistent-elles aux séries officielles, et
quand elles ne résistent pas, sur quoi exactement se trompent-elles ?

### Enjeu

Le débat public sur la dette se mène par formules, non par séries : un citoyen, un élu local, un enseignant, un
journaliste entend des phrases courtes qui décident à sa place de ce qui est possible. Chacune engage une politique (couper,
taxer, attendre, renégocier). Savoir laquelle tient, et à quelle condition, rend au lecteur la possibilité de juger sans
dépendre du camp qui parle. Pour l'auteur : crédibilité (tester les deux camps avec la même règle), pédagogie (un outil
réutilisable), et prolongement du livre *Dette publique : qui paie vraiment ?* (ch. 9, « L'anatomie du discours », et
annexe « 7 arguments »), qui analyse ces formules par le langage et non par les séries.

### Croyance initiale

Deux croyances symétriques, chacune portée par un camp : « les chiffres donnent raison à ceux qui disent que la France vit
au-dessus de ses moyens » ; « les chiffres donnent raison à ceux qui disent que la dette vient des cadeaux fiscaux ». Et
une croyance commune aux deux : une formule est vraie ou fausse, et les chiffres tranchent.

### Découverte principale

**État au 02/11/2026, après l'inventaire, le double codage, le contrôle des frontières, les fiches de test et l'arbitrage
de phase B** (`D:\PRO\.claude\external-audits\ARBITRATIONS\ENTRANTE_2026-11-02_Formules_dette_phaseB_arbitrage.md`).
Question directrice, soumise à l'enquête : les chiffres tranchent un désaccord sur une grandeur mesurable ; tranchent-ils
aussi ses causes, ses conséquences, la politique à suivre ? Pour cette séance, étude de cas et non échantillon :
- **Les désaccords chiffrés portent surtout sur ce qu'on mesure, rarement sur l'arithmétique.** Sur dix formules, on
  compte trois ambiguïtés véritables de l'énoncé (F16, F13, F4) et cinq variantes qui posent une autre question. Une
  seule erreur de définition est établie (F3). Une formule tient sous toutes les variantes : « plus de 1 000 milliards »
  depuis 2017. Ces phénomènes sont comptés séparément ; **aucune proportion n'est publiée**
  (`FORMULES_DETTE\fiches\FICHES_DE_TEST.md`, grille de tolérances `fiches\GRILLE_TOLERANCES.md`).
- **Aucune des sept inférences examinées n'est démontrée par les données.** Deux sont contredites dans une de leurs
  lectures (F16 pour le montant, F4 pour les administrations) ; deux sont étayées dans une lecture précise (F6 comme
  contribution comptable, F4 pour l'État).
- **La contrainte est traitée en sens inverse selon la position.** Ceux qui gouvernent la présentent comme une
  **nécessité technique**, surtout F. Bayrou (« impossible de ne pas l'acquitter »). L'opposition la **nie ou la
  minimise**, surtout en contestant l'alarme. Sur les deux corpus et les trois codages, aucune de ces opérations
  n'apparaît dans l'autre camp (`inventaire\v2\RESULTATS_V2.md`). La ligne de partage est la position, non le bord.

S'y ajoute une observation des fiches : **les orateurs puisent au même stock de chiffres officiels**. Le document du
gouvernement du 15 juillet 2025 compare lui-même, en les nommant, deux périmètres. L. Wauquiez en fait une prévision.
Les 66 milliards d'É. Ciotti pour 2026 égalent le chiffre officiel de 2025 : c'est un écho, la filiation n'est pas
prouvée. **Ce qui ne tient pas** : « la borne de départ désigne le responsable » (M1, réfuté par son critère) ; la
dominance du registre de la fatalité, que le livre affirme (M6, indéterminé). *La version du 02/11 au soir (« neuf sur
dix », « cinq sur sept ») est retirée : elle additionnait des phénomènes différents et comptait deux variantes non
préinscrites.*

*Version du 01/11, conservée pour la trace :* **Révisée après l'arbitrage PRO-20261101-192956 (01/11/2026).** Objet : la transformation d'un fait comptable en
argument. Découverte visée, à éprouver sur l'inventaire codé : *dans cette séance, ce qui sépare les camps n'est presque
jamais le chiffre, mais l'année d'où l'on part, l'unité où on le compte et le pas qui mène du constat à la faute ou au
remède*. Trois motifs déjà observés sur des citations vérifiées : **la borne de départ désigne le responsable**
(gouvernement : « depuis cinquante et un ans », « nous en sommes tous responsables » ; opposition de gauche et de droite :
« depuis 2017 », « depuis huit ans ») ; **la croissance nominale est la variable que personne ne nomme** (« 3 %, seuil à
partir duquel la dette n'augmente plus » : faux pour le montant, exact pour le ratio seulement si la croissance nominale
dépasse environ 2,7 % ; 2,0 % en 2025) ; **le temps de la donnée n'est pas le temps du fait** (F8 exacte à sa date :
septembre 2025, 3,51 % contre 3,39 %, Eurostat mensuel ; la moyenne annuelle répond à une autre question). H1 ci-dessous
reste une hypothèse codée, rejetée comme loi générale.

*Version initiale, conservée pour la trace :* **Hypothèse à éprouver en phase A, pas encore un résultat.** Les formules du débat se trompent rarement sur un chiffre ;
elles se trompent sur la **variable qu'elles tiennent fixe sans le dire** — la fenêtre (de quelle année à quelle année),
l'unité (euros ou points de PIB), le périmètre (l'État, les administrations publiques, la nation), la date (un jour de
marché, une moyenne annuelle), le stock ou le flux. Une même série peut donner raison aux deux camps selon la variable
fixée : sur 2017-2024, le recul des recettes domine ; sur 2019-2025, la hausse des dépenses domine (jetons `dyn.ofce_*`,
`dyn.tresor_*`, déjà publiés). Si plusieurs formules testées se révèlent simplement fausses, ou simplement vraies, sur
toute variable raisonnable, la découverte se réduit et la page le dira.

**Ce motif n'est pas neuf dans le corpus de l'auteur** : l'AWP-09 (04/10/2026, « Trois lectures publiques rapprochées »)
l'établit pour trois estimations **savantes** de l'effet boule de neige (audit citoyen 2014, Cour des comptes, Fondation
iFRAP) — « fenêtres et objets expliquent une grande part de l'écart ». L'apport de la page est de l'éprouver sur les
formules **politiques**, attribuées et datées, des deux camps, avec les tests qu'aucune page ne fait (F1, F3, F4, F5, F8) ;
et d'en tirer un outil pour le lecteur, non un résultat de recherche.

### Mécanisme explicatif

Une formule de débat est un énoncé comprimé : pour tenir en une phrase, elle choisit une fenêtre, une unité, un périmètre,
et ce choix fait l'essentiel de sa conclusion. Le mécanisme est rhétorique (le choix sert la politique que la formule
défend) mais il n'est pas nécessairement fallacieux : chaque choix peut se justifier par la question posée (l'effet des
décisions prises depuis 2017 ; le budget de l'État et non celui des administrations). La page le dit (règle du dossier :
« une période se justifie par la question posée, non par le résultat qu'elle donne »). Hypothèses concurrentes réellement
soutenues : (a) les formules sont fausses parce que partisanes (lecture du soupçon) ; (b) elles sont exactes et le
désaccord porte sur les valeurs, non sur les faits (lecture du pluralisme) ; (c) elles sont exactes sur une variable
fixée et fausses sur une autre (hypothèse de la page). Ce qui ferait varier la conclusion : des formules dont le verdict ne
change sous aucune variante calculée.

### Preuve décisive

Pour chaque formule retenue, **le même protocole écrit avant le calcul** : (1) l'énoncé exact, sa source primaire datée,
son orateur et son groupe ; (2) ce qu'il affirme, réécrit en proposition testable (variable, unité, périmètre, période) ;
(3) la série du dossier qui le teste, au périmètre de l'énoncé, ou l'aveu qu'aucune ne le teste ; (4) le verdict à la
variable de l'énoncé ; (5) une **variante calculée** — l'autre fenêtre, l'autre unité ou l'autre périmètre — et le verdict
qu'elle donne ; (6) la variable qui fait basculer, s'il y en a une. Verdicts possibles, liste fermée : *exact* ; *exact
sur…, inexact sur…* ; *inexact* ; *hors d'atteinte des séries* (proposition normative ou politique, ou périmètre non couvert
— dit, non comblé par un chiffre voisin).

Corpus : **une seule séance**, le vote de confiance du 8 septembre 2025 à l'Assemblée nationale (compte rendu intégral
officiel, *JO* débats AN, p. 7691 et suivantes, PDF relu le 01/11/2026), où tous les groupes ont parlé de la dette le même
jour. Choix motivé : une séance unique neutralise le tri des citations par l'auteur de la page (on ne choisit pas ses
adversaires), et chaque camp y est représenté. Formules relevées à ce stade (attribution par lecture du compte rendu ;
celles marquées ⚠ sont à confirmer par relecture de la page imprimée, l'extraction automatique attribuant mal les
interruptions) :

| # | Formule (texte du compte rendu) | Orateur, groupe | Test envisagé (jetons existants) | Variable suspectée |
|---|---|---|---|---|
| F1 | « Tous les ans, nous dépensons plus — et souvent, beaucoup plus — que nos ressources de l'année » ; « depuis cinquante et un ans » | F. Bayrou, Premier ministre | **test principal : solde total des administrations publiques depuis 1974** (« budget en équilibre » ; série à ajouter) ; le solde primaire, positif 4 années sur 30 (`dyn.annees_excedent`, 1998-2001), est une autre grandeur, en variante étiquetée seulement (contre-expertise du 02/11) | solde total ; période |
| F2 | « Pour acquitter chaque euro de ces dépassements, il a fallu emprunter, comme un ménage ou une entreprise » ; « un euro de déficit, c'est un euro de dette supplémentaire » | F. Bayrou | résidu flux-stock +6,0 points sur 30 ans (`dyn.flux_stock`) ; durée de vie moyenne de la dette négociable 8 ans (`dette.aft_dvm_ans`), refinancement | stock ou flux ; l'analogie du ménage |
| F3 | « Nous transférerons plus de 100 milliards à nos créanciers » | F. Bayrou | charge projetée (`dette.prev_*`) ; détention par la Banque de France 16,5 % (`gen.bc_fin`) ; intérêts nets des intérêts reçus (`dette.interets_nets_mdeur`) | qui sont les créanciers ; brut ou net ; projection |
| F4 | « Nous allons bientôt dépenser plus pour payer les intérêts de la dette que pour former nos enfants » | L. Wauquiez, Droite républicaine | intérêts de 2024 = 40 % de la dépense d'enseignement des administrations de 2024 (`dette.pct_interets_education`, même millésime pour les deux termes, `dette.equiv_annee`) — **périmètre APU** ; la formule vise sans doute le budget de l'État | périmètre (État ou APU) ; horizon |
| F5 | « La charge que nous laisserons à nos enfants […] chaque heure, augmente de 18 millions d'euros » | P. Christophe, Horizons | hausse annuelle de l'encours (`dette_trimestrielle`) ; part des déficits qui a correspondu à des actifs, 18 % (`gen.part_k`) | stock brut ou charge nette ; actifs laissés |
| F6 | « Ce n'est pas l'augmentation des dépenses publiques — restées stables depuis 2017 — qui a creusé le déficit, mais la baisse des recettes » | C. Chatelain, Écologiste et social | fenêtres 2017-2024 et 2019-2025 (`dyn.ofce_*`, `dyn.tresor_*`, `dyn.croise_*`) ; dépenses en euros et en points de PIB | fenêtre ; unité |
| F7 | « Et les cadeaux aux riches ? » (interruption) | J.-P. Lecoq, GDR | recul des recettes en points de PIB (`dyn.ofce_rec`) — ne dit rien de leur répartition par contribuable | hors d'atteinte pour la répartition : à dire |
| F8 | « La France s'endette à des taux supérieurs à ceux de la Grèce » | L. Wauquiez, Droite républicaine (compte rendu, p. 7699, vérifié au tour de parole le 01/11/2026) | écart à l'Allemagne en moyenne annuelle 2025 : France 0,76 point, Grèce 0,78 (`ecarts_allemagne`) ; en 2012 : 1,04 et 21,0 ; données mensuelles : à ajouter | date (jour ou moyenne) ; ce que le prix dit du stock (`monde.r2_prix_stock`) |
| F9 | « D'autres s'y sont essayés avant nous […] la Grèce, le Portugal, l'Espagne » | P. Christophe | baisse du ratio au Portugal (`baisse.cmp_pt_*`) | quel épisode, quelle fenêtre |
| F10 | « La dette peut être vertueuse si elle permet des investissements pour l'école, pour l'hôpital… » | S. Peu, GDR | part des déficits en actifs, de 32 % à 10 % par décennie (`gen.d1_part`…`gen.d3_part`) | condition (« si ») tenue ou non ; capital humain hors champ |
| F11 | « Plus notre dette s'accroît, plus les marchés financiers sont en mesure d'influencer notre politique » | M. Fesneau, Démocrates | prix et stock en 2025 dans l'Union (`monde.r2_prix_stock`, `monde.r2_charge_stock`), 2012 | mécanisme : stock, prix ou charge |

Candidates relevées en seconde lecture (01/11/2026), attributions **toutes à confirmer** sur la page imprimée — l'extraction
du PDF fait chevaucher orateurs et interruptions :

| # | Formule | Orateur probable | Test envisagé | Variable suspectée |
|---|---|---|---|---|
| F12 | « Les spéculations hasardeuses du Mozart de la finance nous ont coûté 1 000 milliards de dette supplémentaire » | M. Panot, LFI | hausse de l'encours depuis 2017 en euros et en points ; part 2020-2025 (`dyn.p3_*`) | attribution d'un montant à une politique ; euros ou points |
| F13 | « 1 200 milliards d'euros de dette supplémentaire depuis 2017 […] après 400 milliards sous François Hollande » | É. Ciotti, UDR | mêmes séries, 2012-2017 et 2017-2025, euros et points de PIB | unité (euros courants) ; fenêtre (crise sanitaire incluse) |
| F14 | « La charge de la dette s'élèvera à 66 milliards en 2026, soit 60 % de plus qu'en 2017 » ; « supérieur au budget de n'importe quel ministère » | É. Ciotti | charge APU 2017 et prévision (`dette.prev_*`) ; comparaison ministérielle hors jeu | périmètre (État ou APU) ; projection |
| F14 bis | « L'année prochaine, en 2026, cette somme devrait atteindre 75 milliards » (F. Bayrou, la « somme » étant l'annuité, intérêts et capital) face à « 66 milliards en 2026 » (É. Ciotti) | F. Bayrou ; É. Ciotti | prévisions publiées en septembre 2025 (charge de l'État, charge des administrations) | même horizon, deux objets : concept, périmètre, scénario (contre-expertise du 02/11) |
| F15 | « La France ne peut vivre éternellement à crédit » | G. Attal, EPR | hors d'atteinte comme norme ; version testable : solde primaire stabilisant (`/dette-publique-peut-elle-baisser/#solde-stabilisant`) | norme ou constat |

Ajoutées à l'arbitrage (citations vérifiées au compte rendu) :

| # | Formule | Orateur | Test | Variable |
|---|---|---|---|---|
| F16 | « Atteindre en 2029 le seuil de 3 % de déficit public, seuil à partir duquel la dette n'augmente plus » | F. Bayrou | déficit stabilisant = dette × g/(1+g) : 2,30 % à g = 2,03 % (2025), 3,37 % à g = 3 % | stock ou ratio ; croissance nominale |
| F17 | « Ils porteront pendant vingt ou trente ans […] le poids des milliers de milliards de dettes que leurs aînés ont contractées » | F. Bayrou | refinancement ; part des déficits en actifs ; détention (`/dette-publique-generations-futures/`) | attribution à une génération |
| F18 | « Désigner à la vindicte publique une classe d'âge […] un système que vous soutenez vous-même depuis quarante ans et […] depuis huit ans » | M. Le Pen, RN | norme et attribution : hors d'atteinte pour la responsabilité ; borne codée | borne de départ |

**Protocole révisé (arbitrage)** : nature de l'énoncé codée **avant** tout calcul (constat, prévision, causalité,
condition, norme, question) ; classes 1 à 5 du contradicteur ; attributs : borne et acteur désigné, unité, millésime,
pronom ; deux issues distinctes, *non déterminé avec les données disponibles* et *hors d'atteinte des séries* ; test
principal **à la date de l'énoncé**, éclairage rétrospectif étiqueté, jamais substitué ; chaque fiche de test répond par
écrit à « ce test répond-il à l'énoncé ? » ; F7 et F9 retirées des tests, gardées à l'inventaire ; critère d'abandon : moins
de cinq cas qui éclairent un mécanisme distinct, ou corpus non reproductible (alors option C). Inventaire exhaustif et
règle de codage dans `D:\PRO\06_PROMOTION\PLAN_SUJETS_LIVRES_2026-11\FORMULES_DETTE\inventaire\`.

**Équilibre du corpus** (constat initial, corrigé par F18) : aucune formule du groupe RN portant sur la dette elle-même n'a encore été isolée (l'intervention de
M. Le Pen relevée vise la responsabilité du gouvernement) ; à rechercher dans la lecture intégrale avant le test décisif.
Si un groupe n'a prononcé aucune formule testable, la page le dit, sans en chercher une hors séance pour équilibrer.

Formules de la commande absentes de la séance : « il n'y a pas d'alternative » (Thatcher, 1980 ; livre, ch. 9) et « on
se la doit à nous-mêmes » (déjà testée par `/dette-publique-generations-futures/#detention`). La première relève du
verdict *hors d'atteinte des séries* (proposition sur le possible, non sur l'observé), sauf sa version testable — « la
dette ne peut pas baisser » —, déjà traitée par `/dette-publique-peut-elle-baisser/` ; la seconde se cite par lien, sans
redite. Test décisif avant la page : les onze lignes calculées au protocole ci-dessus, dans
`D:\PRO\06_PROMOTION\PLAN_SUJETS_LIVRES_2026-11\FORMULES_DETTE\test_decisif\` ; **sans lui, pas de page**.

### Pouvoir discriminant

- **Explications rivales réellement soutenues** : (a) « la dette vient d'un excès de dépenses » (gouvernement Bayrou,
  direction générale du Trésor sur 2019-2025) ; (b) « la dette vient d'un recul des recettes » (groupes de gauche, OFCE sur
  2017-2024, rapport Attac-CADTM de mars 2025) ; (c) « la dette française est jugée par les marchés comme celle de la
  Grèce » (droite) contre « la dette n'est pas jugée sur son stock » (lecture du dossier, `monde.r2_prix_stock`).
- **Témoin qui les départage en ne changeant qu'une variable à la fois** : la même série Eurostat, une seule borne
  déplacée (2017 → 2019 au départ, 2024 → 2025 à l'arrivée) ; la même série de taux, la moyenne annuelle contre le mois ; la
  même dépense, en euros puis en points de PIB ; le même rapport, au périmètre de l'État puis des administrations.
- **Que révèle la figure qu'une série isolée ne montre pas ?** Que le verdict d'une formule bascule avec une seule
  variable, et laquelle — une série isolée donne un verdict, la grille montre sa fragilité.
- **Quelles explications départage-t-elle ?** Elle ne tranche pas entre (a) et (b) : elle montre que les deux sont exactes
  sur leur fenêtre et que la fenêtre commune (2019-2024) en départage une — `dyn.croise_*` : le recul des recettes domine.
  Elle départage (c) : le prix ne suit pas le stock en 2025.
- **Robustesse** : chaque verdict porte sa variante calculée (protocole, point 5) ; une formule dont la variante est
  affirmée et non calculée ne passe pas.
- **Levier ou risque éclairé** : quelle question poser à toute formule (« de quelle année à quelle année ? en euros ou en
  points ? l'État ou les administrations ? »), outil réutilisable hors de ce débat.

Si la grille ne départage rien de plus que les pages du dossier, la page le dit et la décision de phase A bascule vers
l'option « sections » (voir « Singularité »).

### Limite

- Les séries testent ce qui est **observé** ; elles ne disent pas ce qu'il **faut** faire. Un verdict *exact* sur une
  formule ne valide pas la politique qu'elle défend (« nous dépensons plus que nos ressources » peut être exact et ne pas
  dire s'il faut baisser la dépense ou relever l'impôt).
- Une décomposition comptable n'est pas une attribution causale (leçon 15 du site) : « le recul des recettes domine » ne
  dit ni quelles décisions l'ont produit, ni qu'elles sont des « cadeaux ».
- Le corpus est une séance : il ne représente pas tout le débat (plateaux, presse, partis hors Parlement). Il est choisi
  pour qu'aucune citation ne soit triée, non pour qu'il soit exhaustif.
- Deux tests demandent une donnée absente des jeux : le **solde total** depuis 1974 (F1 ; Insee, comptes nationaux base
  2020, série longue) et les **taux mensuels** de 2025 (F8 ; Eurostat `irt_lt_mcby_m`). Sans eux, les deux formules
  reçoivent le verdict partiel que permettent les données annuelles, dit comme tel ; aucun chiffre voisin substitué.
- F4 vise vraisemblablement le budget de l'État (charge de la dette, programme 117, contre mission « Enseignement
  scolaire »), que les jeux du site ne contiennent pas : verdict au périmètre APU, et le périmètre de l'État déclaré non
  testé, ou ajouté au jeu si la loi de finances se lit par script.

### Valeur finale

Après lecture, le lecteur sait dire, sans jargon : ce qu'il croyait (une formule tranche) ; ce qu'il sait (chacune
tranche sur une variable choisie, et laquelle) ; sur quelles preuves (les séries du dossier, une variante par formule) ;
quelle question s'ouvre (les trois questions à poser à toute formule, et celles que les séries ne tranchent pas : qui doit
porter l'ajustement). Outil réutilisable : la grille « fenêtre, unité, périmètre, date, stock ou flux ».

### Singularité

Cette page existe parce qu'elle révèle **que les formules des deux camps sont le plus souvent justes dans un cadre et
fausses dans un autre, que la conclusion qu'on en tire n'est presque jamais démontrée, et que les deux camps traitent la
contrainte en sens inverse** (état au 02/11/2026, voir « Découverte principale »), que le lecteur ne découvre pas dans les neuf pages du dossier dette (lues le
01/11/2026 : chacune répond à **une** question de fond et ne confronte qu'en passant une formule — « on se la doit à
nous-mêmes » dans `/dette-publique-generations-futures/#detention`, l'effet de la fenêtre dans
`/pourquoi-la-dette-publique-augmente/#depenses-recettes` —, aucune ne prend pour objet le discours lui-même, ni ne
confronte des énoncés datés et attribués). Le livre analyse les mêmes formules par le langage (ch. 9-10), sans les
confronter aux séries. L'AWP-09 applique la même règle à trois lectures savantes, non au discours politique : la page en
est l'application grand public à un autre objet, et le dit.

**Risque à contrôler** : la règle du site écarte les « pages carrefours par grand sujet ». Si, une fois écrite, chaque
section ne fait que renvoyer à la page du dossier qui porte la preuve, la page est un carrefour et tombe. Elle ne tient que
si chaque formule y reçoit **son** test (à son périmètre et à sa date, souvent absents des pages du dossier : F1, F3, F4,
F5, F8) et si la grille d'ensemble apporte ce qu'aucune page isolée n'apporte. Option concurrente, soumise à la
contre-expertise : pas de page, une section par formule dans la page du dossier qui porte sa preuve.

### Raccords

- **Définition de l'anthropie** : **écartée** du corps de la page (page de faits sur des énoncés : aucune lecture
  anthropique dans l'exposé des constats). Retenue seulement dans un bloc séparé de fin, présenté comme l'hypothèse de
  l'auteur, si la contre-expertise l'admet : « le livre lit ces formules comme des façons de désigner qui porte
  l'ajustement ; cette page ne teste que ce qu'elles affirment des comptes ».
- **Livre** *Dette publique : qui paie vraiment ?* : **retenu**, `appel-livre` en fin de page, `avis="non"`, phrase :
  « Le chapitre 9 du livre analyse ces formules par le langage — qui parle, de quel droit, en fermant quelles
  possibilités ; cette page les confronte aux comptes. » ⚠ Conflit à déclarer : l'annexe « 7 arguments » du livre défend
  elle-même des formules du même genre (« on ferme des maternités […] pendant qu'on paie des milliards d'intérêts ») que
  le volet *Combien coûte la dette publique ?* nuance (dépenses de santé et d'enseignement en hausse en euros et au-dessus
  de 2019 en part du PIB, `dette.sante_pct_*`). La page ne les teste pas (elles ne sont pas dans la séance) mais ne les
  cautionne pas non plus ; l'appel au livre le présente comme un essai. **Décision de l'auteur (01/11/2026) : note d'autocritique**, audit séparé
  des affirmations empiriques du livre avec les deux mêmes verdicts (contre-expertise du 02/11, § 8). Matière déjà réunie :
  la thèse du ch. 9 se vérifie dans sa forme technique et chez un orateur, non comme registre dominant ; la contestation
  que le livre range parmi les « discours qui renomment pour contester » apparaît surtout comme contestation de l'alarme.
- **Working paper** : **retenu**, AWP-09 (*Ce que les comptes publics permettent d'établir sur le déplacement de la
  charge de la dette*), phrase : « La même règle — fixer la fenêtre et l'objet avant de comparer — rapproche, dans le
  working paper AWP-09, trois estimations savantes réputées contradictoires. » AWP-03 **écarté** du corps (il porte la
  lecture anthropique, hors d'une page de faits ; l'AWP-09 le met lui-même à l'épreuve). Précédent utile au conflit
  ci-dessus : l'AWP-09 rend déjà un verdict énoncé par énoncé sur les thèses de l'auteur (« soutenue dans un périmètre
  patrimonial, conditionnelle ou hors de portée ailleurs »).
- **Pages voisines** : **retenues**, une par verdict qui s'y appuie, avec la phrase qui porte la relation :
  `/pourquoi-la-dette-publique-augmente/#depenses-recettes` (F6, F1) — « la décomposition complète, fenêtre par fenêtre » ;
  `/cout-de-la-dette-publique/` (F3, F4) — « ce que la charge représente, et ce qu'elle rémunère » ;
  `/dette-publique-generations-futures/` (F5, F10, « on se la doit à nous-mêmes ») — « à quoi les déficits ont
  correspondu » ; `/dette-publique-comparaison-internationale/#euro-et-taux` (F8, F11) — « trente ans d'écarts avec
  l'Allemagne » ; `/dette-publique-peut-elle-baisser/` (F9, « il n'y a pas d'alternative ») — « les pays où le ratio a
  baissé ». **Dans l'autre sens** : une phrase depuis `/dette-publique-generations-futures/` (qui mentionne déjà le
  langage du débat), une depuis `#depenses-recettes` ; aucune depuis `/quest-ce-que-lanthropie/` (la page ne démontre pas
  une application du concept).

## Fiche D0

Inscrite dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` (section « Hors étapes — ressource
`/formules-du-debat-sur-la-dette/` », 01/11/2026). Résumé : **résultat visé** — être la page lue et citée sur les
formules du débat (« vivre au-dessus de ses moyens », « la dette vient des cadeaux fiscaux », « la France emprunte plus
cher que la Grèce », « dette laissée à nos enfants ») et y conduire au livre ; **finalités** : crédibilité d'abord (deux
camps, une règle), diffusion du livre ensuite ; **diagnostics** : Search Console sur ces requêtes, citations relevées à
la main, demandes d'exemplaire `?src=consultation-formules-du-debat-sur-la-dette`, navigation vers les volets du dossier ;
**état initial** : page inexistante (01/11/2026), demande Search Console à relever avant la phase B ; **réexamen** : J+60
après la mise en ligne.

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait (01/11/2026, sortie lue : méthode, MAGNIFIER, séries publiques,
  vérificateur de références, votes et dossiers du Parlement, relecture de langue, recette, panel).
- Lecture préalable : fait (01/11/2026) — CLAUDE.md du site (quatre sections), livre ch. 9-10 et annexe « 7 arguments »
  (édition du 17/10/2026, p. 117-135 et 207-209), plans et chapôs des neuf pages du dossier, jeux et jetons existants.
- Corpus primaire : fait en partie (01/11/2026) — compte rendu de la séance du 8 septembre 2025 relu par extraction ;
  attributions vérifiées au tour de parole (F8 : L. Wauquiez) ; archivé avec son empreinte dans `FORMULES_DETTE\_PIECES_RECUES\`
  (SHA-256 `4ab51e50…3701`).
- Protocole du type : écrit (champ « Preuve décisive ») ; calcul non fait (test décisif, après la contre-expertise de
  phase A, pour que le protocole soit arrêté avant les résultats).
- Scénarios d'architecture : fait (01/11/2026, trois scénarios, paquet de contre-expertise § 6).
- Panel avant : non fait (motif : page ni pilote ni refonte ; la décision d'architecture en attente porte sur la
  recevabilité, que la contre-expertise juge mieux qu'une réception simulée ; à reprendre si l'arbitrage retient la page).
- Contre-expertise de phase A : paquet préparé (01/11/2026,
  `D:\PRO\06_PROMOTION\PLAN_SUJETS_LIVRES_2026-11\FORMULES_DETTE\PAQUET_PHASE_A_FORMULES_DETTE_2026-11-01.md`),
  enregistré **PRO-20261101-192956** (SHA-256 `CBA44924…71BD`), sas `D:\CONTRE_EXPERTISE\PRO\PRO-20261101-192956\`,
  statut `AWAITING_MANUAL_SEND` ; envoyée par l'auteur, réponse archivée verbatim le 01/11/2026 (SHA-256
  `DC0C4BA6…AA57`), **arbitrée** le 01/11/2026 : `D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261101-192956_arbitrage.md`
  (option A modifiée ; protocole révisé ; F16-F18 ajoutées ; statut `ARBITRATED` au registre).
- Inventaire exhaustif et codage préenregistré : fait (01/11/2026), `D:\PRO\06_PROMOTION\PLAN_SUJETS_LIVRES_2026-11\FORMULES_DETTE\inventaire\`
  — règle écrite avant extraction (`REGLE_DE_CODAGE.md`, empreinte initiale `506ca2c1…8e55`, journal des précisions) ;
  1 448 phrases, toutes lues (filtre puis témoin sans filtre, qui a fait refaire la passe : 144 énoncés sur 320 venaient de
  lui seul) ; 320 énoncés retenus, 231 phrases exclues avec motif, conservation vérifiée par script (`CONSERVATION.txt`) ;
  codage de première passe et tests préenregistrés (`RESULTATS_CODAGE_PRINCIPAL.md`). Second codeur aveugle : voir
  `ACCORD_DEUX_CODEURS.md`. Classes 1 à 5 : non fait (après les fiches de test).
- Contre-expertise de l'inventaire : fait (02/11/2026, pièce de l'auteur, SHA-256 `7a3a1e9a…4620`), arbitrée :
  `D:\PRO\.claude\external-audits\ARBITRATIONS\ENTRANTE_2026-11-02_Formules_dette_inventaire_arbitrage.md` (règle v2 à écrire,
  dont la contrainte niée et le camp par vote individuel ; six familles de cas retenues à titre provisoire).
- Règle v2 et arbitrage des 333 désaccords de la v1 : fait (02/11/2026), `FORMULES_DETTE\inventaire\ARBITRAGE_DESACCORDS_V1.md`
  (audit indépendant de 40 décisions ; verdicts identiques sous les trois codages). Recodage v2 : fait (02/11/2026,
  `FORMULES_DETTE\inventaire\v2\RESULTATS_V2.md` ; deux codeurs et un arbitre tiers, frontières relues en entier, corpus élargi à
  387 énoncés).
- Fiches de test et test décisif : fait à titre provisoire (02/11/2026), `FORMULES_DETTE\fiches\FICHES_DE_TEST.md`, protocole écrit avant
  (`inventaire\PROTOCOLE_FICHES_DE_TEST.md`) ; deux verdicts par formule ; H1a et H1b non rejetées ; sept mécanismes distincts
  (critère : cinq) ; F3, F4 (État) et F14 bis complétées le même jour sur sources archivées ; reste le millésime en temps réel. Phase B : scénarios écrits
  (`FORMULES_DETTE\PHASE_B_SCENARIOS.md`). Contre-expertise de phase B (02/11/2026, pièce de l'auteur, SHA-256
  `3cfdc64b…02f5f0`) arbitrée : `ENTRANTE_2026-11-02_Formules_dette_phaseB_arbitrage.md`. Proportions H1a et H1b retirées
  et recodées. F2, F4, F5, F6, F13, F14 bis et F16 corrigés. Architecture en trois niveaux (mesurer, expliquer, conclure),
  ouverture sur F4. F8 au jour : fait (02/11/2026) ; France au-dessus de la Grèce les 4 et 18 septembre 2025 (Banque de Grèce,
  mesure homogène), taux grec du 8 non lu. Texte : non fait. Contre-expertise entrante
  du 02/11 (phase A bis) arbitrée : `ENTRANTE_2026-11-02_Formules_dette_phaseA_bis_arbitrage.md`.
- Décision de l'auteur sur le conflit livre / page (raccord « Livre ») : **fait (01/11/2026)** — l'auteur retient la note
  d'autocritique (« oui pour l'autocritique »). Elle examinera quelques passages exacts du livre, dont la thèse du ch. 9
  sur la disparition du sujet, avec le résultat du test M6 quel qu'il soit (règle de codage, § 7).
- Séries ajoutées (02/11/2026) : solde des administrations publiques depuis 1949 (Insee, F1) ; rendements à dix ans mensuels
  (Eurostat, F8) ; millésime de septembre 2025 (Insee IR n° 163 et IP n° 2054 ; `FORMULES_DETTE\fiches\MILLESIME_TEMPS_REEL.md` :
  aucun verdict changé, la prédominance 2019-2024 change) ; valeurs documentaires transcrites avec page, extrait et empreinte
  (`scripts/sources_dette_formules/documentaires.json`). Note d'autocritique : fait (`FORMULES_DETTE\NOTE_AUTOCRITIQUE_LIVRE.md`,
  13 fiches ; synthèse dans la section « Le livre passé aux mêmes tests »).
- Générateur et page (02/11/2026) : `scripts/update_dette_formules.py` (jeu `dette_formules`, deux figures FR/EN avec versions
  téléphone, CSV et JSON), `scripts/og_dette_formules.py` (cartes et vignettes), shortcode `form-val`, jetons `{form.*}` dans
  `partials/desc-figures.html` ; pages FR et EN écrites.
- Gardes vues mordre : fait (02/11/2026) — 44 gardes ; onze mutations (`--mutation=f1` à `inv`), chacune vue mordre ; contrôle
  des hauteurs déclarées vu mordre en usage réel (précaution allongée).
- Figures téléphone : fait (02/11/2026), parité contrôlée par le générateur.
- Relecture de langue : fait (02/11/2026) — `check_langue.py` (11 signalements, tous faux positifs ou artefacts d'extraction) ;
  `check-rendu-ressources.py` (4 défauts corrigés dans le générateur : signe après verbe, accord de « point », « a monté »).
- Recette 320-1600 (`recette.py`) : fait (02/11/2026), RECETTE OK sur six largeurs, FR et EN ; `check-all --ci` 0, build `$?` 0,
  liens, dates et rendu conformes.
- Panel après : non fait (motif : la contre-expertise externe de la page est demandée tout de suite ; à faire si l'auteur le
  souhaite avant publication).
- Gate éditorial : fait (02/11/2026, jugement de la session) — exactitude tenu (réserves : taux grec du 8 septembre non lu,
  codage par agents) ; clarté partiel (page dense, grille téléphone très haute) ; accroche tenu (ouverture F4) ; progression
  tenu (trois niveaux) ; originalité tenu (stock commun, révision qui inverse une prédominance, deux traitements de la
  contrainte) ; valeur finale tenu (six questions). Cinq fonctions remplies.
- Relecture phrase à phrase FR et EN : fait (02/11/2026) sur le texte servi ; corrections : « bientôt » ramené à
  « plausible », comparaison F4 reformulée, citation de la Cour resserrée, accords et pronoms.
- Instantané de relecture : fait (02/11/2026), `docs/relectures/formules-du-debat-sur-la-dette.txt` et `en__public-debt-debate-claims.txt`.
- Contre-expertise de la page : paquet enregistré **PRO-20261102-044049** (SHA-256 `1063F49F…68B9`), sas
  `D:\CONTRE_EXPERTISE\PRO\PRO-20261102-044049\` ; réponse archivée le 02/11/2026 (SHA-256 `7D883E13…DEB8`), **arbitrée** :
  `D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261102-044049_arbitrage.md` (8 P0 traités ; F8 établie le jour même par la page HDAT
  archivée, 3,49 contre 3,34 ; F16 jugée sur 2024 ; registres reformulés ; tableau des 13 affirmations du livre publié en repli).
  Statut `ARBITRATED`. **Décision humaine requise** : courants absents de la séance (NPA, LO, UPR…) ; option (a) appliquée en attendant.
- Décision de l'auteur sur les courants absents : **fait (02/11/2026)** — « l'idéal serait les engagements 2026 pour la
  présidentielle de 2027 » ; dernier texte officiel pour qui n'a rien publié en 2026 ; filtre et témoin ; pièces hors Git,
  manifeste versionné. Protocole préenregistré : `FORMULES_DETTE\hors_hemicycle\PROTOCOLE_HORS_HEMICYCLE.md` (empreinte
  initiale `cab020d0…d0a8`, journal daté de chaque décision prise ensuite).
- Corpus « hors de l'hémicycle » : fait (02/11/2026) — 37 candidats déclarés, 33 avec texte, 368 documents (`CORPUS_2027.md`,
  manifeste et empreintes ; copie sur `G:\_BACKUP_FORMULES_DETTE_HORS_HEMICYCLE_2026-11-02`). Défaut d'extraction des PDF
  (encodage) trouvé par le témoin et corrigé ; critère du témoin atteint (6 documents sur 37, seuil 10 %) : lecture intégrale
  de toutes les pièces. Double codage A / B aveugle et arbitre tiers : 352 énoncés, 21 candidats, 71 testables ; kappa 0,84
  (retenue) et 0,75 (registre), 174 unités arbitrées. Omission constatée après coup et déclarée (phrase de la lettre de
  B. Cazeneuve sans le mot « dette »).
- Tests des 71 énoncés : fait (02/11/2026), `FORMULES_DETTE\hors_hemicycle\TESTS_HORS_HEMICYCLE.md`, à la date de chaque document ;
  citations confrontées au texte intégral par `scripts\extrait_site.py` (vu mordre sur une citation altérée), qui écrit
  l'extrait figé `scripts/sources_dette_formules/hors_hemicycle.json`. Grille de tolérances appliquée sans adaptation.
- Générateur et page, section « Hors de l'hémicycle » (`#hors-hemicycle`, FR et EN) : fait (02/11/2026) — `calcul_hh`,
  verdicts écrits une fois (`VERDICTS_HH`) et servis par jetons, bloc `hors_hemicycle` du JSON et du CSV ; 26 gardes nouvelles
  (72 au total), mutation `--mutation=hh` vue mordre ; plafonds de la Défense et des remboursements transcrits du tableau 1 bis
  du rapport de juillet 2025 ; dette de fin 2024 au millésime de mai 2025 lue dans la figure 5 de l'Insee Première n° 2054.
  Limites et sources mises à jour ; chapô et description du jeu complétés.
- Contrôles après la section : `check-all --ci` 0, build `$?` 0, `typo_build` 0, liens, dates et rendu conformes, recette
  RECETTE OK (320-1600, FR et EN, 19 ancres) ; relecture phrase à phrase du texte servi FR et EN (citations ramenées à la
  lettre de la source, contrôle par script de chaque guillemet de la section ; libellés français de la barre corrigés sur la
  page anglaise) ; `check_langue.py` relu (faux positifs ; « A cause » gardé, lettre de la source) ; instantanés refaits.
- Erreur de nom trouvée avant publication (02/11/2026) : « Dominique Legendre » au lieu de Jean-François Legendre, saisi dans
  l'extrait et la prose ; corrigé partout ; `extrait_site.py` refuse désormais tout nom absent du tableau des candidats de
  `CORPUS_2027.md` (vu mordre).
- Contre-expertise de la section : paquet enregistré **PRO-20261102-080036** (02/11/2026, SHA-256 `10B91761…1483`,
  `FORMULES_DETTE\PAQUET_HORS_HEMICYCLE_FORMULES_DETTE_2026-11-02.md`), sas `D:\CONTRE_EXPERTISE\PRO\PRO-20261102-080036\`,
  statut `AWAITING_MANUAL_SEND` (envoi par l'auteur). Réponse archivée le 02/11/2026 (SHA-256 `B847C4FD…61F8`), **arbitrée** :
  `D:\PRO\.claude\external-audits\ARBITRATIONS\PRO-20261102-080036_arbitrage.md` (accepté avec modification ; rang budgétaire
  jugé sur le document en vigueur à la date du texte, plafonds 2027 ajoutés ; recettes 2025 à l'édition d'octobre 2026 ;
  attributions et bornes contrefactuelles « non établies » ; 19 lignes avec critère de sélection écrit ; vivier des 71
  testables publié ; 77 gardes). Statut `ARBITRATED`. Contrôles refaits : check-all --ci 0, build 0, RECETTE OK, instantanés.
- Point ouvert hors section : `update_dette_dynamique.py` refuse l'édition Eurostat d'octobre 2026 (garde de prose du volet 1) ;
  la page cite donc l'édition d'octobre par un extrait figé propre et dit les deux millésimes.
- Mises à jour d'état du site (`PROJECT_STATUS.md`, `static/llms.txt`) : fait (02/11/2026, seuls nos ajouts indexés, les
  modifications d'une autre session laissées hors du commit).
- Accord de l'auteur : fait (02/11/2026, « Ok finis et pousse »). Commit `3344c98`, vérifié dans un arbre de travail propre
  (check-all --ci 0, build 0, liens, rendu, dates, typographie) ; push ; déploiement réussi.
- Attestation de la version servie : fait (02/11/2026) — FR et EN en 200, section `#hors-hemicycle` et bloc `hors_hemicycle`
  du JSON présents, nom de J.-F. Legendre correct.
