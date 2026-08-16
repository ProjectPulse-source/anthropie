# Import Wikidata — création de l'item « Livresque des mots » (2026-07-09)

Laura — ton import du lot `Import_Wikidata_Laura_2026-07-06` est **vérifié
conforme à 100 %** (contrôle par API le 09/07 : les 7 points du README sont
verts, l'item AWP-07 créé est impeccable — Q140446195). Merci !

Il reste **un dernier fichier** : celui-ci. Deux choses :

1. **Créer l'item du livre « Livresque des mots »** — c'est le seul des
   4 livres sans item Wikidata ;
2. **Ajouter AWP-07 aux œuvres notables** de la fiche personne (une ligne).

## Procédure (identique au lot précédent)

1. https://quickstatements.toolforge.org → *Log in* → **New batch**.
2. Ouvrir `batch_quickstatements.txt`, supprimer les lignes `//`
   (Notepad++ : regex `^//.*\r?\n` → rien). Il doit rester **20 lignes** :
   1 `CREATE`, 18 `LAST`, 1 `Q138909233`.
3. Coller dans l'onglet **V1 commands** → *Import V1 commands* → vérifier :
   la ligne CREATE apparaît comme création, aucune ligne rouge.
4. *Run* (ou *Run in background*).

## Vérifications post-import (3 minutes)

| Où | Quoi |
|---|---|
| Item créé (clic sur la ligne CREATE du journal) | Label « Livresque des mots » FR+EN ; description « anthologie éclectique… (2022 ; 3e édition 2026) » ; ISBN 978-2-9586347-0-4 ; 672 pages ; ASIN **2958634701** ; OpenLibrary OL45424544W ; sous-titre « Anthologie éclectique de citations » |
| [Q138909233](https://www.wikidata.org/wiki/Q138909233) | P800 contient désormais Q140446195 (AWP-07) |

## Post-import manuel (2 gestes)

1. **Renvoyer à Stéphane le QID créé** (Qxxxxxxxxx) — il alimente
   works.yaml et la fiche du site.
2. Sur [Q138909233](https://www.wikidata.org/wiki/Q138909233), ajouter à la
   main : **P800 (œuvre notable) = le QID créé** (QuickStatements ne peut
   pas référencer un item créé dans le même batch).

Ne PAS lier ce livre au concept anthropie (il est hors corpus — même
logique que le site). Aucune autre modification.
