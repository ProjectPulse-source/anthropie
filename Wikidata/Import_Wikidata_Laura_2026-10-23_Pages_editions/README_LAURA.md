# Wikidata — nombre de pages des éditions révisées (23 octobre 2026)

> ✅ **FAIT le 2026-10-23, exécuté par Laura (15:01 UTC)** — relecture API du 23/10 (`readback_api_2026-10-23.json`) :
> Q138827344 (ANTHROPIE) révision 2560013383, un seul P1104 `+630` ; Q140645013 (ANTHROPY) révision 2560013393, un seul
> P1104 `+644`. Écriture en retour : déjà faite dans le site (`data/works.yaml`, fiches, commits `6b1cc4d` et `d16821e`).
> Incident : un premier lancement annoncé n'avait rien écrit (relecture API à 622 / 632, dernière révision au 03/09) ;
> relancé par Laura, puis relu.

Lot : `batch_quickstatements.txt`, lien : `deeplink.txt` (retrait de l'ancienne valeur, ajout de la nouvelle).

## Écarts ouverts

1. **Les deux nouvelles déclarations n'ont pas de référence** (convention de la maison : S854 page Amazon du broché,
   S813 date de consultation ; lot du 04/10). Le lot du jour ne l'ajoutait pas.
   - FR : Amazon.fr affiche « Nombre de pages de l'édition imprimée : 630 pages » (lu dans le navigateur le 23/10) →
     lot prêt : `batch_reference_FR.txt`, lien `deeplink_reference_FR.txt` (ajoute la référence à la déclaration
     existante, sans la dupliquer).
   - EN : **Amazon.fr affiche 632 pages** (23/10). L'auteur confirme le même jour que l'édition en ligne est la
     dernière (644 p.) et que ce champ, calculé par Amazon, est hors de sa main : **644 maintenu**. Pas de référence
     Amazon tant que la page contredit la valeur ; voie de correction : demande au support KDP.
2. **Descriptions KDP** : FR corrigée par l'auteur le 23/10, sans nombre de pages ; EN alignée le même jour
   (« A long history, 168 ways in »), sans nombre de pages. Réglé.

## Référence FR : premier lot sans effet, lot refait (23/10, soir)

Le lot « ajouter la référence à la déclaration existante » s'est terminé en vert dans QuickStatements **sans aucune
écriture** (relecture API : révision inchangée 2560013383, P1104 = 630 sans référence ; contributions de Laura : rien
après 15 h 01 UTC ; `readback_api_2026-10-23_reference.json`). Lot refait sur le modèle qui a fonctionné le 04/10 :
retrait de la déclaration, puis recréation avec sa référence (`batch_reference_FR.txt`, `deeplink_reference_FR.txt`).

> ✅ **Référence FR FAITE le 2026-10-23 (15:28 UTC, Laura)** — relecture API (`readback_api_2026-10-23_reference_2.json`) :
> Q138827344 révision 2560021572, un seul P1104 `+630`, référence S854 `https://www.amazon.fr/dp/2958634728` et S813
> `+2026-10-23`. Séquence : retrait 15:28:33, création 15:28:34, référence 15:28:36. Reste : EN sans référence tant
> qu'Amazon affiche 632.
