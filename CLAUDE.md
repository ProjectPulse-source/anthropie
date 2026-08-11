# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stack

Static site for **stephane-lalut.com** (Stéphane Lalut, économiste). Hugo Extended **0.147.0**, Sass natif Hugo, vanilla JS, **zéro dépendance npm**. Déployé sur GitHub Pages via `.github/workflows/hugo.yml` à chaque push sur `main`. *(Le domaine anthropie.fr n'a jamais été détenu — aftermarket Premium GoDaddy, dossier clos 2026-06-04 : ne jamais le référencer comme site vivant.)*

## Commandes

```bash
hugo server -D            # dev local (inclut drafts)
hugo --minify             # build de production -> ./public
```

Aucun lint/test : pas de toolchain JS, pas de package.json. La validation est visuelle + via le build CI Hugo.

## Configuration Hugo

Config splittée dans `config/_default/` : `hugo.toml` (langues, outputs, markup), `menus.toml`, `params.toml`. Site bilingue **fr (default) / en**, sans préfixe pour le français (`defaultContentLanguageInSubdir = false`). Les pages anglaises vivent côte à côte en `*.en.md`.

Output formats custom **BibTeX** (`citation.bib`), **RIS** (`citation.ris`) et **EndNote** (`citation.enw`) déclarés pour la section `awp` — chaque working paper expose donc quatre sorties : `single.html`, `single.bibtex.bib`, `single.ris.ris`, `single.endnote.enw` (voir `layouts/awp/`).

L'URL `/awp/` redirige (meta-refresh via `aliases`) vers `/serie-awp/`, qui est le point d'entrée éditorial de la série. Les pages AWP individuelles restent à `/awp/awp-01/` etc.

## Architecture du contenu

Les sections `content/` mappent 1-1 aux sections sémantiques du site. Trois familles avec layouts dédiés :

- **`awp/`** — *Anthropie Working Papers*. Pièces maîtresses académiques, au front matter riche (lire un fichier existant pour la liste des champs). Le bloc `faq` alimente `partials/schema-faqpage.html` (JSON-LD FAQPage).
- **`livres/`** — fiches livres avec liens Amazon.
- **`publications/`** — recensions/articles publiés ailleurs ; cartes via `partials/publication-card.html`, gabarit logo/photo unique 160×107.

## Layouts & partials clés

Le squelette commun est `layouts/_default/baseof.html` ; le détail des partials se lit dans `layouts/partials/`.

⚠ `assets/js/hero-flowfield.js` existe dans le dépôt mais n'est plus chargé (canvas supprimé lors du redesign home).

## CSS

Point d'entrée `assets/scss/main.scss`. Les paramètres de design exposés à Hugo (taille H1 hero, gabarit emblème livre) vivent sous `[params.design]` dans `hugo.toml` — modifier là plutôt qu'en dur dans le SCSS quand la valeur est référencée par un template.

## Ajout d'un nouvel AWP

Procédure compacte documentée dans [`docs/CHECKLIST_AJOUT_AWP.md`](docs/CHECKLIST_AJOUT_AWP.md). Points sensibles à retenir :

1. **Convention multilingue par suffixe** : créer `content/awp/awp-NN.md` (FR) + `content/awp/awp-NN.en.md` (EN). Pas de bundle `content/awp/awp-NN/index.md`.
2. **Hero index à mettre à jour manuellement** : `layouts/index.html` lignes 18-22 contient le compteur AWP écrit en lettres (FR et EN). À incrémenter à chaque ajout.
3. **Linter de cohérence** : `python scripts/check-corpus-counters.py` doit sortir 0 avant commit. Détecte les chiffres durs obsolètes (`cinq Anthropie Working Papers` quand on passe à 6, etc.).
3 ter. **Doctrine du dépôt échelonné** (décision auteur, 2026-08-02) — vaut pour SSRN, MPRA, SocArXiv et toute plateforme à modération : **jamais plus de 1 à 2 dépôts à la fois**. On dépose, on surveille avec `python scripts/check_deposits_status.py`, et **on ne pose le suivant qu'une fois le précédent ACCEPTÉ**. Preuve : 5 dépôts MPRA en 18 minutes le 07/04/2026 sont restés bloqués 118 jours, alors qu'un dépôt isolé le 08/05 a été accepté en 7 jours. Ne jamais rattraper un retard en déposant en lot — c'est ce qui crée le blocage qu'on cherche à résorber.
3 bis. **Audit Zenodo** : `python scripts/zenodo_audit_complet.py` doit sortir **0 bloquant** (ajouter la nouvelle paire dans `PAIRS` d'abord). Vérifie verbatim canonique, ORCID, licence, langue, mots-clés, communauté, `isDescribedBy` https et liaison de traduction réciproque. Motif : AWP-08 était sorti sans ORCID ni communauté (détecté et corrigé le 2026-08-02) — les dépôts manuels sont l'endroit où se creusent les trous.
4. **Maillage publications** : si l'AWP prolonge une fiche `content/publications/*.md`, ajouter `awp-NN` au champ `related:` du frontmatter, ordre chronologique croissant.
5. **Pas de traduction `.en.md` pour `content/publications/`** : choix éditorial, fallback multilingue Hugo.

## Méthodologie de patch

Ce dépôt suit la doctrine cross-projets définie dans
`~/.claude/CLAUDE.md` (lue par Claude Code à chaque session).

Avant tout patch substantiel, lecture obligatoire dans cet ordre :

1. `PROJECT_STATUS.md`
2. ce fichier (`CLAUDE.md`) pour les conventions locales

Contextualisations propres à ce repo :

- Linter cohérence corpus : `scripts/check-corpus-counters.py`
- Linter couverture GEO (FR + miroir EN) : `scripts/check-geo-coverage.py`
- Linter encodage console : `scripts/check-console-encoding.py` — un `print()`
  contenant « ✓ », « → » ou un emoji fait sortir **1** un script sain sous
  console Windows cp1252, ce qui est indiscernable d'un vrai échec. Le cookie
  `# -*- coding: utf-8 -*-` ne protège pas : il déclare l'encodage de la source,
  pas celui de `stdout`.
- Checklist d'ajout d'AWP : `docs/CHECKLIST_AJOUT_AWP.md`
- Convention multilingue Hugo : suffixe `.en.md` (pas sous-dossier
  `content/en/`)
- Source unique d'identité auteur : `data/author.toml`

**Règle de fraîcheur d'état (« l'état écrit suit l'acte »)** : toute session
qui exécute un travail met à jour, dans la même session, (1) le log § 0 de
`PROJECT_STATUS.md`, (2) le statut des backlogs et registres touchés
(`data/works.yaml`, `reports/**/12_IMPLEMENTATION_BACKLOG.md`, fiches de
mission), (3) `static/llms.txt` si un fait qu'il énonce a changé. Symétrique :
avant de reprendre un backlog ou une consigne, vérifier ses statuts contre le
git log — un statut périmé provoque soit la re-exécution d'un acquis, soit
l'abandon d'un travail cru fait. Constat fondateur (arbitrages GEO-01→03,
2026-08-02) : la péremption d'état était l'unique défaut récurrent du
système, retrouvé dans le backlog, works.yaml, llms.txt et la mémoire.
Complément (contre-expertise 02/08) : **l'état interne suit l'acte ;
l'état externe expire** — tout relevé d'observation externe (SERP, mode IA,
concurrent, plateforme) porte sa date, son contexte (pays/langue/connexion/
moteur/requête exacte) et une durée de validité ; passé ce délai, il
redevient une hypothèse à re-vérifier, pas un fait. Registre des collisions
de nom/concept : `reports/geo_audit/REGISTRE_COLLISIONS.md` (hors dépôt) —
input obligatoire de toute nouvelle langue ou surface.

## Règle de surface — « la présence vient du dépôt » (actée 2026-08-11)

Défaut récurrent, six occurrences en deux jours, toujours la même forme : **une donnée
existe quelque part et la surface qui la consomme ne la reçoit pas — sans erreur, sans
warning, sans trace.** Un livre publié absent du mur `/a-propos/` ; `pages` manquant sur
une fiche, donc pas de pagination sur deux pages ; `subtitle` manquant, donc pas de hook ;
deux QID Wikidata connus de `works.yaml` mais jamais déclarés en fiche, donc pas de
`sameAs` ; un compteur de corpus périmé ; une page traduite qui ne le disait pas. Aucune
n'a été trouvée par l'appareil : toutes par l'auteur, en regardant le site.

Trois règles en découlent, à appliquer à **toute** surface qui agrège ou reflète du contenu :

1. **La présence vient du dépôt, l'éditorial du front matter.** Un gabarit n'énumère
   jamais à la main ce que `content/` sait déjà. Le front matter ne porte que ce qui ne
   se déduit pas (une ligne éditoriale, une étiquette), en **table de surcharges indexée
   par slug**, avec repli. Toute valeur dérivable (pagination, titre, URL, couverture,
   traduction) se **dérive** — la recopier, c'est programmer sa dérive.
2. **Une exclusion peut être légitime ; le silence, jamais.** Quand une liste manuelle se
   justifie (ex. `$order` de `/ressources-offertes/`, où l'on retire un livre sans stock),
   elle porte un `warnf` sur ce qu'elle omet. Idem pour un champ éditorial absent : la
   tuile s'affiche **et** le build avertit — ne jamais faire disparaître l'objet.
3. **Le registre est la source, la fiche doit le refléter.** `scripts/check-fiches-registre.py`
   compare fiches et `data/works.yaml` (QID, pagination, ISBN) et signale « le registre le
   sait, la fiche ne le dit pas ». À lancer avant commit, comme les autres linters.

⚠ Un `warnf` **ne survit pas à `hugo --quiet`** (faux négatif observé le 11/08 en testant
la première garde). La CI utilise `hugo --minify` sans `--quiet` : ne pas changer cela.
Et un garde-fou se **teste par mutation réelle puis restauration**, jamais par relecture
du code.

## Conventions de contenu

- Typographie française : espaces insécables (`&nbsp;`) avant `:`, `;`, `?`, `!` dans les `.md` français — voir `partials/fr-typo.html` et les fichiers AWP existants.
- `unsafe = true` dans le renderer Goldmark : HTML inline autorisé dans le markdown.
- Tout nouveau working paper doit fournir `doi_zenodo` + `url_zenodo` + `pdf_url` (Zenodo community `anthropie-working-papers`) et un pendant `.en.md` avec `translation` croisé.
