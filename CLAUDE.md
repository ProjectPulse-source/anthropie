# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stack

Static site for **anthropie.fr** (Stéphane Lalut, économiste). Hugo Extended **0.147.0**, Sass natif Hugo, vanilla JS, **zéro dépendance npm**. Decap CMS via GitHub backend + Netlify OAuth proxy. Déployé sur GitHub Pages via `.github/workflows/hugo.yml` à chaque push sur `main`.

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

- **`awp/`** — *Anthropie Working Papers* (AWP-01..05). Pièces maîtresses académiques. Front matter riche : `awp_number`, `doi_zenodo`, `url_zenodo`, `pdf_url`, `jel_codes`, `keywords[_en]`, `faq[]`, `translation.{doi,url,title}`, `related[]` (slugs d'autres AWP), `related_book`. Le bloc `faq` alimente `partials/schema-faqpage.html` (JSON-LD FAQPage).
- **`livres/`** — fiches livres avec liens Amazon (placeholders ASIN à remplacer, voir README).
- **`publications/`** — recensions/articles publiés ailleurs ; cartes via `partials/publication-card.html` avec gabarit logo/photo unique 160×107 (cf. commits récents).

Les sections `presse/`, `glossaire/`, `a-propos/`, `quest-ce-que-lanthropie/`, `serie-awp/`, `contact/` n'ont qu'un `_index.md` (+ `.en.md`).

## Layouts & partials clés

- `layouts/_default/baseof.html` → squelette commun, charge `partials/head.html` + `header.html` + `footer.html`.
- `partials/cross-language-banner.html` → bandeau de bascule fr↔en, lit `translation.url` du front matter.
- `partials/how-to-cite.html` → bloc citation (lié aux outputs BibTeX/RIS).
- `partials/related-awp.html` + `partials/awp-card.html` → graphe de navigation entre working papers via le champ `related[]`.
- `partials/schema-itemlist.html`, `schema-faqpage.html` → JSON-LD pour le SEO académique.
- `partials/background-anthropie.html` → fond SVG décoratif. Le fichier `assets/js/hero-flowfield.js` existe dans le dépôt mais n'est plus chargé (canvas supprimé lors du redesign home).

`data/awp_short_titles.yaml` mappe les slugs AWP vers leurs titres courts (utilisé par les cartes pour éviter de réimporter la page entière).

## CSS

Point d'entrée `assets/scss/main.scss` qui importe les partials `_variables`, `_typography`, `_layout`, `_components`, `_hero`, `_academic`, `_book-single`, `_publication-card`, `_related-awp`, `_amazon-button`, `_anthropie-bg`, `_how-to-cite`, `_awp-single`, `_serie-awp`, `_home`. Les paramètres de design exposés à Hugo (taille H1 hero, gabarit emblème livre) vivent sous `[params.design]` dans `hugo.toml` — modifier là plutôt qu'en dur dans le SCSS quand la valeur est référencée par un template.

## CMS

`static/admin/config.yml` (Decap) référence `[USERNAME]` (compte GitHub) et `[NETLIFY-SITE]` (proxy OAuth) — placeholders à remplacer avant déploiement réel du CMS.

## Conventions de contenu

- Typographie française : espaces insécables (`&nbsp;`) avant `:`, `;`, `?`, `!` dans les `.md` français — voir `partials/fr-typo.html` et les fichiers AWP existants.
- `unsafe = true` dans le renderer Goldmark : HTML inline autorisé dans le markdown.
- Tout nouveau working paper doit fournir `doi_zenodo` + `url_zenodo` + `pdf_url` (Zenodo community `anthropie-working-papers`) et un pendant `.en.md` avec `translation` croisé.
