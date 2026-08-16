# 10 — Wikidata target completion

Différence entre **l'état actuel** (cf. `09_wikidata_existing_state.yaml`) et
**l'état cible** (déduit du croisement entre `01_` à `08_` et `09_`).

Document de synthèse humaine. Pas exécutable. Source des batches QuickStatements
Phase A / B / C (`11_`, `12_`, `13_`).

**Note v1.1.** Depuis l'intégration du maillage stratégique
`wikidata_maillage_lalut_v1.md` retrouvé dans `Wikidata/`, la spécification
authoritative des batches QuickStatements est ce maillage (§A, §B, §C).
Ce document `10_` reste utile comme synthèse repo-centrée, mais le
maillage v1 est la **source de vérité opérationnelle** pour Laura :
il contient en plus de cette synthèse les références (`S854`/`S813`),
les checklists pré/post-batch (§9-§10), la cinétique recommandée (§13)
et la liste exhaustive des Q-IDs/P-IDs (§3).

---

## Q138909233 — Stéphane Lalut (person)

### Propriétés déjà présentes (selon `09_`)
- P31 instance of : human
- P27 country of citizenship : France
- P106 occupation : economist, writer, researcher, essayist
- P800 notable work : Q138827344, Q138910896
- P856 official website : https://stephane-lalut.com/
- P269 IdRef ID : 283054085
- P1960 Google Scholar author ID : J4NqzwSfrHAC
- P10283 OpenAlex ID : A5130851063
- P496 ORCID iD : 0009-0002-1794-4895
- P5587 SSRN author ID : 11065608
- P5023 Academia.edu profile URL

