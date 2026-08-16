# Scripts Wikidata — automatisation génération de batches

Génère des fichiers `.qs` QuickStatements pour les nouvelles publications.
**Aucune communication directe avec Wikidata.** Tous les batches passent
par validation humaine avant transmission à Laura.

## Prérequis

Python 3.10+. Aucune dépendance externe (stdlib uniquement).

## Usage

Depuis `Wikidata/scripts/` :

### Nouvel AWP

```powershell
python generate_wikidata_batch.py awp --zenodo-doi 10.5281/zenodo.XXXXXXXX --awp-number 7
```

Optionnel : `--zenodo-doi-en` pour la version EN.

### Nouvel article de revue

```powershell
python generate_wikidata_batch.py article --title "Titre de l'article" --url "https://..." --date 2026-05-13
```

Optionnel : `--journal-qid Q...`, `--language en`, `--doi 10...`.

### Nouveau livre

```powershell
python generate_wikidata_batch.py book --isbn 978-2-9586347-X-X --title "Titre" --date 2026
```

Optionnel : `--subtitle`, `--asin`, `--amazon-url`.

## Workflow complet

1. Lance le script avec les paramètres requis.
2. Le script fetch les métadonnées (Zenodo / Crossref / OpenLibrary).
3. Le script valide le batch (regex DOI, contraintes Wikidata).
4. Si validation OK, écriture dans `Wikidata/batches-generated/`.
5. Stéphane vérifie visuellement le fichier `.qs`.
6. Stéphane transmet à Laura.
7. Laura colle dans QuickStatements, vérifie le preview, exécute.

## Garde-fous intégrés

Le module `validators.py` bloque la génération si :

- **P9934 utilisé comme qualifier ou source** (bug Phase A 2026-05-12 reproduit)
- **P407 utilisé comme qualifier de P356** (bug Phase B 2026-05-12 reproduit)
- **Format DOI/ISBN invalide**

Warnings non bloquants :
- Plusieurs P356 sur le même item (recommande P953 pour les variantes)

## Tests

```powershell
cd Wikidata\scripts
python -m unittest tests.test_validators
```

## Évolutions futures

- Générateur `recension.py` : pour ajouter des références sur des items existants
  sans créer de nouvel item.
- Mode `--check` : compare `data/works.yaml` à un index local pour identifier
  les publications non encore traitées.
- Intégration `data/works.yaml` comme source de vérité unifiée.

## Limitations

- Les Q-IDs des sujets non encore listés dans `config.py` doivent être ajoutés
  manuellement (avec vérification sur wikidata.org).
- La création d'item dépend de l'absence de doublon — vérification via
  `https://hub.toolforge.org/P356:[DOI]` reste à faire manuellement par Laura.
