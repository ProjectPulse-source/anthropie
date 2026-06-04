# Anthropie — Site de Stéphane Lalut

Site statique Hugo pour [stephane-lalut.com](https://stephane-lalut.com).

## Stack

- **Générateur** : Hugo Extended 0.147.0
- **Hébergement** : GitHub Pages via GitHub Actions
- **CSS** : Sass natif Hugo
- **JavaScript** : Vanilla uniquement
- **Dépendances** : Aucune (zéro npm)

## Placeholders à remplacer

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
