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
téléphone) et un récit public de l'université abandonnée. Trois questions s'y mêlent, qui décident de choses
différentes : **qui souffre davantage** (les populations à cibler), **qu'est-ce qui explique l'écart** (les mécanismes
sur lesquels agir), **quelle intervention fonctionne** (prévention, aide financière, logement, soins). Se tromper de
population conduit à mal cibler ; se tromper de cause, à choisir une intervention inefficace ; mais l'origine d'un
trouble ne désigne pas le lieu du remède : un service de santé universitaire peut être utile pour une détresse née au
lycée (arbitrage de la pièce 01, 23/10/2026). L'enjeu concerne aussi les lycéens qui entrent dans le supérieur.

### Croyance initiale

Celle de la note reçue : massification de 1985 sans moyens, réformes qui fragmentent les études, smartphone, chocs du
covid, de l'inflation et du logement, absence de perspectives — six causes empilées qui produisent un « malaise étudiant
généralisé ». Et son contre-récit, celui de nos premiers avis : un malaise générationnel et mondial, à peu près
indépendant de l'université. La page les éprouve tous les deux.

### Découverte principale

Ni l'un ni l'autre ne tient tel quel. Trois niveaux d'énoncé gouvernent la rédaction :
- **établi** : de 2017 à 2021, l'épisode dépressif déclaré augmente dans chacune des situations publiées ; chez les
  étudiants, il passe de 10,1 % (2010) à 13,3 % (2017) puis 20,3 % (2021) : la hausse précède le covid, qui l'accélère ;
