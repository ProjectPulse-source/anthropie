# État actuel des items Wikidata — relevé du 2026-07-04

**Méthode** : téléchargement direct de `https://www.wikidata.org/wiki/Special:EntityData/<QID>.json` (11/11 items récupérés, aucun échec, aucune redirection) puis extraction programmée — aucune valeur ci-dessous n'est de mémoire ou déduite.
**Référentiel de comparaison** : `reports/geo_audit/GEO_WORKLIST_NOEUDS_EXTERNES.md` § 0 et § 2, `data/works.yaml`, `content/livres/*.md`, `content/awp/*.md`.
**Légende** : ✅ déjà conforme (aucune ligne batch) · ⚠️ écart → ligne dans `batch_quickstatements.txt` · 🔶 point de vigilance sans action batch.

---

## Q138909233 — Stéphane Lalut (personne)

*lastrevid 2491064826 · modifié 2026-05-13*

| Champ | Valeur actuelle | Verdict |
|---|---|---|
| Label fr / en | `Stéphane Lalut` / `Stéphane Lalut` | ✅ |
| Description fr | `économiste français, chercheur indépendant auteur du cadre anthropique` | ⚠️ cible worklist 2.2 : « économiste, chercheur indépendant et essayiste » |
| Description en | `French independent economist and researcher, author of the anthropic framework` | ⚠️ idem ; « anthropic framework » crée en plus une collision lexicale avec le principe anthropique (anthropic principle) — la cible l'élimine |
| Aliases fr / en | (aucun) | ✅ |
| Descriptions de / es | présentes, avec fautes (`ükonom under forscher`, `francès`, `antropico`) | 🔶 hors périmètre FR/EN — correctifs proposés en bloc OPTIONNEL commenté |

Claims relevés : P31=Q5 (humain) ✅ · P106 = Q188094 (économiste), Q36180 (écrivain), Q1650915 (chercheur), **Q11774202 (essayiste)** — « essayiste » déjà porté en occupation ✅ · P27=Q142 ✅ · P800 (œuvres notables) = les 3 livres + concept + série + les 6 AWP + Q139040913 ✅ · P856 = `https://stephane-lalut.com/` ✅. Autres propriétés présentes non détaillées : P21, P101, P269, P496, P648, P735, P973, P1960, P3747, P5715, P10283.

---

## Q138827949 — Anthropie (concept)

*lastrevid 2490063977 · modifié 2026-05-12*

| Champ | Valeur actuelle | Verdict |
|---|---|---|
| Label fr / en | `Anthropie` / `Anthropy` | ✅ (aucune confusion avec le principe anthropique) |
| Description fr | `Mécanisme par lequel les systèmes sociaux et techniques déplacent le désordre plutôt qu'ils ne le résolvent.` | ⚠️ « Mécanisme » ≠ « hypothèse » (verbatim canonique), « et techniques » absent du verbatim, point final contraire aux conventions Wikidata |
| Description en | `Mechanism by which social systems displace disorder rather than resolving it` | ⚠️ idem (« Mechanism » ≠ « hypothesis ») |
| Aliases fr / en | `Déplacement du désordre` / `Displacement of disorder` | ✅ aucun « terme inventé par » — conforme à la nuance actée 04/07 |
| Desc. de / es / it | de = déjà « Hypothese… » (avec fautes de casse) ; es / it = encore « Mecanismo / Meccanismo » | 🔶 hors périmètre FR/EN — bloc OPTIONNEL commenté |

Claims relevés : P31 = Q151885 (concept), Q17737 (théorie), Q41719 (hypothèse) ✅ — « hypothèse » déjà en P31, cohérent avec la nouvelle description · **P61 (découvreur ou inventeur) = Q138909233** 🔶 — compatible avec la nuance 04/07 : la claim porte sur le CONCEPT, pas sur le mot ; « concept développé par S. Lalut » est la lecture correcte ; aucune action, mais signalé · P941=Q45003 · P973 = pages `quest-ce-que-lanthropie` FR + EN ✅ · P1343=Q138827344 ✅ · P9934=`anthropie-working-papers` ✅ · P800 = Q138827344, Q138910896, Q139040913 ✅ · P101 = Q8134, Q1554076, Q34749.

---

## Q138827344 — livre ANTHROPIE — Ordre ici. Dette ailleurs

*lastrevid 2491064848 · modifié 2026-05-13*

