# Wayback Machine — Archivage automatique

Ce dossier centralise l'archivage automatique du site `stephane-lalut.com` sur
Internet Archive via le service Save Page Now.

## Mécanisme

Le workflow GitHub Actions `wayback-archive.yml` s'exécute :

- **Automatiquement** le 1er de chaque mois à 6h UTC
- **Manuellement** via l'onglet Actions du repo GitHub (déclenchement workflow_dispatch)

À chaque run, il :

1. Récupère le sitemap canonique `https://stephane-lalut.com/sitemap.xml`
2. Extrait toutes les URLs (FR + EN)
3. Pour chaque URL, appelle `https://web.archive.org/save/<URL>` (politesse : 5s entre requêtes)
4. Enregistre le résultat (status HTTP + timestamp de snapshot) dans `archive-log.md`
5. Commit et push le log

## Fichiers

- `archive-log.md` : journal cumulatif de tous les runs (ajout en bas à chaque exécution)
- `README.md` : ce document

## Pourquoi cet archivage est important

### Robustesse face à la disparition du site

Si pour une raison quelconque `stephane-lalut.com` devient inaccessible (problème
DNS, indisponibilité OVH, fin de domaine), les URLs archivées sur Wayback Machine
restent consultables à perpétuité via leurs snapshots horodatés.

### Citations académiques pérennes

Les chercheurs qui citent une URL du site dans leurs publications peuvent
pointer vers la version Wayback (URL stable horodatée) plutôt que vers
l'URL vivante (susceptible de changer). Cela renforce la fiabilité bibliographique
des AWPs et articles.

### Preuve antérieure

L'archivage horodaté constitue une preuve datée du contenu publié à un instant T.
Utile en cas de litige sur la primauté d'une idée ou d'une formulation.

### Alimentation des corpus LLM

Wayback Machine est l'une des sources les plus utilisées par les projets de
recherche LLM (Common Crawl, CCNet, RedPajama). Une URL archivée a plus de
chances d'entrer dans un corpus d'entraînement futur que la même URL vivante
mais ponctuellement inaccessible lors d'un crawl.

## Format du log

Chaque run produit une entrée Markdown avec :

```
## Run du YYYY-MM-DD HH:MM:SS UTC

- Total URLs : N
- Succès : N
- Échecs : N

| URL | Status | Snapshot |
|---|---|---|
| https://stephane-lalut.com/.../ | OK | `20260513120000` |
```

Le `snapshot` est le timestamp Wayback. URL de consultation directe :
`https://web.archive.org/web/<snapshot>/<URL>`

## Codes statut

- **OK** : archivage réussi, snapshot disponible
- **FAIL(403)** : refusé par Wayback Machine (URL probablement en robots.txt ou rate limit)
- **FAIL(429)** : rate limit Wayback (trop de requêtes — réessayer plus tard)
- **FAIL(523)** : timeout Wayback (URL inaccessible)
- **TIMEOUT** : timeout côté script (> 60s)
- **ERROR(...)** : exception Python lors de l'appel

En cas d'échecs récurrents (> 30% des URLs), le workflow émet un warning visible
dans l'onglet Actions du repo.

## Limites connues

- Pas d'authentification S3-like activée : rate limit standard (suffisant pour
  un site < 100 pages, ce qui est le cas)
- Le workflow ne ré-essaie pas les URLs en échec automatiquement (à faire
  manuellement via `workflow_dispatch` si besoin)
- Wayback Machine peut ignorer les requêtes si l'URL a été archivée récemment
  (politique de cache interne) — c'est normal et non problématique
