# Batches générés en attente de validation

Ce répertoire contient les fichiers `.qs` produits automatiquement par
`Wikidata/scripts/generate_wikidata_batch.py`.

**Chaque fichier doit être validé manuellement avant transmission à Laura.**

## Convention de nommage

- `awp-XX-YYYY-MM-DD.qs` : nouveau working paper
- `article-titre-tronqué-YYYY-MM-DD.qs` : nouvel article
- `book-ISBN-YYYY-MM-DD.qs` : nouveau livre

## Cycle de vie d'un fichier

1. Généré par le script (date du jour).
2. Validé visuellement par Stéphane.
3. Transmis à Laura (par email ou drive).
4. Exécuté par Laura via QuickStatements.
5. Une fois exécuté avec succès, peut être déplacé dans `executed/`
   (à créer manuellement si souhaité) ou archivé.

## Statut

Ne pas committer ce répertoire tant qu'une politique d'archivage n'est pas
décidée. Pour l'instant, fichiers en `.gitignore` recommandé.
