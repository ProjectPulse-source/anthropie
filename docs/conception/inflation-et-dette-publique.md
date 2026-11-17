# Fiche de conception — L'inflation a-t-elle vraiment allégé la dette française ?

<!-- Fiche écrite le 16/11/2026 pendant la reprise du lot « dette-a », APRÈS la relecture des sources :
LOTS\dette-a\SOURCES\inflation-et-dette-publique_R1.md (« R1 », lignes du texte servi). La page existait depuis le
07/10/2026 sans fiche ; celle-ci dit son état réel au 16/11. -->

Page : `/inflation-et-dette-publique/` (FR) · `/en/inflation-and-french-public-debt/` (EN) · ouverte le 2026-10-07 (fiche
écrite le 2026-11-16, après la relecture des sources)

## Forme

Données (`quantitatif`) et explicative (`explicatif-causal`), prolongement du dossier dette. Données : jeu
`dette_inflation` (JSON, CSV), jetons sans chiffre saisi, gardes vues mordre (dont `pal_pont`, 16/11), figures en SVG et
PNG avec version téléphone, Réutiliser, Dataset. Explicative : un contrefactuel explicite (inflation prévue contre
réalisée) et la séparation entre avantage brut et gain budgétaire net.

## Fiche de conception

### Question centrale

L'inflation de 2021-2023 a-t-elle allégé la dette de l'État, de combien, au profit de qui, et à quel coût ?

### Enjeu

« L'État a gagné 150 milliards grâce à l'inflation » circule ; c'est une érosion de la valeur réelle de paiements promis,
étalée jusqu'aux échéances, pas une recette, et les titres indexés et les achats de la banque centrale ont joué en sens
inverse. Confondre les deux fausse le débat sur qui a payé la dette.

### Croyance initiale

« L'inflation a effacé une partie de la dette » (gain budgétaire net).

### Découverte principale

L'inflation non prévue de 2021-2023 a réduit d'environ 150 milliards d'euros de 2020, en somme non actualisée, la valeur
réelle des paiements promis sur la dette négociable de l'État à taux fixe de fin 2020 (144 à 172 selon la prévision de
départ), un cinquième seulement fin 2023 ; c'est un avantage brut, non un gain net identifiable. Porté par R1 § 1 (l. 5,
21-28 : entrées relues à la source, IPCH, SPF, AFT ; recalculs indépendants) et R1 § 2, P2-2 (le résultat doit garder
« sans actualisation » et « négociable »).

### Mécanisme explicatif

Un paiement nominal fixé d'avance perd de la valeur réelle quand les prix montent plus que prévu ; la perte se réalise au
fil des paiements. Les titres indexés jouent en sens inverse (charge d'indexation en droits constatés, R1 § 2, P1-3) ; les
achats de la Banque de France, payés en réserves rémunérées au taux du moment, ont raccourci la durée de refixation de la
dette consolidée (R1 § 1, l. 64-70 ; P2-4 : la grandeur est une hausse de charge annuelle au bout d'un an).

### Preuve décisive

Le calcul ligne à ligne sur l'encours de l'AFT au 31/12/2020, dans deux mondes (inflation prévue, inflation réalisée),
avec quatre prévisions publiées entre novembre 2020 et février 2021 ; deux témoins publiés retrouvés (maturité des
émissions de l'AFT 2019-2020, durée de vie moyenne des bulletins, R1 bilan).

### Pouvoir discriminant

Rivales soutenues : « gain de l'État » (lecture courante) ; Pallotti et al. (NBER, gain brut plus large, et gain net
positif pour la France après coûts budgétaires, hors hausse des taux, R1 P1-2). Le rapprochement par périmètre,
valorisation et choc réduit l'écart avec leur chiffre d'environ les trois quarts (77 %, non 87 %, R1 P1-1 ; garde
`pal_pont`). Variantes calculées : quatre prévisions de départ, points morts d'inflation (sensibilité), actualisation de
−1 % à +1 %. Levier et risque rendus visibles : la sensibilité de la charge aux taux, accrue à court terme par les achats
de titres.

### Limite

Avantage brut sur un périmètre (dette négociable de l'État à taux fixe de fin 2020) ; l'effet net sur les recettes n'est
pas chiffré, faute, dans les travaux lus, d'une estimation causale comparable ; l'incidence finale de la perte reste
ouverte. Neuf lignes NON VÉRIFIÉES (R1 § 3).

### Valeur finale

Le lecteur sait ce que valent les 150 milliards (érosion brute, étalée, sur un périmètre) et ce qu'ils ne valent pas (une
recette, un gain net), et peut confronter les chiffres concurrents à leurs conventions.

### Singularité

Cette page existe parce qu'elle mesure, ligne à ligne sur l'encours de l'AFT, l'érosion par l'inflation non prévue et
son étalement dans le temps, que le lecteur ne trouve pas dans Pallotti et al. (choc instantané, valeur de marché, toutes
administrations), lus aux sections qui fondent ce qui en est dit (R1 P1-5).

### Raccords

Retenus : `/pourquoi-la-dette-publique-augmente/` (l'effet taux–croissance de 2021-2023 répond à toute la croissance
nominale ; le renvoi de cette page-là est réécrit) ; livre *Dette publique : qui paie vraiment ?* (bloc d'appel, l'inflation
comme l'un des payeurs). Écarté : la définition de l'anthropie (non mobilisée par le calcul).

## Fiche D0

Aucune fiche D0 trouvée pour cette page dans `D:\PRO\06_PROMOTION\FEUILLE_DE_ROUTE_GEO_RESSOURCES.md` (recherche du
16/11/2026 sur les adresses FR et EN). Résultat visé au plus près de la finalité : que les 150 milliards soient cités comme
une érosion brute et étalée, non comme un gain de l'État, par les lecteurs et les moteurs de réponse. État initial et
relevés : non faits (motif : préparation de nuit sans relevé des moteurs) ; à poser à la publication.

## Étapes de la méthode

- Plan d'outils : non fait dans cette reprise (outils déjà câblés) ; à lancer à la publication.
- Relecture des sources : fait (16/11/2026, R1, FR et EN : 0 P0, 5 P1 distincts, 12 lignes P2).
- Scénarios d'architecture : sans objet (organes existants).
- Panel avant : non fait ; premier écran testé par des lecteurs qui ne voient que lui (rapport du lot).
- Gardes vues mordre : fait (mutation `pal_pont`, 16/11 ; 43 gardes passées).
- Figures téléphone : fait (`--check`, parité des 4 figures).
- Relecture de langue : fait (`RAPPORTS\langue\`, aucun blocage).
- Recette 320-1440 : fait par `captures.py` (0 débordement) ; `recette.py` non lancé.
- Panel après, gate éditorial : non faits (préparation de nuit).
- Instantané de relecture : non fait (à refaire à la publication).
- Contre-expertise de la page : paquet du lot préparé le 16/11, à envoyer par l'auteur.
- Accord de l'auteur : non obtenu (préparation seule).
