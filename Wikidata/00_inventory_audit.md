# 00 — Inventory Audit

Document humainement lisible. Génération : **2026-05-11**, v2.5.

## 1. Résumé exécutif

- **Fichiers produits dans `Wikidata/`** : 16 (README + 9 YAMLs + 2 MD + 3 QS + CHANGELOG + maillage v1 préexistant).
- **Sources consultées dans le repo** : 25 fichiers (cf. §2), dont le maillage stratégique `wikidata_maillage_lalut_v1.md` retrouvé dans `Wikidata/` après première passe.
- **Champs `null`** (= donnée absente du repo) : 19 cas documentés ci-dessous (§3).
- **Incohérences détectées** : 12 cas documentés (§4) — dont 1 entre maillage v1 et repo.
- **Données qui ne peuvent pas être dans le repo** : 5 catégories (§5) — la 6e (maillage non trouvé) est levée en v1.1.
- **Statut PROJECT_STATUS** : architecture stable, phase 90j diffusion en cours,
  aucun chantier technique bloquant. La densification Wikidata est explicitement
  listée comme chantier acceptable hors site (PROJECT_STATUS.md §6).

### v1.0 → v1.1 (changements)

Le fichier `wikidata_maillage_lalut_v1.md` était **présent dans `Wikidata/`**
(570 lignes) — non trouvé à la première passe car la recherche initiale n'avait
pas exploré le dossier nouvellement créé. Conséquences :

- `11_quickstatements_phase_A_filled.qs` réécrit en miroir exact de §A.1-A.6 du maillage v1.
- `12_quickstatements_phase_B_filled.qs` réécrit en miroir exact de §B.1-B.6.
- `13_quickstatements_phase_C_filled.qs` réécrit en miroir exact de §C.1-C.3.
- Substitutions repo appliquées sur 3 valeurs confirmables (cf. §6).
- 1 erreur détectée dans le maillage v1 (URL EN série AWP, cf. §4).
- Les `[À VÉRIFIER]` Wikidata externes restent inchangés (Laura valide).

## 2. Sources consultées

| Fichier `Wikidata/` | Sources réelles utilisées | Notes |
|---|---|---|
| `01_author.yaml` | `data/author.toml`, `data/works.yaml.author`, `PROJECT_STATUS.md §2-3` | source principale = author.toml |
| `02_concept_anthropie.yaml` | `content/quest-ce-que-lanthropie/_index.md` + `_index.en.md`, `content/glossaire/_index.md`, `config/_default/hugo.toml`, `config/_default/params.toml`, `data/works.yaml` | 18 entrées glossaire extraites |
| `03_books.yaml` | `data/works.yaml` (id book-anthropie, book-dette-publique, book-livresque-des-mots) + `content/livres/*.md` (3 fichiers) | livre L'Odyssée absent (signalé) |
| `04_awp_series.yaml` | `data/works.yaml`, `content/serie-awp/_index.md` + `.en.md`, `data/awp_short_titles.yaml`, `config/_default/hugo.toml` | QID Q139040913 = mémoire externe |
| `05_awps.yaml` | `content/awp/awp-NN.md` (6) + `content/awp/awp-NN.en.md` (6) + `data/works.yaml` | 12 frontmatters lus, FR + EN |
| `06_articles.yaml` | `data/works.yaml` (sections publiés + accepted_pending + in_review) + `content/publications/*.md` (11 fichiers) | divergences titres works.yaml / fiche site |
| `07_site_mapping.yaml` | tous les précédents | 21 entrées de mapping |
| `08_external_links.yaml` | `data/author.toml` (sameAs), `data/works.yaml.deposits`, frontmatters AWP, frontmatters livres | 6 AWPs × ~10 liens, 3 livres × 7 Amazon |
| `09_wikidata_existing_state.yaml` | `_wikidata-prompt.txt` (mémoire externe, hors repo) + croisement repo | Laura valide |
| `10_wikidata_target_completion.md` | croisement `01_`-`08_` vs `09_` | synthèse |
| `11_quickstatements_phase_A_filled.qs` | `Wikidata/wikidata_maillage_lalut_v1.md` §A + `10_` + substitutions repo | batch QS V2 |
| `12_quickstatements_phase_B_filled.qs` | `Wikidata/wikidata_maillage_lalut_v1.md` §B + `05_` | 6 CREATE |
| `13_quickstatements_phase_C_filled.qs` | `Wikidata/wikidata_maillage_lalut_v1.md` §C + `01_`-`05_` | placeholders <Q-AWP-NN> |

