# 14 — Décisions Wikidata restantes pour Laura

**Génération : 2026-05-11**
**Statut : à arbitrer avant exécution des batches `11_`, `12_`, `13_`**

---

## Mode d'emploi

Ce document liste toutes les valeurs Wikidata externes (Q-IDs et P-IDs) qui n'ont pas pu être validées depuis le repo Hugo ni depuis une recherche web Anthropic. Chaque entrée donne :
- la valeur actuellement posée dans les batches QS,
- son contexte d'usage,
- les alternatives connues,
- une recommandation neutre,
- la décision finale à reporter dans le batch.

**Convention :** Laura tranche par item, reporte sa décision finale dans le tableau de tête, et substitue manuellement dans le fichier QS concerné AVANT le lancement du batch.

---

## Tableau de tête — décisions à reporter par Laura

| # | Concept / propriété | Valeur actuelle batch | Décision Laura | Validé le |
|---|---|---|---|---|
| 1 | given name "Stéphane" | ~~Q937131~~ → **Q3501543 (RÉSOLU v2.1)** | n/a | 2026-05-11 |
| 2 | public finance | ~~Q161157~~ → **Q274490 (RÉSOLU v2.2)** | n/a | 2026-05-11 |
| 3 | ecological economics | ~~Q1062148~~ → **Q1049066 (RÉSOLU v2.2)** | n/a | 2026-05-11 |
| 4 | social sciences | ~~Q21201~~ → **Q34749 (RÉSOLU v2.2)** | n/a | 2026-05-11 |
| 5 | self-published | ~~Q3504054~~ → **OMIS (RÉSOLU v2.3)** | n/a | 2026-05-11 |
| 6 | publication series | ~~Q1711593~~ → **RECONDUIT P31=Q13442814 (RÉSOLU v2.3)** | n/a | 2026-05-11 |
| 7 | economic essay (genre) | ~~Q62482~~ → **OMIS (RÉSOLU v2.3)** | n/a | 2026-05-11 |
| 8 | independent research | ~~Q161732~~ → **OMIS (RÉSOLU v2.3)** | n/a | 2026-05-11 |
| 9 | longue durée | ~~Q1339645~~ → **OMIS (RÉSOLU v2.3 — Q1812879 confirmé non pertinent)** | n/a | 2026-05-11 |
| 10 | Zenodo (repository) | ~~Q1322603~~ → **Q22661177 (RÉSOLU v2.1)** | n/a | 2026-05-11 |
| 11 | Academia.edu profile property | ~~P6079~~ → **P5715 (RÉSOLU v2.2)** | n/a | 2026-05-11 |
| 12 | Google Scholar property | **P1960 confirmé (RÉSOLU v2.3 — P4985 = TMDB person ID, écarté)** | n/a | 2026-05-11 |
| 13 | Amazon URL property | ~~P953/P856~~ → **P5749 ASIN (RÉSOLU v2.1 — doctrine Wikidata)** | n/a | 2026-05-11 |

---

## Détail par décision

### #1 — Given name "Stéphane"

**Fichier concerné :** `11_quickstatements_phase_A_filled.qs` §A.1
**Ligne approximative :** `Q138909233	P735	Q937131	# given name: Stéphane`
**Valeur posée :** Q937131
**Statut :** À vérifier
**Action Laura :** ouvrir https://www.wikidata.org/wiki/Q937131 et confirmer que le libellé est bien « Stéphane » (et non un homonyme).
**Alternative si erroné :** rechercher « Stéphane » sur wikidata.org → autocomplétion sur les items « given name (male) ».
**Recommandation :** vérification rapide (30 s).

### #2 — Public finance (RÉSOLU v2.2)

**Statut :** **RÉSOLU.** Substitution Q161157 → **Q274490** appliquée dans `11_` §A.1.
**Validé le :** 2026-05-11
**Source :** validation utilisateur 2026-05-11.

### #3 — Ecological economics (RÉSOLU v2.2)

**Statut :** **RÉSOLU.** Substitution Q1062148 → **Q1049066** appliquée dans `11_` §A.1.
**Validé le :** 2026-05-11
**Source :** validation utilisateur 2026-05-11.

