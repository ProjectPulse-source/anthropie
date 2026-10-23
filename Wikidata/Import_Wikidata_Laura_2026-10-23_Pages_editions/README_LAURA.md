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
   - EN : **Amazon.fr affichait encore 632 pages le 23/10** (détails et description) : pas de référence tant que la page
     ne montre pas 644. Si elle ne le montre pas d'ici le 26/10, vérifier dans KDP que l'édition révisée est bien
     publiée ; si non, revenir à 632 sur Wikidata et sur le site.
2. **Descriptions KDP périmées** (texte du produit, geste de l'auteur dans KDP) : FR « Sept âges, 168 jalons, 622 pages » ;
   EN « Seven ages, 168 milestones, 632 pages ».
