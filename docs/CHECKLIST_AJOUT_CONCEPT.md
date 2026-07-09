# Checklist — Ajout d'une page concept

> Troisième volet du triptyque (AWP / livre / publication). Une page concept
> est un événement rare : elle ne se crée **qu'en réaction à un signal
> externe** (doctrine PROJECT_STATUS §7), jamais en anticipation. Modèle :
> `/quest-ce-que-lanthropie/` (refonte GEO-01 du 2026-07-04).

## 0. Conditions d'ouverture

- [ ] Signal externe documenté (demande d'un tiers, citation, traction de
      requête vérifiée) — pas une intuition d'optimisation.
- [ ] Le concept ne peut pas être traité par un bloc H2/FAQ sur une page
      existante (test de suppression : la page dédiée apporte-t-elle plus
      que l'enrichissement ?).
- [ ] Slug plat (`/mon-concept/`), pas de section `/concepts/` (acté 04/07).

## 1. Contenu (anatomie de la page concept)

- [ ] **Définition canonique en ouverture** — une phrase citable, stable.
      Si le concept a vocation à être répété sur plusieurs surfaces :
      single-sourcer le verbatim dans `config/_default/params.toml` (modèle
      `canonicalDefinition` + shortcode dédié) ; sinon verbatim en dur mais
      unique.
- [ ] Étymologie / origine — ne jamais laisser croire à une invention du
      mot si des usages antérieurs existent (leçon GEO-01).
- [ ] Section « À distinguer de » — concepts voisins et homonymes.
- [ ] Section « Objections et limites » — la branche sceptique fait partie
      de la couverture (audit QEA 04/07).
- [ ] `faq[]` au front matter : questions réelles, réponses autosuffisantes.
      **Aucun chiffre canonique en dur** dans les `answer` (source unique
      `data/works.yaml` corpus_stats).
- [ ] Titres H2/H3 en forme de questions quand c'est naturel ; typographie
      française (espaces insécables).

## 2. Bilinguisme et URLs

- [ ] Pendant `.en.md` systématique (les concepts, contrairement aux fiches
      livres/publications, sont bilingues — parité AWP).
- [ ] ⚠ `slug:` est **ignoré** sur les `_index.md` de section : l'URL EN
      reste le nom du dossier. Pour une URL EN propre, utiliser `url:` dès
      la création, ou assumer l'URL FR + `aliases:` (chemins absolus résolus
      depuis la racine du site, préfixe de langue à écrire soi-même —
      cf. correctif what-is-anthropy, 2026-07-09).
- [ ] Vérifier hreflang + bannière cross-language.

## 3. JSON-LD

- [ ] Nœud `DefinedTerm` avec `@id` stable (`<url>#concept`), `name`,
      `description` (= définition canonique), `sameAs` (item Wikidata dès
      qu'il existe).
- [ ] Les pages qui parlent du concept le référencent en `about` avec le
      **même `@id`** (modèle : AWP/livres → `#concept` anthropie).
- [ ] FAQPage émise automatiquement via `faq[]` (rien à faire de plus).

## 4. Registres et maillage

- [ ] `data/intent_matrix.yaml` : entrée du concept (cercles de requêtes,
      statuts) — c'est le déclencheur de mise à jour prévu par sa doctrine.
- [ ] `static/llms.txt` : section concepts, à la main.
- [ ] Maillage entrant : depuis les AWP/livres/pages qui mobilisent le
      concept. Maillage sortant : livre principal, AWP fondateur, concepts
      voisins.
- [ ] Item Wikidata du concept (à créer via le pipeline `Wikidata/scripts/`)
      + P973 vers la page — **avec l'URL réellement servie** (vérifier le
      build, pas le front matter).

## 5. Vérifications et indexation

- [ ] `hugo --minify` OK ; page dans le sitemap ; canonical correct.
- [ ] `python scripts/check-corpus-counters.py` → exit 0.
- [ ] Push → IndexNow automatique ; vérifier le nombre d'URLs dans le log.
- [ ] Search Console « Demander une indexation » (facultatif, 24-48 h).
