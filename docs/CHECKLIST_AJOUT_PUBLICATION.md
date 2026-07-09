# Checklist — Ajout d'une fiche publication

> Miroir de `CHECKLIST_AJOUT_AWP.md` pour la section `content/publications/`.
> Créée suite à l'audit GEO-03 du 2026-07-08. **Lire `NOTES_PUBLICATIONS.md`
> avant** (taxonomie `source_type`, règle d'or SCSS BEM des cartes).

## 1. Fiche `content/publications/<slug>.md`

Modèle : `revue-projet-commune-republique.md` (2026-07-07).

- [ ] `title`, `date`, `revue`, `source_type` (taxonomie de
      `NOTES_PUBLICATIONS.md` : Revue / Magazine / Quotidien / Journal /
      Portail ; « Académique » réservée, activation sur décision).
- [ ] `url_externe` — l'article publié ailleurs (c'est lui que la carte
      et l'`ItemList` JSON-LD de `/publications/` pointent).
- [ ] `image_type` (logo/photo, gabarit unique 160×107).
- [ ] `chapo` + `chapo_en` — titres d'œuvres en `<em>…</em>`, jamais en
      `*markdown*` (rendu via `safeHTML` dans `publication-card.html`).
- [ ] `related: [awp-NN, …]` — AWP prolongés, **ordre chronologique
      croissant** (alimente le graphe related-awp).
- [ ] `related_book: <slug>` si la publication éclaire un livre.
- [ ] **Doctrine noindex (actée audit GEO 2026-07-04, item 1.3a)** : tant
      que le corps de la fiche est quasi vide, ajouter :
      `noindex: true` + `sitemap: disable: true` (la carte reste listée,
      le sitemap n'est pas dilué). **Bascule** : si la fiche est un jour
      enrichie en vraie page de preuve, retirer ces deux blocs.
- [ ] **Pas de pendant `.en.md`** (choix éditorial acté : la fiche reste
      dans la langue de la revue source ; `/en/publications/` rend les
      cartes FR par fallback).

## 2. Registres à synchroniser

- [ ] `data/works.yaml` : entrée/mise à jour de l'œuvre (cf. commit
      `470f6fa` qui touche la fiche ET works.yaml).
- [ ] `static/llms.txt` : section publications, à la main.
- [ ] Typographie française : espaces insécables avant `: ; ? !`
      (cf. `partials/fr-typo.html` et fiches existantes).

## 3. Vérifications avant commit

- [ ] `hugo server` : carte visible sur `/publications/` (alternance
      logo navy/crème automatique), lien externe correct, chapô propre ;
      la fiche apparaît dans l'`ItemList` JSON-LD si `url_externe` présent.
- [ ] `python scripts/check-corpus-counters.py` → exit 0.
- [ ] `python scripts/audit_works.py` → pas de warning nouveau.

## 4. Indexation (après merge sur `main`)

La fiche elle-même est `noindex` : c'est **la page liste `/publications/`**
(indexée, ItemList JSON-LD) et **l'article externe** qui portent la
visibilité. Le push déclenche IndexNow (Bing/Yandex/…) qui resoumet le
sitemap complet, dont `/publications/`.

- [ ] Vérifier le nombre d'URLs extraites dans le log du run IndexNow.
- [ ] Si actualité chaude : Search Console → « Demander une indexation »
      sur `/publications/` (la liste, pas la fiche noindex).
