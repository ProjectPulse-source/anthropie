# Wikidata, *Livresque des mots* (Q140517745) : sous-titre et nombre de pages

> ✅ **FAIT le 2026-09-17 (les deux lots)** — Q140517745 révision 2546908838 (05:52 UTC).
> Readback API du 17/09 (`readback_api_2026-09-17.json`, dans ce dossier) : **conforme** — un seul P1680,
> `fr`, « Anthologie inédite & éclectique de citations », référence amazon.fr + date du 17/09 ; un seul
> P1104, `+694`, référence amazon.fr. Écriture en retour : aucune (registre v1.20 et fiche déjà à 694 et
> au nouveau sous-titre, commit `50a324d`) ; `check-wikidata-registre.py` et `check-fiches-registre.py` à 0.
> ⚠ Le lot 2 est parti avant qu'amazon.fr affiche 694 pages (672 le 17/09 à midi) : la valeur est juste
> (édition acceptée par KDP), la référence le deviendra au déploiement Amazon.
>
> Historique : préparé le 17/09 ; exécuté par Laura le même jour.

Laura, deux corrections sur l'item du livre, sans création d'item.

## Pourquoi

L'édition brochée de *Livresque des mots* a été refaite (acceptée par KDP le 17/09/2026) : sommaire,
« Promenades dans le livre » et un **index des auteurs** en fin de volume. Deux données de l'item
deviennent fausses :

| Propriété | Sur Wikidata (lecture API du 17/09) | Valeur juste | Preuve |
|---|---|---|---|
| P1680 sous-titre | « Anthologie éclectique de citations » | « Anthologie inédite & éclectique de citations » | page de titre imprimée du livre et nouvelle couverture ; titre de la fiche amazon.fr relevé le 17/09 |
| P1104 nombre de pages | 672 | **694** | nouvelle édition brochée ; amazon.fr l'affichera à sa mise en ligne |

La lecture de l'item avant modification est dans ce dossier : `lecture_api_2026-09-17_avant.json`.

## Lot 1 : sous-titre (tout de suite)

Lien direct : `deeplink_lot1_soustitre.txt`. Il retire l'ancien sous-titre et pose le nouveau, en
français, avec sa référence (page amazon.fr, consultée le 17/09/2026).

## Lot 2 : nombre de pages (quand amazon.fr affiche 694 pages)

1. Ouvrir https://www.amazon.fr/dp/2958634701, section « Détails sur le produit » : vérifier
   **694 pages**. S'il est encore écrit 672, attendre, ne rien envoyer.
2. Lien direct : `deeplink_lot2_pages.txt`. Il retire 672 et pose 694, avec la page amazon.fr en
   référence.
3. Noter la date du jour de la vérification dans le bloc ✅ ci-dessus.

Le détail des deux lots, lisible, est dans `batch_quickstatements.txt`.

## Après exécution : relecture et écriture en retour

1. Relire l'item à l'API (`wbgetentities`, pas la page HTML) et poser le JSON dans ce dossier
   (`readback_api_<date>.json`) : un seul P1680, en `fr`, « Anthologie inédite & éclectique de
   citations » ; un seul P1104, `+694`.
2. Côté site, rien à changer : `data/works.yaml` et la fiche portent déjà 694 pages et le nouveau
   sous-titre (registre v1.20). Relancer `python scripts/check-wikidata-registre.py` et
   `python scripts/check-fiches-registre.py` à 0, puis ouvrir ce fichier sur un bloc ✅ (QID, révisions,
   sortie des deux scripts).
