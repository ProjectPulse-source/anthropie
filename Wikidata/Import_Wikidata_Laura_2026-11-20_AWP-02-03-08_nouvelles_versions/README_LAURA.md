# Wikidata — nouvelles versions d'AWP-02, AWP-03 et AWP-08 (2026-11-20)

> ✅ **EXÉCUTÉ — dossier clos (2026-11-21).** Les six liens des nouvelles versions sont en place avec leur langue, relus
> par l'API le 21/11 : Q139771990 (AWP-02) `24368734` français, `24368735` anglais ; Q139771991 (AWP-03) `24368736`
> français, `24368737` anglais ; Q140680750 (AWP-08) `24364809` français (posé le 21/11 par le lot
> `Import_Wikidata_Laura_2026-11-21_corrections`, révision 2573095613), `24364810` anglais. Le 20/11, plusieurs passages
> partiels : adresses coupées par une espace au copier-coller depuis le chat ; « Run in background » qui écrit en
> parallèle sur un même item. Leçon : ouvrir le fichier, jamais une copie ; un lot de déclarations avec qualificatifs se
> passe en « Run ». Écriture en retour : aucune (les QID ne changent pas).

Laura — trois working papers ont une nouvelle version publiée sur Zenodo le 19/11/2026, en français et en anglais
(corrections de sources et de références). Les items existent déjà ; il s'agit seulement d'y ajouter les pages Zenodo
des nouvelles versions, comme le 30/10 pour AWP-02.

| Item | Œuvre | Ajouts (texte intégral P953, langue P407) |
|---|---|---|
| **Q139771990** | AWP-02, v1.2 | `zenodo.org/records/24368734` (français Q150) ; `…/24368735` (anglais Q1860) |
| **Q139771991** | AWP-03, v1.1 | `zenodo.org/records/24368736` (français) ; `…/24368737` (anglais) |
| **Q140680750** | AWP-08, v1.1 | `zenodo.org/records/24364809` (français) ; `…/24364810` (anglais) |

Inchangé : le DOI de chaque item (P356, celui de la v1.0, valeur unique, qui continue de désigner l'article) et les
liens existants. État relu par l'API le 20/11 (lecture seule) : aucun des six liens n'est encore présent.

## Comment faire

1. Ouvrir le lien du fichier **`deeplink.txt`** : il ouvre QuickStatements avec le lot chargé (6 lignes).
2. Vérifier d'être connectée, puis **« Run in background »** (pas « Run »). Le lot doit apparaître dans
   « Latest batches ».
   *(Repli : coller `batch_quickstatements.txt` en mode Import, en retirant les lignes `//`.)*
3. Prévenir Stéphane : rien à renvoyer, les QID ne changent pas. Une relecture par l'API confirmera ensuite les
   12 commandes (6 liens et leurs 6 qualificatifs de langue).
