# Wikidata — corrections du 2026-11-21

> ✅ **EXÉCUTÉ par Laura le 2026-11-21 (08:38-08:39 UTC). Dossier clos.** Relecture API le jour même : source
> `zenodo.org/records/24368737` posée sur AWP-03 P2860 → Q142233801 (révision 2573095460) ; Q140680750 P953
> `zenodo.org/records/24364809` avec P407 Q150 (révisions 2573095537 et 2573095613).

Deux commandes, à lancer en **« Run »** (pas « Run in background »), en ouvrant `deeplink.txt` (jamais une copie du chat).

1. `Q139771991|P2860|Q142233801|S854|"https://zenodo.org/records/24368737"` — ajoute la source (AWP-03 v1.1 sur
   Zenodo) au lien « cite l'œuvre » d'AWP-03 vers l'article de Blanchard et Leigh (2013), item créé le 21/11 par le lot
   `Import_Wikidata_Laura_2026-11-20_RePEc_et_AWP-03_citations` : la déclaration existe, sa source n'a pas été posée
   (QuickStatements pose mal une source sur une déclaration qui vise un item créé dans le même lot).
2. `Q140680750|P953|"https://zenodo.org/records/24364809"|P407|Q150` — lien AWP-08 v1.1 français, **consigne de
   l'auteur** (échec répété le 20/11 ; bloc 🔴 du `README.md` de la navette).

État relu par l'API le 21/11 avant ce lot : lot du 21/11 (RePEc + AWP-03) entièrement passé sauf la source du point 1 ;
AWP-08 français absent. Relecture API à faire après passage.
