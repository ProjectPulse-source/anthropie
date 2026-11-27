# Fiche de conception — Les élèves maîtrisent-ils moins bien la langue française ?

Page : `/les-eleves-maitrisent-ils-moins-bien-la-langue-francaise/` (FR seul : `lang_repli` vers `/en/resources/`, exclusion
déclarée — langue, programmes et statistique français) · ouverte le 2026-10-09 · fiche écrite le 2026-11-17, à la reprise de
la page, **après** la relecture des sources (`D:\PRO\06_PROMOTION\INTELLIGIBILITE_RESSOURCES_2026-11-11\LOTS\les-eleves-maitrisent-ils-moins-bien-la-langue-francaise\SOURCES\`,
rapports `langue_R1.md` et `langue_R2.md`, sondes `SONDES_SESSION.md`) : la page, publiée le 10/10/2026, précède la règle 12.
Recherche : `D:\PRO\06_PROMOTION\RECHERCHE_LYCEES_LECTURE_2026-10-09\` (plan, protocole écrit avant calcul, verdict).
**Reprise du 25/11/2026** (lot `LOTS\corrections-radar-2411\`, `PLAN_E07.md`), après la relecture des sources du 24/11 par
un agent séparé (`SOURCES\RELECTURE_E07.md`, cité ci-dessous « RS24 ») : la fiche portait encore « le vocabulaire n'est suivi
par aucune série au collège ni au lycée », faux à la source (RS24, P0-1) ; découverte, mécanisme, discriminant, limite et D0
réalignés, chaque énoncé rattaché à sa ligne de relecture.

## Forme

Données (`quantitatif`, `donnees: [langue_eleves]`) : séries officielles reprises et, en partie, recalculées. Critères du
type : définitions, périmètres, millésimes, unités, calculs reproductibles, changements de série, dénominateurs,
incertitudes ; chaque chiffre important relié à sa source, son calcul, sa figure et sa formulation. Modèle vérifié par
machine : carte de partage et vignette, résultat en une phrase, « Réutiliser », `Dataset`, JSON et CSV, jetons, gardes.

## Fiche de conception

### Question centrale

Les élèves maîtrisent-ils moins bien la langue française qu'avant, et que mesure-t-on vraiment quand on le dit ?

### Enjeu

Le diagnostic d'un déclin de la langue, centré sur les mots et imputé aux écrans, oriente des politiques (téléphone à
l'école, programmes) : le ministère attribue aux usages récréatifs du numérique « de graves conséquences » sur les résultats
(dossier de presse PISA 2025, lu par la relecture R1, l. 88). S'il est mal posé, il oriente mal l'action.

### Croyance initiale

Un déclin d'ensemble de la langue des élèves, d'abord lexical (« les jeunes n'utilisent plus que quelques centaines de
mots »), précipité par le smartphone.

### Découverte principale

La langue des élèves ne recule pas d'un bloc. À la même dictée de CM2, les erreurs passent de 10,7 à 19,4 de 1987 à 2021,
dont environ 0,9 seulement sur l'orthographe des mots (R1, l. 3 et 16-19 : CONFORME À LA SOURCE, NI 22.37 ; « environ » :
la NI 22.37 n'écrit pas la décimale nulle, lecture du « 3 » de 2021 plausible, non vérifiable dans ses données). Trois reculs précèdent
la généralisation du smartphone en 2013 : dictée de 1987 à 2007, lecture en CM2 de 1997 à 2007, temps de lecture pour le
plaisir à 15 ans de 2000 à 2009 (R1, l. 40 et 46-50 : CONFORME ; verdict T4). PISA, revenu en 2012 à un niveau proche de
celui de 2000 (sans écart significatif selon un test de l'auteur, plus enclin que celui de l'OCDE à trouver une baisse, ce
qui ne démontre pas une stabilité), recule ensuite ; sur des périodes qui recouvrent en partie cette baisse, CEDRE et PIRLS ne montrent pas de recul établi par
un test, quand les évaluations nationales de sixième et de seconde (depuis 2021) et de quatrième (depuis 2023), sans test
publié, reculent comme PISA (RS24, § 3, G2 : la généralisation tient à la lettre, la présentation omettait cet accord, P1-3).
Au collège et au lycée, aucune série publique recensée ne mesure l'étendue du vocabulaire ; la DEPP y compare des
compétences lexicales, en quatrième depuis 2024, en sixième et en seconde depuis 2025, sur deux ou trois années sans test
(RS24, P0-1 et § 3, G1 : portée exacte des séries) ; à l'école primaire, deux séries de la DEPP ne vont pas dans le même
sens (R2, P0-1 ; RS24, G7 ; DT 2026-E19 et E22).

### Mécanisme explicatif

La page n'établit aucun mécanisme causal : elle montre que des instruments différents (âge, compétence, enjeu, période,
population) mesurent des choses différentes, sans suivre les mêmes élèves (verdict T3, à deux niveaux ; R1, l. 62-63 :
CONFORME). Son seul raisonnement causal est négatif et borné : la généralisation du smartphone, en 2013, ne peut pas
expliquer l'apparition d'un recul déjà engagé avant elle (R1, l. 50 ; formulation resserrée le 25/11/2026 sur l'avis
concordant du juge interne et du contradicteur externe PRO-20261125-195657 : « pas la seule cause » laissait lire « une des
causes ») ; ses premiers usages, les autres écrans et ce qui a pu aggraver ces reculs ensuite restent ouverts. À la dictée, la hausse tient
surtout à des erreurs autres que lexicales, grammaticales sur la seule période détaillée, 1987-2007 (NI 08.38, tableau 4 ;
R1, l. 22). En fin de collège, un effet de répartition, établi par l'arithmétique des moyennes pondérées : les élèves « à
l'heure » et ceux en retard baissent tous deux significativement, la moyenne moins que chacun, la part des élèves en retard,
aux scores plus bas, ayant diminué (RS24, L. 122 et P2-6 ; données de la NI 22.29, figure 3 ; garde du générateur, qui
retrouve la moyenne publiée par la moyenne pondérée des deux groupes). Le poids des groupes ayant changé, rien ne garantit
que leurs élèves présentent les mêmes caractéristiques d'une enquête à l'autre : ces résultats n'établissent pas une baisse
à caractéristiques comparables, et la page ne lit pas la stabilité de la moyenne comme une baisse masquée (formulation du
contradicteur externe, plus prudente que celle du juge interne) (juge interne du 25/11, témoin chez le producteur : NI 08.38, lecture en CM2 de 1987 à
1997, « une légère baisse des résultats, équivalente dans les deux groupes […], alors que la moyenne générale est stable »).

### Preuve décisive

La frise des douze mesures (onze jusqu'au 26/11/2026 ; quatrième ajoutée avec le millésime 2026) face au repère de 2013, où chaque intervalle porte le verdict publié par le producteur (trait
plein) ou son absence (tirets) — recodée le 17/11/2026 pour PIRLS 2001-2011, test publié et non significatif (NI 12.21 ;
R1, P0-1 ; sonde S4) ; et la même dictée de 67 mots, décomposée entre erreurs lexicales et autres (NI 22.37, NI 08.38).

### Pouvoir discriminant

Explications rivales soutenues : (a) le smartphone, cause du recul (ministère, presse) ; (b) un déclin d'abord lexical
(chiffre des « 400 mots ») ; (c) la crise sanitaire. Le témoin qui ne change qu'une variable : la date de chaque recul par
rapport à 2013. Il écarte (a) comme explication de l'apparition des reculs antérieurs, sans rien dire des premiers usages
ni de ce qui a pu les aggraver ensuite ; la
décomposition de la dictée écarte (b) pour l'orthographe des mots (environ 0,9 erreur sur 8,7), sans rien dire du vocabulaire, et
les séries lexicales de la DEPP au collège et au lycée, de deux ou trois années, sans test, ne le départagent pas non plus
(RS24, conclusion interdite n° 8, dans les deux sens) ; aucune série ne départage (c), et la page le dit. Surprise informative : les reculs les plus anciens précèdent 2013.
Explications départagées : (a), seulement comme explication de l'apparition des reculs antérieurs. Robustesse : trois séries de deux
producteurs (DEPP, OCDE) et trois instruments. Levier : aucun ; la page borne un diagnostic, elle n'évalue pas une
politique.

### Limite

Les enquêtes mesurent des compétences évaluées par des épreuves, pas la pensée ; temps d'écran et de lecture sont
déclarés, et la non-réponse a presque doublé dans PISA 2025 ; les instruments ne sont pas comparables entre eux ; les
séries anciennes n'ont pas d'erreur type ; les évaluations exhaustives n'ont pas de test, et leur participation va de 81 % à
91 % en 2026, sans l'académie de Toulouse ; l'étendue du vocabulaire des adolescents n'a pas de série, et leurs compétences
lexicales ne sont comparées que sur deux ou trois années ; la correction de la dictée, centralisée à partir de 2007, a un
effet éventuel que la DEPP ne peut pas estimer directement ; aucune mesure ne dit si les
textes donnés à lire se sont simplifiés.

### Valeur finale

Le lecteur sait dire quelles compétences reculent, chez quels élèves et depuis quand ; il sait lire un chiffre sur la
langue par son instrument, sa population, sa période et sa significativité ; il dispose d'une chronologie qui borne
l'argument des écrans sans le trancher.

### Singularité

Cette page existe parce qu'elle place douze mesures de la langue face à la généralisation du smartphone et décompose une
même dictée sur trente-quatre ans, ce que le lecteur ne trouve ni dans les notes de la DEPP (une enquête à la fois), ni dans
le dossier de presse ministériel de PISA 2025, qui impute la baisse aux usages numériques (R1, l. 88), ni dans la chronique
de Franck Ramus, qui date la baisse de 2000 (R2, P2-2).

### Raccords

- Définition de l'anthropie : écartée — page de faits ; aucune lecture anthropique dans l'exposé des constats.
- Livre : retenu — *Livresque des mots*, bloc d'appel « Et si l'on rouvrait les livres par les mots ? » : le livre prend la
  question par la lecture, non par la mesure.
- Working paper : écarté — aucun AWP ne traite de la langue des élèves.
- Pages voisines : retenue — `/le-niveau-des-eleves-baisse-t-il/#evaluations`, « toutes les évaluations montrent-elles la
  même baisse ? », la question de la section cible (27/11/2026 : le libellé « pourquoi les évaluations ne montrent pas
  toutes la même baisse » promettait une explication que la page Niveau ne donne pas, « aucune de ces explications n'est
  testée ici ») ; la page Niveau renvoie vers `#ecrans`.

## Fiche D0

Écrite le 09/10/2026 (`D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`, « Hors étapes — ressource Langue ») :
résultat observé (reprises et citations de la page et de ses figures ; passages vers *Livresque des mots* ; passages entre
onglets du bloc), diagnostics (Search Console, téléchargements du jeu). Deux de ses critères d'infirmation se sont réalisés
et ont été traités à la reprise du 17/11/2026 : « une série de vocabulaire publiée par un producteur » (CP et CE1 depuis 2019,
DEPP) ; « une significativité publiée qui change un verdict de la frise » (PIRLS 2001-2011, NI 12.21). Le premier s'était
aussi réalisé au collège, sans être vu le 17/11 : la DEPP compare le lexique de quatrième depuis avril 2026 (DT 2025-E14),
puis celui de sixième et de seconde le 18/11/2026 ; traité à la reprise du 25/11/2026 (RS24, P0-1). Relevés J+30 et J+60
après la republication : à inscrire par la session de publication.

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait (17/11/2026).
- Protocole du type : fait (09/10/2026, `PROTOCOLE.md`, `VERDICT.md`) ; reprise du 17/11 : relecture des sources par deux
  relecteurs neufs (R1, R2) et douze sondes de la session à la source (S2 à S13), toutes conformes aux relecteurs.
- Scénarios d'architecture : fait (10/10/2026, refonte pilote, `PHASE_A_DIAGNOSTIC_ET_SCENARIOS.md`).
- Panel avant : fait (10/10/2026, `PANEL_LECTEURS_2026-10-10.md`).
- Contre-expertise de phase A : fait (PRO-20261009-202511).
- Gardes vues mordre : fait (53 gardes ; les cinq gardes ajoutées le 17/11 vues mordre par mutation).
- Figures téléphone : fait (versions `-m` ; frise régénérée le 17/11, `check-figures.py` à 0).
- Relecture de langue : phrases nouvelles du 17/11 relues dans la session de préparation (voir le lot).
- Recette 320-1280 (`recette.py`) : non fait à la reprise (motif : préparation sans publication) ; débordement mesuré de 320
  à 1 440 px par `captures.py` (0).
- Panel après : non fait (motif : la méthode de reprise écarte les lectures simulées de la page entière, § R5).
- Gate éditorial : remplacé, à la reprise, par le juge interne à l'aveugle (méthode de reprise, étape 10).
- Relecture phrase à phrase FR et EN : FR, phrases changées du 17/11 ; EN sans objet (page française seule).
- Instantané de relecture : non fait (motif : à refaire par la session de publication, sur le build publié).
- Contre-expertise de la page : paquet du jugement externe à l'aveugle préparé le 17/11/2026 ; réponse à venir.
- Accord de l'auteur : à venir.
- **Reprise du 25/11/2026** (lot `corrections-radar-2411`) : relecture des sources par un agent séparé, arbre figé (24/11,
  RS24 : 2 P0, 3 P1, 16 P2) ; sondes de la session : les valeurs du § 4 de RS24 relues par ancre dans six documents de la
  DEPP par l'extracteur complémentaire (25/11), toutes conformes ; gardes : 16 nouvelles (69 au total), 14 témoins de
  mutation vus mordre ; figures : inchangées (SVG identiques à l'octet, la frise reste au millésime 2025) ; contrôle de la
  lettre, `check-all --ci`, build, liens, rendu, dates : fait ; relecture de langue des 53 phrases servies nouvelles : faite ;
  juge interne à l'aveugle et contre-expertise externe : voir le lot ; publication : non (mode préparer).
- **Publication du 25/11/2026** : contre-expertise externe PRO-20261125-195657 arbitrée (20 décisions), puis arbitrage final
  du contradicteur (version proposée retenue, deux corrections localisées : PISA 2000-2012, l'absence d'écart significatif ne
  démontre pas une stabilité ; « environ » devant la part lexicale de la hausse, chapô, question fréquente, « Réutiliser »
  et carte de partage) ; repère du smartphone daté à chaque affirmation de la page ; description de la frise bornée à son
  dernier millésime (dessin inchangé) ; accord de l'auteur : demande de publication du 25/11 ; contrôles et instantané de
  relecture : voir le lot.
- **Correction du 26/11/2026** (contre-expertise PRO-20261126-121229, décisions de l'auteur L1, L2, L3) : la frise va
  jusqu'au millésime 2026 et trace douze mesures (sixième et seconde GT de 2021 à 2026, quatrième de 2023 à 2026, sans test
  publié), par le générateur, garde nouvelle vue mordre (mutation « sixième 2026 ») ; chapô et note de la figure de la
  dictée : correction centralisée à partir de 2007, effet éventuel non directement estimable selon la DEPP ; « en France »
  pour la passation de PISA sur ordinateur (NI 16.38 ; OCDE, *PISA 2018 Results*, vol. III). Premier écran retesté
  conforme ; figures : deux contrôleurs indépendants, deux passages ; ils ont fait lire 2026 sur la frise, porter la
  réserve de la dictée et le champ des évaluations de 2026 (hors académie de Toulouse) dans sa note, et trouvé que
  « l'indice de plaisir de lire ne baisse ni chez les filles ni chez les garçons » (2000-2009) taisait une hausse
  significative chez les garçons (OCDE, tableau II.B1.8.5 : +0,107, e.t. 0,039), relue dans le classeur archivé :
  corps, frise, texte alternatif et sources corrigés, garde réécrite et vue mordre ; contrôles : voir le lot.
- Forme du 26/11/2026 (point A15 du lot, demande de l'auteur) : la lecture à côté de la figure « plaisir » dépassait la
  figure de 215 px ; la dernière phrase (« Elle ne dit pas que les élèves perdent le goût de lire en grandissant… »)
  passe sous le bloc, sans changer une phrase ; la réserve qui qualifie le résultat (« des élèves différents la même
  année… pas une évolution ») reste à côté de lui. Mesure (`captures.py`, lecture contre figure) : +67 px, sous le seuil
  de 150 ; aucun débordement de 320 à 1 440 px. Texte servi inchangé, phrase pour phrase (instantané valable).