| Champ | Valeur actuelle | Verdict |
|---|---|---|
| Label fr / en | `ANTHROPIE — Ordre ici. Dette ailleurs` | ✅ (tiret cadratin = verbatim worklist § 0 ; le titre Hugo utilise un demi-cadratin, sans conséquence) |
| Descriptions fr / en | essai 2025 de S. Lalut | ✅ |
| P577 | 2025 (précision année) | ✅ |
| P212 | `978-2-9586347-2-8` | ✅ |
| P1104 | **+606** | ⚠️ canonique = **622** (site + works.yaml) — correctif déjà préparé le 29/05 (`Wikidata/correction_pagination_anthropie_2026-05-29.qs`, statut DIFFÉRÉ), repris dans ce batch |
| P50 / P407 / P136 / P921 | Q138909233 / Q150 / Q35760 / Q138827949 | ✅ |
| P856 / P953 | fiche site / `https://www.amazon.fr/dp/B0FQ9PG246` | ✅ |
| P1476 (titre) | absent | 🔶 pas exigé par la worklist — non batché |

---

## Q138910896 — livre Dette Publique : Qui paie vraiment ?

*lastrevid 2491064866 · modifié 2026-05-13*

| Champ | Valeur actuelle | Verdict |
|---|---|---|
| Label fr / en | `Dette Publique : Qui paie vraiment ?` | ✅ (identique au titre Hugo) |
| Descriptions fr / en | essai 2025, cadre anthropique appliqué à la dette | ✅ dates/attribution correctes · 🔶 « anthropic framework » en EN = même collision lexicale que la personne, mais worklist 2.5 = contrôle dates/ISBN seulement → non batché |
| P577 | 2025 (précision année) | ✅ |
| P212 | `978-2-9586347-3-5` | ✅ |
| P1104 | **+225** (1 référence attachée) | ⚠️ canonique = **224** (site + works.yaml, nombre de pages broché) — la réf. attachée (probablement Amazon, qui affiche 225) sera perdue au remove/add, assumé |
| P50 / P407 / P136 / P921 / P856 / P973 | conformes (dont P921 double : anthropie + dette publique) | ✅ |

---

## Q138911733 — livre L'Odyssée des idées ⚠️ ITEM CRITIQUE

*lastrevid 2491064887 · modifié 2026-05-13*

**Verdict global : l'item décrit ENTIÈREMENT l'ancienne édition (2023)** — c'est le scénario redouté par la worklist 2.4 et la source du mode de défaillance M4 (fusion d'éditions).