- **descriptivement établi** : la hausse ponctuelle est la plus forte chez les étudiants (+7 points, contre +5,3 chez
  les chômeurs et +4,4 chez les actifs occupés ; BEH 2023 n° 2, 18-75 ans, groupes de structures d'âge différentes) ;
- **non établi** : que cette progression excède celle de jeunes non étudiants comparables, et que l'excédent tienne aux
  conditions d'études. Les auteurs du BEH le disent eux-mêmes ; l'étude CONFINS (*BMJ Open*, 2021 ; en ligne, premier
  confinement, PHQ-9) trouve un risque plus élevé chez les étudiants après ajustement (rapport de cotes 1,58), sans
  représentativité nationale.
Deux témoins déplacent la question : les enquêtes ne détectent pas d'augmentation significative des états anxieux sur
la même période (BEH 2025 n° 14, autre instrument, autre fenêtre) ; et la dégradation est visible **avant le
supérieur** (EnCLASS : collégiens et lycéens, 2018-2022), avec en 2024 un bien-être qui remonte (+11 points au collège,
+12 au lycée) pendant que le risque important de dépression des lycéens continue de croître (18,9 %). Le « malaise »
n'est pas une grandeur unique. Hypothèse directrice, à mesurer : des vulnérabilités qui apparaissent à différents
moments de la jeunesse, et dont les études peuvent modifier l'intensité.

### Mécanisme explicatif

Deux familles de mécanismes, qui peuvent se combiner et ne s'excluent pas :
- **une question de sexe avant d'être de statut ?** L'écart le plus constant de toutes les sources est entre femmes et
  hommes (18-24 ans : +11,4 points contre +6,9 de 2017 à 2021 ; lycéennes 25,7 % contre lycéens 11,7 % de risque
  important de dépression en 2024) ; le supérieur étant majoritairement féminin, une part du « malaise étudiant » peut
  être celui des jeunes femmes — à tester par le croisement sexe × statut, jamais à affirmer ;
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
3. EnCLASS 2018-2022 et 2024 (Santé publique France, *Le point sur*, 02/06/2026) — lu le 23/10 par sources
   secondaires et communiqué : à relire dans le PDF avant chiffre.
4. Témoin de comptabilité des sources : chaque valeur OVE avec son enquête et son champ (fiche SIES n° 16, lue le 23/10
   dans l'archive du web, le site du SIES répondant 503) ; la dépense par étudiant dans la seule édition n° 19 du SIES.
5. **Témoin non déclaratif** (arbitrage de la pièce 01, pattern P1) : décès par suicide (CépiDc) et gestes
   auto-infligés aux urgences et à l'hôpital des 18-24 ans (Odissé, Santé publique France), traitements antidépresseurs
   des 20-24 ans (cartographie des pathologies, Assurance maladie). Il éprouve le récit de génération, pas l'écart
   étudiant (aucune de ces séries ne connaît le statut d'étudiant).

**Test décisif avant d'écrire la page** (modèle dette, discipline 4) : **l'écart des variations** entre étudiants et
jeunes non étudiants du même âge, avec son incertitude (ou l'interaction année × statut sous plan de sondage) — non
publié, demandé si l'auteur l'approuve, **sans suspendre la rédaction**. À défaut, la page s'écrit sur les trois niveaux
d'énoncé de la découverte principale, et le test manquant y figure comme résultat (« ce que les données publiques ne
permettent pas d'identifier »). Le test par recouvrement des intervalles de niveaux, écrit d'abord ici, est **retiré** :
des intervalles de niveaux ne disent rien d'une différence d'évolutions. Test décisif du scénario 3 : les séries non
déclaratives se prêtent-elles à la comparaison 2010-2023 (méthodologie lue, ruptures nommées) ? Sinon, le scénario 3
tombe.

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

Cette page existe parce qu'elle pose la même question à des sources de natures différentes — ce qu'on déclare
(enquêtes), ce qu'on soigne (traitements remboursés), ce qu'on fait (gestes auto-infligés, suicides) — et à deux témoins
(jeunes du même âge, lycéens), en disant pour chacune ce qu'elle permet d'identifier, ce que le lecteur ne découvre pas
dans les publications de l'OVE (étudiants seulement, vagues présentées à la suite), dans le BEH 2023 (qui pose la
question âge / statut et renvoie à des analyses complémentaires), dans CONFINS (un échantillon en ligne, un confinement)
ni dans le débat public, qui oppose le récit de l'université abandonnée à celui de la génération des écrans. Elle ne
prétend pas être la première à poser la question étudiants / non-étudiants (rectifié le 23/10, pièce 01). Lus :
synthèse MESR des enquêtes OVE, BEH 2023 n° 2 (discussion comprise) et 2025 n° 14, fiche SIES n° 16, CONFINS, EnCLASS
2024 ; **la revue de presse et des rapports reste à faire** avant de figer cette phrase, et la triangulation dépend des
séries non déclaratives, non encore extraites.

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
inexistante au 23/10/2026, aucune impression. Relevés : J+30 et J+60 après publication. **Critère de réussite
intellectuelle** (pièce 01) : la page rend vérifiable au moins une distinction que les synthèses ordinaires laissent
ambiguë — ce que les données représentatives permettent ou non d'identifier après contrôle de l'âge, et ce que les
séries non déclaratives confirment ou non du récit déclaratif. Une reprise par un journaliste, un enseignant ou un
chercheur est un résultat à observer, jamais une propriété déclarée avant publication. **À inscrire dans
`D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` avant publication** (non fait à ce jour : la page n'existe pas).

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : fait le 23/10 — retenus : MCP `sources` (séries Insee, OCDE),
  vérificateur de références (articles du BEH, *PNAS Nexus*, *Lancet*), `check_langue.py`, recette, panel, MAGNIFIER en
  finition.
- Forme et rattachement : fait le 23/10 — bloc `ecole`, élargi en « École, lycée et université » sur décision de
  l'auteur (en ligne, commit du site `c6e4b01`).
- Contre-expertise de phase A : faite et arbitrée le 23/10 (`PRO-20261023-180856`, audit fermé).
- Contre-expertise de la fiche (pièce 01, 23/10) : faite et arbitrée —
  `D:\PRO\06_PROMOTION\RECHERCHE_MALAISE_ETUDIANT_2026-10-23\ARBITRAGE_PIECE_01_2026-10-23.md` ; quatre corrections
  portées ici le même jour (enjeu, découverte en trois niveaux, test décisif, singularité).
- Protocole du type : en cours — lu : BEH 2023 (texte et discussion), BEH 2025 n° 14, CONFINS, EnCLASS 2024 (communiqué
  et reprises), fiche SIES n° 16. À lire avant le texte : figure 3 du BEH 2023 (PDF) ; BEH 2025 n° 14 (valeur étudiante) ;
  EnCLASS 2024 (PDF) ; série DEPP des bacheliers (`data.education.gouv.fr`) ; tableau rétrospectif du SIES n° 19 ;
  chômage des 15-24 ans (Insee, série longue) ; OVE 2024 (champ, sélection) ; Castelo et al. 2025 (durée, effectif) ;
  revue de presse.
- Bases nouvelles (arbitrage pièce 01, § 9) : joignables par API le 23/10 — Odissé (suicides, gestes auto-infligés,
  EDC régional), Assurance maladie (`effectifs`, traitements antidépresseurs par âge de cinq ans), SIES (réussite en
  licence, InserSup, logement Crous, enseignants), DEPP (bacheliers par génération) ; Eurostat EHIS par `sources`
  (ventilation « étudiants » à vérifier). Extraction non faite.
- Test décisif : non fait (écart des variations non publié ; demande à Santé publique France en attente de l'auteur) ;
  test du scénario 3 (méthodologies des séries non déclaratives) : non fait.
- Scénarios d'architecture : non fait — trois à écrire : 1, les sept séquences de la pièce 01 (paradoxe, premier
  témoin, deuxième témoin, avant la crise sanitaire, ce que les études ajoutent, réponses qui fonctionnent, frontière),
  six maillons en tableau de confrontation ; 2, « deux témoins » ; 3, « trois instruments » (déclarer, soigner, agir),
  si son test passe.
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