Fichiers repo consultés (24 au total) :
1. `PROJECT_STATUS.md`
2. `data/author.toml`
3. `data/works.yaml` (v1.2, 33 œuvres)
4. `data/awp_short_titles.yaml`
5. `config/_default/hugo.toml`
6. `config/_default/params.toml`
7-12. `content/awp/awp-{01..06}.md` (6 fichiers FR)
13-18. `content/awp/awp-{01..06}.en.md` (6 fichiers EN)
19-21. `content/livres/{anthropie-ordre-ici-dette-ailleurs,dette-publique-qui-paie-vraiment,livresque-des-mots}.md` (3 livres)
22-32. `content/publications/*.md` (11 articles — fichiers individuels lus)
33. `content/quest-ce-que-lanthropie/_index.md` + `_index.en.md` (2)
34. `content/serie-awp/_index.md` + `_index.en.md` (2)
35. `content/glossaire/_index.md` (1)
36. `Wikidata/wikidata_maillage_lalut_v1.md` (maillage stratégique, v1.0 — 570 lignes, retrouvé en v1.1 de l'audit dans le dossier généré)

Layouts NON modifiés (lecture seule). Aucune modification du repo source.

## 3. Tableau des données manquantes (`null`)

| Entité | Champ | `expected_source` | Statut |
|---|---|---|---|
| author | `given_name` | `data/author.toml` (champ non éclaté) | non bloquant |
| author | `family_name` | `data/author.toml` (idem) | non bloquant |
| author | `date_of_birth` | hors repo (vie privée) | à valider Laura hors-repo |
| author | `place_of_birth` | hors repo | idem |
| author | `work_location` | hors repo | idem |
| author | `affiliation_qid` | n/a (chercheur indépendant) | non applicable |
| book-anthropie | `license` | `data/works.yaml ligne 276` (cellule vide "# à préciser") | MANQUANT |
| book-anthropie | `abstract_short_en` | `data/works.yaml ligne 279` (vide "# à compléter") | MANQUANT |
| book-anthropie | `title_en` page dédiée | `content/livres/anthropie-ordre-ici-dette-ailleurs.en.md` | n/a (pas de page EN — chantier P3 reporté) |
| book-dette-publique | `pages` | `data/works.yaml ligne 302` (0 + "# todo") | MANQUANT |
| book-dette-publique | `license` | `data/works.yaml ligne 306` (vide) | MANQUANT |
| book-dette-publique | `abstract_short_en` | `data/works.yaml ligne 310` (vide) | MANQUANT |
| book-livresque-des-mots | `wikidata_qid` | (à créer) | DÉCISION HUMAINE |
| book-livresque-des-mots | `pages` | `data/works.yaml ligne 333` | MANQUANT |
| book-livresque-des-mots | `license` | `data/works.yaml ligne 337` | MANQUANT |
| book-livresque-des-mots | `abstract_short_fr` | `data/works.yaml ligne 340` (vide) | présent dans frontmatter (cf. §4) |
| book-livresque-des-mots | `keywords` | `data/works.yaml ligne 341` ([] vide) | MANQUANT |
| book-livresque-des-mots | `page_url_fr` | `data/works.yaml ligne 343` (vide "# todo") | fichier `content/livres/livresque-des-mots.md` existe — URL déductible |
| awp-01 à awp-06 | `wikidata_qid` | n/a (à créer en Phase B) | EN ATTENTE |
| awp-01 à awp-06 | `citation_format_canonical` | `layouts/awp/single.html` (BibTeX/RIS) | non lu (template, hors scope) |
| L'Odyssée des Idées | **toutes** | n/a (livre absent du repo, mais QID Q138911733 existe sur Wikidata selon prompt) | DONNÉES HORS REPO |

## 4. Tableau des incohérences détectées

| Champ | Valeur A | Source A | Valeur B | Source B | Note |
|---|---|---|---|---|---|
| livre1.title (typographie) | `ANTHROPIE — Ordre ici. Dette ailleurs` | `data/works.yaml ligne 267` | `ANTHROPIE – Ordre ici. Dette ailleurs` | `content/livres/anthropie-ordre-ici-dette-ailleurs.md ligne 2` | cadratin `—` vs demi-cadratin `–` |
| livresque.publication_date | `""` (vide, "# todo") | `data/works.yaml ligne 330` | `2022-12-20` | `content/livres/livresque-des-mots.md ligne 5` | frontmatter plus complet que works.yaml |
| livresque.abstract_short_fr | vide | `data/works.yaml ligne 340` | présent (98 mots) | `content/livres/livresque-des-mots.md ligne 4` | works.yaml à mettre à jour |
| livresque.cover_image_url | absent | `data/works.yaml` | `https://m.media-amazon.com/images/I/71j0iwWpe5L._SL1436_.jpg` | `content/livres/livresque-des-mots.md ligne 8` | works.yaml à mettre à jour |
| livre1.amazon_urls (uk/de/es/it/ca) | absents | `data/works.yaml` | présents | `content/livres/anthropie-ordre-ici-dette-ailleurs.md` | works.yaml à compléter |
| livre2.pages | `0` (todo) | `data/works.yaml ligne 302` | `225` | `09_wikidata_existing_state.yaml` (Wikidata P1104) | source 225 non identifiée (Amazon ?) ; works.yaml prioritaire |
| awp-02.title | court : `3,3 millions d'années en un principe` | `content/awp/awp-02.md ligne 2` | long : `3,3 millions d'années en un principe : l'anthropie dans la longue durée` | `data/works.yaml ligne 113` | works.yaml = canonique |
| awp-05.title | `Penser hors les murs : notes sur la recherche indépendante` | `content/awp/awp-05.md ligne 2` | `Penser hors les murs : notes sur la recherche indépendante en économie` | `data/works.yaml ligne 209` | works.yaml = canonique |
| awp-05.zenodo record id | `19269486` (DOI) | `data/works.yaml ligne 220` + `content/awp/awp-05.md ligne 12` | `19269487` (pdf_url) | `content/awp/awp-05.md ligne 22` | divergence record/file Zenodo — à investiguer côté Zenodo |
| awp-06.jel_codes | 2 codes FR `[L86, Q55]` | `content/awp/awp-06.md ligne 14` | 5 codes EN `[L86, Q55, L96, Q56, O33]` | `content/awp/awp-06.en.md ligne 14` | asymétrie intentionnelle ou à harmoniser (`data/works.yaml ligne 257` signale) |
| art-ean-welgryn-2026.status | `accepted_pending` (sans date) | `data/works.yaml ligne 590-592` | `2026-05-05` (URL active + page publications) | `content/publications/en-attendant-nadeau-welgryn-alves-da-costa.md ligne 3` | works.yaml à corriger : probablement publié |
| concept anthropie.slug EN | `what-is-anthropy` | `content/quest-ce-que-lanthropie/_index.en.md ligne 3` | `quest-ce-que-lanthropie` (menu EN) | `config/_default/hugo.toml ligne 23` | slug effectif côté Hugo à confirmer |
| Q138827949 community attachment | `Person` (concept potentiel) | doctrine implicite | `Concept` (rattachement correct) | `PROJECT_STATUS.md §3` | déjà tranché côté Wikidata par Laura |
| URL EN série AWP (maillage v1) | `https://stephane-lalut.com/en/awp-series/` | `wikidata_maillage_lalut_v1.md` §2 ligne 67 | `https://stephane-lalut.com/en/serie-awp/` | `config/_default/hugo.toml` ligne 27-29 + absence de slug "awp-series" dans `content/serie-awp/_index.en.md` | **ERREUR maillage v1** — corrigée dans `11_` |

## 5. Données hors-repo (à valider par Laura ou Stéphane)

1. **QIDs et P-IDs Wikidata externes** : tous les QIDs cités (Q138909233, Q138827949, Q138827344, Q138910896, Q138911733, Q139040913) viennent du prompt utilisateur ou de `data/works.yaml`/`content/livres/*.md`. Les P-propriétés de l'état existant (`09_`) proviennent exclusivement du prompt.
2. **Date de naissance / lieu de naissance** de Stéphane Lalut : volontairement hors site.
3. **Affiliation institutionnelle** : n/a (chercheur indépendant — pas d'institution).
4. **L'Odyssée des Idées (Q138911733)** : aucune donnée dans le repo Hugo (ni `works.yaml`, ni `content/livres/`). Données partielles fournies hors-repo par l'utilisateur le **2026-05-11** : URL Amazon FR (`https://www.amazon.fr/Lodyssée-idées-philosophie-lintelligence-artificielle/dp/295863471X`), ISBN-13 (`978-2958634711` — strictement équivalent à la valeur Wikidata existante `978-2-9586347-1-1`), ISBN-10/ASIN papier (`295863471X`). Le slug Amazon suggère un sous-titre "philosophie de l'intelligence artificielle" mais **non recopié** (anti-pattern : ne pas extraire un titre depuis un slug URL sans confirmation). Restent à fournir : titre canonique complet, sous-titre, date précise (jour/mois 2023), pages, ASIN Kindle, abstract, autres marchés Amazon.
5. **Compteurs Google Scholar / citations** : `data/works.yaml.google_scholar.citations_observed` est un snapshot manuel (pas live).
6. ~~Fichier `wikidata_maillage_lalut_v1.md` non trouvé~~ → **LEVÉ en v1.1** : retrouvé dans `Wikidata/wikidata_maillage_lalut_v1.md` (570 lignes, version 1.0 Mai 2026). Les batches `11_`, `12_`, `13_` sont désormais en miroir exact des sections §A, §B, §C du maillage.

## 6. Discrépances avec la « mémoire stratégique » (`09_`)

| Item | Mémoire externe (prompt) | Réalité repo | Remarque |
|---|---|---|---|
| Q138909233 P-properties | 11 propriétés listées | PROJECT_STATUS.md §3 dit "7 P-propriétés renseignées par Laura" | Écart à investiguer côté Wikidata |
| Q138910896 P1104 | `225` | `data/works.yaml` dit `0 (todo)` | Valeur 225 d'origine inconnue |
| Q138911733 P31 | `Q3331189` (signalé erreur) | Pas dans repo | Correction proposée en Phase A |
| Q139040913 P31 | `Q13442814` (signalé inadapté) | Pas dans repo (le QID non plus) | Correction proposée en Phase A |
| `lodyssee-des-idees` | livre supposé du corpus | Absent du repo (works.yaml + content/livres/) | Données à fournir hors-repo |

## 6.5. État des `[À VÉRIFIER]` du maillage v1

Le maillage v1 contient ~25 marqueurs `[À VÉRIFIER]`. Catégorisation :

### Résolus depuis le repo (substitués dans 11_, 12_, 13_)

| Maillage v1 (origine) | Valeur substituée | Source repo |
|---|---|---|
| §2 URL EN concept `https://stephane-lalut.com/en/what-is-anthropy/` | **CONFIRMÉ** : utilisée verbatim dans `11_` A.2 | `content/quest-ce-que-lanthropie/_index.en.md` ligne 3 (slug "what-is-anthropy") |
| §2 URL EN série `https://stephane-lalut.com/en/awp-series/` | **CORRIGÉ** : remplacée par `/en/serie-awp/` dans `11_` A.6 | `config/_default/hugo.toml` ligne 27-29 + absence du slug "awp-series" dans le repo |
| §A.3 ASIN Kindle `B0FQ9PG246` (livre ANTHROPIE) | **CONFIRMÉ** dans `11_` A.3 | `data/works.yaml` ligne 275 |
| §A.3 Pages `+622` (livre ANTHROPIE) | **CONFIRMÉ** dans `11_` A.3 | `data/works.yaml` ligne 272 |
| §A.4 ISBN `978-2-9586347-3-5` (livre Dette Publique) | **CONFIRMÉ** dans `11_` A.4 | `data/works.yaml` ligne 300 + `content/livres/dette-publique-qui-paie-vraiment.md` ligne 5 |
| §B.1-B.6 DOIs Zenodo/SSRN/MPRA + dates publication | **CONFIRMÉ** dans `12_` B.1-B.6 (verbatim repo) | `data/works.yaml` + `content/awp/*.md` (concordance) |

### Non résolvables (Wikidata externe — Laura valide)

Les Q-IDs/P-IDs Wikidata externes ne peuvent pas être confirmés depuis le repo
et restent verbatim avec `[À VÉRIFIER]` dans `11_`, `12_`, `13_` :

- `Q937131` (given name "Stéphane")
- `Q161157` (public finance)
- `Q1062148` (ecological economics)
- `Q161172` (political ecology)
- `Q21201` (social sciences)
- `Q17737` (theory)
- `Q1149875` (hypothesis)
- `Q42213` (entropy)
- `Q62482` (economic essay)
- `Q3504054` (self-published)
- `Q1711593` (scholarly publication series)
- `Q1339645` (longue durée)
- `Q12739` (energy transition)
- `Q161732` (independent research)
- `Q1066186` (data center)
- `Q22954024` (government debt)
- `Q6581097` (male)
- `P6079` (Academia.edu profile ID)
- `P953` (full work URL — acceptée pour Amazon ?)

### Décisions différées (relevant de Stéphane / Laura)

- §A.1 `P21` sex or gender = `Q6581097` (male) : "confirmer avant exécution".
- §A.2 description italienne `Dit` : à ajouter si Q138827949 n'en a pas déjà.
- §C.3 création des 3 concepts dérivés (Paradoxe terminal, Créanciers invisibles, Quadruple peine) : recommandation maillage v1 = **différer**.

## 6.6 — Corrections Q-IDs Wikidata externes (v1.3, 2026-05-11)

Sept Q-IDs initialement marqués `[À VÉRIFIER]` dans le maillage v1.0 ont été corrigés ou confirmés via recherche web ciblée :

| Concept | V1 (initial, inventé) | V2 (vérifié) | Méthode |
|---|---|---|---|
| government debt | ~~Q22954024~~ | Q3024789 | web_search Anthropic |
| entropy | ~~Q42213~~ | Q45003 | web_search Anthropic |
| energy transition | ~~Q12739~~ | Q795757 | web_search Anthropic |
| data center | ~~Q1066186~~ | Q671224 | web_search Anthropic |
| political ecology | ~~Q161172~~ | Q1554076 | web_search Anthropic |
| hypothesis | ~~Q1149875~~ | Q41719 | web_search Anthropic |
| theory | Q17737 (déjà correct) | Q17737 | confirmation web |
| artificial intelligence | Q11660 (déjà correct) | Q11660 | confirmation web |
| AI data center (bonus AWP-06) | — | Q137571914 | découverte web |

Les Q-IDs et P-IDs encore à arbitrer (13 items) sont isolés dans le fichier dédié `14_remaining_decisions_for_laura.md`. Total effort Laura estimé : 15-25 min.

**Modification du décompte d'audit** : sur les ~19 `[À VÉRIFIER]` Wikidata externes du maillage v1.0, **8 sont désormais résolus**, **13 restent** (isolés en `14_`).

## 6.7 — Décisions structurantes résolues (v2.1, 2026-05-11)

Quatre décisions du fichier `14_remaining_decisions_for_laura.md` ont été soumises à une seconde passe de recherche web Anthropic. Résultats :

| # | Concept / propriété | V1 (inventé) | V2.1 (résolu) | Méthode |
|---|---|---|---|---|
| #1 | given name "Stéphane" | ~~Q937131~~ | Q3501543 | web_search |
| #6 | publication series | ~~Q1711593~~ | non résolu — pas de Q-ID standard | web_search infructueuse |
| #10 | Zenodo | ~~Q1322603~~ | Q22661177 | web_search |
| #13 | Amazon URL | P953/P856 | P5749 ASIN (doctrine Wikidata) | web_search |

**Effet de bord critique** : la correction « supprimer P31=Q3331189 sur Q138911733 » du maillage v1 est annulée (contrainte P5749 exige cette valeur). Conserver Q3331189, ajouter Q47461344 et Q571 en complément.

**Décompte global v2.1** :
- Maillage v1.0 : ~19 `[À VÉRIFIER]` Wikidata externes.
- Prompt v2 (corrections cat. 1 stable) : -8 résolus → 11 restants.
- Patch v2.1 (corrections cat. 1 structurantes) : -3 supplémentaires → 8 restants à Laura.
- Sur ces 8 restants, 7 ont une recommandation d'omission par défaut. Item #6 unique décision active de Laura.

## 6.8 — Substitutions supplémentaires validées par l'utilisateur (v2.2, 2026-05-11)

Quatre substitutions supplémentaires fournies par l'utilisateur 2026-05-11 :

| # | Concept / propriété | Avant | Après | Méthode |
|---|---|---|---|---|
| #2 | public finance | ~~Q161157~~ | Q274490 | validation utilisateur |
| #3 | ecological economics | ~~Q1062148~~ | Q1049066 | validation utilisateur |
| #4 | social sciences | ~~Q21201~~ | Q34749 | validation utilisateur (alternative déjà signalée v1) |
| #11 | Academia.edu profile property | ~~P6079~~ | P5715 | validation utilisateur |

Substitution `Q1322603 → Q22661177` (Zenodo) fournie également par l'utilisateur a confirmé la résolution déjà appliquée en v2.1 (aucune occurrence résiduelle de Q1322603).

**Décompte global v2.2** :
- Maillage v1.0 : ~19 `[À VÉRIFIER]` Wikidata externes initialement.
- Prompt v2 (8 résolus) → 11 restants.
- Patch v2.1 (3 résolus + 1 correction critique) → 8 restants.
- Patch v2.2 (4 résolus dont 1 P-ID) → **6 restants** pour Laura.
- Sur ces 6 restants : 4 ont une recommandation d'omission acceptable (#5, #7, #8, #9), 1 ne pas toucher (#6), 1 vérification rapide (#12).
- **Décision active stricte de Laura : seulement #9 (longue durée) et #12 (Google Scholar P1960).**

**Note croisée** : `09_wikidata_existing_state.yaml` mentionne P5023 sur Q138909233 pour Academia ; l'utilisateur a validé P5715 comme propriété officielle. Possible typo dans le prompt initial v1 (P5023 ↔ P5715). Laura confirme côté Wikidata.

## 6.9 — Résolution finale par omission/reconduction (v2.3, 2026-05-11)

Cinq dernières décisions du fichier `14_remaining_decisions_for_laura.md` résolues par l'utilisateur 2026-05-11 — toutes sous forme d'**omission** ou **reconduction de l'état actuel**, aucun nouveau Q-ID introduit (anti-pattern « inventer » respecté à l'extrême).

### Q-IDs supprimés des batches (sans remplacement)

| # | Concept | Q-ID supprimé | Justification |
|---|---|---|---|
| #5 | self-published | Q3504054 | faux pour ce sens — pas de Q-ID propre identifié |
| #7 | economic essay | Q62482 | faux pour ce sens — P136=Q35760 (essay) générique suffit |
| #8 | independent research | Q161732 | faux pour ce sens — P921 anthropy suffit pour AWP-05 |
| #9 | longue durée | Q1339645 | faux pour ce sens — Q1812879 également écarté |

7 lignes supprimées au total (3 lignes P123=Q3504054 dans `11_` §A.3/§A.4/§A.5, 1 ligne P136=Q62482 dans `11_` §A.3, 1 ligne P31=Q1711593 dans `11_` §A.6, 1 ligne P921=Q161732 dans `12_` §B.5, 1 ligne P921=Q1339645 dans `12_` §B.2).

### Q-IDs / P-IDs alternatives écartés (à ne pas introduire)

| Q/P-ID | Identité réelle (selon utilisateur) | Item concerné |
|---|---|---|
| Q1711593 | edited volume (≠ publication series) | #6 publication series |
| Q5633421 | scientific journal (≠ working paper series) | #6 publication series |
| Q1812879 | non identifié à « longue durée » | #9 longue durée |
| P4985 | TMDB person ID (≠ Google Scholar) | #12 Google Scholar property |

### Reconductions

| # | État actuel reconduit | Justification |
|---|---|---|
| #6 | P31=Q13442814 sur Q139040913 (série AWP) | pas de meilleure classe identifiée ; ne pas toucher au P31 existant |
| #12 | P1960=J4NqzwSfrHAC sur Q138909233 (Google Scholar) | propriété active et standard, P4985 est TMDB |

### Décompte final

| Étape | Restants à Laura |
|---|---|
| Maillage v1.0 | ~19 `[À VÉRIFIER]` |
| Prompt v2 (8 résolus) | 11 |
| Patch v2.1 (3 résolus + correction critique) | 8 |
| Patch v2.2 (4 résolus) | 6 |
| **Patch v2.3 (5 résolus par omission/reconduction)** | **0** |

**Le batch QuickStatements est désormais prêt pour exécution Laura sans aucune décision Wikidata active en attente.**

## 6.10 — Intégration SocArXiv (v2.5, 2026-05-11)

Stéphane a un compte SocArXiv actif (OSF Preprints). URL profil : `https://osf.io/ymkpj/`. OSF User ID : `ymkpj`.

**Dépôts effectués :**
- AWP-06 (Digital Infrastructures) : DOI `10.31235/osf.io/z6x38_v1`, accepté 2026-05-11.

**Dépôts à venir** (cinétique 2-3 jours entre chaque, ordre séquentiel AWP-01 → AWP-05) :
- AWP-01, AWP-02, AWP-03, AWP-04, AWP-05.

**Batch additif créé :** `15_quickstatements_socarxiv_filled.qs`. Strictement additif aux batches 11_, 12_, 13_. À exécuter après Phase B Wikidata (besoin des QIDs réels des AWPs). Substitution partielle tolérée.

**Sourcing total par AWP après exécution du batch 15_ complet :**
- DOI Zenodo FR (P356 principal)
- DOI Zenodo EN (P356 qualifié langue anglaise)
- DOI SSRN (P356)
- DOI SocArXiv (P356) — ajouté par batch 15_

Quatre plateformes indépendantes = signal de pérennité robuste face aux procédures de suppression Wikidata.

**État `sameAs` JSON-LD `data/author.toml` :**
- Avant : 8 entrées (ORCID, Zenodo, OpenAlex, Google Scholar, Academia, Wikidata, SSRN, IdRef)
- Après : 9 entrées (ajout SocArXiv via `https://osf.io/ymkpj/`)

## 7. Décisions à prendre par Laura / Stéphane

1. **Création du QID Livresque des mots** : oui/non ? Si oui, métadonnées à compléter (pages, abstract, keywords).
2. **L'Odyssée des Idées** : ajouter une page `content/livres/lodyssee-des-idees.md` + une entrée `works.yaml` ? Ou laisser hors site et garder seulement le QID externe ?
3. **P31 des AWPs** : `Q13442814` (scholarly article) vs `Q22907736` (working paper series part — à confirmer existence) vs autre. Choisi `Q13442814` dans `12_` faute de mieux ; Laura tranche.
4. **P2860 cites work** entre AWPs : poser les rétro-liens "related" du frontmatter Hugo comme citations effectives, ou pas (cf. doctrine `13_`) ?
5. **JEL codes asymétriques AWP-06** : harmoniser FR (2 codes) ↔ EN (5 codes) ?
6. **Correction P1104=225 sur Q138910896** : valeur 225 confirmée ou erreur ? Si erreur, supprimer la claim Wikidata.

## 8. État des critères d'acceptation du prompt

- [x] Les 14 fichiers du dossier `Wikidata/` sont créés.
- [x] `00_inventory_audit.md` liste explicitement chaque champ `null` avec son `expected_source` (§3).
- [x] Aucun champ n'est rempli par déduction ou web fetch.
- [x] Les 3 fichiers `.qs` (Phase A/B/C) sont des batches QuickStatements
      syntaxiquement valides (TAB-separated, `CREATE` + `LAST<TAB>...` pour Phase B).
- [x] Le résumé final (§1) explicite : nombre de fichiers, champs `null`, incohérences.
- [x] **Rien n'est committé** (cf. `CHANGELOG.md` § "Pas de commit Git").

## 9. Prochaine étape

> Transmettre le dossier `Wikidata/` à Stéphane pour relecture et validation,
> puis à Laura pour l'exécution des batches QuickStatements selon la cinétique
> du maillage v1 § 13 :
>
>   - **J** : Lecture + check P-IDs/Q-IDs `[À VÉRIFIER]` (45 min)
>   - **J+1** : Phase A — items existants, batch unique (30 min)
>   - **J+3, J+7, J+10** : Phase B — création AWPs, 3 sous-batches de 2 items chacun (45 min × 3)
>   - **J+14** : Phase C — maillage final (20 min)
>   - **Surveillance** : 5 min × jour × 14 j
>
> Total effort Laura : ~6-7 h cumulées sur 2 semaines.
> Total effort Stéphane : décision sur les concepts dérivés (§ C.3 maillage v1) uniquement.
> Total effort site Hugo : 1 prompt unique (§ 11 maillage v1), ~20 min.
