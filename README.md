# Anthropie — Site de Stéphane Lalut

Site statique Hugo pour [anthropie.fr](https://anthropie.fr).

## Stack

- **Générateur** : Hugo Extended 0.147.0
- **CMS** : Decap CMS (backend GitHub + proxy OAuth Netlify)
- **Hébergement** : GitHub Pages via GitHub Actions
- **CSS** : Sass natif Hugo
- **JavaScript** : Vanilla uniquement
- **Dépendances** : Aucune (zéro npm)

## Placeholders à remplacer

- `[USERNAME]` dans `static/admin/config.yml` : votre nom d'utilisateur GitHub
- `[NETLIFY-SITE]` dans `static/admin/config.yml` : le sous-domaine Netlify pour le proxy OAuth
- URLs Amazon dans les fichiers `content/livres/*.md` : ASINs/URLs Amazon réels
- `VOTRE_ID` dans `content/contact/_index.md` : identifiant Formspree

## Développement local

```bash
hugo server -D
```

## Build

```bash
hugo --minify
```
