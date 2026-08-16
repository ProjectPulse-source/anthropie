# Maillage Wikidata — Stéphane Lalut / Anthropie
**Version 1.0 — Mai 2026**
**Destinataire : Laura (opératrice Wikidata) — Source : stephane-lalut.com / D:\anthropie\anthropie-site**

---

## 0. Mode d'emploi

Ce fichier est conçu pour être exécuté par **QuickStatements V2** (https://quickstatements.toolforge.org/) depuis le compte Laura. Il est découpé en **trois phases** indépendantes, chacune correspondant à un batch distinct à exécuter à **48-72 heures d'intervalle** pour respecter la cinétique de prudence (éviter pattern de mass-editing).

**Avant tout batch, lire la section « Checklist pré-batch » (§ 9).**
**Après chaque batch, lire la section « Checklist post-batch » (§ 10).**

Conventions du fichier :
- **Bloc CODE** = à coller dans QuickStatements
- **Bloc `[À VÉRIFIER]`** = déclaration conditionnelle, à activer/supprimer par Laura après check 30s
- Les références (`S854`, `S813` etc.) sont incluses pour stabiliser les déclarations face aux patrouilleurs

---

## 1. État Wikidata existant (rappel)

| QID | Sujet | Notes |
|---|---|---|
| **Q138909233** | Stéphane Lalut (personne) | Riche, à compléter |
| **Q138827949** | Anthropy (concept) | Minimal, à enrichir |
| **Q138827344** | ANTHROPIE — Ordre ici. Dette ailleurs (livre 1) | Solide, à compléter |
| **Q138910896** | Dette Publique : Qui paie vraiment ? (livre 2) | ISBN absent visible, à corriger |
| **Q138911733** | L'Odyssée des Idées (livre 2023) | **P31 erroné + P50 absent** |
| **Q139040913** | Anthropie Working Papers (série) | **P31 inadapté** |

| QID à créer | Sujet | Phase |
|---|---|---|
| **AWP-01** à **AWP-06** | 6 working papers individuels | Phase B |
| *(optionnel)* Livresque des mots | Livre antérieur 2024 | Phase C (différé) |

---

## 2. Référentiel canonique (à ne jamais s'écarter de ces valeurs)

### Identifiants pérennes
- ORCID : `0009-0002-1794-4895`
- OpenAlex auteur : `A5130851063`
- Google Scholar : `J4NqzwSfrHAC`
- SSRN auteur : `11065608`
- IdRef : `283054085`
- Wikidata personne : `Q138909233`
- Zenodo community : `anthropie-working-papers`

### Définition canonique de l'anthropie (verbatim, ne jamais paraphraser)
> *« L'anthropie est l'hypothèse selon laquelle les systèmes sociaux déplacent le désordre plutôt qu'ils ne le résolvent. »*

### AWPs — Table croisée DOIs
| AWP | DOI Zenodo FR | DOI Zenodo EN | DOI SSRN | MPRA | Date FR |
|---|---|---|---|---|---|
| AWP-01 | 10.5281/zenodo.19266862 | 10.5281/zenodo.19431208 | 10.2139/ssrn.6543618 | 128604 | 2026-02-01 |
| AWP-02 | 10.5281/zenodo.19268037 | 10.5281/zenodo.19433086 | 10.2139/ssrn.6615059 | 128605 | 2026-02-15 |
| AWP-03 | 10.5281/zenodo.19268769 | 10.5281/zenodo.19434094 | 10.2139/ssrn.6615278 | 128606 | 2026-03-01 |
| AWP-04 | 10.5281/zenodo.19269244 | 10.5281/zenodo.19439921 | 10.2139/ssrn.6615305 | 128607 | 2026-03-10 |
| AWP-05 | 10.5281/zenodo.19269486 | 10.5281/zenodo.19440866 | 10.2139/ssrn.6615438 | 128608 | 2026-03-20 |
| AWP-06 | 10.5281/zenodo.20025421 | 10.5281/zenodo.20077993 | 10.2139/ssrn.6735581 | 129034 | 2026-05-07 |

### URLs canoniques pages site
| Type | URL FR | URL EN |
|---|---|---|
| Concept | https://stephane-lalut.com/quest-ce-que-lanthropie/ | https://stephane-lalut.com/en/what-is-anthropy/ [À VÉRIFIER URL EN] |
| Série AWP | https://stephane-lalut.com/serie-awp/ | https://stephane-lalut.com/en/awp-series/ [À VÉRIFIER URL EN] |
| AWP-NN | https://stephane-lalut.com/awp/awp-NN/ | https://stephane-lalut.com/en/awp/awp-NN/ |
| Livre ANTHROPIE | https://stephane-lalut.com/livres/anthropie-ordre-ici-dette-ailleurs/ | — |
| Livre Dette Publique | https://stephane-lalut.com/livres/dette-publique-qui-paie-vraiment/ | — |

---

## 3. Q/P-IDs utilisés (référentiel)

**Classes (Q-IDs) confirmés :**
- Q5 = human
- Q142 = France
- Q150 = French (langue)
- Q1860 = English (langue)
- Q571 = book
- Q47461344 = written work
- Q3331189 = version, edition or translation
- Q35760 = essay
- Q13442814 = scholarly article
- Q151885 = concept
- Q188094 = economist
- Q36180 = writer
- Q1650915 = researcher
- Q11774202 = essayist
- Q45003 = entropy (physique) ****
- Q22661177 = Zenodo (en tant que repository) ****
- Q3024789 = government debt ****

**Propriétés (P-IDs) confirmées :**
- P31 = instance of
- P21 = sex or gender
- P27 = country of citizenship
- P50 = author
- P101 = field of work
- P106 = occupation
- P123 = publisher
- P136 = genre
- P212 = ISBN-13
- P248 = stated in (référence)
- P269 = IdRef ID
- P291 = place of publication
- P356 = DOI
- P361 = part of
- P407 = language of work or name
- P495 = country of origin
- P496 = ORCID iD
- P569 = date of birth **[NE PAS UTILISER — date inconnue, NE PAS INVENTER]**
- P577 = publication date
- P629 = edition or translation of
- P735 = given name
- P734 = family name
- P747 = has edition or translation
- P800 = notable work
- P813 = retrieved (référence)
- P854 = reference URL
- P856 = official website
- P921 = main subject
- P941 = inspired by
- P953 = full work available at URL
- P973 = described at URL
- P1104 = number of pages
- P1343 = described by source
- P1416 = affiliation
- P1476 = title (avec qualifier langue)
- P1680 = subtitle
- P1960 = Google Scholar author ID
- P5587 = SSRN author ID
- P5715 = Academia.edu profile ID ****
- P9934 = Zenodo communities ID
- P10283 = OpenAlex ID

---

# PHASE A — Corrections et enrichissements d'items existants

> **À exécuter en premier.** Pas de création nouvelle. Risque très faible.
> Volume estimé : ~70 déclarations. Durée Laura : ~30 min de validation + exécution.

## A.1 — Stéphane Lalut (Q138909233)

```quickstatements
# === Ajouts identité ===
Q138909233	P735	Q3501543	# given name: Stéphane
Q138909233	P734	"Lalut"	# family name (texte si pas d'item Wikidata)
Q138909233	P21	Q6581097	# sex or gender: male [confirmer avant exécution]

# === Champs de travail (P101) ===
Q138909233	P101	Q8134	# field of work: economics
Q138909233	P101	Q274490	# field of work: public finance
Q138909233	P101	Q1049066	# field of work: ecological economics
Q138909233	P101	Q138827949	# field of work: anthropy (auto-référentiel mais légitime — théoricien d'un concept)

# === Notable works additionnels ===
Q138909233	P800	Q138911733	# notable work: L'Odyssée des Idées
Q138909233	P800	Q138827949	# notable work: anthropie (concept)
Q138909233	P800	Q139040913	# notable work: Anthropie Working Papers (série)

# === Pas de P569 (date de naissance) — non publique, NE PAS INVENTER ===
```

## A.2 — Anthropy (Q138827949)

```quickstatements
# === Reclassification du P31 ===
# P31 actuel = concept (Q151885) → conserver, ajouter qualificatif théorique
Q138827949	P31	Q17737	# add: theory
Q138827949	P31	Q41719	# add: hypothesis

# === Champ disciplinaire ===
Q138827949	P101	Q8134	# field: economics
Q138827949	P101	Q1554076	# field: political ecology
Q138827949	P101	Q34749	# field: social sciences

# === Inspirations (relations conceptuelles) ===
Q138827949	P941	Q45003	# inspired by: entropy (thermodynamique)
# Note: NE PAS écrire que l'anthropie EST l'entropie. Relation = inspiration analogique.

# === Œuvres notables qui traitent du concept ===
Q138827949	P800	Q138827344	# notable work: ANTHROPIE livre
Q138827949	P800	Q138910896	# notable work: Dette Publique livre
Q138827949	P800	Q139040913	# notable work: Anthropie Working Papers série

# === Sources et URLs supplémentaires ===
Q138827949	P973	"https://stephane-lalut.com/en/what-is-anthropy/"	P407	Q1860	# described at URL (EN) [À VÉRIFIER URL]

# === Description en plus de langues (si pas déjà fait) ===
Dit	"Meccanismo per cui i sistemi sociali spostano il disordine invece di risolverlo"
Den	"Mechanism by which social systems displace disorder rather than resolving it"
# Note : labels FR/EN/ES déjà présents selon fiche actuelle.
```

## A.3 — ANTHROPIE — Ordre ici. Dette ailleurs (Q138827344)

```quickstatements
# === Compléments métadonnées ===
Q138827344	P1104	+622	# number of pages: 622
Q138827344	P136	Q35760	# genre: essay
Q138827344	P136	Q62482	# genre: economic essay [À VÉRIFIER Q62482]
Q138827344	P291	Q142	# place of publication: France
Q138827344	P123	Q3504054	# publisher: self-published [À VÉRIFIER Q3504054]

# === Reference URL (sourcing renforcé) ===
# Si une déclaration existe sans source, ajouter sourcing :
# Pour l'ISBN, sources possibles : BnF, IdRef, Amazon
Q138827344	P953	"https://www.amazon.fr/dp/B0FQ9PG246"	# Amazon FR Kindle ASIN URL [À VÉRIFIER si propriété P953 acceptée pour Amazon]
```

## A.4 — Dette Publique : Qui paie vraiment ? (Q138910896)

```quickstatements
# === Ajout ISBN (manquant sur la fiche actuelle) ===
Q138910896	P212	"978-2-9586347-3-5"	S854	"https://stephane-lalut.com/livres/dette-publique-qui-paie-vraiment/"	S813	+2026-05-11T00:00:00Z/11

# === Compléments métadonnées ===
Q138910896	P136	Q35760	# genre: essay
Q138910896	P407	Q150	# language: French (manque sur fiche)
Q138910896	P291	Q142	# place of publication: France
Q138910896	P123	Q3504054	# publisher: self-published [À VÉRIFIER]
```

## A.5 — L'Odyssée des Idées (Q138911733) — CORRECTIONS CRITIQUES

```quickstatements
# === CORRECTION P31 (erreur structurelle) ===
# ATTENTION : Laura doit d'abord SUPPRIMER l'ancienne déclaration P31=Q3331189
# via l'interface web, puis exécuter :
Q138911733	P31	Q47461344	# instance of: written work
Q138911733	P31	Q571	# also instance of: book

# === AJOUT AUTEUR (P50 absent — maillage cassé) ===
Q138911733	P50	Q138909233	S854	"https://stephane-lalut.com/"	S813	+2026-05-11T00:00:00Z/11

# === Compléments ===
Q138911733	P136	Q35760	# genre: essay (existe déjà ? — sinon ajouter)
Q138911733	P291	Q142	# place of publication: France
Q138911733	P123	Q3504054	# self-published [À VÉRIFIER]

# === Page site (si une page dédiée existe) ===
Q138911733	P856	"https://stephane-lalut.com/livres/lodyssee-des-idees/"	# [À VÉRIFIER que la page existe]
```

## A.6 — Anthropie Working Papers série (Q139040913)

```quickstatements
# === CORRECTION P31 (article ≠ série d'articles) ===
# ATTENTION : Laura supprime d'abord P31=Q13442814 via interface
Q139040913	P31	Q1711593	# scholarly publication series [À VÉRIFIER Q1711593]
# Alternative si Q1711593 inadéquat : Q277759 (book series) ou créer un nouveau concept

# === Compléments ===
Q139040913	P407	Q150	# language: French (principal)
Q139040913	P407	Q1860	# language: English (versions traduites)
Q139040913	P9934	"anthropie-working-papers"	# Zenodo communities ID
Q139040913	P101	Q8134	# field of work: economics
Q139040913	P101	Q138827949	# field of work: anthropy
Q139040913	P50	Q138909233	# author already present — skip if exists

# === Diffusion / has parts (chaque AWP fera P361 vers Q139040913) ===
# Note : le lien parent→enfants se fait depuis chaque AWP via P361, pas ici.
```

---

# PHASE B — Création des items AWP-01 à AWP-06

> **À exécuter après Phase A validée et après vérification doublons.**
> Volume : 6 items × ~15 déclarations = ~90 déclarations.
> Durée Laura : 45 min validation + exécution.

## B.0 — PRÉALABLE OBLIGATOIRE (recherche doublons)

Pour chaque DOI, Laura interroge :
```
https://hub.toolforge.org/P356:10.5281/zenodo.19266862
https://hub.toolforge.org/P356:10.5281/zenodo.19268037
https://hub.toolforge.org/P356:10.5281/zenodo.19268769
https://hub.toolforge.org/P356:10.5281/zenodo.19269244
https://hub.toolforge.org/P356:10.5281/zenodo.19269486
https://hub.toolforge.org/P356:10.5281/zenodo.20025421
```
**Si un QID est retourné** : ne PAS créer, mais enrichir l'item existant (substituer le bloc CREATE par le QID retourné).
**Si « no match » sur tous** : exécuter le batch ci-dessous tel quel.

## B.1 — AWP-01

```quickstatements
CREATE
LAST	Lfr	"Qu'est-ce que l'anthropie ? Principes d'une hypothèse"
LAST	Len	"What is anthropy? Principles of a hypothesis"
LAST	Dfr	"Working paper de Stéphane Lalut sur les fondements théoriques de l'anthropie (AWP-01, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on the theoretical foundations of anthropy (AWP-01, 2026)"
LAST	P31	Q13442814	# scholarly article
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19266862"	S854	"https://doi.org/10.5281/zenodo.19266862"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19431208"	P407	Q1860	# DOI version EN (qualifié langue anglaise)
LAST	P356	"10.2139/ssrn.6543618"	# DOI SSRN
LAST	P407	Q150	# language: French (principal)
LAST	P577	+2026-02-01T00:00:00Z/11	# publication date FR
LAST	P921	Q138827949	# main subject: anthropy
LAST	P361	Q139040913	# part of: Anthropie Working Papers
LAST	P953	"https://zenodo.org/records/19266862"	# full work URL
LAST	P953	"https://stephane-lalut.com/awp/awp-01/"	P407	Q150	# canonical site URL FR
LAST	P953	"https://stephane-lalut.com/en/awp/awp-01/"	P407	Q1860	# canonical site URL EN
```

## B.2 — AWP-02

```quickstatements
CREATE
LAST	Lfr	"3,3 millions d'années en un principe : l'anthropie en longue durée"
LAST	Len	"3.3 million years in one principle: anthropy in the longue durée"
LAST	Dfr	"Working paper de Stéphane Lalut appliquant l'anthropie à l'histoire longue (AWP-02, 2026)"
LAST	Den	"Working paper by Stéphane Lalut applying anthropy to long-term history (AWP-02, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19268037"	S854	"https://doi.org/10.5281/zenodo.19268037"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19433086"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615059"
LAST	P407	Q150
LAST	P577	+2026-02-15T00:00:00Z/11
LAST	P921	Q138827949	# main subject: anthropy
LAST	P921	Q1339645	# main subject: longue durée [À VÉRIFIER Q1339645]
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19268037"
LAST	P953	"https://stephane-lalut.com/awp/awp-02/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-02/"	P407	Q1860
```

## B.3 — AWP-03

```quickstatements
CREATE
LAST	Lfr	"Dette publique et anthropie : qui paie vraiment le désordre ?"
LAST	Len	"Public debt and anthropy: who really pays for disorder?"
LAST	Dfr	"Working paper de Stéphane Lalut sur la dette publique comme transfert anthropique (AWP-03, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on public debt as anthropic transfer (AWP-03, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19268769"	S854	"https://doi.org/10.5281/zenodo.19268769"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19434094"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615278"
LAST	P407	Q150
LAST	P577	+2026-03-01T00:00:00Z/11
LAST	P921	Q138827949	# anthropy
LAST	P921	Q3024789	# government debt
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19268769"
LAST	P953	"https://stephane-lalut.com/awp/awp-03/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-03/"	P407	Q1860
```

## B.4 — AWP-04

```quickstatements
CREATE
LAST	Lfr	"Transition énergétique ou transfert entropique ?"
LAST	Len	"Energy transition or entropic transfer?"
LAST	Dfr	"Working paper de Stéphane Lalut sur la transition énergétique comme déplacement de désordre (AWP-04, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on energy transition as displacement of disorder (AWP-04, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19269244"	S854	"https://doi.org/10.5281/zenodo.19269244"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19439921"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615305"
LAST	P407	Q150
LAST	P577	+2026-03-10T00:00:00Z/11
LAST	P921	Q138827949	# anthropy
LAST	P921	Q795757	# main subject: energy transition
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19269244"
LAST	P953	"https://stephane-lalut.com/awp/awp-04/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-04/"	P407	Q1860
```

## B.5 — AWP-05

```quickstatements
CREATE
LAST	Lfr	"Penser hors les murs : notes sur la recherche indépendante en économie"
LAST	Len	"Thinking beyond the walls: notes on independent research in economics"
LAST	Dfr	"Working paper de Stéphane Lalut sur la recherche indépendante en économie (AWP-05, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on independent research in economics (AWP-05, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19269486"	S854	"https://doi.org/10.5281/zenodo.19269486"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19440866"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615438"
LAST	P407	Q150
LAST	P577	+2026-03-20T00:00:00Z/11
LAST	P921	Q138827949
LAST	P921	Q161732	# main subject: independent research [À VÉRIFIER Q161732]
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19269486"
LAST	P953	"https://stephane-lalut.com/awp/awp-05/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-05/"	P407	Q1860
```

## B.6 — AWP-06

```quickstatements
CREATE
LAST	Lfr	"Infrastructures numériques et dette technologique : data centers, IA et déplacement du désordre"
LAST	Len	"Digital infrastructures and technological debt: data centers, AI, and the displacement of disorder"
LAST	Dfr	"Working paper de Stéphane Lalut sur les infrastructures numériques comme nouveau site de transfert anthropique (AWP-06, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on digital infrastructures as new locus of anthropic transfer (AWP-06, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.20025421"	S854	"https://doi.org/10.5281/zenodo.20025421"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.20077993"	P407	Q1860
LAST	P356	"10.2139/ssrn.6735581"
LAST	P407	Q150
LAST	P577	+2026-05-07T00:00:00Z/11
LAST	P921	Q138827949	# anthropy
LAST	P921	Q671224	# main subject: data center
LAST	P921	Q11660	# main subject: artificial intelligence
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/20025421"
LAST	P953	"https://stephane-lalut.com/awp/awp-06/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-06/"	P407	Q1860
```

---

# PHASE C — Finitions et maillage avancé

> **À exécuter après Phase B validée et stabilisée (>72h sans contestation).**
> Risque très faible. Volume ~20 déclarations.

## C.1 — Rétro-liens depuis la série vers ses AWPs

Une fois les 6 items AWP créés, ajouter sur Q139040913 la liste de ses parties :

```quickstatements
# Remplacer Q-AWP-NN par les QIDs obtenus en Phase B
Q139040913	P527	Q-AWP-01	# has part(s): AWP-01
Q139040913	P527	Q-AWP-02	# has part(s): AWP-02
Q139040913	P527	Q-AWP-03	# has part(s): AWP-03
Q139040913	P527	Q-AWP-04	# has part(s): AWP-04
Q139040913	P527	Q-AWP-05	# has part(s): AWP-05
Q139040913	P527	Q-AWP-06	# has part(s): AWP-06
```

## C.2 — Liens AWP ↔ Livres (œuvre dérivée / source théorique)

```quickstatements
# AWP-03 dérive du livre Dette Publique
Q-AWP-03	P1343	Q138910896	# described by source: livre Dette Publique
# AWP-01 dérive du livre ANTHROPIE
Q-AWP-01	P1343	Q138827344	# described by source: livre ANTHROPIE
```

## C.3 — Concepts dérivés (création différée — décision Laura)

**⚠️ Décision éditoriale requise.** Trois concepts dérivés notables :
- *Paradoxe terminal de l'anthropie*
- *Créanciers invisibles*
- *Quadruple peine*

**Recommandation prudente : NE PAS créer maintenant.** Risque de proposition à la suppression élevé (hyper-spécifique, source unique). Attendre :
- soit une citation par un tiers indépendant dans une revue à comité,
- soit un retour public sur les AWPs.

Sinon, format de création (à activer plus tard) :
```quickstatements
CREATE
LAST	Lfr	"Paradoxe terminal de l'anthropie"
LAST	Dfr	"Concept théorique de Stéphane Lalut désignant la limite de l'absorption du désordre"
LAST	P31	Q151885	# concept
LAST	P361	Q138827949	# part of: anthropy
LAST	P61	Q138909233	# discoverer: Lalut
LAST	P973	"https://stephane-lalut.com/glossaire/#paradoxe-terminal"	P407	Q150
```

---

# § 9. Checklist pré-batch (à dérouler par Laura avant chaque exécution)

- [ ] **Phase A — Items existants** : ouvrir chaque QID (Q138909233, Q138827949, etc.) dans un onglet. Pour chaque déclaration du batch, vérifier qu'elle n'existe pas déjà (sinon QuickStatements la dupliquera).
- [ ] **Phase B — Recherche doublons** : interroger https://hub.toolforge.org/P356:[chaque DOI] pour les 6 DOIs Zenodo FR. Si match, substituer CREATE par QID.
- [ ] **Q-IDs marqués [À VÉRIFIER]** : ouvrir wikidata.org, taper le label (ex. « hypothesis »), vérifier que le Q-ID retourné correspond. Substituer si erreur.
- [ ] **P-IDs marqués** : idem sur properties (ex. P5715 pour Academia.edu).
- [ ] **Mode preview QuickStatements** : ne JAMAIS cliquer Run sans avoir vu le preview en mode "import V1" avec validation visuelle.
- [ ] **Découpage** : si > 80 commandes dans un batch, fractionner en deux.
- [ ] **Cinétique** : laisser ≥ 48h entre Phase A et Phase B, ≥ 72h entre Phase B et Phase C.

---

# § 10. Checklist post-batch

- [ ] **H+1** : vérifier chaque item modifié sur wikidata.org → onglet "View history" → confirmer absence d'undo.
- [ ] **H+24** : recharger chaque item, vérifier absence de bannière "Proposed for deletion" et absence de message en page Discussion.
- [ ] **H+72** : refaire un check global. Si proposition de suppression sur un item AWP, défendre via : sources Zenodo + SSRN + MPRA + OpenAlex (4 plateformes indépendantes = critère de pérennité multi-sourcée).
- [ ] **Si annulation nécessaire** : utiliser EditGroups (https://editgroups.toolforge.org/) — chaque batch QuickStatements y est tracé et rollback possible en un clic.

---

# § 11. Patch site Hugo (D:\anthropie\anthropie-site)

Pour activer le maillage **site → Wikidata**, prompt à coller dans Claude Code :

```
Patch Hugo : injecter des liens canoniques vers Wikidata dans le JSON-LD.

1. Dans data/author.toml, ajouter dans sameAs :
   "https://www.wikidata.org/wiki/Q138909233"
   (vérifier que ce lien y figure ; sinon l'ajouter en respectant la convention 
   actuelle des 8 entrées sameAs)

2. Dans le frontmatter des pages AWP (content/awp/awp-NN.md et content/en/awp/awp-NN.md),
   ajouter un champ optionnel :
   wikidata: "Q-XXXXXXX"
   (à compléter manuellement après Phase B, quand les QIDs des AWPs seront connus)

3. Dans layouts/awp/single.html, si le champ wikidata est présent dans le front matter,
   ajouter une balise dans le JSON-LD ScholarlyArticle :
   "sameAs": ["https://www.wikidata.org/wiki/{{ .Params.wikidata }}", ...]

4. Sur les pages livres (content/livres/anthropie-ordre-ici-dette-ailleurs.md
   et content/livres/dette-publique-qui-paie-vraiment.md), ajouter dans le frontmatter :
   wikidata: "Q138827344" (livre ANTHROPIE)
   wikidata: "Q138910896" (livre Dette Publique)

5. Sur layouts/livres/single.html, injecter sameAs Wikidata dans le JSON-LD Book.

6. Sur la page concept https://stephane-lalut.com/quest-ce-que-lanthropie/,
   ajouter dans le JSON-LD :
   "sameAs": "https://www.wikidata.org/wiki/Q138827949"

7. Sur la page série https://stephane-lalut.com/serie-awp/, ajouter :
   "sameAs": "https://www.wikidata.org/wiki/Q139040913"

Lire PROJECT_STATUS.md avant intervention.
Commit atomique par page modifiée. PR via GitHub UI.
```

---

# § 12. Notes de prudence

1. **Capital Wikidata de Laura.** Ne pas tout exécuter en une journée. Étalement 2-3 semaines minimum.
2. **Patrouilleurs.** Si un patrouilleur questionne, ne pas argumenter en chaîne. Une seule réponse sourcée, puis laisser l'item exister par décantation.
3. **AWP-06 ne sera pleinement légitimable sur Wikidata** qu'après son acceptation MPRA (statut actuel « Under Review »). Décision prudente : créer l'item maintenant mais ne pas s'étonner si la notabilité est questionnée tant que MPRA n'a pas approuvé.
4. **Wikipedia.** Aucun lien Wikipedia n'est créé ici. Conformément à la doctrine en mémoire : « Deferred until more independent sources accumulate. »
5. **L'item Q138911733 (Odyssée des Idées)** est le maillon le plus fragile (livre 2023, peu de visibilité actuelle). Si une proposition de suppression apparaît, ne pas s'en alarmer — corriger d'abord les erreurs structurelles (P50 absent), et laisser le maillage faire son travail.

---

# § 13. Récapitulatif des actions Laura

| Étape | Durée | Délai |
|---|---|---|
| Lecture du fichier + check P-IDs/Q-IDs | 45 min | J |
| Phase A — Items existants (batch unique) | 30 min | J+1 |
| Phase B — Création AWPs (3 sous-batches de 2 items chacun) | 45 min × 3 sessions | J+3, J+7, J+10 |
| Phase C — Maillage final | 20 min | J+14 |
| Surveillance globale | 5 min × jour × 14j | J→J+14 |

**Total effort Laura** : ~6-7h cumulées sur 2 semaines.
**Total effort Stéphane** : décision sur les concepts dérivés (§ C.3) uniquement.
**Total effort site Hugo (via Claude Code)** : 1 prompt unique (§ 11), ~20 min.

---

*Fichier produit le 11 mai 2026. À conserver dans `D:\anthropie\anthropie-site\docs\wikidata\` ou équivalent. Ne pas committer dans un repo public tant que Laura n'a pas validé les Q/P-IDs marqués [À VÉRIFIER].*
