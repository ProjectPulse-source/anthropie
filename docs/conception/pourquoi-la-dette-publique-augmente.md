# Fiche de conception — Pourquoi la dette publique augmente-t-elle ?

<!-- Fiche écrite le 16/11/2026 pendant la reprise du lot « dette-a » (méthode de reprise, § R2), APRÈS la relecture des
sources : LOTS\dette-a\SOURCES\pourquoi-la-dette-publique-augmente_R1.md (« R1 » ci-dessous, lignes du texte servi). La
page existait depuis le 30/09/2026 sans fiche ; celle-ci dit son état réel au 16/11, pas un état souhaité. -->

Page : `/pourquoi-la-dette-publique-augmente/` (FR) · `/en/why-does-public-debt-rise/` (EN) · ouverte le 2026-09-30 (fiche
écrite le 2026-11-16, après la relecture des sources)

## Forme

Données (`quantitatif`) et explicative (`explicatif-causal`). Données : jeu `dette_dynamique` (JSON, CSV), jetons sans
chiffre saisi, gardes vues mordre, figure signature en SVG et PNG avec version téléphone, Réutiliser, Dataset. Explicative :
la page sépare ce que l'identité comptable établit (la contribution de chaque terme) de ce qu'elle n'établit pas (la cause
des déficits), et confronte chaque lecture publique à l'objet qu'elle examine.

## Fiche de conception

### Question centrale

D'où vient la hausse de la dette publique française, qui a doublé en part de PIB depuis 1995 (57,9 points de fin 1995 à
fin 2025, R1 § 2) : des intérêts, de la croissance, des déficits hors intérêts, ou d'opérations qui ne passent pas par le
déficit ?

### Enjeu

Le débat public attribue la hausse tantôt aux taux d'intérêt (audit citoyen de 2014), tantôt à la dépense (direction
générale du Trésor), tantôt aux baisses de prélèvements (OFCE), tantôt aux crises (Note du CAE). Chaque lecture fonde une
politique différente. Une décomposition comptable sur la série harmonisée dit ce que chaque terme a apporté et à quelle
période ; elle ne dit pas quelle décision a creusé les déficits, et la page doit le dire avec la même netteté.

### Croyance initiale

« La dette augmente à cause des intérêts » (effet boule de neige), ou, en sens inverse, « la dépense publique a explosé ».

### Découverte principale