### Propriétés à ajouter
| Propriété | Label | Valeur | Source repo |
|---|---|---|---|
| P9934 | Zenodo communities ID | `anthropie-working-papers` | `data/author.toml ligne 31` (rattaché aussi au concept Q138827949 — déjà posé là) |
| P800 (nouvelle valeur) | notable work | `Q139040913` (série AWP) | mise en cohérence avec `09_` |
| P800 (nouvelle valeur) | notable work | les 6 QIDs AWPs créés en Phase B | post-Phase B (Phase C) |
| P800 (potentielle) | notable work | `Q138911733` (L'Odyssée des Idées) | si Laura valide la création + auteur manquant |

### Notes éditoriales
- PROJECT_STATUS.md §3 dit "7 P-propriétés renseignées par Laura" mais `09_` en liste 11. Vérifier l'écart côté Wikidata.
- knowsAbout actuellement français uniquement (`data/author.toml ligne 20`). Pas d'équivalent EN dans le repo. Chantier reporté (PROJECT_STATUS.md §6).

---

## Q138827949 — Anthropy (concept)

### Propriétés déjà présentes
- P31 concept
- P61 discoverer or inventor : Q138909233
- P973 described at URL : https://stephane-lalut.com/quest-ce-que-lanthropie/
- P1343 described by source : Q138827344
- P9934 Zenodo communities ID : anthropie-working-papers

### Propriétés à ajouter
| Propriété | Label | Valeur | Source repo |
|---|---|---|---|
| P973 (variante EN) | described at URL | `https://stephane-lalut.com/en/quest-ce-que-lanthropie/` | `config/_default/hugo.toml ligne 23` (menu EN) |
| P1343 (multiple) | described by source | `Q138910896` (livre Dette Publique) | `data/works.yaml book-dette-publique` |
| P1343 (multiple) | described by source | `Q139040913` (série AWP) | `04_awp_series.yaml` |
| P1343 (potentiel) | described by source | les 6 QIDs AWPs créés en Phase B | post-Phase B (Phase C) |
| Label / alias EN | — | 'Anthropy', 'framework of anthropy' | `config/_default/hugo.toml ligne 18-19` |
| Description courte EN | — | 'Hypothesis that social systems displace disorder rather than resolve it' (≤ 250 chars) | `config/_default/hugo.toml ligne 19` |
| Description courte FR | — | "Hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent" | `config/_default/params.toml ligne 2` |

### Notes éditoriales
- Le slug EN frontmatter dit "what-is-anthropy" (cf. `02_`) mais le menu EN garde `/en/quest-ce-que-lanthropie/`. Le slug effectif côté Hugo est à confirmer ; conserver `quest-ce-que-lanthropie` dans les batches QS tant que la divergence n'est pas tranchée.

---

## Q138827344 — ANTHROPIE — Ordre ici. Dette ailleurs (livre)

### Propriétés déjà présentes
- P31 written work
- P921 main subject : Q138827949
- P50 author : Q138909233
- P577 publication date : 2025
- P407 French
- P856 official website : <URL>
- P212 ISBN-13 : 978-2-9586347-2-8

### Propriétés à ajouter
| Propriété | Label | Valeur | Source repo |
|---|---|---|---|
| P577 (précision date) | publication date | `2025-09-09` | `data/works.yaml ligne 269` |
| P1104 | number of pages | `622` | `data/works.yaml ligne 272` |
| P136 | genre | essay | par cohérence avec genre Q138911733 (à arbitrer Laura) |
| P973 | described at URL | `https://stephane-lalut.com/livres/anthropie-ordre-ici-dette-ailleurs/` | `data/works.yaml ligne 283` |
| P2333 | author's KDP ASIN (ou P2003 si différent) | `B0FQ9PG246` | `data/works.yaml ligne 275` — propriété Wikidata exacte à valider |

### Notes éditoriales
- Distribution Amazon KDP confirmée — pas de publisher Wikidata clair (auto-édition).

---

## Q138910896 — Dette Publique : Qui paie vraiment ? (livre)

### Propriétés déjà présentes
- P31 written work
- P921 main subject : [Q138827949, government debt]
- P50 author : Q138909233
- P577 publication date : 2025
- P1104 number of pages : **225** ⚠ (cf. note)
- P856 official website : <URL>
- P973 described at URL : <URL Alternatives Économiques>

### Propriétés à ajouter
| Propriété | Label | Valeur | Source repo |
|---|---|---|---|
| P212 | ISBN-13 | `978-2-9586347-3-5` | `data/works.yaml ligne 300` |
| P577 (précision date) | publication date | `2025-10-17` | `data/works.yaml ligne 299` |
| P407 | language of work | French | par symétrie avec Q138827344 |
| P136 | genre | essay | idem |
| P973 (URL site stephane-lalut.com) | described at URL | `https://stephane-lalut.com/livres/dette-publique-qui-paie-vraiment/` | `data/works.yaml ligne 313` |

### Erreurs structurelles
- **INCOHÉRENCE P1104=225 vs repo** : `data/works.yaml ligne 302` dit `pages: 0  # todo`. La valeur 225 dans Wikidata provient probablement d'Amazon. À vérifier avant correction.

---

## Q138911733 — L'Odyssée des Idées (livre antérieur)

### Propriétés déjà présentes
- P31 : `Q3331189` (**ERREUR à corriger**)
- P136 essay
- P577 publication date : 2023
- P407 French
- P212 ISBN-13 : 978-2-9586347-1-1

### Propriétés à ajouter
| Propriété | Label | Valeur | Source |
|---|---|---|---|
| P50 | author | `Q138909233` | maillage cassé selon `09_` |

### Erreurs structurelles
- **P31 = Q3331189 INADAPTÉ** (Q3331189 = "page d'homonymie") — devrait être `Q571` (book) ou `Q47461344` (written work).
- Maillage cassé : pas de P50 → l'auteur n'est pas lié au livre côté Wikidata.

### Données manquantes (hors repo)
- Aucune donnée le concernant n'est dans le repo (ni `works.yaml`, ni `content/livres/`). Toutes les valeurs à compléter restent à valider hors-repo par Laura/Stéphane.

---

## Q139040913 — Anthropie Working Papers (série)

### Propriétés déjà présentes
- P31 : `Q13442814` (**INADAPTÉ**)
- P921 main subject : Q138827949
- P50 author : Q138909233
- P495 country of origin : Q142 (France)
- P407 languages : French, English
- P856 official website : <URL serie-awp>

### Propriétés à ajouter
| Propriété | Label | Valeur | Source repo |
|---|---|---|---|
| P856 (variante EN) | official website | `https://stephane-lalut.com/en/serie-awp/` | `config/_default/hugo.toml ligne 27-29` |
| P9934 | Zenodo communities ID | `anthropie-working-papers` | `data/author.toml ligne 31` |
| P361 (potentiel) | part of | (chaîne avec les 6 AWPs créés) | post-Phase B |
| P527 | has part | 6 valeurs (AWP-01 à AWP-06 QIDs) | post-Phase B (Phase C) |
| P577 | publication date (début) | `2026-02-01` | `04_awp_series.yaml.publication_window.first_publication_fr` |
| Label / description EN | — | 'Open-access working paper series on anthropy by Stéphane Lalut (CC-BY 4.0, Zenodo).' | déduit du repo |

### Erreurs structurelles
- **P31 = Q13442814 (scholarly article) INADAPTÉ** — devrait être `Q1668921` (publication series) ou `Q22907736` (working paper series). Décision finale par Laura.

---

## AWPs (Phase B — à créer)

Les 6 AWPs ne sont pas encore sur Wikidata. **Phase B (cf. `12_quickstatements_phase_B_filled.qs`)** créera 6 items avec :

| Propriété | Valeur (source) |
|---|---|
| P31 | scholarly article ou working paper (Q22907736) — à valider |
| P50 | Q138909233 (auteur) |
| P407 | French + English (chaque AWP a 2 versions linguistiques) |
| P577 | publication_date_fr (canonique repo) |
| P921 | Q138827949 (anthropy) — main subject systématique |
| P179 (P361) | Q139040913 (série) — part of series |
| P1476 | titre FR canonique |
| P356 | DOI (Zenodo FR) |
| P953 | URL fulltext (PDF Zenodo) |
| P973 | URL site canonique |
| P275 | CC-BY 4.0 |
| P826 | citations Crossref (si reflet automatique) |
| P5024 | SSRN abstract ID |
| Description courte FR/EN | depuis `05_awps.yaml.abstract_fr/en` tronqué à ≤ 250 chars |

Données complètes par AWP : voir `05_awps.yaml`.

---

## Phase C — Rétro-liens

Une fois les 6 QIDs AWPs obtenus (post-Phase B), les rétro-liens suivants seront posés :

| Source (Q) | Propriété | Cible (Q) |
|---|---|---|
| Q138909233 (auteur) | P800 notable work | 6 × QID AWP |
| Q138827949 (concept) | P1343 described by source | 6 × QID AWP |
| Q139040913 (série) | P527 has part | 6 × QID AWP |
| Q138827344 (livre 1) | P527 has part / P1343 | sélection QID AWP (chapitre/correspondance) |
| Q138910896 (livre 2) | P527 has part / P1343 | QID AWP-03 |

Le détail des rétro-liens est dans `13_quickstatements_phase_C_filled.qs` (template à compléter par Laura après Phase B).

---

## Données qui ne peuvent pas venir du repo

- Date de naissance, lieu de naissance de Stéphane Lalut
- Affiliation institutionnelle (n/a — "chercheur indépendant")
- Tous les QIDs / P-IDs Wikidata externes (ces fichiers les exposent symboliquement ; Laura confirme côté Wikidata)
- Métadonnées de L'Odyssée des Idées (Q138911733) au-delà de l'ISBN et de l'année — livre absent du repo
- Citations Crossref/Scholar exactes en flux dynamique (`google_scholar.citations_observed` dans `works.yaml` est un snapshot manuel, pas une métrique live)
