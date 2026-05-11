# Checklist — Ajout d'un nouvel AWP

Procédure compacte pour ajouter un *Anthropie Working Paper* (AWP-NN) sur le site, sans rater de surface dépendante. À suivre dans l'ordre.

## 1. Dépôt Zenodo FR et EN

Dépôt FR sur la communauté Zenodo `anthropie-working-papers`, licence CC-BY 4.0. Dépôt EN en second pour obtenir un DOI EN distinct. Lier les deux dépôts via `isDerivedFrom` (FR canonique, EN traduction). Récupérer les deux DOIs `10.5281/zenodo.XXXXXXX` et les URLs `https://zenodo.org/records/XXXXXXX`.

## 2. Création des fichiers content

Convention multilingue Hugo **par suffixe** (pas par sous-dossier) :

- `content/awp/awp-NN.md` — version FR
- `content/awp/awp-NN.en.md` — version EN

Ne pas créer de bundle `content/awp/awp-NN/index.md`. Le repo utilise le format flat avec suffixe `.en.md`, cohérent avec `defaultContentLanguageInSubdir = false`.

## 3. Frontmatter minimal

S'aligner sur un AWP existant (par exemple `awp-05.md`) pour la complétude. Champs requis : `title`, `date`, `doi_zenodo`, `url_zenodo`, `pdf_url`, `abstract`, `citation_pdf_url`, `jel_codes`, `keywords[_en]`, `faq[]`, `translation.{doi,url,title,is_canonical}`, `related[]`, `related_book` (si pertinent).

## 4. Mise à jour `data/works.yaml`

Nouvelle entrée AWP avec `type: awp`, `series_number: N`, `canonical_title.{fr,en}`, `publication_date_fr`, `publication_date_en`, blocs `deposits.{zenodo_fr,zenodo_en,ssrn_en,mpra_en}`, `site_pages.{fr,en}`. Conserver l'ordre chronologique des entrées.

## 5. Rendu local Hugo + vérifications

Lancer `hugo server` et vérifier sur les deux URLs FR et EN : balises `<meta name="citation_*">` présentes, lien hreflang, JSON-LD `ScholarlyArticle` et `FAQPage` valides (extension Schema Markup Validator ou copier-coller dans schema.org/validator).

## 6. Linter cohérence corpus

Exécuter `python scripts/check-corpus-counters.py`. Doit sortir code 0 (aucune divergence). Si le linter détecte un chiffre dur obsolète (par exemple `cinq Anthropie Working Papers` quand on passe à 6) : corriger les occurrences listées avant commit.

## 7. Mise à jour du hero index (FR + EN)

Le hero de `layouts/index.html` (lignes 18-22) affiche `X Anthropie Working Papers, deux livres` en FR et `X Anthropy Working Papers, two books` en EN, où **X est écrit en lettres** (`cinq`, `six`, `seven`/`sept`, etc.). À chaque ajout d'AWP, incrémenter X dans **les deux blocs** (`if eq .Lang "en"` et `else`).

Le compteur livres reste `deux` / `two` : il désigne le **cadre anthropique** stricto sensu (livres ANTHROPIE + Dette Publique), pas le corpus livres total (qui inclut *Livresque des mots*, antérieur et hors série).

## 8. Maillage avec `/publications/`

Si le nouvel AWP **prolonge** une recension ou un article déjà publié dans `content/publications/*.md` : ajouter `awp-NN` au champ `related: [...]` du frontmatter de la fiche concernée. Préserver l'ordre chronologique croissant (`awp-01`, `awp-04`, `awp-06` plutôt que `awp-06`, `awp-01`).

Le libellé visible humain est généré par i18n : clé `pub_related_label` (`"Prolonge :"` FR / `"Extends:"` EN). Le champ `related:` se rend automatiquement.

## 9. Build production + vérification HTTP

`hugo --minify`. Si déploiement GitHub Pages : push sur `main` déclenche le workflow `.github/workflows/hugo.yml`. Après quelques minutes, vérifier HTTP 200 sur :

- `https://stephane-lalut.com/awp/awp-NN/`
- `https://stephane-lalut.com/en/awp/awp-NN/`
- `https://stephane-lalut.com/` (hero compteur mis à jour)
- `https://stephane-lalut.com/en/` (idem)

## 10. Note convention bilinguisme publications

Aucune traduction `.en.md` n'est créée pour les fiches `content/publications/*.md`. Choix éditorial : les fiches publication restent en FR (langue de la revue source) sur les deux versions du site. La page `/en/publications/` rend les fiches FR via fallback multilingue Hugo. Ne pas créer de `*.en.md` dans `content/publications/` sauf décision éditoriale explicite.
