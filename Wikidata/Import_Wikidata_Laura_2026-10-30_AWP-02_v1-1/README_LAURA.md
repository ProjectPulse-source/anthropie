# Wikidata — AWP-02, version 1.1 (2026-10-30)

> ⏳ **À EXÉCUTER par Laura.** Au retour : bloc ✅ avec readback API (2 déclarations P953 nouvelles, qualifiées P407,
> aucune autre modification de Q139771990), le commit d'écriture en retour s'il y en a un (aucun attendu : le QID ne
> change pas) et la sortie de `python scripts/check-wikidata-registre.py`.

Laura — le working paper AWP-02 (*3,3 millions d'années en un principe : l'anthropie dans la longue durée*) a une
**version 1.1** publiée sur Zenodo le 30/10/2026, en français et en anglais : une correction de numérotation (la
conclusion, la figure 1 et la note du tableau 1 suivent désormais le tableau 1 et le plan du texte), rien d'autre.
L'item existe déjà : **Q139771990**. Il s'agit seulement d'y ajouter les deux pages Zenodo de la nouvelle version.

| | |
|---|---|
| Item | **Q139771990** (AWP-02, article scientifique, série Q139040913) |
| Ajout 1 | texte intégral (P953) `https://zenodo.org/records/23807981`, langue (P407) français (Q150) |
| Ajout 2 | texte intégral (P953) `https://zenodo.org/records/23807982`, langue (P407) anglais (Q1860) |
| Inchangé | le DOI (P356 `10.5281/ZENODO.19268037`, celui de la v1.0, qui reste valide) et le lien Zenodo de la v1.0 |

Pourquoi le DOI ne change pas : la propriété DOI n'admet en principe qu'une valeur par item, et le DOI de la v1.0
continue de désigner l'article. Les DOI de la v1.1 (FR 10.5281/zenodo.23807981, EN 10.5281/zenodo.23807982) sont
portés par les deux liens ajoutés ; le DOI de concept (FR 10.5281/zenodo.19268036) mène toujours à la dernière version.

## Comment faire

1. Ouvrir le lien du fichier **`deeplink.txt`** : il ouvre QuickStatements avec le lot chargé (2 lignes).
2. Vérifier d'être connectée, puis **« Run in background »** (pas « Run »). Le lot doit apparaître dans
   « Latest batches ».
   *(Repli : coller `batch_quickstatements.txt` en mode Import, en retirant les lignes `//`.)*
3. Prévenir Stéphane : rien d'autre n'est à renvoyer, le QID ne change pas.

Lecture préalable par l'API d'import (sans rien écrire), le 2026-10-30 : `status: OK`, **4 commandes** (2 déclarations
et leurs 2 qualificatifs de langue), sur `lot.txt`.
