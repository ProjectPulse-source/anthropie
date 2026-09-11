# Wikidata — compte rendu *Sociologie du travail* (Pugh) : item à créer

> ⏳ **Statut au 2026-09-11 : préparé, NON envoyé — en attente du DOI.**
> Le compte rendu est en ligne depuis le 09/09 (https://journals.openedition.org/sdt/50224),
> mais **aucun article du numéro 68-2 ne porte encore de DOI**, alors que la revue en dépose
> chez Crossref (article Girard-Chanudet 2025 : `10.4000/14pg5`). Les deux comptes rendus du
> même type déjà créés sur OpenEdition portent leur `P356` (Q141072264, Q141072265) : créer
> celui-ci sans DOI obligerait Laura à repasser.
>
> **Déclencheur, un prédicat et non une date** : la commande ci-dessous rend un DOI. Alors,
> ajouter au lot la ligne `LAST	P356	"<DOI EN MAJUSCULES>"`, vérifier `P577` contre la notice
> Crossref, générer le lien direct, envoyer à Laura.

```
curl -s "https://api.crossref.org/works?query.author=Lalut&filter=prefix:10.4000&rows=50&select=DOI,title"
```

Lecture : chercher « Last Human Job » dans les titres rendus. **Témoin** : la même réponse
doit contenir le compte rendu Kaba `10.4000/162f0` (le 11/09 : 2 résultats, Kaba et Ridde).
Sans ce témoin, une absence ne vaut pas « pas encore de DOI ». La forme courte de la
commande est la ligne de reprise du `HANDOFF.md` de pilotage, bloc du 11/09.

⚠ Ne pas y ajouter `query.bibliographic` : chaque champ `query.*` de Crossref agit comme une
condition. Avec `query.bibliographic=Pugh+Last+Human+Job`, la requête rend **0**, avant comme
après la parution du DOI, et le témoin Kaba disparaît avec elle ; un premier jet de ce dossier
l'affirmait pourtant présent.

## Ce qui sera créé — lot `batch_quickstatements.txt`

Modèle : Q141072264 (compte rendu Kaba, *Lectures*, OpenEdition), structure relue à l'API le 11/09.

| Propriété | Valeur | Source |
|---|---|---|
| `P31` | Q637866 (compte rendu) | modèle |
| `P50` | Q138909233 | item auteur |
| `P407` | Q150 (français) | balise `DC.language` de la page |
| `P1433` | **Q15708759** *Sociologie du travail* | ISSN 0038-0296 et 1777-5701 relus sur l'item, identiques à ceux de la page |
| `P478` / `P433` | `68` / `2` | balises `prism.volume` / `prism.number` |
| `P577` | 2026-09-09 | « mis en ligne le 09 septembre 2026 », bloc « Pour citer ». ⚠ Les balises DC/citation de la même page portent 2026-09-10 : la notice Crossref tranchera, et si elle dit 10, corriger ici **et** dans `data/works.yaml` |
| `P953` | https://journals.openedition.org/sdt/50224 | page de **consultation**, jamais `/sdt/pdf/50224` : demande expresse de l'éditrice (licence CC BY-NC-ND, « renvoyer vos lecteurices vers la page de consultation ») |
| `P1476` | fr : titre de la page | `DC.title` |
| `P921` | Q140734883 *The Last Human Job* | item existant ; **ajout** par rapport au modèle *Lectures*, qui ne portait pas l'œuvre recensée |
| `P275` | Q24082749 CC BY-NC-ND 4.0 | mention « Droits d'auteur » de la page ; **ajout** par rapport au modèle |
| `P356` | DOI | **à ajouter au déclenchement** |

Aucun doublon au 11/09 : `haswbstatement:P50=Q138909233 Pugh` → 0 résultat.

## Après exécution

1. Readback API de l'item créé (fichier `readback_api_<date>.txt` dans ce dossier).
2. Écriture en retour : `wikidata:` sur `art-sdt-pugh-2026-09` dans `data/works.yaml`,
   `wikidata_qid` sur `content/publications/sociologie-du-travail-pugh.md` (alimente le `sameAs`
   de l'`ItemList`), et le `doi` sur les deux.
3. `python scripts/check-wikidata-registre.py` → 0.
4. Bloc ✅ en tête de ce fichier : QID rendu, commit d'écriture en retour, sortie du script.