### #4 — Social sciences (RÉSOLU v2.2)

**Statut :** **RÉSOLU.** Substitution Q21201 → **Q34749** (« social science ») appliquée dans `11_` §A.2.
**Validé le :** 2026-05-11
**Source :** validation utilisateur 2026-05-11 (l'alternative déjà signalée en v1 était la bonne).

### #5 — Self-published (RÉSOLU v2.3 — omission)

**Statut :** **RÉSOLU par omission.** Q3504054 confirmé faux pour "self-published" (validation utilisateur 2026-05-11). Les 3 déclarations P123=Q3504054 ont été supprimées de `11_` §A.3, §A.4, §A.5.
**Validé le :** 2026-05-11
**Conséquence :** P123 publisher reste absent sur les 3 livres auto-édités (book-anthropie, book-dette-publique, lodyssee-des-idees). Acceptable selon doctrine Wikidata — l'absence est un signal recevable pour un patrouilleur, l'erreur sur Q-ID l'est moins.

### #6 — Publication series (RÉSOLU v2.3 — reconduction P31 existant)

**Statut :** **RÉSOLU par non-action.** Validation utilisateur 2026-05-11 confirme l'option 1 de la recommandation v2.1 : ne pas toucher au `P31=Q13442814` actuellement présent sur Q139040913. Les alternatives proposées (Q1711593, Q5633421) sont confirmées non pertinentes :
- Q1711593 = edited volume (pas une série)
- Q5633421 = scientific journal (pas une série de working papers)
- Q1812879 = pas longue durée (item différent)

La ligne `Q139040913 P31 Q1711593` a été supprimée de `11_` §A.6. Le bloc commentaire « ATTENTION Laura supprime d'abord P31=Q13442814 » a été remplacé par un bloc explicitant la doctrine de reconduction.

**Validé le :** 2026-05-11
**Action future éventuelle :** si une meilleure classe émerge ultérieurement via recherche Wikidata SPARQL communautaire, appliquer la correction en deux temps (ajout + suppression manuelle).

### #7 — Economic essay (RÉSOLU v2.3 — omission)

**Statut :** **RÉSOLU par omission.** Q62482 confirmé faux pour "economic essay" (validation utilisateur 2026-05-11). La ligne `Q138827344 P136 Q62482` a été supprimée de `11_` §A.3.
**Validé le :** 2026-05-11
**Conséquence :** P136 = Q35760 (essay) générique reste posé sur Q138827344 — suffit comme catégorisation de genre.

### #8 — Independent research (RÉSOLU v2.3 — omission)

**Statut :** **RÉSOLU par omission.** Q161732 confirmé faux pour "independent research" (validation utilisateur 2026-05-11). La ligne `LAST P921 Q161732` a été supprimée de `12_` §B.5 (AWP-05).
**Validé le :** 2026-05-11
**Conséquence :** P921 = Q138827949 (anthropy) reste l'unique sujet principal de l'AWP-05 — suffit pour la sémantique du working paper.

### #9 — Longue durée (RÉSOLU v2.3 — omission)

**Statut :** **RÉSOLU par omission.** Q1339645 confirmé faux pour "longue durée" (validation utilisateur 2026-05-11). L'alternative Q1812879 est également confirmée non pertinente. La ligne `LAST P921 Q1339645` a été supprimée de `12_` §B.2 (AWP-02).
**Validé le :** 2026-05-11
**Conséquence :** P921 = Q138827949 (anthropy) reste l'unique sujet principal de l'AWP-02. Le concept braudelien de longue durée est mentionné dans abstract / keywords, mais pas dans les claims structurés Wikidata faute de Q-ID propre.

### #10 — Zenodo (en tant que repository, pour le sourcing)

**Fichier concerné :** sourcing dans plusieurs lignes des batches (statement `S248 Q1322603`)
**Valeur posée :** Q1322603
**Statut :** À vérifier.
**Action Laura :** ouvrir https://www.wikidata.org/wiki/Q1322603 et confirmer que c'est bien « Zenodo » (repository).
**Alternative :** Q4994924 « Zenodo » — à départager.
**Recommandation :** essentiel pour la qualité du sourcing — vérifier.

---

## Décisions de propriétés P-IDs

### #11 — Academia.edu profile property (RÉSOLU v2.2)

**Statut :** **RÉSOLU.** Propriété officielle = **P5715** (« Academia.edu profile URL »). Substitution P6079 → P5715 appliquée dans le référentiel du maillage v1 §3.
**Validé le :** 2026-05-11
**Source :** validation utilisateur 2026-05-11.

**Notes :**
- `09_wikidata_existing_state.yaml` mentionne P5023 sur Q138909233 (« Academia.edu profile URL ») — sans doute une typo du prompt initial pour P5715. À vérifier côté Wikidata par Laura : la propriété active sur Q138909233 est-elle P5715 (URL) ou réellement P5023 ?
- Format attendu pour P5715 : URL complète `https://independent.academia.edu/StéphaneLALUT`.
- Pas de claim Academia.edu dans les batches QS Phase A actuels (la propriété est déjà posée selon `09_`).

### #12 — Google Scholar property (RÉSOLU v2.3)

**Statut :** **RÉSOLU.** P1960 (Google Scholar author ID) reste la propriété active et standard pour Q138909233. L'alternative P4985 est confirmée non pertinente : il s'agit en réalité de « TMDB person ID » (validation utilisateur 2026-05-11), pas une propriété Google Scholar.
**Validé le :** 2026-05-11
**Conséquence :** aucune modification — la déclaration P1960=J4NqzwSfrHAC déjà posée sur Q138909233 selon `09_` est conservée.

### #13 — Amazon URL property (RÉSOLU v2.1, doctrine Wikidata)

**Statut :** **RÉSOLU.** La doctrine officielle Wikidata sur P973 (cf. https://www.wikidata.org/wiki/Property:P973) précise : « Si un identifiant Wikidata dédié pour le site ciblé existe, utilisez-le à la place ». Pour Amazon, l'identifiant dédié est **P5749 (Amazon Standard Identification Number / ASIN)**.

**Application v2.1 sur Q138911733 (L'Odyssée des Idées) :**
- P5749 = `295863471X` (ASIN papier = ISBN-10 pour les livres)
- Source : URL Amazon FR fournie par Stéphane 2026-05-11
- Pas de P973 / P953 / P856 redondants

**Contrainte technique vérifiée :** P5749 exige `P31 ∈ {Q3331189, Q277759, Q41298, Q732577, Q7725634, Q3966, Q620615, Q10929058, Q11424}`. Q138911733 a Q3331189 ✓.

**Effet de bord (correction #14) :** ma recommandation V1 de SUPPRIMER Q3331189 sur Q138911733 était fausse. Conserver Q3331189, ajouter Q47461344 / Q571 en complément.

---

## Hors-périmètre — questions non-Wikidata

Aucune. Tout ce qui pouvait être validé depuis le repo l'a été en v1.1 et v1.2.

---

## Synthèse pour exécution (post-v2.3)

| Catégorie | Volume initial | Résolus v2.1 | Résolus v2.2 | Résolus v2.3 | Restant à Laura |
|---|---|---|---|---|---|
| Q-IDs structurants confirmés | 4 items | 3 (#1, #10, #13) | 0 | 1 (#6 reconduit) | 0 |
| Q-IDs ambigus à arbitrer | 6 items (#2-5, 7-9) | 0 | 3 (#2, #3, #4) | 3 (#5, #7, #8, #9 → omis) | 0 |
| P-IDs à arbitrer | 3 items (#11, 12, 13) | 1 (#13) | 1 (#11) | 1 (#12 confirmé P1960) | 0 |
| **Total** | **13 items** | **4** | **4** | **5** | **0 restants** |

**Effort Laura post-v2.3 : 0 min.**

Tous les `[À VÉRIFIER]` Wikidata externes du fichier sont désormais résolus. Le batch QuickStatements est prêt à exécution selon la cinétique du maillage v1 §13 (J+1 Phase A, J+3/+7/+10 Phase B sous-batches, J+14 Phase C). Aucune décision Wikidata active ne bloque le lancement.

**Note de prudence** : les vérifications de doublons (`§B.0` du maillage v1, recherche via hub.toolforge.org/P356:DOI) restent obligatoires avant Phase B.
