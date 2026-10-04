# Wikidata — nouvel item AWP-09 (2026-10-04)

> ✅ **ITEM CRÉÉ le 2026-10-04 par Laura : Q141641858.** Readback API le jour même : **14 déclarations**, exactement
> celles du lot (P31, P50 réf., P356 réf. `10.5281/ZENODO.23143030`, P407, P577, P921 ×2, P361, P2860 ×2, P953 ×4
> qualifiés), libellés et descriptions FR/EN conformes, aucun effet de bord.
> Écriture en retour : `data/works.yaml` (`wikidata: "Q141641858"`) et `wikidata_qid` des fiches `awp-09.md` /
> `awp-09.en.md` (même commit que ce bloc) ; `sameAs` présent dans les deux pages construites ;
> `check-fiches-registre.py` 0 divergence ; `check-wikidata-registre.py` : 23 items ↔ 23 QID, OK.
>
> ⏳ **RESTE : rétro-liens** — `deeplink_retroliens.txt` (2 commandes, lues sans erreur par l'API d'import :
> série Q139040913 P527 et auteur Q138909233 P800 → Q141641858). Avant envoi, la série compte 8 valeurs P527 ;
> attendu après : 9. Readback à écrire ici.

Laura — un nouveau working paper est publié aujourd'hui, en français et en anglais, à créer sur Wikidata au
même patron que les AWP précédents (un item par AWP, article scientifique, rattaché à la série).

| | |
|---|---|
| Titre FR | **Ce que les comptes publics permettent d'établir sur le déplacement de la charge de la dette — Identités comptables, témoins indépendants et limites (France, 1995-2025)** |
| Titre EN | What Public Accounts Can Establish about the Displacement of the Public Debt Burden — Accounting Identities, Independent Benchmarks, and Limits (France, 1995-2025) |
| Auteur | Stéphane Lalut (**Q138909233**) |
| Série | Anthropie Working Papers (**Q139040913**), n° 9 |
| DOI (FR, canonique) | **10.5281/zenodo.23143030** |
| Zenodo EN (isDerivedFrom) | 10.5281/zenodo.23145963 |
| Sujets | anthropie (Q138827949) ; dette publique de la France (Q3024794) |
| Cite | AWP-03 (Q139771991), AWP-01 (Q139771989) |
| Publication | 2026-10-04 · Licence CC-BY 4.0 |
| Pages site | https://stephane-lalut.com/awp/awp-09/ · /en/awp/awp-09/ |

## Comment faire

1. Ouvrir le lien du fichier **`deeplink.txt`** : il ouvre QuickStatements avec le lot chargé.
2. Vérifier d'être connectée, puis **« Run in background »** (pas « Run » : le 04/10, un lot lancé par « Run »
   a tourné sans rien écrire). Le lot doit apparaître dans « Latest batches ».
   *(Repli : coller `batch_quickstatements.txt` en mode Import, en retirant les lignes `//`.)*
3. **Noter le QID créé** et l'envoyer à Stéphane.
4. **Rétro-liens** : Stéphane te renverra un second lien (2 lignes) une fois le QID connu :
   série « a pour partie » l'AWP-09, auteur « œuvre notable » l'AWP-09.

> Item FR-canonique, comme les AWP précédents : DOI FR en P356, édition anglaise via les liens texte intégral
> qualifiés (P953 + P407 anglais). Ne pas créer d'item séparé pour l'édition anglaise.

Merci !
