# Arbitrage — complément sur le graphique « masses comparées » (29/09/2026)

**Pièce** : `D:\CONTRE_EXPERTISE\2026-09-29_GRAPHIQUE_DETTE\01_COMPLEMENT_GRAPHIQUE.txt`, SHA-256
`1038e62bc9441b1433d881d501e2555b61125fff4f8ac49190b38260fe645c6b`, archivée en lecture seule et
copie prouvée identique à la source **avant** lecture. **Objet** : la figure `masses-comparees`
de `/cout-de-la-dette-publique/`. **Canal** : audit de raisonnement, dépôt manuel.

## Verdict d'ensemble

Quatre demandes sur cinq sont retenues, dont trois appliquées telles quelles. La cinquième est sans
objet. La deuxième — passer « Ordre et sécurité » au bleu ardoise — est **rejetée sur le moyen et
retenue sur le diagnostic** : la pièce a vu le bon défaut et proposé le mauvais remède.

**Les onze chiffres avancés ont tous été vérifiés à la source** (Eurostat `gov_10a_exp`, FR, S13,
MIO_EUR, niveau II COFOG, millésime 2024) : hôpital 109,3 · ambulatoire 91,8 · produits médicaux
43,7 · total santé 261,2 ; primaire 42,2 · secondaire 63,8 · supérieur 12,3 · annexes 20,0. Écart
maximal avec la pièce : **0,0**. Les sommes se ferment exactement (261,2 = 261,2 ; 148,6 = 148,6).
Le creux de 2020 à **29,7 Md€** est confirmé par `data/dette_officielle.json`.

## Verdicts, point par point

| § | Proposition | Verdict | Motif |
|---|---|---|---|
| 1 | Décomposer santé et enseignement sous les étiquettes, en corps plus petit | **ACCEPTÉ**, avec une modification de méthode | les valeurs ne sont pas recopiées : sept codes de niveau II sont ajoutés à la requête Eurostat existante et le reste se calcule par soustraction, ce qui **ferme la somme par construction**. La règle de surface du dépôt l'impose — « toute valeur dérivable se dérive ; la recopier, c'est programmer sa dérive ». Recopiés, ces onze chiffres se seraient figés au millésime du jour où on les a lus |
| 1b | Ne pas écrire « réellement consacrés aux soins » | **ACCEPTÉ** | une qualification normative là où la décomposition factuelle suffit |
| 2 | « Ordre et sécurité » en bleu ardoise `#58748A` | **DIAGNOSTIC ACCEPTÉ, REMÈDE REJETÉ** | voir ci-dessous |
| 3 | Marquer le creux de 2020 sur la courbe orange | **ACCEPTÉ** | c'est la meilleure des propositions : « +102 % depuis 2020 » cessait d'être une assertion à croire pour devenir une lecture — 30, puis 60. La valeur et l'année sont **calculées** (`ref` est déjà le minimum de la série), jamais écrites à la main |
| 4 | Titre autosuffisant : « France · administrations publiques · milliards d'euros courants » | **ACCEPTÉ** | la figure est offerte en ressource réutilisable ; hors de la page, « France » et « administrations publiques » n'étaient plus déductibles. Appliqué FR et EN |
| 5 | Conserver la note méthodologique en la raccourcissant | **SANS OBJET** | la note affichée n'est pas `LABELS_MASSES["note"]` mais la précaution `C["masses"]`, qui porte **déjà en tête** la phrase que la pièce juge essentielle : « Les intérêts sont une nature de dépense, les trois autres des fonctions ». Rien à raccourcir. En revanche `LABELS_MASSES["note"]` n'était **lu par aucun appelant** — champ mort, vérifié par grep, **retiré** : deux formulations pour la même note auraient divergé |

## Le point 2 en détail : bon défaut, mauvais remède

**Ce que la pièce a vu juste** : cette quatrième série « paraît presque accessoire alors qu'elle est
la comparaison la plus spectaculaire avec les intérêts ». C'est exact, et la cause est plus précise
qu'elle ne le dit : la courbe était tracée en `AXIS` (`#c3c2b7`), **la couleur de l'axe des
abscisses**. Une série de données partageait la teinte d'un élément de structure ; elle se lisait
comme du quadrillage.

**Pourquoi le bleu est refusé**, trois raisons qui se cumulent :

1. **La charte de l'auteur** (28/09) fixe deux couleurs de données, et leur donne un sens : bleu
   profond `#184f95` = stock, orange `#eb6834` = coût. Les quatre séries de cette figure sont des
   **dépenses** — la même grandeur. « La même grandeur toujours de la même couleur » : un bleu y
   introduirait une distinction sémantique qui n'existe pas.
2. **La docstring de la figure protège un invariant** que la pièce ignore : « budgets en gris de
   valeurs différentes : la hiérarchie tient sans la couleur (**test du noir et blanc**) ». En
   niveaux de gris, `#58748A` et le gris moyen de l'enseignement se confondraient — la hiérarchie
   reposerait alors sur la couleur seule.
3. **Une teinte neuve doit passer `validate_palette.js`** avant application, et le bleu marine du
   site y échoue déjà comme couleur de données (chroma trop faible, il lit gris). `#58748A` n'a
   aucune raison d'y réussir mieux.

**Ce qui est appliqué à la place** : une valeur de gris supplémentaire, `CTX3 = #a5a39a`, entre le
gris moyen et celui de l'axe. Elle sépare la donnée de la structure **sans introduire de seconde
couleur de données**, et le test du noir et blanc reste satisfait. Le libellé et la courbe passent
ensemble à cette valeur, comme la pièce le demandait pour le bleu.

## Ce qui a été fait en plus, et pourquoi

- **Gardes de cohérence sur les nouveaux postes**, dans la section des gardes dures, donc **avant
  toute écriture**. Elles ne portent pas sur des bandes absolues en euros — une part du total ne
  dérive pas avec l'inflation — mais sur la **part de chaque poste dans sa fonction**, et sur le
  reste, qui doit rester positif. C'est ce qui arrêterait une inversion de code ou un poste devenu
  aberrant. Passées au `--check` du 29/09.
- **Équilibrage des deux lignes de décomposition par longueur de texte**, non par nombre de postes :
  au premier rendu, « secondaire 64 · primaire 42 · supérieur 12 » débordait la marge tandis que la
  ligne suivante restait à moitié vide. Mesuré sur le rendu, corrigé, re-mesuré.
- **Marge droite élargie** de 168 à 196 px pour les lignes de détail.

## Contrôles

Figure construite hors dépôt et **regardée**, FR et EN, avant toute écriture (harnais isolé, aucune
donnée du dépôt modifiée). Séparateur décimal vérifié **dans le SVG** et non à l'œil sur un PNG
redimensionné : « 29,7 » en français, « 29.7 » en anglais. `update_dette_insee.py --check` : gardes
passées, rien écrit. `check-all.py --ci` : quatre contrôles à 0. Aucune **sortie nouvelle** n'est
créée — la liste énumérée du workflow `dette-insee.yml` reste donc valable, et la garde interne du
script qui compare ses sorties à cette liste n'a rien à signaler.

## Ce qui reste NON_VÉRIFIÉ

Rien de ce qui est appliqué. La pièce ne cite aucune source hors Eurostat, et les valeurs Eurostat
ont été relues à la source.
