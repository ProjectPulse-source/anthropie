# Wikidata — nombre de pages de *La Société du premier coup* et de *L'Odyssée des idées* (31 octobre 2026)

> ⏳ **À EXÉCUTER par Laura** (même procédure que le lot du 23/10). Puis relecture par l'API avant d'écrire « fait ».

## Pourquoi

Les deux items portent le nombre de pages d'une édition retirée :

| Item | Livre | Wikidata (relu par l'API le 31/10) | Broché en vente | Preuve |
|---|---|---|---|---|
| Q141072263 | *La Société du premier coup* | 138 | **140** (révision du 26/09) | PDF `03_LIVRES/premier-coup/03_LIVRABLES/PREMIER_COUP_BROCHE_FINAL.pdf` : 140 pages |
| Q138911733 | *L'Odyssée des idées* | 696 | **682** (édition corrigée du 28/09, même ISBN) | PDF `03_LIVRES/odyssee/03_LIVRABLES/odyssee_broche_interieur.pdf` : 682 pages |

Le site est corrigé dans le même geste (`data/works.yaml` et les pages des deux livres).

## Lot

`batch_quickstatements.txt` (retrait de l'ancienne valeur, puis ajout de la nouvelle) ; lien : `deeplink.txt`.

**Sans référence**, volontairement : la convention de la maison prend la page Amazon du broché comme référence (S854,
avec la date de consultation en S813), mais le nombre de pages qu'Amazon affiche n'a pas été relu le 31/10. Le
23/10, Amazon affichait encore l'ancien nombre pour *Anthropy*. Une référence s'ajoutera par un second lot, une fois
la page relue et conforme.

## Après exécution

Relire les deux items par l'API (`wbgetentities`, `props=claims`) : un seul P1104 par item, de valeur `+140` et `+682`.
Consigner la révision dans ce fichier. Un lancement « vert » sans écriture s'est déjà produit le 23/10.