| Champ | Valeur actuelle | Verdict |
|---|---|---|
| Label fr / en | `L'Odyssée des Idées` | ⚠️ casse : canonique site/works.yaml = `L'Odyssée des idées` (i minuscule) |
| Description fr | `Essai de Stéphane Lalut sur l'histoire des idées, des origines du langage à l'intelligence artificielle (2023)` | ⚠️ « (2023) » + « des origines du langage » = formulation ancienne édition |
| Description en | `Essay by Stéphane Lalut on the history of ideas, from the origins of language to artificial intelligence (2023)` | ⚠️ idem |
| P31 | Q3331189 (édition), Q47461344 (œuvre écrite), Q571 (livre) | ✅ hybride œuvre/édition préexistant — inchangé ; la bascule des claims d'édition suit la consigne worklist (« basculer plutôt que laisser l'hybride ») |
| P577 | **2023** (précision année) | ⚠️ cible = 2026 (nouvelle édition entièrement recomposée) |
| P212 | **`978-2-9586347-1-1`** (2 références attachées) | ⚠️ = ANCIEN ISBN, exactement ce que la mémoire projet annonçait ; cible `978-2-9586347-4-2` ; les 2 réfs seront perdues au remove/add, assumé (elles sourcent l'ancienne édition) |
| P1104 | absent | ⚠️ cible +696 |
| P5749 (ASIN) | **`295863471X`** | ⚠️ = ancien broché DÉPUBLIÉ ; cible broché actif `2958634744` (le Kindle B0CVXQSLBQ, hérité de la 1ʳᵉ éd., n'est volontairement pas ajouté : c'est l'ancre du risque de fusion) |
| P1476 (titre) | absent | ⚠️ ajout `fr:"L'Odyssée des idées"` — titre principal non ambigu (acté : reste « L'Odyssée des idées » pour Wikidata) |
| P1680 (sous-titre) | absent | 🛑 **DÉCISION AUTEUR** — deux candidats documentés, aucun importé (voir README_LAURA.md) |
| P50 / P407 / P136 / P291 | Q138909233 / Q150 / Q35760 / Q142 | ✅ |
| P648 | `OL45424562W` (work OpenLibrary) | ✅ identifiant d'ŒUVRE, reste valable quelle que soit l'édition (le rattachement de l'édition 2026 se joue côté OpenLibrary, worklist § 3.1) |

Note : « 250 escales » n'a pas de propriété Wikidata naturelle — non batché ; la défense sur ce chiffre passe par ISBN + pages + descriptions.

---

## Q139771989 → Q139771994 — les 6 Anthropie Working Papers

*lastrevid 2500771204-2500771216 · modifiés 2026-06-01*

Structure commune, vérifiée item par item : P31=Q13442814 (article scientifique) ✅ · P50=Q138909233 ✅ · P407=Q150 ✅ · P921 inclut Q138827949 ✅ · P953 = record Zenodo + fiches site FR et EN ✅ · P361 présent (série).

| Item | AWP | P577 (item) | Date site | P356 (item) | DOI version attendu (worklist § 0) | Verdict |
|---|---|---|---|---|---|---|
| Q139771989 | 01 | 2026-02-01 | 2026-02-01 | `10.5281/ZENODO.19266862` | `…19266862` | ✅ |
| Q139771990 | 02 | 2026-02-15 | 2026-02-15 | `10.5281/ZENODO.19268037` | `…19268037` | ✅ |
| Q139771991 | 03 | 2026-03-01 | 2026-03-01 | `10.5281/ZENODO.19268769` | `…19268769` | ✅ |
| Q139771992 | 04 | 2026-03-10 | 2026-03-10 | `10.5281/ZENODO.19269244` | `…19269244` | ✅ |
| **Q139771993** | **05** | 2026-03-20 | 2026-03-20 | **`10.5281/ZENODO.19269486`** | `…19269487` | ⚠️ **CONCEPT-DOI** — vérifié le 04/07 sur l'API Zenodo : record 19269487 porte `doi=10.5281/zenodo.19269487` et `conceptdoi=10.5281/zenodo.19269486`. L'item porte donc le concept-DOI, en violation de la convention Option B (12-13/05). Le P953 Zenodo pointe aussi sur `records/19269486` |
| Q139771994 | 06 | 2026-05-07 | 2026-05-07 | `10.5281/ZENODO.20025421` | `…20025421` | ✅ |

Toutes les dates de publication = 2026 avec précision jour, alignées sur le site ✅. Descriptions FR/EN : « Working paper de/by Stéphane Lalut … (AWP-NN, 2026) » — factuelles, cohérentes ✅, non touchées.

🔶 **Signalement hors Wikidata (pour le passage § 1 Zenodo, Stéphane)** : le record Zenodo 19269487 (AWP-05 FR) affiche `publication_date = 2026-03-01` alors que site et Wikidata portent 2026-03-20 — métadonnée Zenodo à corriger côté Zenodo, rien à changer côté Wikidata.

🔶 Les 6 items représentent les versions FR ; les DOI des traductions EN (`…19431208`, `…19433086`, `…19434094`, `…19439921`, `…19440866`, `…20077993` d'après le site) n'ont pas d'item — hors périmètre worklist, noté pour mémoire.

---

## Complément du 2026-07-06 — AWP-07 (BLOC 7 : CRÉATION)

**AWP-07 « La boucle anthropique » publié le 2026-07-05** (Zenodo FR `10.5281/zenodo.21200286` version-DOI, EN `…21200288` ; pages site `/awp/awp-07/` FR+EN en ligne).

**État Wikidata au 06/07 : l'item N'EXISTE PAS** — vérifié par recherche d'entités (« boucle anthropique » fr et « anthropic loop » en : 0 résultat). Le BLOC 7 du batch le CRÉE, sur le modèle exact des 6 items existants (mêmes propriétés que Q139771994/AWP-06, hors SocArXiv — dépôt volontairement différé pour AWP-07).

Pas d'état antérieur, donc pas de rollback : en cas d'erreur, corriger la déclaration fautive dans l'item créé (jamais de suppression d'item). **Le QID attribué à la création est à renvoyer à Stéphane** (registre projet + futurs batchs).
