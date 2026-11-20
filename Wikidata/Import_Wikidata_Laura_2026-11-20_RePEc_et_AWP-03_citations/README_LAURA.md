# Wikidata — identifiant RePEc de Stéphane et bibliographie d'AWP-03 (2026-11-20)

Laura — un lot en trois parties, **47 commandes** (lues sans écriture par l'API d'import le 20/11 : `status OK`).

1. **Identifiant RePEc** sur l'item de Stéphane (Q138909233) : `pla1203` (P2428), référence : sa page IDEAS
   `ideas.repec.org/f/pla1203.html`, consultée le 20/11/2026.
2. **Création d'un item** pour un article cité par AWP-03 qui n'en avait pas : Blanchard et Leigh, « Growth Forecast
   Errors and Fiscal Multipliers », *American Economic Review* 103 (3), 2013, DOI 10.1257/aer.103.3.117 (métadonnées
   relues chez Crossref). L'item existant du même titre (Q105877255) est le working paper du NBER, une autre œuvre.
3. **AWP-03** (Q139771991) : 13 liens « cite l'œuvre » (P2860) vers les œuvres de sa bibliographie v1.1 qui ont un item
   (référence : la version 1.1 sur Zenodo), et 2 sujets (P921) : finances publiques, austérité — deux des mots-clés de
   l'article, qui en porte déjà deux autres (anthropie, dette de l'État).

Les 23 autres références (rapports d'institutions, statistiques, articles sans item) ne sont pas liées : aucune n'a
d'item, et aucune n'est créée sans identifiant sérieux.

## Comment faire

1. Ouvrir le lien du fichier **`deeplink.txt`** (lot chargé, 30 lignes).
2. Vérifier d'être connectée, puis **« Run in background »** (pas « Run »). Le lot doit apparaître dans
   « Latest batches ».
   *(Repli : coller `batch_quickstatements.txt` en mode Import, en retirant les lignes `//`.)*
3. Prévenir Stéphane, avec **le QID du nouvel item** (affiché dans le lot) si possible ; sinon la relecture par l'API le
   retrouvera par son DOI.

Ce lot est indépendant de celui des nouvelles versions AWP-02/03/08 (même jour) : l'ordre importe peu.
