# Wikidata — compte rendu *Sociologie du travail* (Pugh) : item à créer

> ✅ **FAIT le 2026-09-11 à 20:09 UTC, exécuté par Laura — item [Q141435769](https://www.wikidata.org/wiki/Q141435769)**,
> révision 2544165666. Readback API du 11/09 (`readback_api_2026-09-11.json`, dans ce dossier) : les
> 12 déclarations du lot, toutes conformes, labels et descriptions fr/en identiques au lot.
> Écriture en retour dans le même commit que ce bloc : `wikidata: "Q141435769"` sur
> `art-sdt-pugh-2026-09` (`data/works.yaml`), `wikidata_qid` sur la fiche ; `check-wikidata-registre.py`
> et `check-fiches-registre.py` relancés à 0 avant commit.
>
> Historique de l'envoi : **prêt à envoyer le 11/09 au soir.** Le DOI est paru chez Crossref le 11/09 à 18:54 UTC :
> `10.4000/16rju`. Notice relue : titre exact, *Sociologie du travail* 68 n° 2, auteur rattaché à
> l'ORCID de l'auteur, licence CC BY-NC-ND ; `doi.org` redirige vers la page de consultation. La ligne
> `P356` est au lot, DOI en majuscules comme Wikidata les stocke ; `deeplink_New.txt` porte le lien direct (renommé à l'envoi le 11/09, contenu identique à l'octet au `deeplink.txt` d'origine).
> Aucun item ne porte ce DOI au 11/09 : `haswbstatement:P356=10.4000/16RJU` → 0, avec le témoin Kaba
> (`P356=10.4000/162F0` → Q141072264) qui répond. **Envoi à Laura : geste auteur.**

Historique : préparé le 11/09 dans l'après-midi en attente du DOI, aucun article du numéro n'en
portant encore. Les deux comptes rendus OpenEdition déjà créés portent leur `P356` (Q141072264,
Q141072265) : créer celui-ci sans DOI aurait obligé Laura à repasser. Le DOI a paru quelques heures
plus tard, deux jours après la mise en ligne.

## Contrôle d'un DOI chez Crossref — la forme qui a un témoin

```
curl -s "https://api.crossref.org/works?query.author=Lalut&filter=prefix:10.4000&rows=50&select=DOI,title"
```

Chercher le titre dans les résultats. **Témoin** : la même réponse doit contenir le compte rendu Kaba
`10.4000/162f0`, faute de quoi une absence ne vaut pas « pas encore de DOI ».

⚠ Ne pas y ajouter `query.bibliographic` : chaque champ `query.*` de Crossref agit comme une
condition. Avec `query.bibliographic=Pugh+Last+Human+Job`, la requête rendait **0** avant comme
après la parution, et le témoin disparaissait avec elle ; un premier jet de ce dossier l'affirmait
pourtant présent.

## Ce qui sera créé — lot `batch_quickstatements.txt`

Modèle : Q141072264 (compte rendu Kaba, *Lectures*, OpenEdition), structure relue à l'API le 11/09.

| Propriété | Valeur | Source |
|---|---|---|
| `P31` | Q637866 (compte rendu) | modèle |
| `P50` | Q138909233 | item auteur |
| `P407` | Q150 (français) | balise `DC.language` de la page |
| `P1433` | **Q15708759** *Sociologie du travail* | ISSN 0038-0296 et 1777-5701 relus sur l'item, identiques à ceux de la page et de la notice Crossref |
| `P478` / `P433` | `68` / `2` | notice Crossref, balises `prism` de la page |
| `P577` | 2026-09-09 | « mis en ligne le 09 septembre 2026 », bloc « Pour citer ». La notice Crossref ne porte que l'année ; les balises DC de la page portent le 10 |
| `P953` | https://journals.openedition.org/sdt/50224 | page de **consultation**, jamais `/sdt/pdf/50224` : demande expresse de l'éditrice (licence CC BY-NC-ND, « renvoyer vos lecteurices vers la page de consultation ») |
| `P1476` | fr : titre de la page | `DC.title` |
| `P921` | Q140734883 *The Last Human Job* | item existant ; **ajout** par rapport au modèle *Lectures*, qui ne portait pas l'œuvre recensée |
| `P275` | Q24082749 CC BY-NC-ND 4.0 | mention « Droits d'auteur » de la page, licence de la notice Crossref ; **ajout** par rapport au modèle |
| `P356` | `10.4000/16RJU` | notice Crossref, déposée le 11/09 à 18:54 UTC |

## Après exécution

1. Readback API de l'item créé (fichier `readback_api_<date>.txt` dans ce dossier).
2. Écriture en retour : `wikidata:` sur `art-sdt-pugh-2026-09` dans `data/works.yaml` et
   `wikidata_qid` sur `content/publications/sociologie-du-travail-pugh.md` (alimente le `sameAs` de
   l'`ItemList`). Le `doi` y est déjà, depuis le 11/09.
3. `python scripts/check-wikidata-registre.py` → 0.
4. Bloc ✅ en tête de ce fichier : QID rendu, commit d'écriture en retour, sortie du script.