Sur trente ans, intérêts et croissance nominale se sont presque annulés, en deux périodes opposées (taux implicite
au-dessus de la croissance nominale jusqu'à la bascule, en dessous ensuite) ; les déficits primaires apportent l'essentiel
de la hausse, 50,5 des 57,9 points. Porté par R1 § 0 (recalcul indépendant sur les séries brutes d'Eurostat du 21/10/2026,
qui redonne toutes les valeurs de la décomposition) et R1 § 2, P2 l. 349 (« les déficits primaires en apportent
l'essentiel : 50,5 des 57,9 points »). Le déficit corrigé du cycle n'est pas né des crises : il existe dès 2002 selon les
trois producteurs (R1 § 2, P1 l. 89-92 : FMI, Commission, OCDE, 2007 à −1,7, −1,9 et −2,0 % du PIB potentiel).

### Mécanisme explicatif

L'identité de la dynamique de la dette : la variation du ratio égale l'effet taux–croissance (taux implicite moins
croissance nominale, appliqué au ratio de l'année précédente), plus le déficit primaire, plus les ajustements flux-stock.
L'effet taux–croissance est positif tant que le taux implicite dépasse la croissance nominale et négatif ensuite ; le
déficit primaire ajoute chaque année sa valeur en points de PIB. R1 § 1 (statuts CONFORME À LA SOURCE et CONFORME AU CALCUL
SEUL des l. 16-40) et § 2, P1 l. 315 : la condition de baisse par l'inflation est une croissance nominale supérieure au
taux implicite, non une croissance du PIB plus rapide que la charge (2021-2022 : charge +17 % puis +46 %, ratio en baisse).

### Preuve décisive

La décomposition reproduit les ratios publiés par Eurostat (témoin qui a rejeté une erreur de convention, AWP-09), et le
calcul des mesures nouvelles retrouve la décomposition 2017-2022 de la Cour des comptes à 0,15 point près (garde bloquante
du générateur, l. 352).

### Pouvoir discriminant

Rivales réellement soutenues : les taux (audit citoyen de 2014, « un gros tiers » de la hausse 1980-2012), la dépense
(direction générale du Trésor, depuis 2019), les baisses de prélèvements (OFCE, depuis 2017), les crises (Note du CAE). Ce
que révèle le graphe qu'une série isolée ne montre pas : la quasi-annulation de l'effet taux–croissance sur trente ans,
en deux périodes de signe opposé. Ce qu'il départage : sur la période commune avec l'audit (1995-2012), l'effet
taux–croissance pèse 14,7 points sur 33,9 et ne passe devant les déficits primaires que si l'on isole les flux-stock (R1
§ 2, P1 l. 262) ; « dépenses ou recettes » dépend de la fenêtre comparée, et la page le montre au lieu de trancher.
Variantes calculées : trois estimations du solde corrigé du cycle (FMI, Commission, OCDE), sans moyenne. Levier : le solde
primaire structurel ; contrainte : le taux implicite repasse en 2025 légèrement au-dessus de la croissance nominale.

### Limite

Décomposition comptable, pas causale : elle ne dit pas quelles décisions ont creusé les déficits. Le solde corrigé du cycle
repose sur une estimation de la production potentielle, révisable. Les mesures nouvelles sont chiffrées par
l'administration ; la convention de ce chiffrage reste NON VÉRIFIÉE (R1 § 3, note du HCFP non lue).

### Valeur finale

Le lecteur sait quelle part chaque terme a apportée, à quelle période, et sur quel objet portent les lectures concurrentes ;
il peut réutiliser la série et la figure avec leurs réserves.

### Singularité

Cette page existe parce qu'elle révèle, sur la série harmonisée d'Eurostat, les deux périodes opposées de l'effet
taux–croissance et la part propre des ajustements flux-stock, que le lecteur ne découvre pas dans la Note du CAE n° 82
(1970-2023, déficits et flux-stock réunis, effet boule de neige proche de zéro en moyenne), lue (R1 § 0).

### Raccords

Retenus : `/dette-publique-peut-elle-baisser/` (même identité, autre question) ; `/inflation-et-dette-publique/` (renvoi
réécrit : « mesure autre chose », R1 P1 l. 40) ; working paper AWP-09 (méthode et témoin, DOI cité) ; livre *Dette
publique : qui paie vraiment ?* (bloc d'appel). Écarté : la définition de l'anthropie (la page est comptable ; aucun
déplacement de coût n'y est mesuré).

## Fiche D0

Fiche D0 existante : `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md`, entrée de la page (l. 237 au 16/11/2026) :
objet, requêtes cibles et relevés. Résultat visé au plus près de la finalité : que la page soit citée avec sa réserve
(décomposition comptable, non causale) par les moteurs de réponse et par les lecteurs du débat. Relevé suivant : à la
publication de la version reprise.

## Étapes de la méthode

- Plan d'outils (`outils_du_produit.py ressource`) : non fait dans cette reprise (outils déjà câblés sur la page) ; à lancer
  à la publication.
- Protocole du type, relecture des sources : fait (16/11/2026, R1, 395 lignes FR et 401 EN, 177 entrées : 0 P0, 7 P1, 14 P2).
- Scénarios d'architecture : sans objet (reprise dans les organes existants).
- Panel avant : non fait (reprise sans changement de structure) ; premier écran testé par des lecteurs qui ne voient que lui
  (voir le rapport du lot).
- Gardes vues mordre : fait (mutations `fmi_signe` et `sfa_2009` du générateur, 16/11).
- Figures téléphone : fait (`--check` du générateur, parité des figures).
- Relecture de langue : fait (`RAPPORTS\langue\`, aucun blocage).
- Recette 320-1440 : fait par `captures.py` (0 débordement, lecture contre figure conforme) ; `recette.py` non lancé.
- Panel après, gate éditorial : non faits (préparation de nuit).
- Instantané de relecture : non fait (à refaire à la publication).
- Contre-expertise de la page : paquet du lot préparé le 16/11, à envoyer par l'auteur.
- Accord de l'auteur : non obtenu (préparation seule).
