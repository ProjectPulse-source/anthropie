# Wikidata — Livresque des mots, édition CORR14 (2026-11-24)

> ⏳ **À EXÉCUTER par Laura QUAND amazon.fr affiche 678 pages** pour le broché (fiche https://www.amazon.fr/dp/2958634701,
> rubrique « Nombre de pages »). Téléversement KDP le 24/11/2026 ; mise en ligne sous 72 h environ. Avant, la référence
> Amazon dirait encore 680 : ne pas lancer.

Deux commandes, en **« Run »** (pas « Run in background »), en ouvrant `deeplink.txt` (jamais une copie du chat) :

1. `-Q140517745|P1104|680` — retire l'ancienne pagination (680 p., référence Amazon du 04/10/2026).
2. `Q140517745|P1104|678|S854|"https://www.amazon.fr/dp/2958634701"|S813|+2026-11-24T00:00:00Z/11` — pose 678 p.,
   même référence, consultée le jour de la mise en ligne (remplacer la date S813 par celle du constat si elle diffère).

État relu par l'API le 24/11/2026 avant ce lot : P1104 = 680 (déclaration `Q140517745$3E5D4669-…`, sources P854
amazon.fr/dp/2958634701 et P813 2026-10-04) ; aucun item ne porte l'ISBN du relié 978-2-9586347-9-7.

**Lot 2, plus tard** : l'édition reliée (ISBN 978-2-9586347-9-7, 540 p., 44,90 €) n'a pas d'item. À préparer quand le
relié est en vente (ASIN et date de publication connus) : item d'édition, P629 → Q140517745, P212, P1104 540, P50
Q138909233, P407 français, référence amazon.fr.

Relecture API à faire après passage, et `data/works.yaml` (pages 678) déjà à jour (commit du site du 24/11/2026).
